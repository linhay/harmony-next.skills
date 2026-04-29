#!/usr/bin/env python3
from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path


OLD_HEADER_LINK_PATTERN = re.compile(r"\]\((\.\./\.\./capi/headers/([^)#]+\.md))((?:#[^)]+)?)\)")
INTERNAL_MD_LINK_PATTERN = re.compile(r"\[([^\]]+)\]\(([^)]+\.md(?:#[^)]+)?)\)")


@dataclass(frozen=True)
class ReferencePaths:
    repo_root: Path
    references_root: Path
    js_api_root: Path
    old_headers_root: Path
    references_index: Path
    js_index: Path


@dataclass(frozen=True)
class ResidualLinkCandidate:
    file_rel: str
    label: str
    target: str
    classification: str


def build_paths(repo_root: Path) -> ReferencePaths:
    references_root = repo_root / "references"
    js_api_root = references_root / "JsEtsAPIReference"
    return ReferencePaths(
        repo_root=repo_root,
        references_root=references_root,
        js_api_root=js_api_root,
        old_headers_root=js_api_root / "capi" / "headers",
        references_index=references_root / "INDEX.md",
        js_index=js_api_root / "INDEX.md",
    )


DEFAULT_PATHS = build_paths(Path(__file__).resolve().parents[1])


def build_header_mapping(paths: ReferencePaths) -> dict[str, Path]:
    mapping: dict[str, Path] = {}
    for path in paths.js_api_root.rglob("*.md"):
        rel = path.relative_to(paths.js_api_root)
        if rel.parts[:2] == ("capi", "headers"):
            continue
        if not path.name.endswith(".h.md"):
            continue
        if path.name in mapping:
            raise RuntimeError(f"头文件名重复，无法重写旧引用: {path.name}")
        mapping[path.name] = rel
    return mapping


def build_index_entries(paths: ReferencePaths) -> list[str]:
    return sorted(
        str(path.relative_to(paths.js_api_root)).replace("\\", "/")
        for path in paths.js_api_root.rglob("*.md")
        if path.relative_to(paths.js_api_root).parts[:2] != ("capi", "headers")
        if path.name != "INDEX.md"
    )


def build_references_index_entries(paths: ReferencePaths) -> list[str]:
    return sorted(
        str(path.relative_to(paths.references_root)).replace("\\", "/")
        for path in paths.references_root.rglob("*.md")
        if path.name != "INDEX.md"
    )


def generate_index(paths: ReferencePaths) -> None:
    entries = build_index_entries(paths)
    if not entries:
        raise RuntimeError("未从 JsEtsAPIReference/ 目录扫描到任何 Markdown 条目")
    paths.js_index.parent.mkdir(parents=True, exist_ok=True)
    paths.js_index.write_text("\n".join(entries) + "\n", encoding="utf-8")


def generate_references_index(paths: ReferencePaths) -> None:
    entries = build_references_index_entries(paths)
    if not entries:
        raise RuntimeError("未从 references/ 目录扫描到任何 Markdown 条目")
    paths.references_index.parent.mkdir(parents=True, exist_ok=True)
    paths.references_index.write_text("\n".join(entries) + "\n", encoding="utf-8")


def rewrite_header_links(paths: ReferencePaths) -> int:
    mapping = build_header_mapping(paths)
    rewritten_files = 0

    for path in paths.js_api_root.rglob("*.md"):
        rel = path.relative_to(paths.js_api_root)
        if rel.parts[:2] == ("capi", "headers"):
            continue
        original = path.read_text(encoding="utf-8")

        def repl(match: re.Match[str]) -> str:
            name = match.group(2)
            anchor = match.group(3)
            target = mapping.get(name)
            if target is None:
                raise RuntimeError(f"找不到头文件新路径: {name}")
            return f"](../../{target.as_posix()}{anchor})"

        updated = OLD_HEADER_LINK_PATTERN.sub(repl, original)
        if updated != original:
            path.write_text(updated, encoding="utf-8")
            rewritten_files += 1

    return rewritten_files


def list_changed_markdown_files(paths: ReferencePaths) -> list[str]:
    raw = subprocess.check_output(
        ["git", "diff", "--name-only", "-z", "--", str(paths.js_api_root.relative_to(paths.repo_root))],
        cwd=paths.repo_root,
    )
    return [
        item.decode("utf-8")
        for item in raw.split(b"\x00")
        if item and item.decode("utf-8").endswith(".md") and not item.decode("utf-8").endswith("INDEX.md")
    ]


def extract_head_links(paths: ReferencePaths, file_rel: str) -> list[tuple[str, str]]:
    try:
        old_text = subprocess.check_output(
            ["git", "show", f"HEAD:{file_rel}"],
            cwd=paths.repo_root,
            text=True,
            stderr=subprocess.DEVNULL,
        )
    except subprocess.CalledProcessError:
        return []
    seen: set[tuple[str, str]] = set()
    links: list[tuple[str, str]] = []
    for item in INTERNAL_MD_LINK_PATTERN.findall(old_text):
        if item not in seen:
            seen.add(item)
            links.append(item)
    return links


def classify_residual(text: str, label: str, target: str) -> str:
    if f"[{label}](" in text:
        return "linked"
    if label not in text:
        return "missing_label"
    if target.startswith("http://") or target.startswith("https://"):
        return "external_link"
    if "../../guides/" in target:
        return "historical_missing_guides_link"

    in_code = False
    saw_noncode = False
    saw_actionable_noncode = False
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("```"):
            in_code = not in_code
            continue
        if label not in line:
            continue
        if in_code:
            continue
        saw_noncode = True
        if line.lstrip().startswith("|") or stripped.startswith("- ") or stripped.startswith("* "):
            saw_actionable_noncode = True
            break
        if re.search(rf"(?<![\w`]){re.escape(label)}(?![\w`])", line):
            saw_actionable_noncode = True
            break

    if saw_actionable_noncode:
        return "actionable_internal_link"
    if saw_noncode:
        return "noncode_ambiguous"
    return "code_or_signature_false_positive"


def audit_removed_links(paths: ReferencePaths) -> list[ResidualLinkCandidate]:
    candidates: list[ResidualLinkCandidate] = []
    for file_rel in list_changed_markdown_files(paths):
        file_path = paths.repo_root / file_rel
        if not file_path.exists():
            continue
        text = file_path.read_text(encoding="utf-8")
        for label, target in extract_head_links(paths, file_rel):
            classification = classify_residual(text, label, target)
            if classification == "linked":
                continue
            candidates.append(ResidualLinkCandidate(file_rel=file_rel, label=label, target=target, classification=classification))
    return candidates


def audit(paths: ReferencePaths) -> int:
    candidates = audit_removed_links(paths)
    actionable = [item for item in candidates if item.classification == "actionable_internal_link"]
    if actionable:
        for item in actionable[:50]:
            print(
                f"残留可行动链接: {item.file_rel} :: {item.label} -> {item.target}",
                file=sys.stderr,
            )
        if len(actionable) > 50:
            print("残留可行动链接超过 50 个", file=sys.stderr)
        return 1

    counts: dict[str, int] = {}
    for item in candidates:
        counts[item.classification] = counts.get(item.classification, 0) + 1
    summary = ", ".join(f"{key}={value}" for key, value in sorted(counts.items()))
    print(f"OK: 无残留可行动内部链接。{summary or 'no residual candidates'}")
    return 0


def iter_old_header_links(paths: ReferencePaths) -> list[tuple[Path, str]]:
    matches: list[tuple[Path, str]] = []
    for path in paths.js_api_root.rglob("*.md"):
        rel = path.relative_to(paths.js_api_root)
        if rel.parts[:2] == ("capi", "headers"):
            continue
        text = path.read_text(encoding="utf-8")
        for link, _, _ in OLD_HEADER_LINK_PATTERN.findall(text):
            matches.append((path, link))
    return matches


def check(paths: ReferencePaths) -> int:
    errors: list[str] = []

    if paths.old_headers_root.exists():
        leftovers = sorted(p.relative_to(paths.repo_root) for p in paths.old_headers_root.rglob("*.md"))
        if leftovers:
            for leftover in leftovers[:20]:
                errors.append(f"残留旧头文件页: {leftover}")
            if len(leftovers) > 20:
                errors.append("残留旧头文件页超过 20 个")

    if not paths.js_index.exists():
        errors.append(f"缺少索引: {paths.js_index}")
    else:
        actual_entries = build_index_entries(paths)
        indexed_entries = [line.strip() for line in paths.js_index.read_text(encoding="utf-8").splitlines() if line.strip()]
        if indexed_entries != actual_entries:
            actual_set = set(actual_entries)
            indexed_set = set(indexed_entries)
            for item in sorted(actual_set - indexed_set)[:20]:
                errors.append(f"索引缺项: {item}")
            for item in sorted(indexed_set - actual_set)[:20]:
                errors.append(f"索引陈旧项: {item}")
            if len(actual_set - indexed_set) > 20 or len(indexed_set - actual_set) > 20:
                errors.append("索引与文件系统不一致，且差异条目超过 20 个")

    if not paths.references_index.exists():
        errors.append(f"缺少全库索引: {paths.references_index}")
    else:
        actual_entries = build_references_index_entries(paths)
        indexed_entries = [line.strip() for line in paths.references_index.read_text(encoding="utf-8").splitlines() if line.strip()]
        if indexed_entries != actual_entries:
            actual_set = set(actual_entries)
            indexed_set = set(indexed_entries)
            for item in sorted(actual_set - indexed_set)[:20]:
                errors.append(f"全库索引缺项: {item}")
            for item in sorted(indexed_set - actual_set)[:20]:
                errors.append(f"全库索引陈旧项: {item}")
            if len(actual_set - indexed_set) > 20 or len(indexed_set - actual_set) > 20:
                errors.append("全库索引与文件系统不一致，且差异条目超过 20 个")

    for source, link in iter_old_header_links(paths):
        errors.append(f"残留旧路径引用: {source.relative_to(paths.repo_root)} -> {link}")

    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1

    print("OK: 索引存在，且无残留旧头文件页或旧路径引用。")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "维护 HarmonyOS NEXT 参考库迁移后的链接与索引。"
            "generate 负责重写旧头文件引用并重建索引；"
            "check 负责校验磁盘与索引一致；"
            "audit 负责扫描当前改动里被抹掉的内部 Markdown 链接。"
        )
    )
    parser.add_argument(
        "command",
        choices=("generate", "check", "audit"),
        help="generate: 重写旧链接并重建索引；check: 校验索引与旧路径残留；audit: 扫描当前改动里被移除的内部链接。",
    )
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=DEFAULT_PATHS.repo_root,
        help="目标仓库根目录，需要包含 references/JsEtsAPIReference。",
    )
    args = parser.parse_args()
    paths = build_paths(args.repo_root.resolve())

    if args.command == "generate":
        rewritten = rewrite_header_links(paths)
        generate_references_index(paths)
        generate_index(paths)
        print(
            f"Generated {paths.references_index.relative_to(paths.repo_root)} and "
            f"{paths.js_index.relative_to(paths.repo_root)}; rewrote {rewritten} files"
        )
        return 0
    if args.command == "audit":
        return audit(paths)
    return check(paths)


if __name__ == "__main__":
    raise SystemExit(main())
