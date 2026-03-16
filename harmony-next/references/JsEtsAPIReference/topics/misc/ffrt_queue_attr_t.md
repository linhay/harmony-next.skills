# ffrt_queue_attr_t

```ets
typedef struct {...} ffrt_queue_attr_t
```

#### 概述

串行队列属性结构。

**起始版本：** 10

**相关模块：**[FFRT](FFRT.md)

**所在头文件：**[type_def.h](../../capi/headers/type_def.h.md)

#### 汇总

#### 成员变量

名称描述uint32_t storage[(ffrt_queue_attr_storage_size + sizeof(uint32_t) - 1) / sizeof(uint32_t)]串行队列属性所占空间