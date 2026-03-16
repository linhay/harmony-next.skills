# HarmonyOS NEXT Reference Skill

`harmony-next.skills` is a reference skill for coding agents.
It provides a local source of truth for HarmonyOS NEXT (primarily API 12+, with extensive API 12-23 version notes/compatibility-change hints, and occasional references to earlier APIs for comparison), with 3,400+ Markdown references across ArkTS, ArkUI, and NDK topics.

## Key Features (v1.0.6+)

Beyond API references, this skill now includes **expert guides** for:
- **IDE Operations**: Signing, Debugging, Emulator/Real Device setup, and AI assistance.
- **Standalone Toolchain**: Standalone CLI download, env vars, and CI/CD configuration.
- **Multi-device Adaptation**: Strategies for phone, foldable, and tablet (Adaptive/Responsive Layout).
- **Continuation**: Cross-device migration and multi-device collaboration logic.
- **NDK Development**: Node-API (napi) basics and ArkTS/C++ interoperability.
- **App Publishing**: AGC configuration, certificates, and release process.
- **Performance Tuning**: CPU, Memory, Frame Rate, and Launch analysis via DevEco Profiler.
- **Architecture**: HAP/HAR/HSP structures and Stage Model concurrency.
- **Automation Testing**: Unit and UI testing with Hypium, including CI integration.

## How It Works

When your agent needs HarmonyOS knowledge, it should use this repository as a retrieval layer instead of guessing from model memory.

Recommended lookup flow:

1. Read [`SKILL.md`](harmony-next/SKILL.md) for retrieval rules and answer constraints.
2. Narrow scope via [`KITS.md`](harmony-next/references/KITS.md) (kit identification + keywords/module prefixes) or [`TASK_MAP.md`](harmony-next/references/TASK_MAP.md) (intent to keywords).
3. Resolve exact files from [`INDEX.md`](harmony-next/references/INDEX.md) (full paths) and [`JsEtsAPIReference/INDEX.md`](harmony-next/references/JsEtsAPIReference/INDEX.md) (bucketed API paths).
4. Open only the 1-3 matched Markdown files for API-level detail (avoid blind reads).

This keeps responses precise, traceable, and stable.

## Quickstart

### User Integration Cheatsheet

#### Gemini CLI

```bash
gemini skills install https://github.com/linhay/harmony-next.skills --path harmony-next --scope user
```

#### Claude Code

For actual skill installation, Anthropic's current distribution model is:

1. Download the skill folder from this repository.
2. Zip the skill folder if needed.
3. Upload it in Claude.ai via `Settings > Capabilities > Skills`.
4. Or place it in your Claude Code skills directory.

If you only want to attach the repository as project context, use:

```bash
git clone https://github.com/linhay/harmony-next.skills.git
claude --add-dir /path/to/harmony-next.skills/harmony-next
```

Or in `CLAUDE.md`:

```markdown
## HarmonyOS NEXT Reference
@/path/to/harmony-next.skills/harmony-next/SKILL.md
```

#### Codex / Custom Agents

Use these two entry files:

1. [`harmony-next/SKILL.md`](https://github.com/linhay/harmony-next.skills/blob/master/harmony-next/SKILL.md)
2. [`harmony-next/references/INDEX.md`](https://github.com/linhay/harmony-next.skills/blob/master/harmony-next/references/INDEX.md)

#### skills.sh

```bash
# list skills in this repo
npx skills add https://github.com/linhay/harmony-next.skills --list

# install only harmony-next
npx skills add https://github.com/linhay/harmony-next.skills --skill harmony-next

# optional: install globally for all projects
npx skills add https://github.com/linhay/harmony-next.skills --skill harmony-next -g
```

Use `--full-depth` only when the repository has deeply nested skill folders and default scanning misses them.

## Provider Release

`skills.sh` is the primary distribution channel for this repository.
As the skill provider, you only need to keep this GitHub repository updated. Users install directly from the repo.

Provider verification:

```bash
# run in this repository before release
npx skills add . --list
```

## What Is Included

- `harmony-next/references/`: 3,403 markdown reference files (about 50 MB).
- `harmony-next/SKILL.md`: retrieval rules and answer policy for agents.
- `harmony-next.skill`: packaged release artifact produced by GitHub Actions.

## Why This Exists

- Reduce hallucination in HarmonyOS implementation guidance.
- Provide deterministic, file-addressable answers for agent workflows.
- Keep API references usable in offline or constrained environments.

## Source and License

- Source: Huawei HarmonyOS official documentation.
- This repository repackages those references for AI-assisted development workflows.
