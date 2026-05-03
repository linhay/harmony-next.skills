# @ObservedV2与@Trace：类属性变化观测

本文档用于承接原先跳转到官方 `arkts-new-observedv2-and-trace` 的说明。

## 核心关系

- `@ObservedV2` 说明一个 class 可以被 V2 状态系统观察。
- `@Trace` 用于标记真正需要精确跟踪变化的属性。
- 两者通常成对出现：只有 class 可观察还不够，关键属性还需要 `@Trace`。

## 适用场景

- V2 组件依赖对象内部属性变化刷新。
- 需要比 V1 更清晰的对象级观察模型。
- 从 `@Observed/@ObjectLink/@Track` 迁往 V2 体系。

## 相关离线文档

- [状态管理V1-V2迁移指导](状态管理V1-V2迁移指导.md#数据对象状态变量迁移)
- [状态变量变化监听](../topics/components/状态变量变化监听.md)
- [makeObserved接口：将非观察数据变为可观察数据](makeObserved接口：将非观察数据变为可观察数据.md)
