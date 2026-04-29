# NotificationTemplate

通知模板。

本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

**NotificationTemplate**

**系统能力**：SystemCapability.Notification.Notification

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| name | string | 否 | 否 | 模板名称。当前仅支持表示下载进度的进度条通知模板，取值为'downloadTemplate'。 |
| data | Record<string, Object> | 否 | 否 | 模板数据。  - title: 表示下载标题。必填字段，值为字符串类型。  - fileName: 表示下载文件名。必填字段，值为字符串类型。  - progressValue: 表示下载进度，值为数值类型。 |