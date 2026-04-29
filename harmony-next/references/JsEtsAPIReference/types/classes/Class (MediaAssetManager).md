# Class (MediaAssetManager)

媒体资产管理类，管理媒体资源读取。

- 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
- 本Class首批接口从API version 11开始支持。

#### 导入模块

```ets
import { photoAccessHelper } from '@kit.MediaLibraryKit';
```

#### requestImage11+

static requestImage(context: Context, asset: PhotoAsset, requestOptions: RequestOptions, dataHandler: MediaAssetDataHandler<image.ImageSource>): Promise<string>

根据不同的策略模式，请求图片资源。使用Promise异步回调。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**需要权限**：ohos.permission.READ_IMAGEVIDEO

- 通过picker的方式调用该接口来请求图片资源，不需要申请'ohos.permission.READ_IMAGEVIDEO'权限，详情请参考[指定URI获取图片或视频资源](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/photoaccesshelper-photoviewpicker#指定uri获取图片或视频资源)。

- 对于本应用保存到媒体库的图片资源，应用无需额外申请'ohos.permission.READ_IMAGEVIDEO'权限即可访问。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 传入Ability实例的上下文。 |
| asset | PhotoAsset | 是 | 待请求的媒体文件对象。 |
| requestOptions | RequestOptions | 是 | 图片请求策略模式配置项。 |
| dataHandler | MediaAssetDataHandler<image.ImageSource> | 是 | 媒体资源处理器，请求完成时触发回调。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回请求id，可用于cancelRequest取消请求。 |

**错误码：**

接口抛出错误码的详细介绍请参见[通用错误码]([通用错误码](../../errors/通用错误码.md).md)和[文件管理错误码]([文件管理错误码](../../errors/文件管理错误码.md).md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14000011 | System inner fail. |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](Functions.md#ZH-CN_TOPIC_0000002553362007__photoaccesshelpergetphotoaccesshelper)的示例使用。

```ets
import { dataSharePredicates } from '@kit.ArkData';
import { image } from '@kit.ImageKit';

class MediaHandler implements photoAccessHelper.MediaAssetDataHandler<image.ImageSource> {
  onDataPrepared(data: image.ImageSource) {
    if (data === undefined) {
      console.error('Error occurred when preparing data');
      return;
    }
    console.info('on image data prepared');
}

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper, context: Context) {
  console.info('requestImage');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOptions: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  let requestOptions: photoAccessHelper.RequestOptions = {
    deliveryMode: photoAccessHelper.DeliveryMode.HIGH_QUALITY_MODE,
  }
  const handler = new MediaHandler();

  phAccessHelper.getAssets(fetchOptions, async (err, fetchResult) => {
    console.info('fetchResult success');
    let photoAsset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
    if (photoAsset === undefined) {
      console.error('photoAsset is undefined');
      return;
    }
    await photoAccessHelper.MediaAssetManager.requestImage(context, photoAsset, requestOptions, handler);
    console.info('requestImage successfully');
  });
}
```

#### requestImageData11+

static requestImageData(context: Context, asset: PhotoAsset, requestOptions: RequestOptions, dataHandler: MediaAssetDataHandler<ArrayBuffer>): Promise<string>

根据不同的策略模式，请求图片资源数据。使用Promise异步回调。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**需要权限**：ohos.permission.READ_IMAGEVIDEO

- 通过picker的方式调用该接口来请求图片资源数据，不需要申请'ohos.permission.READ_IMAGEVIDEO'权限，详情请参考[指定URI获取图片或视频资源](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/photoaccesshelper-photoviewpicker#指定uri获取图片或视频资源)。

- 对于本应用保存到媒体库的图片资源，应用无需额外申请'ohos.permission.READ_IMAGEVIDEO'权限即可访问。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 传入Ability实例的上下文。 |
| asset | PhotoAsset | 是 | 待请求的媒体文件对象。 |
| requestOptions | RequestOptions | 是 | 图片请求策略模式配置项。 |
| dataHandler | MediaAssetDataHandler<ArrayBuffer> | 是 | 媒体资源处理器，当所请求的图片资源准备完成时会触发回调。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回请求id，可用于cancelRequest取消请求。 |

**错误码：**

接口抛出错误码的详细介绍请参见[通用错误码](通用错误码.md)和[文件管理错误码](文件管理错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14000011 | System inner fail. |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](Functions.md#ZH-CN_TOPIC_0000002553362007__photoaccesshelpergetphotoaccesshelper)的示例使用。

```ets
import { dataSharePredicates } from '@kit.ArkData';

class MediaDataHandler implements photoAccessHelper.MediaAssetDataHandler<ArrayBuffer> {
  onDataPrepared(data: ArrayBuffer) {
    if (data === undefined) {
      console.error('Error occurred when preparing data');
      return;
    }
    console.info('on image data prepared');
}

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper, context: Context) {
  console.info('requestImageData');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOptions: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  let requestOptions: photoAccessHelper.RequestOptions = {
    deliveryMode: photoAccessHelper.DeliveryMode.HIGH_QUALITY_MODE,
  }
  const handler = new MediaDataHandler();

  phAccessHelper.getAssets(fetchOptions, async (err, fetchResult) => {
      console.info('fetchResult success');
      let photoAsset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
      if (photoAsset === undefined) {
      console.error('requestImageData photoAsset is undefined');
      return;
    }
      await photoAccessHelper.MediaAssetManager.requestImageData(context, photoAsset, requestOptions, handler);
      console.info('requestImageData successfully');
  });
}
```

#### requestMovingPhoto12+

static requestMovingPhoto(context: Context, asset: PhotoAsset, requestOptions: RequestOptions, dataHandler: MediaAssetDataHandler<MovingPhoto>): Promise<string>

根据不同的策略模式，请求动态照片对象（动态照片对象可用于请求动态照片的资源数据）。使用Promise异步回调。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**需要权限**：ohos.permission.READ_IMAGEVIDEO

- 通过picker的方式调用该接口来请求动态照片对象，不需要申请'ohos.permission.READ_IMAGEVIDEO'权限，详情请参考[指定URI获取图片或视频资源](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/photoaccesshelper-photoviewpicker#指定uri获取图片或视频资源)。

- 对于本应用保存到媒体库的动态照片资源，应用无需额外申请'ohos.permission.READ_IMAGEVIDEO'权限即可访问。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 传入Ability实例的上下文。 |
| asset | PhotoAsset | 是 | 待请求的媒体文件对象。 |
| requestOptions | RequestOptions | 是 | 图片请求策略模式配置项。 |
| dataHandler | MediaAssetDataHandler<MovingPhoto> | 是 | 媒体资源处理器，当所请求的图片资源准备完成时会触发回调。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回请求id，可用于cancelRequest取消请求。 |

**错误码：**

接口抛出错误码的详细介绍请参见[通用错误码](通用错误码.md)和[文件管理错误码](文件管理错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 14000011 | System inner fail |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](Functions.md#ZH-CN_TOPIC_0000002553362007__photoaccesshelpergetphotoaccesshelper)的示例使用。

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
```

#### requestVideoFile12+

static requestVideoFile(context: Context, asset: PhotoAsset, requestOptions: RequestOptions, fileUri: string, dataHandler: MediaAssetDataHandler<boolean>): Promise<string>

根据不同的策略模式，请求视频资源数据到沙箱路径。使用Promise异步回调。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**需要权限**：ohos.permission.READ_IMAGEVIDEO

- 通过picker的方式调用该接口来请求视频资源数据到应用沙箱，不需要申请'ohos.permission.READ_IMAGEVIDEO'权限，详情请参考[指定URI获取图片或视频资源](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/photoaccesshelper-photoviewpicker#指定uri获取图片或视频资源)。

- 对于本应用保存到媒体库的视频资源，应用无需额外申请'ohos.permission.READ_IMAGEVIDEO'权限即可访问。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 传入Ability实例的上下文。 |
| asset | PhotoAsset | 是 | 待请求的媒体文件对象。 |
| requestOptions | RequestOptions | 是 | 视频请求策略模式配置项。 |
| fileUri | string | 是 | 目标写入沙箱路径uri。示例fileUri：'file://com.example.temptest/data/storage/el2/base/haps/entry/files/test.mp4'。 |
| dataHandler | MediaAssetDataHandler<boolean> | 是 | 媒体资源处理器，当所请求的视频资源写入完成时会触发回调。 视频资源写入成功时返回true，写入失败则返回false。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回请求id，可用于cancelRequest取消请求。 |

**错误码：**

接口抛出错误码的详细介绍请参见[通用错误码](通用错误码.md)和[文件管理错误码](文件管理错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 14000011 | System inner fail. |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](Functions.md#ZH-CN_TOPIC_0000002553362007__photoaccesshelpergetphotoaccesshelper)的示例使用。

```ets
import { dataSharePredicates } from '@kit.ArkData';

class MediaDataHandler implements photoAccessHelper.MediaAssetDataHandler<boolean> {
    onDataPrepared(data: boolean) {
        console.info('on video request status prepared');
}

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper, context: Context) {
  console.info('requestVideoFile');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOptions: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  let requestOptions: photoAccessHelper.RequestOptions = {
    deliveryMode: photoAccessHelper.DeliveryMode.HIGH_QUALITY_MODE,
  }
  const handler = new MediaDataHandler();
  let fileUri = 'file://com.example.temptest/data/storage/el2/base/haps/entry/files/test.mp4';
  phAccessHelper.getAssets(fetchOptions, async (err, fetchResult) => {
      console.info('fetchResult success');
      let photoAsset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
      await photoAccessHelper.MediaAssetManager.requestVideoFile(context, photoAsset, requestOptions, fileUri, handler);
      console.info('requestVideoFile successfully');
  });
}
```

#### cancelRequest12+

static cancelRequest(context: Context, requestId: string): Promise<void>

取消未触发回调的资产内容请求。使用Promise异步回调。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**需要权限**：ohos.permission.READ_IMAGEVIDEO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 传入Ability实例的上下文。 |
| requestId | string | 是 | 需要取消的请求id，requestImage等接口返回的有效请求id。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，返回void。 |

**错误码：**

接口抛出错误码的详细介绍请参见[通用错误码](通用错误码.md)和[文件管理错误码](文件管理错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14000011 | System inner fail |

**示例：**

```ets
import { dataSharePredicates } from '@kit.ArkData';

async function example(context: Context) {
  try {
    let requestId: string = 'xxx-xxx'; // 应用需使用requestImage等接口返回的有效requestId
    await photoAccessHelper.MediaAssetManager.cancelRequest(context, requestId);
    console.info("request cancelled successfully");
  } catch (err) {
    console.error(`cancelRequest failed with error: ${err.code}, ${err.message}`);
  }
```

#### loadMovingPhoto12+

static loadMovingPhoto(context: Context, imageFileUri: string, videoFileUri: string): Promise<MovingPhoto>

加载应用沙箱的动态照片。使用Promise异步回调。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 传入AbilityContext或者UIExtensionContext的实例。 |
| imageFileUri | string | 是 | 应用沙箱动态照片的图片uri。 示例：'file://com.example.temptest/data/storage/el2/base/haps/ImageFile.jpg' |
| videoFileUri | string | 是 | 应用沙箱动态照片的视频uri。 示例：'file://com.example.temptest/data/storage/el2/base/haps/VideoFile.mp4' |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<MovingPhoto> | Promise对象，返回MovingPhoto实例。 |

**错误码：**

接口抛出错误码的详细介绍请参见[通用错误码](通用错误码.md)和[文件管理错误码](文件管理错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14000011 | Internal system error. |

**示例：**

```ets
async function example(context: Context) {
  try {
    let imageFileUri: string = 'file://com.example.temptest/data/storage/el2/base/haps/ImageFile.jpg'; // 应用沙箱动态照片的图片uri。
    let videoFileUri: string = 'file://com.example.temptest/data/storage/el2/base/haps/VideoFile.mp4'; // 应用沙箱动态照片的视频uri。
    let movingPhoto: photoAccessHelper.MovingPhoto = await photoAccessHelper.MediaAssetManager.loadMovingPhoto(context, imageFileUri, videoFileUri);
  } catch (err) {
    console.error(`loadMovingPhoto failed with error: ${err.code}, ${err.message}`);
  }
```

#### quickRequestImage13+

static quickRequestImage(context: Context, asset: PhotoAsset, requestOptions: RequestOptions, dataHandler: QuickImageDataHandler<image.Picture>): Promise<string>

根据不同的策略模式，快速请求图片资源。使用Promise异步回调。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**需要权限**：ohos.permission.READ_IMAGEVIDEO

- 通过picker的方式调用该接口来请求图片资源，不需要申请'ohos.permission.READ_IMAGEVIDEO'权限，详情请参考[指定URI获取图片或视频资源](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/photoaccesshelper-photoviewpicker#指定uri获取图片或视频资源)。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 传入Ability实例的上下文。 |
| asset | PhotoAsset | 是 | 待请求的媒体文件对象。 |
| requestOptions | RequestOptions | 是 | 图片请求策略模式配置项。 |
| dataHandler | QuickImageDataHandler<image.Picture> | 是 | 媒体资源处理器，当所请求的图片资源准备完成时会触发回调。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回请求id，可用于cancelRequest取消请求。 |

**错误码：**

接口抛出错误码的详细介绍请参见[通用错误码](通用错误码.md)和[文件管理错误码](文件管理错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14000011 | Internal system error. |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](Functions.md#ZH-CN_TOPIC_0000002553362007__photoaccesshelpergetphotoaccesshelper)的示例使用。

```ets
import { dataSharePredicates } from '@kit.ArkData';
import { image } from '@kit.ImageKit';

class MediaHandler implements photoAccessHelper.QuickImageDataHandler<image.Picture> {
  onDataPrepared(data: image.Picture, imageSource: image.ImageSource, map: Map<string, string>) {
    console.info('on image data prepared');
}

async function example(context: Context) {
  console.info('quickRequestImage');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOptions: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  let requestOptions: photoAccessHelper.RequestOptions = {
    deliveryMode: photoAccessHelper.DeliveryMode.HIGH_QUALITY_MODE,
  }
  const handler = new MediaHandler();
  let phAccessHelper = photoAccessHelper.getPhotoAccessHelper(context);
  phAccessHelper.getAssets(fetchOptions, async (err, fetchResult) => {
      console.info('fetchResult success');
      let photoAsset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
      await photoAccessHelper.MediaAssetManager.quickRequestImage(context, photoAsset, requestOptions, handler);
      console.info('quickRequestImage successfully');
  });
}
```