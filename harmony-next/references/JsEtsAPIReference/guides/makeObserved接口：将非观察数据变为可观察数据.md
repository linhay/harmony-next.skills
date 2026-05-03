# makeObserved接口：将非观察数据变为可观察数据

`UIUtils.makeObserved` 用于把“原本不会触发 V2 渲染刷新的对象”转换成可观察对象。它更接近“运行时补观察能力”的工具，而不是完整的 V1 -> V2 装饰器迁移方案。

API 原文可参考：

- [@ohos.arkui.StateManagement（状态管理）中的 makeObserved](../modules/ohos/@ohos.arkui.StateManagement%20(状态管理).md#ZH-CN_TOPIC_0000002553200701__makeobserved)

## 适用对象

典型适用对象包括：

- 未使用 `@ObservedV2` / `@Trace` 修饰的普通 class 实例
- `JSON.parse()` 返回的普通 object
- `Array`、`Map`、`Set`、`Date`
- 运行时拼装后需要直接参与渲染的对象

## 何时使用

当你遇到下面这些现象时，应优先检查是否需要 `makeObserved`：

- 修改对象内部字段后，V2 组件没有刷新
- 列表项、瀑布流项的子字段变化不触发重绘
- `Modifier` 或其他依赖对象字段的 UI 状态没有同步更新

如果问题本质上是：

- 组件内状态变量从 `@State/@Link/@Prop` 迁往 V2
- 数据对象从 `@Observed/@Track/@ObjectLink` 迁往 `@ObservedV2/@Trace`

那么应优先走 [状态管理V1-V2迁移指导](状态管理V1-V2迁移指导.md) 中的正式迁移路径，而不是直接用 `makeObserved` 代替全部改造。

## 使用建议

- 在对象进入 UI 之前转换，避免在深层子组件里重复包裹。
- 只转换真正参与渲染的对象，减少无意义代理。
- 对于简单的标量状态，优先继续使用普通状态变量，不必强行封装为对象。

## 相关迁移文档

- [状态管理V1-V2迁移指导](状态管理V1-V2迁移指导.md)
- [状态管理V1和V2混用指导（API version 19及之后）](状态管理V1和V2混用指导（API%20version%2019及之后）.md)
