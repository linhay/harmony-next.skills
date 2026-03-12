# ExtensionContext

ExtensionContext是[ExtensionAbility](@ohos.app.ability.ExtensionAbility (扩展能力基类).md)的上下文环境，继承自[Context](Context (Stage模型的上下文基类).md#ZH-CN_TOPIC_0000002529444589__context)。

ExtensionContext模块提供访问特定[ExtensionAbility](@ohos.app.ability.ExtensionAbility (扩展能力基类).md)的资源的能力。

- 本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
- 本模块接口仅可在Stage模型下使用。

#### 导入模块

```ets
import { common } from '@kit.AbilityKit';
```

#### 属性

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

名称类型只读可选说明currentHapModuleInfo[HapModuleInfo](HapModuleInfo.md)否否所属Hap包的信息。config[Configuration](@ohos.app.ability.Configuration (环境变量).md)否否所属Module的配置信息。extensionAbilityInfo[ExtensionAbilityInfo](ExtensionAbilityInfo.md)否否所属[ExtensionAbility](@ohos.app.ability.ExtensionAbility (扩展能力基类).md)的信息。

#### 使用场景

ExtensionContext主要用于查询所属ExtensionAbility的信息、Module的配置信息以及HAP包的信息，开发者可根据自身业务需求使用对应的信息。

**示例：**

在扩展的[FormExtensionAbility](@ohos.app.form.FormExtensionAbility (FormExtensionAbility).md)中获取上下文，查询该扩展的FormExtensionAbility所属HAP包等信息。

```ets
import { FormExtensionAbility, formBindingData } from '@kit.FormKit';
import { Want } from '@kit.AbilityKit';

export default class MyFormExtensionAbility extends FormExtensionAbility {
  onAddForm(want: Want) {
    console.info(`FormExtensionAbility onAddForm, want: ${want.abilityName}`);
    let extensionContext = this.context;
    let hapInfo = extensionContext.currentHapModuleInfo;
    console.info(`HAP name is: ${hapInfo.name}`);
    let dataObj1: Record<string, string> = {
      'temperature': '11c',
      'time': '11:00'
    };
    let obj1: formBindingData.FormBindingData = formBindingData.createFormBindingData(dataObj1);
    return obj1;
  }
};
```