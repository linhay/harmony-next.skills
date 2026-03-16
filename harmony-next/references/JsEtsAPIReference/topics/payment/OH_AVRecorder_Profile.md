# OH_AVRecorder_Profile

```ets
typedef struct OH_AVRecorder_Profile {...} OH_AVRecorder_Profile
```

#### 概述

定义音视频录制的详细参数。

通过参数设置可以选择只录制音频或只录制视频：

1. 当 audioBitrate 或 audioChannels 为 0 时，不录制音频。
1. 当 videoFrameWidth 或 videoFrameHeight 为 0 时，不录制视频。

各参数的范围请参见[AVRecorderProfile](../../types/interfaces/Interfaces (其他).md#ZH-CN_TOPIC_0000002497605902__avrecorderprofile9)。

**起始版本：** 18

**相关模块：**[AVRecorder](AVRecorder.md)

**所在头文件：**[avrecorder_base.h](../../capi/headers/avrecorder_base.h.md)

#### 汇总

#### 成员变量

名称描述int32_t audioBitrate音频比特率。int32_t audioChannels音频通道数。[OH_AVRecorder_CodecMimeType](../../capi/headers/avrecorder_base.h.md#ZH-CN_TOPIC_0000002497605916__oh_avrecorder_codecmimetype) audioCodec音频编码格式。int32_t audioSampleRate音频采样率。[OH_AVRecorder_ContainerFormatType](../../capi/headers/avrecorder_base.h.md#ZH-CN_TOPIC_0000002497605916__oh_avrecorder_containerformattype) fileFormat输出文件格式。int32_t videoBitrate视频比特率。[OH_AVRecorder_CodecMimeType](../../capi/headers/avrecorder_base.h.md#ZH-CN_TOPIC_0000002497605916__oh_avrecorder_codecmimetype) videoCodec视频编码格式。int32_t videoFrameWidth视频宽度。int32_t videoFrameHeight视频高度。int32_t videoFrameRate视频帧率。bool isHdr

是否录制HDR视频。

true表示录制HDR视频，false表示不录制HDR视频。

默认是false。

bool enableTemporalScale

是否支持时域分层编码功能。

true表示编码输出的码流中部分帧可以支持跳过不编码，false表示编码输出的码流中所有帧不支持跳过不编码，详情请参考[时域可分层视频编码](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/video-encoding-temporal-scalability)。

默认是false。