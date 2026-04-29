# MapComponentController

**导入模块**

```ets
import { map, mapCommon } from '@kit.MapKit';
```

**MapComponentController**

地图的主要功能入口类，与地图有关的所有方法从此处接入。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 4.1.0(11)

示例：

```ets
import { MapComponent, mapCommon, map } from '@kit.MapKit';
import { AsyncCallback } from '@kit.BasicServicesKit';

@Entry
@Component
struct HuaweiMapDemo {
  private TAG = "HuaweiMapDemo";
  private mapOptions?: mapCommon.MapOptions;
  private callback?: AsyncCallback<map.MapComponentController>;
  private mapController?: map.MapComponentController;
  private mapEventManager?: map.MapEventManager;

  aboutToAppear(): void {
    // 地图初始化参数，设置地图中心点坐标及层级
    this.mapOptions = {
      position: {
        target: {
          latitude: 39.9,
          longitude: 116.4
        },
        zoom: 10
      }
    };

    // 地图初始化的回调
    this.callback = async (err, mapController) => {
      if (!err) {
        // 获取地图的控制器类，用来操作地图
        this.mapController = mapController;
        // 返回地图组件的监听事件管理接口
        this.mapEventManager = this.mapController.getEventManager();
        let callback = () => {
          console.info(this.TAG, `on-mapLoad`);
        }
        this.mapEventManager.on("mapLoad", callback);

        // 执行自定义的方法
        this.customizedMethod();
      }
    };
  }

  // 自定义的方法
  private customizedMethod() {
    // ...
  }

  build() {
    Stack() {
      // 调用MapComponent组件初始化地图
      MapComponent({ mapOptions: this.mapOptions, mapCallback: this.callback })
        .width('100%')
        .height('100%')
    }.height('100%')
  }
```

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

MapComponentController中的方法需要放在上述示例的地图初始化的回调中运行或自定义的方法中运行。

**animateCamera**

animateCamera(update: CameraUpdate, duration?: number): void

在指定的持续时间内以动画的形式更新相机状态。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 4.1.0(11)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| update | CameraUpdate | 是 | 相机状态将要发生的变化。 |
| duration | number | 否 | 动画的持续时间，单位：ms，默认值为250，取值范围：大于0，小于等于0按照默认值处理。 |

示例：

```ets
let target: mapCommon.LatLng = {
  latitude: 39.9,
  longitude: 116.4
};
let cameraPosition: mapCommon.CameraPosition = {
  target: target,
  zoom: 10
};
// 新建CameraUpdate对象
let cameraUpdate: map.CameraUpdate = map.newCameraPosition(cameraPosition);
// 在1000ms内以动画的形式移动相机
this.mapController.animateCamera(cameraUpdate, 1000);
```

**animateCameraStatus**

animateCameraStatus(update: CameraUpdate, duration?: number): Promise<AnimateResult>

在指定的持续时间内以动画的形式更新相机状态，并返回动画结果。使用Promise异步回调。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| update | CameraUpdate | 是 | 相机状态将要发生的变化。 |
| duration | number | 否 | 动画的持续时间，单位：ms，默认值为250，取值范围：大于0，小于等于0按照默认值处理。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<AnimateResult> | Promise对象，返回AnimateResult。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. |

示例：

```ets
let target: mapCommon.LatLng = {
  latitude: 39.9,
  longitude: 116.4
};
let cameraPosition: mapCommon.CameraPosition = {
  target: target,
  zoom: 10
};
// 新建CameraUpdate对象
let cameraUpdate: map.CameraUpdate = map.newCameraPosition(cameraPosition);
// 在1000ms内以动画的形式移动相机
let animateResult = await this.mapController.animateCameraStatus(cameraUpdate, 1000);
```

**animateCameraWithMarker**

animateCameraWithMarker(update: CameraUpdate, marker: Marker, duration: number): Promise<AnimateResult>

在指定的持续时间内以动画的形式更新相机状态，并更新指定的marker。使用Promise异步回调。相机移动过程中不能被打断，否则[AnimateResult](AnimateResult.md)的参数isCanceled返回值为true。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| update | CameraUpdate | 是 | 相机状态将要发生的变化。 |
| marker | Marker | 是 | 标记。 |
| duration | number | 是 | 动画的持续时间，单位：ms，默认值为250，取值范围：大于0，小于等于0按照默认值处理。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<AnimateResult> | Promise对象，返回AnimateResult。 |

示例：

```ets
let target: mapCommon.LatLng = {
  latitude: 39.9,
  longitude: 116.4
};
let cameraPosition: mapCommon.CameraPosition = {
  target: target,
  zoom: 10
};
// 新建CameraUpdate对象
let cameraUpdate: map.CameraUpdate = map.newCameraPosition(cameraPosition);
// marker初始化参数
let markerOptions: mapCommon.MarkerOptions = {
  position: {
    latitude: 39.9,
    longitude: 116.4
  },
  title: "XXX",
  // 图标需存放在resources/rawfile目录下
  icon: 'icon/icon.png',
  clickable: true
};
// 新建marker
let marker = await this.mapController?.addMarker(markerOptions);
// 在1000ms内以动画的形式移动相机, 并更新指定的marker
await this.mapController.animateCameraWithMarker(cameraUpdate, marker, 1000);
```

**animateCameraWithMarkers**

animateCameraWithMarkers(update: CameraUpdate, markers: Array<Marker>, duration: number): Promise<AnimateResult>

在指定的持续时间内以动画的形式更新相机状态，并更新传入的marker，支持传一组标记。使用Promise异步回调。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| update | CameraUpdate | 是 | 相机状态将要发生的变化。 |
| markers | Array<Marker> | 是 | 一组标记。 说明： 一组标记的位置必须相同，否则会返回401错误码。 |
| duration | number | 是 | 动画的持续时间，单位：ms，默认值为250，取值范围：大于0，小于等于0按照默认值处理。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<AnimateResult> | Promise对象，返回AnimateResult。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. |

示例：

```ets
let target: mapCommon.LatLng = {
  latitude: 39.9,
  longitude: 116.4
};
let cameraPosition: mapCommon.CameraPosition = {
  target: target,
  zoom: 10
};
// 新建CameraUpdate对象
let cameraUpdate: map.CameraUpdate = map.newCameraPosition(cameraPosition);
// marker1初始化参数
let markerOptions1: mapCommon.MarkerOptions = {
  position: {
    latitude: 31.984410259206815,
    longitude: 118.76625379397866
  },
  title: "icon",
  // 图标需存放在resources/rawfile目录下
  icon: 'icon/icon.png',
  clickable: true
};
let markerOptions2: mapCommon.MarkerOptions = {
  position: {
    latitude: 31.984410259206815,
    longitude: 118.76625379397866
  },
  title: "avocado",
  // 图标需存放在resources/rawfile目录下
  icon: 'icon/avocado.png',
  clickable: true,
  anchorU: 0.5,
  anchorV: 1
};
let marker1 = await this.mapController?.addMarker(markerOptions1);
// marker2初始化参数
let marker2 = await this.mapController?.addMarker(markerOptions2);
// 在1000ms内以动画的形式移动相机, 并更新指定的marker
await this.mapController.animateCameraWithMarkers(cameraUpdate, [marker1, marker2], 1000);
```

**stopAnimation**

stopAnimation(): void

停止当前执行的改变地图状态的动画。调用该方法时，相机立即停止移动并保持在该位置。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 4.1.0(11)

示例：

```ets
this.mapController.stopAnimation();
```

**clear**

clear(): void

移除地图上所有的圆、标记、折线等覆盖物。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 4.1.0(11)

示例：

```ets
this.mapController.clear();
```

**moveCamera**

moveCamera(update: CameraUpdate): void

更新相机状态。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 4.1.0(11)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| update | CameraUpdate | 是 | 相机状态将要发生的变化。 |

示例：

```ets
let target: mapCommon.LatLng = {
  latitude: 39.9,
  longitude: 116.4
};
let cameraPosition: mapCommon.CameraPosition = {
  target: target,
  zoom: 10
};
// 新建CameraUpdate对象
let cameraUpdate: map.CameraUpdate = map.newCameraPosition(cameraPosition);
// 移动相机
this.mapController.moveCamera(cameraUpdate);
```

**getCameraPosition**

getCameraPosition(): mapCommon.CameraPosition

获取相机的当前状态信息。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 4.1.0(11)

返回值：

| 类型 | 说明 |
| --- | --- |
| mapCommon.CameraPosition | 相机的当前状态信息。 |

示例：

```ets
let cameraPosition: mapCommon.CameraPosition = this.mapController.getCameraPosition();
```

**setLatLngBounds**

setLatLngBounds(bounds: mapCommon.LatLngBounds): void

指定一个[mapCommon.LatLngBounds](mapCommon（地图属性模型）.md#ZH-CN_TOPIC_0000002522082416__latlngbounds)来约束相机目标，使用户移动地图时，相机目标不会移出此边界。当设置新的边界时，新边界将覆盖之前设置的边界。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 4.1.0(11)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bounds | mapCommon.LatLngBounds | 是 | 约束相机目标的边界。 说明： 西南角纬度大于东北角纬度时不生效。 |

示例：

```ets
let bounds:mapCommon.LatLngBounds = {
  northeast: {
    latitude: 31,
    longitude: 118
  },
  southwest: {
    latitude: 30,
    longitude: 117
  }
};
this.mapController.setLatLngBounds(bounds);
```

**setPointToCenter**

setPointToCenter(point: mapCommon.MapPoint): void

将屏幕上的像素位置设置为地图的中心点。使用此方法后，地图将根据设置的屏幕坐标进行缩放和旋转。异常值不处理。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 4.1.0(11)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| point | mapCommon.MapPoint | 是 | 屏幕坐标点。 |

示例：

```ets
let point: mapCommon.MapPoint = {
  positionX: 1000,
  positionY: 1000
};
this.mapController.setPointToCenter(point);
```

**setMaxZoom**

setMaxZoom(maxZoom: number): void

设置相机最大缩放级别。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 4.1.0(11)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| maxZoom | number | 是 | 相机最大缩放级别，取值范围：[2, 20]。 传入的值大于20，最大缩放级别会取20。 传入的值小于2，最大缩放级别会取2。 在取值范围内，传入的值小于当前minZoom，最大缩放级别和最小缩放级别都会被设置为当前传入的值。 |

示例：

```ets
this.mapController.setMaxZoom(10);
```

**setMinZoom**

setMinZoom(minZoom: number): void

设置相机最小缩放级别。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 4.1.0(11)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| minZoom | number | 是 | 相机最小缩放级别，取值范围：[2, 20]。 传入的值大于20，最小缩放级别会取20。 传入的值小于2，最小缩放级别会取2。 在取值范围内，传入的值大于当前maxZoom，最大缩放级别和最小缩放级别都会被设置为当前传入的值。 |

示例：

```ets
this.mapController.setMinZoom(3);
```

**getMaxZoom**

getMaxZoom(): number

获取相机最大缩放级别。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 4.1.0(11)

返回值：

| 类型 | 说明 |
| --- | --- |
| number | 相机最大缩放级别。 |

示例：

```ets
let maxZoom: number = this.mapController.getMaxZoom();
```

**getMinZoom**

getMinZoom(): number

获取相机最小缩放级别。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 4.1.0(11)

返回值：

| 类型 | 说明 |
| --- | --- |
| number | 相机最小缩放级别。 |

示例：

```ets
let minZoom: number = this.mapController.getMinZoom();
```

**setTrafficEnabled**

setTrafficEnabled(enabled: boolean): void

打开或关闭路况图层。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 4.1.0(11)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean | 是 | - true：打开路况图层 - false：关闭路况图层 默认值为false。 |

示例：

```ets
this.mapController.setTrafficEnabled(true);
```

**isTrafficEnabled**

isTrafficEnabled(): boolean

获取路况图层开启状态。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 4.1.0(11)

返回值：

| 类型 | 说明 |
| --- | --- |
| boolean | - true：路况图层为开启状态 - false：路况图层为关闭状态 |

示例：

```ets
let isTrafficEnabled: boolean = this.mapController.isTrafficEnabled();
```

**setBuildingEnabled**

setBuildingEnabled(enabled: boolean): void

打开或者关闭3D建筑图层。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 4.1.0(11)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean | 是 | - true：打开3D建筑图层 - false：关闭3D建筑图层 默认值为false。 说明： 打开3D建筑图层后将地图层级缩放至建筑物可视层，即可展现3D图层效果。 |

示例：

```ets
this.mapController.setBuildingEnabled(true);
```

**isBuildingEnabled**

isBuildingEnabled(): boolean

获取3D建筑图层开启状态。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 4.1.0(11)

返回值：

| 类型 | 说明 |
| --- | --- |
| boolean | - true：3D建筑图层为开启状态 - false：3D建筑图层为关闭状态 |

示例：

```ets
let isBuildingEnabled: boolean = this.mapController.isBuildingEnabled();
```

**setMyLocationEnabled**

setMyLocationEnabled(myLocationEnabled: boolean): void

我的位置图层功能开关，默认使用系统的连续定位能力显示用户位置。开关打开后，“我的位置”按钮默认显示在地图的右下角。点击“我的位置”按钮，将会在屏幕中心显示当前定位，以蓝色圆点的形式呈现。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 4.1.0(11)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| myLocationEnabled | boolean | 是 | - true：启用我的位置图层 - false：禁用我的位置图层 默认值为false。 |

示例：

```ets
this.mapController.setMyLocationEnabled(true);
```

**setMyLocation**

setMyLocation(location: geoLocationManager.Location): void

Map Kit默认使用系统的连续定位能力显示用户位置，如果您希望定制显示频率或者精准度，可以调用此接口设置我的位置坐标。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 4.1.0(11)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| location | geoLocationManager.Location | 是 | 用户的位置。 说明： location参数需使用WGS84坐标系。 |

示例：

```ets
// 需要引入@kit.LocationKit模块
import { geoLocationManager } from '@kit.LocationKit';

let location = await geoLocationManager.getCurrentLocation();
this.mapController.setMyLocation(location);
```

**setMyLocationStyle**

setMyLocationStyle(style: mapCommon.MyLocationStyle): Promise<void>

设置用户的位置样式。使用Promise异步回调。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 4.1.0(11)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| style | mapCommon.MyLocationStyle | 是 | 用户的位置样式。 说明： 如果displayType使用FOLLOW_ROTATE需应用申请传感器权限：ohos.permission.ACCELEROMETER。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

示例：

```ets
let style: mapCommon.MyLocationStyle = {
  anchorU: 0.5,
  anchorV: 0.5,
  radiusFillColor: 0xffff0000,
  // icon为自定义图标资源，使用时需要替换，图标存放在resources/rawfile
  icon: 'icon/avocado.png'
};
await this.mapController.setMyLocationStyle(style);
```

**isMyLocationEnabled**

isMyLocationEnabled(): boolean

获取我的位置图层的开启状态。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 4.1.0(11)

返回值：

| 类型 | 说明 |
| --- | --- |
| boolean | 我的位置图层的开启状态。 - true：启用 - false：禁用 |

示例：

```ets
let isMyLocationEnabled: boolean = this.mapController.isMyLocationEnabled();
```

**setZoomGesturesEnabled**

setZoomGesturesEnabled(enabled: boolean): void

设置是否启用缩放手势。默认情况下，缩放手势处于启用状态。

-

启用状态，用户可以使用以下手势缩放相机：

  1. 单指双击可将缩放级别提高1（放大）层级，用双指单击可将缩放级别降低1（缩小）层级。

  1. 双指张合，实现放大缩小。

  1. 单指双击实现单指缩放，第二次点时按住，然后上划缩小，或下划放大。

-

禁用状态，缩放手势无效。此设置不影响缩放按钮，也不限制通过接口移动相机和相机动画。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 4.1.0(11)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean | 是 | - true：启用缩放手势 - false：禁用缩放手势 默认值为true。 |

示例：

```ets
this.mapController.setZoomGesturesEnabled(true);
```

**isZoomGesturesEnabled**

isZoomGesturesEnabled(): boolean

获取缩放手势功能的启用状态。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 4.1.0(11)

返回值：

| 类型 | 说明 |
| --- | --- |
| boolean | 缩放手势功能的启用状态。 - true：启用缩放手势 - false：禁用缩放手势 |

示例：

```ets
let isZoomGesturesEnabled: boolean = this.mapController.isZoomGesturesEnabled();
```

**setScrollGesturesEnabled**

setScrollGesturesEnabled(enabled: boolean): void

设置是否启用滚动手势。默认情况下，滚动手势处于启用状态。

-

启用状态，用户可以通过滑动来平移相机。

-

禁用状态，滑动无效。此设置不限制通过接口移动相机和相机动画。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 4.1.0(11)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean | 是 | - true：启用滚动手势 - false：禁用滚动手势 默认值为true。 |

示例：

```ets
this.mapController.setScrollGesturesEnabled(true);
```

**isScrollGesturesEnabled**

isScrollGesturesEnabled(): boolean

获取滚动手势的启用状态。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 4.1.0(11)

返回值：

| 类型 | 说明 |
| --- | --- |
| boolean | 滚动手势的启用状态。 - true：启用滚动手势 - false：禁用滚动手势 |

示例：

```ets
let isScrollGesturesEnabled: boolean = this.mapController.isScrollGesturesEnabled();
```

**setRotateGesturesEnabled**

setRotateGesturesEnabled(enabled: boolean): void

设置是否启用旋转手势，默认情况下，旋转手势处于启用状态。

-

启用状态，用户可以使用两指旋转手势旋转相机。

-

禁用状态，用户将无法通过手势旋转相机。此设置不限制用户点击指南针图标以重置相机方向，也不限制通过接口移动相机和相机动画。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 4.1.0(11)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean | 是 | - true：启用旋转手势 - false：禁用旋转手势 默认值为true。 |

示例：

```ets
this.mapController.setRotateGesturesEnabled(true);
```

**isRotateGesturesEnabled**

isRotateGesturesEnabled(): boolean

获取旋转手势的启用状态。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 4.1.0(11)

返回值：

| 类型 | 说明 |
| --- | --- |
| boolean | 旋转手势的启用状态。 - true：启用旋转手势 - false：禁用旋转手势 |

示例：

```ets
let isRotateGesturesEnabled: boolean = this.mapController.isRotateGesturesEnabled();
```

**setTiltGesturesEnabled**

setTiltGesturesEnabled(enabled: boolean): void

设置是否启用倾斜手势，默认情况下，倾斜手势处于启用状态。

-

启用状态，用户可以使用两指垂直向上或者向下滑动来倾斜相机。

-

禁用状态，用户无法通过手势来倾斜相机。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 4.1.0(11)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean | 是 | - true：启用倾斜手势 - false：禁用倾斜手势 默认值为true。 |

示例：

```ets
this.mapController.setTiltGesturesEnabled(true);
```

**isTiltGesturesEnabled**

isTiltGesturesEnabled(): boolean

获取倾斜手势的启用状态。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 4.1.0(11)

返回值：

| 类型 | 说明 |
| --- | --- |
| boolean | 倾斜手势的启用状态。 - true：启用倾斜手势 - false：禁用倾斜手势 |

示例：

```ets
let isTiltGesturesEnabled: boolean = this.mapController.isTiltGesturesEnabled();
```

**setZoomControlsEnabled**

setZoomControlsEnabled(enabled: boolean): void

设置是否启用缩放控制器，默认情况下，缩放控件处于启用状态。

-

启用状态，地图上会出现一对按钮的缩放控件（用于缩放地图）。点击按钮时，会使相机放大（或缩小）一个缩放级别。

-

禁用状态，不会显示缩放控件。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 4.1.0(11)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean | 是 | - true：启用缩放控制器 - false：禁用缩放控制器 默认值为true。 |

示例：

```ets
this.mapController.setZoomControlsEnabled(true);
```

**isZoomControlsEnabled**

isZoomControlsEnabled(): boolean

获取缩放控制器的启用状态。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 4.1.0(11)

返回值：

| 类型 | 说明 |
| --- | --- |
| boolean | 缩放控制器的启用状态。 - true：启用缩放控制器 - false：禁用缩放控制器 |

示例：

```ets
let isZoomControlsEnabled: boolean = this.mapController.isZoomControlsEnabled();
```

**setMyLocationControlsEnabled**

setMyLocationControlsEnabled(enabled: boolean): void

设置是否启用我的位置按钮。只显示按钮，在不开启我的位置图层功能的情况下，点击按钮没反应。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 4.1.0(11)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean | 是 | - true：启用我的位置按钮 - false：禁用我的位置按钮 默认值为false。 |

示例：

```ets
this.mapController.setMyLocationControlsEnabled(true);
```

**isMyLocationControlsEnabled**

isMyLocationControlsEnabled(): boolean

获取我的位置按钮的启用状态。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 4.1.0(11)

返回值：

| 类型 | 说明 |
| --- | --- |
| boolean | 我的位置按钮的启用状态。 - true：启用 - false：禁用 |

示例：

```ets
let isMyLocationControlsEnabled: boolean = this.mapController.isMyLocationControlsEnabled();
```

**setScaleControlsEnabled**

setScaleControlsEnabled(enabled: boolean): void

设置是否启用比例尺。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 4.1.0(11)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean | 是 | - true：启用比例尺 - false：禁用比例尺 默认值为false。 |

示例：

```ets
this.mapController.setScaleControlsEnabled(true);
```

**isScaleControlsEnabled**

isScaleControlsEnabled(): boolean

获取比例尺的启用状态。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 4.1.0(11)

返回值：

| 类型 | 说明 |
| --- | --- |
| boolean | 比例尺的启用状态。 - true：启用 - false：禁用 |

示例：

```ets
let isScaleControlsEnabled: boolean = this.mapController.isScaleControlsEnabled();
```

**setCompassControlsEnabled**

setCompassControlsEnabled(enabled: boolean): void

设置是否启用指南针。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 4.1.0(11)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean | 是 | - true：启用指南针 - false：禁用指南针 默认值为true。 |

示例：

```ets
this.mapController.setCompassControlsEnabled(true);
```

**isCompassControlsEnabled**

isCompassControlsEnabled(): boolean

获取指南针的启用状态。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 4.1.0(11)

返回值：

| 类型 | 说明 |
| --- | --- |
| boolean | 指南针的启用状态。 - true：启用 - false：禁用 |

示例：

```ets
let isCompassControlsEnabled: boolean = this.mapController.isCompassControlsEnabled();
```

**setGestureScaleByMapCenter**

setGestureScaleByMapCenter(enabled: boolean): void

设置以固定屏幕中心点进行缩放功能是否可用，默认是禁用状态。

-

启用状态，地图将以传入的固定屏幕点进行缩放。通过[setPointToCenter](#ZH-CN_TOPIC_0000002553362311__setpointtocenter)方法设置屏幕中心点坐标。

-

禁用状态，将以手指点击的位置为中心进行缩放。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 4.1.0(11)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean | 是 | - true：启用，地图将以传入的固定屏幕点进行缩放。 - false：禁用，地图将以手指点击的位置为中心进行缩放。 默认值为false。 |

示例：

```ets
this.mapController.setGestureScaleByMapCenter(true);
```

**isGestureScaleByMapCenter**

isGestureScaleByMapCenter(): boolean

获取以固定屏幕中心点进行缩放功能的开启状态。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 4.1.0(11)

返回值：

| 类型 | 说明 |
| --- | --- |
| boolean | 以固定屏幕中心点进行缩放功能的开启状态。 - true：启用 - false：禁用 |

示例：

```ets
let isGestureScaleByMapCenter: boolean = this.mapController.isGestureScaleByMapCenter();
```

**setLogoAlignment**

setLogoAlignment(alignment: mapCommon.LogoAlignment): void

设置地图Logo的对齐方式。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 4.1.0(11)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| alignment | mapCommon.LogoAlignment | 是 | 地图Logo的对齐方式，默认值为LogoAlignment.BOTTOM_START。 |

示例：

```ets
this.mapController.setLogoAlignment(mapCommon.LogoAlignment.BOTTOM_START);
```

**setLogoPadding**

setLogoPadding(padding: mapCommon.Padding): void

设置地图边界与Logo之间的间距。Logo不随横竖屏而改变，大小固定不随地图缩放变化。

-

当您设置的任意padding值超出范围（例如：负值，或超出边界）时被认为非法，Logo位置不变化。

-

当Logo位置在左下角时left、bottom生效。

-

当Logo位置在右上角时right、top生效，以此类推。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

在调整设置地图边界与Logo之间的间距时，请避免隐藏或遮盖Logo。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 4.1.0(11)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| padding | mapCommon.Padding | 是 | 地图边界与Logo之间的间距。 |

示例：

```ets
let padding: mapCommon.Padding = {
  left: 0,
  bottom: 50
};
this.mapController.setLogoPadding(padding);
```

**getScalePerPixel**

getScalePerPixel(): number

获取当前缩放级别下，地图上1像素点对应的长度，单位：米。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 4.1.0(11)

返回值：

| 类型 | 说明 |
| --- | --- |
| number | 地图上1像素点对应的长度，单位：米。 |

示例：

```ets
let scalePerPixel: number = this.mapController.getScalePerPixel();
```

**addMarker**

addMarker(options: mapCommon.MarkerOptions): Promise<Marker>

在地图上添加一个标记。使用Promise异步回调。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 4.1.0(11)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | mapCommon.MarkerOptions | 是 | 标记的属性设置。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<Marker> | Promise对象，返回Marker。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. |
| 1002601001 | The object to be operated does not exist. |
| 1002601005 | Failed to generate the icon of the customized component. 说明： 从6.0.0(20)版本开始。 |

示例：

```ets
// Marker初始化参数
let markerOptions: mapCommon.MarkerOptions = {
  position: {
    latitude: 39.9,
    longitude: 116.4
  },
  rotation: 0,
  visible: true,
  zIndex: 0,
  alpha: 1,
  anchorU: 0.5,
  anchorV: 1,
  clickable: true,
  draggable: true,
  flat: false,
  // 图标存放在resources/rawfile
  icon: 'test.png'
};
// 在地图上添加一个marker
let marker: map.Marker = await this.mapController.addMarker(markerOptions);
```

**addCircle**

addCircle(options: mapCommon.MapCircleOptions): Promise<MapCircle>

在地图上添加一个圆，指定圆心经纬度和圆的半径，用于表示某个位置的周边范围。使用Promise异步回调。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 4.1.0(11)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | mapCommon.MapCircleOptions | 是 | 圆的属性设置。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<MapCircle> | Promise对象，返回MapCircle。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. |
| 1002601001 | The object to be operated does not exist. |

示例：

```ets
// Circle初始化参数
let mapCircleOptions: mapCommon.MapCircleOptions = {
  center: {
    latitude: 39.9,
    longitude: 116.4
  },
  patterns: [{
    type: 0,
    length: 100
  }, {
    type: 1,
    length: 100
  }, {
    type: 2,
    length: 100
  }],
  radius: 700,
  fillColor: 0XFF00FFFF,
  strokeColor: 0xFFFF0000,
  strokeWidth: 10,
  zIndex: 15
};
// 在地图上添加一个Circle
let mapCircle: map.MapCircle = await this.mapController.addCircle(mapCircleOptions);
```

**addPolyline**

addPolyline(options: mapCommon.MapPolylineOptions): Promise<MapPolyline>

在地图上添加一条折线。使用Promise异步回调。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 4.1.0(11)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | mapCommon.MapPolylineOptions | 是 | 折线的属性设置。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<MapPolyline> | Promise对象，返回MapPolyline。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. |
| 1002601001 | The object to be operated does not exist. |

示例：

```ets
// 初始化参数
let polylineOption: mapCommon.MapPolylineOptions = {
  // 折线坐标点，必传
  points: [{
    latitude: 31.984410,
    longitude: 118.7662537
  }, {
    latitude: 31.084410,
    longitude: 118.0662537
  }],
  clickable: true,
  color: 0xff000000,
  startCap: mapCommon.CapStyle.BUTT,
  endCap: mapCommon.CapStyle.BUTT,
  geodesic: false,
  jointType: mapCommon.JointType.DEFAULT,
  visible: true,
  width: 10,
  zIndex: 0,
  gradient: false
};
// 在地图上添加一条折线
let mapPolyline: map.MapPolyline = await this.mapController.addPolyline(polylineOption);
```

**addPolygon**

addPolygon(options: mapCommon.MapPolygonOptions): Promise<MapPolygon>

在地图上添加一个多边形。使用Promise异步回调。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 4.1.0(11)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | mapCommon.MapPolygonOptions | 是 | 多边形的属性设置。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<MapPolygon> | Promise对象，返回MapPolygon。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. |
| 1002601001 | The object to be operated does not exist. |

示例：

```ets
// 初始化参数
let polygonOptions: mapCommon.MapPolygonOptions = {
  // 多边形坐标点，必传
  points: [{
    latitude: 31.98441,
    longitude: 118.066253
  }, {
    latitude: 31.98441,
    longitude: 118.766253
  }, {
    latitude: 32.98441,
    longitude: 118.766253
  }, {
    latitude: 32.98441,
    longitude: 118.066253
  }],
  clickable: true,
  fillColor: 0xff00DE00,
  geodesic: false,
  strokeColor: 0xff000000,
  jointType: mapCommon.JointType.DEFAULT,
  strokeWidth: 10,
  visible: true,
  zIndex: 10
};
// 在地图上添加一个多边形
let mapPolygon: map.MapPolygon = await this.mapController.addPolygon(polygonOptions);
```

**addPointAnnotation**

addPointAnnotation(params: mapCommon.PointAnnotationParams): Promise<PointAnnotation>

在地图上添加一个点注释。使用Promise异步回调。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 4.1.0(11)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| params | mapCommon.PointAnnotationParams | 是 | 点注释的属性设置。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<PointAnnotation> | Promise对象，返回PointAnnotation。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. |
| 1002601001 | The object to be operated does not exist. |

示例：

```ets
let pointAnnotationOptions: mapCommon.PointAnnotationParams = {
  // 定义点注释图标锚点
  position: {
    latitude: 39.918,
    longitude: 116.397
  },
  // 定义点注释名称与地图POI名称相同时，是否支持去重
  repeatable: true,
  // 定义点注释的碰撞规则
  collisionRule: mapCommon.CollisionRule.NAME,
  // 定义点注释的标题，数组长度最小为1，最大为3
  titles: [{
    // 定义标题内容
    content: "Title1",
    // 定义标题字体颜色
    color: 0xFF000000,
    // 定义标题字体大小
    fontSize: 15,
    // 定义标题描边颜色
    strokeColor: 0xFFFFFFFF,
    // 定义标题描边宽度
    strokeWidth: 2,
    // 定义标题字体样式
    fontStyle: mapCommon.FontStyle.ITALIC
  }],
  // 定义点注释的图标，图标存放在resources/rawfile
  icon: "icon/avocado.png",
  // 定义点注释是否展示图标
  showIcon: true,
  // 定义点注释的锚点在水平方向上的位置
  anchorU: 0.5,
  // 定义点注释的锚点在垂直方向上的位置
  anchorV: 1,
  // 定义点注释的显示属性，为true时，在被碰撞后仍能显示
  forceVisible: false,
  // 定义碰撞优先级，数值越大，优先级越低
  priority: 3,
  // 定义点注释展示的最小层级
  minZoom: 2,
  // 定义点注释展示的最大层级
  maxZoom: 20,
  // 定义点注释是否可见
  visible: true,
  // 定义点注释叠加层级属性
  zIndex: 10
};
let pointAnnotation: map.PointAnnotation = await this.mapController.addPointAnnotation(pointAnnotationOptions);
```

**addBubble**

addBubble(params: mapCommon.BubbleParams): Promise<Bubble>

在地图上添加气泡。使用Promise异步回调。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 4.1.0(11)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| params | mapCommon.BubbleParams | 是 | 气泡的属性设置。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<Bubble> | Promise对象，返回Bubble。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. |
| 1002601001 | The object to be operated does not exist. |

示例：

```ets
let bubbleOptions: mapCommon.BubbleParams = {
  // 气泡位置
  positions: [[{ latitude: 31, longitude: 118 }]],
  // 气泡图标，需要传4个方向的图标，图标存放在resources/rawfile
  icons: [
    'icon.png',
    'icon.png'
  ],
  // 定义气泡的显示属性，为true时，在被碰撞后仍能显示
  forceVisible: true,
  // 定义气泡碰撞优先级，数值越大，优先级越低
  priority: 3,
  // 定义气泡展示的最小层级
  minZoom: 2,
  // 定义气泡展示的最大层级
  maxZoom: 20,
  // 定义气泡是否可见
  visible: true,
  // 定义气泡叠加层级属性
  zIndex: 1
};
let bubble: map.Bubble = await this.mapController.addBubble(bubbleOptions);
```

**setPadding**

setPadding(padding?: mapCommon.Padding): void

设置地图和边界的距离来定义地图的可见区域。地图图层元素将适应填充，例如，缩放控件、指南针等将被移动到适应定义的区域，相机将相对于可见区域的中心移动。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 4.1.0(11)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| padding | mapCommon.Padding | 否 | 地图和边界的距离，默认值为{ left: 0, right: 0, top: 0, bottom: 0 }。 |

示例：

```ets
// 初始化参数，左边距0，底边距50
let padding: mapCommon.Padding = {
  left: 0,
  bottom: 50
};
this.mapController.setPadding(padding);
```

**getProjection**

getProjection(): Projection

获取Projection对象，用于实现屏幕坐标和经纬度坐标之间的相互转换。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 4.1.0(11)

返回值：

| 类型 | 说明 |
| --- | --- |
| Projection | Projection对象。 |

示例：

```ets
let projection: map.Projection = this.mapController.getProjection();
```

**setCustomMapStyle**

setCustomMapStyle(customMapStyleOptions: mapCommon.CustomMapStyleOptions): Promise<void>

将地图样式修改为自定义样式。使用Promise异步回调。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| customMapStyleOptions | mapCommon.CustomMapStyleOptions | 是 | 自定义样式参数。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果的Promise对象。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1002601002 | The custom map style file does not exist. |
| 1002601004 | The style content format is incorrect. |

示例：

```ets
// styleId需要替换为您自己的样式ID，样式ID可在Petal Maps Studio平台上创建
let param: mapCommon.CustomMapStyleOptions = {
  styleId: "xxxxxxx"
};
await this.mapController.setCustomMapStyle(param);
```

**getDayNightMode**

getDayNightMode(): mapCommon.DayNightMode

查询地图的日间夜间模式。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 5.0.0(12)

返回值：

| 类型 | 说明 |
| --- | --- |
| mapCommon.DayNightMode | 日间夜间模式。 |

示例：

```ets
let mode = this.mapController.getDayNightMode();
```

**setDayNightMode**

setDayNightMode(mode: mapCommon.DayNightMode): void

设置地图的日间夜间模式。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | mapCommon.DayNightMode | 是 | 日间夜间模式。 |

示例：

```ets
this.mapController.setDayNightMode(mapCommon.DayNightMode.AUTO);
```

**getMapType**

getMapType(): mapCommon.MapType

查询地图类型。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 5.0.0(12)

返回值：

| 类型 | 说明 |
| --- | --- |
| mapCommon.MapType | 查询地图的类型。 |

示例：

```ets
let mapType = this.mapController.getMapType();
```

**setMapType**

setMapType(mapType: mapCommon.MapType): void

设置地图类型。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mapType | mapCommon.MapType | 是 | 地图类型。 |

示例：

```ets
this.mapController.setMapType(mapCommon.MapType.TERRAIN);
```

**setScalePosition**

setScalePosition(point: mapCommon.MapPoint): void

设置比例尺控件的位置。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| point | mapCommon.MapPoint | 是 | 比例尺位置。 说明： 比例尺在穿戴设备上默认处于左右居中位置，接口传入的positionX值在穿戴设备上不显示效果。 |

示例：

```ets
let point: mapCommon.MapPoint = {
  // 以当前地图组件左上角为原点，向右移动1000
  positionX: 1000,
  // 以当前地图组件左上角为原点，向下移动1000
  positionY: 1000
};
this.mapController.setScalePosition(point);
```

**getScaleLevel**

getScaleLevel(): number

查询当前层级的比例尺大小。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 5.0.0(12)

返回值：

| 类型 | 说明 |
| --- | --- |
| number | 接口返回比例尺上的文本数字，单位：米。 |

示例：

```ets
let level = this.mapController.getScaleLevel();
```

**setCompassPosition**

setCompassPosition(point: mapCommon.MapPoint): void

设置指南针位置。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| point | mapCommon.MapPoint | 是 | 设置指南针位置，即指南针左上角相对地图组件左上角的偏移量，单位：px。 |

示例：

```ets
let point: mapCommon.MapPoint = {
  positionX: 10,
  positionY: 10
};
this.mapController.setCompassPosition(point);
```

**setAllGesturesEnabled**

setAllGesturesEnabled(enabled: boolean): void

提供禁用所有手势的接口。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean | 是 | - true：启用手势 - false：禁用手势 默认值为true。 |

示例：

```ets
this.mapController.setAllGesturesEnabled(true);
```

**getScaleControlsHeight**

getScaleControlsHeight(): number

获取比例尺控件的高度。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 5.0.0(12)

返回值：

| 类型 | 说明 |
| --- | --- |
| number | 比例尺控件的高度，单位：vp。 |

示例：

```ets
let height = this.mapController.getScaleControlsHeight();
```

**getScaleControlsWidth**

getScaleControlsWidth(): number

获取比例尺控件的宽度。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 5.0.0(12)

返回值：

| 类型 | 说明 |
| --- | --- |
| number | 比例尺控件的宽度，单位：vp。 |

示例：

```ets
let width = this.mapController.getScaleControlsWidth();
```

**setAlwaysShowScaleEnabled**

setAlwaysShowScaleEnabled(enabled: boolean): void

设置是否始终显示比例尺。该功能需优先使用[setScaleControlsEnabled](#ZH-CN_TOPIC_0000002553362311__setscalecontrolsenabled)方法开启比例尺控件方可使用。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean | 是 | - true：始终显示 - false：关闭始终显示，比例尺显示2秒后关闭 默认值为false。 |

示例：

```ets
this.mapController.setAlwaysShowScaleEnabled(true);
```

**isAlwaysShowScaleEnabled**

isAlwaysShowScaleEnabled(): boolean

返回是否始终显示比例尺。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 5.0.0(12)

返回值：

| 类型 | 说明 |
| --- | --- |
| boolean | - true: 始终显示 - false: 关闭始终显示 |

示例：

```ets
let scaleEnabled: boolean = this.mapController.isAlwaysShowScaleEnabled();
```

**addClusterOverlay**

addClusterOverlay(params: mapCommon.ClusterOverlayParams): Promise<ClusterOverlay>

新增聚合图层。使用Promise异步回调。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| params | mapCommon.ClusterOverlayParams | 是 | 聚合图层参数。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<ClusterOverlay> | Promise对象，返回ClusterOverlay。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. |
| 1002601001 | The object to be operated does not exist. |

示例：

```ets
let clusterItem1: mapCommon.ClusterItem = {
  position: {
    latitude: 31.98,
    longitude: 118.766
  }
};
let clusterItem2: mapCommon.ClusterItem = {
  position: {
    latitude: 31.68,
    longitude: 118.366
  }
};
let array: Array<mapCommon.ClusterItem> = [
  clusterItem1,
  clusterItem2
];
let clusterOverlayParams: mapCommon.ClusterOverlayParams = { distance: 40, clusterItems: array };
let clusterOverlay: map.ClusterOverlay = await this.mapController.addClusterOverlay(clusterOverlayParams);
```

**addImageOverlay**

addImageOverlay(params: mapCommon.ImageOverlayParams): Promise<ImageOverlay>

新增图片覆盖物。使用Promise异步回调。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| params | mapCommon.ImageOverlayParams | 是 | 覆盖物参数。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<ImageOverlay> | Promise对象，返回ImageOverlay。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. |
| 1002601001 | The object to be operated does not exist. |

示例：

```ets
let imageOverlayParams: mapCommon.ImageOverlayParams = {
  bounds: {
    southwest: { latitude: 32, longitude: 118 },
    northeast: { latitude: 32.4, longitude: 118.4 }
  },
  // 图标需存放在resources/rawfile目录下
  image: 'icon/icon.png',
  transparency: 0.3,
  zIndex: 101,
  anchorU: 0.5,
  anchorV: 0.5,
  clickable: true,
  visible: true,
  bearing: 0
};
let imageOverlay = await this.mapController?.addImageOverlay(imageOverlayParams);
```

**snapshot**

snapshot(): Promise<image.PixelMap>

生成地图快照。使用Promise异步回调。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 5.0.0(12)

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<image.PixelMap> | Promise对象，返回image.PixelMap。 |

示例：

```ets
import { image } from '@kit.ImageKit';

let image: image.PixelMap = await this.mapController.snapshot();
```

**addBuildingOverlay**

addBuildingOverlay(params: mapCommon.BuildingOverlayParams): Promise<BuildingOverlay>

添加3D建筑。使用Promise异步回调。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| params | mapCommon.BuildingOverlayParams | 是 | 3D建筑相关属性。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<BuildingOverlay> | Promise对象，返回BuildingOverlay。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. |
| 1002601001 | The object to be operated does not exist. |

示例：

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
  };
let cameraUpdate = map.newCameraPosition({
  target: {
    latitude: 31.984794,
    longitude: 118.765865
  },
  zoom: 18,
  tilt: 70
});
// 将地图镜头移动到3D建筑区域
this.mapController?.moveCamera(cameraUpdate);
// 新建3D建筑
let buildingOverlay: map.BuildingOverlay = await this.mapController?.addBuildingOverlay(buildingOverlayOptions);
```

**addTraceOverlay**

addTraceOverlay(params: mapCommon.TraceOverlayParams, markers?: Array<Marker>): Promise<TraceOverlay>

绘制动态轨迹，支持传一组标记，标记将和轨迹一起移动。使用Promise异步回调。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| params | mapCommon.TraceOverlayParams | 是 | 动态轨迹参数。 |
| markers | Array<Marker> | 否 | 动态轨迹的图片数组。 说明： 一组标记的位置必须相同。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<TraceOverlay> | Promise对象，返回TraceOverlay。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. |
| 1002601001 | The object to be operated does not exist. |

示例：

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

**addArc**

addArc(params: mapCommon.MapArcParams): MapArc

在地图上添加一条弧线。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| params | mapCommon.MapArcParams | 是 | 弧线的相关属性。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| MapArc | 返回MapArc。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. |
| 1002601001 | The object to be operated does not exist. |

示例：

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
this.mapController.addArc(mapArcParams);
```

**show**

show(): void

将地图切换到前台，开发者在绘制地图页面的生命周期onPageShow中调用。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 5.0.0(12)

示例：

```ets
// 页面每次显示时触发一次，包括路由过程、应用进入前台等场景，仅@Entry装饰的自定义组件生效
onPageShow(): void {
  // 绘制地图页面的生命周期onPageShow，将地图切换到前台
  if (this.mapController) {
    this.mapController.show();
  }
```

**hide**

hide(): void

将地图切换到后台，开发者在绘制地图页面的生命周期onPageHide中调用。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 5.0.0(12)

示例：

```ets
// 页面每次隐藏时触发一次，包括路由过程、应用进入后台等场景，仅@Entry装饰的自定义组件生效。
onPageHide(): void {
  // 绘制地图页面的生命周期onPageHide，将地图切换到后台
  if (this.mapController) {
    this.mapController.hide();
  }
```

**getEventManager**

getEventManager(): MapEventManager

返回地图监听事件管理器。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 5.0.0(12)

返回值：

| 类型 | 说明 |
| --- | --- |
| MapEventManager | 地图监听事件管理器。 |

示例：

```ets
let mapEventManager: map.MapEventManager = this.mapController.getEventManager();
```

**setDisplayOrder**

setDisplayOrder(types: Array<mapCommon.MapElementType>): void

设置地图元素的显示顺序，按照从低到高排列，即后面的覆盖物会压盖前面的覆盖物。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| types | Array<mapCommon.MapElementType> | 是 | 四类地图元素的显示顺序，默认顺序为[1, 2, 3, 4]。 入参的长度必须是4，且必须是mapCommon.MapElementType的4个取值，如果不满足，则返回错误码401。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. |

示例：

```ets
let mapElementTypeArr: Array<mapCommon.MapElementType> = [
  mapCommon.MapElementType.OVERLAY,
  mapCommon.MapElementType.POI,
  mapCommon.MapElementType.CUSTOM_POI,
  mapCommon.MapElementType.MARKER];
this.mapController.setDisplayOrder(mapElementTypeArr);
```

**setLogoScale**

setLogoScale(logoScale: number): void

修改Logo缩放比例。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本5.0.3(15)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 5.0.3(15)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| logoScale | number | 是 | Logo缩放比例，取值范围：[0.8, 1]。异常值返回错误码401。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. |

示例：

```ets
this.mapController.setLogoScale(0.9);
```

**getLogoScale**

getLogoScale(): number

查询Logo缩放比例。缩放比例取值范围是[0.8,1]，当缩放比例不在[0.8,1]时默认返回值为1。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本5.0.3(15)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 5.0.3(15)

返回值：

| 类型 | 说明 |
| --- | --- |
| number | Logo缩放比例。 |

示例：

```ets
let logoScale: number = this.mapController.getLogoScale();
```

**isSphereEnabled**

isSphereEnabled(): boolean

获取3D地球开启状态。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本5.0.3(15)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 5.0.3(15)

返回值：

| 类型 | 说明 |
| --- | --- |
| boolean | - true：3D地球为开启状态 - false：3D地球为关闭状态 |

示例：

```ets
let result: boolean = this.mapController.isSphereEnabled();
```

**setSphereEnabled**

setSphereEnabled(enabled: boolean): void

设置是否开启3D地球效果开关。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本5.0.3(15)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 5.0.3(15)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean | 是 | 是否开启3D地球效果开关。取值范围： - true：开启3D地球效果开关 - false：不开启3D地球效果开关 默认不开启3D地球效果。 |

示例：

```ets
this.mapController.setSphereEnabled(true);
```

**setSphereEnabled**

setSphereEnabled(enabled: boolean, animateDuration: number): void

以动画形式切换2D或3D地球。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本6.0.0(20)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 6.0.0(20)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean | 是 | 以动画形式切换2D或3D地球。取值范围： - true：开启3D地球 - false：开启2D地球 |
| animateDuration | number | 是 | 动画持续时间，单位：毫秒。 |

示例：

```ets
this.mapController.setSphereEnabled(true, 1000);
```

**setSphereEnabled**

setSphereEnabled(enabled: boolean, animateDuration: number, cityLight: boolean): void

以动画形式切换2D或3D地球。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本6.1.0(23)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 6.1.0(23)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean | 是 | 以动画形式切换2D或3D地球。取值范围： - true：开启3D地球 - false：开启2D地球 |
| animateDuration | number | 是 | 动画持续时间，单位：ms。 |
| cityLight | boolean | 是 | 是否启用城市灯光，需要开启3D地球，默认值：true。 - true：开启城市灯光 - false：关闭城市灯光 |

示例：

```ets
this.mapController.setSphereEnabled(true, 1000, true);
```

**addHeatmap**

addHeatmap(params: mapCommon.HeatmapParams): Promise<Heatmap>

添加热力图。使用Promise异步回调。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本6.0.0(20)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 6.0.0(20)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| params | mapCommon.HeatmapParams | 是 | 添加热力图的参数。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<Heatmap> | Promise对象，返回Heatmap，热力图覆盖物。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1002601001 | The object to be operated does not exist. |
| 1002600015 | The heatmap ID already exists. |

示例：

```ets
let data: mapCommon.WeightedLatLng[] = [];
for (let i = 0; i < 500; i++) {
  data.push({
    point: {
      longitude: 118.000000 + Math.random() * 1 - 0.25,
      latitude: 31.000000 + Math.random() * 1 - 0.25,
    },
    intensity: 1
  });
}
let heatMapOptions: mapCommon.HeatmapParams = {
  id: 'heatmap0001',
  data: data,
  radius: 20,
  intensity: {
    2: 1,
    5: 5,
    8: 10
  },
}
await this.mapController?.addHeatmap(heatMapOptions)
```

**addMvtOverlay**

addMvtOverlay(params: mapCommon.MvtOverlayParams): MvtOverlay

添加矢量图层。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本6.0.0(20)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core.EnhancedOverlay

起始版本： 6.0.0(20)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| params | mapCommon.MvtOverlayParams | 是 | 矢量图层的参数。 说明： 使用在线下载方式添加矢量图层时（即使用mapCommon.MvtOverlayParams中mapCommon.MvtSource参数的tileUrl方式），需要申请访问网络的权限：ohos.permission.INTERNET。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| MvtOverlay | 矢量图层管理对象。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1022100001 | The operation object does not exist. |

```ets
let params: mapCommon.MvtOverlayParams = {
  source: {
    // 设置矢量图层的地址,必须是以http或者https开头的URL且包含占位符{x}、{y}和{z}
    tileUrl: 'http://xxx/tiles/{z}/{x}/{y}.pbf',
    minZoom: 2,
    maxZoom: 15
  },
  layers: [{
    id: 'layer-map',
    type: mapCommon.MvtLayerType.FILL,
    // 对应矢量图层数据中图层的name字段
    sourceLayer: 'XX',
    paint: {
      fillColor: {
        operator: mapCommon.Operator.GET,
        args: 'fill'
      },
      fillOpacity: {
        operator: mapCommon.Operator.GET,
        args: 'fill-opacity'
      }
  }]
};
let mvtOverlay = this.mapController?.addMvtOverlay(params);
```

**setFramePerSecond**

setFramePerSecond(fps: number): void

设置每秒期望的帧数。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本6.0.0(20)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 6.0.0(20)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fps | number | 是 | 每秒期望的帧数，取值范围：[1, 60]。 |

示例：

```ets
this.mapController?.setFramePerSecond(60);
```

**addFlowFieldOverlay**

addFlowFieldOverlay(params: mapCommon.FlowFieldOverlayParams): Promise<FlowFieldOverlay>

添加流场图层，适用于风场和洋流场景。使用Promise异步回调。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本6.0.0(20)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core.EnhancedOverlay

起始版本： 6.0.0(20)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| params | mapCommon.FlowFieldOverlayParams | 是 | 流场图层的参数。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<FlowFieldOverlay> | Promise对象，返回流场图层的管理对象。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1022100001 | The operation object does not exist. |

示例：

```ets
let params: mapCommon.FlowFieldOverlayParams = {
  // data为GRIB2规范的json数据，需开发者自行传输，可参考流场数据格式参考
  data: 'xxx'
};
let fieldOverlay = await this.mapController.addFlowFieldOverlay(params);
```

**addMassPointOverlay**

addMassPointOverlay(params: mapCommon.MassPointOverlayParams): Promise<MassPointOverlay>

添加海量点图层。使用Promise异步回调。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本6.0.0(20)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 6.0.0(20)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| params | mapCommon.MassPointOverlayParams | 是 | 海量点图层的参数。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<MassPointOverlay> | Promise对象，返回海量点的管理对象。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1002601001 | The object to be operated does not exist. |

示例：

```ets
let items: mapCommon.MassPointItem[] = [];
for (let i = 0; i < 1000; i++) {
  // 将海量点存入items
  items.push({
    itemId: 'test' + i,
    position: {
      longitude: 118.11111 + Math.random() * 1 - 0.5,
      latitude: 32.11111 + Math.random() * 1 - 0.5,
    },
    snippet: 'test' + i,
    title: 'test' + i
  })
}
let params: mapCommon.MassPointOverlayParams = {
  id: 'test',
  items: items,
  // 图标存放在resources/rawfile，icon参数传入rawfile文件夹下的相对路径
  icon: 'icon/maps_blue_dot.png',
}
let massPointOverlay = await this.mapController?.addMassPointOverlay(params);
```

**setLanguage**

setLanguage(language: string): void

设置地图组件语言。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本6.0.0(20)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 6.0.0(20)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| language | string | 是 | 地图语言。语种取值请参见地图组件支持语言列表。 |

示例：

```ets
this.mapController?.setLanguage('ja');
```

**getLanguage**

getLanguage(): string

获取地图组件语言。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本6.0.0(20)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 6.0.0(20)

返回值：

| 类型 | 说明 |
| --- | --- |
| string | 地图语言。语种取值请参见地图组件支持语言列表。 |

示例：

```ets
let language = this.mapController?.getLanguage();
```

**changeMyLocationLayerOrder**

changeMyLocationLayerOrder(isBelow: boolean): void

更改我的位置图层相对于覆盖物的压盖顺序。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本6.0.1(21)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 6.0.1(21)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isBelow | boolean | 是 | 我的位置图层是否位于覆盖物之下。 - true：我的位置图层位于覆盖物之下 - false：我的位置图层位于覆盖物之上 说明： 该接口对Marker、MapPolyline、MapPolygon、MapCircle、PointAnnotation、Bubble、ImageOverlay、MapArc、TraceOverlay、底图Poi生效。 |

示例：

```ets
this.mapController?.changeMyLocationLayerOrder(true);
```

**addTileOverlay**

addTileOverlay(params: mapCommon.TileOverlayParams | mapCommon.TileOverlayOptions): TileOverlay

新增瓦片图层。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本5.0.3(15)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 5.0.3(15)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| params | mapCommon.TileOverlayParams | mapCommon.TileOverlayOptions | 是 | 瓦片图层参数。 说明： 从6.0.0(20)版本开始，params属性支持mapCommon.TileOverlayOptions类型。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| TileOverlay | 瓦片图层。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1002601001 | The object to be operated does not exist. |

示例：

```ets
let params: mapCommon.TileOverlayOptions = {
  // 设置地图瓦片图层的地址,必须是以http或者https开头的URL且包含占位符{x}、{y}和{z}
  // 需要替换为开发者自己的在线地址
  tileUrl: "https://xxx/xxx?x={x}&y={y}&z={z}",
  // 透明度
  transparency: 0.5,
  // 开启瓦片图层淡入
  fadeIn: true,
  // 开启磁盘缓存
  diskCacheEnabled: true,
  // 磁盘缓存大小 默认大小 20480KB, 单位KB
  diskCacheSize: 20480,
  // 存放磁盘缓存的沙箱路径
  diskCachePath: this.getUIContext().getHostContext()?.databaseDir
};
let tileOverlay: map.TileOverlay = this.mapController?.addTileOverlay(params);
```

**on('cameraChange')**

on(type: 'cameraChange', callback: Callback<mapCommon.LatLng>): void

监听地图相机状态变化事件。使用callback异步回调。此回调不会在动画过程中触发，而是在动画结束时触发。

建议使用[MapEventManager.on(type: 'cameraChange')](MapEventManager.md#ZH-CN_TOPIC_0000002553362325__oncamerachange)。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 4.1.0(11)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 'cameraChange'：监听地图相机状态变化事件。 |
| callback | Callback<mapCommon.LatLng> | 是 | 回调函数，返回mapCommon.LatLng，监听地图相机状态变化事件。该回调不会在动画过程中触发，而是在动画结束时触发。 |

示例：

```ets
this.mapController.on("cameraChange", (position) => {
  console.info("cameraChange", `on-cameraChange position = ${position.longitude}`);
});
```

**off('cameraChange')**

off(type: 'cameraChange', callback: Callback<void>): void

取消监听地图相机状态变化事件。使用callback异步回调。

建议使用[MapEventManager.off(type: 'cameraChange')](MapEventManager.md#ZH-CN_TOPIC_0000002553362325__offcamerachange)。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 4.1.0(11)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 'cameraChange'：监听地图相机状态变化事件。 |
| callback | Callback<void> | 是 | 回调函数，无返回结果的回调函数。 |

示例：

```ets
this.mapController.off("cameraChange", (position) => {
  console.info("cameraChange", `off-cameraChange`);
});
```

**on('cameraIdle')**

on(type: 'cameraIdle', callback: Callback<void>): void

监听相机移动结束事件。使用callback异步回调。

建议使用[MapEventManager.on(type: 'cameraIdle')](MapEventManager.md#ZH-CN_TOPIC_0000002553362325__oncameraidle)。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 4.1.0(11)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 'cameraIdle'：监听相机移动结束事件。 |
| callback | Callback<void> | 是 | 回调函数，无返回结果的回调函数。 |

示例：

```ets
this.mapController.on("cameraIdle", () => {
  console.info("cameraIdle", `on-cameraIdle`);
});
```

**off('cameraIdle')**

off(type: 'cameraIdle', callback: Callback<void>): void

取消监听相机移动结束事件。使用callback异步回调。

建议使用[MapEventManager.off(type: 'cameraIdle')](MapEventManager.md#ZH-CN_TOPIC_0000002553362325__offcameraidle)。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 4.1.0(11)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 'cameraIdle'：监听相机移动结束事件。 |
| callback | Callback<void> | 是 | 回调函数，无返回结果的回调函数。 |

示例：

```ets
this.mapController.off("cameraIdle", () => {
  console.info("cameraIdle", `off-cameraIdle`);
});
```

**on('cameraMoveCancel')**

on(type: 'cameraMoveCancel', callback: Callback<void>): void

监听相机移动取消事件。使用callback异步回调。

建议使用[MapEventManager.on(type: 'cameraMoveCancel')](MapEventManager.md#ZH-CN_TOPIC_0000002553362325__oncameramovecancel)。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 4.1.0(11)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 'cameraMoveCancel'：监听地图相机移动取消事件。 |
| callback | Callback<void> | 是 | 回调函数，无返回结果的回调函数。 |

示例：

```ets
this.mapController.on("cameraMoveCancel", () => {
  console.info("cameraMoveCancel", `on-cameraMoveCancel`);
});
```

**off('cameraMoveCancel')**

off(type: 'cameraMoveCancel', callback: Callback<void>): void

取消监听相机移动取消事件。使用callback异步回调。

建议使用[MapEventManager.off(type: 'cameraMoveCancel')](MapEventManager.md#ZH-CN_TOPIC_0000002553362325__offcameramovecancel)。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 4.1.0(11)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 'cameraMoveCancel'：监听地图相机移动取消事件。 |
| callback | Callback<void> | 是 | 回调函数，无返回结果的回调函数。 |

示例：

```ets
this.mapController.off("cameraMoveCancel", () => {
  console.info("cameraMoveCancel", `off-cameraMoveCancel`);
});
```

**on('cameraMove')**

on(type: 'cameraMove', callback: Callback<void>): void

监听相机移动事件。使用callback异步回调。

建议使用[MapEventManager.on(type: 'cameraMove')](MapEventManager.md#ZH-CN_TOPIC_0000002553362325__oncameramove)。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 4.1.0(11)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 'cameraMove'：监听相机移动事件。 |
| callback | Callback<void> | 是 | 回调函数，无返回结果的回调函数。 |

示例：

```ets
this.mapController.on("cameraMove", () => {
  console.info("cameraMove", `on-cameraMove`);
});
```

**off('cameraMove')**

off(type: 'cameraMove', callback: Callback<void>): void

取消监听相机移动事件。使用callback异步回调。

建议使用[MapEventManager.off(type: 'cameraMove')](MapEventManager.md#ZH-CN_TOPIC_0000002553362325__offcameramove)。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 4.1.0(11)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 'cameraMove'：监听相机移动事件。 |
| callback | Callback<void> | 是 | 回调函数，无返回结果的回调函数。 |

示例：

```ets
this.mapController.off("cameraMove", () => {
  console.info("cameraMove", `off-cameraMove`);
});
```

**on('cameraMoveStart')**

on(type: 'cameraMoveStart', callback: Callback<number>): void

监听相机移动开始事件。使用callback异步回调。

建议使用[MapEventManager.on(type: 'cameraMoveStart')](MapEventManager.md#ZH-CN_TOPIC_0000002553362325__oncameramovestart)。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 4.1.0(11)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 'cameraMoveStart'：监听相机移动开始事件。 |
| callback | Callback<number> | 是 | 回调函数，返回number。 number表示相机改变的原因： 1：地图上的用户手势 2：用户交互产生的默认动画 3：开发人员启动的动画 |

示例：

```ets
this.mapController.on("cameraMoveStart", (reason) => {
  console.info("cameraMoveStart", `on-cameraMoveStart reason = ${reason}`);
});
```

**off('cameraMoveStart')**

off(type: 'cameraMoveStart', callback: Callback<void>): void

取消监听相机移动开始事件。使用callback异步回调。

建议使用[MapEventManager.off(type: 'cameraMoveStart')](MapEventManager.md#ZH-CN_TOPIC_0000002553362325__offcameramovestart)。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 4.1.0(11)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 'cameraMoveStart'：监听相机移动开始事件。 |
| callback | Callback<void> | 是 | 回调函数，无返回结果的回调函数。 |

示例：

```ets
this.mapController.off("cameraMoveStart", () => {
  console.info("cameraMoveStart", `off-cameraMoveStart`);
});
```

**on('mapClick')**

on(type: 'mapClick', callback: Callback<mapCommon.LatLng>): void

监听地图点击事件。使用callback异步回调。

建议使用[MapEventManager.on(type: 'mapClick')](MapEventManager.md#ZH-CN_TOPIC_0000002553362325__onmapclick)。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 4.1.0(11)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 'mapClick'：监听地图点击事件。 |
| callback | Callback<mapCommon.LatLng> | 是 | 回调函数，返回mapCommon.LatLng。 |

示例：

```ets
this.mapController.on("mapClick", (position) => {
  console.info("mapClick", `on-mapClick position = ${position.longitude}`);
});
```

**off('mapClick')**

off(type: 'mapClick', callback: Callback<void>): void

取消监听地图点击事件。使用callback异步回调。

建议使用[MapEventManager.off(type: 'mapClick')](MapEventManager.md#ZH-CN_TOPIC_0000002553362325__offmapclick)。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 4.1.0(11)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 'mapClick'：监听地图点击事件。 |
| callback | Callback<void> | 是 | 回调函数，无返回结果的回调函数。 |

示例：

```ets
this.mapController.off("mapClick", () => {
  console.info("mapClick", `off-mapClick`);
});
```

**on('mapLoad')**

on(type: 'mapLoad', callback: Callback<void>): void

监听地图加载事件。使用callback异步回调。

建议使用[MapEventManager.on(type: 'mapLoad')](MapEventManager.md#ZH-CN_TOPIC_0000002553362325__onmapload)。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 4.1.0(11)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 'mapLoad'：监听地图加载事件。 |
| callback | Callback<void> | 是 | 回调函数，无返回结果的回调函数。 |

示例：

```ets
this.mapController.on("mapLoad", () => {
  console.info("mapLoad", `on-mapLoad`);
});
```

**off('mapLoad')**

off(type: 'mapLoad', callback: Callback<void>): void

取消监听地图加载事件。使用callback异步回调。

建议使用[MapEventManager.off(type: 'mapLoad')](MapEventManager.md#ZH-CN_TOPIC_0000002553362325__offmapload)。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 4.1.0(11)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 'mapLoad'：监听地图加载事件。 |
| callback | Callback<void> | 是 | 回调函数，无返回结果的回调函数。 |

示例：

```ets
this.mapController.off("mapLoad", () => {
  console.info("mapLoad", `off-mapLoad`);
});
```

**on('mapLongClick')**

on(type: 'mapLongClick', callback: Callback<mapCommon.LatLng>): void

监听地图长按事件。使用callback异步回调。

建议使用[MapEventManager.on(type: 'mapLongClick')](MapEventManager.md#ZH-CN_TOPIC_0000002553362325__onmaplongclick)。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 4.1.0(11)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 'mapLongClick'：监听地图长按事件。 |
| callback | Callback<mapCommon.LatLng> | 是 | 回调函数，返回mapCommon.LatLng。 |

示例：

```ets
this.mapController.on("mapLongClick", () => {
  console.info("mapLongClick", `on-mapLongClick`);
});
```

**off('mapLongClick')**

off(type: 'mapLongClick', callback: Callback<void>): void

取消监听地图长按事件。使用callback异步回调。

建议使用[MapEventManager.off(type: 'mapLongClick')](MapEventManager.md#ZH-CN_TOPIC_0000002553362325__offmaplongclick)。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 4.1.0(11)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 'mapLongClick'：监听地图长按事件。 |
| callback | Callback<void> | 是 | 回调函数，无返回结果的回调函数。 |

示例：

```ets
this.mapController.off("mapLongClick", () => {
  console.info("mapLongClick", `off-mapLongClick`);
});
```

**on('myLocationButtonClick')**

on(type: 'myLocationButtonClick', callback: Callback<void>): void

监听我的位置按钮点击事件。使用callback异步回调。

建议使用[MapEventManager.on(type: 'myLocationButtonClick')](MapEventManager.md#ZH-CN_TOPIC_0000002553362325__onmylocationbuttonclick)。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 4.1.0(11)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 'myLocationButtonClick'：监听我的位置按钮点击事件。 |
| callback | Callback<void> | 是 | 回调函数，无返回结果的回调函数。 |

示例：

```ets
this.mapController.on("myLocationButtonClick", () => {
  console.info("myLocationButtonClick", `on-myLocationButtonClick`);
});
```

**off('myLocationButtonClick')**

off(type: 'myLocationButtonClick', callback: Callback<void>): void

取消监听我的位置按钮点击事件。使用callback异步回调。

建议使用[MapEventManager.off(type: 'myLocationButtonClick')](MapEventManager.md#ZH-CN_TOPIC_0000002553362325__offmylocationbuttonclick)。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 4.1.0(11)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 'myLocationButtonClick'：监听我的位置按钮点击事件。 |
| callback | Callback<void> | 是 | 回调函数，无返回结果的回调函数。 |

示例：

```ets
this.mapController.off("myLocationButtonClick", () => {
  console.info("myLocationButtonClick", `off-myLocationButtonClick`);
});
```

**on('myLocationClick')**

on(type: 'myLocationClick', callback: Callback<mapCommon.LatLng>): void

监听我的位置点击事件。使用callback异步回调。

建议使用[MapEventManager.on(type: 'myLocationClick')](MapEventManager.md#ZH-CN_TOPIC_0000002553362325__onmylocationclick)。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 4.1.0(11)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 'myLocationClick'：监听我的位置点击事件。 |
| callback | Callback<mapCommon.LatLng> | 是 | 回调函数，返回mapCommon.LatLng。 |

示例：

```ets
this.mapController.on("myLocationClick", (position) => {
  console.info("myLocationClick", `on-myLocationClick position = ${position.longitude}`);
});
```

**off('myLocationClick')**

off(type: 'myLocationClick', callback: Callback<void>): void

取消监听我的位置点击事件。使用callback异步回调。

建议使用[MapEventManager.off(type: 'myLocationClick')](MapEventManager.md#ZH-CN_TOPIC_0000002553362325__offmylocationclick)。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 4.1.0(11)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 'myLocationClick'：监听我的位置点击事件。 |
| callback | Callback<void> | 是 | 回调函数，无返回结果的回调函数。 |

示例：

```ets
this.mapController.off("myLocationClick", () => {
  console.info("myLocationClick", `off-myLocationClick`);
});
```

**on('poiClick')**

on(type: 'poiClick', callback: Callback<mapCommon.Poi>): void

监听POI点击事件。使用callback异步回调。

建议使用[MapEventManager.on(type: 'poiClick')](MapEventManager.md#ZH-CN_TOPIC_0000002553362325__onpoiclick)。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 4.1.0(11)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 'poiClick'：监听POI点击事件。 |
| callback | Callback<mapCommon.Poi> | 是 | 回调函数，返回mapCommon.Poi。 |

示例：

```ets
this.mapController.on("poiClick", (poi) => {
  console.info("poiClick", `on-poiClick poi = ${poi.id}`);
});
```

**off('poiClick')**

off(type: 'poiClick', callback: Callback<void>): void

取消监听POI点击事件。使用callback异步回调。

建议使用[MapEventManager.off(type: 'poiClick')](MapEventManager.md#ZH-CN_TOPIC_0000002553362325__offpoiclick)。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 4.1.0(11)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 'poiClick'：监听POI点击事件。 |
| callback | Callback<void> | 是 | 回调函数，无返回结果的回调函数。 |

示例：

```ets
this.mapController.off("poiClick", () => {
 console.info("poiClick", `off-poiClick`);
});
```

**on('markerClick')**

on(type: 'markerClick', callback: Callback<Marker>): void

监听标记点击事件。使用callback异步回调。

建议使用[MapEventManager.on(type: 'markerClick')](MapEventManager.md#ZH-CN_TOPIC_0000002553362325__onmarkerclick)。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 4.1.0(11)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 'markerClick'：监听标记点击事件。 |
| callback | Callback<Marker> | 是 | 回调函数，返回Marker。 |

示例：

```ets
this.mapController.on("markerClick", (marker) => {
 console.info("markerClick", `on-markerClick position = ${marker.getId()}`);
});
```

**off('markerClick')**

off(type: 'markerClick', callback: Callback<void>): void

取消监听标记点击事件。使用callback异步回调。

建议使用[MapEventManager.off(type: 'markerClick')](MapEventManager.md#ZH-CN_TOPIC_0000002553362325__offmarkerclick)。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 4.1.0(11)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 'markerClick'：监听标记点击事件。 |
| callback | Callback<void> | 是 | 回调函数，无返回结果的回调函数。 |

示例：

```ets
this.mapController.off("markerClick", () => {
 console.info("markerClick", `off-markerClick`);
});
```

**on('markerDragStart')**

on(type: 'markerDragStart', callback: Callback<Marker>): void

监听标记开始拖拽事件。使用callback异步回调。

建议使用[MapEventManager.on(type: 'markerDragStart')](MapEventManager.md#ZH-CN_TOPIC_0000002553362325__onmarkerdragstart)。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 4.1.0(11)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 'markerDragStart'：监听标记开始拖拽事件。 |
| callback | Callback<Marker> | 是 | 回调函数，返回Marker。 |

示例：

```ets
this.mapController.on("markerDragStart", (marker) => {
 console.info("markerDragStart", `on-markerDragStart position = ${marker.getId()}`);
});
```

**off('markerDragStart')**

off(type: 'markerDragStart', callback: Callback<void>): void

取消监听标记开始拖拽事件。使用callback异步回调。

建议使用[MapEventManager.off(type: 'markerDragStart')](MapEventManager.md#ZH-CN_TOPIC_0000002553362325__offmarkerdragstart)。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 4.1.0(11)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 'markerDragStart'：监听标记开始拖拽事件。 |
| callback | Callback<void> | 是 | 回调函数，无返回结果的回调函数。 |

示例：

```ets
this.mapController.off("markerDragStart", () => {
 console.info("markerDragStart", `off-markerDragStart`);
});
```

**on('markerDrag')**

on(type: 'markerDrag', callback: Callback<Marker>): void

监听标记拖拽事件。使用callback异步回调。

建议使用[MapEventManager.on(type: 'markerDrag')](MapEventManager.md#ZH-CN_TOPIC_0000002553362325__onmarkerdrag)。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 4.1.0(11)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 'markerDrag'：监听标记拖拽事件。 |
| callback | Callback<Marker> | 是 | 回调函数，返回Marker。 |

示例：

```ets
this.mapController.on("markerDrag", (marker) => {
 console.info("markerDrag", `on-markerDrag position = ${marker.getId()}`);
});
```

**off('markerDrag')**

off(type: 'markerDrag', callback: Callback<void>): void

取消监听标记拖拽事件。使用callback异步回调。

建议使用[MapEventManager.off(type: 'markerDrag')](MapEventManager.md#ZH-CN_TOPIC_0000002553362325__offmarkerdrag)。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 4.1.0(11)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 'markerDrag'：监听标记拖拽事件。 |
| callback | Callback<void> | 是 | 回调函数，无返回结果的回调函数。 |

示例：

```ets
this.mapController.off("markerDrag", () => {
 console.info("markerDrag", `off-markerDrag`);
});
```

**on('markerDragEnd')**

on(type: 'markerDragEnd', callback: Callback<Marker>): void

监听标记拖拽结束事件。使用callback异步回调。

建议使用[MapEventManager.on(type: 'markerDragEnd')](MapEventManager.md#ZH-CN_TOPIC_0000002553362325__onmarkerdragend)。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 4.1.0(11)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 'markerDragEnd'：监听标记拖拽结束事件。 |
| callback | Callback<Marker> | 是 | 回调函数，返回Marker。 |

示例：

```ets
this.mapController.on("markerDragEnd", (marker) => {
 console.info("markerDragEnd", `on-markerDragEnd position = ${marker.getId()}`);
});
```

**off('markerDragEnd')**

off(type: 'markerDragEnd', callback: Callback<void>): void

取消监听标记拖动结束事件。使用callback异步回调。

建议使用[MapEventManager.off(type: 'markerDragEnd')](MapEventManager.md#ZH-CN_TOPIC_0000002553362325__offmarkerdragend)。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 4.1.0(11)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 'markerDragEnd'：监听标记拖动结束事件。 |
| callback | Callback<void> | 是 | 回调函数，无返回结果的回调函数。 |

示例：

```ets
this.mapController.off("markerDragEnd", () => {
 console.info("markerDragEnd", `off-markerDragEnd`);
});
```

**on('circleClick')**

on(type: 'circleClick', callback: Callback<MapCircle>): void

监听圆点击事件。使用callback异步回调。

建议使用[MapEventManager.on(type: 'circleClick')](MapEventManager.md#ZH-CN_TOPIC_0000002553362325__oncircleclick)。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 4.1.0(11)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 'circleClick'：监听圆点击事件。 |
| callback | Callback<MapCircle> | 是 | 回调函数，返回MapCircle。 |

示例：

```ets
this.mapController.on("circleClick", (position) => {
 console.info("circleClick", `on-circleClick position = ${position.getCenter().longitude}`);
});
```

**off('circleClick')**

off(type: 'circleClick', callback: Callback<void>): void

取消监听圆点击事件。使用callback异步回调。

建议使用[MapEventManager.off(type: 'circleClick')](MapEventManager.md#ZH-CN_TOPIC_0000002553362325__offcircleclick)。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 4.1.0(11)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 'circleClick'：监听圆点击事件。 |
| callback | Callback<void> | 是 | 回调函数，无返回结果的回调函数。 |

示例：

```ets
this.mapController.off("circleClick", () => {
 console.info("circleClick", `off-circleClick`);
});
```

**on('polylineClick')**

on(type: 'polylineClick', callback: Callback<MapPolyline>): void

监听折线点击事件。使用callback异步回调。

建议使用[MapEventManager.on(type: 'polylineClick')](MapEventManager.md#ZH-CN_TOPIC_0000002553362325__onpolylineclick)。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 4.1.0(11)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 'polylineClick'：监听折线点击事件。 |
| callback | Callback<MapPolyline> | 是 | 回调函数，返回MapPolyline。 |

示例：

```ets
this.mapController.on("polylineClick", (polyline) => {
  console.info("polylineClick", `on-polylineClick position = ${polyline.getId()}`);
});
```

**off('polylineClick')**

off(type: 'polylineClick', callback: Callback<void>): void

取消监听折线点击事件。使用callback异步回调。

建议使用[MapEventManager.off(type: 'polylineClick')](MapEventManager.md#ZH-CN_TOPIC_0000002553362325__offpolylineclick)。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 4.1.0(11)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 'polylineClick'：监听折线点击事件。 |
| callback | Callback<void> | 是 | 回调函数，无返回结果的回调函数。 |

示例：

```ets
this.mapController.off("polylineClick", () => {
  console.info("polylineClick", "off-polylineClick");
});
```

**on('polygonClick')**

on(type: 'polygonClick', callback: Callback<MapPolygon>): void

监听多边形点击事件。使用callback异步回调。

建议使用[MapEventManager.on(type: 'polygonClick')](MapEventManager.md#ZH-CN_TOPIC_0000002553362325__onpolygonclick)。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 4.1.0(11)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 'polygonClick'：监听多边形点击事件。 |
| callback | Callback<MapPolygon> | 是 | 回调函数，返回MapPolygon。 |

示例：

```ets
this.mapController.on("polygonClick", (polygon) => {
  console.info("polygonClick", `on-polygonClick position = ${polygon.getId()}`);
});
```

**off('polygonClick')**

off(type: 'polygonClick', callback: Callback<void>): void

取消监听多边形点击事件。使用callback异步回调。

建议使用[MapEventManager.off(type: 'polygonClick')](MapEventManager.md#ZH-CN_TOPIC_0000002553362325__offpolygonclick)。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 4.1.0(11)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 'polygonClick'：监听多边形点击事件。 |
| callback | Callback<void> | 是 | 回调函数，无返回结果的回调函数。 |

示例：

```ets
this.mapController.off("polygonClick", () => {
  console.info("polygonClick", "off-polygonClick");
});
```

**on('infoWindowClick')**

on(type: 'infoWindowClick', callback: Callback<Marker>): void

监听信息窗点击事件。使用callback异步回调。

建议使用[MapEventManager.on(type: 'infoWindowClick')](MapEventManager.md#ZH-CN_TOPIC_0000002553362325__oninfowindowclick)。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 4.1.0(11)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 'infoWindowClick'：监听信息窗点击事件。 |
| callback | Callback<Marker> | 是 | 回调函数，返回Marker。 |

示例：

```ets
this.mapController.on("infoWindowClick", (infoWindow) => {
 console.info("infoWindowClick", `on-infoWindowClick infoWindow = ${infoWindow.getId()}`);
});
```

**off('infoWindowClick')**

off(type: 'infoWindowClick', callback: Callback<void>): void

取消监听信息窗点击事件。使用callback异步回调。

建议使用[MapEventManager.off(type: 'infoWindowClick')](MapEventManager.md#ZH-CN_TOPIC_0000002553362325__offinfowindowclick)。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 4.1.0(11)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 'infoWindowClick'：监听信息窗点击事件。 |
| callback | Callback<void> | 是 | 回调函数，无返回结果的回调函数。 |

示例：

```ets
this.mapController.off("infoWindowClick", () => {
 console.info("infoWindowClick", `off-infoWindowClick`);
});
```

**on('infoWindowClose')**

on(type: 'infoWindowClose', callback: Callback<Marker>): void

监听信息窗关闭事件。使用callback异步回调。

建议使用[MapEventManager.on(type: 'infoWindowClose')](MapEventManager.md#ZH-CN_TOPIC_0000002553362325__oninfowindowclose)。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 4.1.0(11)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 'infoWindowClose'：监听信息窗关闭事件。 |
| callback | Callback<Marker> | 是 | 回调函数，返回Marker。 |

示例：

```ets
this.mapController.on("infoWindowClose", (infoWindowClose) => {
 console.info("infoWindowClose", `on-infoWindowClose infoWindowClose = ${infoWindowClose.getId()}`);
});
```

**off('infoWindowClose')**

off(type: 'infoWindowClose', callback: Callback<void>): void

取消监听信息窗关闭事件。使用callback异步回调。

建议使用[MapEventManager.off(type: 'infoWindowClose')](MapEventManager.md#ZH-CN_TOPIC_0000002553362325__offinfowindowclose)。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 4.1.0(11)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 'infoWindowClose'：监听信息窗关闭事件。 |
| callback | Callback<void> | 是 | 回调函数，无返回结果的回调函数。 |

示例：

```ets
this.mapController.off("infoWindowClose", () => {
 console.info("infoWindowClose", `off-infoWindowClose`);
});
```

**on('pointAnnotationClick')**

on(type: 'pointAnnotationClick', callback: Callback<PointAnnotation>): void

监听点注释点击事件。使用callback异步回调。

建议使用[MapEventManager.on(type: 'pointAnnotationClick')](MapEventManager.md#ZH-CN_TOPIC_0000002553362325__onpointannotationclick)。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 4.1.0(11)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 'pointAnnotationClick'：监听点注释点击事件。 |
| callback | Callback<PointAnnotation> | 是 | 回调函数，返回PointAnnotation。 |

示例：

```ets
this.mapController.on("pointAnnotationClick", (pointAnnotation) => {
 console.info("pointAnnotationClick", `on-PointAnnotationClick pointAnnotation = ${pointAnnotation.getId()}`);
});
```

**off('pointAnnotationClick')**

off(type: 'pointAnnotationClick', callback: Callback<void>): void

取消监听点注释点击事件。使用callback异步回调。

建议使用[MapEventManager.off(type: 'pointAnnotationClick')](MapEventManager.md#ZH-CN_TOPIC_0000002553362325__offpointannotationclick)。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 4.1.0(11)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 'pointAnnotationClick'：监听点注释点击事件。 |
| callback | Callback<void> | 是 | 回调函数，无返回结果的回调函数。 |

示例：

```ets
this.mapController.off("pointAnnotationClick", () => {
 console.info("pointAnnotationClick", `off-PointAnnotationClick`);
});
```

**on('bubbleClick')**

on(type: 'bubbleClick', callback: Callback<Bubble>): void

监听气泡点击事件。使用callback异步回调。

建议使用[MapEventManager.on(type: 'bubbleClick')](MapEventManager.md#ZH-CN_TOPIC_0000002553362325__onbubbleclick)。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 4.1.0(11)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 'bubbleClick'：监听气泡点击事件。 |
| callback | Callback<Bubble> | 是 | 回调函数，返回Bubble。 |

示例：

```ets
this.mapController.on("bubbleClick", (bubble) => {
 console.info("bubbleClick", `on-BubbleClick bubble = ${bubble.getId()}`);
});
```

**off('bubbleClick')**

off(type: 'bubbleClick', callback: Callback<void>): void

取消监听气泡点击事件。使用callback异步回调。

建议使用[MapEventManager.off(type: 'bubbleClick')](MapEventManager.md#ZH-CN_TOPIC_0000002553362325__offbubbleclick)。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 4.1.0(11)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 'bubbleClick'：监听气泡点击事件。 |
| callback | Callback<void> | 是 | 回调函数，无返回结果的回调函数。 |

示例：

```ets
this.mapController.off("bubbleClick", () => {
 console.info("bubbleClick", `off-BubbleClick`);
});
```

**on('imageOverlayClick')**

on(type: 'imageOverlayClick', callback: Callback<ImageOverlay>): void

监听覆盖物点击事件。使用callback异步回调。

建议使用[MapEventManager.on(type: 'imageOverlayClick')](MapEventManager.md#ZH-CN_TOPIC_0000002553362325__onimageoverlayclick)。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 'imageOverlayClick'：监听覆盖物点击事件。 |
| callback | Callback<ImageOverlay> | 是 | 回调函数，返回ImageOverlay。 |

示例：

```ets
// 监听覆盖物点击事件的回调
let imageOverlayCallback: Callback<map.ImageOverlay> = (imageOverlay:map.ImageOverlay) => {
  console.info("imageOverlay:" + imageOverlay?.getId());
};
this.mapController.on("imageOverlayClick", imageOverlayCallback)
```

**off('imageOverlayClick')**

off(type: 'imageOverlayClick', callback?: Callback<ImageOverlay>): void

取消监听覆盖物点击事件。使用callback异步回调。

建议使用[MapEventManager.off(type: 'imageOverlayClick')](MapEventManager.md#ZH-CN_TOPIC_0000002553362325__offimageoverlayclick)。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 'imageOverlayClick'：监听覆盖物点击事件。 |
| callback | Callback<ImageOverlay> | 否 | 回调函数，返回ImageOverlay，当不填时清除所有监听回调。 |

示例：

```ets
let imageOverlayCallback: Callback<map.ImageOverlay> = (imageOverlay:map.ImageOverlay) => {
  console.info("imageOverlay:" + imageOverlay?.getId());
};
this.mapController.off("imageOverlayClick", imageOverlayCallback);
```

**on('error')**

on(type: 'error', callback: ErrorCallback): void

监听发生的异常。

建议使用[MapEventManager.on(type: 'error')](MapEventManager.md#ZH-CN_TOPIC_0000002553362325__onerror)。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 4.1.0(11)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 'error'：监听发生的异常。 |
| callback | ErrorCallback | 是 | 回调函数，监听异常事件的回调。 |

示例：

```ets
this.mapController.on("error", (error) => {
  console.error("error", `on-error: Code: ${error.code}, message: ${error.message}`);
});
```

**off('error')**

off(type: 'error', callback: Callback<void>): void

取消监听发生的异常。使用callback异步回调。

建议使用[MapEventManager.off(type: 'error')](MapEventManager.md#ZH-CN_TOPIC_0000002553362325__offerror)。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 4.1.0(11)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 'error'：监听发生的异常。 |
| callback | Callback<void> | 是 | 回调函数，无返回结果的回调函数。 |

示例：

```ets
this.mapController.off("error", () => {
  console.error("error", `off-error`);
});
```

**setIndoorMapEnabled**

setIndoorMapEnabled(enabled: boolean): void

打开或关闭室内图。仅17级及以上地图层级可见室内图，仅18级及以上地图层级可见楼层调节控件。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本5.1.1(19)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

设备行为差异： 在API19及之后版本该接口在phone、tablet、2in1均可正常使用，在其他设备中返回801错误。

起始版本： 5.1.1(19)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean | 是 | 是否启用室内图，默认关闭，异常值按照默认值处理。取值范围： - true：启用室内图 - false：关闭室内图 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |

示例：

```ets
// 打开室内图
this.mapController.setIndoorMapEnabled(true);
```

**isIndoorMapEnabled**

isIndoorMapEnabled(): boolean

获取室内图开启状态。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本5.1.1(19)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

设备行为差异： 在API19及之后版本该接口在phone、tablet、2in1均可正常使用，在其他设备中返回801错误。

起始版本： 5.1.1(19)

返回值：

| 类型 | 说明 |
| --- | --- |
| boolean | - true：室内图为开启状态 - false：室内图为关闭状态 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |

示例：

```ets
let isIndoorMapEnabled = this.mapController.isIndoorMapEnabled();
```

**switchIndoorMapFloor**

switchIndoorMapFloor(buildingId: string, floorName: string): void

切换到指定的室内建筑楼层。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本5.1.1(19)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

设备行为差异： 在API19及之后版本该接口在phone、tablet、2in1均可正常使用，在其他设备中返回801错误。

起始版本： 5.1.1(19)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| buildingId | string | 是 | 建筑物的ID。从on('indoorMapEnter')方法的回调函数中获得。 |
| floorName | string | 是 | 建筑物楼层名称（如：3F）。异常值不处理。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |

示例：

```ets
this.mapController?.switchIndoorMapFloor('822588304363886720', '3F');
```

**setFloorControlsPosition**

setFloorControlsPosition(point: mapCommon.MapPoint): void

设置楼层调节控件的位置。需要先调用[setIndoorMapEnabled](#ZH-CN_TOPIC_0000002553362311__setindoormapenabled)方法来开启室内图功能，仅17级及以上地图层级可见室内图，仅18级及以上地图层级可见楼层调节控件。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本6.0.0(20)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

设备行为差异： 在API20及之后版本该接口在phone、tablet、2in1均可正常使用，在其他设备中返回801错误。

起始版本： 6.0.0(20)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| point | mapCommon.MapPoint | 是 | 设置楼层调节控件的位置，单位：px。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |

示例：

```ets
this.mapController?.setFloorControlsPosition({
  positionX: 500,
  positionY: 500
});
```

**isApproveNumberEnabled**

isApproveNumberEnabled(): boolean

获取审图号显示状态。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本6.1.0(23)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 6.1.0(23)

返回值：

| 类型 | 说明 |
| --- | --- |
| boolean | - true：显示审图号 - false：隐藏审图号 |

示例：

```ets
let isApproveNumberEnabled = this.mapController?.isApproveNumberEnabled();
```

**setApproveNumberEnabled**

setApproveNumberEnabled(enabled: boolean): void

设置是否显示审图号。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本6.1.0(23)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 6.1.0(23)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean | 是 | 设置是否显示审图号，只有路由地在中国才会显示。默认值：false。 - true：显示审图号 - false：隐藏审图号 |

示例：

```ets
this.mapController?.setApproveNumberEnabled(true);
```