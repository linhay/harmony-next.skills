# Rcp_OnHeaderReceiveCallback

**概述**

[Rcp_EventsHandler](Rcp_EventsHandler.md)中配置的接收到的header的回调配置。

起始版本： 5.0.0(12)

相关模块： [RemoteCommunication](RemoteCommunication.md)

所在头文件： [rcp.h](rcp.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| Rcp_OnHeaderReceiveCallbackFunccallback | 接收到的headers的回调函数。 |
| void * usrObject | 用户定义的对象，在回调函数中使用。 |

**结构体成员变量说明**

**callback**

```ets
Rcp_OnHeaderReceiveCallbackFunc Rcp_OnHeaderReceiveCallback::callback
```

描述

接收到的headers的回调函数。

**usrObject**

```ets
void* Rcp_OnHeaderReceiveCallback::usrObject
```

描述

用户定义的对象，在回调函数中使用。