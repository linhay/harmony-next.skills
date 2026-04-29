# lowpower_audio_sink_base.h

**概述**

定义LowPowerAudioSink的结构体和枚举。

引用文件： <multimedia/player_framework/lowpower_audio_sink_base.h>

库： liblowpower_avsink.so

系统能力： SystemCapability.Multimedia.Media.LowPowerAVSink

起始版本： 20

相关模块： [LowPowerAudioSink](LowPowerAudioSink.md)

**汇总**

**结构体**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| OH_LowPowerAudioSink | OH_LowPowerAudioSink | LowPowerAudioSink的声明。 |
| OH_LowPowerAudioSinkCallback | OH_LowPowerAudioSinkCallback | 包含了LowPowerAudioSink回调函数指针的集合。  应用需注册此实例结构体到OH_LowPowerAudioSink实例中，并对回调上报的信息进行处理，保证LowPowerAudioSink的正常运行。 |

**函数**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| typedef void (*OH_LowPowerAudioSink_OnError)(OH_LowPowerAudioSink* sink, OH_AVErrCode errCode, const char* errorMsg, void* userData) | OH_LowPowerAudioSink_OnError | LowPowerAudioSink发生错误时调用该方法。 |
| typedef void (*OH_LowPowerAudioSink_OnPositionUpdated)(OH_LowPowerAudioSink* sink, int64_t currentPosition, void* userData) | OH_LowPowerAudioSink_OnPositionUpdated | LowPowerAudioSink进度更新时调用该方法。 |
| typedef void (*OH_LowPowerAudioSink_OnDataNeeded)(OH_LowPowerAudioSink* sink, OH_AVSamplesBuffer* samples, void* userData) | OH_LowPowerAudioSink_OnDataNeeded | LowPowerAudioSink需要数据时调用该方法。 |
| typedef void (*OH_LowPowerAudioSink_OnInterrupted)(OH_LowPowerAudioSink* sink, OH_AudioInterrupt_ForceType type, OH_AudioInterrupt_Hint hint, void* userData) | OH_LowPowerAudioSink_OnInterrupted | LowPowerAudioSink焦点打断时调用该方法。 |
| typedef void (*OH_LowPowerAudioSink_OnDeviceChanged)(OH_LowPowerAudioSink* sink, OH_AudioStream_DeviceChangeReason reason, void* userData) | OH_LowPowerAudioSink_OnDeviceChanged | LowPowerAudioSink设备切换时调用该方法。 |
| typedef void (*OH_LowPowerAudioSink_OnEos)(OH_LowPowerAudioSink* sink, void* userData) | OH_LowPowerAudioSink_OnEos | LowPowerAudioSink播放完成时调用该方法，包含在OH_LowPowerAudioSinkCallback中。 |

**函数说明**

**OH_LowPowerAudioSink_OnError()**

```ets
typedef void (*OH_LowPowerAudioSink_OnError)(OH_LowPowerAudioSink* sink,OH_AVErrCode errCode,const char* errorMsg,void* userData)
```

描述

LowPowerAudioSink发生错误时调用该方法。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_LowPowerAudioSink* sink | 指向OH_LowPowerAudioSink实例的指针。 |
| OH_AVErrCode errorCode | 发生错误时上报的错误码。 |
| const char* errorMsg | 错误描述信息。 |
| void* userData | 用户自定义数据。 |

**OH_LowPowerAudioSink_OnPositionUpdated()**

```ets
typedef void (*OH_LowPowerAudioSink_OnPositionUpdated)(OH_LowPowerAudioSink* sink,int64_t currentPosition,void* userData)
```

描述

LowPowerAudioSink进度更新时调用该方法。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_LowPowerAudioSink* sink | 指向OH_LowPowerAudioSink实例的指针。 |
| int64_t currentPosition | 返回服务当前播放的进度值。 |
| void* userData | 用户自定义数据。 |

**OH_LowPowerAudioSink_OnDataNeeded()**

```ets
typedef void (*OH_LowPowerAudioSink_OnDataNeeded)(OH_LowPowerAudioSink* sink,OH_AVSamplesBuffer* samples,void* userData)
```

描述

LowPowerAudioSink需要数据时调用该方法。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_LowPowerAudioSink* sink | 指向OH_LowPowerAudioSink实例的指针。 |
| OH_AVSamplesBuffer* samples | 即将写入的AVSamplesBuffer实例。 |
| void* userData | 用户自定义数据。 |

**OH_LowPowerAudioSink_OnInterrupted()**

```ets
typedef void (*OH_LowPowerAudioSink_OnInterrupted)(OH_LowPowerAudioSink* sink,OH_AudioInterrupt_ForceType type,OH_AudioInterrupt_Hint hint,void* userData)
```

描述

LowPowerAudioSink焦点打断时调用该方法。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_LowPowerAudioSink* sink | 指向OH_LowPowerAudioSink实例的指针。 |
| OH_AudioInterrupt_ForceType type | 音频打断类型。 |
| OH_AudioInterrupt_Hint hint | 音频打断提示类型。 |
| void* userData | 用户自定义数据。 |

**OH_LowPowerAudioSink_OnDeviceChanged()**

```ets
typedef void (*OH_LowPowerAudioSink_OnDeviceChanged)(OH_LowPowerAudioSink* sink,OH_AudioStream_DeviceChangeReason reason,void* userData)
```

描述

LowPowerAudioSink设备切换时调用该方法。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_LowPowerAudioSink* sink | 指向OH_LowPowerAudioSink实例的指针。 |
| OH_AudioStream_DeviceChangeReason reason | 输出设备发生变化的原因。 |
| void* userData | 用户自定义数据。 |

**OH_LowPowerAudioSink_OnEos()**

```ets
typedef void (*OH_LowPowerAudioSink_OnEos)(OH_LowPowerAudioSink* sink, void* userData)
```

描述

LowPowerAudioSink播放完成时调用该方法，包含在[OH_LowPowerAudioSinkCallback](OH_LowPowerAudioSinkCallback.md)中。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_LowPowerAudioSink* sink | 指向OH_LowPowerAudioSink实例的指针。 |
| void* userData | 用户自定义数据。 |