# media_asset_base_capi.h

**概述**

定义了媒体资产管理器的结构和枚举。

库： libmedia_asset_manager.so

引用文件： <multimedia/media_library/media_asset_base_capi.h>

系统能力： SystemCapability.FileManagement.PhotoAccessHelper.Core

起始版本： 12

相关模块： [MediaAssetManager](MediaAssetManager.md)

**汇总**

**结构体**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| MediaLibrary_RequestId | MediaLibrary_RequestId | 定义请求Id。 当请求媒体库资源时，会返回此类型。 请求Id可用于取消请求。 |
| OH_MediaAssetManager | OH_MediaAssetManager | 定义媒体资产管理器。 此结构提供了请求媒体库资源的能力。 如果创建失败，则返回空指针。 |
| OH_MediaAssetChangeRequest | OH_MediaAssetChangeRequest | 定义媒体资产更改请求。 此结构体提供了处理媒体资产更改请求的能力。 |
| OH_MovingPhoto | OH_MovingPhoto | 定义动态照片。 此结构体提供了获取关于动态照片的信息的能力。 |
| OH_MediaAsset | OH_MediaAsset | 定义媒体资产。 此结构体提供了封装文件资源属性的能力。 |
| MediaLibrary_RequestOptions | MediaLibrary_RequestOptions | 请求策略模式配置项。 此结构体为媒体资源请求策略模式配置项。 |

**枚举**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| MediaLibrary_ErrorCode | MediaLibrary_ErrorCode | 媒体库错误代码的枚举。 |
| MediaLibrary_DeliveryMode | MediaLibrary_DeliveryMode | 请求资源分发模式。 |
| MediaLibrary_MediaType | MediaLibrary_MediaType | 媒体类型的枚举。 |
| MediaLibrary_MediaSubType | MediaLibrary_MediaSubType | 媒体资源子类型的枚举。 |
| MediaLibrary_ResourceType | MediaLibrary_ResourceType | 资源类型的枚举。 |
| MediaLibrary_ImageFileType | MediaLibrary_ImageFileType | 图像文件类型的枚举。 |
| MediaLibrary_MediaQuality | MediaLibrary_MediaQuality | 媒体资源质量枚举。此枚举与请求媒体资源时定义的分发模式有关。 |
| MediaLibrary_MediaContentType | MediaLibrary_MediaContentType | 媒体内容类型的枚举。 |

**函数**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| typedef void (*OH_MediaLibrary_OnDataPrepared)(int32_t result, MediaLibrary_RequestId requestId) | OH_MediaLibrary_OnDataPrepared | 当所请求的媒体资源准备完成时会触发回调。 |
| typedef void (*OH_MediaLibrary_OnImageDataPrepared)(MediaLibrary_ErrorCode result, MediaLibrary_RequestId requestId, MediaLibrary_MediaQuality mediaQuality, MediaLibrary_MediaContentType type,OH_ImageSourceNative* imageSourceNative) | OH_MediaLibrary_OnImageDataPrepared | 当请求的图像源准备就绪时会触发回调。 |
| typedef void (*OH_MediaLibrary_OnMovingPhotoDataPrepared)(MediaLibrary_ErrorCode result, MediaLibrary_RequestId requestId, MediaLibrary_MediaQuality mediaQuality, MediaLibrary_MediaContentType type, OH_MovingPhoto* movingPhoto) | OH_MediaLibrary_OnMovingPhotoDataPrepared | 当请求的动态照片准备就绪时会触发回调。 |

**变量**

| 名称 | 描述 |
| --- | --- |
| static const int32_t UUID_STR_MAX_LENGTH = 37 | 定义UUID最大长度。这个常量定义了UUID字符串的最大长度。 起始版本： 12 |

**枚举类型说明**

**MediaLibrary_ErrorCode**

```ets
enum MediaLibrary_ErrorCode
```

描述

媒体库错误代码的枚举。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| MEDIA_LIBRARY_OK = 0 | 媒体库结果正常。 |
| MEDIA_LIBRARY_PERMISSION_DENIED = 201 | 权限被拒绝。 |
| MEDIA_LIBRARY_PARAMETER_ERROR = 401 | 强制参数未指定，参数类型不正确或参数验证失败。 |
| MEDIA_LIBRARY_NO_SUCH_FILE = 23800101 | 文件不存在。 |
| MEDIA_LIBRARY_INVALID_DISPLAY_NAME = 23800102 | 显示名称无效。 |
| MEDIA_LIBRARY_INVALID_ASSET_URI = 23800103 | 资产uri无效。 |
| MEDIA_LIBRARY_INVALID_PHOTO_KEY = 23800104 | PhotoKey无效。 |
| MEDIA_LIBRARY_OPERATION_NOT_SUPPORTED = 23800201 | 不支持该操作。 |
| MEDIA_LIBRARY_INTERNAL_SYSTEM_ERROR = 23800301 | 内部系统错误。建议重试并检查日志。可能的原因： 1. 数据库已损坏。 2. 文件系统异常。 3. IPC请求超时。 |

**MediaLibrary_DeliveryMode**

```ets
enum MediaLibrary_DeliveryMode
```

描述

请求资源分发模式。

快速分发：不考虑资源质量，直接基于现有资源返回。

高质量分发：返回高质量资源，若没有，则触发生成高质量资源，成功后才返回。

均衡分发：若存在高质量资源，则直接返回高质量资源。否则，先返回低质量资源，并触发生成高质量资源，成功后再返回一次高质量资源。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| MEDIA_LIBRARY_FAST_MODE = 0 | 快速分发。 |
| MEDIA_LIBRARY_HIGH_QUALITY_MODE = 1 | 高质量分发。 |
| MEDIA_LIBRARY_BALANCED_MODE = 2 | 均衡分发。 |

**MediaLibrary_MediaType**

```ets
enum MediaLibrary_MediaType
```

描述

媒体类型的枚举。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| MEDIA_LIBRARY_IMAGE = 1 | 图像资产。 |
| MEDIA_LIBRARY_VIDEO = 2 | 视频资产。 |

**MediaLibrary_MediaSubType**

```ets
enum MediaLibrary_MediaSubType
```

描述

媒体资源子类型的枚举。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| MEDIA_LIBRARY_DEFAULT = 0 | 默认照片类型。 |
| MEDIA_LIBRARY_MOVING_PHOTO = 3 | 动态照片类型。 |
| MEDIA_LIBRARY_BURST = 4 | 连拍照片类型。 |

**MediaLibrary_ResourceType**

```ets
enum MediaLibrary_ResourceType
```

描述

资源类型的枚举。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| MEDIA_LIBRARY_IMAGE_RESOURCE = 1 | 图像资源。 |
| MEDIA_LIBRARY_VIDEO_RESOURCE = 2 | 视频资源。 |

**MediaLibrary_ImageFileType**

```ets
enum MediaLibrary_ImageFileType
```

描述

图像文件类型的枚举。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| MEDIA_LIBRARY_IMAGE_JPEG = 1 | JPEG类型。 |
| MEDIA_LIBRARY_IMAGE_HEIF = 2 | HEIF类型。 起始版本： 23 |
| MEDIA_LIBRARY_FILE_VIDEO = 3 | MPEG类型。 起始版本： 19 |

**MediaLibrary_MediaQuality**

```ets
enum MediaLibrary_MediaQuality
```

描述

媒体资源质量枚举。

此枚举与请求媒体资源时定义的分发模式有关。

快速分发：不考虑资源质量，直接基于现有资源返回。

高质量分发：返回高质量资源，若没有，则触发生成高质量资源，成功后才返回。

均衡分发：若存在高质量资源，则直接返回高质量资源。否则，先返回低质量资源，并触发生成高质量资源，成功后再返回一次高质量资源。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| MEDIA_LIBRARY_QUALITY_FAST = 1 | 不考虑资源质量，直接返回的现有资源。 |
| MEDIA_LIBRARY_QUALITY_FULL = 2 | 高质量资源。 |

**MediaLibrary_MediaContentType**

```ets
enum MediaLibrary_MediaContentType
```

描述

媒体内容类型的枚举。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| MEDIA_LIBRARY_COMPRESSED = 1 | 普通图片格式，如JPEG、HEIC、GIF。 |
| MEDIA_LIBRARY_PICTURE_OBJECT = 2 | 图片解码后的PixelMap、GainMap和图片元数据信息一起封装的对象，方便应用进行编辑和显示。此对象的操作详见OH_PictureNative。 |

**函数说明**

**OH_MediaLibrary_OnDataPrepared()**

```ets
typedef void (*OH_MediaLibrary_OnDataPrepared)(int32_t result, MediaLibrary_RequestId requestId)
```

描述

当所请求的媒体资源准备完成时会触发回调。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| int32_t result | 请求资源处理的结果。 |
| MediaLibrary_RequestId requestId | 请求Id。 |

**OH_MediaLibrary_OnImageDataPrepared()**

```ets
typedef void (*OH_MediaLibrary_OnImageDataPrepared)(MediaLibrary_ErrorCode result,MediaLibrary_RequestId requestId, MediaLibrary_MediaQuality mediaQuality, MediaLibrary_MediaContentType type,OH_ImageSourceNative* imageSourceNative)
```

描述

当请求的图像源准备就绪时会触发回调。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| MediaLibrary_ErrorCode result | 处理所请求资源的结果MediaLibrary_ErrorCode。 |
| MediaLibrary_RequestId requestId | 请求的MediaLibrary_RequestId。 |
| MediaLibrary_MediaQuality mediaQuality | 请求源的MediaLibrary_MediaQuality。 |
| MediaLibrary_MediaContentType type | 请求源的MediaLibrary_MediaContentType。 |
| OH_ImageSourceNative* imageSourceNative | 当请求的图像源准备就绪时获取OH_ImageSourceNative。 |

**OH_MediaLibrary_OnMovingPhotoDataPrepared()**

```ets
typedef void (*OH_MediaLibrary_OnMovingPhotoDataPrepared)(MediaLibrary_ErrorCode result,MediaLibrary_RequestId requestId, MediaLibrary_MediaQuality mediaQuality, MediaLibrary_MediaContentType type,OH_MovingPhoto* movingPhoto)
```

描述

当请求的动态照片准备就绪时会触发回调。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| MediaLibrary_ErrorCode result | 处理所请求资源的结果MediaLibrary_ErrorCode。 |
| MediaLibrary_RequestId requestId | 请求的MediaLibrary_RequestId。 |
| MediaLibrary_MediaQuality mediaQuality | 请求资源的MediaLibrary_MediaQuality。 |
| MediaLibrary_MediaContentType type | 请求资源的MediaLibrary_MediaContentType。 |
| OH_MovingPhoto* movingPhoto | 当请求的动态图片准备就绪时获取OH_MovingPhoto。 |

**OH_MediaLibrary_OnQuickImageDataPrepared()**

```ets
typedef void (*OH_MediaLibrary_OnQuickImageDataPrepared)(MediaLibrary_ErrorCode result, MediaLibrary_RequestId requestId, MediaLibrary_MediaQuality mediaQuality, MediaLibrary_MediaContentType type, OH_ImageSourceNative* imageSourceNative, OH_PictureNative* pictureNative)
```

描述

当请求的图像源准备就绪时调用此函数。如果系统中存在图像缓冲区，则会返回一个图片对象，从而减少编码时间。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| MediaLibrary_ErrorCode result | 处理所请求资源的结果。 |
| MediaLibrary_RequestId requestId | 请求资源的MediaLibrary_RequestId。 |
| MediaLibrary_MediaQuality mediaQuality | 请求资源的MediaLibrary_MediaQuality。 |
| MediaLibrary_MediaContentType type | 请求来源的MediaLibrary_MediaContentType。 |
| OH_ImageSourceNative* imageSourceNative | 用于在准备图像文件时获取OH_ImageSourceNative信息，否则imageSourceNative为null。 |
| OH_PictureNative* pictureNative | 用于在准备图像源时获取OH_PictureNative信息，否则pictureNative为null。 |