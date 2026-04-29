# Rcp_IpAndPort

**概述**

该接口用在[Rcp_DnsServers](Rcp_DnsServers.md)中，表示一个DNS服务器的地址和端口。

起始版本： 5.0.0(12)

相关模块： [RemoteCommunication](RemoteCommunication.md)

所在头文件： [rcp.h](rcp.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| char ip [RCP_IP_MAX_LEN] | IPv4或IPv6地址。 |
| uint16_t port | 表示端口。取值范围：[0, 65535]。 |

**结构体成员变量说明**

**ip**

```ets
char Rcp_IpAndPort::ip[RCP_IP_MAX_LEN]
```

描述

IPv4或IPv6地址。

**port**

```ets
uint16_t Rcp_IpAndPort::port
```

描述

表示端口。取值范围：[0, 65535]。