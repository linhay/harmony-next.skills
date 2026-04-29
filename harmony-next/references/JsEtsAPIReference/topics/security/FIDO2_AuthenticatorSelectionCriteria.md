# FIDO2_AuthenticatorSelectionCriteria

#### 概述

由webAuthn依赖方指定，与认证器有关。

**起始版本：** 6.0.0(20)

相关模块： [FIDO2](通行密钥.md)

#### 汇总

#### 成员变量

| 名称 | 描述 |
| --- | --- |
| [FIDO2_AuthenticatorAttachment](../security/通行密钥.md#ZH-CN_TOPIC_0000002523299537__gaa6aa2fca2e7690e98f6d1d273324e471) [authenticatorAttachment](FIDO2_AuthenticatorSelectionCriteria.md#ZH-CN_TOPIC_0000002490979826__a5a16c0b91ed4c2391957997fb3e88ef9) | 认证器信息（平台、漫游）。默认值为FIDO2_PLATFORM。可选。 |
| const char * [residentKey](FIDO2_AuthenticatorSelectionCriteria.md#ZH-CN_TOPIC_0000002490979826__a589e6893a729673451d1f96de44a5512) | 常驻键。默认空。可选。 |
| bool [requireResidentKey](FIDO2_AuthenticatorSelectionCriteria.md#ZH-CN_TOPIC_0000002490979826__ad6ce444067958a3a44143642bc091404) | 是否需要常驻键，true代表需要常驻键，false代表不需要。默认值为false。可选。 |
| [FIDO2_UserVerificationRequirement](../security/通行密钥.md#ZH-CN_TOPIC_0000002523299537__ga632b7b26c16a519650398ccfc3515f7a) [userVerification](FIDO2_AuthenticatorSelectionCriteria.md#ZH-CN_TOPIC_0000002490979826__a0344ec93a5f4544e6bbc0a2d496c867f) | 用户认证需求枚举。默认值为preferred。可选。 |

#### 结构体成员变量说明

#### [authenticatorAttachment](FIDO2_AuthenticatorSelectionCriteria.md#ZH-CN_TOPIC_0000002490979826__a5a16c0b91ed4c2391957997fb3e88ef9)

```ets
FIDO2_AuthenticatorAttachment FIDO2_AuthenticatorSelectionCriteria::authenticatorAttachment
```

**描述**

认证器信息（平台、漫游）。可选。

#### [requireResidentKey](FIDO2_AuthenticatorSelectionCriteria.md#ZH-CN_TOPIC_0000002490979826__ad6ce444067958a3a44143642bc091404)

```ets
bool FIDO2_AuthenticatorSelectionCriteria::requireResidentKey
```

**描述**

是否需要常驻键，true代表需要常驻键，false代表不需要。默认值为false。可选。

#### [residentKey](FIDO2_AuthenticatorSelectionCriteria.md#ZH-CN_TOPIC_0000002490979826__a589e6893a729673451d1f96de44a5512)

```ets
const char* FIDO2_AuthenticatorSelectionCriteria::residentKey
```

**描述**

常驻键。可选。

#### [userVerification](FIDO2_AuthenticatorSelectionCriteria.md#ZH-CN_TOPIC_0000002490979826__a0344ec93a5f4544e6bbc0a2d496c867f)

```ets
FIDO2_UserVerificationRequirement FIDO2_AuthenticatorSelectionCriteria::userVerification
```

**描述**

用户认证需求枚举。默认值为preferred。可选。
