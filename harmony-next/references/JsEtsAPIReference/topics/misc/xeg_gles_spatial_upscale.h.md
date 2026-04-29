# xeg_gles_spatial_upscale.h

**概述**

XEngine空域GPU超分特性OpenGL ES接口。使用此头文件的接口前需要通过[HMS_XEG_GetString](XEngine.md#ZH-CN_TOPIC_0000002553202223__hms_xeg_getstring)接口查询[XEG_SPATIAL_UPSCALE_EXTENSION_NAME](XEngine.md#ZH-CN_TOPIC_0000002553202223__xeg_spatial_upscale_extension_name)扩展可用。

引用文件：<xengine/xeg_gles_spatial_upscale.h>

库： libxengine.so

系统能力： SystemCapability.Graphic.XEngine

起始版本： 5.0.0(12)

相关模块： [XEngine](XEngine.md)

**汇总**

**宏定义**

| 名称 | 描述 |
| --- | --- |
| XEG_SPATIAL_UPSCALE_SCISSOR 0x1U | 用于设置HMS_XEG_SpatialUpscaleParameter接口的SCISSOR参数。 |
| XEG_SPATIAL_UPSCALE_SHARPNESS 0x2U | 用于设置HMS_XEG_SpatialUpscaleParameter接口的SHARPNESS参数。 |

**类型定义**

| 名称 | 描述 |
| --- | --- |
| typedef void(GL_APIENTRYP PFN_HMS_XEG_SPATIALUPSCALEPARAMETER) (GLenum pname, GLvoid *param) | 设置空域GPU超分输入参数的函数指针定义。 |
| typedef void(GL_APIENTRYP PFN_HMS_XEG_RENDERSPATIALUPSCALE) (GLuint inputTexture) | 执行空域GPU超分渲染命令的函数指针定义。 |

**函数**

| 名称 | 描述 |
| --- | --- |
| GL_APICALL void GL_APIENTRY HMS_XEG_SpatialUpscaleParameter (GLenum pname, GLvoid *param) | 设置空域GPU超分输入参数。 |
| GL_APICALL void GL_APIENTRY HMS_XEG_RenderSpatialUpscale (GLuint inputTexture) | 执行空域GPU超分渲染命令。 |