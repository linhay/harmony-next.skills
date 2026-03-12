# xeg_gles_neural_upscale.h

#### 概述

XEngine空域AI超分特性OpenGL ES接口，推荐超分倍率为[1.0, 1.5]。使用此头文件中的接口前需要通过[HMS_XEG_GetString](XEngine.md#ZH-CN_TOPIC_0000002328319196__hms_xeg_getstring)接口查询[XEG_NEURAL_UPSCALE_EXTENSION_NAME](XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_neural_upscale_extension_name)扩展可用。

**系统能力：** SystemCapability.Graphic.XEngine

**库：** libxengine.so

**起始版本：** 5.0.0(12)

**相关模块： **[XEngine](XEngine.md)

#### 汇总

#### 宏定义

名称

描述

[XEG_NEURAL_UPSCALE_SCISSOR](XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_neural_upscale_scissor) 0x1U

用于通过[HMS_XEG_NeuralUpscaleParameter](XEngine.md#ZH-CN_TOPIC_0000002328319196__hms_xeg_neuralupscaleparameter)接口设置超分的裁剪窗口参数，裁剪窗口用于确定对输入图像采样的区域。

[XEG_NEURAL_UPSCALE_SHARPNESS](XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_neural_upscale_sharpness) 0x2U

用于通过[HMS_XEG_NeuralUpscaleParameter](XEngine.md#ZH-CN_TOPIC_0000002328319196__hms_xeg_neuralupscaleparameter)接口设置超分的锐化度参数，锐化度的建议取值范围为[0, 1]。

[XEG_NEURAL_UPSCALE_INPUT_HANDLE](XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_neural_upscale_input_handle) 0x4U

用于通过[HMS_XEG_NeuralUpscaleParameter](XEngine.md#ZH-CN_TOPIC_0000002328319196__hms_xeg_neuralupscaleparameter)接口设置与超分输入纹理关联的OH_NativeBuffer handle。

#### 类型定义

名称

描述

typedef void(GL_APIENTRYP [PFN_HMS_XEG_NEURALUPSCALEPARAMETER](XEngine.md#ZH-CN_TOPIC_0000002328319196__pfn_hms_xeg_neuralupscaleparameter)) (GLenum pname, GLvoid *param)

设置空域AI超分输入参数的函数指针定义。

typedef void(GL_APIENTRYP [PFN_HMS_XEG_RENDERNEURALUPSCALE](XEngine.md#ZH-CN_TOPIC_0000002328319196__pfn_hms_xeg_renderneuralupscale)) (GLuint inputTexture)

执行空域AI超分渲染命令的函数指针定义。

#### 函数

名称

描述

GL_APICALL void GL_APIENTRY [HMS_XEG_NeuralUpscaleParameter](XEngine.md#ZH-CN_TOPIC_0000002328319196__hms_xeg_neuralupscaleparameter) (GLenum pname, GLvoid *param)

设置空域AI超分输入参数。

GL_APICALL void GL_APIENTRY [HMS_XEG_RenderNeuralUpscale](XEngine.md#ZH-CN_TOPIC_0000002328319196__hms_xeg_renderneuralupscale) (GLuint inputTexture)

执行空域AI超分渲染命令。