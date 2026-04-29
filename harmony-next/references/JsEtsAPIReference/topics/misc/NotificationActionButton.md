# NotificationActionButton

描述通知中显示的操作按钮。

  ![image](public_sys-resources/note_3.0-zh-cn.webp)

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

**NotificationActionButton**

系统能力： SystemCapability.Notification.Notification

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| title | string | 否 | 否 | 按钮标题。字符串长度不超过200字节，超出部分会被截断；也不可为空字符串。 |
| wantAgent | WantAgent | 否 | 否 | 点击按钮时触发的WantAgent。 |
| extras | { [key: string]: any } | 否 | 是 | 按钮扩展信息。预留能力，暂未支持。 |
| userInput8+ | NotificationUserInput | 否 | 是 | 用户输入对象实例。表示用户输入时的标识。 |