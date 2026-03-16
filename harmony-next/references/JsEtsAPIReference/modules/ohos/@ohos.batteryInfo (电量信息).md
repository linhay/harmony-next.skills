# @ohos.batteryInfo (电量信息)

该模块主要提供电池状态和充放电状态的查询接口。

本模块首批接口从API version 6开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import {batteryInfo} from '@kit.BasicServicesKit';
```

#### 常量

描述电池信息。

**系统能力**：SystemCapability.PowerManager.BatteryManager.Core

名称类型只读说明batterySOCnumber是

表示当前设备剩余电池电量百分比。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

chargingStatus[BatteryChargeState](#ZH-CN_TOPIC_0000002497605502__batterychargestate)是

表示当前设备电池的充电状态。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

healthStatus[BatteryHealthState](#ZH-CN_TOPIC_0000002497605502__batteryhealthstate)是表示当前设备电池的健康状态。pluggedType[BatteryPluggedType](#ZH-CN_TOPIC_0000002497605502__batterypluggedtype)是表示当前设备连接的充电器类型。voltagenumber是表示当前设备电池的电压，单位微伏。technologystring是表示当前设备电池的技术型号。batteryTemperaturenumber是表示当前设备电池的温度，单位0.1摄氏度。isBatteryPresent7+boolean是表示当前设备是否支持电池或者电池是否在位。true表示支持电池或电池在位，false表示不支持电池或电池不在位，默认为false。batteryCapacityLevel9+[BatteryCapacityLevel](#ZH-CN_TOPIC_0000002497605502__batterycapacitylevel9)是表示当前设备电池电量的等级。nowCurrent12+number是表示当前设备电池的电流，单位毫安。

**示例**：

```ets
import {batteryInfo} from '@kit.BasicServicesKit';

let batterySOCInfo: number = batteryInfo.batterySOC;
console.info("The batterySOCInfo is: " + batterySOCInfo);

let chargingStatusInfo = batteryInfo.chargingStatus;
console.info("The chargingStatusInfo is: " + chargingStatusInfo);

let healthStatusInfo = batteryInfo.healthStatus;
console.info("The healthStatusInfo is: " + healthStatusInfo);

let pluggedTypeInfo = batteryInfo.pluggedType;
console.info("The pluggedTypeInfo is: " + pluggedTypeInfo);

let voltageInfo: number = batteryInfo.voltage;
console.info("The voltageInfo is: " + voltageInfo);

let technologyInfo: string = batteryInfo.technology;
console.info("The technologyInfo is: " + technologyInfo);

let batteryTemperatureInfo: number = batteryInfo.batteryTemperature;
console.info("The batteryTemperatureInfo is: " + batteryTemperatureInfo);

let isBatteryPresentInfo: boolean = batteryInfo.isBatteryPresent;
console.info("The isBatteryPresentInfo is: " + isBatteryPresentInfo);

let batteryCapacityLevelInfo = batteryInfo.batteryCapacityLevel;
console.info("The batteryCapacityLevelInfo is: " + batteryCapacityLevelInfo);

let nowCurrentInfo: number = batteryInfo.nowCurrent;
console.info("The nowCurrentInfo is: " + nowCurrentInfo);
```

#### BatteryPluggedType

表示连接的充电器类型的枚举。

**系统能力**：SystemCapability.PowerManager.BatteryManager.Core

名称值说明NONE0表示未获取到连接充电器类型。AC1表示连接的充电器类型为交流充电器。USB2表示连接的充电器类型为USB。WIRELESS3表示连接的充电器类型为无线充电器。

#### BatteryChargeState

表示电池充电状态的枚举。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.PowerManager.BatteryManager.Core

名称值说明NONE0表示电池充电状态未知。ENABLE1表示电池充电状态为使能状态。DISABLE2表示电池充电状态为停止状态。FULL3表示电池充电状态为已充满状态。

#### BatteryHealthState

表示电池健康状态的枚举。

**系统能力**：SystemCapability.PowerManager.BatteryManager.Core

名称值说明UNKNOWN0表示电池健康状态未知。GOOD1表示电池健康状态为正常。OVERHEAT2表示电池健康状态为过热。OVERVOLTAGE3表示电池健康状态为过压。COLD4表示电池健康状态为低温。DEAD5表示电池健康状态为僵死状态。

#### BatteryCapacityLevel9+

表示电池电量等级的枚举。

**系统能力**：SystemCapability.PowerManager.BatteryManager.Core

名称值说明LEVEL_FULL1表示电池电量等级为满电量。LEVEL_HIGH2表示电池电量等级为高电量。LEVEL_NORMAL3表示电池电量等级为正常电量。LEVEL_LOW4表示电池电量等级为低电量。LEVEL_WARNING5表示电池电量等级为告警电量。LEVEL_CRITICAL6表示电池电量等级为极低电量。LEVEL_SHUTDOWN7表示电池电量等级为关机电量。

#### CommonEventBatteryChangedKey9+

表示COMMON_EVENT_BATTERY_CHANGED通用事件附加信息的查询键。

**系统能力**：SystemCapability.PowerManager.BatteryManager.Core

名称值说明EXTRA_SOC"soc"表示剩余电池电量百分比的查询键。EXTRA_CHARGE_STATE"chargeState"表示当前设备电池充电状态的查询键。EXTRA_HEALTH_STATE"healthState"表示当前设备电池健康状态的查询键。EXTRA_PLUGGED_TYPE"pluggedType"表示当前设备连接的充电器类型的查询键。EXTRA_VOLTAGE"voltage"表示当前设备电池电压的查询键。EXTRA_TECHNOLOGY"technology"表示当前设备电池技术型号的查询键。EXTRA_TEMPERATURE"temperature"表示当前设备电池温度的查询键。EXTRA_PRESENT"present"表示当前设备是否支持电池或者电池是否在位的查询键。EXTRA_CAPACITY_LEVEL"capacityLevel"表示当前设备电池电量等级的查询键。