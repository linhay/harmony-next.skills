# NetStack_CertificatePinning

```ets
typedef struct NetStack_CertificatePinning {...} NetStack_CertificatePinning
```

#### 概述

定义证书锁定信息。

**起始版本：** 12

**相关模块：**[netstack](Netstack.md)

所在头文件： [net_ssl_c_type.h](net_ssl_c_type.h.md)

#### 汇总

#### 成员变量

| 名称 | 描述 |
| --- | --- |
| [NetStack_CertificatePinningKind](net_ssl_c_type.h.md#ZH-CN_TOPIC_0000002497605458__netstack_certificatepinningkind) kind | 证书锁定类型。 |
| [NetStack_HashAlgorithm](net_ssl_c_type.h.md#ZH-CN_TOPIC_0000002497605458__netstack_hashalgorithm) hashAlgorithm | 哈希算法。 |
| char *publicKeyHash | 哈希值。 |
