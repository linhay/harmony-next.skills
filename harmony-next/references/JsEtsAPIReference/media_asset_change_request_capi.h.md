# media_asset_change_request_capi.h

#### 概述

定义与媒体资产更改请求相关的API。提供更改资产的能力。

**库：** libmedia_asset_manager.so

**引用文件：** <multimedia/media_library/media_asset_change_request_capi.h>

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 12

**相关模块：**[MediaAssetManager](MediaAssetManager.md)

#### 汇总

#### 函数

名称描述[OH_MediaAssetChangeRequest* OH_MediaAssetChangeRequest_Create(OH_MediaAsset* mediaAsset)](#ZH-CN_TOPIC_0000002529285953__oh_mediaassetchangerequest_create)创建[OH_MediaAssetChangeRequest](zh-cn_topic_0000002497605966.html)实例。[MediaLibrary_ErrorCode OH_MediaAssetChangeRequest_AddResourceWithUri(OH_MediaAssetChangeRequest* changeRequest, MediaLibrary_ResourceType resourceType, char* fileUri)](#ZH-CN_TOPIC_0000002529285953__oh_mediaassetchangerequest_addresourcewithuri)通过文件uri添加资源。[MediaLibrary_ErrorCode OH_MediaAssetChangeRequest_AddResourceWithBuffer(OH_MediaAssetChangeRequest* changeRequest, MediaLibrary_ResourceType resourceType, uint8_t* buffer, uint32_t length)](#ZH-CN_TOPIC_0000002529285953__oh_mediaassetchangerequest_addresourcewithbuffer)通过ArrayBuffer数据添加资源。[MediaLibrary_ErrorCode OH_MediaAssetChangeRequest_GetWriteCacheHandler(OH_MediaAssetChangeRequest* changeRequest, int32_t* fd)](#ZH-CN_TOPIC_0000002529285953__oh_mediaassetchangerequest_getwritecachehandler)获取临时文件写句柄。[MediaLibrary_ErrorCode OH_MediaAssetChangeRequest_SaveCameraPhoto(OH_MediaAssetChangeRequest* changeRequest, MediaLibrary_ImageFileType imageFileType)](#ZH-CN_TOPIC_0000002529285953__oh_mediaassetchangerequest_savecameraphoto)保存相机拍摄的照片资源。[MediaLibrary_ErrorCode OH_MediaAssetChangeRequest_DiscardCameraPhoto(OH_MediaAssetChangeRequest* changeRequest)](#ZH-CN_TOPIC_0000002529285953__oh_mediaassetchangerequest_discardcameraphoto)丢弃相机拍摄的照片资源。[MediaLibrary_ErrorCode OH_MediaAssetChangeRequest_Release(OH_MediaAssetChangeRequest* changeRequest)](#ZH-CN_TOPIC_0000002529285953__oh_mediaassetchangerequest_release)释放[OH_MediaAssetChangeRequest](zh-cn_topic_0000002497605966.html)实例。

#### 函数说明

#### OH_MediaAssetChangeRequest_Create()

```ets
OH_MediaAssetChangeRequest* OH_MediaAssetChangeRequest_Create(OH_MediaAsset* mediaAsset)
```

**描述**

创建[OH_MediaAssetChangeRequest](OH_MediaAssetChangeRequest.md)实例。

**起始版本：** 12

**参数：**

参数项描述[OH_MediaAsset](OH_MediaAsset.md)* mediaAsset[OH_MediaAsset](OH_MediaAsset.md)实例。

**返回：**

类型说明[OH_MediaAssetChangeRequest](OH_MediaAssetChangeRequest.md)*

MEDIA_LIBRARY_OK：方法调用成功。

 MEDIA_LIBRARY_PARAMETER_ERROR：参数错误。可能的原因：

 1. 未指定强制参数。

 2. 参数类型不正确。

 3. 参数验证失败。

 MEDIA_LIBRARY_INTERNAL_SYSTEM_ERROR：内部系统错误。

#### OH_MediaAssetChangeRequest_AddResourceWithUri()

```ets
MediaLibrary_ErrorCode OH_MediaAssetChangeRequest_AddResourceWithUri(OH_MediaAssetChangeRequest* changeRequest,MediaLibrary_ResourceType resourceType, char* fileUri)
```

**描述**

通过文件uri添加资源。

**起始版本：** 13

**参数：**

参数项描述[OH_MediaAssetChangeRequest](OH_MediaAssetChangeRequest.md)* changeRequest[OH_MediaAssetChangeRequest](OH_MediaAssetChangeRequest.md)实例。[MediaLibrary_ResourceType](media_asset_base_capi.h.md#ZH-CN_TOPIC_0000002497605962__medialibrary_resourcetype) resourceType要添加的资源的[MediaLibrary_ResourceType](media_asset_base_capi.h.md#ZH-CN_TOPIC_0000002497605962__medialibrary_resourcetype)。char* fileUri文件uri。

**返回：**

类型说明[MediaLibrary_ErrorCode](media_asset_base_capi.h.md#ZH-CN_TOPIC_0000002497605962__medialibrary_errorcode)

MEDIA_LIBRARY_OK：方法调用成功。

 MEDIA_LIBRARY_PARAMETER_ERROR：参数错误。可能的原因：

 1. 未指定强制参数。

 2. 参数类型不正确。

 3. 参数验证失败。

 MEDIA_LIBRARY_NO_SUCH_FILE：文件不存在。

 MEDIA_LIBRARY_INTERNAL_SYSTEM_ERROR：内部系统错误。

 MEDIA_LIBRARY_OPERATION_NOT_SUPPORTED：不支持该操作。

#### OH_MediaAssetChangeRequest_AddResourceWithBuffer()

```ets
MediaLibrary_ErrorCode OH_MediaAssetChangeRequest_AddResourceWithBuffer(OH_MediaAssetChangeRequest* changeRequest,MediaLibrary_ResourceType resourceType, uint8_t* buffer, uint32_t length)
```

**描述**

通过ArrayBuffer数据添加资源。

**起始版本：** 12

**参数：**

参数项描述[OH_MediaAssetChangeRequest](OH_MediaAssetChangeRequest.md)* changeRequest[OH_MediaAssetChangeRequest](OH_MediaAssetChangeRequest.md)实例。[MediaLibrary_ResourceType](media_asset_base_capi.h.md#ZH-CN_TOPIC_0000002497605962__medialibrary_resourcetype) resourceType要添加的资源的类型。uint8_t* buffer要添加的数据缓冲区。uint32_t length数据缓冲区的长度。

**返回：**

类型说明[MediaLibrary_ErrorCode](media_asset_base_capi.h.md#ZH-CN_TOPIC_0000002497605962__medialibrary_errorcode)

MEDIA_LIBRARY_OK：方法调用成功。

 MEDIA_LIBRARY_PARAMETER_ERROR：参数错误。可能的原因：

 1. 未指定强制参数。

 2. 参数类型不正确。

 3. 参数验证失败。

 MEDIA_LIBRARY_INTERNAL_SYSTEM_ERROR：内部系统错误。

 MEDIA_LIBRARY_OPERATION_NOT_SUPPORTED：不支持该操作。

#### OH_MediaAssetChangeRequest_GetWriteCacheHandler()

```ets
MediaLibrary_ErrorCode OH_MediaAssetChangeRequest_GetWriteCacheHandler(OH_MediaAssetChangeRequest* changeRequest,int32_t* fd)
```

**描述**

获取临时文件写句柄。

**需要权限：** ohos.permission.WRITE_IMAGEVIDEO

**起始版本：** 13

**参数：**

参数项描述[OH_MediaAssetChangeRequest](OH_MediaAssetChangeRequest.md)* changeRequest[OH_MediaAssetChangeRequest](OH_MediaAssetChangeRequest.md)实例。int32_t* fd临时文件写句柄。

**返回：**

类型说明[MediaLibrary_ErrorCode](media_asset_base_capi.h.md#ZH-CN_TOPIC_0000002497605962__medialibrary_errorcode)

MEDIA_LIBRARY_OK：方法调用成功。

 MEDIA_LIBRARY_PARAMETER_ERROR：参数错误。可能的原因：

 1. 未指定强制参数。

 2. 参数类型不正确。

 3. 参数验证失败。

 MEDIA_LIBRARY_INTERNAL_SYSTEM_ERROR：内部系统错误。

 MEDIA_LIBRARY_PERMISSION_DENIED：没有权限。

 MEDIA_LIBRARY_OPERATION_NOT_SUPPORTED：不支持该操作。

#### OH_MediaAssetChangeRequest_SaveCameraPhoto()

```ets
MediaLibrary_ErrorCode OH_MediaAssetChangeRequest_SaveCameraPhoto(OH_MediaAssetChangeRequest* changeRequest,MediaLibrary_ImageFileType imageFileType)
```

**描述**

保存相机拍摄的照片资源。

**起始版本：** 12

**参数：**

参数项描述[OH_MediaAssetChangeRequest](OH_MediaAssetChangeRequest.md)* changeRequest[OH_MediaAssetChangeRequest](OH_MediaAssetChangeRequest.md)实例。[MediaLibrary_ImageFileType](media_asset_base_capi.h.md#ZH-CN_TOPIC_0000002497605962__medialibrary_imagefiletype) imageFileType要保存的照片的图像文件类型。

**返回：**

类型说明[MediaLibrary_ErrorCode](media_asset_base_capi.h.md#ZH-CN_TOPIC_0000002497605962__medialibrary_errorcode)

MEDIA_LIBRARY_OK：方法调用成功。

 MEDIA_LIBRARY_PARAMETER_ERROR：参数错误。可能的原因：

 1. 未指定强制参数。

 2. 参数类型不正确。

 3. 参数验证失败。

 MEDIA_LIBRARY_INTERNAL_SYSTEM_ERROR：内部系统错误。

 MEDIA_LIBRARY_OPERATION_NOT_SUPPORTED：不支持该操作。

#### OH_MediaAssetChangeRequest_DiscardCameraPhoto()

```ets
MediaLibrary_ErrorCode OH_MediaAssetChangeRequest_DiscardCameraPhoto(OH_MediaAssetChangeRequest* changeRequest)
```

**描述**

丢弃相机拍摄的照片资源。

**起始版本：** 12

**参数：**

参数项描述[OH_MediaAssetChangeRequest](OH_MediaAssetChangeRequest.md)* changeRequest[OH_MediaAssetChangeRequest](OH_MediaAssetChangeRequest.md)实例。

**返回：**

类型说明[MediaLibrary_ErrorCode](media_asset_base_capi.h.md#ZH-CN_TOPIC_0000002497605962__medialibrary_errorcode)

MEDIA_LIBRARY_OK：方法调用成功。

 MEDIA_LIBRARY_PARAMETER_ERROR：参数错误。可能的原因：

 1. 未指定强制参数。

 2. 参数类型不正确。

 3. 参数验证失败。

 MEDIA_LIBRARY_INTERNAL_SYSTEM_ERROR：内部系统错误。

 MEDIA_LIBRARY_OPERATION_NOT_SUPPORTED：不支持该操作。

#### OH_MediaAssetChangeRequest_Release()

```ets
MediaLibrary_ErrorCode OH_MediaAssetChangeRequest_Release(OH_MediaAssetChangeRequest* changeRequest)
```

**描述**

释放[OH_MediaAssetChangeRequest](OH_MediaAssetChangeRequest.md)实例。

**起始版本：** 12

**参数：**

参数项描述[OH_MediaAssetChangeRequest](OH_MediaAssetChangeRequest.md)* changeRequest[OH_MediaAssetChangeRequest](OH_MediaAssetChangeRequest.md)实例。

**返回：**

类型说明[MediaLibrary_ErrorCode](media_asset_base_capi.h.md#ZH-CN_TOPIC_0000002497605962__medialibrary_errorcode)

MEDIA_LIBRARY_OK：方法调用成功。

 MEDIA_LIBRARY_PARAMETER_ERROR：参数错误。可能的原因：

 1. 未指定强制参数。

 2. 参数类型不正确。

 3. 参数验证失败。