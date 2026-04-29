# XEG_HPSRadixSortDescription

#### 概述

此结构体描述使用[XEG_HPS_RADIX_SORT_EXTENSION_NAME](XEngine.md#ZH-CN_TOPIC_0000002553202223__xeg_hps_radix_sort_extension_name)扩展进行排序时所需的信息。

**起始版本：** 6.0.0(20)

**相关模块：**[XEngine](XEngine.md)

所在头文件： [xeg_vulkan_hps.h](xeg_vulkan_hps.h.md)

#### 汇总

#### 成员变量

| 名称 | 描述 |
| --- | --- |
| [XEG_StructureType](XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_structuretype) sType | 识别此结构的XEG_StructureType值，必须是XEG_STRUCTURE_TYPE_HPS_RADIX_SORT_DESCRIPTION。 |
| const void * pNext | 指向扩展结构的指针。 |
| VkBuffer sortCount | 存储要排序的索引数量的缓冲区，数量值从缓冲区第0位读取。 |
| VkBuffer keyBuffer | 存储排序使用的key值的缓冲区，数据格式为32位无符号整数。 |
| VkBuffer indexBuffer | 存储待排序value值的缓冲区，数据格式为32位无符号整数。 |

#### 结构体成员变量说明

#### indexBuffer

```ets
VkBuffer XEG_HPSRadixSortDescription::indexBuffer
```

**描述**

存储待排序value值的缓冲区，数据格式为32位无符号整数。

#### keyBuffer

```ets
VkBuffer XEG_HPSRadixSortDescription::keyBuffer
```

**描述**

存储排序使用的key值的缓冲区，数据格式为32位无符号整数。

#### pNext

```ets
const void* XEG_HPSRadixSortDescription::pNext
```

**描述**

指向扩展结构的指针。

#### sortCount

```ets
VkBuffer XEG_HPSRadixSortDescription::sortCount
```

**描述**

存储要排序的索引数量的缓冲区，数量值从缓冲区第0位读取。

#### sType

```ets
XEG_StructureType XEG_HPSRadixSortDescription::sType
```

**描述**

识别此结构的[XEG_StructureType](XEngine.md#ZH-CN_TOPIC_0000002553202223__xeg_structuretype)值，必须是XEG_STRUCTURE_TYPE_HPS_RADIX_SORT_DESCRIPTION。
