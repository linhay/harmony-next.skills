# harmony-next.skills

Expert guidance for **HarmonyOS NEXT (API 12+)** development. This repository contains a pre-packaged Gemini CLI skill with over 3,300 localized documentation files covering ArkTS, ArkUI, and NDK.

## Features

- **3,300+ Localized Docs**: Comprehensive API references, components, and quick starts.
- **Optimized Search**: Three-tier search architecture (`KITS.md` -> `TASK_MAP.md` -> `INDEX.md`).
- **High Quality**: Corrected code block indentation and syntax highlighting.
- **Offline First**: All knowledge is embedded within the skill for millisecond lookups.

## Installation

### Gemini CLI (Recommended)

#### 1. Prerequisite
Make sure you have [Gemini CLI](https://github.com/google/gemini-cli) installed.

#### 2. One-Line Install
Run the following command to install the skill directly from the latest release:

```bash
gemini skills install https://github.com/linhey/harmony-next.skills/releases/latest/download/harmony-next.skill --scope user
```

#### 3. Reload
In your interactive Gemini CLI session, run:
```bash
/skills reload
```

### Manual Installation (from Source)
If you prefer to install from source or use other tools:
1. Clone this repository: `git clone https://github.com/linhey/harmony-next.skills.git`
2. Install the local folder: `gemini skills install ./harmony-next --scope workspace`

---

## How to Use

After installation, the agent will automatically use this skill for HarmonyOS-related queries. It follows a specific search protocol:
1. **Identify Kit**: Check `KITS.md` to narrow down the scope.
2. **Task Mapping**: Check `TASK_MAP.md` for common patterns.
3. **Surgical Search**: Use `INDEX.md` to find exact filenames for `read_file`.

## License
Documentation source: Huawei HarmonyOS Official Documentation.
