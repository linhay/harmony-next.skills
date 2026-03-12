# MediaKeySession_Callback

```ets
typedef struct MediaKeySession_Callback {...} MediaKeySession_Callback
```

#### 概述

MediaKeySession_Callback结构体，用于监听密钥过期、密钥更改等事件，不返回媒体密钥会话实例，适用于单媒体密钥会话解密场景。

**起始版本：** 11

**相关模块：**[Drm](Drm.md)

**所在头文件：**[native_mediakeysession.h](native_mediakeysession.h.md)

#### 汇总

#### 成员变量

名称描述[MediaKeySession_EventCallback](native_mediakeysession.h.md#ZH-CN_TOPIC_0000002497445850__mediakeysession_eventcallback) eventCallback正常事件回调，如密钥过期等。[MediaKeySession_KeyChangeCallback](native_mediakeysession.h.md#ZH-CN_TOPIC_0000002497445850__mediakeysession_keychangecallback) keyChangeCallback密钥更改事件的密钥更改回调。