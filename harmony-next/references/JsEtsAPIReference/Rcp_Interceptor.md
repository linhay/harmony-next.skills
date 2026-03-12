# Rcp_Interceptor

#### 概述

异步拦截器。

**起始版本：** 5.0.0(12)

**相关模块：**[RemoteCommunication](RemoteCommunication.md)

#### 汇总

#### 成员变量

名称

描述

uint32_t(* [intercept](Rcp_Interceptor.md#ZH-CN_TOPIC_0000002317126045__a479e39838d2b1c2792ee0152d2735cf6) )([Rcp_Request](Rcp_Request.md) *request, const [Rcp_RequestHandler](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga5ac080855c3aaef66c58d5b5b371be2b) *next, const [Rcp_ResponseCallbackObject](Rcp_ResponseCallbackObject.md) *responseCallback)

指向异步拦截器函数的指针。用户若需要使用拦截器，需实现该函数。

#### 结构体成员变量说明

#### intercept

```ets
uint32_t(* Rcp_Interceptor::intercept) ([Rcp_Request](Rcp_Request.md) *request, const [Rcp_RequestHandler](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga5ac080855c3aaef66c58d5b5b371be2b) *next, const [Rcp_ResponseCallbackObject](Rcp_ResponseCallbackObject.md) *responseCallback)
```

**描述**

指向异步拦截器函数的指针。用户若需要使用拦截器，需实现该函数。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

request

指向[Rcp_Request](Rcp_Request.md)的指针。

next

指向下一个异步处理器的指针[Rcp_RequestHandler](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga5ac080855c3aaef66c58d5b5b371be2b)。

responseCallback

指向[Rcp_ResponseCallbackObject](Rcp_ResponseCallbackObject.md)的指针。

**返回：**

uint32_t 返回表示拦截器的返回值。