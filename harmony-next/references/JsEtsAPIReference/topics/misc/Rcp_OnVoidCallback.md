# Rcp_OnVoidCallback

#### 概述

在[Rcp_EventsHandler](Rcp_EventsHandler.md)中配置的数据结束或已取消事件的回调配置。

**起始版本：** 5.0.0(12)

**相关模块：**[RemoteCommunication](RemoteCommunication.md)

#### 汇总

#### 成员变量

名称

描述

[Rcp_OnVoidCallbackFunc](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga3d6a448e8f0bdcc2b4e70fa6ca00d475)[callback](Rcp_OnVoidCallback.md#ZH-CN_TOPIC_0000002317126005__a64fba630d3ca20f3baa3f2184cd4fd99)

DataEnd或Canceled事件回调函数。

void * [usrObject](Rcp_OnVoidCallback.md#ZH-CN_TOPIC_0000002317126005__ab1d887e227a21e05fb80c407396c3147)

用户定义的对象，在回调函数中使用。

#### 结构体成员变量说明

#### callback

```ets
[Rcp_OnVoidCallbackFunc](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga3d6a448e8f0bdcc2b4e70fa6ca00d475) Rcp_OnVoidCallback::callback
```

**描述**

DataEnd或Canceled事件回调函数。

#### usrObject

```ets
void* Rcp_OnVoidCallback::usrObject
```

**描述**

用户定义的对象，在回调函数中使用。