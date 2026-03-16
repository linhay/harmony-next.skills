# Vibrator_FileDescription

```ets
typedef struct Vibrator_FileDescription { ... } Vibrator_FileDescription
```

#### 概述

振动文件描述。

**起始版本：** 11

**相关模块：**[Vibrator](Vibrator.md)

**所在头文件：**[vibrator_type.h](../../capi/headers/vibrator_type.h.md)

#### 汇总

#### 成员变量

名称描述int32_t fd自定义振动序列的文件句柄。int64_t offset自定义振动序列的偏移地址。int64_t length自定义振动序列的总长度。