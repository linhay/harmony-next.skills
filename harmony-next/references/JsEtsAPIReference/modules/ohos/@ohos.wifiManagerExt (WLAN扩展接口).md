# @ohos.wifiManagerExt (WLAN扩展接口)

该模块主要提供WLAN扩展接口，供非通用类型产品使用。

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

该文档中的接口只供非通用类型产品使用，如路由器等，对于常规类型产品，不应该使用这些接口。

#### 导入模块

```ets
import { wifiManagerExt } from '@kit.ConnectivityKit';
```

#### wifiManagerExt.enableHotspot(deprecated)

enableHotspot(): void

使能WLAN热点。

从API version 9开始支持，从API version 10开始废弃。

**需要权限：** ohos.permission.MANAGE_WIFI_HOTSPOT_EXT

**系统能力：** SystemCapability.Communication.WiFi.AP.Extension

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码]([WIFI错误码](../../errors/WIFI错误码.md).md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2701000 | Operation failed. |

**示例：**

```ets
  import { wifiManagerExt } from '@kit.ConnectivityKit';

  try {
      wifiManagerExt.enableHotspot();
  }catch(error){
      console.error("failed: " + JSON.stringify(error));
  }
```

#### wifiManagerExt.disableHotspot(deprecated)

disableHotspot(): void

去使能WLAN热点。

从API version 9开始支持，从API version 10开始废弃。

**需要权限：** ohos.permission.MANAGE_WIFI_HOTSPOT_EXT

**系统能力：** SystemCapability.Communication.WiFi.AP.Extension

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](WIFI错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2701000 | Operation failed. |

**示例：**

```ets
  import { wifiManagerExt } from '@kit.ConnectivityKit';

  try {
      wifiManagerExt.disableHotspot();
  }catch(error){
      console.error("failed: " + JSON.stringify(error));
  }
```

#### wifiManagerExt.getSupportedPowerMode

getSupportedPowerMode(): Promise<Array<PowerMode>>

获取支持的功率模式。使用Promise异步回调。

**需要权限：** ohos.permission.GET_WIFI_INFO

**系统能力：** SystemCapability.Communication.WiFi.AP.Extension

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<PowerMode>> | Promise对象。表示功率模式。 |

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](WIFI错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2701000 | Operation failed. |

#### PowerMode

表示功率模式的枚举。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SLEEPING | 0 | 睡眠模式。 |
| GENERAL | 1 | 常规模式。 |
| THROUGH_WALL | 2 | 穿墙模式。 |

#### wifiManagerExt.getSupportedPowerMode

getSupportedPowerMode(callback: AsyncCallback<Array<PowerMode>>): void

获取支持的功率模式。使用callback异步回调。

**需要权限：** ohos.permission.GET_WIFI_INFO

**系统能力：** SystemCapability.Communication.WiFi.AP.Extension

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<Array<PowerMode>> | 是 | 回调函数。当操作成功时，err为0，data表示支持的功率模式。如果err为非0，表示处理出现错误。 |

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](WIFI错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2701000 | Operation failed. |

**示例：**

```ets
import { wifiManagerExt } from '@kit.ConnectivityKit';

wifiManagerExt.getSupportedPowerMode((err, data: wifiManagerExt.PowerMode[]) => {
    if (err) {
        console.error("get supported power mode info error: ", err);
        return;
    }
    console.info("get supported power mode info: " + JSON.stringify(data));
});
```

#### wifiManagerExt.getPowerMode

getPowerMode(): Promise<PowerMode>

获取功率模式，使用Promise异步回调。

从API version 9开始支持，从API version 10开始废弃。

**需要权限：** ohos.permission.GET_WIFI_INFO

**系统能力：** SystemCapability.Communication.WiFi.AP.Extension

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<PowerMode> | Promise对象。表示功率模式。 |

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](WIFI错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2701000 | Operation failed. |

**示例：**

```ets
  import { wifiManagerExt } from '@kit.ConnectivityKit';

  try {
      let model = wifiManagerExt.getPowerMode();
      console.info("model info:" + model);
  }catch(error){
      console.error("failed: " + JSON.stringify(error));
  }
```

#### wifiManagerExt.getPowerMode

getPowerMode(callback: AsyncCallback<PowerMode>): void

获取功率模式。使用callback异步回调。

**需要权限：** ohos.permission.GET_WIFI_INFO

**系统能力：** SystemCapability.Communication.WiFi.AP.Extension

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<PowerMode> | 是 | 回调函数。当操作成功时，err为0，data表示功率模式。如果err为非0，表示处理出现错误。 |

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](WIFI错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2701000 | Operation failed. |

**示例：**

```ets
  import { wifiManagerExt } from '@kit.ConnectivityKit';

  wifiManagerExt.getPowerMode((err, data:wifiManagerExt.PowerMode) => {
      if (err) {
          console.error("Failed to get linked information");
          return;
      }
      console.info("get power mode info: " + JSON.stringify(data));
  });

  wifiManagerExt.getPowerMode().then(data => {
      console.info("get power mode info: " + JSON.stringify(data));
  }).catch((error:number) => {
      console.error("get power mode error");
  });
```

#### wifiManagerExt.setPowerMode(deprecated)

setPowerMode(mode: PowerMode) : void

 设置功率模式。

从API version 9开始支持，从API version 10开始废弃。

**需要权限：** ohos.permission.MANAGE_WIFI_HOTSPOT_EXT

**系统能力：** SystemCapability.Communication.WiFi.AP.Extension

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | PowerMode | 是 | 功率模式。 |

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](WIFI错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2701000 | Operation failed. |

**示例：**

```ets
  import { wifiManagerExt } from '@kit.ConnectivityKit';

  try {
      let model = 0;
      wifiManagerExt.setPowerMode(model);
  }catch(error){
      console.error("failed: " + JSON.stringify(error));
  }
```