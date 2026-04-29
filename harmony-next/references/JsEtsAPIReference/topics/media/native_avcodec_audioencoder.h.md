# native_avcodec_audioencoder.h

**概述**

音频编码Native API的声明。

引用文件： <multimedia/player_framework/native_avcodec_audioencoder.h>

库： libnative_media_aenc.so

系统能力： SystemCapability.Multimedia.Media.AudioEncoder

起始版本： 9

废弃版本： 11

替代建议： 当前模块下的接口均已废弃，开发者可使用[native_avcodec_audiocodec.h](native_avcodec_audiocodec.h.md)完成对应功能开发，单个接口的替代关系可查阅具体的接口说明。

相关模块： [AudioEncoder](AudioEncoder.md)

**汇总**

**函数**

| 名称 | 描述 |
| --- | --- |
| OH_AVCodec *OH_AudioEncoder_CreateByMime(const char *mime) | 根据MIME类型创建音频编码器实例，大多数场景下建议使用此方式。(API11废弃) |
| OH_AVCodec *OH_AudioEncoder_CreateByName(const char *name) | 通过音频编码器名称创建音频编码器实例，使用此接口的前提是知道编码器的确切名称。(API11废弃) |
| OH_AVErrCode OH_AudioEncoder_Destroy(OH_AVCodec *codec) | 清理编码器内部资源，销毁编码器实例。(API11废弃) |
| OH_AVErrCode OH_AudioEncoder_SetCallback(OH_AVCodec *codec, OH_AVCodecAsyncCallback callback, void *userData) | 设置异步回调函数，使应用可以响应音频编码器生成的事件。在调用Prepare之前，必须调用此接口。(API11废弃) |
| OH_AVErrCode OH_AudioEncoder_Configure(OH_AVCodec *codec, OH_AVFormat *format) | 要配置音频编码器，通常需要配置编码后的音轨的描述信息。在调用Prepare之前，必须调用此接口。(API11废弃) |
| OH_AVErrCode OH_AudioEncoder_Prepare(OH_AVCodec *codec) | 准备编码器的内部资源，在调用此接口之前必须调用Configure接口。(API11废弃) |
| OH_AVErrCode OH_AudioEncoder_Start(OH_AVCodec *codec) | 调用此接口启动编码器，在Prepare成功后执行。启动后，编码器将开始上报OH_AVCodecOnNeedInputData事件。(API11废弃) |
| OH_AVErrCode OH_AudioEncoder_Stop(OH_AVCodec *codec) | 停止编码器。停止后，您可以通过Start重新进入已启动状态。(API11废弃) |
| OH_AVErrCode OH_AudioEncoder_Flush(OH_AVCodec *codec) | 清除编码器中缓存的输入和输出数据。 调用此接口后，以前通过异步回调上报的所有缓冲区索引都将失效，请确保不要访问这些索引对应的缓冲区。(API11废弃) |
| OH_AVErrCode OH_AudioEncoder_Reset(OH_AVCodec *codec) | 重置编码器。如果要继续编码，需要再次调用Configure接口配置编码器实例。(API11废弃) |
| OH_AVFormat *OH_AudioEncoder_GetOutputDescription(OH_AVCodec *codec) | 获取编码器输出数据的描述信息。需要注意的是，返回值所指向的OH_AVFormat实例的生命周期需要调用者手动释放。(API11废弃) |
| OH_AVErrCode OH_AudioEncoder_SetParameter(OH_AVCodec *codec, OH_AVFormat *format) | 配置编码器的动态参数。 注意：该接口必须在编码器启动后才能调用。另外，参数配置错误可能会导致编码失败。(API11废弃) |
| OH_AVErrCode OH_AudioEncoder_PushInputData(OH_AVCodec *codec, uint32_t index, OH_AVCodecBufferAttr attr) | 通知音频编码器已完成对index所对应缓冲区进行输入数据的填充。 OH_AVCodecOnNeedInputData回调将报告可用的输入缓冲区和相应的索引值。一旦具有指定索引的缓冲区提交到音频编码器，则无法再次访问此缓冲区，直到再次收到OH_AVCodecOnNeedInputData回调，收到相同索引时此缓冲区才可使用。 此外，对于某些编码器，需要在开始时向编码器输入特定配置参数，以初始化编码器的编码过程。(API11废弃) |
| OH_AVErrCode OH_AudioEncoder_FreeOutputData(OH_AVCodec *codec, uint32_t index) | 将处理后的输出缓冲区返回给编码器。(API11废弃) |
| OH_AVErrCode OH_AudioEncoder_IsValid(OH_AVCodec *codec, bool *isValid) | 检查当前编码器实例是否有效，可用于后台故障恢复或应用程序从后台恢复时检测编码器有效状态。(API11废弃) |

**函数说明**

**OH_AudioEncoder_CreateByMime()**

```ets
OH_AVCodec *OH_AudioEncoder_CreateByMime(const char *mime)
```

描述

根据MIME类型创建音频编码器实例，大多数场景下建议使用此方式。

系统能力： SystemCapability.Multimedia.Media.AudioEncoder

起始版本： 9

废弃版本： 11

替代接口： [OH_AudioCodec_CreateByMime](native_avcodec_audiocodec.h.md#ZH-CN_TOPIC_0000002522241856__oh_audiocodec_createbymime)

参数：

| 参数项 | 描述 |
| --- | --- |
| const char *mime | mime类型描述字符串，请参阅AVCODEC_MIMETYPE。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_AVCodec * | 返回指向OH_AVCodec实例的指针。 |

**OH_AudioEncoder_CreateByName()**

```ets
OH_AVCodec *OH_AudioEncoder_CreateByName(const char *name)
```

描述

通过音频编码器名称创建音频编码器实例，使用此接口的前提是知道编码器的确切名称。

系统能力： SystemCapability.Multimedia.Media.AudioEncoder

起始版本： 9

废弃版本： 11

替代接口： [OH_AudioCodec_CreateByName](native_avcodec_audiocodec.h.md#ZH-CN_TOPIC_0000002522241856__oh_audiocodec_createbyname)

参数：

| 参数项 | 描述 |
| --- | --- |
| const char *name | 音频编码器名称。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_AVCodec * | 返回指向OH_AVCodec实例的指针。 |

**OH_AudioEncoder_Destroy()**

```ets
OH_AVErrCode OH_AudioEncoder_Destroy(OH_AVCodec *codec)
```

描述

清理编码器内部资源，销毁编码器实例。

系统能力： SystemCapability.Multimedia.Media.AudioEncoder

起始版本： 9

废弃版本： 11

替代接口： [OH_AudioCodec_Destroy](native_avcodec_audiocodec.h.md#ZH-CN_TOPIC_0000002522241856__oh_audiocodec_destroy)

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVCodec *codec | 指向OH_AVCodec实例的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_AVErrCode | 如果执行成功，则返回AV_ERR_OK，否则返回特定错误代码。 |

**OH_AudioEncoder_SetCallback()**

```ets
OH_AVErrCode OH_AudioEncoder_SetCallback(OH_AVCodec *codec, OH_AVCodecAsyncCallback callback, void *userData)
```

描述

设置异步回调函数，使应用可以响应音频编码器生成的事件。在调用Prepare之前，必须调用此接口。

系统能力： SystemCapability.Multimedia.Media.AudioEncoder

起始版本： 9

废弃版本： 11

替代接口： [OH_AudioCodec_RegisterCallback](native_avcodec_audiocodec.h.md#ZH-CN_TOPIC_0000002522241856__oh_audiocodec_registercallback)

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVCodec *codec | 指向OH_AVCodec实例的指针。 |
| OH_AVCodecAsyncCallback callback | 所有回调函数的集合。 |
| void *userData | 用户特定数据。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_AVErrCode | 如果执行成功，则返回AV_ERR_OK，否则返回特定错误代码。 |

**OH_AudioEncoder_Configure()**

```ets
OH_AVErrCode OH_AudioEncoder_Configure(OH_AVCodec *codec, OH_AVFormat *format)
```

描述

要配置音频编码器，通常需要配置编码后的音轨的描述信息。在调用Prepare之前，必须调用此接口。

系统能力： SystemCapability.Multimedia.Media.AudioEncoder

起始版本： 9

废弃版本： 11

替代接口： [OH_AudioCodec_Configure](native_avcodec_audiocodec.h.md#ZH-CN_TOPIC_0000002522241856__oh_audiocodec_configure)

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVCodec *codec | 指向OH_AVCodec实例的指针。 |
| OH_AVFormat *format | 指向OH_AVFormat的指针，给出要编码的音频轨道的描述。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_AVErrCode | 如果执行成功，则返回AV_ERR_OK，否则返回特定错误代码。 |

**OH_AudioEncoder_Prepare()**

```ets
OH_AVErrCode OH_AudioEncoder_Prepare(OH_AVCodec *codec)
```

描述

准备编码器的内部资源，在调用此接口之前必须调用Configure接口。

系统能力： SystemCapability.Multimedia.Media.AudioEncoder

起始版本： 9

废弃版本： 11

替代接口： [OH_AudioCodec_Prepare](native_avcodec_audiocodec.h.md#ZH-CN_TOPIC_0000002522241856__oh_audiocodec_prepare)

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVCodec *codec | 指向OH_AVCodec实例的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_AVErrCode | 如果执行成功，则返回AV_ERR_OK，否则返回特定错误代码。 |

**OH_AudioEncoder_Start()**

```ets
OH_AVErrCode OH_AudioEncoder_Start(OH_AVCodec *codec)
```

描述

调用此接口启动编码器，在Prepare成功后执行。启动后，编码器将开始上报OH_AVCodecOnNeedInputData事件。

系统能力： SystemCapability.Multimedia.Media.AudioEncoder

起始版本： 9

废弃版本： 11

替代接口： [OH_AudioCodec_Start](native_avcodec_audiocodec.h.md#ZH-CN_TOPIC_0000002522241856__oh_audiocodec_start)

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVCodec *codec | 指向OH_AVCodec实例的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_AVErrCode | 如果执行成功，则返回AV_ERR_OK，否则返回特定错误代码。 |

**OH_AudioEncoder_Stop()**

```ets
OH_AVErrCode OH_AudioEncoder_Stop(OH_AVCodec *codec)
```

描述

停止编码器。停止后，您可以通过Start重新进入已启动状态。

系统能力： SystemCapability.Multimedia.Media.AudioEncoder

起始版本： 9

废弃版本： 11

替代接口： [OH_AudioCodec_Stop](native_avcodec_audiocodec.h.md#ZH-CN_TOPIC_0000002522241856__oh_audiocodec_stop)

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVCodec *codec | 指向OH_AVCodec实例的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_AVErrCode | 如果执行成功，则返回AV_ERR_OK，否则返回特定错误代码。 |

**OH_AudioEncoder_Flush()**

```ets
OH_AVErrCode OH_AudioEncoder_Flush(OH_AVCodec *codec)
```

描述

清除编码器中缓存的输入和输出数据。

调用此接口后，以前通过异步回调上报的所有缓冲区索引都将失效，请确保不要访问这些索引对应的缓冲区。

系统能力： SystemCapability.Multimedia.Media.AudioEncoder

起始版本： 9

废弃版本： 11

替代接口： [OH_AudioCodec_Flush](native_avcodec_audiocodec.h.md#ZH-CN_TOPIC_0000002522241856__oh_audiocodec_flush)

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVCodec *codec | 指向OH_AVCodec实例的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_AVErrCode | 如果执行成功，则返回AV_ERR_OK，否则返回特定错误代码。 |

**OH_AudioEncoder_Reset()**

```ets
OH_AVErrCode OH_AudioEncoder_Reset(OH_AVCodec *codec)
```

描述

重置编码器。如果要继续编码，需要再次调用Configure接口配置编码器实例。

系统能力： SystemCapability.Multimedia.Media.AudioEncoder

起始版本： 9

废弃版本： 11

替代接口： [OH_AudioCodec_Reset](native_avcodec_audiocodec.h.md#ZH-CN_TOPIC_0000002522241856__oh_audiocodec_reset)

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVCodec *codec | 指向OH_AVCodec实例的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_AVErrCode | 如果执行成功，则返回AV_ERR_OK，否则返回特定错误代码。 |

**OH_AudioEncoder_GetOutputDescription()**

```ets
OH_AVFormat *OH_AudioEncoder_GetOutputDescription(OH_AVCodec *codec)
```

描述

获取编码器输出数据的描述信息。需要注意的是，返回值所指向的OH_AVFormat实例的生命周期需要调用者手动释放。

系统能力： SystemCapability.Multimedia.Media.AudioEncoder

起始版本： 9

废弃版本： 11

替代接口： [OH_AudioCodec_GetOutputDescription](native_avcodec_audiocodec.h.md#ZH-CN_TOPIC_0000002522241856__oh_audiocodec_getoutputdescription)

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVCodec *codec | 指向OH_AVCodec实例的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_AVFormat * | 返回OH_AVFormat句柄指针，生命周期将使用下一个GetOutputDescription刷新，或使用OH_AVCodec销毁。 |

**OH_AudioEncoder_SetParameter()**

```ets
OH_AVErrCode OH_AudioEncoder_SetParameter(OH_AVCodec *codec, OH_AVFormat *format)
```

描述

配置编码器的动态参数。

注意：该接口必须在编码器启动后才能调用。另外，参数配置错误可能会导致编码失败。

系统能力： SystemCapability.Multimedia.Media.AudioEncoder

起始版本： 9

废弃版本： 11

替代接口： [OH_AudioCodec_SetParameter](native_avcodec_audiocodec.h.md#ZH-CN_TOPIC_0000002522241856__oh_audiocodec_setparameter)

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVCodec *codec | 指向OH_AVCodec实例的指针。 |
| OH_AVFormat *format | OH_AVFormat句柄指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_AVErrCode | 如果执行成功，则返回AV_ERR_OK，否则返回特定错误代码。 |

**OH_AudioEncoder_PushInputData()**

```ets
OH_AVErrCode OH_AudioEncoder_PushInputData(OH_AVCodec *codec, uint32_t index, OH_AVCodecBufferAttr attr)
```

描述

通知音频编码器已完成对index所对应缓冲区进行输入数据的填充。

[OH_AVCodecOnNeedInputData](native_avcodec_base.h.md#ZH-CN_TOPIC_0000002553201823__oh_avcodeconneedinputdata)回调将报告可用的输入缓冲区和相应的索引值。一旦具有指定索引的缓冲区提交到音频编码器，则无法再次访问此缓冲区，直到再次收到[OH_AVCodecOnNeedInputData](native_avcodec_base.h.md#ZH-CN_TOPIC_0000002553201823__oh_avcodeconneedinputdata)回调，收到相同索引时此缓冲区才可使用。

此外，对于某些编码器，需要在开始时向编码器输入特定配置参数，以初始化编码器的编码过程。

系统能力： SystemCapability.Multimedia.Media.AudioEncoder

起始版本： 9

废弃版本： 11

替代接口： [OH_AudioCodec_PushInputBuffer](native_avcodec_audiocodec.h.md#ZH-CN_TOPIC_0000002522241856__oh_audiocodec_pushinputbuffer)

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVCodec *codec | 指向OH_AVCodec实例的指针。 |
| uint32_t index | 输入缓冲区Buffer对应的索引值。 |
| OH_AVCodecBufferAttr attr | 描述缓冲区中包含的数据的信息。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_AVErrCode | 如果执行成功，则返回AV_ERR_OK，否则返回特定错误代码。 |

**OH_AudioEncoder_FreeOutputData()**

```ets
OH_AVErrCode OH_AudioEncoder_FreeOutputData(OH_AVCodec *codec, uint32_t index)
```

描述

将处理后的输出缓冲区返回给编码器。

系统能力： SystemCapability.Multimedia.Media.AudioEncoder

起始版本： 9

废弃版本： 11

替代接口： [OH_AudioCodec_FreeOutputBuffer](native_avcodec_audiocodec.h.md#ZH-CN_TOPIC_0000002522241856__oh_audiocodec_freeoutputbuffer)

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVCodec *codec | 指向OH_AVCodec实例的指针。 |
| uint32_t index | 输出缓冲区Buffer对应的索引值。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_AVErrCode | 如果执行成功，则返回AV_ERR_OK，否则返回特定错误代码。 |

**OH_AudioEncoder_IsValid()**

```ets
OH_AVErrCode OH_AudioEncoder_IsValid(OH_AVCodec *codec, bool *isValid)
```

描述

检查当前编码器实例是否有效，可用于后台故障恢复或应用程序从后台恢复时检测编码器有效状态。

系统能力： SystemCapability.Multimedia.Media.AudioEncoder

起始版本： 10

废弃版本： 11

替代接口： [OH_AudioCodec_IsValid](native_avcodec_audiocodec.h.md#ZH-CN_TOPIC_0000002522241856__oh_audiocodec_isvalid)

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVCodec *codec | 指向OH_AVCodec实例的指针。 |
| bool *isValid | 指向布尔类型的指针，true：编码器实例有效，false：编码器实例无效。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_AVErrCode | 如果执行成功，则返回AV_ERR_OK，否则返回特定错误代码。 |