# xeg_vulkan_rt_reflection.h

**概述**

XEngine RT Reflection特性接口。使用此头文件中的接口前需要通过[HMS_XEG_EnumerateDeviceExtensionProperties](XEngine.md#ZH-CN_TOPIC_0000002553202223__hms_xeg_enumeratedeviceextensionproperties)接口查询 [XEG_RT_REFLECTION_EXTENSION_NAME](XEngine.md#ZH-CN_TOPIC_0000002553202223__xeg_rt_reflection_extension_name)扩展可用。

引用文件：<xengine/xeg_vulkan_rt_reflection.h>

库： libxengine.so

系统能力： SystemCapability.Graphic.XEngine

起始版本： 6.0.0(20)

相关模块： [XEngine](XEngine.md)

**汇总**

**结构体**

| 名称 | 描述 |
| --- | --- |
| struct XEG_RTReflectionCreateInfo | 此结构体描述创建XEG_RTReflection对象的信息。当结构体中的信息变化时，需要创建新的XEG_RTReflection对象。 |
| struct XEG_RTReflectionDescription | 此结构体描述下发光线求交命令时的输入信息。 |

**类型定义**

| 名称 | 描述 |
| --- | --- |
| VK_DEFINE_HANDLE(XEG_RTReflection) | XEG_RTReflection的句柄。 |
| typedef struct XEG_RTReflectionCreateInfo XEG_RTReflectionCreateInfo | 此结构体描述创建XEG_RTReflection对象的信息。当结构体中的信息变化时，需要创建新的XEG_RTReflection对象。 |
| typedef struct XEG_RTReflectionDescription XEG_RTReflectionDescription | 此结构体描述下发光线求交命令时的输入信息。 |
| typedef VkResult(VKAPI_ATTR * PFN_HMS_XEG_CreateRTReflection) (VkDevice device, const void *pCreateInfo, XEG_RTReflection *pRtReflection) | 创建XEG_RTReflection对象的函数指针定义。 |
| typedef VkResult (VKAPI_ATTR *PFN_HMS_XEG_CmdRenderRTReflection)(VkCommandBuffer commandBuffer, XEG_RTReflection rtReflection, const void *pDescription) | 录制计算RT反射命中信息命令的函数指针定义。 |
| typedef void (VKAPI_ATTR *PFN_HMS_XEG_DestroyRTReflection)(XEG_RTReflection rtReflection) | 销毁XEG_RTReflection对象的函数指针定义。 |

**函数**

| 名称 | 描述 |
| --- | --- |
| VKAPI_ATTR VkResult VKAPI_CALL HMS_XEG_CreateRTReflection (VkDevice device, const void *pCreateInfo, XEG_RTReflection *pRtReflection) | 创建XEG_RTReflection对象。 |
| VKAPI_ATTR VkResult VKAPI_CALL HMS_XEG_CmdRenderRTReflection (VkCommandBuffer commandBuffer, XEG_RTReflection rtReflection, const void *pDescription) | 录制计算RT反射命中信息命令。 |
| VKAPI_ATTR void VKAPI_CALL HMS_XEG_DestroyRTReflection (XEG_RTReflection rtReflection) | 销毁XEG_RTReflection对象。 |