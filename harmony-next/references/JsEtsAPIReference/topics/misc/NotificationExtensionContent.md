# NotificationExtensionContent

通知扩展内容。

本模块首批接口从API version 22开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### NotificationExtensionContent

**系统能力**：SystemCapability.Notification.Notification

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| title | string | 否 | 否 | 通知标题。不能为空且不能超过1024字节，超出内容将被截断。 |
| text | string | 否 | 否 | 通知内容。不能为空且不能超过3072字节，超出内容将被截断。 |