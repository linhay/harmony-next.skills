# @ohos.app.appstartup.StartupConfigEntry (启动框架配置)

本模块提供[应用启动框架](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-startup)配置的能力。

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

#### 导入模块

```ets
import { StartupConfigEntry } from '@kit.AbilityKit';
```

#### StartupConfigEntry

#### onConfig

onConfig?(): StartupConfig

在回调[AbilityStage.onCreate](@ohos.app.ability.AbilityStage (AbilityStage组件管理器).md#ZH-CN_TOPIC_0000002529284571__oncreate)前，若该AbilityStage对应的HAP中启动框架配置文件中[定义了启动框架配置](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-startup#定义启动参数配置)，则会触发该回调。

开发者可以在该回调中设置启动框架配置信息，详细使用方法可参考[设置启动参数](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-startup#设置启动参数)章节。

**系统能力**：SystemCapability.Ability.AppStartup

**返回值：**

类型说明[StartupConfig](@ohos.app.appstartup.StartupConfig (启动框架配置信息).md#ZH-CN_TOPIC_0000002529444561__startupconfig)启动框架配置信息。

**示例：**

```ets
import { StartupConfig, StartupConfigEntry, StartupListener } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

export default class MyStartupConfigEntry extends StartupConfigEntry {
  onConfig() {
    hilog.info(0x0000, 'testTag', `onConfig`);
    let onCompletedCallback = (error: BusinessError<void>) => {
      hilog.info(0x0000, 'testTag', `onCompletedCallback`);
      if (error) {
        hilog.info(0x0000, 'testTag', 'onCompletedCallback: %{public}d, message: %{public}s', error.code,
          error.message);
      } else {
        hilog.info(0x0000, 'testTag', `onCompletedCallback: success.`);
      }
    }
    let startupListener: StartupListener = {
      'onCompleted': onCompletedCallback
    }
    let config: StartupConfig = {
      'timeoutMs': 10000,
      'startupListener': startupListener
    }
    return config;
  }
}
```

#### onRequestCustomMatchRule20+

onRequestCustomMatchRule(want: Want): string

在回调[AbilityStage.onCreate](@ohos.app.ability.AbilityStage (AbilityStage组件管理器).md#ZH-CN_TOPIC_0000002529284571__oncreate)前，若该AbilityStage对应的HAP中启动框架配置文件中[定义了启动框架配置](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-startup#定义启动参数配置)，则会在[StartupConfigEntry.onConfig](#ZH-CN_TOPIC_0000002497604596__onconfig)后触发该回调。

开发者可以在该回调中，可以根据调用方传入启动UIAbility的Want中的不同参数来返回不同的自定义匹配规则。启动框架会将其与启动任务配置的matchRules中customization字段进行匹配。若匹配成功，任务将在自动模式执行。详细匹配规则请参考[添加任务匹配规则](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-startup#添加任务匹配规则)章节。

该接口通常用于无法直接通过uri、action或意图名称规则来匹配启动任务的场景，可以使用本接口对匹配规则进一步细化。

**系统能力**：SystemCapability.Ability.AppStartup

**参数：**

参数名类型必填说明want[Want](@ohos.app.ability.Want (Want).md)是启动UIAbility的Want信息。

**返回值：**

类型说明string返回自定义匹配规则值，用于匹配启动任务是否自动执行。

**示例：**

```ets
import { StartupConfigEntry, Want } from '@kit.AbilityKit';

export default class MyStartupConfigEntry extends StartupConfigEntry {
  // ...

  onRequestCustomMatchRule(want: Want): string {
    if (want?.parameters?.customParam == 'param1') {
      return 'customRule1';
    }
    return '';
  }
}
```