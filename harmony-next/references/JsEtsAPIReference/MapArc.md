# MapArc

#### 导入模块

```ets
import { map, mapCommon } from '@kit.MapKit';
```

#### MapArc

弧线。继承[BaseOverlay](BaseOverlay.md)。在调用map.[MapComponentController](MapComponentController.md)类的[addArc](MapComponentController.md#section123390488448)方法时会返回该类型的实例。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**5.0.0(12)

**示例：**

```ets
// 设置弧线参数
let mapArcParams: mapCommon.MapArcParams = {
  // 弧线起点坐标
  startPoint: {
    latitude: 39.913138,
    longitude: 116.415112
  },
  // 弧线终点坐标
  endPoint: {
    latitude: 28.239473,
    longitude: 112.954094
  },
  // 弧线中心点坐标
  centerPoint: {
    latitude: 33.86970399048567,
    longitude: 112.08633528544145
  },
  width: 10,
  color: 0xffff0000,
  visible: true,
  zIndex: 100
};
// 添加弧线
let mapArc: map.MapArc = this.mapController.addArc(mapArcParams);
```

#### getColor

getColor(): number

获取弧线的颜色。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**5.0.0(12)

**返回值：**

类型

说明

number

ARGB格式颜色值。

**示例：**

```ets
let color: number = mapArc.getColor();
```

#### getWidth

getWidth(): number

获取弧线的宽度。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**5.0.0(12)

**返回值：**

类型

说明

number

弧线的宽度。单位：px。

**示例：**

```ets
let width: number = mapArc.getWidth();
```

#### setColor

setColor(color: number): void

设置弧线的颜色。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**5.0.0(12)

**参数：**

**参数名**

**类型**

必填

**说明**

color

number

是

ARGB格式颜色值。默认值为黑色（0xff000000）

**示例：**

```ets
mapArc.setColor(0xffff00ff);
```

#### setWidth

setWidth(width: number): void

设置弧线的宽度。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**5.0.0(12)

**参数：**

**参数名**

**类型**

必填

**说明**

width

number

是

弧线的宽度，单位：px，取值范围：大于等于0。

**示例：**

```ets
mapArc.setWidth(20);
```