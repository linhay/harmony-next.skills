# @ohos.power (系统电源管理)

该模块主要提供重启、关机、查询屏幕状态等接口。开发者可以使用该模块的接口获取设备的活动状态、电源模式、亮灭屏状态等。

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import {power} from '@kit.BasicServicesKit';
```

#### power.isActive9+

isActive(): boolean

检测当前设备是否处于活动状态。

- 有屏的设备亮屏时为活动状态，熄屏时为非活动状态。
- 无屏的设备非休眠时为活动状态，休眠时为非活动状态。

**系统能力：** SystemCapability.PowerManager.PowerManager.Core

**返回值：**

类型说明boolean活动状态返回true，非活动状态返回false。

**示例：**

```ets
let isActive = power.isActive();
console.info('power is active: ' + isActive);
```

#### power.rebootDevice(deprecated)

rebootDevice(reason: string): void

从API version 7开始支持，从API version 9开始不再维护，替代接口能力仅对系统应用开放。

重启设备。

**需要权限：** ohos.permission.REBOOT,该权限仅系统应用可申请。

**系统能力：** SystemCapability.PowerManager.PowerManager.Core

**参数：**

参数名类型必填说明reasonstring是重启原因。

**示例：**

```ets
power.rebootDevice('reboot_test');
```

#### power.getPowerMode9+

getPowerMode(): DevicePowerMode

获取当前设备的电源模式。

**系统能力：** SystemCapability.PowerManager.PowerManager.Core

**返回值：**

类型说明[DevicePowerMode](#ZH-CN_TOPIC_0000002529285495__devicepowermode9)电源模式。

**示例：**

```ets
let mode = power.getPowerMode();
console.info('power mode: ' + mode);
```

#### power.isStandby10+

isStandby(): boolean

检测当前设备是否进入待机低功耗续航模式。

**系统能力：** SystemCapability.PowerManager.PowerManager.Core

**返回值：**

类型说明boolean进入待机模式返回true，否则返回false。

**错误码：**

以下错误码的详细介绍请参见[系统电源管理错误码](系统电源管理错误码.md)。

错误码ID错误信息4900101Failed to connect to the service.

**示例：**

```ets
try {
    let isStandby = power.isStandby();
    console.info('device is in standby: ' + isStandby);
} catch(err) {
    console.error('check isStandby failed, err: ' + err);
}
```

#### power.isScreenOn(deprecated)

isScreenOn(callback: AsyncCallback<boolean>): void

从API version 7开始支持，从API version 9开始不再维护，建议使用[power.isActive](#ZH-CN_TOPIC_0000002529285495__powerisactive9)替代。

检测当前设备的亮灭屏状态。使用callback异步回调。

**系统能力：** SystemCapability.PowerManager.PowerManager.Core

**参数：**

参数名类型必填说明callbackAsyncCallback<boolean>是回调函数。当检测成功，err为undefined，data为获取到的亮灭屏状态，返回true表示亮屏，返回false表示灭屏；否则为错误对象。

**示例：**

```ets
power.isScreenOn((err: Error, data: boolean) => {
    if (typeof err === 'undefined') {
        console.info('screen on status is ' + data);
    } else {
        console.error('check screen status failed, err: ' + err);
    }
})
```

#### power.isScreenOn(deprecated)

isScreenOn(): Promise<boolean>

从API version 7开始支持，从API version 9开始不再维护，建议使用[power.isActive](#ZH-CN_TOPIC_0000002529285495__powerisactive9)替代。

检测当前设备的亮灭屏状态。使用Promise异步回调。

**系统能力：** SystemCapability.PowerManager.PowerManager.Core

**返回值：**

类型说明Promise<boolean>Promise对象。返回true表示亮屏；返回false表示灭屏。

**示例：**

```ets
power.isScreenOn()
.then((data: boolean) => {
    console.info('screen on status is ' + data);
})
.catch((err: Error) => {
    console.error('check screen status failed, err: ' + err);
})
```

#### DevicePowerMode9+

表示电源模式的枚举值。

**系统能力：** SystemCapability.PowerManager.PowerManager.Core

名称值说明MODE_NORMAL600表示标准模式，默认值。MODE_POWER_SAVE601表示省电模式。MODE_PERFORMANCE602表示性能模式。MODE_EXTREME_POWER_SAVE603表示超级省电模式。MODE_CUSTOM_POWER_SAVE20+650表示自定义省电模式。

#### PowerKeyFilteringStrategy21+

表示电源键过滤策略。

**系统能力：** SystemCapability.PowerManager.PowerManager.Core

名称值说明DISABLE_LONG_PRESS_FILTERING0表示不使能电源键过滤策略，默认值。LONG_PRESS_FILTERING_ONCE1表示仅过滤当前电源键长按事件，下一次不过滤。