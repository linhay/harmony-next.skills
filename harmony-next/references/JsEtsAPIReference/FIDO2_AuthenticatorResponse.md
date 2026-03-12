# FIDO2_AuthenticatorResponse

#### 概述

定义获取认证器断言响应的结构体。

**起始版本：** 6.0.0(20)

**相关模块：**[FIDO2](通行密钥.md)

#### 汇总

#### 成员变量

名称

描述

[Uint8Buff](Uint8Buff.md)[authenticatorData](FIDO2_AuthenticatorResponse.md#ZH-CN_TOPIC_0000002490979828__a4885e9778d931bf68044939fe6a9b895)

身份认证器数据。

[Uint8Buff](Uint8Buff.md)[signature](FIDO2_AuthenticatorResponse.md#ZH-CN_TOPIC_0000002490979828__ad51a95561a84021c8bb2bd5070ca07ec)

签名。

[Uint8Buff](Uint8Buff.md)[userHandle](FIDO2_AuthenticatorResponse.md#ZH-CN_TOPIC_0000002490979828__a09d4f78982031d057d0235ca225a137e)

用户句柄（用户ID）。可选。

[Uint8Buff](Uint8Buff.md)[clientDataJson](FIDO2_AuthenticatorResponse.md#ZH-CN_TOPIC_0000002490979828__aa98421c9febb5f460cbe4c9b9420cc69)

获取客户端数据，表示WebAuthn依赖方和客户端的上下文绑定，包含类型、挑战值及源等数据。

#### 结构体成员变量说明

#### authenticatorData

```ets
[Uint8Buff](Uint8Buff.md) FIDO2_AuthenticatorResponse::authenticatorData
```

**描述**

身份认证器数据。

#### clientDataJson

```ets
[Uint8Buff](Uint8Buff.md) FIDO2_AuthenticatorResponse::clientDataJson
```

**描述**

获取客户端数据，表示WebAuthn依赖方和客户端的上下文绑定，包含类型、挑战值及源等数据。

#### signature

```ets
[Uint8Buff](Uint8Buff.md) FIDO2_AuthenticatorResponse::signature
```

**描述**

签名。

#### userHandle

```ets
[Uint8Buff](Uint8Buff.md) FIDO2_AuthenticatorResponse::userHandle
```

**描述**

用户句柄。可选。