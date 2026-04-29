# TraceOverlay

#### 导入模块

```ets
import { map, mapCommon } from '@kit.MapKit';
```

#### TraceOverlay

动态轨迹。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**5.0.0(12)

**示例：**

```ets
// marker1的参数
let markerOptions1: mapCommon.MarkerOptions = {
  position: {
    latitude: 31.99227173519985,
    longitude: 118.7622219990476
  },
  // 图标需存放在resources/base/media目录下
  icon: $r("app.media.track_setting_sport_map_marker_22"),
  anchorU: 0.5,
  anchorV: 1,
  visible: true
};
// 新增marker1
let markerBoy1 = await this.mapController.addMarker(markerOptions1);
let boyImages1: map.PlayImageAnimation = new map.PlayImageAnimation();
boyImages1.setDuration(1000);
let resourceArray: Array<Resource> = new Array();
resourceArray.push($r("app.media.side_0"));
resourceArray.push($r("app.media.side_1"));
resourceArray.push($r("app.media.side_2"));
resourceArray.push($r("app.media.side_3"));
resourceArray.push($r("app.media.side_4"));
resourceArray.push($r("app.media.side_5"));
resourceArray.push($r("app.media.side_6"));
resourceArray.push($r("app.media.side_7"));
resourceArray.push($r("app.media.side_8"));
resourceArray.push($r("app.media.side_9"));
resourceArray.push($r("app.media.side_10"));
resourceArray.push($r("app.media.side_11"));
resourceArray.push($r("app.media.side_12"));
resourceArray.push($r("app.media.side_13"));
resourceArray.push($r("app.media.side_14"));
resourceArray.push($r("app.media.side_15"));
resourceArray.push($r("app.media.side_16"));
resourceArray.push($r("app.media.side_17"));
resourceArray.push($r("app.media.side_18"));
resourceArray.push($r("app.media.side_19"));
resourceArray.push($r("app.media.side_20"));
await boyImages1.addImages(resourceArray);
boyImages1.setRepeatCount(-1);

// marker1添加动画
markerBoy1.setAnimation(boyImages1);
markerBoy1.startAnimation();

// marker2的参数
let markerOptions2: mapCommon.MarkerOptions = {
  position: {
    latitude: 31.99227173519985,
    longitude: 118.7622219990476
  },
  // 图标需存放在resources/base/media目录下
  icon: $r("app.media.track_setting_sport_map_marker_22"),
  anchorU: 0.5,
  anchorV: 1,
  visible: false
};
// 新增marker2
let markerBoy2 = await this.mapController.addMarker(markerOptions2);
let boyImages2: map.PlayImageAnimation = new map.PlayImageAnimation();
boyImages2.setDuration(1000);
let resourceArray2: Array<Resource> = new Array();
resourceArray2.push($r("app.media.behavior_front_cycling_boy_000"));
resourceArray2.push($r("app.media.behavior_front_cycling_boy_001"));
resourceArray2.push($r("app.media.behavior_front_cycling_boy_002"));
resourceArray2.push($r("app.media.behavior_front_cycling_boy_003"));
resourceArray2.push($r("app.media.behavior_front_cycling_boy_004"));
resourceArray2.push($r("app.media.behavior_front_cycling_boy_005"));
resourceArray2.push($r("app.media.behavior_front_cycling_boy_006"));
resourceArray2.push($r("app.media.behavior_front_cycling_boy_007"));
resourceArray2.push($r("app.media.behavior_front_cycling_boy_008"));
resourceArray2.push($r("app.media.behavior_front_cycling_boy_009"));
resourceArray2.push($r("app.media.behavior_front_cycling_boy_010"));
resourceArray2.push($r("app.media.behavior_front_cycling_boy_011"));
resourceArray2.push($r("app.media.behavior_front_cycling_boy_012"));
resourceArray2.push($r("app.media.behavior_front_cycling_boy_013"));
resourceArray2.push($r("app.media.behavior_front_cycling_boy_014"));
resourceArray2.push($r("app.media.behavior_front_cycling_boy_015"));
resourceArray2.push($r("app.media.behavior_front_cycling_boy_016"));
resourceArray2.push($r("app.media.behavior_front_cycling_boy_017"));
resourceArray2.push($r("app.media.behavior_front_cycling_boy_018"));
await boyImages2.addImages(resourceArray2);
boyImages2.setRepeatCount(-1);
// marker2添加动画
markerBoy2.setAnimation(boyImages2);
markerBoy2.startAnimation();

let points: Array<mapCommon.LatLng> = new Array();
points.push({ latitude: 31.99685233070878, longitude: 118.75846023442728 });
points.push({ latitude: 31.99671325810786, longitude: 118.75846738985165 });
points.push({ latitude: 31.99659191076709, longitude: 118.7585347621686 });
points.push({ latitude: 31.99648202537233, longitude: 118.7586266510386 });
points.push({ latitude: 31.99637707201552, longitude: 118.75872004590596 });
points.push({ latitude: 31.996278207010903, longitude: 118.75880449946251 });
points.push({ latitude: 31.996187481969695, longitude: 118.7588781960278 });
points.push({ latitude: 31.996092248919354, longitude: 118.75895330554488 });
points.push({ latitude: 31.995962740450565, longitude: 118.75904721407304 });
points.push({ latitude: 31.995792921394, longitude: 118.75916904998051 });
points.push({ latitude: 31.995601885713416, longitude: 118.7593235241019 });
points.push({ latitude: 31.995398221178277, longitude: 118.75949998588176 });
points.push({ latitude: 31.995185902197715, longitude: 118.7596871082939 });
points.push({ latitude: 31.994983473052656, longitude: 118.75987334062296 });
points.push({ latitude: 31.99482433699269, longitude: 118.76002095184032 });
points.push({ latitude: 31.994709073721708, longitude: 118.76012902920532 });
points.push({ latitude: 31.99460732100702, longitude: 118.76023892576234 });
points.push({ latitude: 31.99449284962087, longitude: 118.7603694232856 });
points.push({ latitude: 31.99435358179254, longitude: 118.76053622438056 });
points.push({ latitude: 31.99420771148339, longitude: 118.76072790126692 });
points.push({ latitude: 31.994075194901523, longitude: 118.7609100960977 });
points.push({ latitude: 31.993952686158877, longitude: 118.7610741329013 });
points.push({ latitude: 31.993840180644217, longitude: 118.7612193418965 });
points.push({ latitude: 31.993733787150244, longitude: 118.76135383115654 });
points.push({ latitude: 31.993617206525155, longitude: 118.76150529647698 });

// 动态轨迹的入参
let tranceOptions: mapCommon.TraceOverlayParams = {
  // 轨迹点
  points: points,
  // 轨迹的动画时长
  animationDuration: 5000,
  // 相机是否跟随动画移动
  isMapMoving: true,
  // 轨迹的颜色
  color: 0xAAFFAA00,
  // 轨迹的宽度
  width: 20,
  // 轨迹的动画回调（回调轨迹点的index）
  animationCallback: (pointIndex) => {
    // 换成骑行
    if (pointIndex === 10) {
      markerBoy1.setVisible(false);
      markerBoy2.setVisible(true);
    }
};
let markers: Array<map.Marker> = new Array();
markers.push(markerBoy1, markerBoy2);
// 新增轨迹点动画
let traceOverlay: map.TraceOverlay = await this.mapController.addTraceOverlay(tranceOptions, markers);
```

#### getId

getId(): string

返回动态轨迹的ID。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回动态轨迹的ID。 |

**示例：**

```ets
let id: string = traceOverlay.getId();
```

#### remove

remove(): void

删除动态轨迹。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**5.0.0(12)

**示例：**

```ets
traceOverlay.remove();
```

#### pause

pause(): void

暂停动态轨迹回放。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**5.0.0(12)

**示例：**

```ets
traceOverlay.pause();
```

#### resume

resume(): void

恢复动态轨迹回放。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**5.0.0(12)

**示例：**

```ets
traceOverlay.resume();
```