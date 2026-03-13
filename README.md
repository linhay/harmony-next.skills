# HarmonyOS NEXT Superpowers

`harmony-next.skills` is a documentation pack for coding agents.
It provides a local source of truth for HarmonyOS NEXT (API 12+), with 3,394 Markdown references across ArkTS, ArkUI, and NDK topics.

## How It Works

When your agent needs HarmonyOS knowledge, it should use this repository as a retrieval layer instead of guessing from model memory.

Recommended lookup flow:

1. Open [`KITS.md`](harmony-next/references/KITS.md) to locate the correct capability domain.
2. Use [`TASK_MAP.md`](harmony-next/references/TASK_MAP.md) to map user intent to technical keywords.
3. Resolve exact files from [`INDEX.md`](harmony-next/references/INDEX.md).
4. Follow rules in [`SKILL.md`](harmony-next/SKILL.md) to answer with concrete API-level detail.

This keeps responses precise, traceable, and stable.

## Quickstart

### User Integration Cheatsheet

#### Gemini CLI

```bash
gemini skills install https://github.com/linhay/harmony-next.skills/releases/latest/download/harmony-next.skill --scope user
/skills reload
```

#### Claude Code

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

- `harmony-next/references/`: 3,394 markdown reference files (about 50 MB).
- `harmony-next/SKILL.md`: retrieval rules and answer policy for agents.
- `harmony-next.skill`: prebuilt skill package for Gemini CLI (about 8 MB).

## Why This Exists

- Reduce hallucination in HarmonyOS implementation guidance.
- Provide deterministic, file-addressable answers for agent workflows.
- Keep API references usable in offline or constrained environments.

## Source and License

- Source: Huawei HarmonyOS official documentation.
- This repository repackages those references for AI-assisted development workflows.
