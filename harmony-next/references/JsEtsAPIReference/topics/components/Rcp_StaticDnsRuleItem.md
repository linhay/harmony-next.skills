# Rcp_StaticDnsRuleItem

#### 概述

描述单个静态DNS规则。

**起始版本：** 5.0.0(12)

**相关模块：**[RemoteCommunication](../misc/RemoteCommunication.md)

#### 汇总

#### 成员变量

名称

描述

char [host](Rcp_StaticDnsRuleItem.md#ZH-CN_TOPIC_0000002317039125__a1d3b3f7dce4d6bc4cca968d9c039d4f0) [[RCP_HOST_MAX_LEN](../misc/RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__gaf8dd4d8c5c99712c29f29211ad2a76ae)]

主机名。

uint16_t [port](Rcp_StaticDnsRuleItem.md#ZH-CN_TOPIC_0000002317039125__a1171cd3cf4b10f590075fc44b62a6329)

端口号。范围： [0, 65535]。

[Rcp_IpAddress](../misc/Rcp_IpAddress.md) * [ipAddresses](Rcp_StaticDnsRuleItem.md#ZH-CN_TOPIC_0000002317039125__a1e201db9dd01adb4c6790dea4fd8b572)

表示[Rcp_StaticDnsRuleItem.host](Rcp_StaticDnsRuleItem.md#ZH-CN_TOPIC_0000002317039125__a1d3b3f7dce4d6bc4cca968d9c039d4f0)对应的IP地址。

#### 结构体成员变量说明

#### host

```ets
char Rcp_StaticDnsRuleItem::host[[RCP_HOST_MAX_LEN](../misc/RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__gaf8dd4d8c5c99712c29f29211ad2a76ae)]
```

**描述**

主机名。

#### ipAddresses

```ets
[Rcp_IpAddress](../misc/Rcp_IpAddress.md)* Rcp_StaticDnsRuleItem::ipAddresses
```

**描述**

表示[Rcp_StaticDnsRuleItem.host](Rcp_StaticDnsRuleItem.md#ZH-CN_TOPIC_0000002317039125__a1d3b3f7dce4d6bc4cca968d9c039d4f0)对应的IP地址。

#### port

```ets
uint16_t Rcp_StaticDnsRuleItem::port
```

**描述**

端口号。范围： [0, 65535]。