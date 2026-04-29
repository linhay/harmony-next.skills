# [WebSocket_Header](WebSocket_Header.md)

```ets
struct WebSocket_Header {...}
```

#### 概述

websocket客户端增加header头的链表节点。

**起始版本：** 11

**相关模块：**[netstack](Netstack.md)

所在头文件： [net_websocket_type.h](net_websocket_type.h.md)

#### 汇总

#### 成员变量

| 名称 | 描述 |
| --- | --- |
| const char *fieldName | Header头的字段名。 |
| const char *fieldValue | Header头的字段内容。 |
| struct [WebSocket_Header](WebSocket_Header.md) *next | header头链表的next指针。 |
