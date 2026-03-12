# HMS_GCP_PickedColorInfo

#### 概述

定义取色颜色信息的结构体。

**系统能力：** SystemCapability.Stylus.ColorPicker

**起始版本：** 5.0.0(12)

**相关模块：**[GlobalColorPicker](GlobalColorPicker.md)

#### 汇总

#### 成员变量

名称

描述

[HMS_GCP_Color](HMS_GCP_Color.md) color

提取的颜色值。

[HMS_GCP_ColorSpace](GlobalColorPicker.md#ZH-CN_TOPIC_0000002344611090__gafad683a86359c6a71ae84f54338e9e28) colorSpace

颜色所属的颜色空间。

int64_t [timestamp](#ZH-CN_TOPIC_0000002378569069__af1b1674d2f73f350bb47d0f9d97a3664)

提取颜色的时间戳。

#### 结构体成员变量说明

#### color

```ets
[HMS_GCP_Color](HMS_GCP_Color.md) HMS_GCP_PickedColorInfo::color
```

**描述**

提取的颜色值。

#### colorSpace

```ets
[HMS_GCP_ColorSpace](GlobalColorPicker.md#ZH-CN_TOPIC_0000002344611090__gafad683a86359c6a71ae84f54338e9e28) HMS_GCP_PickedColorInfo::colorSpace
```

**描述**

颜色所属的颜色空间。

#### timestamp

```ets
int64_t HMS_GCP_PickedColorInfo::timestamp
```

**描述**

提取颜色的时间戳。