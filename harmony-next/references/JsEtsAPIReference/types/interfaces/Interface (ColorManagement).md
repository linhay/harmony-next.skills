# Interface (ColorManagement)

ColorManagement 继承自 [ColorManagementQuery](Interface (ColorManagementQuery).md)。

色彩管理类，用于设置色彩空间参数。

- 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
- 本Interface首批接口从API version 12开始支持。

#### 导入模块

```ets
import { camera } from '@kit.CameraKit';
```

#### setColorSpace12+

setColorSpace(colorSpace: colorSpaceManager.ColorSpace): void

设置色彩空间。

使用该接口前，必须先通过[getSupportedColorSpaces](Interface (ColorManagementQuery).md#ZH-CN_TOPIC_0000002522081910__getsupportedcolorspaces12)获取当前设备所支持的ColorSpaces。该接口建议在[addOutput](Interface (Session).md#ZH-CN_TOPIC_0000002553201879__addoutput11)之后、[commitConfig](Interface (Session).md#ZH-CN_TOPIC_0000002553201879__commitconfig11-1)之前调用，如果在[commitConfig](Interface (Session).md#ZH-CN_TOPIC_0000002553201879__commitconfig11-1)之后调用该接口，会导致相机会话配置耗时增加。

**P3广色域与HDR高动态范围成像**

应用可以下发不同的色彩空间(ColorSpace)参数来支持P3广色域以及HDR的功能。若应用不主动设置色彩空间，拍照、录像模式均默认为SDR拍摄。

应用针对不同模式使能HDR效果、设置的色彩空间以及设置相机输出流[Profile](Interfaces (其他).md#ZH-CN_TOPIC_0000002522081922__profile)中的[CameraFormat](Enums.md#ZH-CN_TOPIC_0000002553361841__cameraformat)一一对应关系可参考下表。例如，在录像模式下若需要选择HDR拍摄，相机预览输出流和录像输出流[Profile](Interfaces (其他).md#ZH-CN_TOPIC_0000002522081922__profile)中的[CameraFormat](Enums.md#ZH-CN_TOPIC_0000002553361841__cameraformat)可选择CAMERA_FORMAT_YCRCB_P010，色彩空间ColorSpace可选择设置BT2020_HLG_LIMIT。

在拍照模式下，若需要获取HDR高显效果的图片，可通过设置色彩空间（ColorSpace）为DISPLAY_P3或BT2020_HLG实现。其中BT2020_HLG能够表示更广的色域，需要搭配使用预览输出格式（Profile.format）P010（CAMERA_FORMAT_YCRCB_P010/CAMERA_FORMAT_YCBCR_P010）来提升图像质感。

从API version 23开始，可以通过接口[getSupportedFullOutputCapability](Interface (CameraManager).md#ZH-CN_TOPIC_0000002522081908__getsupportedfulloutputcapability23)查询是否支持拍照模式下的预览P010格式。

- 若应用不主动设置色彩空间，在拍照模式下，当预览输出格式为CAMERA_FORMAT_YUV_420_SP时，色彩空间默认为SRGB；当预览输出格式为CAMERA_FORMAT_YCRCB_P010/CAMERA_FORMAT_YCBCR_P010时，色彩空间默认为BT2020_HLG。

- 若应用主动设置色彩空间，在拍照模式下，预览输出格式与色彩空间必须按照下列表格中的对应关系配置，若不满足则会在[setColorSpace](Interface (ColorManagement).md#ZH-CN_TOPIC_0000002553201871__setcolorspace12)或[commitConfig](Interface (Session).md#ZH-CN_TOPIC_0000002553201879__commitconfig11-1)时返回错误码。

 拍照模式：

| SDR/HDR拍摄 | 预览输出格式 | 色彩空间 |
| --- | --- | --- |
| SDR(Default) | CAMERA_FORMAT_YUV_420_SP | SRGB |
| HDR P3 | CAMERA_FORMAT_YUV_420_SP | DISPLAY_P3 |
| HDR BT.2020 | CAMERA_FORMAT_YCRCB_P010、 CAMERA_FORMAT_YCBCR_P010 | BT2020_HLG |

在录像模式下，使能SDR或HDR_VIVID拍摄效果时，[CameraFormat](../enums/Enums.md#ZH-CN_TOPIC_0000002497445814__cameraformat)与ColorSpace必须按照下列表格中的对应关系配置，若不满足表格中CameraFormat与ColorSpace配置，会导致预览异常等问题。

**录像模式：**

| SDR/HDR拍摄 | [CameraFormat](../enums/Enums.md#ZH-CN_TOPIC_0000002497445814__cameraformat) | ColorSpace |
| --- | --- | --- |
| SDR(Default) | CAMERA_FORMAT_YUV_420_SP | BT709_LIMIT |
| HDR_VIVID | CAMERA_FORMAT_YCRCB_P010 | BT2020_HLG_LIMIT、 BT2020_HLG |
| HDR_VIVID | CAMERA_FORMAT_YCBCR_P010 | BT2020_HLG_LIMIT、 BT2020_HLG |

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| colorSpace | colorSpaceManager.ColorSpace | 是 | 色彩空间，通过getSupportedColorSpaces接口获取。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码]([Camera错误码](../../errors/Camera错误码.md).md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400101 | Parameter missing or parameter type incorrect. |
| 7400102 | The colorSpace does not match the format. |
| 7400103 | Session not config. |
| 7400201 | Camera service fatal error. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { colorSpaceManager } from '@kit.ArkGraphics2D';

function setColorSpace(session: camera.PhotoSession, colorSpaces: Array<colorSpaceManager.ColorSpace>): void {
  if (colorSpaces === undefined || colorSpaces.length <= 0) {
    return;
  }
  try {
    session.setColorSpace(colorSpaces[0]);
  } catch (error) {
    let err = error as BusinessError;
    console.error(`The setColorSpace call failed, error code: ${err.code}`);
  }
```

#### getActiveColorSpace12+

getActiveColorSpace(): colorSpaceManager.ColorSpace

获取当前设置的色彩空间。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| colorSpaceManager.ColorSpace | 当前设置的色彩空间。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](Camera错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400103 | Session not config. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { colorSpaceManager } from '@kit.ArkGraphics2D';

function getActiveColorSpace(session: camera.PhotoSession): colorSpaceManager.ColorSpace | undefined {
  let colorSpace: colorSpaceManager.ColorSpace | undefined = undefined;
  try {
    colorSpace = session.getActiveColorSpace();
  } catch (error) {
    let err = error as BusinessError;
    console.error(`The getActiveColorSpace call failed. error code: ${err.code}`);
  }
  return colorSpace;
}
```