# native_avmuxer.h

**概述**

声明用于音视频封装的Native API。

引用文件： <multimedia/player_framework/native_avmuxer.h>

库： libnative_media_avmuxer.so

系统能力： SystemCapability.Multimedia.Media.Muxer

起始版本： 10

相关模块： [AVMuxer](AVMuxer.md)

相关示例：[AVCodec](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/BasicFeature/Media/AVCodec)

**汇总**

**结构体**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| OH_AVMuxer | OH_AVMuxer | 定义封装接口native层对象类型。 |

**函数**

| 名称 | 描述 |
| --- | --- |
| OH_AVMuxer *OH_AVMuxer_Create(int32_t fd, OH_AVOutputFormat format) | 通过文件描述符fd和封装格式创建OH_AVMuxer实例。 |
| OH_AVErrCode OH_AVMuxer_SetRotation(OH_AVMuxer *muxer, int32_t rotation) | 设置视频的旋转角度（顺时针，且旋转角度必须为0、90、180或270）。该接口必须在OH_AVMuxer_Start前调用。 |
| OH_AVErrCode OH_AVMuxer_SetFormat(OH_AVMuxer *muxer, OH_AVFormat *format) | 设置format数据到封装器。  API version 14起，支持设置创建时间OH_MD_KEY_CREATION_TIME。若创建时间未写入成功，请排查OH_MD_KEY_CREATION_TIME字符串设置是否符合ISO 8601标准的时间格式且为UTC时间。  API version 20起，支持：  - 设置文件的描述性文本信息OH_MD_KEY_COMMENT。若文件描述信息未写入成功，请排查OH_MD_KEY_COMMENT是否为字符串类型或字符长度大于等于1且小于等于256。  - 设置MP4 moov的位置OH_MD_KEY_ENABLE_MOOV_FRONT。OH_MD_KEY_ENABLE_MOOV_FRONT为0时moov后置，为1时前置，默认后置。 |
| OH_AVErrCode OH_AVMuxer_AddTrack(OH_AVMuxer *muxer, int32_t *trackIndex, OH_AVFormat *trackFormat) | 向封装器添加音视频轨。每调用一次本接口可以在封装器中添加一个音视频轨。该接口必须在OH_AVMuxer_Start前调用。 |
| OH_AVErrCode OH_AVMuxer_Start(OH_AVMuxer *muxer) | 开始封装。该接口必须在OH_AVMuxer_AddTrack后，OH_AVMuxer_WriteSample前调用。 |
| OH_AVErrCode OH_AVMuxer_WriteSample(OH_AVMuxer *muxer, uint32_t trackIndex, OH_AVMemory *sample, OH_AVCodecBufferAttr info) | 将sample写入封装器。 该接口必须在OH_AVMuxer_Start后，OH_AVMuxer_Stop前调用。调用者需要按info中的时间顺序将sample写入正确的音视频轨。 |
| OH_AVErrCode OH_AVMuxer_WriteSampleBuffer(OH_AVMuxer *muxer, uint32_t trackIndex, const OH_AVBuffer *sample) | 将sample写入封装器。该接口必须在OH_AVMuxer_Start后，OH_AVMuxer_Stop前调用。调用者需要按sample中的时间顺序将sample写入正确的音视频轨。 |
| OH_AVErrCode OH_AVMuxer_Stop(OH_AVMuxer *muxer) | 停止封装。封装器停止后不支持重新开始。 |
| OH_AVErrCode OH_AVMuxer_Destroy(OH_AVMuxer *muxer) | 清理内部资源，销毁OH_AVMuxer实例。  注意不能重复销毁，否则会导致程序崩溃。 |

**函数说明**

**OH_AVMuxer_Create()**

```ets
OH_AVMuxer *OH_AVMuxer_Create(int32_t fd, OH_AVOutputFormat format)
```

描述

通过文件描述符fd和封装格式创建OH_AVMuxer实例。

系统能力： SystemCapability.Multimedia.Media.Muxer

起始版本： 10

参数：

| 参数项 | 描述 |
| --- | --- |
| int32_t fd | 用读写方式打开（O_RDWR），由调用者关闭该fd。 |
| OH_AVOutputFormat format | 封装输出的文件格式。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_AVMuxer * | 返回一个指向OH_AVMuxer实例的指针，需要调用OH_AVMuxer_Destroy销毁。 |

**OH_AVMuxer_SetRotation()**

```ets
OH_AVErrCode OH_AVMuxer_SetRotation(OH_AVMuxer *muxer, int32_t rotation)
```

描述

设置视频的旋转角度（顺时针，且旋转角度必须为0、90、180或270）。该接口必须在[OH_AVMuxer_Start](#ZH-CN_TOPIC_0000002522241862__oh_avmuxer_start)前调用。

系统能力： SystemCapability.Multimedia.Media.Muxer

起始版本： 10

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVMuxer *muxer | 指向OH_AVMuxer实例的指针。 |
| int32_t rotation | 角度，必须为0、90、180 或 270。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_AVErrCode | AV_ERR_OK：执行成功。  AV_ERR_INVALID_VAL：muxer为空指针，或rotation无效。  AV_ERR_OPERATE_NOT_PERMIT：不允许调用该接口，请检查接口调用顺序。 |

**OH_AVMuxer_SetFormat()**

```ets
OH_AVErrCode OH_AVMuxer_SetFormat(OH_AVMuxer *muxer, OH_AVFormat *format)
```

描述

设置format数据到封装器。

 API version 14起，支持设置创建时间OH_MD_KEY_CREATION_TIME。若创建时间未写入成功，请排查OH_MD_KEY_CREATION_TIME字符串设置是否符合ISO 8601标准的时间格式且为UTC时间。

 API version 20起，支持：

- 设置文件的描述性文本信息OH_MD_KEY_COMMENT。若文件描述信息未写入成功，请排查OH_MD_KEY_COMMENT是否为字符串类型或字符长度大于等于1且小于等于256。

- 设置MP4 moov的位置OH_MD_KEY_ENABLE_MOOV_FRONT。OH_MD_KEY_ENABLE_MOOV_FRONT为0时moov后置，为1时前置，默认后置。

系统能力： SystemCapability.Multimedia.Media.Muxer

起始版本： 14

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVMuxer *muxer | 指向OH_AVMuxer实例的指针。 |
| OH_AVFormat *format | 指向OH_AVFormat实例的指针。文件级元数据集。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_AVErrCode | AV_ERR_OK：设置format参数正确。  AV_ERR_INVALID_VAL：muxer为空指针，或format无效。  AV_ERR_OPERATE_NOT_PERMIT：不允许调用该接口，请检查接口调用顺序。 |

**OH_AVMuxer_AddTrack()**

```ets
OH_AVErrCode OH_AVMuxer_AddTrack(OH_AVMuxer *muxer, int32_t *trackIndex, OH_AVFormat *trackFormat)
```

描述

向封装器添加音视频轨。每调用一次本接口可以在封装器中添加一个音视频轨。该接口必须在[OH_AVMuxer_Start](#ZH-CN_TOPIC_0000002522241862__oh_avmuxer_start)前调用。

系统能力： SystemCapability.Multimedia.Media.Muxer

起始版本： 10

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVMuxer *muxer | 指向OH_AVMuxer实例的指针。 |
| int32_t *trackIndex | 用于获取该轨的索引，该值在OH_AVMuxer_WriteSample接口中使用。如果媒体轨添加成功，该值大于或等于0，否则小于0。 |
| OH_AVFormat *trackFormat | 指向OH_AVFormat实例的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_AVErrCode | AV_ERR_OK：执行成功。  AV_ERR_INVALID_VAL：muxer为空指针，或trackIndex无效，或trackFormat无效。  AV_ERR_OPERATE_NOT_PERMIT：不允许调用该接口，请检查接口调用顺序。  AV_ERR_UNSUPPORT：不支持的mime类型。  AV_ERR_NO_MEMORY：申请内存失败。  AV_ERR_UNKNOWN：未知错误。 |

**OH_AVMuxer_Start()**

```ets
OH_AVErrCode OH_AVMuxer_Start(OH_AVMuxer *muxer)
```

描述

开始封装。该接口必须在[OH_AVMuxer_AddTrack](#ZH-CN_TOPIC_0000002522241862__oh_avmuxer_addtrack)后，[OH_AVMuxer_WriteSample](#ZH-CN_TOPIC_0000002522241862__oh_avmuxer_writesample)前调用。

系统能力： SystemCapability.Multimedia.Media.Muxer

起始版本： 10

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVMuxer *muxer | 指向OH_AVMuxer实例的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_AVErrCode | AV_ERR_OK：执行成功。  AV_ERR_INVALID_VAL：muxer为空指针。  AV_ERR_OPERATE_NOT_PERMIT：不允许调用该接口，请检查接口调用顺序。  AV_ERR_UNKNOWN：未知错误。 |

**OH_AVMuxer_WriteSample()**

```ets
OH_AVErrCode OH_AVMuxer_WriteSample(OH_AVMuxer *muxer, uint32_t trackIndex, OH_AVMemory *sample, OH_AVCodecBufferAttr info)
```

描述

将sample写入封装器。该接口必须在[OH_AVMuxer_Start](#ZH-CN_TOPIC_0000002522241862__oh_avmuxer_start)后，[OH_AVMuxer_Stop](#ZH-CN_TOPIC_0000002522241862__oh_avmuxer_stop)前调用。调用者需要按info中的时间顺序将sample写入正确的音视频轨。

系统能力： SystemCapability.Multimedia.Media.Muxer

起始版本： 10

废弃版本： 11

替代接口： [OH_AVMuxer_WriteSampleBuffer](#ZH-CN_TOPIC_0000002522241862__oh_avmuxer_writesamplebuffer)

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVMuxer *muxer | 指向OH_AVMuxer实例的指针。 |
| uint32_t trackIndex | 数据对应的音视频轨的索引。 |
| OH_AVMemory *sample | 编码或解封装得到的数据。 |
| OH_AVCodecBufferAttr info | sample对应的描述信息。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_AVErrCode | AV_ERR_OK：执行成功。  AV_ERR_INVALID_VAL：muxer为空指针，或trackIndex无效，或sample无效，或info无效。  AV_ERR_OPERATE_NOT_PERMIT：不允许调用该接口，请检查接口调用顺序。  AV_ERR_NO_MEMORY：申请内存失败。  AV_ERR_UNKNOWN：未知错误。 |

**OH_AVMuxer_WriteSampleBuffer()**

```ets
OH_AVErrCode OH_AVMuxer_WriteSampleBuffer(OH_AVMuxer *muxer, uint32_t trackIndex, const OH_AVBuffer *sample)
```

描述

将sample写入封装器。该接口必须在[OH_AVMuxer_Start](#ZH-CN_TOPIC_0000002522241862__oh_avmuxer_start)后，[OH_AVMuxer_Stop](#ZH-CN_TOPIC_0000002522241862__oh_avmuxer_stop)前调用。调用者需要按sample中的时间顺序将sample写入正确的音视频轨。

系统能力： SystemCapability.Multimedia.Media.Muxer

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVMuxer *muxer | 指向OH_AVMuxer实例的指针。 |
| uint32_t trackIndex | 数据对应的音视频轨的索引。 |
| const OH_AVBuffer *sample | 编码或解封装得到的数据及属性。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_AVErrCode | AV_ERR_OK：执行成功。  AV_ERR_INVALID_VAL：muxer为空指针，或trackIndex无效，或sample无效。  AV_ERR_OPERATE_NOT_PERMIT：不允许调用该接口，请检查接口调用顺序。  AV_ERR_NO_MEMORY：申请内存失败。  AV_ERR_UNKNOWN：未知错误。 |

**OH_AVMuxer_Stop()**

```ets
OH_AVErrCode OH_AVMuxer_Stop(OH_AVMuxer *muxer)
```

描述

停止封装。封装器停止后不支持重新开始。

系统能力： SystemCapability.Multimedia.Media.Muxer

起始版本： 10

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVMuxer *muxer | 指向OH_AVMuxer实例的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_AVErrCode | AV_ERR_OK：执行成功。  AV_ERR_INVALID_VAL：muxer为空指针。  AV_ERR_OPERATE_NOT_PERMIT：不允许调用该接口，请检查接口调用顺序。 |

**OH_AVMuxer_Destroy()**

```ets
OH_AVErrCode OH_AVMuxer_Destroy(OH_AVMuxer *muxer)
```

描述

清理内部资源，销毁OH_AVMuxer实例。

 注意不能重复销毁，否则会导致程序崩溃。

系统能力： SystemCapability.Multimedia.Media.Muxer

起始版本： 10

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVMuxer *muxer | 指向OH_AVMuxer实例的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_AVErrCode | AV_ERR_OK：执行成功。  AV_ERR_INVALID_VAL：muxer为空指针。 |