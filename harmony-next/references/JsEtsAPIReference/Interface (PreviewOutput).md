# Interface (PreviewOutput)

预览输出类。继承[CameraOutput](Interface (CameraOutput).md)。

本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { camera } from '@kit.CameraKit';
```

#### on('frameStart')

on(type: 'frameStart', callback: AsyncCallback<void>): void

监听预览帧启动，通过注册回调函数获取结果。使用callback异步回调。

当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

参数名类型必填说明typestring是监听事件，固定为'frameStart'，previewOutput创建成功可监听。底层第一次开始曝光时触发该事件并返回。callbackAsyncCallback<void>是回调函数，用于获取结果。只要有该事件返回就证明预览开始。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function callback(err: BusinessError): void {
  if (err !== undefined && err.code !== 0) {
    console.error(`Callback Error, errorCode: ${err.code}`);
    return;
  }
  console.info('Preview frame started');
}

function registerPreviewOutputFrameStart(previewOutput: camera.PreviewOutput): void {
  previewOutput.on('frameStart', callback);
}
```

#### off('frameStart')

off(type: 'frameStart', callback?: AsyncCallback<void>): void

注销预览帧启动的监听。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

参数名类型必填说明typestring是监听事件，固定为'frameStart'，previewOutput创建成功可监听。callbackAsyncCallback<void>否回调函数，如果指定参数则取消对应callback（callback对象不可是匿名函数），否则取消所有callback。

**示例：**

```ets
function unregisterPreviewOutputFrameStart(previewOutput: camera.PreviewOutput): void {
  previewOutput.off('frameStart');
}
```

#### on('frameEnd')

on(type: 'frameEnd', callback: AsyncCallback<void>): void

监听预览帧结束，通过注册回调函数获取结果。使用callback异步回调。

当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

参数名类型必填说明typestring是监听事件，固定为'frameEnd'，previewOutput创建成功可监听。预览完全结束最后一帧时触发该事件并返回。callbackAsyncCallback<void>是回调函数，用于获取结果。只要有该事件返回就证明预览结束。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function callback(err: BusinessError): void {
  if (err !== undefined && err.code !== 0) {
    console.error(`Callback Error, errorCode: ${err.code}`);
    return;
  }
  console.info('Preview frame ended');
}

function registerPreviewOutputFrameEnd(previewOutput: camera.PreviewOutput): void {
  previewOutput.on('frameEnd', callback);
}
```

#### off('frameEnd')

off(type: 'frameEnd', callback?: AsyncCallback<void>): void

注销监听预览帧结束。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

参数名类型必填说明typestring是监听事件，固定为'frameEnd'，previewOutput创建成功可监听。callbackAsyncCallback<void>否回调函数，如果指定参数则取消对应callback（callback对象不可是匿名函数），否则取消所有callback。

**示例：**

```ets
function unregisterPreviewOutputFrameEnd(previewOutput: camera.PreviewOutput): void {
  previewOutput.off('frameEnd');
}
```

#### on('error')

on(type: 'error', callback: ErrorCallback): void

监听预览输出的错误事件，通过注册回调函数获取结果。使用callback异步回调。

当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

参数名类型必填说明typestring是监听事件，固定为'error'，previewOutput创建成功可监听。预览接口使用错误时触发该事件，比如调用[Session.start](Interface (Session).md#ZH-CN_TOPIC_0000002529445753__start11-1)，[CameraOutput.release](Interface (CameraOutput).md#ZH-CN_TOPIC_0000002529285771__release-1)等接口发生错误时返回对应错误信息。callback[ErrorCallback](@ohos.base (公共回调信息).md#ZH-CN_TOPIC_0000002497445536__errorcallback)是回调函数，用于获取错误信息。返回错误码，错误码类型[CameraErrorCode](Enums.md#ZH-CN_TOPIC_0000002497445814__cameraerrorcode)。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function callback(previewOutputError: BusinessError): void {
  console.error(`Preview output error code: ${previewOutputError.code}`);
}

function registerPreviewOutputError(previewOutput: camera.PreviewOutput): void {
  previewOutput.on('error', callback)
}
```

#### off('error')

off(type: 'error', callback?: ErrorCallback): void

注销监听预览输出的错误事件。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

参数名类型必填说明typestring是监听事件，固定为'error'，previewOutput创建成功可监听。callback[ErrorCallback](@ohos.base (公共回调信息).md#ZH-CN_TOPIC_0000002497445536__errorcallback)否回调函数，如果指定参数则取消对应callback（callback对象不可是匿名函数），否则取消所有callback。

**示例：**

```ets
function unregisterPreviewOutputError(previewOutput: camera.PreviewOutput): void {
  previewOutput.off('error');
}
```

#### getSupportedFrameRates12+

 getSupportedFrameRates(): Array<FrameRateRange>

查询支持的帧率范围。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

类型说明Array<[FrameRateRange](Interfaces (其他).md#ZH-CN_TOPIC_0000002497605794__frameraterange)>支持的帧率范围列表。若接口调用失败，返回undefined。

**示例：**

```ets
function getSupportedFrameRates(previewOutput: camera.PreviewOutput): Array<camera.FrameRateRange> {
  let supportedFrameRatesArray: Array<camera.FrameRateRange> = previewOutput.getSupportedFrameRates();
  return supportedFrameRatesArray;
}
```

#### setFrameRate12+

setFrameRate(minFps: number, maxFps: number): void

设置预览流帧率范围，设置的范围必须在支持的帧率范围内。

进行设置前，可通过[getSupportedFrameRates](#ZH-CN_TOPIC_0000002497445808__getsupportedframerates12)接口查询支持的帧率范围。

仅在[PhotoSession](Interface (PhotoSession).md)或[VideoSession](Interface (VideoSession).md)模式下支持。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

参数名类型必填说明minFpsnumber是最小帧率（单位：fps），当传入的最大值小于最小值时，传参异常，接口不生效。maxFpsnumber是最大帧率（单位：fps），当传入的最小值大于最大值时，传参异常，接口不生效。

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](Camera错误码.md)。

错误码ID错误信息7400101Parameter missing or parameter type incorrect.7400110Unresolved conflicts with current configurations.

**示例：**

```ets
function setFrameRateRange(previewOutput: camera.PreviewOutput, frameRateRange: Array<number>): void {
  previewOutput.setFrameRate(frameRateRange[0], frameRateRange[1]);
}
```

#### getActiveFrameRate12+

getActiveFrameRate(): FrameRateRange

获取已设置的帧率范围。

使用[setFrameRate](#ZH-CN_TOPIC_0000002497445808__setframerate12)接口对预览流设置过帧率后可查询。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

类型说明[FrameRateRange](Interfaces (其他).md#ZH-CN_TOPIC_0000002497605794__frameraterange)帧率范围

**示例：**

```ets
function getActiveFrameRate(previewOutput: camera.PreviewOutput): camera.FrameRateRange {
  let activeFrameRate: camera.FrameRateRange = previewOutput.getActiveFrameRate();
  return activeFrameRate;
}
```

#### getActiveProfile12+

getActiveProfile(): Profile

获取当前生效的配置信息。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

类型说明[Profile](Interfaces (其他).md#ZH-CN_TOPIC_0000002497605794__profile)当前生效的配置信息

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](Camera错误码.md)。

错误码ID错误信息7400201Camera service fatal error.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function testGetActiveProfile(previewOutput: camera.PreviewOutput): camera.Profile | undefined {
  let activeProfile: camera.Profile | undefined = undefined;
  try {
    activeProfile = previewOutput.getActiveProfile();
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`The previewOutput.getActiveProfile call failed. error code: ${err.code}`);
  }
  return activeProfile;
}
```

#### getPreviewRotation12+

getPreviewRotation(displayRotation: number): ImageRotation

获取预览旋转角度。

- 设备自然方向：设备默认使用方向，手机为竖屏（充电口向下）。
- 相机镜头角度：值等于相机图像顺时针旋转到设备自然方向的角度，手机后置相机传感器是横屏安装的，所以需要顺时针旋转90度到设备自然方向。
- 屏幕显示方向：需要屏幕显示的图片左上角为第一个像素点为坐标原点。锁屏时与自然方向一致。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

参数名类型必填说明displayRotationnumber是显示设备的屏幕旋转角度，通过[display.getDefaultDisplaySync](@ohos.display (屏幕属性).md#ZH-CN_TOPIC_0000002529284797__displaygetdefaultdisplaysync9)获得。

**返回值：**

类型说明[ImageRotation](Enums.md#ZH-CN_TOPIC_0000002497445814__imagerotation)获取预览旋转角度。若接口调用失败，返回undefined。

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](Camera错误码.md)。

错误码ID错误信息7400101Parameter missing or parameter type incorrect.7400201Camera service fatal error.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function testGetPreviewRotation(previewOutput: camera.PreviewOutput, imageRotation : camera.ImageRotation): camera.ImageRotation {
  let previewRotation: camera.ImageRotation = camera.ImageRotation.ROTATION_0;
  try {
    previewRotation = previewOutput.getPreviewRotation(imageRotation);
    console.info(`Preview rotation is: ${previewRotation}`);
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`The previewOutput.getPreviewRotation call failed. error code: ${err.code}`);
  }
  return previewRotation;
}
```

#### setPreviewRotation12+

setPreviewRotation(previewRotation: ImageRotation, isDisplayLocked?: boolean): void

设置预览旋转角度。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

参数名类型必填说明previewRotation[ImageRotation](Enums.md#ZH-CN_TOPIC_0000002497445814__imagerotation)是预览旋转角度isDisplayLockedboolean否Surface在屏幕旋转时是否锁定方向，未设置时默认取值为false，即不锁定方向。true表示锁定方向，false表示不锁定方向。详情请参考[SurfaceRotationOptions](XComponent.md#ZH-CN_TOPIC_0000002529444889__surfacerotationoptions12对象说明)

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](Camera错误码.md)。

错误码ID错误信息7400101Parameter missing or parameter type incorrect.7400201Camera service fatal error.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function testSetPreviewRotation(previewOutput: camera.PreviewOutput, previewRotation : camera.ImageRotation, isDisplayLocked: boolean): void {
  try {
    previewOutput.setPreviewRotation(previewRotation, isDisplayLocked);
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`The previewOutput.setPreviewRotation call failed. error code: ${err.code}`);
  }
  return;
}
```

#### start(deprecated)

start(callback: AsyncCallback<void>): void

开始输出预览流，通过注册回调函数获取结果。使用callback异步回调。

从 API version 10开始支持，从API version 11开始废弃。建议使用[Session.start](Interface (Session).md#ZH-CN_TOPIC_0000002529445753__start11)替代。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

参数名类型必填说明callbackAsyncCallback<void>是回调函数。当开始输出预览流成功，err为undefined，否则为错误对象。错误码类型[CameraErrorCode](Enums.md#ZH-CN_TOPIC_0000002497445814__cameraerrorcode)。

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](Camera错误码.md)。

错误码ID错误信息7400103Session not config.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function startPreviewOutput(previewOutput: camera.PreviewOutput): void {
  previewOutput.start((err: BusinessError) => {
    if (err) {
      console.error(`Failed to start the preview output, error code: ${err.code}.`);
      return;
    }
    console.info('Callback returned with preview output started.');
  });
}
```

#### start(deprecated)

start(): Promise<void>

开始输出预览流。使用Promise异步回调。

从 API version 10开始支持，从API version 11开始废弃。建议使用[Session.start](Interface (Session).md#ZH-CN_TOPIC_0000002529445753__start11-1)替代。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

类型说明Promise<void>Promise对象，无返回结果。

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](Camera错误码.md)。

错误码ID错误信息7400103Session not config.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function startPreviewOutput(previewOutput: camera.PreviewOutput): void {
  previewOutput.start().then(() => {
    console.info('Promise returned with preview output started.');
  }).catch((error: BusinessError) => {
    console.error(`Failed to preview output start, error code: ${error.code}.`);
  });
}
```

#### stop(deprecated)

stop(callback: AsyncCallback<void>): void

停止输出预览流，通过注册回调函数获取结果。使用callback异步回调。

从 API version 10开始支持，从API version 11开始废弃。建议使用[Session.stop](Interface (Session).md#ZH-CN_TOPIC_0000002529445753__stop11)替代。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

参数名类型必填说明callbackAsyncCallback<void>是回调函数。当停止输出预览流成功，err为undefined，否则为错误对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function stopPreviewOutput(previewOutput: camera.PreviewOutput): void {
  previewOutput.stop((err: BusinessError) => {
    if (err) {
      console.error(`Failed to stop the preview output, error code: ${err.code}.`);
      return;
    }
    console.info('Returned with preview output stopped.');
  })
}
```

#### stop(deprecated)

stop(): Promise<void>

停止输出预览流。使用Promise异步回调。

从 API version 10开始支持，从API version 11开始废弃。建议使用[Session.stop](Interface (Session).md#ZH-CN_TOPIC_0000002529445753__stop11-1)替代。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

类型说明Promise<void>Promise对象，无返回结果。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function stopPreviewOutput(previewOutput: camera.PreviewOutput): void {
  previewOutput.stop().then(() => {
    console.info('Callback returned with preview output stopped.');
  }).catch((error: BusinessError) => {
    console.error(`Failed to preview output stop, error code: ${error.code}.`);
  });
}
```