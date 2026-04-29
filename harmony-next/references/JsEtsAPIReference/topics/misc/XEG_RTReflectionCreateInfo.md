# [XEG_RTReflection](XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_rtreflection)CreateInfo

#### 概述

此结构体描述创建[XEG_RTReflection](XEngine.md#ZH-CN_TOPIC_0000002553202223__xeg_rtreflection)对象的信息。当结构体中的信息变化时，需要创建新的[XEG_RTReflection](XEngine.md#ZH-CN_TOPIC_0000002553202223__xeg_rtreflection)对象。

**起始版本：** 6.0.0(20)

**相关模块：**[XEngine](XEngine.md)

所在头文件： [xeg_vulkan_rt_reflection.h](xeg_vulkan_rt_reflection.h.md)

#### 汇总

#### 成员变量

| 名称 | 描述 |
| --- | --- |
| [XEG_StructureType](XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_structuretype) sType | 识别此结构的XEG_StructureType值，必须是XEG_STRUCTURE_TYPE_RT_REFLECTION_CREATE_INFO。 |
| const void * pNext | 指向扩展结构的指针。 |
| VkExtent2D renderSize | 输入图像的尺寸。 |
| bool enableFastTrace | 是否开启快速求交模式，相较常规求交模式，快速求交模式的性能更好。true表示开启快速求交模式，false表示使用常规求交模式。 |

#### 结构体成员变量说明

#### enableFastTrace

```ets
bool XEG_RTReflectionCreateInfo::enableFastTrace
```

**描述**

是否开启快速求交模式，相较常规求交模式，快速求交模式的性能更好。true表示开启快速求交模式，false表示使用常规求交模式。

#### pNext

```ets
const void* XEG_RTReflectionCreateInfo::pNext
```

**描述**

指向扩展结构的指针。

#### renderSize

```ets
VkExtent2D XEG_RTReflectionCreateInfo::renderSize
```

**描述**

输入图像的尺寸。

#### sType

```ets
XEG_StructureType XEG_RTReflectionCreateInfo::sType
```

**描述**

识别此结构的[XEG_StructureType](XEngine.md#ZH-CN_TOPIC_0000002553202223__xeg_structuretype)值，必须是XEG_STRUCTURE_TYPE_RT_REFLECTION_CREATE_INFO。
