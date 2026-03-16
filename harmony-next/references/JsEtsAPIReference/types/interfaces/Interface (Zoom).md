# Interface (Zoom)

Zoom 继承自 [ZoomQuery](Interface (ZoomQuery).md)。

变焦类，对设备变焦操作。

- 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
- 本Interface首批接口从API version 11开始支持。

#### 导入模块

```ets
import { camera } from '@kit.CameraKit';
```

#### setZoomRatio11+

setZoomRatio(zoomRatio: number): void

设置变焦比，变焦精度最高为小数点后两位，如果设置超过支持的精度范围，则只保留精度范围内数值。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

参数名类型必填说明zoomRationumber是

可变焦距比，通过[getZoomRatioRange](Interface (ZoomQuery).md#ZH-CN_TOPIC_0000002529445757__getzoomratiorange11)获取支持的变焦范围，如果设置超过支持范围的值，则只保留精度范围内数值。

设置可变焦距比到底层生效需要一定时间，获取正确设置的可变焦距比需要等待1~2帧的时间。

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](../../errors/Camera错误码.md)。

错误码ID错误信息7400103Session not config.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function setZoomRatio(photoSession: camera.PhotoSession, zoomRatioRange: Array<number>): void {
  if (zoomRatioRange === undefined || zoomRatioRange.length <= 0) {
    return;
  }
  let zoomRatio = zoomRatioRange[0];
  try {
    photoSession.setZoomRatio(zoomRatio);
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`The setZoomRatio call failed. error code: ${err.code}`);
  }
}
```

#### getZoomRatio11+

getZoomRatio(): number

获取当前的变焦比。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

类型说明number获取当前的变焦比结果。接口调用失败会返回相应错误码，错误码类型[CameraErrorCode](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002497445814__cameraerrorcode)。

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](../../errors/Camera错误码.md)。

错误码ID错误信息7400103Session not config.7400201Camera service fatal error.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function getZoomRatio(photoSession: camera.PhotoSession): number {
  const invalidValue: number = -1;
  let zoomRatio: number = invalidValue;
  try {
    zoomRatio = photoSession.getZoomRatio();
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`The getZoomRatio call failed. error code: ${err.code}`);
  }
  return zoomRatio;
}
```

#### setSmoothZoom11+

setSmoothZoom(targetRatio: number, mode?: SmoothZoomMode): void

触发平滑变焦。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

参数名类型必填说明targetRationumber是目标值。通过[getZoomRatioRange](Interface (ZoomQuery).md#ZH-CN_TOPIC_0000002529445757__getzoomratiorange11)获取支持的变焦范围，如果设置超过支持范围的值，则只保留精度范围内数值。mode[SmoothZoomMode](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002497445814__smoothzoommode11)否平滑变焦模式。默认为0。

**示例：**

```ets
function setSmoothZoom(sessionExtendsZoom: camera.Zoom, targetZoomRatio: number, mode: camera.SmoothZoomMode): void {
  sessionExtendsZoom.setSmoothZoom(targetZoomRatio, mode);
}
```