# @ohos.app.ability.appManager (应用管理)

appManager模块提供应用管理的能力，包括查询当前系统是否处于稳定性测试场景、查询当前设备是否为RAM（Random Access Memory，随机存取存储器）受限设备、获取当前应用程序可以使用的最大内存值、获取有关运行进程的信息等。

本模块首批接口从API version 9 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { appManager } from '@kit.AbilityKit';
```

#### ProcessState10+

表示进程状态的枚举。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| STATE_CREATE | 0 | 进程创建完成。 |
| STATE_FOREGROUND | 1 | 进程处于前台。 |
| STATE_ACTIVE | 2 | 进程中至少有一个窗口获焦。 |
| STATE_BACKGROUND | 3 | 进程处于后台。 |
| STATE_DESTROY | 4 | 进程销毁完成。 |

#### appManager.isRunningInStabilityTest

isRunningInStabilityTest(callback: AsyncCallback<boolean>): void

查询当前系统是否处于稳定性测试场景。使用callback异步回调。

稳定性测试场景指为验证应用在复杂、极端或长期运行条件下的可靠性而设计的特定测试环境。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<boolean> | 是 | 回调函数。当接口调用成功，err为undefined，data为当前系统是否处于稳定性测试场景的结果；否则为错误对象。可进行错误处理或其他自定义处理。 返回true表示系统处于稳定性测试场景；返回false表示系统不处于稳定性测试场景。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码]([通用错误码](../../errors/通用错误码.md).md)和[元能力子系统错误码]([元能力子系统错误码](../../errors/元能力子系统错误码.md).md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 16000050 | Internal error. |

**示例：**

```ets
import { appManager } from '@kit.AbilityKit';

appManager.isRunningInStabilityTest((err, flag) => {
  if (err) {
    console.error(`isRunningInStabilityTest fail, err: ${JSON.stringify(err)}`);
  } else {
    console.info(`The result of isRunningInStabilityTest is: ${JSON.stringify(flag)}`);
  }
});
```

#### appManager.isRunningInStabilityTest

isRunningInStabilityTest(): Promise<boolean>

查询当前系统是否处于稳定性测试场景。使用Promise异步回调。

稳定性测试场景指为验证应用在复杂、极端或长期运行条件下的可靠性而设计的特定测试环境。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | 以Promise方式返回接口运行结果及当前是否处于稳定性测试场景，可进行错误处理或其他自定义处理。 返回true表示系统处于稳定性测试场景；返回false表示系统不处于稳定性测试场景。 |

**错误码**：

以下错误码详细介绍请参考[元能力子系统错误码](元能力子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 16000050 | Internal error. |

**示例：**

```ets
import { appManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

appManager.isRunningInStabilityTest().then((flag) => {
  console.info(`The result of isRunningInStabilityTest is: ${JSON.stringify(flag)}`);
}).catch((error: BusinessError) => {
  console.error(`error: ${JSON.stringify(error)}`);
});
```

#### appManager.isRamConstrainedDevice

isRamConstrainedDevice(): Promise<boolean>

查询当前设备是否为RAM受限设备（内存资源严重受限的设备）。使用Promise异步回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | 以Promise方式返回接口运行结果及当前设备是否为RAM受限设备，可进行错误处理或其他自定义处理。 返回true表示当前设备为RAM受限设备；返回false表示当前设备为非RAM受限设备。 |

**错误码**：

以下错误码详细介绍请参考[元能力子系统错误码](元能力子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 16000050 | Internal error. |

**示例：**

```ets
import { appManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

appManager.isRamConstrainedDevice().then((data) => {
  console.info(`The result of isRamConstrainedDevice is: ${JSON.stringify(data)}`);
}).catch((error: BusinessError) => {
  console.error(`error: ${JSON.stringify(error)}`);
});
```

#### appManager.isRamConstrainedDevice

isRamConstrainedDevice(callback: AsyncCallback<boolean>): void

查询当前设备是否为RAM受限设备（内存资源严重受限的设备）。使用callback异步回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<boolean> | 是 | 回调函数。当接口调用成功，err为undefined，data为当前设备是否为RAM受限设备的结果；否则为错误对象。可进行错误处理或其他自定义处理。 返回true表示当前设备为RAM受限设备；返回false表示当前设备为非RAM受限设备。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](通用错误码.md)和[元能力子系统错误码](元能力子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 16000050 | Internal error. |

**示例：**

```ets
import { appManager } from '@kit.AbilityKit';

appManager.isRamConstrainedDevice((err, data) => {
  if (err) {
    console.error(`isRamConstrainedDevice fail, err: ${JSON.stringify(err)}`);
  } else {
    console.info(`The result of isRamConstrainedDevice is: ${JSON.stringify(data)}`);
  }
});
```

#### appManager.getAppMemorySize

getAppMemorySize(): Promise<number>

获取当前应用程序可以使用的最大内存（RAM）值。使用Promise异步回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | 当前应用程序可以使用的最大内存（RAM）值，可根据此值进行错误处理或其他自定义处理，单位是M。使用Promise异步回调。 |

**错误码**：

以下错误码详细介绍请参考[元能力子系统错误码](元能力子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 16000050 | Internal error. |

**示例：**

```ets
import { appManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

appManager.getAppMemorySize().then((data) => {
  console.info(`The size of app memory is: ${JSON.stringify(data)}`);
}).catch((error: BusinessError) => {
  console.error(`error: ${JSON.stringify(error)}`);
});
```

#### appManager.getAppMemorySize

getAppMemorySize(callback: AsyncCallback<number>): void

获取当前应用程序可以使用的最大内存（RAM）值。使用callback异步回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<number> | 是 | 回调函数。当接口调用成功，err为undefined，data为当前应用程序可以使用的最大内存（RAM）值，单位是M；否则为错误对象。可根据此值进行错误处理或其他自定义处理。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](通用错误码.md)和[元能力子系统错误码](元能力子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 16000050 | Internal error. |

**示例：**

```ets
import { appManager } from '@kit.AbilityKit';

appManager.getAppMemorySize((err, data) => {
  if (err) {
    console.error(`getAppMemorySize fail, err: ${JSON.stringify(err)}`);
  } else {
    console.info(`The size of app memory is: ${JSON.stringify(data)}`);
  }
});
```

#### appManager.getRunning[ProcessInformation](../../topics/misc/ProcessInformation.md)

getRunning[ProcessInformation](../../topics/misc/ProcessInformation.md)(): Promise<Array<ProcessInformation>>

获取当前应用运行进程的相关信息。使用Promise异步回调。

- 对于API version 11之前的版本，该接口需要申请权限ohos.permission.GET_RUNNING_INFO（该权限仅系统应用可申请）。
- 从API version 11开始，该接口仅用于获取调用方自身的进程信息，不再需要申请权限。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[ProcessInformation](../../topics/misc/ProcessInformation.md)>> | Promise对象，返回接口运行结果及有关运行进程的信息，可进行错误处理或其他自定义处理。 |

**错误码**：

以下错误码详细介绍请参考[元能力子系统错误码](元能力子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 16000050 | Internal error. |

**示例：**

```ets
import { appManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

appManager.getRunningProcessInformation().then((data) => {
  console.info(`The running process information is: ${JSON.stringify(data)}`);
}).catch((error: BusinessError) => {
  console.error(`error: ${JSON.stringify(error)}`);
});
```

#### appManager.getRunning[ProcessInformation](../../topics/misc/ProcessInformation.md)

getRunning[ProcessInformation](../../topics/misc/ProcessInformation.md)(callback: AsyncCallback<Array<ProcessInformation>>): void

获取当前应用运行进程的相关信息。使用callback异步回调。

- 对于API version 11之前的版本，该接口需要申请权限ohos.permission.GET_RUNNING_INFO（该权限仅系统应用可申请）。
- 从API version 11开始，该接口仅用于获取调用方自身的进程信息，不再需要申请权限。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<Array<[ProcessInformation](../../topics/misc/ProcessInformation.md)>> | 是 | 回调函数。当接口调用成功，err为undefined，data为当前应用运行进程的信息；否则为错误对象。可进行错误处理或其他自定义处理。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](通用错误码.md)和[元能力子系统错误码](元能力子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 16000050 | Internal error. |

**示例：**

```ets
import { appManager } from '@kit.AbilityKit';

appManager.getRunningProcessInformation((err, data) => {
  if (err) {
    console.error(`getRunningProcessInformation fail, err: ${JSON.stringify(err)}`);
  } else {
    console.info(`The running process information is: ${JSON.stringify(data)}`);
  }
});
```

#### appManager.on('applicationState')14+

on(type: 'applicationState', observer: [ApplicationStateObserver](../../topics/misc/ApplicationStateObserver.md)): number

注册所有应用程序的状态监听器。

**需要权限**：ohos.permission.RUNNING_STATE_OBSERVER

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 调用接口类型，固定填'applicationState'字符串。 |
| observer | [ApplicationStateObserver](../../topics/misc/ApplicationStateObserver.md) | 是 | 应用状态监听器，用于监听应用的生命周期变化。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 已注册监听器ID，调用方可以通过off('applicationState')传入该监听器ID来注销监听器。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](通用错误码.md)和[元能力子系统错误码](元能力子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 16000050 | Internal error. |

**示例：**

```ets
import { appManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let applicationStateObserver: appManager.ApplicationStateObserver = {
  onForegroundApplicationChanged(appStateData) {
    console.info(`[appManager] onForegroundApplicationChanged: ${JSON.stringify(appStateData)}`);
  },
  onAbilityStateChanged(abilityStateData) {
    console.info(`[appManager] onAbilityStateChanged: ${JSON.stringify(abilityStateData)}`);
  },
  onProcessCreated(processData) {
    console.info(`[appManager] onProcessCreated: ${JSON.stringify(processData)}`);
  },
  onProcessDied(processData) {
    console.info(`[appManager] onProcessDied: ${JSON.stringify(processData)}`);
  },
  onProcessStateChanged(processData) {
    console.info(`[appManager] onProcessStateChanged: ${JSON.stringify(processData)}`);
  },
  onAppStarted(appStateData) {
    console.info(`[appManager] onAppStarted: ${JSON.stringify(appStateData)}`);
  },
  onAppStopped(appStateData) {
    console.info(`[appManager] onAppStopped: ${JSON.stringify(appStateData)}`);
  }
};

try {
  const observerId = appManager.on('applicationState', applicationStateObserver);
  console.info(`[appManager] observerCode: ${observerId}`);
} catch (paramError) {
  let code = (paramError as BusinessError).code;
  let message = (paramError as BusinessError).message;
  console.error(`[appManager] error: ${code}, ${message}`);
}
```

#### appManager.on('applicationState')14+

on(type: 'applicationState', observer: [ApplicationStateObserver](../../topics/misc/ApplicationStateObserver.md), bundleNameList: Array<string>): number

注册指定应用程序的状态监听器。

**需要权限**：ohos.permission.RUNNING_STATE_OBSERVER

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 调用接口类型，固定填'applicationState'字符串。 |
| observer | [ApplicationStateObserver](../../topics/misc/ApplicationStateObserver.md) | 是 | 应用状态监听器，用于监听应用的生命周期变化。 |
| bundleNameList | Array<string> | 是 | 表示需要注册监听的bundleName数组。最大值128。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 已注册监听器ID，调用方可以通过off('applicationState')传入该监听器ID来注销监听器。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](通用错误码.md)和[元能力子系统错误码](元能力子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 16000050 | Internal error. |

**示例：**

```ets
import { appManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let applicationStateObserver: appManager.ApplicationStateObserver = {
  onForegroundApplicationChanged(appStateData) {
    console.info(`[appManager] onForegroundApplicationChanged: ${JSON.stringify(appStateData)}`);
  },
  onAbilityStateChanged(abilityStateData) {
    console.info(`[appManager] onAbilityStateChanged: ${JSON.stringify(abilityStateData)}`);
  },
  onProcessCreated(processData) {
    console.info(`[appManager] onProcessCreated: ${JSON.stringify(processData)}`);
  },
  onProcessDied(processData) {
    console.info(`[appManager] onProcessDied: ${JSON.stringify(processData)}`);
  },
  onProcessStateChanged(processData) {
    console.info(`[appManager] onProcessStateChanged: ${JSON.stringify(processData)}`);
  },
  onAppStarted(appStateData) {
    console.info(`[appManager] onAppStarted: ${JSON.stringify(appStateData)}`);
  },
  onAppStopped(appStateData) {
    console.info(`[appManager] onAppStopped: ${JSON.stringify(appStateData)}`);
  }
};

let bundleNameList = ['bundleName1', 'bundleName2'];

try {
  const observerId = appManager.on('applicationState', applicationStateObserver, bundleNameList);
  console.info(`[appManager] observerCode: ${observerId}`);
} catch (paramError) {
  let code = (paramError as BusinessError).code;
  let message = (paramError as BusinessError).message;
  console.error(`[appManager] error: ${code}, ${message}`);
}
```

#### appManager.off('applicationState')14+

off(type: 'applicationState', observerId: number): Promise<void>

注销应用状态监听器。使用Promise异步回调。

**需要权限**：ohos.permission.RUNNING_STATE_OBSERVER

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 调用接口类型，固定填'applicationState'字符串。 |
| observerId | number | 是 | 注册的应用状态监听器ID，即on('applicationState')返回的监听器ID。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](通用错误码.md)和[元能力子系统错误码](元能力子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 16000050 | Internal error. |

**示例：**

```ets
import { appManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let observerId = 0;

// 1.注册应用状态监听器
let applicationStateObserver: appManager.ApplicationStateObserver = {
  onForegroundApplicationChanged(appStateData) {
    console.info(`[appManager] onForegroundApplicationChanged: ${JSON.stringify(appStateData)}`);
  },
  onAbilityStateChanged(abilityStateData) {
    console.info(`[appManager] onAbilityStateChanged: ${JSON.stringify(abilityStateData)}`);
  },
  onProcessCreated(processData) {
    console.info(`[appManager] onProcessCreated: ${JSON.stringify(processData)}`);
  },
  onProcessDied(processData) {
    console.info(`[appManager] onProcessDied: ${JSON.stringify(processData)}`);
  },
  onProcessStateChanged(processData) {
    console.info(`[appManager] onProcessStateChanged: ${JSON.stringify(processData)}`);
  },
  onAppStarted(appStateData) {
    console.info(`[appManager] onAppStarted: ${JSON.stringify(appStateData)}`);
  },
  onAppStopped(appStateData) {
    console.info(`[appManager] onAppStopped: ${JSON.stringify(appStateData)}`);
  }
};
let bundleNameList = ['bundleName1', 'bundleName2'];

try {
  observerId = appManager.on('applicationState', applicationStateObserver, bundleNameList);
} catch (paramError) {
  let code = (paramError as BusinessError).code;
  let message = (paramError as BusinessError).message;
  console.error(`[appManager] error: ${code}, ${message}`);
}

// 2.注销应用状态监听器
try {
  appManager.off('applicationState', observerId).then((data) => {
    console.info(`unregisterApplicationStateObserver success, data: ${JSON.stringify(data)}`);
  }).catch((err: BusinessError) => {
    console.error(`unregisterApplicationStateObserver fail, err: ${JSON.stringify(err)}`);
  });
} catch (paramError) {
  let code = (paramError as BusinessError).code;
  let message = (paramError as BusinessError).message;
  console.error(`[appManager] error: ${code}, ${message}`);
}
```

#### appManager.off('applicationState')15+

off(type: 'applicationState', observerId: number, callback: AsyncCallback<void>): void

注销应用状态监听器。使用callback异步回调。

**需要权限**：ohos.permission.RUNNING_STATE_OBSERVER

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 调用接口类型，固定填'applicationState'字符串。 |
| observerId | number | 是 | 注册的应用状态监听器ID，即on('applicationState')返回的监听器ID。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当取消注册应用程序状态观测器成功，err为undefined，否则为错误对象。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](通用错误码.md)和[元能力子系统错误码](元能力子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 16000050 | Internal error. |

**示例：**

```ets
import { appManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let observerId = 0;

// 1.注册应用状态监听器
let applicationStateObserver: appManager.ApplicationStateObserver = {
  onForegroundApplicationChanged(appStateData) {
    console.info(`[appManager] onForegroundApplicationChanged: ${JSON.stringify(appStateData)}`);
  },
  onAbilityStateChanged(abilityStateData) {
    console.info(`[appManager] onAbilityStateChanged: ${JSON.stringify(abilityStateData)}`);
  },
  onProcessCreated(processData) {
    console.info(`[appManager] onProcessCreated: ${JSON.stringify(processData)}`);
  },
  onProcessDied(processData) {
    console.info(`[appManager] onProcessDied: ${JSON.stringify(processData)}`);
  },
  onProcessStateChanged(processData) {
    console.info(`[appManager] onProcessStateChanged: ${JSON.stringify(processData)}`);
  },
  onAppStarted(appStateData) {
    console.info(`[appManager] onAppStarted: ${JSON.stringify(appStateData)}`);
  },
  onAppStopped(appStateData) {
    console.info(`[appManager] onAppStopped: ${JSON.stringify(appStateData)}`);
  }
};
let bundleNameList = ['bundleName1', 'bundleName2'];

try {
  observerId = appManager.on('applicationState', applicationStateObserver, bundleNameList);
} catch (paramError) {
  let code = (paramError as BusinessError).code;
  let message = (paramError as BusinessError).message;
  console.error(`[appManager] error: ${code}, ${message}`);
}

function offCallback(err: BusinessError) {
  if (err) {
    console.error(`appmanager.off failed, code: ${err.code}, msg: ${err.message}`);
  } else {
    console.info(`appmanager.off success.`);
  }

// 2.注销应用状态监听器
try {
  appManager.off('applicationState', observerId, offCallback);
} catch (paramError) {
  let code = (paramError as BusinessError).code;
  let message = (paramError as BusinessError).message;
  console.error(`[appManager] error: ${code}, ${message}`);
}
```

#### appManager.killProcessesByBundleName14+

killProcessesByBundleName(bundleName: string, clearPageStack: boolean, appIndex?: number): Promise<void>

终止指定应用包名的应用进程。使用Promise异步回调。

**需要权限**：ohos.permission.KILL_APP_PROCESSES 或 ohos.permission.CLEAN_BACKGROUND_PROCESSES

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bundleName | string | 是 | 表示需要终止进程的应用包名。 |
| clearPageStack | boolean | 是 | 表示是否清除页面堆栈。true表示清除，false表示不清除。 |
| appIndex | number | 否 | 应用分身Id，默认值为0。取值为0时，表示终止主应用的所有进程。取值大于0时，表示终止指定分身应用的所有进程。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](通用错误码.md)和[元能力子系统错误码](元能力子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | If the input parameter is not valid parameter. |
| 16000050 | Internal error. |

**示例：**

```ets
import { appManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let bundleName = 'bundleName';
let isClearPageStack = false;
let appIndex = 1;

try {
  appManager.killProcessesByBundleName(bundleName, isClearPageStack, appIndex).then((data) => {
    console.info('killProcessesByBundleName success.');
  }).catch((err: BusinessError) => {
    console.error(`killProcessesByBundleName fail, err: ${JSON.stringify(err)}`);
  });
} catch (paramError) {
  let code = (paramError as BusinessError).code;
  let message = (paramError as BusinessError).message;
  console.error(`[appManager] error: ${code}, ${message}`);
}
```

#### appManager.isAppRunning14+

isAppRunning(bundleName: string, appCloneIndex?: number): Promise<boolean>

判断所有用户下指定包名和分身应用索引的应用是否正在运行。使用Promise异步回调。

如果当前用户未安装该应用，则返回错误码16000073；如果当前用户已安装该应用，则判断所有用户下该指定应用是否正在运行。

**需要权限**：ohos.permission.GET_RUNNING_INFO

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bundleName | string | 是 | 查询的应用包名。 |
| appCloneIndex | number | 否 | 分身应用索引。 取值范围：0~1000。取值为0时表示主应用；取值大于0时表示指定分身应用。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示至少存在一个用户正在运行指定包名和分身应用索引的应用，返回false表示所有用户下指定包名和分身应用索引的应用都没有运行。 |

**错误码**：

 以下错误码详细介绍请参考[通用错误码](通用错误码.md)和[元能力子系统错误码](元能力子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |
| 16000050 | Internal error. |
| 16000073 | The app clone index is invalid. |

**示例：**

```ets
import { appManager } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let bundleName = "ohos.samples.etsclock";
  appManager.isAppRunning(bundleName).then((data: boolean) => {
      hilog.info(0x0000, 'testTag', `data: ${JSON.stringify(data)}`);
    }).catch((err: BusinessError) => {
      hilog.error(0x0000, 'testTag', `isAppRunning error, code: ${err.code}, msg:${err.message}`);
    })
} catch (err) {
  hilog.error(0x0000, 'testTag', `isAppRunning error, code: ${err.code}, msg:${err.message}`);
}
```

#### AbilityStateData14+

type AbilityStateData = [_AbilityStateData.default](../../topics/misc/AbilityStateData.md)

Ability状态信息。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 类型 | 说明 |
| --- | --- |
| [_AbilityStateData.default](../../topics/misc/AbilityStateData.md) | Ability状态信息。 |

#### AppStateData14+

type AppStateData = [_AppStateData.default](../../topics/misc/AppStateData.md)

应用状态信息。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 类型 | 说明 |
| --- | --- |
| [_AppStateData.default](../../topics/misc/AppStateData.md) | 应用状态信息。 |

#### [ApplicationStateObserver](../../topics/misc/ApplicationStateObserver.md)14+

type [ApplicationStateObserver](../../topics/misc/ApplicationStateObserver.md) = [_ApplicationStateObserver.default](../../topics/misc/ApplicationStateObserver.md)

应用状态监听器。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 类型 | 说明 |
| --- | --- |
| _[ApplicationStateObserver](../../topics/misc/ApplicationStateObserver.md).default | 应用状态监听器。 |

#### [ProcessInformation](../../topics/misc/ProcessInformation.md)

type [ProcessInformation](../../topics/misc/ProcessInformation.md) = [_ProcessInformation](../../topics/misc/ProcessInformation.md)

进程信息。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 类型 | 说明 |
| --- | --- |
| _[ProcessInformation](../../topics/misc/ProcessInformation.md) | 进程信息。 |

#### ProcessData14+

type ProcessData = [_ProcessData.default](../../topics/misc/ProcessData.md)

进程数据。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 类型 | 说明 |
| --- | --- |
| [_ProcessData.default](../../topics/misc/ProcessData.md) | 进程数据。 |