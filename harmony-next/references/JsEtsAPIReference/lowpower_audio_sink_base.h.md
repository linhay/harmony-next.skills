# lowpower_audio_sink_base.h

#### 概述

定义LowPowerAudioSink的结构体和枚举。

**引用文件：** <multimedia/player_framework/lowpower_audio_sink_base.h>

**库：** liblowpower_avsink.so

**系统能力：** SystemCapability.Multimedia.Media.LowPowerAVSink

**起始版本：** 20

**相关模块：**[LowPowerAudioSink](LowPowerAudioSink.md)

#### 汇总

#### 结构体

名称typedef关键字描述[OH_LowPowerAudioSink](OH_LowPowerAudioSink.md)OH_LowPowerAudioSinkLowPowerAudioSink的声明。[OH_LowPowerAudioSinkCallback](OH_LowPowerAudioSinkCallback.md)OH_LowPowerAudioSinkCallback

包含了LowPowerAudioSink回调函数指针的集合。

 应用需注册此实例结构体到[OH_LowPowerAudioSink](OH_LowPowerAudioSink.md)实例中，并对回调上报的信息进行处理，保证LowPowerAudioSink的正常运行。

#### 函数

名称typedef关键字描述[typedef void (*OH_LowPowerAudioSink_OnError)(OH_LowPowerAudioSink* sink, OH_AVErrCode errCode, const char* errorMsg, void* userData)](#ZH-CN_TOPIC_0000002529445883__oh_lowpoweraudiosink_onerror)OH_LowPowerAudioSink_OnErrorLowPowerAudioSink发生错误时调用该方法。[typedef void (*OH_LowPowerAudioSink_OnPositionUpdated)(OH_LowPowerAudioSink* sink, int64_t currentPosition, void* userData)](#ZH-CN_TOPIC_0000002529445883__oh_lowpoweraudiosink_onpositionupdated)OH_LowPowerAudioSink_OnPositionUpdatedLowPowerAudioSink进度更新时调用该方法。[typedef void (*OH_LowPowerAudioSink_OnDataNeeded)(OH_LowPowerAudioSink* sink, OH_AVSamplesBuffer* samples, void* userData)](#ZH-CN_TOPIC_0000002529445883__oh_lowpoweraudiosink_ondataneeded)OH_LowPowerAudioSink_OnDataNeededLowPowerAudioSink需要数据时调用该方法。[typedef void (*OH_LowPowerAudioSink_OnInterrupted)(OH_LowPowerAudioSink* sink, OH_AudioInterrupt_ForceType type, OH_AudioInterrupt_Hint hint, void* userData)](#ZH-CN_TOPIC_0000002529445883__oh_lowpoweraudiosink_oninterrupted)OH_LowPowerAudioSink_OnInterruptedLowPowerAudioSink焦点打断时调用该方法。[typedef void (*OH_LowPowerAudioSink_OnDeviceChanged)(OH_LowPowerAudioSink* sink, OH_AudioStream_DeviceChangeReason reason, void* userData)](#ZH-CN_TOPIC_0000002529445883__oh_lowpoweraudiosink_ondevicechanged)OH_LowPowerAudioSink_OnDeviceChangedLowPowerAudioSink设备切换时调用该方法。[typedef void (*OH_LowPowerAudioSink_OnEos)(OH_LowPowerAudioSink* sink, void* userData)](#ZH-CN_TOPIC_0000002529445883__oh_lowpoweraudiosink_oneos)OH_LowPowerAudioSink_OnEosLowPowerAudioSink播放完成时调用该方法，包含在[OH_LowPowerAudioSinkCallback](zh-cn_topic_0000002497605940.html)中。

#### 函数说明

#### OH_LowPowerAudioSink_OnError()

```ets
typedef void (*OH_LowPowerAudioSink_OnError)(OH_LowPowerAudioSink* sink,OH_AVErrCode errCode,const char* errorMsg,void* userData)
```

**描述**

LowPowerAudioSink发生错误时调用该方法。

**起始版本：** 20

**参数：**

参数项描述[OH_LowPowerAudioSink](OH_LowPowerAudioSink.md)* sink指向OH_LowPowerAudioSink实例的指针。[OH_AVErrCode](native_averrors.h.md#ZH-CN_TOPIC_0000002497605740__oh_averrcode) errorCode发生错误时上报的错误码。const char* errorMsg错误描述信息。void* userData用户自定义数据。

#### OH_LowPowerAudioSink_OnPositionUpdated()

```ets
typedef void (*OH_LowPowerAudioSink_OnPositionUpdated)(OH_LowPowerAudioSink* sink,int64_t currentPosition,void* userData)
```

**描述**

LowPowerAudioSink进度更新时调用该方法。

**起始版本：** 20

**参数：**

参数项描述[OH_LowPowerAudioSink](OH_LowPowerAudioSink.md)* sink指向OH_LowPowerAudioSink实例的指针。int64_t currentPosition返回服务当前播放的进度值。void* userData用户自定义数据。

#### OH_LowPowerAudioSink_OnDataNeeded()

```ets
typedef void (*OH_LowPowerAudioSink_OnDataNeeded)(OH_LowPowerAudioSink* sink,OH_AVSamplesBuffer* samples,void* userData)
```

**描述**

LowPowerAudioSink需要数据时调用该方法。

**起始版本：** 20

**参数：**

参数项描述[OH_LowPowerAudioSink](OH_LowPowerAudioSink.md)* sink指向OH_LowPowerAudioSink实例的指针。[OH_AVSamplesBuffer](OH_AVSamplesBuffer.md)* samples即将写入的AVSamplesBuffer实例。void* userData用户自定义数据。

#### OH_LowPowerAudioSink_OnInterrupted()

```ets
typedef void (*OH_LowPowerAudioSink_OnInterrupted)(OH_LowPowerAudioSink* sink,OH_AudioInterrupt_ForceType type,OH_AudioInterrupt_Hint hint,void* userData)
```

**描述**

LowPowerAudioSink焦点打断时调用该方法。

**起始版本：** 20

**参数：**

参数项描述[OH_LowPowerAudioSink](OH_LowPowerAudioSink.md)* sink指向OH_LowPowerAudioSink实例的指针。[OH_AudioInterrupt_ForceType](native_audiostream_base.h.md#ZH-CN_TOPIC_0000002529445679__oh_audiointerrupt_forcetype) type音频打断类型。[OH_AudioInterrupt_Hint](native_audiostream_base.h.md#ZH-CN_TOPIC_0000002529445679__oh_audiointerrupt_hint) hint音频打断提示类型。void* userData用户自定义数据。

#### OH_LowPowerAudioSink_OnDeviceChanged()

```ets
typedef void (*OH_LowPowerAudioSink_OnDeviceChanged)(OH_LowPowerAudioSink* sink,OH_AudioStream_DeviceChangeReason reason,void* userData)
```

**描述**

LowPowerAudioSink设备切换时调用该方法。

**起始版本：** 20

**参数：**

参数项描述[OH_LowPowerAudioSink](OH_LowPowerAudioSink.md)* sink指向OH_LowPowerAudioSink实例的指针。[OH_AudioStream_DeviceChangeReason](native_audiostream_base.h.md#ZH-CN_TOPIC_0000002529445679__oh_audiostream_devicechangereason) reason输出设备发生变化的原因。void* userData用户自定义数据。

#### OH_LowPowerAudioSink_OnEos()

```ets
typedef void (*OH_LowPowerAudioSink_OnEos)(OH_LowPowerAudioSink* sink, void* userData)
```

**描述**

LowPowerAudioSink播放完成时调用该方法，包含在[OH_LowPowerAudioSinkCallback](OH_LowPowerAudioSinkCallback.md)中。

**起始版本：** 20

**参数：**

参数项描述[OH_LowPowerAudioSink](OH_LowPowerAudioSink.md)* sink指向OH_LowPowerAudioSink实例的指针。void* userData用户自定义数据。