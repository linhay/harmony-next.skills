# Rcp_Configuration

#### 概述

请求配置。

**起始版本：** 5.0.0(12)

**相关模块：**[RemoteCommunication](RemoteCommunication.md)

#### 汇总

#### 成员变量

名称

描述

[Rcp_TransferConfiguration](Rcp_TransferConfiguration.md)[transferConfiguration](Rcp_Configuration.md#ZH-CN_TOPIC_0000002282549692__a014070587666903f817328ffdf30852f)

传输配置。

[Rcp_TracingConfiguration](Rcp_TracingConfiguration.md)[tracingConfiguration](Rcp_Configuration.md#ZH-CN_TOPIC_0000002282549692__a279392dde3cda75cc585210dc5ec49c5)

请求追踪配置。

[Rcp_ProxyConfiguration](Rcp_ProxyConfiguration.md)[proxyConfiguration](Rcp_Configuration.md#ZH-CN_TOPIC_0000002282549692__a7280355a1d2c319acb1f37e544249d9e)

代理配置。

[Rcp_DnsConfiguration](Rcp_DnsConfiguration.md)[dnsConfiguration](Rcp_Configuration.md#ZH-CN_TOPIC_0000002282549692__a71f41dfa2cd2c2e6269c7640b83f6b40)

DNS配置。

[Rcp_SecurityConfiguration](Rcp_SecurityConfiguration.md)[securityConfiguration](Rcp_Configuration.md#ZH-CN_TOPIC_0000002282549692__a304a69af4432db3b5f38d24b7a9b3f92)

安全配置。

void * [configurationPrivate](Rcp_Configuration.md#ZH-CN_TOPIC_0000002282549692__aee2bffb54b1f4ec71c2816b85f838238)

可扩展字段。

#### 结构体成员变量说明

#### configurationPrivate

```ets
void* Rcp_Configuration::configurationPrivate
```

**描述**

可扩展字段。

#### dnsConfiguration

```ets
[Rcp_DnsConfiguration](Rcp_DnsConfiguration.md) Rcp_Configuration::dnsConfiguration
```

**描述**

DNS配置。

#### proxyConfiguration

```ets
[Rcp_ProxyConfiguration](Rcp_ProxyConfiguration.md) Rcp_Configuration::proxyConfiguration
```

**描述**

代理配置。

#### securityConfiguration

```ets
[Rcp_SecurityConfiguration](Rcp_SecurityConfiguration.md) Rcp_Configuration::securityConfiguration
```

**描述**

安全配置。

#### tracingConfiguration

```ets
[Rcp_TracingConfiguration](Rcp_TracingConfiguration.md) Rcp_Configuration::tracingConfiguration
```

**描述**

请求追踪配置。

#### transferConfiguration

```ets
[Rcp_TransferConfiguration](Rcp_TransferConfiguration.md) Rcp_Configuration::transferConfiguration
```

**描述**

传输配置。