# Rcp_CookieAttributeEntry

**概述**

响应Cookie属性条目。

起始版本： 5.0.0(12)

相关模块： [RemoteCommunication](RemoteCommunication.md)

所在头文件： [rcp.h](rcp.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| const char * key | 键。 |
| const char * value | 值。 |
| struct Rcp_CookieAttributeEntry * next | 链式存储。指向下一个Rcp_CookieAttributeEntry的指针。 |

**结构体成员变量说明**

**key**

```ets
const char* Rcp_CookieAttributeEntry::key
```

描述

键。

**next**

```ets
struct Rcp_CookieAttributeEntry* Rcp_CookieAttributeEntry::next
```

描述

链式存储。指向下一个[Rcp_CookieAttributeEntry](Rcp_CookieAttributeEntry.md#ZH-CN_TOPIC_0000002522241538__rcp_cookieattributeentry)的指针。

**value**

```ets
const char* Rcp_CookieAttributeEntry::value
```

描述

值。