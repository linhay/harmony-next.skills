# @ohos.file.storageStatistics (应用空间统计)

该模块提供空间查询相关的常用功能：包括对内外卡的空间查询、对应用分类数据统计的查询、对应用数据的查询等。

本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { storageStatistics } from '@kit.CoreFileKit';
```

#### storageStatistics.getCurrentBundleStats9+

getCurrentBundleStats(): Promise<BundleStats>

应用异步获取当前应用存储空间大小（单位为Byte），使用Promise异步回调。

**系统能力**：SystemCapability.FileManagement.StorageService.SpatialStatistics

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<BundleStats> | Promise对象，返回指定卷上的应用存储空间大小（单位为Byte）。 |

**错误码：**

以下错误码的详细介绍请参见[文件管理错误码]([文件管理错误码](../../errors/文件管理错误码.md).md)和[通用错误码]([通用错误码](../../errors/通用错误码.md).md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The input parameter is invalid. Possible causes: Mandatory parameters are left unspecified. |
| 13600001 | IPC error. |
| 13900042 | Unknown error. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
storageStatistics.getCurrentBundleStats().then((BundleStats: storageStatistics.BundleStats) => {
  console.info("getCurrentBundleStats successfully:" + JSON.stringify(BundleStats));
}).catch((err: BusinessError) => {
  console.error("getCurrentBundleStats failed with error:"+ JSON.stringify(err));
});
```

#### storageStatistics.getCurrentBundleStats9+

getCurrentBundleStats(callback: AsyncCallback<BundleStats>): void

应用异步获取当前应用存储空间大小（单位为Byte），使用callback异步回调。

**系统能力**：SystemCapability.FileManagement.StorageService.SpatialStatistics

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<BundleStats> | 是 | 获取指定卷上的应用存储空间大小之后的回调。 |

**错误码：**

以下错误码的详细介绍请参见[文件管理错误码](文件管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The input parameter is invalid. Possible causes: Mandatory parameters are left unspecified. |
| 13600001 | IPC error. |
| 13900042 | Unknown error. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
storageStatistics.getCurrentBundleStats((error: BusinessError, bundleStats: storageStatistics.BundleStats) => {
  if (error) {
    console.error("getCurrentBundleStats failed with error:" + JSON.stringify(error));
  } else {
    // do something
    console.info("getCurrentBundleStats successfully:" + JSON.stringify(bundleStats));
  }
});
```

#### storageStatistics.getTotalSize15+

getTotalSize(): Promise<number>

获取内置存储的总空间大小（单位为Byte），使用Promise异步回调。

**系统能力**：SystemCapability.FileManagement.StorageService.SpatialStatistics

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回内置存储的总空间大小（单位为Byte）。 |

**错误码：**

以下错误码的详细介绍请参见[文件管理错误码](文件管理错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 13600001 | IPC error. |
| 13900042 | Unknown error. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
storageStatistics.getTotalSize().then((number: number) => {
  console.info("getTotalSize successfully:" + JSON.stringify(number));
}).catch((err: BusinessError) => {
  console.error("getTotalSize failed with error:"+ JSON.stringify(err));
});
```

#### storageStatistics.getTotalSize15+

getTotalSize(callback: AsyncCallback<number>): void

获取内置存储的总空间大小（单位为Byte），使用callback异步回调。

**系统能力**：SystemCapability.FileManagement.StorageService.SpatialStatistics

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<number> | 是 | 获取内置存储的总空间大小之后的回调。 |

**错误码：**

以下错误码的详细介绍请参见[文件管理错误码](文件管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The input parameter is invalid. Possible causes: Mandatory parameters are left unspecified. |
| 13600001 | IPC error. |
| 13900042 | Unknown error. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
storageStatistics.getTotalSize((error: BusinessError, number: number) => {
  if (error) {
    console.error("getTotalSize failed with error:" + JSON.stringify(error));
  } else {
    // do something
    console.info("getTotalSize successfully:" + number);
  }
});
```

#### storageStatistics.getTotalSizeSync15+

getTotalSizeSync(): number

同步获取内置存储的总空间大小（单位为Byte）。

**系统能力**：SystemCapability.FileManagement.StorageService.SpatialStatistics

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回内置存储的总空间大小（单位为Byte）。 |

**错误码：**

以下错误码的详细介绍请参见[文件管理错误码](文件管理错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 13600001 | IPC error. |
| 13900042 | Unknown error. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
try {
  let number = storageStatistics.getTotalSizeSync();
  console.info("getTotalSizeSync successfully:" + JSON.stringify(number));
} catch (err) {
  let error: BusinessError = err as BusinessError;
  console.error("getTotalSizeSync failed with error:" + JSON.stringify(error));
}
```

#### storageStatistics.getFreeSize15+

getFreeSize(): Promise<number>

获取内置存储的可用空间大小（单位为Byte），使用Promise异步回调。

**系统能力**：SystemCapability.FileManagement.StorageService.SpatialStatistics

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回内置存储的可用空间大小（单位为Byte）。 |

**错误码：**

以下错误码的详细介绍请参见[文件管理错误码](文件管理错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 13600001 | IPC error. |
| 13900042 | Unknown error. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
storageStatistics.getFreeSize().then((number: number) => {
  console.info("getFreeSize successfully:" + JSON.stringify(number));
}).catch((err: BusinessError) => {
  console.error("getFreeSize failed with error:" + JSON.stringify(err));
});
```

#### storageStatistics.getFreeSize15+

getFreeSize(callback: AsyncCallback<number>): void

获取内置存储的可用空间大小（单位为Byte），使用callback异步回调。

**系统能力**：SystemCapability.FileManagement.StorageService.SpatialStatistics

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<number> | 是 | 获取内置存储的可用空间大小之后的回调。 |

**错误码：**

以下错误码的详细介绍请参见[文件管理错误码](文件管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The input parameter is invalid. Possible causes: Mandatory parameters are left unspecified. |
| 13600001 | IPC error. |
| 13900042 | Unknown error. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
storageStatistics.getFreeSize((error: BusinessError, number: number) => {
  if (error) {
    console.error("getFreeSize failed with error:" + JSON.stringify(error));
  } else {
    // do something
    console.info("getFreeSize successfully:" + number);
  }
});
```

#### storageStatistics.getFreeSizeSync15+

getFreeSizeSync(): number

同步获取内置存储的可用空间大小（单位为Byte）。

**系统能力**：SystemCapability.FileManagement.StorageService.SpatialStatistics

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回内置存储的可用空间大小（单位为Byte）。 |

**错误码：**

以下错误码的详细介绍请参见[文件管理错误码](文件管理错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 13600001 | IPC error. |
| 13900042 | Unknown error. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
try {
  let number = storageStatistics.getFreeSizeSync();
  console.info("getFreeSizeSync successfully:" + JSON.stringify(number));
} catch (err) {
  let error: BusinessError = err as BusinessError;
  console.error("getFreeSizeSync failed with error:" + JSON.stringify(error));
}
```

#### BundleStats9+

**系统能力**：SystemCapability.FileManagement.StorageService.SpatialStatistics

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| appSize | number | 否 | 否 | 应用安装文件大小（单位为Byte）。 |
| cacheSize | number | 否 | 否 | 应用缓存文件大小（单位为Byte）。 |
| dataSize | number | 否 | 否 | 应用文件存储大小（除应用安装文件）（单位为Byte）。 |