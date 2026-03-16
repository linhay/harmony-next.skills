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

使用该接口前，必须先通过[getSupportedColorSpaces](Interface (ColorManagementQuery).md#ZH-CN_TOPIC_0000002497605780__getsupportedcolorspaces12)获取当前设备所支持的ColorSpaces。该接口建议在[addOutput](Interface (Session).md#ZH-CN_TOPIC_0000002529445753__addoutput11)之后、[commitConfig](Interface (Session).md#ZH-CN_TOPIC_0000002529445753__commitconfig11-1)之前调用，如果在[commitConfig](Interface (Session).md#ZH-CN_TOPIC_0000002529445753__commitconfig11-1)之后调用该接口，会导致相机会话配置耗时增加。

**P3广色域与HDR高动态范围成像**

应用可以下发不同的色彩空间(ColorSpace)参数来支持P3广色域以及HDR的功能。

当应用不主动设置色彩空间时，拍照模式默认为SDR拍摄效果。

在拍照模式下若需要获取HDR高显效果的图片可通过设置色彩空间P3色域实现。

应用针对不同模式使能HDR效果、设置的色彩空间以及设置相机输出流[Profile](Interfaces (其他).md#ZH-CN_TOPIC_0000002497605794__profile)中的[CameraFormat](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002497445814__cameraformat)一一对应关系可参考下表。例如，在录像模式下若需要选择HDR拍摄，相机预览输出流和录像输出流[Profile](Interfaces (其他).md#ZH-CN_TOPIC_0000002497605794__profile)中的[CameraFormat](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002497445814__cameraformat)可选择CAMERA_FORMAT_YCRCB_P010，色彩空间ColorSpace可选择设置2020_HLG_LIMIT。

在录像模式下，使能SDR或HDR_VIVID拍摄效果时，CameraFormat与ColorSpace必须按照下列表格中的对应关系配置，若不满足表格中CameraFormat与ColorSpace配置，会导致预览异常等问题。

**录像模式：**

SDR/HDR拍摄CameraFormatColorSpaceSDRCAMERA_FORMAT_YUV_420_SPBT709_LIMITHDR_VIVID

CAMERA_FORMAT_YCRCB_P010

CAMERA_FORMAT_YCBCR_P010

BT2020_HLG_LIMIT

BT2020_HLG_FULL

**拍照模式：**

SDR/HDR拍摄ColorSpaceSDR(Default)SRGBHDRDISPLAY_P3

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

参数名类型必填说明colorSpace[colorSpaceManager.ColorSpace](../../modules/ohos/@ohos.graphics.colorSpaceManager (色彩管理).md#ZH-CN_TOPIC_0000002497445992__colorspace)是色彩空间，通过[getSupportedColorSpaces](Interface (ColorManagementQuery).md#ZH-CN_TOPIC_0000002497605780__getsupportedcolorspaces12)接口获取。

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](../../errors/Camera错误码.md)。

错误码ID错误信息7400101Parameter missing or parameter type incorrect.7400102The colorSpace does not match the format.7400103Session not config.7400201Camera service fatal error.

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
}
```

#### getActiveColorSpace12+

getActiveColorSpace(): colorSpaceManager.ColorSpace

获取当前设置的色彩空间。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

类型说明[colorSpaceManager.ColorSpace](../../modules/ohos/@ohos.graphics.colorSpaceManager (色彩管理).md#ZH-CN_TOPIC_0000002497445992__colorspace)当前设置的色彩空间。

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](../../errors/Camera错误码.md)。

错误码ID错误信息7400103Session not config.

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