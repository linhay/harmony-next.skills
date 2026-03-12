# Http_EventsHandler

```ets
typedef struct {...} Http_EventsHandler
```

#### 概述

监听不同HTTP事件的回调函数。

**起始版本：** 20

**相关模块：**[netstack](Netstack.md)

**所在头文件：**[net_http_type.h](net_http_type.h.md)

#### 汇总

#### 成员变量

名称描述[Http_OnDataReceiveCallback](net_http_type.h.md#ZH-CN_TOPIC_0000002497605460__http_ondatareceivecallback) onDataReceive收到响应体时的回调函数，参考[Http_OnDataReceiveCallback](net_http_type.h.md#ZH-CN_TOPIC_0000002497605460__http_ondatareceivecallback)。[Http_OnProgressCallback](net_http_type.h.md#ZH-CN_TOPIC_0000002497605460__http_onprogresscallback) onUploadProgress上传时调用的回调函数，参考[Http_OnProgressCallback](net_http_type.h.md#ZH-CN_TOPIC_0000002497605460__http_onprogresscallback)。[Http_OnProgressCallback](net_http_type.h.md#ZH-CN_TOPIC_0000002497605460__http_onprogresscallback) onDownloadProgress下载时调用的回调函数，参考[Http_OnProgressCallback](net_http_type.h.md#ZH-CN_TOPIC_0000002497605460__http_onprogresscallback)。[Http_OnHeaderReceiveCallback](net_http_type.h.md#ZH-CN_TOPIC_0000002497605460__http_onheaderreceivecallback) onHeadersReceive收到header时的回调函数，参考[Http_OnHeaderReceiveCallback](net_http_type.h.md#ZH-CN_TOPIC_0000002497605460__http_onheaderreceivecallback)。[Http_OnVoidCallback](net_http_type.h.md#ZH-CN_TOPIC_0000002497605460__http_onvoidcallback) onDataEnd传输结束时的回调函数，参考[Http_OnVoidCallback](net_http_type.h.md#ZH-CN_TOPIC_0000002497605460__http_onvoidcallback)。[Http_OnVoidCallback](net_http_type.h.md#ZH-CN_TOPIC_0000002497605460__http_onvoidcallback) onCanceled请求被取消时的回调函数，参考[Http_OnVoidCallback](net_http_type.h.md#ZH-CN_TOPIC_0000002497605460__http_onvoidcallback)。