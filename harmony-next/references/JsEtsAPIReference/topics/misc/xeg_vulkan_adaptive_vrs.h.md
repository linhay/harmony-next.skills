# xeg_vulkan_adaptive_vrs.h

**概述**

XEngine Adaptive VRS特性Vulkan接口。使用此头文件的接口前需要通过[HMS_XEG_EnumerateDeviceExtensionProperties](XEngine.md#ZH-CN_TOPIC_0000002553202223__hms_xeg_enumeratedeviceextensionproperties)接口查询[XEG_ADAPTIVE_VRS_EXTENSION_NAME](XEngine.md#ZH-CN_TOPIC_0000002553202223__xeg_adaptive_vrs_extension_name)扩展可用。

引用文件：<xengine/xeg_vulkan_adaptive_vrs.h>

库： libxengine.so

系统能力： SystemCapability.Graphic.XEngine

起始版本： 5.0.0(12)

相关模块： [XEngine](XEngine.md)

**汇总**

**结构体**

| 名称 | 描述 |
| --- | --- |
| struct XEG_AdaptiveVRSCreateInfo | 此结构体描述创建XEG_AdaptiveVRS对象的参数信息，当结构体中的信息变化时，需要创建新的XEG_AdaptiveVRS对象。 |
| struct XEG_AdaptiveVRSDescription | 此结构体描述下发绘制着色率纹理命令需要的参数信息，每一帧都需要进行更新。 |

**类型定义**

| 名称 | 描述 |
| --- | --- |
| VK_DEFINE_HANDLE(XEG_AdaptiveVRS) | XEG_AdaptiveVRS的句柄。 |
| typedef struct XEG_AdaptiveVRSCreateInfo XEG_AdaptiveVRSCreateInfo | 此结构体描述创建XEG_AdaptiveVRS对象的参数信息，当结构体中的信息变化时，需要创建新的XEG_AdaptiveVRS对象。 |
| typedef struct XEG_AdaptiveVRSDescription XEG_AdaptiveVRSDescription | 此结构体描述下发绘制着色率纹理命令需要的参数信息，每一帧都需要进行更新。 |
| typedef VkResult(VKAPI_PTR * PFN_HMS_XEG_CreateAdaptiveVRS) (VkDevice device, const XEG_AdaptiveVRSCreateInfo *pXegAdaptiveVRSCreateInfo, XEG_AdaptiveVRS *pXegAdaptiveVRS) | 创建XEG_AdaptiveVRS对象的函数指针定义。 |
| typedef void(VKAPI_PTR * PFN_HMS_XEG_CmdDispatchAdaptiveVRS) (VkCommandBuffer commandBuffer, XEG_AdaptiveVRS xegAdaptiveVRS, XEG_AdaptiveVRSDescription *pXegAdaptiveVRSDescription) | 执行计算自适应可变着色率命令的函数指针定义。 |
| typedef void(VKAPI_PTR * PFN_HMS_XEG_DestroyAdaptiveVRS) (XEG_AdaptiveVRS xegAdaptiveVRS) | 销毁XEG_AdaptiveVRS对象的函数指针定义。 |

**函数**

| 名称 | 描述 |
| --- | --- |
| VKAPI_ATTR VkResult VKAPI_CALL HMS_XEG_CreateAdaptiveVRS (VkDevice device, XEG_AdaptiveVRSCreateInfo *pXegAdaptiveVRSCreateInfo, XEG_AdaptiveVRS *pXegAdaptiveVRS) | 创建XEG_AdaptiveVRS对象。 |
| VKAPI_ATTR void VKAPI_CALL HMS_XEG_CmdDispatchAdaptiveVRS (VkCommandBuffer commandBuffer, XEG_AdaptiveVRS xegAdaptiveVRS, XEG_AdaptiveVRSDescription *pXegAdaptiveVRSDescription) | 执行计算自适应可变着色率命令。 |
| VKAPI_ATTR void VKAPI_CALL HMS_XEG_DestroyAdaptiveVRS (XEG_AdaptiveVRS xegAdaptiveVRS) | 销毁XEG_AdaptiveVRS对象。 |