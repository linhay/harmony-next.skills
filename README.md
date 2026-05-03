# HarmonyOS NEXT 开发者专家技能包

给 Gemini CLI、Claude Code、Codex 等 AI 编程助手使用的 HarmonyOS NEXT 离线参考技能库。

[![release](https://img.shields.io/badge/release-v1.3.1-1f6feb?style=flat-square)](https://github.com/linhay/harmony-next.skills/releases/tag/v1.3.1)
[![readme](https://img.shields.io/badge/readme-English-0f766e?style=flat-square)](./README_en.md)
![docs](https://img.shields.io/badge/docs-3,622%20markdown%20files-7c3aed?style=flat-square)
![js-ets](https://img.shields.io/badge/JsEtsAPIReference-3,598%20files-b45309?style=flat-square)

> 面向 API 12-23 的本地知识源，覆盖 ArkTS、ArkUI、NDK、工具链、调试、发布与多端适配。

## 它解决什么问题

`harmony-next.skills` 不是普通文档镜像，而是一套给 AI 编程助手使用的 HarmonyOS NEXT 检索层。

它主要解决这几类问题：

- `@ohos.*` 模块到底在哪个文件
- 某个 ArkUI 组件、接口或 NDK 头文件是否真的存在
- API 23 新增内容有没有纳入当前知识库
- 某个旧链接是否已经迁移、是否还能跳转

这个仓库的目标，是把这些问题变成可定位、可跳转、可验证的本地文件查询。

## 核心特性

| 能力 | 说明 |
| --- | --- |
| 离线可检索 | 不依赖模型记忆猜 API，先命中文档路径再读取正文 |
| 面向 Agent 工作流 | 按 `SKILL.md -> KITS/TASK_MAP -> INDEX` 组织，适合渐进式检索 |
| 不只 API 手册 | 还包含 IDE、签名、调试、发布、性能、多端与 NDK 实战指引 |

## 内容概览

| 模块 | 说明 | 入口 |
| --- | --- | --- |
| 技能规则 | 告诉 Agent 如何检索、如何回答、哪些内容要优先信文档 | [`harmony-next/SKILL.md`](./harmony-next/SKILL.md) |
| Kit 导航 | 按 AbilityKit、ArkUI、ArkData、MediaKit、Security 等缩小检索范围 | [`references/KITS.md`](./harmony-next/references/KITS.md) |
| 任务导航 | 按 UI、生命周期、网络、媒体、NDK、发布等任务反查关键词 | [`references/TASK_MAP.md`](./harmony-next/references/TASK_MAP.md) |
| 全库索引 | 收录整个参考库的 Markdown 路径，用于先命中路径再读正文 | [`references/INDEX.md`](./harmony-next/references/INDEX.md) |
| API 分桶索引 | 聚焦 `JsEtsAPIReference/`，覆盖 modules、topics、types、errors、guides | [`JsEtsAPIReference/INDEX.md`](./harmony-next/references/JsEtsAPIReference/INDEX.md) |
| 参考正文 | 共 `3,622` 份 Markdown，其中 `3,598` 份在 `JsEtsAPIReference/` | [`harmony-next/references/`](./harmony-next/references/) |

## 推荐检索路径

```text
SKILL.md
  -> KITS.md / TASK_MAP.md
  -> INDEX.md
  -> 目标 Markdown 正文
```

为什么这样设计：

1. 先定规则，避免 Agent 一上来就盲读大库。
2. 再按 Kit 或任务缩小范围，减少误命中。
3. 用索引命中真实路径，而不是凭名称想当然。
4. 最后只打开 1-3 个目标文件读 API 细节。

这套结构的核心是：先找路径，再读内容。

## 适用场景

### ArkTS / ArkUI 开发

- 组件、装饰器、状态管理、导航、UIAbility、Want
- API 版本差异、参数签名、返回值确认
- 组件示例与文档跳转恢复

### NDK / Node-API / C API

- 头文件对应到真实 `topics/**/<header>.h.md`
- 跨语言互调、CMake、原生能力接入
- 旧路径迁移后的索引与链接校验

### IDE / 工具链 / 调试

- 签名、模拟器、真机、断点调试
- 独立命令行工具链与 CI/CD 集成
- 性能分析与发布流程

### Agent 工程化集成

- Gemini CLI、Claude Code、Codex
- 本地知识库检索层
- 避免幻觉、提升可追踪性与可复现性

## 快速接入

### Gemini CLI

```bash
gemini skills install https://github.com/linhay/harmony-next.skills --path harmony-next --scope user
```

### Claude Code

1. 下载本仓库中的技能目录。
2. 按需压缩技能文件夹。
3. 在 Claude.ai 的 `Settings > Capabilities > Skills` 中上传。
4. 或直接放进你的 Claude Code 技能目录。

如果你只是想把仓库作为项目上下文附加：

```bash
git clone https://github.com/linhay/harmony-next.skills.git
claude --add-dir /path/to/harmony-next.skills/harmony-next
```

### Codex

更准确地说，这个仓库对 Codex 来讲是“技能/参考知识源”，不是一条 `npm install` 就完成的插件安装命令。

推荐接入方式：

1. 下载或克隆本仓库：

```bash
git clone https://github.com/linhay/harmony-next.skills.git
```

2. 将 `harmony-next/` 目录放到 Codex 可读取的技能路径下。

常见做法是放到你自己的 Codex 技能目录中，再让 Codex 从该目录加载；如果你已经有项目级技能目录，也可以直接把 `harmony-next/` 放进去。

3. 如果你不是按“技能目录”接入，而是把它当项目内参考库使用，至少应让 Codex 优先读取这两个入口文件：

- [`harmony-next/SKILL.md`](https://github.com/linhay/harmony-next.skills/blob/master/harmony-next/SKILL.md)
- [`harmony-next/references/INDEX.md`](https://github.com/linhay/harmony-next.skills/blob/master/harmony-next/references/INDEX.md)

一句话说清楚：对 Codex 来说，核心不是“安装一个包”，而是“把这份技能目录放到它会读取的位置”。

## v1.2.0 重点

| 版本 | 重点变化 |
| --- | --- |
| `v1.2.0` | API 23 相关内容纳入当前更新；重建 `references/INDEX.md` 与 `JsEtsAPIReference/INDEX.md`；移除旧 `capi/headers/*.md` 页面并改为直链真实目标；新增 `reference_compat.py` 与链接回归审计能力；同步中英文 README 与维护说明 |

## 参考库维护

当 `references/JsEtsAPIReference/` 发生同步、迁移或批量改写后，建议按下面顺序执行：

```bash
python3 harmony-next/scripts/reference_compat.py generate
python3 harmony-next/scripts/reference_compat.py check
python3 harmony-next/scripts/reference_compat.py audit
python3 -m unittest discover -s harmony-next/tests -p 'test_*.py' -v
```

命令职责：

- `generate`
  - 把旧的 `../../capi/headers/*.md` 引用改写到真实 `topics/**/<header>.h.md`
  - 重建 `references/INDEX.md` 与 `references/JsEtsAPIReference/INDEX.md`
- `check`
  - 校验旧 `capi/headers/` 页面已删除
  - 校验索引与磁盘一致
  - 校验正文里没有残留旧路径引用
- `audit`
  - 扫描当前未提交改动
  - 找出“原本有内部 Markdown 链接、现在被改成纯文本”的残留问题
- `unittest`
  - 校验迁移脚本与审计逻辑没有回归

## 为什么值得接入

| 价值 | 说明 |
| --- | --- |
| 更少幻觉 | 回答基于真实文档路径，而不是模型记忆补全 |
| 更易追溯 | 每个答案都能落回具体 Markdown 文件 |
| 更适合自动化 | 有索引、有规则、有校验，适合长期接入 Agent 工作流 |

## 来源与许可

- 数据源：华为 HarmonyOS 官方文档
- 本仓库：为 AI 辅助开发工作流重新封装这些参考资料

英文说明见 [README_en.md](./README_en.md)。
