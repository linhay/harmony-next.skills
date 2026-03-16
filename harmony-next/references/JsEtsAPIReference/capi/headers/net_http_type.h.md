# net_http_type.h

#### 概述

定义HTTP请求模块的C接口需要的数据结构。

**引用文件：** <network/netstack/net_http_type.h>

**库：** libnet_http.so

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 20

**相关模块：**[netstack](../../topics/networking/Netstack.md)

#### 汇总

#### 结构体

名称typedef关键字描述[Http_Buffer](../../topics/networking/Http_Buffer.md)Http_BufferHTTP缓存结构体。[Http_HeaderValue](../../topics/networking/Http_HeaderValue.md)Http_HeaderValue请求或者响应的标头映射的值类型。[Http_HeaderEntry](../../topics/networking/Http_HeaderEntry.md)Http_HeaderEntry请求或者响应的标头的所有键值对。[Http_ClientCert](../../topics/networking/Http_ClientCert.md)Http_ClientCert发送到服务端的客户端证书配置，服务端将通过客户端证书校验客户端身份。[Http_CustomProxy](../../topics/networking/Http_CustomProxy.md)Http_CustomProxy用户自定义代理配置。[Http_Proxy](../../topics/networking/Http_Proxy.md)Http_Proxy代理配置结构体。[Http_PerformanceTiming](../../topics/networking/Http_PerformanceTiming.md)Http_PerformanceTimingHTTP响应时间信息，会在[Http_Response.performanceTiming](../../topics/networking/Http_Response.md#ZH-CN_TOPIC_0000002497605476__成员变量)中收集。[Http_RequestOptions](../../topics/networking/Http_RequestOptions.md)Http_RequestOptions定义HTTP请求配置的结构体。[Http_Response](../../topics/networking/Http_Response.md)Http_Response定义HTTP响应的结构体。[Http_Request](../../topics/networking/Http_Request.md)Http_RequestHTTP请求结构体。[Http_EventsHandler](../../topics/networking/Http_EventsHandler.md)Http_EventsHandler监听不同HTTP事件的回调函数。[Http_Headers](../../topics/networking/Http_Headers.md)Http_HeadersHTTP请求或者是响应中的标头。

#### 枚举

名称typedef关键字描述[Http_ErrCode](#ZH-CN_TOPIC_0000002497605460__http_errcode)Http_ErrCode定义HTTP请求的错误码。[Http_ResponseCode](#ZH-CN_TOPIC_0000002497605460__http_responsecode)Http_ResponseCode定义HTTP响应码。[Http_AddressFamilyType](#ZH-CN_TOPIC_0000002497605460__http_addressfamilytype)Http_AddressFamilyType定义解析目标域名时限定的地址类型。[Http_HttpProtocol](#ZH-CN_TOPIC_0000002497605460__http_httpprotocol)Http_HttpProtocolHTTP协议版本号枚举定义。[Http_CertType](#ZH-CN_TOPIC_0000002497605460__http_certtype)Http_CertType证书类型枚举。[Http_ProxyType](#ZH-CN_TOPIC_0000002497605460__http_proxytype)Http_ProxyType代理配置类型枚举定义。

#### 宏定义

名称描述OHOS_HTTP_MAX_PATH_LEN 128

HTTP请求最长目录路径长度。

**起始版本：** 20

**系统能力：** SystemCapability.Communication.NetStack

OHOS_HTTP_MAX_STR_LEN 256

HTTP请求最长字符串长度。

**起始版本：** 20

**系统能力：** SystemCapability.Communication.NetStack

OHOS_HTTP_DNS_SERVER_NUM_MAX 3

HTTP请求最多DNS服务器数量。

**起始版本：** 20

**系统能力：** SystemCapability.Communication.NetStack

NET_HTTP_METHOD_GET "GET"

HTTP请求GET方法。

**起始版本：** 20

**系统能力：** SystemCapability.Communication.NetStack

NET_HTTPMETHOD_HEAD "HEAD"

HTTP请求HEAD方法。

**起始版本：** 20

**系统能力：** SystemCapability.Communication.NetStack

NET_HTTPMETHOD_OPTIONS "OPTIONS"

HTTP请求OPTIONS方法。

**起始版本：** 20

**系统能力：** SystemCapability.Communication.NetStack

NET_HTTPMETHOD_TRACE "TRACE"

HTTP请求TRACE方法。

**起始版本：** 20

**系统能力：** SystemCapability.Communication.NetStack

NET_HTTPMETHOD_DELETE "DELETE"

HTTP请求DELETE方法。

**起始版本：** 20

**系统能力：** SystemCapability.Communication.NetStack

NET_HTTP_METHOD_POST "POST"

HTTP请求POST方法。

**起始版本：** 20

**系统能力：** SystemCapability.Communication.NetStack

NET_HTTP_METHOD_PUT "PUT"

HTTP请求PUT方法。

**起始版本：** 20

**系统能力：** SystemCapability.Communication.NetStack

NET_HTTP_METHOD_PATCH "CONNECT"

HTTP请求CONNECT方法。

**起始版本：** 20

**系统能力：** SystemCapability.Communication.NetStack

#### 函数

名称typedef关键字描述[typedef void (*Http_ResponseCallback)(struct Http_Response *response, uint32_t errCode)](#ZH-CN_TOPIC_0000002497605460__http_responsecallback)Http_ResponseCallback接收到HTTP响应的回调函数。[typedef void (*Http_OnDataReceiveCallback)(const char *data, size_t length)](#ZH-CN_TOPIC_0000002497605460__http_ondatareceivecallback)Http_OnDataReceiveCallback接收到数据的回调。[typedef void (*Http_OnProgressCallback)(uint64_t totalSize, uint64_t transferredSize)](#ZH-CN_TOPIC_0000002497605460__http_onprogresscallback)Http_OnProgressCallback请求/响应数据传输过程中调用的回调函数。[typedef void (*Http_OnHeaderReceiveCallback)(Http_Headers *headers)](#ZH-CN_TOPIC_0000002497605460__http_onheaderreceivecallback)Http_OnHeaderReceiveCallback收到HTTP响应头的回调函数。[typedef void (*Http_OnVoidCallback)(void)](#ZH-CN_TOPIC_0000002497605460__http_onvoidcallback)Http_OnVoidCallback请求的DataEnd或Cancel事件回调的回调函数。

#### 枚举类型说明

#### Http_ErrCode

```ets
enum Http_ErrCode
```

**描述**

定义HTTP请求的错误码。

**起始版本：** 20

枚举项描述OH_HTTP_RESULT_OK = 0请求成功。OH_HTTP_PARAMETER_ERROR = 401参数错误。OH_HTTP_PERMISSION_DENIED = 201权限校验失败。OH_HTTP_NETSTACK_E_BASE = 2300000基础错误码偏移。OH_HTTP_UNSUPPORTED_PROTOCOL = (OH_HTTP_NETSTACK_E_BASE + 1)不支持的协议。OH_HTTP_INVALID_URL = (OH_HTTP_NETSTACK_E_BASE + 3)URL格式错误。OH_HTTP_RESOLVE_PROXY_FAILED = (OH_HTTP_NETSTACK_E_BASE + 5)代理服务器域名解析失败。OH_HTTP_RESOLVE_HOST_FAILED = (OH_HTTP_NETSTACK_E_BASE + 6)域名解析失败。OH_HTTP_CONNECT_SERVER_FAILED = (OH_HTTP_NETSTACK_E_BASE + 7)无法连接到服务器。OH_HTTP_INVALID_SERVER_RESPONSE = (OH_HTTP_NETSTACK_E_BASE + 8)服务器返回非法数据。OH_HTTP_ACCESS_REMOTE_DENIED = (OH_HTTP_NETSTACK_E_BASE + 9)拒绝访问远程资源。OH_HTTP_HTTP2_FRAMING_ERROR = (OH_HTTP_NETSTACK_E_BASE + 16)HTTP2框架层出现错误。OH_HTTP_TRANSFER_PARTIAL_FILE = (OH_HTTP_NETSTACK_E_BASE + 18)传输了部分文件。OH_HTTP_WRITE_DATA_FAILED = (OH_HTTP_NETSTACK_E_BASE + 23)无法将接收到的数据写入磁盘或应用程序。OH_HTTP_UPLOAD_FAILED = (OH_HTTP_NETSTACK_E_BASE + 25)上传失败。OH_HTTP_OPEN_LOCAL_DATA_FAILED = (OH_HTTP_NETSTACK_E_BASE + 26)无法打开或读取文件或应用程序中的本地数据。OH_HTTP_OUT_OF_MEMORY = (OH_HTTP_NETSTACK_E_BASE + 27)内存不足。OH_HTTP_OPERATION_TIMEOUT = (OH_HTTP_NETSTACK_E_BASE + 28)操作超时。OH_HTTP_TOO_MANY_REDIRECTIONS = (OH_HTTP_NETSTACK_E_BASE + 47)重定向次数已达到允许的最大值。OH_HTTP_SERVER_RETURNED_NOTHING = (OH_HTTP_NETSTACK_E_BASE + 52)服务器没有返回任何内容（没有标头或数据）。OH_HTTP_SEND_DATA_FAILED = (OH_HTTP_NETSTACK_E_BASE + 55)发送数据失败。OH_HTTP_RECEIVE_DATA_FAILED = (OH_HTTP_NETSTACK_E_BASE + 56)接收数据失败。OH_HTTP_SSL_CERTIFICATE_ERROR = (OH_HTTP_NETSTACK_E_BASE + 58)本地SSL证书错误。OH_HTTP_SSL_CIPHER_USED_ERROR = (OH_HTTP_NETSTACK_E_BASE + 59)指定的加密套件不可用。OH_HTTP_INVALID_SSL_PEER_CERT = (OH_HTTP_NETSTACK_E_BASE + 60)SSL对等证书或SSH远程密钥无效。OH_HTTP_INVALID_ENCODING_FORMAT = (OH_HTTP_NETSTACK_E_BASE + 61)HTTP编码格式无效。OH_HTTP_FILE_TOO_LARGE = (OH_HTTP_NETSTACK_E_BASE + 63)超出最大文件大小。OH_HTTP_REMOTE_DISK_FULL = (OH_HTTP_NETSTACK_E_BASE + 70)远端磁盘满。OH_HTTP_REMOTE_FILE_EXISTS = (OH_HTTP_NETSTACK_E_BASE + 73)远端文件已存在。OH_HTTP_SSL_CA_NOT_EXIST = (OH_HTTP_NETSTACK_E_BASE + 77)SSL CA证书不存在或无法访问。OH_HTTP_REMOTE_FILE_NOT_FOUND = (OH_HTTP_NETSTACK_E_BASE + 78)远端文件未找到。OH_HTTP_AUTHENTICATION_ERROR = (OH_HTTP_NETSTACK_E_BASE + 94)身份验证错误。OH_HTTP_ACCESS_DOMAIN_NOT_ALLOWED = (OH_HTTP_NETSTACK_E_BASE + 998)不允许访问该域。OH_HTTP_UNKNOWN_ERROR = (OH_HTTP_NETSTACK_E_BASE + 999)未知错误。

#### Http_ResponseCode

```ets
enum Http_ResponseCode
```

**描述**

定义HTTP响应码。

**起始版本：** 20

枚举项描述OH_HTTP_OK = 200请求成功。OH_HTTP_CREATED = 201成功请求并创建新资源。OH_HTTP_ACCEPTED = 202请求已被接受但尚未完全处理。OH_HTTP_NOT_AUTHORITATIVE = 203请求成功。但是有未授权信息。OH_HTTP_NO_CONTENT = 204服务器处理成功，但未返回内容。OH_HTTP_RESET = 205重置内容。OH_HTTP_PARTIAL = 206服务器成功处理了部分GET请求。OH_HTTP_MULT_CHOICE = 300多种选择。OH_HTTP_MOVED_PERM = 301请求的资源已永久移动到新的URI，返回信息将包含新的URI。浏览器将自动重定向到新的URI。OH_HTTP_MOVED_TEMP = 302临时重定向。OH_HTTP_SEE_OTHER = 303查看其他地址。请求的资源已移动到新的URL，客户端应使用GET方法访问该URL。OH_HTTP_NOT_MODIFIED = 304请求的资源没有修改。OH_HTTP_USE_PROXY = 305请求资源需要使用代理访问。OH_HTTP_BAD_REQUEST = 400服务器无法理解客户端请求的语法错误。OH_HTTP_UNAUTHORIZED = 401请求用户身份验证。OH_HTTP_PAYMENT_REQUIRED = 402保留以供将来使用。OH_HTTP_FORBIDDEN = 403服务器理解来自请求客户端的请求，但拒绝执行。OH_HTTP_NOT_FOUND = 404服务器无法根据客户端的请求找到资源。OH_HTTP_BAD_METHOD = 405客户端请求中的方法被禁止。OH_HTTP_NOT_ACCEPTABLE = 406服务器无法根据客户端请求的内容特征完成请求。OH_HTTP_PROXY_AUTH = 407请求验证代理人的身份。OH_HTTP_CLIENT_TIMEOUT = 408请求耗时太长，超时。OH_HTTP_CONFLICT = 409服务器在完成客户端的PUT请求时可能返回此代码，因为服务器在处理请求时发生冲突。OH_HTTP_GONE = 410客户端请求的资源不再存在。OH_HTTP_LENGTH_REQUIRED = 411服务器无法处理客户端发送的不带Content Length的请求信息。OH_HTTP_PRECON_FAILED = 412向客户端请求信息的前提条件不正确。OH_HTTP_ENTITY_TOO_LARGE = 413请求被拒绝，因为请求的实体太大，服务器无法处理。OH_HTTP_REQ_TOO_LONG = 414请求的URI超过了服务器能够解析的长度，服务器无法处理。OH_HTTP_UNSUPPORTED_TYPE = 415服务器无法处理请求的格式。OH_HTTP_RANGE_NOT_SATISFIABLE = 416请求的范围无法满足。OH_HTTP_INTERNAL_ERROR = 500内部服务器错误，无法完成请求。OH_HTTP_NOT_IMPLEMENTED = 501服务器不支持请求的功能，无法完成请求。OH_HTTP_BAD_GATEWAY = 502充当网关或代理的服务器从远程服务器收到无效请求。OH_HTTP_UNAVAILABLE = 503由于超载或系统维护，服务器暂时无法处理客户端请求。OH_HTTP_GATEWAY_TIMEOUT = 504作为网关的服务器没有及时从远程服务器获取请求。OH_HTTP_VERSION = 505服务器请求的HTTP协议版本。

#### Http_AddressFamilyType

```ets
enum Http_AddressFamilyType
```

**描述**

定义解析目标域名时限定的地址类型。

**起始版本：** 20

枚举项描述HTTP_ADDRESS_FAMILY_DEFAULT = 0默认值，系统将自行选择目标域名的IPv4地址或IPv6地址。HTTP_ADDRESS_FAMILY_ONLY_V4 = 1系统仅解析目标域名的IPv4地址，忽略IPv6地址。HTTP_ADDRESS_FAMILY_ONLY_V6 = 2系统仅解析目标域名的IPv6地址，忽略IPv4地址。

#### Http_HttpProtocol

```ets
enum Http_HttpProtocol
```

**描述**

HTTP协议版本号枚举定义。

**起始版本：** 20

枚举项描述OH_HTTP_NONE = 0跟随curl的协议版本选择。OH_HTTP1_1HTTP1.1版本。OH_HTTP2HTTP2版本。OH_HTTP3HTTP3版本。

#### Http_CertType

```ets
enum Http_CertType
```

**描述**

证书类型枚举。

**起始版本：** 20

枚举项描述OH_HTTP_PEM = 0PEM证书类型。OH_HTTP_DER = 1DER证书类型。OH_HTTP_P12 = 2P12证书类型。

#### Http_ProxyType

```ets
enum Http_ProxyType
```

**描述**

代理配置类型枚举定义。

**起始版本：** 20

枚举项描述HTTP_PROXY_NOT_USE不使用代理。HTTP_PROXY_SYSTEM使用系统代理。HTTP_PROXY_CUSTOM使用用户自定义代理。

#### 函数说明

#### Http_ResponseCallback()

```ets
typedef void (*Http_ResponseCallback)(struct Http_Response *response, uint32_t errCode)
```

**描述**

接收到HTTP响应的回调函数。

**起始版本：** 20

**参数：**

参数项描述[struct Http_Response](../../topics/networking/Http_Response.md) *responseHTTP响应结构体，指向Http_Response的指针，参考[Http_Response](../../topics/networking/Http_Response.md)。uint32_t errCode响应码。

#### Http_OnDataReceiveCallback()

```ets
typedef void (*Http_OnDataReceiveCallback)(const char *data, size_t length)
```

**描述**

接收到数据的回调。

**起始版本：** 20

**参数：**

参数项描述const char *data响应体。size_t length响应体的长度。

#### Http_OnProgressCallback()

```ets
typedef void (*Http_OnProgressCallback)(uint64_t totalSize, uint64_t transferredSize)
```

**描述**

请求/响应数据传输过程中调用的回调函数。

**起始版本：** 20

**参数：**

参数项描述uint64_t totalSize数据总大小。uint64_t transferredSize已传输的数据大小。

#### Http_OnHeaderReceiveCallback()

```ets
typedef void (*Http_OnHeaderReceiveCallback)(Http_Headers *headers)
```

**描述**

收到HTTP响应头的回调函数。

**起始版本：** 20

**参数：**

参数项描述[Http_Headers](../../topics/networking/Http_Headers.md) *headers接收到的请求头，指向Http_Headers的指针，参考[Http_Headers](../../topics/networking/Http_Headers.md)。

#### Http_OnVoidCallback()

```ets
typedef void (*Http_OnVoidCallback)(void)
```

**描述**

请求的DataEnd或Cancel事件回调的回调函数。

**起始版本：** 20