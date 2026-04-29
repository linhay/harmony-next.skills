# OH_Huks_KeyAliasSet

```ets
struct OH_Huks_KeyAliasSet {...}
```

**概述**

定义密钥别名集的结构体类型。

起始版本： 20

相关模块： [HuksTypeApi](HuksTypeApi.md)

所在头文件： [native_huks_type.h](native_huks_type.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| uint32_t aliasesCnt | 密钥别名集个数。 |
| struct OH_Huks_Blob *aliases | 指向密钥别名集数据的指针。 |