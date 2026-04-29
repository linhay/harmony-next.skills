# OH_Huks_Result

```ets
struct OH_Huks_Result {...}
```

**概述**

表示状态返回数据，包括返回码和消息。

起始版本： 9

相关模块： [HuksTypeApi](HuksTypeApi.md)

所在头文件： [native_huks_type.h](native_huks_type.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| int32_t errorCode | 状态返回码，参考OH_Huks_ErrCode。 |
| const char *errorMsg | 对状态返回码的说明信息。 |
| uint8_t *data | 其他返回数据。 |