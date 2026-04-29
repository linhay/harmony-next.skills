# navi（路径规划）

本模块提供路径规划功能。

**起始版本：**4.1.0(11)

#### 导入模块

```ets
import { navi } from '@kit.MapKit';
```

#### getDrivingRoutes

getDrivingRoutes(params: DrivingRouteParams): Promise<RouteResult>

规划两个地点之间的驾车路线。使用Promise异步回调。


-

- 每次调用最多可以返回3条路径。

-

- 最多可以指定5个途经点。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| params | DrivingRouteParams | 是 | 驾车路径规划的参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<RouteResult> | Promise对象，返回RouteResult。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码]([ArkTS API错误码](../../errors/ArkTS API错误码.md).md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. |
| 1002600001 | System internal error. |
| 1002600002 | Failed to connect to the Map Kit server. |
| 1002600003 | App authentication failed. |
| 1002600004 | The Map permission is not enabled. |
| 1002600006 | The API call times exceed the quota. |
| 1002600007 | The API QPS exceeds the quota. |
| 1002600008 | The API is in arrears. |
| 1002600009 | The API has not subscribed to any pay-as-you-go package. |
| 1002600010 | The server is busy. Please wait and try again. |
| 1002600011 | Server error. |
| 1002600999 | Unknown error. |
| 1002602001 | The start and end points do not have home countries, or a service error occurred. |
| 1002602002 | Cross-region route planning is not supported. |
| 1002602003 | The number of start points or end points exceed 100. |
| 1002602004 | The linear distance between the start point and end point exceeds the upper limit. |
| 1002602005 | The start point, end point, or waypoint does not support navigation. |
| 1002602006 | The request point is mapped to the same point on the road. |

**示例：**

```ets
let params: navi.DrivingRouteParams = {
  origins: [{
    "latitude": 31.9821213545843,
    "longitude": 120.27745557768591
  }],
  destination: {
    "latitude": 31.983545843,
    "longitude": 120.27745557768591
  },
  waypoints: [
    { "latitude": 31.967236140819114, "longitude": 120.27142088866847 },
    { "latitude": 31.972868002238872, "longitude": 120.2943211817165 },
    { "latitude": 31.98469327973332, "longitude": 120.29101107384068 }
  ],
  language: "zh_CN"
};
const result = await navi.getDrivingRoutes(params);
console.info("Succeeded in getting driving routes.");
```

#### getDrivingRoutes

getDrivingRoutes(context: common.Context, params: DrivingRouteParams): Promise<RouteResult>

规划两个地点之间的驾车路线，支持传入Context上下文。使用Promise异步回调。


-

- 每次调用最多可以返回3条路径。

-

- 最多可以指定5个途经点。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | common.Context | 是 | Context上下文。 |
| params | DrivingRouteParams | 是 | 驾车路径规划的参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<RouteResult> | Promise对象，返回RouteResult。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. |
| 1002600001 | System internal error. |
| 1002600002 | Failed to connect to the Map Kit server. |
| 1002600003 | App authentication failed. |
| 1002600004 | The Map permission is not enabled. |
| 1002600006 | The API call times exceed the quota. |
| 1002600007 | The API QPS exceeds the quota. |
| 1002600008 | The API is in arrears. |
| 1002600009 | The API has not subscribed to any pay-as-you-go package. |
| 1002600010 | The server is busy. Please wait and try again. |
| 1002600011 | Server error. |
| 1002600999 | Unknown error. |
| 1002602001 | The start and end points do not have home countries, or a service error occurred. |
| 1002602002 | Cross-region route planning is not supported. |
| 1002602003 | The number of start points or end points exceed 100. |
| 1002602004 | The linear distance between the start point and end point exceeds the upper limit. |
| 1002602005 | The start point, end point, or waypoint does not support navigation. |
| 1002602006 | The request point is mapped to the same point on the road. |

**示例：**

```ets
let params: navi.DrivingRouteParams = {
  origins: [{
    "latitude": 31.982129213545843,
    "longitude": 120.27745557768591
  }],
  destination: {
    "latitude": 31.9821213545843,
    "longitude": 120.277557768591
  },
  waypoints: [
    { "latitude": 31.967236140819114, "longitude": 120.27142088866847 },
    { "latitude": 31.972868002238872, "longitude": 120.2943211817165 },
    { "latitude": 31.98469327973332, "longitude": 120.29101107384068 }
  ],
  language: "zh_CN"
};
const result = await navi.getDrivingRoutes(this.getUIContext().getHostContext(), params);
console.info("Succeeded in getting driving routes.");
```

#### getWalkingRoutes

getWalkingRoutes(params: RouteParams): Promise<RouteResult>

规划两个地点之间的步行路线。使用Promise异步回调。

只能规划直线距离150公里内的两个地点步行路线。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| params | RouteParams | 是 | 步行路径规划的参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<RouteResult> | Promise对象，返回RouteResult。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. |
| 1002600001 | System internal error. |
| 1002600002 | Failed to connect to the Map Kit server. |
| 1002600003 | App authentication failed. |
| 1002600004 | The Map permission is not enabled. |
| 1002600006 | The API call times exceed the quota. |
| 1002600007 | The API QPS exceeds the quota. |
| 1002600008 | The API is in arrears. |
| 1002600009 | The API has not subscribed to any pay-as-you-go package. |
| 1002600010 | The server is busy. Please wait and try again. |
| 1002600011 | Server error. |
| 1002600999 | Unknown error. |
| 1002602001 | The start and end points do not have home countries, or a service error occurred. |
| 1002602002 | Cross-region route planning is not supported. |
| 1002602003 | The number of start points or end points exceed 100. |
| 1002602004 | The linear distance between the start point and end point exceeds the upper limit. |
| 1002602005 | The start point, end point, or waypoint does not support navigation. |
| 1002602006 | The request point is mapped to the same point on the road. |

**示例：**

```ets
let params: navi.RouteParams = {
  origins: [
    { "latitude": 39.992281, "longitude": 116.31088 },
    { "latitude": 39.996, "longitude": 116.311 }
  ],
  destination: {
    "latitude": 39.94,
    "longitude": 116.311
  },
  language: "zh_CN"
};
const result = await navi.getWalkingRoutes(params);
console.info("Succeeded in getting walking routes.");
```

#### getWalkingRoutes

getWalkingRoutes(context: common.Context, params: RouteParams): Promise<RouteResult>

规划两个地点之间的步行路线，支持传入Context上下文。使用Promise异步回调。

只能在直线距离150公里内规划步行路线。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | common.Context | 是 | Context上下文。 |
| params | RouteParams | 是 | 步行路径规划的参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<RouteResult> | Promise对象，返回RouteResult。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. |
| 1002600001 | System internal error. |
| 1002600002 | Failed to connect to the Map Kit server. |
| 1002600003 | App authentication failed. |
| 1002600004 | The Map permission is not enabled. |
| 1002600006 | The API call times exceed the quota. |
| 1002600007 | The API QPS exceeds the quota. |
| 1002600008 | The API is in arrears. |
| 1002600009 | The API has not subscribed to any pay-as-you-go package. |
| 1002600010 | The server is busy. Please wait and try again. |
| 1002600011 | Server error. |
| 1002600999 | Unknown error. |
| 1002602001 | The start and end points do not have home countries, or a service error occurred. |
| 1002602002 | Cross-region route planning is not supported. |
| 1002602003 | The number of start points or end points exceed 100. |
| 1002602004 | The linear distance between the start point and end point exceeds the upper limit. |
| 1002602005 | The start point, end point, or waypoint does not support navigation. |
| 1002602006 | The request point is mapped to the same point on the road. |

**示例：**

```ets
let params: navi.DrivingRouteParams = {
  origins: [{
    "latitude": 31.982129213545843,
    "longitude": 120.27745557768591
  }],
  destination: {
    "latitude": 31.9821213545843,
    "longitude": 120.277557768591
  },
  waypoints: [
    { "latitude": 31.967236140819114, "longitude": 120.27142088866847 },
    { "latitude": 31.972868002238872, "longitude": 120.2943211817165 },
    { "latitude": 31.98469327973332, "longitude": 120.29101107384068 }
  ],
  language: "zh_CN"
};
const result = await navi.getWalkingRoutes(this.getUIContext().getHostContext(), params);
console.info("Succeeded in getting walking routes.");
```

#### getCyclingRoutes

getCyclingRoutes(params: RouteParams): Promise<RouteResult>

规划两个地点之间的骑行路线。使用Promise异步回调。

只能在直线距离500公里内规划骑行路线。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| params | RouteParams | 是 | 骑行路径规划的参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<RouteResult> | Promise对象，返回RouteResult。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. |
| 1002600001 | System internal error. |
| 1002600002 | Failed to connect to the Map Kit server. |
| 1002600003 | App authentication failed. |
| 1002600004 | The Map permission is not enabled. |
| 1002600006 | The API call times exceed the quota. |
| 1002600007 | The API QPS exceeds the quota. |
| 1002600008 | The API is in arrears. |
| 1002600009 | The API has not subscribed to any pay-as-you-go package. |
| 1002600010 | The server is busy. Please wait and try again. |
| 1002600011 | Server error. |
| 1002600999 | Unknown error. |
| 1002602001 | The start and end points do not have home countries, or a service error occurred. |
| 1002602002 | Cross-region route planning is not supported. |
| 1002602003 | The number of start points or end points exceed 100. |
| 1002602004 | The linear distance between the start point and end point exceeds the upper limit. |
| 1002602005 | The start point, end point, or waypoint does not support navigation. |
| 1002602006 | The request point is mapped to the same point on the road. |

**示例：**

```ets
let params: navi.RouteParams = {
  origins: [{
    latitude: 31.984410259206815,
    longitude: 118.76625379397866
  }],
  destination: {
    latitude: 30.9844259206815,
    longitude: 119.766259397866
  },
  language: "zh_CN"
};
const result = await navi.getCyclingRoutes(params);
console.info("Succeeded in getting cycling routes.");
```

#### getCyclingRoutes

getCyclingRoutes(context: common.Context, params: RouteParams): Promise<RouteResult>

规划两个地点之间的骑行路线，支持传入Context上下文。使用Promise异步回调。

只能在直线距离500公里内规划骑行路线。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | common.Context | 是 | Context上下文。 |
| params | RouteParams | 是 | 骑行路径规划的参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<RouteResult> | Promise对象，返回RouteResult。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. |
| 1002600001 | System internal error. |
| 1002600002 | Failed to connect to the Map Kit server. |
| 1002600003 | App authentication failed. |
| 1002600004 | The Map permission is not enabled. |
| 1002600006 | The API call times exceed the quota. |
| 1002600007 | The API QPS exceeds the quota. |
| 1002600008 | The API is in arrears. |
| 1002600009 | The API has not subscribed to any pay-as-you-go package. |
| 1002600010 | The server is busy. Please wait and try again. |
| 1002600011 | Server error. |
| 1002600999 | Unknown error. |
| 1002602001 | The start and end points do not have home countries, or a service error occurred. |
| 1002602002 | Cross-region route planning is not supported. |
| 1002602003 | The number of start points or end points exceed 100. |
| 1002602004 | The linear distance between the start point and end point exceeds the upper limit. |
| 1002602005 | The start point, end point, or waypoint does not support navigation. |
| 1002602006 | The request point is mapped to the same point on the road. |

**示例：**

```ets
let params: navi.RouteParams = {
  origins: [{
    latitude: 31.98441059206815,
    longitude: 118.76625379397866
  }],
  destination: {
    latitude: 30.984410259206815,
    longitude: 119.766259397866
  },
  language: "zh_CN"
};
const result = await navi.getCyclingRoutes(this.getUIContext().getHostContext(), params);
console.info("Succeeded in getting cycling routes.");
```

#### getTransitRoutes

getTransitRoutes(context: common.Context, params: TransitRouteParams): Promise<TransitRouteResult>

规划两地之间的中转路线，仅支持中国大陆。支持传入Context上下文，使用Promise异步回调。

非同城起点和终点的直线距离不超过100km，同城不限制距离。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.1.1(19)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**5.1.1(19)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | common.Context | 是 | Context上下文。 |
| params | TransitRouteParams | 是 | 中转路线规划的参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<TransitRouteResult> | Promise对象，返回TransitRouteResult。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1002600001 | System internal error. |
| 1002600002 | Failed to connect to the Map Kit server. |
| 1002600003 | App authentication failed. |
| 1002600004 | The Map permission is not enabled. |
| 1002600006 | The API call times exceed the quota. |
| 1002600007 | The API QPS exceeds the quota. |
| 1002600008 | The API is in arrears. |
| 1002600009 | The API has not subscribed to any pay-as-you-go package. |
| 1002600010 | The server is busy. Please wait and try again. |
| 1002600011 | Server error. |
| 1002600999 | Unknown error. |
| 1002602001 | The start and end points do not have home countries, or a service error occurred. |
| 1002602002 | Cross-region route planning is not supported. |
| 1002602004 | The linear distance between the start point and end point exceeds the upper limit. |
| 1002602005 | The start point, end point, or waypoint does not support navigation. |
| 1002602006 | The request point is mapped to the same point on the road. |

**示例：**

```ets
let params: navi.TransitRouteParams = {
  "origin": { "latitude": 39.921619, "longitude": 116.356587 },
  "destination": { "latitude": 39.94161, "longitude": 116.353621 },
  "departureTime": new Date().getTime() / 1000
};
const result = await navi.getTransitRoutes(this.getUIContext().getHostContext(), params);
console.info("Succeeded in getting transit routes.");
```

#### getDrivingMatrix

getDrivingMatrix(params: DrivingMatrixParams): Promise<MatrixResult>

规划多个地点之间的驾车路线。使用Promise异步回调。

该功能适用于高并发场景，例如网约车订单调度。在这种情况下，该功能可以计算多个起点和终点之间的路线，并找到网约车订单调度所需的起点和终点。


1.

只能在直线距离2000公里内规划驾车路线。

1.

起点的数量乘以终点的数量不能超过100。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| params | DrivingMatrixParams | 是 | 驾车批量算路的参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<MatrixResult> | Promise对象，返回MatrixResult。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. |
| 1002600001 | System internal error. |
| 1002600002 | Failed to connect to the Map Kit server. |
| 1002600003 | App authentication failed. |
| 1002600004 | The Map permission is not enabled. |
| 1002600006 | The API call times exceed the quota. |
| 1002600007 | The API QPS exceeds the quota. |
| 1002600008 | The API is in arrears. |
| 1002600009 | The API has not subscribed to any pay-as-you-go package. |
| 1002600010 | The server is busy. Please wait and try again. |
| 1002600011 | Server error. |
| 1002600999 | Unknown error. |
| 1002602001 | The start and end points do not have home countries, or a service error occurred. |
| 1002602002 | Cross-region route planning is not supported. |
| 1002602003 | The number of start points or end points exceed 100. |
| 1002602004 | The linear distance between the start point and end point exceeds the upper limit. |
| 1002602005 | The start point, end point, or waypoint does not support navigation. |
| 1002602006 | The request point is mapped to the same point on the road. |

**示例：**

```ets
let params: navi.DrivingMatrixParams = {
  "origins": [
    {
      latitude: 31.9844159206815,
      longitude: 118.76625379397866
    },
    {
      latitude: 31.184410259206815,
      longitude: 118.366379397866
    }
  ],
  "destinations": [{
    latitude: 30.98441259206815,
    longitude: 119.765379397866
  }],
  "trafficMode": 2,
  "language": "zh_CN"
};
const result = await navi.getDrivingMatrix(params);
console.info("Succeeded in getting driving matrix.");
```

#### getDrivingMatrix

getDrivingMatrix(context: common.Context, params: DrivingMatrixParams): Promise<MatrixResult>

规划多个地点之间的驾车路线，支持传入Context上下文。使用Promise异步回调。

该功能适用于高并发场景，例如网约车订单调度。在这种情况下，该功能可以计算多个起点和终点之间的路线，并找到网约车订单调度所需的起点和终点。


1.

只能在直线距离2000公里内规划驾车路线。

1.

起点的数量乘以终点的数量不能超过100。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | common.Context | 是 | Context上下文。 |
| params | DrivingMatrixParams | 是 | 驾车批量算路的参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<MatrixResult> | Promise对象，返回MatrixResult。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. |
| 1002600001 | System internal error. |
| 1002600002 | Failed to connect to the Map Kit server. |
| 1002600003 | App authentication failed. |
| 1002600004 | The Map permission is not enabled. |
| 1002600006 | The API call times exceed the quota. |
| 1002600007 | The API QPS exceeds the quota. |
| 1002600008 | The API is in arrears. |
| 1002600009 | The API has not subscribed to any pay-as-you-go package. |
| 1002600010 | The server is busy. Please wait and try again. |
| 1002600011 | Server error. |
| 1002600999 | Unknown error. |
| 1002602001 | The start and end points do not have home countries, or a service error occurred. |
| 1002602002 | Cross-region route planning is not supported. |
| 1002602003 | The number of start points or end points exceed 100. |
| 1002602004 | The linear distance between the start point and end point exceeds the upper limit. |
| 1002602005 | The start point, end point, or waypoint does not support navigation. |
| 1002602006 | The request point is mapped to the same point on the road. |

**示例：**

```ets
let params: navi.DrivingMatrixParams = {
  "origins": [
    {
      latitude: 31.984410259206815,
      longitude: 118.76625379397866
    },
    {
      latitude: 31.904410259206815,
      longitude: 118.70625379397866
    }
  ],
  "destinations": [{
    latitude: 30.9844109206815,
    longitude: 119.765379397866
  }],
  "trafficMode": 2,
  "language": "zh_CN"
};
const result = await navi.getDrivingMatrix(this.getUIContext().getHostContext(), params);
console.info("Succeeded in getting driving matrix.");
```

#### getWalkingMatrix

getWalkingMatrix(params: MatrixParams): Promise<MatrixResult>

规划多个地点之间的步行路线。使用Promise异步回调。

该功能适用于高并发场景，例如包裹递送。在这种情况下，该功能可以计算多个起点和终点之间的路线，并找到包裹递送所需的起点和终点。


1.

只能在直线距离150公里内规划步行路线。

1.

起点的数量乘以终点的数量不能超过100。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| params | MatrixParams | 是 | 步行批量算路的参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<MatrixResult> | Promise对象，返回MatrixResult。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. |
| 1002600001 | System internal error. |
| 1002600002 | Failed to connect to the Map Kit server. |
| 1002600003 | App authentication failed. |
| 1002600004 | The Map permission is not enabled. |
| 1002600006 | The API call times exceed the quota. |
| 1002600007 | The API QPS exceeds the quota. |
| 1002600008 | The API is in arrears. |
| 1002600009 | The API has not subscribed to any pay-as-you-go package. |
| 1002600010 | The server is busy. Please wait and try again. |
| 1002600011 | Server error. |
| 1002600999 | Unknown error. |
| 1002602001 | The start and end points do not have home countries, or a service error occurred. |
| 1002602002 | Cross-region route planning is not supported. |
| 1002602003 | The number of start points or end points exceed 100. |
| 1002602004 | The linear distance between the start point and end point exceeds the upper limit. |
| 1002602005 | The start point, end point, or waypoint does not support navigation. |
| 1002602006 | The request point is mapped to the same point on the road. |

**示例：**

```ets
let params: navi.MatrixParams = {
  "origins": [
    {
      latitude: 31.984410259206815,
      longitude: 118.76625379397866
    },
    {
      latitude: 31.904410259206815,
      longitude: 118.70625379397866
    }
  ],
  "destinations": [{
    latitude: 30.9844259206815,
    longitude: 119.765379397866
  }],
  "language": "zh_CN"
};
const result = await navi.getWalkingMatrix(params);
console.info("Succeeded in getting walking matrix.");
```

#### getWalkingMatrix

getWalkingMatrix(context: common.Context, params: MatrixParams): Promise<MatrixResult>

规划多个地点之间的步行路线，支持传入Context上下文。使用Promise异步回调。

该功能适用于高并发场景，例如包裹递送。在这种情况下，该功能可以计算多个起点和终点之间的路线，并找到包裹递送所需的起点和终点。


1.

只能在直线距离150公里内规划步行路线。

1.

起点的数量乘以终点的数量不能超过100。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | common.Context | 是 | Context上下文。 |
| params | MatrixParams | 是 | 步行批量算路的参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<MatrixResult> | Promise对象，返回MatrixResult。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. |
| 1002600001 | System internal error. |
| 1002600002 | Failed to connect to the Map Kit server. |
| 1002600003 | App authentication failed. |
| 1002600004 | The Map permission is not enabled. |
| 1002600006 | The API call times exceed the quota. |
| 1002600007 | The API QPS exceeds the quota. |
| 1002600008 | The API is in arrears. |
| 1002600009 | The API has not subscribed to any pay-as-you-go package. |
| 1002600010 | The server is busy. Please wait and try again. |
| 1002600011 | Server error. |
| 1002600999 | Unknown error. |
| 1002602001 | The start and end points do not have home countries, or a service error occurred. |
| 1002602002 | Cross-region route planning is not supported. |
| 1002602003 | The number of start points or end points exceed 100. |
| 1002602004 | The linear distance between the start point and end point exceeds the upper limit. |
| 1002602005 | The start point, end point, or waypoint does not support navigation. |
| 1002602006 | The request point is mapped to the same point on the road. |

**示例：**

```ets
let params: navi.MatrixParams = {
  "origins": [
    {
      latitude: 31.984410259206815,
      longitude: 118.76625379397866
    },
    {
      latitude: 31.904410259206815,
      longitude: 118.70625379397866
    }
  ],
  "destinations": [{
    latitude: 30.9810259206815,
    longitude: 119.765379397866
  }],
  "language": "zh_CN"
};
const result = await navi.getWalkingMatrix(this.getUIContext().getHostContext(), params);
console.info("Succeeded in getting walking matrix.");
```

#### getCyclingMatrix

getCyclingMatrix(params: MatrixParams): Promise<MatrixResult>

规划多个地点之间的骑行路线。使用Promise异步回调。

该功能适用于高并发场景，例如包裹递送。在这种情况下，该功能可以计算多个起点和终点之间的路线，并找到包裹递送所需的起点和终点。


1.

只能在直线距离500公里内规划骑行路线。

1.

起点的数量乘以终点的数量不能超过100。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| params | MatrixParams | 是 | 骑行批量算路的参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<MatrixResult> | Promise对象，返回MatrixResult。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. |
| 1002600001 | System internal error. |
| 1002600002 | Failed to connect to the Map Kit server. |
| 1002600003 | App authentication failed. |
| 1002600004 | The Map permission is not enabled. |
| 1002600006 | The API call times exceed the quota. |
| 1002600007 | The API QPS exceeds the quota. |
| 1002600008 | The API is in arrears. |
| 1002600009 | The API has not subscribed to any pay-as-you-go package. |
| 1002600010 | The server is busy. Please wait and try again. |
| 1002600011 | Server error. |
| 1002600999 | Unknown error. |
| 1002602001 | The start and end points do not have home countries, or a service error occurred. |
| 1002602002 | Cross-region route planning is not supported. |
| 1002602003 | The number of start points or end points exceed 100. |
| 1002602004 | The linear distance between the start point and end point exceeds the upper limit. |
| 1002602005 | The start point, end point, or waypoint does not support navigation. |
| 1002602006 | The request point is mapped to the same point on the road. |

**示例：**

```ets
let params: navi.MatrixParams = {
  "origins": [
    {
      latitude: 31.984410259206815,
      longitude: 118.76625379397866
    },
    {
      latitude: 31.904410259206815,
      longitude: 118.70625379397866
    }
  ],
  "destinations": [{
    latitude: 30.9841259206815,
    longitude: 119.766239397866
  }],
  "language": "zh_CN"
};
const result = await navi.getCyclingMatrix(params);
console.info("Succeeded in getting cycling matrix.");
```

#### getCyclingMatrix

getCyclingMatrix(context: common.Context, params: MatrixParams): Promise<MatrixResult>

规划多个地点之间的骑行路线，支持传入Context上下文。使用Promise异步回调。

该功能适用于高并发场景，例如包裹递送。在这种情况下，该功能可以计算多个起点和终点之间的路线，并找到包裹递送所需的起点和终点。


1.

只能在直线距离500公里内规划骑行路线。

1.

起点的数量乘以终点的数量不能超过100。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | common.Context | 是 | Context上下文。 |
| params | MatrixParams | 是 | 骑行批量算路的参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<MatrixResult> | Promise对象，返回MatrixResult。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. |
| 1002600001 | System internal error. |
| 1002600002 | Failed to connect to the Map Kit server. |
| 1002600003 | App authentication failed. |
| 1002600004 | The Map permission is not enabled. |
| 1002600006 | The API call times exceed the quota. |
| 1002600007 | The API QPS exceeds the quota. |
| 1002600008 | The API is in arrears. |
| 1002600009 | The API has not subscribed to any pay-as-you-go package. |
| 1002600010 | The server is busy. Please wait and try again. |
| 1002600011 | Server error. |
| 1002600999 | Unknown error. |
| 1002602001 | The start and end points do not have home countries, or a service error occurred. |
| 1002602002 | Cross-region route planning is not supported. |
| 1002602003 | The number of start points or end points exceed 100. |
| 1002602004 | The linear distance between the start point and end point exceeds the upper limit. |
| 1002602005 | The start point, end point, or waypoint does not support navigation. |
| 1002602006 | The request point is mapped to the same point on the road. |

**示例：**

```ets
let params: navi.MatrixParams = {
  "origins": [
    {
      latitude: 31.984410259206815,
      longitude: 118.76625379397866
    },
    {
      latitude: 31.904410259206815,
      longitude: 118.70625379397866
    }
  ],
  "destinations": [{
    latitude: 30.98259206815,
    longitude: 119.7679397866
  }],
  "language": "zh_CN"
};
const result = await navi.getCyclingMatrix(this.getUIContext().getHostContext(), params);
console.info("Succeeded in getting cycling matrix.");
```

#### snapToRoads

snapToRoads(params: SnapToRoadsParams): Promise<SnapToRoadsResult>

基于指定的坐标点捕获道路，将用户轨迹移动到正确的道路，并返回车辆行驶在实际道路上的一组坐标点。使用Promise异步回调。

坐标点的数量不能超过100，并且两个相邻点之间的距离必须小于等于500米。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| params | SnapToRoadsParams | 是 | 轨迹绑路的参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<SnapToRoadsResult> | Promise对象，返回SnapToRoadsResult。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. |
| 1002600001 | System internal error. |
| 1002600002 | Failed to connect to the Map Kit server. |
| 1002600003 | App authentication failed. |
| 1002600004 | The Map permission is not enabled. |
| 1002600006 | The API call times exceed the quota. |
| 1002600007 | The API QPS exceeds the quota. |
| 1002600008 | The API is in arrears. |
| 1002600009 | The API has not subscribed to any pay-as-you-go package. |
| 1002600010 | The server is busy. Please wait and try again. |
| 1002600011 | Server error. |
| 1002600999 | Unknown error. |
| 1002602001 | The start and end points do not have home countries, or a service error occurred. |
| 1002602002 | Cross-region route planning is not supported. |
| 1002602003 | The number of start points or end points exceed 100. |
| 1002602004 | The linear distance between the start point and end point exceeds the upper limit. |
| 1002602005 | The start point, end point, or waypoint does not support navigation. |
| 1002602006 | The request point is mapped to the same point on the road. |

**示例：**

```ets
let params: navi.SnapToRoadsParams = {
  points: [{
    latitude: 31.984410259206815,
    longitude: 118.76625379397866
  }]
};
const result = await navi.snapToRoads(params);
console.info("Succeeded in snapping to roads.");
```

#### snapToRoads

snapToRoads(context: common.Context, params: SnapToRoadsParams): Promise<SnapToRoadsResult>

基于指定的坐标点捕获道路，将用户轨迹移动到正确的道路，并返回车辆行驶在实际道路上的一组坐标点，支持传入Context上下文。使用Promise异步回调。

坐标点的数量不能超过100，并且两个相邻点之间的距离必须小于等于500米。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | common.Context | 是 | Context上下文。 |
| params | SnapToRoadsParams | 是 | 轨迹绑路的参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<SnapToRoadsResult> | Promise对象，返回SnapToRoadsResult。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. |
| 1002600001 | System internal error. |
| 1002600002 | Failed to connect to the Map Kit server. |
| 1002600003 | App authentication failed. |
| 1002600004 | The Map permission is not enabled. |
| 1002600006 | The API call times exceed the quota. |
| 1002600007 | The API QPS exceeds the quota. |
| 1002600008 | The API is in arrears. |
| 1002600009 | The API has not subscribed to any pay-as-you-go package. |
| 1002600010 | The server is busy. Please wait and try again. |
| 1002600011 | Server error. |
| 1002600999 | Unknown error. |
| 1002602001 | The start and end points do not have home countries, or a service error occurred. |
| 1002602002 | Cross-region route planning is not supported. |
| 1002602003 | The number of start points or end points exceed 100. |
| 1002602004 | The linear distance between the start point and end point exceeds the upper limit. |
| 1002602005 | The start point, end point, or waypoint does not support navigation. |
| 1002602006 | The request point is mapped to the same point on the road. |

**示例：**

```ets
let params: navi.SnapToRoadsParams = {
  points: [{
    latitude: 31.984410259206815,
    longitude: 118.76625379397866
  }]
};
const result = await navi.snapToRoads(this.getUIContext().getHostContext(), params);
console.info("Succeeded in snapping to roads.");
```

#### RouteCoordinate

路线规划属性。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| matchType | number | 否 | 是 | 起终点绑路类型。 取值包括0、1、3，默认值为0。 0：限制绑路。起点避免绑定封闭、施工、限行、偏好设置所避免的道路，终点避免绑定高速、轮渡、 偏好设置所避免的道路。 1：无限制绑路，不考虑道路本身限制。 3：轨迹绑路，通过origins字段输入连续轨迹点的经纬度进行无限制绑路，只支持起点。 |
| latitude | number | 否 | 否 | 纬度，取值范围：[-90, 90] 。 |
| longitude | number | 否 | 否 | 经度，取值范围：[-180, 180) 。 |
| accuracy | number | 否 | 是 | GPS定位精度，单位：米。无默认值。 |
| altitude | number | 否 | 是 | 海拔高度，单位：米。无默认值。 |
| bearing | number | 否 | 是 | 偏转角度。无默认值。 以正北方向为0度、顺时针方向为正的角度，默认值为0，取值范围：[0, 360)。超出取值范围的值会换算成取值范围内的值，比如361会被换算成1，-1换算为359。 |
| speed | number | 否 | 是 | 当前行驶速度，单位：米/秒。无默认值。 |
| timestamp | number | 否 | 是 | 当前定位生成时间的时间戳。无默认值。 |

#### RouteParams

步行、骑行和驾车路径规划参数接口。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| origins | Array<RouteCoordinate> | 否 | 否 | 道路绑定的起点坐标列表。 坐标点的数量不能超过31个，相邻两个点之间的距离应大于1米。 |
| destination | RouteCoordinate | 否 | 否 | 目的地。 说明： 若未设置途经点起点和目的地坐标不能相同。 |
| language | string | 否 | 是 | 文字指引/描述的语种。目前只支持中文zh_CN和英文en。如果不传，返回地点的当地语言。 |
| avoids | Array<number> | 否 | 是 | 表示指定计算路线的策略。取值包括： 0：速度快 1：避免收费 2：避免高速 4：距离短 8：避免轮渡 16：躲避拥堵 32：大路优先 64：智能路线 128：高速优先 256：少收费 512：速度流畅 默认值为0。 步行和骑行仅支持两种策略：0和8。 目前设置项16、32、128和256仅在中国大陆的路线规划中支持，后续将在其他国家和地区陆续支持这些设置项。 说明： 以上为单独策略，组合策略仅驾车支持1和8：避免收费+避免轮渡。 |
| extension | number | 否 | 是 | 额外信息。包括： 0：基础路况信息 1：新增路况信息 默认值为0。 |

#### RouteResult

路径规划的结果。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| routes | Array<Route> | 否 | 否 | 从起点到目的地的规划路径。如果没有结果，返回空数组。 |

#### DrivingRouteParams

驾车路径规划参数接口，继承[RouteParams](#ZH-CN_TOPIC_0000002553362337__routeparams)。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| waypoints | Array<[mapCommon.LatLng](mapCommon（地图属性模型）.md#section20691173773810)> | 否 | 是 | 途经点。最多可以输入5个途经点。 |
| isViaType | boolean | 否 | 是 | 途经点类型，是via类型还是stopover类型，默认值为false。 - false：stopover类型。 - true：via类型 说明： 1. stopover类型为经停点，将分段下发路线信息。 2. via类型为经过点，将整段下发路线信息。 |
| optimize | boolean | 否 | 是 | 是否对途经点进行优化。 - false：不进行途经点优化 - true：进行途经点优化 默认值为false。 |
| alternatives | boolean | 否 | 是 | 是否返回多条规划路线结果。 - true：返回多条规划路线结果 - false：返回单条规划路线结果 默认值为false。 |
| departAt | number | 否 | 是 | 预计出发时间。以自UTC 1970年1月1日午夜以来的秒数为单位。 必须是当前或者未来时间，不能是过去时间。 说明： departAt输入0时，按照当前时间进行处理。 |
| trafficMode | number | 否 | 是 | 时间预估模型。取值包括： 0：智能预测 1：路况差于历史平均水平 2：路况优于历史平均水平 默认值为0。 |

#### Route

从起点到目的地的规划路径。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| steps | Array<RouteStep> | 否 | 否 | 路线规划信息。 |
| overviewPolyline | Array<[mapCommon.LatLng](mapCommon（地图属性模型）.md#section20691173773810)> | 否 | 是 | 表示该路线的编码后的折线经纬度。 |
| optimizedWaypoints | Array<number> | 否 | 是 | 当isViaType = false且optimize = true 时才会有结果，表示进行路径优化之后途经点的索引。 |
| bounds | Array<CoordinateBound> | 否 | 是 | 路线边界范围。 |
| trafficLightCount | number | 否 | 是 | 红绿灯个数。 |
| isDestinationInRestrictedArea | boolean | 否 | 是 | 终点是否在限制区域。 - true：在限制区域 - false：不在限制区域 |
| isDestinationInDiffTimeZone | boolean | 否 | 是 | 目的地是否在不同时区。 - true：在不同时区 - false：在相同时区 |
| isCrossCountry | boolean | 否 | 是 | 是否穿越国境线。 - true：穿越国境线 - false：不穿越国境线 |
| isCrossMultiCountries | boolean | 否 | 是 | 是否穿越多条国境线。 - true：穿越多条国境线 - false：不穿越多条国境线 |
| hasRestrictedRoad | boolean | 否 | 是 | 此路段是否包含私家/限制用途。 - true：包含私家/限制用途 - false：不包含私家/限制用途 |
| hasRoughRoad | boolean | 否 | 是 | 此路段是否经过崎岖道路。 - true：经过崎岖道路 - false：不经过崎岖道路 |
| hasFerry | boolean | 否 | 是 | 是否途经轮渡。 - true：途经轮渡 - false：不途经轮渡 |
| hasTolls | boolean | 否 | 是 | 此路段是否含收费站。 - true：含收费站 - false：不含收费站 |
| hasStairs | boolean | 否 | 是 | 此路段是否含有阶梯。 - true：含有阶梯 - false：不含有阶梯 |

#### RouteStep

路段规划信息。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| roads | Array<RouteRoad> | 否 | 否 | 路线分段信息。 |
| startLocation | [mapCommon.LatLng](mapCommon（地图属性模型）.md#section20691173773810) | 否 | 否 | 出发地的经纬度。 |
| startAddress | string | 否 | 是 | startLocation对应的地址详情。 |
| endLocation | [mapCommon.LatLng](mapCommon（地图属性模型）.md#section20691173773810) | 否 | 否 | 目的地的经纬度。 |
| endAddress | string | 否 | 是 | endLocation对应的地址详情。 |
| viaWaypoints | Array<Waypoint> | 否 | 是 | 途经点信息。 |
| distance | number | 否 | 是 | 行驶/步行/骑行距离，单位：米。 |
| distanceDescription | string | 否 | 是 | distance的文本描述。 |
| duration | number | 否 | 是 | 行驶/步行/骑行时长，单位：秒。 |
| durationDescription | string | 否 | 是 | duration的文本描述。 |
| durationInTraffic | number | 否 | 是 | 基于实时路况计算出来的行驶/步行/骑行时长，单位：秒。 |
| durationInTrafficDescription | string | 否 | 是 | durationInTraffic的文本描述。 |

#### RouteRoad

路线分段信息。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| startLocation | [mapCommon.LatLng](mapCommon（地图属性模型）.md#section20691173773810) | 否 | 否 | 出发地的经纬度。 |
| endLocation | [mapCommon.LatLng](mapCommon（地图属性模型）.md#section20691173773810) | 否 | 否 | 目的地的经纬度。 |
| polyline | Array<[mapCommon.LatLng](mapCommon（地图属性模型）.md#section20691173773810)> | 否 | 否 | 此路段的一系列坐标点（包含起点和终点坐标）。 |
| distance | number | 否 | 否 | 行驶/步行/骑行距离，单位：米。 |
| distanceDescription | string | 否 | 是 | distance的文本描述。 |
| duration | number | 否 | 否 | 行驶/步行/骑行时长，单位：秒。 |
| durationDescription | string | 否 | 是 | duration的文本描述。 |
| roadName | string | 否 | 是 | 路名。 |
| action | string | 否 | 是 | 当前步骤要执行的操作。取值包括： - turn_slight_left：向左微转 - turn_sharp_left：向左急转 - turn_left：左转 - turn_slight_right：向右微转 - turn_sharp_right：向右急转 - turn_right：右转 - straight：直行 - end：终点 - waypoint：途经点 |
| orientation | number | 否 | 是 | 道路方向。取值包括： 0：双向 1：正向 2：反向 |
| instruction | string | 否 | 是 | 文字指引。 |
| trafficSegments | Array<TrafficSegment> | 否 | 是 | 路况信息。 |

#### CoordinateBound

路线边界范围。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| northeast | [mapCommon.LatLng](mapCommon（地图属性模型）.md#section20691173773810) | 否 | 否 | 东北角的位置。 |
| southwest | [mapCommon.LatLng](mapCommon（地图属性模型）.md#section20691173773810) | 否 | 否 | 西南角的位置。 |

#### Waypoint

途经点信息。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| location | [mapCommon.LatLng](mapCommon（地图属性模型）.md#section20691173773810) | 否 | 否 | 途经点的经纬度。 |
| stepIndex | number | 否 | 否 | 途经点在roads数组里的索引。 |

#### TrafficSegment

路况信息。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| distance | number | 否 | 否 | 行驶/步行/骑行距离，单位：米。 |
| status | number | 否 | 否 | 路况状态。取值包括： 0：未知 1：畅通 2：缓行 3：拥堵 4：严重拥堵 |
| polyline | Array<[mapCommon.LatLng](mapCommon（地图属性模型）.md#section20691173773810)> | 否 | 否 | 路段的形状坐标。 |

#### MatrixParams

步行、骑行和驾车批量算路参数接口。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| origins | Array<RouteCoordinate> | 否 | 否 | 起点的经纬度，不能超过100个。 |
| destinations | Array<RouteCoordinate> | 否 | 否 | 终点的经纬度，不能超过100个。 说明： 1. 驾车路线只能在直线距离2000公里内规划；步行路线只能在直线距离150公里内规划；骑行路线只能在直线距离500公里内规划。 2. 起点的数量乘以终点的数量不能超过100。 |
| language | string | 否 | 是 | 文字指引/描述的语种。目前只支持zh_CN和en。如果不传，返回地点的当地语言。 |
| avoids | Array<number> | 否 | 是 | 表示指定计算路线的策略。取值包括： 0：速度快 1：避免收费 2：避免高速 4：距离短 8：避免轮渡 16：躲避拥堵 32：大路优先 64：智能路线 128：高速优先 256：少收费 默认值为0。 步行和骑行只支持两种设置项：0和8。 驾车支持所有设置项，但目前设置项16、32、128和256仅在中国大陆的路线规划中支持，后续将在其他国家和地区陆续支持这些设置项。 |

#### TransitRouteParams

中转规划算路参数接口。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.1.1(19)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**5.1.1(19)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| origin | RouteCoordinate | 否 | 否 | 起点的经纬度。 |
| destination | RouteCoordinate | 否 | 否 | 终点的经纬度。 说明： 起点和终点的经纬度不能相同。 |
| departureTime | number | 否 | 是 | 预计出发时间，自1970年1月1日00:00:00（UTC）起的秒数。该值应该是当前时间或未来时间。 |
| preference | number | 否 | 是 | 偏好设置。取值包括： 0：推荐（默认值）。 1：地铁优先。 2：少走路。 3：少中转。 4：时间短。 5：不坐地铁。 默认值为0。 |

#### TransitRouteResult

中转规划结果。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.1.1(19)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**5.1.1(19)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| routes | TransitRoute[] | 否 | 是 | 可能的路线列表。 |

#### TransitRoute

中转路线。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.1.1(19)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**5.1.1(19)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| id | string | 否 | 否 | 路线ID。 |
| sections | TransitRouteSection[] | 否 | 否 | 交通路线和行人路段列表。 |
| busSortInfo | BusSortInfo | 否 | 是 | 路线规划汇总信息。 |

#### BusSortInfo

路线规划汇总信息。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.1.1(19)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**5.1.1(19)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| totalCost | number | 否 | 是 | 总时长（单位：秒）。 |
| walkLength | number | 否 | 是 | 步行距离（单位：米）。 |
| transferNum | number | 否 | 是 | 中转次数。 |
| fee | number | 否 | 是 | 费用。预留字段，当前无使用场景。 |
| score | number | 否 | 是 | 建议得分。考虑耗时、步行距离、换乘次数、站点数量、路线性质(纯公交、纯地铁、混合)，加权后得到路线的得分，使用得分对路线排序，系统推荐得分更高的路线。预留字段，当前无使用场景。 |
| routeId | string | 否 | 是 | 路径ID。 |
| currency | string | 否 | 是 | 收款货币。预留字段，当前无使用场景。 |
| arrivalTime | number | 否 | 是 | 最早到达时间（单位：秒）。 |
| routeDesc | number | 否 | 是 | 路线标签。取值包括： 0：正常路线。 1：超出运行时间路线。 2：此路线可能错过末班车。 预留字段，当前无使用场景。 |

#### TransitRouteSection

交通路线和行人路段。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.1.1(19)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**5.1.1(19)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | string | 否 | 否 | 路段类型。取值包括： - pedestrian：步行 - transit：中转 |
| pedestrianSection | PedestrianSection | 否 | 是 | 行人路段。 |
| transitSection | TransitSection | 否 | 是 | 中转区。 |

#### PedestrianSection

表示路线中行人路段。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.1.1(19)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**5.1.1(19)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| id | string | 否 | 否 | 行人路段的唯一标识符。 |
| type | string | 否 | 否 | 客户端用来标识的类型。固定值：'pedestrian'。 |
| arrival | PedestrianDepartureArrival | 否 | 否 | 行人路段的终点。 |
| departure | PedestrianDepartureArrival | 否 | 否 | 行人路段的起点。 |
| language | string | 否 | 是 | 本地语言（如果有），采用BCP47格式。 |
| passthrough | Passthrough[] | 否 | 是 | 此路段正在经过的途经点列表。请求的每个途经点在响应中显示为passThrough=true。途经点出现在最近的非直达路线中。途经点按请求中的顺序遍历。 预留字段，当前无使用场景。 |
| polyline | [mapCommon.LatLng](mapCommon（地图属性模型）.md#section20691173773810)[] | 否 | 是 | 路线的形状坐标。 |
| travelSummary | BaseSummary | 否 | 是 | 关键属性（例如，持续时间、长度）的集合，仅在‘出发’和‘到达’之间的旅行部分。 |

#### PedestrianDepartureArrival

行人路线起、终点。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.1.1(19)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**5.1.1(19)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| place | Place | 否 | 否 | 行人路线中的场所。 |
| time | number | 否 | 是 | 预计出发时间，从1970年1月1日00:00:00开始的秒数（UTC）。 |

#### Passthrough

描述路线经过的地点。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.1.1(19)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**5.1.1(19)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| place | Place | 否 | 否 | 出发/到达地点。 |
| offset | number | 否 | 是 | 途经点的坐标索引值。 |

#### Place

表示与路线相关的通用地点。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.1.1(19)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**5.1.1(19)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| location | [mapCommon.LatLng](mapCommon（地图属性模型）.md#section20691173773810) | 否 | 否 | 地点。 |
| type | string | 否 | 否 | 场所类型。取值包括： - accessPoint：步行接入点。 - station：公共交通站台。 |
| name | string | 否 | 是 | 地点名称。 |

#### BaseSummary

路线关键属性的集合。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.1.1(19)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**5.1.1(19)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| duration | number | 否 | 否 | 持续时间，单位：秒。 |
| length | number | 否 | 否 | 距离，单位：米。 |
| waitTime | number | 否 | 是 | 等待时间，单位：秒。 |

#### TransitSection

路线的一段。它包含出发、到达和路线信息。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.1.1(19)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**5.1.1(19)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| id | string | 否 | 否 | 路线的唯一标识符。预留字段，当前无使用场景。 |
| type | string | 否 | 否 | 客户端用来标识可用基础部分扩展的类型。固定值：'transit'。 |
| arrival | TransitArrival | 否 | 否 | 中转结束。 |
| departure | TransitDeparture | 否 | 否 | 中转开始。 |
| intermediateStops | TransitStop[] | 否 | 是 | 中转线路的始发站和目的地之间的中间站点。 如果此信息不可用或未请求，则可能缺失。 |
| language | string | 否 | 是 | 本地语言（如果有），采用BCP47格式。预留字段，当前无使用场景。 |
| passthrough | Passthrough[] | 否 | 是 | 此路段正在经过的途经点列表。请求的每个途经点在响应中显示为passThrough=true。途经点出现在最近的非直达路线中。途经点按请求中的顺序遍历。 预留字段，当前无使用场景。 |
| polyline | [mapCommon.LatLng](mapCommon（地图属性模型）.md#section20691173773810)[] | 否 | 是 | 路线的形状坐标。 |
| transport | TransitTransport | 否 | 是 | 中转路线信息。 |
| travelSummary | BaseSummary | 否 | 是 | 关键属性（例如，持续时间、长度）的集合。仅在‘出发’和‘到达’之间的旅行部分进行汇总，不包括预操作和后操作。 |
| extraTransitSection | ExtraTransitSection[] | 否 | 是 | 相同的起点和终点，可到达的其他公共交通线路。 |
| sectionDesc | number | 否 | 是 | 路线标签。取值包括： 0：正常路线。 1：不在操作时间路线中。 2：此路线可能错过末班车。 预留字段，当前无使用场景。 |
| firstVehicleHour | number | 否 | 是 | 首班车/地铁时间（单位：秒）。 |
| finalVehicleHour | number | 否 | 是 | 末班车/地铁时间（单位：秒）。 |
| stopOffset | number | 否 | 是 | 上车站点/换乘站点距离始发站的偏移时间。 |

#### TransitArrival

中转到达。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.1.1(19)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**5.1.1(19)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| place | Place | 否 | 否 | 到达地点。 |
| delay | number | 否 | 是 | 距计划时间的累计延迟（以秒为单位）。预留字段，当前无使用场景。 |
| time | number | 否 | 是 | 自1970年1月1日00:00:00（UTC）起，中转站的预计到达时间。以秒为单位。 |
| exit | TransitEntranceExit | 否 | 是 | 中转站出口。 |

#### TransitDeparture

中转出发。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.1.1(19)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**5.1.1(19)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| place | Place | 否 | 否 | 出发地点。 |
| delay | number | 否 | 是 | 距计划时间的累计延迟（以秒为单位）。预留字段，当前无使用场景。 |
| time | number | 否 | 是 | 自1970年1月1日00:00:00（UTC）起，中转站的预计出发时间。以秒为单位。 |
| entrance | TransitEntranceExit | 否 | 是 | 中转站入口。 |

#### TransitEntranceExit

中转站出入口。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.1.1(19)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**5.1.1(19)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| name | string | 否 | 否 | 出入口编号。 |
| location | [mapCommon.LatLng](mapCommon（地图属性模型）.md#section20691173773810) | 否 | 否 | 地点。 |

#### TransitStop

路线的中转站。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.1.1(19)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**5.1.1(19)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| departure | TransitDeparture | 否 | 否 | 中转开始。 |
| duration | number | 否 | 是 | 停止时长。如果未设置，车辆将在人员上车后立即出发（以秒为单位）。 |

#### TransitTransport

中转路线信息。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.1.1(19)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**5.1.1(19)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| mode | TransitMode | 否 | 否 | 中转类型。 |
| category | string | 否 | 是 | 人类易辨认的交通工具类别（如公共汽车、贡多拉、电车、火车等）。 |
| color | string | 否 | 是 | 公共交通路线的背景颜色。 |
| headsign | string | 否 | 是 | 中转线标志。 |
| name | string | 否 | 是 | 中转线名称。 |
| textColor | string | 否 | 是 | 公共交通名称的颜色。 |

#### ExtraTransitSection

额外中转路线信息。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.1.1(19)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**5.1.1(19)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| intermediateStops | TransitStop[] | 否 | 否 | 中转线路的始发站和目的地之间的中间站点。如果此信息不可用或未请求，则可能缺失。 |
| polyline | [mapCommon.LatLng](mapCommon（地图属性模型）.md#section20691173773810)[] | 否 | 否 | 路线的形状坐标。 |
| transport | TransitTransport | 否 | 否 | 中转路线信息。 |
| travelSummary | BaseSummary | 否 | 否 | 关键属性（例如，持续时间、长度）的集合。仅在‘出发’和‘到达’之间的旅行部分进行汇总，不包括预操作和后操作。 |
| firstVehicleHour | number | 否 | 是 | 首班车/地铁时间（单位：秒）。 |
| finalVehicleHour | number | 否 | 是 | 末班车/地铁时间（单位：秒）。 |
| stopOffset | number | 否 | 是 | 上车站点/换乘站点距离始发站的偏移时间。 |

#### TransitMode

中转类型。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.1.1(19)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**5.1.1(19)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| BUS | bus | 公交。 |
| SUBWAY | subway | 地铁。 |

#### MatrixResult

批量算路的结果。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| originAddresses | Array<string> | 否 | 否 | 起点的地址详情。 |
| destinationAddresses | Array<string> | 否 | 否 | 终点的地址详情。 |
| rows | Array<MatrixRow> | 否 | 否 | 起点和终点两两进行路径规划后的计算出来的时长和距离。 |

#### DrivingMatrixParams

驾车批量算路参数接口，继承[MatrixParams](#ZH-CN_TOPIC_0000002553362337__matrixparams)。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| departAt | number | 否 | 是 | 预计出发时间。以自UTC 1970年1月1日午夜以来的秒数为单位。 必须是当前或者未来时间，不能是过去时间。 说明： departAt输入0时，按照当前时间进行处理。 |
| trafficMode | number | 否 | 是 | 时间预估模型。取值包括： 0：最佳猜测（默认值）。 1：路况差于历史平均水平。 2：路况优于历史平均水平。 默认值为0。 |

#### MatrixRow

起点和终点两两进行路径规划后的计算出来的时长和距离。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| cells | Array<MatrixCell> | 否 | 否 | 距离矩阵中每个单元格的信息。 |

#### MatrixCell

距离矩阵中每个单元格的信息。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| distance | number | 否 | 是 | 行驶/步行/骑行距离，单位：米。 |
| distanceDescription | string | 否 | 是 | distance的文本描述。 |
| duration | number | 否 | 是 | 行驶/步行/骑行时长，单位：秒。 |
| durationDescription | string | 否 | 是 | duration的文本描述。 |

#### SnapToRoadsParams

轨迹绑路的参数。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| points | Array<[mapCommon.LatLng](mapCommon（地图属性模型）.md#section20691173773810)> | 否 | 否 | 道路贴合点集合，集合个数取值范围：[1,100]，且相邻两个点距离需小于等于500米。 |

#### SnapToRoadsResult

轨迹绑路的结果。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| responseTime | number | 否 | 否 | 耗时，单位：毫秒。 |
| snappedPoints | Array<SnappedPoint> | 否 | 否 | 道路上的坐标点。坐标点的数量不能超过100个，并且两个相邻点之间的距离不能超过500米。 |

#### SnappedPoint

道路吸附点。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| latitude | number | 否 | 否 | 纬度 。 |
| longitude | number | 否 | 否 | 经度 。 |
| roadId | string | 否 | 否 | 道路ID。 |