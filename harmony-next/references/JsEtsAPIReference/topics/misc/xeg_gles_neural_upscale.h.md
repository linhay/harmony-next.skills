# xeg_gles_neural_upscale.h

**概述**

XEngine空域AI超分特性OpenGL ES接口，推荐超分倍率为[1.0, 1.5]。使用此头文件中的接口前需要通过[HMS_XEG_GetString](XEngine.md#ZH-CN_TOPIC_0000002553202223__hms_xeg_getstring)接口查询[XEG_NEURAL_UPSCALE_EXTENSION_NAME](XEngine.md#ZH-CN_TOPIC_0000002553202223__xeg_neural_upscale_extension_name)扩展可用。

引用文件：<xengine/xeg_gles_neural_upscale.h>

库： libxengine.so

系统能力： SystemCapability.Graphic.XEngine

起始版本： 5.0.0(12)

相关模块： [XEngine](XEngine.md)

**汇总**

**宏定义**

| 名称 | 描述 |
| --- | --- |
| XEG_NEURAL_UPSCALE_SCISSOR 0x1U | 用于通过HMS_XEG_NeuralUpscaleParameter接口设置超分的裁剪窗口参数，裁剪窗口用于确定对输入图像采样的区域。 |
| XEG_NEURAL_UPSCALE_SHARPNESS 0x2U | 用于通过HMS_XEG_NeuralUpscaleParameter接口设置超分的锐化度参数，锐化度的建议取值范围为[0, 1]。 |
| XEG_NEURAL_UPSCALE_INPUT_HANDLE 0x4U | 用于通过HMS_XEG_NeuralUpscaleParameter接口设置与超分输入纹理关联的OH_NativeBuffer handle。 |

**类型定义**

| 名称 | 描述 |
| --- | --- |
| typedef void(GL_APIENTRYP PFN_HMS_XEG_NEURALUPSCALEPARAMETER) (GLenum pname, GLvoid *param) | 设置空域AI超分输入参数的函数指针定义。 |
| typedef void(GL_APIENTRYP PFN_HMS_XEG_RENDERNEURALUPSCALE) (GLuint inputTexture) | 执行空域AI超分渲染命令的函数指针定义。 |

**函数**

| 名称 | 描述 |
| --- | --- |
| GL_APICALL void GL_APIENTRY HMS_XEG_NeuralUpscaleParameter (GLenum pname, GLvoid *param) | 设置空域AI超分输入参数。 |
| GL_APICALL void GL_APIENTRY HMS_XEG_RenderNeuralUpscale (GLuint inputTexture) | 执行空域AI超分渲染命令。 |