# media_asset_manager_capi.h

**概述**

定义媒体资产管理器的接口。使用由媒体资产管理器提供的C API来请求媒体库资源。

库： libmedia_asset_manager.so

引用文件： <multimedia/media_library/media_asset_manager_capi.h>

系统能力： SystemCapability.FileManagement.PhotoAccessHelper.Core

起始版本： 12

相关模块： [MediaAssetManager](MediaAssetManager.md)

**汇总**

**函数**

| 名称 | 描述 |
| --- | --- |
| OH_MediaAssetManager* OH_MediaAssetManager_Create(void) | 创建一个媒体资产管理器。 |
| MediaLibrary_RequestId OH_MediaAssetManager_RequestImageForPath(OH_MediaAssetManager* manager, const char* uri, MediaLibrary_RequestOptions requestOptions, const char* destPath, OH_MediaLibrary_OnDataPrepared callback) | 请求具有目标路径的图像资源。 |
| MediaLibrary_RequestId OH_MediaAssetManager_RequestVideoForPath(OH_MediaAssetManager* manager, const char* uri, MediaLibrary_RequestOptions requestOptions, const char* destPath, OH_MediaLibrary_OnDataPrepared callback) | 请求具有目标路径的视频资源。 |
| bool OH_MediaAssetManager_CancelRequest(OH_MediaAssetManager* manager, const MediaLibrary_RequestId requestId) | 通过请求Id取消请求。 |
| MediaLibrary_ErrorCode OH_MediaAssetManager_RequestMovingPhoto(OH_MediaAssetManager* manager, OH_MediaAsset* mediaAsset, MediaLibrary_RequestOptions requestOptions, MediaLibrary_RequestId* requestId, OH_MediaLibrary_OnMovingPhotoDataPrepared callback) | 根据不同的策略模式请求动态照片资源。 |
| MediaLibrary_ErrorCode OH_MediaAssetManager_RequestImage(OH_MediaAssetManager* manager, OH_MediaAsset* mediaAsset, MediaLibrary_RequestOptions requestOptions, MediaLibrary_RequestId* requestId, OH_MediaLibrary_OnImageDataPrepared callback) | 根据不同的策略模式请求图像资源。 |
| MediaLibrary_ErrorCode OH_MediaAssetManager_Release(OH_MediaAssetManager* manager) | 释放OH_MediaAssetManager实例。 |
| MediaLibrary_ErrorCode OH_MediaAssetManager_QuickRequestImage(OH_MediaAssetManager* manager, OH_MediaAsset* mediaAsset, MediaLibrary_RequestOptions requestOptions, MediaLibrary_RequestId* requestId, OH_MediaLibrary_OnQuickImageDataPrepared callback) | 根据不同的策略模式请求图像资源。 |

**函数说明**

**OH_MediaAssetManager_Create()**

```ets
OH_MediaAssetManager* OH_MediaAssetManager_Create(void)
```

描述

创建一个媒体资产管理器。

起始版本： 12

返回：

| 类型 | 说明 |
| --- | --- |
| OH_MediaAssetManager* | 返回一个指向OH_MediaAssetManager实例的指针。 |

**OH_MediaAssetManager_RequestImageForPath()**

```ets
MediaLibrary_RequestId OH_MediaAssetManager_RequestImageForPath(OH_MediaAssetManager* manager, const char* uri,MediaLibrary_RequestOptions requestOptions, const char* destPath, OH_MediaLibrary_OnDataPrepared callback)
```

描述

请求具有目标路径的图像资源。

需要权限： ohos.permission.READ_IMAGEVIDEO

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_MediaAssetManager* manager | 指向OH_MediaAssetManager实例的指针。 |
| const char* uri | 请求的图像资源的uri。 |
| MediaLibrary_RequestOptions requestOptions | 请求策略模式配置项。 |
| const char* destPath | 请求资源的目标地址。 |
| OH_MediaLibrary_OnDataPrepared callback | 媒体资源处理器，当所请求的媒体资源准备完成时会触发回调。 |

返回：

| 类型 | 说明 |
| --- | --- |
| MediaLibrary_RequestId | 返回请求Id。 |

**OH_MediaAssetManager_RequestVideoForPath()**

```ets
MediaLibrary_RequestId OH_MediaAssetManager_RequestVideoForPath(OH_MediaAssetManager* manager, const char* uri,MediaLibrary_RequestOptions requestOptions, const char* destPath, OH_MediaLibrary_OnDataPrepared callback)
```

描述

请求具有目标路径的视频资源。

需要权限： ohos.permission.READ_IMAGEVIDEO

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_MediaAssetManager* manager | 指向OH_MediaAssetManager实例的指针。 |
| const char* uri | 请求的视频资源的uri。 |
| MediaLibrary_RequestOptions requestOptions | 请求策略模式配置项。 |
| const char* destPath | 请求资源的目标地址。 |
| OH_MediaLibrary_OnDataPrepared callback | 媒体资源处理器，当所请求的媒体资源准备完成时会触发回调。 |

返回：

| 类型 | 说明 |
| --- | --- |
| MediaLibrary_RequestId | 返回请求Id。 |

**OH_MediaAssetManager_CancelRequest()**

```ets
bool OH_MediaAssetManager_CancelRequest(OH_MediaAssetManager* manager, const MediaLibrary_RequestId requestId)
```

描述

通过请求Id取消请求。

需要权限： ohos.permission.READ_IMAGEVIDEO

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_MediaAssetManager* manager | 指向OH_MediaAssetManager实例的指针。 |
| const MediaLibrary_RequestId requestId | 待取消的请求Id。 |

返回：

| 类型 | 说明 |
| --- | --- |
| bool | 如果请求成功取消，则返回true；否则返回false。 |

**OH_MediaAssetManager_RequestMovingPhoto()**

```ets
MediaLibrary_ErrorCode OH_MediaAssetManager_RequestMovingPhoto(OH_MediaAssetManager* manager,OH_MediaAsset* mediaAsset, MediaLibrary_RequestOptions requestOptions, MediaLibrary_RequestId* requestId,OH_MediaLibrary_OnMovingPhotoDataPrepared callback)
```

描述

根据不同的策略模式请求动态照片资源。

需要权限： ohos.permission.READ_IMAGEVIDEO

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_MediaAssetManager* manager | OH_MediaAssetManager实例指针。 |
| OH_MediaAsset* mediaAsset | 要请求的媒体文件对象的OH_MediaAsset实例。 |
| MediaLibrary_RequestOptions requestOptions | 用于图像请求策略模式的MediaLibrary_RequestOptions。 |
| MediaLibrary_RequestId* requestId | 请求的MediaLibrary_RequestId，出参。 |
| OH_MediaLibrary_OnMovingPhotoDataPrepared callback | 当请求的动态照片准备就绪时调用OH_MediaLibrary_OnMovingPhotoDataPrepared。 |

返回：

| 类型 | 说明 |
| --- | --- |
| MediaLibrary_ErrorCode | MEDIA_LIBRARY_OK：方法调用成功。  MEDIA_LIBRARY_PARAMETER_ERROR：参数错误。可能的原因：  1. 未指定强制参数。  2. 参数类型不正确。  3. 参数验证失败。  MEDIA_LIBRARY_OPERATION_NOT_SUPPORTED：不支持该操作。  MEDIA_LIBRARY_PERMISSION_DENIED：没有权限。  MEDIA_LIBRARY_INTERNAL_SYSTEM_ERROR：内部系统错误。 |

**OH_MediaAssetManager_RequestImage()**

```ets
MediaLibrary_ErrorCode OH_MediaAssetManager_RequestImage(OH_MediaAssetManager* manager, OH_MediaAsset* mediaAsset,MediaLibrary_RequestOptions requestOptions, MediaLibrary_RequestId* requestId,OH_MediaLibrary_OnImageDataPrepared callback)
```

描述

根据不同的策略模式请求图像资源。

需要权限： ohos.permission.READ_IMAGEVIDEO

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_MediaAssetManager* manager | OH_MediaAssetManager实例指针。 |
| OH_MediaAsset* mediaAsset | 要请求的媒体文件对象的OH_MediaAsset实例。 |
| MediaLibrary_RequestOptions requestOptions | 用于图像请求策略模式的MediaLibrary_RequestOptions。 |
| MediaLibrary_RequestId* requestId | 请求的MediaLibrary_RequestId，出参。 |
| OH_MediaLibrary_OnImageDataPrepared callback | 当请求的图像源准备就绪时调用OH_MediaLibrary_OnImageDataPrepared。 |

返回：

| 类型 | 说明 |
| --- | --- |
| MediaLibrary_ErrorCode | MEDIA_LIBRARY_OK：方法调用成功。  MEDIA_LIBRARY_PARAMETER_ERROR：参数错误。可能的原因：  1. 未指定强制参数。  2. 参数类型不正确。  3. 参数验证失败。  MEDIA_LIBRARY_OPERATION_NOT_SUPPORTED：不支持该操作。  MEDIA_LIBRARY_PERMISSION_DENIED：没有权限。  MEDIA_LIBRARY_INTERNAL_SYSTEM_ERROR：内部系统错误。 |

**OH_MediaAssetManager_Release()**

```ets
MediaLibrary_ErrorCode OH_MediaAssetManager_Release(OH_MediaAssetManager* manager)
```

描述

释放[OH_MediaAssetManager](OH_MediaAssetManager.md)实例。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_MediaAssetManager* manager | 要释放的OH_MediaAssetManager实例。 |

返回：

| 类型 | 说明 |
| --- | --- |
| MediaLibrary_ErrorCode | MEDIA_LIBRARY_OK：方法调用成功。  MEDIA_LIBRARY_PARAMETER_ERROR：参数错误。可能的原因：  1. 未指定强制参数。  2. 参数类型不正确。  3. 参数验证失败。 |

**OH_MediaAssetManager_QuickRequestImage()**

```ets
MediaLibrary_ErrorCode OH_MediaAssetManager_QuickRequestImage(OH_MediaAssetManager* manager, OH_MediaAsset* mediaAsset, MediaLibrary_RequestOptions requestOptions, MediaLibrary_RequestId* requestId, OH_MediaLibrary_OnQuickImageDataPrepared callback)
```

描述

根据不同的策略模式请求图像资源。

需要权限： ohos.permission.READ_IMAGEVIDEO

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_MediaAssetManager* manager | OH_MediaAssetManager的实例指针。 |
| OH_MediaAsset* mediaAsset | 要请求的媒体文件对象的OH_MediaAsset实例。 |
| MediaLibrary_RequestOptions requestOptions | 用于图像请求策略模式的MediaLibrary_RequestOptions。 |
| MediaLibrary_RequestId* requestId | 请求的MediaLibrary_RequestId，该参数为输出参数。 |
| OH_MediaLibrary_OnQuickImageDataPrepared callback | 当请求的源数据准备就绪时，将会调用OH_MediaLibrary_OnQuickImageDataPrepared方法。 |

返回：

| 类型 | 说明 |
| --- | --- |
| MediaLibrary_ErrorCode | MEDIA_LIBRARY_OK：方法调用成功。  MEDIA_LIBRARY_OPERATION_NOT_SUPPORTED：不支持该操作。  MEDIA_LIBRARY_PERMISSION_DENIED：没有权限。  MEDIA_LIBRARY_INTERNAL_SYSTEM_ERROR：内部系统错误。 |