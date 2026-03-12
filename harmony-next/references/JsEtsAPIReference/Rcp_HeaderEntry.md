# Rcp_HeaderEntry

#### 概述

请求或响应的标头的所有键值对。

**起始版本：** 5.0.0(12)

**相关模块：**[RemoteCommunication](RemoteCommunication.md)

#### 汇总

#### 成员变量

名称

描述

char * [key](Rcp_HeaderEntry.md#ZH-CN_TOPIC_0000002317039177__a5fe5651c6fb34ca1c58f9ef27f8b3236)

键。如果用户希望使用自定义的content-type覆盖系统原有的content-type，键必须使用小写的“content-type”。

[Rcp_HeaderValue](Rcp_HeaderValue.md) * [value](Rcp_HeaderEntry.md#ZH-CN_TOPIC_0000002317039177__a3535a6d660132530e59c62d651648455)

值。

struct [Rcp_HeaderEntry](Rcp_HeaderEntry.md) * [next](Rcp_HeaderEntry.md#ZH-CN_TOPIC_0000002317039177__a9f821c0572ebb0e1ad391a13b6db3d4c)

链式存储。指向下一个键值对[Rcp_HeaderEntry](Rcp_HeaderEntry.md)。

#### 结构体成员变量说明

#### key

```ets
char* Rcp_HeaderEntry::key
```

**描述**

键。如果用户希望使用自定义的content-type覆盖系统原有的content-type，键必须使用小写的“content-type”。

#### next

```ets
struct [Rcp_HeaderEntry](Rcp_HeaderEntry.md)* Rcp_HeaderEntry::next
```

**描述**

链式存储。指向下一个键值对[Rcp_HeaderEntry](Rcp_HeaderEntry.md)。

#### value

```ets
[Rcp_HeaderValue](Rcp_HeaderValue.md)* Rcp_HeaderEntry::value
```

**描述**

标头键值对的值。