# Interface (PhotoAccessHelper)

本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { photoAccessHelper } from '@kit.MediaLibraryKit';
```

#### getAssets

getAssets(options: FetchOptions, callback: AsyncCallback<FetchResult<PhotoAsset>>): void

获取图片和视频资源，使用callback方式返回结果。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**需要权限**：ohos.permission.READ_IMAGEVIDEO

通过picker的方式调用该接口来查询指定URI对应的图片或视频资源，不需要申请'ohos.permission.READ_IMAGEVIDEO'权限，详情请参考[指定URI获取图片或视频资源](../../guides/使用Picker选择媒体库资源.md#指定uri获取图片或视频资源)。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | FetchOptions | 是 | 图片和视频检索选项。 |
| callback | AsyncCallback<FetchResult<PhotoAsset>> | 是 | callback返回图片和视频检索结果集。 |

**错误码：**

接口抛出错误码的详细介绍请参见[通用错误码]([通用错误码](../../errors/通用错误码.md).md)和[文件管理错误码]([文件管理错误码](../../errors/文件管理错误码.md).md)。

在API version 13及之前的版本，无相关权限返回错误码13900012；从API version 14开始，无相关权限返回错误码201。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 201 | Permission denied. |
| 13900020 | Invalid argument. |
| 14000011 | System inner fail. |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](Functions.md#ZH-CN_TOPIC_0000002553362007__photoaccesshelpergetphotoaccesshelper)的示例使用。

```ets
import { dataSharePredicates } from '@kit.ArkData';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('getAssets');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOptions: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };

  phAccessHelper.getAssets(fetchOptions, async (err, fetchResult) => {
    if (fetchResult !== undefined) {
      console.info('fetchResult success');
      let photoAsset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
      if (photoAsset !== undefined) {
        console.info('photoAsset.displayName : ' + photoAsset.displayName);
      }
    } else {
      console.error(`fetchResult fail with error: ${err.code}, ${err.message}`);
    }
  });
}
```

#### getAssets

getAssets(options: FetchOptions): Promise<FetchResult<PhotoAsset>>

获取图片和视频资源，使用Promise方式返回结果。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**需要权限**：ohos.permission.READ_IMAGEVIDEO

通过picker的方式调用该接口来查询指定URI对应的图片或视频资源，不需要申请'ohos.permission.READ_IMAGEVIDEO'权限，详情请参考[指定URI获取图片或视频资源](../../guides/使用Picker选择媒体库资源.md#指定uri获取图片或视频资源)。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | FetchOptions | 是 | 图片和视频检索选项。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<FetchResult<PhotoAsset>> | Promise对象，返回图片和视频数据结果集。 |

**错误码：**

接口抛出错误码的详细介绍请参见[通用错误码](通用错误码.md)和[文件管理错误码](文件管理错误码.md)。

在API version 13及之前的版本，无相关权限返回错误码13900012；从API version 14开始，无相关权限返回错误码201。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 13900020 | Invalid argument. |
| 14000011 | System inner fail. |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](Functions.md#ZH-CN_TOPIC_0000002553362007__photoaccesshelpergetphotoaccesshelper)的示例使用。

```ets
import { dataSharePredicates } from '@kit.ArkData';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('getAssets');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOptions: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  try {
    let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOptions);
    if (fetchResult !== undefined) {
      console.info('fetchResult success');
      let photoAsset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
      if (photoAsset !== undefined) {
        console.info('photoAsset.displayName :' + photoAsset.displayName);
      }
  } catch (err) {
    console.error(`getAssets failed, error: ${err.code}, ${err.message}`);
}
```

#### getBurstAssets12+

getBurstAssets(burstKey: string, options: FetchOptions): Promise<FetchResult<PhotoAsset>>

获取连拍照片资源，使用Promise方式返回结果。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**需要权限**：ohos.permission.READ_IMAGEVIDEO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| burstKey | string | 是 | 一组连拍照片的唯一标识：uuid(可传入[PhotoKeys](../enums/Enums.md#ZH-CN_TOPIC_0000002529445919__photokeys)的BURST_KEY)。字符串长度为36。 |
| options | FetchOptions | 是 | 连拍照片检索选项。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<FetchResult<PhotoAsset>> | Promise对象，返回连拍照片数据结果集。 |

**错误码：**

接口抛出错误码的详细介绍请参见[通用错误码](通用错误码.md)和[文件管理错误码](文件管理错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 14000011 | Internal system error. |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](Functions.md#ZH-CN_TOPIC_0000002553362007__photoaccesshelpergetphotoaccesshelper)的示例使用。

```ets
import { dataSharePredicates } from '@kit.ArkData';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('getBurstAssets');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOptions: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  // burstKey为36位的uuid，可以根据photoAccessHelper.PhotoKeys获取。
  let burstKey: string = "e719d696-09fa-44f8-8e9e-ec3f215aa62a";
  try {
    let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await
      phAccessHelper.getBurstAssets(burstKey, fetchOptions);
    if (fetchResult !== undefined) {
      console.info('fetchResult success');
      let photoAsset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
      if (photoAsset !== undefined) {
        console.info('photoAsset.displayName :' + photoAsset.displayName);
      }
  } catch (err) {
    console.error(`getBurstAssets failed, error: ${err.code}, ${err.message}`);
}
```

#### createAsset

createAsset(photoType: [PhotoType](../enums/Enums.md#ZH-CN_TOPIC_0000002529445919__phototype), extension: string, options: CreateOptions, callback: AsyncCallback<string>): void

指定文件类型、后缀和创建选项，创建图片或视频资源。使用callback方式返回结果。

在未申请相册管理模块权限'ohos.permission.WRITE_IMAGEVIDEO'时，可以使用安全控件或授权弹窗的方式创建媒体资源，详情请参考[保存媒体库资源](../../guides/保存媒体库资源.md)。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**需要权限**：ohos.permission.WRITE_IMAGEVIDEO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| photoType | [PhotoType](../enums/Enums.md#ZH-CN_TOPIC_0000002529445919__phototype) | 是 | 创建的文件类型，IMAGE或者VIDEO类型。 |
| extension | string | 是 | 文件名后缀参数，例如：'jpg'。 |
| options | CreateOptions | 是 | 创建选项，当前仅支持'title'，例如{title: 'testPhoto'}。 注意： 传入'subtype'选项，配置不生效，仅支持保存DEFAULT类型图片。 文件名中不允许出现非法英文字符，包括： . .. \ / : * ? " ' ` < > | { } [ ] |
callbackAsyncCallback<string>是callback返回创建的图片和视频的uri。

**错误码：**

接口抛出错误码的详细介绍请参见[通用错误码](通用错误码.md)和[文件管理错误码](文件管理错误码.md)。

在API version 13及之前的版本，无相关权限返回错误码13900012；从API version 14开始，无相关权限返回错误码201。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 201 | Permission denied. |
| 13900020 | Invalid argument. |
| 14000011 | System inner fail. |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](Functions.md#ZH-CN_TOPIC_0000002553362007__photoaccesshelpergetphotoaccesshelper)的示例使用。

```ets
async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('createAssetDemo');
  let photoType: photoAccessHelper.PhotoType = photoAccessHelper.PhotoType.IMAGE;
  let extension:string = 'jpg';
  let options: photoAccessHelper.CreateOptions = {
    title: 'testPhoto'
  }
  phAccessHelper.createAsset(photoType, extension, options, (err, uri) => {
    if (uri !== undefined) {
      console.info('createAsset uri' + uri);
      console.info('createAsset successfully');
    } else {
      console.error(`createAsset failed, error: ${err.code}, ${err.message}`);
    }
  });
}
```

#### createAsset

createAsset(photoType: [PhotoType](../enums/Enums.md#ZH-CN_TOPIC_0000002529445919__phototype), extension: string, callback: AsyncCallback<string>): void

指定文件类型和后缀，创建图片或视频资源，使用callback方式返回结果。

在未申请相册管理模块权限'ohos.permission.WRITE_IMAGEVIDEO'时，可以使用安全控件或授权弹窗的方式创建媒体资源，详情请参考[保存媒体库资源](../../guides/保存媒体库资源.md)。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**需要权限**：ohos.permission.WRITE_IMAGEVIDEO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| photoType | [PhotoType](../enums/Enums.md#ZH-CN_TOPIC_0000002529445919__phototype) | 是 | 创建的文件类型，IMAGE或者VIDEO类型。 |
| extension | string | 是 | 文件名后缀参数，例如：'jpg'。 |
| callback | AsyncCallback<string> | 是 | callback返回创建的图片和视频的uri。 |

**错误码：**

接口抛出错误码的详细介绍请参见[通用错误码](通用错误码.md)和[文件管理错误码](文件管理错误码.md)。

在API version 13及之前的版本，无相关权限返回错误码13900012；从API version 14开始，无相关权限返回错误码201。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 201 | Permission denied. |
| 13900020 | Invalid argument. |
| 14000011 | System inner fail. |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](Functions.md#ZH-CN_TOPIC_0000002553362007__photoaccesshelpergetphotoaccesshelper)的示例使用。

```ets
async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('createAssetDemo');
  let photoType: photoAccessHelper.PhotoType = photoAccessHelper.PhotoType.IMAGE;
  let extension: string = 'jpg';
  phAccessHelper.createAsset(photoType, extension, (err, uri) => {
    if (uri !== undefined) {
      console.info('createAsset uri' + uri);
      console.info('createAsset successfully');
    } else {
      console.error(`createAsset failed, error: ${err.code}, ${err.message}`);
    }
  });
}
```

#### createAsset

createAsset(photoType: [PhotoType](../enums/Enums.md#ZH-CN_TOPIC_0000002529445919__phototype), extension: string, options?: CreateOptions): Promise<string>

指定文件类型、后缀和创建选项，创建图片或视频资源，以Promise方式返回结果。

在未申请相册管理模块权限'ohos.permission.WRITE_IMAGEVIDEO'时，可以使用安全控件或授权弹窗的方式创建媒体资源，详情请参考[保存媒体库资源](../../guides/保存媒体库资源.md)。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**需要权限**：ohos.permission.WRITE_IMAGEVIDEO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| photoType | [PhotoType](../enums/Enums.md#ZH-CN_TOPIC_0000002529445919__phototype) | 是 | 创建的文件类型，IMAGE或者VIDEO类型。 |
| extension | string | 是 | 文件名后缀参数，例如：'jpg'。 |
| options | CreateOptions | 否 | 创建选项，当前仅支持'title'，例如{title: 'testPhoto'}。 注意： 传入'subtype'选项，配置不生效，仅支持保存DEFAULT类型图片。 文件名中不允许出现非法英文字符，包括： . .. \ / : * ? " ' ` < > | { } [ ] |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回创建的图片和视频的uri。 |

**错误码：**

接口抛出错误码的详细介绍请参见[通用错误码](通用错误码.md)和[文件管理错误码](文件管理错误码.md)。

在API version 13及之前的版本，无相关权限返回错误码13900012；从API version 14开始，无相关权限返回错误码201。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 201 | Permission denied. |
| 13900020 | Invalid argument. |
| 14000011 | System inner fail. |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](Functions.md#ZH-CN_TOPIC_0000002553362007__photoaccesshelpergetphotoaccesshelper)的示例使用。

```ets
async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('createAssetDemo');
  try {
    let photoType: photoAccessHelper.PhotoType = photoAccessHelper.PhotoType.IMAGE;
    let extension: string = 'jpg';
    let options: photoAccessHelper.CreateOptions = {
      title: 'testPhoto'
    }
    let uri: string = await phAccessHelper.createAsset(photoType, extension, options);
    console.info('createAsset uri' + uri);
    console.info('createAsset successfully');
  } catch (err) {
    console.error(`createAsset failed, error: ${err.code}, ${err.message}`);
  }
```

**createPhotoAsset23+**

createPhotoAsset(photoType: [PhotoType](../enums/Enums.md#ZH-CN_TOPIC_0000002529445919__phototype), extension: string, title?: string): Promise<string>

指定文件类型、后缀和标题，创建图片或视频资源。使用Promise异步回调。

在未申请相册管理模块权限'ohos.permission.WRITE_IMAGEVIDEO'时，可以使用安全控件或授权弹窗的方式创建媒体资源，详情请参考[开发指南](../../guides/保存媒体库资源.md)。

模型约束：此接口仅可在Stage模型下使用。

元服务API：从API version 23开始，该接口支持在元服务中使用。

需要权限：ohos.permission.WRITE_IMAGEVIDEO

系统能力：SystemCapability.FileManagement.PhotoAccessHelper.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| photoType | [PhotoType](../enums/Enums.md#ZH-CN_TOPIC_0000002529445919__phototype) | 是 | 创建的文件类型。例如：IMAGE或者VIDEO类型。 |
| extension | string | 是 | 文件名后缀参数。例如：'jpg'。 |
| title | string | 否 | 图片或视频资产的标题。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回创建的图片或视频的URL。 |

错误码：

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[媒体库错误码]([媒体库错误码](../../errors/媒体库错误码.md).md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 23800151 | The scenario parameter verification fails.Possible causes: 1. The extension format is unsupported. 2. Title contains unsupported character, such as . .. \ / : * ? " ' ` < > | { } [ ]. 3. The title is an empty string 4. The total length of title and extension is more than 255. |
| 23800301 | Internal systtem error. It is recommended to retry and check the logs.Possible causes: 1. Database corrupted; 2.The fille system is abnormal; 3. The IPC request time out. |

示例：

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](Functions.md#ZH-CN_TOPIC_0000002553362007__photoaccesshelpergetphotoaccesshelper)的示例使用。

```ets
async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('createPhotoAssetDemo');
  try {
    let photoType: photoAccessHelper.PhotoType = photoAccessHelper.PhotoType.IMAGE;
    let extension: string = 'jpg';
    let title: string = 'testPhoto';
    let uri: string = await phAccessHelper.createPhotoAsset(photoType, extension, title);
    console.info('createPhotoAsset uri' + uri);
    console.info('createPhotoAsset successfully');
  } catch (err) {
    console.error(`createPhotoAsset failed, error: ${err.code}, ${err.message}`);
}
```

#### getAlbums

getAlbums(type: [AlbumType](../enums/Enums.md#ZH-CN_TOPIC_0000002529445919__albumtype), subtype: AlbumSubtype, options: FetchOptions, callback: AsyncCallback<FetchResult<Album>>): void

根据检索选项和相册类型获取相册，使用callback方式返回结果。

获取相册前，确保相册已存在。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**需要权限**：ohos.permission.READ_IMAGEVIDEO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [AlbumType](../enums/Enums.md#ZH-CN_TOPIC_0000002529445919__albumtype) | 是 | 相册类型。 |
| subtype | [AlbumSubtype](../enums/Enums.md#ZH-CN_TOPIC_0000002529445919__albumsubtype) | 是 | 相册子类型。 |
| options | FetchOptions | 是 | 检索选项。 |
| callback | AsyncCallback<FetchResult<Album>> | 是 | callback返回获取相册的结果集。 |

**错误码：**

接口抛出错误码的详细介绍请参见[通用错误码](通用错误码.md)和[文件管理错误码](文件管理错误码.md)。

在API version 13及之前的版本，无相关权限返回错误码13900012；从API version 14开始，无相关权限返回错误码201。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 201 | Permission denied. |
| 13900020 | Invalid argument. |
| 14000011 | System inner fail. |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](Functions.md#ZH-CN_TOPIC_0000002553362007__photoaccesshelpergetphotoaccesshelper)的示例使用。

```ets
import { dataSharePredicates } from '@kit.ArkData';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  // 示例代码中为获取相册名为newAlbumName的相册。
  console.info('getAlbumsDemo');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  predicates.equalTo('album_name', 'newAlbumName');
  let fetchOptions: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  phAccessHelper.getAlbums(photoAccessHelper.AlbumType.USER, photoAccessHelper.AlbumSubtype.USER_GENERIC, fetchOptions, async (err, fetchResult) => {
    if (err) {
      console.error(`getAlbumsCallback failed with err: ${err.code}, ${err.message}`);
      return;
    }
    if (fetchResult === undefined) {
      console.error('getAlbumsCallback fetchResult is undefined');
      return;
    }
    let album = await fetchResult.getFirstObject();
    console.info('getAlbumsCallback successfully, albumName: ' + album.albumName);
    fetchResult.close();
  });
}
```

#### getAlbums

getAlbums(type: [AlbumType](../enums/Enums.md#ZH-CN_TOPIC_0000002529445919__albumtype), subtype: AlbumSubtype, callback: AsyncCallback<FetchResult<Album>>): void

根据相册类型获取相册，使用callback方式返回结果。

获取相册前需先保证相册存在。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**需要权限**：ohos.permission.READ_IMAGEVIDEO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [AlbumType](../enums/Enums.md#ZH-CN_TOPIC_0000002529445919__albumtype) | 是 | 相册类型。 |
| subtype | [AlbumSubtype](../enums/Enums.md#ZH-CN_TOPIC_0000002529445919__albumsubtype) | 是 | 相册子类型。 |
| callback | AsyncCallback<FetchResult<Album>> | 是 | callback返回获取相册的结果集。 |

**错误码：**

接口抛出错误码的详细介绍请参见[通用错误码](通用错误码.md)和[文件管理错误码](文件管理错误码.md)。

在API version 13及之前的版本，无相关权限返回错误码13900012；从API version 14开始，无相关权限返回错误码201。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 201 | Permission denied. |
| 13900020 | Invalid argument. |
| 14000011 | System inner fail. |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](Functions.md#ZH-CN_TOPIC_0000002553362007__photoaccesshelpergetphotoaccesshelper)的示例使用。

```ets
async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  // 示例代码中为获取系统相册VIDEO，默认已预置。
  console.info('getAlbumsDemo');
  phAccessHelper.getAlbums(photoAccessHelper.AlbumType.SYSTEM, photoAccessHelper.AlbumSubtype.VIDEO, async (err, fetchResult) => {
    if (err) {
      console.error(`getAlbumsCallback failed with err: ${err.code}, ${err.message}`);
      return;
    }
    if (fetchResult === undefined) {
      console.error('getAlbumsCallback fetchResult is undefined');
      return;
    }
    let album: photoAccessHelper.Album = await fetchResult.getFirstObject();
    console.info('getAlbumsCallback successfully, albumUri: ' + album.albumUri);
    fetchResult.close();
  });
}
```

#### getAlbums

getAlbums(type: [AlbumType](../enums/Enums.md#ZH-CN_TOPIC_0000002529445919__albumtype), subtype: AlbumSubtype, options?: FetchOptions): Promise<FetchResult<Album>>

根据检索选项和相册类型获取相册，使用Promise方式返回结果。

在获取相册之前，确保相册已存在。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**需要权限**：ohos.permission.READ_IMAGEVIDEO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [AlbumType](../enums/Enums.md#ZH-CN_TOPIC_0000002529445919__albumtype) | 是 | 相册类型。 |
| subtype | [AlbumSubtype](../enums/Enums.md#ZH-CN_TOPIC_0000002529445919__albumsubtype) | 是 | 相册子类型。 |
| options | FetchOptions | 否 | 检索选项，不填时默认根据相册类型检索。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<FetchResult<Album>> | Promise对象，返回获取相册的结果集。 |

**错误码：**

接口抛出错误码的详细介绍请参见[通用错误码](通用错误码.md)和[文件管理错误码](文件管理错误码.md)。

错误码13900012，请参考[开发准备](../../guides/开发准备（媒体库）.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 201 | Permission denied. |
| 13900020 | Invalid argument. |
| 14000011 | System inner fail. |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](Functions.md#ZH-CN_TOPIC_0000002553362007__photoaccesshelpergetphotoaccesshelper)的示例使用。

```ets
import { dataSharePredicates } from '@kit.ArkData';
import { BusinessError } from '@kit.BasicServicesKit';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  // 示例代码中为获取相册名为newAlbumName的相册。
  console.info('getAlbumsDemo');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  predicates.equalTo('album_name', 'newAlbumName');
  let fetchOptions: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  phAccessHelper.getAlbums(photoAccessHelper.AlbumType.USER, photoAccessHelper.AlbumSubtype.USER_GENERIC, fetchOptions).then( async (fetchResult) => {
    if (fetchResult === undefined) {
      console.error('getAlbumsPromise fetchResult is undefined');
      return;
    }
    let album: photoAccessHelper.Album = await fetchResult.getFirstObject();
    console.info('getAlbumsPromise successfully, albumName: ' + album.albumName);
    fetchResult.close();
  }).catch((err: BusinessError) => {
    console.error(`getAlbumsPromise failed with err: ${err.code}, ${err.message}`);
  });
}
```

#### registerChange

registerChange(uri: string, forChildUris: boolean, callback: Callback<ChangeData>) : void

注册指定uri的监听，并通过callback方式返回异步结果。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | PhotoAsset的uri, Album的uri或[DefaultChangeUri](../enums/Enums.md#ZH-CN_TOPIC_0000002529445919__defaultchangeuri)的值。 |
| forChildUris | boolean | 是 | 是否模糊监听。uri为相册uri时：forChildUris为true，能监听到相册中文件的变化。如果是false，只能监听相册本身变化；uri为photoAsset时：forChildUris为true、false没有区别；uri为[DefaultChangeUri](../enums/Enums.md#ZH-CN_TOPIC_0000002529445919__defaultchangeuri)时：forChildUris必须为true，如果为false将找不到该uri，收不到任何消息。 |
| callback | Callback<ChangeData> | 是 | 返回要监听的ChangeData。注：uri可以注册多个不同的callback监听，unRegisterChange可以关闭该uri所有监听，也可以关闭指定callback的监听。 |

**错误码：**

接口抛出错误码的详细介绍请参见[通用错误码](通用错误码.md)和[文件管理错误码](文件管理错误码.md)。

错误码13900012，请参考[开发准备](../../guides/开发准备（媒体库）.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 13900012 | Permission denied. |
| 13900020 | Invalid argument. |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](Functions.md#ZH-CN_TOPIC_0000002553362007__photoaccesshelpergetphotoaccesshelper)的示例使用。

```ets
import { dataSharePredicates } from '@kit.ArkData';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper, context: Context) {
  console.info('registerChangeDemo');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOptions: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOptions);
  let photoAsset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
  if (photoAsset !== undefined) {
    console.info('photoAsset.displayName : ' + photoAsset.displayName);
  }
  let onCallback1 = (changeData: photoAccessHelper.ChangeData) => {
      console.info('onCallback1 success, changData: ' + JSON.stringify(changeData));
    //file had changed, do something.
  }
  let onCallback2 = (changeData: photoAccessHelper.ChangeData) => {
      console.info('onCallback2 success, changData: ' + JSON.stringify(changeData));
    //file had changed, do something.
  }
  // 注册onCallback1监听。
  phAccessHelper.registerChange(photoAsset.uri, false, onCallback1);
  // 注册onCallback2监听。
  phAccessHelper.registerChange(photoAsset.uri, false, onCallback2);

  await photoAccessHelper.MediaAssetChangeRequest.deleteAssets(context, [photoAsset]);
}
```

#### unRegisterChange

unRegisterChange(uri: string, callback?: Callback<ChangeData>): void

取消指定uri的监听，一个uri可以注册多个监听，存在多个callback监听时，可以取消指定注册的callback的监听；不指定callback时取消该uri的所有监听。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | PhotoAsset的uri, Album的uri或[DefaultChangeUri](../enums/Enums.md#ZH-CN_TOPIC_0000002529445919__defaultchangeuri)的值。 |
| callback | Callback<ChangeData> | 否 | 取消registerChange注册时的callback的监听，不填时，取消该uri的所有监听。注：off指定注册的callback后不会进入此回调。 |

**错误码：**

接口抛出错误码的详细介绍请参见[通用错误码](通用错误码.md)和[文件管理错误码](文件管理错误码.md)。

错误码13900012，请参考[开发准备](../../guides/开发准备（媒体库）.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 13900012 | Permission denied. |
| 13900020 | Invalid argument. |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](Functions.md#ZH-CN_TOPIC_0000002553362007__photoaccesshelpergetphotoaccesshelper)的示例使用。

```ets
import { dataSharePredicates } from '@kit.ArkData';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper, context: Context) {
  console.info('offDemo');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOptions: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOptions);
  let photoAsset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
  if (photoAsset !== undefined) {
    console.info('photoAsset.displayName : ' + photoAsset.displayName);
  }
  let onCallback1 = (changeData: photoAccessHelper.ChangeData) => {
    console.info('onCallback1 on');
  }
  let onCallback2 = (changeData: photoAccessHelper.ChangeData) => {
    console.info('onCallback2 on');
  }
  // 注册onCallback1监听。
  phAccessHelper.registerChange(photoAsset.uri, false, onCallback1);
  // 注册onCallback2监听。
  phAccessHelper.registerChange(photoAsset.uri, false, onCallback2);
  // 关闭onCallback1监听，onCallback2 继续监听。
  phAccessHelper.unRegisterChange(photoAsset.uri, onCallback1);
  await photoAccessHelper.MediaAssetChangeRequest.deleteAssets(context, [photoAsset]);
}
```

#### applyChanges11+

applyChanges(mediaChangeRequest: MediaChangeRequest): Promise<void>

提交媒体变更请求，使用Promise方式返回结果。

**需要权限**：ohos.permission.WRITE_IMAGEVIDEO

在未申请相册管理模块权限'ohos.permission.WRITE_IMAGEVIDEO'时，可以使用安全控件或授权弹窗的方式创建媒体资源，详情请参考[保存媒体库资源](../../guides/保存媒体库资源.md)。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mediaChangeRequest | MediaChangeRequest | 是 | 媒体变更请求，支持资产变更请求和相册变更请求。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，返回void。 |

**错误码：**

接口抛出错误码的详细介绍请参见[通用错误码](通用错误码.md)和[文件管理错误码](文件管理错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14000011 | System inner fail. |

**示例：**

该接口依赖于[MediaChangeRequest](Interfaces (其他).md#ZH-CN_TOPIC_0000002522082094__mediachangerequest11)对象，详细代码示例请参见[MediaAssetChangeRequest](Class (MediaAssetChangeRequest).md)和[MediaAlbumChangeRequest](Class (MediaAlbumChangeRequest).md)中的接口示例。

#### release

release(callback: AsyncCallback<void>): void

释放PhotoAccessHelper实例。使用callback异步回调。

当后续不需要使用PhotoAccessHelper实例中的方法时调用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调表示成功还是失败。 |

**错误码：**

接口抛出错误码的详细介绍请参见[通用错误码](通用错误码.md)和[文件管理错误码](文件管理错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 13900020 | Invalid argument. |
| 14000011 | System inner fail. |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](Functions.md#ZH-CN_TOPIC_0000002553362007__photoaccesshelpergetphotoaccesshelper)的示例使用。

```ets
async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('releaseDemo');
  phAccessHelper.release((err) => {
    if (err !== undefined) {
      console.error(`release failed. error: ${err.code}, ${err.message}`);
    } else {
      console.info('release ok.');
    }
  });
}
```

#### release

release(): Promise<void>

释放PhotoAccessHelper实例。使用Promise异步回调。

当后续不需要使用PhotoAccessHelper 实例中的方法时调用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，返回void。 |

**错误码：**

接口抛出错误码的详细介绍请参见[通用错误码](通用错误码.md)和[文件管理错误码](文件管理错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 13900020 | Invalid argument. |
| 14000011 | System inner fail. |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](Functions.md#ZH-CN_TOPIC_0000002553362007__photoaccesshelpergetphotoaccesshelper)的示例使用。

```ets
async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('releaseDemo');
  try {
    await phAccessHelper.release();
    console.info('release ok.');
  } catch (err) {
    console.error(`release failed. error: ${err.code}, ${err.message}`);
  }
```

#### showAssetsCreationDialog12+

showAssetsCreationDialog(srcFileUris: Array<string>, photoCreationConfigs: Array<PhotoCreationConfig>): Promise<Array<string>>

调用接口显示保存确认弹窗。如果用户同意保存，将返回一个已创建并授予保存权限的URI列表（此列表永久生效），应用可使用这些URI写入图片或视频。如果用户拒绝保存，将返回一个空列表。

弹框需显示应用名称，但无法直接获取。因此，调用此接口时，请确保module.json5文件中的abilities标签已配置label和icon项。需要注意的是，图标不受abilities标签中的icon项影响，不支持修改。


当传入URI为沙箱路径时，可正常保存图片/视频，但无界面预览。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| srcFileUris | Array<string> | 是 | 需保存到媒体库中的图片/视频文件对应的媒体文件URI。 注意： - 一次弹窗最多保存100张图片。 - 仅支持处理图片、视频URI。 - 不支持手动拼接的URI，需调用接口获取，获取方式参考媒体文件URI获取方式。 |
| photoCreationConfigs | Array<PhotoCreationConfig> | 是 | 保存图片或视频到媒体库的配置，包括文件名等，与srcFileUris保持一一对应。 注意： 传入'subtype'选项，配置项不生效，仅支持保存DEFAULT类型图片。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<string>> | Promise对象，返回给应用的媒体库文件URI列表。URI已对应用授权，支持应用写入数据。如果生成URI异常，则返回批量创建错误码。 具体返回值情况如下： - 返回-3006表示不允许出现非法字符。 - 返回-2004表示图片类型和后缀不符。 - 返回-203表示文件操作异常。 |

**错误码：**

接口抛出错误码的详细介绍请参见[通用错误码](通用错误码.md)和[文件管理错误码](文件管理错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14000011 | Internal system error. |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](Functions.md#ZH-CN_TOPIC_0000002553362007__photoaccesshelpergetphotoaccesshelper)的示例使用。

```ets
import { dataSharePredicates } from '@kit.ArkData';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('ShowAssetsCreationDialogDemo.');

  try {
    // 获取需要保存到媒体库的位于应用沙箱的图片/视频uri。
    let srcFileUris: Array<string> = [
      'file://fileUriDemo1' // 实际场景请使用真实的uri。
    ];
    let photoCreationConfigs: Array<photoAccessHelper.PhotoCreationConfig> = [
      {
        title: 'test2', // 可选。
        fileNameExtension: 'jpg',
        photoType: photoAccessHelper.PhotoType.IMAGE,
        subtype: photoAccessHelper.PhotoSubtype.DEFAULT, // 可选。
      }
    ];
    let desFileUris: Array<string> = await phAccessHelper.showAssetsCreationDialog(srcFileUris, photoCreationConfigs);
    console.info('showAssetsCreationDialog success, data is ' + desFileUris);
  } catch (err) {
    console.error('showAssetsCreationDialog failed, errCode is ' + err.code + ', errMsg is ' + err.message);
  }
```

**showAssetsCreationDialogEx23+**

showAssetsCreationDialogEx(srcFileUris: Array<string>, creationSettings: Array<CreationSetting>): Promise<Array<string>>

调用接口显示保存确认弹窗。使用Promise异步回调。


- 用户同意后，返回已创建并授予保存权限的URI列表，该列表永久有效，支持写入图片/视频。用户拒绝时，返回空列表。

- 弹框需显示应用名称，名称和图标需在module.json5文件的abilities标签中配置label和icon项。

- 当传入URI为沙箱路径时，可正常保存图片或视频，但不显示界面预览。

模型约束：此接口仅可在Stage模型下使用。

元服务API：从API version 23开始，该接口支持在元服务中使用。

系统能力：SystemCapability.FileManagement.PhotoAccessHelper.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| srcFileUris | Array<string> | 是 | 需保存到媒体库中的图片或视频文件对应的媒体文件URI。 注意： - 一次弹窗最多保存100张图片。 - 仅支持处理图片和视频URI。 - 不支持手动拼接URI，需调用接口获取，具体请参考媒体文件URI获取方式。 |
| creationSettings | Array<CreationSetting> | 是 | 保存图片或视频到媒体库的配置，包括文件名等，与srcFileUris参数中的URI保持一一对应。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<Array<string>> | Promise对象，返回给应用的媒体库文件URI列表。支持应用使用返回的URI写入数据。 |

错误码：

以下错误码的详细介绍请参见[媒体库错误码](媒体库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 23800301 | Internal system error. It is recommended to retry and check the logs. Possible causes: 1. Database corrupted; 2. The file system is abnormal; 3. The IPC request timed out. |

示例：

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](Functions.md#ZH-CN_TOPIC_0000002553362007__photoaccesshelpergetphotoaccesshelper)的示例使用。

```ets
import { dataSharePredicates } from '@kit.ArkData';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('ShowAssetsCreationDialogExDemo.');

  try {
    // 获取需要保存到媒体库的位于应用沙箱的图片/视频uri。
    let srcFileUris: Array<string> = [
      'file://fileUriDemo1' // 实际场景请使用真实的uri。
    ];
    let creationSettings: Array<photoAccessHelper.CreationSetting> = [
      {
        title: 'test2', // 可选。
        fileNameExtension: 'jpg',
        photoType: photoAccessHelper.PhotoType.IMAGE
      }
    ];
    let desFileUris: Array<string> = await phAccessHelper.showAssetsCreationDialogEx(srcFileUris, photoCreationConfigs);
    console.info('showAssetsCreationDialogEx success, data is ' + desFileUris);
  } catch (err) {
    console.error('showAssetsCreationDialogEx failed, errCode is ' + err.code + ', errMsg is ' + err.message);
  }
```

**showSingleAssetCreationDialogEx23+**

showSingleAssetCreationDialogEx(srcFileUri: string, creationSetting: CreationSetting, isImageFullyDisplayed: boolean): Promise<string>

针对单个图片/视频调用接口显示保存确认弹窗。使用Promise异步回调。


- 如果用户同意保存，将返回一个已创建并授予保存权限的URI（此URI永久生效），应用可使用这个URI写入图片或视频。如果用户拒绝保存，将返回一个空字符串。

- 弹框需显示应用名称，但无法直接获取。因此，调用此接口时，请确保module.json5文件中的abilities标签已配置label和icon项。需要注意的是，图标不受abilities标签中的icon项影响，不支持修改。

- 当传入URI为沙箱路径时，可正常保存图片/视频，但无界面预览。

模型约束：此接口仅可在Stage模型下使用。

元服务API： 从API version 23开始，该接口支持在元服务中使用。

系统能力：SystemCapability.FileManagement.PhotoAccessHelper.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| srcFileUri | string | 是 | 需要保存到媒体库中的图片/视频文件所对应的媒体文件URI。 注意： - 一次弹窗最多保存1张图片。 - 仅支持处理图片、视频URI。 - 不支持手动拼接的URI，需调用接口获取，具体请参考媒体文件URI获取方式。 |
| creationSetting | CreationSetting | 是 | 保存图片或视频到媒体库的配置（包括文件名等），与srcFileUri保持对应。 |
| isImageFullyDisplayed | boolean | 是 | 表示是否完整显示图片。true表示完整显示，false表示不完整显示。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回给应用的媒体库文件URI。URI已对应用授权，支持应用写入数据。如果生成URI异常，则返回批量创建错误码。 具体返回值情况如下： - 返回-3006表示不允许出现非法字符。 - 返回-2004表示图片类型和后缀不符。 - 返回-203表示文件操作异常。 |

错误码：

以下错误码的详细介绍请参见[媒体库错误码](媒体库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 23800301 | Internal system error. It is recommended to retry and check the logs. Possible causes: 1. Database corrupted; 2. The file system is abnormal; 3. The IPC request timed out. |

示例：

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](Functions.md#ZH-CN_TOPIC_0000002553362007__photoaccesshelpergetphotoaccesshelper)的示例使用。

```ets
import { dataSharePredicates } from '@kit.ArkData';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('ShowSingleAssetCreationDialogExDemo.');

  try {
    // 获取需要保存到媒体库的位于应用沙箱的图片/视频uri。
    let srcFileUri: string = [
      'file://fileUriDemo1' // 实际场景请使用真实的uri。
    ];
    let creationSetting: photoAccessHelper.CreationSetting = {
      title: 'test2', // 可选。
      fileNameExtension: 'jpg',
      photoType: photoAccessHelper.PhotoType.IMAGE
    }
    let isImageFullyDisplayed: boolean = true
    let desFileUri: string = await phAccessHelper.showSingleAssetCreationDialogEx(srcFileUris, photoCreationConfigs, isImageFullyDisplayed);
    console.info('showSingleAssetCreationDialogEx success, data is ' + desFileUris);
  } catch (err) {
    console.error('showSingleAssetCreationDialogEx failed, errCode is ' + err.code + ', errMsg is ' + err.message);
}
```

#### createAssetWithShortTermPermission12+

createAssetWithShortTermPermission(photoCreationConfig: PhotoCreationConfig): Promise<string>

接口提供给应用调用，支持首次调用后拉起保存确认弹框。在用户同意保存后返回已创建并授予保存权限的uri，支持应用使用uri写入图片/视频。

在用户"同意"后的5分钟之内，同一个应用再次调用接口，支持无需弹框确认自动返回已授权的uri给应用，支持应用保存图片/视频。退出应用会结束授权，再次进入需要重新弹出弹框进行确认授权。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**需要权限：** ohos.permission.SHORT_TERM_WRITE_IMAGEVIDEO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| photoCreationConfig | PhotoCreationConfig; | 是 | 保存图片/视频到媒体库的配置，包括保存的文件名等。 注意： 传入'subtype'选项，配置项不生效，仅支持保存DEFAULT类型图片。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回给应用的媒体库文件uri。uri已对应用授权，支持应用写入数据。如果生成uri异常，则返回批量创建错误码。 返回-3006表示不允许出现非法字符；返回-2004表示图片类型和后缀不符；返回-203表示文件操作异常。 |

**错误码：**

接口抛出错误码的详细介绍请参见[通用错误码](通用错误码.md)和[文件管理错误码](文件管理错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14000011 | Internal system error |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](Functions.md#ZH-CN_TOPIC_0000002553362007__photoaccesshelpergetphotoaccesshelper)的示例使用。

```ets
import { fileIo } from '@kit.CoreFileKit';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
    console.info('createAssetWithShortTermPermissionDemo.');

    try {
        let photoCreationConfig: photoAccessHelper.PhotoCreationConfig = {
            title: '123456',
            fileNameExtension: 'jpg',
            photoType: photoAccessHelper.PhotoType.IMAGE,
            subtype: photoAccessHelper.PhotoSubtype.DEFAULT,
        };

        let resultUri: string = await phAccessHelper.createAssetWithShortTermPermission(photoCreationConfig);
        let resultFile: fileIo.File = fileIo.openSync(resultUri, fileIo.OpenMode.READ_WRITE);
        // 实际场景请使用真实的uri和文件大小。
        let srcFile:  fileIo.File = fileIo.openSync("file://test.jpg", fileIo.OpenMode.READ_ONLY);
        let bufSize: number = 2000000;
        let readSize: number = 0;
        let buf = new ArrayBuffer(bufSize);
        let readLen = fileIo.readSync(srcFile.fd, buf, {
            offset: readSize,
            length: bufSize
        });
        if (readLen > 0) {
            readSize += readLen;
            fileIo.writeSync(resultFile.fd, buf, { length: readLen });
        }
        fileIo.closeSync(srcFile);
        fileIo.closeSync(resultFile);
    } catch (err) {
        console.error('createAssetWithShortTermPermission failed, errCode is ' + err.code + ', errMsg is ' + err.message);
    }

}
```

**createAssetWithShortTermPermissionEx23+**

createAssetWithShortTermPermissionEx(creationSetting: CreationSetting): Promise<string>

应用调用该接口后，系统会首次拉起保存确认弹框。使用Promise异步回调。


- 用户同意保存后，接口将返回已创建并授予保存权限的URI，应用可使用该URI写入图片/视频。

- 在用户同意后的5分钟内，若同一应用再次调用此接口，系统将无需弹框确认，直接返回已授权的URI，供应用保存图片/视频。退出应用会结束授权，再次进入需要重新弹出弹框进行确认授权。

模型约束：此接口仅可在Stage模型下使用。

系统能力：SystemCapability.FileManagement.PhotoAccessHelper.Core

需要权限：ohos.permission.SHORT_TERM_WRITE_IMAGEVIDEO

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| creationSetting | CreationSetting | 是 | 保存图片或视频到媒体库时的配置项，包括保存的文件名等。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回给应用的媒体库文件URI。支持应用使用返回的URI写入数据。 |

错误码：

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[文件管理错误码](文件管理错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied |
| 14000011 | Internal system error |

#### requestPhotoUrisReadPermission14+

requestPhotoUrisReadPermission(srcFileUris: Array<string>): Promise<Array<string>>

从HarmonyOS 3.1/4.0进入HarmonyOS 5.0时，调用接口给未授权的URI进行授权，返回已创建并授予保存权限的URI列表。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| srcFileUris | Array<string> | 是 | 需进行授权的图片/视频文件对应的媒体文件URI。 注意： 仅支持处理图片、视频URI，且最大数量限制为100个。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<string>> | Promise对象，返回已授权的URI列表。 |

**错误码：**

接口抛出错误码的详细介绍请参见[通用错误码](通用错误码.md)和[文件管理错误码](文件管理错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14000011 | Internal system error |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](Functions.md#ZH-CN_TOPIC_0000002553362007__photoaccesshelpergetphotoaccesshelper)的示例使用。

```ets
import { dataSharePredicates } from '@kit.ArkData';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper, context: Context) {
  console.info('requestPhotoUrisReadPermissionDemo.');

  try {
    // 获取需要进行授权的图片/视频uri。
    let srcFileUris: Array<string> = [
      'file://fileUriDemo1' // 实际场景请使用真实的uri。
    ];
    let desFileUris: Array<string> = await phAccessHelper.requestPhotoUrisReadPermission(srcFileUris);
    console.info('requestPhotoUrisReadPermission success, data is ' + desFileUris);
  } catch (err) {
    console.error('requestPhotoUrisReadPermission failed, errCode is ' + err.code + ', errMsg is ' + err.message);
  }
```

**requestPhotoUrisReadPermissionEx23+**

requestPhotoUrisReadPermissionEx(srcFileUris: Array<string>): Promise<RequestReadPermissionResult>

应用调用接口为未授权的URI授权。使用promise异步回调。

返回授权结果，其中包含已创建并授予保存权限的URI列表以及无效的URI列表。

元服务API： 从API version 23开始，该接口支持在元服务中使用。

​模型约束： 此接口仅可在Stage模型下使用。

系统能力：SystemCapability.FileManagement.PhotoAccessHelper.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| srcFileUris | Array<string> | 是 | 需进行授权的图片/视频文件对应的媒体库uri。 注意： 仅支持处理图片、视频uri，且最大数量限制为100个。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<RequestReadPermissionResult> | Promise对象，返回已授权的uri列表和无效的uri列表。 |

错误码：

接口抛出错误码的详细介绍请参见[媒体库错误码](媒体库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 23800301 | Internal system error. You are advised to retry and check the logs. Possible causes: 1. The database is corrupted. 2. The file system is abnormal. 3. The IPC request timed out. |

示例：

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](Functions.md#ZH-CN_TOPIC_0000002553362007__photoaccesshelpergetphotoaccesshelper)的示例使用。

```ets
import { dataSharePredicates } from '@kit.ArkData';
import { photoAccessHelper } from '@kit.MediaLibraryKit';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper, context: Context) {
console.info('requestPhotoUrisReadPermissionExDemo.');

  try {
    // 获取需要进行授权的图片/视频uri。
    let srcFileUris: Array<string> = [
      'file://fileUriDemo1' // 实际场景请使用真实的uri。
    ];
    let requestReadPermissionResult: photoAccessHelper.RequestReadPermissionResult = await phAccessHelper.requestPhotoUrisReadPermissionEx(srcFileUris);
    console.info('requestPhotoUrisReadPermissionEx success, data is ' + requestReadPermissionResult);
  } catch (err) {
    console.error('requestPhotoUrisReadPermissionEx failed, errCode is ' + err.code + ', errMsg is ' + err.message);
}
```

#### getSupportedPhotoFormats18+

getSupportedPhotoFormats(photoType: [PhotoType](../enums/Enums.md#ZH-CN_TOPIC_0000002529445919__phototype)): Promise<Array<string>>

接口提供给应用调用，获取媒体库支持的图片或者视频后缀列表。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| photoType | [PhotoType](../enums/Enums.md#ZH-CN_TOPIC_0000002529445919__phototype) | 是 | 媒体文件类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<string>> | Promise对象，返回支持的图片或者视频后缀列表。 |

**错误码：**

接口抛出错误码的详细介绍请参见[通用错误码](通用错误码.md)和[文件管理错误码](文件管理错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14000011 | Internal system error. It is recommended to retry and check the logs. |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](Functions.md#ZH-CN_TOPIC_0000002553362007__photoaccesshelpergetphotoaccesshelper)的示例使用。

```ets
async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper, photoTypeNumber: number){
  console.info('getSupportedPhotoFormatsDemo.');

  try {
    let outputText: string;
    if (photoTypeNumber !== photoAccessHelper.PhotoType.IMAGE && photoTypeNumber !== photoAccessHelper.PhotoType.VIDEO) {
      outputText = 'Does not support querying formats other than images or videos';
      return;
    }
    outputText = 'The supported types are:\n';
    let imageFormat  = await phAccessHelper.getSupportedPhotoFormats(photoAccessHelper.PhotoType.IMAGE);
    let result = "";
    for (let i = 0; i < imageFormat.length; i++) {
      result += imageFormat[i];
      if (i !== imageFormat.length - 1) {
        result += ', ';
      }
    outputText += result;
    console.info('getSupportedPhotoFormats success, data is ' + outputText);
  } catch (error) {
    console.error('getSupportedPhotoFormats failed, errCode is', error);
}
```

#### on('photoChange')20+

on(type: 'photoChange', callback: Callback<PhotoAssetChangeInfos>): void

注册'photoChange'监听媒体资产，并通过callback方式返回资产变化结果，可以注册多个callback。

**需要权限**：ohos.permission.READ_IMAGEVIDEO

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 注册监听媒体资产，取值为'photoChange'。注册完成后，有资产发生变化时，通过callback返回变更信息。 |
| callback | Callback<PhotoAssetChangeInfos> | 是 | 返回变更的媒体资产信息PhotoAssetChangeInfos。 注意： 该接口可以注册多个不同的callback监听，off('photoChange')既可以关闭所有监听，也可以关闭指定callback监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[媒体库错误码](媒体库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 23800151 | The scenario parameter verification fails. Possible causes: 1. The type is not fixed at 'photoChange'; 2. The same callback is registered repeatedly. |
| 23800301 | Internal system error. You are advised to retry and check the logs. Possible causes: 1. The database is corrupted. 2. The file system is abnormal. 3. The IPC request timed out. |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](Functions.md#ZH-CN_TOPIC_0000002553362007__photoaccesshelpergetphotoaccesshelper)的示例使用。

```ets
import { dataSharePredicates } from '@kit.ArkData'

let onCallback1 = (changeData: photoAccessHelper.PhotoAssetChangeInfos) => {
    console.info('onCallback1 success, changData: ' + JSON.stringify(changeData));
  // file had changed, do something.
}
let onCallback2 = (changeData: photoAccessHelper.PhotoAssetChangeInfos) => {
    console.info('onCallback2 success, changData: ' + JSON.stringify(changeData));
  // file had changed, do something.
}

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper, context: Context){
  console.info('onPhotoChangeDemo.');

  try {
    // 注册onCallback1监听。
    phAccessHelper.on('photoChange', onCallback1);
    // 注册onCallback2监听。
    phAccessHelper.on('photoChange', onCallback2);
  } catch (error) {
    console.error('onPhotoChangeDemo failed, errCode is', error);
  }
```

#### off('photoChange')20+

off(type: 'photoChange', callback?: Callback<PhotoAssetChangeInfos>): void

取消对'photoChange'媒体资产的监听。存在多个callback监听时，可以取消指定注册的callback监听；不指定callback时取消所有监听。

**需要权限**：ohos.permission.READ_IMAGEVIDEO

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消监听媒体资产，取值为'photoChange'。取消监听后，有资产发生变化时，不再通过callback返回变更信息。 |
| callback | Callback<PhotoAssetChangeInfos> | 否 | 取消on('photoChange')注册时指定的callback监听；不填时，则取消对'photoChange'的所有监听。 注意： 取消注册的callback后，有资产发生变化时，不会进入此回调。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[媒体库错误码](媒体库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 23800151 | The scenario parameter verification fails. Possible causes: 1. The type is not fixed at 'photoChange'; 2. The same callback is unregistered repeatedly. |
| 23800301 | Internal system error. You are advised to retry and check the logs. Possible causes: 1. The database is corrupted. 2. The file system is abnormal. 3. The IPC request timed out. |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](Functions.md#ZH-CN_TOPIC_0000002553362007__photoaccesshelpergetphotoaccesshelper)的示例使用。

```ets
import { dataSharePredicates } from '@kit.ArkData'

let onCallback1 = (changeData: photoAccessHelper.PhotoAssetChangeInfos) => {
    console.info('onCallback1 success, changData: ' + JSON.stringify(changeData));
  // file had changed, do something.
}
let onCallback2 = (changeData: photoAccessHelper.PhotoAssetChangeInfos) => {
    console.info('onCallback2 success, changData: ' + JSON.stringify(changeData));
  // file had changed, do something.
}

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper, context: Context){
  console.info('offPhotoChangeDemo.');

  try {
    // 注册onCallback1监听。
    phAccessHelper.on('photoChange', onCallback1);
    // 注册onCallback2监听。
    phAccessHelper.on('photoChange', onCallback2);

    // 关闭onCallback1监听，onCallback2继续监听。
    phAccessHelper.off('photoChange', onCallback1);
  } catch (error) {
    console.error('offPhotoChangeDemo failed, errCode is', error);
  }
```

#### on('photoAlbumChange')20+

on(type: 'photoAlbumChange', callback: Callback<AlbumChangeInfos>): void

注册'photoAlbumChange'监听相册，并通过callback方式返回相册变化结果，可以注册多个callback。

**需要权限**：ohos.permission.READ_IMAGEVIDEO

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 注册监听相册，取值为'photoAlbumChange'。注册完成后，有相册发生变化时，通过callback返回变更信息。 |
| callback | Callback<AlbumChangeInfos> | 是 | 返回变更的相册信息AlbumChangeInfos。 注意： 该接口可以注册多个不同的callback监听，off('photoAlbumChange')既可以关闭所有监听，也可以关闭指定callback监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[媒体库错误码](媒体库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 23800151 | The scenario parameter verification fails. Possible causes: 1. The type is not fixed at 'photoAlbumChange'; 2. The same callback is registered repeatedly. |
| 23800301 | Internal system error. You are advised to retry and check the logs. Possible causes: 1. The database is corrupted. 2. The file system is abnormal. 3. The IPC request timed out. |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](Functions.md#ZH-CN_TOPIC_0000002553362007__photoaccesshelpergetphotoaccesshelper)的示例使用。

```ets
import { dataSharePredicates } from '@kit.ArkData'

let onCallback1 = (changeData: photoAccessHelper.AlbumChangeInfos) => {
    console.info('onCallback1 success, changData: ' + JSON.stringify(changeData));
  // file had changed, do something.
}
let onCallback2 = (changeData: photoAccessHelper.AlbumChangeInfos) => {
    console.info('onCallback2 success, changData: ' + JSON.stringify(changeData));
  // file had changed, do something.
}

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper, context: Context){
  console.info('onPhotoAlbumChangeDemo.');

  try {
    // 注册onCallback1监听。
    phAccessHelper.on('photoAlbumChange', onCallback1);
    // 注册onCallback2监听。
    phAccessHelper.on('photoAlbumChange', onCallback2);
  } catch (error) {
    console.error('onPhotoAlbumChangeDemo failed, errCode is', error);
  }
```

#### off('photoAlbumChange')20+

off(type: 'photoAlbumChange', callback?: Callback<AlbumChangeInfos>): void

取消对'photoAlbumChange'相册的监听。存在多个callback监听时，可以取消指定注册的callback监听；不指定callback时取消所有监听。

**需要权限**：ohos.permission.READ_IMAGEVIDEO

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消监听相册，取值为'photoAlbumChange'。取消监听后，有相册发生变化时，不再通过callback返回变更信息。 |
| callback | Callback<AlbumChangeInfos> | 否 | 取消on('photoAlbumChange')注册时指定的callback监听；不填时，则取消对'photoAlbumChange'的所有监听。 注意： 取消注册的callback后，有相册发生变化时，不会进入此回调。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[媒体库错误码](媒体库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 23800151 | The scenario parameter verification fails. Possible causes: 1. The type is not fixed at 'photoAlbumChange'; 2. The same callback is unregistered repeatedly. |
| 23800301 | Internal system error. You are advised to retry and check the logs. Possible causes: 1. The database is corrupted. 2. The file system is abnormal. 3. The IPC request timed out. |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](Functions.md#ZH-CN_TOPIC_0000002553362007__photoaccesshelpergetphotoaccesshelper)的示例使用。

```ets
import { dataSharePredicates } from '@kit.ArkData'

let onCallback1 = (changeData: photoAccessHelper.AlbumChangeInfos) => {
    console.info('onCallback1 success, changData: ' + JSON.stringify(changeData));
  // file had changed, do something.
}
let onCallback2 = (changeData: photoAccessHelper.AlbumChangeInfos) => {
    console.info('onCallback2 success, changData: ' + JSON.stringify(changeData));
  // file had changed, do something.
}

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper, context: Context){
  console.info('onPhotoAlbumChangeDemo.');

  try {
    // 注册onCallback1监听。
    phAccessHelper.on('photoAlbumChange', onCallback1);
    // 注册onCallback2监听。
    phAccessHelper.on('photoAlbumChange', onCallback2);

    // 关闭onCallback1监听，onCallback2继续监听。
    phAccessHelper.off('photoAlbumChange', onCallback1);
  } catch (error) {
    console.error('onPhotoAlbumChangeDemo failed, errCode is', error);
  }
```

#### getPhotoPickerComponentDefaultAlbumName20+

getPhotoPickerComponentDefaultAlbumName(): Promise<string>

应用使用PhotoPickerComponent组件选择照片时，支持调用API获取组件默认显示相册的相册名字符串。跟随当前系统语言，支持返回当前语言的相册名。使用Promise异步回调。

**元服务API**： 从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回默认相册的相册名。 |

**错误码：**

以下错误码的详细介绍请参见[文件管理错误码](文件管理错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 23800301 | Internal system error. It is recommended to retry and check the logs. Possible causes: 1. The IPC request timed out. 2. system running error. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import {photoAccessHelper} from '@kit.MediaLibraryKit';

async function example(context: Context) {
  console.info('getPhotoPickerComponentDefaultAlbumNameDemo');
  let phAccessHelper: photoAccessHelper.PhotoAccessHelper = photoAccessHelper.getPhotoAccessHelper(context);

  phAccessHelper.getPhotoPickerComponentDefaultAlbumName().then((defaultAlbumName) => {
    console.info('getPhotoPickerComponentDefaultAlbumName success, defaultAlbumName is ' + defaultAlbumName);
  }).catch((err: BusinessError) => {
    console.error(`getPhotoPickerComponentDefaultAlbumName failed with error: ${err.code}, ${err.message}`);
  });
}
```

#### createDeleteRequest(deprecated)

createDeleteRequest(uriList: Array<string>, callback: AsyncCallback<void>): void

创建一个弹出框来删除照片，删除的文件进入到回收站，使用callback方式返回结果。


从API version 10开始支持，从API version 11开始废弃。建议使用[MediaAssetChangeRequest.deleteAssets](Class (MediaAssetChangeRequest).md#ZH-CN_TOPIC_0000002553202049__deleteassets11-1)替代。

**需要权限**：ohos.permission.WRITE_IMAGEVIDEO

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uriList | Array<string> | 是 | 待删除的媒体文件uri数组，最大删除数量300。 |
| callback | AsyncCallback<void> | 是 | callback返回void。 |

**错误码：**

接口抛出错误码的详细介绍请参见[通用错误码](通用错误码.md)和[文件管理错误码](文件管理错误码.md)。

错误码13900012，请参考[开发准备](../../guides/开发准备（媒体库）.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 13900012 | Permission denied. |
| 13900020 | Invalid argument. |
| 14000011 | System inner fail. |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](Functions.md#ZH-CN_TOPIC_0000002553362007__photoaccesshelpergetphotoaccesshelper)的示例使用。

```ets
import { dataSharePredicates } from '@kit.ArkData';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('createDeleteRequestDemo');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOptions: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  try {
    let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOptions);
    let asset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
    if (asset === undefined) {
      console.error('asset not exist');
      return;
    }
    phAccessHelper.createDeleteRequest([asset.uri], (err) => {
      if (err === undefined) {
        console.info('createDeleteRequest successfully');
      } else {
        console.error(`createDeleteRequest failed with error: ${err.code}, ${err.message}`);
      }
    });
  } catch (err) {
    console.error(`fetch failed, error: ${err.code}, ${err.message}`);
  }
```

#### createDeleteRequest(deprecated)

createDeleteRequest(uriList: Array<string>): Promise<void>

创建一个弹出框来删除照片，删除的文件进入到回收站，使用Promise方式返回结果。


从API version 10开始支持，从API version 11开始废弃。建议使用[MediaAssetChangeRequest.deleteAssets](Class (MediaAssetChangeRequest).md#ZH-CN_TOPIC_0000002553202049__deleteassets11-1)替代。

**需要权限**：ohos.permission.WRITE_IMAGEVIDEO

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uriList | Array<string> | 是 | 待删除的媒体文件uri数组，最大删除数量300。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，返回void。 |

**错误码：**

接口抛出错误码的详细介绍请参见[通用错误码](通用错误码.md)和[文件管理错误码](文件管理错误码.md)。

错误码13900012，请参考[开发准备](../../guides/开发准备（媒体库）.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 13900012 | Permission denied. |
| 13900020 | Invalid argument. |
| 14000011 | System inner fail. |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](Functions.md#ZH-CN_TOPIC_0000002553362007__photoaccesshelpergetphotoaccesshelper)的示例使用。

```ets
import { dataSharePredicates } from '@kit.ArkData';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('createDeleteRequestDemo');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOptions: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  try {
    let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOptions);
    let asset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
    if (asset === undefined) {
      console.error('asset not exist');
      return;
    }
    await phAccessHelper.createDeleteRequest([asset.uri]);
    console.info('createDeleteRequest successfully');
  } catch (err) {
    console.error(`createDeleteRequest failed with error: ${err.code}, ${err.message}`);
  }
```

#### getRecentPhotoInfo20+

getRecentPhotoInfo(options?: RecentPhotoOptions): Promise<RecentPhotoInfo>

应用使用RecentPhotoComponent组件查看最近图片时，支持调用API获取最近图片信息。使用Promise异步回调。

**元服务API**： 从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | RecentPhotoOptions | 否 | 最近图片配置选项参数。若无此参数，则取按照创建时间排序的最新一张图片。 该参数在配置的情况下，需与RecentPhotoComponent组件中的options配置相同才可以查到一样的图片，否则可能存在接口能查到最近图片，组件没查到最近图片的情况。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<RecentPhotoInfo> | Promise对象，返回最近图片信息。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { photoAccessHelper, PhotoSource, RecentPhotoOptions} from '@kit.MediaLibraryKit';

async function example(context: Context) {
  console.info('getRecentPhotoInfoDemo');
  let phAccessHelper: photoAccessHelper.PhotoAccessHelper = photoAccessHelper.getPhotoAccessHelper(context);
  let recentPhotoOptions: RecentPhotoOptions = {
    period: 60 * 60,
    MIMEType: photoAccessHelper.PhotoViewMIMETypes.IMAGE_VIDEO_TYPE,
    photoSource: PhotoSource.ALL
  }

  phAccessHelper.getRecentPhotoInfo(recentPhotoOptions).then((recentPhotoInfo) => {
    console.info('getRecentPhotoInfo success, recentPhotoInfo is ' + JSON.stringify(recentPhotoInfo));
  }).catch((err: BusinessError) => {
    console.error(`getRecentPhotoInfo failed with error: ${err.code}, ${err.message}`);
  });
}
```

#### getAlbumIdByLpath22+

getAlbumIdByLpath(lpath: string): Promise<number>

根据相册的虚拟路径获取媒体库相册的ID。使用Promise异步回调。

该接口仅支持以下相册：相机相册('/DCIM/Camera')、截图相册('/Pictures/Screenshots')和屏幕录制相册('/Pictures/Screenrecords')。

​**模型约束**： 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| lpath | string | 是 | 相册的虚拟路径，lpath长度不能超过255个字符。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回相册lpath对应的媒体库相册的ID。 |

**错误码：**

接口抛出错误码的详细介绍请参见[媒体库错误码](媒体库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 23800151 | The lpath is invalid, such as null, undefined and empty. |
| 23800301 | Internal system error. You are advised to retry and check the logs. Possible causes: 1. The database is corrupted. 2. The file system is abnormal. 3. The IPC request timed out. |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](Functions.md#ZH-CN_TOPIC_0000002553362007__photoaccesshelpergetphotoaccesshelper)的示例使用。

```ets
async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('getAlbumIdByLpath');

  try {
      let albumId: number = await phAccessHelper.getAlbumIdByLpath('testLpath');
      console.info('requestFile:: albumId: ', albumId);

      console.info('getAlbumIdByLpath completed.');
      console.info(`albumId : ${albumId}`);
    } catch (err) {
      console.error(`getAlbumIdByLpath failed: ${err.code}, ${err.message}`);
    }
```

**onSinglePhotoChange23+**

onSinglePhotoChange(asset: PhotoAsset, callback: Callback<PhotoAssetChangeInfos>): void

注册对普通单个资产变化的监听。使用callback异步回调。

需要权限：ohos.permission.READ_IMAGEVIDEO

系统能力：SystemCapability.FileManagement.PhotoAccessHelper.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| asset | PhotoAsset | 是 | 注册单个监听的媒体资产。注册完成后，有资产发生变化时，通过callback返回变更信息。 |
| callback | Callback<PhotoAssetChangeInfos> | 是 | 返回变更的媒体资产信息PhotoAssetChangeInfos。 注意： 该接口可以注册多个不同的callback监听。 |

错误码：

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[媒体库错误码](媒体库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 23800151 | The scenario parameter verification fails. Possible causes: 1. The same callback is registered repeatedly. 2. Asset has been removed. 3. The uri of the asset invalid. |
| 23800301 | Internal system error. You are advised to retry and check the logs. Possible causes: 1. The database is corrupted. 2. The file system is abnormal. 3. The IPC request timed out. |

示例：

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](Functions.md#ZH-CN_TOPIC_0000002553362007__photoaccesshelpergetphotoaccesshelper)的示例使用。

```ets
import { dataSharePredicates } from '@kit.ArkData'

let onCallback1 = (changeData: photoAccessHelper.PhotoAssetChangeInfos) => {
    console.info('onCallback1 success, changeData: ' + JSON.stringify(changeData));
  // 触发回调时，具体的操作。
}
let onCallback2 = (changeData: photoAccessHelper.PhotoAssetChangeInfos) => {
    console.info('onCallback2 success, changeData: ' + JSON.stringify(changeData));
  // 触发回调时，具体的操作。
}

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper, context: Context){
  console.info('onSinglePhotoChangeDemo.');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOptions: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  try {
    let albumFetchResult: photoAccessHelper.FetchResult<photoAccessHelper.Album> = await phAccessHelper.getAlbums(photoAccessHelper.AlbumType.USER, photoAccessHelper.AlbumSubtype.USER_GENERIC);
    let album: photoAccessHelper.Album = await albumFetchResult.getFirstObject();
    let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await album.getAssets(fetchOptions);
    let asset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();

    if (albumFetchResult.isAfterLast()) {
      console.error('lack of album to be moved into');
      return;
    }
    // 注册onCallback1监听。
    phAccessHelper.onSinglePhotoChange(asset, onCallback1);
    // 注册onCallback2监听。
    phAccessHelper.onSinglePhotoChange(asset, onCallback2);
  } catch (error) {
    console.error('onSinglePhotoChangeDemo failed, errCode is', error);
  }
```

**offSinglePhotoChange23+**

offSinglePhotoChange(asset?: PhotoAsset, callback?: Callback<PhotoAssetChangeInfos>): void;

取消单个资产的监听。具体规则如下：1）不携带参数时，取消所有单个资产监听。2）携带asset，不携带callback时，取消该asset下所有callback监听。3）携带asset和callback时，仅取消指定callback监听。

需要权限：ohos.permission.READ_IMAGEVIDEO

系统能力：SystemCapability.FileManagement.PhotoAccessHelper.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| asset | PhotoAsset | 否 | 取消监听资产。取消asset资产监听后,当asset发生变化时,不再通过callback返回变更信息。不携带时，取消注册过的所有单个资产监听。 |
| callback | Callback<PhotoAssetChangeInfos> | 否 | 用于取消订阅的回调。不携带时，取消asset参数下所有callback。 |

错误码：

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[媒体库错误码](媒体库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 23800151 | The scenario parameter verification fails. Possible causes: 1. The same callback is unregistered repeatedly. 2. The uri of the asset invalid. |
| 23800301 | Internal system error. You are advised to retry and check the logs.Possible causes: 1. The database is corrupted. 2. The file system is abnormal. 3. The IPC request timed out. |

示例：

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](Functions.md#ZH-CN_TOPIC_0000002553362007__photoaccesshelpergetphotoaccesshelper)的示例使用。

```ets
import { dataSharePredicates } from '@kit.ArkData'

let onCallback1 = (changeData: photoAccessHelper.PhotoAssetChangeInfos) => {
    console.info('onCallback1 success, changeData: ' + JSON.stringify(changeData));
  // 触发回调时，具体的操作。
}
let onCallback2 = (changeData: photoAccessHelper.PhotoAssetChangeInfos) => {
    console.info('onCallback2 success, changeData: ' + JSON.stringify(changeData));
  // 触发回调时，具体的操作。
}
let onCallback3 = (changeData: photoAccessHelper.PhotoAssetChangeInfos) => {
    console.info('onCallback3 success, changeData: ' + JSON.stringify(changeData));
  // 触发回调时，具体的操作。
}

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper, context: Context){
  console.info('onSinglePhotoChangeDemo.');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOptions: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  try {
    let albumFetchResult: photoAccessHelper.FetchResult<photoAccessHelper.Album> = await phAccessHelper.getAlbums(photoAccessHelper.AlbumType.USER, photoAccessHelper.AlbumSubtype.USER_GENERIC);
    let album: photoAccessHelper.Album = await albumFetchResult.getFirstObject();
    let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await album.getAssets(fetchOptions);
    let asset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();

    if (albumFetchResult.isAfterLast()) {
      console.error('lack of album to be moved into');
      return;
    }
    // 注册onCallback1监听。
    phAccessHelper.onSinglePhotoChange(asset, onCallback1);
    // 注册onCallback2监听。
    phAccessHelper.onSinglePhotoChange(asset, onCallback2);
    // 注册onCallback3监听。
    phAccessHelper.onSinglePhotoChange(asset, onCallback3);

    // 解注册onCallback1监听。
    phAccessHelper.offSinglePhotoChange(asset, onCallback1);
    // 解注册asset下所有callback。
    phAccessHelper.offSinglePhotoChange(asset);
    // 解注册所有singlePhotoAssetChange类型监听。
    phAccessHelper.offSinglePhotoChange();
  } catch (error) {
    console.error('offSinglePhotoChangeDemo failed, errCode is', error);
  }
```

**onSinglePhotoAlbumChange23+**

onSinglePhotoAlbumChange(album: Album, callback: Callback<AlbumChangeInfos>): void;

注册对普通单个相册变化的监听。使用callback异步回调。

需要权限：ohos.permission.READ_IMAGEVIDEO

系统能力：SystemCapability.FileManagement.PhotoAccessHelper.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| album | Album | 是 | 注册单个监听的媒体相册。注册完成后，当该相册发生变化时，通过callback返回变更信息。 |
| callback | Callback<AlbumChangeInfos> | 是 | 返回变更的媒体相册信息PhotoAssetChangeInfos。 注意： 该接口可以注册多个不同的callback监听。 |

错误码：

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[媒体库错误码](媒体库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 23800151 | The scenario parameter verification fails. Possible causes: 1. The same callback is registered repeatedly. 2. Album has been removed. 3. The uri of the a invalid. |
| 23800301 | - Internal system error. You are advised to retry and check the logs. Possible causes: 1. The database is corrupted. 2. The file system is abnormal. 3. The IPC request timed out. |

示例：

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](Functions.md#ZH-CN_TOPIC_0000002553362007__photoaccesshelpergetphotoaccesshelper)的示例使用。

```ets
import { dataSharePredicates } from '@kit.ArkData'

let onCallback1 = (changeData: photoAccessHelper.AlbumChangeInfos) => {
    console.info('onCallback1 success, changeData: ' + JSON.stringify(changeData));
  // 触发回调时，具体的操作。
}
let onCallback2 = (changeData: photoAccessHelper.AlbumChangeInfos) => {
    console.info('onCallback2 success, changeData: ' + JSON.stringify(changeData));
  // 触发回调时，具体的操作。
}

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper, context: Context){
  console.info('onSinglePhotoAlbumChangeDemo.');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOptions: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  try {
    let albumFetchResult: photoAccessHelper.FetchResult<photoAccessHelper.Album> = await phAccessHelper.getAlbums(photoAccessHelper.AlbumType.USER, photoAccessHelper.AlbumSubtype.USER_GENERIC);
    let album: photoAccessHelper.Album = await albumFetchResult.getFirstObject();

    if (albumFetchResult.isAfterLast()) {
      console.error('lack of album to be moved into');
      return;
    }
    // 注册onCallback1监听。
    phAccessHelper.onSinglePhotoAlbumChange(album, onCallback1);
    // 注册onCallback2监听。
    phAccessHelper.onSinglePhotoAlbumChange(album, onCallback2);
  } catch (error) {
    console.error('onSinglePhotoAlbumChangeDemo failed, errCode is', error);
  }
```

**offSinglePhotoAlbumChange23+**

offSinglePhotoAlbumChange(album?: Album, callback?: Callback<AlbumChangeInfos>): void

取消对单个相册的监听，具体规则如下：1）不携带任何参数时，取消所有单个相册监听。2）携带album，不携带callback时，取消该album下所有callback监听。3）携带album和callback时，仅取消指定callback监听。

需要权限：ohos.permission.READ_IMAGEVIDEO

系统能力：SystemCapability.FileManagement.PhotoAccessHelper.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| album | Album | 否 | 取消监听相册。取消监听后,有相册发生变化时,不再通过callback返回变更信息。 |
| callback | Callback<AlbumChangeInfos> | 否 | 用于取消订阅的回调。不携带时，取消album参数下所有callback。 |

错误码：

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[媒体库错误码](媒体库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 23800151 | The scenario parameter verification fails. Possible causes： 1. The same callback is unregistered repeatedly. 2. The uri of the album invalid. |
| 23800301 | Internal system error. You are advised to retry and check the logs. Possible causes: 1. The database is corrupted. 2. The file system is abnormal. 3. The IPC request timed out. |

示例：

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](Functions.md#ZH-CN_TOPIC_0000002553362007__photoaccesshelpergetphotoaccesshelper)的示例使用。

```ets
import { dataSharePredicates } from '@kit.ArkData'

let onCallback1 = (changeData: photoAccessHelper.AlbumChangeInfos) => {
    console.info('onCallback1 success, changeData: ' + JSON.stringify(changeData));
  // 触发回调时，具体的操作。
}
let onCallback2 = (changeData: photoAccessHelper.AlbumChangeInfos) => {
    console.info('onCallback2 success, changeData: ' + JSON.stringify(changeData));
  // 触发回调时，具体的操作。
}
let onCallback3 = (changeData: photoAccessHelper.AlbumChangeInfos) => {
    console.info('onCallback3 success, changeData: ' + JSON.stringify(changeData));
  // 触发回调时，具体的操作。
}

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper, context: Context){
  console.info('onSinglePhotoChangeDemo.');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOptions: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  try {
    let albumFetchResult: photoAccessHelper.FetchResult<photoAccessHelper.Album> = await phAccessHelper.getAlbums(photoAccessHelper.AlbumType.USER, photoAccessHelper.AlbumSubtype.USER_GENERIC);
    let album: photoAccessHelper.Album = await albumFetchResult.getFirstObject();

    if (albumFetchResult.isAfterLast()) {
      console.error('lack of album to be moved into');
      return;
    }
    // 注册onCallback1监听。
    phAccessHelper.onSinglePhotoAlbumChange(album, onCallback1);
    // 注册onCallback2监听。
    phAccessHelper.onSinglePhotoAlbumChange(album, onCallback2);
    // 注册onCallback3监听。
    phAccessHelper.onSinglePhotoAlbumChange(album, onCallback3);

    // 解注册onCallback1监听。
    phAccessHelper.offSinglePhotoAlbumChange(album, onCallback1);
    // 解注册album下所有callback。
    phAccessHelper.offSinglePhotoAlbumChange(album);
    // 解注册所有singlePhotoAlbumChange类型监听。
    phAccessHelper.offSinglePhotoAlbumChange();
  } catch (error) {
    console.error('offSinglePhotoAlbumChangeDemo failed, errCode is', error);
  }
```