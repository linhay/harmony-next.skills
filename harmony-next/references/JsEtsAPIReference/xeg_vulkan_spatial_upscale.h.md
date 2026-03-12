# xeg_vulkan_spatial_upscale.h

#### 概述

XEngine空域GPU超分特性Vulkan接口。使用此头文件的接口前需要通过[HMS_XEG_EnumerateDeviceExtensionProperties](XEngine.md#ZH-CN_TOPIC_0000002328319196__hms_xeg_enumeratedeviceextensionproperties)接口查询[XEG_SPATIAL_UPSCALE_EXTENSION_NAME](XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_spatial_upscale_extension_name)扩展可用。

**库：** libxengine.so

**系统能力：** SystemCapability.Graphic.XEngine

**起始版本：** 5.0.0(12)

**相关模块：**[XEngine](XEngine.md)

#### 汇总

#### 结构体

名称

描述

struct [XEG_SpatialUpscaleCreateInfo](XEG_SpatialUpscaleCreateInfo.md)

此结构体描述创建[XEG_SpatialUpscale](XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_spatialupscale)对象的信息，当结构体中的信息变化时，需要创建新的[XEG_SpatialUpscale](XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_spatialupscale)对象。

struct [XEG_SpatialUpscaleDescription](XEG_SpatialUpscaleDescription.md)

此结构体描述下发空域GPU超分渲染命令时需要的图像信息。

#### 类型定义

名称

描述

VK_DEFINE_HANDLE([XEG_SpatialUpscale](XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_spatialupscale))

[XEG_SpatialUpscale](XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_spatialupscale)的句柄。

typedef struct [XEG_SpatialUpscaleCreateInfo](XEG_SpatialUpscaleCreateInfo.md) XEG_SpatialUpscaleCreateInfo

此结构体描述创建[XEG_SpatialUpscale](XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_spatialupscale)对象的信息，当结构体中的信息变化时，需要创建新的[XEG_SpatialUpscale](XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_spatialupscale)对象。

typedef struct [XEG_SpatialUpscaleDescription](XEG_SpatialUpscaleDescription.md) XEG_SpatialUpscaleDescription

此结构体描述下发空域GPU超分渲染命令时需要的图像信息。

typedef VkResult(VKAPI_PTR * [PFN_HMS_XEG_CreateSpatialUpscale](XEngine.md#ZH-CN_TOPIC_0000002328319196__pfn_hms_xeg_createspatialupscale)) (VkDevice device, const [XEG_SpatialUpscaleCreateInfo](XEG_SpatialUpscaleCreateInfo.md) *pXegSpatialUpscaleCreateInfo, [XEG_SpatialUpscale](XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_spatialupscale) *pXegSpatialUpscale)

创建[XEG_SpatialUpscale](XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_spatialupscale)对象的函数指针定义。

typedef void(VKAPI_PTR * [PFN_HMS_XEG_CmdRenderSpatialUpscale](XEngine.md#ZH-CN_TOPIC_0000002328319196__pfn_hms_xeg_cmdrenderspatialupscale)) (VkCommandBuffer commandBuffer, [XEG_SpatialUpscale](XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_spatialupscale) xegSpatialUpscale, [XEG_SpatialUpscaleDescription](XEG_SpatialUpscaleDescription.md) *pXegSpatialUpscaleDescription)

执行空域GPU超分渲染命令的函数指针定义。

typedef void(VKAPI_PTR * [PFN_HMS_XEG_DestroySpatialUpscale](XEngine.md#ZH-CN_TOPIC_0000002328319196__pfn_hms_xeg_destroyspatialupscale)) ([XEG_SpatialUpscale](XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_spatialupscale) xegSpatialUpscale)

销毁[XEG_SpatialUpscale](XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_spatialupscale)对象的函数指针定义。

#### 函数

名称

描述

VKAPI_ATTR VkResult VKAPI_CALL [HMS_XEG_CreateSpatialUpscale](XEngine.md#ZH-CN_TOPIC_0000002328319196__hms_xeg_createspatialupscale) (VkDevice device, const [XEG_SpatialUpscaleCreateInfo](XEG_SpatialUpscaleCreateInfo.md) *pXegSpatialUpscaleCreateInfo, [XEG_SpatialUpscale](XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_spatialupscale) *pXegSpatialUpscale)

创建[XEG_SpatialUpscale](XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_spatialupscale)对象。

VKAPI_ATTR void VKAPI_CALL [HMS_XEG_CmdRenderSpatialUpscale](XEngine.md#ZH-CN_TOPIC_0000002328319196__hms_xeg_cmdrenderspatialupscale) (VkCommandBuffer commandBuffer, [XEG_SpatialUpscale](XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_spatialupscale) xegSpatialUpscale, [XEG_SpatialUpscaleDescription](XEG_SpatialUpscaleDescription.md) *pXegSpatialUpscaleDescription)

执行空域GPU超分渲染命令。

VKAPI_ATTR void VKAPI_CALL [HMS_XEG_DestroySpatialUpscale](XEngine.md#ZH-CN_TOPIC_0000002328319196__hms_xeg_destroyspatialupscale) ([XEG_SpatialUpscale](XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_spatialupscale) xegSpatialUpscale)

销毁[XEG_SpatialUpscale](XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_spatialupscale)对象。