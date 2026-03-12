# AbilityStageMonitor

本模块提供监听指定[AbilityStage](@ohos.app.ability.AbilityStage (AbilityStage组件管理器).md)对象的能力。开发者可以将AbilityStageMonitor作为[abilityDelegator.waitAbilityStageMonitor](AbilityDelegator.md#ZH-CN_TOPIC_0000002497445712__waitabilitystagemonitor9)的入参来注册监听。

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### AbilityStageMonitor

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

名称类型只读可选说明moduleNamestring否否被监听的AbilityStage的模块名。srcEntrancestring否否被监听的AbilityStage的源路径。

**示例：**

```ets
import { abilityDelegatorRegistry } from '@kit.TestKit';

let monitor: abilityDelegatorRegistry.AbilityStageMonitor = {
  moduleName: 'feature_as1',
  srcEntrance: './ets/Application/MyAbilityStage.ts',
}

let abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.waitAbilityStageMonitor(monitor, (error, data) => {
  if (error) {
    console.error(`waitAbilityStageMonitor fail, error: ${JSON.stringify(error)}`);
  } else {
    console.info(`waitAbilityStageMonitor success, data: ${JSON.stringify(data)}`);
  }
});
```