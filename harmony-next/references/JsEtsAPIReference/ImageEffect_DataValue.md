# ImageEffect_DataValue

```ets
typedef union ImageEffect_DataValue {...} ImageEffect_DataValue
```

#### 概述

数据值联合体。

**起始版本：** 12

**相关模块：**[ImageEffect](ImageEffect.md)

**所在头文件：**[image_effect_filter.h](image_effect_filter.h.md)

#### 汇总

#### 成员变量

名称描述int32_t int32Value整型值，对应[EFFECT_DATA_TYPE_INT32](image_effect_filter.h.md#ZH-CN_TOPIC_0000002497445880__imageeffect_datatype)。float floatValue单精度浮点值，对应[EFFECT_DATA_TYPE_FLOAT](image_effect_filter.h.md#ZH-CN_TOPIC_0000002497445880__imageeffect_datatype)。double doubleValue双精度浮点值，对应[EFFECT_DATA_TYPE_DOUBLE](image_effect_filter.h.md#ZH-CN_TOPIC_0000002497445880__imageeffect_datatype)。char charValue字节值，对应[EFFECT_DATA_TYPE_CHAR](image_effect_filter.h.md#ZH-CN_TOPIC_0000002497445880__imageeffect_datatype)。long longValue长整型值，对应[EFFECT_DATA_TYPE_LONG](image_effect_filter.h.md#ZH-CN_TOPIC_0000002497445880__imageeffect_datatype)。bool boolValue布尔值，对应[EFFECT_DATA_TYPE_BOOL](image_effect_filter.h.md#ZH-CN_TOPIC_0000002497445880__imageeffect_datatype)。void* ptrValue指针值，对应[EFFECT_DATA_TYPE_PTR](image_effect_filter.h.md#ZH-CN_TOPIC_0000002497445880__imageeffect_datatype)。