# @ohos.resourceschedule.systemload (性能功耗热融合档位)

系统根据当前温度、负载以及是否处于高负载场景等信息决策出系统负载融合档位，并在档位变化时通知已注册的应用。

- 本模块首批接口从 API version 12 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { systemLoad } from '@kit.BasicServicesKit';
```

#### systemLoad.on('systemLoadChange')

on(type: 'systemLoadChange', callback: Callback<SystemLoadLevel>): void

注册系统负载回调，感知系统负载融合档位变化，使用callback异步回调。

**系统能力:** SystemCapability.ResourceSchedule.SystemLoad

**参数**：

参数名类型必填说明typestring是固定取值'systemLoadChange'，系统负载变化类型。callbackCallback<[SystemLoadLevel](#ZH-CN_TOPIC_0000002529285509__systemloadlevel)>是回调函数，返回本次注册系统负载时的系统负载融合档位。

**错误码**：

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible cause: 1. Callback parameter error; 2. Register a exist callback type; 3. Parameter verification failed.

**示例**：

```ets
import { systemLoad } from '@kit.BasicServicesKit';

function onSystemLoadChange(res: systemLoad.SystemLoadLevel) {
    console.info(`system load changed, current level ` + res);
}

try {
    systemLoad.on('systemLoadChange', onSystemLoadChange);
    console.info(`register systemload callback succeeded. `);
} catch (err) {
    console.error(`register systemload callback failed: ` + JSON.stringify(err));
}
```

#### systemLoad.off('systemLoadChange')

off(type: 'systemLoadChange', callback?: Callback<SystemLoadLevel>): void

取消注册系统负载回调，使用callback异步回调。

**系统能力:** SystemCapability.ResourceSchedule.SystemLoad

**参数**：

参数名类型必填说明typestring是固定取值'systemLoadChange'，系统负载变化类型。callbackCallback<[SystemLoadLevel](#ZH-CN_TOPIC_0000002529285509__systemloadlevel)>否回调函数，返回本次取消注册系统负载时的系统负载融合档位。

**错误码**：

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible cause: 1. Callback parameter error; 2. Unregister type has not register; 3. Parameter verification failed.

**示例**：

```ets
import { systemLoad } from '@kit.BasicServicesKit';

function onSystemLoadChange(res: systemLoad.SystemLoadLevel) {
    console.info(`system load changed, current level ` + res);
}

try {
    systemLoad.off('systemLoadChange', onSystemLoadChange);
    console.info(`unregister systemload callback succeeded:. `);
} catch (err) {
    console.error(`unregister systemload callback failed: ` + JSON.stringify(err));
}
```

#### systemLoad.getLevel

getLevel(): Promise<[SystemLoadLevel](#ZH-CN_TOPIC_0000002529285509__systemloadlevel)>

获取系统负载融合档位，使用promise异步回调。

**系统能力:** SystemCapability.ResourceSchedule.SystemLoad

**返回值**：

类型说明Promise<[SystemLoadLevel](#ZH-CN_TOPIC_0000002529285509__systemloadlevel)>Promise对象，返回系统负载融合档位。

**示例**：

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { systemLoad } from '@kit.BasicServicesKit';

systemLoad.getLevel().then((res: systemLoad.SystemLoadLevel) => {
    console.info(`getLevel promise succeeded. result: ` + JSON.stringify(res));
}).catch((err: BusinessError) => {
    console.error(`getLevel promise failed. code is ${err.code} message is ${err.message}`);
})
```

#### SystemLoadLevel

系统负载融合档位。

**系统能力:** SystemCapability.ResourceSchedule.SystemLoad

名称值说明LOW0设备当前温度、负载比较低，无高负载场景。NORMAL1设备温度、负载正常，但邻近中等状态，无感知业务应降低规格和负载。MEDIUM2设备温度、负载有一项或多项稍高，或者当前处于高负载场景，无感知业务应暂停或延迟运行。HIGH3设备当前发热明显或负载比较高，或处于负载温度中等但处于高负载场景，无感知业务应停止，非关键业务应降低规格及负载。OVERHEATED4设备发热严重或者负载较重，无感知业务与非关键业务应停止，前台关键业务应降低规格及负载。WARNING5设备过热或负载过重，或者温度较高但处于高负载场景，即将进入紧急状态，整机资源供给大幅降低，停止所有非关键，前台关键业务应降低至最低规格。EMERGENCY6设备已经进入过热状态或负载极高紧急状态，或接近紧急状态但处于高负载场景，整机资源供给降至最低，设备功能受限，仅保留基础功能可用。ESCAPE7设备即将进入热逃生状态或当前负载已经不堪重负，或已经处于紧急状态且高负载状态，所有业务将被强制停止，业务需做好逃生措施，例如保存重要数据等。