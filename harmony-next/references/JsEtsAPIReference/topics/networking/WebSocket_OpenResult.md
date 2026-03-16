# WebSocket_OpenResult

```ets
struct WebSocket_OpenResult {...}
```

#### 概述

websocket客户端来自服务端连接成功的参数。

**起始版本：** 11

**相关模块：**[netstack](Netstack.md)

**所在头文件：**[net_websocket_type.h](../../capi/headers/net_websocket_type.h.md)

#### 汇总

#### 成员变量

名称描述uint32_t codewebsocket客户端连接成功码。const char *reasonwebsocket客户端连接成功原因。