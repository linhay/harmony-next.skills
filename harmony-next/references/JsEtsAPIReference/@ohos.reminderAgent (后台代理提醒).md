# @ohos.reminderAgent (后台代理提醒)

本模块提供后台代理提醒的能力。

开发应用时，开发者可以调用相关接口创建定时提醒，包括倒计时、日历、闹钟这三类提醒类型。使用后台代理提醒能力后，应用被冻结或退出后，计时和弹出提醒的功能将被后台系统服务代理。

从API Version 9 开始，该接口不再维护，推荐使用新接口[@ohos.reminderAgentManager （后台代理提醒）](@ohos.reminderAgentManager (后台代理提醒).md)

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import reminderAgent from'@ohos.reminderAgent';
```

#### reminderAgent.publishReminder(deprecated)

publishReminder(reminderReq: ReminderRequest, callback: AsyncCallback<number>): void

发布一个后台代理提醒，使用回调的方式实现异步调用，该方法需要申请通知弹窗权限[Notification.requestEnableNotification](@ohos.notification (Notification模块).md#ZH-CN_TOPIC_0000002529286111__notificationrequestenablenotification8)后才能调用。

从 API version 7开始支持，从API version 9开始废弃。建议使用[reminderAgentManager.publishReminder](@ohos.reminderAgentManager (后台代理提醒).md#ZH-CN_TOPIC_0000002497445260__reminderagentmanagerpublishreminder)替代。

**需要权限**：ohos.permission.PUBLISH_AGENT_REMINDER

**系统能力**：SystemCapability.Notification.ReminderAgent

**参数**：

参数名类型必填说明reminderReq[ReminderRequest](#ZH-CN_TOPIC_0000002529445209__reminderrequestdeprecated)是需要发布的提醒实例。callbackAsyncCallback<number>是异步回调，返回当前发布的提醒的id。

**示例**：

```ets
import { BusinessError } from '@ohos.base';

let timer:reminderAgent.ReminderRequestTimer = {
  reminderType: reminderAgent.ReminderType.REMINDER_TYPE_TIMER,
  triggerTimeInSeconds: 10
}

reminderAgent.publishReminder(timer, (err: BusinessError, reminderId: number) => {
  console.log("callback, reminderId = " + reminderId);
});
```

#### reminderAgent.publishReminder(deprecated)

publishReminder(reminderReq: ReminderRequest): Promise<number>

发布一个后台代理提醒，使用Promise方式实现异步调用，该方法需要申请通知弹窗权限[Notification.requestEnableNotification](@ohos.notification (Notification模块).md#ZH-CN_TOPIC_0000002529286111__notificationrequestenablenotification8)后才能调用。

从 API version 7开始支持，从API version 9开始废弃。建议使用[reminderAgentManager.publishReminder](@ohos.reminderAgentManager (后台代理提醒).md#ZH-CN_TOPIC_0000002497445260__reminderagentmanagerpublishreminder-1)替代。

**需要权限**：ohos.permission.PUBLISH_AGENT_REMINDER

**系统能力**：SystemCapability.Notification.ReminderAgent

**参数**：

参数名类型必填说明reminderReq[ReminderRequest](#ZH-CN_TOPIC_0000002529445209__reminderrequestdeprecated)是需要发布的提醒实例。

**返回值**：

类型说明Promise<number>返回提醒的Id。

**示例**：

```ets
let timer:reminderAgent.ReminderRequestTimer = {
  reminderType: reminderAgent.ReminderType.REMINDER_TYPE_TIMER,
  triggerTimeInSeconds: 10
}

reminderAgent.publishReminder(timer).then((reminderId: number) => {
  console.log("promise, reminderId = " + reminderId);
});
```

#### reminderAgent.cancelReminder(deprecated)

cancelReminder(reminderId: number, callback: AsyncCallback<void>): void

取消指定id的提醒，使用回调的方式实现异步调用。

从 API version 7开始支持，从API version 9开始废弃。建议使用[reminderAgentManager.cancelReminder](@ohos.reminderAgentManager (后台代理提醒).md#ZH-CN_TOPIC_0000002497445260__reminderagentmanagercancelreminder)替代。

**系统能力**： SystemCapability.Notification.ReminderAgent

**参数**：

参数名类型必填说明reminderIdnumber是目标reminder的id号。callbackAsyncCallback<void>是异步回调。

**示例**：

```ets
import { BusinessError } from '@ohos.base';

reminderAgent.cancelReminder(1, (err: BusinessError, data: void) => {
  console.log("cancelReminder callback");
});
```

#### reminderAgent.cancelReminder(deprecated)

cancelReminder(reminderId: number): Promise<void>

取消指定id的提醒，使用Promise方式实现异步调用。

从 API version 7开始支持，从API version 9开始废弃。建议使用[reminderAgentManager.cancelReminder](@ohos.reminderAgentManager (后台代理提醒).md#ZH-CN_TOPIC_0000002497445260__reminderagentmanagercancelreminder-1)替代。

**系统能力**： SystemCapability.Notification.ReminderAgent

**参数**：

参数名类型必填说明reminderIdnumber是目标reminder的id号。

**返回值**：

类型说明Promise<void>Promise类型异步回调。

**示例**：

```ets
reminderAgent.cancelReminder(1).then(() => {
    console.log("cancelReminder promise");
});
```

#### reminderAgent.getValidReminders(deprecated)

getValidReminders(callback: AsyncCallback<Array<ReminderRequest>>): void

获取当前应用已设置的所有有效（未过期）的提醒，使用回调的方式实现异步调用。

从 API version 7开始支持，从API version 9开始废弃。建议使用[reminderAgentManager.getValidReminders](@ohos.reminderAgentManager (后台代理提醒).md#ZH-CN_TOPIC_0000002497445260__reminderagentmanagergetvalidreminders)替代。

**系统能力**： SystemCapability.Notification.ReminderAgent

**参数**：

参数名类型必填说明callbackAsyncCallback<Array<[ReminderRequest](#ZH-CN_TOPIC_0000002529445209__reminderrequestdeprecated)>>是异步回调，返回当前应用已设置的所有有效（未过期）的提醒。

**示例**：

```ets
import { BusinessError } from '@ohos.base';

reminderAgent.getValidReminders((err: BusinessError, reminders: Array<reminderAgent.ReminderRequest>) => {
  console.log("callback, getValidReminders length = " + reminders.length);
  for (let i = 0; i < reminders.length; i++) {
    console.log("getValidReminders = " + reminders[i]);
    console.log("getValidReminders, reminderType = " + reminders[i].reminderType);
    const actionButton = reminders[i].actionButton || [];
    for (let j = 0; j < actionButton.length; j++) {
      console.log("getValidReminders, actionButton.title = " + actionButton[j]?.title);
      console.log("getValidReminders, actionButton.type = " + actionButton[j]?.type);
    }
    console.log("getValidReminders, wantAgent.pkgName = " + reminders[i].wantAgent?.pkgName);
    console.log("getValidReminders, wantAgent.abilityName = " + reminders[i].wantAgent?.abilityName);
    console.log("getValidReminders, ringDuration = " + reminders[i].ringDuration);
    console.log("getValidReminders, snoozeTimes = " + reminders[i].snoozeTimes);
    console.log("getValidReminders, timeInterval = " + reminders[i].timeInterval);
    console.log("getValidReminders, title = " + reminders[i].title);
    console.log("getValidReminders, content = " + reminders[i].content);
    console.log("getValidReminders, expiredContent = " + reminders[i].expiredContent);
    console.log("getValidReminders, snoozeContent = " + reminders[i].snoozeContent);
    console.log("getValidReminders, notificationId = " + reminders[i].notificationId);
    console.log("getValidReminders, slotType = " + reminders[i].slotType);
  }
})
```

#### reminderAgent.getValidReminders(deprecated)

getValidReminders(): Promise<Array<ReminderRequest>>

获取当前应用已设置的所有有效（未过期）的提醒，使用Promise方式实现异步调用。

从 API version 7开始支持，从API version 9开始废弃。建议使用[reminderAgentManager.getValidReminders](@ohos.reminderAgentManager (后台代理提醒).md#ZH-CN_TOPIC_0000002497445260__reminderagentmanagergetvalidreminders-1)替代。

**系统能力**： SystemCapability.Notification.ReminderAgent

**返回值**：

类型说明Promise<Array<[ReminderRequest](#ZH-CN_TOPIC_0000002529445209__reminderrequestdeprecated)>>返回当前应用已设置的所有有效（未过期）的提醒。

**示例**：

```ets
reminderAgent.getValidReminders().then((reminders: Array<reminderAgent.ReminderRequest>) => {
  console.log("promise, getValidReminders length = " + reminders.length);
  for (let i = 0; i < reminders.length; i++) {
    console.log("getValidReminders = " + reminders[i]);
    console.log("getValidReminders, reminderType = " + reminders[i].reminderType);
    const actionButton = reminders[i].actionButton || [];
    for (let j = 0; j < actionButton.length; j++) {
      console.log("getValidReminders, actionButton.title = " + actionButton[j]?.title);
      console.log("getValidReminders, actionButton.type = " + actionButton[j]?.type);
    }
    console.log("getValidReminders, wantAgent.pkgName = " + reminders[i].wantAgent?.pkgName);
    console.log("getValidReminders, wantAgent.abilityName = " + reminders[i].wantAgent?.abilityName);
    console.log("getValidReminders, ringDuration = " + reminders[i].ringDuration);
    console.log("getValidReminders, snoozeTimes = " + reminders[i].snoozeTimes);
    console.log("getValidReminders, timeInterval = " + reminders[i].timeInterval);
    console.log("getValidReminders, title = " + reminders[i].title);
    console.log("getValidReminders, content = " + reminders[i].content);
    console.log("getValidReminders, expiredContent = " + reminders[i].expiredContent);
    console.log("getValidReminders, snoozeContent = " + reminders[i].snoozeContent);
    console.log("getValidReminders, notificationId = " + reminders[i].notificationId);
    console.log("getValidReminders, slotType = " + reminders[i].slotType);
  }
})
```

#### reminderAgent.cancelAllReminders(deprecated)

cancelAllReminders(callback: AsyncCallback<void>): void

取消当前应用所有的提醒，使用回调的方式实现异步调用。

从 API version 7开始支持，从API version 9开始废弃。建议使用[reminderAgentManager.cancelAllReminders](@ohos.reminderAgentManager (后台代理提醒).md#ZH-CN_TOPIC_0000002497445260__reminderagentmanagercancelallreminders)替代。

**系统能力**： SystemCapability.Notification.ReminderAgent

**参数**：

参数名类型必填说明callbackAsyncCallback<void>是异步回调。

**示例**：

```ets
import { BusinessError } from '@ohos.base';

reminderAgent.cancelAllReminders((err: BusinessError, data: void) =>{
  console.log("cancelAllReminders callback")
})
```

#### reminderAgent.cancelAllReminders(deprecated)

cancelAllReminders(): Promise<void>

取消当前应用所有的提醒，使用Promise方式实现异步调用。

从 API version 7开始支持，从API version 9开始废弃。建议使用[reminderAgentManager.cancelAllReminders](@ohos.reminderAgentManager (后台代理提醒).md#ZH-CN_TOPIC_0000002497445260__reminderagentmanagercancelallreminders-1)替代。

**系统能力**： SystemCapability.Notification.ReminderAgent

**返回值**：

类型说明Promise<void>Promise类型异步回调。

**示例**：

```ets
reminderAgent.cancelAllReminders().then(() => {
    console.log("cancelAllReminders promise")
})
```

#### reminderAgent.addNotificationSlot(deprecated)

addNotificationSlot(slot: NotificationSlot, callback: AsyncCallback<void>): void

添加一个NotificationSlot，使用回调的方式实现异步调用。

从 API version 7开始支持，从API version 9开始废弃。建议使用[reminderAgentManager.addNotificationSlot](@ohos.reminderAgentManager (后台代理提醒).md#ZH-CN_TOPIC_0000002497445260__reminderagentmanageraddnotificationslot)替代。

**系统能力**： SystemCapability.Notification.ReminderAgent

**参数**：

参数名类型必填说明slot[NotificationSlot](@ohos.notification (Notification模块).md#ZH-CN_TOPIC_0000002529286111__notificationslot)是notification.slot实例，仅支持设置其type属性。callbackAsyncCallback<void>是异步回调。

**示例**：

```ets
import notification from '@ohos.notificationManager'
import { BusinessError } from '@ohos.base';

let mySlot:notification.NotificationSlot = {
  type: notification.SlotType.SOCIAL_COMMUNICATION
}
reminderAgent.addNotificationSlot(mySlot, (err: BusinessError, data: void) => {
  console.log("addNotificationSlot callback");
});
```

#### reminderAgent.addNotificationSlot(deprecated)

addNotificationSlot(slot: NotificationSlot): Promise<void>

添加一个NotificationSlot，使用Promise方式实现异步调用。

从 API version 7开始支持，从API version 9开始废弃。建议使用[reminderAgentManager.addNotificationSlot](@ohos.reminderAgentManager (后台代理提醒).md#ZH-CN_TOPIC_0000002497445260__reminderagentmanageraddnotificationslot-1)替代。

**系统能力**： SystemCapability.Notification.ReminderAgent

**参数**：

参数名类型必填说明slot[NotificationSlot](@ohos.notification (Notification模块).md#ZH-CN_TOPIC_0000002529286111__notificationslot)是notification.slot实例，仅支持设置其type属性。

**返回值**：

类型说明Promise<void>Promise类型异步回调。

**示例**：

```ets
import notification from '@ohos.notificationManager'

let mySlot:notification.NotificationSlot = {
  type: notification.SlotType.SOCIAL_COMMUNICATION
}
reminderAgent.addNotificationSlot(mySlot).then(() => {
  console.log("addNotificationSlot promise");
});
```

#### reminderAgent.removeNotificationSlot(deprecated)

removeNotificationSlot(slotType: notification.SlotType, callback: AsyncCallback<void>): void

删除目标NotificationSlot，使用callback方式实现异步调用。

从 API version 7开始支持，从API version 9开始废弃。建议使用[reminderAgentManager.removeNotificationSlot](@ohos.reminderAgentManager (后台代理提醒).md#ZH-CN_TOPIC_0000002497445260__reminderagentmanagerremovenotificationslot)替代。

**系统能力**：SystemCapability.Notification.ReminderAgent

**参数**：

参数名类型必填说明slotType[notification.SlotType](@ohos.notification (Notification模块).md#ZH-CN_TOPIC_0000002529286111__slottype)是目标notification.slot的类型。callbackAsyncCallback<void>是异步回调。

**示例**：

```ets
import notification from '@ohos.notification'
import { BusinessError } from '@ohos.base';

reminderAgent.removeNotificationSlot(notification.SlotType.CONTENT_INFORMATION, (err: BusinessError, data: void) => {
  console.log("removeNotificationSlot callback");
});
```

#### reminderAgent.removeNotificationSlot(deprecated)

removeNotificationSlot(slotType: notification.SlotType): Promise<void>

删除目标NotificationSlot，使用Promise方式实现异步调用。

从 API version 7开始支持，从API version 9开始废弃。建议使用[reminderAgentManager.removeNotificationSlot](@ohos.reminderAgentManager (后台代理提醒).md#ZH-CN_TOPIC_0000002497445260__reminderagentmanagerremovenotificationslot-1)替代。

**系统能力**：SystemCapability.Notification.ReminderAgent

**参数**：

参数名类型必填说明slotType[notification.SlotType](@ohos.notification (Notification模块).md#ZH-CN_TOPIC_0000002529286111__slottype)是目标notification.slot的类型。

**返回值**：

类型说明Promise<void>Promise类型异步回调。

**示例**：

```ets
import notification from '@ohos.notification'

reminderAgent.removeNotificationSlot(notification.SlotType.CONTENT_INFORMATION).then(() => {
    console.log("removeNotificationSlot promise");
});
```

#### ActionButtonType(deprecated)

按钮的类型。

从 API version 7开始支持，从API version 9开始废弃。建议使用[reminderAgentManager.ActionButtonType](@ohos.reminderAgentManager (后台代理提醒).md#ZH-CN_TOPIC_0000002497445260__actionbuttontype)替代。

**系统能力**：SystemCapability.Notification.ReminderAgent

名称值说明ACTION_BUTTON_TYPE_CLOSE0表示关闭提醒的按钮。ACTION_BUTTON_TYPE_SNOOZE1表示延迟提醒的按钮。

#### ReminderType(deprecated)

提醒的类型。

从 API version 7开始支持，从API version 9开始废弃。建议使用[reminderAgentManager.ReminderType](@ohos.reminderAgentManager (后台代理提醒).md#ZH-CN_TOPIC_0000002497445260__remindertype)替代。

**系统能力**：SystemCapability.Notification.ReminderAgent

名称值说明REMINDER_TYPE_TIMER0表示提醒类型：倒计时。REMINDER_TYPE_CALENDAR1表示提醒类型：日历。REMINDER_TYPE_ALARM2表示提醒类型：闹钟。

#### ActionButton(deprecated)

用于设置弹出的提醒通知信息上显示的按钮类型和标题。

从 API version 7开始支持，从API version 9开始废弃。建议使用[reminderAgentManager.ActionButton](@ohos.reminderAgentManager (后台代理提醒).md#ZH-CN_TOPIC_0000002497445260__actionbutton)替代。

**系统能力**：SystemCapability.Notification.ReminderAgent

名称类型只读可选说明titlestring否否按钮显示的标题。type[ActionButtonType](#ZH-CN_TOPIC_0000002529445209__actionbuttontypedeprecated)否否按钮的类型。

#### WantAgent(deprecated)

点击提醒通知后跳转的目标ability信息。

从 API version 7开始支持，从API version 9开始废弃。建议使用[reminderAgentManager.WantAgent](@ohos.reminderAgentManager (后台代理提醒).md#ZH-CN_TOPIC_0000002497445260__wantagent)替代。

**系统能力**：SystemCapability.Notification.ReminderAgent

名称类型只读可选说明pkgNamestring否否指明点击提醒通知栏后跳转的目标HAP名。abilityNamestring否否指明点击提醒通知栏后跳转的目标ability名称。

#### MaxScreenWantAgent(deprecated)

全屏显示提醒到达时自动拉起的目标ability信息，该接口预留。

从 API version 7开始支持，从API version 9开始废弃。建议使用[reminderAgentManager.MaxScreenWantAgent](@ohos.reminderAgentManager (后台代理提醒).md#ZH-CN_TOPIC_0000002497445260__maxscreenwantagent)替代。

**系统能力**：SystemCapability.Notification.ReminderAgent

名称类型只读可选说明pkgNamestring否否指明提醒到达时自动拉起的目标HAP名（如果设备在使用中，则只弹出通知横幅框）。abilityNamestring否否指明提醒到达时自动拉起的目标ability名（如果设备在使用中，则只弹出通知横幅框）。

#### ReminderRequest(deprecated)

提醒实例对象，用于设置提醒类型、响铃时长等具体信息。

从 API version 7开始支持，从API version 9开始废弃。建议使用[reminderAgentManager.ReminderRequest](@ohos.reminderAgentManager (后台代理提醒).md#ZH-CN_TOPIC_0000002497445260__reminderrequest)替代。

**系统能力**：SystemCapability.Notification.ReminderAgent

名称类型只读可选说明reminderType[ReminderType](#ZH-CN_TOPIC_0000002529445209__remindertypedeprecated)否否指明提醒类型。actionButton[[ActionButton?, ActionButton?]](#ZH-CN_TOPIC_0000002529445209__actionbuttondeprecated)否是弹出的提醒通知栏中显示的按钮（参数可选，支持0/1/2个按钮）。wantAgentWantAgent否是点击通知后需要跳转的目标ability信息。maxScreenWantAgent[MaxScreenWantAgent](#ZH-CN_TOPIC_0000002529445209__maxscreenwantagentdeprecated)否是提醒到达时跳转的目标包。如果设备正在使用中，则弹出一个通知框。ringDurationnumber否是指明响铃时长（单位：秒），默认1秒。snoozeTimesnumber否是指明延迟提醒次数，默认0次。timeIntervalnumber否是执行延迟提醒间隔（单位：秒），默认0秒。titlestring否是指明提醒标题。contentstring否是指明提醒内容。expiredContentstring否是指明提醒过期后需要显示的内容。snoozeContentstring否是指明延迟提醒时需要显示的内容。notificationIdnumber否是指明提醒使用的通知的id号，相同id号的提醒会覆盖。slotType[notification.SlotType](zh-cn_topic_0000002529286111.html#ZH-CN_TOPIC_0000002529286111__slottype)否是指明提醒的slot类型。

#### ReminderRequestCalendar(deprecated)

日历实例对象，用于设置提醒的时间。

从 API version 7开始支持，从API version 9开始废弃。建议使用[reminderAgentManager.ReminderRequestCalendar](@ohos.reminderAgentManager (后台代理提醒).md#ZH-CN_TOPIC_0000002497445260__reminderrequestcalendar)替代。

**系统能力**：SystemCapability.Notification.ReminderAgent

名称类型只读可选说明dateTime[LocalDateTime](#ZH-CN_TOPIC_0000002529445209__localdatetimedeprecated)否否指明提醒的目标时间。repeatMonthsArray<number>否是指明重复提醒的月份。repeatDaysArray<number>否是指明重复提醒的日期。

#### ReminderRequestAlarm(deprecated)

闹钟实例对象，用于设置提醒的时间。

从 API version 7开始支持，从API version 9开始废弃。建议使用[reminderAgentManager.ReminderRequestAlarm](@ohos.reminderAgentManager (后台代理提醒).md#ZH-CN_TOPIC_0000002497445260__reminderrequestalarm)替代。

**系统能力**：SystemCapability.Notification.ReminderAgent

名称类型只读可选说明hournumber否否指明提醒的目标时刻。minutenumber否否指明提醒的目标分钟。daysOfWeekArray<number>否是指明每周哪几天需要重复提醒。范围为周一到周末，对应数字为1到7。

#### ReminderRequestTimer(deprecated)

倒计时实例对象，用于设置提醒的时间。

从 API version 7开始支持，从API version 9开始废弃。建议使用[reminderAgentManager.ReminderRequestTimer](@ohos.reminderAgentManager (后台代理提醒).md#ZH-CN_TOPIC_0000002497445260__reminderrequesttimer)替代。

**系统能力**：SystemCapability.Notification.ReminderAgent

名称类型只读可选说明triggerTimeInSecondsnumber否否指明倒计时的秒数。

#### LocalDateTime(deprecated)

用于日历类提醒设置时指定时间信息。

从 API version 7开始支持，从API version 9开始废弃。建议使用[reminderAgentManager.LocalDateTime](@ohos.reminderAgentManager (后台代理提醒).md#ZH-CN_TOPIC_0000002497445260__localdatetime)替代。

**系统能力**：SystemCapability.Notification.ReminderAgent

名称类型只读可选说明yearnumber否否年monthnumber否否月daynumber否否日hournumber否否时minutenumber否否分secondnumber否是秒