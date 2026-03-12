# zoomIn

#### 导入模块

```ets
import { map } from '@kit.MapKit';
```

#### zoomIn

zoomIn(): CameraUpdate

放大地图缩放级别，在当前地图显示的级别基础上加1。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

**返回值：**

类型

说明

[CameraUpdate](CameraUpdate.md)

描述地图状态将要发生的变化。

**示例：**

```ets
let cameraUpdate: map.CameraUpdate = map.zoomIn();
```