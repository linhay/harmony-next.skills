# UsbInterfaceDescriptor

```ets
typedef struct UsbInterfaceDescriptor {...} __attribute__((packed)) UsbInterfaceDescriptor
```

#### 概述

标准接口描述符，对应USB协议中Standard Interface Descriptor。

**起始版本：** 10

**相关模块：**[UsbDDK](UsbDDK.md)

**所在头文件：**[usb_ddk_types.h](usb_ddk_types.h.md)

#### 汇总

#### 成员变量

名称描述uint8_t bLength该描述符的大小，单位为字节。uint8_t bDescriptorType描述符类型。uint8_t bInterfaceNumber接口编号。uint8_t bAlternateSetting用来选择该接口的备用配置的值。uint8_t bNumEndpoints该接口所使用的端点数量（不包括端点零）。uint8_t bInterfaceClass由USB标准化组织（USB-IF）分配的设备类代码。uint8_t bInterfaceSubClass由USB标准化组织（USB-IF）分配的子类代码，其值由{@link bInterfaceClass}的值限定。uint8_t bInterfaceProtocol由USB标准化组织（USB-IF）分配的协议代码，其值由{@link bInterfaceClass}和{@link bInterfaceSubClass}的值限定。uint8_t iInterface描述该接口的字符串描述符的索引。