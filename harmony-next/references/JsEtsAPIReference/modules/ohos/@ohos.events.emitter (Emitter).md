# @ohos.events.emitter (Emitter)

本模块提供了在同一进程不同线程间或同一线程内发送和处理事件的能力，支持持续订阅事件、单次订阅事件、取消订阅事件及发送事件到事件队列。

本模块首批接口从API version 7开始支持。后续版本新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { emitter } from '@kit.BasicServicesKit';
```

#### emitter.on

on(event: InnerEvent, callback: Callback<EventData>): void

持续订阅指定的事件，并在接收到该事件时，执行对应的回调处理函数。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

系统能力：SystemCapability.Notification.Emitter

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | InnerEvent | 是 | 持续订阅的事件，其中EventPriority，在订阅事件时无需指定，也不生效。 |
| callback | Callback<EventData> | 是 | 接收到该事件时需要执行的回调处理函数。 |

**示例：**

```ets
import { Callback } from '@kit.BasicServicesKit';

let innerEvent: emitter.InnerEvent = {
  eventId: 1
};

let callback: Callback<emitter.EventData> = (eventData: emitter.EventData) => {
  console.info(`eventData: ${JSON.stringify(eventData)}`);
}

// 收到eventId为1的事件后执行回调函数
emitter.on(innerEvent, callback);
```

#### emitter.on11+

on(eventId: string, callback: Callback<EventData>): void

持续订阅指定的事件，并在接收到该事件时，执行对应的回调处理函数。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

系统能力：SystemCapability.Notification.Emitter

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| eventId | string | 是 | 持续订阅的事件。取值为长度不超过10240字节的自定义字符串，且不可为空字符。 |
| callback | Callback<EventData> | 是 | 接收到该事件时需要执行的回调处理函数。 |

**示例：**

```ets
import { Callback } from '@kit.BasicServicesKit';

let callback: Callback<emitter.EventData> = (eventData: emitter.EventData) => {
  console.info(`eventData: ${JSON.stringify(eventData)}`);
}
// 收到eventId为"eventId"的事件后执行回调函数
emitter.on(`eventId`, callback);
```

#### emitter.on12+

on<T>(eventId: string, callback: Callback<GenericEventData<T>>): void

持续订阅指定的事件，并在接收到该事件时，执行对应的回调处理函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

系统能力：SystemCapability.Notification.Emitter

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| eventId | string | 是 | 持续订阅的事件。取值为长度不超过10240字节的自定义字符串，且不可为空字符。 |
| callback | Callback<GenericEventData<T>> | 是 | 接收到该事件时需要执行的回调处理函数。 |

**示例：**

```ets
import { Callback } from '@kit.BasicServicesKit';

@Sendable
class Sample {
  constructor() {
    this.count = 100;
  }
  printCount() {
    console.info('Print count : ' + this.count);
  }
  count: number;
}

let callback: Callback<emitter.GenericEventData<Sample>> = (eventData: emitter.GenericEventData<Sample>): void => {
  console.info(`eventData: ${JSON.stringify(eventData?.data)}`);
  if (eventData?.data instanceof Sample) {
    eventData?.data?.printCount();
  }
// 收到eventId为"eventId"的事件后执行回调函数
emitter.on("eventId", callback);
```

#### emitter.once

once(event: InnerEvent, callback: Callback<EventData>): void

单次订阅指定的事件，在接收到该事件且执行完对应的回调函数后，自动取消订阅。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

系统能力：SystemCapability.Notification.Emitter

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | InnerEvent | 是 | 单次订阅的事件，其中EventPriority，在订阅事件时无需指定，也不生效。 |
| callback | Callback<EventData> | 是 | 接收到该事件时需要执行的回调处理函数。 |

**示例：**

```ets
import { Callback } from '@kit.BasicServicesKit';

let innerEvent: emitter.InnerEvent = {
  eventId: 1
};

let callback: Callback<emitter.EventData> = (eventData: emitter.EventData) => {
  console.info(`eventData: ${JSON.stringify(eventData)}`);
}
// 收到eventId为1的事件后执行该回调函数
emitter.once(innerEvent, callback);
```

#### emitter.once11+

once(eventId: string, callback: Callback<EventData>): void

单次订阅指定的事件，在接收到该事件且执行完对应的回调函数后，自动取消订阅。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

系统能力：SystemCapability.Notification.Emitter

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| eventId | string | 是 | 单次订阅的事件。取值为长度不超过10240字节的自定义字符串，且不可为空字符。 |
| callback | Callback<EventData> | 是 | 接收到该事件时需要执行的回调处理函数。 |

**示例：**

```ets
import { Callback } from '@kit.BasicServicesKit';

let callback: Callback<emitter.EventData> = (eventData: emitter.EventData) => {
  console.info(`eventData: ${JSON.stringify(eventData)}`);
}
// 收到eventId为"eventId"的事件后执行该回调函数
emitter.once("eventId", callback);
```

#### emitter.once12+

once<T>(eventId: string, callback: Callback<GenericEventData<T>>): void

单次订阅指定的事件，在接收到该事件且执行完相应的回调函数后，自动取消订阅。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

系统能力：SystemCapability.Notification.Emitter

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| eventId | string | 是 | 单次订阅的事件。取值为长度不超过10240字节的自定义字符串，且不可为空字符。 |
| callback | Callback<GenericEventData<T>> | 是 | 接收到该事件时需要执行的回调处理函数。 |

**示例：**

```ets
import { Callback } from '@kit.BasicServicesKit';

@Sendable
class Sample {
  constructor() {
    this.count = 100;
  }
  printCount() {
    console.info('Print count : ' + this.count);
  }
  count: number;
}

let callback: Callback<emitter.GenericEventData<Sample>> = (eventData: emitter.GenericEventData<Sample>): void => {
  console.info(`eventData: ${JSON.stringify(eventData?.data)}`);
  if (eventData?.data instanceof Sample) {
    eventData?.data?.printCount();
  }
// 收到eventId为"eventId"的事件后执行回调函数
emitter.once("eventId", callback);
```

#### emitter.off

off(eventId: number): void

取消事件ID为eventId的所有订阅。

使用该接口取消某个事件订阅后，已通过[emit](#ZH-CN_TOPIC_0000002522081600__emitteremit)接口发布但尚未被执行的事件将被取消。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

系统能力：SystemCapability.Notification.Emitter

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| eventId | number | 是 | 事件ID。 |

**示例：**

```ets
// 取消eventID为1的所有事件回调处理函数
emitter.off(1);
```

#### emitter.off11+

off(eventId: string): void

取消事件ID为eventId的所有订阅。

使用该接口取消某个事件订阅后，已通过[emit](#ZH-CN_TOPIC_0000002522081600__emitteremit11)接口发布但尚未被执行的事件将被取消。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

系统能力：SystemCapability.Notification.Emitter

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| eventId | string | 是 | 事件ID。取值为长度不超过10240字节的自定义字符串，且不可为空字符。 |

**示例：**

```ets
// 取消eventID为"eventId"的所有事件回调处理函数
emitter.off("eventId");
```

#### emitter.off10+

off(eventId: number, callback: Callback<EventData>): void

取消事件ID为eventId且回调处理函数为callback的订阅。仅当已使用[on](#ZH-CN_TOPIC_0000002522081600__emitteron)或[once](#ZH-CN_TOPIC_0000002522081600__emitteronce)接口订阅callback时，该接口才生效。

使用该接口取消某个事件订阅后，已通过[emit](#ZH-CN_TOPIC_0000002522081600__emitteremit)接口发布但尚未被执行的事件将被取消。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

系统能力：SystemCapability.Notification.Emitter

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| eventId | number | 是 | 事件ID。 |
| callback | Callback<EventData> | 是 | 事件的回调处理函数。 |

**示例：**

```ets
import { Callback } from '@kit.BasicServicesKit';

let callback: Callback<emitter.EventData> = (eventData: emitter.EventData) => {
  console.info(`eventData: ${JSON.stringify(eventData)}`);
}
// 取消eventID为1的事件回调处理函数，callback对象应使用订阅时的对象
// 如果该回调处理函数没有被订阅，则不做任何处理
emitter.off(1, callback);
```

#### emitter.off11+

off(eventId: string, callback: Callback<EventData>): void

取消事件ID为eventId且回调处理函数为callback的订阅。仅当已使用[on](#ZH-CN_TOPIC_0000002522081600__emitteron11)或[once](#ZH-CN_TOPIC_0000002522081600__emitteronce11)接口订阅callback时，该接口才生效。

使用该接口取消某个事件订阅后，已通过[emit](#ZH-CN_TOPIC_0000002522081600__emitteremit11)接口发布但尚未被执行的事件将被取消。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

系统能力：SystemCapability.Notification.Emitter

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| eventId | string | 是 | 事件ID。取值为长度不超过10240字节的自定义字符串，且不可为空字符。 |
| callback | Callback<EventData> | 是 | 事件的回调处理函数。 |

**示例：**

```ets
import { Callback } from '@kit.BasicServicesKit';

let callback: Callback<emitter.EventData> = (eventData: emitter.EventData) => {
  console.info(`eventData: ${JSON.stringify(eventData)}`);
}
// 取消eventID为"eventId"的事件回调处理函数，callback对象应使用订阅时的对象
// 如果该回调处理函数没有被订阅，则不做任何处理
emitter.off("eventId", callback);
```

#### emitter.off12+

off<T>(eventId: string, callback: Callback<GenericEventData<T>>): void

取消事件ID为eventId且回调处理函数为callback的订阅。仅当已使用[on](#ZH-CN_TOPIC_0000002522081600__emitteron12)或[once](#ZH-CN_TOPIC_0000002522081600__emitteronce12)接口订阅callback时，该接口才生效。

使用该接口取消某个事件订阅后，已通过[emit](#ZH-CN_TOPIC_0000002522081600__emitteremit12)接口发布但尚未被执行的事件将被取消。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

系统能力：SystemCapability.Notification.Emitter

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| eventId | string | 是 | 事件ID。取值为长度不超过10240字节的自定义字符串，且不可为空字符。 |
| callback | Callback<GenericEventData<T>> | 是 | 事件的回调处理函数。 |

**示例：**

```ets
import { Callback } from '@kit.BasicServicesKit';

@Sendable
class Sample {
  constructor() {
    this.count = 100;
  }
  printCount() {
    console.info('Print count : ' + this.count);
  }
  count: number;
}

let callback: Callback<emitter.GenericEventData<Sample>> = (eventData: emitter.GenericEventData<Sample>): void => {
  console.info(`eventData: ${JSON.stringify(eventData?.data)}`);
  if (eventData?.data instanceof Sample) {
    eventData?.data?.printCount();
  }
// 取消eventID为"eventId"的事件回调处理函数，callback对象应使用订阅时的对象
// 如果该回调处理函数没有被订阅，则不做任何处理
emitter.off("eventId", callback);
```

#### emitter.emit

emit(event: InnerEvent, data?: EventData): void

发送指定事件。

该接口支持跨线程传输数据对象，需要遵循数据跨线程传输的规格约束，详见[线程间通信对象](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/serializable-overview)。目前不支持使用[@State装饰器](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-state)、[@Observed装饰器](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-observed-and-objectlink)等装饰器修饰的复杂类型数据。

该接口发布某个事件后，不保证该事件立刻执行，执行时间取决于事件队列里面的事件数量以及各事件的执行效率。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

系统能力：SystemCapability.Notification.Emitter

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | InnerEvent | 是 | 发送的事件，其中EventPriority用于指定事件被发送的优先级。 |
| data | EventData | 否 | 事件携带的数据。 |

**示例：**

```ets
let eventData: emitter.EventData = {
  data: {
    "content": "content",
    "id": 1,
  }
};

let innerEvent: emitter.InnerEvent = {
  eventId: 1,
  priority: emitter.EventPriority.HIGH
};

emitter.emit(innerEvent, eventData);
```

#### emitter.emit11+

emit(eventId: string, data?: EventData): void

发送指定事件。

该接口支持跨线程传输数据对象，需要遵循数据跨线程传输的规格约束，详见[线程间通信对象](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/serializable-overview)。目前不支持使用[@State装饰器](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-state)、[@Observed装饰器](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-observed-and-objectlink)等装饰器修饰的复杂类型数据。

该接口发布某个事件后，不保证该事件立刻执行，执行时间取决于事件队列里面的事件数量以及各事件的执行效率。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

系统能力：SystemCapability.Notification.Emitter

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| eventId | string | 是 | 发送的事件ID。取值为长度不超过10240字节的自定义字符串，且不可为空字符。 |
| data | EventData | 否 | 事件携带的数据。 |

**示例：**

```ets
let eventData: emitter.EventData = {
  data: {
  "content": "content",
  "id": 1,
  }
};

emitter.emit("eventId", eventData);
```

#### emitter.emit12+

emit<T>(eventId: string, data?: GenericEventData<T>): void

发送指定事件。

该接口支持跨线程传输数据对象，需要遵循数据跨线程传输的规格约束，详见[线程间通信对象](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/serializable-overview)。目前不支持使用[@State装饰器](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-state)、[@Observed装饰器](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-observed-and-objectlink)等装饰器修饰的复杂类型数据。

该接口发布某个事件后，不保证该事件立刻执行，执行时间取决于事件队列里面的事件数量以及各事件的执行效率。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

系统能力：SystemCapability.Notification.Emitter

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| eventId | string | 是 | 发送的事件ID。取值为长度不超过10240字节的自定义字符串，且不可为空字符。 |
| data | GenericEventData<T> | 否 | 事件携带的数据。 |

**示例：**

```ets
@Sendable
class Sample {
  constructor() {
    this.count = 100;
  }
  printCount() {
    console.info('Print count : ' + this.count);
  }
  count: number;
}

let eventData: emitter.GenericEventData<Sample> = {
  data: new Sample()
};
emitter.emit("eventId", eventData);
```

#### emitter.emit11+

emit(eventId: string, options: Options, data?: EventData): void

发送指定优先级事件。

该接口支持跨线程传输数据对象，需要遵循数据跨线程传输的规格约束，详见[线程间通信对象](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/serializable-overview)。目前不支持使用[@State装饰器](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-state)、[@Observed装饰器](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-observed-and-objectlink)等装饰器修饰的复杂类型数据。

该接口发布某个事件后，不保证该事件立刻执行，执行时间取决于事件队列里面的事件数量以及各事件的执行效率。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

系统能力：SystemCapability.Notification.Emitter

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| eventId | string | 是 | 发送的事件ID。取值为长度不超过10240字节的自定义字符串，且不可为空字符。 |
| options | Options | 是 | 事件优先级。 |
| data | EventData | 否 | 事件携带的数据。 |

**示例：**

```ets
let eventData: emitter.EventData = {
  data: {
    "content": "content",
    "id": 1,
  }
};

let options: emitter.Options = {
  priority: emitter.EventPriority.HIGH
};

emitter.emit("eventId", options, eventData);
```

#### emitter.emit12+

emit<T>(eventId: string, options: Options, data?: GenericEventData<T>): void

发送指定优先级事件。

该接口支持跨线程传输数据对象，需要遵循数据跨线程传输的规格约束，详见[线程间通信对象](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/serializable-overview)。目前不支持使用[@State装饰器](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-state)、[@Observed装饰器](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-observed-and-objectlink)等装饰器修饰的复杂类型数据。

该接口发布某个事件后，不保证该事件立刻执行，执行时间取决于事件队列里面的事件数量以及各事件的执行效率。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

系统能力：SystemCapability.Notification.Emitter

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| eventId | string | 是 | 发送的事件ID。取值为长度不超过10240字节的自定义字符串，且不可为空字符。 |
| options | Options | 是 | 事件优先级。 |
| data | GenericEventData<T> | 否 | 事件携带的数据。 |

**示例：**

```ets
@Sendable
class Sample {
  constructor() {
    this.count = 100;
  }
  printCount() {
    console.info('Print count : ' + this.count);
  }
  count: number;
}

let options: emitter.Options = {
  priority: emitter.EventPriority.HIGH
};
let eventData: emitter.GenericEventData<Sample> = {
  data: new Sample()
};

emitter.emit("eventId", options, eventData);
```

#### emitter.getListenerCount11+

getListenerCount(eventId: number | string): number

获取指定事件的订阅数。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

系统能力：SystemCapability.Notification.Emitter

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| eventId | number | string | 是 | 事件ID，string类型的eventId取值为长度不超过10240字节的自定义字符串，且不可为空字符。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 指定事件的订阅数。 |

**示例：**

```ets
let count: number = emitter.getListenerCount("eventId");
```

#### EventPriority

表示事件的优先级。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Notification.Emitter

| 名称 | 值 | 说明 |
| --- | --- | --- |
| IMMEDIATE | 0 | 表示事件先于HIGH优先级投递。 |
| HIGH | 1 | 表示事件先于LOW优先级投递。 |
| LOW | 2 | 表示事件优于IDLE优先级投递，事件的默认优先级是LOW。 |
| IDLE | 3 | 表示在没有其他事件的情况下，才投递该事件。 |

#### InnerEvent

订阅或发送的事件，订阅事件时EventPriority不生效。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

系统能力：SystemCapability.Notification.Emitter

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| eventId | number | 否 | 否 | 事件ID，由开发者定义，用于辨别事件。 |
| priority | EventPriority | 否 | 是 | 事件的优先级，默认值为EventPriority.LOW。 |

#### EventData

发送事件时传递的数据。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

系统能力：SystemCapability.Notification.Emitter

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| data | { [key: string]: any } | 否 | 是 | 发送事件时传递的数据，支持数据类型包括Array、ArrayBuffer、Boolean、DataView、Date、Error、Map、Number、Object、Primitive（除了symbol）、RegExp、Set、String、TypedArray，数据大小最大为16M。 |

#### Options11+

发送事件的优先级。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

系统能力：SystemCapability.Notification.Emitter

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| priority | EventPriority | 否 | 是 | 事件的优先级，默认值为EventPriority.LOW。 |

#### GenericEventData<T>12+

发送事件时传递的泛型数据。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

系统能力：SystemCapability.Notification.Emitter

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| data | T | 否 | 是 | 发送事件时传递的数据。T：泛型类型。 |

#### Emitter22+

该功能支持在同一进程的同一Emitter类实例中，跨不同线程或同一线程内发送和处理事件。它能够实现持续订阅事件、单次订阅事件、取消订阅事件以及将事件发送到事件队列。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.Emitter

#### constructor22+

constructor()

构造函数。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.Emitter

**示例：**

```ets
let emitter1: emitter.Emitter = new emitter.Emitter();
```

#### on22+

on(eventId: string, callback: Callback<EventData>): void

持续订阅当前Emitter类实例指定的事件，并在接收到该事件时，使用callback异步回调。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

系统能力：SystemCapability.Notification.Emitter

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| eventId | string | 是 | 持续订阅的事件。取值为长度不超过10240字节的自定义字符串，且不可为空字符。 |
| callback | Callback<EventData> | 是 | 回调函数，在接收到该事件时被调用。 |

**示例：**

```ets
import { Callback } from '@kit.BasicServicesKit';

let emitter1: emitter.Emitter = new emitter.Emitter();

let callback: Callback<emitter.EventData> = (eventData: emitter.EventData) => {
  console.info(`eventData: ${JSON.stringify(eventData)}`);
}

emitter1.on(`eventId`, callback);
```

#### on22+

on<T>(eventId: string, callback: Callback<GenericEventData<T>>): void

持续订阅当前Emitter类实例指定的事件，并在接收到该事件时，使用callback异步回调。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

系统能力：SystemCapability.Notification.Emitter

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| eventId | string | 是 | 持续订阅的事件。取值为长度不超过10240字节的自定义字符串，且不可为空字符。 |
| callback | Callback<GenericEventData<T>> | 是 | 回调函数，在接收到该事件时被调用。 |

**示例：**

```ets
import { Callback } from '@kit.BasicServicesKit';

let emitter1: emitter.Emitter = new emitter.Emitter();

@Sendable
class Sample {
  constructor() {
    this.count = 100;
  }
  printCount() {
    console.info('Print count : ' + this.count);
  }
  count: number;
}

let callback: Callback<emitter.GenericEventData<Sample>> = (eventData: emitter.GenericEventData<Sample>): void => {
  console.info(`eventData: ${JSON.stringify(eventData?.data)}`);
  if (eventData?.data instanceof Sample) {
    eventData?.data?.printCount();
  }

emitter1.on("eventId", callback);
```

#### once22+

once(eventId: string, callback: Callback<EventData>): void

单次订阅当前Emitter类实例指定的事件，在接收到该事件且执行完对应的回调函数后，自动取消订阅。使用callback异步回调。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

系统能力：SystemCapability.Notification.Emitter

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| eventId | string | 是 | 单次订阅的事件。取值为长度不超过10240字节的自定义字符串，且不可为空字符。 |
| callback | Callback<EventData> | 是 | 回调函数，在接收到该事件时被调用。 |

**示例：**

```ets
import { Callback } from '@kit.BasicServicesKit';

let emitter1: emitter.Emitter = new emitter.Emitter();

let callback: Callback<emitter.EventData> = (eventData: emitter.EventData) => {
  console.info(`eventData: ${JSON.stringify(eventData)}`);
}

emitter1.once("eventId", callback);
```

#### once22+

once<T>(eventId: string, callback: Callback<GenericEventData<T>>): void

单次订阅当前Emitter类实例指定的事件，在接收到该事件且执行完相应的回调函数后，自动取消订阅。使用callback异步回调。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

系统能力：SystemCapability.Notification.Emitter

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| eventId | string | 是 | 单次订阅的事件。取值为长度不超过10240字节的自定义字符串，且不可为空字符。 |
| callback | Callback<GenericEventData<T>> | 是 | 回调函数，在接收到该事件时被调用。 |

**示例：**

```ets
import { Callback } from '@kit.BasicServicesKit';

let emitter1: emitter.Emitter = new emitter.Emitter();

@Sendable
class Sample {
  constructor() {
    this.count = 100;
  }
  printCount() {
    console.info('Print count : ' + this.count);
  }
  count: number;
}

let callback: Callback<emitter.GenericEventData<Sample>> = (eventData: emitter.GenericEventData<Sample>): void => {
  console.info(`eventData: ${JSON.stringify(eventData?.data)}`);
  if (eventData?.data instanceof Sample) {
    eventData?.data?.printCount();
  }

emitter1.once("eventId", callback);
```

#### off22+

off(eventId: string): void

取消当前Emitter类实例事件ID为eventId的所有订阅。

使用该接口取消某个事件订阅后，已通过[emit](#ZH-CN_TOPIC_0000002522081600__emit22)接口发布但尚未被执行的事件将被取消。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

系统能力：SystemCapability.Notification.Emitter

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| eventId | string | 是 | 事件ID。取值为长度不超过10240字节的自定义字符串，且不可为空字符。 |

**示例：**

```ets
let emitter1: emitter.Emitter = new emitter.Emitter();

emitter1.off("eventId");
```

#### off22+

off(eventId: string, callback: Callback<EventData>): void

取消订阅当前Emitter类实例的事件。仅当已使用[on](#ZH-CN_TOPIC_0000002522081600__on22)或[once](#ZH-CN_TOPIC_0000002522081600__once22)接口订阅了事件ID为eventId且回调处理函数为callback的事件时，该接口才生效。

使用该接口取消事件订阅后，已通过[emit](#ZH-CN_TOPIC_0000002522081600__emit22)接口发布但尚未执行的事件将被取消。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

系统能力：SystemCapability.Notification.Emitter

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| eventId | string | 是 | 事件ID。取值为长度不超过10240字节的自定义字符串，且不可为空字符。 |
| callback | Callback<EventData> | 是 | 回调函数，指定要取消订阅的事件处理函数。 |

**示例：**

```ets
import { Callback } from '@kit.BasicServicesKit';

let emitter1: emitter.Emitter = new emitter.Emitter();

let callback: Callback<emitter.EventData> = (eventData: emitter.EventData) => {
  console.info(`eventData: ${JSON.stringify(eventData)}`);
}

emitter1.off("eventId", callback);
```

#### off22+

off<T>(eventId: string, callback: Callback<GenericEventData<T>>): void

取消订阅当前Emitter类实例的事件。仅当已使用[on](#ZH-CN_TOPIC_0000002522081600__on22-1)或[once](#ZH-CN_TOPIC_0000002522081600__once22-1)接口订阅了事件ID为eventId且回调处理函数为callback的事件时，该接口才生效。

使用该接口取消事件订阅后，已通过[emit](#ZH-CN_TOPIC_0000002522081600__emit22-1)接口发布但尚未执行的事件将被取消。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

系统能力：SystemCapability.Notification.Emitter

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| eventId | string | 是 | 事件ID。取值为长度不超过10240字节的自定义字符串，且不可为空字符。 |
| callback | Callback<GenericEventData<T>> | 是 | 回调函数，指定要取消订阅的事件处理函数。 |

**示例：**

```ets
import { Callback } from '@kit.BasicServicesKit';

@Sendable
class Sample {
  constructor() {
    this.count = 100;
  }
  printCount() {
    console.info('Print count : ' + this.count);
  }
  count: number;
}

let emitter1: emitter.Emitter = new emitter.Emitter();

let callback: Callback<emitter.GenericEventData<Sample>> = (eventData: emitter.GenericEventData<Sample>): void => {
  console.info(`eventData: ${JSON.stringify(eventData?.data)}`);
  if (eventData?.data instanceof Sample) {
    eventData?.data?.printCount();
}

emitter1.off("eventId", callback);
```

#### emit22+

emit(eventId: string, data?: EventData): void

发送指定事件到当前Emitter类实例。

该接口支持跨线程传输数据对象，需要遵循数据跨线程传输的规格约束，详见[线程间通信对象](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/serializable-overview)。目前不支持使用[@State装饰器](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-state)、[@Observed装饰器](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-observed-and-objectlink)等装饰器修饰的复杂类型数据。

该接口发布某个事件后，不保证该事件立刻执行，执行时间取决于事件队列里面的事件数量以及各事件的执行效率。

**元服务API：** 从API version 22开始支持元服务。

系统能力：SystemCapability.Notification.Emitter

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| eventId | string | 是 | 发送的事件ID。取值为长度不超过10240字节的自定义字符串，且不可为空字符。 |
| data | EventData | 否 | 事件携带的数据。 |

**示例：**

```ets
let emitter1: emitter.Emitter = new emitter.Emitter();
let eventData: emitter.EventData = {
  data: {
  "content": "content",
  "id": 1,
  }
};

emitter1.emit("eventId", eventData);
```

#### emit22+

emit<T>(eventId: string, data?: GenericEventData<T>): void

发送指定事件到当前Emitter类实例。

该接口支持跨线程传输数据对象，需要遵循数据跨线程传输的规格约束，详见[线程间通信对象](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/serializable-overview)。目前不支持使用[@State装饰器](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-state)、[@Observed装饰器](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-observed-and-objectlink)等装饰器修饰的复杂类型数据。

该接口发布某个事件后，不保证该事件立刻执行，执行时间取决于事件队列里面的事件数量以及各事件的执行效率。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

系统能力：SystemCapability.Notification.Emitter

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| eventId | string | 是 | 发送的事件ID。取值为长度不超过10240字节的自定义字符串，且不可为空字符。 |
| data | GenericEventData<T> | 否 | 事件携带的数据。 |

**示例：**

```ets
@Sendable
class Sample {
  constructor() {
    this.count = 100;
  }
  printCount() {
    console.info('Print count : ' + this.count);
  }
  count: number;
}

let emitter1: emitter.Emitter = new emitter.Emitter();

let eventData: emitter.GenericEventData<Sample> = {
  data: new Sample()
};

emitter1.emit("eventId", eventData);
```

**emit22+**

emit(eventId: string, options: Options, data?: EventData): void

发送指定事件到当前Emitter类实例。

该接口支持跨线程传输数据对象，需要遵循数据跨线程传输的规格约束，详见[线程间通信对象](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/serializable-overview)。目前不支持使用[@State装饰器](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-state)、[@Observed装饰器](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-observed-and-objectlink)等装饰器修饰的复杂类型数据。

该接口发布某个事件后，不保证该事件立刻执行，执行时间取决于事件队列里面的事件数量以及各事件的执行效率。

元服务API： 从API version 22开始支持元服务。

系统能力：SystemCapability.Notification.Emitter

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| eventId | string | 是 | 发送的事件ID。取值为长度不超过10240字节的自定义字符串，且不可为空字符。 |
| options | Options | 是 | 事件优先级。 |
| data | EventData | 否 | 事件携带的数据。 |

示例：

```ets
let emitter1: emitter.Emitter = new emitter.Emitter();

let options: emitter.Options = {
  priority: emitter.EventPriority.HIGH
};
let eventData: emitter.EventData = {
  data: {
  "content": "content",
  "id": 1,
  }
};

emitter1.emit("eventId", options, eventData);
```

#### emit22+

emit<T>(eventId: string, options: Options, data?: GenericEventData<T>): void

发送指定优先级事件到当前Emitter类实例。

该接口支持跨线程传输数据对象，需要遵循数据跨线程传输的规格约束，详见[线程间通信对象](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/serializable-overview)。目前不支持使用[@State装饰器](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-state)、[@Observed装饰器](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-observed-and-objectlink)等装饰器修饰的复杂类型数据。

该接口发布某个事件后，不保证该事件立刻执行，执行时间取决于事件队列里面的事件数量以及各事件的执行效率。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

系统能力：SystemCapability.Notification.Emitter

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| eventId | string | 是 | 发送的事件ID。取值为长度不超过10240字节的自定义字符串，且不可为空字符。 |
| options | Options | 是 | 事件优先级。 |
| data | GenericEventData<T> | 否 | 事件携带的数据。 |

**示例：**

```ets
@Sendable
class Sample {
  constructor() {
    this.count = 100;
  }
  printCount() {
    console.info('Print count : ' + this.count);
  }
  count: number;
}

let emitter1: emitter.Emitter = new emitter.Emitter();

let options: emitter.Options = {
  priority: emitter.EventPriority.HIGH
};
let eventData: emitter.GenericEventData<Sample> = {
  data: new Sample()
};

emitter1.emit("eventId", options, eventData);
```

#### getListenerCount22+

getListenerCount(eventId: string): number

获取当前Emitter类实例指定事件的订阅数。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

系统能力：SystemCapability.Notification.Emitter

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| eventId | string | 是 | 事件ID，取值为长度不超过10240字节的自定义字符串，且不可为空字符。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 指定事件的订阅数。 |

**示例：**

```ets
let emitter1: emitter.Emitter = new emitter.Emitter();
let count = emitter1.getListenerCount("eventId");
```