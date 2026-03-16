# Interface (AbsAlbum)

本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { photoAccessHelper } from '@kit.MediaLibraryKit';
```

#### 属性

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

名称类型只读可选说明albumType[AlbumType](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529445919__albumtype)是否相册类型。albumSubtype[AlbumSubtype](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529445919__albumsubtype)是否相册子类型。albumNamestring否否相册名称。预置相册不可写，用户相册可写。albumUristring是否相册uri。countnumber是否相册中文件数量。coverUristring是否封面文件uri。

#### getAssets

getAssets(options: FetchOptions, callback: AsyncCallback<FetchResult<PhotoAsset>>): void

获取相册中的文件。使用callback异步回调。

**需要权限**：ohos.permission.READ_IMAGEVIDEO

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

参数名类型必填说明options[FetchOptions](Interfaces (其他).md#ZH-CN_TOPIC_0000002529285945__fetchoptions)是检索选项。callbackAsyncCallback<[FetchResult](Interface (FetchResult).md)<[PhotoAsset](Interface (PhotoAsset).md)>>是回调函数。当获取相册中的文件成功，err为undefined，data为获取到的图片和视频数据结果集[FetchResult](Interface (FetchResult).md)；否则为错误对象。

**错误码：**

接口抛出错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[文件管理错误码](../../errors/文件管理错误码.md)。

在API version 13及之前的版本，无相关权限返回错误码13900012；从API version 14开始，无相关权限返回错误码201。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.201Permission denied.13900020Invalid argument.14000011System inner fail.

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](../../topics/misc/Functions.md#ZH-CN_TOPIC_0000002529445911__photoaccesshelpergetphotoaccesshelper)的示例使用。

```ets
import { dataSharePredicates } from '@kit.ArkData';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('albumGetAssetsDemoCallback');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let albumFetchOptions: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  let fetchOption: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  let albumList: photoAccessHelper.FetchResult<photoAccessHelper.Album> = await phAccessHelper.getAlbums(photoAccessHelper.AlbumType.USER, photoAccessHelper.AlbumSubtype.USER_GENERIC, albumFetchOptions);
  let album: photoAccessHelper.Album = await albumList.getFirstObject();
  album.getAssets(fetchOption, (err, albumFetchResult) => {
    if (albumFetchResult !== undefined) {
      console.info('album getAssets successfully, getCount: ' + albumFetchResult.getCount());
    } else {
      console.error(`album getAssets failed with error: ${err.code}, ${err.message}`);
    }
  });
}
```

#### getAssets

getAssets(options: FetchOptions): Promise<FetchResult<PhotoAsset>>

获取相册中的文件。使用Promise异步回调。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**需要权限**：ohos.permission.READ_IMAGEVIDEO

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

参数名类型必填说明options[FetchOptions](Interfaces (其他).md#ZH-CN_TOPIC_0000002529285945__fetchoptions)是检索选项。

**返回值：**

类型说明Promise<[FetchResult](Interface (FetchResult).md)<[PhotoAsset](Interface (PhotoAsset).md)>>Promise对象，返回图片和视频数据结果集。

**错误码：**

接口抛出错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[文件管理错误码](../../errors/文件管理错误码.md)。

在API version 13及之前的版本，无相关权限返回错误码13900012；从API version 14开始，无相关权限返回错误码201。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.201Permission denied.13900020Invalid argument.14000011System inner fail.

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](../../topics/misc/Functions.md#ZH-CN_TOPIC_0000002529445911__photoaccesshelpergetphotoaccesshelper)的示例使用。

```ets
import { dataSharePredicates } from '@kit.ArkData';
import { BusinessError } from '@kit.BasicServicesKit';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('albumGetAssetsDemoPromise');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let albumFetchOptions: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  let fetchOption: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  let albumList: photoAccessHelper.FetchResult<photoAccessHelper.Album> = await phAccessHelper.getAlbums(photoAccessHelper.AlbumType.USER, photoAccessHelper.AlbumSubtype.USER_GENERIC, albumFetchOptions);
  let album: photoAccessHelper.Album = await albumList.getFirstObject();
  album.getAssets(fetchOption).then((albumFetchResult) => {
    console.info('album getAssets successfully, getCount: ' + albumFetchResult.getCount());
  }).catch((err: BusinessError) => {
    console.error(`album getAssets failed with error: ${err.code}, ${err.message}`);
  });
}
```