# VkNativeBufferUsageOHOS

```ets
typedef struct VkNativeBufferUsageOHOS {...} VkNativeBufferUsageOHOS
```

#### 概述

提供HarmonyOS NativeBuffer用途的说明。

**起始版本：** 10

**相关模块：**[Vulkan](Vulkan.md)

**所在头文件：**[vulkan_ohos.h](vulkan_ohos.h.md)

#### 汇总

#### 成员变量

名称描述VkStructureType sType结构体类型，值必须为VK_STRUCTURE_TYPE_NATIVE_BUFFER_USAGE_OHOS。void* pNext下一级结构体指针。uint64_t OHOSNativeBufferUsageNativeBuffer的用途说明。