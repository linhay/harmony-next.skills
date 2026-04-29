# VkExternalFormatOHOS

```ets
typedef struct VkExternalFormatOHOS {...} VkExternalFormatOHOS
```

#### 概述

表示外部定义的格式标识符。

**起始版本：** 10

相关模块： [Vulkan](Vulkan.md)

所在头文件： [vulkan_ohos.h](vulkan_ohos.h.md)

#### 汇总

#### 成员变量

| 名称 | 描述 |
| --- | --- |
| VkStructureType sType | 结构体类型，值必须为VK_STRUCTURE_TYPE_EXTERNAL_FORMAT_OHOS。 |
| void* pNext | pNext为空或者下一级结构体指针。 |
| uint64_t externalFormat | 外部定义的格式标识符。 |