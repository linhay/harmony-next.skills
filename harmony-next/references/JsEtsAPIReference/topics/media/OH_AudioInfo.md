# OH_AudioInfo

```ets
typedef struct OH_AudioInfo {...} OH_AudioInfo
```

#### 概述

音频信息。

同时采集音频麦克风和音频内录数据时，两路音频的audioSampleRate和audioChannels采样参数需要相同。

**起始版本：** 10

**相关模块：**[AVScreenCapture](../misc/AVScreenCapture.md)

**所在头文件：**[native_avscreen_capture_base.h](../../capi/headers/native_avscreen_capture_base.h.md)

#### 汇总

#### 成员变量

名称描述[OH_AudioCaptureInfo](OH_AudioCaptureInfo.md) micCapInfo音频麦克风采样信息。[OH_AudioCaptureInfo](OH_AudioCaptureInfo.md) innerCapInfo音频内录采样信息。[OH_AudioEncInfo](OH_AudioEncInfo.md) audioEncInfo音频编码信息，原始码流时不需要设置。