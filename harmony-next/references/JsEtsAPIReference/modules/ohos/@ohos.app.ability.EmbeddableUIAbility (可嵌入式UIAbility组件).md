# @ohos.app.ability.EmbeddableUIAbility (可嵌入式UIAbility组件)

EmbeddableUIAbility组件是为元服务提供可嵌入式的UIAbility组件，继承自[UIAbility](@ohos.app.ability.UIAbility (带界面的应用组件).md)。

开发者通过实现EmbeddableUIAbility，为其他应用提供跳出式启动和嵌入式启动元服务方式。

各类Ability的继承关系详见[继承关系说明](@ohos.app.ability.Ability (Ability基类).md#ZH-CN_TOPIC_0000002529444543__ability的继承关系说明)。

本模块首批接口从API version 12 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

#### 导入模块

```ets
import { EmbeddableUIAbility } from '@kit.AbilityKit';
```

#### EmbeddableUIAbility

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

名称类型只读可选说明context[EmbeddableUIAbilityContext](../../topics/graphics/EmbeddableUIAbilityContext.md)否否EmbeddableUIAbility组件的上下文。