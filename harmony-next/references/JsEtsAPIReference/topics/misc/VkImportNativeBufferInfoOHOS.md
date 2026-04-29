# VkImportNativeBufferInfoOHOS

```ets
typedef struct VkImportNativeBufferInfoOHOS {...} VkImportNativeBufferInfoOHOS
```

#### 概述

包含了[OH_NativeBuffer](OH_NativeBuffer.md)结构体的指针。

**起始版本：** 10

相关模块： [Vulkan](Vulkan.md)

所在头文件： [vulkan_ohos.h](vulkan_ohos.h.md)

#### 汇总

#### 成员变量

| 名称 | 描述 |
| --- | --- |
| VkStructureType sType | 结构体类型。 |
| const void* pNext | 下一级结构体指针。 |
| struct [OH_NativeBuffer](OH_NativeBuffer.md)* buffer | OH_NativeBuffer结构体的指针。 |
