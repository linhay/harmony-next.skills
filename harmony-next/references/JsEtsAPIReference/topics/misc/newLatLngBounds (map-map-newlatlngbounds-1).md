[]()[]()

# newLatLngBounds

[]()[]()

#### 导入模块

```ets
import { map, mapCommon } from '@kit.MapKit';
```

[]()[]()

#### newLatLngBounds

newLatLngBounds(bounds: mapCommon.LatLngBounds, padding?: number): CameraUpdate

设置地图经纬度范围、地图区域和边界之间的距离。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

**参数：**

**参数名**

**类型**

必填

**说明**

bounds

[mapCommon.LatLngBounds](mapCommon（地图属性模型）.md#section96341159111320)

是

地图显示经纬度范围。

padding

number

否

地图区域和边界之间的距离，单位：px，默认值为0。

**返回值：**

类型

说明

[CameraUpdate](../media/CameraUpdate.md)

描述地图状态将要发生的变化。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](../../errors/ArkTS API错误码 (map-errorcode).md)。

错误码ID

错误信息

401

Invalid input parameter.

**示例：**

```ets
let bounds: mapCommon.LatLngBounds = {
  northeast: {
    latitude: 33,
    longitude: 118
  },
  southwest: {
    latitude: 32,
    longitude: 119
  }
};
let cameraUpdate: map.CameraUpdate = map.newLatLngBounds(bounds, 5);
```