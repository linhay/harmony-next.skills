# WebSocket_CloseOption

```ets
struct WebSocket_CloseOption {...}
```

#### 概述

websocket客户端主动关闭的参数。

**起始版本：** 11

**相关模块：**[netstack](Netstack.md)

**所在头文件：**[net_websocket_type.h](../../capi/headers/net_websocket_type.h.md)

#### 汇总

#### 成员变量

名称描述uint32_t code错误值。const char *reason错误原因。