# VkSurfaceCreateInfoOHOS

```ets
typedef struct VkSurfaceCreateInfoOHOS {...} VkSurfaceCreateInfoOHOS
```

#### 概述

包含创建Vulkan Surface时必要的参数。

**起始版本：** 10

**相关模块：**[Vulkan](../media/Vulkan.md)

**所在头文件：**[vulkan_ohos.h](../../capi/headers/vulkan_ohos.h.md)

#### 汇总

#### 成员变量

名称描述VkStructureType sType结构体类型，值必须为VK_STRUCTURE_TYPE_SURFACE_CREATE_INFO_OHOS。const void* pNext下一级结构体指针，值必须为空。VkSurfaceCreateFlagsOHOS flags预留的标志类型参数，值必须为0。[OHNativeWindow](NativeWindow.md)* windowOHNativeWindow指针。