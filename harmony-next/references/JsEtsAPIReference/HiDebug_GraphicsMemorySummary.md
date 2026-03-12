# HiDebug_GraphicsMemorySummary

```ets
typedef struct HiDebug_GraphicsMemorySummary {...} HiDebug_GraphicsMemorySummary
```

#### 概述

应用图形显存占用详情的结构定义。

**起始版本：** 21

**相关模块：**[HiDebug](HiDebug.md)

**所在头文件：**[hidebug_type.h](hidebug_type.h.md)

#### 汇总

#### 成员变量

名称描述uint32_t glgl内存大小，RenderService渲染进程加载所需资源占用的内存，例如图片、纹理等，以KB为单位。uint32_t graphgraph内存大小，进程统计的DMA内存占用，包括直接通过接口申请的DMA buffer和通过allocator_host申请的DMA buffer，以KB为单位。