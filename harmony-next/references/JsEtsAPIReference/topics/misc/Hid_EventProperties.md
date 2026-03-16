# Hid_EventProperties

```ets
typedef struct Hid_EventProperties {...} Hid_EventProperties
```

#### 概述

设备关注事件属性。

**起始版本：** 11

**相关模块：**[HidDdk](HidDdk.md)

**所在头文件：**[hid_ddk_types.h](../../capi/headers/hid_ddk_types.h.md)

#### 汇总

#### 成员变量

名称描述struct Hid_EventTypeArray hidEventTypes事件类型属性编码数组struct Hid_KeyCodeArray hidKeys键值属性编码数组struct Hid_AbsAxesArray hidAbs绝对坐标属性编码数组struct Hid_RelAxesArray hidRelBits相对坐标属性编码数组struct Hid_MscEventArray hidMiscellaneous其它特殊事件属性编码数组int32_t hidAbsMax[64]绝对坐标属性最大值int32_t hidAbsMin[64]绝对坐标属性最小值int32_t hidAbsFuzz[64]绝对坐标属性模糊值int32_t hidAbsFlat[64]绝对坐标属性固定值