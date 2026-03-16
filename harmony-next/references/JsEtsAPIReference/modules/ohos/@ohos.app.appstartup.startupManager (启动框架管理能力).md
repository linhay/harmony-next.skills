# @ohos.app.appstartup.startupManager (启动框架管理能力)

本模块提供[应用启动框架](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-startup)管理启动任务的能力，只能在主线程调用。

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块从API version 18开始支持so预加载。

本模块接口仅可在Stage模型下使用。

#### 导入模块

```ets
import { startupManager }  from '@kit.AbilityKit';
```

#### startupManager.run

run(startupTasks: Array<string>, config?: StartupConfig): Promise<void>

执行启动框架启动任务或加载so文件。

本接口不支持执行feature类型HAP中的启动任务，如需要使用相关能力请调用[startupManager.run](#ZH-CN_TOPIC_0000002529284589__startupmanagerrun20)接口。

**系统能力**：SystemCapability.Ability.AppStartup

**参数：**

参数名类型必填说明startupTasksArray<string>是表示准备执行的启动任务[StartupTask](@ohos.app.appstartup.StartupTask (启动框架任务).md)的名称或预加载so名称的数组。config[StartupConfig](@ohos.app.appstartup.StartupConfig (启动框架配置信息).md)否表示启动任务配置信息，包含启动框架超时时间与启动任务监听器配置。

**返回值：**

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**错误码：**

以下错误码详细介绍请参考[通用错误码](../../errors/通用错误码.md)和[元能力子系统错误码](../../errors/元能力子系统错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.16000050Internal error.28800001Startup task or its dependency not found.28800002The startup tasks have circular dependencies.28800003An error occurred while running the startup tasks.28800004Running startup tasks timeout.

**示例：**

```ets
import { AbilityConstant, UIAbility, Want, startupManager } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');
    let startParams = ['StartupTask_001', 'libentry_001'];
    try {
      // 手动调用run方法
      startupManager.run(startParams).then(() => {
        console.info(`StartupTest startupManager run then, startParams = ${startParams}.`);
      }).catch((error: BusinessError) => {
        console.error(`StartupTest promise catch failed, error code: ${error.code}, error msg: ${error.message}.`);
      });
    } catch (error) {
      let errMsg = (error as BusinessError).message;
      let errCode = (error as BusinessError).code;
      console.error(`Startup.run failed, err code: ${errCode}, err msg: ${errMsg}.`);
    }
  }

  // ...
}
```

#### startupManager.run20+

run(startupTasks: Array<string>, context: common.AbilityStageContext, config: StartupConfig): Promise<void>

执行启动框架启动任务或加载so文件。支持指定[AbilityStageContext](../../topics/graphics/AbilityStageContext.md)用于启动任务的加载。使用Promise异步回调。

**系统能力**：SystemCapability.Ability.AppStartup

**参数：**

参数名类型必填说明startupTasksArray<string>是表示准备执行的启动任务[StartupTask](@ohos.app.appstartup.StartupTask (启动框架任务).md)的名称或预加载so名称的数组。context[common.AbilityStageContext](../../topics/graphics/AbilityStageContext.md)是表示执行启动任务[StartupTask](@ohos.app.appstartup.StartupTask (启动框架任务).md)的AbilityStage上下文，作为入参传给启动任务的[init](@ohos.app.appstartup.StartupTask (启动框架任务).md#ZH-CN_TOPIC_0000002529444563__init)。config[StartupConfig](@ohos.app.appstartup.StartupConfig (启动框架配置信息).md)是表示启动任务配置信息，包含启动框架超时时间与启动任务监听器配置。

**返回值：**

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**错误码：**

以下错误码详细介绍请参考[元能力子系统错误码](../../errors/元能力子系统错误码.md)。

错误码ID错误信息16000050Internal error.28800001Startup task or its dependency not found.28800002The startup tasks have circular dependencies.28800003An error occurred while running the startup tasks.28800004Running startup tasks timeout.

**示例：**

```ets
import { AbilityStage, startupManager, StartupListener, StartupConfig } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class MyAbilityStage extends AbilityStage {
  onCreate(): void {
    hilog.info(0x0000, 'testTag', 'AbilityStage onCreate');
    let onCompletedCallback = (error: BusinessError<void>) => {
      if (error) {
        hilog.error(0x0000, 'testTag', 'onCompletedCallback error: %{public}s', JSON.stringify(error));
      } else {
        hilog.info(0x0000, 'testTag', 'onCompletedCallback: success.');
      }
    };
    let startupListener: StartupListener = {
      'onCompleted': onCompletedCallback
    };
    let config: StartupConfig = {
      'timeoutMs': 10000,
      'startupListener': startupListener
    };

    try {
      // 手动调用run方法
      startupManager.run(['StartupTask_001', 'libentry_001'], this.context, config).then(() => {
        hilog.info(0x0000, 'testTag', '%{public}s', 'startupManager.run success');
      }).catch((error: BusinessError<void>) => {
        hilog.error(0x0000, 'testTag', 'startupManager.run promise catch error: %{public}s', JSON.stringify(error));
      })
    } catch (error) {
      hilog.error(0x0000, 'testTag', 'startupManager.run catch error: %{public}s', JSON.stringify(error));
    }
  }
  // ...
}
```

#### startupManager.removeAllStartupTaskResults

removeAllStartupTaskResults(): void

删除所有启动任务结果。

如果存在so预加载任务，则将对应so文件置为未加载状态。对于缓存中已加载的so文件，不会被移除。

**系统能力**：SystemCapability.Ability.AppStartup

**示例：**

```ets
import { AbilityConstant, UIAbility, Want, startupManager } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');
    try {
      startupManager.run(['StartupTask_001', 'libentry_001']).then(() => {
        hilog.info(0x0000, 'testTag', 'StartupTask_001 init successful');
      }).catch((error: BusinessError) => {
        hilog.error(0x0000, 'testTag', `StartupTask_001 promise catch failed, error: %{public}s`,
          JSON.stringify(error) ?? '');
      });
    } catch (error) {
      hilog.error(0x0000, 'testTag', `StartupTask_001.run failed, error: %{public}s`, JSON.stringify(error) ?? '');
    }
  }

  onWindowStageCreate(windowStage: window.WindowStage) {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');
    startupManager.removeAllStartupTaskResults(); // 移除所有启动任务结果

    windowStage.loadContent('pages/Index', (err, data) => {
      if (err.code) {
        hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
        return;
      }
      hilog.info(0x0000, 'testTag', 'Succeeded in loading the content. Data: %{public}s', JSON.stringify(data) ?? '');
    });
  }
}
```

#### startupManager.getStartupTaskResult

getStartupTaskResult(startupTask: string): Object

获取指定启动任务或so预加载任务的执行结果。

**系统能力**：SystemCapability.Ability.AppStartup

**参数：**

参数名类型必填说明startupTaskstring是启动任务[StartupTask](@ohos.app.appstartup.StartupTask (启动框架任务).md)的名称或预加载so名称。

**返回值：**

类型说明Object

输入为启动任务名时，返回指定的启动任务[init](@ohos.app.appstartup.StartupTask (启动框架任务).md#ZH-CN_TOPIC_0000002529444563__init)返回的执行结果。

输入为so文件名时，返回undefined。

**错误码：**

以下错误码详细介绍请参考[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.

**示例：**

```ets
import { AbilityConstant, UIAbility, Want, startupManager } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');
    try {
      startupManager.run(['StartupTask_001']).then(() => {
        hilog.info(0x0000, 'testTag', 'StartupTask_001 init successful');
      }).catch((error: BusinessError) => {
        hilog.error(0x0000, 'testTag', `StartupTask_001 promise catch failed, error: %{public}s`,
          JSON.stringify(error) ?? '');
      });
    } catch (error) {
      hilog.error(0x0000, 'testTag', `StartupTask_001.run failed, error: %{public}s`, JSON.stringify(error) ?? '');
    }
  }

  onWindowStageCreate(windowStage: window.WindowStage) {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');
    let result = startupManager.getStartupTaskResult('StartupTask_001'); // 手动获取启动任务结果
    hilog.info(0x0000, 'testTag', 'getStartupTaskResult result = %{public}s', result);
    windowStage.loadContent('pages/Index', (err, data) => {
      if (err.code) {
        hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
        return;
      }
      hilog.info(0x0000, 'testTag', 'Succeeded in loading the content. Data: %{public}s', JSON.stringify(data) ?? '');
    });
  }
}
```

#### startupManager.isStartupTaskInitialized

isStartupTaskInitialized(startupTask: string): boolean

获取指定启动任务或so预加载任务是否已初始化。

**系统能力**：SystemCapability.Ability.AppStartup

**参数：**

参数名类型必填说明startupTaskstring是启动任务[StartupTask](@ohos.app.appstartup.StartupTask (启动框架任务).md)的名称或预加载so名称。

**返回值：**

类型说明boolean返回布尔值，true表示该启动任务或so预加载任务已执行完成，false表示该启动任务或so预加载任务尚未执行完成。

**错误码：**

以下错误码详细介绍请参考[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.

**示例：**

```ets
import { AbilityConstant, UIAbility, Want, startupManager } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');
    try {
      startupManager.run(['StartupTask_001', 'libentry_001']).then(() => {
      hilog.info(0x0000, 'testTag', 'StartupTask_001 init successful');
      }).catch((error: BusinessError) => {
        hilog.error(0x0000, 'testTag', `StartupTask_001 promise catch failed, error: %{public}s`,
          JSON.stringify(error) ?? '');
      });
    } catch (error) {
      hilog.error(0x0000, 'testTag', `StartupTask_001.run failed, error: %{public}s`, JSON.stringify(error) ?? '');
    }
  }

  onWindowStageCreate(windowStage: window.WindowStage) {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');
    let result1 = startupManager.isStartupTaskInitialized('StartupTask_001');
    let result2 = startupManager.isStartupTaskInitialized('libentry_001');
    if (result1) {
      console.info('StartupTask_001 init successful');
    } else {
      console.info('StartupTask_001 uninitialized');
    }
    if (result2) {
      console.info('libentry_001 init successful');
    } else {
      console.info('libentry_001 uninitialized');
    }

    windowStage.loadContent('pages/Index', (err, data) => {
      if (err.code) {
        hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
        return;
      }
      hilog.info(0x0000, 'testTag', 'Succeeded in loading the content. Data: %{public}s', JSON.stringify(data) ?? '');
    });
  }
}
```

#### startupManager.removeStartupTaskResult

removeStartupTaskResult(startupTask: string): void

删除指定启动任务或so预加载任务的初始化结果。

-

输入为启动任务名时，删除指定启动任务的初始化结果。

-

输入为so文件时，将该so文件置为未加载，缓存中已加载的so文件不会被移除。

**系统能力**：SystemCapability.Ability.AppStartup

**参数：**

参数名类型必填说明startupTaskstring是启动任务[StartupTask](@ohos.app.appstartup.StartupTask (启动框架任务).md)的名称或预加载so名称。

**错误码：**

以下错误码详细介绍请参考[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.

**示例：**

```ets
import { AbilityConstant, UIAbility, Want, startupManager } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');
    try{
      startupManager.run(['StartupTask_001', 'libentry_001']).then(() => {
        hilog.info(0x0000, 'testTag', 'StartupTask_001 init successful');
      }).catch((error: BusinessError) => {
        hilog.error(0x0000, 'testTag', `StartupTask_001 promise catch failed, error: %{public}s`,
          JSON.stringify(error) ?? '');
      });
    } catch (error) {
      hilog.error(0x0000, 'testTag', `StartupTask_001.run failed, error: %{public}s`, JSON.stringify(error) ?? '');
    }
  }

  onWindowStageCreate(windowStage: window.WindowStage) {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');
    startupManager.removeStartupTaskResult('StartupTask_001');
    startupManager.removeStartupTaskResult('libentry_001');

    windowStage.loadContent('pages/Index', (err, data) => {
      if (err.code) {
        hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
        return;
      }
      hilog.info(0x0000, 'testTag', 'Succeeded in loading the content. Data: %{public}s', JSON.stringify(data) ?? '');
    });
  }
}
```