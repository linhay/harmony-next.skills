# @ohos.wifiext (WLAN扩展接口)

该模块主要提供WLAN扩展接口，供非通用类型产品使用。

本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

该文档中的接口只供非通用类型产品使用，如路由器等，对于常规类型产品，不应该使用这些接口。

从API Version 9开始，该接口不再维护，推荐使用[@ohos.wifiManagerExt（WLAN扩展接口）](@ohos.wifiManagerExt (WLAN扩展接口).md)等相关接口。

#### 导入模块

```ets
import wifiext from '@ohos.wifiext';
```

#### wifiext.enableHotspot

enableHotspot(): boolean;

使能WLAN热点。

**需要权限：** ohos.permission.MANAGE_WIFI_HOTSPOT_EXT

**系统能力：** SystemCapability.Communication.WiFi.AP.Extension

**返回值：**

**类型****说明**boolean操作结果， true: 成功， false: 失败。

#### wifiext.disableHotspot

disableHotspot(): boolean;

去使能WLAN热点。

**需要权限：** ohos.permission.MANAGE_WIFI_HOTSPOT_EXT

**系统能力：** SystemCapability.Communication.WiFi.AP.Extension

**返回值：**

**类型****说明**boolean操作结果， true: 成功， false: 失败。

#### wifiext.getSupportedPowerModel

getSupportedPowerModel(): Promise<Array<PowerModel>>

获取支持的功率模式。使用Promise异步回调。

**需要权限：** ohos.permission.GET_WIFI_INFO

**系统能力：** SystemCapability.Communication.WiFi.AP.Extension

**返回值：**

类型说明Promise<Array<[PowerModel](#ZH-CN_TOPIC_0000002529285427__powermodel)>>Promise对象。表示功率模式。

#### PowerModel

表示功率模式的枚举。

**系统能力：** SystemCapability.Communication.WiFi.AP.Extension

名称值说明SLEEPING0睡眠模式。GENERAL1常规模式。THROUGH_WALL2穿墙模式。

#### wifiext.getSupportedPowerModel

getSupportedPowerModel(callback: AsyncCallback<Array<PowerModel>>): void

获取支持的功率模式。使用callback异步回调。

**需要权限：** ohos.permission.GET_WIFI_INFO

**系统能力：** SystemCapability.Communication.WiFi.AP.Extension

**参数：**

参数名类型必填说明callbackAsyncCallback<Array<[PowerModel](#ZH-CN_TOPIC_0000002529285427__powermodel)>>是回调函数。当操作成功时，err为0，data表示支持的功率模式。如果err为非0，表示处理出现错误。

#### wifiext.getPowerModel

getPowerModel(): Promise<PowerModel>

获取功率模式，使用Promise异步回调。

**需要权限：** ohos.permission.GET_WIFI_INFO

**系统能力：** SystemCapability.Communication.WiFi.AP.Extension

**返回值：**

类型说明Promise<[PowerModel](#ZH-CN_TOPIC_0000002529285427__powermodel)>Promise对象。表示功率模式。

#### wifiext.getPowerModel

getPowerModel(callback: AsyncCallback<PowerModel>): void

获取功率模式。使用callback异步回调。

**需要权限：** ohos.permission.GET_WIFI_INFO

**系统能力：** SystemCapability.Communication.WiFi.AP.Extension

**参数：**

参数名类型必填说明callbackAsyncCallback<[PowerModel](#ZH-CN_TOPIC_0000002529285427__powermodel)>是回调函数。当操作成功时，err为0，data表示功率模式。如果err为非0，表示处理出现错误。

#### wifiext.setPowerModel

setPowerModel(model: PowerModel) : boolean;

 设置功率模式。

**需要权限：** ohos.permission.MANAGE_WIFI_HOTSPOT_EXT

**系统能力：** SystemCapability.Communication.WiFi.AP.Extension

**参数：**

参数名类型必填说明model[PowerModel](#ZH-CN_TOPIC_0000002529285427__powermodel)是功率模式。

**返回值：**

**类型****说明**boolean操作结果， true: 成功， false: 失败。