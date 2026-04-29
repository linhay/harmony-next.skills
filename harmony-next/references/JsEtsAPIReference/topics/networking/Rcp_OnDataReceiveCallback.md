# Rcp_OnDataReceiveCallback

**概述**

接收到数据时回调。[Rcp_EventsHandler](Rcp_EventsHandler.md)中的配置。

起始版本： 5.0.0(12)

相关模块： [RemoteCommunication](RemoteCommunication.md)

所在头文件： [rcp.h](rcp.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| Rcp_OnDataReceiveCallbackFunccallback | 接收数据回调函数。 |
| void * usrObject | 用户定义的对象，在回调函数中使用。 |

**结构体成员变量说明**

**callback**

```ets
Rcp_OnDataReceiveCallbackFunc Rcp_OnDataReceiveCallback::callback
```

描述

接收数据回调函数。

**usrObject**

```ets
void* Rcp_OnDataReceiveCallback::usrObject
```

描述

用户定义的对象，在回调函数中使用。