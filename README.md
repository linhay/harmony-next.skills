# HarmonyOS NEXT 开发者专家技能包 (Reference Skill)

`harmony-next.skills` 是为 AI 编程助手（如 Gemini CLI, Claude Code, Codex）设计的参考技能库。
它为 HarmonyOS NEXT（以 API 12+ 为主；文档大量包含 API 12-23 的版本标注/兼容/变更说明，且少量内容会引用更早版本用于对比）提供本地化的离线知识源，包含 4,257 份涵盖 ArkTS、ArkUI 和 NDK 的 Markdown 格式参考文档（其中 `JsEtsAPIReference/` 为 4,232 份）。

[English Version](./README_en.md)

## 核心特性 (v1.0.6+)

除了详尽的 API 参考外，本项目现已包含以下**专家级实战指南**：
- **IDE 实操**：应用签名、断点调试、模拟器与真机配置、AI 辅助编程。
- **独立工具链**：独立命令行工具包 (Standalone CLI) 的下载、环境变量配置及 CI/CD 调优。
- **多端适配**：一次开发多端部署（自适应/响应式布局）、折叠屏与平板适配。
- **自由流转**：跨端迁移、多端协同的核心逻辑与开发步骤。
- **NDK 开发**：Node-API (napi) 基础、C++ 与 ArkTS 跨语言互调。
- **应用发布**：AppGallery Connect 配置、证书申请、上架审核流程。
- **性能调优**：使用 DevEco Profiler 进行 CPU、内存、帧率及启动耗时分析。
- **架构设计**：HAP/HAR/HSP 包结构、Stage 模型并发机制。
- **自动化测试**：基于 Hypium 的单元测试与 UI 测试，以及 CI 命令行集成。

## 工作原理

当你的编程助手需要 HarmonyOS 相关知识时，应使用本仓库作为检索层，而非依赖大模型的训练记忆（避免幻觉）。

**推荐查找流程（渐进式披露）：**
1. 打开 [`SKILL.md`](harmony-next/SKILL.md) 了解检索规则与回答约束。
2. 先缩小范围：[`KITS.md`](harmony-next/references/KITS.md)（Kit 识别 + 关键词/模块前缀）或 [`TASK_MAP.md`](harmony-next/references/TASK_MAP.md)（任务到关键词）。
3. 再精确命中文件：[`INDEX.md`](harmony-next/references/INDEX.md)（全库路径）与 [`JsEtsAPIReference/INDEX.md`](harmony-next/references/JsEtsAPIReference/INDEX.md)（API 分桶路径）。
4. 命中路径后，只打开那 1-3 个目标 Markdown 获取 API 级细节（不要盲读大库）。

## 快速开始

### 用户集成指南

#### Gemini CLI
```bash
gemini skills install https://github.com/linhay/harmony-next.skills --path harmony-next --scope user
```

#### Claude Code
1. 从本仓库下载技能文件夹。
2. 根据需要进行压缩。
3. 在 Claude.ai 的 `Settings > Capabilities > Skills` 中上传。
4. 或者直接将其放置在你的 Claude Code 技能目录中。

如果你只想将其作为项目上下文添加：
```bash
git clone https://github.com/linhay/harmony-next.skills.git
claude --add-dir /path/to/harmony-next.skills/harmony-next
```

#### Codex / 自定义 Agent
使用这两个入口文件进行索引：
1. [`harmony-next/SKILL.md`](https://github.com/linhay/harmony-next.skills/blob/master/harmony-next/SKILL.md)
2. [`harmony-next/references/INDEX.md`](https://github.com/linhay/harmony-next.skills/blob/master/harmony-next/references/INDEX.md)

## 包含内容
- `harmony-next/references/`: 4,257 份 Markdown 文档 (约 50 MB)。
- `harmony-next/SKILL.md`: 助手的检索规则与回答策略。
- `harmony-next.skill`: 由 GitHub Actions 自动生成的打包发布产物。

## 为什么需要它？
- **消除幻觉**：提供 HarmonyOS 5.0+ 真实 API 实现指导。
- **确定性回复**：为 Agent 工作流提供可寻址的文件参考。
- **离线支持**：在无网或受限环境下依然可以使用完整的 API 手册。

## 来源与许可
- 数据源：华为 HarmonyOS 官方文档。
- 本仓库为 AI 辅助开发工作流重新封装了这些参考资料。
