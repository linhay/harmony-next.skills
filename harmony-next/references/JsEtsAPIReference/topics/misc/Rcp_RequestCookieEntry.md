# Rcp_RequestCookieEntry

#### 概述

描述请求的所有Cookie键值对。

**起始版本：** 5.0.0(12)

**相关模块：**[RemoteCommunication](RemoteCommunication.md)

#### 汇总

#### 成员变量

名称

描述

char * [key](Rcp_RequestCookieEntry.md#ZH-CN_TOPIC_0000002282549664__a3412ddb3fe8dd53fdfd78cdc64606dde)

请求Cookie键值对的键。

char * [value](Rcp_RequestCookieEntry.md#ZH-CN_TOPIC_0000002282549664__a9107385a3fbbfc9f224e41b62b6840a2)

请求Cookie键值对的值。

struct [Rcp_RequestCookieEntry](Rcp_RequestCookieEntry.md) * [next](Rcp_RequestCookieEntry.md#ZH-CN_TOPIC_0000002282549664__a0ad803719fa8dabb2e92099b956188c6)

链式存储。指向下一个[Rcp_RequestCookieEntry](Rcp_RequestCookieEntry.md)的指针。

#### 结构体成员变量说明

#### key

```ets
char* Rcp_RequestCookieEntry::key
```

**描述**

请求Cookie键值对的键。

#### next

```ets
struct [Rcp_RequestCookieEntry](Rcp_RequestCookieEntry.md)* Rcp_RequestCookieEntry::next
```

**描述**

链式存储。指向下一个[Rcp_RequestCookieEntry](Rcp_RequestCookieEntry.md)的指针。

#### value

```ets
char* Rcp_RequestCookieEntry::value
```

**描述**

请求Cookie键值对的值。