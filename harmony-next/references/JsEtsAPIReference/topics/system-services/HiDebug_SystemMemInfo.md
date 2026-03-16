# HiDebug_SystemMemInfo

```ets
typedef struct HiDebug_SystemMemInfo {...} HiDebug_SystemMemInfo
```

#### 概述

系统内存信息结构类型定义。

**起始版本：** 12

**相关模块：**[HiDebug](../misc/HiDebug.md)

**所在头文件：**[hidebug_type.h](../../capi/headers/hidebug_type.h.md)

#### 汇总

#### 成员变量

名称描述uint32_t totalMem系统总的内存，以KB为单位。uint32_t freeMem系统空闲的内存，以KB为单位。uint32_t availableMem系统可用的内存，以KB为单位。