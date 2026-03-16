# net_ssl_c_type.h

#### 概述

定义SSL/TLS证书链校验模块的C接口需要的数据结构。

**引用文件：** <network/netstack/net_ssl/net_ssl_c_type.h>

**库：** libnet_ssl.so

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 11

**相关模块：**[netstack](../../topics/networking/Netstack.md)

#### 汇总

#### 结构体

名称typedef关键字描述[NetStack_CertBlob](../../topics/networking/NetStack_CertBlob.md)-证书数据结构体。[NetStack_CertificatePinning](../../topics/networking/NetStack_CertificatePinning.md)NetStack_CertificatePinning定义证书锁定信息。[NetStack_Certificates](../../topics/networking/NetStack_Certificates.md)NetStack_Certificates定义证书信息。

#### 枚举

名称typedef关键字描述[NetStack_CertType](#ZH-CN_TOPIC_0000002497605458__netstack_certtype)-证书类型枚举。[NetStack_CertificatePinningKind](#ZH-CN_TOPIC_0000002497605458__netstack_certificatepinningkind)NetStack_CertificatePinningKind定义证书锁定类型枚举。[NetStack_HashAlgorithm](#ZH-CN_TOPIC_0000002497605458__netstack_hashalgorithm)NetStack_HashAlgorithm定义哈希算法。

#### 枚举类型说明

#### NetStack_CertType

```ets
enum NetStack_CertType
```

**描述**

证书类型枚举。

**起始版本：** 11

枚举项描述NETSTACK_CERT_TYPE_PEM = 0PEM证书类型NETSTACK_CERT_TYPE_DER = 1DER证书类型NETSTACK_CERT_TYPE_INVALID错误证书类型

#### NetStack_CertificatePinningKind

```ets
enum NetStack_CertificatePinningKind
```

**描述**

定义证书锁定类型枚举。

**起始版本：** 12

枚举项描述PUBLIC_KEY公钥锁定类型

#### NetStack_HashAlgorithm

```ets
enum NetStack_HashAlgorithm
```

**描述**

定义哈希算法。

**起始版本：** 12

枚举项描述SHA_256Sha256