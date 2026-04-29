# AVSession_PlaybackPosition

```ets
typedef struct AVSession_PlaybackPosition {...} AVSession_PlaybackPosition
```

**概述**

媒体播放位置的相关属性。

起始版本： 13

相关模块： [OHAVSession](OHAVSession.md)

所在头文件： [native_avplaybackstate.h](native_avplaybackstate.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| int64_t elapsedTime | 已用时间，单位毫秒（ms）。 |
| int64_t updateTime | 更新时间，单位毫秒（ms）。 |