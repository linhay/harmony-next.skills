# Interface (PhotoSession)

PhotoSession 继承自 [Session](Interface (Session).md)、[Flash](Interface (Flash).md)、[AutoExposure](Interface (AutoExposure).md)、[WhiteBalance](Interface (WhiteBalance).md)、[Focus](Interface (Focus).md)、[Zoom](Interface (Zoom).md)、[ColorManagement](Interface (ColorManagement).md)、[AutoDeviceSwitch](Interface (AutoDeviceSwitch).md)、[Macro](Interface (Macro).md)。

普通拍照模式会话类，提供了对闪光灯、曝光、白平衡、对焦、变焦、色彩空间及微距的操作。

默认的拍照模式，用于拍摄标准照片。支持多种照片格式和分辨率，适合大多数日常拍摄场景。

- 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
- 本Interface首批接口从API version 11开始支持。

#### 导入模块

```ets
import { camera } from '@kit.CameraKit';
```

#### canPreconfig12+

canPreconfig(preconfigType: PreconfigType, preconfigRatio?: PreconfigRatio): boolean

查询当前Session是否支持指定的预配置类型。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

参数名类型必填说明preconfigType[PreconfigType](Enums.md#ZH-CN_TOPIC_0000002497445814__preconfigtype12)是指定配置预期分辨率。preconfigRatio[PreconfigRatio](Enums.md#ZH-CN_TOPIC_0000002497445814__preconfigratio12)否可选画幅比例，默认为4:3。

**返回值：**

类型说明boolean

true: 支持指定预配值类型。

false: 不支持指定预配值类型。

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](Camera错误码.md)。

错误码ID错误信息7400201Camera service fatal error.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function testCanPreconfig(photoSession: camera.PhotoSession, preconfigType: camera.PreconfigType,
  preconfigRatio: camera.PreconfigRatio): void {
  try {
    let result = photoSession.canPreconfig(preconfigType, preconfigRatio);
    console.info(`canPreconfig ${preconfigType} ${preconfigRatio} result is : ${result}`);
  } catch (error) {
    let err = error as BusinessError;
    console.error(`The canPreconfig call failed. error code: ${err.code}`);
  }
}
```

#### preconfig12+

preconfig(preconfigType: PreconfigType, preconfigRatio?: PreconfigRatio): void

对当前Session进行预配置。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

参数名类型必填说明preconfigType[PreconfigType](Enums.md#ZH-CN_TOPIC_0000002497445814__preconfigtype12)是指定配置预期分辨率。preconfigRatio[PreconfigRatio](Enums.md#ZH-CN_TOPIC_0000002497445814__preconfigratio12)否可选画幅比例，默认为4:3。

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](Camera错误码.md)。

错误码ID错误信息7400201Camera service fatal error.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function testPreconfig(photoSession: camera.PhotoSession, preconfigType: camera.PreconfigType,
  preconfigRatio: camera.PreconfigRatio): void {
  try {
    photoSession.preconfig(preconfigType, preconfigRatio);
    console.info(`preconfig success preconfigType: ${preconfigType}, preconfigRatio: ${preconfigRatio}`);
  } catch (error) {
    let err = error as BusinessError;
    console.error(`The preconfig call failed. error code: ${err.code}`);
  }
}
```

#### on('error')11+

on(type: 'error', callback: ErrorCallback): void

监听普通拍照会话的错误事件，通过注册回调函数获取结果。使用callback异步回调。

当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

参数名类型必填说明typestring是监听事件，固定为'error'，session创建成功之后可监听该接口。session调用相关接口出现错误时会触发该事件，比如调用[beginConfig](Interface (Session).md#ZH-CN_TOPIC_0000002529445753__beginconfig11)，[commitConfig](Interface (Session).md#ZH-CN_TOPIC_0000002529445753__commitconfig11)，[addInput](Interface (Session).md#ZH-CN_TOPIC_0000002529445753__addinput11)等接口发生错误时返回错误信息。callback[ErrorCallback](@ohos.base (公共回调信息).md#ZH-CN_TOPIC_0000002497445536__errorcallback)是回调函数，用于获取错误信息。返回错误码，错误码类型[CameraErrorCode](Enums.md#ZH-CN_TOPIC_0000002497445814__cameraerrorcode)。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function callback(err: BusinessError): void {
  console.error(`Photo session error code: ${err.code}`);
}

function registerSessionError(photoSession: camera.PhotoSession): void {
  photoSession.on('error', callback);
}
```

#### off('error')11+

off(type: 'error', callback?: ErrorCallback): void

注销监听普通拍照会话的错误事件，通过注册回调函数获取结果。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

参数名类型必填说明typestring是监听事件，固定为'error'，session创建成功之后可监听该接口。callback[ErrorCallback](@ohos.base (公共回调信息).md#ZH-CN_TOPIC_0000002497445536__errorcallback)否回调函数，如果指定参数则取消对应callback（callback对象不可是匿名函数），否则取消所有callback。

**示例：**

```ets
function unregisterSessionError(photoSession: camera.PhotoSession): void {
  photoSession.off('error');
}
```

#### on('focusStateChange')11+

on(type: 'focusStateChange', callback: AsyncCallback<FocusState>): void

监听相机聚焦的状态变化，通过注册回调函数获取结果。使用callback异步回调。

当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

参数名类型必填说明typestring是监听事件，固定为'focusStateChange'，session创建成功可监听。仅当自动对焦模式时，且相机对焦状态发生改变时可触发该事件。callbackAsyncCallback<[FocusState](Enums.md#ZH-CN_TOPIC_0000002497445814__focusstate)>是回调函数，用于获取当前对焦状态。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function callback(err: BusinessError, focusState: camera.FocusState): void {
  if (err !== undefined && err.code !== 0) {
    console.error(`Callback Error, errorCode: ${err.code}`);
    return;
  }
  console.info(`Focus state: ${focusState}`);
}

function registerFocusStateChange(photoSession: camera.PhotoSession): void {
  photoSession.on('focusStateChange', callback);
}
```

#### off('focusStateChange')11+

off(type: 'focusStateChange', callback?: AsyncCallback<FocusState>): void

注销监听相机聚焦的状态变化。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

参数名类型必填说明typestring是监听事件，固定为'focusStateChange'，session创建成功可监听。callbackAsyncCallback<[FocusState](Enums.md#ZH-CN_TOPIC_0000002497445814__focusstate)>否回调函数，如果指定参数则取消对应callback（callback对象不可是匿名函数），否则取消所有callback。

**示例：**

```ets
function unregisterFocusStateChange(photoSession: camera.PhotoSession): void {
  photoSession.off('focusStateChange');
}
```

#### on('smoothZoomInfoAvailable')11+

on(type: 'smoothZoomInfoAvailable', callback: AsyncCallback<SmoothZoomInfo>): void

监听相机平滑变焦的状态变化，通过注册回调函数获取结果。使用callback异步回调。

当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

参数名类型必填说明typestring是监听事件，固定为'smoothZoomInfoAvailable'，session创建成功可监听。callbackAsyncCallback<[SmoothZoomInfo](Interfaces (其他).md#ZH-CN_TOPIC_0000002497605794__smoothzoominfo11)>是回调函数，用于获取当前平滑变焦状态。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function callback(err: BusinessError, smoothZoomInfo: camera.SmoothZoomInfo): void {
  if (err !== undefined && err.code !== 0) {
    console.error(`Callback Error, errorCode: ${err.code}`);
    return;
  }
  console.info(`The duration of smooth zoom: ${smoothZoomInfo.duration}`);
}

function registerSmoothZoomInfo(photoSession: camera.PhotoSession): void {
  photoSession.on('smoothZoomInfoAvailable', callback);
}
```

#### off('smoothZoomInfoAvailable')11+

off(type: 'smoothZoomInfoAvailable', callback?: AsyncCallback<SmoothZoomInfo>): void

注销监听相机平滑变焦的状态变化。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

参数名类型必填说明typestring是监听事件，固定为'smoothZoomInfoAvailable'，session创建成功可监听。callbackAsyncCallback<[SmoothZoomInfo](Interfaces (其他).md#ZH-CN_TOPIC_0000002497605794__smoothzoominfo11)>否回调函数，如果指定参数则取消对应callback（callback对象不可是匿名函数），否则取消所有callback。

**示例：**

```ets
function unregisterSmoothZoomInfo(photoSession: camera.PhotoSession): void {
  photoSession.off('smoothZoomInfoAvailable');
}
```

#### on('autoDeviceSwitchStatusChange')13+

on(type: 'autoDeviceSwitchStatusChange', callback: AsyncCallback<AutoDeviceSwitchStatus>): void

监听相机自动切换镜头状态变化，通过注册回调函数获取结果。使用callback异步回调。

当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

参数名类型必填说明typestring是监听事件，固定为'autoDeviceSwitchStatusChange'，session创建成功可监听。callbackAsyncCallback<[AutoDeviceSwitchStatus](Interfaces (其他).md#ZH-CN_TOPIC_0000002497605794__autodeviceswitchstatus13)>是回调函数，用于获取当前自动切换镜头的状态。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function callback(err: BusinessError, autoDeviceSwitchStatus: camera.AutoDeviceSwitchStatus): void {
  if (err !== undefined && err.code !== 0) {
    console.error(`Callback Error, errorCode: ${err.code}`);
    return;
  }
  console.info(`isDeviceSwitched: ${autoDeviceSwitchStatus.isDeviceSwitched}, isDeviceCapabilityChanged: ${autoDeviceSwitchStatus.isDeviceCapabilityChanged}`);
}

function registerAutoDeviceSwitchStatus(photoSession: camera.PhotoSession): void {
  photoSession.on('autoDeviceSwitchStatusChange', callback);
}
```

#### off('autoDeviceSwitchStatusChange')13+

off(type: 'autoDeviceSwitchStatusChange', callback?: AsyncCallback<AutoDeviceSwitchStatus>): void

注销监听相机自动切换镜头状态变化。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

参数名类型必填说明typestring是监听事件，固定为'autoDeviceSwitchStatusChange'，session创建成功可监听。callbackAsyncCallback<[AutoDeviceSwitchStatus](Interfaces (其他).md#ZH-CN_TOPIC_0000002497605794__autodeviceswitchstatus13)>否回调函数，如果指定参数则取消对应callback（callback对象不可是匿名函数），否则取消所有callback。

**示例：**

```ets
function unregisterSmoothZoomInfo(photoSession: camera.PhotoSession): void {
  photoSession.off('autoDeviceSwitchStatusChange');
}
```

#### on('systemPressureLevelChange')20+

on(type: 'systemPressureLevelChange', callback: AsyncCallback<SystemPressureLevel>): void

监听系统压力状态变化，通过注册回调函数获取结果。使用callback异步回调。

当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

参数名类型必填说明typestring是监听事件，固定为'systemPressureLevelChange'，session创建成功可监听。callbackAsyncCallback<[SystemPressureLevel](Enums.md#ZH-CN_TOPIC_0000002497445814__systempressurelevel20)>是回调函数，用于获取当前系统压力状态.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function callback(err: BusinessError, systemPressureLevel: camera.SystemPressureLevel): void {
  if (err !== undefined && err.code !== 0) {
    console.error(`Callback Error, errorCode: ${err.code}`);
    return;
  }
  console.info(`systemPressureLevel: ${systemPressureLevel}`);
}

function registerSystemPressureLevelChangeCallback(photoSession: camera.PhotoSession): void {
    photoSession.on('systemPressureLevelChange', callback);
}
```

#### off('systemPressureLevelChange')20+

off(type: 'systemPressureLevelChange', callback?: AsyncCallback<SystemPressureLevel>): void

注销监听系统压力状态变化。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

参数名类型必填说明typestring是注销监听事件，固定为'systemPressureLevelChange'，session创建成功可触发此事件。callbackAsyncCallback<[SystemPressureLevel](Enums.md#ZH-CN_TOPIC_0000002497445814__systempressurelevel20)>否回调函数，如果指定参数则取消对应callback (callback对象不可是匿名函数)，否则参数默认为空，取消所有callback。

**示例：**

```ets
function unregisterSystemPressureLevelChangeCallback(photoSession: camera.PhotoSession): void {
  photoSession.off('systemPressureLevelChange');
}
```

#### on('macroStatusChanged')20+

on(type: 'macroStatusChanged', callback: AsyncCallback<boolean>): void

监听相机微距状态变化，通过注册回调函数获取结果。使用callback异步回调。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

参数名类型必填说明typestring是监听事件，固定为'macroStatusChanged'，session创建成功可监听。callbackAsyncCallback<boolean>是回调函数，用于获取当前微距状态，返回true为开启状态，返回false为禁用状态。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function callback(err: BusinessError, macroStatus: boolean): void {
  if (err !== undefined && err.code !== 0) {
    console.error(`Callback Error, errorCode: ${err.code}`);
    return;
  }
  console.info(`Macro state: ${macroStatus}`);
}

function registerMacroStatusChanged(photoSession: camera.PhotoSession): void {
  photoSession.on('macroStatusChanged', callback);
}
```

#### off('macroStatusChanged')20+

off(type: 'macroStatusChanged', callback?: AsyncCallback<boolean>): void

注销相机微距状态变化的监听。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

参数名类型必填说明typestring是注销监听事件，固定为'macroStatusChanged'，session创建成功可触发此事件。callbackAsyncCallback<boolean>否回调函数，可选，如果指定参数则取消对应callback (callback对象不可是匿名函数)，否则参数默认为空，取消所有callback。

**示例：**

```ets
function unregisterMacroStatusChanged(photoSession: camera.PhotoSession): void {
  photoSession.off('macroStatusChanged');
}
```