# NotificationActionButton

描述通知中显示的操作按钮。

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### NotificationActionButton

**系统能力：** SystemCapability.Notification.Notification

名称类型只读可选说明titlestring否否按钮标题。字符串长度不超过200字节，超出部分会被截断；也不可为空字符串。wantAgent[WantAgent](../../modules/ohos/@ohos.app.ability.wantAgent (WantAgent模块).md)否否点击按钮时触发的WantAgent。extras{ [key: string]: any }否是按钮扩展信息。预留能力，暂未支持。userInput8+[NotificationUserInput](../input/NotificationUserInput.md)否是用户输入对象实例。表示用户输入时的标识。