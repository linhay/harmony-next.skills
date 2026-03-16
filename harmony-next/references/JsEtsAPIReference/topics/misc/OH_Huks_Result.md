# OH_Huks_Result

```ets
struct OH_Huks_Result {...}
```

#### 概述

表示状态返回数据，包括返回码和消息。

**起始版本：** 9

**相关模块：**[HuksTypeApi](../networking/HuksTypeApi.md)

**所在头文件：**[native_huks_type.h](../../capi/headers/native_huks_type.h.md)

#### 汇总

#### 成员变量

名称描述int32_t errorCode状态返回码，参考[OH_Huks_ErrCode](../../capi/headers/native_huks_type.h.md#ZH-CN_TOPIC_0000002529285393__oh_huks_errcode)。const char *errorMsg对状态返回码的说明信息。uint8_t *data其他返回数据。