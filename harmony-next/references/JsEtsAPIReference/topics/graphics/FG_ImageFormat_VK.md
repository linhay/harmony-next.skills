# FG_ImageFormat_VK

#### 概述

此结构体描述超帧输入输出图像的格式信息，该接口仅适配Vulkan图形API平台。

**起始版本：** 5.0.0(12)

**相关模块：**[GraphicsAccelerate](GraphicsAccelerate.md)

#### 汇总

#### 成员变量

名称

描述

VkFormat [inputColorFormat](FG_ImageFormat_VK.md#ZH-CN_TOPIC_0000002385157894__a09363220ef43f5006a2954d6906538f9)

真实渲染帧颜色缓冲区图像格式。

VkFormat [inputDepthStencilFormat](FG_ImageFormat_VK.md#ZH-CN_TOPIC_0000002385157894__a1e1bfcba3b16941fd78ed5ed93af7a49)

深度模板缓冲区图像格式。

VkFormat [outputColorFormat](FG_ImageFormat_VK.md#ZH-CN_TOPIC_0000002385157894__adc87ed6f09c0fd7d07d1b85af3d715bb)

预测帧缓冲区图像格式。

#### 结构体成员变量说明

#### inputColorFormat

```ets
VkFormat FG_ImageFormat_VK::inputColorFormat
```

**描述**

真实渲染帧颜色缓冲区图像格式。

#### inputDepthStencilFormat

```ets
VkFormat FG_ImageFormat_VK::inputDepthStencilFormat
```

**描述**

深度模板缓冲区图像格式。

#### outputColorFormat

```ets
VkFormat FG_ImageFormat_VK::outputColorFormat
```

**描述**

预测帧缓冲区图像格式。