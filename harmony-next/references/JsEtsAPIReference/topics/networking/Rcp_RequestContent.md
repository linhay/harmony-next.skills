# Rcp_RequestContent

**概述**

请求的内容。

起始版本： 5.0.0(12)

相关模块： [RemoteCommunication](RemoteCommunication.md)

所在头文件： [rcp.h](rcp.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| Rcp_ContentTypetype | 表示union中使用的数据类型。 |
| union {   Rcp_Buffer contentStr   Rcp_Form * form   Rcp_MultipartForm * multipartForm   Rcp_GetDataCallback getDataCallback   } | contentStr：文本。 form：表单。 multipartForm：多部分表单。 getDataCallback：使用回调函数获取数据。 |

**结构体成员变量说明**

**contentStr**

```ets
Rcp_Buffer Rcp_RequestContent::contentStr
```

描述

字符串内容。

**form**

```ets
Rcp_Form* Rcp_RequestContent::form
```

描述

表单内容。

**getDataCallback**

```ets
Rcp_GetDataCallback Rcp_RequestContent::getDataCallback
```

描述

回调函数。

**multipartForm**

```ets
Rcp_MultipartForm* Rcp_RequestContent::multipartForm
```

描述

多部分表单内容。

**type**

```ets
Rcp_ContentType Rcp_RequestContent::type
```

描述

表示union中使用的数据类型。