# FIDO2_AuthenticatorMetadataArray

#### 概述

描述支持的认证器数组。

**起始版本：** 6.0.0(20)

**相关模块：**[FIDO2](通行密钥.md)

#### 汇总

#### 成员变量

名称

描述

uint32_t [number](FIDO2_AuthenticatorMetadataArray.md#ZH-CN_TOPIC_0000002523299541__a7c651eca3b7f544a7b233fcb23ab8717)

认证器数目。

[FIDO2_AuthenticatorMetadata](FIDO2_AuthenticatorMetadata.md) * [authenticators](FIDO2_AuthenticatorMetadataArray.md#ZH-CN_TOPIC_0000002523299541__a25670f7508e2a20f0c72519db28c5c59)

认证器支持的扩展。

#### 结构体成员变量说明

#### authenticators

```ets
[FIDO2_AuthenticatorMetadata](FIDO2_AuthenticatorMetadata.md)* FIDO2_AuthenticatorMetadataArray::authenticators
```

**描述**

认证器支持的扩展。

#### number

```ets
uint32_t FIDO2_AuthenticatorMetadataArray::number
```

**描述**

认证器数目。