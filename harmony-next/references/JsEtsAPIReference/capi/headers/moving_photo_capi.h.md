# moving_photo_capi.h

#### 概述

定义与动态照片相关的API。提供获取动态照片信息的功能。

**库：** libmedia_asset_manager.so

**引用文件：** <multimedia/media_library/moving_photo_capi.h>

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 13

**相关模块：**[MediaAssetManager](../../topics/media/MediaAssetManager.md)

#### 汇总

#### 函数

名称描述[MediaLibrary_ErrorCode OH_MovingPhoto_GetUri(OH_MovingPhoto* movingPhoto, const char** uri)](#ZH-CN_TOPIC_0000002497605964__oh_movingphoto_geturi)获取动态照片的uri。[MediaLibrary_ErrorCode OH_MovingPhoto_RequestContentWithUris(OH_MovingPhoto* movingPhoto, char* imageUri, char* videoUri)](#ZH-CN_TOPIC_0000002497605964__oh_movingphoto_requestcontentwithuris)同时请求动态照片的图片内容和视频内容，并写入参数指定的对应的uri中。[MediaLibrary_ErrorCode OH_MovingPhoto_RequestContentWithUri(OH_MovingPhoto* movingPhoto, MediaLibrary_ResourceType resourceType, char* uri)](#ZH-CN_TOPIC_0000002497605964__oh_movingphoto_requestcontentwithuri)请求指定资源类型的动态照片内容，并写入参数指定的uri中。[MediaLibrary_ErrorCode OH_MovingPhoto_RequestContentWithBuffer(OH_MovingPhoto* movingPhoto, MediaLibrary_ResourceType resourceType, const uint8_t** buffer, uint32_t* size)](#ZH-CN_TOPIC_0000002497605964__oh_movingphoto_requestcontentwithbuffer)请求指定资源类型的动态照片内容，以ArrayBuffer的形式返回。[MediaLibrary_ErrorCode OH_MovingPhoto_Release(OH_MovingPhoto* movingPhoto)](#ZH-CN_TOPIC_0000002497605964__oh_movingphoto_release)Release [OH_MovingPhoto](../../topics/misc/OH_MovingPhoto.md)实例。

#### 函数说明

#### OH_MovingPhoto_GetUri()

```ets
MediaLibrary_ErrorCode OH_MovingPhoto_GetUri(OH_MovingPhoto* movingPhoto, const char** uri)
```

**描述**

获取动态照片的uri。

**起始版本：** 13

**参数：**

参数项描述[OH_MovingPhoto](../../topics/misc/OH_MovingPhoto.md)* movingPhoto[OH_MovingPhoto](../../topics/misc/OH_MovingPhoto.md)实例。const char** uri动态照片的uri。

**返回：**

类型说明[MediaLibrary_ErrorCode](media_asset_base_capi.h.md#ZH-CN_TOPIC_0000002497605962__medialibrary_errorcode)

MEDIA_LIBRARY_OK：方法调用成功。

 MEDIA_LIBRARY_PARAMETER_ERROR：参数错误。可能的原因：

 1. 未指定强制参数。

 2. 参数类型不正确。

 3. 参数验证失败。

 MEDIA_LIBRARY_INTERNAL_SYSTEM_ERROR：内部系统错误。

#### OH_MovingPhoto_RequestContentWithUris()

```ets
MediaLibrary_ErrorCode OH_MovingPhoto_RequestContentWithUris(OH_MovingPhoto* movingPhoto, char* imageUri,char* videoUri)
```

**描述**

同时请求动态照片的图片内容和视频内容，并写入参数指定的对应的uri中。

**需要权限：** ohos.permission.READ_IMAGEVIDEO

**起始版本：** 13

**参数：**

参数项描述[OH_MovingPhoto](../../topics/misc/OH_MovingPhoto.md)* movingPhoto[OH_MovingPhoto](../../topics/misc/OH_MovingPhoto.md)实例。char* imageUri用于保存图像数据的目标文件uri。char* videoUri用于保存视频数据的目标文件uri。

**返回：**

类型说明[MediaLibrary_ErrorCode](media_asset_base_capi.h.md#ZH-CN_TOPIC_0000002497605962__medialibrary_errorcode)

MEDIA_LIBRARY_OK：方法调用成功。

 MEDIA_LIBRARY_PARAMETER_ERROR：参数错误。可能的原因：

 1. 未指定强制参数。

 2. 参数类型不正确。

 3. 参数验证失败。

 MEDIA_LIBRARY_PERMISSION_DENIED：没有权限。

 MEDIA_LIBRARY_INTERNAL_SYSTEM_ERROR：内部系统错误。

#### OH_MovingPhoto_RequestContentWithUri()

```ets
MediaLibrary_ErrorCode OH_MovingPhoto_RequestContentWithUri(OH_MovingPhoto* movingPhoto,MediaLibrary_ResourceType resourceType, char* uri)
```

**描述**

请求指定资源类型的动态照片内容，并写入参数指定的uri中。

**需要权限：** ohos.permission.READ_IMAGEVIDEO

**起始版本：** 13

**参数：**

参数项描述[OH_MovingPhoto](../../topics/misc/OH_MovingPhoto.md)* movingPhoto[OH_MovingPhoto](../../topics/misc/OH_MovingPhoto.md)实例。[MediaLibrary_ResourceType](media_asset_base_capi.h.md#ZH-CN_TOPIC_0000002497605962__medialibrary_resourcetype) resourceType指定的资源类型[MediaLibrary_ResourceType](media_asset_base_capi.h.md#ZH-CN_TOPIC_0000002497605962__medialibrary_resourcetype)。char* uri保存数据的目标文件uri。

**返回：**

类型说明[MediaLibrary_ErrorCode](media_asset_base_capi.h.md#ZH-CN_TOPIC_0000002497605962__medialibrary_errorcode)

MEDIA_LIBRARY_OK：方法调用成功。

 MEDIA_LIBRARY_PARAMETER_ERROR：参数错误。可能的原因：

 1. 未指定强制参数。

 2. 参数类型不正确。

 3. 参数验证失败。

 MEDIA_LIBRARY_PERMISSION_DENIED：没有权限。

 MEDIA_LIBRARY_INTERNAL_SYSTEM_ERROR：内部系统错误。

#### OH_MovingPhoto_RequestContentWithBuffer()

```ets
MediaLibrary_ErrorCode OH_MovingPhoto_RequestContentWithBuffer(OH_MovingPhoto* movingPhoto,MediaLibrary_ResourceType resourceType, const uint8_t** buffer, uint32_t* size)
```

**描述**

请求指定资源类型的动态照片内容，以ArrayBuffer的形式返回。

**需要权限：** ohos.permission.READ_IMAGEVIDEO

**起始版本：** 13

**参数：**

参数项描述[OH_MovingPhoto](../../topics/misc/OH_MovingPhoto.md)* movingPhoto[OH_MovingPhoto](../../topics/misc/OH_MovingPhoto.md)实例。[MediaLibrary_ResourceType](media_asset_base_capi.h.md#ZH-CN_TOPIC_0000002497605962__medialibrary_resourcetype) resourceType指定的资源类型[MediaLibrary_ResourceType](media_asset_base_capi.h.md#ZH-CN_TOPIC_0000002497605962__medialibrary_resourcetype)。const uint8_t** buffer保存目标文件数据的缓冲区。uint32_t* size缓冲区的大小。

**返回：**

类型说明[MediaLibrary_ErrorCode](media_asset_base_capi.h.md#ZH-CN_TOPIC_0000002497605962__medialibrary_errorcode)

MEDIA_LIBRARY_OK：方法调用成功。

 MEDIA_LIBRARY_PARAMETER_ERROR：参数错误。可能的原因：

 1. 未指定强制参数。

 2. 参数类型不正确。

 3. 参数验证失败。

 MEDIA_LIBRARY_PERMISSION_DENIED：没有权限。

 MEDIA_LIBRARY_INTERNAL_SYSTEM_ERROR：内部系统错误。

#### OH_MovingPhoto_Release()

```ets
MediaLibrary_ErrorCode OH_MovingPhoto_Release(OH_MovingPhoto* movingPhoto)
```

**描述**

Release [OH_MovingPhoto](../../topics/misc/OH_MovingPhoto.md)实例。

**起始版本：** 13

**参数：**

参数项描述[OH_MovingPhoto](../../topics/misc/OH_MovingPhoto.md)* movingPhoto要释放的[OH_MovingPhoto](../../topics/misc/OH_MovingPhoto.md)实例。

**返回：**

类型说明[MediaLibrary_ErrorCode](media_asset_base_capi.h.md#ZH-CN_TOPIC_0000002497605962__medialibrary_errorcode)

MEDIA_LIBRARY_OK：方法调用成功。

 MEDIA_LIBRARY_PARAMETER_ERROR：参数错误。可能的原因：

 1. 未指定强制参数。

 2. 参数类型不正确。

 3. 参数验证失败。