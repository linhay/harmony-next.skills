# native_audio_suite_base.h

#### 概述

声明音频编创相关底层数据结构。

**引用文件：** <ohaudiosuite/native_audio_suite_base.h>

**库：** libohaudiosuite.so

**系统能力：** SystemCapability.Multimedia.Audio.SuiteEngine

**起始版本：** 22

**相关模块：**[OHAudioSuite](OHAudioSuite.md)

#### 汇总

#### 结构体

名称typedef关键字描述[OH_AudioFormat](OH_AudioFormat.md)OH_AudioFormat定义音频编创的音频流信息，用于描述基本音频格式。[OH_AudioDataArray](OH_AudioDataArray.md)OH_AudioDataArray定义多路输出渲染接口的输入数据描述。当管线中存在多输出效果节点时，通过多输出渲染接口获取处理过后的音频数据。[OH_EqualizerFrequencyBandGains](OH_EqualizerFrequencyBandGains.md)OH_EqualizerFrequencyBandGains定义音频编创均衡器效果节点配置参数。[OH_AudioSuiteEngineStruct](OH_AudioSuiteEngineStruct.md)OH_AudioSuiteEngine声明音频编创引擎，用来管理音频编创管线。[OH_AudioSuitePipelineStruct](OH_AudioSuitePipelineStruct.md)OH_AudioSuitePipeline声明音频编创管线，用来管理音频编创节点。[OH_AudioNodeStruct](OH_AudioNodeStruct.md)OH_AudioNode声明音频编创节点，用于描述音频编创节点实例。[OH_AudioNodeBuilderStruct](OH_AudioNodeBuilderStruct.md)OH_AudioNodeBuilder声明音频编创节点的构造器。用于构建[OH_AudioNode](OH_AudioNodeStruct.md)，配置输入输出节点数据格式，配置输入节点回调接口。

#### 枚举

名称typedef关键字描述[OH_AudioNode_Type](#ZH-CN_TOPIC_0000002497445736__oh_audionode_type)OH_AudioNode_Type定义音频编创节点类型。[OH_AudioSuite_PipelineWorkMode](#ZH-CN_TOPIC_0000002497445736__oh_audiosuite_pipelineworkmode)OH_AudioSuite_PipelineWorkMode定义音频编创管线工作模式。[OH_AudioSuite_PipelineState](#ZH-CN_TOPIC_0000002497445736__oh_audiosuite_pipelinestate)OH_AudioSuite_PipelineState定义音频编创管线运行状态。[OH_AudioSuite_Result](#ZH-CN_TOPIC_0000002497445736__oh_audiosuite_result)OH_AudioSuite_Result音频编创错误码。[OH_Audio_SampleFormat](#ZH-CN_TOPIC_0000002497445736__oh_audio_sampleformat)OH_Audio_SampleFormat定义音频编创节点音频流的位深度。[OH_Audio_EncodingType](#ZH-CN_TOPIC_0000002497445736__oh_audio_encodingtype)OH_Audio_EncodingType定义音频流编码类型。[OH_Audio_SampleRate](#ZH-CN_TOPIC_0000002497445736__oh_audio_samplerate)OH_Audio_SampleRate定义音频采样率。[OH_SoundFieldType](#ZH-CN_TOPIC_0000002497445736__oh_soundfieldtype)OH_SoundFieldType定义音频编创声场效果节点的效果模式。[OH_EnvironmentType](#ZH-CN_TOPIC_0000002497445736__oh_environmenttype)OH_EnvironmentType定义音频编创环境效果节点的模式。[OH_VoiceBeautifierType](#ZH-CN_TOPIC_0000002497445736__oh_voicebeautifiertype)OH_VoiceBeautifierType定义音频编创美化效果节点模式。

#### 宏定义

名称描述EQUALIZER_BAND_NUM (10)

定义均衡器频带数量为10个。

**起始版本：** 22

#### 变量

名称描述const [OH_EqualizerFrequencyBandGains](OH_EqualizerFrequencyBandGains.md) OH_EQUALIZER_PARAM_DEFAULT

默认均衡器频带增益效果。

 各频带增益：{0, 0, 0, 0, 0, 0, 0, 0, 0, 0}。

**起始版本：** 22

const [OH_EqualizerFrequencyBandGains](OH_EqualizerFrequencyBandGains.md) OH_EQUALIZER_PARAM_BALLADS

均衡器节点内置民谣效果。

 各频带增益：{3, 5, 2, -4, 1, 2, -3, 1, 4, 5}。

**起始版本：** 22

const [OH_EqualizerFrequencyBandGains](OH_EqualizerFrequencyBandGains.md) OH_EQUALIZER_PARAM_CHINESE_STYLE

均衡器节点内置中国风效果。

 各频带增益：{0, 0, 2, 0, 0, 4, 4, 2, 2, 5}。

**起始版本：** 22

const [OH_EqualizerFrequencyBandGains](OH_EqualizerFrequencyBandGains.md) OH_EQUALIZER_PARAM_CLASSICAL

均衡器节点内置古典效果。

 各频带增益：{2, 3, 2, 1, 0, 0, -5, -5, -5, -6}。

**起始版本：** 22

const [OH_EqualizerFrequencyBandGains](OH_EqualizerFrequencyBandGains.md) OH_EQUALIZER_PARAM_DANCE_MUSIC

均衡器节点内置舞曲效果。

 各频带增益：{4, 3, 2, -3, 0, 0, 5, 4, 2, 0}。

**起始版本：** 22

const [OH_EqualizerFrequencyBandGains](OH_EqualizerFrequencyBandGains.md) OH_EQUALIZER_PARAM_JAZZ

均衡器节点内置爵士效果。

 各频带增益：{2, 0, 2, 3, 6, 5, -1, 3, 4, 4}。

**起始版本：** 22

const [OH_EqualizerFrequencyBandGains](OH_EqualizerFrequencyBandGains.md) OH_EQUALIZER_PARAM_POP

均衡器节点内置流行效果。

 各频带增益：{5, 2, 1, -1, -5, -5, -2, 1, 2, 4}。

**起始版本：** 22

const [OH_EqualizerFrequencyBandGains](OH_EqualizerFrequencyBandGains.md) OH_EQUALIZER_PARAM_RB

均衡器节点内置R&B效果。

 各频带增益：{1, 4, 5, 3, -2, -2, 2, 3, 5, 5}。

**起始版本：** 22

const [OH_EqualizerFrequencyBandGains](OH_EqualizerFrequencyBandGains.md) OH_EQUALIZER_PARAM_ROCK

均衡器节点内置摇滚效果。

 各频带增益：{6, 4, 4, 2, 0, 1, 3, 3, 5, 4}。

**起始版本：** 22

#### 枚举类型说明

#### OH_AudioNode_Type

```ets
enum OH_AudioNode_Type
```

**描述**

定义音频编创节点类型。

**起始版本：** 22

枚举项描述INPUT_NODE_TYPE_DEFAULT = 1输入节点，支持从应用程序获取音频数据。OUTPUT_NODE_TYPE_DEFAULT = 101输出节点，支持向应用程序提供音频数据。EFFECT_NODE_TYPE_EQUALIZER = 201

均衡器效果节点。均衡器效果节点输出的音频格式如下：

 采样率：48000Hz。

 采样格式：[OH_Audio_SampleFormat](native_audio_suite_base.h.md#ZH-CN_TOPIC_0000002497445736__oh_audio_sampleformat).AUDIO_SAMPLE_S16LE。

 声道数：2。

EFFECT_NODE_TYPE_NOISE_REDUCTION = 202

降噪效果节点。降噪效果节点输出的音频格式如下：

 采样率：16000Hz。

 采样格式：[OH_Audio_SampleFormat](native_audio_suite_base.h.md#ZH-CN_TOPIC_0000002497445736__oh_audio_sampleformat).AUDIO_SAMPLE_S16LE。

 声道数：1。

EFFECT_NODE_TYPE_SOUND_FIELD = 203

声场效果节点。声场效果节点支持的声场类型：[OH_SoundFieldType](native_audio_suite_base.h.md#ZH-CN_TOPIC_0000002497445736__oh_soundfieldtype)。

 声场效果节点输出的音频格式如下：

 采样率：48000Hz。

 采样格式：[OH_Audio_SampleFormat](native_audio_suite_base.h.md#ZH-CN_TOPIC_0000002497445736__oh_audio_sampleformat).AUDIO_SAMPLE_S16LE。

 声道数：2。

EFFECT_MULTII_OUTPUT_NODE_TYPE_AUDIO_SEPARATION = 204

音源分离效果节点。音源分离效果节点只能连接输出节点。

 音源分离效果节点输出的音频格式如下：

 采样率：48000Hz。

 采样格式：[OH_Audio_SampleFormat](native_audio_suite_base.h.md#ZH-CN_TOPIC_0000002497445736__oh_audio_sampleformat).AUDIO_SAMPLE_F32LE。

 声道数：4（前2个声道用于人声，后2个声道用于伴奏）。

EFFECT_NODE_TYPE_VOICE_BEAUTIFIER = 205

声音美化效果节点。声音美化效果节点支持的声音美化类型：[OH_VoiceBeautifierType](native_audio_suite_base.h.md#ZH-CN_TOPIC_0000002497445736__oh_voicebeautifiertype)。

 声音美化效果节点输出的音频格式如下：

 采样率：48000Hz。

 采样格式：[OH_Audio_SampleFormat](native_audio_suite_base.h.md#ZH-CN_TOPIC_0000002497445736__oh_audio_sampleformat).AUDIO_SAMPLE_S16LE。

 声道数：2。

EFFECT_NODE_TYPE_ENVIRONMENT_EFFECT = 206

环境效果节点。环境效果节点输出的音频格式如下：

 采样率：48000Hz。

 采样格式：[OH_Audio_SampleFormat](native_audio_suite_base.h.md#ZH-CN_TOPIC_0000002497445736__oh_audio_sampleformat).AUDIO_SAMPLE_S16LE。

 声道数：2。

EFFECT_NODE_TYPE_AUDIO_MIXER = 207

混音效果节点。混音效果节点输出的音频格式如下：

 采样率：[OH_Audio_SampleRate](native_audio_suite_base.h.md#ZH-CN_TOPIC_0000002497445736__oh_audio_samplerate)。

 采样格式：[OH_Audio_SampleFormat](native_audio_suite_base.h.md#ZH-CN_TOPIC_0000002497445736__oh_audio_sampleformat).AUDIO_SAMPLE_F32LE。

 声道数：2。

#### OH_AudioSuite_PipelineWorkMode

```ets
enum OH_AudioSuite_PipelineWorkMode
```

**描述**

定义音频编创管线工作模式。

**起始版本：** 22

枚举项描述AUDIOSUITE_PIPELINE_EDIT_MODE = 1编辑模式，管线处于该工作模式下可创建多种效果节点进行音频处理。AUDIOSUITE_PIPELINE_REALTIME_MODE = 2

实时渲染模式，即在音频处理过程中实时播放已处理的音频。

 实时渲染模式下，管线仅支持均衡器效果处理。

#### OH_AudioSuite_PipelineState

```ets
enum OH_AudioSuite_PipelineState
```

**描述**

定义音频编创管线运行状态。

**起始版本：** 22

枚举项描述AUDIOSUITE_PIPELINE_STOPPED = 1管线处于停止状态。AUDIOSUITE_PIPELINE_RUNNING = 2管线处于运行状态。

#### OH_AudioSuite_Result

```ets
enum OH_AudioSuite_Result
```

**描述**

音频编创错误码。

**起始版本：** 22

枚举项描述AUDIOSUITE_SUCCESS = 0调用成功。AUDIOSUITE_ERROR_INVALID_PARAM = 1输入参数无效。AUDIOSUITE_ERROR_INVALID_STATE = 2非法状态。AUDIOSUITE_ERROR_SYSTEM = 3系统通用错误。AUDIOSUITE_ERROR_UNSUPPORTED_FORMAT = 4不支持的音频格式，如不支持的编码类型、采样格式等。AUDIOSUITE_ERROR_ENGINE_NOT_EXIST = 5引擎不存在。AUDIOSUITE_ERROR_PIPELINE_NOT_EXIST = 6管线不存在。AUDIOSUITE_ERROR_NODE_NOT_EXIST = 7节点不存在。AUDIOSUITE_ERROR_UNSUPPORTED_CONNECT = 8节点之间不支持连接。AUDIOSUITE_ERROR_UNSUPPORTED_OPERATION = 9不支持的操作。例如，效果节点不支持设置音频格式。AUDIOSUITE_ERROR_CREATED_EXCEED_SYSTEM_LIMITS = 10

创建管线或者节点超过系统最大数量限制。具体情况如下：

 引擎最多支持创建10条管线（其中，实时渲染管线最多创建1条）。每一个管线中，输入节点不超过5个，输出节点不超过1个，混音节点不超过3个，音源分离节点不超过1个，其余效果节点不超过5个。

AUDIOSUITE_ERROR_REQUIRED_PARAMETERS_MISSING = 11参数缺少必要参数。例如，输入节点未设置回调函数、输出节点未设置音频格式。AUDIOSUITE_ERROR_TIMEOUT = 12操作超时。AUDIOSUITE_ERROR_MEMORY_ALLOC_FAILED = 13内存申请失败。

#### OH_Audio_SampleFormat

```ets
enum OH_Audio_SampleFormat
```

**描述**

定义音频编创节点音频流的位深度。

**起始版本：** 22

枚举项描述AUDIO_SAMPLE_U8 = 0Unsigned 8位。AUDIO_SAMPLE_S16LE = 1Short 16位小端。AUDIO_SAMPLE_S24LE = 2Short 24位小端。AUDIO_SAMPLE_S32LE = 3Short 32位小端。AUDIO_SAMPLE_F32LE = 4Float 32位小端。

#### OH_Audio_EncodingType

```ets
enum OH_Audio_EncodingType
```

**描述**

定义音频流编码类型。

**起始版本：** 22

枚举项描述AUDIO_ENCODING_TYPE_RAW = 0PCM编码。

#### OH_Audio_SampleRate

```ets
enum OH_Audio_SampleRate
```

**描述**

定义音频采样率。

**起始版本：** 22

枚举项描述SAMPLE_RATE_8000 = 8000采样率8kHz。SAMPLE_RATE_11025 = 11025采样率11.025kHz。SAMPLE_RATE_12000 = 12000采样率12kHz。SAMPLE_RATE_16000 = 16000采样率16kHz。SAMPLE_RATE_22050 = 22050采样率22.05kHz。SAMPLE_RATE_24000 = 24000采样率24kHz。SAMPLE_RATE_32000 = 32000采样率32kHz。SAMPLE_RATE_44100 = 44100采样率44.1kHz。SAMPLE_RATE_48000 = 48000采样率48kHz。SAMPLE_RATE_64000 = 64000采样率64kHz。SAMPLE_RATE_88200 = 88200采样率88.2kHz。SAMPLE_RATE_96000 = 96000采样率96kHz。SAMPLE_RATE_176400 = 176400采样率176.4kHz。SAMPLE_RATE_192000 = 192000采样率192kHz。

#### OH_SoundFieldType

```ets
enum OH_SoundFieldType
```

**描述**

定义音频编创声场效果节点的效果模式。

**起始版本：** 22

枚举项描述SOUND_FIELD_FRONT_FACING = 1前置声场效果。SOUND_FIELD_GRAND = 2宏大声场效果。SOUND_FIELD_NEAR = 3聆听声场效果。SOUND_FIELD_WIDE = 4宽广声场效果。

#### OH_EnvironmentType

```ets
enum OH_EnvironmentType
```

**描述**

定义音频编创环境效果节点的模式。

**起始版本：** 22

枚举项描述ENVIRONMENT_TYPE_BROADCAST = 1环境节点效果为广播。ENVIRONMENT_TYPE_EARPIECE = 2环境节点效果为电话听筒。ENVIRONMENT_TYPE_UNDERWATER = 3环境节点效果为水下。ENVIRONMENT_TYPE_GRAMOPHONE = 4环境节点效果为留声机。

#### OH_VoiceBeautifierType

```ets
enum OH_VoiceBeautifierType
```

**描述**

定义音频编创美化效果节点模式。

**起始版本：** 22

枚举项描述VOICE_BEAUTIFIER_TYPE_CLEAR = 1声音美化节点效果为清澈。VOICE_BEAUTIFIER_TYPE_THEATRE = 2声音美化节点效果为剧场。VOICE_BEAUTIFIER_TYPE_CD = 3声音美化节点效果为CD。VOICE_BEAUTIFIER_TYPE_RECORDING_STUDIO = 4声音美化节点效果为录音棚。