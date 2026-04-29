# HiDebug_MemoryLimit

```ets
typedef struct HiDebug_MemoryLimit {...} HiDebug_MemoryLimit
```

#### 概述

应用程序进程内存限制结构类型定义。

**起始版本：** 12

**相关模块：**[HiDebug](HiDebug.md)

所在头文件： [hidebug_type.h](hidebug_type.h.md)

#### 汇总

#### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint64_t rssLimit | 应用程序进程可用的物理内存限制，以KB为单位，实际当前系统未对进程可用物理内存做限制，但是进程的可用物理内存仍然不会超过设备的实际最大可用物理内存，当前设备的物理内存使用情况可通过OH_HiDebug_GetSystemMemInfo获取。 |
| uint64_t vssLimit | 应用程序进程的虚拟内存限制，以KB为单位。 |