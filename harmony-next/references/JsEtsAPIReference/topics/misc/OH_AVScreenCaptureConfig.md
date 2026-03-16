# OH_AVScreenCaptureConfig

```ets
typedef struct OH_AVScreenCaptureConfig {...} OH_AVScreenCaptureConfig
```

#### 概述

屏幕录制配置参数。

**起始版本：** 10

**相关模块：**[AVScreenCapture](AVScreenCapture.md)

**所在头文件：**[native_avscreen_capture_base.h](../../capi/headers/native_avscreen_capture_base.h.md)

#### 汇总

#### 成员变量

名称描述[OH_CaptureMode](../../capi/headers/native_avscreen_capture_base.h.md#ZH-CN_TOPIC_0000002497605918__oh_capturemode) captureMode屏幕录制的模式。[OH_DataType](../../capi/headers/native_avscreen_capture_base.h.md#ZH-CN_TOPIC_0000002497605918__oh_datatype) dataType屏幕录制流的数据格式。[OH_AudioInfo](../media/OH_AudioInfo.md) audioInfo音频录制参数。[OH_VideoInfo](../media/OH_VideoInfo.md) videoInfo视频录制参数。[OH_RecorderInfo](../payment/OH_RecorderInfo.md) recorderInfo录制文件参数，当数据格式为OH_CAPTURE_FILE时必须设置。