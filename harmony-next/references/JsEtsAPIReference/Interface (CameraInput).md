# Interface (CameraInput)

相机设备输入对象。

会话中[Session](Interface (Session).md)使用的相机信息。

本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { camera } from '@kit.CameraKit';
```

#### open

open(callback: AsyncCallback<void>): void

打开相机，通过注册回调函数获取状态。使用callback异步回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

参数名类型必填说明callbackAsyncCallback<void>是回调函数。当打开相机成功，err为undefined，否则为错误对象，错误码类型[CameraErrorCode](Enums.md#ZH-CN_TOPIC_0000002497445814__cameraerrorcode)。

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](Camera错误码.md)。

错误码ID错误信息7400107Can not use camera cause of conflict.7400108Camera disabled cause of security reason.7400201Camera service fatal error.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function openCameraInput(cameraInput: camera.CameraInput): void {
  cameraInput.open((err: BusinessError) => {
    if (err) {
      console.error(`Failed to open the camera, error code: ${err.code}.`);
      return;
    }
    console.info('Callback returned with camera opened.');
  });
}
```

#### open

open(): Promise<void>

打开相机，使用Promise异步回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

类型说明Promise<void>Promise对象，无返回结果。

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](Camera错误码.md)。

错误码ID错误信息7400102Operation not allowed.7400107Can not use camera cause of conflict.7400108Camera disabled cause of security reason.7400201Camera service fatal error.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function openCameraInput(cameraInput: camera.CameraInput): void {
  cameraInput.open().then(() => {
    console.info('Promise returned with camera opened.');
  }).catch((error: BusinessError) => {
    console.error(`Failed to open the camera, error code: ${error.code}.`);
  });
}
```

#### open12+

open(isSecureEnabled: boolean): Promise<bigint>

打开相机。使用Promise异步回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

参数名类型必填说明isSecureEnabledboolean是设置true为使能以安全的方式打开相机，设置false则反之。接口调用失败会返回相应错误码，错误码类型[CameraErrorCode](Enums.md#ZH-CN_TOPIC_0000002497445814__cameraerrorcode)。

**返回值：**

类型说明Promise<bigint>Promise对象，返回安全相机的句柄。

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](Camera错误码.md)。

错误码ID错误信息7400107Can not use camera cause of conflict.7400108Camera disabled cause of security reason.7400201Camera service fatal error.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function openCameraInput(cameraInput: camera.CameraInput): void {
  cameraInput.open(true).then(() => {
    console.info('Promise returned with camera opened.');
  }).catch((error: BusinessError) => {
    console.error(`Failed to open the camera, error code: ${error.code}.`);
  });
}
```

#### open18+

open(type: CameraConcurrentType): Promise<void>

以指定的并发类型打开相机。使用Promise异步回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

参数名类型必填说明type[CameraConcurrentType](Enums.md#ZH-CN_TOPIC_0000002497445814__cameraconcurrenttype18)是以指定的并发类型打开相机。接口调用失败会返回相应错误码。

**返回值：**

类型说明Promise<void>Promise对象，无返回结果。

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](Camera错误码.md)。

错误码ID错误信息7400102Operation not allowed.7400107Can not use camera cause of conflict.7400108Camera disabled cause of security reason.7400201Camera service fatal error.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function openCameraInput(cameraInput: camera.CameraInput): void {
  cameraInput.open(0).then(() => {
    console.info('Promise returned with camera opened.');
  }).catch((error: BusinessError) => {
    console.error(`Failed to open the camera, error code: ${error.code}.`);
  });
}
```

#### close

close(callback: AsyncCallback<void>): void

关闭相机，通过注册回调函数获取状态。使用callback异步回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

参数名类型必填说明callbackAsyncCallback<void>是回调函数。当关闭相机成功，err为undefined，否则为错误对象。错误码类型[CameraErrorCode](Enums.md#ZH-CN_TOPIC_0000002497445814__cameraerrorcode)。

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](Camera错误码.md)。

错误码ID错误信息7400201Camera service fatal error.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function closeCameraInput(cameraInput: camera.CameraInput): void {
  cameraInput.close((err: BusinessError) => {
    if (err) {
      console.error(`Failed to close the cameras, error code: ${err.code}.`);
      return;
    }
    console.info('Callback returned with camera closed.');
  });
}
```

#### close

close(): Promise<void>

关闭相机，使用Promise异步回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

类型说明Promise<void>Promise对象，无返回结果。

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](Camera错误码.md)。

错误码ID错误信息7400201Camera service fatal error.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function closeCameraInput(cameraInput: camera.CameraInput): void {
  cameraInput.close().then(() => {
    console.info('Promise returned with camera closed.');
  }).catch((error: BusinessError) => {
    console.error(`Failed to close the cameras, error code: ${error.code}.`);
  });
}
```

#### on('error')

on(type: 'error', camera: CameraDevice, callback: ErrorCallback): void

监听CameraInput的错误事件，通过注册回调函数获取结果。使用callback异步回调。

当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

参数名类型必填说明typestring是监听事件，固定为'error'，CameraInput对象创建成功可监听。相机设备出错情况下可触发该事件并返回结果，比如设备不可用或者冲突等返回对应错误信息。camera[CameraDevice](Interfaces (其他).md#ZH-CN_TOPIC_0000002497605794__cameradevice)是CameraDevice对象。callback[ErrorCallback](@ohos.base (公共回调信息).md#ZH-CN_TOPIC_0000002497445536__errorcallback)是回调函数，用于获取结果。返回错误码，错误码类型[CameraErrorCode](Enums.md#ZH-CN_TOPIC_0000002497445814__cameraerrorcode)。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function callback(err: BusinessError): void {
  console.error(`Camera input error code: ${err.code}`);
}

function registerCameraInputError(cameraInput: camera.CameraInput, camera: camera.CameraDevice): void {
  cameraInput.on('error', camera, callback);
}
```

#### off('error')

off(type: 'error', camera: CameraDevice, callback?: ErrorCallback): void

注销监听CameraInput的错误事件。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

参数名类型必填说明typestring是监听事件，固定为'error'，CameraInput对象创建成功可监听。相机设备出错情况下可触发该事件并返回结果，比如设备不可用或者冲突等返回对应错误信息。camera[CameraDevice](Interfaces (其他).md#ZH-CN_TOPIC_0000002497605794__cameradevice)是CameraDevice对象。callback[ErrorCallback](@ohos.base (公共回调信息).md#ZH-CN_TOPIC_0000002497445536__errorcallback)否回调函数，如果指定参数则取消对应callback（callback对象不可是匿名函数），否则取消所有callback。

**示例：**

```ets
function unregisterCameraInputError(cameraInput: camera.CameraInput, camera: camera.CameraDevice): void {
  cameraInput.off('error', camera);
}
```

#### isPhysicalCameraOrientationVariable22+

isPhysicalCameraOrientationVariable(): boolean

查询设备不同折叠状态下，相机物理镜头角度是否可变。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

类型说明boolean查询设备不同折叠状态下，相机物理镜头角度是否可变。true表示可变，false表示不可变。若接口调用失败，返回undefined。

**示例：**

```ets
function isPhysicalCameraOrientationVariable(cameraInput: camera.CameraInput): boolean {
  let isVariable: boolean = cameraInput.isPhysicalCameraOrientationVariable();
  return isVariable;
}
```

#### getPhysicalCameraOrientation22+

getPhysicalCameraOrientation(): number

获取设备当前折叠状态下的物理镜头角度。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

类型说明number返回设备当前折叠状态下的物理镜头角度。

**示例：**

```ets
function getPhysicalCameraOrientation(cameraInput: camera.CameraInput): number {
  let physicalCameraOrientation: number = cameraInput.getPhysicalCameraOrientation();
  return physicalCameraOrientation;
}
```

#### usePhysicalCameraOrientation22+

usePhysicalCameraOrientation(isUsed: boolean): void

选择是否使用物理镜头角度。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

参数名类型必填说明isUsedboolean是选择是否使用物理镜头角度。true表示使用，false表示不使用。

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](Camera错误码.md)。

错误码ID错误信息7400102Operation not allowed.7400201Camera service fatal error.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function usePhysicalCameraOrientation(cameraInput: camera.CameraInput, isUsed: boolean): void {
  try {
    cameraInput.usePhysicalCameraOrientation(isUsed);
  } catch (error) {
    let err = error as BusinessError;
    console.error(`The usePhysicalCameraOrientation call failed. error code: ${err.code}`);
  }
}
```