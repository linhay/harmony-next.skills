# Rcp_SecurityConfiguration

**概述**

请求的安全配置。

起始版本： 5.0.0(12)

相关模块： [RemoteCommunication](RemoteCommunication.md)

所在头文件： [rcp.h](rcp.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| Rcp_RemoteValidationTyperemoteValidationType | 远端认证方法类型。 |
| Rcp_CertificateAuthoritycertificateAuthority | 用于验证远程服务器标识的证书颁发机构（CA）。默认值为“system”，如果未设置此字段，将使用system CA验证远程服务器的标识。 |
| Rcp_ClientCertificatecertificate | 发送到远程服务器的客户端证书，远程服务器将使用它来验证客户端的标识。 |
| Rcp_ServerAuthenticationserverAuthentication | 服务器身份验证设置。默认情况下不进行身份验证。 |

**结构体成员变量说明**

**certificate**

```ets
Rcp_ClientCertificate Rcp_SecurityConfiguration::certificate
```

描述

发送到远程服务器的客户端证书，远程服务器将使用它来验证客户端的标识。

**certificateAuthority**

```ets
Rcp_CertificateAuthority Rcp_SecurityConfiguration::certificateAuthority
```

描述

用于验证远程服务器标识的证书颁发机构（CA）。默认值为“system”，如果未设置此字段，将使用system CA验证远程服务器的标识。

**remoteValidationType**

```ets
Rcp_RemoteValidationType Rcp_SecurityConfiguration::remoteValidationType
```

描述

远端认证方法类型。

**serverAuthentication**

```ets
Rcp_ServerAuthentication Rcp_SecurityConfiguration::serverAuthentication
```

描述

服务器身份验证设置。默认情况下不进行身份验证。