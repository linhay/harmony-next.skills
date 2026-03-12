# Interface (Flash)

Flash 继承自 [FlashQuery](Interface (FlashQuery).md)。

闪光灯类，对设备闪光灯操作。

- 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
- 本Interface首批接口从API version 11开始支持。

#### 导入模块

```ets
import { camera } from '@kit.CameraKit';
```

#### setFlashMode11+

setFlashMode(flashMode: FlashMode): void

设置闪光灯模式。

进行设置之前，需要先检查：

1. 设备是否支持闪光灯，可使用方法[hasFlash](Interface (FlashQuery).md#ZH-CN_TOPIC_0000002497605782__hasflash11)。
1. 设备是否支持指定的闪光灯模式，可使用方法[isFlashModeSupported](Interface (FlashQuery).md#ZH-CN_TOPIC_0000002497605782__isflashmodesupported11)。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

参数名类型必填说明flashMode[FlashMode](Enums.md#ZH-CN_TOPIC_0000002497445814__flashmode)是指定闪光灯模式。传参为null或者undefined，作为0处理，闪光灯关闭。

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](Camera错误码.md)。

错误码ID错误信息7400103Session not config.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function setFlashMode(photoSession: camera.PhotoSession): void {
  try {
    photoSession.setFlashMode(camera.FlashMode.FLASH_MODE_AUTO);
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`The setFlashMode call failed. error code: ${err.code}`);
  }
}
```

#### getFlashMode11+

getFlashMode(): FlashMode

获取当前设备的闪光灯模式。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

类型说明[FlashMode](Enums.md#ZH-CN_TOPIC_0000002497445814__flashmode)获取当前设备的闪光灯模式。接口调用失败会抛出相应错误码并返回undefined，错误码类型[CameraErrorCode](Enums.md#ZH-CN_TOPIC_0000002497445814__cameraerrorcode)。

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](Camera错误码.md)。

错误码ID错误信息7400103Session not config.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function getFlashMode(photoSession: camera.PhotoSession): camera.FlashMode | undefined {
  let flashMode: camera.FlashMode | undefined = undefined;
  try {
    flashMode = photoSession.getFlashMode();
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`The getFlashMode call failed.error code: ${err.code}`);
  }
  return flashMode;
}
```