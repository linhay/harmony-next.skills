# FIDO2_AuthenticatorAttestationResponse

#### 概述

认证器声明响应。

**起始版本：** 6.0.0(20)

**相关模块：**[FIDO2](../misc/通行密钥.md)

#### 汇总

#### 成员变量

名称

描述

[Uint8Buff](../misc/Uint8Buff.md)[attestationObject](FIDO2_AuthenticatorAttestationResponse.md#ZH-CN_TOPIC_0000002491139798__a3e876d044501dcc3fb3f0433d7c2766b)

声明对象。

[Uint8Buff](../misc/Uint8Buff.md)[clientDataJson](FIDO2_AuthenticatorAttestationResponse.md#ZH-CN_TOPIC_0000002491139798__ab0b05a7e50e252583481e8b47404bd00)

获取客户端数据，表示WebAuthn依赖方和客户端的上下文绑定，包含类型、挑战值及源等数据。

[Uint8Buff](../misc/Uint8Buff.md)[publicKey](FIDO2_AuthenticatorAttestationResponse.md#ZH-CN_TOPIC_0000002491139798__a9479186904add89fc9a5cac11b4b64cd)

publicKey凭证请求的选项，字节流。

[Uint8Buff](../misc/Uint8Buff.md)[authenticatorData](FIDO2_AuthenticatorAttestationResponse.md#ZH-CN_TOPIC_0000002491139798__ab9d09b1672f4690d8246200e8ce0d2ab)

认证器数据，字节流。

[FIDO2_Algorithm](../misc/通行密钥.md#ZH-CN_TOPIC_0000002523299537__ga27cd96fc7f972c4cd8cfe4d92737920a)[publicKeyAlgorithm](FIDO2_AuthenticatorAttestationResponse.md#ZH-CN_TOPIC_0000002491139798__a283dce979858a43e0185bb17d8e4ab32)

密码算法。

[FIDO2_AuthenticatorTransportArray](FIDO2_AuthenticatorTransportArray.md)[transports](FIDO2_AuthenticatorAttestationResponse.md#ZH-CN_TOPIC_0000002491139798__a152f995f69179b1067d32cd2cabfadde)

定义身份认证器访问类型（USB、NFC、蓝牙）。

#### 结构体成员变量说明

#### attestationObject

```ets
[Uint8Buff](../misc/Uint8Buff.md) FIDO2_AuthenticatorAttestationResponse::attestationObject
```

**描述**

声明对象。

#### authenticatorData

```ets
[Uint8Buff](../misc/Uint8Buff.md) FIDO2_AuthenticatorAttestationResponse::authenticatorData
```

**描述**

认证器数据，字节流。

#### clientDataJson

```ets
[Uint8Buff](../misc/Uint8Buff.md) FIDO2_AuthenticatorAttestationResponse::clientDataJson
```

**描述**

获取客户端数据，表示WebAuthn依赖方和客户端的上下文绑定，包含类型、挑战值及源等数据。

#### publicKey

```ets
[Uint8Buff](../misc/Uint8Buff.md) FIDO2_AuthenticatorAttestationResponse::publicKey
```

**描述**

publicKey凭证请求的选项，字节流。

#### publicKeyAlgorithm

```ets
[FIDO2_Algorithm](../misc/通行密钥.md#ZH-CN_TOPIC_0000002523299537__ga27cd96fc7f972c4cd8cfe4d92737920a) FIDO2_AuthenticatorAttestationResponse::publicKeyAlgorithm
```

**描述**

密码算法。

#### transports

```ets
[FIDO2_AuthenticatorTransportArray](FIDO2_AuthenticatorTransportArray.md) FIDO2_AuthenticatorAttestationResponse::transports
```

**描述**

定义身份认证器访问类型（USB、NFC、蓝牙）。