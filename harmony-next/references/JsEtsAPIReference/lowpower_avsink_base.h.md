# lowpower_avsink_base.h

#### 概述

定义OH_LowPowerAudioSink和OH_LowPowerVideoSink的基础依赖。

**引用文件：** <multimedia/player_framework/lowpower_avsink_base.h>

**库：** liblowpower_avsink.so

**系统能力：** SystemCapability.Multimedia.Media.LowPowerAVSink

**起始版本：** 20

**相关模块：**[AVSinkBase](AVSinkBase.md)

#### 汇总

#### 结构体

名称typedef关键字描述[OH_AVSamplesBuffer](OH_AVSamplesBuffer.md)OH_AVSamplesBufferLowPowerAVSink输入数据的结构体。应用在收到DataNeeded回调后需要将数据打包装进OH_AVSamplesBuffer实例中送给对应的lowpower_avsink。

#### 函数

名称描述[OH_AVErrCode OH_AVSamplesBuffer_AppendOneBuffer(OH_AVSamplesBuffer *samplesBuffer, OH_AVBuffer *avBuffer)](#ZH-CN_TOPIC_0000002497605920__oh_avsamplesbuffer_appendonebuffer)将一个OH_AVBuffer中的数据添加到OH_AVSamplesBuffer实例中。[int32_t OH_AVSamplesBuffer_GetRemainedCapacity(OH_AVSamplesBuffer *samplesBuffer)](#ZH-CN_TOPIC_0000002497605920__oh_avsamplesbuffer_getremainedcapacity)获取OH_AVSamplesBuffer实例的剩余可使用容量。[OH_LowPowerAVSink_Capability *OH_LowPowerAVSink_GetCapability()](#ZH-CN_TOPIC_0000002497605920__oh_lowpoweravsink_getcapability)

获取Lpp播放器能力。该函数的主要作用是获取当前低功耗播放器所支持的功能和媒体格式。

 通过调用此函数，可以了解设备在音频或视频处理方面的支持能力，例如支持的编码格式、解码格式、码率范围等。

#### 函数说明

#### OH_AVSamplesBuffer_AppendOneBuffer()

```ets
OH_AVErrCode OH_AVSamplesBuffer_AppendOneBuffer(OH_AVSamplesBuffer *samplesBuffer, OH_AVBuffer *avBuffer)
```

**描述**

将一个OH_AVBuffer中的数据添加到OH_AVSamplesBuffer实例中。

**起始版本：** 20

**参数：**

参数项描述[OH_AVSamplesBuffer](OH_AVSamplesBuffer.md) *samplesBuffer指向OH_AVSamplesBuffer实例的指针。[OH_AVBuffer](OH_AVBuffer.md) *avBuffer指向OH_AVBuffer实例的指针。

**返回：**

类型说明[OH_AVErrCode](native_averrors.h.md#ZH-CN_TOPIC_0000002497605740__oh_averrcode)

AV_ERR_OK：执行成功。

 AV_ERR_INVALID_VAL：参数为nullptr或参数非法。

 AV_ERR_NO_MEMORY：framePacketBuffer没有足够的剩余容量来追加一个OH_AVBuffer。

 AV_ERR_UNKNOWN：未知错误。

#### OH_AVSamplesBuffer_GetRemainedCapacity()

```ets
int32_t OH_AVSamplesBuffer_GetRemainedCapacity(OH_AVSamplesBuffer *samplesBuffer)
```

**描述**

获取OH_AVSamplesBuffer实例的剩余可使用容量。

**起始版本：** 20

**参数：**

参数项描述[OH_AVSamplesBuffer](OH_AVSamplesBuffer.md) *samplesBuffer指向OH_AVSamplesBuffer实例的指针。

**返回：**

类型说明int32_tOH_AVSamplesBuffer实例剩余可使用容量，单位为字节。如果sampleBuffer或data poniter为nullptr或无效，则返回-1。

#### OH_LowPowerAVSink_GetCapability()

```ets
OH_LowPowerAVSink_Capability *OH_LowPowerAVSink_GetCapability()
```

**描述**

获取Lpp播放器能力。该函数的主要作用是获取当前低功耗播放器所支持的功能和媒体格式。

 通过调用此函数，可以了解设备在音频或视频处理方面的支持能力，例如支持的编码格式、解码格式、码率范围等。

**起始版本：** 21

**返回：**

类型说明OH_LowPowerAVSink_Capability *

OH_LowPowerAVSink_Capability：支持Lpp播放器。

 nullptr：不支持Lpp播放器或者获取失败。