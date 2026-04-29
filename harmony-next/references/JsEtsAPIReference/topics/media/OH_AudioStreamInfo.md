# OH_AudioStreamInfo

```ets
typedef struct OH_AudioStreamInfo {...} OH_AudioStreamInfo
```

#### 概述

定义音频流信息，用于描述基本音频格式。

**起始版本：** 19

**相关模块：**[OHAudio](OHAudio.md)

所在头文件： [native_audiostream_base.h](native_audiostream_base.h.md)

#### 汇总

#### 成员变量

| 名称 | 描述 |
| --- | --- |
| int32_t samplingRate | 音频流采样率。 |
| [OH_AudioChannelLayout](native_audio_channel_layout.h.md#ZH-CN_TOPIC_0000002497445760__oh_audiochannellayout) channelLayout | 音频流声道布局。 |
| [OH_AudioStream_EncodingType](native_audiostream_base.h.md#ZH-CN_TOPIC_0000002529445679__oh_audiostream_encodingtype) encodingType | 音频流编码类型。 |
| [OH_AudioStream_SampleFormat](native_audiostream_base.h.md#ZH-CN_TOPIC_0000002529445679__oh_audiostream_sampleformat) sampleFormat | 音频流采样格式。 |
