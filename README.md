# HarmonyOS NEXT 开发者专家技能包 (Reference Skill)

`harmony-next.skills` 是为 AI 编程助手（如 Gemini CLI, Claude Code, Codex）设计的参考技能库。
它为 HarmonyOS NEXT (API 12+) 提供本地化的离线知识源，包含超过 3,409 份涵盖 ArkTS、ArkUI 和 NDK 的 Markdown 格式参考文档。

[English Version](./README_en.md)

## 核心特性 (v1.0.6+)

除了详尽的 API 参考外，本项目现已包含以下**专家级实战指南**：
- 🛠 **IDE 实操**：应用签名、断点调试、模拟器与真机配置、AI 智能辅助编程。
- 🤖 **独立工具链**：**独立命令行工具包 (Standalone CLI)** 的下载、环境变量配置及 CI/CD 深度调优。
- 📱 **多端适配**：一次开发多端部署（自适应/响应式布局）、折叠屏与平板专项适配。
- 🔄 **自由流转**：跨端迁移、多端协同的核心逻辑与开发步骤。
- ⚙️ **NDK 开发**：**Node-API (napi)** 基础、C++ 与 ArkTS 跨语言互调。
- 🚀 **应用发布**：AppGallery Connect 配置、发布证书申请、上架审核流程。
- 📈 **性能调优**：深入使用 DevEco Profiler 进行 CPU、内存、帧率及启动耗时分析。
- 🏗 **架构设计**：HAP/HAR/HSP 包结构深度解析、Stage 模型并发机制。
- 🧪 **自动化测试**：基于 Hypium 的单元测试与 UI 测试，以及 CI/CD 命令行集成。

## 工作原理

当你的编程助手需要 HarmonyOS 相关知识时，应使用本仓库作为检索层，而非依赖大模型的训练记忆（避免幻觉）。

**推荐查找流程：**
1. 查看 [`KITS.md`](harmony-next/references/KITS.md) 确定所属能力集。
2. 使用 [`TASK_MAP.md`](harmony-next/references/TASK_MAP.md) 将任务需求映射到技术关键词。
3. 从 [`INDEX.md`](harmony-next/references/INDEX.md) 中定位具体文件。
4. 遵循 [`SKILL.md`](harmony-next/SKILL.md) 中的规则，以获取精准的 API 级细节。

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
- `harmony-next/references/`: 3,403 份 Markdown 文档 (约 50 MB)。
- `harmony-next/SKILL.md`: 助手的检索规则与回答策略。
- `harmony-next.skill`: 由 GitHub Actions 自动生成的打包发布产物。

## 为什么需要它？
- **消除幻觉**：提供 HarmonyOS 5.0+ 真实 API 实现指导。
- **确定性回复**：为 Agent 工作流提供可寻址的文件参考。
- **离线支持**：在无网或受限环境下依然可以使用完整的 API 手册。

## 来源与许可
- 数据源：华为 HarmonyOS 官方文档。
- 本仓库为 AI 辅助开发工作流重新封装了这些参考资料。
