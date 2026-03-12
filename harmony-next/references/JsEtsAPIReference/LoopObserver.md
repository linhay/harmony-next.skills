# LoopObserver

定义异常监听，可以作为[ErrorManager.on](@ohos.app.ability.errorManager (错误管理模块).md#ZH-CN_TOPIC_0000002497604610__errormanageronloopobserver12)的入参监听当前应用主线程事件处理事件。

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { errorManager } from '@kit.AbilityKit';
```

#### LoopObserver.onLoopTimeOut

onLoopTimeOut?(timeout: number): void

将在js运行时应用主线程处理事件超时的回调。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

参数名类型必填说明timeoutnumber是返回应用主线程消息实际执行时间。

**示例：**

```ets
import { errorManager } from '@kit.AbilityKit';

let observer: errorManager.LoopObserver = {
  onLoopTimeOut(timeout: number) {
    console.info('Duration timeout: ' + timeout);
  }
};

errorManager.on("loopObserver", 1, observer);
```