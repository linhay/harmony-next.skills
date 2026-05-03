# @Observed与@ObjectLink：V1数据对象观测

本文档用于承接原先跳转到官方 `arkts-observed-and-objectlink` 的说明。

## 核心关系

- `@Observed` 用于声明 class 实例可被 V1 观察。
- `@ObjectLink` 用于在组件间传递并观察这类对象，常见于嵌套对象场景。
- 如果需要更细粒度的属性观察，通常还会和 `@Track` 一起使用。

## 适用场景

- 组件需要依赖对象内部属性变化刷新。
- 父子组件之间传递的是被 V1 观察的对象，而不是简单标量。
- 还处于 V1 体系或 V1/V2 迁移过渡期。

## 离线对应文档

- [状态管理V1-V2迁移指导](状态管理V1-V2迁移指导.md#数据对象状态变量迁移)
- [@ohos.arkui.StateManagement（状态管理）中的 makeV1Observed](../modules/ohos/@ohos.arkui.StateManagement%20(状态管理).md#ZH-CN_TOPIC_0000002553200701__makev1observed19)
- [状态管理V1装饰器参数](../topics/components/状态管理V1装饰器参数.md)
