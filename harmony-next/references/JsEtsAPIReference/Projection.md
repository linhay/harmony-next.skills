# Projection

#### 导入模块

```ets
import { map, mapCommon } from '@kit.MapKit';
```

#### Projection

用于在屏幕坐标和经纬度之间进行转换，在调用map.[MapComponentController](MapComponentController.md)类的[getProjection](MapComponentController.md#section8132133414720)方法时会返回该类型的实例。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

**示例：**

```ets
let projection: map.Projection = this.mapController?.getProjection();
```

#### fromScreenLocation

fromScreenLocation(point: mapCommon.MapPoint): mapCommon.LatLng

将屏幕像素点坐标转换成经纬度。屏幕位置是以相对于地图左上角（而不是整个屏幕的左上角）的屏幕像素（而非显示像素）指定的。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

**参数：**

**参数名**

**类型**

必填

**说明**

point

[mapCommon.MapPoint](mapCommon（地图属性模型）.md#section123881566186)

是

屏幕上的坐标点，单位：px。

**返回值：**

类型

说明

[mapCommon.LatLng](mapCommon（地图属性模型）.md#section20691173773810)

经纬度坐标。

**示例：**

```ets
let point: mapCommon.MapPoint = {
  positionX: 10,
  positionY: 10
};
let latLng: mapCommon.LatLng = projection.fromScreenLocation(point);
```

#### toScreenLocation

toScreenLocation(position: mapCommon.LatLng): mapCommon.MapPoint

将经纬度转换为对应的屏幕上的点的坐标。屏幕上的点的坐标是以相对于地图左上角（而不是整个屏幕的左上角）的屏幕像素（而非显示像素）指定的。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

**参数：**

**参数名**

**类型**

必填

**说明**

position

[mapCommon.LatLng](mapCommon（地图属性模型）.md#section20691173773810)

是

经纬度坐标。

**返回值：**

类型

说明

[mapCommon.MapPoint](mapCommon（地图属性模型）.md#section123881566186)

屏幕上的坐标点，单位：px。

**示例：**

```ets
let position: mapCommon.MapPoint = projection.toScreenLocation({ latitude: 31.984, longitude: 118.766 });
```

#### getVisibleRegion

getVisibleRegion(): mapCommon.VisibleRegion

获取可视区域的坐标信息。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

**返回值：**

类型

说明

[mapCommon.VisibleRegion](mapCommon（地图属性模型）.md#section88850322916)

可见区域。

**示例：**

```ets
let visibleRegion: mapCommon.VisibleRegion = projection.getVisibleRegion();
```

#### getMapBounds

getMapBounds(center: mapCommon.LatLng, zoom: number): mapCommon.LatLngBounds

根据中心点和缩放级别获取地图控件对应的目标区域。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**5.0.0(12)

**参数：**

**参数名**

**类型**

必填

**说明**

center

[mapCommon.LatLng](mapCommon（地图属性模型）.md#section20691173773810)

是

中心点经纬度坐标。

zoom

number

是

缩放级别，取值范围：[2, 20]。传入的值大于最大层级，会取最大层级，传入的值小于最小层级，会取最小层级。

**返回值：**

类型

说明

[mapCommon.LatLngBounds](mapCommon（地图属性模型）.md#section96341159111320)

目标区域。

**示例：**

```ets
let position: mapCommon.LatLng = {
  latitude: 31.98, longitude: 118.766
};
let result: mapCommon.LatLngBounds = projection.getMapBounds(position, 10);
```