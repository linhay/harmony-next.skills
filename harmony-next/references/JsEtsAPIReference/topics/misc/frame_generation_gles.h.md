# frame_generation_gles.h

**概述**

声明OpenGL ES图形API平台的超帧接口。

引用文件： <graphics_game_sdk/frame_generation_gles.h>

库： libframegeneration.so

系统能力： SystemCapability.GraphicsGame.RenderAccelerate

起始版本： 5.0.0(12)

相关模块： [GraphicsAccelerate](GraphicsAccelerate.md)

**汇总**

**结构体**

| 名称 | 描述 |
| --- | --- |
| struct FG_DispatchDescription_GLES | 此结构体描述下发帧生成命令HMS_FG_Dispatch_GLES需要的参数信息，每一帧都需要进行更新。该接口仅适配OpenGL ES图形API平台。 |

**类型定义**

| 名称 | 描述 |
| --- | --- |
| typedef struct FG_Context_GLES FG_Context_GLES | 此结构体描述超帧上下文，该接口仅适配OpenGL ES图形API平台。 |
| typedef struct FG_DispatchDescription_GLES FG_DispatchDescription_GLES | 此结构体描述下发帧生成命令HMS_FG_Dispatch_GLES需要的参数信息，每一帧都需要进行更新。该接口仅适配OpenGL ES图形API平台。 |
| typedef enum FG_ImageFormat_GLES FG_ImageFormat_GLES | 此枚举描述真实渲染帧颜色缓冲区和预测帧缓冲区的图像格式。该接口仅适配OpenGL ES图形API平台。 |

**枚举**

| 名称 | 描述 |
| --- | --- |
| FG_ImageFormat_GLES { FG_FORMAT_R8G8B8A8_UNORM = 0, FG_FORMAT_R11G11B10_SFLOAT = 1, FG_FORMAT_R16G16B16A16_SFLOAT = 2 } | 此枚举描述真实渲染帧颜色缓冲区和预测帧缓冲区的图像格式。该接口仅适配OpenGL ES图形API平台。 |

**函数**

| 名称 | 描述 |
| --- | --- |
| FG_Context_GLES* HMS_FG_CreateContext_GLES(void) | 创建超帧上下文实例，调用成功则返回指向FG_Context_GLES对象的指针。该接口仅适配OpenGL ES图形API平台。 |
| FG_ErrorCode HMS_FG_SetAlgorithmMode_GLES(FG_Context_GLES* context, const FG_AlgorithmModeInfo* predictionModeInfo) | 设置超帧预测算法模式和运动估计模式，必选。该接口仅适配OpenGL ES图形API平台。 |
| FG_ErrorCode HMS_FG_SetResolution_GLES(FG_Context_GLES* context, const FG_ResolutionInfo* resolutionInfo) | 设置超帧输入输出图像分辨率，必选。该接口仅适配OpenGL ES图形API平台。 |
| FG_ErrorCode HMS_FG_SetCvvZSemantic_GLES(FG_Context_GLES* context, FG_CvvZSemantic semantic) | 设置超帧齐次裁剪空间Z/W范围及深度测试函数，可选调用，未调用则默认模式设置为FG_CVV_Z_SEMANTIC_MINUS_ONE_TO_ONE_FORWARD_Z。该接口仅适配OpenGL ES图形API平台。 |
| FG_ErrorCode HMS_FG_SetImageFormat_GLES(FG_Context_GLES* context, FG_ImageFormat_GLES format) | 设置真实渲染帧颜色缓冲区和预测帧缓冲区的图像格式，可选调用，未调用则模式默认设置为FG_FORMAT_R8G8B8A8_UNORM。该接口仅适配OpenGL ES图形API平台。 |
| FG_ErrorCode HMS_FG_SetDepthStencilYDirectionInverted_GLES(FG_Context_GLES* context, bool inverted) | 设置颜色缓冲区相对深度模板缓冲区基于y轴翻转的标志位，可选调用，未调用则默认无翻转。该接口仅适配OpenGL ES图形API平台。 |
| FG_ErrorCode HMS_FG_Activate_GLES(FG_Context_GLES* context) | 激活超帧上下文实例。已激活的超帧实例可调用HMS_FG_Dispatch_GLES接口生成预测帧， 激活超帧上下文实例前需进行实例属性的配置。该接口仅适配OpenGL ES图形API平台。 |
| FG_ErrorCode HMS_FG_Deactivate_GLES(FG_Context_GLES* context) | 去激活超帧上下文实例，可通过HMS_FG_Activate_GLES接口重新激活。 |
| FG_ErrorCode HMS_FG_IsActive_GLES(FG_Context_GLES* context, bool* isActive) | 查询超帧上下文实例是否处于激活状态。该接口仅适配OpenGL ES图形API平台。 |
| FG_ErrorCode HMS_FG_Dispatch_GLES(FG_Context_GLES* context, const FG_DispatchDescription_GLES* desc) | 配置帧预测所需的参数信息，生成预测帧，该接口仅适配OpenGL ES图形API平台。 |
| FG_ErrorCode HMS_FG_SetExtendedCameraInfo_GLES(FG_Context_GLES* context, const FG_PerFrameExtendedCameraInfo* info) | 设置超帧相机扩展属性信息，当视图投影矩阵的平移分量非常大时，提供该信息以获得更加准确的超帧效果。可选调用，该接口仅适配OpenGL ES图形API平台。 |
| FG_ErrorCode HMS_FG_DestroyContext_GLES(FG_Context_GLES** context) | 销毁超帧上下文实例并释放内存资源。该接口仅适配OpenGL ES图形API平台。 |
| FG_ErrorCode HMS_FG_SetIntegrationMode_GLES(FG_Context_GLES* context, const FG_IntegrationInfo* integrationInfo) | 设置超帧集成信息，该接口仅适配OpenGL ES图形API平台。 |
| FG_ErrorCode HMS_FG_SetUiPredictionEnabled_GLES(FG_Context_GLES* context, bool isEnabled) | 选择是否启用UI预测功能，这个功能只能在系统显示模式下启用，在游戏显示模式下无效。该接口仅适配OpenGL ES图形API平台。 |
| FG_ErrorCode HMS_FG_SetTargetFps_GLES(FG_Context_GLES* context, int targetFps) | 设置超帧后的目标帧率，这个设置仅在系统显示模式下生效，对游戏显示模式无影响。该接口在游戏初次上架之后生效且仅适配OpenGL ES图形API平台。 |