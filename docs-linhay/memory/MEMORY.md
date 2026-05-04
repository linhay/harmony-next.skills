# MEMORY

- 2026-05-04：状态管理 V1/V2 迁移相关的 3 个官方 guide 已开始在仓库内做定向离线化，链接重写由 `harmony-next/scripts/reference_compat.py` 维护。
- 2026-05-04：`reference_compat.py` 的状态管理 guide 映射同时兼容旧版 `arkts-v1-v2-migration-*` 和新版 `arkts-v1-v2-guide` / `arkts-state-management-v1-v2-migration-guide` slug。
- 2026-05-04：状态管理相关的 `AppStorageV2`、`PersistenceV2`、`@ObservedV2/@Trace`、`addMonitor/clearMonitor`、`applySync/flushUpdates/flushUIUpdates`、`@Env`、`状态管理概述` 等 guide 已纳入离线映射。
- 2026-05-04：状态管理 / ArkUI 基础语义中的 `arkts-watch`、`arkts-new-monitor`、`arkts-appstorage`、`arkts-localstorage`、`arkts-persiststorage`、`arkts-state`、`arkts-state-management-glossary`、`arkts-provide-and-consume`、`arkts-create-custom-components`、`arkts-page-custom-components-lifecycle` 已纳入定向离线映射。
- 2026-05-04：`reference_compat.py` 支持对指定 slug 丢弃原在线锚点；仅在本地目标页没有等价锚点时启用，避免生成无效本地锚点。
- 2026-05-04：当仓库内不存在语义等价页，但官方 guide 外链在参考库中高频出现时，允许直接基于华为官方 `getDocumentById` 接口抓取正文，整理为 `JsEtsAPIReference/guides/*.md` 后再纳入 `reference_compat.py` 映射。
