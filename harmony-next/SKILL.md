---
name: harmony-next
description: HarmonyOS NEXT（以 API 12-23 为主）离线参考库导航：按 Kit/任务/索引渐进式定位文档（ArkTS/ArkUI/NDK）。
---

# HarmonyOS NEXT（离线文档导航）

目标：在不盲读 `references/` 的前提下，快速定位到 1 个或少量目标 Markdown，然后只打开这些文件。

## 渐进式披露（按顺序走）

1. **先缩小范围（选 Kit 或任务）**
   - Kit 导航：`references/KITS.md`
   - 任务导向：`references/TASK_MAP.md`

2. **再精确命中文件（搜路径清单）**
   - 全库路径清单：`references/INDEX.md`
   - JS/ETS API 分桶清单：`references/JsEtsAPIReference/INDEX.md`

3. **仅在必要时浏览目录**
   `references/JsEtsAPIReference/` 目前以 `modules/`、`topics/`、`types/`、`errors/`、`guides/` 为主。

## 常用检索（直接复制用）

- 先按关键词命中路径：`rg -n "UIAbility|AbilityStage|Want" references/INDEX.md | head`
- 查某个 `@ohos.*` 模块：`rg -n "@ohos\\.app\\.ability\\.|@ohos\\.ability\\." references/INDEX.md | rg "JsEtsAPIReference/" | head`
- 查 NDK/C API 头文件：`rg -n "JsEtsAPIReference/topics/.*/.*\\.h\\.md$" references/INDEX.md | rg "(napi|arkui|window|ability)" | head`

## 生成约束（避免踩坑）

- **不要全量读取**：先在 `INDEX.md` 命中路径，再打开对应 `.md`。
- **不确定就查文档**：API 签名、入参、返回值以 `references/` 内文本为准，不凭经验补全。
- **ArkUI 优先声明式**：示例优先使用 `@Entry` / `@Component` / `build()`（除非文档明确是 NDK 或系统服务）。

<!-- version: 1.3.0 -->
