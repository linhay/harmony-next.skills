# rcp.h

#### 概述

声明用于访问远程通信的API。提供基本的函数，结构体和const定义。

**库：** librcp_c.so

**系统能力：** SystemCapability.Collaboration.RemoteCommunication

**起始版本：** 5.0.0(12)

**相关模块：**[RemoteCommunication](RemoteCommunication.md)

#### 汇总

#### 结构体

名称

描述

struct [Rcp_Buffer](Rcp_Buffer.md)

文本存储结构。

struct [Rcp_ContentOrPathOrCallback](Rcp_ContentOrPathOrCallback.md)

[Rcp_FormFieldFileValue](Rcp_FormFieldFileValue.md)中使用的简单表单数据字段值。

struct [Rcp_FormFieldFileValue](Rcp_FormFieldFileValue.md)

表单字段文件值。

struct [Rcp_FormFieldValue](Rcp_FormFieldValue.md)

简单表单数据字段值，参见[Rcp_Form](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga40787f67faf4ea7111e4cda03f3f16be)和[Rcp_MultipartFormFieldValue](Rcp_MultipartFormFieldValue.md)。

struct [Rcp_MultipartFormFieldValue](Rcp_MultipartFormFieldValue.md)

多部分表单域值，在[Rcp_MultipartForm](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga9f974771548d3ed2054aba0e7506fef9)中使用。

struct [Rcp_RequestContent](Rcp_RequestContent.md)

请求的内容。

struct [Rcp_HeaderValue](Rcp_HeaderValue.md)

请求或响应的标头映射的值类型。

struct [Rcp_HeaderEntry](Rcp_HeaderEntry.md)

请求或响应的标头的所有键值对。

struct [Rcp_Credential](Rcp_Credential.md)

凭据。某些服务器或代理服务器需要。

struct [Rcp_ServerAuthentication](Rcp_ServerAuthentication.md)

服务器身份验证。

struct [Rcp_Urls](Rcp_Urls.md)

url，用于确定主机是否正在使用代理。

struct [Rcp_Exclusions](Rcp_Exclusions.md)

代理配置中用于过滤不使用代理的urls。

struct [Rcp_CertificateAuthority](Rcp_CertificateAuthority.md)

用于验证远程服务器标识的证书颁发机构（CA）。

struct [Rcp_ClientCertificate](Rcp_ClientCertificate.md)

发送到远程服务器的客户端证书，远程服务器将使用它来验证客户端的标识。

struct [Rcp_SecurityConfiguration](Rcp_SecurityConfiguration.md)

请求的安全配置。

struct [Rcp_WebProxy](Rcp_WebProxy.md)

自定义代理配置。

struct [Rcp_IpAndPort](Rcp_IpAndPort.md)

该接口用在[Rcp_DnsServers](Rcp_DnsServers.md)中，表示一个DNS服务器的地址和端口。

struct [Rcp_DnsServers](Rcp_DnsServers.md)

DNS服务器。[Rcp_DnsConfiguration.dnsRules](Rcp_DnsConfiguration.md#ZH-CN_TOPIC_0000002317126061__ab09aacb68c682d9beea100cae481eaa4)中的类型之一。

struct [Rcp_IpAddress](Rcp_IpAddress.md)

指定静态DNS规则使用的IP地址组。用于[Rcp_StaticDnsRuleItem](Rcp_StaticDnsRuleItem.md)。

struct [Rcp_StaticDnsRuleItem](Rcp_StaticDnsRuleItem.md)

描述单个静态DNS规则。

struct [Rcp_StaticDnsRule](Rcp_StaticDnsRule.md)

静态DNS规则。

struct [Rcp_DnsRule](Rcp_DnsRule.md)

DNS规则配置。

struct [Rcp_OnDataReceiveCallback](Rcp_OnDataReceiveCallback.md)

接收到数据时回调。[Rcp_EventsHandler](Rcp_EventsHandler.md)中的配置。

struct [Rcp_OnProgressCallback](Rcp_OnProgressCallback.md)

收发时回调配置，在[Rcp_EventsHandler](Rcp_EventsHandler.md)中配置。

struct [Rcp_OnHeaderReceiveCallback](Rcp_OnHeaderReceiveCallback.md)

[Rcp_EventsHandler](Rcp_EventsHandler.md)中配置的接收到的header的回调配置。

struct [Rcp_OnVoidCallback](Rcp_OnVoidCallback.md)

在[Rcp_EventsHandler](Rcp_EventsHandler.md)中配置的数据结束或已取消事件的回调配置。

struct [Rcp_EventsHandler](Rcp_EventsHandler.md)

监听不同HTTP事件的回调函数。

struct [Rcp_Timeout](Rcp_Timeout.md)

请求的超时配置

struct [Rcp_DnsOverHttps](Rcp_DnsOverHttps.md)

HTTPS上的DNS配置如果设置，则首选由DOH dns服务器解析的地址。

struct [Rcp_TransferConfiguration](Rcp_TransferConfiguration.md)

传输配置。

struct [Rcp_InfoToCollect](Rcp_InfoToCollect.md)

指定要收集的请求处理事件。可以通过响应对象检查收集的事件。

struct [Rcp_TracingConfiguration](Rcp_TracingConfiguration.md)

请求追踪配置。

struct [Rcp_ProxyConfiguration](Rcp_ProxyConfiguration.md)

代理配置。

struct [Rcp_DnsConfiguration](Rcp_DnsConfiguration.md)

DNS解析配置。

struct [Rcp_Configuration](Rcp_Configuration.md)

请求配置。

struct [Rcp_TransferRange](Rcp_TransferRange.md)

HTTP传输范围。该设置将转换为HTTP Range标头。具有范围标头的HTTP请求要求服务器仅发送回HTTP响应的一部分。

struct [Rcp_Request](Rcp_Request.md)

网络请求。

struct [Rcp_RequestCookieEntry](Rcp_RequestCookieEntry.md)

描述请求的所有Cookie键值对。

struct [Rcp_DebugInfo](Rcp_DebugInfo.md)

描述存储在[Rcp_Response](Rcp_Response.md)中的调试信息的结构。

struct [Rcp_CookieAttributeEntry](Rcp_CookieAttributeEntry.md)

响应Cookie属性条目。

struct [Rcp_ResponseCookies](Rcp_ResponseCookies.md)

响应Cookie。

struct [Rcp_TimeInfo](Rcp_TimeInfo.md)

响应计时信息。

struct [Rcp_ResponseCallbackObject](Rcp_ResponseCallbackObject.md)

响应回调结构体。

struct [Rcp_Response](Rcp_Response.md)

网络请求的响应。

struct [Rcp_Interceptor](Rcp_Interceptor.md)

异步拦截器。

struct [Rcp_SyncInterceptor](Rcp_SyncInterceptor.md)

同步拦截器

struct [Rcp_InterceptorArray](Rcp_InterceptorArray.md)

异步拦截器数组。

struct [Rcp_SyncInterceptorArray](Rcp_SyncInterceptorArray.md)

同步拦截器数组。

struct [Rcp_SessionListener](Rcp_SessionListener.md)

关闭或取消会话事件的回调函数。

struct [Rcp_ConnectionConfiguration](Rcp_ConnectionConfiguration.md)

连接配置。

struct [Rcp_SessionConfiguration](Rcp_SessionConfiguration.md)

会话配置。

struct [Rcp_OnBinaryReceiveCallback](Rcp_OnBinaryReceiveCallback.md)

接收到响应数据时的回调。支持二进制数据的接收。使用[HMS_Rcp_SetRequestOnBinaryDataRecvCallback](RemoteCommunication.md#section207321113884)给请求设置。

struct [Rcp_OnStatusCodeReceiveCallback](Rcp_OnStatusCodeReceiveCallback.md)

接收到响应状态码时的回调。使用[HMS_Rcp_SetRequestOnStatusCodeReceiveCallback](RemoteCommunication.md#section10194153116201)给请求设置。

#### 宏定义

名称

描述

[RCP_MAX_REQUEST_ID_LEN](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga34b7468983f894581c9e908295c6d92e) 32

请求ID的最大长度。

[RCP_MAX_CONTENT_TYPE_LEN](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga994193494eac9591a85c49f1e3200930) 64

内容类型最大长度。

[RCP_MAX_FILENAME_LEN](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__gaef0f15d9c2cacf9df70ba148cfff171b) 128

文件名最大长度。

[RCP_MAX_PATH_LEN](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga3dac667ae8b6fa64f2fede1e77804e12) 128

路径的最大长度。

[RCP_METHOD_GET](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga2f2cc4bec6023047b63a1b3aaca7e8ff) "GET"

HTTP get方法。

[RCP_METHOD_HEAD](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga01f80464137185de1b1c9d4a84a20328) "HEAD"

HTTP head方法。

[RCP_METHOD_OPTIONS](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__gac3a9a3250402418f4a59875e5e98cfc7) "OPTIONS"

HTTP options方法。

[RCP_METHOD_TRACE](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga3676dd73393ff05d3c487140ac5c3a88) "TRACE"

HTTP trace方法。

[RCP_METHOD_DELETE](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga865bfb4de54f47a05b3adc17eccfccf7) "DELETE"

HTTP delete方法。

[RCP_METHOD_POST](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga5c3de5092bf8c0b6556ccdf35b433b85) "POST"

HTTP post方法。

[RCP_METHOD_PUT](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__gada60d0d101fce537636d5d38ebdcd5b1) "PUT"

HTTP put方法。

[RCP_METHOD_PATCH](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga34617da18b0341c7111d0853834a12a1) "PATCH"

HTTP patch方法。

[RCP_IP_MAX_LEN](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__gaedd78171e1671e9ec89b59ecf6e96730) 40

IP地址的最大长度。

[RCP_HOST_MAX_LEN](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__gaf8dd4d8c5c99712c29f29211ad2a76ae) 256

主机名的最大长度。

#### 类型定义

名称

描述

typedef enum [Rcp_FormValueType](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga9d851389347a39bd4bb849ac31cfa478)[Rcp_FormValueType](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__gaa1493419cc430c47cef7ec7ddfb74220)

表单值类型。

typedef int(* [Rcp_GetDataCallback](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__gac0ac73f33252239ff47a648fe3aa6bd5)) (char *out, uint32_t size)

通过回调函数获取数据。当API需要将数据的下一部分发送到服务器时，将调用此回调。

typedef enum [Rcp_ContentOrPathOrCallbackType](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__gaa5a592f4e68a1dd43f5f41e95199a5e4)[Rcp_ContentOrPathOrCallbackType](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__gaa0382cf2e96821ed741ad9f99dd9e37a)

回调的内容、路径或类型。用于区分[Rcp_ContentOrPathOrCallback](Rcp_ContentOrPathOrCallback.md)中使用的数据。

typedef struct [Rcp_Buffer](Rcp_Buffer.md)[Rcp_Buffer](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga74d7d9dd56fabaa773cf1659c2d2eace)

文本存储结构。

typedef struct [Rcp_ContentOrPathOrCallback](Rcp_ContentOrPathOrCallback.md)[Rcp_ContentOrPathOrCallback](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__gaebb5b634a56751ae23ac2610e230ec72)

[Rcp_FormFieldFileValue](Rcp_FormFieldFileValue.md)中使用的简单表单数据字段值。

typedef enum [Rcp_MultipartValueType](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga76d003b4f9a244c9d11def4128ceeda8)[Rcp_MultipartValueType](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__gafeeacbc819f33dae11912a0c59f4a678)

多部分值类型。用于区分[Rcp_MultipartFormFieldValue](Rcp_MultipartFormFieldValue.md)中使用的数据。

typedef struct [Rcp_FormFieldFileValue](Rcp_FormFieldFileValue.md)[Rcp_FormFieldFileValue](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga774f6381467f16c39aaa2988c69ad7fd)

表单字段文件值。

typedef struct [Rcp_FormFieldValue](Rcp_FormFieldValue.md)[Rcp_FormFieldValue](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__gaf68638c39567d0c7b1e9ed0f145ebc65)

简单表单数据字段值，参见[Rcp_Form](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga40787f67faf4ea7111e4cda03f3f16be)和[Rcp_MultipartFormFieldValue](Rcp_MultipartFormFieldValue.md)。

typedef struct [Rcp_MultipartFormFieldValue](Rcp_MultipartFormFieldValue.md)[Rcp_MultipartFormFieldValue](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga64c7e2addc25dd589c5f65237eded576)

多部分表单域值，在[Rcp_MultipartForm](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga9f974771548d3ed2054aba0e7506fef9)中使用。

typedef enum [Rcp_ContentType](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga05daeab5ad8d265834b4a1b4e61cd8fa)[Rcp_ContentType](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__gacb1c467d93e50c5cdd7ace89f1369975)

内容类型。用于区分[Rcp_RequestContent](Rcp_RequestContent.md)中使用的数据。

typedef struct [Rcp_Form](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga40787f67faf4ea7111e4cda03f3f16be)[Rcp_Form](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga40787f67faf4ea7111e4cda03f3f16be)

简单表单。

typedef struct [Rcp_MultipartForm](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga9f974771548d3ed2054aba0e7506fef9)[Rcp_MultipartForm](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga9f974771548d3ed2054aba0e7506fef9)

多部分表单。

typedef struct [Rcp_RequestContent](Rcp_RequestContent.md)[Rcp_RequestContent](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__gaaf7ad4248342bb42ae9af6eb883e7679)

请求的内容。

typedef struct [Rcp_Headers](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__gac4f343ec02dec34268e93ce746e6c982)[Rcp_Headers](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__gac4f343ec02dec34268e93ce746e6c982)

请求或响应的标头。

typedef struct [Rcp_HeaderValue](Rcp_HeaderValue.md)[Rcp_HeaderValue](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__gac6096559a00691522790022a9335922a)

请求或响应的标头映射的值类型。

typedef struct [Rcp_HeaderEntry](Rcp_HeaderEntry.md)[Rcp_HeaderEntry](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__gae0d149375558a4b9de6058ee281a49c3)

请求或响应的标头的所有键值对。

typedef enum [Rcp_AuthenticationType](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__gaa1b9ec2bd61b2c95492f45eb0a447bff)[Rcp_AuthenticationType](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga60aa25edf4cc00a574abb8ffebcb7f60)

枚举类型。服务器的身份验证类型。如果未设置，请与服务器协商。

typedef struct [Rcp_Credential](Rcp_Credential.md)[Rcp_Credential](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga15452ad2af919bfffeb3a1f723e1eb5d)

凭据。某些服务器或代理服务器需要。

typedef struct [Rcp_ServerAuthentication](Rcp_ServerAuthentication.md)[Rcp_ServerAuthentication](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga9977de0042837319e439fdfe28ec6af8)

服务器身份验证。

typedef bool(* [Rcp_ExclusionFunction](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__gac6517b72e4a8c0feaf864f3669d2c127)) (const char *url)

判断host是否使用代理的函数指针。

typedef struct [Rcp_Urls](Rcp_Urls.md)[Rcp_Urls](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga4580ece64cbef2ce6cd66e0153f31721)

url，用于确定主机是否正在使用代理。

typedef enum [Rcp_ExclusionsValueType](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga1f5ed8748d80bca8e803ea26d63d1ecf)[Rcp_ExclusionsValueType](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__gae691e3a52b7d410309e096d3a6083385)

代理排除中使用的数据类型. 用于区分[Rcp_Exclusions](Rcp_Exclusions.md)中使用的数据。

typedef struct [Rcp_Exclusions](Rcp_Exclusions.md)[Rcp_Exclusions](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__gac98e0508b4e76da5550bdf49b00a28de)

代理配置中用于过滤不使用代理的URLs。

typedef enum [Rcp_CertType](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga4f79c1d41b9c586d99f1c22ed81b9aee)[Rcp_CertType](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga1862154a92f9f18850df7981e4eb7835)

客户端证书类型。

typedef struct [Rcp_CertificateAuthority](Rcp_CertificateAuthority.md)[Rcp_CertificateAuthority](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga5f3dcd559a5c06922af97232ef415a25)

用于验证远程服务器标识的证书颁发机构（CA）。

typedef struct [Rcp_ClientCertificate](Rcp_ClientCertificate.md)[Rcp_ClientCertificate](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga845e91b33e622fea75ca06bda166e5e9)

发送到远程服务器的客户端证书，远程服务器将使用它来验证客户端的标识。

typedef enum [Rcp_RemoteValidationType](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__gaf9356aea6a8c2e447efe3cf7fa889b87)[Rcp_RemoteValidationType](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga188c30a5aa5e064b2b366cfc04c901e7)

远程验证类型。

typedef struct [Rcp_SecurityConfiguration](Rcp_SecurityConfiguration.md)[Rcp_SecurityConfiguration](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__gae90019e06749ddcbc625d7b466b39d6b)

请求的安全配置。

typedef enum [Rcp_ProxyTunnelMode](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga7ae11929cb19cd85be3dd97e712e2ac6)[Rcp_ProxyTunnelMode](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga2c01e03e43784509918e5d3641371e6b)

用于控制何时创建代理隧道。 隧道或隧道传输意味着向代理发送HTTP CONNECT请求，要求它连接到特定端口号上的远程主机，然后流量只是通过代理。“auto”表示为HTTPS创建隧道。“always”表示始终创建隧道。

typedef struct [Rcp_WebProxy](Rcp_WebProxy.md)[Rcp_WebProxy](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga389f9fb59be18ed6ac4ae970eeb4a1a8)

自定义代理配置。

typedef struct [Rcp_IpAndPort](Rcp_IpAndPort.md)[Rcp_IpAndPort](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__gaad7a7752372c8b74f57204678240ad56)

该接口用在[Rcp_DnsServers](Rcp_DnsServers.md)中，表示一个DNS服务器的地址和端口。

typedef struct [Rcp_DnsServers](Rcp_DnsServers.md)[Rcp_DnsServers](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga58948b274c22ba906ac5527c6b5a8a75)

DNS服务器。[Rcp_DnsConfiguration.dnsRules](Rcp_DnsConfiguration.md#ZH-CN_TOPIC_0000002317126061__ab09aacb68c682d9beea100cae481eaa4)中的类型之一。

typedef struct [Rcp_IpAddress](Rcp_IpAddress.md)[Rcp_IpAddress](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__gaeaf532cd57e6cfc944f77bd0ac9cd205)

指定静态DNS规则使用的IP地址组。用于[Rcp_StaticDnsRuleItem](Rcp_StaticDnsRuleItem.md)。

typedef struct [Rcp_StaticDnsRuleItem](Rcp_StaticDnsRuleItem.md)[Rcp_StaticDnsRuleItem](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__gad8ad9f5130bca04060b5ffad30a915e8)

描述单个静态DNS规则。

typedef struct [Rcp_StaticDnsRule](Rcp_StaticDnsRule.md)[Rcp_StaticDnsRule](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga2fb8b04fec14262d27e95ec33f5a8349)

静态DNS规则。

typedef [Rcp_IpAddress](Rcp_IpAddress.md) *(* [Rcp_DynamicDnsRuleFunction](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__gad0ace0c83dd20972b34ff1538700eab3)) (const char *host, uint16_t port)

一个可以根据主机名和端口直接返回IP地址的函数。用于动态DNS解析。

typedef enum [Rcp_DnsRuleType](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga995c92778c5b31c9b4b586c737cfdd3c)[Rcp_DnsRuleType](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga925086d48b97774cc082773be635e3a1)

DNS规则类型。用于区分[Rcp_DnsRule](Rcp_DnsRule.md)中使用的dns规则类型。

typedef struct [Rcp_DnsRule](Rcp_DnsRule.md)[Rcp_DnsRule](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga8acd52cb973f1ce65afffb719fe4026d)

DNS规则配置。

typedef size_t(* [Rcp_OnDataReceiveCallbackFunc](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__gadc4e28c213ddc694e3c0ec76296ef5c0)) (void *usrObject, const char *data)

接收到响应正文时调用的回调函数。

typedef size_t(* [Rcp_OnBinaryReceiveCallbackFunc](RemoteCommunication.md#section1476912410533)) (void *usrObject, [Rcp_Buffer](Rcp_Buffer.md) *buffer)

接收到响应正文时调用的回调函数（二进制数据）。

typedef void (* [Rcp_OnStatusCodeReceiveCallbackFunc](RemoteCommunication.md#section1961611617339))(void *usrObject, uint32_t statusCode)

接收到响应状态码时调用的回调函数。

typedef void(* [Rcp_OnProgressCallbackFunc](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__gaaf74ce6d5578d28829955208318d3fbe)) (void *usrObject, uint64_t totalSize, uint64_t transferredSize)

请求/响应数据传输过程中调用的回调函数。

typedef void(* [Rcp_OnHeaderReceiveCallbackFunc](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__gae90a801a6c386c246e5005eadfe7da0a)) (void *usrObject, [Rcp_Headers](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__gac4f343ec02dec34268e93ce746e6c982) *headers)

收到所有请求时调用的回调。

typedef void(* [Rcp_OnVoidCallbackFunc](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga3d6a448e8f0bdcc2b4e70fa6ca00d475)) (void *usrObject)

请求的DataEnd或Canceled事件回调的回调函数。

typedef struct [Rcp_OnDataReceiveCallback](Rcp_OnDataReceiveCallback.md)[Rcp_OnDataReceiveCallback](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__gacd66d521a147a876e340aed45a3ed1c4)

接收到数据时回调。[Rcp_EventsHandler](Rcp_EventsHandler.md)中的配置。

typedef struct [Rcp_OnProgressCallback](Rcp_OnProgressCallback.md)[Rcp_OnProgressCallback](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__gabd25a25747d1c91772677f68ec8afc67)

收发时回调配置，在[Rcp_EventsHandler](Rcp_EventsHandler.md)中配置。

typedef struct [Rcp_OnHeaderReceiveCallback](Rcp_OnHeaderReceiveCallback.md)[Rcp_OnHeaderReceiveCallback](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__gab23c23acd8c159dfbaf00e439a08caf4)

[Rcp_EventsHandler](Rcp_EventsHandler.md)中配置的接收到的header的回调配置。

typedef struct [Rcp_OnVoidCallback](Rcp_OnVoidCallback.md)[Rcp_OnVoidCallback](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__gadda85b3a46176f92d45f30d97a78494f)

在[Rcp_EventsHandler](Rcp_EventsHandler.md)中配置的数据结束或已取消事件的回调配置。

typedef struct [Rcp_EventsHandler](Rcp_EventsHandler.md)[Rcp_EventsHandler](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga7d9b30e24c4f42e2da0938c04977b6a4)

监听不同HTTP事件的回调函数。

typedef struct [Rcp_Timeout](Rcp_Timeout.md)[Rcp_Timeout](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga4e16d4d91f394ab2070adc42d07b16fa)

请求的超时配置。

typedef struct [Rcp_DnsOverHttps](Rcp_DnsOverHttps.md)[Rcp_DnsOverHttps](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga514d31fc0e2abc3d0138226287c35aa4)

HTTPS上的DNS配置如果设置，则首选由DOH dns服务器解析的地址。

typedef enum [Rcp_PathPreference](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga9498d24addbd529f258fd6faacfd9c67)[Rcp_PathPreference](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga4f6c04d042df5e2835f1d771205aad24)

请求路径首选项。

typedef struct [Rcp_TransferConfiguration](Rcp_TransferConfiguration.md)[Rcp_TransferConfiguration](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga1b92400a50ef056d4490220cf2cefbda)

传输配置。

typedef struct [Rcp_InfoToCollect](Rcp_InfoToCollect.md)[Rcp_InfoToCollect](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga571eceac21f6acbf6fb846ac5a1abd55)

指定要收集的请求处理事件。可以通过响应对象检查收集的事件。

typedef struct [Rcp_TracingConfiguration](Rcp_TracingConfiguration.md)[Rcp_TracingConfiguration](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga8a0a1aa17cd22e2ac5389d55101fe4c5)

请求追踪配置。

typedef enum [Rcp_ProxyType](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__gacfad61d189683cbc02c969a63e246ca1)[Rcp_ProxyType](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga54cfc687bda5aafc6199dfe678e3a2c9)

代理类型。用于区分不同的代理配置。

typedef struct [Rcp_ProxyConfiguration](Rcp_ProxyConfiguration.md)[Rcp_ProxyConfiguration](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__gabc9a05c4bd32b7293392423797fb8e73)

代理配置。

typedef struct [Rcp_DnsConfiguration](Rcp_DnsConfiguration.md)[Rcp_DnsConfiguration](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga5f45694c1825bec6ceb5c7a8591d5127)

DNS解析配置。

typedef struct [Rcp_Configuration](Rcp_Configuration.md)[Rcp_Configuration](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga4ecea20272b8fe673f842e5486ba463b)

请求配置。

typedef struct [Rcp_TransferRange](Rcp_TransferRange.md)[Rcp_TransferRange](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__gaf0e1f4ea19d1c9efa13dc794c6c6590b)

HTTP传输范围。该设置将转换为HTTP Range标头。具有范围标头的HTTP请求要求服务器仅发送回HTTP响应的一部分。

typedef struct [Rcp_RequestCookies](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga44f2b679fefd37e78c43dbcba59d6d50)[Rcp_RequestCookies](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga44f2b679fefd37e78c43dbcba59d6d50)

请求Cookie。

typedef struct [Rcp_Request](Rcp_Request.md)[Rcp_Request](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga98dde966841135537e05053bf4da4d5b)

网络请求。

typedef struct [Rcp_RequestCookieEntry](Rcp_RequestCookieEntry.md)[Rcp_RequestCookieEntry](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__gab2690d1fbefb9998606757527f1b7b15)

描述请求的所有Cookie键值对。

typedef enum [Rcp_StatusCode](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga97929a5349f04300f50318f50393b93e)[Rcp_StatusCode](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__gae926416f69908e790e9bc67bb1e2d1f3)

请求响应的状态码。

typedef enum [Rcp_DebugEvent](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__gadff9eaa1b517bf01defd1273b2eeddbc)[Rcp_DebugEvent](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga79f61404bcc66d914e298c5362d73d69)

描述调试信息的事件类型。

typedef struct [Rcp_DebugInfo](Rcp_DebugInfo.md)[Rcp_DebugInfo](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga5738cb7a4a2768ecf909a22cfba77e0f)

描述存储在[Rcp_Response](Rcp_Response.md)中的调试信息的结构。

typedef struct [Rcp_CookieAttributes](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga08c7b992199bec7e5acdc50ce8ae2651)[Rcp_CookieAttributes](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga08c7b992199bec7e5acdc50ce8ae2651)

描述[Rcp_Response](Rcp_Response.md)中Cookie属性的类型。

typedef struct [Rcp_CookieAttributeEntry](Rcp_CookieAttributeEntry.md)[Rcp_CookieAttributeEntry](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__gaaff95756175ea20a41b1134c6aefb45e)

响应Cookie属性条目。

typedef struct [Rcp_ResponseCookies](Rcp_ResponseCookies.md)[Rcp_ResponseCookies](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga71bcf6497f4d94dc7bbc50adcfee081f)

响应Cookie。

typedef struct [Rcp_TimeInfo](Rcp_TimeInfo.md)[Rcp_TimeInfo](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga0ca30b26b3aeba0a436ac9bbd41c484b)

响应计时信息。

typedef struct [Rcp_Response](Rcp_Response.md)[Rcp_Response](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__gaefca0869b44c6d31f91db0b3476f7863)

网络请求的响应。

typedef void(* [Rcp_ResponseCallback](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga9403920c5b3bbe62d14816c693f5e024)) (void *usrCtx, [Rcp_Response](Rcp_Response.md) *response, uint32_t errCode)

响应回调函数指针。

typedef struct [Rcp_ResponseCallbackObject](Rcp_ResponseCallbackObject.md)[Rcp_ResponseCallbackObject](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga815137188d22749aff74afef7387860a)

响应回调结构体。

typedef struct [Rcp_RequestHandler](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga5ac080855c3aaef66c58d5b5b371be2b)[Rcp_RequestHandler](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga5ac080855c3aaef66c58d5b5b371be2b)

与[Rcp_Interceptor](Rcp_Interceptor.md)关联的异步处理器。

typedef struct [Rcp_SyncRequestHandler](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga2067d1b09b33afa0b8237a049687e9ea)[Rcp_SyncRequestHandler](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga2067d1b09b33afa0b8237a049687e9ea)

与[Rcp_SyncInterceptor](Rcp_SyncInterceptor.md)关联的同步处理器。

typedef struct [Rcp_Interceptor](Rcp_Interceptor.md)[Rcp_Interceptor](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga574aa47231df9c57b58c3aff0736c5e5)

异步拦截器。

typedef struct [Rcp_SyncInterceptor](Rcp_SyncInterceptor.md)[Rcp_SyncInterceptor](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga43a43cc8e864121ada235f484ffefece)

同步拦截器。

typedef struct [Rcp_InterceptorArray](Rcp_InterceptorArray.md)[Rcp_InterceptorArray](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga58ca95fc666a9a5694e92da1ce9b5c0b)

异步拦截器数组。

typedef struct [Rcp_SyncInterceptorArray](Rcp_SyncInterceptorArray.md)[Rcp_SyncInterceptorArray](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga8612d3521508093ed36be72b7f5cb373)

同步拦截器数组。

typedef enum [Rcp_SessionType](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga4fa3aa6821b16425c260d837deace956)[Rcp_SessionType](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga5254a5bead7a2562f9593d33018f460c)

会话类型。

typedef struct [Rcp_Session](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga4f3a7d39c18fe6fdf01c52759213ddcd)[Rcp_Session](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga4f3a7d39c18fe6fdf01c52759213ddcd)

会话。

typedef struct [Rcp_SessionListener](Rcp_SessionListener.md)[Rcp_SessionListener](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga43cd805167e33b051ccbe940d75f5966)

关闭或取消会话事件的回调函数。

typedef struct [Rcp_ConnectionConfiguration](Rcp_ConnectionConfiguration.md)[Rcp_ConnectionConfiguration](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__gac814a198390d0e7a094b241542c9139d)

连接配置。

typedef struct [Rcp_SessionConfiguration](Rcp_SessionConfiguration.md)[Rcp_SessionConfiguration](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga2d8aab48bdb45313f589dbd8ec00e36c)

会话配置。

typedef struct [Rcp_OnBinaryReceiveCallback](Rcp_OnBinaryReceiveCallback.md)[Rcp_OnBinaryReceiveCallback](Rcp_OnBinaryReceiveCallback.md)

响应的二进制数据接收回调函数。

typedef size_t(* [Rcp_OnBinaryReceiveCallbackFunc](RemoteCommunication.md#section1476912410533)) (void *usrObject, [Rcp_Buffer](Rcp_Buffer.md) *buffer)

二进制数据接收回调函数指针。

#### 枚举

名称

描述

[Rcp_FormValueType](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga9d851389347a39bd4bb849ac31cfa478) {

RCP_FORM_VALUE_TYPE_INT32, RCP_FORM_VALUE_TYPE_INT64, RCP_FORM_VALUE_TYPE_BOOL, RCP_FORM_VALUE_TYPE_STRING,

RCP_FORM_VALUE_TYPE_DOUBLE

}

表单值类型。

[Rcp_ContentOrPathOrCallbackType](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__gaa5a592f4e68a1dd43f5f41e95199a5e4) { RCP_FILE_VALUE_TYPE_CONTENT, RCP_FILE_VALUE_TYPE_PATH, RCP_FILE_VALUE_TYPE_CALLBACK}

回调的内容、路径或类型。用于区分[Rcp_ContentOrPathOrCallback](Rcp_ContentOrPathOrCallback.md)中使用的数据。

[Rcp_MultipartValueType](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga76d003b4f9a244c9d11def4128ceeda8) { RCP_TYPE_FORM_FIELD_VALUE, RCP_TYPE_FORM_FIELD_FILE_VALUE }

多部分值类型。用于区分[Rcp_MultipartFormFieldValue](Rcp_MultipartFormFieldValue.md)中使用的数据。

[Rcp_ContentType](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga05daeab5ad8d265834b4a1b4e61cd8fa) { RCP_CONTENT_TYPE_STRING, RCP_CONTENT_TYPE_FORM, RCP_CONTENT_TYPE_MULTIPARTFORM, RCP_CONTENT_TYPE_GETCALLBACK }

内容类型。用于区分[Rcp_RequestContent](Rcp_RequestContent.md)中使用的数据。

[Rcp_AuthenticationType](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__gaa1b9ec2bd61b2c95492f45eb0a447bff) { RCP_AUTHENTICATION_AUTO, RCP_AUTHENTICATION_BASIC, RCP_AUTHENTICATION_NTLM, RCP_AUTHENTICATION_DIGEST }

枚举类型。服务器的身份验证类型。如果未设置，请与服务器协商。

[Rcp_ExclusionsValueType](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga1f5ed8748d80bca8e803ea26d63d1ecf) { RCP_EXCLUSION_USE_URL_ARRAY, RCP_EXCLUSION_USE_CALLBACK }

代理排除中使用的数据类型. 用于区分[Rcp_Exclusions](Rcp_Exclusions.md)中使用的数据。

[Rcp_CertType](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga4f79c1d41b9c586d99f1c22ed81b9aee) { RCP_CERT_PEM, RCP_CERT_DER, RCP_CERT_P12 }

客户端证书类型。

[Rcp_RemoteValidationType](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__gaf9356aea6a8c2e447efe3cf7fa889b87) { RCP_REMOTE_VALIDATION_SYSTEM, RCP_REMOTE_VALIDATION_SKIP, RCP_REMOTE_VALIDATION_CERTIFICATE_AUTHORITY }

远程验证类型。

[Rcp_ProxyTunnelMode](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga7ae11929cb19cd85be3dd97e712e2ac6) { RCP_PROXY_TUNNEL_AUTO, RCP_PROXY_TUNNEL_ALWAYS }

用于控制何时创建代理隧道。 隧道或隧道传输意味着向代理发送HTTP CONNECT请求，要求它连接到特定端口号上的远程主机，然后流量只是通过代理。“auto”表示为HTTPS创建隧道。“always”表示始终创建隧道。

[Rcp_DnsRuleType](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga995c92778c5b31c9b4b586c737cfdd3c) { RCP_DNS_RULE_DNS_SERVERS, RCP_DNS_RULE_STATIC, RCP_DNS_RULE_DYNAMIC }

DNS规则类型。用于区分[Rcp_DnsRule](Rcp_DnsRule.md)中使用的dns规则类型。

[Rcp_PathPreference](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga9498d24addbd529f258fd6faacfd9c67) { RCP_PATH_PREFERENCE_AUTO, RCP_PATH_PREFERENCE_WIFI, RCP_PATH_PREFERENCE_CELLULAR }

请求路径首选项。

[Rcp_ProxyType](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__gacfad61d189683cbc02c969a63e246ca1) { RCP_PROXY_SYSTEM, RCP_PROXY_CUSTOM, RCP_PROXY_NO_PROXY }

代理类型。用于区分不同的代理配置。

[Rcp_StatusCode](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga97929a5349f04300f50318f50393b93e) {

RCP_NONE = 0, RCP_OK = 200, RCP_CREATED, RCP_ACCEPTED,

RCP_NOT_AUTHORITATIVE, RCP_NO_CONTENT, RCP_RESET, RCP_PARTIAL,

RCP_MULTI_CHOICE = 300, RCP_MOVED_PERMANENTLY, RCP_MOVED_TEMPORARILY, RCP_SEE_OTHER,

RCP_NOT_MODIFIED, RCP_USE_PROXY, RCP_BAD_REQUEST = 400, RCP_UNAUTHORIZED,

RCP_PAYMENT_REQUIRED, RCP_FORBIDDEN, RCP_NOT_FOUND, RCP_BAD_METHOD,

RCP_NOT_ACCEPTABLE, RCP_PROXY_AUTH, RCP_CLIENT_TIMEOUT, RCP_CONFLICT,

RCP_GONE, RCP_LENGTH_REQUIRED, RCP_PRECON_FAILED, RCP_ENTITY_TOO_LARGE,

RCP_REQ_TOO_LONG, RCP_UNSUPPORTED_TYPE, RCP_INTERNAL_ERROR = 500, RCP_NOT_IMPLEMENTED,

RCP_BAD_GATEWAY, RCP_UNAVAILABLE, RCP_GATEWAY_TIMEOUT, RCP_VERSION

}

请求响应的状态码。

[Rcp_DebugEvent](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__gadff9eaa1b517bf01defd1273b2eeddbc) {

RCP_DEBUG_EVENT_TEXT, RCP_DEBUG_EVENT_HEADER_IN, RCP_DEBUG_EVENT_HEADER_OUT, RCP_DEBUG_EVENT_DATA_IN,

RCP_DEBUG_EVENT_DATA_OUT, RCP_DEBUG_EVENT_SSL_DATA_IN, RCP_DEBUG_EVENT_SSL_DATA_OUT

}

描述调试信息的事件类型。

[Rcp_SessionType](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga4fa3aa6821b16425c260d837deace956) { RCP_SESSION_TYPE_HTTP = 0, RCP_SESSION_TYPE_MAX = 100}

会话类型。

#### 函数

名称

描述

[Rcp_Form](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga40787f67faf4ea7111e4cda03f3f16be) * [HMS_Rcp_CreateForm](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__gaf46149196c94385e7d8af6c17d1cfab0) (void)

创建一个简单表单。

void [HMS_Rcp_DestroyForm](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga871fb9f3865c854e38594871b8e65b86) ([Rcp_Form](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga40787f67faf4ea7111e4cda03f3f16be) *form)

销毁一个简单表单。

uint32_t [HMS_Rcp_SetFormValue](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga58aba2b2c4bb1bf93aef474c4427638f) ([Rcp_Form](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga40787f67faf4ea7111e4cda03f3f16be) *form, const char *key, const [Rcp_FormFieldValue](Rcp_FormFieldValue.md) *value)

设置简单表单的键值对。

[Rcp_FormFieldValue](Rcp_FormFieldValue.md) * [HMS_Rcp_GetFormValue](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga1b8e250780190403f0a0d63ab0604017) ([Rcp_Form](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga40787f67faf4ea7111e4cda03f3f16be) *form, const char *key)

通过键获取一个简单表单的对应值。

[Rcp_MultipartForm](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga9f974771548d3ed2054aba0e7506fef9) * [HMS_Rcp_CreateMultipartForm](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga2d3c7ad8cd5d670bb4c40b400da52a63) (void)

创建一个多部分表单。

void [HMS_Rcp_DestroyMultipartForm](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga449c4206aec628b1a0a4a2b9b7aafd53) ([Rcp_MultipartForm](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga9f974771548d3ed2054aba0e7506fef9) *multipartForm)

销毁一个多部分表单。

uint32_t [HMS_Rcp_SetMultipartFormValue](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga5148d54bff9d344085c3baa72918dbe9) ([Rcp_MultipartForm](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga9f974771548d3ed2054aba0e7506fef9) *multipartForm, const char *key, const [Rcp_MultipartFormFieldValue](Rcp_MultipartFormFieldValue.md) *value)

设置多部分表单的键值对。

[Rcp_MultipartFormFieldValue](Rcp_MultipartFormFieldValue.md) * [HMS_Rcp_GetMultipartFormValue](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga22d2c7c599edf491eabf84d1eeaee533) ([Rcp_MultipartForm](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga9f974771548d3ed2054aba0e7506fef9) *multipartForm, const char *key)

通过键获取多部分表单的值。

[Rcp_Headers](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__gac4f343ec02dec34268e93ce746e6c982) * [HMS_Rcp_CreateHeaders](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__gab797b6fcc146d8b181fb138d424c4800) (void)

为请求或响应创建标头。

void [HMS_Rcp_DestroyHeaders](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__gaee22e11cc947ae599214df9e84a59ae5) ([Rcp_Headers](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__gac4f343ec02dec34268e93ce746e6c982) *headers)

销毁请求或响应的标头。

uint32_t [HMS_Rcp_SetHeaderValue](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__gafb04d92353985e2f4f9f6c2950019068) ([Rcp_Headers](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__gac4f343ec02dec34268e93ce746e6c982) *headers, const char *name, const char *value)

设置请求或响应头的键值对。

[Rcp_HeaderValue](Rcp_HeaderValue.md) * [HMS_Rcp_GetHeaderValue](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga9c8f0d455b76b21dce29e7d425c31da3) ([Rcp_Headers](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__gac4f343ec02dec34268e93ce746e6c982) *headers, const char *name)

通过键获取请求或响应头的值。

[Rcp_HeaderEntry](Rcp_HeaderEntry.md) * [HMS_Rcp_GetHeaderEntries](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga94edbbabc6b1b76d0e0f729ca618458a) ([Rcp_Headers](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__gac4f343ec02dec34268e93ce746e6c982) *headers)

获取请求或响应头的所有键值对。

void [HMS_Rcp_DestroyHeaderEntries](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__gabd8ecd09483ea431cd32cc7218a4ed27) ([Rcp_HeaderEntry](Rcp_HeaderEntry.md) *headerEntry)

销毁[HMS_Rcp_GetHeaderEntries](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga94edbbabc6b1b76d0e0f729ca618458a)中获取的所有键值对。

[Rcp_Request](Rcp_Request.md) * [HMS_Rcp_CreateRequest](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga63b1b532e9b37754281c6bdfdf198597) (const char *url)

创建请求。

void [HMS_Rcp_DestroyRequest](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__gae2eb219a9afd7ace912e071775058aa2) ([Rcp_Request](Rcp_Request.md) *request)

销毁请求。

[Rcp_RequestCookies](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga44f2b679fefd37e78c43dbcba59d6d50) * [HMS_Rcp_CreateRequestCookies](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__gadb2b6465c6c1966d7983f57dda8582fc) (void)

创建空的请求Cookie。

void [HMS_Rcp_DestroyRequestCookies](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__gaca5c542e4cb61a95d3fbd31ebc07d4d0) ([Rcp_RequestCookies](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga44f2b679fefd37e78c43dbcba59d6d50) *cookies)

销毁请求Cookie。

uint32_t [HMS_Rcp_SetRequestCookieValue](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga27ca41ecf30e0f3a2d10fad61494130a) ([Rcp_RequestCookies](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga44f2b679fefd37e78c43dbcba59d6d50) *cookies, const char *name, const char *value)

设置请求Cookie。

char * [HMS_Rcp_GetRequestCookieValue](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga43a79371dfb3ff211321d1c18d4864b2) ([Rcp_RequestCookies](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga44f2b679fefd37e78c43dbcba59d6d50) *cookies, const char *name)

通过名称获取请求Cookie的值。

[Rcp_RequestCookieEntry](Rcp_RequestCookieEntry.md) * [HMS_Rcp_GetRequestCookieEntries](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga5980d5baff59f1902ff009e557ae9756) ([Rcp_RequestCookies](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga44f2b679fefd37e78c43dbcba59d6d50) *cookies)

获取请求Cookie中的所有键值对。

void [HMS_Rcp_DestroyRequestCookieEntries](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga4a75fce3b4d0b690eef330836977da14) ([Rcp_RequestCookieEntry](Rcp_RequestCookieEntry.md) *cookieEntry)

销毁从[HMS_Rcp_GetRequestCookieValue](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga43a79371dfb3ff211321d1c18d4864b2)获取的所有与请求Cookie相关的键值对。

const char * [HMS_Rcp_GetResponseCookieAttrValue](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga6538a77ca1dcabe15bb2891f941c377e) ([Rcp_CookieAttributes](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga08c7b992199bec7e5acdc50ce8ae2651) *cookieAttributes, const char *name)

通过名称获取Cookie属性的值。

[Rcp_CookieAttributeEntry](Rcp_CookieAttributeEntry.md) * [HMS_Rcp_GetResponseCookieAttrEntries](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga8304b7906b7e81b7135a50d77d6eaf48) ([Rcp_CookieAttributes](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga08c7b992199bec7e5acdc50ce8ae2651) *cookieAttributes)

在[Rcp_CookieAttributes](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga08c7b992199bec7e5acdc50ce8ae2651)中获取所有响应Cookie属性。

void [HMS_Rcp_DestroyResponseCookieAttrEntries](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga83afc8703c589133bf3768e631157413) ([Rcp_CookieAttributeEntry](Rcp_CookieAttributeEntry.md) *entries)

销毁响应Cookie属性。

uint32_t [HMS_Rcp_CallNextRequestHandler](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__gaa12f2da13b0aa095b7c6ae5e195c1536) ([Rcp_Request](Rcp_Request.md) *request, const [Rcp_RequestHandler](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga5ac080855c3aaef66c58d5b5b371be2b) *next, const [Rcp_ResponseCallbackObject](Rcp_ResponseCallbackObject.md) *responseCallback)

在拦截器[Rcp_Interceptor](Rcp_Interceptor.md)的函数中可以调用下一个拦截器或defaultHandler。

[Rcp_Response](Rcp_Response.md) * [HMS_Rcp_CallNextSyncRequestHandler](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga2a4e9df33b7f4c146e6fb1ddc46dc84f) ([Rcp_Request](Rcp_Request.md) *request, const [Rcp_SyncRequestHandler](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga2067d1b09b33afa0b8237a049687e9ea) *next, uint32_t *errCode)

在拦截器[Rcp_SyncInterceptor](Rcp_SyncInterceptor.md)的函数中可以调用下一个拦截器或默认处理器。

[Rcp_Session](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga4f3a7d39c18fe6fdf01c52759213ddcd) * [HMS_Rcp_CreateSession](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__gafc04f552e9d6b90d9d73abbc9535766e) (const [Rcp_SessionConfiguration](Rcp_SessionConfiguration.md) *configuration, uint32_t *errCode)

创建会话。

const char * [HMS_Rcp_GetSessionId](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga10f2bd857b521b631838b9e2428925c3) ([Rcp_Session](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga4f3a7d39c18fe6fdf01c52759213ddcd) *session)

获取会话ID。

const [Rcp_SessionConfiguration](Rcp_SessionConfiguration.md) * [HMS_Rcp_GetSessionConfiguration](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga990339ef86baed18b48fe3ef10031388) ([Rcp_Session](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga4f3a7d39c18fe6fdf01c52759213ddcd) *session)

获取会话配置。

[Rcp_Response](Rcp_Response.md) * [HMS_Rcp_FetchSync](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga48a83535a4658e9872ded4b0dd8c812f) ([Rcp_Session](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga4f3a7d39c18fe6fdf01c52759213ddcd) *session, [Rcp_Request](Rcp_Request.md) *request, uint32_t *errCode)

发送同步请求并获取响应。

uint32_t [HMS_Rcp_Fetch](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga7ea546b69b9ea60ea4716ee64e8b04cb) ([Rcp_Session](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga4f3a7d39c18fe6fdf01c52759213ddcd) *session, [Rcp_Request](Rcp_Request.md) *request, const [Rcp_ResponseCallbackObject](Rcp_ResponseCallbackObject.md) *responseCallback)

发送异步请求并获取响应。

uint32_t [HMS_Rcp_CancelRequest](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__gae7974f60c9b17a16e853befd391b7f81) ([Rcp_Session](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga4f3a7d39c18fe6fdf01c52759213ddcd) *session, const [Rcp_Request](Rcp_Request.md) *request)

取消一个请求。

uint32_t [HMS_Rcp_CancelSession](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga4ef7303528c1ce13cf5f1267c0650221) ([Rcp_Session](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga4f3a7d39c18fe6fdf01c52759213ddcd) *session)

取消会话。

uint32_t [HMS_Rcp_CloseSession](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__gaf659dbbb59360b9c587fb4081b52dd14) ([Rcp_Session](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga4f3a7d39c18fe6fdf01c52759213ddcd) **session)

关闭会话。

uint32_t [HMS_Rcp_SetRequestOnBinaryDataRecvCallback](RemoteCommunication.md#section207321113884) ([Rcp_Request](Rcp_Request.md) *request, [Rcp_OnBinaryReceiveCallback](Rcp_OnBinaryReceiveCallback.md) onBinaryReceiveCallback)

为请求设置流式接收二进制数据的回调函数。该回调函数与[Rcp_OnDataReceiveCallback](Rcp_OnDataReceiveCallback.md)功能一致，功能上可以包含字符数据和二进制数据。