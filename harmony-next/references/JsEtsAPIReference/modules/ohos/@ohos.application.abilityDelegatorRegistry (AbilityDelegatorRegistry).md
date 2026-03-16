# @ohos.application.abilityDelegatorRegistry (AbilityDelegatorRegistry)

AbilityDelegatorRegistry模块提供用于存储已注册的[AbilityDelegator](../../topics/system-services/AbilityDelegator.md)和[AbilityDelegatorArgs](../../topics/system-services/AbilityDelegatorArgs.md)对象的全局寄存器的能力，包括获取应用程序的AbilityDelegator对象、获取单元测试参数AbilityDelegatorArgs对象。该模块中的接口只能用于测试框架中。

本模块首批接口从API version 8开始支持，从API version 9废弃，替换模块为[@ohos.app.ability.abilityDelegatorRegistry](@ohos.app.ability.abilityDelegatorRegistry (AbilityDelegatorRegistry).md)。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import AbilityDelegatorRegistry from '@ohos.application.abilityDelegatorRegistry';
```

#### AbilityLifecycleState

Ability生命周期状态。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

名称值说明UNINITIALIZED0表示无效状态。CREATE1表示Ability处于已创建状态。FOREGROUND2表示Ability处于前台状态。BACKGROUND3表示Ability处于后台状态。DESTROY4表示Ability处于已销毁状态。

#### abilityDelegatorRegistry.getAbilityDelegator

getAbilityDelegator(): AbilityDelegator

获取应用程序的AbilityDelegator对象。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**返回值：**

类型说明[AbilityDelegator](../../topics/system-services/AbilityDelegator.md)[AbilityDelegator](../../topics/system-services/AbilityDelegator.md)对象。可以用来调度测试框架相关功能。

**示例：**

```ets
import AbilityDelegatorRegistry from '@ohos.application.abilityDelegatorRegistry';

let abilityDelegator = AbilityDelegatorRegistry.getAbilityDelegator();
```

#### abilityDelegatorRegistry.getArguments

getArguments(): AbilityDelegatorArgs

获取单元测试参数AbilityDelegatorArgs对象。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**返回值：**

类型说明[AbilityDelegatorArgs](../../topics/system-services/AbilityDelegatorArgs.md)[AbilityDelegatorArgs](../../topics/system-services/AbilityDelegatorArgs.md)对象。可以用来获取测试参数。

**示例：**

```ets
import AbilityDelegatorRegistry from '@ohos.application.abilityDelegatorRegistry';

let args = AbilityDelegatorRegistry.getArguments();
console.info(`getArguments bundleName: ${args.bundleName}`);
console.info(`getArguments testCaseNames: ${args.testCaseNames}`);
console.info(`getArguments testRunnerClassName: ${args.testRunnerClassName}`);
```