# ServiceCollaborationCallback

**概述**

传给[HMS_ServiceCollaboration_StartCollaboration](ServiceCollaboration.md#ZH-CN_TOPIC_0000002553201533__hms_servicecollaboration_startcollaboration)的回调方法。

起始版本： 5.0.0(12)

相关模块： [ServiceCollaboration](ServiceCollaboration.md)

所在头文件： [service_collaboration_api.h](service_collaboration_api.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| int32_t(* OnEvent )(ServiceCollaborationEventCode code, uint32_t extraCode) | 在跨设备互通服务状态变化时被调用。 |
| int32_t(* OnDataCallback )(ServiceCollaborationEventCode code, ServiceCollaborationDataType dataType, uint32_t dataSize, char *data) | 在跨设备互通服务数据返回时被调用。 |

**结构体成员变量说明**

**OnDataCallback**

```ets
int32_t(* ServiceCollaborationCallback::OnDataCallback) (ServiceCollaborationEventCode code, ServiceCollaborationDataType dataType, uint32_t dataSize, char *data)
```

描述

在跨设备互通服务数据返回时被调用。

参数：

| 名称 | 描述 |
| --- | --- |
| ServiceCollaborationEventCode code | 错误码。 |
| ServiceCollaborationDataType dataType | 回传数据类型。 |
| uint32_t dataSize | 数据大小，单位是字节。 |
| char *data | 数据。 |

**OnEvent**

```ets
int32_t(* ServiceCollaborationCallback::OnEvent) (ServiceCollaborationEventCode code, uint32_t extraCode)
```

描述

在跨设备互通服务状态变化时被调用。

参数：

| 名称 | 描述 |
| --- | --- |
| ServiceCollaborationEventCode code | 错误码。 |
| uint32_t extraCode | 拓展状态码，携带错误码未提供的额外信息。 |