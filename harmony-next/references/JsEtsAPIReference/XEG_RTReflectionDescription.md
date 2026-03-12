# XEG_RTReflectionDescription

#### 概述

此结构体描述下发光线求交命令时的输入信息。

**起始版本：** 6.0.0(20)

**相关模块： **[XEngine](XEngine.md)

#### 汇总

#### 成员变量

名称

描述

XEG_StructureType [sType](#ZH-CN_TOPIC_0000002328159384__stype)

识别此结构的[XEG_StructureType](XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_structuretype)值，必须是XEG_STRUCTURE_TYPE_RT_REFLECTION_DESCRIPTION。

const void * [pNext](#ZH-CN_TOPIC_0000002328159384__pnext)

指向扩展结构的指针。

VkImageView [inputRayOriginImage](#ZH-CN_TOPIC_0000002328159384__inputrayoriginimage)

光线原点图像，不能为空。格式必须是至少3通道的float类型，RGB通道分别存储原点的xyz坐标。

VkImageView [inputRayDirectionImage](#ZH-CN_TOPIC_0000002328159384__inputraydirectionimage)

光线方向图像，不能为空。格式必须是至少3通道的float类型，RGB通道分别存储方向的xyz坐标。 如果格式为有符号的float类型，不做特殊处理，如果格式为无符号的float类型，方向信息需要按照以下方式量化：direction = (direction + 1.0) / 2.0 。

VkImageView [outputReflectionInfoImage](#ZH-CN_TOPIC_0000002328159384__outputreflectioninfoimage)

输出的反射光线求交结果，格式必须为R32G32B32A32_UINT。求交结果会将光线追踪最近的命中信息打包成128bit，解析方式参考结构体成员变量说明中[outputReflectionInfoImage](#ZH-CN_TOPIC_0000002328159384__outputreflectioninfoimage)描述。

VkAccelerationStructureKHR [accelerationStructure](#ZH-CN_TOPIC_0000002328159384__accelerationstructure)

场景的光线追踪加速结构。

float [rayMin](#ZH-CN_TOPIC_0000002328159384__raymin)

光线起点到最近可能相交点之间的最小距离。必须为非负值，且小于等于rayMax。

float [rayMax](#ZH-CN_TOPIC_0000002328159384__raymax)

光线起点到最远可能相交点之间的最大距离。超出此范围的任何相交都将被忽略。

uint32_t [reflectionCullMask](#ZH-CN_TOPIC_0000002328159384__reflectioncullmask)

配置光线查询[rayQueryInitializeEXT](https://github.com/KhronosGroup/GLSL/blob/main/extensions/ext/GLSL_EXT_ray_query.txt)函数中的rayFlags和cullMask参数。高24bit表示rayFlags，低8bit表示cullMask。

#### 结构体成员变量说明

#### accelerationStructure

```ets
VkAccelerationStructureKHR XEG_RTReflectionDescription::accelerationStructure
```

**描述**

场景的光线追踪加速结构。

#### inputRayDirectionImage

```ets
VkImageView XEG_RTReflectionDescription::inputRayDirectionImage
```

**描述**

光线方向图像，不能为空。格式必须是至少3通道的float类型，RGB通道分别存储方向的xyz坐标。 如果格式为有符号的float类型，不做特殊处理，如果格式为无符号的float类型，方向信息需要按照以下方式量化：direction = (direction + 1.0) / 2.0 。

#### inputRayOriginImage

```ets
VkImageView XEG_RTReflectionDescription::inputRayOriginImage
```

**描述**

光线原点图像，不能为空。格式必须是至少3通道的float类型，RGB通道分别存储原点的xyz坐标。

#### outputReflectionInfoImage

```ets
VkImageView XEG_RTReflectionDescription::outputReflectionInfoImage
```

**描述**

输出的反射光线求交结果，格式必须为R32G32B32A32_UINT。求交结果会将光线追踪最近的命中信息打包成128bit，解析方式如下：

```ets
uint raymiss = outputReflectionInfoImage.x & 1;
uint primitiveId = (outputReflectionInfoImage.x >> 1) & (0x3ffff);
uint instanceId = outputReflectionInfoImage.x >> 19;
vec2 barycentrics = unpackHalf2x16(outputReflectionInfoImage.z);
float hitT = uintBitsToFloat(outputReflectionInfoImage.w);
uint sbtOffest = (outputReflectionInfoImage.y >> 16);
uint geomtryIndex = (outputReflectionInfoImage.y) & 0xffff;
```

#### pNext

```ets
const void* XEG_RTReflectionDescription::pNext
```

**描述**

指向扩展结构的指针。

#### rayMax

```ets
float XEG_RTReflectionDescription::rayMax
```

**描述**

光线起点到最远可能相交点之间的最大距离。超出此范围的任何相交都将被忽略。

#### rayMin

```ets
float XEG_RTReflectionDescription::rayMin
```

**描述**

光线起点到最近可能相交点之间的最小距离。必须为非负值，且小于等于rayMax。

#### reflectionCullMask

```ets
uint32_t XEG_RTReflectionDescription::reflectionCullMask
```

**描述**

配置光线查询[rayQueryInitializeEXT](https://github.com/KhronosGroup/GLSL/blob/main/extensions/ext/GLSL_EXT_ray_query.txt)函数中的rayFlags和cullMask参数。高24bit表示rayFlags，低8bit表示cullMask。

#### sType

```ets
XEG_StructureType XEG_RTReflectionDescription::sType
```

**描述**

识别此结构的[XEG_StructureType](XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_structuretype)值，必须是XEG_STRUCTURE_TYPE_RT_REFLECTION_DESCRIPTION。