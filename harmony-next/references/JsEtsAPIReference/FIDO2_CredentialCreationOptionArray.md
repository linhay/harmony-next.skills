# FIDO2_CredentialCreationOptionArray

#### 概述

认证凭据的附加参数数组。

**起始版本：** 6.0.0(20)

**相关模块：**[FIDO2](通行密钥.md)

#### 汇总

#### 成员变量

名称

描述

uint32_t [pubKeyCredParamNum](FIDO2_CredentialCreationOptionArray.md#ZH-CN_TOPIC_0000002491139800__a06e70ab9f71fb6291e9b3df957a2ae17)

PubKeyCredParam参数数目。

[FIDO2_PublicKeyCredentialParameters](FIDO2_PublicKeyCredentialParameters.md) * [pubKeyCredParams](FIDO2_CredentialCreationOptionArray.md#ZH-CN_TOPIC_0000002491139800__ab17a90ca7b76e6bca3cde9e18ce1f774)

认证凭据的附加参数。

#### 结构体成员变量说明

#### pubKeyCredParamNum

```ets
uint32_t FIDO2_CredentialCreationOptionArray::pubKeyCredParamNum
```

**描述**

PubKeyCredParam参数数目。

#### pubKeyCredParams

```ets
[FIDO2_PublicKeyCredentialParameters](FIDO2_PublicKeyCredentialParameters.md)* FIDO2_CredentialCreationOptionArray::pubKeyCredParams
```

**描述**

认证凭据的附加参数。