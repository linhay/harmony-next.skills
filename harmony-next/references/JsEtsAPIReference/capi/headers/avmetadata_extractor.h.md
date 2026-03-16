# avmetadata_extractor.h

#### 概述

定义AVMetadataExtractor接口。使用其C API从媒体资源中获取元数据。

**引用文件：** <multimedia/player_framework/avmetadata_extractor.h>

**库：** libavmetadata_extractor.so

**系统能力：** SystemCapability.Multimedia.Media.AVMetadataExtractor

**起始版本：** 18

**相关模块：**[AVMetadataExtractor](../../topics/misc/AVMetadataExtractor.md)

#### 汇总

#### 结构体

名称typedef关键字描述[OH_AVMetadataExtractor](../../topics/misc/OH_AVMetadataExtractor.md)OH_AVMetadataExtractor定义OH_AVMetadataExtractor类型。

#### 函数

名称描述[OH_AVMetadataExtractor* OH_AVMetadataExtractor_Create(void)](#ZH-CN_TOPIC_0000002529445877__oh_avmetadataextractor_create)创建OH_AVMetadataExtractor实例。[OH_AVErrCode OH_AVMetadataExtractor_SetFDSource(OH_AVMetadataExtractor* extractor, int32_t fd, int64_t offset, int64_t size)](#ZH-CN_TOPIC_0000002529445877__oh_avmetadataextractor_setfdsource)通过媒体文件描述设置数据源。[OH_AVErrCode OH_AVMetadataExtractor_FetchMetadata(OH_AVMetadataExtractor* extractor, OH_AVFormat* avMetadata)](#ZH-CN_TOPIC_0000002529445877__oh_avmetadataextractor_fetchmetadata)从媒体资源中获取元数据。此函数必须在[OH_AVMetadataExtractor_SetFDSource](#ZH-CN_TOPIC_0000002529445877__oh_avmetadataextractor_setfdsource)之后调用。[OH_AVErrCode OH_AVMetadataExtractor_FetchAlbumCover(OH_AVMetadataExtractor* extractor, OH_PixelmapNative** pixelMap)](#ZH-CN_TOPIC_0000002529445877__oh_avmetadataextractor_fetchalbumcover)获取音频专辑封面。此函数必须在[OH_AVMetadataExtractor_SetFDSource](#ZH-CN_TOPIC_0000002529445877__oh_avmetadataextractor_setfdsource)之后调用。[OH_AVErrCode OH_AVMetadataExtractor_Release(OH_AVMetadataExtractor* extractor)](#ZH-CN_TOPIC_0000002529445877__oh_avmetadataextractor_release)释放用于OH_AVMetadataExtractor的资源并销毁OH_AVMetadataExtractor实例。

#### 函数说明

#### OH_AVMetadataExtractor_Create()

```ets
OH_AVMetadataExtractor* OH_AVMetadataExtractor_Create(void)
```

**描述**

创建OH_AVMetadataExtractor实例。

**系统能力：** SystemCapability.Multimedia.Media.AVMetadataExtractor

**起始版本：** 18

**返回：**

类型说明[OH_AVMetadataExtractor](../../topics/misc/OH_AVMetadataExtractor.md)*

创建成功时返回指向OH_AVMetadataExtractor实例的指针，否则返回空指针。

 可能的失败原因：HstEngineFactory::CreateAVMetadataHelperEngine执行失败。

#### OH_AVMetadataExtractor_SetFDSource()

```ets
OH_AVErrCode OH_AVMetadataExtractor_SetFDSource(OH_AVMetadataExtractor* extractor,int32_t fd, int64_t offset, int64_t size)
```

**描述**

通过媒体文件描述设置数据源。

**系统能力：** SystemCapability.Multimedia.Media.AVMetadataExtractor

**起始版本：** 18

**参数：**

参数项描述[OH_AVMetadataExtractor](../../topics/misc/OH_AVMetadataExtractor.md)* extractor指向OH_AVMetadataExtractor实例的指针。int32_t fd媒体源的文件描述符。int64_t offset媒体源在文件描述符中的偏移量。int64_t size媒体源的大小。

**返回：**

类型说明[OH_AVErrCode](native_averrors.h.md#ZH-CN_TOPIC_0000002497605740__oh_averrcode)

AV_ERR_OK：执行成功。

 AV_ERR_INVALID_VAL： 输入的extractor为空指针或参数无效。

 AV_ERR_OPERATE_NOT_PERMIT：操作被禁止。

 AV_ERR_NO_MEMORY：内部内存分配失败。

#### OH_AVMetadataExtractor_FetchMetadata()

```ets
OH_AVErrCode OH_AVMetadataExtractor_FetchMetadata(OH_AVMetadataExtractor* extractor, OH_AVFormat* avMetadata)
```

**描述**

从媒体资源中获取元数据。

此函数必须在[OH_AVMetadataExtractor_SetFDSource](#ZH-CN_TOPIC_0000002529445877__oh_avmetadataextractor_setfdsource)之后调用。

**系统能力：** SystemCapability.Multimedia.Media.AVMetadataExtractor

**起始版本：** 18

**参数：**

参数项描述[OH_AVMetadataExtractor](../../topics/misc/OH_AVMetadataExtractor.md)* extractor指向OH_AVMetadataExtractor实例的指针。[OH_AVFormat](../../topics/misc/OH_AVFormat.md)* avMetadata指向OH_AVFormat实例的指针，其内容包含获取的元数据信息。

**返回：**

类型说明[OH_AVErrCode](native_averrors.h.md#ZH-CN_TOPIC_0000002497605740__oh_averrcode)

AV_ERR_OK：执行成功。

 AV_ERR_INVALID_VAL： 输入的extractor为空指针或参数无效。

 AV_ERR_OPERATE_NOT_PERMIT：操作被禁止。

 AV_ERR_UNSUPPORTED_FORMAT：格式不支持。

 AV_ERR_NO_MEMORY：内部内存分配失败。

#### OH_AVMetadataExtractor_FetchAlbumCover()

```ets
OH_AVErrCode OH_AVMetadataExtractor_FetchAlbumCover(OH_AVMetadataExtractor* extractor, OH_PixelmapNative** pixelMap)
```

**描述**

获取音频专辑封面。

此函数必须在[OH_AVMetadataExtractor_SetFDSource](#ZH-CN_TOPIC_0000002529445877__oh_avmetadataextractor_setfdsource)之后调用。

**系统能力：** SystemCapability.Multimedia.Media.AVMetadataExtractor

**起始版本：** 18

**参数：**

参数项描述[OH_AVMetadataExtractor](../../topics/misc/OH_AVMetadataExtractor.md)* extractor指向OH_AVMetadataExtractor实例的指针。[OH_PixelmapNative](../../topics/graphics/OH_PixelmapNative.md)** pixelMap从音频源获取的专辑封面。

**返回：**

类型说明[OH_AVErrCode](native_averrors.h.md#ZH-CN_TOPIC_0000002497605740__oh_averrcode)

AV_ERR_OK：执行成功。

 AV_ERR_INVALID_VAL： 输入的extractor为空指针或参数无效。

 AV_ERR_OPERATE_NOT_PERMIT：操作被禁止。

 AV_ERR_UNSUPPORTED_FORMAT：格式不支持。

 AV_ERR_NO_MEMORY：内部内存分配失败。

#### OH_AVMetadataExtractor_Release()

```ets
OH_AVErrCode OH_AVMetadataExtractor_Release(OH_AVMetadataExtractor* extractor)
```

**描述**

释放用于OH_AVMetadataExtractor的资源并销毁OH_AVMetadataExtractor实例。

**系统能力：** SystemCapability.Multimedia.Media.AVMetadataExtractor

**起始版本：** 18

**参数：**

参数项描述[OH_AVMetadataExtractor](../../topics/misc/OH_AVMetadataExtractor.md)* extractor指向OH_AVMetadataExtractor实例指针。

**返回：**

类型说明[OH_AVErrCode](native_averrors.h.md#ZH-CN_TOPIC_0000002497605740__oh_averrcode)

AV_ERR_OK：执行成功。

 AV_ERR_INVALID_VAL： 输入的extractor为空指针或参数无效。