# ApplicationContext (应用上下文)

ApplicationContext作为应用上下文，继承自[Context](Context (Stage模型的上下文基类).md)，提供了应用生命周期监听、进程管理、应用环境设置等应用级别的管控能力。

  ![image](public_sys-resources/note_3.0-zh-cn.webp)

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

**导入模块**

```ets
import { common } from '@kit.AbilityKit';
```

**ApplicationContext.on('abilityLifecycle')**

on(type: 'abilityLifecycle', callback: AbilityLifecycleCallback): number

注册监听应用内UIAbility的生命周期。使用callback异步回调。仅支持主线程调用。

元服务API：从API version 11开始，该接口支持在元服务中使用。

系统能力：SystemCapability.Ability.AbilityRuntime.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 此类型表示应用内UIAbility的生命周期，固定为'abilityLifecycle'。 |
| callback | AbilityLifecycleCallback | 是 | UIAbility生命周期变化时触发的回调方法。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| number | 返回此次注册的callbackID，该ID用于在ApplicationContext.off('abilityLifecycle')方法中取消注册对应的callback。 |

错误码：

以下错误码详细介绍请参考[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |

示例：

```ets
import { UIAbility, AbilityLifecycleCallback } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let lifecycleId: number;

export default class EntryAbility extends UIAbility {
  onCreate() {
    console.info('MyAbility onCreate');
    let AbilityLifecycleCallback: AbilityLifecycleCallback = {
      onAbilityCreate(ability) {
        console.info(`AbilityLifecycleCallback onAbilityCreate ability: ${ability}`);
      },
      onWindowStageCreate(ability, windowStage) {
        console.info(`AbilityLifecycleCallback onWindowStageCreate ability: ${ability}`);
        console.info(`AbilityLifecycleCallback onWindowStageCreate windowStage: ${windowStage}`);
      },
      onWindowStageActive(ability, windowStage) {
        console.info(`AbilityLifecycleCallback onWindowStageActive ability: ${ability}`);
        console.info(`AbilityLifecycleCallback onWindowStageActive windowStage: ${windowStage}`);
      },
      onWindowStageInactive(ability, windowStage) {
        console.info(`AbilityLifecycleCallback onWindowStageInactive ability: ${ability}`);
        console.info(`AbilityLifecycleCallback onWindowStageInactive windowStage: ${windowStage}`);
      },
      onWindowStageDestroy(ability, windowStage) {
        console.info(`AbilityLifecycleCallback onWindowStageDestroy ability: ${ability}`);
        console.info(`AbilityLifecycleCallback onWindowStageDestroy windowStage: ${windowStage}`);
      },
      onAbilityDestroy(ability) {
        console.info(`AbilityLifecycleCallback onAbilityDestroy ability: ${ability}`);
      },
      onAbilityForeground(ability) {
        console.info(`AbilityLifecycleCallback onAbilityForeground ability: ${ability}`);
      },
      onAbilityBackground(ability) {
        console.info(`AbilityLifecycleCallback onAbilityBackground ability: ${ability}`);
      },
      onAbilityContinue(ability) {
        console.info(`AbilityLifecycleCallback onAbilityContinue ability: ${ability}`);
      }
    // 1.通过context属性获取applicationContext
    let applicationContext = this.context.getApplicationContext();
    try {
      // 2.通过applicationContext注册监听应用内生命周期
      lifecycleId = applicationContext.on('abilityLifecycle', AbilityLifecycleCallback);
    } catch (paramError) {
      console.error(`error code: ${(paramError as BusinessError).code}, error msg: ${(paramError as BusinessError).message}`);
    }
    console.info(`registerAbilityLifecycleCallback lifecycleId: ${lifecycleId}`);
  }
```

**ApplicationContext.off('abilityLifecycle')**

off(type: 'abilityLifecycle', callbackId: number, callback: AsyncCallback<void>): void

取消监听应用内UIAbility的生命周期。使用callback异步回调。仅支持主线程调用。

元服务API：从API version 11开始，该接口支持在元服务中使用。

系统能力：SystemCapability.Ability.AbilityRuntime.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 此类型表示应用内UIAbility的生命周期，固定为'abilityLifecycle'。 |
| callbackId | number | 是 | 通过ApplicationContext.on('abilityLifecycle')接口注册监听应用内UIAbility的生命周期时返回的ID。 |
| callback | AsyncCallback<void> | 是 | 回调方法。当取消监听应用内生命周期成功，err为undefined，否则为错误对象。 |

错误码：

以下错误码详细介绍请参考[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |

示例：

```ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let lifecycleId: number;

export default class EntryAbility extends UIAbility {
  onDestroy() {
    let applicationContext = this.context.getApplicationContext();
    console.info(`stage applicationContext: ${applicationContext}`);
    try {
      applicationContext.off('abilityLifecycle', lifecycleId, (error, data) => {
        if (error) {
          console.error(`unregisterAbilityLifecycleCallback fail, err: ${JSON.stringify(error)}`);
        } else {
          console.info(`unregisterAbilityLifecycleCallback success, data: ${JSON.stringify(data)}`);
        }
      });
    } catch (paramError) {
      console.error(`error code: ${(paramError as BusinessError).code}, error code: ${(paramError as BusinessError).message}`);
    }
```

**ApplicationContext.off('abilityLifecycle')**

off(type: 'abilityLifecycle', callbackId: number): Promise<void>

取消监听应用内UIAbility的生命周期。使用Promise异步回调。仅支持主线程调用。

元服务API：从API version 11开始，该接口支持在元服务中使用。

系统能力：SystemCapability.Ability.AbilityRuntime.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 此类型表示应用内UIAbility的生命周期，固定为'abilityLifecycle'。 |
| callbackId | number | 是 | 通过ApplicationContext.on('abilityLifecycle')接口注册监听应用内UIAbility的生命周期时返回的ID。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

错误码：

以下错误码详细介绍请参考[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |

示例：

```ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let lifecycleId: number;

export default class MyAbility extends UIAbility {
  onDestroy() {
    let applicationContext = this.context.getApplicationContext();
    console.info(`stage applicationContext: ${applicationContext}`);
    try {
      applicationContext.off('abilityLifecycle', lifecycleId);
    } catch (paramError) {
      console.error(`error code: ${(paramError as BusinessError).code}, error msg: ${(paramError as BusinessError).message}`);
    }
```

**ApplicationContext.on('environment')**

on(type: 'environment', callback: EnvironmentCallback): number

注册对系统环境变化的监听。使用callback异步回调。仅支持主线程调用。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

- 使用[onConfigurationUpdate](@ohos.app.ability.Ability (Ability基类).md#ZH-CN_TOPIC_0000002553360447__abilityonconfigurationupdate)也可以实现对系统环境变量的监听。相较于Ability的[onConfigurationUpdate](@ohos.app.ability.Ability (Ability基类).md#ZH-CN_TOPIC_0000002553360447__abilityonconfigurationupdate)接口，当前接口的使用场景更加灵活，不仅可以在应用组件中使用，还可以在页面中使用，但是支持订阅的环境变量与Ability的[onConfigurationUpdate](@ohos.app.ability.Ability (Ability基类).md#ZH-CN_TOPIC_0000002553360447__abilityonconfigurationupdate)接口存在差异，如不支持订阅direction、screenDensity、displayId，详见[Configuration](@ohos.app.ability.Configuration (环境变量).md#ZH-CN_TOPIC_0000002522240556__configuration)中各个环境变量的说明。

- 当前接口在实际触发时存在一定限制。例如如果开发者通过[setLanguage](ApplicationContext (应用上下文).md#ZH-CN_TOPIC_0000002553360493__applicationcontextsetlanguage11)接口设置应用的语言，即便系统语言发生变化，系统也不再触发当前接口的[callback](@ohos.app.ability.EnvironmentCallback (系统环境变化监听器).md)回调。详见[使用场景](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/subscribe-system-environment-variable-changes#使用场景)。

元服务API：从API version 11开始，该接口支持在元服务中使用。

系统能力：SystemCapability.Ability.AbilityRuntime.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 此类型表示系统环境变化，如系统深浅色发生变化，固定为'environment'。 |
| callback | EnvironmentCallback | 是 | 系统环境变化时触发的回调方法。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| number | 返回此次注册的callbackID，该ID用于在ApplicationContext.off('environment')方法中取消注册对应的callback。 |

错误码：

以下错误码详细介绍请参考[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |

示例：

```ets
import { UIAbility, EnvironmentCallback } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let callbackId: number;

export default class EntryAbility extends UIAbility {
  onCreate() {
    console.info('MyAbility onCreate')
    let environmentCallback: EnvironmentCallback = {
      onConfigurationUpdated(config) {
        console.info(`onConfigurationUpdated config: ${JSON.stringify(config)}`);
      },
      onMemoryLevel(level) {
        console.info(`onMemoryLevel level: ${level}`);
      }
    };
    // 1.获取applicationContext
    let applicationContext = this.context.getApplicationContext();
    try {
      // 2.通过applicationContext注册监听系统环境变化
      callbackId = applicationContext.on('environment', environmentCallback);
    } catch (paramError) {
      console.error(`error code: ${(paramError as BusinessError).code}, error msg: ${(paramError as BusinessError).message}`);
    }
    console.info(`registerEnvironmentCallback callbackId: ${callbackId}`);
  }
```

**ApplicationContext.off('environment')**

off(type: 'environment', callbackId: number, callback: AsyncCallback<void>): void

取消对系统环境变化的监听。使用callback异步回调。仅支持主线程调用。

元服务API：从API version 11开始，该接口支持在元服务中使用。

系统能力：SystemCapability.Ability.AbilityRuntime.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 此类型表示系统环境变化，如系统深浅色发生变化，固定为'environment'。 |
| callbackId | number | 是 | 通过ApplicationContext.on('environment')接口注册监听系统环境变化时返回的ID。 |
| callback | AsyncCallback<void> | 是 | 回调方法。当取消对系统环境变化的监听成功，err为undefined，否则为错误对象。 |

错误码：

以下错误码详细介绍请参考[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |

示例：

```ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let callbackId: number;

export default class EntryAbility extends UIAbility {
  onDestroy() {
    let applicationContext = this.context.getApplicationContext();
    try {
      applicationContext.off('environment', callbackId, (error, data) => {
        if (error) {
          console.error(`unregisterEnvironmentCallback fail, err: ${JSON.stringify(error)}`);
        } else {
          console.info(`unregisterEnvironmentCallback success, data: ${JSON.stringify(data)}`);
        }
      });
    } catch (paramError) {
      console.error(`error code: ${(paramError as BusinessError).code}, error msg: ${(paramError as BusinessError).message}`);
    }
```

**ApplicationContext.off('environment')**

off(type: 'environment', callbackId: number): Promise<void>

取消对系统环境变化的监听。使用Promise异步回调。仅支持主线程调用。

元服务API：从API version 11开始，该接口支持在元服务中使用。

系统能力：SystemCapability.Ability.AbilityRuntime.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 此类型表示系统环境变化，如系统深浅色发生变化，固定为'environment'。 |
| callbackId | number | 是 | 通过ApplicationContext.on('environment')接口注册监听系统环境变化时返回的ID。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

错误码：

以下错误码详细介绍请参考[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |

示例：

```ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let callbackId: number;

export default class MyAbility extends UIAbility {
  onDestroy() {
    let applicationContext = this.context.getApplicationContext();
    try {
      applicationContext.off('environment', callbackId);
    } catch (paramError) {
      console.error(`error: ${(paramError as BusinessError).code}, ${(paramError as BusinessError).message}`);
    }
```

**ApplicationContext.on('applicationStateChange')10+**

on(type: 'applicationStateChange', callback: ApplicationStateChangeCallback): void

注册对当前应用进程状态变化的监听。使用callback异步回调。仅支持主线程调用。

元服务API：从API version 11开始，该接口支持在元服务中使用。

系统能力：SystemCapability.Ability.AbilityRuntime.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 此类型表示当前应用进程状态变化，固定为'applicationStateChange'。 |
| callback | ApplicationStateChangeCallback | 是 | 当前应用进程状态切换时触发的回调方法。 |

错误码：

以下错误码详细介绍请参考[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |

示例：

```ets
import { UIAbility, ApplicationStateChangeCallback } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class MyAbility extends UIAbility {
  onCreate() {
    console.info('MyAbility onCreate');
    let applicationStateChangeCallback: ApplicationStateChangeCallback = {
      onApplicationForeground() {
        console.info('applicationStateChangeCallback onApplicationForeground');
      },
      onApplicationBackground() {
        console.info('applicationStateChangeCallback onApplicationBackground');
      }

    // 1.获取applicationContext
    let applicationContext = this.context.getApplicationContext();
    try {
      // 2.通过applicationContext注册当前应用进程状态监听
      applicationContext.on('applicationStateChange', applicationStateChangeCallback);
    } catch (paramError) {
      console.error(`error code: ${(paramError as BusinessError).code}, error msg: ${(paramError as BusinessError).message}`);
    }
    console.info('Register applicationStateChangeCallback');
  }
```

**ApplicationContext.off('applicationStateChange')10+**

off(type: 'applicationStateChange', callback?: ApplicationStateChangeCallback): void

取消对当前应用进程状态变化的监听。使用callback异步回调。仅支持主线程调用。

元服务API：从API version 11开始，该接口支持在元服务中使用。

系统能力：SystemCapability.Ability.AbilityRuntime.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 此类型表示当前应用进程状态变化，固定为'applicationStateChange'。 |
| callback | ApplicationStateChangeCallback | 否 | 回调函数。取值可以为使用ApplicationContext.on('applicationStateChange')方法定义的callback回调，也可以为空。 - 如果传入已定义的回调，则取消该监听。 - 如果未传入参数，则取消所有已注册的该类型事件的监听。 |

错误码：

以下错误码详细介绍请参考[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |

示例：

假定已使用[ApplicationContext.on('applicationStateChange')](#ZH-CN_TOPIC_0000002553360493__applicationcontextonapplicationstatechange10)方法注册名为applicationStateChangeCallback回调，下面示例展示如何取消对应的事件监听。

```ets
import { UIAbility, ApplicationStateChangeCallback } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let applicationStateChangeCallback: ApplicationStateChangeCallback = {
  onApplicationForeground() {
    console.info('applicationStateChangeCallback onApplicationForeground');
  },
  onApplicationBackground() {
    console.info('applicationStateChangeCallback onApplicationBackground');
  }
};

export default class MyAbility extends UIAbility {
  onDestroy() {
    let applicationContext = this.context.getApplicationContext();
    try {
      // 本例中的callback字段取值为ApplicationStateChangeCallback，需要替换为实际值。
      // 如果callback字段不传入参数，则取消所有已注册的该类型事件的监听。
      applicationContext.off('applicationStateChange', applicationStateChangeCallback);
    } catch (paramError) {
      console.error(`error: ${(paramError as BusinessError).code}, ${(paramError as BusinessError).message}`);
    }
```

**ApplicationContext.getRunningProcessInformation**

getRunningProcessInformation(): Promise<Array<ProcessInformation>>

获取运行中的进程信息。使用Promise异步回调。

元服务API：从API version 11开始，该接口支持在元服务中使用。

系统能力：SystemCapability.Ability.AbilityRuntime.Core

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<Array<ProcessInformation>> | Promise对象，返回接口运行结果及有关运行进程的信息，可进行错误处理或其他自定义处理。 |

错误码：

以下错误码详细介绍请参考[通用错误码](通用错误码.md)和[元能力子系统错误码](元能力子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000011 | The context does not exist. |
| 16000050 | Internal error. |

示例：

```ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class MyAbility extends UIAbility {
  onForeground() {
    let applicationContext = this.context.getApplicationContext();
    applicationContext.getRunningProcessInformation().then((data) => {
      console.info(`The process running information is: ${JSON.stringify(data)}`);
    }).catch((error: BusinessError) => {
      console.error(`error code: ${error.code}, error msg: ${error.message}`);
    });
  }
```

**ApplicationContext.getRunningProcessInformation**

getRunningProcessInformation(callback: AsyncCallback<Array<ProcessInformation>>): void

获取运行中的进程信息。使用callback异步回调。

元服务API：从API version 11开始，该接口支持在元服务中使用。

系统能力：SystemCapability.Ability.AbilityRuntime.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<Array<ProcessInformation>> | 是 | 回调函数，返回有关运行进程的信息。 |

错误码：

以下错误码详细介绍请参考[通用错误码](通用错误码.md)和[元能力子系统错误码](元能力子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000011 | The context does not exist. |
| 16000050 | Internal error. |

示例：

```ets
import { UIAbility } from '@kit.AbilityKit';

export default class MyAbility extends UIAbility {
  onForeground() {
    let applicationContext = this.context.getApplicationContext();
    applicationContext.getRunningProcessInformation((err, data) => {
      if (err) {
        console.error(`getRunningProcessInformation failed, err: ${JSON.stringify(err)}`);
      } else {
        console.info(`The process running information is: ${JSON.stringify(data)}`);
      }
    })
  }
```

**ApplicationContext.killAllProcesses**

killAllProcesses(): Promise<void>

终止应用的所有进程，进程退出时不会正常执行完整的应用生命周期流程。使用Promise异步回调。仅支持主线程调用。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

该接口用于应用异常场景中强制退出应用。如需正常退出应用，可以使用[terminateSelf()](UIAbilityContext.md#ZH-CN_TOPIC_0000002553200541__terminateself-1)接口。

元服务API：从API version 11开始，该接口支持在元服务中使用。

系统能力：SystemCapability.Ability.AbilityRuntime.Core

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

错误码：

以下错误码详细介绍请参考[通用错误码](通用错误码.md)和[元能力子系统错误码](元能力子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000011 | The context does not exist. |

示例：

```ets
import { UIAbility } from '@kit.AbilityKit';

export default class MyAbility extends UIAbility {
  onBackground() {
    let applicationContext = this.context.getApplicationContext();
    applicationContext.killAllProcesses();
  }
```

**ApplicationContext.killAllProcesses14+**

killAllProcesses(clearPageStack: boolean): Promise<void>

终止应用的所有进程，进程退出时不会正常执行完整的应用生命周期流程。使用Promise异步回调。仅支持主线程调用。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

该接口用于应用异常场景中强制退出应用。如需正常退出应用，可以使用[terminateSelf()](UIAbilityContext.md#ZH-CN_TOPIC_0000002553200541__terminateself-1)接口。

元服务API：从API version 14开始，该接口支持在元服务中使用。

系统能力：SystemCapability.Ability.AbilityRuntime.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| clearPageStack | boolean | 是 | 表示是否清除页面堆栈。true表示清除，false表示不清除。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

错误码：

以下错误码详细介绍请参考[通用错误码](通用错误码.md)和[元能力子系统错误码](元能力子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter is not valid parameter. |
| 16000011 | The context does not exist. |

示例：

```ets
import { UIAbility } from '@kit.AbilityKit';

let isClearPageStack = false;

export default class MyAbility extends UIAbility {
  onBackground() {
    let applicationContext = this.context.getApplicationContext();
    applicationContext.killAllProcesses(isClearPageStack);
  }
```

**ApplicationContext.killAllProcesses**

killAllProcesses(callback: AsyncCallback<void>): void

终止应用的所有进程，进程退出时不会正常执行完整的应用生命周期流程。使用callback异步回调。仅支持主线程调用。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

该接口用于应用异常场景中强制退出应用。如需正常退出应用，可以使用[terminateSelf()](UIAbilityContext.md#ZH-CN_TOPIC_0000002553200541__terminateself-1)接口。

元服务API：从API version 11开始，该接口支持在元服务中使用。

系统能力：SystemCapability.Ability.AbilityRuntime.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当终止应用所在的进程成功，err为undefined，否则为错误对象。 |

错误码：

以下错误码详细介绍请参考[通用错误码](通用错误码.md)和[元能力子系统错误码](元能力子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000011 | The context does not exist. |

示例：

```ets
import { UIAbility } from '@kit.AbilityKit';

export default class MyAbility extends UIAbility {
  onBackground() {
    let applicationContext = this.context.getApplicationContext();
    applicationContext.killAllProcesses(error => {
      if (error) {
        console.error(`killAllProcesses fail, error: ${JSON.stringify(error)}`);
      }
    });
  }
```

**ApplicationContext.setColorMode11+**

setColorMode(colorMode: ConfigurationConstant.ColorMode): void

设置应用的深浅色模式。仅支持主线程调用。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

调用该接口前，需要确保窗口已完成创建、且UIAbility对应的页面已完成加载，即在[onWindowStageCreate()](@ohos.app.ability.UIAbility (带界面的应用组件).md#ZH-CN_TOPIC_0000002522240540__onwindowstagecreate)生命周期中通过[loadContent](Interface (WindowStage).md#ZH-CN_TOPIC_0000002553360677__loadcontent9)方法加载页面之后调用。

元服务API：从API version 11开始，该接口支持在元服务中使用。

系统能力：SystemCapability.Ability.AbilityRuntime.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| colorMode | ConfigurationConstant.ColorMode | 是 | 深浅色模式，包括：深色模式、浅色模式、未设置颜色模式（默认）。 |

错误码：

以下错误码详细介绍请参考[通用错误码](通用错误码.md)和[元能力子系统错误码](元能力子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000011 | The context does not exist. |

示例：

```ets
import { UIAbility, ConfigurationConstant } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';

export default class MyAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    console.info("Ability onWindowStageCreate");
    windowStage.loadContent('pages/Index', (err, data) => {
      if (err.code) {
        console.error(`Failed to load the content. Code: ${err.code}, message: ${err.message}`);
        return;
      }
      console.info(`Succeeded in loading the content. Data: ${JSON.stringify(data)}`);
      let applicationContext = this.context.getApplicationContext();
      applicationContext.setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_DARK);
    });
  }
```

**ApplicationContext.setLanguage11+**

setLanguage(language: string): void

设置应用的语言。仅支持主线程调用。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

调用该接口前，需要确保窗口已完成创建、且UIAbility对应的页面已完成加载，即在[onWindowStageCreate()](@ohos.app.ability.UIAbility (带界面的应用组件).md#ZH-CN_TOPIC_0000002522240540__onwindowstagecreate)生命周期中通过[loadContent](Interface (WindowStage).md#ZH-CN_TOPIC_0000002553360677__loadcontent9)方法加载页面之后调用。

元服务API：从API version 11开始，该接口支持在元服务中使用。

系统能力：SystemCapability.Ability.AbilityRuntime.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| language | string | 是 | 设置语言，当前支持的语言列表可以通过getSystemLanguages()获取。 |

错误码：

以下错误码详细介绍请参考[元能力子系统错误码](元能力子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 16000011 | The context does not exist. |

示例：

```ets
import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';

export default class MyAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    console.info("Ability onWindowStageCreate");
    windowStage.loadContent('pages/Index', (err, data) => {
      if (err.code) {
        console.error(`Failed to load the content. Code: ${err.code}, message: ${err.message}`);
        return;
      }
      console.info(`Succeeded in loading the content. Data: ${JSON.stringify(data)}`);
    });
    let applicationContext = this.context.getApplicationContext();
    applicationContext.setLanguage('zh-cn');
  }
```

**ApplicationContext.clearUpApplicationData11+**

clearUpApplicationData(): Promise<void>

清理当前应用的应用文件路径下的所有数据，同时撤销应用向用户申请的权限。使用Promise异步回调。仅支持主线程调用。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

应用文件路径详见[应用文件目录信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-sandbox-directory#应用文件目录与应用文件路径)。图中仅标识了el1~el2目录下的应用文件路径，其他文件加密类型目录下的应用文件路径可以参考el1。

该接口会停止应用进程，应用进程停止后，后续的所有回调都不会再触发。

系统能力：SystemCapability.Ability.AbilityRuntime.Core

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

错误码：

以下错误码详细介绍请参考[元能力子系统错误码](元能力子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 16000011 | The context does not exist. |
| 16000050 | Internal error. |

示例：

```ets
import { UIAbility } from '@kit.AbilityKit';

export default class MyAbility extends UIAbility {
  onBackground() {
    let applicationContext = this.context.getApplicationContext();
    applicationContext.clearUpApplicationData();
  }
```

**ApplicationContext.clearUpApplicationData11+**

clearUpApplicationData(callback: AsyncCallback<void>): void

清理当前应用的应用文件路径下的所有数据，同时撤销应用向用户申请的权限。使用callback异步回调。仅支持主线程调用。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

应用文件路径详见[应用文件目录信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-sandbox-directory#应用文件目录与应用文件路径)。图中仅标识了el1~el2目录下的应用文件路径，其他文件加密类型目录下的应用文件路径可以参考el1。

该接口会停止应用进程，应用进程停止后，后续的所有回调都不会再触发。

系统能力：SystemCapability.Ability.AbilityRuntime.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调方法。清理应用本身的数据成功时，error为undefined，否则返回错误对象。 |

错误码：

以下错误码详细介绍请参考[通用错误码](通用错误码.md)和[元能力子系统错误码](元能力子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000011 | The context does not exist. |
| 16000050 | Internal error. |

示例：

```ets
import { UIAbility } from '@kit.AbilityKit';

export default class MyAbility extends UIAbility {
  onBackground() {
    let applicationContext = this.context.getApplicationContext();
    applicationContext.clearUpApplicationData(error => {
      if (error) {
        console.error(`clearUpApplicationData fail, error: ${JSON.stringify(error)}`);
      }
    });
  }
```

**ApplicationContext.restartApp12+**

restartApp(want: Want): void

应用重启并拉起自身指定UIAbility。仅支持主线程调用，且待重启的应用需要处于获焦状态。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

通过该接口重启应用时，不会触发应用中Ability的onDestroy生命周期回调。

在元服务调用本接口成功后的3秒内，再次调用本接口、[restartSelfAtomicService()](@ohos.app.ability.abilityManager (Ability信息管理).md#ZH-CN_TOPIC_0000002553200519__abilitymanagerrestartselfatomicservice20)或[UIAbilityContext.restartApp()](UIAbilityContext.md#ZH-CN_TOPIC_0000002553200541__restartapp22)接口中的任一接口，系统将返回错误码16000064。

在应用调用本接口成功后的3秒内，若再次调用本接口或[UIAbilityContext.restartApp()](UIAbilityContext.md#ZH-CN_TOPIC_0000002553200541__restartapp22)接口中的任一接口，系统将返回错误码16000064。

元服务API：从API version 12开始，该接口支持在元服务中使用。

系统能力：SystemCapability.Ability.AbilityRuntime.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | Want | 是 | Want类型参数，传入需要启动的UIAbility信息，校验abilityName，不校验bundleName。 |

错误码：

以下错误码详细介绍请参考[通用错误码](通用错误码.md)和[元能力子系统错误码](元能力子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000050 | Internal error. |
| 16000053 | The ability is not on the top of the UI. |
| 16000063 | The target to restart does not belong to the current application or is not a UIAbility. |
| 16000064 | Restart too frequently. Try again at least 3s later. |

示例：

```ets
import { hilog } from '@kit.PerformanceAnalysisKit';
import { common, Want } from '@kit.AbilityKit';

@Entry
@Component
struct Index {
  @State message: string = 'restartApp';
  private context = this.getUIContext().getHostContext()?.getApplicationContext() as common.ApplicationContext;

  build() {
    RelativeContainer() {
      Text(this.message)
        .id('HelloWorld')
        .fontSize($r('app.float.page_text_font_size'))
        .fontWeight(FontWeight.Bold)
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        })
        .onClick(() => {
          let want: Want = {
            bundleName: 'com.example.myapplication',
            abilityName: 'EntryAbility'
          };
          if (this.context) {
            try {
              this.context.restartApp(want);
            } catch (err) {
              hilog.error(0x0000, 'testTag', `restart failed: ${err.code}, ${err.message}`);
            }
          } else {
            hilog.error(0x0000, 'testTag', "%{public}s", 'AppContext is null');
          }
        })
    }
    .height('100%')
    .width('100%')
  }
```

**ApplicationContext.getCurrentAppCloneIndex12+**

getCurrentAppCloneIndex(): number

获取当前应用的分身索引。

元服务API：从API version 12开始，该接口支持在元服务中使用。

系统能力：SystemCapability.Ability.AbilityRuntime.Core

返回值：

| 类型 | 说明 |
| --- | --- |
| number | 当前应用的分身索引。 |

错误码：

| 错误码ID | 错误信息 |
| --- | --- |
| 16000011 | The context does not exist. |
| 16000071 | The MultiAppMode is not App_CLONE. |

以上错误码详细介绍请参考[元能力子系统错误码](元能力子系统错误码.md)。

示例：

```ets
import { UIAbility } from '@kit.AbilityKit';

export default class MyAbility extends UIAbility {
  onBackground() {
    let applicationContext = this.context.getApplicationContext();
    try {
      let appCloneIndex = applicationContext.getCurrentAppCloneIndex();
    } catch (error) {
      console.error(`getCurrentAppCloneIndex fail, error: ${JSON.stringify(error)}`);
    }
```

**ApplicationContext.setFont12+**

setFont(font: string): void

设置应用的字体类型。仅支持主线程调用。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

调用该接口前，需要确保窗口已完成创建、且UIAbility对应的页面已完成加载，即在[onWindowStageCreate()](@ohos.app.ability.UIAbility (带界面的应用组件).md#ZH-CN_TOPIC_0000002522240540__onwindowstagecreate)生命周期中通过[loadContent](Interface (WindowStage).md#ZH-CN_TOPIC_0000002553360677__loadcontent9)方法加载页面之后调用。

系统能力：SystemCapability.Ability.AbilityRuntime.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| font | string | 是 | 设置字体类型，字体可以通过UIContext.registerFont方法进行注册使用。 |

错误码：

以下错误码详细介绍请参考[元能力子系统错误码](元能力子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 16000011 | The context does not exist. |
| 16000050 | Internal error. |

示例：

```ets
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct Index {
  @State message: string = 'Hello World';
  context = this.getUIContext().getHostContext() as common.UIAbilityContext;

  aboutToAppear() {
    this.getUIContext().getFont().registerFont({
      familyName: 'fontName',
      familySrc: $rawfile('font/medium.ttf')  // 'font/medium.ttf'仅作为示例，实际使用时请替换为真实的字体资源文件。
    });

    this.context.getApplicationContext().setFont('fontName');
  }

  build() {
    Row() {
      Column() {
        Text(this.message)
          .fontSize(50)
          .fontWeight(50)
      }
      .width('100%')
    }
    .height('100%')
  }
```

**ApplicationContext.setSupportedProcessCache12+**

setSupportedProcessCache(isSupported : boolean): void

设置当前应用进程是否支持进程资源的缓存，便于应用再次启动时复用缓存的进程资源。仅支持主线程调用。

该接口仅对单个进程实例生效，不同进程实例互不影响。应用进程实例销毁后，已设置的状态不保留，需要重新设置。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

- 该接口仅表示应用自身是否为缓存后快速启动做好了准备，还需综合其他条件来判断最终是否为应用启用快速启动。

- 为了确保该接口在进程退出前生效，调用时机应尽量提前。建议在[AbilityStage](@ohos.app.ability.AbilityStage (AbilityStage组件管理器).md)的onCreate()中调用该接口。

- 在同一进程多次调用该接口时，会以最后一次调用的结果为准。当存在多个AbilityStage时，为了确保结果符合预期，需要在各个AbilityStage中分别调用该接口并配置相同的取值。

模型约束：此接口仅可在Stage模型下使用。

系统能力：SystemCapability.Ability.AbilityRuntime.Core

设备行为差异：该接口仅在Phone和2in1设备中可正常调用，在其他设备中返回801错误码。

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isSupported | boolean | 是 | 表示应用是否支持进程资源的缓存。true表示支持，false表示不支持。 |

错误码：

以下错误码详细介绍请参考[通用错误码](通用错误码.md)、[元能力子系统错误码](元能力子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 801 | Capability not supported. |
| 16000011 | The context does not exist. |
| 16000050 | Internal error. |

示例：

```ets
import { AbilityStage, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class MyAbilityStage extends AbilityStage {
  onCreate() {
    let applicationContext = this.context.getApplicationContext();
    try {
      applicationContext.setSupportedProcessCache(true);
    } catch (error) {
      let code = (error as BusinessError).code;
      let message = (error as BusinessError).message;
      console.error(`setSupportedProcessCache fail, code: ${code}, msg: ${message}`);
    }
```

**ApplicationContext.setFontSizeScale13+**

setFontSizeScale(fontSizeScale: number): void

设置应用字体大小缩放比例。仅支持主线程调用。

元服务API：从API version 13开始，该接口支持在元服务中使用。

系统能力：SystemCapability.Ability.AbilityRuntime.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fontSizeScale | number | 是 | 表示字体缩放比例，取值为非负数。当应用字体跟随系统且该字段取值超过fontSizeMaxScale取值时，实际生效值为fontSizeMaxScale取值。 |

示例：

```ets
import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';

export default class MyAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    windowStage.loadContent('pages/Index', (err, data) => {
      if (err.code) {
        return;
      }
      let applicationContext = this.context.getApplicationContext();
      applicationContext.setFontSizeScale(2);
    });
  }
```

**ApplicationContext.getCurrentInstanceKey14+**

getCurrentInstanceKey(): string

获取当前应用多实例的唯一实例标识。仅支持主线程调用。

系统能力：SystemCapability.Ability.AbilityRuntime.Core

设备行为差异：该接口仅在2in1设备中可正常调用，在其他设备中返回16000078错误码。

返回值：

| 类型 | 说明 |
| --- | --- |
| string | 返回当前应用多实例的唯一实例标识。 |

错误码：

以下错误码详细介绍请参考[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 16000011 | The context does not exist. |
| 16000078 | The multi-instance is not supported. |

示例：

```ets
import { AbilityStage } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class MyAbilityStage extends AbilityStage {
  onCreate() {
    let applicationContext = this.context.getApplicationContext();
    let currentInstanceKey = '';
    try {
      currentInstanceKey = applicationContext.getCurrentInstanceKey();
    } catch (error) {
      let code = (error as BusinessError).code;
      let message = (error as BusinessError).message;
      console.error(`getCurrentInstanceKey fail, code: ${code}, msg: ${message}`);
    }
    console.info(`currentInstanceKey: ${currentInstanceKey}`);
  }
```

**ApplicationContext.getAllRunningInstanceKeys14+**

getAllRunningInstanceKeys(): Promise<Array<string>>;

获取应用的所有多实例的唯一实例标识。使用Promise异步回调。仅支持主线程调用。

系统能力：SystemCapability.Ability.AbilityRuntime.Core

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<Array<string>> | Promise对象，返回应用的所有多实例的唯一实例标识。 |

错误码：

以下错误码详细介绍请参考[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 16000011 | The context does not exist. |
| 16000050 | Internal error. |
| 16000078 | The multi-instance is not supported. |

示例：

```ets
import { AbilityStage } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class MyAbilityStage extends AbilityStage {
  onCreate() {
    let applicationContext = this.context.getApplicationContext();
    try {
      applicationContext.getAllRunningInstanceKeys();
    } catch (error) {
      let code = (error as BusinessError).code;
      let message = (error as BusinessError).message;
      console.error(`getAllRunningInstanceKeys fail, code: ${code}, msg: ${message}`);
    }
```

**ApplicationContext.getAllWindowStages23+**

getAllWindowStages(): Promise<Array<window.WindowStage>>

获取应用当前进程内的所有WindowStage对象。使用Promise异步回调。仅支持主线程调用。

该接口主要用于包含多个UIAbility的应用进行多窗口管理，例如管理多个WindowStage的状态、同一应用的多个窗口间的状态或数据同步等。

元服务API：从API version 23开始，该接口支持在元服务中使用。

系统能力：SystemCapability.Ability.AbilityRuntime.Core

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<Array<window.WindowStage>> | Promise对象，返回应用当前进程内的所有WindowStage对象。 |

示例：

```ets
import { AbilityStage } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

export default class MyAbilityStage extends AbilityStage {
  onCreate() {
    let applicationContext = this.context.getApplicationContext();
    try {
      applicationContext.getAllWindowStages().then((data: window.WindowStage[]) => {
        let windowStage: window.WindowStage[] = data;
        console.info(`WindowStages size ${windowStage.length}`);
      }).catch((error: BusinessError) => {
        console.error(`getAllWindowStages error, code: ${error.code}, error msg: ${error.message}`);
      });
    } catch (error) {
      let code = (error as BusinessError).code;
      let message = (error as BusinessError).message;
      console.error(`getAllWindowStages fail, code: ${code}, msg: ${message}`);
    }
```