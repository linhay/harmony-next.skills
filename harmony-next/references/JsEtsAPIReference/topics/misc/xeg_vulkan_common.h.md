# xeg_vulkan_common.h

**概述**

包含XEngine中Vulkan相关的通用类型定义。

引用文件：<xengine/xeg_vulkan_common.h>

库： libxengine.so

系统能力： SystemCapability.Graphic.XEngine

起始版本： 6.0.0(20)

相关模块： [XEngine](XEngine.md)

**汇总**

**类型定义**

| 名称 | 描述 |
| --- | --- |
| typedef enum XEG_StructureType XEG_StructureType | XEngine结构体类型的枚举。 |
| typedef VkResult(VKAPI_PTR * PFN_HMS_XEG_CmdSetSynchronization) (VkCommandBuffer commandBuffer, const void *xegHandle) | 设置同步信号，等待渲染结果写入指定图像的函数指针定义。使用RTGI特性时，为等待GI渲染结果到写入指定图像。 |

**枚举**

| 名称 | 描述 |
| --- | --- |
| XEG_StructureType { XEG_STRUCTURE_TYPE_RT_SHADOWAO_CREATE_INFO = 0, XEG_STRUCTURE_TYPE_RT_SHADOWAO_DESCRIPTION = 1, XEG_STRUCTURE_TYPE_RT_REFLECTION_CREATE_INFO = 2, XEG_STRUCTURE_TYPE_RT_REFLECTION_DESCRIPTION = 3, XEG_STRUCTURE_TYPE_NNGI_CREATE_INFO = 4, XEG_STRUCTURE_TYPE_NNGI_DESCRIPTION = 5, XEG_STRUCTURE_TYPE_DDGI_CREATE_INFO = 6, XEG_STRUCTURE_TYPE_DDGI_DESCRIPTION = 7, XEG_STRUCTURE_TYPE_HPS_CREATE_INFO = 1001, XEG_STRUCTURE_TYPE_HPS_RADIX_SORT = 1002, XEG_STRUCTURE_TYPE_HPS_RADIX_SORT_DESCRIPTION = 1003 } | XEngine结构体类型的枚举。 |

**函数**

| 名称 | 描述 |
| --- | --- |
| VKAPI_ATTR VkResult VKAPI_CALL HMS_XEG_CmdSetSynchronization (VkCommandBuffer commandBuffer, const void *xegHandle) | 设置同步信号，等待渲染结果写入指定图像。使用RTGI特性时，为等待GI渲染结果写入指定图像。 |