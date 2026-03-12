# Http_Response

```ets
typedef struct Http_Response {...} Http_Response
```

#### 概述

定义HTTP响应的结构体。

**起始版本：** 20

**相关模块：**[netstack](Netstack.md)

**所在头文件：**[net_http_type.h](net_http_type.h.md)

#### 汇总

#### 成员变量

名称描述[Http_Buffer](Http_Buffer.md) bodyHTTP请求响应的数据，参考[Http_Buffer](Http_Buffer.md)。[Http_ResponseCode](net_http_type.h.md#ZH-CN_TOPIC_0000002497605460__http_responsecode) responseCodeHTTP请求响应码，参考[Http_ResponseCode](net_http_type.h.md#ZH-CN_TOPIC_0000002497605460__http_responsecode)。[Http_Headers](Http_Headers.md) *headersHTTP响应的头，指向Http_Headers的指针，参考[Http_Headers](Http_Headers.md)。char *cookiesHTTP响应Cookies。[Http_PerformanceTiming](Http_PerformanceTiming.md) *performanceTimingHTTP响应时间信息，指向Http_PerformanceTiming的指针，参考[Http_PerformanceTiming](Http_PerformanceTiming.md)。

#### 成员函数

名称描述[void (*destroyResponse)(struct Http_Response **response)](#ZH-CN_TOPIC_0000002497605476__destroyresponse)销毁HTTP响应的回调函数

#### 成员函数说明

#### destroyResponse()

```ets
void (*destroyResponse)(struct Http_Response **response)
```

**描述**

销毁HTTP响应的回调函数

**起始版本：** 20

**参数：**

参数项描述struct [Http_Response](Http_Response.md) **response要销毁的HTTP响应，指向Http_Response的指针，参考[Http_Response](Http_Response.md)。