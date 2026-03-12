# harmony-next.skills

Expert guidance for **HarmonyOS NEXT (API 12+)** development. This repository contains a pre-packaged Gemini CLI Skill with over 3,300 localized documentation files covering ArkTS, ArkUI, and NDK.

## Features

- **3,300+ Localized Docs**: Comprehensive API references, components, and quick starts.
- **Optimized Search**: Three-tier search architecture (`KITS.md` -> `TASK_MAP.md` -> `INDEX.md`).
- **High Quality**: Corrected code block indentation and syntax highlighting.
- **Offline First**: All knowledge is embedded within the skill for millisecond lookups.

## Installation

### 1. Prerequisite
Make sure you have [Gemini CLI](https://github.com/google/gemini-cli) installed.

### 2. Download and Install
Clone this repo and install the `.skill` file:

```bash
git clone https://github.com/linhey/harmony-next.skills.git
cd harmony-next.skills
gemini skills install harmony-next.skill --scope user
```

### 3. Reload
In your Gemini CLI session, run:
```bash
/skills reload
```

## How to Use

After installation, the agent will automatically use this skill for HarmonyOS-related queries. It follows a specific search protocol to find exact APIs within the massive reference library.

## License
Documentation source: Huawei HarmonyOS Official Documentation.
