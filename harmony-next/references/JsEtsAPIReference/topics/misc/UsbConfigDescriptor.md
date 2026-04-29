# UsbConfigDescriptor

```ets
typedef struct UsbConfigDescriptor {...} __attribute__((packed)) UsbConfigDescriptor
```

#### 概述

标准配置描述符，对应USB协议中Standard Configuration Descriptor。

**起始版本：** 10

相关模块： [UsbDdk](UsbDdk.md)

所在头文件： [usb_ddk_types.h](usb_ddk_types.h.md)

#### 汇总

#### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint8_t bLength | 该描述符的大小，单位为字节。 |
| uint8_t bDescriptorType | 描述符类型。 |
| uint16_t wTotalLength | 该配置描述符的总长度，包含配置、接口、端点和特定于类或供应商的描述符。 |
| uint8_t bNumInterfaces | 该配置所支持的接口数量。 |
| uint8_t bConfigurationValue | 设置配置所需要的参数，用来选择当前配置。 |
| uint8_t iConfiguration | 描述该配置的字符串描述符的索引。 |
| uint8_t bmAttributes | 配置属性，包含供电模式，远程唤醒等配置。 |
| uint8_t bMaxPower | 总线供电的USB设备的最大功耗，以2mA为单位。 |