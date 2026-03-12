# xeg_vulkan_rt_reflection.h

#### 概述

XEngine RT Reflection特性接口。使用此头文件中的接口前需要通过[HMS_XEG_EnumerateDeviceExtensionProperties](XEngine.md#ZH-CN_TOPIC_0000002328319196__hms_xeg_enumeratedeviceextensionproperties)接口查询 [XEG_RT_REFLECTION_EXTENSION_NAME](XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_rt_reflection_extension_name)扩展可用。

**库：** libxengine.so

**系统能力：** SystemCapability.Graphic.XEngine

**起始版本：** 6.0.0(20)

**相关模块： **[XEngine](XEngine.md)

#### 汇总

#### 结构体

名称

描述

struct [XEG_RTReflectionCreateInfo](XEG_RTReflectionCreateInfo.md)

此结构体描述创建[XEG_RTReflection](XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_rtreflection)对象的信息。当结构体中的信息变化时，需要创建新的[XEG_RTReflection](XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_rtreflection)对象。

struct [XEG_RTReflectionDescription](XEG_RTReflectionDescription.md)

此结构体描述下发光线求交命令时的输入信息。

#### 类型定义

名称

描述

VK_DEFINE_HANDLE([XEG_RTReflection](XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_rtreflection))

[XEG_RTReflection](XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_rtreflection)的句柄。

typedef struct [XEG_RTReflectionCreateInfo](XEG_RTReflectionCreateInfo.md) XEG_RTReflectionCreateInfo

此结构体描述创建[XEG_RTReflection](XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_rtreflection)对象的信息。当结构体中的信息变化时，需要创建新的[XEG_RTReflection](XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_rtreflection)对象。

typedef struct [XEG_RTReflectionDescription](XEG_RTReflectionDescription.md) XEG_RTReflectionDescription

此结构体描述下发光线求交命令时的输入信息。

typedef VkResult(VKAPI_ATTR * [PFN_HMS_XEG_CreateRTReflection](XEngine.md#ZH-CN_TOPIC_0000002328319196__pfn_hms_xeg_creatertreflection)) (VkDevice device, const void *pCreateInfo, [XEG_RTReflection](XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_rtreflection) *pRtReflection)

创建[XEG_RTReflection](XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_rtreflection)对象的函数指针定义。

typedef VkResult (VKAPI_ATTR *[PFN_HMS_XEG_CmdRenderRTReflection](XEngine.md#ZH-CN_TOPIC_0000002328319196__pfn_hms_xeg_cmdrenderrtreflection))(VkCommandBuffer commandBuffer, [XEG_RTReflection](XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_rtreflection) rtReflection, const void *pDescription)

录制计算RT反射命中信息命令的函数指针定义。

typedef void (VKAPI_ATTR *[PFN_HMS_XEG_DestroyRTReflection](XEngine.md#ZH-CN_TOPIC_0000002328319196__pfn_hms_xeg_destroyrtreflection))([XEG_RTReflection](XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_rtreflection) rtReflection)

销毁[XEG_RTReflection](XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_rtreflection)对象的函数指针定义。

#### 函数

名称

描述

VKAPI_ATTR VkResult VKAPI_CALL [HMS_XEG_CreateRTReflection](XEngine.md#ZH-CN_TOPIC_0000002328319196__hms_xeg_creatertreflection) (VkDevice device, const void *pCreateInfo, [XEG_RTReflection](XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_rtreflection) *pRtReflection)

创建[XEG_RTReflection](XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_rtreflection)对象。

VKAPI_ATTR VkResult VKAPI_CALL [HMS_XEG_CmdRenderRTReflection](XEngine.md#ZH-CN_TOPIC_0000002328319196__hms_xeg_cmdrenderrtreflection) (VkCommandBuffer commandBuffer, [XEG_RTReflection](XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_rtreflection) rtReflection, const void *pDescription)

录制计算RT反射命中信息命令。

VKAPI_ATTR void VKAPI_CALL [HMS_XEG_DestroyRTReflection](XEngine.md#ZH-CN_TOPIC_0000002328319196__hms_xeg_destroyrtreflection) ([XEG_RTReflection](XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_rtreflection) rtReflection)

销毁[XEG_RTReflection](XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_rtreflection)对象。