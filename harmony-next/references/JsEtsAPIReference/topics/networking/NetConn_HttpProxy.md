# NetConn_HttpProxy

```ets
typedef struct NetConn_HttpProxy {...} NetConn_HttpProxy
```

#### 概述

代理配置信息。

**起始版本：** 11

**相关模块：**[NetConnection](NetConnection.md)

**所在头文件：**[net_connection_type.h](../../capi/headers/net_connection_type.h.md)

#### 汇总

#### 成员变量

名称描述char host[[NETCONN_MAX_STR_LEN]](net_connection_type.h.md#ZH-CN_TOPIC_0000002529285449__宏定义)主机名。char exclusionList[[NETCONN_MAX_EXCLUSION_SIZE]](net_connection_type.h.md#ZH-CN_TOPIC_0000002529285449__宏定义)[[NETCONN_MAX_STR_LEN]](net_connection_type.h.md#ZH-CN_TOPIC_0000002529285449__宏定义)代理服务器的排除列表。int32_t exclusionListSize排除列表的实际大小。uint16_t port端口号。