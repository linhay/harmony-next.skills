# xeg_gles_temporal_upscale.h

#### 概述

XEngine时域AI超分特性OpenGL ES接口。推荐超分倍率为[1.25, 2.0]，使用此头文件中的接口前需要通过[HMS_XEG_GetString](XEngine.md#ZH-CN_TOPIC_0000002328319196__hms_xeg_getstring)接口查询[XEG_TEMPORAL_UPSCALE_EXTENSION_NAME](XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_temporal_upscale_extension_name)扩展可用。

**库：** libxengine.so

**起始版本：** 6.0.0(20)

**相关模块：**[XEngine](XEngine.md)

#### 汇总

#### 宏定义

名称

描述

[XEG_TEMPORAL_UPSCALE_INPUT_SIZE](XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_temporal_upscale_input_size) 0x1U

用于通过[HMS_XEG_TemporalUpscaleParameter](XEngine.md#ZH-CN_TOPIC_0000002328319196__hms_xeg_temporalupscaleparameter)接口设置超分输入纹理的真实宽高。

[XEG_TEMPORAL_UPSCALE_JITTER_NUM](XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_temporal_upscale_jitter_num) 0x2U

用于通过[HMS_XEG_TemporalUpscaleParameter](XEngine.md#ZH-CN_TOPIC_0000002328319196__hms_xeg_temporalupscaleparameter)接口设置相机抖动的周期数，取值范围为[4, 16]，推荐8。

[XEG_TEMPORAL_UPSCALE_DEPTH_REVERSED](XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_temporal_upscale_depth_reversed) 0x3U

用于通过[HMS_XEG_TemporalUpscaleParameter](XEngine.md#ZH-CN_TOPIC_0000002328319196__hms_xeg_temporalupscaleparameter)接口设置是否存在深度反转。true表示存在深度反转，false表示不存在深度反转。

[XEG_TEMPORAL_UPSCALE_RESET_HISTORY](XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_temporal_upscale_reset_history) 0x4U

用于通过[HMS_XEG_TemporalUpscaleParameter](XEngine.md#ZH-CN_TOPIC_0000002328319196__hms_xeg_temporalupscaleparameter)接口设置是否重置历史帧数据，true表示重置，false表示不重置。在历史帧未使用超分，并且当前帧开始使用超分的情况下建议设置为true。

[XEG_TEMPORAL_UPSCALE_STEADY_LEVEL](XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_temporal_upscale_steady_level) 0x5U

用于通过[HMS_XEG_TemporalUpscaleParameter](XEngine.md#ZH-CN_TOPIC_0000002328319196__hms_xeg_temporalupscaleparameter)接口设置画面偏向当前帧（鬼影少但可能存在闪烁）还是历史帧（鬼影多但是更稳定）的平衡程度。取值范围为[0.0, 1.0]，值越大越偏向历史帧。

#### 类型定义

名称

描述

typedef void(GL_APIENTRYP [PFN_HMS_XEG_TemporalUpscaleParameter](XEngine.md#ZH-CN_TOPIC_0000002328319196__pfn_hms_xeg_temporalupscaleparameter)) (GLenum pname, GLvoid *param)

设置时域AI超分输入参数的函数指针定义。

typedef void(GL_APIENTRYP [PFN_HMS_XEG_RenderTemporalUpscale](XEngine.md#ZH-CN_TOPIC_0000002328319196__pfn_hms_xeg_rendertemporalupscale)) (GLuint inputTexture, GLuint depthTexture, GLuint motionVectorTexture, GLuint dynamicMaskTexture, GLfloat jitterX, GLfloat jitterY)

执行时域AI超分渲染命令的函数指针定义。

#### 函数

名称

描述

GL_APICALL void GL_APIENTRY [HMS_XEG_TemporalUpscaleParameter](XEngine.md#ZH-CN_TOPIC_0000002328319196__hms_xeg_temporalupscaleparameter) (GLenum pname, const GLvoid *param)

设置时域AI超分输入参数。

GL_APICALL void GL_APIENTRY [HMS_XEG_RenderTemporalUpscale](XEngine.md#ZH-CN_TOPIC_0000002328319196__hms_xeg_rendertemporalupscale) (GLuint inputTexture, GLuint depthTexture, GLuint motionVectorTexture, GLuint dynamicMaskTexture, GLfloat jitterX, GLfloat jitterY)

执行时域AI超分渲染命令。