#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


INSTALL_FRAGMENTS = [
    "npx skills add linhay/harmony-next.skills",
    "npx skills add linhay/harmony-next.skills --list",
    "gemini skills install https://github.com/linhay/harmony-next.skills --path harmony-next --scope user",
    "npx skills add linhay/harmony-next.skills --skill harmony-next -a claude-code -g -y --copy",
    "npx skills add linhay/harmony-next.skills --skill harmony-next -a codex -g -y --copy",
    "$HOME/.agents/skills/harmony-next",
    "DSH_SOURCE=/path/to/harmony-next.skills",
    ".dsh/skills/harmony-next",
    "dsh plugin --profile demo add github:linhay/harmony-next.skills",
    "dsh-harmony-next",
]

PORTABILITY_FRAGMENTS = [
    "harmony-next/SKILL.md",
    "npx skills add linhay/harmony-next.skills --skill harmony-next -a claude-code -g -y --copy",
    "npx skills add linhay/harmony-next.skills --skill harmony-next -a codex -g -y --copy",
    "harmony-next.skill.zip",
    "not a Codex plugin",
    "dsh-skill-filesystem",
    "$HOME/.dsh/skills/harmony-next",
    "dsh.bundle.patch",
    "dsh.bundle",
    "cordis.patch.yml",
    "dsh plugin --profile demo add",
]

SMOKE_CASES = [
    (
        "ArkUI Button",
        ["harmony-next/references/TASK_MAP.md", "harmony-next/references/JsEtsAPIReference/topics/components/Button.md"],
        ["dumpLayout", "uiInput click", "blocked"],
    ),
    (
        "UIAbility / Want",
        [
            "harmony-next/references/KITS.md",
            "harmony-next/references/JsEtsAPIReference/modules/ohos/@ohos.app.ability.UIAbility (带界面的应用组件).md",
            "harmony-next/references/JsEtsAPIReference/guides/启动应用内的UIAbility组件.md",
        ],
        ["aa start", "hilog", "blocked"],
    ),
    (
        "Network HTTP / Socket",
        [
            "harmony-next/references/TASK_MAP.md",
            "harmony-next/references/JsEtsAPIReference/modules/ohos/@ohos.net.http (数据请求).md",
            "harmony-next/references/JsEtsAPIReference/modules/ohos/@ohos.net.socket (Socket连接).md",
        ],
        ["网络权限", "endpoint", "blocked"],
    ),
    (
        "Data RDB / Preferences",
        [
            "harmony-next/references/KITS.md",
            "harmony-next/references/JsEtsAPIReference/modules/ohos/@ohos.data.rdb (关系型数据库).md",
            "harmony-next/references/JsEtsAPIReference/topics/misc/Preferences.md",
        ],
        ["ArkTS API", "C API", "blocked"],
    ),
    (
        "Command Line Tools",
        [
            "harmony-next/SKILL.md",
            "harmony-next/references/ideGuides/独立命令行工具配置手册.md",
            "harmony-next/references/ideGuides/命令行工具指南.md",
        ],
        ["commandline_tools_manager.py doctor", "blocked"],
    ),
    (
        "NDK Node-API",
        [
            "harmony-next/references/ndkGuides/NDK开发与Node-API指南.md",
            "harmony-next/references/JsEtsAPIReference/topics/misc/Node-API.md",
            "harmony-next/references/JsEtsAPIReference/topics/misc/native_node_napi.h.md",
        ],
        ["libace_napi.z.so", "externalNativeBuild", "assembleHap", "blocked"],
    ),
    (
        "Testing / Publishing / Security",
        [
            "harmony-next/references/testing/应用测试与Hypium指南.md",
            "harmony-next/references/ideGuides/应用签名指南.md",
            "harmony-next/references/JsEtsAPIReference/guides/声明权限.md",
        ],
        ["Hypium", "Profile", "module.json5", "blocked"],
    ),
    (
        "HVD / Emulator",
        ["harmony-next/SKILL.md", "harmony-next/references/ideGuides/DevEco模拟器私有接口与AI自动化.md"],
        ["hvd_manager.py doctor", "blocked"],
    ),
    (
        "Offline UI/UX Audit",
        ["harmony-next/SKILL.md", "harmony-next/references/ideGuides/DevEco Studio IDE私有接口与AI自动化.md"],
        ["ux_audit_pipeline.py doctor", "capture-audit", "audit --evidence-summary", "blocked"],
    ),
    (
        "Profiler Trace",
        ["harmony-next/SKILL.md", "harmony-next/references/performanceAndStandards/性能调优与Profiler指南.md"],
        ["profiler_trace_audit.py doctor", "audit --input", "blocked"],
    ),
]


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def skill_version(skill_text: str) -> str:
    metadata = re.search(r'^\s+version:\s*"(\d+\.\d+\.\d+)"', skill_text, re.MULTILINE)
    visible = re.search(r"Current local skill version:\s*`v(\d+\.\d+\.\d+)`", skill_text)
    hidden = re.search(r"<!-- version:\s*(\d+\.\d+\.\d+)\s*-->", skill_text)
    versions = [match.group(1) for match in [metadata, visible, hidden] if match]
    if len(versions) != 3 or len(set(versions)) != 1:
        raise ValueError("SKILL.md version fields drifted")
    return versions[0]


def require_contains(errors: list[str], label: str, text: str, fragments: list[str]) -> None:
    for fragment in fragments:
        if fragment not in text:
            errors.append(f"{label} missing: {fragment}")


def check_smoke_paths(root: Path, errors: list[str]) -> None:
    smoke_path = root / "docs-linhay" / "spaces" / "20260706-ponytail-portability-plan" / "smoke-set.md"
    if not smoke_path.is_file():
        errors.append("missing smoke-set.md")
        return

    smoke_text = read(smoke_path)
    sections = re.split(r"(?m)^### \d+\. ", smoke_text)[1:]
    if len(sections) != len(SMOKE_CASES):
        errors.append(f"smoke-set.md should define exactly {len(SMOKE_CASES)} questions, found {len(sections)}")
        return

    for section, (title, paths, fragments) in zip(sections, SMOKE_CASES, strict=True):
        label = f"smoke-set.md {title}"
        if not section.startswith(title):
            errors.append(f"{label} title drifted")
        require_contains(errors, label, section, paths + fragments)
        section_paths = sorted(set(re.findall(r"`(harmony-next/[^`]+?\.md)`", section)))
        if not 1 <= len(section_paths) <= 3:
            errors.append(f"{label} should reference 1-3 target Markdown paths")
        for relative in section_paths:
            if not (root / relative).is_file():
                errors.append(f"{label} path does not exist: {relative}")


def check_dsh_bundle(root: Path, skill_version_value: str, errors: list[str]) -> None:
    package_path = root / "package.json"
    patch_path = root / "cordis.patch.yml"
    provider_path = root / "index.js"
    if not package_path.is_file():
        errors.append("missing package.json for DSH bundle")
        return
    if not patch_path.is_file():
        errors.append("missing cordis.patch.yml for DSH bundle")
    if not provider_path.is_file():
        errors.append("missing index.js for DSH bundle provider")

    try:
        manifest = json.loads(read(package_path))
    except (json.JSONDecodeError, OSError) as exc:
        errors.append(f"invalid package.json for DSH bundle: {exc}")
        return

    if manifest.get("name") != "dsh-harmony-next":
        errors.append("package.json DSH bundle name must be dsh-harmony-next")
    if manifest.get("version") != skill_version_value:
        errors.append("package.json version must match SKILL.md metadata.version")
    bundle_patch = manifest.get("dsh", {}).get("bundle", {}).get("patch")
    if bundle_patch != "./cordis.patch.yml":
        errors.append("package.json must declare dsh.bundle.patch as ./cordis.patch.yml")
    package_files = set(manifest.get("files", []))
    for required in ["index.js", "cordis.patch.yml", "harmony-next/SKILL.md", "harmony-next/references/**"]:
        if required not in package_files:
            errors.append(f"package.json files missing: {required}")

    if patch_path.is_file():
        patch_text = read(patch_path)
        require_contains(errors, "cordis.patch.yml", patch_text, ["id: harmony-next-skill", "name: dsh-harmony-next"])
    if provider_path.is_file():
        provider_text = read(provider_path)
        require_contains(
            errors,
            "index.js",
            provider_text,
            ["harmony-next/SKILL.md", "resourceBase", "ctx.skills.registerProvider"],
        )


def check(root: Path) -> list[str]:
    errors: list[str] = []
    try:
        skill_text = read(root / "harmony-next" / "SKILL.md")
        readme_text = read(root / "README.md")
        readme_en_text = read(root / "README_en.md")
        portability_text = read(root / "docs" / "agent-portability.md")
        version = skill_version(skill_text)
    except (OSError, ValueError) as exc:
        return [str(exc)]

    for label, text in [("README.md", readme_text), ("README_en.md", readme_en_text)]:
        require_contains(errors, label, text, INSTALL_FRAGMENTS)
        if f"`v{version}`" not in text:
            errors.append(f"{label} missing current version v{version}")
        if "docs/agent-portability.md" not in text:
            errors.append(f"{label} missing docs/agent-portability.md link")

    require_contains(errors, "docs/agent-portability.md", portability_text, PORTABILITY_FRAGMENTS)
    check_dsh_bundle(root, version, errors)
    check_smoke_paths(root, errors)
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Check README, skill, portability, and smoke-set drift.")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2])
    args = parser.parse_args()

    errors = check(args.root.resolve())
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1
    print("packaging docs are consistent")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
