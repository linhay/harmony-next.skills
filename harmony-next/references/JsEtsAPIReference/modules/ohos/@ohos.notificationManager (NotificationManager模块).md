# @ohos.notificationManager (NotificationManager模块)

本模块提供通知管理的能力，包括发布、更新、取消通知，创建、获取、移除通知渠道，获取发布通知应用的使能状态，获取通知的相关信息等。

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { notificationManager } from '@kit.NotificationKit';
```

#### notificationManager.publish

publish(request: NotificationRequest, callback: AsyncCallback<void>): void

发布通知。使用callback异步回调。

如果新发布通知与已发布通知的ID和标签都相同，则新通知将取代原有通知。

**系统能力**：SystemCapability.Notification.Notification

**参数：**

参数名类型必填说明request[NotificationRequest](../../topics/misc/NotificationRequest.md#ZH-CN_TOPIC_0000002497606118__notificationrequest-1)是设置发布通知的内容和相关配置信息。callbackAsyncCallback<void>是回调函数。当发布通知成功，err为undefined，否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)、[通知错误码](../../errors/通知错误码.md)、[HTTP错误码](../../errors/HTTP错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed.1600001Internal error.1600002Marshalling or unmarshalling error.1600003Failed to connect to the service.1600004Notification disabled.1600005Notification slot disabled.1600007The notification does not exist.1600009The notification sending frequency reaches the upper limit.1600012No memory space.1600014No permission.1600015The current notification status does not support duplicate configurations.1600016The notification version for this update is too low.1600020The application is not allowed to send notifications due to permission settings.2300007Network unreachable.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

// publish回调
let publishCallback = (err: BusinessError): void => {
  if (err) {
    console.error(`Failed to publish notification. Code is ${err.code}, message is ${err.message}`);
  } else {
    console.info(`Succeeded in publishing notification.`);
  }
}
// 通知Request对象
let notificationRequest: notificationManager.NotificationRequest = {
  id: 1,
  content: {
    notificationContentType: notificationManager.ContentType.NOTIFICATION_CONTENT_BASIC_TEXT,
    normal: {
      title: "test_title",
      text: "test_text",
      additionalText: "test_additionalText"
    }
  }
};
notificationManager.publish(notificationRequest, publishCallback);
```

#### notificationManager.publish

publish(request: NotificationRequest): Promise<void>

发布通知。使用Promise异步回调。

如果新发布通知与已发布通知的ID和标签都相同，则新通知将取代原有通知。

**系统能力**：SystemCapability.Notification.Notification

**参数：**

参数名类型必填说明request[NotificationRequest](../../topics/misc/NotificationRequest.md#ZH-CN_TOPIC_0000002497606118__notificationrequest-1)是设置发布通知的内容和相关配置信息。

**返回值：**

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)、[通知错误码](../../errors/通知错误码.md)、[HTTP错误码](../../errors/HTTP错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed.1600001Internal error.1600002Marshalling or unmarshalling error.1600003Failed to connect to the service.1600004Notification disabled.1600005Notification slot disabled.1600007The notification does not exist.1600009The notification sending frequency reaches the upper limit.1600012No memory space.1600014No permission.1600015The current notification status does not support duplicate configurations.1600016The notification version for this update is too low.1600020The application is not allowed to send notifications due to permission settings.2300007Network unreachable.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

// 通知Request对象
let notificationRequest: notificationManager.NotificationRequest = {
  id: 1,
  content: {
    notificationContentType: notificationManager.ContentType.NOTIFICATION_CONTENT_BASIC_TEXT,
    normal: {
      title: "test_title",
      text: "test_text",
      additionalText: "test_additionalText"
    }
  }
};
notificationManager.publish(notificationRequest).then(() => {
  console.info(`Succeeded in publishing notification.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to publish notification. Code is ${err.code}, message is ${err.message}`);
});
```

#### notificationManager.cancel

cancel(id: number, label: string, callback: AsyncCallback<void>): void

根据通知ID和标签取消已发布的通知。使用callback异步回调。

**系统能力**：SystemCapability.Notification.Notification

**参数：**

参数名类型必填说明idnumber是通知ID。labelstring是通知标签。callbackAsyncCallback<void>是回调函数。根据通知ID和标签取消已发布的通知成功，err为undefined，否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[通知错误码](../../errors/通知错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed.1600001Internal error.1600002Marshalling or unmarshalling error.1600003Failed to connect to the service.1600007The notification does not exist.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

// cancel回调
let cancelCallback = (err: BusinessError): void => {
  if (err) {
    console.error(`Failed to cancel notification. Code is ${err.code}, message is ${err.message}`);
  } else {
    console.info(`Succeeded in canceling notification.`);
  }
}
notificationManager.cancel(0, "label", cancelCallback);
```

#### notificationManager.cancel

cancel(id: number, label?: string): Promise<void>

根据通知ID和标签取消已发布的通知，若标签为空，则取消与指定通知ID匹配的已发布通知。使用Promise异步回调。

**系统能力**：SystemCapability.Notification.Notification

**参数：**

参数名类型必填说明idnumber是通知ID。labelstring否通知标签，默认为空。

**返回值：**

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[通知错误码](../../errors/通知错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed.1600001Internal error.1600002Marshalling or unmarshalling error.1600003Failed to connect to the service.1600007The notification does not exist.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

notificationManager.cancel(0).then(() => {
  console.info(`Succeeded in canceling notification.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to cancel notification. Code is ${err.code}, message is ${err.message}`);
});
```

#### notificationManager.cancel

cancel(id: number, callback: AsyncCallback<void>): void

根据指定的通知ID取消已发布的通知。使用callback异步回调。

**系统能力**：SystemCapability.Notification.Notification

**参数：**

参数名类型必填说明idnumber是通知ID。callbackAsyncCallback<void>是回调函数。当取消已发布的通知成功，err为undefined，否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[通知错误码](../../errors/通知错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed.1600001Internal error.1600002Marshalling or unmarshalling error.1600003Failed to connect to the service.1600007The notification does not exist.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

// cancel回调
let cancelCallback = (err: BusinessError): void => {
  if (err) {
    console.error(`Failed to cancel notification. Code is ${err.code}, message is ${err.message}`);
  } else {
    console.info(`Succeeded in canceling notification.`);
  }
}
notificationManager.cancel(0, cancelCallback);
```

#### notificationManager.cancelAll

cancelAll(callback: AsyncCallback<void>): void

取消当前应用所有已发布的通知。使用callback异步回调。

**系统能力**：SystemCapability.Notification.Notification

**参数：**

参数名类型必填说明callbackAsyncCallback<void>是回调函数。当取消当前应用所有已发布的通知成功，err为undefined，否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[通知错误码](../../errors/通知错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed.1600001Internal error.1600002Marshalling or unmarshalling error.1600003Failed to connect to the service.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

// cancel回调
let cancelAllCallback = (err: BusinessError): void => {
  if (err) {
    console.error(`Failed to cancel all notification. Code is ${err.code}, message is ${err.message}`);
  } else {
    console.info(`Succeeded in canceling all notification.`);
  }
}
notificationManager.cancelAll(cancelAllCallback);
```

#### notificationManager.cancelAll

cancelAll(): Promise<void>

取消当前应用所有已发布的通知。使用Promise异步回调。

**系统能力**：SystemCapability.Notification.Notification

**返回值：**

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[通知错误码](../../errors/通知错误码.md)。

错误码ID错误信息1600001Internal error.1600002Marshalling or unmarshalling error.1600003Failed to connect to the service.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

notificationManager.cancelAll().then(() => {
  console.info(`Succeeded in canceling all notification.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to cancel all notification. Code is ${err.code}, message is ${err.message}`);
});
```

#### notificationManager.addSlot

addSlot(type: SlotType, callback: AsyncCallback<void>): void

创建指定类型的通知渠道。使用callback异步回调。

**系统能力**：SystemCapability.Notification.Notification

**参数：**

参数名类型必填说明type[SlotType](#ZH-CN_TOPIC_0000002497446132__slottype)是要创建的通知渠道的类型。callbackAsyncCallback<void>是回调函数。当创建指定类型的通知渠道成功，err为undefined，否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[通知错误码](../../errors/通知错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed.1600001Internal error.1600002Marshalling or unmarshalling error.1600003Failed to connect to the service.1600012No memory space.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

// addSlot回调
let addSlotCallBack = (err: BusinessError): void => {
  if (err) {
    console.error(`Failed to add slot. Code is ${err.code}, message is ${err.message}`);
  } else {
    console.info(`Succeeded in adding slot.`);
  }
}
notificationManager.addSlot(notificationManager.SlotType.SOCIAL_COMMUNICATION, addSlotCallBack);
```

#### notificationManager.addSlot

addSlot(type: SlotType): Promise<void>

创建指定类型的通知渠道。使用Promise异步回调。

**系统能力**：SystemCapability.Notification.Notification

**参数：**

参数名类型必填说明type[SlotType](#ZH-CN_TOPIC_0000002497446132__slottype)是要创建的通知渠道的类型。

**返回值：**

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[通知错误码](../../errors/通知错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed.1600001Internal error.1600002Marshalling or unmarshalling error.1600003Failed to connect to the service.1600012No memory space.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

notificationManager.addSlot(notificationManager.SlotType.SOCIAL_COMMUNICATION).then(() => {
  console.info(`Succeeded in adding slot.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to add slot. Code is ${err.code}, message is ${err.message}`);
});
```

#### notificationManager.getSlot

getSlot(slotType: SlotType, callback: AsyncCallback<NotificationSlot>): void

获取指定类型的通知渠道。使用callback异步回调。

**系统能力**：SystemCapability.Notification.Notification

**参数：**

参数名类型必填说明slotType[SlotType](#ZH-CN_TOPIC_0000002497446132__slottype)是通知渠道类型，例如社交通信、服务提醒、内容咨询等类型。callbackAsyncCallback<[NotificationSlot](../../topics/misc/NotificationSlot.md)>是回调函数。当获取通知渠道成功，err为undefined，data为获取到的NotificationSlot，否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[通知错误码](../../errors/通知错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed.1600001Internal error.1600002Marshalling or unmarshalling error.1600003Failed to connect to the service.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

// getSlot回调
let getSlotCallback = (err: BusinessError, data: notificationManager.NotificationSlot): void => {
  if (err) {
    console.error(`Failed to get slot. Code is ${err.code}, message is ${err.message}`);
  } else {
    console.info(`Succeeded in getting slot, data is ${JSON.stringify(data)}`);
  }
}
let slotType: notificationManager.SlotType = notificationManager.SlotType.SOCIAL_COMMUNICATION;
notificationManager.getSlot(slotType, getSlotCallback);
```

#### notificationManager.getSlot

getSlot(slotType: SlotType): Promise<NotificationSlot>

获取指定类型的通知渠道。使用Promise异步回调。

**系统能力**：SystemCapability.Notification.Notification

**参数：**

参数名类型必填说明slotType[SlotType](#ZH-CN_TOPIC_0000002497446132__slottype)是通知渠道类型，例如社交通信、服务提醒、内容咨询等类型。

**返回值：**

类型说明Promise<[NotificationSlot](../../topics/misc/NotificationSlot.md)>Promise对象，返回通知渠道对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[通知错误码](../../errors/通知错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed.1600001Internal error.1600002Marshalling or unmarshalling error.1600003Failed to connect to the service.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let slotType: notificationManager.SlotType = notificationManager.SlotType.SOCIAL_COMMUNICATION;
notificationManager.getSlot(slotType).then((data: notificationManager.NotificationSlot) => {
  console.info(`Succeeded in getting slot, data is ${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to get slot. Code is ${err.code}, message is ${err.message}`);
});
```

#### notificationManager.getSlots

getSlots(callback: AsyncCallback<Array<NotificationSlot>>): void

获取当前应用的所有通知渠道。使用callback异步回调。

**系统能力**：SystemCapability.Notification.Notification

**参数：**

参数名类型必填说明callbackAsyncCallback<Array<[NotificationSlot](../../topics/misc/NotificationSlot.md)>>是回调函数。当获取通知渠道成功，err为undefined，data为获取到的NotificationSlot数组，否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[通知错误码](../../errors/通知错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed.1600001Internal error.1600002Marshalling or unmarshalling error.1600003Failed to connect to the service.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

// getSlots回调
let getSlotsCallback = (err: BusinessError, data: Array<notificationManager.NotificationSlot>): void => {
  if (err) {
    console.error(`Failed to get slots. Code is ${err.code}, message is ${err.message}`);
  } else {
    console.info(`Succeeded in getting slots, data is ${JSON.stringify(data)}`);
  }
}
notificationManager.getSlots(getSlotsCallback);
```

#### notificationManager.getSlots

getSlots(): Promise<Array<NotificationSlot>>

获取当前应用的所有通知渠道。使用Promise异步回调。

**系统能力**：SystemCapability.Notification.Notification

**返回值：**

类型说明Promise<Array<[NotificationSlot](../../topics/misc/NotificationSlot.md)>>Promise对象，返回通知渠道对象。

**错误码：**

以下错误码的详细介绍请参见[通知错误码](../../errors/通知错误码.md)。

错误码ID错误信息1600001Internal error.1600002Marshalling or unmarshalling error.1600003Failed to connect to the service.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

notificationManager.getSlots().then((data: Array<notificationManager.NotificationSlot>) => {
  console.info(`Succeeded in getting slots, data is ${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to get slots. Code is ${err.code}, message is ${err.message}`);
});
```

#### notificationManager.removeSlot

removeSlot(slotType: SlotType, callback: AsyncCallback<void>): void

删除当前应用指定类型的通知渠道。使用callback异步回调。

**系统能力**：SystemCapability.Notification.Notification

**参数：**

参数名类型必填说明slotType[SlotType](#ZH-CN_TOPIC_0000002497446132__slottype)是通知渠道类型，例如社交通信、服务提醒、内容咨询等类型。callbackAsyncCallback<void>是回调函数。当删除指定类型的通知渠道成功，err为undefined，否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[通知错误码](../../errors/通知错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed.1600001Internal error.1600002Marshalling or unmarshalling error.1600003Failed to connect to the service.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

// removeSlot回调
let removeSlotCallback = (err: BusinessError): void => {
  if (err) {
    console.error(`Failed to remove slot. Code is ${err.code}, message is ${err.message}`);
  } else {
    console.info(`Succeeded in removing slot.`);
  }
}
let slotType = notificationManager.SlotType.SOCIAL_COMMUNICATION;
notificationManager.removeSlot(slotType, removeSlotCallback);
```

#### notificationManager.removeSlot

removeSlot(slotType: SlotType): Promise<void>

删除当前应用指定类型的通知渠道。使用Promise异步回调。

**系统能力**：SystemCapability.Notification.Notification

**参数：**

参数名类型必填说明slotType[SlotType](#ZH-CN_TOPIC_0000002497446132__slottype)是通知渠道类型，例如社交通信、服务提醒、内容咨询等类型。

**返回值：**

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[通知错误码](../../errors/通知错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed.1600001Internal error.1600002Marshalling or unmarshalling error.1600003Failed to connect to the service.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let slotType: notificationManager.SlotType = notificationManager.SlotType.SOCIAL_COMMUNICATION;
notificationManager.removeSlot(slotType).then(() => {
  console.info(`Succeeded in removing slot.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to remove slot. Code is ${err.code}, message is ${err.message}`);
});
```

#### notificationManager.removeAllSlots

removeAllSlots(callback: AsyncCallback<void>): void

删除当前应用所有通知渠道。使用callback异步回调。

**系统能力**：SystemCapability.Notification.Notification

**参数：**

参数名类型必填说明callbackAsyncCallback<void>是回调函数。当删除当前应用所有通知渠道成功，err为undefined，否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[通知错误码](../../errors/通知错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed.1600001Internal error.1600002Marshalling or unmarshalling error.1600003Failed to connect to the service.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let removeAllSlotsCallback = (err: BusinessError): void => {
  if (err) {
    console.error(`Failed to remove all slots. Code is ${err.code}, message is ${err.message}`);
  } else {
    console.info(`Succeeded in removing all slots.`);
  }
}
notificationManager.removeAllSlots(removeAllSlotsCallback);
```

#### notificationManager.removeAllSlots

removeAllSlots(): Promise<void>

删除当前应用所有通知渠道。使用Promise异步回调。

**系统能力**：SystemCapability.Notification.Notification

**返回值：**

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[通知错误码](../../errors/通知错误码.md)。

错误码ID错误信息1600001Internal error.1600002Marshalling or unmarshalling error.1600003Failed to connect to the service.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

notificationManager.removeAllSlots().then(() => {
  console.info(`Succeeded in removing all slots.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to remove all slots. Code is ${err.code}, message is ${err.message}`);
});
```

#### notificationManager.isNotificationEnabled11+

isNotificationEnabled(callback: AsyncCallback<boolean>): void

查询当前应用通知使能状态。使用callback异步回调。

**系统能力**：SystemCapability.Notification.Notification

**参数：**

参数名类型必填说明callbackAsyncCallback<boolean>是回调函数。返回true，表示允许发布通知；返回false，表示禁止发布通知；调用失败返回错误对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)、[通知错误码](../../errors/通知错误码.md)、[包管理子系统通用错误码](../../errors/包管理子系统通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed.1600001Internal error.1600002Marshalling or unmarshalling error.1600003Failed to connect to the service.1600008The user does not exist.17700001The specified bundle name was not found.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let isNotificationEnabledCallback = (err: BusinessError, data: boolean): void => {
  if (err) {
    console.error(`isNotificationEnabled failed, code is ${err.code}, message is ${err.message}`);
  } else {
    console.info(`isNotificationEnabled success, data is ${JSON.stringify(data)}`);
  }
}

notificationManager.isNotificationEnabled(isNotificationEnabledCallback);
```

#### notificationManager.isNotificationEnabled11+

isNotificationEnabled(): Promise<boolean>

查询当前应用通知使能状态。使用Promise异步回调。

**系统能力**：SystemCapability.Notification.Notification

**返回值：**

类型说明Promise<boolean>Promise对象。返回true，表示允许发布通知；返回false，表示禁止发布通知。

**错误码：**

以下错误码的详细介绍请参见[通知错误码](../../errors/通知错误码.md)、[包管理子系统通用错误码](../../errors/包管理子系统通用错误码.md)。

错误码ID错误信息1600001Internal error.1600002Marshalling or unmarshalling error.1600003Failed to connect to the service.1600008The user does not exist.17700001The specified bundle name was not found.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

notificationManager.isNotificationEnabled().then((data: boolean) => {
  console.info(`isNotificationEnabled success, data: ${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
  console.error(`isNotificationEnabled failed, code is ${err.code}, message is ${err.message}`);
});
```

#### notificationManager.isNotificationEnabledSync12+

isNotificationEnabledSync(): boolean

同步查询当前应用通知使能状态。

**系统能力**：SystemCapability.Notification.Notification

**返回值：**

类型说明boolean返回查询通知使能状态的结果。返回true，表示允许发布通知；返回false，表示禁止发布通知。

**错误码：**

以下错误码的详细介绍请参见[通知错误码](../../errors/通知错误码.md)。

错误码ID错误信息1600001Internal error.1600002Marshalling or unmarshalling error.1600003Failed to connect to the service.

**示例：**

```ets
let enabled = notificationManager.isNotificationEnabledSync();
console.info(`isNotificationEnabledSync success, data is : ${JSON.stringify(enabled)}`);
```

#### notificationManager.setBadgeNumber10+

setBadgeNumber(badgeNumber: number): Promise<void>

设定角标个数，在应用的桌面图标上呈现。使用Promise异步回调。

**系统能力**：SystemCapability.Notification.Notification

**设备行为差异**：该接口在Wearable中返回801错误码，在其他设备类型中可正常调用。

**参数：**

参数名类型必填说明badgeNumbernumber是角标个数。当角标设定个数取值小于或等于0时，清除角标。取值大于99时，通知角标将显示99+。

**返回值：**

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[通知错误码](../../errors/通知错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed.801Capability not supported.1600001Internal error.1600002Marshalling or unmarshalling error.1600003Failed to connect to the service.1600012No memory space.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let badgeNumber: number = 10;
notificationManager.setBadgeNumber(badgeNumber).then(() => {
  console.info(`Succeeded in setting badge number.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to set badge number. Code is ${err.code}, message is ${err.message}`);
});
```

#### notificationManager.setBadgeNumber10+

setBadgeNumber(badgeNumber: number, callback: AsyncCallback<void>): void

设定角标个数，在应用的桌面图标上呈现。使用callback异步回调。

**系统能力**：SystemCapability.Notification.Notification

**设备行为差异**：该接口在Wearable中返回801错误码，在其他设备类型中可正常调用。

**参数：**

参数名类型必填说明badgeNumbernumber是角标个数。当角标设定个数取值小于或等于0时，清除角标。取值大于99时，通知角标将显示99+。callbackAsyncCallback<void>是回调函数。当设定角标个数成功，err为undefined，否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[通知错误码](../../errors/通知错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed.801Capability not supported.1600001Internal error.1600002Marshalling or unmarshalling error.1600003Failed to connect to the service.1600012No memory space.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let setBadgeNumberCallback = (err: BusinessError): void => {
  if (err) {
    console.error(`Failed to set badge number. Code is ${err.code}, message is ${err.message}`);
  } else {
    console.info(`Succeeded in setting badge number.`);
  }
}
let badgeNumber: number = 10;
notificationManager.setBadgeNumber(badgeNumber, setBadgeNumberCallback);
```

#### notificationManager.getBadgeNumber22+

getBadgeNumber(): Promise<long>

获取当前应用角标数量。使用Promise异步回调。

**系统能力**：SystemCapability.Notification.Notification

**返回值：**

类型说明Promise<long>Promise对象，返回当前应用角标数量。（查询的角标数量与当前应用通知开关，桌面角标开关是否开启无关）

**错误码：**

以下错误码的详细介绍请参见[通知错误码](../../errors/通知错误码.md)。

错误码ID错误信息1600001Internal error.1600002Marshalling or unmarshalling error.1600003Failed to connect to the service.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

notificationManager.getBadgeNumber().then((badgeNumber) => {
  console.info(`Succeeded in getting badge number, badgeNumber is ${JSON.stringify(badgeNumber)}`);
}).catch((err: BusinessError) => {
  console.info(`Failed to get badge number. Code is ${err.code}, message is ${err.message}`);
});
```

#### notificationManager.getActiveNotificationCount

getActiveNotificationCount(callback: AsyncCallback<number>): void

获取当前应用未删除的通知数。使用callback异步回调。

**系统能力**：SystemCapability.Notification.Notification

**参数：**

参数名类型必填说明callbackAsyncCallback<number>是回调函数。当获取当前应用未删除的通知数成功，err为undefined，data为当前应用未删除的通知数，否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[通知错误码](../../errors/通知错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed.1600001Internal error.1600002Marshalling or unmarshalling error.1600003Failed to connect to the service.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let getActiveNotificationCountCallback = (err: BusinessError, data: number): void => {
  if (err) {
    console.error(`Failed to get active notification count. Code is ${err.code}, message is ${err.message}`);
  } else {
    console.info(`Succeeded in getting active notification count, data is ${JSON.stringify(data)}`);
  }
}

notificationManager.getActiveNotificationCount(getActiveNotificationCountCallback);
```

#### notificationManager.getActiveNotificationCount

getActiveNotificationCount(): Promise<number>

获取当前应用未删除的通知数。使用Promise异步回调。

**系统能力**：SystemCapability.Notification.Notification

**返回值：**

类型说明Promise<number>Promise对象，返回当前应用未删除通知数。

**错误码：**

以下错误码的详细介绍请参见[通知错误码](../../errors/通知错误码.md)。

错误码ID错误信息1600001Internal error.1600002Marshalling or unmarshalling error.1600003Failed to connect to the service.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

notificationManager.getActiveNotificationCount().then((data: number) => {
  console.info(`Succeeded in getting active notification count, data is ${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to get active notification count. Code is ${err.code}, message is ${err.message}`);
});
```

#### notificationManager.getActiveNotifications

getActiveNotifications(callback: AsyncCallback<Array<NotificationRequest>>): void

获取当前应用未删除的通知列表。使用callback异步回调。

**系统能力**：SystemCapability.Notification.Notification

**参数：**

参数名类型必填说明callbackAsyncCallback<Array<[NotificationRequest](../../topics/misc/NotificationRequest.md#ZH-CN_TOPIC_0000002497606118__notificationrequest-1)>>是回调函数。当获取未删除的通知列表成功，err为undefined，data为获取到的通知列表，否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[通知错误码](../../errors/通知错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed.1600001Internal error.1600002Marshalling or unmarshalling error.1600003Failed to connect to the service.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let getActiveNotificationsCallback = (err: BusinessError, data: Array<notificationManager.NotificationRequest>): void => {
  if (err) {
    console.error(`Failed to get active notifications. Code is ${err.code}, message is ${err.message}`);
  } else {
    console.info(`Succeeded in getting active notifications, data is ${JSON.stringify(data)}`);
  }
}
notificationManager.getActiveNotifications(getActiveNotificationsCallback);
```

#### notificationManager.getActiveNotifications

getActiveNotifications(): Promise<Array<NotificationRequest>>

获取当前应用未删除的通知列表。使用Promise异步回调。

**系统能力**：SystemCapability.Notification.Notification

**返回值：**

类型说明Promise<Array<[NotificationRequest](../../topics/misc/NotificationRequest.md#ZH-CN_TOPIC_0000002497606118__notificationrequest-1)>>Promise对象，返回当前应用的通知列表。

**错误码：**

以下错误码的详细介绍请参见[通知错误码](../../errors/通知错误码.md)。

错误码ID错误信息1600001Internal error.1600002Marshalling or unmarshalling error.1600003Failed to connect to the service.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

notificationManager.getActiveNotifications().then((data: Array<notificationManager.NotificationRequest>) => {
  console.info(`Succeeded in getting active notifications, data is ${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to get active notifications. Code is ${err.code}, message is ${err.message}`);
});
```

#### notificationManager.cancelGroup

cancelGroup(groupName: string, callback: AsyncCallback<void>): void

取消当前应用指定组下的通知。使用callback异步回调。

**系统能力**：SystemCapability.Notification.Notification

**参数：**

参数名类型必填说明groupNamestring是通知组名称，此名称需要在发布通知时通过[NotificationRequest](../../topics/misc/NotificationRequest.md#ZH-CN_TOPIC_0000002497606118__notificationrequest-1)对象指定。callbackAsyncCallback<void>是回调函数。当取消当前应用指定组下的通知成功，err为undefined，否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[通知错误码](../../errors/通知错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed.1600001Internal error.1600002Marshalling or unmarshalling error.1600003Failed to connect to the service.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let cancelGroupCallback = (err: BusinessError): void => {
  if (err) {
    console.error(`Failed to cancel group. Code is ${err.code}, message is ${err.message}`);
  } else {
    console.info(`Succeeded in canceling group.`);
  }
}
let groupName: string = "GroupName";
notificationManager.cancelGroup(groupName, cancelGroupCallback);
```

#### notificationManager.cancelGroup

cancelGroup(groupName: string): Promise<void>

取消当前应用指定组下的通知。使用Promise异步回调。

**系统能力**：SystemCapability.Notification.Notification

**参数：**

参数名类型必填说明groupNamestring是通知组名称，此名称需要在发布通知时通过[NotificationRequest](../../topics/misc/NotificationRequest.md#ZH-CN_TOPIC_0000002497606118__notificationrequest-1)对象指定。

**返回值：**

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[通知错误码](../../errors/通知错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed.1600001Internal error.1600002Marshalling or unmarshalling error.1600003Failed to connect to the service.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let groupName: string = "GroupName";
notificationManager.cancelGroup(groupName).then(() => {
  console.info(`Succeeded in canceling group.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to cancel group. Code is ${err.code}, message is ${err.message}`);
});
```

#### notificationManager.isSupportTemplate

isSupportTemplate(templateName: string, callback: AsyncCallback<boolean>): void

在使用[通知模板](../../topics/misc/NotificationTemplate.md)发布通知前，可以通过该接口查询是否支持对应的通知模板。使用callback异步回调。

**系统能力**：SystemCapability.Notification.Notification

**参数：**

参数名类型必填说明templateNamestring是模板名称。当前仅支持'downloadTemplate'。callbackAsyncCallback<boolean>是回调函数。返回true表示支持该模板；返回false表示不支持该模板；调用失败返回错误对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[通知错误码](../../errors/通知错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed.1600001Internal error.1600002Marshalling or unmarshalling error.1600003Failed to connect to the service.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let templateName: string = 'downloadTemplate';
let isSupportTemplateCallback = (err: BusinessError, data: boolean): void => {
  if (err) {
    console.error(`isSupportTemplate failed, code is ${err.code}, message is ${err.message}`);
  } else {
    console.info(`isSupportTemplate success, data: ${JSON.stringify(data)}`);
  }
}
notificationManager.isSupportTemplate(templateName, isSupportTemplateCallback);
```

#### notificationManager.isSupportTemplate

isSupportTemplate(templateName: string): Promise<boolean>

在使用[通知模板](../../topics/misc/NotificationTemplate.md)发布通知前，可以通过该接口查询是否支持对应的通知模板。使用Promise异步回调。

**系统能力**：SystemCapability.Notification.Notification

**参数：**

参数名类型必填说明templateNamestring是模板名称。当前仅支持'downloadTemplate'。

**返回值：**

类型说明Promise<boolean>Promise对象。返回true表示支持该模板；返回false表示不支持该模板。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[通知错误码](../../errors/通知错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed.1600001Internal error.1600002Marshalling or unmarshalling error.1600003Failed to connect to the service.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let templateName: string = 'downloadTemplate';
notificationManager.isSupportTemplate(templateName).then((data: boolean) => {
  console.info(`isSupportTemplate success, data: ${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
  console.error(`isSupportTemplate failed, code is ${err.code}, message is ${err.message}`);
});
```

#### notificationManager.requestEnableNotification10+

requestEnableNotification(context: UIAbilityContext, callback: AsyncCallback<void>): void

应用需要获取用户授权才能发送通知。在通知发布前调用该接口，可以拉起通知授权弹窗，让用户选择是否允许发送通知。使用callback异步回调。

- 仅当应用界面加载完成后（即调用[loadContent](@ohos.app.ability.UIExtensionContentSession (UIExtensionAbility界面操作类).md#ZH-CN_TOPIC_0000002497444616__loadcontent)成功），方可使用该接口。
- 在使用该接口拉起通知授权弹窗后，如果用户拒绝授权，将无法使用该接口再次拉起弹窗。开发者可以调用[openNotificationSettings](#ZH-CN_TOPIC_0000002497446132__notificationmanageropennotificationsettings13)二次申请授权，拉起通知管理弹窗。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Notification.Notification

**参数：**

参数名类型必填说明context[UIAbilityContext](../../topics/graphics/UIAbilityContext.md)是通知弹窗绑定Ability的上下文。callbackAsyncCallback<void>是回调函数。当应用通过弹窗获取用户授权成功，err为undefined，否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[通知错误码](../../errors/通知错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed.1600001Internal error.1600002Marshalling or unmarshalling error.1600003Failed to connect to the service.1600004Notification disabled.1600013A notification dialog box is already displayed.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { hilog } from '@kit.PerformanceAnalysisKit';

class MyAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');
    windowStage.loadContent('pages/Index', (err, data) => {
      if (err.code) {
        hilog.error(0x0000, 'testTag', `Failed to load the content. Cause: ${JSON.stringify(err) ?? ''}`);
        return;
      }
      hilog.info(0x0000, 'testTag', `Succeeded in loading the content. Data: ${JSON.stringify(data) ?? ''}`);
      let requestEnableNotificationCallback = (err: BusinessError): void => {
        if (err) {
          hilog.error(0x0000, 'testTag', `[ANS] requestEnableNotification failed, code is ${err.code}, message is ${err.message}`);
        } else {
          hilog.info(0x0000, 'testTag', `[ANS] requestEnableNotification success`);
        }
      };
      notificationManager.requestEnableNotification(this.context, requestEnableNotificationCallback);
    });
  }
}
```

#### notificationManager.requestEnableNotification10+

requestEnableNotification(context: UIAbilityContext): Promise<void>

应用需要获取用户授权才能发送通知。在通知发布前调用该接口，可以拉起通知授权弹窗，让用户选择是否允许发送通知。使用Promise异步回调。

- 仅当应用界面加载完成后（即调用[loadContent](@ohos.app.ability.UIExtensionContentSession (UIExtensionAbility界面操作类).md#ZH-CN_TOPIC_0000002497444616__loadcontent)成功），方可使用该接口。
- 在使用该接口拉起通知授权弹窗后，如果用户拒绝授权，将无法使用该接口再次拉起弹窗。开发者可以调用[openNotificationSettings](#ZH-CN_TOPIC_0000002497446132__notificationmanageropennotificationsettings13)二次申请授权，拉起通知管理弹窗。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Notification.Notification

**参数：**

参数名类型必填说明context[UIAbilityContext](../../topics/graphics/UIAbilityContext.md)是通知弹窗绑定的Ability上下文。

**返回值：**

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[通知错误码](../../errors/通知错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed.1600001Internal error.1600002Marshalling or unmarshalling error.1600003Failed to connect to the service.1600004Notification disabled.1600013A notification dialog box is already displayed.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { hilog } from '@kit.PerformanceAnalysisKit';

class MyAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');
    windowStage.loadContent('pages/Index', (err, data) => {
      if (err.code) {
        hilog.error(0x0000, 'testTag', `Failed to load the content. Cause: ${JSON.stringify(err) ?? ''}`);
        return;
      }
      hilog.info(0x0000, 'testTag', `Succeeded in loading the content. Data: ${JSON.stringify(data) ?? ''}`);
      notificationManager.requestEnableNotification(this.context).then(() => {
        hilog.info(0x0000, 'testTag', `[ANS] requestEnableNotification success`);
      }).catch((err: BusinessError) => {
        hilog.error(0x0000, 'testTag', `[ANS] requestEnableNotification failed, code is ${err.code}, message is ${err.message}`);
      });
    });
  }
}
```

#### notificationManager.requestEnableNotification(deprecated)

requestEnableNotification(callback: AsyncCallback<void>): void

当前应用请求通知使能。使用callback异步回调。

从API version 9开始支持，从API version 12开始废弃，建议使用有context入参的[requestEnableNotification](#ZH-CN_TOPIC_0000002497446132__notificationmanagerrequestenablenotification10)替代。

**系统能力**：SystemCapability.Notification.Notification

**参数：**

参数名类型必填说明callbackAsyncCallback<void>是回调函数。当应用请求通知使能成功，err为undefined，否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[通知错误码](../../errors/通知错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed.1600001Internal error.1600002Marshalling or unmarshalling error.1600003Failed to connect to the service.1600004Notification disabled.1600013A notification dialog box is already displayed.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let requestEnableNotificationCallback = (err: BusinessError): void => {
  if (err) {
    console.error(`requestEnableNotification failed, code is ${err.code}, message is ${err.message}`);
  } else {
    console.info("requestEnableNotification success");
  }
};
notificationManager.requestEnableNotification(requestEnableNotificationCallback);
```

#### notificationManager.requestEnableNotification(deprecated)

requestEnableNotification(): Promise<void>

当前应用请求通知使能。使用Promise异步回调。

从API version 9开始支持，从API version 12开始废弃，建议使用有context入参的[requestEnableNotification](#ZH-CN_TOPIC_0000002497446132__notificationmanagerrequestenablenotification10-1)替代。

**系统能力**：SystemCapability.Notification.Notification

**返回值：**

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[通知错误码](../../errors/通知错误码.md)。

错误码ID错误信息1600001Internal error.1600002Marshalling or unmarshalling error.1600003Failed to connect to the service.1600004Notification disabled.1600013A notification dialog box is already displayed.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

notificationManager.requestEnableNotification().then(() => {
  console.info("requestEnableNotification success");
}).catch((err: BusinessError) => {
  console.error(`requestEnableNotification failed, code is ${err.code}, message is ${err.message}`);
});
```

#### notificationManager.isDistributedEnabled

isDistributedEnabled(callback: AsyncCallback<boolean>): void

查询设备是否支持跨设备协同通知。使用callback异步回调。

**设备行为差异**：该接口在Wearable/TV中回调返回恒为false，在其他设备类型中回调正常。

**系统能力**：SystemCapability.Notification.Notification

**参数：**

参数名类型必填说明callbackAsyncCallback<boolean>是回调函数。返回true表示支持跨设备协同通知；返回false表示不支持跨设备协同通知；调用失败返回错误对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[通知错误码](../../errors/通知错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed.1600001Internal error.1600002Marshalling or unmarshalling error.1600003Failed to connect to the service.1600010Distributed operation failed.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let isDistributedEnabledCallback = (err: BusinessError, data: boolean): void => {
  if (err) {
    console.error(`isDistributedEnabled failed, code is ${err.code}, message is ${err.message}`);
  } else {
    console.info(`isDistributedEnabled success ${JSON.stringify(data)}`);
  }
};
notificationManager.isDistributedEnabled(isDistributedEnabledCallback);
```

#### notificationManager.isDistributedEnabled

isDistributedEnabled(): Promise<boolean>

查询设备是否支持跨设备协同通知。使用Promise异步回调。

**设备行为差异**：该接口在Wearable/TV中回调返回恒为false，在其他设备类型中回调正常。

**系统能力**：SystemCapability.Notification.Notification

**返回值：**

类型说明Promise<boolean>Promise对象。返回true表示支持跨设备协同通知；返回false表示不支持跨设备协同通知。

**错误码：**

以下错误码的详细介绍请参见[通知错误码](../../errors/通知错误码.md)。

错误码ID错误信息1600001Internal error.1600002Marshalling or unmarshalling error.1600003Failed to connect to the service.1600010Distributed operation failed.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

notificationManager.isDistributedEnabled().then((data: boolean) => {
  console.info(`isDistributedEnabled success, data: ${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
  console.error(`isDistributedEnabled failed, code is ${err.code}, message is ${err.message}`);
});
```

#### notificationManager.openNotificationSettings13+

openNotificationSettings(context: UIAbilityContext): Promise<void>

拉起应用的通知设置界面，该页面以半模态形式呈现，可用于设置通知开关、通知提醒方式等。使用Promise异步回调。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Notification.NotificationSettings

**参数：**

参数名类型必填说明context[UIAbilityContext](../../topics/graphics/UIAbilityContext.md)是通知设置页面绑定Ability的上下文。

**返回值：**

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[通知错误码](../../errors/通知错误码.md)。

错误码ID错误信息801Capability not supported.1600001Internal error.1600003Failed to connect to the service.1600018The notification settings window is already displayed.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { hilog } from '@kit.PerformanceAnalysisKit';

class MyAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');
    windowStage.loadContent('pages/Index', (err, data) => {
      if (err.code) {
        hilog.error(0x0000, 'testTag', `Failed to load the content. Cause: ${JSON.stringify(err) ?? ''}`);
        return;
      }
      hilog.info(0x0000, 'testTag', `Succeeded in loading the content. Data: ${JSON.stringify(data) ?? ''}`);
      notificationManager.openNotificationSettings(this.context).then(() => {
        hilog.info(0x0000, 'testTag', `[ANS] openNotificationSettings success`);
      }).catch((err: BusinessError) => {
        hilog.error(0x0000, 'testTag', `[ANS] openNotificationSettings failed, code is ${err.code}, message is ${err.message}`);
      });
    });
  }
}
```

#### notificationManager.getNotificationSetting20+

getNotificationSetting(): Promise<NotificationSetting>

获取应用程序的通知设置。使用Promise异步回调。

**系统能力**：SystemCapability.Notification.Notification

**返回值：**

类型说明Promise<[NotificationSetting](#ZH-CN_TOPIC_0000002497446132__notificationsetting20)>Promise对象，返回此应用程序的通知设置。

**错误码：**

以下错误码的详细介绍请参见[通知错误码](../../errors/通知错误码.md)。

错误码ID错误信息1600001Internal error.1600002Marshalling or unmarshalling error.1600003Failed to connect to the service.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

notificationManager.getNotificationSetting().then((data: notificationManager.NotificationSetting) => {
    console.info(`getNotificationSetting success, data: ${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
    console.error(`getNotificationSetting failed, code is ${err.code}, message is ${err.message}`);
});
```

#### ContentType

通知内容类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Notification.Notification

名称值说明NOTIFICATION_CONTENT_BASIC_TEXT0普通文本类型通知。NOTIFICATION_CONTENT_LONG_TEXT1长文本类型通知。NOTIFICATION_CONTENT_PICTURE2图片类型通知。NOTIFICATION_CONTENT_CONVERSATION3社交类型通知。预留能力，暂未支持。NOTIFICATION_CONTENT_MULTILINE4多行文本类型通知。NOTIFICATION_CONTENT_SYSTEM_LIVE_VIEW11+5系统实况窗类型通知。不支持三方应用直接创建该类型通知。系统代理创建系统实况窗类型通知后，三方应用可以通过发布相同ID的通知来更新指定内容。NOTIFICATION_CONTENT_LIVE_VIEW11+6普通实况窗类型通知。仅系统应用可用。

#### SlotLevel

通知级别。

**系统能力**：SystemCapability.Notification.Notification

名称值说明LEVEL_NONE0表示关闭通知功能。LEVEL_MIN1表示通知功能已启用，状态栏中不显示通知图标，无横幅，无提示音。LEVEL_LOW2表示通知功能已启用，状态栏中显示通知图标，无横幅，无提示音。LEVEL_DEFAULT3表示通知功能已启用，状态栏中显示通知图标，无横幅，有提示音。LEVEL_HIGH4表示通知功能已启用，状态栏中显示通知图标，有横幅，有提示音。

#### SlotType

通知渠道类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Notification.Notification

名称值说明UNKNOWN_TYPE0未知类型。该类型对应[SlotLevel](#ZH-CN_TOPIC_0000002497446132__slotlevel)为LEVEL_MIN。SOCIAL_COMMUNICATION1社交通信。该类型对应[SlotLevel](#ZH-CN_TOPIC_0000002497446132__slotlevel)为LEVEL_HIGH。SERVICE_INFORMATION2服务提醒。该类型对应[SlotLevel](#ZH-CN_TOPIC_0000002497446132__slotlevel)为LEVEL_HIGH。CONTENT_INFORMATION3内容资讯。该类型对应[SlotLevel](#ZH-CN_TOPIC_0000002497446132__slotlevel)为LEVEL_MIN。LIVE_VIEW11+4实况窗。不支持三方应用直接创建该渠道类型通知，可以由系统代理创建后，三方应用发布同ID的通知来更新指定内容。该类型对应[SlotLevel](#ZH-CN_TOPIC_0000002497446132__slotlevel)为LEVEL_DEFAULT。CUSTOMER_SERVICE11+5客服消息。该类型用于用户与商家之间的客服消息，需由用户主动发起。该类型对应[SlotLevel](#ZH-CN_TOPIC_0000002497446132__slotlevel)为LEVEL_DEFAULT。OTHER_TYPES0xFFFF其他。该类型对应[SlotLevel](#ZH-CN_TOPIC_0000002497446132__slotlevel)为LEVEL_MIN。

#### NotificationSetting20+

通知设置状态，包括是否开启振动、是否开启响铃。

**系统能力**：SystemCapability.Notification.Notification

名称类型只读可选说明vibrationEnabledboolean否否

表示是否开启振动。

 - true：开启。

 - false：关闭。

soundEnabledboolean否否

表示是否开启响铃。

 - true：开启。

 - false：关闭。

#### BundleOption

type BundleOption = _BundleOption

指定应用的包信息。

**系统能力**： SystemCapability.Notification.Notification

类型说明[_BundleOption](../../topics/misc/NotificationCommonDef.md#ZH-CN_TOPIC_0000002529446079__bundleoption)指定应用的包信息。

#### NotificationActionButton

type NotificationActionButton = _NotificationActionButton

通知中显示的操作按钮。

**系统能力**： SystemCapability.Notification.Notification

类型说明[_NotificationActionButton](../../topics/components/NotificationActionButton.md)通知中显示的操作按钮。

#### NotificationBasicContent

type NotificationBasicContent = _NotificationBasicContent

普通文本通知。

**系统能力**： SystemCapability.Notification.Notification

类型说明[_NotificationBasicContent](../../topics/misc/NotificationContent.md#ZH-CN_TOPIC_0000002497606116__notificationbasiccontent)描述普通文本通知。

#### NotificationContent

type NotificationContent = _NotificationContent

通知内容。

**系统能力**： SystemCapability.Notification.Notification

类型说明[_NotificationContent](../../topics/misc/NotificationContent.md#ZH-CN_TOPIC_0000002497606116__notificationcontent-1)描述通知内容。

#### NotificationLongTextContent

type NotificationLongTextContent = _NotificationLongTextContent

长文本通知。

**系统能力**： SystemCapability.Notification.Notification

类型说明[_NotificationLongTextContent](../../topics/misc/NotificationContent.md#ZH-CN_TOPIC_0000002497606116__notificationlongtextcontent)描述长文本通知。

#### NotificationMultiLineContent

type NotificationMultiLineContent = _NotificationMultiLineContent

多行文本通知。

**系统能力**： SystemCapability.Notification.Notification

类型说明[_NotificationMultiLineContent](../../topics/misc/NotificationContent.md#ZH-CN_TOPIC_0000002497606116__notificationmultilinecontent)描述多行文本通知。

#### NotificationPictureContent

type NotificationPictureContent = _NotificationPictureContent

附有图片的通知。

**系统能力**： SystemCapability.Notification.Notification

类型说明[_NotificationPictureContent](../../topics/misc/NotificationContent.md#ZH-CN_TOPIC_0000002497606116__notificationpicturecontent)附有图片的通知。

#### NotificationSystemLiveViewContent11+

type NotificationSystemLiveViewContent = _NotificationSystemLiveViewContent

系统实况窗通知内容。

**系统能力**： SystemCapability.Notification.Notification

类型说明[_NotificationSystemLiveViewContent](../../topics/misc/NotificationContent.md#ZH-CN_TOPIC_0000002497606116__notificationsystemliveviewcontent)系统实况窗通知内容。

#### NotificationRequest

type NotificationRequest = _NotificationRequest

通知请求。

**系统能力**： SystemCapability.Notification.Notification

类型说明[_NotificationRequest](../../topics/misc/NotificationRequest.md#ZH-CN_TOPIC_0000002497606118__notificationrequest-1)通知请求。

#### DistributedOptions

type DistributedOptions = _DistributedOptions

分布式选项。

**系统能力**： SystemCapability.Notification.Notification

类型说明[_DistributedOptions](../../topics/misc/NotificationRequest.md#ZH-CN_TOPIC_0000002497606118__distributedoptions8)分布式选项。

#### NotificationSlot

type NotificationSlot = _NotificationSlot

通知渠道。

**系统能力**： SystemCapability.Notification.Notification

类型说明[_NotificationSlot](../../topics/misc/NotificationSlot.md)通知渠道。

#### NotificationTemplate

type NotificationTemplate = _NotificationTemplate

通知模板。

**系统能力**： SystemCapability.Notification.Notification

类型说明[_NotificationTemplate](../../topics/misc/NotificationTemplate.md)通知模板。

#### NotificationUserInput

type NotificationUserInput = _NotificationUserInput

保存用户输入的通知消息。

**系统能力**： SystemCapability.Notification.Notification

类型说明[_NotificationUserInput](../../topics/input/NotificationUserInput.md)保存用户输入的通知消息。

#### NotificationCapsule11+

type NotificationCapsule = _NotificationCapsule

通知胶囊。

**系统能力**： SystemCapability.Notification.Notification

类型说明[_NotificationCapsule](../../topics/misc/NotificationContent.md#ZH-CN_TOPIC_0000002497606116__notificationcapsule11)通知胶囊。

#### NotificationButton11+

type NotificationButton = _NotificationButton

通知按钮。

**系统能力**： SystemCapability.Notification.Notification

类型说明[_NotificationButton](../../topics/misc/NotificationContent.md#ZH-CN_TOPIC_0000002497606116__notificationbutton11)通知按钮。

#### NotificationTime11+

type NotificationTime = _NotificationTime

通知计时信息。

**系统能力**： SystemCapability.Notification.Notification

类型说明[_NotificationTime](../../topics/misc/NotificationContent.md#ZH-CN_TOPIC_0000002497606116__notificationtime11)描述通知计时信息。

#### NotificationProgress11+

type NotificationProgress = _NotificationProgress

通知进度。

**系统能力**： SystemCapability.Notification.Notification

类型说明[_NotificationProgress](../../topics/misc/NotificationContent.md#ZH-CN_TOPIC_0000002497606116__notificationprogress11)描述通知进度。