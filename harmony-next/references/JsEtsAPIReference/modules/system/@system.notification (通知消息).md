# @system.notification (通知消息)

-

从API Version 7 开始，该接口不再维护，推荐使用新接口[@ohos.notification](@ohos.notification (Notification模块).md)。

-

本模块首批接口从API version 3开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import notification from '@system.notification';
```

#### ActionResult

**系统能力**：SystemCapability.Notification.Notification

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bundleName | string | 是 | 单击通知后要重定向到的应用程序的Bundle名。 |
| abilityName | string | 是 | 单击通知后要重定向到的应用程序的Ability名称。 |
| uri | string | 否 | 要重定向到的页面的uri。 |

#### ShowNotificationOptions

**系统能力**：SystemCapability.Notification.Notification

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| contentTitle | string | 否 | 通知标题。 |
| contentText | string | 否 | 通知内容。 |
| clickAction(deprecated) | ActionResult | 否 | 通知被点击后触发的行为。 从API version 7开始不再维护。 |

#### notification.show

show(options?: ShowNotificationOptions): void

显示通知。

**系统能力：** SystemCapability.Notification.Notification

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | ShowNotificationOptions | 否 | 通知标题。 |

**示例：**

```ets
let notificationObj: notification = {
  show() {
    notification.show({
      contentTitle: 'title info',
      contentText: 'text',
      clickAction: {
        bundleName: 'com.example.testapp',
        abilityName: 'notificationDemo',
        uri: '/path/to/notification'
      }
    });
  }
```