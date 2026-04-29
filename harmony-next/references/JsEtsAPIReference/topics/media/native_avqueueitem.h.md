# native_avqueueitem.h

**概述**

提供音视频队列元素的定义。

引用文件： <multimedia/av_session/native_avqueueitem.h>

库： libohavsession.so

系统能力： SystemCapability.Multimedia.AVSession.Core

起始版本： 23

相关模块： [OHAVSession](OHAVSession.md)

**汇总**

**结构体**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| OH_AVSession_AVQueueItem | OH_AVSession_AVQueueItem | 音视频队列元素的定义。 |
| OH_AVSession_AVMediaDescription | OH_AVSession_AVMediaDescription | AVMediaDescription的声明。应用为当前资源设置的音视频媒体描述实例。 |
| OH_AVSession_AVMediaDescriptionBuilder | OH_AVSession_AVMediaDescriptionBuilder | 音视频媒体描述构建器的声明。构建器的实例用于创建媒体描述信息。 |

**函数**

| 名称 | 描述 |
| --- | --- |
| AVQueueItem_Result OH_AVSession_AVMediaDescriptionBuilder_Create(OH_AVSession_AVMediaDescriptionBuilder** builder) | 创建OH_AVSession_AVMediaDescriptionBuilder实例。当该实例不再被使用时，调用OH_AVSession_AVMediaDescriptionBuilder_Destroy来释放构建器对象。 |
| AVQueueItem_Result OH_AVSession_AVMediaDescriptionBuilder_Destroy(OH_AVSession_AVMediaDescriptionBuilder* builder) | 销毁构建器。 |
| AVQueueItem_Result OH_AVSession_AVMediaDescriptionBuilder_SetAssetId(OH_AVSession_AVMediaDescriptionBuilder* builder, const char* assetId) | 设置媒体资源的当前资产ID。 |
| AVQueueItem_Result OH_AVSession_AVMediaDescriptionBuilder_SetTitle(OH_AVSession_AVMediaDescriptionBuilder* builder, const char* title) | 设置媒体资源的标题。 |
| AVQueueItem_Result OH_AVSession_AVMediaDescriptionBuilder_SetSubTitle(OH_AVSession_AVMediaDescriptionBuilder* builder, const char* subtitle) | 设置媒体资源的副标题。 |
| AVQueueItem_Result OH_AVSession_AVMediaDescriptionBuilder_SetArtist(OH_AVSession_AVMediaDescriptionBuilder* builder, const char* artist) | 设置媒体资源的艺术家信息。 |
| AVQueueItem_Result OH_AVSession_AVMediaDescriptionBuilder_SetAlbumCoverUri(OH_AVSession_AVMediaDescriptionBuilder* builder, const char* albumCoverUri) | 设置媒体资源的媒体图像URL。 |
| AVQueueItem_Result OH_AVSession_AVMediaDescriptionBuilder_SetMediaType(OH_AVSession_AVMediaDescriptionBuilder* builder, const char* mediaType) | 设置媒体资源的媒体类型。 |
| AVQueueItem_Result OH_AVSession_AVMediaDescriptionBuilder_SetLyricContent(OH_AVSession_AVMediaDescriptionBuilder* builder, const char* lyricContent) | 设置媒体资源的歌词内容。 |
| AVQueueItem_Result OH_AVSession_AVMediaDescriptionBuilder_SetDuration(OH_AVSession_AVMediaDescriptionBuilder* builder, const int32_t duration) | 设置媒体资源的持续时间。 |
| AVQueueItem_Result OH_AVSession_AVMediaDescriptionBuilder_SetMediaUri(OH_AVSession_AVMediaDescriptionBuilder* builder, const char* mediaUri) | 设置媒体资源的媒体URI。 |
| AVQueueItem_Result OH_AVSession_AVMediaDescriptionBuilder_SetStartPosition(OH_AVSession_AVMediaDescriptionBuilder* builder, const int32_t startPosition) | 设置媒体资源的起始位置。 |
| AVQueueItem_Result OH_AVSession_AVMediaDescriptionBuilder_SetMediaSize(OH_AVSession_AVMediaDescriptionBuilder* builder, const int32_t mediaSize) | 设置媒体资源的大小。 |
| AVQueueItem_Result OH_AVSession_AVMediaDescriptionBuilder_SetAlbumTitle(OH_AVSession_AVMediaDescriptionBuilder* builder, const char* albumTitle) | 设置媒体资源的专辑标题。 |
| AVQueueItem_Result OH_AVSession_AVMediaDescriptionBuilder_SetAppName(OH_AVSession_AVMediaDescriptionBuilder* builder, const char* appName) | 设置媒体资源来源的应用名称。 |
| AVQueueItem_Result OH_AVSession_AVMediaDescription_GetAssetId(OH_AVSession_AVMediaDescription* description, char** assetId) | 获取媒体资源的当前资产ID。 |
| AVQueueItem_Result OH_AVSession_AVMediaDescription_GetTitle(OH_AVSession_AVMediaDescription* description, char** title) | 获取媒体资源的标题。 |
| AVQueueItem_Result OH_AVSession_AVMediaDescription_GetSubtitle(OH_AVSession_AVMediaDescription* description, char** subtitle) | 获取媒体资源的副标题。 |
| AVQueueItem_Result OH_AVSession_AVMediaDescription_GetArtist(OH_AVSession_AVMediaDescription* description, char** artist) | 获取媒体资源的艺术家信息。 |
| AVQueueItem_Result OH_AVSession_AVMediaDescription_GetAlbumCoverUri(OH_AVSession_AVMediaDescription* description, char** albumCoverUri) | 获取媒体资源的媒体图像URL。 |
| AVQueueItem_Result OH_AVSession_AVMediaDescription_GetMediaType(OH_AVSession_AVMediaDescription* description, char** mediaType) | 获取媒体类型信息。 |
| AVQueueItem_Result OH_AVSession_AVMediaDescription_GetLyricContent(OH_AVSession_AVMediaDescription* description, char** lyricContent) | 获取资源的歌词内容。 |
| AVQueueItem_Result OH_AVSession_AVMediaDescription_GetDuration(OH_AVSession_AVMediaDescription* description, int32_t* duration) | 获取媒体资源的持续时间。 |
| AVQueueItem_Result OH_AVSession_AVMediaDescription_GetMediaUri(OH_AVSession_AVMediaDescription* description, char** mediaUri) | 获取媒体资源的媒体URI。 |
| AVQueueItem_Result OH_AVSession_AVMediaDescription_GetStartPosition(OH_AVSession_AVMediaDescription* description, int32_t* startPosition) | 获取媒体资源的起始位置。 |
| AVQueueItem_Result OH_AVSession_AVMediaDescription_GetMediaSize(OH_AVSession_AVMediaDescription* description, int32_t* mediaSize) | 获取资源的媒体大小。 |
| AVQueueItem_Result OH_AVSession_AVMediaDescription_GetAlbumTitle(OH_AVSession_AVMediaDescription* description, char** albumTitle) | 获取媒体资源的专辑标题。 |
| AVQueueItem_Result OH_AVSession_AVMediaDescription_GetAppName(OH_AVSession_AVMediaDescription* description, char** appName) | 获取媒体资源的应用名。 |
| AVQueueItem_Result OH_AVSession_AVMediaDescriptionBuilder_GenerateAVMediaDescription(OH_AVSession_AVMediaDescriptionBuilder* builder, OH_AVSession_AVMediaDescription** avMediaDescription) | 创建avMediaDescription对象。当该对象不再使用时，调用OH_AVSession_AVMediaDescription_Destroy释放avMediaDescription对象。 |
| AVQueueItem_Result OH_AVSession_AVMediaDescription_Destroy(OH_AVSession_AVMediaDescription* avMediaDescription) | 释放avMediaDescription对象。 |

**函数说明**

**OH_AVSession_AVMediaDescriptionBuilder_Create()**

```ets
AVQueueItem_Result OH_AVSession_AVMediaDescriptionBuilder_Create(OH_AVSession_AVMediaDescriptionBuilder** builder)
```

描述

创建OH_AVSession_AVMediaDescriptionBuilder实例。当该实例不再被使用时，调用[OH_AVSession_AVMediaDescriptionBuilder_Destroy](native_avqueueitem.h.md#ZH-CN_TOPIC_0000002553361813__oh_avsession_avmediadescriptionbuilder_destroy)来释放构建器对象。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVSession_AVMediaDescriptionBuilder** builder | 指向创建结果的构建器对象。 |

返回：

| 类型 | 说明 |
| --- | --- |
| AVQueueItem_Result | AVQUEUEITEM_SUCCESS：函数执行成功。  AVQUEUEITEM_ERROR_INVALID_PARAM：参数builder为nullptr。  AVQUEUEITEM_ERROR_NO_MEMORY：内存不足。 |

**OH_AVSession_AVMediaDescriptionBuilder_Destroy()**

```ets
AVQueueItem_Result OH_AVSession_AVMediaDescriptionBuilder_Destroy(OH_AVSession_AVMediaDescriptionBuilder* builder)
```

描述

销毁构建器。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVSession_AVMediaDescriptionBuilder* builder | 表示音视频媒体描述构建器实例指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| AVQueueItem_Result | AVQUEUEITEM_SUCCESS：函数执行成功。  AVQUEUEITEM_ERROR_INVALID_PARAM：参数builder为nullptr。 |

**OH_AVSession_AVMediaDescriptionBuilder_SetAssetId()**

```ets
AVQueueItem_Result OH_AVSession_AVMediaDescriptionBuilder_SetAssetId(OH_AVSession_AVMediaDescriptionBuilder* builder, const char* assetId)
```

描述

设置媒体资源的当前资产ID。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVSession_AVMediaDescriptionBuilder* builder | 表示音视频媒体描述构建器实例指针。 |
| const char* assetId | 媒体资源的当前资产ID。 |

返回：

| 类型 | 说明 |
| --- | --- |
| AVQueueItem_Result | AVQUEUEITEM_SUCCESS：函数执行成功。  AVQUEUEITEM_ERROR_INVALID_PARAM：  1. 参数builder为nullptr。  2. 参数assetId为nullptr。 |

**OH_AVSession_AVMediaDescriptionBuilder_SetTitle()**

```ets
AVQueueItem_Result OH_AVSession_AVMediaDescriptionBuilder_SetTitle(OH_AVSession_AVMediaDescriptionBuilder* builder, const char* title)
```

描述

设置媒体资源的标题。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVSession_AVMediaDescriptionBuilder* builder | 表示音视频媒体描述构建器实例指针。 |
| const char* title | 媒体资源的标题。 |

返回：

| 类型 | 说明 |
| --- | --- |
| AVQueueItem_Result | AVQUEUEITEM_SUCCESS：函数执行成功。  AVQUEUEITEM_ERROR_INVALID_PARAM：  1. 参数builder为nullptr。  2. 参数title为nullptr。 |

**OH_AVSession_AVMediaDescriptionBuilder_SetSubTitle()**

```ets
AVQueueItem_Result OH_AVSession_AVMediaDescriptionBuilder_SetSubTitle(OH_AVSession_AVMediaDescriptionBuilder* builder, const char* subtitle)
```

描述

设置媒体资源的副标题。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVSession_AVMediaDescriptionBuilder* builder | 表示音视频媒体描述构建器实例指针。 |
| const char* subtitle | 媒体资源的副标题。 |

返回：

| 类型 | 说明 |
| --- | --- |
| AVQueueItem_Result | AVQUEUEITEM_SUCCESS：函数执行成功。  AVQUEUEITEM_ERROR_INVALID_PARAM：  1. 参数builder为nullptr。  2. 参数subtitle为nullptr。 |

**OH_AVSession_AVMediaDescriptionBuilder_SetArtist()**

```ets
AVQueueItem_Result OH_AVSession_AVMediaDescriptionBuilder_SetArtist(OH_AVSession_AVMediaDescriptionBuilder* builder, const char* artist)
```

描述

设置媒体资源的艺术家信息。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVSession_AVMediaDescriptionBuilder* builder | 表示音视频媒体描述构建器实例指针。 |
| const char* artist | 媒体资源的艺术家。 |

返回：

| 类型 | 说明 |
| --- | --- |
| AVQueueItem_Result | AVQUEUEITEM_SUCCESS：函数执行成功。  AVQUEUEITEM_ERROR_INVALID_PARAM：  1. 参数builder为nullptr。  2. 参数artist为nullptr。 |

**OH_AVSession_AVMediaDescriptionBuilder_SetAlbumCoverUri()**

```ets
AVQueueItem_Result OH_AVSession_AVMediaDescriptionBuilder_SetAlbumCoverUri(OH_AVSession_AVMediaDescriptionBuilder* builder, const char* albumCoverUri)
```

描述

设置媒体资源的媒体图像URL。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVSession_AVMediaDescriptionBuilder* builder | 表示音视频媒体描述构建器实例指针。 |
| const char* albumCoverUri | 在媒体中心显示的资源的图像URL。 |

返回：

| 类型 | 说明 |
| --- | --- |
| AVQueueItem_Result | AVQUEUEITEM_SUCCESS：函数执行成功。  AVQUEUEITEM_ERROR_INVALID_PARAM：  1. 参数builder为nullptr。  2. 参数albumCoverUri为nullptr。 |

**OH_AVSession_AVMediaDescriptionBuilder_SetMediaType()**

```ets
AVQueueItem_Result OH_AVSession_AVMediaDescriptionBuilder_SetMediaType(OH_AVSession_AVMediaDescriptionBuilder* builder, const char* mediaType)
```

描述

设置媒体资源的媒体类型。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVSession_AVMediaDescriptionBuilder* builder | 表示音视频媒体描述构建器实例指针。 |
| const char* mediaType | 媒体资源的媒体类型。如VIDEO或AUDIO。 |

返回：

| 类型 | 说明 |
| --- | --- |
| AVQueueItem_Result | AVQUEUEITEM_SUCCESS：函数执行成功。  AVQUEUEITEM_ERROR_INVALID_PARAM：  1. 参数builder为nullptr。  2. 参数mediaType为nullptr。 |

**OH_AVSession_AVMediaDescriptionBuilder_SetLyricContent()**

```ets
AVQueueItem_Result OH_AVSession_AVMediaDescriptionBuilder_SetLyricContent(OH_AVSession_AVMediaDescriptionBuilder* builder, const char* lyricContent)
```

描述

设置媒体资源的歌词内容。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVSession_AVMediaDescriptionBuilder* builder | 表示音视频媒体描述构建器实例指针。 |
| const char* lyricContent | 媒体资源的歌词内容。为LRC（Lyric Reduced Codec）格式。 |

返回：

| 类型 | 说明 |
| --- | --- |
| AVQueueItem_Result | AVQUEUEITEM_SUCCESS：函数执行成功。  AVQUEUEITEM_ERROR_INVALID_PARAM：  1. 参数builder为nullptr。  2. 参数lyricContent为nullptr。 |

**OH_AVSession_AVMediaDescriptionBuilder_SetDuration()**

```ets
AVQueueItem_Result OH_AVSession_AVMediaDescriptionBuilder_SetDuration(OH_AVSession_AVMediaDescriptionBuilder* builder, const int32_t duration)
```

描述

设置媒体资源的持续时间。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVSession_AVMediaDescriptionBuilder* builder | 表示音视频媒体描述构建器实例指针。 |
| const int32_t duration | 媒体资源的持续时间。单位为毫秒。 |

返回：

| 类型 | 说明 |
| --- | --- |
| AVQueueItem_Result | AVQUEUEITEM_SUCCESS：函数执行成功。  AVQUEUEITEM_ERROR_INVALID_PARAM：  1. 参数builder为nullptr。  2. 参数duration为nullptr。 |

**OH_AVSession_AVMediaDescriptionBuilder_SetMediaUri()**

```ets
AVQueueItem_Result OH_AVSession_AVMediaDescriptionBuilder_SetMediaUri(OH_AVSession_AVMediaDescriptionBuilder* builder, const char* mediaUri)
```

描述

设置媒体资源的媒体URI。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVSession_AVMediaDescriptionBuilder* builder | 表示音视频媒体描述构建器实例指针。 |
| const char* mediaUri | 媒体资源的URI。 |

返回：

| 类型 | 说明 |
| --- | --- |
| AVQueueItem_Result | AVQUEUEITEM_SUCCESS：函数执行成功。  AVQUEUEITEM_ERROR_INVALID_PARAM：  1. 参数builder为nullptr。  2. 参数mediaUri为nullptr。 |

**OH_AVSession_AVMediaDescriptionBuilder_SetStartPosition()**

```ets
AVQueueItem_Result OH_AVSession_AVMediaDescriptionBuilder_SetStartPosition(OH_AVSession_AVMediaDescriptionBuilder* builder, const int32_t startPosition)
```

描述

设置媒体资源的起始位置。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVSession_AVMediaDescriptionBuilder* builder | 表示音视频媒体描述构建器实例指针。 |
| const int32_t startPosition | 媒体资源的起始位置。 |

返回：

| 类型 | 说明 |
| --- | --- |
| AVQueueItem_Result | AVQUEUEITEM_SUCCESS：函数执行成功。  AVQUEUEITEM_ERROR_INVALID_PARAM：  1. 参数builder为nullptr。  2. 参数startPosition是无效的。 |

**OH_AVSession_AVMediaDescriptionBuilder_SetMediaSize()**

```ets
AVQueueItem_Result OH_AVSession_AVMediaDescriptionBuilder_SetMediaSize(OH_AVSession_AVMediaDescriptionBuilder* builder, const int32_t mediaSize)
```

描述

设置媒体资源的大小。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVSession_AVMediaDescriptionBuilder* builder | 表示音视频媒体描述构建器实例指针。 |
| const int32_t mediaSize | 媒体资源的大小。 |

返回：

| 类型 | 说明 |
| --- | --- |
| AVQueueItem_Result | AVQUEUEITEM_SUCCESS：函数执行成功。  AVQUEUEITEM_ERROR_INVALID_PARAM：  1. 参数builder为nullptr。  2. 参数mediaSize是无效的。 |

**OH_AVSession_AVMediaDescriptionBuilder_SetAlbumTitle()**

```ets
AVQueueItem_Result OH_AVSession_AVMediaDescriptionBuilder_SetAlbumTitle(OH_AVSession_AVMediaDescriptionBuilder* builder, const char* albumTitle)
```

描述

设置媒体资源的专辑标题。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVSession_AVMediaDescriptionBuilder* builder | 表示音视频媒体描述构建器实例指针。 |
| const char* albumTitle | 媒体资源的专辑标题。 |

返回：

| 类型 | 说明 |
| --- | --- |
| AVQueueItem_Result | AVQUEUEITEM_SUCCESS：函数执行成功。  AVQUEUEITEM_ERROR_INVALID_PARAM：  1. 参数builder为nullptr。  2. 参数albumTitle为nullptr。 |

**OH_AVSession_AVMediaDescriptionBuilder_SetAppName()**

```ets
AVQueueItem_Result OH_AVSession_AVMediaDescriptionBuilder_SetAppName(OH_AVSession_AVMediaDescriptionBuilder* builder, const char* appName)
```

描述

设置媒体资源来源的应用名称。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVSession_AVMediaDescriptionBuilder* builder | 表示音视频媒体描述构建器实例指针。 |
| const char* appName | 媒体资源来源的应用名称。 |

返回：

| 类型 | 说明 |
| --- | --- |
| AVQueueItem_Result | AVQUEUEITEM_SUCCESS：函数执行成功。  AVQUEUEITEM_ERROR_INVALID_PARAM：  1. 参数builder为nullptr。  2. 参数appName为nullptr。 |

**OH_AVSession_AVMediaDescription_GetAssetId()**

```ets
AVQueueItem_Result OH_AVSession_AVMediaDescription_GetAssetId(OH_AVSession_AVMediaDescription* description, char** assetId)
```

描述

获取媒体资源的当前资产ID。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVSession_AVMediaDescription* description | 表示音视频媒体描述实例指针。 |
| char** assetId | 指针变量将返回媒体资源的当前资产ID。 |

返回：

| 类型 | 说明 |
| --- | --- |
| AVQueueItem_Result | AVQUEUEITEM_SUCCESS：函数执行成功。  AVQUEUEITEM_ERROR_INVALID_PARAM：  1. 参数description为nullptr。  2. 参数assetId为nullptr。 |

**OH_AVSession_AVMediaDescription_GetTitle()**

```ets
AVQueueItem_Result OH_AVSession_AVMediaDescription_GetTitle(OH_AVSession_AVMediaDescription* description, char** title)
```

描述

获取媒体资源的标题。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVSession_AVMediaDescription* description | 表示音视频媒体描述实例指针。 |
| char** title | 指针变量将返回当前媒体资源的标题。 |

返回：

| 类型 | 说明 |
| --- | --- |
| AVQueueItem_Result | AVQUEUEITEM_SUCCESS：函数执行成功。  AVQUEUEITEM_ERROR_INVALID_PARAM：  1. 参数description为nullptr。  2. 参数title为nullptr。 |

**OH_AVSession_AVMediaDescription_GetSubtitle()**

```ets
AVQueueItem_Result OH_AVSession_AVMediaDescription_GetSubtitle(OH_AVSession_AVMediaDescription* description, char** subtitle)
```

描述

获取媒体资源的副标题。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVSession_AVMediaDescription* description | 表示音视频媒体描述实例指针。 |
| char** subtitle | 指针变量将返回当前媒体资源的副标题。 |

返回：

| 类型 | 说明 |
| --- | --- |
| AVQueueItem_Result | AVQUEUEITEM_SUCCESS：函数执行成功。  AVQUEUEITEM_ERROR_INVALID_PARAM：  1. 参数description为nullptr。  2. 参数subtitle为nullptr。 |

**OH_AVSession_AVMediaDescription_GetArtist()**

```ets
AVQueueItem_Result OH_AVSession_AVMediaDescription_GetArtist(OH_AVSession_AVMediaDescription* description, char** artist)
```

描述

获取媒体资源的艺术家信息。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVSession_AVMediaDescription* description | 表示音视频媒体描述实例指针。 |
| char** artist | 指针变量将返回当前媒体资源的艺术家信息。 |

返回：

| 类型 | 说明 |
| --- | --- |
| AVQueueItem_Result | AVQUEUEITEM_SUCCESS：函数执行成功。  AVQUEUEITEM_ERROR_INVALID_PARAM：  1. 参数description为nullptr。  2. 参数artist为nullptr。 |

**OH_AVSession_AVMediaDescription_GetAlbumCoverUri()**

```ets
AVQueueItem_Result OH_AVSession_AVMediaDescription_GetAlbumCoverUri(OH_AVSession_AVMediaDescription* description, char** albumCoverUri)
```

描述

获取媒体资源的媒体图像URL。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVSession_AVMediaDescription* description | 表示音视频媒体描述实例指针。 |
| char** albumCoverUri | 指针变量将返回资源的媒体图像URL。 |

返回：

| 类型 | 说明 |
| --- | --- |
| AVQueueItem_Result | AVQUEUEITEM_SUCCESS：函数执行成功。  AVQUEUEITEM_ERROR_INVALID_PARAM：  1. 参数description为nullptr。  2. 参数albumCoverUri为nullptr。 |

**OH_AVSession_AVMediaDescription_GetMediaType()**

```ets
AVQueueItem_Result OH_AVSession_AVMediaDescription_GetMediaType(OH_AVSession_AVMediaDescription* description, char** mediaType)
```

描述

获取媒体类型信息。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVSession_AVMediaDescription* description | 表示音视频媒体描述实例指针。 |
| char** mediaType | 指针变量将返回当前媒体类型。 |

返回：

| 类型 | 说明 |
| --- | --- |
| AVQueueItem_Result | AVQUEUEITEM_SUCCESS：函数执行成功。  AVQUEUEITEM_ERROR_INVALID_PARAM：  1. 参数description为nullptr。  2. 参数mediaType为nullptr。 |

**OH_AVSession_AVMediaDescription_GetLyricContent()**

```ets
AVQueueItem_Result OH_AVSession_AVMediaDescription_GetLyricContent(OH_AVSession_AVMediaDescription* description, char** lyricContent)
```

描述

获取资源的歌词内容。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVSession_AVMediaDescription* description | 表示音视频媒体描述实例指针。 |
| char** lyricContent | 指针变量将返回当前媒体歌词内容。 |

返回：

| 类型 | 说明 |
| --- | --- |
| AVQueueItem_Result | AVQUEUEITEM_SUCCESS：函数执行成功。  AVQUEUEITEM_ERROR_INVALID_PARAM：  1. 参数description为nullptr。  2. 参数lyricContent为nullptr。 |

**OH_AVSession_AVMediaDescription_GetDuration()**

```ets
AVQueueItem_Result OH_AVSession_AVMediaDescription_GetDuration(OH_AVSession_AVMediaDescription* description, int32_t* duration)
```

描述

获取媒体资源的持续时间。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVSession_AVMediaDescription* description | 表示音视频媒体描述实例指针。 |
| int32_t* duration | 指针变量将返回当前媒体资源的总时长。 |

返回：

| 类型 | 说明 |
| --- | --- |
| AVQueueItem_Result | AVQUEUEITEM_SUCCESS：函数执行成功。  AVQUEUEITEM_ERROR_INVALID_PARAM：  1. 参数description为nullptr。  2. 参数duration为nullptr。 |

**OH_AVSession_AVMediaDescription_GetMediaUri()**

```ets
AVQueueItem_Result OH_AVSession_AVMediaDescription_GetMediaUri(OH_AVSession_AVMediaDescription* description, char** mediaUri)
```

描述

获取媒体资源的媒体URI。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVSession_AVMediaDescription* description | 表示音视频媒体描述实例指针。 |
| char** mediaUri | 指针变量将返回当前媒体资源标识符。 |

返回：

| 类型 | 说明 |
| --- | --- |
| AVQueueItem_Result | AVQUEUEITEM_SUCCESS：函数执行成功。  AVQUEUEITEM_ERROR_INVALID_PARAM：  1. 参数description为nullptr。  2. 参数mediaUri为nullptr。 |

**OH_AVSession_AVMediaDescription_GetStartPosition()**

```ets
AVQueueItem_Result OH_AVSession_AVMediaDescription_GetStartPosition(OH_AVSession_AVMediaDescription* description, int32_t* startPosition)
```

描述

获取媒体资源的起始位置。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVSession_AVMediaDescription* description | 表示音视频媒体描述实例指针。 |
| int32_t* startPosition | 指针变量将返回当前媒体资源开始的位置。 |

返回：

| 类型 | 说明 |
| --- | --- |
| AVQueueItem_Result | AVQUEUEITEM_SUCCESS：函数执行成功。  AVQUEUEITEM_ERROR_INVALID_PARAM：  1. 参数description为nullptr。  2. 参数startPosition为nullptr。 |

**OH_AVSession_AVMediaDescription_GetMediaSize()**

```ets
AVQueueItem_Result OH_AVSession_AVMediaDescription_GetMediaSize(OH_AVSession_AVMediaDescription* description, int32_t* mediaSize)
```

描述

获取资源的媒体大小。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVSession_AVMediaDescription* description | 表示音视频媒体描述实例指针。 |
| int32_t* mediaSize | 指针变量将返回当前媒体资源的大小。 |

返回：

| 类型 | 说明 |
| --- | --- |
| AVQueueItem_Result | AVQUEUEITEM_SUCCESS：函数执行成功。  AVQUEUEITEM_ERROR_INVALID_PARAM：  1. 参数description为nullptr。  2. 参数mediaSize为nullptr。 |

**OH_AVSession_AVMediaDescription_GetAlbumTitle()**

```ets
AVQueueItem_Result OH_AVSession_AVMediaDescription_GetAlbumTitle(OH_AVSession_AVMediaDescription* description, char** albumTitle)
```

描述

获取媒体资源的专辑标题。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVSession_AVMediaDescription* description | 表示音视频媒体描述实例指针。 |
| char** albumTitle | 指针变量将返回当前媒体资源的专辑标题。 |

返回：

| 类型 | 说明 |
| --- | --- |
| AVQueueItem_Result | AVQUEUEITEM_SUCCESS：函数执行成功。  AVQUEUEITEM_ERROR_INVALID_PARAM：  1. 参数description为nullptr。  2. 参数albumTitle为nullptr。 |

**OH_AVSession_AVMediaDescription_GetAppName()**

```ets
AVQueueItem_Result OH_AVSession_AVMediaDescription_GetAppName(OH_AVSession_AVMediaDescription* description, char** appName)
```

描述

获取媒体资源的应用名。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVSession_AVMediaDescription* description | 表示音视频媒体描述实例指针。 |
| char** appName | 指针变量将返回媒体资源的应用名称。 |

返回：

| 类型 | 说明 |
| --- | --- |
| AVQueueItem_Result | AVQUEUEITEM_SUCCESS：函数执行成功。  AVQUEUEITEM_ERROR_INVALID_PARAM：  1. 参数description为nullptr。  2. 参数appName为nullptr。 |

**OH_AVSession_AVMediaDescriptionBuilder_GenerateAVMediaDescription()**

```ets
AVQueueItem_Result OH_AVSession_AVMediaDescriptionBuilder_GenerateAVMediaDescription(OH_AVSession_AVMediaDescriptionBuilder* builder, OH_AVSession_AVMediaDescription** avMediaDescription)
```

描述

创建avMediaDescription对象。当该对象不再使用时，调用[OH_AVSession_AVMediaDescription_Destroy](native_avqueueitem.h.md#ZH-CN_TOPIC_0000002553361813__oh_avsession_avmediadescription_destroy)释放avMediaDescription对象。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVSession_AVMediaDescriptionBuilder* builder | 表示音视频媒体描述构建器实例指针。 |
| OH_AVSession_AVMediaDescription** avMediaDescription | 指向用于接收avMediaDescription对象的指针变量。 |

返回：

| 类型 | 说明 |
| --- | --- |
| AVQueueItem_Result | AVQUEUEITEM_SUCCESS：函数执行成功。  AVQUEUEITEM_ERROR_NO_MEMORY：内存不足。  AVQUEUEITEM_ERROR_INVALID_PARAM：  1. 参数builder为nullptr。  2. 参数avMediaDescription为nullptr。 |

**OH_AVSession_AVMediaDescription_Destroy()**

```ets
AVQueueItem_Result OH_AVSession_AVMediaDescription_Destroy(OH_AVSession_AVMediaDescription* avMediaDescription)
```

描述

释放avMediaDescription对象。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVSession_AVMediaDescription* avMediaDescription | 指向用于接收avMediaDescription对象的指针变量。 |

返回：

| 类型 | 说明 |
| --- | --- |
| AVQueueItem_Result | AVQUEUEITEM_SUCCESS：函数执行成功。  AVQUEUEITEM_ERROR_INVALID_PARAM：参数avMediaDescription为nullptr。 |