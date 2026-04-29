# NetConn_HttpProxy

```ets
typedef struct NetConn_HttpProxy {...} NetConn_HttpProxy
```

#### 概述

代理配置信息。

**起始版本：** 11

**相关模块：**[NetConnection](NetConnection.md)

所在头文件： [net_connection_type.h](net_connection_type.h.md)

#### 汇总

#### 成员变量

| 名称 | 描述 |
| --- | --- |
| char host[NETCONN_MAX_STR_LEN] | 主机名。 |
| char exclusionList[NETCONN_MAX_EXCLUSION_SIZE][NETCONN_MAX_STR_LEN] | 代理服务器的排除列表。 |
| int32_t exclusionListSize | 排除列表的实际大小。 |
| uint16_t port | 端口号。 |