[]()[]()

# Functions

本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

[]()[]()

#### 导入模块

```ets
import { camera } from '@kit.CameraKit';
```

[]()[]()

#### camera.getCameraManager

getCameraManager(context: Context): CameraManager

获取相机管理器实例，同步返回结果。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

参数名类型必填说明context[Context](../graphics/Context (Stage模型的上下文基类).md)是应用上下文。

**返回值：**

类型说明[CameraManager](../../types/interfaces/Interface (CameraManager).md)相机管理器。

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](../../errors/Camera错误码.md)。

错误码ID错误信息7400101Parameter missing or parameter type incorrect.7400201Camera service fatal error.

**示例：**

```ets
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

function getCameraManager(context: common.BaseContext): camera.CameraManager | undefined {
  let cameraManager: camera.CameraManager | undefined = undefined;
  try {
    cameraManager = camera.getCameraManager(context);
  } catch (error) {
    let err = error as BusinessError;
    console.error(`The getCameraManager call failed. error code: ${err.code}`);
  }
  return cameraManager;
}
```