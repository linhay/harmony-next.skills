# Rcp_ContentOrPathOrCallback

**概述**

[Rcp_FormFieldFileValue](Rcp_FormFieldFileValue.md)中使用的简单表单数据字段值。

起始版本： 5.0.0(12)

相关模块： [RemoteCommunication](RemoteCommunication.md)

所在头文件： [rcp.h](rcp.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| Rcp_ContentOrPathOrCallbackTypetype | 表示union中使用的数据类型。 |
| union {   Rcp_Buffer content   char path [RCP_MAX_PATH_LEN]   Rcp_GetDataCallback callback   } | content: 文本数据。 path: 文件路径。 callback: 获取数据的回调函数。 |

**结构体成员变量说明**

**callback**

```ets
Rcp_GetDataCallback Rcp_ContentOrPathOrCallback::callback
```

描述

获取数据的回调。

**content**

```ets
Rcp_Buffer Rcp_ContentOrPathOrCallback::content
```

描述

文本数据。

**path**

```ets
char Rcp_ContentOrPathOrCallback::path[RCP_MAX_PATH_LEN]
```

描述

文件路径。

**type**

```ets
Rcp_ContentOrPathOrCallbackType Rcp_ContentOrPathOrCallback::type
```

描述

union中使用的数据类型。