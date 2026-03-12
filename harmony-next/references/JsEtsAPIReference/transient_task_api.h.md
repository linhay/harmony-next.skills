# transient_task_api.h

#### 概述

提供短时任务申请、查询、取消功能。

**引用文件：** <transient_task/transient_task_api.h>

**库：** libtransient_task.so

**系统能力：** SystemCapability.ResourceSchedule.BackgroundTaskManager.TransientTask

**起始版本：** 13

**相关模块：**[TransientTask](TransientTask.md)

#### 汇总

#### 函数

名称描述[int32_t OH_BackgroundTaskManager_RequestSuspendDelay(const char* reason,TransientTask_Callback callback, TransientTask_DelaySuspendInfo *info)](#ZH-CN_TOPIC_0000002529285239__oh_backgroundtaskmanager_requestsuspenddelay)申请短时任务。[int32_t OH_BackgroundTaskManager_GetRemainingDelayTime(int32_t requestId, int32_t *delayTime)](#ZH-CN_TOPIC_0000002529285239__oh_backgroundtaskmanager_getremainingdelaytime)获取本次短时任务的剩余时间。[int32_t OH_BackgroundTaskManager_CancelSuspendDelay(int32_t requestId)](#ZH-CN_TOPIC_0000002529285239__oh_backgroundtaskmanager_cancelsuspenddelay)取消短时任务。[int32_t OH_BackgroundTaskManager_GetTransientTaskInfo(TransientTask_TransientTaskInfo *transientTaskInfo)](#ZH-CN_TOPIC_0000002529285239__oh_backgroundtaskmanager_gettransienttaskinfo)获取所有短时任务信息，如当日剩余总配额等。

#### 函数说明

#### OH_BackgroundTaskManager_RequestSuspendDelay()

```ets
int32_t OH_BackgroundTaskManager_RequestSuspendDelay(const char* reason,TransientTask_Callback callback, TransientTask_DelaySuspendInfo *info)
```

**描述**

申请短时任务。

**系统能力：** SystemCapability.ResourceSchedule.BackgroundTaskManager.TransientTask

**起始版本：** 13

**参数：**

参数项描述const char* reason申请短时任务的原因。[TransientTask_Callback](transient_task_type.h.md#ZH-CN_TOPIC_0000002529445213__transienttask_callback) callback短时任务即将超时的回调，一般在超时前6秒，通过此回调通知应用。[TransientTask_DelaySuspendInfo](TransientTask_DelaySuspendInfo.md) *info返回短时任务信息。

**返回：**

类型说明int32_t

返回0，表示申请成功。

 返回401，表示入参错误。

 返回9800002，表示Parcel读写操作失败。

 返回9800003，表示IPC通信失败。

 返回9800004，表示系统服务失败。

 返回9900001，表示短时任务客户端信息校验失败。

 返回9900002，表示短时任务服务端校验失败。

 错误码的具体信息请参考[TransientTask_ErrorCode](transient_task_type.h.md#ZH-CN_TOPIC_0000002529445213__transienttask_errorcode)。

#### OH_BackgroundTaskManager_GetRemainingDelayTime()

```ets
int32_t OH_BackgroundTaskManager_GetRemainingDelayTime(int32_t requestId, int32_t *delayTime)
```

**描述**

获取本次短时任务的剩余时间。

**系统能力：** SystemCapability.ResourceSchedule.BackgroundTaskManager.TransientTask

**起始版本：** 13

**参数：**

参数项描述int32_t requestId短时任务的请求ID。int32_t *delayTime短时任务的剩余时间。

**返回：**

类型说明int32_t

返回0，表示查询成功。

 返回401，表示入参错误。

 返回9800002，表示Parcel读写操作失败。

 返回9800003，表示IPC通信失败。

 返回9800004，表示系统服务失败。

 返回9900001，表示短时任务客户端信息校验失败。

 返回9900002，表示短时任务服务端校验失败。

 错误码的具体信息请参考[TransientTask_ErrorCode](transient_task_type.h.md#ZH-CN_TOPIC_0000002529445213__transienttask_errorcode)。

#### OH_BackgroundTaskManager_CancelSuspendDelay()

```ets
int32_t OH_BackgroundTaskManager_CancelSuspendDelay(int32_t requestId)
```

**描述**

取消短时任务。

**系统能力：** SystemCapability.ResourceSchedule.BackgroundTaskManager.TransientTask

**起始版本：** 13

**参数：**

参数项描述int32_t requestId短时任务的请求ID。

**返回：**

类型说明int32_t

返回0，表示取消成功。

 返回401，表示入参错误。

 返回9800002，表示Parcel读写操作失败。

 返回9800003，表示IPC通信失败。

 返回9800004，表示系统服务失败。

 返回9900001，表示短时任务客户端信息校验失败。

 返回9900002，表示短时任务服务端校验失败。

 错误码的具体信息请参考[TransientTask_ErrorCode](transient_task_type.h.md#ZH-CN_TOPIC_0000002529445213__transienttask_errorcode)。

#### OH_BackgroundTaskManager_GetTransientTaskInfo()

```ets
int32_t OH_BackgroundTaskManager_GetTransientTaskInfo(TransientTask_TransientTaskInfo  *transientTaskInfo)
```

**描述**

获取所有短时任务信息，如当日剩余总配额等。

**起始版本：** 20

**参数：**

参数项描述[TransientTask_TransientTaskInfo ](TransientTask_TransientTaskInfo.md) *transientTaskInfo所有短时任务信息，具体请参考[TransientTask_TransientTaskInfo](TransientTask_TransientTaskInfo.md)。

**返回：**

类型说明int32_t

返回0，表示获取成功。

 返回9900001，表示短时任务客户端信息校验失败。

 返回9900003，表示Parcel读写操作失败。

 返回9900004，表示系统服务失败。

 错误码的具体信息请参考[TransientTask_ErrorCode](transient_task_type.h.md#ZH-CN_TOPIC_0000002529445213__transienttask_errorcode)。