# Rcp_DnsRule

#### 概述

DNS规则配置。

**起始版本：** 5.0.0(12)

**相关模块：**[RemoteCommunication](RemoteCommunication.md)

#### 汇总

#### 成员变量

名称

描述

[Rcp_DnsRuleType](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga995c92778c5b31c9b4b586c737cfdd3c)[type](Rcp_DnsRule.md#ZH-CN_TOPIC_0000002317039153__aaeb277a1dfd6466a972da818b6967203)

表示union中使用的数据类型。

****union {

union结构。data中使用的数据由type进行区分。

[Rcp_DnsServers](Rcp_DnsServers.md) * [dnsServers](Rcp_DnsRule.md#ZH-CN_TOPIC_0000002317039153__a652a56e711427feec1cc98d291958d8e)

dnsServers：DNS服务器。

[Rcp_StaticDnsRule](Rcp_StaticDnsRule.md) * [staticDnsRule](Rcp_DnsRule.md#ZH-CN_TOPIC_0000002317039153__a3a84de8e04f9875303db8047fe7461c5)

staticDnsRule：静态DNS规则。

[Rcp_DynamicDnsRuleFunction](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__gad0ace0c83dd20972b34ff1538700eab3)[dynamicDnsRule](Rcp_DnsRule.md#ZH-CN_TOPIC_0000002317039153__a6609c6f2fb05f16974b745b6738d1448)

dynamicDnsRule：动态DNS规则。

} **data**

data中使用的数据由type进行区分。

#### 结构体成员变量说明

#### dnsServers

```ets
[Rcp_DnsServers](Rcp_DnsServers.md)* Rcp_DnsRule::dnsServers
```

**描述**

DNS服务器。

#### dynamicDnsRule

```ets
[Rcp_DynamicDnsRuleFunction](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__gad0ace0c83dd20972b34ff1538700eab3) Rcp_DnsRule::dynamicDnsRule
```

**描述**

动态DNS规则。

#### staticDnsRule

```ets
[Rcp_StaticDnsRule](Rcp_StaticDnsRule.md)* Rcp_DnsRule::staticDnsRule
```

**描述**

静态DNS规则。

#### type

```ets
[Rcp_DnsRuleType](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga995c92778c5b31c9b4b586c737cfdd3c) Rcp_DnsRule::type
```

**描述**

表示union中使用的数据类型。