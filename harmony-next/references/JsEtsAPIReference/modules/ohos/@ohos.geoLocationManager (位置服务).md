# @ohos.geoLocationManager (位置服务)

位置服务提供GNSS定位、网络定位（蜂窝基站、WLAN、蓝牙定位技术）、地理编码、逆地理编码、国家码和地理围栏等基本功能。

使用位置服务时请打开设备“位置”开关。如果“位置”开关关闭并且代码未设置捕获异常，可能导致应用异常。

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块能力仅支持WGS-84坐标系。

#### 申请权限

请参考[申请位置权限开发指导](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/location-permission-guidelines)。

#### 导入模块

```ets
import { geoLocationManager } from '@kit.LocationKit';
```

#### ReverseGeoCodeRequest

逆地理编码请求参数。

**系统能力**：SystemCapability.Location.Location.Geocoder

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| locale | string | 否 | 是 | 指定位置描述信息的语言，“zh”代表中文，“en”代表英文。默认值从设置中的“语言和地区”获取。 |
| country12+ | string | 否 | 是 | 限制查询结果在指定的国家内，采用ISO 3166-1 alpha-2 。“CN”代表中国。默认值从设置中的“语言和地区”获取。 |
| latitude | number | 否 | 否 | 表示纬度信息，正值表示北纬，负值表示南纬。取值范围为-90到90。仅支持WGS84坐标系。 |
| longitude | number | 否 | 否 | 表示经度信息，正值表示东经，负值表示西经。取值范围为-180到180。仅支持WGS84坐标系。 |
| maxItems | number | 否 | 是 | 指定返回位置信息的最大个数。取值范围为大于等于0，推荐该值小于10。默认值是1。 |

#### GeoCodeRequest

地理编码请求参数。

**系统能力**：SystemCapability.Location.Location.Geocoder

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| locale | string | 否 | 是 | 表示位置描述信息的语言，“zh”代表中文，“en”代表英文。默认值从设置中的“语言和地区”获取。 |
| country12+ | string | 否 | 是 | 限制查询结果在指定的国家内，采用ISO 3166-1 alpha-2 。“CN”代表中国。默认值从设置中的“语言和地区”获取。 |
| description | string | 否 | 否 | 表示位置信息描述，如“上海市浦东新区xx路xx号”，字符串长度不超过100。 |
| maxItems | number | 否 | 是 | 表示返回位置信息的最大个数。取值范围为大于等于0，推荐该值小于10。默认值是1。 |
| minLatitude | number | 否 | 是 | 表示最小纬度信息，与下面三个参数一起，表示一个经纬度范围。取值范围为-90到90。仅支持WGS84坐标系。如果该参数有值时，下面三个参数必填。 |
| minLongitude | number | 否 | 是 | 表示最小经度信息。取值范围为-180到180。仅支持WGS84坐标系。 |
| maxLatitude | number | 否 | 是 | 表示最大纬度信息。取值范围为-90到90。仅支持WGS84坐标系。 |
| maxLongitude | number | 否 | 是 | 表示最大经度信息。取值范围为-180到180。仅支持WGS84坐标系。 |

#### GeoAddress

地理编码地址信息。

**系统能力**：SystemCapability.Location.Location.Geocoder

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| latitude | number | 否 | 是 | 表示纬度信息，正值表示北纬，负值表示南纬。取值范围为-90到90。仅支持WGS84坐标系。 |
| longitude | number | 否 | 是 | 表示经度信息，正值表示东经，负值表示西经。取值范围为-180到180。仅支持WGS84坐标系。 |
| locale | string | 否 | 是 | 表示位置描述信息的语言，“zh”代表中文，“en”代表英文。 |
| placeName | string | 否 | 是 | 表示详细地址信息。 |
| countryCode | string | 否 | 是 | 表示国家码信息。 |
| countryName | string | 否 | 是 | 表示国家信息。 |
| administrativeArea | string | 否 | 是 | 表示国家以下的一级行政区，一般是省/州。 |
| subAdministrativeArea | string | 否 | 是 | 表示国家以下的二级行政区，一般是市。 |
| locality | string | 否 | 是 | 表示城市信息，一般是市。 |
| subLocality | string | 否 | 是 | 表示子城市信息，一般是区/县。 |
| roadName | string | 否 | 是 | 表示路名信息。 |
| subRoadName | string | 否 | 是 | 表示子路名信息。 |
| premises | string | 否 | 是 | 表示门牌号信息。 |
| postalCode | string | 否 | 是 | 表示邮政编码信息。 |
| phoneNumber | string | 否 | 是 | 表示联系方式信息。 |
| addressUrl | string | 否 | 是 | 表示位置信息附件的网址信息。 |
| descriptions | Array<string> | 否 | 是 | 表示附加的描述信息。目前包含城市编码cityCode（Array下标为0）和区划编码adminCode（Array下标为1），例如["025","320114001"]。 |
| descriptionsSize | number | 否 | 是 | 表示附加的描述信息数量。取值范围为大于等于0，推荐该值小于10。 |

#### LocationRequest

位置信息请求参数。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Location.Location.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| priority | LocationRequestPriority | 否 | 是 | 表示优先级信息。当scenario取值为UNSET时，priority参数生效，否则priority参数不生效；当scenario和priority均取值为UNSET时，无法发起定位请求。取值范围见LocationRequestPriority的定义。默认值为FIRST_FIX。 |
| scenario | LocationRequestScenario | 否 | 是 | 表示场景信息。当scenario取值为UNSET时，priority参数生效，否则priority参数不生效；当scenario和priority均取值为UNSET时，无法发起定位请求。取值范围见LocationRequestScenario的定义。默认值为UNSET。 |
| timeInterval | number | 否 | 是 | 表示上报位置信息的时间间隔，单位为秒。 取值范围为大于等于0的值。 默认值为对应定位模式下允许的最小时间间隔： 默认值在GNSS定位时为1秒，网络定位时为20秒。 当设置值小于最小间隔时，以最小时间间隔生效。 设置为0时不对时间间隔进行校验，直接上报位置信息。 |
| distanceInterval | number | 否 | 是 | 表示上报位置信息的距离间隔。单位是米，默认值为0，取值范围为大于等于0。等于0时对位置上报距离间隔无限制。 |
| maxAccuracy | number | 否 | 是 | 应用向系统请求位置信息时要求的精度值，单位为米。该参数仅在精确位置功能场景（即同时授权了ohos.permission.APPROXIMATELY_LOCATION和ohos.permission.LOCATION 权限）下有效，模糊位置功能生效场景（即仅授权了ohos.permission.APPROXIMATELY_LOCATION 权限）下该字段无意义。 该参数生效的情况下，系统会对比GNSS或网络定位服务上报的位置信息与应用的位置信息申请。当位置信息Location中的精度值（accuracy）小于等于应用要求的精度值（maxAccuracy）时，位置信息会返回给应用；否则系统将丢弃本次收到的位置信息。 默认值为0，表示不限制位置信息的精度，取值范围为大于等于0。 当scenario为NAVIGATION/TRAJECTORY_TRACKING/CAR_HAILING或者priority为ACCURACY时建议设置maxAccuracy为大于10的值。 当scenario为DAILY_LIFE_SERVICE/NO_POWER或者priority为LOW_POWER/FIRST_FIX时建议设置maxAccuracy为大于100的值。 |

#### CurrentLocationRequest

当前位置信息请求参数。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Location.Location.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| priority | LocationRequestPriority | 否 | 是 | 表示优先级信息。当scenario取值为UNSET时，priority参数生效，否则priority参数不生效；当scenario和priority均取值为UNSET时，无法发起定位请求。取值范围见LocationRequestPriority的定义。默认值为FIRST_FIX。 |
| scenario | LocationRequestScenario | 否 | 是 | 表示场景信息。当scenario取值为UNSET时，priority参数生效，否则priority参数不生效；当scenario和priority均取值为UNSET时，无法发起定位请求。取值范围见LocationRequestScenario的定义。默认值为UNSET。 |
| maxAccuracy | number | 否 | 是 | 应用向系统请求位置信息时要求的精度值，单位为米。该参数仅在精确位置功能场景（即同时授权了ohos.permission.APPROXIMATELY_LOCATION和ohos.permission.LOCATION 权限）下有效，模糊位置功能生效场景（即仅授权了ohos.permission.APPROXIMATELY_LOCATION 权限）下该字段无意义。 该参数生效的情况下，系统会对比GNSS或网络定位服务上报的位置信息与应用的位置信息申请。当位置信息Location中的精度值（accuracy）小于等于应用要求的精度值（maxAccuracy）时，位置信息会返回给应用；否则系统将丢弃本次收到的位置信息。 默认值为0，表示不限制位置信息的精度，取值范围为大于等于0。 当scenario为NAVIGATION/TRAJECTORY_TRACKING/CAR_HAILING或者priority为ACCURACY时建议设置maxAccuracy为大于10的值。 当scenario为DAILY_LIFE_SERVICE/NO_POWER或者priority为LOW_POWER/FIRST_FIX时建议设置maxAccuracy为大于100的值。 |
timeoutMsnumber否是表示超时时间，单位是毫秒，最小为1000毫秒。取值范围为大于等于1000。

#### ContinuousLocationRequest12+

持续定位的请求参数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Location.Location.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| interval | number | 否 | 否 | 表示上报位置信息的时间间隔，单位是秒。默认值为1，取值范围为大于等于0。等于0时对位置上报时间间隔无限制。 |
| locationScenario | UserActivityScenario | PowerConsumptionScenario | 否 | 否 | 表示定位的场景信息。取值范围见UserActivityScenario和PowerConsumptionScenario的定义。 |
| needPoi19+ | boolean | 否 | 是 | 表示是否需要获取当前位置附近的POI信息。false代表不需要获取当前位置附近的POI信息，true代表需要获取当前位置附近的POI信息。不设置时，默认值为false。 该参数仅在精确位置功能场景（即同时授权了ohos.permission.APPROXIMATELY_LOCATION和ohos.permission.LOCATION 权限）下有效，模糊位置功能生效场景（即仅授权了ohos.permission.APPROXIMATELY_LOCATION 权限）下不返回POI信息。 元服务API： 从API version 19开始，该接口支持在元服务中使用。 |

#### SingleLocationRequest12+

单次定位的请求参数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Location.Location.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| locatingPriority | LocatingPriority | 否 | 否 | 表示优先级信息。取值范围见LocatingPriority的定义。 |
| locatingTimeoutMs | number | 否 | 否 | 表示超时时间，单位是毫秒，最小为1000毫秒。取值范围为大于等于1000。 |
| needPoi19+ | boolean | 否 | 是 | 表示是否需要获取当前位置附近的POI信息。false代表不需要获取当前位置附近的POI信息，true代表需要获取当前位置附近的POI信息。不设置时，默认值为false。 该参数仅在精确位置功能场景（即同时授权了ohos.permission.APPROXIMATELY_LOCATION和ohos.permission.LOCATION 权限）下有效，模糊位置功能生效场景（即仅授权了ohos.permission.APPROXIMATELY_LOCATION 权限）下不返回POI信息。 元服务API： 从API version 19开始，该接口支持在元服务中使用。 |

#### SatelliteStatusInfo

卫星状态信息。

**系统能力**：SystemCapability.Location.Location.Gnss

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| satellitesNumber | number | 否 | 否 | 表示卫星个数。取值范围为大于等于0。 |
| satelliteIds | Array<number> | 否 | 否 | 表示每个卫星的ID，数组类型。取值范围为大于等于0。 |
| carrierToNoiseDensitys | Array<number> | 否 | 否 | 表示载波噪声功率谱密度比，即cn0。取值范围为大于0。 |
| altitudes | Array<number> | 否 | 否 | 表示卫星高度角信息。单位是“度”，取值范围为-90到90。 |
| azimuths | Array<number> | 否 | 否 | 表示方位角。单位是“度”，取值范围为0到360。 |
| carrierFrequencies | Array<number> | 否 | 否 | 表示载波频率。单位是Hz，取值范围为大于等于0。 |
| satelliteConstellation12+ | Array<SatelliteConstellationCategory> | 否 | 是 | 表示卫星星座类型。 |
| satelliteAdditionalInfo12+ | Array<number> | 否 | 是 | 表示卫星的附加信息。 每个比特位代表不同含义，具体定义参见SatelliteAdditionalInfo。 |

#### CachedGnssLocationsRequest

请求订阅GNSS缓存位置上报功能接口的配置参数。

**系统能力**：SystemCapability.Location.Location.Gnss

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| reportingPeriodSec | number | 否 | 否 | 表示GNSS缓存位置上报的周期，单位是毫秒。取值范围为大于0。 |
| wakeUpCacheQueueFull | boolean | 否 | 否 | true表示GNSS芯片底层缓存队列满之后会主动唤醒AP芯片，并把缓存位置上报给应用。 false表示GNSS芯片底层缓存队列满之后不会主动唤醒AP芯片，会把缓存位置直接丢弃。 |

#### Geofence

GNSS围栏的配置参数。目前只支持圆形围栏。

**系统能力**：SystemCapability.Location.Location.Geofence

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| latitude | number | 否 | 否 | 表示纬度。取值范围为-90到90。 |
| longitude | number | 否 | 否 | 表示经度。取值范围为-180到180。 |
| coordinateSystemType12+ | CoordinateSystemType | 否 | 是 | 表示地理围栏圆心坐标的坐标系。 APP应先使用getGeofenceSupportedCoordTypes查询支持的坐标系，然后传入正确的圆心坐标。 |
| radius | number | 否 | 否 | 表示圆形围栏的半径。单位是米，取值范围为大于0。 |
| expiration | number | 否 | 否 | 围栏存活的时间，单位是毫秒。取值范围为大于0。 |

#### GeofenceRequest

请求添加GNSS围栏消息中携带的参数，包括定位场景和围栏信息。

**系统能力**：SystemCapability.Location.Location.Geofence

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| scenario | LocationRequestScenario | 否 | 否 | 表示定位场景。 |
| geofence | Geofence | 否 | 否 | 表示围栏信息。 |

#### LocationCommand

扩展命令参数。

**系统能力**：SystemCapability.Location.Location.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| scenario | LocationRequestScenario | 否 | 否 | 表示定位场景。 |
| command | string | 否 | 否 | 扩展命令字符串，字符串长度不超过100。 |

#### Location

位置信息。

**系统能力**：SystemCapability.Location.Location.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| latitude | number | 否 | 否 | 表示纬度信息，正值表示北纬，负值表示南纬。取值范围为-90到90。仅支持WGS84坐标系。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| longitude | number | 否 | 否 | 表示经度信息，正值表示东经，负值表示西经。取值范围为-180到180。仅支持WGS84坐标系。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| altitude | number | 否 | 否 | 表示高度信息，单位米。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| accuracy | number | 否 | 否 | 表示精度信息，单位米。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| speed | number | 否 | 否 | 表示速度信息，单位米每秒。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| timeStamp | number | 否 | 否 | 表示位置时间戳，UTC格式。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| direction | number | 否 | 否 | 表示航向信息。单位是“度”，取值范围为0到360。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| timeSinceBoot | number | 否 | 否 | 表示获取位置成功的时间戳，值表示从本次开机到获取位置成功所经过的时间，单位为纳秒。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| additions | Array<string> | 否 | 是 | 附加信息。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| additionSize | number | 否 | 是 | 附加信息数量。取值范围为大于等于0。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| additionsMap12+ | Map<string, string> | 否 | 是 | 附加信息。具体内容和顺序与additions一致。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| altitudeAccuracy12+ | number | 否 | 是 | 表示高度信息的精度，单位米。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| speedAccuracy12+ | number | 否 | 是 | 表示速度信息的精度，单位米每秒。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| directionAccuracy12+ | number | 否 | 是 | 表示航向信息的精度。单位是“度”，取值范围为0到360。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| uncertaintyOfTimeSinceBoot12+ | number | 否 | 是 | 表示位置时间戳的不确定度。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| sourceType12+ | LocationSourceType | 否 | 是 | 表示定位结果的来源。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| poi19+ | PoiInfo | 否 | 是 | 表示当前位置附近的POI信息。 元服务API： 从API version 19开始，该接口支持在元服务中使用。 |

#### GeofenceTransition12+

地理围栏事件信息；包含地理围栏ID和具体的地理围栏事件。

**系统能力**：SystemCapability.Location.Location.Geofence

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| geofenceId | number | 否 | 否 | 表示地理围栏ID。 |
| transitionEvent | GeofenceTransitionEvent | 否 | 否 | 表示当前发生的地理围栏事件。 |
| beaconFence20+ | BeaconFence | 否 | 是 | beacon围栏的参数配置。仅beacon围栏使用。 从API version 20开始，支持该字段。 |

#### GnssGeofenceRequest12+

GNSS地理围栏请求参数。

**系统能力**：SystemCapability.Location.Location.Geofence

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| geofence | Geofence | 否 | 否 | 表示地理围栏信息，包含圆形围栏圆心坐标、半径等信息。 |
| monitorTransitionEvents | Array<GeofenceTransitionEvent> | 否 | 否 | 表示APP监听的地理围栏事件列表。数组长度不超过3。 |
| notifications | Array<NotificationRequest> | 否 | 是 | 表示地理围栏事件发生后弹出的通知对象列表。 monitorTransitionEvents与notifications中的顺序要一一对应，例如monitorTransitionEvents[0]为GeofenceTransitionEvent.GEOFENCE_TRANSITION_EVENT_ENTER，那notifications[0]中就需要填入用户进入围栏时需要弹出的通知对象。默认值为空数组。 |
| geofenceTransitionCallback | AsyncCallback<GeofenceTransition> | 否 | 否 | 表示用于接收地理围栏事件的回调函数。 |
| loiterTimeMs23+ | number | 否 | 是 | 徘徊时间，单位为毫秒，需关注GEOFENCE_TRANSITION_DWELL事件。若设备在多边形围栏内徘徊时间达到该值，则上报GEOFENCE_TRANSITION_DWELL事件。徘徊状态检测周期为10000毫秒。例如：设置15000，将在驻留超过20000毫秒时上报驻留状态；设置5000，将在驻留超过10000毫秒时上报驻留状态。 |
| fenceExtensionAbilityName23+ | string | 否 | 是 | FenceExtensionAbility名称，参见FenceExtensionAbility。后台拉起需要申请后台定位权限，权限申请方式参见申请位置权限开发指导。 |

#### CountryCode

国家码信息，包含国家码字符串和国家码的来源信息。

**系统能力**：SystemCapability.Location.Location.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| country | string | 否 | 否 | 表示国家码字符串。 |
| type | CountryCodeType | 否 | 否 | 表示国家码信息来源。 |

#### LocationRequestPriority

位置请求中位置信息优先级类型。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Location.Location.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| UNSET | 0x200 | 表示未设置优先级，表示LocationRequestPriority无效。 |
| ACCURACY | 0x201 | 表示精度优先。 定位精度优先策略主要以GNSS定位技术为主。我们会在GNSS提供稳定位置结果之前使用网络定位技术提供服务。在持续定位过程中，如果超过30秒无法获取GNSS定位结果则使用网络定位技术。对设备的硬件资源消耗较大，功耗较大。 |
| LOW_POWER | 0x202 | 表示低功耗优先。 低功耗定位优先策略仅使用网络定位技术，在室内和户外场景均可提供定位服务，因为其依赖周边基站、可见WLAN、蓝牙设备的分布情况，定位结果的精度波动范围较大，推荐在对定位结果精度要求不高的场景下使用该策略，可以有效节省设备功耗。 |
| FIRST_FIX | 0x203 | 表示快速获取位置优先，如果应用希望快速拿到一个位置，可以将优先级设置为该字段。 快速定位优先策略会同时使用GNSS定位和网络定位技术，以便在室内和户外场景下均可以快速获取到位置结果；当各种定位技术都有提供位置结果时，系统会选择其中精度较好的结果返回给应用。因为对各种定位技术同时使用，对设备的硬件资源消耗较大，功耗也较大。 |

#### LocationRequestScenario

位置请求中定位场景类型。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Location.Location.Core


当使用NAVIGATION/TRAJECTORY_TRACKING/CAR_HAILING场景进行单次定位或持续定位时，我们会在GNSS提供稳定位置结果之前使用网络定位技术提供服务；在持续定位时，如果超过30秒无法获取GNSS定位结果则会使用网络定位技术获取位置。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| UNSET | 0x300 | 表示未设置场景信息。 表示LocationRequestScenario字段无效。 |
| NAVIGATION | 0x301 | 表示导航场景。 适用于在户外获取设备实时位置的场景，如车载、步行导航。 主要使用GNSS定位技术提供定位服务，功耗较高。 |
| TRAJECTORY_TRACKING | 0x302 | 表示运动轨迹记录场景。 适用于记录用户位置轨迹的场景，如运动类应用记录轨迹功能。 主要使用GNSS定位技术提供定位服务，功耗较高。 |
| CAR_HAILING | 0x303 | 表示打车场景。 适用于用户出行打车时定位当前位置的场景，如网约车类应用。 主要使用GNSS定位技术提供定位服务，功耗较高。 |
| DAILY_LIFE_SERVICE | 0x304 | 表示日常服务使用场景。 适用于不需要定位用户精确位置的使用场景，如新闻资讯、网购、点餐类应用。 该场景仅使用网络定位技术提供定位服务，功耗较低。 |
NO_POWER0x305表示无功耗功场景，这种场景下不会主动触发定位，会在其他应用定位时，才给当前应用返回位置。

#### CountryCodeType

国家码来源类型。

**系统能力**：SystemCapability.Location.Location.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| COUNTRY_CODE_FROM_LOCALE | 1 | 从全球化模块的语言配置信息中获取到的国家码。 |
| COUNTRY_CODE_FROM_SIM | 2 | 从SIM卡中获取到的国家码。 |
| COUNTRY_CODE_FROM_LOCATION | 3 | 基于用户的位置信息，通过逆地理编码查询到的国家码。 |
| COUNTRY_CODE_FROM_NETWORK | 4 | 从蜂窝网络注册信息中获取到的国家码。 |

#### CoordinateSystemType12+

坐标系类型。

**系统能力**：SystemCapability.Location.Location.Geofence

| 名称 | 值 | 说明 |
| --- | --- | --- |
| WGS84 | 1 | World Geodetic System 1984，是为GPS全球定位系统使用而建立的坐标系统。 |
| GCJ02 | 2 | GCJ-02是由中国国家测绘局制订的地理信息系统的坐标系统。 |

#### GeofenceTransitionEvent12+

地理围栏事件。

**系统能力**：SystemCapability.Location.Location.Geofence

| 名称 | 值 | 说明 |
| --- | --- | --- |
| GEOFENCE_TRANSITION_EVENT_ENTER | 1 | 该事件表示设备从地理围栏外进入地理围栏内。 |
| GEOFENCE_TRANSITION_EVENT_EXIT | 2 | 该事件表示设备从地理围栏内退出到地理围栏外。 |
| GEOFENCE_TRANSITION_EVENT_DWELL | 4 | 该事件表示设备在地理围栏范围内，且持续徘徊超过10秒。 |

#### SatelliteConstellationCategory12+

卫星星座类型。

**系统能力**：SystemCapability.Location.Location.Gnss

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CONSTELLATION_CATEGORY_UNKNOWN | 0 | 默认值。 |
| CONSTELLATION_CATEGORY_GPS | 1 | GPS（Global Positioning System），即全球定位系统，是美国研制发射的一种以人造地球卫星为基础的高精度无线电导航的定位系统。 |
| CONSTELLATION_CATEGORY_SBAS | 2 | SBAS（Satellite-Based Augmentation System），即星基增强系统，通过地球静止轨道（GEO）卫星搭载卫星导航增强信号转发器，可以向用户播发星历误差、卫星钟差、电离层延迟等多种修正信息，实现对于原有卫星导航系统定位精度的改进。 |
| CONSTELLATION_CATEGORY_GLONASS | 3 | GLONASS（GLOBAL NAVIGATION SATELLITE SYSTEM），是苏联/俄罗斯研制卫星导航系统。 |
| CONSTELLATION_CATEGORY_QZSS | 4 | QZSS（Quasi-Zenith Satellite System），即准天顶卫星系统，是以三颗人造卫星透过时间转移完成全球定位系统区域性功能的卫星扩增系统，是日本研发的卫星系统。 |
| CONSTELLATION_CATEGORY_BEIDOU | 5 | 北斗卫星导航系统（Beidou Navigation Satellite System）是中国自行研制的全球卫星导航系统。 |
| CONSTELLATION_CATEGORY_GALILEO | 6 | GALILEO（Galileo satellite navigation system），即伽利略卫星导航系统，是由欧盟研制和建立的全球卫星导航定位系统。 |
| CONSTELLATION_CATEGORY_IRNSS | 7 | IRNSS（Indian Regional Navigation Satellite System），即印度区域导航卫星系统，是一个由印度空间研究组织（ISRO）发展的自由区域型卫星导航系统。 |

#### SatelliteAdditionalInfo12+

卫星附加信息类型。

**系统能力**：SystemCapability.Location.Location.Gnss

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SATELLITES_ADDITIONAL_INFO_NULL | 0 | 默认值。 |
| SATELLITES_ADDITIONAL_INFO_EPHEMERIS_DATA_EXIST | 1 | 表示本卫星具有星历数据。 |
| SATELLITES_ADDITIONAL_INFO_ALMANAC_DATA_EXIST | 2 | 表示本卫星具有年历数据。 |
| SATELLITES_ADDITIONAL_INFO_USED_IN_FIX | 4 | 表示在最新的位置解算中使用了本卫星。 |
| SATELLITES_ADDITIONAL_INFO_CARRIER_FREQUENCY_EXIST | 8 | 表示本卫星具有载波频率。 |

#### PowerConsumptionScenario12+

位置请求中的功耗场景类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Location.Location.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| HIGH_POWER_CONSUMPTION | 0x601 | 高功耗。 以GNSS定位技术为主。我们会在GNSS提供稳定位置结果之前使用网络定位技术提供服务；在持续定位时，如果超过30秒无法获取GNSS定位结果则会使用网络定位技术获取位置。对设备的硬件资源消耗较大，功耗较大。 |
| LOW_POWER_CONSUMPTION | 0x602 | 低功耗。 适用于对用户位置精度要求不高的使用场景，如新闻资讯、网购、点餐类应用。 该场景仅使用网络定位技术提供定位服务，功耗较低。 |
| NO_POWER_CONSUMPTION | 0x603 | 无功耗。 这种场景下不会主动触发定位，会在其他应用定位时，才给当前应用返回位置。 |

#### UserActivityScenario12+

位置请求中的用户活动场景类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Location.Location.Core


当使用NAVIGATION/SPORT/TRANSPORT场景进行单次定位或持续定位时，我们会在GNSS提供稳定位置结果之前使用网络定位技术提供服务；在持续定位时，如果超过30秒无法获取GNSS定位结果则会使用网络定位技术获取位置。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NAVIGATION | 0x401 | 表示导航场景。 适用于在户外获取设备实时位置的场景，如车载、步行导航。 主要使用GNSS定位技术提供定位服务，功耗较高。 |
| SPORT | 0x402 | 表示运动场景。 适用于记录用户位置轨迹的场景，如运动类应用记录轨迹功能。 主要使用GNSS定位技术提供定位服务，功耗较高。 |
| TRANSPORT | 0x403 | 表示出行场景。 适用于用户出行场景，如打车、乘坐公共交通等场景。 主要使用GNSS定位技术提供定位服务，功耗较高。 |
| DAILY_LIFE_SERVICE | 0x404 | 表示日常服务使用场景。 适用于不需要定位用户精确位置的使用场景，如新闻资讯、网购、点餐类应用。 该场景仅使用网络定位技术提供定位服务，功耗较低。 |

#### LocatingPriority12+

单次位置请求中的优先级类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Location.Location.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PRIORITY_ACCURACY | 0x501 | 表示精度优先。 定位精度优先策略会同时使用GNSS定位和网络定位技术，并把一段时间内精度较好的结果返回给应用；这个时间段长度为SingleLocationRequest.locatingTimeoutMs与“30秒”中的较小者。 对设备的硬件资源消耗较大，功耗较大。 |
| PRIORITY_LOCATING_SPEED | 0x502 | 表示快速获取位置优先，如果应用希望快速拿到一个位置，可以将优先级设置为该类型。 快速定位优先策略会同时使用GNSS定位和网络定位技术，以便在室内和户外场景下均可以快速获取到位置结果，我们会把最先拿到的定位结果返回给应用。对设备的硬件资源消耗较大，功耗也较大。 |

#### LocationError12+

持续定位过程中的错误信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Location.Location.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| LOCATING_FAILED_DEFAULT | -1 | 默认值。 |
| LOCATING_FAILED_LOCATION_PERMISSION_DENIED | -2 | 表示ohos.permission.APPROXIMATELY_LOCATION权限或ohos.permission.LOCATION权限校验失败导致持续定位失败。 |
| LOCATING_FAILED_BACKGROUND_PERMISSION_DENIED | -3 | 表示应用在后台时位置权限校验失败导致持续定位失败。APP在后台定位时的位置权限申请方式参见申请位置权限开发指导。 |
| LOCATING_FAILED_LOCATION_SWITCH_OFF | -4 | 表示位置信息开关关闭导致持续定位失败。 |
| LOCATING_FAILED_INTERNET_ACCESS_FAILURE | -5 | 表示无法访问网络，导致网络定位失败。 |

#### LocationSourceType12+

定位结果的来源。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Location.Location.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| GNSS | 1 | 表示定位结果来自于GNSS定位技术。 |
| NETWORK | 2 | 表示定位结果来自于网络定位技术。 |
| INDOOR | 3 | 表示定位结果来自于室内高精度定位技术。 |
| RTK | 4 | 表示定位结果来自于室外高精度定位技术。 |

#### BluetoothScanResult16+

蓝牙扫描结果。

**系统能力**：SystemCapability.Location.Location.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| deviceId | string | 否 | 否 | 表示扫描到的设备地址。例如："XX:XX:XX:XX:XX:XX"。 |
| rssi | number | 否 | 否 | 表示扫描到的设备的rssi值。 |
| data | ArrayBuffer | 否 | 是 | 表示扫描到的设备发送的广播包。 |
| deviceName | string | 否 | 否 | 表示扫描到的设备名称。 |
| connectable | boolean | 否 | 否 | 表示扫描到的设备是否可连接。true表示可连接，false表示不可连接。 |

#### Poi19+

POI(Point of Interest, 兴趣点)信息。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Location.Location.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| id | string | 否 | 否 | 表示POI的ID。 |
| confidence | number | 否 | 否 | 表示POI信息的置信度。置信度越高，用户离该POI信息点越近。取值范围为0到1。 |
| name | string | 否 | 否 | 表示POI的名称。 |
| latitude | number | 否 | 否 | 表示POI所在的纬度。取值范围为-90到90。 |
| longitude | number | 否 | 否 | 表示POI所在的经度。取值范围为-180到180。 |
| administrativeArea | string | 否 | 否 | 表示POI所在的国家以下的一级行政区，一般是省/州。 |
| subAdministrativeArea | string | 否 | 否 | 表示POI所在的国家以下的二级行政区，一般是市。 |
| locality | string | 否 | 否 | 表示POI所在的城市信息，一般是市。 |
| subLocality | string | 否 | 否 | 表示POI所在的子城市信息，一般是区/县。 |
| address | string | 否 | 否 | 表示POI的详细地址。 |

#### PoiInfo19+

POI信息结构体。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Location.Location.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| poiArray | Array<Poi> | 否 | 否 | 表示POI信息列表。 |
| timestamp | number | 否 | 否 | 表示获取到POI信息时的时间戳，UTC时间，单位毫秒。 |

#### SportsType18+

运动类型。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Location.Location.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| RUNNING | 1 | 表示跑步。 |
| WALKING | 2 | 表示步行。 |
| CYCLING | 3 | 表示骑行。 |

#### BeaconFenceInfoType20+

beacon围栏信息类型。当前仅支持设备制造商数据过滤。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Location.Location.Geofence

| 名称 | 值 | 说明 |
| --- | --- | --- |
| BEACON_MANUFACTURE_DATA | 1 | 标识使用beacon设备制造商数据。 |

#### BeaconManufactureData20+

beacon设备制造商数据。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Location.Location.Geofence

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| manufactureId | number | 否 | 否 | 制造商标识。 |
| manufactureData | ArrayBuffer | 否 | 否 | 厂商自定义数据。例如：[0x02,0x15,0x00...0xFF,0x11,0x22,0x33,0x44,0x55] |
| manufactureDataMask | ArrayBuffer | 否 | 否 | 搭配manufactureData使用，可设置过滤部分制造商数据，0xFF为全匹配，0x00为模糊匹配。例如：[0xFF,0xFF,0xFF...0xFF,0xFF,0xFF,0xFF,0xFF,0xFF] |

#### BeaconFence20+

beacon围栏的参数配置。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Location.Location.Geofence

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| identifier | string | 否 | 否 | beacon围栏标识。可自行定义，如："123", "beaconName"。 |
| beaconFenceInfoType | BeaconFenceInfoType | 否 | 否 | beacon围栏信息类型。 |
| manufactureData | BeaconManufactureData | 否 | 是 | beacon设备制造商数据。 |

#### BeaconFenceRequest20+

beacon围栏请求参数。transitionCallback与fenceExtensionAbilityName任选其一，都不填则参数无效。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Location.Location.Geofence

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| beacon | BeaconFence | 否 | 否 | beacon围栏的参数配置。 |
| transitionCallback | Callback<GeofenceTransition> | 否 | 是 | beacon围栏事件信息。仅支持前台回调。 |
| fenceExtensionAbilityName | string | 否 | 是 | FenceExtensionAbility名称。 |

#### geoLocationManager.on('locationChange')

on(type: 'locationChange', request: LocationRequest | ContinuousLocationRequest, callback: Callback<Location>): void

开启位置变化订阅，并发起定位请求。使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**需要权限**：ohos.permission.APPROXIMATELY_LOCATION

**系统能力**：SystemCapability.Location.Location.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置事件类型。type为“locationChange”，表示位置变化。 |
| request | LocationRequest | ContinuousLocationRequest | 是 | 设置位置请求参数。 ContinuousLocationRequest为API12新增参数。 |
| callback | Callback<Location> | 是 | 回调函数，返回位置信息。 |

**错误码**：

以下错误码的详细介绍请参见[位置服务子系统错误码](位置服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call ${geoLocationManager.on('locationChange')} due to limited device capabilities. |
| 3301000 | The location service is unavailable. |
| 3301100 | The location switch is off. |

**示例**

```ets
import { geoLocationManager } from '@kit.LocationKit';

// 方式一：使用LocationRequest作为入参
let requestInfo: geoLocationManager.LocationRequest = {
  'priority': geoLocationManager.LocationRequestPriority.FIRST_FIX,
  'scenario': geoLocationManager.LocationRequestScenario.UNSET,
  'timeInterval': 1,
  'distanceInterval': 0,
  'maxAccuracy': 0
};
let locationChange = (location:geoLocationManager.Location):void => {
    console.info('locationChange: data: ' + JSON.stringify(location));
};
try {
    geoLocationManager.on('locationChange', requestInfo, locationChange);
} catch (err) {
    console.error("errCode:" + err.code + ", message:"  + err.message);
}

// 方式二：使用ContinuousLocationRequest作为入参
let request: geoLocationManager.ContinuousLocationRequest = {
  'interval': 1,
  'locationScenario': geoLocationManager.UserActivityScenario.NAVIGATION
};
let locationCallback = (location:geoLocationManager.Location):void => {
    console.info('locationCallback: data: ' + JSON.stringify(location));
};
try {
    geoLocationManager.on('locationChange', request, locationCallback);
} catch (err) {
    console.error("errCode:" + err.code + ", message:"  + err.message);
}
```

#### geoLocationManager.off('locationChange')

off(type: 'locationChange', callback?: Callback<Location>): void

关闭位置变化订阅，并删除对应的定位请求。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**需要权限**：ohos.permission.APPROXIMATELY_LOCATION

**系统能力**：SystemCapability.Location.Location.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置事件类型。type为“locationChange”，表示位置变化。 |
| callback | Callback<Location> | 否 | 需要取消订阅的回调函数。该回调函数需要与on接口传入的回调函数保持一致。若无此参数，则取消当前类型的所有订阅。 |

**错误码**：

以下错误码的详细介绍请参见[位置服务子系统错误码](位置服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call ${geoLocationManager.off('locationChange')} due to limited device capabilities. |
| 3301000 | The location service is unavailable. |

**示例**

```ets
import { geoLocationManager } from '@kit.LocationKit';

let requestInfo: geoLocationManager.LocationRequest = {
  'priority': geoLocationManager.LocationRequestPriority.FIRST_FIX,
  'scenario': geoLocationManager.LocationRequestScenario.UNSET,
  'timeInterval': 1,
  'distanceInterval': 0,
  'maxAccuracy': 0
};
let locationChange = (location:geoLocationManager.Location):void => {
  console.info('locationChange: data: ' + JSON.stringify(location));
};
try {
    geoLocationManager.on('locationChange', requestInfo, locationChange);
    geoLocationManager.off('locationChange', locationChange);
} catch (err) {
    console.error("errCode:" + err.code + ", message:"  + err.message);
}
```

#### geoLocationManager.on('locationError')12+

on(type: 'locationError', callback: Callback<LocationError>): void

订阅持续定位过程中的错误码。使用callback异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**需要权限**：ohos.permission.APPROXIMATELY_LOCATION

**系统能力**：SystemCapability.Location.Location.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置事件类型。type为“locationError”，表示持续定位过程中的错误码变化。 |
| callback | Callback<LocationError> | 是 | 回调函数，返回持续定位过程中的错误码。 |

**错误码**：

以下错误码的详细介绍请参见[位置服务子系统错误码](位置服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call ${geoLocationManager.on('locationError')} due to limited device capabilities. |
| 3301000 | The location service is unavailable. |

**示例**

```ets
import { geoLocationManager } from '@kit.LocationKit';

let requestInfo: geoLocationManager.LocationRequest = {
  'priority': geoLocationManager.LocationRequestPriority.FIRST_FIX,
  'scenario': geoLocationManager.LocationRequestScenario.UNSET,
  'timeInterval': 1,
  'distanceInterval': 0,
  'maxAccuracy': 0
};
let locationChange = (location:geoLocationManager.Location):void => {
    console.info('locationChange: data: ' + JSON.stringify(location));
};
try {
    geoLocationManager.on('locationChange', requestInfo, locationChange);
} catch (err) {
    console.error("errCode:" + err.code + ", message:"  + err.message);
}

let locationErrorChange = (errcode: geoLocationManager.LocationError):void => {
  console.info('locationErrorChange: data: ' + JSON.stringify(errcode));
};
try {
  geoLocationManager.on('locationError', locationErrorChange);
} catch (err) {
  console.error("errCode:" + err.code + ", message:"  + err.message);
}
```

#### geoLocationManager.off('locationError')12+

off(type: 'locationError', callback?: Callback<LocationError>): void

取消订阅持续定位过程中的错误码。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**需要权限**：ohos.permission.APPROXIMATELY_LOCATION

**系统能力**：SystemCapability.Location.Location.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置事件类型。type为“locationError”，表示持续定位过程中的错误码变化。 |
| callback | Callback<LocationError> | 否 | 需要取消订阅的回调函数。该回调函数需要与on接口传入的回调函数保持一致。若无此参数，则取消当前类型的所有订阅。 |

**错误码**：

以下错误码的详细介绍请参见[位置服务子系统错误码](位置服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call ${geoLocationManager.off('locationError')} due to limited device capabilities. |
| 3301000 | The location service is unavailable. |

**示例**

```ets
import { geoLocationManager } from '@kit.LocationKit';

let locationErrorChange = (errcode: geoLocationManager.LocationError):void => {
  console.info('locationErrorChange: data: ' + JSON.stringify(errcode));
};
try {
  geoLocationManager.on('locationError', locationErrorChange);
  geoLocationManager.off('locationError', locationErrorChange);
} catch (err) {
  console.error("errCode:" + err.code + ", message:"  + err.message);
}
```

#### geoLocationManager.on('locationEnabledChange')

on(type: 'locationEnabledChange', callback: Callback<boolean>): void

订阅位置服务状态变化。使用callback异步回调。

**系统能力**：SystemCapability.Location.Location.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置事件类型。type为“locationEnabledChange”，表示位置服务状态。 |
| callback | Callback<boolean> | 是 | 回调函数。返回true表示位置信息开关已经开启；返回false表示位置信息开关已经关闭。 |

**错误码**：

以下错误码的详细介绍请参见[位置服务子系统错误码](位置服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call ${geoLocationManager.on('locationEnabledChange')} due to limited device capabilities. |
| 3301000 | The location service is unavailable. |

**示例**

```ets
import { geoLocationManager } from '@kit.LocationKit';

let locationEnabledChange = (state:boolean):void => {
    console.info('locationEnabledChange: ' + JSON.stringify(state));
}
try {
    geoLocationManager.on('locationEnabledChange', locationEnabledChange);
} catch (err) {
    console.error("errCode:" + err.code + ", message:"  + err.message);
}
```

#### geoLocationManager.off('locationEnabledChange')

off(type: 'locationEnabledChange', callback?: Callback<boolean>): void

取消订阅位置服务状态变化。

**系统能力**：SystemCapability.Location.Location.Core

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置事件类型。type为“locationEnabledChange”，表示位置服务状态。 |
| callback | Callback<boolean> | 否 | 需要取消订阅的回调函数。返回true表示位置信息开关已经开启；返回false表示位置信息开关已经关闭。该回调函数需要与on接口传入的回调函数保持一致。若无此参数，则取消当前类型的所有订阅。 |

**错误码**：

以下错误码的详细介绍请参见[位置服务子系统错误码](位置服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call ${geoLocationManager.off('locationEnabledChange')} due to limited device capabilities. |
| 3301000 | The location service is unavailable. |

**示例**

```ets
import { geoLocationManager } from '@kit.LocationKit';

let locationEnabledChange = (state:boolean):void => {
    console.info('locationEnabledChange: state: ' + JSON.stringify(state));
}
try {
    geoLocationManager.on('locationEnabledChange', locationEnabledChange);
    geoLocationManager.off('locationEnabledChange', locationEnabledChange);
} catch (err) {
    console.error("errCode:" + err.code + ", message:"  + err.message);
}
```

#### geoLocationManager.on('cachedGnssLocationsChange')

on(type: 'cachedGnssLocationsChange', request: CachedGnssLocationsRequest, callback: Callback<Array<Location>>): void

订阅缓存GNSS定位结果上报事件。该接口功能由GNSS定位芯片提供（仅部分型号支持），如果设备无此芯片或使用的芯片型号不支持该功能，则返回错误码801（Capability not supported）。使用callback异步回调。

**需要权限**：ohos.permission.APPROXIMATELY_LOCATION

**系统能力**：SystemCapability.Location.Location.Gnss

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置事件类型。type为“cachedGnssLocationsChange”，表示GNSS缓存定位结果上报。 |
| request | CachedGnssLocationsRequest | 是 | GNSS缓存功能配置参数。 |
| callback | Callback<Array<Location>> | 是 | 回调函数，返回GNSS缓存位置。 |

**错误码**：

以下错误码的详细介绍请参见[位置服务子系统错误码](位置服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call ${geoLocationManager.on('cachedGnssLocationsChange')} due to limited device capabilities. |
| 3301000 | The location service is unavailable. |
| 3301100 | The location switch is off. |

**示例**

```ets
import { geoLocationManager } from '@kit.LocationKit';

let cachedLocationsCb = (locations:Array<geoLocationManager.Location>):void => {
    console.info('cachedGnssLocationsChange: locations: ' + JSON.stringify(locations));
}
let requestInfo: geoLocationManager.CachedGnssLocationsRequest = {
  'reportingPeriodSec': 10,
  'wakeUpCacheQueueFull': true
};
try {
    geoLocationManager.on('cachedGnssLocationsChange', requestInfo, cachedLocationsCb);
} catch (err) {
    console.error("errCode:" + err.code + ", message:"  + err.message);
}
```

#### geoLocationManager.off('cachedGnssLocationsChange')

off(type: 'cachedGnssLocationsChange', callback?: Callback<Array<Location>>): void

取消订阅缓存GNSS定位结果上报事件。该接口功能由GNSS定位芯片提供（仅部分型号支持），如果设备无此芯片或使用的芯片型号不支持该功能，则返回错误码801（Capability not supported）。

**需要权限**：ohos.permission.APPROXIMATELY_LOCATION

**系统能力**：SystemCapability.Location.Location.Gnss

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置事件类型。type为“cachedGnssLocationsChange”，表示GNSS缓存定位结果上报。 |
| callback | Callback<Array<Location>> | 否 | 需要取消订阅的回调函数。该回调函数需要与on接口传入的回调函数保持一致。若无此参数，则取消当前类型的所有订阅。 |

**错误码**：

以下错误码的详细介绍请参见[位置服务子系统错误码](位置服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call ${geoLocationManager.off('cachedGnssLocationsChange')} due to limited device capabilities. |
| 3301000 | The location service is unavailable. |
| 3301100 | The location switch is off. |

**示例**

```ets
import { geoLocationManager } from '@kit.LocationKit';

let cachedLocationsCb = (locations:Array<geoLocationManager.Location>):void => {
    console.info('cachedGnssLocationsChange: locations: ' + JSON.stringify(locations));
}
let requestInfo: geoLocationManager.CachedGnssLocationsRequest = {
  'reportingPeriodSec': 10,
  'wakeUpCacheQueueFull': true
};
try {
    geoLocationManager.on('cachedGnssLocationsChange', requestInfo, cachedLocationsCb);
    geoLocationManager.off('cachedGnssLocationsChange');
} catch (err) {
    console.error("errCode:" + err.code + ", message:"  + err.message);
}
```

#### geoLocationManager.on('satelliteStatusChange')

on(type: 'satelliteStatusChange', callback: Callback<SatelliteStatusInfo>): void

订阅GNSS卫星状态信息上报事件。使用callback异步回调。

**需要权限**：ohos.permission.APPROXIMATELY_LOCATION

**系统能力**：SystemCapability.Location.Location.Gnss

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置事件类型。type为“satelliteStatusChange”，表示订阅GNSS卫星状态信息上报。 |
| callback | Callback<SatelliteStatusInfo> | 是 | 回调函数，返回GNSS卫星状态信息。 |

**错误码**：

以下错误码的详细介绍请参见[位置服务子系统错误码](位置服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call ${geoLocationManager.on('satelliteStatusChange')} due to limited device capabilities. |
| 3301000 | The location service is unavailable. |
| 3301100 | The location switch is off. |

**示例**

```ets
import { geoLocationManager } from '@kit.LocationKit';

let gnssStatusCb = (satelliteStatusInfo:geoLocationManager.SatelliteStatusInfo):void => {
    console.info('satelliteStatusChange: ' + JSON.stringify(satelliteStatusInfo));
    // 表示卫星个数
    let totalNumber: number = satelliteStatusInfo.satellitesNumber;
    let satelliteIds: Array<number> = satelliteStatusInfo.satelliteIds;
    let carrierToNoiseDensitys: Array<number> = satelliteStatusInfo.carrierToNoiseDensitys;
    let altitudes: Array<number> = satelliteStatusInfo.altitudes;
    let azimuths: Array<number> = satelliteStatusInfo.azimuths;
    let carrierFrequencies: Array<number> = satelliteStatusInfo.carrierFrequencies;
    let satelliteConstellations: Array<geoLocationManager.SatelliteConstellationCategory> | undefined = satelliteStatusInfo.satelliteConstellation;
    let satelliteAdditionalInfos: Array<number> | undefined = satelliteStatusInfo.satelliteAdditionalInfo;
    for (let i = 0;i < totalNumber;i++) {
      // 卫星的ID
      let satelliteId: number = satelliteIds[i];
      // 表示卫星的ID为 ${satelliteId} 的卫星的载波噪声功率谱密度比
      let carrierToNoiseDensity: number = carrierToNoiseDensitys[i];
      // 表示卫星的ID为 ${satelliteId} 的卫星的高度角信息
      let altitude: number = altitudes[i];
      // 表示卫星的ID为 ${satelliteId} 的卫星的方位角
      let azimuth: number = azimuths[i];
      // 表示卫星的ID为 ${satelliteId} 的卫星的载波频率
    let carrierFrequency: number = carrierFrequencies[i];
      if (satelliteConstellations != undefined) {
        // 表示卫星的ID为 ${satelliteId} 的卫星的星座类型
        let satelliteConstellation: geoLocationManager.SatelliteConstellationCategory = satelliteConstellations[i];
      }
      if (satelliteAdditionalInfos != undefined) {
        // 表示卫星的ID为 ${satelliteId} 的卫星的附加信息；表示是否在最新的位置解算中使用了本卫星，是否具有星历数据，是否具有年历数据，是否具有载波频率信息等。
        let satelliteAdditionalInfo: number = satelliteAdditionalInfos[i];
}

try {
    geoLocationManager.on('satelliteStatusChange', gnssStatusCb);
} catch (err) {
    console.error("errCode:" + err.code + ", message:"  + err.message);
}
```

#### geoLocationManager.off('satelliteStatusChange')

off(type: 'satelliteStatusChange', callback?: Callback<SatelliteStatusInfo>): void

取消订阅GNSS卫星状态信息上报事件。

**需要权限**：ohos.permission.APPROXIMATELY_LOCATION

**系统能力**：SystemCapability.Location.Location.Gnss

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置事件类型。type为“satelliteStatusChange”，表示订阅GNSS卫星状态信息上报。 |
| callback | Callback<SatelliteStatusInfo> | 否 | 需要取消订阅的回调函数。该回调函数需要与on接口传入的回调函数保持一致。若无此参数，则取消当前类型的所有订阅。 |

**错误码**：

以下错误码的详细介绍请参见[位置服务子系统错误码](位置服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call ${geoLocationManager.off('satelliteStatusChange')} due to limited device capabilities. |
| 3301000 | The location service is unavailable. |
| 3301100 | The location switch is off. |

**示例**

```ets
import { geoLocationManager } from '@kit.LocationKit';

let gnssStatusCb = (satelliteStatusInfo:geoLocationManager.SatelliteStatusInfo):void => {
    console.info('satelliteStatusChange: ' + JSON.stringify(satelliteStatusInfo));
}
try {
    geoLocationManager.on('satelliteStatusChange', gnssStatusCb);
    geoLocationManager.off('satelliteStatusChange', gnssStatusCb);
} catch (err) {
    console.error("errCode:" + err.code + ", message:"  + err.message);
}
```

#### geoLocationManager.on('nmeaMessage')

on(type: 'nmeaMessage', callback: Callback<string>): void

订阅GNSS NMEA信息上报事件。使用callback异步回调。

**需要权限**：ohos.permission.LOCATION 和 ohos.permission.APPROXIMATELY_LOCATION

**系统能力**：SystemCapability.Location.Location.Gnss

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置事件类型。type为“nmeaMessage”，表示订阅GNSS NMEA信息上报。 |
| callback | Callback<string> | 是 | 回调函数，返回GNSS NMEA信息。 |

**错误码**：

以下错误码的详细介绍请参见[位置服务子系统错误码](位置服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call ${geoLocationManager.on('nmeaMessage')} due to limited device capabilities. |
| 3301000 | The location service is unavailable. |
| 3301100 | The location switch is off. |

**示例**

```ets
import { geoLocationManager } from '@kit.LocationKit';

let nmeaCb = (str:string):void => {
    console.info('nmeaMessage: ' + JSON.stringify(str));
}

try {
    geoLocationManager.on('nmeaMessage', nmeaCb );
} catch (err) {
    console.error("errCode:" + err.code + ", message:"  + err.message);
}
```

#### geoLocationManager.off('nmeaMessage')

off(type: 'nmeaMessage', callback?: Callback<string>): void

取消订阅GNSS NMEA信息上报事件。

**需要权限**：ohos.permission.LOCATION 和 ohos.permission.APPROXIMATELY_LOCATION

**系统能力**：SystemCapability.Location.Location.Gnss

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置事件类型。type为“nmeaMessage”，表示订阅GNSS NMEA信息上报。 |
| callback | Callback<string> | 否 | 需要取消订阅的回调函数。该回调函数需要与on接口传入的回调函数保持一致。若无此参数，则取消当前类型的所有订阅。 |

**错误码**：

以下错误码的详细介绍请参见[位置服务子系统错误码](位置服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call ${geoLocationManager.off('nmeaMessage')} due to limited device capabilities. |
| 3301000 | The location service is unavailable. |
| 3301100 | The location switch is off. |

**示例**

```ets
import { geoLocationManager } from '@kit.LocationKit';

let nmeaCb = (str:string):void => {
    console.info('nmeaMessage: ' + JSON.stringify(str));
}

try {
    geoLocationManager.on('nmeaMessage', nmeaCb);
    geoLocationManager.off('nmeaMessage', nmeaCb);
} catch (err) {
    console.error("errCode:" + err.code + ", message:"  + err.message);
}
```

#### geoLocationManager.on('gnssFenceStatusChange')

on(type: 'gnssFenceStatusChange', request: GeofenceRequest, want: WantAgent): void

添加一个围栏，并订阅地理围栏事件。该接口功能由GNSS定位芯片提供（仅部分型号支持），如果设备无此芯片或使用的芯片型号不支持该功能，则返回错误码801（Capability not supported）。

**需要权限**：ohos.permission.APPROXIMATELY_LOCATION

**系统能力**：SystemCapability.Location.Location.Geofence

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置事件类型。type为“gnssFenceStatusChange”，表示订阅围栏事件上报。 |
| request | GeofenceRequest | 是 | 围栏的配置参数。 |
| want | WantAgent | 是 | 用于接收地理围栏事件上报（进出围栏）。 |

**错误码**：

以下错误码的详细介绍请参见[位置服务子系统错误码](位置服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call ${geoLocationManager.on('gnssFenceStatusChange')} due to limited device capabilities. |
| 3301000 | The location service is unavailable. |
| 3301100 | The location switch is off. |
| 3301600 | Failed to operate the geofence. |

**示例**

```ets
import { geoLocationManager } from '@kit.LocationKit';
import { wantAgent } from '@kit.AbilityKit';

let wantAgentInfo:wantAgent.WantAgentInfo = {
    wants: [
        {
            bundleName: "com.example.myapplication",
            abilityName: "EntryAbility",
            action: "action1"
        }
    ],
    actionType: wantAgent.OperationType.START_ABILITY,
    requestCode: 0,
    wantAgentFlags: [wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
};

wantAgent.getWantAgent(wantAgentInfo).then((wantAgentObj) => {
  let requestInfo: geoLocationManager.GeofenceRequest = {
    'scenario': 0x301,
    "geofence": { "latitude": 31.12, "longitude": 121.11, "radius": 100, "expiration": 10000 }
  };
  try {
      geoLocationManager.on('gnssFenceStatusChange', requestInfo, wantAgentObj);
  } catch (err) {
      console.error("errCode:" + err.code + ", message:"  + err.message);
  }
});
```

#### geoLocationManager.off('gnssFenceStatusChange')

off(type: 'gnssFenceStatusChange', request: GeofenceRequest, want: WantAgent): void

删除一个围栏，并取消订阅该围栏事件。该接口功能由GNSS定位芯片提供（仅部分型号支持），如果设备无此芯片或使用的芯片型号不支持该功能，则返回错误码801（Capability not supported）。

**需要权限**：ohos.permission.APPROXIMATELY_LOCATION

**系统能力**：SystemCapability.Location.Location.Geofence

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置事件类型。type为“gnssFenceStatusChange”，表示订阅围栏事件上报。 |
| request | GeofenceRequest | 是 | 围栏的配置参数。 |
| want | WantAgent | 是 | 用于接收地理围栏事件上报（进出围栏）。 |

**错误码**：

以下错误码的详细介绍请参见[位置服务子系统错误码](位置服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call ${geoLocationManager.off('gnssFenceStatusChange')} due to limited device capabilities. |
| 3301000 | The location service is unavailable. |
| 3301100 | The location switch is off. |
| 3301600 | Failed to operate the geofence. |

**示例**

```ets
import { geoLocationManager } from '@kit.LocationKit';
import { wantAgent } from '@kit.AbilityKit';

let wantAgentInfo:wantAgent.WantAgentInfo = {
    wants: [
        {
            bundleName: "com.example.myapplication",
            abilityName: "EntryAbility",
            action: "action1",
        }
    ],
    actionType: wantAgent.OperationType.START_ABILITY,
    requestCode: 0,
    wantAgentFlags: [wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
};

wantAgent.getWantAgent(wantAgentInfo).then((wantAgentObj) => {
  let requestInfo: geoLocationManager.GeofenceRequest = {
    'scenario': 0x301,
    "geofence": { "latitude": 31.12, "longitude": 121.11, "radius": 100, "expiration": 10000 }
  };
  try {
      geoLocationManager.on('gnssFenceStatusChange', requestInfo, wantAgentObj);
      geoLocationManager.off('gnssFenceStatusChange', requestInfo, wantAgentObj);
  } catch (err) {
      console.error("errCode:" + err.code + ", message:"  + err.message);
  }
});
```

#### geoLocationManager.on('countryCodeChange')

on(type: 'countryCodeChange', callback: Callback<CountryCode>): void

订阅国家码信息变化事件。使用callback异步回调。

**系统能力**：SystemCapability.Location.Location.Core

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置事件类型。type为“countryCodeChange”，表示订阅国家码信息变化事件。 |
| callback | Callback<CountryCode> | 是 | 回调函数，返回国家码信息。 |

**错误码**：

以下错误码的详细介绍请参见[位置服务子系统错误码](位置服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call ${geoLocationManager.on('countryCodeChange')} due to limited device capabilities. |
| 3301000 | The location service is unavailable. |
| 3301500 | Failed to query the area information. |

**示例**

```ets
import { geoLocationManager } from '@kit.LocationKit';

let callback = (code:geoLocationManager.CountryCode):void => {
    console.info('countryCodeChange: ' + JSON.stringify(code));
}

try {
    geoLocationManager.on('countryCodeChange', callback);
} catch (err) {
    console.error("errCode:" + err.code + ", message:"  + err.message);
}
```

#### geoLocationManager.off('countryCodeChange')

off(type: 'countryCodeChange', callback?: Callback<CountryCode>): void

取消订阅国家码变化事件。

**系统能力**：SystemCapability.Location.Location.Core

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置事件类型。type为“countryCodeChange”，表示取消订阅国家码信息变化事件。 |
| callback | Callback<CountryCode> | 否 | 需要取消订阅的回调函数。该回调函数需要与on接口传入的回调函数保持一致。若无此参数，则取消当前类型的所有订阅。 |

**错误码**：

以下错误码的详细介绍请参见[位置服务子系统错误码](位置服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call ${geoLocationManager.off('countryCodeChange')} due to limited device capabilities. |
| 3301000 | The location service is unavailable. |
| 3301500 | Failed to query the area information. |

**示例**

```ets
import { geoLocationManager } from '@kit.LocationKit';

let callback = (code:geoLocationManager.CountryCode):void => {
    console.info('countryCodeChange: ' + JSON.stringify(code));
}

try {
    geoLocationManager.on('countryCodeChange', callback);
    geoLocationManager.off('countryCodeChange', callback);
} catch (err) {
    console.error("errCode:" + err.code + ", message:"  + err.message);
}
```

#### geoLocationManager.getCurrentLocation

getCurrentLocation(request: CurrentLocationRequest | SingleLocationRequest, callback: AsyncCallback<Location>): void

获取当前位置，使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**需要权限**：ohos.permission.APPROXIMATELY_LOCATION

**系统能力**：SystemCapability.Location.Location.Core

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| request | CurrentLocationRequest | SingleLocationRequest | 是 | 设置位置请求参数。 SingleLocationRequest为API12新增参数。 |
| callback | AsyncCallback<Location> | 是 | 回调函数，返回当前位置信息。 |

**错误码**：

以下错误码的详细介绍请参见[位置服务子系统错误码](位置服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call ${geoLocationManager.getCurrentLocation} due to limited device capabilities. |
| 3301000 | The location service is unavailable. |
| 3301100 | The location switch is off. |
| 3301200 | Failed to obtain the geographical location. |

**示例**

```ets
import { geoLocationManager } from '@kit.LocationKit';
import { BusinessError } from '@kit.BasicServicesKit';
// 方式一：使用CurrentLocationRequest作为入参
let requestInfo: geoLocationManager.CurrentLocationRequest = {
  'priority': geoLocationManager.LocationRequestPriority.FIRST_FIX,
  'scenario': geoLocationManager.LocationRequestScenario.UNSET,
  'maxAccuracy': 0
};
let locationChange = (err:BusinessError, location:geoLocationManager.Location):void => {
    if (err) {
        console.error('locationChange: err=' + JSON.stringify(err));
    }
    if (location) {
        console.info('locationChange: location=' + JSON.stringify(location));
    }
};

try {
    geoLocationManager.getCurrentLocation(requestInfo, locationChange);
} catch (err) {
    console.error("errCode:" + err.code + ", message:"  + err.message);
}

// 方式二：使用SingleLocationRequest作为入参
let request: geoLocationManager.SingleLocationRequest = {
  'locatingTimeoutMs': 10000,
  'locatingPriority': geoLocationManager.LocatingPriority.PRIORITY_ACCURACY
};
let locationCallback = (err:BusinessError, location:geoLocationManager.Location):void => {
    if (err) {
        console.error('locationChange: err=' + JSON.stringify(err));
    }
    if (location) {
        console.info('locationChange: location=' + JSON.stringify(location));
    }
};

try {
    geoLocationManager.getCurrentLocation(request, locationCallback);
} catch (err) {
    console.error("errCode:" + err.code + ", message:"  + err.message);
}
```

#### geoLocationManager.getCurrentLocation

getCurrentLocation(callback: AsyncCallback<Location>): void

获取当前位置，使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**需要权限**：ohos.permission.APPROXIMATELY_LOCATION

**系统能力**：SystemCapability.Location.Location.Core

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<Location> | 是 | 回调函数，返回当前位置信息。 |

**错误码**：

以下错误码的详细介绍请参见[位置服务子系统错误码](位置服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call ${geoLocationManager.getCurrentLocation} due to limited device capabilities. |
| 3301000 | The location service is unavailable. |
| 3301100 | The location switch is off. |
| 3301200 | Failed to obtain the geographical location. |

**示例**

```ets
import { geoLocationManager } from '@kit.LocationKit';
import { BusinessError } from '@kit.BasicServicesKit';
let locationChange = (err:BusinessError, location:geoLocationManager.Location) => {
    if (err) {
        console.error('locationChange: err=' + JSON.stringify(err));
    }
    if (location) {
        console.info('locationChange: location=' + JSON.stringify(location));
    }
};

try {
    geoLocationManager.getCurrentLocation(locationChange);
} catch (err) {
    console.error("errCode:" + err.code + ", message:"  + err.message);
}
```

#### geoLocationManager.getCurrentLocation

getCurrentLocation(request?: CurrentLocationRequest | SingleLocationRequest): Promise<Location>

获取当前位置，使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**需要权限**：ohos.permission.APPROXIMATELY_LOCATION

**系统能力**：SystemCapability.Location.Location.Core

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| request | CurrentLocationRequest | SingleLocationRequest | 否 | 设置位置请求参数。 SingleLocationRequest为API12新增参数。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<Location> | Promise对象，返回当前位置信息。 |

**错误码**：

以下错误码的详细介绍请参见[位置服务子系统错误码](位置服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call ${geoLocationManager.getCurrentLocation} due to limited device capabilities. |
| 3301000 | The location service is unavailable. |
| 3301100 | The location switch is off. |
| 3301200 | Failed to obtain the geographical location. |

**示例**

```ets
import { geoLocationManager } from '@kit.LocationKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 方式一：使用CurrentLocationRequest作为入参
let requestInfo: geoLocationManager.CurrentLocationRequest = {
  'priority': geoLocationManager.LocationRequestPriority.FIRST_FIX,
  'scenario': geoLocationManager.LocationRequestScenario.UNSET,
  'maxAccuracy': 0
};
try {
    geoLocationManager.getCurrentLocation(requestInfo).then((result) => {
        console.info('current location: ' + JSON.stringify(result));
    })
    .catch((error:BusinessError) => {
        console.error('promise, getCurrentLocation: error=' + JSON.stringify(error));
    });
} catch (err) {
    console.error("errCode:" + err.code + ", message:"  + err.message);
}

// 方式二：使用SingleLocationRequest作为入参
let request: geoLocationManager.SingleLocationRequest = {
  'locatingTimeoutMs': 10000,
  'locatingPriority': geoLocationManager.LocatingPriority.PRIORITY_ACCURACY
};
try {
    geoLocationManager.getCurrentLocation(request).then((result) => {
        console.info('current location: ' + JSON.stringify(result));
    })
    .catch((error:BusinessError) => {
        console.error('promise, getCurrentLocation: error=' + JSON.stringify(error));
    });
} catch (err) {
    console.error("errCode:" + err.code + ", message:"  + err.message);
}
```

#### geoLocationManager.getLastLocation

getLastLocation(): Location

获取上一次位置。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**需要权限**：ohos.permission.APPROXIMATELY_LOCATION

**系统能力**：SystemCapability.Location.Location.Core

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Location | 位置信息。 |

**错误码**：

以下错误码的详细介绍请参见[位置服务子系统错误码](位置服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 801 | Capability not supported. Failed to call ${geoLocationManager.getLastLocation} due to limited device capabilities. |
| 3301000 | The location service is unavailable. |
| 3301100 | The location switch is off. |
| 3301200 | Failed to obtain the geographical location. |

**示例**

```ets
import { geoLocationManager } from '@kit.LocationKit';
try {
    let location = geoLocationManager.getLastLocation();
} catch (err) {
    console.error("errCode:" + err.code + ", message:"  + err.message);
}
```

#### geoLocationManager.isLocationEnabled

isLocationEnabled(): boolean

判断位置服务是否已经开启。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Location.Location.Core

**返回值**：

| 类型 | 说明 |
| --- | --- |
| boolean | true：位置信息开关已开启。 false：位置信息开关已关闭。 |

**错误码**：

以下错误码的详细介绍请参见[位置服务子系统错误码](位置服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call ${geoLocationManager.isLocationEnabled} due to limited device capabilities. |
| 3301000 | The location service is unavailable. |

**示例**

```ets
import { geoLocationManager } from '@kit.LocationKit';
try {
    let locationEnabled = geoLocationManager.isLocationEnabled();
} catch (err) {
    console.error("errCode:" + err.code + ", message:"  + err.message);
}
```

#### geoLocationManager.getAddressesFromLocation

getAddressesFromLocation(request: ReverseGeoCodeRequest, callback: AsyncCallback<Array<GeoAddress>>): void

调用逆地理编码服务，将坐标转换为地理描述，使用callback异步回调。

**系统能力**：SystemCapability.Location.Location.Geocoder

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| request | ReverseGeoCodeRequest | 是 | 设置逆地理编码请求的相关参数。 |
| callback | AsyncCallback<Array<GeoAddress>> | 是 | 回调函数，返回逆地理编码结果。 |

**错误码**：

以下错误码的详细介绍请参见[位置服务子系统错误码](位置服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call ${geoLocationManager.getAddressesFromLocation} due to limited device capabilities. |
| 3301000 | The location service is unavailable. |
| 3301300 | Reverse geocoding query failed. |

**示例**

```ets
import { geoLocationManager } from '@kit.LocationKit';

let reverseGeocodeRequest: geoLocationManager.ReverseGeoCodeRequest = {
  "latitude": 31.12,
  "longitude": 121.11,
  "maxItems": 1
};
try {
    geoLocationManager.getAddressesFromLocation(reverseGeocodeRequest, (err, data) => {
        if (err) {
            console.error('getAddressesFromLocation: err=' + JSON.stringify(err));
        }
        if (data) {
            console.info('getAddressesFromLocation: data=' + JSON.stringify(data));
        }
    });
} catch (err) {
    console.error("errCode:" + err.code + ", message:"  + err.message);
}
```

#### geoLocationManager.getAddressesFromLocation

getAddressesFromLocation(request: ReverseGeoCodeRequest): Promise<Array<GeoAddress>>

调用逆地理编码服务，将坐标转换为地理描述，使用Promise异步回调。

**系统能力**：SystemCapability.Location.Location.Geocoder

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| request | ReverseGeoCodeRequest | 是 | 设置逆地理编码请求的相关参数。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<Array<GeoAddress>> | Promise对象，返回地理描述信息。 |

**错误码**：

以下错误码的详细介绍请参见[位置服务子系统错误码](位置服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call ${geoLocationManager.getAddressesFromLocation} due to limited device capabilities. |
| 3301000 | The location service is unavailable. |
| 3301300 | Reverse geocoding query failed. |

**示例**

```ets
import { geoLocationManager } from '@kit.LocationKit';
import { BusinessError } from '@kit.BasicServicesKit';

let reverseGeocodeRequest: geoLocationManager.ReverseGeoCodeRequest = {
  "latitude": 31.12,
  "longitude": 121.11,
  "maxItems": 1
};
try {
    geoLocationManager.getAddressesFromLocation(reverseGeocodeRequest).then((data) => {
        console.info('getAddressesFromLocation: ' + JSON.stringify(data));
    })
    .catch((error:BusinessError) => {
        console.error('promise, getAddressesFromLocation: error=' + JSON.stringify(error));
    });
} catch (err) {
    console.error("errCode:" + err.code + ", message:"  + err.message);
}
```

#### geoLocationManager.getAddressesFromLocationName

getAddressesFromLocationName(request: GeoCodeRequest, callback: AsyncCallback<Array<GeoAddress>>): void

调用地理编码服务，将地理描述转换为具体坐标，使用callback异步回调。

**系统能力**：SystemCapability.Location.Location.Geocoder

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| request | GeoCodeRequest | 是 | 设置地理编码请求的相关参数。 |
| callback | AsyncCallback<Array<GeoAddress>> | 是 | 回调函数，返回地理编码结果。 |

**错误码**：

以下错误码的详细介绍请参见[位置服务子系统错误码](位置服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call ${geoLocationManager.getAddressesFromLocationName} due to limited device capabilities. |
| 3301000 | The location service is unavailable. |
| 3301400 | Geocoding query failed. |

**示例**

```ets
import { geoLocationManager } from '@kit.LocationKit';
let geocodeRequest:geoLocationManager.GeoCodeRequest = {"description": "上海市浦东新区xx路xx号", "maxItems": 1};
try {
    geoLocationManager.getAddressesFromLocationName(geocodeRequest, (err, data) => {
        if (err) {
            console.error('getAddressesFromLocationName: err=' + JSON.stringify(err));
        }
        if (data) {
            console.info('getAddressesFromLocationName: data=' + JSON.stringify(data));
        }
    });
} catch (err) {
    console.error("errCode:" + err.code + ", message:"  + err.message);
}
```

#### geoLocationManager.getAddressesFromLocationName

getAddressesFromLocationName(request: GeoCodeRequest): Promise<Array<GeoAddress>>

调用地理编码服务，将地理描述转换为具体坐标，使用Promise异步回调。

**系统能力**：SystemCapability.Location.Location.Geocoder

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| request | GeoCodeRequest | 是 | 设置地理编码请求的相关参数。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<Array<GeoAddress>> | Promise对象，返回地理编码查询结果。 |

**错误码**：

以下错误码的详细介绍请参见[位置服务子系统错误码](位置服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call ${geoLocationManager.getAddressesFromLocationName} due to limited device capabilities. |
| 3301000 | The location service is unavailable. |
| 3301400 | Geocoding query failed. |

**示例**

```ets
import { geoLocationManager } from '@kit.LocationKit';
import { BusinessError } from '@kit.BasicServicesKit';
let geocodeRequest:geoLocationManager.GeoCodeRequest = {"description": "上海市浦东新区xx路xx号", "maxItems": 1};
try {
    geoLocationManager.getAddressesFromLocationName(geocodeRequest).then((result) => {
        console.info('getAddressesFromLocationName: ' + JSON.stringify(result));
    })
    .catch((error:BusinessError) => {
        console.error('promise, getAddressesFromLocationName: error=' + JSON.stringify(error));
    });
} catch (err) {
    console.error("errCode:" + err.code + ", message:"  + err.message);
}
```

#### geoLocationManager.isGeocoderAvailable

isGeocoderAvailable(): boolean

判断地理编码与逆地理编码服务状态。

**系统能力**：SystemCapability.Location.Location.Geocoder

**返回值**：

| 类型 | 说明 |
| --- | --- |
| boolean | true:地理编码与逆地理编码服务可用。 false：地理编码与逆地理编码服务不可用。 |

**错误码**：

以下错误码的详细介绍请参见[位置服务子系统错误码](位置服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call ${geoLocationManager.isGeocoderAvailable} due to limited device capabilities. |
| 3301000 | The location service is unavailable. |

**示例**

```ets
import { geoLocationManager } from '@kit.LocationKit';
try {
    let isAvailable = geoLocationManager.isGeocoderAvailable();
} catch (err) {
    console.error("errCode:" + err.code + ", message:"  + err.message);
}
```

#### geoLocationManager.getCachedGnssLocationsSize

getCachedGnssLocationsSize(callback: AsyncCallback<number>): void

获取GNSS芯片缓存位置的个数。该接口功能由GNSS定位芯片提供（仅部分型号支持），如果设备无此芯片或使用的芯片型号不支持该功能，则返回错误码801（Capability not supported）。使用callback异步回调。

**需要权限**：ohos.permission.APPROXIMATELY_LOCATION

**系统能力**：SystemCapability.Location.Location.Gnss

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<number> | 是 | 回调函数，返回GNSS芯片缓存位置个数。 |

**错误码**：

以下错误码的详细介绍请参见[位置服务子系统错误码](位置服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call ${geoLocationManager.getCachedGnssLocationsSize} due to limited device capabilities. |
| 3301000 | The location service is unavailable. |
| 3301100 | The location switch is off. |

**示例**

```ets
import { geoLocationManager } from '@kit.LocationKit';
try {
    geoLocationManager.getCachedGnssLocationsSize((err, size) => {
        if (err) {
            console.error('getCachedGnssLocationsSize: err=' + JSON.stringify(err));
        }
        if (size) {
            console.info('getCachedGnssLocationsSize: size=' + JSON.stringify(size));
        }
    });
} catch (err) {
    console.error("errCode:" + err.code + ", message:"  + err.message);
}
```

#### geoLocationManager.getCachedGnssLocationsSize

getCachedGnssLocationsSize(): Promise<number>

获取GNSS芯片缓存位置的个数。该接口功能由GNSS定位芯片提供（仅部分型号支持），如果设备无此芯片或使用的芯片型号不支持该功能，则返回错误码801（Capability not supported）。使用Promise异步回调。

**需要权限**：ohos.permission.APPROXIMATELY_LOCATION

**系统能力**：SystemCapability.Location.Location.Gnss

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回GNSS缓存位置的个数。 |

**错误码**：

以下错误码的详细介绍请参见[位置服务子系统错误码](位置服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 801 | Capability not supported. Failed to call ${geoLocationManager.getCachedGnssLocationsSize} due to limited device capabilities. |
| 3301000 | The location service is unavailable. |
| 3301100 | The location switch is off. |

**示例**

```ets
import { geoLocationManager } from '@kit.LocationKit';
import { BusinessError } from '@kit.BasicServicesKit';
try {
    geoLocationManager.getCachedGnssLocationsSize().then((result) => {
        console.info('promise, getCachedGnssLocationsSize: ' + JSON.stringify(result));
    })
    .catch((error:BusinessError) => {
        console.error('promise, getCachedGnssLocationsSize: error=' + JSON.stringify(error));
    });
} catch (err) {
    console.error("errCode:" + err.code + ", message:"  + err.message);
}
```

#### geoLocationManager.flushCachedGnssLocations

flushCachedGnssLocations(callback: AsyncCallback<void>): void

读取并清空GNSS芯片所有缓存位置。该接口功能由GNSS定位芯片提供（仅部分型号支持），如果设备无此芯片或使用的芯片型号不支持该功能，则返回错误码801（Capability not supported）。使用callback异步回调。

**需要权限**：ohos.permission.APPROXIMATELY_LOCATION

**系统能力**：SystemCapability.Location.Location.Gnss

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当操作成功，err为undefined，否则为错误对象。 |

**错误码**：

以下错误码的详细介绍请参见[位置服务子系统错误码](位置服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call ${geoLocationManager.flushCachedGnssLocations} due to limited device capabilities. |
| 3301000 | The location service is unavailable. |
| 3301100 | The location switch is off. |
| 3301200 | Failed to obtain the geographical location. |

**示例**

```ets
import { geoLocationManager } from '@kit.LocationKit';
try {
    geoLocationManager.flushCachedGnssLocations((err) => {
        if (err) {
            console.error('flushCachedGnssLocations: err=' + JSON.stringify(err));
        }
    });
} catch (err) {
    console.error("errCode:" + err.code + ", message:"  + err.message);
}
```

#### geoLocationManager.flushCachedGnssLocations

flushCachedGnssLocations(): Promise<void>

读取并清空GNSS芯片所有缓存位置。该接口功能由GNSS定位芯片提供（仅部分型号支持），如果设备无此芯片或使用的芯片型号不支持该功能，则返回错误码801（Capability not supported）。使用Promise异步回调。

**需要权限**：ohos.permission.APPROXIMATELY_LOCATION

**系统能力**：SystemCapability.Location.Location.Gnss

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象 |

**错误码**：

以下错误码的详细介绍请参见[位置服务子系统错误码](位置服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 801 | Capability not supported. Failed to call ${geoLocationManager.flushCachedGnssLocations} due to limited device capabilities. |
| 3301000 | The location service is unavailable. |
| 3301100 | The location switch is off. |
| 3301200 | Failed to obtain the geographical location. |

**示例**

```ets
import { geoLocationManager } from '@kit.LocationKit';
import { BusinessError } from '@kit.BasicServicesKit';
try {
    geoLocationManager.flushCachedGnssLocations().then(() => {
        console.info('promise, flushCachedGnssLocations success');
    })
    .catch((error:BusinessError) => {
        console.error('promise, flushCachedGnssLocations: error=' + JSON.stringify(error));
    });
} catch (err) {
    console.error("errCode:" + err.code + ", message:"  + err.message);
}
```

#### geoLocationManager.sendCommand

sendCommand(command: LocationCommand, callback: AsyncCallback<void>): void

给位置服务子系统的各个部件发送扩展命令。使用callback异步回调。

**系统能力**：SystemCapability.Location.Location.Core

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| command | LocationCommand | 是 | 指定目标场景，和将要发送的命令（字符串）。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当命令发送成功，err为undefined，否则为错误对象。 |

**错误码**：

以下错误码的详细介绍请参见[位置服务子系统错误码](位置服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call ${geoLocationManager.sendCommand} due to limited device capabilities. |
| 3301000 | The location service is unavailable. |

**示例**

```ets
import { geoLocationManager } from '@kit.LocationKit';
let requestInfo:geoLocationManager.LocationCommand = {'scenario': 0x301, 'command': "command_1"};
try {
    geoLocationManager.sendCommand(requestInfo, (err) => {
        if (err) {
            console.error('sendCommand: err=' + JSON.stringify(err));
        }
    });
} catch (err) {
    console.error("errCode:" + err.code + ", message:"  + err.message);
}
```

#### geoLocationManager.sendCommand

sendCommand(command: LocationCommand): Promise<void>

给位置服务子系统的各个部件发送扩展命令。使用Promise异步回调。

**系统能力**：SystemCapability.Location.Location.Core

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| command | LocationCommand | 是 | 指定目标场景，和将要发送的命令（字符串）。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象 |

**错误码**：

以下错误码的详细介绍请参见[位置服务子系统错误码](位置服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call ${geoLocationManager.sendCommand} due to limited device capabilities. |
| 3301000 | The location service is unavailable. |

**示例**

```ets
import { geoLocationManager } from '@kit.LocationKit';
import { BusinessError } from '@kit.BasicServicesKit';
let requestInfo:geoLocationManager.LocationCommand = {'scenario': 0x301, 'command': "command_1"};
try {
    geoLocationManager.sendCommand(requestInfo).then(() => {
        console.info('promise, sendCommand success');
    })
    .catch((error:BusinessError) => {
        console.error('promise, sendCommand: error=' + JSON.stringify(error));
    });
} catch (err) {
    console.error("errCode:" + err.code + ", message:"  + err.message);
}
```

#### geoLocationManager.getCountryCode

getCountryCode(callback: AsyncCallback<CountryCode>): void

查询当前的国家码。使用callback异步回调。

**系统能力**：SystemCapability.Location.Location.Core

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<CountryCode> | 是 | 回调函数，返回国家码信息。 |

**错误码**：

以下错误码的详细介绍请参见[位置服务子系统错误码](位置服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call ${geoLocationManager.getCountryCode} due to limited device capabilities. |
| 3301000 | The location service is unavailable. |
| 3301500 | Failed to query the area information. |

**示例**

```ets
import { geoLocationManager } from '@kit.LocationKit';
try {
    geoLocationManager.getCountryCode((err, result) => {
        if (err) {
            console.error('getCountryCode: err=' + JSON.stringify(err));
        }
        if (result) {
            console.info('getCountryCode: result=' + JSON.stringify(result));
        }
    });
} catch (err) {
    console.error("errCode:" + err.code + ", message:"  + err.message);
}
```

#### geoLocationManager.getCountryCode

getCountryCode(): Promise<CountryCode>

查询当前的国家码。使用Promise异步回调。

**系统能力**：SystemCapability.Location.Location.Core

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<CountryCode> | Promise对象，返回国家码信息。 |

**错误码**：

以下错误码的详细介绍请参见[位置服务子系统错误码](位置服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call ${geoLocationManager.getCountryCode} due to limited device capabilities. |
| 3301000 | The location service is unavailable. |
| 3301500 | Failed to query the area information. |

**示例**

```ets
import { geoLocationManager } from '@kit.LocationKit';
import { BusinessError } from '@kit.BasicServicesKit';
try {
    geoLocationManager.getCountryCode()
    .then((result) => {
        console.info('promise, getCountryCode: result=' + JSON.stringify(result));
    })
    .catch((error:BusinessError) => {
        console.error('promise, getCountryCode: error=' + JSON.stringify(error));
    });
} catch (err) {
    console.error("errCode:" + err.code + ", message:"  + err.message);
}
```

#### geoLocationManager.addGnssGeofence12+

addGnssGeofence(fenceRequest: GnssGeofenceRequest): Promise<number>

添加一个GNSS地理围栏，并订阅地理围栏事件。使用Promise异步回调。

APP可以在入参[GnssGeofenceRequest](#ZH-CN_TOPIC_0000002553202339__gnssgeofencerequest12)中传入回调函数用于接收地理围栏事件；也可以传入通知对象[NotificationRequest](@ohos.notification (Notification模块).md#ZH-CN_TOPIC_0000002522082432__notificationrequest)，在系统识别到地理围栏事件发生时会弹出APP创建的通知。

GNSS地理围栏功能依赖GNSS定位芯片（仅部分型号支持），如果设备无此芯片或使用的芯片型号不支持该功能，则返回错误码801（Capability not supported）。

**需要权限**：ohos.permission.LOCATION 和 ohos.permission.APPROXIMATELY_LOCATION

**系统能力**：SystemCapability.Location.Location.Geofence

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fenceRequest | GnssGeofenceRequest | 是 | 添加GNSS地理围栏请求参数。 包含圆形围栏信息、需要监听的地理围栏事件、地理围栏事件触发后弹出的通知对象和监听地理围栏事件的回调函数。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回地理围栏ID。 |

**错误码**：

以下错误码的详细介绍请参见[位置服务子系统错误码](位置服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call ${geoLocationManager.addGnssGeofence} due to limited device capabilities. |
| 3301000 | The location service is unavailable. |
| 3301100 | The location switch is off. |
| 3301601 | The number of geofences exceeds the maximum. |

**示例**

```ets
import { geoLocationManager } from '@kit.LocationKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { notificationManager } from '@kit.NotificationKit';
// 创建围栏
let geofence: geoLocationManager.Geofence = {
  "latitude": 34.12, "longitude": 124.11, "radius": 10000.0, "expiration": 10000.0
}
// 指定APP需要监听的地理围栏事件类型，这里表示需要监听进入围栏和退出围栏事件
let transitionStatusList: Array<geoLocationManager.GeofenceTransitionEvent> = [
  geoLocationManager.GeofenceTransitionEvent.GEOFENCE_TRANSITION_EVENT_ENTER,
  geoLocationManager.GeofenceTransitionEvent.GEOFENCE_TRANSITION_EVENT_EXIT,
];
// 创建GEOFENCE_TRANSITION_EVENT_ENTER事件对应的通知对象
let notificationRequest1: notificationManager.NotificationRequest = {
  id: 1,
  content: {
    notificationContentType: notificationManager.ContentType.NOTIFICATION_CONTENT_BASIC_TEXT,
    normal: {
      title: "围栏通知",
      text: "围栏进入",
      additionalText: ""
    }
};
// 创建GEOFENCE_TRANSITION_EVENT_EXIT事件对应的通知对象
let notificationRequest2: notificationManager.NotificationRequest = {
  id: 2,
  content: {
    notificationContentType: notificationManager.ContentType.NOTIFICATION_CONTENT_BASIC_TEXT,
    normal: {
      title: '围栏通知',
      text: '围栏退出',
      additionalText: ""
  }
};
// 把创建的通知对象存入Array中，存入顺序与transitionStatusList一致
let notificationRequestList: Array<notificationManager.NotificationRequest> =
  [notificationRequest1, notificationRequest2];
// 构造GNSS地理围栏请求对象gnssGeofenceRequest
let gnssGeofenceRequest: geoLocationManager.GnssGeofenceRequest = {
  // 围栏属性，包含圆心和半径等信息
  geofence: geofence,
  // 指定APP需要监听的地理围栏事件类型
  monitorTransitionEvents: transitionStatusList,
  // 地理围栏事件对应的通知对象，该参数为可选
  notifications: notificationRequestList,
  // 设备驻留在地理围栏内的时间，该参数为可选
  loiterTimeMs: 10000,
  // 围栏回调要拉起的FenceExtensionAbility名称，该参数为可选
  fenceExtensionAbilityName: "FenceExtensionAbility",
  // 用于监听围栏事件的callback
  geofenceTransitionCallback: (err : BusinessError, transition : geoLocationManager.GeofenceTransition) => {
    if (err) {
      console.error('geofenceTransitionCallback: err=' + JSON.stringify(err));
    }
    if (transition) {
      console.info("GeofenceTransition: %{public}s", JSON.stringify(transition));
}
try {
  // 添加围栏
  geoLocationManager.addGnssGeofence(gnssGeofenceRequest).then((id) => {
    // 围栏添加成功后返回围栏ID
    console.info("addGnssGeofence success, fence id: " + id);
    let fenceId = id;
  }).catch((err: BusinessError) => {
    console.error("addGnssGeofence failed, promise errCode:" + (err as BusinessError).code +
      ",errMessage:" + (err as BusinessError).message);
  });
} catch(error) {
    console.error("addGnssGeofence failed, err:" + JSON.stringify(error));
}
```

#### geoLocationManager.removeGnssGeofence12+

removeGnssGeofence(geofenceId: number): Promise<void>

删除一个GNSS地理围栏，并取消订阅该地理围栏事件。使用Promise异步回调。

GNSS地理围栏功能依赖GNSS定位芯片（仅部分型号支持），如果设备无此芯片或使用的芯片型号不支持该功能，则返回错误码801（Capability not supported）。

**需要权限**：ohos.permission.LOCATION 和 ohos.permission.APPROXIMATELY_LOCATION

**系统能力**：SystemCapability.Location.Location.Geofence

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| geofenceId | number | 是 | GNSS地理围栏的ID。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码**：

以下错误码的详细介绍请参见[位置服务子系统错误码](位置服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call ${geoLocationManager.removeGnssGeofence} due to limited device capabilities. |
| 3301000 | The location service is unavailable. |
| 3301602 | Failed to delete a geofence due to an incorrect ID. |

**示例**

```ets
import { geoLocationManager } from '@kit.LocationKit';
import { BusinessError } from '@kit.BasicServicesKit';
// fenceId是在geoLocationManager.addGnssGeofence执行成功后获取的
let fenceId = 1;
try {
  geoLocationManager.removeGnssGeofence(fenceId).then(() => {
    console.info("removeGnssGeofence success fenceId:" + fenceId);
  }).catch((error : BusinessError) => {
    console.error("removeGnssGeofence: error=" + JSON.stringify(error));
  });
} catch(error) {
  console.error("removeGnssGeofence: error=" + JSON.stringify(error));
}
```

#### geoLocationManager.getGeofenceSupportedCoordTypes12+

getGeofenceSupportedCoordTypes(): Array<CoordinateSystemType>

获取地理围栏功能支持的坐标系列表。

**系统能力**：SystemCapability.Location.Location.Geofence

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Array<CoordinateSystemType> | 地理围栏功能支持的坐标系列表。 |

**错误码**：

以下错误码的详细介绍请参见[位置服务子系统错误码](位置服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call ${geoLocationManager.getGeofenceSupportedCoordTypes} due to limited device capabilities. |
| 3301000 | The location service is unavailable. |

**示例**

```ets
import { geoLocationManager } from '@kit.LocationKit';
try {
  let supportedCoordTypes: Array<geoLocationManager.CoordinateSystemType> = geoLocationManager.getGeofenceSupportedCoordTypes();
  console.info("getGeofenceSupportedCoordTypes return:" + JSON.stringify(supportedCoordTypes));
} catch(error) {
  console.error("getGeofenceSupportedCoordTypes: error=" + JSON.stringify(error));
}
```

#### geoLocationManager.getCurrentWifiBssidForLocating14+

getCurrentWifiBssidForLocating(): string

获取连接的Wi-Fi AP（Access Point）的Bssid（Basic Service Set Identifier）信息。如果当前设备未连接Wi-Fi，调用该接口将抛出错误码3301900。建议参考示例代码，通过try-catch结构捕获异常。

**需要权限**：ohos.permission.LOCATION 和 ohos.permission.APPROXIMATELY_LOCATION

**系统能力**：SystemCapability.Location.Location.Core

**返回值**：

| 类型 | 说明 |
| --- | --- |
| string | Wi-Fi Bssid |

**错误码**：

以下错误码的详细介绍请参见[位置服务子系统错误码](位置服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 801 | Capability not supported. Failed to call ${geoLocationManager.getCurrentWifiBssidForLocating()} due to limited device capabilities. |
| 3301000 | The location service is unavailable. |
| 3301100 | The location switch is off. |
| 3301900 | Failed to obtain the BSSID of the Wi-Fi hotspot. The Wi-Fi network is not connected. |

**示例**

```ets
import { geoLocationManager } from '@kit.LocationKit';
try {
  let bssid: string = geoLocationManager.getCurrentWifiBssidForLocating();
  console.info("get wifi bssid:" + bssid);
} catch(error) {
  console.error("getCurrentWifiBssidForLocating: errCode" + error.code + ", errMessage" + error.message);
}
```

#### geoLocationManager.on('bluetoothScanResultChange')16+

on(type: 'bluetoothScanResultChange', callback: Callback<BluetoothScanResult>): void

订阅蓝牙扫描信息上报事件，使用callback异步回调。

本API需要开发者向[locationkit@huawei.com](mailto:locationkit@huawei.com)发送邮件申请，请在邮件中写明使用该API的业务场景和获取蓝牙deviceId（MAC）的真实用途，申请审批通过后会方可使用。

本API会启动蓝牙扫描，为了避免产生较多功耗，需要开发者在适当的时机调用 [geoLocationManager.off('bluetoothScanResultChange')](#ZH-CN_TOPIC_0000002553202339__geolocationmanageroffbluetoothscanresultchange16)接口停止蓝牙扫描。

当前仅支持扫描BLE设备。

**需要权限**：ohos.permission.APPROXIMATELY_LOCATION 和 ohos.permission.LOCATION

**系统能力**：SystemCapability.Location.Location.Core

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置事件类型。type为“bluetoothScanResultChange”，表示订阅蓝牙扫描信息上报事件。 |
| callback | Callback<BluetoothScanResult> | 是 | 回调函数，返回蓝牙扫描信息。 |

**错误码**：

以下错误码的详细介绍请参见[位置服务子系统错误码](位置服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call ${geoLocationManager.on('bluetoothScanResultChange')} due to limited device capabilities. |
| 3301000 | The location service is unavailable. |
| 3301100 | The location switch is off. |

**示例**

```ets
import { geoLocationManager } from '@kit.LocationKit';

let callback = (result: geoLocationManager.BluetoothScanResult):void => {
    console.info('bluetoothScanResultChange: ' + JSON.stringify(result));
};
try {
    geoLocationManager.on('bluetoothScanResultChange', callback);
} catch (err) {
    console.error("errCode:" + err.code + ", message:"  + err.message);
}
```

#### geoLocationManager.off('bluetoothScanResultChange')16+

off(type: 'bluetoothScanResultChange', callback?: Callback<BluetoothScanResult>): void

取消订阅蓝牙扫描信息上报事件并停止蓝牙扫描。

**需要权限**：ohos.permission.APPROXIMATELY_LOCATION 和 ohos.permission.LOCATION

**系统能力**：SystemCapability.Location.Location.Core

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置事件类型。type为“bluetoothScanResultChange”，表示停止订阅蓝牙扫描信息上报事件。 |
| callback | Callback<BluetoothScanResult> | 否 | 需要取消订阅的回调函数。该回调函数需要与on接口传入的回调函数保持一致。若无此参数，则取消当前类型的所有订阅。 |

**错误码**：

以下错误码的详细介绍请参见[位置服务子系统错误码](位置服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call ${geoLocationManager.off('bluetoothScanResultChange')} due to limited device capabilities. |
| 3301000 | The location service is unavailable. |

**示例**

```ets
import { geoLocationManager } from '@kit.LocationKit';

let callback = (result: geoLocationManager.BluetoothScanResult):void => {
    console.info('bluetoothScanResultChange: ' + JSON.stringify(result));
};
try {
    geoLocationManager.on('bluetoothScanResultChange', callback);
    geoLocationManager.off('bluetoothScanResultChange', callback);
} catch (err) {
    console.error("errCode:" + err.code + ", message:"  + err.message);
}
```

#### geoLocationManager.isPoiServiceSupported20+

isPoiServiceSupported(): boolean

查询系统（即软件）是否支持POI服务。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Location.Location.Core

**返回值**：

| 类型 | 说明 |
| --- | --- |
| boolean | true:POI服务可用。 false:POI服务不可用。 |

**示例**

```ets
import { geoLocationManager } from '@kit.LocationKit';
let poiServiceState = geoLocationManager.isPoiServiceSupported();
console.info("poiServiceState:" + poiServiceState);
```

#### geoLocationManager.getPoiInfo20+

getPoiInfo(): Promise<PoiInfo>

获取当前位置附近的POI信息。使用Promise异步回调。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**需要权限**：ohos.permission.LOCATION 和 ohos.permission.APPROXIMATELY_LOCATION

**系统能力**：SystemCapability.Location.Location.Core

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<PoiInfo> | 当前位置附近的POI信息。 |

**错误码**：

以下错误码的详细介绍请参见[位置服务子系统错误码](位置服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 801 | Capability not supported. Failed to call ${geoLocationManager.getPoiInfo} due to limited device capabilities. |
| 3301000 | The location service is unavailable. |
| 3301100 | The location switch is off. |

**示例**

```ets
import { geoLocationManager } from '@kit.LocationKit';
try {
  if (geoLocationManager.isPoiServiceSupported()) {
    geoLocationManager.getPoiInfo().then((poiInfo) => {
      if (poiInfo !== undefined) {
        console.info("get PoiInfo:" + JSON.stringify(poiInfo));
      }
    })
  }
} catch(error) {
  console.error("getPoiInfo errCode:" + error.code + ", errMessage:" + error.message);
}
```

#### geoLocationManager.getDistanceBetweenLocations20+

getDistanceBetweenLocations(location1: Location, location2: Location): number

获取两个位置之间的直线距离。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Location.Location.Core

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| location1 | Location | 是 | 位置1。 |
| location2 | Location | 是 | 位置2。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| number | 两个位置之间的直线距离，单位为米。 |

**示例**

```ets
import { geoLocationManager } from '@kit.LocationKit';
try {
  let location1: geoLocationManager.Location = {
    "latitude": 30.12,
    "longitude": 120.11,
    "altitude": 0,
    "accuracy": 0,
    "speed": 0,
    "timeStamp": 0,
    "direction": 0,
    "timeSinceBoot": 0,
    "additionSize": 0
  }
  let location2: geoLocationManager.Location = {
    "latitude": 30.12,
    "longitude": 120.11,
    "altitude": 0,
    "accuracy": 0,
    "speed": 0,
    "timeStamp": 0,
    "direction": 0,
    "timeSinceBoot": 0,
    "additionSize": 0
  }
  let distance = geoLocationManager.getDistanceBetweenLocations(location1, location2);
  console.info("distance:" + distance);
} catch(error) {
  console.error("getDistanceBetweenLocations: errCode" + error.code + ", errMessage" + error.message);
}
```

#### geoLocationManager.addBeaconFence20+

addBeaconFence(fenceRequest: BeaconFenceRequest): Promise<number>

添加一个beacon围栏，并订阅地理围栏事件。使用Promise异步回调。

beacon围栏是指通过蓝牙beacon设备和手机应用配合，实现“虚拟围栏”的功能。当用户靠近或离开某个特定的beacon设备时，手机应用会收到通知。

应用可以在入参[BeaconFenceRequest](#ZH-CN_TOPIC_0000002553202339__beaconfencerequest20)中传入回调函数用于接收围栏事件；也可以传入[FenceExtensionAbility](@ohos.app.ability.FenceExtensionAbility (FenceExtensionAbility).md)名称，在系统识别到围栏事件发生时通知应用。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**需要权限**：ohos.permission.LOCATION 和 ohos.permission.APPROXIMATELY_LOCATION

**系统能力**：SystemCapability.Location.Location.Geofence

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fenceRequest | BeaconFenceRequest | 是 | 添加beacon围栏请求参数。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回beacon围栏ID。 |

**错误码**：

以下错误码的详细介绍请参见[位置服务子系统错误码](位置服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 801 | Capability not supported. Failed to call ${geoLocationManager.addBeaconFence} due to limited device capabilities. |
| 3501100 | Failed to add a beacon fence because the location switch is off. |
| 3501101 | Failed to add a beacon fence because the bluetooth switch is off. |
| 3501601 | The number of beacon fence exceeds the maximum. |
| 3501603 | Duplicate beacon fence information. |

**示例**

```ets
import { geoLocationManager } from '@kit.LocationKit';
import { BusinessError } from '@kit.BasicServicesKit';
try {
  // 以iBeacon协议为例，格式如下
  // 01 byte    type = 0x02
  // 01 byte    len = 0x15 = 21
  // 16 byte    UUID
  // 02 byte    major
  // 02 byte    minor
  // 01 byte    tx power
  let manufactureDataBuffer: Uint8Array = new Uint8Array([0X02, 0X15, 0X00, 0X11, 0X22, 0X33, 0X44, 0X55,
    0X66, 0X77, 0X88, 0X99, 0XAA, 0XBB, 0XCC, 0XDD, 0XEE, 0XFF, 0X11, 0X22, 0X33, 0X44, 0X55]);
  let manufactureDataMaskBuffer: Uint8Array = new Uint8Array([0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF,
    0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF]);

  let manufactureData:geoLocationManager.BeaconManufactureData = {
    manufactureId: 0X004C,
    manufactureData: manufactureDataBuffer.buffer,
    manufactureDataMask: manufactureDataMaskBuffer.buffer
  };

  let beacon:geoLocationManager.BeaconFence = {
    identifier: "11",
    beaconFenceInfoType: geoLocationManager.BeaconFenceInfoType.BEACON_MANUFACTURE_DATA,
    manufactureData:manufactureData
  };

  let fenceRequest:geoLocationManager.BeaconFenceRequest = {
    beacon: beacon,
    transitionCallback: (transition : geoLocationManager.GeofenceTransition) => {
      if (transition) {
        console.info("GeofenceTransition: err" + JSON.stringify(transition));
      }
    },
    fenceExtensionAbilityName: "MyFenceExtensionAbility",
  };
  geoLocationManager.addBeaconFence(fenceRequest).then((id) => {
    console.info("addBeaconFence success, fence id:" + id);
  }).catch((err : BusinessError) => {
    console.error('promise, addBeaconFence: error=' + JSON.stringify(err));
  });
} catch(error) {
  console.error("addBeaconFence: errCode" + error.code + ", errMessage" + error.message);
}
```

#### geoLocationManager.removeBeaconFence20+

removeBeaconFence(beaconFence?: BeaconFence): Promise<void>

删除beacon围栏，并取消订阅地理围栏事件。使用Promise异步回调。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**需要权限**：ohos.permission.LOCATION 和 ohos.permission.APPROXIMATELY_LOCATION

**系统能力**：SystemCapability.Location.Location.Geofence

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| beaconFence | BeaconFence | 否 | 传入beaconFence参数，删除指定围栏；不传入参数，删除该应用所有围栏。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码**：

以下错误码的详细介绍请参见[位置服务子系统错误码](位置服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 801 | Capability not supported. Failed to call ${geoLocationManager.removeBeaconFence} due to limited device capabilities. |
| 3501602 | Failed to delete the fence due to incorrect beacon fence information. |

**示例**

```ets
import { geoLocationManager } from '@kit.LocationKit';
import { BusinessError } from '@kit.BasicServicesKit';
try {
  let manufactureDataBuffer: Uint8Array = new Uint8Array([0X02, 0X15, 0X00, 0X11, 0X22, 0X33, 0X44, 0X55,
    0X66, 0X77, 0X88, 0X99, 0XAA, 0XBB, 0XCC, 0XDD, 0XEE, 0XFF, 0X11, 0X22, 0X33, 0X44, 0X55]);
  let manufactureDataMaskBuffer: Uint8Array = new Uint8Array([0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF,
    0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF]);

  let manufactureData:geoLocationManager.BeaconManufactureData = {
    manufactureId: 0X004C,
    manufactureData: manufactureDataBuffer.buffer,
    manufactureDataMask: manufactureDataMaskBuffer.buffer
  };

  let beacon:geoLocationManager.BeaconFence = {
    identifier: "11",
    beaconFenceInfoType: geoLocationManager.BeaconFenceInfoType.BEACON_MANUFACTURE_DATA,
    manufactureData:manufactureData
  };
  geoLocationManager.removeBeaconFence(beacon).then(() => {
    console.info("promise, removeBeaconFence success");
  })
  .catch((error:BusinessError) => {
    console.error("promise, removeBeaconFence: errCode" + error.code + ", errMessage" + error.message);
  });
} catch(error) {
  console.error("removeBeaconFence: errCode" + error.code + ", errMessage" + error.message);
}
```

#### geoLocationManager.isBeaconFenceSupported20+

isBeaconFenceSupported(): boolean;

判断当前设备是否支持beacon围栏。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Location.Location.Geofence

**返回值**：

| 类型 | 说明 |
| --- | --- |
| boolean | true：支持beacon围栏。 false：不支持beacon围栏。 |

**示例**

```ets
import { geoLocationManager } from '@kit.LocationKit';
try {
    let isBeaconFenceSupported = geoLocationManager.isBeaconFenceSupported();
} catch (err) {
    console.error("errCode:" + err.code + ", message:"  + err.message);
}
```

#### geoLocationManager.isWlanBssidMatched21+

isWlanBssidMatched(wlanBssidArray: Array<string>, rssiThreshold: number, needStartScan: boolean): Promise<boolean>

判断指定的BSSID是否存在于最新的WLAN扫描结果里。使用Promise异步回调。

**元服务API：** 从API version 21开始，该接口支持在元服务中使用。

**需要权限**：ohos.permission.LOCATION 和 ohos.permission.APPROXIMATELY_LOCATION

**系统能力**：SystemCapability.Location.Location.Core

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| wlanBssidArray | Array<string> | 是 | 请求匹配的BSSID列表。单个字符串的长度不超过64，数组的长度不超过1000。 |
| rssiThreshold | number | 是 | RSSI阈值。只匹配RSSI大于此阈值的BSSID，取值范围为-10000至10000（单位：dBm）。 |
| needStartScan | boolean | 是 | 是否需要发起WLAN扫描。需要发起WLAN扫描设置为true。不需要发起WLAN扫描，使用最近一次WLAN扫描结果进行匹配设置为false。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | 表示匹配是否成功。当扫描结果中存在wlanBssidArray中的任意BSSID，且其RSSI值高于rssiThreshold时，返回true，否则返回false。 |

**错误码**：

以下错误码的详细介绍请参见[位置服务子系统错误码](位置服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 801 | Capability not supported. Failed to call ${geoLocationManager.isWlanBssidMatched} due to limited device capabilities. |
| 3301100 | The location switch is off. |
| 3301800 | Failed to start WiFi scanning. |

**示例**

```ets
import { geoLocationManager } from '@kit.LocationKit';
try {
  let wlanBssidArray: Array<string> = ["02:1b:32:23:ea:91", "02:1b:32:23:ea:93"];
  let rssiThreshold: number = -70;
  let needStartScan: boolean = true;
  geoLocationManager.isWlanBssidMatched(wlanBssidArray, rssiThreshold, needStartScan).then((res) => {
        console.info("Wlan Bssid Matched Result:" + res);
  })
} catch(error) {
  console.error("isWlanBssidMatched: errCode" + error.code + ", errMessage" + error.message);
}
```

**geoLocationManager.getActiveGeoFences23+**

getActiveGeoFences(): Promise<Map<int, Geofence>>

查询当前有效的围栏信息。使用Promise异步回调。

需要权限：ohos.permission.LOCATION 和 ohos.permission.APPROXIMATELY_LOCATION

系统能力：SystemCapability.Location.Location.Geofence

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<Map<int, Geofence>> | Promise对象，返回有效的围栏信息。Map中的key值为fenceId，value值为对应围栏的具体信息。 |

错误码：

以下错误码的详细介绍请参见[位置服务子系统错误码](位置服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 801 | Capability not supported. Failed to call ${geoLocationManager.getActiveGeoFences} due to limited device capabilities. |

示例

```ets
import { geoLocationManager } from '@kit.LocationKit';

try {
  geoLocationManager.getActiveGeoFences().then((res) => {
    if (res) {
      console.info("fence num:" + res.size);
      for (const item of res) {
        console.info("data=" + JSON.stringify(item));
      }
  })
    .catch((error: BusinessError) => {
      console.error('promise, getActiveGeoFences: error=' + JSON.stringify(error));
    });
} catch (error) {
  console.error("getActiveGeoFences: errCode" + error.code + ", errMessage" + error.message);
}
```