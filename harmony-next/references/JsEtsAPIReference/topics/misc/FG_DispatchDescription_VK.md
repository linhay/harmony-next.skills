# FG_DispatchDescription_VK

#### 概述

此结构体描述下发帧生成命令[HMS_FG_Dispatch_VK](../graphics/GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga21f86a194e72e99dd54fd39080385a37)需要的参数信息，每一帧都需要进行更新。该接口仅适配Vulkan图形API平台。

**起始版本：** 5.0.0(12)

**相关模块：**[GraphicsAccelerate](../graphics/GraphicsAccelerate.md)

#### 汇总

#### 成员变量

名称

描述

[FG_ImageInfo_VK](../graphics/FG_ImageInfo_VK.md)[inputColorInfo](FG_DispatchDescription_VK.md#ZH-CN_TOPIC_0000002385317766__a7578dc22d86211692bc10f03d3e6bd80)

真实渲染帧颜色缓冲区图像实例，该图像实例由[HMS_FG_CreateImage_VK](../graphics/GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga7733f097ea5f4ae4d2aa53d11d7e60ff)创建，由[HMS_FG_DestroyImage_VK](../graphics/GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gac850c7cd41a1aebaf9bcf943ebff372a)销毁。

[FG_ImageInfo_VK](../graphics/FG_ImageInfo_VK.md)[inputDepthStencilInfo](FG_DispatchDescription_VK.md#ZH-CN_TOPIC_0000002385317766__a8d769ac5e41a27c668d32e0819895de5)

真实渲染帧深度模板缓冲区图像实例，该图像实例由[HMS_FG_CreateImage_VK](../graphics/GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga7733f097ea5f4ae4d2aa53d11d7e60ff)创建，由[HMS_FG_DestroyImage_VK](../graphics/GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gac850c7cd41a1aebaf9bcf943ebff372a)销毁。

[FG_ImageInfo_VK](../graphics/FG_ImageInfo_VK.md)[outputColorInfo](FG_DispatchDescription_VK.md#ZH-CN_TOPIC_0000002385317766__a50597ac7da9fc3292f0ebc1a9e36157c)

预测帧缓冲区图像实例 ，该图像实例由[HMS_FG_CreateImage_VK](../graphics/GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga7733f097ea5f4ae4d2aa53d11d7e60ff)创建，由[HMS_FG_DestroyImage_VK](../graphics/GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gac850c7cd41a1aebaf9bcf943ebff372a)销毁。

[FG_Mat4x4](FG_Mat4x4.md)[viewProj](FG_DispatchDescription_VK.md#ZH-CN_TOPIC_0000002385317766__abfad453e18fe901b2e7539b96e45a02a)

真实渲染帧视图投影矩阵，即世界空间到相机裁剪空间坐标系转换矩阵，矩阵必须是4x4列主序的矩阵。

[FG_Mat4x4](FG_Mat4x4.md)[invViewProj](FG_DispatchDescription_VK.md#ZH-CN_TOPIC_0000002385317766__a2edcff364646e5bd4506e96a6e6fd863)

真实渲染帧视图投影逆矩阵，即相机裁剪空间到世界空间坐标系转换矩阵，矩阵必须是4x4列主序的矩阵。

VkCommandBuffer [vkCommandBuffer](FG_DispatchDescription_VK.md#ZH-CN_TOPIC_0000002385317766__a4c42121e915c5293c142f0737ff242d3)

用于录入超帧绘制指令的命令缓冲区。

uint8_t [frameIdx](FG_DispatchDescription_VK.md#ZH-CN_TOPIC_0000002385317766__acffef3d1baef878cd923ec2e1709c80b)

当前帧序号，序号计数从0开始。该值必须小于[FG_ContextDescription_VK](../graphics/FG_ContextDescription_VK.md)中的framesInFlight。

#### 结构体成员变量说明

#### frameIdx

```ets
uint8_t FG_DispatchDescription_VK::frameIdx
```

**描述**

当前帧序号，序号计数从0开始。该值必须小于[FG_ContextDescription_VK](../graphics/FG_ContextDescription_VK.md)中的framesInFlight。

#### inputColorInfo

```ets
[FG_ImageInfo_VK](../graphics/FG_ImageInfo_VK.md) FG_DispatchDescription_VK::inputColorInfo
```

**描述**

真实渲染帧颜色缓冲图像实例，该图像实例由[HMS_FG_CreateImage_VK](../graphics/GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga7733f097ea5f4ae4d2aa53d11d7e60ff)创建，由[HMS_FG_DestroyImage_VK](../graphics/GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gac850c7cd41a1aebaf9bcf943ebff372a)销毁。

#### inputDepthStencilInfo

```ets
[FG_ImageInfo_VK](../graphics/FG_ImageInfo_VK.md) FG_DispatchDescription_VK::inputDepthStencilInfo
```

**描述**

真实渲染帧深度模板缓冲区图像实例，该图像实例由[HMS_FG_CreateImage_VK](../graphics/GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga7733f097ea5f4ae4d2aa53d11d7e60ff)创建，由[HMS_FG_DestroyImage_VK](../graphics/GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gac850c7cd41a1aebaf9bcf943ebff372a)销毁。

#### invViewProj

```ets
[FG_Mat4x4](FG_Mat4x4.md) FG_DispatchDescription_VK::invViewProj
```

**描述**

真实渲染帧视图投影逆矩阵，即相机裁剪空间到世界空间坐标系转换矩阵，矩阵必须是4x4列主序的矩阵。

#### outputColorInfo

```ets
[FG_ImageInfo_VK](../graphics/FG_ImageInfo_VK.md) FG_DispatchDescription_VK::outputColorInfo
```

**描述**

预测帧缓冲区图像实例，该图像实例由[HMS_FG_CreateImage_VK](../graphics/GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga7733f097ea5f4ae4d2aa53d11d7e60ff)创建，由[HMS_FG_DestroyImage_VK](../graphics/GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gac850c7cd41a1aebaf9bcf943ebff372a)销毁。

#### viewProj

```ets
[FG_Mat4x4](FG_Mat4x4.md) FG_DispatchDescription_VK::viewProj
```

**描述**

真实渲染帧视图投影矩阵，即世界空间到相机裁剪空间坐标系转换矩阵，矩阵必须是4x4列主序的矩阵。

#### vkCommandBuffer

```ets
VkCommandBuffer FG_DispatchDescription_VK::vkCommandBuffer
```

**描述**

用于录入超帧绘制指令的命令缓冲区。