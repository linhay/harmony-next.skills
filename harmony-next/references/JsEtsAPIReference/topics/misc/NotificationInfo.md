# NotificationInfo

通知信息应描述与第三方可穿戴设备共享的内容。

本模块首批接口从API version 22开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### NotificationInfo

**系统能力**：SystemCapability.Notification.Notification

名称类型只读可选说明hashCodestring是否通知的唯一标识符。notificationSlotType[notificationManager.SlotType](../../modules/ohos/@ohos.notificationManager (NotificationManager模块).md#ZH-CN_TOPIC_0000002497446132__slottype)是否通知渠道类型。默认值为OTHER_TYPES。content[NotificationExtensionContent](NotificationExtensionContent.md)是否通知内容。bundleNamestring是否创建通知的包名。appNamestring是是创建通知的应用程序名称。deliveryTimelong是是通知发布的时间戳（毫秒数）。groupNamestring是是通知组名称。默认情况下此参数为空。appIndexint是否创建通知的应用包的分身索引标识，仅在分身应用中生效。