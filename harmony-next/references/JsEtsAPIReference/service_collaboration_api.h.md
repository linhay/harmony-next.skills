# service_collaboration_api.h

#### 概述

函数export定义的接口。

**库：**libservice_collaboration_ndk.z.so

**系统能力：** SystemCapability.Collaboration.Service

**起始版本：** 5.0.0(12)

**相关模块：**[ServiceCollaboration](ServiceCollaboration.md)

#### 汇总

#### 结构体

名称

描述

struct [ServiceCollaboration_CollaborationDeviceInfo](ServiceCollaboration_CollaborationDeviceInfo.md)

跨设备互通获取的设备信息对象，包含设备的基本信息和能力类型。

struct [ServiceCollaboration_CollaborationDeviceInfoSets](ServiceCollaboration_CollaborationDeviceInfoSets.md)

通过[HMS_ServiceCollaboration_GetCollaborationDeviceInfos](ServiceCollaboration.md#ZH-CN_TOPIC_0000002394951629__gaeffea1546cbe64aeba533e5b72bca7ba)获取的对端设备信息对象集合。

struct [ServiceCollaboration_SelectInfo](ServiceCollaboration_SelectInfo.md)

使用[HMS_ServiceCollaboration_StartCollaboration](ServiceCollaboration.md#section4531193410296)触发跨设备互通时，被选择的设备信息。

struct [ServiceCollaborationCallback](ServiceCollaborationCallback.md)

传给[HMS_ServiceCollaboration_StartCollaboration](ServiceCollaboration.md#section4531193410296)的回调方法。

#### 宏定义

名称

描述

[COLLABORATIONDEVICEINFO_DEVICENETWORKID_MAXLENGTH](ServiceCollaboration.md#ZH-CN_TOPIC_0000002394951629__ga22d10f5d68c518533857b4a3e5947647) 65

设备network Id最大长度。

**[COLLABORATIONDEVICEINFO_DEVICENAME_MAXLENGTH](ServiceCollaboration.md#section115253318501) 128

设备名最大长度。

#### 类型定义

名称

描述

typedef enum [ServiceCollaborationFilterType](ServiceCollaboration.md#section16675437105618)[ServiceCollaborationFilterType](ServiceCollaboration.md#ZH-CN_TOPIC_0000002394951629__ga1d033f8a2e87fab0e1e01cb1e9859243)

跨设备互通能力类型枚举。

typedef enum [ServiceCollaborationDataType](ServiceCollaboration.md#section1467523718564)[ServiceCollaborationDataType](ServiceCollaboration.md#ZH-CN_TOPIC_0000002394951629__ga3547eca8cf19ab049ffc992e5b712142)

回传数据类型。

typedef enum [ServiceCollaborationEventCode](ServiceCollaboration.md#section967514377563)[ServiceCollaborationEventCode](ServiceCollaboration.md#ZH-CN_TOPIC_0000002394951629__ga7ff0af9a33e5e5a3acfada94d422a60b)

错误码枚举。

typedef struct [ServiceCollaboration_CollaborationDeviceInfo](ServiceCollaboration_CollaborationDeviceInfo.md)[ServiceCollaboration_CollaborationDeviceInfo](ServiceCollaboration.md#ZH-CN_TOPIC_0000002394951629__ga36cefd0afb1105cdbc28b9460d5f336f)

设备信息对象。

typedef struct [ServiceCollaboration_CollaborationDeviceInfoSets](ServiceCollaboration_CollaborationDeviceInfoSets.md)[ServiceCollaboration_CollaborationDeviceInfoSets](ServiceCollaboration.md#section121718545319)

设备信息对象集合。

typedef struct [ServiceCollaboration_SelectInfo](ServiceCollaboration_SelectInfo.md)[ServiceCollaboration_SelectInfo](ServiceCollaboration.md#section1871418518535)

被选择的设备信息。

typedef struct [ServiceCollaborationCallback](ServiceCollaborationCallback.md)[ServiceCollaborationCallback](ServiceCollaboration.md#section1958717716536)

回调跨设备互通状态信息。

#### 枚举

名称

描述

[ServiceCollaborationFilterType](ServiceCollaboration.md#section16675437105618) {

TAKE_PHOTO = 1,

SCAN_DOCUMENT = 2,

IMAGE_PICKER = 3

}

跨设备互通能力类型的枚举。

[ServiceCollaborationDataType](ServiceCollaboration.md#section1467523718564){

IMAGE = 1

}

回传数据类型。

[ServiceCollaborationEventCode](ServiceCollaboration.md#section967514377563){

LAST_DATA_BACK = 1001202000,

PEER_CANCEL = 1001202001,

NETWORK_ERROR = 1001202002,

PEER_WIFI_NOT_OPEN = 1001202004,

LOCAL_WIFI_NOT_OPEN = 1001202005,

DATA_BACK_START = 1001202006,

MIDDLE_DATA_BACK = 1001202007,

TIMEOUT_AUTO_CANCEL = 1001202008,

DATA_READ_FAILED = 1001202009,

LINK_SHUTDOWN = 1001202011,

REMOTE_HOTSPOT_CONFLICT = 1001202013,

REMOTE_DISTRIBUTED_SERVICES_CONFLICT = 1001202014

}

错误码枚举。

#### 函数

名称

描述

[ServiceCollaboration_CollaborationDeviceInfoSets](ServiceCollaboration_CollaborationDeviceInfoSets.md)* [HMS_ServiceCollaboration_GetCollaborationDeviceInfos](ServiceCollaboration.md#ZH-CN_TOPIC_0000002394951629__gaeffea1546cbe64aeba533e5b72bca7ba)(

uint32_t fileterNum, [ServiceCollaborationFilterType](ServiceCollaboration.md#section16675437105618) serviceFileterTypes[]);

获取支持相关能力的设备列表。

uint32_t [HMS_ServiceCollaboration_StartCollaboration](ServiceCollaboration.md#section4531193410296)(

const [ServiceCollaboration_SelectInfo](ServiceCollaboration_SelectInfo.md)* selectService, [ServiceCollaborationCallback](ServiceCollaborationCallback.md)* callback)

拉起跨设备互通能力。

int32_t [HMS_ServiceCollaboration_StopCollaboration](ServiceCollaboration.md#section67211235132913)(uint32_t collaborationId);

取消跨设备互通能力。