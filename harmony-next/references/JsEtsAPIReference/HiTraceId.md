# HiTraceId

```ets
typedef struct HiTraceId {...} HiTraceId
```

#### 概述

HiTraceId定义。

**起始版本：** 12

**相关模块：**[Hitrace](HiTrace.md)

**所在头文件：**[trace.h](trace.h.md)

#### 汇总

#### 成员变量

如果字节序为小端模式，结构体顺序如下表所示：

字段字段bit数描述uint64_t valid1HiTraceId是否有效。uint64_t ver3HiTraceId的版本号。uint64_t chainId60HiTraceId的跟踪链标识。uint64_t flags12HiTraceId的跟踪标志位。uint64_t spanId26HiTraceId的分支标识。uint64_t parentSpanId26HiTraceId的父分支标识。

如果字节序为大端模式，结构体顺序如下表所示：

字段字段bit数描述uint64_t chainId60HiTraceId的跟踪链标识。uint64_t ver3HiTraceId的版本号。uint64_t valid1HiTraceId是否有效。uint64_t parentSpanId26HiTraceId的父分支标识。uint64_t spanId26HiTraceId的分支标识。uint64_t flags12HiTraceId的跟踪标志位。