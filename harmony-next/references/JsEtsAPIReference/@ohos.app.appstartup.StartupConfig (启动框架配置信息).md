# @ohos.app.appstartup.StartupConfig (启动框架配置信息)

本模块提供[应用启动框架](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-startup)配置信息的定义。

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

#### 导入模块

```ets
import { StartupConfig } from '@kit.AbilityKit';
```

#### StartupConfig

用于配置任务超时时间和启动框架的监听器。详细使用方法可参考[设置启动参数](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-startup#设置启动参数)章节。

**系统能力**：SystemCapability.Ability.AppStartup

名称类型只读可选说明timeoutMsnumber否是执行所有启动任务的超时时间（单位：毫秒），默认值为10000毫秒。startupListener[StartupListener](@ohos.app.appstartup.StartupListener (启动框架任务监听器).md)否是表示启动框架的监听器，该监听器将在所有启动任务完成时调用。

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
        hilog.error(0x0000, 'testTag', 'onCompletedCallback: %{public}d, message: %{public}s', error.code,
          error.message);
      } else {
        hilog.info(0x0000, 'testTag', `onCompletedCallback: success.`);
      }
    };
    let startupListener: StartupListener = {
      'onCompleted': onCompletedCallback
    };
    let config: StartupConfig = {
      'timeoutMs': 10000,
      'startupListener': startupListener
    };
    return config;
  }
}
```