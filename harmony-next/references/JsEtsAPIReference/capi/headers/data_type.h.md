# data_type.h

#### 概述

声明了张量的数据的类型。

**引用文件：** <mindspore/data_type.h>

**库：** libmindspore_lite_ndk.so

**系统能力：** SystemCapability.Ai.MindSpore

**起始版本：** 9

**相关模块：**[MindSpore](../../topics/misc/MindSpore.md)

#### 汇总

#### 枚举

名称typedef关键字描述[OH_AI_DataType](#ZH-CN_TOPIC_0000002497606138__oh_ai_datatype)OH_AI_DataTypeMSTensor保存的数据支持的类型。

#### 枚举类型说明

#### OH_AI_DataType

```ets
enum OH_AI_DataType
```

**描述**

MSTensor保存的数据支持的类型。

**起始版本：** 9

枚举项描述OH_AI_DATATYPE_UNKNOWN = 0未知的数据类型。OH_AI_DATATYPE_OBJECTTYPE_STRING = 12String数据类型。OH_AI_DATATYPE_OBJECTTYPE_LIST = 13List数据类型。OH_AI_DATATYPE_OBJECTTYPE_TUPLE = 14Tuple数据类型。OH_AI_DATATYPE_OBJECTTYPE_TENSOR = 17TensorList数据类型。OH_AI_DATATYPE_NUMBERTYPE_BEGIN = 29Number类型的起始。OH_AI_DATATYPE_NUMBERTYPE_BOOL = 30Bool数据类型。OH_AI_DATATYPE_NUMBERTYPE_INT8 = 32Int8数据类型。OH_AI_DATATYPE_NUMBERTYPE_INT16 = 33Int16数据类型。OH_AI_DATATYPE_NUMBERTYPE_INT32 = 34Int32数据类型。OH_AI_DATATYPE_NUMBERTYPE_INT64 = 35Int64数据类型。OH_AI_DATATYPE_NUMBERTYPE_UINT8 = 37UInt8数据类型。OH_AI_DATATYPE_NUMBERTYPE_UINT16 = 38UInt16数据类型。OH_AI_DATATYPE_NUMBERTYPE_UINT32 = 39UInt32数据类型。OH_AI_DATATYPE_NUMBERTYPE_UINT64 = 40UInt64数据类型。OH_AI_DATATYPE_NUMBERTYPE_FLOAT16 = 42Float16数据类型。OH_AI_DATATYPE_NUMBERTYPE_FLOAT32 = 43Float32数据类型。OH_AI_DATATYPE_NUMBERTYPE_FLOAT64 = 44Float64数据类型。OH_AI_DATATYPE_NUMBERTYPE_END = 46Number类型的结尾。OH_AI_DataTypeInvalid = INT32_MAX无效的数据类型。