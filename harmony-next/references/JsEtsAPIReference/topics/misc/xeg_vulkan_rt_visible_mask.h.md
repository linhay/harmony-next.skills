# xeg_vulkan_rt_visible_mask.h

**概述**

XEngine RT VisibleMask特性接口。使用此头文件中的接口前需要通过[HMS_XEG_EnumerateDeviceExtensionProperties](XEngine.md#ZH-CN_TOPIC_0000002553202223__hms_xeg_enumeratedeviceextensionproperties)接口查询[XEG_RT_SHADOW_AO_EXTENSION_NAME](XEngine.md#ZH-CN_TOPIC_0000002553202223__xeg_rt_shadow_ao_extension_name)扩展可用。

引用文件：<xengine/xeg_vulkan_rt_visible_mask.h>

库： libxengine.so

系统能力： SystemCapability.Graphic.XEngine

起始版本： 6.0.0(20)

相关模块： [XEngine](XEngine.md)

**汇总**

**结构体**

| 名称 | 描述 |
| --- | --- |
| struct XEG_RTShadowAOCreateInfo | 此结构体描述创建支持光线追踪阴影和环境光遮蔽效果XEG_RTVisibleMask实例的初始化信息。当结构体中的信息变化时，需要创建新的XEG_RTVisibleMask对象。 |
| struct XEG_RTShadowParameters | 光线追踪阴影（Shadow）算法参数。 |
| struct XEG_RTAOParameters | 光线追踪环境光遮蔽（AO）算法参数。 |
| struct XEG_RTShadowAODenoiserParameters | 光线追踪阴影和环境光遮蔽算法去噪参数。 |
| struct XEG_RTShadowAODescription | 此结构体描述光线追踪阴影和环境光遮蔽算法渲染命令的输入信息。 |

**类型定义**

| 名称 | 描述 |
| --- | --- |
| VK_DEFINE_HANDLE(XEG_RTVisibleMask) | XEG_RTVisibleMask的句柄。表示光线追踪VisibleMask特性实例，支持阴影和环境光遮蔽效果。 |
| typedef enum XEG_DenoiseQualityMode XEG_DenoiseQualityMode | 去噪质量模式枚举。 |
| typedef enum XEG_TraversalMode XEG_TraversalMode | 遍历模式枚举。 |
| typedef VkResult(VKAPI_PTR * PFN_HMS_XEG_CreateRTVisibleMask) (VkDevice device, const void *pCreateInfo, XEG_RTVisibleMask *pRTVisibleMask) | 创建XEG_RTVisibleMask对象的函数指针定义。 |
| typedef VkResult(VKAPI_PTR * PFN_HMS_XEG_CmdRenderRTVisibleMask) (VkCommandBuffer commandBuffer, XEG_RTVisibleMask rtVisibleMask, const void *pDescription) | 录制光线追踪VisibleMask渲染命令的函数指针定义。 |
| typedef void(VKAPI_PTR * PFN_HMS_XEG_DestroyRTVisibleMask) (XEG_RTVisibleMask rtVisibleMask) | 销毁XEG_RTVisibleMask对象的函数指针定义。 |

**枚举**

| 名称 | 描述 |
| --- | --- |
| XEG_DenoiseQualityMode { XEG_DENOISE_QUALITY_MODE_NONE = 0, XEG_DENOISE_QUALITY_MODE_QUALITY = 1, XEG_DENOISE_QUALITY_MODE_BALANCED = 2, XEG_DENOISE_QUALITY_MODE_PERFORMANCES = 3 } | 去噪质量模式枚举。 |
| XEG_TraversalMode { XEG_TRAVERSAL_MODE_DEFAULT = 0, XEG_TRAVERSAL_MODE_PERFORMANCES = 1 } | 遍历模式枚举。 |

**函数**

| 名称 | 描述 |
| --- | --- |
| VKAPI_ATTR VkResult VKAPI_CALL HMS_XEG_CreateRTVisibleMask (VkDevice device, const void *pCreateInfo, XEG_RTVisibleMask *pRTVisibleMask) | 创建XEG_RTVisibleMask对象。 |
| VKAPI_ATTR VkResult VKAPI_CALL HMS_XEG_CmdRenderRTVisibleMask (VkCommandBuffer commandBuffer, XEG_RTVisibleMask rtVisibleMask, const void *pDescription) | 录制光线追踪VisibleMask渲染命令。 |
| VKAPI_ATTR void VKAPI_CALL HMS_XEG_DestroyRTVisibleMask (XEG_RTVisibleMask rtVisibleMask) | 销毁XEG_RTVisibleMask对象。 |