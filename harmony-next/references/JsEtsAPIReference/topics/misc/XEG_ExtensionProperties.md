# XEG_ExtensionProperties

#### 概述

此结构体描述通过[HMS_XEG_EnumerateDeviceExtensionProperties](XEngine.md#ZH-CN_TOPIC_0000002553202223__hms_xeg_enumeratedeviceextensionproperties)接口查询到的XEngine扩展特性集合。

**起始版本：** 5.0.0(12)

**相关模块： **[XEngine](XEngine.md)

所在头文件： [xeg_vulkan_extension.h](xeg_vulkan_extension.h.md)

#### 汇总

#### 成员变量

| 名称 | 描述 |
| --- | --- |
| char extensionName [[XEG_MAX_EXTENSION_NAME_SIZE](XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_max_extension_name_size)] | XEngine支持的扩展特性名称。 |
| uint32_t version | XEngine支持的扩展特性版本号。 |

#### 结构体成员变量说明

#### extensionName

```ets
char XEG_ExtensionProperties::extensionName[XEG_MAX_EXTENSION_NAME_SIZE]
```

**描述**

XEngine支持的扩展特性名称。

#### version

```ets
uint32_t XEG_ExtensionProperties::version
```

**描述**

XEngine支持的扩展特性版本号。
