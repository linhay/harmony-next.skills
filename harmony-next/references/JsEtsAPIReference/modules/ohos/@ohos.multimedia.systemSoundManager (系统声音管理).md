# @ohos.multimedia.systemSoundManager (系统声音管理)

系统声音管理提供管理系统声音的基础能力，包括对系统音效类型的定义、获取系统音效播放器等。

  ![image](public_sys-resources/note_3.0-zh-cn.webp)

本模块首批接口从API version 23开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

**导入模块**

```ets
import { systemSoundManager } from '@kit.AudioKit';
```

**SystemSoundType**

枚举，表示系统音效类型。

模型约束：此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Multimedia.SystemSound.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PHOTO_SHUTTER | 0 | 拍照音效。 |
| VIDEO_RECORDING_BEGIN | 1 | 视频录制开始音效。 |
| VIDEO_RECORDING_END | 2 | 视频录制结束音效。 |

**systemSoundManager.createSystemSoundPlayer**

createSystemSoundPlayer(): Promise<SystemSoundPlayer | null>

创建系统音效播放器对象。使用Promise异步回调。

系统能力： SystemCapability.Multimedia.SystemSound.Core

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<SystemSoundPlayer | null> | 成功返回系统音效播放器对象，失败返回null。 |

错误码：

以下错误码的详细介绍请参见[媒体错误码](Media错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400101 | No memory. Return by promise. |

示例：

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let systemSoundPlayer: systemSoundManager.SystemSoundPlayer | null = null;

systemSoundManager.createSystemSoundPlayer().then((systemSoundPlayerInstance) => {
  console.info('Succeeded in creating the system sound player.');
  systemSoundPlayer = systemSoundPlayerInstance;
}).catch((err: BusinessError) => {
  console.error(`Failed to create the system sound player. Code: ${err.code}, message: ${err.message}`);
});
```

**SystemSoundPlayer**

type SystemSoundPlayer = _SystemSoundPlayer

系统音效播放器对象。

系统能力： SystemCapability.Multimedia.SystemSound.Core

| 类型 | 说明 |
| --- | --- |
| _SystemSoundPlayer | 系统音效播放器对象。 |