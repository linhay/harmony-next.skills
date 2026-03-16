# Rcp_IpAndPort

#### 概述

该接口用在[Rcp_DnsServers](../networking/Rcp_DnsServers.md)中，表示一个DNS服务器的地址和端口。

**起始版本：** 5.0.0(12)

**相关模块：**[RemoteCommunication](RemoteCommunication.md)

#### 汇总

#### 成员变量

名称

描述

char [ip](Rcp_IpAndPort.md#ZH-CN_TOPIC_0000002282549704__ab94eb927a982d2e062cbb4266d1f5425) [[RCP_IP_MAX_LEN](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__gaedd78171e1671e9ec89b59ecf6e96730)]

IPv4或IPv6地址。

uint16_t [port](Rcp_IpAndPort.md#ZH-CN_TOPIC_0000002282549704__acde1a98de31e0b6bcc636efd60bda511)

表示端口。取值范围：[0, 65535]。

#### 结构体成员变量说明

#### ip

```ets
char Rcp_IpAndPort::ip[[RCP_IP_MAX_LEN](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__gaedd78171e1671e9ec89b59ecf6e96730)]
```

**描述**

IPv4或IPv6地址。

#### port

```ets
uint16_t Rcp_IpAndPort::port
```

**描述**

表示端口。取值范围：[0, 65535]。