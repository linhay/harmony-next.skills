# media_asset_base_capi.h

#### 概述

定义了媒体资产管理器的结构和枚举。

**库：** libmedia_asset_manager.so

**引用文件：** <multimedia/media_library/media_asset_base_capi.h>

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 12

**相关模块：**[MediaAssetManager](MediaAssetManager.md)

#### 汇总

#### 结构体

名称typedef关键字描述[MediaLibrary_RequestId](MediaLibrary_RequestId.md)MediaLibrary_RequestId

定义请求Id。

当请求媒体库资源时，会返回此类型。

请求Id可用于取消请求。

[OH_MediaAssetManager](OH_MediaAssetManager.md)OH_MediaAssetManager

定义媒体资产管理器。

此结构提供了请求媒体库资源的能力。

如果创建失败，则返回空指针。

[OH_MediaAssetChangeRequest](OH_MediaAssetChangeRequest.md)OH_MediaAssetChangeRequest

定义媒体资产更改请求。

此结构体提供了处理媒体资产更改请求的能力。

[OH_MovingPhoto](OH_MovingPhoto.md)OH_MovingPhoto

定义动态照片。

此结构体提供了获取关于动态照片的信息的能力。

[OH_MediaAsset](OH_MediaAsset.md)OH_MediaAsset

定义媒体资产。

此结构体提供了封装文件资源属性的能力。

[MediaLibrary_RequestOptions](MediaLibrary_RequestOptions.md)MediaLibrary_RequestOptions

请求策略模式配置项。

此结构体为媒体资源请求策略模式配置项。

#### 枚举

名称typedef关键字描述[MediaLibrary_ErrorCode](#ZH-CN_TOPIC_0000002497605962__medialibrary_errorcode)MediaLibrary_ErrorCode媒体库错误代码的枚举。[MediaLibrary_DeliveryMode](#ZH-CN_TOPIC_0000002497605962__medialibrary_deliverymode)MediaLibrary_DeliveryMode请求资源分发模式。[MediaLibrary_MediaType](#ZH-CN_TOPIC_0000002497605962__medialibrary_mediatype)MediaLibrary_MediaType媒体类型的枚举。[MediaLibrary_MediaSubType](#ZH-CN_TOPIC_0000002497605962__medialibrary_mediasubtype)MediaLibrary_MediaSubType媒体资源子类型的枚举。[MediaLibrary_ResourceType](#ZH-CN_TOPIC_0000002497605962__medialibrary_resourcetype)MediaLibrary_ResourceType资源类型的枚举。[MediaLibrary_ImageFileType](#ZH-CN_TOPIC_0000002497605962__medialibrary_imagefiletype)MediaLibrary_ImageFileType图像文件类型的枚举。[MediaLibrary_MediaQuality](#ZH-CN_TOPIC_0000002497605962__medialibrary_mediaquality)MediaLibrary_MediaQuality媒体资源质量枚举。此枚举与请求媒体资源时定义的分发模式有关。[MediaLibrary_MediaContentType](#ZH-CN_TOPIC_0000002497605962__medialibrary_mediacontenttype)MediaLibrary_MediaContentType媒体内容类型的枚举。

#### 函数

名称typedef关键字描述[typedef void (*OH_MediaLibrary_OnDataPrepared)(int32_t result, MediaLibrary_RequestId requestId)](#ZH-CN_TOPIC_0000002497605962__oh_medialibrary_ondataprepared)OH_MediaLibrary_OnDataPrepared当所请求的媒体资源准备完成时会触发回调。[typedef void (*OH_MediaLibrary_OnImageDataPrepared)(MediaLibrary_ErrorCode result, MediaLibrary_RequestId requestId, MediaLibrary_MediaQuality mediaQuality, MediaLibrary_MediaContentType type,OH_ImageSourceNative* imageSourceNative)](#ZH-CN_TOPIC_0000002497605962__oh_medialibrary_onimagedataprepared)OH_MediaLibrary_OnImageDataPrepared当请求的图像源准备就绪时会触发回调。[typedef void (*OH_MediaLibrary_OnMovingPhotoDataPrepared)(MediaLibrary_ErrorCode result, MediaLibrary_RequestId requestId, MediaLibrary_MediaQuality mediaQuality, MediaLibrary_MediaContentType type, OH_MovingPhoto* movingPhoto)](#ZH-CN_TOPIC_0000002497605962__oh_medialibrary_onmovingphotodataprepared)OH_MediaLibrary_OnMovingPhotoDataPrepared当请求的动态照片准备就绪时会触发回调。

#### 变量

名称描述static const int32_t UUID_STR_MAX_LENGTH = 37

定义UUID最大长度。这个常量定义了UUID字符串的最大长度。

**起始版本：** 12

#### 枚举类型说明

#### MediaLibrary_ErrorCode

```ets
enum MediaLibrary_ErrorCode
```

**描述**

媒体库错误代码的枚举。

**起始版本：** 12

枚举项描述MEDIA_LIBRARY_OK = 0媒体库结果正常。MEDIA_LIBRARY_PERMISSION_DENIED = 201权限被拒绝。MEDIA_LIBRARY_PARAMETER_ERROR = 401强制参数未指定，参数类型不正确或参数验证失败。MEDIA_LIBRARY_NO_SUCH_FILE = 23800101文件不存在。MEDIA_LIBRARY_INVALID_DISPLAY_NAME = 23800102显示名称无效。MEDIA_LIBRARY_INVALID_ASSET_URI = 23800103资产uri无效。MEDIA_LIBRARY_INVALID_PHOTO_KEY = 23800104PhotoKey无效。MEDIA_LIBRARY_OPERATION_NOT_SUPPORTED = 23800201不支持该操作。MEDIA_LIBRARY_INTERNAL_SYSTEM_ERROR = 23800301

内部系统错误。建议重试并检查日志。可能的原因：

1. 数据库已损坏。

2. 文件系统异常。

3. IPC请求超时。

#### MediaLibrary_DeliveryMode

```ets
enum MediaLibrary_DeliveryMode
```

**描述**

请求资源分发模式。

快速分发：不考虑资源质量，直接基于现有资源返回。

高质量分发：返回高质量资源，若没有，则触发生成高质量资源，成功后才返回。

均衡分发：若存在高质量资源，则直接返回高质量资源。否则，先返回低质量资源，并触发生成高质量资源，成功后再返回一次高质量资源。

**起始版本：** 12

枚举项描述MEDIA_LIBRARY_FAST_MODE = 0快速分发。MEDIA_LIBRARY_HIGH_QUALITY_MODE = 1高质量分发。MEDIA_LIBRARY_BALANCED_MODE = 2均衡分发。

#### MediaLibrary_MediaType

```ets
enum MediaLibrary_MediaType
```

**描述**

媒体类型的枚举。

**起始版本：** 12

枚举项描述MEDIA_LIBRARY_IMAGE = 1图像资产。MEDIA_LIBRARY_VIDEO = 2视频资产。

#### MediaLibrary_MediaSubType

```ets
enum MediaLibrary_MediaSubType
```

**描述**

媒体资源子类型的枚举。

**起始版本：** 12

枚举项描述MEDIA_LIBRARY_DEFAULT = 0默认照片类型。MEDIA_LIBRARY_MOVING_PHOTO = 3动态照片类型。MEDIA_LIBRARY_BURST = 4连拍照片类型。

#### MediaLibrary_ResourceType

```ets
enum MediaLibrary_ResourceType
```

**描述**

资源类型的枚举。

**起始版本：** 12

枚举项描述MEDIA_LIBRARY_IMAGE_RESOURCE = 1图像资源。MEDIA_LIBRARY_VIDEO_RESOURCE = 2视频资源。

#### MediaLibrary_ImageFileType

```ets
enum MediaLibrary_ImageFileType
```

**描述**

图像文件类型的枚举。

**起始版本：** 12

枚举项描述MEDIA_LIBRARY_IMAGE_JPEG = 1JPEG类型。MEDIA_LIBRARY_FILE_VIDEO = 3

MPEG类型。

**起始版本：** 19

#### MediaLibrary_MediaQuality

```ets
enum MediaLibrary_MediaQuality
```

**描述**

媒体资源质量枚举。

此枚举与请求媒体资源时定义的分发模式有关。

快速分发：不考虑资源质量，直接基于现有资源返回。

高质量分发：返回高质量资源，若没有，则触发生成高质量资源，成功后才返回。

均衡分发：若存在高质量资源，则直接返回高质量资源。否则，先返回低质量资源，并触发生成高质量资源，成功后再返回一次高质量资源。

**起始版本：** 12

枚举项描述MEDIA_LIBRARY_QUALITY_FAST = 1不考虑资源质量，直接返回的现有资源。MEDIA_LIBRARY_QUALITY_FULL = 2高质量资源。

#### MediaLibrary_MediaContentType

```ets
enum MediaLibrary_MediaContentType
```

**描述**

媒体内容类型的枚举。

**起始版本：** 12

枚举项描述MEDIA_LIBRARY_COMPRESSED = 1普通图片格式，如JPEG、HEIC、GIF。MEDIA_LIBRARY_PICTURE_OBJECT = 2图片解码后的PixelMap、GainMap和图片元数据信息一起封装的对象，方便应用进行编辑和显示。此对象的操作详见[OH_PictureNative](OH_PictureNative.md)。

#### 函数说明

#### OH_MediaLibrary_OnDataPrepared()

```ets
typedef void (*OH_MediaLibrary_OnDataPrepared)(int32_t result, MediaLibrary_RequestId requestId)
```

**描述**

当所请求的媒体资源准备完成时会触发回调。

**起始版本：** 12

**参数：**

参数项描述int32_t result请求资源处理的结果。MediaLibrary_RequestId requestId请求Id。

#### OH_MediaLibrary_OnImageDataPrepared()

```ets
typedef void (*OH_MediaLibrary_OnImageDataPrepared)(MediaLibrary_ErrorCode result,MediaLibrary_RequestId requestId, MediaLibrary_MediaQuality mediaQuality, MediaLibrary_MediaContentType type,OH_ImageSourceNative* imageSourceNative)
```

**描述**

当请求的图像源准备就绪时会触发回调。

**起始版本：** 12

**参数：**

参数项描述[MediaLibrary_ErrorCode](#ZH-CN_TOPIC_0000002497605962__medialibrary_errorcode) result处理所请求资源的结果[MediaLibrary_ErrorCode](#ZH-CN_TOPIC_0000002497605962__medialibrary_errorcode)。[MediaLibrary_RequestId](zh-cn_topic_0000002529285955.html) requestId请求的[MediaLibrary_RequestId](MediaLibrary_RequestId.md)。[MediaLibrary_MediaQuality](#ZH-CN_TOPIC_0000002497605962__medialibrary_mediaquality) mediaQuality请求源的[MediaLibrary_MediaQuality](#ZH-CN_TOPIC_0000002497605962__medialibrary_mediaquality)。[MediaLibrary_MediaContentType](zh-cn_topic_0000002497605962.html#ZH-CN_TOPIC_0000002497605962__medialibrary_mediacontenttype) type请求源的[MediaLibrary_MediaContentType](media_asset_base_capi.h.md#ZH-CN_TOPIC_0000002497605962__medialibrary_mediacontenttype)。[OH_ImageSourceNative](OH_ImageSourceNative.md)* imageSourceNative当请求的图像源准备就绪时获取[OH_ImageSourceNative](OH_ImageSourceNative.md)。

#### OH_MediaLibrary_OnMovingPhotoDataPrepared()

```ets
typedef void (*OH_MediaLibrary_OnMovingPhotoDataPrepared)(MediaLibrary_ErrorCode result,MediaLibrary_RequestId requestId, MediaLibrary_MediaQuality mediaQuality, MediaLibrary_MediaContentType type,OH_MovingPhoto* movingPhoto)
```

**描述**

当请求的动态照片准备就绪时会触发回调。

**起始版本：** 13

**参数：**

参数项描述[MediaLibrary_ErrorCode](#ZH-CN_TOPIC_0000002497605962__medialibrary_errorcode) result处理所请求资源的结果[MediaLibrary_ErrorCode](zh-cn_topic_0000002497605962.html#ZH-CN_TOPIC_0000002497605962__medialibrary_errorcode)。[MediaLibrary_RequestId](MediaLibrary_RequestId.md) requestId请求的[MediaLibrary_RequestId](MediaLibrary_RequestId.md)。[MediaLibrary_MediaQuality](#ZH-CN_TOPIC_0000002497605962__medialibrary_mediaquality) mediaQuality请求资源的[MediaLibrary_MediaQuality](#ZH-CN_TOPIC_0000002497605962__medialibrary_mediaquality)。[MediaLibrary_MediaContentType](zh-cn_topic_0000002497605962.html#ZH-CN_TOPIC_0000002497605962__medialibrary_mediacontenttype) type请求资源的[MediaLibrary_MediaContentType](media_asset_base_capi.h.md#ZH-CN_TOPIC_0000002497605962__medialibrary_mediacontenttype)。[OH_MovingPhoto](OH_MovingPhoto.md)* movingPhoto当请求的动态图片准备就绪时获取[OH_MovingPhoto](OH_MovingPhoto.md)。