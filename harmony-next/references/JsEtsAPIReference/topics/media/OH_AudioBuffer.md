# OH_AudioBuffer

```ets
typedef struct OH_AudioBuffer {...} OH_AudioBuffer
```

#### 概述

定义了音频数据的大小、类型、时间戳等配置信息。

**起始版本：** 10

**相关模块：**[AVScreenCapture](../misc/AVScreenCapture.md)

**所在头文件：**[native_avscreen_capture_base.h](../../capi/headers/native_avscreen_capture_base.h.md)

#### 汇总

#### 成员变量

名称描述uint8_t* buf音频buffer内存。int32_t size音频buffer内存大小。int64_t timestamp音频buffer时间戳。[OH_AudioCaptureSourceType](../../capi/headers/native_avscreen_capture_base.h.md#ZH-CN_TOPIC_0000002497605918__oh_audiocapturesourcetype) type音频录制源类型。