# media_asset_manager_capi.h

#### 概述

定义媒体资产管理器的接口。使用由媒体资产管理器提供的C API来请求媒体库资源。

**库：** libmedia_asset_manager.so

**引用文件：** <multimedia/media_library/media_asset_manager_capi.h>

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 12

**相关模块：**[MediaAssetManager](MediaAssetManager.md)

#### 汇总

#### 函数

名称描述[OH_MediaAssetManager* OH_MediaAssetManager_Create(void)](#ZH-CN_TOPIC_0000002529445927__oh_mediaassetmanager_create)创建一个媒体资产管理器。[MediaLibrary_RequestId OH_MediaAssetManager_RequestImageForPath(OH_MediaAssetManager* manager, const char* uri, MediaLibrary_RequestOptions requestOptions, const char* destPath, OH_MediaLibrary_OnDataPrepared callback)](#ZH-CN_TOPIC_0000002529445927__oh_mediaassetmanager_requestimageforpath)请求具有目标路径的图像资源。[MediaLibrary_RequestId OH_MediaAssetManager_RequestVideoForPath(OH_MediaAssetManager* manager, const char* uri, MediaLibrary_RequestOptions requestOptions, const char* destPath, OH_MediaLibrary_OnDataPrepared callback)](#ZH-CN_TOPIC_0000002529445927__oh_mediaassetmanager_requestvideoforpath)请求具有目标路径的视频资源。[bool OH_MediaAssetManager_CancelRequest(OH_MediaAssetManager* manager, const MediaLibrary_RequestId requestId)](#ZH-CN_TOPIC_0000002529445927__oh_mediaassetmanager_cancelrequest)通过请求Id取消请求。[MediaLibrary_ErrorCode OH_MediaAssetManager_RequestMovingPhoto(OH_MediaAssetManager* manager, OH_MediaAsset* mediaAsset, MediaLibrary_RequestOptions requestOptions, MediaLibrary_RequestId* requestId, OH_MediaLibrary_OnMovingPhotoDataPrepared callback)](#ZH-CN_TOPIC_0000002529445927__oh_mediaassetmanager_requestmovingphoto)根据不同的策略模式请求动态照片资源。[MediaLibrary_ErrorCode OH_MediaAssetManager_RequestImage(OH_MediaAssetManager* manager, OH_MediaAsset* mediaAsset, MediaLibrary_RequestOptions requestOptions, MediaLibrary_RequestId* requestId, OH_MediaLibrary_OnImageDataPrepared callback)](#ZH-CN_TOPIC_0000002529445927__oh_mediaassetmanager_requestimage)根据不同的策略模式请求图像资源。[MediaLibrary_ErrorCode OH_MediaAssetManager_Release(OH_MediaAssetManager* manager)](#ZH-CN_TOPIC_0000002529445927__oh_mediaassetmanager_release)释放[OH_MediaAssetManager](zh-cn_topic_0000002529445929.html)实例。

#### 函数说明

#### OH_MediaAssetManager_Create()

```ets
OH_MediaAssetManager* OH_MediaAssetManager_Create(void)
```

**描述**

创建一个媒体资产管理器。

**起始版本：** 12

**返回：**

类型说明[OH_MediaAssetManager](OH_MediaAssetManager.md)*返回一个指向OH_MediaAssetManager实例的指针。

#### OH_MediaAssetManager_RequestImageForPath()

```ets
MediaLibrary_RequestId OH_MediaAssetManager_RequestImageForPath(OH_MediaAssetManager* manager, const char* uri,MediaLibrary_RequestOptions requestOptions, const char* destPath, OH_MediaLibrary_OnDataPrepared callback)
```

**描述**

请求具有目标路径的图像资源。

**需要权限：** ohos.permission.READ_IMAGEVIDEO

**起始版本：** 12

**参数：**

参数项描述[OH_MediaAssetManager](OH_MediaAssetManager.md)* manager指向OH_MediaAssetManager实例的指针。const char* uri请求的图像资源的uri。[MediaLibrary_RequestOptions](MediaLibrary_RequestOptions.md) requestOptions请求策略模式配置项。const char* destPath请求资源的目标地址。[OH_MediaLibrary_OnDataPrepared](media_asset_base_capi.h.md#ZH-CN_TOPIC_0000002497605962__oh_medialibrary_ondataprepared) callback媒体资源处理器，当所请求的媒体资源准备完成时会触发回调。

**返回：**

类型说明[MediaLibrary_RequestId](MediaLibrary_RequestId.md)返回请求Id。

#### OH_MediaAssetManager_RequestVideoForPath()

```ets
MediaLibrary_RequestId OH_MediaAssetManager_RequestVideoForPath(OH_MediaAssetManager* manager, const char* uri,MediaLibrary_RequestOptions requestOptions, const char* destPath, OH_MediaLibrary_OnDataPrepared callback)
```

**描述**

请求具有目标路径的视频资源。

**需要权限：** ohos.permission.READ_IMAGEVIDEO

**起始版本：** 12

**参数：**

参数项描述[OH_MediaAssetManager](OH_MediaAssetManager.md)* manager指向OH_MediaAssetManager实例的指针。const char* uri请求的视频资源的uri。[MediaLibrary_RequestOptions](MediaLibrary_RequestOptions.md) requestOptions请求策略模式配置项。const char* destPath请求资源的目标地址。[OH_MediaLibrary_OnDataPrepared](media_asset_base_capi.h.md#ZH-CN_TOPIC_0000002497605962__oh_medialibrary_ondataprepared) callback媒体资源处理器，当所请求的媒体资源准备完成时会触发回调。

**返回：**

类型说明[MediaLibrary_RequestId](MediaLibrary_RequestId.md)返回请求Id。

#### OH_MediaAssetManager_CancelRequest()

```ets
bool OH_MediaAssetManager_CancelRequest(OH_MediaAssetManager* manager, const MediaLibrary_RequestId requestId)
```

**描述**

通过请求Id取消请求。

**需要权限：** ohos.permission.READ_IMAGEVIDEO

**起始版本：** 12

**参数：**

参数项描述[OH_MediaAssetManager](OH_MediaAssetManager.md)* manager指向OH_MediaAssetManager实例的指针。const [MediaLibrary_RequestId](MediaLibrary_RequestId.md) requestId待取消的请求Id。

**返回：**

类型说明bool如果请求成功取消，则返回true；否则返回false。

#### OH_MediaAssetManager_RequestMovingPhoto()

```ets
MediaLibrary_ErrorCode OH_MediaAssetManager_RequestMovingPhoto(OH_MediaAssetManager* manager,OH_MediaAsset* mediaAsset, MediaLibrary_RequestOptions requestOptions, MediaLibrary_RequestId* requestId,OH_MediaLibrary_OnMovingPhotoDataPrepared callback)
```

**描述**

根据不同的策略模式请求动态照片资源。

**需要权限：** ohos.permission.READ_IMAGEVIDEO

**起始版本：** 13

**参数：**

参数项描述[OH_MediaAssetManager](OH_MediaAssetManager.md)* manager[OH_MediaAssetManager](OH_MediaAssetManager.md)实例指针。[OH_MediaAsset](OH_MediaAsset.md)* mediaAsset要请求的媒体文件对象的[OH_MediaAsset](OH_MediaAsset.md)实例。[MediaLibrary_RequestOptions](MediaLibrary_RequestOptions.md) requestOptions用于图像请求策略模式的[MediaLibrary_RequestOptions](MediaLibrary_RequestOptions.md)。[MediaLibrary_RequestId](MediaLibrary_RequestId.md)* requestId请求的[MediaLibrary_RequestId](MediaLibrary_RequestId.md)，出参。[OH_MediaLibrary_OnMovingPhotoDataPrepared](media_asset_base_capi.h.md#ZH-CN_TOPIC_0000002497605962__oh_medialibrary_onmovingphotodataprepared) callback当请求的动态照片准备就绪时调用[OH_MediaLibrary_OnMovingPhotoDataPrepared](media_asset_base_capi.h.md#ZH-CN_TOPIC_0000002497605962__oh_medialibrary_onmovingphotodataprepared)。

**返回：**

类型说明[MediaLibrary_ErrorCode](media_asset_base_capi.h.md#ZH-CN_TOPIC_0000002497605962__medialibrary_errorcode)

MEDIA_LIBRARY_OK：方法调用成功。

 MEDIA_LIBRARY_PARAMETER_ERROR：参数错误。可能的原因：

 1. 未指定强制参数。

 2. 参数类型不正确。

 3. 参数验证失败。

 MEDIA_LIBRARY_OPERATION_NOT_SUPPORTED：不支持该操作。

 MEDIA_LIBRARY_PERMISSION_DENIED：没有权限。

 MEDIA_LIBRARY_INTERNAL_SYSTEM_ERROR：内部系统错误。

#### OH_MediaAssetManager_RequestImage()

```ets
MediaLibrary_ErrorCode OH_MediaAssetManager_RequestImage(OH_MediaAssetManager* manager, OH_MediaAsset* mediaAsset,MediaLibrary_RequestOptions requestOptions, MediaLibrary_RequestId* requestId,OH_MediaLibrary_OnImageDataPrepared callback)
```

**描述**

根据不同的策略模式请求图像资源。

**需要权限：** ohos.permission.READ_IMAGEVIDEO

**起始版本：** 12

**参数：**

参数项描述[OH_MediaAssetManager](OH_MediaAssetManager.md)* manager[OH_MediaAssetManager](OH_MediaAssetManager.md)实例指针。[OH_MediaAsset](OH_MediaAsset.md)* mediaAsset要请求的媒体文件对象的[OH_MediaAsset](OH_MediaAsset.md)实例。[MediaLibrary_RequestOptions](MediaLibrary_RequestOptions.md) requestOptions用于图像请求策略模式的[MediaLibrary_RequestOptions](MediaLibrary_RequestOptions.md)。[MediaLibrary_RequestId](MediaLibrary_RequestId.md)* requestId请求的[MediaLibrary_RequestId](MediaLibrary_RequestId.md)，出参。[OH_MediaLibrary_OnImageDataPrepared](media_asset_base_capi.h.md#ZH-CN_TOPIC_0000002497605962__oh_medialibrary_onimagedataprepared) callback当请求的图像源准备就绪时调用[OH_MediaLibrary_OnImageDataPrepared](media_asset_base_capi.h.md#ZH-CN_TOPIC_0000002497605962__oh_medialibrary_onimagedataprepared)。

**返回：**

类型说明[MediaLibrary_ErrorCode](media_asset_base_capi.h.md#ZH-CN_TOPIC_0000002497605962__medialibrary_errorcode)

MEDIA_LIBRARY_OK：方法调用成功。

 MEDIA_LIBRARY_PARAMETER_ERROR：参数错误。可能的原因：

 1. 未指定强制参数。

 2. 参数类型不正确。

 3. 参数验证失败。

 MEDIA_LIBRARY_OPERATION_NOT_SUPPORTED：不支持该操作。

 MEDIA_LIBRARY_PERMISSION_DENIED：没有权限。

 MEDIA_LIBRARY_INTERNAL_SYSTEM_ERROR：内部系统错误。

#### OH_MediaAssetManager_Release()

```ets
MediaLibrary_ErrorCode OH_MediaAssetManager_Release(OH_MediaAssetManager* manager)
```

**描述**

释放[OH_MediaAssetManager](OH_MediaAssetManager.md)实例。

**起始版本：** 13

**参数：**

参数项描述[OH_MediaAssetManager](OH_MediaAssetManager.md)* manager要释放的[OH_MediaAssetManager](OH_MediaAssetManager.md)实例。

**返回：**

类型说明[MediaLibrary_ErrorCode](media_asset_base_capi.h.md#ZH-CN_TOPIC_0000002497605962__medialibrary_errorcode)

MEDIA_LIBRARY_OK：方法调用成功。

 MEDIA_LIBRARY_PARAMETER_ERROR：参数错误。可能的原因：

 1. 未指定强制参数。

 2. 参数类型不正确。

 3. 参数验证失败。