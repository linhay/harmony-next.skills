# FIDO2_PublicKeyCredentialUserEntity

#### 概述

创建新凭据时用户的属性。

**起始版本：** 6.0.0(20)

**相关模块：**[FIDO2](通行密钥.md)

#### 汇总

#### 成员变量

名称

描述

[Uint8Buff](Uint8Buff.md)[id](FIDO2_PublicKeyCredentialUserEntity.md#ZH-CN_TOPIC_0000002491139802__a89acdc47998ced27b3e55b7f99c90797)

凭据的标识符。

char * [displayName](FIDO2_PublicKeyCredentialUserEntity.md#ZH-CN_TOPIC_0000002491139802__af3d18ba7f46b81ffe1d54660c0cfe4be)

前台显示的用户名。

char * [name](FIDO2_PublicKeyCredentialUserEntity.md#ZH-CN_TOPIC_0000002491139802__ae25422337bd8154afbfc7272698f3978)

用户名。

#### 结构体成员变量说明

#### displayName

```ets
char* FIDO2_PublicKeyCredentialUserEntity::displayName
```

**描述**

前台显示的用户名。

#### id

```ets
[Uint8Buff](Uint8Buff.md) FIDO2_PublicKeyCredentialUserEntity::id
```

**描述**

凭据的标识符。

#### name

```ets
char* FIDO2_PublicKeyCredentialUserEntity::name
```

**描述**

用户名。