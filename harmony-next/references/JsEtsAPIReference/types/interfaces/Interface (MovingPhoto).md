# Interface (MovingPhoto)

动态照片对象。

- 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
- 本Interface首批接口从API version 12开始支持。

#### 导入模块

```ets
import { photoAccessHelper } from '@kit.MediaLibraryKit';
```

#### getUri12+

getUri(): string

获取动态照片的uri。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**返回值：**

类型说明string动态照片的uri。

**错误码：**

接口抛出错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[文件管理错误码](../../errors/文件管理错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.14000011System inner fail.

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](../../topics/misc/Functions.md#ZH-CN_TOPIC_0000002529445911__photoaccesshelpergetphotoaccesshelper)的示例使用。

```ets
import { dataSharePredicates } from '@kit.ArkData';

class MovingPhotoHandler implements photoAccessHelper.MediaAssetDataHandler<photoAccessHelper.MovingPhoto> {
  async onDataPrepared(movingPhoto: photoAccessHelper.MovingPhoto) {
    if (movingPhoto === undefined) {
      console.error('Error occurred when preparing data');
      return;
    }
    console.info("moving photo acquired successfully, uri: " + movingPhoto.getUri());
  }
}

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper, context: Context) {
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  predicates.equalTo(photoAccessHelper.PhotoKeys.PHOTO_SUBTYPE, photoAccessHelper.PhotoSubtype.MOVING_PHOTO);
  let fetchOptions: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  // 请确保图库内存在动态照片。
  let assetResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOptions);
  let asset: photoAccessHelper.PhotoAsset = await assetResult.getFirstObject();
  if (asset === undefined) {
    console.error('asset is undefined');
    return;
  }
  let requestOptions: photoAccessHelper.RequestOptions = {
    deliveryMode: photoAccessHelper.DeliveryMode.FAST_MODE,
  }
  const handler = new MovingPhotoHandler();
  try {
    let requestId: string = await photoAccessHelper.MediaAssetManager.requestMovingPhoto(context, asset, requestOptions, handler);
    console.info("moving photo requested successfully, requestId: " + requestId);
  } catch (err) {
    console.error(`failed to request moving photo, error code is ${err.code}, message is ${err.message}`);
  }
}
```

#### requestContent12+

requestContent(imageFileUri: string, videoFileUri: string): Promise<void>

同时请求动态照片的图片内容和视频内容，并写入参数指定的对应的uri中。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**需要权限**：ohos.permission.READ_IMAGEVIDEO

- 通过picker的方式调用该接口来请求动态照片对象并读取内容，不需要申请'ohos.permission.READ_IMAGEVIDEO'权限，详情请参考[开发指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/photoaccesshelper-movingphoto)。
- 对于本应用保存到媒体库的动态照片资源，应用无需额外申请'ohos.permission.READ_IMAGEVIDEO'权限即可访问。

**参数：**

参数名类型必填说明imageFileUristring是待写入动态照片图片内容的uri。示例imageFileUri为："file://com.example.temptest/data/storage/el2/base/haps/ImageFile.jpg"。videoFileUristring是待写入动态照片视频内容的uri。示例videoFileUri为："file://com.example.temptest/data/storage/el2/base/haps/VideoFile.mp4"。

**返回值：**

类型说明Promise<void>Promise对象，无返回结果。

**错误码：**

接口抛出错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[文件管理错误码](../../errors/文件管理错误码.md)。

错误码ID错误信息201Permission denied401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.14000011System inner fail.

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](../../topics/misc/Functions.md#ZH-CN_TOPIC_0000002529445911__photoaccesshelpergetphotoaccesshelper)的示例使用。

```ets
import { dataSharePredicates } from '@kit.ArkData';

class MovingPhotoHandler implements photoAccessHelper.MediaAssetDataHandler<photoAccessHelper.MovingPhoto> {
  async onDataPrepared(movingPhoto: photoAccessHelper.MovingPhoto) {
    if (movingPhoto === undefined) {
      console.error('Error occurred when preparing data');
      return;
    }
    // 应用需要确保待写入的uri是有效的。
    let imageFileUri: string = "file://com.example.temptest/data/storage/el2/base/haps/ImageFile.jpg";
    let videoFileUri: string = "file://com.example.temptest/data/storage/el2/base/haps/VideoFile.mp4";
    try {
      await movingPhoto.requestContent(imageFileUri, videoFileUri);
      console.info("moving photo contents retrieved successfully");
    } catch (err) {
      console.error(`failed to retrieve contents of moving photo, error code is ${err.code}, message is ${err.message}`);
    }
  }
}

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper, context: Context) {
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  predicates.equalTo(photoAccessHelper.PhotoKeys.PHOTO_SUBTYPE, photoAccessHelper.PhotoSubtype.MOVING_PHOTO);
  let fetchOptions: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  // 请确保图库内存在动态照片。
  let assetResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOptions);
  if (assetResult === undefined) {
    console.error('assetResult is undefined');
    return;
  }
  let asset: photoAccessHelper.PhotoAsset = await assetResult.getFirstObject();
  if (asset === undefined) {
    console.error('asset is undefined');
    return;
  }
  let requestOptions: photoAccessHelper.RequestOptions = {
    deliveryMode: photoAccessHelper.DeliveryMode.FAST_MODE,
  }
  const handler = new MovingPhotoHandler();
  try {
    let requestId: string = await photoAccessHelper.MediaAssetManager.requestMovingPhoto(context, asset, requestOptions, handler);
    console.info("moving photo requested successfully, requestId: " + requestId);
  } catch (err) {
    console.error(`failed to request moving photo, error code is ${err.code}, message is ${err.message}`);
  }
}
```

#### requestContent12+

requestContent(resourceType: ResourceType, fileUri: string): Promise<void>

请求指定资源类型的动态照片内容，并写入参数指定的uri中。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**需要权限**：ohos.permission.READ_IMAGEVIDEO

- 通过picker调用接口请求动态照片对象并读取内容，不需要申请'ohos.permission.READ_IMAGEVIDEO'权限，详情请参考[开发指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/photoaccesshelper-movingphoto)。
- 对于本应用保存到媒体库的动态照片资源，应用无需额外申请'ohos.permission.READ_IMAGEVIDEO'权限即可访问。

**参数：**

参数名类型必填说明resourceType[ResourceType](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529445919__resourcetype11)是所请求动态照片内容的资源类型。fileUristring是待写入动态照片内容的uri。

**返回值：**

类型说明Promise<void>Promise对象，无返回结果。

**错误码：**

接口抛出错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[文件管理错误码](../../errors/文件管理错误码.md)。

错误码ID错误信息201Permission denied401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.14000011System inner fail.

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](../../topics/misc/Functions.md#ZH-CN_TOPIC_0000002529445911__photoaccesshelpergetphotoaccesshelper)的示例使用。

```ets
import { dataSharePredicates } from '@kit.ArkData';

class MovingPhotoHandler implements photoAccessHelper.MediaAssetDataHandler<photoAccessHelper.MovingPhoto> {
  async onDataPrepared(movingPhoto: photoAccessHelper.MovingPhoto) {
    if (movingPhoto === undefined) {
      console.error('Error occurred when preparing data');
      return;
    }
    // 应用需要确保待写入的uri是有效的。
    let imageFileUri: string = "file://com.example.temptest/data/storage/el2/base/haps/ImageFile.jpg";
    try {
      await movingPhoto.requestContent(photoAccessHelper.ResourceType.IMAGE_RESOURCE, imageFileUri);
      console.info("moving photo image content retrieved successfully");
    } catch (err) {
      console.error(`failed to retrieve image content of moving photo, error code is ${err.code}, message is ${err.message}`);
    }
  }
}

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper, context: Context) {
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  predicates.equalTo(photoAccessHelper.PhotoKeys.PHOTO_SUBTYPE, photoAccessHelper.PhotoSubtype.MOVING_PHOTO);
  let fetchOptions: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  // 请确保图库内存在动态照片。
  let assetResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOptions);
  let asset: photoAccessHelper.PhotoAsset = await assetResult.getFirstObject();
  if (asset === undefined) {
    console.error('asset is undefined');
    return;
  }
  let requestOptions: photoAccessHelper.RequestOptions = {
    deliveryMode: photoAccessHelper.DeliveryMode.FAST_MODE,
  }
  const handler = new MovingPhotoHandler();
  try {
    let requestId: string = await photoAccessHelper.MediaAssetManager.requestMovingPhoto(context, asset, requestOptions, handler);
    console.info("moving photo requested successfully, requestId: " + requestId);
  } catch (err) {
    console.error(`failed to request moving photo, error code is ${err.code}, message is ${err.message}`);
  }
}
```

#### requestContent12+

requestContent(resourceType: ResourceType): Promise<ArrayBuffer>

请求指定资源类型的动态照片内容，以ArrayBuffer的形式返回。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**需要权限**：ohos.permission.READ_IMAGEVIDEO

- 使用picker调用该接口请求动态照片对象并读取内容时，不需要申请'ohos.permission.READ_IMAGEVIDEO'权限，详情请参考[开发指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/photoaccesshelper-movingphoto)。
- 对于本应用保存到媒体库的动态照片资源，应用无需额外申请'ohos.permission.READ_IMAGEVIDEO'权限即可访问。

**参数：**

参数名类型必填说明resourceType[ResourceType](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529445919__resourcetype11)是所请求动态照片内容的资源类型。

**返回值：**

类型说明Promise<ArrayBuffer>Promise对象，返回包含所请求文件内容的ArrayBuffer。

**错误码：**

接口抛出错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[文件管理错误码](../../errors/文件管理错误码.md)。

错误码ID错误信息201Permission denied401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.14000011System inner fail.

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](../../topics/misc/Functions.md#ZH-CN_TOPIC_0000002529445911__photoaccesshelpergetphotoaccesshelper)的示例使用。

```ets
import { dataSharePredicates } from '@kit.ArkData';

class MovingPhotoHandler implements photoAccessHelper.MediaAssetDataHandler<photoAccessHelper.MovingPhoto> {
  async onDataPrepared(movingPhoto: photoAccessHelper.MovingPhoto) {
    if (movingPhoto === undefined) {
      console.error('Error occurred when preparing data');
      return;
    }
    try {
      let buffer: ArrayBuffer = await movingPhoto.requestContent(photoAccessHelper.ResourceType.IMAGE_RESOURCE);
      console.info("moving photo image content retrieved successfully, buffer length: " + buffer.byteLength);
    } catch (err) {
      console.error(`failed to retrieve image content of moving photo, error code is ${err.code}, message is ${err.message}`);
    }
  }
}

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper, context: Context) {
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  predicates.equalTo(photoAccessHelper.PhotoKeys.PHOTO_SUBTYPE, photoAccessHelper.PhotoSubtype.MOVING_PHOTO);
  let fetchOptions: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  // 请确保图库内存在动态照片。
  let assetResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOptions);
  let asset: photoAccessHelper.PhotoAsset = await assetResult.getFirstObject();
  if (asset === undefined) {
    console.error('asset is undefined');
    return;
  }
  let requestOptions: photoAccessHelper.RequestOptions = {
    deliveryMode: photoAccessHelper.DeliveryMode.FAST_MODE,
  }
  const handler = new MovingPhotoHandler();
  try {
    let requestId: string = await photoAccessHelper.MediaAssetManager.requestMovingPhoto(context, asset, requestOptions, handler);
    console.info("moving photo requested successfully, requestId: " + requestId);
  } catch (err) {
    console.error(`failed to request moving photo, error code is ${err.code}, message is ${err.message}`);
  }
}
```