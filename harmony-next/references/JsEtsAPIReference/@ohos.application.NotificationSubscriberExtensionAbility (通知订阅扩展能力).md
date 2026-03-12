# @ohos.application.NotificationSubscriberExtensionAbility (通知订阅扩展能力)

NotificationSubscriberExtensionAbility 是通知订阅者扩展能力的基类，提供通知订阅的相关功能。

本模块首批接口从API version 22开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

#### 导入模块

```ets
import { hilog } from '@kit.PerformanceAnalysisKit';
import { notificationExtensionSubscription, NotificationSubscriberExtensionAbility } from '@kit.NotificationKit';
```

#### NotificationSubscriberExtensionAbility

#### 属性

**系统能力**：SystemCapability.Notification.Notification

名称类型只读可选说明context[NotificationSubscriberExtensionContext](@ohos.application.NotificationSubscriberExtensionContext (通知订阅扩展上下文).md)否否NotificationSubscriberExtensionAbility的上下文环境。

#### onDestroy

onDestroy(): void

通知订阅扩展被销毁时的回调。

**系统能力**：SystemCapability.Notification.Notification

**示例：**

```ets
const DOMAIN = 0x0000;
const TAG = 'NotificationSubscriberExtAbility';

export default class NotificationSubscriberExtAbility extends NotificationSubscriberExtensionAbility {
  onDestroy(): void {
    hilog.info(DOMAIN, 'testTag', `${TAG} onDestroy`);
  }
}
```

#### onReceiveMessage

onReceiveMessage(notificationInfo: NotificationInfo): void

当系统收到通知时回调。

**系统能力**：SystemCapability.Notification.Notification

**参数：**

参数名类型必填说明notificationInfo[NotificationInfo](NotificationInfo.md)是包括ability名称、bundle名称等。

**示例：**

```ets
const DOMAIN = 0x0000;
const TAG = 'NotificationSubscriberExtAbility';

export default class NotificationSubscriberExtAbility extends NotificationSubscriberExtensionAbility {
  onReceiveMessage(notificationInfo: notificationExtensionSubscription.NotificationInfo): void {
    hilog.info(DOMAIN, 'testTag', `${TAG} onReceiveMessage. notificationInfo: ${JSON.stringify(notificationInfo)}`);
  }
}
```

#### onCancelMessages

onCancelMessages(hashCodes: Array<string>): void

取消通知时的回调。

**系统能力**：SystemCapability.Notification.Notification

**参数：**

参数名类型必填说明hashCodesArray<string>是要取消的通知的哈希码列表。

**示例：**

```ets
const DOMAIN = 0x0000;
const TAG = 'NotificationSubscriberExtAbility';

export default class NotificationSubscriberExtAbility extends NotificationSubscriberExtensionAbility {
    onCancelMessages(hashCodes: Array<string>): void {
        hilog.info(DOMAIN, 'testTag', `${TAG} onCancelMessages. hashCodes: ${JSON.stringify(hashCodes)}`);
    }
}
```