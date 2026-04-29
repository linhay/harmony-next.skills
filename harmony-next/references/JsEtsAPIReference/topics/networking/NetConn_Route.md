# NetConn_Route

```ets
typedef struct NetConn_Route {...} NetConn_Route
```

#### 概述

路由配置信息。

**起始版本：** 11

**相关模块：**[NetConnection](NetConnection.md)

所在头文件： [net_connection_type.h](net_connection_type.h.md)

#### 汇总

#### 成员变量

| 名称 | 描述 |
| --- | --- |
| char iface[NETCONN_MAX_STR_LEN] | 网络接口 |
| [NetConn_NetAddr](NetConn_NetAddr.md) destination | 目标地址 |
| [NetConn_NetAddr](NetConn_NetAddr.md) gateway | 网关地址 |
| int32_t hasGateway | 是否存在网关 |
| int32_t isDefaultRoute | 是否是默认路由 |
