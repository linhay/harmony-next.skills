# Rcp_Response

**概述**

网络请求的响应。

起始版本： 5.0.0(12)

相关模块： [RemoteCommunication](RemoteCommunication.md)

所在头文件： [rcp.h](rcp.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| const Rcp_Request * request | 表示生成响应的请求。 |
| char * effectiveUrl | 上次使用的有效URL。 |
| Rcp_StatusCodestatusCode | 响应状态码。 |
| Rcp_Headers * headers | 响应标头。 |
| Rcp_Bufferbody | 响应消息体。 |
| Rcp_DebugInfo * debugInfo | 请求/响应处理调试信息。 |
| Rcp_TimeInfo * timeInfo | 响应时间信息。 |
| Rcp_ResponseCookies * cookies | 响应Cookies。 |
| const Rcp_ResponseCallbackObject * responseCallback | 使用的响应回调。 |
| void(* destroyResponse )(struct Rcp_Response *response) | 用于销毁响应的方法。 |
| void * responsePrivate | 可扩展字段。 |

**结构体成员变量说明**

**body**

```ets
Rcp_Buffer Rcp_Response::body
```

描述

响应消息体。

**cookies**

```ets
Rcp_ResponseCookies* Rcp_Response::cookies
```

描述

响应Cookies。

**debugInfo**

```ets
Rcp_DebugInfo* Rcp_Response::debugInfo
```

描述

请求/响应处理调试信息。

收集的事件取决于[Rcp_TracingConfiguration](Rcp_TracingConfiguration.md)配置信息。

**destroyResponse**

```ets
void(* Rcp_Response::destroyResponse) (struct Rcp_Response *response)
```

描述

用于销毁响应的方法。

起始版本： 5.0.0(12)

参数:

| 名称 | 描述 |
| --- | --- |
| response | 指示要销毁的响应。它是一个指向Rcp_Response的指针。 |

**effectiveUrl**

```ets
char* Rcp_Response::effectiveUrl
```

描述

上次使用的有效URL。

如果重定向，或设置了[Rcp_SessionConfiguration.baseUrl](Rcp_SessionConfiguration.md#ZH-CN_TOPIC_0000002522241554__baseurl)，则有效URL可能不等于[Rcp_Request.url](Rcp_Request.md#ZH-CN_TOPIC_0000002522241550__url)。

**headers**

```ets
Rcp_Headers* Rcp_Response::headers
```

描述

响应标头。

**request**

```ets
const Rcp_Request* Rcp_Response::request
```

描述

表示生成响应的请求。

**responseCallback**

```ets
const Rcp_ResponseCallbackObject* Rcp_Response::responseCallback
```

描述

使用的响应回调。

**responsePrivate**

```ets
void* Rcp_Response::responsePrivate
```

描述

可扩展字段。

**statusCode**

```ets
Rcp_StatusCode Rcp_Response::statusCode
```

描述

响应状态码。

**timeInfo**

```ets
Rcp_TimeInfo* Rcp_Response::timeInfo
```

描述

响应时间信息。

是否收集该信息取决于[Rcp_TracingConfiguration.collectTimeInfo](Rcp_TracingConfiguration.md#ZH-CN_TOPIC_0000002522241558__collecttimeinfo)文件中的配置信息。