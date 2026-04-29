# HMS_GCP_PickedColorInfo

**概述**

定义取色颜色信息的结构体。

系统能力： SystemCapability.Stylus.ColorPicker

起始版本： 5.0.0(12)

相关模块： [GlobalColorPicker](GlobalColorPicker.md)

所在头文件： [native_gcp_api.h](native_gcp_api.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| HMS_GCP_Color color | 提取的颜色值。 |
| HMS_GCP_ColorSpace colorSpace | 颜色所属的颜色空间。 |
| int64_t timestamp | 提取颜色的时间戳。 |

**结构体成员变量说明**

**color**

```ets
HMS_GCP_Color HMS_GCP_PickedColorInfo::color
```

描述

提取的颜色值。

**colorSpace**

```ets
HMS_GCP_ColorSpace HMS_GCP_PickedColorInfo::colorSpace
```

描述

颜色所属的颜色空间。

**timestamp**

```ets
int64_t HMS_GCP_PickedColorInfo::timestamp
```

描述

提取颜色的时间戳。