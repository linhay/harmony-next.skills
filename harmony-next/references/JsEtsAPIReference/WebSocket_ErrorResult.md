# WebSocket_ErrorResult

```ets
struct WebSocket_ErrorResult {...}
```

#### 概述

websocket客户端来自服务端连接错误的参数。

**起始版本：** 11

**相关模块：**[netstack](Netstack.md)

**所在头文件：**[net_websocket_type.h](net_websocket_type.h.md)

#### 汇总

#### 成员变量

名称描述uint32_t errorCode错误码。const char *errorMessage错误的消息。