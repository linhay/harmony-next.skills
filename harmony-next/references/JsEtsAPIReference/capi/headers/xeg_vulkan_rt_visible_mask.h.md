# xeg_vulkan_rt_visible_mask.h

#### 概述

XEngine RT VisibleMask特性接口。使用此头文件中的接口前需要通过[HMS_XEG_EnumerateDeviceExtensionProperties](../../topics/misc/XEngine.md#ZH-CN_TOPIC_0000002328319196__hms_xeg_enumeratedeviceextensionproperties)接口查询[XEG_RT_SHADOW_AO_EXTENSION_NAME](../../topics/misc/XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_rt_shadow_ao_extension_name)扩展可用。

**库：** libxengine.so

**系统能力：** SystemCapability.Graphic.XEngine

**起始版本：** 6.0.0(20)

**相关模块：**[XEngine](../../topics/misc/XEngine.md)

#### 汇总

#### 结构体

名称

描述

struct [XEG_RTShadowAOCreateInfo](../../topics/graphics/XEG_RTShadowAOCreateInfo.md)

此结构体描述创建支持光线追踪阴影和环境光遮蔽效果[XEG_RTVisibleMask](../../topics/misc/XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_rtvisiblemask)实例的初始化信息。当结构体中的信息变化时，需要创建新的[XEG_RTVisibleMask](../../topics/misc/XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_rtvisiblemask)对象。

struct [XEG_RTShadowParameters](../../topics/graphics/XEG_RTShadowParameters.md)

光线追踪阴影（Shadow）算法参数。

struct [XEG_RTAOParameters](../../topics/media/XEG_RTAOParameters.md)

光线追踪环境光遮蔽（AO）算法参数。

struct [XEG_RTShadowAODenoiserParameters](../../topics/graphics/XEG_RTShadowAODenoiserParameters.md)

光线追踪阴影和环境光遮蔽算法去噪参数。

struct [XEG_RTShadowAODescription](../../topics/graphics/XEG_RTShadowAODescription.md)

此结构体描述光线追踪阴影和环境光遮蔽算法渲染命令的输入信息。

#### 类型定义

名称

描述

VK_DEFINE_HANDLE([XEG_RTVisibleMask](../../topics/misc/XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_rtvisiblemask))

[XEG_RTVisibleMask](../../topics/misc/XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_rtvisiblemask)的句柄。表示光线追踪VisibleMask特性实例，支持阴影和环境光遮蔽效果。

typedef enum [XEG_DenoiseQualityMode](../../topics/misc/XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_denoisequalitymode) XEG_DenoiseQualityMode

去噪质量模式枚举。

typedef enum [XEG_TraversalMode](../../topics/misc/XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_traversalmode) XEG_TraversalMode

遍历模式枚举。

typedef VkResult(VKAPI_PTR * [PFN_HMS_XEG_CreateRTVisibleMask](../../topics/misc/XEngine.md#ZH-CN_TOPIC_0000002328319196__pfn_hms_xeg_creatertvisiblemask)) (VkDevice device, const void *pCreateInfo, [XEG_RTVisibleMask](../../topics/misc/XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_rtvisiblemask) *pRTVisibleMask)

创建[XEG_RTVisibleMask](../../topics/misc/XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_rtvisiblemask)对象的函数指针定义。

typedef VkResult(VKAPI_PTR * [PFN_HMS_XEG_CmdRenderRTVisibleMask](../../topics/misc/XEngine.md#ZH-CN_TOPIC_0000002328319196__pfn_hms_xeg_cmdrenderrtvisiblemask)) (VkCommandBuffer commandBuffer, [XEG_RTVisibleMask](../../topics/misc/XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_rtvisiblemask) rtVisibleMask, const void *pDescription)

录制光线追踪VisibleMask渲染命令的函数指针定义。

typedef void(VKAPI_PTR * [PFN_HMS_XEG_DestroyRTVisibleMask](../../topics/misc/XEngine.md#ZH-CN_TOPIC_0000002328319196__pfn_hms_xeg_destroyrtvisiblemask)) ([XEG_RTVisibleMask](../../topics/misc/XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_rtvisiblemask) rtVisibleMask)

销毁[XEG_RTVisibleMask](../../topics/misc/XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_rtvisiblemask)对象的函数指针定义。

#### 枚举

名称

描述

[XEG_DenoiseQualityMode](../../topics/misc/XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_denoisequalitymode) { [XEG_DENOISE_QUALITY_MODE_NONE](../../topics/misc/XEngine.md) = 0, [XEG_DENOISE_QUALITY_MODE_QUALITY](../../topics/misc/XEngine.md) = 1, [XEG_DENOISE_QUALITY_MODE_BALANCED](../../topics/misc/XEngine.md) = 2, [XEG_DENOISE_QUALITY_MODE_PERFORMANCES](../../topics/misc/XEngine.md) = 3 }

去噪质量模式枚举。

[XEG_TraversalMode](../../topics/misc/XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_traversalmode) { [XEG_TRAVERSAL_MODE_DEFAULT](../../topics/misc/XEngine.md) = 0, [XEG_TRAVERSAL_MODE_PERFORMANCES](../../topics/misc/XEngine.md) = 1 }

遍历模式枚举。

#### 函数

名称

描述

VKAPI_ATTR VkResult VKAPI_CALL [HMS_XEG_CreateRTVisibleMask](../../topics/misc/XEngine.md#ZH-CN_TOPIC_0000002328319196__hms_xeg_creatertvisiblemask) (VkDevice device, const void *pCreateInfo, [XEG_RTVisibleMask](../../topics/misc/XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_rtvisiblemask) *pRTVisibleMask)

创建[XEG_RTVisibleMask](../../topics/misc/XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_rtvisiblemask)对象。

VKAPI_ATTR VkResult VKAPI_CALL [HMS_XEG_CmdRenderRTVisibleMask](../../topics/misc/XEngine.md#ZH-CN_TOPIC_0000002328319196__hms_xeg_cmdrenderrtvisiblemask) (VkCommandBuffer commandBuffer, [XEG_RTVisibleMask](../../topics/misc/XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_rtvisiblemask) rtVisibleMask, const void *pDescription)

录制光线追踪VisibleMask渲染命令。

VKAPI_ATTR void VKAPI_CALL [HMS_XEG_DestroyRTVisibleMask](../../topics/misc/XEngine.md#ZH-CN_TOPIC_0000002328319196__hms_xeg_destroyrtvisiblemask) ([XEG_RTVisibleMask](../../topics/misc/XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_rtvisiblemask) rtVisibleMask)

销毁[XEG_RTVisibleMask](../../topics/misc/XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_rtvisiblemask)对象。