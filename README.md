<p align="right">
  <a href="./README_en.md" title="[readme-English](./README_en.md)"><img src="https://img.shields.io/badge/Language-English-0f766e?style=for-the-badge" alt="readme-English" /></a>
</p>

# 🧰 HarmonyOS NEXT 开发者专家技能包

给 Gemini CLI、Claude Code、Codex 等 AI 编程助手使用的 HarmonyOS NEXT 离线参考技能库。

[![release](https://img.shields.io/github/v/release/linhay/harmony-next.skills?style=flat-square)](https://github.com/linhay/harmony-next.skills/releases/latest)
[![skills.sh](https://skills.sh/b/linhay/harmony-next.skills)](https://skills.sh/linhay/harmony-next.skills)
![docs](https://img.shields.io/badge/docs-3,708%20markdown%20files-7c3aed?style=flat-square)
![js-ets](https://img.shields.io/badge/JsEtsAPIReference-3,678%20files-b45309?style=flat-square)

> 面向 API 12-23 的本地知识源，覆盖 ArkTS、ArkUI、NDK、工具链、调试、发布与多端适配。

## 🎯 解决的问题

AI 编程助手在 HarmonyOS 开发中经常碰到的几类问题：

- 找不到 `@ohos.*` 模块的真实文档
- 不确定某个 ArkUI 组件或 NDK 头文件是否存在
- API 版本差异、新增内容未纳入知识库
- 旧文档链接失效或迁移
- DevEco Studio 模拟器、`hdc`、`uitest` 等本地自动化的验证路径不清晰

本仓库把这些不确定性变成**可定位、可跳转、可验证的本地文件查询**。

## Before / After

**没有 skill**：模型凭记忆猜 `@ohos.*` 模块、ArkUI 组件名或 DevEco 命令，答案看起来合理但缺少来源。

**使用本 skill**：先按 `SKILL.md → KITS.md / TASK_MAP.md → INDEX.md` 命中文档路径，再打开目标 Markdown，最后给出代码片段和 `hdc` / `uitest` / wrapper 脚本验证命令。

## ✨ 核心特性

- **完全离线检索**：不依赖模型记忆，先命中文档路径再读取正文
- **为 Agent 工作流设计**：按 `SKILL.md → KITS/TASK_MAP → INDEX` 层层递进检索
- **覆盖范围广**：不只 API 手册，还包含 IDE、签名、调试、发布、性能、NDK 实战指引
- **私有能力隔离**：DevEco 模拟器、IDE 未公开接口单独成章，默认先验证版本和风险
- **自动化优先**：支持非交互式自动化策略，提供证据采集、UI/UX 离线体检、trace 审计等脚本
- **可运行的最小工程**：提供 `empty-ability-app` 模板，可直接复制用于 smoke 测试

## 📚 内容导览

| 入口 / 模块 | 用途 |
| --- | --- |
| [`SKILL.md`](./harmony-next/SKILL.md) | 技能规则唯一来源：告诉 Agent 如何检索、哪些内容优先信文档 |
| [`references/KITS.md`](./harmony-next/references/KITS.md) | 按 Kit 导航（AbilityKit、ArkUI、ArkData…） |
| [`references/TASK_MAP.md`](./harmony-next/references/TASK_MAP.md) | 按任务反查（UI、网络、媒体、NDK…） |
| [`references/INDEX.md`](./harmony-next/references/INDEX.md) | 全库文件索引（3,708 个 Markdown 路径） |
| [`JsEtsAPIReference/INDEX.md`](./harmony-next/references/JsEtsAPIReference/INDEX.md) | API 分桶索引（modules、topics、errors…） |
| [`references/templates/empty-ability-app`](./harmony-next/references/templates/empty-ability-app/) | 可复制的 HarmonyOS NEXT smoke fixture（最小工程） |
| [`docs/agent-portability.md`](./docs/agent-portability.md) | Agent 安装与适配路径说明 |
| `harmony-next/references/` | 所有 Markdown 正文（含 3,678 个 API 文档） |

**自动化与诊断脚本**（按需使用）：

| 脚本 | 功能 | 入口命令示例 |
| --- | --- | --- |
| [`commandline_tools_manager.py`](./harmony-next/scripts/commandline_tools_manager.py) | Command Line Tools 下载与安装 | `python3 harmony-next/scripts/commandline_tools_manager.py install ...` |
| [`device_evidence_bundle.py`](./harmony-next/scripts/device_evidence_bundle.py) | 设备证据采集与 WebView DevTools 转发诊断 | `python3 harmony-next/scripts/device_evidence_bundle.py webview-devtools ...` |
| [`device_ui_action.py`](./harmony-next/scripts/device_ui_action.py) | 单次 UI 操作与前后证据采集 | `python3 harmony-next/scripts/device_ui_action.py tap ...` |
| [`ux_audit_pipeline.py`](./harmony-next/scripts/ux_audit_pipeline.py) | 一键离线 UI/UX 体检 | `python3 harmony-next/scripts/ux_audit_pipeline.py doctor ...` |
| [`profiler_trace_audit.py`](./harmony-next/scripts/profiler_trace_audit.py) | 离线 Trace 性能审计 | `python3 harmony-next/scripts/profiler_trace_audit.py audit ...` |
| [`hvd_manager.py`](./harmony-next/scripts/hvd_manager.py) | HVD 设备管理 | `python3 harmony-next/scripts/hvd_manager.py doctor ...` |

**特殊领域文档**：

- [`DevEco模拟器私有接口与AI自动化.md`](./harmony-next/references/ideGuides/DevEco模拟器私有接口与AI自动化.md)
- [`ArkWeb WebView CDP调试与字段到达证明.md`](./harmony-next/references/ideGuides/ArkWeb%20WebView%20CDP调试与字段到达证明.md)
- [`DevEco Studio IDE私有接口与AI自动化.md`](./harmony-next/references/ideGuides/DevEco%20Studio%20IDE私有接口与AI自动化.md)
- [`minimal-project-scaffold.md`](./harmony-next/references/quickStart/ets/minimal-project-scaffold.md)

## 🚀 快速接入

### 通用方式（推荐）

```bash
npx skills add linhay/harmony-next.skills
```

当前仓库只有一个 skill，直接运行上面的命令会自动安装 `harmony-next`。如果想先查看可用技能：

```bash
npx skills add linhay/harmony-next.skills --list
```

### Gemini CLI

```bash
gemini skills install https://github.com/linhay/harmony-next.skills --path harmony-next --scope user
```

### Claude Code

```bash
npx skills add linhay/harmony-next.skills --skill harmony-next -a claude-code -g -y --copy
```

或手动添加仓库目录：

```bash
git clone https://github.com/linhay/harmony-next.skills.git
claude --add-dir /path/to/harmony-next.skills/harmony-next
```

### Codex

```bash
npx skills add linhay/harmony-next.skills --skill harmony-next -a codex -g -y --copy
```

> 本仓库当前还不是 Codex plugin；`npx skills` 只会把 skill 安装到 Codex 可扫描的 skill 目录，不会安装 MCP/tools/apps。

也可手动放入官方路径（常用如 `$HOME/.agents/skills/harmony-next`；完整路径见 [`docs/agent-portability.md`](./docs/agent-portability.md)）。

### DeepSeek Harness（DSH）

本仓库提供官方 DSH profile bundle `dsh-harmony-next`。推荐通过 DSH profile 安装：

```bash
# 从 GitHub 安装
dsh plugin --profile demo add github:linhay/harmony-next.skills

# 或从本地 checkout 安装
dsh plugin --profile demo add /path/to/harmony-next.skills

# 检查 bundle layer
dsh --profile demo --dump-config
```

Bundle 只注册 `harmony-next` skill 及其离线参考资源，不安装 MCP、tools 或 apps。DSH bundle 的 manifest 是根目录的 `package.json`，patch 是 `cordis.patch.yml`。

如果只需要 filesystem skill，也可以手动安装到 DSH 的兼容根目录：

```bash
# DSH_SOURCE 指向本仓库的本地 checkout
DSH_SOURCE=/path/to/harmony-next.skills

# 项目级 skill
mkdir -p .dsh/skills/harmony-next
cp -R "$DSH_SOURCE/harmony-next/." .dsh/skills/harmony-next/

# 或用户级 skill（默认 ~/.dsh/skills）
mkdir -p "$HOME/.dsh/skills/harmony-next"
cp -R "$DSH_SOURCE/harmony-next/." "$HOME/.dsh/skills/harmony-next/"
```

DSH 也支持 `.agents/skills`、`$DSH_AGENTS_HOME/skills` 等兼容根目录；发现优先级和更新方式见 [`docs/agent-portability.md`](./docs/agent-portability.md)。

各 Host 只负责加载 skill；HarmonyOS 检索规则以 `harmony-next/SKILL.md` 为准。

## 🧭 推荐检索路径

```text
SKILL.md → KITS.md / TASK_MAP.md → INDEX.md → 目标 Markdown
```

设计原则：先定规则，再按 Kit 或任务缩小范围，用索引命中真实路径，最后只打开 1-3 个文件读细节。

## 📦 适用场景

- **ArkTS / ArkUI 开发**：组件、装饰器、状态管理、UIAbility 等 API 确认与示例
- **NDK / C API**：头文件对应真实文档、跨语言调用、CMake 配置
- **IDE / 工具链 / 调试**：签名、模拟器、真机调试、性能分析与发布流程
- **DevEco 模拟器自动化**：免 IDE 启动、HVD、`hdc`/`uitest` 自动化、抓包诊断
- **DevEco IDE 私有能力**：CodeGenie、ArkUI Inspector、离线 trace 审计、UI/UX 体检
- **Agent 工程化集成**：作为 Gemini CLI、Claude Code、Codex 的本地知识检索层

### ⚠️ 安全边界：私有接口与本地自动化

涉及 **DevEco 模拟器、IDE 私有接口、设备日志、截图、抓包、HVD 创建/删除**等操作时，**必须先阅读对应的私有接口文档**。这些流程要求：

- 执行前验证 DevEco / Emulator / SDK 版本和命令能力
- 明确产物目录、脱敏边界和失败时的 `blocked` 输出
- 非交互模式下的执行策略、超时与脱敏契约

私有接口文档入口：

- [`DevEco模拟器私有接口与AI自动化.md`](./harmony-next/references/ideGuides/DevEco模拟器私有接口与AI自动化.md)
- [`DevEco Studio IDE私有接口与AI自动化.md`](./harmony-next/references/ideGuides/DevEco%20Studio%20IDE私有接口与AI自动化.md)

<details>
<summary>展开：模拟器/IDE 私有接口使用规则摘要</summary>

**DevEco 模拟器私有接口** 触发词：`DevEco Studio`、`HarmonyOS Emulator`、`免 IDE 启动`、`HVD`、`hdc`、`uitest`、`aa`、`bm`、`snapshot_display` 等。
规则：先读 `SKILL.md` 的私有接口章节，每次执行前重新验证版本和能力；在用户已授权的本地环境内，自动化策略用于描述执行模式、产物目录和脱敏契约；wrapper 脚本阻塞时建议先尝试官方 CLI 路径采集证据。

**DevEco Studio IDE 私有接口** 触发词：`CodeGenie`、`MCP`、`devecostudio://`、`inspect.sh`、`ArkUI Inspector`、`Profiler`、`UxTestService` 等。
规则：默认只做静态只读分析（插件 XML、jar、配置、离线 trace 等）；启动 IDE/GUI、本地服务、设备连接、MCP 配置等需记录目标、产物和脱敏边界；离线 trace 审计和 UI/UX 体检只使用已验证的 wrapper 脚本和规则子集。

完整细节请务必查阅上述两份文档。
</details>

## 📈 版本重点

| 版本 | 关键更新 |
| --- | --- |
| `v1.3.35` | 增加 DeepSeek Harness（DSH）官方 profile bundle 与 filesystem skill fallback 适配 |
| `v1.3.30` | 模拟器应用沙箱速查与 HVD doctor 的 DevEco Emulator 优先级修正 |
| `Unreleased` | 一键离线 UI/UX 体检 CLI（`ux_audit_pipeline.py`） |
| `Unreleased` | 设备调试证据包 CLI（`device_evidence_bundle.py`） |
| `Unreleased` | 离线 Trace 性能审计 CLI（`profiler_trace_audit.py`） |
| `Unreleased` | HVD launch 改进：trace socket 守护、镜像校验、许可协议处理 |
| `Unreleased` | WebView DevTools 诊断、CDP 字段证明、单次 UI 操作证据与 Emulator 崩溃分类 |
| `v1.3.23` | Release workflow 更新到 Node 24 |
| `v1.3.7` | 新增可复制最小测试工程模板；SDK 版本适配验证（含 6.0.2(22)）；`uitest` smoke |
| `v1.3.6` | 模拟器非交互自动化策略 |
| `v1.3.5` | DevEco Studio IDE 私有接口参考 |
| `v1.2.0` | API 23 纳入；索引重建；链接兼容审计 |

## 🔧 维护与贡献

参考库更新后运行校验：

```bash
python3 harmony-next/scripts/check_packaging_docs.py
python3 harmony-next/scripts/reference_compat.py generate
python3 harmony-next/scripts/reference_compat.py check
python3 harmony-next/scripts/reference_compat.py audit
python3 -m unittest discover -s harmony-next/tests -p 'test_*.py' -v
```

## 📜 来源与许可

- 数据源：华为 HarmonyOS 官方文档
- 本仓库为 AI 辅助开发重新封装，英文说明见 [README_en.md](./README_en.md)

---

感谢 [LINUX DO](https://linux.do/) 的支持。

[![Star History Chart](https://api.star-history.com/svg?repos=linhay/harmony-next.skills&type=Date)](https://www.star-history.com/#linhay/harmony-next.skills&Date)
