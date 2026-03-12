# FG_ContextDescription_VK

#### 概述

此结构体描述创建超帧上下文实例[FG_Context_VK](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga4022ab63c2296d63dcf2c2df178508b7)所需的属性信息。

**起始版本：** 5.0.0(12)

**相关模块：**[GraphicsAccelerate](GraphicsAccelerate.md)

#### 汇总

#### 成员变量

名称

描述

VkInstance [vkInstance](FG_ContextDescription_VK.md#ZH-CN_TOPIC_0000002385157870__a8743dce62193ecfaffb7eff178f2a877)

Vulkan实例，需在[FG_Context_VK](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga4022ab63c2296d63dcf2c2df178508b7)的整个生命周期内有效。

VkPhysicalDevice [vkPhysicalDevice](FG_ContextDescription_VK.md#ZH-CN_TOPIC_0000002385157870__a4237948c43a0da8fbb0bc2278b0027f9)

Vulkan物理设备句柄, 需在[FG_Context_VK](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga4022ab63c2296d63dcf2c2df178508b7)的整个生命周期内有效。

VkDevice [vkDevice](FG_ContextDescription_VK.md#ZH-CN_TOPIC_0000002385157870__a484ba219df54c20302d07f0aa27129ed)

Vulkan逻辑设备句柄，需在[FG_Context_VK](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga4022ab63c2296d63dcf2c2df178508b7)的整个生命周期内有效。

uint8_t [framesInFlight](FG_ContextDescription_VK.md#ZH-CN_TOPIC_0000002385157870__a31b5b649ec9ac22013ad2f24b136cc3a)

设置并行渲染图像数。例如，如果下一帧图像需要等待上一帧图像送显后再进行渲染，则framesInFlight应设置为1；如果上一帧图像送显的同时，下一帧图像已经在进行渲染，则framesInFlight应设置为2。注意：framesInFlight不允许设置成0。

取值范围：[1, 2]。

PFN_vkGetInstanceProcAddr [fnVulkanLoaderFunction](FG_ContextDescription_VK.md#ZH-CN_TOPIC_0000002385157870__a83cf228e483f5a26ff0022a3dea788f3)

指向Vulkan的vkGetInstanceProcAddr的函数指针，不允许设置为空。

#### 结构体成员变量说明

#### fnVulkanLoaderFunction

```ets
PFN_vkGetInstanceProcAddr FG_ContextDescription_VK::fnVulkanLoaderFunction
```

**描述**

指向Vulkan的vkGetInstanceProcAddr的函数指针，不允许设置为空。

#### framesInFlight

```ets
uint8_t FG_ContextDescription_VK::framesInFlight
```

**描述**

设置并行渲染图像数。 例如，如果下一帧图像需要等待上一帧图像送显后再进行渲染，则framesInFlight应设置为1； 如果上一帧图像送显的同时，下一帧图像已经在进行渲染，则framesInFlight应设置为2。注意：framesInFlight不允许设置成0。

#### vkDevice

```ets
VkDevice FG_ContextDescription_VK::vkDevice
```

**描述**

Vulkan逻辑设备句柄，需在[FG_Context_VK](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga4022ab63c2296d63dcf2c2df178508b7)的整个生命周期内有效。

#### vkInstance

```ets
VkInstance FG_ContextDescription_VK::vkInstance
```

**描述**

Vulkan实例, 需在[FG_Context_VK](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga4022ab63c2296d63dcf2c2df178508b7)的整个生命周期内有效。

#### vkPhysicalDevice

```ets
VkPhysicalDevice FG_ContextDescription_VK::vkPhysicalDevice
```

**描述**

Vulkan物理设备句柄, 需在[FG_Context_VK](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga4022ab63c2296d63dcf2c2df178508b7)的整个生命周期内有效。