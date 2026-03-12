# harmony-next.skills

Expert guidance for **HarmonyOS NEXT (API 12+)** development. This repository contains a pre-packaged skill with over 3,300 localized documentation files covering ArkTS, ArkUI, and NDK. Compatible with Gemini CLI, Claude Code, and OpenAI Codex.

## Features

- **3,300+ Localized Docs**: Comprehensive API references, components, and quick starts.
- **Optimized Search**: Three-tier search architecture (`KITS.md` -> `TASK_MAP.md` -> `INDEX.md`).
- **High Quality**: Corrected code block indentation and syntax highlighting.
- **Offline First**: All knowledge is embedded within the skill for millisecond lookups.

## Installation

### Gemini CLI

#### 1. Prerequisite
Make sure you have [Gemini CLI](https://github.com/google/gemini-cli) installed.

#### 2. Download and Install
1. Go to the [Releases](https://github.com/linhay/harmony-next.skills/releases) page.
2. Download the `harmony-next.skill` file from the latest release.
3. Install it using the following command:

```bash
gemini skills install path/to/harmony-next.skill --scope user
```

#### 3. Reload
In your Gemini CLI session, run:
```bash
/skills reload
```

---

### Claude Code

#### 1. Prerequisite
Make sure you have [Claude Code](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/overview) installed.

```bash
npm install -g @anthropic-ai/claude-code
```

#### 2. Clone the Repository

```bash
git clone https://github.com/linhay/harmony-next.skills.git
```

#### 3. Add Context to Your Project

In your project root, add the skill path to your `CLAUDE.md` file:

```markdown
## HarmonyOS NEXT Reference

@/path/to/harmony-next.skills/harmony-next/SKILL.md
```

Or launch Claude Code with the skill directory added as context:

```bash
claude --add-dir /path/to/harmony-next.skills/harmony-next
```

---

### OpenAI Codex

#### 1. Prerequisite
Make sure you have [Codex CLI](https://github.com/openai/codex) installed.

```bash
npm install -g @openai/codex
```

#### 2. Clone the Repository

```bash
git clone https://github.com/linhay/harmony-next.skills.git
```

#### 3. Add Context to Your Project

In your project root, add the skill path to your `AGENTS.md` file:

```markdown
## HarmonyOS NEXT Reference

See /path/to/harmony-next.skills/harmony-next/SKILL.md for HarmonyOS NEXT (API 12+) expert guidance including ArkTS, ArkUI, and NDK documentation.
```

---

## How to Use

After installation, the agent will automatically use this skill for HarmonyOS-related queries. It follows a specific search protocol to find exact APIs within the massive reference library.

## License
Documentation source: Huawei HarmonyOS Official Documentation.
