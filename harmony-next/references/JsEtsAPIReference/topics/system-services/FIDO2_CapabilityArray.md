# FIDO2_CapabilityArray

#### 概述

描述能力数组。

**起始版本：** 6.0.0(20)

**相关模块：**[FIDO2](../misc/通行密钥.md)

#### 汇总

#### 成员变量

名称

描述

uint32_t [number](FIDO2_CapabilityArray.md#ZH-CN_TOPIC_0000002491139790__a76a1441a6186306388f5008c4e6a3c1c)

能力的数量。

[FIDO2_Capability](FIDO2_Capability.md) * [capability](FIDO2_CapabilityArray.md#ZH-CN_TOPIC_0000002491139790__ab0bdcdf4d5eb6f72906334316629193c)

能力的数组。

#### 结构体成员变量说明

#### capability

```ets
[FIDO2_Capability](FIDO2_Capability.md)* FIDO2_CapabilityArray::capability
```

**描述**

能力数组。

#### number

```ets
uint32_t FIDO2_CapabilityArray::number
```

**描述**

能力数组长度。