# VkSurfaceCreateInfoOHOS

```ets
typedef struct VkSurfaceCreateInfoOHOS {...} VkSurfaceCreateInfoOHOS
```

#### 概述

包含创建[Vulkan](Vulkan.md) Surface时必要的参数。

**起始版本：** 10

相关模块： [Vulkan](Vulkan.md)

所在头文件： [vulkan_ohos.h](vulkan_ohos.h.md)

#### 汇总

#### 成员变量

| 名称 | 描述 |
| --- | --- |
| VkStructureType sType | 结构体类型，值必须为VK_STRUCTURE_TYPE_SURFACE_CREATE_INFO_OHOS。 |
| const void* pNext | 下一级结构体指针，值必须为空。 |
| VkSurfaceCreateFlagsOHOS flags | 预留的标志类型参数，值必须为0。 |
| [OHNativeWindow](NativeWindow.md)* window | OHNativeWindow指针。 |
