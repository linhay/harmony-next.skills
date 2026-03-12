# OH_Huks_KeyMaterial25519

```ets
struct OH_Huks_KeyMaterial25519 {...}
```

#### 概述

定义25519类型密钥的结构体类型。

**起始版本：** 9

**相关模块：**[HuksTypeApi](HuksTypeApi.md)

**所在头文件：**[native_huks_type.h](native_huks_type.h.md)

#### 汇总

#### 成员变量

名称描述enum [OH_Huks_KeyAlg](native_huks_type.h.md#ZH-CN_TOPIC_0000002529285393__oh_huks_keyalg) keyAlg密钥的算法类型。uint32_t keySize25519类型密钥的长度。uint32_t pubKeySize公钥的长度。uint32_t priKeySize私钥的长度。uint32_t reserved预留字段。建议开发者赋值为0。