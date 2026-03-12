# @ohos.app.ability.ActionExtensionAbility (支持业务操作自定义的ExtensionAbility组件)

ActionExtensionAbility是为开发者提供的自定义操作业务模板，继承自[UIExtensionAbility](@ohos.app.ability.UIExtensionAbility (带界面的ExtensionAbility组件).md)。

开发者通过实现ActionExtensionAbility，为其他应用提供内容查看与处理功能。例如，开发者使用ActionExtensionAbility实现了文本翻译功能。其他应用可以通过调用该ActionExtensionAbility来处理需要翻译的内容，并获取到处理后的翻译内容。

各类Ability的继承关系详见[继承关系说明](@ohos.app.ability.Ability (Ability基类).md#ZH-CN_TOPIC_0000002529444543__ability的继承关系说明)。

本模块首批接口从API version 10 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

#### 导入模块

```ets
import { ActionExtensionAbility } from '@kit.AbilityKit';
```

#### ActionExtensionAbility

ActionExtensionAbility是为开发者提供的自定义操作业务模板，继承自[UIExtensionAbility](@ohos.app.ability.UIExtensionAbility (带界面的ExtensionAbility组件).md)。

ActionExtensionAbility主要用于实现宿主应用的内容查看及交互处理功能。例如，添加一个书签、将选中的文本翻译成其他语言、在当前页面编辑图像等。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore