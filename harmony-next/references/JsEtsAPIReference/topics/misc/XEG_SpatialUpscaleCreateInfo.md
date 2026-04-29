# [XEG_SpatialUpscale](XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_spatialupscale)CreateInfo

#### 概述

此结构体描述创建[XEG_SpatialUpscale](XEngine.md#ZH-CN_TOPIC_0000002553202223__xeg_spatialupscale)对象的信息，当结构体中的信息变化时，需要创建新的[XEG_SpatialUpscale](XEngine.md#ZH-CN_TOPIC_0000002553202223__xeg_spatialupscale)对象。

**起始版本：** 5.0.0(12)

**相关模块：**[XEngine](XEngine.md)

所在头文件： [xeg_vulkan_spatial_upscale.h](xeg_vulkan_spatial_upscale.h.md)

#### 汇总

#### 成员变量

| 名称 | 描述 |
| --- | --- |
| VkExtent2D inputSize | 超分输入图像的尺寸，必须与超分输入图像的VkimageView的尺寸一致，否则会导致未定义问题，如超分失败、程序崩溃等。 |
| VkRect2D inputRegion | 超分输入图像的采样区域，图像超分区域参数必须大于0且小于等于图像尺寸，否则会导致渲染失败或者渲染效果不合预期，此参数存在两个结构体：VkOffset2D offset和VkExtent2D extent。其中offset为图像区域的左上角点的x与y值，extent为图像区域的宽与高。 |
| VkExtent2D outputSize | 超分输出图像的尺寸，必须与超分结果VkimageView的尺寸一致，否则会导致未定义问题，如超分失败、程序崩溃等。 |
| VkRect2D outputRegion | 超分输出图像的绘制区域，图像超分区域参数必须大于0且小于等于图像尺寸，否则会导致渲染失败或者渲染效果不合预期，此参数存在两个结构体：VkOffset2D offset和VkExtent2D extent。其中offset为图像区域的左上角点的x与y值，extent为图像区域的宽与高。 |
| VkFormat format | 超分输入图像的格式。 |
| float sharpness | 超分的锐化参数，建议取值范围为[0, 1]，不同风格图像锐化值需要调整，否则会导致过度锐化现象，如出现大量噪点。 |

#### 结构体成员变量说明

#### format

```ets
VkFormat XEG_SpatialUpscaleCreateInfo::format
```

**描述**

超分输入图像的格式。

#### inputRegion

```ets
VkRect2D XEG_SpatialUpscaleCreateInfo::inputRegion
```

**描述**

超分输入图像的采样区域，图像超分区域参数必须大于0且小于等于图像尺寸，否则会导致渲染失败或者渲染效果不合预期，此参数存在两个结构体：VkOffset2D offset和VkExtent2D extent。其中offset为图像区域的左上角点的x与y值，extent为图像区域的宽与高。

#### inputSize

```ets
VkExtent2D XEG_SpatialUpscaleCreateInfo::inputSize
```

**描述**

超分输入图像的尺寸，必须与超分输入图像的VkimageView的尺寸一致，否则会导致未定义问题，如超分失败、程序崩溃等。

#### outputRegion

```ets
VkRect2D XEG_SpatialUpscaleCreateInfo::outputRegion
```

**描述**

超分输出图像的绘制区域，图像超分区域参数必须大于0且小于等于图像尺寸，否则会导致渲染失败或者渲染效果不合预期，此参数存在两个结构体：VkOffset2D offset和VkExtent2D extent。其中offset为图像区域的左上角点的x与y值，extent为图像区域的宽与高。

#### outputSize

```ets
VkExtent2D XEG_SpatialUpscaleCreateInfo::outputSize
```

**描述**

超分输出图像的尺寸，必须与超分结果VkimageView的尺寸一致，否则会导致未定义问题，如超分失败、程序崩溃等。

#### sharpness

```ets
float XEG_SpatialUpscaleCreateInfo::sharpness
```

**描述**

超分的锐化参数，建议取值范围为[0, 1]，不同风格图像锐化值需要调整，否则会导致过度锐化现象，如出现大量噪点。