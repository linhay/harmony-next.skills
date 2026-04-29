# Interface (Flash)

Flash 继承自 [FlashQuery](Interface (FlashQuery).md)。

闪光灯类，对设备闪光灯操作。

- 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
- 本Interface首批接口从API version 11开始支持。

#### 导入模块

```ets
import { camera } from '@kit.CameraKit';
```

#### set[FlashMode](../enums/Enums.md#ZH-CN_TOPIC_0000002497445814__flashmode)11+

set[FlashMode](../enums/Enums.md#ZH-CN_TOPIC_0000002497445814__flashmode)(flashMode: FlashMode): void

设置闪光灯模式。

进行设置之前，需要先检查：

1. 设备是否支持闪光灯，可使用方法[hasFlash](Interface (FlashQuery).md#ZH-CN_TOPIC_0000002522081912__hasflash11)。

1. 设备是否支持指定的闪光灯模式，可使用方法[isFlashModeSupported](Interface (FlashQuery).md#ZH-CN_TOPIC_0000002522081912__isflashmodesupported11)。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| flashMode | [FlashMode](../enums/Enums.md#ZH-CN_TOPIC_0000002497445814__flashmode) | 是 | 指定闪光灯模式。传参为null或者undefined，作为0处理，闪光灯关闭。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码]([Camera错误码](../../errors/Camera错误码.md).md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400103 | Session not config. |

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
```

#### get[FlashMode](../enums/Enums.md#ZH-CN_TOPIC_0000002497445814__flashmode)11+

get[FlashMode](../enums/Enums.md#ZH-CN_TOPIC_0000002497445814__flashmode)(): FlashMode

获取当前设备的闪光灯模式。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [FlashMode](../enums/Enums.md#ZH-CN_TOPIC_0000002497445814__flashmode) | 获取当前设备的闪光灯模式。接口调用失败会抛出相应错误码并返回undefined，错误码类型[CameraErrorCode](../enums/Enums.md#ZH-CN_TOPIC_0000002497445814__cameraerrorcode)。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](Camera错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400103 | Session not config. |

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