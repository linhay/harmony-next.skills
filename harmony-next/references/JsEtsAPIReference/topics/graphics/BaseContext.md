# BaseContext

BaseContext抽象类用于表示继承的子类Context是Stage模型还是FA模型，是所有Context类型的父类。

本模块首批接口从API version 8 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { common } from '@kit.AbilityKit';
```

#### 属性

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

名称类型只读可选说明stageModeboolean否否

表示是否Stage模型。

true：[Stage模型](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ability-terminology#stage模型)。

false：[FA模型](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ability-terminology#fa模型)。

**示例：**

以Stage模型为例，用户可通过UIAbilityContext访问stageMode字段。

```ets
import { UIAbility, AbilityConstant, Want } from '@kit.AbilityKit';

class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    // EntryAbility onCreate, isStageMode: true
    console.info(`EntryAbility onCreate, isStageMode: ${this.context.stageMode}`);
  }
}
```