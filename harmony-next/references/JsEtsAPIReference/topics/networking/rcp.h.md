# rcp.h

**概述**

声明用于访问远程通信的API。提供基本的函数，结构体和const定义。

引用文件： <RemoteCommunicationKit/rcp.h>

库： librcp_c.so

系统能力： SystemCapability.Collaboration.RemoteCommunication

起始版本： 5.0.0(12)

相关模块： [RemoteCommunication](RemoteCommunication.md)

**汇总**

**结构体**

| 名称 | 描述 |
| --- | --- |
| struct Rcp_Buffer | 文本存储结构。 |
| struct Rcp_ContentOrPathOrCallback | Rcp_FormFieldFileValue中使用的简单表单数据字段值。 |
| struct Rcp_FormFieldFileValue | 表单字段文件值。 |
| struct Rcp_FormFieldValue | 简单表单数据字段值，参见Rcp_Form和Rcp_MultipartFormFieldValue。 |
| struct Rcp_MultipartFormFieldValue | 多部分表单域值，在Rcp_MultipartForm中使用。 |
| struct Rcp_RequestContent | 请求的内容。 |
| struct Rcp_HeaderValue | 请求或响应的标头映射的值类型。 |
| struct Rcp_HeaderEntry | 请求或响应的标头的所有键值对。 |
| struct Rcp_Credential | 凭据。某些服务器或代理服务器需要。 |
| struct Rcp_ServerAuthentication | 服务器身份验证。 |
| struct Rcp_Urls | url，用于确定主机是否正在使用代理。 |
| struct Rcp_Exclusions | 代理配置中用于过滤不使用代理的urls。 |
| struct Rcp_CertificateAuthority | 用于验证远程服务器标识的证书颁发机构（CA）。 |
| struct Rcp_ClientCertificate | 发送到远程服务器的客户端证书，远程服务器将使用它来验证客户端的标识。 |
| struct Rcp_SecurityConfiguration | 请求的安全配置。 |
| struct Rcp_WebProxy | 自定义代理配置。 |
| struct Rcp_IpAndPort | 该接口用在Rcp_DnsServers中，表示一个DNS服务器的地址和端口。 |
| struct Rcp_DnsServers | DNS服务器。Rcp_DnsConfiguration.dnsRules中的类型之一。 |
| struct Rcp_IpAddress | 指定静态DNS规则使用的IP地址组。用于Rcp_StaticDnsRuleItem。 |
| struct Rcp_StaticDnsRuleItem | 描述单个静态DNS规则。 |
| struct Rcp_StaticDnsRule | 静态DNS规则。 |
| struct Rcp_DnsRule | DNS规则配置。 |
| struct Rcp_OnDataReceiveCallback | 接收到数据时回调。Rcp_EventsHandler中的配置。 |
| struct Rcp_OnProgressCallback | 收发时回调配置，在Rcp_EventsHandler中配置。 |
| struct Rcp_OnHeaderReceiveCallback | Rcp_EventsHandler中配置的接收到的header的回调配置。 |
| struct Rcp_OnVoidCallback | 在Rcp_EventsHandler中配置的数据结束或已取消事件的回调配置。 |
| struct Rcp_EventsHandler | 监听不同HTTP事件的回调函数。 |
| struct Rcp_Timeout | 请求的超时配置 |
| struct Rcp_DnsOverHttps | HTTPS上的DNS配置如果设置，则首选由DOH dns服务器解析的地址。 |
| struct Rcp_TransferConfiguration | 传输配置。 |
| struct Rcp_InfoToCollect | 指定要收集的请求处理事件。可以通过响应对象检查收集的事件。 |
| struct Rcp_TracingConfiguration | 请求追踪配置。 |
| struct Rcp_ProxyConfiguration | 代理配置。 |
| struct Rcp_DnsConfiguration | DNS解析配置。 |
| struct Rcp_Configuration | 请求配置。 |
| struct Rcp_TransferRange | HTTP传输范围。该设置将转换为HTTP Range标头。具有范围标头的HTTP请求要求服务器仅发送回HTTP响应的一部分。 |
| struct Rcp_Request | 网络请求。 |
| struct Rcp_RequestCookieEntry | 描述请求的所有Cookie键值对。 |
| struct Rcp_DebugInfo | 描述存储在Rcp_Response中的调试信息的结构。 |
| struct Rcp_CookieAttributeEntry | 响应Cookie属性条目。 |
| struct Rcp_ResponseCookies | 响应Cookie。 |
| struct Rcp_TimeInfo | 响应计时信息。 |
| struct Rcp_ResponseCallbackObject | 响应回调结构体。 |
| struct Rcp_Response | 网络请求的响应。 |
| struct Rcp_Interceptor | 异步拦截器。 |
| struct Rcp_SyncInterceptor | 同步拦截器 |
| struct Rcp_InterceptorArray | 异步拦截器数组。 |
| struct Rcp_SyncInterceptorArray | 同步拦截器数组。 |
| struct Rcp_SessionListener | 关闭或取消会话事件的回调函数。 |
| struct Rcp_ConnectionConfiguration | 连接配置。 |
| struct Rcp_SessionConfiguration | 会话配置。 |
| struct Rcp_OnBinaryReceiveCallback | 接收到响应数据时的回调。支持二进制数据的接收。使用HMS_Rcp_SetRequestOnBinaryDataRecvCallback给请求设置。 |
| struct Rcp_OnStatusCodeReceiveCallback | 接收到响应状态码时的回调。使用HMS_Rcp_SetRequestOnStatusCodeReceiveCallback给请求设置。 |

**宏定义**

| 名称 | 描述 |
| --- | --- |
| RCP_MAX_REQUEST_ID_LEN 32 | 请求ID的最大长度。 |
| RCP_MAX_CONTENT_TYPE_LEN 64 | 内容类型最大长度。 |
| RCP_MAX_FILENAME_LEN 128 | 文件名最大长度。 |
| RCP_MAX_PATH_LEN 128 | 路径的最大长度。 |
| RCP_METHOD_GET "GET" | HTTP get方法。 |
| RCP_METHOD_HEAD "HEAD" | HTTP head方法。 |
| RCP_METHOD_OPTIONS "OPTIONS" | HTTP options方法。 |
| RCP_METHOD_TRACE "TRACE" | HTTP trace方法。 |
| RCP_METHOD_DELETE "DELETE" | HTTP delete方法。 |
| RCP_METHOD_POST "POST" | HTTP post方法。 |
| RCP_METHOD_PUT "PUT" | HTTP put方法。 |
| RCP_METHOD_PATCH "PATCH" | HTTP patch方法。 |
| RCP_IP_MAX_LEN 40 | IP地址的最大长度。 |
| RCP_HOST_MAX_LEN 256 | 主机名的最大长度。 |

**类型定义**

| 名称 | 描述 |
| --- | --- |
| typedef enum Rcp_FormValueTypeRcp_FormValueType | 表单值类型。 |
| typedef int(* Rcp_GetDataCallback) (char *out, uint32_t size) | 通过回调函数获取数据。当API需要将数据的下一部分发送到服务器时，将调用此回调。 |
| typedef enum Rcp_ContentOrPathOrCallbackTypeRcp_ContentOrPathOrCallbackType | 回调的内容、路径或类型。用于区分Rcp_ContentOrPathOrCallback中使用的数据。 |
| typedef struct Rcp_BufferRcp_Buffer | 文本存储结构。 |
| typedef struct Rcp_ContentOrPathOrCallbackRcp_ContentOrPathOrCallback | Rcp_FormFieldFileValue中使用的简单表单数据字段值。 |
| typedef enum Rcp_MultipartValueTypeRcp_MultipartValueType | 多部分值类型。用于区分Rcp_MultipartFormFieldValue中使用的数据。 |
| typedef struct Rcp_FormFieldFileValueRcp_FormFieldFileValue | 表单字段文件值。 |
| typedef struct Rcp_FormFieldValueRcp_FormFieldValue | 简单表单数据字段值，参见Rcp_Form和Rcp_MultipartFormFieldValue。 |
| typedef struct Rcp_MultipartFormFieldValueRcp_MultipartFormFieldValue | 多部分表单域值，在Rcp_MultipartForm中使用。 |
| typedef enum Rcp_ContentTypeRcp_ContentType | 内容类型。用于区分Rcp_RequestContent中使用的数据。 |
| typedef struct Rcp_FormRcp_Form | 简单表单。 |
| typedef struct Rcp_MultipartFormRcp_MultipartForm | 多部分表单。 |
| typedef struct Rcp_RequestContentRcp_RequestContent | 请求的内容。 |
| typedef struct Rcp_HeadersRcp_Headers | 请求或响应的标头。 |
| typedef struct Rcp_HeaderValueRcp_HeaderValue | 请求或响应的标头映射的值类型。 |
| typedef struct Rcp_HeaderEntryRcp_HeaderEntry | 请求或响应的标头的所有键值对。 |
| typedef enum Rcp_AuthenticationTypeRcp_AuthenticationType | 枚举类型。服务器的身份验证类型。如果未设置，请与服务器协商。 |
| typedef struct Rcp_CredentialRcp_Credential | 凭据。某些服务器或代理服务器需要。 |
| typedef struct Rcp_ServerAuthenticationRcp_ServerAuthentication | 服务器身份验证。 |
| typedef bool(* Rcp_ExclusionFunction) (const char *url) | 判断host是否使用代理的函数指针。 |
| typedef struct Rcp_UrlsRcp_Urls | url，用于确定主机是否正在使用代理。 |
| typedef enum Rcp_ExclusionsValueTypeRcp_ExclusionsValueType | 代理排除中使用的数据类型. 用于区分Rcp_Exclusions中使用的数据。 |
| typedef struct Rcp_ExclusionsRcp_Exclusions | 代理配置中用于过滤不使用代理的URLs。 |
| typedef enum Rcp_CertTypeRcp_CertType | 客户端证书类型。 |
| typedef struct Rcp_CertificateAuthorityRcp_CertificateAuthority | 用于验证远程服务器标识的证书颁发机构（CA）。 |
| typedef struct Rcp_ClientCertificateRcp_ClientCertificate | 发送到远程服务器的客户端证书，远程服务器将使用它来验证客户端的标识。 |
| typedef enum Rcp_RemoteValidationTypeRcp_RemoteValidationType | 远程验证类型。 |
| typedef struct Rcp_SecurityConfigurationRcp_SecurityConfiguration | 请求的安全配置。 |
| typedef enum Rcp_ProxyTunnelModeRcp_ProxyTunnelMode | 用于控制何时创建代理隧道。 隧道或隧道传输意味着向代理发送HTTP CONNECT请求，要求它连接到特定端口号上的远程主机，然后流量只是通过代理。“auto”表示为HTTPS创建隧道。“always”表示始终创建隧道。 |
| typedef struct Rcp_WebProxyRcp_WebProxy | 自定义代理配置。 |
| typedef struct Rcp_IpAndPortRcp_IpAndPort | 该接口用在Rcp_DnsServers中，表示一个DNS服务器的地址和端口。 |
| typedef struct Rcp_DnsServersRcp_DnsServers | DNS服务器。Rcp_DnsConfiguration.dnsRules中的类型之一。 |
| typedef struct Rcp_IpAddressRcp_IpAddress | 指定静态DNS规则使用的IP地址组。用于Rcp_StaticDnsRuleItem。 |
| typedef struct Rcp_StaticDnsRuleItemRcp_StaticDnsRuleItem | 描述单个静态DNS规则。 |
| typedef struct Rcp_StaticDnsRuleRcp_StaticDnsRule | 静态DNS规则。 |
| typedef Rcp_IpAddress *(* Rcp_DynamicDnsRuleFunction) (const char *host, uint16_t port) | 一个可以根据主机名和端口直接返回IP地址的函数。用于动态DNS解析。 |
| typedef enum Rcp_DnsRuleTypeRcp_DnsRuleType | DNS规则类型。用于区分Rcp_DnsRule中使用的dns规则类型。 |
| typedef struct Rcp_DnsRuleRcp_DnsRule | DNS规则配置。 |
| typedef size_t(* Rcp_OnDataReceiveCallbackFunc) (void *usrObject, const char *data) | 接收到响应正文时调用的回调函数。 |
| typedef size_t(* Rcp_OnBinaryReceiveCallbackFunc) (void *usrObject, Rcp_Buffer *buffer) | 接收到响应正文时调用的回调函数（二进制数据）。 |
| typedef void (* Rcp_OnStatusCodeReceiveCallbackFunc)(void *usrObject, uint32_t statusCode) | 接收到响应状态码时调用的回调函数。 |
| typedef void(* Rcp_OnProgressCallbackFunc) (void *usrObject, uint64_t totalSize, uint64_t transferredSize) | 请求/响应数据传输过程中调用的回调函数。 |
| typedef void(* Rcp_OnHeaderReceiveCallbackFunc) (void *usrObject, Rcp_Headers *headers) | 收到所有请求时调用的回调。 |
| typedef void(* Rcp_OnVoidCallbackFunc) (void *usrObject) | 请求的DataEnd或Canceled事件回调的回调函数。 |
| typedef struct Rcp_OnDataReceiveCallbackRcp_OnDataReceiveCallback | 接收到数据时回调。Rcp_EventsHandler中的配置。 |
| typedef struct Rcp_OnProgressCallbackRcp_OnProgressCallback | 收发时回调配置，在Rcp_EventsHandler中配置。 |
| typedef struct Rcp_OnHeaderReceiveCallbackRcp_OnHeaderReceiveCallback | Rcp_EventsHandler中配置的接收到的header的回调配置。 |
| typedef struct Rcp_OnVoidCallbackRcp_OnVoidCallback | 在Rcp_EventsHandler中配置的数据结束或已取消事件的回调配置。 |
| typedef struct Rcp_EventsHandlerRcp_EventsHandler | 监听不同HTTP事件的回调函数。 |
| typedef struct Rcp_TimeoutRcp_Timeout | 请求的超时配置。 |
| typedef struct Rcp_DnsOverHttpsRcp_DnsOverHttps | HTTPS上的DNS配置如果设置，则首选由DOH dns服务器解析的地址。 |
| typedef enum Rcp_PathPreferenceRcp_PathPreference | 请求路径首选项。 |
| typedef struct Rcp_TransferConfigurationRcp_TransferConfiguration | 传输配置。 |
| typedef struct Rcp_InfoToCollectRcp_InfoToCollect | 指定要收集的请求处理事件。可以通过响应对象检查收集的事件。 |
| typedef struct Rcp_TracingConfigurationRcp_TracingConfiguration | 请求追踪配置。 |
| typedef enum Rcp_ProxyTypeRcp_ProxyType | 代理类型。用于区分不同的代理配置。 |
| typedef struct Rcp_ProxyConfigurationRcp_ProxyConfiguration | 代理配置。 |
| typedef struct Rcp_DnsConfigurationRcp_DnsConfiguration | DNS解析配置。 |
| typedef struct Rcp_ConfigurationRcp_Configuration | 请求配置。 |
| typedef struct Rcp_TransferRangeRcp_TransferRange | HTTP传输范围。该设置将转换为HTTP Range标头。具有范围标头的HTTP请求要求服务器仅发送回HTTP响应的一部分。 |
| typedef struct Rcp_RequestCookiesRcp_RequestCookies | 请求Cookie。 |
| typedef struct Rcp_RequestRcp_Request | 网络请求。 |
| typedef struct Rcp_RequestCookieEntryRcp_RequestCookieEntry | 描述请求的所有Cookie键值对。 |
| typedef enum Rcp_StatusCodeRcp_StatusCode | 请求响应的状态码。 |
| typedef enum Rcp_DebugEventRcp_DebugEvent | 描述调试信息的事件类型。 |
| typedef struct Rcp_DebugInfoRcp_DebugInfo | 描述存储在Rcp_Response中的调试信息的结构。 |
| typedef struct Rcp_CookieAttributesRcp_CookieAttributes | 描述Rcp_Response中Cookie属性的类型。 |
| typedef struct Rcp_CookieAttributeEntryRcp_CookieAttributeEntry | 响应Cookie属性条目。 |
| typedef struct Rcp_ResponseCookiesRcp_ResponseCookies | 响应Cookie。 |
| typedef struct Rcp_TimeInfoRcp_TimeInfo | 响应计时信息。 |
| typedef struct Rcp_ResponseRcp_Response | 网络请求的响应。 |
| typedef void(* Rcp_ResponseCallback) (void *usrCtx, Rcp_Response *response, uint32_t errCode) | 响应回调函数指针。 |
| typedef struct Rcp_ResponseCallbackObjectRcp_ResponseCallbackObject | 响应回调结构体。 |
| typedef struct Rcp_RequestHandlerRcp_RequestHandler | 与Rcp_Interceptor关联的异步处理器。 |
| typedef struct Rcp_SyncRequestHandlerRcp_SyncRequestHandler | 与Rcp_SyncInterceptor关联的同步处理器。 |
| typedef struct Rcp_InterceptorRcp_Interceptor | 异步拦截器。 |
| typedef struct Rcp_SyncInterceptorRcp_SyncInterceptor | 同步拦截器。 |
| typedef struct Rcp_InterceptorArrayRcp_InterceptorArray | 异步拦截器数组。 |
| typedef struct Rcp_SyncInterceptorArrayRcp_SyncInterceptorArray | 同步拦截器数组。 |
| typedef enum Rcp_SessionTypeRcp_SessionType | 会话类型。 |
| typedef struct Rcp_SessionRcp_Session | 会话。 |
| typedef struct Rcp_SessionListenerRcp_SessionListener | 关闭或取消会话事件的回调函数。 |
| typedef struct Rcp_ConnectionConfigurationRcp_ConnectionConfiguration | 连接配置。 |
| typedef struct Rcp_SessionConfigurationRcp_SessionConfiguration | 会话配置。 |
| typedef struct Rcp_OnBinaryReceiveCallbackRcp_OnBinaryReceiveCallback | 响应的二进制数据接收回调函数。 |
| typedef size_t(* Rcp_OnBinaryReceiveCallbackFunc) (void *usrObject, Rcp_Buffer *buffer) | 二进制数据接收回调函数指针。 |

**枚举**

| 名称 | 描述 |
| --- | --- |
| Rcp_FormValueType { RCP_FORM_VALUE_TYPE_INT32, RCP_FORM_VALUE_TYPE_INT64, RCP_FORM_VALUE_TYPE_BOOL, RCP_FORM_VALUE_TYPE_STRING, RCP_FORM_VALUE_TYPE_DOUBLE } | 表单值类型。 |
| Rcp_ContentOrPathOrCallbackType { RCP_FILE_VALUE_TYPE_CONTENT, RCP_FILE_VALUE_TYPE_PATH, RCP_FILE_VALUE_TYPE_CALLBACK} | 回调的内容、路径或类型。用于区分Rcp_ContentOrPathOrCallback中使用的数据。 |
| Rcp_MultipartValueType { RCP_TYPE_FORM_FIELD_VALUE, RCP_TYPE_FORM_FIELD_FILE_VALUE } | 多部分值类型。用于区分Rcp_MultipartFormFieldValue中使用的数据。 |
| Rcp_ContentType { RCP_CONTENT_TYPE_STRING, RCP_CONTENT_TYPE_FORM, RCP_CONTENT_TYPE_MULTIPARTFORM, RCP_CONTENT_TYPE_GETCALLBACK } | 内容类型。用于区分Rcp_RequestContent中使用的数据。 |
| Rcp_AuthenticationType { RCP_AUTHENTICATION_AUTO, RCP_AUTHENTICATION_BASIC, RCP_AUTHENTICATION_NTLM, RCP_AUTHENTICATION_DIGEST } | 枚举类型。服务器的身份验证类型。如果未设置，请与服务器协商。 |
| Rcp_ExclusionsValueType { RCP_EXCLUSION_USE_URL_ARRAY, RCP_EXCLUSION_USE_CALLBACK } | 代理排除中使用的数据类型. 用于区分Rcp_Exclusions中使用的数据。 |
| Rcp_CertType { RCP_CERT_PEM, RCP_CERT_DER, RCP_CERT_P12 } | 客户端证书类型。 |
| Rcp_RemoteValidationType { RCP_REMOTE_VALIDATION_SYSTEM, RCP_REMOTE_VALIDATION_SKIP, RCP_REMOTE_VALIDATION_CERTIFICATE_AUTHORITY } | 远程验证类型。 |
| Rcp_ProxyTunnelMode { RCP_PROXY_TUNNEL_AUTO, RCP_PROXY_TUNNEL_ALWAYS } | 用于控制何时创建代理隧道。 隧道或隧道传输意味着向代理发送HTTP CONNECT请求，要求它连接到特定端口号上的远程主机，然后流量只是通过代理。“auto”表示为HTTPS创建隧道。“always”表示始终创建隧道。 |
| Rcp_DnsRuleType { RCP_DNS_RULE_DNS_SERVERS, RCP_DNS_RULE_STATIC, RCP_DNS_RULE_DYNAMIC } | DNS规则类型。用于区分Rcp_DnsRule中使用的dns规则类型。 |
| Rcp_PathPreference { RCP_PATH_PREFERENCE_AUTO, RCP_PATH_PREFERENCE_WIFI, RCP_PATH_PREFERENCE_CELLULAR } | 请求路径首选项。 |
| Rcp_ProxyType { RCP_PROXY_SYSTEM, RCP_PROXY_CUSTOM, RCP_PROXY_NO_PROXY } | 代理类型。用于区分不同的代理配置。 |
| Rcp_StatusCode { RCP_NONE = 0, RCP_OK = 200, RCP_CREATED, RCP_ACCEPTED, RCP_NOT_AUTHORITATIVE, RCP_NO_CONTENT, RCP_RESET, RCP_PARTIAL, RCP_MULTI_CHOICE = 300, RCP_MOVED_PERMANENTLY, RCP_MOVED_TEMPORARILY, RCP_SEE_OTHER, RCP_NOT_MODIFIED, RCP_USE_PROXY, RCP_BAD_REQUEST = 400, RCP_UNAUTHORIZED, RCP_PAYMENT_REQUIRED, RCP_FORBIDDEN, RCP_NOT_FOUND, RCP_BAD_METHOD, RCP_NOT_ACCEPTABLE, RCP_PROXY_AUTH, RCP_CLIENT_TIMEOUT, RCP_CONFLICT, RCP_GONE, RCP_LENGTH_REQUIRED, RCP_PRECON_FAILED, RCP_ENTITY_TOO_LARGE, RCP_REQ_TOO_LONG, RCP_UNSUPPORTED_TYPE, RCP_INTERNAL_ERROR = 500, RCP_NOT_IMPLEMENTED, RCP_BAD_GATEWAY, RCP_UNAVAILABLE, RCP_GATEWAY_TIMEOUT, RCP_VERSION } | 请求响应的状态码。 |
| Rcp_DebugEvent { RCP_DEBUG_EVENT_TEXT, RCP_DEBUG_EVENT_HEADER_IN, RCP_DEBUG_EVENT_HEADER_OUT, RCP_DEBUG_EVENT_DATA_IN, RCP_DEBUG_EVENT_DATA_OUT, RCP_DEBUG_EVENT_SSL_DATA_IN, RCP_DEBUG_EVENT_SSL_DATA_OUT } | 描述调试信息的事件类型。 |
| Rcp_SessionType { RCP_SESSION_TYPE_HTTP = 0, RCP_SESSION_TYPE_MAX = 100} | 会话类型。 |

**函数**

| 名称 | 描述 |
| --- | --- |
| Rcp_Form * HMS_Rcp_CreateForm (void) | 创建一个简单表单。 |
| void HMS_Rcp_DestroyForm (Rcp_Form *form) | 销毁一个简单表单。 |
| uint32_t HMS_Rcp_SetFormValue (Rcp_Form *form, const char *key, const Rcp_FormFieldValue *value) | 设置简单表单的键值对。 |
| Rcp_FormFieldValue * HMS_Rcp_GetFormValue (Rcp_Form *form, const char *key) | 通过键获取一个简单表单的对应值。 |
| Rcp_MultipartForm * HMS_Rcp_CreateMultipartForm (void) | 创建一个多部分表单。 |
| void HMS_Rcp_DestroyMultipartForm (Rcp_MultipartForm *multipartForm) | 销毁一个多部分表单。 |
| uint32_t HMS_Rcp_SetMultipartFormValue (Rcp_MultipartForm *multipartForm, const char *key, const Rcp_MultipartFormFieldValue *value) | 设置多部分表单的键值对。 |
| Rcp_MultipartFormFieldValue * HMS_Rcp_GetMultipartFormValue (Rcp_MultipartForm *multipartForm, const char *key) | 通过键获取多部分表单的值。 |
| Rcp_Headers * HMS_Rcp_CreateHeaders (void) | 为请求或响应创建标头。 |
| void HMS_Rcp_DestroyHeaders (Rcp_Headers *headers) | 销毁请求或响应的标头。 |
| uint32_t HMS_Rcp_SetHeaderValue (Rcp_Headers *headers, const char *name, const char *value) | 设置请求或响应头的键值对。 |
| Rcp_HeaderValue * HMS_Rcp_GetHeaderValue (Rcp_Headers *headers, const char *name) | 通过键获取请求或响应头的值。 |
| Rcp_HeaderEntry * HMS_Rcp_GetHeaderEntries (Rcp_Headers *headers) | 获取请求或响应头的所有键值对。 |
| void HMS_Rcp_DestroyHeaderEntries (Rcp_HeaderEntry *headerEntry) | 销毁HMS_Rcp_GetHeaderEntries中获取的所有键值对。 |
| Rcp_Request * HMS_Rcp_CreateRequest (const char *url) | 创建请求。 |
| void HMS_Rcp_DestroyRequest (Rcp_Request *request) | 销毁请求。 |
| Rcp_RequestCookies * HMS_Rcp_CreateRequestCookies (void) | 创建空的请求Cookie。 |
| void HMS_Rcp_DestroyRequestCookies (Rcp_RequestCookies *cookies) | 销毁请求Cookie。 |
| uint32_t HMS_Rcp_SetRequestCookieValue (Rcp_RequestCookies *cookies, const char *name, const char *value) | 设置请求Cookie。 |
| char * HMS_Rcp_GetRequestCookieValue (Rcp_RequestCookies *cookies, const char *name) | 通过名称获取请求Cookie的值。 |
| Rcp_RequestCookieEntry * HMS_Rcp_GetRequestCookieEntries (Rcp_RequestCookies *cookies) | 获取请求Cookie中的所有键值对。 |
| void HMS_Rcp_DestroyRequestCookieEntries (Rcp_RequestCookieEntry *cookieEntry) | 销毁从HMS_Rcp_GetRequestCookieValue获取的所有与请求Cookie相关的键值对。 |
| const char * HMS_Rcp_GetResponseCookieAttrValue (Rcp_CookieAttributes *cookieAttributes, const char *name) | 通过名称获取Cookie属性的值。 |
| Rcp_CookieAttributeEntry * HMS_Rcp_GetResponseCookieAttrEntries (Rcp_CookieAttributes *cookieAttributes) | 在Rcp_CookieAttributes中获取所有响应Cookie属性。 |
| void HMS_Rcp_DestroyResponseCookieAttrEntries (Rcp_CookieAttributeEntry *entries) | 销毁响应Cookie属性。 |
| uint32_t HMS_Rcp_CallNextRequestHandler (Rcp_Request *request, const Rcp_RequestHandler *next, const Rcp_ResponseCallbackObject *responseCallback) | 在拦截器Rcp_Interceptor的函数中可以调用下一个拦截器或defaultHandler。 |
| Rcp_Response * HMS_Rcp_CallNextSyncRequestHandler (Rcp_Request *request, const Rcp_SyncRequestHandler *next, uint32_t *errCode) | 在拦截器Rcp_SyncInterceptor的函数中可以调用下一个拦截器或默认处理器。 |
| Rcp_Session * HMS_Rcp_CreateSession (const Rcp_SessionConfiguration *configuration, uint32_t *errCode) | 创建会话。 |
| const char * HMS_Rcp_GetSessionId (Rcp_Session *session) | 获取会话ID。 |
| const Rcp_SessionConfiguration * HMS_Rcp_GetSessionConfiguration (Rcp_Session *session) | 获取会话配置。 |
| Rcp_Response * HMS_Rcp_FetchSync (Rcp_Session *session, Rcp_Request *request, uint32_t *errCode) | 发送同步请求并获取响应。 |
| uint32_t HMS_Rcp_Fetch (Rcp_Session *session, Rcp_Request *request, const Rcp_ResponseCallbackObject *responseCallback) | 发送异步请求并获取响应。 |
| uint32_t HMS_Rcp_CancelRequest (Rcp_Session *session, const Rcp_Request *request) | 取消一个请求。 |
| uint32_t HMS_Rcp_CancelSession (Rcp_Session *session) | 取消会话。 |
| uint32_t HMS_Rcp_CloseSession (Rcp_Session **session) | 关闭会话。 |
| uint32_t HMS_Rcp_SetRequestOnBinaryDataRecvCallback (Rcp_Request *request, Rcp_OnBinaryReceiveCallback onBinaryReceiveCallback) | 为请求设置流式接收二进制数据的回调函数。该回调函数与Rcp_OnDataReceiveCallback功能一致，功能上可以包含字符数据和二进制数据。 |