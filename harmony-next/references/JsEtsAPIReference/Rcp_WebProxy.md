# Rcp_WebProxy

#### 概述

自定义代理配置。

**起始版本：** 5.0.0(12)

**相关模块：**[RemoteCommunication](RemoteCommunication.md)

#### 汇总

#### 成员变量

名称

描述

const char * [url](Rcp_WebProxy.md#ZH-CN_TOPIC_0000002282446446__a16daba15d11690d1213ab06b6d037865)

代理服务器的URL。如果您没有明确设置端口，则端口将为1080。

[Rcp_ProxyTunnelMode](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga7ae11929cb19cd85be3dd97e712e2ac6)[createTunnel](Rcp_WebProxy.md#ZH-CN_TOPIC_0000002282446446__acacb9b6bb4c814b12b1aac1df60a873f)

用于控制何时创建代理隧道。

[Rcp_Exclusions](Rcp_Exclusions.md)[exclusions](Rcp_WebProxy.md#ZH-CN_TOPIC_0000002282446446__a11817f43fef6b3e1afc3c9539f5b7808)

如果[Rcp_Request.url](Rcp_Request.md#ZH-CN_TOPIC_0000002317039157__a39a1cc0a1ad666d8d9ad40eec4b52de7)匹配[Rcp_Exclusions](Rcp_Exclusions.md)规则，则[Rcp_Request](Rcp_Request.md)将不使用代理。

[Rcp_SecurityConfiguration](Rcp_SecurityConfiguration.md)[securityConfiguration](Rcp_WebProxy.md#ZH-CN_TOPIC_0000002282446446__acc58f45a01e990be428e5eb7d660d417)

代理中的[Rcp_SecurityConfiguration](Rcp_SecurityConfiguration.md)。

#### 结构体成员变量说明

#### createTunnel

```ets
[Rcp_ProxyTunnelMode](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga7ae11929cb19cd85be3dd97e712e2ac6) Rcp_WebProxy::createTunnel
```

**描述**

用于控制何时创建代理隧道。

#### exclusions

```ets
[Rcp_Exclusions](Rcp_Exclusions.md) Rcp_WebProxy::exclusions
```

**描述**

如果[Rcp_Request.url](Rcp_Request.md#ZH-CN_TOPIC_0000002317039157__a39a1cc0a1ad666d8d9ad40eec4b52de7)匹配[Rcp_Exclusions](Rcp_Exclusions.md)规则，则[Rcp_Request](Rcp_Request.md)将不使用代理。

#### securityConfiguration

```ets
[Rcp_SecurityConfiguration](Rcp_SecurityConfiguration.md) Rcp_WebProxy::securityConfiguration
```

**描述**

代理中的[Rcp_SecurityConfiguration](Rcp_SecurityConfiguration.md)。

#### url

```ets
const char* Rcp_WebProxy::url
```

**描述**

代理服务器的URL。如果您没有明确设置端口，则端口将为1080。