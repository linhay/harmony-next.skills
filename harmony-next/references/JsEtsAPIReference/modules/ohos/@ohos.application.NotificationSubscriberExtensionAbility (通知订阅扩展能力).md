# @ohos.application.NotificationSubscriberExtensionAbility (通知订阅扩展能力)

NotificationSubscriberExtensionAbility 是通知订阅者扩展能力的基类，提供通知订阅的相关功能。

本模块首批接口从API version 22开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

#### 导入模块

```ets
import { notificationExtensionSubscription, NotificationSubscriberExtensionAbility } from '@kit.NotificationKit';
```

#### NotificationSubscriberExtensionAbility

**系统能力**：SystemCapability.Notification.Notification

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| context | NotificationSubscriberExtensionContext | 否 | 否 | NotificationSubscriberExtensionAbility的上下文环境。 |

#### onDestroy

onDestroy(): void

通知订阅扩展被销毁时的回调。

**系统能力**：SystemCapability.Notification.Notification

**示例：**

```ets
const TAG = 'NotificationSubscriberExtAbility';

export default class NotificationSubscriberExtAbility extends NotificationSubscriberExtensionAbility {
  onDestroy(): void {
    console.info(`${TAG} onDestroy`);
}
```

#### onReceiveMessage

onReceiveMessage(notificationInfo: [NotificationInfo](../../topics/misc/NotificationInfo.md)): void

收到通知时回调。

**系统能力**：SystemCapability.Notification.Notification

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| notificationInfo | [NotificationInfo](../../topics/misc/NotificationInfo.md) | 是 | 通知订阅扩展能力中onReceiveMessage回调的通知信息。 |

**示例：**

```ets
const TAG = 'NotificationSubscriberExtAbility';

export default class NotificationSubscriberExtAbility extends NotificationSubscriberExtensionAbility {
  onReceiveMessage(notificationInfo: notificationExtensionSubscription.NotificationInfo): void {
    console.info(`${TAG} onReceiveMessage. notificationInfo: ${JSON.stringify(notificationInfo)}`);
}
```

#### onCancelMessages

onCancelMessages(hashCodes: Array<string>): void

取消通知时的回调。

**系统能力**：SystemCapability.Notification.Notification

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| hashCodes | Array<string> | 是 | 要取消的通知的哈希码列表。 |

**示例：**

```ets
const TAG = 'NotificationSubscriberExtAbility';

export default class NotificationSubscriberExtAbility extends NotificationSubscriberExtensionAbility {
    onCancelMessages(hashCodes: Array<string>): void {
        console.info(`${TAG} onCancelMessages. hashCodes: ${JSON.stringify(hashCodes)}`);
    }
```