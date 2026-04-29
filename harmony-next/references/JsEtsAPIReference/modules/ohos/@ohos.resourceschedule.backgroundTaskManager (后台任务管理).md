# @ohos.resourceschedule.backgroundTaskManager (后台任务管理)

本模块提供申请后台任务的接口。当应用退至后台时，开发者可以通过本模块接口为应用申请短时、长时任务，避免应用进程被终止或挂起。开发指导请参考[长时任务开发指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/continuous-task)、[短时任务开发指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/transient-task)。

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { backgroundTaskManager } from '@kit.BackgroundTasksKit';
```

#### backgroundTaskManager.requestSuspendDelay

requestSuspendDelay(reason: string, callback: Callback<void>): DelaySuspendInfo

申请短时任务。

短时任务的申请和使用过程中的约束与限制请参考[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/transient-task#约束与限制)。

**系统能力:** SystemCapability.ResourceSchedule.BackgroundTaskManager.TransientTask

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| reason | string | 是 | 申请短时任务的原因。 |
| callback | Callback<void> | 是 | 短时任务即将超时的回调函数，一般在超时前6秒，通过此回调通知应用。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| DelaySuspendInfo | 返回短时任务信息。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码]([通用错误码](../../errors/通用错误码.md).md)和[backgroundTaskManager错误码]([backgroundTaskManager错误码](../../errors/backgroundTaskManager错误码.md).md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 9800001 | Memory operation failed. |
| 9800002 | Failed to write data into parcel. Possible reasons: 1. Invalid parameters; 2. Failed to apply for memory. |
| 9800003 | Internal transaction failed. |
| 9800004 | System service operation failed. |
| 9900001 | Caller information verification failed for a transient task. |
| 9900002 | Transient task verification failed. |

**示例**：

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { backgroundTaskManager } from '@kit.BackgroundTasksKit';

let myReason = 'test requestSuspendDelay';
try {
    let delayInfo = backgroundTaskManager.requestSuspendDelay(myReason, () => {
    // 回调函数。应用申请的短时任务即将超时，通过此函数回调应用，执行一些清理和标注工作，并取消短时任务
    // 此处回调与应用的业务功能不耦合，短时任务申请成功后，正常执行应用本身的业务
        console.info("Request suspension delay will time out.");
    })
    let id = delayInfo.requestId;
    let time = delayInfo.actualDelayTime;
    console.info("The requestId is: " + id);
    console.info("The actualDelayTime is: " + time);
} catch (error) {
    console.error(`requestSuspendDelay failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}`);
}
```

#### backgroundTaskManager.getRemainingDelayTime

getRemainingDelayTime(requestId: number, callback: AsyncCallback<number>): void

获取本次短时任务的剩余时间，使用callback异步回调。

**系统能力:** SystemCapability.ResourceSchedule.BackgroundTaskManager.TransientTask

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| requestId | number | 是 | 短时任务的请求ID。通过申请短时任务requestSuspendDelay接口获取。 |
| callback | AsyncCallback<number> | 是 | 回调函数，返回本次短时任务的剩余时间，单位：ms。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[backgroundTaskManager错误码](backgroundTaskManager错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |
| 9800001 | Memory operation failed. |
| 9800002 | Failed to write data into parcel. Possible reasons: 1. Invalid parameters; 2. Failed to apply for memory. |
| 9800003 | Internal transaction failed. |
| 9800004 | System service operation failed. |
| 9900001 | Caller information verification failed for a transient task. |
| 9900002 | Transient task verification failed. |

**示例**：

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { backgroundTaskManager } from '@kit.BackgroundTasksKit';

let id = 1;
backgroundTaskManager.getRemainingDelayTime(id, (error: BusinessError, res: number) => {
    if(error) {
        console.error(`callback => Operation getRemainingDelayTime failed. code is ${error.code} message is ${error.message}`);
    } else {
        console.info('callback => Operation getRemainingDelayTime succeeded. Data: ' + JSON.stringify(res));
    }
})
```

#### backgroundTaskManager.getRemainingDelayTime

getRemainingDelayTime(requestId: number): Promise<number>

获取本次短时任务的剩余时间，使用Promise异步回调。

**系统能力:** SystemCapability.ResourceSchedule.BackgroundTaskManager.TransientTask

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| requestId | number | 是 | 短时任务的请求ID。通过申请短时任务requestSuspendDelay接口获取。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回本次短时任务的剩余时间，单位：ms。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[backgroundTaskManager错误码](backgroundTaskManager错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |
| 9800001 | Memory operation failed. |
| 9800002 | Failed to write data into parcel. Possible reasons: 1. Invalid parameters; 2. Failed to apply for memory. |
| 9800003 | Internal transaction failed. |
| 9800004 | System service operation failed. |
| 9900001 | Caller information verification failed for a transient task. |
| 9900002 | Transient task verification failed. |

**示例**：

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { backgroundTaskManager } from '@kit.BackgroundTasksKit';

let id = 1;
backgroundTaskManager.getRemainingDelayTime(id).then((res: number) => {
    console.info('promise => Operation getRemainingDelayTime succeeded. Data: ' + JSON.stringify(res));
}).catch((error: BusinessError) => {
    console.error(`promise => Operation getRemainingDelayTime failed. code is ${error.code} message is ${error.message}`);
})
```

#### backgroundTaskManager.cancelSuspendDelay

cancelSuspendDelay(requestId: number): void

取消短时任务。

**系统能力:** SystemCapability.ResourceSchedule.BackgroundTaskManager.TransientTask

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| requestId | number | 是 | 短时任务的请求ID。通过申请短时任务requestSuspendDelay接口获取。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[backgroundTaskManager错误码](backgroundTaskManager错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |
| 9800001 | Memory operation failed. |
| 9800002 | Failed to write data into parcel. Possible reasons: 1. Invalid parameters; 2. Failed to apply for memory. |
| 9800003 | Internal transaction failed. |
| 9800004 | System service operation failed. |
| 9900001 | Caller information verification failed for a transient task. |
| 9900002 | Transient task verification failed. |

**示例**：

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { backgroundTaskManager } from '@kit.BackgroundTasksKit';

let id = 1;
try {
  backgroundTaskManager.cancelSuspendDelay(id);
} catch (error) {
  console.error(`cancelSuspendDelay failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}`);
}
```

#### backgroundTaskManager.getTransientTaskInfo20+

getTransientTaskInfo(): Promise<TransientTaskInfo>

获取所有短时任务信息，如当日剩余总配额等，使用Promise异步回调。

**系统能力**: SystemCapability.ResourceSchedule.BackgroundTaskManager.TransientTask

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<TransientTaskInfo> | Promise对象，返回所有短时任务信息。 |

**错误码**：

以下错误码的详细介绍请参见[backgroundTaskManager错误码](backgroundTaskManager错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9900001 | Caller information verification failed for a transient task. |
| 9900003 | Failed to write data into parcel. Possible reasons: 1. Invalid parameters; 2. Failed to apply for memory. |
| 9900004 | System service operation failed. |

**示例**：

```ets
import { backgroundTaskManager } from '@kit.BackgroundTasksKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
    backgroundTaskManager.getTransientTaskInfo().then((res: backgroundTaskManager.TransientTaskInfo) => {
        console.info(`Operation getTransientTaskInfo succeeded. data: ` + JSON.stringify(res));
    }).catch((error : BusinessError) => {
        console.error(`Operation getTransientTaskInfo failed. code is ${error.code} message is ${error.message}`);
    });
} catch (error) {
    console.error(`Operation getTransientTaskInfo failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}`);
}
```

#### backgroundTaskManager.startBackgroundRunning

startBackgroundRunning(context: Context, bgMode: BackgroundMode, wantAgent: WantAgent, callback: AsyncCallback<void>): void

申请长时任务，支持申请一种类型，使用callback异步回调。长时任务申请成功后，会有通知栏消息，没有提示音。一个UIAbility（FA模型则为ServiceAbility）同一时刻仅支持通过本接口支持申请一个长时任务，可以通过API version 21新增接口[startBackgroundRunning](#ZH-CN_TOPIC_0000002553361127__backgroundtaskmanagerstartbackgroundrunning21)申请多个长时任务。

**需要权限:** ohos.permission.KEEP_BACKGROUND_RUNNING

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用运行的上下文。 FA模型的应用Context定义见Context。 Stage模型的应用Context定义见Context。 |
| bgMode | BackgroundMode | 是 | 长时任务类型。 |
| wantAgent | WantAgent | 是 | 通知参数，用于指定点击长时任务通知后跳转的界面。 |
| callback | AsyncCallback<void> | 是 | 回调函数，申请长时任务成功时，err为undefined，否则为错误对象。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[backgroundTaskManager错误码](backgroundTaskManager错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 202 | Not System App. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |
| 9800001 | Memory operation failed. |
| 9800002 | Failed to write data into parcel. Possible reasons: 1. Invalid parameters; 2. Failed to apply for memory. |
| 9800003 | Internal transaction failed. |
| 9800004 | System service operation failed. |
| 9800005 | Continuous task verification failed. |
| 9800006 | Notification verification failed for a continuous task. |
| 9800007 | Continuous task storage failed. |

**示例**：

```ets
import { backgroundTaskManager } from '@kit.BackgroundTasksKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { wantAgent, WantAgent } from '@kit.AbilityKit';
// 在元服务中，请删除WantAgent导入

function callback(error: BusinessError, data: void) {
    if (error) {
        console.error(`Operation startBackgroundRunning failed. code is ${error.code} message is ${error.message}`);
    } else {
        console.info("Operation startBackgroundRunning succeeded");
}

export default class EntryAbility extends UIAbility {
    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
        let wantAgentInfo: wantAgent.WantAgentInfo = {
            // 点击通知后，将要执行的动作列表
            wants: [
                {
                    bundleName: "com.example.myapplication",
                    abilityName: "EntryAbility"
                }
            ],
            // 点击通知后，动作类型
            actionType: wantAgent.OperationType.START_ABILITY,
            // 使用者自定义的一个私有值
            requestCode: 0,
            // 点击通知后，动作执行属性
            wantAgentFlags: [wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
        };

        try {
            // 通过wantAgent模块下getWantAgent方法获取WantAgent对象
            // 在元服务中，请使用wantAgent.getWantAgent(wantAgentInfo).then((wantAgentObj: object) => {替换下面一行代码
            wantAgent.getWantAgent(wantAgentInfo).then((wantAgentObj: WantAgent) => {
                try {
                    backgroundTaskManager.startBackgroundRunning(this.context,
                        backgroundTaskManager.BackgroundMode.AUDIO_PLAYBACK, wantAgentObj, callback)
                } catch (error) {
                    console.error(`Operation startBackgroundRunning failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}`);
                }
            });
        } catch (error) {
            console.error(`Operation getWantAgent failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}`);
        }
};
```

#### backgroundTaskManager.startBackgroundRunning

startBackgroundRunning(context: Context, bgMode: BackgroundMode, wantAgent: WantAgent): Promise<void>

申请长时任务，支持申请一种类型，使用Promise异步回调。长时任务申请成功后，会有通知栏消息，没有提示音。一个UIAbility（FA模型则为ServiceAbility）同一时刻仅支持通过本接口支持申请一个长时任务，可以通过API version 21新增接口[startBackgroundRunning](#ZH-CN_TOPIC_0000002553361127__backgroundtaskmanagerstartbackgroundrunning21)申请多个长时任务。

**需要权限:** ohos.permission.KEEP_BACKGROUND_RUNNING

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用运行的上下文。 FA模型的应用Context定义见Context。 Stage模型的应用Context定义见Context。 |
| bgMode | BackgroundMode | 是 | 长时任务类型。 |
| wantAgent | WantAgent | 是 | 通知参数，用于指定点击长时任务通知后跳转的界面。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[backgroundTaskManager错误码](backgroundTaskManager错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 202 | Not System App. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |
| 9800001 | Memory operation failed. |
| 9800002 | Failed to write data into parcel. Possible reasons: 1. Invalid parameters; 2. Failed to apply for memory. |
| 9800003 | Internal transaction failed. |
| 9800004 | System service operation failed. |
| 9800005 | Continuous task verification failed. |
| 9800006 | Notification verification failed for a continuous task. |
| 9800007 | Continuous task storage failed. |

**示例**：

```ets
import { backgroundTaskManager } from '@kit.BackgroundTasksKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { wantAgent, WantAgent } from '@kit.AbilityKit';
// 在元服务中，请删除WantAgent导入

export default class EntryAbility extends UIAbility {
    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
        let wantAgentInfo: wantAgent.WantAgentInfo = {
            // 点击通知后，将要执行的动作列表
            wants: [
                {
                    bundleName: "com.example.myapplication",
                    abilityName: "EntryAbility"
                }
            ],
            // 点击通知后，动作类型
            actionType: wantAgent.OperationType.START_ABILITY,
            // 使用者自定义的一个私有值
            requestCode: 0,
            // 点击通知后，动作执行属性
            wantAgentFlags: [wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
        };

        try {
            // 通过wantAgent模块下getWantAgent方法获取WantAgent对象
            // 在元服务中，请使用wantAgent.getWantAgent(wantAgentInfo).then((wantAgentObj: object) => {替换下面一行代码
            wantAgent.getWantAgent(wantAgentInfo).then((wantAgentObj: WantAgent) => {
                try {
                    backgroundTaskManager.startBackgroundRunning(this.context,
                        backgroundTaskManager.BackgroundMode.AUDIO_PLAYBACK, wantAgentObj).then(() => {
                        console.info("Operation startBackgroundRunning succeeded");
                    }).catch((error: BusinessError) => {
                        console.error(`Operation startBackgroundRunning failed. code is ${error.code} message is ${error.message}`);
                    });
                } catch (error) {
                    console.error(`Operation startBackgroundRunning failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}`);
                }
            });
        } catch (error) {
            console.error(`Operation getWantAgent failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}`);
        }
};
```

#### backgroundTaskManager.stopBackgroundRunning

stopBackgroundRunning(context: Context, callback: AsyncCallback<void>): void

取消当前UIAbility（FA模型则为ServiceAbility）下所有长时任务，使用callback异步回调。也可以通过[stopBackgroundRunning](#ZH-CN_TOPIC_0000002553361127__backgroundtaskmanagerstopbackgroundrunning21)接口取消指定Id的长时任务。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用运行的上下文。 FA模型的应用Context定义见Context。 Stage模型的应用Context定义见Context。 |
callbackAsyncCallback<void>是回调函数，取消长时任务成功时，err为undefined，否则为错误对象。

**错误码**：

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[backgroundTaskManager错误码](backgroundTaskManager错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. |
| 9800001 | Memory operation failed. |
| 9800002 | Failed to write data into parcel. Possible reasons: 1. Invalid parameters; 2. Failed to apply for memory. |
| 9800003 | Internal transaction failed. |
| 9800004 | System service operation failed. |
| 9800005 | Continuous task verification failed. |
| 9800006 | Notification verification failed for a continuous task. |
| 9800007 | Continuous task storage failed. |

**示例**：

```ets
import { backgroundTaskManager } from '@kit.BackgroundTasksKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';

function callback(error: BusinessError, data: void) {
    if (error) {
        console.error(`Operation stopBackgroundRunning failed. code is ${error.code} message is ${error.message}`);
    } else {
        console.info("Operation stopBackgroundRunning succeeded");
    }

export default class EntryAbility extends UIAbility {
    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
        try {
            backgroundTaskManager.stopBackgroundRunning(this.context, callback);
        } catch (error) {
            console.error(`Operation stopBackgroundRunning failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}`);
        }
};
```

#### backgroundTaskManager.stopBackgroundRunning

stopBackgroundRunning(context: Context): Promise<void>

取消当前UIAbility（FA模型则为ServiceAbility）下所有长时任务，使用Promise异步回调。也可以通过[stopBackgroundRunning](#ZH-CN_TOPIC_0000002553361127__backgroundtaskmanagerstopbackgroundrunning21)接口取消指定Id的长时任务。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用运行的上下文。 FA模型的应用Context定义见Context。 Stage模型的应用Context定义见Context。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[backgroundTaskManager错误码](backgroundTaskManager错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. |
| 9800001 | Memory operation failed. |
| 9800002 | Failed to write data into parcel. Possible reasons: 1. Invalid parameters; 2. Failed to apply for memory. |
| 9800003 | Internal transaction failed. |
| 9800004 | System service operation failed. |
| 9800005 | Continuous task verification failed. |
| 9800006 | Notification verification failed for a continuous task. |
| 9800007 | Continuous task storage failed. |

**示例**：

```ets
import { backgroundTaskManager } from '@kit.BackgroundTasksKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';

export default class EntryAbility extends UIAbility {
    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
        try {
            backgroundTaskManager.stopBackgroundRunning(this.context).then(() => {
                console.info("Operation stopBackgroundRunning succeeded");
            }).catch((error: BusinessError) => {
                console.error(`Operation stopBackgroundRunning failed. code is ${error.code} message is ${error.message}`);
            });
        } catch (error) {
            console.error(`Operation stopBackgroundRunning failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}`);
        }
};
```

#### backgroundTaskManager.startBackgroundRunning12+

startBackgroundRunning(context: Context, bgModes: string[], wantAgent: WantAgent): Promise<ContinuousTaskNotification>

申请长时任务，支持申请多种类型，使用Promise异步回调。长时任务申请成功后，会有通知栏消息，没有提示音。一个UIAbility（FA模型则为ServiceAbility）同一时刻仅支持通过本接口支持申请一个长时任务，可以通过API version 21新增接口[startBackgroundRunning](#ZH-CN_TOPIC_0000002553361127__backgroundtaskmanagerstartbackgroundrunning21)申请多个长时任务。

**需要权限:** ohos.permission.KEEP_BACKGROUND_RUNNING

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用运行的上下文。 |
| bgModes | string[] | 是 | 长时任务类型，取值范围请参考长时任务类型中的配置项。 说明： 支持传入一个或多个类型。 |
| wantAgent | WantAgent | 是 | 通知参数，用于指定点击长时任务通知后跳转的界面。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<ContinuousTaskNotification> | Promise对象，返回ContinuousTaskNotification类型对象。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[backgroundTaskManager错误码](backgroundTaskManager错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |
| 9800001 | Memory operation failed. |
| 9800002 | Failed to write data into parcel. Possible reasons: 1. Invalid parameters; 2. Failed to apply for memory. |
| 9800003 | Internal transaction failed. |
| 9800004 | System service operation failed. |
| 9800005 | Continuous task verification failed. |
| 9800006 | Notification verification failed for a continuous task. |
| 9800007 | Continuous task storage failed. |

**示例**：

```ets
import { backgroundTaskManager } from '@kit.BackgroundTasksKit';
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { notificationManager } from '@kit.NotificationKit';
import { wantAgent, WantAgent } from '@kit.AbilityKit';
// 在元服务中，请删除WantAgent导入

export default class EntryAbility extends UIAbility {
  id: number = 0; // 保存通知id

  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    let wantAgentInfo: wantAgent.WantAgentInfo = {
      // 点击通知后，将要执行的动作列表
      wants: [
        {
          bundleName: "com.example.myapplication",
          abilityName: "EntryAbility"
        }
      ],
      // 点击通知后，动作类型
      actionType: wantAgent.OperationType.START_ABILITY,
      // 使用者自定义的一个私有值
      requestCode: 0,
      // 点击通知后，动作执行属性
      wantAgentFlags: [wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
    };

    try {
      // 通过wantAgent模块下getWantAgent方法获取WantAgent对象
      // 在元服务中，请使用wantAgent.getWantAgent(wantAgentInfo).then((wantAgentObj: object) => {替换下面一行代码
      wantAgent.getWantAgent(wantAgentInfo).then((wantAgentObj: WantAgent) => {
        try {
          let list: Array<string> = ["dataTransfer"];
          // 在元服务中，let list: Array<string> = ["audioPlayback"];
          backgroundTaskManager.startBackgroundRunning(this.context, list, wantAgentObj).then((res: backgroundTaskManager.ContinuousTaskNotification) => {
            console.info("Operation startBackgroundRunning succeeded");
            // 对于上传下载类的长时任务，应用可以使用res中返回的notificationId来更新通知，比如发送带进度条的模板通知
            this.id = res.notificationId;
          }).catch((error: BusinessError) => {
            console.error(`Operation startBackgroundRunning failed. code is ${error.code} message is ${error.message}`);
          });
        } catch (error) {
          console.error(`Operation startBackgroundRunning failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}`);
        }
      });
    } catch (error) {
      console.error(`Operation getWantAgent failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}`);
    }

  // 应用更新进度
  updateProcess(process: number) {
    // 定义通知类型，更新进度时的通知类型必须为实况窗
    let downLoadTemplate: notificationManager.NotificationTemplate = {
      name: 'downloadTemplate', // 当前只支持downloadTemplate，保持不变
      data: {
        title: '文件下载：music.mp4', // 必填
        fileName: 'senTemplate', // 必填
        progressValue: process, // 应用更新进度值，自定义
      }
    };
    let request: notificationManager.NotificationRequest = {
      content: {
        // 系统实况类型，保持不变
        notificationContentType: notificationManager.ContentType.NOTIFICATION_CONTENT_SYSTEM_LIVE_VIEW,
        systemLiveView: {
          typeCode: 8, // 上传下载类型需要填写 8，当前仅支持此类型。保持不变
          title: "test", // 应用自定义
          text: "test", // 应用自定义
        }
      },
      id: this.id, // 必须是申请长时任务返回的id，否则应用更新通知失败
      notificationSlotType: notificationManager.SlotType.LIVE_VIEW, // 实况窗类型，保持不变
      template: downLoadTemplate // 应用需要设置的模版名称
    };

    try {
      notificationManager.publish(request).then(() => {
        console.info("publish success, id= " + this.id);
      }).catch((err: BusinessError) => {
        console.error(`publish fail: ${JSON.stringify(err)}`);
      });
    } catch (err) {
      console.error(`publish fail: ${JSON.stringify(err)}`);
    }
};
```

#### backgroundTaskManager.updateBackgroundRunning12+

updateBackgroundRunning(context: Context, bgModes: string[]): Promise<ContinuousTaskNotification>

更新长时任务类型，使用Promise异步回调。长时任务更新成功后，会有通知栏消息，没有提示音。

更新长时任务前，可以通过[getAllContinuousTasks](#ZH-CN_TOPIC_0000002553361127__backgroundtaskmanagergetallcontinuoustasks20)接口获取当前所有长时任务信息，如果当前没有已经存在的长时任务，会更新失败。

该接口仅支持更新如下三个接口申请的长时任务：

[startBackgroundRunning(context: Context, bgMode: BackgroundMode, wantAgent: WantAgent, callback: AsyncCallback<void>): void](#ZH-CN_TOPIC_0000002553361127__backgroundtaskmanagerstartbackgroundrunning)

[startBackgroundRunning(context: Context, bgMode: BackgroundMode, wantAgent: WantAgent): Promise<void>](#ZH-CN_TOPIC_0000002553361127__backgroundtaskmanagerstartbackgroundrunning-1)

[startBackgroundRunning(context: Context, bgModes: string[], wantAgent: WantAgent): Promise<ContinuousTaskNotification>](#ZH-CN_TOPIC_0000002553361127__backgroundtaskmanagerstartbackgroundrunning12)

**需要权限:** ohos.permission.KEEP_BACKGROUND_RUNNING

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用运行的上下文。 |
| bgModes | string[] | 是 | 更新后的长时任务类型，取值范围请参考长时任务类型中的配置项。 说明： 支持传入一个或多个类型。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<ContinuousTaskNotification> | Promise对象，返回ContinuousTaskNotification类型对象。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[backgroundTaskManager错误码](backgroundTaskManager错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |
| 9800001 | Memory operation failed. |
| 9800002 | Failed to write data into parcel. Possible reasons: 1. Invalid parameters; 2. Failed to apply for memory. |
| 9800003 | Internal transaction failed. |
| 9800004 | System service operation failed. |
| 9800005 | Continuous task verification failed. |
| 9800006 | Notification verification failed for a continuous task. |
| 9800007 | Continuous task storage failed. |

**示例**：

```ets
import { backgroundTaskManager } from '@kit.BackgroundTasksKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';

export default class EntryAbility extends UIAbility {
    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
        try {
            // 必须先执行startBackgroundRunning，才能调用updateBackgroundRunning，这里假设已经申请过
            let list: Array<string> = ["audioPlayback"];
            backgroundTaskManager.updateBackgroundRunning(this.context, list).then(() => {
                console.info("Operation updateBackgroundRunning succeeded");
            }).catch((error: BusinessError) => {
                console.error(`Operation updateBackgroundRunning failed. code is ${error.code} message is ${error.message}`);
            });
        } catch (error) {
            console.error(`Operation updateBackgroundRunning failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}`);
        }
};
```

#### backgroundTaskManager.getAllContinuousTasks20+

getAllContinuousTasks(context: Context): Promise<ContinuousTaskInfo[]>

获取所有长时任务信息，如长时任务ID、长时任务类型等，使用Promise异步回调。

**需要权限**: ohos.permission.KEEP_BACKGROUND_RUNNING

**系统能力**: SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用运行的上下文。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<ContinuousTaskInfo[]> | Promise对象，返回所有长时任务信息。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[backgroundTaskManager错误码](backgroundTaskManager错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 9800002 | Failed to write data into parcel. Possible reasons: 1. Invalid parameters; 2. Failed to apply for memory. |
| 9800004 | System service operation failed. |
| 9800005 | Continuous task verification failed. |

**示例**：

```ets
import { backgroundTaskManager } from '@kit.BackgroundTasksKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';

export default class EntryAbility extends UIAbility {
    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
        try {
            // 如果当前没有申请长时任务，则获取到一个空数组
            backgroundTaskManager.getAllContinuousTasks(this.context).then((res: backgroundTaskManager.ContinuousTaskInfo[]) => {
                console.info(`Operation getAllContinuousTasks succeeded. data: ` + JSON.stringify(res));
            }).catch((error: BusinessError) => {
                console.error(`Operation getAllContinuousTasks failed. code is ${error.code} message is ${error.message}`);
            });
        } catch (error) {
            console.error(`Operation getAllContinuousTasks failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}`);
        }
};
```

#### backgroundTaskManager.getAllContinuousTasks20+

getAllContinuousTasks(context: Context, includeSuspended: boolean): Promise<ContinuousTaskInfo[]>

获取所有长时任务信息，如长时任务ID、长时任务类型等。可选择是否获取暂停的长时任务信息，使用Promise异步回调。

**需要权限**: ohos.permission.KEEP_BACKGROUND_RUNNING

**系统能力**: SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用运行的上下文。 |
| includeSuspended | boolean | 是 | 是否获取暂停的长时任务信息， true表示获取， false表示不获取。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<ContinuousTaskInfo[]> | Promise对象，返回所有长时任务信息。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[backgroundTaskManager错误码](backgroundTaskManager错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 9800002 | Failed to write data into parcel. Possible reasons: 1. Invalid parameters; 2. Failed to apply for memory. |
| 9800004 | System service operation failed. |
| 9800005 | Continuous task verification failed. |

**示例**：

```ets
import { backgroundTaskManager } from '@kit.BackgroundTasksKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';

export default class EntryAbility extends UIAbility {
    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
        try {
            // 如果当前没有申请长时任务，则获取到一个空数组
            backgroundTaskManager.getAllContinuousTasks(this.context, false).then((res: backgroundTaskManager.ContinuousTaskInfo[]) => {
                console.info(`Operation getAllContinuousTasks succeeded. data: ` + JSON.stringify(res));
            }).catch((error: BusinessError) => {
                console.error(`Operation getAllContinuousTasks failed. code is ${error.code} message is ${error.message}`);
            });
        } catch (error) {
            console.error(`Operation getAllContinuousTasks failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}`);
        }
};
```

#### backgroundTaskManager.on('continuousTaskCancel')15+

on(type: 'continuousTaskCancel', callback: Callback<ContinuousTaskCancelInfo>): void

注册长时任务取消的监听，使用callback异步回调。

**需要权限:** ohos.permission.KEEP_BACKGROUND_RUNNING

**系统能力:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，固定取值为'continuousTaskCancel'，表示长时任务取消。 |
| callback | Callback<ContinuousTaskCancelInfo> | 是 | 回调函数，返回长时任务取消原因等信息。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible cause: 1. Callback parameter error; 2. Register a exist callback type; 3. Parameter verification failed. |

**示例**：

```ets
import { backgroundTaskManager } from '@kit.BackgroundTasksKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';

function callback(info: backgroundTaskManager.ContinuousTaskCancelInfo) {
  console.info('continuousTaskCancel callback id ' + info.id);
  console.info('continuousTaskCancel callback reason ' + info.reason);
}

export default class EntryAbility extends UIAbility {
    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
        try {
            backgroundTaskManager.on("continuousTaskCancel", callback);
        } catch (error) {
            console.error(`Operation onContinuousTaskCancel failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}`);
        }
};
```

#### backgroundTaskManager.off('continuousTaskCancel')15+

off(type: 'continuousTaskCancel', callback?: Callback<ContinuousTaskCancelInfo>): void

解除长时任务取消的监听，使用callback异步回调。

**需要权限:** ohos.permission.KEEP_BACKGROUND_RUNNING

**系统能力:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消长时任务，固定取值为'continuousTaskCancel'。 |
| callback | Callback<ContinuousTaskCancelInfo> | 否 | 需要取消监听的回调函数，未传入则取消所有注册回调。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible cause: 1. Callback parameter error; 2. Unregister type has not register; 3. Parameter verification failed. |

**示例**：

```ets
import { backgroundTaskManager } from '@kit.BackgroundTasksKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';

function callback(info: backgroundTaskManager.ContinuousTaskCancelInfo) {
  console.info('continuousTaskCancel callback id ' + info.id);
  console.info('continuousTaskCancel callback reason ' + info.reason);
}

export default class EntryAbility extends UIAbility {
    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
        try {
            backgroundTaskManager.off("continuousTaskCancel", callback);
        } catch (error) {
            console.error(`Operation onContinuousTaskCancel failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}`);
        }
};
```

#### backgroundTaskManager.on('continuousTaskSuspend')20+

on(type: 'continuousTaskSuspend', callback: Callback<ContinuousTaskSuspendInfo>): void

注册长时任务暂停的监听，使用callback异步回调。注册该回调后，如果系统首次检测到应用未执行相应的业务，不会直接取消长时任务，而是将长时任务标记为暂停状态，如果连续检测失败，仍会取消长时任务。

长时任务处于暂停状态时，应用退后台会被挂起，回前台自动激活。

**需要权限:** ohos.permission.KEEP_BACKGROUND_RUNNING

**系统能力:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，固定取值为'continuousTaskSuspend'，表示长时任务暂停。 |
| callback | Callback<ContinuousTaskSuspendInfo> | 是 | 回调函数，返回长时任务暂停原因等信息。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[backgroundTaskManager错误码](backgroundTaskManager错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 9800005 | Continuous task verification failed. |

**示例**：

```ets
import { backgroundTaskManager } from '@kit.BackgroundTasksKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';

function callback(info: backgroundTaskManager.ContinuousTaskSuspendInfo) {
  console.info('continuousTaskSuspend callback continuousTaskId: ' + info.continuousTaskId);
  console.info('continuousTaskSuspend callback suspendState: ' + info.suspendState);
  console.info('continuousTaskSuspend callback suspendReason: ' + info.suspendReason);
}

export default class EntryAbility extends UIAbility {
    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
        try {
            backgroundTaskManager.on("continuousTaskSuspend", callback);
        } catch (error) {
            console.error(`Operation onContinuousTaskSuspend failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}`);
        }
};
```

#### backgroundTaskManager.off('continuousTaskSuspend')20+

off(type: 'continuousTaskSuspend', callback?: Callback<ContinuousTaskSuspendInfo>): void

取消长时任务暂停的监听，使用callback异步回调。

**需要权限:** ohos.permission.KEEP_BACKGROUND_RUNNING

**系统能力:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，固定取值为'continuousTaskSuspend'，表示长时任务暂停。 |
| callback | Callback<ContinuousTaskSuspendInfo> | 否 | 需要取消监听的回调函数，未传入则取消所有注册的暂停回调。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[backgroundTaskManager错误码](backgroundTaskManager错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 9800005 | Continuous task verification failed. |

**示例**：

```ets
import { backgroundTaskManager } from '@kit.BackgroundTasksKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';

function callback(info: backgroundTaskManager.ContinuousTaskSuspendInfo) {
  console.info('continuousTaskSuspend callback continuousTaskId: ' + info.continuousTaskId);
  console.info('continuousTaskSuspend callback suspendState: ' + info.suspendState);
  console.info('continuousTaskSuspend callback suspendReason: ' + info.suspendReason);
}

export default class EntryAbility extends UIAbility {
    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
        try {
            backgroundTaskManager.off("continuousTaskSuspend", callback);
        } catch (error) {
            console.error(`Operation offContinuousTaskSuspend failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}`);
        }
};
```

#### backgroundTaskManager.on('continuousTaskActive')20+

on(type: 'continuousTaskActive', callback: Callback<ContinuousTaskActiveInfo>): void

注册长时任务激活的监听，使用callback异步回调。应用回前台激活暂停的长时任务。

**需要权限:** ohos.permission.KEEP_BACKGROUND_RUNNING

**系统能力:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，固定取值为'continuousTaskActive'，表示长时任务激活。 |
| callback | Callback<ContinuousTaskActiveInfo> | 是 | 回调函数，返回长时任务激活相关信息。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[backgroundTaskManager错误码](backgroundTaskManager错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 9800005 | Continuous task verification failed. |

**示例**：

```ets
import { backgroundTaskManager } from '@kit.BackgroundTasksKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';

function callback(info: backgroundTaskManager.ContinuousTaskActiveInfo) {
  console.info('continuousTaskActive callback id: ' + info.id);
}

export default class EntryAbility extends UIAbility {
    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
        try {
            backgroundTaskManager.on("continuousTaskActive", callback);
        } catch (error) {
            console.error(`Operation onContinuousTaskActive failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}`);
        }
};
```

#### backgroundTaskManager.off('continuousTaskActive')20+

off(type: 'continuousTaskActive', callback?: Callback<ContinuousTaskActiveInfo>): void

取消长时任务激活的监听，使用callback异步回调。

**需要权限:** ohos.permission.KEEP_BACKGROUND_RUNNING

**系统能力:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，固定取值为'continuousTaskActive'，表示长时任务激活。 |
| callback | Callback<ContinuousTaskActiveInfo> | 否 | 需要取消监听的回调函数，未传入则取消所有注册的激活回调。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[backgroundTaskManager错误码](backgroundTaskManager错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 9800005 | Continuous task verification failed. |

**示例**：

```ets
import { backgroundTaskManager } from '@kit.BackgroundTasksKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';

function callback(info: backgroundTaskManager.ContinuousTaskActiveInfo) {
  console.info('continuousTaskActive callback id: ' + info.id);
}

export default class EntryAbility extends UIAbility {
    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
        try {
            backgroundTaskManager.off("continuousTaskActive", callback);
        } catch (error) {
            console.error(`Operation offContinuousTaskActive failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}`);
        }
};
```

#### backgroundTaskManager.startBackgroundRunning21+

startBackgroundRunning(context: Context, request: ContinuousTaskRequest): Promise<ContinuousTaskNotification>

申请长时任务，一个UIAbility（FA模型则为ServiceAbility）下支持通过本接口申请多个长时任务，使用Promise异步回调。通过本接口申请长时任务时，支持与已存在的长时任务合并通知，具体请参考[ContinuousTaskRequest](#ZH-CN_TOPIC_0000002553361127__continuoustaskrequest21)。

同一时间最多可存在10个长时任务，长时任务申请成功后，会有通知栏消息，没有提示音。

如果通过本接口申请的一个长时任务中同时包含多种类型，且包含数据传输类型，则在通知栏会发送2个长时任务通知，一个为数据传输类型，另一个为其他类型的合并通知。任意一个通知被移除时，长时任务取消，且另一个通知也会同步移除。接口返回的长时任务通知Id为数据传输类型的Id，主要用于数据传输的进度更新。

**需要权限:** ohos.permission.KEEP_BACKGROUND_RUNNING

**系统能力:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用运行的上下文。 |
| request | ContinuousTaskRequest | 是 | 长时任务请求信息，包括长时任务主类型、子类型等。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<ContinuousTaskNotification> | Promise对象，返回长时任务通知信息，包括长时任务ID等。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[backgroundTaskManager错误码](backgroundTaskManager错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 9800001 | Memory operation failed. |
| 9800004 | System service operation failed. |
| 9800005 | Continuous task verification failed. |
| 9800006 | Notification verification failed for a continuous task. |
| 9800007 | Continuous task storage failed. |

**示例**：

```ets
import { backgroundTaskManager } from '@kit.BackgroundTasksKit';
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { wantAgent, WantAgent } from '@kit.AbilityKit';

export default class EntryAbility extends UIAbility {
  notificationId: number = 0; // 保存通知id
  continuousTaskId: number | undefined = -1;
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    let wantAgentInfo: wantAgent.WantAgentInfo = {
      // 请开发者替换为实际被拉起应用的bundleName和abilityName
      wants: [
        {
          bundleName: "com.example.myapplication",
          abilityName: "EntryAbility"
        }
      ],
      // 设置点击通知后的动作类型
      actionType: wantAgent.OperationType.START_ABILITY,
      // 开发者自定义的请求码，用于标识将被执行的动作
      requestCode: 0,
      // 设置点击通知后的动作执行属性
      wantAgentFlags: [wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
    };

    try {
      // 通过wantAgent模块下getWantAgent方法获取WantAgent对象
      wantAgent.getWantAgent(wantAgentInfo).then((wantAgentObj: WantAgent) => {
        try {
          // 如果要合并通知，主类型和子类型都必须相同，combinedTaskNotification为true，continuousTaskId必须存在且合法
          // 申请主类型为MODE_LOCATION的长时任务
          let modeList: Array<number> = [backgroundTaskManager.BackgroundTaskMode.MODE_LOCATION];
          let subModeList: Array<number> = [backgroundTaskManager.BackgroundTaskSubmode.SUBMODE_NORMAL_NOTIFICATION];
          let continuousTaskRequest = new backgroundTaskManager.ContinuousTaskRequest();
          continuousTaskRequest.backgroundTaskModes =  modeList;
          continuousTaskRequest.backgroundTaskSubmodes = subModeList;
          continuousTaskRequest.wantAgent = wantAgentObj;
          continuousTaskRequest.combinedTaskNotification = false;
          continuousTaskRequest.continuousTaskId = this.continuousTaskId;
          backgroundTaskManager.startBackgroundRunning(this.context, continuousTaskRequest).then((res: backgroundTaskManager.ContinuousTaskNotification) => {
            console.info(`Operation startBackgroundRunning succeeded. notificationId is ${res.notificationId} continuousTaskId is ${res.continuousTaskId}`);
            this.notificationId = res.notificationId;
            this.continuousTaskId = res.continuousTaskId;
          }).catch((error: BusinessError) => {
            console.error(`Operation startBackgroundRunning failed. code is ${error.code} message is ${error.message}`);
          });
        } catch (error) {
          console.error(`Operation startBackgroundRunning failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}`);
        }
      });
    } catch (error) {
      console.error(`Operation getWantAgent failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}`);
    }
};
```

#### backgroundTaskManager.updateBackgroundRunning21+

updateBackgroundRunning(context: Context, request: ContinuousTaskRequest): Promise<ContinuousTaskNotification>

更新长时任务，使用Promise异步回调。长时任务更新成功后，会有通知栏消息，没有提示音。

更新长时任务还存在如下约束限制：

1. 本接口仅支持更新如下接口申请的长时任务：[startBackgroundRunning(context: Context, request: ContinuousTaskRequest): Promise<ContinuousTaskNotification>](#ZH-CN_TOPIC_0000002553361127__backgroundtaskmanagerstartbackgroundrunning21)。

1. 已经合并的长时任务，且后台任务主类型和子类型均相同，仅支持更新ContinuousTaskRequest.wantAgent中的wants信息（abilityName等），如果类型不同，更新失败。
1. 如果待更新的长时任务或指定的更新类型中包含数据传输类型，直接返回失败。

**需要权限:** ohos.permission.KEEP_BACKGROUND_RUNNING

**系统能力:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用运行的上下文。 |
| request | ContinuousTaskRequest | 是 | 长时任务请求信息, 包括待更新的长时任务ID等。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<ContinuousTaskNotification> | Promise对象，返回更新后的长时任务通知信息，包括长时任务ID等。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[backgroundTaskManager错误码](backgroundTaskManager错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 9800001 | Memory operation failed. |
| 9800004 | System service operation failed. |
| 9800005 | Continuous task verification failed. |
| 9800006 | Notification verification failed for a continuous task. |
| 9800007 | Continuous task storage failed. |

**示例**：

```ets
import { backgroundTaskManager } from '@kit.BackgroundTasksKit';
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { wantAgent, WantAgent } from '@kit.AbilityKit';

export default class EntryAbility extends UIAbility {
  notificationId: number = 0; // 保存通知id
  continuousTaskId: number | undefined = -1; //长时任务ID
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    let wantAgentInfo: wantAgent.WantAgentInfo = {
      // 添加需要被拉起应用的bundleName和abilityName, 请开发者替换为实际的bundleName和abilityName
      wants: [
        {
          bundleName: "com.example.myapplication",
          abilityName: "EntryAbility"
        }
      ],
      // 设置点击通知后的动作类型
      actionType: wantAgent.OperationType.START_ABILITY,
      // 开发者自定义的请求码，用于标识将被执行的动作
      requestCode: 0,
      // 设置点击通知后的动作执行属性
      wantAgentFlags: [wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
    };

    try {
      // 通过wantAgent模块下getWantAgent方法获取WantAgent对象
      wantAgent.getWantAgent(wantAgentInfo).then((wantAgentObj: WantAgent) => {
        try {
          // 必须先执行startBackgroundRunning，才能调用updateBackgroundRunning，请开发者提前申请长时任务
          let modeList: Array<number> = [backgroundTaskManager.BackgroundTaskMode.MODE_LOCATION];
          let subModeList: Array<number> = [backgroundTaskManager.BackgroundTaskSubmode.SUBMODE_NORMAL_NOTIFICATION];
          let continuousTaskRequest = new backgroundTaskManager.ContinuousTaskRequest();
          continuousTaskRequest.backgroundTaskModes =  modeList;
          continuousTaskRequest.backgroundTaskSubmodes = subModeList;
          continuousTaskRequest.wantAgent = wantAgentObj;
          continuousTaskRequest.combinedTaskNotification = false;
          continuousTaskRequest.continuousTaskId = this.continuousTaskId; //对于更新接口，长时任务ID必须要传且为存在的ID，否则更新失败
          backgroundTaskManager.updateBackgroundRunning(this.context, continuousTaskRequest).then((res: backgroundTaskManager.ContinuousTaskNotification) => {
            console.info("Operation updateBackgroundRunning succeeded");
            this.notificationId = res.notificationId;
          }).catch((error: BusinessError) => {
            console.error(`Operation updateBackgroundRunning failed. code is ${error.code} message is ${error.message}`);
          });
        } catch (error) {
          console.error(`Operation updateBackgroundRunning failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}`);
        }
      });
    } catch (error) {
      console.error(`Operation getWantAgent failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}`);
    }
};
```

#### backgroundTaskManager.stopBackgroundRunning21+

stopBackgroundRunning(context: Context, continuousTaskId: number): Promise<void>

取消指定Id的长时任务，使用Promise异步回调。也可以通过[stopBackgroundRunning](#ZH-CN_TOPIC_0000002553361127__backgroundtaskmanagerstopbackgroundrunning)取消当前UIAbility下所有长时任务。

**系统能力:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用运行的上下文。 |
| continuousTaskId | number | 是 | 长时任务ID。 说明：可以通过startBackgroundRunning接口的返回值获取当前申请的长时任务ID，或者通过getAllContinuousTasks接口获取所有长时任务信息。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码**：

以下错误码的详细介绍请参见[backgroundTaskManager错误码](backgroundTaskManager错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9800001 | Memory operation failed. |
| 9800004 | System service operation failed. |
| 9800005 | Continuous task verification failed. |
| 9800006 | Notification verification failed for a continuous task. |
| 9800007 | Continuous task storage failed. |

**示例**：

```ets
import { backgroundTaskManager } from '@kit.BackgroundTasksKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';

export default class EntryAbility extends UIAbility {
  continuousTaskId: number = 0;
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    try {
        backgroundTaskManager.stopBackgroundRunning(this.context, this.continuousTaskId).then(() => {
            console.info("Operation stopBackgroundRunning succeeded");
        }).catch((error: BusinessError) => {
            console.error(`Operation stopBackgroundRunning failed. code is ${error.code} message is ${error.message}`);
        });
    } catch (error) {
        console.error(`Operation stopBackgroundRunning failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}`);
    }
};
```

#### DelaySuspendInfo

短时任务信息。

**系统能力:** SystemCapability.ResourceSchedule.BackgroundTaskManager.TransientTask

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| requestId | number | 否 | 否 | 短时任务的请求ID。 |
| actualDelayTime | number | 否 | 否 | 应用实际申请的短时任务时间，单位：ms。 说明 ：申请时间最长为3分钟，低电量时最长为1分钟。 |

#### TransientTaskInfo20+

所有短时任务信息。

**系统能力**: SystemCapability.ResourceSchedule.BackgroundTaskManager.TransientTask

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| remainingQuota | number | 否 | 否 | 应用当日所剩余总配额，单位：ms。 |
| transientTasks | DelaySuspendInfo[] | 否 | 否 | 当前已申请的所有短时任务信息。 |

#### BackgroundMode

长时任务类型。

**系统能力:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DATA_TRANSFER | 1 | 数据传输。 使用场景举例：非托管形式的上传、下载，如在浏览器后台上传或下载数据。 说明： 在数据传输时，应用需要更新进度，如果进度长时间（超过10分钟）未更新，数据传输的长时任务会被取消。 更新进度的通知类型必须为实况窗，具体实现可参考startBackgroundRunning()中的示例。 |
| AUDIO_PLAYBACK | 2 | 音视频播放。 使用场景举例：音频、视频在后台播放，音视频投播。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 说明： 从API version 20开始，申请/更新AUDIO_PLAYBACK类型长时任务但不接入AVSession，申请/更新长时任务成功后会在通知栏显示通知。 接入AVSession后，后台任务模块不会发送通知栏通知，由AVSession发送通知。 对于API version 19及之前的版本，后台任务模块不会在通知栏显示通知。 |
| AUDIO_RECORDING | 3 | 录制。 使用场景举例：录音、录屏退后台。 |
| LOCATION | 4 | 定位导航。 |
| BLUETOOTH_INTERACTION | 5 | 蓝牙相关业务。 使用场景举例：通过蓝牙传输文件时退后台。 |
| MULTI_DEVICE_CONNECTION | 6 | 多设备互联。 使用场景举例：分布式业务连接、投播。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| VOIP13+ | 8 | 音视频通话。 使用场景举例：某些聊天类应用（具有音视频业务）音频、视频通话时退后台。 |
| TASK_KEEPING | 9 | 计算任务。 使用场景举例：杀毒软件。 说明： 从API version 21开始，对PC/2in1设备、非PC/2in1设备但申请了ACL权限为ohos.permission.KEEP_BACKGROUND_RUNNING_SYSTEM的应用开放。 API version 20及之前版本，仅对PC/2in1设备开放。 |

#### ContinuousTaskNotification12+

长时任务通知信息。

**系统能力:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| slotType | notificationManager.SlotType | 否 | 否 | 长时任务通知的渠道类型。 说明： 长时任务申请或更新成功后不支持提示音。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| contentType | notificationManager.ContentType | 否 | 否 | 长时任务通知的内容类型。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| notificationId | number | 否 | 否 | 长时任务通知 Id。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
continuousTaskId15+number否是长时任务 Id。

#### ContinuousTaskCancelInfo15+

长时任务取消信息。

**系统能力:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| reason | ContinuousTaskCancelReason | 否 | 否 | 长时任务取消原因。 |
| id | number | 否 | 否 | 被取消的长时任务 Id。 |

#### ContinuousTaskCancelReason15+

长时任务取消原因。

**系统能力:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

| 名称 | 值 | 说明 |
| --- | --- | --- |
| USER_CANCEL | 1 | 用户取消。 |
| SYSTEM_CANCEL | 2 | 系统取消。 |
| USER_CANCEL_REMOVE_NOTIFICATION | 3 | 用户移除通知。预留接口，暂未启用。 |
| SYSTEM_CANCEL_DATA_TRANSFER_LOW_SPEED | 4 | 申请DATA_TRANSFER类型长时任务，但是数据传输速率低。预留接口，暂未启用。 |
| SYSTEM_CANCEL_AUDIO_PLAYBACK_NOT_USE_AVSESSION | 5 | 申请AUDIO_PLAYBACK类型长时任务，但是未接入AVSession。预留接口，暂未启用。 |
| SYSTEM_CANCEL_AUDIO_PLAYBACK_NOT_RUNNING | 6 | 申请AUDIO_PLAYBACK类型长时任务，但是未播放音视频。预留接口，暂未启用。 |
| SYSTEM_CANCEL_AUDIO_RECORDING_NOT_RUNNING | 7 | 申请AUDIO_RECORDING类型长时任务，但是未录制。预留接口，暂未启用。 |
| SYSTEM_CANCEL_NOT_USE_LOCATION | 8 | 申请LOCATION类型长时任务，但是未使用定位导航。预留接口，暂未启用。 |
| SYSTEM_CANCEL_NOT_USE_BLUETOOTH | 9 | 申请BLUETOOTH_INTERACTION类型长时任务，但是未使用蓝牙相关业务。预留接口，暂未启用。 |
| SYSTEM_CANCEL_NOT_USE_MULTI_DEVICE | 10 | 申请MULTI_DEVICE_CONNECTION类型长时任务，但是未使用多设备互联。预留接口，暂未启用。 |
| SYSTEM_CANCEL_USE_ILLEGALLY | 11 | 使用非法类型的长时任务，如申请AUDIO_PLAYBACK类型长时任务，但是使用音视频播放及定位导航业务。预留接口，暂未启用。 |

#### BackgroundSubMode16+

长时任务子类型。

**系统能力:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CAR_KEY | 1 | 车钥匙。 说明： 1. 只有申请BLUETOOTH_INTERACTION类型的长时任务，车钥匙子类型才能生效。 2. 不支持通过updateBackgroundRunning接口更新为此类型长时任务。 |

#### BackgroundModeType16+

长时任务类型类别。

**系统能力:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SUB_MODE | 'subMode' | 子类型。 |

#### ContinuousTaskSuspendInfo20+

长时任务暂停信息。

**系统能力:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| continuousTaskId | number | 否 | 否 | 被暂停的长时任务 Id。 |
| suspendState | boolean | 否 | 否 | 长时任务状态，false表示激活，true表示暂停。 |
| suspendReason | ContinuousTaskSuspendReason | 否 | 否 | 长时任务暂停原因。 |

#### ContinuousTaskSuspendReason20+

长时任务暂停原因。

**系统能力:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SYSTEM_SUSPEND_DATA_TRANSFER_LOW_SPEED | 4 | 申请DATA_TRANSFER类型长时任务，但是数据传输速率低。 |
| SYSTEM_SUSPEND_AUDIO_PLAYBACK_NOT_USE_AVSESSION | 5 | 申请AUDIO_PLAYBACK类型长时任务，但是未接入AVSession。 |
| SYSTEM_SUSPEND_AUDIO_PLAYBACK_NOT_RUNNING | 6 | 申请AUDIO_PLAYBACK类型长时任务，但是未播放音视频。 |
| SYSTEM_SUSPEND_AUDIO_RECORDING_NOT_RUNNING | 7 | 申请AUDIO_RECORDING类型长时任务，但是未录制。 |
| SYSTEM_SUSPEND_LOCATION_NOT_USED | 8 | 申请LOCATION类型长时任务，但是未使用定位导航。 |
| SYSTEM_SUSPEND_BLUETOOTH_NOT_USED | 9 | 申请BLUETOOTH_INTERACTION类型长时任务，但是未使用蓝牙相关业务。 |
| SYSTEM_SUSPEND_MULTI_DEVICE_NOT_USED | 10 | 申请MULTI_DEVICE_CONNECTION类型长时任务，但是未使用多设备互联。 |
| SYSTEM_SUSPEND_USED_ILLEGALLY | 11 | 使用非法类型的长时任务，如申请AUDIO_PLAYBACK类型长时任务，但是使用音视频播放及定位导航业务。预留接口，暂未启用。 |
| SYSTEM_SUSPEND_SYSTEM_LOAD_WARNING | 12 | 系统高负载暂停长时任务。预留接口，暂未启用。 |

#### ContinuousTaskActiveInfo20+

长时任务激活信息。

**系统能力:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| id | number | 否 | 否 | 被激活的长时任务 Id。 |

#### ContinuousTaskInfo20+

长时任务信息。

**系统能力**: SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| abilityName | string | 否 | 否 | UIAbility名称。 |
| uid | number | 否 | 否 | 应用的UID。 |
| pid | number | 否 | 否 | 应用进程的PID。 |
| isFromWebView | boolean | 否 | 否 | 是否通过Webview方式申请，即通过系统代理应用申请长时任务。true表示通过Webview方式申请，false表示不通过Webview方式申请。 |
| backgroundModes | string[] | 否 | 否 | 长时任务类型。 |
| backgroundSubModes | string[] | 否 | 否 | 长时任务子类型。 |
| notificationId | number | 否 | 否 | 通知 Id。 |
| continuousTaskId | number | 否 | 否 | 长时任务ID。 |
| abilityId | number | 否 | 否 | UIAbility Id。 |
| wantAgentBundleName | string | 否 | 否 | WantAgent 配置的包名。WantAgent为通知参数，用于指定点击长时任务通知后跳转的界面，在申请长时任务时作为参数传入。 |
| wantAgentAbilityName | string | 否 | 否 | WantAgent 配置的ability名称。WantAgent为通知参数，用于指定点击长时任务通知后跳转的界面，在申请长时任务时作为参数传入。 |
| suspendState | boolean | 否 | 否 | 申请的长时任务是否处于暂停状态。true表示处于暂停状态，false表示处于激活状态。 |
| bundleName23+ | string | 否 | 是 | 应用包名。 |
| appIndex23+ | number | 否 | 是 | 应用分身ID。 |

#### ContinuousTaskRequest21+

通常作为[startBackgroundRunning()](#ZH-CN_TOPIC_0000002553361127__backgroundtaskmanagerstartbackgroundrunning21)和[updateBackgroundRunning](#ZH-CN_TOPIC_0000002553361127__backgroundtaskmanagerupdatebackgroundrunning21)接口的入参，用于指定申请或更新的长时任务信息。其中：

1. 通过[startBackgroundRunning()](#ZH-CN_TOPIC_0000002553361127__backgroundtaskmanagerstartbackgroundrunning21)接口申请长时任务时，如果待申请长时任务与当前应用下已存在长时任务，两者的主类型和子类型均相同，且combinedTaskNotification均取值为true，则会合并通知。否则不会合并通知。

1. 如果长时任务本身没有通知，则不会合并，长时任务类型是否会通知请参考[BackgroundTaskMode](#ZH-CN_TOPIC_0000002553361127__backgroundtaskmode21)。

1. 如果长时任务类型中包含数据传输类型，则不会合并通知。
1. 通知合并后不能取消合并，已合并的不能更新成不合并。
1. 通知合并后，点击通知栏消息，会跳转到第一个申请的长时任务对应的UIAbility，如果调用了更新接口，则跳转到最后一次更新的长时任务对应的UIAbility。

1. 通过[updateBackgroundRunning](#ZH-CN_TOPIC_0000002553361127__backgroundtaskmanagerupdatebackgroundrunning21)接口更新长时任务时，传入的continuousTaskId必须存在，否则更新失败。

1. 从API version 22开始支持[特殊场景类型的长时任务](#ZH-CN_TOPIC_0000002553361127__backgroundtaskmode21)。必须单独使用且不支持通知合并，即申请或更新长时任务时，长时任务类型只能有特殊场景类型，否则返回错误。

#### 属性

**系统能力:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| backgroundTaskModes | BackgroundTaskMode[] | 否 | 否 | 长时任务主类型。 说明： 主类型与子类型必须匹配。 |
| backgroundTaskSubmodes | BackgroundTaskSubmode[] | 否 | 否 | 长时任务子类型。 说明： 主类型与子类型必须匹配。 |
| wantAgent | WantAgent | 否 | 否 | 通知参数，用于指定点击长时任务通知后跳转的界面。 |
| combinedTaskNotification | boolean | 否 | 是 | 是否合并通知，true表示合并，false表示不合并，默认为false。 说明： 该属性在updateBackgroundRunning接口中不生效，如需在已有任务上合并通知，请重新申请该任务，并在申请时设置为支持合并。 |
| continuousTaskId | number | 否 | 是 | 长时任务ID，默认值为-1。 说明： 如果combinedTaskNotification取值为true，则该值为必填项，且必须是存在的ID。 作为updateBackgroundRunning接口入参时，该属性必填，且必须是存在的ID。 可以通过getAllContinuousTasks接口查看当前所有长时任务信息。 |

#### isModeSupported21+

isModeSupported(): boolean

查询当前[ContinuousTaskRequest](#ZH-CN_TOPIC_0000002553361127__continuoustaskrequest21)设置的长时任务主类型，是否支持申请长时任务。是否支持申请长时任务请参考[BackgroundTaskMode](#ZH-CN_TOPIC_0000002553361127__backgroundtaskmode21)的说明。

**需要权限:** ohos.permission.KEEP_BACKGROUND_RUNNING

**系统能力:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**返回值**：

| 类型 | 说明 |
| --- | --- |
| boolean | 返回长时任务主类型是否支持。true表示支持，false表示不支持。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[backgroundTaskManager错误码](backgroundTaskManager错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 9800005 | Continuous task verification failed. |

**示例**：

```ets
import { backgroundTaskManager } from '@kit.BackgroundTasksKit';
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    let isModeSupported: boolean = false;
    let continuousTaskRequest = new backgroundTaskManager.ContinuousTaskRequest();
    let modeList: Array<number> = [backgroundTaskManager.BackgroundTaskMode.MODE_TASK_KEEPING];
    continuousTaskRequest.backgroundTaskModes = modeList;
    try {
      isModeSupported = continuousTaskRequest.isModeSupported();
      console.info(`Operation isModeSupported succeeded. isModeSupported is ${isModeSupported}`);
    } catch (error) {
      console.error(`Operation startBackgroundRunning failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}`);
    }
};
```

#### requestAuthFromUser22+

requestAuthFromUser(context: Context, callback: Callback<UserAuthResult>): void

请求用户授权是否能在后台长时间运行，使用callback异步回调。接口调用成功会发送横幅通知，有提示音。仅适用于[特殊场景类型长时任务](#ZH-CN_TOPIC_0000002553361127__backgroundtaskmode21)。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.KEEP_BACKGROUND_RUNNING

**系统能力：** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**设备行为差异：** 该接口在Phone、Tablet、PC/2in1中可正常调用，在其他设备类型中返回9800005错误码。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用运行的上下文。 |
| callback | Callback<UserAuthResult> | 是 | 用户操作后，返回授权结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[backgroundTaskManager错误码](backgroundTaskManager错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 9800004 | System service operation failed. |
| 9800005 | Continuous task verification failed. |

**示例：**

```ets
import { backgroundTaskManager } from '@kit.BackgroundTasksKit';
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

function callbackAuth(authResult: backgroundTaskManager.UserAuthResult) {
    console.info('Operation requestAuthFromUser success. auth result: ' + JSON.stringify(authResult));
}

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    let continuousTaskRequest = new backgroundTaskManager.ContinuousTaskRequest();
    let modeList: Array<number> = [backgroundTaskManager.BackgroundTaskMode.MODE_SPECIAL_SCENARIO_PROCESSING];
    continuousTaskRequest.backgroundTaskModes = modeList;
    let subModeList: Array<number> = [backgroundTaskManager.BackgroundTaskSubmode.SUBMODE_MEDIA_PROCESS_NORMAL_NOTIFICATION];
    continuousTaskRequest.backgroundTaskSubmodes = subModeList;
    try {
      continuousTaskRequest.requestAuthFromUser(this.context, callbackAuth);
      console.info('Operation requestAuthFromUser succeeded.');
    } catch (error) {
      console.error(`Operation requestAuthFromUser failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}`);
    }
};
```

#### checkSpecialScenarioAuth22+

checkSpecialScenarioAuth(context: Context): Promise<UserAuthResult>

查询用户是否授权能在后台长时间运行。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.KEEP_BACKGROUND_RUNNING

**系统能力：** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**设备行为差异：** 该接口在Phone、Tablet、PC/2in1中可正常调用，在其他设备类型中返回9800005错误码。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用运行的上下文。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<UserAuthResult> | Promise对象，返回用户授权结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[backgroundTaskManager错误码](backgroundTaskManager错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 9800004 | System service operation failed. |
| 9800005 | Continuous task verification failed. |

**示例：**

```ets
import { backgroundTaskManager } from '@kit.BackgroundTasksKit';
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    try {
      let continuousTaskRequest = new backgroundTaskManager.ContinuousTaskRequest();
      continuousTaskRequest.checkSpecialScenarioAuth(this.context).then((res: backgroundTaskManager.UserAuthResult) => {
        console.info('Operation checkSpecialScenarioAuth succeeded. data: ' + JSON.stringify(res));
      }).catch((error: BusinessError) => {
        console.error(`Operation checkSpecialScenarioAuth failed. code is ${error.code} message is ${error.message}`);
      });
    } catch (error) {
      console.error(`Operation checkSpecialScenarioAuth failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}`);
    }
};
```

#### BackgroundTaskMode21+

长时任务主类型。通常与长时任务子类型[BackgroundTaskSubmode](#ZH-CN_TOPIC_0000002553361127__backgroundtasksubmode21)配合使用，对照关系请参考长时任务主类型与子类型对照表，两者共同作为API version 21新增的[申请](#ZH-CN_TOPIC_0000002553361127__backgroundtaskmanagerstartbackgroundrunning21)、[更新](#ZH-CN_TOPIC_0000002553361127__backgroundtaskmanagerupdatebackgroundrunning21)长时任务接口入参，用于指定长时任务类型。

**系统能力**: SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

| 名称 | 值 | 说明 |
| --- | --- | --- |
| MODE_DATA_TRANSFER | 1 | 数据传输。 使用场景举例：非托管形式的上传、下载，如在浏览器后台上传或下载数据。 说明： 1. 在数据传输时，应用需要更新进度，如果进度长时间（超过10分钟）未更新，数据传输的长时任务会被取消。 2. 更新进度的通知类型必须为实况窗，具体实现可参考startBackgroundRunning()中的示例。 |
| MODE_AUDIO_PLAYBACK | 2 | 音视频播放。 使用场景举例：音频、视频在后台播放，音视频投播。 说明： 申请/更新MODE_AUDIO_PLAYBACK类型长时任务但不接入AVSession，申请/更新长时任务成功后会在通知栏显示通知。接入AVSession后，后台任务模块不会发送通知栏通知，由AVSession发送通知。 |
| MODE_AUDIO_RECORDING | 3 | 录制。 使用场景举例：录音、录屏退后台。 |
| MODE_LOCATION | 4 | 定位导航。 |
| MODE_BLUETOOTH_INTERACTION | 5 | 蓝牙相关业务。 使用场景举例：通过蓝牙传输文件时退后台。 |
| MODE_MULTI_DEVICE_CONNECTION | 6 | 多设备互联。 使用场景举例：分布式业务连接、投播。 |
| MODE_VOIP | 8 | 音视频通话。 使用场景举例：某些聊天类应用（具有音视频业务）音频、视频通话时退后台。 |
| MODE_TASK_KEEPING | 9 | 计算任务。 使用场景举例：杀毒软件。 说明： 仅对PC/2in1设备开放，或者非PC/2in1设备但申请了ACL权限为ohos.permission.KEEP_BACKGROUND_RUNNING_SYSTEM的应用开放。 |
| MODE_AV_PLAYBACK_AND_RECORD22+ | 12 | 多媒体相关业务。 使用场景举例：音视频播放、录制、音视频通话场景，场景需与长时任务子类型相匹配。在上述场景下，选择此类型或者对应的长时任务主类型均可。例如：音视频播放场景可以申请MODE_AUDIO_PLAYBACK或者MODE_AV_PLAYBACK_AND_RECORD长时任务主类型。 |
| MODE_SPECIAL_SCENARIO_PROCESSING22+ | 13 | 特殊场景类型（仅对Phone、Tablet、PC/2in1设备开放）。 使用场景举例：应用在后台导出媒体文件导出、应用使用三方投播组件在后台进行投播，场景需与长时任务子类型相匹配。 说明： 1. 如果应用需要在后台长时间运行，可以通过requestAuthFromUser接口请求用户授权、通过checkSpecialScenarioAuth接口查询用户授权结果。 2. 仅对申请ACL权限ohos.permission.KEEP_BACKGROUND_RUNNING_SYSTEM的应用开放。 3. 必须单独使用且不支持通知合并，即申请或更新长时任务时，长时任务类型只能有特殊场景类型，否则返回错误。 |

#### BackgroundTaskSubmode21+

长时任务子类型。通常与长时任务主类型[BackgroundTaskMode](#ZH-CN_TOPIC_0000002553361127__backgroundtaskmode21)配合使用，对照关系请参考长时任务主类型与子类型对照表，两者共同作为API version 21新增的申请、更新长时任务接口入参，用于指定长时任务类型。

**系统能力**: SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SUBMODE_CAR_KEY_NORMAL_NOTIFICATION | 1 | 车钥匙类型，通知类型为普通文本通知。 |
| SUBMODE_NORMAL_NOTIFICATION | 2 | 普通文本通知。 |
| SUBMODE_LIVE_VIEW_NOTIFICATION | 3 | 实况窗通知。 |
| SUBMODE_AUDIO_PLAYBACK_NORMAL_NOTIFICATION22+ | 4 | 音视频播放，通知类型为普通文本通知。根据实际场景选择是否接入AVSession。 |
| SUBMODE_AVSESSION_AUDIO_PLAYBACK22+ | 5 | 已接入AVSession的音视频播放场景，通知类型为普通文本类型。 |
| SUBMODE_AUDIO_RECORD_NORMAL_NOTIFICATION22+ | 6 | 录音，通知类型为普通文本通知。 |
| SUBMODE_SCREEN_RECORD_NORMAL_NOTIFICATION22+ | 7 | 录屏，通知类型为普通文本通知。 |
| SUBMODE_VOICE_CHAT_NORMAL_NOTIFICATION22+ | 8 | 通话，通知类型为普通文本通知。 |
| SUBMODE_MEDIA_PROCESS_NORMAL_NOTIFICATION22+ | 9 | 媒体处理，例如：应用在后台导出媒体文件，通知类型为普通文本通知。 |
| SUBMODE_VIDEO_BROADCAST_NORMAL_NOTIFICATION22+ | 10 | 视频投播，例如：应用使用三方投播组件在后台进行投播，通知类型为普通文本通知。 |
| SUBMODE_WORK_OUT_NORMAL_NOTIFICATION23+ | 11 | 运动，例如：应用在后台有室内跑步场景，通知类型为普通文本通知。 模型约束： 此接口仅可在Stage模型下使用。 |

**长时任务主类型与子类型对照表：**

| 长时任务主类型 | 长时任务子类型 |
| --- | --- |
| MODE_DATA_TRANSFER | SUBMODE_LIVE_VIEW_NOTIFICATION |
| MODE_AUDIO_PLAYBACK | SUBMODE_NORMAL_NOTIFICATION |
| MODE_AUDIO_RECORDING | SUBMODE_NORMAL_NOTIFICATION |
| MODE_LOCATION | SUBMODE_NORMAL_NOTIFICATION |
| MODE_BLUETOOTH_INTERACTION | SUBMODE_NORMAL_NOTIFICATION SUBMODE_CAR_KEY_NORMAL_NOTIFICATION |
| MODE_MULTI_DEVICE_CONNECTION | SUBMODE_NORMAL_NOTIFICATION |
| MODE_VOIP | SUBMODE_NORMAL_NOTIFICATION |
| MODE_TASK_KEEPING | SUBMODE_NORMAL_NOTIFICATION |
| MODE_AV_PLAYBACK_AND_RECORD22+ | SUBMODE_AUDIO_PLAYBACK_NORMAL_NOTIFICATION22+ SUBMODE_AVSESSION_AUDIO_PLAYBACK22+ SUBMODE_AUDIO_RECORD_NORMAL_NOTIFICATION22+ SUBMODE_SCREEN_RECORD_NORMAL_NOTIFICATION22+ SUBMODE_VOICE_CHAT_NORMAL_NOTIFICATION22+ |
| MODE_SPECIAL_SCENARIO_PROCESSING22+ | SUBMODE_MEDIA_PROCESS_NORMAL_NOTIFICATION22+ SUBMODE_VIDEO_BROADCAST_NORMAL_NOTIFICATION22+ SUBMODE_WORK_OUT_NORMAL_NOTIFICATION23+ |

#### UserAuthResult22+

用户授权结果。

**系统能力：** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NOT_SUPPORTED | 0 | 不支持。例如：申请的长时任务主类型非MODE_SPECIAL_SCENARIO_PROCESSING时，不支持申请用户授权是否能在后台长时间运行。 |
| NOT_DETERMINED | 1 | 用户未操作。 |
| DENIED | 2 | 拒绝。 |
| GRANTED_ONCE | 3 | 本次允许。 说明： 在应用退出时该授权记录会被清除。 |
| GRANTED_ALWAYS | 4 | 始终允许。 说明： 当接收到以下公共事件时，相关授权记录将被清除： [COMMON_EVENT_PACKAGE_ADDED](../../topics/misc/系统定义的公共事件.md#ZH-CN_TOPIC_0000002497605510__common_event_package_added)、[COMMON_EVENT_PACKAGE_REMOVED](../../topics/misc/系统定义的公共事件.md#ZH-CN_TOPIC_0000002497605510__common_event_package_removed)、[COMMON_EVENT_BUNDLE_REMOVED](../../topics/misc/系统定义的公共事件.md#ZH-CN_TOPIC_0000002497605510__common_event_package_removed)、[COMMON_EVENT_PACKAGE_FULLY_REMOVED](../../topics/misc/系统定义的公共事件.md#ZH-CN_TOPIC_0000002497605510__common_event_package_fully_removed)、[COMMON_EVENT_PACKAGE_CHANGED](../../topics/misc/系统定义的公共事件.md#ZH-CN_TOPIC_0000002497605510__common_event_package_changed)。 |