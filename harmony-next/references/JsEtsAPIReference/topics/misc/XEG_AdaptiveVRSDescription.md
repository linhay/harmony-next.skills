# XEG_AdaptiveVRSDescription

#### 概述

此结构体描述下发绘制着色率纹理命令需要的参数信息，每一帧都需要进行更新。

**起始版本：** 5.0.0(12)

**相关模块： **[XEngine](XEngine.md)

#### 汇总

#### 成员变量

名称

描述

float * [reprojectionMatrix](#ZH-CN_TOPIC_0000002328319192__reprojectionmatrix)

参数可选，参数非空时画质更优。此参数为重投影矩阵的指针，计算公式为：（上一帧投影矩阵*上一帧的观察矩阵）*（（当前帧的投影矩阵*当前帧的观察矩阵）的逆矩阵），矩阵必须是4*4列主序的矩阵。

VkImageView [inputColorImage](#ZH-CN_TOPIC_0000002328319192__inputcolorimage)

上一帧渲染管线最终渲染结果颜色附件的VkImageView。

VkImageView [inputDepthImage](#ZH-CN_TOPIC_0000002328319192__inputdepthimage)

当前帧渲染管线深度附件的VkImageView。

VkImageView [outputShadingRateImage](#ZH-CN_TOPIC_0000002328319192__outputshadingrateimage)

准备生成着色率图信息的VkImageView，此VkImageView需要用户创建并输入。

对创建VkImageView的VkImage对象有以下约束：

imageType = VK_IMAGE_TYPE_2D, extent.depth = 1, mipLevels = 1, arrayLayers = 1。

#### 结构体成员变量说明

#### inputColorImage

```ets
VkImageView XEG_AdaptiveVRSDescription::inputColorImage
```

**描述**

上一帧渲染管线最终渲染结果颜色附件的VkImageView。

#### inputDepthImage

```ets
VkImageView XEG_AdaptiveVRSDescription::inputDepthImage
```

**描述**

当前帧渲染管线深度附件的VkImageView。

#### outputShadingRateImage

```ets
VkImageView XEG_AdaptiveVRSDescription::outputShadingRateImage
```

**描述**

准备生成着色率图信息的VkImageView，此VkImageView需要用户创建并输入。

#### reprojectionMatrix

```ets
float* XEG_AdaptiveVRSDescription::reprojectionMatrix
```

**描述**

参数可选，参数非空时画质更优。此参数为重投影矩阵的指针，计算公式为：（上一帧投影矩阵*上一帧的观察矩阵）*（（当前帧的投影矩阵*当前帧的观察矩阵）的逆矩阵），矩阵必须是4*4列主序的矩阵。