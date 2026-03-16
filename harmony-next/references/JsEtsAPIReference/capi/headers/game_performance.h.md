# game_performance.h

#### 概述

声明游戏场景感知的类型及相关接口。

**库：** libgame_performance.z.so

**系统能力：** SystemCapability.GameService.GamePerformance

**起始版本：** 5.0.2(14)

**相关模块：**[GamePerformance](../../topics/misc/GamePerformance.md)

#### 汇总

#### 类型定义

名称

描述

typedef struct [GamePerformance_DeviceInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga530e1cf28aa5c4d0b355dc053ce27e80)[GamePerformance_DeviceInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga530e1cf28aa5c4d0b355dc053ce27e80)

定义设备性能信息。

typedef struct [GamePerformance_GpuInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gae85f740f82b3ca3f7ec9892d2f81a113)[GamePerformance_GpuInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gae85f740f82b3ca3f7ec9892d2f81a113)

定义GPU性能信息。

typedef struct [GamePerformance_CpuInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga5e0fa80aa26633c1b9d765340e4a262d)[GamePerformance_CpuInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga5e0fa80aa26633c1b9d765340e4a262d)

定义CPU性能信息。

typedef struct [GamePerformance_ThermalInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga6767ea8a1d76ed32db95dc0d3a265a8a)[GamePerformance_ThermalInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga6767ea8a1d76ed32db95dc0d3a265a8a)

定义温度信息。

typedef struct [GamePerformance_ThermalInfoQueryParameters](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga0e825c8963101d40a987d4057033c788)[GamePerformance_ThermalInfoQueryParameters](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga0e825c8963101d40a987d4057033c788)

定义温度信息的查询参数。

typedef struct [GamePerformance_InitParameters](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga9ba0e813bb05d37656f9973a35fa0411)[GamePerformance_InitParameters](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga9ba0e813bb05d37656f9973a35fa0411)

定义初始化参数。

typedef struct [GamePerformance_PackageInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab57ecb4bce0af8b741ef4aa069df2d87)[GamePerformance_PackageInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab57ecb4bce0af8b741ef4aa069df2d87)

定义游戏包信息。

typedef struct [GamePerformance_ConfigInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab05a6dca6b3570c3b45d74a9cb8ffdc9)[GamePerformance_ConfigInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab05a6dca6b3570c3b45d74a9cb8ffdc9)

定义游戏配置信息。

typedef struct [GamePerformance_SceneInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7)[GamePerformance_SceneInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7)

定义游戏场景信息。

typedef struct [GamePerformance_NetInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gaba275a8588101424676258ffa7217097)[GamePerformance_NetInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gaba275a8588101424676258ffa7217097)

定义游戏网络信息。

typedef struct [GamePerformance_PlayerInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga804b472fc080d73a2ce23da927ffd842)[GamePerformance_PlayerInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga804b472fc080d73a2ce23da927ffd842)

定义游戏玩家信息。

typedef enum [GamePerformance_EngineType](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab7f3d09e6dd4af1692872b6b5815af45)[GamePerformance_EngineType](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga449d5fa8c8ee0fbea9188fd345401462)

定义游戏引擎类型。

typedef enum [GamePerformance_GameType](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga9c1b6f00c4769f13c510a7a871c7afd3)[GamePerformance_GameType](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga1e1370020b763cb4cce215d955ebb78d)

定义游戏类型。

typedef enum [GamePerformance_PictureQualityLevel](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64fd3d566be9f8240d0f474d52c292dd)[GamePerformance_PictureQualityLevel](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab726f445d701d96ff647efa723ef993d)

定义画质等级。

typedef enum [GamePerformance_SceneImportanceLevel](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gaf6bbf14a7010d4e99e6c758a718a08a6)[GamePerformance_SceneImportanceLevel](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga59c720e67f9586ae4f24223be1ae3dc5)

定义游戏场景重要程度。

typedef enum [GamePerformance_CpuLevel](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga11ac456fd1b33d0b1f6220af5e5cd1ce)[GamePerformance_CpuLevel](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga4d30bee20aca3ea7082302ae7164a196)

定义CPU等级。

typedef enum [GamePerformance_GpuLevel](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga48d14f66a8d484b497157458dd13a473)[GamePerformance_GpuLevel](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga12e1ee7ac06fc6bd25a87cce66d2a632)

定义GPU等级。

typedef enum [GamePerformance_DdrLevel](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gaec1b60b592a13ea85774a4d2ec8581bb)[GamePerformance_DdrLevel](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga57b549a68edbc9c84843040beb886389)

定义DDR等级。

typedef enum [GamePerformance_NetLoad](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga517e25164876d3727c407c887943aee2)[GamePerformance_NetLoad](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga638c2b6f6d0dda3138e34869635b2dd4)

定义网络负载等级。

typedef enum [GamePerformance_ErrorCode](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316)[GamePerformance_ErrorCode](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gad952c8a450a72955d4dc24c43df7eee6)

定义错误码。

typedef enum [GamePerformance_DeviceInfoType](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga3ebb81788405856534d8fb3cd6194ca4)[GamePerformance_DeviceInfoType](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gac1d8c407b85cedf00dc6f6cf1f3ac202)

定义设备性能信息类型。

typedef void(*[GamePerformance_ThermalLevelChangedCallback](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga94e7e85a3f0ad0b495b2c525a15ebc8e)) ([GamePerformance_DeviceInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga530e1cf28aa5c4d0b355dc053ce27e80) *deviceInfo, void *userData)

[HMS_GamePerformance_RegisterThermalLevelChangedCallback](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gaa73a9464dbe4a973e7aed559835adbc6)中使用的回调函数。当温度等级改变并且温度等级小于3档时，该函数将被调用一次。当温度等级大于或等于3档时，该函数将每10秒调用一次。

#### 枚举

名称

描述

[GamePerformance_EngineType](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab7f3d09e6dd4af1692872b6b5815af45) {

GAME_PERFORMANCE_ENGINE_TYPE_UNITY = 1,

GAME_PERFORMANCE_ENGINE_TYPE_UNREAL = 2,

GAME_PERFORMANCE_ENGINE_TYPE_MESSIAH = 3,

GAME_PERFORMANCE_ENGINE_TYPE_COCOS = 4,

GAME_PERFORMANCE_ENGINE_TYPE_OTHERS = 200

}

此枚举描述引擎类型。

[GamePerformance_GameType](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga9c1b6f00c4769f13c510a7a871c7afd3) {

GAME_PERFORMANCE_GAME_TYPE_MOBA = 1,

GAME_PERFORMANCE_GAME_TYPE_RPG = 2,

GAME_PERFORMANCE_GAME_TYPE_FPS = 3,

GAME_PERFORMANCE_GAME_TYPE_FTG = 4,

GAME_PERFORMANCE_GAME_TYPE_RAC = 5,

GAME_PERFORMANCE_GAME_TYPE_OTHERS = 200

}

此枚举描述游戏类型。

[GamePerformance_PictureQualityLevel](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64fd3d566be9f8240d0f474d52c292dd) {

GAME_PERFORMANCE_PQL_SMOOTH = 1,

GAME_PERFORMANCE_PQL_BALANCED = 2,

GAME_PERFORMANCE_PQL_HD = 3,

GAME_PERFORMANCE_PQL_HDR = 4,

GAME_PERFORMANCE_PQL_UHD = 5

}

此枚举描述画质等级。

[GamePerformance_SceneImportanceLevel](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gaf6bbf14a7010d4e99e6c758a718a08a6) {

GAME_PERFORMANCE_SIL_LEVEL1 = 1,

GAME_PERFORMANCE_SIL_LEVEL2 = 2,

GAME_PERFORMANCE_SIL_LEVEL3 = 3,

GAME_PERFORMANCE_SIL_LEVEL4 = 4,

GAME_PERFORMANCE_SIL_LEVEL5 = 5

}

此枚举描述场景重要程度。

[GamePerformance_CpuLevel](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga11ac456fd1b33d0b1f6220af5e5cd1ce) {

GAME_PERFORMANCE_CPU_LEVEL_LOW = 1,

GAME_PERFORMANCE_CPU_LEVEL_MIDDLE = 2,

GAME_PERFORMANCE_CPU_LEVEL_HIGH = 3

}

此枚举描述CPU等级。

[GamePerformance_GpuLevel](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga48d14f66a8d484b497157458dd13a473) {

GAME_PERFORMANCE_GPU_LEVEL_LOW = 1,

GAME_PERFORMANCE_GPU_LEVEL_MIDDLE = 2,

GAME_PERFORMANCE_GPU_LEVEL_HIGH = 3

}

此枚举描述GPU等级。

[GamePerformance_DdrLevel](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gaec1b60b592a13ea85774a4d2ec8581bb) {

GAME_PERFORMANCE_DDR_LEVEL_LOW = 1,

GAME_PERFORMANCE_DDR_LEVEL_MIDDLE = 2,

GAME_PERFORMANCE_DDR_LEVEL_HIGH = 3

}

此枚举描述DDR等级。

[GamePerformance_NetLoad](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga517e25164876d3727c407c887943aee2) {

GAME_PERFORMANCE_NET_LOAD_LIGHT = 1,

GAME_PERFORMANCE_NET_LOAD_MODERATE = 2,

GAME_PERFORMANCE_NET_LOAD_HEAVY = 3

}

此枚举描述网络负载等级。

[GamePerformance_ErrorCode](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316) {

GAME_PERFORMANCE_SUCCESS = 0,

GAME_PERFORMANCE_PARAM_INVALID = 401,

GAME_PERFORMANCE_INTERNAL_ERROR = 1010300001,

GAME_PERFORMANCE_AUTH_FAILED = 1010300002,

GAME_PERFORMANCE_INVALID_REQUEST = 1010300003,

GAME_PERFORMANCE_PARAM_ERROR = 1010300004

}

此枚举描述错误码。

GAME_PERFORMANCE_PARAM_ERROR 从6.0.2(22)开始支持。

[GamePerformance_DeviceInfoType](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga3ebb81788405856534d8fb3cd6194ca4) {

GAME_PERFORMANCE_DEVICEINFO_TYPE_THERMAL = 0,

GAME_PERFORMANCE_DEVICEINFO_TYPE_GPU = 1,

GAME_PERFORMANCE_DEVICEINFO_TYPE_CPU = 2

}

此枚举描述设备性能信息类型。

GAME_PERFORMANCE_DEVICEINFO_TYPE_CPU 从6.0.2(22)开始支持。

#### 函数

名称

描述

**初始化（init）相关**

调用HMS_GamePerformance_Init前，必须已设置bundleName，appVersion。

[GamePerformance_ErrorCode](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316)[HMS_GamePerformance_CreateInitParameters](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga82a96cb32e0980c6650b262b268158a2) ([GamePerformance_InitParameters](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga9ba0e813bb05d37656f9973a35fa0411) **initParameters)

创建[GamePerformance_InitParameters](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga9ba0e813bb05d37656f9973a35fa0411)实例，该实例在[HMS_GamePerformance_Init](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga1045d9d8f4e7972b44ff95571afca8f9)方法中使用。

[GamePerformance_ErrorCode](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316)[HMS_GamePerformance_DestroyInitParameters](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gaef8a6ecaefc0f7ca4b8e2c88a84f5db0) ([GamePerformance_InitParameters](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga9ba0e813bb05d37656f9973a35fa0411) **initParameters)

当[GamePerformance_InitParameters](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga9ba0e813bb05d37656f9973a35fa0411)实例不再使用，销毁该实例。

[GamePerformance_ErrorCode](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316)[HMS_GamePerformance_InitParameters_SetBundleName](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga35962b201b42b841202d0986e7e80250) ([GamePerformance_InitParameters](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga9ba0e813bb05d37656f9973a35fa0411) *initParameters, const char *bundleName)

为[GamePerformance_InitParameters](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga9ba0e813bb05d37656f9973a35fa0411)实例设置包名。

[GamePerformance_ErrorCode](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316)[HMS_GamePerformance_InitParameters_SetAppVersion](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab19d551d38ea087012ba205f975ec5ed) ([GamePerformance_InitParameters](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga9ba0e813bb05d37656f9973a35fa0411) *initParameters, const char *appVersion)

为[GamePerformance_InitParameters](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga9ba0e813bb05d37656f9973a35fa0411)实例设置版本号。

[GamePerformance_ErrorCode](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316)[HMS_GamePerformance_Init](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga1045d9d8f4e7972b44ff95571afca8f9) ([GamePerformance_InitParameters](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga9ba0e813bb05d37656f9973a35fa0411) *initParameters)

初始化游戏场景感知。

**游戏包信息（PackageInfo）相关**

调用HMS_GamePerformance_UpdatePackageInfo前，必须已设置bundleName，appVersion。

[GamePerformance_ErrorCode](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316)[HMS_GamePerformance_CreatePackageInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga6b54d67769794ce6833cbecf7a0fb9ab) ([GamePerformance_PackageInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab57ecb4bce0af8b741ef4aa069df2d87) **packageInfo)

创建[GamePerformance_PackageInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab57ecb4bce0af8b741ef4aa069df2d87)实例，该实例在[HMS_GamePerformance_UpdatePackageInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga317ba7027076ce06ae73a6188bc3b129)方法中使用。

[GamePerformance_ErrorCode](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316)[HMS_GamePerformance_DestroyPackageInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga2019dcc34f428ae80868c0af612237c3) ([GamePerformance_PackageInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab57ecb4bce0af8b741ef4aa069df2d87) **packageInfo)

当[GamePerformance_PackageInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab57ecb4bce0af8b741ef4aa069df2d87)实例不再使用，销毁该实例。

[GamePerformance_ErrorCode](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316)[HMS_GamePerformance_PackageInfo_SetBundleName](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga623a88c7ea2c5eb022dd8a784e8b6661) ([GamePerformance_PackageInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab57ecb4bce0af8b741ef4aa069df2d87) *packageInfo, const char *bundleName)

为[GamePerformance_PackageInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab57ecb4bce0af8b741ef4aa069df2d87)实例设置包名。

[GamePerformance_ErrorCode](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316)[HMS_GamePerformance_PackageInfo_SetAppVersion](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga0afa327f6afed7acfc998c3f79bfeb76) ([GamePerformance_PackageInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab57ecb4bce0af8b741ef4aa069df2d87) *packageInfo, const char *appVersion)

为[GamePerformance_PackageInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab57ecb4bce0af8b741ef4aa069df2d87)实例设置版本号。

[GamePerformance_ErrorCode](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316)[HMS_GamePerformance_PackageInfo_SetEngineType](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga1436072d310ec40ddc2a85d6bafd0ee2) ([GamePerformance_PackageInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab57ecb4bce0af8b741ef4aa069df2d87) *packageInfo, const [GamePerformance_EngineType](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab7f3d09e6dd4af1692872b6b5815af45) engineType)

为[GamePerformance_PackageInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab57ecb4bce0af8b741ef4aa069df2d87)实例设置引擎类型。

[GamePerformance_ErrorCode](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316)[HMS_GamePerformance_PackageInfo_SetEngineVersion](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga73b762ef177488deecf97f04395f70d5) ([GamePerformance_PackageInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab57ecb4bce0af8b741ef4aa069df2d87) *packageInfo, const char *engineVersion)

为[GamePerformance_PackageInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab57ecb4bce0af8b741ef4aa069df2d87)实例设置引擎版本号。

[GamePerformance_ErrorCode](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316)[HMS_GamePerformance_PackageInfo_SetGameType](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gac5f6695702063b61b4f7cc885129dfe2) ([GamePerformance_PackageInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab57ecb4bce0af8b741ef4aa069df2d87) *packageInfo, const [GamePerformance_GameType](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga9c1b6f00c4769f13c510a7a871c7afd3) gameType)

为[GamePerformance_PackageInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab57ecb4bce0af8b741ef4aa069df2d87)实例设置游戏类型。

[GamePerformance_ErrorCode](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316)[HMS_GamePerformance_PackageInfo_SetVulkanSupported](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gadfbc32fbe65b9763d2cb393af8485dbb) ([GamePerformance_PackageInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab57ecb4bce0af8b741ef4aa069df2d87) *packageInfo, const bool vulkanSupported)

为[GamePerformance_PackageInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab57ecb4bce0af8b741ef4aa069df2d87)实例设置是否支持vulkan。

[GamePerformance_ErrorCode](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316)[HMS_GamePerformance_UpdatePackageInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga317ba7027076ce06ae73a6188bc3b129) ([GamePerformance_PackageInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab57ecb4bce0af8b741ef4aa069df2d87) *packageInfo)

更新游戏包信息。

**游戏配置信息（ConfigInfo）相关**

[GamePerformance_ErrorCode](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316)[HMS_GamePerformance_CreateConfigInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga2124abdf7dfed3b2c37242228a442128) ([GamePerformance_ConfigInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab05a6dca6b3570c3b45d74a9cb8ffdc9) **configInfo)

创建[GamePerformance_ConfigInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab05a6dca6b3570c3b45d74a9cb8ffdc9)实例，该实例在[HMS_GamePerformance_UpdateConfigInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga6fe77ea4f43939333c7c3b07e1204448)方法中使用。

[GamePerformance_ErrorCode](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316)[HMS_GamePerformance_DestroyConfigInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga8328d927012e4b868175ad3c192a947b) ([GamePerformance_ConfigInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab05a6dca6b3570c3b45d74a9cb8ffdc9) **configInfo)

当[GamePerformance_ConfigInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab05a6dca6b3570c3b45d74a9cb8ffdc9)实例不再使用，销毁该实例。

[GamePerformance_ErrorCode](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316)[HMS_GamePerformance_ConfigInfo_SetMaxPictureQualityLevel](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga5f85d32e8f74f4ab008abd49f1109c46) ([GamePerformance_ConfigInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab05a6dca6b3570c3b45d74a9cb8ffdc9) *configInfo, const [GamePerformance_PictureQualityLevel](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64fd3d566be9f8240d0f474d52c292dd) maxPictureQualityLevel)

为[GamePerformance_ConfigInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab05a6dca6b3570c3b45d74a9cb8ffdc9)实例设置最大画质等级。

[GamePerformance_ErrorCode](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316)[HMS_GamePerformance_ConfigInfo_SetCurrentPictureQualityLevel](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gad44e9925a145ab621f4d8ff348de4034) ([GamePerformance_ConfigInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab05a6dca6b3570c3b45d74a9cb8ffdc9) *configInfo, const [GamePerformance_PictureQualityLevel](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64fd3d566be9f8240d0f474d52c292dd) currentPictureQualityLevel)

为[GamePerformance_ConfigInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab05a6dca6b3570c3b45d74a9cb8ffdc9)实例设置当前画质等级。

[GamePerformance_ErrorCode](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316)[HMS_GamePerformance_ConfigInfo_SetMaxFrameRate](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga6665850e826d430bba7525351ef2df70) ([GamePerformance_ConfigInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab05a6dca6b3570c3b45d74a9cb8ffdc9) *configInfo, const int64_t maxFrameRate)

为[GamePerformance_ConfigInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab05a6dca6b3570c3b45d74a9cb8ffdc9)实例设置最大帧率。

[GamePerformance_ErrorCode](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316)[HMS_GamePerformance_ConfigInfo_SetCurrentFrameRate](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga89845a005ea8f0a5069ef2563f55936e) ([GamePerformance_ConfigInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab05a6dca6b3570c3b45d74a9cb8ffdc9) *configInfo, const int64_t currentFrameRate)

为[GamePerformance_ConfigInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab05a6dca6b3570c3b45d74a9cb8ffdc9)实例设置当前帧率。

[GamePerformance_ErrorCode](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316)[HMS_GamePerformance_ConfigInfo_SetMaxResolution](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gad34b019dfa3a973512c7157dcba92ad1) ([GamePerformance_ConfigInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab05a6dca6b3570c3b45d74a9cb8ffdc9) *configInfo, const char *maxResolution)

为[GamePerformance_ConfigInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab05a6dca6b3570c3b45d74a9cb8ffdc9)实例设置最大分辨率。

[GamePerformance_ErrorCode](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316)[HMS_GamePerformance_ConfigInfo_SetCurrentResolution](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga9bee7c2052d81a0dd6c6f93ce57ddc1f) ([GamePerformance_ConfigInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab05a6dca6b3570c3b45d74a9cb8ffdc9) *configInfo, const char *currentResolution)

为[GamePerformance_ConfigInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab05a6dca6b3570c3b45d74a9cb8ffdc9)实例设置当前分辨率。

[GamePerformance_ErrorCode](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316)[HMS_GamePerformance_ConfigInfo_SetAntiAliasingEnabled](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga5657a6e00ba9e08803a201a8d0c1cecd) ([GamePerformance_ConfigInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab05a6dca6b3570c3b45d74a9cb8ffdc9) *configInfo, const bool antiAliasingEnabled)

为[GamePerformance_ConfigInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab05a6dca6b3570c3b45d74a9cb8ffdc9)实例设置是否开启抗锯齿。

[GamePerformance_ErrorCode](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316)[HMS_GamePerformance_ConfigInfo_SetShadowEnabled](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga1beebb2eabcea33e37de8015ac29ef9c) ([GamePerformance_ConfigInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab05a6dca6b3570c3b45d74a9cb8ffdc9) *configInfo, const bool shadowEnabled)

为[GamePerformance_ConfigInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab05a6dca6b3570c3b45d74a9cb8ffdc9)实例设置是否开启阴影。

[GamePerformance_ErrorCode](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316)[HMS_GamePerformance_ConfigInfo_SetMultithreadingEnabled](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab69ed9d7e95fe067d618514a6472c2b3) ([GamePerformance_ConfigInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab05a6dca6b3570c3b45d74a9cb8ffdc9) *configInfo, const bool multithreadingEnabled)

为[GamePerformance_ConfigInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab05a6dca6b3570c3b45d74a9cb8ffdc9)实例设置开启多线程。

[GamePerformance_ErrorCode](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316)[HMS_GamePerformance_ConfigInfo_SetParticleEnabled](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga808ed7b13bc8ed4fd97267a65c8f4469) ([GamePerformance_ConfigInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab05a6dca6b3570c3b45d74a9cb8ffdc9) *configInfo, const bool particleEnabled)

为[GamePerformance_ConfigInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab05a6dca6b3570c3b45d74a9cb8ffdc9)实例设置粒子效果。

[GamePerformance_ErrorCode](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316)[HMS_GamePerformance_ConfigInfo_SetHdModeEnabled](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga5ef09e013a67def087e5f6b5442ff0b0) ([GamePerformance_ConfigInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab05a6dca6b3570c3b45d74a9cb8ffdc9) *configInfo, const bool hdModeEnabled)

为[GamePerformance_ConfigInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab05a6dca6b3570c3b45d74a9cb8ffdc9)实例设置开启高清模式。

[GamePerformance_ErrorCode](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316)[HMS_GamePerformance_UpdateConfigInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga6fe77ea4f43939333c7c3b07e1204448) ([GamePerformance_ConfigInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab05a6dca6b3570c3b45d74a9cb8ffdc9) *configInfo)

更新游戏配置信息。

**游戏场景信息（SceneInfo）相关**

调用HMS_GamePerformance_UpdateSceneInfo前，必须已设置sceneID，importanceLevel。

[GamePerformance_ErrorCode](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316)[HMS_GamePerformance_CreateSceneInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga20ba3d28237372a1f44652f50d0850c4) ([GamePerformance_SceneInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7) **sceneInfo)

创建[GamePerformance_SceneInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7)实例，该实例在[HMS_GamePerformance_UpdateSceneInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gad9504bae5e5b570e55bdf7f84a7a05bf)方法中使用。

[GamePerformance_ErrorCode](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316)[HMS_GamePerformance_DestroySceneInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gadc5f2c4b6b7258830736fb194d06bdd8) ([GamePerformance_SceneInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7) **sceneInfo)

当[GamePerformance_SceneInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7)实例不再使用，销毁该实例。

[GamePerformance_ErrorCode](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316)[HMS_GamePerformance_SceneInfo_SetSceneID](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gaaf792159ff58c372c80106a3e050e7bc) ([GamePerformance_SceneInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7) *sceneInfo, const int64_t sceneID)

为[GamePerformance_SceneInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7)实例设置场景ID。

[GamePerformance_ErrorCode](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316)[HMS_GamePerformance_SceneInfo_SetDescription](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga32193247c7f59a29920b5ec084a89a6c) ([GamePerformance_SceneInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7) *sceneInfo, const char *description)

为[GamePerformance_SceneInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7)实例设置场景描述。

[GamePerformance_ErrorCode](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316)[HMS_GamePerformance_SceneInfo_SetSubSceneID](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gaf66ab2b453b1f9e5df8173f839490540) ([GamePerformance_SceneInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7) *sceneInfo, const char *subSceneID)

为[GamePerformance_SceneInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7)实例设置子场景ID。

[GamePerformance_ErrorCode](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316)[HMS_GamePerformance_SceneInfo_SetSubDescription](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga1d6ed7ffa24f5002ffbd799877467056) ([GamePerformance_SceneInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7) *sceneInfo, const char *subDescription)

为[GamePerformance_SceneInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7)实例设置子场景描述。

[GamePerformance_ErrorCode](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316)[HMS_GamePerformance_SceneInfo_SetImportanceLevel](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga5a7748133e83c9aebaa439e0d97fe742) ([GamePerformance_SceneInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7) *sceneInfo, const [GamePerformance_SceneImportanceLevel](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gaf6bbf14a7010d4e99e6c758a718a08a6) importanceLevel)

为[GamePerformance_SceneInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7)实例设置场景重要程度。

[GamePerformance_ErrorCode](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316)[HMS_GamePerformance_SceneInfo_SetSceneFrequency](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga3743a3ad2a364d6b039b2dbc1213f04a) ([GamePerformance_SceneInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7) *sceneInfo, const int64_t sceneFrequency)

为[GamePerformance_SceneInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7)实例设置该场景在一局游戏中出现的次数。

[GamePerformance_ErrorCode](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316)[HMS_GamePerformance_SceneInfo_SetSceneTime](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gaa7d8eab6076c00e220da385a51016847) ([GamePerformance_SceneInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7) *sceneInfo, const int64_t sceneTime)

为[GamePerformance_SceneInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7)实例设置场景持续时间。

[GamePerformance_ErrorCode](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316)[HMS_GamePerformance_SceneInfo_SetRecommendedCpuLevel](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga423176ac542a8058fd4bdc31e19e49fb) ([GamePerformance_SceneInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7) *sceneInfo, const [GamePerformance_CpuLevel](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga11ac456fd1b33d0b1f6220af5e5cd1ce) recommendedCpuLevel)

为[GamePerformance_SceneInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7)实例设置推荐的CPU等级。

[GamePerformance_ErrorCode](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316)[HMS_GamePerformance_SceneInfo_SetRecommendedGpuLevel](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gaf7bb4de842d1045434417997abb12365) ([GamePerformance_SceneInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7) *sceneInfo, const [GamePerformance_GpuLevel](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga48d14f66a8d484b497157458dd13a473) recommendedGpuLevel)

为[GamePerformance_SceneInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7)实例设置推荐的GPU等级。

[GamePerformance_ErrorCode](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316)[HMS_GamePerformance_SceneInfo_SetRecommendedDdrLevel](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga919d39c5eaa6e8e0a1f88c42f4d55264) ([GamePerformance_SceneInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7) *sceneInfo, const [GamePerformance_DdrLevel](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gaec1b60b592a13ea85774a4d2ec8581bb) recommendedDdrLevel)

为[GamePerformance_SceneInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7)实例设置推荐的DDR等级。

[GamePerformance_ErrorCode](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316)[HMS_GamePerformance_SceneInfo_SetMaxFrameRate](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gad672cb46e420b0cee29da39d4009a7c9) ([GamePerformance_SceneInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7) *sceneInfo, const int64_t maxFrameRate)

为[GamePerformance_SceneInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7)实例设置场景最大帧率。

[GamePerformance_ErrorCode](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316)[HMS_GamePerformance_SceneInfo_SetCurrentFrameRate](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga70f297a098b963e0216cf1fc0b2d3075) ([GamePerformance_SceneInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7) *sceneInfo, const int64_t currentFrameRate)

为[GamePerformance_SceneInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7)实例设置场景当前帧率。

[GamePerformance_ErrorCode](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316)[HMS_GamePerformance_SceneInfo_SetKeyThread](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gaa41913e398bd82a136497889c4c40435) ([GamePerformance_SceneInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7) *sceneInfo, const char *keyThread)

为[GamePerformance_SceneInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7)实例设置关键线程。

[GamePerformance_ErrorCode](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316)[HMS_GamePerformance_SceneInfo_SetDrawCallCount](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga8504590e1f52eba1ab01f9e29d5344e3) ([GamePerformance_SceneInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7) *sceneInfo, const int64_t drawCallCount)

为[GamePerformance_SceneInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7)实例设置每帧的平均Drawcall数。

[GamePerformance_ErrorCode](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316)[HMS_GamePerformance_SceneInfo_SetVertexCount](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga5a10d96f46fbc5353d4c077970b5b3b7) ([GamePerformance_SceneInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7) *sceneInfo, const int64_t vertexCount)

为[GamePerformance_SceneInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7)实例设置每帧的平均模型顶点数。

[GamePerformance_ErrorCode](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316)[HMS_GamePerformance_SceneInfo_SetTriangleCount](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga98ba98ee175a97bc9b40dfb4576194ea) ([GamePerformance_SceneInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7) *sceneInfo, const int64_t triangleCount)

为[GamePerformance_SceneInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7)实例设置每帧的平均模型三角形数。

[GamePerformance_ErrorCode](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316)[HMS_GamePerformance_SceneInfo_SetShaderCount](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gacc04bf99a463910cfdf3e96e0d1f7168) ([GamePerformance_SceneInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7) *sceneInfo, const int64_t shaderCount)

为[GamePerformance_SceneInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7)实例设置每帧的平均shader数量。

[GamePerformance_ErrorCode](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316)[HMS_GamePerformance_SceneInfo_SetTextureCount](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gac374255a0c99f721ff7227e2c9a599d3) ([GamePerformance_SceneInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7) *sceneInfo, const int64_t textureCount)

为[GamePerformance_SceneInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7)实例设置每帧的平均纹理数量。

[GamePerformance_ErrorCode](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316)[HMS_GamePerformance_SceneInfo_SetMeshCount](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga00ab8ad16a928499daf8359fed8343b8) ([GamePerformance_SceneInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7) *sceneInfo, const int64_t meshCount)

为[GamePerformance_SceneInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7)实例设置每帧的平均mesh数量。

[GamePerformance_ErrorCode](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316)[HMS_GamePerformance_SceneInfo_SetChannelCount](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga4d6f34ef3b653c79c110c0fd35a5cca6) ([GamePerformance_SceneInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7) *sceneInfo, const int64_t channelCount)

为[GamePerformance_SceneInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7)实例设置每帧渲染的通道数。

[GamePerformance_ErrorCode](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316)[HMS_GamePerformance_SceneInfo_SetParticipantCount](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga3a3eaf50d555e6539c0f61543bc7898e) ([GamePerformance_SceneInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7) *sceneInfo, const int64_t participantCount)

为[GamePerformance_SceneInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7)实例设置场景下的同屏人数。

[GamePerformance_ErrorCode](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316)[HMS_GamePerformance_UpdateSceneInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gad9504bae5e5b570e55bdf7f84a7a05bf) ([GamePerformance_SceneInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga64047fc82c0783c507e34e10c735e4d7) *sceneInfo)

更新游戏场景信息。

**游戏网络信息（NetInfo）相关**

调用HMS_GamePerformance_UpdateNetInfo前必须已设置totalLatency。

[GamePerformance_ErrorCode](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316)[HMS_GamePerformance_CreateNetInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga7c2084205b1c6402f6c7697aa93ea08e) ([GamePerformance_NetInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gaba275a8588101424676258ffa7217097) **netInfo)

创建[GamePerformance_NetInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gaba275a8588101424676258ffa7217097)实例，该实例在[HMS_GamePerformance_UpdateNetInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga29ff530f9f37560359fdd0d28ba6275b)方法中使用。

[GamePerformance_ErrorCode](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316)[HMS_GamePerformance_DestroyNetInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga7e97470d2e305c3777438ba7cc524cac) ([GamePerformance_NetInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gaba275a8588101424676258ffa7217097) **netInfo)

当[GamePerformance_NetInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gaba275a8588101424676258ffa7217097)实例不再使用，销毁该实例。

[GamePerformance_ErrorCode](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316)[HMS_GamePerformance_NetInfo_SetTotalLatency](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gaf2b2757c599992d8eb90767513abef59) ([GamePerformance_NetInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gaba275a8588101424676258ffa7217097) *netInfo, const int64_t total)

为[GamePerformance_NetInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gaba275a8588101424676258ffa7217097)实例设置总网络时延。

[GamePerformance_ErrorCode](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316)[HMS_GamePerformance_NetInfo_SetUplinkLatency](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gaa0876f5a71061d68f084d40d2b1039e2) ([GamePerformance_NetInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gaba275a8588101424676258ffa7217097) *netInfo, const int64_t up)

为[GamePerformance_NetInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gaba275a8588101424676258ffa7217097)实例设置上行网络时延。

[GamePerformance_ErrorCode](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316)[HMS_GamePerformance_NetInfo_SetDownlinkLatency](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga1edfa8aa64d9773b3b768e1653690479) ([GamePerformance_NetInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gaba275a8588101424676258ffa7217097) *netInfo, const int64_t down)

为[GamePerformance_NetInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gaba275a8588101424676258ffa7217097)实例设置下行网络时延。

[GamePerformance_ErrorCode](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316)[HMS_GamePerformance_NetInfo_SetServerLatency](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga5920ded727e6ca21760b82d5586064b9) ([GamePerformance_NetInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gaba275a8588101424676258ffa7217097) *netInfo, const int64_t server)

为[GamePerformance_NetInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gaba275a8588101424676258ffa7217097)实例设置服务器网络时延。

[GamePerformance_ErrorCode](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316)[HMS_GamePerformance_NetInfo_SetNetLoad](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga74aab7c053e2bf62aacef57ea223aa28) ([GamePerformance_NetInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gaba275a8588101424676258ffa7217097) *netInfo, const [GamePerformance_NetLoad](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga517e25164876d3727c407c887943aee2) netLoad)

为[GamePerformance_NetInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gaba275a8588101424676258ffa7217097)实例设置网络负载。

[GamePerformance_ErrorCode](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316)[HMS_GamePerformance_UpdateNetInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga29ff530f9f37560359fdd0d28ba6275b) ([GamePerformance_NetInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gaba275a8588101424676258ffa7217097) *netInfo)

更新游戏网络信息。

**游戏玩家信息（PlayerInfo）相关**

gamePlayerId、teamPlayerId和thirdOpenId不能同时为空。

[GamePerformance_ErrorCode](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316)[HMS_GamePerformance_CreatePlayerInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga97925740bdc7df3aefbd482304294208) ([GamePerformance_PlayerInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga804b472fc080d73a2ce23da927ffd842) **playerInfo)

创建[GamePerformance_PlayerInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga804b472fc080d73a2ce23da927ffd842)实例，该实例在[HMS_GamePerformance_UpdatePlayerInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga71c7be26b9531af9bcd807e3255c4e6f)方法中使用。

[GamePerformance_ErrorCode](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316)[HMS_GamePerformance_DestroyPlayerInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga42254ab6d5c9a8ec61f512d1e2903256) ([GamePerformance_PlayerInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga804b472fc080d73a2ce23da927ffd842) **playerInfo)

当[GamePerformance_PlayerInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga804b472fc080d73a2ce23da927ffd842)实例不再使用，销毁该实例。

[GamePerformance_ErrorCode](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316)[HMS_GamePerformance_PlayerInfo_SetGamePlayerId](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gaccabd2811fc0e84e95a50219b34f1814) ([GamePerformance_PlayerInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga804b472fc080d73a2ce23da927ffd842) *playerInfo, const char *gamePlayerId)

为[GamePerformance_PlayerInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga804b472fc080d73a2ce23da927ffd842)实例设置游戏玩家ID。

[GamePerformance_ErrorCode](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316)[HMS_GamePerformance_PlayerInfo_SetTeamPlayerId](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gaa5068c2f80ffc184cbebb03f22ece595) ([GamePerformance_PlayerInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga804b472fc080d73a2ce23da927ffd842) *playerInfo, const char *teamPlayerId)

为[GamePerformance_PlayerInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga804b472fc080d73a2ce23da927ffd842)实例设置团队玩家ID。

[GamePerformance_ErrorCode](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316)[HMS_GamePerformance_PlayerInfo_SetThirdOpenId](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga875a2f1dad9091927ada365f6e9b6d5d) ([GamePerformance_PlayerInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga804b472fc080d73a2ce23da927ffd842) *playerInfo, const char *thirdOpenId)

为[GamePerformance_PlayerInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga804b472fc080d73a2ce23da927ffd842)实例设置游戏官方账号。

[GamePerformance_ErrorCode](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316)[HMS_GamePerformance_UpdatePlayerInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga71c7be26b9531af9bcd807e3255c4e6f) ([GamePerformance_PlayerInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga804b472fc080d73a2ce23da927ffd842) *playerInfo)

更新游戏玩家信息。

**订阅相关**

[GamePerformance_ErrorCode](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316)[HMS_GamePerformance_RegisterThermalLevelChangedCallback](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gaa73a9464dbe4a973e7aed559835adbc6) ([GamePerformance_DeviceInfoType](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga3ebb81788405856534d8fb3cd6194ca4) *types[], size_t size, [GamePerformance_ThermalLevelChangedCallback](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga94e7e85a3f0ad0b495b2c525a15ebc8e) callback, void *userData)

订阅温度变化事件，注册温度变化回调，当达到触发点时，将调用回调函数。

[GamePerformance_ErrorCode](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316)[HMS_GamePerformance_UnregisterThermalLevelChangedCallback](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga306734f0bee9af7697b5fbfa19bafec0) ([GamePerformance_ThermalLevelChangedCallback](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga94e7e85a3f0ad0b495b2c525a15ebc8e) callback)

取消注册指定温度变化回调。

[GamePerformance_ErrorCode](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316)[HMS_GamePerformance_UnregisterAllThermalLevelChangedCallbacks](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga0f2cf9152a9421d00bb0c03683b3f57d) (void)

取消注册所有温度变化回调。

**查询温度信息**

[GamePerformance_ErrorCode](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316)[HMS_GamePerformance_CreateThermalInfoQueryParameters](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gad3e60ec2d47a5068206bc3e1f217acc2) ([GamePerformance_ThermalInfoQueryParameters](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga0e825c8963101d40a987d4057033c788) **parameters)

创建[GamePerformance_ThermalInfoQueryParameters](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga0e825c8963101d40a987d4057033c788)实例，该实例在[HMS_GamePerformance_QueryThermalInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab7cb47e0dc3cce1169a8104827f7edb7)方法中使用。

[GamePerformance_ErrorCode](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316)[HMS_GamePerformance_DestroyThermalInfoQueryParameters](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga6b9314f647ed520b11b9dfa4fbc40351) ([GamePerformance_ThermalInfoQueryParameters](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga0e825c8963101d40a987d4057033c788) **parameters)

当[GamePerformance_ThermalInfoQueryParameters](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga0e825c8963101d40a987d4057033c788)实例不再使用，销毁该实例。

[GamePerformance_ErrorCode](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316)[HMS_GamePerformance_ThermalInfoQueryParameters_SetNeedsPrediction](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga7ce2e82b511a0158d93d2ee147536ee7) ([GamePerformance_ThermalInfoQueryParameters](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga0e825c8963101d40a987d4057033c788) *parameters, const bool needsPrediction)

为[GamePerformance_ThermalInfoQueryParameters](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga0e825c8963101d40a987d4057033c788)实例设置是否需要预测温升趋势。

[GamePerformance_ErrorCode](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316)[HMS_GamePerformance_ThermalInfoQueryParameters_SetTargetThermalLevel](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga5cb94581ca23d465933e9316fdb0605d) ([GamePerformance_ThermalInfoQueryParameters](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga0e825c8963101d40a987d4057033c788) *parameters, const int32_t targetThermalLevel)

为[GamePerformance_ThermalInfoQueryParameters](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga0e825c8963101d40a987d4057033c788)实例设置预测温升趋势的目标温度等级。

[GamePerformance_ErrorCode](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316)[HMS_GamePerformance_QueryThermalInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab7cb47e0dc3cce1169a8104827f7edb7) ([GamePerformance_ThermalInfoQueryParameters](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga0e825c8963101d40a987d4057033c788) *parameters，[GamePerformance_ThermalInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga6767ea8a1d76ed32db95dc0d3a265a8a) **thermalInfo)

查询温度信息。

[GamePerformance_ErrorCode](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316)[HMS_GamePerformance_DestroyThermalInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gacc640a4e15fe9cab1f8bccb652d77e59) ([GamePerformance_ThermalInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga6767ea8a1d76ed32db95dc0d3a265a8a) **thermalInfo)

当[GamePerformance_ThermalInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga6767ea8a1d76ed32db95dc0d3a265a8a)实例不再使用，销毁该实例。

**查询GPU性能信息**

[GamePerformance_ErrorCode](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316)[HMS_GamePerformance_QueryGpuInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga93f67c2befdb52f4b59893a7a300f292) ([GamePerformance_GpuInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gae85f740f82b3ca3f7ec9892d2f81a113) **gpuInfo)

查询GPU性能信息。

[GamePerformance_ErrorCode](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316)[HMS_GamePerformance_DestroyGpuInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga249433eea6a463cb2401e7bbbbcd19dd) ([GamePerformance_GpuInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gae85f740f82b3ca3f7ec9892d2f81a113) **gpuInfo)

当[GamePerformance_GpuInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gae85f740f82b3ca3f7ec9892d2f81a113)实例不再使用，销毁该实例。

**查询CPU性能信息**

[GamePerformance_ErrorCode](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316)[HMS_GamePerformance_QueryCpuInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gad59832ffd2679db7b1fa8310f586531f) ([GamePerformance_CpuInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga5e0fa80aa26633c1b9d765340e4a262d) **cpuInfo)

查询CPU性能信息。

[GamePerformance_ErrorCode](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316)[HMS_GamePerformance_DestroyCpuInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga6e76026d1a4c34c4bf983136e0a21734) ([GamePerformance_CpuInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga5e0fa80aa26633c1b9d765340e4a262d) **cpuInfo)

当[GamePerformance_CpuInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga5e0fa80aa26633c1b9d765340e4a262d)实例不再使用，销毁该实例。

**解析温度信息**

[GamePerformance_ErrorCode](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316)[HMS_GamePerformance_DeviceInfo_GetThermalInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga233f517841cc5ab435a1e4fa8cd1d2de) ([GamePerformance_DeviceInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga530e1cf28aa5c4d0b355dc053ce27e80) *deviceInfo, [GamePerformance_ThermalInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga6767ea8a1d76ed32db95dc0d3a265a8a) **thermalInfo)

从设备性能信息[GamePerformance_DeviceInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga530e1cf28aa5c4d0b355dc053ce27e80)中获取温度信息[GamePerformance_ThermalInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga6767ea8a1d76ed32db95dc0d3a265a8a)。

[GamePerformance_ErrorCode](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316)[HMS_GamePerformance_ThermalInfo_GetThermalMargin](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gaf64ba82ad7342aeef688f5f515e86765) ([GamePerformance_ThermalInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga6767ea8a1d76ed32db95dc0d3a265a8a) *thermalInfo, int32_t *thermalMargin)

从温度信息[GamePerformance_ThermalInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga6767ea8a1d76ed32db95dc0d3a265a8a)中获取温度时间裕量。

[GamePerformance_ErrorCode](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316)[HMS_GamePerformance_ThermalInfo_GetThermalTrend](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga4e0b7380232ea2120f017cf717d66f5f) ([GamePerformance_ThermalInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga6767ea8a1d76ed32db95dc0d3a265a8a) *thermalInfo, int32_t *thermalTrend)

从[GamePerformance_ThermalInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga6767ea8a1d76ed32db95dc0d3a265a8a)中获取温升趋势。

[GamePerformance_ErrorCode](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316)[HMS_GamePerformance_ThermalInfo_GetThermalLevel](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga36713ebcb8a94fd99772965437c18b7f) ([GamePerformance_ThermalInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga6767ea8a1d76ed32db95dc0d3a265a8a) *thermalInfo, int32_t *thermalLevel)

从[GamePerformance_ThermalInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga6767ea8a1d76ed32db95dc0d3a265a8a)中获取温度等级。

[GamePerformance_ErrorCode](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316)[HMS_GamePerformance_ThermalInfo_GetRecommendNormalizedCurrent](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gaf0a4a9c0d97ecdc55f44bdbe4560b10b) ([GamePerformance_ThermalInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga6767ea8a1d76ed32db95dc0d3a265a8a) *thermalInfo, int32_t *recommendCurrent)

从[GamePerformance_ThermalInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga6767ea8a1d76ed32db95dc0d3a265a8a)中获取系统建议的工作电流。若当前的工作电流高于此值，温升趋势thermalTrend会大于0，设备有发烫风险。

[GamePerformance_ErrorCode](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316)[HMS_GamePerformance_ThermalInfo_GetNowNormalizedCurrent](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gaa8968228efdefebe9ceb1aeb47ca2005) ([GamePerformance_ThermalInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga6767ea8a1d76ed32db95dc0d3a265a8a) *thermalInfo, int32_t *nowCurrent)

从[GamePerformance_ThermalInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga6767ea8a1d76ed32db95dc0d3a265a8a)中获取当前的工作电流。

[GamePerformance_ErrorCode](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316)[HMS_GamePerformance_ThermalInfo_GetRecommendMaxNormalizedCurrent](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga273f8d969801ef92a8b201b48b66d5dd) ([GamePerformance_ThermalInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga6767ea8a1d76ed32db95dc0d3a265a8a) *thermalInfo, int32_t *recommendMaxCurrent)

从[GamePerformance_ThermalInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga6767ea8a1d76ed32db95dc0d3a265a8a)中获取系统建议的最大工作电流。若当前的工作电流高于此值，设备会立即发烫。

**解析GPU性能信息**

[GamePerformance_ErrorCode](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316)[HMS_GamePerformance_DeviceInfo_GetGpuInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga028805183830f3638fb9b122a934d30a) ([GamePerformance_DeviceInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga530e1cf28aa5c4d0b355dc053ce27e80) *deviceInfo, [GamePerformance_GpuInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gae85f740f82b3ca3f7ec9892d2f81a113) **gpuInfo)

从设备性能信息[GamePerformance_DeviceInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga530e1cf28aa5c4d0b355dc053ce27e80)中获取GPU性能信息[GamePerformance_GpuInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gae85f740f82b3ca3f7ec9892d2f81a113)。

[GamePerformance_ErrorCode](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316)[HMS_GamePerformance_GpuInfo_GetGpuLoadLevel](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga2542ab4c2a7a8ea411f5ca78236f3057) ([GamePerformance_GpuInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gae85f740f82b3ca3f7ec9892d2f81a113) *gpuInfo, int32_t *gpuLoadLevel)

从[GamePerformance_GpuInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gae85f740f82b3ca3f7ec9892d2f81a113)中获取GPU负载信息。

[GamePerformance_ErrorCode](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316)[HMS_GamePerformance_GpuInfo_GetVertexLoadLevel](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gab2c0f4d08ce347fc2ce57cd4f75a207d) ([GamePerformance_GpuInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gae85f740f82b3ca3f7ec9892d2f81a113) *gpuInfo, int32_t *vertexLoadLevel)

从[GamePerformance_GpuInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gae85f740f82b3ca3f7ec9892d2f81a113)中获取GPU顶点处理负载等级。

[GamePerformance_ErrorCode](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316)[HMS_GamePerformance_GpuInfo_GetFragmentLoadLevel](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga9ed72dbe4214471b0c62888e220c535b) ([GamePerformance_GpuInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gae85f740f82b3ca3f7ec9892d2f81a113) *gpuInfo, int32_t *fragmentLoadLevel)

从[GamePerformance_GpuInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gae85f740f82b3ca3f7ec9892d2f81a113)中获取GPU片元处理负载等级。

[GamePerformance_ErrorCode](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316)[HMS_GamePerformance_GpuInfo_GetTextureLoadLevel](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga0b690f0f661dcc5b552e1c3b0a6c48b0) ([GamePerformance_GpuInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gae85f740f82b3ca3f7ec9892d2f81a113) *gpuInfo, int32_t *textureLoadLevel)

从[GamePerformance_GpuInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gae85f740f82b3ca3f7ec9892d2f81a113)中获取GPU纹理处理负载等级。

[GamePerformance_ErrorCode](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316)[HMS_GamePerformance_GpuInfo_GetBandwidthLoadLevel](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga798a410d53057a8735c342c41066e286) ([GamePerformance_GpuInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gae85f740f82b3ca3f7ec9892d2f81a113) *gpuInfo, int32_t *bandwidthLoadLevel)

从[GamePerformance_GpuInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gae85f740f82b3ca3f7ec9892d2f81a113)中获取GPU带宽负载等级。

[GamePerformance_ErrorCode](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316)[HMS_GamePerformance_GpuInfo_GetCurrentFrequency](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga54d57643697d513fb1d2f94fa5d01633) ([GamePerformance_GpuInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gae85f740f82b3ca3f7ec9892d2f81a113) *gpuInfo, int32_t *currentFrequency)

从[GamePerformance_GpuInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gae85f740f82b3ca3f7ec9892d2f81a113)中获取GPU频点信息。

**解析CPU性能信息**

[GamePerformance_ErrorCode](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316)[HMS_GamePerformance_DeviceInfo_GetCpuInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga2526a18580b2c5ad497017bf05adc4da) ([GamePerformance_DeviceInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga530e1cf28aa5c4d0b355dc053ce27e80) *deviceInfo, [GamePerformance_CpuInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga5e0fa80aa26633c1b9d765340e4a262d) **cpuInfo)

从设备性能信息[GamePerformance_DeviceInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga530e1cf28aa5c4d0b355dc053ce27e80)中获取CPU性能信息[GamePerformance_CpuInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga5e0fa80aa26633c1b9d765340e4a262d)。

[GamePerformance_ErrorCode](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316)[HMS_GamePerformance_CpuInfo_GetCpuLoadLevel](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga2f7d2cbc801dc60873bca2664f521ccb) ([GamePerformance_CpuInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga5e0fa80aa26633c1b9d765340e4a262d) *cpuInfo, int32_t *cpuLoadLevel)

从[GamePerformance_CpuInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga5e0fa80aa26633c1b9d765340e4a262d)中获取CPU负载整体等级。

[GamePerformance_ErrorCode](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316)[HMS_GamePerformance_CpuInfo_GetSingleThreadLoadLevel](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gac323aa2708efd9224133e61fb157a27f) ([GamePerformance_CpuInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga5e0fa80aa26633c1b9d765340e4a262d) *cpuInfo, int32_t *singleThreadLoadLevel)

从[GamePerformance_CpuInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga5e0fa80aa26633c1b9d765340e4a262d)中获取游戏最重线程的负载整体等级。

**设备性能信息（DeviceInfo）相关**

[GamePerformance_ErrorCode](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga615243fda2406a6f9cd3a406874b6316)[HMS_GamePerformance_DestroyDeviceInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__gaf8031fd101ee970aa0339aed14d4507e) ([GamePerformance_DeviceInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga530e1cf28aa5c4d0b355dc053ce27e80) **deviceInfo)

当[GamePerformance_DeviceInfo](../../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga530e1cf28aa5c4d0b355dc053ce27e80)实例不再使用，销毁该实例。