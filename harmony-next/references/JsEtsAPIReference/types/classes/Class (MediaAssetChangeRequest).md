# Class (MediaAssetChangeRequest)

MediaAssetChangeRequest implements [MediaChangeRequest](../interfaces/Interfaces (其他).md#ZH-CN_TOPIC_0000002529285945__mediachangerequest11).

资产变更请求。

- 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
- 本Class首批接口从API version 11开始支持。

#### 导入模块

```ets
import { photoAccessHelper } from '@kit.MediaLibraryKit';
```

#### constructor11+

constructor(asset: PhotoAsset)

构造函数，用于初始化资产变更请求。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

参数名类型必填说明asset[PhotoAsset](../interfaces/Interface (PhotoAsset).md)是需要变更的资产。

**错误码：**

接口抛出错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[文件管理错误码](../../errors/文件管理错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.14000011System inner fail.

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](../../topics/misc/Functions.md#ZH-CN_TOPIC_0000002529445911__photoaccesshelpergetphotoaccesshelper)的示例使用。

```ets
import { dataSharePredicates } from '@kit.ArkData';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('MediaAssetChangeRequest constructorDemo');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOptions: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOptions);
  let photoAsset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
  let assetChangeRequest: photoAccessHelper.MediaAssetChangeRequest = new photoAccessHelper.MediaAssetChangeRequest(photoAsset);
}
```

#### createImageAssetRequest11+

static createImageAssetRequest(context: Context, fileUri: string): MediaAssetChangeRequest

创建图片资产变更请求。

指定待创建资产的数据来源，可参考[FileUri](../../modules/ohos/@ohos.file.fileuri (文件URI).md)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

参数名类型必填说明context[Context](../../topics/graphics/Context (Stage模型的上下文基类).md)是传入Ability实例的上下文。fileUristring是图片资产的数据来源，在应用沙箱下的uri。示例fileUri：'file://com.example.temptest/data/storage/el2/base/haps/entry/files/test.jpg'。

**返回值：**

类型说明[MediaAssetChangeRequest](Class (MediaAssetChangeRequest).md)返回创建资产的变更请求。

**错误码：**

接口抛出错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[文件管理错误码](../../errors/文件管理错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.13900002The file corresponding to the URI is not in the app sandbox.14000011System inner fail.

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](../../topics/misc/Functions.md#ZH-CN_TOPIC_0000002529445911__photoaccesshelpergetphotoaccesshelper)的示例使用。

```ets
async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper, context: Context) {
  console.info('createImageAssetRequestDemo');
  try {
    // 需要确保fileUri对应的资源存在。
    let fileUri = 'file://com.example.temptest/data/storage/el2/base/haps/entry/files/test.jpg';
    let assetChangeRequest: photoAccessHelper.MediaAssetChangeRequest = photoAccessHelper.MediaAssetChangeRequest.createImageAssetRequest(context, fileUri);
    await phAccessHelper.applyChanges(assetChangeRequest);
    console.info('apply createImageAssetRequest successfully');
  } catch (err) {
    console.error(`createImageAssetRequestDemo failed with error: ${err.code}, ${err.message}`);
  }
}
```

#### createVideoAssetRequest11+

static createVideoAssetRequest(context: Context, fileUri: string): MediaAssetChangeRequest

创建视频资产变更请求。

指定待创建资产的数据来源，可参考[FileUri](../../modules/ohos/@ohos.file.fileuri (文件URI).md)。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

参数名类型必填说明context[Context](../../topics/graphics/Context (Stage模型的上下文基类).md)是传入Ability实例的上下文。fileUristring是视频资产的数据来源，在应用沙箱下的uri。示例fileUri：'file://com.example.temptest/data/storage/el2/base/haps/entry/files/test.mp4'。

**返回值：**

类型说明[MediaAssetChangeRequest](Class (MediaAssetChangeRequest).md)返回创建资产的变更请求。

**错误码：**

接口抛出错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[文件管理错误码](../../errors/文件管理错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.13900002The file corresponding to the URI is not in the app sandbox.14000011System inner fail.

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](../../topics/misc/Functions.md#ZH-CN_TOPIC_0000002529445911__photoaccesshelpergetphotoaccesshelper)的示例使用。

```ets
async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper, context: Context) {
  console.info('createVideoAssetRequestDemo');
  try {
    // 需要确保fileUri对应的资源存在。
    let fileUri = 'file://com.example.temptest/data/storage/el2/base/haps/entry/files/test.mp4';
    let assetChangeRequest: photoAccessHelper.MediaAssetChangeRequest = photoAccessHelper.MediaAssetChangeRequest.createVideoAssetRequest(context, fileUri);
    await phAccessHelper.applyChanges(assetChangeRequest);
    console.info('apply createVideoAssetRequest successfully');
  } catch (err) {
    console.error(`createVideoAssetRequestDemo failed with error: ${err.code}, ${err.message}`);
  }
}
```

#### createAssetRequest11+

static createAssetRequest(context: Context, photoType: PhotoType, extension: string, options?: CreateOptions): MediaAssetChangeRequest

指定文件类型和扩展名，创建资产变更请求。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

参数名类型必填说明context[Context](../../topics/graphics/Context (Stage模型的上下文基类).md)是传入Ability实例的上下文。photoType[PhotoType](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529445919__phototype)是待创建的文件类型，IMAGE或者VIDEO类型。extensionstring是文件扩展名，例如：'jpg'。options[CreateOptions](../interfaces/Interfaces (其他).md#ZH-CN_TOPIC_0000002529285945__createoptions)否

创建选项，例如：{title: 'testPhoto'}。

文件名中不允许出现非法英文字符，包括： . .. \ / : * ? " ' ` < > | { } [ ]

**返回值：**

类型说明[MediaAssetChangeRequest](Class (MediaAssetChangeRequest).md)返回创建资产的变更请求。

**错误码：**

接口抛出错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[文件管理错误码](../../errors/文件管理错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.14000011System inner fail.

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](../../topics/misc/Functions.md#ZH-CN_TOPIC_0000002529445911__photoaccesshelpergetphotoaccesshelper)的示例使用。

```ets
async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper, context: Context) {
  console.info('createAssetRequestDemo');
  try {
    let photoType: photoAccessHelper.PhotoType = photoAccessHelper.PhotoType.IMAGE;
    let extension: string = 'jpg';
    let options: photoAccessHelper.CreateOptions = {
      title: 'testPhoto'
    }
    let assetChangeRequest: photoAccessHelper.MediaAssetChangeRequest = photoAccessHelper.MediaAssetChangeRequest.createAssetRequest(context, photoType, extension, options);
    // 需要确保fileUri对应的资源存在。
    let fileUri = 'file://com.example.temptest/data/storage/el2/base/haps/entry/files/test.jpg';
    assetChangeRequest.addResource(photoAccessHelper.ResourceType.IMAGE_RESOURCE, fileUri);
    await phAccessHelper.applyChanges(assetChangeRequest);
    console.info('apply createAssetRequest successfully');
  } catch (err) {
    console.error(`createAssetRequestDemo failed with error: ${err.code}, ${err.message}`);
  }
}
```

#### deleteAssets11+

static deleteAssets(context: Context, assets: Array<PhotoAsset>): Promise<void>

删除媒体文件（删除的文件会进入到回收站）。使用Promise异步回调。

**需要权限**：ohos.permission.WRITE_IMAGEVIDEO

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

参数名类型必填说明context[Context](../../topics/graphics/Context (Stage模型的上下文基类).md)是传入Ability实例的上下文。assetsArray<[PhotoAsset](../interfaces/Interface (PhotoAsset).md)>是待删除的媒体文件数组，数组中元素个数不超过300个。

**返回值：**

类型说明Promise<void>Promise对象，返回void。

**错误码：**

接口抛出错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[文件管理错误码](../../errors/文件管理错误码.md)。

错误码ID错误信息201Permission denied.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.14000011System inner fail.

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](../../topics/misc/Functions.md#ZH-CN_TOPIC_0000002529445911__photoaccesshelpergetphotoaccesshelper)的示例使用。

```ets
import { dataSharePredicates } from '@kit.ArkData';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper, context: Context) {
  console.info('deleteAssetsDemo');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOptions: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  try {
    let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOptions);
    let photoAssetList: Array<photoAccessHelper.PhotoAsset> = await fetchResult.getAllObjects();
    await photoAccessHelper.MediaAssetChangeRequest.deleteAssets(context, photoAssetList);
    console.info('deleteAssets successfully');
  } catch (err) {
    console.error(`deleteAssetsDemo failed with error: ${err.code}, ${err.message}`);
  }
}
```

#### deleteAssets11+

static deleteAssets(context: Context, uriList: Array<string>): Promise<void>

删除媒体文件（删除的文件会进入到回收站）。使用Promise异步回调。

**需要权限**：ohos.permission.WRITE_IMAGEVIDEO

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

参数名类型必填说明context[Context](../../topics/graphics/Context (Stage模型的上下文基类).md)是传入Ability实例的上下文。uriListArray<string>是待删除的媒体文件uri数组，数组中元素个数不超过300个。

**返回值：**

类型说明Promise<void>Promise对象，返回void。

**错误码：**

接口抛出错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[文件管理错误码](../../errors/文件管理错误码.md)。

错误码ID错误信息201Permission denied.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.14000002The uri format is incorrect or does not exist.14000011System inner fail.

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](../../topics/misc/Functions.md#ZH-CN_TOPIC_0000002529445911__photoaccesshelpergetphotoaccesshelper)的示例使用。

```ets
import { dataSharePredicates } from '@kit.ArkData';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper, context: Context) {
  console.info('deleteAssetsDemo');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOptions: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  try {
    let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOptions);
    let asset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
    await photoAccessHelper.MediaAssetChangeRequest.deleteAssets(context, [asset.uri]);
    console.info('deleteAssets successfully');
  } catch (err) {
    console.error(`deleteAssetsDemo failed with error: ${err.code}, ${err.message}`);
  }
}
```

#### getAsset11+

getAsset(): PhotoAsset

获取当前资产变更请求中的资产。

对于创建资产的变更请求，在调用接口[applyChanges](../interfaces/Interface (PhotoAccessHelper).md#ZH-CN_TOPIC_0000002529445917__applychanges11)的提交生效之前，该接口会返回null。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**返回值：**

类型说明[PhotoAsset](../interfaces/Interface (PhotoAsset).md)返回当前资产变更请求中的资产。

**错误码：**

接口抛出错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[文件管理错误码](../../errors/文件管理错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.14000011System inner fail.

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](../../topics/misc/Functions.md#ZH-CN_TOPIC_0000002529445911__photoaccesshelpergetphotoaccesshelper)的示例使用。

```ets
async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper, context: Context) {
  console.info('getAssetDemo');
  try {
    // 需要确保fileUri对应的资源存在。
    let fileUri = 'file://com.example.temptest/data/storage/el2/base/haps/entry/files/test.jpg';
    let assetChangeRequest: photoAccessHelper.MediaAssetChangeRequest = photoAccessHelper.MediaAssetChangeRequest.createImageAssetRequest(context, fileUri);
    await phAccessHelper.applyChanges(assetChangeRequest);
    let asset: photoAccessHelper.PhotoAsset = assetChangeRequest.getAsset();
    console.info('create asset successfully with uri = ' + asset.uri);
  } catch (err) {
    console.error(`getAssetDemo failed with error: ${err.code}, ${err.message}`);
  }
}
```

#### setTitle11+

setTitle(title: string): void

修改媒体资产的标题。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

参数名类型必填说明titlestring是待修改的资产标题。

title参数规格为：

- 不应包含扩展名。
- 文件名字符串长度为1~255。
-

不允许出现的非法英文字符，包括：

 . \ / : * ? " ' ` < > | { } [ ]

**错误码：**

接口抛出错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[文件管理错误码](../../errors/文件管理错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.14000011System inner fail.

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](../../topics/misc/Functions.md#ZH-CN_TOPIC_0000002529445911__photoaccesshelpergetphotoaccesshelper)的示例使用。

```ets
import { dataSharePredicates } from '@kit.ArkData';
import { BusinessError } from '@kit.BasicServicesKit';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('setTitleDemo');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOption: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOption);
  let asset = await fetchResult.getFirstObject();
  let assetChangeRequest: photoAccessHelper.MediaAssetChangeRequest = new photoAccessHelper.MediaAssetChangeRequest(asset);
  let newTitle: string = 'newTitle';
  assetChangeRequest.setTitle(newTitle);
  phAccessHelper.applyChanges(assetChangeRequest).then(() => {
    console.info('apply setTitle successfully');
  }).catch((err: BusinessError) => {
    console.error(`apply setTitle failed with error: ${err.code}, ${err.message}`);
  });
}
```

#### getWriteCacheHandler11+

getWriteCacheHandler(): Promise<number>

获取临时文件写句柄。使用Promise异步回调。

对于同一个资产变更请求，不支持在成功获取临时文件写句柄后，重复调用该接口。

**需要权限**：ohos.permission.WRITE_IMAGEVIDEO

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**返回值：**

类型说明Promise<number>Promise对象，返回临时文件写句柄。

**错误码：**

接口抛出错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[文件管理错误码](../../errors/文件管理错误码.md)。

错误码ID错误信息201Permission denied.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.14000011System inner fail.14000016Operation Not Support.

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](../../topics/misc/Functions.md#ZH-CN_TOPIC_0000002529445911__photoaccesshelpergetphotoaccesshelper)的示例使用。

```ets
import { fileIo } from '@kit.CoreFileKit';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper, context: Context) {
  console.info('getWriteCacheHandlerDemo');
  try {
    let photoType: photoAccessHelper.PhotoType = photoAccessHelper.PhotoType.VIDEO;
    let extension: string = 'mp4';
    let assetChangeRequest: photoAccessHelper.MediaAssetChangeRequest = photoAccessHelper.MediaAssetChangeRequest.createAssetRequest(context, photoType, extension);
    let fd: number = await assetChangeRequest.getWriteCacheHandler();
    console.info('getWriteCacheHandler successfully');
    // write data into fd..
    await fileIo.close(fd);
    await phAccessHelper.applyChanges(assetChangeRequest);
  } catch (err) {
    console.error(`getWriteCacheHandlerDemo failed with error: ${err.code}, ${err.message}`);
  }
}
```

#### addResource11+

addResource(type: ResourceType, fileUri: string): void

通过[fileUri](../../modules/ohos/@ohos.file.fileuri (文件URI).md)从应用沙箱添加资源。

对于同一个资产变更请求，成功添加资源后不支持重复调用该接口。对于动态照片，可调用两次该接口分别添加图片和视频资源。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

参数名类型必填说明type[ResourceType](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529445919__resourcetype11)是待添加资源的类型。fileUristring是待添加资源的数据来源，在应用沙箱下的uri。示例fileUri：'file://com.example.temptest/data/storage/el2/base/haps/entry/files/test.jpg'。

**错误码：**

接口抛出错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[文件管理错误码](../../errors/文件管理错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.13900002The file corresponding to the URI is not in the app sandbox.14000011System inner fail.14000016Operation Not Support.

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](../../topics/misc/Functions.md#ZH-CN_TOPIC_0000002529445911__photoaccesshelpergetphotoaccesshelper)的示例使用。

```ets
async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper, context: Context) {
  console.info('addResourceByFileUriDemo');
  try {
    let photoType: photoAccessHelper.PhotoType = photoAccessHelper.PhotoType.IMAGE;
    let extension: string = 'jpg';
    let assetChangeRequest: photoAccessHelper.MediaAssetChangeRequest = photoAccessHelper.MediaAssetChangeRequest.createAssetRequest(context, photoType, extension);
    // 需要确保fileUri对应的资源存在。
    let fileUri = 'file://com.example.temptest/data/storage/el2/base/haps/entry/files/test.jpg';
    assetChangeRequest.addResource(photoAccessHelper.ResourceType.IMAGE_RESOURCE, fileUri);
    await phAccessHelper.applyChanges(assetChangeRequest);
    console.info('addResourceByFileUri successfully');
  } catch (err) {
    console.error(`addResourceByFileUriDemo failed with error: ${err.code}, ${err.message}`);
  }
}
```

#### addResource11+

addResource(type: ResourceType, data: ArrayBuffer): void

通过ArrayBuffer数据添加资源。

对于同一个资产变更请求，成功添加资源后不支持重复调用该接口。对于动态照片，可调用两次该接口分别添加图片和视频资源。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

参数名类型必填说明type[ResourceType](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529445919__resourcetype11)是待添加资源的类型。dataArrayBuffer是待添加资源的数据。

**错误码：**

接口抛出错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[文件管理错误码](../../errors/文件管理错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.14000011System inner fail.14000016Operation Not Support.

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](../../topics/misc/Functions.md#ZH-CN_TOPIC_0000002529445911__photoaccesshelpergetphotoaccesshelper)的示例使用。

```ets
async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper, context: Context) {
  console.info('addResourceByArrayBufferDemo');
  try {
    let photoType: photoAccessHelper.PhotoType = photoAccessHelper.PhotoType.IMAGE;
    let extension: string = 'jpg';
    let assetChangeRequest: photoAccessHelper.MediaAssetChangeRequest = photoAccessHelper.MediaAssetChangeRequest.createAssetRequest(context, photoType, extension);
    let buffer: ArrayBuffer = new ArrayBuffer(2048);
    assetChangeRequest.addResource(photoAccessHelper.ResourceType.IMAGE_RESOURCE, buffer);
    await phAccessHelper.applyChanges(assetChangeRequest);
    console.info('addResourceByArrayBuffer successfully');
  } catch (err) {
    console.error(`addResourceByArrayBufferDemo failed with error: ${err.code}, ${err.message}`);
  }
}
```

#### saveCameraPhoto12+

saveCameraPhoto(): void

保存相机拍摄的照片。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**错误码：**

接口抛出错误码的详细介绍请参见[文件管理错误码](../../errors/文件管理错误码.md)。

错误码ID错误信息14000011System inner fail.14000016Operation Not Support.

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](../../topics/misc/Functions.md#ZH-CN_TOPIC_0000002529445911__photoaccesshelpergetphotoaccesshelper)的示例使用。

```ets
async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper, asset: photoAccessHelper.PhotoAsset) {
  console.info('saveCameraPhotoDemo');
  try {
    let assetChangeRequest: photoAccessHelper.MediaAssetChangeRequest = new photoAccessHelper.MediaAssetChangeRequest(asset);
    assetChangeRequest.saveCameraPhoto();
    await phAccessHelper.applyChanges(assetChangeRequest);
    console.info('apply saveCameraPhoto successfully');
  } catch (err) {
    console.error(`apply saveCameraPhoto failed with error: ${err.code}, ${err.message}`);
  }
}
```

#### saveCameraPhoto13+

saveCameraPhoto(imageFileType: ImageFileType): void

保存相机拍摄的照片。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

参数名类型必填说明imageFileType[ImageFileType](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529445919__imagefiletype13)是需要保存的类型。

**错误码：**

接口抛出错误码的详细介绍请参见[文件管理错误码](../../errors/文件管理错误码.md)。

错误码ID错误信息14000011System inner fail.14000016Operation Not Support.

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](../../topics/misc/Functions.md#ZH-CN_TOPIC_0000002529445911__photoaccesshelpergetphotoaccesshelper)的示例使用。

```ets
import { dataSharePredicates } from '@kit.ArkData';
import { image } from '@kit.ImageKit';

async function example(context: Context, asset: photoAccessHelper.PhotoAsset) {
  console.info('saveCameraPhotoDemo');
  try {
    let phAccessHelper = photoAccessHelper.getPhotoAccessHelper(context);
    let assetChangeRequest: photoAccessHelper.MediaAssetChangeRequest = new photoAccessHelper.MediaAssetChangeRequest(asset);
    assetChangeRequest.saveCameraPhoto(photoAccessHelper.ImageFileType.JPEG);
    await phAccessHelper.applyChanges(assetChangeRequest);
    console.info('apply saveCameraPhoto successfully');
  } catch (err) {
    console.error(`apply saveCameraPhoto failed with error: ${err.code}, ${err.message}`);
  }
}
```

#### discardCameraPhoto12+

discardCameraPhoto(): void

删除相机拍摄的照片。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**错误码：**

接口抛出错误码的详细介绍请参见[文件管理错误码](../../errors/文件管理错误码.md)。

错误码ID错误信息14000011Internal system error.14000016Operation Not Support.

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](../../topics/misc/Functions.md#ZH-CN_TOPIC_0000002529445911__photoaccesshelpergetphotoaccesshelper)的示例使用。

```ets
async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper, asset: photoAccessHelper.PhotoAsset) {
  console.info('discardCameraPhotoDemo');
  try {
    let assetChangeRequest: photoAccessHelper.MediaAssetChangeRequest = new photoAccessHelper.MediaAssetChangeRequest(asset);
    assetChangeRequest.discardCameraPhoto();
    await phAccessHelper.applyChanges(assetChangeRequest);
    console.info('apply discardCameraPhoto successfully');
  } catch (err) {
    console.error(`apply discardCameraPhoto failed with error: ${err.code}, ${err.message}`);
  }
}
```

#### setOrientation15+

setOrientation(orientation: number): void

修改图片的旋转角度。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

参数名类型必填说明orientationnumber是待修改的图片旋转角度，且只能为0、90、180、270。

**错误码：**

接口抛出错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[文件管理错误码](../../errors/文件管理错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.14000011Internal system error.

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](../../topics/misc/Functions.md#ZH-CN_TOPIC_0000002529445911__photoaccesshelpergetphotoaccesshelper)的示例使用。

```ets
import { dataSharePredicates } from '@kit.ArkData';
import { BusinessError } from '@kit.BasicServicesKit';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('setOrientationDemo');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOption: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOption);
  let asset = await fetchResult.getFirstObject();
  let assetChangeRequest: photoAccessHelper.MediaAssetChangeRequest = new photoAccessHelper.MediaAssetChangeRequest(asset);
  assetChangeRequest.setOrientation(90);
  phAccessHelper.applyChanges(assetChangeRequest).then(() => {
    console.info('apply setOrientation successfully');
  }).catch((err: BusinessError) => {
    console.error(`apply setOrientation failed with error: ${err.code}, ${err.message}`);
  });
}
```