# Hid_Device

```ets
typedef struct Hid_Device {...} Hid_Device
```

#### 概述

设备基本信息。

**起始版本：** 11

**相关模块：**[HidDdk](HidDdk.md)

**所在头文件：**[hid_ddk_types.h](hid_ddk_types.h.md)

#### 汇总

#### 成员变量

名称描述const char* deviceName设备名称uint16_t vendorId厂商IDuint16_t productId产品IDuint16_t version版本号uint16_t bustype总线类型Hid_DeviceProp* properties设备特性uint16_t propLength设备特性数量