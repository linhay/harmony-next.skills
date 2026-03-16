# XEG_DDGICreateInfo

#### 概述

此结构体描述创建具有DDGI特性的[XEG_RTGI](XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_rtgi)对象的信息，当结构体中的信息变化时，需要创建新的[XEG_RTGI](XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_rtgi)对象。

**起始版本：** 6.0.0(20)

**相关模块： **[XEngine](XEngine.md)

#### 汇总

#### 成员变量

名称

描述

XEG_StructureType [sType](#ZH-CN_TOPIC_0000002328319184__stype)

识别此结构的[XEG_StructureType](XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_structuretype)值，必须是XEG_STRUCTURE_TYPE_DDGI_CREATE_INFO。

const void * [pNext](#ZH-CN_TOPIC_0000002328319184__pnext)

指向扩展结构的指针。

XEG_RTGIQualityMode [qualityMode](#ZH-CN_TOPIC_0000002328319184__qualitymode)

输出图像的质量模式，必须为[XEG_RTGIQualityMode](XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_rtgiqualitymode)中的枚举值。

uint32_t [numberVolume](#ZH-CN_TOPIC_0000002328319184__numbervolume)

需要同时渲染的最大体积数量，范围为[1, 9]。

VkExtent2D [scaledView](#ZH-CN_TOPIC_0000002328319184__scaledview)

渲染宽高缩小倍率，建议范围为[1, 4]，必须不小于1。

VkExtent2D [viewSize](#ZH-CN_TOPIC_0000002328319184__viewsize)

输出GI图像的渲染宽高。

bool [enableCloud](#ZH-CN_TOPIC_0000002328319184__enablecloud)

是否开启端云模式，true为开启，false为关闭。

#### 结构体成员变量说明

#### enableCloud

```ets
bool XEG_DDGICreateInfo::enableCloud
```

**描述**

是否开启端云模式，true为开启，false为关闭。

#### numberVolume

```ets
uint32_t XEG_DDGICreateInfo::numberVolume
```

**描述**

需要同时渲染的最大体积数量，范围为[1, 9]。

#### pNext

```ets
const void* XEG_DDGICreateInfo::pNext
```

**描述**

指向扩展结构的指针。

#### qualityMode

```ets
XEG_RTGIQualityMode XEG_DDGICreateInfo::qualityMode
```

**描述**

输出图像的质量模式，必须为[XEG_RTGIQualityMode](XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_rtgiqualitymode)中的枚举值。

#### scaledView

```ets
VkExtent2D XEG_DDGICreateInfo::scaledView
```

**描述**

渲染宽高缩小倍率，建议范围为[1, 4]，必须不小于1。

#### sType

```ets
XEG_StructureType XEG_DDGICreateInfo::sType
```

**描述**

识别此结构的[XEG_StructureType](XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_structuretype)值，必须是XEG_STRUCTURE_TYPE_DDGI_CREATE_INFO。

#### viewSize

```ets
VkExtent2D XEG_DDGICreateInfo::viewSize
```

**描述**

输出GI图像的渲染宽高。