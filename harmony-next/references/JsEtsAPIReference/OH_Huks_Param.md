# OH_Huks_Param

```ets
struct OH_Huks_Param {...}
```

#### 概述

定义参数集中的参数结构体类型。

**起始版本：** 9

**相关模块：**[HuksTypeApi](HuksTypeApi.md)

**所在头文件：**[native_huks_type.h](native_huks_type.h.md)

#### 汇总

#### 成员变量

名称描述uint32_t tag标签值。

union {

 bool boolParam;

 int32_t int32Param;

 uint32_t uint32Param;

 uint64_t uint64Param;

[struct OH_Huks_Blob](OH_Huks_Blob.md) blob;

 }

boolParam：bool型参数。

int32Param：int32_t型参数。

uint32Param：uint32_t型参数。

uint64Param：uint64_t型参数。

blob：OH_Huks_Blob型参数。