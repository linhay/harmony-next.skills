# FG_IntegrationInfo

#### 概述

此结构体描述超帧集成的信息。包括显示模式，是否需要额外缓存深度和颜色纹理，以及是否需要翻转颜色纹理。仅在[FG_PredictionMode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002522242234__fg_predictionmode-1)为FG_PREDICTION_MODE_INTERPOLATION时生效。

**起始版本**：5.1.0(18)

相关模块： [GraphicsAccelerate](GraphicsAccelerate.md)

所在头文件： [frame_generation_base.h](frame_generation_base.h.md)

#### 汇总

#### 成员变量

| 名称 | 描述 |
| --- | --- |
| [FG_PresentMode](GraphicsAccelerate.md#section11881356193212) presentMode | 预测帧展示模式。取值为FG_PRESENT_BY_SYSTEM时，仅在[FG_PredictionMode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga79e55783a2a38873fc6890c297885275)为FG_PREDICTION_MODE_INTERPOLATION时生效。 |
| bool textureCachedByGame | 深度纹理和颜色纹理是否被游戏单独缓存来用于超帧。缓存情况下算法将直接使用不再额外缓存。取值为True时，仅在[FG_PredictionMode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gaea2169cd5ae4bf9e8a17dc58f33e8766)为FG_PREDICTION_MODE_INTERPOLATION时生效。 取值范围：[true, false]。 |
| bool needFlipInputColor | 输入的颜色纹理是否需要翻转。需要翻转情况下，算法映射Y轴坐标读取颜色纹理。取值为True时，仅在[FG_PredictionMode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gaea2169cd5ae4bf9e8a17dc58f33e8766)为FG_PREDICTION_MODE_INTERPOLATION时生效。 取值范围：[true, false]。 |
| bool needFlipOutputColor | 预测帧是否需要翻转。需要翻转情况下，算法映射Y轴坐标进行翻转输出。取值为True时，仅在[FG_PredictionMode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gaea2169cd5ae4bf9e8a17dc58f33e8766)为FG_PREDICTION_MODE_INTERPOLATION时生效。 取值范围：[true, false]。 |

#### 结构体成员变量说明

#### presentMode

```ets
[FG_PresentMode](GraphicsAccelerate.md#section131101213459) FG_IntegrationInfo::presentMode
```

**描述**

展示模式。

#### textureCachedByGame

```ets
bool FG_IntegrationInfo::textureCachedByGame
```

**描述**

深度纹理和颜色纹理是否被游戏单独缓存来用于超帧。缓存情况下算法将直接使用不再额外缓存。取值为True时，仅在[FG_PredictionMode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002522242234__fg_predictionmode-1)为FG_PREDICTION_MODE_INTERPOLATION生效。

#### needFlipInputColor

```ets
bool FG_IntegrationInfo::needFlipInputColor
```

**描述**

输入的颜色纹理是否需要翻转。需要翻转情况下，算法映射Y轴坐标读取颜色纹理。取值为True时，仅在[FG_PredictionMode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002522242234__fg_predictionmode-1)为FG_PREDICTION_MODE_INTERPOLATION生效。

#### needFlipOutputColor

```ets
bool FG_IntegrationInfo::needFlipOutputColor
```

**描述**

预测帧是否需要翻转。需要翻转情况下，算法映射Y轴坐标进行翻转输出。取值为True时，仅在[FG_PredictionMode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002522242234__fg_predictionmode-1)为FG_PREDICTION_MODE_INTERPOLATION生效。
