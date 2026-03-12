# Rcp_CookieAttributeEntry

#### 概述

响应Cookie属性条目。

**起始版本：** 5.0.0(12)

**相关模块：**[RemoteCommunication](RemoteCommunication.md)

#### 汇总

#### 成员变量

名称

描述

const char * [key](Rcp_CookieAttributeEntry.md#ZH-CN_TOPIC_0000002317126033__a4c173743e8b8fdc21094c8e44bc9e916)

键。

const char * [value](Rcp_CookieAttributeEntry.md#ZH-CN_TOPIC_0000002317126033__a66825b3668ef744508b196afbe27ad72)

值。

struct [Rcp_CookieAttributeEntry](Rcp_CookieAttributeEntry.md) * [next](Rcp_CookieAttributeEntry.md#ZH-CN_TOPIC_0000002317126033__a1adcb4e7945ef806942a20d2b6188eba)

链式存储。指向下一个[Rcp_CookieAttributeEntry](Rcp_CookieAttributeEntry.md)的指针。

#### 结构体成员变量说明

#### key

```ets
const char* Rcp_CookieAttributeEntry::key
```

**描述**

键。

#### next

```ets
struct [Rcp_CookieAttributeEntry](Rcp_CookieAttributeEntry.md)* Rcp_CookieAttributeEntry::next
```

**描述**

链式存储。指向下一个[Rcp_CookieAttributeEntry](Rcp_CookieAttributeEntry.md)的指针。

#### value

```ets
const char* Rcp_CookieAttributeEntry::value
```

**描述**

值。