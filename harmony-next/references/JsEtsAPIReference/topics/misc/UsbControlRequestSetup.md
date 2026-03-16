# UsbControlRequestSetup

```ets
typedef struct UsbControlRequestSetup {...} __attribute__((aligned(8))) UsbControlRequestSetup
```

#### 概述

控制传输setup包，对应USB协议中的Setup Data。

**起始版本：** 10

**相关模块：**[UsbDDK](UsbDDK.md)

**所在头文件：**[usb_ddk_types.h](../../capi/headers/usb_ddk_types.h.md)

#### 汇总

#### 成员变量

名称描述uint8_t bmRequestType请求类型。uint8_t bRequest具体的请求。uint16_t wValue具体的请求不同，其代表的含义不一样。uint16_t wIndex具体的请求不同，其代表的含义不一样，通常用来传递索引或者偏移量。uint16_t wLength如果有数据阶段的传输，其代表传输的字节个数。