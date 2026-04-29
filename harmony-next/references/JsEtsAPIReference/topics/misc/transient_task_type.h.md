# transient_task_type.h

**概述**

定义短时任务的错误码和结构体。

引用文件： <transient_task/transient_task_type.h>

库： libtransient_task.so

系统能力： SystemCapability.ResourceSchedule.BackgroundTaskManager.TransientTask

起始版本： 11

相关模块： [TransientTask](TransientTask.md)

**汇总**

**结构体**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| TransientTask_DelaySuspendInfo | TransientTask_DelaySuspendInfo | 定义短时任务返回信息结构体。 |
| TransientTask_TransientTaskInfo | TransientTask_TransientTaskInfo | 定义所有短时任务信息结构体。 |

**宏定义**

| 名称 | 描述 |
| --- | --- |
| TRANSIENT_TASK_MAX_NUM 3 | 同一时刻最大短时任务数量。 起始版本： 20 |

**枚举**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| TransientTask_ErrorCode | TransientTask_ErrorCode | 定义短时任务错误码。 |

**函数**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| typedef void (*TransientTask_Callback)(void) | TransientTask_Callback | 定义短时任务超时回调类型。 |

**枚举类型说明**

**TransientTask_ErrorCode**

```ets
enum TransientTask_ErrorCode
```

描述

定义短时任务错误码。

起始版本： 13

| 枚举项 | 描述 |
| --- | --- |
| ERR_TRANSIENT_TASK_OK = 0 | 成功。 |
| ERR_TRANSIENT_TASK_INVALID_PARAM = 401 | 参数检查失败。可能原因：1.必选参数没有传入。2.参数类型错误。 |
| ERR_TRANSIENT_TASK_PARCEL_FAILED = 9800002 | Parcel读写操作失败。 |
| ERR_TRANSIENT_TASK_TRANSACTION_FAILED = 9800003 | IPC通信失败。 |
| ERR_TRANSIENT_TASK_SYS_NOT_READY = 9800004 | 系统服务失败。 |
| ERR_TRANSIENT_TASK_CLIENT_INFO_VERIFICATION_FAILED = 9900001 | 短时任务客户端信息校验失败。 |
| ERR_TRANSIENT_TASK_SERVICE_VERIFICATION_FAILED = 9900002 | 短时任务服务端校验失败。 |
| ERR_TRANSIENT_TASK_PARCELABLE_FAILED = 9900003 | 短时任务Parcel读写操作失败。可能原因：1.参数非法。2.申请内存失败。 |
| ERR_TRANSIENT_TASK_SERVICE_NOT_READY = 9900004 | 短时任务系统服务失败。 |

**函数说明**

**TransientTask_Callback()**

```ets
typedef void (*TransientTask_Callback)(void)
```

描述

定义短时任务超时回调类型。

起始版本： 13