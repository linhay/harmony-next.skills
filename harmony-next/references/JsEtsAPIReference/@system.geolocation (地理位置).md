# @system.geolocation (地理位置)

本模块仅提供GNSS定位、网络定位等基本功能。

- 本模块首批接口从API version 3开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
- 从API Version 9开始，该接口不再维护，推荐使用新接口[geoLocationManager](@ohos.geoLocationManager (位置服务).md)。

#### 导入模块

```ets
import geolocation from '@system.geolocation';
```

#### 权限列表

ohos.permission.LOCATION

#### geolocation.getLocation(deprecated)

getLocation(options?: GetLocationOption): void

获取设备的地理位置。

从API version 9开始废弃，建议使用[geoLocationManager.getCurrentLocation](@ohos.geoLocationManager (位置服务).md#ZH-CN_TOPIC_0000002497606102__geolocationmanagergetcurrentlocation)替代。

**需要权限**：ohos.permission.LOCATION

**系统能力：** SystemCapability.Location.Location.Lite

**参数：**

参数名类型必填说明options[GetLocationOption](#ZH-CN_TOPIC_0000002497446124__getlocationoptiondeprecated)否单次定位请求的配置参数。

**示例：**

```ets
export default {
  getLocation() {
    geolocation.getLocation({
      success: function(data) {
        console.info('success get location data. latitude:' + data.latitude);
      },
      fail: function(data, code) {
        console.info('fail to get location. code:' + code + ', data:' + data);
      }
    });
  }
}
```

#### geolocation.getLocationType(deprecated)

getLocationType(options?: GetLocationTypeOption): void

获取当前设备支持的定位类型。

从API version 9开始废弃。位置服务子系统仅支持gnss和network两种定位类型，后续不再提供接口查询支持的定位类型。

**系统能力：** SystemCapability.Location.Location.Lite

**参数：**

参数名类型必填说明options[GetLocationTypeOption](#ZH-CN_TOPIC_0000002497446124__getlocationtypeoptiondeprecated)否回调函数，用于接收查询结果，或者接收查询失败的结果。

**示例：**

```ets
export default {
  getLocationType() {
    geolocation.getLocationType({
      success: function(data) {
        console.info('success get location type:' + data.types[0]);
      },
      fail: function(data, code) {
        console.info('fail to get location. code:' + code + ', data:' + data);
       },
     });
  },
}
```

#### geolocation.subscribe(deprecated)

subscribe(options: SubscribeLocationOption): void

订阅设备的地理位置信息。多次调用的话，只有最后一次的调用生效。

从API version 9开始废弃，建议使用[geoLocationManager.on('locationChange')](@ohos.geoLocationManager (位置服务).md#ZH-CN_TOPIC_0000002497606102__geolocationmanageronlocationchange)替代。

**需要权限**：ohos.permission.LOCATION

**系统能力：** SystemCapability.Location.Location.Lite

**参数：**

参数名类型必填说明options[SubscribeLocationOption](#ZH-CN_TOPIC_0000002497446124__subscribelocationoptiondeprecated)是持续定位的配置参数。

**示例：**

```ets
export default {
  subscribe() {
    geolocation.subscribe({
      success: function(data) {
        console.info('get location. latitude:' + data.latitude);
      },
      fail: function(data, code) {
        console.info('fail to get location. code:' + code + ', data:' + data);
      },
    });
  },
}
```

#### geolocation.unsubscribe(deprecated)

unsubscribe(): void

取消订阅设备的地理位置信息。

从API version 9开始废弃，建议使用[geoLocationManager.off('locationChange')](@ohos.geoLocationManager (位置服务).md#ZH-CN_TOPIC_0000002497606102__geolocationmanagerofflocationchange)替代。

**需要权限**：ohos.permission.LOCATION

**系统能力：** SystemCapability.Location.Location.Lite

**示例：**

```ets
export default {
  unsubscribe() {
    geolocation.unsubscribe();
  }
}
```

#### geolocation.getSupportedCoordTypes(deprecated)

getSupportedCoordTypes(): Array<string>

获取设备支持的坐标系类型。

从API version 9开始废弃。位置服务子系统仅支持WGS-84坐标系，后续不再提供接口查询支持的坐标系类型。

**系统能力：** SystemCapability.Location.Location.Lite

**返回值：**

类型非空说明Array<string>是表示坐标系类型，如[wgs84, gcj02]。

**示例：**

```ets
export default {
  getSupportedCoordTypes() {
    var types = geolocation.getSupportedCoordTypes();
  },
}
```

#### GetLocationOption(deprecated)

单次定位请求的配置参数。

从API version 9开始废弃，建议使用[geoLocationManager.CurrentLocationRequest](@ohos.geoLocationManager (位置服务).md#ZH-CN_TOPIC_0000002497606102__currentlocationrequest)替代。

**需要权限**：ohos.permission.LOCATION

**系统能力**：SystemCapability.Location.Location.Lite

名称类型必填说明timeoutnumber否

超时时间，单位为ms，默认值为30000。

设置超时，是为了防止出现权限被系统拒绝、定位信号弱或者定位设置不当，导致请求阻塞的情况。超时后会使用fail回调函数。

取值范围为32位正整数。如果设置值小于等于0，系统按默认值处理。

coordTypestring否坐标系的类型，可通过getSupportedCoordTypes获取可选值，缺省值为wgs84。success(data: [GeolocationResponse](#ZH-CN_TOPIC_0000002497446124__geolocationresponsedeprecated)) => void否接口调用成功的回调函数。fail(data: string, code: number) => void否接口调用失败的回调函数。data为错误信息，code为错误码。complete() => void否接口调用结束的回调函数。

fail返回错误代码：

错误码说明601获取定位权限失败，失败原因：用户拒绝。602权限未声明。800超时，失败原因：网络状况不佳或GNSS不可用。801系统位置开关未打开。802该次调用结果未返回前接口又被重新调用，该次调用失败返回错误码。

#### GeolocationResponse(deprecated)

位置信息，包含经度、纬度、定位精度等信息。

从API version 9开始废弃，建议使用[geoLocationManager.Location](@ohos.geoLocationManager (位置服务).md#ZH-CN_TOPIC_0000002497606102__location)替代。

**系统能力**：SystemCapability.Location.Location.Lite

名称类型只读可选说明longitudenumber否否设备位置信息：经度。latitudenumber否否设备位置信息：纬度。altitudenumber否否设备位置信息：海拔。accuracynumber否否设备位置信息：精确度。timenumber否否设备位置信息：时间。

#### GetLocationTypeOption(deprecated)

查询定位类型接口的入参，用于存放回调函数，在查询成功或者失败时接收查询结果。

从API version 9开始废弃。

**系统能力**：SystemCapability.Location.Location.Lite

名称类型必填说明success(data: [GetLocationTypeResponse](#ZH-CN_TOPIC_0000002497446124__getlocationtyperesponsedeprecated)) => void否接口调用成功的回调函数。fail(data: string, code: number) => void否接口调用失败的回调函数。complete() => void否接口调用结束的回调函数。

#### GetLocationTypeResponse(deprecated)

当前设备支持的定位类型列表

从API version 9开始废弃。

**系统能力**：SystemCapability.Location.Location.Lite

名称类型只读可选说明typesArray<string>否否可选的定位类型['gps', 'network']。

#### SubscribeLocationOption(deprecated)

持续定位请求的配置参数。

从API version 9开始废弃，建议使用[geoLocationManager.CurrentLocationRequest](@ohos.geoLocationManager (位置服务).md#ZH-CN_TOPIC_0000002497606102__currentlocationrequest)替代。

**需要权限**：ohos.permission.LOCATION

**系统能力**：SystemCapability.Location.Location.Lite

名称类型必填说明coordTypestring否坐标系的类型，可通过getSupportedCoordTypes获取可选值，默认值为wgs84。success(data: [GeolocationResponse](#ZH-CN_TOPIC_0000002497446124__geolocationresponsedeprecated)) => void是位置信息发生变化的回调函数。fail(data: string, code: number) => void否接口调用失败的回调函数。

fail返回错误代码：

错误码说明601获取定位权限失败，失败原因：用户拒绝。602权限未声明。801系统位置开关未打开。