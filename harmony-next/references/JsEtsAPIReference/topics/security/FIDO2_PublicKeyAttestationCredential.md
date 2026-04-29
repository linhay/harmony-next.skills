# FIDO2_PublicKeyAttestationCredential

#### 概述

定义获取注册结果结构体。

**起始版本：** 6.0.0(20)

相关模块： [FIDO2](通行密钥.md)

#### 汇总

#### 成员变量

| 名称 | 描述 |
| --- | --- |
| [Uint8Buff](Uint8Buff.md) [rawId](FIDO2_PublicKeyAttestationCredential.md#ZH-CN_TOPIC_0000002523299543__abc90a2b565a8e48d6d965ccc27c32445) | 原始凭据标识符。 |
| [FIDO2_AuthenticatorAttestationResponse](FIDO2_AuthenticatorAttestationResponse.md) [response](FIDO2_PublicKeyAttestationCredential.md#ZH-CN_TOPIC_0000002523299543__ad1c1c4fd329dc63e5332d26dc404b405) | 认证器证明响应。 |
| [FIDO2_AuthenticatorAttachment](../security/通行密钥.md#ZH-CN_TOPIC_0000002523299537__gaa6aa2fca2e7690e98f6d1d273324e471) [authenticatorAttachment](FIDO2_PublicKeyAttestationCredential.md#ZH-CN_TOPIC_0000002523299543__ae15ff75bfa90c5c79c8ddbe3cf464366) | 认证器信息（平台、漫游）。默认值为FIDO2_PLATFORM。可选。 |
| const char * [id](FIDO2_PublicKeyAttestationCredential.md#ZH-CN_TOPIC_0000002523299543__afa23550117d766125eca72390af0632e) | 凭据的标识符。对于每种类型的凭据，标识符的要求都是不同的。 |
| const char * [type](FIDO2_PublicKeyAttestationCredential.md#ZH-CN_TOPIC_0000002523299543__a180d55f4eff94208c319c1b5f3d40e20) | 此属性返回对象的接口对象的槽的值，它指定此对象所代表的凭据类型。 |
| [AuthenticationExtensionsClientOutputs](AuthenticationExtensionsClientOutputs.md) [clientExtensionResults](FIDO2_PublicKeyAttestationCredential.md#ZH-CN_TOPIC_0000002523299543__aef514f978325f0a09305b10353f8ec3c) | 客户端扩展结果。当前版本不支持扩展，因此占位符始终为NULL，必须将clientExtensionResults键对应的值解析为{}。 |

#### 结构体成员变量说明

#### [authenticatorAttachment](FIDO2_PublicKeyAttestationCredential.md#ZH-CN_TOPIC_0000002523299543__ae15ff75bfa90c5c79c8ddbe3cf464366)

```ets
FIDO2_AuthenticatorAttachment FIDO2_PublicKeyAttestationCredential::authenticatorAttachment
```

**描述**

认证器信息（平台、漫游）。可选。

#### [clientExtensionResults](FIDO2_PublicKeyAttestationCredential.md#ZH-CN_TOPIC_0000002523299543__aef514f978325f0a09305b10353f8ec3c)

```ets
[AuthenticationExtensionsClientOutputs](AuthenticationExtensionsClientOutputs.md) FIDO2_PublicKeyAttestationCredential::clientExtensionResults
```

**描述**

客户端扩展结果。当前版本不支持扩展，因此占位符始终为NULL，必须将[clientExtensionResults](FIDO2_PublicKeyAttestationCredential.md#ZH-CN_TOPIC_0000002523299543__aef514f978325f0a09305b10353f8ec3c)键对应的值解析为{}。

#### [id](FIDO2_PublicKeyAttestationCredential.md#ZH-CN_TOPIC_0000002523299543__afa23550117d766125eca72390af0632e)

```ets
const char* FIDO2_PublicKeyAttestationCredential::id
```

**描述**

凭据的标识符。对于每种类型的凭据，标识符的要求都是不同的。

#### [rawId](FIDO2_PublicKeyAttestationCredential.md#ZH-CN_TOPIC_0000002523299543__abc90a2b565a8e48d6d965ccc27c32445)

```ets
[Uint8Buff](Uint8Buff.md) FIDO2_PublicKeyAttestationCredential::rawId
```

**描述**

原始凭据标识符。

#### [response](FIDO2_PublicKeyAttestationCredential.md#ZH-CN_TOPIC_0000002523299543__ad1c1c4fd329dc63e5332d26dc404b405)

```ets
[FIDO2_AuthenticatorAttestationResponse](FIDO2_AuthenticatorAttestationResponse.md) FIDO2_PublicKeyAttestationCredential::response
```

**描述**

认证器证明响应。

#### [type](FIDO2_PublicKeyAttestationCredential.md#ZH-CN_TOPIC_0000002523299543__a180d55f4eff94208c319c1b5f3d40e20)

```ets
const char* FIDO2_PublicKeyAttestationCredential::type
```

**描述**

此属性返回对象的接口对象的槽的值，它指定此对象所代表的凭据类型。
