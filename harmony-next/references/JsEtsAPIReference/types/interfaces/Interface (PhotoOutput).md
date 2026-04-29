# Interface (PhotoOutput)

拍照会话中使用的输出信息，继承[CameraOutput](Interface (CameraOutput).md)。

本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { camera } from '@kit.CameraKit';
```

#### capture

capture(callback: AsyncCallback<void>): void

以默认设置触发一次拍照，通过注册回调函数获取结果。使用callback异步回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当以默认设置触发拍照成功，err为undefined，否则为错误对象。错误码类型[CameraErrorCode](../enums/Enums.md#ZH-CN_TOPIC_0000002497445814__cameraerrorcode)。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码]([Camera错误码](../../errors/Camera错误码.md).md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400104 | Session not running. |
| 7400201 | Camera service fatal error. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function capture(photoOutput: camera.PhotoOutput): void {
  photoOutput.capture((err: BusinessError) => {
    if (err) {
      console.error(`Failed to capture the photo, error code: ${err.code}.`);
      return;
    }
    console.info('Callback invoked to indicate the photo capture request success.');
  });
}
```

#### capture

capture(): Promise<void>

以默认设置触发一次拍照。使用Promise异步回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](Camera错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400104 | Session not running. |
| 7400201 | Camera service fatal error. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function capture(photoOutput: camera.PhotoOutput): void {
  photoOutput.capture().then(() => {
    console.info('Promise returned to indicate that photo capture request success.');
  }).catch((error: BusinessError) => {
    console.error(`Failed to photo output capture, error code: ${error.code}.`);
  });
}
```

#### capture

capture(setting: PhotoCaptureSetting, callback: AsyncCallback<void>): void

以指定参数触发一次拍照，通过注册回调函数获取结果。使用callback异步回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| setting | PhotoCaptureSetting | 是 | 拍照设置，传入undefined类型数据按默认设置触发一次拍照处理。 |
| callback | AsyncCallback<void> | 是 | 回调函数，用于获取结果。接口调用失败会返回相应错误码，错误码类型[CameraErrorCode](../enums/Enums.md#ZH-CN_TOPIC_0000002497445814__cameraerrorcode)。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](Camera错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400101 | Parameter missing or parameter type incorrect. |
| 7400104 | Session not running. |
| 7400201 | Camera service fatal error. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function capture(photoOutput: camera.PhotoOutput): void {
  let captureLocation: camera.Location = {
    latitude: 0,
    longitude: 0,
    altitude: 0
  }
  let settings: camera.PhotoCaptureSetting = {
    quality: camera.QualityLevel.QUALITY_LEVEL_LOW,
    rotation: camera.ImageRotation.ROTATION_0,
    location: captureLocation,
    mirror: false
  }
  photoOutput.capture(settings, (err: BusinessError) => {
    if (err) {
      console.error(`Failed to capture the photo, error code: ${err.code}.`);
      return;
    }
    console.info('Callback invoked to indicate the photo capture request success.');
  });
}
```

#### capture

capture(setting: PhotoCaptureSetting): Promise<void>

以指定参数触发一次拍照。使用Promise异步回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| setting | PhotoCaptureSetting | 是 | 拍照设置，传入undefined类型数据按默认设置触发一次拍照处理。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](Camera错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400101 | Parameter missing or parameter type incorrect. |
| 7400104 | Session not running. |
| 7400201 | Camera service fatal error. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function capture(photoOutput: camera.PhotoOutput): void {
  let captureLocation: camera.Location = {
    latitude: 0,
    longitude: 0,
    altitude: 0
  }
  let settings: camera.PhotoCaptureSetting = {
    quality: camera.QualityLevel.QUALITY_LEVEL_LOW,
    rotation: camera.ImageRotation.ROTATION_0,
    location: captureLocation,
    mirror: false
  }
  photoOutput.capture(settings).then(() => {
    console.info('Promise returned to indicate that photo capture request success.');
  }).catch((error: BusinessError) => {
    console.error(`Failed to photo output capture, error code: ${error.code}.`);
  });
}
```

#### on('photoAvailable')11+

on(type: 'photoAvailable', callback: AsyncCallback<Photo>): void

注册监听拍照返回照片上报事件。使用callback异步回调。


当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'photoAvailable'，photoOutput创建成功后可监听。 |
| callback | AsyncCallback<Photo> | 是 | 回调函数，用于监听拍照返回照片上报事件。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { image } from '@kit.ImageKit';
import { camera } from '@kit.CameraKit';

function callback(err: BusinessError, photo: camera.Photo): void {
  if (err !== undefined && err.code !== 0) {
    console.error(`Callback Error, errorCode: ${err.code}`);
    return;
  }
  let mainImage: image.Image = photo.main;
}

function registerPhotoOutputPhotoAvailable(photoOutput: camera.PhotoOutput): void {
  photoOutput.on('photoAvailable', callback);
}
```

#### off('photoAvailable')11+

off(type: 'photoAvailable', callback?: AsyncCallback<Photo>): void

注销监听拍照返回照片上报事件。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'photoAvailable'，photoOutput创建成功后可监听。 |
| callback | AsyncCallback<Photo> | 否 | 回调函数，如果指定参数则取消对应callback（callback对象不可是匿名函数），否则取消所有callback。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { image } from '@kit.ImageKit';

function callback(err: BusinessError, photo: camera.Photo): void {
  if (err !== undefined && err.code !== 0) {
    console.error(`Callback Error, errorCode: ${err.code}`);
    return;
  }
  let mainImage: image.Image = photo.main;
}

function unRegisterPhotoOutputPhotoAvailable(photoOutput: camera.PhotoOutput): void {
  photoOutput.off('photoAvailable', callback);
}
```

**onCapturePhotoAvailable23+**

onCapturePhotoAvailable(callback: Callback<CapturePhoto>): void

注册监听全质量图和未压缩图。使用callback异步回调。


-

注册监听接口时，不支持在该接口监听的回调方法里调用[offCapturePhotoAvailable](#ZH-CN_TOPIC_0000002553201877__offcapturephotoavailable23)注销回调。

-

拍摄未压缩图（YUV）格式图片时，仅支持使用此接口注册监听。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从API version 23开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Multimedia.Camera.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<CapturePhoto> | 是 | 回调函数，用于监听全质量图和未压缩图上报事件。 |

示例：

```ets
import { camera } from '@kit.CameraKit';
import { image } from '@kit.ImageKit';

function callback(capturePhoto: camera.CapturePhoto): void {
  let picture: image.Image | image.Picture = capturePhoto.main;
}

function registerCapturePhotoOutputPhotoAvailable(photoOutput: camera.PhotoOutput): void {
  photoOutput.onCapturePhotoAvailable(callback);
}
```

**offCapturePhotoAvailable23+**

offCapturePhotoAvailable(callback?: Callback<CapturePhoto>): void

注销监听全质量图和未压缩图。使用callback异步回调。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从API version 23开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Multimedia.Camera.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<CapturePhoto> | 否 | 回调函数，如果指定参数则取消对应callback，callback对象不可是匿名函数，否则取消所有callback。 |

示例：

```ets
import { camera } from '@kit.CameraKit';
import { image } from '@kit.ImageKit';

function callback(capturePhoto: camera.CapturePhoto): void {
  let picture: image.Image | image.Picture = capturePhoto.main;
}

function unRegisterCapturePhotoOutputPhotoAvailable(photoOutput: camera.PhotoOutput): void {
  photoOutput.offCapturePhotoAvailable(callback);
}
```

#### on('captureStartWithInfo')11+

on(type: 'captureStartWithInfo', callback: AsyncCallback<CaptureStartInfo>): void

监听拍照开始，通过注册回调函数获取[CaptureStartInfo](Interfaces (其他).md#ZH-CN_TOPIC_0000002522081922__capturestartinfo11)。使用callback异步回调。


当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'captureStartWithInfo'，photoOutput创建成功后可监听。 |
| callback | AsyncCallback<CaptureStartInfo> | 是 | 使用callback的方式获取Capture ID。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function callback(err: BusinessError, captureStartInfo: camera.CaptureStartInfo): void {
  if (err !== undefined && err.code !== 0) {
    console.error(`Callback Error, errorCode: ${err.code}`);
    return;
  }
  console.info(`photo capture started, captureStartInfo : ${captureStartInfo}`);
}

function registerCaptureStartWithInfo(photoOutput: camera.PhotoOutput): void {
  photoOutput.on('captureStartWithInfo', callback);
}
```

#### off('captureStartWithInfo')11+

off(type: 'captureStartWithInfo', callback?: AsyncCallback<CaptureStartInfo>): void

注销监听拍照。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'captureStartWithInfo'，photoOutput创建成功后可监听。 |
| callback | AsyncCallback<CaptureStartInfo> | 否 | 回调函数，如果指定参数则取消对应callback（callback对象不可是匿名函数），否则取消所有callback。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function unRegisterCaptureStartWithInfo(photoOutput: camera.PhotoOutput): void {
  photoOutput.off('captureStartWithInfo');
}
```

#### isMovingPhotoSupported12+

isMovingPhotoSupported(): boolean

查询是否支持动态照片拍摄。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回是否支持动态照片拍照。true表示支持，false表示不支持。若接口调用失败，返回undefined。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](Camera错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400201 | Camera service fatal error. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function isMovingPhotoSupported(photoOutput: camera.PhotoOutput): boolean {
  let isSupported: boolean = false;
  try {
    isSupported = photoOutput.isMovingPhotoSupported();
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`The isMovingPhotoSupported call failed. error code: ${err.code}`);
  }
  return isSupported;
}
```

#### enableMovingPhoto12+

enableMovingPhoto(enabled: boolean): void

使能动态照片拍照。

**需要权限：** ohos.permission.MICROPHONE

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean | 是 | 使能动态照片拍照。true为开启动态照片，false为关闭动态照片。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](Camera错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | permission denied. |
| 7400101 | Parameter missing or parameter type incorrect. |
| 7400201 | Camera service fatal error. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function enableMovingPhoto(photoOutput: camera.PhotoOutput): void {
  try {
    photoOutput.enableMovingPhoto(true);
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`The enableMovingPhoto call failed. error code: ${err.code}`);
  }
```

#### on('photoAssetAvailable')12+

on(type: 'photoAssetAvailable', callback: AsyncCallback<photoAccessHelper.PhotoAsset>): void

注册监听photoAsset上报。使用callback异步回调。

当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'photoAssetAvailable'，photoOutput创建成功后可监听。 |
| callback | AsyncCallback<photoAccessHelper.PhotoAsset> | 是 | 回调函数，用于监听photoAsset上报。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { photoAccessHelper } from '@kit.MediaLibraryKit';

function photoAssetAvailableCallback(err: BusinessError, photoAsset: photoAccessHelper.PhotoAsset): void {
  if (err) {
    console.info(`photoAssetAvailable error: ${JSON.stringify(err)}.`);
    return;
  }
  console.info('photoOutPutCallBack photoAssetAvailable');
  // 开发者可通过photoAsset获取图片相关信息。
}

function onPhotoOutputPhotoAssetAvailable(photoOutput: camera.PhotoOutput): void {
  photoOutput.on('photoAssetAvailable', photoAssetAvailableCallback);
}
```

#### off('photoAssetAvailable')12+

off(type: 'photoAssetAvailable', callback?: AsyncCallback<photoAccessHelper.PhotoAsset>): void

注销photoAsset上报。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'photoAssetAvailable'，photoOutput创建成功后可监听。 |
| callback | AsyncCallback<photoAccessHelper.PhotoAsset> | 否 | 需要解监听的回调方法。如果callback不为空且与此对应的监听方法一致，不为匿名方法，则解注册该方法；如果callback为空，则解监听所有回调。 |

**示例：**

```ets
function offPhotoOutputPhotoAssetAvailable(photoOutput: camera.PhotoOutput): void {
  photoOutput.off('photoAssetAvailable');
}
```

#### isMirrorSupported

isMirrorSupported(): boolean

查询是否支持镜像拍照。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回是否支持镜像拍照，true表示支持，false表示不支持。若接口调用失败，返回undefined。 |

**示例：**

```ets
function isMirrorSupported(photoOutput: camera.PhotoOutput): boolean {
  let isSupported: boolean = photoOutput.isMirrorSupported();
  return isSupported;
}
```

#### enableMirror13+

enableMirror(enabled: boolean): void

是否启用动态照片镜像拍照。

调用该接口前，需要通过[isMovingPhotoSupported](#ZH-CN_TOPIC_0000002553201877__ismovingphotosupported12)查询是否支持动态照片拍摄功能以及通过[isMirrorSupported](#ZH-CN_TOPIC_0000002553201877__ismirrorsupported)查询是否支持镜像拍照功能。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean | 是 | 是否启用动态照片镜像拍照。true为开启动态照片镜像拍照，false为关闭动态照片镜像拍照。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](Camera错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400101 | Parameter missing or parameter type incorrect. |
| 7400103 | Session not config. |
| 7400201 | Camera service fatal error. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function enableMirror(photoOutput: camera.PhotoOutput): void {
  try {
    photoOutput.enableMirror(true);
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`The enableMirror call failed. error code: ${err.code}`);
  }
```

#### getSupportedMovingPhoto[VideoCodecType](../enums/Enums.md#ZH-CN_TOPIC_0000002497445814__videocodectype13)s13+

getSupportedMovingPhoto[VideoCodecType](../enums/Enums.md#ZH-CN_TOPIC_0000002497445814__videocodectype13)s(): Array<VideoCodecType>

查询支持的动态照片短视频编码类型。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<[VideoCodecType](../enums/Enums.md#ZH-CN_TOPIC_0000002497445814__videocodectype13)> | 支持的动态照片短视频编码类型列表。若接口调用失败，返回undefined。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](Camera错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400201 | Camera service fatal error. |

**示例：**

```ets
function getSupportedMovingPhotoVideoCodecType(photoOutput: camera.PhotoOutput): Array<camera.VideoCodecType> {
  let supportedVideoCodecTypesArray: Array<camera.VideoCodecType> = photoOutput.getSupportedMovingPhotoVideoCodecTypes();
  return supportedVideoCodecTypesArray;
}
```

#### setMovingPhoto[VideoCodecType](../enums/Enums.md#ZH-CN_TOPIC_0000002497445814__videocodectype13)13+

setMovingPhoto[VideoCodecType](../enums/Enums.md#ZH-CN_TOPIC_0000002497445814__videocodectype13)(codecType: VideoCodecType): void

设置动态照片短视频编码类型。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| codecType | [VideoCodecType](../enums/Enums.md#ZH-CN_TOPIC_0000002497445814__videocodectype13) | 是 | 动态照片短视频编码类型。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](Camera错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400201 | Camera service fatal error. |

**示例：**

```ets
function setMovingPhotoVideoCodecTypes(photoOutput: camera.PhotoOutput, videoCodecType: camera.VideoCodecType): void {
  photoOutput.setMovingPhotoVideoCodecType(videoCodecType);
}
```

#### on('frameShutter')

on(type: 'frameShutter', callback: AsyncCallback<FrameShutterInfo>): void

监听拍照帧输出捕获，通过注册回调函数获取结果。使用callback异步回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'frameShutter'，photoOutput创建成功后可监听。 |
| callback | AsyncCallback<FrameShutterInfo> | 是 | 回调函数，用于获取相关信息。该回调返回意味着可以再次下发拍照请求。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function callback(err: BusinessError, frameShutterInfo: camera.FrameShutterInfo): void {
  if (err !== undefined && err.code !== 0) {
    console.error(`Callback Error, errorCode: ${err.code}`);
    return;
  }
  console.info(`CaptureId for frame : ${frameShutterInfo.captureId}`);
  console.info(`Timestamp for frame : ${frameShutterInfo.timestamp}`);
}

function registerPhotoOutputFrameShutter(photoOutput: camera.PhotoOutput): void {
  photoOutput.on('frameShutter', callback);
}
```

#### off('frameShutter')

off(type: 'frameShutter', callback?: AsyncCallback<FrameShutterInfo>): void

注销监听拍照帧输出捕获。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'frameShutter'，photoOutput创建成功后可监听。 |
| callback | AsyncCallback<FrameShutterInfo> | 否 | 回调函数，如果指定参数则取消对应callback（callback对象不可是匿名函数），否则取消所有callback。 |

**示例：**

```ets
function unregisterPhotoOutputFrameShutter(photoOutput: camera.PhotoOutput): void {
  photoOutput.off('frameShutter');
}
```

#### on('captureEnd')

on(type: 'captureEnd', callback: AsyncCallback<CaptureEndInfo>): void

监听拍照结束，通过注册回调函数获取结果。使用callback异步回调。

当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'captureEnd'。photoOutput创建成功后可监听。拍照完全结束可触发该事件发生并返回相应信息。 |
| callback | AsyncCallback<CaptureEndInfo> | 是 | 回调函数，用于获取相关信息。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function callback(err: BusinessError, captureEndInfo: camera.CaptureEndInfo): void {
  if (err !== undefined && err.code !== 0) {
    console.error(`Callback Error, errorCode: ${err.code}`);
    return;
  }
  console.info(`photo capture end, captureId : ${captureEndInfo.captureId}`);
  console.info(`frameCount : ${captureEndInfo.frameCount}`);
}

function registerPhotoOutputCaptureEnd(photoOutput: camera.PhotoOutput): void {
  photoOutput.on('captureEnd', callback);
}
```

#### off('captureEnd')

off(type: 'captureEnd', callback?: AsyncCallback<CaptureEndInfo>): void

注销监听拍照结束。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'captureEnd'，photoOutput创建成功后可监听。 |
| callback | AsyncCallback<CaptureEndInfo> | 否 | 回调函数，如果指定参数则取消对应callback（callback对象不可是匿名函数），否则取消所有callback。 |

**示例：**

```ets
function unregisterPhotoOutputCaptureEnd(photoOutput: camera.PhotoOutput): void {
  photoOutput.off('captureEnd');
}
```

#### on('frameShutterEnd')12+

on(type: 'frameShutterEnd', callback: AsyncCallback<FrameShutterEndInfo>): void

监听拍照曝光结束捕获，通过注册回调函数获取结果。使用callback异步回调。

当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'frameShutterEnd'，photoOutput创建成功后可监听。 |
| callback | AsyncCallback<FrameShutterEndInfo> | 是 | 回调函数，用于获取相关信息。该回调返回表示拍照曝光结束。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function callback(err: BusinessError, frameShutterEndInfo: camera.FrameShutterEndInfo): void {
  if (err !== undefined && err.code !== 0) {
    console.error(`Callback Error, errorCode: ${err.code}`);
    return;
  }
  console.info(`CaptureId for frame : ${frameShutterEndInfo.captureId}`);
}

function registerPhotoOutputFrameShutterEnd(photoOutput: camera.PhotoOutput): void {
  photoOutput.on('frameShutterEnd', callback);
}
```

#### off('frameShutterEnd')12+

off(type: 'frameShutterEnd', callback?: AsyncCallback<FrameShutterEndInfo>): void

注销监听拍照曝光结束捕获。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'frameShutterEnd'，photoOutput创建成功后可监听。 |
| callback | AsyncCallback<FrameShutterEndInfo> | 否 | 回调函数，如果指定参数则取消对应callback（callback对象不可是匿名函数），否则取消所有callback。 |

**示例：**

```ets
function unregisterPhotoOutputFrameShutterEnd(photoOutput: camera.PhotoOutput): void {
  photoOutput.off('frameShutterEnd');
}
```

#### on('captureReady')12+

on(type: 'captureReady', callback: AsyncCallback<void>): void

监听可拍下一张，通过注册回调函数获取结果。使用callback异步回调。

当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'captureReady'，photoOutput创建成功后可监听。当下一张可拍时可触发该事件发生并返回相应信息。 |
| callback | AsyncCallback<void> | 是 | 回调函数，用于获取相关信息。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function callback(err: BusinessError): void {
  if (err !== undefined && err.code !== 0) {
    console.error(`Callback Error, errorCode: ${err.code}`);
    return;
  }
  console.info(`photo capture ready`);
}

function registerPhotoOutputCaptureReady(photoOutput: camera.PhotoOutput): void {
  photoOutput.on('captureReady', callback);
}
```

#### off('captureReady')12+

off(type: 'captureReady', callback?: AsyncCallback<void>): void

注销监听可拍下一张。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'captureReady'，photoOutput创建成功后可监听。 |
| callback | AsyncCallback<void> | 否 | 回调函数，如果指定参数则取消对应callback（callback对象不可是匿名函数），否则取消所有callback。 |

**示例：**

```ets
function unregisterPhotoOutputCaptureReady(photoOutput: camera.PhotoOutput): void {
  photoOutput.off('captureReady');
}
```

#### on('estimatedCaptureDuration')12+

on(type: 'estimatedCaptureDuration', callback: AsyncCallback<number>): void

监听预估的拍照时间，通过注册回调函数获取结果。使用callback异步回调。

当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'estimatedCaptureDuration'，photoOutput创建成功后可监听。拍照完全结束可触发该事件发生并返回相应信息。 |
| callback | AsyncCallback<number> | 是 | 回调函数，用于获取预估的单次拍照底层出sensor采集帧时间，单位：毫秒。如果上报-1，代表没有预估时间。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function callback(err: BusinessError, duration: number): void {
  if (err !== undefined && err.code !== 0) {
    console.error(`Callback Error, errorCode: ${err.code}`);
    return;
  }
  console.info(`photo estimated capture duration : ${duration}`);
}

function registerPhotoOutputEstimatedCaptureDuration(photoOutput: camera.PhotoOutput): void {
  photoOutput.on('estimatedCaptureDuration', callback);
}
```

#### off('estimatedCaptureDuration')12+

off(type: 'estimatedCaptureDuration', callback?: AsyncCallback<number>): void

注销监听预估的拍照时间。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'estimatedCaptureDuration'，photoOutput创建成功后可监听。 |
| callback | AsyncCallback<number> | 否 | 回调函数，如果指定参数则取消对应callback（callback对象不可是匿名函数），否则取消所有callback。 |

**示例：**

```ets
function unregisterPhotoOutputEstimatedCaptureDuration(photoOutput: camera.PhotoOutput): void {
  photoOutput.off('estimatedCaptureDuration');
}
```

#### on('error')

on(type: 'error', callback: ErrorCallback): void

监听拍照输出发生错误，通过注册回调函数获取结果。使用callback异步回调。

当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'error'，photoOutput创建成功后可监听。拍照接口调用时出现错误触发该事件并返回错误信息。 |
| callback | ErrorCallback | 是 | 回调函数，用于获取错误信息。返回错误码，错误码类型[CameraErrorCode](../enums/Enums.md#ZH-CN_TOPIC_0000002497445814__cameraerrorcode)。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function callback(err: BusinessError): void {
  console.error(`Photo output error code: ${err.code}`);
}

function registerPhotoOutputError(photoOutput: camera.PhotoOutput): void {
  photoOutput.on('error', callback);
}
```

#### off('error')

off(type: 'error', callback?: ErrorCallback): void

注销监听拍照输出发生错误。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'error'，photoOutput创建成功后可监听。 |
| callback | ErrorCallback | 否 | 回调函数，如果指定参数则取消对应callback（callback对象不可是匿名函数），否则取消所有callback。 |

**示例：**

```ets
function unregisterPhotoOutputError(photoOutput: camera.PhotoOutput): void {
  photoOutput.off('error');
}
```

#### getActiveProfile12+

getActiveProfile(): Profile

获取当前生效的配置信息。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Profile | 当前生效的配置信息 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](Camera错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400201 | Camera service fatal error. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function testGetActiveProfile(photoOutput: camera.PhotoOutput): camera.Profile | undefined {
  let activeProfile: camera.Profile | undefined = undefined;
  try {
    activeProfile = photoOutput.getActiveProfile();
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`The photoOutput.getActiveProfile call failed. error code: ${err.code}`);
  }
  return activeProfile;
}
```

#### getPhotoRotation12+

getPhotoRotation(deviceDegree?: number): [ImageRotation](../enums/Enums.md#ZH-CN_TOPIC_0000002497445814__imagerotation)

获取拍照旋转角度。

- 设备自然方向：设备默认使用方向。例如，直板机默认使用方向为竖屏（充电口向下）。

- 相机镜头角度：值等于相机图像顺时针旋转到设备自然方向的角度。例如，直板机后置相机传感器是横屏安装的，所以需要顺时针旋转90度到设备自然方向。

模型约束： 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceDegree | number | 否 | 设备旋转角度，单位度，取值范围：[0, 360]。 若入参超过该范围，则取入参除以360的余数。 从API version 23开始，入参deviceDegree为可选参数，当不传入参数时，由系统获取deviceDegree进行拍照旋转角度计算。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ImageRotation](../enums/Enums.md#ZH-CN_TOPIC_0000002497445814__imagerotation) | 返回拍照旋转角度。若接口调用失败，返回undefined。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](Camera错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400201 | Camera service fatal error. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function testGetPhotoRotation(photoOutput: camera.PhotoOutput, deviceDegree : number): camera.ImageRotation {
  let photoRotation: camera.ImageRotation = camera.ImageRotation.ROTATION_0;
  try {
    photoRotation = photoOutput.getPhotoRotation(deviceDegree);
    console.info(`Photo rotation is: ${photoRotation}`);
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`The photoOutput.getPhotoRotation call failed. error code: ${err.code}`);
  }
  return photoRotation;
}

function testGetPhotoRotationWithOutParam(photoOutput: camera.PhotoOutput): camera.ImageRotation {
  let photoRotation: camera.ImageRotation = camera.ImageRotation.ROTATION_0;
  try {
    photoRotation = photoOutput.getPhotoRotation();
    console.info(`Photo rotation is: ${photoRotation}`);
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`The photoOutput.testGetPhotoRotationWithOutParam call failed. error code: ${err.code}`);
  }
  return photoRotation;
}
```

#### on('captureStart')(deprecated)

on(type: 'captureStart', callback: AsyncCallback<number>): void

监听拍照开始，通过注册回调函数获取Capture ID。使用callback异步回调。


从 API version 10开始支持，从API version 11开始废弃。建议使用[on('captureStartWithInfo')](#ZH-CN_TOPIC_0000002553201877__oncapturestartwithinfo11)替代。

当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'captureStart'，photoOutput创建成功后可监听。每次拍照，底层开始曝光时触发该事件并返回。 |
| callback | AsyncCallback<number> | 是 | 使用callback的方式获取Capture ID。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function callback(err: BusinessError, captureId: number): void {
  if (err !== undefined && err.code !== 0) {
    console.error(`Callback Error, errorCode: ${err.code}`);
    return;
  }
  console.info(`photo capture started, captureId : ${captureId}`);
}

function registerPhotoOutputCaptureStart(photoOutput: camera.PhotoOutput): void {
  photoOutput.on('captureStart', callback);
}
```

#### off('captureStart')(deprecated)

off(type: 'captureStart', callback?: AsyncCallback<number>): void

注销拍照开始的监听。


从 API version 10开始支持，从API version 11开始废弃。建议使用[off('captureStartWithInfo')](#ZH-CN_TOPIC_0000002553201877__offcapturestartwithinfo11)替代。

当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'captureStart'，photoOutput创建成功后可监听。 |
| callback | AsyncCallback<number> | 否 | 回调函数，如果指定参数则取消对应callback（callback对象不可是匿名函数），否则取消所有callback。 |

**示例：**

```ets
function unregisterPhotoOutputCaptureStart(photoOutput: camera.PhotoOutput): void {
  photoOutput.off('captureStart');
}
```

#### is[PhotoQualityPrioritization](../enums/Enums.md#ZH-CN_TOPIC_0000002497445814__photoqualityprioritization21)Supported21+

is[PhotoQualityPrioritization](../enums/Enums.md#ZH-CN_TOPIC_0000002497445814__photoqualityprioritization21)Supported(qualityPrioritization: PhotoQualityPrioritization): boolean

检查是否支持指定的拍照画质优先策略。

**元服务API：** 从API version 21开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| qualityPrioritization | [PhotoQualityPrioritization](../enums/Enums.md#ZH-CN_TOPIC_0000002497445814__photoqualityprioritization21) | 是 | 要检查的拍照画质优先策略。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 是否支持指定的拍照画质优先策略。true表示支持，false表示不支持。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](Camera错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400201 | Camera service fatal error, reconfiguring streams is needed to recover from failure. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { camera } from '@kit.CameraKit';

let photoOutput: camera.PhotoOutput;

function isPhotoQualityPrioritizationSupported(qualityPrioritization: camera.PhotoQualityPrioritization): boolean {
  let isSupported: boolean = false;
  try {
    isSupported = photoOutput.isPhotoQualityPrioritizationSupported(qualityPrioritization);
  } catch (error) {
    let err = error as BusinessError;
    console.error(`The isPhotoQualityPrioritizationSupported call failed. error code: ${err.code}`);
  }
  return isSupported;
}
```

#### set[PhotoQualityPrioritization](../enums/Enums.md#ZH-CN_TOPIC_0000002497445814__photoqualityprioritization21)21+

set[PhotoQualityPrioritization](../enums/Enums.md#ZH-CN_TOPIC_0000002497445814__photoqualityprioritization21)(qualityPrioritization: PhotoQualityPrioritization): void

设置拍照画质优先策略。

设置之前，可先使用方法[isPhotoQualityPrioritizationSupported](#ZH-CN_TOPIC_0000002553201877__isphotoqualityprioritizationsupported21)对设备是否支持指定的拍照画质优先策略进行检查。

**元服务API：** 从API version 21开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| qualityPrioritization | [PhotoQualityPrioritization](../enums/Enums.md#ZH-CN_TOPIC_0000002497445814__photoqualityprioritization21) | 是 | 要设置的拍照画质优先策略。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](Camera错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400102 | Operation not allowed. |
| 7400201 | Camera service fatal error, reconfiguring streams is needed to recover from failure. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { camera } from '@kit.CameraKit';

let photoOutput: camera.PhotoOutput;

function setPhotoQualityPrioritization(qualityPrioritization: camera.PhotoQualityPrioritization): void {
  try {
    photoOutput.setPhotoQualityPrioritization(qualityPrioritization);
  } catch (error) {
    let err = error as BusinessError;
    console.error(`The setPhotoQualityPrioritization call failed. error code: ${err.code}`);
  }
```