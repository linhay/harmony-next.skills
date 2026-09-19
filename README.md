<p align="right">[<img src="https://img.shields.io/badge/Language-English-0f766e?style=for-the-badge" alt="readme-English" />](./README_en.md)</p>

# HarmonyOS NEXT Agent Skills

给 Gemini CLI、Claude Code、Codex 和其他 AI 编程助手使用的 HarmonyOS NEXT 离线技能包。

[![release](https://img.shields.io/github/v/release/linhay/harmony-next.skills?style=flat-square)](https://github.com/linhay/harmony-next.skills/releases/latest)
[![skills.sh](https://skills.sh/b/linhay/harmony-next.skills)](https://skills.sh/linhay/harmony-next.skills)
![docs](https://img.shields.io/badge/docs-4238-7c3aed?style=flat-square)
![api](https://img.shields.io/badge/API%2012--26-4207-b45309?style=flat-square)

> API 12–26 的本地 HarmonyOS 参考、ArkTS/ArkUI、NDK、DevEco Studio、模拟器自动化和发布调试工作流。

## 让 Agent 自动安装

把这段话发给你的 Agent：

<details>
<summary>展开安装提示词</summary>

```text
请安装并启用 linhay/harmony-next.skills 的 harmony-next skill。
先识别当前 Agent：
- Gemini CLI：gemini skills install https://github.com/linhay/harmony-next.skills --path harmony-next --scope user
- Claude Code：npx skills add linhay/harmony-next.skills --skill harmony-next -a claude-code -g -y --copy
- Codex：npx skills add linhay/harmony-next.skills --skill harmony-next -a codex -g -y --copy
- 其他支持 skills CLI 的 Agent：npx skills add linhay/harmony-next.skills --skill harmony-next
安装后读取 harmony-next/SKILL.md，确认 skill 名称和版本，并报告实际安装路径；命令不可用时给出手动安装路径，不要假设成功。
```

</details>

## 快速开始

```bash
npx skills add linhay/harmony-next.skills --skill harmony-next
```

安装后直接提出 HarmonyOS 开发问题。Agent 会按 `SKILL.md → KITS.md / TASK_MAP.md → INDEX.md` 查找本地资料。

## 能力总览

| 能力 | 适用场景 | 入口 |
| --- | --- | --- |
| API 参考 | ArkTS、ArkUI、系统模块、API 版本确认 | [`JsEtsAPIReference/INDEX.md`](./harmony-next/references/JsEtsAPIReference/INDEX.md) |
| Kit / 任务导航 | 按 Kit 或任务定位文档 | [`KITS.md`](./harmony-next/references/KITS.md) · [`TASK_MAP.md`](./harmony-next/references/TASK_MAP.md) |
| API 26 快照 | API 26.0.0 声明、类型和签名 | [`api26/`](./harmony-next/references/JsEtsAPIReference/api26/) |
| DevEco / Emulator | HVD、hdc、uitest、抓包和诊断 | [`DevEco模拟器私有接口与AI自动化.md`](./harmony-next/references/ideGuides/DevEco模拟器私有接口与AI自动化.md) |
| 最小工程 | Empty Ability、构建和 smoke 测试 | [`empty-ability-app`](./harmony-next/references/templates/empty-ability-app/) |
| 自动化脚本 | 设备证据、UI/UX、Trace、命令行工具 | [`scripts/`](./harmony-next/scripts/) |

关键词入口：**抓包诊断**、**DevEco 模拟器自动化**、**filesystem skill**、**Codex plugin**。

## 推荐检索路径

```text
SKILL.md → KITS.md / TASK_MAP.md → INDEX.md → 目标文档
```

## 安装方式

- Gemini CLI：`gemini skills install https://github.com/linhay/harmony-next.skills --path harmony-next --scope user`
- Claude Code：`npx skills add linhay/harmony-next.skills --skill harmony-next -a claude-code -g -y --copy`
- Codex：`npx skills add linhay/harmony-next.skills --skill harmony-next -a codex -g -y --copy`
- DSH：`dsh plugin --profile demo add github:linhay/harmony-next.skills`

DeepSeek Harness (DSH) 使用 filesystem skill；该 bundle 不安装 MCP、tools 或 apps。本仓库当前还不是 Codex plugin。

`empty-ability-app` smoke fixture：[`references/templates/empty-ability-app`](./harmony-next/references/templates/empty-ability-app/)。

私有接口工作流必须先阅读对应的私有接口文档，并明确产物目录、脱敏边界和非交互模式。

<details>
<summary>高级说明、脚本与维护</summary>

- [完整技能规则](./harmony-next/SKILL.md)
- [Agent 适配与安装路径](./docs/agent-portability.md)
- [API 26 发布与同步记录](./harmony-next/references/harmonyos-releases/api-26-release.md)
- [问题反馈指南](./harmony-next/ISSUE_GUIDE.md)

兼容安装路径：`npx skills add linhay/harmony-next.skills --list`、`$HOME/.agents/skills/harmony-next`、`DSH_SOURCE=/path/to/harmony-next.skills`、`.dsh/skills/harmony-next`、`dsh-harmony-next`。

API 26 声明快照可从新版 DevEco Studio 重新生成：

```bash
python3 harmony-next/scripts/sync_api26_snapshot.py \
  --deveco-app /path/to/DevEco-Studio.app
python3 harmony-next/scripts/reference_compat.py generate
```

发布前运行：

```bash
python3 harmony-next/scripts/check_packaging_docs.py
python3 harmony-next/scripts/reference_compat.py check
python3 -m unittest discover -s harmony-next/tests -p 'test_*.py' -v
```

</details>

## 版本

| 当前发布 | 说明 |
| --- | --- |
| `v1.3.37` | [API 26.0.0 Release 声明快照](https://github.com/linhay/harmony-next.skills/releases/tag/v1.3.37) 已纳入；官网 guide、示例和差异说明持续补充 |

## 许可证

MIT。文档来源为华为 HarmonyOS 官方资料，版权归原作者所有。
