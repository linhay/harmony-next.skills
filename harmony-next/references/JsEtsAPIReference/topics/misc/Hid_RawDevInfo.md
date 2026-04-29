# Hid_RawDevInfo

```ets
typedef struct Hid_RawDevInfo {...} Hid_RawDevInfo
```

#### 概述

原始设备信息定义。

**起始版本：** 18

**相关模块：**[HidDdk](HidDdk.md)

所在头文件： [hid_ddk_types.h](hid_ddk_types.h.md)

#### 汇总

#### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint32_t busType | 总线类型 |
| uint16_t vendor | 供应商ID |
| uint16_t product | 产品ID |