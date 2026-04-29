# Rcp_Interceptor

**概述**

异步拦截器。

起始版本： 5.0.0(12)

相关模块： [RemoteCommunication](RemoteCommunication.md)

所在头文件： [rcp.h](rcp.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| uint32_t(* intercept )(Rcp_Request *request, const Rcp_RequestHandler *next, const Rcp_ResponseCallbackObject *responseCallback) | 指向异步拦截器函数的指针。用户若需要使用拦截器，需实现该函数。 |

**结构体成员变量说明**

**intercept**

```ets
uint32_t(* Rcp_Interceptor::intercept) (Rcp_Request *request, const Rcp_RequestHandler *next, const Rcp_ResponseCallbackObject *responseCallback)
```

描述

指向异步拦截器函数的指针。用户若需要使用拦截器，需实现该函数。

起始版本： 5.0.0(12)

参数:

| 名称 | 描述 |
| --- | --- |
| request | 指向Rcp_Request的指针。 |
| next | 指向下一个异步处理器的指针Rcp_RequestHandler。 |
| responseCallback | 指向Rcp_ResponseCallbackObject的指针。 |

返回：

uint32_t 返回表示拦截器的返回值。