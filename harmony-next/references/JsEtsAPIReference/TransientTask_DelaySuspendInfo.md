# TransientTask_DelaySuspendInfo

```ets
typedef struct TransientTask_DelaySuspendInfo {...} TransientTask_DelaySuspendInfo
```

#### 概述

定义短时任务返回信息结构体。

**起始版本：** 13

**相关模块：**[TransientTask](TransientTask.md)

**所在头文件：**[transient_task_type.h](transient_task_type.h.md)

#### 汇总

#### 成员变量

名称描述int32_t requestId短时任务请求ID。int32_t actualDelayTime剩余时间（单位：毫秒）。