# ImageEffect_Any

```ets
typedef struct ImageEffect_Any {...} ImageEffect_Any
```

**概述**

参数结构体。

起始版本： 12

相关模块： [ImageEffect](ImageEffect.md)

所在头文件： [image_effect_filter.h](image_effect_filter.h.md)

**汇总**

**成员变量**

支持C++语言语法的声明如下：

| 名称 | 描述 |
| --- | --- |
| ImageEffect_DataType dataType = ImageEffect_DataType::EFFECT_DATA_TYPE_UNKNOWN | 参数类型，默认为未定义类型。 |
| ImageEffect_DataValue dataValue = { 0 } | 参数值，默认为空。 |

支持C语言语法的声明如下：

| 名称 | 描述 |
| --- | --- |
| ImageEffect_DataType dataType | 参数类型。 |
| ImageEffect_DataValue dataValue | 参数值。 |