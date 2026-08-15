<p align="right">
  <a href="./README.md" title="[readme-中文](./README.md)"><img src="https://img.shields.io/badge/Language-中文-0f766e?style=for-the-badge" alt="readme-中文" /></a>
</p>

# 🧰 HarmonyOS NEXT Developer Expert Skill Pack

An offline HarmonyOS NEXT reference skill library for AI coding assistants such as Gemini CLI, Claude Code, and Codex.

[![release](https://img.shields.io/github/v/release/linhay/harmony-next.skills?style=flat-square)](https://github.com/linhay/harmony-next.skills/releases/latest)
[![skills.sh](https://skills.sh/b/linhay/harmony-next.skills)](https://skills.sh/linhay/harmony-next.skills)
![docs](https://img.shields.io/badge/docs-3,708%20markdown%20files-7c3aed?style=flat-square)
![js-ets](https://img.shields.io/badge/JsEtsAPIReference-3,678%20files-b45309?style=flat-square)

> A local knowledge source for API 12-23, covering ArkTS, ArkUI, NDK, tooling, debugging, release workflows, and multi-device adaptation.

## 🎯 Problems It Solves

AI coding assistants commonly hit these issues during HarmonyOS development:

- Cannot locate the real documentation for `@ohos.*` modules
- Cannot confirm whether an ArkUI component or NDK header actually exists
- API version differences or newly added APIs are missing from model knowledge
- Old documentation links are broken or moved
- DevEco Studio Emulator, `hdc`, `uitest`, and other local automation paths are unclear

This repository turns those uncertainties into **local file lookups that are locatable, linkable, and verifiable**.

## Before / After

**Without the skill**: the model guesses `@ohos.*` modules, ArkUI component names, or DevEco commands from memory, often without a verifiable source.

**With this skill**: the agent follows `SKILL.md → KITS.md / TASK_MAP.md → INDEX.md`, opens the target Markdown files, then returns code plus `hdc` / `uitest` / wrapper-script validation commands.

## ✨ Core Features

- **Fully offline lookup**: avoid guessing from model memory; resolve documentation paths before reading content
- **Designed for agent workflows**: progressive lookup via `SKILL.md → KITS/TASK_MAP → INDEX`
- **Broad coverage**: API references plus IDE, signing, debugging, release, performance, and NDK practice guides
- **Private capability isolation**: private DevEco Emulator and IDE interfaces are documented separately, with version and risk checks first
- **Automation-first**: non-interactive automation policies plus evidence capture, offline UI/UX audit, and trace audit scripts
- **Runnable minimal project**: an `empty-ability-app` template that can be copied directly for smoke tests

## 📚 Contents

| Entry / Module | Purpose |
| --- | --- |
| [`SKILL.md`](./harmony-next/SKILL.md) | Single source of truth for skill rules: how agents should search and which sources to trust first |
| [`references/KITS.md`](./harmony-next/references/KITS.md) | Navigate by Kit, such as AbilityKit, ArkUI, and ArkData |
| [`references/TASK_MAP.md`](./harmony-next/references/TASK_MAP.md) | Navigate by task, such as UI, networking, media, and NDK |
| [`references/INDEX.md`](./harmony-next/references/INDEX.md) | Full repository index with 3,708 Markdown paths |
| [`JsEtsAPIReference/INDEX.md`](./harmony-next/references/JsEtsAPIReference/INDEX.md) | API bucket index for modules, topics, errors, and more |
| [`references/templates/empty-ability-app`](./harmony-next/references/templates/empty-ability-app/) | Copyable HarmonyOS NEXT smoke fixture |
| [`docs/agent-portability.md`](./docs/agent-portability.md) | Agent install and adapter path notes |
| `harmony-next/references/` | All Markdown source documents, including 3,678 API documents |

**Automation and diagnostic scripts**:

| Script | Purpose | Entry command example |
| --- | --- | --- |
| [`commandline_tools_manager.py`](./harmony-next/scripts/commandline_tools_manager.py) | Download and install Command Line Tools | `python3 harmony-next/scripts/commandline_tools_manager.py install ...` |
| [`device_evidence_bundle.py`](./harmony-next/scripts/device_evidence_bundle.py) | Capture device evidence and diagnose WebView DevTools forwarding | `python3 harmony-next/scripts/device_evidence_bundle.py webview-devtools ...` |
| [`device_ui_action.py`](./harmony-next/scripts/device_ui_action.py) | Perform one bounded UI action with before/after evidence | `python3 harmony-next/scripts/device_ui_action.py tap ...` |
| [`ux_audit_pipeline.py`](./harmony-next/scripts/ux_audit_pipeline.py) | Run offline UI/UX audits | `python3 harmony-next/scripts/ux_audit_pipeline.py doctor ...` |
| [`profiler_trace_audit.py`](./harmony-next/scripts/profiler_trace_audit.py) | Audit offline trace performance evidence | `python3 harmony-next/scripts/profiler_trace_audit.py audit ...` |
| [`hvd_manager.py`](./harmony-next/scripts/hvd_manager.py) | Manage HVD devices | `python3 harmony-next/scripts/hvd_manager.py doctor ...` |

**Specialized documents**:

- [`DevEco模拟器私有接口与AI自动化.md`](./harmony-next/references/ideGuides/DevEco模拟器私有接口与AI自动化.md)
- [`ArkWeb WebView CDP调试与字段到达证明.md`](./harmony-next/references/ideGuides/ArkWeb%20WebView%20CDP调试与字段到达证明.md)
- [`DevEco Studio IDE私有接口与AI自动化.md`](./harmony-next/references/ideGuides/DevEco%20Studio%20IDE私有接口与AI自动化.md)
- [`minimal-project-scaffold.md`](./harmony-next/references/quickStart/ets/minimal-project-scaffold.md)

## 🚀 Quick Start

### Generic Path (Recommended)

```bash
npx skills add linhay/harmony-next.skills
```

This repository currently contains one skill, so the command above automatically installs `harmony-next`. To list available skills first:

```bash
npx skills add linhay/harmony-next.skills --list
```

### Gemini CLI

```bash
gemini skills install https://github.com/linhay/harmony-next.skills --path harmony-next --scope user
```

### Claude Code

```bash
npx skills add linhay/harmony-next.skills --skill harmony-next -a claude-code -g -y --copy
```

Or add the repository directory manually:

```bash
git clone https://github.com/linhay/harmony-next.skills.git
claude --add-dir /path/to/harmony-next.skills/harmony-next
```

### Codex

```bash
npx skills add linhay/harmony-next.skills --skill harmony-next -a codex -g -y --copy
```

> This repository is not currently packaged as a Codex plugin; `npx skills` only installs the skill into a directory that Codex can scan. It does not install MCP/tools/apps.

You can also place it manually in an official path such as `$HOME/.agents/skills/harmony-next`; see [`docs/agent-portability.md`](./docs/agent-portability.md) for the full path list.

### DeepSeek Harness (DSH)

This repository provides the official DSH profile bundle `dsh-harmony-next`. The recommended installation is through a DSH profile:

```bash
# Install from GitHub
dsh plugin --profile demo add github:linhay/harmony-next.skills

# Or install from a local checkout
dsh plugin --profile demo add /path/to/harmony-next.skills

# Inspect the bundle layer
dsh --profile demo --dump-config
```

The bundle registers only the `harmony-next` skill and its offline reference resources; it does not install MCP servers, tools, or apps. The DSH bundle manifest is the root `package.json`, and its patch is `cordis.patch.yml`.

If you only need a filesystem skill, you can also install it manually into a DSH-compatible root:

```bash
# DSH_SOURCE points to a local checkout of this repository
DSH_SOURCE=/path/to/harmony-next.skills

# Project-local skill
mkdir -p .dsh/skills/harmony-next
cp -R "$DSH_SOURCE/harmony-next/." .dsh/skills/harmony-next/

# Or user-level skill (default: ~/.dsh/skills)
mkdir -p "$HOME/.dsh/skills/harmony-next"
cp -R "$DSH_SOURCE/harmony-next/." "$HOME/.dsh/skills/harmony-next/"
```

DSH also supports `.agents/skills`, `$DSH_AGENTS_HOME/skills`, and other compatible roots; see [`docs/agent-portability.md`](./docs/agent-portability.md) for discovery priority and update guidance.

Each host only loads the skill. HarmonyOS lookup behavior is governed by `harmony-next/SKILL.md`.

## 🧭 Recommended Lookup Path

```text
SKILL.md → KITS.md / TASK_MAP.md → INDEX.md → target Markdown
```

Principle: establish the rules first, narrow by Kit or task, resolve the real path through the index, then open only 1-3 target files for details.

## 📦 Use Cases

- **ArkTS / ArkUI development**: confirm APIs and examples for components, decorators, state management, UIAbility, and more
- **NDK / C API**: map headers to real documentation, cross-language calls, and CMake configuration
- **IDE / tooling / debugging**: signing, emulators, device debugging, performance analysis, and release workflows
- **DevEco Emulator automation**: launch without the IDE, HVD, `hdc`/`uitest` automation, and proxy diagnostics
- **Private DevEco IDE capabilities**: CodeGenie, ArkUI Inspector, offline trace audit, and UI/UX audit
- **Agent engineering integration**: a local knowledge retrieval layer for Gemini CLI, Claude Code, and Codex

### ⚠️ Safety Boundary: Private Interfaces and Local Automation

When working with **DevEco Emulator, private IDE interfaces, device logs, screenshots, proxy capture, or HVD create/delete operations**, agents **must read the corresponding private-interface documents first**. These workflows require:

- verifying DevEco / Emulator / SDK versions and command capabilities before execution
- defining artifact directories, redaction boundaries, and `blocked` output on failure
- specifying non-interactive execution policy, timeouts, and redaction contracts

Private-interface document entry points:

- [`DevEco模拟器私有接口与AI自动化.md`](./harmony-next/references/ideGuides/DevEco模拟器私有接口与AI自动化.md)
- [`DevEco Studio IDE私有接口与AI自动化.md`](./harmony-next/references/ideGuides/DevEco%20Studio%20IDE私有接口与AI自动化.md)

<details>
<summary>Expand: summary of Emulator/IDE private-interface rules</summary>

**DevEco Emulator private interfaces** trigger on terms such as `DevEco Studio`, `HarmonyOS Emulator`, `launch without IDE`, `HVD`, `hdc`, `uitest`, `aa`, `bm`, and `snapshot_display`.
Rules: first read the private-interface section in `SKILL.md`; re-verify versions and capabilities before each run; in a user-authorized local environment, automation policy describes execution mode, artifact directories, and redaction contracts; if wrapper scripts are blocked, try official CLI evidence paths first.

**DevEco Studio IDE private interfaces** trigger on terms such as `CodeGenie`, `MCP`, `devecostudio://`, `inspect.sh`, `ArkUI Inspector`, `Profiler`, and `UxTestService`.
Rules: default to static read-only analysis, such as plugin XML, jars, configuration, and offline traces; when launching IDE/GUI, local services, device connections, or MCP configuration, record the target, artifacts, and redaction boundary; offline trace audit and UI/UX audit should use only verified wrapper scripts and rule subsets.

Read the two documents above for full details.
</details>

## 📈 Version Highlights

| Version | Key updates |
| --- | --- |
| `v1.3.35` | Add the official DeepSeek Harness (DSH) profile bundle and filesystem-skill fallback adapter |
| `v1.3.30` | Emulator app sandbox quick reference and DevEco Emulator priority fix for HVD doctor |
| `Unreleased` | One-click offline UI/UX audit CLI (`ux_audit_pipeline.py`) |
| `Unreleased` | Device debugging evidence bundle CLI (`device_evidence_bundle.py`) |
| `Unreleased` | Offline trace performance audit CLI (`profiler_trace_audit.py`) |
| `Unreleased` | HVD launch improvements: trace socket holder, image validation, and license-agreement handling |
| `Unreleased` | WebView DevTools diagnostics, CDP field-arrival guidance, bounded UI action evidence, and Emulator crash classification |
| `v1.3.23` | Release workflow updated to Node 24 |
| `v1.3.7` | Copyable minimal test project template, SDK version adaptation checks including 6.0.2(22), and `uitest` smoke coverage |
| `v1.3.6` | Non-interactive automation policy for emulator workflows |
| `v1.3.5` | Private DevEco Studio IDE interface reference |
| `v1.2.0` | API 23 content added, indexes rebuilt, and link compatibility auditing added |

## 🔧 Maintenance and Contributions

After syncing, migrating, or rewriting the reference library, run:

```bash
python3 harmony-next/scripts/check_packaging_docs.py
python3 harmony-next/scripts/reference_compat.py generate
python3 harmony-next/scripts/reference_compat.py check
python3 harmony-next/scripts/reference_compat.py audit
python3 -m unittest discover -s harmony-next/tests -p 'test_*.py' -v
```

## 📜 Sources and License

- Data source: Huawei HarmonyOS official documentation
- This repository repackages the documentation for AI-assisted development. The Chinese README is [README.md](./README.md).

---

Thanks to [LINUX DO](https://linux.do/) for the support.

[![Star History Chart](https://api.star-history.com/svg?repos=linhay/harmony-next.skills&type=Date)](https://www.star-history.com/#linhay/harmony-next.skills&Date)
