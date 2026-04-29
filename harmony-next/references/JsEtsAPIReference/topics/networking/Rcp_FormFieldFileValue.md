# Rcp_FormFieldFileValue

**概述**

表单字段文件值。

起始版本： 5.0.0(12)

相关模块： [RemoteCommunication](RemoteCommunication.md)

所在头文件： [rcp.h](rcp.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| char contentType [RCP_MAX_CONTENT_TYPE_LEN] | 多部分表单数据内容类型。 |
| char remoteFileName [RCP_MAX_FILENAME_LEN] | 多部分表单数据远程文件名。 |
| Rcp_ContentOrPathOrCallbackcontentOrPathOrCb | 多部分表单数据内容。 |

**结构体成员变量说明**

**contentOrPathOrCb**

```ets
Rcp_ContentOrPathOrCallback Rcp_FormFieldFileValue::contentOrPathOrCb
```

描述

多部分表单数据内容。

**contentType**

```ets
char Rcp_FormFieldFileValue::contentType[RCP_MAX_CONTENT_TYPE_LEN]
```

描述

多部分表单数据内容类型。

**remoteFileName**

```ets
char Rcp_FormFieldFileValue::remoteFileName[RCP_MAX_FILENAME_LEN]
```

描述

多部分表单数据远程文件名。