# Rcp_OnHeaderReceiveCallback

#### 概述

[Rcp_EventsHandler](Rcp_EventsHandler.md)中配置的接收到的header的回调配置。

**起始版本：** 5.0.0(12)

**相关模块：**[RemoteCommunication](RemoteCommunication.md)

#### 汇总

#### 成员变量

名称

描述

[Rcp_OnHeaderReceiveCallbackFunc](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__gae90a801a6c386c246e5005eadfe7da0a)[callback](Rcp_OnHeaderReceiveCallback.md#ZH-CN_TOPIC_0000002317039117__ad76e89185d94287ec3ed93d862748b41)

接收到的headers的回调函数。

void * [usrObject](Rcp_OnHeaderReceiveCallback.md#ZH-CN_TOPIC_0000002317039117__a0255dccff52be488b78cba31fb43bd30)

用户定义的对象，在回调函数中使用。

#### 结构体成员变量说明

#### callback

```ets
[Rcp_OnHeaderReceiveCallbackFunc](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__gae90a801a6c386c246e5005eadfe7da0a) Rcp_OnHeaderReceiveCallback::callback
```

**描述**

接收到的headers的回调函数。

#### usrObject

```ets
void* Rcp_OnHeaderReceiveCallback::usrObject
```

**描述**

用户定义的对象，在回调函数中使用。