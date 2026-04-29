# Interface (AVScreenCaptureRecorder)

屏幕录制管理类，用于进行屏幕录制。在调用AVScreenCaptureRecorder的方法前，需要先通过[createAVScreenCaptureRecorder()](Functions.md#ZH-CN_TOPIC_0000002522082030__mediacreateavscreencapturerecorder12)创建一个AVScreenCaptureRecorder实例。


- 本模块首批接口从API version 6开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
- 本Interface首批接口从API version 12开始支持。

#### 导入模块

```ets
import { media } from '@kit.MediaKit';
```

#### init12+

init(config: AVScreenCaptureRecordConfig): Promise<void>

进行录屏初始化，设置录屏参数。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| config | AVScreenCaptureRecordConfig | 是 | 配置屏幕录制的相关参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)和[Media错误码]([Media错误码](../../errors/Media错误码.md).md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. Return by promise. |
| 5400103 | IO error. Return by promise. |
| 5400105 | Service died. Return by promise. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo as fs } from '@kit.CoreFileKit';
import { media } from '@kit.MediaKit';

// 初始化avScreenCaptureRecorder。
let avScreenCaptureRecorder: media.AVScreenCaptureRecorder | undefined;
media.createAVScreenCaptureRecorder().then((captureRecorder: media.AVScreenCaptureRecorder) => {
  if (captureRecorder != null) {
    avScreenCaptureRecorder = captureRecorder;
    console.info('Succeeded in createAVScreenCaptureRecorder');
  } else {
    console.error('Failed to createAVScreenCaptureRecorder');
  }
}).catch((error: BusinessError) => {
  console.error(`createAVScreenCaptureRecorder catchCallback, error message:${error.message}`);
});

// 创建文件。
let filesDir = '/data/storage/el2/base/haps';
let file = fs.openSync(filesDir + '/screenCapture.mp4', fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);

let avCaptureConfig: media.AVScreenCaptureRecordConfig = {
    fd: file.fd, // 文件需要先由调用者创建，通常是MP4文件，赋予写权限，将文件fd传给此参数。
    frameWidth: 640,
    frameHeight: 480
    // 补充其他参数。
};

if (avScreenCaptureRecorder != undefined) {
avScreenCaptureRecorder.init(avCaptureConfig).then(() => {
    console.info('Succeeded in initializing avScreenCaptureRecorder');
}).catch((err: BusinessError) => {
    console.error(`Failed to init avScreenCaptureRecorder. Code: ${err.code}, message: ${err.message}`);
});
}
```

#### startRecording12+

startRecording(): Promise<void>

开始录屏，在使用前需要先调用[init](Interface (AVScreenCaptureRecorder).md#ZH-CN_TOPIC_0000002553361953__init12)接口。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[Media错误码](Media错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400103 | IO error. Return by promise. |
| 5400105 | Service died. Return by promise. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

avScreenCaptureRecorder.startRecording().then(() => {
    console.info('Succeeded in starting avScreenCaptureRecorder');
}).catch((err: BusinessError) => {
    console.error(`Failed to start avScreenCaptureRecorder. Code: ${err.code}, message: ${err.message}`);
});
```

#### stopRecording12+

stopRecording(): Promise<void>

结束录屏。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[Media错误码](Media错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400103 | IO error. Return by promise. |
| 5400105 | Service died. Return by promise. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

avScreenCaptureRecorder.stopRecording().then(() => {
    console.info('Succeeded in stopping avScreenCaptureRecorder');
}).catch((err: BusinessError) => {
    console.error(`Failed to stop avScreenCaptureRecorder. Code: ${err.code}, message: ${err.message}`);
});
```

#### skipPrivacyMode12+

skipPrivacyMode(windowIDs: Array<number>): Promise<void>

录屏时，应用可对本应用的隐私窗口做安全豁免。使用Promise异步回调。

如录屏时，用户在本应用进行输入密码等操作，应用不会进行黑屏处理。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| windowIDs | Array<number> | 是 | 需要豁免隐私的窗口列表，包括主窗口id和子窗口id，窗口属性获取方法可以参考getWindowProperties。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[Media错误码](Media错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400103 | IO error. Return by promise. |
| 5400105 | Service died. Return by promise. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let windowIDs = [];
avScreenCaptureRecorder.skipPrivacyMode(windowIDs).then(() => {
    console.info('Succeeded in skipping privacy mode');
}).catch((err: BusinessError) => {
    console.error(`Failed to skip privacy mode. Code: ${err.code}, message: ${err.message}`);
});
```

#### setMicEnabled12+

setMicEnabled(enable: boolean): Promise<void>

设置麦克风开关。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | boolean | 是 | 麦克风开关控制，true代表麦克风打开，false代表麦克风关闭。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[Media错误码](Media错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400103 | IO error. Return by promise. |
| 5400105 | Service died. Return by promise. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

avScreenCaptureRecorder.setMicEnabled(true).then(() => {
  console.info('Succeeded in setting microphone enabled.');
}).catch((err: BusinessError) => {
  console.error(`Failed to set microphone enabled. Code: ${err.code}, message: ${err.message}`);
});
```

#### set[PickerMode](../enums/Enums.md#ZH-CN_TOPIC_0000002497445922__pickermode22)22+

set[PickerMode](../enums/Enums.md#ZH-CN_TOPIC_0000002497445922__pickermode22)(pickerMode: PickerMode): Promise<void>

设置Picker显示模式，在下一次显示Picker时生效。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pickerMode | [PickerMode](../enums/Enums.md#ZH-CN_TOPIC_0000002497445922__pickermode22) | 是 | 选择Picker模式。 定义了在Picker中显示的内容类型： - SCREEN_ONLY：仅显示屏幕列表。 - WINDOW_ONLY：仅显示窗口列表。 - SCREEN_AND_WINDOW：同时显示屏幕列表和窗口列表（默认值）。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[Media错误码](Media错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400102 | Operation not allowed. Return by promise. |
| 5400103 | IO error. Return by promise. |
| 5400105 | Service died. Return by promise. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

avScreenCaptureRecorder.setPickerMode(media.PickerMode.WINDOW_ONLY).then(() => {
  console.info('Succeeded in setting picker mode.');
}).catch((err: BusinessError) => {
  console.error(`Failed to set picker mode. Code: ${err.code}, message: ${err.message}`);
});
```

#### excludePickerWindows22+

excludePickerWindows(excludedWindows: Array<number>): Promise<void>

设置在Picker中隐藏的窗口列表，在下一次显示Picker时生效。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| excludedWindows | Array<number> | 是 | 需要在Picker中隐藏的窗口列表，窗口属性获取方法可以参考getWindowProperties。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[Media错误码](Media错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400102 | Operation not allowed. Return by promise. |
| 5400103 | IO error. Return by promise. |
| 5400105 | Service died. Return by promise. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let excludedWindows: Array<number> = [101, 102, 103];

avScreenCaptureRecorder.excludePickerWindows(excludedWindows).then(() => {
  console.info('Succeeded in excluding picker windows.');
}).catch((err: BusinessError) => {
  console.error(`Failed to exclude picker windows. Code: ${err.code}, message: ${err.message}`);
});
```

#### presentPicker22+

presentPicker(): Promise<void>

录屏开始后，调用该接口再次弹出Picker，可动态更新录制源（窗口、屏幕）。使用Promise异步回调。

- 更新录制源过程中，原录制流程不中断。
- 通过picker动态更新录制源后，按照新的录制源进行录制。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[Media错误码](Media错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400102 | Operation not allowed. Return by promise. |
| 5400103 | IO error. Return by promise. |
| 5400105 | Service died. Return by promise. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

avScreenCaptureRecorder.presentPicker().then(() => {
  console.info('Succeeded in presenting picker avScreenCaptureRecorder.');
}).catch((err: BusinessError) => {
  console.error(`Failed to present picker avScreenCaptureRecorder. Code: ${err.code}, message: ${err.message}`);
});
```

#### release12+

release(): Promise<void>

释放录屏。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[Media错误码](Media错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400103 | IO error. Return by promise. |
| 5400105 | Service died. Return by promise. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

avScreenCaptureRecorder.release().then(() => {
    console.info('Succeeded in releasing avScreenCaptureRecorder');
}).catch((err: BusinessError) => {
    console.error(`Failed to release avScreenCaptureRecorder. Code: ${err.code}, message: ${err.message}`);
});
```

#### on('stateChange')12+

on(type: 'stateChange', callback: Callback<[AVScreenCaptureStateCode](../enums/Enums.md#ZH-CN_TOPIC_0000002497445922__avscreencapturestatecode12)>): void

订阅录屏状态切换的事件，当状态发生的时候，会通过订阅的回调通知用户。用户只能订阅一个状态切换的回调方法，重复订阅时，以最后一次订阅的回调接口为准。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 状态切换事件回调类型，支持的事件：'stateChange'。 |
| callback | Callback<[AVScreenCaptureStateCode](../enums/Enums.md#ZH-CN_TOPIC_0000002497445922__avscreencapturestatecode12)> | 是 | 状态切换事件回调方法，AVScreenCaptureStateCode表示切换到的状态。 |

**示例：**

```ets
avScreenCaptureRecorder.on('stateChange', (state: media.AVScreenCaptureStateCode) => {
    console.info('avScreenCaptureRecorder stateChange to ' + state);
});
```

#### on('error')12+

on(type: 'error', callback: ErrorCallback): void

订阅AVScreenCaptureRecorder的错误事件，用户可以根据应用自身逻辑对错误事件进行处理。用户只能订阅一个错误事件的回调方法，重复订阅时，以最后一次订阅的回调接口为准。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 错误事件回调类型，支持的事件：'error'。 |
| callback | ErrorCallback | 是 | 录屏错误事件回调方法。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)和[Media错误码](Media错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | permission denied. |
| 5400103 | IO error. Return by ErrorCallback. |
| 5400105 | Service died. Return by ErrorCallback. |

**示例：**

```ets
avScreenCaptureRecorder.on('error', (err: BusinessError) => {
    console.error(`avScreenCaptureRecorder error: Code: ${err.code}, message: ${err.message}`);
});
```

#### off('stateChange')12+

 off(type: 'stateChange', callback?: Callback<[AVScreenCaptureStateCode](../enums/Enums.md#ZH-CN_TOPIC_0000002497445922__avscreencapturestatecode12)>): void

取消订阅状态切换回调事件。用户可以指定填入状态切换的回调方法来取消订阅。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 状态切换事件回调类型，支持的事件：'stateChange'。 |
| callback | Callback<[AVScreenCaptureStateCode](../enums/Enums.md#ZH-CN_TOPIC_0000002497445922__avscreencapturestatecode12)> | 否 | 状态切换事件回调方法，AVScreenCaptureStateCode表示切换到的状态，不填此参数则会取消最后一次订阅事件。 |

**示例：**

```ets
avScreenCaptureRecorder.off('stateChange');
```

#### off('error')12+

off(type: 'error', callback?: ErrorCallback): void

取消订阅错误回调事件。用户可以指定填入错误回调方法来取消订阅。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 状态切换事件回调类型，支持的事件：'error'。 |
| callback | ErrorCallback | 否 | 录屏错误事件回调方法，不填此参数则会取消最后一次订阅事件。 |

**示例：**

```ets
avScreenCaptureRecorder.off('error');
```