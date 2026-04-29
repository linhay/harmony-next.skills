# NetConn_TraceRouteInfo

```ets
typedef struct NetConn_TraceRouteInfo {...} NetConn_TraceRouteInfo
```

#### 概述

定义跟踪路由信息。

**起始版本：** 20

**相关模块：**[NetConnection](NetConnection.md)

所在头文件： [net_connection_type.h](net_connection_type.h.md)

#### 汇总

#### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint8_t jumpNo | 跳数。 |
| char address[NETCONN_MAX_STR_LEN] | 主机名或地址。 |
| uint32_t rtt[NETCONN_MAX_RTT_NUM] | 往返时间（单位：毫秒)，包含最大、最小、平均、标准差。 |