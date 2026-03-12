# Rcp_ServerAuthentication

#### 概述

服务器身份验证。

**起始版本：** 5.0.0(12)

**相关模块：**[RemoteCommunication](RemoteCommunication.md)

#### 汇总

#### 成员变量

名称

描述

[Rcp_Credential](Rcp_Credential.md)[credential](Rcp_ServerAuthentication.md#ZH-CN_TOPIC_0000002282446418__a01fbe231a7a2302e66e9582d617ef73b)

服务器的凭据。

[Rcp_AuthenticationType](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__gaa1b9ec2bd61b2c95492f45eb0a447bff)[authenticationType](Rcp_ServerAuthentication.md#ZH-CN_TOPIC_0000002282446418__accd28314a33f1ded057b40e33322292a)

服务器的身份验证类型。如果未设置，请与服务器协商。

#### 结构体成员变量说明

#### authenticationType

```ets
[Rcp_AuthenticationType](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__gaa1b9ec2bd61b2c95492f45eb0a447bff) Rcp_ServerAuthentication::authenticationType
```

**描述**

服务器的身份验证类型。如果未设置，请与服务器协商。

#### credential

```ets
[Rcp_Credential](Rcp_Credential.md) Rcp_ServerAuthentication::credential
```

**描述**

服务器的凭据。