# opengtx_base.h

#### 概述

声明不区分OpenGL ES和Vulkan图形API平台的OpenGTX接口。

**库：** libopengtx.so

**系统能力：** SystemCapability.GraphicsGame.RenderAccelerate

**起始版本：** 5.0.0(12)

**相关模块：**[GraphicsAccelerate](GraphicsAccelerate.md)

#### 汇总

#### 结构体

名称

描述

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