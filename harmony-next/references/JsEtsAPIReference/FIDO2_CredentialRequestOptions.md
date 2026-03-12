# FIDO2_CredentialRequestOptions

#### 概述

认证信息字典对象。

**起始版本：** 6.0.0(20)

**相关模块：**[FIDO2](通行密钥.md)

#### 汇总

#### 成员变量

名称

描述

[FIDO2_CredentialMediationRequirement](通行密钥.md#ZH-CN_TOPIC_0000002523299537__ga16035d1941d25a1ea71203ad72809b93)[mediation](FIDO2_CredentialRequestOptions.md#ZH-CN_TOPIC_0000002490979830__a6df6ad2781b6259aabaa3762a9986270)

操作是否需要用户参与。

[FIDO2_PublicKeyCredentialRequestOptions](FIDO2_PublicKeyCredentialRequestOptions.md)[publicKey](FIDO2_CredentialRequestOptions.md#ZH-CN_TOPIC_0000002490979830__a2a422b8e07f1a596cd9c90afd244c54e)

publicKey凭证请求的选项。

#### 结构体成员变量说明

#### mediation

```ets
[FIDO2_CredentialMediationRequirement](通行密钥.md#ZH-CN_TOPIC_0000002523299537__ga16035d1941d25a1ea71203ad72809b93) FIDO2_CredentialRequestOptions::mediation
```

**描述**

用户介入要求。

#### publicKey

```ets
[FIDO2_PublicKeyCredentialRequestOptions](FIDO2_PublicKeyCredentialRequestOptions.md) FIDO2_CredentialRequestOptions::publicKey
```

**描述**

publicKey凭证请求的选项。