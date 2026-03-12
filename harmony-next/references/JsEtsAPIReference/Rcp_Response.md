# Rcp_Response

#### 概述

网络请求的响应。

**起始版本：** 5.0.0(12)

**相关模块：**[RemoteCommunication](RemoteCommunication.md)

#### 汇总

#### 成员变量

名称

描述

const [Rcp_Request](Rcp_Request.md) * [request](Rcp_Response.md#ZH-CN_TOPIC_0000002282446450__ac840978bf352227f8dc889dd74b9ba18)

表示生成响应的请求。

char * [effectiveUrl](Rcp_Response.md#ZH-CN_TOPIC_0000002282446450__a70b36ed43793ef7b2316e6651e70bb02)

上次使用的有效URL。

[Rcp_StatusCode](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga97929a5349f04300f50318f50393b93e)[statusCode](Rcp_Response.md#ZH-CN_TOPIC_0000002282446450__a49900c34bb1ce245916a9afa53d1cf29)

响应状态码。

[Rcp_Headers](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__gac4f343ec02dec34268e93ce746e6c982) * [headers](Rcp_Response.md#ZH-CN_TOPIC_0000002282446450__a270f2855aa008069d5ae45284f00a7eb)

响应标头。

[Rcp_Buffer](Rcp_Buffer.md)[body](Rcp_Response.md#ZH-CN_TOPIC_0000002282446450__a2ef03d4c3fbd3eb2b39063cdad784c9f)

响应消息体。

[Rcp_DebugInfo](Rcp_DebugInfo.md) * [debugInfo](Rcp_Response.md#ZH-CN_TOPIC_0000002282446450__ab42553d48543d390dc3e168daa6679fc)

请求/响应处理调试信息。

[Rcp_TimeInfo](Rcp_TimeInfo.md) * [timeInfo](Rcp_Response.md#ZH-CN_TOPIC_0000002282446450__a57d437be63e686ada47b96b3126067d8)

响应时间信息。

[Rcp_ResponseCookies](Rcp_ResponseCookies.md) * [cookies](Rcp_Response.md#ZH-CN_TOPIC_0000002282446450__a8faaf3b941ee3ea71ea9a5f29f0cba0d)

响应Cookies。

const [Rcp_ResponseCallbackObject](Rcp_ResponseCallbackObject.md) * [responseCallback](Rcp_Response.md#ZH-CN_TOPIC_0000002282446450__a3280f7e39349795a5545663ce573798f)

使用的响应回调。

void(* [destroyResponse](Rcp_Response.md#ZH-CN_TOPIC_0000002282446450__a1fed4fc16ee61a226a4a3cc52d9775bb) )(struct [Rcp_Response](Rcp_Response.md) *response)

用于销毁响应的方法。

void * [responsePrivate](Rcp_Response.md#ZH-CN_TOPIC_0000002282446450__a0fc41a839e5d0646410fc11d46f7fd40)

可扩展字段。

#### 结构体成员变量说明

#### body

```ets
[Rcp_Buffer](Rcp_Buffer.md) Rcp_Response::body
```

**描述**

响应消息体。

#### cookies

```ets
[Rcp_ResponseCookies](Rcp_ResponseCookies.md)* Rcp_Response::cookies
```

**描述**

响应Cookies。

#### debugInfo

```ets
[Rcp_DebugInfo](Rcp_DebugInfo.md)* Rcp_Response::debugInfo
```

**描述**

请求/响应处理调试信息。

收集的事件取决于[Rcp_TracingConfiguration](Rcp_TracingConfiguration.md)配置信息。

#### destroyResponse

```ets
void(* Rcp_Response::destroyResponse) (struct [Rcp_Response](Rcp_Response.md) *response)
```

**描述**

用于销毁响应的方法。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

response

指示要销毁的响应。它是一个指向[Rcp_Response](Rcp_Response.md)的指针。

#### effectiveUrl

```ets
char* Rcp_Response::effectiveUrl
```

**描述**

上次使用的有效URL。

如果重定向，或设置了[Rcp_SessionConfiguration.baseUrl](Rcp_SessionConfiguration.md#ZH-CN_TOPIC_0000002282446402__a8cb997b4f5fdcdf28aad95f975ed2a0c)，则有效URL可能不等于[Rcp_Request.url](Rcp_Request.md#ZH-CN_TOPIC_0000002317039157__a39a1cc0a1ad666d8d9ad40eec4b52de7)。

#### headers

```ets
[Rcp_Headers](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__gac4f343ec02dec34268e93ce746e6c982)* Rcp_Response::headers
```

**描述**

响应标头。

#### request

```ets
const [Rcp_Request](Rcp_Request.md)* Rcp_Response::request
```

**描述**

表示生成响应的请求。

#### responseCallback

```ets
const [Rcp_ResponseCallbackObject](Rcp_ResponseCallbackObject.md)* Rcp_Response::responseCallback
```

**描述**

使用的响应回调。

#### responsePrivate

```ets
void* Rcp_Response::responsePrivate
```

**描述**

可扩展字段。

#### statusCode

```ets
[Rcp_StatusCode](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga97929a5349f04300f50318f50393b93e) Rcp_Response::statusCode
```

**描述**

响应状态码。

#### timeInfo

```ets
[Rcp_TimeInfo](Rcp_TimeInfo.md)* Rcp_Response::timeInfo
```

**描述**

响应时间信息。

是否收集该信息取决于[Rcp_TracingConfiguration.collectTimeInfo](Rcp_TracingConfiguration.md#ZH-CN_TOPIC_0000002317126029__aded07a3d27e7524e18362082264b9b94)文件中的配置信息。