# media_access_helper_capi.h

**概述**

定义与相册管理模块相关的API。

提供创建相册的功能，以及访问和修改相册中的媒体数据信息的功能。

库： libmedia_asset_manager.so

引用文件： <multimedia/media_library/media_access_helper_capi.h>

系统能力： SystemCapability.FileManagement.PhotoAccessHelper.Core

起始版本： 12

相关模块： [MediaAssetManager](MediaAssetManager.md)

**汇总**

**函数**

| 名称 | 描述 |
| --- | --- |
| MediaLibrary_ErrorCode OH_MediaAccessHelper_ApplyChanges(OH_MediaAssetChangeRequest* changeRequest) | 发起应用资产或相册的更改请求。 |

**函数说明**

**OH_MediaAccessHelper_ApplyChanges()**

```ets
MediaLibrary_ErrorCode OH_MediaAccessHelper_ApplyChanges(OH_MediaAssetChangeRequest* changeRequest)
```

描述

发起应用资产或相册的更改请求。

需要权限： ohos.permission.WRITE_IMAGEVIDEO

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_MediaAssetChangeRequest* changeRequest | 变更请求实例。 |

返回：

| 类型 | 说明 |
| --- | --- |
| MediaLibrary_ErrorCode | MEDIA_LIBRARY_OK：方法调用成功。  MEDIA_LIBRARY_PARAMETER_ERROR：参数错误。可能的原因：  1. 未指定强制参数。  2. 参数类型不正确。  3. 参数验证失败。  MEDIA_LIBRARY_PERMISSION_DENIED：没有权限。  MEDIA_LIBRARY_INTERNAL_SYSTEM_ERROR：内部系统错误。 |