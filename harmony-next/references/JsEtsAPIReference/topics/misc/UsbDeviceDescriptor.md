# UsbDeviceDescriptor

```ets
typedef struct UsbDeviceDescriptor {...} __attribute__((aligned(8))) UsbDeviceDescriptor
```

**概述**

标准设备描述符，对应USB协议中Standard Device Descriptor。

起始版本： 10

相关模块： [UsbDdk](UsbDdk.md)

所在头文件： [usb_ddk_types.h](usb_ddk_types.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| uint8_t bLength | 该描述符的大小，单位为字节。 |
| uint8_t bDescriptorType | 描述符类型。 |
| uint16_t bcdUSB | USB协议发布号。 |
| uint8_t bDeviceClass | 由USB标准化组织（USB-IF）分配的设备类代码。 |
| uint8_t bDeviceSubClass | 由USB标准化组织（USB-IF）分配的子类代码，其值由bDeviceClass的值限定。 |
| uint8_t bDeviceProtocol | 由USB标准化组织（USB-IF）分配的协议代码，其值由bDeviceClass和bDeviceSubClass的值限定。 |
| uint8_t bMaxPacketSize0 | 端点零的最大包大小，只有8，16，32，64是合法的。 |
| uint16_t idVendor | 由USB标准化组织（USB-IF）分配的厂商编号。 |
| uint16_t idProduct | 由厂商分配的产品编号。 |
| uint16_t bcdDevice | 设备发布编号。 |
| uint8_t iManufacturer | 描述厂商的字符串描述符的索引。 |
| uint8_t iProduct | 描述产品的字符串描述符的索引。 |
| uint8_t iSerialNumber | 描述设备序列号的字符串描述符的索引。 |
| uint8_t bNumConfigurations | 配置数量。 |