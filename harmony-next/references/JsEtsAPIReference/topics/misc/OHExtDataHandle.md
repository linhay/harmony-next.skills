# OHExtDataHandle

```ets
typedef struct OHExtDataHandle {...} OHExtDataHandle
```

#### 概述

扩展数据句柄结构体定义。

**起始版本：** 9

**废弃版本：** 从API version 10开始废弃，不再提供替代接口。

**相关模块：**[NativeWindow](NativeWindow.md)

**所在头文件：**[external_window.h](../../capi/headers/external_window.h.md)

#### 汇总

#### 成员变量

名称描述int32_t fd句柄 Fd，-1代表不支持。uint32_t reserveIntsReserve数组的个数。int32_t reserve[0]Reserve数组。