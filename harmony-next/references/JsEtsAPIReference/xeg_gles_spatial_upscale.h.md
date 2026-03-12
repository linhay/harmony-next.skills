# xeg_gles_spatial_upscale.h

#### 概述

XEngine空域GPU超分特性OpenGL ES接口。使用此头文件的接口前需要通过[HMS_XEG_GetString](XEngine.md#ZH-CN_TOPIC_0000002328319196__hms_xeg_getstring)接口查询[XEG_SPATIAL_UPSCALE_EXTENSION_NAME](XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_spatial_upscale_extension_name)扩展可用。

**库：** libxengine.so

**系统能力：** SystemCapability.Graphic.XEngine

**起始版本：** 5.0.0(12)

**相关模块： **[XEngine](XEngine.md)

#### 汇总

#### 宏定义

名称

描述

[XEG_SPATIAL_UPSCALE_SCISSOR](XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_spatial_upscale_scissor) 0x1U

用于设置[HMS_XEG_SpatialUpscaleParameter](XEngine.md#ZH-CN_TOPIC_0000002328319196__hms_xeg_spatialupscaleparameter)接口的SCISSOR参数。

[XEG_SPATIAL_UPSCALE_SHARPNESS](XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_spatial_upscale_sharpness) 0x2U

用于设置[HMS_XEG_SpatialUpscaleParameter](XEngine.md#ZH-CN_TOPIC_0000002328319196__hms_xeg_spatialupscaleparameter)接口的SHARPNESS参数。

#### 类型定义

名称

描述

typedef void(GL_APIENTRYP [PFN_HMS_XEG_SPATIALUPSCALEPARAMETER](XEngine.md#ZH-CN_TOPIC_0000002328319196__pfn_hms_xeg_spatialupscaleparameter)) (GLenum pname, GLvoid *param)

设置空域GPU超分输入参数的函数指针定义。

typedef void(GL_APIENTRYP [PFN_HMS_XEG_RENDERSPATIALUPSCALE](XEngine.md#ZH-CN_TOPIC_0000002328319196__pfn_hms_xeg_renderspatialupscale)) (GLuint inputTexture)

执行空域GPU超分渲染命令的函数指针定义。

#### 函数

名称

描述

GL_APICALL void GL_APIENTRY [HMS_XEG_SpatialUpscaleParameter](XEngine.md#ZH-CN_TOPIC_0000002328319196__hms_xeg_spatialupscaleparameter) (GLenum pname, GLvoid *param)

设置空域GPU超分输入参数。

GL_APICALL void GL_APIENTRY [HMS_XEG_RenderSpatialUpscale](XEngine.md#ZH-CN_TOPIC_0000002328319196__hms_xeg_renderspatialupscale) (GLuint inputTexture)

执行空域GPU超分渲染命令。