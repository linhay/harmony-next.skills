# network_boost_handover.h

#### 概述

声明用于连接迁移模块的API。提供基本的函数、结构体和const定义。

**库：** libnetwork_boost.so

**系统能力：** SystemCapability.Communication.NetworkBoost.Core

**起始版本：** 5.1.0(18)

**相关模块：**[NetworkBoost](NetworkBoost.md)

#### 汇总

#### 结构体

名称

描述

struct [NetworkBoost_DataSpeedAction](NetworkBoost_DataSpeedAction.md)

发包建议。

struct [NetworkBoost_NetHandle](NetworkBoost_NetHandle.md)

数据网络的句柄。

struct [NetworkBoost_HandoverStart](NetworkBoost_HandoverStart.md)

连接迁移开始信息。

struct [NetworkBoost_HandoverComplete](NetworkBoost_HandoverComplete.md)

连接迁移完成信息。

struct [HMS_NetworkBoost_HandoverCallback](HMS_NetworkBoost_HandoverCallback.md)

回调函数，返回连接迁移开始和完成的详细信息。

struct [NetworkBoost_MultiPathQuotaInfo](NetworkBoost_MultiPathQuotaInfo.md)

配额信息。

struct [NetworkBoost_MultiPathQuota](NetworkBoost_MultiPathQuota.md)

应用配额使用信息。

struct [NetworkBoost_MultiPathRequestResult](NetworkBoost_MultiPathRequestResult.md)

多网请求结果。

struct [NetworkBoost_MultiPathStateChange](NetworkBoost_MultiPathStateChange.md)

多网状态信息。

struct [NetworkBoost_MultiPathRecommendation](NetworkBoost_MultiPathRecommendation.md)

多网推荐信息。

#### 类型定义

名称

描述

typedef enum [NetworkBoost_DataSpeedSimpleAction](NetworkBoost.md#ZH-CN_TOPIC_0000002463695266__gae2c308911ff3569b20102600d64d460a)[NetworkBoost_DataSpeedSimpleAction](NetworkBoost.md#ZH-CN_TOPIC_0000002463695266__gac06c759288ec3617480002297aa11dab)

应用发包策略的简单建议。

typedef enum [NetworkBoost_ErrorResult](NetworkBoost.md#ZH-CN_TOPIC_0000002463695266__ga98419dae6f140b89cac79821f9cbbc9d)[NetworkBoost_ErrorResult](NetworkBoost.md#ZH-CN_TOPIC_0000002463695266__ga6946f85cae25ae0ebfd5bbee9579cd08)

表示连接迁移结果枚举。

typedef enum [NetworkBoost_ReEstAction](NetworkBoost.md#ZH-CN_TOPIC_0000002463695266__ga99d4ae084f2d5e3744231152e58e51aa)[NetworkBoost_ReEstAction](NetworkBoost.md#ZH-CN_TOPIC_0000002463695266__gab5ab8d4dfd6770df9ddf344440fe39c9)

表示重建枚举。

typedef struct [NetworkBoost_DataSpeedAction](NetworkBoost_DataSpeedAction.md)[NetworkBoost_DataSpeedAction](NetworkBoost.md#ZH-CN_TOPIC_0000002463695266__ga98032d55873b9c438e4fe7a4393b6ebb)

发包速率建议。

typedef struct [NetworkBoost_NetHandle](NetworkBoost_NetHandle.md)[NetworkBoost_NetHandle](NetworkBoost.md#ZH-CN_TOPIC_0000002463695266__ga83a1277967e95e2965b6f8dbee5945cc)

数据网络的句柄。

typedef struct [NetworkBoost_HandoverStart](NetworkBoost_HandoverStart.md)[NetworkBoost_HandoverStart](NetworkBoost.md#ZH-CN_TOPIC_0000002463695266__gae5e48d9919724eba0c72d4e320122ca6)

连接迁移开始信息。

typedef struct [NetworkBoost_HandoverComplete](NetworkBoost_HandoverComplete.md)[NetworkBoost_HandoverComplete](NetworkBoost.md#ZH-CN_TOPIC_0000002463695266__ga9490335b78db33fe8effe0674036146f)

连接迁移完成信息。

typedef enum [NetworkBoost_HandoverMode](NetworkBoost.md#ZH-CN_TOPIC_0000002463695266__ga7911fd83a6c8af864d1c87e67d5b0cb1)[NetworkBoost_HandoverMode](NetworkBoost.md#ZH-CN_TOPIC_0000002463695266__gaf4d63e47ed8a29ad3bd4104669d80755)

连接迁移模式枚举。

typedef void(* [HMS_NetworkBoost_OnHandoverStart](NetworkBoost.md#ZH-CN_TOPIC_0000002463695266__gaeb846c7c42199e314b95770657ed583d)) ([NetworkBoost_HandoverStart](NetworkBoost_HandoverStart.md) *handoverStart)

连接迁移开始的回调原型。

typedef void(* [HMS_NetworkBoost_OnHandoverComplete](NetworkBoost.md#ZH-CN_TOPIC_0000002463695266__ga799fbecb09ede04fec174737425082f6)) ([NetworkBoost_HandoverComplete](NetworkBoost_HandoverComplete.md) *handoverComplete)

连接迁移结束的回调原型。

typedef struct [HMS_NetworkBoost_HandoverCallback](HMS_NetworkBoost_HandoverCallback.md)[HMS_NetworkBoost_HandoverCallback](NetworkBoost.md#ZH-CN_TOPIC_0000002463695266__ga8ce6f265f4275452f332441338e3035c)

回调函数，返回连接迁移开始和完成的详细信息。

typedef void ([HMS_NetworkBoost_OnMultiPathRequestResult](NetworkBoost.md#section1291820306417))([NetworkBoost_MultiPathRequestResult](NetworkBoost_MultiPathRequestResult.md)* result)

多网请求结果回调原型。

typedef void ([HMS_NetworkBoost_OnMultiPathStateChange](NetworkBoost.md#section192149121805))([NetworkBoost_MultiPathStateChange](NetworkBoost_MultiPathStateChange.md)* multiPathState)

多网状态变化回调原型。

typedef void ([HMS_NetworkBoost_OnMultiPathRecommendation](NetworkBoost.md#section198348561206))([NetworkBoost_MultiPathRecommendation](NetworkBoost_MultiPathRecommendation.md)* recommendation)

系统多网建议变化回调原型。

#### 枚举

名称

描述

[NetworkBoost_DataSpeedSimpleAction](NetworkBoost.md#ZH-CN_TOPIC_0000002463695266__gae2c308911ff3569b20102600d64d460a) { NB_SIMPLEACTION_SUSPEND_DATA = 1, NB_SIMPLEACTION_DECREASE_DATA = 2, NB_SIMPLEACTION_INCREASE_DATA = 3, NB_SIMPLEACTION_KEEP_DATA = 4 }

应用发包策略的简单建议。

[NetworkBoost_ErrorResult](NetworkBoost.md#ZH-CN_TOPIC_0000002463695266__ga98419dae6f140b89cac79821f9cbbc9d) { NB_ERROR_NONE = 0, NB_ERROR_HANDOVER_TIMEOUT = 1, NB_ERROR_NEW_PATH_ACTIVATION_FAILED = 2, NB_ERROR_ABORT = 3 }

连接迁移结果枚举。

[NetworkBoost_ReEstAction](NetworkBoost.md#ZH-CN_TOPIC_0000002463695266__ga99d4ae084f2d5e3744231152e58e51aa) {

NB_REEST_DEFAULT = 0, NB_REEST_QUERY_DNS = 1, NB_REEST_CHANGE_REMOTE_IP = 2, NB_REEST_CHANGE_IP_VERSION = 3,

NB_NO_EST = 4

}

重建枚举。

[NetworkBoost_HandoverMode](NetworkBoost.md#ZH-CN_TOPIC_0000002463695266__ga7911fd83a6c8af864d1c87e67d5b0cb1) { NB_MODE_DELEGATION = 0, NB_MODE_DISCRETION = 1 }

连接迁移模式枚举。

[NetworkBoost_PathState](NetworkBoost.md#section1774664693518){

NB_PATH_IDLE = 0，NB_PATH_CONNECTED = 1，NB_PATH_SUSPENDED = 2

}

多网链路状态的枚举。

[NetworkBoost_MultiPathErrorResult](NetworkBoost.md#section129101047154112){

NB_MULTIPATH_ERROR_NONE = 0，NB_MULTIPATH_ERROR_NETWORK_REFUSED = 1， NB_MULTIPATH_ERROR_TIMEOUT = 2， NB_MULTIPATH_ERROR_LOCAL = 3

}

多网建立结果的枚举。

[NetworkBoost_MultiPathChangeCause](NetworkBoost.md#section19927184203916){

NB_MULTIPATH_CAUSE_REQUEST_NORMAL = 0, NB_MULTIPATH_CAUSE_RELEASE_NORMAL = 50, NB_MULTIPATH_CHANGE_CAUSE_RELEASE_NETWORK = 51, NB_MULTIPATH_CHANGE_CAUSE_RELEASE_USER_REFUSED = 52, NB_MULTIPATH_CAUSE_RELEASE_NO_QUOTA = 53, NB_MULTIPATH_CAUSE_RELEASE_POWER_CONSUMPTION = 54, NB_MULTIPATH_CHANGE_CAUSE_RELEASE_INSUFFICIENT_TRAFFIC = 55, NB_MULTIPATH_CHANGE_CAUSE_RELEASE_CONFLICT = 56, NB_MULTIPATH_CHANGE_CAUSE_RELEASE_SYS_FUSING = 57, NB_MULTIPATH_CHANGE_CAUSE_RELEASE_SYS_DEFAULT = 99, NB_MULTIPATH_CHANGE_CAUSE_SUSPEND_ENTER = 100, NB_MULTIPATH_CHANGE_CAUSE_SUSPEND_LEAVE = 101, NB_MULTIPATH_CHANGE_CAUSE_CONN_PROPERTIES_UPDATE = 102

}

多网变化原因的枚举。

[NetworkBoost_MultiPathState](NetworkBoost.md#section12626124820456){

NB_MULTIPATH_IDLE = 0, NB_MULTIPATH_CREATEING = 1, NB_MULTIPATH_CREATED = 2, NB_MULTIPATH_RELEASING = 3

}

多网状态的枚举。

[NetworkBoost_MultiPathAction](NetworkBoost.md#section12185112974610){

NB_MULTIPATH_ACTION_REQUEST = 0， NB_MULTIPATH_ACTION_RELEASE = 1

}

多网推荐动作的枚举。

#### 函数

名称

描述

int32_t [HMS_NetworkBoost_RegisterHandoverChangeCallback](NetworkBoost.md#ZH-CN_TOPIC_0000002463695266__gac3d95b4bf5c8cbec5ca862130d441fce) ([HMS_NetworkBoost_HandoverCallback](HMS_NetworkBoost_HandoverCallback.md) *callback, uint32_t *callbackId)

注册连接迁移回调。

int32_t [HMS_NetworkBoost_UnregisterHandoverChangeCallback](NetworkBoost.md#ZH-CN_TOPIC_0000002463695266__gaca0ae3e209bc314e808d808786d76eae) (uint32_t callbackId)

取消注册连接迁移回调。

int32_t [HMS_NetworkBoost_SetHandoverMode](NetworkBoost.md#ZH-CN_TOPIC_0000002463695266__ga1f03a8af2bbf9de6af215df385498a7a) ([NetworkBoost_HandoverMode](NetworkBoost.md#ZH-CN_TOPIC_0000002463695266__ga7911fd83a6c8af864d1c87e67d5b0cb1) mode)

应用可通过该接口变更连接迁移模式，包括委托模式(由系统发起连接迁移)，和自主模式(由应用发起连接迁移)，默认为委托模式。设置失败，接口会抛出异常。

int32_t [HMS_NetworkBoost_GetMultiPathQuotaStats](NetworkBoost.md#section3899010125311)([NetworkBoost_MultiPathQuota](NetworkBoost_MultiPathQuota.md) *quota)

获取当前应用多网使用的配额，包括已使用的配额信息和剩余配额信息。

int32_t [HMS_NetworkBoost_RequestMultiPath](NetworkBoost.md#section13240250195914)([HMS_NetworkBoost_OnMultiPathRequestResult](NetworkBoost_MultiPathRequestResult.md) result, uint32_t *requestId)

发起多网请求。

int32_t [HMS_NetworkBoost_ReleaseMultiPath](NetworkBoost.md#section58537189614)(uint32_t requestId)

释放多网请求。

int32_t [HMS_NetworkBoost_RegisterMultiPathStateChangeCallback](NetworkBoost.md#section421172813919)([HMS_NetworkBoost_OnMultiPathStateChange](NetworkBoost.md#section192149121805)callback, uint32_t *callbackId)

注册多网状态变化事件。

int32_t [HMS_NetworkBoost_UnregisterMultiPathStateChangeCallback](NetworkBoost.md#section52786305915)(uint32_t callbackId)

去注册多网状态变化事件。

int32_t [HMS_NetworkBoost_RegisterMultiPathRecommendationCallback](NetworkBoost.md#section463012484123)([HMS_NetworkBoost_OnMultiPathRecommendation](NetworkBoost.md#section198348561206)callback, uint32_t *callbackId)

注册系统多网建议变化事件。

int32_t [HMS_NetworkBoost_UnregisterMultiPathRecommendationCallback](NetworkBoost.md#section18632948201214)(uint32_t callbackId)

去系统多网建议变化事件。