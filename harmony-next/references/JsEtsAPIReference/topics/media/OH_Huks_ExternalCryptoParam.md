# OH_Huks_ExternalCryptoParam

```ets
typedef struct {...} OH_Huks_ExternalCryptoParam
```

#### 概述

定义参数集合中单个参数的结构体。

**起始版本：** 22

**相关模块：**[HuksExternalCryptoTypeApi](../networking/HuksExternalCryptoTypeApi.md)

**所在头文件：**[native_huks_external_crypto_type.h](../../capi/headers/native_huks_external_crypto_type.h.md)

#### 汇总

#### 成员变量

名称描述uint32_t tag标签值。

union {

 bool boolParam;

 int32_t int32Param;

 uint32_t uint32Param;

 uint64_t uint64Param;

[struct OH_Huks_Blob](../misc/OH_Huks_Blob.md) blob;

 }

标签内容。

boolParam：布尔类型参数。

int32Param：int32_t类型参数。

uint32Param：uint32_t类型参数。

uint64Param：uint64_t类型参数。

blob：OH_Huks_Blob类型参数。