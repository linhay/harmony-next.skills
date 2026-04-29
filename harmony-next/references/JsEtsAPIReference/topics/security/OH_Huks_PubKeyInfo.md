# OH_Huks_PubKeyInfo

```ets
struct OH_Huks_PubKeyInfo {...}
```

**概述**

定义公钥信息的结构体类型。

起始版本： 9

相关模块： [HuksTypeApi](HuksTypeApi.md)

所在头文件： [native_huks_type.h](native_huks_type.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| enum OH_Huks_KeyAlg keyAlg | 公钥的算法类型。 |
| uint32_t keySize | 公钥的长度。 |
| uint32_t nOrXSize | n或X值的长度。 |
| uint32_t eOrYSize | e或Y值的长度。 |
| uint32_t placeHolder | 占位符大小。 |