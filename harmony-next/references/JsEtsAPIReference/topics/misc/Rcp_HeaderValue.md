# Rcp_HeaderValue

#### 概述

请求或响应的标头映射的值类型。

**起始版本：** 5.0.0(12)

**相关模块：**[RemoteCommunication](RemoteCommunication.md)

#### 汇总

#### 成员变量

名称

描述

char * [value](Rcp_HeaderValue.md#ZH-CN_TOPIC_0000002317039169__a2808b89bd4ee544a9167315c782d5dc0)

标头键值对的值。

struct [Rcp_HeaderValue](Rcp_HeaderValue.md) * [next](Rcp_HeaderValue.md#ZH-CN_TOPIC_0000002317039169__a6f80339bd4632840890dbed4516a2c7c)

链式存储。指向下一个[Rcp_HeaderValue](Rcp_HeaderValue.md)。

#### 结构体成员变量说明

#### next

```ets
struct [Rcp_HeaderValue](Rcp_HeaderValue.md)* Rcp_HeaderValue::next
```

**描述**

链式存储。指向下一个[Rcp_HeaderValue](Rcp_HeaderValue.md)。

#### value

```ets
char* Rcp_HeaderValue::value
```

**描述**

值。