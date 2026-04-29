# moving_photo_capi.h

**概述**

定义与动态照片相关的API。提供获取动态照片信息的功能。

库： libmedia_asset_manager.so

引用文件： <multimedia/media_library/moving_photo_capi.h>

系统能力： SystemCapability.FileManagement.PhotoAccessHelper.Core

起始版本： 13

相关模块： [MediaAssetManager](MediaAssetManager.md)

**汇总**

**函数**

| 名称 | 描述 |
| --- | --- |
| MediaLibrary_ErrorCode OH_MovingPhoto_GetUri(OH_MovingPhoto* movingPhoto, const char** uri) | 获取动态照片的uri。 |
| MediaLibrary_ErrorCode OH_MovingPhoto_RequestContentWithUris(OH_MovingPhoto* movingPhoto, char* imageUri, char* videoUri) | 同时请求动态照片的图片内容和视频内容，并写入参数指定的对应的uri中。 |
| MediaLibrary_ErrorCode OH_MovingPhoto_RequestContentWithUri(OH_MovingPhoto* movingPhoto, MediaLibrary_ResourceType resourceType, char* uri) | 请求指定资源类型的动态照片内容，并写入参数指定的uri中。 |
| MediaLibrary_ErrorCode OH_MovingPhoto_RequestContentWithBuffer(OH_MovingPhoto* movingPhoto, MediaLibrary_ResourceType resourceType, const uint8_t** buffer, uint32_t* size) | 请求指定资源类型的动态照片内容，以ArrayBuffer的形式返回。 |
| MediaLibrary_ErrorCode OH_MovingPhoto_Release(OH_MovingPhoto* movingPhoto) | Release OH_MovingPhoto实例。 |

**函数说明**

**OH_MovingPhoto_GetUri()**

```ets
MediaLibrary_ErrorCode OH_MovingPhoto_GetUri(OH_MovingPhoto* movingPhoto, const char** uri)
```

描述

获取动态照片的uri。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_MovingPhoto* movingPhoto | OH_MovingPhoto实例。 |
| const char** uri | 动态照片的uri。 |

返回：

| 类型 | 说明 |
| --- | --- |
| MediaLibrary_ErrorCode | MEDIA_LIBRARY_OK：方法调用成功。  MEDIA_LIBRARY_PARAMETER_ERROR：参数错误。可能的原因：  1. 未指定强制参数。  2. 参数类型不正确。  3. 参数验证失败。  MEDIA_LIBRARY_INTERNAL_SYSTEM_ERROR：内部系统错误。 |

**OH_MovingPhoto_RequestContentWithUris()**

```ets
MediaLibrary_ErrorCode OH_MovingPhoto_RequestContentWithUris(OH_MovingPhoto* movingPhoto, char* imageUri,char* videoUri)
```

描述

同时请求动态照片的图片内容和视频内容，并写入参数指定的对应的uri中。

需要权限： ohos.permission.READ_IMAGEVIDEO

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_MovingPhoto* movingPhoto | OH_MovingPhoto实例。 |
| char* imageUri | 用于保存图像数据的目标文件uri。 |
| char* videoUri | 用于保存视频数据的目标文件uri。 |

返回：

| 类型 | 说明 |
| --- | --- |
| MediaLibrary_ErrorCode | MEDIA_LIBRARY_OK：方法调用成功。  MEDIA_LIBRARY_PARAMETER_ERROR：参数错误。可能的原因：  1. 未指定强制参数。  2. 参数类型不正确。  3. 参数验证失败。  MEDIA_LIBRARY_PERMISSION_DENIED：没有权限。  MEDIA_LIBRARY_INTERNAL_SYSTEM_ERROR：内部系统错误。 |

**OH_MovingPhoto_RequestContentWithUri()**

```ets
MediaLibrary_ErrorCode OH_MovingPhoto_RequestContentWithUri(OH_MovingPhoto* movingPhoto,MediaLibrary_ResourceType resourceType, char* uri)
```

描述

请求指定资源类型的动态照片内容，并写入参数指定的uri中。

需要权限： ohos.permission.READ_IMAGEVIDEO

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_MovingPhoto* movingPhoto | OH_MovingPhoto实例。 |
| MediaLibrary_ResourceType resourceType | 指定的资源类型MediaLibrary_ResourceType。 |
| char* uri | 保存数据的目标文件uri。 |

返回：

| 类型 | 说明 |
| --- | --- |
| MediaLibrary_ErrorCode | MEDIA_LIBRARY_OK：方法调用成功。  MEDIA_LIBRARY_PARAMETER_ERROR：参数错误。可能的原因：  1. 未指定强制参数。  2. 参数类型不正确。  3. 参数验证失败。  MEDIA_LIBRARY_PERMISSION_DENIED：没有权限。  MEDIA_LIBRARY_INTERNAL_SYSTEM_ERROR：内部系统错误。 |

**OH_MovingPhoto_RequestContentWithBuffer()**

```ets
MediaLibrary_ErrorCode OH_MovingPhoto_RequestContentWithBuffer(OH_MovingPhoto* movingPhoto,MediaLibrary_ResourceType resourceType, const uint8_t** buffer, uint32_t* size)
```

描述

请求指定资源类型的动态照片内容，以ArrayBuffer的形式返回。

需要权限： ohos.permission.READ_IMAGEVIDEO

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_MovingPhoto* movingPhoto | OH_MovingPhoto实例。 |
| MediaLibrary_ResourceType resourceType | 指定的资源类型MediaLibrary_ResourceType。 |
| const uint8_t** buffer | 保存目标文件数据的缓冲区。 |
| uint32_t* size | 缓冲区的大小。 |

返回：

| 类型 | 说明 |
| --- | --- |
| MediaLibrary_ErrorCode | MEDIA_LIBRARY_OK：方法调用成功。  MEDIA_LIBRARY_PARAMETER_ERROR：参数错误。可能的原因：  1. 未指定强制参数。  2. 参数类型不正确。  3. 参数验证失败。  MEDIA_LIBRARY_PERMISSION_DENIED：没有权限。  MEDIA_LIBRARY_INTERNAL_SYSTEM_ERROR：内部系统错误。 |

**OH_MovingPhoto_Release()**

```ets
MediaLibrary_ErrorCode OH_MovingPhoto_Release(OH_MovingPhoto* movingPhoto)
```

描述

Release [OH_MovingPhoto](OH_MovingPhoto.md)实例。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_MovingPhoto* movingPhoto | 要释放的OH_MovingPhoto实例。 |

返回：

| 类型 | 说明 |
| --- | --- |
| MediaLibrary_ErrorCode | MEDIA_LIBRARY_OK：方法调用成功。  MEDIA_LIBRARY_PARAMETER_ERROR：参数错误。可能的原因：  1. 未指定强制参数。  2. 参数类型不正确。  3. 参数验证失败。 |