# XEG_AdaptiveVRSCreateInfo

#### 概述

此结构体描述创建[XEG_AdaptiveVRS](XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_adaptivevrs)对象的参数信息，当结构体中的信息变化时，需要创建新的[XEG_AdaptiveVRS](XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_adaptivevrs)对象。

**起始版本：** 5.0.0(12)

**相关模块： **[XEngine](XEngine.md)

#### 汇总

#### 成员变量

名称

描述

VkExtent2D [inputSize](#ZH-CN_TOPIC_0000002362157649__inputsize)

上一帧渲染管线最终渲染的图像尺寸。

VkRect2D [inputRegion](#ZH-CN_TOPIC_0000002362157649__inputregion)

上一帧渲染管线最终渲染的图像区域。此参数存在两个结构体：VkOffset2D offset和VkExtent2D extent。其中offset为渲染图像区域的左上角点的x与y值，extent为渲染图像区域的宽与高。

int32_t [adaptiveTileSize](#ZH-CN_TOPIC_0000002362157649__adaptivetilesize)

自适应VRS的渲染的分片大小，分片大的情况下性能会更好，但是画质会劣化。当前XEngine Adaptive VRS支持16和8两种规格。

float [errorSensitivity](#ZH-CN_TOPIC_0000002362157649__errorsensitivity)

控制最终生成着色率纹理结果的阈值。该值越大，平均着色率越小，即性能更好但画质会劣化。取值范围为[0, 1]。

bool [flip](#ZH-CN_TOPIC_0000002362157649__flip)

是否执行图像上下翻转。true表示进行图像上下翻转，false表示不进行图像上下翻转。

#### 结构体成员变量说明

#### adaptiveTileSize

```ets
int32_t XEG_AdaptiveVRSCreateInfo::adaptiveTileSize
```

**描述**

自适应VRS的渲染的分片大小，分片大的情况下性能会更好，但是画质会劣化。当前XEngine Adaptive VRS支持16和8两种规格。

#### errorSensitivity

```ets
float XEG_AdaptiveVRSCreateInfo::errorSensitivity
```

**描述**

控制最终生成着色率纹理结果的阈值。该值越大，平均着色率越小，即性能更好但画质会劣化。取值范围为[0, 1]。

#### flip

```ets
bool XEG_AdaptiveVRSCreateInfo::flip
```

**描述**

是否执行图像上下翻转。true表示进行图像上下翻转，false表示不进行图像上下翻转。

#### inputRegion

```ets
VkRect2D XEG_AdaptiveVRSCreateInfo::inputRegion
```

**描述**

上一帧渲染管线最终渲染的图像区域。此参数存在两个结构体：VkOffset2D offset和VkExtent2D extent。其中offset为渲染图像区域的左上角点的x与y值，extent为渲染图像区域的宽与高。

#### inputSize

```ets
VkExtent2D XEG_AdaptiveVRSCreateInfo::inputSize
```

**描述**

上一帧渲染管线最终渲染的图像尺寸。