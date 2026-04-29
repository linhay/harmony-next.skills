# Http_ClientCert

```ets
typedef struct Http_ClientCert {...} Http_ClientCert
```

#### 概述

发送到服务端的客户端证书配置，服务端将通过客户端证书校验客户端身份。

**起始版本：** 20

**相关模块：**[netstack](Netstack.md)

所在头文件： [net_http_type.h](net_http_type.h.md)

#### 汇总

#### 成员变量

| 名称 | 描述 |
| --- | --- |
| char *certPath | 证书路径。 |
| [Http_CertType](net_http_type.h.md#ZH-CN_TOPIC_0000002497605460__http_certtype) type | 证书类型，默认是PEM，参考Http_CertType。 |
| char *keyPath | 证书密钥的路径。 |
| char *keyPassword | 证书密钥的密码。 |
