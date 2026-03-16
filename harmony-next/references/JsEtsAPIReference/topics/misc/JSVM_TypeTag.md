# JSVM_TypeTag

```ets
typedef struct {...} JSVM_TypeTag
```

#### 概述

类型标记，存储为两个无符号64位整数的128位值。作为一个UUID，通过它，JavaScript对象可以是"tagged"，以确保它们的类型保持不变。

**起始版本：** 11

**相关模块：**[JSVM](JSVM.md)

**所在头文件：**[jsvm_types.h](../../capi/headers/jsvm_types.h.md)

#### 汇总

#### 成员变量

名称描述uint64_t lower低64位uint64_t upper高64位