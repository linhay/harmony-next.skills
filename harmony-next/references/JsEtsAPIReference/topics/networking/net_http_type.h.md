# net_http_type.h

**概述**

定义HTTP请求模块的C接口需要的数据结构。

引用文件： <network/netstack/net_http_type.h>

库： libnet_http.so

系统能力： SystemCapability.Communication.NetStack

起始版本： 20

相关模块： [netstack](Netstack.md)

**汇总**

**结构体**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| Http_Buffer | Http_Buffer | HTTP缓存结构体。 |
| Http_HeaderValue | Http_HeaderValue | 请求或者响应的标头映射的值类型。 |
| Http_HeaderEntry | Http_HeaderEntry | 请求或者响应的标头的所有键值对。 |
| Http_ClientCert | Http_ClientCert | 发送到服务端的客户端证书配置，服务端将通过客户端证书校验客户端身份。 |
| Http_CustomProxy | Http_CustomProxy | 用户自定义代理配置。 |
| Http_Proxy | Http_Proxy | 代理配置结构体。 |
| Http_PerformanceTiming | Http_PerformanceTiming | HTTP响应时间信息，会在Http_Response.performanceTiming中收集。 |
| Http_RequestOptions | Http_RequestOptions | 定义HTTP请求配置的结构体。 |
| Http_Response | Http_Response | 定义HTTP响应的结构体。 |
| Http_Request | Http_Request | HTTP请求结构体。 |
| Http_EventsHandler | Http_EventsHandler | 监听不同HTTP事件的回调函数。 |
| Http_Headers | Http_Headers | HTTP请求或者是响应中的标头。 |

**枚举**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| Http_ErrCode | Http_ErrCode | 定义HTTP请求的错误码。 |
| Http_ResponseCode | Http_ResponseCode | 定义HTTP响应码。 |
| Http_AddressFamilyType | Http_AddressFamilyType | 定义解析目标域名时限定的地址类型。 |
| Http_HttpProtocol | Http_HttpProtocol | HTTP协议版本号枚举定义。 |
| Http_CertType | Http_CertType | 证书类型枚举。 |
| Http_ProxyType | Http_ProxyType | 代理配置类型枚举定义。 |

**宏定义**

| 名称 | 描述 |
| --- | --- |
| OHOS_HTTP_MAX_PATH_LEN 128 | HTTP请求最长目录路径长度。 起始版本： 20 |
| OHOS_HTTP_MAX_STR_LEN 256 | HTTP请求最长字符串长度。 起始版本： 20 |
| OHOS_HTTP_DNS_SERVER_NUM_MAX 3 | HTTP请求最多DNS服务器数量。 起始版本： 20 |
| NET_HTTP_METHOD_GET "GET" | HTTP请求GET方法。 起始版本： 20 |
| NET_HTTPMETHOD_HEAD "HEAD" | HTTP请求HEAD方法。 起始版本： 20 |
| NET_HTTPMETHOD_OPTIONS "OPTIONS" | HTTP请求OPTIONS方法。 起始版本： 20 |
| NET_HTTPMETHOD_TRACE "TRACE" | HTTP请求TRACE方法。 起始版本： 20 |
| NET_HTTPMETHOD_DELETE "DELETE" | HTTP请求DELETE方法。 起始版本： 20 |
| NET_HTTP_METHOD_POST "POST" | HTTP请求POST方法。 起始版本： 20 |
| NET_HTTP_METHOD_PUT "PUT" | HTTP请求PUT方法。 起始版本： 20 |
| NET_HTTP_METHOD_PATCH "CONNECT" | HTTP请求CONNECT方法。 起始版本： 20 |

**函数**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| typedef void (*Http_ResponseCallback)(struct Http_Response *response, uint32_t errCode) | Http_ResponseCallback | 接收到HTTP响应的回调函数。 |
| typedef void (*Http_OnDataReceiveCallback)(const char *data, size_t length) | Http_OnDataReceiveCallback | 接收到数据的回调。 |
| typedef void (*Http_OnProgressCallback)(uint64_t totalSize, uint64_t transferredSize) | Http_OnProgressCallback | 请求/响应数据传输过程中调用的回调函数。 |
| typedef void (*Http_OnHeaderReceiveCallback)(Http_Headers *headers) | Http_OnHeaderReceiveCallback | 收到HTTP响应头的回调函数。 |
| typedef void (*Http_OnVoidCallback)(void) | Http_OnVoidCallback | 请求的DataEnd或Cancel事件回调的回调函数。 |

**枚举类型说明**

**Http_ErrCode**

```ets
enum Http_ErrCode
```

描述

定义HTTP请求的错误码。

起始版本： 20

| 枚举项 | 描述 |
| --- | --- |
| OH_HTTP_RESULT_OK = 0 | 请求成功。 |
| OH_HTTP_PARAMETER_ERROR = 401 | 参数错误。 |
| OH_HTTP_PERMISSION_DENIED = 201 | 权限校验失败。 |
| OH_HTTP_NETSTACK_E_BASE = 2300000 | 基础错误码偏移。 |
| OH_HTTP_UNSUPPORTED_PROTOCOL = (OH_HTTP_NETSTACK_E_BASE + 1) | 不支持的协议。 |
| OH_HTTP_INVALID_URL = (OH_HTTP_NETSTACK_E_BASE + 3) | URL格式错误。 |
| OH_HTTP_RESOLVE_PROXY_FAILED = (OH_HTTP_NETSTACK_E_BASE + 5) | 代理服务器域名解析失败。 |
| OH_HTTP_RESOLVE_HOST_FAILED = (OH_HTTP_NETSTACK_E_BASE + 6) | 域名解析失败。 |
| OH_HTTP_CONNECT_SERVER_FAILED = (OH_HTTP_NETSTACK_E_BASE + 7) | 无法连接到服务器。 |
| OH_HTTP_INVALID_SERVER_RESPONSE = (OH_HTTP_NETSTACK_E_BASE + 8) | 服务器返回非法数据。 |
| OH_HTTP_ACCESS_REMOTE_DENIED = (OH_HTTP_NETSTACK_E_BASE + 9) | 拒绝访问远程资源。 |
| OH_HTTP_HTTP2_FRAMING_ERROR = (OH_HTTP_NETSTACK_E_BASE + 16) | HTTP2框架层出现错误。 |
| OH_HTTP_TRANSFER_PARTIAL_FILE = (OH_HTTP_NETSTACK_E_BASE + 18) | 传输了部分文件。 |
| OH_HTTP_WRITE_DATA_FAILED = (OH_HTTP_NETSTACK_E_BASE + 23) | 无法将接收到的数据写入磁盘或应用程序。 |
| OH_HTTP_UPLOAD_FAILED = (OH_HTTP_NETSTACK_E_BASE + 25) | 上传失败。 |
| OH_HTTP_OPEN_LOCAL_DATA_FAILED = (OH_HTTP_NETSTACK_E_BASE + 26) | 无法打开或读取文件或应用程序中的本地数据。 |
| OH_HTTP_OUT_OF_MEMORY = (OH_HTTP_NETSTACK_E_BASE + 27) | 内存不足。 |
| OH_HTTP_OPERATION_TIMEOUT = (OH_HTTP_NETSTACK_E_BASE + 28) | 操作超时。 |
| OH_HTTP_TOO_MANY_REDIRECTIONS = (OH_HTTP_NETSTACK_E_BASE + 47) | 重定向次数已达到允许的最大值。 |
| OH_HTTP_SERVER_RETURNED_NOTHING = (OH_HTTP_NETSTACK_E_BASE + 52) | 服务器没有返回任何内容（没有标头或数据）。 |
| OH_HTTP_SEND_DATA_FAILED = (OH_HTTP_NETSTACK_E_BASE + 55) | 发送数据失败。 |
| OH_HTTP_RECEIVE_DATA_FAILED = (OH_HTTP_NETSTACK_E_BASE + 56) | 接收数据失败。 |
| OH_HTTP_SSL_CERTIFICATE_ERROR = (OH_HTTP_NETSTACK_E_BASE + 58) | 本地SSL证书错误。 |
| OH_HTTP_SSL_CIPHER_USED_ERROR = (OH_HTTP_NETSTACK_E_BASE + 59) | 指定的加密套件不可用。 |
| OH_HTTP_INVALID_SSL_PEER_CERT = (OH_HTTP_NETSTACK_E_BASE + 60) | SSL对等证书或SSH远程密钥无效。 |
| OH_HTTP_INVALID_ENCODING_FORMAT = (OH_HTTP_NETSTACK_E_BASE + 61) | HTTP编码格式无效。 |
| OH_HTTP_FILE_TOO_LARGE = (OH_HTTP_NETSTACK_E_BASE + 63) | 超出最大文件大小。 |
| OH_HTTP_REMOTE_DISK_FULL = (OH_HTTP_NETSTACK_E_BASE + 70) | 远端磁盘满。 |
| OH_HTTP_REMOTE_FILE_EXISTS = (OH_HTTP_NETSTACK_E_BASE + 73) | 远端文件已存在。 |
| OH_HTTP_SSL_CA_NOT_EXIST = (OH_HTTP_NETSTACK_E_BASE + 77) | SSL CA证书不存在或无法访问。 |
| OH_HTTP_REMOTE_FILE_NOT_FOUND = (OH_HTTP_NETSTACK_E_BASE + 78) | 远端文件未找到。 |
| OH_HTTP_AUTHENTICATION_ERROR = (OH_HTTP_NETSTACK_E_BASE + 94) | 身份验证错误。 |
| OH_HTTP_ACCESS_DOMAIN_NOT_ALLOWED = (OH_HTTP_NETSTACK_E_BASE + 998) | 不允许访问该域。 |
| OH_HTTP_UNKNOWN_ERROR = (OH_HTTP_NETSTACK_E_BASE + 999) | 未知错误。 |

**Http_ResponseCode**

```ets
enum Http_ResponseCode
```

描述

定义HTTP响应码。

起始版本： 20

| 枚举项 | 描述 |
| --- | --- |
| OH_HTTP_OK = 200 | 请求成功。 |
| OH_HTTP_CREATED = 201 | 成功请求并创建新资源。 |
| OH_HTTP_ACCEPTED = 202 | 请求已被接受但尚未完全处理。 |
| OH_HTTP_NON_AUTHORITATIVE_INFO = 203 | 请求成功。但是有未授权信息。 |
| OH_HTTP_NO_CONTENT = 204 | 服务器处理成功，但未返回内容。 |
| OH_HTTP_RESET = 205 | 重置内容。 |
| OH_HTTP_PARTIAL = 206 | 服务器成功处理了部分GET请求。 |
| OH_HTTP_MULTI_CHOICE = 300 | 多种选择。 |
| OH_HTTP_MOVED_PERM = 301 | 请求的资源已永久移动到新的URI，返回信息将包含新的URI。浏览器将自动重定向到新的URI。 |
| OH_HTTP_MOVED_TEMP = 302 | 临时重定向。 |
| OH_HTTP_SEE_OTHER = 303 | 查看其他地址。请求的资源已移动到新的URL，客户端应使用GET方法访问该URL。 |
| OH_HTTP_NOT_MODIFIED = 304 | 请求的资源没有修改。 |
| OH_HTTP_USE_PROXY = 305 | 请求资源需要使用代理访问。 |
| OH_HTTP_BAD_REQUEST = 400 | 服务器无法理解客户端请求的语法错误。 |
| OH_HTTP_UNAUTHORIZED = 401 | 请求用户身份验证。 |
| OH_HTTP_PAYMENT_REQUIRED = 402 | 保留以供将来使用。 |
| OH_HTTP_FORBIDDEN = 403 | 服务器理解来自请求客户端的请求，但拒绝执行。 |
| OH_HTTP_NOT_FOUND = 404 | 服务器无法根据客户端的请求找到资源。 |
| OH_HTTP_BAD_METHOD = 405 | 客户端请求中的方法被禁止。 |
| OH_HTTP_NOT_ACCEPTABLE = 406 | 服务器无法根据客户端请求的内容特征完成请求。 |
| OH_HTTP_PROXY_AUTH = 407 | 请求验证代理人的身份。 |
| OH_HTTP_CLIENT_TIMEOUT = 408 | 请求耗时太长，超时。 |
| OH_HTTP_CONFLICT = 409 | 服务器在完成客户端的PUT请求时可能返回此代码，因为服务器在处理请求时发生冲突。 |
| OH_HTTP_GONE = 410 | 客户端请求的资源不再存在。 |
| OH_HTTP_LENGTH_REQUIRED = 411 | 服务器无法处理客户端发送的不带Content Length的请求信息。 |
| OH_HTTP_PRECON_FAILED = 412 | 向客户端请求信息的前提条件不正确。 |
| OH_HTTP_ENTITY_TOO_LARGE = 413 | 请求被拒绝，因为请求的实体太大，服务器无法处理。 |
| OH_HTTP_REQUEST_TOO_LONG = 414 | 请求的URI超过了服务器能够解析的长度，服务器无法处理。 |
| OH_HTTP_UNSUPPORTED_TYPE = 415 | 服务器无法处理请求的格式。 |
| OH_HTTP_RANGE_NOT_MET = 416 | 请求的范围无法满足。 |
| OH_HTTP_INTERNAL_ERROR = 500 | 内部服务器错误，无法完成请求。 |
| OH_HTTP_NOT_IMPLEMENTED = 501 | 服务器不支持请求的功能，无法完成请求。 |
| OH_HTTP_BAD_GATEWAY = 502 | 充当网关或代理的服务器从远程服务器收到无效请求。 |
| OH_HTTP_UNAVAILABLE = 503 | 由于超载或系统维护，服务器暂时无法处理客户端请求。 |
| OH_HTTP_GATEWAY_TIMEOUT = 504 | 作为网关的服务器没有及时从远程服务器获取请求。 |
| OH_HTTP_VERSION = 505 | 服务器请求的HTTP协议版本。 |

**Http_AddressFamilyType**

```ets
enum Http_AddressFamilyType
```

描述

定义解析目标域名时限定的地址类型。

起始版本： 20

| 枚举项 | 描述 |
| --- | --- |
| HTTP_ADDRESS_FAMILY_DEFAULT = 0 | 默认值，系统将自行选择目标域名的IPv4地址或IPv6地址。 |
| HTTP_ADDRESS_FAMILY_ONLY_V4 = 1 | 系统仅解析目标域名的IPv4地址，忽略IPv6地址。 |
| HTTP_ADDRESS_FAMILY_ONLY_V6 = 2 | 系统仅解析目标域名的IPv6地址，忽略IPv4地址。 |

**Http_HttpProtocol**

```ets
enum Http_HttpProtocol
```

描述

HTTP协议版本号枚举定义。

起始版本： 20

| 枚举项 | 描述 |
| --- | --- |
| OH_HTTP_NONE = 0 | 跟随curl的协议版本选择。 |
| OH_HTTP1_1 | HTTP1.1版本。 |
| OH_HTTP2 | HTTP2版本。 |
| OH_HTTP3 | HTTP3版本。 |

**Http_CertType**

```ets
enum Http_CertType
```

描述

证书类型枚举。

起始版本： 20

| 枚举项 | 描述 |
| --- | --- |
| OH_HTTP_PEM = 0 | PEM证书类型。 |
| OH_HTTP_DER = 1 | DER证书类型。 |
| OH_HTTP_P12 = 2 | P12证书类型。 |

**Http_ProxyType**

```ets
enum Http_ProxyType
```

描述

代理配置类型枚举定义。

起始版本： 20

| 枚举项 | 描述 |
| --- | --- |
| HTTP_PROXY_NOT_USE | 不使用代理。 |
| HTTP_PROXY_SYSTEM | 使用系统代理。 |
| HTTP_PROXY_CUSTOM | 使用用户自定义代理。 |

**函数说明**

**Http_ResponseCallback()**

```ets
typedef void (*Http_ResponseCallback)(struct Http_Response *response, uint32_t errCode)
```

描述

接收到HTTP响应的回调函数。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| struct Http_Response *response | HTTP响应结构体，指向Http_Response的指针，参考Http_Response。 |
| uint32_t errCode | 响应码。 |

**Http_OnDataReceiveCallback()**

```ets
typedef void (*Http_OnDataReceiveCallback)(const char *data, size_t length)
```

描述

接收到数据的回调。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| const char *data | 响应体。 |
| size_t length | 响应体的长度。 |

**Http_OnProgressCallback()**

```ets
typedef void (*Http_OnProgressCallback)(uint64_t totalSize, uint64_t transferredSize)
```

描述

请求/响应数据传输过程中调用的回调函数。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| uint64_t totalSize | 数据总大小。 |
| uint64_t transferredSize | 已传输的数据大小。 |

**Http_OnHeaderReceiveCallback()**

```ets
typedef void (*Http_OnHeaderReceiveCallback)(Http_Headers *headers)
```

描述

收到HTTP响应头的回调函数。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| Http_Headers *headers | 接收到的请求头，指向Http_Headers的指针，参考Http_Headers。 |

**Http_OnVoidCallback()**

```ets
typedef void (*Http_OnVoidCallback)(void)
```

描述

请求的DataEnd或Cancel事件回调的回调函数。

起始版本： 20