# OH_Huks_KeyMaterialEcc

```ets
struct OH_Huks_KeyMaterialEcc {...}
```

#### 概述

定义Ecc密钥的结构体类型。

**起始版本：** 9

**相关模块：**[HuksTypeApi](../networking/HuksTypeApi.md)

**所在头文件：**[native_huks_type.h](../../capi/headers/native_huks_type.h.md)

#### 汇总

#### 成员变量

名称描述enum [OH_Huks_KeyAlg](../../capi/headers/native_huks_type.h.md#ZH-CN_TOPIC_0000002529285393__oh_huks_keyalg) keyAlg密钥的算法类型。uint32_t keySize密钥的长度。uint32_t xSizex值的长度。uint32_t ySizey值的长度。uint32_t zSizez值的长度。