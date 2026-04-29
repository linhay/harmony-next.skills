# FG_DispatchDescription_GLES

#### 概述

此结构体描述下发帧生成命令[HMS_FG_Dispatch_GLES](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002522242234__hms_fg_dispatch_gles)需要的参数信息，每一帧都需要进行更新。该接口仅适配OpenGL ES图形API平台。

**起始版本：** 5.0.0(12)

相关模块： [GraphicsAccelerate](GraphicsAccelerate.md)

所在头文件： [frame_generation_gles.h](frame_generation_gles.h.md)

#### 汇总

#### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint32_t [inputColor](FG_DispatchDescription_GLES.md#ZH-CN_TOPIC_0000002385317758__a91056017b03b30a68df9018ce8e7b676) | 真实渲染帧颜色缓冲区索引，支持格式包括GL_RGBA8、GL_R11F_G11F_B10F、GL_RGBA16F。 取值范围：[0, 2^32 -1]。 |
| uint32_t [inputDepthStencil](FG_DispatchDescription_GLES.md#ZH-CN_TOPIC_0000002385317758__a39d8ea5f2f685328f3d309f14e445e39) | 真实渲染帧深度模板缓冲区索引，支持格式包括GL_DEPTH24_STENCIL8、GL_DEPTH32F_STENCIL8。 取值范围：[0, 2^32 -1]。 |
| [FG_Mat4x4](FG_Mat4x4.md) [viewProj](FG_DispatchDescription_GLES.md#ZH-CN_TOPIC_0000002385317758__a46bffa3d279f60171488a6e4c0c8436d) | 真实渲染帧视图投影矩阵，即世界空间到相机裁剪空间坐标系转换矩阵，矩阵必须是4x4列主序的矩阵。 |
| FG_Mat4x4 [invViewProj](FG_DispatchDescription_GLES.md#ZH-CN_TOPIC_0000002385317758__a03c61b50406beb0d0c9e7a7fa50fcf02) | 真实渲染帧逆视图投影矩阵，即相机裁剪空间到世界空间坐标系转换矩阵，矩阵必须是4x4列主序的矩阵。 |
| uint32_t [outputColor](FG_DispatchDescription_GLES.md#ZH-CN_TOPIC_0000002385317758__ad4c32e775aa14015a7b1e31530d7c9ab) | 预测帧缓冲区索引，此预测帧缓冲区需要用户创建并输入，支持格式包括GL_RGBA8、GL_R11F_G11F_B10F、GL_RGBA16F。 取值范围：[0, 2^32 -1]。 |

#### 结构体成员变量说明

#### [inputColor](FG_DispatchDescription_GLES.md#ZH-CN_TOPIC_0000002385317758__a91056017b03b30a68df9018ce8e7b676)

```ets
uint32_t FG_DispatchDescription_GLES::inputColor
```

**描述**

真实渲染帧颜色缓冲区索引，支持格式包括GL_RGBA8、GL_R11F_G11F_B10F、GL_RGBA16F。

#### [inputDepthStencil](FG_DispatchDescription_GLES.md#ZH-CN_TOPIC_0000002385317758__a39d8ea5f2f685328f3d309f14e445e39)

```ets
uint32_t FG_DispatchDescription_GLES::inputDepthStencil
```

**描述**

真实渲染帧深度模板缓冲区索引，支持格式包括GL_DEPTH24_STENCIL8、GL_DEPTH32F_STENCIL8。

#### [invViewProj](FG_DispatchDescription_GLES.md#ZH-CN_TOPIC_0000002385317758__a03c61b50406beb0d0c9e7a7fa50fcf02)

```ets
[FG_Mat4x4](FG_Mat4x4.md) FG_DispatchDescription_GLES::invViewProj
```

**描述**

真实渲染帧逆视图投影矩阵，即相机裁剪空间到世界空间坐标系转换矩阵，矩阵必须是4x4列主序的矩阵。

#### [outputColor](FG_DispatchDescription_GLES.md#ZH-CN_TOPIC_0000002385317758__ad4c32e775aa14015a7b1e31530d7c9ab)

```ets
uint32_t FG_DispatchDescription_GLES::outputColor
```

**描述**

预测帧缓冲区索引，此预测帧缓冲区需要用户创建并输入，支持格式包括GL_RGBA8、GL_R11F_G11F_B10F、GL_RGBA16F。

#### [viewProj](FG_DispatchDescription_GLES.md#ZH-CN_TOPIC_0000002385317758__a46bffa3d279f60171488a6e4c0c8436d)

```ets
[FG_Mat4x4](FG_Mat4x4.md) FG_DispatchDescription_GLES::viewProj
```

**描述**

真实渲染帧视图投影矩阵，即世界空间到相机裁剪空间坐标系转换矩阵，矩阵必须是4x4列主序的矩阵。
