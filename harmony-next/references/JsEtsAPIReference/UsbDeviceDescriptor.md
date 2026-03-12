# UsbDeviceDescriptor

```ets
typedef struct UsbDeviceDescriptor {...} __attribute__((aligned(8))) UsbDeviceDescriptor
```

#### 概述

标准设备描述符，对应USB协议中Standard Device Descriptor。

**起始版本：** 10

**相关模块：**[UsbDDK](UsbDDK.md)

**所在头文件：**[usb_ddk_types.h](usb_ddk_types.h.md)

#### 汇总

#### 成员变量

名称描述uint8_t bLength该描述符的大小，单位为字节。uint8_t bDescriptorType描述符类型。uint16_t bcdUSBUSB协议发布号。uint8_t bDeviceClass由USB标准化组织（USB-IF）分配的设备类代码。uint8_t bDeviceSubClass由USB标准化组织（USB-IF）分配的子类代码，其值由{@link bDeviceClass}的值限定。uint8_t bDeviceProtocol由USB标准化组织（USB-IF）分配的协议代码，其值由{@link bDeviceClass}和{@link bDeviceSubClass}的值限定。uint8_t bMaxPacketSize0端点零的最大包大小，只有8，16，32，64是合法的。uint16_t idVendor由USB标准化组织（USB-IF）分配的厂商编号。uint16_t idProduct由厂商分配的产品编号。uint16_t bcdDevice设备发布编号。uint8_t iManufacturer描述厂商的字符串描述符的索引。uint8_t iProduct描述产品的字符串描述符的索引。uint8_t iSerialNumber描述设备序列号的字符串描述符的索引。uint8_t bNumConfigurations配置数量。