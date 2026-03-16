# Interface (ControlCenter)

ControlCenter 继承自 [ControlCenterQuery](Interface (ControlCenterQuery).md)。

控制中心类，用于使能相机控制器。

- 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
- 本Interface首批接口从API version 20开始支持。

#### 导入模块

```ets
import { camera } from '@kit.CameraKit';
```

#### enableControlCenter20+

enableControlCenter(enabled: boolean): void

使能相机控制器。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

参数名类型必填说明enabledboolean是开启或关闭相机控制器。true表示开启，false表示关闭。

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](../../errors/Camera错误码.md)。

错误码ID错误信息7400103Session not config.

**示例：**

```ets
function enableControlCenter(videoSession: camera.VideoSession, enable: boolean): void {
    let isSupported: boolean = videoSession.isControlCenterSupported();
    if (isSupported) {
        videoSession.enableControlCenter(enable);
    }
}
```