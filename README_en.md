# HarmonyOS NEXT Reference Skill

An offline HarmonyOS NEXT reference skill for coding agents such as Gemini CLI, Claude Code, and Codex.

[![release](https://img.shields.io/badge/release-v1.3.2-1f6feb?style=flat-square)](https://github.com/linhay/harmony-next.skills/releases/tag/v1.3.2)
[![readme](https://img.shields.io/badge/readme-%E4%B8%AD%E6%96%87-0f766e?style=flat-square)](./README.md)
![docs](https://img.shields.io/badge/docs-3,622%20markdown%20files-7c3aed?style=flat-square)
![js-ets](https://img.shields.io/badge/JsEtsAPIReference-3,598%20files-b45309?style=flat-square)

> A local knowledge source for API 12-23, covering ArkTS, ArkUI, NDK, toolchains, debugging, release workflows, and multi-device adaptation.

## What Problem It Solves

`harmony-next.skills` is not just a document mirror. It is a HarmonyOS NEXT retrieval layer designed for coding agents.

It is meant to answer questions like:

- Which file contains a specific `@ohos.*` module
- Whether an ArkUI component, interface, or NDK header actually exists
- Whether API 23 additions are already included in the current knowledge base
- Whether a legacy internal link has been migrated and still resolves correctly

The goal is to turn those questions into local file lookups that are traceable, linkable, and verifiable.

## Core Features

| Capability | Description |
| --- | --- |
| Offline retrieval | Resolve document paths first, then read the source instead of guessing from model memory |
| Agent-oriented workflow | Organized as `SKILL.md -> KITS/TASK_MAP -> INDEX`, which fits progressive retrieval |
| More than API docs | Includes IDE setup, signing, debugging, release, performance, multi-device, and NDK guidance |

## Repository Overview

| Module | Description | Entry |
| --- | --- | --- |
| Skill rules | Tells the agent how to search, answer, and what to trust | [`harmony-next/SKILL.md`](./harmony-next/SKILL.md) |
| Kit navigation | Narrow scope by AbilityKit, ArkUI, ArkData, MediaKit, Security, and more | [`references/KITS.md`](./harmony-next/references/KITS.md) |
| Task navigation | Map UI, lifecycle, network, media, NDK, release, and other tasks to keywords | [`references/TASK_MAP.md`](./harmony-next/references/TASK_MAP.md) |
| Global index | Full Markdown path index for the reference corpus | [`references/INDEX.md`](./harmony-next/references/INDEX.md) |
| Bucketed API index | Focused index for `JsEtsAPIReference/`, covering modules, topics, types, errors, and guides | [`JsEtsAPIReference/INDEX.md`](./harmony-next/references/JsEtsAPIReference/INDEX.md) |
| Reference corpus | `3,622` Markdown files total, with `3,598` under `JsEtsAPIReference/` | [`harmony-next/references/`](./harmony-next/references/) |

## Recommended Retrieval Path

```text
SKILL.md
  -> KITS.md / TASK_MAP.md
  -> INDEX.md
  -> target Markdown file
```

Why this layout works:

1. Start with rules so the agent does not blind-read the entire corpus.
2. Narrow the scope by kit or task to reduce false hits.
3. Resolve real file paths from indexes instead of relying on name guesses.
4. Open only 1-3 target files for API-level detail.

The core principle is simple: find the path first, then read the content.

## Typical Use Cases

### ArkTS / ArkUI Development

- Components, decorators, state management, navigation, UIAbility, and Want
- API version differences, parameter signatures, and return values
- Restoring working links inside component documentation

### NDK / Node-API / C API

- Mapping headers to real `topics/**/<header>.h.md` pages
- ArkTS/C++ interoperability, CMake, and native capability access
- Index and link validation after legacy path migration

### IDE / Toolchain / Debugging

- Signing, emulators, real devices, and breakpoints
- Standalone CLI setup and CI/CD integration
- Performance analysis and release workflows

### Agent Engineering Integration

- Gemini CLI, Claude Code, and Codex
- Local knowledge base retrieval layer
- Lower hallucination risk with higher traceability

## Quick Start

### Gemini CLI

```bash
gemini skills install https://github.com/linhay/harmony-next.skills --path harmony-next --scope user
```

### Claude Code

1. Download the skill directory from this repository.
2. Zip it if needed.
3. Upload it in Claude.ai via `Settings > Capabilities > Skills`.
4. Or place it in your Claude Code skills directory.

If you only want to attach it as project context:

```bash
git clone https://github.com/linhay/harmony-next.skills.git
claude --add-dir /path/to/harmony-next.skills/harmony-next
```

### Codex

More precisely, this repository is a Codex skill / reference knowledge source, not a standalone plugin installed through a single `npm install` command.

Recommended setup:

1. Download or clone this repository:

```bash
git clone https://github.com/linhay/harmony-next.skills.git
```

2. Move the `harmony-next/` directory into a skill path that Codex reads.

A common approach is to place it in your Codex skills directory. If you already maintain a project-level skills directory, you can place `harmony-next/` there directly.

3. If you are not wiring it in as a formal skill directory and instead want to use it as an in-project reference source, make sure Codex prioritizes these two entry files:

- [`harmony-next/SKILL.md`](https://github.com/linhay/harmony-next.skills/blob/master/harmony-next/SKILL.md)
- [`harmony-next/references/INDEX.md`](https://github.com/linhay/harmony-next.skills/blob/master/harmony-next/references/INDEX.md)

In short: for Codex, the key is not “install a package”, but “place this skill directory where Codex will read it”.

## What Matters in v1.2.0

| Version | Highlights |
| --- | --- |
| `v1.2.0` | API 23 content is included; `references/INDEX.md` and `JsEtsAPIReference/INDEX.md` were rebuilt; legacy `capi/headers/*.md` pages were removed and replaced with direct links to real targets; `reference_compat.py` and link-audit tooling were added; both Chinese and English README files were synchronized |

## Reference Maintenance

After syncing, migrating, or bulk-rewriting `references/JsEtsAPIReference/`, run the following in order:

```bash
python3 harmony-next/scripts/reference_compat.py generate
python3 harmony-next/scripts/reference_compat.py check
python3 harmony-next/scripts/reference_compat.py audit
python3 -m unittest discover -s harmony-next/tests -p 'test_*.py' -v
```

Command roles:

- `generate`
  - Rewrite legacy `../../capi/headers/*.md` links to real `topics/**/<header>.h.md` targets
  - Rebuild `references/INDEX.md` and `references/JsEtsAPIReference/INDEX.md`
- `check`
  - Verify legacy `capi/headers/` pages are gone
  - Verify indexes match the filesystem
  - Verify body content no longer points at old header paths
- `audit`
  - Scan current uncommitted changes
  - Detect internal Markdown links that used to exist but were flattened into plain text
- `unittest`
  - Verify the migration and audit tooling itself has not regressed

## Why It Is Worth Integrating

| Value | Description |
| --- | --- |
| Fewer hallucinations | Answers come from real document paths instead of memory completion |
| Better traceability | Every answer can point back to a concrete Markdown file |
| Better automation fit | Indexes, rules, and validation make it suitable for long-term agent workflows |

## Source and License

- Source: Huawei HarmonyOS official documentation
- This repository repackages those materials for AI-assisted development workflows

Chinese documentation is available in [README.md](./README.md).
