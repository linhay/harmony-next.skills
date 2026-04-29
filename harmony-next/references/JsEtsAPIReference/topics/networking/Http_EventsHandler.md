# Http_EventsHandler

```ets
typedef struct Http_EventsHandler {...} Http_EventsHandler
```

#### 概述

监听不同HTTP事件的回调函数。

**起始版本：** 20

**相关模块：**[netstack](Netstack.md)

所在头文件： [net_http_type.h](net_http_type.h.md)

#### 汇总

#### 成员变量

| 名称 | 描述 |
| --- | --- |
| [Http_OnDataReceiveCallback](net_http_type.h.md#ZH-CN_TOPIC_0000002497605460__http_ondatareceivecallback) onDataReceive | 收到响应体时的回调函数，参考Http_OnDataReceiveCallback。 |
| [Http_OnProgressCallback](net_http_type.h.md#ZH-CN_TOPIC_0000002497605460__http_onprogresscallback) onUploadProgress | 上传时调用的回调函数，参考Http_OnProgressCallback。 |
| [Http_OnProgressCallback](net_http_type.h.md#ZH-CN_TOPIC_0000002497605460__http_onprogresscallback) onDownloadProgress | 下载时调用的回调函数，参考Http_OnProgressCallback。 |
| [Http_OnHeaderReceiveCallback](net_http_type.h.md#ZH-CN_TOPIC_0000002497605460__http_onheaderreceivecallback) onHeadersReceive | 收到header时的回调函数，参考Http_OnHeaderReceiveCallback。 |
| [Http_OnVoidCallback](net_http_type.h.md#ZH-CN_TOPIC_0000002497605460__http_onvoidcallback) onDataEnd | 传输结束时的回调函数，参考Http_OnVoidCallback。 |
| [Http_OnVoidCallback](net_http_type.h.md#ZH-CN_TOPIC_0000002497605460__http_onvoidcallback) onCanceled | 请求被取消时的回调函数，参考Http_OnVoidCallback。 |
