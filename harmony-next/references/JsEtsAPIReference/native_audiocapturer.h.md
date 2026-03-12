# native_audiocapturer.h

#### 概述

声明音频采集的相关接口。

**引用文件：** <ohaudio/native_audiocapturer.h>

**库：** libohaudio.so

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 10

**相关模块：**[OHAudio](OHAudio.md)

#### 汇总

#### 函数

名称typedef关键字描述[OH_AudioStream_Result OH_AudioCapturer_Release(OH_AudioCapturer* capturer)](#ZH-CN_TOPIC_0000002497445730__oh_audiocapturer_release)-释放输入音频流。[OH_AudioStream_Result OH_AudioCapturer_Start(OH_AudioCapturer* capturer)](#ZH-CN_TOPIC_0000002497445730__oh_audiocapturer_start)-启动音频采集器，开始获取音频数据。[OH_AudioStream_Result OH_AudioCapturer_Pause(OH_AudioCapturer* capturer)](#ZH-CN_TOPIC_0000002497445730__oh_audiocapturer_pause)-暂停输入音频流。[OH_AudioStream_Result OH_AudioCapturer_Stop(OH_AudioCapturer* capturer)](#ZH-CN_TOPIC_0000002497445730__oh_audiocapturer_stop)-停止音频采集器，停止输入音频流。[OH_AudioStream_Result OH_AudioCapturer_Flush(OH_AudioCapturer* capturer)](#ZH-CN_TOPIC_0000002497445730__oh_audiocapturer_flush)-丢弃获取的音频数据。[OH_AudioStream_Result OH_AudioCapturer_GetCurrentState(OH_AudioCapturer* capturer, OH_AudioStream_State* state)](#ZH-CN_TOPIC_0000002497445730__oh_audiocapturer_getcurrentstate)-查询当前音频流状态。[OH_AudioStream_Result OH_AudioCapturer_GetLatencyMode(OH_AudioCapturer* capturer, OH_AudioStream_LatencyMode* latencyMode)](#ZH-CN_TOPIC_0000002497445730__oh_audiocapturer_getlatencymode)-查询当前音频流时延模式。[OH_AudioStream_Result OH_AudioCapturer_GetStreamId(OH_AudioCapturer* capturer, uint32_t* streamId)](#ZH-CN_TOPIC_0000002497445730__oh_audiocapturer_getstreamid)-查询当前输入音频流ID。[OH_AudioStream_Result OH_AudioCapturer_GetSamplingRate(OH_AudioCapturer* capturer, int32_t* rate)](#ZH-CN_TOPIC_0000002497445730__oh_audiocapturer_getsamplingrate)-查询当前输入音频流采样率。[OH_AudioStream_Result OH_AudioCapturer_GetChannelCount(OH_AudioCapturer* capturer, int32_t* channelCount)](#ZH-CN_TOPIC_0000002497445730__oh_audiocapturer_getchannelcount)-查询当前音频流通道数。[OH_AudioStream_Result OH_AudioCapturer_GetSampleFormat(OH_AudioCapturer* capturer, OH_AudioStream_SampleFormat* sampleFormat)](#ZH-CN_TOPIC_0000002497445730__oh_audiocapturer_getsampleformat)-查询当前输入音频流采样格式。[OH_AudioStream_Result OH_AudioCapturer_GetEncodingType(OH_AudioCapturer* capturer, OH_AudioStream_EncodingType* encodingType)](#ZH-CN_TOPIC_0000002497445730__oh_audiocapturer_getencodingtype)-查询当前音频流编码类型。[OH_AudioStream_Result OH_AudioCapturer_GetCapturerInfo(OH_AudioCapturer* capturer, OH_AudioStream_SourceType* sourceType)](#ZH-CN_TOPIC_0000002497445730__oh_audiocapturer_getcapturerinfo)-查询当前音频流工作场景类型。[OH_AudioStream_Result OH_AudioCapturer_GetFrameSizeInCallback(OH_AudioCapturer* capturer, int32_t* frameSize)](#ZH-CN_TOPIC_0000002497445730__oh_audiocapturer_getframesizeincallback)-在回调中查询帧大小，它是每次回调返回的缓冲区的固定长度。[OH_AudioStream_Result OH_AudioCapturer_GetTimestamp(OH_AudioCapturer* capturer, clockid_t clockId,int64_t* framePosition, int64_t* timestamp)](#ZH-CN_TOPIC_0000002497445730__oh_audiocapturer_gettimestamp)-

获取输入音频流时间戳和当前数据帧位置信息。

 该接口可以获取到音频通道实际录制位置（framePosition）以及录制到该位置时候的时间戳（timestamp），时间戳单位为纳秒。

[OH_AudioStream_Result OH_AudioCapturer_GetFramesRead(OH_AudioCapturer* capturer, int64_t* frames)](#ZH-CN_TOPIC_0000002497445730__oh_audiocapturer_getframesread)-查询自创建流以来已读取的帧数。[OH_AudioStream_Result OH_AudioCapturer_GetOverflowCount(OH_AudioCapturer* capturer, uint32_t* count)](#ZH-CN_TOPIC_0000002497445730__oh_audiocapturer_getoverflowcount)-查询当前录制音频流过载数。[typedef void (*OH_AudioCapturer_OnReadDataCallback)(OH_AudioCapturer* capturer, void* userData, void* audioData, int32_t audioDataSize)](#ZH-CN_TOPIC_0000002497445730__oh_audiocapturer_onreaddatacallback)OH_AudioCapturer_OnReadDataCallback读取音频数据的回调函数。[typedef void (*OH_AudioCapturer_OnDeviceChangeCallback)(OH_AudioCapturer* capturer, void* userData, OH_AudioDeviceDescriptorArray* deviceArray)](#ZH-CN_TOPIC_0000002497445730__oh_audiocapturer_ondevicechangecallback)OH_AudioCapturer_OnDeviceChangeCallback音频录制流的设备变化事件回调函数。[typedef void (*OH_AudioCapturer_OnInterruptCallback)(OH_AudioCapturer* capturer, void* userData, OH_AudioInterrupt_ForceType type, OH_AudioInterrupt_Hint hint)](#ZH-CN_TOPIC_0000002497445730__oh_audiocapturer_oninterruptcallback)OH_AudioCapturer_OnInterruptCallback音频录制流的中断事件回调函数。[typedef void (*OH_AudioCapturer_OnErrorCallback)(OH_AudioCapturer* capturer, void* userData, OH_AudioStream_Result error)](#ZH-CN_TOPIC_0000002497445730__oh_audiocapturer_onerrorcallback)OH_AudioCapturer_OnErrorCallback音频录制流的错误事件回调函数。[OH_AudioStream_Result OH_AudioCapturer_GetFastStatus(OH_AudioCapturer* capturer, OH_AudioStream_FastStatus* status)](#ZH-CN_TOPIC_0000002497445730__oh_audiocapturer_getfaststatus)-获取音频录制过程中的运行状态，是否在低时延状态下工作。[typedef void (*OH_AudioCapturer_OnFastStatusChange)(OH_AudioCapturer* capturer, void* userData, OH_AudioStream_FastStatus status)](#ZH-CN_TOPIC_0000002497445730__oh_audiocapturer_onfaststatuschange)OH_AudioCapturer_OnFastStatusChange音频录制过程中低时延状态改变事件的回调函数。

#### 函数说明

#### OH_AudioCapturer_Release()

```ets
OH_AudioStream_Result OH_AudioCapturer_Release(OH_AudioCapturer* capturer)
```

**描述**

释放输入音频流。

**需要权限：** ohos.permission.MICROPHONE

**起始版本：** 10

**参数：**

参数项描述[OH_AudioCapturer](OH_AudioCapturerStruct.md)* capturer指向[OH_AudioStreamBuilder_GenerateCapturer](native_audiostreambuilder.h.md#ZH-CN_TOPIC_0000002497605714__oh_audiostreambuilder_generatecapturer)创建的音频流实例。

**返回：**

类型说明[OH_AudioStream_Result](native_audiostream_base.h.md#ZH-CN_TOPIC_0000002529445679__oh_audiostream_result)

AUDIOSTREAM_SUCCESS：函数执行成功。

 AUDIOSTREAM_ERROR_INVALID_PARAM：参数capturer为nullptr。

 AUDIOSTREAM_ERROR_ILLEGAL_STATE：执行状态异常。

#### OH_AudioCapturer_Start()

```ets
OH_AudioStream_Result OH_AudioCapturer_Start(OH_AudioCapturer* capturer)
```

**描述**

启动音频采集器，开始获取音频数据。

**需要权限：** ohos.permission.MICROPHONE

**起始版本：** 10

**参数：**

参数项描述[OH_AudioCapturer](OH_AudioCapturerStruct.md)* capturer指向[OH_AudioStreamBuilder_GenerateCapturer](native_audiostreambuilder.h.md#ZH-CN_TOPIC_0000002497605714__oh_audiostreambuilder_generatecapturer)创建的音频流实例。

**返回：**

类型说明[OH_AudioStream_Result](native_audiostream_base.h.md#ZH-CN_TOPIC_0000002529445679__oh_audiostream_result)

AUDIOSTREAM_SUCCESS：函数执行成功。

 AUDIOSTREAM_ERROR_INVALID_PARAM：参数capturer为nullptr。

 AUDIOSTREAM_ERROR_ILLEGAL_STATE：执行状态异常。

#### OH_AudioCapturer_Pause()

```ets
OH_AudioStream_Result OH_AudioCapturer_Pause(OH_AudioCapturer* capturer)
```

**描述**

暂停输入音频流。

**需要权限：** ohos.permission.MICROPHONE

**起始版本：** 10

**参数：**

参数项描述[OH_AudioCapturer](OH_AudioCapturerStruct.md)* capturer指向[OH_AudioStreamBuilder_GenerateCapturer](native_audiostreambuilder.h.md#ZH-CN_TOPIC_0000002497605714__oh_audiostreambuilder_generatecapturer)创建的音频流实例。

**返回：**

类型说明[OH_AudioStream_Result](native_audiostream_base.h.md#ZH-CN_TOPIC_0000002529445679__oh_audiostream_result)

AUDIOSTREAM_SUCCESS：函数执行成功。

 AUDIOSTREAM_ERROR_INVALID_PARAM：参数capturer为nullptr。

 AUDIOSTREAM_ERROR_ILLEGAL_STATE：执行状态异常。

#### OH_AudioCapturer_Stop()

```ets
OH_AudioStream_Result OH_AudioCapturer_Stop(OH_AudioCapturer* capturer)
```

**描述**

停止音频采集器，停止输入音频流。

**需要权限：** ohos.permission.MICROPHONE

**起始版本：** 10

**参数：**

参数项描述[OH_AudioCapturer](OH_AudioCapturerStruct.md)* capturer指向[OH_AudioStreamBuilder_GenerateCapturer](native_audiostreambuilder.h.md#ZH-CN_TOPIC_0000002497605714__oh_audiostreambuilder_generatecapturer)创建的音频流实例。

**返回：**

类型说明[OH_AudioStream_Result](native_audiostream_base.h.md#ZH-CN_TOPIC_0000002529445679__oh_audiostream_result)

AUDIOSTREAM_SUCCESS：函数执行成功。

 AUDIOSTREAM_ERROR_INVALID_PARAM：参数capturer为nullptr。

 AUDIOSTREAM_ERROR_ILLEGAL_STATE：执行状态异常。

#### OH_AudioCapturer_Flush()

```ets
OH_AudioStream_Result OH_AudioCapturer_Flush(OH_AudioCapturer* capturer)
```

**描述**

丢弃获取的音频数据。

**起始版本：** 10

**参数：**

参数项描述[OH_AudioCapturer](OH_AudioCapturerStruct.md)* capturer指向[OH_AudioStreamBuilder_GenerateCapturer](native_audiostreambuilder.h.md#ZH-CN_TOPIC_0000002497605714__oh_audiostreambuilder_generatecapturer)创建的音频流实例。

**返回：**

类型说明[OH_AudioStream_Result](native_audiostream_base.h.md#ZH-CN_TOPIC_0000002529445679__oh_audiostream_result)

AUDIOSTREAM_SUCCESS：函数执行成功。

 AUDIOSTREAM_ERROR_INVALID_PARAM：参数capturer为nullptr。

 AUDIOSTREAM_ERROR_ILLEGAL_STATE：执行状态异常。

#### OH_AudioCapturer_GetCurrentState()

```ets
OH_AudioStream_Result OH_AudioCapturer_GetCurrentState(OH_AudioCapturer* capturer, OH_AudioStream_State* state)
```

**描述**

查询当前音频流状态。

**起始版本：** 10

**参数：**

参数项描述[OH_AudioCapturer](OH_AudioCapturerStruct.md)* capturer指向[OH_AudioStreamBuilder_GenerateCapturer](native_audiostreambuilder.h.md#ZH-CN_TOPIC_0000002497605714__oh_audiostreambuilder_generatecapturer)创建的音频流实例。[OH_AudioStream_State](native_audiostream_base.h.md#ZH-CN_TOPIC_0000002529445679__oh_audiostream_state)* state指向一个用来接收音频流状态的变量。

**返回：**

类型说明[OH_AudioStream_Result](native_audiostream_base.h.md#ZH-CN_TOPIC_0000002529445679__oh_audiostream_result)

AUDIOSTREAM_SUCCESS：函数执行成功。

 AUDIOSTREAM_ERROR_INVALID_PARAM：参数capturer为nullptr。

#### OH_AudioCapturer_GetLatencyMode()

```ets
OH_AudioStream_Result OH_AudioCapturer_GetLatencyMode(OH_AudioCapturer* capturer,OH_AudioStream_LatencyMode* latencyMode)
```

**描述**

查询当前音频流时延模式。

**起始版本：** 10

**参数：**

参数项描述[OH_AudioCapturer](OH_AudioCapturerStruct.md)* capturer指向[OH_AudioStreamBuilder_GenerateCapturer](native_audiostreambuilder.h.md#ZH-CN_TOPIC_0000002497605714__oh_audiostreambuilder_generatecapturer)创建的音频流实例。[OH_AudioStream_LatencyMode](native_audiostream_base.h.md#ZH-CN_TOPIC_0000002529445679__oh_audiostream_latencymode)* latencyMode指向一个用来接收音频流时延模式的变量。

**返回：**

类型说明[OH_AudioStream_Result](native_audiostream_base.h.md#ZH-CN_TOPIC_0000002529445679__oh_audiostream_result)

AUDIOSTREAM_SUCCESS：函数执行成功。

 AUDIOSTREAM_ERROR_INVALID_PARAM：参数capturer为nullptr。

#### OH_AudioCapturer_GetStreamId()

```ets
OH_AudioStream_Result OH_AudioCapturer_GetStreamId(OH_AudioCapturer* capturer, uint32_t* streamId)
```

**描述**

查询当前输入音频流ID。

**起始版本：** 10

**参数：**

参数项描述[OH_AudioCapturer](OH_AudioCapturerStruct.md)* capturer指向[OH_AudioStreamBuilder_GenerateCapturer](native_audiostreambuilder.h.md#ZH-CN_TOPIC_0000002497605714__oh_audiostreambuilder_generatecapturer)创建的音频流实例。uint32_t* streamId指向一个用来接收音频流ID的变量。

**返回：**

类型说明[OH_AudioStream_Result](native_audiostream_base.h.md#ZH-CN_TOPIC_0000002529445679__oh_audiostream_result)

AUDIOSTREAM_SUCCESS：函数执行成功。

 AUDIOSTREAM_ERROR_INVALID_PARAM：参数capturer为nullptr。

#### OH_AudioCapturer_GetSamplingRate()

```ets
OH_AudioStream_Result OH_AudioCapturer_GetSamplingRate(OH_AudioCapturer* capturer, int32_t* rate)
```

**描述**

查询当前输入音频流采样率。

**起始版本：** 10

**参数：**

参数项描述[OH_AudioCapturer](OH_AudioCapturerStruct.md)* capturer指向[OH_AudioStreamBuilder_GenerateCapturer](native_audiostreambuilder.h.md#ZH-CN_TOPIC_0000002497605714__oh_audiostreambuilder_generatecapturer)创建的音频流实例。int32_t* rate指向一个用来接收音频流采样率的变量。

**返回：**

类型说明[OH_AudioStream_Result](native_audiostream_base.h.md#ZH-CN_TOPIC_0000002529445679__oh_audiostream_result)

AUDIOSTREAM_SUCCESS：函数执行成功。

 AUDIOSTREAM_ERROR_INVALID_PARAM：参数capturer为nullptr。

#### OH_AudioCapturer_GetChannelCount()

```ets
OH_AudioStream_Result OH_AudioCapturer_GetChannelCount(OH_AudioCapturer* capturer, int32_t* channelCount)
```

**描述**

查询当前音频流通道数。

**起始版本：** 10

**参数：**

参数项描述[OH_AudioCapturer](OH_AudioCapturerStruct.md)* capturer指向[OH_AudioStreamBuilder_GenerateCapturer](native_audiostreambuilder.h.md#ZH-CN_TOPIC_0000002497605714__oh_audiostreambuilder_generatecapturer)创建的音频流实例。int32_t* channelCount指向一个用来接收音频流通道数的变量。

**返回：**

类型说明[OH_AudioStream_Result](native_audiostream_base.h.md#ZH-CN_TOPIC_0000002529445679__oh_audiostream_result)

AUDIOSTREAM_SUCCESS：函数执行成功。

 AUDIOSTREAM_ERROR_INVALID_PARAM：参数capturer为nullptr。

#### OH_AudioCapturer_GetSampleFormat()

```ets
OH_AudioStream_Result OH_AudioCapturer_GetSampleFormat(OH_AudioCapturer* capturer,OH_AudioStream_SampleFormat* sampleFormat)
```

**描述**

查询当前输入音频流采样格式。

**起始版本：** 10

**参数：**

参数项描述[OH_AudioCapturer](OH_AudioCapturerStruct.md)* capturer指向[OH_AudioStreamBuilder_GenerateCapturer](native_audiostreambuilder.h.md#ZH-CN_TOPIC_0000002497605714__oh_audiostreambuilder_generatecapturer)创建的音频流实例。[OH_AudioStream_SampleFormat](native_audiostream_base.h.md#ZH-CN_TOPIC_0000002529445679__oh_audiostream_sampleformat)* sampleFormat指向一个用来接收音频流采样格式的变量。

**返回：**

类型说明[OH_AudioStream_Result](native_audiostream_base.h.md#ZH-CN_TOPIC_0000002529445679__oh_audiostream_result)

AUDIOSTREAM_SUCCESS：函数执行成功。

 AUDIOSTREAM_ERROR_INVALID_PARAM：参数capturer为nullptr。

#### OH_AudioCapturer_GetEncodingType()

```ets
OH_AudioStream_Result OH_AudioCapturer_GetEncodingType(OH_AudioCapturer* capturer,OH_AudioStream_EncodingType* encodingType)
```

**描述**

查询当前音频流编码类型。

**起始版本：** 10

**参数：**

参数项描述[OH_AudioCapturer](OH_AudioCapturerStruct.md)* capturer指向[OH_AudioStreamBuilder_GenerateCapturer](native_audiostreambuilder.h.md#ZH-CN_TOPIC_0000002497605714__oh_audiostreambuilder_generatecapturer)创建的音频流实例。[OH_AudioStream_EncodingType](native_audiostream_base.h.md#ZH-CN_TOPIC_0000002529445679__oh_audiostream_encodingtype)* encodingType指向一个用来接收音频流编码类型的变量。

**返回：**

类型说明[OH_AudioStream_Result](native_audiostream_base.h.md#ZH-CN_TOPIC_0000002529445679__oh_audiostream_result)

AUDIOSTREAM_SUCCESS：函数执行成功。

 AUDIOSTREAM_ERROR_INVALID_PARAM：参数capturer为nullptr。

#### OH_AudioCapturer_GetCapturerInfo()

```ets
OH_AudioStream_Result OH_AudioCapturer_GetCapturerInfo(OH_AudioCapturer* capturer,OH_AudioStream_SourceType* sourceType)
```

**描述**

查询当前音频流工作场景类型。

**起始版本：** 10

**参数：**

参数项描述[OH_AudioCapturer](OH_AudioCapturerStruct.md)* capturer指向[OH_AudioStreamBuilder_GenerateCapturer](native_audiostreambuilder.h.md#ZH-CN_TOPIC_0000002497605714__oh_audiostreambuilder_generatecapturer)创建的音频流实例。[OH_AudioStream_SourceType](native_audiostream_base.h.md#ZH-CN_TOPIC_0000002529445679__oh_audiostream_sourcetype)* sourceType指向一个用来接收输入类型音频流的工作场景的变量。

**返回：**

类型说明[OH_AudioStream_Result](native_audiostream_base.h.md#ZH-CN_TOPIC_0000002529445679__oh_audiostream_result)

AUDIOSTREAM_SUCCESS：函数执行成功。

 AUDIOSTREAM_ERROR_INVALID_PARAM：参数capturer为nullptr。

#### OH_AudioCapturer_GetFrameSizeInCallback()

```ets
OH_AudioStream_Result OH_AudioCapturer_GetFrameSizeInCallback(OH_AudioCapturer* capturer,int32_t* frameSize)
```

**描述**

在回调中查询帧大小，它是每次回调返回的缓冲区的固定长度。

**起始版本：** 10

**参数：**

参数项描述[OH_AudioCapturer](OH_AudioCapturerStruct.md)* capturer指向[OH_AudioStreamBuilder_GenerateCapturer](native_audiostreambuilder.h.md#ZH-CN_TOPIC_0000002497605714__oh_audiostreambuilder_generatecapturer)创建的音频流实例。int32_t* frameSize指向将为帧大小设置的变量的指针。

**返回：**

类型说明[OH_AudioStream_Result](native_audiostream_base.h.md#ZH-CN_TOPIC_0000002529445679__oh_audiostream_result)

AUDIOSTREAM_SUCCESS：函数执行成功。

 AUDIOSTREAM_ERROR_INVALID_PARAM：参数capturer为nullptr。

 AUDIOSTREAM_ERROR_ILLEGAL_STATE：执行状态异常。

#### OH_AudioCapturer_GetTimestamp()

```ets
OH_AudioStream_Result OH_AudioCapturer_GetTimestamp(OH_AudioCapturer* capturer, clockid_t clockId,int64_t* framePosition, int64_t* timestamp)
```

**描述**

获取输入音频流时间戳和当前数据帧位置信息。

 该接口可以获取到音频通道实际录制位置（framePosition）以及录制到该位置时候的时间戳（timestamp），时间戳单位为纳秒。

**起始版本：** 10

**参数：**

参数项描述[OH_AudioCapturer](OH_AudioCapturerStruct.md)* capturer指向[OH_AudioStreamBuilder_GenerateCapturer](native_audiostreambuilder.h.md#ZH-CN_TOPIC_0000002497605714__oh_audiostreambuilder_generatecapturer)创建的音频流实例。clockid_t clockId时钟标识符，使用CLOCK_MONOTONIC。int64_t* framePosition指向要接收位置的变量的指针。int64_t* timestamp指向接收时间戳的变量的指针。

**返回：**

类型说明[OH_AudioStream_Result](native_audiostream_base.h.md#ZH-CN_TOPIC_0000002529445679__oh_audiostream_result)

AUDIOSTREAM_SUCCESS：函数执行成功。

 AUDIOSTREAM_ERROR_INVALID_PARAM：

 1. 参数capturer为nullptr；

 2. 参数clockId无效。

 AUDIOSTREAM_ERROR_ILLEGAL_STATE：执行状态异常。

#### OH_AudioCapturer_GetFramesRead()

```ets
OH_AudioStream_Result OH_AudioCapturer_GetFramesRead(OH_AudioCapturer* capturer, int64_t* frames)
```

**描述**

查询自创建流以来已读取的帧数。

**起始版本：** 10

**参数：**

参数项描述[OH_AudioCapturer](OH_AudioCapturerStruct.md)* capturer指向[OH_AudioStreamBuilder_GenerateCapturer](native_audiostreambuilder.h.md#ZH-CN_TOPIC_0000002497605714__oh_audiostreambuilder_generatecapturer)创建的音频流实例。int64_t* frames指向将为帧计数设置的变量的指针。

**返回：**

类型说明[OH_AudioStream_Result](native_audiostream_base.h.md#ZH-CN_TOPIC_0000002529445679__oh_audiostream_result)

AUDIOSTREAM_SUCCESS：函数执行成功。

 AUDIOSTREAM_ERROR_INVALID_PARAM：参数capturer为nullptr。

#### OH_AudioCapturer_GetOverflowCount()

```ets
OH_AudioStream_Result OH_AudioCapturer_GetOverflowCount(OH_AudioCapturer* capturer, uint32_t* count)
```

**描述**

查询当前录制音频流过载数。

**起始版本：** 12

**参数：**

参数项描述[OH_AudioCapturer](OH_AudioCapturerStruct.md)* capturer指向[OH_AudioStreamBuilder_GenerateCapturer](native_audiostreambuilder.h.md#ZH-CN_TOPIC_0000002497605714__oh_audiostreambuilder_generatecapturer)创建的音频流实例。uint32_t* count指向一个用来接收音频流过载数的变量的指针。

**返回：**

类型说明[OH_AudioStream_Result](native_audiostream_base.h.md#ZH-CN_TOPIC_0000002529445679__oh_audiostream_result)

AUDIOSTREAM_SUCCESS：函数执行成功。

 AUDIOSTREAM_ERROR_INVALID_PARAM：参数capturer为nullptr。

#### OH_AudioCapturer_OnReadDataCallback()

```ets
typedef void (*OH_AudioCapturer_OnReadDataCallback)(OH_AudioCapturer* capturer, void* userData, void* audioData,int32_t audioDataSize)
```

**描述**

读取音频数据的回调函数。

**起始版本：** 20

**参数：**

参数项描述[OH_AudioCapturer](OH_AudioCapturerStruct.md)* capturer指向[OH_AudioStreamBuilder_GenerateCapturer](native_audiostreambuilder.h.md#ZH-CN_TOPIC_0000002497605714__oh_audiostreambuilder_generatecapturer)创建的音频流实例。void* userData指向应用自定义的数据存储区域。void* audioData指向录制数据存储区域，用于应用读取录制数据。int32_t audioDataSize录制数据的长度。

#### OH_AudioCapturer_OnDeviceChangeCallback()

```ets
typedef void (*OH_AudioCapturer_OnDeviceChangeCallback)(OH_AudioCapturer* capturer, void* userData,OH_AudioDeviceDescriptorArray* deviceArray)
```

**描述**

音频录制流的设备变化事件回调函数。

**起始版本：** 20

**参数：**

参数项描述[OH_AudioCapturer](OH_AudioCapturerStruct.md)* capturer指向[OH_AudioStreamBuilder_GenerateCapturer](native_audiostreambuilder.h.md#ZH-CN_TOPIC_0000002497605714__oh_audiostreambuilder_generatecapturer)创建的音频流实例。void* userData指向应用自定义的数据存储区域。[OH_AudioDeviceDescriptorArray](OH_AudioDeviceDescriptorArray.md)* deviceArray音频设备描述符数组。

#### OH_AudioCapturer_OnInterruptCallback()

```ets
typedef void (*OH_AudioCapturer_OnInterruptCallback)(OH_AudioCapturer* capturer, void* userData,OH_AudioInterrupt_ForceType type, OH_AudioInterrupt_Hint hint)
```

**描述**

音频录制流的中断事件回调函数。

**起始版本：** 20

**参数：**

参数项描述[OH_AudioCapturer](OH_AudioCapturerStruct.md)* capturer指向[OH_AudioStreamBuilder_GenerateCapturer](native_audiostreambuilder.h.md#ZH-CN_TOPIC_0000002497605714__oh_audiostreambuilder_generatecapturer)创建的音频流实例。void* userData指向应用自定义的数据存储区域。[OH_AudioInterrupt_ForceType](native_audiostream_base.h.md#ZH-CN_TOPIC_0000002529445679__oh_audiointerrupt_forcetype) type音频流中断类型。[OH_AudioInterrupt_Hint](native_audiostream_base.h.md#ZH-CN_TOPIC_0000002529445679__oh_audiointerrupt_hint) hint音频流中断提示类型。

#### OH_AudioCapturer_OnErrorCallback()

```ets
typedef void (*OH_AudioCapturer_OnErrorCallback)(OH_AudioCapturer* capturer, void* userData,OH_AudioStream_Result error)
```

**描述**

音频录制流的错误事件回调函数。

**起始版本：** 20

**参数：**

参数项描述[OH_AudioCapturer](OH_AudioCapturerStruct.md)* capturer指向[OH_AudioStreamBuilder_GenerateCapturer](native_audiostreambuilder.h.md#ZH-CN_TOPIC_0000002497605714__oh_audiostreambuilder_generatecapturer)创建的音频流实例。void* userData指向应用自定义的数据存储区域。[OH_AudioStream_Result](native_audiostream_base.h.md#ZH-CN_TOPIC_0000002529445679__oh_audiostream_result) error音频流录制错误结果。

#### OH_AudioCapturer_GetFastStatus()

```ets
OH_AudioStream_Result OH_AudioCapturer_GetFastStatus(OH_AudioCapturer* capturer,OH_AudioStream_FastStatus* status)
```

**描述**

获取音频录制过程中的运行状态，是否在低时延状态下工作。

**起始版本：** 20

**参数：**

参数项描述[OH_AudioCapturer](OH_AudioCapturerStruct.md)* capturer指向[OH_AudioStreamBuilder_GenerateCapturer](native_audiostreambuilder.h.md#ZH-CN_TOPIC_0000002497605714__oh_audiostreambuilder_generatecapturer)创建的音频流实例。[OH_AudioStream_FastStatus](native_audiostream_base.h.md#ZH-CN_TOPIC_0000002529445679__oh_audiostream_faststatus)* status指向接收低时延状态的指针。

**返回：**

类型说明[OH_AudioStream_Result](native_audiostream_base.h.md#ZH-CN_TOPIC_0000002529445679__oh_audiostream_result)

AUDIOSTREAM_SUCCESS：函数执行成功。

 AUDIOSTREAM_ERROR_INVALID_PARAM：参数capturer为nullptr。

 AUDIOSTREAM_ERROR_ILLEGAL_STATE：执行状态异常，仅在释放状态之前可用。

#### OH_AudioCapturer_OnFastStatusChange()

```ets
typedef void (*OH_AudioCapturer_OnFastStatusChange)(OH_AudioCapturer* capturer,void* userData,OH_AudioStream_FastStatus status)
```

**描述**

音频录制过程中低时延状态改变事件的回调函数。

**起始版本：** 20

**参数：**

参数项描述[OH_AudioCapturer](OH_AudioCapturerStruct.md)* capturer指向[OH_AudioStreamBuilder_GenerateCapturer](native_audiostreambuilder.h.md#ZH-CN_TOPIC_0000002497605714__oh_audiostreambuilder_generatecapturer)创建的音频流实例。void* userData指向应用自定义的数据存储区域。[OH_AudioStream_FastStatus](native_audiostream_base.h.md#ZH-CN_TOPIC_0000002529445679__oh_audiostream_faststatus) status返回当前低时延状态。