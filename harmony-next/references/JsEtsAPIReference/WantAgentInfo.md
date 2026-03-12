# WantAgentInfo

定义触发WantAgent所需要的信息。

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { wantAgent as abilityWantAgent } from '@kit.AbilityKit';
```

#### WantAgentInfo

定义触发WantAgent所需要的信息，可以作为[getWantAgent](@ohos.app.ability.wantAgent (WantAgent模块).md#ZH-CN_TOPIC_0000002529444577__wantagentgetwantagent)的入参创建指定的WantAgent对象。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

名称类型只读可选说明wantsArray<[Want](@ohos.app.ability.Want (Want).md)>否否

将被执行的动作列表。wants数组为预留能力，当前只支持一个want。传入多个时只取wants数组的第一个成员。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

operationType(deprecated)[wantAgent.OperationType](@ohos.wantAgent (WantAgent模块).md#ZH-CN_TOPIC_0000002497444666__operationtype)否是

动作类型。

从API version 7 开始支持，从API version 11 开始废弃，建议使用actionType11+替代。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

actionType11+[abilityWantAgent.OperationType](@ohos.app.ability.wantAgent (WantAgent模块).md#ZH-CN_TOPIC_0000002529444577__operationtype)否是

动作类型。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

requestCodenumber否否

开发者自定义的请求码，用于标识将被执行的动作。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

wantAgentFlags(deprecated)Array<[wantAgent.WantAgentFlags](@ohos.wantAgent (WantAgent模块).md#ZH-CN_TOPIC_0000002497444666__wantagentflags)>否是

动作执行属性。

从API version 7 开始支持，从API version 11 开始废弃，建议使用actionFlags11+替代。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

actionFlags11+Array<[abilityWantAgent.WantAgentFlags](@ohos.app.ability.wantAgent (WantAgent模块).md#ZH-CN_TOPIC_0000002529444577__wantagentflags)>否是

动作执行属性。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

extraInfo{ [key: string]: any }否是

额外数据。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

extraInfos11+Record<string, Object>否是

额外数据。推荐使用该属性替代extraInfo，设置该属性后，extraInfo不再生效。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。