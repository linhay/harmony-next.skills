# DeepSeek Harness（DSH）主动适配调研 Space

日期：2026-08-15

状态：官方 profile bundle、文件系统 fallback、静态检查和真实 DSH catalog smoke test 均已通过

## 目标

确认 `linhay/harmony-next.skills` 如何以当前官方契约接入 DeepSeek Harness（`dsh`），并区分“文件系统 skill 适配”和“运行时 Cordis 插件适配”，避免沿用已经废弃的 `.dsh-plugin` 路线。

## 研究边界

- 本 Space 只记录公开源码、公开文档和本仓库静态结构。
- 本轮只在隔离临时目录安装 DSH、运行本地 Web Host 和调用 catalog API；不修改开发者真实 DSH 用户目录、不使用真实凭据、不连接设备或真实 HarmonyOS 工程。
- DSH 当前仍是 developer preview，后续实现必须把版本和契约漂移作为显式风险。
- 结论优先引用官方仓库；社区仓库只用于观察生态形态，不作为官方规范来源。

## 结论摘要

### 1. `dsh` 的目标对象已确认

这里的 `dsh` 是 DeepSeek Harness。官方仓库的定位是“Everything is a Plugin”，但它把可复用 Agent 指令单独抽象成 skill capability；本项目现在同时提供官方 profile bundle 和文件系统 skill fallback。bundle 只挂载本仓库已有的 `harmony-next` skill，不额外安装 MCP、tools 或 apps。

### 2. 当前项目已经满足 DSH 的核心 skill 文件契约

官方本地 provider 支持以下 skill 形态：

- 目录 bundle：`<skill-root>/<name>/SKILL.md`
- 平铺文件：`<skill-root>/<name>.md`
- skill 名称必须匹配 kebab-case：`^[a-z0-9]+(?:-[a-z0-9]+)*$`
- frontmatter 至少需要 `name` 和 `description`

本项目已有：

```text
harmony-next/SKILL.md
```

且 frontmatter 中的 `name: harmony-next`、`description: ...` 均符合要求；`metadata.version` 属于允许保留的附加元数据。因此，手动接入时把 `harmony-next/` 放入 DSH 的任一兼容根目录即可被发现；profile bundle 则通过根目录 `index.js` 注册同一份 skill provider。

### 3. DSH 当前默认发现根目录

官方 `dsh-skill-filesystem` 的优先级如下：

| 优先级 | 来源 | 根目录 |
| ---: | --- | --- |
| 100 | project-dsh | `<projectRoot>/.dsh/skills` |
| 200 | project-agents | `<projectRoot>/.agents/skills` |
| 300 | custom | `customSkillDirs` |
| 400 | user-dsh | `$DSH_HOME/skills`，默认 `~/.dsh/skills` |
| 500 | user-agents | `$DSH_AGENTS_HOME/skills`，默认 `~/.agents/skills` |

因此，DSH 的手动接入目标路径应是：

```text
<project>/.dsh/skills/harmony-next/SKILL.md
<project>/.agents/skills/harmony-next/SKILL.md
~/.dsh/skills/harmony-next/SKILL.md
~/.agents/skills/harmony-next/SKILL.md
```

### 4. 当前采用官方 profile bundle，不使用 `.dsh-plugin`

官方实现记录显示，旧的 repository-plugin / `.dsh-plugin` authoring format 已移除；当前独立运行时插件的分发入口是 profile bundle：npm 包在 `package.json` 中声明：

```json
{
  "dsh": {
    "bundle": {
      "patch": "./cordis.patch.yml"
    }
  }
}
```

再通过 `dsh plugin --profile <name> add <package-or-git-spec>` 安装。本项目已按该官方 bundle 契约补齐根目录 `package.json`、`cordis.patch.yml` 和 `index.js`：patch 声明 bundle，provider 从包内 `harmony-next/SKILL.md` 读取并注册 skill，同时暴露离线 references。这样不引入已移除的 `.dsh-plugin` 格式，也不把脚本误装成 MCP、tools 或 apps。

## 现状与差距

| 项目 | 当前状态 | 判断 |
| --- | --- | --- |
| skill 目录结构 | `harmony-next/SKILL.md` | 已满足 DSH directory-bundle 形态 |
| skill 名称 | `harmony-next` | 已满足 kebab-case |
| frontmatter | `name`、`description`、`metadata.version` | 已满足当前解析要求 |
| 文档入口 | README 有 DSH profile bundle 和文件系统 fallback 安装说明 | 已覆盖官方安装与边界 |
| 可移植性文档 | `docs/agent-portability.md` 有 DSH Host 表和路径说明 | 已覆盖 bundle、fallback 与验证 |
| DSH bundle manifest | 根目录 `package.json` 声明 `dsh.bundle.patch`，配套 `cordis.patch.yml` | 已满足 profile bundle 安装契约 |
| DSH bundle provider | 根目录 `index.js` 注册 `dsh-harmony-next` provider | 已复用现有 `harmony-next/SKILL.md` 和离线 references |
| DSH 文件系统 fallback | `.dsh/skills`、`.agents/skills`、`$DSH_HOME/skills`、`$DSH_AGENTS_HOME/skills` | 保留手动安装路径 |
| DSH 实机验证 | 隔离临时 profile + `@deepseek-ai/dsh@0.1.0-rc.6` | bundle 安装、配置投影和 Web catalog 均已通过 |

## 已执行的 DSH smoke test

测试使用独立临时目录、独立 `DSH_HOME` 和独立 `DSH_AGENTS_HOME`，没有读取或修改开发者真实的 DSH 配置、skill 目录、凭据或持久化会话。

### 测试入口

```text
dsh plugin --profile demo add <local-checkout>
dsh --profile demo --dump-config
dsh plugin --profile web add <local-checkout>
@deepseek-ai/dsh@0.1.0-rc.6 web --host 127.0.0.1 --port <free-port>
POST /api/session.create
POST /api/skill.list
```

每个 case 都先创建一个 cwd 指向测试项目的 session，再以 `client-request` envelope 查询该 session 的 skill catalog，断言返回 `harmony-next`、完整 description 和 `modelInvocable: true`。

### 测试结果

| Case | Skill 文件位置 | 结果 | 返回 |
| --- | --- | --- | --- |
| profile bundle install | `dsh plugin --profile demo add <local-checkout>` | PASS | profile manifest contains `dsh-harmony-next` |
| profile config projection | `dsh --profile demo --dump-config` | PASS | patch contains `harmony-next-skill` |
| bundle Web catalog | `dsh plugin --profile web add <local-checkout>` + Web API | PASS | `harmony-next`, `modelInvocable: true`, `skillCount: 1` |
| project-dsh fallback | `<projectRoot>/.dsh/skills/harmony-next/SKILL.md` | PASS | `harmony-next`, `modelInvocable: true`, `skillCount: 1` |
| user-dsh fallback | `$DSH_HOME/skills/harmony-next/SKILL.md` | PASS | `harmony-next`, `modelInvocable: true`, `skillCount: 1` |

这次 smoke test 验证了 DSH Web Host 的真实发现、frontmatter 解析和 catalog 投影；没有发送模型请求，因此不把 provider credential、模型执行或完整 body 注入误报为已验证。仓库新增的静态测试会继续保证入口目录、kebab-case 名称和必需 frontmatter 不漂移。

## 推荐适配切分

### P0：官方 profile bundle 与文件系统兼容（已完成）

1. 已在根目录增加官方 bundle 所需的 `package.json`、`cordis.patch.yml` 和 `index.js`；provider 只注册现有 `harmony-next` skill 及其离线 references。
2. 已在 `README.md`、`README_en.md` 和 `docs/agent-portability.md` 增加 profile bundle 安装、dump-config、文件系统 fallback 和边界说明。
3. 已在现有 Python unittest、`check_packaging_docs.py`、Node syntax check 和 npm pack dry-run 中增加静态契约检查：manifest、patch、provider、入口文件、名称、frontmatter 和包内路径不会漂移。

### P1：隔离 smoke test（已完成）

在临时目录构造 profile bundle 和 filesystem fallback：

```text
<tmp-project>/.git/
<local-checkout>/{package.json,cordis.patch.yml,index.js,harmony-next/}
<tmp-project>/.dsh/skills/harmony-next/SKILL.md
```

已验证 DSH 能列出 `harmony-next`，并在后续有可控模型/运行时 fixture 时再验证按名称加载完整 body；未在没有模型凭据的情况下伪造 body 注入结果。

### P2：版本漂移维护

当前 bundle 已满足 `dsh plugin --profile ... add ...` 一键安装，但 DSH 仍是 developer preview。后续发布 DSH 新版本时，需要重新核对 profile bundle、Cordis patch 和 skill provider 契约；不要把当前内部 patch 结构当成长期稳定 API。若未来要挂载工具或 MCP，应另行扩展并单独验证，不应隐式改变本 bundle 的 skill-only 边界。

## 证据来源

- [DeepSeek Harness README](https://github.com/deepseek-ai/deepseek-harness/blob/master/README.md)：官方定位、developer preview、`dsh-plugin` 发现入口。
- [DSH Skills subsystem](https://github.com/deepseek-ai/deepseek-harness/blob/master/docs/subsystems/skills.md)：skill provider、目录形态、名称和发现优先级。
- [DSH skill filesystem README](https://github.com/deepseek-ai/deepseek-harness/blob/master/packages/skill/skill-filesystem/README.md)：默认根目录与配置字段。
- [Publish a DSH plugin bundle](https://github.com/deepseek-ai/deepseek-harness/blob/master/docs/user/develop/basic/publish.md)：`package.json`、`dsh.bundle.patch` 和 `dsh plugin ... add` 的官方发布流程。
- [Profile plugin bundles note](https://github.com/deepseek-ai/deepseek-harness/blob/master/.agents/notes/implemented/architecture/2026-08-05-profile-plugin-bundles.md)：当前 bundle 分发模型。
- [Remove repository Plugin path note](https://github.com/deepseek-ai/deepseek-harness/blob/master/.agents/notes/implemented/simplification/2026-08-09-remove-repository-plugin.md)：`.dsh-plugin` 路线已移除的证据。
- 本项目：[harmony-next/SKILL.md](../../../harmony-next/SKILL.md)、[README.md](../../../README.md)、[agent-portability.md](../../../docs/agent-portability.md)。

## 下一步

适配、文档、静态检查和隔离 catalog smoke 已完成。后续按 DSH 版本更新重新跑同一套检查；若需要验证模型侧 `/harmony-next` 注入，再补充受控模型 fixture，不把无凭据环境下的 catalog 结果扩大解释为模型执行验证。
