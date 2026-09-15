<p align="right"><a href="./README.md">简体中文</a></p>

# HarmonyOS NEXT Agent Skills

Offline HarmonyOS NEXT skills for Gemini CLI, Claude Code, Codex, and other AI coding agents.

[![release](https://img.shields.io/github/v/release/linhay/harmony-next.skills?style=flat-square)](https://github.com/linhay/harmony-next.skills/releases/latest)
[![skills.sh](https://skills.sh/b/linhay/harmony-next.skills)](https://skills.sh/linhay/harmony-next.skills)
![docs](https://img.shields.io/badge/docs-4238-7c3aed?style=flat-square)
![api](https://img.shields.io/badge/API%2012--26-4207-b45309?style=flat-square)

> Offline references and repeatable workflows for HarmonyOS API 12–26, ArkTS/ArkUI, NDK, DevEco Studio, emulator automation, debugging, and publishing.

## Let an Agent Install It

Send this prompt to your agent:

<details>
<summary>Show installation prompt</summary>

```text
Install and enable the harmony-next skill from linhay/harmony-next.skills.
Detect the current agent:
- Gemini CLI：gemini skills install https://github.com/linhay/harmony-next.skills --path harmony-next --scope user
- Claude Code：npx skills add linhay/harmony-next.skills --skill harmony-next -a claude-code -g -y --copy
- Codex：npx skills add linhay/harmony-next.skills --skill harmony-next -a codex -g -y --copy
- Other agents supporting skills CLI:npx skills add linhay/harmony-next.skills --skill harmony-next
After installation, read harmony-next/SKILL.md, verify the name and version, and report the actual path. If a command is unavailable, give the manual path and do not claim success.
```

</details>

## Quick Start

```bash
npx skills add linhay/harmony-next.skills --skill harmony-next
```

After installation, ask your agent a HarmonyOS development question. It will follow `SKILL.md → KITS.md / TASK_MAP.md → INDEX.md` to find local references.

## Capabilities

| Capability | Use cases | Entry |
| --- | --- | --- |
| API reference | ArkTS、ArkUI、系统模块、API 版本确认 | [`JsEtsAPIReference/INDEX.md`](./harmony-next/references/JsEtsAPIReference/INDEX.md) |
| Kit / 任务导航 | Find references by Kit or task | [`KITS.md`](./harmony-next/references/KITS.md) · [`TASK_MAP.md`](./harmony-next/references/TASK_MAP.md) |
| API 26 snapshot | API 26.0.0 declarations, types, and signatures | [`api26/`](./harmony-next/references/JsEtsAPIReference/api26/) |
| DevEco / Emulator | HVD、hdc、uitest、抓包和诊断 | [`DevEco模拟器私有接口与AI自动化.md`](./harmony-next/references/ideGuides/DevEco模拟器私有接口与AI自动化.md) |
| Minimal project | Empty Ability、构建和 smoke 测试 | [`empty-ability-app`](./harmony-next/references/templates/empty-ability-app/) |
| Automation scripts | 设备证据、UI/UX、Trace、命令行工具 | [`scripts/`](./harmony-next/scripts/) |

## Recommended lookup path

```text
SKILL.md → KITS.md / TASK_MAP.md → INDEX.md → 目标文档
```

## Installation options

- Gemini CLI：`gemini skills install https://github.com/linhay/harmony-next.skills --path harmony-next --scope user`
- Claude Code：`npx skills add linhay/harmony-next.skills --skill harmony-next -a claude-code -g -y --copy`
- Codex：`npx skills add linhay/harmony-next.skills --skill harmony-next -a codex -g -y --copy`
- DSH：`dsh plugin --profile demo add github:linhay/harmony-next.skills`

<details>
<summary>高级说明、脚本与维护</summary>

- [Full skill rules](./harmony-next/SKILL.md)
- [Agent adapters and install paths](./docs/agent-portability.md)
- [API 26 release and sync record](./harmony-next/references/harmonyos-releases/api-26-release.md)
- [Issue guide](./harmony-next/ISSUE_GUIDE.md)

Compatible install references: `npx skills add linhay/harmony-next.skills --list`, `$HOME/.agents/skills/harmony-next`, `DSH_SOURCE=/path/to/harmony-next.skills`, `.dsh/skills/harmony-next`, and `dsh-harmony-next`.

Regenerate the API 26 declaration snapshot from an updated DevEco Studio:

```bash
python3 harmony-next/scripts/sync_api26_snapshot.py \
  --deveco-app /path/to/DevEco-Studio.app
python3 harmony-next/scripts/reference_compat.py generate
```

Run before publishing:

```bash
python3 harmony-next/scripts/check_packaging_docs.py
python3 harmony-next/scripts/reference_compat.py check
python3 -m unittest discover -s harmony-next/tests -p 'test_*.py' -v
```

</details>

## Version

Current release:[`v1.3.37`](https://github.com/linhay/harmony-next.skills/releases/tag/v1.3.37)。The API 26.0.0 Release declarations are included; official guides, examples, and change notes continue to be added.

## License

MIT. Documentation is derived from official Huawei HarmonyOS materials; copyrights remain with their respective owners.
