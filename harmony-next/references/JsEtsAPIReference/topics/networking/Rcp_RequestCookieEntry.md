# Rcp_RequestCookieEntry

**概述**

描述请求的所有Cookie键值对。

起始版本： 5.0.0(12)

相关模块： [RemoteCommunication](RemoteCommunication.md)

所在头文件： [rcp.h](rcp.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| char * key | 请求Cookie键值对的键。 |
| char * value | 请求Cookie键值对的值。 |
| struct Rcp_RequestCookieEntry * next | 链式存储。指向下一个Rcp_RequestCookieEntry的指针。 |

**结构体成员变量说明**

**key**

```ets
char* Rcp_RequestCookieEntry::key
```

描述

请求Cookie键值对的键。

**next**

```ets
struct Rcp_RequestCookieEntry* Rcp_RequestCookieEntry::next
```

描述

链式存储。指向下一个[Rcp_RequestCookieEntry](Rcp_RequestCookieEntry.md#ZH-CN_TOPIC_0000002522081556__rcp_requestcookieentry)的指针。

**value**

```ets
char* Rcp_RequestCookieEntry::value
```

描述

请求Cookie键值对的值。