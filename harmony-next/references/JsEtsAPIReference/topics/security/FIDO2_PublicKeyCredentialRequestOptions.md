# FIDO2_PublicKeyCredentialRequestOptions

#### 概述

定义通行密钥认证请求参数。

**起始版本：** 6.0.0(20)

**相关模块：**[FIDO2](../misc/通行密钥.md)

#### 汇总

#### 成员变量

名称

描述

[Uint8Buff](../misc/Uint8Buff.md)[challenge](FIDO2_PublicKeyCredentialRequestOptions.md#ZH-CN_TOPIC_0000002491139796__a1e9595b070a8f14c84584caac9fe4b12)

获取挑战值。

uint32_t [timeout](FIDO2_PublicKeyCredentialRequestOptions.md#ZH-CN_TOPIC_0000002491139796__af40a180a55e9ec9ccdbdfbc0663fa6a0)

认证操作最长时间，单位为毫秒。默认为300000（5分钟）。可选。

char * [rpId](FIDO2_PublicKeyCredentialRequestOptions.md#ZH-CN_TOPIC_0000002491139796__af1e1f8a828c88c2baace9cc97e13253d)

依赖方标识（如域名等）。默认空。可选。

[FIDO2_PublicKeyCredentialDescriptorArray](FIDO2_PublicKeyCredentialDescriptorArray.md)[allowCredentials](FIDO2_PublicKeyCredentialRequestOptions.md#ZH-CN_TOPIC_0000002491139796__a8b1b230c4537756fdedfa3d3011efa7f)

认证凭据的附加参数列表。默认空列表。可选。

[FIDO2_UserVerificationRequirement](../misc/通行密钥.md#ZH-CN_TOPIC_0000002523299537__ga632b7b26c16a519650398ccfc3515f7a)[userVerification](FIDO2_PublicKeyCredentialRequestOptions.md#ZH-CN_TOPIC_0000002491139796__a56ab962fc3732a25608cb0be55b1bc03)

用户认证需求枚举。默认值为preferred。可选。

[FIDO2_PublicKeyCredentialHintArray](FIDO2_PublicKeyCredentialHintArray.md)[hints](FIDO2_PublicKeyCredentialRequestOptions.md#ZH-CN_TOPIC_0000002491139796__a5397cbbb234b741cbc00b288b289a3a0)

认证方式指示。默认值为[]。可选。

char * [extensions](FIDO2_PublicKeyCredentialRequestOptions.md#ZH-CN_TOPIC_0000002491139796__ad9695387a2b91111848f47232235e2d3)

扩展名必须是表示Map<string, Object> object的JSON字符串。默认空。可选。

#### 结构体成员变量说明

#### allowCredentials

```ets
[FIDO2_PublicKeyCredentialDescriptorArray](FIDO2_PublicKeyCredentialDescriptorArray.md) FIDO2_PublicKeyCredentialRequestOptions::allowCredentials
```

**描述**

认证凭据的附加参数列表。可选。

#### challenge

```ets
[Uint8Buff](../misc/Uint8Buff.md) FIDO2_PublicKeyCredentialRequestOptions::challenge
```

**描述**

获取挑战值。

#### extensions

```ets
char* FIDO2_PublicKeyCredentialRequestOptions::extensions
```

**描述**

扩展名必须是表示Map<string, Object> object的JSON字符串。可选。

#### hints

```ets
[FIDO2_PublicKeyCredentialHintArray](FIDO2_PublicKeyCredentialHintArray.md) FIDO2_PublicKeyCredentialRequestOptions::hints
```

**描述**

认证方式指示。默认值为[]。可选。

#### rpId

```ets
char* FIDO2_PublicKeyCredentialRequestOptions::rpId
```

**描述**

依赖方标识。可选。

#### timeout

```ets
uint32_t FIDO2_PublicKeyCredentialRequestOptions::timeout
```

**描述**

认证操作最长时间，单位为毫秒。可选。

#### userVerification

```ets
[FIDO2_UserVerificationRequirement](../misc/通行密钥.md#ZH-CN_TOPIC_0000002523299537__ga632b7b26c16a519650398ccfc3515f7a) FIDO2_PublicKeyCredentialRequestOptions::userVerification
```

**描述**

用户认证需求枚举。默认值为preferred。可选。