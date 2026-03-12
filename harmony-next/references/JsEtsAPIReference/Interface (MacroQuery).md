# Interface (MacroQuery)

提供查询设备是否支持相机微距拍摄的方法。

- 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
- 本Interface首批接口从API version 19开始支持。

#### 导入模块

```ets
import { camera } from '@kit.CameraKit';
```

#### isMacroSupported19+

isMacroSupported(): boolean

检测当前状态下是否支持微距能力，需要在CaptureSession调用[commitConfig](Interface (Session).md#ZH-CN_TOPIC_0000002529445753__commitconfig11)之后进行调用。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

类型说明boolean返回是否支持微距能力。true表示支持，false表示不支持。

**示例：**

```ets
function isMacroSupported(photoSession: camera.PhotoSession): boolean {
  let isSupported: boolean = photoSession.isMacroSupported();
  return isSupported;
}
```