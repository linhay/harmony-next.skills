# GraphicsAccelerate

#### 概述

提供Graphics Accelerate Kit图形渲染加速能力的相关接口。

**系统能力：** SystemCapability.GraphicsGame.RenderAccelerate

**起始版本：** 5.0.0(12)

#### 汇总

#### 文件

名称

描述

[abr_base.h](abr_base.h.md)

声明不区分图形API平台的ABR（自适应稳态渲染）接口。

[abr_gles.h](abr_gles.h.md)

声明OpenGL ES图形API平台的ABR接口。

[frame_generation_base.h](frame_generation_base.h.md)

声明不区分图形API平台的超帧接口。

[frame_generation_gles.h](frame_generation_gles.h.md)

声明OpenGL ES图形API平台的超帧接口。

[frame_generation_vk.h](frame_generation_vk.h.md)

声明Vulkan图形API平台的超帧接口。

[opengtx_base.h](opengtx_base.h.md)

声明不区分OpenGL ES和Vulkan图形API平台的OpenGTX接口。

#### 结构体

名称

描述

struct [ABR_Vector3](ABR_Vector3.md)

此结构体描述ABR三维向量。

struct [ABR_CameraData](ABR_CameraData.md)

此结构体描述游戏应用每帧的相机运动数据，ABR会结合相机运动数据自适应调整FrameBuffer（帧缓冲，下文简称Buffer）分辨率因子。

struct [FG_Mat4x4](FG_Mat4x4.md)

此结构体描述列主序4x4矩阵。

struct [FG_AlgorithmModeInfo](FG_AlgorithmModeInfo.md)

此结构体描述超帧算法模式信息。

struct [FG_Dimension2D](FG_Dimension2D.md)

此结构体描述2D图像分辨率，以像素为单位。

struct [FG_ResolutionInfo](FG_ResolutionInfo.md)

此结构体描述超帧输入输出图像的分辨率。

struct [FG_Vec3D](FG_Vec3D.md)

此结构体描述超帧三维向量。

struct [FG_PerFrameExtendedCameraInfo](FG_PerFrameExtendedCameraInfo.md)

此结构体描述相机扩展信息。当视图投影矩阵的平移分量非常大时，可以提供更加详细的相机信息以获得更加准确的超帧预测效果。

struct [FG_IntegrationInfo](FG_IntegrationInfo.md)

此结构体描述超帧集成的信息。包括送显模式，是否需要额外缓存深度和颜色纹理，以及是否需要翻转颜色纹理。仅在[FG_PredictionMode](#ZH-CN_TOPIC_0000002418917005__gaea2169cd5ae4bf9e8a17dc58f33e8766)为FG_PREDICTION_MODE_INTERPOLATION时生效。

struct [FG_DispatchDescription_GLES](FG_DispatchDescription_GLES.md)

此结构体描述下发帧生成命令[HMS_FG_Dispatch_GLES](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gab135a0f59582d168d461ef115423cfb4)需要的参数信息，每一帧都需要进行更新。该接口仅适配OpenGL ES图形API平台。

struct [FG_ContextDescription_VK](FG_ContextDescription_VK.md)

此结构体描述创建超帧上下文实例[FG_Context_VK](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga4022ab63c2296d63dcf2c2df178508b7)所需的属性信息。

struct [FG_ImageFormat_VK](FG_ImageFormat_VK.md)

此结构体描述超帧输入输出图像的格式信息，该接口仅适配Vulkan图形API平台。

struct [FG_ImageSync_VK](FG_ImageSync_VK.md)

此结构体描述超帧输入输出图像同步状态信息，用于创建超帧图像内存屏障。该接口仅适配Vulkan图形API平台。

struct [FG_ImageInfo_VK](FG_ImageInfo_VK.md)

此结构体描述超帧输入输出图像信息，该接口仅适配Vulkan图形API平台。

struct [FG_DispatchDescription_VK](FG_DispatchDescription_VK.md)

此结构体描述下发帧生成命令[HMS_FG_Dispatch_VK](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga21f86a194e72e99dd54fd39080385a37)需要的参数信息，每一帧都需要进行更新。该接口仅适配Vulkan图形API平台。

struct [OpenGTX_ConfigDescription](OpenGTX_ConfigDescription.md)

此结构体描述OpenGTX属性配置。

struct [OpenGTX_GameSceneInfo](OpenGTX_GameSceneInfo.md)

此结构体描述游戏场景信息，游戏应用获取到场景后传递此参数。

struct [OpenGTX_FrameRenderInfo](OpenGTX_FrameRenderInfo.md)

此结构体描述帧渲染信息，游戏应用获取到帧属性后传递此参数。

struct [OpenGTX_NetworkInfo](OpenGTX_NetworkInfo.md)

此结构体描述当前设备网络信息，游戏应用获取到网络信息后传递此参数。

struct [OpenGTX_ResolutionValue](OpenGTX_ResolutionValue.md)

此结构体描述游戏应用的分辨率值。

struct [OpenGTX_Vector3](OpenGTX_Vector3.md)

此结构体描述OpenGTX三维向量。

struct [OpenGTX_NetworkLatency](OpenGTX_NetworkLatency.md)

此结构体描述当前设备网络延迟信息，游戏应用获取到网络延迟后传递此参数。

#### 类型定义

名称

描述

typedef struct [ABR_Context](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga52e8dba39ee979b70826401b3d36574e)[ABR_Context](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga52e8dba39ee979b70826401b3d36574e)

此结构体描述ABR上下文。

typedef enum [ABR_RenderAPI_Type](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga9359d16ecefa21f0e6e5f29732cbf6f4)[ABR_RenderAPI_Type](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga3a6ead3a3c0f19a6434e97fda13f42f2)

此枚举描述ABR支持的图形API类型。

typedef struct [ABR_Vector3](ABR_Vector3.md)[ABR_Vector3](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga71a845f23f7ec4c0935db8e9f00ab8b9)

此结构体描述ABR三维向量。

typedef struct [ABR_CameraData](ABR_CameraData.md)[ABR_CameraData](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gada21a47272d5db8e28e2a9bb4fd033d4)

此结构体描述游戏应用每帧的相机运动数据，ABR会结合相机运动数据自适应调整FrameBuffer（帧缓冲，下文简称Buffer）分辨率因子。

typedef enum [ABR_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga72df702d70a8326b5b46c118be6ad1d7)[ABR_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga86d5860f91dc4f1de6b381cd65389b9d)

此枚举描述ABR接口调用错误码。

typedef struct [FG_Mat4x4](FG_Mat4x4.md)[FG_Mat4x4](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gabbf87d3423630e0b50f19da2cbda3e90)

此结构体描述列主序4x4矩阵。

typedef enum [FG_PredictionMode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gaea2169cd5ae4bf9e8a17dc58f33e8766)[FG_PredictionMode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga79e55783a2a38873fc6890c297885275)

此枚举描述超帧预测算法模式。

typedef enum [FG_MeMode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga8bd44b6bea12774dd2ee6014d696e7d1)[FG_MeMode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga81cbe226af620e6ef19cd8ec5e9b5256)

此枚举描述超帧运动估计算法模式，支持基础模式和增强模式。

typedef enum [FG_PresentMode](#section131101213459)[FG_PresentMode](#section11881356193212)

此枚举定义预测帧送显模式，支持游戏端送显预测帧模式和系统端送显预测帧模式。

typedef struct [FG_AlgorithmModeInfo](FG_AlgorithmModeInfo.md)[FG_AlgorithmModeInfo](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga1750087784d7cbf19957243db12a7ba3)

此结构体描述超帧算法模式信息。

typedef struct [FG_Vec3D](FG_Vec3D.md)[FG_Vec3D](FG_Vec3D.md)

此结构体描述超帧三维向量。

typedef struct [FG_PerFrameExtendedCameraInfo](FG_PerFrameExtendedCameraInfo.md)[FG_PerFrameExtendedCameraInfo](FG_PerFrameExtendedCameraInfo.md)

此结构体描述相机扩展信息。当视图投影矩阵的平移分量非常大时，可以提供更加详细的相机信息以获得更加准确的超帧预测效果。

typedef struct [FG_IntegrationInfo](FG_IntegrationInfo.md)[FG_IntegrationInfo](FG_IntegrationInfo.md)

此结构体描述超帧集成的信息。包括送显模式，是否需要额外缓存深度和颜色纹理，以及是否需要翻转颜色纹理。仅在[FG_PredictionMode](#ZH-CN_TOPIC_0000002418917005__gaea2169cd5ae4bf9e8a17dc58f33e8766)为FG_PREDICTION_MODE_INTERPOLATION时生效。

typedef enum [FG_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga68efbf5ff41faeb835f5587654c1e669)[FG_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga394c554fc5d056d702180ee031ccee2c)

此枚举描述超帧接口调用错误码。

typedef enum [FG_CvvZSemantic](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga530448309918d6d703e28c61a848a267)[FG_CvvZSemantic](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gabac7987ddc62b712f36d95b185e47bb2)

此枚举描述经过相机投影变换后，齐次裁剪空间Z/W范围及深度测试模式。

typedef struct [FG_Dimension2D](FG_Dimension2D.md)[FG_Dimension2D](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga545268ccc070666954981580f5764d20)

此结构体描述2D图像分辨率，以像素为单位。

typedef struct [FG_ResolutionInfo](FG_ResolutionInfo.md)[FG_ResolutionInfo](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gacbc0d894e11f18711fd4558d45c7cd39)

此结构体描述超帧输入输出图像的分辨率。

typedef struct [FG_Context_GLES](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga62e666292d67fd19fd35ad07463e21cc)[FG_Context_GLES](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga62e666292d67fd19fd35ad07463e21cc)

此结构体描述超帧上下文，该接口仅适配OpenGL ES图形API平台。

typedef struct [FG_DispatchDescription_GLES](FG_DispatchDescription_GLES.md)[FG_DispatchDescription_GLES](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga3f4c6e065ff13670d8c64cb9cc3796a7)

此结构体描述下发帧生成命令[HMS_FG_Dispatch_GLES](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gab135a0f59582d168d461ef115423cfb4)需要的参数信息，每一帧都需要进行更新。该接口仅适配OpenGL ES图形API平台。

typedef enum [FG_ImageFormat_GLES](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga3bec27405891e089234bf50d0589c3cd)[FG_ImageFormat_GLES](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga5fbce7432ad1a2e3d9a37554bce2352a)

此枚举描述真实渲染帧颜色缓冲区和预测帧缓冲区的图像格式。该接口仅适配OpenGL ES图形API平台。

typedef struct [FG_Context_VK](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga4022ab63c2296d63dcf2c2df178508b7)[FG_Context_VK](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga4022ab63c2296d63dcf2c2df178508b7)

此结构体描述超帧上下文，该接口仅适配Vulkan图形API平台。

typedef struct [FG_Image_VK](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gabd6ee9704e997ffc2792ad3c89847019)[FG_Image_VK](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gabd6ee9704e997ffc2792ad3c89847019)

超帧输入输出图像结构体，该接口仅适配Vulkan图形API平台。

typedef struct [FG_ContextDescription_VK](FG_ContextDescription_VK.md)[FG_ContextDescription_VK](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga6d3f20ae7b60a4a38baf696031d609c0)

此结构体描述创建超帧上下文实例[FG_Context_VK](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga4022ab63c2296d63dcf2c2df178508b7)所需的属性信息。

typedef struct [FG_ImageFormat_VK](FG_ImageFormat_VK.md)[FG_ImageFormat_VK](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga2ef395664c0fd54102510c62a84ebc3a)

此结构体描述超帧输入输出图像的格式信息，该接口仅适配Vulkan图形API平台。

typedef struct [FG_ImageSync_VK](FG_ImageSync_VK.md)[FG_ImageSync_VK](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga847779a17b04d183b31397007b11735f)

此结构体描述超帧输入输出图像同步状态信息，用于创建超帧图像内存屏障。该接口仅适配Vulkan图形API平台。

typedef struct [FG_ImageInfo_VK](FG_ImageInfo_VK.md)[FG_ImageInfo_VK](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gabf275c34e4b1335ddcda4b576009d6c7)

此结构体描述超帧输入输出图像信息，该接口仅适配Vulkan图形API平台。

typedef struct [FG_DispatchDescription_VK](FG_DispatchDescription_VK.md)[FG_DispatchDescription_VK](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gabdf63f9fb31687516fee81d83b609302)

此结构体描述下发帧生成命令[HMS_FG_Dispatch_VK](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga21f86a194e72e99dd54fd39080385a37)需要的参数信息，每一帧都需要进行更新。该接口仅适配Vulkan图形API平台。

typedef enum [OpenGTX_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga97deebd9adf3e19947ec5b4615fa1d9c)[OpenGTX_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gaa2c657ed21a175b099bea0ed2491cc34)

此枚举描述OpenGTX接口调用错误码。

typedef enum [OpenGTX_LTPO_Mode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gad531d05ca502b93f4153e4b1f749ed0c)[OpenGTX_LTPO_Mode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gace5aaeeb51bae6d9cfa77ff009787fac)

此枚举描述OpenGTX_LTPO模式类型，以控制游戏中的帧率。

typedef enum [OpenGTX_EngineType](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gadd5a5e0b3b4aa3ea8b0974cba13c0389)[OpenGTX_EngineType](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga1f7722a3c293500468662b4ab531a6cf)

此枚举描述游戏应用的底层游戏引擎类型。

typedef enum [OpenGTX_GameType](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga34d898acfaacb3750db454a9ed2038a5)[OpenGTX_GameType](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga25a7691e1e839f1a242927d70633d816)

此枚举描述游戏应用的类型。

typedef enum [OpenGTX_SceneID](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gad7e5d2d235183dc0c6549331d6bc2932)[OpenGTX_SceneID](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gaef86d901a97a6e16dfff3f3d68bf123c)

此枚举描述OpenGTX算法的游戏场景类型。

typedef enum [OpenGTX_PictureQualityMaxLevel](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gacd5c090213b3593e7c9ab6c93118ff8e)[OpenGTX_PictureQualityMaxLevel](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gae9ef047f7f1e854186af0d62dacff68d)

此枚举描述游戏应用的图像质量。

typedef enum [OpenGTX_TempLevel](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gaeff4735d18eb3086603ab6d04e7ad133)[OpenGTX_TempLevel](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga4571f1a424d551ba387ab3ea4fd6d8b8)

此枚举描述设备的温度级别。

typedef struct [OpenGTX_Context](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga3ef8c7447a236d882b625ec8434385ed)[OpenGTX_Context](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga3ef8c7447a236d882b625ec8434385ed)

此结构体描述OpenGTX上下文。

typedef struct [OpenGTX_ConfigDescription](OpenGTX_ConfigDescription.md)[OpenGTX_ConfigDescription](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga2536aca243f80e8fee0a4f3b6a9c2b63)

此结构体描述OpenGTX属性配置。

typedef struct [OpenGTX_GameSceneInfo](OpenGTX_GameSceneInfo.md)[OpenGTX_GameSceneInfo](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gae72bdc657dfd31dae48df5e069eaddda)

此结构体描述游戏场景信息，游戏应用获取到场景后传递此参数。

typedef struct [OpenGTX_FrameRenderInfo](OpenGTX_FrameRenderInfo.md)[OpenGTX_FrameRenderInfo](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gab7cf8edc160e7a0c9050e39443df34b1)

此结构体描述帧渲染信息，游戏应用获取到帧属性后传递此参数。

typedef struct [OpenGTX_NetworkInfo](OpenGTX_NetworkInfo.md)[OpenGTX_NetworkInfo](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga8f8b321e53382f5f07e850c79478204b)

此结构体描述当前设备网络信息，游戏应用获取到网络信息后传递此参数。

typedef struct [OpenGTX_ResolutionValue](OpenGTX_ResolutionValue.md)[OpenGTX_ResolutionValue](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga36078da348203d9ce874cb4b4d953d40)

此结构体描述游戏应用的分辨率值。

typedef struct [OpenGTX_Vector3](OpenGTX_Vector3.md)[OpenGTX_Vector3](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gaba0a76029883a1c315a61c28719b9839)

此结构体描述OpenGTX三维向量。

typedef struct [OpenGTX_NetworkLatency](OpenGTX_NetworkLatency.md)[OpenGTX_NetworkLatency](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga75435c59fdcf1b9d651d2a00f154be7b)

此结构体描述当前设备网络延迟信息，游戏应用获取到网络延迟后传递此参数。

typedef void(* [OpenGTX_DeviceInfoCallback](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga1d66cec4aa0e01696d878c330f012d7a)) ([OpenGTX_TempLevel](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gaeff4735d18eb3086603ab6d04e7ad133))

设备的温度信息回调。

#### 枚举

名称

描述

[ABR_RenderAPI_Type](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga9359d16ecefa21f0e6e5f29732cbf6f4) {

RENDER_API_GLES = 0

}

此枚举描述ABR支持的图形API类型。

[ABR_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga72df702d70a8326b5b46c118be6ad1d7) {

ABR_SUCCESS = 0,

ABR_INVALID_PARAMETER = 401,

ABR_CONTEXT_CONFIG_AFTER_ACTIVE = 1009501001,

ABR_CONTEXT_NOT_CONFIG = 1009501002,

ABR_CONTEXT_NOT_ACTIVE = 1009501003,

ABR_METADATA_INVALID = 1009501004,

ABR_FRAMEBUFFER_INVALID = 1009501005

}

此枚举描述ABR接口调用错误码。

[FG_PredictionMode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gaea2169cd5ae4bf9e8a17dc58f33e8766) {

FG_PREDICTION_MODE_INTERPOLATION = 0,

FG_PREDICTION_MODE_EXTRAPOLATION = 1

}

此枚举描述超帧预测算法模式。

[FG_MeMode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga8bd44b6bea12774dd2ee6014d696e7d1) {

FG_ME_MODE_BASIC = 0,

FG_ME_MODE_ENHANCED = 1

}

此枚举描述超帧运动估计算法模式，支持基础模式和增强模式。

[FG_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga68efbf5ff41faeb835f5587654c1e669) {

FG_SUCCESS = 0,

FG_INVALID_PARAMETER = 401,

FG_CONTEXT_NOT_CONFIG = 1009500001,

FG_CONTEXT_NOT_ACTIVE = 1009500002,

FG_COLLECTING_PREVIOUS_FRAMES = 1009500003

}

此枚举描述超帧接口调用错误码。

[FG_CvvZSemantic](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga530448309918d6d703e28c61a848a267) {

FG_CVV_Z_SEMANTIC_MINUS_ONE_TO_ONE_FORWARD_Z = 0,

FG_CVV_Z_SEMANTIC_ZERO_TO_ONE_REVERSE_Z = 1,

FG_CVV_Z_SEMANTIC_MINUS_ONE_TO_ONE_REVERSE_Z = 2,

FG_CVV_Z_SEMANTIC_ZERO_TO_ONE_FORWARD_Z = 3

}

此枚举描述经过相机投影变换后，齐次裁剪空间Z/W范围及深度测试模式。

[FG_ImageFormat_GLES](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga3bec27405891e089234bf50d0589c3cd) {

FG_FORMAT_R8G8B8A8_UNORM = 0,

FG_FORMAT_R11G11B10_SFLOAT = 1,

FG_FORMAT_R16G16B16A16_SFLOAT = 2

}

此枚举描述真实渲染帧颜色缓冲区和预测帧缓冲区的图像格式。该接口仅适配OpenGL ES图形API平台。

[FG_PresentMode](#section131101213459) {

FG_PRESENT_BY_GAME = 0,

FG_PRESENT_BY_SYSTEM = 1

}

定义预测帧送显模式，该模式包括两种：游戏端预测帧送显和系统端预测帧送显。

[OpenGTX_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga97deebd9adf3e19947ec5b4615fa1d9c) {

OPENGTX_SUCCESS = 0,

OPENGTX_INVALID_PARAMETER = 401,

OPENGTX_CONTEXT_NOT_CONFIG = 1009502001,

OPENGTX_CONTEXT_NOT_ACTIVE = 1009502002

}

此枚举描述OpenGTX接口调用错误码。

[OpenGTX_LTPO_Mode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gad531d05ca502b93f4153e4b1f749ed0c) {

SCENE_MODE = 0x0001,

TOUCH_MODE = 0x0010,

ADAPTIVE_MODE = 0x0100

}

此枚举描述OpenGTX_LTPO模式类型，以控制游戏中的帧率。

[OpenGTX_EngineType](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gadd5a5e0b3b4aa3ea8b0974cba13c0389) {

UNITY = 1,

UNREAL = 2,

MESSIAH = 3,

COCOS = 4,

OTHERS_ENGINE = 100

}

此枚举描述游戏应用的底层游戏引擎类型。

[OpenGTX_GameType](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga34d898acfaacb3750db454a9ed2038a5) {

MOBA = 1,

RPG = 2,

FPS = 3,

RAC = 4,

OTHERS_TYPE = 100

}

此枚举描述游戏应用的类型。

[OpenGTX_SceneID](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gad7e5d2d235183dc0c6549331d6bc2932) {

LOGIN = 1,

GAME_INTERFACE = 2,

LOADING = 3,

PLAYING = 4,

SPECTATOR = 5,

DEATH = 6,

HEAVY_LOAD = 7,

OTHERS_SCENE = 100

}

此枚举描述OpenGTX算法的游戏场景类型。

[OpenGTX_PictureQualityMaxLevel](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gacd5c090213b3593e7c9ab6c93118ff8e) {

SD = 1,

HD = 2,

FHD = 3,

QHD = 4,

UHD = 5

}

此枚举描述游戏应用的图像质量。

[OpenGTX_TempLevel](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gaeff4735d18eb3086603ab6d04e7ad133) {

TEMP_LEVEL1 = 1,

TEMP_LEVEL2 = 2,

TEMP_LEVEL3 = 3,

TEMP_LEVEL4 = 4,

TEMP_LEVEL5 = 5,

TEMP_LEVEL6 = 6

}

此枚举描述设备的温度级别。

#### 函数

名称

描述

[ABR_Context](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga52e8dba39ee979b70826401b3d36574e)* [HMS_ABR_CreateContext](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga8f785903a5382ff31baef78a3968f66a)([ABR_RenderAPI_Type](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga9359d16ecefa21f0e6e5f29732cbf6f4) type)

创建ABR上下文实例，每次调用会新建[ABR_Context](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga52e8dba39ee979b70826401b3d36574e)对象，并返回指向[ABR_Context](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga52e8dba39ee979b70826401b3d36574e)对象的指针。

[ABR_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga72df702d70a8326b5b46c118be6ad1d7)[HMS_ABR_SetTargetFps](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga6c613e02088d559b9dc1450fde15bc2a)([ABR_Context](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga52e8dba39ee979b70826401b3d36574e)* context, const uint32_t targetFps)

配置ABR上下文实例的目标帧率属性。

[ABR_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga72df702d70a8326b5b46c118be6ad1d7)[HMS_ABR_SetScaleRange](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga1001c6a7739d8ce57bf851986f121bf5)([ABR_Context](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga52e8dba39ee979b70826401b3d36574e)* context, const float minValue, const float maxValue)

配置ABR上下文实例的Buffer分辨率因子范围属性。

[ABR_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga72df702d70a8326b5b46c118be6ad1d7)[HMS_ABR_Activate](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga463d8d5396bfd5f6ed800ddab616479a)([ABR_Context](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga52e8dba39ee979b70826401b3d36574e)* context)

激活ABR上下文实例。激活ABR上下文实例前需调用[HMS_ABR_SetTargetFps](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga6c613e02088d559b9dc1450fde15bc2a)和[HMS_ABR_SetScaleRange](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga1001c6a7739d8ce57bf851986f121bf5)接口进行实例属性的配置。

[ABR_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga72df702d70a8326b5b46c118be6ad1d7)[HMS_ABR_IsActive](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga791519fde19801e6da60094cf077b00f)([ABR_Context](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga52e8dba39ee979b70826401b3d36574e)* context, bool* isActive)

查询ABR上下文实例是否处于激活状态。

[ABR_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga72df702d70a8326b5b46c118be6ad1d7)[HMS_ABR_Deactivate](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga4abb4b37392e77c15fbedfa8ceba3da4)([ABR_Context](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga52e8dba39ee979b70826401b3d36574e)* context)

去激活ABR上下文实例，可通过[HMS_ABR_Activate](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga463d8d5396bfd5f6ed800ddab616479a)重新激活。

[ABR_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga72df702d70a8326b5b46c118be6ad1d7)[HMS_ABR_UpdateCameraData](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga5b895e36d31e46f71d04aba78c8f3716)([ABR_Context](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga52e8dba39ee979b70826401b3d36574e)* context, [ABR_CameraData](ABR_CameraData.md)* data)

更新每帧相机运动数据，ABR更新相机运动数据前需调用[HMS_ABR_Activate](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga463d8d5396bfd5f6ed800ddab616479a)接口激活ABR上下文实例。

[ABR_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga72df702d70a8326b5b46c118be6ad1d7)[HMS_ABR_GetScale](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga936129328fea3a5f77b2aae4935f67c6)([ABR_Context](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga52e8dba39ee979b70826401b3d36574e)* context, float* scale)

获取ABR Buffer分辨率因子。

[ABR_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga72df702d70a8326b5b46c118be6ad1d7)[HMS_ABR_GetNextScale](#section157311245143415)([ABR_Context](zh-cn_topic_0000002418917005.html#ZH-CN_TOPIC_0000002418917005__ga52e8dba39ee979b70826401b3d36574e)* context, float* scale)

获取下一帧的ABR Buffer分辨率因子。

[ABR_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga72df702d70a8326b5b46c118be6ad1d7)[HMS_ABR_DestroyContext](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gaf3c03179b9bcf1b8475230cbbb0d877c)([ABR_Context](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga52e8dba39ee979b70826401b3d36574e)** context)

销毁ABR上下文实例并释放内存资源。

[ABR_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga72df702d70a8326b5b46c118be6ad1d7)[HMS_ABR_MarkFrameBuffer_GLES](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga821fb33620312d3adba51d30254c1ef0)([ABR_Context](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga52e8dba39ee979b70826401b3d36574e)* context)

标记ABR进行自适应渲染处理的GLES Buffer，需要在GLES Buffer开始渲染前调用此接口。

[ABR_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga72df702d70a8326b5b46c118be6ad1d7)[HMS_ABR_GetScaledTexture_GLES](#section791920394423)([ABR_Context](zh-cn_topic_0000002418917005.html#ZH-CN_TOPIC_0000002418917005__ga52e8dba39ee979b70826401b3d36574e)* context, uint32_t originTexture, uint32_t* scaledTexture)

根据原始分辨率的GLES纹理索引获取ABR自适应缩放后的GLES纹理索引。

[FG_Context_GLES](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga62e666292d67fd19fd35ad07463e21cc)* [HMS_FG_CreateContext_GLES](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga58e6b601cc4a7e8f0208d4f10f16c7e5)(void)

创建超帧上下文实例，调用成功则返回指向[FG_Context_GLES](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga62e666292d67fd19fd35ad07463e21cc)对象的指针。该接口仅适配OpenGL ES图形API平台。

[FG_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga68efbf5ff41faeb835f5587654c1e669)[HMS_FG_SetAlgorithmMode_GLES](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga79cc36ec768553a6560d1c553ef83c3b)([FG_Context_GLES](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga62e666292d67fd19fd35ad07463e21cc)* context, const [FG_AlgorithmModeInfo](FG_AlgorithmModeInfo.md)* predictionModeInfo)

设置超帧预测算法模式和运动估计模式，必选。该接口仅适配OpenGL ES图形API平台。

[FG_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga68efbf5ff41faeb835f5587654c1e669)[HMS_FG_SetResolution_GLES](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gae46fcee6c715a6fda24df727465d42b1)([FG_Context_GLES](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga62e666292d67fd19fd35ad07463e21cc)* context, const [FG_ResolutionInfo](FG_ResolutionInfo.md)* resolutionInfo)

设置超帧输入输出图像分辨率，必选。该接口仅适配OpenGL ES图形API平台。

[FG_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga68efbf5ff41faeb835f5587654c1e669)[HMS_FG_SetCvvZSemantic_GLES](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga6247264302a139024a92cf89da565b52)([FG_Context_GLES](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga62e666292d67fd19fd35ad07463e21cc)* context, [FG_CvvZSemantic](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga530448309918d6d703e28c61a848a267) semantic)

设置超帧齐次裁剪空间Z/W范围及深度测试函数，可选调用，未调用则默认模式设置为FG_CVV_Z_SEMANTIC_MINUS_ONE_TO_ONE_FORWARD_Z。该接口仅适配OpenGL ES图形API平台。

[FG_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga68efbf5ff41faeb835f5587654c1e669)[HMS_FG_SetImageFormat_GLES](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gaafa490d4377cc5babbc0ac0f4f7b78a7)([FG_Context_GLES](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga62e666292d67fd19fd35ad07463e21cc)* context, [FG_ImageFormat_GLES](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga3bec27405891e089234bf50d0589c3cd) format)

设置真实渲染帧颜色缓冲区和预测帧缓冲区的图像格式，可选调用，未调用则模式默认设置为FG_FORMAT_R8G8B8A8_UNORM。该接口仅适配OpenGL ES图形API平台。

[FG_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga68efbf5ff41faeb835f5587654c1e669)[HMS_FG_SetDepthStencilYDirectionInverted_GLES](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gaa6e340d0b1f1bc4dcd6abf378aa933df)([FG_Context_GLES](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga62e666292d67fd19fd35ad07463e21cc)* context, bool inverted)

设置颜色缓冲区相对深度模板缓冲区基于y轴翻转的标志位，可选调用，未调用则默认无翻转。该接口仅适配OpenGL ES图形API平台。

[FG_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga68efbf5ff41faeb835f5587654c1e669)[HMS_FG_Activate_GLES](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gaa5f1d5b98694100aa3e3dbb4c99ac23a)([FG_Context_GLES](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga62e666292d67fd19fd35ad07463e21cc)* context)

激活超帧上下文实例。已激活的超帧实例可调用[HMS_FG_Dispatch_GLES](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gab135a0f59582d168d461ef115423cfb4)接口生成预测帧， 激活超帧上下文实例前需进行实例属性的配置。该接口仅适配OpenGL ES图形API平台。

[FG_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga68efbf5ff41faeb835f5587654c1e669)[HMS_FG_Deactivate_GLES](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gad08ff75c271a0c7c99ae3ebc596928b9)([FG_Context_GLES](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga62e666292d67fd19fd35ad07463e21cc)* context)

去激活超帧上下文实例，可通过[HMS_FG_Activate_GLES](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gaa5f1d5b98694100aa3e3dbb4c99ac23a)接口重新激活。

[FG_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga68efbf5ff41faeb835f5587654c1e669)[HMS_FG_IsActive_GLES](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gaaa592e60d1cda40068b51c36d436b8eb)([FG_Context_GLES](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga62e666292d67fd19fd35ad07463e21cc)* context, bool* isActive)

查询超帧上下文实例是否处于激活状态。该接口仅适配OpenGL ES图形API平台。

[FG_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga68efbf5ff41faeb835f5587654c1e669)[HMS_FG_Dispatch_GLES](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gab135a0f59582d168d461ef115423cfb4)([FG_Context_GLES](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga62e666292d67fd19fd35ad07463e21cc)* context, const [FG_DispatchDescription_GLES](FG_DispatchDescription_GLES.md)* desc)

配置帧预测所需的参数信息，生成预测帧，该接口仅适配OpenGL ES图形API平台。

[FG_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga68efbf5ff41faeb835f5587654c1e669)[HMS_FG_SetExtendedCameraInfo_GLES](#section1450921818712)([FG_Context_GLES](zh-cn_topic_0000002418917005.html#ZH-CN_TOPIC_0000002418917005__ga62e666292d67fd19fd35ad07463e21cc)* context, const [FG_PerFrameExtendedCameraInfo](FG_PerFrameExtendedCameraInfo.md)* info)

设置超帧相机扩展属性信息，当视图投影矩阵的平移分量非常大时，提供该信息以获得更加准确的超帧效果。可选调用，该接口仅适配OpenGL ES图形API平台。

[FG_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga68efbf5ff41faeb835f5587654c1e669)[HMS_FG_DestroyContext_GLES](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga8c61d12e9e4c8f7e95bed76006ee3335)([FG_Context_GLES](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga62e666292d67fd19fd35ad07463e21cc)** context)

销毁超帧上下文实例并释放内存资源。该接口仅适配OpenGL ES图形API平台。

[FG_ErrorCode](#ZH-CN_TOPIC_0000002418917005__ga68efbf5ff41faeb835f5587654c1e669)[HMS_FG_SetIntegrationMode_GLES](#section291123211916)([FG_Context_GLES](#ZH-CN_TOPIC_0000002418917005__ga62e666292d67fd19fd35ad07463e21cc)* context, const [FG_IntegrationInfo](zh-cn_topic_0000002418916973.html)* integrationInfo)

设置帧预测集成信息，该接口仅适配OpenGL ES图形API平台。

[FG_ErrorCode](#ZH-CN_TOPIC_0000002418917005__ga68efbf5ff41faeb835f5587654c1e669)[HMS_FG_SetUiPredictionEnabled_GLES](#section41231648141914)([FG_Context_GLES](#ZH-CN_TOPIC_0000002418917005__ga62e666292d67fd19fd35ad07463e21cc)* context, bool isEnabled)

选择是否启用UI预测功能，这个功能只能在系统送显模式下启用，在游戏送显模式下无效。该接口仅适配OpenGL ES图形API平台。

[FG_ErrorCode](#ZH-CN_TOPIC_0000002418917005__ga68efbf5ff41faeb835f5587654c1e669)[HMS_FG_SetTargetFps_GLES](#section19112185207)([FG_Context_GLES](#ZH-CN_TOPIC_0000002418917005__ga62e666292d67fd19fd35ad07463e21cc)* context, int targetFps)

设置超帧后的目标帧率，这个设置仅在系统送显模式下生效，对游戏送显模式无影响。该接口在游戏初次上架之后生效且仅适配OpenGL ES图形API平台。

[FG_Context_VK](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga4022ab63c2296d63dcf2c2df178508b7)* [HMS_FG_CreateContext_VK](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gac39606d03c25d898c656ab6973bb54f3)(const [FG_ContextDescription_VK](FG_ContextDescription_VK.md)* contextDescription)

创建超帧上下文实例，调用成功则返回指向[FG_Context_VK](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga4022ab63c2296d63dcf2c2df178508b7)对象的指针。该接口仅适配Vulkan图形API平台。

[FG_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga68efbf5ff41faeb835f5587654c1e669)[HMS_FG_SetAlgorithmMode_VK](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga9262d0cde377603a6ccc1239095be917)([FG_Context_VK](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga4022ab63c2296d63dcf2c2df178508b7)* context, const [FG_AlgorithmModeInfo](FG_AlgorithmModeInfo.md)* predictionModeInfo)

设置超帧算法模式，包括预测算法模式和运动估计模式，必选。该接口仅适配Vulkan图形API平台。

[FG_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga68efbf5ff41faeb835f5587654c1e669)[HMS_FG_SetResolution_VK](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga2295f5bde5b0186e0f89f7d49e3338bf)([FG_Context_VK](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga4022ab63c2296d63dcf2c2df178508b7)* context, const [FG_ResolutionInfo](FG_ResolutionInfo.md)* resolutionInfo)

设置超帧输入输出图像分辨率，必选。该接口仅适配Vulkan图形API平台。

[FG_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga68efbf5ff41faeb835f5587654c1e669)[HMS_FG_SetCvvZSemantic_VK](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga7a71df6640e6e95d5d6f67b2e24448fd)([FG_Context_VK](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga4022ab63c2296d63dcf2c2df178508b7)* context, [FG_CvvZSemantic](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga530448309918d6d703e28c61a848a267) semantic)

设置超帧齐次裁剪空间Z/W范围及深度测试函数，可选调用，未调用则默认模式设置为FG_CVV_Z_SEMANTIC_ZERO_TO_ONE_FORWARD_Z。 该接口仅适配Vulkan图形API平台。

[FG_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga68efbf5ff41faeb835f5587654c1e669)[HMS_FG_SetImageFormat_VK](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gabcb428cb2187ce986cf8ac0f1c76a3ca)([FG_Context_VK](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga4022ab63c2296d63dcf2c2df178508b7)* context, const [FG_ImageFormat_VK](FG_ImageFormat_VK.md)* format)

设置超帧输入输出图像格式，可选调用。未调用则真实帧颜色缓冲区和预测帧缓冲区图像格式默认为VK_FORMAT_R8G8B8A8_UNORM； 深度模板缓冲区图像格式默认为VK_FORMAT_D24_UNORM_S8_UINT。该接口仅适配Vulkan图形API平台。

[FG_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga68efbf5ff41faeb835f5587654c1e669)[HMS_FG_SetDepthStencilYDirectionInverted_VK](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga5148977465964658f817de45e28ab80a)([FG_Context_VK](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga4022ab63c2296d63dcf2c2df178508b7)* context, bool inverted)

设置颜色缓冲区相对深度模板缓冲区是否存在y轴翻转的标志位，可选调用，未调用则默认无翻转。该接口仅适配Vulkan图形API平台。 如果存在翻转但没有将inverted设置为true，可能导致预测帧效果异常。

[FG_Image_VK](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gabd6ee9704e997ffc2792ad3c89847019)* [HMS_FG_CreateImage_VK](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga7733f097ea5f4ae4d2aa53d11d7e60ff)([FG_Context_VK](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga4022ab63c2296d63dcf2c2df178508b7)* context, VkImage image, VkImageView view)

创建超帧输入输出图像实例。真实帧颜色缓冲区、深度模板缓冲区、预测帧缓冲区均需要通过该接口创建对应的图像实例，并传入预测帧生成接口[HMS_FG_Dispatch_VK](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga21f86a194e72e99dd54fd39080385a37)进行预测帧绘制。该接口将用户提供的图像资源和超帧算法实现之间建立关联。

[FG_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga68efbf5ff41faeb835f5587654c1e669)[HMS_FG_DestroyImage_VK](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gac850c7cd41a1aebaf9bcf943ebff372a)([FG_Context_VK](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga4022ab63c2296d63dcf2c2df178508b7)* context, [FG_Image_VK](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gabd6ee9704e997ffc2792ad3c89847019)* image)

销毁超帧输入输出图像实例，取消对应关联。

[FG_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga68efbf5ff41faeb835f5587654c1e669)[HMS_FG_Activate_VK](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga6871faa08ebf19d380301cf400c086a8)([FG_Context_VK](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga4022ab63c2296d63dcf2c2df178508b7)* context)

激活超帧上下文实例。已激活的超帧实例可调用[HMS_FG_Dispatch_VK](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga21f86a194e72e99dd54fd39080385a37)接口生成预测帧，激活超帧上下文实例前需进行实例属性的配置。该接口仅适配Vulkan图形API平台。

[FG_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga68efbf5ff41faeb835f5587654c1e669)[HMS_FG_Deactivate_VK](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gad52fbbb8dcfd929300224cb91ce96380)([FG_Context_VK](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga4022ab63c2296d63dcf2c2df178508b7)* context)

去激活超帧上下文实例，可通过[HMS_FG_Activate_VK](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga6871faa08ebf19d380301cf400c086a8)接口重新激活。

[FG_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga68efbf5ff41faeb835f5587654c1e669)[HMS_FG_IsActive_VK](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga2b8aea406b51b42083c740fbe44b3ad1)([FG_Context_VK](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga4022ab63c2296d63dcf2c2df178508b7)* context, bool* isActive)

查询超帧上下文实例是否处于激活状态。该接口仅适配Vulkan图形API平台。

[FG_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga68efbf5ff41faeb835f5587654c1e669)[HMS_FG_Dispatch_VK](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga21f86a194e72e99dd54fd39080385a37)([FG_Context_VK](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga4022ab63c2296d63dcf2c2df178508b7)* context, const [FG_DispatchDescription_VK](FG_DispatchDescription_VK.md)* desc)

配置帧预测所需的参数信息，生成预测帧，该接口仅适配Vulkan图形API平台。

[FG_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga68efbf5ff41faeb835f5587654c1e669)[HMS_FG_DestroyContext_VK](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga6be707669124e0bb6e5d61c2e24043be)([FG_Context_VK](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga4022ab63c2296d63dcf2c2df178508b7)** context)

销毁超帧上下文实例并释放内存资源，该接口仅适配Vulkan图形API平台。

[FG_ErrorCode](#ZH-CN_TOPIC_0000002418917005__ga394c554fc5d056d702180ee031ccee2c)[HMS_FG_SetIntegrationMode_VK](#section1557174711191)([FG_Context_VK](#ZH-CN_TOPIC_0000002418917005__ga4022ab63c2296d63dcf2c2df178508b7)* context, const [FG_IntegrationInfo](zh-cn_topic_0000002418916973.html)* integrationInfo)

设置帧预测集成信息，该接口仅适配Vulkan图形API平台。

[FG_ErrorCode](#ZH-CN_TOPIC_0000002418917005__ga68efbf5ff41faeb835f5587654c1e669)[HMS_FG_SetUiPredictionEnabled_VK](#section9619114861914)([FG_Context_VK](#ZH-CN_TOPIC_0000002418917005__ga4022ab63c2296d63dcf2c2df178508b7)* context, bool isEnabled)

选择是否启用UI预测功能，这个功能只能在系统送显模式下启用，在游戏送显模式下无效。该接口仅适配Vulkan图形API平台。

[FG_ErrorCode](#ZH-CN_TOPIC_0000002418917005__ga68efbf5ff41faeb835f5587654c1e669)[HMS_FG_SetTargetFps_VK](#section655214195204)([FG_Context_VK](#ZH-CN_TOPIC_0000002418917005__ga4022ab63c2296d63dcf2c2df178508b7)* context, int targetFps)

设置超帧后的目标帧率，这个设置仅在系统送显模式下生效，对游戏送显模式无影响。该接口在游戏初次上架之后生效且仅适配Vulkan图形API平台。

[OpenGTX_Context](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga3ef8c7447a236d882b625ec8434385ed)* [HMS_OpenGTX_CreateContext](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga94aadbb64ffb5382a4661790c040f1c3)([OpenGTX_DeviceInfoCallback](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga1d66cec4aa0e01696d878c330f012d7a) deviceInfoCallback)

创建OpenGTX上下文实例，每次调用会新建[OpenGTX_Context](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga3ef8c7447a236d882b625ec8434385ed)对象，并返回指向[OpenGTX_Context](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga3ef8c7447a236d882b625ec8434385ed)对象的指针。

[OpenGTX_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga97deebd9adf3e19947ec5b4615fa1d9c)[HMS_OpenGTX_Activate](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga67e6cc5b491539c5e219f9e9ef15abca)([OpenGTX_Context](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga3ef8c7447a236d882b625ec8434385ed)* context)

激活OpenGTX上下文实例。使用OpenGTX上下文实例前需要激活实例。

[OpenGTX_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga97deebd9adf3e19947ec5b4615fa1d9c)[HMS_OpenGTX_Deactivate](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gaa741745687d067180d27d3be30db7422)([OpenGTX_Context](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga3ef8c7447a236d882b625ec8434385ed)* context)

去激活OpenGTX上下文实例，可通过[HMS_OpenGTX_Activate](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga67e6cc5b491539c5e219f9e9ef15abca)重新激活。

[OpenGTX_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga97deebd9adf3e19947ec5b4615fa1d9c)[HMS_OpenGTX_SetConfiguration](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gaaa09a16f113a0a9e0014b495ff961b6e)([OpenGTX_Context](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga3ef8c7447a236d882b625ec8434385ed)* context, const [OpenGTX_ConfigDescription](OpenGTX_ConfigDescription.md)* config)

初始化OpenGTX上下文实例，配置OpenGTX实例属性。

[OpenGTX_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga97deebd9adf3e19947ec5b4615fa1d9c)[HMS_OpenGTX_DispatchFrameRenderInfo](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga0c0b0034e4a6337e509888b2a9611489)([OpenGTX_Context](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga3ef8c7447a236d882b625ec8434385ed)* context, const [OpenGTX_FrameRenderInfo](OpenGTX_FrameRenderInfo.md)* frameRenderInfo)

设置OpenGTX运行所需的场景渲染关键信息，每帧变化均需要更新。

[OpenGTX_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga97deebd9adf3e19947ec5b4615fa1d9c)[HMS_OpenGTX_DispatchGameSceneInfo](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gafd01b1b2726f10b10968cdcd73da632f)([OpenGTX_Context](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga3ef8c7447a236d882b625ec8434385ed)* context, const [OpenGTX_GameSceneInfo](OpenGTX_GameSceneInfo.md)* gameSceneInfo)

设置OpenGTX运行所需的游戏场景信息。

[OpenGTX_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga97deebd9adf3e19947ec5b4615fa1d9c)[HMS_OpenGTX_DispatchNetworkInfo](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gad7a6544a832f28ef068df580ac8a1b78)([OpenGTX_Context](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga3ef8c7447a236d882b625ec8434385ed)* context, const [OpenGTX_NetworkInfo](OpenGTX_NetworkInfo.md)* networkInfo)

设置OpenGTX运行所需的网络延迟信息。

[OpenGTX_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga97deebd9adf3e19947ec5b4615fa1d9c)[HMS_OpenGTX_DestroyContext](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga0b757b487acf42e92b06178e159b03ac)([OpenGTX_Context](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga3ef8c7447a236d882b625ec8434385ed)** context)

销毁OpenGTX上下文实例并释放内存资源。

#### 类型定义说明

#### ABR_CameraData

```ets
typedef struct [ABR_CameraData](ABR_CameraData.md) [ABR_CameraData](ABR_CameraData.md)
```

**描述**

此结构体描述游戏应用每帧的相机运动数据，ABR会结合相机运动数据自适应调整FrameBuffer（帧缓冲，下文简称Buffer）分辨率因子。

**起始版本：** 5.0.0(12)

#### ABR_Context

```ets
typedef struct [ABR_Context](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga52e8dba39ee979b70826401b3d36574e) [ABR_Context](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga52e8dba39ee979b70826401b3d36574e)
```

**描述**

此结构体描述ABR上下文。

**起始版本：** 5.0.0(12)

#### ABR_ErrorCode

```ets
typedef enum [ABR_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga72df702d70a8326b5b46c118be6ad1d7) [ABR_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga72df702d70a8326b5b46c118be6ad1d7)
```

**描述**

此枚举描述ABR接口调用错误码。

**起始版本：** 5.0.0(12)

#### ABR_RenderAPI_Type

```ets
typedef enum [ABR_RenderAPI_Type](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga9359d16ecefa21f0e6e5f29732cbf6f4) [ABR_RenderAPI_Type](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga9359d16ecefa21f0e6e5f29732cbf6f4)
```

**描述**

此枚举描述ABR支持的图形API类型。

**起始版本：** 5.0.0(12)

#### ABR_Vector3

```ets
typedef struct [ABR_Vector3](ABR_Vector3.md) [ABR_Vector3](ABR_Vector3.md)
```

**描述**

此结构体描述ABR三维向量。

**起始版本：** 5.0.0(12)

#### FG_AlgorithmModeInfo

```ets
typedef struct [FG_AlgorithmModeInfo](FG_AlgorithmModeInfo.md) [FG_AlgorithmModeInfo](FG_AlgorithmModeInfo.md)
```

**描述**

此结构体描述超帧算法模式信息。

**起始版本：** 5.0.0(12)

#### FG_Context_GLES

```ets
typedef struct [FG_Context_GLES](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga62e666292d67fd19fd35ad07463e21cc) [FG_Context_GLES](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga62e666292d67fd19fd35ad07463e21cc)
```

**描述**

此结构体描述超帧上下文，该接口仅适配OpenGL ES图形API平台。

**起始版本：** 5.0.0(12)

#### FG_Context_VK

```ets
typedef struct [FG_Context_VK](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga4022ab63c2296d63dcf2c2df178508b7) [FG_Context_VK](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga4022ab63c2296d63dcf2c2df178508b7)
```

**描述**

此结构体描述超帧上下文，该接口仅适配Vulkan图形API平台。

**起始版本：** 5.0.0(12)

#### FG_ContextDescription_VK

```ets
typedef struct [FG_ContextDescription_VK](FG_ContextDescription_VK.md) [FG_ContextDescription_VK](FG_ContextDescription_VK.md)
```

**描述**

此结构体描述创建超帧上下文实例[FG_Context_VK](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga4022ab63c2296d63dcf2c2df178508b7)所需的属性信息。

**起始版本：** 5.0.0(12)

#### FG_CvvZSemantic

```ets
typedef enum [FG_CvvZSemantic](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga530448309918d6d703e28c61a848a267) [FG_CvvZSemantic](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga530448309918d6d703e28c61a848a267)
```

**描述**

此枚举描述经过相机投影变换后，齐次裁剪空间Z/W范围及深度测试模式。

**起始版本：** 5.0.0(12)

#### FG_Dimension2D

```ets
typedef struct [FG_Dimension2D](FG_Dimension2D.md) [FG_Dimension2D](FG_Dimension2D.md)
```

**描述**

此结构体描述2D图像分辨率，以像素为单位。

**起始版本：** 5.0.0(12)

#### FG_DispatchDescription_GLES

```ets
typedef struct [FG_DispatchDescription_GLES](FG_DispatchDescription_GLES.md) [FG_DispatchDescription_GLES](FG_DispatchDescription_GLES.md)
```

**描述**

此结构体描述下发帧生成命令[HMS_FG_Dispatch_GLES](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gab135a0f59582d168d461ef115423cfb4)需要的参数信息，每一帧都需要进行更新。该接口仅适配OpenGL ES图形API平台。

**起始版本：** 5.0.0(12)

#### FG_DispatchDescription_VK

```ets
typedef struct [FG_DispatchDescription_VK](FG_DispatchDescription_VK.md) [FG_DispatchDescription_VK](FG_DispatchDescription_VK.md)
```

**描述**

此结构体描述下发帧生成命令[HMS_FG_Dispatch_VK](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga21f86a194e72e99dd54fd39080385a37)需要的参数信息，每一帧都需要进行更新。该接口仅适配Vulkan图形API平台。

**起始版本：** 5.0.0(12)

#### FG_ErrorCode

```ets
typedef enum [FG_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga68efbf5ff41faeb835f5587654c1e669) [FG_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga68efbf5ff41faeb835f5587654c1e669)
```

**描述**

此枚举描述超帧接口调用错误码。

**起始版本：** 5.0.0(12)

#### FG_Image_VK

```ets
typedef struct [FG_Image_VK](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gabd6ee9704e997ffc2792ad3c89847019) [FG_Image_VK](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gabd6ee9704e997ffc2792ad3c89847019)
```

**描述**

超帧输入输出图像结构体，该接口仅适配Vulkan图形API平台。

**起始版本：** 5.0.0(12)

#### FG_ImageFormat_GLES

```ets
typedef enum [FG_ImageFormat_GLES](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga3bec27405891e089234bf50d0589c3cd) [FG_ImageFormat_GLES](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga3bec27405891e089234bf50d0589c3cd)
```

**描述**

此枚举描述真实渲染帧颜色缓冲区和预测帧缓冲区的图像格式。该接口仅适配OpenGL ES图形API平台。

**起始版本：** 5.0.0(12)

#### FG_ImageFormat_VK

```ets
typedef struct [FG_ImageFormat_VK](FG_ImageFormat_VK.md) [FG_ImageFormat_VK](FG_ImageFormat_VK.md)
```

**描述**

此结构体描述超帧输入输出图像的格式信息，该接口仅适配Vulkan图形API平台。

**起始版本：** 5.0.0(12)

#### FG_ImageInfo_VK

```ets
typedef struct [FG_ImageInfo_VK](FG_ImageInfo_VK.md) [FG_ImageInfo_VK](FG_ImageInfo_VK.md)
```

**描述**

此结构体描述超帧输入输出图像信息。

**起始版本：** 5.0.0(12)

#### FG_ImageSync_VK

```ets
typedef struct [FG_ImageSync_VK](FG_ImageSync_VK.md) [FG_ImageSync_VK](FG_ImageSync_VK.md)
```

**描述**

此结构体描述超帧输入输出图像同步状态信息，用于创建超帧图像内存屏障。

**起始版本：** 5.0.0(12)

#### FG_Mat4x4

```ets
typedef struct [FG_Mat4x4](FG_Mat4x4.md) [FG_Mat4x4](FG_Mat4x4.md)
```

**描述**

此结构体描述列主序4x4矩阵。

**起始版本：** 5.0.0(12)

#### FG_MeMode

```ets
typedef enum [FG_MeMode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga8bd44b6bea12774dd2ee6014d696e7d1) [FG_MeMode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga8bd44b6bea12774dd2ee6014d696e7d1)
```

**描述**

此枚举描述超帧运动估计算法模式，支持基础模式和增强模式。

**起始版本：** 5.0.0(12)

#### FG_PredictionMode

```ets
typedef enum [FG_PredictionMode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gaea2169cd5ae4bf9e8a17dc58f33e8766) [FG_PredictionMode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gaea2169cd5ae4bf9e8a17dc58f33e8766)
```

**描述**

此枚举描述超帧预测算法模式。

**起始版本：** 5.0.0(12)

#### FG_PresentMode

```ets
typedef struct [FG_PresentMode](#section131101213459) [FG_PresentMode](#section131101213459)
```

**描述**

此枚举定义预测帧送显模式，支持游戏端送显预测帧模式和系统端送显预测帧模式。

**起始版本：** 5.1.0(18)

#### FG_ResolutionInfo

```ets
typedef struct [FG_ResolutionInfo](FG_ResolutionInfo.md) [FG_ResolutionInfo](FG_ResolutionInfo.md)
```

**描述**

此结构体描述超帧输入输出图像的分辨率。

**起始版本：** 5.0.0(12)

#### FG_Vec3D

```ets
typedef struct [FG_Vec3D](FG_Vec3D.md) [FG_Vec3D](FG_Vec3D.md)
```

**描述**

此结构体描述超帧三维向量。

**起始版本：** 5.0.0(12)

#### FG_PerFrameExtendedCameraInfo

```ets
typedef struct [FG_PerFrameExtendedCameraInfo](FG_PerFrameExtendedCameraInfo.md) [FG_PerFrameExtendedCameraInfo](FG_PerFrameExtendedCameraInfo.md)
```

**描述**

此结构体描述相机扩展信息。当视图投影矩阵的平移分量非常大时，可以提供更加详细的相机信息以获得更加准确的超帧预测效果。

**起始版本：** 5.0.0(12)

#### FG_IntegrationInfo

```ets
typedef struct [FG_IntegrationInfo](FG_IntegrationInfo.md) [FG_IntegrationInfo](FG_IntegrationInfo.md)
```

**描述**

此结构体描述超帧集成的信息。包括送显模式，是否需要额外缓存深度和颜色纹理，以及是否需要翻转颜色纹理。仅在[FG_PredictionMode](#ZH-CN_TOPIC_0000002418917005__gaea2169cd5ae4bf9e8a17dc58f33e8766)为FG_PREDICTION_MODE_INTERPOLATION时生效。

**起始版本：** 5.1.0(18)

#### OpenGTX_ConfigDescription

```ets
typedef struct [OpenGTX_ConfigDescription](OpenGTX_ConfigDescription.md) [OpenGTX_ConfigDescription](OpenGTX_ConfigDescription.md)
```

**描述**

此结构体描述OpenGTX属性配置。

**起始版本：** 5.0.0(12)

#### OpenGTX_Context

```ets
typedef struct [OpenGTX_Context](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga3ef8c7447a236d882b625ec8434385ed) [OpenGTX_Context](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga3ef8c7447a236d882b625ec8434385ed)
```

**描述**

此结构体描述OpenGTX上下文。

**起始版本：** 5.0.0(12)

#### OpenGTX_DeviceInfoCallback

```ets
typedef void(* OpenGTX_DeviceInfoCallback) ([OpenGTX_TempLevel](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gaeff4735d18eb3086603ab6d04e7ad133))
```

**描述**

设备的温度信息回调。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

OpenGTX_TempLevel

设备的温度级别[OpenGTX_TempLevel](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga4571f1a424d551ba387ab3ea4fd6d8b8)。

#### OpenGTX_EngineType

```ets
typedef enum [OpenGTX_EngineType](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gadd5a5e0b3b4aa3ea8b0974cba13c0389) [OpenGTX_EngineType](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gadd5a5e0b3b4aa3ea8b0974cba13c0389)
```

**描述**

此枚举描述游戏应用的底层游戏引擎类型。

**起始版本：** 5.0.0(12)

#### OpenGTX_ErrorCode

```ets
typedef enum [OpenGTX_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga97deebd9adf3e19947ec5b4615fa1d9c) [OpenGTX_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga97deebd9adf3e19947ec5b4615fa1d9c)
```

**描述**

此枚举描述OpenGTX接口调用错误码。

**起始版本：** 5.0.0(12)

#### OpenGTX_FrameRenderInfo

```ets
typedef struct [OpenGTX_FrameRenderInfo](OpenGTX_FrameRenderInfo.md) [OpenGTX_FrameRenderInfo](OpenGTX_FrameRenderInfo.md)
```

**描述**

此结构体描述帧渲染信息，游戏应用获取到帧属性后传递此参数。

**起始版本：** 5.0.0(12)

#### OpenGTX_GameSceneInfo

```ets
typedef struct [OpenGTX_GameSceneInfo](OpenGTX_GameSceneInfo.md) [OpenGTX_GameSceneInfo](OpenGTX_GameSceneInfo.md)
```

**描述**

此结构体描述游戏场景信息，游戏应用获取到场景后传递此参数。

**起始版本：** 5.0.0(12)

#### OpenGTX_GameType

```ets
typedef enum [OpenGTX_GameType](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga34d898acfaacb3750db454a9ed2038a5) [OpenGTX_GameType](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga34d898acfaacb3750db454a9ed2038a5)
```

**描述**

此枚举描述游戏应用的类型。

**起始版本：** 5.0.0(12)

#### OpenGTX_LTPO_Mode

```ets
typedef enum [OpenGTX_LTPO_Mode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gad531d05ca502b93f4153e4b1f749ed0c) [OpenGTX_LTPO_Mode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gad531d05ca502b93f4153e4b1f749ed0c)
```

**描述**

此枚举描述OpenGTX_LTPO模式类型，以控制游戏中的帧率。

**起始版本：** 5.0.0(12)

#### OpenGTX_NetworkInfo

```ets
typedef struct [OpenGTX_NetworkInfo](OpenGTX_NetworkInfo.md) [OpenGTX_NetworkInfo](OpenGTX_NetworkInfo.md)
```

**描述**

此结构体描述当前设备网络信息，游戏应用获取到网络信息后传递此参数。

**起始版本：** 5.0.0(12)

#### OpenGTX_NetworkLatency

```ets
typedef struct [OpenGTX_NetworkLatency](OpenGTX_NetworkLatency.md) [OpenGTX_NetworkLatency](OpenGTX_NetworkLatency.md)
```

**描述**

此结构体描述当前设备网络延迟信息，游戏应用获取到网络延迟后传递此参数。

**起始版本：** 5.0.0(12)

#### OpenGTX_PictureQualityMaxLevel

```ets
typedef enum [OpenGTX_PictureQualityMaxLevel](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gacd5c090213b3593e7c9ab6c93118ff8e) [OpenGTX_PictureQualityMaxLevel](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gacd5c090213b3593e7c9ab6c93118ff8e)
```

**描述**

此枚举描述游戏应用的图像质量。

**起始版本：** 5.0.0(12)

#### OpenGTX_ResolutionValue

```ets
typedef struct [OpenGTX_ResolutionValue](OpenGTX_ResolutionValue.md) [OpenGTX_ResolutionValue](OpenGTX_ResolutionValue.md)
```

**描述**

此结构体描述游戏应用的分辨率值。

**起始版本：** 5.0.0(12)

#### OpenGTX_SceneID

```ets
typedef enum [OpenGTX_SceneID](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gad7e5d2d235183dc0c6549331d6bc2932) [OpenGTX_SceneID](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gad7e5d2d235183dc0c6549331d6bc2932)
```

**描述**

此枚举描述OpenGTX算法的游戏场景类型。

**起始版本：** 5.0.0(12)

#### OpenGTX_TempLevel

```ets
typedef enum [OpenGTX_TempLevel](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gaeff4735d18eb3086603ab6d04e7ad133) [OpenGTX_TempLevel](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gaeff4735d18eb3086603ab6d04e7ad133)
```

**描述**

此枚举描述设备的温度级别。

**起始版本：** 5.0.0(12)

#### OpenGTX_Vector3

```ets
typedef struct [OpenGTX_Vector3](OpenGTX_Vector3.md) [OpenGTX_Vector3](OpenGTX_Vector3.md)
```

**描述**

此结构体描述OpenGTX三维向量。

**起始版本：** 5.0.0(12)

#### 枚举类型说明

#### ABR_ErrorCode

```ets
enum [ABR_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga72df702d70a8326b5b46c118be6ad1d7)
```

**描述**

此枚举描述ABR接口调用错误码。

**起始版本：** 5.0.0(12)

枚举值

描述

****ABR_SUCCESS

接口执行成功。

****ABR_INVALID_PARAMETER

参数检查失败，包括必选参数没有传入，参数类型错误，参数值不合法等。

****ABR_CONTEXT_CONFIG_AFTER_ACTIVE

激活ABR上下文实例后配置ABR上下文实例属性。当配置ABR上下文实例属性时ABR上下文实例处于已激活状态则返回该状态码。

****ABR_CONTEXT_NOT_CONFIG

ABR上下文实例属性未配置。当调用[HMS_ABR_Activate](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga463d8d5396bfd5f6ed800ddab616479a)函数时ABR上下文实例属性未配置或配置失败则返回该错误码。

****ABR_CONTEXT_NOT_ACTIVE

ABR上下文实例属性未激活。当调用[HMS_ABR_MarkFrameBuffer_GLES](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga821fb33620312d3adba51d30254c1ef0)函数或ABR Update相关函数时ABR上下文实例未激活则返回该错误码。

****ABR_METADATA_INVALID

无效的ABR MetaData（元数据）。当配置ABR上下文实例属性时，ABR检测到无效MetaData则返回该错误码

****ABR_FRAMEBUFFER_INVALID

无效的FrameBuffer。当调用[HMS_ABR_MarkFrameBuffer_GLES](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga821fb33620312d3adba51d30254c1ef0)函数时，ABR检测到无效FrameBuffer则返回该错误码。

#### ABR_RenderAPI_Type

```ets
enum [ABR_RenderAPI_Type](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga9359d16ecefa21f0e6e5f29732cbf6f4)
```

**描述**

此枚举描述ABR支持的图形API类型。

**起始版本：** 5.0.0(12)

枚举值

描述

****RENDER_API_GLES

OpenGL ES API

#### FG_CvvZSemantic

```ets
enum [FG_CvvZSemantic](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga530448309918d6d703e28c61a848a267)
```

**描述**

此枚举描述经过相机投影变换后，齐次裁剪空间Z/W范围及深度测试模式。

**起始版本：** 5.0.0(12)

枚举值

描述

****FG_CVV_Z_SEMANTIC_MINUS_ONE_TO_ONE_FORWARD_Z

投影变换后的齐次裁剪空间Z/W范围在[-1, 1]之间，深度测试比较函数为less equal，如OpenGL ES API平台。

****FG_CVV_Z_SEMANTIC_ZERO_TO_ONE_REVERSE_Z

投影变换后的齐次裁剪空间Z/W范围在[0, 1]之间，深度测试比较函数为greater equal，如DirectX/Vulkan API平台。

****FG_CVV_Z_SEMANTIC_MINUS_ONE_TO_ONE_REVERSE_Z

投影变换后的齐次裁剪空间Z/W范围在[-1, 1]之间，深度测试比较函数为greater equal。

****FG_CVV_Z_SEMANTIC_ZERO_TO_ONE_FORWARD_Z

投影变换后的齐次裁剪空间Z/W范围在[0, 1]之间，深度测试比较函数为less equal。

#### FG_ErrorCode

```ets
enum [FG_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga68efbf5ff41faeb835f5587654c1e669)
```

**描述**

此枚举描述超帧接口调用错误码。

**起始版本：** 5.0.0(12)

枚举值

描述

****FG_SUCCESS

接口执行成功。

****FG_INVALID_PARAMETER

参数检查失败，包括必选参数没有传入，参数类型错误，参数值不合法等。

****FG_CONTEXT_NOT_CONFIG

超帧上下文实例属性未配置。当调用[HMS_FG_Activate_GLES](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gaa5f1d5b98694100aa3e3dbb4c99ac23a)函数时超帧上下文实例属性未配置或配置失败则返回该错误码。

****FG_CONTEXT_NOT_ACTIVE

超帧上下文实例未激活。当调用[HMS_FG_Dispatch_GLES](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gab135a0f59582d168d461ef115423cfb4)函数时超帧上下文实例处于未激活状态则返回该错误码。

****FG_COLLECTING_PREVIOUS_FRAMES

超帧需要多帧历史帧信息进行运动估计，当调用[HMS_FG_Dispatch_GLES](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gab135a0f59582d168d461ef115423cfb4)函数时，如果传入真实渲染帧数量小于固定阈值（GLES基础内插模式为2，GLES基础外插模式为3，GLES增强内插模式为2，GLES增强外插模式为2，Vulkan基础内插模式为3，Vulkan基础外插模式为3），此时无预测帧生成，返回该状态码。当调用次数大于等于固定阈值后，函数调用成功则返回FG_SUCCESS。

#### FG_ImageFormat_GLES

```ets
enum [FG_ImageFormat_GLES](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga3bec27405891e089234bf50d0589c3cd)
```

**描述**

此枚举描述真实渲染帧颜色缓冲区和预测帧缓冲区的图像格式。该接口仅适配OpenGL ES图形API平台。

**起始版本：** 5.0.0(12)

枚举值

描述

****FG_FORMAT_R8G8B8A8_UNORM

GL_RGBA8图像格式。

****FG_FORMAT_R11G11B10_SFLOAT

GL_R11F_G11F_B10F图像格式。

****FG_FORMAT_R16G16B16A16_SFLOAT

GL_RGBA16F图像格式。

#### FG_MeMode

```ets
enum [FG_MeMode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga8bd44b6bea12774dd2ee6014d696e7d1)
```

**描述**

此枚举描述超帧运动估计算法模式，支持基础模式和增强模式。

**起始版本：** 5.0.0(12)

枚举值

描述

****FG_ME_MODE_BASIC

基础模式，即利用历史帧颜色信息、深度信息及相机矩阵信息进行运动估计。

****FG_ME_MODE_ENHANCED

增强模式，即利用历史帧中的几何顶点信息进行更精准的运动估计，生成的预测帧效果更优。该模式需要开发者对绘制顶点的draw call进行标记。不传入深度图的情况下切换到AI超帧算法进行预测。

#### FG_PredictionMode

```ets
enum [FG_PredictionMode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gaea2169cd5ae4bf9e8a17dc58f33e8766)
```

**描述**

此枚举描述超帧预测算法模式。

**起始版本：** 5.0.0(12)

枚举值

描述

****FG_PREDICTION_MODE_INTERPOLATION

内插模式，即通过第N-1帧真实渲染帧及第N帧真实渲染帧生成N-0.5帧预测帧。该模式适用于高渲染画质游戏和对运行平滑度要求高的游戏，如角色扮演游戏、竞速类游戏等。

****FG_PREDICTION_MODE_EXTRAPOLATION

外插模式，即通过N-1帧真实渲染帧及第N帧真实渲染帧生成N+0.5帧预测帧。该模式适用于对响应时延和操作跟手性要求高的游戏，如动作类游戏、射击类游戏等。

#### FG_PresentMode

```ets
enum FG_PresentMode
```

**描述**

此枚举定义预测帧送显模式，支持游戏端送显预测帧模式和系统端送显预测帧模式。

**起始版本：** 5.1.0(18)

枚举值

描述

****FG_PRESENT_BY_GAME

游戏申请和管理预测帧，并负责预测帧的送显。

****FG_PRESENT_BY_SYSTEM

系统申请和管理预测帧，并负责预测帧的送显。

#### OpenGTX_EngineType

```ets
enum [OpenGTX_EngineType](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gadd5a5e0b3b4aa3ea8b0974cba13c0389)
```

**描述**

此枚举描述游戏应用的底层游戏引擎类型。

**起始版本：** 5.0.0(12)

枚举值

描述

****UNITY

游戏引擎类型为UNITY。

****UNREAL

游戏引擎类型为UNREAL。

****MESSIAH

游戏引擎类型为MESSIAH。

****COCOS

游戏引擎类型为COCOS。

****OTHERS_ENGINE

游戏引擎类型为OTHERS_ENGINE。

#### OpenGTX_ErrorCode

```ets
enum [OpenGTX_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga97deebd9adf3e19947ec5b4615fa1d9c)
```

**描述**

此枚举描述OpenGTX接口调用错误码。

**起始版本：** 5.0.0(12)

枚举值

描述

****OPENGTX_SUCCESS

接口执行成功。

****OPENGTX_INVALID_PARAMETER

参数检查失败，包括必选参数没有传入，参数类型错误，参数值不合法等。

****OPENGTX_CONTEXT_NOT_CONFIG

OpenGTX上下文实例属性未配置。 当调用[HMS_OpenGTX_DispatchFrameRenderInfo](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga0c0b0034e4a6337e509888b2a9611489)等函数时，OpenGTX上下文实例未配置则返回该错误码。

****OPENGTX_CONTEXT_NOT_ACTIVE

OpenGTX上下文实例属性未激活。 当调用[HMS_OpenGTX_DispatchFrameRenderInfo](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga0c0b0034e4a6337e509888b2a9611489)等函数时，OpenGTX上下文实例未激活则返回该错误码。

#### OpenGTX_GameType

```ets
enum [OpenGTX_GameType](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga34d898acfaacb3750db454a9ed2038a5)
```

**描述**

此枚举描述游戏应用的类型。

**起始版本：** 5.0.0(12)

枚举值

描述

****MOBA

游戏应用类型为MOBA。

****RPG

游戏应用类型为RPG。

****FPS

游戏应用类型为FPS。

****RAC

游戏应用类型为RAC。

****OTHERS_TYPE

游戏应用类型为OTHERS_TYPE。

#### OpenGTX_LTPO_Mode

```ets
enum [OpenGTX_LTPO_Mode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gad531d05ca502b93f4153e4b1f749ed0c)
```

**描述**

此枚举描述OpenGTX_LTPO模式类型，以控制游戏中的帧率。

**起始版本：** 5.0.0(12)

枚举值

描述

****SCENE_MODE

场景模式。

****TOUCH_MODE

触控模式。

****ADAPTIVE_MODE

自适应模式。

#### OpenGTX_PictureQualityMaxLevel

```ets
enum [OpenGTX_PictureQualityMaxLevel](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gacd5c090213b3593e7c9ab6c93118ff8e)
```

**描述**

此枚举描述游戏应用的图像质量。

**起始版本：** 5.0.0(12)

枚举值

描述

****SD

图像质量为SD，如480p。

****HD

图像质量为HD，如720p。

****FHD

图像质量为FHD，如1080p。

****QHD

图像质量为QHD，如2k。

****UHD

图像质量为UHD，如4k。

#### OpenGTX_SceneID

```ets
enum [OpenGTX_SceneID](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gad7e5d2d235183dc0c6549331d6bc2932)
```

**描述**

此枚举描述OpenGTX算法的游戏场景类型。

**起始版本：** 5.0.0(12)

枚举值

描述

****LOGIN

游戏场景类型为登录。

****GAME_INTERFACE

游戏场景类型为游戏大厅界面。

****LOADING

游戏场景类型为游戏加载中。

****PLAYING

游戏场景类型为游戏对局中。

****SPECTATOR

游戏场景类型为游戏观战中。

****DEATH

游戏场景类型为人物战斗准备中。

****HEAVY_LOAD

游戏场景类型为重负载。

****OTHERS_SCENE

游戏场景类型为其他场景。

#### OpenGTX_TempLevel

```ets
enum [OpenGTX_TempLevel](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gaeff4735d18eb3086603ab6d04e7ad133)
```

**描述**

此枚举描述设备的温度级别。

**起始版本：** 5.0.0(12)

枚举值

描述

****TEMP_LEVEL1

温度等级1。游戏可以保持当前配置。

****TEMP_LEVEL2

温度等级2。游戏应该减少不必要的服务，如减少后台更新。

****TEMP_LEVEL3

温度等级3。游戏应该停止非重点服务。

****TEMP_LEVEL4

温度等级4。游戏应该降低游戏效果。

****TEMP_LEVEL5

温度等级5。游戏要降低游戏场景配置，如帧分辨率、帧率、画质等。

****TEMP_LEVEL6

温度等级6。游戏应保持最低配置。

#### 函数说明

#### HMS_ABR_Activate()

```ets
[ABR_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga72df702d70a8326b5b46c118be6ad1d7) HMS_ABR_Activate([ABR_Context](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga52e8dba39ee979b70826401b3d36574e)* context)
```

**描述**

激活ABR上下文实例。激活ABR上下文实例前需调用[HMS_ABR_SetTargetFps](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga6c613e02088d559b9dc1450fde15bc2a)和[HMS_ABR_SetScaleRange](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga1001c6a7739d8ce57bf851986f121bf5)接口进行实例属性的配置。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

context

已创建的ABR上下文实例，即指向[ABR_Context](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga52e8dba39ee979b70826401b3d36574e)实例的指针，非空，否则返回失败。

**返回：**

函数执行结果状态。执行成功返回ABR_SUCCESS；失败返回具体错误码，具体失败错误码可参考[ABR_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga86d5860f91dc4f1de6b381cd65389b9d)。

#### HMS_ABR_CreateContext()

```ets
[ABR_Context](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga52e8dba39ee979b70826401b3d36574e)* HMS_ABR_CreateContext([ABR_RenderAPI_Type](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga9359d16ecefa21f0e6e5f29732cbf6f4) type)
```

**描述**

创建ABR上下文实例，每次调用会新建[ABR_Context](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga52e8dba39ee979b70826401b3d36574e)对象，并返回指向[ABR_Context](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga52e8dba39ee979b70826401b3d36574e)对象的指针。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

type

图形API类型[ABR_RenderAPI_Type](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga3a6ead3a3c0f19a6434e97fda13f42f2)。

**返回：**

成功时返回指向ABR上下文结构体[ABR_Context](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga52e8dba39ee979b70826401b3d36574e)的指针，失败返回空指针。

#### HMS_ABR_Deactivate()

```ets
[ABR_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga72df702d70a8326b5b46c118be6ad1d7) HMS_ABR_Deactivate([ABR_Context](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga52e8dba39ee979b70826401b3d36574e)* context)
```

**描述**

去激活ABR上下文实例，可通过[HMS_ABR_Activate](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga463d8d5396bfd5f6ed800ddab616479a)重新激活。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

context

已创建的ABR上下文实例，即指向[ABR_Context](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga52e8dba39ee979b70826401b3d36574e)实例的指针，非空，否则返回失败。

**返回：**

函数执行结果状态。执行成功返回ABR_SUCCESS；失败返回具体错误码，具体失败错误码可参考[ABR_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga86d5860f91dc4f1de6b381cd65389b9d)。

#### HMS_ABR_DestroyContext()

```ets
[ABR_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga72df702d70a8326b5b46c118be6ad1d7) HMS_ABR_DestroyContext([ABR_Context](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga52e8dba39ee979b70826401b3d36574e)** context)
```

**描述**

销毁ABR上下文实例并释放内存资源。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

context

已创建的指向ABR上下文实例[ABR_Context](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga52e8dba39ee979b70826401b3d36574e)的二级指针，非空，否则返回失败。

**返回：**

函数执行结果状态。执行成功返回ABR_SUCCESS；失败返回具体错误码，具体失败错误码可参考[ABR_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga86d5860f91dc4f1de6b381cd65389b9d)。

#### HMS_ABR_GetScale()

```ets
[ABR_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga72df702d70a8326b5b46c118be6ad1d7) HMS_ABR_GetScale([ABR_Context](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga52e8dba39ee979b70826401b3d36574e)* context, float* scale )
```

**描述**

获取ABR Buffer分辨率因子。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

context

已创建的ABR上下文实例，即指向[ABR_Context](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga52e8dba39ee979b70826401b3d36574e)实例的指针，非空，否则返回失败。

scale

指向一个用来接收ABR分辨率因子的变量，非空，否则返回失败。scale取值范围[0.5, 1.0]。

**返回：**

函数执行结果状态。执行成功返回ABR_SUCCESS；失败返回具体错误码，具体失败错误码可参考[ABR_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga86d5860f91dc4f1de6b381cd65389b9d)。

#### HMS_ABR_GetNextScale()

```ets
[ABR_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga72df702d70a8326b5b46c118be6ad1d7) HMS_ABR_GetNextScale([ABR_Context](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga52e8dba39ee979b70826401b3d36574e)* context, float* scale)
```

**描述**

获取下一帧的ABR Buffer分辨率因子。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

context

已创建的ABR上下文实例，即指向[ABR_Context](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga52e8dba39ee979b70826401b3d36574e)实例的指针，非空，否则返回失败。

scale

指向一个用来接收ABR分辨率因子的变量，非空，否则返回失败。scale取值范围[0.5, 1.0]。

**返回：**

函数执行结果状态。执行成功返回ABR_SUCCESS；失败返回具体错误码，具体失败错误码可参考[ABR_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga86d5860f91dc4f1de6b381cd65389b9d)。

#### HMS_ABR_IsActive()

```ets
[ABR_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga72df702d70a8326b5b46c118be6ad1d7) HMS_ABR_IsActive([ABR_Context](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga52e8dba39ee979b70826401b3d36574e)* context, bool* isActive )
```

**描述**

查询ABR上下文实例是否处于激活状态。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

context

已创建的ABR上下文实例，即指向[ABR_Context](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga52e8dba39ee979b70826401b3d36574e)实例的指针，非空，否则返回失败。

isActive

ABR上下文实例的激活状态。

- true : ABR上下文实例处于激活状态；
- false : ABR上下文实例处于去激活状态。

**返回：**

函数执行结果状态。执行成功返回ABR_SUCCESS；失败返回具体错误码，具体失败错误码可参考[ABR_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga86d5860f91dc4f1de6b381cd65389b9d)。

#### HMS_ABR_MarkFrameBuffer_GLES()

```ets
[ABR_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga72df702d70a8326b5b46c118be6ad1d7) HMS_ABR_MarkFrameBuffer_GLES([ABR_Context](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga52e8dba39ee979b70826401b3d36574e)* context)
```

**描述**

标记ABR进行自适应渲染处理的GLES Buffer，需要在GLES Buffer开始渲染前调用此接口。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

context

已创建的ABR上下文实例，即指向[ABR_Context](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga52e8dba39ee979b70826401b3d36574e)实例的指针，非空，否则返回失败。

**返回：**

函数执行结果状态。执行成功返回ABR_SUCCESS；失败返回具体错误码，具体失败错误码可参考[ABR_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga86d5860f91dc4f1de6b381cd65389b9d)。

#### HMS_ABR_GetScaledTexture_GLES()

```ets
[ABR_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga72df702d70a8326b5b46c118be6ad1d7) HMS_ABR_GetScaledTexture_GLES([ABR_Context](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga52e8dba39ee979b70826401b3d36574e)* context, uint32_t originTexture, uint32_t* scaledTexture)
```

**描述**

根据原始分辨率的GLES纹理索引获取ABR自适应缩放后的GLES纹理索引。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

context

已创建的ABR上下文实例，即指向[ABR_Context](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga52e8dba39ee979b70826401b3d36574e)实例的指针，非空，否则返回失败。

originTexture

原始分辨率的GLES纹理索引。

scaledTexture

ABR自适应缩放后的GLES纹理索引。

**返回：**

函数执行结果状态。执行成功返回ABR_SUCCESS；失败返回具体错误码，具体失败错误码可参考[ABR_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga86d5860f91dc4f1de6b381cd65389b9d)。

#### HMS_ABR_SetScaleRange()

```ets
[ABR_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga72df702d70a8326b5b46c118be6ad1d7) HMS_ABR_SetScaleRange([ABR_Context](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga52e8dba39ee979b70826401b3d36574e)* context, const float minValue, const float maxValue )
```

**描述**

配置ABR上下文实例的Buffer分辨率因子范围属性。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

context

已创建的ABR上下文实例，即指向[ABR_Context](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga52e8dba39ee979b70826401b3d36574e)实例的指针，非空，否则返回失败。

minValue

ABR上下文实例的最小Buffer分辨率因子属性，取值范围[0.5, 1.0]。

maxValue

ABR上下文实例的最大Buffer分辨率因子属性，取值范围[0.5, 1.0]。

**返回：**

函数执行结果状态。执行成功返回ABR_SUCCESS；失败返回具体错误码，具体失败错误码可参考[ABR_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga86d5860f91dc4f1de6b381cd65389b9d)。

#### HMS_ABR_SetTargetFps()

```ets
[ABR_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga72df702d70a8326b5b46c118be6ad1d7) HMS_ABR_SetTargetFps([ABR_Context](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga52e8dba39ee979b70826401b3d36574e)* context, const uint32_t targetFps )
```

**描述**

配置ABR上下文实例的目标帧率属性。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

context

已创建的ABR上下文实例，即指向[ABR_Context](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga52e8dba39ee979b70826401b3d36574e)实例的指针，非空，否则返回失败。

targetFps

ABR上下文实例的目标帧率属性，取值范围[30, 120]。

**返回：**

函数执行结果状态。执行成功返回ABR_SUCCESS；失败返回具体错误码，具体失败错误码可参考[ABR_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga86d5860f91dc4f1de6b381cd65389b9d)。

#### HMS_ABR_UpdateCameraData()

```ets
[ABR_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga72df702d70a8326b5b46c118be6ad1d7) HMS_ABR_UpdateCameraData([ABR_Context](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga52e8dba39ee979b70826401b3d36574e)* context, [ABR_CameraData](ABR_CameraData.md)* data )
```

**描述**

更新每帧相机运动数据，ABR更新相机运动数据前需调用[HMS_ABR_Activate](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga463d8d5396bfd5f6ed800ddab616479a)接口激活ABR上下文实例。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

context

已创建的ABR上下文实例，即指向[ABR_Context](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga52e8dba39ee979b70826401b3d36574e)实例的指针，非空，否则返回失败。

data

游戏应用每帧的相机运动数据，即指向ABR相机运动数据[ABR_CameraData](ABR_CameraData.md)的指针，非空，否则返回失败。

**返回：**

函数执行结果状态。执行成功返回ABR_SUCCESS；失败返回具体错误码，具体失败错误码可参考[ABR_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga86d5860f91dc4f1de6b381cd65389b9d)。

#### HMS_FG_Activate_GLES()

```ets
[FG_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga68efbf5ff41faeb835f5587654c1e669) HMS_FG_Activate_GLES([FG_Context_GLES](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga62e666292d67fd19fd35ad07463e21cc)* context)
```

**描述**

激活超帧上下文实例。已激活的超帧实例可调用[HMS_FG_Dispatch_GLES](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gab135a0f59582d168d461ef115423cfb4)接口生成预测帧， 激活超帧上下文实例前需进行实例属性的配置。该接口仅适配OpenGL ES图形API平台。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

context

已创建的超帧上下文实例，即指向[FG_Context_GLES](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga62e666292d67fd19fd35ad07463e21cc)对象的指针，不允许为空。

**返回：**

函数执行结果状态。执行成功返回FG_SUCCESS；失败返回具体错误码，具体失败错误码可参考[FG_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga394c554fc5d056d702180ee031ccee2c)。

#### HMS_FG_Activate_VK()

```ets
[FG_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga68efbf5ff41faeb835f5587654c1e669) HMS_FG_Activate_VK([FG_Context_VK](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga4022ab63c2296d63dcf2c2df178508b7)* context)
```

**描述**

激活超帧上下文实例。已激活的超帧实例可调用[HMS_FG_Dispatch_VK](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga21f86a194e72e99dd54fd39080385a37)接口生成预测帧，激活超帧上下文实例前需进行实例属性的配置。该接口仅适配Vulkan图形API平台。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

context

已创建的超帧上下文实例，即指向[FG_Context_VK](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga4022ab63c2296d63dcf2c2df178508b7)对象的指针，不允许为空。

**返回：**

函数执行结果状态。执行成功返回FG_SUCCESS；失败返回具体错误码，具体失败错误码可参考[FG_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga394c554fc5d056d702180ee031ccee2c)。

#### HMS_FG_CreateContext_GLES()

```ets
[FG_Context_GLES](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga62e666292d67fd19fd35ad07463e21cc)* HMS_FG_CreateContext_GLES(void )
```

**描述**

创建超帧上下文实例，调用成功则返回指向[FG_Context_GLES](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga62e666292d67fd19fd35ad07463e21cc)对象的指针。该接口仅适配OpenGL ES图形API平台。

**起始版本：** 5.0.0(12)

**返回：**

成功时返回指向超帧上下文结构体[FG_Context_GLES](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga62e666292d67fd19fd35ad07463e21cc)对象的指针，失败返回空指针。

#### HMS_FG_CreateContext_VK()

```ets
[FG_Context_VK](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga4022ab63c2296d63dcf2c2df178508b7)* HMS_FG_CreateContext_VK(const [FG_ContextDescription_VK](FG_ContextDescription_VK.md)* contextDescription)
```

**描述**

创建超帧上下文实例，调用成功则返回指向[FG_Context_VK](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga4022ab63c2296d63dcf2c2df178508b7)对象的指针。该接口仅适配Vulkan图形API平台。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

contextDescription

指向创建超帧上下文实例所需属性信息结构体[FG_ContextDescription_VK](FG_ContextDescription_VK.md)对象的指针，不允许为空。

**返回：**

成功时返回指向超帧上下文结构体[FG_Context_VK](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga4022ab63c2296d63dcf2c2df178508b7)对象的指针，失败返回空指针。

#### HMS_FG_CreateImage_VK()

```ets
[FG_Image_VK](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gabd6ee9704e997ffc2792ad3c89847019)* HMS_FG_CreateImage_VK([FG_Context_VK](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga4022ab63c2296d63dcf2c2df178508b7)* context, VkImage image, VkImageView view )
```

**描述**

创建超帧输入输出图像实例。真实帧颜色缓冲区、深度模板缓冲区、预测帧缓冲区均需要通过该接口创建对应的图像实例，并传入预测帧生成接口[HMS_FG_Dispatch_VK](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga21f86a194e72e99dd54fd39080385a37)进行预测帧绘制。该接口将用户提供的图像资源和超帧算法实现之间建立关联。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

context

已创建的超帧上下文实例，即指向[FG_Context_VK](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga4022ab63c2296d63dcf2c2df178508b7)对象的指针，不允许为空。

image

VkImage对象。

view

VkImageView对象。

**返回：**

超帧输入输出图像实例。

#### HMS_FG_Deactivate_GLES()

```ets
[FG_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga68efbf5ff41faeb835f5587654c1e669) HMS_FG_Deactivate_GLES([FG_Context_GLES](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga62e666292d67fd19fd35ad07463e21cc)* context)
```

**描述**

去激活超帧上下文实例，可通过[HMS_FG_Activate_GLES](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gaa5f1d5b98694100aa3e3dbb4c99ac23a)接口重新激活。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

context

已创建的超帧上下文实例，即指向[FG_Context_GLES](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga62e666292d67fd19fd35ad07463e21cc)对象的指针，不允许为空。

**返回：**

函数执行结果状态。执行成功返回FG_SUCCESS；失败返回具体错误码，具体失败错误码可参考[FG_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga394c554fc5d056d702180ee031ccee2c)。

#### HMS_FG_Deactivate_VK()

```ets
[FG_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga68efbf5ff41faeb835f5587654c1e669) HMS_FG_Deactivate_VK([FG_Context_VK](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga4022ab63c2296d63dcf2c2df178508b7)* context)
```

**描述**

去激活超帧上下文实例，可通过[HMS_FG_Activate_VK](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga6871faa08ebf19d380301cf400c086a8)接口重新激活。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

context

已创建的超帧上下文实例，即指向[FG_Context_VK](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga4022ab63c2296d63dcf2c2df178508b7)对象的指针，不允许为空。

**返回：**

函数执行结果状态。执行成功返回FG_SUCCESS；失败返回具体错误码，具体失败错误码可参考[FG_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga394c554fc5d056d702180ee031ccee2c)。

#### HMS_FG_DestroyContext_GLES()

```ets
[FG_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga68efbf5ff41faeb835f5587654c1e669) HMS_FG_DestroyContext_GLES([FG_Context_GLES](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga62e666292d67fd19fd35ad07463e21cc)** context)
```

**描述**

销毁超帧上下文实例并释放内存资源。该接口仅适配OpenGL ES图形API平台。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

context

已创建的指向超帧上下文结构体[FG_Context_GLES](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga62e666292d67fd19fd35ad07463e21cc)对象的二级指针，不允许为空。

**返回：**

函数执行结果状态。执行成功返回FG_SUCCESS；失败返回具体错误码，具体失败错误码可参考[FG_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga394c554fc5d056d702180ee031ccee2c)。

#### HMS_FG_DestroyContext_VK()

```ets
[FG_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga68efbf5ff41faeb835f5587654c1e669) HMS_FG_DestroyContext_VK([FG_Context_VK](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga4022ab63c2296d63dcf2c2df178508b7)** context)
```

**描述**

销毁超帧上下文实例并释放内存资源。该接口仅适配Vulkan图形API平台。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

context

已创建的指向超帧上下文结构体[FG_Context_VK](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga4022ab63c2296d63dcf2c2df178508b7)对象的二级指针，不允许为空。

**返回：**

函数执行结果状态。执行成功返回FG_SUCCESS；失败返回具体错误码，具体失败错误码可参考[FG_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga394c554fc5d056d702180ee031ccee2c)。

#### HMS_FG_DestroyImage_VK()

```ets
[FG_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga68efbf5ff41faeb835f5587654c1e669) HMS_FG_DestroyImage_VK([FG_Context_VK](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga4022ab63c2296d63dcf2c2df178508b7)* context, [FG_Image_VK](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gabd6ee9704e997ffc2792ad3c89847019)* image )
```

**描述**

销毁超帧输入输出图像实例，取消对应关联。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

context

已创建的超帧上下文实例，即指向[FG_Context_VK](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga4022ab63c2296d63dcf2c2df178508b7)对象的指针，不允许为空。

image

指向[FG_Image_VK](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gabd6ee9704e997ffc2792ad3c89847019)对象的指针。

**返回：**

函数执行结果状态。执行成功返回FG_SUCCESS；失败返回具体错误码，具体失败错误码可参考[FG_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga394c554fc5d056d702180ee031ccee2c)。

#### HMS_FG_Dispatch_GLES()

```ets
[FG_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga68efbf5ff41faeb835f5587654c1e669) HMS_FG_Dispatch_GLES([FG_Context_GLES](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga62e666292d67fd19fd35ad07463e21cc)* context, const [FG_DispatchDescription_GLES](FG_DispatchDescription_GLES.md)* desc )
```

**描述**

配置帧预测所需的参数信息，生成预测帧，该接口仅适配OpenGL ES图形API平台。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

context

已创建的超帧上下文实例，即指向[FG_Context_GLES](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga62e666292d67fd19fd35ad07463e21cc)对象的指针，不允许为空。

desc

下发帧生成命令的参数结构体[FG_DispatchDescription_GLES](FG_DispatchDescription_GLES.md)的指针，不允许为空，需每帧更新。

**返回：**

函数执行结果状态。执行成功返回FG_SUCCESS；当输入历史帧数量未达到固定阈值时（基础内插模式为2，基础外插模式为3，增强内插模式为2，增强外插模式为2），返回FG_COLLECTING_PREVIOUS_FRAMES；当执行失败则返回具体错误码，具体失败错误码可参考[FG_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga394c554fc5d056d702180ee031ccee2c)。

#### HMS_FG_SetExtendedCameraInfo_GLES()

```ets
[FG_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga68efbf5ff41faeb835f5587654c1e669) HMS_FG_SetExtendedCameraInfo_GLES([FG_Context_GLES](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga62e666292d67fd19fd35ad07463e21cc)* context, const [FG_PerFrameExtendedCameraInfo](FG_PerFrameExtendedCameraInfo.md)* info)
```

**描述**

设置超帧相机扩展属性信息，当视图投影矩阵的平移分量非常大时，提供该信息以获得更加准确的超帧效果。可选调用，该接口仅适配OpenGL ES图形API平台。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

context

已创建的超帧上下文实例，即指向[FG_Context_GLES](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga62e666292d67fd19fd35ad07463e21cc)对象的指针，不允许为空。

info

指向相机扩展信息结构体[FG_PerFrameExtendedCameraInfo](FG_PerFrameExtendedCameraInfo.md)对象的指针，不允许为空。

**返回：**

函数执行结果状态。执行成功返回FG_SUCCESS；失败返回具体错误码，具体失败错误码可参考[FG_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga394c554fc5d056d702180ee031ccee2c)。

#### HMS_FG_Dispatch_VK()

```ets
[FG_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga68efbf5ff41faeb835f5587654c1e669) HMS_FG_Dispatch_VK([FG_Context_VK](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga4022ab63c2296d63dcf2c2df178508b7)* context, const [FG_DispatchDescription_VK](FG_DispatchDescription_VK.md)* desc )
```

**描述**

配置帧预测所需的参数信息，生成预测帧，该接口仅适配Vulkan图形API平台。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

context

已创建的超帧上下文实例，即指向[FG_Context_VK](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga4022ab63c2296d63dcf2c2df178508b7)对象的指针，不允许为空。

desc

下发帧生成命令的参数结构体[FG_DispatchDescription_VK](FG_DispatchDescription_VK.md)的指针，不允许为空，需每帧更新。

**返回：**

函数执行结果状态。执行成功返回FG_SUCCESS；当输入历史帧数量未达到固定阈值时（内插模式和外插模式均为3），返回FG_COLLECTING_PREVIOUS_FRAMES；当执行失败则返回具体错误码，具体失败错误码可参考[FG_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga394c554fc5d056d702180ee031ccee2c)。

#### HMS_FG_IsActive_GLES()

```ets
[FG_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga68efbf5ff41faeb835f5587654c1e669) HMS_FG_IsActive_GLES([FG_Context_GLES](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga62e666292d67fd19fd35ad07463e21cc)* context, bool* isActive )
```

**描述**

查询超帧上下文实例是否处于激活状态。该接口仅适配OpenGL ES图形API平台。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

context

已创建的超帧上下文实例，即指向[FG_Context_GLES](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga62e666292d67fd19fd35ad07463e21cc)对象的指针，不允许为空。

isActive

超帧上下文实例的激活状态。

true : 超帧上下文实例处于激活状态；

false : 超帧上下文实例处于未激活状态。

**返回：**

函数执行结果状态。执行成功返回FG_SUCCESS；失败返回具体错误码，具体失败错误码可参考[FG_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga394c554fc5d056d702180ee031ccee2c)。

#### HMS_FG_IsActive_VK()

```ets
[FG_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga68efbf5ff41faeb835f5587654c1e669) HMS_FG_IsActive_VK([FG_Context_VK](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga4022ab63c2296d63dcf2c2df178508b7)* context, bool* isActive )
```

**描述**

查询超帧上下文实例是否处于激活状态。该接口仅适配Vulkan图形API平台。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

context

已创建的超帧上下文实例，即指向[FG_Context_VK](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga4022ab63c2296d63dcf2c2df178508b7)对象的指针，不允许为空。

isActive

超帧上下文实例的激活状态。

true : 超帧上下文实例处于激活状态；

false : 超帧上下文实例处于未激活状态。

**返回：**

函数执行结果状态。执行成功返回FG_SUCCESS；失败返回具体错误码，具体失败错误码可参考[FG_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga394c554fc5d056d702180ee031ccee2c)。

#### HMS_FG_SetAlgorithmMode_GLES()

```ets
[FG_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga68efbf5ff41faeb835f5587654c1e669) HMS_FG_SetAlgorithmMode_GLES([FG_Context_GLES](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga62e666292d67fd19fd35ad07463e21cc)* context, const [FG_AlgorithmModeInfo](FG_AlgorithmModeInfo.md)* predictionModeInfo )
```

**描述**

设置超帧预测算法模式和运动估计模式，必选。该接口仅适配OpenGL ES图形API平台。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

context

已创建的超帧上下文实例，即指向[FG_Context_GLES](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga62e666292d67fd19fd35ad07463e21cc)对象的指针，不允许为空。

predictionModeInfo

指向超帧算法模式结构体[FG_AlgorithmModeInfo](FG_AlgorithmModeInfo.md)对象的指针，不允许为空。

**返回：**

函数执行结果状态。执行成功返回FG_SUCCESS；失败返回具体错误码，具体失败错误码可参考[FG_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga394c554fc5d056d702180ee031ccee2c)。

#### HMS_FG_SetAlgorithmMode_VK()

```ets
[FG_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga68efbf5ff41faeb835f5587654c1e669) HMS_FG_SetAlgorithmMode_VK([FG_Context_VK](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga4022ab63c2296d63dcf2c2df178508b7)* context, const [FG_AlgorithmModeInfo](FG_AlgorithmModeInfo.md)* predictionModeInfo )
```

**描述**

设置超帧算法模式，包括预测算法模式和运动估计模式，必选。该接口仅适配Vulkan图形API平台。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

context

已创建的超帧上下文实例，即指向[FG_Context_VK](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga4022ab63c2296d63dcf2c2df178508b7)对象的指针，不允许为空。

predictionModeInfo

指向超帧算法模式结构体[FG_AlgorithmModeInfo](FG_AlgorithmModeInfo.md)对象的指针，不允许为空。

**返回：**

函数执行结果状态。执行成功返回FG_SUCCESS；失败返回具体错误码，具体失败错误码可参考[FG_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga394c554fc5d056d702180ee031ccee2c)。

#### HMS_FG_SetCvvZSemantic_GLES()

```ets
[FG_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga68efbf5ff41faeb835f5587654c1e669) HMS_FG_SetCvvZSemantic_GLES([FG_Context_GLES](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga62e666292d67fd19fd35ad07463e21cc)* context, [FG_CvvZSemantic](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga530448309918d6d703e28c61a848a267) semantic )
```

**描述**

设置超帧齐次裁剪空间Z/W范围及深度测试函数，可选调用，未调用则默认模式设置为FG_CVV_Z_SEMANTIC_MINUS_ONE_TO_ONE_FORWARD_Z。该接口仅适配OpenGL ES图形API平台。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

context

已创建的超帧上下文实例，即指向[FG_Context_GLES](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga62e666292d67fd19fd35ad07463e21cc)对象的指针，不允许为空。

semantic

表示齐次裁剪空间Z/W范围及深度测试函数的枚举值。

**返回：**

函数执行结果状态。执行成功返回FG_SUCCESS；失败返回具体错误码，具体失败错误码可参考[FG_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga394c554fc5d056d702180ee031ccee2c)。

#### HMS_FG_SetCvvZSemantic_VK()

```ets
[FG_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga68efbf5ff41faeb835f5587654c1e669) HMS_FG_SetCvvZSemantic_VK([FG_Context_VK](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga4022ab63c2296d63dcf2c2df178508b7)* context, [FG_CvvZSemantic](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga530448309918d6d703e28c61a848a267) semantic )
```

**描述**

设置超帧齐次裁剪空间Z/W范围及深度测试函数，可选调用，未调用则默认模式设置为FG_CVV_Z_SEMANTIC_ZERO_TO_ONE_FORWARD_Z。 该接口仅适配Vulkan图形API平台。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

context

已创建的超帧上下文实例，即指向[FG_Context_VK](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga4022ab63c2296d63dcf2c2df178508b7)对象的指针，不允许为空。

semantic

表示齐次裁剪空间Z/W范围及深度测试函数的枚举值。

**返回：**

函数执行结果状态。执行成功返回FG_SUCCESS；失败返回具体错误码，具体失败错误码可参考[FG_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga394c554fc5d056d702180ee031ccee2c)。

#### HMS_FG_SetDepthStencilYDirectionInverted_GLES()

```ets
[FG_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga68efbf5ff41faeb835f5587654c1e669) HMS_FG_SetDepthStencilYDirectionInverted_GLES([FG_Context_GLES](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga62e666292d67fd19fd35ad07463e21cc)* context, bool inverted )
```

**描述**

设置颜色缓冲区相对深度模板缓冲区基于y轴翻转的标志位，可选调用，未调用则默认无翻转。该接口仅适配OpenGL ES图形API平台。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

context

已创建的超帧上下文实例，即指向[FG_Context_GLES](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga62e666292d67fd19fd35ad07463e21cc)对象的指针，不允许为空。

inverted

颜色缓冲区相对深度模板缓冲区基于y轴翻转的标志位。

true : 颜色缓冲区相对深度模板缓冲区基于y轴翻转180°；

false : 颜色缓冲区相对深度模板缓冲区无翻转。

**返回：**

函数执行结果状态。执行成功返回FG_SUCCESS；失败返回具体错误码，具体失败错误码可参考[FG_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga394c554fc5d056d702180ee031ccee2c)。

#### HMS_FG_SetDepthStencilYDirectionInverted_VK()

```ets
[FG_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga68efbf5ff41faeb835f5587654c1e669) HMS_FG_SetDepthStencilYDirectionInverted_VK([FG_Context_VK](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga4022ab63c2296d63dcf2c2df178508b7)* context, bool inverted )
```

**描述**

设置颜色缓冲区相对深度模板缓冲区是否存在y轴翻转的标志位，可选调用，未调用则默认无翻转。该接口仅适配Vulkan图形API平台。 如果存在翻转但没有将inverted设置为true，可能导致预测帧效果异常。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

context

已创建的超帧上下文实例，即指向[FG_Context_VK](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga4022ab63c2296d63dcf2c2df178508b7)对象的指针，不允许为空。

inverted

颜色缓冲区相对深度模板缓冲区是否存在y轴翻转的标志位。

true : 颜色缓冲区相对深度模板缓冲区基于y轴翻转180°；

false : 颜色缓冲区相对深度模板缓冲区无翻转。

**返回：**

函数执行结果状态。执行成功返回FG_SUCCESS；失败返回具体错误码，具体失败错误码可参考[FG_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga394c554fc5d056d702180ee031ccee2c)。

#### HMS_FG_SetImageFormat_GLES()

```ets
[FG_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga68efbf5ff41faeb835f5587654c1e669) HMS_FG_SetImageFormat_GLES([FG_Context_GLES](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga62e666292d67fd19fd35ad07463e21cc)* context, [FG_ImageFormat_GLES](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga3bec27405891e089234bf50d0589c3cd) format )
```

**描述**

设置真实渲染帧颜色缓冲区和预测帧缓冲区的图像格式，可选调用，未调用则模式默认设置为FG_FORMAT_R8G8B8A8_UNORM。该接口仅适配OpenGL ES图形API平台。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

context

已创建的超帧上下文实例，即指向[FG_Context_GLES](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga62e666292d67fd19fd35ad07463e21cc)对象的指针，不允许为空。

format

表示真实渲染帧颜色缓冲区和预测帧缓冲区图像格式的枚举值。

**返回：**

函数执行结果状态。执行成功返回FG_SUCCESS；失败返回具体错误码，具体失败错误码可参考[FG_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga394c554fc5d056d702180ee031ccee2c)。

#### HMS_FG_SetImageFormat_VK()

```ets
[FG_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga68efbf5ff41faeb835f5587654c1e669) HMS_FG_SetImageFormat_VK([FG_Context_VK](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga4022ab63c2296d63dcf2c2df178508b7)* context, const [FG_ImageFormat_VK](FG_ImageFormat_VK.md)* format )
```

**描述**

设置超帧输入输出图像格式，可选调用。未调用则真实帧颜色缓冲区和预测帧缓冲区图像格式默认为VK_FORMAT_R8G8B8A8_UNORM； 深度模板缓冲区图像格式默认为VK_FORMAT_D24_UNORM_S8_UINT。该接口仅适配Vulkan图形API平台。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

context

已创建的超帧上下文实例，即指向[FG_Context_VK](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga4022ab63c2296d63dcf2c2df178508b7)对象的指针，不允许为空。

format

指向超帧输入输出图像格式结构体[FG_ImageFormat_VK](FG_ImageFormat_VK.md)对象的指针，不允许为空。

**返回：**

函数执行结果状态。执行成功返回FG_SUCCESS；失败返回具体错误码，具体失败错误码可参考[FG_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga394c554fc5d056d702180ee031ccee2c)。

#### HMS_FG_SetResolution_GLES()

```ets
[FG_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga68efbf5ff41faeb835f5587654c1e669) HMS_FG_SetResolution_GLES([FG_Context_GLES](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga62e666292d67fd19fd35ad07463e21cc)* context, const [FG_ResolutionInfo](FG_ResolutionInfo.md)* resolutionInfo )
```

**描述**

设置超帧输入输出图像分辨率，必选。该接口仅适配OpenGL ES图形API平台。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

context

已创建的超帧上下文实例，即指向[FG_Context_GLES](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga62e666292d67fd19fd35ad07463e21cc)对象的指针，不允许为空。

resolutionInfo

指向超帧输入输出图像分辨率结构体[FG_ResolutionInfo](FG_ResolutionInfo.md)对象的指针，不允许为空。

**返回：**

函数执行结果状态。执行成功返回FG_SUCCESS；失败返回具体错误码，具体失败错误码可参考[FG_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga394c554fc5d056d702180ee031ccee2c)。

#### HMS_FG_SetResolution_VK()

```ets
[FG_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga68efbf5ff41faeb835f5587654c1e669) HMS_FG_SetResolution_VK([FG_Context_VK](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga4022ab63c2296d63dcf2c2df178508b7)* context, const [FG_ResolutionInfo](FG_ResolutionInfo.md)* resolutionInfo )
```

**描述**

设置超帧输入输出图像分辨率，必选。该接口仅适配Vulkan图形API平台。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

context

已创建的超帧上下文实例，即指向[FG_Context_VK](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga4022ab63c2296d63dcf2c2df178508b7)对象的指针，不允许为空。

resolutionInfo

指向超帧输入输出图像分辨率结构体[FG_ResolutionInfo](FG_ResolutionInfo.md)对象的指针，不允许为空。

**返回：**

函数执行结果状态。执行成功返回FG_SUCCESS；失败返回具体错误码，具体失败错误码可参考[FG_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga394c554fc5d056d702180ee031ccee2c)。

#### HMS_FG_SetIntegrationMode_GLES()

```ets
[FG_ErrorCode](#ZH-CN_TOPIC_0000002418917005__ga68efbf5ff41faeb835f5587654c1e669) HMS_FG_SetIntegrationMode_GLES([FG_Context_GLES](#ZH-CN_TOPIC_0000002418917005__ga62e666292d67fd19fd35ad07463e21cc)* context, const [FG_IntegrationInfo](zh-cn_topic_0000002418916973.html)* integrationInfo)
```

**描述**

设置超帧集成信息，该接口仅适配OpenGL ES图形API平台。

**起始版本：** 5.1.0(18)

**参数:**

名称

描述

context

已创建的超帧上下文实例，即指向[FG_Context_GLES](#ZH-CN_TOPIC_0000002418917005__ga62e666292d67fd19fd35ad07463e21cc)对象的指针，不允许为空。

integrationInfo

指向超帧集成信息的结构体[FG_IntegrationInfo](FG_IntegrationInfo.md)对象的指针，不允许为空。

**返回：**

函数执行结果状态。执行成功返回FG_SUCCESS；失败返回具体错误码，具体失败错误码可参考[FG_ErrorCode](#ZH-CN_TOPIC_0000002418917005__ga394c554fc5d056d702180ee031ccee2c)。

#### HMS_FG_SetIntegrationMode_VK()

```ets
[FG_ErrorCode](#ZH-CN_TOPIC_0000002418917005__ga68efbf5ff41faeb835f5587654c1e669) HMS_FG_SetIntegrationMode_VK([FG_Context_VK](#ZH-CN_TOPIC_0000002418917005__ga4022ab63c2296d63dcf2c2df178508b7)* context, const [FG_IntegrationInfo](zh-cn_topic_0000002418916973.html)* integrationInfo)
```

**描述**

设置超帧集成信息，该接口仅适配Vulkan图形API平台。

**起始版本：** 5.1.0(18)

**参数:**

名称

描述

context

已创建的超帧上下文实例，即指向[FG_Context_VK](#ZH-CN_TOPIC_0000002418917005__ga4022ab63c2296d63dcf2c2df178508b7)对象的指针，不允许为空。

integrationInfo

指向超帧集成信息的结构体[FG_IntegrationInfo](FG_IntegrationInfo.md)对象的指针，不允许为空。

**返回：**

函数执行结果状态。执行成功返回FG_SUCCESS；失败返回具体错误码，具体失败错误码可参考[FG_ErrorCode](#ZH-CN_TOPIC_0000002418917005__ga394c554fc5d056d702180ee031ccee2c)。

#### HMS_FG_SetUiPredictionEnabled_GLES()

```ets
[FG_ErrorCode](#ZH-CN_TOPIC_0000002418917005__ga68efbf5ff41faeb835f5587654c1e669) HMS_FG_SetUiPredictionEnabled_GLES([FG_Context_GLES](#ZH-CN_TOPIC_0000002418917005__ga62e666292d67fd19fd35ad07463e21cc)* context, bool isEnabled)
```

**描述**

选择是否启用UI预测功能，这个功能只能在系统送显模式下启用，在游戏送显模式下无效。该接口仅适配OpenGL ES图形API平台。

**起始版本：** 5.1.0(18)

**参数:**

名称

描述

context

已创建的超帧上下文实例，即指向[FG_Context_GLES](#ZH-CN_TOPIC_0000002418917005__ga62e666292d67fd19fd35ad07463e21cc)对象的指针，不允许为空。

isEnabled

UI预测的激活状态。

true : UI预测处于激活状态。

false : UI预测处于未激活状态。

**返回：**

函数执行结果状态。执行成功返回FG_SUCCESS；失败返回具体错误码，具体失败错误码可参考[FG_ErrorCode](#ZH-CN_TOPIC_0000002418917005__ga394c554fc5d056d702180ee031ccee2c)。

#### HMS_FG_SetUiPredictionEnabled_VK()

```ets
[FG_ErrorCode](#ZH-CN_TOPIC_0000002418917005__ga68efbf5ff41faeb835f5587654c1e669) HMS_FG_SetUiPredictionEnabled_VK([FG_Context_VK](#ZH-CN_TOPIC_0000002418917005__ga4022ab63c2296d63dcf2c2df178508b7)* context, bool isEnabled)
```

**描述**

选择是否启用UI预测功能，这个功能只能在系统送显模式下启用，在游戏送显模式下无效。该接口仅适配Vulkan图形API平台。

**起始版本：** 5.1.0(18)

**参数:**

名称

描述

context

已创建的超帧上下文实例，即指向[FG_Context_VK](#ZH-CN_TOPIC_0000002418917005__ga4022ab63c2296d63dcf2c2df178508b7)对象的指针，不允许为空。

isEnabled

UI预测的激活状态。

true : UI预测处于激活状态。

false : UI预测处于未激活状态。

**返回：**

函数执行结果状态。执行成功返回FG_SUCCESS；失败返回具体错误码，具体失败错误码可参考[FG_ErrorCode](#ZH-CN_TOPIC_0000002418917005__ga394c554fc5d056d702180ee031ccee2c)。

#### HMS_FG_SetTargetFps_GLES()

```ets
[FG_ErrorCode](#ZH-CN_TOPIC_0000002418917005__ga68efbf5ff41faeb835f5587654c1e669) HMS_FG_SetTargetFps_GLES([FG_Context_GLES](#ZH-CN_TOPIC_0000002418917005__ga62e666292d67fd19fd35ad07463e21cc)* context, int targetFps)
```

**描述**

设置超帧后的目标帧率，这个设置仅在系统送显模式下生效，对游戏送显模式无影响。该接口在游戏初次上架之后生效且仅适配OpenGL ES图形API平台。

**起始版本：** 5.1.0(18)

**参数:**

名称

描述

context

已创建的超帧上下文实例，即指向[FG_Context_GLES](#ZH-CN_TOPIC_0000002418917005__ga62e666292d67fd19fd35ad07463e21cc)对象的指针，不允许为空。

targetFps

超帧后的目标帧率。最小值为30，最大值为144。

**返回：**

函数执行结果状态。执行成功返回FG_SUCCESS；失败返回具体错误码，具体失败错误码可参考[FG_ErrorCode](#ZH-CN_TOPIC_0000002418917005__ga394c554fc5d056d702180ee031ccee2c)。

#### HMS_FG_SetTargetFps_VK()

```ets
[FG_ErrorCode](#ZH-CN_TOPIC_0000002418917005__ga68efbf5ff41faeb835f5587654c1e669) HMS_FG_SetTargetFps_VK([FG_Context_VK](#ZH-CN_TOPIC_0000002418917005__ga4022ab63c2296d63dcf2c2df178508b7)* context, int targetFps)
```

**描述**

设置超帧后的目标帧率，这个设置仅在系统送显模式下生效，对游戏送显模式无影响。该接口在游戏初次上架之后生效且仅适配Vulkan图形API平台。

**起始版本：** 5.1.0(18)

**参数:**

名称

描述

context

已创建的超帧上下文实例，即指向[FG_Context_VK](#ZH-CN_TOPIC_0000002418917005__ga4022ab63c2296d63dcf2c2df178508b7)对象的指针，不允许为空。

targetFps

超帧后的目标帧率。最小值为30，最大值为144。

**返回：**

函数执行结果状态。执行成功返回FG_SUCCESS；失败返回具体错误码，具体失败错误码可参考[FG_ErrorCode](#ZH-CN_TOPIC_0000002418917005__ga394c554fc5d056d702180ee031ccee2c)。

#### HMS_OpenGTX_Activate()

```ets
[OpenGTX_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga97deebd9adf3e19947ec5b4615fa1d9c) HMS_OpenGTX_Activate([OpenGTX_Context](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga3ef8c7447a236d882b625ec8434385ed)* context)
```

**描述**

激活OpenGTX上下文实例。使用OpenGTX上下文实例前需要激活实例。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

context

已创建的OpenGTX上下文实例，即指向[OpenGTX_Context](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga3ef8c7447a236d882b625ec8434385ed)实例的指针；非空，否则返回失败。

**返回：**

函数执行结果状态。执行成功返回OPENGTX_SUCCESS；失败返回具体错误码，具体失败错误码可参考[OpenGTX_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gaa2c657ed21a175b099bea0ed2491cc34)。

#### HMS_OpenGTX_CreateContext()

```ets
[OpenGTX_Context](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga3ef8c7447a236d882b625ec8434385ed)* HMS_OpenGTX_CreateContext([OpenGTX_DeviceInfoCallback](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga1d66cec4aa0e01696d878c330f012d7a) deviceInfoCallback)
```

**描述**

创建OpenGTX上下文实例，每次调用会新建[OpenGTX_Context](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga3ef8c7447a236d882b625ec8434385ed)对象，并返回指向[OpenGTX_Context](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga3ef8c7447a236d882b625ec8434385ed)对象的指针。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

deviceInfoCallback

设备的温度信息回调[OpenGTX_DeviceInfoCallback](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga1d66cec4aa0e01696d878c330f012d7a)。

**返回：**

成功时返回指向OpenGTX上下文结构体[OpenGTX_Context](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga3ef8c7447a236d882b625ec8434385ed)的指针，失败返回空指针。

#### HMS_OpenGTX_Deactivate()

```ets
[OpenGTX_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga97deebd9adf3e19947ec5b4615fa1d9c) HMS_OpenGTX_Deactivate([OpenGTX_Context](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga3ef8c7447a236d882b625ec8434385ed)* context)
```

**描述**

去激活OpenGTX上下文实例，可通过[HMS_OpenGTX_Activate](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga67e6cc5b491539c5e219f9e9ef15abca)重新激活。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

context

已创建的OpenGTX上下文实例，即指向[OpenGTX_Context](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga3ef8c7447a236d882b625ec8434385ed)实例的指针；非空，否则返回失败。

**返回：**

函数执行结果状态。执行成功返回OPENGTX_SUCCESS；失败返回具体错误码，具体失败错误码可参考[OpenGTX_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gaa2c657ed21a175b099bea0ed2491cc34)。

#### HMS_OpenGTX_DestroyContext()

```ets
[OpenGTX_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga97deebd9adf3e19947ec5b4615fa1d9c) HMS_OpenGTX_DestroyContext([OpenGTX_Context](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga3ef8c7447a236d882b625ec8434385ed)** context)
```

**描述**

销毁OpenGTX上下文实例并释放内存资源。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

context

已创建的OpenGTX上下文实例，即指向[OpenGTX_Context](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga3ef8c7447a236d882b625ec8434385ed)实例的指针；非空，否则返回失败。

**返回：**

函数执行结果状态。执行成功返回OPENGTX_SUCCESS；失败返回具体错误码，具体失败错误码可参考[OpenGTX_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gaa2c657ed21a175b099bea0ed2491cc34)。

#### HMS_OpenGTX_DispatchFrameRenderInfo()

```ets
[OpenGTX_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga97deebd9adf3e19947ec5b4615fa1d9c) HMS_OpenGTX_DispatchFrameRenderInfo([OpenGTX_Context](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga3ef8c7447a236d882b625ec8434385ed)* context, const [OpenGTX_FrameRenderInfo](OpenGTX_FrameRenderInfo.md)* frameRenderInfo )
```

**描述**

设置OpenGTX运行所需的场景渲染关键信息，每帧变化均需要更新。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

context

已创建的OpenGTX上下文实例，即指向[OpenGTX_Context](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga3ef8c7447a236d882b625ec8434385ed)实例的指针；非空，否则返回失败。

frameRenderInfo

帧渲染信息结构，即指向OpenGTX每帧渲染信息结构体[OpenGTX_FrameRenderInfo](OpenGTX_FrameRenderInfo.md)的指针；非空，否则返回失败。

**返回：**

函数执行结果状态。执行成功返回OPENGTX_SUCCESS；失败返回具体错误码，具体失败错误码可参考[OpenGTX_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gaa2c657ed21a175b099bea0ed2491cc34)。

#### HMS_OpenGTX_DispatchGameSceneInfo()

```ets
[OpenGTX_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga97deebd9adf3e19947ec5b4615fa1d9c) HMS_OpenGTX_DispatchGameSceneInfo([OpenGTX_Context](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga3ef8c7447a236d882b625ec8434385ed)* context, const [OpenGTX_GameSceneInfo](OpenGTX_GameSceneInfo.md)* gameSceneInfo )
```

**描述**

设置OpenGTX运行所需的游戏场景信息。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

context

已创建的OpenGTX上下文实例，即指向[OpenGTX_Context](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga3ef8c7447a236d882b625ec8434385ed)实例的指针；非空，否则返回失败。

gameSceneInfo

游戏场景信息，即指向OpenGTX场景信息结构体[OpenGTX_GameSceneInfo](OpenGTX_GameSceneInfo.md)的指针；非空，否则返回失败。

**返回：**

函数执行结果状态。执行成功返回OPENGTX_SUCCESS；失败返回具体错误码，具体失败错误码可参考[OpenGTX_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gaa2c657ed21a175b099bea0ed2491cc34)。

#### HMS_OpenGTX_DispatchNetworkInfo()

```ets
[OpenGTX_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga97deebd9adf3e19947ec5b4615fa1d9c) HMS_OpenGTX_DispatchNetworkInfo([OpenGTX_Context](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga3ef8c7447a236d882b625ec8434385ed)* context, const [OpenGTX_NetworkInfo](OpenGTX_NetworkInfo.md)* networkInfo )
```

**描述**

设置OpenGTX运行所需的网络延迟信息。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

context

已创建的OpenGTX上下文实例，即指向[OpenGTX_Context](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga3ef8c7447a236d882b625ec8434385ed)实例的指针；非空，否则返回失败。

networkInfo

网络信息，即指向OpenGTX网络信息结构体[OpenGTX_NetworkInfo](OpenGTX_NetworkInfo.md)的指针；非空，否则返回失败。

**返回：**

函数执行结果状态。执行成功返回OPENGTX_SUCCESS；失败返回具体错误码，具体失败错误码可参考[OpenGTX_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gaa2c657ed21a175b099bea0ed2491cc34)。

#### HMS_OpenGTX_SetConfiguration()

```ets
[OpenGTX_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga97deebd9adf3e19947ec5b4615fa1d9c) HMS_OpenGTX_SetConfiguration ([OpenGTX_Context](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga3ef8c7447a236d882b625ec8434385ed)* context, const [OpenGTX_ConfigDescription](OpenGTX_ConfigDescription.md)* config )
```

**描述**

初始化OpenGTX上下文实例，配置OpenGTX实例属性。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

context

已创建的OpenGTX上下文实例，即指向[OpenGTX_Context](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga3ef8c7447a236d882b625ec8434385ed)实例的指针；非空，否则返回失败。

config

OpenGTX上下文实例的初始化参数，即指向OpenGTX配置数据[OpenGTX_ConfigDescription](OpenGTX_ConfigDescription.md)的指针；非空，否则返回失败。

**返回：**

函数执行结果状态。执行成功返回OPENGTX_SUCCESS；失败返回具体错误码，具体失败错误码可参考[OpenGTX_ErrorCode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gaa2c657ed21a175b099bea0ed2491cc34)。