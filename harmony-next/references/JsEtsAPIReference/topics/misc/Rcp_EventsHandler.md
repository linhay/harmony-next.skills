# Rcp_EventsHandler

#### 概述

监听不同HTTP事件的回调函数。

**起始版本：** 5.0.0(12)

**相关模块：**[RemoteCommunication](RemoteCommunication.md)

#### 汇总

#### 成员变量

名称

描述

[Rcp_OnDataReceiveCallback](../media/Rcp_OnDataReceiveCallback.md)[onDataReceive](Rcp_EventsHandler.md#ZH-CN_TOPIC_0000002282446438__adbe4eae15e9325332c4723041c956ca1)

收到响应体时的回调函数。

[Rcp_OnProgressCallback](../components/Rcp_OnProgressCallback.md)[onUploadProgress](Rcp_EventsHandler.md#ZH-CN_TOPIC_0000002282446438__a2ed016a986b6813c6983ffbeac55827f)

上传时调用的回调函数。

[Rcp_OnProgressCallback](../components/Rcp_OnProgressCallback.md)[onDownloadProgress](Rcp_EventsHandler.md#ZH-CN_TOPIC_0000002282446438__a9f8a879701150c07720137a61945fcb5)

下载时调用的回调函数。

[Rcp_OnHeaderReceiveCallback](Rcp_OnHeaderReceiveCallback.md)[onHeaderReceive](Rcp_EventsHandler.md#ZH-CN_TOPIC_0000002282446438__a8431cdb73925f4df6213ec6385b2f0f9)

收到header时的回调函数。

[Rcp_OnVoidCallback](Rcp_OnVoidCallback.md)[onDataEnd](Rcp_EventsHandler.md#ZH-CN_TOPIC_0000002282446438__a7dfa76b63d826eddafc885b79813d226)

传输结束时的回调函数。

[Rcp_OnVoidCallback](Rcp_OnVoidCallback.md)[onCanceled](Rcp_EventsHandler.md#ZH-CN_TOPIC_0000002282446438__aff228ac71317d81091f0ded4a2164624)

请求或会话被取消时的回调函数。

#### 结构体成员变量说明

#### onCanceled

```ets
[Rcp_OnVoidCallback](Rcp_OnVoidCallback.md) Rcp_EventsHandler::onCanceled
```

**描述**

请求或会话被取消时的回调函数。

#### onDataEnd

```ets
[Rcp_OnVoidCallback](Rcp_OnVoidCallback.md) Rcp_EventsHandler::onDataEnd
```

**描述**

传输结束时的回调函数。

#### onDataReceive

```ets
[Rcp_OnDataReceiveCallback](../media/Rcp_OnDataReceiveCallback.md) Rcp_EventsHandler::onDataReceive
```

**描述**

收到响应体时的回调函数。

#### onDownloadProgress

```ets
[Rcp_OnProgressCallback](../components/Rcp_OnProgressCallback.md) Rcp_EventsHandler::onDownloadProgress
```

**描述**

下载时调用的回调函数。

#### onHeaderReceive

```ets
[Rcp_OnHeaderReceiveCallback](Rcp_OnHeaderReceiveCallback.md) Rcp_EventsHandler::onHeaderReceive
```

**描述**

收到header时的回调函数。

#### onUploadProgress

```ets
[Rcp_OnProgressCallback](../components/Rcp_OnProgressCallback.md) Rcp_EventsHandler::onUploadProgress
```

**描述**

上传时调用的回调函数。