# FIDO2_PublicKeyAssertionCredential

#### 概述

定义获取认证结果结构体。

**起始版本：** 6.0.0(20)

**相关模块：**[FIDO2](通行密钥.md)

#### 汇总

#### 成员变量

名称

描述

[Uint8Buff](Uint8Buff.md)[rawId](FIDO2_PublicKeyAssertionCredential.md#ZH-CN_TOPIC_0000002523139567__a8adf6d21e094b1cf4b0a1e751014f2a3)

原始凭据标识符。

const char * [id](FIDO2_PublicKeyAssertionCredential.md#ZH-CN_TOPIC_0000002523139567__ad4fcc71b65296eec9da4fe4d759b1103)

凭据的标识符。对于每种类型的凭据，标识符的要求都是不同的。

const char * [type](FIDO2_PublicKeyAssertionCredential.md#ZH-CN_TOPIC_0000002523139567__a0bc28b95c86cbecf8818b9d12918ca44)

该属性以JSON字符串形式，返回对象的接口对象的插槽的值。该插槽用于指定此对象所表示的凭据类型。

[FIDO2_AuthenticatorResponse](FIDO2_AuthenticatorResponse.md)[response](FIDO2_PublicKeyAssertionCredential.md#ZH-CN_TOPIC_0000002523139567__a219c84e621a4f6039bbdfa774d33439b)

认证器断言响应。

[FIDO2_AuthenticatorAttachment](通行密钥.md#ZH-CN_TOPIC_0000002523299537__gaa6aa2fca2e7690e98f6d1d273324e471)[authenticatorAttachment](FIDO2_PublicKeyAssertionCredential.md#ZH-CN_TOPIC_0000002523139567__ac29d396433f47c6230ccca4fd046dfa1)

认证器信息（平台、漫游）。默认值为FIDO2_PLATFORM。可选。

[AuthenticationExtensionsClientOutputs](AuthenticationExtensionsClientOutputs.md)[clientExtensionResults](FIDO2_PublicKeyAssertionCredential.md#ZH-CN_TOPIC_0000002523139567__a62824d1fe883644cda1960e011fede7c)

客户端扩展结果。当前版本不支持扩展，因此占位符始终为NULL，必须将clientExtensionResults键对应的值解析为{}。

#### 结构体成员变量说明

#### authenticatorAttachment

```ets
[FIDO2_AuthenticatorAttachment](通行密钥.md#ZH-CN_TOPIC_0000002523299537__gaa6aa2fca2e7690e98f6d1d273324e471) FIDO2_PublicKeyAssertionCredential::authenticatorAttachment
```

**描述**

认证器信息（平台、漫游）。可选。

#### clientExtensionResults

```ets
[AuthenticationExtensionsClientOutputs](AuthenticationExtensionsClientOutputs.md) FIDO2_PublicKeyAssertionCredential::clientExtensionResults
```

**描述**

客户端扩展结果。当前版本不支持扩展，因此占位符始终为NULL，必须将clientExtensionResults键对应的值解析为{}。

#### id

```ets
const char* FIDO2_PublicKeyAssertionCredential::id
```

**描述**

凭据的标识符。对于每种类型的凭据，标识符的要求都是不同的。

#### rawId

```ets
[Uint8Buff](Uint8Buff.md) FIDO2_PublicKeyAssertionCredential::rawId
```

**描述**

原始凭据标识符。

#### response

```ets
[FIDO2_AuthenticatorResponse](FIDO2_AuthenticatorResponse.md) FIDO2_PublicKeyAssertionCredential::response
```

**描述**

认证器断言响应。

#### type

```ets
const char* FIDO2_PublicKeyAssertionCredential::type
```

**描述**

该属性以JSON字符串形式返回对象的接口对象的插槽的值，该插槽指定此对象所表示的凭据类型。