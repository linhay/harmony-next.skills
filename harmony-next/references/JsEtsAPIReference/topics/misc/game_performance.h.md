# game_performance.h

**概述**

声明游戏场景感知的类型及相关接口。

引用文件： <GameServiceKit/game_performance.h>

库： libgame_performance.z.so

系统能力： SystemCapability.GameService.GamePerformance

起始版本： 5.0.2(14)

相关模块： [GamePerformance](GamePerformance.md)

**汇总**

**类型定义**

| 名称 | 描述 |
| --- | --- |
| typedef struct GamePerformance_DeviceInfo GamePerformance_DeviceInfo | 定义设备性能信息。 |
| typedef struct GamePerformance_GpuInfo GamePerformance_GpuInfo | 定义GPU性能信息。 |
| typedef struct GamePerformance_CpuInfo GamePerformance_CpuInfo | 定义CPU性能信息。 |
| typedef struct GamePerformance_ThermalInfo GamePerformance_ThermalInfo | 定义温度信息。 |
| typedef struct GamePerformance_ThermalInfoQueryParameters GamePerformance_ThermalInfoQueryParameters | 定义温度信息的查询参数。 |
| typedef struct GamePerformance_InitParameters GamePerformance_InitParameters | 定义初始化参数。 |
| typedef struct GamePerformance_PackageInfo GamePerformance_PackageInfo | 定义游戏包信息。 |
| typedef struct GamePerformance_ConfigInfo GamePerformance_ConfigInfo | 定义游戏配置信息。 |
| typedef struct GamePerformance_SceneInfo GamePerformance_SceneInfo | 定义游戏场景信息。 |
| typedef struct GamePerformance_NetInfo GamePerformance_NetInfo | 定义游戏网络信息。 |
| typedef struct GamePerformance_PlayerInfo GamePerformance_PlayerInfo | 定义游戏玩家信息。 |
| typedef enum GamePerformance_EngineType GamePerformance_EngineType | 定义游戏引擎类型。 |
| typedef enum GamePerformance_GameType GamePerformance_GameType | 定义游戏类型。 |
| typedef enum GamePerformance_PictureQualityLevel GamePerformance_PictureQualityLevel | 定义画质等级。 |
| typedef enum GamePerformance_SceneImportanceLevel GamePerformance_SceneImportanceLevel | 定义游戏场景重要程度。 |
| typedef enum GamePerformance_CpuLevel GamePerformance_CpuLevel | 定义CPU等级。 |
| typedef enum GamePerformance_GpuLevel GamePerformance_GpuLevel | 定义GPU等级。 |
| typedef enum GamePerformance_DdrLevel GamePerformance_DdrLevel | 定义DDR等级。 |
| typedef enum GamePerformance_NetLoad GamePerformance_NetLoad | 定义网络负载等级。 |
| typedef enum GamePerformance_ErrorCode GamePerformance_ErrorCode | 定义错误码。 |
| typedef enum GamePerformance_DeviceInfoType GamePerformance_DeviceInfoType | 定义设备性能信息类型。 |
| typedef void(*GamePerformance_ThermalLevelChangedCallback) (GamePerformance_DeviceInfo *deviceInfo, void *userData) | HMS_GamePerformance_RegisterThermalLevelChangedCallback中使用的回调函数。当温度等级改变并且温度等级小于3档时，该函数将被调用一次。当温度等级大于或等于3档时，该函数将每10秒调用一次。 |

**枚举**

| 名称 | 描述 |
| --- | --- |
| GamePerformance_EngineType { GAME_PERFORMANCE_ENGINE_TYPE_UNITY = 1, GAME_PERFORMANCE_ENGINE_TYPE_UNREAL = 2, GAME_PERFORMANCE_ENGINE_TYPE_MESSIAH = 3, GAME_PERFORMANCE_ENGINE_TYPE_COCOS = 4, GAME_PERFORMANCE_ENGINE_TYPE_OTHERS = 200 } | 此枚举描述引擎类型。 |
| GamePerformance_GameType { GAME_PERFORMANCE_GAME_TYPE_MOBA = 1, GAME_PERFORMANCE_GAME_TYPE_RPG = 2, GAME_PERFORMANCE_GAME_TYPE_FPS = 3, GAME_PERFORMANCE_GAME_TYPE_FTG = 4, GAME_PERFORMANCE_GAME_TYPE_RAC = 5, GAME_PERFORMANCE_GAME_TYPE_OTHERS = 200 } | 此枚举描述游戏类型。 |
| GamePerformance_PictureQualityLevel { GAME_PERFORMANCE_PQL_SMOOTH = 1, GAME_PERFORMANCE_PQL_BALANCED = 2, GAME_PERFORMANCE_PQL_HD = 3, GAME_PERFORMANCE_PQL_HDR = 4, GAME_PERFORMANCE_PQL_UHD = 5 } | 此枚举描述画质等级。 |
| GamePerformance_SceneImportanceLevel { GAME_PERFORMANCE_SIL_LEVEL1 = 1, GAME_PERFORMANCE_SIL_LEVEL2 = 2, GAME_PERFORMANCE_SIL_LEVEL3 = 3, GAME_PERFORMANCE_SIL_LEVEL4 = 4, GAME_PERFORMANCE_SIL_LEVEL5 = 5 } | 此枚举描述场景重要程度。 |
| GamePerformance_CpuLevel { GAME_PERFORMANCE_CPU_LEVEL_LOW = 1, GAME_PERFORMANCE_CPU_LEVEL_MIDDLE = 2, GAME_PERFORMANCE_CPU_LEVEL_HIGH = 3 } | 此枚举描述CPU等级。 |
| GamePerformance_GpuLevel { GAME_PERFORMANCE_GPU_LEVEL_LOW = 1, GAME_PERFORMANCE_GPU_LEVEL_MIDDLE = 2, GAME_PERFORMANCE_GPU_LEVEL_HIGH = 3 } | 此枚举描述GPU等级。 |
| GamePerformance_DdrLevel { GAME_PERFORMANCE_DDR_LEVEL_LOW = 1, GAME_PERFORMANCE_DDR_LEVEL_MIDDLE = 2, GAME_PERFORMANCE_DDR_LEVEL_HIGH = 3 } | 此枚举描述DDR等级。 |
| GamePerformance_NetLoad { GAME_PERFORMANCE_NET_LOAD_LIGHT = 1, GAME_PERFORMANCE_NET_LOAD_MODERATE = 2, GAME_PERFORMANCE_NET_LOAD_HEAVY = 3 } | 此枚举描述网络负载等级。 |
| GamePerformance_ErrorCode { GAME_PERFORMANCE_SUCCESS = 0, GAME_PERFORMANCE_PARAM_INVALID = 401, GAME_PERFORMANCE_INTERNAL_ERROR = 1010300001, GAME_PERFORMANCE_AUTH_FAILED = 1010300002, GAME_PERFORMANCE_INVALID_REQUEST = 1010300003, GAME_PERFORMANCE_PARAM_ERROR = 1010300004 } | 此枚举描述错误码。 GAME_PERFORMANCE_PARAM_ERROR 从6.0.2(22)开始支持。 |
| GamePerformance_DeviceInfoType { GAME_PERFORMANCE_DEVICEINFO_TYPE_THERMAL = 0, GAME_PERFORMANCE_DEVICEINFO_TYPE_GPU = 1, GAME_PERFORMANCE_DEVICEINFO_TYPE_CPU = 2 } | 此枚举描述设备性能信息类型。 GAME_PERFORMANCE_DEVICEINFO_TYPE_CPU 从6.0.2(22)开始支持。 |

**函数**

| 名称 | 描述 |
| --- | --- |
| GamePerformance_ErrorCode HMS_GamePerformance_CreateInitParameters (GamePerformance_InitParameters **initParameters) | 创建GamePerformance_InitParameters实例，该实例在HMS_GamePerformance_Init方法中使用。 |
| GamePerformance_ErrorCode HMS_GamePerformance_DestroyInitParameters (GamePerformance_InitParameters **initParameters) | 当GamePerformance_InitParameters实例不再使用，销毁该实例。 |
| GamePerformance_ErrorCode HMS_GamePerformance_InitParameters_SetBundleName (GamePerformance_InitParameters *initParameters, const char *bundleName) | 为GamePerformance_InitParameters实例设置包名。 |
| GamePerformance_ErrorCode HMS_GamePerformance_InitParameters_SetAppVersion (GamePerformance_InitParameters *initParameters, const char *appVersion) | 为GamePerformance_InitParameters实例设置版本号。 |
| GamePerformance_ErrorCode HMS_GamePerformance_Init (GamePerformance_InitParameters *initParameters) | 初始化游戏场景感知。 说明：调用HMS_GamePerformance_Init前，必须已设置bundleName，appVersion。 |
| GamePerformance_ErrorCode HMS_GamePerformance_CreatePackageInfo (GamePerformance_PackageInfo **packageInfo) | 创建GamePerformance_PackageInfo实例，该实例在HMS_GamePerformance_UpdatePackageInfo方法中使用。 |
| GamePerformance_ErrorCode HMS_GamePerformance_DestroyPackageInfo (GamePerformance_PackageInfo **packageInfo) | 当GamePerformance_PackageInfo实例不再使用，销毁该实例。 |
| GamePerformance_ErrorCode HMS_GamePerformance_PackageInfo_SetBundleName (GamePerformance_PackageInfo *packageInfo, const char *bundleName) | 为GamePerformance_PackageInfo实例设置包名。 |
| GamePerformance_ErrorCode HMS_GamePerformance_PackageInfo_SetAppVersion (GamePerformance_PackageInfo *packageInfo, const char *appVersion) | 为GamePerformance_PackageInfo实例设置版本号。 |
| GamePerformance_ErrorCode HMS_GamePerformance_PackageInfo_SetEngineType (GamePerformance_PackageInfo *packageInfo, const GamePerformance_EngineType engineType) | 为GamePerformance_PackageInfo实例设置引擎类型。 |
| GamePerformance_ErrorCode HMS_GamePerformance_PackageInfo_SetEngineVersion (GamePerformance_PackageInfo *packageInfo, const char *engineVersion) | 为GamePerformance_PackageInfo实例设置引擎版本号。 |
| GamePerformance_ErrorCode HMS_GamePerformance_PackageInfo_SetGameType (GamePerformance_PackageInfo *packageInfo, const GamePerformance_GameType gameType) | 为GamePerformance_PackageInfo实例设置游戏类型。 |
| GamePerformance_ErrorCode HMS_GamePerformance_PackageInfo_SetVulkanSupported (GamePerformance_PackageInfo *packageInfo, const bool vulkanSupported) | 为GamePerformance_PackageInfo实例设置是否支持vulkan。 |
| GamePerformance_ErrorCode HMS_GamePerformance_UpdatePackageInfo (GamePerformance_PackageInfo *packageInfo) | 更新游戏包信息。 说明：调用HMS_GamePerformance_UpdatePackageInfo前，必须已设置bundleName，appVersion。 |
| GamePerformance_ErrorCode HMS_GamePerformance_CreateConfigInfo (GamePerformance_ConfigInfo **configInfo) | 创建GamePerformance_ConfigInfo实例，该实例在HMS_GamePerformance_UpdateConfigInfo方法中使用。 |
| GamePerformance_ErrorCode HMS_GamePerformance_DestroyConfigInfo (GamePerformance_ConfigInfo **configInfo) | 当GamePerformance_ConfigInfo实例不再使用，销毁该实例。 |
| GamePerformance_ErrorCode HMS_GamePerformance_ConfigInfo_SetMaxPictureQualityLevel (GamePerformance_ConfigInfo *configInfo, const GamePerformance_PictureQualityLevel maxPictureQualityLevel) | 为GamePerformance_ConfigInfo实例设置最大画质等级。 |
| GamePerformance_ErrorCode HMS_GamePerformance_ConfigInfo_SetCurrentPictureQualityLevel (GamePerformance_ConfigInfo *configInfo, const GamePerformance_PictureQualityLevel currentPictureQualityLevel) | 为GamePerformance_ConfigInfo实例设置当前画质等级。 |
| GamePerformance_ErrorCode HMS_GamePerformance_ConfigInfo_SetMaxFrameRate (GamePerformance_ConfigInfo *configInfo, const int64_t maxFrameRate) | 为GamePerformance_ConfigInfo实例设置最大帧率。 |
| GamePerformance_ErrorCode HMS_GamePerformance_ConfigInfo_SetCurrentFrameRate (GamePerformance_ConfigInfo *configInfo, const int64_t currentFrameRate) | 为GamePerformance_ConfigInfo实例设置当前帧率。 |
| GamePerformance_ErrorCode HMS_GamePerformance_ConfigInfo_SetMaxResolution (GamePerformance_ConfigInfo *configInfo, const char *maxResolution) | 为GamePerformance_ConfigInfo实例设置最大分辨率。 |
| GamePerformance_ErrorCode HMS_GamePerformance_ConfigInfo_SetCurrentResolution (GamePerformance_ConfigInfo *configInfo, const char *currentResolution) | 为GamePerformance_ConfigInfo实例设置当前分辨率。 |
| GamePerformance_ErrorCode HMS_GamePerformance_ConfigInfo_SetAntiAliasingEnabled (GamePerformance_ConfigInfo *configInfo, const bool antiAliasingEnabled) | 为GamePerformance_ConfigInfo实例设置是否开启抗锯齿。 |
| GamePerformance_ErrorCode HMS_GamePerformance_ConfigInfo_SetShadowEnabled (GamePerformance_ConfigInfo *configInfo, const bool shadowEnabled) | 为GamePerformance_ConfigInfo实例设置是否开启阴影。 |
| GamePerformance_ErrorCode HMS_GamePerformance_ConfigInfo_SetMultithreadingEnabled (GamePerformance_ConfigInfo *configInfo, const bool multithreadingEnabled) | 为GamePerformance_ConfigInfo实例设置开启多线程。 |
| GamePerformance_ErrorCode HMS_GamePerformance_ConfigInfo_SetParticleEnabled (GamePerformance_ConfigInfo *configInfo, const bool particleEnabled) | 为GamePerformance_ConfigInfo实例设置粒子效果。 |
| GamePerformance_ErrorCode HMS_GamePerformance_ConfigInfo_SetHdModeEnabled (GamePerformance_ConfigInfo *configInfo, const bool hdModeEnabled) | 为GamePerformance_ConfigInfo实例设置开启高清模式。 |
| GamePerformance_ErrorCode HMS_GamePerformance_UpdateConfigInfo (GamePerformance_ConfigInfo *configInfo) | 更新游戏配置信息。 |
| GamePerformance_ErrorCode HMS_GamePerformance_CreateSceneInfo (GamePerformance_SceneInfo **sceneInfo) | 创建GamePerformance_SceneInfo实例，该实例在HMS_GamePerformance_UpdateSceneInfo方法中使用。 |
| GamePerformance_ErrorCode HMS_GamePerformance_DestroySceneInfo (GamePerformance_SceneInfo **sceneInfo) | 当GamePerformance_SceneInfo实例不再使用，销毁该实例。 |
| GamePerformance_ErrorCode HMS_GamePerformance_SceneInfo_SetSceneID (GamePerformance_SceneInfo *sceneInfo, const int64_t sceneID) | 为GamePerformance_SceneInfo实例设置场景ID。 |
| GamePerformance_ErrorCode HMS_GamePerformance_SceneInfo_SetDescription (GamePerformance_SceneInfo *sceneInfo, const char *description) | 为GamePerformance_SceneInfo实例设置场景描述。 |
| GamePerformance_ErrorCode HMS_GamePerformance_SceneInfo_SetSubSceneID (GamePerformance_SceneInfo *sceneInfo, const char *subSceneID) | 为GamePerformance_SceneInfo实例设置子场景ID。 |
| GamePerformance_ErrorCode HMS_GamePerformance_SceneInfo_SetSubDescription (GamePerformance_SceneInfo *sceneInfo, const char *subDescription) | 为GamePerformance_SceneInfo实例设置子场景描述。 |
| GamePerformance_ErrorCode HMS_GamePerformance_SceneInfo_SetImportanceLevel (GamePerformance_SceneInfo *sceneInfo, const GamePerformance_SceneImportanceLevel importanceLevel) | 为GamePerformance_SceneInfo实例设置场景重要程度。 |
| GamePerformance_ErrorCode HMS_GamePerformance_SceneInfo_SetSceneFrequency (GamePerformance_SceneInfo *sceneInfo, const int64_t sceneFrequency) | 为GamePerformance_SceneInfo实例设置该场景在一局游戏中出现的次数。 |
| GamePerformance_ErrorCode HMS_GamePerformance_SceneInfo_SetSceneTime (GamePerformance_SceneInfo *sceneInfo, const int64_t sceneTime) | 为GamePerformance_SceneInfo实例设置场景持续时间。 |
| GamePerformance_ErrorCode HMS_GamePerformance_SceneInfo_SetRecommendedCpuLevel (GamePerformance_SceneInfo *sceneInfo, const GamePerformance_CpuLevel recommendedCpuLevel) | 为GamePerformance_SceneInfo实例设置推荐的CPU等级。 |
| GamePerformance_ErrorCode HMS_GamePerformance_SceneInfo_SetRecommendedGpuLevel (GamePerformance_SceneInfo *sceneInfo, const GamePerformance_GpuLevel recommendedGpuLevel) | 为GamePerformance_SceneInfo实例设置推荐的GPU等级。 |
| GamePerformance_ErrorCode HMS_GamePerformance_SceneInfo_SetRecommendedDdrLevel (GamePerformance_SceneInfo *sceneInfo, const GamePerformance_DdrLevel recommendedDdrLevel) | 为GamePerformance_SceneInfo实例设置推荐的DDR等级。 |
| GamePerformance_ErrorCode HMS_GamePerformance_SceneInfo_SetMaxFrameRate (GamePerformance_SceneInfo *sceneInfo, const int64_t maxFrameRate) | 为GamePerformance_SceneInfo实例设置场景最大帧率。 |
| GamePerformance_ErrorCode HMS_GamePerformance_SceneInfo_SetCurrentFrameRate (GamePerformance_SceneInfo *sceneInfo, const int64_t currentFrameRate) | 为GamePerformance_SceneInfo实例设置场景当前帧率。 |
| GamePerformance_ErrorCode HMS_GamePerformance_SceneInfo_SetKeyThread (GamePerformance_SceneInfo *sceneInfo, const char *keyThread) | 为GamePerformance_SceneInfo实例设置关键线程。 |
| GamePerformance_ErrorCode HMS_GamePerformance_SceneInfo_SetDrawCallCount (GamePerformance_SceneInfo *sceneInfo, const int64_t drawCallCount) | 为GamePerformance_SceneInfo实例设置每帧的平均Drawcall数。 |
| GamePerformance_ErrorCode HMS_GamePerformance_SceneInfo_SetVertexCount (GamePerformance_SceneInfo *sceneInfo, const int64_t vertexCount) | 为GamePerformance_SceneInfo实例设置每帧的平均模型顶点数。 |
| GamePerformance_ErrorCode HMS_GamePerformance_SceneInfo_SetTriangleCount (GamePerformance_SceneInfo *sceneInfo, const int64_t triangleCount) | 为GamePerformance_SceneInfo实例设置每帧的平均模型三角形数。 |
| GamePerformance_ErrorCode HMS_GamePerformance_SceneInfo_SetShaderCount (GamePerformance_SceneInfo *sceneInfo, const int64_t shaderCount) | 为GamePerformance_SceneInfo实例设置每帧的平均shader数量。 |
| GamePerformance_ErrorCode HMS_GamePerformance_SceneInfo_SetTextureCount (GamePerformance_SceneInfo *sceneInfo, const int64_t textureCount) | 为GamePerformance_SceneInfo实例设置每帧的平均纹理数量。 |
| GamePerformance_ErrorCode HMS_GamePerformance_SceneInfo_SetMeshCount (GamePerformance_SceneInfo *sceneInfo, const int64_t meshCount) | 为GamePerformance_SceneInfo实例设置每帧的平均mesh数量。 |
| GamePerformance_ErrorCode HMS_GamePerformance_SceneInfo_SetChannelCount (GamePerformance_SceneInfo *sceneInfo, const int64_t channelCount) | 为GamePerformance_SceneInfo实例设置每帧渲染的通道数。 |
| GamePerformance_ErrorCode HMS_GamePerformance_SceneInfo_SetParticipantCount (GamePerformance_SceneInfo *sceneInfo, const int64_t participantCount) | 为GamePerformance_SceneInfo实例设置场景下的同屏人数。 |
| GamePerformance_ErrorCode HMS_GamePerformance_UpdateSceneInfo (GamePerformance_SceneInfo *sceneInfo) | 更新游戏场景信息。 说明：调用HMS_GamePerformance_UpdateSceneInfo前，必须已设置sceneID，importanceLevel。 |
| GamePerformance_ErrorCode HMS_GamePerformance_CreateNetInfo (GamePerformance_NetInfo **netInfo) | 创建GamePerformance_NetInfo实例，该实例在HMS_GamePerformance_UpdateNetInfo方法中使用。 |
| GamePerformance_ErrorCode HMS_GamePerformance_DestroyNetInfo (GamePerformance_NetInfo **netInfo) | 当GamePerformance_NetInfo实例不再使用，销毁该实例。 |
| GamePerformance_ErrorCode HMS_GamePerformance_NetInfo_SetTotalLatency (GamePerformance_NetInfo *netInfo, const int64_t total) | 为GamePerformance_NetInfo实例设置总网络时延。 |
| GamePerformance_ErrorCode HMS_GamePerformance_NetInfo_SetUplinkLatency (GamePerformance_NetInfo *netInfo, const int64_t up) | 为GamePerformance_NetInfo实例设置上行网络时延。 |
| GamePerformance_ErrorCode HMS_GamePerformance_NetInfo_SetDownlinkLatency (GamePerformance_NetInfo *netInfo, const int64_t down) | 为GamePerformance_NetInfo实例设置下行网络时延。 |
| GamePerformance_ErrorCode HMS_GamePerformance_NetInfo_SetServerLatency (GamePerformance_NetInfo *netInfo, const int64_t server) | 为GamePerformance_NetInfo实例设置服务器网络时延。 |
| GamePerformance_ErrorCode HMS_GamePerformance_NetInfo_SetNetLoad (GamePerformance_NetInfo *netInfo, const GamePerformance_NetLoad netLoad) | 为GamePerformance_NetInfo实例设置网络负载。 |
| GamePerformance_ErrorCode HMS_GamePerformance_UpdateNetInfo (GamePerformance_NetInfo *netInfo) | 更新游戏网络信息。 说明：调用HMS_GamePerformance_UpdateNetInfo前必须已设置totalLatency。 |
| GamePerformance_ErrorCode HMS_GamePerformance_CreatePlayerInfo (GamePerformance_PlayerInfo **playerInfo) | 创建GamePerformance_PlayerInfo实例，该实例在HMS_GamePerformance_UpdatePlayerInfo方法中使用。 |
| GamePerformance_ErrorCode HMS_GamePerformance_DestroyPlayerInfo (GamePerformance_PlayerInfo **playerInfo) | 当GamePerformance_PlayerInfo实例不再使用，销毁该实例。 |
| GamePerformance_ErrorCode HMS_GamePerformance_PlayerInfo_SetGamePlayerId (GamePerformance_PlayerInfo *playerInfo, const char *gamePlayerId) | 为GamePerformance_PlayerInfo实例设置游戏玩家ID。 说明：gamePlayerId、teamPlayerId和thirdOpenId不能同时为空。 |
| GamePerformance_ErrorCode HMS_GamePerformance_PlayerInfo_SetTeamPlayerId (GamePerformance_PlayerInfo *playerInfo, const char *teamPlayerId) | 为GamePerformance_PlayerInfo实例设置团队玩家ID。 说明：gamePlayerId、teamPlayerId和thirdOpenId不能同时为空。 |
| GamePerformance_ErrorCode HMS_GamePerformance_PlayerInfo_SetThirdOpenId (GamePerformance_PlayerInfo *playerInfo, const char *thirdOpenId) | 为GamePerformance_PlayerInfo实例设置游戏官方账号。 说明：gamePlayerId、teamPlayerId和thirdOpenId不能同时为空。 |
| GamePerformance_ErrorCode HMS_GamePerformance_UpdatePlayerInfo (GamePerformance_PlayerInfo *playerInfo) | 更新游戏玩家信息。 |
| GamePerformance_ErrorCode HMS_GamePerformance_RegisterThermalLevelChangedCallback (GamePerformance_DeviceInfoType *types[], size_t size, GamePerformance_ThermalLevelChangedCallback callback, void *userData) | 订阅温度变化事件，注册温度变化回调，当达到触发点时，将调用回调函数。 |
| GamePerformance_ErrorCode HMS_GamePerformance_UnregisterThermalLevelChangedCallback (GamePerformance_ThermalLevelChangedCallback callback) | 取消注册指定温度变化回调。 |
| GamePerformance_ErrorCode HMS_GamePerformance_UnregisterAllThermalLevelChangedCallbacks (void) | 取消注册所有温度变化回调。 |
| GamePerformance_ErrorCode HMS_GamePerformance_CreateThermalInfoQueryParameters (GamePerformance_ThermalInfoQueryParameters **parameters) | 创建GamePerformance_ThermalInfoQueryParameters实例，该实例在HMS_GamePerformance_QueryThermalInfo方法中使用。 |
| GamePerformance_ErrorCode HMS_GamePerformance_DestroyThermalInfoQueryParameters (GamePerformance_ThermalInfoQueryParameters **parameters) | 当GamePerformance_ThermalInfoQueryParameters实例不再使用，销毁该实例。 |
| GamePerformance_ErrorCode HMS_GamePerformance_ThermalInfoQueryParameters_SetNeedsPrediction (GamePerformance_ThermalInfoQueryParameters *parameters, const bool needsPrediction) | 为GamePerformance_ThermalInfoQueryParameters实例设置是否需要预测温升趋势。 |
| GamePerformance_ErrorCode HMS_GamePerformance_ThermalInfoQueryParameters_SetTargetThermalLevel (GamePerformance_ThermalInfoQueryParameters *parameters, const int32_t targetThermalLevel) | 为GamePerformance_ThermalInfoQueryParameters实例设置预测温升趋势的目标温度等级。 |
| GamePerformance_ErrorCode HMS_GamePerformance_QueryThermalInfo (GamePerformance_ThermalInfoQueryParameters *parameters，GamePerformance_ThermalInfo **thermalInfo) | 查询温度信息。 |
| GamePerformance_ErrorCode HMS_GamePerformance_DestroyThermalInfo (GamePerformance_ThermalInfo **thermalInfo) | 当GamePerformance_ThermalInfo实例不再使用，销毁该实例。 |
| GamePerformance_ErrorCode HMS_GamePerformance_QueryGpuInfo (GamePerformance_GpuInfo **gpuInfo) | 查询GPU性能信息。 |
| GamePerformance_ErrorCode HMS_GamePerformance_DestroyGpuInfo (GamePerformance_GpuInfo **gpuInfo) | 当GamePerformance_GpuInfo实例不再使用，销毁该实例。 |
| GamePerformance_ErrorCode HMS_GamePerformance_QueryCpuInfo (GamePerformance_CpuInfo **cpuInfo) | 查询CPU性能信息。 |
| GamePerformance_ErrorCode HMS_GamePerformance_DestroyCpuInfo (GamePerformance_CpuInfo **cpuInfo) | 当GamePerformance_CpuInfo实例不再使用，销毁该实例。 |
| GamePerformance_ErrorCode HMS_GamePerformance_DeviceInfo_GetThermalInfo (GamePerformance_DeviceInfo *deviceInfo, GamePerformance_ThermalInfo **thermalInfo) | 从设备性能信息GamePerformance_DeviceInfo中获取温度信息GamePerformance_ThermalInfo。 |
| GamePerformance_ErrorCode HMS_GamePerformance_ThermalInfo_GetThermalMargin (GamePerformance_ThermalInfo *thermalInfo, int32_t *thermalMargin) | 从温度信息GamePerformance_ThermalInfo中获取温度时间裕量。 |
| GamePerformance_ErrorCode HMS_GamePerformance_ThermalInfo_GetThermalTrend (GamePerformance_ThermalInfo *thermalInfo, int32_t *thermalTrend) | 从GamePerformance_ThermalInfo中获取温升趋势。 |
| GamePerformance_ErrorCode HMS_GamePerformance_ThermalInfo_GetThermalLevel (GamePerformance_ThermalInfo *thermalInfo, int32_t *thermalLevel) | 从GamePerformance_ThermalInfo中获取温度等级。 |
| GamePerformance_ErrorCode HMS_GamePerformance_ThermalInfo_GetRecommendNormalizedCurrent (GamePerformance_ThermalInfo *thermalInfo, int32_t *recommendCurrent) | 从GamePerformance_ThermalInfo中获取系统建议的工作电流。若当前的工作电流高于此值，温升趋势thermalTrend会大于0，设备有发烫风险。 |
| GamePerformance_ErrorCode HMS_GamePerformance_ThermalInfo_GetNowNormalizedCurrent (GamePerformance_ThermalInfo *thermalInfo, int32_t *nowCurrent) | 从GamePerformance_ThermalInfo中获取当前的工作电流。 |
| GamePerformance_ErrorCode HMS_GamePerformance_ThermalInfo_GetRecommendMaxNormalizedCurrent (GamePerformance_ThermalInfo *thermalInfo, int32_t *recommendMaxCurrent) | 从GamePerformance_ThermalInfo中获取系统建议的最大工作电流。若当前的工作电流高于此值，设备会立即发烫。 |
| GamePerformance_ErrorCode HMS_GamePerformance_DeviceInfo_GetGpuInfo (GamePerformance_DeviceInfo *deviceInfo, GamePerformance_GpuInfo **gpuInfo) | 从设备性能信息GamePerformance_DeviceInfo中获取GPU性能信息GamePerformance_GpuInfo。 |
| GamePerformance_ErrorCode HMS_GamePerformance_GpuInfo_GetGpuLoadLevel (GamePerformance_GpuInfo *gpuInfo, int32_t *gpuLoadLevel) | 从GamePerformance_GpuInfo中获取GPU负载信息。 |
| GamePerformance_ErrorCode HMS_GamePerformance_GpuInfo_GetVertexLoadLevel (GamePerformance_GpuInfo *gpuInfo, int32_t *vertexLoadLevel) | 从GamePerformance_GpuInfo中获取GPU顶点处理负载等级。 |
| GamePerformance_ErrorCode HMS_GamePerformance_GpuInfo_GetFragmentLoadLevel (GamePerformance_GpuInfo *gpuInfo, int32_t *fragmentLoadLevel) | 从GamePerformance_GpuInfo中获取GPU片元处理负载等级。 |
| GamePerformance_ErrorCode HMS_GamePerformance_GpuInfo_GetTextureLoadLevel (GamePerformance_GpuInfo *gpuInfo, int32_t *textureLoadLevel) | 从GamePerformance_GpuInfo中获取GPU纹理处理负载等级。 |
| GamePerformance_ErrorCode HMS_GamePerformance_GpuInfo_GetBandwidthLoadLevel (GamePerformance_GpuInfo *gpuInfo, int32_t *bandwidthLoadLevel) | 从GamePerformance_GpuInfo中获取GPU带宽负载等级。 |
| GamePerformance_ErrorCode HMS_GamePerformance_GpuInfo_GetCurrentFrequency (GamePerformance_GpuInfo *gpuInfo, int32_t *currentFrequency) | 从GamePerformance_GpuInfo中获取GPU频点信息。 |
| GamePerformance_ErrorCode HMS_GamePerformance_DeviceInfo_GetCpuInfo (GamePerformance_DeviceInfo *deviceInfo, GamePerformance_CpuInfo **cpuInfo) | 从设备性能信息GamePerformance_DeviceInfo中获取CPU性能信息GamePerformance_CpuInfo。 |
| GamePerformance_ErrorCode HMS_GamePerformance_CpuInfo_GetCpuLoadLevel (GamePerformance_CpuInfo *cpuInfo, int32_t *cpuLoadLevel) | 从GamePerformance_CpuInfo中获取CPU负载整体等级。 |
| GamePerformance_ErrorCode HMS_GamePerformance_CpuInfo_GetSingleThreadLoadLevel (GamePerformance_CpuInfo *cpuInfo, int32_t *singleThreadLoadLevel) | 从GamePerformance_CpuInfo中获取游戏最重线程的负载整体等级。 |
| GamePerformance_ErrorCode HMS_GamePerformance_DestroyDeviceInfo (GamePerformance_DeviceInfo **deviceInfo) | 当GamePerformance_DeviceInfo实例不再使用，销毁该实例。 |