# @ohos.app.ability.abilityDelegatorRegistry ([AbilityDelegator](../../topics/misc/AbilityDelegator.md)Registry)

AbilityDelegatorRegistry是自动化测试框架使用指南模块，该模块用于获取[AbilityDelegator](AbilityDelegator.md)和[AbilityDelegatorArgs]([AbilityDelegatorArgs](../../topics/misc/AbilityDelegatorArgs.md).md)对象，其中[AbilityDelegator](AbilityDelegator.md)对象提供添加用于监视指定ability的生命周期状态更改的[AbilityMonitor](AbilityMonitor.md#ZH-CN_TOPIC_0000002553200531__abilitymonitor-1)对象的能力，[AbilityDelegatorArgs](AbilityDelegatorArgs.md)对象提供获取当前测试参数的能力。


本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在[单元测试框架](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/unittest-guidelines)中使用。

#### 导入模块

```ets
import { abilityDelegatorRegistry } from '@kit.TestKit';
```

#### AbilityLifecycleState

Ability生命周期状态，该类型为枚举，可配合[AbilityDelegator](AbilityDelegator.md)的[getAbilityState(ability)](AbilityDelegator.md#ZH-CN_TOPIC_0000002522241804__getabilitystate9)方法返回不同ability生命周期。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力** ：以下各项对应的系统能力均为SystemCapability.Ability.AbilityRuntime.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| UNINITIALIZED | 0 | 表示Ability处于无效状态。 |
| CREATE | 1 | 表示Ability处于已创建状态。 |
| FOREGROUND | 2 | 表示Ability处于前台状态。 |
| BACKGROUND | 3 | 表示Ability处于后台状态。 |
| DESTROY | 4 | 表示Ability处于已销毁状态。 |

#### abilityDelegatorRegistry.get[AbilityDelegator](../../topics/misc/AbilityDelegator.md)

get[AbilityDelegator](../../topics/misc/AbilityDelegator.md)(): AbilityDelegator

获取应用程序的[AbilityDelegator](AbilityDelegator.md)对象，该对象能够使用调度测试框架的相关功能。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AbilityDelegator](../../topics/misc/AbilityDelegator.md) | AbilityDelegator对象。可以用来调度测试框架相关功能。 |

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

getArguments(): [AbilityDelegator](../../topics/misc/AbilityDelegator.md)Args

获取单元测试参数[AbilityDelegatorArgs](AbilityDelegatorArgs.md)对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AbilityDelegator](../../topics/misc/AbilityDelegator.md)Args | AbilityDelegatorArgs对象。可以用来获取测试参数。 |

**示例：**

```ets
import { abilityDelegatorRegistry } from '@kit.TestKit';

let args = abilityDelegatorRegistry.getArguments();
console.info(`getArguments bundleName: ${args.bundleName}`);
console.info(`getArguments parameters: ${JSON.stringify(args.parameters)}`);
console.info(`getArguments testCaseNames: ${args.testCaseNames}`);
console.info(`getArguments testRunnerClassName: ${args.testRunnerClassName}`);
```

#### [AbilityDelegator](../../topics/misc/AbilityDelegator.md)

type [AbilityDelegator](../../topics/misc/AbilityDelegator.md) = [_AbilityDelegator](../../topics/misc/AbilityDelegator.md)

[AbilityDelegator](../../topics/misc/AbilityDelegator.md)模块。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

| 类型 | 说明 |
| --- | --- |
| _[AbilityDelegator](../../topics/misc/AbilityDelegator.md) | AbilityDelegator模块。 |

#### [AbilityDelegator](../../topics/misc/AbilityDelegator.md)Args

type [AbilityDelegator](../../topics/misc/AbilityDelegator.md)Args = [_AbilityDelegatorArgs](../../topics/misc/AbilityDelegatorArgs.md)

[AbilityDelegator](../../topics/misc/AbilityDelegator.md)Args模块。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

| 类型 | 说明 |
| --- | --- |
| _[AbilityDelegator](../../topics/misc/AbilityDelegator.md)Args | AbilityDelegatorArgs模块。 |

#### [AbilityMonitor](../../topics/misc/AbilityMonitor.md#ZH-CN_TOPIC_0000002497604618__abilitymonitor-1)

type [AbilityMonitor](../../topics/misc/AbilityMonitor.md#ZH-CN_TOPIC_0000002497604618__abilitymonitor-1) = [_AbilityMonitor](../../topics/misc/AbilityMonitor.md)

[AbilityMonitor](../../topics/misc/AbilityMonitor.md#ZH-CN_TOPIC_0000002497604618__abilitymonitor-1)模块。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

| 类型 | 说明 |
| --- | --- |
| _[AbilityMonitor](../../topics/misc/AbilityMonitor.md#ZH-CN_TOPIC_0000002497604618__abilitymonitor-1) | AbilityMonitor模块。 |

#### ShellCmdResult

type ShellCmdResult = [_ShellCmdResult](../../topics/misc/ShellCmdResult.md)

ShellCmdResult模块。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

| 类型 | 说明 |
| --- | --- |
| [_ShellCmdResult](../../topics/misc/ShellCmdResult.md) | ShellCmdResult模块。 |

#### AbilityStageMonitor14+

type AbilityStageMonitor = [_AbilityStageMonitor](../../topics/misc/AbilityStageMonitor.md)

AbilityStageMonitor模块。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

| 类型 | 说明 |
| --- | --- |
| [_AbilityStageMonitor](../../topics/misc/AbilityStageMonitor.md) | AbilityStageMonitor模块。 |