# xeg_vulkan_temporal_upscale.h

#### 概述

XEngine时域AI超分特性接口，推荐超分倍率为[1.25, 2.0]。使用此头文件中的接口前需要通过[HMS_XEG_EnumerateDeviceExtensionProperties](XEngine.md#ZH-CN_TOPIC_0000002328319196__hms_xeg_enumeratedeviceextensionproperties)接口查询[XEG_TEMPORAL_UPSCALE_EXTENSION_NAME](XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_temporal_upscale_extension_name)扩展可用。

**库：** libxengine.so

**系统能力：** SystemCapability.Graphic.XEngine

**起始版本：** 5.0.0(12)

**相关模块： **[XEngine](XEngine.md)

#### 汇总

#### 结构体

名称

描述

struct [XEG_TemporalUpscaleCreateInfo](XEG_TemporalUpscaleCreateInfo.md)

此结构体描述创建[XEG_TemporalUpscale](XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_temporalupscale)对象的信息。当结构体中的信息变化时，需要创建新的[XEG_TemporalUpscale](XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_temporalupscale)对象。

struct [XEG_TemporalUpscaleDescription](XEG_TemporalUpscaleDescription.md)

此结构体描述下发时域AI超分渲染命令时的输入信息。

#### 类型定义

名称

描述

VK_DEFINE_HANDLE([XEG_TemporalUpscale](XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_temporalupscale))

[XEG_TemporalUpscale](XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_temporalupscale)的句柄。

typedef struct [XEG_TemporalUpscaleCreateInfo](XEG_TemporalUpscaleCreateInfo.md) XEG_TemporalUpscaleCreateInfo

此结构体描述创建[XEG_TemporalUpscale](XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_temporalupscale)对象的信息。当结构体中的信息变化时，需要创建新的[XEG_TemporalUpscale](XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_temporalupscale)对象。

typedef struct [XEG_TemporalUpscaleDescription](XEG_TemporalUpscaleDescription.md) XEG_TemporalUpscaleDescription

此结构体描述下发时域AI超分渲染命令时的输入信息。

typedef VkResult(VKAPI_ATTR * [PFN_HMS_XEG_CreateTemporalUpscale](XEngine.md#ZH-CN_TOPIC_0000002328319196__pfn_hms_xeg_createtemporalupscale)) (VkDevice device, [XEG_TemporalUpscaleCreateInfo](XEG_TemporalUpscaleCreateInfo.md) *pTemporalUpscaleInfo, [XEG_TemporalUpscale](XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_temporalupscale) *pTemporalUpscale)

创建[XEG_TemporalUpscale](XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_temporalupscale)对象的函数指针定义。

typedef void(VKAPI_ATTR * [PFN_HMS_XEG_CmdRenderTemporalUpscale](XEngine.md#ZH-CN_TOPIC_0000002328319196__pfn_hms_xeg_cmdrendertemporalupscale)) (VkCommandBuffer commandBuffer, [XEG_TemporalUpscale](XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_temporalupscale) temporalUpscale, [XEG_TemporalUpscaleDescription](XEG_TemporalUpscaleDescription.md) *pDescription)

录制时域AI超分渲染命令的函数指针定义。

typedef void(VKAPI_ATTR * [PFN_HMS_XEG_DestroyTemporalUpscale](XEngine.md#ZH-CN_TOPIC_0000002328319196__pfn_hms_xeg_destroytemporalupscale)) ([XEG_TemporalUpscale](XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_temporalupscale) temporalUpscale)

销毁[XEG_TemporalUpscale](XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_temporalupscale)对象的函数指针定义。

#### 函数

名称

描述

VKAPI_ATTR VkResult VKAPI_CALL [HMS_XEG_CreateTemporalUpscale](XEngine.md#ZH-CN_TOPIC_0000002328319196__hms_xeg_createtemporalupscale) (VkDevice device, [XEG_TemporalUpscaleCreateInfo](XEG_TemporalUpscaleCreateInfo.md) *pTemporalUpscaleInfo, [XEG_TemporalUpscale](XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_temporalupscale) *pTemporalUpscale)

创建[XEG_TemporalUpscale](XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_temporalupscale)对象。

VKAPI_ATTR void VKAPI_CALL [HMS_XEG_CmdRenderTemporalUpscale](XEngine.md#ZH-CN_TOPIC_0000002328319196__hms_xeg_cmdrendertemporalupscale) (VkCommandBuffer commandBuffer, [XEG_TemporalUpscale](XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_temporalupscale) temporalUpscale, [XEG_TemporalUpscaleDescription](XEG_TemporalUpscaleDescription.md) *pDescription)

录制时域AI超分渲染命令。

VKAPI_ATTR void VKAPI_CALL [HMS_XEG_DestroyTemporalUpscale](XEngine.md#ZH-CN_TOPIC_0000002328319196__hms_xeg_destroytemporalupscale) ([XEG_TemporalUpscale](XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_temporalupscale) temporalUpscale)

销毁[XEG_TemporalUpscale](XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_temporalupscale)对象。