# FIDO2_PublicKeyCredentialCreationOptions

#### 概述

创建新的认证凭据的选项。

**起始版本：** 6.0.0(20)

**相关模块：**[FIDO2](../misc/通行密钥.md)

#### 汇总

#### 成员变量

名称

描述

[FIDO2_PublicKeyCredentialRpEntity](FIDO2_PublicKeyCredentialRpEntity.md)[rp](FIDO2_PublicKeyCredentialCreationOptions.md#ZH-CN_TOPIC_0000002523139573__a73116b439c5f43f84087e894ed664ad1)

创建新凭据时的依赖方属性。

[FIDO2_PublicKeyCredentialUserEntity](FIDO2_PublicKeyCredentialUserEntity.md)[user](FIDO2_PublicKeyCredentialCreationOptions.md#ZH-CN_TOPIC_0000002523139573__a92cb44322ca7e1007c8736632cd0964b)

创建新凭据时用户的属性。

[Uint8Buff](../misc/Uint8Buff.md)[challenge](FIDO2_PublicKeyCredentialCreationOptions.md#ZH-CN_TOPIC_0000002523139573__aeba2a19abf19398c6d4292e3f144ab94)

挑战值。

[FIDO2_CredentialCreationOptionArray](FIDO2_CredentialCreationOptionArray.md)[pubKeyCredParams](FIDO2_PublicKeyCredentialCreationOptions.md#ZH-CN_TOPIC_0000002523139573__aee42ffb77c2581dcc04b49fd0fcc8f41)

认证凭据的附加参数数组。

uint32_t [timeout](FIDO2_PublicKeyCredentialCreationOptions.md#ZH-CN_TOPIC_0000002523139573__afc2e551c307244eb5ac213e0cad9e2ac)

注册操作最长时间，单位为毫秒。默认为300000（5分钟）。可选。

[FIDO2_PublicKeyCredentialDescriptorArray](FIDO2_PublicKeyCredentialDescriptorArray.md)[excludeCredentials](FIDO2_PublicKeyCredentialCreationOptions.md#ZH-CN_TOPIC_0000002523139573__ae5ada7403f89bbe3d9e1c8e09c6c8a5e)

FIDO服务器已注册的凭据列表。默认值为[]。可选。

[FIDO2_AuthenticatorSelectionCriteria](FIDO2_AuthenticatorSelectionCriteria.md)[authenticatorSelection](FIDO2_PublicKeyCredentialCreationOptions.md#ZH-CN_TOPIC_0000002523139573__a7eef9101b8235fc4ef31e22cb7f43af9)

身份认证器相关配置项。

[FIDO2_PublicKeyCredentialHintArray](FIDO2_PublicKeyCredentialHintArray.md)[hints](FIDO2_PublicKeyCredentialCreationOptions.md#ZH-CN_TOPIC_0000002523139573__a5ca0d3727ad8d0b262af8592b2a5bbbb)

认证方式指示。默认值为[]。可选。

[FIDO2_AttestationConveyancePreference](../misc/通行密钥.md#ZH-CN_TOPIC_0000002523299537__ga1e33947b822678781f03c849ade9f45f)[attestation](FIDO2_PublicKeyCredentialCreationOptions.md#ZH-CN_TOPIC_0000002523139573__a7f6d16e60e5fc64bb54a3299a975e539)

凭据传递首选项。默认值为none，可选。

[FIDO2_AttestationFormatsArray](../media/FIDO2_AttestationFormatsArray.md)[attestationFormats](FIDO2_PublicKeyCredentialCreationOptions.md#ZH-CN_TOPIC_0000002523139573__a94e9ebb712dd404ac3807bc52549d6dd)

依赖方可以使用此选项指定有关认证方使用的证明声明格式的偏好。默认值为[]。

char * [extensions](FIDO2_PublicKeyCredentialCreationOptions.md#ZH-CN_TOPIC_0000002523139573__acbb159628fcd36243f29b10d4d04449d)

扩展名必须是表示Map<string, Object>对象的JSON字符串。默认空。可选。

#### 结构体成员变量说明

#### attestation

```ets
[FIDO2_AttestationConveyancePreference](../misc/通行密钥.md#ZH-CN_TOPIC_0000002523299537__ga1e33947b822678781f03c849ade9f45f) FIDO2_PublicKeyCredentialCreationOptions::attestation
```

**描述**

凭据传递首选项。默认值为none，可选。

#### attestationFormats

```ets
[FIDO2_AttestationFormatsArray](../media/FIDO2_AttestationFormatsArray.md) FIDO2_PublicKeyCredentialCreationOptions::attestationFormats
```

**描述**

依赖方可以使用此选项指定有关认证方使用的证明声明格式的偏好。默认值为[]。

#### authenticatorSelection

```ets
[FIDO2_AuthenticatorSelectionCriteria](FIDO2_AuthenticatorSelectionCriteria.md) FIDO2_PublicKeyCredentialCreationOptions::authenticatorSelection
```

**描述**

身份认证器相关配置项。

#### challenge

```ets
[Uint8Buff](../misc/Uint8Buff.md) FIDO2_PublicKeyCredentialCreationOptions::challenge
```

**描述**

挑战。

#### excludeCredentials

```ets
[FIDO2_PublicKeyCredentialDescriptorArray](FIDO2_PublicKeyCredentialDescriptorArray.md) FIDO2_PublicKeyCredentialCreationOptions::excludeCredentials
```

**描述**

FIDO服务器已注册的凭据列表。默认值为[]。可选。

#### extensions

```ets
char* FIDO2_PublicKeyCredentialCreationOptions::extensions
```

**描述**

扩展名必须是表示Map<string, Object>对象的JSON字符串。可选。

#### hints

```ets
[FIDO2_PublicKeyCredentialHintArray](FIDO2_PublicKeyCredentialHintArray.md) FIDO2_PublicKeyCredentialCreationOptions::hints
```

**描述**

认证方式指示。默认值为[]。可选。

#### pubKeyCredParams

```ets
[FIDO2_CredentialCreationOptionArray](FIDO2_CredentialCreationOptionArray.md) FIDO2_PublicKeyCredentialCreationOptions::pubKeyCredParams
```

**描述**

认证凭据的附加参数数组。

#### rp

```ets
[FIDO2_PublicKeyCredentialRpEntity](FIDO2_PublicKeyCredentialRpEntity.md) FIDO2_PublicKeyCredentialCreationOptions::rp
```

**描述**

创建新凭据时的依赖方属性。

#### timeout

```ets
uint32_t FIDO2_PublicKeyCredentialCreationOptions::timeout
```

**描述**

注册操作最长时间，单位为毫秒。可选。

#### user

```ets
[FIDO2_PublicKeyCredentialUserEntity](FIDO2_PublicKeyCredentialUserEntity.md) FIDO2_PublicKeyCredentialCreationOptions::user
```

**描述**

创建新凭据时用户的属性。