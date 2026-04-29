# Rcp_Urls

**概述**

URLs，用于确定主机是否正在使用代理。

起始版本： 5.0.0(12)

相关模块： [RemoteCommunication](RemoteCommunication.md)

所在头文件： [rcp.h](rcp.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| const char * url | 匹配的URL。 |
| struct Rcp_Urls * next | 链式存储。指向下一个Rcp_Urls的指针。 |

**结构体成员变量说明**

**next**

```ets
struct Rcp_Urls* Rcp_Urls::next
```

描述

链式存储。指向下一个[Rcp_Urls](Rcp_Urls.md#ZH-CN_TOPIC_0000002553361485__rcp_urls)的指针。

**url**

```ets
const char* Rcp_Urls::url
```

描述

匹配的URL。