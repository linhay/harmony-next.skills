# AssetAccelerationExtensionAbility（资源加速ExtensionAbility）

本模块为资源包后台下载框架，为资源包后台下载提供关键的生命周期函数。在后台下载任务成功/失败/结束后支持调用相应的回调函数。本模块存在如下约束：

- AssetAccelerationExtensionAbility为轻量、独立的子进程，不允许唤醒主进程。
- assetDownloadManager提供的接口仅支持调用如下方法：

  - [assetDownloadManager.fetchManifestUrl](assetDownloadManager（资源包下载管理）.md#section81101219425)
  - [assetDownloadManager.removeAssetDownloadTask](assetDownloadManager（资源包下载管理）.md#section222042984419)
  - [assetDownloadManager.fetchAllAssetDownloadTasks](assetDownloadManager（资源包下载管理）.md#section918114094718)
  - [assetDownloadManager.removeAllAssetDownloadTasks](assetDownloadManager（资源包下载管理）.md#section2809432393)
  - [assetDownloadManager.fetchGroupAssetDownloadTasks](assetDownloadManager（资源包下载管理）.md#section93791016111111)
  - [assetDownloadManager.removeGroupAssetDownloadTasks](assetDownloadManager（资源包下载管理）.md#section641613495177)
  - [assetDownloadManager.limitDownloadTaskSpeed](assetDownloadManager（资源包下载管理）.md#section17279143882113)
  - [assetDownloadManager.reportDownloadProgress](assetDownloadManager（资源包下载管理）.md#section1492357144916)

**系统能力：**SystemCapability.GraphicsGame.AssetAcceleration

**模型约束：**此接口仅可在Stage模型下使用。

**起始版本：**5.1.0(18)

#### 导入模块

```ets
import { AssetAccelerationExtensionAbility } from '@kit.GraphicsAccelerateKit';
```

#### AssetAccelerationExtensionInfo

资源加速ExtensionAbility信息。

**系统能力：**SystemCapability.GraphicsGame.AssetAcceleration

**模型约束：**本模块接口仅可在Stage模型下使用。

**起始版本：**5.1.0(18)

**名称**

**类型**

****只读

可选

**说明**

maxBackgroundDownloadSize

number

是

否

最大的资源大小，单位：字节。只有当用户设备剩余存储空间大于maxBackgroundDownloadSize的三倍时，资源加速ExtensionAbility才会使能。

默认值：0。

domainList

string[]

是

否

域名白名单列表。域名不在此列表中的下载任务将直接失败。

#### ContentRequestType

type ContentRequestType = 'INSTALL' | 'UPDATE' | 'IDLE'

内容请求类型。

**系统能力：**SystemCapability.GraphicsGame.AssetAcceleration

**模型约束：**本模块接口仅可在Stage模型下使用。

**起始版本：**5.1.0(18)

类型

说明

'INSTALL'

安装。

'UPDATE'

更新。

'IDLE'

空闲。

#### AssetAccelerationExtensionAbility

资源加速扩展能力类。

**系统能力：**SystemCapability.GraphicsGame.AssetAcceleration

**模型约束：**此接口仅可在Stage模型下使用。

**起始版本：**5.1.0(18)

#### 属性

**系统能力：**SystemCapability.GraphicsGame.AssetAcceleration

**模型约束：**此接口仅可在Stage模型下使用。

**起始版本：**5.1.0(18)

**名称**

**类型**

****只读

可选

**说明**

context

[AssetAccelerationExtensionContext](AssetAccelerationExtensionContext（资源加速ExtensionContext）.md)

否

否

AssetAccelerationExtensionAbility的上下文环境，继承自[ExtensionContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-extensioncontext)。

#### onDownloadContentRequest

onDownloadContentRequest(requestType: ContentRequestType, manifestUrl: string, assetAccelerationExtensionInfo: AssetAccelerationExtensionInfo): Promise<assetDownloadManager.AssetDownloadConfig[]>

安装应用、更新应用、设备闲时，执行该方法，获取资源包下载任务列表。返回任务量不超过200条。使用Promise异步回调。

**系统能力：**SystemCapability.GraphicsGame.AssetAcceleration

**模型约束：**此接口仅可在Stage模型下使用。

**起始版本：**5.1.0(18)

**参数**：

**参数名**

**类型**

必填

**说明**

requestType

[ContentRequestType](#section48341532123214)

是

内容请求类型。

manifestUrl

string

是

资源包下载URL：

- 使用华为CDN托管资源，则此参数不为空。
- 使用三方CDN，则此参数为空。

默认值：空字符串。

assetAccelerationExtensionInfo

[AssetAccelerationExtensionInfo](#section14401125712)

是

资源加速ExtensionAbility信息。

**返回值：**

类型

说明

Promise<[assetDownloadManager.AssetDownloadConfig[]](assetDownloadManager（资源包下载管理）.md#section14401125712)>

Promise对象。返回资源包下载任务的配置信息列表，最多返回200条配置信息。

**示例**：

```ets
import { assetDownloadManager, AssetAccelerationExtensionAbility, AssetAccelerationExtensionInfo, ContentRequestType } from '@kit.GraphicsAccelerateKit';

// 此处以AssetAccelExtAbility继承AssetAccelerationExtensionAbility为例
export default class AssetAccelExtAbility extends AssetAccelerationExtensionAbility {
  async onDownloadContentRequest(requestType: ContentRequestType, manifestUrl: string,
    assetAccelerationExtensionInfo: AssetAccelerationExtensionInfo): Promise<assetDownloadManager.AssetDownloadConfig[]> {
    console.info('AssetAccelDemo', `onDownloadContentRequest enter, requestType: ${requestType}, manifestUrl: ${manifestUrl}.`);
    // 构造资源包下载配置信息，用于函数返回值。
    let downloadList: Array<assetDownloadManager.AssetDownloadConfig> = [];
    let download: assetDownloadManager.AssetDownloadConfig = {
        identifier: 'identifier',
        url: 'url',
        isEssential: false,
        groupId:'groupId',
        fileName: 'fileName'
      }
    downloadList.push(download);
    return downloadList;
  }
};
```

#### onDownloadWithAppControl

onDownloadWithAppControl(requestType: ContentRequestType, manifestUrl: string, assetAccelerationExtensionInfo: AssetAccelerationExtensionInfo): Promise<boolean>

安装应用、更新应用、设备闲时，执行该方法，触发extension协同下载，如果有资源包下载任务则返回true，否则返回false。使用Promise异步回调。

**系统能力：**SystemCapability.GraphicsGame.AssetAcceleration

**模型约束：**此接口仅可在Stage模型下使用。

**起始版本：**5.1.1(19)

**参数**：

**参数名**

**类型**

必填

**说明**

requestType

[ContentRequestType](#section48341532123214)

是

内容请求类型。

manifestUrl

string

是

资源包下载URL：

- 使用华为CDN托管资源，则此URL由系统提供。
- 使用三方CDN，则此参数为空。

默认值：空字符串。

assetAccelerationExtensionInfo

[AssetAccelerationExtensionInfo](#section14401125712)

是

资源加速ExtensionAbility信息。

**返回值：**

类型

说明

Promise<boolean>

Promise对象。

- 返回true：应用自身下载器已开启资源包下载。
- 返回false：应用自身下载器无下载任务。

**示例**：

```ets
import { AssetAccelerationExtensionAbility, AssetAccelerationExtensionInfo, ContentRequestType } from '@kit.GraphicsAccelerateKit';

// 此处以AssetAccelExtAbility继承AssetAccelerationExtensionAbility为例
export default class AssetAccelExtAbility extends AssetAccelerationExtensionAbility {
  async onDownloadWithAppControl(requestType: ContentRequestType, manifestUrl: string,
    assetAccelerationExtensionInfo: AssetAccelerationExtensionInfo): Promise<boolean> {
    console.info('AssetAccelDemo', `onDownloadWithAppControl enter, requestType: ${requestType}, manifestUrl: ${manifestUrl}.`);
    // 如果有下载任务，则调用应用自身下载器进行资源下载，并返回true，否则返回false。
    // ...
    let result = true;
    return result;
  }
};
```

#### onBackgroundDownloadSucceeded

onBackgroundDownloadSucceeded(downloadTask: assetDownloadManager.AssetDownloadTask, filePath: string): Promise<void>

在系统后台下载任务成功时，执行该方法，通知资源加速ExtensionAbility下载成功。使用Promise异步回调。

**系统能力：**SystemCapability.GraphicsGame.AssetAcceleration

**模型约束：**此接口仅可在Stage模型下使用。

**起始版本：**5.1.0(18)

**参数**：

**参数名**

**类型**

必填

**说明**

downloadTask

[assetDownloadManager.AssetDownloadTask](assetDownloadManager（资源包下载管理）.md#section1639510932819)

是

下载任务信息。

filePath

string

是

下载文件的本地沙箱地址。位于应用程序缓存(cache)目录下，示例路径如下：

```ets
/data/storage/el2/base/haps/entry/cache/asset_acceleration/1.8.2/xxx.bin
```

最大长度512个字符。

**返回值：**

类型

说明

Promise<void>

Promise对象。无返回结果的Promise对象。

**示例**：

```ets
import { assetDownloadManager, AssetAccelerationExtensionAbility } from '@kit.GraphicsAccelerateKit';

// 此处以AssetAccelExtAbility继承AssetAccelerationExtensionAbility为例
export default class AssetAccelExtAbility extends AssetAccelerationExtensionAbility {
  // 接收后台资源包下载成功消息的接口。
  async onBackgroundDownloadSucceeded(downloadTask: assetDownloadManager.AssetDownloadTask,
    filePath: string): Promise<void> {
    console.info('AssetAccelDemo', `onBackgroundDownloadSucceeded enter, taskId is ${downloadTask.taskId}, filePath = ${filePath}`);
    // 添加文件转移处理逻辑。
  }
};
```

#### onBackgroundDownloadFailed

onBackgroundDownloadFailed(downloadTask: assetDownloadManager.AssetDownloadTask, fault: assetDownloadManager.DownloadFault): Promise<void>

在系统后台下载任务失败时，执行该方法，通知资源加速ExtensionAbility下载失败。使用Promise异步回调。

**系统能力：**SystemCapability.GraphicsGame.AssetAcceleration

**模型约束：**此接口仅可在Stage模型下使用。

**起始版本：**5.1.0(18)

**参数**：

**参数名**

**类型**

必填

**说明**

downloadTask

[assetDownloadManager.AssetDownloadTask](assetDownloadManager（资源包下载管理）.md#section1639510932819)

是

下载任务信息。

fault

[assetDownloadManager.DownloadFault](assetDownloadManager（资源包下载管理）.md#section82071855806)

是

下载失败的原因。

**返回值：**

类型

说明

Promise<void>

Promise对象。无返回结果的Promise对象。

**示例**：

```ets
import { assetDownloadManager, AssetAccelerationExtensionAbility } from '@kit.GraphicsAccelerateKit';

// 此处以AssetAccelExtAbility继承AssetAccelerationExtensionAbility为例
export default class AssetAccelExtAbility extends AssetAccelerationExtensionAbility {
  // 接收后台资源包下载失败消息的接口。
  async onBackgroundDownloadFailed(downloadTask: assetDownloadManager.AssetDownloadTask,
    fault: assetDownloadManager.DownloadFault): Promise<void> {
    console.info('AssetAccelDemo', `onBackgroundDownloadFailed enter, download url: ${downloadTask.config.url}, err: ${fault}`);
    // 添加下载异常处理逻辑
  }
};
```

#### onExtensionWillTerminate

onExtensionWillTerminate(error?: BusinessError<void>): Promise<void>

在资源加速ExtensionAbility生命周期即将结束时、调度异常退出后，执行该方法，通知关闭资源包后台下载功能。建议在该方法中执行资源清理等操作，请避免耗时操作。使用Promise异步回调。

**系统能力：**SystemCapability.GraphicsGame.AssetAcceleration

**模型约束：**此接口仅可在Stage模型下使用。

**起始版本：**5.1.0(18)

**参数**：

**参数名**

**类型**

必填

**说明**

error

BusinessError<void>

否

错误码：

- 401：参数错误。
- 1016600005：资源加速ExtensionAbility方法执行超时。
- 1016600006：资源加速ExtensionAbility生命周期方法出现异常。
- 1016600094：服务异常。

**返回值：**

类型

说明

Promise<void>

Promise对象。无返回结果的Promise对象。

**示例**：

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { AssetAccelerationExtensionAbility } from '@kit.GraphicsAccelerateKit';

// 此处以AssetAccelExtAbility继承AssetAccelerationExtensionAbility为例
export default class AssetAccelExtAbility extends AssetAccelerationExtensionAbility {
  // 当AssetAccelerationExtensionAbility生命周期即将结束时、调度异常退出，会执行该回调
  async onExtensionWillTerminate(error?: BusinessError<void>): Promise<void> {
    // 添加资源清理等处理逻辑，请避免耗时操作
    if (!error) {
      console.info('AssetAccelDemo', `onExtensionWillTerminate enter, BusinessError is null;`);
      return;
    }
    console.error('AssetAccelDemo', `onExtensionWillTerminate enter, BusinessError：${error?.code}, msg: ${error?.message}`);
  }
};
```