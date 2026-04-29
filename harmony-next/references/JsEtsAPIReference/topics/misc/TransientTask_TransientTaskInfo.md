# TransientTask_TransientTaskInfo

```ets
typedef struct TransientTask_TransientTaskInfo {...} TransientTask_TransientTaskInfo
```

**概述**

定义所有短时任务信息结构体。

起始版本： 20

相关模块： [TransientTask](TransientTask.md)

所在头文件： [transient_task_type.h](transient_task_type.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| int32_t remainingQuota | 当日剩余总配额。单位：毫秒。 |
| TransientTask_DelaySuspendInfo transientTasks[TRANSIENT_TASK_MAX_NUM] | 已申请的所有短时任务信息。包括短时任务请求ID、剩余时间（单位：毫秒）。 |