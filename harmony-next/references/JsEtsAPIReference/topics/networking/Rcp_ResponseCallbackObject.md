# Rcp_ResponseCallbackObject

**概述**

响应回调结构体。

起始版本： 5.0.0(12)

相关模块： [RemoteCommunication](RemoteCommunication.md)

所在头文件： [rcp.h](rcp.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| Rcp_ResponseCallbackcallback | 响应回调函数。 |
| void * usrCtx | 用户上下文。 |

**结构体成员变量说明**

**callback**

```ets
Rcp_ResponseCallback Rcp_ResponseCallbackObject::callback
```

描述

响应回调函数。

**usrCtx**

```ets
void* Rcp_ResponseCallbackObject::usrCtx
```

描述

用户上下文。