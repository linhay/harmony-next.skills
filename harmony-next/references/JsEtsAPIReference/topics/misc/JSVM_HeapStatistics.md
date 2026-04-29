# JSVM_HeapStatistics

```ets
typedef struct {...} JSVM_HeapStatistics
```

#### 概述

用于保存有关JavaScript堆内存使用情况的统计信息。

**起始版本：** 12

**相关模块：**[JSVM](JSVM.md)

所在头文件： [jsvm_types.h](jsvm_types.h.md)

#### 汇总

#### 成员变量

| 名称 | 描述 |
| --- | --- |
| size_t totalHeapSize | 总堆大小，单位kb。 |
| size_t totalHeapSizeExecutable | 可执行堆的总大小，单位kb。 |
| size_t totalPhysicalSize | 总的物理内存大小，单位kb。 |
| size_t totalAvailableSize | 总的可用内存大小，单位kb。 |
| size_t usedHeapSize | 已使用的堆大小，单位kb。 |
| size_t heapSizeLimit | 堆大小限制，单位kb。 |
| size_t mallocedMemory | 已分配内存的大小，单位kb。 |
| size_t externalMemory | 外部内存大小，单位kb。 |
| size_t peakMallocedMemory | 最大可分配内存的大小，单位kb。 |
| size_t numberOfNativeContexts | 表示当前活跃的native上下文的数量，该数值一直增加可能指示存在内存泄漏。 |
| size_t numberOfDetachedContexts | 表示已经脱离的上下文数量。 |
| size_t totalGlobalHandlesSize | 全局Handle的总大小，单位kb。 |
| size_t usedGlobalHandlesSize | 已经使用的全局Handle的大小，单位kb。 |