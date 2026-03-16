# Class (PhotoViewPicker)

图库选择器对象用于支持选择图片、视频等用户场景。使用前，需先创建PhotoViewPicker实例。

本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { photoAccessHelper } from '@kit.MediaLibraryKit';
```

#### select

select(option?: PhotoSelectOptions) : Promise<PhotoSelectResult>

通过选择模式拉起photoPicker界面，用户可以选择一个或多个图片/视频。接口采用Promise异步返回形式，传入可选参数PhotoSelectOptions对象，返回PhotoSelectResult对象。

此接口返回的PhotoSelectResult对象中的photoUris具有永久授权，可通过调用接口[photoAccessHelper.getAssets](../interfaces/Interface (PhotoAccessHelper).md#ZH-CN_TOPIC_0000002529445917__getassets)去使用。具体操作请参考[媒体文件uri的使用方式](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/user-file-uri-intro#媒体文件uri的使用方式)。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

参数名类型必填说明option[PhotoSelectOptions](Classes (其他).md#ZH-CN_TOPIC_0000002497605950__photoselectoptions)否photoPicker选择选项，若无此参数，则默认选择媒体文件类型为图片和视频类型，默认选择媒体文件数量的最大值为50。

**返回值：**

类型说明Promise<[PhotoSelectResult](Classes (其他).md#ZH-CN_TOPIC_0000002497605950__photoselectresult)>Promise对象。返回photoPicker选择后的结果集

**错误码：**

接口抛出错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[文件管理错误码](../../errors/文件管理错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.13900042Unknown error.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function example01(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  try {
    let PhotoSelectOptions = new photoAccessHelper.PhotoSelectOptions();
    PhotoSelectOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE;
    PhotoSelectOptions.maxSelectNumber = 5;
    let photoPicker = new photoAccessHelper.PhotoViewPicker();
    photoPicker.select(PhotoSelectOptions).then((PhotoSelectResult: photoAccessHelper.PhotoSelectResult) => {
      console.info('PhotoViewPicker.select successfully, PhotoSelectResult uri: ' + JSON.stringify(PhotoSelectResult));
    }).catch((err: BusinessError) => {
      console.error(`PhotoViewPicker.select failed with err: ${err.code}, ${err.message}`);
    });
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    console.error(`PhotoViewPicker failed with err: ${err.code}, ${err.message}`);
  }
}
```

#### select

select(option: PhotoSelectOptions, callback: AsyncCallback<PhotoSelectResult>) : void

通过选择模式拉起photoPicker界面，用户可以选择一个或多个图片/视频。接口采用callback异步返回形式，传入参数PhotoSelectOptions对象，返回PhotoSelectResult对象。

此接口返回的PhotoSelectResult对象中的photoUris具有永久授权，可通过调用接口[photoAccessHelper.getAssets](../interfaces/Interface (PhotoAccessHelper).md#ZH-CN_TOPIC_0000002529445917__getassets)去使用。具体操作请参考[媒体文件uri的使用方式](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/user-file-uri-intro#媒体文件uri的使用方式)。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

参数名类型必填说明option[PhotoSelectOptions](Classes (其他).md#ZH-CN_TOPIC_0000002497605950__photoselectoptions)是photoPicker选择选项。callbackAsyncCallback<[PhotoSelectResult](Classes (其他).md#ZH-CN_TOPIC_0000002497605950__photoselectresult)>是callback 返回photoPicker选择后的结果集。

**错误码：**

接口抛出错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[文件管理错误码](../../errors/文件管理错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.13900042Unknown error.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function example02(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  try {
    let PhotoSelectOptions = new photoAccessHelper.PhotoSelectOptions();
    PhotoSelectOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE;
    PhotoSelectOptions.maxSelectNumber = 5;
    let photoPicker = new photoAccessHelper.PhotoViewPicker();
    photoPicker.select(PhotoSelectOptions, (err: BusinessError, PhotoSelectResult: photoAccessHelper.PhotoSelectResult) => {
      if (err) {
        console.error(`PhotoViewPicker.select failed with err: ${err.code}, ${err.message}`);
        return;
      }
      console.info('PhotoViewPicker.select successfully, PhotoSelectResult uri: ' + JSON.stringify(PhotoSelectResult));
    });
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    console.error(`PhotoViewPicker failed with err: ${err.code}, ${err.message}`);
  }
}
```

#### select

select(callback: AsyncCallback<PhotoSelectResult>) : void

通过选择模式拉起photoPicker界面，用户可以选择一个或多个图片/视频。接口采用callback异步返回形式，返回PhotoSelectResult对象。

此接口返回的PhotoSelectResult对象中的photoUris具有永久授权，可通过调用接口[photoAccessHelper.getAssets](../interfaces/Interface (PhotoAccessHelper).md#ZH-CN_TOPIC_0000002529445917__getassets)去使用。具体操作请参考[媒体文件uri的使用方式](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/user-file-uri-intro#媒体文件uri的使用方式)。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

参数名类型必填说明callbackAsyncCallback<[PhotoSelectResult](Classes (其他).md#ZH-CN_TOPIC_0000002497605950__photoselectresult)>是callback 返回photoPicker选择后的结果集。

**错误码：**

接口抛出错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[文件管理错误码](../../errors/文件管理错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.13900042Unknown error.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function example03(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  try {
    let photoPicker = new photoAccessHelper.PhotoViewPicker();
    photoPicker.select((err: BusinessError, PhotoSelectResult: photoAccessHelper.PhotoSelectResult) => {
      if (err) {
        console.error(`PhotoViewPicker.select failed with err: ${err.code}, ${err.message}`);
        return;
      }
      console.info('PhotoViewPicker.select successfully, PhotoSelectResult uri: ' + JSON.stringify(PhotoSelectResult));
    });
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    console.error(`PhotoViewPicker failed with err: ${err.code}, ${err.message}`);
  }
}
```