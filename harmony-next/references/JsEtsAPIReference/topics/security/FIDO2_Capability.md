# FIDO2_Capability

**概述**

通行密钥能力的结构体。

起始版本： 6.0.0(20)

相关模块： [FIDO2](通行密钥.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| FIDO2_ClientCapability capability | 通行密钥的能力。 |
| bool isSupported | 是否支持。如果为true表示支持，false表示不支持。 |

**结构体成员变量说明**

**capability**

```ets
FIDO2_ClientCapability FIDO2_Capability::capability
```

描述

通行密钥的能力。

**isSupported**

```ets
bool FIDO2_Capability::isSupported
```

描述

是否支持。如果为true表示支持，false表示不支持。