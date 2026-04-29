# Rcp_Configuration

**概述**

请求配置。

起始版本： 5.0.0(12)

相关模块： [RemoteCommunication](RemoteCommunication.md)

所在头文件： [rcp.h](rcp.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| Rcp_TransferConfigurationtransferConfiguration | 传输配置。 |
| Rcp_TracingConfigurationtracingConfiguration | 请求追踪配置。 |
| Rcp_ProxyConfigurationproxyConfiguration | 代理配置。 |
| Rcp_DnsConfigurationdnsConfiguration | DNS配置。 |
| Rcp_SecurityConfigurationsecurityConfiguration | 安全配置。 |
| void * configurationPrivate | 可扩展字段。 |

**结构体成员变量说明**

**configurationPrivate**

```ets
void* Rcp_Configuration::configurationPrivate
```

描述

可扩展字段。

**dnsConfiguration**

```ets
Rcp_DnsConfiguration Rcp_Configuration::dnsConfiguration
```

描述

DNS配置。

**proxyConfiguration**

```ets
Rcp_ProxyConfiguration Rcp_Configuration::proxyConfiguration
```

描述

代理配置。

**securityConfiguration**

```ets
Rcp_SecurityConfiguration Rcp_Configuration::securityConfiguration
```

描述

安全配置。

**tracingConfiguration**

```ets
Rcp_TracingConfiguration Rcp_Configuration::tracingConfiguration
```

描述

请求追踪配置。

**transferConfiguration**

```ets
Rcp_TransferConfiguration Rcp_Configuration::transferConfiguration
```

描述

传输配置。