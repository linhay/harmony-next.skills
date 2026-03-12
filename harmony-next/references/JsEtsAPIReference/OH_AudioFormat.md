# OH_AudioFormat

```ets
typedef struct {...} OH_AudioFormat
```

#### 概述

定义音频编创的音频流信息，用于描述基本音频格式。

**起始版本：** 22

**相关模块：**[OHAudioSuite](OHAudioSuite.md)

**所在头文件：**[native_audio_suite_base.h](native_audio_suite_base.h.md)

#### 汇总

#### 成员变量

名称描述[OH_Audio_SampleRate](native_audio_suite_base.h.md#ZH-CN_TOPIC_0000002497445736__oh_audio_samplerate) samplingRate音频流采样率。OH_AudioChannelLayout channelLayout音频流声道布局，当前只支持CH_LAYOUT_MONO 和 CH_LAYOUT_STEREO。uint32_t channelCount音频流声道个数，当前只支持1声道和2声道。[OH_Audio_EncodingType](native_audio_suite_base.h.md#ZH-CN_TOPIC_0000002497445736__oh_audio_encodingtype) encodingType音频流编码类型。[OH_Audio_SampleFormat](native_audio_suite_base.h.md#ZH-CN_TOPIC_0000002497445736__oh_audio_sampleformat) sampleFormat音频流采样格式。