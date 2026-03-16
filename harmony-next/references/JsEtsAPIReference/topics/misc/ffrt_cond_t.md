# ffrt_cond_t

```ets
typedef struct {...} ffrt_cond_t
```

#### 概述

FFRT条件变量结构。

**起始版本：** 10

**相关模块：**[FFRT](FFRT.md)

**所在头文件：**[type_def.h](../../capi/headers/type_def.h.md)

#### 汇总

#### 成员变量

名称描述uint32_t storage[(ffrt_cond_storage_size + sizeof(uint32_t) - 1) / sizeof(uint32_t)]FFRT条件变量所占空间