# NetConn_NetConnCallback

```ets
typedef struct NetConn_NetConnCallback {...} NetConn_NetConnCallback
```

#### 概述

网络状态监听回调集合。

**起始版本：** 12

**相关模块：**[NetConnection](NetConnection.md)

**所在头文件：**[net_connection_type.h](net_connection_type.h.md)

#### 汇总

#### 成员变量

名称描述[OH_NetConn_NetworkAvailable](net_connection_type.h.md#ZH-CN_TOPIC_0000002529285449__oh_netconn_networkavailable) onNetworkAvailable网络可用回调。[OH_NetConn_NetCapabilitiesChange](net_connection_type.h.md#ZH-CN_TOPIC_0000002529285449__oh_netconn_netcapabilitieschange) onNetCapabilitiesChange网络能力集变更回调。[OH_NetConn_NetConnectionPropertiesChange](net_connection_type.h.md#ZH-CN_TOPIC_0000002529285449__oh_netconn_netconnectionpropertieschange) onConnetionProperties网络连接属性变更回调。[OH_NetConn_NetLost](net_connection_type.h.md#ZH-CN_TOPIC_0000002529285449__oh_netconn_netlost) onNetLost网络断开回调。[OH_NetConn_NetUnavailable](net_connection_type.h.md#ZH-CN_TOPIC_0000002529285449__oh_netconn_netunavailable) onNetUnavailable网络不可用回调, 在指定的超时时间内网络未激活时触发该回调，如果未设置超时时间则不会触发该回调。[OH_NetConn_NetBlockStatusChange](net_connection_type.h.md#ZH-CN_TOPIC_0000002529285449__oh_netconn_netblockstatuschange) onNetBlockStatusChange网络阻塞状态变更回调。