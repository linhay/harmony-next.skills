# GamePerformance

#### 概述

为游戏场景感知模块提供C接口的定义。

**系统能力：** SystemCapability.GameService.GamePerformance

**起始版本：**5.0.2(14)

#### 汇总

#### 文件

| 名称 | 描述 |
| --- | --- |
| [game_performance.h](game_performance.h.md) | 声明游戏场景感知的基本概念。 |

#### 类型定义

| 名称 | 描述 |
| --- | --- |
| typedef struct [GamePerformance_DeviceInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga530e1cf28aa5c4d0b355dc053ce27e80) GamePerformance_DeviceInfo | 定义设备性能信息。 |
| typedef struct [GamePerformance_GpuInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gae85f740f82b3ca3f7ec9892d2f81a113) GamePerformance_GpuInfo | 定义GPU性能信息。 |
| typedef struct GamePerformance_CpuInfo GamePerformance_CpuInfo | 定义CPU性能信息。 |
| typedef struct [GamePerformance_ThermalInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga6767ea8a1d76ed32db95dc0d3a265a8a) GamePerformance_ThermalInfo | 定义温度信息。 |
| typedef struct [GamePerformance_ThermalInfoQueryParameters](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga0e825c8963101d40a987d4057033c788) GamePerformance_ThermalInfoQueryParameters | 定义温度信息的查询参数。 |
| typedef struct [GamePerformance_InitParameters](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga9ba0e813bb05d37656f9973a35fa0411) GamePerformance_InitParameters | 定义初始化参数。 |
| typedef struct [GamePerformance_PackageInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab57ecb4bce0af8b741ef4aa069df2d87) GamePerformance_PackageInfo | 定义游戏包信息。 |
| typedef struct [GamePerformance_ConfigInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab05a6dca6b3570c3b45d74a9cb8ffdc9) GamePerformance_ConfigInfo | 定义游戏配置信息。 |
| typedef struct [GamePerformance_SceneInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7) GamePerformance_SceneInfo | 定义游戏场景信息。 |
| typedef struct [GamePerformance_NetInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gaba275a8588101424676258ffa7217097) GamePerformance_NetInfo | 定义游戏网络信息。 |
| typedef struct [GamePerformance_PlayerInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga804b472fc080d73a2ce23da927ffd842) GamePerformance_PlayerInfo | 定义游戏玩家信息。 |
| typedef enum [GamePerformance_EngineType](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab7f3d09e6dd4af1692872b6b5815af45) [GamePerformance_EngineType](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga449d5fa8c8ee0fbea9188fd345401462) | 定义游戏引擎类型。 |
| typedef enum [GamePerformance_GameType](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga9c1b6f00c4769f13c510a7a871c7afd3) [GamePerformance_GameType](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga1e1370020b763cb4cce215d955ebb78d) | 定义游戏类型。 |
| typedef enum [GamePerformance_PictureQualityLevel](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64fd3d566be9f8240d0f474d52c292dd) [GamePerformance_PictureQualityLevel](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab726f445d701d96ff647efa723ef993d) | 定义画质等级。 |
| typedef enum [GamePerformance_SceneImportanceLevel](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gaf6bbf14a7010d4e99e6c758a718a08a6) [GamePerformance_SceneImportanceLevel](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga59c720e67f9586ae4f24223be1ae3dc5) | 定义游戏场景重要程度。 |
| typedef enum [GamePerformance_CpuLevel](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga11ac456fd1b33d0b1f6220af5e5cd1ce) [GamePerformance_CpuLevel](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga4d30bee20aca3ea7082302ae7164a196) | 定义CPU等级。 |
| typedef enum [GamePerformance_GpuLevel](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga48d14f66a8d484b497157458dd13a473) [GamePerformance_GpuLevel](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga12e1ee7ac06fc6bd25a87cce66d2a632) | 定义GPU等级。 |
| typedef enum [GamePerformance_DdrLevel](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gaec1b60b592a13ea85774a4d2ec8581bb) [GamePerformance_DdrLevel](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga57b549a68edbc9c84843040beb886389) | 定义DDR等级。 |
| typedef enum [GamePerformance_NetLoad](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga517e25164876d3727c407c887943aee2) [GamePerformance_NetLoad](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga638c2b6f6d0dda3138e34869635b2dd4) | 定义网络负载等级。 |
| typedef enum [GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) [GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gad952c8a450a72955d4dc24c43df7eee6) | 定义错误码。 |
| typedef enum [GamePerformance_DeviceInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga530e1cf28aa5c4d0b355dc053ce27e80)Type [GamePerformance_DeviceInfoType](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gac1d8c407b85cedf00dc6f6cf1f3ac202) | 定义设备性能信息类型。 |
| typedef void(*GamePerformance_ThermalLevelChangedCallback) ([GamePerformance_DeviceInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga530e1cf28aa5c4d0b355dc053ce27e80) *deviceInfo, void *userData) | HMS_GamePerformance_RegisterThermalLevelChangedCallback中使用的回调函数。当温度等级改变并且温度等级小于3档时，该函数将被调用一次。当温度等级大于或等于3档时，该函数将每10秒调用一次。 |

#### 枚举

| 名称 | 描述 |
| --- | --- |
| [GamePerformance_EngineType](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab7f3d09e6dd4af1692872b6b5815af45) { GAME_PERFORMANCE_ENGINE_TYPE_UNITY = 1, GAME_PERFORMANCE_ENGINE_TYPE_UNREAL = 2, GAME_PERFORMANCE_ENGINE_TYPE_MESSIAH = 3, GAME_PERFORMANCE_ENGINE_TYPE_COCOS = 4, GAME_PERFORMANCE_ENGINE_TYPE_OTHERS = 200 } | 此枚举描述引擎类型。 |
| [GamePerformance_GameType](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga9c1b6f00c4769f13c510a7a871c7afd3) { GAME_PERFORMANCE_GAME_TYPE_MOBA = 1, GAME_PERFORMANCE_GAME_TYPE_RPG = 2, GAME_PERFORMANCE_GAME_TYPE_FPS = 3, GAME_PERFORMANCE_GAME_TYPE_FTG = 4, GAME_PERFORMANCE_GAME_TYPE_RAC = 5, GAME_PERFORMANCE_GAME_TYPE_OTHERS = 200 } | 此枚举描述游戏类型。 |
| [GamePerformance_PictureQualityLevel](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64fd3d566be9f8240d0f474d52c292dd) { GAME_PERFORMANCE_PQL_SMOOTH = 1, GAME_PERFORMANCE_PQL_BALANCED = 2, GAME_PERFORMANCE_PQL_HD = 3, GAME_PERFORMANCE_PQL_HDR = 4, GAME_PERFORMANCE_PQL_UHD = 5 } | 此枚举描述画质等级。 |
| [GamePerformance_SceneImportanceLevel](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gaf6bbf14a7010d4e99e6c758a718a08a6) { GAME_PERFORMANCE_SIL_LEVEL1 = 1, GAME_PERFORMANCE_SIL_LEVEL2 = 2, GAME_PERFORMANCE_SIL_LEVEL3 = 3, GAME_PERFORMANCE_SIL_LEVEL4 = 4, GAME_PERFORMANCE_SIL_LEVEL5 = 5 } | 此枚举描述场景重要程度。 |
| [GamePerformance_CpuLevel](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga11ac456fd1b33d0b1f6220af5e5cd1ce) { GAME_PERFORMANCE_CPU_LEVEL_LOW = 1, GAME_PERFORMANCE_CPU_LEVEL_MIDDLE = 2, GAME_PERFORMANCE_CPU_LEVEL_HIGH = 3 } | 此枚举描述CPU等级。 |
| [GamePerformance_GpuLevel](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga48d14f66a8d484b497157458dd13a473) { GAME_PERFORMANCE_GPU_LEVEL_LOW = 1, GAME_PERFORMANCE_GPU_LEVEL_MIDDLE = 2, GAME_PERFORMANCE_GPU_LEVEL_HIGH = 3 } | 此枚举描述GPU等级。 |
| [GamePerformance_DdrLevel](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gaec1b60b592a13ea85774a4d2ec8581bb) { GAME_PERFORMANCE_DDR_LEVEL_LOW = 1, GAME_PERFORMANCE_DDR_LEVEL_MIDDLE = 2, GAME_PERFORMANCE_DDR_LEVEL_HIGH = 3 } | 此枚举描述DDR等级。 |
| [GamePerformance_NetLoad](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga517e25164876d3727c407c887943aee2) { GAME_PERFORMANCE_NET_LOAD_LIGHT = 1, GAME_PERFORMANCE_NET_LOAD_MODERATE = 2, GAME_PERFORMANCE_NET_LOAD_HEAVY = 3 } | 此枚举描述网络负载等级。 |
| [GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) { GAME_PERFORMANCE_SUCCESS = 0, GAME_PERFORMANCE_PARAM_INVALID = 401, GAME_PERFORMANCE_INTERNAL_ERROR = 1010300001, GAME_PERFORMANCE_AUTH_FAILED = 1010300002, GAME_PERFORMANCE_INVALID_REQUEST = 1010300003, GAME_PERFORMANCE_PARAM_ERROR = 1010300004 } | 此枚举描述错误码。 GAME_PERFORMANCE_PARAM_ERROR 从6.0.2(22)开始支持。 |
| [GamePerformance_DeviceInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga530e1cf28aa5c4d0b355dc053ce27e80)Type { GAME_PERFORMANCE_DEVICEINFO_TYPE_THERMAL = 0, GAME_PERFORMANCE_DEVICEINFO_TYPE_GPU = 1, GAME_PERFORMANCE_DEVICEINFO_TYPE_CPU = 2 } | 此枚举描述设备性能信息类型。 GAME_PERFORMANCE_DEVICEINFO_TYPE_CPU 从6.0.2(22)开始支持。 |

#### 函数

| 名称 | 描述 |
| --- | --- |
| GamePerformance_ErrorCode HMS_GamePerformance_CreateInitParameters ([GamePerformance_InitParameters](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga9ba0e813bb05d37656f9973a35fa0411) **initParameters) | 创建GamePerformance_InitParameters实例，该实例在HMS_GamePerformance_Init方法中使用。 |
| GamePerformance_ErrorCode HMS_GamePerformance_DestroyInitParameters ([GamePerformance_InitParameters](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga9ba0e813bb05d37656f9973a35fa0411) **initParameters) | 当GamePerformance_InitParameters实例不再使用，销毁该实例。 |
| GamePerformance_ErrorCode HMS_[GamePerformance_InitParameters](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga9ba0e813bb05d37656f9973a35fa0411)_SetBundleName (GamePerformance_InitParameters *initParameters, const char *bundleName) | 为GamePerformance_InitParameters实例设置包名。 |
| GamePerformance_ErrorCode HMS_[GamePerformance_InitParameters](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga9ba0e813bb05d37656f9973a35fa0411)_SetAppVersion (GamePerformance_InitParameters *initParameters, const char *appVersion) | 为GamePerformance_InitParameters实例设置版本号。 |
| GamePerformance_ErrorCode HMS_GamePerformance_Init ([GamePerformance_InitParameters](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga9ba0e813bb05d37656f9973a35fa0411) *initParameters) | 初始化游戏场景感知。 说明：调用HMS_GamePerformance_Init前，必须已设置bundleName，appVersion。 |
| GamePerformance_ErrorCode HMS_GamePerformance_CreatePackageInfo ([GamePerformance_PackageInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab57ecb4bce0af8b741ef4aa069df2d87) **packageInfo) | 创建GamePerformance_PackageInfo实例，该实例在HMS_GamePerformance_UpdatePackageInfo方法中使用。 |
| GamePerformance_ErrorCode HMS_GamePerformance_DestroyPackageInfo ([GamePerformance_PackageInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab57ecb4bce0af8b741ef4aa069df2d87) **packageInfo) | 当GamePerformance_PackageInfo实例不再使用，销毁该实例。 |
| GamePerformance_ErrorCode HMS_[GamePerformance_PackageInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab57ecb4bce0af8b741ef4aa069df2d87)_SetBundleName (GamePerformance_PackageInfo *packageInfo, const char *bundleName) | 为GamePerformance_PackageInfo实例设置包名。 |
| GamePerformance_ErrorCode HMS_[GamePerformance_PackageInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab57ecb4bce0af8b741ef4aa069df2d87)_SetAppVersion (GamePerformance_PackageInfo *packageInfo, const char *appVersion) | 为GamePerformance_PackageInfo实例设置版本号。 |
| GamePerformance_ErrorCode HMS_[GamePerformance_PackageInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab57ecb4bce0af8b741ef4aa069df2d87)_SetEngineType (GamePerformance_PackageInfo *packageInfo, const GamePerformance_EngineType engineType) | 为GamePerformance_PackageInfo实例设置引擎类型。 |
| GamePerformance_ErrorCode HMS_[GamePerformance_PackageInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab57ecb4bce0af8b741ef4aa069df2d87)_SetEngineVersion (GamePerformance_PackageInfo *packageInfo, const char *engineVersion) | 为GamePerformance_PackageInfo实例设置引擎版本号。 |
| GamePerformance_ErrorCode HMS_[GamePerformance_PackageInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab57ecb4bce0af8b741ef4aa069df2d87)_SetGameType (GamePerformance_PackageInfo *packageInfo, const GamePerformance_GameType gameType) | 为GamePerformance_PackageInfo实例设置游戏类型。 |
| GamePerformance_ErrorCode HMS_[GamePerformance_PackageInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab57ecb4bce0af8b741ef4aa069df2d87)_SetVulkanSupported (GamePerformance_PackageInfo *packageInfo, const bool vulkanSupported) | 为GamePerformance_PackageInfo实例设置是否支持vulkan。 |
| GamePerformance_ErrorCode HMS_GamePerformance_UpdatePackageInfo ([GamePerformance_PackageInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab57ecb4bce0af8b741ef4aa069df2d87) *packageInfo) | 更新游戏包信息。 说明：调用HMS_GamePerformance_UpdatePackageInfo前，必须已设置bundleName，appVersion。 |
| GamePerformance_ErrorCode HMS_GamePerformance_CreateConfigInfo ([GamePerformance_ConfigInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab05a6dca6b3570c3b45d74a9cb8ffdc9) **configInfo) | 创建GamePerformance_ConfigInfo实例，该实例在HMS_GamePerformance_UpdateConfigInfo方法中使用。 |
| GamePerformance_ErrorCode HMS_GamePerformance_DestroyConfigInfo ([GamePerformance_ConfigInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab05a6dca6b3570c3b45d74a9cb8ffdc9) **configInfo) | 当GamePerformance_ConfigInfo实例不再使用，销毁该实例。 |
| GamePerformance_ErrorCode HMS_[GamePerformance_ConfigInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab05a6dca6b3570c3b45d74a9cb8ffdc9)_SetMaxPictureQualityLevel (GamePerformance_ConfigInfo *configInfo, const GamePerformance_PictureQualityLevel maxPictureQualityLevel) | 为GamePerformance_ConfigInfo实例设置最大画质等级。 |
| GamePerformance_ErrorCode HMS_[GamePerformance_ConfigInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab05a6dca6b3570c3b45d74a9cb8ffdc9)_SetCurrentPictureQualityLevel (GamePerformance_ConfigInfo *configInfo, const GamePerformance_PictureQualityLevel currentPictureQualityLevel) | 为GamePerformance_ConfigInfo实例设置当前画质等级。 |
| GamePerformance_ErrorCode HMS_[GamePerformance_ConfigInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab05a6dca6b3570c3b45d74a9cb8ffdc9)_SetMaxFrameRate (GamePerformance_ConfigInfo *configInfo, const int64_t maxFrameRate) | 为GamePerformance_ConfigInfo实例设置最大帧率。 |
| GamePerformance_ErrorCode HMS_[GamePerformance_ConfigInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab05a6dca6b3570c3b45d74a9cb8ffdc9)_SetCurrentFrameRate (GamePerformance_ConfigInfo *configInfo, const int64_t currentFrameRate) | 为GamePerformance_ConfigInfo实例设置当前帧率。 |
| GamePerformance_ErrorCode HMS_[GamePerformance_ConfigInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab05a6dca6b3570c3b45d74a9cb8ffdc9)_SetMaxResolution (GamePerformance_ConfigInfo *configInfo, const char *maxResolution) | 为GamePerformance_ConfigInfo实例设置最大分辨率。 |
| GamePerformance_ErrorCode HMS_[GamePerformance_ConfigInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab05a6dca6b3570c3b45d74a9cb8ffdc9)_SetCurrentResolution (GamePerformance_ConfigInfo *configInfo, const char *currentResolution) | 为GamePerformance_ConfigInfo实例设置当前分辨率。 |
| GamePerformance_ErrorCode HMS_[GamePerformance_ConfigInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab05a6dca6b3570c3b45d74a9cb8ffdc9)_SetAntiAliasingEnabled (GamePerformance_ConfigInfo *configInfo, const bool antiAliasingEnabled) | 为GamePerformance_ConfigInfo实例设置是否开启抗锯齿。 |
| GamePerformance_ErrorCode HMS_[GamePerformance_ConfigInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab05a6dca6b3570c3b45d74a9cb8ffdc9)_SetShadowEnabled (GamePerformance_ConfigInfo *configInfo, const bool shadowEnabled) | 为GamePerformance_ConfigInfo实例设置是否开启阴影。 |
| GamePerformance_ErrorCode HMS_[GamePerformance_ConfigInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab05a6dca6b3570c3b45d74a9cb8ffdc9)_SetMultithreadingEnabled (GamePerformance_ConfigInfo *configInfo, const bool multithreadingEnabled) | 为GamePerformance_ConfigInfo实例设置开启多线程。 |
| GamePerformance_ErrorCode HMS_[GamePerformance_ConfigInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab05a6dca6b3570c3b45d74a9cb8ffdc9)_SetParticleEnabled (GamePerformance_ConfigInfo *configInfo, const bool particleEnabled) | 为GamePerformance_ConfigInfo实例设置粒子效果。 |
| GamePerformance_ErrorCode HMS_[GamePerformance_ConfigInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab05a6dca6b3570c3b45d74a9cb8ffdc9)_SetHdModeEnabled (GamePerformance_ConfigInfo *configInfo, const bool hdModeEnabled) | 为GamePerformance_ConfigInfo实例设置开启高清模式。 |
| GamePerformance_ErrorCode HMS_GamePerformance_UpdateConfigInfo ([GamePerformance_ConfigInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab05a6dca6b3570c3b45d74a9cb8ffdc9) *configInfo) | 更新游戏配置信息。 |
| GamePerformance_ErrorCode HMS_GamePerformance_CreateSceneInfo ([GamePerformance_SceneInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7) **sceneInfo) | 创建GamePerformance_SceneInfo实例，该实例在HMS_GamePerformance_UpdateSceneInfo方法中使用。 |
| GamePerformance_ErrorCode HMS_GamePerformance_DestroySceneInfo ([GamePerformance_SceneInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7) **sceneInfo) | 当GamePerformance_SceneInfo实例不再使用，销毁该实例。 |
| GamePerformance_ErrorCode HMS_[GamePerformance_SceneInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7)_SetSceneID (GamePerformance_SceneInfo *sceneInfo, const int64_t sceneID) | 为GamePerformance_SceneInfo实例设置场景ID。 |
| GamePerformance_ErrorCode HMS_[GamePerformance_SceneInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7)_SetDescription (GamePerformance_SceneInfo *sceneInfo, const char *description) | 为GamePerformance_SceneInfo实例设置场景描述。 |
| GamePerformance_ErrorCode HMS_[GamePerformance_SceneInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7)_SetSubSceneID (GamePerformance_SceneInfo *sceneInfo, const char *subSceneID) | 为GamePerformance_SceneInfo实例设置子场景ID。 |
| GamePerformance_ErrorCode HMS_[GamePerformance_SceneInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7)_SetSubDescription (GamePerformance_SceneInfo *sceneInfo, const char *subDescription) | 为GamePerformance_SceneInfo实例设置子场景描述。 |
| GamePerformance_ErrorCode HMS_[GamePerformance_SceneInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7)_SetImportanceLevel (GamePerformance_SceneInfo *sceneInfo, const GamePerformance_SceneImportanceLevel importanceLevel) | 为GamePerformance_SceneInfo实例设置场景重要程度。 |
| GamePerformance_ErrorCode HMS_[GamePerformance_SceneInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7)_SetSceneFrequency (GamePerformance_SceneInfo *sceneInfo, const int64_t sceneFrequency) | 为GamePerformance_SceneInfo实例设置该场景在一局游戏中出现的次数。 |
| GamePerformance_ErrorCode HMS_[GamePerformance_SceneInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7)_SetSceneTime (GamePerformance_SceneInfo *sceneInfo, const int64_t sceneTime) | 为GamePerformance_SceneInfo实例设置场景持续时间。 |
| GamePerformance_ErrorCode HMS_[GamePerformance_SceneInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7)_SetRecommendedCpuLevel (GamePerformance_SceneInfo *sceneInfo, const GamePerformance_CpuLevel recommendedCpuLevel) | 为GamePerformance_SceneInfo实例设置推荐的CPU等级。 |
| GamePerformance_ErrorCode HMS_[GamePerformance_SceneInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7)_SetRecommendedGpuLevel (GamePerformance_SceneInfo *sceneInfo, const GamePerformance_GpuLevel recommendedGpuLevel) | 为GamePerformance_SceneInfo实例设置推荐的GPU等级。 |
| GamePerformance_ErrorCode HMS_[GamePerformance_SceneInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7)_SetRecommendedDdrLevel (GamePerformance_SceneInfo *sceneInfo, const GamePerformance_DdrLevel recommendedDdrLevel) | 为GamePerformance_SceneInfo实例设置推荐的DDR等级。 |
| GamePerformance_ErrorCode HMS_[GamePerformance_SceneInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7)_SetMaxFrameRate (GamePerformance_SceneInfo *sceneInfo, const int64_t maxFrameRate) | 为GamePerformance_SceneInfo实例设置场景最大帧率。 |
| GamePerformance_ErrorCode HMS_[GamePerformance_SceneInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7)_SetCurrentFrameRate (GamePerformance_SceneInfo *sceneInfo, const int64_t currentFrameRate) | 为GamePerformance_SceneInfo实例设置场景当前帧率。 |
| GamePerformance_ErrorCode HMS_[GamePerformance_SceneInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7)_SetKeyThread (GamePerformance_SceneInfo *sceneInfo, const char *keyThread) | 为GamePerformance_SceneInfo实例设置关键线程。 |
| GamePerformance_ErrorCode HMS_[GamePerformance_SceneInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7)_SetDrawCallCount (GamePerformance_SceneInfo *sceneInfo, const int64_t drawCallCount) | 为GamePerformance_SceneInfo实例设置每帧的平均Drawcall数。 |
| GamePerformance_ErrorCode HMS_[GamePerformance_SceneInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7)_SetVertexCount (GamePerformance_SceneInfo *sceneInfo, const int64_t vertexCount) | 为GamePerformance_SceneInfo实例设置每帧的平均模型顶点数。 |
| GamePerformance_ErrorCode HMS_[GamePerformance_SceneInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7)_SetTriangleCount (GamePerformance_SceneInfo *sceneInfo, const int64_t triangleCount) | 为GamePerformance_SceneInfo实例设置每帧的平均模型三角形数。 |
| GamePerformance_ErrorCode HMS_[GamePerformance_SceneInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7)_SetShaderCount (GamePerformance_SceneInfo *sceneInfo, const int64_t shaderCount) | 为GamePerformance_SceneInfo实例设置每帧的平均shader数量。 |
| GamePerformance_ErrorCode HMS_[GamePerformance_SceneInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7)_SetTextureCount (GamePerformance_SceneInfo *sceneInfo, const int64_t textureCount) | 为GamePerformance_SceneInfo实例设置每帧的平均纹理数量。 |
| GamePerformance_ErrorCode HMS_[GamePerformance_SceneInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7)_SetMeshCount (GamePerformance_SceneInfo *sceneInfo, const int64_t meshCount) | 为GamePerformance_SceneInfo实例设置每帧的平均mesh数量。 |
| GamePerformance_ErrorCode HMS_[GamePerformance_SceneInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7)_SetChannelCount (GamePerformance_SceneInfo *sceneInfo, const int64_t channelCount) | 为GamePerformance_SceneInfo实例设置每帧渲染的通道数。 |
| GamePerformance_ErrorCode HMS_[GamePerformance_SceneInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7)_SetParticipantCount (GamePerformance_SceneInfo *sceneInfo, const int64_t participantCount) | 为GamePerformance_SceneInfo实例设置场景下的同屏人数。 |
| GamePerformance_ErrorCode HMS_GamePerformance_UpdateSceneInfo ([GamePerformance_SceneInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7) *sceneInfo) | 更新游戏场景信息。 说明：调用HMS_GamePerformance_UpdateSceneInfo前，必须已设置sceneID，importanceLevel。 |
| GamePerformance_ErrorCode HMS_GamePerformance_CreateNetInfo ([GamePerformance_NetInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gaba275a8588101424676258ffa7217097) **netInfo) | 创建GamePerformance_NetInfo实例，该实例在HMS_GamePerformance_UpdateNetInfo方法中使用。 |
| GamePerformance_ErrorCode HMS_GamePerformance_DestroyNetInfo ([GamePerformance_NetInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gaba275a8588101424676258ffa7217097) **netInfo) | 当GamePerformance_NetInfo实例不再使用，销毁该实例。 |
| GamePerformance_ErrorCode HMS_[GamePerformance_NetInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gaba275a8588101424676258ffa7217097)_SetTotalLatency (GamePerformance_NetInfo *netInfo, const int64_t total) | 为GamePerformance_NetInfo实例设置总网络时延。 |
| GamePerformance_ErrorCode HMS_[GamePerformance_NetInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gaba275a8588101424676258ffa7217097)_SetUplinkLatency (GamePerformance_NetInfo *netInfo, const int64_t up) | 为GamePerformance_NetInfo实例设置上行网络时延。 |
| GamePerformance_ErrorCode HMS_[GamePerformance_NetInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gaba275a8588101424676258ffa7217097)_SetDownlinkLatency (GamePerformance_NetInfo *netInfo, const int64_t down) | 为GamePerformance_NetInfo实例设置下行网络时延。 |
| GamePerformance_ErrorCode HMS_[GamePerformance_NetInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gaba275a8588101424676258ffa7217097)_SetServerLatency (GamePerformance_NetInfo *netInfo, const int64_t server) | 为GamePerformance_NetInfo实例设置服务器网络时延。 |
| GamePerformance_ErrorCode HMS_[GamePerformance_NetInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gaba275a8588101424676258ffa7217097)_SetNetLoad (GamePerformance_NetInfo *netInfo, const GamePerformance_NetLoad netLoad) | 为GamePerformance_NetInfo实例设置网络负载。 |
| GamePerformance_ErrorCode HMS_GamePerformance_UpdateNetInfo ([GamePerformance_NetInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gaba275a8588101424676258ffa7217097) *netInfo) | 更新游戏网络信息。 说明：调用HMS_GamePerformance_UpdateNetInfo前必须已设置totalLatency。 |
| GamePerformance_ErrorCode HMS_GamePerformance_CreatePlayerInfo ([GamePerformance_PlayerInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga804b472fc080d73a2ce23da927ffd842) **playerInfo) | 创建GamePerformance_PlayerInfo实例，该实例在HMS_GamePerformance_UpdatePlayerInfo方法中使用。 |
| GamePerformance_ErrorCode HMS_GamePerformance_DestroyPlayerInfo ([GamePerformance_PlayerInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga804b472fc080d73a2ce23da927ffd842) **playerInfo) | 当GamePerformance_PlayerInfo实例不再使用，销毁该实例。 |
| GamePerformance_ErrorCode HMS_[GamePerformance_PlayerInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga804b472fc080d73a2ce23da927ffd842)_SetGamePlayerId (GamePerformance_PlayerInfo *playerInfo, const char *gamePlayerId) | 为GamePerformance_PlayerInfo实例设置游戏玩家ID。 说明：gamePlayerId、teamPlayerId和thirdOpenId不能同时为空。 |
| GamePerformance_ErrorCode HMS_[GamePerformance_PlayerInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga804b472fc080d73a2ce23da927ffd842)_SetTeamPlayerId (GamePerformance_PlayerInfo *playerInfo, const char *teamPlayerId) | 为GamePerformance_PlayerInfo实例设置团队玩家ID。 说明：gamePlayerId、teamPlayerId和thirdOpenId不能同时为空。 |
| GamePerformance_ErrorCode HMS_[GamePerformance_PlayerInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga804b472fc080d73a2ce23da927ffd842)_SetThirdOpenId (GamePerformance_PlayerInfo *playerInfo, const char *thirdOpenId) | 为GamePerformance_PlayerInfo实例设置游戏官方账号。 说明：gamePlayerId、teamPlayerId和thirdOpenId不能同时为空。 |
| GamePerformance_ErrorCode HMS_GamePerformance_UpdatePlayerInfo ([GamePerformance_PlayerInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga804b472fc080d73a2ce23da927ffd842) *playerInfo) | 更新游戏玩家信息。 |
| GamePerformance_ErrorCode HMS_GamePerformance_RegisterThermalLevelChangedCallback ([GamePerformance_DeviceInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga530e1cf28aa5c4d0b355dc053ce27e80)Type *types[], size_t size, GamePerformance_ThermalLevelChangedCallback callback, void *userData) | 订阅温度变化事件，注册温度变化回调，当达到触发点时，将调用回调函数。 |
| [GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) HMS_GamePerformance_UnregisterThermalLevelChangedCallback (GamePerformance_ThermalLevelChangedCallback callback) | 取消注册指定温度变化回调。 |
| [GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) HMS_GamePerformance_UnregisterAllThermalLevelChangedCallbacks (void) | 取消注册所有温度变化回调。 |
| GamePerformance_ErrorCode HMS_GamePerformance_CreateThermalInfoQueryParameters ([GamePerformance_ThermalInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga6767ea8a1d76ed32db95dc0d3a265a8a)QueryParameters **parameters) | 创建GamePerformance_ThermalInfoQueryParameters实例，该实例在HMS_GamePerformance_QueryThermalInfo方法中使用。 |
| GamePerformance_ErrorCode HMS_GamePerformance_DestroyThermalInfoQueryParameters ([GamePerformance_ThermalInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga6767ea8a1d76ed32db95dc0d3a265a8a)QueryParameters **parameters) | 当GamePerformance_ThermalInfoQueryParameters实例不再使用，销毁该实例。 |
| GamePerformance_ErrorCode HMS_[GamePerformance_ThermalInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga6767ea8a1d76ed32db95dc0d3a265a8a)QueryParameters_SetNeedsPrediction (GamePerformance_ThermalInfoQueryParameters *parameters, const bool needsPrediction) | 为GamePerformance_ThermalInfoQueryParameters实例设置是否需要预测温升趋势。 |
| GamePerformance_ErrorCode HMS_[GamePerformance_ThermalInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga6767ea8a1d76ed32db95dc0d3a265a8a)QueryParameters_SetTargetThermalLevel (GamePerformance_ThermalInfoQueryParameters *parameters, const int32_t targetThermalLevel) | 为GamePerformance_ThermalInfoQueryParameters实例设置预测温升趋势的目标温度等级。 |
| GamePerformance_ErrorCode HMS_GamePerformance_QueryThermalInfo ([GamePerformance_ThermalInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga6767ea8a1d76ed32db95dc0d3a265a8a)QueryParameters *parameters，GamePerformance_ThermalInfo **thermalInfo) | 查询温度信息。 |
| GamePerformance_ErrorCode HMS_GamePerformance_DestroyThermalInfo ([GamePerformance_ThermalInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga6767ea8a1d76ed32db95dc0d3a265a8a) **thermalInfo) | 当GamePerformance_ThermalInfo实例不再使用，销毁该实例。 |
| GamePerformance_ErrorCode HMS_GamePerformance_QueryGpuInfo ([GamePerformance_GpuInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gae85f740f82b3ca3f7ec9892d2f81a113) **gpuInfo) | 查询GPU性能信息。 |
| GamePerformance_ErrorCode HMS_GamePerformance_DestroyGpuInfo ([GamePerformance_GpuInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gae85f740f82b3ca3f7ec9892d2f81a113) **gpuInfo) | 当GamePerformance_GpuInfo实例不再使用，销毁该实例。 |
| [GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) HMS_GamePerformance_QueryCpuInfo (GamePerformance_CpuInfo **cpuInfo) | 查询CPU性能信息。 |
| [GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) HMS_GamePerformance_DestroyCpuInfo (GamePerformance_CpuInfo **cpuInfo) | 当GamePerformance_CpuInfo实例不再使用，销毁该实例。 |
| GamePerformance_ErrorCode HMS_[GamePerformance_DeviceInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga530e1cf28aa5c4d0b355dc053ce27e80)_GetThermalInfo (GamePerformance_DeviceInfo *deviceInfo, GamePerformance_ThermalInfo **thermalInfo) | 从设备性能信息GamePerformance_DeviceInfo中获取温度信息GamePerformance_ThermalInfo。 |
| GamePerformance_ErrorCode HMS_[GamePerformance_ThermalInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga6767ea8a1d76ed32db95dc0d3a265a8a)_GetThermalMargin (GamePerformance_ThermalInfo *thermalInfo, int32_t *thermalMargin) | 从温度信息GamePerformance_ThermalInfo中获取温度时间裕量。 |
| GamePerformance_ErrorCode HMS_[GamePerformance_ThermalInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga6767ea8a1d76ed32db95dc0d3a265a8a)_GetThermalTrend (GamePerformance_ThermalInfo *thermalInfo, int32_t *thermalTrend) | 从GamePerformance_ThermalInfo中获取温升趋势。 |
| GamePerformance_ErrorCode HMS_[GamePerformance_ThermalInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga6767ea8a1d76ed32db95dc0d3a265a8a)_GetThermalLevel (GamePerformance_ThermalInfo *thermalInfo, int32_t *thermalLevel) | 从GamePerformance_ThermalInfo中获取温度等级。 |
| GamePerformance_ErrorCode HMS_[GamePerformance_ThermalInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga6767ea8a1d76ed32db95dc0d3a265a8a)_GetRecommendNormalizedCurrent (GamePerformance_ThermalInfo *thermalInfo, int32_t *recommendCurrent) | 从GamePerformance_ThermalInfo中获取系统建议的工作电流。若当前的工作电流高于此值，温升趋势thermalTrend会大于0，设备有发烫风险。 |
| GamePerformance_ErrorCode HMS_[GamePerformance_ThermalInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga6767ea8a1d76ed32db95dc0d3a265a8a)_GetNowNormalizedCurrent (GamePerformance_ThermalInfo *thermalInfo, int32_t *nowCurrent) | 从GamePerformance_ThermalInfo中获取当前的工作电流。 |
| GamePerformance_ErrorCode HMS_[GamePerformance_ThermalInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga6767ea8a1d76ed32db95dc0d3a265a8a)_GetRecommendMaxNormalizedCurrent (GamePerformance_ThermalInfo *thermalInfo, int32_t *recommendMaxCurrent) | 从GamePerformance_ThermalInfo中获取系统建议的最大工作电流。若当前的工作电流高于此值，设备会立即发烫。 |
| GamePerformance_ErrorCode HMS_[GamePerformance_DeviceInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga530e1cf28aa5c4d0b355dc053ce27e80)_GetGpuInfo (GamePerformance_DeviceInfo *deviceInfo, GamePerformance_GpuInfo **gpuInfo) | 从设备性能信息GamePerformance_DeviceInfo中获取GPU性能信息GamePerformance_GpuInfo。 |
| GamePerformance_ErrorCode HMS_[GamePerformance_GpuInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gae85f740f82b3ca3f7ec9892d2f81a113)_GetGpuLoadLevel (GamePerformance_GpuInfo *gpuInfo, int32_t *gpuLoadLevel) | 从GamePerformance_GpuInfo中获取GPU负载信息。 |
| GamePerformance_ErrorCode HMS_[GamePerformance_GpuInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gae85f740f82b3ca3f7ec9892d2f81a113)_GetVertexLoadLevel (GamePerformance_GpuInfo *gpuInfo, int32_t *vertexLoadLevel) | 从GamePerformance_GpuInfo中获取GPU顶点处理负载等级。 |
| GamePerformance_ErrorCode HMS_[GamePerformance_GpuInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gae85f740f82b3ca3f7ec9892d2f81a113)_GetFragmentLoadLevel (GamePerformance_GpuInfo *gpuInfo, int32_t *fragmentLoadLevel) | 从GamePerformance_GpuInfo中获取GPU片元处理负载等级。 |
| GamePerformance_ErrorCode HMS_[GamePerformance_GpuInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gae85f740f82b3ca3f7ec9892d2f81a113)_GetTextureLoadLevel (GamePerformance_GpuInfo *gpuInfo, int32_t *textureLoadLevel) | 从GamePerformance_GpuInfo中获取GPU纹理处理负载等级。 |
| GamePerformance_ErrorCode HMS_[GamePerformance_GpuInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gae85f740f82b3ca3f7ec9892d2f81a113)_GetBandwidthLoadLevel (GamePerformance_GpuInfo *gpuInfo, int32_t *bandwidthLoadLevel) | 从GamePerformance_GpuInfo中获取GPU带宽负载等级。 |
| GamePerformance_ErrorCode HMS_[GamePerformance_GpuInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gae85f740f82b3ca3f7ec9892d2f81a113)_GetCurrentFrequency (GamePerformance_GpuInfo *gpuInfo, int32_t *currentFrequency) | 从GamePerformance_GpuInfo中获取GPU频点信息。 |
| GamePerformance_ErrorCode HMS_[GamePerformance_DeviceInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga530e1cf28aa5c4d0b355dc053ce27e80)_GetCpuInfo (GamePerformance_DeviceInfo *deviceInfo, GamePerformance_CpuInfo **cpuInfo) | 从设备性能信息GamePerformance_DeviceInfo中获取CPU性能信息GamePerformance_CpuInfo。 |
| [GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) HMS_GamePerformance_CpuInfo_GetCpuLoadLevel (GamePerformance_CpuInfo *cpuInfo, int32_t *cpuLoadLevel) | 从GamePerformance_CpuInfo中获取CPU负载整体等级。 |
| [GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) HMS_GamePerformance_CpuInfo_GetSingleThreadLoadLevel (GamePerformance_CpuInfo *cpuInfo, int32_t *singleThreadLoadLevel) | 从GamePerformance_CpuInfo中获取游戏最重线程的负载整体等级。 |
| GamePerformance_ErrorCode HMS_GamePerformance_DestroyDeviceInfo ([GamePerformance_DeviceInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga530e1cf28aa5c4d0b355dc053ce27e80) **deviceInfo) | 当GamePerformance_DeviceInfo实例不再使用，销毁该实例。 |

#### 类型定义说明

#### [GamePerformance_ConfigInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab05a6dca6b3570c3b45d74a9cb8ffdc9)

```ets
typedef struct [GamePerformance_ConfigInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab05a6dca6b3570c3b45d74a9cb8ffdc9) GamePerformance_ConfigInfo
```

**描述**

定义游戏配置信息。

**起始版本：**5.0.2(14)

#### GamePerformance_CpuInfo

```ets
typedef struct GamePerformance_CpuInfo GamePerformance_CpuInfo
```

**描述**

定义CPU性能信息。

**起始版本：**6.0.2(22)

#### [GamePerformance_CpuLevel](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga11ac456fd1b33d0b1f6220af5e5cd1ce)

```ets
typedef enum GamePerformance_CpuLevel GamePerformance_CpuLevel
```

**描述**

定义CPU等级。

**起始版本：**5.0.2(14)

#### [GamePerformance_DdrLevel](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gaec1b60b592a13ea85774a4d2ec8581bb)

```ets
typedef enum GamePerformance_DdrLevel GamePerformance_DdrLevel
```

**描述**

定义DDR等级。

**起始版本：**5.0.2(14)

#### [GamePerformance_DeviceInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga530e1cf28aa5c4d0b355dc053ce27e80)

```ets
typedef struct GamePerformance_DeviceInfo GamePerformance_DeviceInfo
```

**描述**

定义设备性能信息。

**起始版本：**5.0.2(14)

#### [GamePerformance_DeviceInfoType](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga3ebb81788405856534d8fb3cd6194ca4)

```ets
typedef enum GamePerformance_DeviceInfoType GamePerformance_DeviceInfoType
```

**描述**

定义设备性能信息类型。

**起始版本：**5.0.2(14)

#### [GamePerformance_EngineType](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab7f3d09e6dd4af1692872b6b5815af45)

```ets
typedef enum GamePerformance_EngineType GamePerformance_EngineType
```

**描述**

定义游戏引擎类型。

**起始版本：**5.0.2(14)

#### [GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316)

```ets
typedef enum [GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) GamePerformance_ErrorCode
```

**描述**

定义错误码。

**起始版本：**5.0.2(14)

#### [GamePerformance_GameType](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga9c1b6f00c4769f13c510a7a871c7afd3)

```ets
typedef enum GamePerformance_GameType GamePerformance_GameType
```

**描述**

定义游戏类型。

**起始版本：**5.0.2(14)

#### [GamePerformance_GpuInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gae85f740f82b3ca3f7ec9892d2f81a113)

```ets
typedef struct GamePerformance_GpuInfo GamePerformance_GpuInfo
```

**描述**

定义GPU性能信息。

**起始版本：**5.0.2(14)

#### [GamePerformance_GpuLevel](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga48d14f66a8d484b497157458dd13a473)

```ets
typedef enum GamePerformance_GpuLevel GamePerformance_GpuLevel
```

**描述**

定义GPU等级。

**起始版本：**5.0.2(14)

#### [GamePerformance_InitParameters](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga9ba0e813bb05d37656f9973a35fa0411)

```ets
typedef struct GamePerformance_InitParameters GamePerformance_InitParameters
```

**描述**

定义初始化参数。

**起始版本：**5.0.2(14)

#### [GamePerformance_NetInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gaba275a8588101424676258ffa7217097)

```ets
typedef struct GamePerformance_NetInfo GamePerformance_NetInfo
```

**描述**

定义游戏网络信息。

**起始版本：**5.0.2(14)

#### [GamePerformance_NetLoad](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga517e25164876d3727c407c887943aee2)

```ets
typedef enum GamePerformance_NetLoad GamePerformance_NetLoad
```

**描述**

定义网络负载等级。

**起始版本：**5.0.2(14)

#### [GamePerformance_PackageInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab57ecb4bce0af8b741ef4aa069df2d87)

```ets
typedef struct GamePerformance_PackageInfo GamePerformance_PackageInfo
```

**描述**

定义包信息。

**起始版本：**5.0.2(14)

#### [GamePerformance_PictureQualityLevel](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64fd3d566be9f8240d0f474d52c292dd)

```ets
typedef enum GamePerformance_PictureQualityLevel GamePerformance_PictureQualityLevel
```

**描述**

定义画质等级。

**起始版本：**5.0.2(14)

#### [GamePerformance_PlayerInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga804b472fc080d73a2ce23da927ffd842)

```ets
typedef struct GamePerformance_PlayerInfo GamePerformance_PlayerInfo
```

**描述**

定义游戏玩家信息。

**起始版本：**5.0.2(14)

#### [GamePerformance_SceneImportanceLevel](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gaf6bbf14a7010d4e99e6c758a718a08a6)

```ets
typedef enum GamePerformance_SceneImportanceLevel GamePerformance_SceneImportanceLevel
```

**描述**

定义场景重要程度。

**起始版本：**5.0.2(14)

#### [GamePerformance_SceneInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7)

```ets
typedef struct GamePerformance_SceneInfo GamePerformance_SceneInfo
```

**描述**

定义游戏场景信息。

**起始版本：**5.0.2(14)

#### [GamePerformance_ThermalInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga6767ea8a1d76ed32db95dc0d3a265a8a)

```ets
typedef struct GamePerformance_ThermalInfo GamePerformance_ThermalInfo
```

**描述**

定义温度信息。

**起始版本：**5.0.2(14)

#### [GamePerformance_ThermalInfoQueryParameters](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga0e825c8963101d40a987d4057033c788)

```ets
typedef struct GamePerformance_ThermalInfoQueryParameters GamePerformance_ThermalInfoQueryParameters
```

**描述**

定义温度信息的查询参数。

**起始版本：**5.0.2(14)

#### [GamePerformance_ThermalLevelChangedCallback](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga94e7e85a3f0ad0b495b2c525a15ebc8e)

```ets
typedef void(*GamePerformance_ThermalLevelChangedCallback) (GamePerformance_DeviceInfo *deviceInfo, void *userData)
```

**描述**

[HMS_GamePerformance_RegisterThermalLevelChangedCallback](#ZH-CN_TOPIC_0000002553202309__hms_gameperformance_registerthermallevelchangedcallback)中使用的回调函数。当温度等级改变并且温度等级小于3时，该函数将被调用一次。当温度等级大于或等于3级时，该函数将每10秒调用一次。

**起始版本：**5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| deviceInfo | 设备详细信息[GamePerformance_DeviceInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga530e1cf28aa5c4d0b355dc053ce27e80)。 |
| userData | 用户指定的数据。用户自定义传参。 |

#### 枚举类型说明

#### [GamePerformance_CpuLevel](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga11ac456fd1b33d0b1f6220af5e5cd1ce)

```ets
enum GamePerformance_CpuLevel
```

**描述**

定义CPU等级。

**起始版本：**5.0.2(14)

| 枚举值 | 描述 |
| --- | --- |
| GAME_PERFORMANCE_CPU_LEVEL_LOW | 低。 |
| GAME_PERFORMANCE_CPU_LEVEL_MIDDLE | 中。 |
| GAME_PERFORMANCE_CPU_LEVEL_HIGH | 高。 |

#### [GamePerformance_DdrLevel](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gaec1b60b592a13ea85774a4d2ec8581bb)

```ets
enum GamePerformance_DdrLevel
```

**描述**

定义DDR等级。

**起始版本：**5.0.2(14)

| 枚举值 | 描述 |
| --- | --- |
| GAME_PERFORMANCE_DDR_LEVEL_LOW | 低。 |
| GAME_PERFORMANCE_DDR_LEVEL_MIDDLE | 中。 |
| GAME_PERFORMANCE_DDR_LEVEL_HIGH | 高。 |

#### [GamePerformance_DeviceInfoType](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga3ebb81788405856534d8fb3cd6194ca4)

```ets
enum GamePerformance_DeviceInfoType
```

**描述**

定义回调返回的设备性能信息类型。

**起始版本：**5.0.2(14)

| 枚举值 | 描述 |
| --- | --- |
| GAME_PERFORMANCE_DEVICEINFO_TYPE_THERMAL | 温度信息。 |
| GAME_PERFORMANCE_DEVICEINFO_TYPE_GPU | GPU性能信息。 |
| GAME_PERFORMANCE_DEVICEINFO_TYPE_CPU | CPU性能信息。 起始版本： 6.0.2(22) |

#### [GamePerformance_EngineType](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab7f3d09e6dd4af1692872b6b5815af45)

```ets
enum GamePerformance_EngineType
```

**描述**

定义游戏引擎类型。

**起始版本：**5.0.2(14)

| 枚举值 | 描述 |
| --- | --- |
| GAME_PERFORMANCE_ENGINE_TYPE_UNITY | UNITY。 |
| GAME_PERFORMANCE_ENGINE_TYPE_UNREAL | UNREAL。 |
| GAME_PERFORMANCE_ENGINE_TYPE_MESSIAH | MESSIAH。 |
| GAME_PERFORMANCE_ENGINE_TYPE_COCOS | COCOS。 |
| GAME_PERFORMANCE_ENGINE_TYPE_OTHERS | 其他引擎类型。 |

#### [GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316)

```ets
enum [GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316)
```

**描述**

定义错误码。

**起始版本：**5.0.2(14)

| 枚举值 | 描述 |
| --- | --- |
| GAME_PERFORMANCE_SUCCESS | 成功。 |
| GAME_PERFORMANCE_PARAM_INVALID | 无效参数。 |
| GAME_PERFORMANCE_INTERNAL_ERROR | 系统内部错误。 |
| GAME_PERFORMANCE_AUTH_FAILED | 鉴权失败。 |
| GAME_PERFORMANCE_INVALID_REQUEST | 非法请求。 |
| GAME_PERFORMANCE_PARAM_ERROR | 参数错误。 起始版本：6.0.2(22) |

#### [GamePerformance_GameType](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga9c1b6f00c4769f13c510a7a871c7afd3)

```ets
enum GamePerformance_GameType
```

**描述**

定义游戏类型。

**起始版本：**5.0.2(14)

| 枚举值 | 描述 |
| --- | --- |
| GAME_PERFORMANCE_GAME_TYPE_MOBA | 多人在线战术竞技。 |
| GAME_PERFORMANCE_GAME_TYPE_RPG | 角色扮演。 |
| GAME_PERFORMANCE_GAME_TYPE_FPS | 第一人称射击类。 |
| GAME_PERFORMANCE_GAME_TYPE_FTG | 格斗游戏。 |
| GAME_PERFORMANCE_GAME_TYPE_RAC | 竞速游戏。 |
| GAME_PERFORMANCE_GAME_TYPE_OTHERS | 其他游戏类型。 |

#### [GamePerformance_GpuLevel](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga48d14f66a8d484b497157458dd13a473)

```ets
enum GamePerformance_GpuLevel
```

**描述**

定义GPU等级。

**起始版本：**5.0.2(14)

| 枚举值 | 描述 |
| --- | --- |
| GAME_PERFORMANCE_GPU_LEVEL_LOW | 低。 |
| GAME_PERFORMANCE_GPU_LEVEL_MIDDLE | 中。 |
| GAME_PERFORMANCE_GPU_LEVEL_HIGH | 高。 |

#### [GamePerformance_NetLoad](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga517e25164876d3727c407c887943aee2)

```ets
enum GamePerformance_NetLoad
```

**描述**

定义网络负载等级。

**起始版本：**5.0.2(14)

| 枚举值 | 描述 |
| --- | --- |
| GAME_PERFORMANCE_NET_LOAD_LIGHT | 轻度负载。 |
| GAME_PERFORMANCE_NET_LOAD_MODERATE | 中度负载。 |
| GAME_PERFORMANCE_NET_LOAD_HEAVY | 重度负载。 |

#### [GamePerformance_PictureQualityLevel](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64fd3d566be9f8240d0f474d52c292dd)

```ets
enum GamePerformance_PictureQualityLevel
```

**描述**

定义画质等级。

**起始版本：**5.0.2(14)

| 枚举值 | 描述 |
| --- | --- |
| GAME_PERFORMANCE_PQL_SMOOTH | 流畅。 |
| GAME_PERFORMANCE_PQL_BALANCED | 均衡。 |
| GAME_PERFORMANCE_PQL_HD | 高清。 |
| GAME_PERFORMANCE_PQL_HDR | HDR高清。 |
| GAME_PERFORMANCE_PQL_UHD | 超高清。 |

#### [GamePerformance_SceneImportanceLevel](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gaf6bbf14a7010d4e99e6c758a718a08a6)

```ets
enum GamePerformance_SceneImportanceLevel
```

**描述**

定义游戏场景重要程度，5个等级，重要程度从1到5递增。

**起始版本：**5.0.2(14)

| 枚举值 | 描述 |
| --- | --- |
| GAME_PERFORMANCE_SIL_LEVEL1 | 等级1。 |
| GAME_PERFORMANCE_SIL_LEVEL2 | 等级2。 |
| GAME_PERFORMANCE_SIL_LEVEL3 | 等级3。 |
| GAME_PERFORMANCE_SIL_LEVEL4 | 等级4。 |
| GAME_PERFORMANCE_SIL_LEVEL5 | 等级5。 |

#### 函数说明

#### [HMS_GamePerformance_ConfigInfo_SetAntiAliasingEnabled](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga5657a6e00ba9e08803a201a8d0c1cecd)()

```ets
[GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) HMS_GamePerformance_ConfigInfo_SetAntiAliasingEnabled (GamePerformance_ConfigInfo *configInfo, const bool antiAliasingEnabled)
```

**描述**

为[GamePerformance_ConfigInfo](#ZH-CN_TOPIC_0000002553202309__gameperformance_configinfo)实例设置是否开启抗锯齿。

**起始版本：**5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| configInfo | 指针指向[GamePerformance_ConfigInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab05a6dca6b3570c3b45d74a9cb8ffdc9)实例。该值不可以为空，否则将返回错误码401。 |
| antiAliasingEnabled | 是否开启抗锯齿。 - true：开启 - false：不开启 默认为false。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |

#### [HMS_GamePerformance_ConfigInfo_SetCurrentFrameRate](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga89845a005ea8f0a5069ef2563f55936e)()

```ets
GamePerformance_ErrorCode HMS_GamePerformance_ConfigInfo_SetCurrentFrameRate (GamePerformance_ConfigInfo *configInfo, const int64_t currentFrameRate)
```

**描述**

为[GamePerformance_ConfigInfo](#ZH-CN_TOPIC_0000002553202309__gameperformance_configinfo)实例设置当前帧率。

**起始版本：**5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| configInfo | 指针指向[GamePerformance_ConfigInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab05a6dca6b3570c3b45d74a9cb8ffdc9)实例。该值不可以为空，否则将返回错误码401。 |
| currentFrameRate | 当前帧率。取值范围为[1, 144]。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |

#### [HMS_GamePerformance_ConfigInfo_SetCurrentPictureQualityLevel](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gad44e9925a145ab621f4d8ff348de4034)()

```ets
[GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) HMS_GamePerformance_ConfigInfo_SetCurrentPictureQualityLevel (GamePerformance_ConfigInfo *configInfo, const GamePerformance_PictureQualityLevel currentPictureQualityLevel)
```

**描述**

为[GamePerformance_ConfigInfo](#ZH-CN_TOPIC_0000002553202309__gameperformance_configinfo)实例设置当前画质等级。

**起始版本：**5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| configInfo | 指针指向[GamePerformance_ConfigInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab05a6dca6b3570c3b45d74a9cb8ffdc9)实例。该值不可以为空，否则将返回错误码401。 |
| currentPictureQualityLevel | 当前画质等级[GamePerformance_PictureQualityLevel](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64fd3d566be9f8240d0f474d52c292dd)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |

#### [HMS_GamePerformance_ConfigInfo_SetCurrentResolution](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga9bee7c2052d81a0dd6c6f93ce57ddc1f)()

```ets
GamePerformance_ErrorCode HMS_GamePerformance_ConfigInfo_SetCurrentResolution (GamePerformance_ConfigInfo *configInfo, const char *currentResolution)
```

**描述**

为[GamePerformance_ConfigInfo](#ZH-CN_TOPIC_0000002553202309__gameperformance_configinfo)实例设置当前分辨率。

**起始版本：**5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| configInfo | 指针指向[GamePerformance_ConfigInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab05a6dca6b3570c3b45d74a9cb8ffdc9)实例。该值不可以为空，否则将返回错误码401。 |
| currentResolution | 当前分辨率。格式AxB（如1260x1980），字符长度范围：[1, 32]。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |

#### [HMS_GamePerformance_ConfigInfo_SetHdModeEnabled](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga5ef09e013a67def087e5f6b5442ff0b0)()

```ets
[GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) HMS_GamePerformance_ConfigInfo_SetHdModeEnabled (GamePerformance_ConfigInfo *configInfo, const bool hdModeEnabled)
```

**描述**

为[GamePerformance_ConfigInfo](#ZH-CN_TOPIC_0000002553202309__gameperformance_configinfo)实例设置开启高清模式。

**起始版本：**5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| configInfo | 指针指向[GamePerformance_ConfigInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab05a6dca6b3570c3b45d74a9cb8ffdc9)实例。该值不可以为空，否则将返回错误码401。 |
| hdModeEnabled | 是否开启高清模式。 - true：开启 - false：不开启 默认为false。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |

#### [HMS_GamePerformance_ConfigInfo_SetMaxFrameRate](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga6665850e826d430bba7525351ef2df70)()

```ets
GamePerformance_ErrorCode HMS_GamePerformance_ConfigInfo_SetMaxFrameRate (GamePerformance_ConfigInfo *configInfo, const int64_t maxFrameRate)
```

**描述**

为[GamePerformance_ConfigInfo](#ZH-CN_TOPIC_0000002553202309__gameperformance_configinfo)实例设置最大帧率。

**起始版本：**5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| configInfo | 指针指向[GamePerformance_ConfigInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab05a6dca6b3570c3b45d74a9cb8ffdc9)实例。该值不可以为空，否则将返回错误码401。 |
| maxFrameRate | 最大帧率。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |

#### [HMS_GamePerformance_ConfigInfo_SetMaxPictureQualityLevel](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga5f85d32e8f74f4ab008abd49f1109c46)()

```ets
[GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) HMS_GamePerformance_ConfigInfo_SetMaxPictureQualityLevel (GamePerformance_ConfigInfo *configInfo, const GamePerformance_PictureQualityLevel maxPictureQualityLevel)
```

**描述**

为[GamePerformance_ConfigInfo](#ZH-CN_TOPIC_0000002553202309__gameperformance_configinfo)实例设置最大画质等级。

**起始版本：**5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| configInfo | 指针指向[GamePerformance_ConfigInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab05a6dca6b3570c3b45d74a9cb8ffdc9)实例。该值不可以为空，否则将返回错误码401。 |
| maxPictureQualityLevel | 支持的画质最高等级[GamePerformance_PictureQualityLevel](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64fd3d566be9f8240d0f474d52c292dd)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |

#### [HMS_GamePerformance_ConfigInfo_SetMaxResolution](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gad34b019dfa3a973512c7157dcba92ad1)()

```ets
GamePerformance_ErrorCode HMS_GamePerformance_ConfigInfo_SetMaxResolution (GamePerformance_ConfigInfo *configInfo, const char *maxResolution)
```

**描述**

为[GamePerformance_ConfigInfo](#ZH-CN_TOPIC_0000002553202309__gameperformance_configinfo)实例设置最大分辨率。

**起始版本：**5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| configInfo | 指针指向[GamePerformance_ConfigInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab05a6dca6b3570c3b45d74a9cb8ffdc9)实例。该值不可以为空，否则将返回错误码401。 |
| maxResolution | 最大分辨率。格式AxB（如1260x1980），字符长度范围：[1, 32]。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |

#### [HMS_GamePerformance_ConfigInfo_SetMultithreadingEnabled](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab69ed9d7e95fe067d618514a6472c2b3)()

```ets
[GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) HMS_GamePerformance_ConfigInfo_SetMultithreadingEnabled (GamePerformance_ConfigInfo *configInfo, const bool multithreadingEnabled)
```

**描述**

为[GamePerformance_ConfigInfo](#ZH-CN_TOPIC_0000002553202309__gameperformance_configinfo)实例设置开启多线程。

**起始版本：**5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| configInfo | 指针指向[GamePerformance_ConfigInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab05a6dca6b3570c3b45d74a9cb8ffdc9)实例。该值不可以为空，否则将返回错误码401。 |
| multithreadingEnabled | 是否开启多线程。 - true：开启 - false：不开启 默认为false。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |

#### [HMS_GamePerformance_ConfigInfo_SetParticleEnabled](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga808ed7b13bc8ed4fd97267a65c8f4469)()

```ets
GamePerformance_ErrorCode HMS_GamePerformance_ConfigInfo_SetParticleEnabled (GamePerformance_ConfigInfo *configInfo, const bool particleEnabled)
```

**描述**

为[GamePerformance_ConfigInfo](#ZH-CN_TOPIC_0000002553202309__gameperformance_configinfo)实例设置粒子效果。

**起始版本：**5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| configInfo | 指针指向[GamePerformance_ConfigInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab05a6dca6b3570c3b45d74a9cb8ffdc9)实例。该值不可以为空，否则将返回错误码401。 |
| particleEnabled | 是否开启粒子效果。 - true：开启 - false：不开启 默认为false。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |

#### [HMS_GamePerformance_ConfigInfo_SetShadowEnabled](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga1beebb2eabcea33e37de8015ac29ef9c)()

```ets
[GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) HMS_GamePerformance_ConfigInfo_SetShadowEnabled (GamePerformance_ConfigInfo *configInfo, const bool shadowEnabled)
```

**描述**

为[GamePerformance_ConfigInfo](#ZH-CN_TOPIC_0000002553202309__gameperformance_configinfo)实例设置是否开启阴影。

**起始版本：**5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| configInfo | 指针指向[GamePerformance_ConfigInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab05a6dca6b3570c3b45d74a9cb8ffdc9)实例。该值不可以为空，否则将返回错误码401。 |
| shadowEnabled | 是否开启阴影。 - true：开启 - false：不开启 默认为false。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |

#### HMS_GamePerformance_CpuInfo_GetCpuLoadLevel()

```ets
GamePerformance_ErrorCode HMS_GamePerformance_CpuInfo_GetCpuLoadLevel (GamePerformance_CpuInfo *cpuInfo, int32_t *cpuLoadLevel)
```

**描述**

从[GamePerformance_CpuInfo](#ZH-CN_TOPIC_0000002553202309__gameperformance_cpuinfo)中获取CPU负载整体等级。

**起始版本：**6.0.2(22)

**参数:**

| 名称 | 描述 |
| --- | --- |
| cpuInfo | 指向GamePerformance_CpuInfo实例的指针。该值不可以为空，否则将返回错误码1010300004。 |
| cpuLoadLevel | CPU负载整体等级，取值范围为[1, 10]区间的整数。值越大表示负载越高。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_ERROR：参数错误。参数不能为空指针。 |

#### HMS_GamePerformance_CpuInfo_GetSingleThreadLoadLevel()

```ets
[GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) HMS_GamePerformance_CpuInfo_GetSingleThreadLoadLevel (GamePerformance_CpuInfo *cpuInfo, int32_t *singleThreadLoadLevel)
```

**描述**

从[GamePerformance_CpuInfo](#ZH-CN_TOPIC_0000002553202309__gameperformance_cpuinfo)中获取游戏最重线程的负载整体等级。

**起始版本：**6.0.2(22)

**参数:**

| 名称 | 描述 |
| --- | --- |
| cpuInfo | 指针指向GamePerformance_CpuInfo实例。该值不可以为空，否则将返回错误码1010300004。 |
| singleThreadLoadLevel | 游戏最重线程的负载整体等级，取值范围为[1, 10]区间的整数。值越大表示负载越高。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_ERROR：参数错误。参数不能为空指针。 |

#### [HMS_GamePerformance_CreateConfigInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga2124abdf7dfed3b2c37242228a442128)()

```ets
GamePerformance_ErrorCode HMS_GamePerformance_CreateConfigInfo (GamePerformance_ConfigInfo **configInfo)
```

**描述**

创建[GamePerformance_ConfigInfo](#ZH-CN_TOPIC_0000002553202309__gameperformance_configinfo)实例，该实例在[HMS_GamePerformance_UpdateConfigInfo](#ZH-CN_TOPIC_0000002553202309__hms_gameperformance_updateconfiginfo)方法中使用。

**起始版本：**5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| configInfo | 二级指针指向[GamePerformance_ConfigInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab05a6dca6b3570c3b45d74a9cb8ffdc9)实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) | GAME_PERFORMANCE_SUCCESS：成功。 |

#### [HMS_GamePerformance_CreateInitParameters](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga82a96cb32e0980c6650b262b268158a2)()

```ets
[GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) HMS_GamePerformance_CreateInitParameters (GamePerformance_InitParameters **initParameters)
```

**描述**

创建[GamePerformance_InitParameters](#ZH-CN_TOPIC_0000002553202309__gameperformance_initparameters)实例，该实例在[HMS_GamePerformance_Init](#ZH-CN_TOPIC_0000002553202309__hms_gameperformance_init)方法中使用。

**起始版本：**5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| initParameters | 二级指针指向[GamePerformance_InitParameters](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga9ba0e813bb05d37656f9973a35fa0411)初始化参数实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) | GAME_PERFORMANCE_SUCCESS：成功。 |

#### [HMS_GamePerformance_CreateNetInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga7c2084205b1c6402f6c7697aa93ea08e)()

```ets
GamePerformance_ErrorCode HMS_GamePerformance_CreateNetInfo (GamePerformance_NetInfo **netInfo)
```

**描述**

创建[GamePerformance_NetInfo](#ZH-CN_TOPIC_0000002553202309__gameperformance_netinfo)实例，该实例在[HMS_GamePerformance_UpdateNetInfo](#ZH-CN_TOPIC_0000002553202309__hms_gameperformance_updatenetinfo)方法中使用。

**起始版本：**5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| netInfo | 二级指针指向[GamePerformance_NetInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gaba275a8588101424676258ffa7217097)实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) | GAME_PERFORMANCE_SUCCESS：成功。 |

#### [HMS_GamePerformance_CreatePackageInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga6b54d67769794ce6833cbecf7a0fb9ab)()

```ets
[GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) HMS_GamePerformance_CreatePackageInfo ([GamePerformance_PackageInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab57ecb4bce0af8b741ef4aa069df2d87) **packageInfo)
```

**描述**

创建[GamePerformance_PackageInfo](#ZH-CN_TOPIC_0000002553202309__gameperformance_packageinfo)实例，该实例在[HMS_GamePerformance_UpdatePackageInfo](#ZH-CN_TOPIC_0000002553202309__hms_gameperformance_updatepackageinfo)方法中使用。

**起始版本：**5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| packageInfo | 二级指针指向[GamePerformance_PackageInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab57ecb4bce0af8b741ef4aa069df2d87)实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) | GAME_PERFORMANCE_SUCCESS：成功。 |

#### [HMS_GamePerformance_CreatePlayerInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga97925740bdc7df3aefbd482304294208)()

```ets
GamePerformance_ErrorCode HMS_GamePerformance_CreatePlayerInfo (GamePerformance_PlayerInfo **playerInfo)
```

**描述**

创建[GamePerformance_PlayerInfo](#ZH-CN_TOPIC_0000002553202309__gameperformance_playerinfo)实例，该实例在[HMS_GamePerformance_UpdatePlayerInfo](#ZH-CN_TOPIC_0000002553202309__hms_gameperformance_updateplayerinfo)方法中使用。

**起始版本：**5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| playerInfo | 二级指针指向[GamePerformance_PlayerInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga804b472fc080d73a2ce23da927ffd842)实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) | GAME_PERFORMANCE_SUCCESS：成功。 |

#### [HMS_GamePerformance_CreateSceneInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga20ba3d28237372a1f44652f50d0850c4)()

```ets
[GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) HMS_GamePerformance_CreateSceneInfo (GamePerformance_SceneInfo **sceneInfo)
```

**描述**

创建[GamePerformance_SceneInfo](#ZH-CN_TOPIC_0000002553202309__gameperformance_sceneinfo)实例，该实例在[HMS_GamePerformance_UpdateSceneInfo](#ZH-CN_TOPIC_0000002553202309__hms_gameperformance_updatesceneinfo)方法中使用。

**起始版本：**5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| sceneInfo | 二级指针指向[GamePerformance_SceneInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7)实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) | GAME_PERFORMANCE_SUCCESS：成功。 |

#### [HMS_GamePerformance_CreateThermalInfoQueryParameters](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gad3e60ec2d47a5068206bc3e1f217acc2)()

```ets
GamePerformance_ErrorCode HMS_GamePerformance_CreateThermalInfoQueryParameters (GamePerformance_ThermalInfoQueryParameters **parameters)
```

**描述**

创建[GamePerformance_ThermalInfoQueryParameters](#ZH-CN_TOPIC_0000002553202309__gameperformance_thermalinfoqueryparameters)实例，该实例在[HMS_GamePerformance_QueryThermalInfo](#ZH-CN_TOPIC_0000002553202309__hms_gameperformance_querythermalinfo)方法中使用。

**起始版本：**5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| parameters | 二级指针指向[GamePerformance_ThermalInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga6767ea8a1d76ed32db95dc0d3a265a8a)QueryParameters实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) | GAME_PERFORMANCE_SUCCESS：成功。 |

#### [HMS_GamePerformance_DestroyConfigInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga8328d927012e4b868175ad3c192a947b)()

```ets
[GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) HMS_GamePerformance_DestroyConfigInfo (GamePerformance_ConfigInfo **configInfo)
```

**描述**

当[GamePerformance_ConfigInfo](#ZH-CN_TOPIC_0000002553202309__gameperformance_configinfo)实例不再使用，销毁该实例。

**起始版本：**5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| configInfo | 二级指针指向[GamePerformance_ConfigInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab05a6dca6b3570c3b45d74a9cb8ffdc9)实例。该值不可以为空，否则将返回错误码401。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |

#### HMS_GamePerformance_DestroyCpuInfo()

```ets
GamePerformance_ErrorCode HMS_GamePerformance_DestroyCpuInfo (GamePerformance_CpuInfo **cpuInfo)
```

**描述**

当[GamePerformance_CpuInfo](#ZH-CN_TOPIC_0000002553202309__gameperformance_cpuinfo)实例不再使用，销毁该实例。

**起始版本：**6.0.2(22)

**参数:**

| 名称 | 描述 |
| --- | --- |
| cpuInfo | 二级指针指向GamePerformance_CpuInfo实例。该值不可以为空，否则将返回错误码1010300004。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_ERROR：参数错误。参数不能为空指针。 |

#### [HMS_GamePerformance_DestroyDeviceInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gaf8031fd101ee970aa0339aed14d4507e)()

```ets
[GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) HMS_GamePerformance_DestroyDeviceInfo (GamePerformance_DeviceInfo **deviceInfo)
```

**描述**

当[GamePerformance_DeviceInfo](#ZH-CN_TOPIC_0000002553202309__gameperformance_deviceinfo)实例不再使用，销毁该实例。

**起始版本：**5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| deviceInfo | 二级指针指向[GamePerformance_DeviceInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga530e1cf28aa5c4d0b355dc053ce27e80)实例。该值不可以为空，否则将返回错误码401。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |

#### [HMS_GamePerformance_DestroyGpuInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga249433eea6a463cb2401e7bbbbcd19dd)()

```ets
GamePerformance_ErrorCode HMS_GamePerformance_DestroyGpuInfo (GamePerformance_GpuInfo **gpuInfo)
```

**描述**

当[GamePerformance_GpuInfo](#ZH-CN_TOPIC_0000002553202309__gameperformance_gpuinfo)实例不再使用，销毁该实例。

**起始版本：**5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| gpuInfo | 二级指针指向[GamePerformance_GpuInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gae85f740f82b3ca3f7ec9892d2f81a113)实例。该值不可以为空，否则将返回错误码401。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |

#### [HMS_GamePerformance_DestroyInitParameters](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gaef8a6ecaefc0f7ca4b8e2c88a84f5db0)()

```ets
[GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) HMS_GamePerformance_DestroyInitParameters (GamePerformance_InitParameters **initParameters)
```

**描述**

当[GamePerformance_InitParameters](#ZH-CN_TOPIC_0000002553202309__gameperformance_initparameters)实例不再使用，销毁该实例。

**起始版本：**5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| initParameters | 二级指针指向[GamePerformance_InitParameters](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga9ba0e813bb05d37656f9973a35fa0411)实例。该值不可以为空，否则将返回错误码401。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |

#### [HMS_GamePerformance_DestroyNetInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga7e97470d2e305c3777438ba7cc524cac)()

```ets
GamePerformance_ErrorCode HMS_GamePerformance_DestroyNetInfo (GamePerformance_NetInfo **netInfo)
```

**描述**

当[GamePerformance_NetInfo](#ZH-CN_TOPIC_0000002553202309__gameperformance_netinfo)实例不再使用，销毁该实例。

**起始版本：**5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| netInfo | 二级指针指向[GamePerformance_NetInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gaba275a8588101424676258ffa7217097)实例。该值不可以为空，否则将返回错误码401。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |

#### [HMS_GamePerformance_DestroyPackageInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga2019dcc34f428ae80868c0af612237c3)()

```ets
[GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) HMS_GamePerformance_DestroyPackageInfo (GamePerformance_PackageInfo **packageInfo)
```

**描述**

当[GamePerformance_PackageInfo](#ZH-CN_TOPIC_0000002553202309__gameperformance_packageinfo)实例不再使用，销毁该实例。

**起始版本：**5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| packageInfo | 二级指针指向[GamePerformance_PackageInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab57ecb4bce0af8b741ef4aa069df2d87)实例。该值不可以为空，否则将返回错误码401。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |

#### [HMS_GamePerformance_DestroyPlayerInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga42254ab6d5c9a8ec61f512d1e2903256)()

```ets
GamePerformance_ErrorCode HMS_GamePerformance_DestroyPlayerInfo (GamePerformance_PlayerInfo **playerInfo)
```

**描述**

当[GamePerformance_PlayerInfo](#ZH-CN_TOPIC_0000002553202309__gameperformance_playerinfo)实例不再使用，销毁该实例。

**起始版本：**5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| playerInfo | 二级指针指向[GamePerformance_PlayerInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga804b472fc080d73a2ce23da927ffd842)实例。该值不可以为空，否则将返回错误码401。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |

#### [HMS_GamePerformance_DestroySceneInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gadc5f2c4b6b7258830736fb194d06bdd8)()

```ets
[GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) HMS_GamePerformance_DestroySceneInfo (GamePerformance_SceneInfo **sceneInfo)
```

**描述**

当[GamePerformance_SceneInfo](#ZH-CN_TOPIC_0000002553202309__gameperformance_sceneinfo)实例不再使用，销毁该实例。

**起始版本：**5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| sceneInfo | 二级指针指向[GamePerformance_SceneInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7)实例。该值不可以为空，否则将返回错误码401。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |

#### [HMS_GamePerformance_DestroyThermalInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gacc640a4e15fe9cab1f8bccb652d77e59)()

```ets
GamePerformance_ErrorCode HMS_GamePerformance_DestroyThermalInfo (GamePerformance_ThermalInfo **thermalInfo)
```

**描述**

当[GamePerformance_ThermalInfo](#ZH-CN_TOPIC_0000002553202309__gameperformance_thermalinfo)实例不再使用，销毁该实例。

**起始版本：**5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| thermalInfo | 二级指针指向[GamePerformance_ThermalInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga6767ea8a1d76ed32db95dc0d3a265a8a)实例。该值不可以为空，否则将返回错误码401。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |

#### [HMS_GamePerformance_DestroyThermalInfoQueryParameters](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga6b9314f647ed520b11b9dfa4fbc40351)()

```ets
[GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) HMS_GamePerformance_DestroyThermalInfoQueryParameters (GamePerformance_ThermalInfoQueryParameters **parameters)
```

**描述**

当[GamePerformance_ThermalInfoQueryParameters](#ZH-CN_TOPIC_0000002553202309__gameperformance_thermalinfoqueryparameters)实例不再使用，销毁该实例。

**起始版本：**5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| parameters | 二级指针指向[GamePerformance_ThermalInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga6767ea8a1d76ed32db95dc0d3a265a8a)QueryParameters实例。该值不可以为空，否则将返回错误码401。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |

#### HMS_[GamePerformance_DeviceInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga530e1cf28aa5c4d0b355dc053ce27e80)_GetCpuInfo()

```ets
GamePerformance_ErrorCode HMS_GamePerformance_DeviceInfo_GetCpuInfo (GamePerformance_DeviceInfo *deviceInfo, GamePerformance_CpuInfo **cpuInfo)
```

**描述**

从设备性能信息[GamePerformance_DeviceInfo](#ZH-CN_TOPIC_0000002553202309__gameperformance_deviceinfo)中获取CPU性能信息[GamePerformance_CpuInfo](#ZH-CN_TOPIC_0000002553202309__gameperformance_cpuinfo)。当[GamePerformance_CpuInfo](#ZH-CN_TOPIC_0000002553202309__gameperformance_cpuinfo)实例不再使用，必须调用[HMS_GamePerformance_DestroyCpuInfo](#ZH-CN_TOPIC_0000002553202309__hms_gameperformance_destroycpuinfo)销毁该实例。

**起始版本：**6.0.2(22)

**参数:**

| 名称 | 描述 |
| --- | --- |
| deviceInfo | 指针指向[GamePerformance_DeviceInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga530e1cf28aa5c4d0b355dc053ce27e80)实例。该值不可以为空，否则将返回错误码1010300004。 |
| cpuInfo | 二级指针指向GamePerformance_CpuInfo实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_ERROR：参数错误。参数不能为空指针。 |

#### [HMS_GamePerformance_DeviceInfo_GetGpuInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga028805183830f3638fb9b122a934d30a)()

```ets
[GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) HMS_GamePerformance_DeviceInfo_GetGpuInfo (GamePerformance_DeviceInfo *deviceInfo, GamePerformance_GpuInfo **gpuInfo)
```

**描述**

从设备性能信息[GamePerformance_DeviceInfo](#ZH-CN_TOPIC_0000002553202309__gameperformance_deviceinfo)中获取GPU性能信息[GamePerformance_GpuInfo](#ZH-CN_TOPIC_0000002553202309__gameperformance_gpuinfo)。当[GamePerformance_GpuInfo](#ZH-CN_TOPIC_0000002553202309__gameperformance_gpuinfo)实例不再使用，必须调用[HMS_GamePerformance_DestroyGpuInfo](#ZH-CN_TOPIC_0000002553202309__hms_gameperformance_destroygpuinfo)销毁该实例。

**起始版本：**5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| deviceInfo | 指针指向[GamePerformance_DeviceInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga530e1cf28aa5c4d0b355dc053ce27e80)实例。该值不可以为空，否则将返回错误码401。 |
| gpuInfo | 二级指针指向[GamePerformance_GpuInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gae85f740f82b3ca3f7ec9892d2f81a113)实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |

#### [HMS_GamePerformance_DeviceInfo_GetThermalInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga233f517841cc5ab435a1e4fa8cd1d2de)()

```ets
GamePerformance_ErrorCode HMS_GamePerformance_DeviceInfo_GetThermalInfo (GamePerformance_DeviceInfo *deviceInfo, GamePerformance_ThermalInfo **thermalInfo)
```

**描述**

从设备性能信息[GamePerformance_DeviceInfo](#ZH-CN_TOPIC_0000002553202309__gameperformance_deviceinfo)中获取温度信息[GamePerformance_ThermalInfo](#ZH-CN_TOPIC_0000002553202309__gameperformance_thermalinfo)。当[GamePerformance_ThermalInfo](#ZH-CN_TOPIC_0000002553202309__gameperformance_thermalinfo)实例不再使用，必须调用[HMS_GamePerformance_DestroyThermalInfo](#ZH-CN_TOPIC_0000002553202309__hms_gameperformance_destroythermalinfo)销毁该实例。

**起始版本：**5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| deviceInfo | 指针指向[GamePerformance_DeviceInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga530e1cf28aa5c4d0b355dc053ce27e80)实例。该值不可以为空，否则将返回错误码401。 |
| thermalInfo | 二级指针指向[GamePerformance_ThermalInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga6767ea8a1d76ed32db95dc0d3a265a8a)实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |

#### [HMS_GamePerformance_GpuInfo_GetBandwidthLoadLevel](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga798a410d53057a8735c342c41066e286)()

```ets
[GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) HMS_[GamePerformance_GpuInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gae85f740f82b3ca3f7ec9892d2f81a113)_GetBandwidthLoadLevel (GamePerformance_GpuInfo *gpuInfo, int32_t *bandwidthLoadLevel)
```

**描述**

从[GamePerformance_GpuInfo](#ZH-CN_TOPIC_0000002553202309__gameperformance_gpuinfo)中获取GPU带宽负载等级。

**起始版本：**5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| gpuInfo | 指针指向[GamePerformance_GpuInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gae85f740f82b3ca3f7ec9892d2f81a113)实例。该值不可以为空，否则将返回错误码401。 |
| bandwidthLoadLevel | GPU带宽负载等级，取值范围为[1, 10]区间的整数。值越大表示负载越高。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |

#### HMS_[GamePerformance_GpuInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gae85f740f82b3ca3f7ec9892d2f81a113)_GetCurrentFrequency()

```ets
GamePerformance_ErrorCode HMS_GamePerformance_GpuInfo_GetCurrentFrequency (GamePerformance_GpuInfo *gpuInfo, int32_t *currentFrequency)
```

**描述**

从[GamePerformance_GpuInfo](#ZH-CN_TOPIC_0000002553202309__gameperformance_gpuinfo)中获取GPU频点信息。

**起始版本：**5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| gpuInfo | 指针指向[GamePerformance_GpuInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gae85f740f82b3ca3f7ec9892d2f81a113)实例。该值不可以为空，否则将返回错误码401。 |
| currentFrequency | GPU频点信息，单位：KHz。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |

#### [HMS_GamePerformance_GpuInfo_GetFragmentLoadLevel](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga9ed72dbe4214471b0c62888e220c535b)()

```ets
[GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) HMS_GamePerformance_GpuInfo_GetFragmentLoadLevel (GamePerformance_GpuInfo *gpuInfo, int32_t *fragmentLoadLevel)
```

**描述**

从[GamePerformance_GpuInfo](#ZH-CN_TOPIC_0000002553202309__gameperformance_gpuinfo)中获取GPU片元处理负载等级。

**起始版本：**5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| gpuInfo | 指针指向[GamePerformance_GpuInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gae85f740f82b3ca3f7ec9892d2f81a113)实例。该值不可以为空，否则将返回错误码401。 |
| fragmentLoadLevel | GPU片元处理负载等级，取值范围为[1, 10]区间的整数。值越大表示负载越高。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |

#### [HMS_GamePerformance_GpuInfo_GetGpuLoadLevel](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga2542ab4c2a7a8ea411f5ca78236f3057)()

```ets
GamePerformance_ErrorCode HMS_GamePerformance_GpuInfo_GetGpuLoadLevel (GamePerformance_GpuInfo *gpuInfo, int32_t *gpuLoadLevel)
```

**描述**

从[GamePerformance_GpuInfo](#ZH-CN_TOPIC_0000002553202309__gameperformance_gpuinfo)中获取GPU负载信息。

**起始版本：**5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| gpuInfo | 指针指向[GamePerformance_GpuInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gae85f740f82b3ca3f7ec9892d2f81a113)实例。该值不可以为空，否则将返回错误码401。 |
| gpuLoadLevel | GPU负载信息，取值范围为[1, 10]区间的整数。值越大表示负载越高。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |

#### [HMS_GamePerformance_GpuInfo_GetTextureLoadLevel](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga0b690f0f661dcc5b552e1c3b0a6c48b0)()

```ets
[GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) HMS_GamePerformance_GpuInfo_GetTextureLoadLevel (GamePerformance_GpuInfo *gpuInfo, int32_t *textureLoadLevel)
```

**描述**

从[GamePerformance_GpuInfo](#ZH-CN_TOPIC_0000002553202309__gameperformance_gpuinfo)中获取GPU纹理处理负载等级。

**起始版本：**5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| gpuInfo | 指针指向[GamePerformance_GpuInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gae85f740f82b3ca3f7ec9892d2f81a113)实例。该值不可以为空，否则将返回错误码401。 |
| textureLoadLevel | GPU纹理处理负载等级，取值范围为[1, 10]区间的整数。值越高表示负载越高。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |

#### [HMS_GamePerformance_GpuInfo_GetVertexLoadLevel](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab2c0f4d08ce347fc2ce57cd4f75a207d)()

```ets
GamePerformance_ErrorCode HMS_GamePerformance_GpuInfo_GetVertexLoadLevel (GamePerformance_GpuInfo *gpuInfo, int32_t *vertexLoadLevel)
```

**描述**

从[GamePerformance_GpuInfo](#ZH-CN_TOPIC_0000002553202309__gameperformance_gpuinfo)中获取GPU顶点处理负载等级。

**起始版本：**5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| gpuInfo | 指针指向[GamePerformance_GpuInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gae85f740f82b3ca3f7ec9892d2f81a113)实例。该值不可以为空，否则将返回错误码401。 |
| vertexLoadLevel | GPU顶点处理负载等级，取值范围为[1, 10]区间的整数。值越大表示负载越高。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |

#### [HMS_GamePerformance_Init](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga1045d9d8f4e7972b44ff95571afca8f9)()

```ets
GamePerformance_ErrorCode HMS_GamePerformance_Init (GamePerformance_InitParameters *initParameters)
```

**描述**

初始化游戏场景感知。

**起始版本：**5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| initParameters | 指针指向[GamePerformance_InitParameters](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga9ba0e813bb05d37656f9973a35fa0411)实例。该值不可以为空，否则将返回错误码401。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 GAME_PERFORMANCE_INTERNAL_ERROR：系统内部错误。 GAME_PERFORMANCE_AUTH_FAILED：认证失败。 |

#### [HMS_GamePerformance_InitParameters_SetAppVersion](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab19d551d38ea087012ba205f975ec5ed)()

```ets
[GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) HMS_GamePerformance_InitParameters_SetAppVersion (GamePerformance_InitParameters *initParameters,const char *appVersion)
```

**描述**

为[GamePerformance_InitParameters](#ZH-CN_TOPIC_0000002553202309__gameperformance_initparameters)实例设置版本号。

**起始版本：**5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| initParameters | 指针指向[GamePerformance_InitParameters](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga9ba0e813bb05d37656f9973a35fa0411)实例。该值不可以为空，否则将返回错误码401。 |
| appVersion | 游戏版本号。字符长度范围：[1, 64]。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |

#### [HMS_GamePerformance_InitParameters_SetBundleName](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga35962b201b42b841202d0986e7e80250)()

```ets
GamePerformance_ErrorCode HMS_GamePerformance_InitParameters_SetBundleName (GamePerformance_InitParameters *initParameters, const char *bundleName)
```

**描述**

为[GamePerformance_InitParameters](#ZH-CN_TOPIC_0000002553202309__gameperformance_initparameters)实例设置包名。

**起始版本：**5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| initParameters | 指针指向[GamePerformance_InitParameters](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga9ba0e813bb05d37656f9973a35fa0411)实例。该值不可以为空，否则将返回错误码401。 |
| bundleName | 游戏包名。字符长度范围：[1, 128]。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |

#### HMS_[GamePerformance_NetInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gaba275a8588101424676258ffa7217097)_SetDownlinkLatency()

```ets
[GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) HMS_GamePerformance_NetInfo_SetDownlinkLatency (GamePerformance_NetInfo *netInfo, const int64_t down)
```

**描述**

为[GamePerformance_NetInfo](#ZH-CN_TOPIC_0000002553202309__gameperformance_netinfo)实例设置下行网络时延。

**起始版本：**5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| netInfo | 指针指向[GamePerformance_NetInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gaba275a8588101424676258ffa7217097)实例。该值不可以为空，否则将返回错误码401。 |
| down | 下行网络时延，单位：毫秒（ms）。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |

#### [HMS_GamePerformance_NetInfo_SetNetLoad](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga74aab7c053e2bf62aacef57ea223aa28)()

```ets
GamePerformance_ErrorCode HMS_GamePerformance_NetInfo_SetNetLoad (GamePerformance_NetInfo *netInfo, const GamePerformance_NetLoad netLoad)
```

**描述**

为[GamePerformance_NetInfo](#ZH-CN_TOPIC_0000002553202309__gameperformance_netinfo)实例设置网络负载。

**起始版本：**5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| netInfo | 指针指向[GamePerformance_NetInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gaba275a8588101424676258ffa7217097)实例。该值不可以为空，否则将返回错误码401。 |
| netLoad | 网络负载[GamePerformance_NetLoad](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga517e25164876d3727c407c887943aee2)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |

#### [HMS_GamePerformance_NetInfo_SetServerLatency](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga5920ded727e6ca21760b82d5586064b9)()

```ets
[GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) HMS_GamePerformance_NetInfo_SetServerLatency (GamePerformance_NetInfo *netInfo, const int64_t server)
```

**描述**

为[GamePerformance_NetInfo](#ZH-CN_TOPIC_0000002553202309__gameperformance_netinfo)实例设置服务器网络时延。

**起始版本：**5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| netInfo | 指针指向[GamePerformance_NetInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gaba275a8588101424676258ffa7217097)实例。该值不可以为空，否则将返回错误码401。 |
| server | 服务器网络时延，单位：毫秒（ms）。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |

#### [HMS_GamePerformance_NetInfo_SetTotalLatency](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gaf2b2757c599992d8eb90767513abef59)()

```ets
GamePerformance_ErrorCode HMS_GamePerformance_NetInfo_SetTotalLatency (GamePerformance_NetInfo *netInfo, const int64_t total)
```

**描述**

为[GamePerformance_NetInfo](#ZH-CN_TOPIC_0000002553202309__gameperformance_netinfo)实例设置总网络时延。

**起始版本：**5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| netInfo | 指针指向[GamePerformance_NetInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gaba275a8588101424676258ffa7217097)实例。该值不可以为空，否则将返回错误码401。 |
| total | 总网络时延，单位：毫秒（ms）。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |

#### HMS_[GamePerformance_NetInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gaba275a8588101424676258ffa7217097)_SetUplinkLatency()

```ets
[GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) HMS_GamePerformance_NetInfo_SetUplinkLatency (GamePerformance_NetInfo *netInfo, const int64_t up)
```

**描述**

为[GamePerformance_NetInfo](#ZH-CN_TOPIC_0000002553202309__gameperformance_netinfo)实例设置上行网络时延。

**起始版本：**5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| netInfo | 指针指向[GamePerformance_NetInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gaba275a8588101424676258ffa7217097)实例。该值不可以为空，否则将返回错误码401。 |
| up | 上行网络时延，单位：毫秒（ms）。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |

#### [HMS_GamePerformance_PackageInfo_SetAppVersion](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga0afa327f6afed7acfc998c3f79bfeb76)()

```ets
GamePerformance_ErrorCode HMS_GamePerformance_PackageInfo_SetAppVersion (GamePerformance_PackageInfo *packageInfo, const char *appVersion)
```

**描述**

为[GamePerformance_PackageInfo](#ZH-CN_TOPIC_0000002553202309__gameperformance_packageinfo)实例设置游戏版本号。

**起始版本：**5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| packageInfo | 指针指向[GamePerformance_PackageInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab57ecb4bce0af8b741ef4aa069df2d87)实例。该值不可以为空，否则将返回错误码401。 |
| appVersion | 游戏版本号。字符长度范围：[1, 64]。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |

#### [HMS_GamePerformance_PackageInfo_SetBundleName](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga623a88c7ea2c5eb022dd8a784e8b6661)()

```ets
[GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) HMS_GamePerformance_PackageInfo_SetBundleName (GamePerformance_PackageInfo *packageInfo, const char *bundleName)
```

**描述**

为[GamePerformance_PackageInfo](#ZH-CN_TOPIC_0000002553202309__gameperformance_packageinfo)实例设置包名。

**起始版本：**5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| packageInfo | 指针指向[GamePerformance_PackageInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab57ecb4bce0af8b741ef4aa069df2d87)实例。该值不可以为空，否则将返回错误码401。 |
| bundleName | 游戏包名。字符长度范围：[1, 128]。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |

#### [HMS_GamePerformance_PackageInfo_SetEngineType](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga1436072d310ec40ddc2a85d6bafd0ee2)()

```ets
GamePerformance_ErrorCode HMS_GamePerformance_PackageInfo_SetEngineType (GamePerformance_PackageInfo *packageInfo, const GamePerformance_EngineType engineType)
```

**描述**

为[GamePerformance_PackageInfo](#ZH-CN_TOPIC_0000002553202309__gameperformance_packageinfo)实例设置引擎类型。

**起始版本：**5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| packageInfo | 指针指向[GamePerformance_PackageInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab57ecb4bce0af8b741ef4aa069df2d87)实例。该值不可以为空，否则将返回错误码401。 |
| engineType | 引擎类型[GamePerformance_EngineType](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab7f3d09e6dd4af1692872b6b5815af45)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |

#### [HMS_GamePerformance_PackageInfo_SetEngineVersion](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga73b762ef177488deecf97f04395f70d5)()

```ets
[GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) HMS_GamePerformance_PackageInfo_SetEngineVersion (GamePerformance_PackageInfo *packageInfo, const char *engineVersion)
```

**描述**

为[GamePerformance_PackageInfo](#ZH-CN_TOPIC_0000002553202309__gameperformance_packageinfo)实例设置引擎版本号。

**起始版本：**5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| packageInfo | 指针指向[GamePerformance_PackageInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab57ecb4bce0af8b741ef4aa069df2d87)实例。该值不可以为空，否则将返回错误码401。 |
| engineVersion | 游戏引擎版本号。字符长度范围：[0, 64]。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |

#### [HMS_GamePerformance_PackageInfo_SetGameType](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gac5f6695702063b61b4f7cc885129dfe2)()

```ets
GamePerformance_ErrorCode HMS_GamePerformance_PackageInfo_SetGameType (GamePerformance_PackageInfo *packageInfo, const GamePerformance_GameType gameType)
```

**描述**

为[GamePerformance_PackageInfo](#ZH-CN_TOPIC_0000002553202309__gameperformance_packageinfo)实例设置游戏类型。

**起始版本：**5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| packageInfo | 指针指向[GamePerformance_PackageInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab57ecb4bce0af8b741ef4aa069df2d87)实例。该值不可以为空，否则将返回错误码401。 |
| gameType | 游戏类型[GamePerformance_GameType](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga9c1b6f00c4769f13c510a7a871c7afd3)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |

#### [HMS_GamePerformance_PackageInfo_SetVulkanSupported](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gadfbc32fbe65b9763d2cb393af8485dbb)()

```ets
[GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) HMS_GamePerformance_PackageInfo_SetVulkanSupported (GamePerformance_PackageInfo *packageInfo, const bool vulkanSupported)
```

**描述**

为[GamePerformance_PackageInfo](#ZH-CN_TOPIC_0000002553202309__gameperformance_packageinfo)实例设置是否支持vulkan。

**起始版本：**5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| packageInfo | 指针指向[GamePerformance_PackageInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab57ecb4bce0af8b741ef4aa069df2d87)实例。该值不可以为空，否则将返回错误码401。 |
| vulkanSupported | 是否支持vulkan。 - true：支持 - false：不支持 默认为false。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |

#### [HMS_GamePerformance_PlayerInfo_SetGamePlayerId](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gaccabd2811fc0e84e95a50219b34f1814)()

```ets
GamePerformance_ErrorCode HMS_GamePerformance_PlayerInfo_SetGamePlayerId (GamePerformance_PlayerInfo *playerInfo, const char *gamePlayerId)
```

**描述**

为[GamePerformance_PlayerInfo](#ZH-CN_TOPIC_0000002553202309__gameperformance_playerinfo)实例设置游戏玩家ID。

**起始版本：**5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| playerInfo | 指针指向[GamePerformance_PlayerInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga804b472fc080d73a2ce23da927ffd842)实例。该值不可以为空，否则将返回错误码401。 |
| gamePlayerId | 游戏玩家ID。字符长度范围：[0, 256]。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |

#### [HMS_GamePerformance_PlayerInfo_SetTeamPlayerId](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gaa5068c2f80ffc184cbebb03f22ece595)()

```ets
[GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) HMS_GamePerformance_PlayerInfo_SetTeamPlayerId (GamePerformance_PlayerInfo *playerInfo, const char *teamPlayerId)
```

**描述**

为[GamePerformance_PlayerInfo](#ZH-CN_TOPIC_0000002553202309__gameperformance_playerinfo)实例设置团队玩家ID。

**起始版本：**5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| playerInfo | 指针指向[GamePerformance_PlayerInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga804b472fc080d73a2ce23da927ffd842)实例。该值不可以为空，否则将返回错误码401。 |
| teamPlayerId | 团队玩家ID。字符长度范围：[0, 256]。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |

#### [HMS_GamePerformance_PlayerInfo_SetThirdOpenId](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga875a2f1dad9091927ada365f6e9b6d5d)()

```ets
GamePerformance_ErrorCode HMS_GamePerformance_PlayerInfo_SetThirdOpenId (GamePerformance_PlayerInfo *playerInfo, const char *thirdOpenId)
```

**描述**

为[GamePerformance_PlayerInfo](#ZH-CN_TOPIC_0000002553202309__gameperformance_playerinfo)实例设置游戏官方账号。

**起始版本：**5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| playerInfo | 指针指向[GamePerformance_PlayerInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga804b472fc080d73a2ce23da927ffd842)实例。该值不可以为空，否则将返回错误码401。 |
| thirdOpenId | 游戏官方账号。字符长度范围：[0, 128]。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |

#### HMS_GamePerformance_QueryCpuInfo()

```ets
[GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) HMS_GamePerformance_QueryCpuInfo (GamePerformance_CpuInfo **cpuInfo)
```

**描述**

查询CPU性能信息。当[GamePerformance_CpuInfo](#ZH-CN_TOPIC_0000002553202309__gameperformance_cpuinfo)实例不再使用，必须调用[HMS_GamePerformance_DestroyCpuInfo](#ZH-CN_TOPIC_0000002553202309__hms_gameperformance_destroycpuinfo)销毁该实例。

**起始版本：**6.0.2(22)

**参数:**

| 名称 | 描述 |
| --- | --- |
| cpuInfo | 二级指针指向GamePerformance_CpuInfo实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_INTERNAL_ERROR：系统内部错误。请通过在线提单系统提交此问题。 GAME_PERFORMANCE_INVALID_REQUEST：无效请求。请先调用HMS_GamePerformance_Init接口。 GAME_PERFORMANCE_PARAM_ERROR：参数错误。参数不能为空指针。 |

#### [HMS_GamePerformance_QueryGpuInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga93f67c2befdb52f4b59893a7a300f292)()

```ets
GamePerformance_ErrorCode HMS_GamePerformance_QueryGpuInfo (GamePerformance_GpuInfo **gpuInfo)
```

**描述**

查询GPU性能信息。当[GamePerformance_GpuInfo](#ZH-CN_TOPIC_0000002553202309__gameperformance_gpuinfo)实例不再使用，必须调用[HMS_GamePerformance_DestroyGpuInfo](#ZH-CN_TOPIC_0000002553202309__hms_gameperformance_destroygpuinfo)销毁该实例。


Mali系列GPU不支持采集GPU性能信息，无法获取设备GPU性能信息。

**起始版本：**5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| gpuInfo | 二级指针指向[GamePerformance_GpuInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gae85f740f82b3ca3f7ec9892d2f81a113)实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 GAME_PERFORMANCE_INTERNAL_ERROR：系统内部错误。 GAME_PERFORMANCE_INVALID_REQUEST：无效请求。 |

#### [HMS_GamePerformance_QueryThermalInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab7cb47e0dc3cce1169a8104827f7edb7)()

```ets
[GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) HMS_GamePerformance_QueryThermalInfo (GamePerformance_ThermalInfoQueryParameters *parameters, GamePerformance_ThermalInfo **thermalInfo)
```

**描述**

查询温度信息。当[GamePerformance_ThermalInfo](#ZH-CN_TOPIC_0000002553202309__gameperformance_thermalinfo)实例不再使用，必须调用[HMS_GamePerformance_DestroyThermalInfo](#ZH-CN_TOPIC_0000002553202309__hms_gameperformance_destroythermalinfo)销毁该实例。

**起始版本：**5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| parameters | 指针指向[GamePerformance_ThermalInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga6767ea8a1d76ed32db95dc0d3a265a8a)QueryParameters实例。该值不可以为空，否则将返回错误码401。 |
| thermalInfo | 二级指针指向[GamePerformance_ThermalInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga6767ea8a1d76ed32db95dc0d3a265a8a)实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 GAME_PERFORMANCE_INTERNAL_ERROR：系统内部错误。 GAME_PERFORMANCE_INVALID_REQUEST：无效请求。 |

#### [HMS_GamePerformance_RegisterThermalLevelChangedCallback](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gaa73a9464dbe4a973e7aed559835adbc6)()

```ets
GamePerformance_ErrorCode HMS_GamePerformance_RegisterThermalLevelChangedCallback (GamePerformance_DeviceInfoType *types[], size_t size, GamePerformance_ThermalLevelChangedCallback callback, void *userData)
```

**描述**

订阅温度变化事件，注册温度变化回调，当达到触发点时，将调用回调函数。

当温度等级改变并且温度等级小于3档时，该函数将被调用一次。当温度等级大于或等于3档时，该函数将每10秒调用一次。

Mali系列GPU不支持采集GPU性能信息，无法获取设备GPU性能信息。

**起始版本：**5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| types[] | 注册回调的设备性能信息类型[GamePerformance_DeviceInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga530e1cf28aa5c4d0b355dc053ce27e80)Type。 |
| size | types数组的长度。 |
| callback | 回调函数[GamePerformance_ThermalLevelChangedCallback](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga94e7e85a3f0ad0b495b2c525a15ebc8e)。 |
| userData | 用户指定数据。用户自定义任意类型，callback透传返回。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 GAME_PERFORMANCE_INTERNAL_ERROR：系统内部错误。 GAME_PERFORMANCE_INVALID_REQUEST：无效请求。 |

#### [HMS_GamePerformance_SceneInfo_SetChannelCount](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga4d6f34ef3b653c79c110c0fd35a5cca6)()

```ets
[GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) HMS_[GamePerformance_SceneInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7)_SetChannelCount (GamePerformance_SceneInfo *sceneInfo, const int64_t channelCount)
```

**描述**

为[GamePerformance_SceneInfo](#ZH-CN_TOPIC_0000002553202309__gameperformance_sceneinfo)实例设置每帧渲染的通道数。

**起始版本：**5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| sceneInfo | 指针指向[GamePerformance_SceneInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7)实例。该值不可以为空，否则将返回错误码401。 |
| channelCount | 每帧渲染的通道数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |

#### HMS_[GamePerformance_SceneInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7)_SetCurrentFrameRate()

```ets
GamePerformance_ErrorCode HMS_GamePerformance_SceneInfo_SetCurrentFrameRate (GamePerformance_SceneInfo *sceneInfo, const int64_t currentFrameRate)
```

**描述**

为[GamePerformance_SceneInfo](#ZH-CN_TOPIC_0000002553202309__gameperformance_sceneinfo)实例设置场景当前帧率。

**起始版本：**5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| sceneInfo | 指针指向[GamePerformance_SceneInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7)实例。该值不可以为空，否则将返回错误码401。 |
| currentFrameRate | 场景当前帧率。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |

#### [HMS_GamePerformance_SceneInfo_SetDescription](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga32193247c7f59a29920b5ec084a89a6c)()

```ets
[GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) HMS_[GamePerformance_SceneInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7)_SetDescription (GamePerformance_SceneInfo *sceneInfo, const char *description)
```

**描述**

为[GamePerformance_SceneInfo](#ZH-CN_TOPIC_0000002553202309__gameperformance_sceneinfo)实例设置场景描述。

**起始版本：**5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| sceneInfo | 指针指向[GamePerformance_SceneInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7)实例。该值不可以为空，否则将返回错误码401。 |
| description | 游戏场景描述（自定义描述）。字符长度范围：[0, 128]。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |

#### HMS_[GamePerformance_SceneInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7)_SetDrawCallCount()

```ets
GamePerformance_ErrorCode HMS_GamePerformance_SceneInfo_SetDrawCallCount (GamePerformance_SceneInfo *sceneInfo, const int64_t drawCallCount)
```

**描述**

为[GamePerformance_SceneInfo](#ZH-CN_TOPIC_0000002553202309__gameperformance_sceneinfo)实例设置每帧的平均Drawcall数。

**起始版本：**5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| sceneInfo | 指针指向[GamePerformance_SceneInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7)实例。该值不可以为空，否则将返回错误码401。 |
| drawCallCount | 每帧的平均Drawcall数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |

#### [HMS_GamePerformance_SceneInfo_SetImportanceLevel](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga5a7748133e83c9aebaa439e0d97fe742)()

```ets
[GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) HMS_[GamePerformance_SceneInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7)_SetImportanceLevel (GamePerformance_SceneInfo *sceneInfo, const GamePerformance_SceneImportanceLevel importanceLevel)
```

**描述**

为[GamePerformance_SceneInfo](#ZH-CN_TOPIC_0000002553202309__gameperformance_sceneinfo)实例设置场景重要程度。

**起始版本：**5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| sceneInfo | 指针指向[GamePerformance_SceneInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7)实例。该值不可以为空，否则将返回错误码401。 |
| importanceLevel | 场景重要程度[GamePerformance_SceneImportanceLevel](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gaf6bbf14a7010d4e99e6c758a718a08a6)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |

#### HMS_[GamePerformance_SceneInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7)_SetKeyThread()

```ets
GamePerformance_ErrorCode HMS_GamePerformance_SceneInfo_SetKeyThread (GamePerformance_SceneInfo *sceneInfo, const char *keyThread)
```

**描述**

为[GamePerformance_SceneInfo](#ZH-CN_TOPIC_0000002553202309__gameperformance_sceneinfo)实例设置关键线程。

**起始版本：**5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| sceneInfo | 指针指向[GamePerformance_SceneInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7)实例。该值不可以为空，否则将返回错误码401。 |
| keyThread | 该场景下的关键线程。 - render：渲染线程 - logic：逻辑线程 - net：网络线程 按照 render|xxx|logic|xxx 格式传入。字符长度范围：[0, 32]。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |

#### [HMS_GamePerformance_SceneInfo_SetMaxFrameRate](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gad672cb46e420b0cee29da39d4009a7c9)()

```ets
[GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) HMS_[GamePerformance_SceneInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7)_SetMaxFrameRate (GamePerformance_SceneInfo *sceneInfo, const int64_t maxFrameRate)
```

**描述**

为[GamePerformance_SceneInfo](#ZH-CN_TOPIC_0000002553202309__gameperformance_sceneinfo)实例设置场景最大帧率。

**起始版本：**5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| sceneInfo | 指针指向[GamePerformance_SceneInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7)实例。该值不可以为空，否则将返回错误码401。 |
| maxFrameRate | 场景最大帧率。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |

#### [HMS_GamePerformance_SceneInfo_SetMeshCount](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga00ab8ad16a928499daf8359fed8343b8)()

```ets
GamePerformance_ErrorCode HMS_GamePerformance_SceneInfo_SetMeshCount (GamePerformance_SceneInfo *sceneInfo, const int64_t meshCount)
```

**描述**

为[GamePerformance_SceneInfo](#ZH-CN_TOPIC_0000002553202309__gameperformance_sceneinfo)实例设置每帧的平均mesh数量。

**起始版本：**5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| sceneInfo | 指针指向[GamePerformance_SceneInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7)实例。该值不可以为空，否则将返回错误码401。 |
| meshCount | 每帧的平均mesh数量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |

#### [HMS_GamePerformance_SceneInfo_SetParticipantCount](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga3a3eaf50d555e6539c0f61543bc7898e)()

```ets
[GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) HMS_[GamePerformance_SceneInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7)_SetParticipantCount (GamePerformance_SceneInfo *sceneInfo, const int64_t participantCount)
```

**描述**

为[GamePerformance_SceneInfo](#ZH-CN_TOPIC_0000002553202309__gameperformance_sceneinfo)实例设置场景下的同屏人数。

**起始版本：**5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| sceneInfo | 指针指向[GamePerformance_SceneInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7)实例。该值不可以为空，否则将返回错误码401。 |
| participantCount | 场景下的同屏人数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |

#### HMS_[GamePerformance_SceneInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7)_SetRecommendedCpuLevel()

```ets
GamePerformance_ErrorCode HMS_GamePerformance_SceneInfo_SetRecommendedCpuLevel (GamePerformance_SceneInfo *sceneInfo, const GamePerformance_CpuLevel recommendedCpuLevel)
```

**描述**

为[GamePerformance_SceneInfo](#ZH-CN_TOPIC_0000002553202309__gameperformance_sceneinfo)实例设置推荐的CPU等级。

**起始版本：**5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| sceneInfo | 指针指向[GamePerformance_SceneInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7)实例。该值不可以为空，否则将返回错误码401。 |
| recommendedCpuLevel | 推荐的CPU等级[GamePerformance_CpuLevel](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga11ac456fd1b33d0b1f6220af5e5cd1ce)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |

#### [HMS_GamePerformance_SceneInfo_SetRecommendedDdrLevel](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga919d39c5eaa6e8e0a1f88c42f4d55264)()

```ets
[GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) HMS_[GamePerformance_SceneInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7)_SetRecommendedDdrLevel (GamePerformance_SceneInfo *sceneInfo, const GamePerformance_DdrLevel recommendedDdrLevel)
```

**描述**

为[GamePerformance_SceneInfo](#ZH-CN_TOPIC_0000002553202309__gameperformance_sceneinfo)实例设置推荐的DDR等级。

**起始版本：**5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| sceneInfo | 指针指向[GamePerformance_SceneInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7)实例。该值不可以为空，否则将返回错误码401。 |
| recommendedDdrLevel | 推荐的DDR等级[GamePerformance_DdrLevel](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gaec1b60b592a13ea85774a4d2ec8581bb)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |

#### HMS_[GamePerformance_SceneInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7)_SetRecommendedGpuLevel()

```ets
GamePerformance_ErrorCode HMS_GamePerformance_SceneInfo_SetRecommendedGpuLevel (GamePerformance_SceneInfo *sceneInfo, const GamePerformance_GpuLevel recommendedGpuLevel)
```

**描述**

为[GamePerformance_SceneInfo](#ZH-CN_TOPIC_0000002553202309__gameperformance_sceneinfo)实例设置推荐的GPU等级。

**起始版本：**5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| sceneInfo | 指针指向[GamePerformance_SceneInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7)实例。该值不可以为空，否则将返回错误码401。 |
| recommendedGpuLevel | 推荐的GPU等级[GamePerformance_GpuLevel](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga48d14f66a8d484b497157458dd13a473)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |

#### [HMS_GamePerformance_SceneInfo_SetSceneFrequency](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga3743a3ad2a364d6b039b2dbc1213f04a)()

```ets
[GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) HMS_[GamePerformance_SceneInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7)_SetSceneFrequency (GamePerformance_SceneInfo *sceneInfo, const int64_t sceneFrequency)
```

**描述**

为[GamePerformance_SceneInfo](#ZH-CN_TOPIC_0000002553202309__gameperformance_sceneinfo)实例设置该场景在一局游戏中出现的次数。

**起始版本：**5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| sceneInfo | 指针指向[GamePerformance_SceneInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7)实例。该值不可以为空，否则将返回错误码401。 |
| sceneFrequency | 该场景在一局游戏中出现的次数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |

#### HMS_[GamePerformance_SceneInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7)_SetSceneID()

```ets
GamePerformance_ErrorCode HMS_GamePerformance_SceneInfo_SetSceneID (GamePerformance_SceneInfo *sceneInfo, const int64_t sceneID)
```

**描述**

为[GamePerformance_SceneInfo](#ZH-CN_TOPIC_0000002553202309__gameperformance_sceneinfo)实例设置场景ID。

**起始版本：**5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| sceneInfo | 指针指向[GamePerformance_SceneInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7)实例。该值不可以为空，否则将返回错误码401。 |
| sceneID | 场景ID。 0：回切场景标识结束 1：游戏启动 2：游戏内更新 3：登录过程 4：主界面 5：加载一局游戏（自己加载） 6：加载一局游戏（自己加载完毕，等待其他玩家） 7：游戏中 8：观战模式 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |

#### [HMS_GamePerformance_SceneInfo_SetSceneTime](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gaa7d8eab6076c00e220da385a51016847)()

```ets
[GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) HMS_[GamePerformance_SceneInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7)_SetSceneTime (GamePerformance_SceneInfo *sceneInfo, const int64_t sceneTime)
```

**描述**

为[GamePerformance_SceneInfo](#ZH-CN_TOPIC_0000002553202309__gameperformance_sceneinfo)实例设置场景持续时间。

**起始版本：**5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| sceneInfo | 指针指向[GamePerformance_SceneInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7)实例。该值不可以为空，否则将返回错误码401。 |
| sceneTime | 场景持续时间，单位：毫秒（ms）。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |

#### HMS_[GamePerformance_SceneInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7)_SetShaderCount()

```ets
GamePerformance_ErrorCode HMS_GamePerformance_SceneInfo_SetShaderCount (GamePerformance_SceneInfo *sceneInfo, const int64_t shaderCount)
```

**描述**

为[GamePerformance_SceneInfo](#ZH-CN_TOPIC_0000002553202309__gameperformance_sceneinfo)实例设置每帧的平均shader数量。

**起始版本：**5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| sceneInfo | 指针指向[GamePerformance_SceneInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7)实例。该值不可以为空，否则将返回错误码401。 |
| shaderCount | 每帧的平均shader数量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |

#### [HMS_GamePerformance_SceneInfo_SetSubDescription](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga1d6ed7ffa24f5002ffbd799877467056)()

```ets
[GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) HMS_[GamePerformance_SceneInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7)_SetSubDescription (GamePerformance_SceneInfo *sceneInfo, const char *subDescription)
```

**描述**

为[GamePerformance_SceneInfo](#ZH-CN_TOPIC_0000002553202309__gameperformance_sceneinfo)实例设置子场景描述。

**起始版本：**5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| sceneInfo | 指针指向[GamePerformance_SceneInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7)实例。该值不可以为空，否则将返回错误码401。 |
| subDescription | 游戏子场景描述（自定义描述）。字符长度范围：[0, 128]。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |

#### HMS_[GamePerformance_SceneInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7)_SetSubSceneID()

```ets
GamePerformance_ErrorCode HMS_GamePerformance_SceneInfo_SetSubSceneID (GamePerformance_SceneInfo *sceneInfo, const char *subSceneID)
```

**描述**

为[GamePerformance_SceneInfo](#ZH-CN_TOPIC_0000002553202309__gameperformance_sceneinfo)实例设置子场景ID。

**起始版本：**5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| sceneInfo | 指针指向[GamePerformance_SceneInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7)实例。该值不可以为空，否则将返回错误码401。 |
| subSceneID | 游戏子场景ID。字符长度范围：[0, 128]。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |

#### [HMS_GamePerformance_SceneInfo_SetTextureCount](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gac374255a0c99f721ff7227e2c9a599d3)()

```ets
[GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) HMS_[GamePerformance_SceneInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7)_SetTextureCount (GamePerformance_SceneInfo *sceneInfo, const int64_t textureCount)
```

**描述**

为[GamePerformance_SceneInfo](#ZH-CN_TOPIC_0000002553202309__gameperformance_sceneinfo)实例设置每帧的平均纹理数量。

**起始版本：**5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| sceneInfo | 指针指向[GamePerformance_SceneInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7)实例。该值不可以为空，否则将返回错误码401。 |
| textureCount | 每帧的平均纹理数量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |

#### HMS_[GamePerformance_SceneInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7)_SetTriangleCount()

```ets
GamePerformance_ErrorCode HMS_GamePerformance_SceneInfo_SetTriangleCount (GamePerformance_SceneInfo *sceneInfo, const int64_t triangleCount)
```

**描述**

为[GamePerformance_SceneInfo](#ZH-CN_TOPIC_0000002553202309__gameperformance_sceneinfo)实例设置每帧的平均模型三角形数。

**起始版本：**5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| sceneInfo | 指针指向[GamePerformance_SceneInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7)实例。该值不可以为空，否则将返回错误码401。 |
| triangleCount | 每帧的平均模型三角形数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |

#### [HMS_GamePerformance_SceneInfo_SetVertexCount](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga5a10d96f46fbc5353d4c077970b5b3b7)()

```ets
[GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) HMS_[GamePerformance_SceneInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7)_SetVertexCount (GamePerformance_SceneInfo *sceneInfo, const int64_t vertexCount)
```

**描述**

为[GamePerformance_SceneInfo](#ZH-CN_TOPIC_0000002553202309__gameperformance_sceneinfo)实例设置每帧的平均模型顶点数。

**起始版本：**5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| sceneInfo | 指针指向[GamePerformance_SceneInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7)实例。该值不可以为空，否则将返回错误码401。 |
| vertexCount | 每帧的平均模型顶点数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |

#### HMS_[GamePerformance_ThermalInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga6767ea8a1d76ed32db95dc0d3a265a8a)_GetNowNormalizedCurrent()

```ets
GamePerformance_ErrorCode HMS_[GamePerformance_ThermalInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga6767ea8a1d76ed32db95dc0d3a265a8a)_GetNowNormalizedCurrent (GamePerformance_ThermalInfo *thermalInfo, int32_t *nowCurrent)
```

**描述**

从[GamePerformance_ThermalInfo](#ZH-CN_TOPIC_0000002553202309__gameperformance_thermalinfo)中获取当前的工作电流。

**起始版本：**6.0.2(22)

**设备行为差异：**该接口在Phone中可正常调用，在其他设备类型中无返回值。

**参数:**

| 名称 | 描述 |
| --- | --- |
| thermalInfo | 指针指向[GamePerformance_ThermalInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga6767ea8a1d76ed32db95dc0d3a265a8a)实例。该值不可以为空，否则将返回错误码1010300004。 |
| nowCurrent | 当前的工作电流，单位：mA。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_ERROR：参数错误。参数不能为空指针。 |

#### HMS_[GamePerformance_ThermalInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga6767ea8a1d76ed32db95dc0d3a265a8a)_GetRecommendMaxNormalizedCurrent()

```ets
GamePerformance_ErrorCode HMS_[GamePerformance_ThermalInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga6767ea8a1d76ed32db95dc0d3a265a8a)_GetRecommendMaxNormalizedCurrent (GamePerformance_ThermalInfo *thermalInfo, int32_t *recommendMaxCurrent)
```

**描述**

从[GamePerformance_ThermalInfo](#ZH-CN_TOPIC_0000002553202309__gameperformance_thermalinfo)中获取系统建议的最大工作电流。

**起始版本：**6.0.2(22)

**设备行为差异：**该接口在Phone中可正常调用，在其他设备类型中无返回值。

**参数:**

| 名称 | 描述 |
| --- | --- |
| thermalInfo | 指针指向[GamePerformance_ThermalInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga6767ea8a1d76ed32db95dc0d3a265a8a)实例。该值不可以为空，否则将返回错误码1010300004。 |
| recommendMaxCurrent | 系统建议的最大工作电流，单位：mA。 若当前的工作电流高于此值，设备会立即发烫。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_ERROR：参数错误。参数不能为空指针。 |

#### HMS_[GamePerformance_ThermalInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga6767ea8a1d76ed32db95dc0d3a265a8a)_GetRecommendNormalizedCurrent()

```ets
GamePerformance_ErrorCode HMS_[GamePerformance_ThermalInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga6767ea8a1d76ed32db95dc0d3a265a8a)_GetRecommendNormalizedCurrent (GamePerformance_ThermalInfo *thermalInfo, int32_t *recommendCurrent)
```

**描述**

从[GamePerformance_ThermalInfo](#ZH-CN_TOPIC_0000002553202309__gameperformance_thermalinfo)中获取系统建议的工作电流。

**起始版本：**6.0.2(22)

**设备行为差异：**该接口在Phone中可正常调用，在其他设备类型中无返回值。

**参数:**

| 名称 | 描述 |
| --- | --- |
| thermalInfo | 指针指向[GamePerformance_ThermalInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga6767ea8a1d76ed32db95dc0d3a265a8a)实例。该值不可以为空，否则将返回错误码1010300004。 |
| recommendCurrent | 系统建议的工作电流，单位：mA。 若当前的工作电流高于此值，温升趋势thermalTrend会大于0，设备有发烫风险。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_ERROR：参数错误。参数不能为空指针。 |

#### [HMS_GamePerformance_ThermalInfo_GetThermalLevel](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga36713ebcb8a94fd99772965437c18b7f)()

```ets
[GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) HMS_[GamePerformance_ThermalInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga6767ea8a1d76ed32db95dc0d3a265a8a)_GetThermalLevel (GamePerformance_ThermalInfo *thermalInfo, int32_t *thermalLevel)
```

**描述**

从[GamePerformance_ThermalInfo](#ZH-CN_TOPIC_0000002553202309__gameperformance_thermalinfo)中获取温度等级。

**起始版本：**5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| thermalInfo | 指针指向[GamePerformance_ThermalInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga6767ea8a1d76ed32db95dc0d3a265a8a)实例。该值不可以为空，否则将返回错误码401。 |
| thermalLevel | 温度等级，即温控档位，档位越高表示温度越高。不同档位及其建议如下： 1：无需处理。 2：建议降低无感知业务规格，例如后台更新降速或延迟运行。 3：建议暂停无感知业务，降低游戏非核心业务的规格，例如前台更新降速。 4：建议减少游戏特效，降低分辨率，画质。 5：建议降低全场景规格，进一步降低分辨率、画质等。 6：建议游戏降至最低规格。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |

#### [HMS_GamePerformance_ThermalInfo_GetThermalMargin](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gaf64ba82ad7342aeef688f5f515e86765)()

```ets
[GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) HMS_[GamePerformance_ThermalInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga6767ea8a1d76ed32db95dc0d3a265a8a)_GetThermalMargin (GamePerformance_ThermalInfo *thermalInfo, int32_t *thermalMargin)
```

**描述**

从温度信息[GamePerformance_ThermalInfo](#ZH-CN_TOPIC_0000002553202309__gameperformance_thermalinfo)中获取温度时间裕量。

**起始版本：**5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| thermalInfo | 指针指向[GamePerformance_ThermalInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga6767ea8a1d76ed32db95dc0d3a265a8a)实例。该值不可以为空，否则将返回错误码401。 |
| thermalMargin | 时间裕量，温控到达指定档位的时间，负值表示系统无法预测。单位：秒（s）。 说明： - 该数值超过60时，可信度降低。 - 值为0：表示已达到查询的温控档位。 - 值为-1：表示不能到达。 - 值为-2：表示查询的档位低于当前档位。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |

#### [HMS_GamePerformance_ThermalInfo_GetThermalTrend](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga4e0b7380232ea2120f017cf717d66f5f)()

```ets
[GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) HMS_[GamePerformance_ThermalInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga6767ea8a1d76ed32db95dc0d3a265a8a)_GetThermalTrend (GamePerformance_ThermalInfo *thermalInfo, int32_t *thermalTrend)
```

**描述**

从温度信息[GamePerformance_ThermalInfo](#ZH-CN_TOPIC_0000002553202309__gameperformance_thermalinfo)中获取温升趋势。

**起始版本：**5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| thermalInfo | 指针指向[GamePerformance_ThermalInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga6767ea8a1d76ed32db95dc0d3a265a8a)实例。该值不可以为空，否则将返回错误码401。 |
| thermalTrend | 温升趋势，取值范围为[-100, 100]，负号代表降温，数值越大说明当前温度变化越快。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |

#### HMS_[GamePerformance_ThermalInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga6767ea8a1d76ed32db95dc0d3a265a8a)QueryParameters_SetNeedsPrediction()

```ets
[GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) HMS_[GamePerformance_ThermalInfoQueryParameters](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga0e825c8963101d40a987d4057033c788)_SetNeedsPrediction (GamePerformance_ThermalInfoQueryParameters *parameters, const bool needsPrediction)
```

**描述**

为[GamePerformance_ThermalInfoQueryParameters](#ZH-CN_TOPIC_0000002553202309__gameperformance_thermalinfoqueryparameters)实例设置是否需要预测温升趋势。

**起始版本：**5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| parameters | 指针指向[GamePerformance_ThermalInfoQueryParameters](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga0e825c8963101d40a987d4057033c788)实例。该值不可以为空，否则将返回错误码401。 |
| needsPrediction | 是否需要预测温升趋势。如果需要预测温升趋势，将返回温度时间裕量和温升趋势。 - true：需要 - false：不需要 默认为false。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |

#### [HMS_GamePerformance_ThermalInfoQueryParameters_SetTargetThermalLevel](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga5cb94581ca23d465933e9316fdb0605d)()

```ets
[GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) HMS_[GamePerformance_ThermalInfoQueryParameters](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga0e825c8963101d40a987d4057033c788)_SetTargetThermalLevel (GamePerformance_ThermalInfoQueryParameters *parameters, const int32_t targetThermalLevel)
```

**描述**

为[GamePerformance_ThermalInfoQueryParameters](#ZH-CN_TOPIC_0000002553202309__gameperformance_thermalinfoqueryparameters)实例设置预测温升趋势的目标温度等级。

**起始版本：**5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| parameters | 指针指向[GamePerformance_ThermalInfoQueryParameters](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga0e825c8963101d40a987d4057033c788)实例。该值不可以为空，否则将返回错误码401。 |
| targetThermalLevel | 预测温升趋势的目标温度等级。如果需要预测温升趋势，将根据该目标温度等级计算返回温度时间裕量和温度趋势。取值请参见温度等级。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |

#### HMS_GamePerformance_UnregisterAllThermalLevelChangedCallbacks()

```ets
[GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) HMS_GamePerformance_UnregisterAllThermalLevelChangedCallbacks (void)
```

**描述**

取消注册所有温度变化回调。

**起始版本：**5.0.2(14)

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_INTERNAL_ERROR：系统内部错误。 GAME_PERFORMANCE_INVALID_REQUEST：无效请求。 |

#### HMS_GamePerformance_UnregisterThermalLevelChangedCallback()

```ets
[GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) HMS_GamePerformance_UnregisterThermalLevelChangedCallback ([GamePerformance_ThermalLevelChangedCallback](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga94e7e85a3f0ad0b495b2c525a15ebc8e) callback)
```

**描述**

取消注册指定温度变化回调。

**起始版本：**5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| callback | 回调函数[GamePerformance_ThermalLevelChangedCallback](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga94e7e85a3f0ad0b495b2c525a15ebc8e)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 GAME_PERFORMANCE_INTERNAL_ERROR：系统内部错误。 GAME_PERFORMANCE_INVALID_REQUEST：无效请求。 |

#### [HMS_GamePerformance_UpdateConfigInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga6fe77ea4f43939333c7c3b07e1204448)()

```ets
[GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) HMS_GamePerformance_UpdateConfigInfo ([GamePerformance_ConfigInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab05a6dca6b3570c3b45d74a9cb8ffdc9) *configInfo)
```

**描述**

更新游戏配置信息。

**起始版本：**5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| configInfo | 指针指向[GamePerformance_ConfigInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab05a6dca6b3570c3b45d74a9cb8ffdc9)实例。该值不可以为空，否则将返回错误码401。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 GAME_PERFORMANCE_INTERNAL_ERROR：系统内部错误。 GAME_PERFORMANCE_INVALID_REQUEST：无效请求。 |

#### [HMS_GamePerformance_UpdateNetInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga29ff530f9f37560359fdd0d28ba6275b)()

```ets
[GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) HMS_GamePerformance_UpdateNetInfo ([GamePerformance_NetInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gaba275a8588101424676258ffa7217097) *netInfo)
```

**描述**

更新游戏网络信息。

**起始版本：**5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| netInfo | 指针指向[GamePerformance_NetInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gaba275a8588101424676258ffa7217097)实例。该值不可以为空，否则将返回错误码401。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 GAME_PERFORMANCE_INTERNAL_ERROR：系统内部错误。 GAME_PERFORMANCE_INVALID_REQUEST：无效请求。 |

#### [HMS_GamePerformance_UpdatePackageInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga317ba7027076ce06ae73a6188bc3b129)()

```ets
[GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) HMS_GamePerformance_UpdatePackageInfo ([GamePerformance_PackageInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab57ecb4bce0af8b741ef4aa069df2d87) *packageInfo)
```

**描述**

更新游戏包信息。

**起始版本：**5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| packageInfo | 指针指向[GamePerformance_PackageInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab57ecb4bce0af8b741ef4aa069df2d87)实例。该值不可以为空，否则将返回错误码401。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 GAME_PERFORMANCE_INTERNAL_ERROR：系统内部错误。 GAME_PERFORMANCE_INVALID_REQUEST：无效请求。 |

#### [HMS_GamePerformance_UpdatePlayerInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga71c7be26b9531af9bcd807e3255c4e6f)()

```ets
[GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) HMS_GamePerformance_UpdatePlayerInfo ([GamePerformance_PlayerInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga804b472fc080d73a2ce23da927ffd842) *playerInfo)
```

**描述**

更新游戏玩家信息。

**起始版本：**5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| playerInfo | 指针指向[GamePerformance_PlayerInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga804b472fc080d73a2ce23da927ffd842)实例。该值不可以为空，否则将返回错误码401。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 GAME_PERFORMANCE_INTERNAL_ERROR：系统内部错误。 GAME_PERFORMANCE_INVALID_REQUEST：无效请求。 |

#### [HMS_GamePerformance_UpdateSceneInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gad9504bae5e5b570e55bdf7f84a7a05bf)()

```ets
[GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) HMS_GamePerformance_UpdateSceneInfo ([GamePerformance_SceneInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7) *sceneInfo)
```

**描述**

更新游戏场景信息。

**起始版本：**5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| sceneInfo | 指针指向[GamePerformance_SceneInfo](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7)实例。该值不可以为空，否则将返回错误码401。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance_ErrorCode](GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 GAME_PERFORMANCE_INTERNAL_ERROR：系统内部错误。 GAME_PERFORMANCE_INVALID_REQUEST：无效请求。 |
