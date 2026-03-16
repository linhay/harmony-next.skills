# native_avmetadata.h

#### 概述

提供播控元数据的定义。

**引用文件：** <multimedia/av_session/native_avmetadata.h>

**库：** libohavsession.so

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 13

**相关模块：**[OHAVSession](../../topics/misc/OHAVSession.md)

#### 汇总

#### 结构体

名称typedef关键字描述[OH_AVMetadataBuilderStruct](../../topics/components/OH_AVMetadataBuilderStruct.md)OH_AVMetadataBuilder会话元数据构造器。构造器用于构造会话元数据。[OH_AVMetadataStruct](../../topics/misc/OH_AVMetadataStruct.md)OH_AVMetadata会话元数据。资源设置的avmetadata的实例。

#### 枚举

名称typedef关键字描述[AVMetadata_Result](#ZH-CN_TOPIC_0000002497445790__avmetadata_result)AVMetadata_Result元数据操作的错误码。[AVMetadata_SkipIntervals](#ZH-CN_TOPIC_0000002497445790__avmetadata_skipintervals)AVMetadata_SkipIntervals表示session支持的快进快退时间间隔。[AVMetadata_DisplayTag](#ZH-CN_TOPIC_0000002497445790__avmetadata_displaytag)AVMetadata_DisplayTag应用媒体音源的特殊类型标识。

#### 函数

名称描述[AVMetadata_Result OH_AVMetadataBuilder_Create(OH_AVMetadataBuilder** builder)](#ZH-CN_TOPIC_0000002497445790__oh_avmetadatabuilder_create)创建一个元数据构造器。[AVMetadata_Result OH_AVMetadataBuilder_Destroy(OH_AVMetadataBuilder* builder)](#ZH-CN_TOPIC_0000002497445790__oh_avmetadatabuilder_destroy)销毁元数据构造器。[AVMetadata_Result OH_AVMetadataBuilder_SetAssetId(OH_AVMetadataBuilder* builder, const char* assetId)](#ZH-CN_TOPIC_0000002497445790__oh_avmetadatabuilder_setassetid)设置当前媒体资源id。[AVMetadata_Result OH_AVMetadataBuilder_SetTitle(OH_AVMetadataBuilder* builder, const char* title)](#ZH-CN_TOPIC_0000002497445790__oh_avmetadatabuilder_settitle)设置资源标题。[AVMetadata_Result OH_AVMetadataBuilder_SetArtist(OH_AVMetadataBuilder* builder, const char* artist)](#ZH-CN_TOPIC_0000002497445790__oh_avmetadatabuilder_setartist)设置资源所属的艺术家。[AVMetadata_Result OH_AVMetadataBuilder_SetAuthor(OH_AVMetadataBuilder* builder, const char* author)](#ZH-CN_TOPIC_0000002497445790__oh_avmetadatabuilder_setauthor)设置资源的作者。[AVMetadata_Result OH_AVMetadataBuilder_SetAlbum(OH_AVMetadataBuilder* builder, const char* album)](#ZH-CN_TOPIC_0000002497445790__oh_avmetadatabuilder_setalbum)设置资源专辑名称。[AVMetadata_Result OH_AVMetadataBuilder_SetWriter(OH_AVMetadataBuilder* builder, const char* writer)](#ZH-CN_TOPIC_0000002497445790__oh_avmetadatabuilder_setwriter)设置资源词作者。[AVMetadata_Result OH_AVMetadataBuilder_SetComposer(OH_AVMetadataBuilder* builder, const char* composer)](#ZH-CN_TOPIC_0000002497445790__oh_avmetadatabuilder_setcomposer)设置资源作曲者。[AVMetadata_Result OH_AVMetadataBuilder_SetDuration(OH_AVMetadataBuilder* builder, int64_t duration)](#ZH-CN_TOPIC_0000002497445790__oh_avmetadatabuilder_setduration)设置资源播放时长。[AVMetadata_Result OH_AVMetadataBuilder_SetMediaImageUri(OH_AVMetadataBuilder* builder, const char* mediaImageUri)](#ZH-CN_TOPIC_0000002497445790__oh_avmetadatabuilder_setmediaimageuri)设置媒体图片数据。[AVMetadata_Result OH_AVMetadataBuilder_SetSubtitle(OH_AVMetadataBuilder* builder, const char* subtitle)](#ZH-CN_TOPIC_0000002497445790__oh_avmetadatabuilder_setsubtitle)设置副标题。[AVMetadata_Result OH_AVMetadataBuilder_SetDescription(OH_AVMetadataBuilder* builder, const char* description)](#ZH-CN_TOPIC_0000002497445790__oh_avmetadatabuilder_setdescription)设置媒体描述信息。[AVMetadata_Result OH_AVMetadataBuilder_SetLyric(OH_AVMetadataBuilder* builder, const char* lyric)](#ZH-CN_TOPIC_0000002497445790__oh_avmetadatabuilder_setlyric)设置歌词。[AVMetadata_Result OH_AVMetadataBuilder_SetSkipIntervals(OH_AVMetadataBuilder* builder, AVMetadata_SkipIntervals intervals)](#ZH-CN_TOPIC_0000002497445790__oh_avmetadatabuilder_setskipintervals)设置资源的跳转间隔时间。[AVMetadata_Result OH_AVMetadataBuilder_SetDisplayTags(OH_AVMetadataBuilder* builder, int32_t tags)](#ZH-CN_TOPIC_0000002497445790__oh_avmetadatabuilder_setdisplaytags)设置媒体资源的金标类型。[AVMetadata_Result OH_AVMetadataBuilder_GenerateAVMetadata(OH_AVMetadataBuilder* builder, OH_AVMetadata** avMetadata)](#ZH-CN_TOPIC_0000002497445790__oh_avmetadatabuilder_generateavmetadata)生成媒体元数据对象。[AVMetadata_Result OH_AVMetadata_Destroy(OH_AVMetadata* avMetadata)](#ZH-CN_TOPIC_0000002497445790__oh_avmetadata_destroy)释放媒体元数据对象。

#### 枚举类型说明

#### AVMetadata_Result

```ets
enum AVMetadata_Result
```

**描述**

元数据操作的错误码。

**起始版本：** 13

枚举项描述AVMETADATA_SUCCESS = 0执行成功。AVMETADATA_ERROR_INVALID_PARAM = 1入参错误。AVMETADATA_ERROR_NO_MEMORY = 2内存不足。

#### AVMetadata_SkipIntervals

```ets
enum AVMetadata_SkipIntervals
```

**描述**

表示session支持的快进快退时间间隔。

**起始版本：** 13

枚举项描述SECONDS_10 = 10时间为10秒。SECONDS_15 = 15时间为15秒。SECONDS_30 = 30时间为30秒。

#### AVMetadata_DisplayTag

```ets
enum AVMetadata_DisplayTag
```

**描述**

应用媒体音源的特殊类型标识。

**起始版本：** 13

枚举项描述AVSESSION_DISPLAYTAG_AUDIO_VIVID = 1AUDIO VIVID标识。

#### 函数说明

#### OH_AVMetadataBuilder_Create()

```ets
AVMetadata_Result OH_AVMetadataBuilder_Create(OH_AVMetadataBuilder** builder)
```

**描述**

创建一个元数据构造器。

**起始版本：** 13

**参数：**

参数项描述[OH_AVMetadataBuilder](../../topics/components/OH_AVMetadataBuilderStruct.md)** builder该引用指向创建的构造器实例。

**返回：**

类型说明[AVMetadata_Result](native_avmetadata.h.md#ZH-CN_TOPIC_0000002497445790__avmetadata_result)

AVMETADATA_SUCCESS：函数执行成功。

 AVMETADATA_ERROR_INVALID_PARAM：参数builder为nullptr。

 AVMETADATA_ERROR_NO_MEMORY：没有内存来分配新实例。

#### OH_AVMetadataBuilder_Destroy()

```ets
AVMetadata_Result OH_AVMetadataBuilder_Destroy(OH_AVMetadataBuilder* builder)
```

**描述**

销毁元数据构造器。

**起始版本：** 13

**参数：**

参数项描述[OH_AVMetadataBuilder](../../topics/components/OH_AVMetadataBuilderStruct.md)* builder指向元数据构造器的实例。

**返回：**

类型说明[AVMetadata_Result](native_avmetadata.h.md#ZH-CN_TOPIC_0000002497445790__avmetadata_result)

AVMETADATA_SUCCESS：函数执行成功。

 AVMETADATA_ERROR_INVALID_PARAM：参数builder为nullptr。

#### OH_AVMetadataBuilder_SetAssetId()

```ets
AVMetadata_Result OH_AVMetadataBuilder_SetAssetId(OH_AVMetadataBuilder* builder, const char* assetId)
```

**描述**

设置当前媒体资源id。

**起始版本：** 13

**参数：**

参数项描述[OH_AVMetadataBuilder](../../topics/components/OH_AVMetadataBuilderStruct.md)* builder指向元数据构造器的实例。const char* assetId资源id。

**返回：**

类型说明[AVMetadata_Result](native_avmetadata.h.md#ZH-CN_TOPIC_0000002497445790__avmetadata_result)

AVMETADATA_SUCCESS：函数执行成功。

 AVMETADATA_ERROR_INVALID_PARAM：

 1.参数builder为nullptr。

 2.参数assetId为nullptr。

#### OH_AVMetadataBuilder_SetTitle()

```ets
AVMetadata_Result OH_AVMetadataBuilder_SetTitle(OH_AVMetadataBuilder* builder, const char* title)
```

**描述**

设置资源标题。

**起始版本：** 13

**参数：**

参数项描述[OH_AVMetadataBuilder](../../topics/components/OH_AVMetadataBuilderStruct.md)* builder指向元数据构造器的实例。const char* title标题。

**返回：**

类型说明[AVMetadata_Result](native_avmetadata.h.md#ZH-CN_TOPIC_0000002497445790__avmetadata_result)

AVMETADATA_SUCCESS：函数执行成功。

 AVMETADATA_ERROR_INVALID_PARAM：

 1. 参数builder为nullptr。

 2. 参数title为nullptr。

#### OH_AVMetadataBuilder_SetArtist()

```ets
AVMetadata_Result OH_AVMetadataBuilder_SetArtist(OH_AVMetadataBuilder* builder, const char* artist)
```

**描述**

设置资源所属的艺术家。

**起始版本：** 13

**参数：**

参数项描述[OH_AVMetadataBuilder](../../topics/components/OH_AVMetadataBuilderStruct.md)* builder指向元数据构造器的实例。const char* artist艺术家。

**返回：**

类型说明[AVMetadata_Result](native_avmetadata.h.md#ZH-CN_TOPIC_0000002497445790__avmetadata_result)

AVMETADATA_SUCCESS：函数执行成功。

 AVMETADATA_ERROR_INVALID_PARAM：

 1. 参数builder为nullptr。

 2. 参数artist为nullptr。

#### OH_AVMetadataBuilder_SetAuthor()

```ets
AVMetadata_Result OH_AVMetadataBuilder_SetAuthor(OH_AVMetadataBuilder* builder, const char* author)
```

**描述**

设置资源的作者。

**起始版本：** 13

**参数：**

参数项描述[OH_AVMetadataBuilder](../../topics/components/OH_AVMetadataBuilderStruct.md)* builder指向元数据构造器的实例。const char* author作者。

**返回：**

类型说明[AVMetadata_Result](native_avmetadata.h.md#ZH-CN_TOPIC_0000002497445790__avmetadata_result)

AVMETADATA_SUCCESS：函数执行成功。

 AVMETADATA_ERROR_INVALID_PARAM：

 1. 参数builder为nullptr。

 2. 参数author为nullptr。

#### OH_AVMetadataBuilder_SetAlbum()

```ets
AVMetadata_Result OH_AVMetadataBuilder_SetAlbum(OH_AVMetadataBuilder* builder, const char* album)
```

**描述**

设置资源专辑名称。

**起始版本：** 13

**参数：**

参数项描述[OH_AVMetadataBuilder](../../topics/components/OH_AVMetadataBuilderStruct.md)* builder指向元数据构造器的实例。const char* album专辑名。

**返回：**

类型说明[AVMetadata_Result](native_avmetadata.h.md#ZH-CN_TOPIC_0000002497445790__avmetadata_result)

AVMETADATA_SUCCESS：函数执行成功。

 AVMETADATA_ERROR_INVALID_PARAM：

 1. 参数builder为nullptr。

 2. 参数album为nullptr。

#### OH_AVMetadataBuilder_SetWriter()

```ets
AVMetadata_Result OH_AVMetadataBuilder_SetWriter(OH_AVMetadataBuilder* builder, const char* writer)
```

**描述**

设置资源词作者。

**起始版本：** 13

**参数：**

参数项描述[OH_AVMetadataBuilder](../../topics/components/OH_AVMetadataBuilderStruct.md)* builder指向元数据构造器的实例。const char* writer词作者。

**返回：**

类型说明[AVMetadata_Result](native_avmetadata.h.md#ZH-CN_TOPIC_0000002497445790__avmetadata_result)

AVMETADATA_SUCCESS：函数执行成功。

 AVMETADATA_ERROR_INVALID_PARAM：

 1. 参数builder为nullptr。

 2. 参数writer为nullptr。

#### OH_AVMetadataBuilder_SetComposer()

```ets
AVMetadata_Result OH_AVMetadataBuilder_SetComposer(OH_AVMetadataBuilder* builder, const char* composer)
```

**描述**

设置资源作曲者。

**起始版本：** 13

**参数：**

参数项描述[OH_AVMetadataBuilder](../../topics/components/OH_AVMetadataBuilderStruct.md)* builder指向元数据构造器的实例。const char* composer作曲者。

**返回：**

类型说明[AVMetadata_Result](native_avmetadata.h.md#ZH-CN_TOPIC_0000002497445790__avmetadata_result)

AVMETADATA_SUCCESS：函数执行成功。

 AVMETADATA_ERROR_INVALID_PARAM：

 1. 参数builder为nullptr。

 2. 参数composer为nullptr。

#### OH_AVMetadataBuilder_SetDuration()

```ets
AVMetadata_Result OH_AVMetadataBuilder_SetDuration(OH_AVMetadataBuilder* builder, int64_t duration)
```

**描述**

设置资源播放时长。

**起始版本：** 13

**参数：**

参数项描述[OH_AVMetadataBuilder](../../topics/components/OH_AVMetadataBuilderStruct.md)* builder指向元数据构造器的实例。int64_t duration资源播放时长，以ms为单位。

**返回：**

类型说明[AVMetadata_Result](native_avmetadata.h.md#ZH-CN_TOPIC_0000002497445790__avmetadata_result)

AVMETADATA_SUCCESS：函数执行成功。

 AVMETADATA_ERROR_INVALID_PARAM：参数builder为nullptr。

#### OH_AVMetadataBuilder_SetMediaImageUri()

```ets
AVMetadata_Result OH_AVMetadataBuilder_SetMediaImageUri(OH_AVMetadataBuilder* builder, const char* mediaImageUri)
```

**描述**

设置媒体图片数据。

**起始版本：** 13

**参数：**

参数项描述[OH_AVMetadataBuilder](../../topics/components/OH_AVMetadataBuilderStruct.md)* builder指向元数据构造器的实例。const char* mediaImageUri网络资源图片数据地址。

**返回：**

类型说明[AVMetadata_Result](native_avmetadata.h.md#ZH-CN_TOPIC_0000002497445790__avmetadata_result)

AVMETADATA_SUCCESS：函数执行成功。

 AVMETADATA_ERROR_INVALID_PARAM：

 1. 参数builder为nullptr。

 2. 参数mediaImageUri为nullptr。

#### OH_AVMetadataBuilder_SetSubtitle()

```ets
AVMetadata_Result OH_AVMetadataBuilder_SetSubtitle(OH_AVMetadataBuilder* builder, const char* subtitle)
```

**描述**

设置副标题。

**起始版本：** 13

**参数：**

参数项描述[OH_AVMetadataBuilder](../../topics/components/OH_AVMetadataBuilderStruct.md)* builder指向元数据构造器的实例。const char* subtitle副标题名称。

**返回：**

类型说明[AVMetadata_Result](native_avmetadata.h.md#ZH-CN_TOPIC_0000002497445790__avmetadata_result)

AVMETADATA_SUCCESS：函数执行成功。

 AVMETADATA_ERROR_INVALID_PARAM：

 1. 参数builder为nullptr。

 2. 参数subtitle为nullptr。

#### OH_AVMetadataBuilder_SetDescription()

```ets
AVMetadata_Result OH_AVMetadataBuilder_SetDescription(OH_AVMetadataBuilder* builder, const char* description)
```

**描述**

设置媒体描述信息。

**起始版本：** 13

**参数：**

参数项描述[OH_AVMetadataBuilder](../../topics/components/OH_AVMetadataBuilderStruct.md)* builder指向元数据构造器的实例。const char* description媒体描述信息。

**返回：**

类型说明[AVMetadata_Result](native_avmetadata.h.md#ZH-CN_TOPIC_0000002497445790__avmetadata_result)

AVMETADATA_SUCCESS：函数执行成功。

 AVMETADATA_ERROR_INVALID_PARAM：

 1. 参数builder为nullptr。

 2. 参数description为nullptr。

#### OH_AVMetadataBuilder_SetLyric()

```ets
AVMetadata_Result OH_AVMetadataBuilder_SetLyric(OH_AVMetadataBuilder* builder, const char* lyric)
```

**描述**

设置歌词。

**起始版本：** 13

**参数：**

参数项描述[OH_AVMetadataBuilder](../../topics/components/OH_AVMetadataBuilderStruct.md)* builder指向元数据构造器的实例。const char* lyricLRC格式的歌词内容。

**返回：**

类型说明[AVMetadata_Result](native_avmetadata.h.md#ZH-CN_TOPIC_0000002497445790__avmetadata_result)

AVMETADATA_SUCCESS：函数执行成功。

 AVMETADATA_ERROR_INVALID_PARAM：

 1. 参数builder为nullptr。

 2. 参数lyric为nullptr。

#### OH_AVMetadataBuilder_SetSkipIntervals()

```ets
AVMetadata_Result OH_AVMetadataBuilder_SetSkipIntervals(OH_AVMetadataBuilder* builder,AVMetadata_SkipIntervals intervals)
```

**描述**

设置资源的跳转间隔时间。

**起始版本：** 13

**参数：**

参数项描述[OH_AVMetadataBuilder](../../topics/components/OH_AVMetadataBuilderStruct.md)* builder指向元数据构造器的实例。[AVMetadata_SkipIntervals](native_avmetadata.h.md#ZH-CN_TOPIC_0000002497445790__avmetadata_skipintervals) intervals跳转的时间间隔。

**返回：**

类型说明[AVMetadata_Result](native_avmetadata.h.md#ZH-CN_TOPIC_0000002497445790__avmetadata_result)

AVMETADATA_SUCCESS：函数执行成功。

 AVMETADATA_ERROR_INVALID_PARAM：

 1. 参数builder为nullptr。

 2. 参数intervals为无效。

#### OH_AVMetadataBuilder_SetDisplayTags()

```ets
AVMetadata_Result OH_AVMetadataBuilder_SetDisplayTags(OH_AVMetadataBuilder* builder, int32_t tags)
```

**描述**

设置媒体资源的金标类型。

**起始版本：** 13

**参数：**

参数项描述[OH_AVMetadataBuilder](../../topics/components/OH_AVMetadataBuilderStruct.md)* builder指向元数据构造器的实例。int32_t tags用于显示在播控的媒体资源的金标类型。

**返回：**

类型说明[AVMetadata_Result](native_avmetadata.h.md#ZH-CN_TOPIC_0000002497445790__avmetadata_result)

AVMETADATA_SUCCESS：函数执行成功。

 AVMETADATA_ERROR_INVALID_PARAM：参数builder为nullptr。

#### OH_AVMetadataBuilder_GenerateAVMetadata()

```ets
AVMetadata_Result OH_AVMetadataBuilder_GenerateAVMetadata(OH_AVMetadataBuilder* builder,OH_AVMetadata** avMetadata)
```

**描述**

生成媒体元数据对象。

**起始版本：** 13

**参数：**

参数项描述[OH_AVMetadataBuilder](../../topics/components/OH_AVMetadataBuilderStruct.md)* builder指向元数据构造器的实例。[OH_AVMetadata](../../topics/misc/OH_AVMetadataStruct.md)** avMetadata指向元数据的指针对象。

**返回：**

类型说明[AVMetadata_Result](native_avmetadata.h.md#ZH-CN_TOPIC_0000002497445790__avmetadata_result)

AVMETADATA_SUCCESS：函数执行成功。

 AVMETADATA_ERROR_NO_MEMORY：内存不足。

 AVMETADATA_ERROR_INVALID_PARAM：

 1. 参数builder为nullptr。

 2. 参数avMetadata为nullptr。

#### OH_AVMetadata_Destroy()

```ets
AVMetadata_Result OH_AVMetadata_Destroy(OH_AVMetadata* avMetadata)
```

**描述**

释放媒体元数据对象。

**起始版本：** 13

**参数：**

参数项描述[OH_AVMetadata](../../topics/misc/OH_AVMetadataStruct.md)* avMetadata指向元数据的指针对象。

**返回：**

类型说明[AVMetadata_Result](native_avmetadata.h.md#ZH-CN_TOPIC_0000002497445790__avmetadata_result)

AVMETADATA_SUCCESS：函数执行成功。

 AVMETADATA_ERROR_INVALID_PARAM：参数avMetadata为nullptr。