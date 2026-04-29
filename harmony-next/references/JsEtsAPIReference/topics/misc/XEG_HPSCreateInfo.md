# [XEG_HPS](XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_hps)CreateInfo

#### 概述

此结构体描述创建[XEG_HPS](XEngine.md#ZH-CN_TOPIC_0000002553202223__xeg_hps)对象的信息。

**起始版本：** 6.0.0(20)

**相关模块： **[XEngine](XEngine.md)

所在头文件： [xeg_vulkan_hps.h](xeg_vulkan_hps.h.md)

#### 汇总

#### 成员变量

| 名称 | 描述 |
| --- | --- |
| [XEG_StructureType](XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_structuretype) sType | 识别此结构的XEG_StructureType值，必须是XEG_STRUCTURE_TYPE_HPS_CREATE_INFO。 |
| const void * pNext | 指向扩展结构的指针，不允许为空。表示启用的XEngine HPS扩展，如当使用[XEG_HPS_RADIX_SORT_EXTENSION_NAME](XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_hps_radix_sort_extension_name)扩展时，必须指定为[XEG_HPSRadixSort](XEG_HPSRadixSort.md)。 |

#### 结构体成员变量说明

#### pNext

```ets
const void* XEG_HPSCreateInfo::pNext
```

**描述**

指向扩展结构的指针，不允许为空。表示启用的XEngine HPS扩展，如当使用[XEG_HPS_RADIX_SORT_EXTENSION_NAME](XEngine.md#ZH-CN_TOPIC_0000002553202223__xeg_hps_radix_sort_extension_name)扩展时，必须指定为[XEG_HPSRadixSort](XEG_HPSRadixSort.md)。

#### sType

```ets
XEG_StructureType XEG_HPSCreateInfo::sType
```

**描述**

识别此结构的[XEG_StructureType](XEngine.md#ZH-CN_TOPIC_0000002553202223__xeg_structuretype)值，必须是XEG_STRUCTURE_TYPE_HPS_CREATE_INFO。
