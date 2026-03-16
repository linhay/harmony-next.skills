# media_asset_capi.h

#### 概述

定义与媒体资源相关的API。提供获取图像或视频信息的能力。

**库：** libmedia_asset_manager.so

**引用文件：** <multimedia/media_library/media_asset_capi.h>

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 12

**相关模块：**[MediaAssetManager](../../topics/media/MediaAssetManager.md)

#### 汇总

#### 函数

名称描述[MediaLibrary_ErrorCode OH_MediaAsset_GetUri(OH_MediaAsset* mediaAsset, const char** uri)](#ZH-CN_TOPIC_0000002497445982__oh_mediaasset_geturi)获取媒体资产的uri。[MediaLibrary_ErrorCode OH_MediaAsset_GetMediaType(OH_MediaAsset* mediaAsset, MediaLibrary_MediaType* mediaType)](#ZH-CN_TOPIC_0000002497445982__oh_mediaasset_getmediatype)获取媒体资源类型。[MediaLibrary_ErrorCode OH_MediaAsset_GetMediaSubType(OH_MediaAsset* mediaAsset, MediaLibrary_MediaSubType* mediaSubType)](#ZH-CN_TOPIC_0000002497445982__oh_mediaasset_getmediasubtype)获取媒体资源子类型。[MediaLibrary_ErrorCode OH_MediaAsset_GetDisplayName(OH_MediaAsset* mediaAsset, const char** displayName)](#ZH-CN_TOPIC_0000002497445982__oh_mediaasset_getdisplayname)获取媒体资源的显示名称。[MediaLibrary_ErrorCode OH_MediaAsset_GetSize(OH_MediaAsset* mediaAsset, uint32_t* size)](#ZH-CN_TOPIC_0000002497445982__oh_mediaasset_getsize)获取媒体资产的文件大小。[MediaLibrary_ErrorCode OH_MediaAsset_GetDateAdded(OH_MediaAsset* mediaAsset, uint32_t* dateAdded)](#ZH-CN_TOPIC_0000002497445982__oh_mediaasset_getdateadded)获取资产添加日期。[MediaLibrary_ErrorCode OH_MediaAsset_GetDateModified(OH_MediaAsset* mediaAsset, uint32_t* dateModified)](#ZH-CN_TOPIC_0000002497445982__oh_mediaasset_getdatemodified)获取资产的修改日期。[MediaLibrary_ErrorCode OH_MediaAsset_GetDateTaken(OH_MediaAsset* mediaAsset, uint32_t* dateTaken)](#ZH-CN_TOPIC_0000002497445982__oh_mediaasset_getdatetaken)获取资产的拍摄日期。[MediaLibrary_ErrorCode OH_MediaAsset_GetDateAddedMs(OH_MediaAsset* mediaAsset, uint32_t* dateAddedMs)](#ZH-CN_TOPIC_0000002497445982__oh_mediaasset_getdateaddedms)获取资产的添加时间（毫秒）。[MediaLibrary_ErrorCode OH_MediaAsset_GetDateModifiedMs(OH_MediaAsset* mediaAsset, uint32_t* dateModifiedMs)](#ZH-CN_TOPIC_0000002497445982__oh_mediaasset_getdatemodifiedms)获取资产的修改时间（毫秒）。[MediaLibrary_ErrorCode OH_MediaAsset_GetDuration(OH_MediaAsset* mediaAsset, uint32_t* duration)](#ZH-CN_TOPIC_0000002497445982__oh_mediaasset_getduration)获取媒体资源的持续时间（毫秒）。[MediaLibrary_ErrorCode OH_MediaAsset_GetWidth(OH_MediaAsset* mediaAsset, uint32_t* width)](#ZH-CN_TOPIC_0000002497445982__oh_mediaasset_getwidth)获取媒体资源的图像宽度（像素）。[MediaLibrary_ErrorCode OH_MediaAsset_GetHeight(OH_MediaAsset* mediaAsset, uint32_t* height)](#ZH-CN_TOPIC_0000002497445982__oh_mediaasset_getheight)获取媒体资源的图像高度（像素）。[MediaLibrary_ErrorCode OH_MediaAsset_GetOrientation(OH_MediaAsset* mediaAsset, uint32_t* orientation)](#ZH-CN_TOPIC_0000002497445982__oh_mediaasset_getorientation)获取图像的旋转角度，单位为度。[MediaLibrary_ErrorCode OH_MediaAsset_IsFavorite(OH_MediaAsset* mediaAsset, uint32_t* favorite)](#ZH-CN_TOPIC_0000002497445982__oh_mediaasset_isfavorite)获取资产的收藏状态。[MediaLibrary_ErrorCode OH_MediaAsset_GetTitle(OH_MediaAsset* mediaAsset, const char** title)](#ZH-CN_TOPIC_0000002497445982__oh_mediaasset_gettitle)获取媒体资产的标题。[MediaLibrary_ErrorCode OH_MediaAsset_Release(OH_MediaAsset* mediaAsset)](#ZH-CN_TOPIC_0000002497445982__oh_mediaasset_release)释放媒体资产。

#### 函数说明

#### OH_MediaAsset_GetUri()

```ets
MediaLibrary_ErrorCode OH_MediaAsset_GetUri(OH_MediaAsset* mediaAsset, const char** uri)
```

**描述**

获取媒体资产的uri。

**起始版本：** 12

**参数：**

参数项描述[OH_MediaAsset](../../topics/media/OH_MediaAsset.md)* mediaAsset[OH_MediaAsset](../../topics/media/OH_MediaAsset.md)实例。const char** uri媒体资产的uri。

**返回：**

类型说明[MediaLibrary_ErrorCode](media_asset_base_capi.h.md#ZH-CN_TOPIC_0000002497605962__medialibrary_errorcode)

MEDIA_LIBRARY_OK：方法调用成功。

 MEDIA_LIBRARY_PARAMETER_ERROR：参数错误。可能的原因：

 1. 未指定强制参数。

 2. 参数类型不正确。

 3. 参数验证失败。

 MEDIA_LIBRARY_INTERNAL_SYSTEM_ERROR：内部系统错误。

#### OH_MediaAsset_GetMediaType()

```ets
MediaLibrary_ErrorCode OH_MediaAsset_GetMediaType(OH_MediaAsset* mediaAsset, MediaLibrary_MediaType* mediaType)
```

**描述**

获取媒体资源类型。

**起始版本：** 13

**参数：**

参数项描述[OH_MediaAsset](../../topics/media/OH_MediaAsset.md)* mediaAsset[OH_MediaAsset](../../topics/media/OH_MediaAsset.md)实例。[MediaLibrary_MediaType](media_asset_base_capi.h.md#ZH-CN_TOPIC_0000002497605962__medialibrary_mediatype)* mediaType媒体资源类型。

**返回：**

类型说明[MediaLibrary_ErrorCode](media_asset_base_capi.h.md#ZH-CN_TOPIC_0000002497605962__medialibrary_errorcode)

MEDIA_LIBRARY_OK：方法调用成功。

 MEDIA_LIBRARY_PARAMETER_ERROR：参数错误。可能的原因：

 1. 未指定强制参数。

 2. 参数类型不正确。

 3. 参数验证失败。

 MEDIA_LIBRARY_INTERNAL_SYSTEM_ERROR：内部系统错误。

#### OH_MediaAsset_GetMediaSubType()

```ets
MediaLibrary_ErrorCode OH_MediaAsset_GetMediaSubType(OH_MediaAsset* mediaAsset,MediaLibrary_MediaSubType* mediaSubType)
```

**描述**

获取媒体资源子类型。

**起始版本：** 13

**参数：**

参数项描述[OH_MediaAsset](../../topics/media/OH_MediaAsset.md)* mediaAsset[OH_MediaAsset](../../topics/media/OH_MediaAsset.md)实例。[MediaLibrary_MediaSubType](media_asset_base_capi.h.md#ZH-CN_TOPIC_0000002497605962__medialibrary_mediasubtype)* mediaSubType媒体资源子类型。

**返回：**

类型说明[MediaLibrary_ErrorCode](media_asset_base_capi.h.md#ZH-CN_TOPIC_0000002497605962__medialibrary_errorcode)

MEDIA_LIBRARY_OK：方法调用成功。

 MEDIA_LIBRARY_PARAMETER_ERROR：参数错误。可能的原因：

 1. 未指定强制参数。

 2. 参数类型不正确。

 3. 参数验证失败。

 MEDIA_LIBRARY_INTERNAL_SYSTEM_ERROR：内部系统错误。

#### OH_MediaAsset_GetDisplayName()

```ets
MediaLibrary_ErrorCode OH_MediaAsset_GetDisplayName(OH_MediaAsset* mediaAsset, const char** displayName)
```

**描述**

获取媒体资源的显示名称。

**起始版本：** 12

**参数：**

参数项描述[OH_MediaAsset](../../topics/media/OH_MediaAsset.md)* mediaAsset[OH_MediaAsset](../../topics/media/OH_MediaAsset.md)实例。const char** displayName媒体资源的显示名称。

**返回：**

类型说明[MediaLibrary_ErrorCode](media_asset_base_capi.h.md#ZH-CN_TOPIC_0000002497605962__medialibrary_errorcode)

MEDIA_LIBRARY_OK：方法调用成功。

 MEDIA_LIBRARY_PARAMETER_ERROR：参数错误。可能的原因：

 1. 未指定强制参数。

 2. 参数类型不正确。

 3. 参数验证失败。

 MEDIA_LIBRARY_INTERNAL_SYSTEM_ERROR：内部系统错误。

#### OH_MediaAsset_GetSize()

```ets
MediaLibrary_ErrorCode OH_MediaAsset_GetSize(OH_MediaAsset* mediaAsset, uint32_t* size)
```

**描述**

获取媒体资产的文件大小。

**起始版本：** 12

**参数：**

参数项描述[OH_MediaAsset](../../topics/media/OH_MediaAsset.md)* mediaAsset[OH_MediaAsset](../../topics/media/OH_MediaAsset.md)实例。uint32_t* size媒体资源的文件大小（以字节为单位）。

**返回：**

类型说明[MediaLibrary_ErrorCode](media_asset_base_capi.h.md#ZH-CN_TOPIC_0000002497605962__medialibrary_errorcode)

MEDIA_LIBRARY_OK：方法调用成功。

 MEDIA_LIBRARY_PARAMETER_ERROR：参数错误。可能的原因：

 1. 未指定强制参数。

 2. 参数类型不正确。

 3. 参数验证失败。

 MEDIA_LIBRARY_INTERNAL_SYSTEM_ERROR：内部系统错误。

#### OH_MediaAsset_GetDateAdded()

```ets
MediaLibrary_ErrorCode OH_MediaAsset_GetDateAdded(OH_MediaAsset* mediaAsset, uint32_t* dateAdded)
```

**描述**

获取资产添加日期。

**起始版本：** 13

**参数：**

参数项描述[OH_MediaAsset](../../topics/media/OH_MediaAsset.md)* mediaAsset[OH_MediaAsset](../../topics/media/OH_MediaAsset.md)实例。uint32_t* dateAdded资产添加日期。该值是添加文件时间距1970年1月1日的秒数值。

**返回：**

类型说明[MediaLibrary_ErrorCode](media_asset_base_capi.h.md#ZH-CN_TOPIC_0000002497605962__medialibrary_errorcode)

MEDIA_LIBRARY_OK：方法调用成功。

 MEDIA_LIBRARY_PARAMETER_ERROR：参数错误。可能的原因：

 1. 未指定强制参数。

 2. 参数类型不正确。

 3. 参数验证失败。

 MEDIA_LIBRARY_INTERNAL_SYSTEM_ERROR：内部系统错误。

#### OH_MediaAsset_GetDateModified()

```ets
MediaLibrary_ErrorCode OH_MediaAsset_GetDateModified(OH_MediaAsset* mediaAsset, uint32_t* dateModified)
```

**描述**

获取资产的修改日期。

**起始版本：** 13

**参数：**

参数项描述[OH_MediaAsset](../../topics/media/OH_MediaAsset.md)* mediaAsset[OH_MediaAsset](../../topics/media/OH_MediaAsset.md)实例。uint32_t* dateModified资产的修改日期。该值是修改文件时间距1970年1月1日的秒数值，修改文件名不会改变此值，当文件内容发生修改时才会更新。

**返回：**

类型说明[MediaLibrary_ErrorCode](media_asset_base_capi.h.md#ZH-CN_TOPIC_0000002497605962__medialibrary_errorcode)

MEDIA_LIBRARY_OK：方法调用成功。

 MEDIA_LIBRARY_PARAMETER_ERROR：参数错误。可能的原因：

 1. 未指定强制参数。

 2. 参数类型不正确。

 3. 参数验证失败。

 MEDIA_LIBRARY_INTERNAL_SYSTEM_ERROR：内部系统错误。

#### OH_MediaAsset_GetDateTaken()

```ets
MediaLibrary_ErrorCode OH_MediaAsset_GetDateTaken(OH_MediaAsset* mediaAsset, uint32_t* dateTaken)
```

**描述**

获取资产的拍摄日期。

**起始版本：** 13

**参数：**

参数项描述[OH_MediaAsset](../../topics/media/OH_MediaAsset.md)* mediaAsset[OH_MediaAsset](../../topics/media/OH_MediaAsset.md)实例。uint32_t* dateTaken资产的拍摄日期。该值是文件拍照时间距1970年1月1日的秒数值。

**返回：**

类型说明[MediaLibrary_ErrorCode](media_asset_base_capi.h.md#ZH-CN_TOPIC_0000002497605962__medialibrary_errorcode)

MEDIA_LIBRARY_OK：方法调用成功。

 MEDIA_LIBRARY_PARAMETER_ERROR：参数错误。可能的原因：

 1. 未指定强制参数。

 2. 参数类型不正确。

 3. 参数验证失败。

 MEDIA_LIBRARY_INTERNAL_SYSTEM_ERROR：内部系统错误。

#### OH_MediaAsset_GetDateAddedMs()

```ets
MediaLibrary_ErrorCode OH_MediaAsset_GetDateAddedMs(OH_MediaAsset* mediaAsset, uint32_t* dateAddedMs)
```

**描述**

获取资产的添加时间（毫秒）。

**起始版本：** 13

**参数：**

参数项描述[OH_MediaAsset](../../topics/media/OH_MediaAsset.md)* mediaAsset[OH_MediaAsset](../../topics/media/OH_MediaAsset.md)实例。uint32_t* dateAddedMs资产的添加时间（毫秒）。该值是添加文件时间距1970年1月1日的毫秒数值。

**返回：**

类型说明[MediaLibrary_ErrorCode](media_asset_base_capi.h.md#ZH-CN_TOPIC_0000002497605962__medialibrary_errorcode)

MEDIA_LIBRARY_OK：方法调用成功。

 MEDIA_LIBRARY_PARAMETER_ERROR：参数错误。可能的原因：

 1. 未指定强制参数。

 2. 参数类型不正确。

 3. 参数验证失败。

 MEDIA_LIBRARY_INTERNAL_SYSTEM_ERROR：内部系统错误。

#### OH_MediaAsset_GetDateModifiedMs()

```ets
MediaLibrary_ErrorCode OH_MediaAsset_GetDateModifiedMs(OH_MediaAsset* mediaAsset, uint32_t* dateModifiedMs)
```

**描述**

获取资产的修改时间（毫秒）。

**起始版本：** 12

**参数：**

参数项描述[OH_MediaAsset](../../topics/media/OH_MediaAsset.md)* mediaAsset[OH_MediaAsset](../../topics/media/OH_MediaAsset.md)实例。uint32_t* dateModifiedMs资产的修改时间（毫秒）。该值是修改文件时间距1970年1月1日的毫秒数值，修改文件名不会改变此值，当文件内容发生修改时才会更新。

**返回：**

类型说明[MediaLibrary_ErrorCode](media_asset_base_capi.h.md#ZH-CN_TOPIC_0000002497605962__medialibrary_errorcode)

MEDIA_LIBRARY_OK：方法调用成功。

 MEDIA_LIBRARY_PARAMETER_ERROR：参数错误。可能的原因：

 1. 未指定强制参数。

 2. 参数类型不正确。

 3. 参数验证失败。

 MEDIA_LIBRARY_INTERNAL_SYSTEM_ERROR：内部系统错误。

#### OH_MediaAsset_GetDuration()

```ets
MediaLibrary_ErrorCode OH_MediaAsset_GetDuration(OH_MediaAsset* mediaAsset, uint32_t* duration)
```

**描述**

获取媒体资源的持续时间（毫秒）。

**起始版本：** 13

**参数：**

参数项描述[OH_MediaAsset](../../topics/media/OH_MediaAsset.md)* mediaAsset[OH_MediaAsset](../../topics/media/OH_MediaAsset.md)实例。uint32_t* duration媒体资源的持续时间（毫秒）。

**返回：**

类型说明[MediaLibrary_ErrorCode](media_asset_base_capi.h.md#ZH-CN_TOPIC_0000002497605962__medialibrary_errorcode)

MEDIA_LIBRARY_OK：方法调用成功。

 MEDIA_LIBRARY_PARAMETER_ERROR：参数错误。可能的原因：

 1. 未指定强制参数。

 2. 参数类型不正确。

 3. 参数验证失败。

 MEDIA_LIBRARY_INTERNAL_SYSTEM_ERROR：内部系统错误。

#### OH_MediaAsset_GetWidth()

```ets
MediaLibrary_ErrorCode OH_MediaAsset_GetWidth(OH_MediaAsset* mediaAsset, uint32_t* width)
```

**描述**

获取媒体资源的图像宽度（像素）。

**起始版本：** 12

**参数：**

参数项描述[OH_MediaAsset](../../topics/media/OH_MediaAsset.md)* mediaAsset[OH_MediaAsset](../../topics/media/OH_MediaAsset.md)实例。uint32_t* width媒体资源的图像宽度（像素）。

**返回：**

类型说明[MediaLibrary_ErrorCode](media_asset_base_capi.h.md#ZH-CN_TOPIC_0000002497605962__medialibrary_errorcode)

MEDIA_LIBRARY_OK：方法调用成功。

 MEDIA_LIBRARY_PARAMETER_ERROR：参数错误。可能的原因：

 1. 未指定强制参数。

 2. 参数类型不正确。

 3. 参数验证失败。

 MEDIA_LIBRARY_INTERNAL_SYSTEM_ERROR：内部系统错误。

#### OH_MediaAsset_GetHeight()

```ets
MediaLibrary_ErrorCode OH_MediaAsset_GetHeight(OH_MediaAsset* mediaAsset, uint32_t* height)
```

**描述**

获取媒体资源的图像高度（像素）。

**起始版本：** 12

**参数：**

参数项描述[OH_MediaAsset](../../topics/media/OH_MediaAsset.md)* mediaAsset[OH_MediaAsset](../../topics/media/OH_MediaAsset.md)实例。uint32_t* height媒体资源的图像高度（像素）。

**返回：**

类型说明[MediaLibrary_ErrorCode](media_asset_base_capi.h.md#ZH-CN_TOPIC_0000002497605962__medialibrary_errorcode)

MEDIA_LIBRARY_OK：方法调用成功。

 MEDIA_LIBRARY_PARAMETER_ERROR：参数错误。可能的原因：

 1. 未指定强制参数。

 2. 参数类型不正确。

 3. 参数验证失败。

 MEDIA_LIBRARY_INTERNAL_SYSTEM_ERROR：内部系统错误。

#### OH_MediaAsset_GetOrientation()

```ets
MediaLibrary_ErrorCode OH_MediaAsset_GetOrientation(OH_MediaAsset* mediaAsset, uint32_t* orientation)
```

**描述**

获取图像的旋转角度，单位为度。

**起始版本：** 12

**参数：**

参数项描述[OH_MediaAsset](../../topics/media/OH_MediaAsset.md)* mediaAsset[OH_MediaAsset](../../topics/media/OH_MediaAsset.md)实例。uint32_t* orientation图像的旋转角度，单位为度。

**返回：**

类型说明[MediaLibrary_ErrorCode](media_asset_base_capi.h.md#ZH-CN_TOPIC_0000002497605962__medialibrary_errorcode)

MEDIA_LIBRARY_OK：方法调用成功。

 MEDIA_LIBRARY_PARAMETER_ERROR：参数错误。可能的原因：

 1. 未指定强制参数。

 2. 参数类型不正确。

 3. 参数验证失败。

 MEDIA_LIBRARY_INTERNAL_SYSTEM_ERROR：内部系统错误。

#### OH_MediaAsset_IsFavorite()

```ets
MediaLibrary_ErrorCode OH_MediaAsset_IsFavorite(OH_MediaAsset* mediaAsset, uint32_t* favorite)
```

**描述**

获取资产的收藏状态。

**起始版本：** 13

**参数：**

参数项描述[OH_MediaAsset](../../topics/media/OH_MediaAsset.md)* mediaAsset[OH_MediaAsset](../../topics/media/OH_MediaAsset.md)实例。uint32_t* favorite资产的收藏状态。

**返回：**

类型说明[MediaLibrary_ErrorCode](media_asset_base_capi.h.md#ZH-CN_TOPIC_0000002497605962__medialibrary_errorcode)

MEDIA_LIBRARY_OK：方法调用成功。

 MEDIA_LIBRARY_PARAMETER_ERROR：参数错误。可能的原因：

 1. 未指定强制参数。

 2. 参数类型不正确。

 3. 参数验证失败。

 MEDIA_LIBRARY_INTERNAL_SYSTEM_ERROR：内部系统错误。

#### OH_MediaAsset_GetTitle()

```ets
MediaLibrary_ErrorCode OH_MediaAsset_GetTitle(OH_MediaAsset* mediaAsset, const char** title)
```

**描述**

获取媒体资产的标题。

**起始版本：** 13

**参数：**

参数项描述[OH_MediaAsset](../../topics/media/OH_MediaAsset.md)* mediaAsset[OH_MediaAsset](../../topics/media/OH_MediaAsset.md)实例。const char** title媒体资产的标题。

**返回：**

类型说明[MediaLibrary_ErrorCode](media_asset_base_capi.h.md#ZH-CN_TOPIC_0000002497605962__medialibrary_errorcode)

MEDIA_LIBRARY_OK：方法调用成功。

 MEDIA_LIBRARY_PARAMETER_ERROR：参数错误。可能的原因：

 1. 未指定强制参数。

 2. 参数类型不正确。

 3. 参数验证失败。

 MEDIA_LIBRARY_INTERNAL_SYSTEM_ERROR：内部系统错误。

#### OH_MediaAsset_Release()

```ets
MediaLibrary_ErrorCode OH_MediaAsset_Release(OH_MediaAsset* mediaAsset)
```

**描述**

释放媒体资产。

**起始版本：** 12

**参数：**

参数项描述[OH_MediaAsset](../../topics/media/OH_MediaAsset.md)* mediaAsset[OH_MediaAsset](../../topics/media/OH_MediaAsset.md)实例。

**返回：**

类型说明[MediaLibrary_ErrorCode](media_asset_base_capi.h.md#ZH-CN_TOPIC_0000002497605962__medialibrary_errorcode)

MEDIA_LIBRARY_OK：方法调用成功。

 MEDIA_LIBRARY_PARAMETER_ERROR：参数错误。可能的原因：

 1. 未指定强制参数。

 2. 参数类型不正确。

 3. 参数验证失败。