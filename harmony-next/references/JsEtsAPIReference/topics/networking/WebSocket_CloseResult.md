# WebSocket_CloseResult

```ets
struct WebSocket_CloseResult {...}
```

#### 概述

websocket客户端接收到服务端关闭的参数。

**起始版本：** 11

**相关模块：**[netstack](Netstack.md)

所在头文件： [net_websocket_type.h](net_websocket_type.h.md)

#### 汇总

#### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint32_t code | 错误值。 |
| const char *reason | 错误原因。 |