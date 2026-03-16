# OH_Huks_PubKeyInfo

```ets
struct OH_Huks_PubKeyInfo {...}
```

#### 概述

定义公钥信息的结构体类型。

**起始版本：** 9

**相关模块：**[HuksTypeApi](../networking/HuksTypeApi.md)

**所在头文件：**[native_huks_type.h](../../capi/headers/native_huks_type.h.md)

#### 汇总

#### 成员变量

名称描述enum [OH_Huks_KeyAlg](../../capi/headers/native_huks_type.h.md#ZH-CN_TOPIC_0000002529285393__oh_huks_keyalg) keyAlg公钥的算法类型。uint32_t keySize公钥的长度。uint32_t nOrXSizen或X值的长度。uint32_t eOrYSizee或Y值的长度。uint32_t placeHolder占位符大小。