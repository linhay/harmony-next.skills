# native_avcodec_audiocodec.h

**概述**

音频编解码Native API的声明。

引用文件： <multimedia/player_framework/native_avcodec_audiocodec.h>

库： libnative_media_acodec.so

系统能力： SystemCapability.Multimedia.Media.AudioCodec

起始版本： 11

相关模块： [AudioCodec](AudioCodec.md)

相关示例： [AVCodec](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/BasicFeature/Media/AVCodec)

**汇总**

**结构体**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| MediaKeySession | MediaKeySession | MediaKeySession字段。 |

**函数**

| 名称 | 描述 |
| --- | --- |
| OH_AVCodec *OH_AudioCodec_CreateByMime(const char *mime, bool isEncoder) | 根据MIME类型创建音频编解码器实例，大多数场景下建议使用此方式。 |
| OH_AVCodec *OH_AudioCodec_CreateByName(const char *name) | 通过音频编解码器名称创建音频编解码器实例，使用此接口的前提是知道编解码器的确切名称，编解码器的名称可以通过OH_AVCapability_GetName获取。 |
| OH_AVErrCode OH_AudioCodec_Destroy(OH_AVCodec *codec) | 清理编解码器内部资源，销毁编解码器实例。注意不能进行重复销毁，否则将会导致程序崩溃。 |
| OH_AVErrCode OH_AudioCodec_RegisterCallback(OH_AVCodec *codec, OH_AVCodecCallback callback, void *userData) | 设置异步回调函数，使应用可以响应音频编解码器生成的事件。在调用Prepare之前，必须调用此接口。 |
| OH_AVErrCode OH_AudioCodec_Configure(OH_AVCodec *codec, const OH_AVFormat *format) | 配置音频描述信息。音频编解码器通常会根据音频描述信息进行配置。在调用Prepare之前，必须调用此接口。 |
| OH_AVErrCode OH_AudioCodec_Prepare(OH_AVCodec *codec) | 准备编解码器的内部资源，在调用此接口之前必须调用Configure接口。 |
| OH_AVErrCode OH_AudioCodec_Start(OH_AVCodec *codec) | 调用此接口启动编解码器，在Prepare成功后执行。启动后，编解码器将开始上报OH_AVCodecOnNeedInputBuffer事件。 |
| OH_AVErrCode OH_AudioCodec_Stop(OH_AVCodec *codec) | 停止编解码器。停止后，可以通过Start重新进入已启动状态（started），但需要注意的是，如果编解码器之前已输入数据，则需要重新输入编解码器数据。 |
| OH_AVErrCode OH_AudioCodec_Flush(OH_AVCodec *codec) | 清除编解码器中缓存的输入和输出数据。调用此接口后，以前通过异步回调上报的所有缓冲区索引都将失效，请确保不要访问这些索引对应的缓冲区。 |
| OH_AVErrCode OH_AudioCodec_Reset(OH_AVCodec *codec) | 重置编解码器。此时会清空已配置的参数和输入输出数据。  如果要继续编解码，需要再次调用Configure接口配置编解码器实例。 |
| OH_AVFormat *OH_AudioCodec_GetOutputDescription(OH_AVCodec *codec) | 获取编解码器输出数据的OH_AVFormat信息。  需要注意的是，返回值所指向的OH_AVFormat实例需要开发者调用OH_AVFormat_Destroy接口手动释放。 |
| OH_AVErrCode OH_AudioCodec_SetParameter(OH_AVCodec *codec, const OH_AVFormat *format) | 配置编解码器的动态参数。  注意，该接口必须在编解码器启动后才能调用。另外，参数配置错误可能会导致编解码失败。 |
| OH_AVErrCode OH_AudioCodec_PushInputBuffer(OH_AVCodec *codec, uint32_t index) | 通知音频编解码器已完成对index所对应缓冲区进行输入数据的填充。  OH_AVCodecOnNeedInputBuffer回调将报告可用的输入缓冲区和对应的索引值。  一旦具有指定索引的缓冲区被提交给音频编解码器，该缓冲区将无法再次访问，直到再次收到OH_AVCodecOnNeedInputBuffer回调，收到相同索引时此缓冲区才可使用。  此外，对于某些编解码器，需要在开始时向编解码器输入编解码特定配置数据(Codec-Specific-Data)，以初始化编解码器的编解码过程。  注意：当返回值为AV_ERR_UNKNOWN时此次调用不生效，输入缓冲区仍为未处理状态，需根据返回的特定错误代码处理后输入相同的index重新调用OH_AudioCodec_PushInputBuffer。 |
| OH_AVErrCode OH_AudioCodec_FreeOutputBuffer(OH_AVCodec *codec, uint32_t index) | 将处理后的输出缓冲区返回给编解码器。使用完输出缓冲区后需及时调用此接口进行释放，否则会阻塞编解码流程。 |
| OH_AVErrCode OH_AudioCodec_IsValid(OH_AVCodec *codec, bool *isValid) | 检查当前编解码器实例是否有效。  可用于后台故障恢复或应用程序从后台恢复时检测编解码器有效状态。 |
| OH_AVErrCode OH_AudioCodec_SetDecryptionConfig(OH_AVCodec *codec, MediaKeySession *mediaKeySession, bool secureAudio) | 设置解密信息。 |
| OH_AVErrCode OH_AudioCodec_QueryInputBuffer(struct OH_AVCodec *codec, uint32_t *index, int64_t timeoutUs) | 在设置的超时时间内，尝试查询对应音频编解码器可用的输入缓冲区的索引值。  获取到索引值后，使用OH_AudioCodec_GetInputBuffer接口获取索引值对应的缓冲区。  在缓冲区填充数据后，使用OH_AudioCodec_PushInputBuffer输入对应索引值，将缓冲区数据送到编解码器。  注意：此接口仅可在音频编解码的同步模式中使用。 |
| OH_AVBuffer *OH_AudioCodec_GetInputBuffer(struct OH_AVCodec *codec, uint32_t index) | 输入索引值，获取对应音频编解码器中该索引值对应的输入缓冲区。注意：此接口仅可在音频编解码的同步模式中使用。 |
| OH_AVErrCode OH_AudioCodec_QueryOutputBuffer(struct OH_AVCodec *codec, uint32_t *index, int64_t timeoutUs) | 在设置的超时时间内，尝试查询对应音频编解码器可用的输出缓冲区的索引值。获取到索引值后，通过OH_AudioCodec_GetOutputBuffer接口获取的输出缓冲区使用完后，  需要调用OH_AudioCodec_FreeOutputBuffer接口进行释放。释放后无法再次使用，长期不释放会阻塞编解码流程。注意：此接口仅可在音频编解码的同步模式中使用。 |
| OH_AVBuffer *OH_AudioCodec_GetOutputBuffer(struct OH_AVCodec *codec, uint32_t index) | 输入索引值，获取对应音频编解码器中该索引值对应的输出缓冲区。注意：此接口仅可在音频编解码的同步模式中使用。 |

**函数说明**

**OH_AudioCodec_CreateByMime()**

```ets
OH_AVCodec *OH_AudioCodec_CreateByMime(const char *mime, bool isEncoder)
```

描述

根据MIME类型创建音频编解码器实例，大多数场景下建议使用此方式。

系统能力： SystemCapability.Multimedia.Media.AudioCodec

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| const char *mime | MIME类型描述字符串，请参阅AVCODEC_MIMETYPE。 |
| bool isEncoder | true表示需要创建编码器，false表示需要创建解码器。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_AVCodec * | 返回OH_AVCodec实例的指针。 |

**OH_AudioCodec_CreateByName()**

```ets
OH_AVCodec *OH_AudioCodec_CreateByName(const char *name)
```

描述

通过音频编解码器名称创建音频编解码器实例，使用此接口的前提是知道编解码器的确切名称，编解码器的名称可以通过[OH_AVCapability_GetName](native_avcapability.h.md#ZH-CN_TOPIC_0000002553361779__oh_avcapability_getname)获取。

系统能力： SystemCapability.Multimedia.Media.AudioCodec

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| const char *name | 音频编解码器名称。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_AVCodec * | 返回OH_AVCodec实例的指针。 |

**OH_AudioCodec_Destroy()**

```ets
OH_AVErrCode OH_AudioCodec_Destroy(OH_AVCodec *codec)
```

描述

清理编解码器内部资源，销毁编解码器实例。注意不能进行重复销毁，否则将会导致程序崩溃。

系统能力： SystemCapability.Multimedia.Media.AudioCodec

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVCodec *codec | 指向OH_AVCodec实例的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_AVErrCode | AV_ERR_OK：执行成功。  AV_ERR_INVALID_VAL：OH_AVCodec实例为nullptr或无效。  AV_ERR_INVALID_STATE：编解码器服务不可用。  AV_ERR_NO_MEMORY：内部资源已经释放。  AV_ERR_UNKNOWN：发生内部错误，建议检查日志。 |

**OH_AudioCodec_RegisterCallback()**

```ets
OH_AVErrCode OH_AudioCodec_RegisterCallback(OH_AVCodec *codec, OH_AVCodecCallback callback, void *userData)
```

描述

设置异步回调函数，使应用可以响应音频编解码器生成的事件。在调用Prepare之前，必须调用此接口。

系统能力： SystemCapability.Multimedia.Media.AudioCodec

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVCodec *codec | 指向OH_AVCodec实例的指针。 |
| OH_AVCodecCallback callback | 所有回调函数的集合。 |
| void *userData | 用户特定数据。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_AVErrCode | AV_ERR_OK：执行成功。  AV_ERR_INVALID_VAL：输入参数为nullptr或无效。  AV_ERR_INVALID_STATE：编解码器服务不可用。 |

**OH_AudioCodec_Configure()**

```ets
OH_AVErrCode OH_AudioCodec_Configure(OH_AVCodec *codec, const OH_AVFormat *format)
```

描述

配置音频描述信息。音频编解码器通常会根据音频描述信息进行配置。在调用Prepare之前，必须调用此接口。

系统能力： SystemCapability.Multimedia.Media.AudioCodec

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVCodec *codec | 指向OH_AVCodec实例的指针。 |
| const OH_AVFormat *format | 指向OH_AVFormat的指针，给出要编解码的音频轨道的描述。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_AVErrCode | AV_ERR_OK：执行成功。  AV_ERR_INVALID_VAL：输入参数为nullptr或无效。  AV_ERR_INVALID_STATE：编解码器服务不可用。  AV_ERR_OPERATE_NOT_PERMIT：不允许操作，这可能是由于状态不正确或不支持的操作。  AV_ERR_UNKNOWN：发生内部错误，建议检查日志。 |

**OH_AudioCodec_Prepare()**

```ets
OH_AVErrCode OH_AudioCodec_Prepare(OH_AVCodec *codec)
```

描述

准备编解码器的内部资源，在调用此接口之前必须调用Configure接口。

系统能力： SystemCapability.Multimedia.Media.AudioCodec

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVCodec *codec | 指向OH_AVCodec实例的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_AVErrCode | AV_ERR_OK：执行成功。  AV_ERR_INVALID_VAL：OH_AVCodec实例为nullptr或无效。  AV_ERR_INVALID_STATE：编解码器服务不可用。  AV_ERR_OPERATE_NOT_PERMIT：不允许操作，这可能是由于状态不正确或不支持的操作。  AV_ERR_UNKNOWN：发生内部错误，建议检查日志。 |

**OH_AudioCodec_Start()**

```ets
OH_AVErrCode OH_AudioCodec_Start(OH_AVCodec *codec)
```

描述

调用此接口启动编解码器，在Prepare成功后执行。启动后，编解码器将开始上报OH_AVCodecOnNeedInputBuffer事件。

系统能力： SystemCapability.Multimedia.Media.AudioCodec

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVCodec *codec | 指向OH_AVCodec实例的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_AVErrCode | AV_ERR_OK：执行成功。  AV_ERR_INVALID_VAL：OH_AVCodec实例为nullptr或无效。  AV_ERR_INVALID_STATE：编解码器服务不可用。  AV_ERR_OPERATE_NOT_PERMIT：不允许操作，这可能是由于状态不正确或不支持的操作。  AV_ERR_UNKNOWN：发生内部错误，建议检查日志。 |

**OH_AudioCodec_Stop()**

```ets
OH_AVErrCode OH_AudioCodec_Stop(OH_AVCodec *codec)
```

描述

停止编解码器。停止后，可以通过Start重新进入已启动状态（started），但需要注意的是，如果编解码器之前已输入数据，则需要重新输入编解码器数据。

系统能力： SystemCapability.Multimedia.Media.AudioCodec

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVCodec *codec | 指向OH_AVCodec实例的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_AVErrCode | AV_ERR_OK：执行成功。  AV_ERR_INVALID_VAL：OH_AVCodec实例为nullptr或无效。  AV_ERR_INVALID_STATE：编解码器服务不可用。  AV_ERR_OPERATE_NOT_PERMIT：不允许操作，这可能是由于状态不正确或不支持的操作。  AV_ERR_UNKNOWN：发生内部错误，建议检查日志。 |

**OH_AudioCodec_Flush()**

```ets
OH_AVErrCode OH_AudioCodec_Flush(OH_AVCodec *codec)
```

描述

清除编解码器中缓存的输入和输出数据。调用此接口后，以前通过异步回调上报的所有缓冲区索引都将失效，请确保不要访问这些索引对应的缓冲区。

系统能力： SystemCapability.Multimedia.Media.AudioCodec

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVCodec *codec | 指向OH_AVCodec实例的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_AVErrCode | AV_ERR_OK：执行成功。  AV_ERR_INVALID_VAL：OH_AVCodec实例为nullptr或无效。  AV_ERR_INVALID_STATE：编解码器服务不可用。  AV_ERR_OPERATE_NOT_PERMIT：不允许操作，这可能是由于状态不正确或不支持的操作。  AV_ERR_UNKNOWN：发生内部错误，建议检查日志。 |

**OH_AudioCodec_Reset()**

```ets
OH_AVErrCode OH_AudioCodec_Reset(OH_AVCodec *codec)
```

描述

重置编解码器。此时会清空已配置的参数和输入输出数据。

 如果要继续编解码，需要再次调用Configure接口配置编解码器实例。

系统能力： SystemCapability.Multimedia.Media.AudioCodec

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVCodec *codec | 指向OH_AVCodec实例的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_AVErrCode | AV_ERR_OK：执行成功。  AV_ERR_INVALID_VAL：OH_AVCodec实例为nullptr或无效。  AV_ERR_INVALID_STATE：编解码器服务不可用。 |

**OH_AudioCodec_GetOutputDescription()**

```ets
OH_AVFormat *OH_AudioCodec_GetOutputDescription(OH_AVCodec *codec)
```

描述

获取编解码器输出数据的OH_AVFormat信息。

 需要注意的是，返回值所指向的OH_AVFormat实例需要开发者调用[OH_AVFormat_Destroy](native_avformat.h.md#ZH-CN_TOPIC_0000002553361783__oh_avformat_destroy)接口手动释放。

系统能力： SystemCapability.Multimedia.Media.AudioCodec

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVCodec *codec | 指向OH_AVCodec实例的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_AVFormat * | 返回OH_AVFormat句柄指针，生命周期将使用下一个OH_AudioCodec_GetOutputDescription刷新，或使用OH_AVCodec销毁。 |

**OH_AudioCodec_SetParameter()**

```ets
OH_AVErrCode OH_AudioCodec_SetParameter(OH_AVCodec *codec, const OH_AVFormat *format)
```

描述

配置编解码器的动态参数。

 注意，该接口必须在编解码器启动后才能调用。另外，参数配置错误可能会导致编解码失败。

系统能力： SystemCapability.Multimedia.Media.AudioCodec

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVCodec *codec | 指向OH_AVCodec实例的指针。 |
| const OH_AVFormat *format | OH_AVFormat句柄指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_AVErrCode | AV_ERR_OK：执行成功。  AV_ERR_INVALID_VAL：输入参数为nullptr或无效。  AV_ERR_INVALID_STATE：编解码器服务不可用。  AV_ERR_OPERATE_NOT_PERMIT：不允许操作，这可能是由于状态不正确或不支持的操作。  AV_ERR_UNKNOWN：发生内部错误，建议检查日志。 |

**OH_AudioCodec_PushInputBuffer()**

```ets
OH_AVErrCode OH_AudioCodec_PushInputBuffer(OH_AVCodec *codec, uint32_t index)
```

描述

通知音频编解码器已完成对index所对应缓冲区进行输入数据的填充。

 [OH_AVCodecOnNeedInputBuffer](native_avcodec_base.h.md#ZH-CN_TOPIC_0000002553201823__oh_avcodeconneedinputbuffer)回调将报告可用的输入缓冲区和对应的索引值。

 一旦具有指定索引的缓冲区被提交给音频编解码器，该缓冲区将无法再次访问，直到再次收到[OH_AVCodecOnNeedInputBuffer](native_avcodec_base.h.md#ZH-CN_TOPIC_0000002553201823__oh_avcodeconneedinputbuffer)回调，收到相同索引时此缓冲区才可使用。

 此外，对于某些编解码器，需要在开始时向编解码器输入编解码特定配置数据(Codec-Specific-Data)，以初始化编解码器的编解码过程。

 注意：当返回值为AV_ERR_UNKNOWN时此次调用不生效，输入缓冲区仍为未处理状态，需根据返回的特定错误代码处理后输入相同的index重新调用OH_AudioCodec_PushInputBuffer。

系统能力： SystemCapability.Multimedia.Media.AudioCodec

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVCodec *codec | 指向OH_AVCodec实例的指针。 |
| uint32_t index | 输入回调OH_AVCodecOnNeedInputBuffer给出的索引值。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_AVErrCode | AV_ERR_OK：执行成功。  AV_ERR_INVALID_VAL：输入的index已使用或无效，需使用其他OH_AVCodecOnNeedInputBuffer回调返回的index。  AV_ERR_INVALID_STATE：编解码器状态错误，调用OH_AudioCodec_PushInputBuffer前需确保按顺序成功调用OH_AudioCodec_Configure、OH_AudioCodec_Prepare、OH_AudioCodec_Start。  AV_ERR_UNKNOWN：输入buffer size无效，需确保buffer设置了正确的buffer size和flags。 |

**OH_AudioCodec_FreeOutputBuffer()**

```ets
OH_AVErrCode OH_AudioCodec_FreeOutputBuffer(OH_AVCodec *codec, uint32_t index)
```

描述

将处理后的输出缓冲区返回给编解码器。使用完输出缓冲区后需及时调用此接口进行释放，否则会阻塞编解码流程。

系统能力： SystemCapability.Multimedia.Media.AudioCodec

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVCodec *codec | 指向OH_AVCodec实例的指针。 |
| uint32_t index | 输出OH_AVCodecOnNewOutputBuffer给出的索引值。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_AVErrCode | AV_ERR_OK：执行成功。  AV_ERR_INVALID_VAL：输入参数为nullptr或无效。缓冲区索引应该由OH_AVCodecOnNewOutputBuffer给出。  AV_ERR_INVALID_STATE：编解码器服务不可用。  AV_ERR_OPERATE_NOT_PERMIT：不允许操作，这可能是由于状态不正确或不支持的操作。  AV_ERR_UNKNOWN：发生内部错误，建议检查日志。 |

**OH_AudioCodec_IsValid()**

```ets
OH_AVErrCode OH_AudioCodec_IsValid(OH_AVCodec *codec, bool *isValid)
```

描述

检查当前编解码器实例是否有效。

 可用于后台故障恢复或应用程序从后台恢复时检测编解码器有效状态。

系统能力： SystemCapability.Multimedia.Media.AudioCodec

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVCodec *codec | 指向OH_AVCodec实例的指针。 |
| bool *isValid | 输出参数。指向布尔类型的指针，true：编解码器实例有效，false：编解码器实例无效。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_AVErrCode | AV_ERR_OK：执行成功。  AV_ERR_INVALID_VAL：输入参数为nullptr或无效。 |

**OH_AudioCodec_SetDecryptionConfig()**

```ets
OH_AVErrCode OH_AudioCodec_SetDecryptionConfig(OH_AVCodec *codec, MediaKeySession *mediaKeySession,bool secureAudio)
```

描述

设置解密信息。

系统能力： SystemCapability.Multimedia.Media.AudioCodec

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVCodec *codec | 指向OH_AVCodec实例的指针。 |
| MediaKeySession *mediaKeySession | 带有解密功能的媒体秘钥会话实例。 |
| bool secureAudio | 是否使用安全解码器。使用安全解码器为true,否则为false。  注意：当前音频解密尚不支持使用安全解码器。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_AVErrCode | AV_ERR_OK：执行成功。  AV_ERR_INVALID_VAL：OH_AVCodec实例为nullptr或无效，mediaKeySystemInfo实例为nullptr或无效。  AV_ERR_INVALID_STATE：编解码器服务不可用。  AV_ERR_NO_MEMORY：请求内存失败。 |

**OH_AudioCodec_QueryInputBuffer()**

```ets
OH_AVErrCode OH_AudioCodec_QueryInputBuffer(struct OH_AVCodec *codec, uint32_t *index, int64_t timeoutUs)
```

描述

在设置的超时时间内，尝试查询对应音频编解码器可用的输入缓冲区的索引值。

 获取到索引值后，使用[OH_AudioCodec_GetInputBuffer](#ZH-CN_TOPIC_0000002522241856__oh_audiocodec_getinputbuffer)接口获取索引值对应的缓冲区。

 在缓冲区填充数据后，使用[OH_AudioCodec_PushInputBuffer](#ZH-CN_TOPIC_0000002522241856__oh_audiocodec_pushinputbuffer)输入对应索引值，将缓冲区数据送到编解码器。

 注意：此接口仅可在音频编解码的同步模式中使用。

系统能力： SystemCapability.Multimedia.Media.AudioCodec

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| struct OH_AVCodec *codec | 指向OH_AVCodec实例的指针。 |
| uint32_t *index | 输出参数，获取到的输入缓冲区的索引值。 |
| int64_t timeoutUs | 超时时间，单位：微秒。设置为负值时表示无限等待。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_AVErrCode | AV_ERR_OK：执行成功。  AV_ERR_INVALID_VAL：执行失败，输入参数错误。  AV_ERR_INVALID_STATE：执行失败，状态非法，没有启动编解码器等。  AV_ERR_OPERATE_NOT_PERMIT：执行失败，不允许非同步模式下调用。  AV_ERR_TRY_AGAIN_LATER：执行失败，超时时间内获取不到可用的缓冲区。 |

**OH_AudioCodec_GetInputBuffer()**

```ets
OH_AVBuffer *OH_AudioCodec_GetInputBuffer(struct OH_AVCodec *codec, uint32_t index)
```

描述

输入索引值，获取对应音频编解码器中该索引值对应的输入缓冲区。注意：此接口仅可在音频编解码的同步模式中使用。

系统能力： SystemCapability.Multimedia.Media.AudioCodec

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| struct OH_AVCodec *codec | 指向OH_AVCodec实例的指针。 |
| uint32_t index | 输入缓冲区的索引值。该索引值通过接口OH_AudioCodec_QueryInputBuffer获取。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_AVBuffer * | 如果执行成功，则返回一个指向OH_AVBuffer实例的指针，否则返回NULL。 |

**OH_AudioCodec_QueryOutputBuffer()**

```ets
OH_AVErrCode OH_AudioCodec_QueryOutputBuffer(struct OH_AVCodec *codec, uint32_t *index, int64_t timeoutUs)
```

描述

在设置的超时时间内，尝试查询对应音频编解码器可用的输出缓冲区的索引值。获取到索引值后，通过[OH_AudioCodec_GetOutputBuffer](#ZH-CN_TOPIC_0000002522241856__oh_audiocodec_getoutputbuffer)接口获取的输出缓冲区使用完后，

 需要调用[OH_AudioCodec_FreeOutputBuffer](#ZH-CN_TOPIC_0000002522241856__oh_audiocodec_freeoutputbuffer)接口进行释放。释放后无法再次使用，长期不释放会阻塞编解码流程。注意：此接口仅可在音频编解码的同步模式中使用。

系统能力： SystemCapability.Multimedia.Media.AudioCodec

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| struct OH_AVCodec *codec | 指向OH_AVCodec实例的指针。 |
| uint32_t *index | 输出参数，获取到的输出缓冲区的索引值。 |
| int64_t timeoutUs | 超时时间，单位：微秒。设置为负值时表示无限等待。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_AVErrCode | AV_ERR_OK：执行成功。  AV_ERR_INVALID_VAL：执行失败，输入参数错误。  AV_ERR_INVALID_STATE：执行失败，状态非法，没有启动编解码器等。  AV_ERR_OPERATE_NOT_PERMIT：执行失败，不允许非同步模式下调用。  AV_ERR_STREAM_CHANGED：解码输出流格式发生变化, 可以通过调用OH_AudioCodec_GetOutputDescription接口获取新的流信息。  AV_ERR_TRY_AGAIN_LATER：执行失败，超时时间内获取不到可用的缓冲区。 |

**OH_AudioCodec_GetOutputBuffer()**

```ets
OH_AVBuffer *OH_AudioCodec_GetOutputBuffer(struct OH_AVCodec *codec, uint32_t index)
```

描述

输入索引值，获取对应音频编解码器中该索引值对应的输出缓冲区。注意：此接口仅可在音频编解码的同步模式中使用。

系统能力： SystemCapability.Multimedia.Media.AudioCodec

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| struct OH_AVCodec *codec | 指向OH_AVCodec实例的指针。 |
| uint32_t index | 输出缓冲区的索引值。该索引值通过接口OH_AudioCodec_QueryOutputBuffer获取。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_AVBuffer * | 如果执行成功，则返回一个指向OH_AVBuffer实例的指针，否则返回NULL。 |