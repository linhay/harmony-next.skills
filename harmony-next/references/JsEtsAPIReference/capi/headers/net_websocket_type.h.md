# net_websocket_type.h

#### 概述

定义websocket客户端模块的C接口需要的数据结构。

**引用文件：** <network/netstack/net_websocket_type.h>

**库：** libnet_websocket.so

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 11

**相关模块：**[netstack](../../topics/networking/Netstack.md)

#### 汇总

#### 结构体

名称描述[WebSocket_CloseResult](../../topics/networking/WebSocket_CloseResult.md)websocket客户端来自服务端关闭的参数。[WebSocket_CloseOption](../../topics/networking/WebSocket_CloseOption.md)websocket客户端主动关闭的参数。[WebSocket_ErrorResult](../../topics/networking/WebSocket_ErrorResult.md)websocket客户端来自服务端连接错误的参数。[WebSocket_OpenResult](../../topics/networking/WebSocket_OpenResult.md)websocket客户端来自服务端连接成功的参数。[WebSocket_Header](../../topics/networking/WebSocket_Header.md)websocket客户端增加header头的链表节点。[WebSocket_RequestOptions](../../topics/networking/WebSocket_RequestOptions.md)webSocket客户端和服务端建立连接的参数。[WebSocket](../../topics/networking/WebSocket.md)webSocket客户端结构体。

#### 函数

名称typedef关键字描述[typedef void (*WebSocket_OnOpenCallback)(struct WebSocket *client, WebSocket_OpenResult openResult)](#ZH-CN_TOPIC_0000002529285451__websocket_onopencallback)WebSocket_OnOpenCallbackwebsocket客户端接收open消息的回调函数定义。[typedef void (*WebSocket_OnMessageCallback)(struct WebSocket *client, char *data, uint32_t length)](#ZH-CN_TOPIC_0000002529285451__websocket_onmessagecallback)WebSocket_OnMessageCallbackwebsocket客户端接收数据的回调函数定义。[typedef void (*WebSocket_OnErrorCallback)(struct WebSocket *client, WebSocket_ErrorResult errorResult)](#ZH-CN_TOPIC_0000002529285451__websocket_onerrorcallback)WebSocket_OnErrorCallbackwebsocket客户端接收error错误消息的回调函数定义。[typedef void (*WebSocket_OnCloseCallback)(struct WebSocket *client, WebSocket_CloseResult closeResult)](#ZH-CN_TOPIC_0000002529285451__websocket_onclosecallback)WebSocket_OnCloseCallbackwebSocket客户端接收close消息的回调函数定义。

#### 函数说明

#### WebSocket_OnOpenCallback()

```ets
typedef void (*WebSocket_OnOpenCallback)(struct WebSocket *client, WebSocket_OpenResult openResult)
```

**描述**

websocket客户端接收open消息的回调函数定义。

**起始版本：** 11

**参数：**

参数项描述[struct WebSocket](../../topics/networking/WebSocket.md) *clientwebsocket客户端。[ WebSocket_OpenResult](../../topics/networking/WebSocket_OpenResult.md) openResultwebsocket客户端接收建立连接消息的内容。

#### WebSocket_OnMessageCallback()

```ets
typedef void (*WebSocket_OnMessageCallback)(struct WebSocket *client, char *data, uint32_t length)
```

**描述**

websocket客户端接收数据的回调函数定义。

**起始版本：** 11

**参数：**

参数项描述[struct WebSocket](../../topics/networking/WebSocket.md) *clientwebsocket客户端。char *datawebsocket客户端接收的数据。uint32_t lengthwebsocket客户端接收的数据长度。

#### WebSocket_OnErrorCallback()

```ets
typedef void (*WebSocket_OnErrorCallback)(struct WebSocket *client, WebSocket_ErrorResult errorResult)
```

**描述**

websocket客户端接收error错误消息的回调函数定义。

**起始版本：** 11

**参数：**

参数项描述[struct WebSocket](../../topics/networking/WebSocket.md) *clientwebsocket客户端。[ WebSocket_ErrorResult](../../topics/networking/WebSocket_ErrorResult.md) errorResultwebsocket客户端接收连接错误消息的内容。

#### WebSocket_OnCloseCallback()

```ets
typedef void (*WebSocket_OnCloseCallback)(struct WebSocket *client, WebSocket_CloseResult closeResult)
```

**描述**

webSocket客户端接收close消息的回调函数定义。

**起始版本：** 11

**参数：**

参数项描述[struct WebSocket](../../topics/networking/WebSocket.md) *clientwebsocket客户端。[ WebSocket_CloseResult](../../topics/networking/WebSocket_CloseResult.md) closeResultwebSocket客户端接收关闭消息的内容。