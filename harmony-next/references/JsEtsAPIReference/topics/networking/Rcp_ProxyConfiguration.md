# Rcp_ProxyConfiguration

#### 概述

代理配置。

**起始版本：** 5.0.0(12)

相关模块： [RemoteCommunication](RemoteCommunication.md)

所在头文件： [rcp.h](rcp.h.md)

#### 汇总

#### 成员变量

| 名称 | 描述 |
| --- | --- |
| [Rcp_ProxyType](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__gacfad61d189683cbc02c969a63e246ca1)[proxyType](Rcp_ProxyConfiguration.md#ZH-CN_TOPIC_0000002317126049__a70883d9a11b3be0fbe4321f3c43d400b) | 区分请求使用的代理类型。 |
| [Rcp_WebProxy](Rcp_WebProxy.md)[customProxy](Rcp_ProxyConfiguration.md#ZH-CN_TOPIC_0000002317126049__a01dc17cde923a3499c90dd116ad68468) | 自定义代理配置，参见Rcp_WebProxy。 |

#### 结构体成员变量说明

#### [customProxy](Rcp_ProxyConfiguration.md#ZH-CN_TOPIC_0000002317126049__a01dc17cde923a3499c90dd116ad68468)

```ets
[Rcp_WebProxy](Rcp_WebProxy.md) Rcp_ProxyConfiguration::customProxy
```

**描述**

自定义代理配置，参见[Rcp_WebProxy](Rcp_WebProxy.md)。

#### [proxyType](Rcp_ProxyConfiguration.md#ZH-CN_TOPIC_0000002317126049__a70883d9a11b3be0fbe4321f3c43d400b)

```ets
[Rcp_ProxyType](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__gacfad61d189683cbc02c969a63e246ca1) Rcp_ProxyConfiguration::proxyType
```

**描述**

区分请求使用的代理类型。
