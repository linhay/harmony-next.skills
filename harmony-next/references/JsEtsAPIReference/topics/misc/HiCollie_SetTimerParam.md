# HiCollie_SetTimerParam

```ets
typedef struct HiCollie_SetTimerParam {...} HiCollie_SetTimerParam
```

**概述**

定义OH_HiCollie_SetTimer函数的输入参数。

起始版本： 18

相关模块： [HiCollie](HiCollie.md)

所在头文件： [hicollie.h](hicollie.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| const char *name | timer任务名称。 |
| unsigned int timeout | 任务超时时间阈值，单位：s。 |
| OH_HiCollie_Callback func | 超时发生时执行的回调函数。 |
| void *arg | 回调函数的参数。 |
| HiCollie_Flag flag | 超时发生时执行的动作，参考HiCollie_Flag。 |