# ImageEffect_DataValue

```ets
typedef union ImageEffect_DataValue {...} ImageEffect_DataValue
```

#### 概述

数据值联合体。

**起始版本：** 12

**相关模块：**[ImageEffect](ImageEffect.md)

**所在头文件：**[image_effect_filter.h](../../capi/headers/image_effect_filter.h.md)

#### 汇总

#### 成员变量

名称描述int32_t int32Value整型值，对应[EFFECT_DATA_TYPE_INT32](../../capi/headers/image_effect_filter.h.md#ZH-CN_TOPIC_0000002497445880__imageeffect_datatype)。float floatValue单精度浮点值，对应[EFFECT_DATA_TYPE_FLOAT](../../capi/headers/image_effect_filter.h.md#ZH-CN_TOPIC_0000002497445880__imageeffect_datatype)。double doubleValue双精度浮点值，对应[EFFECT_DATA_TYPE_DOUBLE](../../capi/headers/image_effect_filter.h.md#ZH-CN_TOPIC_0000002497445880__imageeffect_datatype)。char charValue字节值，对应[EFFECT_DATA_TYPE_CHAR](../../capi/headers/image_effect_filter.h.md#ZH-CN_TOPIC_0000002497445880__imageeffect_datatype)。long longValue长整型值，对应[EFFECT_DATA_TYPE_LONG](../../capi/headers/image_effect_filter.h.md#ZH-CN_TOPIC_0000002497445880__imageeffect_datatype)。bool boolValue布尔值，对应[EFFECT_DATA_TYPE_BOOL](../../capi/headers/image_effect_filter.h.md#ZH-CN_TOPIC_0000002497445880__imageeffect_datatype)。void* ptrValue指针值，对应[EFFECT_DATA_TYPE_PTR](../../capi/headers/image_effect_filter.h.md#ZH-CN_TOPIC_0000002497445880__imageeffect_datatype)。