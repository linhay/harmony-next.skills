# xeg_vulkan_hps.h

#### 概述

XEngine 高性能着色器接口。使用此头文件中的接口前需要通过[HMS_XEG_EnumerateDeviceExtensionProperties](../../topics/misc/XEngine.md#ZH-CN_TOPIC_0000002328319196__hms_xeg_enumeratedeviceextensionproperties)接口查询[XEG_HPS_RADIX_SORT_EXTENSION_NAME](../../topics/misc/XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_hps_radix_sort_extension_name)扩展可用。

**库：** libxengine.so

**系统能力：** SystemCapability.Graphic.XEngine

**起始版本：** 6.0.0(20)

**相关模块：**[XEngine](../../topics/misc/XEngine.md)

#### 汇总

#### 结构体

名称

描述

struct [XEG_HPSCreateInfo](../../topics/misc/XEG_HPSCreateInfo.md)

此结构体描述创建[XEG_HPS](../../topics/misc/XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_hps)对象的信息。

struct [XEG_HPSRadixSort](../../topics/misc/XEG_HPSRadixSort.md)

此结构体描述HPS基数排序扩展结构信息。

struct [XEG_HPSRadixSortDescription](../../topics/misc/XEG_HPSRadixSortDescription.md)

此结构体描述使用[XEG_HPS_RADIX_SORT_EXTENSION_NAME](../../topics/misc/XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_hps_radix_sort_extension_name)扩展进行排序时所需的信息。

#### 类型定义

名称

描述

VK_DEFINE_HANDLE([XEG_HPS](../../topics/misc/XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_hps))

[XEG_HPS](../../topics/misc/XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_hps)的句柄。

typedef struct [XEG_HPSCreateInfo](../../topics/misc/XEG_HPSCreateInfo.md)[XEG_HPSCreateInfo](../../topics/misc/XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_hpscreateinfo)

此结构体描述创建[XEG_HPS](../../topics/misc/XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_hps)对象的信息。

typedef struct [XEG_HPSRadixSort](../../topics/misc/XEG_HPSRadixSort.md)[XEG_HPSRadixSort](../../topics/misc/XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_hpsradixsort)

此结构体描述HPS基数排序扩展结构信息。

typedef struct [XEG_HPSRadixSortDescription](../../topics/misc/XEG_HPSRadixSortDescription.md)[XEG_HPSRadixSortDescription](../../topics/misc/XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_hpsradixsortdescription)

此结构体描述使用[XEG_HPS_RADIX_SORT_EXTENSION_NAME](../../topics/misc/XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_hps_radix_sort_extension_name)扩展进行排序时所需的信息。

typedef VkResult(VKAPI_PTR * [PFN_HMS_XEG_CreateHPS](../../topics/misc/XEngine.md#ZH-CN_TOPIC_0000002328319196__pfn_hms_xeg_createhps)) (VkDevice device, const [XEG_HPSCreateInfo](../../topics/misc/XEG_HPSCreateInfo.md) *pCreateInfo, [XEG_HPS](../../topics/misc/XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_hps) *pHps)

创建[XEG_HPS](../../topics/misc/XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_hps)对象的函数指针定义。

typedef void(VKAPI_PTR * [PFN_HMS_XEG_DestroyHPS](../../topics/misc/XEngine.md#ZH-CN_TOPIC_0000002328319196__pfn_hms_xeg_destroyhps)) ([XEG_HPS](../../topics/misc/XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_hps) hps)

销毁[XEG_HPS](../../topics/misc/XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_hps)对象的函数指针定义。

typedef VkResult(VKAPI_PTR * [PFN_HMS_XEG_CmdRadixSortHPS](../../topics/misc/XEngine.md#ZH-CN_TOPIC_0000002328319196__pfn_hms_xeg_cmdradixsorthps)) (VkCommandBuffer commandBuffer, [XEG_HPS](../../topics/misc/XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_hps) hps, const [XEG_HPSRadixSortDescription](../../topics/misc/XEG_HPSRadixSortDescription.md) *pDescription)

录制HPS排序命令的函数指针定义，使用此接口前需要通过[HMS_XEG_EnumerateDeviceExtensionProperties](../../topics/misc/XEngine.md#ZH-CN_TOPIC_0000002328319196__hms_xeg_enumeratedeviceextensionproperties)接口查询是否支持[XEG_HPS_RADIX_SORT_EXTENSION_NAME](../../topics/misc/XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_hps_radix_sort_extension_name)扩展。

#### 函数

名称

描述

VKAPI_ATTR VkResult VKAPI_CALL [HMS_XEG_CreateHPS](../../topics/misc/XEngine.md#ZH-CN_TOPIC_0000002328319196__hms_xeg_createhps) (VkDevice device, const [XEG_HPSCreateInfo](../../topics/misc/XEG_HPSCreateInfo.md) *pCreateInfo, [XEG_HPS](../../topics/misc/XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_hps) *pHps)

创建[XEG_HPS](../../topics/misc/XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_hps)对象。

VKAPI_ATTR void VKAPI_CALL [HMS_XEG_DestroyHPS](../../topics/misc/XEngine.md#ZH-CN_TOPIC_0000002328319196__hms_xeg_destroyhps) ([XEG_HPS](../../topics/misc/XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_hps) hps)

销毁[XEG_HPS](../../topics/misc/XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_hps)对象。

VKAPI_ATTR VkResult VKAPI_CALL [HMS_XEG_CmdRadixSortHPS](../../topics/misc/XEngine.md#ZH-CN_TOPIC_0000002328319196__hms_xeg_cmdradixsorthps) (VkCommandBuffer commandBuffer, [XEG_HPS](../../topics/misc/XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_hps) hps, const [XEG_HPSRadixSortDescription](../../topics/misc/XEG_HPSRadixSortDescription.md) *pDescription)

录制HPS排序命令，使用此接口前需要通过[HMS_XEG_EnumerateDeviceExtensionProperties](../../topics/misc/XEngine.md#ZH-CN_TOPIC_0000002328319196__hms_xeg_enumeratedeviceextensionproperties)接口查询是否支持[XEG_HPS_RADIX_SORT_EXTENSION_NAME](../../topics/misc/XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_hps_radix_sort_extension_name)扩展。