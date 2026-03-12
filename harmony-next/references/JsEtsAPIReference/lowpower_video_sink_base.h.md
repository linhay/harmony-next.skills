# lowpower_video_sink_base.h

#### 概述

定义LowPowerVideoSink的结构体和枚举。

**引用文件：** <multimedia/player_framework/lowpower_video_sink_base.h>

**库：** liblowpower_avsink.so

**系统能力：** SystemCapability.Multimedia.Media.LowPowerAVSink

**起始版本：** 20

**相关模块：**[LowPowerVideoSink](LowPowerVideoSink.md)

#### 汇总

#### 结构体

名称typedef关键字描述[OH_LowPowerVideoSink](OH_LowPowerVideoSink.md)OH_LowPowerVideoSinkLowPowerVideoSink声明。[OH_LowPowerVideoSinkCallback](OH_LowPowerVideoSinkCallback.md)OH_LowPowerVideoSinkCallback

包含了LowPowerVideoSink回调函数指针的集合。

 应用需注册此实例结构体到[OH_LowPowerVideoSink](OH_LowPowerVideoSink.md)实例中，并对回调上报的信息进行处理，保证LowPowerVideoSink的正常运行。

#### 函数

名称typedef关键字描述[typedef void (*OH_LowPowerVideoSink_OnDataNeeded)(OH_LowPowerVideoSink* sink, OH_AVSamplesBuffer* buffer, void *userData)](#ZH-CN_TOPIC_0000002529285911__oh_lowpowervideosink_ondataneeded)OH_LowPowerVideoSink_OnDataNeededLowPowerVideoSink需要数据时调用该方法，包含在[OH_LowPowerVideoSinkCallback](zh-cn_topic_0000002529445905.html)中。[typedef void (*OH_LowPowerVideoSink_OnError)(OH_LowPowerVideoSink* sink, OH_AVErrCode errCode, const char* errMsg, void* userData)](#ZH-CN_TOPIC_0000002529285911__oh_lowpowervideosink_onerror)OH_LowPowerVideoSink_OnErrorLowPowerVideoSink发生错误时调用该方法。[typedef void (*OH_LowPowerVideoSink_OnTargetArrived)(OH_LowPowerVideoSink* sink, const int64_t targetPts, const bool isTimeout, void* userData)](#ZH-CN_TOPIC_0000002529285911__oh_lowpowervideosink_ontargetarrived)OH_LowPowerVideoSink_OnTargetArrivedLowPowerVideoSink到达目标点时调用该方法，包含在[OH_LowPowerVideoSinkCallback](zh-cn_topic_0000002529445905.html)中。[typedef void (*OH_LowPowerVideoSink_OnRenderStarted)(OH_LowPowerVideoSink* sink, void* userData)](#ZH-CN_TOPIC_0000002529285911__oh_lowpowervideosink_onrenderstarted)OH_LowPowerVideoSink_OnRenderStartedLowPowerVideoSink开始渲染时调用该方法，包含在[OH_LowPowerVideoSinkCallback](zh-cn_topic_0000002529445905.html)中。[typedef void (*OH_LowPowerVideoSink_OnStreamChanged)(OH_LowPowerVideoSink* sink, OH_AVFormat* format, void* userData)](#ZH-CN_TOPIC_0000002529285911__oh_lowpowervideosink_onstreamchanged)OH_LowPowerVideoSink_OnStreamChangedLowPowerVideoSink流切换调用该方法，包含在[OH_LowPowerVideoSinkCallback](zh-cn_topic_0000002529445905.html)中。[typedef void (*OH_LowPowerVideoSink_OnFirstFrameDecoded)(OH_LowPowerVideoSink* sink, void* userData)](#ZH-CN_TOPIC_0000002529285911__oh_lowpowervideosink_onfirstframedecoded)OH_LowPowerVideoSink_OnFirstFrameDecodedLowPowerVideoSink第一帧解码成功时调用该方法，包含在[OH_LowPowerVideoSinkCallback](zh-cn_topic_0000002529445905.html)中。[typedef void (*OH_LowPowerVideoSink_OnEos)(OH_LowPowerVideoSink* sink, void* userData)](#ZH-CN_TOPIC_0000002529285911__oh_lowpowervideosink_oneos)OH_LowPowerVideoSink_OnEosLowPowerVideoSink播放完成时调用该方法，包含在[OH_LowPowerVideoSinkCallback](zh-cn_topic_0000002529445905.html)中。

#### 函数说明

#### OH_LowPowerVideoSink_OnDataNeeded()

```ets
typedef void (*OH_LowPowerVideoSink_OnDataNeeded)(OH_LowPowerVideoSink* sink,OH_AVSamplesBuffer* buffer,void *userData)
```

**描述**

LowPowerVideoSink需要数据时调用该方法，包含在[OH_LowPowerVideoSinkCallback](OH_LowPowerVideoSinkCallback.md)中。

**起始版本：** 20

**参数：**

参数项描述[OH_LowPowerVideoSink](OH_LowPowerVideoSink.md)* sink指向OH_LowPowerVideoSink实例的指针。[OH_AVSamplesBuffer](OH_AVSamplesBuffer.md)* buffer指向OH_AVSamplesBuffer实例的指针。void *userData用户执行回调所依赖的数据。

#### OH_LowPowerVideoSink_OnError()

```ets
typedef void (*OH_LowPowerVideoSink_OnError)(OH_LowPowerVideoSink* sink,OH_AVErrCode errCode,const char* errMsg,void* userData)
```

**描述**

LowPowerVideoSink发生错误时调用该方法。

**起始版本：** 20

**参数：**

参数项描述[OH_LowPowerVideoSink](OH_LowPowerVideoSink.md)* sink指向OH_LowPowerVideoSink实例的指针。[OH_AVErrCode](native_averrors.h.md#ZH-CN_TOPIC_0000002497605740__oh_averrcode) errCode业务操作过程中发生错误时返回的错误码。const char* errMsg业务操作过程中发生错误时返回的错误描述信息。void* userData用户执行回调所依赖的数据。

#### OH_LowPowerVideoSink_OnTargetArrived()

```ets
typedef void (*OH_LowPowerVideoSink_OnTargetArrived)(OH_LowPowerVideoSink* sink,const int64_t targetPts,const bool isTimeout,void* userData)
```

**描述**

LowPowerVideoSink到达目标点时调用该方法，包含在[OH_LowPowerVideoSinkCallback](OH_LowPowerVideoSinkCallback.md)中。

**起始版本：** 20

**参数：**

参数项描述[OH_LowPowerVideoSink](OH_LowPowerVideoSink.md)* sink指向OH_LowPowerVideoSink实例的指针。const int64_t targetPts目标点的pts。const bool isTimeout表示等待目标点是否超时。若为true，表示等待目标点超时；若为false，则表示未超时。void* userData用户执行回调所依赖的数据。

#### OH_LowPowerVideoSink_OnRenderStarted()

```ets
typedef void (*OH_LowPowerVideoSink_OnRenderStarted)(OH_LowPowerVideoSink* sink, void* userData)
```

**描述**

LowPowerVideoSink开始渲染时调用该方法，包含在[OH_LowPowerVideoSinkCallback](OH_LowPowerVideoSinkCallback.md)中。

**起始版本：** 20

**参数：**

参数项描述[OH_LowPowerVideoSink](OH_LowPowerVideoSink.md)* sink指向OH_LowPowerVideoSink实例的指针。void* userData用户执行回调所依赖的数据。

#### OH_LowPowerVideoSink_OnStreamChanged()

```ets
typedef void (*OH_LowPowerVideoSink_OnStreamChanged)(OH_LowPowerVideoSink* sink, OH_AVFormat* format, void* userData)
```

**描述**

LowPowerVideoSink流切换调用该方法，包含在[OH_LowPowerVideoSinkCallback](OH_LowPowerVideoSinkCallback.md)中。

**起始版本：** 20

**参数：**

参数项描述[OH_LowPowerVideoSink](OH_LowPowerVideoSink.md)* sink指向OH_LowPowerVideoSink实例的指针。[OH_AVFormat](OH_AVFormat.md)* format包含变化的参数和对应的值。void* userData用户执行回调所依赖的数据。

#### OH_LowPowerVideoSink_OnFirstFrameDecoded()

```ets
typedef void (*OH_LowPowerVideoSink_OnFirstFrameDecoded)(OH_LowPowerVideoSink* sink, void* userData)
```

**描述**

LowPowerVideoSink第一帧解码成功时调用该方法，包含在[OH_LowPowerVideoSinkCallback](OH_LowPowerVideoSinkCallback.md)中。

**起始版本：** 20

**参数：**

参数项描述[OH_LowPowerVideoSink](OH_LowPowerVideoSink.md)* sink指向OH_LowPowerVideoSink实例的指针。void* userData用户执行回调所依赖的数据。

#### OH_LowPowerVideoSink_OnEos()

```ets
typedef void (*OH_LowPowerVideoSink_OnEos)(OH_LowPowerVideoSink* sink, void* userData)
```

**描述**

LowPowerVideoSink播放完成时调用该方法，包含在[OH_LowPowerVideoSinkCallback](OH_LowPowerVideoSinkCallback.md)中。

**起始版本：** 20

**参数：**

参数项描述[OH_LowPowerVideoSink](OH_LowPowerVideoSink.md)* sink指向OH_LowPowerVideoSink实例的指针。void* userData用户执行回调所依赖的数据。