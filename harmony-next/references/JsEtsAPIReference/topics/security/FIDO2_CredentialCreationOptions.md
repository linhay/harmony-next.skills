# FIDO2_CredentialCreationOptions

#### 概述

凭据请求的选项。

**起始版本：** 6.0.0(20)

相关模块： [FIDO2](通行密钥.md)

#### 汇总

#### 成员变量

| 名称 | 描述 |
| --- | --- |
| [FIDO2_CredentialMediationRequirement](../security/通行密钥.md#ZH-CN_TOPIC_0000002523299537__ga16035d1941d25a1ea71203ad72809b93) [mediation](FIDO2_CredentialCreationOptions.md#ZH-CN_TOPIC_0000002523299545__a1babc47c84516dac68c018057b33a23b) | 该操作是否需要用户参与。 |
| [FIDO2_PublicKeyCredentialCreationOptions](FIDO2_PublicKeyCredentialCreationOptions.md) [publicKey](FIDO2_CredentialCreationOptions.md#ZH-CN_TOPIC_0000002523299545__ab70a2bf85546ec37e7fb7ac0c9d82635) | publicKey凭证请求的选项。 |

#### 结构体成员变量说明

#### [mediation](FIDO2_CredentialCreationOptions.md#ZH-CN_TOPIC_0000002523299545__a1babc47c84516dac68c018057b33a23b)

```ets
FIDO2_CredentialMediationRequirement FIDO2_CredentialCreationOptions::mediation
```

**描述**

操作是否需要用户参与。

#### [publicKey](FIDO2_CredentialCreationOptions.md#ZH-CN_TOPIC_0000002523299545__ab70a2bf85546ec37e7fb7ac0c9d82635)

```ets
[FIDO2_PublicKeyCredentialCreationOptions](FIDO2_PublicKeyCredentialCreationOptions.md) FIDO2_CredentialCreationOptions::publicKey
```

**描述**

[publicKey](FIDO2_CredentialCreationOptions.md#ZH-CN_TOPIC_0000002523299545__ab70a2bf85546ec37e7fb7ac0c9d82635)凭证请求的选项。
