# ffrt_rwlock_t

```ets
typedef struct {...} ffrt_rwlock_t
```

#### 概述

FFRT读写锁结构。

**起始版本：** 18

**相关模块：**[FFRT](FFRT.md)

**所在头文件：**[type_def.h](type_def.h.md)

#### 汇总

#### 成员变量

名称描述uint32_t storage[(ffrt_rwlock_storage_size + sizeof(uint32_t) - 1) / sizeof(uint32_t)]FFRT读写锁所占空间