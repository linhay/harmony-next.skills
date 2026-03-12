# XEG_TemporalUpscaleDescription

#### 概述

此结构体描述下发时域AI超分渲染命令时的输入信息。

**起始版本：** 5.0.0(12)

**相关模块：**[XEngine](XEngine.md)

#### 汇总

#### 成员变量

名称

描述

VkImageView [inputImage](#ZH-CN_TOPIC_0000002362157641__inputimage)

输入图像。

VkImageView [depthImage](#ZH-CN_TOPIC_0000002362157641__depthimage)

深度图像。

VkImageView [motionVectorImage](#ZH-CN_TOPIC_0000002362157641__motionvectorimage)

运动矢量图像。运动矢量的计算方式为当前渲染像素的NDC坐标的XY值减去上一帧的NDC坐标的XY值。图像格式需要是VK_FORMAT_R16G16_SFLOAT或更高精度。

VkImageView [dynamicMaskImage](#ZH-CN_TOPIC_0000002362157641__dynamicmaskimage)

物体的动态遮罩图像，格式需要是VK_FORMAT_R8_UNORM或其兼容格式。R通道的合法值为0.0，0.2或1.0，其中0.0表示静态物体，0.2表示运动物体如人物，1.0表示特效或半透明物体。

VkImageView [outputImage](#ZH-CN_TOPIC_0000002362157641__outputimage)

输出图像。

float [jitterX](#ZH-CN_TOPIC_0000002362157641__jitterx)

相机在X方向上的抖动。

float [jitterY](#ZH-CN_TOPIC_0000002362157641__jittery)

相机在Y方向上的抖动。

bool [resetHistory](#ZH-CN_TOPIC_0000002362157641__resethistory)

是否重置历史帧数据，true表示重置，false表示不重置。在历史帧未使用超分，当前帧开始使用超分的情况下建议设置为true。

float [steadyLevel](#ZH-CN_TOPIC_0000002362157641__steadylevel)

画面偏向当前帧（鬼影少但可能存在闪烁）还是历史帧（鬼影多但是更稳定）的平衡程度。取值范围为[0.0, 1.0]，值越大越偏向历史帧。

#### 结构体成员变量说明

#### depthImage

```ets
VkImageView XEG_TemporalUpscaleDescription::depthImage
```

**描述**

深度图像。

#### dynamicMaskImage

```ets
VkImageView XEG_TemporalUpscaleDescription::dynamicMaskImage
```

**描述**

物体的动态遮罩图像，格式需要是VK_FORMAT_R8_UNORM或其兼容格式。R通道的合法值为0.0，0.2或1.0，其中0.0表示静态物体，0.2表示运动物体如人物，1.0表示特效或半透明物体。

#### inputImage

```ets
VkImageView XEG_TemporalUpscaleDescription::inputImage
```

**描述**

输入图像。

#### jitterX

```ets
float XEG_TemporalUpscaleDescription::jitterX
```

**描述**

相机在X方向上的抖动。

#### jitterY

```ets
float XEG_TemporalUpscaleDescription::jitterY
```

**描述**

相机在Y方向上的抖动。

#### motionVectorImage

```ets
VkImageView XEG_TemporalUpscaleDescription::motionVectorImage
```

**描述**

运动矢量图像。运动矢量的计算方式为当前渲染像素的NDC坐标的XY值减去上一帧的NDC坐标的XY值。图像格式需要是VK_FORMAT_R16G16_SFLOAT或更高精度。

#### outputImage

```ets
VkImageView XEG_TemporalUpscaleDescription::outputImage
```

**描述**

输出图像。

#### resetHistory

```ets
bool XEG_TemporalUpscaleDescription::resetHistory
```

**描述**

是否重置历史帧数据，true表示重置，false表示不重置。在历史帧未使用超分，当前帧开始使用超分的情况下建议设置为true。

#### steadyLevel

```ets
float XEG_TemporalUpscaleDescription::steadyLevel
```

**描述**

画面偏向当前帧（鬼影少但可能存在闪烁）还是历史帧（鬼影多但是更稳定）的平衡程度。取值范围为[0.0, 1.0]，值越大越偏向历史帧。