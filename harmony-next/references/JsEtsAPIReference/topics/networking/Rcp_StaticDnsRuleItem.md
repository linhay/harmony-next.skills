# Rcp_StaticDnsRuleItem

**概述**

描述单个静态DNS规则。

起始版本： 5.0.0(12)

相关模块： [RemoteCommunication](RemoteCommunication.md)

所在头文件： [rcp.h](rcp.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| char host [RCP_HOST_MAX_LEN] | 主机名。 |
| uint16_t port | 端口号。范围： [0, 65535]。 |
| Rcp_IpAddress * ipAddresses | 表示Rcp_StaticDnsRuleItem.host对应的IP地址。 |

**结构体成员变量说明**

**host**

```ets
char Rcp_StaticDnsRuleItem::host[RCP_HOST_MAX_LEN]
```

描述

主机名。

**ipAddresses**

```ets
Rcp_IpAddress* Rcp_StaticDnsRuleItem::ipAddresses
```

描述

表示[Rcp_StaticDnsRuleItem.host](#ZH-CN_TOPIC_0000002553361481__host)对应的IP地址。

**port**

```ets
uint16_t Rcp_StaticDnsRuleItem::port
```

描述

端口号。范围： [0, 65535]。