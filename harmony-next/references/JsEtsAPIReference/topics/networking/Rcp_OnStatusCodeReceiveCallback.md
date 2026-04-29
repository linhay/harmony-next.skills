# Rcp_OnStatusCodeReceiveCallback

**概述**

响应的状态码接收回调函数。可以通过[HMS_Rcp_SetRequestOnStatusCodeReceiveCallback](RemoteCommunication.md#ZH-CN_TOPIC_0000002522081538__hms_rcp_setrequestonstatuscodereceivecallback)为请求设置相应回调函数。

起始版本： 6.0.1(21)

相关模块： [RemoteCommunication](RemoteCommunication.md)

所在头文件： [rcp.h](rcp.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| Rcp_OnStatusCodeReceiveCallbackFunc | 请求过程中接收响应状态码的回调函数。 |
| void *usrObject | 用户定义的对象，在回调函数中使用。 |

**结构体成员变量说明**

**callback**

```ets
Rcp_OnStatusCodeReceiveCallbackFunc Rcp_OnStatusCodeReceiveCallback::callback
```

描述

响应状态码接收回调函数。

**usrObject**

```ets
void* Rcp_OnStatusCodeReceiveCallback::usrObject
```

描述

用户定义的对象，在回调函数中使用。