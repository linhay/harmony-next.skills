# convertCoordinateSync

#### 导入模块

```ets
import { map, mapCommon } from '@kit.MapKit';
```

#### convertCoordinateSync

convertCoordinateSync(fromType: mapCommon.CoordinateType, toType: mapCommon.CoordinateType, location: mapCommon.LatLng): mapCommon.LatLng

坐标系转换。当前仅支持WGS84坐标系转GCJ02坐标系。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**5.0.0(12)

**参数：**

**参数名**

**类型**

必填

**说明**

fromType

[mapCommon.CoordinateType](mapCommon（地图属性模型）.md#section78948324526)

是

转换前坐标类型，当前仅支持WGS84。

toType

[mapCommon.CoordinateType](mapCommon（地图属性模型）.md#section78948324526)

是

转换后坐标类型，当前仅支持GCJ02。

location

[mapCommon.LatLng](mapCommon（地图属性模型）.md#section20691173773810)

是

待转换坐标。

**返回值：**

类型

说明

[mapCommon.LatLng](mapCommon（地图属性模型）.md#section20691173773810)

经纬度对象。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

错误码ID

错误信息

401

Invalid input parameter.

**示例：**

```ets
let wgs84Position: mapCommon.LatLng = {
  latitude: 30,
  longitude: 118
};
// 转换经纬度坐标
let gcj02Position: mapCommon.LatLng =
  map.convertCoordinateSync(mapCommon.CoordinateType.WGS84, mapCommon.CoordinateType.GCJ02, wgs84Position);
```