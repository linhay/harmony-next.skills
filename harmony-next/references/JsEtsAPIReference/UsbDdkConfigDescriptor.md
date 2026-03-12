# UsbDdkConfigDescriptor

```ets
typedef struct UsbDdkConfigDescriptor {...} UsbDdkConfigDescriptor
```

#### 概述

配置描述符。

**起始版本：** 10

**相关模块：**[UsbDDK](UsbDDK.md)

**所在头文件：**[usb_ddk_types.h](usb_ddk_types.h.md)

#### 汇总

#### 成员变量

名称描述struct UsbConfigDescriptor configDescriptor标准配置描述符。struct UsbDdkInterface* interface该配置所包含的接口。const uint8_t* extra未做解析的描述符，包含特定于类或供应商的描述符。uint32_t extraLength未做解析的描述符长度。