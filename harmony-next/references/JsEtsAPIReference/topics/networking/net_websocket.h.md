# net_websocket.h

**概述**

定义websocket客户端模块的接口。

引用文件： <network/netstack/net_websocket.h>

库： libnet_websocket.so

系统能力： SystemCapability.Communication.NetStack

起始版本： 11

相关模块： [netstack](Netstack.md)

**汇总**

**函数**

| 名称 | 描述 |
| --- | --- |
| struct WebSocket *OH_WebSocketClient_Constructor(WebSocket_OnOpenCallback onOpen, WebSocket_OnMessageCallback onMessage,WebSocket_OnErrorCallback onError, WebSocket_OnCloseCallback onclose) | websocket客户端的构造函数。 |
| int OH_WebSocketClient_AddHeader(struct WebSocket *client, struct WebSocket_Header header) | 将header头信息添加到client客户端request中。 |
| int OH_WebSocketClient_Connect(struct WebSocket *client, const char *url, struct WebSocket_RequestOptions options) | 客户端连接服务端。 |
| int OH_WebSocketClient_Send(struct WebSocket *client, char *data, size_t length) | 客户端向服务端发送数据。 |
| int OH_WebSocketClient_Close(struct WebSocket *client, struct WebSocket_CloseOption options) | 客户端主动关闭webSocket连接。 |
| int OH_WebSocketClient_Destroy(struct WebSocket *client) | 释放websocket连接上下文和资源。 |

**函数说明**

**OH_WebSocketClient_Constructor()**

```ets
struct WebSocket *OH_WebSocketClient_Constructor(WebSocket_OnOpenCallback onOpen, WebSocket_OnMessageCallback onMessage,WebSocket_OnErrorCallback onError, WebSocket_OnCloseCallback onclose)
```

描述

websocket客户端的构造函数。

系统能力： SystemCapability.Communication.NetStack

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| WebSocket_OnOpenCallback onOpen | 客户端定义的建立连接消息的回调函数。 |
| WebSocket_OnMessageCallback onMessage | 客户端定义的接收消息的回调函数。 |
| WebSocket_OnErrorCallback onError | 客户端定义的错误消息的回调函数。 |
| WebSocket_OnCloseCallback onclose | 客户端定义的关闭消息的回调函数。 |

返回：

| 类型 | 说明 |
| --- | --- |
| struct WebSocket * | 成功返回客户端指针，失败返回为NULL。 |

**OH_WebSocketClient_AddHeader()**

```ets
int OH_WebSocketClient_AddHeader(struct WebSocket *client, struct WebSocket_Header header)
```

描述

将header头信息添加到client客户端request中。

系统能力： SystemCapability.Communication.NetStack

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| struct WebSocket *client | 客户端指针。 |
| struct WebSocket_Header header | Header头信息。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回值为0表示执行成功，返回值不为0表示失败。返回值详细信息可以查看OH_Websocket_ErrCode。 |

**OH_WebSocketClient_Connect()**

```ets
int OH_WebSocketClient_Connect(struct WebSocket *client, const char *url, struct WebSocket_RequestOptions options)
```

描述

客户端连接服务端。

系统能力： SystemCapability.Communication.NetStack

需要权限： ohos.permission.INTERNET

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| struct WebSocket *client | 客户端指针。 |
| const char *url | 客户端要连接到服务端的地址。 |
| struct WebSocket_RequestOptions options | 发起连接的可选参数。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回值为0表示执行成功，返回值不为0表示失败。返回值详细信息可以查看OH_Websocket_ErrCode。 |

**OH_WebSocketClient_Send()**

```ets
int OH_WebSocketClient_Send(struct WebSocket *client, char *data, size_t length)
```

描述

客户端向服务端发送数据。

系统能力： SystemCapability.Communication.NetStack

需要权限： ohos.permission.INTERNET

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| struct WebSocket *client | 客户端。 |
| char *data | 客户端发送的数据。 |
| size_t length | 客户端发送的数据长度。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回值为0表示执行成功，返回值不为0表示失败。返回值详细信息可以查看OH_Websocket_ErrCode。 |

**OH_WebSocketClient_Close()**

```ets
int OH_WebSocketClient_Close(struct WebSocket *client, struct WebSocket_CloseOption options)
```

描述

客户端主动关闭webSocket连接。

系统能力： SystemCapability.Communication.NetStack

需要权限： ohos.permission.INTERNET

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| struct WebSocket *client | 客户端。 |
| struct WebSocket_CloseOption options | 发起关闭连接的可选参数。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回值为0表示执行成功，返回值不为0表示失败。返回值详细信息可以查看OH_Websocket_ErrCode。 |

**OH_WebSocketClient_Destroy()**

```ets
int OH_WebSocketClient_Destroy(struct WebSocket *client)
```

描述

释放websocket连接上下文和资源。

系统能力： SystemCapability.Communication.NetStack

需要权限： ohos.permission.INTERNET

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| struct WebSocket *client | 客户端。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回值为0表示执行成功，返回值不为0表示失败。返回值详细信息可以查看OH_Websocket_ErrCode。 |