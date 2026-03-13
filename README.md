# harmony-next.skills 🚀

Expert guidance for **HarmonyOS NEXT (API 12+)** development. 3,300+ precision-localized documentation files covering ArkTS, ArkUI, and NDK. 

This repository provides **"Superpowers"** for your AI agents (Gemini CLI, Claude Code, OpenAI Codex, etc.) by providing a reliable Source of Truth for HarmonyOS development.

---

## 🛠️ Usage for AI Agents

### ♊ Gemini CLI (Recommended)
Install the pre-packaged skill for an optimized, offline-first experience.

```bash
# One-line install from latest release
gemini skills install https://github.com/linhey/harmony-next.skills/releases/latest/download/harmony-next.skill --scope user

# Reload session
/skills reload
```

### 🤖 Claude Code
Add this repository as a "Superpower" context to your Claude Code session.

1. Clone the repo: `git clone https://github.com/linhey/harmony-next.skills.git`
2. Add to context:
```bash
# Launch Claude with the docs directory
claude --add-dir /path/to/harmony-next.skills/harmony-next
```
3. Or reference the **SKILL.md** in your `CLAUDE.md`:
```markdown
## HarmonyOS NEXT Reference
@/path/to/harmony-next.skills/harmony-next/SKILL.md
```

### 🧠 OpenAI Codex / Custom Agents
Point your agent to the [SKILL.md](https://github.com/linhey/harmony-next.skills/blob/master/harmony-next/SKILL.md) and the [INDEX.md](https://github.com/linhey/harmony-next.skills/blob/master/harmony-next/references/INDEX.md) to enable surgical documentation lookups.

---

## ✨ Features

- **3,300+ Docs**: Full API signatures, component lifecycles, and NDK headers.
- **Three-Tier Search Architecture**:
  1. [`KITS.md`](harmony-next/references/KITS.md) - Identify the module (AbilityKit, ArkUI, etc.).
  2. [`TASK_MAP.md`](harmony-next/references/TASK_MAP.md) - Map common tasks to technical keywords.
  3. [`INDEX.md`](harmony-next/references/INDEX.md) - Fast lookup for exact filenames.
- **Refined Format**: Corrected ETS code block indentation and syntax highlighting.
- **Zero Hallucination**: Rely on official docs, not outdated training data.

---

## 📂 Structure

- `harmony-next/SKILL.md`: The core instruction set for AI Agents.
- `harmony-next/references/`: The massive Markdown knowledge base.
- `harmony-next.skill`: The compiled package for Gemini CLI.

## License
Documentation source: Huawei HarmonyOS Official Documentation.
