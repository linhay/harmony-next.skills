# OH_MediaKeySession_Callback

```ets
typedef struct OH_MediaKeySession_Callback {...} OH_MediaKeySession_Callback
```

#### 概述

OH_MediaKeySession_Callback结构体，用于监听密钥过期、密钥更改等事件，返回媒体密钥会话实例，适用多个媒体密钥会话解密场景。

**起始版本：** 12

**相关模块：**[Drm](../misc/Drm.md)

**所在头文件：**[native_mediakeysession.h](../../capi/headers/native_mediakeysession.h.md)

#### 汇总

#### 成员变量

名称描述[OH_MediaKeySession_EventCallback](../../capi/headers/native_mediakeysession.h.md#ZH-CN_TOPIC_0000002497445850__oh_mediakeysession_eventcallback) eventCallback正常事件回调，如密钥过期等。[OH_MediaKeySession_KeyChangeCallback](../../capi/headers/native_mediakeysession.h.md#ZH-CN_TOPIC_0000002497445850__oh_mediakeysession_keychangecallback) keyChangeCallback密钥更改事件的密钥更改回调。