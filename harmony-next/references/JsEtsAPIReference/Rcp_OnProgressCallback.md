# Rcp_OnProgressCallback

#### 概述

收发时回调配置，在[Rcp_EventsHandler](Rcp_EventsHandler.md)中配置。

**起始版本：** 5.0.0(12)

**相关模块：**[RemoteCommunication](RemoteCommunication.md)

#### 汇总

#### 成员变量

名称

描述

[Rcp_OnProgressCallbackFunc](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__gaaf74ce6d5578d28829955208318d3fbe)[callback](Rcp_OnProgressCallback.md#ZH-CN_TOPIC_0000002317126053__a899177e3d91f73c817ccdb2edafbcd8f)

收发过程中的回调函数。

void * [usrObject](Rcp_OnProgressCallback.md#ZH-CN_TOPIC_0000002317126053__a4ad524ee058227acd02fdc1beebde386)

用户定义的对象，在回调函数中使用。

#### 结构体成员变量说明

#### callback

```ets
[Rcp_OnProgressCallbackFunc](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__gaaf74ce6d5578d28829955208318d3fbe) Rcp_OnProgressCallback::callback
```

**描述**

收发过程中的回调函数。

#### usrObject

```ets
void* Rcp_OnProgressCallback::usrObject
```

**描述**

用户定义的对象，在回调函数中使用。