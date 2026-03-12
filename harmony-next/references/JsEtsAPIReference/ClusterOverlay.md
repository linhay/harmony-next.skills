# ClusterOverlay

#### 导入模块

```ets
import { map, mapCommon } from '@kit.MapKit';
```

#### ClusterOverlay

聚合图层类。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**5.0.0(12)

**示例：**

```ets
let clusterItem1: mapCommon.ClusterItem = {
  position: {
    latitude: 31.984,
    longitude: 118.766
  }
};
let clusterItem2: mapCommon.ClusterItem = {
  position: {
    latitude: 31.974,
    longitude:118.75
  }
};
let array: Array<mapCommon.ClusterItem> = [
  clusterItem1,
  clusterItem2
];
let clusterOverlayParams: mapCommon.ClusterOverlayParams = { distance: 40, clusterItems: array };
let clusterOverlay: map.ClusterOverlay = await this.mapController.addClusterOverlay(clusterOverlayParams);
```

#### on('clusterClick')

on(type: 'clusterClick', callback: Callback<Array<mapCommon.ClusterItem>>): void

监听cluster的点击事件。使用callback异步回调。

建议使用[ClusterOverlay.on(type: 'click')](#section8306133712135)。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**5.0.0(12)

**参数：**

**参数名**

**类型**

必填

**说明**

type

string

是

'clusterClick'：聚合图层的聚合点点击监听事件。

callback

Callback<Array<[mapCommon.ClusterItem](mapCommon（地图属性模型）.md#section9436522104316)>>

是

回调函数，返回Array<[mapCommon.ClusterItem](mapCommon（地图属性模型）.md#section9436522104316)>。

**示例：**

```ets
clusterOverlay.on("clusterClick", (clusterItems) => {
  console.info(`callback: ${clusterItems.length}`);
});
```

#### off('clusterClick')

off(type: 'clusterClick', callback?: Callback<void>): void

取消监听cluster的点击事件。使用callback异步回调。

建议使用[ClusterOverlay.off(type: 'click')](#section13314133751318)。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**5.0.0(12)

**参数：**

**参数名**

**类型**

必填

**说明**

type

string

是

'clusterClick'：聚合图层的聚合点点击监听事件。

callback

Callback<void>

否

回调函数。无返回结果的回调函数。

**示例：**

```ets
clusterOverlay.off("clusterClick", () => {
  console.info("callback off");
});
```

#### on('click')

on(type: 'click', callback: Callback<Array<mapCommon.ClusterItem>>): void

监听聚合图层的聚合点点击事件。支持传递多个callback异步回调。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**5.0.0(12)

**参数：**

**参数名**

**类型**

必填

**说明**

type

string

是

'click'：监听聚合图层的聚合点点击事件。

callback

Callback<Array<[mapCommon.ClusterItem](mapCommon（地图属性模型）.md#section9436522104316)>>

是

回调函数，返回Array<[mapCommon.ClusterItem](mapCommon（地图属性模型）.md#section9436522104316)>，监听聚合图层的聚合点点击事件。

**示例：**

```ets
let callback1 = (clusterItem: Array<mapCommon.ClusterItem>) => {
  console.info("click", `callback1 clusterItem length: ${clusterItem.length}`);
};
let callback2 = (clusterItem: Array<mapCommon.ClusterItem>) => {
  console.info("click", `callback2 clusterItem length: ${clusterItem.length}`);
};
let callback3 = (clusterItem: Array<mapCommon.ClusterItem>) => {
  console.info("click", `callback3 clusterItem length: ${clusterItem.length}`);
};
clusterOverlay.on("click", callback1);
clusterOverlay.on("click", callback2);
clusterOverlay.on("click", callback3);
```

#### off('click')

off(type: 'click', callback?: Callback<Array<mapCommon.ClusterItem>>): void

取消监听聚合图层的聚合点点击事件。支持传递多个callback异步回调。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**5.0.0(12)

**参数：**

**参数名**

**类型**

必填

**说明**

type

string

是

'click'：监听聚合图层的聚合点点击事件。

callback

Callback<Array<[mapCommon.ClusterItem](mapCommon（地图属性模型）.md#section9436522104316)>>

否

回调函数，返回Array<[mapCommon.ClusterItem](mapCommon（地图属性模型）.md#section9436522104316)>，取消监听聚合图层的聚合点点击事件。

- callback为空：取消所有callback回调。
- callback非空：取消指定的callback回调。

**示例：**

```ets
let callback1 = (clusterItem: Array<mapCommon.ClusterItem>) => {
  console.info("click", `callback1 clusterItem`);
};
let callback2 = (clusterItem: Array<mapCommon.ClusterItem>) => {
  console.info("click", `callback2 clusterItem`);
};
let callback3 = (clusterItem: Array<mapCommon.ClusterItem>) => {
  console.info("click", `callback3 clusterItem`);
};
clusterOverlay.on("click", callback1);
clusterOverlay.on("click", callback2);
clusterOverlay.on("click", callback3);

// 只取消callback1对象的事件响应，当click事件发生时，callback2和callback3会正常被调用
clusterOverlay.off('click', callback1);
// 取消全部click事件响应
clusterOverlay.off('click');
```

#### on('markerClusterClick')

on(type: 'markerClusterClick', callback: Callback<MarkerClusterInfo>): void

监听聚合图层的标记点击事件。使用callback异步回调。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.3(15)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**5.0.3(15)

**参数：**

**参数名**

**类型**

必填

**说明**

type

string

是

'markerClusterClick'：聚合图层的标记点击监听事件。

callback

Callback<[MarkerClusterInfo](MarkerClusterInfo.md)>

是

回调函数，返回Callback<[MarkerClusterInfo](MarkerClusterInfo.md)>，监听聚合图层的标记点击事件。

MarkerClusterInfo包括：

- marker：聚合图层的标记。
- clusterItems：聚合节点数组。

**示例：**

```ets
let callback1 = (markerClusterInfo: map.MarkerClusterInfo) => {
  console.info("markerClusterClick", `callback1 markerClusterInfo`);
};
let callback2 = (markerClusterInfo: map.MarkerClusterInfo) => {
  console.info("markerClusterClick", `callback2 markerClusterInfo`);
};
let callback3 = (markerClusterInfo: map.MarkerClusterInfo) => {
  console.info("markerClusterClick", `callback3 markerClusterInfo`);
};
clusterOverlay.on("markerClusterClick", callback1);
clusterOverlay.on("markerClusterClick", callback2);
clusterOverlay.on("markerClusterClick", callback3);
```

#### off('markerClusterClick')

off(type: 'markerClusterClick', callback?: Callback<MarkerClusterInfo>): void

取消监听聚合图层的标记点击事件。使用callback异步回调。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.3(15)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**5.0.3(15)

**参数：**

**参数名**

**类型**

必填

**说明**

type

string

是

'markerClusterClick'：聚合图层的标记点击监听事件。

callback

Callback<[MarkerClusterInfo](MarkerClusterInfo.md)>

否

回调函数，返回Callback<[MarkerClusterInfo](MarkerClusterInfo.md)>，取消监听聚合图层的标记点击事件。

- callback为空：取消所有callback回调。
- callback非空：取消指定的callback回调。

MarkerClusterInfo包括：

- marker：聚合图层的标记。
- clusterItems：聚合节点数组。

**示例：**

```ets
let callback1 = (markerClusterInfo: map.MarkerClusterInfo) => {
  console.info("markerClusterClick", `callback1 markerClusterInfo`);
};
let callback2 = (markerClusterInfo: map.MarkerClusterInfo) => {
  console.info("markerClusterClick", `callback2 markerClusterInfo`);
};
let callback3 = (markerClusterInfo: map.MarkerClusterInfo) => {
  console.info("markerClusterClick", `callback3 markerClusterInfo`);
};
clusterOverlay.on("markerClusterClick", callback1);
clusterOverlay.on("markerClusterClick", callback2);
clusterOverlay.on("markerClusterClick", callback3);
// 只取消callback1对象的事件响应，当markerClusterClick事件发生时，callback2和callback3会正常被调用
clusterOverlay.off('markerClusterClick', callback1);
// 取消全部markerClusterClick事件响应
clusterOverlay.off('markerClusterClick');
```

#### addItem

addItem(item: mapCommon.ClusterItem): Promise<void>

新增聚合节点。使用Promise异步回调。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**5.0.0(12)

**参数：**

**参数名**

**类型**

必填

**说明**

item

mapCommon.[ClusterItem](mapCommon（地图属性模型）.md#section9436522104316)

是

待聚合节点。

**返回值：**

类型

说明

Promise<void>

Promise对象。无返回结果的Promise对象。

**示例：**

```ets
let clusterItem: mapCommon.ClusterItem = {
  position: {
    latitude: 31.98,
    longitude: 118.766
  }
};
await clusterOverlay.addItem(clusterItem);
```

#### remove

remove(): Promise<void>

移除聚合图层。使用Promise异步回调。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**5.0.0(12)

**返回值：**

类型

说明

Promise<void>

Promise对象。无返回结果的Promise对象。

**示例：**

```ets
await clusterOverlay.remove();
```