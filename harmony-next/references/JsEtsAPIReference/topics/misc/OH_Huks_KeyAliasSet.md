# OH_Huks_KeyAliasSet

```ets
struct OH_Huks_KeyAliasSet {...}
```

#### 概述

定义密钥别名集的结构体类型。

**起始版本：** 20

**相关模块：**[HuksTypeApi](../networking/HuksTypeApi.md)

**所在头文件：**[native_huks_type.h](../../capi/headers/native_huks_type.h.md)

#### 汇总

#### 成员变量

名称描述uint32_t aliasesCnt密钥别名集个数。struct [OH_Huks_Blob](OH_Huks_Blob.md) *aliases指向密钥别名集数据的指针。