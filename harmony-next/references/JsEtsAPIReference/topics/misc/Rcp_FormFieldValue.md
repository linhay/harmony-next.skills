# Rcp_FormFieldValue

#### 概述

简单表单数据字段值，参见[Rcp_Form](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga40787f67faf4ea7111e4cda03f3f16be)和[Rcp_MultipartFormFieldValue](../media/Rcp_MultipartFormFieldValue.md)。

**起始版本：** 5.0.0(12)

**相关模块：**[RemoteCommunication](RemoteCommunication.md)

#### 汇总

#### 成员变量

名称

描述

[Rcp_FormValueType](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga9d851389347a39bd4bb849ac31cfa478)[type](Rcp_FormFieldValue.md#ZH-CN_TOPIC_0000002317125997__aa2f5ee901ec18d3a45a3a4b32ce648a0)

表示union中使用的数据类型。

****union {

union结构。

uint8_t [varBool](Rcp_FormFieldValue.md#ZH-CN_TOPIC_0000002317125997__adfd646a1efd2853ce64eee38cc1f2cc2)

bool类型。

int32_t [varInt32](Rcp_FormFieldValue.md#ZH-CN_TOPIC_0000002317125997__ad63df8004b42c748ea9e43e33dc63f6d)

int32类型。

int64_t [varInt64](Rcp_FormFieldValue.md#ZH-CN_TOPIC_0000002317125997__a5392f4cacec7a90c59c5e857f022da4b)

int64类型。

double [varDouble](Rcp_FormFieldValue.md#ZH-CN_TOPIC_0000002317125997__ae1dd3fa224b13f7a3daefddffda41721)

double类型。

[Rcp_Buffer](Rcp_Buffer.md)[varStr](Rcp_FormFieldValue.md#ZH-CN_TOPIC_0000002317125997__a0e38aaf495895692510bc46b36acf4ad)

string类型。

} **data**

data中使用的数据由type进行区分。

struct [Rcp_FormFieldValue](Rcp_FormFieldValue.md) * [next](Rcp_FormFieldValue.md#ZH-CN_TOPIC_0000002317125997__a3ceed646c6f06c8249ff962782da0068)

指向下一个[Rcp_FormFieldValue](Rcp_FormFieldValue.md)。链式存储。

#### 结构体成员变量说明

#### next

```ets
struct [Rcp_FormFieldValue](Rcp_FormFieldValue.md)* Rcp_FormFieldValue::next
```

**描述**

指向下一个[Rcp_FormFieldValue](Rcp_FormFieldValue.md)。链式存储。

#### type

```ets
[Rcp_FormValueType](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga9d851389347a39bd4bb849ac31cfa478) Rcp_FormFieldValue::type
```

**描述**

表示union中使用的数据类型。

#### varBool

```ets
uint8_t Rcp_FormFieldValue::varBool
```

**描述**

bool。

#### varDouble

```ets
double Rcp_FormFieldValue::varDouble
```

**描述**

double。

#### varInt32

```ets
int32_t Rcp_FormFieldValue::varInt32
```

**描述**

int32。

#### varInt64

```ets
int64_t Rcp_FormFieldValue::varInt64
```

**描述**

int64。

#### varStr

```ets
[Rcp_Buffer](Rcp_Buffer.md) Rcp_FormFieldValue::varStr
```

**描述**

string。