# net_ssl_c_type.h

**概述**

定义SSL/TLS证书链校验模块的C接口需要的数据结构。

引用文件： <network/netstack/net_ssl/net_ssl_c_type.h>

库： libnet_ssl.so

系统能力： SystemCapability.Communication.NetStack

起始版本： 11

相关模块： [netstack](Netstack.md)

**汇总**

**结构体**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| NetStack_CertBlob | - | 证书数据结构体。 |
| NetStack_CertificatePinning | NetStack_CertificatePinning | 定义证书锁定信息。 |
| NetStack_Certificates | NetStack_Certificates | 定义证书信息。 |

**枚举**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| NetStack_CertType | - | 证书类型枚举。 |
| NetStack_CertificatePinningKind | NetStack_CertificatePinningKind | 定义证书锁定类型枚举。 |
| NetStack_HashAlgorithm | NetStack_HashAlgorithm | 定义哈希算法。 |

**枚举类型说明**

**NetStack_CertType**

```ets
enum NetStack_CertType
```

描述

证书类型枚举。

起始版本： 11

| 枚举项 | 描述 |
| --- | --- |
| NETSTACK_CERT_TYPE_PEM = 0 | PEM证书类型 |
| NETSTACK_CERT_TYPE_DER = 1 | DER证书类型 |
| NETSTACK_CERT_TYPE_INVALID | 错误证书类型 |

**NetStack_CertificatePinningKind**

```ets
enum NetStack_CertificatePinningKind
```

描述

定义证书锁定类型枚举。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| PUBLIC_KEY | 公钥锁定类型 |

**NetStack_HashAlgorithm**

```ets
enum NetStack_HashAlgorithm
```

描述

定义哈希算法。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| SHA_256 | Sha256 |