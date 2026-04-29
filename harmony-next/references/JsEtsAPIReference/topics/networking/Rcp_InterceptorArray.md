# Rcp_InterceptorArray

**概述**

异步拦截器数组。

起始版本： 5.0.0(12)

相关模块： [RemoteCommunication](RemoteCommunication.md)

所在头文件： [rcp.h](rcp.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| Rcp_Interceptor * interceptors | 异步拦截器数组。 Rcp_Interceptor[]。 |
| int size | 数组大小。 |

**结构体成员变量说明**

**interceptors**

```ets
Rcp_Interceptor* Rcp_InterceptorArray::interceptors
```

描述

异步拦截器数组。 [Rcp_Interceptor](Rcp_Interceptor.md)[]。

**size**

```ets
int Rcp_InterceptorArray::size
```

描述

数组大小。