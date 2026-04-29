# native_audio_suite_base.h

**概述**

声明音频编创相关底层数据结构。

引用文件： <ohaudiosuite/native_audio_suite_base.h>

库： libohaudiosuite.so

系统能力： SystemCapability.Multimedia.Audio.SuiteEngine

起始版本： 22

相关模块： [OHAudioSuite](OHAudioSuite.md)

**汇总**

**结构体**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| OH_AudioFormat | OH_AudioFormat | 定义音频编创的音频流信息，用于描述基本音频格式。 |
| OH_AudioDataArray | OH_AudioDataArray | 定义多路输出渲染接口的输入数据描述。当管线中存在多输出效果节点时，通过多输出渲染接口获取处理过后的音频数据。 |
| OH_EqualizerFrequencyBandGains | OH_EqualizerFrequencyBandGains | 定义音频编创均衡器效果节点配置参数。 |
| OH_AudioSuite_SpaceRenderPositionParams | OH_AudioSuite_SpaceRenderPositionParams | 定义3D空间渲染效果节点固定摆位模式的配置参数。左手坐标系：伸出左手，用拇指和食指形成一个“L”形。  拇指指向右侧，食指向上，其余手指指向前。  此时形成了一个3D的左手坐标系。在这个坐标系中，拇指、食指  和其他手指分别代表x轴、y轴和z轴的正方向。 |
| OH_AudioSuite_SpaceRenderRotationParams | OH_AudioSuite_SpaceRenderRotationParams | 定义空间渲染效果节点旋转模式配置参数。 |
| OH_AudioSuite_SpaceRenderExtensionParams | OH_AudioSuite_SpaceRenderExtensionParams | 定义空间渲染效果节点扩展模式配置参数。 |
| OH_AudioSuite_PureVoiceChangeOption | OH_AudioSuite_PureVoiceChangeOption | 定义音频编创传统变声选项。 |
| OH_AudioSuiteEngineStruct | OH_AudioSuiteEngine | 声明音频编创引擎，用来管理音频编创管线。 |
| OH_AudioSuitePipelineStruct | OH_AudioSuitePipeline | 声明音频编创管线，用来管理音频编创节点。 |
| OH_AudioNodeStruct | OH_AudioNode | 声明音频编创节点，用于描述音频编创节点实例。 |
| OH_AudioNodeBuilderStruct | OH_AudioNodeBuilder | 声明音频编创节点的构造器。用于构建OH_AudioNode，配置输入输出节点数据格式，配置输入节点回调接口。 |

**枚举**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| OH_AudioNode_Type | OH_AudioNode_Type | 定义音频编创节点类型。 |
| OH_AudioSuite_PipelineWorkMode | OH_AudioSuite_PipelineWorkMode | 定义音频编创管线工作模式。 |
| OH_AudioSuite_PipelineState | OH_AudioSuite_PipelineState | 定义音频编创管线运行状态。 |
| OH_AudioSuite_Result | OH_AudioSuite_Result | 音频编创错误码。 |
| OH_Audio_SampleFormat | OH_Audio_SampleFormat | 定义音频编创节点音频流的位深度。 |
| OH_Audio_EncodingType | OH_Audio_EncodingType | 定义音频流编码类型。 |
| OH_Audio_SampleRate | OH_Audio_SampleRate | 定义音频采样率。 |
| OH_SoundFieldType | OH_SoundFieldType | 定义音频编创声场效果节点的效果模式。 |
| OH_EnvironmentType | OH_EnvironmentType | 定义音频编创环境效果节点的模式。 |
| OH_VoiceBeautifierType | OH_VoiceBeautifierType | 定义音频编创美化效果节点模式。 |
| OH_AudioSuite_SurroundDirection | OH_AudioSuite_SurroundDirection | 定义空间渲染效果节点旋转模式环绕方向。 |
| OH_AudioSuite_PureVoiceChangeGenderOption | OH_AudioSuite_PureVoiceChangeGenderOption | 定义音频编创传统变声效果节点的性别。 |
| OH_AudioSuite_PureVoiceChangeType | OH_AudioSuite_PureVoiceChangeType | 定义音频编创传统变声效果节点的变声类型。 |
| OH_AudioSuite_GeneralVoiceChangeType | OH_AudioSuite_GeneralVoiceChangeType | 定义音频编创通用变声的节点类型。 |

**宏定义**

| 名称 | 描述 |
| --- | --- |
| EQUALIZER_BAND_NUM (10) | 定义均衡器频带数量为10个。 起始版本： 22 |
| OH_PURE_VOICE_DEFAULT_PITCH (0.0f) | 使用系统推荐的音调。用于OH_AudioSuite_PureVoiceChangeOption。 起始版本： 23 |

**变量**

| 名称 | 描述 |
| --- | --- |
| const OH_EqualizerFrequencyBandGains OH_EQUALIZER_PARAM_DEFAULT | 默认均衡器频带增益效果。  各频带增益：{0, 0, 0, 0, 0, 0, 0, 0, 0, 0}。 起始版本： 22 |
| const OH_EqualizerFrequencyBandGains OH_EQUALIZER_PARAM_BALLADS | 均衡器节点内置民谣效果。  各频带增益：{3, 5, 2, -4, 1, 2, -3, 1, 4, 5}。 起始版本： 22 |
| const OH_EqualizerFrequencyBandGains OH_EQUALIZER_PARAM_CHINESE_STYLE | 均衡器节点内置中国风效果。  各频带增益：{0, 0, 2, 0, 0, 4, 4, 2, 2, 5}。 起始版本： 22 |
| const OH_EqualizerFrequencyBandGains OH_EQUALIZER_PARAM_CLASSICAL | 均衡器节点内置古典效果。  各频带增益：{2, 3, 2, 1, 0, 0, -5, -5, -5, -6}。 起始版本： 22 |
| const OH_EqualizerFrequencyBandGains OH_EQUALIZER_PARAM_DANCE_MUSIC | 均衡器节点内置舞曲效果。  各频带增益：{4, 3, 2, -3, 0, 0, 5, 4, 2, 0}。 起始版本： 22 |
| const OH_EqualizerFrequencyBandGains OH_EQUALIZER_PARAM_JAZZ | 均衡器节点内置爵士效果。  各频带增益：{2, 0, 2, 3, 6, 5, -1, 3, 4, 4}。 起始版本： 22 |
| const OH_EqualizerFrequencyBandGains OH_EQUALIZER_PARAM_POP | 均衡器节点内置流行效果。  各频带增益：{5, 2, 1, -1, -5, -5, -2, 1, 2, 4}。 起始版本： 22 |
| const OH_EqualizerFrequencyBandGains OH_EQUALIZER_PARAM_RB | 均衡器节点内置R&B效果。  各频带增益：{1, 4, 5, 3, -2, -2, 2, 3, 5, 5}。 起始版本： 22 |
| const OH_EqualizerFrequencyBandGains OH_EQUALIZER_PARAM_ROCK | 均衡器节点内置摇滚效果。  各频带增益：{6, 4, 4, 2, 0, 1, 3, 3, 5, 4}。 起始版本： 22 |

**枚举类型说明**

**OH_AudioNode_Type**

```ets
enum OH_AudioNode_Type
```

描述

定义音频编创节点类型。

起始版本： 22

| 枚举项 | 描述 |
| --- | --- |
| INPUT_NODE_TYPE_DEFAULT = 1 | 输入节点，支持从应用程序获取音频数据。 起始版本： 22 |
| OUTPUT_NODE_TYPE_DEFAULT = 101 | 输出节点，支持向应用程序提供音频数据。 起始版本： 22 |
| EFFECT_NODE_TYPE_EQUALIZER = 201 | 均衡器效果节点。均衡器效果节点输出的音频格式如下：  采样率：48000Hz。  采样格式：OH_Audio_SampleFormat.AUDIO_SAMPLE_S16LE。  声道数：2。 起始版本： 22 |
| EFFECT_NODE_TYPE_NOISE_REDUCTION = 202 | 降噪效果节点。降噪效果节点输出的音频格式如下：  采样率：16000Hz。  采样格式：OH_Audio_SampleFormat.AUDIO_SAMPLE_S16LE。  声道数：1。 起始版本： 22 |
| EFFECT_NODE_TYPE_SOUND_FIELD = 203 | 声场效果节点。声场效果节点支持的声场类型：OH_SoundFieldType。  声场效果节点输出的音频格式如下：  采样率：48000Hz。  采样格式：OH_Audio_SampleFormat.AUDIO_SAMPLE_S16LE。  声道数：2。 起始版本： 22 |
| EFFECT_MULTII_OUTPUT_NODE_TYPE_AUDIO_SEPARATION = 204 | 音源分离效果节点。音源分离效果节点只能连接输出节点。  音源分离效果节点输出的音频格式如下：  采样率：48000Hz。  采样格式：OH_Audio_SampleFormat.AUDIO_SAMPLE_F32LE。  声道数：4（前2个声道用于人声，后2个声道用于伴奏）。 起始版本： 22 |
| EFFECT_NODE_TYPE_VOICE_BEAUTIFIER = 205 | 声音美化效果节点。声音美化效果节点支持的声音美化类型：OH_VoiceBeautifierType。  声音美化效果节点输出的音频格式如下：  采样率：48000Hz。  采样格式：OH_Audio_SampleFormat.AUDIO_SAMPLE_S16LE。  声道数：2。 起始版本： 22 |
| EFFECT_NODE_TYPE_ENVIRONMENT_EFFECT = 206 | 环境效果节点。环境效果节点输出的音频格式如下：  采样率：48000Hz。  采样格式：OH_Audio_SampleFormat.AUDIO_SAMPLE_S16LE。  声道数：2。 起始版本： 22 |
| EFFECT_NODE_TYPE_AUDIO_MIXER = 207 | 混音效果节点。混音效果节点输出的音频格式如下：  采样率：OH_Audio_SampleRate。  采样格式：OH_Audio_SampleFormat.AUDIO_SAMPLE_F32LE。  声道数：2。 起始版本： 22 |
| EFFECT_NODE_TYPE_SPACE_RENDER = 208 | 空间渲染效果节点。空间渲染效果节点输出的音频格式如下：  采样率：48000Hz。  采样格式：OH_Audio_SampleFormat.AUDIO_SAMPLE_S16LE。  声道数：2。 起始版本： 23 |
| EFFECT_NODE_TYPE_PURE_VOICE_CHANGE = 209 | 传统变声效果节点。传统变声效果节点输出的音频格式如下：  采样率：16000Hz。  采样格式：OH_Audio_SampleFormat.AUDIO_SAMPLE_S16LE。  声道数：1。 起始版本： 23 |
| EFFECT_NODE_TYPE_GENERAL_VOICE_CHANGE = 210 | 通用变声效果节点。通用变声效果节点的输出音频格式如下：  采样率：48000Hz。  采样格式：OH_Audio_SampleFormat.AUDIO_SAMPLE_S16LE。  声道数：2。 起始版本： 23 |
| EFFECT_NODE_TYPE_TEMPO_PITCH = 211 | 变速变调效果节点。变速变调效果节点的输出音频格式如下：  采样率：48000Hz。  采样格式：OH_Audio_SampleFormat.AUDIO_SAMPLE_S16LE。  声道数：1。 起始版本： 23 |

**OH_AudioSuite_PipelineWorkMode**

```ets
enum OH_AudioSuite_PipelineWorkMode
```

描述

定义音频编创管线工作模式。

起始版本： 22

| 枚举项 | 描述 |
| --- | --- |
| AUDIOSUITE_PIPELINE_EDIT_MODE = 1 | 编辑模式，管线处于该工作模式下可创建多种效果节点进行音频处理。 |
| AUDIOSUITE_PIPELINE_REALTIME_MODE = 2 | 实时渲染模式，即在音频处理过程中实时播放已处理的音频。  实时渲染模式下，管线仅支持均衡器效果处理。 |

**OH_AudioSuite_PipelineState**

```ets
enum OH_AudioSuite_PipelineState
```

描述

定义音频编创管线运行状态。

起始版本： 22

| 枚举项 | 描述 |
| --- | --- |
| AUDIOSUITE_PIPELINE_STOPPED = 1 | 管线处于停止状态。 |
| AUDIOSUITE_PIPELINE_RUNNING = 2 | 管线处于运行状态。 |

**OH_AudioSuite_Result**

```ets
enum OH_AudioSuite_Result
```

描述

音频编创错误码。

起始版本： 22

| 枚举项 | 描述 |
| --- | --- |
| AUDIOSUITE_SUCCESS = 0 | 调用成功。 |
| AUDIOSUITE_ERROR_INVALID_PARAM = 1 | 输入参数无效。 |
| AUDIOSUITE_ERROR_INVALID_STATE = 2 | 非法状态。 |
| AUDIOSUITE_ERROR_SYSTEM = 3 | 系统通用错误。 |
| AUDIOSUITE_ERROR_UNSUPPORTED_FORMAT = 4 | 不支持的音频格式，如不支持的编码类型、采样格式等。 |
| AUDIOSUITE_ERROR_ENGINE_NOT_EXIST = 5 | 引擎不存在。 |
| AUDIOSUITE_ERROR_PIPELINE_NOT_EXIST = 6 | 管线不存在。 |
| AUDIOSUITE_ERROR_NODE_NOT_EXIST = 7 | 节点不存在。 |
| AUDIOSUITE_ERROR_UNSUPPORTED_CONNECT = 8 | 节点之间不支持连接。 |
| AUDIOSUITE_ERROR_UNSUPPORTED_OPERATION = 9 | 不支持的操作。例如，效果节点不支持设置音频格式。 |
| AUDIOSUITE_ERROR_CREATED_EXCEED_SYSTEM_LIMITS = 10 | 创建管线或者节点超过系统最大数量限制。具体情况如下：  引擎最多支持创建10条管线（其中，实时渲染管线最多创建1条）。  每一个管线中，输入节点不超过5个，输出节点不超过1个，混音节点不超过3个，音源分离节点不超过1个，其余效果节点不超过5个。 |
| AUDIOSUITE_ERROR_REQUIRED_PARAMETERS_MISSING = 11 | 参数缺少必要参数。例如，输入节点未设置回调函数、输出节点未设置音频格式。 |
| AUDIOSUITE_ERROR_TIMEOUT = 12 | 操作超时。 |
| AUDIOSUITE_ERROR_MEMORY_ALLOC_FAILED = 13 | 内存申请失败。 |

**OH_Audio_SampleFormat**

```ets
enum OH_Audio_SampleFormat
```

描述

定义音频编创节点音频流的位深度。

起始版本： 22

| 枚举项 | 描述 |
| --- | --- |
| AUDIO_SAMPLE_U8 = 0 | Unsigned 8位。 |
| AUDIO_SAMPLE_S16LE = 1 | Short 16位小端。 |
| AUDIO_SAMPLE_S24LE = 2 | Short 24位小端。 |
| AUDIO_SAMPLE_S32LE = 3 | Short 32位小端。 |
| AUDIO_SAMPLE_F32LE = 4 | Float 32位小端。 |

**OH_Audio_EncodingType**

```ets
enum OH_Audio_EncodingType
```

描述

定义音频流编码类型。

起始版本： 22

| 枚举项 | 描述 |
| --- | --- |
| AUDIO_ENCODING_TYPE_RAW = 0 | PCM编码。 |

**OH_Audio_SampleRate**

```ets
enum OH_Audio_SampleRate
```

描述

定义音频采样率。

起始版本： 22

| 枚举项 | 描述 |
| --- | --- |
| SAMPLE_RATE_8000 = 8000 | 采样率8kHz。 |
| SAMPLE_RATE_11025 = 11025 | 采样率11.025kHz。 |
| SAMPLE_RATE_12000 = 12000 | 采样率12kHz。 |
| SAMPLE_RATE_16000 = 16000 | 采样率16kHz。 |
| SAMPLE_RATE_22050 = 22050 | 采样率22.05kHz。 |
| SAMPLE_RATE_24000 = 24000 | 采样率24kHz。 |
| SAMPLE_RATE_32000 = 32000 | 采样率32kHz。 |
| SAMPLE_RATE_44100 = 44100 | 采样率44.1kHz。 |
| SAMPLE_RATE_48000 = 48000 | 采样率48kHz。 |
| SAMPLE_RATE_64000 = 64000 | 采样率64kHz。 |
| SAMPLE_RATE_88200 = 88200 | 采样率88.2kHz。 |
| SAMPLE_RATE_96000 = 96000 | 采样率96kHz。 |
| SAMPLE_RATE_176400 = 176400 | 采样率176.4kHz。 |
| SAMPLE_RATE_192000 = 192000 | 采样率192kHz。 |

**OH_SoundFieldType**

```ets
enum OH_SoundFieldType
```

描述

定义音频编创声场效果节点的效果模式。

起始版本： 22

| 枚举项 | 描述 |
| --- | --- |
| SOUND_FIELD_FRONT_FACING = 1 | 前置声场效果。 |
| SOUND_FIELD_GRAND = 2 | 宏大声场效果。 |
| SOUND_FIELD_NEAR = 3 | 聆听声场效果。 |
| SOUND_FIELD_WIDE = 4 | 宽广声场效果。 |

**OH_EnvironmentType**

```ets
enum OH_EnvironmentType
```

描述

定义音频编创环境效果节点的模式。

起始版本： 22

| 枚举项 | 描述 |
| --- | --- |
| ENVIRONMENT_TYPE_BROADCAST = 1 | 环境节点效果为广播。 |
| ENVIRONMENT_TYPE_EARPIECE = 2 | 环境节点效果为电话听筒。 |
| ENVIRONMENT_TYPE_UNDERWATER = 3 | 环境节点效果为水下。 |
| ENVIRONMENT_TYPE_GRAMOPHONE = 4 | 环境节点效果为留声机。 |

**OH_VoiceBeautifierType**

```ets
enum OH_VoiceBeautifierType
```

描述

定义音频编创美化效果节点模式。

起始版本： 22

| 枚举项 | 描述 |
| --- | --- |
| VOICE_BEAUTIFIER_TYPE_CLEAR = 1 | 声音美化节点效果为清澈。 |
| VOICE_BEAUTIFIER_TYPE_THEATRE = 2 | 声音美化节点效果为剧场。 |
| VOICE_BEAUTIFIER_TYPE_CD = 3 | 声音美化节点效果为CD。 |
| VOICE_BEAUTIFIER_TYPE_RECORDING_STUDIO = 4 | 声音美化节点效果为录音棚。 |

**OH_AudioSuite_SurroundDirection**

```ets
enum OH_AudioSuite_SurroundDirection
```

描述

定义空间渲染效果节点旋转模式环绕方向。

起始版本： 23

| 枚举项 | 描述 |
| --- | --- |
| SPACE_RENDER_CCW = 0 | 逆时针旋转。 |
| SPACE_RENDER_CW = 1 | 顺时针旋转。 |

**OH_AudioSuite_PureVoiceChangeGenderOption**

```ets
enum OH_AudioSuite_PureVoiceChangeGenderOption
```

描述

定义音频编创传统变声效果节点的性别。

起始版本： 23

| 枚举项 | 描述 |
| --- | --- |
| PURE_VOICE_CHANGE_FEMALE = 1 | 设置女声。 |
| PURE_VOICE_CHANGE_MALE = 2 | 设置男声。 |

**OH_AudioSuite_PureVoiceChangeType**

```ets
enum OH_AudioSuite_PureVoiceChangeType
```

描述

定义音频编创传统变声效果节点的变声类型。

起始版本： 23

| 枚举项 | 描述 |
| --- | --- |
| PURE_VOICE_CHANGE_TYPE_CARTOON = 1 | 传统变声效果节点为卡通类型。 |
| PURE_VOICE_CHANGE_TYPE_CUTE = 2 | 传统变声效果节点为萝莉类型。 |
| PURE_VOICE_CHANGE_TYPE_FEMALE = 3 | 传统变声效果节点为女声类型。 |
| PURE_VOICE_CHANGE_TYPE_MALE = 4 | 传统变声效果节点为男声类型。 |
| PURE_VOICE_CHANGE_TYPE_MONSTER = 5 | 传统变声效果节点为怪兽类型。 |
| PURE_VOICE_CHANGE_TYPE_ROBOTS = 6 | 传统变声效果节点为机器人类型。 |
| PURE_VOICE_CHANGE_TYPE_SEASONED = 7 | 传统变声效果节点为大叔类型。 |

**OH_AudioSuite_GeneralVoiceChangeType**

```ets
enum OH_AudioSuite_GeneralVoiceChangeType
```

描述

定义音频编创通用变声的节点类型。

起始版本： 23

| 枚举项 | 描述 |
| --- | --- |
| GENERAL_VOICE_CHANGE_TYPE_CUTE = 1 | 通用变声效果节点为萝莉类型。 |
| GENERAL_VOICE_CHANGE_TYPE_CYBERPUNK = 2 | 通用变声效果节点为赛博朋克类型。 |
| GENERAL_VOICE_CHANGE_TYPE_FEMALE = 3 | 通用变声效果节点为女声类型。 |
| GENERAL_VOICE_CHANGE_TYPE_MALE = 4 | 通用变声效果节点为男声类型。 |
| GENERAL_VOICE_CHANGE_TYPE_MIX = 5 | 通用变声效果节点为混响类型。 |
| GENERAL_VOICE_CHANGE_TYPE_MONSTER = 6 | 通用变声效果节点为怪兽类型。 |
| GENERAL_VOICE_CHANGE_TYPE_SEASONED = 7 | 通用变声效果节点为大叔类型。 |
| GENERAL_VOICE_CHANGE_TYPE_SYNTH = 8 | 通用变声效果节点为合成器类型。 |
| GENERAL_VOICE_CHANGE_TYPE_TRILL = 9 | 通用变声效果节点为颤音类型。 |
| GENERAL_VOICE_CHANGE_TYPE_WAR = 10 | 通用变声效果节点为战争类型。 |