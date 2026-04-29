# network_boost_quality.h

**概述**

声明用于网络质量模块的API。提供基本的函数、结构体和const定义。

库： libnetwork_boost.so

系统能力： SystemCapability.Communication.NetworkBoost.Core

起始版本： 5.1.0(18)

相关模块： [NetworkBoost](NetworkBoost.md)

**汇总**

**结构体**

| 名称 | 描述 |
| --- | --- |
| struct NetworkBoost_NetworkQos | 网络质量回调信息。 |
| struct NetworkBoost_NetworkQosArray | 网络质量变化的详细信息。 |
| struct NetworkBoost_WeakSignalPrediction | 弱信号预测相关信息。 |
| struct NetworkBoost_NetworkScene | 网络场景状态变更回调信息。 |

**宏定义**

| 名称 | 描述 |
| --- | --- |
| NETBOOST_MAX_PATH_NUM 4 | 网络质量变化的最大路径数量。 |
| NB_BPS 1 | 1bps |
| NB_KBPS 1000 | 1kbps |
| NB_MBPS 1000000 | 1mbps |
| NB_GBPS 1000000000 | 1gbps |
| NB_TBPS 1000000000000 | 1tbps，请使用uint64_t类型来避免溢出。 |

**类型定义**

| 名称 | 描述 |
| --- | --- |
| typedef enum NetworkBoost_RecommendedAction NetworkBoost_RecommendedAction | 应用数传策略建议。 |
| typedef enum NetworkBoost_PathType NetworkBoost_PathType | 数据路径类型，枚举值。 |
| typedef enum NetworkBoost_Scene NetworkBoost_Scene | 网络场景类型。 |
| typedef enum NetworkBoost_ServiceType NetworkBoost_ServiceType | 应用业务类型。 |
| typedef enum NetworkBoost_QoeType NetworkBoost_QoeType | 应用体验类型。 |
| typedef struct NetworkBoost_NetworkQos NetworkBoost_NetworkQos | 网络质量回调信息。 |
| typedef struct NetworkBoost_NetworkQosArray NetworkBoost_NetworkQosArray | 网络质量变化的详细信息。 |
| typedef struct NetworkBoost_WeakSignalPrediction NetworkBoost_WeakSignalPrediction | 弱信号预测相关信息。 |
| typedef struct NetworkBoost_NetworkScene NetworkBoost_NetworkScene | 网络场景状态变更回调信息。 |
| typedef void(* HMS_NetworkBoost_NetQosChange) (NetworkBoost_NetworkQosArray *networkQosArray) | 网络质量变更回调。 |
| typedef void(* HMS_NetworkBoost_NetSceneChange) (NetworkBoost_NetworkScene *networkScene) | 网络场景状态变更回调。 |

**枚举**

| 名称 | 描述 |
| --- | --- |
| NetworkBoost_RecommendedAction { NB_ACTION_DO_CACHING = 0, NB_ACTION_SUSPEND_DATA = 1, NB_ACTION_DECREASE_DATA = 2, NB_ACTION_INCREASE_DATA = 3, NB_ACTION_KEEP_DATA = 4 } | 应用数传策略建议。 |
| NetworkBoost_PathType { NB_PATH_CELLULAR_PRIMARY = 0, NB_PATH_CELLULAR_SECONDARY = 1, NB_PATH_WIFI_PRIMARY = 2, NB_PATH_WIFI_SECONDARY = 3 } | 数据路径类型，枚举值。 |
| NetworkBoost_Scene { NB_SCENE_NORMAL = 0, NB_SCENE_CONGESTION = 1, NB_SCENE_FREQUENT_HANDOVER = 2, NB_SCENE_WEAK_SIGNAL = 3 } | 网络场景类型。 |
| NetworkBoost_ServiceType { NB_SERVICE_DEFAULT = 0, NB_SERVICE_BACKGROUND = 1, NB_SERVICE_REAL_TIME_VOICE = 2, NB_SERVICE_REAL_TIME_VIDEO = 3, NB_SERVICE_CALL_SIGNALING = 4, NB_SERVICE_REAL_TIME_GAME = 5, NB_SERVICE_NORMAL_GAME = 6, NB_SERVICE_SHORT_VIDEO = 7, NB_SERVICE_LONG_VIDEO = 8, NB_SERVICE_LIVE_STREAMING_ANCHOR = 9, NB_SERVICE_LIVE_STREAMING_WATCHER = 10, NB_SERVICE_DOWNLOAD = 11, NB_SERVICE_UPLOAD = 12, NB_SERVICE_BROWSER = 13, NB_SERVICE_TRANSACTION = 14, NB_SERVICE_DETECTION = 15, NB_SERVICE_CLOUDSERVICE = 16, NB_SERVICE_VOICE_CONFERENCE = 17, NB_SERVICE_VIDEO_CONFERENCE = 18, NB_SERVICE_NAVIGATION = 19, NB_SERVICE_SECKILL_SERVICE = 20, NB_SERVICE_LOGIN = 21, NB_SERVICE_AUDIO = 22, NB_SERVICE_SHOPPING = 23 } | 应用业务类型。 |
| NetworkBoost_QoeType { NB_QOE_GOOD = 0, NB_QOE_BAD_UNKNOWN = 1, NB_QOE_BAD_SERVER_ERROR = 2, NB_QOE_BAD_NO_DATA = 3, NB_QOE_BAD_PACKET_LOST = 4, NB_QOE_BAD_PACKET_OUT_OF_ORDER = 5, NB_QOE_BAD_HIGH_JITTER = 6, NB_QOE_BAD_HIGH_LATENCY = 7 } | 应用体验类型。 |

**函数**

| 名称 | 描述 |
| --- | --- |
| int32_t HMS_NetworkBoost_RegisterNetQosCallback (HMS_NetworkBoost_NetQosChange callback, uint32_t *callbackId) | 注册网络质量信息回调。 |
| int32_t HMS_NetworkBoost_UnregisterNetQosCallback (uint32_t callbackId) | 取消注册网络质量信息回调。 |
| int32_t HMS_NetworkBoost_RegisterNetSceneCallback (HMS_NetworkBoost_NetSceneChange callback, uint32_t *callbackId) | 注册网络场景变化信息回调。 |
| int32_t HMS_NetworkBoost_UnregisterNetSceneCallback (uint32_t callbackId) | 取消注册网络场景变化信息回调。 |
| int32_t HMS_NetworkBoost_ReportQoe (NetworkBoost_ServiceType serviceType, NetworkBoost_QoeType qoeType) | 应用传输体验反馈。 |