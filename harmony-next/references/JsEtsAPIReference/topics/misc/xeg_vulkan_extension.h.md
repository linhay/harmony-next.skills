# xeg_vulkan_extension.h

**概述**

XEngine扩展特性查询接口（Vulkan）。

引用文件：<xengine/xeg_vulkan_extension.h>

库： libxengine.so

系统能力： SystemCapability.Graphic.XEngine

起始版本： 5.0.0(12)

相关模块： [XEngine](XEngine.md)

**汇总**

**结构体**

| 名称 | 描述 |
| --- | --- |
| struct XEG_ExtensionProperties | 此结构体描述通过HMS_XEG_EnumerateDeviceExtensionProperties接口查询到的XEngine扩展特性集合。 |

**宏定义**

| 名称 | 描述 |
| --- | --- |
| XEG_MAX_EXTENSION_NAME_SIZE 256 | XEngine扩展特性名称支持的最大长度。 |

**类型定义**

| 名称 | 描述 |
| --- | --- |
| typedef struct XEG_ExtensionProperties XEG_ExtensionProperties | 此结构体描述通过HMS_XEG_EnumerateDeviceExtensionProperties接口查询到的XEngine扩展特性集合。 |
| typedef VkResult(VKAPI_PTR * PFN_HMS_XEG_EnumerateDeviceExtensionProperties) (VkPhysicalDevice physicalDevice, uint32_t *pPropertyCount, XEG_ExtensionProperties *pProperties) | XEngine Vulkan扩展特性查询接口函数指针定义。 |

**函数**

| 名称 | 描述 |
| --- | --- |
| VKAPI_ATTR VkResult VKAPI_CALL HMS_XEG_EnumerateDeviceExtensionProperties (VkPhysicalDevice physicalDevice, uint32_t *pPropertyCount, XEG_ExtensionProperties *pProperties) | XEngine Vulkan扩展特性查询接口。 |