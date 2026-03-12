# 废弃的Interface (CaptureSession, deprecated)

拍照会话类，保存一次相机运行所需要的所有资源[CameraInput](Interface (CameraInput).md)、[CameraOutput](Interface (CameraOutput).md)，并向相机设备申请完成相机功能(录像，拍照)。

从 API version 10开始支持，从API version 11开始废弃。建议使用[PhotoSession](Interface (PhotoSession).md)、[VideoSession](Interface (VideoSession).md)替代。

#### 导入模块

```ets
import { camera } from '@kit.CameraKit';
```

#### beginConfig(deprecated)

beginConfig(): void

开始配置会话。

从 API version 10开始支持，从API version 11开始废弃。建议使用[Session.beginConfig](Interface (Session).md#ZH-CN_TOPIC_0000002529445753__beginconfig11)替代。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](Camera错误码.md)。

错误码ID错误信息7400105Session config locked.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function beginConfig(captureSession: camera.CaptureSession): void {
  try {
    captureSession.beginConfig();
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`The beginConfig call failed. error code: ${err.code}`);
  }
}
```

#### commitConfig(deprecated)

commitConfig(callback: AsyncCallback<void>): void

提交配置信息，通过注册回调函数获取结果。使用callback异步回调。

从 API version 10开始支持，从API version 11开始废弃。建议使用[Session.commitConfig](Interface (Session).md#ZH-CN_TOPIC_0000002529445753__commitconfig11)替代。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

参数名类型必填说明callbackAsyncCallback<void>是回调函数。当提交配置信息成功，err为undefined，否则为错误对象。错误码类型[CameraErrorCode](Enums.md#ZH-CN_TOPIC_0000002497445814__cameraerrorcode)

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](Camera错误码.md)。

错误码ID错误信息7400102Operation not allowed.7400201Camera service fatal error.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function commitConfig(captureSession: camera.CaptureSession): void {
  captureSession.commitConfig((err: BusinessError) => {
    if (err) {
      console.error(`The commitConfig call failed. error code: ${err.code}`);
      return;
    }
    console.info('Callback invoked to indicate the commit config success.');
  });
}
```

#### commitConfig(deprecated)

commitConfig(): Promise<void>

提交配置信息。使用Promise异步回调。

从 API version 10开始支持，从API version 11开始废弃。建议使用[Session.commitConfig](Interface (Session).md#ZH-CN_TOPIC_0000002529445753__commitconfig11-1)替代。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

类型说明Promise<void>Promise对象，无返回结果。

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](Camera错误码.md)。

错误码ID错误信息7400102Operation not allowed.7400201Camera service fatal error.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function commitConfig(captureSession: camera.CaptureSession): void {
  captureSession.commitConfig().then(() => {
    console.info('Promise returned to indicate the commit config success.');
  }).catch((error: BusinessError) => {
    // 失败返回错误码error.code并处理。
    console.error(`The commitConfig call failed. error code: ${error.code}`);
  });
}
```

#### addInput(deprecated)

addInput(cameraInput: CameraInput): void

把[CameraInput](Interface (CameraInput).md)加入到会话。

从 API version 10开始支持，从API version 11开始废弃。建议使用[Session.addInput](Interface (Session).md#ZH-CN_TOPIC_0000002529445753__addinput11)替代。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

参数名类型必填说明cameraInput[CameraInput](Interface (CameraInput).md)是需要添加的CameraInput实例。

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](Camera错误码.md)。

错误码ID错误信息7400101Parameter missing or parameter type incorrect.7400102Operation not allowed.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function addInput(captureSession: camera.CaptureSession, cameraInput: camera.CameraInput): void {
  try {
    captureSession.addInput(cameraInput);
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`The addInput call failed. error code: ${err.code}`);
  }
}
```

#### removeInput(deprecated)

removeInput(cameraInput: CameraInput): void

移除[CameraInput](Interface (CameraInput).md)。

从 API version 10开始支持，从API version 11开始废弃。建议使用[Session.removeInput](Interface (Session).md#ZH-CN_TOPIC_0000002529445753__removeinput11)替代。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

参数名类型必填说明cameraInput[CameraInput](Interface (CameraInput).md)是需要移除的CameraInput实例。

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](Camera错误码.md)。

错误码ID错误信息7400101Parameter missing or parameter type incorrect.7400102Operation not allowed.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function removeInput(captureSession: camera.CaptureSession, cameraInput: camera.CameraInput): void {
  try {
    captureSession.removeInput(cameraInput);
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`The removeInput call failed. error code: ${err.code}`);
  }
}
```

#### addOutput(deprecated)

addOutput(cameraOutput: CameraOutput): void

把[CameraOutput](Interface (CameraOutput).md)加入到会话。

从 API version 10开始支持，从API version 11开始废弃。建议使用[Session.addOutput](Interface (Session).md#ZH-CN_TOPIC_0000002529445753__addoutput11)替代。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

参数名类型必填说明cameraOutput[CameraOutput](Interface (CameraOutput).md)是需要添加的CameraOutput实例。

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](Camera错误码.md)。

错误码ID错误信息7400101Parameter missing or parameter type incorrect.7400102Operation not allowed.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function addOutput(captureSession: camera.CaptureSession, cameraOutput: camera.CameraOutput): void {
  try {
    captureSession.addOutput(cameraOutput);
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`The addOutput call failed. error code: ${err.code}`);
  }
}
```

#### removeOutput(deprecated)

removeOutput(cameraOutput: CameraOutput): void

从会话中移除[CameraOutput](Interface (CameraOutput).md)。

从 API version 10开始支持，从API version 11开始废弃。建议使用[Session.removeOutput](Interface (Session).md#ZH-CN_TOPIC_0000002529445753__removeoutput11)替代。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

参数名类型必填说明cameraOutput[CameraOutput](Interface (CameraOutput).md)是需要移除的CameraOutput实例。

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](Camera错误码.md)。

错误码ID错误信息7400101Parameter missing or parameter type incorrect.7400102Operation not allowed.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function removeOutput(captureSession: camera.CaptureSession, previewOutput: camera.PreviewOutput): void {
  try {
    captureSession.removeOutput(previewOutput);
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`The removeOutput call failed. error code: ${err.code}`);
  }
}
```

#### start(deprecated)

start(callback: AsyncCallback<void>): void

开始会话工作，通过注册回调函数获取结果。使用callback异步回调。

从 API version 10开始支持，从API version 11开始废弃。建议使用[Session.start](Interface (Session).md#ZH-CN_TOPIC_0000002529445753__start11)替代。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

参数名类型必填说明callbackAsyncCallback<void>是回调函数。当开始会话工作成功，err为undefined，否则为错误对象。错误码类型[CameraErrorCode](Enums.md#ZH-CN_TOPIC_0000002497445814__cameraerrorcode)。

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](Camera错误码.md)。

错误码ID错误信息7400103Session not config.7400201Camera service fatal error.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function startCaptureSession(captureSession: camera.CaptureSession): void {
  captureSession.start((err: BusinessError) => {
    if (err) {
      console.error(`Failed to start the session, error code: ${err.code}.`);
      return;
    }
    console.info('Callback invoked to indicate the session start success.');
  });
}
```

#### start(deprecated)

start(): Promise<void>

开始会话工作。使用Promise异步回调。

从 API version 10开始支持，从API version 11开始废弃。建议使用[Session.start](Interface (Session).md#ZH-CN_TOPIC_0000002529445753__start11-1)替代。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

类型说明Promise<void>Promise对象，无返回结果。

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](Camera错误码.md)。

错误码ID错误信息7400103Session not config.7400201Camera service fatal error.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function startCaptureSession(captureSession: camera.CaptureSession): void {
  captureSession.start().then(() => {
    console.info('Promise returned to indicate the session start success.');
  }).catch((err: BusinessError) => {
    console.error(`Failed to start the session, error code: ${err.code}.`);
  });
}
```

#### stop(deprecated)

stop(callback: AsyncCallback<void>): void

停止会话工作，通过注册回调函数获取结果。使用callback异步回调。

从 API version 10开始支持，从API version 11开始废弃。建议使用[Session.stop](Interface (Session).md#ZH-CN_TOPIC_0000002529445753__stop11)替代。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

参数名类型必填说明callbackAsyncCallback<void>是回调函数。当停止会话工作成功，err为undefined，否则为错误对象。错误码类型[CameraErrorCode](Enums.md#ZH-CN_TOPIC_0000002497445814__cameraerrorcode)。

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](Camera错误码.md)。

错误码ID错误信息7400201Camera service fatal error.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function stopCaptureSession(captureSession: camera.CaptureSession): void {
  captureSession.stop((err: BusinessError) => {
    if (err) {
      console.error(`Failed to stop the session, error code: ${err.code}.`);
      return;
    }
    console.info('Callback invoked to indicate the session stop success.');
  });
}
```

#### stop(deprecated)

stop(): Promise<void>

停止会话工作。使用Promise异步回调。

从 API version 10开始支持，从API version 11开始废弃。建议使用[Session.stop](Interface (Session).md#ZH-CN_TOPIC_0000002529445753__stop11-1)替代。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

类型说明Promise<void>Promise对象，无返回结果。

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](Camera错误码.md)。

错误码ID错误信息7400201Camera service fatal error.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function stopCaptureSession(captureSession: camera.CaptureSession): void {
  captureSession.stop().then(() => {
    console.info('Promise returned to indicate the session stop success.');
  }).catch((err: BusinessError) => {
    console.error(`Failed to stop the session, error code: ${err.code}.`);
  });
}
```

#### release(deprecated)

release(callback: AsyncCallback<void>): void

释放会话资源，通过注册回调函数获取结果。使用callback异步回调。

从 API version 10开始支持，从API version 11开始废弃。建议使用[Session.release](Interface (Session).md#ZH-CN_TOPIC_0000002529445753__release11)替代。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

参数名类型必填说明callbackAsyncCallback<void>是回调函数。当释放会话资源成功，err为undefined，否则为错误对象。错误码类型[CameraErrorCode](Enums.md#ZH-CN_TOPIC_0000002497445814__cameraerrorcode)。

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](Camera错误码.md)。

错误码ID错误信息7400201Camera service fatal error.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function releaseCaptureSession(captureSession: camera.CaptureSession): void {
  captureSession.release((err: BusinessError) => {
    if (err) {
      console.error(`Failed to release the CaptureSession instance, error code: ${err.code}.`);
      return;
    }
    console.info('Callback invoked to indicate that the CaptureSession instance is released successfully.');
  });
}
```

#### release(deprecated)

release(): Promise<void>

释放会话资源。使用Promise异步回调。

从 API version 10开始支持，从API version 11开始废弃。建议使用[Session.release](Interface (Session).md#ZH-CN_TOPIC_0000002529445753__release11-1)替代。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

类型说明Promise<void>Promise对象，无返回结果。

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](Camera错误码.md)。

错误码ID错误信息7400201Camera service fatal error.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function releaseCaptureSession(captureSession: camera.CaptureSession): void {
  captureSession.release().then(() => {
    console.info('Promise returned to indicate that the CaptureSession instance is released successfully.');
  }).catch((err: BusinessError) => {
    console.error(`Failed to release the CaptureSession instance, error code: ${err.code}.`);
  });
}
```

#### hasFlash(deprecated)

hasFlash(): boolean

检测是否有闪光灯。

从 API version 10开始支持，从API version 11开始废弃。建议使用[Flash.hasFlash](Interface (FlashQuery).md#ZH-CN_TOPIC_0000002497605782__hasflash11)替代。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

类型说明boolean设备支持闪光灯。true表示支持，false表示不支持。接口调用失败会返回相应错误码，错误码类型[CameraErrorCode](Enums.md#ZH-CN_TOPIC_0000002497445814__cameraerrorcode)。

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](Camera错误码.md)。

错误码ID错误信息7400103Session not config.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function hasFlash(captureSession: camera.CaptureSession): boolean {
  let status: boolean = false;
  try {
    status = captureSession.hasFlash();
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`The hasFlash call failed. error code: ${err.code}`);
  }
  return status;
}
```

#### isFlashModeSupported(deprecated)

isFlashModeSupported(flashMode: FlashMode): boolean

检测闪光灯模式是否支持。

从 API version 10开始支持，从API version 11开始废弃。建议使用[Flash.isFlashModeSupported](Interface (FlashQuery).md#ZH-CN_TOPIC_0000002497605782__isflashmodesupported11)替代。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

参数名类型必填说明flashMode[FlashMode](Enums.md#ZH-CN_TOPIC_0000002497445814__flashmode)是指定闪光灯模式。

**返回值：**

类型说明boolean检测闪光灯模式是否支持。true表示支持，false表示不支持。接口调用失败会返回相应错误码，错误码类型[CameraErrorCode](Enums.md#ZH-CN_TOPIC_0000002497445814__cameraerrorcode)。

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](Camera错误码.md)。

错误码ID错误信息7400103Session not config.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function isFlashModeSupported(captureSession: camera.CaptureSession): boolean {
  let status: boolean = false;
  try {
    status = captureSession.isFlashModeSupported(camera.FlashMode.FLASH_MODE_AUTO);
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`The isFlashModeSupported call failed. error code: ${err.code}`);
  }
  return status;
}
```

#### setFlashMode(deprecated)

setFlashMode(flashMode: FlashMode): void

设置闪光灯模式。

进行设置之前，需要先检查：

1. 设备是否支持闪光灯，可使用方法[hasFlash](#ZH-CN_TOPIC_0000002529285785__hasflashdeprecated)。
1. 设备是否支持指定的闪光灯模式，可使用方法[isFlashModeSupported](#ZH-CN_TOPIC_0000002529285785__isflashmodesupporteddeprecated)。

从 API version 10开始支持，从API version 11开始废弃。建议使用[Flash.setFlashMode](Interface (Flash).md#ZH-CN_TOPIC_0000002529445747__setflashmode11)替代。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

参数名类型必填说明flashMode[FlashMode](Enums.md#ZH-CN_TOPIC_0000002497445814__flashmode)是指定闪光灯模式。

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](Camera错误码.md)。

错误码ID错误信息7400103Session not config.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function setFlashMode(captureSession: camera.CaptureSession): void {
  try {
    captureSession.setFlashMode(camera.FlashMode.FLASH_MODE_AUTO);
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`The setFlashMode call failed. error code: ${err.code}`);
  }
}
```

#### getFlashMode(deprecated)

getFlashMode(): FlashMode

获取当前设备的闪光灯模式。

从 API version 10开始支持，从API version 11开始废弃。建议使用[Flash.getFlashMode](Interface (Flash).md#ZH-CN_TOPIC_0000002529445747__getflashmode11)替代。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

类型说明[FlashMode](Enums.md#ZH-CN_TOPIC_0000002497445814__flashmode)获取当前设备的闪光灯模式。接口调用失败会返回相应错误码，错误码类型[CameraErrorCode](Enums.md#ZH-CN_TOPIC_0000002497445814__cameraerrorcode)。

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](Camera错误码.md)。

错误码ID错误信息7400103Session not config.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function getFlashMode(captureSession: camera.CaptureSession): camera.FlashMode | undefined {
  let flashMode: camera.FlashMode | undefined = undefined;
  try {
    flashMode = captureSession.getFlashMode();
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`The getFlashMode call failed.error code: ${err.code}`);
  }
  return flashMode;
}
```

#### isExposureModeSupported(deprecated)

isExposureModeSupported(aeMode: ExposureMode): boolean

查询曝光模式是否支持。

从 API version 10开始支持，从API version 11开始废弃。建议使用[AutoExposure.isExposureModeSupported](Interface (AutoExposureQuery).md#ZH-CN_TOPIC_0000002529445743__isexposuremodesupported11)替代。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

参数名类型必填说明aeMode[ExposureMode](Enums.md#ZH-CN_TOPIC_0000002497445814__exposuremode)是曝光模式。

**返回值：**

类型说明boolean获取是否支持曝光模式。true表示支持，false表示不支持。接口调用失败会返回相应错误码，错误码类型[CameraErrorCode](Enums.md#ZH-CN_TOPIC_0000002497445814__cameraerrorcode)。

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](Camera错误码.md)。

错误码ID错误信息7400103Session not config.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function isExposureModeSupported(captureSession: camera.CaptureSession): boolean {
  let isSupported: boolean = false;
  try {
    isSupported = captureSession.isExposureModeSupported(camera.ExposureMode.EXPOSURE_MODE_LOCKED);
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`The isExposureModeSupported call failed. error code: ${err.code}`);
  }
  return isSupported;
}
```

#### getExposureMode(deprecated)

getExposureMode(): ExposureMode

获取当前曝光模式。

从 API version 10开始支持，从API version 11开始废弃。建议使用[AutoExposure.getExposureMode](Interface (AutoExposure).md#ZH-CN_TOPIC_0000002529285769__getexposuremode11)替代。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

类型说明[ExposureMode](Enums.md#ZH-CN_TOPIC_0000002497445814__exposuremode)获取当前曝光模式。接口调用失败会返回相应错误码，错误码类型[CameraErrorCode](Enums.md#ZH-CN_TOPIC_0000002497445814__cameraerrorcode)。

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](Camera错误码.md)。

错误码ID错误信息7400103Session not config.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function getExposureMode(captureSession: camera.CaptureSession): camera.ExposureMode | undefined {
  let exposureMode: camera.ExposureMode | undefined = undefined;
  try {
    exposureMode = captureSession.getExposureMode();
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`The getExposureMode call failed. error code: ${err.code}`);
  }
  return exposureMode;
}
```

#### setExposureMode(deprecated)

setExposureMode(aeMode: ExposureMode): void

设置曝光模式。进行设置之前，需要先检查设备是否支持指定的曝光模式，可使用方法[isExposureModeSupported](#ZH-CN_TOPIC_0000002529285785__isexposuremodesupporteddeprecated)。

从 API version 10开始支持，从API version 11开始废弃。建议使用[AutoExposure.setExposureMode](Interface (AutoExposure).md#ZH-CN_TOPIC_0000002529285769__setexposuremode11)替代。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

参数名类型必填说明aeMode[ExposureMode](Enums.md#ZH-CN_TOPIC_0000002497445814__exposuremode)是曝光模式。

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](Camera错误码.md)。

错误码ID错误信息7400103Session not config.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function setExposureMode(captureSession: camera.CaptureSession): void {
  try {
    captureSession.setExposureMode(camera.ExposureMode.EXPOSURE_MODE_LOCKED);
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`The setExposureMode call failed. error code: ${err.code}`);
  }
}
```

#### getMeteringPoint(deprecated)

getMeteringPoint(): Point

查询曝光区域中心点。

从 API version 10开始支持，从API version 11开始废弃。建议使用[AutoExposure.getMeteringPoint](Interface (AutoExposure).md#ZH-CN_TOPIC_0000002529285769__getmeteringpoint11)替代。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

类型说明[Point](Interfaces (其他).md#ZH-CN_TOPIC_0000002497605794__point)获取当前曝光点。接口调用失败会返回相应错误码，错误码类型[CameraErrorCode](Enums.md#ZH-CN_TOPIC_0000002497445814__cameraerrorcode)。

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](Camera错误码.md)。

错误码ID错误信息7400103Session not config.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function getMeteringPoint(captureSession: camera.CaptureSession): camera.Point | undefined {
  let exposurePoint: camera.Point | undefined = undefined;
  try {
    exposurePoint = captureSession.getMeteringPoint();
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`The getMeteringPoint call failed. error code: ${err.code}`);
  }
  return exposurePoint;
}
```

#### setMeteringPoint(deprecated)

setMeteringPoint(point: Point): void

设置曝光区域中心点，曝光点应位于0-1坐标系内，该坐标系左上角为{0，0}，右下角为{1，1}。

此坐标系是以设备充电口在右侧时的横向设备方向为基准的，例如应用的预览界面布局以

设备充电口在下侧时的竖向方向为基准，布局宽高为{w，h}，且触碰点为{x，y}，

则转换后的坐标点为{y/h，1-x/w}。

从 API version 10开始支持，从API version 11开始废弃。建议使用[AutoExposure.setMeteringPoint](Interface (AutoExposure).md#ZH-CN_TOPIC_0000002529285769__setmeteringpoint11)替代。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

参数名类型必填说明point[Point](Interfaces (其他).md#ZH-CN_TOPIC_0000002497605794__point)是曝光点，x,y设置范围应在[0,1]之内，超过范围，如果小于0设置0，大于1设置1。

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](Camera错误码.md)。

错误码ID错误信息7400103Session not config.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function setMeteringPoint(captureSession: camera.CaptureSession): void {
  const point: camera.Point = {x: 1, y: 1};
  try {
    captureSession.setMeteringPoint(point);
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`The setMeteringPoint call failed. error code: ${err.code}`);
  }
}
```

#### getExposureBiasRange(deprecated)

getExposureBiasRange(): Array<number>

查询曝光补偿范围。

从 API version 10开始支持，从API version 11开始废弃。建议使用[AutoExposure.getExposureBiasRange](Interface (AutoExposureQuery).md#ZH-CN_TOPIC_0000002529445743__getexposurebiasrange11)替代。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

类型说明Array<number>获取补偿范围的数组。接口调用失败会返回相应错误码，错误码类型[CameraErrorCode](Enums.md#ZH-CN_TOPIC_0000002497445814__cameraerrorcode)。

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](Camera错误码.md)。

错误码ID错误信息7400103Session not config.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function getExposureBiasRange(captureSession: camera.CaptureSession): Array<number> {
  let biasRangeArray: Array<number> = [];
  try {
    biasRangeArray = captureSession.getExposureBiasRange();
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`The getExposureBiasRange call failed. error code: ${err.code}`);
  }
  return biasRangeArray;
}
```

#### setExposureBias(deprecated)

setExposureBias(exposureBias: number): void

设置曝光补偿，曝光补偿值（EV）。

进行设置之前，建议先通过方法[getExposureBiasRange](#ZH-CN_TOPIC_0000002529285785__getexposurebiasrangedeprecated)查询支持的范围。

从 API version 10开始支持，从API version 11开始废弃。建议使用[AutoExposure.setExposureBias](Interface (AutoExposure).md#ZH-CN_TOPIC_0000002529285769__setexposurebias11)替代。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

参数名类型必填说明exposureBiasnumber是曝光补偿，[getExposureBiasRange](Interface (AutoExposureQuery).md#ZH-CN_TOPIC_0000002529445743__getexposurebiasrange11)查询支持的范围，如果设置超过支持范围的值，自动匹配到就近临界点。曝光补偿存在步长，如步长为0.5。则设置1.2时，获取到实际生效曝光补偿为1.0。接口调用失败会返回相应错误码，错误码类型[CameraErrorCode](Enums.md#ZH-CN_TOPIC_0000002497445814__cameraerrorcode)。传参为null或者undefined，作为0处理，曝光补偿设置0。

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](Camera错误码.md)。

错误码ID错误信息7400103Session not config.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function setExposureBias(captureSession: camera.CaptureSession, biasRangeArray: Array<number>): void {
  if (biasRangeArray && biasRangeArray.length > 0) {
    let exposureBias = biasRangeArray[0];
    try {
      captureSession.setExposureBias(exposureBias);
    } catch (error) {
      // 失败返回错误码error.code并处理。
      let err = error as BusinessError;
      console.error(`The setExposureBias call failed. error code: ${err.code}`);
    }
  }
}
```

#### getExposureValue(deprecated)

getExposureValue(): number

查询当前的曝光值。

从 API version 10开始支持，从API version 11开始废弃。建议使用[AutoExposure.getExposureValue](Interface (AutoExposure).md#ZH-CN_TOPIC_0000002529285769__getexposurevalue11)替代。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

类型说明number获取曝光值。曝光补偿存在步长，如步长为0.5。则设置1.2时，获取到实际生效曝光补偿为1.0。接口调用失败会返回相应错误码，错误码类型[CameraErrorCode](Enums.md#ZH-CN_TOPIC_0000002497445814__cameraerrorcode)。

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](Camera错误码.md)。

错误码ID错误信息7400103Session not config.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function getExposureValue(captureSession: camera.CaptureSession): number {
  const invalidValue: number = -1;
  let exposureValue: number = invalidValue;
  try {
    exposureValue = captureSession.getExposureValue();
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`The getExposureValue call failed. error code: ${err.code}`);
  }
  return exposureValue;
}
```

#### isFocusModeSupported(deprecated)

isFocusModeSupported(afMode: FocusMode): boolean

查询对焦模式是否支持。

从 API version 10开始支持，从API version 11开始废弃。建议使用[Focus.isFocusModeSupported](Interface (FocusQuery).md#ZH-CN_TOPIC_0000002529285775__isfocusmodesupported11)替代。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

参数名类型必填说明afMode[FocusMode](Enums.md#ZH-CN_TOPIC_0000002497445814__focusmode)是指定的焦距模式。

**返回值：**

类型说明boolean检测对焦模式是否支持。true表示支持，false表示不支持。接口调用失败会返回相应错误码，错误码类型[CameraErrorCode](Enums.md#ZH-CN_TOPIC_0000002497445814__cameraerrorcode)。

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](Camera错误码.md)。

错误码ID错误信息7400103Session not config.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function isFocusModeSupported(captureSession: camera.CaptureSession): boolean {
  let status: boolean = false;
  try {
    status = captureSession.isFocusModeSupported(camera.FocusMode.FOCUS_MODE_AUTO);
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`The isFocusModeSupported call failed. error code: ${err.code}`);
  }
  return status;
}
```

#### setFocusMode(deprecated)

setFocusMode(afMode: FocusMode): void

设置对焦模式。

进行设置之前，需要先检查设备是否支持指定的焦距模式，可使用方法[isFocusModeSupported](#ZH-CN_TOPIC_0000002529285785__isfocusmodesupporteddeprecated)。

从 API version 10开始支持，从API version 11开始废弃。建议使用[Focus.setFocusMode](Interface (Focus).md#ZH-CN_TOPIC_0000002497445804__setfocusmode11)替代。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

参数名类型必填说明afMode[FocusMode](Enums.md#ZH-CN_TOPIC_0000002497445814__focusmode)是指定的焦距模式。

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](Camera错误码.md)。

错误码ID错误信息7400103Session not config.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function setFocusMode(captureSession: camera.CaptureSession): void {
  try {
    captureSession.setFocusMode(camera.FocusMode.FOCUS_MODE_AUTO);
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`The setFocusMode call failed. error code: ${err.code}`);
  }
}
```

#### getFocusMode(deprecated)

getFocusMode(): FocusMode

获取当前的对焦模式。

从 API version 10开始支持，从API version 11开始废弃。建议使用[Focus.getFocusMode](Interface (Focus).md#ZH-CN_TOPIC_0000002497445804__getfocusmode11)替代。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

类型说明[FocusMode](Enums.md#ZH-CN_TOPIC_0000002497445814__focusmode)获取当前设备的焦距模式。接口调用失败会返回相应错误码，错误码类型[CameraErrorCode](Enums.md#ZH-CN_TOPIC_0000002497445814__cameraerrorcode)。

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](Camera错误码.md)。

错误码ID错误信息7400103Session not config.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function getFocusMode(captureSession: camera.CaptureSession): camera.FocusMode | undefined {
  let afMode: camera.FocusMode | undefined = undefined;
  try {
    afMode = captureSession.getFocusMode();
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`The getFocusMode call failed. error code: ${err.code}`);
  }
  return afMode;
}
```

#### setFocusPoint(deprecated)

setFocusPoint(point: Point): void

设置焦点，焦点应在0-1坐标系内，该坐标系左上角为{0，0}，右下角为{1，1}。

此坐标系是以设备充电口在右侧时的横向设备方向为基准的，例如应用的预览界面布局以

设备充电口在下侧时的竖向方向为基准，布局宽高为{w，h}，且触碰点为{x，y}，

则转换后的坐标点为{y/h，1-x/w}。

从 API version 10开始支持，从API version 11开始废弃。建议使用[Focus.setFocusPoint](Interface (Focus).md#ZH-CN_TOPIC_0000002497445804__setfocuspoint11)替代。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

参数名类型必填说明point[Point](Interfaces (其他).md#ZH-CN_TOPIC_0000002497605794__point)是焦点。x,y设置范围应在[0,1]之内，超过范围，如果小于0设置0，大于1设置1。

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](Camera错误码.md)。

错误码ID错误信息7400103Session not config.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function setFocusPoint(captureSession: camera.CaptureSession): void {
  const focusPoint: camera.Point = {x: 1, y: 1};
  try {
    captureSession.setFocusPoint(focusPoint);
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`The setFocusPoint call failed. error code: ${err.code}`);
  }
}
```

#### getFocusPoint(deprecated)

getFocusPoint(): Point

查询焦点。

从 API version 10开始支持，从API version 11开始废弃。建议使用[Focus.getFocusPoint](Interface (Focus).md#ZH-CN_TOPIC_0000002497445804__getfocuspoint11)替代。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

类型说明[Point](Interfaces (其他).md#ZH-CN_TOPIC_0000002497605794__point)用于获取当前焦点。接口调用失败会返回相应错误码，错误码类型[CameraErrorCode](Enums.md#ZH-CN_TOPIC_0000002497445814__cameraerrorcode)。

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](Camera错误码.md)。

错误码ID错误信息7400103Session not config.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function getFocusPoint(captureSession: camera.CaptureSession): camera.Point | undefined {
  let point: camera.Point | undefined = undefined;
  try {
    point = captureSession.getFocusPoint();
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`The getFocusPoint call failed. error code: ${err.code}`);
  }
  return point;
}
```

#### getFocalLength(deprecated)

getFocalLength(): number

查询焦距值。

从 API version 10开始支持，从API version 11开始废弃。建议使用[Focus.getFocalLength](Interface (Focus).md#ZH-CN_TOPIC_0000002497445804__getfocallength11)替代。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

类型说明number用于获取当前焦距。接口调用失败会返回相应错误码，错误码类型[CameraErrorCode](Enums.md#ZH-CN_TOPIC_0000002497445814__cameraerrorcode)。

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](Camera错误码.md)。

错误码ID错误信息7400103Session not config.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function getFocalLength(captureSession: camera.CaptureSession): number {
  const invalidValue: number = -1;
  let focalLength: number = invalidValue;
  try {
    focalLength = captureSession.getFocalLength();
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`The getFocalLength call failed. error code: ${err.code}`);
  }
  return focalLength;
}
```

#### getZoomRatioRange(deprecated)

getZoomRatioRange(): Array<number>

获取支持的变焦范围。

从 API version 10开始支持，从API version 11开始废弃。建议使用[Zoom.getZoomRatioRange](Interface (ZoomQuery).md#ZH-CN_TOPIC_0000002529445757__getzoomratiorange11)替代。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

类型说明Array<number>用于获取可变焦距比范围，返回的数组包括其最小值和最大值。接口调用失败会返回相应错误码，错误码类型[CameraErrorCode](Enums.md#ZH-CN_TOPIC_0000002497445814__cameraerrorcode)。

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](Camera错误码.md)。

错误码ID错误信息7400103Session not config.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function getZoomRatioRange(captureSession: camera.CaptureSession): Array<number> {
  let zoomRatioRange: Array<number> = [];
  try {
    zoomRatioRange = captureSession.getZoomRatioRange();
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`The getZoomRatioRange call failed. error code: ${err.code}`);
  }
  return zoomRatioRange;
}
```

#### setZoomRatio(deprecated)

setZoomRatio(zoomRatio: number): void

设置变焦比，变焦精度最高为小数点后两位，如果设置超过支持的精度范围，则只保留精度范围内数值。

从 API version 10开始支持，从API version 11开始废弃。建议使用[Zoom.setZoomRatio](Interface (Zoom).md#ZH-CN_TOPIC_0000002529285783__setzoomratio11)替代。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

参数名类型必填说明zoomRationumber是可变焦距比，通过[getZoomRatioRange](Interface (ZoomQuery).md#ZH-CN_TOPIC_0000002529445757__getzoomratiorange11)获取支持的变焦范围，如果设置超过支持范围的值，则只保留精度范围内数值。传参为null或者undefined，作为0处理，变焦设置最小值。

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](Camera错误码.md)。

错误码ID错误信息7400103Session not config.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function setZoomRatio(captureSession: camera.CaptureSession, zoomRatioRange: Array<number>): void {
  if (zoomRatioRange === undefined || zoomRatioRange.length <= 0) {
    return;
  }
  let zoomRatio = zoomRatioRange[0];
  try {
    captureSession.setZoomRatio(zoomRatio);
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`The setZoomRatio call failed. error code: ${err.code}`);
  }
}
```

#### getZoomRatio(deprecated)

getZoomRatio(): number

获取当前的变焦比。

从 API version 10开始支持，从API version 11开始废弃。建议使用[Zoom.getZoomRatio](Interface (Zoom).md#ZH-CN_TOPIC_0000002529285783__getzoomratio11)替代。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

类型说明number获取当前的变焦比结果。接口调用失败会返回相应错误码，错误码类型[CameraErrorCode](Enums.md#ZH-CN_TOPIC_0000002497445814__cameraerrorcode)。

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](Camera错误码.md)。

错误码ID错误信息7400103Session not config.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function getZoomRatio(captureSession: camera.CaptureSession): number {
  const invalidValue: number = -1;
  let zoomRatio: number = invalidValue;
  try {
    zoomRatio = captureSession.getZoomRatio();
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`The getZoomRatio call failed. error code: ${err.code}`);
  }
  return zoomRatio;
}
```

#### isVideoStabilizationModeSupported(deprecated)

isVideoStabilizationModeSupported(vsMode: VideoStabilizationMode): boolean

查询是否支持指定的视频防抖模式。

从 API version 10开始支持，从API version 11开始废弃。建议使用[Stabilization.isVideoStabilizationModeSupported](Interface (StabilizationQuery).md#ZH-CN_TOPIC_0000002497445810__isvideostabilizationmodesupported11)替代。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

参数名类型必填说明vsMode[VideoStabilizationMode](Enums.md#ZH-CN_TOPIC_0000002497445814__videostabilizationmode)是视频防抖模式。传参为null或者undefined，作为0处理，超级防抖模式关闭。

**返回值：**

类型说明boolean返回视频防抖模式是否支持。true表示支持，false表示不支持。接口调用失败会返回相应错误码，错误码类型[CameraErrorCode](Enums.md#ZH-CN_TOPIC_0000002497445814__cameraerrorcode)。

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](Camera错误码.md)。

错误码ID错误信息7400103Session not config.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function isVideoStabilizationModeSupported(captureSession: camera.CaptureSession): boolean {
  let isSupported: boolean = false;
  try {
    isSupported = captureSession.isVideoStabilizationModeSupported(camera.VideoStabilizationMode.OFF);
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`The isVideoStabilizationModeSupported call failed. error code: ${err.code}`);
  }
  return isSupported;
}
```

#### getActiveVideoStabilizationMode(deprecated)

getActiveVideoStabilizationMode(): VideoStabilizationMode

查询当前正在使用的视频防抖模式。

从 API version 10开始支持，从API version 11开始废弃。建议使用[Stabilization.getActiveVideoStabilizationMode](Interface (Stabilization).md#ZH-CN_TOPIC_0000002497605790__getactivevideostabilizationmode11)替代。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

类型说明[VideoStabilizationMode](Enums.md#ZH-CN_TOPIC_0000002497445814__videostabilizationmode)视频防抖是否正在使用。接口调用失败会返回相应错误码，错误码类型[CameraErrorCode](Enums.md#ZH-CN_TOPIC_0000002497445814__cameraerrorcode)。

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](Camera错误码.md)。

错误码ID错误信息7400103Session not config.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function getActiveVideoStabilizationMode(captureSession: camera.CaptureSession): camera.VideoStabilizationMode | undefined {
  let vsMode: camera.VideoStabilizationMode | undefined = undefined;
  try {
    vsMode = captureSession.getActiveVideoStabilizationMode();
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`The getActiveVideoStabilizationMode call failed. error code: ${err.code}`);
  }
  return vsMode;
}
```

#### setVideoStabilizationMode(deprecated)

setVideoStabilizationMode(mode: VideoStabilizationMode): void

设置视频防抖模式。需要先检查设备是否支持对应的防抖模式，可以通过[isVideoStabilizationModeSupported](#ZH-CN_TOPIC_0000002529285785__isvideostabilizationmodesupporteddeprecated)方法判断所设置的模式是否支持。

从 API version 10开始支持，从API version 11开始废弃。建议使用[Stabilization.setVideoStabilizationMode](Interface (Stabilization).md#ZH-CN_TOPIC_0000002497605790__setvideostabilizationmode11)替代。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

参数名类型必填说明mode[VideoStabilizationMode](Enums.md#ZH-CN_TOPIC_0000002497445814__videostabilizationmode)是需要设置的视频防抖模式。传参为null或者undefined，作为0处理，超级防抖模式关闭。

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](Camera错误码.md)。

错误码ID错误信息7400103Session not config.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function setVideoStabilizationMode(captureSession: camera.CaptureSession): void {
  try {
    captureSession.setVideoStabilizationMode(camera.VideoStabilizationMode.OFF);
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`The setVideoStabilizationMode call failed. error code: ${err.code}`);
  }
}
```

#### on('focusStateChange')(deprecated)

on(type: 'focusStateChange', callback: AsyncCallback<FocusState>): void

监听相机聚焦的状态变化，通过注册回调函数获取结果。使用callback异步回调。

从 API version 10开始支持，从API version 11开始废弃。建议使用[VideoSession.on('focusStateChange')](Interface (VideoSession).md#ZH-CN_TOPIC_0000002529445755__onfocusstatechange11)替代。

当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

参数名类型必填说明typestring是监听事件，固定为'focusStateChange'，session 创建成功可监听。仅当自动对焦模式时,且相机对焦状态发生改变时可触发该事件。callbackAsyncCallback<[FocusState](Enums.md#ZH-CN_TOPIC_0000002497445814__focusstate)>是回调函数，用于获取当前对焦状态。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function registerFocusStateChange(captureSession: camera.CaptureSession): void {
  captureSession.on('focusStateChange', (err: BusinessError, focusState: camera.FocusState) => {
    if (err !== undefined && err.code !== 0) {
      console.error(`Callback Error, errorCode: ${err.code}`);
      return;
    }
    console.info(`Focus state: ${focusState}`);
  });
}
```

#### off('focusStateChange')(deprecated)

off(type: 'focusStateChange', callback?: AsyncCallback<FocusState>): void

注销监听相机聚焦的状态变化。

从 API version 10开始支持，从API version 11开始废弃。建议使用[VideoSession.off('focusStateChange')](Interface (VideoSession).md#ZH-CN_TOPIC_0000002529445755__offfocusstatechange11)替代。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

参数名类型必填说明typestring是监听事件，固定为'focusStateChange'，session 创建成功可监听。callbackAsyncCallback<[FocusState](Enums.md#ZH-CN_TOPIC_0000002497445814__focusstate)>否回调函数，如果指定参数则取消对应callback（callback对象不可是匿名函数），否则取消所有callback。

**示例：**

```ets
function unregisterFocusStateChange(captureSession: camera.CaptureSession): void {
  captureSession.off('focusStateChange');
}
```

#### on('error')(deprecated)

on(type: 'error', callback: ErrorCallback): void

监听拍照会话的错误事件，通过注册回调函数获取结果。使用callback异步回调。

当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。

从 API version 10开始支持，从API version 11开始废弃。建议使用[VideoSession.on('error')](Interface (VideoSession).md#ZH-CN_TOPIC_0000002529445755__onerror11)替代。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

参数名类型必填说明typestring是监听事件，固定为'error'，session创建成功之后可监听该接口。session调用相关接口出现错误时会触发该事件，比如调用[beginConfig](#ZH-CN_TOPIC_0000002529285785__beginconfigdeprecated)，[commitConfig](#ZH-CN_TOPIC_0000002529285785__commitconfigdeprecated-1)，[addInput](#ZH-CN_TOPIC_0000002529285785__addinputdeprecated)等接口发生错误时返回错误信息。callback[ErrorCallback](zh-cn_topic_0000002497445536.html#ZH-CN_TOPIC_0000002497445536__errorcallback)是回调函数，用于获取错误信息。返回错误码，错误码类型[CameraErrorCode](Enums.md#ZH-CN_TOPIC_0000002497445814__cameraerrorcode)。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function registerCaptureSessionError(captureSession: camera.CaptureSession): void {
  captureSession.on('error', (error: BusinessError) => {
    console.error(`Capture session error code: ${error.code}`);
  });
}
```

#### off('error')(deprecated)

off(type: 'error', callback?: ErrorCallback): void

注销监听拍照会话的错误事件，通过注册回调函数获取结果。

从 API version 10开始支持，从API version 11开始废弃。建议使用[VideoSession.off('error')](Interface (VideoSession).md#ZH-CN_TOPIC_0000002529445755__offerror11)替代。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

参数名类型必填说明typestring是监听事件，固定为'error'，session创建成功之后可监听该接口。callback[ErrorCallback](@ohos.base (公共回调信息).md#ZH-CN_TOPIC_0000002497445536__errorcallback)否回调函数，如果指定参数则取消对应callback（callback对象不可是匿名函数），否则取消所有callback。

**示例：**

```ets
function unregisterCaptureSessionError(captureSession: camera.CaptureSession): void {
  captureSession.off('error');
}
```