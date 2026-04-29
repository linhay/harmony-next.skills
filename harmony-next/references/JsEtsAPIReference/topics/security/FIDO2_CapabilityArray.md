# FIDO2_CapabilityArray

**概述**

描述能力数组。

起始版本： 6.0.0(20)

相关模块： [FIDO2](通行密钥.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| uint32_t number | 能力的数量。 |
| FIDO2_Capability * capability | 能力的数组。 |

**结构体成员变量说明**

**capability**

```ets
FIDO2_Capability* FIDO2_CapabilityArray::capability
```

描述

能力数组。

**number**

```ets
uint32_t FIDO2_CapabilityArray::number
```

描述

能力数组长度。