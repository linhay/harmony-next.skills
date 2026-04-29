# ServiceCollaboration_CollaborationDeviceInfo

**概述**

跨设备互通获取的设备信息对象，包含设备的基本信息和能力类型。

起始版本： 5.0.0(12)

相关模块： [ServiceCollaboration](ServiceCollaboration.md)

所在头文件： [service_collaboration_api.h](service_collaboration_api.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| uint32_t deviceType | 对端设备类型。只有手机或者平板。手机设备类型的值为0x14，平板设备类型的值为0x17。 |
| char deviceNetworkId [COLLABORATIONDEVICEINFO_DEVICENETWORKID_MAXLENGTH] | 对端设备network Id。 |
| char deviceName [COLLABORATIONDEVICEINFO_DEVICENAME_MAXLENGTH] | 对端设备名。 |
| uint32_t filterNum | 对端设备支持的能力类型列表的大小。 |
| ServiceCollaborationFilterType * serviceFilterTypes | 对端设备支持的能力类型列表。 |

**结构体成员变量说明**

**deviceName**

```ets
char ServiceCollaboration_CollaborationDeviceInfo::deviceName[COLLABORATIONDEVICEINFO_DEVICENAME_MAXLENGTH]
```

描述

对端设备名。

**deviceNetworkId**

```ets
char ServiceCollaboration_CollaborationDeviceInfo::deviceNetworkId[COLLABORATIONDEVICEINFO_DEVICENETWORKID_MAXLENGTH]
```

描述

对端设备network Id。

**deviceType**

```ets
uint32_t ServiceCollaboration_CollaborationDeviceInfo::deviceType
```

描述

对端设备类型。只有手机或者平板。手机设备类型的值为0x14，平板设备类型的值为0x17。

**filterNum**

```ets
uint32_t ServiceCollaboration_CollaborationDeviceInfo::filterNum
```

描述

对端设备支持的能力类型列表的大小。

**serviceFilterTypes**

```ets
ServiceCollaborationFilterType* ServiceCollaboration_CollaborationDeviceInfo::serviceFilterTypes
```

描述

对端设备支持的能力类型列表。