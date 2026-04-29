# @ohos.reminderAgentManager (后台代理提醒)

本模块提供后台代理提醒的能力，即当应用被冻结或应用退出时，定时提醒功能将被系统服务代理。开发者可以调用本模块接口创建定时提醒，提醒类型支持倒计时、日历、闹钟三种。开发指导请参考[代理提醒开发指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agent-powered-reminder)。

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { reminderAgentManager } from '@kit.BackgroundTasksKit';
```

#### reminderAgentManager.publishReminder

publishReminder(reminderReq: ReminderRequest, callback: AsyncCallback<number>): void

发布后台代理提醒。使用callback异步回调。

代理提醒发布成功后，当到达设置的提醒时间点时，通知中心会弹出相应的提醒，此时如果[ReminderRequest.ringDuration](#ZH-CN_TOPIC_0000002522081202__reminderrequest)参数值大于0，则设置的自定义铃声默认在闹钟通道上播放，如果值不大于0，则不播放自定义铃声。


该接口需要申请通知弹窗权限[notificationManager.requestEnableNotification](@ohos.notificationManager (NotificationManager模块).md#ZH-CN_TOPIC_0000002553202383__notificationmanagerrequestenablenotification10)后调用。

为了防止代理提醒被滥用于广告、营销类提醒，影响用户体验，部分设备上代理提醒增加了管控机制。管控后的适配或申请权限的方法，请参考[约束与限制中的管控限制](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agent-powered-reminder#约束与限制)。

**需要权限**： ohos.permission.PUBLISH_AGENT_REMINDER

**系统能力**： SystemCapability.Notification.ReminderAgent

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| reminderReq | ReminderRequest | 是 | 需要发布的代理提醒实例。 |
| callback | AsyncCallback<number> | 是 | 回调函数，返回当前发布提醒的id。 |

**错误码：**

以下错误码的详细介绍请参见[reminderAgentManager错误码]([reminderAgentManager错误码](../../errors/reminderAgentManager错误码.md).md)和[通用错误码]([通用错误码](../../errors/通用错误码.md).md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter is not valid parameter. |
| 1700001 | Notification is not enabled. |
| 1700002 | The number of reminders exceeds the limit. |

**示例**：

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { reminderAgentManager } from '@kit.BackgroundTasksKit';

let timer: reminderAgentManager.ReminderRequestTimer = {
  reminderType: reminderAgentManager.ReminderType.REMINDER_TYPE_TIMER,
  triggerTimeInSeconds: 10
}

reminderAgentManager.publishReminder(timer, (err: BusinessError, reminderId: number) => {
  if (err.code) {
    console.error("callback err code:" + err.code + " message:" + err.message);
  } else {
    console.info("callback, reminderId = " + reminderId);
  }
});
```

#### reminderAgentManager.publishReminder

publishReminder(reminderReq: ReminderRequest): Promise<number>

发布后台代理提醒。使用Promise异步回调。

如果[ReminderRequest.ringDuration](#ZH-CN_TOPIC_0000002522081202__reminderrequest)参数值大于0，则自定义铃声默认在闹钟通道上播放，如果值不大于0，则无响铃。


该接口需要申请通知弹窗权限[notificationManager.requestEnableNotification](@ohos.notificationManager (NotificationManager模块).md#ZH-CN_TOPIC_0000002553202383__notificationmanagerrequestenablenotification10)后调用。

为了防止代理提醒被滥用于广告、营销类提醒，影响用户体验，部分设备上代理提醒增加了管控机制。管控后的适配或申请权限的方法，请参考[约束与限制中的管控限制](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agent-powered-reminder#约束与限制)。

**需要权限**： ohos.permission.PUBLISH_AGENT_REMINDER

**系统能力**： SystemCapability.Notification.ReminderAgent

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| reminderReq | ReminderRequest | 是 | 需要发布的代理提醒实例。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回当前发布提醒的id。 |

**错误码：**

以下错误码的详细介绍请参见[reminderAgentManager错误码](reminderAgentManager错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter is not valid parameter. |
| 1700001 | Notification is not enabled. |
| 1700002 | The number of reminders exceeds the limit. |

**示例**：

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { reminderAgentManager } from '@kit.BackgroundTasksKit';

let timer: reminderAgentManager.ReminderRequestTimer = {
  reminderType: reminderAgentManager.ReminderType.REMINDER_TYPE_TIMER,
  triggerTimeInSeconds: 10
}

reminderAgentManager.publishReminder(timer).then((reminderId: number) => {
  console.info("promise, reminderId = " + reminderId);
}).catch((err: BusinessError) => {
  console.error("promise err code:" + err.code + " message:" + err.message);
});
```

#### reminderAgentManager.cancelReminder

cancelReminder(reminderId: number, callback: AsyncCallback<void>): void

取消指定id的代理提醒。使用callback异步回调。

**系统能力**： SystemCapability.Notification.ReminderAgent

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| reminderId | number | 是 | 需要取消的代理提醒的id，代理提醒id会在发布代理提醒时作为返回值返回。 |
| callback | AsyncCallback<void> | 是 | 回调函数，取消代理提醒成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[reminderAgentManager错误码](reminderAgentManager错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter is not valid parameter. |
| 1700003 | The reminder does not exist. |
| 1700004 | The bundle name does not exist. |

**示例**：

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { reminderAgentManager } from '@kit.BackgroundTasksKit';

let reminderId: number = 1;
reminderAgentManager.cancelReminder(reminderId, (err: BusinessError) => {
  if (err.code) {
    console.error("callback err code:" + err.code + " message:" + err.message);
  } else {
    console.info("cancelReminder callback");
  }
});
```

#### reminderAgentManager.cancelReminder

cancelReminder(reminderId: number): Promise<void>

取消指定id的代理提醒。使用Promise异步回调。

**系统能力**： SystemCapability.Notification.ReminderAgent

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| reminderId | number | 是 | 需要取消的代理提醒的id，代理提醒id会在发布代理提醒时作为返回值返回。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[reminderAgentManager错误码](reminderAgentManager错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter is not valid parameter. |
| 1700003 | The reminder does not exist. |
| 1700004 | The bundle name does not exist. |

**示例**：

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { reminderAgentManager } from '@kit.BackgroundTasksKit';

let reminderId: number = 1;
reminderAgentManager.cancelReminder(reminderId).then(() => {
  console.info("cancelReminder promise");
}).catch((err: BusinessError) => {
  console.error("promise err code:" + err.code + " message:" + err.message);
});
```

#### reminderAgentManager.getValidReminders

getValidReminders(callback: AsyncCallback<Array<ReminderRequest>>): void

获取当前应用设置的所有[有效（未过期）的代理提醒](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agent-powered-reminder#约束与限制)。使用callback异步回调。

**系统能力**： SystemCapability.Notification.ReminderAgent

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<Array<ReminderRequest>> | 是 | 回调函数，返回当前应用设置的所有有效（未过期）的代理提醒。 |

**错误码：**

以下错误码的详细介绍请参见[reminderAgentManager错误码](reminderAgentManager错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter is not valid parameter. |
| 1700004 | The bundle name does not exist. |

**示例**：

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { reminderAgentManager } from '@kit.BackgroundTasksKit';

reminderAgentManager.getValidReminders((err: BusinessError, reminders: Array<reminderAgentManager.ReminderRequest>) => {
  if (err.code) {
    console.error("callback err code:" + err.code + " message:" + err.message);
  } else {
    console.info("callback, getValidReminders length = " + reminders.length);
    for (let i = 0; i < reminders.length; i++) {
      console.info("getValidReminders = " + reminders[i]);
      console.info("getValidReminders, reminderType = " + reminders[i].reminderType);
      const actionButton = reminders[i].actionButton || [];
      for (let j = 0; j < actionButton.length; j++) {
        console.info("getValidReminders, actionButton.title = " + actionButton[j]?.title);
        console.info("getValidReminders, actionButton.type = " + actionButton[j]?.type);
      }
      console.info("getValidReminders, wantAgent.pkgName = " + reminders[i].wantAgent?.pkgName);
      console.info("getValidReminders, wantAgent.abilityName = " + reminders[i].wantAgent?.abilityName);
      console.info("getValidReminders, ringDuration = " + reminders[i].ringDuration);
      console.info("getValidReminders, snoozeTimes = " + reminders[i].snoozeTimes);
      console.info("getValidReminders, timeInterval = " + reminders[i].timeInterval);
      console.info("getValidReminders, title = " + reminders[i].title);
      console.info("getValidReminders, content = " + reminders[i].content);
      console.info("getValidReminders, expiredContent = " + reminders[i].expiredContent);
      console.info("getValidReminders, snoozeContent = " + reminders[i].snoozeContent);
      console.info("getValidReminders, notificationId = " + reminders[i].notificationId);
      console.info("getValidReminders, slotType = " + reminders[i].slotType);
    }
});
```

#### reminderAgentManager.getValidReminders

getValidReminders(): Promise<Array<ReminderRequest>>

获取当前应用设置的所有[有效（未过期）的代理提醒](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agent-powered-reminder#约束与限制)。使用Promise异步回调。

**系统能力**： SystemCapability.Notification.ReminderAgent

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<Array<ReminderRequest>> | Promise对象，返回当前应用设置的所有有效（未过期）的代理提醒。 |

**错误码：**

以下错误码的详细介绍请参见[reminderAgentManager错误码](reminderAgentManager错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter is not valid parameter. |
| 1700004 | The bundle name does not exist. |

**示例**：

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { reminderAgentManager } from '@kit.BackgroundTasksKit';

reminderAgentManager.getValidReminders().then((reminders: Array<reminderAgentManager.ReminderRequest>) => {
  console.info("promise, getValidReminders length = " + reminders.length);
  for (let i = 0; i < reminders.length; i++) {
    console.info("getValidReminders = " + reminders[i]);
    console.info("getValidReminders, reminderType = " + reminders[i].reminderType);
    const actionButton = reminders[i].actionButton || [];
    for (let j = 0; j < actionButton.length; j++) {
      console.info("getValidReminders, actionButton.title = " + actionButton[j]?.title);
      console.info("getValidReminders, actionButton.type = " + actionButton[j]?.type);
    }
    console.info("getValidReminders, wantAgent.pkgName = " + reminders[i].wantAgent?.pkgName);
    console.info("getValidReminders, wantAgent.abilityName = " + reminders[i].wantAgent?.abilityName);
    console.info("getValidReminders, ringDuration = " + reminders[i].ringDuration);
    console.info("getValidReminders, snoozeTimes = " + reminders[i].snoozeTimes);
    console.info("getValidReminders, timeInterval = " + reminders[i].timeInterval);
    console.info("getValidReminders, title = " + reminders[i].title);
    console.info("getValidReminders, content = " + reminders[i].content);
    console.info("getValidReminders, expiredContent = " + reminders[i].expiredContent);
    console.info("getValidReminders, snoozeContent = " + reminders[i].snoozeContent);
    console.info("getValidReminders, notificationId = " + reminders[i].notificationId);
    console.info("getValidReminders, slotType = " + reminders[i].slotType);
  }
}).catch((err: BusinessError) => {
  console.error("promise err code:" + err.code + " message:" + err.message);
});
```

#### reminderAgentManager.cancelAllReminders

cancelAllReminders(callback: AsyncCallback<void>): void

取消当前应用设置的所有代理提醒。使用callback异步回调。

**系统能力**： SystemCapability.Notification.ReminderAgent

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数，取消代理提醒成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[reminderAgentManager错误码](reminderAgentManager错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter is not valid parameter. |
| 1700004 | The bundle name does not exist. |

**示例**：

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { reminderAgentManager } from '@kit.BackgroundTasksKit';

reminderAgentManager.cancelAllReminders((err: BusinessError) =>{
  if (err.code) {
    console.error("callback err code:" + err.code + " message:" + err.message);
  } else {
    console.info("cancelAllReminders callback")
  }
});
```

#### reminderAgentManager.cancelAllReminders

cancelAllReminders(): Promise<void>

取消当前应用设置的所有代理提醒。使用Promise异步回调。

**系统能力**： SystemCapability.Notification.ReminderAgent

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[reminderAgentManager错误码](reminderAgentManager错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter is not valid parameter. |
| 1700004 | The bundle name does not exist. |

**示例**：

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { reminderAgentManager } from '@kit.BackgroundTasksKit';

reminderAgentManager.cancelAllReminders().then(() => {
  console.info("cancelAllReminders promise")
}).catch((err: BusinessError) => {
  console.error("promise err code:" + err.code + " message:" + err.message);
});
```

#### reminderAgentManager.add[NotificationSlot](../../topics/misc/NotificationSlot.md#ZH-CN_TOPIC_0000002497446138__notificationslot-1)

add[NotificationSlot](../../topics/misc/NotificationSlot.md#ZH-CN_TOPIC_0000002497446138__notificationslot-1)(slot: NotificationSlot, callback: AsyncCallback<void>): void

添加通知渠道。使用callback异步回调。

**系统能力**： SystemCapability.Notification.ReminderAgent

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slot | [NotificationSlot](../../topics/misc/NotificationSlot.md#ZH-CN_TOPIC_0000002497446138__notificationslot-1) | 是 | 通知渠道实例，仅支持设置其notificationType属性。 |
| callback | AsyncCallback<void> | 是 | 回调函数，添加[NotificationSlot](../../topics/misc/NotificationSlot.md#ZH-CN_TOPIC_0000002497446138__notificationslot-1)成功时，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter is not valid parameter. |

**示例**：

```ets
import { notificationManager } from '@kit.NotificationKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { reminderAgentManager } from '@kit.BackgroundTasksKit';

let mySlot: notificationManager.NotificationSlot = {
  notificationType: notificationManager.SlotType.SOCIAL_COMMUNICATION
}

reminderAgentManager.addNotificationSlot(mySlot, (err: BusinessError) => {
  if (err.code) {
    console.error("callback err code:" + err.code + " message:" + err.message);
  } else {
    console.info("addNotificationSlot callback");
  }
});
```

#### reminderAgentManager.add[NotificationSlot](../../topics/misc/NotificationSlot.md#ZH-CN_TOPIC_0000002497446138__notificationslot-1)

add[NotificationSlot](../../topics/misc/NotificationSlot.md#ZH-CN_TOPIC_0000002497446138__notificationslot-1)(slot: NotificationSlot): Promise<void>

添加通知渠道。使用Promise异步回调。

**系统能力**： SystemCapability.Notification.ReminderAgent

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slot | [NotificationSlot](../../topics/misc/NotificationSlot.md#ZH-CN_TOPIC_0000002497446138__notificationslot-1) | 是 | 通知渠道实例，仅支持设置其notificationType属性。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter is not valid parameter. |

**示例**：

```ets
import { notificationManager } from '@kit.NotificationKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { reminderAgentManager } from '@kit.BackgroundTasksKit';

let mySlot: notificationManager.NotificationSlot = {
  notificationType: notificationManager.SlotType.SOCIAL_COMMUNICATION
}
reminderAgentManager.addNotificationSlot(mySlot).then(() => {
  console.info("addNotificationSlot promise");
}).catch((err: BusinessError) => {
  console.error("promise err code:" + err.code + " message:" + err.message);
});
```

#### reminderAgentManager.remove[NotificationSlot](../../topics/misc/NotificationSlot.md#ZH-CN_TOPIC_0000002497446138__notificationslot-1)

remove[NotificationSlot](../../topics/misc/NotificationSlot.md#ZH-CN_TOPIC_0000002497446138__notificationslot-1)(slotType: notification.SlotType, callback: AsyncCallback<void>): void

删除指定的通知渠道类型，使用callback异步回调。

**系统能力**： SystemCapability.Notification.ReminderAgent

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotType | notification.SlotType | 是 | 通知渠道类型。 |
| callback | AsyncCallback<void> | 是 | 回调函数，当删除成功时，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter is not valid parameter. |

**示例**：

```ets
import { notificationManager } from '@kit.NotificationKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { reminderAgentManager } from '@kit.BackgroundTasksKit';

reminderAgentManager.removeNotificationSlot(notificationManager.SlotType.CONTENT_INFORMATION,
  (err: BusinessError) => {
  if (err.code) {
    console.error("callback err code:" + err.code + " message:" + err.message);
  } else {
    console.info("removeNotificationSlot callback");
  }
});
```

#### reminderAgentManager.remove[NotificationSlot](../../topics/misc/NotificationSlot.md#ZH-CN_TOPIC_0000002497446138__notificationslot-1)

remove[NotificationSlot](../../topics/misc/NotificationSlot.md#ZH-CN_TOPIC_0000002497446138__notificationslot-1)(slotType: notification.SlotType): Promise<void>

删除指定的通知渠道类型，使用Promise异步回调。

**系统能力**： SystemCapability.Notification.ReminderAgent

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotType | notification.SlotType | 是 | 通知渠道类型。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter is not valid parameter. |

**示例**：

```ets
import { notificationManager } from '@kit.NotificationKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { reminderAgentManager } from '@kit.BackgroundTasksKit';

reminderAgentManager.removeNotificationSlot(notificationManager.SlotType.CONTENT_INFORMATION).then(() => {
  console.info("removeNotificationSlot promise");
}).catch((err: BusinessError) => {
  console.error("promise err code:" + err.code + " message:" + err.message);
});
```

#### reminderAgentManager.getAllValidReminders12+

getAllValidReminders(): Promise<Array<ReminderInfo>>

获取当前应用设置的所有[有效（未过期）的代理提醒](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agent-powered-reminder#约束与限制)。使用Promise异步回调。该接口调用需要申请ohos.permission.PUBLISH_AGENT_REMINDER权限。

**系统能力**： SystemCapability.Notification.ReminderAgent

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<Array<ReminderInfo>> | Promise对象，返回当前应用设置的所有有效（未过期）的代理提醒。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |

**示例**：

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { reminderAgentManager } from '@kit.BackgroundTasksKit';

reminderAgentManager.getAllValidReminders().then((reminders: Array<reminderAgentManager.ReminderInfo>) => {
  console.info("promise, getAllValidReminders length = " + reminders.length);
  for (let i = 0; i < reminders.length; i++) {
    console.info("getAllValidReminders, reminderId = " + reminders[i].reminderId);
    console.info("getAllValidReminders, reminderType = " + reminders[i].reminderReq.reminderType);
    const actionButton = reminders[i].reminderReq.actionButton || [];
    for (let j = 0; j < actionButton.length; j++) {
      console.info("getAllValidReminders, actionButton.title = " + actionButton[j]?.title);
      console.info("getAllValidReminders, actionButton.type = " + actionButton[j]?.type);
    }
    console.info("getAllValidReminders, wantAgent.pkgName = " + reminders[i].reminderReq.wantAgent?.pkgName);
    console.info("getAllValidReminders, wantAgent.abilityName = " + reminders[i].reminderReq.wantAgent?.abilityName);
    console.info("getAllValidReminders, ringDuration = " + reminders[i].reminderReq.ringDuration);
    console.info("getAllValidReminders, snoozeTimes = " + reminders[i].reminderReq.snoozeTimes);
    console.info("getAllValidReminders, timeInterval = " + reminders[i].reminderReq.timeInterval);
    console.info("getAllValidReminders, title = " + reminders[i].reminderReq.title);
    console.info("getAllValidReminders, content = " + reminders[i].reminderReq.content);
    console.info("getAllValidReminders, expiredContent = " + reminders[i].reminderReq.expiredContent);
    console.info("getAllValidReminders, snoozeContent = " + reminders[i].reminderReq.snoozeContent);
    console.info("getAllValidReminders, notificationId = " + reminders[i].reminderReq.notificationId);
    console.info("getAllValidReminders, slotType = " + reminders[i].reminderReq.slotType);
  }
}).catch((err: BusinessError) => {
  console.error("promise err code:" + err.code + " message:" + err.message);
});
```

#### reminderAgentManager.addExcludeDate12+

addExcludeDate(reminderId: number, date: Date): Promise<void>

为指定id的周期性的日历提醒，添加不提醒日期（如每天提醒的日历，设置周二不提醒）。使用Promise异步回调。

**系统能力**： SystemCapability.Notification.ReminderAgent

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| reminderId | number | 是 | 需要添加不提醒日期的代理提醒id，代理提醒id会在发布代理提醒时作为返回值返回。 |
| date | Date | 是 | 不提醒的日期。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[reminderAgentManager错误码](reminderAgentManager错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | If the input parameter is not valid parameter. |
| 1700003 | The reminder does not exist. |

**示例**：

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { reminderAgentManager } from '@kit.BackgroundTasksKit';

let reminderId: number = 1;
let date = new Date();
reminderAgentManager.addExcludeDate(reminderId, date).then(() => {
  console.info("addExcludeDate promise");
}).catch((err: BusinessError) => {
  console.error("promise err code:" + err.code + " message:" + err.message);
});
```

#### reminderAgentManager.deleteExcludeDates12+

deleteExcludeDates(reminderId: number): Promise<void>

为指定id的周期性的日历提醒，删除设置的所有不提醒日期。使用Promise异步回调。

**系统能力**： SystemCapability.Notification.ReminderAgent

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| reminderId | number | 是 | 需要删除不提醒日期的代理提醒id，代理提醒id会在发布代理提醒时作为返回值返回。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[reminderAgentManager错误码](reminderAgentManager错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 1700003 | The reminder does not exist. |

**示例**：

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { reminderAgentManager } from '@kit.BackgroundTasksKit';

let reminderId: number = 1;
reminderAgentManager.deleteExcludeDates(reminderId).then(() => {
  console.info("deleteExcludeDates promise");
}).catch((err: BusinessError) => {
  console.error("promise err code:" + err.code + " message:" + err.message);
});
```

#### reminderAgentManager.getExcludeDates12+

getExcludeDates(reminderId: number): Promise<Array<Date>>

为指定id的周期性的日历提醒，查询设置的所有不提醒日期。使用Promise异步回调。

**系统能力**： SystemCapability.Notification.ReminderAgent

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| reminderId | number | 是 | 需要查询不提醒日期的代理提醒id，代理提醒id会在发布代理提醒时作为返回值返回。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<Array<Date>> | Promise对象。返回特定日历设置的所有不提醒日期。 |

**错误码：**

以下错误码的详细介绍请参见[reminderAgentManager错误码](reminderAgentManager错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 1700003 | The reminder does not exist. |

**示例**：

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { reminderAgentManager } from '@kit.BackgroundTasksKit';

let reminderId: number = 1;
reminderAgentManager.getExcludeDates(reminderId).then((dates) => {
  console.info("getExcludeDates promise length: " + dates.length);
  for (let i = 0; i < dates.length; i++) {
    console.info("getExcludeDates promise date is: " + dates[i].toString());
  }
}).catch((err: BusinessError) => {
  console.error("promise err code:" + err.code + " message:" + err.message);
});
```

#### reminderAgentManager.updateReminder20+

updateReminder(reminderId: number, reminderReq: ReminderRequest): Promise<void>

更新指定id的代理提醒，使用Promise异步回调。仅[有效（未过期）](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agent-powered-reminder#约束与限制)、未显示在通知中心的代理提醒支持更新。

**需要权限**： ohos.permission.PUBLISH_AGENT_REMINDER

**系统能力**： SystemCapability.Notification.ReminderAgent

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| reminderId | number | 是 | 需要更新的代理提醒的id，代理提醒id会在发布代理提醒时作为返回值返回。 |
| reminderReq | ReminderRequest | 是 | 代理提醒对象实例，用于设置提醒类型、响铃时长等具体信息。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[reminderAgentManager错误码](reminderAgentManager错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 1700003 | The reminder does not exist. |
| 1700007 | If the input parameter is not valid parameter. |

**示例**：

```ets
import { reminderAgentManager } from '@kit.BackgroundTasksKit';
import { BusinessError } from '@kit.BasicServicesKit';

let timer: reminderAgentManager.ReminderRequestTimer = {
  reminderType: reminderAgentManager.ReminderType.REMINDER_TYPE_TIMER,
  triggerTimeInSeconds: 10
}

let reminderId: number = 1;
reminderAgentManager.updateReminder(reminderId, timer).then(() => {
  console.info("update reminder succeed");
}).catch((err: BusinessError) => {
  console.error("promise err code:" + err.code + " message:" + err.message);
});
```

**reminderAgentManager.cancelReminderOnDisplay23+**

cancelReminderOnDisplay(reminderId: number): Promise<void>

取消当前通知中心内显示的通知卡片，不取消代理提醒数据。例如：每天重复的提醒，该提醒正在通知中心内显示，该接口将通知从通知中心内取消，并且会按照设定的周期，在第二天再次提醒。

系统能力： SystemCapability.Notification.ReminderAgent

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| reminderId | number | 是 | 需要取消的代理提醒的id，代理提醒id会在发布代理提醒时作为返回值返回。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

错误码：

以下错误码的详细介绍请参见[reminderAgentManager错误码](reminderAgentManager错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1700003 | The reminder does not exist. |
| 1700007 | If the input parameter is not valid parameter. |

示例：

```ets
import { reminderAgentManager } from '@kit.BackgroundTasksKit';
import { BusinessError } from '@kit.BasicServicesKit';

let reminderId: number = 1;
reminderAgentManager.cancelReminderOnDisplay(reminderId).then(() => {
  console.info("cancel display reminder  succeed");
}).catch((err: BusinessError) => {
  console.error("promise err code:" + err.code + " message:" + err.message);
});
```

**reminderAgentManager.subscribeReminderState23+**

subscribeReminderState(callback: Callback<Array<ReminderState>>): Promise<void>

订阅代理提醒状态。使用Promise异步回调。

需要权限： ohos.permission.PUBLISH_AGENT_REMINDER

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Notification.ReminderAgent

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<Array<ReminderState>> | 是 | 回调函数，返回代理提醒状态信息。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

错误码：

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[reminderAgentManager错误码](reminderAgentManager错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 1700007 | If the input parameter is not valid parameter. |

示例：

```ets
import { reminderAgentManager } from '@kit.BackgroundTasksKit';
import { BusinessError } from '@kit.BasicServicesKit';

function reminderStateCallback(states: Array<reminderAgentManager.ReminderState>) {
  console.info('length is : ' + states.length);
}

reminderAgentManager.subscribeReminderState(reminderStateCallback).then(() => {
  console.info('subscribe succeed');
}).catch((err: BusinessError) => {
  console.error('promise err code:' + err.code + ' message:' + err.message);
});
```

**reminderAgentManager.unsubscribeReminderState23+**

unsubscribeReminderState(callback?: Callback<Array<ReminderState>>): Promise<void>

取消订阅代理提醒状态。使用Promise异步回调。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Notification.ReminderAgent

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<Array<ReminderState>> | 否 | 回调函数。如果不传参数callback，则取消所有订阅。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

错误码：

以下错误码的详细介绍请参见[reminderAgentManager错误码](reminderAgentManager错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1700007 | If the input parameter is not valid parameter. |

示例：

```ets
import { reminderAgentManager } from '@kit.BackgroundTasksKit';
import { BusinessError } from '@kit.BasicServicesKit';

function reminderStateCallback(states: Array<reminderAgentManager.ReminderState>) {
  console.info('length is : ' + states.length);
}

reminderAgentManager.unsubscribeReminderState(reminderStateCallback).then(() => {
  console.info('unsubscribe succeed');
}).catch((err: BusinessError) => {
  console.error('promise err code:' + err.code + ' message:' + err.message);
});
```

#### ActionButtonType

提醒上的按钮的类型。

**系统能力**：SystemCapability.Notification.ReminderAgent

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ACTION_BUTTON_TYPE_CLOSE | 0 | 表示关闭提醒的按钮。 |
| ACTION_BUTTON_TYPE_SNOOZE | 1 | 表示延时提醒的按钮，提醒次数和间隔通过ReminderRequest中snoozeTimes和timeInterval设置。 |

#### ReminderType

提醒的类型。

**系统能力**：SystemCapability.Notification.ReminderAgent

| 名称 | 值 | 说明 |
| --- | --- | --- |
| REMINDER_TYPE_TIMER | 0 | 表示提醒类型：倒计时。 |
| REMINDER_TYPE_CALENDAR | 1 | 表示提醒类型：日历。 |
| REMINDER_TYPE_ALARM | 2 | 表示提醒类型：闹钟。 |

#### RingChannel20+

自定义提示音的音频播放通道。

**系统能力**：SystemCapability.Notification.ReminderAgent

| 名称 | 值 | 说明 |
| --- | --- | --- |
| RING_CHANNEL_ALARM | 0 | 闹钟通道。 |
| RING_CHANNEL_MEDIA | 1 | 媒体通道。 |
| RING_CHANNEL_NOTIFICATION23+ | 2 | 通知通道。 |

#### ActionButton

弹出的提醒中按钮的类型和标题。

**系统能力**：SystemCapability.Notification.ReminderAgent

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| title | string | 否 | 否 | 按钮显示的标题。 |
| titleResource11+ | string | 否 | 是 | 标题的资源ID，用于切换系统语言后读取对应标题信息。 |
| type | ActionButtonType | 否 | 否 | 按钮的类型。 |

#### WantAgent

跳转目标的ability信息。

**系统能力**：SystemCapability.Notification.ReminderAgent

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| pkgName | string | 否 | 否 | 指明跳转目标的包名。 |
| abilityName | string | 否 | 否 | 指明跳转目标的ability名称。 |
| parameters12+ | Record<string, Object> | 否 | 是 | 需要传递到目标的参数。 |
| uri12+ | string | 否 | 是 | 指明跳转目标的uri信息。 |

#### MaxScreenWantAgent

通知中心弹出提醒时，全屏显示自动拉起目标的ability信息。该接口为预留接口，暂不支持使用。

**系统能力**：SystemCapability.Notification.ReminderAgent

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| pkgName | string | 否 | 否 | 指明提醒到达时自动拉起的目标包名（如果设备在使用中，则只弹出通知横幅框）。 |
| abilityName | string | 否 | 否 | 指明提醒到达时自动拉起的目标ability名（如果设备在使用中，则只弹出通知横幅框）。 |

#### ReminderRequest

代理提醒对象，用于设置提醒类型、响铃时长等具体信息。

**系统能力**：SystemCapability.Notification.ReminderAgent

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| reminderType | ReminderType | 否 | 否 | 指明代理提醒类型。 |
| actionButton | [ActionButton?, ActionButton?, ActionButton?] | 否 | 是 | 弹出的提醒通知中显示的按钮。 针对三方应用：最多支持两个按钮。 针对系统应用：从API version 10开始最多支持三个按钮，API version 10之前的版本最多支持两个按钮。 |
| wantAgent | WantAgent | 否 | 是 | 点击通知后需要跳转的目标ability信息。 |
| maxScreenWantAgent | MaxScreenWantAgent | 否 | 是 | 提醒到达时，全屏显示自动拉起目标的ability信息。如果设备正在使用中，则弹出一个通知横幅框。 说明：该接口为预留接口，暂不支持使用。 |
| ringDuration | number | 否 | 是 | 指明响铃时长（单位：秒），默认1秒，最长30分钟。 |
| snoozeTimes | number | 否 | 是 | 指明延时提醒次数，默认0次（不适用于倒计时提醒类型）。 |
| timeInterval | number | 否 | 是 | 执行延时提醒间隔（单位：秒），最少30秒（不适用于倒计时提醒类型）。 |
| title | string | 否 | 是 | 指明提醒标题。 |
| titleResourceId18+ | number | 否 | 是 | 指明提醒标题的资源ID。 |
| content | string | 否 | 是 | 指明提醒内容。 |
| contentResourceId18+ | number | 否 | 是 | 指明提醒内容的资源ID。 |
| expiredContent | string | 否 | 是 | 指明提醒过期后需要显示的内容。 |
| expiredContentResourceId18+ | number | 否 | 是 | 指明提醒过期后内容的资源ID。 |
| snoozeContent | string | 否 | 是 | 指明延时提醒时需要显示的内容（不适用于倒计时提醒类型）。 |
| snoozeContentResourceId18+ | number | 否 | 是 | 指明延时提醒内容的资源ID。 |
| notificationId | number | 否 | 是 | 指明提醒使用的通知的id号，需开发者传入，相同id号的提醒会覆盖。 |
| groupId11+ | string | 否 | 是 | 指明提醒使用相同的组id。相同组id中，一个提醒被点击不在提醒后，组内其他提醒也会被取消。 |
| slotType | notification.SlotType | 否 | 是 | 指明提醒的通道渠道类型。 |
| tapDismissed10+ | boolean | 否 | 是 | 通知是否自动清除，默认值为true，具体请参考[NotificationRequest.tapDismissed](../../topics/misc/NotificationRequest.md#ZH-CN_TOPIC_0000002497606118__notificationrequest-1)。 - true：点击通知消息或通知按钮后，自动删除当前通知。 - false：点击通知消息或通知按钮后，保留当前通知。 |
| autoDeletedTime10+ | number | 否 | 是 | 自动清除的时间，具体请参考[NotificationRequest.autoDeletedTime](../../topics/misc/NotificationRequest.md#ZH-CN_TOPIC_0000002497606118__notificationrequest-1)。 |
| snoozeSlotType11+ | notification.SlotType | 否 | 是 | 指明延时提醒的通道渠道类型（不适用于倒计时提醒类型）。 |
| customRingUri11+ | string | 否 | 是 | 指明自定义提示音的uri，提示音文件必须放在resources/rawfile目录下，支持m4a、aac、mp3、ogg、wav、flac、amr等格式。 |
| ringChannel20+ | RingChannel | 否 | 是 | 指明自定义提示音的音频播放通道，默认为闹钟通道。 |

#### ReminderRequestCalendar

ReminderRequestCalendar extends ReminderRequest

日历实例对象，用于设置提醒的时间。

**系统能力**：SystemCapability.Notification.ReminderAgent

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| dateTime | LocalDateTime | 否 | 否 | 指明提醒的目标时间。 |
| repeatMonths | Array<number> | 否 | 是 | 指明重复提醒的月份，范围：[1, 12]。 |
| repeatDays | Array<number> | 否 | 是 | 指明重复提醒的日期，范围：[1, 31]。 |
| daysOfWeek11+ | Array<number> | 否 | 是 | 指明每周哪几天需要重复提醒。范围为周一到周日，对应数字为1到7。 |
| endDateTime12+ | LocalDateTime | 否 | 是 | 指明提醒的结束时间。 |

#### ReminderRequestAlarm

ReminderRequestAlarm extends ReminderRequest

闹钟实例对象，用于设置提醒的时间。

**系统能力**：SystemCapability.Notification.ReminderAgent

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| hour | number | 否 | 否 | 指明提醒的目标时刻，范围：[0, 23]。 |
| minute | number | 否 | 否 | 指明提醒的目标分钟，范围：[0, 59]。 |
| daysOfWeek | Array<number> | 否 | 是 | 指明每周哪几天需要重复提醒。范围为周一到周日，对应数字为1到7。 |

#### ReminderRequestTimer

ReminderRequestTimer extends ReminderRequest

倒计时实例对象，用于设置提醒的时间。

**系统能力**：SystemCapability.Notification.ReminderAgent

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| triggerTimeInSeconds | number | 否 | 否 | 指明倒计时的秒数。 |

#### LocalDateTime

用于日历类提醒设置时指定时间信息。

**系统能力**：SystemCapability.Notification.ReminderAgent

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| year | number | 否 | 否 | 年 |
| month | number | 否 | 否 | 月，取值范围是[1, 12]。 |
| day | number | 否 | 否 | 日，取值范围是[1, 31]。 |
| hour | number | 否 | 否 | 时，取值范围是[0, 23]。 |
| minute | number | 否 | 否 | 分，取值范围是[0, 59]。 |
| second | number | 否 | 是 | 秒，取值范围是[0, 59]。 |

#### ReminderInfo12+

代理提醒信息，包含 ReminderRequest 和 ReminderId。

**系统能力**：SystemCapability.Notification.ReminderAgent

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| reminderId | number | 否 | 否 | 发布提醒后返回的id。 |
| reminderReq | ReminderRequest | 否 | 否 | 代理提醒对象。 |

**ReminderState23+**

代理提醒状态信息。状态信息会在如下两种情况发送通知：

1. 用户点击代理提醒的通知按钮时，如果应用进程存在，则会发送用户点击的按钮类型的通知给应用。如果应用未运行，则无法收到通知。

1. 由于第1点不能保证应用可以收到通知，因此应用注册新的回调函数时，会将该应用下所有用户点击的按钮类型回调给应用。状态信息最多保存30天，应用注册新的回调函数时或者超过30天未注册回调函数，会删除缓存的状态信息。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Notification.ReminderAgent

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| reminderId | number | 否 | 否 | 发布提醒后返回的id。 |
| buttonType | ActionButtonType | 否 | 否 | 按钮类型。 |
| isMessageResent | boolean | 否 | 否 | 信息是否为重复发送。 - false：信息首次发送。具体场景包括：用户点击代理提醒的通知按钮时，应用进程存在；用户点击代理提醒的通知按钮时，应用未运行，后续应用注册新的回调函数。 - true：信息重复发送，具体场景为：应用进程存在，用户点击代理提醒的通知按钮后，应用注册新的回调函数。 |