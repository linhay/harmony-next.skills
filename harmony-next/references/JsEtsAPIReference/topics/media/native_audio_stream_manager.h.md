# native_audio_stream_manager.h

**概述**

声明音频流管理器相关的接口。

 该文件接口用于创建AudioStreamManager以及音频流设置和管理。

引用文件： <ohaudio/native_audio_stream_manager.h>

库： libohaudio.so

系统能力： SystemCapability.Multimedia.Audio.Core

起始版本： 19

相关模块： [OHAudio](OHAudio.md)

**汇总**

**结构体**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| OH_AudioStreamManager | OH_AudioStreamManager | 声明音频流管理器。用于管理音频流相关功能。 |

**函数**

| 名称 | 描述 |
| --- | --- |
| OH_AudioCommon_Result OH_AudioManager_GetAudioStreamManager(OH_AudioStreamManager **streamManager) | 获取音频流管理器句柄。 |
| OH_AudioCommon_Result OH_AudioStreamManager_GetDirectPlaybackSupport(OH_AudioStreamManager *audioStreamManager, OH_AudioStreamInfo *streamInfo, OH_AudioStream_Usage usage, OH_AudioStream_DirectPlaybackMode *directPlaybackMode) | 获取当前音频流支持的direct通路播放模式。 |
| OH_AudioCommon_Result OH_AudioStreamManager_IsAcousticEchoCancelerSupported(OH_AudioStreamManager *streamManager, OH_AudioStream_SourceType sourceType, bool *supported) | 查询指定的录音流类型使用场景是否支持回声消除。 |
| bool OH_AudioStreamManager_IsFastPlaybackSupported(OH_AudioStreamManager *streamManager, OH_AudioStreamInfo *streamInfo, OH_AudioStream_Usage usage) | 查询当前设备在特定音频流信息和使用场景下是否支持低时延播放。 |
| bool OH_AudioStreamManager_IsFastRecordingSupported(OH_AudioStreamManager *streamManager, OH_AudioStreamInfo *streamInfo, OH_AudioStream_SourceType source) | 查询当前设备在特定音频流信息和使用场景下是否支持低时延录制。 |
| bool OH_AudioStreamManager_IsIntelligentNoiseReductionEnabledForCurrentDevice(OH_AudioStreamManager *streamManager, OH_AudioStream_SourceType source) | 查询指定录音流类型的智能降噪开关是否已开启。 |

**函数说明**

**OH_AudioManager_GetAudioStreamManager()**

```ets
OH_AudioCommon_Result OH_AudioManager_GetAudioStreamManager(OH_AudioStreamManager **streamManager)
```

描述

获取音频流管理器句柄。

起始版本： 19

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AudioStreamManager **streamManager | 音频流管理器句柄。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_AudioCommon_Result | AUDIOCOMMON_RESULT_SUCCESS = 0：函数执行成功。  AUDIOCOMMON_RESULT_ERROR_SYSTEM = 6800301：系统状态错误。 |

**OH_AudioStreamManager_GetDirectPlaybackSupport()**

```ets
OH_AudioCommon_Result OH_AudioStreamManager_GetDirectPlaybackSupport(OH_AudioStreamManager *audioStreamManager, OH_AudioStreamInfo *streamInfo, OH_AudioStream_Usage usage, OH_AudioStream_DirectPlaybackMode *directPlaybackMode)
```

描述

获取当前音频流支持的direct通路播放模式。

起始版本： 19

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AudioStreamManager *audioStreamManager | 音频流管理器句柄。通过 OH_AudioManager_GetAudioStreamManager获取句柄。 |
| OH_AudioStreamInfo *streamInfo | 音频流信息指针。 |
| OH_AudioStream_Usage usage | 音频流使用场景。 |
| OH_AudioStream_DirectPlaybackMode *directPlaybackMode | 指向 OH_AudioStream_DirectPlaybackMode，用于获取当前音频流支持的direct通路播放模式。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_AudioCommon_Result | AUDIOCOMMON_RESULT_SUCCESS = 0：函数执行成功。  AUDIOCOMMON_RESULT_ERROR_INVALID_PARAM = 6800101：  1. 参数audioStreamManager为nullptr；  2. 参数streamInfo为nullptr；  3. 参数usage无效；  4. 参数directPlaybackMode为nullptr。 |

**OH_AudioStreamManager_IsAcousticEchoCancelerSupported()**

```ets
OH_AudioCommon_Result OH_AudioStreamManager_IsAcousticEchoCancelerSupported(OH_AudioStreamManager *streamManager, OH_AudioStream_SourceType sourceType, bool *supported)
```

描述

查询指定的录音流类型使用场景是否支持回声消除。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AudioStreamManager *streamManager | 音频流管理器句柄。通过 OH_AudioManager_GetAudioStreamManager获取句柄。 |
| OH_AudioStream_SourceType sourceType | 指向OH_AudioStream_SourceType，用于设置音频输入流的使用场景。 |
| bool *supported | 查询指定的source type是否支持回声消除的结果。true表示支持回声消除，false表示不支持回声消除。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_AudioCommon_Result | AUDIOCOMMON_RESULT_SUCCESS = 0 ：函数执行成功。  AUDIOCOMMON_RESULT_ERROR_INVALID_PARAM = 6800101 ：  1.参数audioStreamManager为nullptr；  2.参数sourceType无效；  3.参数supported为nullptr。 |

**OH_AudioStreamManager_IsFastPlaybackSupported()**

```ets
bool OH_AudioStreamManager_IsFastPlaybackSupported(OH_AudioStreamManager *streamManager, OH_AudioStreamInfo *streamInfo, OH_AudioStream_Usage usage)
```

描述

查询当前设备在特定音频流信息和使用场景下是否支持低时延播放。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AudioStreamManager *streamManager | 音频流管理器句柄。通过OH_AudioManager_GetAudioStreamManager获取句柄。 |
| OH_AudioStreamInfo *streamInfo | 音频流信息指针。 |
| OH_AudioStream_Usage usage | 音频流使用场景。 |

返回：

| 类型 | 说明 |
| --- | --- |
| bool | 返回true时表示支持低时延播放，返回false时表示不支持。 |

**OH_AudioStreamManager_IsFastRecordingSupported()**

```ets
bool OH_AudioStreamManager_IsFastRecordingSupported(OH_AudioStreamManager *streamManager, OH_AudioStreamInfo *streamInfo, OH_AudioStream_SourceType source)
```

描述

查询当前设备在特定音频流信息和使用场景下是否支持低时延录制。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AudioStreamManager *streamManager | 音频流管理器句柄。通过OH_AudioManager_GetAudioStreamManager获取句柄。 |
| OH_AudioStreamInfo *streamInfo | 音频流信息指针。 |
| OH_AudioStream_SourceType source | 音频流使用场景。 |

返回：

| 类型 | 说明 |
| --- | --- |
| bool | 返回true时表示支持低时延录制，返回false时表示不支持。 |

**OH_AudioStreamManager_IsIntelligentNoiseReductionEnabledForCurrentDevice()**

```ets
bool OH_AudioStreamManager_IsIntelligentNoiseReductionEnabledForCurrentDevice(OH_AudioStreamManager *streamManager, OH_AudioStream_SourceType source)
```

描述

查询指定录音流类型的智能降噪开关是否已开启。

起始版本： 21

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AudioStreamManager *streamManager | 音频流管理器句柄。通过OH_AudioManager_GetAudioStreamManager获取句柄。 |
| OH_AudioStream_SourceType source | 根据音频设备和管道类型选择结果得出的音频流使用场景。 |

返回：

| 类型 | 说明 |
| --- | --- |
| bool | 返回true时表示智能降噪开关已打开，返回false时表示开关已关闭。 |