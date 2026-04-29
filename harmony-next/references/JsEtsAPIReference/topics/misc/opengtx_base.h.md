# opengtx_base.h

**概述**

声明不区分OpenGL ES和Vulkan图形API平台的OpenGTX接口。

引用文件： <graphics_game_sdk/opengtx_base.h>

库： libopengtx.so

系统能力： SystemCapability.GraphicsGame.RenderAccelerate

起始版本： 5.0.0(12)

相关模块： [GraphicsAccelerate](GraphicsAccelerate.md)

**汇总**

**结构体**

| 名称 | 描述 |
| --- | --- |
| struct OpenGTX_ConfigDescription | 此结构体描述OpenGTX属性配置。 |
| struct OpenGTX_GameSceneInfo | 此结构体描述游戏场景信息，游戏应用获取到场景后传递此参数。 |
| struct OpenGTX_FrameRenderInfo | 此结构体描述帧渲染信息，游戏应用获取到帧属性后传递此参数。 |
| struct OpenGTX_NetworkInfo | 此结构体描述当前设备网络信息，游戏应用获取到网络信息后传递此参数。 |
| struct OpenGTX_ResolutionValue | 此结构体描述游戏应用的分辨率值。 |
| struct OpenGTX_Vector3 | 此结构体描述OpenGTX三维向量。 |
| struct OpenGTX_NetworkLatency | 此结构体描述当前设备网络延迟信息，游戏应用获取到网络延迟后传递此参数。 |

**类型定义**

| 名称 | 描述 |
| --- | --- |
| typedef enum OpenGTX_ErrorCode OpenGTX_ErrorCode | 此枚举描述OpenGTX接口调用错误码。 |
| typedef enum OpenGTX_LTPO_Mode OpenGTX_LTPO_Mode | 此枚举描述OpenGTX_LTPO模式类型，以控制游戏中的帧率。 |
| typedef enum OpenGTX_EngineType OpenGTX_EngineType | 此枚举描述游戏应用的底层游戏引擎类型。 |
| typedef enum OpenGTX_GameType OpenGTX_GameType | 此枚举描述游戏应用的类型。 |
| typedef enum OpenGTX_SceneID OpenGTX_SceneID | 此枚举描述OpenGTX算法的游戏场景类型。 |
| typedef enum OpenGTX_PictureQualityMaxLevel OpenGTX_PictureQualityMaxLevel | 此枚举描述游戏应用的图像质量。 |
| typedef enum OpenGTX_TempLevel OpenGTX_TempLevel | 此枚举描述设备的温度级别。 |
| typedef struct OpenGTX_Context OpenGTX_Context | 此结构体描述OpenGTX上下文。 |
| typedef struct OpenGTX_ConfigDescription OpenGTX_ConfigDescription | 此结构体描述OpenGTX属性配置。 |
| typedef struct OpenGTX_GameSceneInfo OpenGTX_GameSceneInfo | 此结构体描述游戏场景信息，游戏应用获取到场景后传递此参数。 |
| typedef struct OpenGTX_FrameRenderInfo OpenGTX_FrameRenderInfo | 此结构体描述帧渲染信息，游戏应用获取到帧属性后传递此参数。 |
| typedef struct OpenGTX_NetworkInfo OpenGTX_NetworkInfo | 此结构体描述当前设备网络信息，游戏应用获取到网络信息后传递此参数。 |
| typedef struct OpenGTX_ResolutionValue OpenGTX_ResolutionValue | 此结构体描述游戏应用的分辨率值。 |
| typedef struct OpenGTX_Vector3 OpenGTX_Vector3 | 此结构体描述OpenGTX三维向量。 |
| typedef struct OpenGTX_NetworkLatency OpenGTX_NetworkLatency | 此结构体描述当前设备网络延迟信息，游戏应用获取到网络延迟后传递此参数。 |
| typedef void(* OpenGTX_DeviceInfoCallback) (OpenGTX_TempLevel) | 设备的温度信息回调。 |

**枚举**

| 名称 | 描述 |
| --- | --- |
| OpenGTX_ErrorCode { OPENGTX_SUCCESS = 0, OPENGTX_INVALID_PARAMETER = 401, OPENGTX_CONTEXT_NOT_CONFIG = 1009502001, OPENGTX_CONTEXT_NOT_ACTIVE = 1009502002 } | 此枚举描述OpenGTX接口调用错误码。 |
| OpenGTX_LTPO_Mode { SCENE_MODE = 0x0001, TOUCH_MODE = 0x0010, ADAPTIVE_MODE = 0x0100 } | 此枚举描述OpenGTX_LTPO模式类型，以控制游戏中的帧率。 |
| OpenGTX_EngineType { UNITY = 1, UNREAL = 2, MESSIAH = 3, COCOS = 4, OTHERS_ENGINE = 100 } | 此枚举描述游戏应用的底层游戏引擎类型。 |
| OpenGTX_GameType { MOBA = 1, RPG = 2, FPS = 3, RAC = 4, OTHERS_TYPE = 100 } | 此枚举描述游戏应用的类型。 |
| OpenGTX_SceneID { LOGIN = 1, GAME_INTERFACE = 2, LOADING = 3, PLAYING = 4, SPECTATOR = 5, DEATH = 6, HEAVY_LOAD = 7, OTHERS_SCENE = 100 } | 此枚举描述OpenGTX算法的游戏场景类型。 |
| OpenGTX_PictureQualityMaxLevel { SD = 1, HD = 2, FHD = 3, QHD = 4, UHD = 5 } | 此枚举描述游戏应用的图像质量。 |
| OpenGTX_TempLevel { TEMP_LEVEL1 = 1, TEMP_LEVEL2 = 2, TEMP_LEVEL3 = 3, TEMP_LEVEL4 = 4, TEMP_LEVEL5 = 5, TEMP_LEVEL6 = 6 } | 此枚举描述设备的温度级别。 |

**函数**

| 名称 | 描述 |
| --- | --- |
| OpenGTX_Context* HMS_OpenGTX_CreateContext(OpenGTX_DeviceInfoCallback deviceInfoCallback) | 创建OpenGTX上下文实例，每次调用会新建OpenGTX_Context对象，并返回指向OpenGTX_Context对象的指针。 |
| OpenGTX_ErrorCode HMS_OpenGTX_Activate(OpenGTX_Context* context) | 激活OpenGTX上下文实例。使用OpenGTX上下文实例前需要激活实例。 |
| OpenGTX_ErrorCode HMS_OpenGTX_Deactivate(OpenGTX_Context* context) | 去激活OpenGTX上下文实例，可通过HMS_OpenGTX_Activate重新激活。 |
| OpenGTX_ErrorCode HMS_OpenGTX_SetConfiguration(OpenGTX_Context* context, const OpenGTX_ConfigDescription* config) | 初始化OpenGTX上下文实例，配置OpenGTX实例属性。 |
| OpenGTX_ErrorCode HMS_OpenGTX_DispatchFrameRenderInfo(OpenGTX_Context* context, const OpenGTX_FrameRenderInfo* frameRenderInfo) | 设置OpenGTX运行所需的场景渲染关键信息，每帧变化均需要更新。 |
| OpenGTX_ErrorCode HMS_OpenGTX_DispatchGameSceneInfo(OpenGTX_Context* context, const OpenGTX_GameSceneInfo* gameSceneInfo) | 设置OpenGTX运行所需的游戏场景信息。 |
| OpenGTX_ErrorCode HMS_OpenGTX_DispatchNetworkInfo(OpenGTX_Context* context, const OpenGTX_NetworkInfo* networkInfo) | 设置OpenGTX运行所需的网络延迟信息。 |
| OpenGTX_ErrorCode HMS_OpenGTX_DestroyContext(OpenGTX_Context** context) | 销毁OpenGTX上下文实例并释放内存资源。 |