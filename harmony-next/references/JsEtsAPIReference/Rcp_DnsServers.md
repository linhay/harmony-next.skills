# Rcp_DnsServers

#### 概述

DNS服务器。[Rcp_DnsConfiguration.dnsRules](Rcp_DnsConfiguration.md#ZH-CN_TOPIC_0000002317126061__ab09aacb68c682d9beea100cae481eaa4)中的类型之一。

**起始版本：** 5.0.0(12)

**相关模块：**[RemoteCommunication](RemoteCommunication.md)

#### 汇总

#### 成员变量

名称

描述

[Rcp_IpAndPort](Rcp_IpAndPort.md)[ipAndPort](Rcp_DnsServers.md#ZH-CN_TOPIC_0000002317039149__a4cd8b8fb177386081b28758bb0b2f97c)

IP和端口。

struct [Rcp_DnsServers](Rcp_DnsServers.md) * [next](Rcp_DnsServers.md#ZH-CN_TOPIC_0000002317039149__a89103c531bba6cd8cf60fd5d30dba8ef)

链式存储。指向下一个[Rcp_DnsServers](Rcp_DnsServers.md)的指针。

#### 结构体成员变量说明

#### ipAndPort

```ets
[Rcp_IpAndPort](Rcp_IpAndPort.md) Rcp_DnsServers::ipAndPort
```

**描述**

IP和端口。

#### next

```ets
struct [Rcp_DnsServers](Rcp_DnsServers.md)* Rcp_DnsServers::next
```

**描述**

链式存储。指向下一个[Rcp_DnsServers](Rcp_DnsServers.md)的指针。