# xeg_vulkan_rtgi.h

**概述**

XEngine光线追踪全局光照特性Vulkan接口，提供动态漫反射全局光照（DDGI）及神经网络全局光照（NNGI）两种特性。使用此头文件的接口前，需要先调用[HMS_XEG_EnumerateDeviceExtensionProperties](XEngine.md#ZH-CN_TOPIC_0000002553202223__hms_xeg_enumeratedeviceextensionproperties)接口查询扩展[XEG_RTGI_EXTENSION_NAME](XEngine.md#ZH-CN_TOPIC_0000002553202223__xeg_rtgi_extension_name)可用。

引用文件：<xengine/xeg_vulkan_rtgi.h>

库： libxengine.so

系统能力： SystemCapability.Graphic.XEngine

起始版本： 6.0.0(20)

相关模块： [XEngine](XEngine.md)

**汇总**

**结构体**

| 名称 | 描述 |
| --- | --- |
| struct XEG_DDGIVolumeEntryParameters | 此结构体描述每一个DDGI体积的必要参数。 |
| struct XEG_DDGICreateInfo | 此结构体描述创建具有DDGI特性的XEG_RTGI对象的信息，当结构体中的信息变化时，需要创建新的XEG_RTGI对象。 |
| struct XEG_DDGIDescription | 此结构体描述更新DDGI探针辐照度及渲染输出GI图像所需的信息。 |
| struct XEG_NNGICreateInfo | 此结构体描述创建具有NNGI特性的XEG_RTGI对象的信息，当结构体中的信息变化时，需要创建新的XEG_RTGI对象。 |
| struct XEG_NNGIDescription | 此结构体描述更新NNGI用于计算光线追踪全局光照的所需的信息。 |

**类型定义**

| 名称 | 描述 |
| --- | --- |
| VK_DEFINE_HANDLE(XEG_RTGI) | XEG_RTGI的句柄。 |
| typedef enum XEG_RTGIQualityMode XEG_RTGIQualityMode | 输出图像质量模式的枚举。 |
| typedef VkResult(VKAPI_PTR * PFN_HMS_XEG_CreateRTGI) (VkDevice device, const void *pCreateInfo, XEG_RTGI *pRtGI) | 创建XEG_RTGI对象的函数指针定义。 |
| typedef void(VKAPI_PTR * PFN_HMS_XEG_DestroyRTGI) (XEG_RTGI rtGI) | 销毁XEG_RTGI对象的函数指针定义。 |
| typedef VkResult(VKAPI_PTR * PFN_HMS_XEG_CmdRenderRTGI) (VkCommandBuffer commandBuffer, XEG_RTGI rtGI, const void *pDescription) | 执行渲染命令的函数指针定义。 |

**枚举**

| 名称 | 描述 |
| --- | --- |
| XEG_RTGIQualityMode { XEG_RTGI_QUALITY_MODE_QUALITY = 0, XEG_RTGI_QUALITY_MODE_BALANCED = 1, XEG_RTGI_QUALITY_MODE_PERFORMANCE = 2 } | 输出图像质量模式的枚举。 |

**函数**

| 名称 | 描述 |
| --- | --- |
| VKAPI_ATTR VkResult VKAPI_CALL HMS_XEG_CreateRTGI (VkDevice device, const void *pCreateInfo, XEG_RTGI *pRtGI) | 创建XEG_RTGI对象。 |
| VKAPI_ATTR void VKAPI_CALL HMS_XEG_DestroyRTGI (XEG_RTGI rtGI) | 销毁XEG_RTGI对象。 |
| VKAPI_ATTR VkResult VKAPI_CALL HMS_XEG_CmdRenderRTGI (VkCommandBuffer commandBuffer, XEG_RTGI rtGI, const void *pDescription) | 执行渲染命令。 |