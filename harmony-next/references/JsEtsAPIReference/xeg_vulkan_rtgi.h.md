# xeg_vulkan_rtgi.h

#### 概述

XEngine光线追踪全局光照特性Vulkan接口，提供动态漫反射全局光照（DDGI）及神经网络全局光照（NNGI）两种特性。使用此头文件的接口前，需要先调用[HMS_XEG_EnumerateDeviceExtensionProperties](XEngine.md#ZH-CN_TOPIC_0000002328319196__hms_xeg_enumeratedeviceextensionproperties)接口查询扩展[XEG_RTGI_EXTENSION_NAME](XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_rtgi_extension_name)可用。

**库：** libxengine.so

**系统能力：** SystemCapability.Graphic.XEngine

**起始版本：** 6.0.0(20)

**相关模块： **[XEngine](XEngine.md)

#### 汇总

#### 结构体

名称

描述

struct [XEG_DDGIVolumeEntryParameters](XEG_DDGIVolumeEntryParameters.md)

此结构体描述每一个DDGI体积的必要参数。

struct [XEG_DDGICreateInfo](XEG_DDGICreateInfo.md)

此结构体描述创建具有DDGI特性的[XEG_RTGI](XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_rtgi)对象的信息，当结构体中的信息变化时，需要创建新的[XEG_RTGI](XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_rtgi)对象。

struct [XEG_DDGIDescription](XEG_DDGIDescription.md)

此结构体描述更新DDGI探针辐照度及渲染输出GI图像所需的信息。

struct [XEG_NNGICreateInfo](XEG_NNGICreateInfo.md)

此结构体描述创建具有NNGI特性的[XEG_RTGI](XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_rtgi)对象的信息，当结构体中的信息变化时，需要创建新的[XEG_RTGI](XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_rtgi)对象。

struct [XEG_NNGIDescription](XEG_NNGIDescription.md)

此结构体描述更新NNGI用于计算光线追踪全局光照的所需的信息。

#### 类型定义

名称

描述

VK_DEFINE_HANDLE([XEG_RTGI](XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_rtgi))

[XEG_RTGI](XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_rtgi)的句柄。

typedef enum [XEG_RTGIQualityMode](XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_rtgiqualitymode) XEG_RTGIQualityMode

输出图像质量模式的枚举。

typedef VkResult(VKAPI_PTR * [PFN_HMS_XEG_CreateRTGI](XEngine.md#ZH-CN_TOPIC_0000002328319196__pfn_hms_xeg_creatertgi)) (VkDevice device, const void *pCreateInfo, [XEG_RTGI](XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_rtgi) *pRtGI)

创建[XEG_RTGI](XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_rtgi)对象的函数指针定义。

typedef void(VKAPI_PTR * [PFN_HMS_XEG_DestroyRTGI](XEngine.md#ZH-CN_TOPIC_0000002328319196__pfn_hms_xeg_destroyrtgi)) ([XEG_RTGI](XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_rtgi) rtGI)

销毁[XEG_RTGI](XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_rtgi)对象的函数指针定义。

typedef VkResult(VKAPI_PTR * [PFN_HMS_XEG_CmdRenderRTGI](XEngine.md#ZH-CN_TOPIC_0000002328319196__pfn_hms_xeg_cmdrenderrtgi)) (VkCommandBuffer commandBuffer, [XEG_RTGI](XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_rtgi) rtGI, const void *pDescription)

执行渲染命令的函数指针定义。

#### 枚举

名称

描述

[XEG_RTGIQualityMode](XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_rtgiqualitymode) { [XEG_RTGI_QUALITY_MODE_QUALITY](XEngine.md) = 0, [XEG_RTGI_QUALITY_MODE_BALANCED](XEngine.md) = 1, [XEG_RTGI_QUALITY_MODE_PERFORMANCE](XEngine.md) = 2 }

输出图像质量模式的枚举。

#### 函数

名称

描述

VKAPI_ATTR VkResult VKAPI_CALL [HMS_XEG_CreateRTGI](XEngine.md#ZH-CN_TOPIC_0000002328319196__hms_xeg_creatertgi) (VkDevice device, const void *pCreateInfo, [XEG_RTGI](XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_rtgi) *pRtGI)

创建[XEG_RTGI](XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_rtgi)对象。

VKAPI_ATTR void VKAPI_CALL [HMS_XEG_DestroyRTGI](XEngine.md#ZH-CN_TOPIC_0000002328319196__hms_xeg_destroyrtgi) ([XEG_RTGI](XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_rtgi) rtGI)

销毁[XEG_RTGI](XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_rtgi)对象。

VKAPI_ATTR VkResult VKAPI_CALL [HMS_XEG_CmdRenderRTGI](XEngine.md#ZH-CN_TOPIC_0000002328319196__hms_xeg_cmdrenderrtgi) (VkCommandBuffer commandBuffer, [XEG_RTGI](XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_rtgi) rtGI, const void *pDescription)

执行渲染命令。