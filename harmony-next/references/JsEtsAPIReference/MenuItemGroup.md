# MenuItemGroup

该组件用来展示菜单MenuItem的分组。

该组件从API version 9开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

#### 子组件

包含[MenuItem](MenuItem.md)子组件。

#### 接口

MenuItemGroup(value?: MenuItemGroupOptions)

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明value[MenuItemGroupOptions](#ZH-CN_TOPIC_0000002497444948__menuitemgroupoptions对象说明)否包含设置MenuItemGroup的标题和尾部显示信息。

#### MenuItemGroupOptions对象说明

菜单MenuItem分组的标题和尾部信息。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明header[ResourceStr](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcestr) | [CustomBuilder](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__custombuilder8)否是设置对应group的标题显示信息。footer[ResourceStr](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcestr) | [CustomBuilder](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__custombuilder8)否是设置对应group的尾部显示信息。

#### 示例

详见[Menu组件示例](Menu.md#ZH-CN_TOPIC_0000002529444891__示例)。