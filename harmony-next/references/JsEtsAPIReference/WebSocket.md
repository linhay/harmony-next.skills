# WebSocket

```ets
struct WebSocket {...}
```

#### 概述

webSocket客户端结构体。

**起始版本：** 11

**相关模块：**[netstack](Netstack.md)

**所在头文件：**[net_websocket_type.h](net_websocket_type.h.md)

#### 汇总

#### 成员变量

名称描述[WebSocket_OnOpenCallback](net_websocket_type.h.md#ZH-CN_TOPIC_0000002529285451__websocket_onopencallback) onOpen客户端接收连接消息的回调指针。[WebSocket_OnMessageCallback](net_websocket_type.h.md#ZH-CN_TOPIC_0000002529285451__websocket_onmessagecallback) onMessage客户端接收消息的回调指针。[WebSocket_OnErrorCallback](net_websocket_type.h.md#ZH-CN_TOPIC_0000002529285451__websocket_onerrorcallback) onError客户端接收错误消息的回调指针。[WebSocket_OnCloseCallback](net_websocket_type.h.md#ZH-CN_TOPIC_0000002529285451__websocket_onclosecallback) onClose客户端接收关闭消息的回调指针。[WebSocket_RequestOptions](WebSocket_RequestOptions.md) requestOptions客户端建立连接请求内容。