# assetDownloadManager（资源包下载管理）

本模块提供资源包下载管理能力。

**起始版本：**5.1.0(18)

#### 导入模块

```ets
import { assetDownloadManager } from '@kit.GraphicsAccelerateKit';
```

#### DownloadFault

资源包下载失败原因的枚举。

**系统能力：**SystemCapability.GraphicsGame.AssetAcceleration

**模型约束：**本模块接口仅可在Stage模型下使用。

**起始版本：**5.1.0(18)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| FAULT_FILE_ALREADY_EXISTS | 0 | 资源包已存在。 |
| FAULT_FILE_ERROR | 1 | 文件操作失败。 |
| FAULT_INSUFFICIENT_SPACE | 2 | 用户设备的内存空间不足。 |
| FAULT_DISCONNECT | 3 | 下载过程中链接丢失或断开。 |
| FAULT_TIMEOUT | 4 | 下载超时，例如HTTP 408请求超时、或504网关超时。 |
| FAULT_PROTOCOL | 5 | HTTP协议错误，例如HTTP 500服务器内部错误、或HTTP 400错误请求。 |
| FAULT_DNS | 6 | DNS域名解析错误，无法解析服务器地址。 |
| FAULT_SSL | 7 | SSL/TLS证书错误。 |
| FAULT_REDIRECT | 8 | 重定向错误，例如超出最大重定向限制或无效的重定向URL。 |
| FAULT_UNKNOWN | 9 | 未知错误。 |

#### State

资源包下载任务状态的枚举。

**系统能力：**SystemCapability.GraphicsGame.AssetAcceleration

**模型约束：**本模块接口仅可在Stage模型下使用。

**起始版本：**5.1.0(18)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CREATED | 0 | 已创建的下载任务。 |
| WAITING | 1 | 等待执行的下载任务。 |
| DOWNLOADING | 2 | 正在下载中的任务。 |
| PAUSED | 3 | 处于暂停状态的下载任务。 |
| FINISHED | 4 | 下载任务已完成。 |
| FAILED | 5 | 任务下载失败。 |

#### AssetDownloadConfig

资源包下载任务的配置信息。

**系统能力：**SystemCapability.GraphicsGame.AssetAcceleration

**模型约束：**本模块接口仅可在Stage模型下使用。

**起始版本：**5.1.0(18)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| identifier | string | 否 | 否 | 任务ID。下载任务的唯一标识。 最大长度64个字节。 |
| url | string | 否 | 否 | 当前下载任务URL，要求以http或者https开头，最大长度512个字节。 URL的域名需要符合域名白名单要求： - 三方CDN：请前往AppGallery Connect查看已配置的CDN域名白名单。具体操作步骤请参见创建下载任务。 - 华为CDN：域名白名单将基于资源包下载任务自动配置。 |
| isEssential | boolean | 否 | 否 | 是否为必需资源： - false：非必需资源。默认值。 - true：必需资源。 下载必需资源的优先级高于非必需资源。 |
| groupId | string | 否 | 是 | 组ID，用于标识资源的版本信息。 最大长度32个字节。 默认值：空字符串。 |
| fileName | string | 否 | 是 | 下载资源的文件名。若输入文件名，系统下载的临时文件将以该文件名命名，否则，文件名将以任务ID命名。 最大长度128个字节。 默认值：空字符串。 |
| begins | number | 否 | 是 | HTTP范围请求的起始字节位置。 默认值：0。 |
| ends | number | 否 | 是 | HTTP范围请求的结束字节位置。 默认值：0。 |
| userData | string | 否 | 是 | 允许用户自定义的扩展字段。 最大长度1024个字节。 默认值：空字符串。 |

#### AssetDownloadTask

资源包下载任务的信息。

**系统能力：**SystemCapability.GraphicsGame.AssetAcceleration

**模型约束：**本模块接口仅可在Stage模型下使用。

**起始版本：**5.1.0(18)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| config | AssetDownloadConfig | 是 | 否 | 资源包下载任务的配置信息，包含任务ID、URL、下载优先级等信息。 |
| taskId | string | 是 | 否 | 系统自动生成的任务ID，用于唯一标识下载任务。 最大长度36个字节。 |
| state | State | 是 | 否 | 资源包下载任务的状态。 |

#### DownloadProgressInfo

资源包下载任务的进度信息。

**系统能力：**SystemCapability.GraphicsGame.AssetAcceleration

**模型约束：**本模块接口仅可在Stage模型下使用。

**起始版本：**5.1.0(18)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| downloadTask | AssetDownloadTask | 是 | 否 | 资源包下载任务的信息。 |
| totalBytesWritten | number | 是 | 否 | 待下载的资源总大小，单位：字节。 默认值：0。 |
| totalExpectedBytes | number | 是 | 否 | 已下载的资源总大小，单位：字节。 默认值：0。 |

#### DownloadCompletedInfo

资源包下载任务的完成信息。

**系统能力：**SystemCapability.GraphicsGame.AssetAcceleration

**模型约束：**本模块接口仅可在Stage模型下使用。

**起始版本：**5.1.0(18)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| downloadTask | AssetDownloadTask | 是 | 否 | 资源包下载任务的信息。 |
| filePath | string | 是 | 否 | 下载文件的本地沙箱地址。 最大长度512个字节。 |

#### DownloadFailedInfo

资源包下载任务的失败信息。

**系统能力：**SystemCapability.GraphicsGame.AssetAcceleration

**模型约束：**本模块接口仅可在Stage模型下使用。

**起始版本：**5.1.0(18)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| downloadTask | AssetDownloadTask | 是 | 否 | 资源包下载任务的信息。 |
| fault | DownloadFault | 是 | 否 | 资源包下载失败的原因。 |

#### assetDownloadManager.on('progress')

on(type: 'progress', callback: Callback<DownloadProgressInfo[]>): void

订阅资源包下载进度事件。使用callback形式返回结果。

**系统能力：**SystemCapability.GraphicsGame.AssetAcceleration

**模型约束：**本模块接口仅可在Stage模型下使用。

**起始版本：**5.1.0(18)

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，固定为'progress'，表示资源包下载进度。 |
| callback | Callback<DownloadProgressInfo[]> | 是 | 回调函数。返回任务进度信息。 |

**错误码**：

错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[ArkTS API错误码]([ArkTS API错误码](../../errors/ArkTS API错误码.md).md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 1016600000 | The API call from an ExtensionAbility is not allowed. |
| 1016600094 | Task service ability error. |

**示例**：

```ets
import { assetDownloadManager } from '@kit.GraphicsAccelerateKit';

let onProgressCallback = (progressArray: assetDownloadManager.DownloadProgressInfo[]) => {
  console.info('AssetAccelDemo', `onProgressCallback progressArray length: ${progressArray.length}`);
  // 添加资源包下载进度处理逻辑。
};
// 订阅资源包下载进度事件。
assetDownloadManager.on("progress", onProgressCallback);
```

#### assetDownloadManager.off('progress')

off(type: 'progress', callback?: Callback<DownloadProgressInfo[]>): void

取消订阅资源包下载进度事件。使用callback形式返回结果。

**系统能力：**SystemCapability.GraphicsGame.AssetAcceleration

**模型约束：**本模块接口仅可在Stage模型下使用。

**起始版本：**5.1.0(18)

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消事件回调类型，固定为'progress'，表示资源包下载进度。 |
| callback | Callback<DownloadProgressInfo[]> | 否 | 需要取消监听的回调函数，需与订阅时传入的回调函数一致。若不填，则取消当前监听该事件的所有回调函数。 |

**错误码**：

错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 1016600000 | The API call from an ExtensionAbility is not allowed. |
| 1016600094 | Task service ability error. |

**示例**：

```ets
import { assetDownloadManager } from '@kit.GraphicsAccelerateKit';

let onProgressCallback = (progressArray: assetDownloadManager.DownloadProgressInfo[]) => {
  console.info('AssetAccelDemo', `onProgressCallback progressArray length: ${progressArray.length}`);
  // 添加资源包下载进度处理逻辑。
};
// 取消订阅资源包下载进度事件。
assetDownloadManager.off("progress", onProgressCallback);
```

#### assetDownloadManager.on('pause')

on(type: 'pause', callback: Callback<AssetDownloadTask>): void

订阅资源包下载暂停事件。使用callback形式返回结果。

**系统能力：**SystemCapability.GraphicsGame.AssetAcceleration

**模型约束：**本模块接口仅可在Stage模型下使用。

**起始版本：**5.1.0(18)

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，固定为'pause'，表示资源暂停事件。 |
| callback | Callback<AssetDownloadTask> | 是 | 回调函数。返回任务信息。 |

**错误码**：

错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 1016600000 | The API call from an ExtensionAbility is not allowed. |
| 1016600094 | Task service ability error. |

**示例**：

```ets
import { assetDownloadManager } from '@kit.GraphicsAccelerateKit';

let onPauseCallback = (downloadTaskInfo: assetDownloadManager.AssetDownloadTask) => {
  console.info('AssetAccelDemo', `task identifier = ${downloadTaskInfo.config.identifier} has paused.`);
  // 添加资源包下载暂停处理逻辑。
};
// 订阅资源包下载暂停事件。
assetDownloadManager.on("pause", onPauseCallback);
```

#### assetDownloadManager.off('pause')

off(type: 'pause', callback?: Callback<AssetDownloadTask>): void

取消订阅资源包下载暂停事件。使用callback形式返回结果。

**系统能力：**SystemCapability.GraphicsGame.AssetAcceleration

**模型约束：**本模块接口仅可在Stage模型下使用。

**起始版本：**5.1.0(18)

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消事件回调类型，固定为'pause'，表示资源暂停事件。 |
| callback | Callback<AssetDownloadTask> | 否 | 需要取消监听的回调函数，需与订阅时传入的回调函数一致。若不填，则取消当前监听该事件的所有回调函数。 |

**错误码**：

错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 1016600000 | The API call from an ExtensionAbility is not allowed. |
| 1016600094 | Task service ability error. |

**示例**：

```ets
import { assetDownloadManager } from '@kit.GraphicsAccelerateKit';

let onPauseCallback = (downloadTaskInfo: assetDownloadManager.AssetDownloadTask) => {
  console.info('AssetAccelDemo', `task identifier = ${downloadTaskInfo.config.identifier} has paused.`);
  // 添加资源包下载暂停处理逻辑。
};
// 取消订阅资源包下载暂停事件.
assetDownloadManager.off("pause", onPauseCallback);
```

#### assetDownloadManager.on('complete')

on(type: 'complete', callback: Callback<DownloadCompletedInfo>): void

订阅资源包下载成功事件。使用callback形式返回结果。

**系统能力：**SystemCapability.GraphicsGame.AssetAcceleration

**模型约束：**本模块接口仅可在Stage模型下使用。

**起始版本：**5.1.0(18)

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，固定为'complete'，表示资源包下载成功事件。 |
| callback | Callback<DownloadCompletedInfo> | 是 | 回调函数。返回任务完成信息。 |

**错误码**：

错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 1016600000 | The API call from an ExtensionAbility is not allowed. |
| 1016600094 | Task service ability error. |

**示例**：

```ets
import { assetDownloadManager } from '@kit.GraphicsAccelerateKit';

let onCompleteCallback = (completeInfo: assetDownloadManager.DownloadCompletedInfo) => {
  console.info('AssetAccelDemo', `task identifier = ${completeInfo.downloadTask.config.identifier} has completed.`);
  // 添加资源包下载成功处理逻辑。
};
// 订阅资源包下载成功事件。
assetDownloadManager.on("complete", onCompleteCallback);
```

#### assetDownloadManager.off('complete')

off(type: 'complete', callback?: Callback<DownloadCompletedInfo>): void

取消订阅资源包下载成功事件。使用callback形式返回结果。

**系统能力：**SystemCapability.GraphicsGame.AssetAcceleration

**模型约束：**本模块接口仅可在Stage模型下使用。

**起始版本：**5.1.0(18)

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消事件回调类型，固定为'complete'，表示资源包下载成功事件。 |
| callback | Callback<DownloadCompletedInfo> | 否 | 需要取消监听的回调函数，需与订阅时传入的回调函数一致。若不填，则取消当前监听该事件的所有回调函数。 |

**错误码**：

错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 1016600000 | The API call from an ExtensionAbility is not allowed. |
| 1016600094 | Task service ability error. |

**示例**：

```ets
import { assetDownloadManager } from '@kit.GraphicsAccelerateKit';

let onCompleteCallback = (completeInfo: assetDownloadManager.DownloadCompletedInfo) => {
  console.info('AssetAccelDemo', `task identifier = ${completeInfo.downloadTask.config.identifier} has completed.`);
  // 添加资源包下载成功处理逻辑。
};
// 取消订阅资源包下载成功事件。
assetDownloadManager.off("complete", onCompleteCallback);
```

#### assetDownloadManager.on('fail')

on(type: 'fail', callback: Callback<DownloadFailedInfo>): void

订阅资源包下载失败事件。使用callback形式返回结果。

**系统能力：**SystemCapability.GraphicsGame.AssetAcceleration

**模型约束：**本模块接口仅可在Stage模型下使用。

**起始版本：**5.1.0(18)

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，固定为'fail'，表示资源包下载失败事件。 |
| callback | Callback<DownloadFailedInfo> | 是 | 回调函数。返回任务失败信息。 |

**错误码**：

错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 1016600000 | The API call from an ExtensionAbility is not allowed. |
| 1016600094 | Task service ability error. |

**示例**：

```ets
import { assetDownloadManager } from '@kit.GraphicsAccelerateKit';

let onFailedCallback = (failedInfo: assetDownloadManager.DownloadFailedInfo) => {
  console.info('AssetAccelDemo', `task identifier = ${failedInfo.downloadTask.config.identifier} has failed.`);
  // 添加资源包下载失败处理逻辑。
};
// 订阅资源包下载失败事件。
assetDownloadManager.on("fail", onFailedCallback);
```

#### assetDownloadManager.off('fail')

off(type: 'fail', callback?: Callback<DownloadFailedInfo>): void

取消订阅资源包下载失败事件。使用callback形式返回结果。

**系统能力：**SystemCapability.GraphicsGame.AssetAcceleration

**模型约束：**本模块接口仅可在Stage模型下使用。

**起始版本：**5.1.0(18)

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消事件回调类型，固定为'fail'，表示资源包下载失败事件。 |
| callback | Callback<DownloadFailedInfo> | 否 | 需要取消监听的回调函数，需与订阅时传入的回调函数一致。若不填，则取消当前监听该事件的所有回调函数。 |

**错误码**：

错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 1016600000 | The API call from an ExtensionAbility is not allowed. |
| 1016600094 | Task service ability error. |

**示例**：

```ets
import { assetDownloadManager } from '@kit.GraphicsAccelerateKit';

let onFailedCallback = (failedInfo: assetDownloadManager.DownloadFailedInfo) => {
  console.info('AssetAccelDemo', `task identifier = ${failedInfo.downloadTask.config.identifier} has failed.`);
  // 添加资源包下载失败处理逻辑。
};
// 取消订阅资源包下载失败事件。
assetDownloadManager.off("fail", onFailedCallback);
```

#### assetDownloadManager.fetchManifestUrl

fetchManifestUrl(): Promise<string>

获取资源包下载列表。使用Promise异步回调。

**需要权限：**ohos.permission.INTERNET

**系统能力：**SystemCapability.GraphicsGame.AssetAcceleration

**模型约束：**此接口仅可在Stage模型下使用。

**起始版本：**5.1.0(18)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象。 - 若资源托管至华为CDN，返回资源包下载清单manifestUrl。 - 若资源托管至三方CDN，则返回空字符串。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | No Internet permission. |
| 1016600094 | Task service ability error. |

**示例**：

```ets
import { assetDownloadManager } from '@kit.GraphicsAccelerateKit';

async fetchManifestUrl() {
  let manifestUrl : string = '';
  try {
    manifestUrl = await assetDownloadManager.fetchManifestUrl();
    console.info('AssetAccelDemo', `Succeeded in fetching manifestUrl, manifestUrl = ${manifestUrl}`);
  } catch (error) {
    console.error('AssetAccelDemo', `Failed to fetch manifestUrl, errCode: ${error.code}, errMessage: ${error.message}`);
    return;
  }
```

#### assetDownloadManager.addAssetDownloadTask

addAssetDownloadTask(context: common.BaseContext, downloadConfig: AssetDownloadConfig): Promise<string>

新增资源包下载任务。使用Promise异步回调。

**需要权限：**ohos.permission.INTERNET

**系统能力：**SystemCapability.GraphicsGame.AssetAcceleration

**模型约束：**此接口仅可在Stage模型下使用。

**起始版本：**5.1.0(18)

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | common.BaseContext | 是 | 应用程序上下文。 |
| downloadConfig | AssetDownloadConfig | 是 | 资源包下载任务的配置信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象。返回下载任务taskID。 最大长度36个字节。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | No Internet permission. |
| 401 | Parameter error. |
| 1016600000 | The API call from an ExtensionAbility is not allowed. |
| 1016600001 | The domain name of the download task is not in the domain name trustlist. |
| 1016600004 | The application task queue is full. |
| 1016600094 | Task service ability error. |

**示例**：

```ets
import { assetDownloadManager } from '@kit.GraphicsAccelerateKit';
import { common } from '@kit.AbilityKit';

async addAssetDownloadTask() {
  // 构造资源包下载配置信息。
  let assetDownload: assetDownloadManager.AssetDownloadConfig = {
    fileName: 'fileName', // 下载资源的文件名。
    url: 'url', // 下载资源url。
    isEssential: false, // 是否是必要下载资源。
    identifier: 'identifier', // 下载资源标识信息。
    groupId: 'groupId' // 组ID，用于标识资源的版本信息。
  }
  try {
    // 添加资源包下载任务。
    // 根据实际代码上下文自行传入合适的context。
    const taskId: string = await assetDownloadManager.addAssetDownloadTask(this.getUIContext().getHostContext() as common.Context, assetDownload);
    console.info('AssetAccelDemo', `Succeeded in adding assetDownloadTask`);
  } catch (error) {
    console.error('AssetAccelDemo', `Failed to add assetDownloadTask, errCode:${error.code}, errMessage:${error.message}`);
  }
```

#### assetDownloadManager.pauseAssetDownloadTask

pauseAssetDownloadTask(taskId: string): Promise<void>

暂停资源包下载任务。使用Promise异步回调。

**需要权限：**ohos.permission.INTERNET

**系统能力：**SystemCapability.GraphicsGame.AssetAcceleration

**模型约束：**此接口仅可在Stage模型下使用。

**起始版本：**5.1.0(18)

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| taskId | string | 是 | 任务ID。 最大长度36个字节。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | No Internet permission. |
| 401 | Parameter error. |
| 1016600000 | The API call from an ExtensionAbility is not allowed. |
| 1016600002 | The task ID or group ID entered during operations such as pause, resume, and fetch does not exist. |
| 1016600003 | The current task status does not support the current operator. |
| 1016600094 | Task service ability error. |

**示例**：

```ets
import { assetDownloadManager } from '@kit.GraphicsAccelerateKit';
import { common } from '@kit.AbilityKit';

async pauseAssetDownloadTask() {
  // 构造资源包下载配置信息。
  let assetDownload: assetDownloadManager.AssetDownloadConfig = {
    fileName: 'fileName', // 下载资源的文件名。
    url: 'url', // 下载资源url。
    isEssential: false, // 是否是必要下载资源。
    identifier: 'identifier', // 下载资源标识信息。
    groupId: 'groupId' // 组ID，用于标识资源的版本信息。
  }
  let taskId: string = '';
  try {
    // 添加资源包下载任务。
    // 根据实际代码上下文自行传入合适的context。
    taskId = await assetDownloadManager.addAssetDownloadTask(this.getUIContext().getHostContext() as common.Context, assetDownload);
    console.info('AssetAccelDemo', `Succeeded in adding assetDownloadTask`);
  } catch (error) {
    console.error('AssetAccelDemo', `Failed to add assetDownloadTask, errCode:${error.code}, errMessage:${error.message}`);
    return;
  }
  try {
    // 根据taskId暂停资源包下载任务
    await assetDownloadManager.pauseAssetDownloadTask(taskId);
    console.info('AssetAccelDemo', `Succeeded in pausing assetDownloadTask`);
  } catch (error) {
    console.error('AssetAccelDemo', `Failed to pause assetDownloadTask, errCode:${error.code}, errMessage:${error.message}`);
    return;
  }
```

#### assetDownloadManager.resumeAssetDownloadTask

resumeAssetDownloadTask(taskId: string): Promise<void>

恢复资源包下载任务。使用Promise异步回调。

**需要权限：**ohos.permission.INTERNET

**系统能力：**SystemCapability.GraphicsGame.AssetAcceleration

**模型约束：**此接口仅可在Stage模型下使用。

**起始版本：**5.1.0(18)

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| taskId | string | 是 | 任务ID。 最大长度36个字节。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | No Internet permission. |
| 401 | Parameter error. |
| 1016600000 | The API call from an ExtensionAbility is not allowed. |
| 1016600002 | The task ID or group ID entered during operations such as pause, resume, and fetch does not exist. |
| 1016600003 | The current task status does not support the current operator. |
| 1016600094 | Task service ability error. |

**示例**：

```ets
import { assetDownloadManager } from '@kit.GraphicsAccelerateKit';
import { common } from '@kit.AbilityKit';

async resumeAssetDownloadTask() {
  // 构造资源包下载配置信息。
  let assetDownload: assetDownloadManager.AssetDownloadConfig = {
    fileName: 'fileName', // 下载资源的文件名。
    url: 'url', // 下载资源url。
    isEssential: false, // 是否是必要下载资源。
    identifier: 'identifier', // 下载资源标识信息。
    groupId: 'groupId' // 组ID，用于标识资源的版本信息。
  }
  let taskId: string = '';
  try {
    // 添加资源包下载任务。
    // 根据实际代码上下文自行传入合适的context。
    taskId = await assetDownloadManager.addAssetDownloadTask(this.getUIContext().getHostContext() as common.Context, assetDownload);
    console.info('AssetAccelDemo', `Succeeded in adding assetDownloadTask`);
  } catch (error) {
    console.error('AssetAccelDemo', `Failed to add assetDownloadTask, errCode:${error.code}, errMessage:${error.message}`);
    return;
  }
  try {
    // 根据taskId暂停资源包下载任务
    assetDownloadManager.pauseAssetDownloadTask(taskId);
    console.info('AssetAccelDemo', `Succeeded in pausing assetDownloadTask`);
  } catch (error) {
    console.error('AssetAccelDemo', `Failed to pause assetDownloadTask, errCode:${error.code}, errMessage:${error.message}`);
    return;
  }
  try {
    // 根据taskId恢复资源包下载任务
    await assetDownloadManager.resumeAssetDownloadTask(taskId);
    console.info('AssetAccelDemo', `Succeeded in resuming assetDownloadTask`);
  } catch (error) {
    console.error('AssetAccelDemo', `Failed to resume assetDownloadTask, errCode:${error.code}, errMessage:${error.message}`);
    return;
  }
```

#### assetDownloadManager.removeAssetDownloadTask

removeAssetDownloadTask(taskId: string): Promise<void>

移除资源包下载任务。使用Promise异步回调。

**系统能力：**SystemCapability.GraphicsGame.AssetAcceleration

**模型约束：**此接口仅可在Stage模型下使用。

**起始版本：**5.1.0(18)

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| taskId | string | 是 | 任务ID。 最大长度36个字节。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 1016600002 | The task ID or group ID entered during operations such as pause, resume, and fetch does not exist. |
| 1016600094 | Task service ability error. |

**示例**：

```ets
import { assetDownloadManager } from '@kit.GraphicsAccelerateKit';
import { common } from '@kit.AbilityKit';

async removeAssetDownloadTask() {
  // 构造资源包下载配置信息。
  let assetDownload: assetDownloadManager.AssetDownloadConfig = {
    fileName: 'fileName', // 下载资源的文件名。
    url: 'url', // 下载资源url。
    isEssential: false, // 是否是必要下载资源。
    identifier: 'identifier', // 下载资源标识信息。
    groupId: 'groupId' // 组ID，用于标识资源的版本信息。
  }
  let taskId: string = '';
  try {
    // 添加资源包下载任务。
    // 根据实际代码上下文自行传入合适的context。
    taskId = await assetDownloadManager.addAssetDownloadTask(this.getUIContext().getHostContext() as common.Context, assetDownload);
    console.info('AssetAccelDemo', `Succeeded in adding assetDownloadTask`);
  } catch (error) {
    console.error('AssetAccelDemo', `Failed to add assetDownloadTask, errCode:${error.code}, errMessage:${error.message}`);
    return;
  }
  try {
    // 根据taskId删除资源包下载任务
    await assetDownloadManager.removeAssetDownloadTask(taskId);
    console.info('AssetAccelDemo', `Succeeded in removing assetDownloadTask`);
  } catch (error) {
    console.error('AssetAccelDemo', `Failed to remove assetDownloadTask, errCode:${error.code}, errMessage:${error.message}`);
    return;
  }
```

#### assetDownloadManager.fetchAllAssetDownloadTasks

fetchAllAssetDownloadTasks(): Promise<AssetDownloadTask[]>

获取所有资源包下载任务，已下载完成的任务除外。使用Promise异步回调。

**系统能力：**SystemCapability.GraphicsGame.AssetAcceleration

**模型约束：**此接口仅可在Stage模型下使用。

**起始版本：**5.1.0(18)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<AssetDownloadTask[]> | Promise对象。返回资源包下载任务列表。 |

**错误码**：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1016600094 | Task service ability error. |

**示例**：

```ets
import { assetDownloadManager } from '@kit.GraphicsAccelerateKit';
import { common } from '@kit.AbilityKit';

async fetchAllAssetDownloadTasks() {
  // 构造资源包下载配置信息。
  let assetDownload: assetDownloadManager.AssetDownloadConfig = {
    fileName: 'fileName', // 下载资源的文件名。
    url: 'url', // 下载资源url。
    isEssential: false, // 是否是必要下载资源。
    identifier: 'identifier', // 下载资源标识信息。
    groupId: 'groupId' // 组ID，用于标识资源的版本信息。
  }
  let taskId: string = '';
  try {
    // 添加资源包下载任务。
    // 根据实际代码上下文自行传入合适的context。
    taskId = await assetDownloadManager.addAssetDownloadTask(this.getUIContext().getHostContext() as common.Context, assetDownload);
    console.info('AssetAccelDemo', `Succeeded in adding assetDownloadTask`);
  } catch (error) {
    console.error('AssetAccelDemo', `Failed to add assetDownloadTask, errCode:${error.code}, errMessage:${error.message}`);
    return;
  }
  let downloadTaskArr: Array<assetDownloadManager.AssetDownloadTask>;
  try {
    // 获取所有资源包下载任务信息。
    downloadTaskArr = await assetDownloadManager.fetchAllAssetDownloadTasks();
    console.info('AssetAccelDemo', `Succeeded in fetching allAssetDownloadTasks success, downloadTaskArr length:${downloadTaskArr.length}.`);
  } catch (error) {
    console.error('AssetAccelDemo', `Failed to fetch allAssetDownloadTasks, errCode:${error.code}, errMessage:${error.message}`);
    return;
  }
```

#### assetDownloadManager.pauseAllAssetDownloadTasks

pauseAllAssetDownloadTasks(): Promise<void>

暂停所有资源包下载任务。使用Promise异步回调。

**需要权限：**ohos.permission.INTERNET

**系统能力：**SystemCapability.GraphicsGame.AssetAcceleration

**模型约束：**此接口仅可在Stage模型下使用。

**起始版本：**5.1.0(18)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | No Internet permission. |
| 1016600000 | The API call from an ExtensionAbility is not allowed. |
| 1016600094 | Task service ability error. |

**示例**：

```ets
import { assetDownloadManager } from '@kit.GraphicsAccelerateKit';
import { common } from '@kit.AbilityKit';

async pauseAllAssetDownloadTasks() {
  // 构造资源包下载配置信息。
  let assetDownload: assetDownloadManager.AssetDownloadConfig = {
    fileName: 'fileName', // 下载资源的文件名。
    url: 'url', // 下载资源url。
    isEssential: false, // 是否是必要下载资源。
    identifier: 'identifier', // 下载资源标识信息。
    groupId: 'groupId' // 组ID，用于标识资源的版本信息。
  }
  let taskId: string = '';
  try {
    // 添加资源包下载任务。
    // 根据实际代码上下文自行传入合适的context。
    taskId = await assetDownloadManager.addAssetDownloadTask(this.getUIContext().getHostContext() as common.Context, assetDownload);
    console.info('AssetAccelDemo', `Succeeded in adding assetDownloadTask`);
  } catch (error) {
    console.error('AssetAccelDemo', `Failed to add assetDownloadTask, errCode:${error.code}, errMessage:${error.message}`);
    return;
  }
  try {
    // 暂停所有资源包下载任务。
    await assetDownloadManager.pauseAllAssetDownloadTasks();
    console.info('AssetAccelDemo', `Succeeded in pausing allAssetDownloadTasks`);
  } catch (error) {
    console.error('AssetAccelDemo', `Failed to pause allAssetDownloadTasks, errCode:${error.code}, errMessage:${error.message}`);
    return;
  }
```

#### assetDownloadManager.resumeAllAssetDownloadTasks

resumeAllAssetDownloadTasks(): Promise<void>

恢复所有资源包下载任务。使用Promise异步回调。

**需要权限：**ohos.permission.INTERNET

**系统能力：**SystemCapability.GraphicsGame.AssetAcceleration

**模型约束：**此接口仅可在Stage模型下使用。

**起始版本：**5.1.0(18)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | No Internet permission. |
| 1016600000 | The API call from an ExtensionAbility is not allowed. |
| 1016600094 | Task service ability error. |

**示例**：

```ets
import { assetDownloadManager } from '@kit.GraphicsAccelerateKit';
import { common } from '@kit.AbilityKit';

async resumeAllAssetDownloadTasks() {
  // 构造资源包下载配置信息。
  let assetDownload: assetDownloadManager.AssetDownloadConfig = {
    fileName: 'fileName', // 下载资源的文件名。
    url: 'url', // 下载资源url。
    isEssential: false, // 是否是必要下载资源。
    identifier: 'identifier', // 下载资源标识信息。
    groupId: 'groupId' // 组ID，用于标识资源的版本信息。
  }
  let taskId: string = '';
  try {
    // 添加资源包下载任务。
    // 根据实际代码上下文自行传入合适的context。
    taskId = await assetDownloadManager.addAssetDownloadTask(this.getUIContext().getHostContext() as common.Context, assetDownload);
    console.info('AssetAccelDemo', `Succeeded in adding assetDownloadTask`);
  } catch (error) {
    console.error('AssetAccelDemo', `Failed to add assetDownloadTask, errCode:${error.code}, errMessage:${error.message}`);
    return;
  }
  try {
    // 暂停所有资源包下载任务。
    await assetDownloadManager.pauseAllAssetDownloadTasks();
    console.info('AssetAccelDemo', `Succeeded in pausing allAssetDownloadTasks`);
  } catch (error) {
    console.error('AssetAccelDemo', `Failed to pause allAssetDownloadTasks, errCode:${error.code}, errMessage:${error.message}`);
    return;
  }
  try {
    // 恢复所有资源包下载任务。
    await assetDownloadManager.resumeAllAssetDownloadTasks();
    console.info('AssetAccelDemo', `Succeeded in resuming allAssetDownloadTasks`);
  } catch (error) {
    console.error('AssetAccelDemo', `Failed to resume allAssetDownloadTasks, errCode:${error.code}, errMessage:${error.message}`);
    return;
  }
```

#### assetDownloadManager.removeAllAssetDownloadTasks

removeAllAssetDownloadTasks(): Promise<void>

移除所有资源包下载任务。使用Promise异步回调。

**系统能力：**SystemCapability.GraphicsGame.AssetAcceleration

**模型约束：**此接口仅可在Stage模型下使用。

**起始版本：**5.1.0(18)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码**：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1016600094 | Task service ability error. |

**示例**：

```ets
import { assetDownloadManager } from '@kit.GraphicsAccelerateKit';
import { common } from '@kit.AbilityKit';

async removeAllAssetDownloadTasks() {
  // 构造资源包下载配置信息。
  let assetDownload: assetDownloadManager.AssetDownloadConfig = {
    fileName: 'fileName', // 下载资源的文件名。
    url: 'url', // 下载资源url。
    isEssential: false, // 是否是必要下载资源。
    identifier: 'identifier', // 下载资源标识信息。
    groupId: 'groupId' // 组ID，用于标识资源的版本信息。
  }
  let taskId: string = '';
  try {
    // 添加资源包下载任务。
    // 根据实际代码上下文自行传入合适的context。
    taskId = await assetDownloadManager.addAssetDownloadTask(this.getUIContext().getHostContext() as common.Context, assetDownload);
    console.info('AssetAccelDemo', `Succeeded in adding assetDownloadTask`);
  } catch (error) {
    console.error('AssetAccelDemo', `Failed to add assetDownloadTask, errCode:${error.code}, errMessage:${error.message}`);
    return;
  }
  try {
    // 移除所有资源包下载任务。
    await assetDownloadManager.removeAllAssetDownloadTasks();
    console.info('AssetAccelDemo', `Succeeded in removing allAssetDownloadTasks`);
  } catch (error) {
    console.error('AssetAccelDemo', `Failed to remove allAssetDownloadTasks, errCode:${error.code}, errMessage:${error.message}`);
    return;
  }
```

#### assetDownloadManager.fetchGroupAssetDownloadTasks

fetchGroupAssetDownloadTasks(groupId: string): Promise<AssetDownloadTask[]>

获取同一组的资源包下载任务。使用Promise异步回调。

**系统能力：**SystemCapability.GraphicsGame.AssetAcceleration

**模型约束：**此接口仅可在Stage模型下使用。

**起始版本：**5.1.0(18)

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| groupId | string | 是 | 组ID，用于标识资源的版本信息。 最大长度32个字节。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<AssetDownloadTask[]> | Promise对象。返回资源包下载任务列表。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 1016600002 | The task ID or group ID entered during operations such as pause, resume, and fetch does not exist. |
| 1016600094 | Task service ability error. |

**示例**：

```ets
import { assetDownloadManager } from '@kit.GraphicsAccelerateKit';
import { common } from '@kit.AbilityKit';

async fetchGroupAssetDownloadTasks() {
  // 构造资源包下载配置信息。
  let assetDownload: assetDownloadManager.AssetDownloadConfig = {
    fileName: 'fileName', // 下载资源的文件名。
    url: 'url', // 下载资源url。
    isEssential: false, // 是否是必要下载资源。
    identifier: 'identifier', // 下载资源标识信息。
    groupId: 'groupId' // 组ID，用于标识资源的版本信息。
  }
  let taskId: string = '';
  try {
    // 添加资源包下载任务。
    // 根据实际代码上下文自行传入合适的context。
    taskId = await assetDownloadManager.addAssetDownloadTask(this.getUIContext().getHostContext() as common.Context, assetDownload);
    console.info('AssetAccelDemo', `Succeeded in adding assetDownloadTask`);
  } catch (error) {
    console.error('AssetAccelDemo', `Failed to add assetDownloadTask, errCode:${error.code}, errMessage:${error.message}`);
    return;
  }
  let groupId = 'groupId';
  let downloadTaskArr: Array<assetDownloadManager.AssetDownloadTask>;
  try {
    // 获取同一groupId下的资源包下载任务信息。
    downloadTaskArr = await assetDownloadManager.fetchGroupAssetDownloadTasks(groupId);
    console.info('AssetAccelDemo', `Succeeded in fetching groupAssetDownloadTasks`);
  } catch (error) {
    console.error('AssetAccelDemo', `Failed to fetch groupAssetDownloadTasks, errCode:${error.code}, errMessage:${error.message}`);
    return;
  }
```

#### assetDownloadManager.pauseGroupAssetDownloadTasks

pauseGroupAssetDownloadTasks(groupId: string): Promise<void>

暂停同一组的资源包下载任务。使用Promise异步回调。

**需要权限**：ohos.permission.INTERNET

**系统能力：**SystemCapability.GraphicsGame.AssetAcceleration

**模型约束：**此接口仅可在Stage模型下使用。

**起始版本：**5.1.0(18)

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| groupId | string | 是 | 组ID，用于标识资源的版本信息。 最大长度32个字节。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | No Internet permission. |
| 401 | Parameter error. |
| 1016600000 | The API call from an ExtensionAbility is not allowed. |
| 1016600002 | The task ID or group ID entered during operations such as pause, resume, and fetch does not exist. |
| 1016600094 | Task service ability error. |

**示例**：

```ets
import { assetDownloadManager } from '@kit.GraphicsAccelerateKit';
import { common } from '@kit.AbilityKit';

async pauseGroupAssetDownloadTasks() {
  // 构造资源包下载配置信息。
  let assetDownload: assetDownloadManager.AssetDownloadConfig = {
    fileName: 'fileName', // 下载资源的文件名。
    url: 'url', // 下载资源url。
    isEssential: false, // 是否是必要下载资源。
    identifier: 'identifier', // 下载资源标识信息。
    groupId: 'groupId' // 组ID，用于标识资源的版本信息。
  }
  let taskId: string = '';
  try {
    // 添加资源包下载任务。
    // 根据实际代码上下文自行传入合适的context。
    taskId = await assetDownloadManager.addAssetDownloadTask(this.getUIContext().getHostContext() as common.Context, assetDownload);
    console.info('AssetAccelDemo', `Succeeded in adding assetDownloadTask`);
  } catch (error) {
    console.error('AssetAccelDemo', `Failed to add assetDownloadTask, errCode:${error.code}, errMessage:${error.message}`);
    return;
  }
  let groupId = 'groupId';
  try {
    // 暂停同一groupId下的资源包下载任务。
    await assetDownloadManager.pauseGroupAssetDownloadTasks(groupId);
    console.info('AssetAccelDemo', `Succeeded in pausing groupAssetDownloadTasks`);
  } catch (error) {
    console.error('AssetAccelDemo', `Failed to pause groupAssetDownloadTasks, errCode:${error.code}, errMessage:${error.message}`);
    return;
  }
```

#### assetDownloadManager.resumeGroupAssetDownloadTasks

resumeGroupAssetDownloadTasks(groupId: string): Promise<void>

恢复同一组的资源包下载任务。使用Promise异步回调。

**需要权限**：ohos.permission.INTERNET

**系统能力：**SystemCapability.GraphicsGame.AssetAcceleration

**模型约束：**此接口仅可在Stage模型下使用。

**起始版本：**5.1.0(18)

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| groupId | string | 是 | 组ID，用于标识资源的版本信息。 最大长度32个字节。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | No Internet permission. |
| 401 | Parameter error. |
| 1016600000 | The API call from an ExtensionAbility is not allowed. |
| 1016600002 | The task ID or group ID entered during operations such as pause, resume, and fetch does not exist. |
| 1016600094 | Task service ability error. |

**示例**：

```ets
import { assetDownloadManager } from '@kit.GraphicsAccelerateKit';
import { common } from '@kit.AbilityKit';

async resumeGroupAssetDownloadTasks() {
  // 构造资源包下载配置信息。
  let assetDownload: assetDownloadManager.AssetDownloadConfig = {
    fileName: 'fileName', // 下载资源的文件名。
    url: 'url', // 下载资源url。
    isEssential: false, // 是否是必要下载资源。
    identifier: 'identifier', // 下载资源标识信息。
    groupId: 'groupId' // 组ID，用于标识资源的版本信息。
  }
  let taskId: string = '';
  try {
    // 添加资源包下载任务。
    // 根据实际代码上下文自行传入合适的context。
    taskId = await assetDownloadManager.addAssetDownloadTask(this.getUIContext().getHostContext() as common.Context, assetDownload);
    console.info('AssetAccelDemo', `Succeeded in adding assetDownloadTask`);
  } catch (error) {
    console.error('AssetAccelDemo', `Failed to add assetDownloadTask, errCode:${error.code}, errMessage:${error.message}`);
    return;
  }
  let groupId = 'groupId';
  try {
    // 暂停同一groupId下的资源包下载任务。
    await assetDownloadManager.pauseGroupAssetDownloadTasks(groupId);
    console.info('AssetAccelDemo', `Succeeded in pausing groupAssetDownloadTasks`);
  } catch (error) {
    console.error('AssetAccelDemo', `Failed to pause groupAssetDownloadTasks, errCode:${error.code}, errMessage:${error.message}`);
    return;
  }
  try {
    // 恢复同一groupId下的资源包下载任务。
    await assetDownloadManager.resumeGroupAssetDownloadTasks(groupId);
    console.info('AssetAccelDemo', `Succeeded in resuming groupAssetDownloadTasks`);
  } catch (error) {
    console.error('AssetAccelDemo', `Failed to resume groupAssetDownloadTasks, errCode:${error.code}, errMessage:${error.message}`);
    return;
  }
```

#### assetDownloadManager.removeGroupAssetDownloadTasks

removeGroupAssetDownloadTasks(groupId: string): Promise<void>

移除同一组的资源包下载任务。使用Promise异步回调。

**系统能力：**SystemCapability.GraphicsGame.AssetAcceleration

**模型约束：**此接口仅可在Stage模型下使用。

**起始版本：**5.1.0(18)

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| groupId | string | 是 | 组ID，用于标识资源的版本信息。 最大长度32个字节。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 1016600002 | The task ID or group ID entered during operations such as pause, resume, and fetch does not exist. |
| 1016600094 | Task service ability error. |

**示例**：

```ets
import { assetDownloadManager } from '@kit.GraphicsAccelerateKit';
import { common } from '@kit.AbilityKit';

async removeGroupAssetDownloadTasks() {
  // 构造资源包下载配置信息。
  let assetDownload: assetDownloadManager.AssetDownloadConfig = {
    fileName: 'fileName', // 下载资源的文件名。
    url: 'url', // 下载资源url。
    isEssential: false, // 是否是必要下载资源。
    identifier: 'identifier', // 下载资源标识信息。
    groupId: 'groupId' // 组ID，用于标识资源的版本信息。
  }
  let taskId: string = '';
  try {
    // 添加资源包下载任务。
    // 根据实际代码上下文自行传入合适的context。
    taskId = await assetDownloadManager.addAssetDownloadTask(this.getUIContext().getHostContext() as common.Context, assetDownload);
    console.info('AssetAccelDemo', `Succeeded in adding assetDownloadTask`);
  } catch (error) {
    console.error('AssetAccelDemo', `Failed to add assetDownloadTask, errCode:${error.code}, errMessage:${error.message}`);
    return;
  }
  let groupId = 'groupId';
  try {
    // 移除同一groupId下的资源包下载任务。
    await assetDownloadManager.removeGroupAssetDownloadTasks(groupId);
    console.info('AssetAccelDemo', `Succeeded in removing groupAssetDownloadTasks`);
  } catch (error) {
    console.error('AssetAccelDemo', `Failed to remove groupAssetDownloadTasks, errCode:${error.code}, errMessage:${error.message}`);
    return;
  }
```

#### NetSpeedLevel

网络限速等级的枚举。

**系统能力：**SystemCapability.GraphicsGame.AssetAcceleration

**模型约束：**本模块接口仅可在Stage模型下使用。

**起始版本：**5.1.0(18)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NO_LIMIT | 0 | 无速度限制。 |
| LIMIT_MEDIUM | 1 | 中等速度限制。 |
| LIMIT_LOW | 2 | 低等速度限制。 |

#### assetDownloadManager.limitDownloadTaskSpeed

limitDownloadTaskSpeed(taskIds: string[], speedLimit: NetSpeedLevel): Promise<void>

限制资源包下载的速度。使用Promise异步回调。

**需要权限**：ohos.permission.INTERNET

**系统能力：**SystemCapability.GraphicsGame.AssetAcceleration

**模型约束：**此接口仅可在Stage模型下使用。

**起始版本：**5.1.0(18)

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| taskIds | string[] | 是 | 任务ID列表。 |
| speedLimit | NetSpeedLevel | 是 | 网络限速等级。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | No Internet permission. |
| 401 | Parameter error. |
| 1016600094 | Task service ability error. |

**示例**：

```ets
import { assetDownloadManager } from '@kit.GraphicsAccelerateKit';
import { common } from '@kit.AbilityKit';

async limitDownloadTaskSpeed() {
  // 构造资源包下载配置信息。
  let assetDownload: assetDownloadManager.AssetDownloadConfig = {
    fileName: 'fileName', // 下载资源的文件名。
    url: 'url', // 下载资源url。
    isEssential: false, // 是否是必要下载资源。
    identifier: 'identifier', // 下载资源标识信息。
    groupId: 'groupId' // 组ID，用于标识资源的版本信息。
  }
  let taskId: string = '';
  try {
    // 添加资源包下载任务。
    // 根据实际代码上下文自行传入合适的context。
    taskId = await assetDownloadManager.addAssetDownloadTask(this.getUIContext().getHostContext() as common.Context, assetDownload);
    console.info('AssetAccelDemo', `Succeeded in adding assetDownloadTask`);
  } catch (error) {
    console.error('AssetAccelDemo', `Failed to add assetDownloadTask, errCode:${error.code}, errMessage:${error.message}`);
    return;
  }
  try {
    const taskIds: string[] = [taskId];
    // 限制资源包下载任务的下载速度。
    assetDownloadManager.limitDownloadTaskSpeed(taskIds, assetDownloadManager.NetSpeedLevel.LIMIT_MEDIUM);
    console.info('AssetAccelDemo', `Succeeded in limiting downloadTaskSpeed`);
  } catch (error) {
    console.error('AssetAccelDemo', `Failed to limit downloadTaskSpeed, errCode:${error.code}, errMessage:${error.message}`);
    return;
  }
```

#### AppDownloadStatus

应用自身下载器中资源包下载状态的枚举。

**系统能力：**SystemCapability.GraphicsGame.AssetAcceleration

**模型约束：**本模块接口仅可在Stage模型下使用。

**起始版本：**5.1.1(19)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| IN_PROGRESS | 0 | 下载中。 |
| FINISH | 1 | 已完成下载。 |

**ResourceType**

资源类型，影响下载完成通知的内容样式。

系统能力： SystemCapability.GraphicsGame.AssetAcceleration

模型约束： 本模块接口仅可在Stage模型下使用。

起始版本： 6.1.0(23)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| RELEASED | 0 | 已发布的资源，即已公开发布过的资源。 完成下载后，通知栏展示“xxx 游戏资源包已更新”。 |
| PRE_RELEASE | 1 | 预发布的资源，即未公开发布过的资源。 完成下载后，通知栏展示“xxx 游戏资源包预下载已完成” |

#### AppDownloadProgress

应用自身下载器中资源包的下载进度信息。

**系统能力：**SystemCapability.GraphicsGame.AssetAcceleration

**模型约束：**本模块接口仅可在Stage模型下使用。

**起始版本：**5.1.1(19)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| totalBytesWritten | number | 否 | 否 | 已下载的资源总大小，单位：字节。取值范围：大于等于0。 默认值：0。 |
| totalExpectedBytes | number | 否 | 否 | 待下载的资源总大小，单位：字节。取值大于等于0，异常值按0处理。 默认值：0。 |
| totalFiles | number | 否 | 否 | 资源文件总数。取值大于等于0，异常值按0处理。 默认值：0。 |
| successCount | number | 否 | 否 | 已成功下载的文件数。取值大于等于0，异常值按0处理。 默认值：0。 |
| failureCount | number | 否 | 否 | 下载失败的文件数。取值大于等于0，异常值按0处理。 默认值：0。 |
| status | AppDownloadStatus | 否 | 否 | 当前应用自身下载器中的下载状态。 |
| resourceType | ResourceType | 否 | 是 | 后台正在下载的资源类型，不同的资源类型决定了后台下载通知的内容样式。 默认值为RELEASED。 起始版本： 6.1.0(23) |

#### assetDownloadManager.reportDownloadProgress

reportDownloadProgress(progressInfo: AppDownloadProgress): void

上报应用自身下载器中资源包的下载进度信息。

**系统能力：**SystemCapability.GraphicsGame.AssetAcceleration

**模型约束：**本模块接口仅可在Stage模型下使用。

**起始版本：**5.1.1(19)

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| progressInfo | AppDownloadProgress | 是 | 应用自身下载器中的下载进度信息。 |

**错误码**：

错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1016600094 | Task service ability error. |
| 1016600401 | Parameter error. |

**示例**：

```ets
import { assetDownloadManager } from '@kit.GraphicsAccelerateKit';
import { deviceInfo } from '@kit.BasicServicesKit';

try {
  let progressInfo: assetDownloadManager.AppDownloadProgress = {
    totalBytesWritten: 0,
    totalExpectedBytes: 0,
    totalFiles: 0,
    successCount: 0,
    failureCount: 0,
    status:assetDownloadManager.AppDownloadStatus.IN_PROGRESS
  }
  // 判断当前HarmonyOS SDK版本是否为6.1.0(23)及以上版本
  if (deviceInfo.sdkApiVersion >= 23) {
    progressInfo.resourceType = assetDownloadManager.ResourceType.RELEASED
  }
  assetDownloadManager.reportDownloadProgress(progressInfo);
  console.info('AssetAccelDemo', `Succeeded in reporting downloadProgress`);
} catch (error) {
  console.error('AssetAccelDemo', `Failed to report downloadProgress, errCode:${error.code}, errMessage:${error.message}`);
}
```
