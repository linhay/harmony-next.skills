# UsbRequestPipe

```ets
typedef struct UsbRequestPipe {...} __attribute__((aligned(8))) UsbRequestPipe
```

#### 概述

请求管道。

**起始版本：** 10

**相关模块：**[UsbDDK](UsbDDK.md)

**所在头文件：**[usb_ddk_types.h](../../capi/headers/usb_ddk_types.h.md)

#### 汇总

#### 成员变量

名称描述uint64_t interfaceHandle接口操作句柄。uint8_t endpoint要通信的端点的地址。uint32_t timeout超时时间，单位是毫秒。