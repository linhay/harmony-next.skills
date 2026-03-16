# Rcp_RequestContent

#### 概述

请求的内容。

**起始版本：** 5.0.0(12)

**相关模块：**[RemoteCommunication](RemoteCommunication.md)

#### 汇总

#### 成员变量

名称

描述

[Rcp_ContentType](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga05daeab5ad8d265834b4a1b4e61cd8fa)[type](Rcp_RequestContent.md#ZH-CN_TOPIC_0000002282446458__a46cdb54d4c402f9eca88b46c3746f913)

表示union中使用的数据类型。

****union {

union结构。data中使用的数据由type进行区分。

[Rcp_Buffer](Rcp_Buffer.md)[contentStr](Rcp_RequestContent.md#ZH-CN_TOPIC_0000002282446458__a81dfde6bdcabe53dd1ca25f85173d19a)

contentStr：文本。

[Rcp_Form](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga40787f67faf4ea7111e4cda03f3f16be) * [form](Rcp_RequestContent.md#ZH-CN_TOPIC_0000002282446458__a385cd35b8a47800f13a6ef5520842c58)

form：表单。

[Rcp_MultipartForm](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga9f974771548d3ed2054aba0e7506fef9) * [multipartForm](Rcp_RequestContent.md#ZH-CN_TOPIC_0000002282446458__afb9b3ece4b637e347bafc3d98899ae45)

multipartForm：多部分表单。

[Rcp_GetDataCallback](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__gac0ac73f33252239ff47a648fe3aa6bd5)[getDataCallback](Rcp_RequestContent.md#ZH-CN_TOPIC_0000002282446458__a042146cb217fe387a22d8538de6b147c)

getDataCallback：使用回调函数获取数据。

} **data**

data中使用的数据由type进行区分。

#### 结构体成员变量说明

#### contentStr

```ets
[Rcp_Buffer](Rcp_Buffer.md) Rcp_RequestContent::contentStr
```

**描述**

字符串内容。

#### form

```ets
[Rcp_Form](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga40787f67faf4ea7111e4cda03f3f16be)* Rcp_RequestContent::form
```

**描述**

表单内容。

#### getDataCallback

```ets
[Rcp_GetDataCallback](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__gac0ac73f33252239ff47a648fe3aa6bd5) Rcp_RequestContent::getDataCallback
```

**描述**

回调函数。

#### multipartForm

```ets
[Rcp_MultipartForm](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga9f974771548d3ed2054aba0e7506fef9)* Rcp_RequestContent::multipartForm
```

**描述**

多部分表单内容。

#### type

```ets
[Rcp_ContentType](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga05daeab5ad8d265834b4a1b4e61cd8fa) Rcp_RequestContent::type
```

**描述**

表示union中使用的数据类型。