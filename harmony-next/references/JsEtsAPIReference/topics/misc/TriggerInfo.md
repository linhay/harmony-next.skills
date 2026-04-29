# TriggerInfo

作为[trigger](@ohos.app.ability.wantAgent (WantAgent模块).md#ZH-CN_TOPIC_0000002522240560__wantagenttrigger)的入参定义触发WantAgent所需要的信息。


本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { wantAgent } from '@kit.AbilityKit';
```

#### 属性

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| code | number | 否 | 否 | 表示传递的公共事件数据，仅当WantAgent实例的OperationType类型是'SEND_COMMON_EVENT'时有效。该字段与发布者使用commonEventManager.publish发布公共事件时，传递[CommonEventPublishData](CommonEventPublishData.md#ZH-CN_TOPIC_0000002497445534__属性)公共事件数据中的code字段含义一致。 |
| want | Want | 否 | 是 | 对象间信息传递的载体，可以用于应用组件间的信息传递。 |
| permission | string | 否 | 是 | 表示公共事件订阅者的权限。仅当WantAgent实例的OperationType类型是'SEND_COMMON_EVENT'时，该字段生效。 |
| extraInfo | { [key: string]: any } | 否 | 是 | 额外数据。 |
| extraInfos11+ | Record<string, Object> | 否 | 是 | 额外数据。推荐使用该属性替代extraInfo，设置该属性后，extraInfo不再生效。 |
