# ohbattery_info.h

#### 概述

声明电池API以获取当前电池容量和电源类型的信息，定义电池相应常见事件。

**引用文件：** <BasicServicesKit/ohbattery_info.h>

**库：** libohbattery_info.so

**系统能力：** SystemCapability.PowerManager.BatteryManager.Core

**起始版本：** 13

**相关模块：**[OH_BatteryInfo](../../topics/misc/OH_BatteryInfo.md)

#### 汇总

#### 枚举

名称typedef关键字描述[BatteryInfo_BatteryPluggedType](#ZH-CN_TOPIC_0000002529285521__batteryinfo_batterypluggedtype)BatteryInfo_BatteryPluggedType定义插入类型。

#### 函数

名称描述[int32_t OH_BatteryInfo_GetCapacity()](#ZH-CN_TOPIC_0000002529285521__oh_batteryinfo_getcapacity)返回当前电池容量。[BatteryInfo_BatteryPluggedType OH_BatteryInfo_GetPluggedType()](#ZH-CN_TOPIC_0000002529285521__oh_batteryinfo_getpluggedtype)返回当前插入的类型。

#### 变量

名称描述static const char * COMMON_EVENT_KEY_CAPACITY = "soc"

标识电池容量变化后发送的常见事件。

**起始版本：** 13

**系统能力：** SystemCapability.PowerManager.BatteryManager.Core

static const char * COMMON_EVENT_KEY_CHARGE_STATE = "chargeState"

标识充电状态更改后发送的常见事件。

**起始版本：** 13

static const char * COMMON_EVENT_KEY_PLUGGED_TYPE = "pluggedType"

标识插入类型更改后发送的常见事件。

**起始版本：** 13

#### 枚举类型说明

#### BatteryInfo_BatteryPluggedType

```ets
enum BatteryInfo_BatteryPluggedType
```

**描述**

定义插入类型。

**起始版本：** 13

枚举项描述PLUGGED_TYPE_NONE = 0电源已拔下。PLUGGED_TYPE_AC = 1电源是交流充电。PLUGGED_TYPE_USB = 2电源是USB DC充电。PLUGGED_TYPE_WIRELESS = 3电源为无线充电。PLUGGED_TYPE_BUTT = 4预留枚举

#### 函数说明

#### OH_BatteryInfo_GetCapacity()

```ets
int32_t OH_BatteryInfo_GetCapacity()
```

**描述**

返回当前电池容量。

**系统能力：** SystemCapability.PowerManager.BatteryManager.Core

**起始版本：** 13

**返回：**

类型说明int32_t返回介于0和100之间的数字。

#### OH_BatteryInfo_GetPluggedType()

```ets
BatteryInfo_BatteryPluggedType OH_BatteryInfo_GetPluggedType()
```

**描述**

返回当前插入的类型。

**系统能力：** SystemCapability.PowerManager.BatteryManager.Core

**起始版本：** 13

**返回：**

类型说明[BatteryInfo_BatteryPluggedType](#ZH-CN_TOPIC_0000002529285521__batteryinfo_batterypluggedtype)

[BatteryInfo_BatteryPluggedType](#ZH-CN_TOPIC_0000002529285521__batteryinfo_batterypluggedtype) 如果电源被拔下。

[PLUGGED_TYPE_AC](ohbattery_info.h.md#ZH-CN_TOPIC_0000002529285521__batteryinfo_batterypluggedtype) 如果电源是AC充电。

[PLUGGED_TYPE_USB](ohbattery_info.h.md#ZH-CN_TOPIC_0000002529285521__batteryinfo_batterypluggedtype) 如果电源是USB DC充电。

[PLUGGED_TYPE_WIRELESS](ohbattery_info.h.md#ZH-CN_TOPIC_0000002529285521__batteryinfo_batterypluggedtype) 如果电源是无线充电。

[PLUGGED_TYPE_BUTT](ohbattery_info.h.md#ZH-CN_TOPIC_0000002529285521__batteryinfo_batterypluggedtype) 如果类型未知。