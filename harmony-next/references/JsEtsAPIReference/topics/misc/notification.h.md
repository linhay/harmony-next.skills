# notification.h

**概述**

定义通知服务API接口。

引用文件： <NotificationKit/notification.h>

库： libohnotification.so

系统能力： SystemCapability.Notification.Notification

起始版本： 13

相关模块： [NOTIFICATION](NOTIFICATION.md)

**汇总**

**函数**

| 名称 | 描述 |
| --- | --- |
| bool OH_Notification_IsNotificationEnabled(void) | 查询当前应用通知使能状态。 |

**函数说明**

**OH_Notification_IsNotificationEnabled()**

```ets
bool OH_Notification_IsNotificationEnabled(void)
```

描述

查询当前应用通知使能状态。

起始版本： 13

返回：

| 类型 | 说明 |
| --- | --- |
| bool | true - 表示当前应用已使能通知。  false - 表示当前应用未使能通知。 |