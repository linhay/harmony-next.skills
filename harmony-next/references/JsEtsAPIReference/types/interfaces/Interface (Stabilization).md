# Interface (Stabilization)

Stabilization 继承自 [StabilizationQuery](Interface (StabilizationQuery).md)。

提供设备在录像模式下设置视频防抖的操作。

需要会话中有录像流（[VideoOutput](Interface (VideoOutput).md)）的前提下，才可以对视频进行防抖设置，

其中[VideoStabilizationMode](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002497445814__videostabilizationmode)中的枚举HIGH需要在[Profile](Interfaces (其他).md#ZH-CN_TOPIC_0000002497605794__profile)的分辨率为1920*1080的场景下生效。

- 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
- 本Interface首批接口从API version 11开始支持。

#### 导入模块

```ets
import { camera } from '@kit.CameraKit';
```

#### getActiveVideoStabilizationMode11+

getActiveVideoStabilizationMode(): VideoStabilizationMode

查询当前正在使用的视频防抖模式。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

类型说明[VideoStabilizationMode](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002497445814__videostabilizationmode)视频防抖是否正在使用。若接口调用失败，返回undefined。

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](../../errors/Camera错误码.md)。

错误码ID错误信息7400103Session not config.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function getActiveVideoStabilizationMode(videoSession: camera.VideoSession): camera.VideoStabilizationMode | undefined {
  let vsMode: camera.VideoStabilizationMode | undefined = undefined;
  try {
    vsMode = videoSession.getActiveVideoStabilizationMode();
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`The getActiveVideoStabilizationMode call failed. error code: ${err.code}`);
  }
  return vsMode;
}
```

#### setVideoStabilizationMode11+

setVideoStabilizationMode(mode: VideoStabilizationMode): void

设置视频防抖模式。需要先检查设备是否支持对应的防抖模式，可以通过[isVideoStabilizationModeSupported](Interface (StabilizationQuery).md#ZH-CN_TOPIC_0000002497445810__isvideostabilizationmodesupported11)方法判断所设置的模式是否支持。建议在[commitConfig](Interface (Session).md#ZH-CN_TOPIC_0000002529445753__commitconfig11-1)与[Start](Interface (Session).md#ZH-CN_TOPIC_0000002529445753__start11-1)之间设置视频防抖。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

参数名类型必填说明mode[VideoStabilizationMode](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002497445814__videostabilizationmode)是需要设置的视频防抖模式。

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](../../errors/Camera错误码.md)。

错误码ID错误信息7400103Session not config.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function setVideoStabilizationMode(videoSession: camera.VideoSession): void {
  try {
    videoSession.setVideoStabilizationMode(camera.VideoStabilizationMode.OFF);
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`The setVideoStabilizationMode call failed. error code: ${err.code}`);
  }
}
```