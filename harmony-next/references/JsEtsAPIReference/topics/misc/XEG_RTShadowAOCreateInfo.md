# XEG_RTShadowAOCreateInfo

**概述**

此结构体描述创建支持光线追踪阴影和环境光遮蔽效果[XEG_RTVisibleMask](XEngine.md#ZH-CN_TOPIC_0000002553202223__xeg_rtvisiblemask)实例的初始化信息。当结构体中的信息变化时，需要创建新的[XEG_RTVisibleMask](XEngine.md#ZH-CN_TOPIC_0000002553202223__xeg_rtvisiblemask)对象。

起始版本： 6.0.0(20)

相关模块： [XEngine](XEngine.md)

所在头文件： [xeg_vulkan_rt_visible_mask.h](xeg_vulkan_rt_visible_mask.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| XEG_StructureType sType | 识别此结构的XEG_StructureType值，必须是XEG_STRUCTURE_TYPE_RT_SHADOWAO_CREATE_INFO。 |
| const void * pNext | 指向扩展结构的指针。 |
| VkExtent2D rtInputGbufferSize | 输入的GBuffer深度和法线图像的尺寸，深度图像和法线图像的尺寸必须相同。 |
| VkExtent2D rtShadowAOSize | 输出的阴影和环境光遮蔽图像的尺寸，必须与rtInputGbufferSize等比例。 |
| bool enableRTShadow | 是否开启光线追踪阴影效果，true为开启，false为不开启。阴影与环境光遮蔽效果至少需要开启一个。 |
| bool enableRTAO | 是否开启光线追踪环境光遮蔽效果，true为开启，false为不开启。阴影与环境光遮蔽效果至少需要开启一个。 |
| XEG_TraversalMode traversalMode | 遍历模式，光线追踪阴影和环境光遮蔽使用相同的遍历模式设置。 |
| XEG_DenoiseQualityMode denoiseMode | 去噪质量模式，光线追踪阴影和环境光遮蔽使用相同的质量设置。 |
| bool aoOnlyInShadow | 仅在开启光线追踪阴影效果时生效，如果设置为true，将只计算处于阴影区域的像素的环境光遮蔽值。如果设置为false则计算所有像素。 |
| bool reverseZ | 场景是否开启了深度翻转，即远平面处的深度为0。深度翻转可以获取更高精度的深度值，建议开启。true表示已开启，false表示未开启。 |

**结构体成员变量说明**

**aoOnlyInShadow**

```ets
bool XEG_RTShadowAOCreateInfo::aoOnlyInShadow
```

描述

仅在开启光线追踪阴影效果时生效，如果设置为true，将只计算处于阴影区域的像素的环境光遮蔽值。如果设置为false则计算所有像素。

**denoiseMode**

```ets
XEG_DenoiseQualityMode XEG_RTShadowAOCreateInfo::denoiseMode
```

描述

去噪质量模式，光线追踪阴影和环境光遮蔽使用相同的质量设置。

**enableRTAO**

```ets
bool XEG_RTShadowAOCreateInfo::enableRTAO
```

描述

是否开启光线追踪环境光遮蔽效果，true为开启，false为不开启。阴影与环境光遮蔽效果至少需要开启一个。

**enableRTShadow**

```ets
bool XEG_RTShadowAOCreateInfo::enableRTShadow
```

描述

是否开启光线追踪阴影效果，true为开启，false为不开启。阴影与环境光遮蔽效果至少需要开启一个。

**pNext**

```ets
const void* XEG_RTShadowAOCreateInfo::pNext
```

描述

指向扩展结构的指针。

**reverseZ**

```ets
bool XEG_RTShadowAOCreateInfo::reverseZ
```

描述

场景是否开启了深度翻转，即远平面处的深度为0。深度翻转可以获取更高精度的深度值，建议开启。true表示已开启，false表示未开启。

**rtInputGbufferSize**

```ets
VkExtent2D XEG_RTShadowAOCreateInfo::rtInputGbufferSize
```

描述

输入的GBuffer深度和法线图像的尺寸，深度图像和法线图像的尺寸必须相同。

**rtShadowAOSize**

```ets
VkExtent2D XEG_RTShadowAOCreateInfo::rtShadowAOSize
```

描述

输出的阴影和环境光遮蔽图像的尺寸，必须与rtInputGbufferSize等比例。

**sType**

```ets
XEG_StructureType XEG_RTShadowAOCreateInfo::sType
```

描述

识别此结构的[XEG_StructureType](XEngine.md#ZH-CN_TOPIC_0000002553202223__xeg_structuretype)值，必须是XEG_STRUCTURE_TYPE_RT_SHADOWAO_CREATE_INFO。

**traversalMode**

```ets
XEG_TraversalMode XEG_RTShadowAOCreateInfo::traversalMode
```

描述

遍历模式，光线追踪阴影和环境光遮蔽使用相同的遍历模式设置。