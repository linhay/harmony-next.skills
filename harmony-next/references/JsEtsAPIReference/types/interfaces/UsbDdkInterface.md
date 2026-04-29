# UsbDdkInterface

```ets
typedef struct UsbDdkInterface {...} UsbDdkInterface
```

**概述**

USB接口，是特定接口下备用设置的集合。

起始版本： 10

相关模块： [UsbDdk](UsbDdk.md)

所在头文件： [usb_ddk_types.h](usb_ddk_types.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| uint8_t numAltsetting | 接口的备用设置数量。 |
| struct UsbDdkInterfaceDescriptor* altsetting | 接口的备用设置。 |