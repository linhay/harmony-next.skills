# @ohos.thermal (热管理)

该模块提供热管理相关的接口，包括热档位查询及注册回调等功能。

本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import {thermal} from '@kit.BasicServicesKit';
```

#### thermal.registerThermalLevelCallback9+

registerThermalLevelCallback(callback: Callback<ThermalLevel>): void

**方法介绍：** 订阅热档位变化时的回调提醒。使用callback异步回调。

**系统能力：** SystemCapability.PowerManager.ThermalManager

**参数：**

参数名类型必填说明callbackCallback<[ThermalLevel](#ZH-CN_TOPIC_0000002497605504__thermallevel)>是回调函数，返回变化后的热档位；该参数是一个函数类型。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Incorrect parameter types.

**示例：**

```ets
try {
    thermal.registerThermalLevelCallback((level: thermal.ThermalLevel) => {
        console.info('thermal level is: ' + level);
    });
    console.info('register thermal level callback success.');
} catch(err) {
    console.error('register thermal level callback failed, err: ' + err);
}
```

#### thermal.unregisterThermalLevelCallback9+

unregisterThermalLevelCallback(callback?: Callback<void>): void

**方法介绍：** 取消订阅热档位变化时的回调提醒。使用callback异步回调。

**系统能力：** SystemCapability.PowerManager.ThermalManager

**参数：**

参数名类型必填说明callbackCallback<void>否可选参数，回调函数，无返回值。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Incorrect parameter types.

**示例：**

```ets
try {
    thermal.unregisterThermalLevelCallback(() => {
        console.info('unsubscribe thermal level success.');
    });
    console.info('unregister thermal level callback success.');
} catch(err) {
    console.error('unregister thermal level callback failed, err: ' + err);
}
```

#### thermal.getLevel9+

getLevel(): ThermalLevel

**方法介绍：** 获取当前热档位信息。

**系统能力：** SystemCapability.PowerManager.ThermalManager

**返回值：**

类型说明[ThermalLevel](#ZH-CN_TOPIC_0000002497605504__thermallevel)热档位信息。

**示例：**

```ets
let level = thermal.getLevel();
console.info('thermal level is: ' + level);
```

#### thermal.subscribeThermalLevel(deprecated)

subscribeThermalLevel(callback: AsyncCallback<ThermalLevel>): void

从API version 8开始支持，从API version 9开始不再维护，建议使用[thermal.registerThermalLevelCallback](#ZH-CN_TOPIC_0000002497605504__thermalregisterthermallevelcallback9)替代。

**方法介绍：** 订阅热档位变化时的回调提醒。使用callback异步回调。

**系统能力：** SystemCapability.PowerManager.ThermalManager

**参数：**

参数名类型必填说明callbackAsyncCallback<[ThermalLevel](#ZH-CN_TOPIC_0000002497605504__thermallevel)>是回调函数。AsyncCallback只返回一个参数，为热档位信息。

**示例：**

```ets
thermal.subscribeThermalLevel((err: Error, level: thermal.ThermalLevel) => {
    console.info('thermal level is: ' + level);
});
```

#### thermal.unsubscribeThermalLevel(deprecated)

unsubscribeThermalLevel(callback?: AsyncCallback<void>): void

从API version 8开始支持，从API version 9开始不再维护，建议使用[thermal.unregisterThermalLevelCallback](#ZH-CN_TOPIC_0000002497605504__thermalunregisterthermallevelcallback9)替代。

**方法介绍：** 取消订阅热档位变化时的回调提醒。使用callback异步回调。

**系统能力：** SystemCapability.PowerManager.ThermalManager

**参数：**

参数名类型必填说明callbackAsyncCallback<void>否回调函数，无返回值。不填该参数则取消所有回调。

**示例：**

```ets
thermal.unsubscribeThermalLevel(() => {
    console.info('unsubscribe thermal level success.');
});
```

#### thermal.getThermalLevel(deprecated)

getThermalLevel(): ThermalLevel

从API version 8开始支持，从API version 9开始不再维护，建议使用[thermal.getLevel](#ZH-CN_TOPIC_0000002497605504__thermalgetlevel9)替代。

**方法介绍：** 获取当前热档位信息。

**系统能力：** SystemCapability.PowerManager.ThermalManager

**返回值：**

类型说明[ThermalLevel](#ZH-CN_TOPIC_0000002497605504__thermallevel)热档位信息。

**示例：**

```ets
let level = thermal.getThermalLevel();
console.info('thermal level is: ' + level);
```

#### ThermalLevel

热档位信息。

**系统能力：** SystemCapability.PowerManager.ThermalManager

名称值说明COOL0表明设备处于清凉状态，业务执行不受热控的限制。NORMAL1表明设备温度正常，但邻近温热状态，无感知业务应降低规格和负载。WARM2表明设备进入温热状态，无感知业务应暂停或延迟运行。HOT3表明设备发热明显，无感知业务应停止，非关键业务应降低规格及负载。OVERHEATED4表明设备发热严重，无感知业务与非关键业务应停止，前台关键业务应降低规格及负载。WARNING5表明设备过热即将进入紧急状态，整机资源供给大幅降低，停止所有非关键业务，前台关键业务应降低至最低规格。EMERGENCY6表明设备已经进入过热紧急状态，整机资源供给降至最低，设备功能受限，仅保留基础功能可用。ESCAPE11+7

表明设备即将进入热逃生状态，所有业务将被强制停止，业务需做好逃生措施，例如保存重要数据等。

**说明**: 从API version 11开始支持。