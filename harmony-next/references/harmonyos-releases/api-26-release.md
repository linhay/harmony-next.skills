# HarmonyOS SDK 26.0.0（API 26）发布追踪

更新时间：2026-09-15

本地验证对象：`inputs/DevEco-Studio.app/Contents/sdk/default/sdk-pkg.json`（随 issue 30 提供的 DevEco Studio 26.0.0 环境）。

## 当前结论

华为开发者文档中心列出的 **HarmonyOS SDK 26.0.0 Release** 于 2026-08-29 发布，底座为 OpenHarmony SDK `Ohos_sdk_public 26.0.0.105`，对应 API Version `26.0.0 Release`。

本仓库的 `references/` 仍是 API 12–23 的离线快照，因此本文件是版本追踪和适配入口，不代表 API 26 的接口正文已经随包提供。涉及 API 26 新增、变更或废弃接口时，应先查华为在线 API Change List，再回到本地索引确认是否存在对应页面。

## 本地 SDK 取证

提供的 SDK 清单确认：`apiVersion=26`、`platformVersion=26.0.0`、`releaseType=Release`、构建版本 `26.0.0.105`。该 SDK 包含 4,174 个 TypeScript 声明文件，其中 `openharmony/js/api/` 下有 470 个公共 JS/ETS 声明入口；这些声明可用于 API 存在性和签名比对，但不包含本仓库 Markdown 快照中的完整中文说明、示例和兼容性段落。

因此本轮先完成版本证据和检索入口同步；API 26 声明快照已从本地 SDK 导入至 `JsEtsAPIReference/api26/`，可用于离线检索 API 名称、签名和类型；官方完整说明、示例和兼容性段落仍需后续补齐。

## 版本号注意事项

从 API 26.0.0 开始，HarmonyOS API 版本号统一采用 SemVer（`X.Y.Z`）格式，取代此前以括号标识 API level 的版本写法。文档、构建配置和问题反馈中应保留完整的 `26.0.0`，不要把它简写成无法区分 Release/Beta 的 `26`。

## 适配入口

- 官方发布总览：[HarmonyOS SDK 26.0.0 Release](https://developer.huawei.com/consumer/cn/doc/doccenter-release-notes/overview-2600)
- 版本号规则：[API 版本号说明](https://developer.huawei.com/consumer/cn/doc/doccenter-release-notes/version-number-26)
- 升级指南：[Upgrading to 26.0.0](https://developer.huawei.com/consumer/en/doc/harmonyos-releases/upgrade-adaptation)
- API 差异：在华为文档中按 Kit 查看“APIs Introduced in 26.0.0 Release”列表，并记录具体 d.ts 或模块页面后再更新本地快照。

## 后续同步清单

1. 获取 API 26.0.0 Release 的官方 API 文档包并保留来源版本信息。
2. 将新增或变更页面放入 `JsEtsAPIReference/`，同时重建 `INDEX.md`、`KITS.md` 和 `TASK_MAP.md`。
3. 更新 README、`SKILL.md` 的覆盖范围，并运行 `check_packaging_docs.py`、`reference_compat.py` 和测试套件。
