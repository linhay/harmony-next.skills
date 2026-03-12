# XEG_RTShadowAODescription

#### 概述

此结构体描述光线追踪阴影和环境光遮蔽算法渲染命令的输入信息。

**起始版本：** 6.0.0(20)

**相关模块： **[XEngine](XEngine.md)

#### 汇总

#### 成员变量

名称

描述

XEG_StructureType [sType](#ZH-CN_TOPIC_0000002362157661__stype)

识别此结构的[XEG_StructureType](XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_structuretype)值，必须是XEG_STRUCTURE_TYPE_RT_SHADOWAO_DESCRIPTION。

const void * [pNext](#ZH-CN_TOPIC_0000002362157661__pnext)

指向扩展结构的指针。

VkImageView [inputDepthImage](#ZH-CN_TOPIC_0000002362157661__inputdepthimage)

深度图像，不能为空。

VkImageView [inputNormalImage](#ZH-CN_TOPIC_0000002362157661__inputnormalimage)

法线图像，不能为空。需要是无符号浮点格式并包含3个以上通道，如VK_FORMAT_R8G8B8_UNORM。XEngine将按照Normal=textureLod(inputNormalImage).xyz*2.0–1.0的方式解析法线。

VkImageView [inputMotionVectorImage](#ZH-CN_TOPIC_0000002362157661__inputmotionvectorimage)

运动矢量图像，可以为空。运动矢量的计算方式为当前渲染像素的NDC坐标的XY值减去其上一帧的NDC坐标的XY值。图像格式需要是VK_FORMAT_R16G16_SFLOAT或更高精度。保留字段，暂不支持。

VkImageView [outputShadowAOImage](#ZH-CN_TOPIC_0000002362157661__outputshadowaoimage)

输出的阴影和环境光遮蔽图像，不能为空，格式必须为VK_FORMAT_R8G8_UNORM。阴影值将写入R通道，环境光遮蔽值将写入G通道。

VkAccelerationStructureKHR [accelerationStructure](#ZH-CN_TOPIC_0000002362157661__accelerationstructure)

场景的光线追踪加速结构。

bool [isAsInTranslatedSpace](#section136835616294)

光线追踪加速结构是否在Translated世界空间构建。ture表示在Translated世界空间构建，false表示在绝对世界空间构建。默认值为false。

float [translatedViewMatrix](#section195161648153112)

相机Translated观察矩阵，必须是4*4列主序矩阵。当isAsInTranslatedSpace值为false时可以不赋值。

float [viewMatrix](#ZH-CN_TOPIC_0000002362157661__viewmatrix) [16]

相机观察矩阵，必须是4*4列主序矩阵。

float [projectionMatrix](#ZH-CN_TOPIC_0000002362157661__projectionmatrix) [16]

相机投影矩阵，必须是4*4列主序矩阵。

float [worldCameraOrigin](#ZH-CN_TOPIC_0000002362157661__worldcameraorigin) [3]

相机在世界空间中的位置坐标。

bool [ndcFilpY](#section2323113111347)

标识NDC空间与世界空间是否存在Y轴翻转关系。true表示翻转，false表示不翻转。默认值为false。

const [XEG_RTShadowParameters](XEG_RTShadowParameters.md) * [pRtShadowParameters](#ZH-CN_TOPIC_0000002362157661__prtshadowparameters)

光线追踪阴影算法参数，当XEG_RTShadowAOCreateInfo::enableRTShadow=true时不能为空。

const [XEG_RTAOParameters](XEG_RTAOParameters.md) * [pRtAOParameters](#ZH-CN_TOPIC_0000002362157661__prtaoparameters)

光线追踪环境光算法参数，当XEG_RTShadowAOCreateInfo::enableRTAO=true时不能为空。

const [XEG_RTShadowAODenoiserParameters](XEG_RTShadowAODenoiserParameters.md) * [pRtShadowAODenoiserParameters](#ZH-CN_TOPIC_0000002362157661__prtshadowaodenoiserparameters)

去噪参数，不能为空。光线追踪阴影和环境光遮蔽使用相同的去噪参数。

#### 结构体成员变量说明

#### accelerationStructure

```ets
VkAccelerationStructureKHR XEG_RTShadowAODescription::accelerationStructure
```

**描述**

场景的光线追踪加速结构。

#### inputDepthImage

```ets
VkImageView XEG_RTShadowAODescription::inputDepthImage
```

**描述**

深度图像，不能为空。

#### inputMotionVectorImage

```ets
VkImageView XEG_RTShadowAODescription::inputMotionVectorImage
```

**描述**

运动矢量图像，可以为空。运动矢量的计算方式为当前渲染像素的NDC坐标的XY值减去其上一帧的NDC坐标的XY值。图像格式需要是VK_FORMAT_R16G16_SFLOAT或更高精度。保留字段，暂不支持。

#### inputNormalImage

```ets
VkImageView XEG_RTShadowAODescription::inputNormalImage
```

**描述**

法线图像，不能为空。需要是无符号浮点格式并包含3个以上通道，如VK_FORMAT_R8G8B8_UNORM。XEngine将按照Normal=textureLod(inputNormalImage).xyz*2.0–1.0的方式解析法线。

#### outputShadowAOImage

```ets
VkImageView XEG_RTShadowAODescription::outputShadowAOImage
```

**描述**

输出的阴影和环境光遮蔽图像，不能为空，格式必须为VK_FORMAT_R8G8_UNORM。阴影值将写入R通道，环境光遮蔽值将写入G通道。

#### pNext

```ets
const void* XEG_RTShadowAODescription::pNext
```

**描述**

指向扩展结构的指针。

#### projectionMatrix

```ets
float XEG_RTShadowAODescription::projectionMatrix[16]
```

**描述**

相机投影矩阵，必须是4*4列主序矩阵。

#### pRtAOParameters

```ets
const XEG_RTAOParameters* XEG_RTShadowAODescription::pRtAOParameters
```

**描述**

光线追踪环境光算法参数，当XEG_RTShadowAOCreateInfo::enableRTAO=true时不能为空。

#### pRtShadowAODenoiserParameters

```ets
const XEG_RTShadowAODenoiserParameters* XEG_RTShadowAODescription::pRtShadowAODenoiserParameters
```

**描述**

去噪参数，不能为空。光线追踪阴影和环境光遮蔽使用相同的去噪参数。

#### pRtShadowParameters

```ets
const XEG_RTShadowParameters* XEG_RTShadowAODescription::pRtShadowParameters
```

**描述**

光线追踪阴影算法参数，当XEG_RTShadowAOCreateInfo::enableRTShadow=true时不能为空。

#### sType

```ets
XEG_StructureType XEG_RTShadowAODescription::sType
```

**描述**

识别此结构的[XEG_StructureType](XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_structuretype)值，必须是XEG_STRUCTURE_TYPE_RT_SHADOWAO_DESCRIPTION。

#### viewMatrix

```ets
float XEG_RTShadowAODescription::viewMatrix[16]
```

**描述**

相机观察矩阵，必须是4*4列主序矩阵。

#### worldCameraOrigin

```ets
float XEG_RTShadowAODescription::worldCameraOrigin[3]
```

**描述**

相机在世界空间中的位置坐标。

#### isAsInTranslatedSpace

```ets
bool XEG_RTShadowAODescription::isAsInTranslatedSpace = false;
```

**描述**

光线追踪加速结构是否在Translated世界空间构建。ture表示在Translated世界空间构建，false表示在绝对世界空间构建。默认值为false。

#### translatedViewMatrix

```ets
float XEG_RTShadowAODescription::translatedViewMatrix[16];
```

**描述**

相机Translated观察矩阵，必须是4*4列主序矩阵。当isAsInTranslatedSpace值为false时可以不赋值。

#### ndcFilpY

```ets
bool XEG_RTShadowAODescription::ndcFilpY  = false;
```

**描述**

标识NDC空间与世界空间是否存在Y轴翻转关系。true表示翻转，false表示不翻转。默认值为false。