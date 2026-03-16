# Http_ClientCert

```ets
typedef struct Http_ClientCert {...} Http_ClientCert
```

#### 概述

发送到服务端的客户端证书配置，服务端将通过客户端证书校验客户端身份。

**起始版本：** 20

**相关模块：**[netstack](Netstack.md)

**所在头文件：**[net_http_type.h](../../capi/headers/net_http_type.h.md)

#### 汇总

#### 成员变量

名称描述char *certPath证书路径。[Http_CertType](../../capi/headers/net_http_type.h.md#ZH-CN_TOPIC_0000002497605460__http_certtype) type证书类型，默认是PEM，参考[Http_CertType](../../capi/headers/net_http_type.h.md#ZH-CN_TOPIC_0000002497605460__http_certtype)。char *keyPath证书密钥的路径。char *keyPassword证书密钥的密码。