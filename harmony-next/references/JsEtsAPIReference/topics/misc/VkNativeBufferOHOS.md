# VkNativeBufferOHOS

```ets
typedef struct VkNativeBufferOHOS {...} VkNativeBufferOHOS
```

**概述**

包含本地显存的参数。

起始版本： 10

相关模块： [Vulkan](Vulkan.md)

所在头文件： [vulkan_ohos.h](vulkan_ohos.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| VkStructureType sType | 结构体类型。 |
| const void* pNext | 下一级结构体指针，pNext为空或者下一级结构体指针。 |
| struct OHBufferHandle* handle | 显存句柄。 |