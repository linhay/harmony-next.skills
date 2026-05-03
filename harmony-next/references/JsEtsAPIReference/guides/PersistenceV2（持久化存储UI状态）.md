# PersistenceV2（持久化存储UI状态）

本文档用于承接原先跳转到官方 `arkts-new-persistencev2` 的说明。

## 用途

`PersistenceV2` 在 `AppStorageV2` 的基础上增加磁盘持久化能力，适合需要跨进程重建、跨启动恢复的 UI 状态数据。

## 典型能力

- `globalConnect`：创建或获取持久化状态
- `save`：手动持久化
- `notifyOnError`：注册持久化错误回调

## globalConnect支持集合的类型

当前仓库离线文档里已经记录了 `Array`、`Map`、`Set`、`Date` 以及部分类集合持久化场景。涉及数组或嵌套对象时，通常还要结合 `makeObserved` 或默认子创建器，避免持久化后的对象失去观察能力。

## 相关离线文档

- [@ohos.arkui.StateManagement（状态管理）中的 PersistenceV2](../modules/ohos/@ohos.arkui.StateManagement%20(状态管理).md#persistencev2)
- [makeObserved接口：将非观察数据变为可观察数据](makeObserved接口：将非观察数据变为可观察数据.md)
- [状态管理概述](状态管理概述.md#状态管理v2)
