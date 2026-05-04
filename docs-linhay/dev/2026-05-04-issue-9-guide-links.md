# issue 9 guide 离线化处理

日期：2026-05-04

## 背景

issue 9 指出仓库内与状态管理 V1/V2 迁移相关的引导链接仍然指向华为在线文档，离线场景不可用；同时本地参考库缺少对应的迁移指导页。

## 本次处理

1. 在 `harmony-next/references/JsEtsAPIReference/guides/` 下新增 3 个最小可用 guide：
   - `状态管理V1-V2迁移指导.md`
   - `状态管理V1和V2混用指导（API version 19及之后）.md`
   - `makeObserved接口：将非观察数据变为可观察数据.md`
2. 扩展 `harmony-next/scripts/reference_compat.py`：
   - 为明确收录的华为 guide slug 建立映射
   - `generate` 时重写目标外链为本地相对路径
   - `check` 时阻止这些目标外链残留
3. 重建 `references/INDEX.md` 与 `references/JsEtsAPIReference/INDEX.md`
4. 使用官方 `arkts-v1-v2-guide`、`arkts-state-management-v1-v2-migration-guide`、`arkts-v1-v2-migration-inner-component`、`arkts-v1-v2-migration-inner-class` 页面回校本地 guide 的目录结构与章节标题。
5. 继续清理同类状态管理外链，新增并映射：
   - `状态管理概述.md`
   - `@Observed与@ObjectLink：V1数据对象观测.md`
   - `@ObservedV2与@Trace：类属性变化观测.md`
   - `addMonitor与clearMonitor开发指南.md`
   - `applySync与flushUpdates与flushUIUpdates接口：同步刷新.md`
   - `AppStorageV2（应用全局的UI状态存储）.md`
   - `PersistenceV2（持久化存储UI状态）.md`
6. 第三轮继续清理“已有明确离线落点”的状态管理 / ArkUI 基础语义外链：
   - `arkts-state-management-introduce` -> `guides/状态管理概述.md`
   - `arkts-watch`、`arkts-new-monitor` -> `topics/components/状态变量变化监听.md`
   - `arkts-appstorage`、`arkts-localstorage`、`arkts-persiststorage` -> `topics/components/应用级变量的状态管理.md`
   - `arkts-create-custom-components` -> `topics/components/自定义组件.md`
   - `arkts-page-custom-components-lifecycle` -> `topics/components/自定义组件的生命周期.md`
7. 第四轮补收状态管理装饰器基础语义：
   - `arkts-state`
   - `arkts-state-management-glossary`
   - `arkts-provide-and-consume`
   - 统一离线到 `modules/ohos/@ohos.arkui.StateManagement (状态管理).md`
8. `reference_compat.py` 新增“可丢弃原在线锚点”的映射能力：
   - 对于落到本地 API 总览页但不存在对应锚点的 slug，不再保留原始华为页面锚点
   - 避免把在线链接重写成本地后留下无效锚点
9. 第五轮继续清理“已有明确离线落点”的通用 ArkUI guide 外链：
   - `arkts-global-interface` -> `types/classes/Class (UIContext).md`
   - `arkts-routing` -> `types/classes/Class (Router).md`
   - 两者统一丢弃原在线锚点，回落到本地总览页，避免保留无效锚点
10. 重新执行 `generate` / `check` 后，`arkts-global-interface` 与 `arkts-routing` 已无正文残留；剩余高频在线 guide 主要集中在：
   - `arkts-rendering-control-ifelse`
   - `arkts-sendable`
   - `arkts-two-way-sync`
   - `arkts-new-binding`
   - `arkts-builder`
   - `arkts-reusable`
11. 对上述剩余项的结论：
   - `arkts-rendering-control-ifelse`：未找到独立 `IfElse` 离线页，仅存在各组件页内的引用描述
   - `arkts-sendable`：本地只有 `@arkts.lang` 的 `ISendable` 定义与零散 API 引用，缺少覆盖“协议 / 装饰器 / 支持数据类型”的总览页
   - `arkts-two-way-sync`、`arkts-new-binding`：本地有零散组件参数说明与 `Binding/MutableBinding` API，但语义不等价于“系统组件参数双向绑定”总览
   - `arkts-builder`：本地存在大量 `@Builder` 用例与 `wrapBuilder` / `BuilderNode` 关联说明，但缺少独立总览页
   - `arkts-reusable`：本地只有 `@ReusableV2` 相关页和 V1 语义的被引用说明，缺少 `@Reusable` V1 独立总览页
12. 第六轮继续清理“已有明确离线落点”的组件与事件 guide 外链：
   - `arkts-common-components-text-input` -> `topics/components/TextInput.md`
   - `arkts-common-events-focus-event` -> `topics/components/焦点事件.md`
   - `pastebutton` -> `topics/components/PasteButton.md`
   - 三者统一丢弃原在线锚点，回落到本地组件页
13. 第六轮后重新审计剩余高频在线 guide：
   - `module-configuration-file`、`app-startup`、`uiability-usage` 等项在仓库中只能命中到若干 API / 上下文 / 快速开始页面
   - 但未找到与华为在线 guide 语义等价的一页式离线总览页
   - 因此本次停止继续重写，避免把外链误导到不对题的本地 API 页
14. 用户进一步放宽策略后，开始直接从华为官方文档接口抓取缺失 guide 的正文，并整理为本地离线版：
   - `window-terminology` -> `guides/窗口开发术语.md`
   - `uiability-usage` -> `guides/UIAbility组件基本用法.md`
   - `module-configuration-file` -> `guides/module.json5配置文件.md`
   - `app-startup` -> `guides/应用启动框架AppStartup.md`
   - `arkts-sendable` -> `guides/Sendable对象简介.md`
   - `arkts-builder` -> `guides/@Builder装饰器：自定义构建函数.md`
   - `arkts-two-way-sync` -> `guides/$$语法：系统组件双向同步.md`
   - `arkts-new-binding` -> `guides/!!语法：双向绑定.md`
   - `arkts-rendering-control-ifelse` -> `guides/if-else：条件渲染.md`
15. `reference_compat.py` 已纳入上述 9 个 slug；重新执行 `generate` 后，累计重写 88 个 guide-link 文件，`check` 通过。
16. 当前补文流程已验证可复用：
   - 通过官方 `getDocumentById` 接口按 `objectId=<slug>` 获取 HTML 正文
   - 只保留仓库中实际被引用的标题锚点与必要上下文，避免无差别整页镜像
   - 先落本地 `guides/*.md`，再扩 `TARGETED_GUIDE_MAPPING`，最后执行 `generate/check`
17. 第七轮继续按相同流程补齐上一轮剩余的高频在线 guide：
   - `data-backup-and-restore` -> `guides/数据库备份与恢复.md`
   - `mdm-kit-multi-mdm` -> `guides/多应用管控.md`
   - `terminology` -> `guides/Connectivity Kit术语.md`
   - `component-startup-rules` -> `guides/组件启动规则（Stage模型）.md`
   - `mdm-kit-guide` -> `guides/MDM Kit开发指南.md`
   - `declare-permissions-in-acl` -> `guides/申请受限权限.md`
   - `push-jwt-token` -> `guides/基于服务账号生成鉴权令牌.md`
   - `data-persistence-by-kv-store` -> `guides/通过键值型数据库实现数据持久化.md`
   - `declare-permissions` -> `guides/声明权限.md`
   - `ability-terminology` -> `guides/Ability Kit术语.md`
   - `application-context-stage` -> `guides/应用上下文Context.md`
   - `app-configuration-file` -> `guides/app.json5配置文件.md`
   - `component-startup-rules-fa` -> `guides/组件启动规则（FA模型）.md`
18. 第七轮后重新执行 `generate/check`：
   - `generate` 实际新增重写 75 个 guide-link 文件
   - `check` 通过
   - 上一轮列出的高频剩余项已全部从残留榜单消失
19. 当前新的高频在线 guide 头部已经切换为下一批待处理项：
   - `nfc-tag-access-guide`
   - `arkts-layout-development-grid-layout`
   - `serializable-overview`
   - `restricted-permissions`
   - `resource-categories-and-access`
   - `extensionability-overview`
   - `uiability-launch-type`
   - `get-pastedata-permission-guidelines`
   - `arkts-reusable`
   - `ui-design-hds-tabs-bar-floating`

## 约束

- 仅重写已经决定离线化的目标 guide slug，避免误改仓库内其他仍保留在线引用的官方文档。
- 若后续继续收录更多 guide，应先新增本地 Markdown，再把 slug 加入 `TARGETED_GUIDE_MAPPING`。
- 当前 `TARGETED_GUIDE_MAPPING` 同时兼容旧 slug（如 `arkts-v1-v2-migration-inner-object`）与新 slug（如 `arkts-v1-v2-guide` 系列）。
- 当前策略只清理“仓库已有明确离线落点”的状态管理 guide，不批量替换所有 HarmonyOS 外链。
- 当本地没有语义等价页，但仓库内出现稳定高频的官方 guide 外链时，允许直接基于官方正文整理“最小可用”的离线 guide，再接入映射。
- 当前仍未纳入批量替换的高频 slug 已切换为 `nfc-tag-access-guide`、`arkts-layout-development-grid-layout`、`serializable-overview`、`restricted-permissions`、`resource-categories-and-access`、`extensionability-overview` 等；后续继续按“先抓官方正文、再补本地 guide、最后接映射”的流程推进。
