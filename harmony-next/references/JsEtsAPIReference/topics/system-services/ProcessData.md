# ProcessData

进程数据的对象定义。使用接口[appManager.on('applicationState')](../../modules/ohos/@ohos.app.ability.appManager (应用管理).md#ZH-CN_TOPIC_0000002497444628__appmanageronapplicationstate14)注册生命周期变化监听后，当应用或组件的生命周期变化时，系统通过[ApplicationStateObserver](ApplicationStateObserver.md)的[onProcessCreated](ApplicationStateObserver.md#ZH-CN_TOPIC_0000002529444587__applicationstateobserveronprocesscreated)等方法回调给开发者。

本模块首批接口从API version 14开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { appManager } from '@kit.AbilityKit';
```

#### 属性

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

名称类型只读可选说明pidnumber否否进程ID。bundleNamestring否否应用包名。uidnumber否否应用的uid。isContinuousTaskboolean否否是否为长时任务，true表示是，false表示不是。isKeepAliveboolean否否是否为常驻进程，true表示是，false表示不是statenumber否否

应用的状态，取值及对应的状态为：

0 - 初始化状态，进程正在初始化，

1 - 就绪状态，进程已初始化完毕，

2 - 前台，

4 - 后台，

5 - 已终止。

**示例：**

```ets
import { appManager } from '@kit.AbilityKit';

let observerCode = appManager.on('applicationState', {
  onForegroundApplicationChanged(appStateData: appManager.AppStateData) {
    console.info(`onForegroundApplicationChanged, appStateData: ${JSON.stringify(appStateData)}.`);
  },
  onAbilityStateChanged(abilityStateData: appManager.AbilityStateData) {
    console.info(`onAbilityStateChanged, abilityStateData: ${JSON.stringify(abilityStateData)}.`);
  },
  onProcessCreated(processData: appManager.ProcessData) {
    console.info(`onProcessCreated, processData: ${JSON.stringify(processData)}.`);
  },
  onProcessDied(processData: appManager.ProcessData) {
    console.info(`onProcessDied, processData: ${JSON.stringify(processData)}.`);
  },
  onProcessStateChanged(processData: appManager.ProcessData) {
    console.info(`onProcessStateChanged, processData.pid : ${JSON.stringify(processData.pid)}.`);
    console.info(`onProcessStateChanged, processData.bundleName : ${JSON.stringify(processData.bundleName)}.`);
    console.info(`onProcessStateChanged, processData.uid : ${JSON.stringify(processData.uid)}.`);
    console.info(`onProcessStateChanged, processData.isContinuousTask : ${JSON.stringify(processData.isContinuousTask)}.`);
    console.info(`onProcessStateChanged, processData.isKeepAlive : ${JSON.stringify(processData.isKeepAlive)}.`);
  },
  onAppStarted(appStateData: appManager.AppStateData) {
    console.info(`onAppStarted, appStateData: ${JSON.stringify(appStateData)}.`);
  },
  onAppStopped(appStateData: appManager.AppStateData) {
    console.info(`onAppStopped, appStateData: ${JSON.stringify(appStateData)}.`);
  }
});
```