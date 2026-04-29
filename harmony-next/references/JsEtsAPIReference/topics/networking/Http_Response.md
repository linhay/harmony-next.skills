# [Http_Response](Http_Response.md)

```ets
typedef struct Http_Response {...} Http_Response
```

#### 概述

定义HTTP响应的结构体。

**起始版本：** 20

**相关模块：**[netstack](Netstack.md)

所在头文件： [net_http_type.h](net_http_type.h.md)

#### 汇总

#### 成员变量

| 名称 | 描述 |
| --- | --- |
| [Http_Buffer](Http_Buffer.md) body | HTTP请求响应的数据，参考Http_Buffer。 |
| [Http_ResponseCode](net_http_type.h.md#ZH-CN_TOPIC_0000002497605460__http_responsecode) responseCode | HTTP请求响应码，参考Http_ResponseCode。 |
| [Http_Headers](Http_Headers.md) *headers | HTTP响应的头，指向Http_Headers的指针，参考Http_Headers。 |
| char *cookies | HTTP响应Cookies。 |
| [Http_PerformanceTiming](Http_PerformanceTiming.md) *performanceTiming | HTTP响应时间信息，指向Http_PerformanceTiming的指针，参考Http_PerformanceTiming。 |

#### 成员函数

| 名称 | 描述 |
| --- | --- |
| void (*destroyResponse)(struct [Http_Response](Http_Response.md) **response) | 销毁HTTP响应的回调函数 |

#### 成员函数说明

#### destroyResponse()

```ets
void (*destroyResponse)(struct Http_Response **response)
```

**描述**

销毁HTTP响应的回调函数

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| struct [Http_Response](Http_Response.md) **response | 要销毁的HTTP响应，指向Http_Response的指针，参考Http_Response。 |
