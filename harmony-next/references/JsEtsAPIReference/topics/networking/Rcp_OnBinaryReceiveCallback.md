# Rcp_OnBinaryReceiveCallback

**概述**

响应的二进制数据接收回调函数。可以通过[HMS_Rcp_SetRequestOnBinaryDataRecvCallback](RemoteCommunication.md#ZH-CN_TOPIC_0000002522081538__hms_rcp_setrequestonbinarydatarecvcallback)为请求设置相应回调函数。

起始版本： 5.0.1(13)

相关模块： [RemoteCommunication](RemoteCommunication.md)

所在头文件： [rcp.h](rcp.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| Rcp_OnBinaryReceiveCallbackFunccallback | 请求过程中接收二进制数据的回调函数。 |
| void *usrObject | 用户定义的对象，在回调函数中使用。 |

**结构体成员变量说明**

**callback**

```ets
Rcp_OnBinaryReceiveCallbackFunc Rcp_OnBinaryReceiveCallback::callback
```

描述

二进制数据接收回调函数。

**usrObject**

```ets
void* Rcp_OnBinaryReceiveCallback::usrObject
```

描述

用户定义的对象，在回调函数中使用。