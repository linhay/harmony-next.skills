# Usb_DeviceArray

```ets
typedef struct Usb_DeviceArray {...} Usb_DeviceArray
```

#### 概述

设备ID清单，用于存放OH_Usb_GetDevices接口获取到的设备ID列表和设备数量。

**起始版本：** 18

**相关模块：**[UsbDDK](../misc/UsbDDK.md)

**所在头文件：**[usb_ddk_types.h](../../capi/headers/usb_ddk_types.h.md)

#### 汇总

#### 成员变量

名称描述uint64_t* deviceIds开发者申请好的设备数组首地址，申请的大小不超过128个设备ID。uint32_t num实际返回的设备数量，根据数量遍历deviceIds获得设备ID。当该值为0时，表示不存在USB设备。