# native_avmetadata.h

**概述**

提供播控元数据的定义。

引用文件： <multimedia/av_session/native_avmetadata.h>

库： libohavsession.so

系统能力： SystemCapability.Multimedia.AVSession.Core

起始版本： 13

相关模块： [OHAVSession](OHAVSession.md)

**汇总**

**结构体**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| OH_AVMetadataBuilderStruct | OH_AVMetadataBuilder | 会话元数据构造器。构造器用于构造会话元数据。 |
| OH_AVMetadataStruct | OH_AVMetadata | 会话元数据。资源设置的avmetadata的实例。 |

**函数**

| 名称 | 描述 |
| --- | --- |
| AVMetadata_Result OH_AVMetadataBuilder_Create(OH_AVMetadataBuilder** builder) | 创建一个元数据构造器。 |
| AVMetadata_Result OH_AVMetadataBuilder_Destroy(OH_AVMetadataBuilder* builder) | 销毁元数据构造器。 |
| AVMetadata_Result OH_AVMetadataBuilder_SetAssetId(OH_AVMetadataBuilder* builder, const char* assetId) | 设置当前媒体资源id。 |
| AVMetadata_Result OH_AVMetadataBuilder_SetTitle(OH_AVMetadataBuilder* builder, const char* title) | 设置资源标题。 |
| AVMetadata_Result OH_AVMetadataBuilder_SetArtist(OH_AVMetadataBuilder* builder, const char* artist) | 设置资源所属的艺术家信息。 |
| AVMetadata_Result OH_AVMetadataBuilder_SetAuthor(OH_AVMetadataBuilder* builder, const char* author) | 设置资源的作者。 |
| AVMetadata_Result OH_AVMetadataBuilder_SetAlbum(OH_AVMetadataBuilder* builder, const char* album) | 设置资源专辑名称。 |
| AVMetadata_Result OH_AVMetadataBuilder_SetWriter(OH_AVMetadataBuilder* builder, const char* writer) | 设置资源词作者。 |
| AVMetadata_Result OH_AVMetadataBuilder_SetComposer(OH_AVMetadataBuilder* builder, const char* composer) | 设置资源作曲者。 |
| AVMetadata_Result OH_AVMetadataBuilder_SetDuration(OH_AVMetadataBuilder* builder, int64_t duration) | 设置资源播放时长。 |
| AVMetadata_Result OH_AVMetadataBuilder_SetMediaImageUri(OH_AVMetadataBuilder* builder, const char* mediaImageUri) | 设置媒体图片数据。 |
| AVMetadata_Result OH_AVMetadataBuilder_SetSubtitle(OH_AVMetadataBuilder* builder, const char* subtitle) | 设置副标题。 |
| AVMetadata_Result OH_AVMetadataBuilder_SetDescription(OH_AVMetadataBuilder* builder, const char* description) | 设置媒体描述信息。 |
| AVMetadata_Result OH_AVMetadataBuilder_SetLyric(OH_AVMetadataBuilder* builder, const char* lyric) | 设置歌词。 |
| AVMetadata_Result OH_AVMetadataBuilder_SetSkipIntervals(OH_AVMetadataBuilder* builder, AVMetadata_SkipIntervals intervals) | 设置资源的跳转间隔时间。 |
| AVMetadata_Result OH_AVMetadataBuilder_SetDisplayTags(OH_AVMetadataBuilder* builder, int32_t tags) | 设置媒体资源的金标类型。 |
| AVMetadata_Result OH_AVMetadataBuilder_SetFilter(OH_AVMetadataBuilder* builder, uint32_t filter) | 设置支持的协议。 |
| AVMetadata_Result OH_AVMetadataBuilder_GenerateAVMetadata(OH_AVMetadataBuilder* builder, OH_AVMetadata** avMetadata) | 生成媒体元数据对象。 |
| AVMetadata_Result OH_AVMetadata_Destroy(OH_AVMetadata* avMetadata) | 释放媒体元数据对象。 |

**函数说明**

**OH_AVMetadataBuilder_Create()**

```ets
AVMetadata_Result OH_AVMetadataBuilder_Create(OH_AVMetadataBuilder** builder)
```

描述

创建一个元数据构造器。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVMetadataBuilder** builder | 该引用指向创建的构造器实例。 |

返回：

| 类型 | 说明 |
| --- | --- |
| AVMetadata_Result | AVMETADATA_SUCCESS：函数执行成功。  AVMETADATA_ERROR_INVALID_PARAM：参数builder为nullptr。  AVMETADATA_ERROR_NO_MEMORY：内存不足。 |

**OH_AVMetadataBuilder_Destroy()**

```ets
AVMetadata_Result OH_AVMetadataBuilder_Destroy(OH_AVMetadataBuilder* builder)
```

描述

销毁元数据构造器。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVMetadataBuilder* builder | 指向元数据构造器的实例。 |

返回：

| 类型 | 说明 |
| --- | --- |
| AVMetadata_Result | AVMETADATA_SUCCESS：函数执行成功。  AVMETADATA_ERROR_INVALID_PARAM：参数builder为nullptr。 |

**OH_AVMetadataBuilder_SetAssetId()**

```ets
AVMetadata_Result OH_AVMetadataBuilder_SetAssetId(OH_AVMetadataBuilder* builder, const char* assetId)
```

描述

设置当前媒体资源id。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVMetadataBuilder* builder | 指向元数据构造器的实例。 |
| const char* assetId | 资源id。 |

返回：

| 类型 | 说明 |
| --- | --- |
| AVMetadata_Result | AVMETADATA_SUCCESS：函数执行成功。  AVMETADATA_ERROR_INVALID_PARAM：  1. 参数builder为nullptr。  2. 参数assetId为nullptr。 |

**OH_AVMetadataBuilder_SetTitle()**

```ets
AVMetadata_Result OH_AVMetadataBuilder_SetTitle(OH_AVMetadataBuilder* builder, const char* title)
```

描述

设置资源标题。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVMetadataBuilder* builder | 指向元数据构造器的实例。 |
| const char* title | 标题。 |

返回：

| 类型 | 说明 |
| --- | --- |
| AVMetadata_Result | AVMETADATA_SUCCESS：函数执行成功。  AVMETADATA_ERROR_INVALID_PARAM：  1. 参数builder为nullptr。  2. 参数title为nullptr。 |

**OH_AVMetadataBuilder_SetArtist()**

```ets
AVMetadata_Result OH_AVMetadataBuilder_SetArtist(OH_AVMetadataBuilder* builder, const char* artist)
```

描述

设置资源所属的艺术家信息。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVMetadataBuilder* builder | 指向元数据构造器的实例。 |
| const char* artist | 媒体资源的艺术家。 |

返回：

| 类型 | 说明 |
| --- | --- |
| AVMetadata_Result | AVMETADATA_SUCCESS：函数执行成功。  AVMETADATA_ERROR_INVALID_PARAM：  1. 参数builder为nullptr。  2. 参数artist为nullptr。 |

**OH_AVMetadataBuilder_SetAuthor()**

```ets
AVMetadata_Result OH_AVMetadataBuilder_SetAuthor(OH_AVMetadataBuilder* builder, const char* author)
```

描述

设置资源的作者。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVMetadataBuilder* builder | 指向元数据构造器的实例。 |
| const char* author | 作者。 |

返回：

| 类型 | 说明 |
| --- | --- |
| AVMetadata_Result | AVMETADATA_SUCCESS：函数执行成功。  AVMETADATA_ERROR_INVALID_PARAM：  1. 参数builder为nullptr。  2. 参数author为nullptr。 |

**OH_AVMetadataBuilder_SetAlbum()**

```ets
AVMetadata_Result OH_AVMetadataBuilder_SetAlbum(OH_AVMetadataBuilder* builder, const char* album)
```

描述

设置资源专辑名称。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVMetadataBuilder* builder | 指向元数据构造器的实例。 |
| const char* album | 专辑名。 |

返回：

| 类型 | 说明 |
| --- | --- |
| AVMetadata_Result | AVMETADATA_SUCCESS：函数执行成功。  AVMETADATA_ERROR_INVALID_PARAM：  1. 参数builder为nullptr。  2. 参数album为nullptr。 |

**OH_AVMetadataBuilder_SetWriter()**

```ets
AVMetadata_Result OH_AVMetadataBuilder_SetWriter(OH_AVMetadataBuilder* builder, const char* writer)
```

描述

设置资源词作者。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVMetadataBuilder* builder | 指向元数据构造器的实例。 |
| const char* writer | 词作者。 |

返回：

| 类型 | 说明 |
| --- | --- |
| AVMetadata_Result | AVMETADATA_SUCCESS：函数执行成功。  AVMETADATA_ERROR_INVALID_PARAM：  1. 参数builder为nullptr。  2. 参数writer为nullptr。 |

**OH_AVMetadataBuilder_SetComposer()**

```ets
AVMetadata_Result OH_AVMetadataBuilder_SetComposer(OH_AVMetadataBuilder* builder, const char* composer)
```

描述

设置资源作曲者。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVMetadataBuilder* builder | 指向元数据构造器的实例。 |
| const char* composer | 作曲者。 |

返回：

| 类型 | 说明 |
| --- | --- |
| AVMetadata_Result | AVMETADATA_SUCCESS：函数执行成功。  AVMETADATA_ERROR_INVALID_PARAM：  1. 参数builder为nullptr。  2. 参数composer为nullptr。 |

**OH_AVMetadataBuilder_SetDuration()**

```ets
AVMetadata_Result OH_AVMetadataBuilder_SetDuration(OH_AVMetadataBuilder* builder, int64_t duration)
```

描述

设置资源播放时长。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVMetadataBuilder* builder | 指向元数据构造器的实例。 |
| int64_t duration | 资源播放时长，以ms为单位。 |

返回：

| 类型 | 说明 |
| --- | --- |
| AVMetadata_Result | AVMETADATA_SUCCESS：函数执行成功。  AVMETADATA_ERROR_INVALID_PARAM：参数builder为nullptr。 |

**OH_AVMetadataBuilder_SetMediaImageUri()**

```ets
AVMetadata_Result OH_AVMetadataBuilder_SetMediaImageUri(OH_AVMetadataBuilder* builder, const char* mediaImageUri)
```

描述

设置媒体图片数据。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVMetadataBuilder* builder | 指向元数据构造器的实例。 |
| const char* mediaImageUri | 网络资源图片数据地址。 |

返回：

| 类型 | 说明 |
| --- | --- |
| AVMetadata_Result | AVMETADATA_SUCCESS：函数执行成功。  AVMETADATA_ERROR_INVALID_PARAM：  1. 参数builder为nullptr。  2. 参数mediaImageUri为nullptr。 |

**OH_AVMetadataBuilder_SetSubtitle()**

```ets
AVMetadata_Result OH_AVMetadataBuilder_SetSubtitle(OH_AVMetadataBuilder* builder, const char* subtitle)
```

描述

设置副标题。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVMetadataBuilder* builder | 指向元数据构造器的实例。 |
| const char* subtitle | 副标题名称。 |

返回：

| 类型 | 说明 |
| --- | --- |
| AVMetadata_Result | AVMETADATA_SUCCESS：函数执行成功。  AVMETADATA_ERROR_INVALID_PARAM：  1. 参数builder为nullptr。  2. 参数subtitle为nullptr。 |

**OH_AVMetadataBuilder_SetDescription()**

```ets
AVMetadata_Result OH_AVMetadataBuilder_SetDescription(OH_AVMetadataBuilder* builder, const char* description)
```

描述

设置媒体描述信息。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVMetadataBuilder* builder | 指向元数据构造器的实例。 |
| const char* description | 媒体描述信息。 |

返回：

| 类型 | 说明 |
| --- | --- |
| AVMetadata_Result | AVMETADATA_SUCCESS：函数执行成功。  AVMETADATA_ERROR_INVALID_PARAM：  1. 参数builder为nullptr。  2. 参数description为nullptr。 |

**OH_AVMetadataBuilder_SetLyric()**

```ets
AVMetadata_Result OH_AVMetadataBuilder_SetLyric(OH_AVMetadataBuilder* builder, const char* lyric)
```

描述

设置歌词。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVMetadataBuilder* builder | 指向元数据构造器的实例。 |
| const char* lyric | LRC格式的歌词内容。 |

返回：

| 类型 | 说明 |
| --- | --- |
| AVMetadata_Result | AVMETADATA_SUCCESS：函数执行成功。  AVMETADATA_ERROR_INVALID_PARAM：  1. 参数builder为nullptr。  2. 参数lyric为nullptr。 |

**OH_AVMetadataBuilder_SetSkipIntervals()**

```ets
AVMetadata_Result OH_AVMetadataBuilder_SetSkipIntervals(OH_AVMetadataBuilder* builder, AVMetadata_SkipIntervals intervals)
```

描述

设置资源的跳转间隔时间。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVMetadataBuilder* builder | 指向元数据构造器的实例。 |
| AVMetadata_SkipIntervals intervals | 跳转的时间间隔。 |

返回：

| 类型 | 说明 |
| --- | --- |
| AVMetadata_Result | AVMETADATA_SUCCESS：函数执行成功。  AVMETADATA_ERROR_INVALID_PARAM：  1. 参数builder为nullptr。  2. 参数intervals为nullptr。 |

**OH_AVMetadataBuilder_SetDisplayTags()**

```ets
AVMetadata_Result OH_AVMetadataBuilder_SetDisplayTags(OH_AVMetadataBuilder* builder, int32_t tags)
```

描述

设置媒体资源的金标类型。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVMetadataBuilder* builder | 指向元数据构造器的实例。 |
| int32_t tags | 用于显示在播控的媒体资源的金标类型。 |

返回：

| 类型 | 说明 |
| --- | --- |
| AVMetadata_Result | AVMETADATA_SUCCESS：函数执行成功。  AVMETADATA_ERROR_INVALID_PARAM：参数builder为nullptr。 |

**OH_AVMetadataBuilder_SetFilter()**

```ets
AVMetadata_Result OH_AVMetadataBuilder_SetFilter(OH_AVMetadataBuilder* builder, uint32_t filter)
```

描述

设置支持的协议。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVMetadataBuilder* builder | 指向元数据构造器的实例。 |
| uint32_t filter | 此会话支持的协议。如果没有设置，默认为AVSession_ProtocolType.TYPE_CAST_PLUS_STREAM。 |

返回：

| 类型 | 说明 |
| --- | --- |
| AVMetadata_Result | AVMETADATA_SUCCESS：函数执行成功。  AVMETADATA_ERROR_INVALID_PARAM：  1. 参数builder为nullptr。  2. 参数filter是无效的。 |

**OH_AVMetadataBuilder_GenerateAVMetadata()**

```ets
AVMetadata_Result OH_AVMetadataBuilder_GenerateAVMetadata(OH_AVMetadataBuilder* builder, OH_AVMetadata** avMetadata)
```

描述

生成媒体元数据对象。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVMetadataBuilder* builder | 指向元数据构造器的实例。 |
| OH_AVMetadata** avMetadata | 指向元数据的指针对象。 |

返回：

| 类型 | 说明 |
| --- | --- |
| AVMetadata_Result | AVMETADATA_SUCCESS：函数执行成功。  AVMETADATA_ERROR_NO_MEMORY：内存不足。  AVMETADATA_ERROR_INVALID_PARAM：  1. 参数builder为nullptr。  2. 参数avMetadata为nullptr。 |

**OH_AVMetadata_Destroy()**

```ets
AVMetadata_Result OH_AVMetadata_Destroy(OH_AVMetadata* avMetadata)
```

描述

释放媒体元数据对象。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVMetadata* avMetadata | 指向元数据的指针对象。 |

返回：

| 类型 | 说明 |
| --- | --- |
| AVMetadata_Result | AVMETADATA_SUCCESS：函数执行成功。  AVMETADATA_ERROR_INVALID_PARAM：参数avMetadata为nullptr。 |