# Interface (VideoSession)

VideoSession 继承自 [Session](Interface (Session).md)、[Flash](Interface (Flash).md)、[AutoExposure](Interface (AutoExposure).md)、 [WhiteBalance](Interface (WhiteBalance).md)、[Focus](Interface (Focus).md)、[Zoom](Interface (Zoom).md)、[Stabilization](Interface (Stabilization).md)、[ColorManagement](Interface (ColorManagement).md)、[AutoDeviceSwitch](Interface (AutoDeviceSwitch).md)、[Macro](Interface (Macro).md)、[ControlCenter](Interface (ControlCenter).md)。

普通录像模式会话类，提供了对闪光灯、曝光、白平衡、对焦、变焦、视频防抖、色彩空间、微距及控制器的操作。

默认的视频录制模式，适用于一般场景。支持720P、1080p等多种分辨率的录制，可选择不同帧率（如30fps、60fps）。

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

参数名类型必填说明preconfigType[PreconfigType](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002497445814__preconfigtype12)是指定配置预期分辨率。preconfigRatio[PreconfigRatio](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002497445814__preconfigratio12)否可选画幅比例，默认为16:9。

**返回值：**

类型说明boolean

true: 支持指定预配置类型。

false: 不支持指定预配置类型。

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](../../errors/Camera错误码.md)。

错误码ID错误信息7400201Camera service fatal error.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function testCanPreconfig(videoSession: camera.VideoSession, preconfigType: camera.PreconfigType,
  preconfigRatio: camera.PreconfigRatio): void {
  try {
    let result = videoSession.canPreconfig(preconfigType, preconfigRatio);
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

参数名类型必填说明preconfigType[PreconfigType](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002497445814__preconfigtype12)是指定配置预期分辨率。preconfigRatio[PreconfigRatio](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002497445814__preconfigratio12)否可选画幅比例，默认为16:9。

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](../../errors/Camera错误码.md)。

错误码ID错误信息7400201Camera service fatal error.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function testPreconfig(videoSession: camera.VideoSession, preconfigType: camera.PreconfigType,
  preconfigRatio: camera.PreconfigRatio): void {
  try {
    videoSession.preconfig(preconfigType, preconfigRatio);
    console.info(`preconfig ${preconfigType} ${preconfigRatio} success`);
  } catch (error) {
    let err = error as BusinessError;
    console.error(`The preconfig call failed. error code: ${err.code}`);
  }
}
```

#### on('error')11+

on(type: 'error', callback: ErrorCallback): void

监听普通录像会话的错误事件，通过注册回调函数获取结果。使用callback异步回调。

当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

参数名类型必填说明typestring是监听事件，固定为'error'，session创建成功之后可监听该接口。session调用相关接口出现错误时会触发该事件，比如调用[beginConfig](Interface (Session).md#ZH-CN_TOPIC_0000002529445753__beginconfig11)，[commitConfig](Interface (Session).md#ZH-CN_TOPIC_0000002529445753__commitconfig11)，[addInput](Interface (Session).md#ZH-CN_TOPIC_0000002529445753__addinput11)等接口发生错误时返回错误信息。callback[ErrorCallback](../../modules/ohos/@ohos.base (公共回调信息).md#ZH-CN_TOPIC_0000002497445536__errorcallback)是回调函数，用于获取错误信息。返回错误码，错误码类型[CameraErrorCode](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002497445814__cameraerrorcode)。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function callback(err: BusinessError): void {
  console.error(`Video session error code: ${err.code}`);
}

function registerSessionError(videoSession: camera.VideoSession): void {
  videoSession.on('error', callback);
}
```

#### off('error')11+

off(type: 'error', callback?: ErrorCallback): void

注销监听普通录像会话的错误事件，通过注册回调函数获取结果。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

参数名类型必填说明typestring是监听事件，固定为'error'，session创建成功之后可监听该接口。callback[ErrorCallback](../../modules/ohos/@ohos.base (公共回调信息).md#ZH-CN_TOPIC_0000002497445536__errorcallback)否回调函数，如果指定参数则取消对应callback（callback对象不可是匿名函数），否则取消所有callback。

**示例：**

```ets
function unregisterSessionError(videoSession: camera.VideoSession): void {
  videoSession.off('error');
}
```

#### on('focusStateChange')11+

on(type: 'focusStateChange', callback: AsyncCallback<FocusState>): void

监听相机聚焦的状态变化，通过注册回调函数获取结果。使用callback异步回调。

当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

参数名类型必填说明typestring是监听事件，固定为'focusStateChange'，session创建成功可监听。仅当自动对焦模式时，且相机对焦状态发生改变时可触发该事件。callbackAsyncCallback<[FocusState](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002497445814__focusstate)>是回调函数，用于获取当前对焦状态。

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

function registerFocusStateChange(videoSession: camera.VideoSession): void {
  videoSession.on('focusStateChange', callback);
}
```

#### off('focusStateChange')11+

off(type: 'focusStateChange', callback?: AsyncCallback<FocusState>): void

注销监听相机聚焦的状态变化。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

参数名类型必填说明typestring是监听事件，固定为'focusStateChange'，session创建成功可监听。callbackAsyncCallback<[FocusState](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002497445814__focusstate)>否回调函数，如果指定参数则取消对应callback（callback对象不可是匿名函数），否则取消所有callback。

**示例：**

```ets
function unregisterFocusStateChange(videoSession: camera.VideoSession): void {
  videoSession.off('focusStateChange');
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

function registerSmoothZoomInfo(videoSession: camera.VideoSession): void {
  videoSession.on('smoothZoomInfoAvailable', callback);
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
function unregisterSmoothZoomInfo(videoSession: camera.VideoSession): void {
  videoSession.off('smoothZoomInfoAvailable');
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

function registerAutoDeviceSwitchStatus(videoSession: camera.VideoSession): void {
  videoSession.on('autoDeviceSwitchStatusChange', callback);
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
function unregisterSmoothZoomInfo(videoSession: camera.VideoSession): void {
  videoSession.off('autoDeviceSwitchStatusChange');
}
```

#### setQualityPrioritization14+

setQualityPrioritization(quality : QualityPrioritization) : void;

设置录像质量优先级。

- 默认为高录像质量，设置为功耗平衡将降低录像质量以减少功耗。实际功耗收益因平台而异。
- 建议该接口在[commitConfig](Interface (Session).md#ZH-CN_TOPIC_0000002529445753__commitconfig11)和[start](Interface (Session).md#ZH-CN_TOPIC_0000002529445753__start11-1)之间调用。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

参数名类型必填说明quality[QualityPrioritization](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002497445814__qualityprioritization14)是需要设置的视频质量优先级（默认为高录像质量）。

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](../../errors/Camera错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.7400103Session not config. The session has not been committed or configured.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function setQualityPrioritization(videoSession: camera.VideoSession): void {
  try {
    videoSession.setQualityPrioritization(camera.QualityPrioritization.POWER_BALANCE);
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`The setQualityPrioritization call failed. error code: ${err.code}`);
  }
}
```

#### on('systemPressureLevelChange')20+

on(type: 'systemPressureLevelChange', callback: AsyncCallback<SystemPressureLevel>): void

监听系统压力状态变化，通过注册回调函数获取结果。使用callback异步回调。

当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

参数名类型必填说明typestring是监听事件，固定为'systemPressureLevelChange'，session创建成功可监听。callbackAsyncCallback<[SystemPressureLevel](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002497445814__systempressurelevel20)>是回调函数，用于获取当前系统压力状态。

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

function registerSystemPressureLevelChangeCallback(videoSession: camera.VideoSession): void {
    videoSession.on('systemPressureLevelChange', callback);
}
```

#### off('systemPressureLevelChange')20+

off(type: 'systemPressureLevelChange', callback?: AsyncCallback<SystemPressureLevel>): void

注销监听系统压力状态变化。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

参数名类型必填说明typestring是注销监听事件，固定为'systemPressureLevelChange'，session创建成功可触发此事件。callbackAsyncCallback<[SystemPressureLevel](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002497445814__systempressurelevel20)>否回调函数，如果指定参数则取消对应callback (callback对象不可是匿名函数)，否则参数默认为空，取消所有callback。

**示例：**

```ets
function unregisterSystemPressureLevelChangeCallback(videoSession: camera.VideoSession): void {
  videoSession.off('systemPressureLevelChange');
}
```

#### on('controlCenterEffectStatusChange')20+

on(type: 'controlCenterEffectStatusChange', callback: AsyncCallback<ControlCenterStatusInfo>): void

监听相机控制器效果激活状态变化，通过注册回调函数获取结果。使用callback异步回调。

当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

参数名类型必填说明typestring是监听事件，固定为'controlCenterEffectStatusChange'，session创建成功可监听。callbackAsyncCallback<[ControlCenterStatusInfo](Interfaces (其他).md#ZH-CN_TOPIC_0000002497605794__controlcenterstatusinfo20)>是回调函数，用于获取当前控制器激活状态。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function callback(err: BusinessError, status: camera.ControlCenterStatusInfo): void {
  if (err !== undefined && err.code !== 0) {
    console.error(`Callback Error, errorCode: ${err.code}`);
    return;
  }
  console.info(`controlCenterEffectStatusChange: ${status}`);
}

function registerControlCenterEffectStatusChangeCallback(videoSession: camera.VideoSession): void {
  videoSession.on('controlCenterEffectStatusChange', callback);
}
```

#### off('controlCenterEffectStatusChange')20+

off(type: 'controlCenterEffectStatusChange', callback?: AsyncCallback<ControlCenterStatusInfo>): void

注销监听相机控制器激活状态变化。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

参数名类型必填说明typestring是注销监听事件，固定为'controlCenterEffectStatusChange'，session创建成功可触发此事件。callbackAsyncCallback<[ControlCenterStatusInfo](Interfaces (其他).md#ZH-CN_TOPIC_0000002497605794__controlcenterstatusinfo20)>否回调函数，如果指定参数则取消对应callback (callback对象不可是匿名函数)，否则参数默认为空，取消所有callback。

**示例：**

```ets
function unregisterControlCenterEffectStatusChange(videoSession: camera.VideoSession): void {
  videoSession.off('controlCenterEffectStatusChange');
}
```

#### on('macroStatusChanged')20+

on(type: 'macroStatusChanged', callback: AsyncCallback<boolean>): void

监听相机微距状态变化，通过注册回调函数获取结果。使用callback异步回调。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

参数名类型必填说明typestring是监听事件，固定为'macroStatusChanged'，session创建成功可监听。callbackAsyncCallback<boolean>是回调函数，用于获取当前微距状态，返回true是开启状态，返回false是禁用状态。

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

function registerMacroStatusChanged(videoSession: camera.VideoSession): void {
  videoSession.on('macroStatusChanged', callback);
}
```

#### off('macroStatusChanged')20+

off(type: 'macroStatusChanged', callback?: AsyncCallback<boolean>): void

注销相机微距状态变化的监听。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

参数名类型必填说明typestring是注销监听事件，固定为'macroStatusChanged'，session创建成功可触发此事件。callbackAsyncCallback<boolean>否回调函数，可选，如果指定参数则取消对应callback (callback对象不可是匿名函数)，否则参数默认为空，取消所有callback, 返回true表示成功，false表示失败。

**示例：**

```ets
function unregisterMacroStatusChanged(videoSession: camera.VideoSession): void {
  videoSession.off('macroStatusChanged');
}
```

#### onIsoInfoChange22+

onIsoInfoChange(callback: Callback<IsoInfo>): void

监听相机感光度（ISO）状态变化，通过注册回调函数获取最新ISO值。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

参数名类型必填说明callbackCallback<[IsoInfo](Interfaces (其他).md#ZH-CN_TOPIC_0000002497605794__isoinfo22)>是回调函数，用于获取相机当前的ISO值。

**示例：**

```ets

function callback(isoInfo: camera.IsoInfo): void {
  console.info(`Iso : ${isoInfo}`);
}

function registerIsoInfoChanged(videoSession: camera.VideoSession): void {
  videoSession.onIsoInfoChange(callback);
}
```

#### offIsoInfoChange22+

offIsoInfoChange(callback?: Callback<IsoInfo>): void

取消监听相机感光度（ISO）状态的变化。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

参数名类型必填说明callbackCallback<[IsoInfo](Interfaces (其他).md#ZH-CN_TOPIC_0000002497605794__isoinfo22)>否

回调函数，可选。

如果指定callback参数则注销该callback监听，callback不可是匿名函数。

如果未指定callback，则注销所有已存在的callback监听。

**示例：**

```ets

function callback(isoInfo: camera.IsoInfo): void {
  console.info(`Iso : ${isoInfo}`);
}

function unregisterIsoInfoChanged(videoSession: camera.VideoSession): void {
  videoSession.offIsoInfoChange(callback);
}

function unregisterAllIsoInfoChanged(videoSession: camera.VideoSession): void {
  videoSession.offIsoInfoChange();
}
```