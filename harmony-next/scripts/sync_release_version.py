from __future__ import annotations

import argparse
import re
from pathlib import Path


VERSION_PATTERN = re.compile(r"^v?(\d+\.\d+\.\d+)$")


def normalize_version(raw_version: str) -> tuple[str, str]:
    value = raw_version.strip()
    if value.startswith("refs/tags/"):
        value = value.removeprefix("refs/tags/")

    match = VERSION_PATTERN.fullmatch(value)
    if not match:
        raise ValueError(f"Expected version like 1.2.3 or v1.2.3, got: {raw_version!r}")

    bare = match.group(1)
    return bare, f"v{bare}"


def replace_once(text: str, pattern: str, replacement: str, label: str) -> str:
    updated, count = re.subn(pattern, replacement, text, count=1, flags=re.MULTILINE)
    if count != 1:
        raise ValueError(f"Could not update {label}")
    return updated


def replace_once_if_present(text: str, pattern: str, replacement: str) -> tuple[str, bool]:
    updated, count = re.subn(pattern, replacement, text, count=1, flags=re.MULTILINE)
    return updated, count == 1


def sync_skill(skill_path: Path, bare_version: str, tag_version: str) -> None:
    text = skill_path.read_text(encoding="utf-8")
    text = replace_once(
        text,
        r'(^  version: ")(\d+\.\d+\.\d+)(")',
        rf"\g<1>{bare_version}\3",
        "SKILL.md metadata.version",
    )
    text = replace_once(
        text,
        r"(Current local skill version:\s*`)v\d+\.\d+\.\d+(`\.)",
        rf"\g<1>{tag_version}\2",
        "SKILL.md visible version",
    )
    text = replace_once(
        text,
        r"(<!-- version:\s*)\d+\.\d+\.\d+(\s*-->)",
        rf"\g<1>{bare_version}\2",
        "SKILL.md hidden version",
    )
    skill_path.write_text(text, encoding="utf-8")


def sync_dsh_bundle(package_path: Path, bare_version: str) -> None:
    text = package_path.read_text(encoding="utf-8")
    text = replace_once(
        text,
        r'(^  "version": ")(\d+\.\d+\.\d+)(",$)',
        rf"\g<1>{bare_version}\3",
        "package.json version",
    )
    package_path.write_text(text, encoding="utf-8")


def sync_readme(readme_path: Path, tag_version: str) -> None:
    text = readme_path.read_text(encoding="utf-8")
    text = replace_once(
        text,
        r"^(\|\s*`)v\d+\.\d+\.\d+(`\s*\|)",
        rf"\g<1>{tag_version}\2",
        f"{readme_path.name} current version highlight",
    )
    text, badge_replaced = replace_once_if_present(
        text,
        r"(badge/release-)v\d+\.\d+\.\d+(-1f6feb)",
        rf"\g<1>{tag_version}\2",
    )
    if not badge_replaced and "https://img.shields.io/github/v/release/linhay/harmony-next.skills?style=flat-square" not in text:
        raise ValueError(f"Could not update {readme_path.name} release badge")

    text, link_replaced = replace_once_if_present(
        text,
        r"(releases/tag/)v\d+\.\d+\.\d+",
        rf"\g<1>{tag_version}",
    )
    if not link_replaced and "https://github.com/linhay/harmony-next.skills/releases/latest" not in text:
        raise ValueError(f"Could not update {readme_path.name} release link")

    readme_path.write_text(text, encoding="utf-8")


def sync_release_version(root: Path, raw_version: str) -> tuple[str, str]:
    bare_version, tag_version = normalize_version(raw_version)
    sync_skill(root / "harmony-next" / "SKILL.md", bare_version, tag_version)
    sync_dsh_bundle(root / "package.json", bare_version)
    sync_readme(root / "README.md", tag_version)
    sync_readme(root / "README_en.md", tag_version)
    return bare_version, tag_version


def main() -> None:
    parser = argparse.ArgumentParser(description="Sync release version metadata before packaging.")
    parser.add_argument("--version", required=True, help="Release version, e.g. 1.2.3 or v1.2.3")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2])
    args = parser.parse_args()

    bare_version, tag_version = sync_release_version(args.root, args.version)
    print(f"Synced release version: {tag_version} ({bare_version})")


if __name__ == "__main__":
    main()
