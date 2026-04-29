# @ohos.app.ability.EmbeddedUIExtensionAbility (支持跨进程界面嵌入的ExtensionAbility组件)

EmbeddedUIExtensionAbility为开发者提供了跨进程界面嵌入的能力，继承自[UIExtensionAbility](@ohos.app.ability.UIExtensionAbility (带界面的ExtensionAbility组件).md)。

开发者通过实现EmbeddedUIExtensionAbility，为本应用提供跨进程界面嵌入能力。例如，开发者可以在[UIAbility](@ohos.app.ability.UIAbility (带界面的应用组件).md)的页面中通过[EmbeddedComponent]([EmbeddedComponent](../../topics/components/EmbeddedComponent.md).md)嵌入本应用的EmbeddedUIExtensionAbility提供的界面。

各类Ability的继承关系详见[继承关系说明](@ohos.app.ability.Ability (Ability基类).md#ZH-CN_TOPIC_0000002553360447__ability的继承关系说明)。


本模块首批接口从API version 12 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

#### 导入模块

```ets
import { EmbeddedUIExtensionAbility } from '@kit.AbilityKit';
```

#### EmbeddedUIExtensionAbility

EmbeddedUIExtensionAbility为开发者提供了跨进程界面嵌入的能力，继承自[UIExtensionAbility](@ohos.app.ability.UIExtensionAbility (带界面的ExtensionAbility组件).md)。

目前EmbeddedUIExtensionAbility只能被同应用的UIAbility拉起。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**设备行为差异**：该接口在PC/2in1、Tablet中可正常调用，在其他设备类型中无法被启动。