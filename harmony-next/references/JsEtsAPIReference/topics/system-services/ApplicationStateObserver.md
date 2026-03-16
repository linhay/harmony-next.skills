# ApplicationStateObserver

应用状态监听器，可以作为入参传入[on('applicationState')](../../modules/ohos/@ohos.app.ability.appManager (应用管理).md#ZH-CN_TOPIC_0000002497444628__appmanageronapplicationstate14)方法，监听应用的生命周期变化。

本模块首批接口从API version 14开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { appManager } from '@kit.AbilityKit';
```

#### ApplicationStateObserver.onForegroundApplicationChanged

onForegroundApplicationChanged(appStateData: AppStateData): void

应用前后台状态发生变化时执行的回调函数。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数**：

参数名类型必填说明appStateData[AppStateData](AppStateData.md)是应用状态信息。

#### ApplicationStateObserver.onAbilityStateChanged

onAbilityStateChanged(abilityStateData: AbilityStateData): void

Ability状态发生变化时执行的回调函数。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数**：

参数名类型必填说明abilityStateData[AbilityStateData](AbilityStateData.md)是Ability状态信息。

#### ApplicationStateObserver.onProcessCreated

onProcessCreated(processData: ProcessData): void

进程创建时执行的回调函数。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数**：

参数名类型必填说明processData[ProcessData](ProcessData.md)是进程数据信息。

#### ApplicationStateObserver.onProcessDied

onProcessDied(processData: ProcessData): void

进程销毁时执行的回调函数。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数**：

参数名类型必填说明processData[ProcessData](ProcessData.md)是进程数据信息。

#### ApplicationStateObserver.onProcessStateChanged

onProcessStateChanged(processData: ProcessData): void

进程状态更新时执行的回调函数。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数**：

参数名类型必填说明processData[ProcessData](ProcessData.md)是进程数据信息。

#### ApplicationStateObserver.onAppStarted

onAppStarted(appStateData: AppStateData): void

应用第一个进程创建时执行的回调函数。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数**：

参数名类型必填说明appStateData[AppStateData](AppStateData.md)是应用状态信息。

#### ApplicationStateObserver.onAppStopped

onAppStopped(appStateData: AppStateData): void

应用最后一个进程销毁时执行的回调函数。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数**：

参数名类型必填说明appStateData[AppStateData](AppStateData.md)是应用状态信息。

#### ProcessData

type ProcessData = _ProcessData.default

进程数据信息。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

类型说明[_ProcessData.default](ProcessData.md)进程数据信息。

**示例：**

```ets
import { appManager } from '@kit.AbilityKit';

let applicationStateObserver: appManager.ApplicationStateObserver = {
  onForegroundApplicationChanged(appStateData) {
    console.info(`onForegroundApplicationChanged, appStateData: ${JSON.stringify(appStateData)}.`);
  },
  onAbilityStateChanged(abilityStateData) {
    console.info(`onAbilityStateChanged, abilityStateData: ${JSON.stringify(abilityStateData)}.`);
  },
  onProcessCreated(processData) {
    console.info(`onProcessCreated, processData: ${JSON.stringify(processData)}.`);
  },
  onProcessDied(processData) {
    console.info(`onProcessDied, processData: ${JSON.stringify(processData)}.`);
  },
  onProcessStateChanged(processData) {
    console.info(`onProcessStateChanged, processData: ${JSON.stringify(processData)}.`);
  },
  onAppStarted(appStateData) {
    console.info(`onAppStarted, appStateData: ${JSON.stringify(appStateData)}.`);
  },
  onAppStopped(appStateData) {
    console.info(`onAppStopped, appStateData: ${JSON.stringify(appStateData)}.`);
  }
};
let observerCode = appManager.on('applicationState', applicationStateObserver);
```