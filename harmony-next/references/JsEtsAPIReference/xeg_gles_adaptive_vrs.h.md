# xeg_gles_adaptive_vrs.h

#### 概述

XEngine VRS特性接口。使用此头文件的接口前需要通过[HMS_XEG_GetString](XEngine.md#ZH-CN_TOPIC_0000002328319196__hms_xeg_getstring)接口查询[XEG_ADAPTIVE_VRS_EXTENSION_NAME](XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_adaptive_vrs_extension_name)扩展可用。

**系统能力：** SystemCapability.Graphic.XEngine

**库：** libxengine.so

**起始版本：** 5.0.0(12)

**相关模块： **[XEngine](XEngine.md)

#### 汇总

#### 宏定义

名称

描述

[XEG_ADAPTIVE_VRS_INPUT_SIZE](XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_adaptive_vrs_input_size) 0x1U

用于设置[HMS_XEG_AdaptiveVRSParameter](XEngine.md#ZH-CN_TOPIC_0000002328319196__hms_xeg_adaptivevrsparameter)接口的INPUT_SIZE参数，表示上一帧渲染管线最终渲染的图像宽度和高度。

[XEG_ADAPTIVE_VRS_INPUT_REGION](XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_adaptive_vrs_input_region) 0x2U

用于设置[HMS_XEG_AdaptiveVRSParameter](XEngine.md#ZH-CN_TOPIC_0000002328319196__hms_xeg_adaptivevrsparameter)接口的INPUT_REGION参数，表示上一帧渲染管线最终渲染的图像区域。

[XEG_ADAPTIVE_VRS_TEXEL_SIZE](XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_adaptive_vrs_texel_size) 0x3U

用于设置[HMS_XEG_AdaptiveVRSParameter](XEngine.md#ZH-CN_TOPIC_0000002328319196__hms_xeg_adaptivevrsparameter)接口的TEXEL_SIZE参数。

[XEG_ADAPTIVE_VRS_ERROR_SENSITIVITY](XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_adaptive_vrs_error_sensitivity) 0x4U

用于设置[HMS_XEG_AdaptiveVRSParameter](XEngine.md#ZH-CN_TOPIC_0000002328319196__hms_xeg_adaptivevrsparameter)接口的ERROR_SENSITIVITY参数，表示控制生成着色率图像的阈值。该值越大，平均着色率越小，即性能会越好但画质会劣化。建议取值范围为[0, 1]。

[XEG_ADAPTIVE_VRS_FLIP](XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_adaptive_vrs_flip) 0x5U

用于设置[HMS_XEG_AdaptiveVRSParameter](XEngine.md#ZH-CN_TOPIC_0000002328319196__hms_xeg_adaptivevrsparameter)接口的FLIP参数，该参数用于控制是否执行图像上下翻转。

#### 类型定义

名称

描述

typedef void(GL_APIENTRYP [PFN_HMS_XEG_ADAPTIVEVRSPARAMETER](XEngine.md#ZH-CN_TOPIC_0000002328319196__pfn_hms_xeg_adaptivevrsparameter)) (GLenum pname, GLvoid *param)

设置自适应VRS输入参数的函数指针定义。

typedef void(GL_APIENTRYP [PFN_HMS_XEG_DISPATCHADAPTIVEVRS](XEngine.md#ZH-CN_TOPIC_0000002328319196__pfn_hms_xeg_dispatchadaptivevrs)) (GLfloat *reprojectionMatrix, GLuint inputColorImage, GLuint inputDepthImage, GLuint shadingRateImage)

计算着色率图像的函数指针定义。

typedef void(GL_APIENTRYP [PFN_HMS_XEG_APPLYADAPTIVEVRS](XEngine.md#ZH-CN_TOPIC_0000002328319196__pfn_hms_xeg_applyadaptivevrs)) (GLuint shadingRateImage)

将着色率图像应用到渲染目标中的函数指针定义。

#### 函数

名称

描述

GL_APICALL void GL_APIENTRY [HMS_XEG_AdaptiveVRSParameter](XEngine.md#ZH-CN_TOPIC_0000002328319196__hms_xeg_adaptivevrsparameter) (GLenum pname, GLvoid *param)

设置自适应VRS的参数。

GL_APICALL void GL_APIENTRY [HMS_XEG_DispatchAdaptiveVRS](XEngine.md#ZH-CN_TOPIC_0000002328319196__hms_xeg_dispatchadaptivevrs) (GLfloat *reprojectionMatrix, GLuint inputColorImage, GLuint inputDepthImage, GLuint shadingRateImage)

计算着色率图像。

GL_APICALL void GL_APIENTRY [HMS_XEG_ApplyAdaptiveVRS](XEngine.md#ZH-CN_TOPIC_0000002328319196__hms_xeg_applyadaptivevrs) (GLuint shadingRateImage)

将着色率图像应用到渲染目标中。