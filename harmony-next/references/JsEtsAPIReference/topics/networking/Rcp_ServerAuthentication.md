# Rcp_ServerAuthentication

**概述**

服务器身份验证。

起始版本： 5.0.0(12)

相关模块： [RemoteCommunication](RemoteCommunication.md)

所在头文件： [rcp.h](rcp.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| Rcp_Credentialcredential | 服务器的凭据。 |
| Rcp_AuthenticationTypeauthenticationType | 服务器的身份验证类型。如果未设置，请与服务器协商。 |

**结构体成员变量说明**

**authenticationType**

```ets
Rcp_AuthenticationType Rcp_ServerAuthentication::authenticationType
```

描述

服务器的身份验证类型。如果未设置，请与服务器协商。

**credential**

```ets
Rcp_Credential Rcp_ServerAuthentication::credential
```

描述

服务器的凭据。