# XEG_HPSRadixSort

#### 概述

此结构体描述HPS基数排序扩展结构信息。

**起始版本：** 6.0.0(20)

**相关模块：**[XEngine](XEngine.md)

#### 汇总

#### 成员变量

名称

描述

XEG_StructureType [sType](#ZH-CN_TOPIC_0000002362157645__stype)

识别此结构的[XEG_StructureType](XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_structuretype)值，必须是[XEG_STRUCTURE_TYPE_HPS_RADIX_SORT](XEngine.md)。

const void * [pNext](#ZH-CN_TOPIC_0000002362157645__pnext)

指向扩展结构的指针。

#### 结构体成员变量说明

#### pNext

```ets
const void* XEG_HPSRadixSort::pNext
```

**描述**

指向扩展结构的指针。

#### sType

```ets
XEG_StructureType XEG_HPSRadixSort::sType
```

**描述**

识别此结构的[XEG_StructureType](XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_structuretype)值，必须是[XEG_STRUCTURE_TYPE_HPS_RADIX_SORT](XEngine.md)。