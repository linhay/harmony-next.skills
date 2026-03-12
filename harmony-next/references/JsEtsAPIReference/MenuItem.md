# MenuItem

用来展示菜单中具体的菜单选项。

该组件从API version 9开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

#### 子组件

无

#### 接口

MenuItem(value?: MenuItemOptions | CustomBuilder)

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明value[MenuItemOptions](#ZH-CN_TOPIC_0000002497604926__menuitemoptions对象说明) | [CustomBuilder](zh-cn_topic_0000002497604974.html#ZH-CN_TOPIC_0000002497604974__custombuilder8)否包含设置MenuItem的各项信息。

#### MenuItemOptions对象说明

Menu中具体item菜单项信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明startIcon[ResourceStr](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcestr)否是

MenuItem的起始图标。不支持Symbol图标。使用Symbol图标时，须使用symbolStartIcon。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

content[ResourceStr](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcestr)否是

MenuItem的内容。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

endIcon[ResourceStr](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcestr)否是

MenuItem的末尾图标。不支持Symbol图标。使用Symbol图标时，须使用symbolEndIcon。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

labelInfo[ResourceStr](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcestr)否是

MenuItem结束的标签信息，如快捷方式Ctrl+C等。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

builder[CustomBuilder](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__custombuilder8)否是

用于构建二级菜单。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

symbolStartIcon12+[SymbolGlyphModifier](动态SymbolGlyphModifier属性设置.md)否是

MenuItem起始的Symbol图标。配置该项时，原先startIcon图标不显示。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

symbolEndIcon12+[SymbolGlyphModifier](动态SymbolGlyphModifier属性设置.md)否是

MenuItem末尾的Symbol图标。配置该项时，原先endIcon图标不显示。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

#### 属性

除支持[通用属性](通用属性.md)外，还支持以下属性：

#### selected

selected(value: boolean)

设置菜单项是否选中。

从API version 10开始，该参数支持[$$](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-two-way-sync)双向绑定变量。

从API version 18开始，该参数支持[!!](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-binding#系统组件参数双向绑定)双向绑定变量。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明valueboolean是

菜单项是否选中。

true：菜单项被选中；false：菜单项不被选中。

默认值：false

#### selectIcon

selectIcon(value: boolean | ResourceStr | SymbolGlyphModifier)

设置当菜单项被选中时，是否显示被选中的图标。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明valueboolean | [ResourceStr](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcestr)10+| [SymbolGlyphModifier](动态SymbolGlyphModifier属性设置.md)12+是

菜单项被选中时，是否显示被选中的图标。

true：显示默认的对勾图标；false：不显示图标。

ResourceStr：显示指定的图标。

SymbolGlyphModifier：显示指定的HMSymbol图标。

默认值：false

#### contentFont10+

contentFont(value: Font)

设置菜单项中内容信息的字体样式。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明value[Font](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__font)是菜单项中内容信息的字体样式。

#### contentFontColor10+

contentFontColor(value: ResourceColor)

设置菜单项中内容信息的字体颜色。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明value[ResourceColor](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)是

菜单项中内容信息的字体颜色。

默认值：'#E5000000'

#### labelFont10+

labelFont(value: Font)

设置菜单项中标签信息的字体样式。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明value[Font](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__font)是菜单项中标签信息的字体样式。

#### labelFontColor10+

labelFontColor(value: ResourceColor)

设置菜单项中标签信息的字体颜色。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明value[ResourceColor](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)是

菜单项中标签信息的字体颜色。

默认值：'#99000000'

#### 事件

#### onChange

onChange(callback: (selected: boolean) => void)

当选中状态发生变化时，触发该回调。只有手动触发且MenuItem状态改变时才会触发onChange回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明selectedboolean是

选中状态发生变化时，触发该回调。

true：未选中切换为选中；false：选中切换为未选中。

#### 示例

详见[Menu组件示例](Menu.md#ZH-CN_TOPIC_0000002529444891__示例)。