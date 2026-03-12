# HiCollie_SetTimerParam

```ets
typedef struct HiCollie_SetTimerParam {...} HiCollie_SetTimerParam
```

#### 概述

定义OH_HiCollie_SetTimer函数的输入参数。

**起始版本：** 18

**相关模块：**[HiCollie](HiCollie.md)

**所在头文件：**[hicollie.h](hicollie.h.md)

#### 汇总

#### 成员变量

名称描述const char *nametimer任务名称。unsigned int timeout任务超时时间阈值，单位s。[OH_HiCollie_Callback](hicollie.h.md#ZH-CN_TOPIC_0000002497605670__oh_hicollie_callback) func超时发生时执行的回调函数。void *arg回调函数的参数。[HiCollie_Flag](hicollie.h.md#ZH-CN_TOPIC_0000002497605670__hicollie_flag) flag超时发生时执行的动作，参考[HiCollie_Flag](hicollie.h.md#ZH-CN_TOPIC_0000002497605670__hicollie_flag)。