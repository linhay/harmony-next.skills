# @ohos.commonEvent (公共事件模块)

本模块提供了公共事件的能力，包括公共事件的权限列表，发布公共事件，订阅或取消订阅公共事件，获取或修改公共事件结果代码、结果数据等。

-

从API Version 9开始，该接口不再维护，推荐使用新接口[@ohos.commonEventManager](@ohos.commonEventManager (公共事件模块).md)。

-

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import commonEvent from '@ohos.commonEvent';
```

#### Support

系统公共事件是指由系统服务或系统应用发布的事件，订阅这些系统公共事件需要特定的权限。发布或订阅这些事件需要使用如下链接中的枚举定义。

全部系统公共事件枚举定义请参见[系统公共事件定义](系统公共事件定义(待停用).md)。

#### commonEvent.publish(deprecated)

publish(event: string, callback: AsyncCallback<void>): void

发布公共事件（回调形式）。

从 API version 7开始支持，从API version 9开始废弃。建议使用[commonEventManager.publish](@ohos.commonEventManager (公共事件模块).md#ZH-CN_TOPIC_0000002497445532__commoneventmanagerpublish)替代。

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

参数名类型必填说明eventstring是表示要发送的公共事件。callbackAsyncCallback<void>是表示被指定的回调方法。

**示例：**

```ets
import Base from '@ohos.base';

//发布公共事件回调
function publishCB(err:Base.BusinessError) {
    if (err.code) {
        console.error(`publish failed, code is ${err.code}`);
    } else {
        console.info("publish");
    }
}

//发布公共事件
commonEvent.publish("event", publishCB);
```

#### commonEvent.publish(deprecated)

publish(event: string, options: CommonEventPublishData, callback: AsyncCallback<void>): void

以回调的形式发布公共事件。

从 API version 7开始支持，从API version 9开始废弃。建议使用[commonEventManager.publish](@ohos.commonEventManager (公共事件模块).md#ZH-CN_TOPIC_0000002497445532__commoneventmanagerpublish-1)替代。

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

参数名类型必填说明eventstring是表示要发布的公共事件。options[CommonEventPublishData](CommonEventPublishData.md)是表示发布公共事件的属性。callbackAsyncCallback<void>是表示被指定的回调方法。

**示例：**

```ets
import Base from '@ohos.base';
import CommonEventManager from '@ohos.commonEventManager';

//公共事件相关信息
let options:CommonEventManager.CommonEventPublishData = {
    code: 0,             //公共事件的初始代码
    data: "initial data",//公共事件的初始数据
    isOrdered: true  //有序公共事件
}

//发布公共事件回调
function publishCB(err:Base.BusinessError) {
    if (err.code) {
        console.error(`publish failed, code is ${err.code}`);
    } else {
        console.info("publish");
    }
}

//发布公共事件
commonEvent.publish("event", options, publishCB);
```

#### commonEvent.createSubscriber(deprecated)

createSubscriber(subscribeInfo: CommonEventSubscribeInfo, callback: AsyncCallback<CommonEventSubscriber>): void

以回调形式创建订阅者。

从 API version 7开始支持，从API version 9开始废弃。建议使用[commonEventManager.createSubscriber](@ohos.commonEventManager (公共事件模块).md#ZH-CN_TOPIC_0000002497445532__commoneventmanagercreatesubscriber)替代。

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

参数名类型必填说明subscribeInfo[CommonEventSubscribeInfo](CommonEventSubscribeInfo.md)是表示订阅信息。callbackAsyncCallback<[CommonEventSubscriber](commonEventSubscriber.md)>是表示创建订阅者的回调方法。

**示例：**

```ets
import Base from '@ohos.base';
import CommonEventManager from '@ohos.commonEventManager';

let subscriber:CommonEventManager.CommonEventSubscriber; // 用于保存创建成功的订阅者对象，后续使用其完成订阅及退订的动作

// 订阅者信息
let subscribeInfo:CommonEventManager.CommonEventSubscribeInfo = {
    events: ["event"]
};

// 创建订阅者回调
function createCB(err:Base.BusinessError, commonEventSubscriber:CommonEventManager.CommonEventSubscriber) {
    if (err.code) {
        console.error(`createSubscriber failed, code is ${err.code}`);
    } else {
        console.info("createSubscriber");
        subscriber = commonEventSubscriber;
    }
}

// 创建订阅者
commonEvent.createSubscriber(subscribeInfo, createCB);
```

#### commonEvent.createSubscriber(deprecated)

createSubscriber(subscribeInfo: CommonEventSubscribeInfo): Promise<CommonEventSubscriber>

以Promise形式创建订阅者。

从 API version 7开始支持，从API version 9开始废弃。建议使用[commonEventManager.createSubscriber](@ohos.commonEventManager (公共事件模块).md#ZH-CN_TOPIC_0000002497445532__commoneventmanagercreatesubscriber-1)替代。

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

参数名类型必填说明subscribeInfo[CommonEventSubscribeInfo](CommonEventSubscribeInfo.md)是表示订阅信息。

**返回值：**

类型说明Promise<[CommonEventSubscriber](commonEventSubscriber.md)>返回订阅者对象。

**示例：**

```ets
import Base from '@ohos.base';
import CommonEventManager from '@ohos.commonEventManager';

let subscriber:CommonEventManager.CommonEventSubscriber; // 用于保存创建成功的订阅者对象，后续使用其完成订阅及退订的动作

// 订阅者信息
let subscribeInfo:CommonEventManager.CommonEventSubscribeInfo = {
    events: ["event"]
};

// 创建订阅者
commonEvent.createSubscriber(subscribeInfo).then((commonEventSubscriber:CommonEventManager.CommonEventSubscriber) => {
    console.info("createSubscriber");
    subscriber = commonEventSubscriber;
}).catch((err:Base.BusinessError) => {
    console.error(`createSubscriber failed, code is ${err.code}`);
});
```

#### commonEvent.subscribe(deprecated)

subscribe(subscriber: CommonEventSubscriber, callback: AsyncCallback<CommonEventData>): void

以回调形式订阅公共事件。

从 API version 7开始支持，从API version 9开始废弃。建议使用[commonEventManager.subscribe](@ohos.commonEventManager (公共事件模块).md#ZH-CN_TOPIC_0000002497445532__commoneventmanagersubscribe)替代。

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

参数名类型必填说明subscriber[CommonEventSubscriber](commonEventSubscriber.md)是表示订阅者对象。callbackAsyncCallback<[CommonEventData](CommonEventData.md)>是表示接收公共事件数据的回调函数。

**示例：**

```ets
import Base from '@ohos.base';
import CommonEventManager from '@ohos.commonEventManager';

let subscriber:CommonEventManager.CommonEventSubscriber;// 用于保存创建成功的订阅者对象，后续使用其完成订阅及退订的动作

// 订阅者信息
let subscribeInfo:CommonEventManager.CommonEventSubscribeInfo = {
    events: ["event"]
};

// 订阅公共事件回调
function subscribeCB(err:Base.BusinessError, data:CommonEventManager.CommonEventData) {
    if (err.code) {
        console.error(`subscribe failed, code is ${err.code}`);
    } else {
        console.info("subscribe " + JSON.stringify(data));
    }
}

// 创建订阅者回调
function createCB(err:Base.BusinessError, commonEventSubscriber:CommonEventManager.CommonEventSubscriber) {
    if (err.code) {
        console.error(`createSubscriber failed, code is ${err.code}`);
    } else {
        console.info("createSubscriber");
        subscriber = commonEventSubscriber;
        // Subscribe to a common event.
        commonEvent.subscribe(subscriber, subscribeCB);
    }
}

// 创建订阅者
commonEvent.createSubscriber(subscribeInfo, createCB);
```

#### commonEvent.unsubscribe(deprecated)

unsubscribe(subscriber: CommonEventSubscriber, callback?: AsyncCallback<void>): void

以回调形式取消订阅公共事件。

从 API version 7开始支持，从API version 9开始废弃。建议使用[commonEventManager.unsubscribe](@ohos.commonEventManager (公共事件模块).md#ZH-CN_TOPIC_0000002497445532__commoneventmanagerunsubscribe)替代。

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

参数名类型必填说明subscriber[CommonEventSubscriber](commonEventSubscriber.md)是表示订阅者对象。callbackAsyncCallback<void>否表示取消订阅的回调方法。

**示例：**

```ets
import Base from '@ohos.base';
import CommonEventManager from '@ohos.commonEventManager';

let subscriber:CommonEventManager.CommonEventSubscriber;    // 用于保存创建成功的订阅者对象，后续使用其完成订阅及退订的动作

// 订阅者信息
let subscribeInfo:CommonEventManager.CommonEventSubscribeInfo = {
    events: ["event"]
};

// 订阅公共事件回调
function subscribeCB(err:Base.BusinessError, data:CommonEventManager.CommonEventData) {
    if (err.code) {
        console.error(`subscribe failed, code is ${err.code}`);
    } else {
        console.info("subscribe " + JSON.stringify(data));
    }
}

// 创建订阅者回调
function createCB(err:Base.BusinessError, commonEventSubscriber:CommonEventManager.CommonEventSubscriber) {
    if (err.code) {
        console.error(`createSubscriber failed, code is ${err.code}`);
    } else {
        console.info("createSubscriber");
        subscriber = commonEventSubscriber;
        // Subscribe to a common event.
        commonEvent.subscribe(subscriber, subscribeCB);
    }
}

// 取消订阅公共事件回调
function unsubscribeCB(err:Base.BusinessError) {
    if (err.code) {
        console.error(`unsubscribe failed, code is ${err.code}`);
    } else {
        console.info("unsubscribe");
    }
}

// 创建订阅者
commonEvent.createSubscriber(subscribeInfo, createCB);

// 取消订阅公共事件
commonEvent.unsubscribe(subscriber, unsubscribeCB);
```