# VkNativeBufferUsageOHOS

```ets
typedef struct VkNativeBufferUsageOHOS {...} VkNativeBufferUsageOHOS
```

#### 概述

提供HarmonyOS NativeBuffer用途的说明。

**起始版本：** 10

相关模块： [Vulkan](Vulkan.md)

所在头文件： [vulkan_ohos.h](vulkan_ohos.h.md)

#### 汇总

#### 成员变量

| 名称 | 描述 |
| --- | --- |
| VkStructureType sType | 结构体类型，值必须为VK_STRUCTURE_TYPE_NATIVE_BUFFER_USAGE_OHOS。 |
| void* pNext | 下一级结构体指针。 |
| uint64_t OHOSNativeBufferUsage | NativeBuffer的用途说明。 |