# openFileBoost（文件打开加速）

本模块为应用提供文件打开加速状态感知能力。应用可以通过接入对应API，感知文件的加速状态，进而应用可以实现对已加速文件给出独特的UI（user interface）标识等功能，优化用户文件打开体验。

**起始版本：**5.0.5(17)

#### 导入模块

```ets
import { openFileBoost } from '@kit.PreviewKit';
```

#### FilePreloadState

表示文件预加载状态的枚举。

**系统能力：** SystemCapability.PCService.OpenFileBoost

**起始版本：**5.0.5(17)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NOT_PRELOADED | 0 | 文件未预加载 |
| PRELOADING | 1 | 文件预加载中 |
| PRELOADED | 2 | 文件预加载完成 |

#### FilePreloadStatusInfo

文件预加载回调返回的接口实例，表示文件的预加载状态信息。

**系统能力：** SystemCapability.PCService.OpenFileBoost

**起始版本：**5.0.5(17)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| sandboxPath | string | 否 | 否 | 文件的沙箱路径 |
| progress | number | 否 | 否 | 文件预加载进度 |
| state | FilePreloadState | 否 | 否 | 文件预加载状态 |

#### openFileBoost.on('filePreloadStateChanged')

on(type: 'filePreloadStateChanged', callback: Callback<FilePreloadStatusInfo>): void

文件预加载状态回调，应用通过注册回调函数获取文件预加载的状态变化。

**系统能力：** SystemCapability.PCService.OpenFileBoost

**起始版本：**5.0.5(17)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，固定为'filePreloadStateChanged'，每当预加载文件状态变化时都会触发该事件并返回对应信息。 |
| callback | Callback<FilePreloadStatusInfo> | 是 | 回调函数，用于应用获取预加载文件状态变化信息。 |

**错误码：**

通用错误码的详细介绍请参见和[模块错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | 参数检查失败 |
| 1017220001 | 内部失败 |
| 1017220002 | 服务不可用 |

**示例：**

```ets
import { openFileBoost } from '@kit.PreviewKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

function  callback(filePreloadStatusInfo: openFileBoost.FilePreloadStatusInfo): void {
  if (filePreloadStatusInfo.state === openFileBoost.FilePreloadState.PRELOADING) {
    // 预加载过程中，应用可以根据自己设计对应UX
    hilog.info(0x0000, 'testTag', `file is PRELOADING, suggest to show loading animation`);
  }
  if (filePreloadStatusInfo.state === openFileBoost.FilePreloadState.PRELOADED) {
    // 预加载完成，应用可以通过UX显示提示用户加速完成
    hilog.info(0x0000, 'testTag', `file is PRELOADED, suggest to show loaded animation`);
  }
  if (filePreloadStatusInfo.state === openFileBoost.FilePreloadState.NOT_PRELOADED) {
    // 没有预加载，应用可以不显示任何额外UX
    hilog.info(0x0000, 'testTag', `file is UNPRELOADED, suggest do not show animation `);
  }

function register(): void {
  try {
    openFileBoost.on('filePreloadStateChanged', callback);
  } catch(error) {
    let code = (error as BusinessError).code;
    let message = (error as BusinessError).message;
    hilog.error(0x0000, 'testTag', `on filePreloadStateChanged failed, error code: ${code}, message: ${message}.`);
  }
```

#### openFileBoost.off('filePreloadStateChanged')

off(type: 'filePreloadStateChanged', callback?: Callback<FilePreloadStatusInfo>): void

文件预加载状态注销回调，通过注销回调函数取消获取文件预加载的状态变化。

**系统能力：** SystemCapability.PCService.OpenFileBoost

**起始版本：**5.0.5(17)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调用类型，固定为'filePreloadStateChanged'，当预加载文件状态变化时会触发该事件并返回对应信息。 |
| callback | Callback<FilePreloadStatusInfo> | 否 | 回调函数，如果指定参数则取消对应callback（callback对象不可是匿名函数），否则取消所有callback。 |

**错误码：**

通用错误码的详细介绍请参见和[模块错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | 参数检查失败 |
| 1017220001 | 内部失败 |
| 1017220002 | 服务不可用 |

**示例：**

```ets
import { openFileBoost } from '@kit.PreviewKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

function callback1(filePreloadStatusInfo: openFileBoost.FilePreloadStatusInfo): void {
  hilog.info(0x0000, 'testTag', `on filePreloadStateChanged in callback1`);
}
function callback2(filePreloadStatusInfo: openFileBoost.FilePreloadStatusInfo): void {
  hilog.info(0x0000, 'testTag', `on filePreloadStateChanged in callback2`);
}
function callback3(filePreloadStatusInfo: openFileBoost.FilePreloadStatusInfo): void {
  hilog.info(0x0000, 'testTag', `on filePreloadStateChanged in callback3`);
}

function testUnregister(): void {
  try {
    openFileBoost.on('filePreloadStateChanged', callback1);
    openFileBoost.on('filePreloadStateChanged', callback2);
    openFileBoost.on('filePreloadStateChanged', callback3);
    // 单独取消callback1的监听，传入callback1作为参数，后续不会再调用callback1的回调做通知
    openFileBoost.off('filePreloadStateChanged', callback1);
    // 取消所有callback的监听，不传第二个可选参数，后续不会再调用callback2和callback3做通知
    openFileBoost.off('filePreloadStateChanged');
  } catch(error) {
    let code = (error as BusinessError).code;
    let message = (error as BusinessError).message;
    hilog.error(0x0000, 'testTag', `off filePreloadStateChanged failed, error code: ${code}, message: ${message}.`);
  }
```

#### openFileBoost.addFile

addFile(file: string): void

监听一个文件的预加载状态，应用传入文件路径后系统开始监听该文件的预加载状态。后续该文件状态有变化时系统通过'filePreloadStateChanged'事件回调向应用返回文件预加载状态变化。


1.

需要先调用[openFileBoost.on('filePreloadStateChanged')](#ZH-CN_TOPIC_0000002553362431__openfileboostonfilepreloadstatechanged)接口后再调用该接口添加文件预加载状态监听。

1.

当前一个应用最多添加50个文件监听。

当前支持加速的文件类型见[文件打开加速支持的文件类型](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/preview-introduction#文件打开加速支持的文件类型)，不支持的文件类型默认为未预加载状态，不需要调用该接口监听文件预加载状态变更。

**系统能力：** SystemCapability.PCService.OpenFileBoost

**起始版本：**5.0.5(17)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| file | string | 是 | 文件的沙箱路径 |

**错误码：**

通用错误码的详细介绍请参见和[模块错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | 参数检查失败 |
| 1017220001 | 内部失败 |
| 1017220002 | 服务不可用 |
| 1017220003 | 添加的文件个数超过上限 |

**示例：**

```ets
import { openFileBoost } from '@kit.PreviewKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const file:string = "/storage/Users/currentUser/Desktop/10MB_file.docx";
function fileStateChangedCallback(filePreloadStatusInfo: openFileBoost.FilePreloadStatusInfo): void {
  hilog.info(0x0000, 'testTag', `on filePreloadStateChanged, state: ${filePreloadStatusInfo.state}}`);
}

function testAddFile(): void {
  try {
    openFileBoost.on('filePreloadStateChanged', fileStateChangedCallback);
    openFileBoost.addFile(file);
  } catch(error) {
    let code = (error as BusinessError).code;
    let message = (error as BusinessError).message;
    hilog.error(0x0000, 'testTag', `addFile failed, error code: ${code}, message: ${message}.`);
  }
```

#### openFileBoost.removeFile

removeFile(file: string): void

取消监听一个文件的预加载状态，取消后文件的预加载状态变化不会通过回调再通知应用。

**系统能力：** SystemCapability.PCService.OpenFileBoost

**起始版本：**5.0.5(17)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| file | string | 是 | 文件的沙箱路径 |

**错误码：**

通用错误码的详细介绍请参见和[模块错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | 参数检查失败 |
| 1017220001 | 内部失败 |
| 1017220002 | 服务不可用 |

**示例：**

```ets
import { openFileBoost } from '@kit.PreviewKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const file:string = "/storage/Users/currentUser/Desktop/10MB_file.docx";
try {
  openFileBoost.removeFile(file);
} catch(error) {
  let code = (error as BusinessError).code;
  let message = (error as BusinessError).message;
  hilog.error(0x0000, 'testTag', `removeFile failed, error code: ${code}, message: ${message}.`);
}
```

#### openFileBoost.queryFilePreloadStatusInfo

queryFilePreloadStatusInfo(file: string): FilePreloadStatusInfo

查询文件预加载状态，传入文件路径，通过返回值返回该文件当前的预加载状态。

**系统能力：** SystemCapability.PCService.OpenFileBoost

**起始版本：**5.0.5(17)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| file | string | 是 | 文件的沙箱路径 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FilePreloadStatusInfo | 文件预加载状态信息 |

**错误码：**

通用错误码的详细介绍请参见和[模块错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | 参数检查失败 |
| 1017220001 | 内部失败 |
| 1017220002 | 服务不可用 |

**示例：**

```ets
import { openFileBoost } from '@kit.PreviewKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const file:string = "/storage/Users/currentUser/Desktop/10MB_file.docx";
try {
  let statusInfo : openFileBoost.FilePreloadStatusInfo = openFileBoost.queryFilePreloadStatusInfo(file);
  hilog.info(0x0000, 'testTag', 'file, %{public}s, progress:%{public}d  preloadState:%{public}d',
    statusInfo.sandboxPath, statusInfo.progress, statusInfo.state);
} catch(error) {
  let code = (error as BusinessError).code;
  let message = (error as BusinessError).message;
  hilog.error(0x0000, 'testTag', `query failed, error code: ${code}, message: ${message}.`);
}
```
