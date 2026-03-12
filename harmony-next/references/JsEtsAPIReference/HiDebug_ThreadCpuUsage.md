# HiDebug_ThreadCpuUsage

```ets
typedef struct HiDebug_ThreadCpuUsage {...} HiDebug_ThreadCpuUsage
```

#### 概述

应用程序所有线程的CPU使用率结构体定义。

**起始版本：** 12

**相关模块：**[HiDebug](HiDebug.md)

**所在头文件：**[hidebug_type.h](hidebug_type.h.md)

#### 汇总

#### 成员变量

名称描述uint32_t threadId线程ID。double cpuUsage线程CPU使用率百分比。struct [HiDebug_ThreadCpuUsage](HiDebug_ThreadCpuUsage.md) *next下一个线程的使用率信息。