# FG_ImageFormat_VK

**概述**

此结构体描述超帧输入输出图像的格式信息，该接口仅适配Vulkan图形API平台。

起始版本： 5.0.0(12)

相关模块： [GraphicsAccelerate](GraphicsAccelerate.md)

所在头文件： [frame_generation_vk.h](frame_generation_vk.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| VkFormat inputColorFormat | 真实渲染帧颜色缓冲区图像格式。 |
| VkFormat inputDepthStencilFormat | 深度模板缓冲区图像格式。 |
| VkFormat outputColorFormat | 预测帧缓冲区图像格式。 |

**结构体成员变量说明**

**inputColorFormat**

```ets
VkFormat FG_ImageFormat_VK::inputColorFormat
```

描述

真实渲染帧颜色缓冲区图像格式。

**inputDepthStencilFormat**

```ets
VkFormat FG_ImageFormat_VK::inputDepthStencilFormat
```

描述

深度模板缓冲区图像格式。

**outputColorFormat**

```ets
VkFormat FG_ImageFormat_VK::outputColorFormat
```

描述

预测帧缓冲区图像格式。