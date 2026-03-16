# @ohos.geolocation (位置服务)

位置服务提供GNSS定位、网络定位、地理编码、逆地理编码、国家码和地理围栏等基本功能。

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

从API Version 9开始，该接口不再维护，推荐使用新接口[geoLocationManager](@ohos.geoLocationManager (位置服务).md)。

本模块能力仅支持WGS-84坐标系。

#### 申请权限

应用在使用系统能力前，需要检查是否已经获取用户授权访问设备位置信息。如未获得授权，可以向用户申请需要的位置权限，申请方式请参考下文。

系统提供的定位权限有：

-

ohos.permission.LOCATION

-

ohos.permission.APPROXIMATELY_LOCATION

-

ohos.permission.LOCATION_IN_BACKGROUND

访问设备的位置信息，必须申请权限，并且获得用户授权。

API9之前的版本，申请ohos.permission.LOCATION即可。

API9及之后的版本，需要申请ohos.permission.APPROXIMATELY_LOCATION或者同时申请ohos.permission.APPROXIMATELY_LOCATION和ohos.permission.LOCATION；无法单独申请ohos.permission.LOCATION。

使用的API版本申请位置权限申请结果位置的精确度小于9ohos.permission.LOCATION成功获取到精准位置，精准度在米级别。大于等于9ohos.permission.LOCATION失败无法获取位置。大于等于9ohos.permission.APPROXIMATELY_LOCATION成功获取到模糊位置，精确度为5公里。大于等于9ohos.permission.APPROXIMATELY_LOCATION和ohos.permission.LOCATION成功获取到精准位置，精准度在米级别。

如果应用在后台运行时也需要访问设备位置，需要申请LOCATION类型的长时任务，这样应用在切入后台之后，系统可以继续上报位置信息。长时任务申请可参考[长时任务](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/continuous-task)。

应用如需使用ohos.permission.LOCATION_IN_BACKGROUND权限，需要在设置界面由用户手动授予，具体授权方式可参考[ohos.permission.LOCATION_IN_BACKGROUND权限说明](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/permissions-for-all-user#ohospermissionlocation_in_background)。

开发者可以在应用配置文件中声明所需要的权限，具体可参考[向用户申请授权](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/request-user-authorization)。

#### 导入模块

```ets
import geolocation from '@ohos.geolocation';
```

#### geolocation.on('locationChange')(deprecated)

on(type: 'locationChange', request: LocationRequest, callback: Callback<Location>): void

开启位置变化订阅，并发起定位请求。使用callback异步回调。

从API version 9开始废弃，建议使用[geoLocationManager.on('locationChange')](@ohos.geoLocationManager (位置服务).md#ZH-CN_TOPIC_0000002497606102__geolocationmanageronlocationchange)替代。

**需要权限**：ohos.permission.LOCATION

**系统能力**：SystemCapability.Location.Location.Core

**参数：**

参数名类型必填说明typestring是设置事件类型。type为“locationChange”，表示位置变化。request[LocationRequest](#ZH-CN_TOPIC_0000002497606104__locationrequestdeprecated)是设置位置请求参数。callbackCallback<[Location](#ZH-CN_TOPIC_0000002497606104__locationdeprecated)>是回调函数，返回位置信息。

**示例**

```ets
import geolocation from '@ohos.geolocation';
let requestInfo:geolocation.LocationRequest = {'priority': 0x203, 'scenario': 0x300, 'timeInterval': 0, 'distanceInterval': 0, 'maxAccuracy': 0};
let locationChange = (location:geolocation.Location):void => {
    console.info('locationChanger: data: ' + JSON.stringify(location));
};
geolocation.on('locationChange', requestInfo, locationChange);
```

#### geolocation.off('locationChange')(deprecated)

off(type: 'locationChange', callback?: Callback<Location>): void

关闭位置变化订阅，并删除对应的定位请求。

从API version 9开始废弃，建议使用[geoLocationManager.off('locationChange')](@ohos.geoLocationManager (位置服务).md#ZH-CN_TOPIC_0000002497606102__geolocationmanagerofflocationchange)替代。

**需要权限**：ohos.permission.LOCATION

**系统能力**：SystemCapability.Location.Location.Core

**参数：**

参数名类型必填说明typestring是设置事件类型。type为“locationChange”，表示位置变化。callbackCallback<[Location](#ZH-CN_TOPIC_0000002497606104__locationdeprecated)>否需要取消订阅的回调函数。该回调函数需要与on接口传入的回调函数保持一致。若无此参数，则取消当前类型的所有订阅。

**示例**

```ets
import geolocation from '@ohos.geolocation';
let requestInfo:geolocation.LocationRequest = {'priority': 0x203, 'scenario': 0x300, 'timeInterval': 0, 'distanceInterval': 0, 'maxAccuracy': 0};
let locationChange = (location:geolocation.Location):void => {
    console.info('locationChanger: data: ' + JSON.stringify(location));
};
geolocation.on('locationChange', requestInfo, locationChange);
geolocation.off('locationChange', locationChange);
```

#### geolocation.on('locationServiceState')(deprecated)

on(type: 'locationServiceState', callback: Callback<boolean>): void

订阅位置服务状态变化。使用callback异步回调。

从API version 9开始废弃，建议使用[geoLocationManager.on('locationEnabledChange')](@ohos.geoLocationManager (位置服务).md#ZH-CN_TOPIC_0000002497606102__geolocationmanageronlocationenabledchange)替代。

**需要权限**：ohos.permission.LOCATION

**系统能力**：SystemCapability.Location.Location.Core

**参数：**

参数名类型必填说明typestring是设置事件类型。type为“locationServiceState”，表示位置服务状态。callbackCallback<boolean>是回调函数。返回true表示打开位置服务；返回false表示关闭位置服务。

**示例**

```ets
import geolocation from '@ohos.geolocation';
let locationServiceState = (state:boolean):void => {
    console.info('locationServiceState: ' + JSON.stringify(state));
}
geolocation.on('locationServiceState', locationServiceState);
```

#### geolocation.off('locationServiceState')(deprecated)

off(type: 'locationServiceState', callback?: Callback<boolean>): void

取消订阅位置服务状态变化。

从API version 9开始废弃，建议使用[geoLocationManager.off('locationEnabledChange')](@ohos.geoLocationManager (位置服务).md#ZH-CN_TOPIC_0000002497606102__geolocationmanagerofflocationenabledchange)替代。

**需要权限**：ohos.permission.LOCATION

**系统能力**：SystemCapability.Location.Location.Core

**参数**：

参数名类型必填说明typestring是设置事件类型。type为“locationServiceState”，表示位置服务状态。callbackCallback<boolean>否需要取消订阅的回调函数。Callback返回true表示位置服务处于开启状态；返回false表示位置服务处于关闭状态。该回调函数需要与on接口传入的回调函数保持一致。若无此参数，则取消当前类型的所有订阅。

**示例**

```ets
import geolocation from '@ohos.geolocation';
let locationServiceState = (state:boolean):void => {
    console.info('locationServiceState: state: ' + JSON.stringify(state));
}
geolocation.on('locationServiceState', locationServiceState);
geolocation.off('locationServiceState', locationServiceState);
```

#### geolocation.on('cachedGnssLocationsReporting')(deprecated)

on(type: 'cachedGnssLocationsReporting', request: CachedGnssLocationsRequest, callback: Callback<Array<Location>>): void

订阅缓存GNSS定位结果上报事件。使用callback异步回调。

从API version 8开始支持。

从API version 9开始废弃，建议使用[geoLocationManager.on('cachedGnssLocationsChange')](@ohos.geoLocationManager (位置服务).md#ZH-CN_TOPIC_0000002497606102__geolocationmanageroncachedgnsslocationschange)替代。

**需要权限**：ohos.permission.LOCATION

**系统能力**：SystemCapability.Location.Location.Gnss

**参数**：

参数名类型必填说明typestring是设置事件类型。type为“cachedGnssLocationsReporting”，表示GNSS缓存定位结果上报。request[CachedGnssLocationsRequest](#ZH-CN_TOPIC_0000002497606104__cachedgnsslocationsrequestdeprecated)是GNSS缓存功能配置参数。callbackCallback<Array<[Location](#ZH-CN_TOPIC_0000002497606104__locationdeprecated)>>是回调函数，返回GNSS缓存位置。

**示例**

```ets
import geolocation from '@ohos.geolocation';
let cachedLocationsCb = (locations:Array<geolocation.Location>):void => {
    console.info('cachedGnssLocationsReporting: locations: ' + JSON.stringify(locations));
}
let requestInfo:geolocation.CachedGnssLocationsRequest = {'reportingPeriodSec': 10, 'wakeUpCacheQueueFull': true};
geolocation.on('cachedGnssLocationsReporting', requestInfo, cachedLocationsCb);
```

#### geolocation.off('cachedGnssLocationsReporting')(deprecated)

off(type: 'cachedGnssLocationsReporting', callback?: Callback<Array<Location>>): void

取消订阅缓存GNSS定位结果上报事件。

从API version 8开始支持。

从API version 9开始废弃，建议使用[geoLocationManager.off('cachedGnssLocationsChange')](@ohos.geoLocationManager (位置服务).md#ZH-CN_TOPIC_0000002497606102__geolocationmanageroffcachedgnsslocationschange)替代。

**需要权限**：ohos.permission.LOCATION

**系统能力**：SystemCapability.Location.Location.Gnss

**参数**：

参数名类型必填说明typestring是设置事件类型。type为“cachedGnssLocationsReporting”，表示GNSS缓存定位结果上报。callbackCallback<Array<[Location](#ZH-CN_TOPIC_0000002497606104__locationdeprecated)>>否需要取消订阅的回调函数。该回调函数需要与on接口传入的回调函数保持一致。若无此参数，则取消当前类型的所有订阅。

**示例**

```ets
import geolocation from '@ohos.geolocation';
let cachedLocationsCb = (locations:Array<geolocation.Location>):void => {
    console.info('cachedGnssLocationsReporting: locations: ' + JSON.stringify(locations));
}
let requestInfo:geolocation.CachedGnssLocationsRequest = {'reportingPeriodSec': 10, 'wakeUpCacheQueueFull': true};
geolocation.on('cachedGnssLocationsReporting', requestInfo, cachedLocationsCb);
geolocation.off('cachedGnssLocationsReporting');
```

#### geolocation.on('gnssStatusChange')(deprecated)

on(type: 'gnssStatusChange', callback: Callback<SatelliteStatusInfo>): void

订阅GNSS卫星状态信息上报事件。使用callback异步回调。

从API version 8开始支持。

从API version 9开始废弃，建议使用[geoLocationManager.on('satelliteStatusChange')](@ohos.geoLocationManager (位置服务).md#ZH-CN_TOPIC_0000002497606102__geolocationmanageronsatellitestatuschange)替代。

**需要权限**：ohos.permission.LOCATION

**系统能力**：SystemCapability.Location.Location.Gnss

**参数**：

参数名类型必填说明typestring是设置事件类型。type为“gnssStatusChange”，表示订阅GNSS卫星状态信息上报。callbackCallback<[SatelliteStatusInfo](#ZH-CN_TOPIC_0000002497606104__satellitestatusinfodeprecated)>是回调函数，返回GNSS卫星状态信息。

**示例**

```ets
import geolocation from '@ohos.geolocation';
let gnssStatusCb = (satelliteStatusInfo:geolocation.SatelliteStatusInfo):void => {
    console.info('gnssStatusChange: ' + JSON.stringify(satelliteStatusInfo));
}
geolocation.on('gnssStatusChange', gnssStatusCb);
```

#### geolocation.off('gnssStatusChange')(deprecated)

off(type: 'gnssStatusChange', callback?: Callback<SatelliteStatusInfo>): void

取消订阅GNSS卫星状态信息上报事件。

从API version 8开始支持。

从API version 9开始废弃，建议使用[geoLocationManager.off('satelliteStatusChange')](@ohos.geoLocationManager (位置服务).md#ZH-CN_TOPIC_0000002497606102__geolocationmanageroffsatellitestatuschange)替代。

**需要权限**：ohos.permission.LOCATION

**系统能力**：SystemCapability.Location.Location.Gnss

**参数**：

参数名类型必填说明typestring是设置事件类型。type为“gnssStatusChange”，表示订阅GNSS卫星状态信息上报。callbackCallback<[SatelliteStatusInfo](#ZH-CN_TOPIC_0000002497606104__satellitestatusinfodeprecated)>否需要取消订阅的回调函数。该回调函数需要与on接口传入的回调函数保持一致。若无此参数，则取消当前类型的所有订阅。

**示例**

```ets
import geolocation from '@ohos.geolocation';
let gnssStatusCb = (satelliteStatusInfo:geolocation.SatelliteStatusInfo) => {
    console.info('gnssStatusChange: ' + JSON.stringify(satelliteStatusInfo));
}
geolocation.on('gnssStatusChange', gnssStatusCb);
geolocation.off('gnssStatusChange', gnssStatusCb);
```

#### geolocation.on('nmeaMessageChange')(deprecated)

on(type: 'nmeaMessageChange', callback: Callback<string>): void

订阅GNSS NMEA信息上报事件。使用callback异步回调。

从API version 8开始支持。

从API version 9开始废弃，建议使用[geoLocationManager.on('nmeaMessage')](@ohos.geoLocationManager (位置服务).md#ZH-CN_TOPIC_0000002497606102__geolocationmanageronnmeamessage)替代。

**需要权限**：ohos.permission.LOCATION

**系统能力**：SystemCapability.Location.Location.Gnss

**参数**：

参数名类型必填说明typestring是设置事件类型。type为“nmeaMessageChange”，表示订阅GNSS NMEA信息上报。callbackCallback<string>是回调函数，返回GNSS NMEA信息。

**示例**

```ets
import geolocation from '@ohos.geolocation';
let nmeaCb = (str:string):void => {
    console.info('nmeaMessageChange: ' + JSON.stringify(str));
}
geolocation.on('nmeaMessageChange', nmeaCb );
```

#### geolocation.off('nmeaMessageChange')(deprecated)

off(type: 'nmeaMessageChange', callback?: Callback<string>): void

取消订阅GNSS NMEA信息上报事件。

从API version 8开始支持。

从API version 9开始废弃，建议使用[geoLocationManager.off('nmeaMessage')](@ohos.geoLocationManager (位置服务).md#ZH-CN_TOPIC_0000002497606102__geolocationmanageroffnmeamessage)替代。

**需要权限**：ohos.permission.LOCATION

**系统能力**：SystemCapability.Location.Location.Gnss

**参数**：

参数名类型必填说明typestring是设置事件类型。type为“nmeaMessageChange”，表示订阅GNSS NMEA信息上报。callbackCallback<string>否需要取消订阅的回调函数。该回调函数需要与on接口传入的回调函数保持一致。若无此参数，则取消当前类型的所有订阅。

**示例**

```ets
import geolocation from '@ohos.geolocation';
let nmeaCb = (str:string):void => {
    console.info('nmeaMessageChange: ' + JSON.stringify(str));
}
geolocation.on('nmeaMessageChange', nmeaCb);
geolocation.off('nmeaMessageChange', nmeaCb);
```

#### geolocation.on('fenceStatusChange')(deprecated)

on(type: 'fenceStatusChange', request: GeofenceRequest, want: WantAgent): void

添加一个围栏，并订阅地理围栏事件。使用callback异步回调。

从API version 8开始支持。

从API version 9开始废弃，建议使用[geoLocationManager.on('gnssFenceStatusChange')](@ohos.geoLocationManager (位置服务).md#ZH-CN_TOPIC_0000002497606102__geolocationmanagerongnssfencestatuschange)替代。

**需要权限**：ohos.permission.LOCATION

**系统能力**：SystemCapability.Location.Location.Geofence

**参数**：

参数名类型必填说明typestring是设置事件类型。type为“fenceStatusChange”，表示订阅围栏事件上报。request[GeofenceRequest](#ZH-CN_TOPIC_0000002497606104__geofencerequestdeprecated)是围栏的配置参数。want[WantAgent](@ohos.app.ability.wantAgent (WantAgent模块).md)是用于接收地理围栏事件上报（进出围栏）。

**示例**

```ets
import geolocation from '@ohos.geolocation';
import wantAgent from '@ohos.app.ability.wantAgent';

let wantAgentInfo:wantAgent.WantAgentInfo = {
    wants: [
        {
            bundleName: "com.example.myapplication",
            abilityName: "EntryAbility",
            action: "action1"
        }
    ],
    operationType: wantAgent.OperationType.START_ABILITY,
    requestCode: 0,
    wantAgentFlags: [wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG],
};

wantAgent.getWantAgent(wantAgentInfo).then((wantAgentObj) => {
  let requestInfo:geolocation.GeofenceRequest = {'priority': 0x201, 'scenario': 0x301, "geofence": {"latitude": 31.12, "longitude": 121.11, "radius": 100, "expiration": 10000}};
  geolocation.on('fenceStatusChange', requestInfo, wantAgentObj);
});
```

#### geolocation.off('fenceStatusChange')(deprecated)

off(type: 'fenceStatusChange', request: GeofenceRequest, want: WantAgent): void

删除一个围栏，并取消订阅该围栏事件。

从API version 8开始支持。

从API version 9开始废弃，建议使用[geoLocationManager.off('gnssFenceStatusChange')](@ohos.geoLocationManager (位置服务).md#ZH-CN_TOPIC_0000002497606102__geolocationmanageroffgnssfencestatuschange)替代。

**需要权限**：ohos.permission.LOCATION

**系统能力**：SystemCapability.Location.Location.Geofence

**参数**：

参数名类型必填说明typestring是设置事件类型。type为“fenceStatusChange”，表示订阅围栏事件上报。request[GeofenceRequest](#ZH-CN_TOPIC_0000002497606104__geofencerequestdeprecated)是围栏的配置参数。want[WantAgent](@ohos.app.ability.wantAgent (WantAgent模块).md)是用于接收地理围栏事件上报（进出围栏）。

**示例**

```ets
import geolocation from '@ohos.geolocation';
import wantAgent from '@ohos.app.ability.wantAgent';

let wantAgentInfo:wantAgent.WantAgentInfo = {
    wants: [
        {
            bundleName: "com.example.myapplication",
            abilityName: "EntryAbility",
            action: "action1",
        }
    ],
    operationType: wantAgent.OperationType.START_ABILITY,
    requestCode: 0,
    wantAgentFlags: [wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
};

wantAgent.getWantAgent(wantAgentInfo).then((wantAgentObj) => {
  let requestInfo:geolocation.GeofenceRequest = {'priority': 0x201, 'scenario': 0x301, "geofence": {"latitude": 31.12, "longitude": 121.11, "radius": 100, "expiration": 10000}};
  geolocation.on('fenceStatusChange', requestInfo, wantAgentObj);
  geolocation.off('fenceStatusChange', requestInfo, wantAgentObj);
});
```

#### geolocation.getCurrentLocation(deprecated)

getCurrentLocation(request: CurrentLocationRequest, callback: AsyncCallback<Location>): void

获取当前位置，使用callback异步回调。

从API version 9开始废弃，建议使用[geoLocationManager.getCurrentLocation](@ohos.geoLocationManager (位置服务).md#ZH-CN_TOPIC_0000002497606102__geolocationmanagergetcurrentlocation)替代。

**需要权限**：ohos.permission.LOCATION

**系统能力**：SystemCapability.Location.Location.Core

**参数**：

参数名类型必填说明request[CurrentLocationRequest](#ZH-CN_TOPIC_0000002497606104__currentlocationrequestdeprecated)是设置位置请求参数。callbackAsyncCallback<[Location](#ZH-CN_TOPIC_0000002497606104__locationdeprecated)>是回调函数，返回当前位置信息。

**示例**

```ets
import geolocation from '@ohos.geolocation';
import BusinessError from "@ohos.base"
let requestInfo:geolocation.CurrentLocationRequest = {'priority': 0x203, 'scenario': 0x300,'maxAccuracy': 0};
let locationChange = (err:BusinessError.BusinessError, location:geolocation.Location) => {
    if (err) {
        console.info('locationChanger: err=' + JSON.stringify(err));
    }
    if (location) {
        console.info('locationChanger: location=' + JSON.stringify(location));
    }
};
geolocation.getCurrentLocation(requestInfo, locationChange);
```

#### geolocation.getCurrentLocation(deprecated)

getCurrentLocation(callback: AsyncCallback<Location>): void

获取当前位置，使用callback异步回调。

从API version 9开始废弃，建议使用[geoLocationManager.getCurrentLocation](@ohos.geoLocationManager (位置服务).md#ZH-CN_TOPIC_0000002497606102__geolocationmanagergetcurrentlocation)替代。

**需要权限**：ohos.permission.LOCATION

**系统能力**：SystemCapability.Location.Location.Core

**参数**：

参数名类型必填说明callbackAsyncCallback<[Location](#ZH-CN_TOPIC_0000002497606104__locationdeprecated)>是回调函数，返回当前位置信息。

**示例**

```ets
import geolocation from '@ohos.geolocation';
import BusinessError from "@ohos.base"
let locationChange = (err:BusinessError.BusinessError, location:geolocation.Location):void => {
    if (err) {
        console.info('locationChanger: err=' + JSON.stringify(err));
    }
    if (location) {
        console.info('locationChanger: location=' + JSON.stringify(location));
    }
};
geolocation.getCurrentLocation(locationChange);
```

#### geolocation.getCurrentLocation(deprecated)

getCurrentLocation(request?: CurrentLocationRequest): Promise<Location>

获取当前位置，使用Promise异步回调。

从API version 9开始废弃，建议使用[geoLocationManager.getCurrentLocation](@ohos.geoLocationManager (位置服务).md#ZH-CN_TOPIC_0000002497606102__geolocationmanagergetcurrentlocation-2)替代。

**需要权限**：ohos.permission.LOCATION

**系统能力**：SystemCapability.Location.Location.Core

**参数**：

参数名类型必填说明request[CurrentLocationRequest](#ZH-CN_TOPIC_0000002497606104__currentlocationrequestdeprecated)否设置位置请求参数。

**返回值**：

类型说明Promise<[Location](#ZH-CN_TOPIC_0000002497606104__locationdeprecated)>Promise对象，返回当前位置信息。

**示例**

```ets
import geolocation from '@ohos.geolocation';
let requestInfo:geolocation.CurrentLocationRequest = {'priority': 0x203, 'scenario': 0x300,'maxAccuracy': 0};
geolocation.getCurrentLocation(requestInfo).then((result) => {
    console.info('current location: ' + JSON.stringify(result));
});
```

#### geolocation.getLastLocation(deprecated)

getLastLocation(callback: AsyncCallback<Location>): void

获取上一次位置，使用callback异步回调。

从API version 9开始废弃，建议使用[geoLocationManager.getLastLocation](@ohos.geoLocationManager (位置服务).md#ZH-CN_TOPIC_0000002497606102__geolocationmanagergetlastlocation)替代。

**需要权限**：ohos.permission.LOCATION

**系统能力**：SystemCapability.Location.Location.Core

**参数**：

参数名类型必填说明callbackAsyncCallback<[Location](#ZH-CN_TOPIC_0000002497606104__locationdeprecated)>是回调函数，返回上次位置信息。

**示例**

```ets
import geolocation from '@ohos.geolocation';
geolocation.getLastLocation((err, data) => {
    if (err) {
        console.info('getLastLocation: err=' + JSON.stringify(err));
    }
    if (data) {
        console.info('getLastLocation: data=' + JSON.stringify(data));
    }
});
```

#### geolocation.getLastLocation(deprecated)

getLastLocation(): Promise<Location>

获取上一次位置，使用Promise异步回调。

从API version 9开始废弃，建议使用[geoLocationManager.getLastLocation](@ohos.geoLocationManager (位置服务).md#ZH-CN_TOPIC_0000002497606102__geolocationmanagergetlastlocation)替代。

**需要权限**：ohos.permission.LOCATION

**系统能力**：SystemCapability.Location.Location.Core

**返回值**：

类型说明Promise<[Location](#ZH-CN_TOPIC_0000002497606104__locationdeprecated)>Promise对象，返回上次位置信息。

**示例**

```ets
import geolocation from '@ohos.geolocation';
geolocation.getLastLocation().then((result) => {
    console.info('getLastLocation: result: ' + JSON.stringify(result));
});
```

#### geolocation.isLocationEnabled(deprecated)

isLocationEnabled(callback: AsyncCallback<boolean>): void

判断位置服务是否已经打开，使用callback异步回调。

从API version 9开始废弃，建议使用[geoLocationManager.isLocationEnabled](@ohos.geoLocationManager (位置服务).md#ZH-CN_TOPIC_0000002497606102__geolocationmanagerislocationenabled)替代。

**需要权限**：ohos.permission.LOCATION

**系统能力**：SystemCapability.Location.Location.Core

**参数**：

参数名类型必填说明callbackAsyncCallback<boolean>是回调函数。返回true表示位置服务已经开启；返回false表示位置服务已经关闭。

**示例**

```ets
import geolocation from '@ohos.geolocation';
geolocation.isLocationEnabled((err, data) => {
    if (err) {
        console.info('isLocationEnabled: err=' + JSON.stringify(err));
    }
    if (data) {
        console.info('isLocationEnabled: data=' + JSON.stringify(data));
    }
});
```

#### geolocation.isLocationEnabled(deprecated)

isLocationEnabled(): Promise<boolean>

判断位置服务是否已经开启，使用Promise异步回调。

从API version 9开始废弃，建议使用[geoLocationManager.isLocationEnabled](@ohos.geoLocationManager (位置服务).md#ZH-CN_TOPIC_0000002497606102__geolocationmanagerislocationenabled)替代。

**需要权限**：ohos.permission.LOCATION

**系统能力**：SystemCapability.Location.Location.Core

**返回值**：

类型说明Promise<boolean>Promise对象，返回true表示位置服务已经开启；返回false表示位置服务已经关闭。

**示例**

```ets
import geolocation from '@ohos.geolocation';
geolocation.isLocationEnabled().then((result) => {
    console.info('promise, isLocationEnabled: ' + JSON.stringify(result));
});
```

#### geolocation.requestEnableLocation(deprecated)

requestEnableLocation(callback: AsyncCallback<boolean>): void

请求打开位置服务，使用callback异步回调。

从API version 9开始废弃，建议由应用本身弹框请求用户跳转到settings开启位置开关，并且在弹框上写清楚会在什么场景下使用位置信息。

**需要权限**：ohos.permission.LOCATION

**系统能力**：SystemCapability.Location.Location.Core

**参数**：

参数名类型必填说明callbackAsyncCallback<boolean>是回调函数。返回true表示打开位置服务；返回false表示关闭位置服务。

**示例**

```ets
import geolocation from '@ohos.geolocation';
geolocation.requestEnableLocation((err, data) => {
    if (err) {
        console.info('requestEnableLocation: err=' + JSON.stringify(err));
    }
    if (data) {
        console.info('requestEnableLocation: data=' + JSON.stringify(data));
    }
});
```

#### geolocation.requestEnableLocation(deprecated)

requestEnableLocation(): Promise<boolean>

请求打开位置服务，使用Promise异步回调。

从API version 9开始废弃，建议由应用本身弹框请求用户跳转到settings开启位置开关，并且在弹框上写清楚会在什么场景下使用位置信息。

**需要权限**：ohos.permission.LOCATION

**系统能力**：SystemCapability.Location.Location.Core

**返回值**：

类型说明Promise<boolean>Promise对象，返回true表示位置服务已经开启；返回false表示位置服务已经关闭。

**示例**

```ets
import geolocation from '@ohos.geolocation';
geolocation.requestEnableLocation().then((result) => {
    console.info('promise, requestEnableLocation: ' + JSON.stringify(result));
});
```

#### geolocation.isGeoServiceAvailable(deprecated)

isGeoServiceAvailable(callback: AsyncCallback<boolean>): void

判断（逆）地理编码服务状态，使用callback异步回调。

从API version 9开始废弃，建议使用[geoLocationManager.isGeocoderAvailable](@ohos.geoLocationManager (位置服务).md#ZH-CN_TOPIC_0000002497606102__geolocationmanagerisgeocoderavailable)替代。

**需要权限**：ohos.permission.LOCATION

**系统能力**：SystemCapability.Location.Location.Geocoder

**参数**：

参数名类型必填说明callbackAsyncCallback<boolean>是回调函数，返回true表示地理编码服务可用；返回false表示地理编码服务不可用。

**示例**

```ets
import geolocation from '@ohos.geolocation';
geolocation.isGeoServiceAvailable((err, data) => {
    if (err) {
        console.info('isGeoServiceAvailable: err=' + JSON.stringify(err));
    }
    if (data) {
        console.info('isGeoServiceAvailable: data=' + JSON.stringify(data));
    }
});
```

#### geolocation.isGeoServiceAvailable(deprecated)

isGeoServiceAvailable(): Promise<boolean>

判断（逆）地理编码服务状态，使用Promise异步回调。

从API version 9开始废弃，建议使用[geoLocationManager.isGeocoderAvailable](@ohos.geoLocationManager (位置服务).md#ZH-CN_TOPIC_0000002497606102__geolocationmanagerisgeocoderavailable)替代。

**需要权限**：ohos.permission.LOCATION

**系统能力**：SystemCapability.Location.Location.Geocoder

**返回值**：

类型说明Promise<boolean>Promise对象，返回true表示地理编码服务可用；返回false表示地理编码服务不可用。

**示例**

```ets
import geolocation from '@ohos.geolocation';
geolocation.isGeoServiceAvailable().then((result) => {
    console.info('promise, isGeoServiceAvailable: ' + JSON.stringify(result));
});
```

#### geolocation.getAddressesFromLocation(deprecated)

getAddressesFromLocation(request: ReverseGeoCodeRequest, callback: AsyncCallback<Array<GeoAddress>>): void

调用逆地理编码服务，将坐标转换为地理描述，使用callback异步回调。

从API version 9开始废弃，建议使用[geoLocationManager.getAddressesFromLocation](@ohos.geoLocationManager (位置服务).md#ZH-CN_TOPIC_0000002497606102__geolocationmanagergetaddressesfromlocation)替代。

**需要权限**：ohos.permission.LOCATION

**系统能力**：SystemCapability.Location.Location.Geocoder

**参数**：

参数名类型必填说明request[ReverseGeoCodeRequest](#ZH-CN_TOPIC_0000002497606104__reversegeocoderequestdeprecated)是设置逆地理编码请求的相关参数。callbackAsyncCallback<Array<[GeoAddress](#ZH-CN_TOPIC_0000002497606104__geoaddressdeprecated)>>是回调函数，返回逆地理编码结果。

**示例**

```ets
import geolocation from '@ohos.geolocation';
let reverseGeocodeRequest:geolocation.ReverseGeoCodeRequest = {"latitude": 31.12, "longitude": 121.11, "maxItems": 1};
geolocation.getAddressesFromLocation(reverseGeocodeRequest, (err, data) => {
    if (err) {
        console.info('getAddressesFromLocation: err=' + JSON.stringify(err));
    }
    if (data) {
        console.info('getAddressesFromLocation: data=' + JSON.stringify(data));
    }
});
```

#### geolocation.getAddressesFromLocation(deprecated)

getAddressesFromLocation(request: ReverseGeoCodeRequest): Promise<Array<GeoAddress>>

调用逆地理编码服务，将坐标转换为地理描述，使用Promise异步回调。

从API version 9开始废弃，建议使用[geoLocationManager.getAddressesFromLocation](@ohos.geoLocationManager (位置服务).md#ZH-CN_TOPIC_0000002497606102__geolocationmanagergetaddressesfromlocation-1)替代。

**需要权限**：ohos.permission.LOCATION

**系统能力**：SystemCapability.Location.Location.Geocoder

**参数**：

参数名类型必填说明request[ReverseGeoCodeRequest](#ZH-CN_TOPIC_0000002497606104__reversegeocoderequestdeprecated)是设置逆地理编码请求的相关参数。

**返回值**：

类型说明Promise<Array<[GeoAddress](#ZH-CN_TOPIC_0000002497606104__geoaddressdeprecated)>>Promise对象，返回地理描述信息。

**示例**

```ets
import geolocation from '@ohos.geolocation';
let reverseGeocodeRequest:geolocation.ReverseGeoCodeRequest = {"latitude": 31.12, "longitude": 121.11, "maxItems": 1};
geolocation.getAddressesFromLocation(reverseGeocodeRequest).then((data) => {
    console.info('getAddressesFromLocation: ' + JSON.stringify(data));
});
```

#### geolocation.getAddressesFromLocationName(deprecated)

getAddressesFromLocationName(request: GeoCodeRequest, callback: AsyncCallback<Array<GeoAddress>>): void

调用地理编码服务，将地理描述转换为具体坐标，使用callback异步回调。

从API version 9开始废弃，建议使用[geoLocationManager.getAddressesFromLocationName](@ohos.geoLocationManager (位置服务).md#ZH-CN_TOPIC_0000002497606102__geolocationmanagergetaddressesfromlocationname)替代。

**需要权限**：ohos.permission.LOCATION

**系统能力**：SystemCapability.Location.Location.Geocoder

**参数**：

参数名类型必填说明request[GeoCodeRequest](#ZH-CN_TOPIC_0000002497606104__geocoderequestdeprecated)是设置地理编码请求的相关参数。callbackAsyncCallback<Array<[GeoAddress](#ZH-CN_TOPIC_0000002497606104__geoaddressdeprecated)>>是回调函数，返回地理编码结果。

**示例**

```ets
import geolocation from '@ohos.geolocation';
let geocodeRequest:geolocation.GeoCodeRequest = {"description": "上海市浦东新区xx路xx号", "maxItems": 1};
geolocation.getAddressesFromLocationName(geocodeRequest, (err, data) => {
    if (err) {
        console.info('getAddressesFromLocationName: err=' + JSON.stringify(err));
    }
    if (data) {
        console.info('getAddressesFromLocationName: data=' + JSON.stringify(data));
    }
});
```

#### geolocation.getAddressesFromLocationName(deprecated)

getAddressesFromLocationName(request: GeoCodeRequest): Promise<Array<GeoAddress>>

调用地理编码服务，将地理描述转换为具体坐标，使用Promise异步回调。

从API version 9开始废弃，建议使用[geoLocationManager.getAddressesFromLocationName](@ohos.geoLocationManager (位置服务).md#ZH-CN_TOPIC_0000002497606102__geolocationmanagergetaddressesfromlocationname-1)替代。

**需要权限**：ohos.permission.LOCATION

**系统能力**：SystemCapability.Location.Location.Geocoder

**参数**：

参数名类型必填说明request[GeoCodeRequest](#ZH-CN_TOPIC_0000002497606104__geocoderequestdeprecated)是设置地理编码请求的相关参数。

**返回值**：

类型说明Promise<Array<[GeoAddress](#ZH-CN_TOPIC_0000002497606104__geoaddressdeprecated)>>Promise对象，返回地理编码查询结果。

**示例**

```ets
import geolocation from '@ohos.geolocation';
let geocodeRequest:geolocation.GeoCodeRequest = {"description": "上海市浦东新区xx路xx号", "maxItems": 1};
geolocation.getAddressesFromLocationName(geocodeRequest).then((result) => {
    console.info('getAddressesFromLocationName: ' + JSON.stringify(result));
});
```

#### geolocation.getCachedGnssLocationsSize(deprecated)

getCachedGnssLocationsSize(callback: AsyncCallback<number>): void

获取GNSS芯片缓存位置的个数。使用callback异步回调。

从API version 8开始支持。

从API version 9开始废弃，建议使用[geoLocationManager.getCachedGnssLocationsSize](@ohos.geoLocationManager (位置服务).md#ZH-CN_TOPIC_0000002497606102__geolocationmanagergetcachedgnsslocationssize)替代。

**需要权限**：ohos.permission.LOCATION

**系统能力**：SystemCapability.Location.Location.Gnss

**参数**：

参数名类型必填说明callbackAsyncCallback<number>是回调函数，返回GNSS芯片缓存位置个数。

**示例**

```ets
import geolocation from '@ohos.geolocation';
geolocation.getCachedGnssLocationsSize((err, size) => {
    if (err) {
        console.info('getCachedGnssLocationsSize: err=' + JSON.stringify(err));
    }
    if (size) {
        console.info('getCachedGnssLocationsSize: size=' + JSON.stringify(size));
    }
});
```

#### geolocation.getCachedGnssLocationsSize(deprecated)

getCachedGnssLocationsSize(): Promise<number>;

获取GNSS芯片缓存位置的个数。使用Promise异步回调。

从API version 8开始支持。

从API version 9开始废弃，建议使用[geoLocationManager.getCachedGnssLocationsSize](@ohos.geoLocationManager (位置服务).md#ZH-CN_TOPIC_0000002497606102__geolocationmanagergetcachedgnsslocationssize-1)替代。

**需要权限**：ohos.permission.LOCATION

**系统能力**：SystemCapability.Location.Location.Gnss

**返回值**：

类型说明Promise<number>Promise对象，返回GNSS缓存位置的个数。

**示例**

```ets
import geolocation from '@ohos.geolocation';
geolocation.getCachedGnssLocationsSize().then((result) => {
    console.info('promise, getCachedGnssLocationsSize: ' + JSON.stringify(result));
});
```

#### geolocation.flushCachedGnssLocations(deprecated)

flushCachedGnssLocations(callback: AsyncCallback<boolean>): void

读取并清空GNSS芯片所有缓存位置。使用callback异步回调。

从API version 8开始支持。

从API version 9开始废弃，建议使用[geoLocationManager.flushCachedGnssLocations](@ohos.geoLocationManager (位置服务).md#ZH-CN_TOPIC_0000002497606102__geolocationmanagerflushcachedgnsslocations)替代。

**需要权限**：ohos.permission.LOCATION

**系统能力**：SystemCapability.Location.Location.Gnss

**参数**：

参数名类型必填说明callbackAsyncCallback<boolean>是回调函数。返回true表示操作成功；返回false表示操作失败。

**示例**

```ets
import geolocation from '@ohos.geolocation';
geolocation.flushCachedGnssLocations((err, result) => {
    if (err) {
        console.info('flushCachedGnssLocations: err=' + JSON.stringify(err));
    }
    if (result) {
        console.info('flushCachedGnssLocations: result=' + JSON.stringify(result));
    }
});
```

#### geolocation.flushCachedGnssLocations(deprecated)

flushCachedGnssLocations(): Promise<boolean>

读取并清空GNSS芯片所有缓存位置。使用Promise异步回调。

从API version 8开始支持。

从API version 9开始废弃，建议使用[geoLocationManager.flushCachedGnssLocations](@ohos.geoLocationManager (位置服务).md#ZH-CN_TOPIC_0000002497606102__geolocationmanagerflushcachedgnsslocations-1)替代。

**需要权限**：ohos.permission.LOCATION

**系统能力**：SystemCapability.Location.Location.Gnss

**返回值**：

类型说明Promise<boolean>Promise对象，返回true表示操作成功；返回false表示操作失败。

**示例**

```ets
import geolocation from '@ohos.geolocation';
geolocation.flushCachedGnssLocations().then((result) => {
    console.info('promise, flushCachedGnssLocations: ' + JSON.stringify(result));
});
```

#### geolocation.sendCommand(deprecated)

sendCommand(command: LocationCommand, callback: AsyncCallback<boolean>): void

给位置服务子系统的各个部件发送扩展命令。使用callback异步回调。

从API version 8开始支持。

从API version 9开始废弃，建议使用[geoLocationManager.sendCommand](@ohos.geoLocationManager (位置服务).md#ZH-CN_TOPIC_0000002497606102__geolocationmanagersendcommand)替代。

**需要权限**：ohos.permission.LOCATION

**系统能力**：SystemCapability.Location.Location.Core

**参数**：

参数名类型必填说明command[LocationCommand](#ZH-CN_TOPIC_0000002497606104__locationcommanddeprecated)是指定目标场景，和将要发送的命令（字符串）。callbackAsyncCallback<boolean>是回调函数。返回true表示命令发送成功；返回false表示命令发送失败。

**示例**

```ets
import geolocation from '@ohos.geolocation';
let requestInfo:geolocation.LocationCommand = {'scenario': 0x301, 'command': "command_1"};
geolocation.sendCommand(requestInfo, (err, result) => {
    if (err) {
        console.info('sendCommand: err=' + JSON.stringify(err));
    }
    if (result) {
        console.info('sendCommand: result=' + JSON.stringify(result));
    }
});
```

#### geolocation.sendCommand(deprecated)

sendCommand(command: LocationCommand): Promise<boolean>

给位置服务子系统的各个部件发送扩展命令。使用Promise异步回调。

从API version 8开始支持。

从API version 9开始废弃，建议使用[geoLocationManager.sendCommand](@ohos.geoLocationManager (位置服务).md#ZH-CN_TOPIC_0000002497606102__geolocationmanagersendcommand)替代。

**需要权限**：ohos.permission.LOCATION

**系统能力**：SystemCapability.Location.Location.Core

**参数**：

参数名类型必填说明command[LocationCommand](#ZH-CN_TOPIC_0000002497606104__locationcommanddeprecated)是指定目标场景，和将要发送的命令（字符串）。

**返回值**：

类型说明Promise<boolean>Promise对象，返回true表示命令发送成功；返回false表示命令发送失败。

**示例**

```ets
import geolocation from '@ohos.geolocation';
let requestInfo:geolocation.LocationCommand = {'scenario': 0x301, 'command': "command_1"};
geolocation.sendCommand(requestInfo).then((result) => {
    console.info('promise, sendCommand: ' + JSON.stringify(result));
});
```

#### ReverseGeoCodeRequest(deprecated)

逆地理编码请求参数。

从API version 9开始废弃，建议使用[geoLocationManager.ReverseGeoCodeRequest](@ohos.geoLocationManager (位置服务).md#ZH-CN_TOPIC_0000002497606102__reversegeocoderequest)替代。

**需要权限**：ohos.permission.LOCATION

**系统能力**：SystemCapability.Location.Location.Geocoder

名称类型只读可选说明localestring否是指定位置描述信息的语言，“zh”代表中文，“en”代表英文。latitudenumber否否表示纬度信息，正值表示北纬，负值表示南纬。取值范围为-90到90。longitudenumber否否表示经度信息，正值表示东经，负值表示西经。取值范围为-180到180。maxItemsnumber否是指定返回位置信息的最大个数。取值范围为大于等于0，推荐该值小于10。

#### GeoCodeRequest(deprecated)

地理编码请求参数。

从API version 9开始废弃，建议使用[geoLocationManager.GeoCodeRequest](@ohos.geoLocationManager (位置服务).md#ZH-CN_TOPIC_0000002497606102__geocoderequest)替代。

**需要权限**：ohos.permission.LOCATION

**系统能力**：SystemCapability.Location.Location.Geocoder

名称类型只读可选说明localestring否是表示位置描述信息的语言，“zh”代表中文，“en”代表英文。descriptionstring否否表示位置信息描述，如“上海市浦东新区xx路xx号”。maxItemsnumber否是表示返回位置信息的最大个数。取值范围为大于等于0，推荐该值小于10。minLatitudenumber否是表示最小纬度信息，与下面三个参数一起，表示一个经纬度范围。取值范围为-90到90。minLongitudenumber否是表示最小经度信息。取值范围为-180到180。maxLatitudenumber否是表示最大纬度信息。取值范围为-90到90。maxLongitudenumber否是表示最大经度信息。取值范围为-180到180。

#### GeoAddress(deprecated)

地理编码地址信息。

从API version 9开始废弃，建议使用[geoLocationManager.GeoAddress](@ohos.geoLocationManager (位置服务).md#ZH-CN_TOPIC_0000002497606102__geoaddress)替代。

**需要权限**：ohos.permission.LOCATION

**系统能力**：SystemCapability.Location.Location.Geocoder

名称类型只读可选说明latitude7+number否是表示纬度信息，正值表示北纬，负值表示南纬。取值范围为-90到90。longitude7+number否是表示经度信息，正值表示东经，负值表是西经。取值范围为-180到180。locale7+string否是表示位置描述信息的语言，“zh”代表中文，“en”代表英文。placeName7+string否是表示地区信息。countryCode7+string否是表示国家码信息。countryName7+string否是表示国家信息。administrativeArea7+string否是表示省份区域信息。subAdministrativeArea7+string否是表示子区域信息。locality7+string否是表示城市信息。subLocality7+string否是表示子城市信息。roadName7+string否是表示路名信息。subRoadName7+string否是表示子路名信息。premises7+string否是表示门牌号信息。postalCode7+string否是表示邮政编码信息。phoneNumber7+string否是表示联系方式信息。addressUrl7+string否是表示位置信息附件的网址信息。descriptions7+Array<string>否是表示附加的描述信息。descriptionsSize7+number否是表示附加的描述信息数量。取值范围为大于等于0，推荐该值小于10。

#### LocationRequest(deprecated)

位置信息请求参数。

从API version 9开始废弃，建议使用[geoLocationManager.LocationRequest](@ohos.geoLocationManager (位置服务).md#ZH-CN_TOPIC_0000002497606102__locationrequest)替代。

**需要权限**：ohos.permission.LOCATION

**系统能力**：SystemCapability.Location.Location.Core

名称类型只读可选说明priority[LocationRequestPriority](#ZH-CN_TOPIC_0000002497606104__locationrequestprioritydeprecated)否是表示优先级信息。取值范围见[LocationRequestPriority](#ZH-CN_TOPIC_0000002497606104__locationrequestprioritydeprecated)的定义。scenario[LocationRequestScenario](#ZH-CN_TOPIC_0000002497606104__locationrequestscenariodeprecated)否是表示场景信息。取值范围见[LocationRequestScenario](#ZH-CN_TOPIC_0000002497606104__locationrequestscenariodeprecated)的定义。timeIntervalnumber否是表示上报位置信息的时间间隔，单位是秒。取值范围为大于0。distanceIntervalnumber否是表示上报位置信息的距离间隔。单位是米，取值范围为大于0。maxAccuracynumber否是

表示精度信息，单位是米。

仅在精确位置功能场景（同时授予了ohos.permission.APPROXIMATELY_LOCATION和ohos.permission.LOCATION 权限）下有效，模糊位置功能生效场景（仅授予了ohos.permission.APPROXIMATELY_LOCATION 权限）下该字段无意义。

默认值为0，取值范围为大于等于0。

当scenario为NAVIGATION/TRAJECTORY_TRACKING/CAR_HAILING或者priority为ACCURACY时建议设置maxAccuracy为大于10的值。

当scenario为DAILY_LIFE_SERVICE/NO_POWER或者priority为LOW_POWER/FIRST_FIX时建议设置maxAccuracy为大于100的值。

#### CurrentLocationRequest(deprecated)

当前位置信息请求参数。

从API version 9开始废弃，建议使用[geoLocationManager.CurrentLocationRequest](@ohos.geoLocationManager (位置服务).md#ZH-CN_TOPIC_0000002497606102__currentlocationrequest)替代。

**需要权限**：ohos.permission.LOCATION

**系统能力**：SystemCapability.Location.Location.Core

名称类型只读可选说明priority[LocationRequestPriority](#ZH-CN_TOPIC_0000002497606104__locationrequestprioritydeprecated)否是表示优先级信息。取值范围见[LocationRequestPriority](#ZH-CN_TOPIC_0000002497606104__locationrequestprioritydeprecated)的定义。scenario[LocationRequestScenario](#ZH-CN_TOPIC_0000002497606104__locationrequestscenariodeprecated)否是表示场景信息。取值范围见[LocationRequestScenario](#ZH-CN_TOPIC_0000002497606104__locationrequestscenariodeprecated)的定义。maxAccuracynumber否是

表示精度信息，单位是米。

仅在精确位置功能场景（同时授予了ohos.permission.APPROXIMATELY_LOCATION和ohos.permission.LOCATION 权限）下有效，模糊位置功能生效场景（仅授予了ohos.permission.APPROXIMATELY_LOCATION 权限）下该字段无意义。

默认值为0，取值范围为大于等于0。

当scenario为NAVIGATION/TRAJECTORY_TRACKING/CAR_HAILING或者priority为ACCURACY时建议设置maxAccuracy为大于10的值。

当scenario为DAILY_LIFE_SERVICE/NO_POWER或者priority为LOW_POWER/FIRST_FIX时建议设置maxAccuracy为大于100的值。

timeoutMsnumber否是表示超时时间，单位是毫秒，最小为1000毫秒。取值范围为大于等于1000。

#### SatelliteStatusInfo(deprecated)

卫星状态信息。

从API version 8开始支持。

从API version 9开始废弃，建议使用[geoLocationManager.SatelliteStatusInfo](@ohos.geoLocationManager (位置服务).md#ZH-CN_TOPIC_0000002497606102__satellitestatusinfo)替代。

**需要权限**：ohos.permission.LOCATION

**系统能力**：SystemCapability.Location.Location.Gnss

名称类型只读可选说明satellitesNumbernumber否否表示卫星个数。取值范围为大于等于0。satelliteIdsArray<number>否否表示每个卫星的ID，数组类型。取值范围为大于等于0。carrierToNoiseDensitysArray<number>否否表示载波噪声功率谱密度比，即cn0。取值范围为大于0。altitudesArray<number>否否表示卫星高度角信息。单位是“度”，取值范围为-90到90。azimuthsArray<number>否否表示方位角。单位是“度”，取值范围为0到360。carrierFrequenciesArray<number>否否表示载波频率。单位是Hz，取值范围为大于等于0。

#### CachedGnssLocationsRequest(deprecated)

请求订阅GNSS缓存位置上报功能接口的配置参数。

从API version 8开始支持。

从API version 9开始废弃，建议使用[geoLocationManager.CachedGnssLocationsRequest](@ohos.geoLocationManager (位置服务).md#ZH-CN_TOPIC_0000002497606102__cachedgnsslocationsrequest)替代。

**需要权限**：ohos.permission.LOCATION

**系统能力**：SystemCapability.Location.Location.Gnss

名称类型只读可选说明reportingPeriodSecnumber否否表示GNSS缓存位置上报的周期，单位是毫秒。取值范围为大于0。wakeUpCacheQueueFullboolean否否

true表示GNSS芯片底层缓存队列满之后会主动唤醒AP芯片，并把缓存位置上报给应用。

false表示GNSS芯片底层缓存队列满之后不会主动唤醒AP芯片，会把缓存位置直接丢弃。

#### Geofence(deprecated)

GNSS围栏的配置参数。目前只支持圆形围栏。

从API version 8开始支持。

从API version 9开始废弃，建议使用[geoLocationManager.Geofence](@ohos.geoLocationManager (位置服务).md#ZH-CN_TOPIC_0000002497606102__geofence)替代。

**需要权限**：ohos.permission.LOCATION

**系统能力**：SystemCapability.Location.Location.Geofence

名称类型只读可选说明latitudenumber否否表示纬度。取值范围为-90到90。longitudenumber否否表示经度。取值范围为-180到180。radiusnumber否否表示圆形围栏的半径。单位是米，取值范围为大于0。expirationnumber否否围栏存活的时间，单位是毫秒。取值范围为大于0。

#### GeofenceRequest(deprecated)

请求添加GNSS围栏消息中携带的参数，包括定位场景和围栏信息。

从API version 8开始支持。

从API version 9开始废弃，建议使用[geoLocationManager.GeofenceRequest](@ohos.geoLocationManager (位置服务).md#ZH-CN_TOPIC_0000002497606102__geofencerequest)替代。

**需要权限**：ohos.permission.LOCATION

**系统能力**：SystemCapability.Location.Location.Geofence

名称类型只读可选说明priority[LocationRequestPriority](#ZH-CN_TOPIC_0000002497606104__locationrequestprioritydeprecated)否否表示位置信息优先级。scenario[LocationRequestScenario](#ZH-CN_TOPIC_0000002497606104__locationrequestscenariodeprecated)否否表示定位场景。geofence[Geofence](#ZH-CN_TOPIC_0000002497606104__geofencedeprecated)否否表示围栏信息。

#### LocationCommand(deprecated)

扩展命令参数。

从API version 8开始支持。

从API version 9开始废弃，建议使用[geoLocationManager.LocationCommand](@ohos.geoLocationManager (位置服务).md#ZH-CN_TOPIC_0000002497606102__locationcommand)替代。

**需要权限**：ohos.permission.LOCATION

**系统能力**：SystemCapability.Location.Location.Core

名称类型只读可选说明scenario[LocationRequestScenario](#ZH-CN_TOPIC_0000002497606104__locationrequestscenariodeprecated)否否表示定位场景。commandstring否否扩展命令字符串。

#### Location(deprecated)

位置信息。

从API version 9开始废弃，建议使用[geoLocationManager.Location](@ohos.geoLocationManager (位置服务).md#ZH-CN_TOPIC_0000002497606102__location)替代。

**需要权限**：ohos.permission.LOCATION

**系统能力**：SystemCapability.Location.Location.Core

名称类型只读可选说明latitude7+number否否表示纬度信息，正值表示北纬，负值表示南纬。取值范围为-90到90。longitude7+number否否表示经度信息，正值表示东经，负值表是西经。取值范围为-180到180。altitude7+number否否表示高度信息，单位米。accuracy7+number否否表示精度信息，单位米。speed7+number否否表示速度信息，单位米每秒。timeStamp7+number否否表示位置时间戳，UTC格式。direction7+number否否表示航向信息。单位是“度”，取值范围为0到360。timeSinceBoot7+number否否表示位置时间戳，开机时间格式。additions7+Array<string>否是附加信息。additionSize7+number否是附加信息数量。取值范围为大于等于0。

#### LocationPrivacyType(deprecated)

定位服务隐私协议类型。

从API version 8开始支持。

从API version 9开始废弃，替代接口geoLocationManager.LocationPrivacyType仅供系统应用使用。

**需要权限**：ohos.permission.LOCATION

**系统能力**：SystemCapability.Location.Location.Core

名称值说明OTHERS0其他场景。预留字段。STARTUP1开机向导场景下的隐私协议。在开机时弹出协议，提醒用户阅读并选择是否授权。CORE_LOCATION2开启网络定位时弹出的隐私协议。

#### LocationRequestPriority(deprecated)

位置请求中位置信息优先级类型。

从API version 9开始废弃，建议使用[geoLocationManager.LocationRequestPriority](@ohos.geoLocationManager (位置服务).md#ZH-CN_TOPIC_0000002497606102__locationrequestpriority)替代。

**需要权限**：ohos.permission.LOCATION

**系统能力**：SystemCapability.Location.Location.Core

名称值说明UNSET0x200表示未设置优先级，表示[LocationRequestPriority](#ZH-CN_TOPIC_0000002497606104__locationrequestprioritydeprecated)无效。ACCURACY0x201

表示精度优先。

定位精度优先策略主要以GNSS定位技术为主，在开阔场景下可以提供米级的定位精度，具体性能指标依赖用户设备的定位硬件能力，但在室内等强遮蔽定位场景下，无法提供准确的位置服务。

LOW_POWER0x202

表示低功耗优先。

低功耗定位优先策略主要使用基站定位和WLAN、蓝牙定位技术，也可以同时提供室内和户外场景下的位置服务，因为其依赖周边基站、可见WLAN、蓝牙设备的分布情况，定位结果的精度波动范围较大，如果对定位结果精度要求不高，或者使用场景多在有基站、可见WLAN、蓝牙设备高密度分布的情况下，推荐使用，可以有效节省设备功耗。

FIRST_FIX0x203

表示快速获取位置优先，如果应用希望快速拿到一个位置，可以将优先级设置为该字段。

快速定位优先策略会同时使用GNSS定位、基站定位和WLAN、蓝牙定位技术，以便室内和户外场景下，通过此策略都可以获得位置结果，当各种定位技术都有提供位置结果时，系统会选择其中精度较好的结果返回给应用。因为对各种定位技术同时使用，对设备的硬件资源消耗较大，功耗也较大。

#### LocationRequestScenario(deprecated)

位置请求中定位场景类型。

从API version 9开始废弃，建议使用[geoLocationManager.LocationRequestScenario](@ohos.geoLocationManager (位置服务).md#ZH-CN_TOPIC_0000002497606102__locationrequestscenario)替代。

**需要权限**：ohos.permission.LOCATION

**系统能力**：SystemCapability.Location.Location.Core

名称值说明UNSET0x300

表示未设置场景信息。

表示[LocationRequestScenario](#ZH-CN_TOPIC_0000002497606104__locationrequestscenariodeprecated)字段无效。

NAVIGATION0x301

表示导航场景。

适用于在户外定位设备实时位置的场景，如车载、步行导航。

在此场景下，为保证系统提供位置结果精度最优，主要使用GNSS定位技术提供定位服务。

此场景默认以最小1秒间隔上报定位结果。

TRAJECTORY_TRACKING0x302

表示运动轨迹记录场景。

适用于记录用户位置轨迹的场景，如运动类应用记录轨迹功能。主要使用GNSS定位技术提供定位服务。

此场景默认以最小1秒间隔上报定位结果。

CAR_HAILING0x303

表示打车场景。

适用于用户出行打车时定位当前位置的场景，如网约车类应用。

此场景默认以最小1秒间隔上报定位结果。

DAILY_LIFE_SERVICE0x304

表示日常服务使用场景。

适用于不需要定位用户精确位置的使用场景，如新闻资讯、网购、点餐类应用，做推荐、推送时定位用户大致位置即可。

此场景默认以最小1秒间隔上报定位结果。

NO_POWER0x305表示无功耗功场景，这种场景下不会主动触发定位，会在其他应用定位时，才给当前应用返回位置。

#### GeoLocationErrorCode(deprecated)

位置服务中的错误码信息。

从API version 9开始废弃，建议使用[位置服务子系统错误码](../../errors/位置服务错误码.md)替代。

**需要权限**：ohos.permission.LOCATION

**系统能力**：SystemCapability.Location.Location.Core

名称值说明INPUT_PARAMS_ERROR7+101表示输入参数错误。REVERSE_GEOCODE_ERROR7+102表示逆地理编码接口调用失败。GEOCODE_ERROR7+103表示地理编码接口调用失败。LOCATOR_ERROR7+104表示定位失败。LOCATION_SWITCH_ERROR7+105表示定位开关。LAST_KNOWN_LOCATION_ERROR7+106表示获取上次位置失败。LOCATION_REQUEST_TIMEOUT_ERROR7+107表示单次定位，没有在指定时间内返回位置。