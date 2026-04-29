# HiDebug_NativeMemInfo

```ets
typedef struct HiDebug_NativeMemInfo {...} HiDebug_NativeMemInfo
```

#### 概述

应用程序进程本机内存信息结构类型定义。

**起始版本：** 12

**相关模块：**[HiDebug](HiDebug.md)

所在头文件： [hidebug_type.h](hidebug_type.h.md)

#### 汇总

#### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint32_t pss | 进程比例集大小内存，以KB为单位。 |
| uint32_t vss | 虚拟内存大小，以KB为单位。 |
| uint32_t rss | 常驻集大小，以KB为单位。 |
| uint32_t sharedDirty | 共享脏内存的大小，以KB为单位。 |
| uint32_t privateDirty | 专用脏内存的大小，以KB为单位。 |
| uint32_t sharedClean | 共享干净内存的大小，以KB为单位。 |
| uint32_t privateClean | 专用干净内存的大小，以KB为单位。 |