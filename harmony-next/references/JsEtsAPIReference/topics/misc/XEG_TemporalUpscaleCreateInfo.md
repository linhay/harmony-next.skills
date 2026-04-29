# [XEG_TemporalUpscale](XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_temporalupscale)CreateInfo

#### 概述

此结构体描述创建[XEG_TemporalUpscale](XEngine.md#ZH-CN_TOPIC_0000002553202223__xeg_temporalupscale)对象的信息。当结构体中的信息变化时，需要创建新的[XEG_TemporalUpscale](XEngine.md#ZH-CN_TOPIC_0000002553202223__xeg_temporalupscale)对象。

**起始版本：** 5.0.0(12)

**相关模块： **[XEngine](XEngine.md)

所在头文件： [xeg_vulkan_temporal_upscale.h](xeg_vulkan_temporal_upscale.h.md)

#### 汇总

#### 成员变量

| 名称 | 描述 |
| --- | --- |
| VkExtent2D inputSize | 输入图像的尺寸。支持的最大尺寸为2048 * 1024。 |
| VkExtent2D outputSize | 输出图像的尺寸。 |
| VkRect2D outputRegion | 超分输出图像区域。 |
| VkFormat outputFormat | 输出图像的格式。 |
| int jitterNum | 相机抖动的周期数，取值范围为[4, 16]，推荐8。 |
| bool isDepthReversed | 是否存在深度反转，如果使用0.0表示最远深度则需要设置此参数值为true，否则设置为false。 |

#### 结构体成员变量说明

#### inputSize

```ets
VkExtent2D XEG_TemporalUpscaleCreateInfo::inputSize
```

**描述**

输入图像的尺寸。支持的最大尺寸为2048 * 1024。

#### isDepthReversed

```ets
bool XEG_TemporalUpscaleCreateInfo::isDepthReversed
```

**描述**

是否存在深度反转，如果使用0.0表示最远深度则需要设置此参数值为true，否则设置为false。

#### jitterNum

```ets
int XEG_TemporalUpscaleCreateInfo::jitterNum
```

**描述**

相机抖动的周期数，取值范围为[4, 16]，推荐8。

#### outputFormat

```ets
VkFormat XEG_TemporalUpscaleCreateInfo::outputFormat
```

**描述**

输出图像的格式。

#### outputRegion

```ets
VkRect2D XEG_TemporalUpscaleCreateInfo::outputRegion
```

**描述**

超分输出图像区域。

#### outputSize

```ets
VkExtent2D XEG_TemporalUpscaleCreateInfo::outputSize
```

**描述**

输出图像的尺寸。