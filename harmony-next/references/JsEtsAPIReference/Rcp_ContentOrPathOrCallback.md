# Rcp_ContentOrPathOrCallback

#### 概述

[Rcp_FormFieldFileValue](Rcp_FormFieldFileValue.md)中使用的简单表单数据字段值。

**起始版本：** 5.0.0(12)

**相关模块：**[RemoteCommunication](RemoteCommunication.md)

#### 汇总

#### 成员变量

名称

描述

[Rcp_ContentOrPathOrCallbackType](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__gaa5a592f4e68a1dd43f5f41e95199a5e4)[type](Rcp_ContentOrPathOrCallback.md#ZH-CN_TOPIC_0000002282549716__ab083ea1a78b6bb4d37728fdb63258ac9)

表示union中使用的数据类型。

union {

union结构。data中使用的数据由type进行区分。

[Rcp_Buffer](Rcp_Buffer.md)[content](Rcp_ContentOrPathOrCallback.md#ZH-CN_TOPIC_0000002282549716__a9a98334505537018eec3356254ef6340)

content: 文本数据。

char [path](Rcp_ContentOrPathOrCallback.md#ZH-CN_TOPIC_0000002282549716__a3c4cb1ec63c7e30ef25f3e8c04007639) [[RCP_MAX_PATH_LEN](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga3dac667ae8b6fa64f2fede1e77804e12)]

path: 文件路径。

[Rcp_GetDataCallback](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__gac0ac73f33252239ff47a648fe3aa6bd5)[callback](Rcp_ContentOrPathOrCallback.md#ZH-CN_TOPIC_0000002282549716__a307b3cb12a976b3e3555b20dc0f5d0bd)

callback: 获取数据的回调函数。

} **data**

data中使用的数据由type进行区分。

#### 结构体成员变量说明

#### callback

```ets
[Rcp_GetDataCallback](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__gac0ac73f33252239ff47a648fe3aa6bd5) Rcp_ContentOrPathOrCallback::callback
```

**描述**

获取数据的回调。

#### content

```ets
[Rcp_Buffer](Rcp_Buffer.md) Rcp_ContentOrPathOrCallback::content
```

**描述**

文本数据。

#### path

```ets
char Rcp_ContentOrPathOrCallback::path[[RCP_MAX_PATH_LEN](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga3dac667ae8b6fa64f2fede1e77804e12)]
```

**描述**

文件路径。

#### type

```ets
[Rcp_ContentOrPathOrCallbackType](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__gaa5a592f4e68a1dd43f5f41e95199a5e4) Rcp_ContentOrPathOrCallback::type
```

**描述**

union中使用的数据类型。