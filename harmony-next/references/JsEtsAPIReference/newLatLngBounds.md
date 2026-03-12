# newLatLngBounds

#### 导入模块

```ets
import { map, mapCommon } from '@kit.MapKit';
```

#### newLatLngBounds

newLatLngBounds(bounds: mapCommon.LatLngBounds, padding: mapCommon.Padding): CameraUpdate

设置地图经纬度范围和4个方向与边界之间的距离。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.1(13)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**5.0.1(13)

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

[mapCommon.Padding](mapCommon（地图属性模型）.md#section144591344648)

是

地图区域和边界之间的距离，单位：px，默认值为0。

 说明：

- 地图组件高度减去padding的top值和bottom值，结果需要大于等于100px。
- 地图组件宽度减去padding的left值和right值，结果需要大于等于100px。

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
let bounds: mapCommon.LatLngBounds = {
  northeast: {
    latitude: 31,
    longitude: 118
  },
  southwest: {
    latitude: 30.5,
    longitude: 123
  }
};
// 初始化参数，左边距0，底边距50
let padding: mapCommon.Padding = {
  left: 0,
  bottom: 50
};
let cameraUpdate: map.CameraUpdate = map.newLatLngBounds(bounds, padding);
```