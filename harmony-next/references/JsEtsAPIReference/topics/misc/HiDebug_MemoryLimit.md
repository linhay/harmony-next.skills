# HiDebug_MemoryLimit

```ets
typedef struct HiDebug_MemoryLimit {...} HiDebug_MemoryLimit
```

#### 概述

应用程序进程内存限制结构类型定义。

**起始版本：** 12

**相关模块：**[HiDebug](HiDebug.md)

**所在头文件：**[hidebug_type.h](../../capi/headers/hidebug_type.h.md)

#### 汇总

#### 成员变量

名称描述uint64_t rssLimit应用程序进程驻留集的限制，以KB为单位。uint64_t vssLimit应用程序进程的虚拟内存限制，以KB为单位。