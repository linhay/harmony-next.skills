# FIDO2_PublicKeyCredentialHintArray

#### 概述

认证方式指示数组。

**起始版本：** 6.0.0(20)

**相关模块：**[FIDO2](通行密钥.md)

#### 汇总

#### 成员变量

名称

描述

uint32_t [hintNum](FIDO2_PublicKeyCredentialHintArray.md#ZH-CN_TOPIC_0000002491139792__a246f153f4da878f2cafe8c8c6cb13b50)

认证方式指示数目。

[FIDO2_PublicKeyCredentialHint](通行密钥.md#ZH-CN_TOPIC_0000002523299537__gab7b1367ea48debe767ae103f8ac9e96c) * [hints](FIDO2_PublicKeyCredentialHintArray.md#ZH-CN_TOPIC_0000002491139792__afab2c10a892afca1908947135f8b6fd6)

认证方式指示列表。

#### 结构体成员变量说明

#### hintNum

```ets
uint32_t FIDO2_PublicKeyCredentialHintArray::hintNum
```

**描述**

认证方式指示数目。

#### hints

```ets
[FIDO2_PublicKeyCredentialHint](通行密钥.md#ZH-CN_TOPIC_0000002523299537__gab7b1367ea48debe767ae103f8ac9e96c)* FIDO2_PublicKeyCredentialHintArray::hints
```

**描述**

认证方式指示列表。