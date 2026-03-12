# network_boost_quality.h

#### 概述

声明用于网络质量模块的API。提供基本的函数、结构体和const定义。

**库：** libnetwork_boost.so

**系统能力：** SystemCapability.Communication.NetworkBoost.Core

**起始版本：** 5.1.0(18)

**相关模块：**[NetworkBoost](NetworkBoost.md)

#### 汇总

#### 结构体

名称

描述

struct [NetworkBoost_NetworkQos](NetworkBoost_NetworkQos.md)

网络质量回调信息。

struct [NetworkBoost_NetworkQosArray](NetworkBoost_NetworkQosArray.md)

网络质量变化的详细信息。

struct [NetworkBoost_WeakSignalPrediction](NetworkBoost_WeakSignalPrediction.md)

弱信号预测相关信息。

struct [NetworkBoost_NetworkScene](NetworkBoost_NetworkScene.md)

网络场景状态变更回调信息。

#### 宏定义

名称

描述

[NETBOOST_MAX_PATH_NUM](NetworkBoost.md#ZH-CN_TOPIC_0000002463695266__ga7668e89aac2dea1d584a9ccacea33614) 4

网络质量变化的最大路径数量。

[NB_BPS](NetworkBoost.md#ZH-CN_TOPIC_0000002463695266__gabdf273f7096ba64be754f03a0da421f1) 1

1bps

[NB_KBPS](NetworkBoost.md#ZH-CN_TOPIC_0000002463695266__gab99b17bff7ea6a679f99ac7cdd1b3700) 1000

1kbps

[NB_MBPS](NetworkBoost.md#ZH-CN_TOPIC_0000002463695266__gafd7fe5b6bd12a15f1eafab390bd8a8bd) 1000000

1mbps

[NB_GBPS](NetworkBoost.md#ZH-CN_TOPIC_0000002463695266__ga1e4efaf6c147fb7cfbd8f72083be3f82) 1000000000

1gbps

[NB_TBPS](NetworkBoost.md#ZH-CN_TOPIC_0000002463695266__gade9c8363d332d7740b454e2920315ac5) 1000000000000

1tbps，请使用uint64_t类型来避免溢出。

#### 类型定义

名称

描述

typedef enum [NetworkBoost_RecommendedAction](NetworkBoost.md#ZH-CN_TOPIC_0000002463695266__ga42f25be03d340c17630c3a0f9cd0d123)[NetworkBoost_RecommendedAction](NetworkBoost.md#ZH-CN_TOPIC_0000002463695266__ga3543e6660b965ebc071fd13d359d6a39)

应用数传策略建议。

typedef enum [NetworkBoost_PathType](NetworkBoost.md#ZH-CN_TOPIC_0000002463695266__gae8474ae83c3add50ac3fa7702c089ea8)[NetworkBoost_PathType](NetworkBoost.md#ZH-CN_TOPIC_0000002463695266__ga45748b2a298346cbea2f1cbe573ffe72)

数据路径类型，枚举值。

typedef enum [NetworkBoost_Scene](NetworkBoost.md#ZH-CN_TOPIC_0000002463695266__ga972c3eb36772eb1affb0cd551429547b)[NetworkBoost_Scene](NetworkBoost.md#ZH-CN_TOPIC_0000002463695266__ga551f8ada8a742207e5eba134765d2a0f)

网络场景类型。

typedef enum [NetworkBoost_ServiceType](NetworkBoost.md#ZH-CN_TOPIC_0000002463695266__ga5b192f3d72de3ac083df4cf36cbc318f)[NetworkBoost_ServiceType](NetworkBoost.md#ZH-CN_TOPIC_0000002463695266__gaabe242932bb115198d2f27c0deedb0f5)

应用业务类型。

typedef enum [NetworkBoost_QoeType](NetworkBoost.md#ZH-CN_TOPIC_0000002463695266__ga539adc59ea2ca1c7498eac3a59bc62be)[NetworkBoost_QoeType](NetworkBoost.md#ZH-CN_TOPIC_0000002463695266__ga152febbb6bccad7017f37457e433ba6e)

应用体验类型。

typedef struct [NetworkBoost_NetworkQos](NetworkBoost_NetworkQos.md)[NetworkBoost_NetworkQos](NetworkBoost.md#ZH-CN_TOPIC_0000002463695266__ga950f78df8282426c91728728c8ca9e8e)

网络质量回调信息。

typedef struct [NetworkBoost_NetworkQosArray](NetworkBoost_NetworkQosArray.md)[NetworkBoost_NetworkQosArray](NetworkBoost.md#ZH-CN_TOPIC_0000002463695266__gac61cbd4df3cf59284dcbdc5860e6ef9b)

网络质量变化的详细信息。

typedef struct [NetworkBoost_WeakSignalPrediction](NetworkBoost_WeakSignalPrediction.md)[NetworkBoost_WeakSignalPrediction](NetworkBoost.md#ZH-CN_TOPIC_0000002463695266__ga2d2d1a19e06dd2746d18eb9eaa8ae8af)

弱信号预测相关信息。

typedef struct [NetworkBoost_NetworkScene](NetworkBoost_NetworkScene.md)[NetworkBoost_NetworkScene](NetworkBoost.md#ZH-CN_TOPIC_0000002463695266__ga133be4442e775aa5b062a29f6de9bfe0)

网络场景状态变更回调信息。

typedef void(* [HMS_NetworkBoost_NetQosChange](NetworkBoost.md#ZH-CN_TOPIC_0000002463695266__ga51a4f0de15c82e94eceafdc8444dd51a)) ([NetworkBoost_NetworkQosArray](NetworkBoost_NetworkQosArray.md) *networkQosArray)

网络质量变更回调。

typedef void(* [HMS_NetworkBoost_NetSceneChange](NetworkBoost.md#ZH-CN_TOPIC_0000002463695266__gab00c153ac0c6faf6066cd013ac1d97d4)) ([NetworkBoost_NetworkScene](NetworkBoost_NetworkScene.md) *networkScene)

网络场景状态变更回调。

#### 枚举

名称

描述

[NetworkBoost_RecommendedAction](NetworkBoost.md#ZH-CN_TOPIC_0000002463695266__ga42f25be03d340c17630c3a0f9cd0d123) {

NB_ACTION_DO_CACHING = 0, NB_ACTION_SUSPEND_DATA = 1, NB_ACTION_DECREASE_DATA = 2, NB_ACTION_INCREASE_DATA = 3,

NB_ACTION_KEEP_DATA = 4

}

应用数传策略建议。

[NetworkBoost_PathType](NetworkBoost.md#ZH-CN_TOPIC_0000002463695266__gae8474ae83c3add50ac3fa7702c089ea8) { NB_PATH_CELLULAR_PRIMARY = 0, NB_PATH_CELLULAR_SECONDARY = 1, NB_PATH_WIFI_PRIMARY = 2, NB_PATH_WIFI_SECONDARY = 3 }

数据路径类型，枚举值。

[NetworkBoost_Scene](NetworkBoost.md#ZH-CN_TOPIC_0000002463695266__ga972c3eb36772eb1affb0cd551429547b) { NB_SCENE_NORMAL = 0, NB_SCENE_CONGESTION = 1, NB_SCENE_FREQUENT_HANDOVER = 2, NB_SCENE_WEAK_SIGNAL = 3 }

网络场景类型。

[NetworkBoost_ServiceType](NetworkBoost.md#ZH-CN_TOPIC_0000002463695266__ga5b192f3d72de3ac083df4cf36cbc318f) {

NB_SERVICE_DEFAULT = 0, NB_SERVICE_BACKGROUND = 1, NB_SERVICE_REAL_TIME_VOICE = 2, NB_SERVICE_REAL_TIME_VIDEO = 3,

NB_SERVICE_CALL_SIGNALING = 4, NB_SERVICE_REAL_TIME_GAME = 5, NB_SERVICE_NORMAL_GAME = 6, NB_SERVICE_SHORT_VIDEO = 7,

NB_SERVICE_LONG_VIDEO = 8, NB_SERVICE_LIVE_STREAMING_ANCHOR = 9, NB_SERVICE_LIVE_STREAMING_WATCHER = 10, NB_SERVICE_DOWNLOAD = 11,

NB_SERVICE_UPLOAD = 12, NB_SERVICE_BROWSER = 13, NB_SERVICE_TRANSACTION = 14, NB_SERVICE_DETECTION = 15, NB_SERVICE_CLOUDSERVICE = 16, NB_SERVICE_VOICE_CONFERENCE = 17, NB_SERVICE_VIDEO_CONFERENCE = 18, NB_SERVICE_NAVIGATION = 19, NB_SERVICE_SECKILL_SERVICE = 20, NB_SERVICE_LOGIN = 21, NB_SERVICE_AUDIO = 22, NB_SERVICE_SHOPPING = 23

}

应用业务类型。

[NetworkBoost_QoeType](NetworkBoost.md#ZH-CN_TOPIC_0000002463695266__ga539adc59ea2ca1c7498eac3a59bc62be) {

NB_QOE_GOOD = 0, NB_QOE_BAD_UNKNOWN = 1, NB_QOE_BAD_SERVER_ERROR = 2, NB_QOE_BAD_NO_DATA = 3,

NB_QOE_BAD_PACKET_LOST = 4, NB_QOE_BAD_PACKET_OUT_OF_ORDER = 5, NB_QOE_BAD_HIGH_JITTER = 6, NB_QOE_BAD_HIGH_LATENCY = 7

}

应用体验类型。

#### 函数

名称

描述

int32_t [HMS_NetworkBoost_RegisterNetQosCallback](NetworkBoost.md#ZH-CN_TOPIC_0000002463695266__ga72cac93efbd98d448ae2d3dc7d3b3dfe) ([HMS_NetworkBoost_NetQosChange](NetworkBoost.md#ZH-CN_TOPIC_0000002463695266__ga51a4f0de15c82e94eceafdc8444dd51a) callback, uint32_t *callbackId)

注册网络质量信息回调。

int32_t [HMS_NetworkBoost_UnregisterNetQosCallback](NetworkBoost.md#ZH-CN_TOPIC_0000002463695266__gae435e58413bd125a9bca06aed0b6ebfe) (uint32_t callbackId)

取消注册网络质量信息回调。

int32_t [HMS_NetworkBoost_RegisterNetSceneCallback](NetworkBoost.md#ZH-CN_TOPIC_0000002463695266__ga13b998a6c6fca1a4b84dd77f547f20ea) ([HMS_NetworkBoost_NetSceneChange](NetworkBoost.md#ZH-CN_TOPIC_0000002463695266__gab00c153ac0c6faf6066cd013ac1d97d4) callback, uint32_t *callbackId)

注册网络场景变化信息回调。

int32_t [HMS_NetworkBoost_UnregisterNetSceneCallback](NetworkBoost.md#ZH-CN_TOPIC_0000002463695266__gad7e9989cb65b01ba52e0b8427fa3e113) (uint32_t callbackId)

取消注册网络场景变化信息回调。

int32_t [HMS_NetworkBoost_ReportQoe](NetworkBoost.md#ZH-CN_TOPIC_0000002463695266__ga2d62d2b3ec0536118a28175d53e0f363) ([NetworkBoost_ServiceType](NetworkBoost.md#ZH-CN_TOPIC_0000002463695266__ga5b192f3d72de3ac083df4cf36cbc318f) serviceType, [NetworkBoost_QoeType](NetworkBoost.md#ZH-CN_TOPIC_0000002463695266__ga539adc59ea2ca1c7498eac3a59bc62be) qoeType)

应用传输体验反馈。