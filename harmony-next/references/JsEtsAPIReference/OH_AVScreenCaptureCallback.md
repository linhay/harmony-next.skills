# OH_AVScreenCaptureCallback

```ets
typedef struct OH_AVScreenCaptureCallback {...} OH_AVScreenCaptureCallback
```

#### 概述

OH_AVScreenCapture中所有异步回调函数指针的集合。将该结构体的实例注册到OH_AVScreenCapture实例中，并处理回调上报的信息，以保证OH_AVScreenCapture的正常运行。

从API version 12开始，推荐使用接口[OH_AVScreenCapture_OnError](native_avscreen_capture_base.h.md#ZH-CN_TOPIC_0000002497605918__oh_avscreencapture_onerror)、[OH_AVScreenCapture_OnBufferAvailable](native_avscreen_capture_base.h.md#ZH-CN_TOPIC_0000002497605918__oh_avscreencapture_onbufferavailable)替代。

**起始版本：** 10

**相关模块：**[AVScreenCapture](AVScreenCapture.md)

**所在头文件：**[native_avscreen_capture_base.h](native_avscreen_capture_base.h.md)

#### 汇总

#### 成员变量

名称描述[OH_AVScreenCaptureOnError](native_avscreen_capture_base.h.md#ZH-CN_TOPIC_0000002497605918__oh_avscreencaptureonerror) onError

监控录屏调用操作错误。

从API version 12开始，推荐使用接口[OH_AVScreenCapture_OnError](native_avscreen_capture_base.h.md#ZH-CN_TOPIC_0000002497605918__oh_avscreencapture_onerror)替代。

[OH_AVScreenCaptureOnAudioBufferAvailable](native_avscreen_capture_base.h.md#ZH-CN_TOPIC_0000002497605918__oh_avscreencaptureonaudiobufferavailable) onAudioBufferAvailable

监控音频码流是否有数据产生。

从API version 12开始，推荐使用接口[OH_AVScreenCapture_OnBufferAvailable](native_avscreen_capture_base.h.md#ZH-CN_TOPIC_0000002497605918__oh_avscreencapture_onbufferavailable)替代。

[OH_AVScreenCaptureOnVideoBufferAvailable](native_avscreen_capture_base.h.md#ZH-CN_TOPIC_0000002497605918__oh_avscreencaptureonvideobufferavailable) onVideoBufferAvailable

监控视频码流是否有数据产生。

从API version 12开始，推荐使用接口[OH_AVScreenCapture_OnBufferAvailable](native_avscreen_capture_base.h.md#ZH-CN_TOPIC_0000002497605918__oh_avscreencapture_onbufferavailable)替代。