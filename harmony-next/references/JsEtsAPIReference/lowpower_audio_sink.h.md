# lowpower_audio_sink.h

#### 概述

定义LowPowerAudioSink接口。使用LowPowerAudioSink提供的Native API进行音频通路的低功耗播放。

**引用文件：** <multimedia/player_framework/lowpower_audio_sink.h>

**库：** liblowpower_avsink.so

**系统能力：** SystemCapability.Multimedia.Media.LowPowerAVSink

**起始版本：** 20

**相关模块：**[LowPowerAudioSink](LowPowerAudioSink.md)

#### 汇总

#### 函数

名称描述[OH_LowPowerAudioSink* OH_LowPowerAudioSink_CreateByMime(const char* mime)](#ZH-CN_TOPIC_0000002529285909__oh_lowpoweraudiosink_createbymime)创建LowPowerAudioSink。[OH_AVErrCode OH_LowPowerAudioSink_Configure(OH_LowPowerAudioSink* sink, const OH_AVFormat* format)](#ZH-CN_TOPIC_0000002529285909__oh_lowpoweraudiosink_configure)配置LowPowerAudioSink，需要在[OH_LowPowerAudioSink_Prepare](zh-cn_topic_0000002529285909.html#ZH-CN_TOPIC_0000002529285909__oh_lowpoweraudiosink_prepare)前完成。[OH_AVErrCode OH_LowPowerAudioSink_SetParameter(OH_LowPowerAudioSink* sink, const OH_AVFormat* format)](#ZH-CN_TOPIC_0000002529285909__oh_lowpoweraudiosink_setparameter)为LowPowerAudioSink设置参数，支持[OH_LowPowerAudioSink_Prepare](zh-cn_topic_0000002529285909.html#ZH-CN_TOPIC_0000002529285909__oh_lowpoweraudiosink_prepare)后动态设置。[OH_AVErrCode OH_LowPowerAudioSink_GetParameter(OH_LowPowerAudioSink* sink, OH_AVFormat* format)](#ZH-CN_TOPIC_0000002529285909__oh_lowpoweraudiosink_getparameter)获取LowPowerAudioSink的相关参数。[OH_AVErrCode OH_LowPowerAudioSink_Prepare(OH_LowPowerAudioSink* sink)](#ZH-CN_TOPIC_0000002529285909__oh_lowpoweraudiosink_prepare)

准备LowPowerAudioSink的解码、渲染资源，在[OH_LowPowerAudioSink_Configure](lowpower_audio_sink.h.md#ZH-CN_TOPIC_0000002529285909__oh_lowpoweraudiosink_configure)后调用。

 调用此接口前必须调用LowPowerVideoSink的[OH_LowPowerVideoSink_SetSyncAudioSink](lowpower_video_sink.h.md#ZH-CN_TOPIC_0000002497445940__oh_lowpowervideosink_setsyncaudiosink)方法。

[OH_AVErrCode OH_LowPowerAudioSink_Start(OH_LowPowerAudioSink* sink)](#ZH-CN_TOPIC_0000002529285909__oh_lowpoweraudiosink_start)

启动低功耗音频接收器，此接口必须在[OH_LowPowerAudioSink_Prepare](lowpower_audio_sink.h.md#ZH-CN_TOPIC_0000002529285909__oh_lowpoweraudiosink_prepare)成功后调用。

 启动成功后，LowPowerAudioSink将开始上报[OH_LowPowerAudioSink_OnDataNeeded](lowpower_audio_sink_base.h.md#ZH-CN_TOPIC_0000002529445883__oh_lowpoweraudiosink_ondataneeded)事件。

[OH_AVErrCode OH_LowPowerAudioSink_Pause(OH_LowPowerAudioSink* sink)](#ZH-CN_TOPIC_0000002529285909__oh_lowpoweraudiosink_pause)

暂停LowPowerAudioSink，在[OH_LowPowerAudioSink_Start](lowpower_audio_sink.h.md#ZH-CN_TOPIC_0000002529285909__oh_lowpoweraudiosink_start)或[OH_LowPowerAudioSink_Resume](lowpower_audio_sink.h.md#ZH-CN_TOPIC_0000002529285909__oh_lowpoweraudiosink_resume)后调用。

 暂停成功后，LowPowerAudioSink将暂停[OH_LowPowerAudioSink_OnDataNeeded](lowpower_audio_sink_base.h.md#ZH-CN_TOPIC_0000002529445883__oh_lowpoweraudiosink_ondataneeded)事件的上报。

[OH_AVErrCode OH_LowPowerAudioSink_Resume(OH_LowPowerAudioSink* sink)](#ZH-CN_TOPIC_0000002529285909__oh_lowpoweraudiosink_resume)

恢复LowPowerAudioSink，在[OH_LowPowerAudioSink_Pause](lowpower_audio_sink.h.md#ZH-CN_TOPIC_0000002529285909__oh_lowpoweraudiosink_pause)后调用。

 恢复成功后，LowPowerAudioSink将恢复[OH_LowPowerAudioSink_OnDataNeeded](lowpower_audio_sink_base.h.md#ZH-CN_TOPIC_0000002529445883__oh_lowpoweraudiosink_ondataneeded)事件的上报。

[OH_AVErrCode OH_LowPowerAudioSink_Flush(OH_LowPowerAudioSink* sink)](#ZH-CN_TOPIC_0000002529285909__oh_lowpoweraudiosink_flush)

清除LowPowerAudioSink中所有解码器和渲染缓存的输入输出数据。

 此接口不建议在[OH_LowPowerAudioSink_Start](lowpower_audio_sink.h.md#ZH-CN_TOPIC_0000002529285909__oh_lowpoweraudiosink_start)或[OH_LowPowerAudioSink_Resume](lowpower_audio_sink.h.md#ZH-CN_TOPIC_0000002529285909__oh_lowpoweraudiosink_resume)之后调用。

 需要注意的是，如果编解码器之前已输入数据，则需要重新输入编解码器数据。

[OH_AVErrCode OH_LowPowerAudioSink_Stop(OH_LowPowerAudioSink* sink)](#ZH-CN_TOPIC_0000002529285909__oh_lowpoweraudiosink_stop)停止LowPowerAudioSink。[OH_AVErrCode OH_LowPowerAudioSink_Reset(OH_LowPowerAudioSink* sink)](#ZH-CN_TOPIC_0000002529285909__oh_lowpoweraudiosink_reset)

重置LowPowerAudioSink。

 如果要重新使用该实例，需要调用[OH_LowPowerAudioSink_Configure](lowpower_audio_sink.h.md#ZH-CN_TOPIC_0000002529285909__oh_lowpoweraudiosink_configure)完成配置。

[OH_AVErrCode OH_LowPowerAudioSink_Destroy(OH_LowPowerAudioSink* sink)](#ZH-CN_TOPIC_0000002529285909__oh_lowpoweraudiosink_destroy)清理LowPowerAudioSink内部资源，销毁LowPowerAudioSink实例。不能重复销毁。[OH_AVErrCode OH_LowPowerAudioSink_SetVolume(OH_LowPowerAudioSink* sink, const float volume)](#ZH-CN_TOPIC_0000002529285909__oh_lowpoweraudiosink_setvolume)为LowPowerAudioSink设置渲染音量。[OH_AVErrCode OH_LowPowerAudioSink_SetLoudnessGain(OH_LowPowerAudioSink* sink, float loudnessGain)](#ZH-CN_TOPIC_0000002529285909__oh_lowpoweraudiosink_setloudnessgain)为LowPowerAudioSink设置播放响度。[OH_AVErrCode OH_LowPowerAudioSink_SetPlaybackSpeed(OH_LowPowerAudioSink* sink, const float speed)](#ZH-CN_TOPIC_0000002529285909__oh_lowpoweraudiosink_setplaybackspeed)为LowPowerAudioSink设置音频渲染倍速。[OH_AVErrCode OH_LowPowerAudioSink_ReturnSamples(OH_LowPowerAudioSink* sink, OH_AVSamplesBuffer* samples)](#ZH-CN_TOPIC_0000002529285909__oh_lowpoweraudiosink_returnsamples)给LowPowerAudioSink输入buffer。[OH_AVErrCode OH_LowPowerAudioSink_RegisterCallback(OH_LowPowerAudioSink* sink, OH_LowPowerAudioSinkCallback* callback)](#ZH-CN_TOPIC_0000002529285909__oh_lowpoweraudiosink_registercallback)为LowPowerAudioSink注册回调。[OH_LowPowerAudioSinkCallback* OH_LowPowerAudioSinkCallback_Create(void)](#ZH-CN_TOPIC_0000002529285909__oh_lowpoweraudiosinkcallback_create)创建OH_LowPowerAudioSinkCallback实例。[OH_AVErrCode OH_LowPowerAudioSinkCallback_Destroy(OH_LowPowerAudioSinkCallback* callback)](#ZH-CN_TOPIC_0000002529285909__oh_lowpoweraudiosinkcallback_destroy)销毁OH_LowPowerAudioSinkCallback实例。[OH_AVErrCode OH_LowPowerAudioSinkCallback_SetPositionUpdateListener(OH_LowPowerAudioSinkCallback* callback, OH_LowPowerAudioSink_OnPositionUpdated onPositionUpdated, void* userData)](#ZH-CN_TOPIC_0000002529285909__oh_lowpoweraudiosinkcallback_setpositionupdatelistener)为LowPowerAudioSinkCallback设置进度更新监听。[OH_AVErrCode OH_LowPowerAudioSinkCallback_SetDataNeededListener(OH_LowPowerAudioSinkCallback* callback, OH_LowPowerAudioSink_OnDataNeeded onDataNeeded, void* userData)](#ZH-CN_TOPIC_0000002529285909__oh_lowpoweraudiosinkcallback_setdataneededlistener)为LowPowerAudioSinkCallback设置需要数据监听。[OH_AVErrCode OH_LowPowerAudioSinkCallback_SetErrorListener(OH_LowPowerAudioSinkCallback* callback, OH_LowPowerAudioSink_OnError onError, void* userData)](#ZH-CN_TOPIC_0000002529285909__oh_lowpoweraudiosinkcallback_seterrorlistener)为LowPowerAudioSinkCallback设置错误监听。[OH_AVErrCode OH_LowPowerAudioSinkCallback_SetInterruptListener(OH_LowPowerAudioSinkCallback* callback, OH_LowPowerAudioSink_OnInterrupted onInterrupted, void* userData)](#ZH-CN_TOPIC_0000002529285909__oh_lowpoweraudiosinkcallback_setinterruptlistener)为LowPowerAudioSinkCallback设置音频焦点打断监听。[OH_AVErrCode OH_LowPowerAudioSinkCallback_SetDeviceChangeListener(OH_LowPowerAudioSinkCallback* callback, OH_LowPowerAudioSink_OnDeviceChanged onDeviceChanged, void* userData)](#ZH-CN_TOPIC_0000002529285909__oh_lowpoweraudiosinkcallback_setdevicechangelistener)为LowPowerAudioSinkCallback设置音频设备切换监听。[OH_AVErrCode OH_LowPowerAudioSinkCallback_SetEosListener(OH_LowPowerAudioSinkCallback callback, OH_LowPowerAudioSink_OnEos onEos, void userData)](#ZH-CN_TOPIC_0000002529285909__oh_lowpoweraudiosinkcallback_seteoslistener)为LowPowerAudioSinkCallback设置播放完成监听。

#### 函数说明

#### OH_LowPowerAudioSink_CreateByMime()

```ets
OH_LowPowerAudioSink* OH_LowPowerAudioSink_CreateByMime(const char* mime)
```

**描述**

创建LowPowerAudioSink。

**起始版本：** 20

**参数：**

参数项描述const char* mime音频解码器MIME类型，取值范围请参考[AVCODEC_MIME_TYPE](native_avcodec_base.h.md#ZH-CN_TOPIC_0000002529445703__变量)。

**返回：**

类型说明[OH_LowPowerAudioSink](OH_LowPowerAudioSink.md)*如果创建成功返回指向OH_LowPowerAudioSink实例的指针，否则返回空指针。

#### OH_LowPowerAudioSink_Configure()

```ets
OH_AVErrCode OH_LowPowerAudioSink_Configure(OH_LowPowerAudioSink* sink, const OH_AVFormat* format)
```

**描述**

配置LowPowerAudioSink，需要在[OH_LowPowerAudioSink_Prepare](lowpower_audio_sink.h.md#ZH-CN_TOPIC_0000002529285909__oh_lowpoweraudiosink_prepare)前完成。

**起始版本：** 20

**参数：**

参数项描述[OH_LowPowerAudioSink](OH_LowPowerAudioSink.md)* sink指向OH_LowPowerAudioSink实例的指针。const [OH_AVFormat](OH_AVFormat.md)* format指向OH_AVFormat的指针，用于配置LowPowerAudioSink的参数。

**返回：**

类型说明[OH_AVErrCode](native_averrors.h.md#ZH-CN_TOPIC_0000002497605740__oh_averrcode)

AV_ERR_OK：执行成功。

 AV_ERR_INVALID_VAL：参数为nullptr或参数非法。

 AV_ERR_UNSUPPORT：不支持的格式。

 AV_ERR_SERVICE_DIED：媒体服务端已销毁。

 AV_ERR_OPERATE_NOT_PERMIT：操作不支持。

#### OH_LowPowerAudioSink_SetParameter()

```ets
OH_AVErrCode OH_LowPowerAudioSink_SetParameter(OH_LowPowerAudioSink* sink, const OH_AVFormat* format)
```

**描述**

为LowPowerAudioSink设置参数，支持[OH_LowPowerAudioSink_Prepare](lowpower_audio_sink.h.md#ZH-CN_TOPIC_0000002529285909__oh_lowpoweraudiosink_prepare)后动态设置。

**起始版本：** 20

**参数：**

参数项描述[OH_LowPowerAudioSink](OH_LowPowerAudioSink.md)* sink指向OH_LowPowerAudioSink实例的指针。const [OH_AVFormat](OH_AVFormat.md)* format指向OH_AVFormat的指针，为LowPowerAudioSink设置的参数。

**返回：**

类型说明[OH_AVErrCode](native_averrors.h.md#ZH-CN_TOPIC_0000002497605740__oh_averrcode)

AV_ERR_OK：执行成功。

 AV_ERR_INVALID_VAL：参数为nullptr或参数非法。

 AV_ERR_UNSUPPORT：不支持的格式。

 AV_ERR_SERVICE_DIED：媒体服务端已销毁。

 AV_ERR_OPERATE_NOT_PERMIT：操作不支持。

#### OH_LowPowerAudioSink_GetParameter()

```ets
OH_AVErrCode OH_LowPowerAudioSink_GetParameter(OH_LowPowerAudioSink* sink, OH_AVFormat* format)
```

**描述**

获取LowPowerAudioSink的相关参数。

**起始版本：** 20

**参数：**

参数项描述[OH_LowPowerAudioSink](OH_LowPowerAudioSink.md)* sink指向LowPowerAudioSink实例的指针。[OH_AVFormat](OH_AVFormat.md)* format指向OH_AVFormat实例的指针。

**返回：**

类型说明[OH_AVErrCode](native_averrors.h.md#ZH-CN_TOPIC_0000002497605740__oh_averrcode)

AV_ERR_OK：执行成功。

 AV_ERR_INVALID_VAL：参数为nullptr或参数非法。

 AV_ERR_OPERATE_NOT_PERMIT：操作不支持。

#### OH_LowPowerAudioSink_Prepare()

```ets
OH_AVErrCode OH_LowPowerAudioSink_Prepare(OH_LowPowerAudioSink* sink)
```

**描述**

准备LowPowerAudioSink的解码、渲染资源，在[OH_LowPowerAudioSink_Configure](lowpower_audio_sink.h.md#ZH-CN_TOPIC_0000002529285909__oh_lowpoweraudiosink_configure)后调用。

 调用此接口前必须调用LowPowerVideoSink的[OH_LowPowerVideoSink_SetSyncAudioSink](lowpower_video_sink.h.md#ZH-CN_TOPIC_0000002497445940__oh_lowpowervideosink_setsyncaudiosink)方法。

**起始版本：** 20

**参数：**

参数项描述[OH_LowPowerAudioSink](OH_LowPowerAudioSink.md)* sink指向OH_LowPowerAudioSink实例的指针。

**返回：**

类型说明[OH_AVErrCode](native_averrors.h.md#ZH-CN_TOPIC_0000002497605740__oh_averrcode)

AV_ERR_OK：执行成功。

 AV_ERR_INVALID_VAL：参数为nullptr或参数非法。

 AV_ERR_UNSUPPORT：不支持的格式。

 AV_ERR_SERVICE_DIED：媒体服务端已销毁。

 AV_ERR_OPERATE_NOT_PERMIT：操作不支持。

#### OH_LowPowerAudioSink_Start()

```ets
OH_AVErrCode OH_LowPowerAudioSink_Start(OH_LowPowerAudioSink* sink)
```

**描述**

启动低功耗音频接收器，此接口必须在[OH_LowPowerAudioSink_Prepare](lowpower_audio_sink.h.md#ZH-CN_TOPIC_0000002529285909__oh_lowpoweraudiosink_prepare)成功后调用。

 启动成功后，LowPowerAudioSink将开始上报[OH_LowPowerAudioSink_OnDataNeeded](lowpower_audio_sink_base.h.md#ZH-CN_TOPIC_0000002529445883__oh_lowpoweraudiosink_ondataneeded)事件。

**起始版本：** 20

**参数：**

参数项描述[OH_LowPowerAudioSink](OH_LowPowerAudioSink.md)* sink指向OH_LowPowerAudioSink实例的指针。

**返回：**

类型说明[OH_AVErrCode](native_averrors.h.md#ZH-CN_TOPIC_0000002497605740__oh_averrcode)

AV_ERR_OK：执行成功。

 AV_ERR_INVALID_VAL：参数为nullptr或参数非法。

 AV_ERR_UNSUPPORT：不支持的格式。

 AV_ERR_SERVICE_DIED：媒体服务端已销毁。

 AV_ERR_OPERATE_NOT_PERMIT：操作不支持。

#### OH_LowPowerAudioSink_Pause()

```ets
OH_AVErrCode OH_LowPowerAudioSink_Pause(OH_LowPowerAudioSink* sink)
```

**描述**

暂停LowPowerAudioSink，在[OH_LowPowerAudioSink_Start](lowpower_audio_sink.h.md#ZH-CN_TOPIC_0000002529285909__oh_lowpoweraudiosink_start)或[OH_LowPowerAudioSink_Resume](lowpower_audio_sink.h.md#ZH-CN_TOPIC_0000002529285909__oh_lowpoweraudiosink_resume)后调用。

 暂停成功后，LowPowerAudioSink将暂停[OH_LowPowerAudioSink_OnDataNeeded](lowpower_audio_sink_base.h.md#ZH-CN_TOPIC_0000002529445883__oh_lowpoweraudiosink_ondataneeded)事件的上报。

**起始版本：** 20

**参数：**

参数项描述[OH_LowPowerAudioSink](OH_LowPowerAudioSink.md)* sink指向OH_LowPowerAudioSink实例的指针。

**返回：**

类型说明[OH_AVErrCode](native_averrors.h.md#ZH-CN_TOPIC_0000002497605740__oh_averrcode)

AV_ERR_OK：执行成功。

 AV_ERR_INVALID_VAL：参数为nullptr或参数非法。

 AV_ERR_SERVICE_DIED：媒体服务端已销毁。

 AV_ERR_OPERATE_NOT_PERMIT：操作不支持。

#### OH_LowPowerAudioSink_Resume()

```ets
OH_AVErrCode OH_LowPowerAudioSink_Resume(OH_LowPowerAudioSink* sink)
```

**描述**

恢复LowPowerAudioSink，在[OH_LowPowerAudioSink_Pause](lowpower_audio_sink.h.md#ZH-CN_TOPIC_0000002529285909__oh_lowpoweraudiosink_pause)后调用。

 恢复成功后，LowPowerAudioSink将恢复[OH_LowPowerAudioSink_OnDataNeeded](lowpower_audio_sink_base.h.md#ZH-CN_TOPIC_0000002529445883__oh_lowpoweraudiosink_ondataneeded)事件的上报。

**起始版本：** 20

**参数：**

参数项描述[OH_LowPowerAudioSink](OH_LowPowerAudioSink.md)* sink指向OH_LowPowerAudioSink实例的指针。

**返回：**

类型说明[OH_AVErrCode](native_averrors.h.md#ZH-CN_TOPIC_0000002497605740__oh_averrcode)

AV_ERR_OK：执行成功。

 AV_ERR_INVALID_VAL：参数为nullptr或参数非法。

 AV_ERR_SERVICE_DIED：媒体服务端已销毁。

 AV_ERR_OPERATE_NOT_PERMIT：操作不支持。

#### OH_LowPowerAudioSink_Flush()

```ets
OH_AVErrCode OH_LowPowerAudioSink_Flush(OH_LowPowerAudioSink* sink)
```

**描述**

清除LowPowerAudioSink中所有解码器和渲染缓存的输入输出数据。

 此接口不建议在[OH_LowPowerAudioSink_Start](lowpower_audio_sink.h.md#ZH-CN_TOPIC_0000002529285909__oh_lowpoweraudiosink_start)或[OH_LowPowerAudioSink_Resume](lowpower_audio_sink.h.md#ZH-CN_TOPIC_0000002529285909__oh_lowpoweraudiosink_resume)之后调用。

 需要注意的是，如果编解码器之前已输入数据，则需要重新输入编解码器数据。

**起始版本：** 20

**参数：**

参数项描述[OH_LowPowerAudioSink](OH_LowPowerAudioSink.md)* sink指向OH_LowPowerAudioSink实例的指针。

**返回：**

类型说明[OH_AVErrCode](native_averrors.h.md#ZH-CN_TOPIC_0000002497605740__oh_averrcode)

AV_ERR_OK：执行成功。

 AV_ERR_INVALID_VAL：参数为nullptr或参数非法。

 AV_ERR_SERVICE_DIED：媒体服务端已销毁。

 AV_ERR_OPERATE_NOT_PERMIT：操作不支持。

#### OH_LowPowerAudioSink_Stop()

```ets
OH_AVErrCode OH_LowPowerAudioSink_Stop(OH_LowPowerAudioSink* sink)
```

**描述**

停止LowPowerAudioSink。

**起始版本：** 20

**参数：**

参数项描述[OH_LowPowerAudioSink](OH_LowPowerAudioSink.md)* sink指向OH_LowPowerAudioSink实例的指针。

**返回：**

类型说明[OH_AVErrCode](native_averrors.h.md#ZH-CN_TOPIC_0000002497605740__oh_averrcode)

AV_ERR_OK：执行成功。

 AV_ERR_INVALID_VAL：参数为nullptr或参数非法。

 AV_ERR_SERVICE_DIED：媒体服务端已销毁。

 AV_ERR_OPERATE_NOT_PERMIT：操作不支持。

#### OH_LowPowerAudioSink_Reset()

```ets
OH_AVErrCode OH_LowPowerAudioSink_Reset(OH_LowPowerAudioSink* sink)
```

**描述**

重置LowPowerAudioSink。

 如果要重新使用该实例，需要调用[OH_LowPowerAudioSink_Configure](lowpower_audio_sink.h.md#ZH-CN_TOPIC_0000002529285909__oh_lowpoweraudiosink_configure)完成配置。

**起始版本：** 20

**参数：**

参数项描述[OH_LowPowerAudioSink](OH_LowPowerAudioSink.md)* sink指向OH_LowPowerAudioSink实例的指针。

**返回：**

类型说明[OH_AVErrCode](native_averrors.h.md#ZH-CN_TOPIC_0000002497605740__oh_averrcode)

AV_ERR_OK：执行成功。

 AV_ERR_INVALID_VAL：参数为nullptr或参数非法。

 AV_ERR_SERVICE_DIED：媒体服务端已销毁。

 AV_ERR_OPERATE_NOT_PERMIT：操作不支持。

#### OH_LowPowerAudioSink_Destroy()

```ets
OH_AVErrCode OH_LowPowerAudioSink_Destroy(OH_LowPowerAudioSink* sink)
```

**描述**

清理LowPowerAudioSink内部资源，销毁LowPowerAudioSink实例。不能重复销毁。

**起始版本：** 20

**参数：**

参数项描述[OH_LowPowerAudioSink](OH_LowPowerAudioSink.md)* sink指向OH_LowPowerAudioSink实例的指针。

**返回：**

类型说明[OH_AVErrCode](native_averrors.h.md#ZH-CN_TOPIC_0000002497605740__oh_averrcode)

AV_ERR_OK：执行成功。

 AV_ERR_INVALID_VAL：参数为nullptr或参数非法。

 AV_ERR_SERVICE_DIED：媒体服务端已销毁。

 AV_ERR_OPERATE_NOT_PERMIT：操作不支持。

#### OH_LowPowerAudioSink_SetVolume()

```ets
OH_AVErrCode OH_LowPowerAudioSink_SetVolume(OH_LowPowerAudioSink* sink, const float volume)
```

**描述**

为LowPowerAudioSink设置渲染音量。

**起始版本：** 20

**参数：**

参数项描述[OH_LowPowerAudioSink](OH_LowPowerAudioSink.md)* sink指向OH_LowPowerAudioSink实例的指针。const float volume音量值，取值范围[0.0, 1.0]。

**返回：**

类型说明[OH_AVErrCode](native_averrors.h.md#ZH-CN_TOPIC_0000002497605740__oh_averrcode)

AV_ERR_OK：执行成功。

 AV_ERR_INVALID_VAL：参数为nullptr或参数非法。

 AV_ERR_SERVICE_DIED：媒体服务端已销毁。

 AV_ERR_OPERATE_NOT_PERMIT：操作不支持。

#### OH_LowPowerAudioSink_SetLoudnessGain()

```ets
OH_AVErrCode OH_LowPowerAudioSink_SetLoudnessGain(OH_LowPowerAudioSink* sink, float loudnessGain)
```

**描述**

为LowPowerAudioSink设置播放响度。

**起始版本：** 21

**参数：**

参数项描述[OH_LowPowerAudioSink](OH_LowPowerAudioSink.md)* sink指向OH_LowPowerAudioSink实例的指针。float loudnessGain响度值，取值范围[-90.0, 24.0]。默认值为0.0dB。

**返回：**

类型说明[OH_AVErrCode](native_averrors.h.md#ZH-CN_TOPIC_0000002497605740__oh_averrcode)

AV_ERR_OK：执行成功。

 AV_ERR_INVALID_VAL：参数为nullptr或参数非法。

 AV_ERR_SERVICE_DIED：媒体服务端已销毁。

#### OH_LowPowerAudioSink_SetPlaybackSpeed()

```ets
OH_AVErrCode OH_LowPowerAudioSink_SetPlaybackSpeed(OH_LowPowerAudioSink* sink, const float speed)
```

**描述**

为LowPowerAudioSink设置音频渲染倍速。

**起始版本：** 20

**参数：**

参数项描述[OH_LowPowerAudioSink](OH_LowPowerAudioSink.md)* sink指向OH_LowPowerAudioSink实例的指针。const float speed音频渲染倍速值，取值范围[0.25, 4.0]。

**返回：**

类型说明[OH_AVErrCode](native_averrors.h.md#ZH-CN_TOPIC_0000002497605740__oh_averrcode)

AV_ERR_OK：执行成功。

 AV_ERR_INVALID_VAL：参数为nullptr或参数非法。

 AV_ERR_SERVICE_DIED：媒体服务端已销毁。

 AV_ERR_OPERATE_NOT_PERMIT：操作不支持。

#### OH_LowPowerAudioSink_ReturnSamples()

```ets
OH_AVErrCode OH_LowPowerAudioSink_ReturnSamples(OH_LowPowerAudioSink* sink, OH_AVSamplesBuffer* samples)
```

**描述**

给LowPowerAudioSink输入buffer。

**起始版本：** 20

**参数：**

参数项描述[OH_LowPowerAudioSink](OH_LowPowerAudioSink.md)* sink指向OH_LowPowerAudioSink实例的指针。[OH_AVSamplesBuffer](OH_AVSamplesBuffer.md)* samples需要送OH_AVSamplesBuffer消费的OH_AVSamplesBuffer实例，支持聚包输入。

**返回：**

类型说明[OH_AVErrCode](native_averrors.h.md#ZH-CN_TOPIC_0000002497605740__oh_averrcode)

AV_ERR_OK：执行成功。

 AV_ERR_INVALID_VAL：参数为nullptr或参数非法。

 AV_ERR_SERVICE_DIED：媒体服务端已销毁。

 AV_ERR_OPERATE_NOT_PERMIT：操作不支持。

#### OH_LowPowerAudioSink_RegisterCallback()

```ets
OH_AVErrCode OH_LowPowerAudioSink_RegisterCallback(OH_LowPowerAudioSink* sink, OH_LowPowerAudioSinkCallback* callback)
```

**描述**

为LowPowerAudioSink注册回调。

**起始版本：** 20

**参数：**

参数项描述[OH_LowPowerAudioSink](OH_LowPowerAudioSink.md)* sink指向OH_LowPowerAudioSink实例的指针。[OH_LowPowerAudioSinkCallback](OH_LowPowerAudioSinkCallback.md)* callback指向OH_LowPowerAudioSinkCallback实例的指针。

**返回：**

类型说明[OH_AVErrCode](native_averrors.h.md#ZH-CN_TOPIC_0000002497605740__oh_averrcode)

AV_ERR_OK：执行成功。

 AV_ERR_INVALID_VAL：参数为nullptr或参数非法。

 AV_ERR_SERVICE_DIED：媒体服务端已销毁。

 AV_ERR_OPERATE_NOT_PERMIT：操作不支持。

#### OH_LowPowerAudioSinkCallback_Create()

```ets
OH_LowPowerAudioSinkCallback* OH_LowPowerAudioSinkCallback_Create(void)
```

**描述**

创建OH_LowPowerAudioSinkCallback实例。

**起始版本：** 20

**返回：**

类型说明[OH_LowPowerAudioSinkCallback](OH_LowPowerAudioSinkCallback.md)*返回指向OH_LowPowerAudioSinkCallback实例的指针。如果内存不足，则返回nullptr。

#### OH_LowPowerAudioSinkCallback_Destroy()

```ets
OH_AVErrCode OH_LowPowerAudioSinkCallback_Destroy(OH_LowPowerAudioSinkCallback* callback)
```

**描述**

销毁OH_LowPowerAudioSinkCallback实例。

**起始版本：** 20

**参数：**

参数项描述[OH_LowPowerAudioSinkCallback](OH_LowPowerAudioSinkCallback.md)* callback指向OH_LowPowerAudioSinkCallback实例的指针。

**返回：**

类型说明[OH_AVErrCode](native_averrors.h.md#ZH-CN_TOPIC_0000002497605740__oh_averrcode)

AV_ERR_OK：执行成功。

 AV_ERR_INVALID_VAL：参数为nullptr或参数非法。

#### OH_LowPowerAudioSinkCallback_SetPositionUpdateListener()

```ets
OH_AVErrCode OH_LowPowerAudioSinkCallback_SetPositionUpdateListener(OH_LowPowerAudioSinkCallback* callback, OH_LowPowerAudioSink_OnPositionUpdated onPositionUpdated, void* userData)
```

**描述**

为LowPowerAudioSinkCallback设置进度更新监听。

**起始版本：** 20

**参数：**

参数项描述[OH_LowPowerAudioSinkCallback](OH_LowPowerAudioSinkCallback.md)* callback指向OH_LowPowerAudioSinkCallback实例的指针。[OH_LowPowerAudioSink_OnPositionUpdated](lowpower_audio_sink_base.h.md#ZH-CN_TOPIC_0000002529445883__oh_lowpoweraudiosink_onpositionupdated) onPositionUpdatedOH_LowPowerAudioSink_OnPositionUpdated方法，在PositionUpdate事件触发时调用。void* userData用户执行回调所依赖的数据。

**返回：**

类型说明[OH_AVErrCode](native_averrors.h.md#ZH-CN_TOPIC_0000002497605740__oh_averrcode)

AV_ERR_OK：执行成功。

 AV_ERR_INVALID_VAL：参数为nullptr或参数非法。

 AV_ERR_OPERATE_NOT_PERMIT：操作不支持。

#### OH_LowPowerAudioSinkCallback_SetDataNeededListener()

```ets
OH_AVErrCode OH_LowPowerAudioSinkCallback_SetDataNeededListener(OH_LowPowerAudioSinkCallback* callback, OH_LowPowerAudioSink_OnDataNeeded onDataNeeded, void* userData)
```

**描述**

为LowPowerAudioSinkCallback设置需要数据监听。

**起始版本：** 20

**参数：**

参数项描述[OH_LowPowerAudioSinkCallback](OH_LowPowerAudioSinkCallback.md)* callback指向OH_LowPowerAudioSinkCallback实例的指针。[OH_LowPowerAudioSink_OnDataNeeded](lowpower_audio_sink_base.h.md#ZH-CN_TOPIC_0000002529445883__oh_lowpoweraudiosink_ondataneeded) onDataNeededOH_LowPowerAudioSink_OnDataNeeded方法，在DataNeeded事件触发时调用。void* userData用户执行回调所依赖的数据。

**返回：**

类型说明[OH_AVErrCode](native_averrors.h.md#ZH-CN_TOPIC_0000002497605740__oh_averrcode)

AV_ERR_OK：执行成功。

 AV_ERR_INVALID_VAL：参数为nullptr或参数非法。

 AV_ERR_OPERATE_NOT_PERMIT：操作不支持。

#### OH_LowPowerAudioSinkCallback_SetErrorListener()

```ets
OH_AVErrCode OH_LowPowerAudioSinkCallback_SetErrorListener(OH_LowPowerAudioSinkCallback* callback, OH_LowPowerAudioSink_OnError onError, void* userData)
```

**描述**

为LowPowerAudioSinkCallback设置错误监听。

**起始版本：** 20

**参数：**

参数项描述[OH_LowPowerAudioSinkCallback](OH_LowPowerAudioSinkCallback.md)* callback指向OH_LowPowerAudioSinkCallback实例的指针。[OH_LowPowerAudioSink_OnError](lowpower_audio_sink_base.h.md#ZH-CN_TOPIC_0000002529445883__oh_lowpoweraudiosink_onerror) onErrorOH_LowPowerAudioSink_OnError方法，在Error事件触发时调用。void* userData用户执行回调所依赖的数据。

**返回：**

类型说明[OH_AVErrCode](native_averrors.h.md#ZH-CN_TOPIC_0000002497605740__oh_averrcode)

AV_ERR_OK：执行成功。

 AV_ERR_INVALID_VAL：参数为nullptr或参数非法。

 AV_ERR_OPERATE_NOT_PERMIT：操作不支持。

#### OH_LowPowerAudioSinkCallback_SetInterruptListener()

```ets
OH_AVErrCode OH_LowPowerAudioSinkCallback_SetInterruptListener(OH_LowPowerAudioSinkCallback* callback, OH_LowPowerAudioSink_OnInterrupted onInterrupted, void* userData)
```

**描述**

为LowPowerAudioSinkCallback设置音频焦点打断监听。

**起始版本：** 20

**参数：**

参数项描述[OH_LowPowerAudioSinkCallback](OH_LowPowerAudioSinkCallback.md)* callback指向OH_LowPowerAudioSinkCallback实例的指针。[OH_LowPowerAudioSink_OnInterrupted](lowpower_audio_sink_base.h.md#ZH-CN_TOPIC_0000002529445883__oh_lowpoweraudiosink_oninterrupted) onInterruptedOH_LowPowerAudioSink_OnInterrupted方法，在Interrupted事件触发时调用。void* userData用户执行回调所依赖的数据。

**返回：**

类型说明[OH_AVErrCode](native_averrors.h.md#ZH-CN_TOPIC_0000002497605740__oh_averrcode)

AV_ERR_OK：执行成功。

 AV_ERR_INVALID_VAL：参数为nullptr或参数非法。

 AV_ERR_OPERATE_NOT_PERMIT：操作不支持。

#### OH_LowPowerAudioSinkCallback_SetDeviceChangeListener()

```ets
OH_AVErrCode OH_LowPowerAudioSinkCallback_SetDeviceChangeListener(OH_LowPowerAudioSinkCallback* callback, OH_LowPowerAudioSink_OnDeviceChanged onDeviceChanged, void* userData)
```

**描述**

为LowPowerAudioSinkCallback设置音频设备切换监听。

**起始版本：** 20

**参数：**

参数项描述[OH_LowPowerAudioSinkCallback](OH_LowPowerAudioSinkCallback.md)* callback指向OH_LowPowerAudioSinkCallback实例的指针。[OH_LowPowerAudioSink_OnDeviceChanged](lowpower_audio_sink_base.h.md#ZH-CN_TOPIC_0000002529445883__oh_lowpoweraudiosink_ondevicechanged) onDeviceChangedOH_LowPowerAudioSink_OnDeviceChanged方法，在DeviceChanged事件触发时调用。void* userData用户执行回调所依赖的数据。

**返回：**

类型说明[OH_AVErrCode](native_averrors.h.md#ZH-CN_TOPIC_0000002497605740__oh_averrcode)

AV_ERR_OK：执行成功。

 AV_ERR_INVALID_VAL：参数为nullptr或参数非法。

 AV_ERR_OPERATE_NOT_PERMIT：操作不支持。

#### OH_LowPowerAudioSinkCallback_SetEosListener()

```ets
OH_AVErrCode OH_LowPowerAudioSinkCallback_SetEosListener(OH_LowPowerAudioSinkCallback *callback, OH_LowPowerAudioSink_OnEos onEos, void* userData)
```

**描述**

为LowPowerAudioSinkCallback设置播放完成监听。

**起始版本：** 20

**参数：**

参数项描述[OH_LowPowerAudioSinkCallback](OH_LowPowerAudioSinkCallback.md) *callback指向OH_LowPowerAudioSinkCallback实例的指针。[OH_LowPowerAudioSink_OnEos](lowpower_audio_sink_base.h.md#ZH-CN_TOPIC_0000002529445883__oh_lowpoweraudiosink_oneos) onEosOH_LowPowerAudioSink_OnEos方法，在Eos事件触发时调用。void* userData用户执行回调所依赖的数据。

**返回：**

类型说明[OH_AVErrCode](native_averrors.h.md#ZH-CN_TOPIC_0000002497605740__oh_averrcode)

AV_ERR_OK：执行成功。

 AV_ERR_INVALID_VAL：参数为nullptr或参数非法。

 AV_ERR_OPERATE_NOT_PERMIT：操作不支持。