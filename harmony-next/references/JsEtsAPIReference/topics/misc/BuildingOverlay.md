# BuildingOverlay

#### 导入模块

```ets
import { map, mapCommon } from '@kit.MapKit';
```

#### BuildingOverlay

3D建筑。缩放地图到能看到建筑物时，才显示3D建筑效果。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**5.0.0(12)

**示例：**

```ets
let points: Array<mapCommon.LatLng> = [
  {
    latitude: 31.984794,
    longitude: 118.765865
  },
  {
    latitude: 31.98468,
    longitude: 118.766076
  },
  {
    latitude: 31.98472,
    longitude: 118.766116
  },
  {
    latitude: 31.98463,
    longitude: 118.766292
  },
  {
    latitude: 31.984586,
    longitude: 118.766251
  },
  {
    latitude: 31.984536,
    longitude: 118.766344
  },
  {
    latitude: 31.984633,
    longitude: 118.766446
  },
  {
    latitude: 31.9848,
    longitude: 118.766285
  },
  {
    latitude: 31.984925,
    longitude: 118.766312
  },
  {
    latitude: 31.985282,
    longitude: 118.766661
  },
  {
    latitude: 31.985438,
    longitude: 118.766419
  },
  {
    latitude: 31.985801,
    longitude: 118.766755
  },
  {
    latitude: 31.985856,
    longitude: 118.766504
  },
  {
    latitude: 31.985785,
    longitude: 118.766434
  },
  {
    latitude: 31.985821,
    longitude: 118.766278
  },
  {
    latitude: 31.985897,
    longitude: 118.766311
  },
  {
    latitude: 31.985944,
    longitude: 118.766095
  },
  {
    latitude: 31.985909,
    longitude: 118.766069
  },
  {
    latitude: 31.985794,
    longitude: 118.765989
  },
  {
    latitude: 31.9857,
    longitude: 118.766029
  },
  {
    latitude: 31.985658,
    longitude: 118.766164
  },
  {
    latitude: 31.985647,
    longitude: 118.766271
  },
  {
    latitude: 31.985574,
    longitude: 118.766297
  },
  {
    latitude: 31.985458,
    longitude: 118.766285
  },
  {
    latitude: 31.985271,
    longitude: 118.766002
  },
  {
    latitude: 31.985219,
    longitude: 118.766002
  },
  {
    latitude: 31.985135,
    longitude: 118.766029
  },
  {
    latitude: 31.985093,
    longitude: 118.766083
  },
  {
    latitude: 31.985019,
    longitude: 118.766109
  },
  {
    latitude: 31.984978,
    longitude: 118.766083
  },
  {
    latitude: 31.984794,
    longitude: 118.765865
  }
];
points.reverse();
// 3D建筑参数
let buildingOverlayOptions: mapCommon.BuildingOverlayParams =
  {
    // 3D建筑的范围参数（点为顺时针绘制）
    points: points,
    // 3D建筑的高度
    totalHeight: 51,
    // 3D建筑的选中楼层高度
    floorBottomHeight: 33,
    // 3D建筑的顶部颜色
    topFaceColor: 0xffa4b8f7,
    // 3D建筑的侧面颜色
    sideFaceColor: 0x44a4b8f7,
    // 3D建筑的选中楼层颜色
    floorColor: 0xff000000,
    // 3D建筑的展示层级
    showLevel: 14,
    // 3D建筑选中楼层从底部升起的动画时长
    animationDuration: 5000,
    // 3D建筑侧面的纹理
    sideTexture: { image: $r("app.media.side_tex"), height: 3, width: 3 },
    // 3D建筑选中楼层的纹理
    floorTexture: { image: $r("app.media.floor_tex"), height: 3, width: 3 }
  }
let buildingOverlay: map.BuildingOverlay= await this.mapController?.addBuildingOverlay(buildingOverlayOptions);
```

#### getId

getId(): string

返回3D建筑的ID。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**5.0.0(12)

**返回值：**

类型

说明

string

返回3D建筑的ID。

**示例：**

```ets
let id: String = buildingOverlay.getId();
```

#### remove

remove(): void

移除3D建筑。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**5.0.0(12)

**示例：**

```ets
buildingOverlay.remove();
```

#### setSideVisible

setSideVisible(visible: boolean): void

设置是否显示3D建筑的侧面和顶部。如果不需要显示3D建筑请同时将[setSideVisible](#section162717125719)和[setFloorVisible](#section164221712205712)设置为false。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**5.0.0(12)

**参数**：

**参数名**

**类型**

必填

**说明**

visible

boolean

是

是否显示3D建筑的侧面和顶部。

- true：显示
- false：不显示

**示例：**

```ets
buildingOverlay.setSideVisible(true);
```

#### setFloorVisible

setFloorVisible(visible: boolean): void

设置是否显示选中的楼层。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**5.0.0(12)

**参数**：

**参数名**

**类型**

必填

**说明**

visible

boolean

是

是否显示建筑的所选楼层。

- true：显示
- false：不显示

**示例：**

```ets
buildingOverlay.setFloorVisible(true);
```

#### setFloorBottomHeight

setFloorBottomHeight(height: number): void

设置所选楼层底部到地面的高度。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**5.0.0(12)

**参数**：

**参数名**

**类型**

必填

**说明**

height

number

是

所选楼层底部到地面的高度，单位：米，取值范围：大于等于0。

**示例：**

```ets
buildingOverlay.setFloorBottomHeight(80);
```