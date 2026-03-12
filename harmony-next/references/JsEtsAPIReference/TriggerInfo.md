# TriggerInfo

作为[trigger](@ohos.app.ability.wantAgent (WantAgent模块).md#ZH-CN_TOPIC_0000002529444577__wantagenttrigger)的入参定义触发WantAgent所需要的信息。

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { wantAgent } from '@kit.AbilityKit';
```

#### 属性

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

名称类型只读可选说明codenumber否否表示传递的公共事件数据，仅当WantAgent实例的[OperationType](@ohos.app.ability.wantAgent (WantAgent模块).md#ZH-CN_TOPIC_0000002529444577__operationtype)类型是'SEND_COMMON_EVENT'时有效。该字段与发布者使用[commonEventManager.publish](@ohos.commonEventManager (公共事件模块).md#ZH-CN_TOPIC_0000002497445532__commoneventmanagerpublish-1)发布公共事件时，传递[CommonEventPublishData](CommonEventPublishData.md#ZH-CN_TOPIC_0000002497445534__属性)公共事件数据中的code字段含义一致。want[Want](@ohos.app.ability.Want (Want).md)否是对象间信息传递的载体，可以用于应用组件间的信息传递。permissionstring否是表示公共事件订阅者的权限。仅当WantAgent实例的[OperationType](@ohos.app.ability.wantAgent (WantAgent模块).md#ZH-CN_TOPIC_0000002529444577__operationtype)类型是'SEND_COMMON_EVENT'时，该字段生效。extraInfo{ [key: string]: any }否是额外数据。extraInfos11+Record<string, Object>否是额外数据。推荐使用该属性替代extraInfo，设置该属性后，extraInfo不再生效。