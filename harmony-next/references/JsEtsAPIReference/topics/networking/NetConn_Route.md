# NetConn_Route

```ets
typedef struct NetConn_Route {...} NetConn_Route
```

#### 概述

路由配置信息。

**起始版本：** 11

**相关模块：**[NetConnection](NetConnection.md)

**所在头文件：**[net_connection_type.h](../../capi/headers/net_connection_type.h.md)

#### 汇总

#### 成员变量

名称描述char iface[[NETCONN_MAX_STR_LEN]](net_connection_type.h.md#ZH-CN_TOPIC_0000002529285449__宏定义)网络接口[NetConn_NetAddr](NetConn_NetAddr.md) destination目标地址[NetConn_NetAddr](NetConn_NetAddr.md) gateway网关地址int32_t hasGateway是否存在网关int32_t isDefaultRoute是否是默认路由