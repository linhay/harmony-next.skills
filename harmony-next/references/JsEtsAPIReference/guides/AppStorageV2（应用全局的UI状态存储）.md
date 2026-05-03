# AppStorageV2（应用全局的UI状态存储）

本文档用于承接原先跳转到官方 `arkts-new-appstoragev2` 的说明。

## 用途

`AppStorageV2` 用于在应用级范围保存 V2 UI 状态数据，适合跨页面、跨组件共享的全局 UI 状态。

## 典型能力

- `connect`：创建或获取全局状态数据
- `remove`：删除指定 key
- `keys`：查看当前保存的 key

## 相关离线文档

- [@ohos.arkui.StateManagement（状态管理）中的 AppStorageV2](../modules/ohos/@ohos.arkui.StateManagement%20(状态管理).md#appstoragev2)
- [状态管理概述](状态管理概述.md#状态管理v2)
- [应用级变量的状态管理](../topics/components/应用级变量的状态管理.md)
