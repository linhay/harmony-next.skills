# petalMaps（拉起地图应用）

本模块提供拉起地图应用功能。

**起始版本：**5.0.3(15)

#### 导入模块

```ets
import { petalMaps } from '@kit.MapKit';
```

#### openMapHomePage

openMapHomePage(context: common.Context): Promise<void>

根据提供的参数打开地图应用首页。使用Promise异步回调。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.Map.Core

**设备行为差异：**对于API 19及之前的版本，该接口在phone、tablet中可正常使用，在其他设备中返回801错误。在API20及之后版本该接口在phone、tablet、2in1均可正常使用，在其他设备中返回801错误。

**起始版本：**5.0.3(15)

**参数：**

**参数名**

**类型**

必填

**说明**

context

[common.Context](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-context)

是

Context上下文。

**返回值：**

类型

说明

Promise<void>

Promise对象。无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

错误码ID

错误信息

401

Invalid input parameter.

1002600014

Failed to start the map app.

801

Capability not supported. Failed to call the API due to limited device capabilities.

**示例：**

```ets
await petalMaps.openMapHomePage(this.getUIContext().getHostContext());
```

#### openMapPoiDetail

openMapPoiDetail(context: common.Context, poiDetailParams: PoiDetailParams): Promise<void>

根据提供的参数打开地图应用的POI详情页面。使用Promise异步回调。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.Map.Core

**设备行为差异：**对于API 19及之前的版本，该接口在phone、tablet中可正常使用，在其他设备中返回801错误。在API20及之后版本该接口在phone、tablet、2in1均可正常使用，在其他设备中返回801错误。

**起始版本：**5.0.3(15)

**参数：**

**参数名**

**类型**

必填

**说明**

context

[common.Context](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-context)

是

Context上下文。

poiDetailParams

[PoiDetailParams](#section1555293218278)

是

POI详情的参数。

**返回值：**

类型

说明

Promise<void>

Promise对象。无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

错误码ID

错误信息

401

Invalid input parameter.

1002600014

Failed to start the map app.

801

Capability not supported. Failed to call the API due to limited device capabilities.

**示例：**

```ets
let params: petalMaps.PoiDetailParams = {
  destinationPosition: {
    latitude: 30.983015468224288,
    longitude: 118.78058590757131
  }
};
await petalMaps.openMapPoiDetail(this.getUIContext().getHostContext(), params);
```

#### openMapTextSearch

openMapTextSearch(context: common.Context, textSearchParams: TextSearchParams): Promise<void>

根据提供的参数打开地图应用的文本搜索页面。使用Promise异步回调。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.Map.Core

**设备行为差异：**对于API 19及之前的版本，该接口在phone、tablet中可正常使用，在其他设备中返回801错误。在API20及之后版本该接口在phone、tablet、2in1均可正常使用，在其他设备中返回801错误。

**起始版本：**5.0.3(15)

**参数：**

**参数名**

**类型**

必填

**说明**

context

[common.Context](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-context)

是

Context上下文。

textSearchParams

[TextSearchParams](#section810823717266)

是

文本搜索的参数。

**返回值：**

类型

说明

Promise<void>

Promise对象。无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

错误码ID

错误信息

401

Invalid input parameter.

1002600014

Failed to start the map app.

801

Capability not supported. Failed to call the API due to limited device capabilities.

**示例：**

```ets
let params: petalMaps.TextSearchParams = {
  destinationName: '云谷'
};
await petalMaps.openMapTextSearch(this.getUIContext().getHostContext(), params);
```

#### openMapRoutePlan

openMapRoutePlan(context: common.Context, routePlanParams: RoutePlanParams): Promise<void>

根据提供的参数打开地图应用的路线规划页面。使用Promise异步回调。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.Map.Core

**设备行为差异：**对于API 19及之前的版本，该接口在phone、tablet中可正常使用，在其他设备中返回801错误。在API20及之后版本该接口在phone、tablet、2in1均可正常使用，在其他设备中返回801错误。

**起始版本：**5.0.3(15)

**参数：**

**参数名**

**类型**

必填

**说明**

context

[common.Context](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-context)

是

Context上下文。

routePlanParams

[RoutePlanParams](#section491624219261)

是

路线规划的参数。

**返回值：**

类型

说明

Promise<void>

Promise对象。无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

错误码ID

错误信息

401

Invalid input parameter.

1002600014

Failed to start the map app.

801

Capability not supported. Failed to call the API due to limited device capabilities.

**示例：**

```ets
let params: petalMaps.RoutePlanParams = {
  destinationPosition: {
    latitude: 31.983015468224288,
    longitude: 118.78058590757131
  }
};
await petalMaps.openMapRoutePlan(this.getUIContext().getHostContext(), params);
```

#### openMapNavi

openMapNavi(context: common.Context, naviParams: NaviParams): Promise<void>

根据提供的参数打开地图应用的导航页面。使用Promise异步回调。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.Map.Core

**设备行为差异：**对于API 19及之前的版本，该接口在phone、tablet中可正常使用，在其他设备中返回801错误。在API20及之后版本该接口在phone、tablet、2in1均可正常使用，在其他设备中返回801错误。

**起始版本：**5.0.3(15)

**参数：**

**参数名**

**类型**

必填

**说明**

context

[common.Context](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-context)

是

Context上下文。

naviParams

[NaviParams](#section7249174522611)

是

导航的参数。

**返回值：**

类型

说明

Promise<void>

Promise对象。无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

错误码ID

错误信息

401

Invalid input parameter.

1002600014

Failed to start the map app.

801

Capability not supported. Failed to call the API due to limited device capabilities.

**示例：**

```ets
let params: petalMaps.NaviParams = {
  destinationPosition: {
    latitude: 31.983015468224288,
    longitude: 118.78058590757131
  }
};
await petalMaps.openMapNavi(this.getUIContext().getHostContext(), params);
```

#### openMapTaxi

openMapTaxi(context: common.Context, taxiParams: TaxiParams): Promise<void>

根据提供的参数打开地图应用的打车页面。使用Promise异步回调。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.Map.Core

**设备行为差异：**在API21及之后版本该接口在phone和tablet均可正常使用，在其他设备中返回801错误。

**起始版本：**6.0.1(21)

**参数：**

**参数名**

**类型**

必填

**说明**

context

[common.Context](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-context)

是

Context上下文。

taxiParams

[TaxiParams](#section1625316256212)

是

打车的参数。

**返回值：**

类型

说明

Promise<void>

Promise对象。无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

错误码ID

错误信息

1002600014

Failed to start the map app.

801

Capability not supported. Failed to call the API due to limited device capabilities.

**示例：**

```ets
let params: petalMaps.TaxiParams = {
  destinationPosition: {
    latitude: 31.983015468224288,
    longitude: 118.78058590757131
  }
};
await petalMaps.openMapTaxi(this.getUIContext().getHostContext(), params);
```

#### PoiDetailParams

POI详情的参数。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.Map.Core

**设备行为差异：**对于API 19及之前的版本，该接口在phone、tablet中可正常使用，在其他设备中返回801错误。在API20及之后版本该接口在phone、tablet、2in1均可正常使用，在其他设备中返回801错误。

**起始版本：**5.0.3(15)

**名称**

**类型**

只读

可选

**说明**

destinationPosition

[mapCommon.LatLng](mapCommon（地图属性模型）.md#section20691173773810)

否

否

终点的坐标。

取值范围：经度[-180, 180)，纬度[-85.2, 85.2]。对异常值进行处理，返回错误码401。

destinationName

string

否

是

终点的名称，超长名称超出部分用省略号“...”表示。

destinationPoiId

string

否

是

终点的POI ID。

POI ID和经纬度都作为入参时，POI ID具有更高优先级。

zoom

number

否

是

地图缩放级别。取值范围：[3, 20]，默认值：17，异常值按照默认值处理。

 说明：

当传入destinationPoiId时zoom层级不支持自定义。

**起始版本：**6.0.1(21)

coordinateType

[mapCommon.CoordinateType](mapCommon（地图属性模型）.md#section78948324526)

否

是

地图坐标系类型。默认值[mapCommon.CoordinateType](mapCommon（地图属性模型）.md#section78948324526).GCJ02，异常值按照默认值处理。

**起始版本：**6.0.1(21)

**示例：**

```ets
let params: petalMaps.PoiDetailParams = {
  destinationPosition: {
    latitude: 30.983015468224288,
    longitude: 118.78058590757131
  }
};
```

#### TextSearchParams

文本搜索的参数。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.Map.Core

**设备行为差异：**对于API 19及之前的版本，该接口在phone、tablet中可正常使用，在其他设备中返回801错误。在API20及之后版本该接口在phone、tablet、2in1均可正常使用，在其他设备中返回801错误。

**起始版本：**5.0.3(15)

**名称**

**类型**

只读

可选

**说明**

destinationName

string

否

是

终点的名称，超长名称超出部分用省略号“...”表示。

**示例：**

```ets
let params: petalMaps.TextSearchParams = {
  destinationName: '云谷'
};
```

#### RoutePlanParams

路线规划的参数。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.Map.Core

**设备行为差异：**对于API 19及之前的版本，该接口在phone、tablet中可正常使用，在其他设备中返回801错误。在API20及之后版本该接口在phone、tablet、2in1均可正常使用，在其他设备中返回801错误。

**起始版本：**5.0.3(15)

**名称**

**类型**

只读

可选

**说明**

originPosition

[mapCommon.LatLng](mapCommon（地图属性模型）.md#section20691173773810)

否

是

起点的坐标。默认值为用户当前坐标。

取值范围：经度[-180, 180)，纬度[-85.2, 85.2]。对异常值进行处理，返回错误码401。

originName

string

否

是

起点的名称，超长名称超出部分用省略号“...”表示。

originPoiId

string

否

是

起点的POI ID。

POI ID和经纬度都入参时，POI ID具有更高优先级。

destinationPosition

[mapCommon.LatLng](mapCommon（地图属性模型）.md#section20691173773810)

否

否

终点的坐标。

取值范围：经度[-180, 180)，纬度[-85.2, 85.2]。对异常值进行处理，返回错误码401。

destinationName

string

否

是

终点的名称，超长名称超出部分用省略号“...”表示。

destinationPoiId

string

否

是

终点的POI ID。

POI ID和经纬度都入参时，POI ID具有更高优先级。

vehicleType

[VehicleType](#section73559613164)

否

是

出行方式。

默认值为[VehicleType](#section73559613164).DRIVING，异常值按默认值处理。

coordinateType

[mapCommon.CoordinateType](mapCommon（地图属性模型）.md#section78948324526)

否

是

地图坐标系类型。默认值[mapCommon.CoordinateType](mapCommon（地图属性模型）.md#section78948324526).GCJ02，异常值按照默认值处理。

**起始版本：**6.0.1(21)

**示例：**

```ets
let params: petalMaps.RoutePlanParams = {
  destinationPosition: {
    latitude: 31.983015468224288,
    longitude: 118.78058590757131
  }
};
```

#### NaviParams

导航的参数。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.Map.Core

**设备行为差异：**对于API 19及之前的版本，该接口在phone、tablet中可正常使用，在其他设备中返回801错误。在API20及之后版本该接口在phone、tablet、2in1均可正常使用，在其他设备中返回801错误。

**起始版本：**5.0.3(15)

**名称**

**类型**

只读

可选

**说明**

destinationPosition

[mapCommon.LatLng](mapCommon（地图属性模型）.md#section20691173773810)

否

否

终点的坐标。

取值范围：经度[-180, 180)，纬度[-85.2, 85.2]。对异常值进行处理，返回错误码401。

destinationName

string

否

是

终点名称，超长名称超出部分用省略号“...”表示。

destinationPoiId

string

否

是

终点的POI ID。

POI ID和经纬度都入参时，POI ID具有更高优先级。

vehicleType

[VehicleType](#section73559613164)

否

是

出行方式。

默认值为[VehicleType](#section73559613164).DRIVING，异常值按默认值处理。

originPosition

[mapCommon.LatLng](mapCommon（地图属性模型）.md#section20691173773810)

否

是

起点的坐标。默认值为用户当前坐标。

取值范围：经度[-180, 180)，纬度[-85.2, 85.2]。对异常值进行处理，返回错误码401。

**起始版本：**6.0.1(21)

originName

string

否

是

起点的名称，超长名称超出部分用省略号“...”表示。

**起始版本：**6.0.1(21)

originPoiId

string

否

是

起点的POI ID。

POI ID和经纬度都入参时，POI ID具有更高优先级。

**起始版本：**6.0.1(21)

coordinateType

[mapCommon.CoordinateType](mapCommon（地图属性模型）.md#section78948324526)

否

是

地图坐标系类型。默认值[mapCommon.CoordinateType](mapCommon（地图属性模型）.md#section78948324526).GCJ02，异常值按照默认值处理。

**起始版本：**6.0.1(21)

**示例：**

```ets
let params: petalMaps.NaviParams = {
  destinationPosition: {
    latitude: 31.983015468224288,
    longitude: 118.78058590757131
  }
};
```

#### VehicleType

出行方式。地图应用侧目前出行方式暂时仅支持驾车、步行、骑行、公交。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.Map.Core

**设备行为差异：**对于API 19及之前的版本，该接口在phone、tablet中可正常使用，在其他设备中返回801错误。在API20及之后版本该接口在phone、tablet、2in1均可正常使用，在其他设备中返回801错误。

**起始版本：**5.0.3(15)

名称

值

说明

DRIVING

0

驾车。

WALKING

1

步行。

CYCLING

2

骑行。

TRANSIT

3

公交。

**起始版本：**6.0.1(21)

#### TaxiParams

打车的参数。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.Map.Core

**设备行为差异：**在API21及之后版本该接口在phone、tablet均可正常使用，在其他设备中返回801错误。

**起始版本：**6.0.1(21)

**名称**

**类型**

只读

可选

**说明**

destinationPosition

[mapCommon.LatLng](mapCommon（地图属性模型）.md#section20691173773810)

否

否

终点的坐标。

取值范围：经度[-180, 180)，纬度[-85.2, 85.2]。对异常值进行处理，返回错误码401。

destinationName

string

否

是

终点名称，超长名称超出部分用省略号“...”表示。

destinationPoiId

string

否

是

终点的POI ID。

POI ID和经纬度都入参时，POI ID具有更高优先级。

originPosition

[mapCommon.LatLng](mapCommon（地图属性模型）.md#section20691173773810)

否

是

起点的坐标。默认值为用户当前坐标。

取值范围：经度[-180, 180)，纬度[-85.2, 85.2]。对异常值进行处理，返回错误码401。

originName

string

否

是

起点的名称，超长名称超出部分用省略号“...”表示。

originPoiId

string

否

是

起点的POI ID。

POI ID和经纬度都入参时，POI ID具有更高优先级。

coordinateType

[mapCommon.CoordinateType](mapCommon（地图属性模型）.md#section78948324526)

否

是

地图坐标系类型。默认值[mapCommon.CoordinateType](mapCommon（地图属性模型）.md#section78948324526).GCJ02，异常值按照默认值处理。

**示例：**

```ets
let params: petalMaps.TaxiParams = {
  destinationPosition: {
    latitude: 31.983015468224288,
    longitude: 118.78058590757131
  }
};
```