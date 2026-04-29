# Rcp_EventsHandler

**概述**

监听不同HTTP事件的回调函数。

起始版本： 5.0.0(12)

相关模块： [RemoteCommunication](RemoteCommunication.md)

所在头文件： [rcp.h](rcp.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| Rcp_OnDataReceiveCallbackonDataReceive | 收到响应体时的回调函数。 |
| Rcp_OnProgressCallbackonUploadProgress | 上传时调用的回调函数。 |
| Rcp_OnProgressCallbackonDownloadProgress | 下载时调用的回调函数。 |
| Rcp_OnHeaderReceiveCallbackonHeaderReceive | 收到header时的回调函数。 |
| Rcp_OnVoidCallbackonDataEnd | 传输结束时的回调函数。 |
| Rcp_OnVoidCallbackonCanceled | 请求或会话被取消时的回调函数。 |

**结构体成员变量说明**

**onCanceled**

```ets
Rcp_OnVoidCallback Rcp_EventsHandler::onCanceled
```

描述

请求或会话被取消时的回调函数。

**onDataEnd**

```ets
Rcp_OnVoidCallback Rcp_EventsHandler::onDataEnd
```

描述

传输结束时的回调函数。

**onDataReceive**

```ets
Rcp_OnDataReceiveCallback Rcp_EventsHandler::onDataReceive
```

描述

收到响应体时的回调函数。

**onDownloadProgress**

```ets
Rcp_OnProgressCallback Rcp_EventsHandler::onDownloadProgress
```

描述

下载时调用的回调函数。

**onHeaderReceive**

```ets
Rcp_OnHeaderReceiveCallback Rcp_EventsHandler::onHeaderReceive
```

描述

收到header时的回调函数。

**onUploadProgress**

```ets
Rcp_OnProgressCallback Rcp_EventsHandler::onUploadProgress
```

描述

上传时调用的回调函数。