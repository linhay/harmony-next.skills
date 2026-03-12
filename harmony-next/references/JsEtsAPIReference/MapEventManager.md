# MapEventManager

#### 导入模块

```ets
import { map, mapCommon } from '@kit.MapKit';
```

#### MapEventManager

地图监听事件管理器。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**5.0.0(12)

**示例：**

```ets
let mapEventManager: map.MapEventManager = this.mapController.getEventManager();
```

#### on('cameraChange')

on(type: 'cameraChange', callback: Callback<mapCommon.LatLng>): void

监听地图相机状态变化。支持传递多个callback异步回调。此回调不会在动画过程中触发，而是在动画结束时触发。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**5.0.0(12)

**参数**：

**参数名**

**类型**

必填

**说明**

type

string

是

'cameraChange'：监听地图相机状态变化事件。

callback

Callback<[mapCommon.LatLng](mapCommon（地图属性模型）.md#section20691173773810)>

是

回调函数，返回[mapCommon.LatLng](mapCommon（地图属性模型）.md#section20691173773810)，监听地图相机状态变化事件。该回调不会在动画过程中触发，而是在动画结束时触发。

**示例：**

```ets
let callback1 = (position: mapCommon.LatLng) => {
  console.info("cameraChange", `callback1 position = ${position.longitude}`);
};
let callback2 = (position: mapCommon.LatLng) => {
  console.info("cameraChange", `callback2 position = ${position.longitude}`);
};
let callback3 = (position: mapCommon.LatLng) => {
  console.info("cameraChange", `callback3 position = ${position.longitude}`);
};
mapEventManager.on("cameraChange", callback1);
mapEventManager.on("cameraChange", callback2);
mapEventManager.on("cameraChange", callback3);
```

#### off('cameraChange')

off(type: 'cameraChange', callback?: Callback<mapCommon.LatLng>): void

取消监听地图相机状态变化事件。支持传递多个callback异步回调。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**5.0.0(12)

**参数**：

**参数名**

**类型**

必填

**说明**

type

string

是

'cameraChange'：监听地图相机状态变化事件。

callback

Callback<[mapCommon.LatLng](mapCommon（地图属性模型）.md#section20691173773810)>

否

回调函数，返回[mapCommon.LatLng](mapCommon（地图属性模型）.md#section20691173773810)，取消监听地图相机状态变化事件。

- callback为空：取消所有callback回调。
- callback非空：取消指定的callback回调。

**示例：**

```ets
let callback1 = (position: mapCommon.LatLng) => {
  console.info("cameraChange", `callback1 position`);
};
let callback2 = (position: mapCommon.LatLng) => {
  console.info("cameraChange", `callback2 position`);
};
let callback3 = (position: mapCommon.LatLng) => {
  console.info("cameraChange", `callback3 position`);
};
mapEventManager.on("cameraChange", callback1);
mapEventManager.on("cameraChange", callback2);
mapEventManager.on("cameraChange", callback3);
// 只取消callback1对象的事件响应，当cameraChange事件发生时，callback2和callback3会正常被调用
mapEventManager.off('cameraChange', callback1);
// 取消所有cameraChange事件响应
mapEventManager.off('cameraChange');
```

#### on('cameraIdle')

on(type: 'cameraIdle', callback: Callback<void>): void

监听相机移动结束事件。支持传递多个callback异步回调。

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

'cameraIdle'：监听相机移动结束事件。

callback

Callback<void>

是

回调函数，无返回结果的回调函数，监听相机移动结束事件。

**示例：**

```ets
let callback1 = () => {
  console.info("cameraIdle", `callback1`);
};
let callback2 = () => {
  console.info("cameraIdle", `callback2`);
};
let callback3 = () => {
  console.info("cameraIdle", `callback3`);
};
mapEventManager.on("cameraIdle", callback1);
mapEventManager.on("cameraIdle", callback2);
mapEventManager.on("cameraIdle", callback3);
```

#### off('cameraIdle')

off(type: 'cameraIdle', callback?: Callback<void>): void

取消监听相机移动结束事件。支持传递多个callback异步回调。

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

'cameraIdle'：监听相机移动结束事件。

callback

Callback<void>

否

回调函数，无返回结果的回调函数，取消监听相机移动结束事件。

- callback为空：取消所有callback回调。
- callback非空：取消指定的callback回调。

**示例：**

```ets
let callback1 = () => {
  console.info("cameraIdle", `callback1`);
};
let callback2 = () => {
  console.info("cameraIdle", `callback2`);
};
let callback3 = () => {
  console.info("cameraIdle", `callback3`);
};
mapEventManager.on("cameraIdle", callback1);
mapEventManager.on("cameraIdle", callback2);
mapEventManager.on("cameraIdle", callback3);
// 只取消callback1对象的事件响应，当cameraIdle事件发生时，callback2和callback3会正常被调用
mapEventManager.off('cameraIdle', callback1);
// 取消全部cameraIdle事件响应
mapEventManager.off('cameraIdle');
```

#### on('cameraMoveCancel')

on(type: 'cameraMoveCancel', callback: Callback<void>): void

监听相机移动取消事件。支持传递多个callback异步回调。

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

'cameraMoveCancel'：监听地图相机移动取消事件。

callback

Callback<void>

是

回调函数，无返回结果的回调函数，监听地图相机移动取消事件。

**示例：**

```ets
let callback1 = () => {
  console.info("cameraMoveCancel", `callback1`);
};
let callback2 = () => {
  console.info("cameraMoveCancel", `callback2`);
};
let callback3 = () => {
  console.info("cameraMoveCancel", `callback3`);
};
mapEventManager.on("cameraMoveCancel", callback1);
mapEventManager.on("cameraMoveCancel", callback2);
mapEventManager.on("cameraMoveCancel", callback3);
```

#### off('cameraMoveCancel')

off(type: 'cameraMoveCancel', callback?: Callback<void>): void

取消监听相机移动取消事件。支持传递多个callback异步回调。

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

'cameraMoveCancel'：监听地图相机移动取消事件。

callback

Callback<void>

否

回调函数，无返回结果的回调函数，取消监听地图相机移动取消事件。

- callback为空：取消所有callback回调。
- callback非空：取消指定的callback回调。

**示例：**

```ets
let callback1 = () => {
  console.info("cameraMoveCancel", `callback1`);
};
let callback2 = () => {
  console.info("cameraMoveCancel", `callback2`);
};
let callback3 = () => {
  console.info("cameraMoveCancel", `callback3`);
};
mapEventManager.on("cameraMoveCancel", callback1);
mapEventManager.on("cameraMoveCancel", callback2);
mapEventManager.on("cameraMoveCancel", callback3);
// 只取消callback1对象的事件响应，当cameraMoveCancel事件发生时，callback2和callback3会正常被调用
mapEventManager.off('cameraMoveCancel', callback1);
// 取消全部cameraMoveCancel事件响应
mapEventManager.off('cameraMoveCancel');
```

#### on('cameraMove')

on(type: 'cameraMove', callback: Callback<void>): void

监听相机移动事件。支持传递多个callback异步回调。

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

'cameraMove'：监听相机移动事件。

callback

Callback<void>

是

回调函数，无返回结果的回调函数，监听相机移动事件。

**示例：**

```ets
let callback1 = () => {
  console.info("cameraMove", `callback1`);
};
let callback2 = () => {
  console.info("cameraMove", `callback2`);
};
let callback3 = () => {
  console.info("cameraMove", `callback3`);
};
mapEventManager.on("cameraMove", callback1);
mapEventManager.on("cameraMove", callback2);
mapEventManager.on("cameraMove", callback3);
```

#### off('cameraMove')

off(type: 'cameraMove', callback?: Callback<void>): void

取消监听相机移动事件。支持传递多个callback异步回调。

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

'cameraMove'：监听相机移动事件。

callback

Callback<void>

否

回调函数，无返回结果的回调函数，取消监听相机移动事件。

- callback为空：取消所有callback回调。
- callback非空：取消指定的callback回调。

**示例：**

```ets
let callback1 = () => {
  console.info("cameraMove", `callback1`);
};
let callback2 = () => {
  console.info("cameraMove", `callback2`);
};
let callback3 = () => {
  console.info("cameraMove", `callback3`);
};
mapEventManager.on("cameraMove", callback1);
mapEventManager.on("cameraMove", callback2);
mapEventManager.on("cameraMove", callback3);
// 只取消callback1对象的事件响应，当cameraMove事件发生时，callback2和callback3会正常被调用
mapEventManager.off('cameraMove', callback1);
// 取消全部cameraMove事件响应
mapEventManager.off('cameraMove');
```

#### on('cameraMoveStart')

on(type: 'cameraMoveStart', callback: Callback<number>): void

监听相机移动开始事件。支持传递多个callback异步回调。

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

'cameraMoveStart'：监听相机移动开始事件。

callback

Callback<number>

是

回调函数，返回number，监听相机移动开始事件。

number表示相机改变的原因：

- 1：地图上的用户手势
- 2：用户交互产生的默认动画
- 3：开发人员启动的动画

**示例：**

```ets
let callback1 = (reason: number) => {
  console.info("cameraMoveStart", `callback1 reason = ${reason}`);
};
let callback2 = (reason: number) => {
  console.info("cameraMoveStart", `callback2 reason = ${reason}`);
};
let callback3 = (reason: number) => {
  console.info("cameraMoveStart", `callback3 reason = ${reason}`);
};
mapEventManager.on("cameraMoveStart", callback1);
mapEventManager.on("cameraMoveStart", callback2);
mapEventManager.on("cameraMoveStart", callback3);
```

#### off('cameraMoveStart')

off(type: 'cameraMoveStart', callback?: Callback<number>): void

取消监听相机移动开始事件。支持传递多个callback异步回调。

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

'cameraMoveStart'：监听相机移动开始事件。

callback

Callback<number>

否

回调函数，取消监听相机移动开始事件。

- callback为空：取消所有callback回调。
- callback非空：取消指定的callback回调。

number表示相机改变的原因：

- 1：地图上的用户手势
- 2：用户交互产生的默认动画
- 3：开发人员启动的动画

**示例：**

```ets
let callback1 = (reason: number) => {
  console.info("cameraMoveStart", `callback1`);
};
let callback2 = (reason: number) => {
  console.info("cameraMoveStart", `callback2`);
};
let callback3 = (reason: number) => {
  console.info("cameraMoveStart", `callback3`);
};
mapEventManager.on("cameraMoveStart", callback1);
mapEventManager.on("cameraMoveStart", callback2);
mapEventManager.on("cameraMoveStart", callback3);

// 只取消callback1对象的事件响应，当cameraMoveStart事件发生时，callback2和callback3会正常被调用
mapEventManager.off('cameraMoveStart', callback1);
// 取消全部cameraMoveStart事件响应
mapEventManager.off('cameraMoveStart');
```

#### on('mapClick')

on(type: 'mapClick', callback: Callback<mapCommon.LatLng>): void

监听地图点击事件。支持传递多个callback异步回调。

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

'mapClick'：监听地图点击事件。

callback

Callback<[mapCommon.LatLng](mapCommon（地图属性模型）.md#section20691173773810)>

是

回调函数，返回[mapCommon.LatLng](mapCommon（地图属性模型）.md#section20691173773810)，监听地图点击事件。

**示例：**

```ets
let callback1 = (position: mapCommon.LatLng) => {
  console.info("mapClick", `callback1 position = ${position.longitude}`);
};
let callback2 = (position: mapCommon.LatLng) => {
  console.info("mapClick", `callback2 position = ${position.longitude}`);
};
let callback3 = (position: mapCommon.LatLng) => {
  console.info("mapClick", `callback3 position = ${position.longitude}`);
};
mapEventManager.on("mapClick", callback1);
mapEventManager.on("mapClick", callback2);
mapEventManager.on("mapClick", callback3);
```

#### off('mapClick')

off(type: 'mapClick', callback?: Callback<[mapCommon.LatLng](mapCommon（地图属性模型）.md#section20691173773810)>): void

取消监听地图点击事件。支持传递多个callback异步回调。

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

'mapClick'：监听地图点击事件。

callback

Callback<[mapCommon.LatLng](mapCommon（地图属性模型）.md#section20691173773810)>

否

回调函数，返回[mapCommon.LatLng](mapCommon（地图属性模型）.md#section20691173773810)，取消监听地图点击事件。

- callback为空：取消所有callback回调。
- callback非空：取消指定的callback回调。

**示例：**

```ets
let callback1 = (position: mapCommon.LatLng) => {
  console.info("mapClick", `callback1 position`);
};
let callback2 = (position: mapCommon.LatLng) => {
  console.info("mapClick", `callback2 position`);
};
let callback3 = (position: mapCommon.LatLng) => {
  console.info("mapClick", `callback3 position`);
};
mapEventManager.on("mapClick", callback1);
mapEventManager.on("mapClick", callback2);
mapEventManager.on("mapClick", callback3);

// 只取消callback1对象的事件响应，当mapClick事件发生时，callback2和callback3会正常被调用
mapEventManager.off('mapClick', callback1);
// 取消全部mapClick事件响应
mapEventManager.off('mapClick');
```

#### on('mapLoad')

on(type: 'mapLoad', callback: Callback<void>): void

监听地图加载事件。支持传递多个callback异步回调。

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

'mapLoad'：监听地图加载事件。

callback

Callback<void>

是

回调函数，无返回结果的回调函数，监听地图加载事件。

**示例：**

```ets
let callback1 = () => {
  console.info("mapLoad", `callback1`);
};
let callback2 = () => {
  console.info("mapLoad", `callback2`);
};
let callback3 = () => {
  console.info("mapLoad", `callback3`);
};
mapEventManager.on("mapLoad", callback1);
mapEventManager.on("mapLoad", callback2);
mapEventManager.on("mapLoad", callback3);
```

#### off('mapLoad')

off(type: 'mapLoad', callback?: Callback<void>): void

取消监听地图加载事件。支持传递多个callback异步回调。

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

'mapLoad'：监听地图加载事件。

callback

Callback<void>

否

回调函数，无返回结果的回调函数，取消监听地图加载事件。

- callback为空：取消所有callback回调。
- callback非空：取消指定的callback回调。

**示例：**

```ets
let callback1 = () => {
  console.info("mapLoad", `callback1`);
};
let callback2 = () => {
  console.info("mapLoad", `callback2`);
};
let callback3 = () => {
  console.info("mapLoad", `callback3`);
};
mapEventManager.on("mapLoad", callback1);
mapEventManager.on("mapLoad", callback2);
mapEventManager.on("mapLoad", callback3);

// 只取消callback1对象的事件响应，当mapLoad事件发生时，callback2和callback3会正常被调用
mapEventManager.off('mapLoad', callback1);
// 取消全部mapLoad事件响应
mapEventManager.off('mapLoad');
```

#### on('mapLongClick')

on(type: 'mapLongClick', callback: Callback<mapCommon.LatLng>): void

监听地图长按事件。支持传递多个callback异步回调。

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

'mapLongClick'：监听地图长按事件。

callback

Callback<[mapCommon.LatLng](mapCommon（地图属性模型）.md#section20691173773810)>

是

回调函数，返回[mapCommon.LatLng](mapCommon（地图属性模型）.md#section20691173773810)，监听地图长按事件。

**示例：**

```ets
let callback1 = (position: mapCommon.LatLng) => {
  console.info("mapLongClick", `callback1 position = ${position.longitude}`);
};
let callback2 = (position: mapCommon.LatLng) => {
  console.info("mapLongClick", `callback2 position = ${position.longitude}`);
};
let callback3 = (position: mapCommon.LatLng) => {
  console.info("mapLongClick", `callback3 position = ${position.longitude}`);
};
mapEventManager.on("mapLongClick", callback1);
mapEventManager.on("mapLongClick", callback2);
mapEventManager.on("mapLongClick", callback3);
```

#### off('mapLongClick')

off(type: 'mapLongClick', callback?: Callback<mapCommon.LatLng>): void

取消监听地图长按事件。支持传递多个callback异步回调。

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

'mapLongClick'：监听地图长按事件。

callback

Callback<[mapCommon.LatLng](mapCommon（地图属性模型）.md#section20691173773810)>

否

回调函数，返回[mapCommon.LatLng](mapCommon（地图属性模型）.md#section20691173773810)，取消监听地图长按事件。

- callback为空：取消所有callback回调。
- callback非空：取消指定的callback回调。

**示例：**

```ets
let callback1 = (position: mapCommon.LatLng) => {
  console.info("mapLongClick", `callback1 position`);
};
let callback2 = (position: mapCommon.LatLng) => {
  console.info("mapLongClick", `callback2 position`);
};
let callback3 = (position: mapCommon.LatLng) => {
  console.info("mapLongClick", `callback3 position`);
};
mapEventManager.on("mapLongClick", callback1);
mapEventManager.on("mapLongClick", callback2);
mapEventManager.on("mapLongClick", callback3);

// 只取消callback1对象的事件响应，当mapLongClick事件发生时，callback2和callback3会正常被调用
mapEventManager.off('mapLongClick', callback1);
// 取消全部mapLongClick事件响应
mapEventManager.off('mapLongClick');
```

#### on('myLocationButtonClick')

on(type: 'myLocationButtonClick', callback: Callback<void>): void

监听“我的位置”按钮点击事件。支持传递多个callback异步回调。

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

'myLocationButtonClick'：监听“我的位置”按钮点击事件。

callback

Callback<void>

是

回调函数，无返回结果的回调函数，监听“我的位置”按钮点击事件。

**示例：**

```ets
let callback1 = () => {
  console.info("myLocationButtonClick", `callback1`);
};
let callback2 = () => {
  console.info("myLocationButtonClick", `callback2`);
};
let callback3 = () => {
  console.info("myLocationButtonClick", `callback3`);
};
mapEventManager.on("myLocationButtonClick", callback1);
mapEventManager.on("myLocationButtonClick", callback2);
mapEventManager.on("myLocationButtonClick", callback3);
```

#### off('myLocationButtonClick')

off(type: 'myLocationButtonClick', callback?: Callback<void>): void

取消监听“我的位置”按钮点击事件。支持传递多个callback异步回调。

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

'myLocationButtonClick'：监听“我的位置”按钮点击事件。

callback

Callback<void>

否

回调函数，无返回结果的回调函数，取消监听“我的位置”按钮点击事件。

- callback为空：取消所有callback回调。
- callback非空：取消指定的callback回调。

**示例：**

```ets
let callback1 = () => {
  console.info("myLocationButtonClick", `callback1`);
};
let callback2 = () => {
  console.info("myLocationButtonClick", `callback2`);
};
let callback3 = () => {
  console.info("myLocationButtonClick", `callback3`);
};
mapEventManager.on("myLocationButtonClick", callback1);
mapEventManager.on("myLocationButtonClick", callback2);
mapEventManager.on("myLocationButtonClick", callback3);

// 只取消callback1对象的事件响应，当myLocationButtonClick事件发生时，callback2和callback3会正常被调用
mapEventManager.off('myLocationButtonClick', callback1);
// 取消全部myLocationButtonClick事件响应
mapEventManager.off('myLocationButtonClick');
```

#### on('myLocationClick')

on(type: 'myLocationClick', callback: Callback<mapCommon.LatLng>): void

监听“我的位置”点击事件。支持传递多个callback异步回调。

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

'myLocationClick'：监听“我的位置”点击事件。

callback

Callback<[mapCommon.LatLng](mapCommon（地图属性模型）.md#section20691173773810)>

是

回调函数，返回[mapCommon.LatLng](mapCommon（地图属性模型）.md#section20691173773810)，监听“我的位置”点击事件。

**示例：**

```ets
let callback1 = (position: mapCommon.LatLng) => {
  console.info("myLocationClick", `callback1 position = ${position.longitude}`);
};
let callback2 = (position: mapCommon.LatLng) => {
  console.info("myLocationClick", `callback2 position = ${position.longitude}`);
};
let callback3 = (position: mapCommon.LatLng) => {
  console.info("myLocationClick", `callback3 position = ${position.longitude}`);
};
mapEventManager.on("myLocationClick", callback1);
mapEventManager.on("myLocationClick", callback2);
mapEventManager.on("myLocationClick", callback3);
```

#### off('myLocationClick')

off(type: 'myLocationClick', callback?: Callback<mapCommon.LatLng>): void

取消监听“我的位置”点击事件。支持传递多个callback异步回调。

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

'myLocationClick'：监听“我的位置”点击事件。

callback

Callback<[mapCommon.LatLng](mapCommon（地图属性模型）.md#section20691173773810)>

否

回调函数，返回[mapCommon.LatLng](mapCommon（地图属性模型）.md#section20691173773810)，取消监听“我的位置”点击事件。

- callback为空：取消所有callback回调。
- callback非空：取消指定的callback回调。

**示例：**

```ets
let callback1 = (position: mapCommon.LatLng) => {
  console.info("myLocationClick", `callback1 position`);
};
let callback2 = (position: mapCommon.LatLng) => {
  console.info("myLocationClick", `callback2 position`);
};
let callback3 = (position: mapCommon.LatLng) => {
  console.info("myLocationClick", `callback3 position`);
};
mapEventManager.on("myLocationClick", callback1);
mapEventManager.on("myLocationClick", callback2);
mapEventManager.on("myLocationClick", callback3);

// 只取消callback1对象的事件响应，当myLocationClick事件发生时，callback2和callback3会正常被调用
mapEventManager.off('myLocationClick', callback1);
// 取消全部myLocationClick事件响应
mapEventManager.off('myLocationClick');
```

#### on('poiClick')

on(type: 'poiClick', callback: Callback<mapCommon.Poi>): void

监听POI点击事件。支持传递多个callback异步回调。

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

'poiClick'：监听POI点击事件。

callback

Callback<[mapCommon.Poi](mapCommon（地图属性模型）.md#section1155919456273)>

是

回调函数，返回[mapCommon.Poi](mapCommon（地图属性模型）.md#section1155919456273)，监听POI点击事件。

**示例：**

```ets
let callback1 = (poi: mapCommon.Poi) => {
  console.info("poiClick", `callback1 poi = ${poi.id}`);
};
let callback2 = (poi: mapCommon.Poi) => {
  console.info("poiClick", `callback2 poi = ${poi.id}`);
};
let callback3 = (poi: mapCommon.Poi) => {
  console.info("poiClick", `callback3 poi = ${poi.id}`);
};
mapEventManager.on("poiClick", callback1);
mapEventManager.on("poiClick", callback2);
mapEventManager.on("poiClick", callback3);
```

#### off('poiClick')

off(type: 'poiClick', callback?: Callback<mapCommon.Poi>): void

取消监听POI点击事件。支持传递多个callback异步回调。

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

'poiClick'：监听POI点击事件。

callback

Callback<[mapCommon.Poi](mapCommon（地图属性模型）.md#section1155919456273)>

否

回调函数，返回[mapCommon.Poi](mapCommon（地图属性模型）.md#section1155919456273)，取消监听POI点击事件。

- callback为空：取消所有callback回调。
- callback非空：取消指定的callback回调。

**示例：**

```ets
let callback1 = (poi: mapCommon.Poi) => {
  console.info("poiClick", `callback1 poi`);
};
let callback2 = (poi: mapCommon.Poi) => {
  console.info("poiClick", `callback2 poi`);
};
let callback3 = (poi: mapCommon.Poi) => {
  console.info("poiClick", `callback3 poi`);
};
mapEventManager.on("poiClick", callback1);
mapEventManager.on("poiClick", callback2);
mapEventManager.on("poiClick", callback3);

// 只取消callback1对象的事件响应，当poiClick事件发生时，callback2和callback3会正常被调用
mapEventManager.off('poiClick', callback1);
// 取消全部poiClick事件响应
mapEventManager.off('poiClick');
```

#### on('markerClick')

on(type: 'markerClick', callback: Callback<Marker>): void

监听标记点击事件。支持传递多个callback异步回调。

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

'markerClick'：监听标记点击事件。

callback

Callback<[Marker](Marker.md)>

是

回调函数，返回[Marker](Marker.md)，监听标记点击事件。

**示例：**

```ets
let callback1 = (marker: map.Marker) => {
  console.info("markerClick", `callback1 marker = ${marker.getId()}`);
};
let callback2 = (marker: map.Marker) => {
  console.info("markerClick", `callback2 marker = ${marker.getId()}`);
};
let callback3 = (marker: map.Marker) => {
  console.info("markerClick", `callback3 marker = ${marker.getId()}`);
};
mapEventManager.on("markerClick", callback1);
mapEventManager.on("markerClick", callback2);
mapEventManager.on("markerClick", callback3);
```

#### off('markerClick')

off(type: 'markerClick', callback?: Callback<Marker>): void

取消监听标记点击事件。支持传递多个callback异步回调。

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

'markerClick'：监听标记点击事件。

callback

Callback<[Marker](Marker.md)>

否

回调函数，返回[Marker](Marker.md)，取消监听标记点击事件。

- callback为空：取消所有callback回调。
- callback非空：取消指定的callback回调。

**示例：**

```ets
let callback1 = (marker: map.Marker) => {
  console.info("markerClick", `callback1 marker`);
};
let callback2 = (marker: map.Marker) => {
  console.info("markerClick", `callback2 marker`);
};
let callback3 = (marker: map.Marker) => {
  console.info("markerClick", `callback3 marker`);
};
mapEventManager.on("markerClick", callback1);
mapEventManager.on("markerClick", callback2);
mapEventManager.on("markerClick", callback3);

// 只取消callback1对象的事件响应，当markerClick事件发生时，callback2和callback3会正常被调用
mapEventManager.off('markerClick', callback1);
// 取消全部markerClick事件响应
mapEventManager.off('markerClick');
```

#### on('markerDragStart')

on(type: 'markerDragStart', callback: Callback<Marker>): void

监听标记开始拖拽事件。支持传递多个callback异步回调。

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

'markerDragStart'：监听标记开始拖拽事件。

callback

Callback<[Marker](Marker.md)>

是

回调函数，返回[Marker](Marker.md)，监听标记开始拖拽事件。

**示例：**

```ets
let callback1 = (marker: map.Marker) => {
  console.info("markerDragStart", `callback1 marker = ${marker.getId()}`);
};
let callback2 = (marker: map.Marker) => {
  console.info("markerDragStart", `callback2 marker = ${marker.getId()}`);
};
let callback3 = (marker: map.Marker) => {
  console.info("markerDragStart", `callback3 marker = ${marker.getId()}`);
};
mapEventManager.on("markerDragStart", callback1);
mapEventManager.on("markerDragStart", callback2);
mapEventManager.on("markerDragStart", callback3);
```

#### off('markerDragStart')

off(type: 'markerDragStart', callback?: Callback<Marker>): void

取消监听标记开始拖拽事件。支持传递多个callback异步回调。

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

'markerDragStart'：监听标记开始拖拽事件。

callback

Callback<[Marker](Marker.md)>

否

回调函数，返回[Marker](Marker.md)，取消监听标记开始拖拽事件。

- callback为空：取消所有callback回调。
- callback非空：取消指定的callback回调。

**示例：**

```ets
let callback1 = (marker: map.Marker) => {
  console.info("markerDragStart", `callback1 marker`);
};
let callback2 = (marker: map.Marker) => {
  console.info("markerDragStart", `callback2 marker`);
};
let callback3 = (marker: map.Marker) => {
  console.info("markerDragStart", `callback3 marker`);
};
mapEventManager.on("markerDragStart", callback1);
mapEventManager.on("markerDragStart", callback2);
mapEventManager.on("markerDragStart", callback3);

// 只取消callback1对象的事件响应，当markerDragStart事件发生时，callback2和callback3会正常被调用
mapEventManager.off('markerDragStart', callback1);
// 取消全部markerDragStart事件响应
mapEventManager.off('markerDragStart');
```

#### on('markerDrag')

on(type: 'markerDrag', callback: Callback<Marker>): void

监听标记拖拽事件。支持传递多个callback异步回调。

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

'markerDrag'：监听标记拖拽事件。

callback

Callback<[Marker](Marker.md)>

是

回调函数，返回[Marker](Marker.md)，监听标记拖拽事件。

**示例：**

```ets
let callback1 = (marker: map.Marker) => {
  console.info("markerDrag", `callback1 marker = ${marker.getId()}`);
};
let callback2 = (marker: map.Marker) => {
  console.info("markerDrag", `callback2 marker = ${marker.getId()}`);
};
let callback3 = (marker: map.Marker) => {
  console.info("markerDrag", `callback3 marker = ${marker.getId()}`);
};
mapEventManager.on("markerDrag", callback1);
mapEventManager.on("markerDrag", callback2);
mapEventManager.on("markerDrag", callback3);
```

#### off('markerDrag')

off(type: 'markerDrag', callback?: Callback<Marker>): void

取消监听标记拖拽事件。支持传递多个callback异步回调。

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

'markerDrag'：监听标记拖拽事件。

callback

Callback<[Marker](Marker.md)>

否

回调函数，返回[Marker](Marker.md)，取消监听标记拖拽事件。

- callback为空：取消所有callback回调。
- callback非空：取消指定的callback回调。

**示例：**

```ets
let callback1 = (marker: map.Marker) => {
  console.info("markerDrag", `callback1 marker`);
};
let callback2 = (marker: map.Marker) => {
  console.info("markerDrag", `callback2 marker`);
};
let callback3 = (marker: map.Marker) => {
  console.info("markerDrag", `callback3 marker`);
};
mapEventManager.on("markerDrag", callback1);
mapEventManager.on("markerDrag", callback2);
mapEventManager.on("markerDrag", callback3);

// 只取消callback1对象的事件响应，当markerDrag事件发生时，callback2和callback3会正常被调用
mapEventManager.off('markerDrag', callback1);
// 取消全部markerDrag事件响应
mapEventManager.off('markerDrag');
```

#### on('markerDragEnd')

on(type: 'markerDragEnd', callback: Callback<Marker>): void

监听标记拖拽结束事件。支持传递多个callback异步回调。

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

'markerDragEnd'：监听标记拖拽结束事件。

callback

Callback<[Marker](Marker.md)>

是

回调函数，返回[Marker](Marker.md)，监听标记拖拽结束事件。

**示例：**

```ets
let callback1 = (marker: map.Marker) => {
  console.info("markerDragEnd", `callback1 marker = ${marker.getId()}`);
};
let callback2 = (marker: map.Marker) => {
  console.info("markerDragEnd", `callback2 marker = ${marker.getId()}`);
};
let callback3 = (marker: map.Marker) => {
  console.info("markerDragEnd", `callback3 marker = ${marker.getId()}`);
};
mapEventManager.on("markerDragEnd", callback1);
mapEventManager.on("markerDragEnd", callback2);
mapEventManager.on("markerDragEnd", callback3);
```

#### off('markerDragEnd')

off(type: 'markerDragEnd', callback?: Callback<Marker>): void

取消监听标记拖动结束事件。支持传递多个callback异步回调。

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

'markerDragEnd'：监听标记拖动结束事件。

callback

Callback<[Marker](Marker.md)>

否

回调函数，返回[Marker](Marker.md)，取消监听标记拖拽结束事件。

- callback为空：取消所有callback回调。
- callback非空：取消指定的callback回调。

**示例：**

```ets
let callback1 = (marker: map.Marker) => {
  console.info("markerDragEnd", `callback1 marker`);
};
let callback2 = (marker: map.Marker) => {
  console.info("markerDragEnd", `callback2 marker`);
};
let callback3 = (marker: map.Marker) => {
  console.info("markerDragEnd", `callback3 marker`);
};
mapEventManager.on("markerDragEnd", callback1);
mapEventManager.on("markerDragEnd", callback2);
mapEventManager.on("markerDragEnd", callback3);

// 只取消callback1对象的事件响应，当markerDragEnd事件发生时，callback2和callback3会正常被调用
mapEventManager.off('markerDragEnd', callback1);
// 取消全部markerDragEnd事件响应
mapEventManager.off('markerDragEnd');
```

#### on('circleClick')

on(type: 'circleClick', callback: Callback<MapCircle>): void

监听圆点击事件。支持传递多个callback异步回调。

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

'circleClick'：监听圆点击事件。

callback

Callback<[MapCircle](MapCircle.md)>

是

回调函数，返回[MapCircle](MapCircle.md)，监听圆点击事件。

**示例：**

```ets
let callback1 = (circle: map.MapCircle) => {
  console.info("circleClick", `callback1 circle = ${circle.getId()}`);
};
let callback2 = (circle: map.MapCircle) => {
  console.info("circleClick", `callback2 circle = ${circle.getId()}`);
};
let callback3 = (circle: map.MapCircle) => {
  console.info("circleClick", `callback3 circle = ${circle.getId()}`);
};
mapEventManager.on("circleClick", callback1);
mapEventManager.on("circleClick", callback2);
mapEventManager.on("circleClick", callback3);
```

#### off('circleClick')

off(type: 'circleClick', callback?: Callback<MapCircle>): void

取消监听圆点击事件。支持传递多个callback异步回调。

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

'circleClick'：监听圆点击事件。

callback

Callback<[MapCircle](MapCircle.md)>

否

回调函数，返回[MapCircle](MapCircle.md)，取消监听圆点击事件。

- callback为空：取消所有callback回调。
- callback非空：取消指定的callback回调。

**示例：**

```ets
let callback1 = (circle: map.MapCircle) => {
  console.info("circleClick", `callback1 circle`);
};
let callback2 = (circle: map.MapCircle) => {
  console.info("circleClick", `callback2 circle`);
};
let callback3 = (circle: map.MapCircle) => {
  console.info("circleClick", `callback3 circle`);
};
mapEventManager.on("circleClick", callback1);
mapEventManager.on("circleClick", callback2);
mapEventManager.on("circleClick", callback3);

// 只取消callback1对象的事件响应，当circleClick事件发生时，callback2和callback3会正常被调用
mapEventManager.off('circleClick', callback1);
// 取消全部circleClick事件响应
mapEventManager.off('circleClick');
```

#### on('polylineClick')

on(type: 'polylineClick', callback: Callback<MapPolyline>): void

监听折线点击事件。支持传递多个callback异步回调。

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

'polylineClick'：监听折线点击事件。

callback

Callback<[MapPolyline](MapPolyline.md)>

是

回调函数，返回[MapPolyline](MapPolyline.md)，监听折线点击事件。

**示例：**

```ets
let callback1 = (polyline: map.MapPolyline) => {
  console.info("polylineClick", `callback1 polyline = ${polyline.getId()}`);
};
let callback2 = (polyline: map.MapPolyline) => {
  console.info("polylineClick", `callback2 polyline = ${polyline.getId()}`);
};
let callback3 = (polyline: map.MapPolyline) => {
  console.info("polylineClick", `callback3 polyline = ${polyline.getId()}`);
};
mapEventManager.on("polylineClick", callback1);
mapEventManager.on("polylineClick", callback2);
mapEventManager.on("polylineClick", callback3);
```

#### off('polylineClick')

off(type: 'polylineClick', callback?: Callback<MapPolyline>): void

取消监听折线点击事件。支持传递多个callback异步回调。

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

'polylineClick'：监听折线点击事件。

callback

Callback<[MapPolyline](MapPolyline.md)>

否

回调函数，返回[MapPolyline](MapPolyline.md)，取消监听折线点击事件。

- callback为空：取消所有callback回调。
- callback非空：取消指定的callback回调。

**示例：**

```ets
let callback1 = (polyline: map.MapPolyline) => {
  console.info("polylineClick", `callback1 polyline`);
};
let callback2 = (polyline: map.MapPolyline) => {
  console.info("polylineClick", `callback2 polyline`);
};
let callback3 = (polyline: map.MapPolyline) => {
  console.info("polylineClick", `callback3 polyline`);
};
mapEventManager.on("polylineClick", callback1);
mapEventManager.on("polylineClick", callback2);
mapEventManager.on("polylineClick", callback3);

// 只取消callback1对象的事件响应，当polylineClick事件发生时，callback2和callback3会正常被调用
mapEventManager.off('polylineClick', callback1);
// 取消全部polylineClick事件响应
mapEventManager.off('polylineClick');
```

#### on('polygonClick')

on(type: 'polygonClick', callback: Callback<MapPolygon>): void

监听多边形点击事件。支持传递多个callback异步回调。

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

'polygonClick'：监听多边形点击事件。

callback

Callback<[MapPolygon](MapPolygon.md)>

是

回调函数，返回[MapPolygon](MapPolygon.md)，监听多边形点击事件。

**示例：**

```ets
let callback1 = (polygon: map.MapPolygon) => {
  console.info("polygonClick", `callback1 polygon = ${polygon.getId()}`);
};
let callback2 = (polygon: map.MapPolygon) => {
  console.info("polygonClick", `callback2 polygon = ${polygon.getId()}`);
};
let callback3 = (polygon: map.MapPolygon) => {
  console.info("polygonClick", `callback3 polygon = ${polygon.getId()}`);
};
mapEventManager.on("polygonClick", callback1);
mapEventManager.on("polygonClick", callback2);
mapEventManager.on("polygonClick", callback3);
```

#### off('polygonClick')

off(type: 'polygonClick', callback?: Callback<MapPolygon>): void

取消监听多边形点击事件。支持传递多个callback异步回调。

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

'polygonClick'：监听多边形点击事件。

callback

Callback<[MapPolygon](MapPolygon.md)>

否

回调函数，返回[MapPolygon](MapPolygon.md)，取消监听多边形点击事件。

- callback为空：取消所有callback回调。
- callback非空：取消指定的callback回调。

**示例：**

```ets
let callback1 = (polygon: map.MapPolygon) => {
  console.info("polygonClick", `callback1 polygon`);
};
let callback2 = (polygon: map.MapPolygon) => {
  console.info("polygonClick", `callback2 polygon`);
};
let callback3 = (polygon: map.MapPolygon) => {
  console.info("polygonClick", `callback3 polygon`);
};
mapEventManager.on("polygonClick", callback1);
mapEventManager.on("polygonClick", callback2);
mapEventManager.on("polygonClick", callback3);

// 只取消callback1对象的事件响应，当polygonClick事件发生时，callback2和callback3会正常被调用
mapEventManager.off('polygonClick', callback1);
// 取消全部polygonClick事件响应
mapEventManager.off('polygonClick');
```

#### on('infoWindowClick')

on(type: 'infoWindowClick', callback: Callback<Marker>): void

监听信息窗点击事件。支持传递多个callback异步回调。

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

'infoWindowClick'：监听信息窗点击事件。

callback

Callback<[Marker](Marker.md)>

是

回调函数，返回[Marker](Marker.md)，监听信息窗点击事件。

**示例：**

```ets
let callback1 = (infoWindow: map.Marker) => {
  console.info("infoWindowClick", `callback1 infoWindow = ${infoWindow.getId()}`);
};
let callback2 = (infoWindow: map.Marker) => {
  console.info("infoWindowClick", `callback2 infoWindow = ${infoWindow.getId()}`);
};
let callback3 = (infoWindow: map.Marker) => {
  console.info("infoWindowClick", `callback3 infoWindow = ${infoWindow.getId()}`);
};
mapEventManager.on("infoWindowClick", callback1);
mapEventManager.on("infoWindowClick", callback2);
mapEventManager.on("infoWindowClick", callback3);
```

#### off('infoWindowClick')

off(type: 'infoWindowClick', callback?: Callback<[Marker](Marker.md)>): void

取消监听信息窗点击事件。支持传递多个callback异步回调。

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

'infoWindowClick'：监听信息窗点击事件。

callback

Callback<[Marker](Marker.md)>

否

回调函数，返回[Marker](Marker.md)，取消监听信息窗点击事件。

- callback为空：取消所有callback回调。
- callback非空：取消指定的callback回调。

**示例：**

```ets
let callback1 = (infoWindow: map.Marker) => {
  console.info("infoWindowClick", `callback1 infoWindow`);
};
let callback2 = (infoWindow: map.Marker) => {
  console.info("infoWindowClick", `callback2 infoWindow`);
};
let callback3 = (infoWindow: map.Marker) => {
  console.info("infoWindowClick", `callback3 infoWindow`);
};
mapEventManager.on("infoWindowClick", callback1);
mapEventManager.on("infoWindowClick", callback2);
mapEventManager.on("infoWindowClick", callback3);

// 只取消callback1对象的事件响应，当infoWindowClick事件发生时，callback2和callback3会正常被调用
mapEventManager.off('infoWindowClick', callback1);
// 取消全部infoWindowClick事件响应
mapEventManager.off('infoWindowClick');
```

#### on('infoWindowClose')

on(type: 'infoWindowClose', callback: Callback<Marker>): void

监听信息窗关闭事件。支持传递多个callback异步回调。

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

'infoWindowClose'：监听信息窗关闭事件。

callback

Callback<[Marker](Marker.md)>

是

回调函数，返回[Marker](Marker.md)，监听信息窗关闭事件。

**示例：**

```ets
let callback1 = (infoWindow: map.Marker) => {
  console.info("infoWindowClose", `callback1 infoWindowClose = ${infoWindow.getId()}`);
};
let callback2 = (infoWindow: map.Marker) => {
  console.info("infoWindowClose", `callback2 infoWindowClose = ${infoWindow.getId()}`);
};
let callback3 = (infoWindow: map.Marker) => {
  console.info("infoWindowClose", `callback3 infoWindowClose = ${infoWindow.getId()}`);
};
mapEventManager.on("infoWindowClose", callback1);
mapEventManager.on("infoWindowClose", callback2);
mapEventManager.on("infoWindowClose", callback3);
```

#### off('infoWindowClose')

off(type: 'infoWindowClose', callback?: Callback<Marker>): void

取消监听信息窗关闭事件。支持传递多个callback异步回调。

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

'infoWindowClose'：监听信息窗关闭事件。

callback

Callback<[Marker](Marker.md)>

否

回调函数，返回[Marker](Marker.md)，取消监听信息窗关闭事件。

- callback为空：取消所有callback回调。
- callback非空：取消指定的callback回调。

**示例：**

```ets
let callback1 = (infoWindow: map.Marker) => {
  console.info("infoWindowClose", `callback1 infoWindowClose`);
};
let callback2 = (infoWindow: map.Marker) => {
  console.info("infoWindowClose", `callback2 infoWindowClose`);
};
let callback3 = (infoWindow: map.Marker) => {
  console.info("infoWindowClose", `callback3 infoWindowClose`);
};
mapEventManager.on("infoWindowClose", callback1);
mapEventManager.on("infoWindowClose", callback2);
mapEventManager.on("infoWindowClose", callback3);

// 只取消callback1对象的事件响应，当infoWindowClose事件发生时，callback2和callback3会正常被调用
mapEventManager.off('infoWindowClose', callback1);
// 取消全部infoWindowClose事件响应
mapEventManager.off('infoWindowClose');
```

#### on('pointAnnotationClick')

on(type: 'pointAnnotationClick', callback: Callback<PointAnnotation>): void

监听点注释点击事件。支持传递多个callback异步回调。

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

'pointAnnotationClick'：监听点注释点击事件。

callback

Callback<[PointAnnotation](PointAnnotation.md)>

是

回调函数，返回[PointAnnotation](PointAnnotation.md)，监听点注释点击事件。

**示例：**

```ets
let callback1 = (pointAnnotation: map.PointAnnotation) => {
  console.info("pointAnnotationClick", `callback1 pointAnnotation = ${pointAnnotation.getId()}`);
};
let callback2 = (pointAnnotation: map.PointAnnotation) => {
  console.info("pointAnnotationClick", `callback2 pointAnnotation = ${pointAnnotation.getId()}`);
};
let callback3 = (pointAnnotation: map.PointAnnotation) => {
  console.info("pointAnnotationClick", `callback3 pointAnnotation = ${pointAnnotation.getId()}`);
};
mapEventManager.on("pointAnnotationClick", callback1);
mapEventManager.on("pointAnnotationClick", callback2);
mapEventManager.on("pointAnnotationClick", callback3);
```

#### off('pointAnnotationClick')

off(type: 'pointAnnotationClick', callback?: Callback<PointAnnotation>): void

取消监听点注释点击事件。支持传递多个callback异步回调。

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

'pointAnnotationClick'：监听点注释点击事件。

callback

Callback<[PointAnnotation](PointAnnotation.md)>

否

回调函数，返回[PointAnnotation](PointAnnotation.md)，取消监听点注释点击事件。

- callback为空：取消所有callback回调。
- callback非空：取消指定的callback回调。

**示例：**

```ets
let callback1 = (pointAnnotation: map.PointAnnotation) => {
  console.info("pointAnnotationClick", `callback1 pointAnnotation`);
};
let callback2 = (pointAnnotation: map.PointAnnotation) => {
  console.info("pointAnnotationClick", `callback2 pointAnnotation`);
};
let callback3 = (pointAnnotation: map.PointAnnotation) => {
  console.info("pointAnnotationClick", `callback3 pointAnnotation`);
};
mapEventManager.on("pointAnnotationClick", callback1);
mapEventManager.on("pointAnnotationClick", callback2);
mapEventManager.on("pointAnnotationClick", callback3);

// 只取消callback1对象的事件响应，当pointAnnotationClick事件发生时，callback2和callback3会正常被调用
mapEventManager.off('pointAnnotationClick', callback1);
// 取消全部pointAnnotationClick事件响应
mapEventManager.off('pointAnnotationClick');
```

#### on('bubbleClick')

on(type: 'bubbleClick', callback: Callback<Bubble>): void

监听气泡点击事件。支持传递多个callback异步回调。

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

'bubbleClick'：监听气泡点击事件。

callback

Callback<[Bubble](Bubble.md)>

是

回调函数，返回[Bubble](Bubble.md)，监听气泡点击事件。

**示例：**

```ets
let callback1 = (bubble: map.Bubble) => {
  console.info("bubbleClick", `callback1 bubble = ${bubble.getId()}`);
};
let callback2 = (bubble: map.Bubble) => {
  console.info("bubbleClick", `callback2 bubble = ${bubble.getId()}`);
};
let callback3 = (bubble: map.Bubble) => {
  console.info("bubbleClick", `callback3 bubble = ${bubble.getId()}`);
};
mapEventManager.on("bubbleClick", callback1);
mapEventManager.on("bubbleClick", callback2);
mapEventManager.on("bubbleClick", callback3);
```

#### off('bubbleClick')

off(type: 'bubbleClick', callback?: Callback<Bubble>): void

取消监听气泡点击事件。支持传递多个callback异步回调。

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

'bubbleClick'：监听气泡点击事件。

callback

Callback<[Bubble](Bubble.md)>

否

回调函数，返回[Bubble](Bubble.md)，取消监听气泡点击事件。

- callback为空：取消所有callback回调。
- callback非空：取消指定的callback回调。

**示例：**

```ets
let callback1 = (bubble: map.Bubble) => {
  console.info("bubbleClick", `callback1 bubble`);
};
let callback2 = (bubble: map.Bubble) => {
  console.info("bubbleClick", `callback2 bubble`);
};
let callback3 = (bubble: map.Bubble) => {
  console.info("bubbleClick", `callback3 bubble`);
};
mapEventManager.on("bubbleClick", callback1);
mapEventManager.on("bubbleClick", callback2);
mapEventManager.on("bubbleClick", callback3);

// 只取消callback1对象的事件响应，当bubbleClick事件发生时，callback2和callback3会正常被调用
mapEventManager.off('bubbleClick', callback1);
// 取消全部bubbleClick事件响应
mapEventManager.off('bubbleClick');
```

#### on('imageOverlayClick')

on(type: 'imageOverlayClick', callback: Callback<ImageOverlay>): void

监听覆盖物点击事件。支持传递多个callback异步回调。

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

'imageOverlayClick'：监听覆盖物点击事件。

callback

Callback<[ImageOverlay](ImageOverlay.md)>

是

回调函数，返回[ImageOverlay](ImageOverlay.md)，监听覆盖物点击事件。

**示例：**

```ets
let callback1 = (imageOverlay: map.ImageOverlay) => {
  console.info("imageOverlayClick", `callback1 imageOverlay = ${imageOverlay.getId()}`);
};
let callback2 = (imageOverlay: map.ImageOverlay) => {
  console.info("imageOverlayClick", `callback2 imageOverlay = ${imageOverlay.getId()}`);
};
let callback3 = (imageOverlay: map.ImageOverlay) => {
  console.info("imageOverlayClick", `callback3 imageOverlay = ${imageOverlay.getId()}`);
};
mapEventManager.on("imageOverlayClick", callback1);
mapEventManager.on("imageOverlayClick", callback2);
mapEventManager.on("imageOverlayClick", callback3);
```

#### off('imageOverlayClick')

off(type: 'imageOverlayClick', callback?: Callback<ImageOverlay>): void

取消监听覆盖物点击事件。支持传递多个callback异步回调。

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

'imageOverlayClick'：监听覆盖物点击事件。

callback

Callback<[ImageOverlay](ImageOverlay.md)>

否

回调函数，返回[ImageOverlay](ImageOverlay.md)，取消监听覆盖物点击事件。

- callback为空：取消所有callback回调。
- callback非空：取消指定的callback回调。

**示例：**

```ets
let callback1 = (imageOverlay: map.ImageOverlay) => {
  console.info("imageOverlayClick", `callback1 imageOverlay`);
};
let callback2 = (imageOverlay: map.ImageOverlay) => {
  console.info("imageOverlayClick", `callback2 imageOverlay`);
};
let callback3 = (imageOverlay: map.ImageOverlay) => {
  console.info("imageOverlayClick", `callback3 imageOverlay`);
};
mapEventManager.on("imageOverlayClick", callback1);
mapEventManager.on("imageOverlayClick", callback2);
mapEventManager.on("imageOverlayClick", callback3);

// 只取消callback1对象的事件响应，当imageOverlayClick事件发生时，callback2和callback3会正常被调用
mapEventManager.off('imageOverlayClick', callback1);
// 取消全部imageOverlayClick事件响应
mapEventManager.off('imageOverlayClick');
```

#### on('error')

on(type: 'error', callback: ErrorCallback): void

监听异常事件。支持传递多个callback异步回调。

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

'error'：监听异常事件。

callback

[ErrorCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-base#errorcallback)

是

回调函数，返回[ErrorCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-base#errorcallback)，监听异常事件。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let callback1 = (error: BusinessError) => {
  console.error("error", `callback1 code: ${error.code}, message: ${error.message}`);
};
let callback2 = (error: BusinessError) => {
  console.error("error", `callback2 code: ${error.code}, message: ${error.message}`);
};
let callback3 = (error: BusinessError) => {
  console.error("error", `callback3 code: ${error.code}, message: ${error.message}`);
};
mapEventManager.on("error", callback1);
mapEventManager.on("error", callback2);
mapEventManager.on("error", callback3);
```

#### off('error')

off(type: 'error', callback?: ErrorCallback): void

取消监听异常事件。支持传递多个callback异步回调。

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

'error'：监听异常事件。

callback

[ErrorCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-base#errorcallback)

否

回调函数，返回[ErrorCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-base#errorcallback)，取消监听异常事件。

- callback为空：取消所有callback回调。
- callback非空：取消指定的callback回调。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let callback1 = (error: BusinessError) => {
  console.info("error", `callback1`);
};
let callback2 = (error: BusinessError) => {
  console.info("error", `callback2`);
};
let callback3 = (error: BusinessError) => {
  console.info("error", `callback3`);
};
mapEventManager.on("error", callback1);
mapEventManager.on("error", callback2);
mapEventManager.on("error", callback3);

// 只取消callback1对象的事件响应，当error事件发生时，callback2和callback3会正常被调用
mapEventManager.off('error', callback1);
// 取消全部error事件响应
mapEventManager.off('error');
```

#### on('indoorMapEnter')

on(type: 'indoorMapEnter', callback: Callback<IndoorMapInfo>): void

监听室内图进入事件。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.1.1(19)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**设备行为差异：**在API19及之后版本该接口在phone、tablet、2in1均可正常使用，在其他设备中返回801错误。

**起始版本：**5.1.1(19)

**参数：**

**参数名**

**类型**

必填

**说明**

type

string

是

'indoorMapEnter'：监听室内图进入事件。

callback

Callback<[IndoorMapInfo](IndoorMapInfo.md)>

是

回调函数，返回[IndoorMapInfo](IndoorMapInfo.md)，监听室内图进入事件。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

错误码ID

错误信息

801

Capability not supported. Failed to call the API due to limited device capabilities.

**示例：**

```ets
let callback = (indoorMapInfo: map.IndoorMapInfo) => {
  console.info("indoorMapEnter", `callback indoorMapInfo`);
};
mapEventManager.on("indoorMapEnter", callback);
```

#### off('indoorMapEnter')

off(type: 'indoorMapEnter', callback?: Callback<IndoorMapInfo>): void

取消监听室内图进入事件。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.1.1(19)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**设备行为差异：**在API19及之后版本该接口在phone、tablet、2in1均可正常使用，在其他设备中返回801错误。

**起始版本：**5.1.1(19)

**参数：**

**参数名**

**类型**

必填

**说明**

type

string

是

'indoorMapEnter'：监听室内图进入事件。

callback

Callback<[IndoorMapInfo](IndoorMapInfo.md)>

否

回调函数，返回[IndoorMapInfo](IndoorMapInfo.md)，取消监听室内图进入事件。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

错误码ID

错误信息

801

Capability not supported. Failed to call the API due to limited device capabilities.

**示例：**

```ets
let callback = (indoorMapInfo: map.IndoorMapInfo) => {
  console.info("indoorMapEnter", `callback`);
};
mapEventManager.on("indoorMapEnter", callback);

// 取消callback对象的事件响应
mapEventManager.off('indoorMapEnter', callback);
```

#### on('indoorMapExit')

on(type: 'indoorMapExit', callback: Callback<void>): void

监听室内图退出事件。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.1.1(19)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**设备行为差异：**在API19及之后版本该接口在phone、tablet、2in1均可正常使用，在其他设备中返回801错误。

**起始版本：**5.1.1(19)

**参数：**

**参数名**

**类型**

必填

**说明**

type

string

是

'indoorMapExit'：监听室内图退出事件。

callback

Callback<void>

是

回调函数，无返回结果的回调函数，监听室内图退出事件。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

错误码ID

错误信息

801

Capability not supported. Failed to call the API due to limited device capabilities.

**示例：**

```ets
let callback = () => {
  console.info("indoorMapExit", `callback`);
};
mapEventManager.on("indoorMapExit", callback);
```

#### off('indoorMapExit')

off(type: 'indoorMapExit', callback?: Callback<void>): void

取消监听室内图退出事件。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.1.1(19)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**设备行为差异：**在API19及之后版本该接口在phone、tablet、2in1均可正常使用，在其他设备中返回801错误。

**起始版本：**5.1.1(19)

**参数：**

**参数名**

**类型**

必填

**说明**

type

string

是

'indoorMapExit'：监听室内图退出事件。

callback

Callback<void>

否

回调函数，无返回结果的回调函数，取消监听室内图退出事件。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

错误码ID

错误信息

801

Capability not supported. Failed to call the API due to limited device capabilities.

**示例：**

```ets
let callback = () => {
  console.info("indoorMapExit", `callback`);
};
mapEventManager.on("indoorMapExit", callback);

// 取消callback对象的事件响应
mapEventManager.off('indoorMapExit', callback);
```

#### on('massPointOverlayClick')

on(type: 'massPointOverlayClick', callback: MassPointOverlayCallback): void

监听海量点图层点击事件。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**6.0.0(20)

**参数：**

**参数名**

**类型**

必填

**说明**

type

string

是

'massPointOverlayClick'：监听海量点图层点击事件。

callback

[MassPointOverlayCallback](MassPointOverlayCallback.md)

是

回调函数，无返回结果的回调函数，监听海量点图层点击事件。

**示例：**

```ets
// 初始化地图组件的监听事件管理接口
let mapEventManager = this.mapController.getEventManager();
let massCallback: map.MassPointOverlayCallback = (overlay, item) => {
  console.info(`overlayId:${overlay.getId()},item :${JSON.stringify(item)}`);
}
// 启动海量点点击事件监听
mapEventManager.on('massPointOverlayClick', massCallback);
```

#### off('massPointOverlayClick')

off(type: 'massPointOverlayClick', callback?: MassPointOverlayCallback): void

取消监听海量点图层点击事件。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**6.0.0(20)

**参数：**

**参数名**

**类型**

必填

**说明**

type

string

是

'massPointOverlayClick'：监听海量点图层点击退出事件。

callback

[MassPointOverlayCallback](MassPointOverlayCallback.md)

否

回调函数，无返回结果的回调函数，取消监听海量点图层点击事件。

- callback为空：取消所有callback回调。
- callback非空：取消指定的callback回调。

**示例：**

```ets
// 初始化地图组件的监听事件管理接口
let mapEventManager = this.mapController.getEventManager();
let massCallback: map.MassPointOverlayCallback = (overlay, item) => {
  console.info(`overlayId:${overlay.getId()},item :${JSON.stringify(item)}`);
}
// 启动海量点点击事件监听
mapEventManager.on('massPointOverlayClick', massCallback);
// 停止海量点点击事件监听,传入指定callback
mapEventManager.off('massPointOverlayClick', massCallback);
// 停止所有海量点点击事件监听，无需传入callback
mapEventManager.off('massPointOverlayClick');
```