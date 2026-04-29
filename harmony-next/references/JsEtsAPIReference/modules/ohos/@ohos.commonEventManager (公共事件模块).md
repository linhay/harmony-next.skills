# @ohos.commonEventManager (公共事件模块)

本模块提供了公共事件相关的能力，包括发布公共事件、订阅公共事件、以及退订公共事件。

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { commonEventManager } from '@kit.BasicServicesKit';
```

#### Support

系统公共事件是指由系统服务或系统应用发布的事件，订阅这些公共事件需要特定的权限、使用相应的值，详见[系统定义的公共事件]([系统定义的公共事件](../../topics/misc/系统定义的公共事件.md).md)。

#### commonEventManager.publish

publish(event: string, callback: AsyncCallback<void>): void

发布公共事件。使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | 表示要发送的公共事件。详见[系统公共事件定义](../../topics/misc/系统定义的公共事件.md)。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当公共事件发布成功时，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码]([通用错误码](../../errors/通用错误码.md).md)和[事件错误码]([事件错误码](../../errors/事件错误码.md).md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1500003 | The common event sending frequency too high. |
| 1500007 | Failed to send the message to the common event service. |
| 1500008 | Failed to initialize the common event service. |
| 1500009 | Failed to obtain system parameters. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

// 发布公共事件
try {
  commonEventManager.publish('event', (err: BusinessError) => {
    if (err) {
      console.error(`Failed to publish common event. Code is ${err.code}, message is ${err.message}`);
      return;
    }
    console.info(`Succeeded in publishing common event.`);
  });
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(`Failed to publish common event. Code is ${err.code}, message is ${err.message}`);
}
```

#### commonEventManager.publish

publish(event: string, options: [CommonEventPublishData](../../topics/misc/CommonEventPublishData.md), callback: AsyncCallback<void>): void

发布公共事件。使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | 表示要发布的公共事件。详见[系统公共事件定义](../../topics/misc/系统定义的公共事件.md)。 |
| options | [CommonEventPublishData](../../topics/misc/CommonEventPublishData.md) | 是 | 表示发布公共事件的属性。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当公共事件发布成功时，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[事件错误码](事件错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1500003 | The common event sending frequency too high. |
| 1500007 | Failed to send the message to the common event service. |
| 1500008 | Failed to initialize the common event service. |
| 1500009 | Failed to obtain system parameters. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

// 公共事件相关信息，以发布有序公共事件为例
let options: commonEventManager.CommonEventPublishData = {
  code: 0,
  data: 'initial data',
  isOrdered: true // 有序公共事件
}

// 发布公共事件
try {
  commonEventManager.publish('event', options, (err: BusinessError) => {
    if (err) {
      console.error(`Failed to publish common event. Code is ${err.code}, message is ${err.message}`);
      return;
    }
    console.info(`Succeeded in publishing common event.`);
  });
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(`Failed to publish common event. Code is ${err.code}, message is ${err.message}`);
}
```

#### commonEventManager.createSubscriber

createSubscriber(subscribeInfo: [CommonEventSubscribeInfo](../../topics/misc/CommonEventSubscribeInfo.md), callback: AsyncCallback<CommonEventSubscriber>): void

创建订阅者。使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| subscribeInfo | [CommonEventSubscribeInfo](../../topics/misc/CommonEventSubscribeInfo.md) | 是 | 表示订阅信息。 |
| callback | AsyncCallback<[CommonEventSubscriber](../../topics/misc/commonEventSubscriber.md#ZH-CN_TOPIC_0000002529285505__commoneventsubscriber-1)> | 是 | 回调函数。当公共事件订阅者创建成功时，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

// 定义订阅者，用于保存创建成功的订阅者对象，后续使用其完成订阅及退订的动作
let subscriber: commonEventManager.CommonEventSubscriber | null = null;
// 订阅者信息
let subscribeInfo: commonEventManager.CommonEventSubscribeInfo = {
  events: ['event']
};

// 创建订阅者
try {
  commonEventManager.createSubscriber(subscribeInfo,
    (err: BusinessError, commonEventSubscriber: commonEventManager.CommonEventSubscriber) => {
      if(!err) {
        console.info(`Succeeded in creating subscriber.`);
        subscriber = commonEventSubscriber;
        return;
      }
      console.error(`Failed to create subscriber. Code is ${err.code}, message is ${err.message}`);
    });
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(`Failed to create subscriber. Code is ${err.code}, message is ${err.message}`);
}
```

#### commonEventManager.createSubscriber

createSubscriber(subscribeInfo: [CommonEventSubscribeInfo](../../topics/misc/CommonEventSubscribeInfo.md)): Promise<CommonEventSubscriber>

创建订阅者。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| subscribeInfo | [CommonEventSubscribeInfo](../../topics/misc/CommonEventSubscribeInfo.md) | 是 | 表示订阅信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[CommonEventSubscriber](../../topics/misc/commonEventSubscriber.md#ZH-CN_TOPIC_0000002529285505__commoneventsubscriber-1)> | Promise对象，返回创建成功的订阅者对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

// 定义订阅者，用于保存创建成功的订阅者对象，后续使用其完成订阅及退订的动作
let subscriber: commonEventManager.CommonEventSubscriber | null = null;
// 订阅者信息
let subscribeInfo: commonEventManager.CommonEventSubscribeInfo = {
  events: ['event']
};
// 创建订阅者
commonEventManager.createSubscriber(subscribeInfo).then((commonEventSubscriber: commonEventManager.CommonEventSubscriber) => {
  console.info(`Succeeded in creating subscriber.`);
  subscriber = commonEventSubscriber;
}).catch((err: BusinessError) => {
  console.error(`Failed to create subscriber. Code is ${err.code}, message is ${err.message}`);
});
```

#### commonEventManager.createSubscriberSync10+

createSubscriberSync(subscribeInfo: [CommonEventSubscribeInfo](../../topics/misc/CommonEventSubscribeInfo.md)): CommonEventSubscriber

createSubscriber的同步接口。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| subscribeInfo | [CommonEventSubscribeInfo](../../topics/misc/CommonEventSubscribeInfo.md) | 是 | 表示订阅信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [CommonEventSubscriber](../../topics/misc/commonEventSubscriber.md#ZH-CN_TOPIC_0000002529285505__commoneventsubscriber-1) | 返回订阅者对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

// 定义订阅者，用于保存创建成功的订阅者对象，后续使用其完成订阅及退订的动作
let subscriber: commonEventManager.CommonEventSubscriber | null = null;
// 订阅者信息
let subscribeInfo: commonEventManager.CommonEventSubscribeInfo = {
  events: ['event']
};
// 创建订阅者
try {
  subscriber = commonEventManager.createSubscriberSync(subscribeInfo);
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(`Failed to create subscriber. Code is ${err.code}, message is ${err.message}`);
}
```

#### commonEventManager.subscribe

subscribe(subscriber: [CommonEventSubscriber](../../topics/misc/commonEventSubscriber.md#ZH-CN_TOPIC_0000002529285505__commoneventsubscriber-1), callback: AsyncCallback<CommonEventData>): void

订阅公共事件。使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| subscriber | [CommonEventSubscriber](../../topics/misc/commonEventSubscriber.md#ZH-CN_TOPIC_0000002529285505__commoneventsubscriber-1) | 是 | 表示订阅者对象。 |
| callback | AsyncCallback<[CommonEventData](../../topics/misc/CommonEventData.md)> | 是 | 回调函数。当公共事件订阅成功后，事件触发时执行的回调函数；否则订阅失败时，err为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[事件错误码](事件错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | capability not supported. |
| 1500007 | Failed to send the message to the common event service. |
| 1500008 | Failed to initialize the common event service. |
| 1500010 | The count of subscriber exceed system specification. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

// 定义订阅者，用于保存创建成功的订阅者对象，后续使用其完成订阅及退订的动作
let subscriber: commonEventManager.CommonEventSubscriber | null = null;
// 订阅者信息
let subscribeInfo: commonEventManager.CommonEventSubscribeInfo = {
  events: ['event']
};

// 创建订阅者
try {
  commonEventManager.createSubscriber(subscribeInfo,
    (err: BusinessError, commonEventSubscriber: commonEventManager.CommonEventSubscriber) => {
      if(!err) {
        console.info(`Succeeded in creating subscriber.`);
        subscriber = commonEventSubscriber;
        // 订阅公共事件
        try {
          commonEventManager.subscribe(subscriber, (err: BusinessError, data: commonEventManager.CommonEventData) => {
            if (err) {
              console.error(`Failed to subscribe. Code is ${err.code}, message is ${err.message}`);
              return;
            }
            console.info(`Succeeded in subscribing, data is ${JSON.stringify(data)}`);
          });
        } catch (error) {
          let err: BusinessError = error as BusinessError;
          console.error(`Failed to subscribe. Code is ${err.code}, message is ${err.message}`);
        }
        return;
      }
      console.error(`Failed to create subscriber. Code is ${err.code}, message is ${err.message}`);
    });
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(`Failed to create subscriber. Code is ${err.code}, message is ${err.message}`);
}
```

#### commonEventManager.unsubscribe

unsubscribe(subscriber: [CommonEventSubscriber](../../topics/misc/commonEventSubscriber.md#ZH-CN_TOPIC_0000002529285505__commoneventsubscriber-1), callback?: AsyncCallback<void>): void

取消订阅公共事件。使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| subscriber | [CommonEventSubscriber](../../topics/misc/commonEventSubscriber.md#ZH-CN_TOPIC_0000002529285505__commoneventsubscriber-1) | 是 | 表示订阅者对象。 |
| callback | AsyncCallback<void> | 否 | 回调函数。当取消公共事件订阅成功时，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[事件错误码](事件错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | capability not supported. |
| 1500007 | Failed to send the message to the common event service. |
| 1500008 | Failed to initialize the common event service. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

// 定义订阅者，用于保存创建成功的订阅者对象，后续使用其完成订阅及退订的动作
let subscriber: commonEventManager.CommonEventSubscriber | null = null;
// 订阅者信息
let subscribeInfo: commonEventManager.CommonEventSubscribeInfo = {
  events: ['event']
};

// 创建订阅者
try {
  commonEventManager.createSubscriber(subscribeInfo,
    (err: BusinessError, commonEventSubscriber: commonEventManager.CommonEventSubscriber) => {
      if(!err) {
        console.info(`Succeeded in creating subscriber.`);
        subscriber = commonEventSubscriber;
        // 订阅公共事件
        try {
          commonEventManager.subscribe(subscriber, (err: BusinessError, data: commonEventManager.CommonEventData) => {
            if (err) {
              console.error(`Failed to subscribe. Code is ${err.code}, message is ${err.message}`);
              return;
            }
            console.info(`Succeeded in subscribing, data is ${JSON.stringify(data)}`);
          });
        } catch (error) {
          let err: BusinessError = error as BusinessError;
          console.error(`Failed to subscribe. Code is ${err.code}, message is ${err.message}`);
        }
        return;
      }
      console.error(`Failed to create subscriber. Code is ${err.code}, message is ${err.message}`);
    });
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(`Failed to create subscriber. Code is ${err.code}, message is ${err.message}`);
}

// 取消订阅公共事件
// 等待异步接口subscribe执行完毕，开发者根据实际业务选择是否需要添加setTimeout
setTimeout(() => {
  try {
    commonEventManager.unsubscribe(subscriber, (err: BusinessError) => {
      if (err) {
        console.error(`Failed to unsubscribe. Code is ${err.code}, message is ${err.message}`);
        return;
      }
      // subscriber不再使用时需要将其置为undefined，避免内存泄露
      subscriber = undefined;
      console.info(`Succeeded in unsubscribing.`);
    });
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    console.error(`Failed to unsubscribe. Code is ${err.code}, message is ${err.message}`);
  }
}, 500);
```

#### commonEventManager.subscribeToEvent20+

subscribeToEvent(subscriber: [CommonEventSubscriber](../../topics/misc/commonEventSubscriber.md#ZH-CN_TOPIC_0000002529285505__commoneventsubscriber-1), callback: Callback<CommonEventData>): Promise<void>

订阅公共事件，并返回订阅成功或失败信息。使用Promise异步回调。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| subscriber | [CommonEventSubscriber](../../topics/misc/commonEventSubscriber.md#ZH-CN_TOPIC_0000002529285505__commoneventsubscriber-1) | 是 | 表示订阅者对象。 |
| callback | Callback<[CommonEventData](../../topics/misc/CommonEventData.md)> | 是 | 表示接收公共事件数据的回调函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[事件错误码](事件错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |
| 1500007 | Failed to send the message to the common event service. |
| 1500008 | Failed to initialize the common event service. |
| 1500010 | The count of subscriber exceed system specification. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

// 定义订阅者，用于保存创建成功的订阅者对象，后续使用其完成订阅及退订的动作
let subscriber: commonEventManager.CommonEventSubscriber | null = null;
// 订阅者信息
let subscribeInfo: commonEventManager.CommonEventSubscribeInfo = {
  events: ["event"]
};

// 创建订阅者
try {
  commonEventManager.createSubscriber(subscribeInfo,
    (err: BusinessError, commonEventSubscriber: commonEventManager.CommonEventSubscriber) => {
      if (err) {
        console.error(`Failed to create subscriber. Code is ${err.code}, message is ${err.message}`);
      } else {
        console.info(`Succeeded in creating subscriber.`);
        subscriber = commonEventSubscriber;
        // 订阅公共事件
        try {
          commonEventManager.subscribeToEvent(subscriber, (data: commonEventManager.CommonEventData) => {
            console.info(`Succeeded to receive common event, data is ` + JSON.stringify(data));
          }).then(() => {
            console.info(`Succeeded to subscribe.`);
          }).catch((err: BusinessError) => {
            console.error(`Failed to subscribe. Code is ${err.code}, message is ${err.message}`);
          });
        } catch (error) {
          let err: BusinessError = error as BusinessError;
          console.error(`Failed to subscribe. Code is ${err.code}, message is ${err.message}`);
        }
    });
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(`Failed to create subscriber. Code is ${err.code}, message is ${err.message}`);
}
```

#### [CommonEventData](../../topics/misc/CommonEventData.md)10+

type [CommonEventData](../../topics/misc/CommonEventData.md) = [_CommonEventData](../../topics/misc/CommonEventData.md)

表示公共事件的数据。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.CommonEvent

| 类型 | 说明 |
| --- | --- |
| _[CommonEventData](../../topics/misc/CommonEventData.md) | 表示公共事件的数据。 |

#### [CommonEventSubscriber](../../topics/misc/commonEventSubscriber.md#ZH-CN_TOPIC_0000002529285505__commoneventsubscriber-1)10+

type [CommonEventSubscriber](../../topics/misc/commonEventSubscriber.md#ZH-CN_TOPIC_0000002529285505__commoneventsubscriber-1) = [_CommonEventSubscriber](../../topics/misc/commonEventSubscriber.md#ZH-CN_TOPIC_0000002529285505__commoneventsubscriber-1)

描述公共事件的订阅者。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.CommonEvent

| 类型 | 说明 |
| --- | --- |
| _[CommonEventSubscriber](../../topics/misc/commonEventSubscriber.md#ZH-CN_TOPIC_0000002529285505__commoneventsubscriber-1) | 描述公共事件的订阅者。 |

#### [CommonEventSubscribeInfo](../../topics/misc/CommonEventSubscribeInfo.md)10+

type [CommonEventSubscribeInfo](../../topics/misc/CommonEventSubscribeInfo.md) = [_CommonEventSubscribeInfo](../../topics/misc/CommonEventSubscribeInfo.md)

用于表示订阅者的信息。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.CommonEvent

| 类型 | 说明 |
| --- | --- |
| _[CommonEventSubscribeInfo](../../topics/misc/CommonEventSubscribeInfo.md) | 用于表示订阅者的信息。 |

#### [CommonEventPublishData](../../topics/misc/CommonEventPublishData.md)10+

type [CommonEventPublishData](../../topics/misc/CommonEventPublishData.md) = [_CommonEventPublishData](../../topics/misc/CommonEventPublishData.md)

描述公共事件内容和属性。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.CommonEvent

| 类型 | 说明 |
| --- | --- |
| _[CommonEventPublishData](../../topics/misc/CommonEventPublishData.md) | 描述公共事件内容和属性。 |