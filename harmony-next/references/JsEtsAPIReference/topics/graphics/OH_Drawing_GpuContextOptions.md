# OH_Drawing_GpuContextOptions

```ets
typedef struct {...} OH_Drawing_GpuContextOptions
```

#### 概述

定义有关图形处理器上下文的选项。

**起始版本：** 12

**废弃版本：** 18

**相关模块：**[Drawing](Drawing.md)

**所在头文件：**[drawing_gpu_context.h](../../capi/headers/drawing_gpu_context.h.md)

#### 汇总

#### 成员变量

名称描述bool allowPathMaskCaching用于控制是否启用路径蒙版缓存，如果为true，则允许缓存路径蒙版纹理，如果为false，则不允许。