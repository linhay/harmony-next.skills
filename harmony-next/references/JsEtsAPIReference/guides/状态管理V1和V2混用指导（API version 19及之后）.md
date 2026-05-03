# 状态管理V1和V2混用指导（API version 19及之后）

本文档对应官方“状态管理V1和V2混用场景”在 API version 19 及之后的路径，用于处理“页面或父组件仍在状态管理 V1，局部子树已经迁移到 `@ComponentV2`”的过渡阶段。

核心 API 参考：

- [enableV2Compatibility](../modules/ohos/@ohos.arkui.StateManagement%20(状态管理).md#ZH-CN_TOPIC_0000002553200701__enablev2compatibility19)
- [makeV1Observed](../modules/ohos/@ohos.arkui.StateManagement%20(状态管理).md#ZH-CN_TOPIC_0000002553200701__makev1observed19)

## 适用场景

- 父组件仍使用 V1 装饰器和 V1 状态对象。
- 子组件已经迁移到 `@ComponentV2`，但短期内无法同步重写整条数据链路。
- 需要先保证迁移期间的刷新正确性，再逐步完成整体改造。

## 推荐方案

### V1 状态对象传入 V2 组件

当 V1 状态对象需要被 `@ComponentV2` 观察时，优先使用 `enableV2Compatibility`。它的职责是让 V1 状态数据在 V2 组件中具备可观察能力。

使用时要注意：

- 只对 V1 状态数据使用该接口。
- 优先在边界处转换，也就是从 V1 组件传给 V2 组件之前。
- 迁移完成后应回收这层兼容，避免长期保留双模型桥接。

### 普通对象先补成 V1 可观察对象

如果手头还是普通对象，但下游链路依赖 V1 的 `@ObjectLink` 等能力，可先用 `makeV1Observed` 转成 V1 可观察对象，再在需要时配合 `enableV2Compatibility` 进入 V2 子树。

### 判断优先级

可以按下面顺序判断：

1. 如果对象本来就是 V1 状态数据，优先考虑 `enableV2Compatibility`。
2. 如果对象还不是 V1 可观察对象，但下游链路依赖 V1 能力，先 `makeV1Observed`，再视需要接 `enableV2Compatibility`。
3. 如果正在开发全新 V2 链路，不要引入这套兼容层，直接改为纯 V2 状态建模。

## 边界与限制

- `enableV2Compatibility` 面向 V1 状态数据，不是普通对象的通用替代品。
- `makeV1Observed` 不适用于 V2 数据，也不适用于 `makeObserved` 的返回值。
- 这套方案是迁移过渡层，不是新代码的默认模式。

## 迁移顺序建议

1. 先明确当前对象属于 V1 状态、普通对象还是 V2 可观察对象。
2. 仅在 V1/V2 边界处引入兼容转换。
3. 功能稳定后，再逐步把上游状态和下游组件统一到 V2。
