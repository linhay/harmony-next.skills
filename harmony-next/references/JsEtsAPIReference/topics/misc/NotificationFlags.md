# NotificationFlags

描述通知标志的实例。

本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

**系统能力**：SystemCapability.Notification.Notification

#### 属性

名称类型只读可选说明soundEnabled[NotificationFlagStatus](#ZH-CN_TOPIC_0000002529286107__notificationflagstatus11)是是是否启用声音提示。vibrationEnabled[NotificationFlagStatus](#ZH-CN_TOPIC_0000002529286107__notificationflagstatus11)是是是否启用振动提醒功能。

#### NotificationFlagStatus11+

描述通知标志状态。

**系统能力**：SystemCapability.Notification.Notification

名称值说明TYPE_NONE0默认标志，效果等同于打开。TYPE_OPEN1通知标志打开。TYPE_CLOSE2通知标志关闭。