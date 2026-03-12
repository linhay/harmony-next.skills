# Rcp_MultipartFormFieldValue

#### 概述

多部分表单域值，在[Rcp_MultipartForm](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga9f974771548d3ed2054aba0e7506fef9)中使用。

**起始版本：** 5.0.0(12)

**相关模块：**[RemoteCommunication](RemoteCommunication.md)

#### 汇总

#### 成员变量

名称

描述

[Rcp_MultipartValueType](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga76d003b4f9a244c9d11def4128ceeda8)[type](Rcp_MultipartFormFieldValue.md#ZH-CN_TOPIC_0000002282446434__ae2593c817ecd64051feacb47ea40e647)

表示union中使用的数据类型。

****union {

union结构。

[Rcp_FormFieldValue](Rcp_FormFieldValue.md)[formValue](Rcp_MultipartFormFieldValue.md#ZH-CN_TOPIC_0000002282446434__a5fa2b6978205158b9df2f332b8de46ee)

简单表单数据字段值。

[Rcp_FormFieldFileValue](Rcp_FormFieldFileValue.md)[formFileValue](Rcp_MultipartFormFieldValue.md#ZH-CN_TOPIC_0000002282446434__ada1b5ea030493ddc6c0b77c0fd6314b7)

简单表单数据字段文件值。

} **data**

data中使用的数据由type进行区分。

struct [Rcp_MultipartFormFieldValue](Rcp_MultipartFormFieldValue.md) * [next](Rcp_MultipartFormFieldValue.md#ZH-CN_TOPIC_0000002282446434__abb8d932651a02819e0a94d6af317f845)

指向下一个[Rcp_MultipartFormFieldValue](Rcp_MultipartFormFieldValue.md)。链式存储。

#### 结构体成员变量说明

#### formFileValue

```ets
[Rcp_FormFieldFileValue](Rcp_FormFieldFileValue.md) Rcp_MultipartFormFieldValue::formFileValue
```

**描述**

简单表单数据字段文件值。

#### formValue

```ets
[Rcp_FormFieldValue](Rcp_FormFieldValue.md) Rcp_MultipartFormFieldValue::formValue
```

**描述**

简单表单数据字段值。

#### next

```ets
struct [Rcp_MultipartFormFieldValue](Rcp_MultipartFormFieldValue.md)* Rcp_MultipartFormFieldValue::next
```

**描述**

指向下一个[Rcp_MultipartFormFieldValue](Rcp_MultipartFormFieldValue.md)。链式存储。

#### type

```ets
[Rcp_MultipartValueType](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga76d003b4f9a244c9d11def4128ceeda8) Rcp_MultipartFormFieldValue::type
```

**描述**

表示union中使用的数据类型。