# FIDO2_PublicKeyCredentialDescriptorArray

#### 概述

PublicKey凭证描述符数组。

**起始版本：** 6.0.0(20)

**相关模块：**[FIDO2](通行密钥.md)

#### 汇总

#### 成员变量

名称

描述

uint32_t [allowCredentiallNum](FIDO2_PublicKeyCredentialDescriptorArray.md#ZH-CN_TOPIC_0000002523139563__a1085b6c76d592a26a86e2502d44312e3)

允许凭证数目。

[FIDO2_PublicKeyCredentialDescriptor](FIDO2_PublicKeyCredentialDescriptor.md) * [allowCredentials](FIDO2_PublicKeyCredentialDescriptorArray.md#ZH-CN_TOPIC_0000002523139563__aaccb43d445bbaacfabcd5d9a37152c3f)

认证凭据的附加参数列表。默认值为[]。

#### 结构体成员变量说明

#### allowCredentiallNum

```ets
uint32_t FIDO2_PublicKeyCredentialDescriptorArray::allowCredentiallNum
```

**描述**

允许凭证数目。

#### allowCredentials

```ets
[FIDO2_PublicKeyCredentialDescriptor](FIDO2_PublicKeyCredentialDescriptor.md)* FIDO2_PublicKeyCredentialDescriptorArray::allowCredentials
```

**描述**

认证凭据的附加参数列表。默认值为[]。