# XEG_DDGIDescription

#### 概述

此结构体描述更新DDGI探针辐照度及渲染输出GI图像所需的信息。

**起始版本：** 6.0.0(20)

**相关模块： **[XEngine](XEngine.md)

所在头文件： [xeg_vulkan_rtgi.h](xeg_vulkan_rtgi.h.md)

#### 汇总

#### 成员变量

| 名称 | 描述 |
| --- | --- |
| [XEG_StructureType](XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_structuretype) sType | 识别此结构的XEG_StructureType值，必须是XEG_STRUCTURE_TYPE_DDGI_DESCRIPTION。 |
| const void * pNext | 指向扩展结构的指针。 |
| float viewMatrix [16] | 相机观察矩阵，必须是4*4列主序矩阵。 |
| float projectionMatrix [16] | 相机投影矩阵，必须是4*4列主序矩阵。 |
| VkImageView inputNormalImage | 输入Gbuffer法向量图像，其宽高必须和[XEG_DDGICreateInfo](XEG_DDGICreateInfo.md)中viewSize的宽高保持一致。 |
| VkImageView inputDepthImage | 输入Gbuffer深度图像，其宽高必须和[XEG_DDGICreateInfo](XEG_DDGICreateInfo.md)中viewSize的宽高保持一致。 |
| VkImageView inputBasecolorMetallicImage | 输入Gbuffer基础颜色和金属度图像，其宽高必须和[XEG_DDGICreateInfo](XEG_DDGICreateInfo.md)中viewSize的宽高保持一致。 |
| VkImageView inputDirectionImage | 输入探针发射光线方向图像，其宽高分别为：探针发射光线数量，输入探针数量。 |
| VkImageView inputRayRadianceDistanceImage | 输入探针发射光线交点的辐射率及距离图像，其宽高分别为：探针发射光线数量，输入探针数量。 |
| VkImageView inputRayHitNormalAndMetallicImage | 输入探针发射光线交点的法向量及金属度图像，其宽高分别为：探针发射光线数量，输入探针数量。 |
| VkBuffer inputVolumeIndexAndProbeIndex | 输入探针的索引信息，对应于探针发射光线的信息，每个数据为两个uint值（探针索引/体积索引）。 |
| uint32_t inputProbeCount | 输入探针数量，对应于inputVolumeIndexAndProbeIndex中的有效数据个数。 |
| VkBuffer outputVolumeIndexAndProbeIndex | 输出探针的索引信息，指示用户下一帧如何发射光线，每个数据为两个uint值（探针索引/体积索引）。 |
| VkBuffer outputProbeCount | 输出探针数量，对应于outputVolumeIndexAndProbeIndex中的有效数据个数。 |
| VkImageView outputGIImage | 输出GI 2D图像，其宽高必须和[XEG_DDGICreateInfo](XEG_DDGICreateInfo.md)中viewSize的宽高保持一致，VkFormat为VK_FORMAT_R8G8B8A8_UNORM。 |
| uint32_t enableVolumeNumber | 使用的体积数量，必须不大于[XEG_DDGICreateInfo](XEG_DDGICreateInfo.md)中的numberVolume值。 |
| const struct [XEG_DDGIVolumeEntryParameters](XEG_DDGIVolumeEntryParameters.md) * pVolumeEntryParameters | 输入体积参数信息，对应于XEG_DDGIVolumeEntryParameters。该结构体数组的大小必须等于enableVolumeNumber的值。 |

#### 结构体成员变量说明

#### enableVolumeNumber

```ets
uint32_t XEG_DDGIDescription::enableVolumeNumber
```

**描述**

使用的体积数量，必须不大于[XEG_DDGICreateInfo](XEG_DDGICreateInfo.md)中的numberVolume值。

#### inputBasecolorMetallicImage

```ets
VkImageView XEG_DDGIDescription::inputBasecolorMetallicImage
```

**描述**

输入Gbuffer基础颜色和金属度图像，其宽高必须和[XEG_DDGICreateInfo](XEG_DDGICreateInfo.md)中viewSize的宽高保持一致。

#### inputDepthImage

```ets
VkImageView XEG_DDGIDescription::inputDepthImage
```

**描述**

输入Gbuffer深度图像，其宽高必须和[XEG_DDGICreateInfo](XEG_DDGICreateInfo.md)中viewSize的宽高保持一致。

#### inputDirectionImage

```ets
VkImageView XEG_DDGIDescription::inputDirectionImage
```

**描述**

输入探针发射光线方向图像，其宽高分别为：探针发射光线数量，输入探针数量。

#### inputNormalImage

```ets
VkImageView XEG_DDGIDescription::inputNormalImage
```

**描述**

输入Gbuffer法向量图像，其宽高必须和[XEG_DDGICreateInfo](XEG_DDGICreateInfo.md)中viewSize的宽高保持一致。

#### inputProbeCount

```ets
uint32_t XEG_DDGIDescription::inputProbeCount
```

**描述**

输入探针数量，对应于inputVolumeIndexAndProbeIndex中的有效数据个数。

#### inputRayHitNormalAndMetallicImage

```ets
VkImageView XEG_DDGIDescription::inputRayHitNormalAndMetallicImage
```

**描述**

输入探针发射光线交点的法向量及金属度图像，其宽高分别为：探针发射光线数量，输入探针数量。

#### inputRayRadianceDistanceImage

```ets
VkImageView XEG_DDGIDescription::inputRayRadianceDistanceImage
```

**描述**

输入探针发射光线交点的辐射率及距离图像，其宽高分别为：探针发射光线数量，输入探针数量。

#### inputVolumeIndexAndProbeIndex

```ets
VkBuffer XEG_DDGIDescription::inputVolumeIndexAndProbeIndex
```

**描述**

输入探针的索引信息，对应于探针发射光线的信息，每个数据为两个uint值（探针索引/体积索引）。

#### outputGIImage

```ets
VkImageView XEG_DDGIDescription::outputGIImage
```

**描述**

输出GI 2D图像，其宽高必须和[XEG_DDGICreateInfo](XEG_DDGICreateInfo.md)中viewSize的宽高保持一致，VkFormat为VK_FORMAT_R8G8B8A8_UNORM。

#### outputProbeCount

```ets
VkBuffer XEG_DDGIDescription::outputProbeCount
```

**描述**

输出探针数量，对应于outputVolumeIndexAndProbeIndex中的有效数据个数。

#### outputVolumeIndexAndProbeIndex

```ets
VkBuffer XEG_DDGIDescription::outputVolumeIndexAndProbeIndex
```

**描述**

输出探针的索引信息，指示用户下一帧如何发射光线，每个数据为两个uint值（探针索引/体积索引）。

#### pNext

```ets
const void* XEG_DDGIDescription::pNext
```

**描述**

指向扩展结构的指针。

#### projectionMatrix

```ets
float XEG_DDGIDescription::projectionMatrix[16]
```

**描述**

相机投影矩阵，必须是4*4列主序矩阵。

#### pVolumeEntryParameters

```ets
const struct XEG_DDGIVolumeEntryParameters* XEG_DDGIDescription::pVolumeEntryParameters
```

**描述**

输入体积参数信息，对应于[XEG_DDGIVolumeEntryParameters](XEG_DDGIVolumeEntryParameters.md)。该结构体数组的大小必须等于enableVolumeNumber的值。

#### sType

```ets
XEG_StructureType XEG_DDGIDescription::sType
```

**描述**

识别此结构的[XEG_StructureType](XEngine.md#ZH-CN_TOPIC_0000002553202223__xeg_structuretype)值，必须是XEG_STRUCTURE_TYPE_DDGI_DESCRIPTION。

#### viewMatrix

```ets
float XEG_DDGIDescription::viewMatrix[16]
```

**描述**

相机观察矩阵，必须是4*4列主序矩阵。
