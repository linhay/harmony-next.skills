# service_collaboration_api.h

**概述**

函数export定义的接口。

引用文件： <service_collaboration/service_collaboration_api.h>

库： libservice_collaboration_ndk.z.so

系统能力： SystemCapability.Collaboration.Service

起始版本： 5.0.0(12)

相关模块： [ServiceCollaboration](ServiceCollaboration.md)

**汇总**

**结构体**

| 名称 | 描述 |
| --- | --- |
| struct ServiceCollaboration_CollaborationDeviceInfo | 跨设备互通获取的设备信息对象，包含设备的基本信息和能力类型。 |
| struct ServiceCollaboration_CollaborationDeviceInfoSets | 通过HMS_ServiceCollaboration_GetCollaborationDeviceInfos获取的对端设备信息对象集合。 |
| struct ServiceCollaboration_SelectInfo | 使用HMS_ServiceCollaboration_StartCollaboration触发跨设备互通时，被选择的设备信息。 |
| struct ServiceCollaborationCallback | 传给HMS_ServiceCollaboration_StartCollaboration的回调方法。 |
| struct ServiceCollaboration_SelectInfoV2 | 使用HMS_ServiceCollaboration_StartCollaborationV2触发跨设备互通时，被选择的设备信息，支持选择具有图片和视频回传能力的设备。 |

**宏定义**

| 名称 | 描述 |
| --- | --- |
| COLLABORATIONDEVICEINFO_DEVICENETWORKID_MAXLENGTH 65 | 设备network Id最大长度。 |
| COLLABORATIONDEVICEINFO_DEVICENAME_MAXLENGTH 128 | 设备名最大长度。 |
| SERVICE_COLLABORATION_URI_MAXLENGTH 4096 | 传入应用沙箱目录uri的最大长度。 |

**类型定义**

| 名称 | 描述 |
| --- | --- |
| typedef enum ServiceCollaborationFilterType ServiceCollaborationFilterType | 跨设备互通能力类型枚举。 |
| typedef enum ServiceCollaborationDataType ServiceCollaborationDataType | 回传数据类型。 |
| typedef enum ServiceCollaborationEventCode ServiceCollaborationEventCode | 错误码枚举。 |
| typedef struct ServiceCollaboration_CollaborationDeviceInfo ServiceCollaboration_CollaborationDeviceInfo | 设备信息对象。 |
| typedef struct ServiceCollaboration_CollaborationDeviceInfoSets ServiceCollaboration_CollaborationDeviceInfoSets | 设备信息对象集合。 |
| typedef struct ServiceCollaboration_SelectInfo ServiceCollaboration_SelectInfo | 被选择的设备信息。 |
| typedef struct ServiceCollaborationCallback ServiceCollaborationCallback | 回调跨设备互通状态信息。 |
| typedef struct ServiceCollaboration_SelectInfoV2 ServiceCollaboration_SelectInfoV2 | 被选择的设备信息。 |
| typedef struct CollaborationDeviceFilterType CollaborationDeviceFilterType | 跨设备互通设备类型枚举 |

**枚举**

| 名称 | 描述 |
| --- | --- |
| ServiceCollaborationFilterType { TAKE_PHOTO = 1, SCAN_DOCUMENT = 2, IMAGE_PICKER = 3, VIDEO_PICKER = 5, IMAGE_VIDEO_PICKER = 6 } | 跨设备互通能力类型的枚举。 |
| ServiceCollaborationDataType{ IMAGE = 1, VIDEO = 2 } | 回传数据类型。 |
| ServiceCollaborationEventCode{ LAST_DATA_BACK = 1001202000, PEER_CANCEL = 1001202001, NETWORK_ERROR = 1001202002, PEER_WIFI_NOT_OPEN = 1001202004, LOCAL_WIFI_NOT_OPEN = 1001202005, DATA_BACK_START = 1001202006, MIDDLE_DATA_BACK = 1001202007, TIMEOUT_AUTO_CANCEL = 1001202008, DATA_READ_FAILED = 1001202009, LINK_SHUTDOWN = 1001202011, REMOTE_HOTSPOT_CONFLICT = 1001202013, REMOTE_DISTRIBUTED_SERVICES_CONFLICT = 1001202014, SEND_VIDEO_SUCCESS = 1001202015, MULTI_VIDEO_SENDING_BACK = 1001202016, STORE_VIDEO_FAIL = 1001202017 } | 错误码枚举。 |
| CollaborationDeviceFilterType { PHONE = 1, TABLET = 2, PC_2IN1 = 3 } | 被调用端设备类型的枚举。 |

**函数**

| 名称 | 描述 |
| --- | --- |
| ServiceCollaboration_CollaborationDeviceInfoSets* HMS_ServiceCollaboration_GetCollaborationDeviceInfos( uint32_t fileterNum, ServiceCollaborationFilterType serviceFileterTypes[]); | 获取支持相关能力的设备列表。 |
| uint32_t HMS_ServiceCollaboration_StartCollaboration( const ServiceCollaboration_SelectInfo* selectService, ServiceCollaborationCallback* callback) | 拉起跨设备互通回传图片的能力。 |
| int32_t HMS_ServiceCollaboration_StopCollaboration(uint32_t collaborationId); | 取消跨设备互通能力。 |
| uint32_t HMS_ServiceCollaboration_StartCollaborationV2( const ServiceCollaboration_SelectInfoV2* selectService, ServiceCollaborationCallback* callback) | 拉起跨设备互通回传图片和视频的能力。 |
| ServiceCollaboration_CollaborationDeviceInfoSets* HMS_ServiceCollaboration_GetCollaborationDeviceInfosV2 ( uint32_t deviceFilterNum, CollaborationDeviceFilterType deviceFilterTypes[], uint32_t serviceFilterNum, ServiceCollaborationFilterType serviceFilterTypes[]) | 获取支持相关能力的相关指定设备列表。 |