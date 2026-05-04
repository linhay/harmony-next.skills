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
TARGETED_GUIDE_LINK_PATTERN = re.compile(
    r"\]\((https://developer\.huawei\.com/consumer/cn/doc/harmonyos-guides/([^)#]+))((?:#[^)]+)?)\)"
)
INTERNAL_MD_LINK_PATTERN = re.compile(r"\[([^\]]+)\]\(([^)]+\.md(?:#[^)]+)?)\)")

@dataclass(frozen=True)
class TargetedGuideMapping:
    target: Path
    default_anchor: str | None = None
    preserve_source_anchor: bool = True


# 仅覆盖仓库已经决定离线化的 guide，避免批量替换大量仍保留在线引用的文档。
TARGETED_GUIDE_MAPPING = {
    "arkts-v1-v2-guide": TargetedGuideMapping(Path("guides/状态管理V1-V2迁移指导.md")),
    "arkts-v1-v2-migration": TargetedGuideMapping(Path("guides/状态管理V1-V2迁移指导.md")),
    "arkts-state-management-v1-v2-migration-guide": TargetedGuideMapping(
        Path("guides/状态管理V1-V2迁移指导.md"),
        "#状态管理V1向V2迁移场景",
    ),
    "arkts-v1-v2-migration-inner-component": TargetedGuideMapping(
        Path("guides/状态管理V1-V2迁移指导.md"),
        "#组件内状态变量迁移",
    ),
    "arkts-v1-v2-migration-inner-class": TargetedGuideMapping(
        Path("guides/状态管理V1-V2迁移指导.md"),
        "#数据对象状态变量迁移",
    ),
    "arkts-v1-v2-migration-inner-object": TargetedGuideMapping(Path("guides/状态管理V1-V2迁移指导.md")),
    "arkts-v1-v2-mixusage": TargetedGuideMapping(Path("guides/状态管理V1和V2混用指导（API version 19及之后）.md")),
    "arkts-new-makeobserved": TargetedGuideMapping(Path("guides/makeObserved接口：将非观察数据变为可观察数据.md")),
    "arkts-state-management-overview": TargetedGuideMapping(Path("guides/状态管理概述.md")),
    "arkts-state-management-introduce": TargetedGuideMapping(
        Path("guides/状态管理概述.md"),
        preserve_source_anchor=False,
    ),
    "arkts-observed-and-objectlink": TargetedGuideMapping(Path("guides/@Observed与@ObjectLink：V1数据对象观测.md")),
    "arkts-new-observedv2-and-trace": TargetedGuideMapping(Path("guides/@ObservedV2与@Trace：类属性变化观测.md")),
    "arkts-new-addmonitor-clearmonitor": TargetedGuideMapping(Path("guides/addMonitor与clearMonitor开发指南.md")),
    "arkts-new-applysync-flushupdates-flushuiupdates": TargetedGuideMapping(
        Path("guides/applySync与flushUpdates与flushUIUpdates接口：同步刷新.md")
    ),
    "arkts-env-system-property": TargetedGuideMapping(Path("topics/components/@Env：环境变量.md")),
    "arkts-new-appstoragev2": TargetedGuideMapping(Path("guides/AppStorageV2（应用全局的UI状态存储）.md")),
    "arkts-new-persistencev2": TargetedGuideMapping(Path("guides/PersistenceV2（持久化存储UI状态）.md")),
    "arkts-watch": TargetedGuideMapping(Path("topics/components/状态变量变化监听.md"), preserve_source_anchor=False),
    "arkts-new-monitor": TargetedGuideMapping(Path("topics/components/状态变量变化监听.md"), preserve_source_anchor=False),
    "arkts-appstorage": TargetedGuideMapping(Path("topics/components/应用级变量的状态管理.md"), preserve_source_anchor=False),
    "arkts-localstorage": TargetedGuideMapping(Path("topics/components/应用级变量的状态管理.md"), preserve_source_anchor=False),
    "arkts-persiststorage": TargetedGuideMapping(Path("topics/components/应用级变量的状态管理.md"), preserve_source_anchor=False),
    "arkts-state": TargetedGuideMapping(
        Path("modules/ohos/@ohos.arkui.StateManagement (状态管理).md"),
        preserve_source_anchor=False,
    ),
    "arkts-state-management-glossary": TargetedGuideMapping(
        Path("modules/ohos/@ohos.arkui.StateManagement (状态管理).md"),
        preserve_source_anchor=False,
    ),
    "arkts-provide-and-consume": TargetedGuideMapping(
        Path("modules/ohos/@ohos.arkui.StateManagement (状态管理).md"),
        preserve_source_anchor=False,
    ),
    "arkts-rendering-control-foreach": TargetedGuideMapping(
        Path("topics/components/ForEach.md"),
        preserve_source_anchor=False,
    ),
    "arkts-rendering-control-lazyforeach": TargetedGuideMapping(
        Path("topics/components/LazyForEach.md"),
        preserve_source_anchor=False,
    ),
    "arkts-new-rendering-control-repeat": TargetedGuideMapping(
        Path("topics/components/Repeat.md"),
        preserve_source_anchor=False,
    ),
    "arkts-mutablebuilder": TargetedGuideMapping(
        Path("topics/components/mutableBuilder.md"),
        preserve_source_anchor=False,
    ),
    "arkts-user-defined-arktsnode-buildernode": TargetedGuideMapping(
        Path("topics/misc/BuilderNode.md"),
        preserve_source_anchor=False,
    ),
    "arkts-create-custom-components": TargetedGuideMapping(
        Path("topics/components/自定义组件.md"),
        preserve_source_anchor=False,
    ),
    "arkts-page-custom-components-lifecycle": TargetedGuideMapping(
        Path("topics/components/自定义组件的生命周期.md"),
        preserve_source_anchor=False,
    ),
    "arkts-global-interface": TargetedGuideMapping(
        Path("types/classes/Class (UIContext).md"),
        preserve_source_anchor=False,
    ),
    "arkts-routing": TargetedGuideMapping(
        Path("types/classes/Class (Router).md"),
        preserve_source_anchor=False,
    ),
    "arkts-common-components-text-input": TargetedGuideMapping(
        Path("topics/components/TextInput.md"),
        preserve_source_anchor=False,
    ),
    "arkts-common-events-focus-event": TargetedGuideMapping(
        Path("topics/components/焦点事件.md"),
        preserve_source_anchor=False,
    ),
    "pastebutton": TargetedGuideMapping(
        Path("topics/components/PasteButton.md"),
        preserve_source_anchor=False,
    ),
    "window-terminology": TargetedGuideMapping(Path("guides/窗口开发术语.md")),
    "uiability-usage": TargetedGuideMapping(Path("guides/UIAbility组件基本用法.md")),
    "module-configuration-file": TargetedGuideMapping(Path("guides/module.json5配置文件.md")),
    "app-startup": TargetedGuideMapping(Path("guides/应用启动框架AppStartup.md")),
    "arkts-sendable": TargetedGuideMapping(Path("guides/Sendable对象简介.md")),
    "arkts-builder": TargetedGuideMapping(Path("guides/@Builder装饰器：自定义构建函数.md")),
    "arkts-two-way-sync": TargetedGuideMapping(Path("guides/$$语法：系统组件双向同步.md")),
    "arkts-new-binding": TargetedGuideMapping(Path("guides/!!语法：双向绑定.md")),
    "arkts-rendering-control-ifelse": TargetedGuideMapping(Path("guides/if-else：条件渲染.md")),
    "data-backup-and-restore": TargetedGuideMapping(Path("guides/数据库备份与恢复.md")),
    "mdm-kit-multi-mdm": TargetedGuideMapping(Path("guides/多应用管控.md")),
    "terminology": TargetedGuideMapping(Path("guides/Connectivity Kit术语.md")),
    "component-startup-rules": TargetedGuideMapping(Path("guides/组件启动规则（Stage模型）.md")),
    "mdm-kit-guide": TargetedGuideMapping(Path("guides/MDM Kit开发指南.md")),
    "declare-permissions-in-acl": TargetedGuideMapping(Path("guides/申请受限权限.md")),
    "push-jwt-token": TargetedGuideMapping(Path("guides/基于服务账号生成鉴权令牌.md")),
    "data-persistence-by-kv-store": TargetedGuideMapping(Path("guides/通过键值型数据库实现数据持久化.md")),
    "declare-permissions": TargetedGuideMapping(Path("guides/声明权限.md")),
    "ability-terminology": TargetedGuideMapping(Path("guides/Ability Kit术语.md")),
    "application-context-stage": TargetedGuideMapping(Path("guides/应用上下文Context.md")),
    "app-configuration-file": TargetedGuideMapping(Path("guides/app.json5配置文件.md")),
    "component-startup-rules-fa": TargetedGuideMapping(Path("guides/组件启动规则（FA模型）.md")),
}


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


def build_relative_link(source: Path, target: Path) -> str:
    return Path(os.path.relpath(target, start=source.parent)).as_posix()


def rewrite_targeted_guide_links(paths: ReferencePaths) -> int:
    rewritten_files = 0

    for path in paths.js_api_root.rglob("*.md"):
        rel = path.relative_to(paths.js_api_root)
        if rel.parts[:2] == ("capi", "headers"):
            continue
        original = path.read_text(encoding="utf-8")

        def repl(match: re.Match[str]) -> str:
            slug = match.group(2)
            anchor = match.group(3)
            mapping = TARGETED_GUIDE_MAPPING.get(slug)
            if mapping is None:
                return match.group(0)
            if anchor and mapping.preserve_source_anchor:
                resolved_anchor = anchor
            else:
                resolved_anchor = mapping.default_anchor or ""
            relative = build_relative_link(path, paths.js_api_root / mapping.target)
            return f"]({relative}{resolved_anchor})"

        updated = TARGETED_GUIDE_LINK_PATTERN.sub(repl, original)
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


def iter_targeted_guide_links(paths: ReferencePaths) -> list[tuple[Path, str]]:
    matches: list[tuple[Path, str]] = []
    for path in paths.js_api_root.rglob("*.md"):
        rel = path.relative_to(paths.js_api_root)
        if rel.parts[:2] == ("capi", "headers"):
            continue
        text = path.read_text(encoding="utf-8")
        for full_url, slug, anchor in TARGETED_GUIDE_LINK_PATTERN.findall(text):
            if slug in TARGETED_GUIDE_MAPPING:
                matches.append((path, f"{full_url}{anchor}"))
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
    for source, link in iter_targeted_guide_links(paths):
        errors.append(f"残留目标 guide 外链: {source.relative_to(paths.repo_root)} -> {link}")

    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1

    print("OK: 索引存在，且无残留旧头文件页、旧路径引用或目标 guide 外链。")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "维护 HarmonyOS NEXT 参考库迁移后的链接与索引。"
            "generate 负责重写旧头文件引用、目标 guide 外链并重建索引；"
            "check 负责校验索引与目标外链残留；"
            "audit 负责扫描当前改动里被抹掉的内部 Markdown 链接。"
        )
    )
    parser.add_argument(
        "command",
        choices=("generate", "check", "audit"),
        help="generate: 重写旧链接并重建索引；check: 校验索引与残留旧路径或目标 guide 外链；audit: 扫描当前改动里被移除的内部链接。",
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
        guide_rewritten = rewrite_targeted_guide_links(paths)
        generate_references_index(paths)
        generate_index(paths)
        print(
            f"Generated {paths.references_index.relative_to(paths.repo_root)} and "
            f"{paths.js_index.relative_to(paths.repo_root)}; rewrote {rewritten} header-link files "
            f"and {guide_rewritten} guide-link files"
        )
        return 0
    if args.command == "audit":
        return audit(paths)
    return check(paths)


if __name__ == "__main__":
    raise SystemExit(main())
