# Rcp_FormFieldValue

**概述**

简单表单数据字段值，参见[Rcp_Form](RemoteCommunication.md#ZH-CN_TOPIC_0000002522081538__rcp_form)和[Rcp_MultipartFormFieldValue](Rcp_MultipartFormFieldValue.md)。

起始版本： 5.0.0(12)

相关模块： [RemoteCommunication](RemoteCommunication.md)

所在头文件： [rcp.h](rcp.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| Rcp_FormValueTypetype | 表示union中使用的数据类型。 |
| union {   uint8_t varBool   int32_t varInt32   int64_t varInt64   double varDouble   Rcp_Buffer varStr   } | bool类型。 int32类型。 int64类型。 double类型。 string类型。 |
| struct Rcp_FormFieldValue * next | 指向下一个Rcp_FormFieldValue。链式存储。 |

**结构体成员变量说明**

**next**

```ets
struct Rcp_FormFieldValue* Rcp_FormFieldValue::next
```

描述

指向下一个[Rcp_FormFieldValue](Rcp_FormFieldValue.md#ZH-CN_TOPIC_0000002522081548__rcp_formfieldvalue)。链式存储。

**type**

```ets
Rcp_FormValueType Rcp_FormFieldValue::type
```

描述

表示union中使用的数据类型。

**varBool**

```ets
uint8_t Rcp_FormFieldValue::varBool
```

描述

bool类型。

**varDouble**

```ets
double Rcp_FormFieldValue::varDouble
```

描述

double类型。

**varInt32**

```ets
int32_t Rcp_FormFieldValue::varInt32
```

描述

int32类型。

**varInt64**

```ets
int64_t Rcp_FormFieldValue::varInt64
```

描述

int64类型。

**varStr**

```ets
Rcp_Buffer Rcp_FormFieldValue::varStr
```

描述

string类型。