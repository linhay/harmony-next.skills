# Rcp_HeaderValue

**概述**

请求或响应的标头映射的值类型。

起始版本： 5.0.0(12)

相关模块： [RemoteCommunication](RemoteCommunication.md)

所在头文件： [rcp.h](rcp.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| char * value | 标头键值对的值。 |
| struct Rcp_HeaderValue * next | 链式存储。指向下一个Rcp_HeaderValue。 |

**结构体成员变量说明**

**next**

```ets
struct Rcp_HeaderValue* Rcp_HeaderValue::next
```

描述

链式存储。指向下一个[Rcp_HeaderValue](Rcp_HeaderValue.md#ZH-CN_TOPIC_0000002522241544__rcp_headervalue)。

**value**

```ets
char* Rcp_HeaderValue::value
```

描述

标头键值对的值。