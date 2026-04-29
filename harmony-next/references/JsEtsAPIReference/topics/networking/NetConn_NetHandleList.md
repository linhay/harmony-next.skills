# NetConn_NetHandleList

```ets
typedef struct NetConn_NetHandleList {...} NetConn_NetHandleList
```

**概述**

网络列表。

起始版本： 11

相关模块： [NetConnection](NetConnection.md)

所在头文件： [net_connection_type.h](net_connection_type.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| NetConn_NetHandle netHandles[NETCONN_MAX_NET_SIZE] | netHandle列表。 |
| int32_t netHandleListSize | netHandleList的实际大小。 |