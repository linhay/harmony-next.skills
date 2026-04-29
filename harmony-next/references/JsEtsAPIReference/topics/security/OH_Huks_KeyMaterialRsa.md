# OH_Huks_KeyMaterialRsa

```ets
struct OH_Huks_KeyMaterialRsa {...}
```

**概述**

定义Rsa密钥的结构体类型。

起始版本： 9

相关模块： [HuksTypeApi](HuksTypeApi.md)

所在头文件： [native_huks_type.h](native_huks_type.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| enum OH_Huks_KeyAlg keyAlg | 密钥的算法类型。 |
| uint32_t keySize | 密钥的长度。 |
| uint32_t nSize | n值的长度。 |
| uint32_t eSize | e值的长度。 |
| uint32_t dSize | d值的长度。 |