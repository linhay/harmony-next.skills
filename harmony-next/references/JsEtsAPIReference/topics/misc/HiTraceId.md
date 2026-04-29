# HiTraceId

```ets
typedef struct HiTraceId {...} HiTraceId
```

**概述**

HiTraceId定义。

起始版本： 12

相关模块： [HiTrace](HiTrace.md)

所在头文件： [trace.h](trace.h.md)

**汇总**

**成员变量**

如果字节序为小端模式，结构体顺序如下表所示：

| 字段 | 字段bit数 | 描述 |
| --- | --- | --- |
| uint64_t valid | 1 | HiTraceId是否有效。 |
| uint64_t ver | 3 | HiTraceId的版本号。 |
| uint64_t chainId | 60 | HiTraceId的跟踪链标识。 |
| uint64_t flags | 12 | HiTraceId的跟踪标志位。 |
| uint64_t spanId | 26 | HiTraceId的分支标识。 |
| uint64_t parentSpanId | 26 | HiTraceId的父分支标识。 |

如果字节序为大端模式，结构体顺序如下表所示：

| 字段 | 字段bit数 | 描述 |
| --- | --- | --- |
| uint64_t chainId | 60 | HiTraceId的跟踪链标识。 |
| uint64_t ver | 3 | HiTraceId的版本号。 |
| uint64_t valid | 1 | HiTraceId是否有效。 |
| uint64_t parentSpanId | 26 | HiTraceId的父分支标识。 |
| uint64_t spanId | 26 | HiTraceId的分支标识。 |
| uint64_t flags | 12 | HiTraceId的跟踪标志位。 |