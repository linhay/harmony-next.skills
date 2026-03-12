# Rcp_SecurityConfiguration

#### 概述

请求的安全配置。

**起始版本：** 5.0.0(12)

**相关模块：**[RemoteCommunication](RemoteCommunication.md)

#### 汇总

#### 成员变量

名称

描述

[Rcp_RemoteValidationType](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__gaf9356aea6a8c2e447efe3cf7fa889b87)[remoteValidationType](Rcp_SecurityConfiguration.md#ZH-CN_TOPIC_0000002282446426__a2b5f2905c3e2f904ec9b2820ae39f367)

远端认证方法类型。

[Rcp_CertificateAuthority](Rcp_CertificateAuthority.md)[certificateAuthority](Rcp_SecurityConfiguration.md#ZH-CN_TOPIC_0000002282446426__a341651044da2a76bbb5eb9126b49b709)

用于验证远程服务器标识的证书颁发机构（CA）。默认值为“system”，如果未设置此字段，将使用system CA验证远程服务器的标识。

[Rcp_ClientCertificate](Rcp_ClientCertificate.md)[certificate](Rcp_SecurityConfiguration.md#ZH-CN_TOPIC_0000002282446426__aed7e691dbb64dcfbd4935eced4099de6)

发送到远程服务器的客户端证书，远程服务器将使用它来验证客户端的标识。

[Rcp_ServerAuthentication](Rcp_ServerAuthentication.md)[serverAuthentication](Rcp_SecurityConfiguration.md#ZH-CN_TOPIC_0000002282446426__a9e6d74aa37d2118852bf780075d466c0)

服务器身份验证设置。默认情况下不进行身份验证。

#### 结构体成员变量说明

#### certificate

```ets
[Rcp_ClientCertificate](Rcp_ClientCertificate.md) Rcp_SecurityConfiguration::certificate
```

**描述**

发送到远程服务器的客户端证书，远程服务器将使用它来验证客户端的标识。

#### certificateAuthority

```ets
[Rcp_CertificateAuthority](Rcp_CertificateAuthority.md) Rcp_SecurityConfiguration::certificateAuthority
```

**描述**

用于验证远程服务器标识的证书颁发机构（CA）。默认值为“system”，如果未设置此字段，将使用system CA验证远程服务器的标识。

#### remoteValidationType

```ets
[Rcp_RemoteValidationType](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__gaf9356aea6a8c2e447efe3cf7fa889b87) Rcp_SecurityConfiguration::remoteValidationType
```

**描述**

远端认证方法类型。

#### serverAuthentication

```ets
[Rcp_ServerAuthentication](Rcp_ServerAuthentication.md) Rcp_SecurityConfiguration::serverAuthentication
```

**描述**

服务器身份验证设置。默认情况下不进行身份验证。