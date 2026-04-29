# Rcp_TracingConfiguration

**概述**

请求追踪配置。

起始版本： 5.0.0(12)

相关模块： [RemoteCommunication](RemoteCommunication.md)

所在头文件： [rcp.h](rcp.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| bool verbose | 请求运行时是否记录详细日志。默认值为false。如果设置了infoToCollect中的选项，则自动启用。 |
| Rcp_InfoToCollectinfoToCollect | 指定要收集的请求处理事件。可以通过响应对象检查收集的事件。 |
| bool collectTimeInfo | 是否收集请求计时信息。默认值为false。 |
| Rcp_EventsHandlerhttpEventsHandler | 监听不同HTTP事件的回调函数。 |

**结构体成员变量说明**

**collectTimeInfo**

```ets
bool Rcp_TracingConfiguration::collectTimeInfo
```

描述

是否收集请求计时信息。默认值为false。

**httpEventsHandler**

```ets
Rcp_EventsHandler Rcp_TracingConfiguration::httpEventsHandler
```

描述

监听不同HTTP事件的回调函数。

**infoToCollect**

```ets
Rcp_InfoToCollect Rcp_TracingConfiguration::infoToCollect
```

描述

指定要收集的请求处理事件。可以通过响应对象检查收集的事件。

**verbose**

```ets
bool Rcp_TracingConfiguration::verbose
```

描述

请求运行时是否记录详细日志。默认值为false。如果设置了infoToCollect中的选项，则自动启用。