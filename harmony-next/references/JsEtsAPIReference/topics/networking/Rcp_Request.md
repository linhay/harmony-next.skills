# Rcp_Request

**概述**

网络请求。

起始版本： 5.0.0(12)

相关模块： [RemoteCommunication](RemoteCommunication.md)

所在头文件： [rcp.h](rcp.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| char id [RCP_MAX_REQUEST_ID_LEN] | 每个请求的唯一ID。由系统生成。 |
| char * url | 请求URL。 |
| const char * method | 请求方法。默认值为GET。 |
| Rcp_Headers * headers | 请求标头。 |
| Rcp_RequestContent * content | 请求体。 |
| Rcp_Configuration * configuration | 请求配置。请参见Rcp_Configuration。 |
| Rcp_TransferRange * transferRange | HTTP传输范围。该设置将转换为HTTP Range标头。 |
| Rcp_RequestCookies * cookies | 请求Cookie。该设置将转换为HTTP Cookie标头。 |
| void * requestPrivate | 可扩展字段。 |

**结构体成员变量说明**

**configuration**

```ets
Rcp_Configuration* Rcp_Request::configuration
```

描述

请求配置。请参见[Rcp_Configuration](Rcp_Configuration.md)。

**content**

```ets
Rcp_RequestContent* Rcp_Request::content
```

描述

请求体。

**cookies**

```ets
Rcp_RequestCookies* Rcp_Request::cookies
```

描述

请求Cookie。该设置将转换为HTTP Cookie标头。

**headers**

```ets
Rcp_Headers* Rcp_Request::headers
```

描述

请求标头。

**id**

```ets
char Rcp_Request::id[RCP_MAX_REQUEST_ID_LEN]
```

描述

每个请求的唯一ID。由系统生成。

**method**

```ets
const char* Rcp_Request::method
```

描述

请求方法。默认值为GET。

**requestPrivate**

```ets
void* Rcp_Request::requestPrivate
```

描述

可扩展字段。

**transferRange**

```ets
Rcp_TransferRange* Rcp_Request::transferRange
```

描述

HTTP传输范围。该设置将转换为HTTP Range标头。

**url**

```ets
char* Rcp_Request::url
```

描述

请求URL。