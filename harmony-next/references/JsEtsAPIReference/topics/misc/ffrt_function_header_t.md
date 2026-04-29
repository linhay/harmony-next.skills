# ffrt_function_header_t

```ets
typedef struct {...} ffrt_function_header_t
```

#### 概述

任务执行体。

**起始版本：** 10

**相关模块：**[FFRT](FFRT.md)

所在头文件： [type_def.h](type_def.h.md)

#### 汇总

#### 成员变量

| 名称 | 描述 |
| --- | --- |
| [ffrt_function_t](type_def.h.md#ZH-CN_TOPIC_0000002497605556__ffrt_function_t) exec | 任务执行函数 |
| [ffrt_function_t](type_def.h.md#ZH-CN_TOPIC_0000002497605556__ffrt_function_t) destroy | 任务销毁函数 |
| uint64_t reserve[2] | 保留位需要设置为0 |
