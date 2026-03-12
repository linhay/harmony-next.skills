# VkMemoryGetNativeBufferInfoOHOS

```ets
typedef struct VkMemoryGetNativeBufferInfoOHOS {...} VkMemoryGetNativeBufferInfoOHOS
```

#### 概述

用于从Vulkan内存中获取OH_NativeBuffer。

**起始版本：** 10

**相关模块：**[Vulkan](Vulkan.md)

**所在头文件：**[vulkan_ohos.h](vulkan_ohos.h.md)

#### 汇总

#### 成员变量

名称描述VkStructureType sType结构体类型，值必须为VK_STRUCTURE_TYPE_MEMORY_GET_NATIVE_BUFFER_INFO_OHOS。const void* pNext下一级结构体指针，值必须为空。VkDeviceMemory memoryVkDeviceMemory对象，值必须为一个有效的VkDeviceMemory对象。