# Select

提供下拉选择菜单，让用户在多个选项间选择。

  ![image](public_sys-resources/note_3.0-zh-cn.webp)

该组件从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

**子组件**

无

**接口**

Select(options: Array<SelectOption>)

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | Array<SelectOption> | 是 | 设置下拉选项。 |

**SelectOption对象说明**

下拉菜单项的信息。

系统能力： SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| value | ResourceStr | 否 | 否 | 下拉选项内容。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| icon | ResourceStr | 否 | 是 | 下拉选项图片。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| symbolIcon12+ | SymbolGlyphModifier | 否 | 是 | 下拉选项Symbol图片。 symbolIcon优先级高于icon。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |

**属性**

除支持[通用属性](通用属性.md)外，还支持以下属性：

**selected**

selected(value: number | Resource)

设置下拉菜单初始选项的索引，第一项的索引为0。当不设置selected属性或设置为异常值时，默认选中值为-1，菜单项不选中；当设置为undefined、null时，选中第一项。

从API version 10开始，该属性支持[$$](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-two-way-sync)双向绑定变量。

从API version 18开始，该属性支持[!!](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-binding#系统组件参数双向绑定)双向绑定变量。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | Resource11+ | 是 | 下拉菜单初始选项的索引，索引值从0开始。 |

**selected18+**

selected(numCount: Optional<number | Resource>)

设置下拉菜单初始选项的索引，第一项的索引为0。当不设置selected属性或设置异常值时，默认选择值为-1，菜单项不选中；当设置为undefined、null时，选中第一项。

该属性支持[$$](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-two-way-sync)、[!!](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-binding#系统组件参数双向绑定)双向绑定变量。

元服务API： 从API version 18开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| numCount | Optional<number | Resource> | 是 | 下拉菜单初始选项的索引。 当numCount的值为undefined时，选中第一项。 |

**value**

value(value: ResourceStr)

设置下拉按钮的文本内容。选中菜单项后，按钮文本将自动更新为选中的菜单项文本。

从API version 10开始，该参数支持[$$](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-two-way-sync)双向绑定变量。

从API version 18开始，该参数支持[!!](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-binding#系统组件参数双向绑定)双向绑定变量。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | ResourceStr11+ | 是 | 下拉按钮本身的文本内容。 说明： 文本长度大于列宽时，文本被截断。 |

**value18+**

value(resStr: Optional<ResourceStr>)

设置下拉按钮的文本内容。选中菜单项后，按钮文本将自动更新为选中的菜单项文本。与[value](#ZH-CN_TOPIC_0000002553200803__value)相比，resStr参数新增了对undefined类型的支持。

该参数支持[$$](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-two-way-sync)、[!!](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-binding#系统组件参数双向绑定)双向绑定变量。

元服务API： 从API version 18开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resStr | Optional<ResourceStr> | 是 | 下拉按钮本身的文本内容。 当resStr的值为undefined时维持上次取值。 |

**controlSize12+**

controlSize(value: ControlSize)

设置Select组件的尺寸。

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | ControlSize11+ | 是 | Select组件的尺寸。 默认值：ControlSize.NORMAL |

controlSize、width、height接口作用优先级：

1）如果开发者只设置了width和height，当文字大小设置为较大的值时，文字会超出组件大小，超出的部分以省略号的方式显示；

2）如果开发者只设置了controlSize，没有设置width和height，组件宽高自适应文字，文字不超出组件，并设置最小宽度minWidth和最小高度minHeight；

3）如果同时设置了controlSize、width、height接口，width和height设置的值生效，但如果width和height设置的值小于controlSize设置的最小宽度minWidth和最小高度minHeight，width和height设置的值不生效，宽高仍保持controlSize设置的最小宽度minWidth和最小高度minHeight。

**controlSize18+**

controlSize(size: Optional<ControlSize>)

设置Select组件的尺寸。与[controlSize](#ZH-CN_TOPIC_0000002553200803__controlsize12)12+相比，size参数新增了对undefined类型的支持。

元服务API： 从API version 18开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| size | Optional<ControlSize> | 是 | Select组件的尺寸。 当size的值为undefined时，默认值为ControlSize.NORMAL。 |

controlSize、width、height接口作用优先级：

1）如果开发者只设置了width和height，当文字大小设置的是比较大的值的时候，文字超出组件大小，超出的部分以省略号的方式显示；

2）如果开发者只设置了controlSize，没有设置width和height，组件宽高自适应文字，文字不超出组件，并设置最小宽度minWidth和最小高度minHeight；

3）如果controlSize、width、height接口都设置了，width和height设置的值生效，但如果width和height设置的值小于controlSize设置的最小宽度minWidth和最小高度minHeight，width和height设置的值不生效，宽高仍保持controlSize设置的最小宽度minWidth和最小高度minHeight。

**menuItemContentModifier12+**

menuItemContentModifier(modifier: ContentModifier<MenuItemConfiguration>)

定制Select下拉菜单项内容区的方法。在应用了menuItemContentModifier后，下拉菜单的内容将完全由开发者自定义，此时为Select组件设置的分割线、选项颜色及下拉菜单的字体颜色等属性将不再生效。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

该接口不支持在[attributeModifier](动态属性设置.md#ZH-CN_TOPIC_0000002522240800__attributemodifier)中调用。

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| modifier | ContentModifier<MenuItemConfiguration> | 是 | 在Select组件上，定制下拉菜单项内容区的方法。 modifier：内容修改器，开发者需要自定义class实现ContentModifier接口。 |

**menuItemContentModifier18+**

menuItemContentModifier(modifier: Optional<ContentModifier<MenuItemConfiguration>>)

定制Select下拉菜单项内容区的方法。与[menuItemContentModifier](#ZH-CN_TOPIC_0000002553200803__menuitemcontentmodifier12)12+相比，modifier参数新增了对undefined类型的支持。在应用了menuItemContentModifier后，下拉菜单的内容将完全由开发者自定义，此时为Select组件设置的分割线、选项颜色及下拉菜单的字体颜色等属性将不再生效。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

该接口不支持在[attributeModifier](动态属性设置.md#ZH-CN_TOPIC_0000002522240800__attributemodifier)中调用。

元服务API： 从API version 18开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| modifier | Optional<ContentModifier<MenuItemConfiguration>> | 是 | 在Select组件上，定制下拉菜单项内容区的方法。 modifier：内容修改器，开发者需要自定义class实现ContentModifier接口。 当modifier的值为undefined时，不使用内容修改器。 |

**divider12+**

divider(options: Optional<DividerOptions> | null)

设置分割线样式，不设置该属性则按“默认值”展示分割线。

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | Optional<DividerOptions> | null | 是 | 1.设置DividerOptions，则按设置的样式显示分割线。 默认值： { strokeWidth: '1px' , color: '#33182431' } 2.设置为null时，不显示分割线。 3.strokeWidth设置过宽时，会覆盖文字。分割线会从每一个Item底部开始，同时向上向下画分割线。 4.startMargin和endMargin的默认值与不设置divider属性时的分割线样式保持一致。startMargin和endMargin的和与optionWidth的值相等时，不显示分割线。 startMargin和endMargin的和超过optionWidth的值时，按照默认样式显示分割线。 |

**dividerStyle19+**

dividerStyle(style: Optional<DividerStyleOptions>)

设置分割线样式，不设置该属性则按“默认值”展示分割线。该属性与divider互斥，按调用顺序生效。

元服务API： 从API version 19开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| style | Optional<DividerStyleOptions> | 是 | 1.设置DividerOptions，则按设置的样式显示分割线。 默认值： { strokeWidth: '1px' , color: '#33182431' } 2.设置为null或undefined时，展示默认分割线。 3.当mode为FLOAT_ABOVE_MENU时，strokeWidth设置过宽时，会覆盖文字。分割线会从每一个Item底部开始，同时向上向下画分割线。当mode为EMBEDDED_IN_MENU时，分割线在Menu中展开，独立占用高度。 4.startMargin和endMargin的默认值与不设置divider属性时的分割线样式保持一致。startMargin和endMargin的和与optionWidth的值相等时，不显示分割线。startMargin和endMargin的和超过optionWidth的值时，按照默认样式显示分割线。 |

**font**

font(value: Font)

设置下拉按钮本身的文本样式。当size为0时，文本不显示，当size为负值时，文本的size按照默认值显示。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Font | 是 | 下拉按钮本身的文本样式。 API version 11及以前默认值： { size: $r('sys.float.ohos_id_text_size_button1'), weight: FontWeight.Medium } API version 12以后，如果设置controlSize的值为：controlSize.SMALL，size默认值是$r('sys.float.ohos_id_text_size_button2')，否则为$r('sys.float.ohos_id_text_size_button1')。 |

**font18+**

font(selectFont: Optional<Font>)

设置下拉按钮本身的文本样式。当size为0时，文本不显示，当size为负值时，文本的size按照默认值显示。与[font](#ZH-CN_TOPIC_0000002553200803__font)相比，selectFont参数新增了对undefined类型的支持。

元服务API： 从API version 18开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| selectFont | Optional<Font> | 是 | 下拉按钮本身的文本样式。 如果设置controlSize的值为：controlSize.SMALL，size默认值是$r('sys.float.ohos_id_text_size_button2')，否则为$r('sys.float.ohos_id_text_size_button1')。 当selectFont的值为undefined时，恢复为系统文本样式。 |

**fontColor**

fontColor(value: ResourceColor)

设置下拉按钮本身的文本颜色。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | ResourceColor | 是 | 下拉按钮本身的文本颜色。 默认值：$r('sys.color.ohos_id_color_text_primary')混合$r('sys.color.ohos_id_alpha_content_primary')的透明度。 |

**fontColor18+**

fontColor(resColor: Optional<ResourceColor>)

设置下拉按钮本身的文本颜色。与[fontColor](#ZH-CN_TOPIC_0000002553200803__fontcolor)相比，resColor参数新增了对undefined类型的支持。

元服务API： 从API version 18开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resColor | Optional<ResourceColor> | 是 | 下拉按钮本身的文本颜色。 当resColor的值为undefined时，默认值：$r('sys.color.ohos_id_color_text_primary')混合$r('sys.color.ohos_id_alpha_content_primary')的透明度。 当value的值为undefined时，维持上次取值。 |

**selectedOptionBgColor**

selectedOptionBgColor(value: ResourceColor)

设置下拉菜单选中项的背景色。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | ResourceColor | 是 | 下拉菜单选中项的背景色。 默认值：$r('sys.color.ohos_id_color_component_activated')混合$r('sys.color.ohos_id_alpha_highlight_bg')的透明度。 |

**selectedOptionBgColor18+**

selectedOptionBgColor(resColor: Optional<ResourceColor>)

设置下拉菜单选中项的背景色。与[selectedOptionBgColor](#ZH-CN_TOPIC_0000002553200803__selectedoptionbgcolor)相比，resColor参数新增了对undefined类型的支持。

元服务API： 从API version 18开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resColor | Optional<ResourceColor> | 是 | 下拉菜单选中项的背景色。 当resColor的值为undefined时，默认值：$r('sys.color.ohos_id_color_component_activated')混合$r('sys.color.ohos_id_alpha_highlight_bg')的透明度。 |

**selectedOptionFont**

selectedOptionFont(value: Font)

设置下拉菜单选中项的文本样式。当size为0的时候，文本不显示，当size为负值的时候，文本的size按照默认值显示。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Font | 是 | 下拉菜单选中项的文本样式。 默认值： { size: $r('sys.float.ohos_id_text_size_body1'), weight: FontWeight.Regular } |

**selectedOptionFont18+**

selectedOptionFont(selectFont: Optional<Font>)

设置下拉菜单选中项的文本样式。当size为0的时候，文本不显示，当size为负值的时候，文本的size按照默认值显示。与[selectedOptionFont](#ZH-CN_TOPIC_0000002553200803__selectedoptionfont)相比，selectFont参数新增了对undefined类型的支持。

元服务API： 从API version 18开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| selectFont | Optional<Font> | 是 | 下拉菜单选中项的文本样式。 当selectFont的值为undefined时，默认值： { size: $r('sys.float.ohos_id_text_size_body1'), weight: FontWeight.Regular } |

**selectedOptionFontColor**

selectedOptionFontColor(value: ResourceColor)

设置下拉菜单选中项的文本颜色。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | ResourceColor | 是 | 下拉菜单选中项的文本颜色。 默认值：$r('sys.color.ohos_id_color_text_primary_activated') |

**selectedOptionFontColor18+**

selectedOptionFontColor(resColor: Optional<ResourceColor>)

设置下拉菜单选中项的文本颜色。与[selectedOptionFontColor](#ZH-CN_TOPIC_0000002553200803__selectedoptionfontcolor)相比，resColor参数新增了对undefined类型的支持。

元服务API： 从API version 18开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resColor | Optional<ResourceColor> | 是 | 下拉菜单选中项的文本颜色。 当resColor的值为undefined时，默认值为$r('sys.color.ohos_id_color_text_primary_activated')。 |

**optionBgColor**

optionBgColor(value: ResourceColor)

设置下拉菜单项的背景色。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | ResourceColor | 是 | 下拉菜单项的背景色。 默认值： API version 11之前，默认值为Color.White。 API version 11及之后，默认值为Color.Transparent。 |

**optionBgColor18+**

optionBgColor(resColor: Optional<ResourceColor>)

设置下拉菜单项的背景色。与[optionBgColor](#ZH-CN_TOPIC_0000002553200803__optionbgcolor)相比，resColor参数新增了对undefined类型的支持。

元服务API： 从API version 18开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resColor | Optional<ResourceColor> | 是 | 下拉菜单项的背景色。 当resColor的值为undefined时，下拉菜单项的背景色为Color.White。 |

**optionFont**

optionFont(value: Font)

设置下拉菜单项的文本样式。当size为0的时候，文本不显示，当size为负值的时候，文本的size按照默认值显示。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Font | 是 | 下拉菜单项的文本样式。 默认值： { size: $r('sys.float.ohos_id_text_size_body1'), weight: FontWeight.Regular } |

**optionFont18+**

optionFont(selectFont: Optional<Font>)

设置下拉菜单项的文本样式。当size为0的时候，文本不显示，当size为负值的时候，文本的size按照默认值显示。

与[optionFont](#ZH-CN_TOPIC_0000002553200803__optionfont)相比，selectFont参数新增了对undefined类型的支持。

元服务API： 从API version 18开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| selectFont | Optional<Font> | 是 | 下拉菜单项的文本样式。 当selectFont的值为undefined时，默认值： { size: $r('sys.float.ohos_id_text_size_body1'), weight: FontWeight.Regular } |

**optionFontColor**

optionFontColor(value: ResourceColor)

设置下拉菜单项的文本颜色。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | ResourceColor | 是 | 下拉菜单项的文本颜色。 默认值：$r('sys.color.ohos_id_color_text_primary') |

**optionFontColor18+**

optionFontColor(resColor: Optional<ResourceColor>)

设置下拉菜单项的文本颜色。与[optionFontColor](#ZH-CN_TOPIC_0000002553200803__optionfontcolor)相比，resColor参数新增了对undefined类型的支持。

元服务API： 从API version 18开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resColor | Optional<ResourceColor> | 是 | 下拉菜单项的文本颜色。 当resColor的值为undefined时，默认值：$r('sys.color.ohos_id_color_text_primary') |

**space10+**

space(value: Length)

设置下拉菜单项的文本与箭头的间距。不支持设置百分比。将间距设置为null、undefined，或者小于等于8的值时，取默认值。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Length | 是 | 下拉菜单项的文本与箭头的间距。 默认值：8 说明： 设置string类型时，不支持百分比。 |

**space18+**

space(spaceLength: Optional<Length>)

设置下拉菜单项的文本与箭头的间距。不支持设置百分比。设置为null、undefined，或者小于等于8的值，取默认值。

元服务API： 从API version 18开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| spaceLength | Optional<Length> | 是 | 下拉菜单项的文本与箭头之间的间距。 当spaceLength的值为undefined时，默认值：8 |

**arrowPosition10+**

arrowPosition(value: ArrowPosition)

设置下拉菜单项的文本与箭头之间的对齐方式。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | ArrowPosition | 是 | 下拉菜单项的文本与箭头之间的对齐方式。 默认值：ArrowPosition.END |

**arrowPosition18+**

arrowPosition(position: Optional<ArrowPosition>)

设置下拉菜单项的文本与箭头之间的对齐方式。与[arrowPosition](#ZH-CN_TOPIC_0000002553200803__arrowposition10)相比，position参数新增了对undefined类型的支持。

元服务API： 从API version 18开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| position | Optional<ArrowPosition> | 是 | 下拉菜单项的文本与箭头之间的对齐方式。 当position的值为undefined时，默认值：ArrowPosition.END |

**menuAlign10+**

menuAlign(alignType: MenuAlignType, offset?: Offset)

设置下拉按钮与下拉菜单间的对齐方式。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| alignType | MenuAlignType | 是 | 对齐方式类型。 默认值：MenuAlignType.START |
| offset | Offset | 否 | 按照对齐类型对齐后，下拉菜单相对下拉按钮的偏移量。 默认值：{dx: 0, dy: 0} |

**menuAlign18+**

menuAlign(alignType: Optional<MenuAlignType>, offset?: Offset)

设置下拉按钮与下拉菜单间的对齐方式。与[menuAlign](#ZH-CN_TOPIC_0000002553200803__menualign10)10+相比，alignType参数新增了对undefined类型的支持。

元服务API： 从API version 18开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| alignType | Optional<MenuAlignType> | 是 | 对齐方式类型。 当alignType的值为undefined时，默认值：MenuAlignType.START |
| offset | Offset | 否 | 按照对齐类型对齐后，下拉菜单相对下拉按钮的偏移量。 默认值：{dx: 0, dy: 0} |

**optionWidth11+**

optionWidth(value: Dimension | OptionWidthMode )

设置下拉菜单项的宽度，不支持设置百分比。OptionWidthMode类型为枚举类型，OptionWidthMode决定下拉菜单是否继承下拉按钮宽度。

当设置为异常值或小于最小宽度56vp时，属性无效，菜单项宽度设为默认值，即2栅格。

Select组件距屏幕边缘的左右间距为16vp，建议将组件本身及菜单项的宽度设置为小于等于calc(100% - 32vp)的值，以避免下拉菜单弹出时发生偏移。

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Dimension | OptionWidthMode | 是 | 下拉菜单项的宽度。 |

**optionWidth18+**

optionWidth(width: Optional<Dimension | OptionWidthMode> )

设置下拉菜单项的宽度，不支持设置百分比。OptionWidthMode类型为枚举类型，OptionWidthMode决定下拉菜单是否继承下拉按钮宽度。与[optionWidth](#ZH-CN_TOPIC_0000002553200803__optionwidth11)11+相比，width参数新增了对undefined类型的支持。

当设置为异常值或小于最小宽度56vp时，属性无效，菜单项宽度设为默认值，即2栅格。

Select组件距屏幕边缘的左右间距为16vp，建议将组件本身及菜单项的宽度设置为小于等于calc(100% - 32vp)的值，以避免下拉菜单弹出时发生偏移。

元服务API： 从API version 18开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| width | Optional<Dimension | OptionWidthMode> | 是 | 下拉菜单项的宽度。 当width的值为undefined时，属性无效，菜单项宽度设为默认值，即2栅格。 |

**optionHeight11+**

optionHeight(value: Dimension)

设置下拉菜单显示的最大高度，不支持设置百分比。默认最大高度是屏幕可用高度的80%，设置的菜单最大高度不能超过默认最大高度。

当设置为异常值或零时，属性不生效。

如果下拉菜单所有选项的实际高度没有设定的高度大，下拉菜单的高度按实际高度显示。

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Dimension | 是 | 下拉菜单显示的最大高度。 |

**optionHeight18+**

optionHeight(height: Optional<Dimension>)

设置下拉菜单显示的最大高度，不支持设置百分比。默认最大高度是屏幕可用高度的80%，设置的菜单最大高度不能超过默认最大高度。与[optionHeight](#ZH-CN_TOPIC_0000002553200803__optionheight11)11+相比，height参数新增了对undefined类型的支持。

当设置为异常值或零时，属性不生效。

如果下拉菜单所有选项的实际高度小于设定的高度，下拉菜单的高度按实际高度显示。

元服务API： 从API version 18开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| height | Optional<Dimension> | 是 | 下拉菜单显示的最大高度。 当height的值为undefined时，属性不生效，下拉菜单最大高度设为默认值，即下拉菜单最大高度默认值为屏幕可用高度的80%。 |

**menuBackgroundColor11+**

menuBackgroundColor(value: ResourceColor)

设置下拉菜单的背景色。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

从API version 12开始，该接口支持在[attributeModifier](动态属性设置.md#ZH-CN_TOPIC_0000002522240800__attributemodifier)中调用。

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | ResourceColor | 是 | 下拉菜单的背景色。 默认值： API version 11之前，默认值为$r('sys.color.ohos_id_color_card_bg')。 API version 11及之后，默认值为Color.Transparent。 |

**menuBackgroundColor18+**

menuBackgroundColor(resColor: Optional<ResourceColor>)

设置下拉菜单的背景色。与[menuBackgroundColor](#ZH-CN_TOPIC_0000002553200803__menubackgroundcolor11)11+相比，resColor参数新增了对undefined类型的支持。

元服务API： 从API version 18开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resColor | Optional<ResourceColor> | 是 | 下拉菜单的背景色。 当resColor的值为undefined时，默认值为Color.Transparent。 |

**menuBackgroundBlurStyle11+**

menuBackgroundBlurStyle(value: BlurStyle)

设置下拉菜单的背景模糊材质。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

从API version 12开始，该接口支持在[attributeModifier](动态属性设置.md#ZH-CN_TOPIC_0000002522240800__attributemodifier)中调用。

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | BlurStyle | 是 | 下拉菜单的背景模糊材质。 默认值：BlurStyle.COMPONENT_ULTRA_THICK |

**menuBackgroundBlurStyle18+**

menuBackgroundBlurStyle(style: Optional<BlurStyle>)

设置下拉菜单的背景模糊材质。与[menuBackgroundBlurStyle](#ZH-CN_TOPIC_0000002553200803__menubackgroundblurstyle11)11+相比，style参数新增了对undefined类型的支持。

元服务API： 从API version 18开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| style | Optional<BlurStyle> | 是 | 下拉菜单的背景模糊材质。 当style的值为undefined时，默认值：BlurStyle.COMPONENT_ULTRA_THICK |

**avoidance19+**

avoidance(mode: AvoidanceMode)

设置下拉菜单的避让模式。

元服务API： 从API version 19开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | AvoidanceMode | 是 | 设置下拉菜单的避让模式。 默认值：AvoidanceMode.COVER_TARGET |

**menuOutline20+**

menuOutline(outline: MenuOutlineOptions)

设置下拉菜单框的外描边样式。

元服务API： 从API version 20开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| outline | MenuOutlineOptions | 是 | 下拉菜单框的外描边样式。 |

**showDefaultSelectedIcon20+**

showDefaultSelectedIcon(show: boolean)

设置是否显示默认选择的图标。

元服务API： 从API version 20开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| show | boolean | 是 | 是否显示默认选定的图标。 true：显示默认选择的图标；false：不显示默认选择的图标，通过突出显示背景色来表示选中。 默认值：false 当show为true时，若设置了selectedOptionBgColor选中项的背景色时，则同时显示选中项的背景色和默认选定的图标；若未通过selectedOptionBgColor设置选中项的背景色时，不突出显示背景色，只显示默认选定的图标。 |

**textModifier20+**

textModifier(modifier: Optional<[TextModifier](动态属性设置.md)>)

定制Select按钮文本样式的方法，在应用了textModifier之后，Select按钮的文本样式将完全由开发者自定义。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

该接口不支持在[attributeModifier](动态属性设置.md#ZH-CN_TOPIC_0000002522240800__attributemodifier)中调用。

元服务API： 从API version 20开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| modifier | Optional<TextModifier> | 是 | 在Select组件上，定制按钮文本样式的方法。 |

**arrowModifier20+**

arrowModifier(modifier: Optional<SymbolGlyphModifier>)

定制Select按钮下拉箭头图标样式的方法，在应用arrowModifier之后，Select按钮下拉箭头的图标样式将完全由开发者自定义。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

该接口不支持在[attributeModifier](动态属性设置.md#ZH-CN_TOPIC_0000002522240800__attributemodifier)中调用。

元服务API： 从API version 20开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| modifier | Optional<SymbolGlyphModifier> | 是 | 在Select组件上，定制Select按钮下拉箭头图标样式的方法。 |

**optionTextModifier20+**

optionTextModifier(modifier: Optional<[TextModifier](动态属性设置.md)>)

定制Select下拉菜单未选中项文本样式的方法，在应用optionTextModifier之后，下拉菜单未选中项的文本样式将完全由开发者自定义。

如果[optionFont](#ZH-CN_TOPIC_0000002553200803__optionfont)与optionTextModifier的Font属性同时设置，则优先使用[optionFont](#ZH-CN_TOPIC_0000002553200803__optionfont)设置下拉菜单未选中项的文本样式；[optionFont](#ZH-CN_TOPIC_0000002553200803__optionfont)中缺省的属性将设置为对应的默认值。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

该接口不支持在[attributeModifier](动态属性设置.md#ZH-CN_TOPIC_0000002522240800__attributemodifier)中调用。

元服务API： 从API version 20开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| modifier | Optional<TextModifier> | 是 | 在Select组件上，定制Select下拉菜单未选中项样式的方法。 |

**selectedOptionTextModifier20+**

selectedOptionTextModifier(modifier: Optional<[TextModifier](动态属性设置.md)>)

定制Select下拉菜单选中项文本样式的方法，在应用selectedOptionTextModifier之后，下拉菜单选中项的文本样式将完全由开发者自定义。

如果[selectedOptionFont](#ZH-CN_TOPIC_0000002553200803__selectedoptionfont)与selectedOptionTextModifier的Font属性同时设置，则优先使用[selectedOptionFont](#ZH-CN_TOPIC_0000002553200803__selectedoptionfont)设置下拉菜单选中项的文本样式；若未设置[selectedOptionFont](#ZH-CN_TOPIC_0000002553200803__selectedoptionfont)，则优先使用[optionFont](#ZH-CN_TOPIC_0000002553200803__optionfont)设置下拉菜单选中项的文本样式。其中[selectedOptionFont](#ZH-CN_TOPIC_0000002553200803__selectedoptionfont)或者[optionFont](#ZH-CN_TOPIC_0000002553200803__optionfont)缺省的属性将设置为对应的默认值。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

该接口不支持在[attributeModifier](动态属性设置.md#ZH-CN_TOPIC_0000002522240800__attributemodifier)中调用。

元服务API： 从API version 20开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| modifier | Optional<TextModifier> | 是 | 设置下拉菜单项选中项的文本样式。 开发者可以根据需要管理和维护文本的样式进行设置。 |

**showInSubWindow20+**

showInSubWindow(showInSubWindow:Optional<boolean>)

设置下拉菜单是否显示在子窗中。

元服务API： 从API version 20开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| showInSubWindow | Optional<boolean> | 是 | 设置下拉菜单是否显示在子窗中。 true代表下拉菜单显示在子窗中，仅对2in1设备生效。 false代表下拉菜单不显示在子窗中。 默认值：2in1设备为true，其他设备为false。 |

**keyboardAvoidMode23+**

keyboardAvoidMode(mode:Optional<MenuKeyboardAvoidMode>)

设置下拉菜单是否避让软键盘。未通过该接口设置时，默认不避让软键盘。

元服务API： 从API version 23开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

模型约束： 此接口仅可在Stage模型下使用。

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | Optional<MenuKeyboardAvoidMode> | 是 | 设置下拉菜单是否避让软键盘。取值为undefined时，按照MenuKeyboardAvoidMode.NONE处理，不避让软键盘。 |

**minKeyboardAvoidDistance23+**

minKeyboardAvoidDistance(distance:Optional<LengthMetrics>)

设置Select的菜单避让软键盘的最小距离。未通过该接口设置，最小距离默认为8vp。仅当[keyboardAvoidMode](#ZH-CN_TOPIC_0000002553200803__keyboardavoidmode23)设置为避让软键盘时生效。

元服务API： 从API version 23开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

模型约束： 此接口仅可在Stage模型下使用。

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| distance | Optional<LengthMetrics> | 是 | 设置下拉菜单避让软键盘的最小距离。设置为负数、undefined时，按照8vp处理。 |

**ArrowPosition10+枚举说明**

箭头的位置。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| END | 0 | 文字在前，箭头在后。 |
| START | 1 | 箭头在前，文字在后。 |

**MenuAlignType10+枚举说明**

下拉菜单的对齐方式。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| START | 0 | 按照语言方向起始端对齐。 |
| CENTER | 1 | 居中对齐。 |
| END | 2 | 按照语言方向末端对齐。 |

**AvoidanceMode19+枚举说明**

下拉菜单避让模式的枚举选项。

元服务API： 从API version 19开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

| 名称 | 说明 |
| --- | --- |
| COVER_TARGET | 目标组件下方无足够空间时，覆盖目标组件。 |
| AVOID_AROUND_TARGET | 目标组件四周无足够空间时，在最大空间处压缩显示（可滚动）。 |

**MenuItemConfiguration12+对象说明**

开发者需要自定义class实现ContentModifier接口。继承自[CommonConfiguration](自定义内容.md#ZH-CN_TOPIC_0000002553360727__commonconfigurationt)。

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| value | ResourceStr | 否 | 否 | 下拉菜单项的文本内容。 说明： 当文本字符的长度超过菜单项文本区域的宽度时，文本将会被截断。 |
| icon | ResourceStr | 否 | 是 | 下拉菜单项的图片内容。 说明： string格式可用于加载网络图片和本地图片。 |
| symbolIcon | SymbolGlyphModifier | 否 | 是 | 下拉选项Symbol图片内容。 |
| selected | boolean | 否 | 否 | 下拉菜单项是否被选中。值为true表示选中，值为false表示未选中。 默认值：false |
| index | number | 否 | 否 | 下拉菜单项的索引，索引值从0开始。 |
| triggerSelect | (index: number, value: string) :void | 否 | 否 | 下拉菜单选中某一项的回调函数。 index：选中菜单项的索引。 value：选中菜单项的文本。 说明： index会赋值给事件onSelect回调中的索引参数； value会返回给Select组件显示，同时会赋值给事件onSelect回调中的文本参数。 |

**MenuOutlineOptions20+对象说明**

下拉菜单框的外描边参数对象。

元服务API： 从API version 20开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| width | Dimension | EdgeOutlineWidths | 否 | 是 | 设置外描边宽度，不支持百分比。 默认值：0 |
| color | ResourceColor | EdgeColors | 否 | 是 | 设置外描边颜色。 默认值：#19ffffff |

**事件**

**onSelect**

onSelect(callback: (index: number, value: string) => void)

下拉菜单选中某一项时，会触发回调。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 选中项的索引，索引值从0开始。 |
| value | string | 是 | 选中项的值。 |

**onSelect18+**

onSelect(callback: Optional<OnSelectCallback> )

下拉菜单选中某一项时，会触发回调。与[onSelect](#ZH-CN_TOPIC_0000002553200803__onselect)相比，callback参数新增了对undefined类型的支持。

元服务API： 从API version 18开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Optional<OnSelectCallback> | 是 | 下拉菜单选中某一项的回调。 当callback的值为undefined时，不使用回调函数。 |

**OnSelectCallback18+**

type OnSelectCallback = (index: number, selectStr: string) => void

下拉菜单选中某一项时触发的回调函数类型定义。

元服务API： 从API version 18开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 选中项的索引，索引值从0开始。 |
| selectStr | string | 是 | 选中项的值。 |

**示例**

**示例1（设置下拉菜单）**

该示例通过配置[SelectOption](#ZH-CN_TOPIC_0000002553200803__selectoption对象说明)实现下拉菜单，并从API version 19开始通过设置[avoidance](#ZH-CN_TOPIC_0000002553200803__avoidance19)属性实现菜单的避让方式。

```ets
// xxx.ets
@Entry
@Component
struct SelectExample {
  @State text: string = "TTTTT";
  @State index: number = 2;
  @State space: number = 8;
  @State arrowPosition: ArrowPosition = ArrowPosition.END;

  build() {
    Column() {
      // $r('app.media.selection')需要替换为开发者所需的图像资源文件。
      Select([{ value: 'aaa', icon: $r("app.media.selection") },
        { value: 'bbb', icon: $r("app.media.selection") },
        { value: 'ccc', icon: $r("app.media.selection") },
        { value: 'ddd', icon: $r("app.media.selection") }])
        .selected(this.index)
        .value(this.text)
        .font({ size: 16, weight: 500 })
        .fontColor('#182431')
        .selectedOptionFont({ size: 16, weight: 400 })
        .optionFont({ size: 16, weight: 400 })
        .space(this.space)
        .arrowPosition(this.arrowPosition)
        .menuAlign(MenuAlignType.START, { dx: 0, dy: 0 })
        .optionWidth(200)
        .optionHeight(300)
        .onSelect((index: number, text?: string | undefined) => {
          console.info('Select:' + index);
          this.index = index;
          if (text) {
            this.text = text;
          }
        })
        .avoidance(AvoidanceMode.COVER_TARGET);
    }.width('100%')
  }
```

![image](public_sys-resources/zh-cn_image_0000002522084992.webp)

**示例2（设置symbol类型图标）**

该示例实现了一个下拉菜单中图片为Symbol的Select组件，并从API version 19开始通过设置[avoidance](#ZH-CN_TOPIC_0000002553200803__avoidance19)属性实现菜单的避让方式。

```ets
// xxx.ets
import { SymbolGlyphModifier } from '@kit.ArkUI';

@Entry
@Component
struct SelectExample {
  @State text: string = "TTTTT";
  @State index: number = 2;
  @State space: number = 8;
  @State arrowPosition: ArrowPosition = ArrowPosition.END;
  @State symbolModifier1: SymbolGlyphModifier =
    new SymbolGlyphModifier($r('sys.symbol.ohos_wifi')).fontColor([Color.Green]);
  @State symbolModifier2: SymbolGlyphModifier =
    new SymbolGlyphModifier($r('sys.symbol.ohos_star')).fontColor([Color.Red]);
  @State symbolModifier3: SymbolGlyphModifier =
    new SymbolGlyphModifier($r('sys.symbol.ohos_trash')).fontColor([Color.Gray]);
  @State symbolModifier4: SymbolGlyphModifier =
    new SymbolGlyphModifier($r('sys.symbol.exposure')).fontColor([Color.Gray]);

  build() {
    Column() {
      Select([{ value: 'aaa', symbolIcon: this.symbolModifier1 },
        { value: 'bbb', symbolIcon: this.symbolModifier2 },
        { value: 'ccc', symbolIcon: this.symbolModifier3 },
        { value: 'ddd', symbolIcon: this.symbolModifier4 }])
        .selected(this.index)
        .value(this.text)
        .font({ size: 16, weight: 500 })
        .fontColor('#182431')
        .selectedOptionFont({ size: 16, weight: 400 })
        .optionFont({ size: 16, weight: 400 })
        .space(this.space)
        .arrowPosition(this.arrowPosition)
        .menuAlign(MenuAlignType.START, { dx: 0, dy: 0 })
        .onSelect((index: number, text?: string | undefined) => {
          console.info('Select:' + index);
          this.index = index;
          if (text) {
            this.text = text;
          }
        })
        .avoidance(AvoidanceMode.COVER_TARGET);
    }.width('100%')
  }
```

![image](public_sys-resources/zh-cn_image_0000002553364907.webp)

**示例3（自定义下拉菜单）**

该示例实现了一个自定义下拉菜选项的Select组件。自定义下拉菜单选项样式为“文本 + Symbol图片 + 空白间隔 + 文本 + 绘制三角形”，点击菜单选项后Select组件显示菜单选项的文本内容。

```ets
import { SymbolGlyphModifier } from '@kit.ArkUI';

class MyMenuItemContentModifier implements ContentModifier<MenuItemConfiguration> {
  modifierText: string = "";

  constructor(text: string) {
    this.modifierText = text;
  }

  applyContent(): WrappedBuilder<[MenuItemConfiguration]> {
    return wrapBuilder(MenuItemBuilder);
  }

@Builder
function MenuItemBuilder(configuration: MenuItemConfiguration) {
  Row() {
    Text(configuration.value)
    Blank()
    if (configuration.symbolIcon) {
      SymbolGlyph().attributeModifier(configuration.symbolIcon).fontSize(24)
    } else if (configuration.icon) {
      Image(configuration.icon).size({ width: 24, height: 24 })
    }
    Blank(30)
    Text((configuration.contentModifier as MyMenuItemContentModifier).modifierText)
    Blank(30)
    Path()
      .width('100px')
      .height('150px')
      .commands('M40 0 L80 100 L0 100 Z')
      .fillOpacity(0)
      .stroke(Color.Black)
      .strokeWidth(3)
  }
  .onClick(() => {
    configuration.triggerSelect(configuration.index, configuration.value.valueOf().toString());
  })
}

@Entry
@Component
struct SelectExample {
  @State text: string = "Content Modifier Select";
  @State symbolModifier1: SymbolGlyphModifier =
    new SymbolGlyphModifier($r('sys.symbol.ohos_trash')).fontColor([Color.Gray]);
  @State symbolModifier2: SymbolGlyphModifier =
    new SymbolGlyphModifier($r('sys.symbol.exposure')).fontColor([Color.Gray]);

  build() {
    Column() {
      Row() {
        // $r('app.media.icon')需要替换为开发者所需的图像资源文件。
        Select([{ value: 'item1', icon: $r('app.media.icon'), symbolIcon: this.symbolModifier1 },
          { value: 'item1', icon: $r('app.media.icon'), symbolIcon: this.symbolModifier2 }])
          .value(this.text)
          .onSelect((index: number, text?: string) => {
            console.info('Select index:' + index);
            console.info('Select text:' + text);
          })
          .menuItemContentModifier(new MyMenuItemContentModifier("Content Modifier"))

      }.alignItems(VerticalAlign.Center).height('50%')
    }
```

![image](public_sys-resources/zh-cn_image_0000002522244986.webp)

**示例4（设置分割线样式）**

该示例通过配置divider的DividerOptions类型实现分割线样式的下拉菜单，并从API version 19开始通过设置[avoidance](#ZH-CN_TOPIC_0000002553200803__avoidance19)属性实现菜单的避让方式。

```ets
// xxx.ets
@Entry
@Component
struct SelectExample {
  @State text: string = "TTTTT";
  @State index: number = -1;
  @State arrowPosition: ArrowPosition = ArrowPosition.END;

  build() {
    Column() {
      // $r('app.media.icon')需要替换为开发者所需的图像资源文件。
      Select([{ value: 'aaa', icon: $r("app.media.icon") },
        { value: 'bbb', icon: $r("app.media.icon") },
        { value: 'ccc', icon: $r("app.media.icon") },
        { value: 'ddd', icon: $r("app.media.icon") }])
        .selected(this.index)
        .value(this.text)
        .font({ size: 16, weight: 500 })
        .fontColor('#182431')
        .selectedOptionFont({ size: 16, weight: 400 })
        .optionFont({ size: 16, weight: 400 })
        .arrowPosition(this.arrowPosition)
        .menuAlign(MenuAlignType.START, { dx: 0, dy: 0 })
        .optionWidth(200)
        .optionHeight(300)
        .divider({
          strokeWidth: 5,
          color: Color.Blue,
          startMargin: 10,
          endMargin: 10
        })
        .onSelect((index: number, text?: string | undefined) => {
          console.info('Select:' + index);
          this.index = index;
          if (text) {
            this.text = text;
          }
        })
        .avoidance(AvoidanceMode.COVER_TARGET);
    }.width('100%')
  }
```

![image](public_sys-resources/zh-cn_image_0000002553204947.webp)

**示例5（设置无分割线样式）**

该示例通过配置divider为null实现无分割线样式的下拉菜单，并从API version 19开始通过设置[avoidance](#ZH-CN_TOPIC_0000002553200803__avoidance19)属性实现菜单的避让方式。

```ets
// xxx.ets
@Entry
@Component
struct SelectExample {
  @State text: string = "TTTTT";
  @State index: number = -1;
  @State arrowPosition: ArrowPosition = ArrowPosition.END;

  build() {
    Column() {
      // $r('app.media.icon')需要替换为开发者所需的图像资源文件。
      Select([{ value: 'aaa', icon: $r("app.media.icon") },
        { value: 'bbb', icon: $r("app.media.icon") },
        { value: 'ccc', icon: $r("app.media.icon") },
        { value: 'ddd', icon: $r("app.media.icon") }])
        .selected(this.index)
        .value(this.text)
        .font({ size: 16, weight: 500 })
        .fontColor('#182431')
        .selectedOptionFont({ size: 16, weight: 400 })
        .optionFont({ size: 16, weight: 400 })
        .arrowPosition(this.arrowPosition)
        .menuAlign(MenuAlignType.START, { dx: 0, dy: 0 })
        .optionWidth(200)
        .optionHeight(300)
        .divider(null)
        .onSelect((index: number, text?: string | undefined) => {
          console.info('Select:' + index);
          this.index = index;
          if (text) {
            this.text = text;
          }
        })
        .avoidance(AvoidanceMode.COVER_TARGET);
    }.width('100%')
  }
```

![image](public_sys-resources/zh-cn_image_0000002522084994.webp)

**示例6（设置Select中文本和箭头样式）**

从API version 20开始，该示例通过[textModifier](#ZH-CN_TOPIC_0000002553200803__textmodifier20)和[arrowModifier](#ZH-CN_TOPIC_0000002553200803__arrowmodifier20)属性设置文本以及箭头样式。

```ets
import { TextModifier, SymbolGlyphModifier } from "@kit.ArkUI";

@Entry
@Component
struct SelectExample {
  @State text: string = "TTTTTTTTTT".repeat(3);
  @State index: number = 2;
  textModifier: TextModifier = new TextModifier();
  symbolGlyphModifier: SymbolGlyphModifier = new SymbolGlyphModifier();

  aboutToAppear(): void {
    this.textModifier
      .maxLines(2)
      .fontSize(18)
      .textAlign(TextAlign.Center)
      .fontColor('#333333')
      .fontWeight(FontWeight.Medium)
      .textOverflow({overflow:TextOverflow.Clip})

    this.symbolGlyphModifier
      .fontSize(25)
      .fontColor(['#999999'])
  }

  build() {
    Column() {
      Select([
        // $r('app.media.startIcon')需要替换为开发者所需的图像资源文件。
        { value: 'A very long option text that should be truncated nicely'.repeat(3), icon: $r("app.media.startIcon") },
        { value: 'Option B', icon: $r("app.media.startIcon") },
        { value: 'Option C', icon: $r("app.media.startIcon") },
        { value: 'Option D', icon: $r("app.media.startIcon") }
      ])
        .selected(this.index)
        .value(this.text)
        .textModifier(this.textModifier)
        .arrowModifier(this.symbolGlyphModifier)
        .onSelect((index: number, text?: string) => {
          console.info('Select:' + index);
          this.index = index;
          if (text) {
            this.text = text;
          }
        })
        .margin({ top: 20,left:30 })
        .borderRadius(12)
        .width(200)
        .padding(9)
        .backgroundColor(Color.White)
        .shadow({ radius: 10, color: '#888888', offsetX: 0, offsetY: 10 })
    }
    .alignItems(HorizontalAlign.Start)
    .padding(10)
    .backgroundColor('#F0F2F5')
    .width('100%')
    .height('100%')
  }
```

![image](public_sys-resources/zh-cn_image_0000002553364909.webp)

**示例7（设置Select下拉菜单选中和非选中项文本样式）**

从API version 20开始，该示例通过[optionTextModifier](#ZH-CN_TOPIC_0000002553200803__optiontextmodifier20)和[selectedOptionTextModifier](#ZH-CN_TOPIC_0000002553200803__selectedoptiontextmodifier20)属性设置下拉菜单选中和非选中项文本样式。

```ets
import { TextModifier } from "@kit.ArkUI";

@Entry
@Component
struct SelectExample {
  @State text: string = "TTTTTTTTTT".repeat(3);
  @State index: number = 2;
  optionTextModifier: TextModifier = new TextModifier();
  selectedOptionTextModifier: TextModifier = new TextModifier();
  aboutToAppear(): void {
    this.optionTextModifier
      .maxLines(1)
      .fontSize(16)
      .textAlign(TextAlign.Start)
      .fontColor('#666666')
      .fontWeight(FontWeight.Normal)
      .width(200)

    this.selectedOptionTextModifier
      .maxLines(1)
      .fontSize(18)
      .textAlign(TextAlign.Start)
      .fontColor('#007BFF')
      .fontWeight(FontWeight.Bold)
      .width(200)
  }

  build() {
    Column() {
      Select([
        // $r('app.media.startIcon')需要替换为开发者所需的图像资源文件。
        { value: 'A very long option text that should be truncated nicely'.repeat(3), icon: $r("app.media.startIcon") },
        { value: 'Option B', icon: $r("app.media.startIcon") },
        { value: 'Option C', icon: $r("app.media.startIcon") },
        { value: 'Option D', icon: $r("app.media.startIcon") }
      ])
        .selected(this.index)
        .value(this.text)
        .onSelect((index: number, text?: string) => {
          console.info('Select:' + index);
          this.index = index;
          if (text) {
            this.text = text;
          }
        })
        .optionTextModifier(this.optionTextModifier)
        .selectedOptionTextModifier(this.selectedOptionTextModifier)
        .margin({ top: 20,left:30 })
        .borderRadius(12)
        .width(200)
        .padding(9)
        .backgroundColor(Color.White)
        .shadow({ radius: 10, color: '#888888', offsetX: 0, offsetY: 10 })
    }
    .alignItems(HorizontalAlign.Start)
    .padding(10)
    .backgroundColor('#F0F2F5')
    .width('100%')
    .height('100%')
  }
```

![image](public_sys-resources/zh-cn_image_0000002522244988.webp)

**示例8（设置分割线模式）**

从API version 19开始，该示例通过配置[DividerStyleOptions](基础类型定义.md#ZH-CN_TOPIC_0000002553360849__dividerstyleoptions12)的mode属性设置分割线模式。

```ets
import { LengthMetrics } from '@kit.ArkUI'

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Select([{ value: "SelectItem" }, { value: "SelectItem" }, { value: "SelectItem" },])
        .value("请选择")
        .dividerStyle({
          strokeWidth: LengthMetrics.vp(5),
          color: '#d5d5d5',
          mode: DividerMode.EMBEDDED_IN_MENU
        })
    }
    .height('100%')
    .width('100%')
  }
```

![image](public_sys-resources/zh-cn_image_0000002553204949.webp)

**示例9（设置Select下拉菜单外描边样式）**

从API version 20开始该示例通过配置menuOutline的width和color属性设置下拉菜单外描边样式。

```ets
// xxx.ets
@Entry
@Component
struct SelectExample {
  @State text: string = "TTTTT";
  @State index: number = -1;
  @State arrowPosition: ArrowPosition = ArrowPosition.END;

  build() {
    Column() {
      Select([{ value: 'aaa' },
        { value: 'bbb' },
        { value: 'ccc' },
        { value: 'ddd' }])
        .selected(this.index)
        .value(this.text)
        .font({ size: 16, weight: 500 })
        .fontColor('#182431')
        .selectedOptionFont({ size: 16, weight: 400 })
        .optionFont({ size: 16, weight: 400 })
        .arrowPosition(this.arrowPosition)
        .menuAlign(MenuAlignType.START, { dx: 0, dy: 0 })
        .optionWidth(200)
        .optionHeight(300)
        .menuOutline({
          width: '5vp',
          color: Color.Blue
        })
        .onSelect((index: number, text?: string | undefined) => {
          console.info('Select:' + index);
          this.index = index;
          if (text) {
            this.text = text;
          }
        })
    }
    .width('100%')
    .height('100%')
    .backgroundColor('#F0F2F5')
  }
```

![image](public_sys-resources/zh-cn_image_0000002522084996.webp)

**示例10（设置Select的弹出菜单避让软键盘）**

该示例通过调用[keyboardAvoidMode](#ZH-CN_TOPIC_0000002553200803__keyboardavoidmode23)和[minKeyboardAvoidDistance](#ZH-CN_TOPIC_0000002553200803__minkeyboardavoiddistance23)接口，实现下拉菜单避让软键盘并自定义避让软键盘的最小距离。

从API version 23开始，新增keyboardAvoidMode、minKeyboardAvoidDistance接口。

```ets
import { inputMethod } from '@kit.IMEKit';
import { LengthMetrics } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  private inputController: inputMethod.InputMethodController = inputMethod.getController();

  build() {
    RelativeContainer() {
      Select([{ value: 'SelectOption' },
        { value: 'SelectOption' },
        { value: 'SelectOption' }])
        .value('Click Show Options')
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center },
        })
        .keyboardAvoidMode(MenuKeyboardAvoidMode.TRANSLATE_AND_RESIZE)
        .minKeyboardAvoidDistance(LengthMetrics.vp(20))
        .onClick(() => {
          setTimeout(() => {
            this.attachAndListener()
          }, 2000)
        })
    }
    .height('100%')
    .width('100%')
  }

  async attachAndListener() {
    focusControl.requestFocus('Index')
    try {
      await this.inputController.attach(true, {
        inputAttribute: {
          textInputType: inputMethod.TextInputType.TEXT,
          enterKeyType: inputMethod.EnterKeyType.SEARCH
        }
      })
    } catch (err) {
      console.error('Fail to attach')
    }
```

![image](public_sys-resources/zh-cn_image_0000002553364911.webp)