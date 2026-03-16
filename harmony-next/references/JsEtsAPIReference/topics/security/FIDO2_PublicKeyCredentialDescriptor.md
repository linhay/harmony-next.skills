# FIDO2_PublicKeyCredentialDescriptor

#### 概述

用于注册或认证凭据的参数。

**起始版本：** 6.0.0(20)

**相关模块：**[FIDO2](../misc/通行密钥.md)

#### 汇总

#### 成员变量

名称

描述

[FIDO2_PublicKeyCredentialType](../misc/通行密钥.md#ZH-CN_TOPIC_0000002523299537__gaa46edbba8f1162737d26681080eea727)[type](FIDO2_PublicKeyCredentialDescriptor.md#ZH-CN_TOPIC_0000002523299531__af26b9b07b0b456f01d527439dab91bc7)

凭证类型。

[Uint8Buff](../misc/Uint8Buff.md)[id](FIDO2_PublicKeyCredentialDescriptor.md#ZH-CN_TOPIC_0000002523299531__a1667f2884a9b3fbc969a80196510fe24)

凭据标识符。

[FIDO2_AuthenticatorTransportArray](FIDO2_AuthenticatorTransportArray.md)[transports](FIDO2_PublicKeyCredentialDescriptor.md#ZH-CN_TOPIC_0000002523299531__a97de56cc6859f743b46c399502460d34)

定义身份认证器访问类型（USB、NFC、蓝牙）。

#### 结构体成员变量说明

#### id

```ets
[Uint8Buff](../misc/Uint8Buff.md) FIDO2_PublicKeyCredentialDescriptor::id
```

**描述**

凭据标识符。

#### transports

```ets
[FIDO2_AuthenticatorTransportArray](FIDO2_AuthenticatorTransportArray.md) FIDO2_PublicKeyCredentialDescriptor::transports
```

**描述**

定义身份认证器访问类型（USB、NFC、蓝牙）。

#### type

```ets
[FIDO2_PublicKeyCredentialType](../misc/通行密钥.md#ZH-CN_TOPIC_0000002523299537__gaa46edbba8f1162737d26681080eea727) FIDO2_PublicKeyCredentialDescriptor::type
```

**描述**

凭证类型。