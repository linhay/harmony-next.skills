# addMonitor与clearMonitor开发指南

本文档用于承接原先跳转到官方 `arkts-new-addmonitor-clearmonitor` 的说明。

## 用途

`UIUtils.addMonitor` / `UIUtils.clearMonitor` 用于给状态管理 V2 的状态变量动态注册或移除监听方法，适合运行时按路径监听对象变化的场景。

## 限制条件

- 目标对象仅支持 `@ComponentV2` 或 `@ObservedV2` 实例。
- 监听路径需要是合法的状态变量路径。
- 回调函数需要符合 `MonitorCallback` 约束。

## 离线对应文档

- [@ohos.arkui.StateManagement（状态管理）中的 addMonitor](../modules/ohos/@ohos.arkui.StateManagement%20(状态管理).md#ZH-CN_TOPIC_0000002553200701__addmonitor20)
- [@ohos.arkui.StateManagement（状态管理）中的 clearMonitor](../modules/ohos/@ohos.arkui.StateManagement%20(状态管理).md#ZH-CN_TOPIC_0000002553200701__clearmonitor20)
- [状态变量变化监听](../topics/components/状态变量变化监听.md)
