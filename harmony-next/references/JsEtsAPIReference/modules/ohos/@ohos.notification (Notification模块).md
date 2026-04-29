# @ohos.notification (Notification模块)

本模块提供通知管理的能力，包括发布、取消发布通知，创建、获取、移除通知通道，订阅、取消订阅通知，获取通知的使能状态、角标使能状态，获取通知的相关信息等。

从API version 9开始，该接口不再维护，推荐使用新接口[@ohos.notificationManager](@ohos.notificationManager (NotificationManager模块).md)。

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

通知订阅和取消订阅仅对系统应用开放。

#### 导入模块

```ets
import Notification from '@ohos.notification';
```

#### Notification.publish

publish(request: NotificationRequest, callback: AsyncCallback<void>): void

发布通知（callback形式）。

**系统能力**：SystemCapability.Notification.Notification

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| request | NotificationRequest | 是 | 用于设置要发布通知的内容和相关配置信息。 |
| callback | AsyncCallback<void> | 是 | 发布通知的回调方法。 |

**示例：**

```ets
import NotificationManager from '@ohos.notificationManager';
import Base from '@ohos.base';

// publish回调
let publishCallback = (err: Base.BusinessError) => {
  if (err) {
    console.error(`publish failed, code is ${err}`);
  } else {
    console.info("publish success");
  }
// 通知Request对象
let notificationRequest: NotificationManager.NotificationRequest = {
  id: 1,
  content: {
    contentType: Notification.ContentType.NOTIFICATION_CONTENT_BASIC_TEXT,
    normal: {
      title: "test_title",
      text: "test_text",
      additionalText: "test_additionalText"
    }
};
Notification.publish(notificationRequest, publishCallback);
```

#### Notification.publish

publish(request: NotificationRequest): Promise<void>

发布通知（Promise形式）。

**系统能力**：SystemCapability.Notification.Notification

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| request | NotificationRequest | 是 | 用于设置要发布通知的内容和相关配置信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```ets
import NotificationManager from '@ohos.notificationManager';
import Base from '@ohos.base';

// 通知Request对象
let notificationRequest: NotificationManager.NotificationRequest = {
  id: 1,
  content: {
    contentType: Notification.ContentType.NOTIFICATION_CONTENT_BASIC_TEXT,
    normal: {
      title: "test_title",
      text: "test_text",
      additionalText: "test_additionalText"
    }
};
Notification.publish(notificationRequest).then(() => {
  console.info("publish success");
}).catch((err: Base.BusinessError) => {
  console.error(`publish failed, code is ${err}`);
});
```

#### Notification.cancel

cancel(id: number, label: string, callback: AsyncCallback<void>): void

通过通知ID和通知标签取消已发布的通知（callback形式）。

**系统能力**：SystemCapability.Notification.Notification

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | number | 是 | 通知ID。 |
| label | string | 是 | 通知标签。 |
| callback | AsyncCallback<void> | 是 | 表示被指定的回调方法。 |

**示例：**

```ets
import Base from '@ohos.base';

// cancel回调
let cancelCallback = (err: Base.BusinessError) => {
  if (err) {
    console.info("cancel failed " + JSON.stringify(err));
  } else {
    console.info("cancel success");
  }
Notification.cancel(0, "label", cancelCallback);
```

#### Notification.cancel

cancel(id: number, label?: string): Promise<void>

取消与指定通知ID相匹配的已发布通知，label可以指定也可以不指定（Promise形式）。

**系统能力**：SystemCapability.Notification.Notification

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | number | 是 | 通知ID。 |
| label | string | 否 | 通知标签，默认为空。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```ets
import Base from '@ohos.base';

Notification.cancel(0).then(() => {
  console.info("cancel success");
}).catch((err: Base.BusinessError) => {
  console.error(`cancel failed, code is ${err}`);
});
```

#### Notification.cancel

cancel(id: number, callback: AsyncCallback<void>): void

取消与指定通知ID相匹配的已发布通知（callback形式）。

**系统能力**：SystemCapability.Notification.Notification

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | number | 是 | 通知ID。 |
| callback | AsyncCallback<void> | 是 | 表示被指定的回调方法。 |

**示例：**

```ets
import Base from '@ohos.base';

// cancel回调
let cancelCallback = (err: Base.BusinessError) => {
  if (err) {
    console.info("cancel failed " + JSON.stringify(err));
  } else {
    console.info("cancel success");
  }
Notification.cancel(0, cancelCallback);
```

#### Notification.cancelAll

cancelAll(callback: AsyncCallback<void>): void

取消所有已发布的通知（callback形式）。

**系统能力**：SystemCapability.Notification.Notification

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 表示被指定的回调方法。 |

**示例：**

```ets
import Base from '@ohos.base';

// cancel回调
let cancelAllCallback = (err: Base.BusinessError) => {
  if (err) {
    console.info("cancelAll failed " + JSON.stringify(err));
  } else {
    console.info("cancelAll success");
  }
Notification.cancelAll(cancelAllCallback);
```

#### Notification.cancelAll

cancelAll(): Promise<void>

取消所有已发布的通知（Promise形式）。

**系统能力**：SystemCapability.Notification.Notification

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```ets
import Base from '@ohos.base';

Notification.cancelAll().then(() => {
  console.info("cancelAll success");
}).catch((err: Base.BusinessError) => {
  console.error(`cancelAll failed, code is ${err}`);
});
```

#### Notification.addSlot

addSlot(type: SlotType, callback: AsyncCallback<void>): void

创建指定类型的通知通道（callback形式）。

**系统能力**：SystemCapability.Notification.Notification

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | SlotType | 是 | 要创建的通知通道的类型。 |
| callback | AsyncCallback<void> | 是 | 表示被指定的回调方法。 |

**示例：**

```ets
import Base from '@ohos.base';

// addslot回调
let addSlotCallBack = (err: Base.BusinessError) => {
  if (err) {
    console.info("addSlot failed " + JSON.stringify(err));
  } else {
    console.info("addSlot success");
  }
Notification.addSlot(Notification.SlotType.SOCIAL_COMMUNICATION, addSlotCallBack);
```

#### Notification.addSlot

addSlot(type: SlotType): Promise<void>

创建指定类型的通知通道（Promise形式）。

**系统能力**：SystemCapability.Notification.Notification

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | SlotType | 是 | 要创建的通知通道的类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```ets
import Base from '@ohos.base';

Notification.addSlot(Notification.SlotType.SOCIAL_COMMUNICATION).then(() => {
  console.info("addSlot success");
}).catch((err: Base.BusinessError) => {
  console.error(`addSlot failed, code is ${err}`);
});
```

#### Notification.getSlot

getSlot(slotType: SlotType, callback: AsyncCallback<NotificationSlot>): void

获取一个指定类型的通知通道（callback形式）。

**系统能力**：SystemCapability.Notification.Notification

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotType | SlotType | 是 | 通知渠道类型，目前分为社交通信、服务提醒、内容咨询和其他类型。 |
| callback | AsyncCallback<NotificationSlot> | 是 | 表示被指定的回调方法。 |

**示例：**

```ets
import Base from '@ohos.base';

// getSlot回调
let getSlotCallback = (err: Base.BusinessError) => {
  if (err) {
    console.info("getSlot failed " + JSON.stringify(err));
  } else {
    console.info("getSlot success");
  }
let slotType: Notification.SlotType = Notification.SlotType.SOCIAL_COMMUNICATION;
Notification.getSlot(slotType, getSlotCallback);
```

#### Notification.getSlot

getSlot(slotType: SlotType): Promise<NotificationSlot>

获取一个指定类型的通知通道（Promise形式）。

**系统能力**：SystemCapability.Notification.Notification

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotType | SlotType | 是 | 通知渠道类型，目前分为社交通信、服务提醒、内容咨询和其他类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<NotificationSlot> | 以Promise形式返回获取一个通知通道。 |

**示例：**

```ets
import Base from '@ohos.base';

let slotType: Notification.SlotType = Notification.SlotType.SOCIAL_COMMUNICATION;
Notification.getSlot(slotType).then((data) => {
  console.info("getSlot success, data: " + JSON.stringify(data));
}).catch((err: Base.BusinessError) => {
  console.error(`getSlot failed, code is ${err}`);
});
```

#### Notification.getSlots

getSlots(callback: AsyncCallback<Array<NotificationSlot>>): void

获取此应用程序的所有通知通道（callback形式）。

**系统能力**：SystemCapability.Notification.Notification

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<Array<NotificationSlot>> | 是 | 以callback形式返回获取此应用程序的所有通知通道的结果。 |

**示例：**

```ets
import Base from '@ohos.base';

// getSlots回调
function getSlotsCallback(err: Base.BusinessError) {
  if (err) {
    console.info("getSlots failed " + JSON.stringify(err));
  } else {
    console.info("getSlots success");
  }
Notification.getSlots(getSlotsCallback);
```

#### Notification.getSlots

getSlots(): Promise<Array<NotificationSlot>>

获取此应用程序的所有通知通道（Promise形式）。

**系统能力**：SystemCapability.Notification.Notification

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<NotificationSlot>> | 以Promise形式返回获取此应用程序的所有通知通道的结果。 |

**示例：**

```ets
import Base from '@ohos.base';

Notification.getSlots().then((data) => {
  console.info("getSlots success, data: " + JSON.stringify(data));
}).catch((err: Base.BusinessError) => {
  console.error(`getSlots failed, code is ${err}`);
});
```

#### Notification.removeSlot

removeSlot(slotType: SlotType, callback: AsyncCallback<void>): void

删除指定类型的通知通道（callback形式）。

**系统能力**：SystemCapability.Notification.Notification

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotType | SlotType | 是 | 通知渠道类型,目前分为社交通信、服务提醒、内容咨询和其他类型。 |
| callback | AsyncCallback<void> | 是 | 表示被指定的回调方法。 |

**示例：**

```ets
import Base from '@ohos.base';

// removeSlot回调
let removeSlotCallback = (err: Base.BusinessError) => {
  if (err) {
    console.info("removeSlot failed " + JSON.stringify(err));
  } else {
    console.info("removeSlot success");
  }
let slotType: Notification.SlotType = Notification.SlotType.SOCIAL_COMMUNICATION;
Notification.removeSlot(slotType, removeSlotCallback);
```

#### Notification.removeSlot

removeSlot(slotType: SlotType): Promise<void>

删除指定类型的通知通道（Promise形式）。

**系统能力**：SystemCapability.Notification.Notification

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotType | SlotType | 是 | 通知渠道类型,目前分为社交通信、服务提醒、内容咨询和其他类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```ets
import Base from '@ohos.base';

let slotType: Notification.SlotType = Notification.SlotType.SOCIAL_COMMUNICATION;
Notification.removeSlot(slotType).then(() => {
  console.info("removeSlot success");
}).catch((err: Base.BusinessError) => {
  console.error(`removeSlot failed, code is ${err}`);
});
```

#### Notification.removeAllSlots

removeAllSlots(callback: AsyncCallback<void>): void

删除所有通知通道（callback形式）。

**系统能力**：SystemCapability.Notification.Notification

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 表示被指定的回调方法。 |

**示例：**

```ets
import Base from '@ohos.base';

let removeAllCallBack = (err: Base.BusinessError) => {
  if (err) {
    console.info("removeAllSlots failed " + JSON.stringify(err));
  } else {
    console.info("removeAllSlots success");
  }
Notification.removeAllSlots(removeAllCallBack);
```

#### Notification.removeAllSlots

removeAllSlots(): Promise<void>

删除所有通知通道（Promise形式）。

**系统能力**：SystemCapability.Notification.Notification

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```ets
import Base from '@ohos.base';

Notification.removeAllSlots().then(() => {
  console.info("removeAllSlots success");
}).catch((err: Base.BusinessError) => {
  console.error(`removeAllSlots failed, code is ${err}`);
});
```

#### Notification.getActiveNotificationCount

getActiveNotificationCount(callback: AsyncCallback<number>): void

获取当前应用未删除的通知数（Callback形式）。

**系统能力**：SystemCapability.Notification.Notification

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<number> | 是 | 获取未删除通知数回调函数。 |

**示例：**

```ets
import Base from '@ohos.base';

let getActiveNotificationCountCallback = (err: Base.BusinessError, data: number) => {
  if (err) {
    console.info("getActiveNotificationCount failed " + JSON.stringify(err));
  } else {
    console.info("getActiveNotificationCount success");
  }

Notification.getActiveNotificationCount(getActiveNotificationCountCallback);
```

#### Notification.getActiveNotificationCount

getActiveNotificationCount(): Promise<number>

获取当前应用未删除的通知数（Promise形式）。

**系统能力**：SystemCapability.Notification.Notification

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | 以Promise形式返回获取当前应用未删除通知数。 |

**示例：**

```ets
import Base from '@ohos.base';

Notification.getActiveNotificationCount().then((data: number) => {
  console.info("getActiveNotificationCount success, data: " + JSON.stringify(data));
}).catch((err: Base.BusinessError) => {
  console.error(`getAllActiveNotifications failed, code is ${err}`);
});
```

#### Notification.getActiveNotifications

getActiveNotifications(callback: AsyncCallback<Array<NotificationRequest>>): void

获取当前应用未删除的通知列表（Callback形式）。

**系统能力**：SystemCapability.Notification.Notification

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<Array<NotificationRequest>> | 是 | 获取当前应用通知列表回调函数。 |

**示例：**

```ets
import Base from '@ohos.base';
import NotificationManager from '@ohos.notificationManager';

let getActiveNotificationsCallback = (err: Base.BusinessError, data: NotificationManager.NotificationRequest[]) => {
  if (err) {
    console.info("getActiveNotifications failed " + JSON.stringify(err));
  } else {
    console.info("getActiveNotifications success");
  }

Notification.getActiveNotifications(getActiveNotificationsCallback);
```

#### Notification.getActiveNotifications

getActiveNotifications(): Promise<Array<[NotificationRequest](#ZH-CN_TOPIC_0000002522082432__notificationrequest)>>

获取当前应用未删除的通知列表（Promise形式）。

**系统能力**：SystemCapability.Notification.Notification

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<NotificationRequest>> | 以Promise形式返回获取当前应用通知列表。 |

**示例：**

```ets
import Base from '@ohos.base';
import NotificationManager from '@ohos.notificationManager';

Notification.getActiveNotifications().then((data: NotificationManager.NotificationRequest[]) => {
  console.info("removeGroupByBundle success, data: " + JSON.stringify(data));
}).catch((err: Base.BusinessError) => {
  console.error(`removeGroupByBundle failed, code is ${err}`);
});
```

#### Notification.cancelGroup8+

cancelGroup(groupName: string, callback: AsyncCallback<void>): void

取消本应用指定组下的通知（Callback形式）。

**系统能力**：SystemCapability.Notification.Notification

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| groupName | string | 是 | 通知组名称，此名称需要在发布通知时通过NotificationRequest对象指定。 |
| callback | AsyncCallback<void> | 是 | 取消本应用指定组下通知的回调函数。 |

**示例：**

```ets
import Base from '@ohos.base';

let cancelGroupCallback = (err: Base.BusinessError) => {
  if (err) {
    console.info("cancelGroup failed " + JSON.stringify(err));
  } else {
    console.info("cancelGroup success");
  }

let groupName: string = "GroupName";

Notification.cancelGroup(groupName, cancelGroupCallback);
```

#### Notification.cancelGroup8+

cancelGroup(groupName: string): Promise<void>

取消本应用指定组下的通知（Promise形式）。

**系统能力**：SystemCapability.Notification.Notification

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| groupName | string | 是 | 通知组名称。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```ets
import Base from '@ohos.base';

let groupName: string = "GroupName";
Notification.cancelGroup(groupName).then(() => {
  console.info("cancelGroup success");
}).catch((err: Base.BusinessError) => {
  console.error(`cancelGroup failed, code is ${err}`);
});
```

#### Notification.isSupportTemplate8+

isSupportTemplate(templateName: string, callback: AsyncCallback<boolean>): void

查询模板是否存在（Callback形式）。

**系统能力**：SystemCapability.Notification.Notification

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| templateName | string | 是 | 模板名称。 |
| callback | AsyncCallback<boolean> | 是 | 查询模板是否存在的回调函数。 |

**示例：**

```ets
import Base from '@ohos.base';

let templateName: string = 'process';
function isSupportTemplateCallback(err: Base.BusinessError, data: boolean) {
  if (err) {
    console.info("isSupportTemplate failed " + JSON.stringify(err));
  } else {
    console.info("isSupportTemplate success");
  }

Notification.isSupportTemplate(templateName, isSupportTemplateCallback);
```

#### Notification.isSupportTemplate8+

isSupportTemplate(templateName: string): Promise<boolean>

查询模板是否存在（Promise形式）。

**系统能力**：SystemCapability.Notification.Notification

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| templateName | string | 是 | 模板名称。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise方式返回模板是否存在的结果。 |

**示例：**

```ets
import Base from '@ohos.base';

let templateName: string = 'process';
Notification.isSupportTemplate(templateName).then((data: boolean) => {
  console.info("isSupportTemplate success, data: " + JSON.stringify(data));
}).catch((err: Base.BusinessError) => {
  console.error(`isSupportTemplate failed, code is ${err}`);
});
```

#### Notification.requestEnableNotification8+

requestEnableNotification(callback: AsyncCallback<void>): void

应用请求通知使能（Callback形式）。

**系统能力**：SystemCapability.Notification.Notification

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 应用请求通知使能的回调函数。 |

**示例：**

```ets
import Base from '@ohos.base';

let requestEnableNotificationCallback = (err: Base.BusinessError) => {
  if (err) {
    console.info("requestEnableNotification failed " + JSON.stringify(err));
  } else {
    console.info("requestEnableNotification success");
  }
};

Notification.requestEnableNotification(requestEnableNotificationCallback);
```

#### Notification.requestEnableNotification8+

requestEnableNotification(): Promise<void>

应用请求通知使能（Promise形式）。

**系统能力**：SystemCapability.Notification.Notification

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```ets
import Base from '@ohos.base';

Notification.requestEnableNotification().then(() => {
  console.info("requestEnableNotification success");
}).catch((err: Base.BusinessError) => {
  console.error(`requestEnableNotification failed, code is ${err}`);
});
```

#### Notification.isDistributedEnabled8+

isDistributedEnabled(callback: AsyncCallback<boolean>): void

查询设备是否支持分布式通知（Callback形式）。

**系统能力**：SystemCapability.Notification.Notification

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<boolean> | 是 | 设备是否支持分布式通知的回调函数。 |

**示例：**

```ets
import Base from '@ohos.base';

let isDistributedEnabledCallback = (err: Base.BusinessError, data: boolean) => {
  if (err) {
    console.info("isDistributedEnabled failed " + JSON.stringify(err));
  } else {
    console.info("isDistributedEnabled success " + JSON.stringify(data));
  }
};

Notification.isDistributedEnabled(isDistributedEnabledCallback);
```

#### Notification.isDistributedEnabled8+

isDistributedEnabled(): Promise<boolean>

查询设备是否支持分布式通知（Promise形式）。

**系统能力**：SystemCapability.Notification.Notification

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise方式返回设备是否支持分布式通知的结果。 |

**示例：**

```ets
import Base from '@ohos.base';

Notification.isDistributedEnabled().then((data: boolean) => {
    console.info("isDistributedEnabled success, data: " + JSON.stringify(data));
}).catch((err: Base.BusinessError) => {
  console.error(`isDistributedEnabled failed, code is ${err}`);
});
```

#### ContentType

**系统能力**：SystemCapability.Notification.Notification

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NOTIFICATION_CONTENT_BASIC_TEXT | NOTIFICATION_CONTENT_BASIC_TEXT | 普通类型通知。 |
| NOTIFICATION_CONTENT_LONG_TEXT | NOTIFICATION_CONTENT_LONG_TEXT | 长文本类型通知。 |
| NOTIFICATION_CONTENT_PICTURE | NOTIFICATION_CONTENT_PICTURE | 图片类型通知。 |
| NOTIFICATION_CONTENT_CONVERSATION | NOTIFICATION_CONTENT_CONVERSATION | 社交类型通知。 |
| NOTIFICATION_CONTENT_MULTILINE | NOTIFICATION_CONTENT_MULTILINE | 多行文本类型通知。 |

#### SlotLevel

**系统能力**：SystemCapability.Notification.Notification

| 名称 | 值 | 说明 |
| --- | --- | --- |
| LEVEL_NONE | 0 | 表示关闭通知功能。 |
| LEVEL_MIN | 1 | 表示通知功能已启用，但状态栏中不显示通知图标，且没有横幅或提示音。 |
| LEVEL_LOW | 2 | 表示通知功能已启用，且状态栏中显示通知图标，但没有横幅或提示音。 |
| LEVEL_DEFAULT | 3 | 表示通知功能已启用，状态栏中显示通知图标，没有横幅但有提示音。 |
| LEVEL_HIGH | 4 | 表示通知功能已启用，状态栏中显示通知图标，有横幅和提示音。 |

#### BundleOptiondeprecated

**系统能力**：SystemCapability.Notification.Notification


从 API version 7开始支持，从API version 9开始废弃。建议使用[notificationManager.BundleOption](NotificationCommonDef.md#ZH-CN_TOPIC_0000002553362347__bundleoption)替代。

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bundle | string | 是 | 应用的包信息。 |
| uid | number | 否 | 用户ID，默认为0。 |

#### NotificationKeydeprecated

**系统能力**：SystemCapability.Notification.Notification


从 API version 7开始支持，从API version 9开始废弃。

| 名称 | 类型 | 可读 | 可写 | 说明 |
| --- | --- | --- | --- | --- |
| id | number | 是 | 是 | 通知ID。 |
| label | string | 是 | 是 | 通知标签。 |

#### SlotType

**系统能力**：SystemCapability.Notification.Notification

| 名称 | 值 | 说明 |
| --- | --- | --- |
| UNKNOWN_TYPE | 0 | 未知类型。 |
| SOCIAL_COMMUNICATION | 1 | 社交类型。 |
| SERVICE_INFORMATION | 2 | 服务类型。 |
| CONTENT_INFORMATION | 3 | 内容类型。 |
| OTHER_TYPES | 0xFFFF | 其他类型。 |

#### NotificationActionButton

描述通知中显示的操作按钮。

**系统能力**：SystemCapability.Notification.Notification

| 名称 | 类型 | 可读 | 可写 | 说明 |
| --- | --- | --- | --- | --- |
| title | string | 是 | 是 | 按钮标题。 |
| wantAgent | WantAgent | 是 | 是 | 点击按钮时触发的WantAgent。 |
| extras | { [key: string]: any } | 是 | 是 | 按钮扩展信息。 |
| userInput8+ | NotificationUserInput | 是 | 是 | 用户输入对象实例。 |

#### NotificationBasicContent

描述普通文本通知。

**系统能力**：SystemCapability.Notification.Notification

| 名称 | 类型 | 可读 | 可写 | 说明 |
| --- | --- | --- | --- | --- |
| title | string | 是 | 是 | 通知标题。 |
| text | string | 是 | 是 | 通知内容。 |
| additionalText | string | 是 | 是 | 通知附加内容，是对通知内容的补充。 |

#### NotificationLongTextContent

描述长文本通知。

**系统能力**：SystemCapability.Notification.Notification

| 名称 | 类型 | 可读 | 可写 | 说明 |
| --- | --- | --- | --- | --- |
| title | string | 是 | 是 | 通知标题。 |
| text | string | 是 | 是 | 通知内容。 |
| additionalText | string | 是 | 是 | 通知附加内容，是对通知内容的补充。 |
| longText | string | 是 | 是 | 通知的长文本。 |
| briefText | string | 是 | 是 | 通知概要内容，是对通知内容的总结。 |
| expandedTitle | string | 是 | 是 | 通知展开时的标题。 |

#### NotificationMultiLineContent

描述多行文本通知。

**系统能力**：SystemCapability.Notification.Notification

| 名称 | 类型 | 可读 | 可写 | 说明 |
| --- | --- | --- | --- | --- |
| title | string | 是 | 是 | 通知标题。 |
| text | string | 是 | 是 | 通知内容。 |
| additionalText | string | 是 | 是 | 通知附加内容，是对通知内容的补充。 |
| briefText | string | 是 | 是 | 通知概要内容，是对通知内容的总结。 |
| longTitle | string | 是 | 是 | 通知展开时的标题。 |
| lines | Array<string> | 是 | 是 | 通知的多行文本。 |

#### NotificationPictureContent

描述附有图片的通知。

**系统能力**：SystemCapability.Notification.Notification

| 名称 | 类型 | 可读 | 可写 | 说明 |
| --- | --- | --- | --- | --- |
| title | string | 是 | 是 | 通知标题。 |
| text | string | 是 | 是 | 通知内容。 |
| additionalText | string | 是 | 是 | 通知附加内容，是对通知内容的补充。 |
| briefText | string | 是 | 是 | 通知概要内容，是对通知内容的总结。 |
| expandedTitle | string | 是 | 是 | 通知展开时的标题。 |
| picture | image.PixelMap | 是 | 是 | 通知的图片内容。 |

#### NotificationContent

描述通知类型。

**系统能力**：SystemCapability.Notification.Notification

| 名称 | 类型 | 可读 | 可写 | 说明 |
| --- | --- | --- | --- | --- |
| contentType | notification.ContentType | 是 | 是 | 通知内容类型。 |
| normal | NotificationBasicContent | 是 | 是 | 基本类型通知内容。 |
| longText | NotificationLongTextContent | 是 | 是 | 长文本类型通知内容。 |
| multiLine | NotificationMultiLineContent | 是 | 是 | 多行类型通知内容。 |
| picture | NotificationPictureContent | 是 | 是 | 图片类型通知内容。 |

#### NotificationRequest

描述通知的请求。

**系统能力**：SystemCapability.Notification.Notification

| 名称 | 类型 | 可读 | 可写 | 说明 |
| --- | --- | --- | --- | --- |
| content | NotificationContent | 是 | 是 | 通知内容。 |
| id | number | 是 | 是 | 通知ID。 |
| slotType | notification.SlotType | 是 | 是 | 通道类型。 |
| isOngoing | boolean | 是 | 是 | 是否进行时通知。 |
| isUnremovable | boolean | 是 | 是 | 是否可移除。 |
| deliveryTime | number | 是 | 是 | 通知发送时间。 |
| tapDismissed | boolean | 是 | 是 | 通知是否自动清除。 |
| autoDeletedTime | number | 是 | 是 | 自动清除的时间。 |
| wantAgent | WantAgent | 是 | 是 | WantAgent封装了应用的行为意图，点击通知时触发该行为。 |
| extraInfo | {[key: string]: any} | 是 | 是 | 扩展参数。 |
| color | number | 是 | 是 | 通知背景颜色。预留能力，暂未支持。 |
| colorEnabled | boolean | 是 | 是 | 通知背景颜色是否使能。预留能力，暂未支持。 |
| isAlertOnce | boolean | 是 | 是 | 设置是否仅有一次此通知提醒。 |
| isStopwatch | boolean | 是 | 是 | 是否显示已用时间。 |
| isCountDown | boolean | 是 | 是 | 是否显示倒计时时间。 |
| isFloatingIcon | boolean | 是 | 是 | 是否显示状态栏图标。 |
| label | string | 是 | 是 | 通知标签。 |
| badgeIconStyle | number | 是 | 是 | 通知角标类型。 |
| showDeliveryTime | boolean | 是 | 是 | 是否显示分发时间。 |
| actionButtons | Array<NotificationActionButton> | 是 | 是 | 通知按钮，最多两个按钮。 |
| smallIcon | image.PixelMap | 是 | 是 | 通知小图标。可选字段，大小不超过30KB。 |
| largeIcon | image.PixelMap | 是 | 是 | 通知大图标。可选字段，大小不超过30KB。 |
| creatorBundleName | string | 是 | 否 | 创建通知的包名。 |
| creatorUid | number | 是 | 否 | 创建通知的UID。 |
| creatorPid | number | 是 | 否 | 创建通知的PID。 |
| creatorUserId8+ | number | 是 | 否 | 创建通知的UserId。 |
| hashCode | string | 是 | 否 | 通知唯一标识。 |
| groupName8+ | string | 是 | 是 | 组通知名称。 |
| template8+ | NotificationTemplate | 是 | 是 | 通知模板。 |
| distributedOption8+ | DistributedOptions | 是 | 是 | 分布式通知的选项。 |
| notificationFlags8+ | [NotificationFlags](../../topics/misc/NotificationFlags.md) | 是 | 否 | 获取NotificationFlags。 |
| removalWantAgent9+ | WantAgent | 是 | 是 | 当移除通知时，通知将被重定向到的WantAgent实例。 |
| badgeNumber9+ | number | 是 | 是 | 应用程序图标上显示的通知数。 |

#### DistributedOptions8+

描述分布式选项。

**系统能力**：SystemCapability.Notification.Notification

| 名称 | 类型 | 可读 | 可写 | 说明 |
| --- | --- | --- | --- | --- |
| isDistributed | boolean | 是 | 是 | 是否为分布式通知。 |
| supportDisplayDevices | Array<string> | 是 | 是 | 可以同步通知到的设备列表。 |
| supportOperateDevices | Array<string> | 是 | 是 | 可以打开通知的设备列表。 |

#### NotificationSlot

描述通知槽

**系统能力**：SystemCapability.Notification.Notification

| 名称 | 类型 | 可读 | 可写 | 说明 |
| --- | --- | --- | --- | --- |
| type | notification.SlotType | 是 | 是 | 通道类型。 |
| level | notification.SlotLevel | 是 | 是 | 通知级别，不设置则根据通知渠道类型有默认值。 |
| desc | string | 是 | 是 | 通知渠道描述信息。 |
| badgeFlag | boolean | 是 | 是 | 是否显示角标。 |
| bypassDnd | boolean | 是 | 是 | 设置是否在系统中绕过免打扰模式。 |
| lockscreenVisibility | number | 是 | 是 | 在锁定屏幕上显示通知的模式。 |
| vibrationEnabled | boolean | 是 | 是 | 是否可振动。 |
| sound | string | 是 | 是 | 通知提示音。 |
| lightEnabled | boolean | 是 | 是 | 是否闪灯。 |
| lightColor | number | 是 | 是 | 通知灯颜色。 |
| vibrationValues | Array<number> | 是 | 是 | 通知振动样式。 |
| enabled9+ | boolean | 是 | 否 | 此通知插槽中的启停状态。 |

#### NotificationTemplate8+

通知模板。

**系统能力**：SystemCapability.Notification.Notification

| 名称 | 类型 | 可读 | 可写 | 说明 |
| --- | --- | --- | --- | --- |
| name | string | 是 | 是 | 模板名称。 |
| data | Record<string, Object> | 是 | 是 | 模板数据。 |

#### NotificationUserInput8+

保存用户输入的通知消息。

**系统能力**：SystemCapability.Notification.Notification

| 名称 | 类型 | 可读 | 可写 | 说明 |
| --- | --- | --- | --- | --- |
| inputKey | string | 是 | 是 | 用户输入时用于标识此输入的key。 |