# NetConn_TraceRouteInfo

```ets
typedef struct NetConn_TraceRouteInfo {...} NetConn_TraceRouteInfo
```

#### 概述

定义跟踪路由信息。

**起始版本：** 20

**相关模块：**[NetConnection](NetConnection.md)

**所在头文件：**[net_connection_type.h](../../capi/headers/net_connection_type.h.md)

#### 汇总

#### 成员变量

名称描述uint8_t jumpNo跳数。char address[[NETCONN_MAX_STR_LEN]](net_connection_type.h.md#ZH-CN_TOPIC_0000002529285449__宏定义)主机名或地址。uint32_t rtt[[NETCONN_MAX_RTT_NUM]](net_connection_type.h.md#ZH-CN_TOPIC_0000002529285449__宏定义)往返时间（单位：毫秒)，包含最大、最小、平均、标准差。