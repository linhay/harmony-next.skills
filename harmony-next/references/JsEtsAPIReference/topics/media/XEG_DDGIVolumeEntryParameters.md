# XEG_DDGIVolumeEntryParameters

#### 概述

此结构体描述每一个DDGI体积的必要参数。

**起始版本：** 6.0.0(20)

**相关模块：**[XEngine](../misc/XEngine.md)

#### 汇总

#### 成员变量

名称

描述

uint32_t [volumeIndex](#ZH-CN_TOPIC_0000002328319188__volumeindex)

体积索引范围为[0, 65535]，且唯一。

uint32_t [raysPerProbe](#ZH-CN_TOPIC_0000002328319188__raysperprobe)

探针发射光线数量，建议值为64，范围为[1, 1024]。

float [probeMaxRayDistance](#ZH-CN_TOPIC_0000002328319188__probemaxraydistance)

探针发射光线最大求交距离，建议值为1000.0。

float [volumePosition](#ZH-CN_TOPIC_0000002328319188__volumeposition) [3]

体积中心点坐标。

float [probeSpacing](#ZH-CN_TOPIC_0000002328319188__probespacing) [3]

探针放置间距，必须大于0。

uint32_t [volumeLightingChannelMask](#ZH-CN_TOPIC_0000002328319188__volumelightingchannelmask)

体积光照通道标记，建议值为0xFFFFFFFF。

uint32_t [volumeProbeGridCounts](#ZH-CN_TOPIC_0000002328319188__volumeprobegridcounts) [3]

探针放置数量，必须大于0，范围为[1, 32]。

float [volumeProbeIrradianceEncodingGamma](#ZH-CN_TOPIC_0000002328319188__volumeprobeirradianceencodinggamma)

辐照度的伽马校正系数，建议值为5.0，必须不为0。

float [probeHysteresis](#ZH-CN_TOPIC_0000002328319188__probehysteresis)

探针辐照度历史权重，建议值为0.95，范围为[0, 1]。

float [probeChangeThreshold](#ZH-CN_TOPIC_0000002328319188__probechangethreshold)

探针变化阈值，建议值为1.0。

float [probeBrightnessThreshold](#ZH-CN_TOPIC_0000002328319188__probebrightnessthreshold)

探针亮度阈值，建议值为1.0。

float [volumeNormalBias](#ZH-CN_TOPIC_0000002328319188__volumenormalbias)

探针法向偏移量，建议值为0.12。

float [volumeViewBias](#ZH-CN_TOPIC_0000002328319188__volumeviewbias)

探针视角偏移量，建议值为0.48。

float [volumeBlendDistance](#ZH-CN_TOPIC_0000002328319188__volumeblenddistance)

体积光照混合距离，建议值为1.0。

float [volumeBlendDistanceBlack](#ZH-CN_TOPIC_0000002328319188__volumeblenddistanceblack)

体积边缘光照渐暗范围，建议值为1.0。

float [probeBackfaceThreshold](#ZH-CN_TOPIC_0000002328319188__probebackfacethreshold)

探针反向判断阈值，建议值为0.0。

float [probeMinFrontfaceDistance](#ZH-CN_TOPIC_0000002328319188__probeminfrontfacedistance)

探针正向最小距离，建议值为0.0。

float [volumeIrradianceScalar](#ZH-CN_TOPIC_0000002328319188__volumeirradiancescalar)

体积辐照度缩放倍率，建议值为1.0，必须非负。

float [emissiveMultiplier](#ZH-CN_TOPIC_0000002328319188__emissivemultiplier)

发射光线强度倍率，建议值为1.0，必须非负。

float [lightingMultiplier](#ZH-CN_TOPIC_0000002328319188__lightingmultiplier)

光照倍率，建议值为1.0，必须非负。

bool [bForceUpdate](#ZH-CN_TOPIC_0000002328319188__bforceupdate)

是否强制更新所有探针，true为强制全部更新，false为选择部分更新，建议值为false。

VkImageView [probeIrradianceSH](#ZH-CN_TOPIC_0000002328319188__probeirradiancesh)

存储探针辐照度二阶球谐系数的3D图像，其宽度，高度和深度分别为：volumeProbeGridCounts.y * 4（二阶球谐系数的个数），volumeProbeGridCounts.x，volumeProbeGridCounts.z，VkFormat为VK_FORMAT_R32G32B32A32_SFLOAT。

#### 结构体成员变量说明

#### bForceUpdate

```ets
bool XEG_DDGIVolumeEntryParameters::bForceUpdate
```

**描述**

是否强制更新所有探针，true为强制全部更新，false为选择部分更新，建议值为false。

#### emissiveMultiplier

```ets
float XEG_DDGIVolumeEntryParameters::emissiveMultiplier
```

**描述**

发射光线强度倍率，建议值为1.0，必须非负。

#### lightingMultiplier

```ets
float XEG_DDGIVolumeEntryParameters::lightingMultiplier
```

**描述**

光照倍率，建议值为1.0，必须非负。

#### probeBackfaceThreshold

```ets
float XEG_DDGIVolumeEntryParameters::probeBackfaceThreshold
```

**描述**

探针反向判断阈值，建议值为0.0。

#### probeBrightnessThreshold

```ets
float XEG_DDGIVolumeEntryParameters::probeBrightnessThreshold
```

**描述**

探针亮度阈值，建议值为1.0。

#### probeChangeThreshold

```ets
float XEG_DDGIVolumeEntryParameters::probeChangeThreshold
```

**描述**

探针变化阈值，建议值为1.0。

#### probeHysteresis

```ets
float XEG_DDGIVolumeEntryParameters::probeHysteresis
```

**描述**

探针辐照度历史权重，建议值为0.95，范围为[0, 1]。

#### probeIrradianceSH

```ets
VkImageView XEG_DDGIVolumeEntryParameters::probeIrradianceSH
```

**描述**

存储探针辐照度二阶球谐系数的3D图像，其宽度，高度和深度分别为：volumeProbeGridCounts.y * 4（二阶球谐系数的个数），volumeProbeGridCounts.x，volumeProbeGridCounts.z，VkFormat为VK_FORMAT_R32G32B32A32_SFLOAT。

#### probeMaxRayDistance

```ets
float XEG_DDGIVolumeEntryParameters::probeMaxRayDistance
```

**描述**

探针发射光线最大求交距离，建议值为1000.0。

#### probeMinFrontfaceDistance

```ets
float XEG_DDGIVolumeEntryParameters::probeMinFrontfaceDistance
```

**描述**

探针正向最小距离，建议值为0.0。

#### probeSpacing

```ets
float XEG_DDGIVolumeEntryParameters::probeSpacing[3]
```

**描述**

探针放置间距，必须大于0。

#### raysPerProbe

```ets
uint32_t XEG_DDGIVolumeEntryParameters::raysPerProbe
```

**描述**

探针发射光线数量，建议值为64，范围为[1, 1024]。

#### volumeBlendDistance

```ets
float XEG_DDGIVolumeEntryParameters::volumeBlendDistance
```

**描述**

体积光照混合距离，建议值为1.0。

#### volumeBlendDistanceBlack

```ets
float XEG_DDGIVolumeEntryParameters::volumeBlendDistanceBlack
```

**描述**

体积边缘光照渐暗范围，建议值为1.0。

#### volumeIndex

```ets
uint32_t XEG_DDGIVolumeEntryParameters::volumeIndex
```

**描述**

体积索引范围为[0, 65535]，且唯一。

#### volumeIrradianceScalar

```ets
float XEG_DDGIVolumeEntryParameters::volumeIrradianceScalar
```

**描述**

体积辐照度缩放倍率，建议值为1.0，必须非负。

#### volumeLightingChannelMask

```ets
uint32_t XEG_DDGIVolumeEntryParameters::volumeLightingChannelMask
```

**描述**

体积光照通道标记，建议值为0xFFFFFFFF。

#### volumeNormalBias

```ets
float XEG_DDGIVolumeEntryParameters::volumeNormalBias
```

**描述**

探针法向偏移量，建议值为0.12。

#### volumePosition

```ets
float XEG_DDGIVolumeEntryParameters::volumePosition[3]
```

**描述**

体积中心点坐标。

#### volumeProbeGridCounts

```ets
uint32_t XEG_DDGIVolumeEntryParameters::volumeProbeGridCounts[3]
```

**描述**

探针放置数量，必须大于0，范围为[1, 32]。

#### volumeProbeIrradianceEncodingGamma

```ets
float XEG_DDGIVolumeEntryParameters::volumeProbeIrradianceEncodingGamma
```

**描述**

辐照度的伽马校正系数，建议值为5.0，必须不为0。

#### volumeViewBias

```ets
float XEG_DDGIVolumeEntryParameters::volumeViewBias
```

**描述**

探针视角偏移量，建议值为0.48。