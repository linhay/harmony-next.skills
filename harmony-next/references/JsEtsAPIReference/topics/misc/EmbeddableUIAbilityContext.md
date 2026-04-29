# EmbeddableUIAbilityContext

EmbeddableUIAbilityContext是[EmbeddableUIAbility](@ohos.app.ability.EmbeddableUIAbility (可嵌入式UIAbility组件).md)组件的上下文，继承自[UIAbilityContext](UIAbilityContext.md)。

每个EmbeddableUIAbility组件实例化时，系统都会自动创建对应的EmbeddableUIAbilityContext。

  ![image](public_sys-resources/note_3.0-zh-cn.webp)

- 本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

- 本模块接口仅可在Stage模型下使用。

- 本模块接口需要在主线程中使用，不要在Worker、TaskPool等子线程中使用。

**导入模块**

```ets
import { common } from '@kit.AbilityKit';
```

**EmbeddableUIAbilityContext**

开发者可以通过EmbeddableUIAbilityContext获取EmbeddableUIAbility的相关配置信息以及操作EmbeddableUIAbility和ServiceExtensionAbility的方法，如启动EmbeddableUIAbility，停止当前EmbeddableUIAbilityContext所属的EmbeddableUIAbility，启动、停止、连接、断开连接ServiceExtensionAbility等。

系统能力：SystemCapability.Ability.AbilityRuntime.Core

元服务API：从API version 12开始，该接口支持在元服务中使用。