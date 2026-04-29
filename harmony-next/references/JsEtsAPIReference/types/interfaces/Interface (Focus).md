# Interface (Focus)

Focus 继承自 [FocusQuery](Interface (FocusQuery).md)。

对焦类，对设备对焦操作。

- 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
- 本Interface首批接口从API version 11开始支持。

#### 导入模块

```ets
import { camera } from '@kit.CameraKit';
```

#### set[FocusMode](../enums/Enums.md#ZH-CN_TOPIC_0000002497445814__focusmode)11+

set[FocusMode](../enums/Enums.md#ZH-CN_TOPIC_0000002497445814__focusmode)(afMode: FocusMode): void

设置对焦模式。

进行设置之前，需要先检查设备是否支持指定的焦距模式，可使用方法[isFocusModeSupported](Interface (FocusQuery).md#ZH-CN_TOPIC_0000002522241908__isfocusmodesupported11)。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| afMode | [FocusMode](../enums/Enums.md#ZH-CN_TOPIC_0000002497445814__focusmode) | 是 | 指定的焦距模式。传参为null或者undefined，作为0处理，手动对焦模式。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码]([Camera错误码](../../errors/Camera错误码.md).md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400103 | Session not config. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function setFocusMode(photoSession: camera.PhotoSession): void {
  try {
    photoSession.setFocusMode(camera.FocusMode.FOCUS_MODE_AUTO);
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`The setFocusMode call failed. error code: ${err.code}`);
  }
```

#### get[FocusMode](../enums/Enums.md#ZH-CN_TOPIC_0000002497445814__focusmode)11+

get[FocusMode](../enums/Enums.md#ZH-CN_TOPIC_0000002497445814__focusmode)(): FocusMode

获取当前的对焦模式。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [FocusMode](../enums/Enums.md#ZH-CN_TOPIC_0000002497445814__focusmode) | 获取当前设备的焦距模式。接口调用失败会抛出相应错误码并返回undefined，错误码类型CameraErrorCode。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](Camera错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400103 | Session not config. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function getFocusMode(photoSession: camera.PhotoSession): camera.FocusMode | undefined {
  let afMode: camera.FocusMode | undefined = undefined;
  try {
    afMode = photoSession.getFocusMode();
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`The getFocusMode call failed. error code: ${err.code}`);
  }
  return afMode;
}
```

#### setFocusPoint11+

setFocusPoint(point: Point): void

设置焦点，焦点应在0-1坐标系内，该坐标系左上角为{0，0}，右下角为{1，1}。

此坐标系是以设备充电口在右侧时的横向设备方向为基准的，例如应用的预览界面布局以设备充电口在下侧时的竖向方向为基准，布局宽高为{w，h}，且触碰点为{x，y}，则转换后的坐标点为{y/h，1-x/w}。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| point | Point | 是 | 焦点。x、y设置范围应在[0，1]之内，超过范围，如果小于0设置0，大于1设置1。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](Camera错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400103 | Session not config. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function setFocusPoint(photoSession: camera.PhotoSession): void {
  const focusPoint: camera.Point = {x: 1, y: 1};
  try {
    photoSession.setFocusPoint(focusPoint);
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`The setFocusPoint call failed. error code: ${err.code}`);
  }
```

#### getFocusPoint11+

getFocusPoint(): Point

查询当前的焦点。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Point | 用于获取当前的焦点。接口调用失败会返回相应错误码，错误码类型为[CameraErrorCode](../enums/Enums.md#ZH-CN_TOPIC_0000002497445814__cameraerrorcode)。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](Camera错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400103 | Session not config. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function getFocusPoint(photoSession: camera.PhotoSession): camera.Point | undefined {
  let point: camera.Point | undefined = undefined;
  try {
    point = photoSession.getFocusPoint();
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`The getFocusPoint call failed. error code: ${err.code}`);
  }
  return point;
}
```

#### getFocalLength11+

getFocalLength(): number

查询当前的焦距值。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 用于获取当前焦距，单位mm。接口调用失败会返回相应错误码，错误码类型[CameraErrorCode](../enums/Enums.md#ZH-CN_TOPIC_0000002497445814__cameraerrorcode)。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](Camera错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400103 | Session not config. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function getFocalLength(photoSession: camera.PhotoSession): number {
  const invalidValue: number = -1;
  let focalLength: number = invalidValue;
  try {
    focalLength = photoSession.getFocalLength();
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`The getFocalLength call failed. error code: ${err.code}`);
  }
  return focalLength;
}
```