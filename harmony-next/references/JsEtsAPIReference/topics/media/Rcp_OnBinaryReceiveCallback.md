# Rcp_OnBinaryReceiveCallback

#### 概述

响应的二进制数据接收回调函数。可以通过[HMS_Rcp_SetRequestOnBinaryDataRecvCallback](../misc/RemoteCommunication.md#section207321113884)为请求设置相应回调函数。

**起始版本：** 5.0.1(13)

**相关模块：**[RemoteCommunication](../misc/RemoteCommunication.md)

#### 汇总

#### 成员变量

名称

描述

[Rcp_OnBinaryReceiveCallbackFunc](../misc/RemoteCommunication.md#section1476912410533)[callback](#ZH-CN_TOPIC_0000002282549724__a3c40fdbb12e9ace486f03ca31df05ea5)

请求过程中接收二进制数据的回调函数。

void *[usrObject](#ZH-CN_TOPIC_0000002282549724__ab2e8cda5e0a617a6911360f28b31585a)

用户定义的对象，在回调函数中使用。

#### 结构体成员变量说明

#### callback

```ets
[Rcp_OnBinaryReceiveCallbackFunc](../misc/RemoteCommunication.md#section1476912410533) Rcp_OnBinaryReceiveCallback::callback
```

**描述**

二进制数据接收回调函数。

#### usrObject

```ets
void* Rcp_OnBinaryReceiveCallback::usrObject
```

**描述**

用户定义的对象，在回调函数中使用。