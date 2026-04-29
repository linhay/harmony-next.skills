# Rcp_ClientCertificate

**概述**

发送到远程服务器的客户端证书，远程服务器将使用它来验证客户端的标识。

起始版本： 5.0.0(12)

相关模块： [RemoteCommunication](RemoteCommunication.md)

所在头文件： [rcp.h](rcp.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| char * content | 客户端证书内容。它应采用“PEM”、“DER”或“P12”格式。 |
| char * filePath | 客户端证书的路径。文件的格式应为“PEM”、“DER”或“P12”格式。 |
| char * key | 客户端证书私钥的文件名。 |
| char * keyPassword | 客户端证书私钥的密码。 |
| Rcp_CertTypetype | 客户端证书类型。 |

**结构体成员变量说明**

**content**

```ets
char* Rcp_ClientCertificate::content
```

描述

客户端证书内容。它应采用“PEM”、“DER”或“P12”格式。

**filePath**

```ets
char* Rcp_ClientCertificate::filePath
```

描述

客户端证书的路径。文件的格式应为“PEM”、“DER”或“P12”格式。

**key**

```ets
char* Rcp_ClientCertificate::key
```

描述

客户端证书私钥的文件名。

**keyPassword**

```ets
char* Rcp_ClientCertificate::keyPassword
```

描述

客户端证书私钥的密码。

**type**

```ets
Rcp_CertType Rcp_ClientCertificate::type
```

描述

客户端证书类型。