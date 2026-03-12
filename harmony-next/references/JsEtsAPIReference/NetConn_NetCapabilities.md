# NetConn_NetCapabilities

```ets
typedef struct NetConn_NetCapabilities {...} NetConn_NetCapabilities
```

#### 概述

网络能力集。

**起始版本：** 11

**相关模块：**[NetConnection](NetConnection.md)

**所在头文件：**[net_connection_type.h](net_connection_type.h.md)

#### 汇总

#### 成员变量

名称描述uint32_t linkUpBandwidthKbps上行带宽。uint32_t linkDownBandwidthKbps下行带宽。[NetConn_NetCap](net_connection_type.h.md#ZH-CN_TOPIC_0000002529285449__netconn_netcap) netCaps[[NETCONN_MAX_CAP_SIZE]](net_connection_type.h.md#ZH-CN_TOPIC_0000002529285449__宏定义)网络能力列表。int32_t netCapsSize网络能力列表的实际size。[NetConn_NetBearerType](net_connection_type.h.md#ZH-CN_TOPIC_0000002529285449__netconn_netbearertype) bearerTypes[[NETCONN_MAX_BEARER_TYPE_SIZE]](net_connection_type.h.md#ZH-CN_TOPIC_0000002529285449__宏定义)承载类型列表int32_t bearerTypesSize承载类型列表的实际size