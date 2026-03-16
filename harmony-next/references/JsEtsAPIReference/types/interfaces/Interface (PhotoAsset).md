# Interface (PhotoAsset)

提供封装文件属性的方法。

本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { photoAccessHelper } from '@kit.MediaLibraryKit';
```

#### 属性

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

名称类型只读可选说明uristring是否

媒体文件资源uri（如：file://media/Photo/1/IMG_datetime_0001/displayName.jpg），详情参见用户文件uri介绍中的[媒体文件uri](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/user-file-uri-intro#媒体文件uri)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

photoType[PhotoType](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529445919__phototype)是否

媒体文件类型。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

displayNamestring是否

显示文件名，包含后缀名。字符串长度为1~255。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

#### get

get(member: string): MemberType

获取PhotoAsset成员参数的值。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

参数名类型必填说明memberstring是成员参数名称，在get时，除了'uri'、'media_type'、'subtype'和'display_name'四个属性之外，其他的属性都需要在fetchColumns中填入需要获取的[PhotoKeys](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529445919__photokeys)，例如：get title属性fetchColumns: ['title']。

**返回值：**

类型说明[MemberType](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497605956__membertype)获取PhotoAsset成员参数的值。

**错误码：**

接口抛出错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[文件管理错误码](../../errors/文件管理错误码.md)。

错误码ID错误信息13900020Invalid argument.14000014The provided member must be a property name of PhotoKey.

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](../../topics/misc/Functions.md#ZH-CN_TOPIC_0000002529445911__photoaccesshelpergetphotoaccesshelper)的示例使用。

```ets
import { dataSharePredicates } from '@kit.ArkData';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('photoAssetGetDemo');
  try {
    let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
    let fetchOption: photoAccessHelper.FetchOptions = {
      fetchColumns: ['title'],
      predicates: predicates
    };
    let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOption);
    let photoAsset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
    let title: photoAccessHelper.PhotoKeys = photoAccessHelper.PhotoKeys.TITLE;
    let photoAssetTitle: photoAccessHelper.MemberType = photoAsset.get(title.toString());
    console.info('photoAsset Get photoAssetTitle = ', photoAssetTitle);
  } catch (err) {
    console.error(`release failed. error: ${err.code}, ${err.message}`);
  }
}
```

#### set

set(member: string, value: string): void

设置PhotoAsset成员参数。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

参数名类型必填说明memberstring是成员参数名称例如：[PhotoKeys](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529445919__photokeys).TITLE。字符串长度为1~255。valuestring是

设置成员参数名称，只能修改[PhotoKeys](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529445919__photokeys).TITLE的值。title的参数规格为：

- 不应包含扩展名。

- 文件名字符串长度为1~255（资产文件名为标题+扩展名）。

- 不允许出现的非法英文字符，包括：. \ / : * ? " ' ` < > | { } [ ]

**错误码：**

接口抛出错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[文件管理错误码](../../errors/文件管理错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.13900020Invalid argument.14000014The provided member must be a property name of PhotoKey.

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](../../topics/misc/Functions.md#ZH-CN_TOPIC_0000002529445911__photoaccesshelpergetphotoaccesshelper)的示例使用。

```ets
import { dataSharePredicates } from '@kit.ArkData';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('photoAssetSetDemo');
  try {
    let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
    let fetchOption: photoAccessHelper.FetchOptions = {
      fetchColumns: ['title'],
      predicates: predicates
    };
    let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOption);
    let photoAsset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
    let title: string = photoAccessHelper.PhotoKeys.TITLE.toString();
    photoAsset.set(title, 'newTitle');
  } catch (err) {
    console.error(`release failed. error: ${err.code}, ${err.message}`);
  }
}
```

#### commitModify

commitModify(callback: AsyncCallback<void>): void

修改文件的元数据。使用callback异步回调。

**需要权限**：ohos.permission.WRITE_IMAGEVIDEO

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

参数名类型必填说明callbackAsyncCallback<void>是回调函数。当修改文件元数据成功，err为undefined，否则为错误对象。

**错误码：**

接口抛出错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[文件管理错误码](../../errors/文件管理错误码.md)。

错误码14000001，请参考 [PhotoKeys](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529445919__photokeys)获取有关文件名的格式和长度要求。

错误码13900012，请参考[开发准备](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/photoaccesshelper-preparation)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.201Permission denied.13900020Invalid argument.14000001Invalid display name.14000011System inner fail.

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](../../topics/misc/Functions.md#ZH-CN_TOPIC_0000002529445911__photoaccesshelpergetphotoaccesshelper)的示例使用。

```ets
import { dataSharePredicates } from '@kit.ArkData';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('commitModifyDemo');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOption: photoAccessHelper.FetchOptions = {
    fetchColumns: ['title'],
    predicates: predicates
  };
  let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOption);
  let photoAsset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
  let title: string = photoAccessHelper.PhotoKeys.TITLE.toString();
  let photoAssetTitle: photoAccessHelper.MemberType = photoAsset.get(title);
  console.info('photoAsset get photoAssetTitle = ', photoAssetTitle);
  photoAsset.set(title, 'newTitle2');
  photoAsset.commitModify((err) => {
    if (err === undefined) {
      let newPhotoAssetTitle: photoAccessHelper.MemberType = photoAsset.get(title);
      console.info('photoAsset get newPhotoAssetTitle = ', newPhotoAssetTitle);
    } else {
      console.error(`commitModify failed, error: ${err.code}, ${err.message}`);
    }
  });
}
```

#### commitModify

commitModify(): Promise<void>

修改文件的元数据。使用Promise异步回调。

**需要权限**：ohos.permission.WRITE_IMAGEVIDEO

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**返回值：**

类型说明Promise<void>Promise对象，无返回结果。

**错误码：**

接口抛出错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[文件管理错误码](../../errors/文件管理错误码.md)。

错误码14000001，请参考 [PhotoKeys](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529445919__photokeys)获取有关文件名的格式和长度要求。

在API version 13及之前的版本，无相关权限返回错误码13900012；从API version 14开始，无相关权限返回错误码201。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.201Permission denied.13900020Invalid argument.14000001Invalid display name.14000011System inner fail.

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](../../topics/misc/Functions.md#ZH-CN_TOPIC_0000002529445911__photoaccesshelpergetphotoaccesshelper)的示例使用。

```ets
import { dataSharePredicates } from '@kit.ArkData';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('commitModifyDemo');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOption: photoAccessHelper.FetchOptions = {
    fetchColumns: ['title'],
    predicates: predicates
  };
  let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOption);
  let photoAsset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
  if (photoAsset === undefined) {
    console.error('commitModifyPromise photoAsset is undefined');
    return;
  }
  let title: string = photoAccessHelper.PhotoKeys.TITLE.toString();
  let photoAssetTitle: photoAccessHelper.MemberType = photoAsset.get(title);
  console.info('photoAsset get photoAssetTitle = ', photoAssetTitle);
  photoAsset.set(title, 'newTitle3');
  try {
    await photoAsset.commitModify();
    let newPhotoAssetTitle: photoAccessHelper.MemberType = photoAsset.get(title);
    console.info('photoAsset get newPhotoAssetTitle = ', newPhotoAssetTitle);
  } catch (err) {
    console.error(`release failed. error: ${err.code}, ${err.message}`);
  }
}
```

#### close(deprecated)

close(fd: number, callback: AsyncCallback<void>): void

关闭当前文件。使用callback异步回调。

从API version 10开始支持，从API version 11开始废弃，建议使用[fs.close](../../modules/ohos/@ohos.file.fs (文件管理).md#ZH-CN_TOPIC_0000002529445221__fsclose-1)替代。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

参数名类型必填说明fdnumber是文件描述符。callbackAsyncCallback<void>是回调函数。当关闭当前文件成功，err为undefined，否则为错误对象。

**错误码：**

接口抛出错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[文件管理错误码](../../errors/文件管理错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.13900020Invalid argument.14000011System inner fail.

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](../../topics/misc/Functions.md#ZH-CN_TOPIC_0000002529445911__photoaccesshelpergetphotoaccesshelper)的示例使用。

```ets
import { dataSharePredicates } from '@kit.ArkData';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('closeDemo');
  try {
    let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
    let fetchOption: photoAccessHelper.FetchOptions = {
      fetchColumns: [],
      predicates: predicates
    };
    let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOption);
    let photoAsset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
    let fd: number = await photoAsset.open('rw');
    console.info('file fd', fd);
    photoAsset.close(fd, (err) => {
      if (err === undefined) {
        console.info('asset close succeed.');
      } else {
        console.error(`close failed, error: ${err.code}, ${err.message}`);
      }
    });
  } catch (err) {
    console.error(`close failed, error: ${err.code}, ${err.message}`);
  }
}
```

#### close(deprecated)

close(fd: number): Promise<void>

关闭当前文件。使用Promise异步回调。

从API version 10开始支持，从API version 11开始废弃，建议使用[fs.close](../../modules/ohos/@ohos.file.fs (文件管理).md#ZH-CN_TOPIC_0000002529445221__fsclose)替代。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

参数名类型必填说明fdnumber是文件描述符。

**返回值：**

类型说明Promise<void>Promise对象，无返回结果。

**错误码：**

接口抛出错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[文件管理错误码](../../errors/文件管理错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.13900020Invalid argument.14000011System inner fail.

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](../../topics/misc/Functions.md#ZH-CN_TOPIC_0000002529445911__photoaccesshelpergetphotoaccesshelper)的示例使用。

```ets
import { dataSharePredicates } from '@kit.ArkData';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('closeDemo');
  try {
    let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
    let fetchOption: photoAccessHelper.FetchOptions = {
      fetchColumns: [],
      predicates: predicates
    };
    let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOption);
    let asset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
    let fd = await asset.open('rw');
    console.info('file fd', fd);
    await asset.close(fd);
    console.info('asset close succeed.');
  } catch (err) {
    console.error(`close failed, error: ${err.code}, ${err.message}`);
  }
}
```

#### getThumbnail

getThumbnail(callback: AsyncCallback<image.PixelMap>): void

获取文件的缩略图。使用callback异步回调。

**需要权限**：ohos.permission.READ_IMAGEVIDEO

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

参数名类型必填说明callbackAsyncCallback<[image.PixelMap](Interface (PixelMap).md)>是回调函数。当获取文件的缩略图成功，err为undefined，data为缩略图的PixelMap；否则为错误对象。

**错误码：**

接口抛出错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[文件管理错误码](../../errors/文件管理错误码.md)。

错误码13900012，请参考[开发准备](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/photoaccesshelper-preparation)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.13900012Permission denied.13900020Invalid argument.14000011System inner fail.

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](../../topics/misc/Functions.md#ZH-CN_TOPIC_0000002529445911__photoaccesshelpergetphotoaccesshelper)的示例使用。

```ets
import { dataSharePredicates } from '@kit.ArkData';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('getThumbnailDemo');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOption: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOption);
  let asset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
  console.info('asset displayName = ', asset.displayName);
  asset.getThumbnail((err, pixelMap) => {
    if (err === undefined) {
      console.info('getThumbnail successful ' + pixelMap);
    } else {
      console.error(`getThumbnail fail with error: ${err.code}, ${err.message}`);
    }
  });
}
```

#### getThumbnail

getThumbnail(size: image.Size, callback: AsyncCallback<image.PixelMap>): void

获取文件的缩略图，传入缩略图尺寸。使用callback异步回调。

**需要权限**：ohos.permission.READ_IMAGEVIDEO

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

参数名类型必填说明size[image.Size](Interfaces (其他).md#ZH-CN_TOPIC_0000002497445866__size)是缩略图尺寸。callbackAsyncCallback<[image.PixelMap](Interface (PixelMap).md)>是回调函数。当获取文件的缩略图成功，err为undefined，data为缩略图的PixelMap；否则为错误对象。

**错误码：**

接口抛出错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[文件管理错误码](../../errors/文件管理错误码.md)。

错误码13900012，请参考[开发准备](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/photoaccesshelper-preparation)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.13900012Permission denied.13900020Invalid argument.14000011System inner fail.

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](../../topics/misc/Functions.md#ZH-CN_TOPIC_0000002529445911__photoaccesshelpergetphotoaccesshelper)的示例使用。

```ets
import { dataSharePredicates } from '@kit.ArkData';
import { image } from '@kit.ImageKit';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('getThumbnailDemo');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOption: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  let size: image.Size = { width: 720, height: 720 };
  try {
    let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOption);
    let asset = await fetchResult.getFirstObject();
    console.info('asset displayName = ', asset.displayName);
    asset.getThumbnail(size, (err, pixelMap) => {
      if (err === undefined) {
        console.info('getThumbnail successful ' + pixelMap);
      } else {
        console.error(`getThumbnail fail with error: ${err.code}, ${err.message}`);
      }
    });
  } catch (error) {
    console.error(`Error fetching assets: ${error.message}`);
  }
}
```

#### getThumbnail

getThumbnail(size?: image.Size): Promise<image.PixelMap>

获取文件的缩略图，传入缩略图尺寸。使用Promise异步回调。

**需要权限**：ohos.permission.READ_IMAGEVIDEO

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

参数名类型必填说明size[image.Size](Interfaces (其他).md#ZH-CN_TOPIC_0000002497445866__size)否缩略图尺寸。

**返回值：**

类型说明Promise<[image.PixelMap](Interface (PixelMap).md)>Promise对象，返回缩略图的PixelMap。

**错误码：**

接口抛出错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[文件管理错误码](../../errors/文件管理错误码.md)。

错误码13900012，请参考[开发准备](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/photoaccesshelper-preparation)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.13900012Permission denied.13900020Invalid argument.14000011System inner fail.

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](../../topics/misc/Functions.md#ZH-CN_TOPIC_0000002529445911__photoaccesshelpergetphotoaccesshelper)的示例使用。

```ets
import { dataSharePredicates } from '@kit.ArkData';
import { image } from '@kit.ImageKit';
import { BusinessError } from '@kit.BasicServicesKit';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('getThumbnailDemo');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOption: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  let size: image.Size = { width: 720, height: 720 };
  let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOption);
  let asset = await fetchResult.getFirstObject();
  console.info('asset displayName = ', asset.displayName);
  asset.getThumbnail(size).then((pixelMap) => {
    console.info('getThumbnail successful ' + pixelMap);
  }).catch((err: BusinessError) => {
    console.error(`getThumbnail fail with error: ${err.code}, ${err.message}`);
  });
}
```

#### clone14+

clone(title: string): Promise<PhotoAsset>

克隆资产，可设置文件名，但不支持修改文件类型。使用promise异步回调。

**需要权限**：ohos.permission.WRITE_IMAGEVIDEO

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

参数名类型必填说明titlestring是

克隆后资产的标题。参数规格为：

- 不应包含扩展名。

- 文件名字符串长度为1~255（资产文件名为标题+扩展名）。

- 不允许出现的非法英文字符，包括：. \ / : * ? " ' ` < > | { } [ ]

**返回值：**

类型说明Promise<[PhotoAsset](Interface (PhotoAsset).md)>Promise对象，返回[PhotoAsset](Interface (PhotoAsset).md)。

**错误码：**

接口抛出错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[文件管理错误码](../../errors/文件管理错误码.md)。

错误码ID错误信息201Permission denied.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.14000011Internal system error. It is recommended to retry and check the logs.Possible causes: 1. Database corrupted; 2. The file system is abnormal; 3. The IPC request timed out.

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](../../topics/misc/Functions.md#ZH-CN_TOPIC_0000002529445911__photoaccesshelpergetphotoaccesshelper)的示例使用。

```ets
import { dataSharePredicates } from '@kit.ArkData';
import { systemDateTime } from '@kit.BasicServicesKit';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOptions: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  try {
    let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOptions);
    let photoAsset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
    let title: string = systemDateTime.getTime().toString();
    let newAsset: photoAccessHelper.PhotoAsset = await photoAsset.clone(title);
    console.info('get new asset successfully');
  } catch (error) {
    console.error(`failed to get new asset. message =  ${error.code}, ${error.message}`);
  }
}
```

#### getReadOnlyFd(deprecated)

getReadOnlyFd(callback: AsyncCallback<number>): void

以只读方式打开当前文件。使用callback异步回调。

使用完毕后调用close释放文件描述符。

从API version 10开始支持，从API version 11开始废弃，建议使用[fs.open](../../modules/ohos/@ohos.file.fs (文件管理).md#ZH-CN_TOPIC_0000002529445221__fsopen-1)替代。

**需要权限**：ohos.permission.READ_IMAGEVIDEO

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

参数名类型必填说明callbackAsyncCallback<number>是回调函数。当打开当前文件成功，err为undefined，data为文件描述符；否则为错误对象。

**错误码：**

接口抛出错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[文件管理错误码](../../errors/文件管理错误码.md)。

在API version 13及之前的版本，无相关权限返回错误码13900012；从API version 14开始，无相关权限返回错误码201。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.201Permission denied.13900020Invalid argument.14000011System inner fail.

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](../../topics/misc/Functions.md#ZH-CN_TOPIC_0000002529445911__photoaccesshelpergetphotoaccesshelper)的示例使用。

```ets
import { dataSharePredicates } from '@kit.ArkData';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('getReadOnlyFdDemo');
  // 需要保证设备中存在可读取图片视频文件。
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOptions: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  let assetResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOptions);
  let photoAsset: photoAccessHelper.PhotoAsset = await assetResult.getFirstObject();
  photoAsset.getReadOnlyFd((err, fd) => {
    if (fd !== undefined) {
      console.info('File fd' + fd);
      photoAsset.close(fd);
    } else {
      console.error(`getReadOnlyFd err: ${err.code}, ${err.message}`);
    }
  });
}
```

#### getReadOnlyFd(deprecated)

getReadOnlyFd(): Promise<number>

以只读方式打开当前文件。使用promise异步回调。

返回的文件描述符在使用完毕后需要调用close进行释放。

从API version 10开始支持，从API version 11开始废弃，建议使用[fs.open](../../modules/ohos/@ohos.file.fs (文件管理).md#ZH-CN_TOPIC_0000002529445221__fsopen)替代。

**需要权限**：ohos.permission.READ_IMAGEVIDEO

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**返回值：**

类型说明Promise<number>Promise对象，返回文件描述符。

**错误码：**

接口抛出错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[文件管理错误码](../../errors/文件管理错误码.md)。

在API version 13及之前的版本，无相关权限返回错误码13900012；从API version 14开始，无相关权限返回错误码201。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.201Permission denied.13900020Invalid argument.14000011System inner fail.

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](../../topics/misc/Functions.md#ZH-CN_TOPIC_0000002529445911__photoaccesshelpergetphotoaccesshelper)的示例使用。

```ets
import { dataSharePredicates } from '@kit.ArkData';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('getReadOnlyFdDemo');
  try {
    // 需要保证设备中存在可读取图片视频文件。
    let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
    let fetchOptions: photoAccessHelper.FetchOptions = {
      fetchColumns: [],
      predicates: predicates
    };
    let assetResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOptions);
    let photoAsset: photoAccessHelper.PhotoAsset = await assetResult.getFirstObject();
    if (photoAsset === undefined) {
      console.error('photoAsset is undefined');
      return;
    }
    let fd: number = await photoAsset.getReadOnlyFd();
    if (fd !== undefined) {
      console.info('File fd' + fd);
      photoAsset.close(fd);
    } else {
      console.error('getReadOnlyFd fail');
    }
  } catch (err) {
    console.error(`getReadOnlyFd demo err: ${err.code}, ${err.message}`);
  }
}
```