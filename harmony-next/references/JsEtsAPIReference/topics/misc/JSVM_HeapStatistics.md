# JSVM_HeapStatistics

```ets
typedef struct {...} JSVM_HeapStatistics
```

#### 概述

用于保存有关JavaScript堆内存使用情况的统计信息。

**起始版本：** 12

**相关模块：**[JSVM](JSVM.md)

**所在头文件：**[jsvm_types.h](../../capi/headers/jsvm_types.h.md)

#### 汇总

#### 成员变量

名称描述size_t totalHeapSize总堆大小，单位kb。size_t totalHeapSizeExecutable可执行堆的总大小，单位kb。size_t totalPhysicalSize总的物理内存大小，单位kb。size_t totalAvailableSize总的可用内存大小，单位kb。size_t usedHeapSize已使用的堆大小，单位kb。size_t heapSizeLimit堆大小限制，单位kb。size_t mallocedMemory已分配内存的大小，单位kb。size_t externalMemory外部内存大小，单位kb。size_t peakMallocedMemory最大可分配内存的大小，单位kb。size_t numberOfNativeContexts表示当前活跃的native上下文的数量，该数值一直增加可能指示存在内存泄漏。size_t numberOfDetachedContexts表示已经脱离的上下文数量。size_t totalGlobalHandlesSize全局Handle的总大小，单位kb。size_t usedGlobalHandlesSize已经使用的全局Handle的大小，单位kb。