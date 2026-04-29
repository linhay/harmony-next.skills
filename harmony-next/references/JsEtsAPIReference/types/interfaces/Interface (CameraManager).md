# Interface (CameraManager)

相机管理器类，使用前需要通过[getCameraManager](Functions.md#ZH-CN_TOPIC_0000002522241900__cameragetcameramanager)接口获取相机管理实例。


本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { camera } from '@kit.CameraKit';
```

#### getSupportedCameras

getSupportedCameras(): Array<CameraDevice>

获取支持的相机设备对象，同步返回结果。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<CameraDevice> | 相机设备列表。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function getSupportedCameras(cameraManager: camera.CameraManager): Array<camera.CameraDevice> {
  let cameras: Array<camera.CameraDevice> = [];
  try {
    cameras = cameraManager.getSupportedCameras();
  } catch (error) {
    let err = error as BusinessError;
    console.error(`The getSupportedCameras call failed. error code: ${err.code}`);
  }
  return cameras;
}
```

#### getSupported[SceneMode](../enums/Enums.md#ZH-CN_TOPIC_0000002497445814__scenemode11)s11+

getSupported[SceneMode](../enums/Enums.md#ZH-CN_TOPIC_0000002497445814__scenemode11)s(camera: CameraDevice): Array<SceneMode>

获取指定的相机设备对象支持的模式，同步返回结果。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| camera | CameraDevice | 是 | 相机设备，通过getSupportedCameras接口获取。传参异常时，会返回错误码7400101。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<[SceneMode](../enums/Enums.md#ZH-CN_TOPIC_0000002497445814__scenemode11)> | 相机支持的模式列表。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function getSupportedSceneModes(cameraManager: camera.CameraManager, camera: camera.CameraDevice): Array<camera.SceneMode> {
  let modes: Array<camera.SceneMode> = [];
  try {
    modes = cameraManager.getSupportedSceneModes(camera);
  } catch (error) {
    let err = error as BusinessError;
    console.error(`The getSupportedSceneModes call failed. error code: ${err.code}`);
  }
  return modes;
}
```

#### getSupportedOutputCapability11+

getSupportedOutputCapability(camera: CameraDevice, mode: [SceneMode](../enums/Enums.md#ZH-CN_TOPIC_0000002497445814__scenemode11)): CameraOutputCapability

查询相机设备在指定模式下支持的输出能力，同步返回结果。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| camera | CameraDevice | 是 | 相机设备，通过 getSupportedCameras 接口获取。 |
| mode | [SceneMode](../enums/Enums.md#ZH-CN_TOPIC_0000002497445814__scenemode11) | 是 | 相机模式，通过 getSupportedSceneModes 接口获取。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| CameraOutputCapability | 相机输出能力。 |

**示例：**

```ets
function getSupportedOutputCapability(camera: camera.CameraDevice, cameraManager: camera.CameraManager, sceneMode: camera.SceneMode): camera.CameraOutputCapability {
  let cameraOutputCapability: camera.CameraOutputCapability = cameraManager.getSupportedOutputCapability(camera, sceneMode);
  return cameraOutputCapability;
}
```

**getSupportedFullOutputCapability23+**

getSupportedFullOutputCapability(camera: CameraDevice, mode: [SceneMode](../enums/Enums.md#ZH-CN_TOPIC_0000002497445814__scenemode11)): CameraOutputCapability

查询指定相机在指定模式下支持的完整输出能力，包括未压缩图（YUV）、HEIF和HDR等能力。


使用YUV，HEIF或HDR等能力前，需要先显式调用此方法确保获取完整输出能力。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从API version 23开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Multimedia.Camera.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| camera | CameraDevice | 是 | 相机设备信息，通过getSupportedCameras接口获取。 |
| mode | [SceneMode](../enums/Enums.md#ZH-CN_TOPIC_0000002497445814__scenemode11) | 是 | 相机模式，通过getSupportedSceneModes接口获取。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| CameraOutputCapability | 相机输出能力。 |

示例：

```ets
import { camera } from '@kit.CameraKit';

function getSupportedFullOutputCapability(camera: camera.CameraDevice, cameraManager: camera.CameraManager, sceneMode: camera.SceneMode): camera.CameraOutputCapability {
  let cameraOutputCapability: camera.CameraOutputCapability = cameraManager.getSupportedFullOutputCapability(camera, sceneMode);
  return cameraOutputCapability;
}
```

#### isCameraMuted

isCameraMuted(): boolean

查询当前相机是否禁用。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回true表示相机被禁用，返回false表示相机未被禁用。 |

**示例：**

```ets
function isCameraMuted(cameraManager: camera.CameraManager): boolean {
  let isMuted: boolean = cameraManager.isCameraMuted();
  return isMuted;
}
```

#### createCameraInput

createCameraInput(camera: CameraDevice): CameraInput

使用CameraDevice对象创建CameraInput实例，同步返回结果。

该接口使用前首先通过[getSupportedCameras](#ZH-CN_TOPIC_0000002522081908__getsupportedcameras)接口查询当前设备支持的相机设备信息列表，开发者需要根据具体使用场景选择符合需求的相机设备，然后使用该接口创建CameraInput实例。

**需要权限：** ohos.permission.CAMERA

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| camera | CameraDevice | 是 | CameraDevice对象，通过 getSupportedCameras 接口获取。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| CameraInput | 返回CameraInput实例。接口调用失败会返回相应错误码，错误码类型为[CameraErrorCode](../enums/Enums.md#ZH-CN_TOPIC_0000002497445814__cameraerrorcode)。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码]([Camera错误码](../../errors/Camera错误码.md).md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400101 | Parameter missing or parameter type incorrect. |
| 7400102 | Operation not allowed. |
| 7400201 | Camera service fatal error. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function createCameraInput(camera: camera.CameraDevice, cameraManager: camera.CameraManager): camera.CameraInput | undefined {
  let cameraInput: camera.CameraInput | undefined = undefined;
  try {
    cameraInput = cameraManager.createCameraInput(camera);
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`The createCameraInput call failed. error code: ${err.code}`);
  }
  return cameraInput;
}
```

#### createCameraInput

createCameraInput(position: [CameraPosition](../enums/Enums.md#ZH-CN_TOPIC_0000002497445814__cameraposition), type: CameraType): CameraInput

根据相机位置和类型创建CameraInput实例，同步返回结果。

该接口使用前需要开发者根据应用具体使用场景自行指定相机位置和类型，例如打开前置相机进入自拍功能。

**需要权限：** ohos.permission.CAMERA

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| position | [CameraPosition](../enums/Enums.md#ZH-CN_TOPIC_0000002497445814__cameraposition) | 是 | 相机位置，首先通过 getSupportedCameras 接口获取支持的相机设备对象，然后根据返回的相机设备对象获取设备位置信息。 |
| type | [CameraType](../enums/Enums.md#ZH-CN_TOPIC_0000002497445814__cameratype) | 是 | 相机类型，首先通过 getSupportedCameras 接口获取支持的相机设备对象，然后根据返回的相机设备对象获取设备类型信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| CameraInput | 返回CameraInput实例。接口调用失败会返回相应错误码，错误码类型为[CameraErrorCode](../enums/Enums.md#ZH-CN_TOPIC_0000002497445814__cameraerrorcode)。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](Camera错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400101 | Parameter missing or parameter type incorrect. |
| 7400102 | Operation not allowed. |
| 7400201 | Camera service fatal error. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function createCameraInput(camera: camera.CameraDevice, cameraManager: camera.CameraManager): camera.CameraInput | undefined {
  let position: camera.CameraPosition = camera.cameraPosition;
  let type: camera.CameraType = camera.cameraType;
  let cameraInput: camera.CameraInput | undefined = undefined;
  try {
    cameraInput = cameraManager.createCameraInput(position, type);
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`The createCameraInput call failed. error code: ${err.code}`);
  }
  return cameraInput;
}
```

#### createPreviewOutput

createPreviewOutput(profile: Profile, surfaceId: string): PreviewOutput

创建预览输出对象，同步返回结果。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| profile | Profile | 是 | 支持的预览配置信息，通过getSupportedOutputCapability接口获取。 |
| surfaceId | string | 是 | 从[XComponent](../../topics/components/XComponent.md)或者ImageReceiver组件获取的surfaceId。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| PreviewOutput | PreviewOutput实例。接口调用失败会返回相应错误码，错误码类型[CameraErrorCode](../enums/Enums.md#ZH-CN_TOPIC_0000002497445814__cameraerrorcode)。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](Camera错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400101 | Parameter missing or parameter type incorrect. |
| 7400201 | Camera service fatal error. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function createPreviewOutput(cameraOutputCapability: camera.CameraOutputCapability, cameraManager: camera.CameraManager, surfaceId: string): camera.PreviewOutput | undefined {
  let profile: camera.Profile = cameraOutputCapability.previewProfiles[0];
  let previewOutput: camera.PreviewOutput | undefined = undefined;
  try {
    previewOutput = cameraManager.createPreviewOutput(profile, surfaceId);
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`The createPreviewOutput call failed. error code: ${err.code}`);
  }
  return previewOutput;
}
```

#### createPreviewOutput12+

createPreviewOutput(surfaceId: string): PreviewOutput

创建无配置信息的预览输出对象，同步返回结果。该接口需配合[preconfig](Interface (PhotoSession).md#ZH-CN_TOPIC_0000002522081916__preconfig12)一起使用。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| surfaceId | string | 是 | 从[XComponent](../../topics/components/XComponent.md)或者ImageReceiver组件获取的surfaceId。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| PreviewOutput | PreviewOutput实例。接口调用失败会返回相应错误码，错误码类型[CameraErrorCode](../enums/Enums.md#ZH-CN_TOPIC_0000002497445814__cameraerrorcode)。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](Camera错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400101 | Parameter missing or parameter type incorrect. |
| 7400201 | Camera service fatal error. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function createPreviewOutput(cameraManager: camera.CameraManager, surfaceId: string): camera.PreviewOutput | undefined {
  let previewOutput: camera.PreviewOutput | undefined = undefined;
  try {
    previewOutput = cameraManager.createPreviewOutput(surfaceId);
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`The createPreviewOutput call failed. error code: ${err.code}`);
  }
  return previewOutput;
}
```

#### createPhotoOutput11+

createPhotoOutput(profile?: Profile): PhotoOutput

创建拍照输出对象，同步返回结果。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| profile | Profile | 否 | 支持的拍照配置信息，通过getSupportedOutputCapability接口获取。 API version 11时，该参数必填；从API version 12开始，如果使用preconfig进行预配置，传入profile参数会覆盖preconfig的预配置参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| PhotoOutput | PhotoOutput实例。接口调用失败会返回相应错误码，错误码类型[CameraErrorCode](../enums/Enums.md#ZH-CN_TOPIC_0000002497445814__cameraerrorcode)。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](Camera错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400101 | Parameter missing or parameter type incorrect. |
| 7400201 | Camera service fatal error. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function createPhotoOutput(cameraOutputCapability: camera.CameraOutputCapability, cameraManager: camera.CameraManager): camera.PhotoOutput | undefined {
  let profile: camera.Profile = cameraOutputCapability.photoProfiles[0];
  let photoOutput: camera.PhotoOutput | undefined = undefined;
  try {
    photoOutput = cameraManager.createPhotoOutput(profile);
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`The createPhotoOutput call failed. error code: ${err.code}`);
  }
  return photoOutput;
}
```

#### createVideoOutput

createVideoOutput(profile: VideoProfile, surfaceId: string): VideoOutput

创建录像输出对象，同步返回结果。

在录像模式下，使能SDR或HDR_VIVID拍摄效果时，CameraFormat与ColorSpace必须按照下列表格中的对应关系配置，若不满足表格中CameraFormat与ColorSpace配置，会导致预览异常等问题。

| SDR/HDR拍摄 | CameraFormat | ColorSpace |
| --- | --- | --- |
| SDR | CAMERA_FORMAT_YUV_420_SP | BT709_LIMIT |
| HDR_VIVID | CAMERA_FORMAT_YCRCB_P010 CAMERA_FORMAT_YCBCR_P010 | BT2020_HLG_LIMIT BT2020_HLG_FULL |

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| profile | VideoProfile | 是 | 支持的录像配置信息，通过getSupportedOutputCapability接口获取。 |
| surfaceId | string | 是 | 从AVRecorder获取的surfaceId。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| VideoOutput | VideoOutput实例。接口调用失败会返回相应错误码，错误码类型[CameraErrorCode](../enums/Enums.md#ZH-CN_TOPIC_0000002497445814__cameraerrorcode)。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](Camera错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400101 | Parameter missing or parameter type incorrect. |
| 7400201 | Camera service fatal error. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function createVideoOutput(cameraOutputCapability: camera.CameraOutputCapability, cameraManager: camera.CameraManager, surfaceId: string): camera.VideoOutput | undefined {
  let profile: camera.VideoProfile = cameraOutputCapability.videoProfiles[0];
  let videoOutput: camera.VideoOutput | undefined = undefined;
  try {
    videoOutput = cameraManager.createVideoOutput(profile, surfaceId);
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`The createVideoOutput call failed. error code: ${err.code}`);
  }
  return videoOutput;
}
```

#### createVideoOutput12+

createVideoOutput(surfaceId: string): VideoOutput

创建无配置信息的录像输出对象，同步返回结果。该接口需配合[preconfig](Interface (VideoSession).md#ZH-CN_TOPIC_0000002553201881__preconfig12)功能一起使用。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| surfaceId | string | 是 | 从AVRecorder获取的surfaceId。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| VideoOutput | VideoOutput实例。接口调用失败会返回相应错误码，错误码类型[CameraErrorCode](../enums/Enums.md#ZH-CN_TOPIC_0000002497445814__cameraerrorcode)。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](Camera错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400101 | Parameter missing or parameter type incorrect. |
| 7400201 | Camera service fatal error. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function createVideoOutput(cameraManager: camera.CameraManager, surfaceId: string): camera.VideoOutput | undefined {
  let videoOutput: camera.VideoOutput | undefined = undefined;
  try {
    videoOutput = cameraManager.createVideoOutput(surfaceId);
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`The createVideoOutput call failed. error code: ${err.code}`);
  }
  return videoOutput;
}
```

#### createMetadataOutput

createMetadataOutput(metadataObjectTypes: Array<[MetadataObjectType](../enums/Enums.md#ZH-CN_TOPIC_0000002497445814__metadataobjecttype)>): MetadataOutput

创建metadata流输出对象，同步返回结果。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| metadataObjectTypes | Array<[MetadataObjectType](../enums/Enums.md#ZH-CN_TOPIC_0000002497445814__metadataobjecttype)> | 是 | metadata流类型信息，通过getSupportedOutputCapability接口获取。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| MetadataOutput | MetadataOutput实例。接口调用失败会返回相应错误码，错误码类型[CameraErrorCode](../enums/Enums.md#ZH-CN_TOPIC_0000002497445814__cameraerrorcode)。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](Camera错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400101 | Parameter missing or parameter type incorrect. |
| 7400201 | Camera service fatal error. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function createMetadataOutput(cameraManager: camera.CameraManager, cameraOutputCapability: camera.CameraOutputCapability): void {
  let metadataObjectTypes: Array<camera.MetadataObjectType> = cameraOutputCapability.supportedMetadataObjectTypes;
  let metadataOutput: camera.MetadataOutput | undefined = undefined;
  try {
    metadataOutput = cameraManager.createMetadataOutput(metadataObjectTypes);
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`createMetadataOutput error. error code: ${err.code}`);
  }
```

#### createSession11+

createSession<T extends Session>(mode: [SceneMode](../enums/Enums.md#ZH-CN_TOPIC_0000002497445814__scenemode11)): T

创建指定[SceneMode](../enums/Enums.md#ZH-CN_TOPIC_0000002497445814__scenemode11)的Session实例，同步返回结果。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [SceneMode](../enums/Enums.md#ZH-CN_TOPIC_0000002497445814__scenemode11) | 是 | 相机支持的模式。如果传入的参数异常（如超出范围、传入null或未定义等），实际接口不会生效。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | Session实例。接口调用失败会返回相应的错误码，错误码类型为[CameraErrorCode](../enums/Enums.md#ZH-CN_TOPIC_0000002497445814__cameraerrorcode)。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](Camera错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400101 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3.Parameter verification failed. |
| 7400201 | Camera service fatal error. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function createSession(cameraManager: camera.CameraManager, mode: camera.SceneMode): camera.Session | undefined {
  let photoSession: camera.PhotoSession | undefined = undefined;
  try {
    photoSession = cameraManager.createSession(mode) as camera.PhotoSession;
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`createCaptureSession error. error code: ${err.code}`);
  }
  return photoSession;
}
```

#### on('cameraStatus')

on(type: 'cameraStatus', callback: AsyncCallback<CameraStatusInfo>): void

相机设备状态回调，通过注册回调函数获取相机的状态变化。使用callback异步回调。

当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'cameraStatus'。cameraManager对象获取成功后可监听。目前只支持对设备打开或者关闭会触发该事件并返回对应信息。 |
| callback | AsyncCallback<CameraStatusInfo> | 是 | 回调函数，用于获取镜头状态变化信息。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function callback(err: BusinessError, cameraStatusInfo: camera.CameraStatusInfo): void {
  if (err !== undefined && err.code !== 0) {
    console.error('cameraStatus with errorCode = ' + err.code);
    return;
  }
  console.info(`camera : ${cameraStatusInfo.camera.cameraId}`);
  console.info(`status: ${cameraStatusInfo.status}`);
}

function registerCameraStatus(cameraManager: camera.CameraManager): void {
  cameraManager.on('cameraStatus', callback);
}
```

#### off('cameraStatus')

off(type: 'cameraStatus', callback?: AsyncCallback<CameraStatusInfo>): void

相机设备状态注销回调，通过注销回调函数取消获取相机的状态变化。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'cameraStatus'。cameraManager对象获取成功后可监听。 |
| callback | AsyncCallback<CameraStatusInfo> | 否 | 回调函数，如果指定参数则取消对应callback（callback对象不可是匿名函数），否则取消所有callback。 |

**示例：**

```ets
function unregisterCameraStatus(cameraManager: camera.CameraManager): void {
  cameraManager.off('cameraStatus');
}
```

#### on('foldStatusChange')12+

on(type: 'foldStatusChange', callback: AsyncCallback<FoldStatusInfo>): void

注册折叠设备折叠状态变化的监听。使用callback异步回调。

当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'foldStatusChange'。表示折叠设备折叠状态发生变化。 |
| callback | AsyncCallback<FoldStatusInfo> | 是 | 回调函数。返回折叠设备折叠信息。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function callback(err: BusinessError, foldStatusInfo: camera.FoldStatusInfo): void {
  if (err !== undefined && err.code !== 0) {
    console.error('foldStatusChange with errorCode = ' + err.code);
    return;
  }
  console.info(`camera length: ${foldStatusInfo.supportedCameras.length}`);
  console.info(`foldStatus: ${foldStatusInfo.foldStatus}`);
}

function registerFoldStatusChange(cameraManager: camera.CameraManager): void {
  cameraManager.on('foldStatusChange', callback);
}
```

#### off('foldStatusChange')12+

off(type: 'foldStatusChange', callback?: AsyncCallback<FoldStatusInfo>): void

关闭折叠设备折叠状态变化的监听。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'foldStatusChange'。表示折叠设备折叠状态发生变化。 |
| callback | AsyncCallback<FoldStatusInfo> | 否 | 回调函数，返回折叠设备折叠信息。如果指定参数则取消对应callback（callback对象不可是匿名函数），否则取消所有callback。 |

**示例：**

```ets
function unregisterFoldStatusChange(cameraManager: camera.CameraManager): void {
  cameraManager.off('foldStatusChange');
}
```

#### isTorchSupported11+

isTorchSupported(): boolean

检测设备是否支持手电筒。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回true表示设备支持手电筒，返回false表示设备不支持手电。若接口调用失败，返回undefined。 |

**示例：**

```ets
function isTorchSupported(cameraManager: camera.CameraManager): boolean {
  let isSupported = cameraManager.isTorchSupported();
  return isSupported;
}
```

#### is[TorchMode](../enums/Enums.md#ZH-CN_TOPIC_0000002497445814__torchmode11)Supported11+

is[TorchMode](../enums/Enums.md#ZH-CN_TOPIC_0000002497445814__torchmode11)Supported(mode: TorchMode): boolean

检测是否支持设置的手电筒模式。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [TorchMode](../enums/Enums.md#ZH-CN_TOPIC_0000002497445814__torchmode11) | 是 | 手电筒模式。传参为null或者undefined，作为0处理，手电筒关闭。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回true表示设备支持设置的手电筒模式，返回false表示设备不支持的手电筒模式。若接口调用失败，返回undefined。 |

**示例：**

```ets
function isTorchModeSupported(cameraManager: camera.CameraManager, torchMode: camera.TorchMode): boolean {
  let isSupported = cameraManager.isTorchModeSupported(torchMode);
  return isSupported;
}
```

#### get[TorchMode](../enums/Enums.md#ZH-CN_TOPIC_0000002497445814__torchmode11)11+

get[TorchMode](../enums/Enums.md#ZH-CN_TOPIC_0000002497445814__torchmode11)(): TorchMode

获取当前设备手电筒模式。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [TorchMode](../enums/Enums.md#ZH-CN_TOPIC_0000002497445814__torchmode11) | 返回设备当前手电筒模式。 |

**示例：**

```ets
function getTorchMode(cameraManager: camera.CameraManager): camera.TorchMode | undefined {
  let torchMode: camera.TorchMode | undefined = undefined;
  torchMode = cameraManager.getTorchMode();
  return torchMode;
}
```

#### set[TorchMode](../enums/Enums.md#ZH-CN_TOPIC_0000002497445814__torchmode11)11+

set[TorchMode](../enums/Enums.md#ZH-CN_TOPIC_0000002497445814__torchmode11)(mode: TorchMode): void

设置设备手电筒模式。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [TorchMode](../enums/Enums.md#ZH-CN_TOPIC_0000002497445814__torchmode11) | 是 | 手电筒模式。传参为null或者undefined，作为0处理，手电筒关闭。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](Camera错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400102 | Operation not allowed. |
| 7400201 | Camera service fatal error. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function setTorchMode(cameraManager: camera.CameraManager, torchMode: camera.TorchMode): void {
  try {
    cameraManager.setTorchMode(torchMode);
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`The setTorchMode call failed. error code: ${err.code}`);
  }
```

#### on('torchStatusChange')11+

on(type: 'torchStatusChange', callback: AsyncCallback<TorchStatusInfo>): void

手电筒状态变化回调，通过注册回调函数获取手电筒状态变化。使用callback异步回调。

当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'torchStatusChange'。cameraManager对象获取成功后可监听。目前只支持手电筒打开，手电筒关闭，手电筒不可用，手电筒恢复可用会触发该事件并返回对应信息。 |
| callback | AsyncCallback<TorchStatusInfo> | 是 | 回调函数，用于获取手电筒状态变化信息。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function callback(err: BusinessError, torchStatusInfo: camera.TorchStatusInfo): void {
  if (err !== undefined && err.code !== 0) {
    console.error(`Callback Error, errorCode: ${err.code}`);
    return;
  }
  console.info(`onTorchStatusChange, isTorchAvailable: ${torchStatusInfo.isTorchAvailable}, isTorchActive: ${torchStatusInfo.isTorchActive}, level: ${torchStatusInfo.torchLevel}`);
}

function registerTorchStatusChange(cameraManager: camera.CameraManager): void {
  cameraManager.on('torchStatusChange', callback);
}
```

#### off('torchStatusChange')11+

off(type: 'torchStatusChange', callback?: AsyncCallback<TorchStatusInfo>): void

手电筒状态变化注销回调，通过注销回调函数取消获取手电筒状态变化。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'torchStatusChange'。cameraManager对象获取成功后可监听。 |
| callback | AsyncCallback<TorchStatusInfo> | 否 | 回调函数，如果指定参数则取消对应callback（callback对象不可是匿名函数），否则取消所有callback。 |

**示例：**

```ets
function unregisterTorchStatusChange(cameraManager: camera.CameraManager): void {
  cameraManager.off('torchStatusChange');
}
```

#### getCameraDevice18+

getCameraDevice(position:[CameraPosition](../enums/Enums.md#ZH-CN_TOPIC_0000002497445814__cameraposition), type: CameraType): CameraDevice

根据相机位置和相机类型查询对应相机。

获取指定[CameraPosition](Enums.md#ZH-CN_TOPIC_0000002553361841__cameraposition)和[CameraType](Enums.md#ZH-CN_TOPIC_0000002553361841__cameratype)的相机镜头，如果该接口返回结果为undefined，表示当前设备未查询到该镜头。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| position | [CameraPosition](../enums/Enums.md#ZH-CN_TOPIC_0000002497445814__cameraposition) | 是 | 需要得到的CameraDevice对象对应的CameraPosition条件。 |
| type | [CameraType](../enums/Enums.md#ZH-CN_TOPIC_0000002497445814__cameratype) | 是 | 需要得到的CameraDevice对象对应的CameraType条件。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| CameraDevice | 根据相机位置和相机类型查询的对应相机。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](Camera错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400201 | Camera service fatal error. |

**示例：**

```ets
import { camera } from '@kit.CameraKit';
import { BusinessError } from '@kit.BasicServicesKit';

function getCameraDevice(cameraManager: camera.CameraManager, position: camera.CameraPosition, type: camera.CameraType): void {
  try {
    let curCameraDev: camera.CameraDevice | undefined = undefined;
    curCameraDev = cameraManager.getCameraDevice(position, type);
  } catch (error) {
    // 失败返回错误码并处理。
    let err = error as BusinessError;
    console.error(`The getCameraDevice call failed. error code: ${err.code}`);
  }
```

**getCameraDevices23+**

getCameraDevices(position: [CameraPosition](../enums/Enums.md#ZH-CN_TOPIC_0000002497445814__cameraposition), types: Array<CameraType>, connectType: ConnectionType): Array<CameraDevice>

根据相机位置、相机类型数组和连接类型查询符合条件的相机列表。

元服务API： 从API version 23开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Multimedia.Camera.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| position | [CameraPosition](../enums/Enums.md#ZH-CN_TOPIC_0000002497445814__cameraposition) | 是 | 相机的位置。 |
| types | Array<[CameraType](../enums/Enums.md#ZH-CN_TOPIC_0000002497445814__cameratype)> | 是 | 相机类型数组。 |
| connectType | ConnectionType | 是 | 相机的连接类型。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Array<CameraDevice> | 根据相机位置、相机类型数组和连接类型查询符合条件的相机列表。 |

错误码：

以下错误码的详细介绍请参见[Camera错误码](Camera错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400201 | Camera service fatal error. |

示例：

```ets
import { camera } from '@kit.CameraKit';
import { BusinessError } from '@kit.BasicServicesKit';

function getCameraDevices(cameraManager: camera.CameraManager, position: camera.CameraPosition, types: Array<camera.CameraType>, connectType: camera.ConnectionType): void {
  try {
    let cameraDevs: Array<camera.CameraDevice> = [];
    cameraDevs = cameraManager.getCameraDevices(position, types, connectType);
  } catch (error) {
    // 失败返回错误码并处理。
    let err = error as BusinessError;
    console.error(`The getCameraDevices call failed. error code: ${err.code}`);
}
```

#### getCameraConcurrentInfos18+

getCameraConcurrentInfos(cameras: Array<CameraDevice>): Array<CameraConcurrentInfo>

获取指定相机设备的并发信息。返回空数组表示不支持并发。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| cameras | Array<CameraDevice> | 是 | 一组CameraDevice相机设备，并得到与这一组CameraDevice对应的并发信息，推荐设置为由getCameraDevice获取的前置与后置两个用于并发的相机设备。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<CameraConcurrentInfo> | 一组CameraDevice相机设备对象对应的并发信息，与CameraDevice相机设备一一对应。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](Camera错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400201 | Camera service fatal error. |

**示例：**

```ets
import { camera } from '@kit.CameraKit';
import { BusinessError } from '@kit.BasicServicesKit';

function getCameraConcurrentInfos(cameraManager: camera.CameraManager,
  cameraDeviceArray: Array<camera.CameraDevice>): Array<camera.CameraConcurrentInfo> {
  let cameraConcurrentInfos: Array<camera.CameraConcurrentInfo> = [];
  try {
    cameraConcurrentInfos = cameraManager.getCameraConcurrentInfos(cameraDeviceArray);
  } catch (error) {
    // 失败返回错误码并处理。
    let err = error as BusinessError;
    console.error(`The getCameraConcurrentInfos call failed. error code: ${err.code}`);
  }
  return cameraConcurrentInfos;
}
```

#### getSupportedOutputCapability(deprecated)

getSupportedOutputCapability(camera: CameraDevice): CameraOutputCapability

查询相机设备支持的输出能力，同步返回结果。


从 API version 10开始支持，从API version 11开始废弃。建议使用[getSupportedOutputCapability](#ZH-CN_TOPIC_0000002522081908__getsupportedoutputcapability11)替代。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| camera | CameraDevice | 是 | 相机设备，通过 getSupportedCameras 接口获取。传参异常时，会返回错误码。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| CameraOutputCapability | 相机输出能力。 |

**示例：**

```ets
function getSupportedOutputCapability(camera: camera.CameraDevice, cameraManager: camera.CameraManager): camera.CameraOutputCapability {
  let cameraOutputCapability: camera.CameraOutputCapability = cameraManager.getSupportedOutputCapability(camera);
  return cameraOutputCapability;
}
```

#### createPhotoOutput(deprecated)

createPhotoOutput(profile: Profile, surfaceId: string): PhotoOutput

创建拍照输出对象，同步返回结果。


- 从API version 10开始支持，从API version 11开始废弃。建议使用[createPhotoOutput](#ZH-CN_TOPIC_0000002522081908__createphotooutput11)替代。

- 该接口只支持创建JPEG格式的拍照输出对象。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| profile | Profile | 是 | 支持的拍照配置信息，通过getSupportedOutputCapability接口获取。 |
| surfaceId | string | 是 | 从ImageReceiver获取的surfaceId。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| PhotoOutput | PhotoOutput实例。接口调用失败会返回相应错误码，错误码类型[CameraErrorCode](../enums/Enums.md#ZH-CN_TOPIC_0000002497445814__cameraerrorcode)。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](Camera错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400101 | Parameter missing or parameter type incorrect. |

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function createPhotoOutput(cameraOutputCapability: camera.CameraOutputCapability, cameraManager: camera.CameraManager, surfaceId: string): camera.PhotoOutput | undefined {
  let profile: camera.Profile = cameraOutputCapability.photoProfiles[0];
  let photoOutput: camera.PhotoOutput | undefined = undefined;
  try {
    photoOutput = cameraManager.createPhotoOutput(profile, surfaceId);
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`The createPhotoOutput call failed. error code: ${err.code}`);
  }
  return photoOutput;
}
```

#### createCaptureSession(deprecated)

createCaptureSession(): CaptureSession

创建CaptureSession实例，同步返回结果。


从 API version 10开始支持，从API version 11开始废弃。建议使用[createSession](#ZH-CN_TOPIC_0000002522081908__createsession11)替代。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| CaptureSession | CaptureSession实例。接口调用失败会返回相应错误码，错误码类型[CameraErrorCode](../enums/Enums.md#ZH-CN_TOPIC_0000002497445814__cameraerrorcode)。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](Camera错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400201 | Camera service fatal error. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function createCaptureSession(cameraManager: camera.CameraManager): camera.CaptureSession | undefined {
  let captureSession: camera.CaptureSession | undefined = undefined;
  try {
    captureSession = cameraManager.createCaptureSession();
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`createCaptureSession error. error code: ${err.code}`);
  }
  return captureSession;
}
```