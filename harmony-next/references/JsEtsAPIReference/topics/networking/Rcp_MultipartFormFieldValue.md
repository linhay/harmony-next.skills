# Rcp_MultipartFormFieldValue

**概述**

多部分表单域值，在[Rcp_MultipartForm](RemoteCommunication.md#ZH-CN_TOPIC_0000002522081538__rcp_multipartform)中使用。

起始版本： 5.0.0(12)

相关模块： [RemoteCommunication](RemoteCommunication.md)

所在头文件： [rcp.h](rcp.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| Rcp_MultipartValueType type | 表示union中使用的数据类型。 |
| union {   Rcp_FormFieldValue formValue   Rcp_FormFieldFileValue formFileValue   } | formValue：简单表单数据字段值。 formFileValue：简单表单数据字段文件值。 |
| struct Rcp_MultipartFormFieldValue * next | 指向下一个Rcp_MultipartFormFieldValue。链式存储。 |

**结构体成员变量说明**

**formFileValue**

```ets
Rcp_FormFieldFileValue Rcp_MultipartFormFieldValue::formFileValue
```

描述

简单表单数据字段文件值。

**formValue**

```ets
Rcp_FormFieldValue Rcp_MultipartFormFieldValue::formValue
```

描述

简单表单数据字段值。

**next**

```ets
struct Rcp_MultipartFormFieldValue* Rcp_MultipartFormFieldValue::next
```

描述

指向下一个[Rcp_MultipartFormFieldValue](Rcp_MultipartFormFieldValue.md#ZH-CN_TOPIC_0000002522081552__rcp_multipartformfieldvalue)。链式存储。

**type**

```ets
Rcp_MultipartValueType Rcp_MultipartFormFieldValue::type
```

描述

表示union中使用的数据类型。