# OH_Huks_KeyMaterialEcc

```ets
struct OH_Huks_KeyMaterialEcc {...}
```

**概述**

定义Ecc密钥的结构体类型。

起始版本： 9

相关模块： [HuksTypeApi](HuksTypeApi.md)

所在头文件： [native_huks_type.h](native_huks_type.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| enum OH_Huks_KeyAlg keyAlg | 密钥的算法类型。 |
| uint32_t keySize | 密钥的长度。 |
| uint32_t xSize | x值的长度。 |
| uint32_t ySize | y值的长度。 |
| uint32_t zSize | z值的长度。 |