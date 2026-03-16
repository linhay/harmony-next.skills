# net_http.h

#### 概述

定义HTTP请求模块的接口。

**引用文件：** <network/netstack/net_http.h>

**库：** libnet_http.so

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 20

**相关模块：**[netstack](../../topics/networking/Netstack.md)

#### 汇总

#### 函数

名称描述[Http_Headers *OH_Http_CreateHeaders(void)](#ZH-CN_TOPIC_0000002529445425__oh_http_createheaders)创建HTTP请求或者响应的头。[void OH_Http_DestroyHeaders(Http_Headers **headers)](#ZH-CN_TOPIC_0000002529445425__oh_http_destroyheaders)销毁HTTP请求或者响应的头。[uint32_t OH_Http_SetHeaderValue(struct Http_Headers *headers, const char *name, const char *value)](#ZH-CN_TOPIC_0000002529445425__oh_http_setheadervalue)设置HTTP请求或者响应的头的键值对。[Http_HeaderValue *OH_Http_GetHeaderValue(Http_Headers *headers, const char *name)](#ZH-CN_TOPIC_0000002529445425__oh_http_getheadervalue)通过键获取请求或响应头的值。[Http_HeaderEntry *OH_Http_GetHeaderEntries(Http_Headers *headers)](#ZH-CN_TOPIC_0000002529445425__oh_http_getheaderentries)获取请求或响应头的所有键值对。[void OH_Http_DestroyHeaderEntries(Http_HeaderEntry **headerEntry)](#ZH-CN_TOPIC_0000002529445425__oh_http_destroyheaderentries)销毁OH_Http_GetHeaderEntries中获取的所有键值对。[Http_Request *OH_Http_CreateRequest(const char *url)](#ZH-CN_TOPIC_0000002529445425__oh_http_createrequest)创建HTTP请求。[int OH_Http_Request(Http_Request *request, Http_ResponseCallback callback, Http_EventsHandler handler)](#ZH-CN_TOPIC_0000002529445425__oh_http_request)发起HTTP请求。[void OH_Http_Destroy(struct Http_Request **request)](#ZH-CN_TOPIC_0000002529445425__oh_http_destroy)销毁HTTP请求。

#### 函数说明

#### OH_Http_CreateHeaders()

```ets
Http_Headers *OH_Http_CreateHeaders(void)
```

**描述**

创建HTTP请求或者响应的头。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 20

**返回：**

类型说明[Http_Headers](../../topics/networking/Http_Headers.md) *Http_Headers 返回HTTP请求或者响应的头，指向Http_Headers。

#### OH_Http_DestroyHeaders()

```ets
void OH_Http_DestroyHeaders(Http_Headers **headers)
```

**描述**

销毁HTTP请求或者响应的头。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 20

**参数：**

参数项描述[Http_Headers](../../topics/networking/Http_Headers.md) **headers要被销毁的HTTP请求或响应的头，是通过OH_Http_CreateHeaders生成的数据。

#### OH_Http_SetHeaderValue()

```ets
uint32_t OH_Http_SetHeaderValue(struct Http_Headers *headers, const char *name, const char *value)
```

**描述**

设置HTTP请求或者响应的头的键值对。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 20

**参数：**

参数项描述[struct Http_Headers](../../topics/networking/Http_Headers.md) *headers指向要设置的Http_Headers的指针。const char *name键值。const char *value键值对应的值。

**返回：**

类型说明uint32_tuint32_t 0 - 成功。 401 - 参数错误。 2300027 - 内存不足。

#### OH_Http_GetHeaderValue()

```ets
Http_HeaderValue *OH_Http_GetHeaderValue(Http_Headers *headers, const char *name)
```

**描述**

通过键获取请求或响应头的值。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 20

**参数：**

参数项描述[Http_Headers](../../topics/networking/Http_Headers.md) *headers指向要获取值的Http_Headers的指针。const char *name键值。

**返回：**

类型说明[Http_HeaderValue](../../topics/networking/Http_HeaderValue.md) *Http_HeaderValue 指向获取的Http_HeaderValue的指针。

#### OH_Http_GetHeaderEntries()

```ets
Http_HeaderEntry *OH_Http_GetHeaderEntries(Http_Headers *headers)
```

**描述**

获取请求或响应头的所有键值对。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 20

**参数：**

参数项描述[Http_Headers](../../topics/networking/Http_Headers.md) *headers指向要获取值的Http_Headers的指针。

**返回：**

类型说明[Http_HeaderEntry](../../topics/networking/Http_HeaderEntry.md) *Http_HeaderEntry 指向获取的Http_HeaderEntry的指针。

#### OH_Http_DestroyHeaderEntries()

```ets
void OH_Http_DestroyHeaderEntries(Http_HeaderEntry **headerEntry)
```

**描述**

销毁OH_Http_GetHeaderEntries中获取的所有键值对。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 20

**参数：**

参数项描述[Http_HeaderEntry](../../topics/networking/Http_HeaderEntry.md) **headerEntry指向要销毁的Http_HeaderEntry的指针，是通过OH_Http_GetHeaderEntries获取的数据。

#### OH_Http_CreateRequest()

```ets
Http_Request *OH_Http_CreateRequest(const char *url)
```

**描述**

创建HTTP请求。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 20

**参数：**

参数项描述const char *url请求URL。

**返回：**

类型说明[Http_Request](../../topics/networking/Http_Request.md) *返回创建的请求，指向Http_Request的指针。

#### OH_Http_Request()

```ets
int OH_Http_Request(Http_Request *request, Http_ResponseCallback callback, Http_EventsHandler handler)
```

**描述**

发起HTTP请求。

**系统能力：** SystemCapability.Communication.NetStack

**需要权限：** ohos.permission.INTERNET

**起始版本：** 20

**参数：**

参数项描述[Http_Request](../../topics/networking/Http_Request.md) *request发送的请求，指向Http_Request的指针。[Http_ResponseCallback](net_http_type.h.md#ZH-CN_TOPIC_0000002497605460__http_responsecallback) callback请求的响应，指向Http_ResponseCallback。[Http_EventsHandler](../../topics/networking/Http_EventsHandler.md) handler监听不同HTTP事件的回调函数，指向Http_EventsHandler。

**返回：**

类型说明int

请求发起成功返回0，非0表示请求发起失败，错误码的具体描述，可以参考Http_ErrCode。

 在Http_ResponseCallback中也会携带errCode信息，表示请求发起成功，但是因为一些原因，和服务器的交互异常，具体异常原因，同步参考Http_ErrCode。

#### OH_Http_Destroy()

```ets
void OH_Http_Destroy(struct Http_Request **request)
```

**描述**

销毁HTTP请求。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 20

**参数：**

参数项描述[struct Http_Request](../../topics/networking/Http_Request.md) **request要销毁的请求，指向Http_Request的指针，参考[Http_Request](../../topics/networking/Http_Request.md)。