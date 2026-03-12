# Rcp_OnDataReceiveCallback

#### 概述

接收到数据时回调。[Rcp_EventsHandler](Rcp_EventsHandler.md)中的配置。

**起始版本：** 5.0.0(12)

**相关模块：**[RemoteCommunication](RemoteCommunication.md)

#### 汇总

#### 成员变量

名称

描述

[Rcp_OnDataReceiveCallbackFunc](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__gadc4e28c213ddc694e3c0ec76296ef5c0)[callback](Rcp_OnDataReceiveCallback.md#ZH-CN_TOPIC_0000002282446462__a3c40fdbb12e9ace486f03ca31df05ea5)

接收数据回调函数。

void * [usrObject](Rcp_OnDataReceiveCallback.md#ZH-CN_TOPIC_0000002282446462__ab2e8cda5e0a617a6911360f28b31585a)

用户定义的对象，在回调函数中使用。

#### 结构体成员变量说明

#### callback

```ets
[Rcp_OnDataReceiveCallbackFunc](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__gadc4e28c213ddc694e3c0ec76296ef5c0) Rcp_OnDataReceiveCallback::callback
```

**描述**

接收数据回调函数。

#### usrObject

```ets
void* Rcp_OnDataReceiveCallback::usrObject
```

**描述**

用户定义的对象，在回调函数中使用。