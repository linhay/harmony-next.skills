# newCameraPosition

#### 导入模块

```ets
import { map, mapCommon } from '@kit.MapKit';
```

#### newCameraPosition

newCameraPosition(cameraPosition: mapCommon.CameraPosition): CameraUpdate

创建CameraUpdate对象，更新地图状态。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

**参数：**

**参数名**

**类型**

必填

**说明**

cameraPosition

[mapCommon.CameraPosition](../misc/mapCommon（地图属性模型）.md#section105031244194712)

是

新的地图状态。

**返回值：**

类型

说明

[CameraUpdate](CameraUpdate.md)

描述地图状态将要发生的变化。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](../../errors/ArkTS API错误码.md)。

错误码ID

错误信息

401

Invalid input parameter.

**示例：**

```ets
let target: mapCommon.LatLng = {
  latitude: 39.9,
  longitude: 116.4
};
let cameraPosition: mapCommon.CameraPosition = {
  target: target,
  zoom: 10
};
let cameraUpdate: map.CameraUpdate = map.newCameraPosition(cameraPosition);
```