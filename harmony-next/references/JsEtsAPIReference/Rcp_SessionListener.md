# Rcp_SessionListener

#### 概述

关闭或取消会话事件的回调函数。

**起始版本：** 5.0.0(12)

**相关模块：**[RemoteCommunication](RemoteCommunication.md)

#### 汇总

#### 成员变量

名称

描述

void(* [onClosed](Rcp_SessionListener.md#ZH-CN_TOPIC_0000002317126057__a5ca868b964814af3121f2f6fd4b71706) )(void)

此函数在[Rcp_Session](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga4f3a7d39c18fe6fdf01c52759213ddcd)关闭时调用此函数。

void(* [onCanceled](Rcp_SessionListener.md#ZH-CN_TOPIC_0000002317126057__a3e9cf1cb6445a5b06c96ffefb547d129) )(void)

此函数在[Rcp_Session](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga4f3a7d39c18fe6fdf01c52759213ddcd)取消时调用此函数。

#### 结构体成员变量说明

#### onCanceled

```ets
void(* Rcp_SessionListener::onCanceled) (void)
```

**描述**

此函数在[Rcp_Session](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga4f3a7d39c18fe6fdf01c52759213ddcd)取消时调用此函数。

#### onClosed

```ets
void(* Rcp_SessionListener::onClosed) (void)
```

**描述**

此函数在[Rcp_Session](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga4f3a7d39c18fe6fdf01c52759213ddcd)关闭时调用此函数。