# NotificationExtensionContent

通知扩展内容。

本模块首批接口从API version 22开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### NotificationExtensionContent

**系统能力**：SystemCapability.Notification.Notification

名称类型只读可选说明titlestring否否通知标题。不能为空且不能超过1024字节，超出内容将被截断。textstring否否通知内容。不能为空且不能超过3072字节，超出内容将被截断。