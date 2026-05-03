# applySync与flushUpdates与flushUIUpdates接口：同步刷新

本文档用于承接原先跳转到官方 `arkts-new-applysync-flushupdates-flushuiupdates` 的说明。

## 三者区别

- `applySync`
  只同步执行闭包内的状态修改，并同步触发 `@Computed`、`@Monitor` 和 UI 刷新。
- `flushUpdates`
  同步处理调用前已经累计的状态修改，并执行 `@Computed`、`@Monitor` 和 UI 刷新。
- `flushUIUpdates`
  只立即处理调用前累计的 UI 标脏与渲染，不同步执行 `@Computed` 和 `@Monitor`。

## 适用场景

- 需要显式控制 V2 状态修改的生效时机。
- 希望把多次状态更新收敛到同一个同步刷新点。
- 排查“修改发生了，但 UI / Monitor / Computed 执行时机不符合预期”的问题。

## 离线对应文档

- [@ohos.arkui.StateManagement（状态管理）中的 applySync](../modules/ohos/@ohos.arkui.StateManagement%20(状态管理).md#ZH-CN_TOPIC_0000002553200701__applysync22)
- [@ohos.arkui.StateManagement（状态管理）中的 flushUpdates](../modules/ohos/@ohos.arkui.StateManagement%20(状态管理).md#ZH-CN_TOPIC_0000002553200701__flushupdates22)
- [@ohos.arkui.StateManagement（状态管理）中的 flushUIUpdates](../modules/ohos/@ohos.arkui.StateManagement%20(状态管理).md#ZH-CN_TOPIC_0000002553200701__flushuiupdates22)
