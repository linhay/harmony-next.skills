# Rcp_OnProgressCallback

**概述**

收发时回调配置，在[Rcp_EventsHandler](Rcp_EventsHandler.md)中配置。

起始版本： 5.0.0(12)

相关模块： [RemoteCommunication](RemoteCommunication.md)

所在头文件： [rcp.h](rcp.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| Rcp_OnProgressCallbackFunccallback | 收发过程中的回调函数。 |
| void * usrObject | 用户定义的对象，在回调函数中使用。 |

**结构体成员变量说明**

**callback**

```ets
Rcp_OnProgressCallbackFunc Rcp_OnProgressCallback::callback
```

描述

收发过程中的回调函数。

**usrObject**

```ets
void* Rcp_OnProgressCallback::usrObject
```

描述

用户定义的对象，在回调函数中使用。