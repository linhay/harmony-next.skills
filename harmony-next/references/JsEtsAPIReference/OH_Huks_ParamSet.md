# OH_Huks_ParamSet

```ets
struct OH_Huks_ParamSet {...}
```

#### 概述

定义参数集的结构体类型。

**起始版本：** 9

**相关模块：**[HuksTypeApi](HuksTypeApi.md)

**所在头文件：**[native_huks_type.h](native_huks_type.h.md)

#### 汇总

#### 成员变量

名称描述uint32_t paramSetSize参数集的内存大小。uint32_t paramsCnt参数的个数。struct [OH_Huks_Param](OH_Huks_Param.md) params[]参数数组。