# ServiceCollaboration_CollaborationDeviceInfoSets

**概述**

通过[HMS_ServiceCollaboration_GetCollaborationDeviceInfos](ServiceCollaboration.md#ZH-CN_TOPIC_0000002553201533__hms_servicecollaboration_getcollaborationdeviceinfos)获取的对端设备信息对象集合。

起始版本： 5.0.0(12)

相关模块： [ServiceCollaboration](ServiceCollaboration.md)

所在头文件： [service_collaboration_api.h](service_collaboration_api.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| uint32_t size | 对端设备信息对象集合的大小。 |
| ServiceCollaboration_CollaborationDeviceInfo * deviceInfoSets | 对端设备信息对象集合。 |

**结构体成员变量说明**

**deviceInfoSets**

```ets
ServiceCollaboration_CollaborationDeviceInfo* ServiceCollaboration_CollaborationDeviceInfoSets::deviceInfoSets
```

描述

对端设备信息对象集合。

**size**

```ets
uint32_t ServiceCollaboration_CollaborationDeviceInfoSets::size
```

描述

对端设备信息对象集合的大小。