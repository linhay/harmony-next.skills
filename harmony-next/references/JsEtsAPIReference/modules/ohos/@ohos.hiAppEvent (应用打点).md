# @ohos.hiAppEvent (应用打点)

本模块提供了应用事件打点能力，包括对打点数据的落盘，以及对打点功能的管理配置。

- 本模块接口从API version 9开始废弃，建议使用新接口[@ohos.hiviewdfx.hiAppEvent](@ohos.hiviewdfx.hiAppEvent (应用事件打点).md)替代。
- 本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import hiAppEvent from '@ohos.hiAppEvent';
```

#### 使用说明

开发者在使用应用事件打点功能前，需要首先了解应用事件相关的参数规格定义。

**事件名称**

事件名称为string类型，字符串非空且长度在48个字符以内，首字符必须为字母字符或$字符，中间字符必须为数字字符、字母字符或下划线字符，结尾字符必须为数字字符或字母字符。

**事件类型**

事件类型为[EventType](#ZH-CN_TOPIC_0000002529285655__eventtype)枚举类型。

**事件参数**

事件参数为object类型，key为事件的参数名称，value为事件的参数值，其规格定义如下：

- 参数名为string类型，字符串非空且长度在32个字符以内，首字符必须为字母字符或$字符，中间字符必须为数字字符、字母字符或下划线字符，结尾字符必须为数字字符或字母字符；
- 参数值支持string、number、boolean、数组类型；
- 参数值为string类型时，其长度需在8*1024个字符以内，超出会做丢弃处理；
- 参数值为number类型时，其取值需在Number.MIN_SAFE_INTEGER~Number.MAX_SAFE_INTEGER范围内，超出可能会产生不确定值；
- 参数值为数组类型时，数组中的元素类型只能全为string、number、boolean中的一种，且元素个数需在100以内，超出会做丢弃处理；
- 参数个数需在32以内，超出的参数会做丢弃处理。

**事件回调**

开发者在调用事件打点方法后，可以在回调函数中对打点返回值进行处理，当前支持callback形式和Promise形式的回调，其返回值规格定义如下：

- 返回值为0，表示事件校验成功，将事件直接落盘到事件文件；
- 返回值大于0，表示事件校验存在异常参数，在忽略异常参数后将事件落盘到事件文件；
- 返回值小于0，表示事件校验失败，不将事件落盘到事件文件。

#### hiAppEvent.write

write(eventName: string, eventType: EventType, keyValues: object, callback: AsyncCallback<void>): void

应用事件打点方法，将事件写入到当天的事件文件中，使用callback方式作为异步回调。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**参数：**

参数名类型必填说明eventNamestring是事件名称。eventType[EventType](#ZH-CN_TOPIC_0000002529285655__eventtype)是事件类型。keyValuesobject是事件参数。callbackAsyncCallback<void>是事件回调函数。

**示例：**

```ets
import { BusinessError } from '@ohos.base'

let eventParams: Record<string, number | string> = {
  "int_data": 100,
  "str_data": "strValue",
};
hiAppEvent.write("test_event", hiAppEvent.EventType.FAULT, eventParams, (err: BusinessError) => {
  if (err) {
    // 事件写入异常：事件存在异常参数时忽略异常参数后继续写入，或者事件校验失败时不执行写入
    console.error(`failed to write event, code=${err.code}`);
    return;
  }
  // 事件写入正常
  console.log(`success to write event`);
});
```

#### hiAppEvent.write

write(eventName: string, eventType: EventType, keyValues: object): Promise<void>

应用事件打点方法，将事件写入到当天的事件文件中，使用Promise方式作为异步回调。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**参数：**

参数名类型必填说明eventNamestring是事件名称。eventType[EventType](#ZH-CN_TOPIC_0000002529285655__eventtype)是事件类型。keyValuesobject是事件参数。

**返回值：**

类型说明Promise<void>Promise对象，可以在其then()、catch()方法中分别对事件写入成功、写入异常的情况进行异步处理。

**示例：**

```ets
import { BusinessError } from '@ohos.base'

let eventParams: Record<string, number | string> = {
  "int_data": 100,
  "str_data": "strValue",
};
hiAppEvent.write("test_event", hiAppEvent.EventType.FAULT, eventParams).then(() => {
  // 事件写入正常
  console.log(`success to write event`);
}).catch((err: BusinessError) => {
  // 事件写入异常：事件存在异常参数时忽略异常参数后继续写入，或者事件校验失败时不执行写入
  console.error(`failed to write event, code=${err.code}`);
});
```

#### hiAppEvent.configure

configure(config: ConfigOption): boolean

应用事件打点配置方法，可用于配置打点开关、文件目录存储限额大小等功能。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**参数：**

参数名类型必填说明config[ConfigOption](#ZH-CN_TOPIC_0000002529285655__configoption)是应用事件打点配置项对象。

**返回值：**

类型说明boolean配置结果，true 表示配置成功，false 表示配置失败。

**示例：**

```ets
// 配置应用事件打点功能开关
let config1: hiAppEvent.ConfigOption = {
  disable: true,
};
hiAppEvent.configure(config1);

// 配置事件文件目录存储限额大小
let config2: hiAppEvent.ConfigOption = {
  maxStorage: '100M',
};
hiAppEvent.configure(config2);
```

#### ConfigOption

此接口提供了应用打点的配置选项。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

名称类型只读可选说明disableboolean否是应用打点功能开关。配置值为true表示关闭打点功能，false表示不关闭打点功能。maxStoragestring否是打点数据本地存储文件所在目录的配额大小，默认限额为“10M”。所在目录大小超出限额后会对目录进行清理操作，会按从旧到新的顺序逐个删除打点数据文件，直到目录大小不超出限额时停止。

#### EventType

事件类型枚举。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

名称值说明FAULT1故障类型事件。STATISTIC2统计类型事件。SECURITY3安全类型事件。BEHAVIOR4行为类型事件。

#### Event

此接口提供了所有预定义事件的事件名称常量。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

名称类型可读可写说明USER_LOGINstring是否用户登录事件。USER_LOGOUTstring是否用户登出事件。DISTRIBUTED_SERVICE_STARTstring是否分布式服务启动事件。

#### Param

此接口提供了所有预定义参数的参数名称常量。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

名称类型可读可写说明USER_IDstring是否用户自定义ID。DISTRIBUTED_SERVICE_NAMEstring是否分布式服务名称。DISTRIBUTED_SERVICE_INSTANCE_IDstring是否分布式服务实例ID。