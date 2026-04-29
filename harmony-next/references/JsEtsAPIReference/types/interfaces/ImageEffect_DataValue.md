# ImageEffect_DataValue

```ets
typedef union ImageEffect_DataValue {...} ImageEffect_DataValue
```

**概述**

数据值联合体。

起始版本： 12

相关模块： [ImageEffect](ImageEffect.md)

所在头文件： [image_effect_filter.h](image_effect_filter.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| int32_t int32Value | 整型值，对应EFFECT_DATA_TYPE_INT32。 |
| float floatValue | 单精度浮点值，对应EFFECT_DATA_TYPE_FLOAT。 |
| double doubleValue | 双精度浮点值，对应EFFECT_DATA_TYPE_DOUBLE。 |
| char charValue | 字节值，对应EFFECT_DATA_TYPE_CHAR。 |
| long longValue | 长整型值，对应EFFECT_DATA_TYPE_LONG。 |
| bool boolValue | 布尔值，对应EFFECT_DATA_TYPE_BOOL。 |
| void* ptrValue | 指针值，对应EFFECT_DATA_TYPE_PTR。 |