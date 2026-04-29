# NotificationFlags

描述通知标志的实例。

本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

**NotificationFlags**

描述通知标志位。

**系统能力**：SystemCapability.Notification.Notification

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| soundEnabled | NotificationFlagStatus | 否 | 是 | 是否启用声音提示功能。从API version 23开始成为可写参数，设置时仅TYPE_CLOSE会生效。 |
| vibrationEnabled | NotificationFlagStatus | 否 | 是 | 是否启用振动提醒功能。从API version 23开始成为可写参数，设置时仅TYPE_CLOSE会生效。 |
| bannerEnabled23+ | NotificationFlagStatus | 否 | 是 | 是否启用横幅功能。设置时仅TYPE_CLOSE会生效。 |
| lockScreenEnabled23+ | NotificationFlagStatus | 否 | 是 | 是否启用锁屏功能。设置时仅TYPE_CLOSE会生效。 |

#### NotificationFlagStatus11+

描述通知标志状态。

**系统能力**：SystemCapability.Notification.Notification

| 名称 | 值 | 说明 |
| --- | --- | --- |
| TYPE_NONE | 0 | 默认标志，效果等同于打开。 |
| TYPE_OPEN | 1 | 通知标志打开。 |
| TYPE_CLOSE | 2 | 通知标志关闭。 |