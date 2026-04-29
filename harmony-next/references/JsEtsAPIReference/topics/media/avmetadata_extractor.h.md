# avmetadata_extractor.h

**概述**

定义AVMetadataExtractor接口。使用其Native API从媒体资源中获取元数据。

引用文件： <multimedia/player_framework/avmetadata_extractor.h>

库： libavmetadata_extractor.so

系统能力： SystemCapability.Multimedia.Media.AVMetadataExtractor

起始版本： 18

相关模块： [AVMetadataExtractor](AVMetadataExtractor.md)

**汇总**

**结构体**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| OH_AVMetadataExtractor | OH_AVMetadataExtractor | 定义OH_AVMetadataExtractor类型。 |

**函数**

| 名称 | 描述 |
| --- | --- |
| OH_AVMetadataExtractor_OutputParam* OH_AVMetadataExtractor_OutputParam_Create() | 创建OH_AVMetadataExtractor_OutputParam实例。 |
| void OH_AVMetadataExtractor_OutputParam_Destroy(OH_AVMetadataExtractor_OutputParam* outputParam) | 释放OH_AVMetadataExtractor_OutputParam实例。 |
| bool OH_AVMetadataExtractor_OutputParam_SetSize(OH_AVMetadataExtractor_OutputParam* outputParam, int32_t width, int32_t height) | 设置OH_AVMetadataExtractor_OutputParam实例的期望输出尺寸。若width或height小于0，则使用原始宽度或高度。若width或height等于0，则保持宽高比按比例缩放。若width和height均大于0，则使用输入的width和height参数缩放图像。 |
| OH_AVErrCode OH_AVMetadataExtractor_FetchFrameByTime(OH_AVMetadataExtractor extractor, int64_t timeUs, OH_AVMedia_SeekMode seekMode, const OH_AVMetadataExtractor_OutputParam outputParam, OH_PixelmapNative** pixelMap) | 从视频源中提取指定时间点的图像。该函数必须在设置资源之后使用。 |
| typedef void (*OH_AVMetadataExtractor_OnFrameFetched)(OH_AVMetadataExtractor extractor, const OH_AVMetadataExtractor_FrameInfo frameInfo, OH_AVErrCode code, void* userData) | 定义用于获取AVMetadataExtractor捕获帧的回调函数。注意：frameInfo会在回调后自动释放，但用户需要使用OH_PixelmapNative_Destroy手动释放frameInfo.image，避免内存泄漏。 |
| OH_AVErrCode OH_AVMetadataExtractor_FetchFramesByTimes(OH_AVMetadataExtractor extractor, int64_t timeUs[], uint16_t timesUsSize, OH_AVMedia_SeekMode seekMode, const OH_AVMetadataExtractor_OutputParam outputParam, OH_AVMetadataExtractor_OnFrameFetched onFrameInfoCallback, void* userData) | 从视频源中异步提取多个指定时间点的图像。该函数必须在设置资源之后使用。 |
| void OH_AVMetadataExtractor_CancelAllFetchFrames(OH_AVMetadataExtractor *extractor) | 取消所有由OH_AVMetadataExtractor_FetchFramesByTimes发起的批量获取图像操作。在OH_AVMetadataExtractor_OnFrameFetched回调中，挂起的获取操作被取消，并标记结果为已取消。 |
| OH_AVFormat *OH_AVMetadataExtractor_GetTrackDescription(OH_AVMetadataExtractor *extractor, uint32_t index) | 从媒体源中获取指定索引的轨道描述信息。该函数必须在设置资源之后使用。 |
| OH_AVFormat *OH_AVMetadataExtractor_GetCustomInfo(OH_AVMetadataExtractor *extractor) | 从媒体源中获取自定义元数据信息。该函数必须在设置资源之后使用。 |
| OH_AVErrCode OH_AVMetadataExtractor_SetMediaSource(OH_AVMetadataExtractor *extractor, OH_AVMediaSource *source) | 为提取器设置媒体源。 |
| OH_AVMetadataExtractor* OH_AVMetadataExtractor_Create(void) | 创建OH_AVMetadataExtractor实例。 |
| OH_AVErrCode OH_AVMetadataExtractor_SetFDSource(OH_AVMetadataExtractor* extractor, int32_t fd, int64_t offset, int64_t size) | 通过媒体文件描述设置数据源。 |
| OH_AVErrCode OH_AVMetadataExtractor_FetchMetadata(OH_AVMetadataExtractor* extractor, OH_AVFormat* avMetadata) | 从媒体资源中获取元数据。  此函数必须在OH_AVMetadataExtractor_SetFDSource之后调用。 |
| OH_AVErrCode OH_AVMetadataExtractor_FetchAlbumCover(OH_AVMetadataExtractor* extractor, OH_PixelmapNative** pixelMap) | 获取音频专辑封面。  此函数必须在OH_AVMetadataExtractor_SetFDSource之后调用。 |
| OH_AVErrCode OH_AVMetadataExtractor_Release(OH_AVMetadataExtractor* extractor) | 释放用于OH_AVMetadataExtractor的资源并销毁OH_AVMetadataExtractor实例。 |

**函数说明**

**OH_AVMetadataExtractor_OutputParam_Create()**

```ets
OH_AVMetadataExtractor_OutputParam* OH_AVMetadataExtractor_OutputParam_Create()
```

描述

创建OH_AVMetadataExtractor_OutputParam实例。

起始版本： 23

返回：

| 类型 | 说明 |
| --- | --- |
| OH_AVMetadataExtractor_OutputParam * | 返回指向OH_AVMetadataExtractor_OutputParam实例的指针。 |

**OH_AVMetadataExtractor_OutputParam_Destroy()**

```ets
void OH_AVMetadataExtractor_OutputParam_Destroy(OH_AVMetadataExtractor_OutputParam* outputParam)
```

描述

释放OH_AVMetadataExtractor_OutputParam实例。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVMetadataExtractor_OutputParam* outputParam | 指向OH_AVMetadataExtractor_OutputParam实例的指针。 |

**OH_AVMetadataExtractor_OutputParam_SetSize()**

```ets
bool OH_AVMetadataExtractor_OutputParam_SetSize(OH_AVMetadataExtractor_OutputParam* outputParam, int32_t width, int32_t height)
```

描述

设置OH_AVMetadataExtractor_OutputParam实例的期望输出尺寸。若width或height小于0，则使用原始宽度或高度。若width或height等于0，则保持宽高比按比例缩放。若width和height均大于0，则使用输入的width和height参数缩放图像。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVMetadataExtractor_OutputParam* outputParam | 指向OH_AVMetadataExtractor_OutputParam实例的指针。 |
| int32_t width | 输出图像的期望宽度，如有必要可进行缩放。 |
| int32_t height | 输出图像的期望高度，如有必要可进行缩放。 |

返回：

| 类型 | 说明 |
| --- | --- |
| bool | 成功返回true，失败返回false。  可能失败的原因：outputParam为空指针。 |

**OH_AVMetadataExtractor_FetchFrameByTime()**

```ets
OH_AVErrCode OH_AVMetadataExtractor_FetchFrameByTime(OH_AVMetadataExtractor *extractor, int64_t timeUs, OH_AVMedia_SeekMode seekMode, const OH_AVMetadataExtractor_OutputParam* outputParam, OH_PixelmapNative** pixelMap)
```

描述

从视频源中提取指定时间点的图像。该函数必须在设置资源之后使用。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVMetadataExtractor *extractor | 指向OH_AVMetadataExtractor实例的指针。 |
| int64_t timeUs | 要从视频资源中提取图像的时间位置（单位：微秒）。 |
| OH_AVMedia_SeekMode seekMode | 定义指定时间与关键帧之间关系的跳转模式。详见OH_AVMedia_SeekMode。 |
| const OH_AVMetadataExtractor_OutputParam* outputParam | 图像的输出参数，例如图像的高度或者宽度。详见OH_AVMetadataExtractor_OutputParam。若为空指针，使用视频的原始尺寸。注意：用户需要使用OH_PixelmapNative_Destroy在使用pixelMap后将其释放。 |
| OH_PixelmapNative** pixelMap | 用于接收从视频源提取的图像，详见OH_PixelmapNative。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_AVErrCode | 函数执行结果。  AV_ERR_OK：执行成功。  AV_ERR_INVALID_VAL：输入参数无效。  AV_ERR_OPERATE_NOT_PERMIT：操作不允许。  AV_ERR_UNSUPPORTED_FORMAT：格式不支持。  AV_ERR_SERVICE_DIED：服务已终止。  AV_ERR_IO_CLEARTEXT_NOT_PERMITTED：不允许HTTP明文流量。 |

**OH_AVMetadataExtractor_OnFrameFetched()**

```ets
typedef void (*OH_AVMetadataExtractor_OnFrameFetched)(OH_AVMetadataExtractor *extractor, const OH_AVMetadataExtractor_FrameInfo* frameInfo, OH_AVErrCode code, void* userData)
```

描述

定义用于获取AVMetadataExtractor捕获帧的回调函数。注意：frameInfo会在回调后自动释放，但用户需要使用[OH_PixelmapNative_Destroy](pixelmap_native.h.md#ZH-CN_TOPIC_0000002522241982__oh_pixelmapnative_destroy)手动释放frameInfo.image，避免内存泄漏。

起始版本： 23

**OH_AVMetadataExtractor_FetchFramesByTimes()**

```ets
OH_AVErrCode OH_AVMetadataExtractor_FetchFramesByTimes(OH_AVMetadataExtractor *extractor, int64_t timeUs[], uint16_t timesUsSize, OH_AVMedia_SeekMode seekMode, const OH_AVMetadataExtractor_OutputParam* outputParam, OH_AVMetadataExtractor_OnFrameFetched onFrameInfoCallback, void* userData)
```

描述

从视频源中异步提取多个指定时间点的图像。该函数必须在设置资源之后使用。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVMetadataExtractor *extractor | 指向OH_AVMetadataExtractor实例的指针。 |
| int64_t timeUs[] | 从视频源提取图像时的时间点数组（单位：微秒）。 |
| uint16_t timesUsSize | 输入时间点数组的长度。 |
| OH_AVMedia_SeekMode seekMode | 定义每个给定时间与关键帧之间关系的跳转选项，详见OH_AVMedia_SeekMode。 |
| const OH_AVMetadataExtractor_OutputParam* outputParam | 图像的输出参数，例如图像的高度或者宽度。详见OH_AVMetadataExtractor_OutputParam。若该参数为空指针，则获取的帧使用视频原始尺寸。 |
| OH_AVMetadataExtractor_OnFrameFetched onFrameInfoCallback | 每帧提取完成或提取失败后调用的回调函数。 |
| void* userData | 传递给回调函数的用户自定义数据指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_AVErrCode | 函数执行结果。  AV_ERR_OK：执行成功。  AV_ERR_INVALID_VAL：输入参数无效。  AV_ERR_SERVICE_DIED：服务已终止。  AV_ERR_IO_CLEARTEXT_NOT_PERMITTED：不允许HTTP明文流量。  AV_ERR_OPERATE_NOT_PERMIT：操作不允许。由onFrameInfoCallback返回。  AV_ERR_UNSUPPORTED_FORMAT：格式不支持。由onFrameInfoCallback返回。  AV_ERR_TIMEOUT：执行超时。由onFrameInfoCallback返回。 |

**OH_AVMetadataExtractor_CancelAllFetchFrames()**

```ets
void OH_AVMetadataExtractor_CancelAllFetchFrames(OH_AVMetadataExtractor *extractor)
```

描述

取消所有由[OH_AVMetadataExtractor_FetchFramesByTimes](avmetadata_extractor.h.md#ZH-CN_TOPIC_0000002522242042__oh_avmetadataextractor_fetchframesbytimes)发起的批量获取图像操作。在[OH_AVMetadataExtractor_OnFrameFetched](avmetadata_extractor.h.md#ZH-CN_TOPIC_0000002522242042__oh_avmetadataextractor_onframefetched)回调中，挂起的获取操作被取消，并标记结果为已取消。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVMetadataExtractor *extractor | 指向OH_AVMetadataExtractor实例的指针。 |

**OH_AVMetadataExtractor_GetTrackDescription()**

```ets
OH_AVFormat *OH_AVMetadataExtractor_GetTrackDescription(OH_AVMetadataExtractor *extractor, uint32_t index)
```

描述

从媒体源中获取指定索引的轨道描述信息。该函数必须在设置资源之后使用。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVMetadataExtractor *extractor | 指向OH_AVMetadataExtractor实例的指针。 |
| uint32_t index | 要获取的轨道描述的索引。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_AVFormat * | 成功时返回包含轨道描述信息的OH_AVFormat实例指针，失败时返回空指针。  可能失败的原因：  1、extractor为空指针。  2、未设置媒体源。  3、格式不支持。  注意：用户需要使用OH_AVFormat_Destroy在使用OH_AVFormat后将其释放。 |

**OH_AVMetadataExtractor_GetCustomInfo()**

```ets
OH_AVFormat *OH_AVMetadataExtractor_GetCustomInfo(OH_AVMetadataExtractor *extractor)
```

描述

从媒体源中获取自定义元数据信息。该函数必须在设置资源之后使用。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVMetadataExtractor *extractor | 指向OH_AVMetadataExtractor实例的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_AVFormat * | 成功时返回包含自定义元数据的OH_AVFormat实例指针，失败时返回空指针。  可能失败的原因：  1、extractor为空指针。  2、未设置媒体源。  3、未找到自定义信息。  注意：用户需要使用OH_AVFormat_Destroy在使用OH_AVFormat后将其释放。 |

**OH_AVMetadataExtractor_SetMediaSource()**

```ets
OH_AVErrCode OH_AVMetadataExtractor_SetMediaSource(OH_AVMetadataExtractor *extractor, OH_AVMediaSource *source)
```

描述

为提取器设置媒体源。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVMetadataExtractor *extractor | 指向OH_AVMetadataExtractor实例的指针。 |
| OH_AVMediaSource *source | 要设置的媒体源。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_AVErrCode | 函数执行结果。  AV_ERR_OK：表示执行成功。  AV_ERR_INVALID_VAL：输入的extractor为空指针或输入的source无效。 |

**OH_AVMetadataExtractor_Create()**

```ets
OH_AVMetadataExtractor* OH_AVMetadataExtractor_Create(void)
```

描述

创建OH_AVMetadataExtractor实例。

系统能力： SystemCapability.Multimedia.Media.AVMetadataExtractor

起始版本： 18

返回：

| 类型 | 说明 |
| --- | --- |
| OH_AVMetadataExtractor* | 创建成功时返回指向OH_AVMetadataExtractor实例的指针，否则返回空指针。  可能的失败原因：HstEngineFactory::CreateAVMetadataHelperEngine执行失败。 |

**OH_AVMetadataExtractor_SetFDSource()**

```ets
OH_AVErrCode OH_AVMetadataExtractor_SetFDSource(OH_AVMetadataExtractor* extractor, int32_t fd, int64_t offset, int64_t size)
```

描述

通过媒体文件描述设置数据源。

系统能力： SystemCapability.Multimedia.Media.AVMetadataExtractor

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVMetadataExtractor* extractor | 指向OH_AVMetadataExtractor实例的指针。 |
| int32_t fd | 媒体源的文件描述符。 |
| int64_t offset | 媒体源在文件描述符中的偏移量。 |
| int64_t size | 媒体源的大小。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_AVErrCode | AV_ERR_OK：执行成功。  AV_ERR_INVALID_VAL： 输入的extractor为空指针或参数无效。  AV_ERR_OPERATE_NOT_PERMIT：操作被禁止。  AV_ERR_NO_MEMORY：内部内存分配失败。 |

**OH_AVMetadataExtractor_FetchMetadata()**

```ets
OH_AVErrCode OH_AVMetadataExtractor_FetchMetadata(OH_AVMetadataExtractor* extractor, OH_AVFormat* avMetadata)
```

描述

从媒体资源中获取元数据。

 此函数必须在[OH_AVMetadataExtractor_SetFDSource](avmetadata_extractor.h.md#ZH-CN_TOPIC_0000002522242042__oh_avmetadataextractor_setfdsource)之后调用。

系统能力： SystemCapability.Multimedia.Media.AVMetadataExtractor

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVMetadataExtractor* extractor | 指向OH_AVMetadataExtractor实例的指针。 |
| OH_AVFormat* avMetadata | 指向OH_AVFormat实例的指针，其内容包含获取的元数据信息。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_AVErrCode | AV_ERR_OK：执行成功。  AV_ERR_INVALID_VAL： 输入的extractor为空指针或参数无效。  AV_ERR_OPERATE_NOT_PERMIT：操作被禁止。  AV_ERR_UNSUPPORTED_FORMAT：格式不支持。  AV_ERR_NO_MEMORY：内部内存分配失败。 |

**OH_AVMetadataExtractor_FetchAlbumCover()**

```ets
OH_AVErrCode OH_AVMetadataExtractor_FetchAlbumCover(OH_AVMetadataExtractor* extractor, OH_PixelmapNative** pixelMap)
```

描述

获取音频专辑封面。

 此函数必须在[OH_AVMetadataExtractor_SetFDSource](avmetadata_extractor.h.md#ZH-CN_TOPIC_0000002522242042__oh_avmetadataextractor_setfdsource)之后调用。

系统能力： SystemCapability.Multimedia.Media.AVMetadataExtractor

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVMetadataExtractor* extractor | 指向OH_AVMetadataExtractor实例的指针。 |
| OH_PixelmapNative** pixelMap | 从音频源获取的专辑封面。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_AVErrCode | AV_ERR_OK：执行成功。  AV_ERR_INVALID_VAL： 输入的extractor为空指针或参数无效。  AV_ERR_OPERATE_NOT_PERMIT：操作被禁止。  AV_ERR_UNSUPPORTED_FORMAT：格式不支持。  AV_ERR_NO_MEMORY：内部内存分配失败。 |

**OH_AVMetadataExtractor_Release()**

```ets
OH_AVErrCode OH_AVMetadataExtractor_Release(OH_AVMetadataExtractor* extractor)
```

描述

释放用于OH_AVMetadataExtractor的资源并销毁OH_AVMetadataExtractor实例。

系统能力： SystemCapability.Multimedia.Media.AVMetadataExtractor

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVMetadataExtractor* extractor | 指向OH_AVMetadataExtractor实例指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_AVErrCode | AV_ERR_OK：执行成功。  AV_ERR_INVALID_VAL： 输入的extractor为空指针或参数无效。 |