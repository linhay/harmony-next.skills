# Rcp_HeaderEntry

**概述**

请求或响应的标头的所有键值对。

起始版本： 5.0.0(12)

相关模块： [RemoteCommunication](RemoteCommunication.md)

所在头文件： [rcp.h](rcp.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| char * key | 键。如果用户希望使用自定义的content-type覆盖系统原有的content-type，键必须使用小写的“content-type”。 |
| Rcp_HeaderValue * value | 值。 |
| struct Rcp_HeaderEntry * next | 链式存储。指向下一个键值对Rcp_HeaderEntry。 |

**结构体成员变量说明**

**key**

```ets
char* Rcp_HeaderEntry::key
```

描述

键。如果用户希望使用自定义的content-type覆盖系统原有的content-type，键必须使用小写的“content-type”。

**next**

```ets
struct Rcp_HeaderEntry* Rcp_HeaderEntry::next
```

描述

链式存储。指向下一个键值对[Rcp_HeaderEntry](Rcp_HeaderEntry.md#ZH-CN_TOPIC_0000002553361469__rcp_headerentry)。

**value**

```ets
Rcp_HeaderValue* Rcp_HeaderEntry::value
```

描述

标头键值对的值。