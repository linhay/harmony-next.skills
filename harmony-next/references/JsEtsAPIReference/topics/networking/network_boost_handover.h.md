# network_boost_handover.h

**概述**

声明用于连接迁移模块的API。提供基本的函数、结构体和const定义。

库： libnetwork_boost.so

系统能力： SystemCapability.Communication.NetworkBoost.Core

起始版本： 5.1.0(18)

相关模块： [NetworkBoost](NetworkBoost.md)

**汇总**

**结构体**

| 名称 | 描述 |
| --- | --- |
| struct NetworkBoost_DataSpeedAction | 发包建议。 |
| struct NetworkBoost_NetHandle | 数据网络的句柄。 |
| struct NetworkBoost_HandoverStart | 连接迁移开始信息。 |
| struct NetworkBoost_HandoverComplete | 连接迁移完成信息。 |
| struct HMS_NetworkBoost_HandoverCallback | 回调函数，返回连接迁移开始和完成的详细信息。 |
| struct NetworkBoost_MultiPathQuotaInfo | 配额信息。 |
| struct NetworkBoost_MultiPathQuota | 应用配额使用信息。 |
| struct NetworkBoost_MultiPathRequestResult | 多网请求结果。 |
| struct NetworkBoost_MultiPathStateChange | 多网状态信息。 |
| struct NetworkBoost_MultiPathRecommendation | 多网推荐信息。 |

**类型定义**

| 名称 | 描述 |
| --- | --- |
| typedef enum NetworkBoost_DataSpeedSimpleAction NetworkBoost_DataSpeedSimpleAction | 应用发包策略的简单建议。 |
| typedef enum NetworkBoost_ErrorResult NetworkBoost_ErrorResult | 表示连接迁移结果枚举。 |
| typedef enum NetworkBoost_ReEstAction NetworkBoost_ReEstAction | 表示重建枚举。 |
| typedef struct NetworkBoost_DataSpeedAction NetworkBoost_DataSpeedAction | 发包速率建议。 |
| typedef struct NetworkBoost_NetHandle NetworkBoost_NetHandle | 数据网络的句柄。 |
| typedef struct NetworkBoost_HandoverStart NetworkBoost_HandoverStart | 连接迁移开始信息。 |
| typedef struct NetworkBoost_HandoverComplete NetworkBoost_HandoverComplete | 连接迁移完成信息。 |
| typedef enum NetworkBoost_HandoverMode NetworkBoost_HandoverMode | 连接迁移模式枚举。 |
| typedef void(* HMS_NetworkBoost_OnHandoverStart) (NetworkBoost_HandoverStart *handoverStart) | 连接迁移开始的回调原型。 |
| typedef void(* HMS_NetworkBoost_OnHandoverComplete) (NetworkBoost_HandoverComplete *handoverComplete) | 连接迁移结束的回调原型。 |
| typedef struct HMS_NetworkBoost_HandoverCallback HMS_NetworkBoost_HandoverCallback | 回调函数，返回连接迁移开始和完成的详细信息。 |
| typedef void (HMS_NetworkBoost_OnMultiPathRequestResult)(NetworkBoost_MultiPathRequestResult* result) | 多网请求结果回调原型。 |
| typedef void (HMS_NetworkBoost_OnMultiPathStateChange)(NetworkBoost_MultiPathStateChange* multiPathState) | 多网状态变化回调原型。 |
| typedef void (HMS_NetworkBoost_OnMultiPathRecommendation)(NetworkBoost_MultiPathRecommendation* recommendation) | 系统多网建议变化回调原型。 |

**枚举**

| 名称 | 描述 |
| --- | --- |
| NetworkBoost_DataSpeedSimpleAction { NB_SIMPLEACTION_SUSPEND_DATA = 1, NB_SIMPLEACTION_DECREASE_DATA = 2, NB_SIMPLEACTION_INCREASE_DATA = 3, NB_SIMPLEACTION_KEEP_DATA = 4 } | 应用发包策略的简单建议。 |
| NetworkBoost_ErrorResult { NB_ERROR_NONE = 0, NB_ERROR_HANDOVER_TIMEOUT = 1, NB_ERROR_NEW_PATH_ACTIVATION_FAILED = 2, NB_ERROR_ABORT = 3 } | 连接迁移结果枚举。 |
| NetworkBoost_ReEstAction { NB_REEST_DEFAULT = 0, NB_REEST_QUERY_DNS = 1, NB_REEST_CHANGE_REMOTE_IP = 2, NB_REEST_CHANGE_IP_VERSION = 3, NB_NO_EST = 4 } | 重建枚举。 |
| NetworkBoost_HandoverMode { NB_MODE_DELEGATION = 0, NB_MODE_DISCRETION = 1 } | 连接迁移模式枚举。 |
| NetworkBoost_PathState{ NB_PATH_IDLE = 0，NB_PATH_CONNECTED = 1，NB_PATH_SUSPENDED = 2 } | 多网链路状态的枚举。 |
| NetworkBoost_MultiPathErrorResult{ NB_MULTIPATH_ERROR_NONE = 0，NB_MULTIPATH_ERROR_NETWORK_REFUSED = 1， NB_MULTIPATH_ERROR_TIMEOUT = 2， NB_MULTIPATH_ERROR_LOCAL = 3 } | 多网建立结果的枚举。 |
| NetworkBoost_MultiPathChangeCause{ NB_MULTIPATH_CAUSE_REQUEST_NORMAL = 0, NB_MULTIPATH_CAUSE_RELEASE_NORMAL = 50, NB_MULTIPATH_CHANGE_CAUSE_RELEASE_NETWORK = 51, NB_MULTIPATH_CHANGE_CAUSE_RELEASE_USER_REFUSED = 52, NB_MULTIPATH_CAUSE_RELEASE_NO_QUOTA = 53, NB_MULTIPATH_CAUSE_RELEASE_POWER_CONSUMPTION = 54, NB_MULTIPATH_CHANGE_CAUSE_RELEASE_INSUFFICIENT_TRAFFIC = 55, NB_MULTIPATH_CHANGE_CAUSE_RELEASE_CONFLICT = 56, NB_MULTIPATH_CHANGE_CAUSE_RELEASE_SYS_FUSING = 57, NB_MULTIPATH_CHANGE_CAUSE_RELEASE_SYS_DEFAULT = 99, NB_MULTIPATH_CHANGE_CAUSE_SUSPEND_ENTER = 100, NB_MULTIPATH_CHANGE_CAUSE_SUSPEND_LEAVE = 101, NB_MULTIPATH_CHANGE_CAUSE_CONN_PROPERTIES_UPDATE = 102 } | 多网变化原因的枚举。 |
| NetworkBoost_MultiPathState{ NB_MULTIPATH_IDLE = 0, NB_MULTIPATH_CREATEING = 1, NB_MULTIPATH_CREATED = 2, NB_MULTIPATH_RELEASING = 3 } | 多网状态的枚举。 |
| NetworkBoost_MultiPathAction{ NB_MULTIPATH_ACTION_REQUEST = 0， NB_MULTIPATH_ACTION_RELEASE = 1 } | 多网推荐动作的枚举。 |

**函数**

| 名称 | 描述 |
| --- | --- |
| int32_t HMS_NetworkBoost_RegisterHandoverChangeCallback (HMS_NetworkBoost_HandoverCallback *callback, uint32_t *callbackId) | 注册连接迁移回调。 |
| int32_t HMS_NetworkBoost_UnregisterHandoverChangeCallback (uint32_t callbackId) | 取消注册连接迁移回调。 |
| int32_t HMS_NetworkBoost_SetHandoverMode (NetworkBoost_HandoverMode mode) | 应用可通过该接口变更连接迁移模式，包括委托模式(由系统发起连接迁移)，和自主模式(由应用发起连接迁移)，默认为委托模式。设置失败，接口会抛出异常。 |
| int32_t HMS_NetworkBoost_GetMultiPathQuotaStats(NetworkBoost_MultiPathQuota *quota) | 获取当前应用多网使用的配额，包括已使用的配额信息和剩余配额信息。 |
| int32_t HMS_NetworkBoost_RequestMultiPath(HMS_NetworkBoost_OnMultiPathRequestResult result, uint32_t *requestId) | 发起多网请求。 |
| int32_t HMS_NetworkBoost_ReleaseMultiPath(uint32_t requestId) | 释放多网请求。 |
| int32_t HMS_NetworkBoost_RegisterMultiPathStateChangeCallback(HMS_NetworkBoost_OnMultiPathStateChangecallback, uint32_t *callbackId) | 注册多网状态变化事件。 |
| int32_t HMS_NetworkBoost_UnregisterMultiPathStateChangeCallback(uint32_t callbackId) | 去注册多网状态变化事件。 |
| int32_t HMS_NetworkBoost_RegisterMultiPathRecommendationCallback(HMS_NetworkBoost_OnMultiPathRecommendationcallback, uint32_t *callbackId) | 注册系统多网建议变化事件。 |
| int32_t HMS_NetworkBoost_UnregisterMultiPathRecommendationCallback(uint32_t callbackId) | 去系统多网建议变化事件。 |