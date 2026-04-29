# frame_generation_vk.h

**概述**

声明Vulkan图形API平台的超帧接口。

引用文件： <graphics_game_sdk/frame_generation_vk.h>

库： libframegeneration.so

系统能力： SystemCapability.GraphicsGame.RenderAccelerate

起始版本： 5.0.0(12)

相关模块： [GraphicsAccelerate](GraphicsAccelerate.md)

**汇总**

**结构体**

| 名称 | 描述 |
| --- | --- |
| struct FG_ContextDescription_VK | 此结构体描述创建超帧上下文实例FG_Context_VK所需的属性信息。 |
| struct FG_ImageFormat_VK | 此结构体描述超帧输入输出图像的格式信息，该接口仅适配Vulkan图形API平台。 |
| struct FG_ImageSync_VK | 此结构体描述超帧输入输出图像同步状态信息，用于创建超帧图像内存屏障。 |
| struct FG_ImageInfo_VK | 此结构体描述超帧输入输出图像信息。 |
| struct FG_DispatchDescription_VK | 此结构体描述下发帧生成命令HMS_FG_Dispatch_VK需要的参数信息，每一帧都需要进行更新。该接口仅适配Vulkan图形API平台。 |

**类型定义**

| 名称 | 描述 |
| --- | --- |
| typedef struct FG_Context_VK FG_Context_VK | 此结构体描述超帧上下文，该接口仅适配Vulkan图形API平台。 |
| typedef struct FG_Image_VK FG_Image_VK | 超帧输入输出图像结构体，该接口仅适配Vulkan图形API平台。 |
| typedef struct FG_ContextDescription_VK FG_ContextDescription_VK | 此结构体描述创建超帧上下文实例FG_Context_VK所需的属性信息。 |
| typedef struct FG_ImageFormat_VK FG_ImageFormat_VK | 此结构体描述超帧输入输出图像的格式信息，该接口仅适配Vulkan图形API平台。 |
| typedef struct FG_ImageSync_VK FG_ImageSync_VK | 此结构体描述超帧输入输出图像同步状态信息，用于创建超帧图像内存屏障。 |
| typedef struct FG_ImageInfo_VK FG_ImageInfo_VK | 此结构体描述超帧输入输出图像信息。 |
| typedef struct FG_DispatchDescription_VK FG_DispatchDescription_VK | 此结构体描述下发帧生成命令HMS_FG_Dispatch_VK需要的参数信息，每一帧都需要进行更新。该接口仅适配Vulkan图形API平台。 |

**函数**

| 名称 | 描述 |
| --- | --- |
| FG_Context_VK* HMS_FG_CreateContext_VK(const FG_ContextDescription_VK* contextDescription) | 创建超帧上下文实例，调用成功则返回指向FG_Context_VK对象的指针。该接口仅适配Vulkan图形API平台。 |
| FG_ErrorCode HMS_FG_SetAlgorithmMode_VK(FG_Context_VK* context, const FG_AlgorithmModeInfo* predictionModeInfo) | 设置超帧算法模式，包括预测算法模式和运动估计模式，必选。该接口仅适配Vulkan图形API平台。 |
| FG_ErrorCode HMS_FG_SetResolution_VK(FG_Context_VK* context, const FG_ResolutionInfo* resolutionInfo) | 设置超帧输入输出图像分辨率，必选。该接口仅适配Vulkan图形API平台。 |
| FG_ErrorCode HMS_FG_SetCvvZSemantic_VK(FG_Context_VK* context, FG_CvvZSemantic semantic) | 设置超帧齐次裁剪空间Z/W范围及深度测试函数，可选调用，未调用则默认模式设置为FG_CVV_Z_SEMANTIC_ZERO_TO_ONE_FORWARD_Z。 该接口仅适配Vulkan图形API平台。 |
| FG_ErrorCode HMS_FG_SetImageFormat_VK(FG_Context_VK* context, const FG_ImageFormat_VK* format) | 设置超帧输入输出图像格式，可选调用。未调用则真实帧颜色缓冲区和预测帧缓冲区图像格式默认为VK_FORMAT_R8G8B8A8_UNORM； 深度模板缓冲区图像格式默认为VK_FORMAT_D24_UNORM_S8_UINT。该接口仅适配Vulkan图形API平台。 |
| FG_ErrorCode HMS_FG_SetDepthStencilYDirectionInverted_VK(FG_Context_VK* context, bool inverted) | 设置颜色缓冲区相对深度模板缓冲区是否存在y轴翻转的标志位，可选调用，未调用则默认无翻转。该接口仅适配Vulkan图形API平台。 如果存在翻转但没有将inverted设置为true，可能导致预测帧效果异常。 |
| FG_Image_VK* HMS_FG_CreateImage_VK(FG_Context_VK* context, VkImage image, VkImageView view) | 创建超帧输入输出图像实例。真实帧颜色缓冲区、深度模板缓冲区、预测帧缓冲区均需要通过该接口创建对应的图像实例， 并传入预测帧生成接口HMS_FG_Dispatch_VK进行预测帧绘制。该接口将用户提供的图像资源和超帧算法实现之间建立关联。 |
| FG_ErrorCode HMS_FG_DestroyImage_VK(FG_Context_VK* context, FG_Image_VK* image) | 销毁超帧输入输出图像实例，取消对应关联。 |
| FG_ErrorCode HMS_FG_Activate_VK(FG_Context_VK* context) | 激活超帧上下文实例。已激活的超帧实例可调用HMS_FG_Dispatch_VK接口生成预测帧，激活超帧上下文实例前需进行实例属性的配置。该接口仅适配Vulkan图形API平台。 |
| FG_ErrorCode HMS_FG_Deactivate_VK(FG_Context_VK* context) | 去激活超帧上下文实例，可通过HMS_FG_Activate_VK接口重新激活。 |
| FG_ErrorCode HMS_FG_IsActive_VK(FG_Context_VK* context, bool* isActive) | 查询超帧上下文实例是否处于激活状态，该接口仅适配Vulkan图形API平台。 |
| FG_ErrorCode HMS_FG_Dispatch_VK(FG_Context_VK* context, const FG_DispatchDescription_VK* desc) | 配置帧预测所需的参数信息，生成预测帧，该接口仅适配Vulkan图形API平台。 |
| FG_ErrorCode HMS_FG_DestroyContext_VK(FG_Context_VK** context) | 销毁超帧上下文实例并释放内存资源，该接口仅适配Vulkan图形API平台。 |
| FG_ErrorCode HMS_FG_SetIntegrationMode_VK(FG_Context_VK* context, const FG_IntegrationInfo* integrationInfo) | 设置帧预测集成信息，该接口仅适配Vulkan图形API平台。 |
| FG_ErrorCode HMS_FG_SetUiPredictionEnabled_VK(FG_Context_VK* context, bool isEnabled) | 选择是否启用UI预测功能，这个功能只能在系统显示模式下启用，在游戏显示模式下无效。该接口仅适配Vulkan图形API平台。 |
| FG_ErrorCode HMS_FG_SetTargetFps_VK(FG_Context_VK* context, int targetFps) | 设置超帧后的目标帧率，这个设置仅在系统显示模式下生效，对游戏显示模式无影响。该接口在游戏初次上架之后生效且仅适配Vulkan图形API平台。 |