# Interface (FetchResult)

文件检索结果集。

本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { photoAccessHelper } from '@kit.MediaLibraryKit';
```

#### getCount

getCount(): number

获取文件检索结果中的文件总数。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**返回值：**

类型说明number检索到的文件总数。

**错误码：**

接口抛出错误码的详细介绍请参见[通用错误码](通用错误码.md)和[文件管理错误码](文件管理错误码.md)。

错误码ID错误信息13900020Invalid argument.14000011System inner fail.

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](Functions.md#ZH-CN_TOPIC_0000002529445911__photoaccesshelpergetphotoaccesshelper)的示例使用。

```ets
import { dataSharePredicates } from '@kit.ArkData';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('getCountDemo');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOption: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOption);
  let fetchCount = fetchResult.getCount();
  console.info('fetchCount = ', fetchCount);
}
```

#### isAfterLast

isAfterLast(): boolean

检查结果集是否指向最后一行。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**返回值：**

类型说明boolean当读到最后一条记录后，后续没有记录返回true，否则返回false。

**错误码：**

接口抛出错误码的详细介绍请参见[通用错误码](通用错误码.md)和[文件管理错误码](文件管理错误码.md)。

错误码ID错误信息13900020Invalid argument.14000011System inner fail.

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](Functions.md#ZH-CN_TOPIC_0000002529445911__photoaccesshelpergetphotoaccesshelper)的示例使用。

```ets
import { dataSharePredicates } from '@kit.ArkData';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOption: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOption);
  let fetchCount = fetchResult.getCount();
  console.info('count:' + fetchCount);
  let photoAsset: photoAccessHelper.PhotoAsset = await fetchResult.getLastObject();
  if (fetchResult.isAfterLast()) {
    console.info('photoAsset isAfterLast displayName = ', photoAsset.displayName);
  } else {
    console.info('photoAsset not isAfterLast.');
  }
}
```

#### close

close(): void

释放FetchResult实例并使其失效，无法再调用其他方法。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**错误码：**

接口抛出错误码的详细介绍请参见[通用错误码](通用错误码.md)和[文件管理错误码](文件管理错误码.md)。

错误码ID错误信息13900020Invalid argument.14000011System inner fail.

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](Functions.md#ZH-CN_TOPIC_0000002529445911__photoaccesshelpergetphotoaccesshelper)的示例使用。

```ets
import { dataSharePredicates } from '@kit.ArkData';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('fetchResultCloseDemo');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOption: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  try {
    let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOption);
    fetchResult.close();
    console.info('close succeed.');
  } catch (err) {
    console.error(`close fail. error: ${err.code}, ${err.message}`);
  }
}
```

#### getFirstObject

getFirstObject(callback: AsyncCallback<T>): void

获取文件检索结果中的第一个文件资产。使用callback异步回调。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

参数名类型必填说明callbackAsyncCallback<T>是回调函数。当获取结果集中的第一个文件资产成功，err为undefined，data为具体检索结果；否则为错误对象。

**错误码：**

接口抛出错误码的详细介绍请参见[通用错误码](通用错误码.md)和[文件管理错误码](文件管理错误码.md)。

错误码ID错误信息13900020Invalid argument.14000011System inner fail.

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](Functions.md#ZH-CN_TOPIC_0000002529445911__photoaccesshelpergetphotoaccesshelper)的示例使用。

```ets
import { dataSharePredicates } from '@kit.ArkData';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('getFirstObjectDemo');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOption: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOption);
  fetchResult.getFirstObject((err, photoAsset) => {
    if (photoAsset !== undefined) {
      console.info('photoAsset displayName: ', photoAsset.displayName);
    } else {
      console.error(`photoAsset failed with err:${err.code}, ${err.message}`);
    }
  });
}
```

#### getFirstObject

getFirstObject(): Promise<T>

获取文件检索结果中的第一个文件资产。使用Promise异步回调。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**返回值：**

类型说明Promise<T>Promise对象，返回结果集中第一个对象。

**错误码：**

接口抛出错误码的详细介绍请参见[通用错误码](通用错误码.md)和[文件管理错误码](文件管理错误码.md)。

错误码ID错误信息13900020Invalid argument.14000011System inner fail.

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](Functions.md#ZH-CN_TOPIC_0000002529445911__photoaccesshelpergetphotoaccesshelper)的示例使用。

```ets
import { dataSharePredicates } from '@kit.ArkData';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('getFirstObjectDemo');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOption: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOption);
  let photoAsset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
  console.info('photoAsset displayName: ', photoAsset.displayName);
}
```

#### getNextObject

getNextObject(callback: AsyncCallback<T>): void

获取文件检索结果中的下一个文件资产。使用callback异步回调。

在调用此方法之前，必须使用[isAfterLast()](#ZH-CN_TOPIC_0000002529445915__isafterlast)来检查当前位置是否为最后一行。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

参数名类型必填说明callbackAsyncCallback<T>是回调函数。当获取结果集中的下一个文件资产成功，err为undefined，data为具体检索结果；否则为错误对象。

**错误码：**

接口抛出错误码的详细介绍请参见[通用错误码](通用错误码.md)和[文件管理错误码](文件管理错误码.md)。

错误码ID错误信息13900020Invalid argument.14000011System inner fail.

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](Functions.md#ZH-CN_TOPIC_0000002529445911__photoaccesshelpergetphotoaccesshelper)的示例使用。

```ets
import { dataSharePredicates } from '@kit.ArkData';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('getNextObjectDemo');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOption: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOption);
  await fetchResult.getFirstObject();
  if (!fetchResult.isAfterLast()) {
    fetchResult.getNextObject((err, photoAsset) => {
      if (photoAsset !== undefined) {
        console.info('photoAsset displayName: ', photoAsset.displayName);
      } else {
        console.error(`photoAsset failed with err: ${err.code}, ${err.message}`);
      }
    });
  }
}
```

#### getNextObject

getNextObject(): Promise<T>

获取文件检索结果中的下一个文件资产。使用Promise异步回调。

在调用此方法之前，必须使用[isAfterLast()](#ZH-CN_TOPIC_0000002529445915__isafterlast)来检查当前位置是否为最后一行。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**返回值：**

类型说明Promise<T>Promise对象，返回结果集中下一个对象。

**错误码：**

接口抛出错误码的详细介绍请参见[通用错误码](通用错误码.md)和[文件管理错误码](文件管理错误码.md)。

错误码ID错误信息13900020Invalid argument.14000011System inner fail.

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](Functions.md#ZH-CN_TOPIC_0000002529445911__photoaccesshelpergetphotoaccesshelper)的示例使用。

```ets
import { dataSharePredicates } from '@kit.ArkData';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('getNextObjectDemo');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOption: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOption);
  await fetchResult.getFirstObject();
  if (!fetchResult.isAfterLast()) {
    let photoAsset: photoAccessHelper.PhotoAsset = await fetchResult.getNextObject();
    console.info('photoAsset displayName: ', photoAsset.displayName);
  }
}
```

#### getLastObject

getLastObject(callback: AsyncCallback<T>): void

获取文件检索结果中的最后一个文件资产。使用callback异步回调。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

参数名类型必填说明callbackAsyncCallback<T>是回调函数。当获取结果集中的最后一个文件资产成功，err为undefined，data为具体检索结果；否则为错误对象。

**错误码：**

接口抛出错误码的详细介绍请参见[通用错误码](通用错误码.md)和[文件管理错误码](文件管理错误码.md)。

错误码ID错误信息13900020Invalid argument.14000011System inner fail.

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](Functions.md#ZH-CN_TOPIC_0000002529445911__photoaccesshelpergetphotoaccesshelper)的示例使用。

```ets
import { dataSharePredicates } from '@kit.ArkData';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('getLastObjectDemo');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOption: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOption);
  fetchResult.getLastObject((err, photoAsset) => {
    if (photoAsset !== undefined) {
      console.info('photoAsset displayName: ', photoAsset.displayName);
    } else {
      console.error(`photoAsset failed with err: ${err.code}, ${err.message}`);
    }
  });
}
```

#### getLastObject

getLastObject(): Promise<T>

获取文件检索结果中的最后一个文件资产。使用Promise异步回调。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**返回值：**

类型说明Promise<T>Promise对象，返回结果集中的最后一个对象。

**错误码：**

接口抛出错误码的详细介绍请参见[通用错误码](通用错误码.md)和[文件管理错误码](文件管理错误码.md)。

错误码ID错误信息13900020Invalid argument.14000011System inner fail.

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](Functions.md#ZH-CN_TOPIC_0000002529445911__photoaccesshelpergetphotoaccesshelper)的示例使用。

```ets
import { dataSharePredicates } from '@kit.ArkData';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('getLastObjectDemo');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOption: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOption);
  let photoAsset: photoAccessHelper.PhotoAsset = await fetchResult.getLastObject();
  console.info('photoAsset displayName: ', photoAsset.displayName);
}
```

#### getObjectByPosition

getObjectByPosition(index: number, callback: AsyncCallback<T>): void

获取文件检索结果中具有指定索引的文件资产。使用callback异步回调。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

参数名类型必填说明indexnumber是要获取的文件的索引，从0开始。callbackAsyncCallback<T>是回调函数。当获取结果集中指定索引的文件资产成功，err为undefined，data为具体检索结果；否则为错误对象。

**错误码：**

接口抛出错误码的详细介绍请参见[通用错误码](通用错误码.md)和[文件管理错误码](文件管理错误码.md)。

错误码ID错误信息13900020Invalid argument.14000011System inner fail.

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](Functions.md#ZH-CN_TOPIC_0000002529445911__photoaccesshelpergetphotoaccesshelper)的示例使用。

```ets
import { dataSharePredicates } from '@kit.ArkData';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('getObjectByPositionDemo');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOption: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOption);
  fetchResult.getObjectByPosition(0, (err, photoAsset) => {
    if (photoAsset !== undefined) {
      console.info('photoAsset displayName: ', photoAsset.displayName);
    } else {
      console.error(`photoAsset failed with err: ${err.code}, ${err.message}`);
    }
  });
}
```

#### getObjectByPosition

getObjectByPosition(index: number): Promise<T>

获取文件检索结果中指定索引的文件资产。使用Promise异步回调。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

参数名类型必填说明indexnumber是要获取的文件的索引，从0开始。

**返回值：**

类型说明Promise<T>Promise对象，返回结果集中指定索引的一个对象。

**错误码：**

接口抛出错误码的详细介绍请参见[通用错误码](通用错误码.md)和[文件管理错误码](文件管理错误码.md)。

错误码ID错误信息13900020Invalid argument.14000011System inner fail.

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](Functions.md#ZH-CN_TOPIC_0000002529445911__photoaccesshelpergetphotoaccesshelper)的示例使用。

```ets
import { dataSharePredicates } from '@kit.ArkData';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('getObjectByPositionDemo');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOption: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOption);
  if (fetchResult === undefined) {
    console.error('fetchResult is undefined');
    return;
  }
  let photoAsset: photoAccessHelper.PhotoAsset = await fetchResult.getObjectByPosition(0);
  console.info('photoAsset displayName: ', photoAsset.displayName);
}
```

#### getAllObjects

getAllObjects(callback: AsyncCallback<Array<T>>): void

获取文件检索结果中的所有文件资产。使用callback异步回调。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

参数名类型必填说明callbackAsyncCallback<Array<T>>是回调函数。当获取结果集中的所有文件资产成功，err为undefined，data为具体检索结果；否则为错误对象。

**错误码：**

接口抛出错误码的详细介绍请参见[通用错误码](通用错误码.md)和[文件管理错误码](文件管理错误码.md)。

错误码ID错误信息13900020Invalid argument.14000011System inner fail.

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](Functions.md#ZH-CN_TOPIC_0000002529445911__photoaccesshelpergetphotoaccesshelper)的示例使用。

```ets
import { dataSharePredicates } from '@kit.ArkData';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('getAllObjectDemo');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOption: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOption);
  fetchResult.getAllObjects((err, photoAssetList) => {
    if (photoAssetList !== undefined) {
      console.info('photoAssetList length: ', photoAssetList.length);
    } else {
      console.error(`photoAssetList failed with err:${err.code}, ${err.message}`);
    }
  });
}
```

#### getAllObjects

getAllObjects(): Promise<Array<T>>

获取文件检索结果中的所有文件资产。使用Promise异步回调。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**返回值：**

类型说明Promise<Array<T>>Promise对象，返回所有文件资产的数组。

**错误码：**

接口抛出错误码的详细介绍请参见[通用错误码](通用错误码.md)和[文件管理错误码](文件管理错误码.md)。

错误码ID错误信息13900020Invalid argument.14000011System inner fail.

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](Functions.md#ZH-CN_TOPIC_0000002529445911__photoaccesshelpergetphotoaccesshelper)的示例使用。

```ets
import { dataSharePredicates } from '@kit.ArkData';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('getAllObjectDemo');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOption: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOption);
  let photoAssetList: Array<photoAccessHelper.PhotoAsset> = await fetchResult.getAllObjects();
  console.info('photoAssetList length: ', photoAssetList.length);
}
```