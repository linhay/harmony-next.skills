# native_gcp_api.h

#### 概述

声明用于对外提供全局取色能力。

**库：** libcolorpicker_ndk.z.so

**系统能力：** SystemCapability.Stylus.ColorPicker

**起始版本：** 5.0.0(12)

**相关模块：**[GlobalColorPicker](../../topics/components/GlobalColorPicker.md)

#### 汇总

#### 结构体

名称

描述

struct [HMS_GCP_Color](../../topics/graphics/HMS_GCP_Color.md)

定义颜色值的结构体。

struct [HMS_GCP_PickedColorInfo](../../topics/graphics/HMS_GCP_PickedColorInfo.md)

定义取色的颜色信息的结构体。

#### 类型定义

名称

描述

typedef void(* [HMS_GCP_OnResult](../../topics/components/GlobalColorPicker.md#ZH-CN_TOPIC_0000002344611090__gac06acd25757a5a72f4f8d0aec5821a52)) (void *userData, [HMS_GCP_PickedColorInfo](../../topics/graphics/HMS_GCP_PickedColorInfo.md) colorInfo, const int32_t code)

此回调用于接收拾取的颜色结果。

#### 枚举

名称

描述

[HMS_GCP_ColorSpace](../../topics/components/GlobalColorPicker.md#ZH-CN_TOPIC_0000002344611090__gafad683a86359c6a71ae84f54338e9e28) {

HMS_GCP_UNKNOWN = 0,

HMS_GCP_ADOBE_RGB_1998 = 1,

HMS_GCP_DCI_P3 = 2,

HMS_GCP_DISPLAY_P3 = 3,

HMS_GCP_SRGB = 4,

HMS_GCP_BT709 = 6,

HMS_GCP_BT601_EBU = 7,

HMS_GCP_BT601_SMPTE_C = 8,

HMS_GCP_BT2020_HLG = 9,

HMS_GCP_BT2020_PQ = 10,

HMS_GCP_P3_HLG = 11,

HMS_GCP_P3_PQ = 12,

HMS_GCP_ADOBE_RGB_1998_LIMIT = 13,

HMS_GCP_DISPLAY_P3_LIMIT = 14,

HMS_GCP_SRGB_LIMIT = 15,

HMS_GCP_BT709_LIMIT = 16,

HMS_GCP_BT601_EBU_LIMIT = 17,

HMS_GCP_BT601_SMPTE_C_LIMIT = 18,

HMS_GCP_BT2020_HLG_LIMIT = 19,

HMS_GCP_BT2020_PQ_LIMIT = 20,

HMS_GCP_P3_HLG_LIMIT = 21,

HMS_GCP_P3_PQ_LIMIT = 22,

HMS_GCP_LINEAR_P3 = 23,

HMS_GCP_LINEAR_SRGB = 24,

HMS_GCP_LINEAR_BT2020 = 25,

CUSTOM = 5

}

颜色空间枚举。

#### 函数

名称

描述

int32_t [HMS_GCP_StartColorPicker](../../topics/components/GlobalColorPicker.md#ZH-CN_TOPIC_0000002344611090__ga4c202f3df255013b9920f26027065176) (int32_t initialPosX, int32_t initialPosY, [HMS_GCP_OnResult](../../topics/components/GlobalColorPicker.md#ZH-CN_TOPIC_0000002344611090__gac06acd25757a5a72f4f8d0aec5821a52) onResultCallback, void *userData)

启动全局取色器。

int32_t [HMS_GCP_StartColorPickerWithColorValue](../../topics/components/GlobalColorPicker.md#ZH-CN_TOPIC_0000002344611090__ga8b044a1cfcd3b6eb8461e70c66d2c578) (int32_t initialPosX, int32_t initialPosY, [HMS_GCP_OnResult](../../topics/components/GlobalColorPicker.md#ZH-CN_TOPIC_0000002344611090__gac06acd25757a5a72f4f8d0aec5821a52) onResultCallback, void *userData)

启动全局取色器。