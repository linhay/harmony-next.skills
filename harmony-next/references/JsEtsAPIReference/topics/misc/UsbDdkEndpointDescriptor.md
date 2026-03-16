# UsbDdkEndpointDescriptor

```ets
typedef struct UsbDdkEndpointDescriptor {...} UsbDdkEndpointDescriptor
```

#### 概述

端点描述符。

**起始版本：** 10

**相关模块：**[UsbDDK](UsbDDK.md)

**所在头文件：**[usb_ddk_types.h](../../capi/headers/usb_ddk_types.h.md)

#### 汇总

#### 成员变量

名称描述struct UsbEndpointDescriptor endpointDescriptor标准端点描述符。const uint8_t* extra未做解析的描述符，包含特定于类或供应商的描述符。uint32_t extraLength未做解析的描述符长度。