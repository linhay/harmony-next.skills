# @ohos.multimedia.cameraPicker (相机选择器)

本模块提供相机拍照与录制的能力。应用可选择媒体类型实现拍照和录制的功能。调用此类接口时，应用必须在界面UIAbility中调用，否则无法启动cameraPicker应用。

本模块首批接口从API version 11开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { cameraPicker } from '@kit.CameraKit';
```

#### cameraPicker.pick

pick(context: Context, mediaTypes: Array<PickerMediaType>, pickerProfile: PickerProfile): Promise<PickerResult>

拉起相机选择器，根据媒体类型进入相应的模式。使用Promise异步回调。

当应用在阔折叠设备上运行时，如果已在设备展开态下启动相机picker，将设备由展开态切换到折叠态，相机picker被自动推至后台。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用上下文。 |
| mediaTypes | Array<PickerMediaType> | 是 | 媒体类型。 |
| pickerProfile | PickerProfile | 是 | pickerProfile对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<PickerResult> | Promise对象，返回相机选择器的处理结果PickerResult。 |

**示例：**

```ets
import { cameraPicker } from '@kit.CameraKit';
import { camera } from '@kit.CameraKit';
import { BusinessError } from '@kit.BasicServicesKit';

async function demo(context: Context) {
  try {
    let pickerProfile: cameraPicker.PickerProfile = {
      cameraPosition: camera.CameraPosition.CAMERA_POSITION_BACK
    };
    let pickerResult: cameraPicker.PickerResult = await cameraPicker.pick(context,
      [cameraPicker.PickerMediaType.PHOTO, cameraPicker.PickerMediaType.VIDEO], pickerProfile);
    console.info("the pick pickerResult is:" + JSON.stringify(pickerResult));
  } catch (error) {
    let err = error as BusinessError;
    console.error(`the pick call failed. error code: ${err.code}`);
  }
```

#### PickerMediaType

枚举，相机选择器的媒体类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PHOTO | 'photo' | 拍照模式。 |
| VIDEO | 'video' | 录制模式。 |

#### PickerProfile

相机选择器的配置信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| cameraPosition | [camera.CameraPosition](../../types/enums/Enums.md#ZH-CN_TOPIC_0000002497445814__cameraposition) | 否 | 否 | 相机的位置。 |
| saveUri | string | 否 | 是 | 保存配置信息的uri，默认值请参考文件uri。当前saveUri参数为可选参数，若未配置该参数，则拍摄的照片和视频会默认存入媒体库中；若不想将照片和视频存入媒体库中，请自行配置应用沙箱内的文件资源路径，如自行传入资源路径时请确保该文件存在且具备写入权限，否则会保存失败。 |
| videoDuration | number | 否 | 是 | 录制的最大时长（单位：秒）。默认为0，不设置最大录制时长。 |

#### PickerResult

相机选择器的处理结果。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| resultCode | number | 否 | 否 | 处理的结果，成功返回0，失败返回-1。 |
| resultUri | string | 否 | 否 | 返回的uri地址。若saveUri为空，resultUri为公共媒体路径。若saveUri不为空且具备写权限，resultUri与saveUri相同。若saveUri不为空且不具备写权限，则无法获取到resultUri。 |
| mediaType | PickerMediaType | 否 | 否 | 返回的媒体类型。 |