# Rcp_DnsConfiguration

#### 概述

DNS解析配置。

**起始版本：** 5.0.0(12)

相关模块： [RemoteCommunication](RemoteCommunication.md)

所在头文件： [rcp.h](rcp.h.md)

#### 汇总

#### 成员变量

| 名称 | 描述 |
| --- | --- |
| [Rcp_DnsRule](Rcp_DnsRule.md) * [dnsRules](Rcp_DnsConfiguration.md#ZH-CN_TOPIC_0000002317126061__ab09aacb68c682d9beea100cae481eaa4) | DNS规则配置。 |
| [Rcp_DnsOverHttps](Rcp_DnsOverHttps.md)[dnsOverHttps](Rcp_DnsConfiguration.md#ZH-CN_TOPIC_0000002317126061__a7e3122dc7ea963e7864d4ff6c3f66f0f) | DOH配置。 |

#### 结构体成员变量说明

#### [dnsOverHttps](Rcp_DnsConfiguration.md#ZH-CN_TOPIC_0000002317126061__a7e3122dc7ea963e7864d4ff6c3f66f0f)

```ets
[Rcp_DnsOverHttps](Rcp_DnsOverHttps.md) Rcp_DnsConfiguration::dnsOverHttps
```

**描述**

DOH配置。

#### [dnsRules](Rcp_DnsConfiguration.md#ZH-CN_TOPIC_0000002317126061__ab09aacb68c682d9beea100cae481eaa4)

```ets
[Rcp_DnsRule](Rcp_DnsRule.md)* Rcp_DnsConfiguration::dnsRules
```

**描述**

DNS规则配置。

[Rcp_DnsServers](Rcp_DnsServers.md): 表示优先使用指定的dns服务器解析主机名。

[Rcp_StaticDnsRule](Rcp_StaticDnsRule.md): 表示如果主机名匹配，则优先使用指定的地址。

[Rcp_DynamicDnsRuleFunction](RemoteCommunication.md#ZH-CN_TOPIC_0000002522081538__rcp_dynamicdnsrulefunction): 表示优先使用函数中返回的地址。
