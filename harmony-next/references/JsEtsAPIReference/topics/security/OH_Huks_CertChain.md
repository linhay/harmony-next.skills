# OH_Huks_CertChain

```ets
struct OH_Huks_CertChain {...}
```

#### 概述

定义证书链的结构体类型。

**起始版本：** 9

相关模块： [HuksTypeApi](HuksTypeApi.md)

所在头文件： [native_huks_type.h](native_huks_type.h.md)

#### 汇总

#### 成员变量

| 名称 | 描述 |
| --- | --- |
| struct [OH_Huks_Blob](OH_Huks_Blob.md) *certs | 指向证书数据的指针。 |
| uint32_t certsCount | 证书本数。 |
