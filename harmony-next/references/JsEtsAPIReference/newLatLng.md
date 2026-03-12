# newLatLng

#### 导入模块

```ets
import { map, mapCommon } from '@kit.MapKit';
```

#### newLatLng

newLatLng(latLng: mapCommon.LatLng, zoom?: number): CameraUpdate

设置地图的中心点和缩放层级。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

**参数：**

**参数名**

**类型**

必填

**说明**

latLng

[mapCommon.LatLng](mapCommon（地图属性模型）.md#section20691173773810)

是

经纬度。

zoom

number

否

缩放层级，取值范围：[2, 20]，超出按边界值处理。

**返回值：**

类型

说明

[CameraUpdate](CameraUpdate.md)

描述地图状态将要发生的变化。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

错误码ID

错误信息

401

Invalid input parameter.

**示例：**

```ets
let latLng: mapCommon.LatLng = {
  latitude: 39.9,
  longitude: 116.4
};
let cameraUpdate: map.CameraUpdate = map.newLatLng(latLng);
```