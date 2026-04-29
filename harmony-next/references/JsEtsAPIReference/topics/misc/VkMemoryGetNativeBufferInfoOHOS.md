# VkMemoryGetNativeBufferInfoOHOS

```ets
typedef struct VkMemoryGetNativeBufferInfoOHOS {...} VkMemoryGetNativeBufferInfoOHOS
```

#### 概述

用于从[Vulkan](Vulkan.md)内存中获取OH_NativeBuffer。

**起始版本：** 10

相关模块： [Vulkan](Vulkan.md)

所在头文件： [vulkan_ohos.h](vulkan_ohos.h.md)

#### 汇总

#### 成员变量

| 名称 | 描述 |
| --- | --- |
| VkStructureType sType | 结构体类型，值必须为VK_STRUCTURE_TYPE_MEMORY_GET_NATIVE_BUFFER_INFO_OHOS。 |
| const void* pNext | 下一级结构体指针，值必须为空。 |
| VkDeviceMemory memory | VkDeviceMemory对象，值必须为一个有效的VkDeviceMemory对象。 |