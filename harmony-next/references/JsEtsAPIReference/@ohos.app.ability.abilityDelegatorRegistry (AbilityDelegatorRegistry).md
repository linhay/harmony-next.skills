# @ohos.app.ability.abilityDelegatorRegistry (AbilityDelegatorRegistry)

AbilityDelegatorRegistry是自动化测试框架使用指南模块，该模块用于获取[AbilityDelegator](AbilityDelegator.md)和[AbilityDelegatorArgs](AbilityDelegatorArgs.md)对象，其中[AbilityDelegator](AbilityDelegator.md)对象提供添加用于监视指定ability的生命周期状态更改的[AbilityMonitor](AbilityMonitor.md#ZH-CN_TOPIC_0000002497604618__abilitymonitor-1)对象的能力，[AbilityDelegatorArgs](AbilityDelegatorArgs.md)对象提供获取当前测试参数的能力。

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在[单元测试框架](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/unittest-guidelines)中使用。

#### 导入模块

```ets
import { abilityDelegatorRegistry } from '@kit.TestKit';
```

#### AbilityLifecycleState

Ability生命周期状态，该类型为枚举，可配合[AbilityDelegator](AbilityDelegator.md)的[getAbilityState(ability)](AbilityDelegator.md#ZH-CN_TOPIC_0000002497445712__getabilitystate9)方法返回不同ability生命周期。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力** ：以下各项对应的系统能力均为SystemCapability.Ability.AbilityRuntime.Core

名称值说明UNINITIALIZED0表示Ability处于无效状态。CREATE1表示Ability处于已创建状态。FOREGROUND2表示Ability处于前台状态。BACKGROUND3表示Ability处于后台状态。DESTROY4表示Ability处于已销毁状态。

#### abilityDelegatorRegistry.getAbilityDelegator

getAbilityDelegator(): AbilityDelegator

获取应用程序的[AbilityDelegator](AbilityDelegator.md)对象，该对象能够使用调度测试框架的相关功能。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**返回值：**

类型说明[AbilityDelegator](AbilityDelegator.md)[AbilityDelegator](AbilityDelegator.md)对象。可以用来调度测试框架相关功能。

**示例：**

```ets
import { abilityDelegatorRegistry } from '@kit.TestKit';
import { Want } from '@kit.AbilityKit';

let abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
let want: Want = {
  bundleName: 'com.example.myapplication',
  abilityName: 'EntryAbility'
};

abilityDelegator.startAbility(want, (err) => {
  if (err) {
    console.error(`Failed start ability, error: ${JSON.stringify(err)}`);
  } else {
    console.info('Success start ability.');
  }
});
```

#### abilityDelegatorRegistry.getArguments

getArguments(): AbilityDelegatorArgs

获取单元测试参数[AbilityDelegatorArgs](AbilityDelegatorArgs.md)对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**返回值：**

类型说明[AbilityDelegatorArgs](AbilityDelegatorArgs.md)[AbilityDelegatorArgs](AbilityDelegatorArgs.md)对象。可以用来获取测试参数。

**示例：**

```ets
import { abilityDelegatorRegistry } from '@kit.TestKit';

let args = abilityDelegatorRegistry.getArguments();
console.info(`getArguments bundleName: ${args.bundleName}`);
console.info(`getArguments parameters: ${JSON.stringify(args.parameters)}`);
console.info(`getArguments testCaseNames: ${args.testCaseNames}`);
console.info(`getArguments testRunnerClassName: ${args.testRunnerClassName}`);
```

#### AbilityDelegator

type AbilityDelegator = _AbilityDelegator

AbilityDelegator模块。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

类型说明[_AbilityDelegator](AbilityDelegator.md)AbilityDelegator模块。

#### AbilityDelegatorArgs

type AbilityDelegatorArgs = _AbilityDelegatorArgs

AbilityDelegatorArgs模块。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

类型说明[_AbilityDelegatorArgs](AbilityDelegatorArgs.md)AbilityDelegatorArgs模块。

#### AbilityMonitor

type AbilityMonitor = _AbilityMonitor

AbilityMonitor模块。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

类型说明[_AbilityMonitor](AbilityMonitor.md)AbilityMonitor模块。

#### ShellCmdResult

type ShellCmdResult = _ShellCmdResult

ShellCmdResult模块。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

类型说明[_ShellCmdResult](ShellCmdResult.md)ShellCmdResult模块。

#### AbilityStageMonitor14+

type AbilityStageMonitor = _AbilityStageMonitor

AbilityStageMonitor模块。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

类型说明[_AbilityStageMonitor](AbilityStageMonitor.md)AbilityStageMonitor模块。