# SystemSoundPlayer (音效播放器)

音效播放器提供了加载、卸载和播放系统声音的功能。

SystemSoundPlayer需要和[@ohos.multimedia.systemSoundManager](@ohos.multimedia.systemSoundManager (系统声音管理).md)配合使用，才能完成管理系统音效的功能。

  ![image](public_sys-resources/note_3.0-zh-cn.webp)

本模块首批接口从API version 23开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

**导入模块**

```ets
import { systemSoundManager } from '@kit.AudioKit';
```

**SystemSoundPlayer**

系统音效播放器提供了拍照和录制视频音效的播放功能。在调用SystemSoundPlayer的接口前，需要先通过[createSystemSoundPlayer](@ohos.multimedia.systemSoundManager (系统声音管理).md#ZH-CN_TOPIC_0000002553201787__systemsoundmanagercreatesystemsoundplayer)创建系统音效播放器对象。

**load**

load(soundType: systemSoundManager.SystemSoundType): Promise<void>

加载系统音效。使用Promise异步回调。

模型约束：此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Multimedia.SystemSound.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| soundType | systemSoundManager.SystemSoundType | 是 | 系统音效类型。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

错误码：

以下错误码的详细介绍请参见[媒体服务错误码](Media错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400103 | I/O error. |
| 5400105 | Crash or blocking occurs in system process. |
| 5400108 | Parameter check failed. Returned by promise. |

示例：

```ets
import { BusinessError } from '@kit.BasicServicesKit';

systemSoundPlayer?.load(systemSoundManager.SystemSoundType.PHOTO_SHUTTER).then(() => {
  console.info('Succeeded in calling the load method.');
}).catch((err: BusinessError) => {
  console.error(`Failed to call the load method. Code: ${err.code}, message: ${err.message}`);
});
```

**play**

play(soundType: systemSoundManager.SystemSoundType): Promise<void>

播放系统音效。使用Promise异步回调。

模型约束：此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Multimedia.SystemSound.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| soundType | systemSoundManager.SystemSoundType | 是 | 系统音效类型。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

错误码：

以下错误码的详细介绍请参见[媒体服务错误码](Media错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400103 | I/O error. |
| 5400105 | Crash or blocking occurs in system process. |
| 5400108 | Parameter check failed. Returned by promise. |

示例：

```ets
import { BusinessError } from '@kit.BasicServicesKit';

systemSoundPlayer?.play(systemSoundManager.SystemSoundType.PHOTO_SHUTTER).then(() => {
  console.info('Succeeded in calling the play method.');
}).catch((err: BusinessError) => {
  console.error(`Failed to call the play method. Code: ${err.code}, message: ${err.message}`);
});
```

**unload**

unload(soundType: systemSoundManager.SystemSoundType): Promise<void>

卸载之前已加载的系统音效。使用Promise异步回调。

模型约束：此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Multimedia.SystemSound.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| soundType | systemSoundManager.SystemSoundType | 是 | 系统音效类型。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

错误码：

以下错误码的详细介绍请参见[媒体服务错误码](Media错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400105 | Crash or blocking occurs in system process. |
| 5400108 | Parameter check failed. Returned by promise. |

示例：

```ets
import { BusinessError } from '@kit.BasicServicesKit';

systemSoundPlayer?.unload(systemSoundManager.SystemSoundType.PHOTO_SHUTTER).then(() => {
  console.info('Succeeded in calling the unload method.');
}).catch((err: BusinessError) => {
  console.error(`Failed to call the unload method. Code: ${err.code}, message: ${err.message}`);
});
```

**release**

release(): Promise<void>

释放系统音效播放器。使用Promise异步回调。

模型约束：此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Multimedia.SystemSound.Core

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

错误码：

以下错误码的详细介绍请参见[媒体服务错误码](Media错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400105 | Crash or blocking occurs in system process. |

示例：

```ets
import { BusinessError } from '@kit.BasicServicesKit';

systemSoundPlayer?.release().then(() => {
  console.info('Succeeded in calling the release method.');
}).catch((err: BusinessError) => {
  console.error(`Failed to call the release method. Code: ${err.code}, message: ${err.message}`);
});
```