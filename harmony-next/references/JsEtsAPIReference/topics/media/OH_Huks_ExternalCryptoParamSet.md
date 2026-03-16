# OH_Huks_ExternalCryptoParamSet

```ets
typedef struct OH_Huks_ExternalCryptoParamSet {...} OH_Huks_ExternalCryptoParamSet
```

#### 概述

定义外部加密参数集合的结构。

**起始版本：** 22

**相关模块：**[HuksExternalCryptoTypeApi](../networking/HuksExternalCryptoTypeApi.md)

**所在头文件：**[native_huks_external_crypto_type.h](../../capi/headers/native_huks_external_crypto_type.h.md)

#### 汇总

#### 成员变量

名称描述uint32_t paramSetSize

参数集合所占内存大小，单位：Byte。

**起始版本：** 22

uint32_t paramsCnt

参数集合中的参数数量。

**起始版本：** 22

[OH_Huks_ExternalCryptoParam](OH_Huks_ExternalCryptoParam.md) params[]

参数数组，大小由paramSetSize与paramsCnt决定。

**起始版本：** 22