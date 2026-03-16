# Rcp_DnsOverHttps

#### 概述

HTTPS上的DNS配置如果设置，则首选由DOH dns服务器解析的地址。

**起始版本：** 5.0.0(12)

**相关模块：**[RemoteCommunication](../misc/RemoteCommunication.md)

#### 汇总

#### 成员变量

名称

描述

const char * [url](Rcp_DnsOverHttps.md#ZH-CN_TOPIC_0000002282549696__a0fc9b58ce0b550bc7dc5b5b1bbacb69d)

DOH服务器的URL。

bool [skipCertificatesValidation](Rcp_DnsOverHttps.md#ZH-CN_TOPIC_0000002282549696__acb53e2ac8bdc62816a7046c8d40d6173)

判断是否跳过证书验证。默认值为false。

#### 结构体成员变量说明

#### skipCertificatesValidation

```ets
bool Rcp_DnsOverHttps::skipCertificatesValidation
```

**描述**

判断是否跳过证书验证。默认值为false。

#### url

```ets
const char* Rcp_DnsOverHttps::url
```

**描述**

DOH服务器的URL。