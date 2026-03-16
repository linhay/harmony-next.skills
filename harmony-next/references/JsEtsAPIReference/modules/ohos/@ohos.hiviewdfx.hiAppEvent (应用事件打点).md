# @ohos.hiviewdfx.hiAppEvent (应用事件打点)

本模块提供应用打点和事件订阅能力，包括事件存储、事件订阅、事件清理、打点配置等功能。HiAppEvent将应用运行过程中触发的事件信息统一归纳到[AppEventInfo](#ZH-CN_TOPIC_0000002529285653__appeventinfo)中，并将事件分为系统事件和应用事件两类。

系统事件来源于系统服务，是系统预先定义的事件，这类事件信息中的事件参数对象params包含的字段已由各系统事件定义，具体字段含义在各系统事件指南的介绍中，例如[崩溃事件介绍](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-crash-events)。

应用事件来源于应用，是应用开发者自己定义的事件，这类事件信息支持自定义后通过[Write](#ZH-CN_TOPIC_0000002529285653__hiappeventwrite-1)打点接口进行配置设定，具体字段含义可结合开发者需求展开。

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { hiAppEvent } from '@kit.PerformanceAnalysisKit';
```

#### hiAppEvent.addWatcher

addWatcher(watcher: Watcher): AppEventPackageHolder

添加事件观察者。可通过事件观察者的回调函数监听事件。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**参数：**

参数名类型必填说明watcher[Watcher](#ZH-CN_TOPIC_0000002529285653__watcher)是事件观察者。

**返回值：**

类型说明[AppEventPackageHolder](#ZH-CN_TOPIC_0000002529285653__appeventpackageholder)订阅数据持有者。订阅失败时返回null。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[应用事件打点错误码](../../errors/应用事件打点错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.11102001Invalid watcher name. Possible causes: 1. Contain invalid characters; 2. Length is invalid.11102002Invalid filtering event domain. Possible causes: 1. Contain invalid characters; 2. Length is invalid.11102003Invalid row value. Possible caused by the row value is less than zero.11102004Invalid size value. Possible caused by the size value is less than zero.11102005Invalid timeout value. Possible caused by the timeout value is less than zero.

addWatcher接口涉及I/O操作。在对性能敏感的业务场景中，开发者应根据实际需要确定该接口是在主线程还是在子线程中调用。

如果选择在子线程中调用addWatcher，需要确保该子线程在整个接口使用周期内不会被销毁，以免影响接口的正常工作。

可参考[多线程并发概述](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/multi-thread-concurrency-overview)，以实现在子线程中调用接口。

订阅接口addWatcher传入的名称name是唯一的，相同的name，后一次调用会覆盖前一次的订阅。

**示例：**

根据添加的事件观察者类型，目前有如下三种使用方法：

方法一：设置回调条件triggerCondition，实现onTrigger()回调。当满足回调条件时，系统将自动触发回调。

```ets
import { hilog } from '@kit.PerformanceAnalysisKit';

hiAppEvent.addWatcher({
  name: "watcher1",
  // 订阅过滤条件，这里是订阅了系统事件领域的应用崩溃事件
  appEventFilters: [
    {
      domain: hiAppEvent.domain.OS,
      names: [hiAppEvent.event.APP_CRASH]
    }
  ],
  // 设置触发onTrigger回调的条件，这里是当满足事件总数量达到10个或事件总大小达到1000byte或事件发生超过30s时会触发回调
  triggerCondition: {
    row: 10,
    size: 1000,
    timeOut: 1
  },
  // 实现onTrigger回调，结合triggerCondition使用，满足回调条件触发回调，接收到回调通知后，使用takeNext()查询订阅的事件
  onTrigger: (curRow: number, curSize: number, holder: hiAppEvent.AppEventPackageHolder) => {
    if (holder == null) {
      hilog.error(0x0000, 'hiAppEvent', "holder is null");
      return;
    }
    hilog.info(0x0000, 'hiAppEvent', `curRow=${curRow}, curSize=${curSize}`);
    let eventPkg: hiAppEvent.AppEventPackage | null = null;
    while ((eventPkg = holder.takeNext()) != null) {
      hilog.info(0x0000, 'hiAppEvent', `eventPkg.packageId=${eventPkg.packageId}`);
      hilog.info(0x0000, 'hiAppEvent', `eventPkg.row=${eventPkg.row}`);
      hilog.info(0x0000, 'hiAppEvent', `eventPkg.size=${eventPkg.size}`);
      for (const eventInfo of eventPkg.data) {
        hilog.info(0x0000, 'hiAppEvent', `eventPkg.data=${eventInfo}`);
      }
    }
  }
});
```

方法二：未设置回调条件参数，使用事件订阅返回的holder对象主动获取监听的事件。

针对异常退出时产生的崩溃事件（hiAppEvent.event.APP_CRASH）和应用冻屏事件（hiAppEvent.event.APP_FREEZE），系统捕获维测日志有一定耗时，典型情况下30s内完成，极端情况下2min左右完成。

在手动处理订阅事件的方法中，由于事件可能未生成或日志信息未抓取完成，建议在进程启动后延时重试调用takeNext()获取此类事件。

```ets
import { hilog } from '@kit.PerformanceAnalysisKit';

let holder: hiAppEvent.AppEventPackageHolder = hiAppEvent.addWatcher({
  name: "watcher2",
  // 订阅过滤条件，这里是订阅了系统事件领域的应用崩溃事件
  appEventFilters: [
    {
      domain: hiAppEvent.domain.OS,
      names: [hiAppEvent.event.APP_CRASH]
    }
  ],
});
// 通过订阅数据持有者holder，主动获取崩溃事件
if (holder != null) {
  let eventPkg: hiAppEvent.AppEventPackage | null = null;
  while ((eventPkg = holder.takeNext()) != null) {
    hilog.info(0x0000, 'hiAppEvent', `eventPkg.packageId=${eventPkg.packageId}`);
    hilog.info(0x0000, 'hiAppEvent', `eventPkg.row=${eventPkg.row}`);
    hilog.info(0x0000, 'hiAppEvent', `eventPkg.size=${eventPkg.size}`);
    for (const eventInfo of eventPkg.data) {
      hilog.info(0x0000, 'hiAppEvent', `eventPkg.data=${eventInfo}`);
    }
  }
}
```

方法三：实现onReceive()回调，当监听的事件发生后实时触发回调。

```ets
import { hilog } from '@kit.PerformanceAnalysisKit';

hiAppEvent.addWatcher({
  name: "watcher3",
  // 订阅过滤条件，这里是订阅了系统事件领域的应用崩溃事件
  appEventFilters: [
    {
      domain: hiAppEvent.domain.OS,
      names: [hiAppEvent.event.APP_CRASH]
    }
  ],
  // 实现onReceive回调，监听到事件后实时回调
  onReceive: (domain: string, appEventGroups: Array<hiAppEvent.AppEventGroup>) => {
    hilog.info(0x0000, 'hiAppEvent', `domain=${domain}`);
    for (const eventGroup of appEventGroups) {
      hilog.info(0x0000, 'hiAppEvent', `eventName=${eventGroup.name}`);
      for (const eventInfo of eventGroup.appEventInfos) {
        hilog.info(0x0000, 'hiAppEvent', `event=${JSON.stringify(eventInfo)}`, );
      }
    }
  }
});
```

#### hiAppEvent.removeWatcher

removeWatcher(watcher: Watcher): void

移除事件观察者。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**参数：**

参数名类型必填说明watcher[Watcher](#ZH-CN_TOPIC_0000002529285653__watcher)是事件观察者。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[应用事件打点错误码](../../errors/应用事件打点错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.11102001Invalid watcher name. Possible causes: 1. Contain invalid characters; 2. Length is invalid.

**示例：**

```ets
// 1. 定义一个事件观察者
let watcher: hiAppEvent.Watcher = {
  name: "watcher1",
}

// 2. 添加一个事件观察者来订阅事件
hiAppEvent.addWatcher(watcher);

// 3. 移除该事件观察者以取消订阅事件
hiAppEvent.removeWatcher(watcher);
```

#### hiAppEvent.setEventParam12+

setEventParam(params: Record<string, ParamType>, domain: string, name?: string): Promise<void>

事件自定义参数设置方法，使用Promise方式作为异步回调。在同一生命周期中，可以通过事件领域和事件名称关联系统事件和应用事件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**参数：**

参数名类型必填说明paramsRecord<string, [ParamType](#ZH-CN_TOPIC_0000002529285653__paramtype12)>是

事件自定义参数对象。参数名和参数值规格定义如下：

- 参数名为string类型，首字符必须为字母字符或$字符。中间字符必须为数字字符、字母字符或下划线字符。结尾字符必须为数字字符或字母字符。长度非空且不超过32个字符。

- 参数值为[ParamType](#ZH-CN_TOPIC_0000002529285653__paramtype12)类型，参数值长度需在1024个字符以内。

- 参数个数需在64个以内。

domainstring是事件领域。事件领域可支持关联应用事件和系统事件（hiAppEvent.domain.OS）。namestring否

事件名称。默认为空字符串，空字符串表示关联事件领域下的所有事件名称。事件名称可支持关联应用事件和系统事件，其中系统事件仅支持关联：

- [崩溃事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-crash-events)（hiAppEvent.event.APP_CRASH）

- [应用冻屏事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-freeze-events)（hiAppEvent.event.APP_FREEZE）

- [资源泄漏事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-resourceleak-events)（hiAppEvent.event.RESOURCE_OVERLIMIT）。

**注意**：从API version 20开始，支持[资源泄漏事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-resourceleak-events)。

**返回值：**

类型说明Promise<void>Promise对象，无返回结果。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[应用事件打点错误码](../../errors/应用事件打点错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.11100001Function disabled. Possible caused by the param disable in ConfigOption is true.11101001Invalid event domain. Possible causes: 1. Contain invalid characters; 2. Length is invalid.11101002Invalid event name. Possible causes: 1. Contain invalid characters; 2. Length is invalid.11101004Invalid string length of the event parameter.11101005Invalid event parameter name. Possible causes: 1. Contain invalid characters; 2. Length is invalid.11101007The number of parameter keys exceeds the limit.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let params: Record<string, hiAppEvent.ParamType> = {
  "int_data": 100,
  "str_data": "strValue",
};

// 给应用事件追加自定义参数
hiAppEvent.setEventParam(params, "test_domain", "test_event").then(() => {
  hilog.info(0x0000, 'hiAppEvent', `success to set event param`);
}).catch((err: BusinessError) => {
  hilog.error(0x0000, 'hiAppEvent', `code: ${err.code}, message: ${err.message}`);
});
```

#### hiAppEvent.setEventConfig15+

setEventConfig(name: string, config: Record<string, ParamType>): Promise<void>

事件相关的配置参数设置方法，使用Promise方式作为异步回调。在同一生命周期中，可以通过事件名称，设置事件相关的配置参数。

不同的事件有不同的配置项，目前仅支持以下事件：

- MAIN_THREAD_JANK（参数配置详见[主线程超时事件检测](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-mainthreadjank-events#seteventconfig接口参数设置说明)）
- APP_CRASH（参数配置详见[崩溃日志配置参数设置介绍](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-crash-events#崩溃日志规格自定义参数设置)）
- RESOURCE_OVERLIMIT（参数配置详见[资源泄漏事件检测](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-resourceleak-events#自定义规格设置)）

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**参数：**

参数名类型必填说明namestring是事件名称。configRecord<string, [ParamType](#ZH-CN_TOPIC_0000002529285653__paramtype12)>是

事件自定义参数对象。参数名和参数值规格定义如下：

- 参数名为string类型，要求非空，且参数名长度需在1024个字符以内。

- 参数值为ParamType类型，参数值长度需在1024个字符以内。

**返回值：**

类型说明Promise<void>Promise对象，无返回结果。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3.Parameter verification failed.

**示例：**

以下示例用于模拟配置MAIN_THREAD_JANK事件的采集堆栈自定义参数：

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let params: Record<string, hiAppEvent.ParamType> = {
  "log_type": "1",
  "sample_interval": "100",
  "ignore_startup_time": "11",
  "sample_count": "21",
  "report_times_per_app": "3"
};
hiAppEvent.setEventConfig(hiAppEvent.event.MAIN_THREAD_JANK, params).then(() => {
  hilog.info(0x0000, 'hiAppEvent', `Successfully set sampling stack parameters.`);
}).catch((err: BusinessError) => {
hilog.error(0x0000, 'hiAppEvent', `Failed to set sample stack value. Code: ${err.code}, message: ${err.message}`);
});
```

#### hiAppEvent.configEventPolicy22+

configEventPolicy(policy: EventPolicy): Promise<void>

系统事件相关的配置策略设置方法，使用Promise方式作为异步回调。

在同一生命周期中，可以通过配置策略设置系统事件相关的策略参数。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**参数：**

参数名类型必填说明policy[EventPolicy](#ZH-CN_TOPIC_0000002529285653__eventpolicy22)是系统事件配置策略。

**返回值：**

类型说明Promise<void>

Promise对象，无返回结果。

各个事件的事件配置策略，详细规格见[EventPolicy](#ZH-CN_TOPIC_0000002529285653__eventpolicy22)类型说明。若配置策略设置有误，会导致接口返回失败。

- 参数类型设置有误，则返回401通用错误信息；

- 参数规格设置有误，则在hilog日志输出相关错误信息。

**示例：**

以下示例用于模拟设置MAIN_THREAD_JANK事件的配置策略：

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let policy: hiAppEvent.EventPolicy = {
  "mainThreadJankPolicy":{
    "logType": 1,
    "sampleInterval": 100,
    "ignoreStartupTime": 11,
    "sampleCount": 21,
    "reportTimesPerApp": 3,
    "autoStopSampling": true
  }
};
hiAppEvent.configEventPolicy(policy).then(() => {
  hilog.info(0x0000, 'hiAppEvent', `Successfully set main thread jank event policy.`);
}).catch((err: BusinessError) => {
  hilog.error(0x0000, 'hiAppEvent', `Failed to set main thread jank event policy. Code: ${err?.code}, message: ${err?.message}`);
});
```

#### Watcher

提供事件观察者的参数选项。用于配置和管理事件的观察者，实现对特定事件的监听和处理。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

名称类型只读可选说明namestring否否观察者名称，用于唯一标识观察者。首字符必须为字母字符，中间字符必须为数字字符、字母字符或下划线字符，结尾字符必须为数字字符或字母字符，长度非空且不超过32个字符。如testName1、crash_Watcher等。triggerCondition[TriggerCondition](#ZH-CN_TOPIC_0000002529285653__triggercondition)否是订阅回调触发条件，需要与回调函数onTrigger一同传入才会生效。默认不触发。appEventFilters[AppEventFilter](#ZH-CN_TOPIC_0000002529285653__appeventfilter)[]否是订阅过滤条件，在需要对订阅事件进行过滤时传入。默认不过滤事件。onTrigger(curRow: number, curSize: number, holder: [AppEventPackageHolder](#ZH-CN_TOPIC_0000002529285653__appeventpackageholder)) => void否是

订阅回调函数，需要与回调触发条件triggerCondition一同传入才会生效，函数入参说明如下：

curRow：在本次回调触发时的订阅事件总数量；

curSize：在本次回调触发时的订阅事件总大小，单位为byte；

holder：订阅数据持有者对象，可以通过其对订阅事件进行处理。

onReceive11+(domain: string, appEventGroups: Array<[AppEventGroup](#ZH-CN_TOPIC_0000002529285653__appeventgroup11)>) => void否是

订阅实时回调函数，与回调函数onTrigger同时存在时，只触发此回调，函数入参说明如下：

domain：回调事件的领域名称；

appEventGroups：回调事件集合。

不建议在回调函数中执行[移除观察者](#ZH-CN_TOPIC_0000002529285653__hiappeventremovewatcher)的操作，watcher一旦被移除，则其原有的订阅回调功能也会随之失效，可能会造成某些事件发生后无订阅回调情况。

#### TriggerCondition

提供设置[Watcher](#ZH-CN_TOPIC_0000002529285653__watcher)的onTrigger回调触发条件的参数选项。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

名称类型只读可选说明rownumber否是满足触发回调的事件总数量，正整数。默认值0，不触发回调。传入负值时，会被置为默认值。sizenumber否是满足触发回调的事件总大小，正整数，单位为byte。默认值0，不触发回调。传入负值时，会被置为默认值。timeOutnumber否是满足触发回调的超时时长，正整数，单位为30s。默认值0，不触发回调。传入负值时，会被置为默认值。

#### AppEventFilter

提供设置[Watcher](#ZH-CN_TOPIC_0000002529285653__watcher)的订阅过滤条件的参数选项。用于在事件观察者中设置事件过滤条件，确保只有满足过滤条件的事件才会被监听处理。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

名称类型只读可选说明domainstring否否需要订阅的事件领域。可以是系统事件领域（hiAppEvent.domain.OS）或开发者在使用[Write](#ZH-CN_TOPIC_0000002529285653__hiappeventwrite-1)接口时传入的自定义事件信息（[AppEventInfo](#ZH-CN_TOPIC_0000002529285653__appeventinfo)）中的事件领域。eventTypes[EventType](#ZH-CN_TOPIC_0000002529285653__eventtype)[]否是需要订阅的事件类型集合。默认不进行过滤。names11+string[]否是需要订阅的事件名称集合。默认不进行过滤。

不同类型应用上，系统事件的订阅规格不同，具体规格可参见[HiAppEvent约束与限制](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-intro#约束与限制)。

#### AppEventPackageHolder

订阅数据持有者类，用于对事件信息进行处理。

#### constructor

constructor(watcherName: string)

类构造函数，用于创建订阅数据持有者实例。先通过[addWatcher](#ZH-CN_TOPIC_0000002529285653__hiappeventaddwatcher)添加事件观察者，再通过观察者名称关联到应用内已添加的观察者对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**参数：**

参数名类型必填说明watcherNamestring是已通过[addWatcher](#ZH-CN_TOPIC_0000002529285653__hiappeventaddwatcher)添加的事件观察者名称。若未通过addWatcher添加，则默认无数据。

**示例：**

```ets
// 添加数据观察者“Watcher1”，订阅监听系统事件
hiAppEvent.addWatcher({
  name: "Watcher1",
  appEventFilters: [
    {
      domain: hiAppEvent.domain.OS,
    }
  ],
  });

// 创建订阅数据持有者实例，holder1持有的数据为上述addWatcher中添加的观察者“Watcher1”监听到的事件
let holder1: hiAppEvent.AppEventPackageHolder = new hiAppEvent.AppEventPackageHolder("Watcher1");
```

#### setSize

setSize(size: number): void

设置每次取出的事件包的数据大小阈值。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**参数：**

参数名类型必填说明sizenumber是数据大小阈值，单位为byte。取值范围[0, 2^31-1]，超出范围会抛异常。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[应用事件打点错误码](../../errors/应用事件打点错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.11104001Invalid size value. Possible caused by the size value is less than or equal to zero.

**示例：**

```ets
// 创建订阅数据持有者实例，holder2持有的数据为已通过addWatcher添加的观察者“Watcher1”监听到的事件
let holder2: hiAppEvent.AppEventPackageHolder = new hiAppEvent.AppEventPackageHolder("Watcher1");
// 设置每次取出事件包的数据大小阈值为1000byte
holder2.setSize(1000);
```

#### setRow12+

setRow(size: number): void

设置每次取出的事件包的数据条数，优先级高于setSize，和setSize同时调用时仅setRow生效。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**参数：**

参数名类型必填说明sizenumber是事件条数，单位为条。取值范围(0, 2^31-1]，超出范围会抛异常。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[应用事件打点错误码](../../errors/应用事件打点错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.11104001Invalid size value. Possible caused by the size value is less than or equal to zero.

**示例：**

```ets
// 创建订阅数据持有者实例，holder3持有的数据为已通过addWatcher添加的观察者“Watcher1”监听到的事件
let holder3: hiAppEvent.AppEventPackageHolder = new hiAppEvent.AppEventPackageHolder("Watcher1");
// 设置每次取出的事件包的数据条数为1000条
holder3.setRow(1000);
```

#### takeNext

takeNext(): AppEventPackage

获取订阅事件。

系统根据setSize设置的数据大小阈值或setRow设置的条数来取出订阅事件数据，默认取1条订阅事件。当订阅事件数据全部被取出时返回null。

当setRow和setSize同时调用时仅setRow生效。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**返回值：**

类型说明[AppEventPackage](#ZH-CN_TOPIC_0000002529285653__appeventpackage)取出的事件包对象，订阅事件数据被全部取出后会返回null。

**示例：**

```ets
// 创建订阅数据持有者实例，holder4持有的数据为已通过addWatcher添加的观察者“Watcher1”监听到的事件
let holder4: hiAppEvent.AppEventPackageHolder = new hiAppEvent.AppEventPackageHolder("Watcher1");
// 获取订阅事件
let eventPkg: hiAppEvent.AppEventPackage | null = holder4.takeNext();
```

#### AppEventInfo

提供事件信息的参数选项。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

名称类型只读可选说明domainstring否否事件领域。事件领域名称支持数字、字母、下划线字符，需要以字母开头且不能以下划线结尾，长度非空且不超过32个字符。namestring否否事件名称。首字符必须为字母字符或$字符，中间字符必须为数字字符、字母字符或下划线字符，结尾字符必须为数字字符或字母字符，长度非空且不超过48个字符。eventType[EventType](#ZH-CN_TOPIC_0000002529285653__eventtype)否否事件类型。paramsobject否否

事件参数对象，包含每个事件参数的参数名和参数值。**系统事件中params包含的字段已由各系统事件定义，具体字段含义在各类系统事件指南的介绍中，例如[崩溃事件介绍](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-crash-events)。** 针对应用事件，[Write](#ZH-CN_TOPIC_0000002529285653__hiappeventwrite-1)打点写入的参数由开发者定义，其规格如下：

- 参数名为string类型，首字符必须为字母字符或$字符，中间字符必须为数字字符、字母字符或下划线字符，结尾字符必须为数字字符或字母字符，长度非空且不超过32个字符。如testName、$123_name等。

- 参数值支持string、number、boolean、数组类型。string类型参数长度需在8*1024个字符以内，超出后会和对应的参数名一同被丢弃；number类型参数取值需在Number.MIN_SAFE_INTEGER~Number.MAX_SAFE_INTEGER范围内，超出可能会产生不确定值；数组类型参数中的元素类型只能全为string、number、boolean中的一种，且元素个数需在100以内，超出部分即从第101个元素开始会被丢弃。

- 参数个数需在32个以内，超出的参数会做丢弃处理。

#### AppEventPackage

提供订阅返回的事件包的参数定义。可用于获取事件包的详细信息，事件包由[takeNext](#ZH-CN_TOPIC_0000002529285653__takenext)接口获得。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

名称类型只读可选说明packageIdnumber否否

事件包ID，从0开始自动递增。

**元服务API：** 从API version 11开始，该参数支持在元服务中使用。

rownumber否否

事件包的事件数量。

**元服务API：** 从API version 11开始，该参数支持在元服务中使用。

sizenumber否否

事件包的事件大小，单位为byte。

**元服务API：** 从API version 11开始，该参数支持在元服务中使用。

datastring[]否否

事件包的事件信息。

**元服务API：** 从API version 11开始，该参数支持在元服务中使用。

appEventInfos12+Array<[AppEventInfo](#ZH-CN_TOPIC_0000002529285653__appeventinfo)>否否

事件对象集合。

**元服务API：** 从API version 12开始，该参数支持在元服务中使用。

#### AppEventGroup11+

提供订阅返回的事件组的参数定义。可用于获取事件组的详细信息，事件组常在[Watcher](#ZH-CN_TOPIC_0000002529285653__watcher)的onReceive回调中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

名称类型只读可选说明namestring否否事件名称。appEventInfosArray<[AppEventInfo](#ZH-CN_TOPIC_0000002529285653__appeventinfo)>否否事件对象集合。

#### hiAppEvent.write

write(info: AppEventInfo, callback: AsyncCallback<void>): void

应用事件打点方法，将AppEventInfo类型的事件进行存储，使用callback方式作为异步回调。通过此接口写入的事件对象是开发者自定义的对象，为了避免与系统事件产生冲突混淆，不建议写入系统事件（[Event](#ZH-CN_TOPIC_0000002529285653__hiappeventevent)中定义的系统事件名称常量）。此接口写入的事件可通过订阅事件观察者（[addWatcher](#ZH-CN_TOPIC_0000002529285653__hiappeventaddwatcher)）进行订阅。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**参数：**

参数名类型必填说明info[AppEventInfo](#ZH-CN_TOPIC_0000002529285653__appeventinfo)是应用事件对象。其内部定义的事件名称建议避免与[Event](#ZH-CN_TOPIC_0000002529285653__hiappeventevent)中定义的系统事件名称常量产生冲突。callbackAsyncCallback<void>是打点回调函数。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[应用事件打点错误码](../../errors/应用事件打点错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.11100001Function disabled. Possible caused by the param disable in ConfigOption is true.11101001Invalid event domain. Possible causes: 1. Contain invalid characters; 2. Length is invalid.11101002Invalid event name. Possible causes: 1. Contain invalid characters; 2. Length is invalid.11101003Invalid number of event parameters. Possible caused by the number of parameters is over 32.11101004Invalid string length of the event parameter.11101005Invalid event parameter name. Possible causes: 1. Contain invalid characters; 2. Length is invalid.11101006Invalid array length of the event parameter.

write接口涉及I/O操作，执行时间通常在毫秒级别。因此，开发者应根据实际业务需求，确定该接口是在主线程还是在子线程中调用。

可参考[多线程并发概述](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/multi-thread-concurrency-overview)，以实现在子线程中调用接口。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let eventParams: Record<string, number | string> = {
  "int_data": 100,
  "str_data": "strValue",
};

// 应用事件打点，使用callback方式作为异步回调
hiAppEvent.write({
  domain: "test_domain",
  name: "test_event",
  eventType: hiAppEvent.EventType.FAULT,
  params: eventParams,
}, (err: BusinessError) => {
  if (err) {
    hilog.error(0x0000, 'hiAppEvent', `code: ${err.code}, message: ${err.message}`);
    return;
  }
  hilog.info(0x0000, 'hiAppEvent', `success to write event`);
});
```

#### hiAppEvent.write

write(info: AppEventInfo): Promise<void>

应用事件打点方法，将AppEventInfo类型的事件进行存储，使用Promise方式作为异步回调。通过此接口写入的事件对象是开发者自定义的对象，为了避免与系统事件产生冲突混淆，不建议写入系统事件（[Event](#ZH-CN_TOPIC_0000002529285653__hiappeventevent)中定义的系统事件名称常量）。此接口写入的事件可通过订阅事件观察者（[addWatcher](#ZH-CN_TOPIC_0000002529285653__hiappeventaddwatcher)）进行处理。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**参数：**

参数名类型必填说明info[AppEventInfo](#ZH-CN_TOPIC_0000002529285653__appeventinfo)是应用事件对象。其中的事件名称建议避免与[Event](#ZH-CN_TOPIC_0000002529285653__hiappeventevent)中定义的系统事件名称常量冲突混淆。

**返回值：**

类型说明Promise<void>Promise对象，无返回结果。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[应用事件打点错误码](../../errors/应用事件打点错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.11100001Function disabled. Possible caused by the param disable in ConfigOption is true.11101001Invalid event domain. Possible causes: 1. Contain invalid characters; 2. Length is invalid.11101002Invalid event name. Possible causes: 1. Contain invalid characters; 2. Length is invalid.11101003Invalid number of event parameters. Possible caused by the number of parameters is over 32.11101004Invalid string length of the event parameter.11101005Invalid event parameter name. Possible causes: 1. Contain invalid characters; 2. Length is invalid.11101006Invalid array length of the event parameter.

write接口涉及I/O操作，执行时间通常在毫秒级别。因此，开发者应根据实际业务需求，确定该接口是在主线程还是在子线程中调用。

可参考[多线程并发概述](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/multi-thread-concurrency-overview)，以实现在子线程中调用接口。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let eventParams: Record<string, number | string> = {
  "int_data": 100,
  "str_data": "strValue",
};

// 应用事件打点，使用Promise方式作为异步回调
hiAppEvent.write({
  domain: "test_domain",
  name: "test_event",
  eventType: hiAppEvent.EventType.FAULT,
  params: eventParams,
}).then(() => {
  hilog.info(0x0000, 'hiAppEvent', `success to write event`);
}).catch((err: BusinessError) => {
  hilog.error(0x0000, 'hiAppEvent', `code: ${err.code}, message: ${err.message}`);
});
```

#### hiAppEvent.addProcessor11+

addProcessor(processor: Processor): number

添加数据处理者配置信息，用于配置处理者接收的事件名等信息。事件发生后处理者可以接收事件。

该接口为同步接口，包含耗时操作。为了确保性能，建议使用[addProcessorFromConfig](#ZH-CN_TOPIC_0000002529285653__hiappeventaddprocessorfromconfig20)异步接口或者交由子线程执行。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**参数：**

参数名类型必填说明processor[Processor](#ZH-CN_TOPIC_0000002529285653__processor11)是上报事件的数据处理者。

**返回值：**

类型说明number所添加上报事件数据处理者的ID，标识唯一数据处理者，可用于移除数据处理者。 添加失败返回-1，添加成功返回大于0的值。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.

**示例：**

```ets
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
    let processor: hiAppEvent.Processor = {
      name: 'analytics_demo'
    };
    let id: number = hiAppEvent.addProcessor(processor);
    hilog.info(0x0000, 'hiAppEvent', `addProcessor event was successful, id=${id}`);
} catch (error) {
    hilog.error(0x0000, 'hiAppEvent', `failed to addProcessor event, code=${error.code}`);
}
```

#### hiAppEvent.addProcessorFromConfig20+

addProcessorFromConfig(processorName: string, configName?: string): Promise<number>

添加数据处理者配置信息。系统会自动解析预置在目录“/system/etc/hiappevent”的processor.json配置文件，并根据configName字段加载对应的processor信息（例如支持接收的故障事件名称等信息）。

配置完成后，事件发生时系统将自动触发该回调。使用Promise异步回调。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**参数：**

参数名类型必填说明processorNamestring是

数据处理者的名称。名称只能包含大小写字母、数字、下划线和$，不能以数字开头，长度非空且不超过256个字符。

当前取值仅支持“ha_app_event”，表示接口故障处理者。

configNamestring否

数据处理者的配置名称，系统会根据配置名称从系统预置的processor.json配置文件中自动加载对应的配置项。只能包含大小写字母、数字、下划线和$，不能以数字开头，长度非空且不超过256个字符。

当前取值仅支持默认值“SDK_OCG”，用于配置“接口故障处理者”可处理的事件名称等信息。

**返回值：**

类型说明Promise<number>Promise对象。返回添加的事件数据处理者的唯一ID，可用于移除该数据处理者。 添加失败返回11105001错误码。

**错误码：**

以下错误码的详细介绍请参见[应用事件打点错误码](../../errors/应用事件打点错误码.md)。

错误码ID错误信息11105001Invalid parameter value. Possible causes: 1. Incorrect parameter length; 2. Incorrect parameter format.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

hiAppEvent.addProcessorFromConfig("test_name").then((processorId) => {
  hilog.info(0x0000, 'hiAppEvent', `Succeeded in adding processor from config, processorId=${processorId}`);
}).catch((err: BusinessError) => {
  hilog.error(0x0000, 'hiAppEvent', `Failed to add processor from config, code: ${err.code}, message: ${err.message}`);
});
```

#### hiAppEvent.removeProcessor11+

removeProcessor(id: number): void

移除上报事件的数据处理者。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**参数：**

参数名类型必填说明idnumber是上报事件数据处理者ID。值大于0。由调用[addProcessor](#ZH-CN_TOPIC_0000002529285653__hiappeventaddprocessor11)或[addProcessorFromConfig](#ZH-CN_TOPIC_0000002529285653__hiappeventaddprocessorfromconfig20)接口返回值所得。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.

**示例：**

```ets
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
    let processor: hiAppEvent.Processor = {
      name: 'analytics_demo'
    };
    let id: number = hiAppEvent.addProcessor(processor);
    // 根据添加数据处理者返回的标识id移除特定数据处理者
    hiAppEvent.removeProcessor(id);
} catch (error) {
    hilog.error(0x0000, 'hiAppEvent', `failed to removeProcessor event, code=${error.code}`);
}
```

#### hiAppEvent.setUserId11+

setUserId(name: string, value: string): void

设置用户ID值。用于在配置[Processor](#ZH-CN_TOPIC_0000002529285653__processor11)数据处理者时进行关联。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**参数：**

参数名类型必填说明namestring是用户ID的key。只能包含大小写字母、数字、下划线和 $，不能以数字开头，长度非空且不超过256个字符。valuestring是用户ID的值。长度不超过256，当值为null或空字符串时，则清除用户ID。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.

**示例：**

```ets
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  hiAppEvent.setUserId('key', 'value');
} catch (error) {
  hilog.error(0x0000, 'hiAppEvent', `failed to setUserId event, code=${error.code}`);
}
```

#### hiAppEvent.getUserId11+

getUserId(name: string): string

获取通过setUserId接口设置的value值。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**参数：**

参数名类型必填说明namestring是用户ID的key。只能包含大小写字母、数字、下划线和 $，不能以数字开头，长度非空且不超过256个字符。

**返回值：**

类型说明string用户ID的值。没有查到返回空字符串。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.

**示例：**

```ets
import { hilog } from '@kit.PerformanceAnalysisKit';

hiAppEvent.setUserId('key', 'value');
try {
  let value: string = hiAppEvent.getUserId('key');
  hilog.info(0x0000, 'hiAppEvent', `getUserId event was successful, userId=${value}`);
} catch (error) {
  hilog.error(0x0000, 'hiAppEvent', `failed to getUserId event, code=${error.code}`);
}
```

#### hiAppEvent.setUserProperty11+

setUserProperty(name: string, value: string): void

设置用户属性值。用于在配置[Processor](#ZH-CN_TOPIC_0000002529285653__processor11)数据处理者时进行关联。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**参数：**

参数名类型必填说明namestring是用户属性的key。只能包含大小写字母、数字、下划线和 $，不能以数字开头，长度非空且不超过256个字符。valuestring是用户属性的值。长度不超过1024，当值为null或空字符串时，则清除用户属性。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.

**示例：**

```ets
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  hiAppEvent.setUserProperty('key', 'value');
} catch (error) {
  hilog.error(0x0000, 'hiAppEvent', `failed to setUserProperty event, code=${error.code}`);
}
```

#### hiAppEvent.getUserProperty11+

getUserProperty(name: string): string

获取通过setUserProperty接口设置的value值。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**参数：**

参数名类型必填说明namestring是用户属性的key。只能包含大小写字母、数字、下划线和 $，不能以数字开头，长度非空且不超过256个字符。

**返回值：**

类型说明string用户属性的值。没有查到返回空字符串。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.

**示例：**

```ets
import { hilog } from '@kit.PerformanceAnalysisKit';

hiAppEvent.setUserProperty('key', 'value');
try {
  let value: string = hiAppEvent.getUserProperty('key');
  hilog.info(0x0000, 'hiAppEvent', `getUserProperty event was successful, userProperty=${value}`);
} catch (error) {
  hilog.error(0x0000, 'hiAppEvent', `failed to getUserProperty event, code=${error.code}`);
}
```

#### hiAppEvent.clearData

clearData(): void

应用事件打点数据清理方法，将当前应用存储在本地的打点数据进行清除。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**示例：**

```ets
hiAppEvent.clearData();
```

#### hiAppEvent.configure

configure(config: ConfigOption): void

应用事件打点配置方法，支持配置打点开关和目录存储配额大小。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**参数：**

参数名类型必填说明config[ConfigOption](#ZH-CN_TOPIC_0000002529285653__configoption)是应用事件打点配置项对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[应用事件打点错误码](../../errors/应用事件打点错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.11103001Invalid max storage quota value. Possible caused by incorrectly formatted.

**示例：**

```ets
// 配置打点开关为关闭状态
let config1: hiAppEvent.ConfigOption = {
  disable: true,
};
hiAppEvent.configure(config1);

// 配置文件目录存储配额为100M
let config2: hiAppEvent.ConfigOption = {
  maxStorage: '100M',
};
hiAppEvent.configure(config2);
```

#### ConfigOption

提供对应用事件打点功能的配置选项。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

名称类型只读可选说明disableboolean否是打点功能开关，默认值为false。true：关闭打点功能，false：开启打点功能。maxStoragestring否是

打点数据存放目录的配额大小，默认值为“10M”。建议配额大小不超过10M，配额过大可能会影响接口效率。

在目录大小超出配额后，下次打点会触发对目录的清理操作：按从旧到新的顺序逐个删除打点数据文件，直到目录大小不超出配额时结束。

配额值字符串规格如下：

- 配额值字符串只由数字字符和大小单位字符（单位字符支持[b|k|kb|m|mb|g|gb|t|tb]，不区分大小写）构成。

- 配额值字符串必须以数字开头，后面可以选择不传单位字符（默认使用byte作为单位），或者以单位字符结尾。

#### EventPolicy22+

提供系统事件配置策略的定义，用于使用[configEventPolicy](#ZH-CN_TOPIC_0000002529285653__hiappeventconfigeventpolicy22)设置事件配置策略。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

名称类型只读可选说明mainThreadJankPolicy[MainThreadJankPolicy](#ZH-CN_TOPIC_0000002529285653__mainthreadjankpolicy22)否是主线程超时事件配置策略。

#### MainThreadJankPolicy22+

提供主线程超时事件配置策略的定义。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

名称类型只读可选说明logTypenumber否是

采集日志的类型。

logType=0：默认值，主线程连续两次超时150ms~450ms，采集调用栈；主线程超时450ms，采集trace。

logType=1：仅采集调用栈，触发检测的阈值用户自定义。

logType=2：仅采集trace。

ignoreStartupTimenumber否是应用启动期间忽略主线程超时检测的时间。单位：秒，默认值：10，最小值：3。sampleIntervalnumber否是主线程超时检测间隔和采样间隔。单位：毫秒，默认值：150，取值范围：[50, 500]。sampleCountnumber否是

主线程超时采样次数。单位：次，默认值：10，最小值：1。

最大值需要结合自定义的sampleInterval进行动态计算，计算公式：sampleCount <= (2500 / sampleInterval - 4)。

reportTimesPerAppnumber否是

同一个应用的PID一个生命周期内，主线程超时采样上报次数。一个生命周期内只能设置一次。

默认值：1，单位：次。

开发者选项打开，每小时上报次数范围：[1, 3]。

开发者选项关闭，每分钟上报次数范围：[1, 3]。

autoStopSamplingboolean否是

主线程超时结束时，是否自动停止采样主线程堆栈。

true: 超时结束或达到设置的采样次数，停止采样。

false：达到设置的采样次数时停止采样。

默认值：false。

#### Processor11+

可以上报事件的数据处理者对象。用于事件的上报和管理，开发者可自定义数据处理配置，满足不同的数据处理需求。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

名称类型只读可选说明namestring否否

数据处理者的名称。名称只能包含大小写字母、数字、下划线和 $，不能以数字开头，长度非空且不超过256个字符。

**元服务API：** 从API version 11开始，该参数支持在元服务中使用。

debugModeboolean否是

是否开启debug模式，默认值为false。配置值为true表示开启debug模式，false表示不开启debug模式。

**元服务API：** 从API version 11开始，该参数支持在元服务中使用。

routeInfostring否是

服务器位置信息，默认为空字符串。传入字符串长度不能超过8KB，超过时会被置为默认值。

**元服务API：** 从API version 11开始，该参数支持在元服务中使用。

appIdstring否是

应用id，默认为空字符串。传入字符串长度不能超过8KB，超过时会被置为默认值。

**元服务API：** 从API version 11开始，该参数支持在元服务中使用。

onStartReportboolean否是

数据处理者在启动时是否上报事件，默认值为false。配置值为true表示上报事件，false表示不上报事件。

**元服务API：** 从API version 11开始，该参数支持在元服务中使用。

onBackgroundReportboolean否是

当应用程序进入后台时是否上报事件，默认值为false。配置值为true表示上报事件，false表示不上报事件。

**元服务API：** 从API version 11开始，该参数支持在元服务中使用。

periodReportnumber否是

事件定时上报时间周期，单位为秒。传入数值必须大于或等于0，小于0时会被置为默认值0，不进行定时上报。

**元服务API：** 从API version 11开始，该参数支持在元服务中使用。

batchReportnumber否是

事件上报阈值，当事件条数达到阈值时上报事件。传入数值必须大于0且小于1000，不在数值范围内会被置为默认值0，不进行上报。

**元服务API：** 从API version 11开始，该参数支持在元服务中使用。

userIdsstring[]否是

数据处理者可以上报的用户ID的name数组。name对应[setUserId](#ZH-CN_TOPIC_0000002529285653__hiappeventsetuserid11)接口的name参数。默认为空数组。

**元服务API：** 从API version 11开始，该参数支持在元服务中使用。

userPropertiesstring[]否是

数据处理者可以上报的用户属性的name数组。name对应[setUserProperty](#ZH-CN_TOPIC_0000002529285653__hiappeventsetuserproperty11)接口的name参数。默认为空数组。

**元服务API：** 从API version 11开始，该参数支持在元服务中使用。

eventConfigs[AppEventReportConfig](#ZH-CN_TOPIC_0000002529285653__appeventreportconfig11)[]否是

数据处理者可以上报的事件描述配置数组。默认为空数组。

**元服务API：** 从API version 11开始，该参数支持在元服务中使用。

configId12+number否是

数据处理者配置id。传入数值必须大于或等于0，小于0时会被置为默认值0。传入的值大于0时，与数据处理者的名称name共同唯一标识数据处理者。

**元服务API：** 从API version 12开始，该参数支持在元服务中使用。

customConfigs12+Record<string, string>否是

自定义扩展参数。传入参数名和参数值不符合规格会默认不配置扩展参数，其规格定义如下：

- 参数名为string类型，首字符必须为字母字符或$字符，中间字符必须为数字字符、字母字符或下划线字符，结尾字符必须为数字字符或字母字符，长度非空且不超过32个字符。

- 参数值为string类型，参数值长度需在1024个字符以内。

- 参数个数需在32个以内。

**元服务API：** 从API version 12开始，该参数支持在元服务中使用。

configName20+string否是

数据处理者的配置名称，系统会根据配置名称从系统预置的processor.json配置文件中自动加载对应的配置项。只能包含大小写字母、数字、下划线和$，不能以数字开头，长度非空且不超过256个字符。

当前取值仅支持默认值“SDK_OCG”，用于配置“接口故障处理者”可处理的事件名称等信息。

**元服务API：** 从API version 20开始，该参数支持在元服务中使用。

#### AppEventReportConfig11+

数据处理者可以上报事件的描述配置。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

名称类型只读可选说明domainstring否是事件领域。默认为空字符串，事件领域名称支持数字、字母、下划线字符，需要以字母开头且不能以下划线结尾，长度非空且不超过32个字符。namestring否是事件名称。默认为空字符串，首字符必须为字母字符或$字符，中间字符必须为数字字符、字母字符或下划线字符，结尾字符必须为数字字符或字母字符，长度非空且不超过48个字符。isRealTimeboolean否是是否实时上报事件。默认值为false，配置值为true表示实时上报事件，false表示不实时上报事件。

#### ParamType12+

type ParamType = number | string | boolean | Array<string>

事件自定义参数值的类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

类型说明number表示值类型为数字。string表示值类型为字符串。boolean表示值类型为布尔值。Array<string>表示值类型为字符串类型的数组。

#### EventType

事件类型枚举。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

名称值说明FAULT1故障类型事件。STATISTIC2统计类型事件。SECURITY3安全类型事件。BEHAVIOR4行为类型事件。

#### hiAppEvent.domain11+

提供领域名称常量。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

名称类型只读说明OSstring是系统领域。

#### hiAppEvent.event

提供事件名称常量。包含系统事件名称常量和应用事件名称常量，其中应用事件名称常量是为开发者在调用[Write](#ZH-CN_TOPIC_0000002529285653__hiappeventwrite-1)接口进行应用事件打点时预留的可选自定义事件名称。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

名称类型只读说明USER_LOGINstring是

用户登录事件。预留的应用事件名称常量。

**元服务API：** 从API version 11开始，该参数支持在元服务中使用。

USER_LOGOUTstring是

用户登出事件。预留的应用事件名称常量。

**元服务API：** 从API version 11开始，该参数支持在元服务中使用。

DISTRIBUTED_SERVICE_STARTstring是

分布式服务启动事件。预留的应用事件名称常量。

**元服务API：** 从API version 11开始，该参数支持在元服务中使用。

APP_CRASH11+string是

应用崩溃事件。系统事件名称常量。

**元服务API：** 从API version 11开始，该参数支持在元服务中使用。

APP_FREEZE11+string是

应用冻屏事件。系统事件名称常量。

**元服务API：** 从API version 11开始，该参数支持在元服务中使用。

APP_LAUNCH12+string是

应用启动耗时事件。系统事件名称常量。

**元服务API：** 从API version 12开始，该参数支持在元服务中使用。

SCROLL_JANK12+string是

应用滑动丢帧事件。系统事件名称常量。

**元服务API：** 从API version 12开始，该参数支持在元服务中使用。

CPU_USAGE_HIGH12+string是

应用CPU高负载事件。系统事件名称常量。

**元服务API：** 从API version 12开始，该参数支持在元服务中使用。

BATTERY_USAGE12+string是

应用24h功耗器件分解统计事件。系统事件名称常量。

**元服务API：** 从API version 12开始，该参数支持在元服务中使用。

RESOURCE_OVERLIMIT12+string是

应用资源泄漏事件。系统事件名称常量。

**元服务API：** 从API version 12开始，该参数支持在元服务中使用。

ADDRESS_SANITIZER12+string是

应用地址越界事件。系统事件名称常量。

**元服务API：** 从API version 12开始，该参数支持在元服务中使用。

MAIN_THREAD_JANK12+string是

应用主线程超时事件。系统事件名称常量。

**元服务API：** 从API version 12开始，该参数支持在元服务中使用。

APP_KILLED20+string是

应用终止事件。系统事件名称常量。

**元服务API：** 从API version 20开始，该参数支持在元服务中使用。

APP_HICOLLIE21+string是

应用任务执行超时事件。系统事件名称常量。

**元服务API：** 从API version 21开始，该参数支持在元服务中使用。

AUDIO_JANK_FRAME21+string是

应用音频卡顿事件。系统事件名称常量。

**元服务API：** 从API version 21开始，该参数支持在元服务中使用。

#### hiAppEvent.param

提供参数名称常量。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

名称类型只读说明USER_IDstring是用户自定义ID。DISTRIBUTED_SERVICE_NAMEstring是分布式服务名称。DISTRIBUTED_SERVICE_INSTANCE_IDstring是分布式服务实例ID。