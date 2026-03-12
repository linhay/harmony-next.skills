# Rcp_SyncInterceptor

#### 概述

同步拦截器。

**起始版本：** 5.0.0(12)

**相关模块：**[RemoteCommunication](RemoteCommunication.md)

#### 汇总

#### 成员变量

名称

描述

[Rcp_Response](Rcp_Response.md) *(* [intercept](Rcp_SyncInterceptor.md#ZH-CN_TOPIC_0000002317125989__a4422febd3ef69e443ab4514d4c579aa8) )([Rcp_Request](Rcp_Request.md) *request, const [Rcp_SyncRequestHandler](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga2067d1b09b33afa0b8237a049687e9ea) *next, uint32_t *errCode)

指向同步拦截器函数的指针。用户若需要使用拦截器，需实现该函数。

#### 结构体成员变量说明

#### intercept

```ets
[Rcp_Response](Rcp_Response.md)*(* Rcp_SyncInterceptor::intercept) ([Rcp_Request](Rcp_Request.md) *request, const [Rcp_SyncRequestHandler](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga2067d1b09b33afa0b8237a049687e9ea) *next, uint32_t *errCode)
```

**描述**

指向同步拦截器函数的指针。用户若需要使用拦截器，需实现该函数。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

request

指向[Rcp_Request](Rcp_Request.md)的指针。

next

指向下一个同步处理器的指针[Rcp_SyncRequestHandler](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga2067d1b09b33afa0b8237a049687e9ea)。

errCode

表示拦截器的返回值。

**返回：**

Rcp_Response* 返回的响应。