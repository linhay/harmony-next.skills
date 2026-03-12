---
name: harmony-next
description: Expert guidance for HarmonyOS NEXT (API 12+) development. Use this skill for ArkTS, ArkUI, and NDK development using official offline documentation for 3,300+ APIs and components.
---

# HarmonyOS NEXT Expert

This skill equips you with comprehensive, offline knowledge of HarmonyOS 5+ (ArkTS, ArkUI, NDK, System Services, etc.). The `references/` directory contains thousands of localized Markdown files directly converted from official developer documentation.

## How to use this skill

Because the reference library is massive (~50MB, 3300+ files), **DO NOT attempt to read files blindly**. You MUST use the `grep_search` and `glob` tools to find the exact API or module you need before reading the specific Markdown file.

### Recommended Workflow (Optimized Search Protocol)

Due to the massive size of this knowledge base (3,300+ files), you MUST follow this **Three-Tier Search Protocol** to avoid being overwhelmed by irrelevant files:

1. **Tier 1: Identify the Kit (Read `references/KITS.md`)**
   HarmonyOS 5+ is organized by Kits (e.g., `AbilityKit`, `ArkUI`, `MediaKit`). Read `references/KITS.md` first to identify which Kit contains the functionality you need. This drastically narrows down the search space.

2. **Tier 2: Task-to-File Mapping (Read `references/TASK_MAP.md`)**
   For common tasks (Layout, Lifecycle, Network), check `references/TASK_MAP.md`. It links tasks to their most important keywords and Kits.

3. **Tier 3: Surgical Grep (via `references/INDEX.md`)**
   Once you have the Kit name or specific keywords, use `grep` on `references/INDEX.md` to find the exact filenames.
   - *Example*: `grep "AbilityKit" references/INDEX.md | grep "Context"`

### Core Content Structure

- `JsEtsAPIReference/`: Detailed API signatures and C-API headers.
- `quickStart/`: Step-by-step developer guides.
- `KITS.md`: The primary navigation hub organized by @kit.
- `INDEX.md`: The full A-Z file list for surgical lookups.

### Directory Structure under `references/`

- `JsEtsAPIReference/` : Contains the bulk of ArkTS and ArkUI component APIs, lifecycle methods, error codes, and C-API/NDK headers.
- `quickStart/` : Beginner tutorials and fundamental concepts (e.g., page navigation, entry points).
- `hos/` & `hos_en/` : Core concepts, system services, and framework overviews.

## Core Directives for HarmonyOS Generation

1. **Strictly Declarative**: Always use the declarative UI paradigm syntax (`@Entry`, `@Component`, `build()`).
2. **No Hallucinations**: Rely strictly on the documentation provided in the `references/` folder when unsure about an API signature in HarmonyOS 5+. Do not assume standard Web JS or Android APIs are available unless verified in the docs.
3. **TypeScript/ArkTS Validation**: Ensure type safety and use standard ArkTS conventions.
\n<!-- version: 1.0.1 -->
