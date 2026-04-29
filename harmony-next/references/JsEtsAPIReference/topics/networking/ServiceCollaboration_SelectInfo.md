# ServiceCollaboration_SelectInfo

**概述**

使用[HMS_ServiceCollaboration_StartCollaboration](ServiceCollaboration.md#ZH-CN_TOPIC_0000002553201533__hms_servicecollaboration_startcollaboration)触发跨设备互通时，被选择的设备信息。

起始版本： 5.0.0(12)

相关模块： [ServiceCollaboration](ServiceCollaboration.md)

所在头文件： [service_collaboration_api.h](service_collaboration_api.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| ServiceCollaborationFilterType serviceFilterType | 开发者期望的设备能力类型。 |
| char deviceNetworkId [COLLABORATIONDEVICEINFO_DEVICENETWORKID_MAXLENGTH] | 被选择的设备network Id。 |
| uint32_t maxSize | 被选择的设备能被选中的最大图片数量。 |

**结构体成员变量说明**

**deviceNetworkId**

```ets
char ServiceCollaboration_SelectInfo::deviceNetworkId[COLLABORATIONDEVICEINFO_DEVICENETWORKID_MAXLENGTH]
```

描述

被选择的设备network Id。

**maxSize**

```ets
uint32_t ServiceCollaboration_SelectInfo::maxSize
```

描述

能被选中的最大图片数量，默认50。

**serviceFilterType**

```ets
ServiceCollaborationFilterType ServiceCollaboration_SelectInfo::serviceFilterType
```

描述

开发者期望的设备能力类型。