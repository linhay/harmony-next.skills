# Rcp_Exclusions

**概述**

代理配置中用于过滤不使用代理的urls。

如果[Rcp_Request.url](Rcp_Request.md#ZH-CN_TOPIC_0000002522241550__url)匹配[Rcp_Exclusions](Rcp_Exclusions.md#ZH-CN_TOPIC_0000002522241542__rcp_exclusions)规则，则[Rcp_Request](Rcp_Request.md)不会使用代理。

起始版本： 5.0.0(12)

相关模块： [RemoteCommunication](RemoteCommunication.md)

所在头文件： [rcp.h](rcp.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| Rcp_ExclusionsValueTypetype | 表示union中使用的数据类型。 |
| union {   Rcp_Urls * urls   Rcp_ExclusionFunction exclusionFunction   } | Urls。链式存储url。 回调函数。通过回调函数过滤url。 |

**结构体成员变量说明**

**exclusionFunction**

```ets
Rcp_ExclusionFunction Rcp_Exclusions::exclusionFunction
```

描述

通过回调过滤。

**type**

```ets
Rcp_ExclusionsValueType Rcp_Exclusions::type
```

描述

表示union中使用的数据类型。

**urls**

```ets
Rcp_Urls* Rcp_Exclusions::urls
```

描述

Urls。