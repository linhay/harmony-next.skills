# Interface (ZoomQuery)

提供了与设备的缩放相关的查询功能，包括获取支持的缩放比例范围。

- 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
- 本Interface的起始版本为API version 12。接口在API version 12发生兼容变更，保留了内层元素的起始版本信息，会出现外层元素@since版本号大于内层元素的情况，不影响接口使用。

#### 导入模块

```ets
import { camera } from '@kit.CameraKit';
```

#### getZoomRatioRange11+

getZoomRatioRange(): Array<number>

获取支持的变焦范围。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

类型说明Array<number>用于获取可变焦距比范围，返回的数组包括其最小值和最大值。接口调用失败会抛出相应错误码并返回undefined，错误码类型[CameraErrorCode](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002497445814__cameraerrorcode)。

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](../../errors/Camera错误码.md)。

错误码ID错误信息7400103Session not config, only throw in session usage.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function getZoomRatioRange(photoSession: camera.PhotoSession): Array<number> {
  let zoomRatioRange: Array<number> = [];
  try {
    zoomRatioRange = photoSession.getZoomRatioRange();
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`The getZoomRatioRange call failed. error code: ${err.code}`);
  }
  return zoomRatioRange;
}
```