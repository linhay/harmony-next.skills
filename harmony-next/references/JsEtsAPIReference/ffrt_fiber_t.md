# ffrt_fiber_t

```ets
typedef struct {...} ffrt_fiber_t
```

#### 概述

纤程结构。

**起始版本：** 20

**相关模块：**[FFRT](FFRT.md)

**所在头文件：**[type_def.h](type_def.h.md)

#### 汇总

#### 成员变量

名称描述uintptr_t storage[ffrt_fiber_storage_size]纤程上下文所占空间。