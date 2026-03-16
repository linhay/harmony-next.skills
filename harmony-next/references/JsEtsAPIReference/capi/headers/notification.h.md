# notification.h

#### 概述

定义通知服务API接口。

**引用文件：** <NotificationKit/notification.h>

**库：** libohnotification.so

**系统能力：** SystemCapability.Notification.Notification

**起始版本：** 13

**相关模块：**[NOTIFICATION](../../topics/misc/notification.md)

#### 汇总

#### 函数

名称描述[bool OH_Notification_IsNotificationEnabled(void)](#ZH-CN_TOPIC_0000002497606124__oh_notification_isnotificationenabled)查询当前应用通知使能状态。

#### 函数说明

#### OH_Notification_IsNotificationEnabled()

```ets
bool OH_Notification_IsNotificationEnabled(void)
```

**描述**

查询当前应用通知使能状态。

**起始版本：** 13

**返回：**

类型说明bool

true - 表示当前应用已使能通知。

 false - 表示当前应用未使能通知。