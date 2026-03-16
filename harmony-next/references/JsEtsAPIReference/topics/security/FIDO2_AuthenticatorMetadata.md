# FIDO2_AuthenticatorMetadata

#### 概述

认证器元数据。

**起始版本：** 6.0.0(20)

**相关模块：**[FIDO2](../misc/通行密钥.md)

#### 汇总

#### 成员变量

名称

描述

[Uint8Buff](../misc/Uint8Buff.md)[aaguid](FIDO2_AuthenticatorMetadata.md#ZH-CN_TOPIC_0000002523139571__a69443cd171e66c315384775a12ef5528)

认证器的aaguid。

[FIDO2_Uvm](../misc/通行密钥.md#ZH-CN_TOPIC_0000002523299537__ga60fda18b064802349b186de072b43e98)[uvm](FIDO2_AuthenticatorMetadata.md#ZH-CN_TOPIC_0000002523139571__af352363afd660f220c988b515fd0bba5)

支持的认证器类型。

bool [isAvailable](FIDO2_AuthenticatorMetadata.md#ZH-CN_TOPIC_0000002523139571__a9918ca9079143bbd93a5f977223a0421)

认证器是否可用。

#### 结构体成员变量说明

#### aaguid

```ets
[Uint8Buff](../misc/Uint8Buff.md) FIDO2_AuthenticatorMetadata::aaguid
```

**描述**

认证器的aaguid。

#### isAvailable

```ets
bool FIDO2_AuthenticatorMetadata::isAvailable
```

**描述**

认证器是否可用。如果返回true，则表示认证器可用；返回false，表示认证器不可用。

#### uvm

```ets
[FIDO2_Uvm](../misc/通行密钥.md#ZH-CN_TOPIC_0000002523299537__ga60fda18b064802349b186de072b43e98) FIDO2_AuthenticatorMetadata::uvm
```

**描述**

支持的认证器类型。