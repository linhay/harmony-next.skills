# XEG_NNGICreateInfo

#### 概述

此结构体描述创建具有NNGI特性的[XEG_RTGI](XEngine.md#ZH-CN_TOPIC_0000002553202223__xeg_rtgi)对象的信息，当结构体中的信息变化时，需要创建新的[XEG_RTGI](XEngine.md#ZH-CN_TOPIC_0000002553202223__xeg_rtgi)对象。

**起始版本：** 6.0.0(20)

**相关模块：**[XEngine](XEngine.md)

所在头文件： [xeg_vulkan_rtgi.h](xeg_vulkan_rtgi.h.md)

#### 汇总

#### 成员变量

| 名称 | 描述 |
| --- | --- |
| [XEG_StructureType](XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_structuretype) sType | 识别此结构的XEG_StructureType值，必须是XEG_STRUCTURE_TYPE_NNGI_CREATE_INFO。 |
| const void * pNext | 指向扩展结构的指针。 |
| [XEG_RTGIQualityMode](XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_rtgiqualitymode) qualityMode | 输出图像的质量模式，必须为[XEG_RTGI](XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_rtgi)QualityMode中的枚举值。 |
| VkExtent2D inferenceInputSize | 推理输入图像的分辨率，必须与[XEG_NNGIDescription](XEG_NNGIDescription.md)中的推理输入图像的分辨率保持一致。 |
| VkExtent2D inferenceOutputSize | 推理输出图像的分辨率，必须与[XEG_NNGIDescription](XEG_NNGIDescription.md)中的推理输出图像的分辨率保持一致，推荐使用（640，368）。 |
| VkExtent2D trainingSize | 训练图像的分辨率，必须与[XEG_NNGIDescription](XEG_NNGIDescription.md)中的训练输入和输出图像的分辨率保持一致，推荐使用（64，32）。 |

#### 结构体成员变量说明

#### inferenceInputSize

```ets
VkExtent2D XEG_NNGICreateInfo::inferenceInputSize
```

**描述**

推理输入图像的分辨率，必须与[XEG_NNGIDescription](XEG_NNGIDescription.md)中的推理输入图像的分辨率保持一致。

#### inferenceOutputSize

```ets
VkExtent2D XEG_NNGICreateInfo::inferenceOutputSize
```

**描述**

推理输出图像的分辨率，必须与[XEG_NNGIDescription](XEG_NNGIDescription.md)中的推理输出图像的分辨率保持一致，推荐使用（640，368）。

#### pNext

```ets
const void* XEG_NNGICreateInfo::pNext
```

**描述**

指向扩展结构的指针。

#### qualityMode

```ets
XEG_RTGIQualityMode XEG_NNGICreateInfo::qualityMode
```

**描述**

输出图像的质量模式，必须为[XEG_RTGIQualityMode](XEngine.md#ZH-CN_TOPIC_0000002553202223__xeg_rtgiqualitymode)中的枚举值。

#### sType

```ets
XEG_StructureType XEG_NNGICreateInfo::sType
```

**描述**

识别此结构的[XEG_StructureType](XEngine.md#ZH-CN_TOPIC_0000002553202223__xeg_structuretype)值，必须是XEG_STRUCTURE_TYPE_NNGI_CREATE_INFO。

#### trainingSize

```ets
VkExtent2D XEG_NNGICreateInfo::trainingSize
```

**描述**

训练图像的分辨率，必须与[XEG_NNGIDescription](XEG_NNGIDescription.md)中的训练输入和输出图像的分辨率保持一致，推荐使用（64，32）。
