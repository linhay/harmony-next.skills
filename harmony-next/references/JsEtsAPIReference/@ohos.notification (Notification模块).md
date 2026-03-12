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

参数名类型必填说明request[NotificationRequest](#ZH-CN_TOPIC_0000002529286111__notificationrequest)是用于设置要发布通知的内容和相关配置信息。callbackAsyncCallback<void>是发布通知的回调方法。

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
  }
};
Notification.publish(notificationRequest, publishCallback);
```

#### Notification.publish

publish(request: NotificationRequest): Promise<void>

发布通知（Promise形式）。

**系统能力**：SystemCapability.Notification.Notification

**参数：**

参数名类型必填说明request[NotificationRequest](#ZH-CN_TOPIC_0000002529286111__notificationrequest)是用于设置要发布通知的内容和相关配置信息。

**返回值：**

类型说明Promise<void>无返回结果的Promise对象。

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

参数名类型必填说明idnumber是通知ID。labelstring是通知标签。callbackAsyncCallback<void>是表示被指定的回调方法。

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
}
Notification.cancel(0, "label", cancelCallback);
```

#### Notification.cancel

cancel(id: number, label?: string): Promise<void>

取消与指定通知ID相匹配的已发布通知，label可以指定也可以不指定（Promise形式）。

**系统能力**：SystemCapability.Notification.Notification

**参数：**

参数名类型必填说明idnumber是通知ID。labelstring否通知标签，默认为空。

**返回值：**

类型说明Promise<void>无返回结果的Promise对象。

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

参数名类型必填说明idnumber是通知ID。callbackAsyncCallback<void>是表示被指定的回调方法。

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
}
Notification.cancel(0, cancelCallback);
```

#### Notification.cancelAll

cancelAll(callback: AsyncCallback<void>): void

取消所有已发布的通知（callback形式）。

**系统能力**：SystemCapability.Notification.Notification

**参数：**

参数名类型必填说明callbackAsyncCallback<void>是表示被指定的回调方法。

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
}
Notification.cancelAll(cancelAllCallback);
```

#### Notification.cancelAll

cancelAll(): Promise<void>

取消所有已发布的通知（Promise形式）。

**系统能力**：SystemCapability.Notification.Notification

**返回值：**

类型说明Promise<void>无返回结果的Promise对象。

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

参数名类型必填说明type[SlotType](#ZH-CN_TOPIC_0000002529286111__slottype)是要创建的通知通道的类型。callbackAsyncCallback<void>是表示被指定的回调方法。

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
}
Notification.addSlot(Notification.SlotType.SOCIAL_COMMUNICATION, addSlotCallBack);
```

#### Notification.addSlot

addSlot(type: SlotType): Promise<void>

创建指定类型的通知通道（Promise形式）。

**系统能力**：SystemCapability.Notification.Notification

**参数：**

参数名类型必填说明type[SlotType](#ZH-CN_TOPIC_0000002529286111__slottype)是要创建的通知通道的类型。

**返回值：**

类型说明Promise<void>无返回结果的Promise对象。

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

参数名类型必填说明slotType[SlotType](#ZH-CN_TOPIC_0000002529286111__slottype)是通知渠道类型，目前分为社交通信、服务提醒、内容咨询和其他类型。callbackAsyncCallback<[NotificationSlot](#ZH-CN_TOPIC_0000002529286111__notificationslot)>是表示被指定的回调方法。

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
}
let slotType: Notification.SlotType = Notification.SlotType.SOCIAL_COMMUNICATION;
Notification.getSlot(slotType, getSlotCallback);
```

#### Notification.getSlot

getSlot(slotType: SlotType): Promise<NotificationSlot>

获取一个指定类型的通知通道（Promise形式）。

**系统能力**：SystemCapability.Notification.Notification

**参数：**

参数名类型必填说明slotType[SlotType](#ZH-CN_TOPIC_0000002529286111__slottype)是通知渠道类型，目前分为社交通信、服务提醒、内容咨询和其他类型。

**返回值：**

类型说明Promise<NotificationSlot>以Promise形式返回获取一个通知通道。

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

参数名类型必填说明callbackAsyncCallback<Array<[NotificationSlot](#ZH-CN_TOPIC_0000002529286111__notificationslot)>>是以callback形式返回获取此应用程序的所有通知通道的结果。

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
}
Notification.getSlots(getSlotsCallback);
```

#### Notification.getSlots

getSlots(): Promise<Array<NotificationSlot>>

获取此应用程序的所有通知通道（Promise形式）。

**系统能力**：SystemCapability.Notification.Notification

**返回值：**

类型说明Promise<Array<[NotificationSlot](#ZH-CN_TOPIC_0000002529286111__notificationslot)>>以Promise形式返回获取此应用程序的所有通知通道的结果。

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

参数名类型必填说明slotType[SlotType](#ZH-CN_TOPIC_0000002529286111__slottype)是通知渠道类型,目前分为社交通信、服务提醒、内容咨询和其他类型。callbackAsyncCallback<void>是表示被指定的回调方法。

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
}
let slotType: Notification.SlotType = Notification.SlotType.SOCIAL_COMMUNICATION;
Notification.removeSlot(slotType, removeSlotCallback);
```

#### Notification.removeSlot

removeSlot(slotType: SlotType): Promise<void>

删除指定类型的通知通道（Promise形式）。

**系统能力**：SystemCapability.Notification.Notification

**参数：**

参数名类型必填说明slotType[SlotType](#ZH-CN_TOPIC_0000002529286111__slottype)是通知渠道类型,目前分为社交通信、服务提醒、内容咨询和其他类型。

**返回值：**

类型说明Promise<void>无返回结果的Promise对象。

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

参数名类型必填说明callbackAsyncCallback<void>是表示被指定的回调方法。

**示例：**

```ets
import Base from '@ohos.base';

let removeAllCallBack = (err: Base.BusinessError) => {
  if (err) {
    console.info("removeAllSlots failed " + JSON.stringify(err));
  } else {
    console.info("removeAllSlots success");
  }
}
Notification.removeAllSlots(removeAllCallBack);
```

#### Notification.removeAllSlots

removeAllSlots(): Promise<void>

删除所有通知通道（Promise形式）。

**系统能力**：SystemCapability.Notification.Notification

**返回值：**

类型说明Promise<void>无返回结果的Promise对象。

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

参数名类型必填说明callbackAsyncCallback<number>是获取未删除通知数回调函数。

**示例：**

```ets
import Base from '@ohos.base';

let getActiveNotificationCountCallback = (err: Base.BusinessError, data: number) => {
  if (err) {
    console.info("getActiveNotificationCount failed " + JSON.stringify(err));
  } else {
    console.info("getActiveNotificationCount success");
  }
}

Notification.getActiveNotificationCount(getActiveNotificationCountCallback);
```

#### Notification.getActiveNotificationCount

getActiveNotificationCount(): Promise<number>

获取当前应用未删除的通知数（Promise形式）。

**系统能力**：SystemCapability.Notification.Notification

**返回值：**

类型说明Promise<number>以Promise形式返回获取当前应用未删除通知数。

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

参数名类型必填说明callbackAsyncCallback<Array<[NotificationRequest](#ZH-CN_TOPIC_0000002529286111__notificationrequest)>>是获取当前应用通知列表回调函数。

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
}

Notification.getActiveNotifications(getActiveNotificationsCallback);
```

#### Notification.getActiveNotifications

getActiveNotifications(): Promise<Array<[NotificationRequest](#ZH-CN_TOPIC_0000002529286111__notificationrequest)>>

获取当前应用未删除的通知列表（Promise形式）。

**系统能力**：SystemCapability.Notification.Notification

**返回值：**

类型说明Promise<Array<[NotificationRequest](#ZH-CN_TOPIC_0000002529286111__notificationrequest)>>以Promise形式返回获取当前应用通知列表。

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

参数名类型必填说明groupNamestring是通知组名称，此名称需要在发布通知时通过[NotificationRequest](#ZH-CN_TOPIC_0000002529286111__notificationrequest)对象指定。callbackAsyncCallback<void>是取消本应用指定组下通知的回调函数。

**示例：**

```ets
import Base from '@ohos.base';

let cancelGroupCallback = (err: Base.BusinessError) => {
  if (err) {
    console.info("cancelGroup failed " + JSON.stringify(err));
  } else {
    console.info("cancelGroup success");
  }
}

let groupName: string = "GroupName";

Notification.cancelGroup(groupName, cancelGroupCallback);
```

#### Notification.cancelGroup8+

cancelGroup(groupName: string): Promise<void>

取消本应用指定组下的通知（Promise形式）。

**系统能力**：SystemCapability.Notification.Notification

**参数：**

参数名类型必填说明groupNamestring是通知组名称。

**返回值：**

类型说明Promise<void>无返回结果的Promise对象。

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

参数名类型必填说明templateNamestring是模板名称。callbackAsyncCallback<boolean>是查询模板是否存在的回调函数。

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
}

Notification.isSupportTemplate(templateName, isSupportTemplateCallback);
```

#### Notification.isSupportTemplate8+

isSupportTemplate(templateName: string): Promise<boolean>

查询模板是否存在（Promise形式）。

**系统能力**：SystemCapability.Notification.Notification

**参数：**

参数名类型必填说明templateNamestring是模板名称。

**返回值：**

类型说明Promise<boolean>Promise方式返回模板是否存在的结果。

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

参数名类型必填说明callbackAsyncCallback<void>是应用请求通知使能的回调函数。

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

类型说明Promise<void>无返回结果的Promise对象。

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

参数名类型必填说明callbackAsyncCallback<boolean>是设备是否支持分布式通知的回调函数。

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

类型说明Promise<boolean>Promise方式返回设备是否支持分布式通知的结果。

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

名称值说明NOTIFICATION_CONTENT_BASIC_TEXTNOTIFICATION_CONTENT_BASIC_TEXT普通类型通知。NOTIFICATION_CONTENT_LONG_TEXTNOTIFICATION_CONTENT_LONG_TEXT长文本类型通知。NOTIFICATION_CONTENT_PICTURENOTIFICATION_CONTENT_PICTURE图片类型通知。NOTIFICATION_CONTENT_CONVERSATIONNOTIFICATION_CONTENT_CONVERSATION社交类型通知。NOTIFICATION_CONTENT_MULTILINENOTIFICATION_CONTENT_MULTILINE多行文本类型通知。

#### SlotLevel

**系统能力**：SystemCapability.Notification.Notification

名称值说明LEVEL_NONE0表示关闭通知功能。LEVEL_MIN1表示通知功能已启用，但状态栏中不显示通知图标，且没有横幅或提示音。LEVEL_LOW2表示通知功能已启用，且状态栏中显示通知图标，但没有横幅或提示音。LEVEL_DEFAULT3表示通知功能已启用，状态栏中显示通知图标，没有横幅但有提示音。LEVEL_HIGH4表示通知功能已启用，状态栏中显示通知图标，有横幅和提示音。

#### BundleOptiondeprecated

**系统能力**：SystemCapability.Notification.Notification

从 API version 7开始支持，从API version 9开始废弃。建议使用[notificationManager.BundleOption](NotificationCommonDef.md#ZH-CN_TOPIC_0000002529446079__bundleoption)替代。

名称类型必填说明bundlestring是应用的包信息。uidnumber否用户ID，默认为0。

#### NotificationKeydeprecated

**系统能力**：SystemCapability.Notification.Notification

从 API version 7开始支持，从API version 9开始废弃。

名称类型可读可写说明idnumber是是通知ID。labelstring是是通知标签。

#### SlotType

**系统能力**：SystemCapability.Notification.Notification

名称值说明UNKNOWN_TYPE0未知类型。SOCIAL_COMMUNICATION1社交类型。SERVICE_INFORMATION2服务类型。CONTENT_INFORMATION3内容类型。OTHER_TYPES0xFFFF其他类型。

#### NotificationActionButton

描述通知中显示的操作按钮。

**系统能力**：SystemCapability.Notification.Notification

名称类型可读可写说明titlestring是是按钮标题。wantAgent[WantAgent](@ohos.wantAgent (WantAgent模块).md)是是点击按钮时触发的WantAgent。extras{ [key: string]: any }是是按钮扩展信息。userInput8+[NotificationUserInput](#ZH-CN_TOPIC_0000002529286111__notificationuserinput8)是是用户输入对象实例。

#### NotificationBasicContent

描述普通文本通知。

**系统能力**：SystemCapability.Notification.Notification

名称类型可读可写说明titlestring是是通知标题。textstring是是通知内容。additionalTextstring是是通知附加内容，是对通知内容的补充。

#### NotificationLongTextContent

描述长文本通知。

**系统能力**：SystemCapability.Notification.Notification

名称类型可读可写说明titlestring是是通知标题。textstring是是通知内容。additionalTextstring是是通知附加内容，是对通知内容的补充。longTextstring是是通知的长文本。briefTextstring是是通知概要内容，是对通知内容的总结。expandedTitlestring是是通知展开时的标题。

#### NotificationMultiLineContent

描述多行文本通知。

**系统能力**：SystemCapability.Notification.Notification

名称类型可读可写说明titlestring是是通知标题。textstring是是通知内容。additionalTextstring是是通知附加内容，是对通知内容的补充。briefTextstring是是通知概要内容，是对通知内容的总结。longTitlestring是是通知展开时的标题。linesArray<string>是是通知的多行文本。

#### NotificationPictureContent

描述附有图片的通知。

**系统能力**：SystemCapability.Notification.Notification

名称类型可读可写说明titlestring是是通知标题。textstring是是通知内容。additionalTextstring是是通知附加内容，是对通知内容的补充。briefTextstring是是通知概要内容，是对通知内容的总结。expandedTitlestring是是通知展开时的标题。picture[image.PixelMap](Interface (PixelMap).md)是是通知的图片内容。

#### NotificationContent

描述通知类型。

**系统能力**：SystemCapability.Notification.Notification

名称类型可读可写说明contentType[notification.ContentType](#ZH-CN_TOPIC_0000002529286111__contenttype)是是通知内容类型。normal[NotificationBasicContent](#ZH-CN_TOPIC_0000002529286111__notificationbasiccontent)是是基本类型通知内容。longText[NotificationLongTextContent](#ZH-CN_TOPIC_0000002529286111__notificationlongtextcontent)是是长文本类型通知内容。multiLine[NotificationMultiLineContent](#ZH-CN_TOPIC_0000002529286111__notificationmultilinecontent)是是多行类型通知内容。picture[NotificationPictureContent](#ZH-CN_TOPIC_0000002529286111__notificationpicturecontent)是是图片类型通知内容。

#### NotificationRequest

描述通知的请求。

**系统能力**：SystemCapability.Notification.Notification

名称类型可读可写说明content[NotificationContent](#ZH-CN_TOPIC_0000002529286111__notificationcontent)是是通知内容。idnumber是是通知ID。slotType[notification.SlotType](#ZH-CN_TOPIC_0000002529286111__slottype)是是通道类型。isOngoingboolean是是是否进行时通知。isUnremovableboolean是是是否可移除。deliveryTimenumber是是通知发送时间。tapDismissedboolean是是通知是否自动清除。autoDeletedTimenumber是是自动清除的时间。wantAgent[WantAgent](zh-cn_topic_0000002497444666.html)是是WantAgent封装了应用的行为意图，点击通知时触发该行为。extraInfo{[key: string]: any}是是扩展参数。colornumber是是通知背景颜色。预留能力，暂未支持。colorEnabledboolean是是通知背景颜色是否使能。预留能力，暂未支持。isAlertOnceboolean是是设置是否仅有一次此通知提醒。isStopwatchboolean是是是否显示已用时间。isCountDownboolean是是是否显示倒计时时间。isFloatingIconboolean是是是否显示状态栏图标。labelstring是是通知标签。badgeIconStylenumber是是通知角标类型。showDeliveryTimeboolean是是是否显示分发时间。actionButtonsArray<[NotificationActionButton](#ZH-CN_TOPIC_0000002529286111__notificationactionbutton)>是是通知按钮，最多两个按钮。smallIcon[image.PixelMap](zh-cn_topic_0000002497605846.html)是是通知小图标。可选字段，大小不超过30KB。largeIcon[image.PixelMap](Interface (PixelMap).md)是是通知大图标。可选字段，大小不超过30KB。creatorBundleNamestring是否创建通知的包名。creatorUidnumber是否创建通知的UID。creatorPidnumber是否创建通知的PID。creatorUserId8+number是否创建通知的UserId。hashCodestring是否通知唯一标识。groupName8+string是是组通知名称。template8+[NotificationTemplate](#ZH-CN_TOPIC_0000002529286111__notificationtemplate8)是是通知模板。distributedOption8+[DistributedOptions](#ZH-CN_TOPIC_0000002529286111__distributedoptions8)是是分布式通知的选项。notificationFlags8+[NotificationFlags](zh-cn_topic_0000002529286107.html)是否获取NotificationFlags。removalWantAgent9+[WantAgent](@ohos.wantAgent (WantAgent模块).md)是是当移除通知时，通知将被重定向到的WantAgent实例。badgeNumber9+number是是应用程序图标上显示的通知数。

#### DistributedOptions8+

描述分布式选项。

**系统能力**：SystemCapability.Notification.Notification

名称类型可读可写说明isDistributedboolean是是是否为分布式通知。supportDisplayDevicesArray<string>是是可以同步通知到的设备列表。supportOperateDevicesArray<string>是是可以打开通知的设备列表。

#### NotificationSlot

描述通知槽

**系统能力**：SystemCapability.Notification.Notification

名称类型可读可写说明type[notification.SlotType](#ZH-CN_TOPIC_0000002529286111__slottype)是是通道类型。level[notification.SlotLevel](#ZH-CN_TOPIC_0000002529286111__slotlevel)是是通知级别，不设置则根据通知渠道类型有默认值。descstring是是通知渠道描述信息。badgeFlagboolean是是是否显示角标。bypassDndboolean是是设置是否在系统中绕过免打扰模式。lockscreenVisibilitynumber是是在锁定屏幕上显示通知的模式。vibrationEnabledboolean是是是否可振动。soundstring是是通知提示音。lightEnabledboolean是是是否闪灯。lightColornumber是是通知灯颜色。vibrationValuesArray<number>是是通知振动样式。enabled9+boolean是否此通知插槽中的启停状态。

#### NotificationTemplate8+

通知模板。

**系统能力**：SystemCapability.Notification.Notification

名称类型可读可写说明namestring是是模板名称。dataRecord<string, Object>是是模板数据。

#### NotificationUserInput8+

保存用户输入的通知消息。

**系统能力**：SystemCapability.Notification.Notification

名称类型可读可写说明inputKeystring是是用户输入时用于标识此输入的key。