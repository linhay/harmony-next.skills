# Rcp_SessionListener

**概述**

关闭或取消会话事件的回调函数。

起始版本： 5.0.0(12)

相关模块： [RemoteCommunication](RemoteCommunication.md)

所在头文件： [rcp.h](rcp.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| void(* onClosed )(void) | 此函数在Rcp_Session关闭时调用此函数。 |
| void(* onCanceled )(void) | 此函数在Rcp_Session取消时调用此函数。 |

**结构体成员变量说明**

**onCanceled**

```ets
void(* Rcp_SessionListener::onCanceled) (void)
```

描述

此函数在[Rcp_Session](RemoteCommunication.md#ZH-CN_TOPIC_0000002522081538__rcp_session)取消时调用此函数。

**onClosed**

```ets
void(* Rcp_SessionListener::onClosed) (void)
```

描述

此函数在[Rcp_Session](RemoteCommunication.md#ZH-CN_TOPIC_0000002522081538__rcp_session)关闭时调用此函数。