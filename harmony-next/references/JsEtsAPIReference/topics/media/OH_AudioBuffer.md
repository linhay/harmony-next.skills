# OH_AudioBuffer

```ets
typedef struct OH_AudioBuffer {...} OH_AudioBuffer
```

#### 概述

定义了音频数据的大小、类型、时间戳等配置信息。

**起始版本：** 10

相关模块： [AVScreenCapture](AVScreenCapture.md)

所在头文件： [native_avscreen_capture_base.h](native_avscreen_capture_base.h.md)

#### 汇总

#### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint8_t* buf | 音频buffer内存。 |
| int32_t size | 音频buffer内存大小。 |
| int64_t timestamp | 音频buffer时间戳。 |
| [OH_AudioCaptureSourceType](native_avscreen_capture_base.h.md#ZH-CN_TOPIC_0000002497605918__oh_audiocapturesourcetype) type | 音频录制源类型。 |
