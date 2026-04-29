# NetConn_NetAddr

```ets
typedef struct NetConn_NetAddr {...} NetConn_NetAddr
```

#### 概述

网络地址。

**起始版本：** 11

**相关模块：**[NetConnection](NetConnection.md)

所在头文件： [net_connection_type.h](net_connection_type.h.md)

#### 汇总

#### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint8_t family | 网络地址族。 |
| uint8_t prefixlen | 前缀长度。 |
| uint8_t port | 端口号。 |
| char address[NETCONN_MAX_STR_LEN] | 地址。 |