# RichEditor

支持图文混排和文本交互式编辑的组件。

  ![image](public_sys-resources/note_3.0-zh-cn.webp)

该组件从API version 10开始支持。后续版本新增内容，采用上角标单独标记该内容的起始版本。

**子组件**

不包含子组件。

**接口**

**RichEditor**

RichEditor(value: RichEditorOptions)

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | RichEditorOptions | 是 | 富文本组件初始化选项。 |

**RichEditor12+**

RichEditor(options: RichEditorStyledStringOptions)

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | RichEditorStyledStringOptions | 是 | 富文本组件初始化选项。 |

**属性**

除支持[通用属性](通用属性.md)外，还支持以下属性：

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

- align属性只支持上方、中间和下方位置的对齐方式。

- 不支持[borderImage](图片边框设置.md#ZH-CN_TOPIC_0000002553360707__borderimage)属性。

- 组件水平方向默认padding为16vp，竖直方向默认padding为8vp。

**customKeyboard**

customKeyboard(value: CustomBuilder | ComponentContent | undefined, options?: KeyboardOptions | undefined)

设置自定义键盘。

当设置自定义键盘时，输入框激活后不会打开系统输入法，而是加载指定的自定义组件。

自定义键盘的高度可以通过自定义组件根节点的height属性设置，宽度不可设置，使用系统默认值。

自定义键盘无法获取焦点，但是会拦截手势事件。

默认在输入控件失去焦点时，关闭自定义键盘。

自定义键盘支持接续功能，使用[setCustomKeyboardContinueFeature](Class (UIContext).md#ZH-CN_TOPIC_0000002522240732__setcustomkeyboardcontinuefeature23)接口，可以设置自定义键盘之间切换时是否接续。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

从API version 23开始，该接口支持在[attributeModifier](动态属性设置.md#ZH-CN_TOPIC_0000002522240800__attributemodifier)中调用。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | CustomBuilder | ComponentContent23+ | undefined23+ | 是 | 自定义键盘。 传入undefined时默认使用系统键盘。 |
| options12+ | KeyboardOptions | undefined23+ | 否 | 设置自定义键盘是否支持避让功能。 传入undefined时默认不支持避让。 |

**bindSelectionMenu**

bindSelectionMenu(spanType: RichEditorSpanType, content: CustomBuilder, responseType: ResponseType | RichEditorResponseType, options?: SelectionMenuOptions)

设置自定义选择菜单。自定义菜单超长时，建议内部嵌套[Scroll](Scroll.md)组件使用，避免键盘被遮挡。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| spanType | RichEditorSpanType | 是 | 菜单的类型。 默认值： RichEditorSpanType.TEXT |
| content | CustomBuilder | 是 | 菜单的内容。 |
| responseType | ResponseType | RichEditorResponseType | 是 | 菜单的响应类型。 默认值： ResponseType.LongPress |
| options | SelectionMenuOptions | 否 | 菜单的选项。 |

**copyOptions**

copyOptions(value: CopyOptions)

设置组件是否支持文本内容可复制粘贴。

从API version 20开始，RichEditor组件在执行复制或剪切操作时，会将HTML格式的内容添加到剪贴板中。

-

仅支持TextSpan和ImageSpan向剪贴板中添加HTML内容，其他Span类型（如BuilderSpan、SymbolSpan、CustomSpan）则不能添加。

-

设置RichEditor组件的属性字符串时，请参考属性字符串[toHtml](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-styled-string14)接口文档，以了解支持转换为HTML的范围。

copyOptions不为CopyOptions.None时，长按组件内容，会弹出文本选择菜单。如果通过bindSelectionMenu等方式自定义文本选择菜单，则会弹出自定义的菜单。

设置copyOptions为CopyOptions.None时，禁用复制、剪切、翻译、分享、搜索、帮写功能，且不支持拖拽操作。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | CopyOptions | 是 | 组件支持文本内容是否可复制粘贴。 默认值：CopyOptions.LocalDevice |

**enableDataDetector11+**

enableDataDetector(enable: boolean)

设置是否进行文本特殊实体识别。

该接口依赖设备底层应具有文本识别能力，否则设置不会生效。

当enableDataDetector设置为true且未指定[dataDetectorConfig](#ZH-CN_TOPIC_0000002522080846__datadetectorconfig11)属性时，系统将默认识别所有类型的实体，并将这些实体的color和decoration更改为预设样式：

```ets
color: '#ff007dff'
decoration:{
  type: TextDecorationType.Underline,
  color: '#ff007dff',
  style: TextDecorationStyle.SOLID
}
```

触摸点击或鼠标右键点击实体时，会根据实体类型弹出对应的实体操作菜单，鼠标左键点击实体会直接响应菜单的第一个选项。

对addBuilderSpan的节点文本，该功能不会生效。

当copyOptions设置为CopyOptions.None时，点击实体弹出的菜单没有选择文本和复制功能。

从API version 20开始，组件文本选择菜单支持显示AI菜单。

当enableDataDetector设置为true，并且[copyOptions](#ZH-CN_TOPIC_0000002522080846__copyoptions)设置为CopyOptions.LocalDevice或CopyOptions.CROSS_DEVICE，组件在非编辑态选中内容，选中区包含单个AI实体时，根据AI实体的类型，在文本选择菜单中显示AI菜单选项。

AI菜单选项包括[TextMenuItemId](文本组件公共接口.md#ZH-CN_TOPIC_0000002553200813__textmenuitemid12)中的url（打开链接）、email（新建邮件）、phoneNumber（呼叫）、address（导航至该位置）、dateTime（新建日程提醒）。

从API version 20开始，组件文本选择菜单支持显示问问小艺。

组件在编辑态下，[copyOptions](#ZH-CN_TOPIC_0000002522080846__copyoptions)设置为CopyOptions.LocalDevice或CopyOptions.CROSS_DEVICE，组件内选中任意文本内容时，文本选择菜单与鼠标右键菜单中都可以显示问问小艺选项。组件在非编辑态下，enableDataDetector设置为true，并且[copyOptions](#ZH-CN_TOPIC_0000002522080846__copyoptions)设置为CopyOptions.LocalDevice或CopyOptions.CROSS_DEVICE，组件内选中文本，文本选择菜单与鼠标右键菜单中不显示其他AI菜单时，显示问问小艺选项。

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | boolean | 是 | 使能文本识别。 true表示使能文本特殊实体识别，false表示不使能文本特殊实体识别。 默认值： false |

**dataDetectorConfig11+**

dataDetectorConfig(config: TextDataDetectorConfig)

设置文本特殊实体识别配置，可配置识别类型、实体显示样式，并可选择是否开启长按预览功能。

需配合[enableDataDetector](#ZH-CN_TOPIC_0000002522080846__enabledatadetector11)一起使用，设置enableDataDetector为true时，dataDetectorConfig的配置才能生效。

当有两个实体A、B重叠时，按以下规则保留实体：

1. 若A ⊂ B，则保留B，反之则保留A。

2. 当A ⊄ B且B ⊄ A时，若A.start < B.start，则保留A，反之则保留B。

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| config | TextDataDetectorConfig | 是 | 文本识别配置。 |

**enableSelectedDataDetector22+**

enableSelectedDataDetector(enable: boolean | undefined)

设置是否启用文本选择的AI菜单功能。启用后可识别选区中的邮件、电话、网址、日期、地址等，并在文本选择菜单中展示对应的AI菜单项。默认启用AI菜单功能。

AI菜单功能启用时，在组件中选中文本后，文本选择菜单能够展示对应的AI菜单项，包括[TextMenuItemId](文本组件公共接口.md#ZH-CN_TOPIC_0000002553200813__textmenuitemid12)中的url（打开连接）、email（新建邮件）、phoneNumber（呼叫）、address（导航前往）、dateTime（新建日程）。

AI菜单生效时，选中范围内需包括且仅包括一个完整的AI实体，才能展示对应的选项。该菜单项与[TextMenuItemId](文本组件公共接口.md#ZH-CN_TOPIC_0000002553200813__textmenuitemid12)中的askAI菜单项不同时出现。

本功能仅在[copyOptions](#ZH-CN_TOPIC_0000002522080846__copyoptions)为CopyOptions.LocalDevice或CopyOptions.CROSS_DEVICE时生效。

该接口依赖设备底层具有文本识别能力，否则设置不会生效。

元服务API： 从API version 22开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | boolean | undefined | 是 | 是否启用选择文本识别，true表示启用，false表示不启用。 传入undefined或null时属性重置为默认值。 |

**enablePreviewText12+**

enablePreviewText(enable: boolean)

设置是否开启预上屏功能。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

从API version 18开始，该接口支持在[attributeModifier](动态属性设置.md#ZH-CN_TOPIC_0000002522240800__attributemodifier)中调用。

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | boolean | 是 | 使能预上屏功能。 true表示开启，false表示不开启。 默认值： true |

该接口在CAPI场景使用时默认关闭。可以在工程的module.json5中配置[metadata](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/module-structure#metadata对象内部结构)字段控制是否启用预上屏，配置如下：

```ets
"metadata": [
  {
    "name": "can_preview_text",
    "value": "true"
  }
]
```

**placeholder12+**

placeholder(value: ResourceStr, style?: PlaceholderStyle)

设置无输入时的提示文本。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

从API version 18开始，该接口支持在[attributeModifier](动态属性设置.md#ZH-CN_TOPIC_0000002522240800__attributemodifier)中调用。

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | ResourceStr | 是 | 无输入时的提示文本。 |
| style | PlaceholderStyle | 否 | 提示文本的字体样式。 缺省时默认跟随主题。 |

**caretColor12+**

caretColor(value: ResourceColor)

设置输入框光标、手柄颜色。

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | ResourceColor | 是 | 输入框光标、手柄颜色。 默认值：'#007DFF' |

**selectedBackgroundColor12+**

selectedBackgroundColor(value: ResourceColor)

设置文本选中的底板颜色。如果未设置不透明度，默认为20%不透明度。

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | ResourceColor | 是 | 文本选中的底板颜色。 默认为20%不透明度。 |

**editMenuOptions12+**

editMenuOptions(editMenu: EditMenuOptions)

设置系统默认菜单的扩展项，允许配置扩展项的文本内容、图标和回调方法。

调用[disableMenuItems](Class (TextMenuController).md#ZH-CN_TOPIC_0000002553360657__disablemenuitems20)或[disableSystemServiceMenuItems](Class (TextMenuController).md#ZH-CN_TOPIC_0000002553360657__disablesystemservicemenuitems20)接口屏蔽文本选择菜单内的系统服务菜单项时，editMenuOptions接口内回调方法[onCreateMenu](文本组件公共接口.md#ZH-CN_TOPIC_0000002553200813__oncreatemenu12)的入参列表中不包含被屏蔽的菜单选项。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

从API version 18开始，该接口支持在[attributeModifier](动态属性设置.md#ZH-CN_TOPIC_0000002522240800__attributemodifier)中调用。

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| editMenu | EditMenuOptions | 是 | 扩展菜单选项。 |

**enterKeyType12+**

enterKeyType(value: EnterKeyType)

设置软键盘输入法回车键类型。

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | EnterKeyType | 是 | 软键盘输入法回车键类型。 默认为EnterKeyType.NEW_LINE。 |

**enableKeyboardOnFocus12+**

enableKeyboardOnFocus(isEnabled: boolean)

设置RichEditor通过点击以外的方式获焦时，是否主动拉起软键盘。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

从API version 18开始，该接口支持在[attributeModifier](动态属性设置.md#ZH-CN_TOPIC_0000002522240800__attributemodifier)中调用。

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isEnabled | boolean | 是 | 通过点击以外的方式获焦时，是否主动拉起软键盘。 true表示主动拉起软键盘，false表示不主动拉起软键盘。 默认值： true |

**barState13+**

barState(state: BarState)

设置RichEditor滚动条的显示模式。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

从API version 18开始，该接口支持在[attributeModifier](动态属性设置.md#ZH-CN_TOPIC_0000002522240800__attributemodifier)中调用。

元服务API： 从API version 13开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| state | BarState | 是 | 输入框滚动条的显示模式。 默认值：BarState.Auto |

**maxLength18+**

maxLength(maxLength: Optional<number>)

设置组件内容的最大长度。当内容（包含文本、图片、Symbol和Builder）的总长度达到此值时，将无法继续添加内容。

元服务API： 从API version 18开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| maxLength | Optional<number> | 是 | 文本的最大输入字符数。 默认值：Infinity，可以无限输入，支持undefined类型。 说明： 当不设置该属性或设置异常值时，取默认值，设置小数时，取整数部分。 |

**maxLines18+**

maxLines(maxLines: Optional<number>)

设置富文本可显示的最大行数。maxLines为可显示行数，当设置maxLines时，超出内容可滚动显示。同时设置组件高度和最大行数，组件高度优先生效。

元服务API： 从API version 18开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| maxLines | Optional<number> | 是 | 设置富文本可显示的最大行数。maxLines为可显示行数，当设置maxLines时，超出内容可滚动显示。同时设置组件高度和最大行数，组件高度优先生效。 默认值：UINT32_MAX，可以无限输入，支持undefined类型。 取值范围：(0, UINT32_MAX] |

**enableHapticFeedback13+**

enableHapticFeedback(isEnabled: boolean)

设置RichEditor是否支持触感反馈。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

从API version 20开始，该接口支持在[attributeModifier](动态属性设置.md#ZH-CN_TOPIC_0000002522240800__attributemodifier)中调用。

元服务API： 从API version 13开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isEnabled | boolean | 是 | 控制触感反馈的开关。 默认值：true。true表示开启触感反馈，false表示关闭触感反馈。 说明： 触感反馈需应用具备ohos.permission.VIBRATE权限，用户已启用触感反馈，且系统硬件支持时才会生效。 |

**keyboardAppearance15+**

keyboardAppearance(appearance: Optional<KeyboardAppearance>)

设置键盘外观。

元服务API： 从API version 15开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| appearance | Optional<KeyboardAppearance> | 是 | 键盘外观。 默认值：KeyboardAppearance.NONE_IMMERSIVE |

**stopBackPress18+**

stopBackPress(isStopped: Optional<boolean>)

设置是否阻止返回键传递。

元服务API： 从API version 18开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isStopped | Optional<boolean> | 是 | 是否阻止返回键。 true表示阻止，false表示不阻止。 默认值：true。异常值取默认值。 |

**undoStyle20+**

undoStyle(style: Optional<UndoStyle>)

设置撤销还原时是否保留原内容的样式。

使用[RichEditorStyledStringOptions](#ZH-CN_TOPIC_0000002522080846__richeditorstyledstringoptions12)构建RichEditor组件时，撤销还原时默认保留原内容样式，不受该接口设置的属性影响。

元服务API： 从API version 20开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| style | Optional<UndoStyle> | 是 | 撤销还原是否保留原样式选项。默认值：UndoStyle.CLEAR_STYLE |

**enableAutoSpacing20+**

enableAutoSpacing(enable: Optional<boolean>)

设置是否开启中文与西文的自动间距。

元服务API： 从API version 20开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | Optional<boolean> | 是 | 是否开启中文与西文的自动间距。 true为开启自动间距，false为不开启。 默认值：false |

**scrollBarColor21+**

scrollBarColor(color: Optional<ColorMetrics>)

设置组件滚动条颜色。

元服务API： 从API version 21开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| color | Optional<ColorMetrics> | 是 | 设置组件滚动条颜色。 默认值：'#66182431'，显示为灰色。 说明： 设置异常值时按默认值处理。 |

**includeFontPadding23+**

includeFontPadding(include: Optional<boolean>)

设置是否在首行和尾行增加间距以避免文字截断。不通过该接口设置，默认不增加间距。

元服务API： 从API version 23开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| include | Optional<boolean> | 是 | 是否在首行和尾行增加间距以避免文字截断。 true表示在首行和尾行增加间距；false表示在首行和尾行不增加间距。 |

**fallbackLineSpacing23+**

fallbackLineSpacing(enabled: Optional<boolean>)

针对多行文字叠加，支持行高基于文字实际高度自适应。不通过该接口设置，默认行高不基于文字实际高度自适应。

该接口依赖[RichEditorTextStyle](#ZH-CN_TOPIC_0000002522080846__richeditortextstyle)的lineHeight属性。当lineHeight设置值小于当前字号下文本渲染出的实际高度时，fallbackLineSpacing属性将生效。

元服务API： 从API version 23开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | Optional<boolean> | 是 | 行高是否基于文字实际高度自适应。 true表示行高基于文字实际高度自适应；false表示行高不基于文字实际高度自适应。 |

**compressLeadingPunctuation23+**

compressLeadingPunctuation(enabled: Optional<boolean>)

设置是否开启行首标点符号压缩。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

行首标点符号默认不压缩。

支持压缩的标点符号，请参考[ParagraphStyle](@ohos.graphics.text (文本模块).md#ZH-CN_TOPIC_0000002553362061__paragraphstyle)的行首压缩的标点范围。

元服务API： 从API version 23开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | Optional<boolean> | 是 | 是否开启行首标点符号压缩。 true表示开启行首标点符号压缩；false表示不开启行首标点符号压缩。 |

**selectedDragPreviewStyle23+**

selectedDragPreviewStyle(value: SelectedDragPreviewStyle | undefined)

设置拖动预览样式。

元服务API： 从API version 23开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | SelectedDragPreviewStyle | undefined | 是 | 拖动预览样式。如果设置为undefined，样式将被重置。 |

**singleLine23+**

singleLine(isEnable: boolean | undefined)

设置是否启用单行模式。未通过该接口设置时，默认不启用单行模式。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

单行模式不显示滚动条。

单行模式下换行符会显示为空格。

元服务API： 从API version 23开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isEnable | boolean | undefined | 是 | 是否启用单行模式。 true表示启用单行模式；false表示不启用单行模式。 设置为undefined或null时，按照false处理，不启用单行模式。 |

**事件**

除支持[通用事件](通用事件.md)外，还支持[OnDidChangeCallback](文本组件公共接口.md#ZH-CN_TOPIC_0000002553200813__ondidchangecallback12)、[StyledStringChangedListener](文本组件公共接口.md#ZH-CN_TOPIC_0000002553200813__styledstringchangedlistener12)、[StyledStringChangeValue](文本组件公共接口.md#ZH-CN_TOPIC_0000002553200813__styledstringchangevalue12)和以下事件：

**onReady**

onReady(callback:Callback<void>)

富文本组件初始化完成后触发回调。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<void> | 是 | 订阅富文本组件初始化完成的回调。 |

**onSelect**

onSelect(callback:Callback<[RichEditorSelection](#ZH-CN_TOPIC_0000002522080846__richeditorselection)>)

鼠标左键双击选中内容触发回调；松开鼠标左键再次触发回调。

手指长按选中内容触发回调；松开手指再次触发回调。

通过手指或鼠标连续修改选中区、三击选段场景，不回调onSelect。

需要实时感知选中区变化的场景和使用[RichEditorStyledStringOptions](#ZH-CN_TOPIC_0000002522080846__richeditorstyledstringoptions12)构建的RichEditor组件，请使用onSelectionChange接口。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<RichEditorSelection> | 是 | RichEditorSelection为选中的所有span信息。 选择时触发的回调。 |

**aboutToIMEInput**

aboutToIMEInput(callback:Callback<[RichEditorInsertValue](#ZH-CN_TOPIC_0000002522080846__richeditorinsertvalue), boolean>)

输入法输入内容前触发回调。

使用[RichEditorStyledStringOptions](#ZH-CN_TOPIC_0000002522080846__richeditorstyledstringoptions12)构建的RichEditor组件不支持该回调。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<RichEditorInsertValue, boolean> | 是 | RichEditorInsertValue为输入法将要输入内容信息。 true:组件执行添加内容操作。 false:组件不执行添加内容操作。 输入法输入内容前的回调。 |

**onDidIMEInput12+**

onDidIMEInput(callback:Callback<TextRange>)

输入法输入完成后，触发回调。

使用[RichEditorStyledStringOptions](#ZH-CN_TOPIC_0000002522080846__richeditorstyledstringoptions12)构建的RichEditor组件不支持该回调。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

从API version 20开始，该接口支持在[attributeModifier](动态属性设置.md#ZH-CN_TOPIC_0000002522240800__attributemodifier)中调用。

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<TextRange> | 是 | TextRange为输入法本次输入内容的范围。 输入法完成输入时的回调。 |

**onIMEInputComplete**

onIMEInputComplete(callback:Callback<[RichEditorTextSpanResult](#ZH-CN_TOPIC_0000002522080846__richeditortextspanresult)>)

输入法输入完成后，触发回调。

该接口仅支持返回一个文本span的信息，当编辑操作涉及返回多个文本span信息时，建议使用[onDidIMEInput](#ZH-CN_TOPIC_0000002522080846__ondidimeinput12)接口。

使用[RichEditorStyledStringOptions](#ZH-CN_TOPIC_0000002522080846__richeditorstyledstringoptions12)构建的RichEditor组件不支持该回调。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<RichEditorTextSpanResult> | 是 | RichEditorTextSpanResult为输入法完成输入后的文本Span信息。 输入法完成输入后的回调。 |

**aboutToDelete**

aboutToDelete(callback:Callback<[RichEditorDeleteValue](#ZH-CN_TOPIC_0000002522080846__richeditordeletevalue), boolean>)

输入法删除内容前，触发回调。

使用[RichEditorStyledStringOptions](#ZH-CN_TOPIC_0000002522080846__richeditorstyledstringoptions12)构建的RichEditor组件不支持该回调。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<RichEditorDeleteValue, boolean> | 是 | RichEditorDeleteValue为准备删除的内容所在的文本或者图片Span信息。 true:组件执行删除操作。 false:组件不执行删除操作。 输入法删除内容前的回调，英文预上屏点击候选词时会执行该回调。 |

**onDeleteComplete**

onDeleteComplete(callback:Callback<void>)

输入法删除内容后，触发回调。

使用[RichEditorStyledStringOptions](#ZH-CN_TOPIC_0000002522080846__richeditorstyledstringoptions12)构建的RichEditor组件不支持该回调。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<void> | 是 | 订阅输入法完成删除内容的回调。 |

**onPaste11+**

onPaste(callback: [PasteEventCallback](#ZH-CN_TOPIC_0000002522080846__pasteeventcallback12) )

粘贴时，触发回调。开发者可以通过该方法，覆盖系统默认行为，实现图文的粘贴。

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | PasteEventCallback | 是 | 订阅粘贴时的回调。 |

**onSelectionChange12+**

onSelectionChange(callback:Callback<[RichEditorRange](#ZH-CN_TOPIC_0000002522080846__richeditorrange)>)

内容选择区域或编辑状态下的光标位置发生变化时，将触发该回调。光标位置变化时，回调中选择区域的起始和终止位置相等。

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<RichEditorRange> | 是 | RichEditorRange为所有内容的选择区域起始和终止位置。 订阅文本选择区域发生变化或编辑状态下光标位置发生变化时触发的回调。 |

**onEditingChange12+**

onEditingChange(callback: Callback<boolean>)

组件内容的编辑状态发生变化时触发该回调函数。

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<boolean> | 是 | true表示编辑态，false表示非编辑态。 |

**onSubmit12+**

onSubmit(callback: SubmitCallback)

按下软键盘输入法回车键时触发该回调。

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | SubmitCallback | 是 | 订阅事件的回调。 |

**onWillChange12+**

onWillChange(callback: Callback<[RichEditorChangeValue](#ZH-CN_TOPIC_0000002522080846__richeditorchangevalue12) , boolean>)

在组件执行增删操作前，触发回调。

使用[RichEditorStyledStringOptions](#ZH-CN_TOPIC_0000002522080846__richeditorstyledstringoptions12)构建的RichEditor组件不支持该回调。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

从API version 18开始，该接口支持在[attributeModifier](动态属性设置.md#ZH-CN_TOPIC_0000002522240800__attributemodifier)中调用。

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<RichEditorChangeValue , boolean> | 是 | RichEditorChangeValue为图文变化信息；boolean表示当前图文是否允许被更改，true：允许图文被更改；false：不允许图文被更改。 |

**onDidChange12+**

onDidChange(callback: OnDidChangeCallback)

在组件执行增删操作后，触发回调。如果文本实际未发生增删，则不触发该回调。

使用[RichEditorStyledStringOptions](#ZH-CN_TOPIC_0000002522080846__richeditorstyledstringoptions12)构建的RichEditor组件不支持该回调。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

从API version 18开始，该接口支持在[attributeModifier](动态属性设置.md#ZH-CN_TOPIC_0000002522240800__attributemodifier)中调用。

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | OnDidChangeCallback | 是 | 图文变化前后的内容范围。 |

**onCut12+**

onCut(callback: Callback<CutEvent>)

剪切时触发回调。开发者可以通过该方法，覆盖系统默认行为，实现图文的剪切。

使用[RichEditorStyledStringOptions](#ZH-CN_TOPIC_0000002522080846__richeditorstyledstringoptions12)构建的RichEditor组件，默认支持图文的剪切。

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<CutEvent> | 是 | 定义用户剪切事件。 |

**onCopy12+**

onCopy(callback: Callback<CopyEvent>)

复制时触发回调。开发者可以通过该方法，覆盖系统默认行为，实现图文的复制。

使用[RichEditorStyledStringOptions](#ZH-CN_TOPIC_0000002522080846__richeditorstyledstringoptions12)构建的RichEditor组件，默认支持图文的复制。

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<CopyEvent> | 是 | 定义用户复制事件。 |

**onWillAttachIME22+**

onWillAttachIME(callback: Callback<IMEClient> | undefined)

在组件绑定输入法前，触发回调。

调用[IMEClient](文本组件公共接口.md#ZH-CN_TOPIC_0000002553200813__imeclient20对象说明)的[setExtraConfig](文本组件公共接口.md#ZH-CN_TOPIC_0000002553200813__setextraconfig22)方法设置输入法扩展信息。在绑定输入法成功后，输入法会收到扩展信息，输入法可以依据此信息实现自定义功能。

元服务API： 从API version 22开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<IMEClient> | undefined | 是 | 在组件绑定输入法前触发的回调。 值为undefined时清除已绑定的回调事件。 |

**RichEditorInsertValue**

插入文本的信息。

系统能力： SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| insertOffset | number | 否 | 否 | 插入的文本偏移位置。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| insertValue | string | 否 | 否 | 插入的文本内容。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| previewText12+ | string | 否 | 是 | 插入的预上屏文本内容。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |

**RichEditorDeleteValue**

删除操作和被删除内容的信息。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| offset | number | 否 | 否 | 删除内容的偏移位置。 |
| direction | RichEditorDeleteDirection | 否 | 否 | 删除操作的方向。 |
| length | number | 否 | 否 | 删除内容长度。 |
| richEditorDeleteSpans | Array<RichEditorTextSpanResult | RichEditorImageSpanResult> | 否 | 否 | 删除的文本或图片Span的信息。 |

**RichEditorDeleteDirection**

删除方向。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

| 名称 | 说明 |
| --- | --- |
| BACKWARD | 向后删除。 |
| FORWARD | 向前删除。 |

**RichEditorTextSpanResult**

文本Span信息。

系统能力： SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| spanPosition | RichEditorSpanPosition | 否 | 否 | Span位置。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| value | string | 否 | 否 | 文本Span内容或Symbol的id。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| textStyle | RichEditorTextStyleResult | 否 | 否 | 文本Span样式信息。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| offsetInSpan | [number, number] | 否 | 否 | 文本Span内容里有效内容的起始和结束位置。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| valueResource11+ | Resource | 否 | 是 | 组件SymbolSpan内容。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| symbolSpanStyle11+ | RichEditorSymbolSpanStyle | 否 | 是 | 组件SymbolSpan样式信息。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| paragraphStyle12+ | RichEditorParagraphStyle | 否 | 是 | 段落样式。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| previewText12+ | string | 否 | 是 | 文本Span预上屏内容。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| urlStyle19+ | RichEditorUrlStyle | 否 | 是 | url信息。 默认值：undefined 元服务API： 从API version 19开始，该接口支持在元服务中使用。 |

**RichEditorSpanPosition**

Span位置信息。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| spanIndex | number | 否 | 否 | Span索引值。 |
| spanRange | [number, number] | 否 | 否 | Span内容在RichEditor内的起始和结束位置。 |

**RichEditorSpanType**

Span类型信息。

系统能力： SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| TEXT | 0 | Span类型为文字。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| IMAGE | 1 | Span类型为图像。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| MIXED | 2 | Span类型为图文混合。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| BUILDER12+ | 3 | Span类型为BuilderSpan。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| DEFAULT15+ | 4 | 注册此类型的菜单，但未注册TEXT、IMAGE、MIXED、BUILDER菜单时，文字类型、图像类型、图文混合类型、BuilderSpan类型都会触发并显示此类型对应的菜单。 元服务API： 从API version 15开始，该接口支持在元服务中使用。 |

**RichEditorResponseType11+**

菜单的响应类型。

系统能力： SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| RIGHT_CLICK | 0 | 通过鼠标右键触发菜单弹出。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| LONG_PRESS | 1 | 通过长按触发菜单弹出。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| SELECT | 2 | 通过鼠标选中触发菜单弹出。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| DEFAULT15+ | 3 | 注册此响应类型的菜单，但未注册RIGHT_CLICK、LONG_PRESS、SELECT响应类型的菜单时，通过鼠标右键、长按、鼠标选中都会触发菜单弹出。 元服务API： 从API version 15开始，该接口支持在元服务中使用。 |

**UndoStyle20+**

撤销还原是否保留原样式选项。

元服务API： 从API version 20开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CLEAR_STYLE | 0 | 撤销还原内容不保留原样式。 |
| KEEP_STYLE | 1 | 撤销还原内容保留原样式。 |

**RichEditorTextStyleResult**

后端返回的文本样式信息。

系统能力： SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| fontColor | ResourceColor | 否 | 否 | 文本颜色。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| fontSize | number | 否 | 否 | 字体大小，默认单位为fp。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| fontStyle | FontStyle | 否 | 否 | 字体样式。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| fontWeight | number | 否 | 否 | 字体粗细。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| fontFamily | string | 否 | 否 | 字体列表。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| decoration | DecorationStyleResult | 否 | 否 | 文本装饰线样式信息。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| textShadow12+ | Array<ShadowOptions> | 否 | 是 | 文字阴影效果。 说明： 仅支持查询阴影模糊半径、颜色和偏移量。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| lineHeight12+ | number | 否 | 是 | 文本行高，默认单位为fp。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| letterSpacing12+ | number | 否 | 是 | 文本字符间距，默认单位为fp。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| fontFeature12+ | string | 否 | 是 | 文字特性效果。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| halfLeading18+ | boolean | 否 | 是 | 文本是否将行间距平分至行的顶部与底部。 true表示将行间距平分至行的顶部与底部，false则不平分。 默认值：false。 元服务API： 从API version 18开始，该接口支持在元服务中使用。 |
| textBackgroundStyle18+ | TextBackgroundStyle | 否 | 是 | 文本背景样式。 元服务API： 从API version 18开始，该接口支持在元服务中使用。 |
| strokeWidth23+ | number | 否 | 是 | 文本描边宽度。 单位为vp。 元服务API： 从API version 23开始，该接口支持在元服务中使用。 |
| strokeColor23+ | ResourceColor | 否 | 是 | 文本描边颜色。 元服务API： 从API version 23开始，该接口支持在元服务中使用。 |

在RichEditorTextStyle中，fontWeight是设置字体粗细的输入参数。

而在RichEditorTextStyleResult中，会将之前设置的字体粗细转换为数字后返回。

转换关系如下：

| RichEditorTextStyle中的fontWeight | RichEditorTextStyleResult中的fontWeight |
| --- | --- |
| 100 | 0 |
| 200 | 1 |
| 300 | 2 |
| 400 | 3 |
| 500 | 4 |
| 600 | 5 |
| 700 | 6 |
| 800 | 7 |
| 900 | 8 |
| Lighter | 12 |
| Normal | 10 |
| Regular | 14 |
| Medium | 13 |
| Bold | 9 |
| Bolder | 11 |

RichEditorSymbolSpanStyle和RichEditorSymbolSpanStyleResult中fontWeight的转换关系，与RichEditorTextStyle和RichEditorTextStyleResult中fontWeight的转换关系一致。

**RichEditorSymbolSpanStyleResult11+**

后端返回的SymbolSpan样式信息。

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| fontColor | Array<ResourceColor> | 否 | 否 | SymbolSpan组件颜色。 默认值：不同渲染策略下默认值不同。 |
| fontSize | number | string | Resource | 否 | 否 | SymbolSpan组件大小，默认单位为fp。 默认值：跟随主题。 |
| fontWeight | number | FontWeight | string | 否 | 否 | SymbolSpan组件粗细。 number类型取值[100,900]，取值间隔为100，默认为400，取值越大，字体越粗。 string类型仅支持number类型取值的字符串形式，例如“400”，以及“bold”、“bolder”、“lighter”、“regular” 、“medium”分别对应FontWeight中相应的枚举值。 默认值：FontWeight.Normal。 |
| renderingStrategy | SymbolRenderingStrategy | 否 | 否 | SymbolSpan组件渲染策略。 默认值：SymbolRenderingStrategy.SINGLE。 |
| effectStrategy | SymbolEffectStrategy | 否 | 否 | SymbolSpan组件动效策略。 默认值：SymbolEffectStrategy.NONE。 |

**RichEditorImageSpanResult**

后端返回的图片信息。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| spanPosition | RichEditorSpanPosition | 否 | 否 | Span位置。 |
| valuePixelMap | PixelMap | 否 | 是 | 图片内容。 |
| valueResourceStr | ResourceStr | 否 | 是 | 图片资源id。 |
| imageStyle | RichEditorImageSpanStyleResult | 否 | 否 | 图片样式。 |
| offsetInSpan | [number, number] | 否 | 否 | Span里图片的起始和结束位置。 |

**RichEditorImageSpanStyleResult**

后端返回的图片样式信息。

系统能力： SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| size | [number, number] | 否 | 否 | 图片的宽度和高度，单位为px。默认值：size的默认值与objectFit的值有关，不同的objectFit值对应的size默认值也不同。objectFit的值为Cover时，图片高度为组件高度减去组件上下内边距，图片宽度为组件宽度减去组件左右内边距。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| verticalAlign | ImageSpanAlignment | 否 | 否 | 图片垂直对齐方式。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| objectFit | ImageFit | 否 | 否 | 图片缩放类型。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| layoutStyle12+ | RichEditorLayoutStyle | 否 | 是 | 图片布局风格。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |

**RichEditorLayoutStyle11+**

图片布局信息。

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| margin | Dimension | Margin | 否 | 是 | 外边距类型，用于描述组件不同方向的外边距。 参数为Dimension类型时，四个方向外边距同时生效。 |
| borderRadius | Dimension | BorderRadiuses | 否 | 是 | 圆角类型，用于描述组件边框圆角半径。 参数为Dimension类型时，不支持以Percentage形式设置。 |

**RichEditorOptions**

RichEditor初始化参数。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| controller | RichEditorController | 否 | 否 | 富文本控制器。 |

**RichEditorStyledStringOptions12+**

RichEditor初始化参数。

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| controller | RichEditorStyledStringController | 否 | 否 | 富文本控制器。 |

**RichEditorChangeValue12+**

图文变化信息。

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| rangeBefore | TextRange | 否 | 否 | 即将被替换内容的开始和结束索引。 |
| replacedSpans | Array<RichEditorTextSpanResult> | 否 | 否 | 替换后文本Span的具体信息。 |
| replacedImageSpans | Array<RichEditorImageSpanResult> | 否 | 否 | 替换后ImageSpan的具体信息。 |
| replacedSymbolSpans | Array<RichEditorTextSpanResult> | 否 | 否 | 替换后SymbolSpan的具体信息。 |

**RichEditorBaseController12+**

RichEditor组件控制器基类。

**getCaretOffset10+**

getCaretOffset(): number

返回当前光标所在位置。

当无法获取光标位置时（例如controller未与组件绑定时），该接口返回-1。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

返回值：

| 类型 | 说明 |
| --- | --- |
| number | 当前光标所在位置。 |

**setCaretOffset10+**

setCaretOffset(offset: number): boolean

设置光标位置。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| offset | number | 是 | 光标偏移位置。超出所有内容范围时，设置失败。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| boolean | 光标是否设置成功。 true表示光标位置设置成功，false表示未成功。 |

**closeSelectionMenu10+**

closeSelectionMenu(): void

关闭自定义选择菜单或系统默认选择菜单。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

**getTypingStyle11+**

getTypingStyle(): RichEditorTextStyle

获取用户预设的文本样式。

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

返回值：

| 类型 | 说明 |
| --- | --- |
| RichEditorTextStyle | 用户预设样式。 当controller未绑定组件或绑定controller的组件被释放时，返回undefined。 |

**setTypingStyle11+**

setTypingStyle(value: RichEditorTextStyle): void

设置用户预设的文本样式。

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | RichEditorTextStyle | 是 | 预设样式。 |

**setTypingParagraphStyle20+**

setTypingParagraphStyle(style: RichEditorParagraphStyle): void

设置用户预设的段落样式。仅在组件内容为空或组件末尾换行后，输入文本生效。

元服务API： 从API version 20开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| style | RichEditorParagraphStyle | 是 | 预设段落样式。 |

**setSelection11+**

setSelection(selectionStart: number, selectionEnd: number, options?: SelectionOptions): void

支持设置组件内的内容选中，选中部分背板高亮。

selectionStart和selectionEnd均为-1时表示全选，均为0时可以清空选中区。

未获焦时调用该接口不产生选中效果。

从API version 12开始，在2in1设备中，无论options取何值，调用setSelection接口都不会弹出菜单，此外，如果组件中已经存在菜单，调用setSelection接口会关闭菜单。

在非2in1设备中，options取值为MenuPolicy.DEFAULT时，遵循以下规则：

1.

组件内有手柄菜单时，接口调用后不关闭菜单，并且调整菜单位置。

1.

组件内有不带手柄的菜单时，接口调用后不关闭菜单，并且菜单位置不变。

1.

组件内无菜单时，接口调用后也无菜单显示。

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| selectionStart | number | 是 | 选中开始位置。 |
| selectionEnd | number | 是 | 选中结束位置。 |
| options12+ | SelectionOptions | 否 | 选择项配置。 |

**isEditing12+**

isEditing(): boolean

获取当前富文本的编辑状态。

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

返回值：

| 类型 | 说明 |
| --- | --- |
| boolean | true为编辑态，false为非编辑态。 |

**stopEditing12+**

stopEditing(): void

退出编辑态。

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

**getLayoutManager12+**

getLayoutManager(): LayoutManager

获取布局管理器对象。

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

返回值：

| 类型 | 说明 |
| --- | --- |
| LayoutManager | 布局管理器对象。 当controller未绑定组件或绑定controller的组件被释放时，返回undefined。 |

**getPreviewText12+**

getPreviewText(): PreviewText

获取预上屏信息。

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

返回值：

| 类型 | 说明 |
| --- | --- |
| PreviewText | 预上屏信息。 当controller未绑定组件或绑定controller的组件被释放时，返回undefined。 |

**getCaretRect18+**

getCaretRect(): RectResult | undefined

返回当前光标与RichEditor组件的相对位置。如果光标不闪烁，返回undefined。

元服务API： 从API version 18开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

返回值：

| 类型 | 说明 |
| --- | --- |
| RectResult | undefined | 当前光标与RichEditor的相对位置。 |

**deleteBackward23+**

deleteBackward(): void

提供删除字符能力。没有内容被选中时，删除当前光标位置前的1个字符。有内容被选中时，删除选中内容。

该接口不支持预上屏场景使用。

元服务API： 从API version 23开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

**RichEditorController**

RichEditor组件的控制器，继承自[RichEditorBaseController](#ZH-CN_TOPIC_0000002522080846__richeditorbasecontroller12)。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

当内容的长度超过组件显示区域的高度时，调用插入接口（例如[addTextSpan](#ZH-CN_TOPIC_0000002522080846__addtextspan)、[addImageSpan](#ZH-CN_TOPIC_0000002522080846__addimagespan)、[addBuilderSpan](#ZH-CN_TOPIC_0000002522080846__addbuilderspan11)、[addSymbolSpan](#ZH-CN_TOPIC_0000002522080846__addsymbolspan11)），组件会自动滚动内容使得插入内容末尾可见。

**导入对象**

```ets
controller: RichEditorController = new RichEditorController();
```

**addTextSpan**

addTextSpan(content: ResourceStr, options?: RichEditorTextSpanOptions): number

添加文本内容，如果组件光标闪烁，插入后光标位置更新为新插入文本的后面。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| content | ResourceStr | 是 | 文本内容。 从API version 20开始，支持Resource类型。 |
| options | RichEditorTextSpanOptions | 否 | 文本选项。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| number | 添加完成的TextSpan在所有Span中的索引位置。 |

**addImageSpan**

addImageSpan(value: PixelMap | ResourceStr, options?: RichEditorImageSpanOptions): number

添加图片内容，如果组件光标闪烁，插入后光标位置更新为新插入图片的后面。

该接口为同步接口，在弱网环境下，直接添加网络图片可能会阻塞UI线程造成冻屏问题。不建议直接添加网络图片。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | PixelMap | ResourceStr | 是 | 图片内容。 |
| options | RichEditorImageSpanOptions | 否 | 图片选项。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| number | 添加完成的ImageSpan在所有Span中的索引位置。 |

**addBuilderSpan11+**

addBuilderSpan(value: CustomBuilder, options?: RichEditorBuilderSpanOptions): number

在RichEditor中添加用户自定义布局（BuilderSpan）。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

- RichEditor组件添加占位Span，占位Span调用系统的measure方法计算真实的长宽和位置。

- 可通过[RichEditorBuilderSpanOptions](#ZH-CN_TOPIC_0000002522080846__richeditorbuilderspanoptions11)设置此builder在RichEditor中的index（一个文字为一个单位）。

- 此占位Span不可获焦，支持拖拽，支持部分通用属性，占位、删除等能力等同于ImageSpan，长度视为一个文字。

- 支持通过[bindSelectionMenu](#ZH-CN_TOPIC_0000002522080846__bindselectionmenu)设置自定义菜单。

- 不支持通过[getSpans](#ZH-CN_TOPIC_0000002522080846__getspans)，[getSelection](#ZH-CN_TOPIC_0000002522080846__getselection11)，[onSelect](#ZH-CN_TOPIC_0000002522080846__onselect)，[aboutToDelete](#ZH-CN_TOPIC_0000002522080846__abouttodelete)获取builderSpan信息。

- 不支持通过[updateSpanStyle](#ZH-CN_TOPIC_0000002522080846__updatespanstyle)，[updateParagraphStyle](#ZH-CN_TOPIC_0000002522080846__updateparagraphstyle11)等方式更新builder。

- 对此builder节点进行复制或粘贴不生效。

- builder的布局约束由RichEditor传入，如果builder里最外层组件不设置大小，则会用RichEditor的大小作为maxSize。

- builder的手势相关事件机制与通用手势事件相同，如果builder中未设置透传，则仅有builder中的子组件响应。

- 如果组件光标闪烁，插入后光标位置更新为新插入builder的后面。

通用属性仅支持[size](尺寸设置.md#ZH-CN_TOPIC_0000002553360703__size)、[padding](尺寸设置.md#ZH-CN_TOPIC_0000002553360703__padding)、[margin](尺寸设置.md#ZH-CN_TOPIC_0000002553360703__margin)、[aspectRatio](布局约束.md#ZH-CN_TOPIC_0000002553200743__aspectratio)、[borderStyle](边框设置.md#ZH-CN_TOPIC_0000002522080782__borderstyle)、[borderWidth](边框设置.md#ZH-CN_TOPIC_0000002522080782__borderwidth)、[borderColor](边框设置.md#ZH-CN_TOPIC_0000002522080782__bordercolor)、[borderRadius](边框设置.md#ZH-CN_TOPIC_0000002522080782__borderradius)、[backgroundColor](背景设置.md#ZH-CN_TOPIC_0000002553200739__backgroundcolor)、[backgroundBlurStyle](背景设置.md#ZH-CN_TOPIC_0000002553200739__backgroundblurstyle9)、[opacity](透明度设置.md)、[blur](图像效果.md#ZH-CN_TOPIC_0000002553360709__blur)、[backdropBlur](背景设置.md#ZH-CN_TOPIC_0000002553200739__backdropblur)、[shadow](图像效果.md#ZH-CN_TOPIC_0000002553360709__shadow)、[grayscale](图像效果.md#ZH-CN_TOPIC_0000002553360709__grayscale)、[brightness](图像效果.md#ZH-CN_TOPIC_0000002553360709__brightness)、[saturate](图像效果.md#ZH-CN_TOPIC_0000002553360709__saturate)、[contrast](图像效果.md#ZH-CN_TOPIC_0000002553360709__contrast)、[invert](图像效果.md#ZH-CN_TOPIC_0000002553360709__invert)、[sepia](图像效果.md#ZH-CN_TOPIC_0000002553360709__sepia)、[hueRotate](图像效果.md#ZH-CN_TOPIC_0000002553360709__huerotate)、[colorBlend](图像效果.md#ZH-CN_TOPIC_0000002553360709__colorblend)、[linearGradientBlur](图像效果.md#ZH-CN_TOPIC_0000002553360709__lineargradientblur12)、[clip](形状裁剪.md#ZH-CN_TOPIC_0000002522240784__clip12)、[mask](形状裁剪.md#ZH-CN_TOPIC_0000002522240784__mask12)、[foregroundBlurStyle](组件内容模糊.md#ZH-CN_TOPIC_0000002522080788__foregroundblurstyle)、[accessibilityGroup](无障碍属性.md#ZH-CN_TOPIC_0000002553360723__accessibilitygroup)、[accessibilityText](无障碍属性.md#ZH-CN_TOPIC_0000002553360723__accessibilitytext)、[accessibilityDescription](无障碍属性.md#ZH-CN_TOPIC_0000002553360723__accessibilitydescription)、[accessibilityLevel](无障碍属性.md#ZH-CN_TOPIC_0000002553360723__accessibilitylevel)、[sphericalEffect](图像效果.md#ZH-CN_TOPIC_0000002553360709__sphericaleffect12)、[lightUpEffect](图像效果.md#ZH-CN_TOPIC_0000002553360709__lightupeffect12)、[pixelStretchEffect](图像效果.md#ZH-CN_TOPIC_0000002553360709__pixelstretcheffect12)。

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | CustomBuilder | 是 | 自定义组件。 |
| options | RichEditorBuilderSpanOptions | 否 | builder选项。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| number | 添加完成的builderSpan在所有Span中的索引位置。 |

**addSymbolSpan11+**

addSymbolSpan(value: Resource, options?: RichEditorSymbolSpanOptions ): number

在RichEditor中添加图标小符号（SymbolSpan），如果组件光标闪烁，插入后光标位置更新为新插入SymbolSpan的后面。

暂不支持手势、复制、拖拽处理。

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Resource | 是 | symbol资源信息。 |
| options | RichEditorSymbolSpanOptions | 否 | symbol选项。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| number | 添加完成的SymbolSpan在所有Span中的索引位置。 |

**updateSpanStyle**

updateSpanStyle(value: RichEditorUpdateTextSpanStyleOptions | RichEditorUpdateImageSpanStyleOptions | RichEditorUpdateSymbolSpanStyleOptions): void

更新文本、图片或SymbolSpan样式。

若只更新了一个Span的部分内容，则会根据更新部分、未更新部分将该Span拆分为多个Span。

使用该接口更新文本、图片或SymbolSpan样式时默认不会关闭自定义文本选择菜单。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | RichEditorUpdateTextSpanStyleOptions | RichEditorUpdateImageSpanStyleOptions | RichEditorUpdateSymbolSpanStyleOptions | 是 | 文本、图片或SymbolSpan的样式选项信息。 |

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

当start大于end时为异常情况，此时start为0，end为无穷大。

**updateParagraphStyle11+**

updateParagraphStyle(value: RichEditorParagraphStyleOptions): void

更新段落的样式。

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | RichEditorParagraphStyleOptions | 是 | 段落的样式选项信息。 |

**getSpans**

getSpans(value?: RichEditorRange): Array<RichEditorImageSpanResult | RichEditorTextSpanResult>

获取span信息。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | RichEditorRange | 否 | 需要获取span范围。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Array<RichEditorImageSpanResult | RichEditorTextSpanResult> | 文本和图片Span信息。 当controller未绑定组件或绑定controller的组件被释放时，返回undefined。 |

**deleteSpans**

deleteSpans(value?: RichEditorRange): void

删除指定范围内的文本和图片。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | RichEditorRange | 否 | 删除范围。省略时，删除所有文本和图片。 |

**getParagraphs11+**

getParagraphs(value?: RichEditorRange): Array<RichEditorParagraphResult>

获取指定范围的段落信息。

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | RichEditorRange | 否 | 需要获取段落的范围。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Array<RichEditorParagraphResult> | 选中段落的信息。 当controller未绑定组件或绑定controller的组件被释放时，返回undefined。 |

**getSelection11+**

getSelection(): RichEditorSelection

获取选中内容的范围和span信息。未选中时，返回光标所在span信息。

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

返回值：

| 类型 | 说明 |
| --- | --- |
| RichEditorSelection | 选中内容信息。 当controller未绑定组件或绑定controller的组件被释放时，返回undefined。 |

**fromStyledString12+**

fromStyledString(value: StyledString): Array<RichEditorSpan>

将属性字符串转换为span信息。

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | StyledString | 是 | 转换前的属性字符串。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Array<RichEditorSpan> | 文本和图片Span信息。 |

错误码：

以下错误码的详细介绍请参考[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. |

**toStyledString12+**

toStyledString(value: RichEditorRange): StyledString

将给定范围的组件内容转换成属性字符串，SymbolSpan和BuilderSpan不支持转换。

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | RichEditorRange | 是 | 需要获取的范围。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| StyledString | 转换后的属性字符串 |

错误码：

以下错误码详细介绍请参考[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. |

**RichEditorStyledStringController12+**

使用属性字符串构建的RichEditor组件的控制器，继承自[RichEditorBaseController](#ZH-CN_TOPIC_0000002522080846__richeditorbasecontroller12)。

**导入对象**

```ets
controller: RichEditorStyledStringController = new RichEditorStyledStringController();
```

**getSelection12+**

getSelection(): RichEditorRange

获取富文本当前的选中区域范围。

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

返回值：

| 类型 | 说明 |
| --- | --- |
| RichEditorRange | 选中区域范围。 当controller未绑定组件或绑定controller的组件被释放时，返回undefined。 |

**setStyledString12+**

setStyledString(styledString: StyledString): void

设置富文本组件显示的属性字符串。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

- 调用该接口时，会全量替换富文本组件的StyledString，并重新渲染。

- 当内容超过组件本身区域时，组件会自动向上滚动内容直到末尾处可见。

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| styledString | StyledString | 是 | 属性字符串。 说明： StyledString的子类MutableStyledString也可以作为入参值。 |

**getStyledString12+**

getStyledString(): MutableStyledString

获取富文本组件显示的属性字符串。

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

返回值：

| 类型 | 说明 |
| --- | --- |
| MutableStyledString | 富文本组件显示的属性字符串。 当controller未绑定组件或绑定controller的组件被释放时，返回undefined。 |

**onContentChanged12+**

onContentChanged(listener: StyledStringChangedListener): void

注册文本内容变化回调，该回调仅在后端程序导致文本内容变更时触发，调用[setStyledString](#ZH-CN_TOPIC_0000002522080846__setstyledstring12)时不会触发。

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| listener | StyledStringChangedListener | 是 | 文本内容变化回调监听器。 |

**RichEditorSelection**

选中内容信息。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| selection | [number, number] | 否 | 否 | 选中范围。 |
| spans | Array<RichEditorTextSpanResult | RichEditorImageSpanResult> | 否 | 否 | span信息。 |

**RichEditorRange**

定义RichEditor的范围。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| start | number | 否 | 是 | 需要更新样式的文本起始位置，省略或者设置负值时表示从0开始。 |
| end | number | 否 | 是 | 需要更新样式的文本结束位置，省略或者超出文本范围时表示无穷大。 |

**RichEditorSpanStyleOptions**

文本样式选项。

继承自[RichEditorRange](#ZH-CN_TOPIC_0000002522080846__richeditorrange)。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

**RichEditorUpdateTextSpanStyleOptions**

文本样式选项。

继承自[RichEditorSpanStyleOptions](#ZH-CN_TOPIC_0000002522080846__richeditorspanstyleoptions)。

系统能力： SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| textStyle | RichEditorTextStyle | 否 | 否 | 文本样式。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| urlStyle19+ | RichEditorUrlStyle | 否 | 是 | url信息。 默认值：undefined 元服务API： 从API version 19开始，该接口支持在元服务中使用。 |

**RichEditorUpdateImageSpanStyleOptions**

图片的样式选项。

继承自[RichEditorSpanStyleOptions](#ZH-CN_TOPIC_0000002522080846__richeditorspanstyleoptions)。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| imageStyle | RichEditorImageSpanStyle | 否 | 否 | 图片样式。 |

**RichEditorUpdateSymbolSpanStyleOptions11+**

SymbolSpan样式选项。

继承自[RichEditorSpanStyleOptions](#ZH-CN_TOPIC_0000002522080846__richeditorspanstyleoptions)。

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| symbolStyle | RichEditorSymbolSpanStyle | 否 | 否 | 组件样式。 |

**RichEditorParagraphStyleOptions11+**

段落样式选项。

继承自[RichEditorRange](#ZH-CN_TOPIC_0000002522080846__richeditorrange)。

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| style | RichEditorParagraphStyle | 否 | 否 | 段落样式。 |

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

接口作用的范围：设定的区间所涉及的段落。

**RichEditorParagraphStyle11+**

段落样式。

系统能力： SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| textAlign | TextAlign | 否 | 是 | 设置文本段落在水平方向的对齐方式。默认值：TextAlign.START 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| leadingMargin | Dimension | LeadingMarginPlaceholder | 否 | 是 | 设置文本段落缩进，当段落仅存在ImageSpan或BuilderSpan时，此属性值不生效。参数为Dimension类型时，不支持以Percentage形式设置。默认值：{"size":["0.00px","0.00px"]} 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| wordBreak12+ | WordBreak | 否 | 是 | 设置断行规则。 默认值：WordBreak.BREAK_WORD 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| lineBreakStrategy12+ | LineBreakStrategy | 否 | 是 | 设置折行规则。 默认值：LineBreakStrategy.GREEDY 在wordBreak不等于breakAll的时候生效，不支持连字符。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| paragraphSpacing19+ | number | 否 | 是 | 设置段落间距大小。 单位：fp 段落间距默认大小为0。 元服务API： 从API version 19开始，该接口支持在元服务中使用。 |
| textVerticalAlign20+ | TextVerticalAlign | 否 | 是 | 设置文本段落在垂直方向的对齐方式。 默认值：TextVerticalAlign.BASELINE 元服务API： 从API version 20开始，该接口支持在元服务中使用。 |
| textDirection23+ | TextDirection | 否 | 是 | 设置文本方向。 默认值：TextDirection.DEFAULT 元服务API： 从API version 23开始，该接口支持在元服务中使用。 |

**LeadingMarginPlaceholder11+**

前导边距占位符，用于表示文本段落左侧与组件边缘之间的距离。

系统能力： SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| pixelMap | PixelMap | 否 | 否 | 图片内容。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| size | [Dimension, Dimension] | 否 | 否 | 图片大小，不支持设置百分比。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |

**RichEditorParagraphResult11+**

后端返回的段落信息。

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| style | RichEditorParagraphStyle | 否 | 否 | 段落样式。 |
| range | [number, number] | 否 | 否 | 段落起始和结束位置。 |

**RichEditorTextSpanOptions**

添加文本的偏移位置和文本样式信息。

系统能力： SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| offset | number | 否 | 是 | 添加文本的位置。省略时，添加到所有内容的最后。 当值小于0时，放在所有内容最前面；当值大于所有内容长度时，放在所有内容最后面。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| style | RichEditorTextStyle | 否 | 是 | 文本样式信息。省略时，使用系统默认文本信息。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| paragraphStyle11+ | RichEditorParagraphStyle | 否 | 是 | 段落样式。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| gesture11+ | RichEditorGesture | 否 | 是 | 行为触发回调。省略时，仅使用系统默认行为。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| urlStyle19+ | RichEditorUrlStyle | 否 | 是 | url信息。 默认值：undefined 元服务API： 从API version 19开始，该接口支持在元服务中使用。 |

**RichEditorTextStyle**

文本样式信息。

系统能力： SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| fontColor | ResourceColor | 否 | 是 | 文本颜色。 默认值：$r('sys.color.font_primary')。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| fontSize | Length | number | 否 | 是 | 设置字体大小，Length为number类型时，使用fp单位。字体默认大小16。不支持设置百分比字符串。字体大小设置为0时，显示默认字体大小。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| fontStyle | FontStyle | 否 | 是 | 字体样式。 默认值：FontStyle.Normal。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| fontWeight | number | FontWeight | string | 否 | 是 | 字体粗细。 number类型取值[100,900]，取值间隔为100，默认为400，取值越大，字体越粗。 string类型仅支持number类型取值的字符串形式，例如“400”，以及“bold”、“bolder”、“lighter”、“regular” 、“medium”分别对应FontWeight中相应的枚举值。 默认值：FontWeight.Normal。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| fontFamily | ResourceStr | 否 | 是 | 设置字体列表。默认字体'HarmonyOS Sans'，当前支持'HarmonyOS Sans'字体和注册自定义字体。 默认字体:'HarmonyOS Sans'。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| decoration | DecorationStyleInterface | 否 | 是 | 设置文本装饰线的样式、颜色和粗细。 type默认值：TextDecorationType.None color默认值：跟随字体颜色。 style默认值：TextDecorationStyle.SOLID thicknessScale默认值：1.0 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| textShadow11+ | ShadowOptions | Array<ShadowOptions> | 否 | 是 | 设置文字阴影效果。该接口支持以数组形式入参，实现多重文字阴影。 说明： 仅支持设置阴影模糊半径、颜色和偏移量，不支持智能取色。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| lineHeight12+ | number | string | Resource | 否 | 是 | 设置文本的文本行高，设置值不大于0时，不限制文本行高，自适应字体大小。number类型时单位为fp，不支持设置百分比字符串。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| letterSpacing12+ | number | string | 否 | 是 | 设置文本字符间距，当取值为负值时，文字会发生压缩，负值过小时会将组件内容区大小压缩为0，导致无内容显示，number类型时单位为fp，不支持设置百分比字符串。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| fontFeature12+ | string | 否 | 是 | 设置文字特性效果，比如数字等宽的特性。如果未设置，默认为变宽数字。设置无效字符保持默认。 格式为：normal | <feature-tag-value> <feature-tag-value>的格式为：<string> [ <integer> | on | off ] <feature-tag-value>的个数可以有多个，中间用','隔开。 例如，使用等宽时钟数字的输入格式为："ss01" on。 Font Feature当前支持的属性见 fontFeature属性列表。 设置 Font Feature 属性，Font Feature 是 OpenType 字体的高级排版能力，如支持连字、数字等宽等特性，一般用在自定义字体中，其能力需要字体本身支持。 更多 Font Feature 能力介绍可参考 https://www.w3.org/TR/css-fonts-3/#font-feature-settings-prop 和 https://sparanoid.com/lab/opentype-features/ 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| halfLeading18+ | boolean | 否 | 是 | 文本是否将行间距平分至行的顶部与底部。 true表示将行间距平分至行的顶部与底部，false则不平分。 默认值：false。 元服务API： 从API version 18开始，该接口支持在元服务中使用。 |
| textBackgroundStyle18+ | TextBackgroundStyle | 否 | 是 | 文本背景样式。 默认值： { color: Color.Transparent, radius: 0 } 元服务API： 从API version 18开始，该接口支持在元服务中使用。 |
| strokeWidth23+ | LengthMetrics | number | 否 | 是 | 文本描边宽度。如果LengthMetrics的unit值是PERCENT，当前设置不生效，作为0处理。 值小于0时为实体字，大于0时为轮廓字，等于0时无描边效果。 默认值：0vp。 单位：LengthMetrics类型时跟随LengthMetrics，number类型时是vp。 取值范围：(-∞, +∞) 元服务API： 从API version 23开始，该接口支持在元服务中使用。 模型约束： 此接口仅可在Stage模型下使用。 |
| strokeColor23+ | ResourceColor | 否 | 是 | 文本描边颜色。 默认值：跟随字体颜色。 设置异常值时跟随字体颜色。 元服务API： 从API version 23开始，该接口支持在元服务中使用。 |

**PlaceholderStyle12+**

设置提示文本的字体样式。

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| font | Font | 否 | 是 | 设置placeholder文本样式。 默认值遵循主题设置。 |
| fontColor | ResourceColor | 否 | 是 | 设置placeholder文本颜色。 默认值遵循主题设置。 |

**RichEditorImageSpanOptions**

设置图片的偏移位置和图片样式信息。

系统能力： SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| offset | number | 否 | 是 | 添加图片的位置。省略时，添加到所有内容的末尾。 当值小于0时，设置在所有内容最前面；当值大于所有内容长度时，设置在所有内容最后面。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| imageStyle | RichEditorImageSpanStyle | 否 | 是 | 图片样式信息。省略时，使用系统默认图片信息。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| gesture11+ | RichEditorGesture | 否 | 是 | 行为触发回调。省略时，仅使用系统默认行为。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| onHover14+ | OnHoverCallback | 否 | 是 | 鼠标悬停触发回调。省略时，不执行相关行为。 元服务API： 从API version 14开始，该接口支持在元服务中使用。 |

**RichEditorImageSpanStyle**

图片样式。

系统能力： SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| size | [Dimension, Dimension] | 否 | 是 | 图片宽度和高度。默认值：与objectFit的值相关，不同的objectFit值有不同的默认尺寸。objectFit的值为Cover时，图片高度为组件高度减去组件上下内边距，宽度为组件宽度减去组件左右内边距。不支持以Percentage形式设置。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| verticalAlign | ImageSpanAlignment | 否 | 是 | 图片垂直对齐方式。 默认值:ImageSpanAlignment.BOTTOM 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| objectFit | ImageFit | 否 | 是 | 图片缩放类型。 默认值:ImageFit.Cover。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| layoutStyle11+ | RichEditorLayoutStyle | 否 | 是 | 图片布局风格。默认值：{"borderRadius":"","margin":""}  元服务API： 从API version 12开始，该接口支持在元服务中使用。 |

**RichEditorSymbolSpanOptions11+**

设置SymbolSpan组件的偏移位置和样式。

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| offset | number | 否 | 是 | 添加组件的位置。省略时，添加到所有内容的最后。 如果值小于0，添加到所有内容的最前面；如果值大于所有内容的长度，添加到所有内容的最后面。 |
| style | RichEditorSymbolSpanStyle | 否 | 是 | 组件样式信息。省略时，使用系统默认样式信息。 |

**RichEditorSymbolSpanStyle11+**

组件SymbolSpan样式信息。

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| fontColor | Array<ResourceColor> | 否 | 是 | 设置SymbolSpan组件颜色。 默认值：不同渲染策略下默认值不同。 |
| fontSize | number | string | Resource | 否 | 是 | 设置SymbolSpan组件大小，默认单位为fp。 默认值：跟随主题。 |
| fontWeight | number | FontWeight | string | 否 | 是 | 设置SymbolSpan组件粗细。 number类型取值[100,900]，取值间隔为100，默认为400，取值越大，字体越粗。 string类型仅支持number类型取值的字符串形式，例如“400”，以及“bold”、“bolder”、“lighter”、“regular” 、“medium”分别对应FontWeight中相应的枚举值。 默认值：FontWeight.Normal。 |
| renderingStrategy | SymbolRenderingStrategy | 否 | 是 | 设置SymbolSpan组件渲染策略。 默认值：SymbolRenderingStrategy.SINGLE。 |
| effectStrategy | SymbolEffectStrategy | 否 | 是 | 设置SymbolSpan组件动效策略。 默认值：SymbolEffectStrategy.NONE。 |

**RichEditorBuilderSpanOptions11+**

设置builder的偏移位置和样式。

系统能力： SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| offset | number | 否 | 是 | 添加builder的位置。省略或者为异常值时，添加到所有内容的最后。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| accessibilitySpanOptions23+ | AccessibilitySpanOptions | 否 | 是 | 无障碍朗读功能属性。缺省时，取AccessibilitySpanOptions的默认值。 元服务API： 从API version 23开始，该接口支持在元服务中使用。 模型约束： 此接口仅可在Stage模型下使用。 |

**RichEditorSpan12+**

type RichEditorSpan = RichEditorImageSpanResult | RichEditorTextSpanResult

RichEditor span信息。

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| RichEditorImageSpanResult | 后端返回的图片信息。 |
| RichEditorTextSpanResult | 后端返回的文本信息。 |

**SelectionMenuOptions**

菜单的选项。

系统能力： SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| onAppear | MenuOnAppearCallback | 否 | 是 | 自定义选择菜单弹出时回调。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| onDisappear | Callback<void> | 否 | 是 | 自定义选择菜单关闭时回调。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| menuType13+ | MenuType | 否 | 是 | 自定义选择菜单类型。 元服务API： 从API version 13开始，该接口支持在元服务中使用。 默认值：MenuType.SELECTION_MENU。 |
| onMenuShow15+ | MenuCallback | 否 | 是 | 自定义选择菜单显示时回调。 元服务API： 从API version 15开始，该接口支持在元服务中使用。 |
| onMenuHide15+ | MenuCallback | 否 | 是 | 自定义选择菜单隐藏时回调。 元服务API： 从API version 15开始，该接口支持在元服务中使用。 |
| previewMenuOptions18+ | PreviewMenuOptions | 否 | 是 | 预览菜单的选项。该参数只在RichEditor中生效。 元服务API： 从API version 18开始，该接口支持在元服务中使用。 |

**PreviewMenuOptions18+**

预览菜单的选项。

元服务API： 从API version 18开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| hapticFeedbackMode | HapticFeedbackMode | 否 | 是 | 菜单弹出时振动效果，当ImageSpan或BuilderSpan绑定预览菜单时生效。 默认值：HapticFeedbackMode.DISABLED，菜单弹出时不振动。 说明： 仅当应用具备ohos.permission.VIBRATE权限，且用户启用了触感反馈时才会生效。 |

**PasteEvent11+**

定义用户粘贴事件。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| preventDefault | Callback<void> | 否 | 是 | 阻止系统默认粘贴事件。 |

**CutEvent12+**

定义用户剪切事件。

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| preventDefault | Callback<void> | 否 | 是 | 阻止系统默认剪切事件。 |

**CopyEvent12+**

定义用户复制事件。

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| preventDefault | Callback<void> | 否 | 是 | 阻止组件的默认复制操作。 |

**RichEditorGesture11+**

用户手势事件。

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| onClick | Callback<ClickEvent> | 否 | 是 | ClickEvent为用户点击事件。 点击完成时回调事件。 双击时，第一次点击触发回调事件。 |
| onLongPress | Callback<GestureEvent> | 否 | 是 | GestureEvent为用户长按事件。 长按完成时回调事件。 |

**KeyboardOptions12+**

设置自定义键盘是否支持避让功能。

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| supportAvoidance | boolean | 否 | 是 | 设置自定义键盘是否支持避让功能。默认值为 false，表示不支持避让；true 表示支持避让。 |

**SubmitCallback12+**

type SubmitCallback = (enterKey: EnterKeyType, event: SubmitEvent) => void

软键盘按下回车键时的回调事件。

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enterKey | EnterKeyType | 是 | 软键盘输入法回车键类型。具体类型见EnterKeyType枚举说明。 |
| event | SubmitEvent | 是 | 当提交的时候，提供保持组件编辑状态的方法。EnterKeyType指定为NEW_LINE时，默认保持编辑态。 |

**MenuOnAppearCallback12+**

type MenuOnAppearCallback = (start: number, end: number) => void

自定义选择菜单弹出时触发的回调事件。

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| start | number | 是 | 选中内容的起始位置。 |
| end | number | 是 | 选中内容的终止位置。 |

**MenuCallback15+**

type MenuCallback = (start: number, end: number) => void

自定义选择菜单显示或隐藏时触发的回调事件。

元服务API： 从API version 15开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| start | number | 是 | 选中内容的起始位置。 |
| end | number | 是 | 选中内容的终止位置。 |

**PasteEventCallback12+**

type PasteEventCallback = (event?: PasteEvent) => void

粘贴完成前，触发回调。

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | PasteEvent | 否 | 定义用户粘贴事件。 |

**OnHoverCallback14+**

type OnHoverCallback = (status: boolean, event: HoverEvent) => void

鼠标悬浮触发回调。

元服务API： 从API version 14开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| status | boolean | 是 | 表示鼠标是否悬浮在组件上，鼠标进入组件时为true，离开组件时为false。 |
| event | HoverEvent | 是 | 设置悬浮事件。 |

**RichEditorTextSpan**

文本Span信息。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| spanPosition | RichEditorSpanPosition | 否 | 否 | Span位置。 |
| value | string | 否 | 否 | 文本Span内容。 |
| textStyle | RichEditorTextStyle | 否 | 是 | 文本Span样式信息。 |

**RichEditorImageSpan**

图片Span信息。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| spanPosition | RichEditorSpanPosition | 否 | 否 | Span位置。 |
| value | PixelMap | ResourceStr | 否 | 否 | 图片内容。 |
| imageStyle | RichEditorImageSpanStyle | 否 | 是 | 图片样式。 |

**RichEditorUrlStyle19+**

Url信息。

元服务API： 从API version 19开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| url | ResourceStr | 否 | 是 | url地址。 默认值：undefined |

**示例**

**示例1（更新文本样式）**

通过[updateSpanStyle](#ZH-CN_TOPIC_0000002522080846__updatespanstyle)接口更新已有文本样式，更改样式后，使用[getSpans](#ZH-CN_TOPIC_0000002522080846__getspans)获取文本新的样式信息。

```ets
// xxx.ets
@Entry
@Component
struct Index {
  controller: RichEditorController = new RichEditorController();
  options: RichEditorOptions = { controller: this.controller };
  private start: number = -1;
  private end: number = -1;
  @State message: string = "[-1, -1]";
  @State content: string = "";

  build() {
    Column() {
        Text("selection range:").width("100%")
        Text() {
          Span(this.message)
        }.width("100%")
        Text("selection content:").width("100%")
        Text() {
          Span(this.content)
        }.width("100%")
      }
      .borderWidth(1)
      .borderColor(Color.Red)
      .width("100%")
      .height("20%")

      Row() {
        Button("更新样式:加粗").onClick(() => {
          this.controller.updateSpanStyle({
            start: this.start,
            end: this.end,
            textStyle:
            {
              fontWeight: FontWeight.Bolder
            }
          })
        Button("获取选择内容").onClick(() => {
          this.content = "";
          this.controller.getSpans({
            start: this.start,
            end: this.end
          }).forEach(item => {
            if(typeof(item as RichEditorImageSpanResult)['imageStyle'] != 'undefined'){
              this.content += (item as RichEditorImageSpanResult).valueResourceStr;
              this.content += "\n";
            } else {
              if(typeof(item as RichEditorTextSpanResult)['symbolSpanStyle'] != 'undefined') {
                this.content += (item as RichEditorTextSpanResult).symbolSpanStyle?.fontSize;
                this.content += "\n";
              }else {
                this.content += (item as RichEditorTextSpanResult).value;
                this.content += "\n";
              }
          })
        Button("删除选择内容").onClick(() => {
          this.controller.deleteSpans({
            start: this.start,
            end: this.end
          })
          this.start = -1;
          this.end = -1;
          this.message = "[" + this.start + ", " + this.end + "]";
        })
      }
      .borderWidth(1)
      .borderColor(Color.Red)
      .width("100%")
      .height("10%")

      Column() {
        RichEditor(this.options)
          .onReady(() => {
            this.controller.addTextSpan("012345",
              {
                style:
                {
                  fontColor: Color.Orange,
                  fontSize: 30
                }
              })
            this.controller.addSymbolSpan($r("sys.symbol.ohos_trash"),
              {
                style:
                {
                  fontSize: 30
                }
              })
            // $r('app.media.startIcon')需要替换为开发者所需的图像资源文件。
            this.controller.addImageSpan($r('app.media.startIcon'),
              {
                imageStyle:
                {
                  size: ["57px", "57px"]
                }
              })
            this.controller.addTextSpan("56789",
              {
                style:
                {
                  fontColor: Color.Black,
                  fontSize: 30
                }
              })
          .onSelect((value: RichEditorSelection) => {
            this.start = value.selection[0];
            this.end = value.selection[1];
            this.message = "[" + this.start + ", " + this.end + "]";
          })
          .aboutToIMEInput((value: RichEditorInsertValue) => {
            console.info("---------------------- aboutToIMEInput ----------------------");
            console.info("insertOffset:" + value.insertOffset);
            console.info("insertValue:" + value.insertValue);
            return true;
          })
          .onIMEInputComplete((value: RichEditorTextSpanResult) => {
            console.info("---------------------- onIMEInputComplete ---------------------");
            console.info("spanIndex:" + value.spanPosition.spanIndex);
            console.info("spanRange:[" + value.spanPosition.spanRange[0] + "," + value.spanPosition.spanRange[1] + "]");
            console.info("offsetInSpan:[" + value.offsetInSpan[0] + "," + value.offsetInSpan[1] + "]");
            console.info("value:" + value.value);
          })
          .aboutToDelete((value: RichEditorDeleteValue) => {
            console.info("---------------------- aboutToDelete --------------------------");
            console.info("offset:" + value.offset);
            console.info("direction:" + value.direction);
            console.info("length:" + value.length);
            value.richEditorDeleteSpans.forEach(item => {
              console.info("---------------------- item --------------------------");
              console.info("spanIndex:" + item.spanPosition.spanIndex);
              console.info("spanRange:[" + item.spanPosition.spanRange[0] + "," + item.spanPosition.spanRange[1] + "]");
              console.info("offsetInSpan:[" + item.offsetInSpan[0] + "," + item.offsetInSpan[1] + "]");
              if (typeof(item as RichEditorImageSpanResult)['imageStyle'] != 'undefined') {
                console.info("image:" + (item as RichEditorImageSpanResult).valueResourceStr);
              } else {
                console.info("text:" + (item as RichEditorTextSpanResult).value);
              }
            })
            return true;
          })
          .onDeleteComplete(() => {
            console.info("---------------------- onDeleteComplete ------------------------");
          })
          .placeholder("input...", {
            fontColor: Color.Gray,
            font: {
              size: 16,
              weight: FontWeight.Normal,
              family: "HarmonyOS Sans",
              style: FontStyle.Normal
            }
          })
          .borderWidth(1)
          .borderColor(Color.Green)
          .width("100%")
          .height("30%")
      }
      .borderWidth(1)
      .borderColor(Color.Red)
      .width("100%")
      .height("70%")
    }
```

![image](public_sys-resources/zh-cn_image_0000002522245040.webp)

**示例2（绑定自定义键盘）**

通过[customKeyboard](#ZH-CN_TOPIC_0000002522080846__customkeyboard)给组件绑定自定义键盘。

```ets
// xxx.ets
@Entry
@Component
struct RichEditorExample {
  controller: RichEditorController = new RichEditorController();

  // 自定义键盘组件
  @Builder
  CustomKeyboardBuilder() {
    Column() {
      Grid() {
        ForEach(['1', '2', '3', '4', '5', '6', '7', '8', '9', '*', '0', '#'], (item: string) => {
          GridItem() {
            Button(item).width(110).onClick(() => {
              this.controller.addTextSpan(item + '', {
                offset: this.controller.getCaretOffset(),
                style:
                {
                  fontColor: Color.Orange,
                  fontSize: 30
                }
              })
          }
        })
      }.maxCount(3).columnsGap(10).rowsGap(10).padding(5)
    }.backgroundColor(Color.Gray)
  }

  build() {
    Column() {
      RichEditor({ controller: this.controller })// 绑定自定义键盘
        .customKeyboard(this.CustomKeyboardBuilder())
        .border({ width: 1 })
        .borderWidth(1)
        .borderColor(Color.Red)
        .margin(10)
        .height(200)
        .width("100%")
    }
```

![image](public_sys-resources/zh-cn_image_0000002553205001.webp)

**示例3（绑定自定义菜单）**

通过[bindSelectionMenu](#ZH-CN_TOPIC_0000002522080846__bindselectionmenu)给组件绑定自定义菜单。

示例中的粘贴菜单项涉及读取剪贴板数据，因此需按规范[申请访问剪贴板权限](../../guides/申请访问剪贴板权限.md)。

```ets
// xxx.ets
import { BusinessError, pasteboard } from '@kit.BasicServicesKit';

export interface SelectionMenuTheme {
  imageSize: number;
  buttonSize: number;
  menuSpacing: number;
  editorOptionMargin: number;
  expandedOptionPadding: number;
  defaultMenuWidth: number;
  imageFillColor: Resource;
  backGroundColor: Resource;
  iconBorderRadius: Resource;
  containerBorderRadius: Resource;
  cutIcon: Resource;
  copyIcon: Resource;
  pasteIcon: Resource;
  selectAllIcon: Resource;
  shareIcon: Resource;
  translateIcon: Resource;
  searchIcon: Resource;
  arrowDownIcon: Resource;
  iconPanelShadowStyle: ShadowStyle;
  iconFocusBorderColor: Resource;
}

export const defaultTheme: SelectionMenuTheme = {
  imageSize: 24,
  buttonSize: 48,
  menuSpacing: 8,
  editorOptionMargin: 1,
  expandedOptionPadding: 3,
  defaultMenuWidth: 256,
  imageFillColor: $r('sys.color.ohos_id_color_primary'),
  backGroundColor: $r('sys.color.ohos_id_color_dialog_bg'),
  iconBorderRadius: $r('sys.float.ohos_id_corner_radius_default_m'),
  containerBorderRadius: $r('sys.float.ohos_id_corner_radius_card'),
  cutIcon: $r("sys.media.ohos_ic_public_cut"),
  copyIcon: $r("sys.media.ohos_ic_public_copy"),
  pasteIcon: $r("sys.media.ohos_ic_public_paste"),
  selectAllIcon: $r("sys.media.ohos_ic_public_select_all"),
  shareIcon: $r("sys.media.ohos_ic_public_share"),
  translateIcon: $r("sys.media.ohos_ic_public_translate_c2e"),
  searchIcon: $r("sys.media.ohos_ic_public_search_filled"),
  arrowDownIcon: $r("sys.media.ohos_ic_public_arrow_down"),
  iconPanelShadowStyle: ShadowStyle.OUTER_DEFAULT_MD,
  iconFocusBorderColor: $r('sys.color.ohos_id_color_focused_outline')
}

@Entry
@Component
struct SelectionMenu {
  @State message: string = 'Hello World';
  @State textSize: number = 40;
  @State sliderShow: boolean = false;
  @State start: number = -1;
  @State end: number = -1;
  @State colorTransparent: Color = Color.Transparent;
  controller: RichEditorController = new RichEditorController();
  options: RichEditorOptions = { controller: this.controller };
  // $r('app.media.startIcon')需要替换为开发者所需的图像资源文件。
  private iconArr: Array<Resource> =
    [$r('app.media.startIcon'), $r('app.media.startIcon'), $r('app.media.startIcon'),
    $r('app.media.startIcon'), $r('app.media.startIcon')];
  @State iconBgColor: ResourceColor[] = new Array(this.iconArr.length).fill(this.colorTransparent);
  @State pasteEnable: boolean = false;
  @State visibilityValue: Visibility = Visibility.Visible;
  @State textStyle: RichEditorTextStyle = {};
  private fontWeightTable: string[] = ["100", "200", "300", "400", "500", "600", "700", "800", "900", "bold", "normal", "bolder", "lighter", "medium", "regular"];
  private theme: SelectionMenuTheme = defaultTheme;

  aboutToAppear() {
    if (this.controller) {
      let richEditorSelection = this.controller.getSelection();
      if (richEditorSelection) {
        let start = richEditorSelection.selection[0];
        let end = richEditorSelection.selection[1];
        if (start === 0 && this.controller.getSpans({ start: end + 1, end: end + 1 }).length === 0) {
          this.visibilityValue = Visibility.None;
        } else {
          this.visibilityValue = Visibility.Visible;
        }
    let sysBoard = pasteboard.getSystemPasteboard()
    try {
      if (sysBoard && sysBoard.hasDataSync()) {
        this.pasteEnable = true
      } else {
        this.pasteEnable = false
      }
    } catch (err) {
      console.error('Failed to check the PasteData. Cause:' + err.message)
    }

  build() {
    Column() {
        RichEditor(this.options)
          .onReady(() => {
            this.controller.addTextSpan(this.message, { style: { fontColor: Color.Orange, fontSize: 30 } })
          })
          .onSelect((value: RichEditorSelection) => {
            if (value.selection[0] == -1 && value.selection[1] == -1) {
              return;
            }
            this.start = value.selection[0];
            this.end = value.selection[1];
          })
          .bindSelectionMenu(RichEditorSpanType.TEXT, this.panel, ResponseType.LongPress, { onDisappear: () => {
            this.sliderShow = false;
          }})
          .bindSelectionMenu(RichEditorSpanType.TEXT, this.panel, ResponseType.RightClick, { onDisappear: () => {
            this.sliderShow = false;
          }})
          .bindSelectionMenu(RichEditorSpanType.IMAGE, this.panel, ResponseType.LongPress, {
            menuType : MenuType.PREVIEW_MENU,
            previewMenuOptions : {
              hapticFeedbackMode : HapticFeedbackMode.ENABLED
            }
          })
          .borderWidth(1)
          .borderColor(Color.Red)
          .width(200)
          .height(200)
      }.width('100%').backgroundColor(Color.White)
    }.height('100%')
  }

  PushDataToPasteboard(richEditorSelection: RichEditorSelection) {
    let sysBoard = pasteboard.getSystemPasteboard();
    let pasteData = pasteboard.createData(pasteboard.MIMETYPE_TEXT_PLAIN, '');
    if (richEditorSelection.spans && richEditorSelection.spans.length > 0) {
      let count = richEditorSelection.spans.length;
      for (let i = count - 1; i >= 0; i--) {
        let item = richEditorSelection.spans[i]
        if ((item as RichEditorTextSpanResult)?.textStyle) {
          let span = item as RichEditorTextSpanResult;
          let style = span.textStyle;
          let data = pasteboard.createRecord(pasteboard.MIMETYPE_TEXT_PLAIN, span.value.substring(span.offsetInSpan[0], span.offsetInSpan[1]));
          let prop = pasteData.getProperty();
          let temp: Record<string, Object> = {
            'color': style.fontColor,
            'size': style.fontSize,
            'style': style.fontStyle,
            'weight': this.fontWeightTable[style.fontWeight],
            'fontFamily': style.fontFamily,
            'decorationType': style.decoration.type,
            'decorationColor': style.decoration.color
          };
          prop.additions[i] = temp;
          pasteData.addRecord(data)
          pasteData.setProperty(prop)
        }
    sysBoard.clearData()
    sysBoard.setData(pasteData).then(() => {
      console.info('SelectionMenu copy option, Succeeded in setting PasteData.');
      this.pasteEnable = true;
    }).catch((err: BusinessError) => {
      console.error('SelectionMenu copy option, Failed to set PasteData. Cause:' + err.message);
    })
  }

  PopDataFromPasteboard(richEditorSelection: RichEditorSelection) {
    let start = richEditorSelection.selection[0];
    let end = richEditorSelection.selection[1];
    if (start == end && this.controller) {
      start = this.controller.getCaretOffset();
      end = this.controller.getCaretOffset();
    }
    let moveOffset = 0;
    let sysBoard = pasteboard.getSystemPasteboard();
    sysBoard.getData((err, data) => {
      if (err) {
        return;
      }
      let count = data.getRecordCount();
      for (let i = 0; i < count; i++) {
        const element = data.getRecord(i);
        let tex: RichEditorTextStyle = {
          fontSize: 16,
          fontColor: Color.Black,
          fontWeight: FontWeight.Normal,
          fontFamily: "HarmonyOS Sans",
          fontStyle: FontStyle.Normal,
          decoration: { type: TextDecorationType.None, color: "#FF000000", style: TextDecorationStyle.SOLID }
        }
        if (data.getProperty() && data.getProperty().additions[i]) {
          const tmp = data.getProperty().additions[i] as Record<string, Object | undefined>;
          if (tmp.color) {
            tex.fontColor = tmp.color as ResourceColor;
          }
          if (tmp.size) {
            tex.fontSize = tmp.size as Length | number;
          }
          if (tmp.style) {
            tex.fontStyle = tmp.style as FontStyle;
          }
          if (tmp.weight) {
            tex.fontWeight = tmp.weight as number | FontWeight | string;
          }
          if (tmp.fontFamily) {
            tex.fontFamily = tmp.fontFamily as ResourceStr;
          }
          if (tmp.decorationType && tex.decoration) {
            tex.decoration.type = tmp.decorationType as TextDecorationType;
          }
          if (tmp.decorationColor && tex.decoration) {
            tex.decoration.color = tmp.decorationColor as ResourceColor;
          }
          if (tex.decoration) {
            tex.decoration = { type: tex.decoration.type, color: tex.decoration.color };
          }
        if (element && element.plainText && element.mimeType === pasteboard.MIMETYPE_TEXT_PLAIN && this.controller) {
          this.controller.addTextSpan(element.plainText,
            {
              style: tex,
              offset: start + moveOffset
            }
          )
          moveOffset += element.plainText.length;
        }
      if (this.controller) {
        this.controller.setCaretOffset(start + moveOffset)
        this.controller.closeSelectionMenu()
      }
      if (start != end && this.controller) {
        this.controller.deleteSpans({ start: start + moveOffset, end: end + moveOffset })
      }
    })
  }

  @Builder
  panel() {
    Column() {
      this.iconPanel()
      if (!this.sliderShow) {
        this.SystemMenu()
      } else {
        this.sliderPanel()
      }
    }.width(256)
  }

  @Builder iconPanel() {
    Column() {
      Row({ space: 2 }) {
        ForEach(this.iconArr, (item:Resource, index ?: number) => {
          Flex({ justifyContent: FlexAlign.Center, alignItems: ItemAlign.Center }) {
            Image(item).fillColor(this.theme.imageFillColor).width(24).height(24).focusable(true).draggable(false)
          }
          .borderRadius(this.theme.iconBorderRadius)
          .width(this.theme.buttonSize)
          .height(this.theme.buttonSize)
          .onClick(() => {
            if (index as number == 0) {
              this.sliderShow = false;
              if (this.controller) {
                let selection = this.controller.getSelection();
                let spans = selection.spans;
                spans.forEach((item: RichEditorTextSpanResult | RichEditorImageSpanResult, index) => {
                  if (typeof (item as RichEditorTextSpanResult)['textStyle'] != 'undefined') {
                    let span = item as RichEditorTextSpanResult;
                    this.textStyle = span.textStyle;
                    let start = span.offsetInSpan[0];
                    let end = span.offsetInSpan[1];
                    let offset = span.spanPosition.spanRange[0];
                    if (this.textStyle.fontWeight != 11) {
                      this.textStyle.fontWeight = FontWeight.Bolder;
                    } else {
                      this.textStyle.fontWeight = FontWeight.Normal;
                    }
                    this.controller.updateSpanStyle({
                      start: offset + start,
                      end: offset + end,
                      textStyle: this.textStyle
                    })
                  }
                })
              }
            } else if (index as number == 1) {
              this.sliderShow = false;
              if (this.controller) {
                let selection = this.controller.getSelection();
                let spans = selection.spans;
                spans.forEach((item: RichEditorTextSpanResult | RichEditorImageSpanResult, index) => {
                  if (typeof (item as RichEditorTextSpanResult)['textStyle'] != 'undefined') {
                    let span = item as RichEditorTextSpanResult;
                    this.textStyle = span.textStyle;
                    let start = span.offsetInSpan[0];
                    let end = span.offsetInSpan[1];
                    let offset = span.spanPosition.spanRange[0];
                    if (this.textStyle.fontStyle == FontStyle.Italic) {
                      this.textStyle.fontStyle = FontStyle.Normal;
                    } else {
                      this.textStyle.fontStyle = FontStyle.Italic;
                    }
                    this.controller.updateSpanStyle({
                      start: offset + start,
                      end: offset + end,
                      textStyle: this.textStyle
                    })
                  }
                })
              }
            } else if (index as number == 2) {
              this.sliderShow = false;
              if (this.controller) {
                let selection = this.controller.getSelection();
                let spans = selection.spans;
                spans.forEach((item: RichEditorTextSpanResult | RichEditorImageSpanResult, index) => {
                  if (typeof (item as RichEditorTextSpanResult)['textStyle'] != 'undefined') {
                    let span = item as RichEditorTextSpanResult;
                    this.textStyle = span.textStyle;
                    let start = span.offsetInSpan[0];
                    let end = span.offsetInSpan[1];
                    let offset = span.spanPosition.spanRange[0];
                    if (this.textStyle.decoration) {
                      if (this.textStyle.decoration.type == TextDecorationType.Underline) {
                        this.textStyle.decoration.type = TextDecorationType.None;
                      } else {
                        this.textStyle.decoration.type = TextDecorationType.Underline;
                      }
                    } else {
                      this.textStyle.decoration = { type: TextDecorationType.Underline, color: Color.Black, style: TextDecorationStyle.SOLID };
                    }
                    this.controller.updateSpanStyle({
                      start: offset + start,
                      end: offset + end,
                      textStyle: this.textStyle
                    })
                  }
                })
              }
            } else if (index as number == 3) {
              this.sliderShow = !this.sliderShow;
            } else if (index as number == 4) {
              this.sliderShow = false;
              if (this.controller) {
                let selection = this.controller.getSelection();
                let spans = selection.spans;
                spans.forEach((item: RichEditorTextSpanResult | RichEditorImageSpanResult, index) => {
                  if (typeof (item as RichEditorTextSpanResult)['textStyle'] != 'undefined') {
                    let span = item as RichEditorTextSpanResult;
                    this.textStyle = span.textStyle;
                    let start = span.offsetInSpan[0];
                    let end = span.offsetInSpan[1];
                    let offset = span.spanPosition.spanRange[0];
                    if (this.textStyle.fontColor == Color.Orange || this.textStyle.fontColor == '#FFFFA500') {
                      this.textStyle.fontColor = Color.Black;
                    } else {
                      this.textStyle.fontColor = Color.Orange;
                    }
                    this.controller.updateSpanStyle({
                      start: offset + start,
                      end: offset + end,
                      textStyle: this.textStyle
                    })
                  }
                })
              }
          })
          .onTouch((event?: TouchEvent | undefined) => {
            if(event != undefined){
              if (event.type === TouchType.Down) {
                this.iconBgColor[index as number] = $r('sys.color.ohos_id_color_click_effect');
              }
              if (event.type === TouchType.Up) {
                this.iconBgColor[index as number] = this.colorTransparent;
              }
          })
          .onHover((isHover?: boolean, event?: HoverEvent) => {
            this.iconBgColor.forEach((icon:ResourceColor, index1) => {
              this.iconBgColor[index1] = this.colorTransparent;
            })
            if(isHover != undefined) {
              this.iconBgColor[index as number] = $r('sys.color.ohos_id_color_hover');
            }
          })
          .backgroundColor(this.iconBgColor[index as number])
        })
      }
    .clip(true)
    .width(this.theme.defaultMenuWidth)
    .padding(this.theme.expandedOptionPadding)
    .borderRadius(this.theme.containerBorderRadius)
    .margin({ bottom: this.theme.menuSpacing })
    .backgroundColor(this.theme.backGroundColor)
    .shadow(this.theme.iconPanelShadowStyle)
  }

  @Builder
  SystemMenu() {
    Column() {
      Menu() {
        if (this.controller) {
          MenuItemGroup() {
            MenuItem({ startIcon: this.theme.cutIcon, content: "剪切", labelInfo: "Ctrl+X" })
              .onClick(() => {
                if (!this.controller) {
                  return
                }
                let richEditorSelection = this.controller.getSelection();
                this.PushDataToPasteboard(richEditorSelection);
                this.controller.deleteSpans({
                  start: richEditorSelection.selection[0],
                  end: richEditorSelection.selection[1]
                })
            MenuItem({ startIcon: this.theme.copyIcon, content: "复制", labelInfo: "Ctrl+C" })
              .onClick(() => {
                if (!this.controller) {
                  return;
                }
                let richEditorSelection = this.controller.getSelection();
                this.PushDataToPasteboard(richEditorSelection)
                this.controller.closeSelectionMenu()
              })
            MenuItem({ startIcon: this.theme.pasteIcon, content: "粘贴", labelInfo: "Ctrl+V" })
              .enabled(this.pasteEnable)
              .onClick(() => {
                if (!this.controller) {
                  return;
                }
                let richEditorSelection = this.controller.getSelection();
                this.PopDataFromPasteboard(richEditorSelection)
              })
            MenuItem({ startIcon: this.theme.selectAllIcon, content: "全选", labelInfo: "Ctrl+A" })
              .visibility(this.visibilityValue)
              .onClick(() => {
                if (!this.controller) {
                  return;
                }
                this.controller.setSelection(-1, -1)
                this.visibilityValue = Visibility.None;
              })
            MenuItem({ startIcon: this.theme.shareIcon, content: "分享", labelInfo: "" })
              .enabled(false)
            MenuItem({ startIcon: this.theme.translateIcon, content: "翻译", labelInfo: "" })
              .enabled(false)
            MenuItem({ startIcon: this.theme.searchIcon, content: "搜索", labelInfo: "" })
              .enabled(false)
          }
      .onVisibleAreaChange([0.0, 1.0], () => {
        if (!this.controller) {
          return;
        }
        let richEditorSelection = this.controller.getSelection();
        let start = richEditorSelection.selection[0];
        let end = richEditorSelection.selection[1];
        if (start === 0 && this.controller.getSpans({ start: end + 1, end: end + 1 }).length === 0) {
          this.visibilityValue = Visibility.None;
        } else {
          this.visibilityValue = Visibility.Visible;
        }
      })
      .radius(this.theme.containerBorderRadius)
      .clip(true)
      .backgroundColor(Color.White)
      .width(this.theme.defaultMenuWidth)
    }
    .width(this.theme.defaultMenuWidth)
  }

  @Builder sliderPanel() {
    Column() {
      Flex({ justifyContent: FlexAlign.SpaceBetween, alignItems: ItemAlign.Center }) {
        Text('A').fontSize(15)
        Slider({ value: this.textSize, step: 10, style: SliderStyle.InSet })
          .width(210)
          .onChange((value: number, mode: SliderChangeMode) => {
            if (this.controller) {
              let selection = this.controller.getSelection();
              if (mode == SliderChangeMode.End) {
                if (this.textSize == undefined) {
                  this.textSize = 0;
                }
                let spans = selection.spans;
                spans.forEach((item: RichEditorTextSpanResult | RichEditorImageSpanResult, index) => {
                  if (typeof (item as RichEditorTextSpanResult)['textStyle'] != 'undefined') {
                    this.textSize = Math.max(this.textSize, (item as RichEditorTextSpanResult).textStyle.fontSize);
                  }
                })
              }
              if (mode == SliderChangeMode.Moving || mode == SliderChangeMode.Click) {
                this.start = selection.selection[0];
                this.end = selection.selection[1];
                this.textSize = value;
                this.controller.updateSpanStyle({
                  start: this.start,
                  end: this.end,
                  textStyle: { fontSize: this.textSize }
                })
              }
          })
        Text('A').fontSize(20).fontWeight(FontWeight.Medium)
      }.borderRadius(this.theme.containerBorderRadius)
    }
    .shadow(ShadowStyle.OUTER_DEFAULT_MD)
    .backgroundColor(Color.White)
    .borderRadius(this.theme.containerBorderRadius)
    .padding(15)
    .height(48)
  }
```

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

系统暂未预置加粗、斜体等图标，示例代码使用系统默认图标，开发者使用时需自行替换iconArr中的资源。

![image](public_sys-resources/zh-cn_image_0000002522085048.webp)

**示例4（更新图片样式）**

通过[updateSpanStyle](#ZH-CN_TOPIC_0000002522080846__updatespanstyle)接口更新图片样式。

```ets
// xxx.ets
@Entry
@Component
struct Index {
  controller: RichEditorController = new RichEditorController();
  options: RichEditorOptions = { controller: this.controller };
  private start: number = -1;
  private end: number = -1;
  @State message: string = "[-1, -1]";
  @State content: string = "";
  @State paddingVal: number = 5;
  @State borderRad: number = 4;

  build() {
    Column() {
        Text("selection range:").width("100%")
        Text() {
          Span(this.message)
        }.width("100%")
        Text("selection content:").width("100%")
        Text() {
          Span(this.content)
        }.width("100%")
      }
      .borderWidth(1)
      .borderColor(Color.Red)
      .width("100%")
      .height("20%")

      Row() {
        Button("updateSpanStyle1")
          .fontSize(12)
          .onClick(() => {
            this.controller.updateSpanStyle({
              start: this.start,
              textStyle:
              {
                fontWeight: FontWeight.Bolder,
                fontSize:15
              },
              imageStyle: {
                size: ["80px", "80px"],
                layoutStyle: {
                  borderRadius: undefined,
                  margin: undefined
                }
            })

        Button("updateSpanStyle2")
          .fontSize(12)
          .onClick(() => {
            this.controller.updateSpanStyle({
              start: this.start,
              textStyle:
              {
                fontWeight: FontWeight.Bolder,
                fontSize:15
              },
              imageStyle: {
                size: ["70px", "70px"],
                layoutStyle: {
                  borderRadius: { topLeft: '100px', topRight: '20px', bottomLeft: '100px', bottomRight: '20px' },
                  margin: { left: '30px', top: '20px', right: '20px', bottom: '20px' }
                }
            })

        Button("updateSpanStyle3")
          .fontSize(12)
          .onClick(() => {
            this.controller.updateSpanStyle({
              start: this.start,
              textStyle:
              {
                fontWeight: FontWeight.Bolder,
                fontSize:15
              },
              imageStyle: {
                size: ["60px", "60px"],
                layoutStyle: {
                  borderRadius: '-10px',
                  margin: '-10px'
                }
            })
      }
      .borderWidth(1)
      .borderColor(Color.Red)
      .width("100%")
      .height("10%")

      Row() {
        Button('addImageSpan1')
          .fontSize(12)
          .onClick(() => {
            // $r('app.media.startIcon')需要替换为开发者所需的图像资源文件。
            this.controller.addImageSpan($r('app.media.startIcon'), {
              imageStyle: {
                size: ["80px", "80px"],
                layoutStyle: {
                  borderRadius: '50px',
                  margin: '40px'
                }
            })

        Button('addImageSpan2')
          .fontSize(12)
          .onClick(() => {
            // $r('app.media.startIcon')需要替换为开发者所需的图像资源文件。
            this.controller.addImageSpan($r('app.media.startIcon'), {
              imageStyle: {
                size: ["100px", "100px"],
                verticalAlign: ImageSpanAlignment.BOTTOM,
                layoutStyle: {
                  borderRadius: undefined,
                  margin: undefined
                }
            })

        Button('addImageSpan3')
          .fontSize(12)
          .onClick(() => {
            // $r('app.media.startIcon')需要替换为开发者所需的图像资源文件。
            this.controller.addImageSpan($r('app.media.startIcon'), {
              imageStyle: {
                size: ["60px", "60px"],
                verticalAlign: ImageSpanAlignment.BOTTOM,
                layoutStyle: {
                  borderRadius: { topLeft: '10px', topRight: '20px', bottomLeft: '30px', bottomRight: '40px' },
                  margin: { left: '10px', top: '20px', right: '30px', bottom: '40px' }
                }
            })
      }
      .borderWidth(1)
      .borderColor(Color.Red)
      .width("100%")
      .height("10%")

      Column() {
        RichEditor(this.options)
          .onReady(() => {
            this.controller.addTextSpan("0123456789",
              {
                style:
                {
                  fontColor: Color.Orange,
                  fontSize: 30
                }
              })

            // $r('app.media.startIcon')需要替换为开发者所需的图像资源文件。
            this.controller.addImageSpan($r('app.media.startIcon'),
              {
                imageStyle:
                {
                  size: ["60px", "60px"],
                  verticalAlign: ImageSpanAlignment.BOTTOM,
                  layoutStyle: {
                    borderRadius: { topLeft: '10px', topRight: '20px', bottomLeft: '30px', bottomRight: '40px' },
                    margin: { left: '10px', top: '20px', right: '30px', bottom: '40px' }
                  }
              })

            this.controller.addTextSpan("0123456789",
              {
                style:
                {
                  fontColor: Color.Black,
                  fontSize: 30
                }
              })
          .onSelect((value: RichEditorSelection) => {
            this.start = value.selection[0];
            this.end = value.selection[1];
            this.message = "[" + this.start + ", " + this.end + "]";
          })
          .aboutToIMEInput((value: RichEditorInsertValue) => {
            console.info("---------------------- aboutToIMEInput ----------------------");
            console.info("insertOffset:" + value.insertOffset);
            console.info("insertValue:" + value.insertValue);
            return true;
          })
          .onIMEInputComplete((value: RichEditorTextSpanResult) => {
            console.info("---------------------- onIMEInputComplete ---------------------");
            console.info("spanIndex:" + value.spanPosition.spanIndex);
            console.info("spanRange:[" + value.spanPosition.spanRange[0] + "," + value.spanPosition.spanRange[1] + "]");
            console.info("offsetInSpan:[" + value.offsetInSpan[0] + "," + value.offsetInSpan[1] + "]");
            console.info("value:" + value.value);
          })
          .aboutToDelete((value: RichEditorDeleteValue) => {
            console.info("---------------------- aboutToDelete --------------------------");
            console.info("offset:" + value.offset);
            console.info("direction:" + value.direction);
            console.info("length:" + value.length);
            value.richEditorDeleteSpans.forEach(item => {
              console.info("---------------------- item --------------------------");
              console.info("spanIndex:" + item.spanPosition.spanIndex);
              console.info("spanRange:[" + item.spanPosition.spanRange[0] + "," + item.spanPosition.spanRange[1] + "]");
              console.info("offsetInSpan:[" + item.offsetInSpan[0] + "," + item.offsetInSpan[1] + "]");
              if (typeof (item as RichEditorImageSpanResult)['imageStyle'] != 'undefined') {
                console.info("image:" + (item as RichEditorImageSpanResult).valueResourceStr);
              } else {
                console.info("text:" + (item as RichEditorTextSpanResult).value);
              }
            })
            return true;
          })
          .onDeleteComplete(() => {
            console.info("---------------------- onDeleteComplete ------------------------");
          })
          .borderWidth(1)
          .borderColor(Color.Green)
          .width("100%")
          .height('80.00%')
      }
      .borderWidth(1)
      .borderColor(Color.Red)
      .width("100%")
      .height("70%")
    }
```

![image](public_sys-resources/zh-cn_image_0000002553364965.webp)

**示例5（Span绑定手势事件）**

为Span绑定[gesture](#ZH-CN_TOPIC_0000002522080846__richeditorgesture11)回调。

```ets
// xxx.ets
@Entry
@Component
struct Index {
  controller: RichEditorController = new RichEditorController();
  options: RichEditorOptions = { controller: this.controller };
  @State textFlag: string = "TextFlag";

  build() {
    Column() {
        Text(this.textFlag)
          .copyOption(CopyOptions.InApp)
          .fontSize(50)
          .height(150)
      }
      Divider()
      Column() {
        RichEditor(this.options)
          .onReady(() => {
            this.controller.addTextSpan('Area1\n', {
              style:
              {
                fontColor: Color.Orange,
                fontSize: 50,
              },
              gesture:
              {
                onClick: () => {
                  this.textFlag = "Area1 is onClick.";
                },
                onLongPress: () => {
                  this.textFlag = "Area1 is onLongPress.";
                }
            })

            this.controller.addTextSpan('Area2\n', {
              style:
              {
                fontColor: Color.Blue,
                fontSize: 50
              },
              gesture:
              {
                onClick: () => {
                  this.textFlag = "Area2 is onClick.";
                },
                onLongPress: () => {
                  this.textFlag = "Area2 is onLongPress.";
                }
            })

            // $r('app.media.startIcon')需要替换为开发者所需的图像资源文件。
            this.controller.addImageSpan($r('app.media.startIcon'),
              {
                imageStyle:
                {
                  size: ["100px", "100px"],
                  layoutStyle: {
                    margin: 5,
                    borderRadius: 15
                  }
                },
                gesture:
                {
                  onClick: () => {
                    this.textFlag = "ImageSpan is onClick.";
                  },
                  onLongPress: () => {
                    this.textFlag = "ImageSpan is onLongPress.";
                  }
                },
                onHover : (status) => {
                  this.textFlag = "ImageSpan is onHover :" + status;
                }
              })
      }
      .borderWidth(1)
      .borderColor(Color.Red)
      .width("100%")
      .height("70%")
    }
```

![image](public_sys-resources/zh-cn_image_0000002522245042.webp)

**示例6（更新和获取段落样式）**

通过[updateParagraphStyle](#ZH-CN_TOPIC_0000002522080846__updateparagraphstyle11)接口更新段落样式，通过[getParagraphs](#ZH-CN_TOPIC_0000002522080846__getparagraphs11)接口获取指定范围段落的信息。

```ets
// xxx.ets
@Entry
@Component
struct Index {
  controller: RichEditorController = new RichEditorController();
  private spanParagraphs: RichEditorParagraphResult[] = [];

  build() {
    Column() {
      RichEditor({ controller: this.controller })
        .onReady(() => {
          this.controller.addTextSpan("0123456789\n", {
            style: {
              fontColor: Color.Pink,
              fontSize: "32"
            },
            paragraphStyle: {
              textAlign: TextAlign.Start,
              textVerticalAlign: TextVerticalAlign.BASELINE,
              leadingMargin: 16
            }
          })
          this.controller.addTextSpan("0123456789")
        })
        .width("80%")
        .height("30%")
        .border({ width: 1, radius: 5 })
        .draggable(false)

      Column({ space: 5 }) {
        Button("段落左对齐").onClick(() => {
          this.controller.updateParagraphStyle({ start: -1, end: -1,
            style: {
              textAlign: TextAlign.Start
            }
          })

        Button("段落右对齐").onClick(() => {
          this.controller.updateParagraphStyle({ start: -1, end: -1,
            style: {
              textAlign: TextAlign.End
            }
          })

        Button("段落居中").onClick(() => {
          this.controller.updateParagraphStyle({ start: -1, end: -1,
            style: {
              textAlign: TextAlign.Center
            }
          })

        Button("段落间距设置50").onClick(() => {
          this.controller.updateParagraphStyle({ start: -1, end: -1,
            style: {
              paragraphSpacing: 50
            }
          })
        Divider()
        Button("getParagraphs").onClick(() => {
          this.spanParagraphs = this.controller.getParagraphs({ start: -1, end: -1 });
          console.info("RichEditor getParagraphs:" + JSON.stringify(this.spanParagraphs));
        })

        Button("UpdateSpanStyle1").onClick(() => {
          this.controller.updateSpanStyle({ start: -1, end: -1,
            textStyle: {
              fontColor: Color.Brown,
              fontSize: 20
            }
          })

        Button("UpdateSpanStyle2").onClick(() => {
          this.controller.updateSpanStyle({ start: -1, end: -1,
            textStyle: {
              fontColor: Color.Green,
              fontSize: 30
            }
          })
      }
```

![image](public_sys-resources/zh-cn_image_0000002553205003.webp)

**示例7（更新预设样式与缩进）**

通过[setTypingStyle](#ZH-CN_TOPIC_0000002522080846__settypingstyle11)接口更新文本预设样式，通过[updateParagraphStyle](#ZH-CN_TOPIC_0000002522080846__updateparagraphstyle11)接口设置段落缩进。

```ets
// xxx.ets

const canvasWidth = 1000;
const canvasHeight = 100;
const Indentation = 40;
class LeadingMarginCreator {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private offscreenCanvas: OffscreenCanvas = new OffscreenCanvas(canvasWidth, canvasHeight);
  private offContext: OffscreenCanvasRenderingContext2D = this.offscreenCanvas.getContext("2d", this.settings);
  public static instance: LeadingMarginCreator = new LeadingMarginCreator();

  // 获得字体字号级别，分别是从0到4级
  public getFontSizeLevel(fontSize: number) {
    const fontScaled: number = Number(fontSize) / 16;

    enum FontSizeScaleThreshold {
      SMALL = 0.9,
      NORMAL = 1.1,
      LEVEL_1_LARGE = 1.2,
      LEVEL_2_LARGE = 1.4,
      LEVEL_3_LARGE = 1.5
    }

    let fontSizeLevel: number = 1;

    if (fontScaled < FontSizeScaleThreshold.SMALL) {
      fontSizeLevel = 0;
    } else if (fontScaled < FontSizeScaleThreshold.NORMAL) {
      fontSizeLevel = 1;
    } else if (fontScaled < FontSizeScaleThreshold.LEVEL_1_LARGE) {
      fontSizeLevel = 2;
    } else if (fontScaled < FontSizeScaleThreshold.LEVEL_2_LARGE) {
      fontSizeLevel = 3;
    } else if (fontScaled < FontSizeScaleThreshold.LEVEL_3_LARGE) {
      fontSizeLevel = 4;
    } else {
      fontSizeLevel = 1;
    }

    return fontSizeLevel;
  }
  // 获得字体字号级别，分别是从0到4级
  public getmarginLevel(Width: number) {
    let marginlevel: number = 1;
    if (Width == 40) {
      marginlevel = 2.0;
    } else if (Width == 80) {
      marginlevel = 1.0;
    } else if (Width == 120) {
      marginlevel = 2/3;
    } else if (Width == 160) {
      marginlevel = 0.5;
    } else if (Width == 200) {
      marginlevel = 0.4;
    }
    return marginlevel;
  }

  public genStrMark(fontSize: number, str: string): PixelMap {
    this.offContext = this.offscreenCanvas.getContext("2d", this.settings);
    this.clearCanvas()
    this.offContext.font = fontSize + 'vp sans-serif';
    this.offContext.fillText(str + '.', 0, fontSize * 0.9)
    return this.offContext.getPixelMap(0, 0, fontSize * (str.length + 1) / 1.75, fontSize)
  }

  public genSquareMark(fontSize: number): PixelMap {
    this.offContext = this.offscreenCanvas.getContext("2d", this.settings);
    this.clearCanvas()
    const coordinate = fontSize * (1 - 1 / 1.5) / 2;
    const sideLength = fontSize / 1.5;
    this.offContext.fillRect(coordinate, coordinate, sideLength, sideLength)
    return this.offContext.getPixelMap(0, 0, fontSize, fontSize)
  }

  // 生成圆圈符号
  public genCircleMark(fontSize: number, width: number, level?: number ): PixelMap {
    const indentLevel = level ?? 1;
    const offsetLevel = [22, 28, 32, 34, 38];
    const fontSizeLevel = this.getFontSizeLevel(fontSize);
    const marginlevel = this.getmarginLevel(width);
    const newCanvas = new OffscreenCanvas(canvasWidth, canvasHeight);
    const newOffContext: OffscreenCanvasRenderingContext2D = newCanvas.getContext("2d", this.settings);
    const centerCoordinate = 50;
    const radius = 10;
    this.clearCanvas()
    newOffContext.ellipse(100 * (indentLevel + 1) - centerCoordinate * marginlevel, offsetLevel[fontSizeLevel], radius * marginlevel, radius, 0, 0, 2 * Math.PI)
    newOffContext.fillStyle = '66FF0000';
    newOffContext.fill()
    return newOffContext.getPixelMap(0, 0, 100 + 100 * indentLevel, 100)
  }

  private clearCanvas() {
    this.offContext.clearRect(0, 0, canvasWidth, canvasHeight)
  }

@Entry
@Component
struct Index {
  controller: RichEditorController = new RichEditorController();
  options: RichEditorOptions = { controller: this.controller };
  private leadingMarkCreatorInstance = LeadingMarginCreator.instance;
  private fontNameRawFile: string = 'MiSans-Bold';
  @State fs: number = 30;
  @State cl: number = Color.Black;
  private leftMargin: Dimension = 0;
  private richEditorTextStyle: RichEditorTextStyle = {};

  aboutToAppear() {
    this.getUIContext().getFont().registerFont({
      familyName: 'MiSans-Bold',
      familySrc: '/font/MiSans-Bold.ttf'
    })
  }

  build() {
    Scroll() {
      Column() {
        RichEditor(this.options)
          .onReady(() => {
            this.controller.addTextSpan("0123456789\n",
              {
                style:
                {
                  fontWeight: 'medium',
                  fontFamily: this.fontNameRawFile,
                  fontColor: Color.Red,
                  fontSize: 50,
                  fontStyle: FontStyle.Italic,
                  decoration: { type: TextDecorationType.Underline, color: Color.Green }
                }
              })

            this.controller.addTextSpan("abcdefg",
              {
                style:
                {
                  fontWeight: FontWeight.Lighter,
                  fontFamily: 'HarmonyOS Sans',
                  fontColor: 'rgba(0,128,0,0.5)',
                  fontSize: 30,
                  fontStyle: FontStyle.Normal,
                  decoration: { type: TextDecorationType.Overline, color: 'rgba(169, 26, 246, 0.50)' }
                }
              })
          .borderWidth(1)
          .borderColor(Color.Green)
          .width("100%")
          .height("50%")

        Row({ space: 5 }) {
          Button('setTypingStyle1')
            .fontSize(10)
            .onClick(() => {
              this.controller.setTypingStyle(
                {
                  fontWeight: 'medium',
                  fontFamily: this.fontNameRawFile,
                  fontColor: Color.Blue,
                  fontSize: 50,
                  fontStyle: FontStyle.Italic,
                  decoration: { type: TextDecorationType.Underline, color: Color.Green }
                })

          Button('setTypingStyle2')
            .fontSize(10)
            .onClick(() => {
              this.controller.setTypingStyle(
                {
                  fontWeight: FontWeight.Lighter,
                  fontFamily: 'HarmonyOS Sans',
                  fontColor: Color.Green,
                  fontSize: '30',
                  fontStyle: FontStyle.Normal,
                  decoration: { type: TextDecorationType.Overline, color: 'rgba(169, 26, 246, 0.50)' }
                })
        }
        Divider()
        Button("getTypingStyle").onClick(() => {
          this.richEditorTextStyle = this.controller.getTypingStyle();
          console.info("RichEditor getTypingStyle:" + JSON.stringify(this.richEditorTextStyle));
        })
        Divider()
        Row({ space: 5 }) {
          Button("向右列表缩进").onClick(() => {
            let margin = Number(this.leftMargin);
            if (margin < 200) {
              margin += Indentation;
              this.leftMargin = margin;
            }
            this.controller.updateParagraphStyle({
              start: -10,
              end: -10,
              style: {
                leadingMargin : {
                  pixelMap : this.leadingMarkCreatorInstance.genCircleMark(100, margin, 1),
                  size: [margin, 40]
                }
            })

          Button("向左列表缩进").onClick(() => {
            let margin = Number(this.leftMargin);
            if (margin > 0) {
              margin -= Indentation;
              this.leftMargin = margin;
            }
            this.controller.updateParagraphStyle({
              start: -10,
              end: -10,
              style: {
                leadingMargin : {
                  pixelMap : this.leadingMarkCreatorInstance.genCircleMark(100, margin, 1),
                  size: [margin, 40]
                }
            })
        }
        Divider()
        Row({ space: 5 }) {
          Button("向右空白缩进").onClick(() => {
            let margin = Number(this.leftMargin);
            if (margin < 200) {
              margin += Indentation;
              this.leftMargin = margin;
            }
            this.controller.updateParagraphStyle({
              start: -10,
              end: -10,
              style: {
                leadingMargin: margin
              }
            })

          Button("向左空白缩进").onClick(() => {
            let margin = Number(this.leftMargin)
            if (margin > 0) {
              margin -= Indentation;
              this.leftMargin = margin;
            }
            this.controller.updateParagraphStyle({
              start: -10,
              end: -10,
              style: {
                leadingMargin: margin
              }
            })
        }
      }.borderWidth(1).borderColor(Color.Red)
    }
```

![image](public_sys-resources/zh-cn_image_0000002522085050.webp)

**示例8（设置文本字重与阴影）**

通过[updateParagraphStyle](#ZH-CN_TOPIC_0000002522080846__updateparagraphstyle11)接口设置文本字重与阴影。

```ets
@Entry
@Component
struct Index {
  controller: RichEditorController = new RichEditorController();
  options: RichEditorOptions = { controller: this.controller };
  private start: number = -1;
  private end: number = -1;
  @State message: string = "[-1, -1]"
  @State content: string = ""
  @State textShadows : Array<ShadowOptions> = [
    { radius: 10, color: Color.Red, offsetX: 10, offsetY: 0 },
    { radius: 10, color: Color.Black, offsetX: 20, offsetY: 0 },
    { radius: 10, color: Color.Brown, offsetX: 30, offsetY: 0 },
    { radius: 10, color: Color.Green, offsetX: 40, offsetY: 0 },
    { radius: 10, color: Color.Yellow, offsetX: 100, offsetY: 0 }
  ];

  build() {
    Column() {
        Text("selection range:").width("100%")
        Text() {
          Span(this.message)
        }.width("100%")
        Text("selection content:").width("100%")
        Text() {
          Span(this.content)
        }.width("100%")
      }
      .borderWidth(1)
      .borderColor(Color.Red)
      .width("100%")
      .height("20%")
      Row() {
        Button("更新样式: 加粗 & 文本阴影").onClick(() => {
          this.controller.updateSpanStyle({
            start: this.start,
            end: this.end,
            textStyle:
            {
              fontWeight: FontWeight.Bolder,
              textShadow: this.textShadows
            }
          })
      }
      .borderWidth(1)
      .borderColor(Color.Red)
      .width("100%")
      .height("10%")
      Column() {
        RichEditor(this.options)
          .onReady(() => {
            this.controller.addTextSpan("0123456789",
              {
                style:
                {
                  fontColor: Color.Orange,
                  fontSize: 30,
                  textShadow: { radius: 10, color: Color.Blue, offsetX: 10, offsetY: 0 }
                }
              })
          .borderWidth(1)
          .borderColor(Color.Green)
          .width("100%")
          .height("30%")
      }
      .borderWidth(1)
      .borderColor(Color.Red)
      .width("100%")
      .height("70%")
    }
```

![image](public_sys-resources/zh-cn_image_0000002553364967.webp)

**示例9（添加用户自定义布局Span）**

通过[addBuilderSpan](#ZH-CN_TOPIC_0000002522080846__addbuilderspan11)接口添加用户自定义布局Span。

```ets
@Builder
function placeholderBuilder2() {
  Row({ space: 2 }) {
    // $r('app.media.startIcon')需要替换为开发者所需的图像资源文件。
    Image($r('app.media.startIcon')).width(24).height(24).margin({ left: -5 })
    Text('okokokok').fontSize(10)
  }.width('20%').height(50).padding(10).backgroundColor(Color.Red)
}

// xxx.ets
@Entry
@Component
struct Index {
  controller: RichEditorController = new RichEditorController();
  option: RichEditorOptions = { controller: this.controller };
  private start: number = 2;
  private end: number = 4;
  @State message: string = "[-1, -1]";
  @State content: string = "";
  private my_offset: number | undefined = undefined;
  private my_builder: CustomBuilder = undefined;
  @BuilderParam my_builder2:() => void = placeholderBuilder2;

  @Builder
  placeholderBuilder() {
    Row({ space: 2 }) {
      // $r('app.media.startIcon')需要替换为开发者所需的图像资源文件。
      Image($r('app.media.startIcon')).width(24).height(24).margin({ left: -5 })
      Text('Custom Popup').fontSize(10)
    }.width(100).height(50).padding(5)
  }

  @Builder
  placeholderBuilder3() {
    Text("hello").padding('20').borderWidth(1).width('100%')
  }

  @Builder
  placeholderBuilder4() {
    Column() {
      Column({ space: 5 }) {
        Text('direction:Row').fontSize(9).fontColor(0xCCCCCC).width('90%')
        Flex({ direction: FlexDirection.Row }) { // 子组件在容器主抽上行布局
          Text('1').width('20%').height(50).backgroundColor(0xF5DEB3)
          Text('1').width('20%').height(50).backgroundColor(0xD2B48C)
          Text('1').width('20%').height(50).backgroundColor(0xF5DEB3)
          Text('1').width('20%').height(50).backgroundColor(0xD2B48C)
        }
        .height(70)
        .width('90%')
        .padding(10)
        .backgroundColor(0xAFEEEE)

        Text('direction:RowReverse').fontSize(9).fontColor(0xCCCCCC).width('90%')
        Flex({ direction: FlexDirection.RowReverse }) { // 子组件在容器主抽上反向行布局
          Text('1').width('20%').height(50).backgroundColor(0xF5DEB3)
          Text('1').width('20%').height(50).backgroundColor(0xD2B48C)
          Text('1').width('20%').height(50).backgroundColor(0xF5DEB3)
          Text('1').width('20%').height(50).backgroundColor(0xD2B48C)
        }
        .height(70)
        .width('90%')
        .padding(10)
        .backgroundColor(0xAFEEEE)

        Text('direction:Column').fontSize(9).fontColor(0xCCCCCC).width('90%')
        Flex({ direction: FlexDirection.Column }) { // 子组件在容器主抽上列布局
          Text('1').width('20%').height(40).backgroundColor(0xF5DEB3)
          Text('1').width('20%').height(40).backgroundColor(0xD2B48C)
          Text('1').width('20%').height(40).backgroundColor(0xF5DEB3)
          Text('1').width('20%').height(40).backgroundColor(0xD2B48C)
        }
        .height(160)
        .width('90%')
        .padding(10)
        .backgroundColor(0xAFEEEE)

        Text('direction:ColumnReverse').fontSize(9).fontColor(0xCCCCCC).width('90%')
        Flex({ direction: FlexDirection.ColumnReverse }) { // 子组件在容器主抽上反向列布局
          Text('1').width('20%').height(40).backgroundColor(0xF5DEB3)
          Text('1').width('20%').height(40).backgroundColor(0xD2B48C)
          Text('1').width('20%').height(40).backgroundColor(0xF5DEB3)
          Text('1').width('20%').height(40).backgroundColor(0xD2B48C)
        }
        .height(160)
        .width('90%')
        .padding(10)
        .backgroundColor(0xAFEEEE)
      }.width('100%').margin({ top: 5 })
    }.width('100%')
  }

  @Builder
  MyMenu() {
    Menu() {
      // $r('app.media.startIcon')需要替换为开发者所需的图像资源文件。
      MenuItem({ startIcon: $r('app.media.startIcon'), content: "菜单选项1" })
      MenuItem({ startIcon: $r('app.media.startIcon'), content: "菜单选项2" })
        .enabled(false)
    }

  build() {
    Column() {
        Text("selection range:").width("100%")
        Text() {
          Span(this.message)
        }.width("100%")

        Text("selection content:").width("100%")
        Text() {
          Span(this.content)
        }.width("100%")
      }
      .borderWidth(1)
      .borderColor(Color.Red)
      .width("100%")
      .height("20%")

      Row() {
        Button("获取选择内容 getSpans").onClick(() => {
          console.info('getSpans='+JSON.stringify(this.controller.getSpans({ start:1, end:5 })));
          console.info('getParagraphs='+JSON.stringify(this.controller.getParagraphs({ start:1, end:5 })));
          this.content = "";
          this.controller.getSpans({
            start: this.start,
            end: this.end
          }).forEach(item => {
            if (typeof (item as RichEditorImageSpanResult)['imageStyle'] != 'undefined') {
              if ((item as RichEditorImageSpanResult).valueResourceStr == "") {
                console.info("builder span index " + (item as RichEditorImageSpanResult).spanPosition.spanIndex + ", range : " + (item as RichEditorImageSpanResult).offsetInSpan[0] + ", " +
                  (item as RichEditorImageSpanResult).offsetInSpan[1] + ", size : " + (item as RichEditorImageSpanResult).imageStyle[0] + ", " + (item as RichEditorImageSpanResult).imageStyle[1])
              } else {
                console.info("image span " + (item as RichEditorImageSpanResult).valueResourceStr + ", index : " + (item as RichEditorImageSpanResult).spanPosition.spanIndex + ", range: " +
                  (item as RichEditorImageSpanResult).offsetInSpan[0] + ", " + (item as RichEditorImageSpanResult).offsetInSpan[1] + ", size : " +
                  (item as RichEditorImageSpanResult).imageStyle.size[0] + ", " + (item as RichEditorImageSpanResult).imageStyle.size[1])
              }
            } else {
              this.content += (item as RichEditorTextSpanResult).value;
              this.content += "\n";
              console.info("text span: " + (item as RichEditorTextSpanResult).value);
            }
          })
        Button("获取选择内容 getSelection").onClick(() => {
          this.content = "";
          let select = this.controller.getSelection();
          console.info("selection start " + select.selection[0] + " end " + select.selection[1]);
          select.spans.forEach(item => {
            if (typeof (item as RichEditorImageSpanResult)['imageStyle'] != 'undefined') {
              if ((item as RichEditorImageSpanResult).valueResourceStr == "") {
                console.info("builder span index " + (item as RichEditorImageSpanResult).spanPosition.spanIndex + ", range : " + (item as RichEditorImageSpanResult).offsetInSpan[0] + ", " +
                  (item as RichEditorImageSpanResult).offsetInSpan[1] + ", size : " + (item as RichEditorImageSpanResult).imageStyle[0] + ", " + (item as RichEditorImageSpanResult).imageStyle[1])
              } else {
                console.info("image span " + (item as RichEditorImageSpanResult).valueResourceStr + ", index : " + (item as RichEditorImageSpanResult).spanPosition.spanIndex + ", range: " +
                  (item as RichEditorImageSpanResult).offsetInSpan[0] + ", " + (item as RichEditorImageSpanResult).offsetInSpan[1] + ", size : " +
                  (item as RichEditorImageSpanResult).imageStyle.size[0] + ", " + (item as RichEditorImageSpanResult).imageStyle.size[1])
              }
            } else {
              this.content += (item as RichEditorTextSpanResult).value;
              this.content += "\n";
              console.info("text span: " + (item as RichEditorTextSpanResult).value);
            }
          })
        Button("删除选择内容").onClick(() => {
          this.controller.deleteSpans({
            start: this.start,
            end: this.end
          })
      }
      .borderWidth(1)
      .borderColor(Color.Red)
      .width("100%")
      .height("10%")

      Column() {
        RichEditor(this.option)
          .onReady(() => {
            this.controller.addTextSpan("0123456789",
              {
                style:
                {
                  fontColor: Color.Orange,
                  fontSize: 30
                }
              })
            // $r('app.media.startIcon')需要替换为开发者所需的图像资源文件。
            this.controller.addImageSpan($r('app.media.startIcon'),
              {
                imageStyle:
                {
                  size: ["57px", "57px"]
                }
              })
          .onSelect((value: RichEditorSelection) => {
            this.start = value.selection[0];
            this.end = value.selection[1];
            this.message = "[" + this.start + ", " + this.end + "]";
            console.info("onSelect="+JSON.stringify(value));
          })
          .aboutToIMEInput((value: RichEditorInsertValue) => {
            console.info("---------------------- aboutToIMEInput --------------------");
            console.info("aboutToIMEInput="+JSON.stringify(value));
            console.info("insertOffset:" + value.insertOffset);
            console.info("insertValue:" + value.insertValue);
            return true;
          })
          .onIMEInputComplete((value: RichEditorTextSpanResult) => {
            console.info("---------------------- onIMEInputComplete --------------------");
            console.info("onIMEInputComplete="+JSON.stringify(value));
            console.info("spanIndex:" + value.spanPosition.spanIndex);
            console.info("spanRange:[" + value.spanPosition.spanRange[0] + "," + value.spanPosition.spanRange[1] + "]");
            console.info("offsetInSpan:[" + value.offsetInSpan[0] + "," + value.offsetInSpan[1] + "]");
            console.info("value:" + value.value);
          })
          .aboutToDelete((value: RichEditorDeleteValue) => {
            value.richEditorDeleteSpans.forEach(item => {
              console.info("---------------------- item --------------------");
              console.info("spanIndex=" + item.spanPosition.spanIndex);
              console.info("spanRange:[" + item.spanPosition.spanRange[0] + "," + item.spanPosition.spanRange[1] + "]");
              console.info("offsetInSpan:[" + item.offsetInSpan[0] + "," + item.offsetInSpan[1] + "]");
              if (typeof (item as RichEditorImageSpanResult)['imageStyle'] != 'undefined') {
                if ((item as RichEditorImageSpanResult).valueResourceStr == "") {
                  console.info("builder span index " + (item as RichEditorImageSpanResult).spanPosition.spanIndex + ", range : " + (item as RichEditorImageSpanResult).offsetInSpan[0] + ", " +
                  (item as RichEditorImageSpanResult).offsetInSpan[1] + ", size : " + (item as RichEditorImageSpanResult).imageStyle[0] + ", " + (item as RichEditorImageSpanResult).imageStyle[1])
                } else {
                  console.info("image span " + (item as RichEditorImageSpanResult).valueResourceStr + ", index : " + (item as RichEditorImageSpanResult).spanPosition.spanIndex + ", range: " +
                  (item as RichEditorImageSpanResult).offsetInSpan[0] + ", " + (item as RichEditorImageSpanResult).offsetInSpan[1] + ", size : " +
                  (item as RichEditorImageSpanResult).imageStyle.size[0] + ", " + (item as RichEditorImageSpanResult).imageStyle.size[1])
                }
              } else {
                console.info("delete text: " + (item as RichEditorTextSpanResult).value);
              }
            })
            return true;
          })
          .borderWidth(1)
          .borderColor(Color.Green)
          .width("100%")
          .height("30%")

        Button("add span")
          .onClick(() => {
            let num = this.controller.addBuilderSpan(this.my_builder,
              {
                offset: this.my_offset,
                accessibilitySpanOptions: { accessibilityText:"hello", accessibilityDescription:"world", accessibilityLevel:"yes" }
              });
            console.info('addBuilderSpan return ' + num);
          })
        Button("add image")
          .onClick(() => {
            // $r('app.media.startIcon')需要替换为开发者所需的图像资源文件。
            let num = this.controller.addImageSpan($r('app.media.startIcon'), {
              imageStyle: {
                size: ["50px", "50px"],
                verticalAlign: ImageSpanAlignment.BOTTOM,
                layoutStyle: {
                  borderRadius: undefined,
                  margin: undefined
                }
            })
            console.info('addImageSpan return' + num);
          })
        Row() {
          Button('builder1').onClick(() => {
            this.my_builder = () => {
              this.placeholderBuilder()
            };
          })
          Button('builder2').onClick(() => {
            this.my_builder = () => {
              this.my_builder2()
            };
          })
          Button('builder3').onClick(() => {
            this.my_builder = () => {
              this.placeholderBuilder3()
            };
          })
          Button('builder4').onClick(() => {
            this.my_builder = () => {
              this.placeholderBuilder4()
            };
          })
        }
      .borderWidth(1)
      .borderColor(Color.Red)
      .width("100%")
      .height("70%")
    }
```

![image](public_sys-resources/zh-cn_image_0000002522245044.webp)

**示例10（使用和管理组件内的BuilderSpan）**

通过[addBuilderSpan](#ZH-CN_TOPIC_0000002522080846__addbuilderspan11)接口添加的自定义布局Span，[getSpans](#ZH-CN_TOPIC_0000002522080846__getspans)、[onWillChange](#ZH-CN_TOPIC_0000002522080846__onwillchange12)等API不会返回BuilderSpan内部的信息。开发者需要自行维护BuilderSpan的状态，并且在组件内容发生变化时同步更新。

```ets
const TAG = 'BuilderSpanDemo';

class BuilderObject {
  content: string
  imageUri?: string
  type: string
  id?: string

  constructor(content: string, type: string, imageUri?: string, id?: string) {
    this.content = content
    this.imageUri = imageUri
    this.type = type
    this.id = id
  }

@Entry
@Component
struct Index {
  controller: RichEditorController = new RichEditorController()
  option: RichEditorOptions = { controller: this.controller }
  @State content: string = "";
  @State start: number = 0;
  @State end: number = 0;
  private customBuilder: CustomBuilder = undefined;
  private builderArray: BuilderObject[] = [];
  private indicesToRemove: number[] = [];
  private builderId: number = 0;

  @Builder
  imageTextBuilder(builder: BuilderObject) {
    Row({ space: 2 }) {
      Image($r(builder.imageUri)).width(24).height(24).margin({ left: -5 })
      Text(builder.content).fontSize(10)
    }.width(110).height(50).padding(5)
  }

  @Builder
  chipBuilder(builder: BuilderObject) {
    Row() {
      Text(builder.content)
        .fontSize(14)
        .fontColor(Color.Black)
        .fontFamily('HarmonyHeiTi')
        .margin({ right: 4 })

      SymbolGlyph($r('sys.symbol.xmark'))
        .width(16)
        .height(16)
        .id(builder.id)
        .onClick((event: ClickEvent) => {
          this.deleteChipBuilder(event.target.id)
        })
    }
    .width('auto')
    .height(28)
    .backgroundColor(Color.Gray)
    .borderRadius(10)
    .padding({
      top: 4,
      bottom: 4,
      left: 12,
      right: 12
    })
  }

  private deleteChipBuilder(builderId?: string) {
    if (builderId == null || builderId == "") {
      console.info(TAG, "delete chipBuilder error");
      return
    }
    let deleteRange: number[] = this.getTargetBuilderSpanRange(builderId)
    if (deleteRange.length == 0) {
      console.error(TAG, "getTargetBuilderSpanRange failed" + builderId);
      return
    }
    this.builderArray = this.builderArray.filter(item => item.id !== builderId);
    this.controller.deleteSpans({ start: deleteRange[0], end: deleteRange[1] });
    console.info(TAG, `deleteChipBuilder start = ${deleteRange[0]}, end = ${deleteRange[1]}`);
    console.info(TAG, `deleteChipBuilder builderArray + ${this.builderArray.length}`);
  }

  private getTargetBuilderSpanRange(builderId: string): number[] {
    let allSpans = this.controller.getSpans();
    let result: number[] = [];
    let chitBuilderIndex = 0;
    for (let spanIndex = 0; spanIndex < allSpans.length; spanIndex++) {
      if (!this.isBuilderSpanResult(allSpans[spanIndex])) {
        continue;
      }
      if (this.builderArray.length <= chitBuilderIndex) {
        break;
      }
      if (this.builderArray[chitBuilderIndex].id === builderId) {
        result = allSpans[spanIndex].spanPosition.spanRange;
        break;
      }
      chitBuilderIndex++;
    }
    return result;
  }

  private isTextSpanResult(item: RichEditorImageSpanResult | RichEditorTextSpanResult): boolean {
    return typeof (item as RichEditorImageSpanResult)['imageStyle'] == 'undefined';
  }

  private isBuilderSpanResult(item: RichEditorImageSpanResult | RichEditorTextSpanResult): boolean {
    return typeof (item as RichEditorImageSpanResult)['imageStyle'] != 'undefined'
      && ((item as RichEditorImageSpanResult).valueResourceStr == " "
        || (item as RichEditorImageSpanResult).valueResourceStr == "");
  }

  build() {
    Column() {
      Scroll() {
        Column() {
          Text("Builder Info:").width("100%")
          Text() {
            Span(this.content)
          }.width("100%")
        }
      .borderWidth(1)
      .borderColor(Color.Red)
      .width("100%")
      .height("20%")

      // 添加Builder时，记录builder的相对顺序，以及builder信息
      // getSpans接口valueResourceStr == " "或""的Span是builderSpan，并且会按顺序返回builder
      // 可以根据上面两点，在查询时还原builder信息
      Button("addImageTextBuilder")
        .onClick(() => {
          let insertOffset = this.controller.getCaretOffset();
          // 'app.media.startIcon'需要替换为开发者所需的图像资源文件。
          let builder = new BuilderObject('Custom PopUP ' + this.builderId, 'imageTextBuilder', 'app.media.startIcon');
          this.customBuilder = () => {
            this.imageTextBuilder(builder);
          }
          let addIndex = this.addBuilderByIndex(insertOffset);
          console.info(TAG, "add imageTextBuilder index = " + addIndex);
          this.builderArray.splice(addIndex, 0, builder);
          this.controller.addBuilderSpan(this.customBuilder, { offset: insertOffset });
          this.builderId++;
          console.info(TAG, "add imageTextBuilder success");
        })
      Button("addChipBuilder")
        .onClick(() => {
          let insertOffset = this.controller.getCaretOffset();
          let builder = new BuilderObject('Hello World ' + this.builderId, 'chipBuilder', '',
            'chipBuilder' + this.builderId);
          this.customBuilder = () => {
            this.chipBuilder(builder);
          }
          let addIndex = this.addBuilderByIndex(insertOffset);
          console.info(TAG, "add addChipBuilder index = " + addIndex);
          this.builderArray.splice(addIndex, 0, builder);
          this.controller.addBuilderSpan(this.customBuilder, { offset: insertOffset });
          this.builderId++;
          console.info(TAG, "add chipBuilder success");
        })

      Row() {
        Button("getSpans").onClick(() => {
          console.info(TAG, "getSpans = " + JSON.stringify(this.controller.getSpans()));
          this.content = "";
          let allSpans = this.controller.getSpans();
          let builderSpanIndex = 0;
          allSpans.forEach(item => {
            if (this.isTextSpanResult(item)) {
              console.info(TAG, "text span value: " + (item as RichEditorTextSpanResult).value);
            } else if (this.isBuilderSpanResult(item)) {
              let builderOrder = "This is builderSpan " + builderSpanIndex + ":"
              console.info(TAG, builderOrder);
              this.content += builderOrder + "\n";
              let builderResult = (item as RichEditorImageSpanResult);
              let builderIndex = "index: " + builderResult.spanPosition.spanIndex
                + ", range: " + builderResult.spanPosition.spanRange[0] + ", "
                + builderResult.spanPosition.spanRange[1];
              console.info(TAG, builderIndex);
              this.content += builderIndex + "\n";
              if (builderSpanIndex >= this.builderArray.length) {
                console.error(TAG, "getSpans error,  builderSpanIndex = " + builderSpanIndex
                  + ", builderArray.length = " + this.builderArray.length);
                return;
              }
              let builderInfo = "content: " + this.builderArray[builderSpanIndex].content
                + ", image uri: " + this.builderArray[builderSpanIndex].imageUri
                + ", id: " + this.builderArray[builderSpanIndex].id + "\n\n";
              console.info(TAG, builderInfo);
              this.content += builderInfo;
              builderSpanIndex++;
            } else {
              let imageResult = (item as RichEditorImageSpanResult);
              console.info(TAG, "image span " + imageResult.valueResourceStr + ", index: " +
              imageResult.spanPosition.spanIndex + ", range: " +
              imageResult.offsetInSpan[0] + ", " + imageResult.offsetInSpan[1] + ", size: " +
              imageResult.imageStyle.size[0] + ", " + imageResult.imageStyle.size[1]);
            }
          })
        Button("deleteSelectedSpans")
          .onClick(() => {
            this.start = this.controller.getSelection().selection[0];
            this.end = this.controller.getSelection().selection[1];
            if (this.start == this.end) {
              return;
            }
            let allSpans = this.controller.getSpans();
            let needRemoveIndex = 0;
            for (let i = 0; i < allSpans.length; i++) {
              if (!this.isBuilderSpanResult(allSpans[i])) {
                continue;
              }
              let builderIndex = (allSpans[i] as RichEditorImageSpanResult).spanPosition.spanRange[0];
              if (builderIndex < this.start || builderIndex >= this.end) {
                needRemoveIndex++;
                continue;
              }
              this.indicesToRemove.push(needRemoveIndex);
              needRemoveIndex++;
            }
            console.info(TAG, "deleteSpans indicesToRemove = " + this.indicesToRemove.toString());
            this.deleteBuilderByIndices();
            console.info(TAG, "deleteSpans builderArray = " + this.builderArray.length);
            this.controller.deleteSpans({ start: this.start, end: this.end });
          })
      }
      .borderWidth(1)
      .borderColor(Color.Red)
      .width("100%")
      .height("5%")

      Column() {
        RichEditor(this.option)
          .onReady(() => {
            this.controller.addTextSpan("0123456789",
              {
                style:
                {
                  fontColor: Color.Orange,
                  fontSize: 30
                }
              })
          .aboutToDelete((value: RichEditorDeleteValue) => {
            console.info(TAG, "aboutToDelete = " + JSON.stringify(value));
            let isBuilderAboutToDelete = this.isBuilderAboutToDelete(value);
            console.info(TAG, "aboutToDelete isBuilderAboutToDelete = " + isBuilderAboutToDelete);
            this.getIndicesToRemove(value, isBuilderAboutToDelete);
            console.info(TAG, "indicesToRemove = " + this.indicesToRemove.toString());
            this.deleteBuilderByIndices();
            console.info(TAG, "builderArray = " + this.builderArray.length);
            return true;
          })
          .borderWidth(1)
          .borderColor(Color.Green)
          .width("100%")
          .height("30%")
      }
      .margin({ top: 60 })
      .borderWidth(1)
      .borderColor(Color.Red)
      .width("100%")
      .height("70%")
    }

  private isBuilderAboutToDelete(value: RichEditorDeleteValue): boolean {
    let flag = false;
    for (let i = 0; i < value.richEditorDeleteSpans.length; i++) {
      if (this.isBuilderSpanResult(value.richEditorDeleteSpans[i])) {
        flag = true;
        break;
      }
    return flag;
  }

  private getIndicesToRemove(value: RichEditorDeleteValue, isBuilderAboutToDelete: boolean): void {
    if (!isBuilderAboutToDelete) {
      return
    }
    let allSpans = this.controller.getSpans();
    for (let i = 0; i < value.richEditorDeleteSpans.length; i++) {
      let needRemoveIndex = 0;
      let item = value.richEditorDeleteSpans[i];
      if (!this.isBuilderSpanResult(item)) {
        continue;
      }
      let aboutToDeleteBuilderIndex = (item as RichEditorImageSpanResult).spanPosition.spanIndex
      for (let j = 0; j < allSpans.length; j++) {
        if (!this.isBuilderSpanResult(allSpans[j])) {
          continue;
        }
        let builderIndex = (allSpans[j] as RichEditorImageSpanResult).spanPosition.spanIndex
        if (builderIndex == aboutToDeleteBuilderIndex) {
          this.indicesToRemove.push(needRemoveIndex)
          break;
        }
        needRemoveIndex++;
      }

  private deleteBuilderByIndices(): void {
    let indicesSet: Set<number> = new Set(this.indicesToRemove);
    let newLength = 0;
    for (let i = 0; i < this.builderArray.length; i++) {
      if (!indicesSet.has(i)) {
        this.builderArray[newLength] = this.builderArray[i];
        newLength++;
      }
    this.builderArray.length = newLength;
    this.indicesToRemove.length = 0;
  }

  private addBuilderByIndex(insertOffset: number): number {
    if (insertOffset == 0 || this.builderArray.length == 0) {
      return 0;
    }
    let allSpans = this.controller.getSpans();
    let addIndex = 0;
    for (let i = 0; i < allSpans.length; i++) {
      if (!this.isBuilderSpanResult(allSpans[i])) {
        continue;
      }
      let builderIndex = (allSpans[i] as RichEditorImageSpanResult).spanPosition.spanRange[0];
      if (builderIndex < insertOffset) {
        addIndex++;
        continue;
      }
      break;
    }
    return addIndex;
  }
```

![image](public_sys-resources/zh-cn_image_0000002553205005.webp)

**示例11（设置文本识别配置）**

设置[enableDataDetector](#ZH-CN_TOPIC_0000002522080846__enabledatadetector11)为true时，通过[dataDetectorConfig](#ZH-CN_TOPIC_0000002522080846__datadetectorconfig11)接口设置文本识别配置。

```ets
@Entry
@Component
struct TextExample7 {
  controller: RichEditorController = new RichEditorController();
  options: RichEditorOptions = { controller: this.controller };
  @State phoneNumber: string = '(86) (755) ********';
  @State url: string = 'www.********.com';
  @State email: string = '***@example.com';
  @State address: string = 'XX省XX市XX区XXXX';
  @State enableDataDetector: boolean = true;
  @State enablePreviewText: boolean = false;
  @State types: TextDataDetectorType[] = [];

  build() {
    Row() {
      Column() {
        RichEditor(this.options)
          .onReady(() => {
            this.controller.addTextSpan('电话号码：' + this.phoneNumber + '\n',
              {
                style:
                {
                  fontSize: 30
                }
              })
            this.controller.addTextSpan('链接：' + this.url + '\n',
              {
                style:
                {
                  fontSize: 30
                }
              })
            this.controller.addTextSpan('邮箱：' + this.email + '\n',
              {
                style:
                {
                  fontSize: 30
                }
              })
            this.controller.addTextSpan('地址：' + this.address,
              {
                style:
                {
                  fontSize: 30
                }
              })
          .copyOptions(CopyOptions.InApp)
          .enableDataDetector(this.enableDataDetector)
          .dataDetectorConfig({types : this.types, onDetectResultUpdate: (result: string)=>{}})
          .enablePreviewText(this.enablePreviewText)
          .borderWidth(1)
          .padding(10)
          .width('100%')
      }
      .width('100%')
    }
```

**示例12（设置光标、手柄和底板颜色）**

通过[caretColor](#ZH-CN_TOPIC_0000002522080846__caretcolor12)属性设置输入框光标、手柄颜色，通过[selectedBackgroundColor](#ZH-CN_TOPIC_0000002522080846__selectedbackgroundcolor12)属性设置文本选中底板颜色。

```ets
@Entry
@Component
struct RichEditorDemo {
  @State color: Color = Color.Black;
  controller: RichEditorController = new RichEditorController();

  build() {
    Column() {
      Row() {
        Button("改为红色").onClick(() => {
          this.color = Color.Red;
        })
      }.margin({ top: 50 })

      RichEditor({ controller: this.controller })
        .onReady(() => {
          this.controller.addTextSpan('通过caretColor和selectedBackgroundColor属性设置光标和选中背景色');
        })
        .width("100%")
        .border({ width: 1, radius: 5 })
        .key('RichEditor')
        .caretColor(this.color)// 光标颜色
        .selectedBackgroundColor(this.color)// 选中背景色
        .margin({ top: 50 })
    }
    .width('100%')
  }
```

![image](public_sys-resources/zh-cn_image_0000002522085052.webp)

**示例13（设置行高和字符间距）**

通过[updateSpanStyle](#ZH-CN_TOPIC_0000002522080846__updatespanstyle)接口配置文本行高（[lineHeight](#ZH-CN_TOPIC_0000002522080846__richeditortextstyle)）和字符间距（[letterSpacing](#ZH-CN_TOPIC_0000002522080846__richeditortextstyle)）。

```ets
@Entry
@Component
struct RichEditorDemo03 {
  controller: RichEditorController = new RichEditorController();
  options: RichEditorOptions = { controller: this.controller };
  @State start: number = -1;
  @State end: number = -1;
  @State LH:number = 50;
  @State LS:number = 20;

  build() {
    Column() {
      Scroll(){
        Column(){
          Row() {
            Button("行高++").onClick(()=>{
              this.LH = this.LH + 5;
              this.controller.updateSpanStyle({
                start: this.start,
                end: this.end,
                textStyle:
                {
                  lineHeight: this.LH
                }
              })
            Button("行高--").onClick(()=>{
              this.LH = this.LH - 5;
              this.controller.updateSpanStyle({
                start: this.start,
                end: this.end,
                textStyle:
                {
                  lineHeight: this.LH
                }
              })
            Button("字符间距++").onClick(()=>{
              this.LS = this.LS + 5
              this.controller.updateSpanStyle({
                start: this.start,
                end: this.end,
                textStyle:
                {
                  letterSpacing: this.LS
                }
              })
            Button("字符间距--").onClick(()=>{
              this.LS = this.LS - 5
              this.controller.updateSpanStyle({
                start: this.start,
                end: this.end,
                textStyle:
                {
                  letterSpacing: this.LS
                }
              })
          }
      }.borderWidth(1)
      .borderColor(Color.Red)
      .width("100%")
      .height("20%")
      .margin({top: 20})

      Scroll(){
        Column() {
          Text("LineHeight:" + this.LH).width("100%")
          Text("LetterSpacing:" + this.LS).width("100%")
        }
      .borderWidth(1)
      .borderColor(Color.Red)
      .width("100%")
      .height("20%")
      .margin({bottom: 20})

      Column() {
        RichEditor(this.options).clip(true).padding(10)
          .onReady(() => {
            this.controller.addTextSpan("012345",
              {
                style:
                {
                  fontColor: Color.Orange,
                  fontSize: 30,
                  lineHeight: this.LH,
                  letterSpacing: this.LS
                }
              })
            this.controller.addTextSpan("6789",
              {
                style:
                {
                  fontColor: Color.Black,
                  fontSize: 30,
                  lineHeight: this.LH,
                  letterSpacing: this.LS
                }
              })
          .borderWidth(1)
          .borderColor(Color.Green)
          .width(400)
          .height(400)
      }
      .borderWidth(1)
      .borderColor(Color.Red)
      .width("100%")
      .height("60%")
    }
```

![image](public_sys-resources/zh-cn_image_0000002553364969.webp)

**示例14（自定义粘贴事件）**

为组件添加[onPaste](#ZH-CN_TOPIC_0000002522080846__onpaste11)事件，通过[PasteEvent](#ZH-CN_TOPIC_0000002522080846__pasteevent11)自定义用户粘贴事件。

```ets
@Entry
@Component
struct RichEditorDemo {
  controller: RichEditorController = new RichEditorController();
  options: RichEditorOptions = { controller: this.controller };

  build() {
    Column({ space: 2 }) {
      RichEditor(this.options)
        .onReady(() => {
          this.controller.addTextSpan('RichEditor preventDefault')
        })
        .onPaste((event?: PasteEvent) => {
          if (event != undefined && event.preventDefault) {
            event.preventDefault();
          }
        })
        .borderWidth(1)
        .borderColor(Color.Green)
        .width('100%')
        .height('40%')
    }
```

![image](public_sys-resources/zh-cn_image_0000002522245046.webp)

**示例15（配置文字特性效果）**

通过[addTextSpan](#ZH-CN_TOPIC_0000002522080846__addtextspan)接口设置文字特性效果（[fontFeature](#ZH-CN_TOPIC_0000002522080846__richeditortextstyle)）。当添加“ss01”特性的FontFeature属性时，数字“0”由原来的椭圆形改变为带有倒圆角形。

```ets
@Entry
@Component
struct RichEditorExample {
  controller: RichEditorController = new RichEditorController();
  options: RichEditorOptions = { controller: this.controller };
  @State enableDataDetector: boolean = true;
  @State types: TextDataDetectorType[] = [];
  build() {
    Row() {
      Column() {
        RichEditor(this.options)
          .onReady(() => {
            this.controller.addTextSpan('This is ss01 off :' + '0000' + '\n',
              {
                style:
                {
                  fontSize: 30
                }
              })
            this.controller.addTextSpan('This is ss01 on :' + '0000' + '\n',
              {
                style:
                {
                  fontSize: 30,
                  fontFeature: "\"ss01\" 1"
                }
              })
          .copyOptions(CopyOptions.InApp)
          .enableDataDetector(this.enableDataDetector)
          .dataDetectorConfig({types : this.types, onDetectResultUpdate: (result: string)=>{}})
          .borderWidth(1)
          .padding(10)
          .width('100%')
      }
      .width('100%')
      .margin({top:150})
    }
```

![image](public_sys-resources/zh-cn_image_0000002553205007.webp)

**示例16（自定义键盘避让）**

通过[customKeyboard](#ZH-CN_TOPIC_0000002522080846__customkeyboard)属性绑定自定义键盘，通过参数[KeyboardOptions](#ZH-CN_TOPIC_0000002522080846__keyboardoptions12)设置自定义键盘是否支持避让功能。

```ets
@Entry
@Component
struct RichEditorExample {
  controller: RichEditorController = new RichEditorController();
  @State height1: string | number = '80%';
  @State height2: number = 100;
  @State supportAvoidance: boolean = true;

  // 自定义键盘组件
  @Builder
  CustomKeyboardBuilder() {
    Column() {
      Row() {
        Button('增加特表情包').onClick(() => {
          this.controller.addTextSpan("\uD83D\uDE0A",
            {
              style:
              {
                fontColor: Color.Orange
              }
            })
      }

      Grid() {
        ForEach(['1', '2', '3', '4', '5', '6', '7', '8', '9', '*', '0', '#'], (item: string) => {
          GridItem() {
            Button(item).width(110).onClick(() => {
              this.controller.addTextSpan(item, {
                offset: this.controller.getCaretOffset(),
                style:
                {
                  fontColor: Color.Orange,
                  fontSize: 30
                }
              })
              this.controller.setCaretOffset(this.controller.getCaretOffset() + item.toString().length)
            })
          }
        })
      }.maxCount(3).columnsGap(10).rowsGap(10).padding(5)
    }.backgroundColor(Color.Gray)
  }

  build() {
    Column() {
      Row() {
        Button("20%")
          .fontSize(24)
          .onClick(() => {
            this.height1 = "20%";
          })
        Button("80%")
          .fontSize(24)
          .margin({ left: 20 })
          .onClick(() => {
            this.height1 = "80%";
          })
      }
      .justifyContent(FlexAlign.Center)
      .alignItems(VerticalAlign.Bottom)
      .height(this.height1)
      .width("100%")
      .padding({ bottom: 50 })

      RichEditor({ controller: this.controller })// 绑定自定义键盘
        .customKeyboard(this.CustomKeyboardBuilder(), { supportAvoidance: this.supportAvoidance })
        .margin(10)
        .border({ width: 1 })
        .borderWidth(1)
        .borderColor(Color.Red)
        .width("100%")
    }
```

![image](public_sys-resources/zh-cn_image_0000002522085054.webp)

**示例17（查看编辑状态）**

通过[isEditing](#ZH-CN_TOPIC_0000002522080846__isediting12)接口获取当前富文本的编辑状态。为组件添加[onEditingChange](#ZH-CN_TOPIC_0000002522080846__oneditingchange12)事件，可通过打印日志，获取当前组件是否在编辑态。

```ets
@Entry
@Component
struct RichEditor_onEditingChange {
  controller: RichEditorController = new RichEditorController();
  @State controllerIsEditing: boolean = false;
  @Builder

  build() {
    Column() {
      Row() {
        Button("点击查看编辑状态isEditing()：").onClick(() => {
          this.controllerIsEditing = this.controller.isEditing();
        })
          .padding(5)
        Text('' + this.controllerIsEditing)
          .width('100%')
          .padding(5)
          .fontColor(Color.Orange)
          .fontSize(20)
      }
      RichEditor({ controller: this.controller })
        .onEditingChange((isEditing: boolean) => {
          console.info("Current Editing Status:" + isEditing);
        })
        .height(400)
        .borderWidth(1)
        .borderColor(Color.Red)
        .width("100%")
    }
```

![image](public_sys-resources/zh-cn_image_0000002553364971.webp)

**示例18（配置文本变化回调）**

为组件添加[onWillChange](#ZH-CN_TOPIC_0000002522080846__onwillchange12)事件，能够在组件执行增删操作前，触发回调。

```ets
@Entry
@Component
struct RichEditorExample {
  controller: RichEditorController = new RichEditorController();
  build() {
    Column() {
      RichEditor({ controller: this.controller })
        .height(200)
        .borderWidth(1)
        .borderColor(Color.Red)
        .width("100%")
        .onReady(() => {
          this.controller.addTextSpan('测试文字TestWord', { style: { fontColor: Color.Orange, fontSize: 30 } })
          this.controller.updateSpanStyle({
            start: -1,
            end: -1,
            textStyle:
            {
              fontWeight: FontWeight.Bolder
            }
          })
        .onWillChange((value: RichEditorChangeValue) => {
          console.info('测试log: onWillChange');
          console.info('rangeBefore: ' + JSON.stringify(value.rangeBefore));
          console.info('print replacedSpans');
          value.replacedSpans.forEach((item: RichEditorTextSpanResult) => {
            console.info('spanPosition:' + JSON.stringify(item.spanPosition));
            console.info('value:' + item.value);
            console.info('textStyle:' + JSON.stringify(item.textStyle));
            console.info('offsetInSpan:' + item.offsetInSpan);
            console.info('valueResource:' + item.valueResource);
            console.info('paragraphStyle:' + JSON.stringify(item.paragraphStyle));
          })
          console.info('print replacedImageSpans');
          value.replacedImageSpans.forEach((item: RichEditorImageSpanResult) => {
            console.info('spanPosition:' + JSON.stringify(item.spanPosition));
            console.info('valuePixelMap:' + JSON.stringify(item.valuePixelMap));
            console.info('valueResourceStr:' + item.valueResourceStr);
            console.info('imageStyle:' + JSON.stringify(item.imageStyle));
            console.info('offsetInSpan:' + item.offsetInSpan);
          })
          console.info('print replacedSymbolSpans');
          value.replacedSymbolSpans.forEach((item: RichEditorTextSpanResult) => {
            console.info('spanPosition:' + JSON.stringify(item.spanPosition));
            console.info('value:' + item.value);
            console.info('offsetInSpan:' + item.offsetInSpan);
            console.info('symbolSpanStyle:' + JSON.stringify(item.symbolSpanStyle));
            console.info('valueResource:' + item.valueResource);
            console.info('paragraphStyle:' + JSON.stringify(item.paragraphStyle));
          })
          return true;
        })
        .onDidChange((rangeBefore: TextRange, rangeAfter: TextRange) => {
          console.info('测试log: onDidChange');
          console.info('rangeBefore:' + JSON.stringify(rangeBefore));
          console.info('rangeAfter:' + JSON.stringify(rangeAfter));
        })
        .onCut((event:CutEvent) => {
          event.preventDefault!()
          console.info('测试log：onCut');
        })
        .onCopy((event:CopyEvent) => {
          event.preventDefault!()
          console.info('测试log：onCopy');
        })
        .onPaste(()=>{
          console.info('测试log：onPaste');
        })
      Text('测试文字Hello')
        .lineHeight(50)
        .fontSize(24)
        .draggable(true)
        .onDragStart(()=>{})
      TextInput({text:'测试文字NiHao'})
        .draggable(true)
        .margin(20)
    }
```

**示例19（配置输入法enter键功能）**

通过[enterKeyType](#ZH-CN_TOPIC_0000002522080846__enterkeytype12)属性设置软键盘输入法回车键类型。

```ets
@Entry
@Component
struct SoftKeyboardEnterTypeExample {
  controller: RichEditorController = new RichEditorController();

    build() {
    Column() {
      Button("停止编辑").onClick(()=>{
        this.controller.stopEditing()
      })
      RichEditor({ controller: this.controller })
        .margin(10)
        .border({ width: 1 })
        .height(200)
        .borderWidth(1)
        .borderColor(Color.Red)
        .width("100%")
        .enterKeyType(EnterKeyType.Search)
        .onSubmit((enterKey: EnterKeyType, event: SubmitEvent) => {
          console.info("trigger richeditor onsubmit" + enterKey);
          this.controller.addTextSpan(" type["+ enterKey +"] triggered")
          event.keepEditableState()
        })
    }.height("100%").justifyContent(FlexAlign.Center)
  }
```

![image](public_sys-resources/zh-cn_image_0000002522245048.webp)

**示例20（设置段落折行规则）**

通过[updateParagraphStyle](#ZH-CN_TOPIC_0000002522080846__updateparagraphstyle11)接口设置折行类型（[lineBreakStrategy](#ZH-CN_TOPIC_0000002522080846__richeditorparagraphstyle11)），通过[getParagraphs](#ZH-CN_TOPIC_0000002522080846__getparagraphs11)接口获取当前段落的折行类型。

```ets
@Entry
@Component
struct LineBreakStrategyExample {
  controller: RichEditorController = new RichEditorController();
  private spanParagraphs: RichEditorParagraphResult[] = [];
  @State lineBreakOptionStr: string[] = ['GREEDY', 'HIGH_QUALITY', 'BALANCED'];
  @State attributeValue: string = "";
  @State testStr: string = "0123456789,0123456789,0123456789,0123456789,0123456789.";
  build() {
    Column() {
      RichEditor({ controller: this.controller })
        .onReady(() => {
          this.controller.addTextSpan(this.testStr, {
            style: {
              fontColor: Color.Black,
              fontSize: "32"
            },
            paragraphStyle: {
              textAlign: TextAlign.Start,
              lineBreakStrategy: LineBreakStrategy.GREEDY
            }
          })
        .width(400)
        .height(300)
        .margin({bottom:20})
        .draggable(false)
      Column(){
        Text('linebreak属性值为：' + this.attributeValue).fontSize(20).fontColor(Color.Black)
      }.margin({bottom: 10})
      Column({ space: 10 }) {
        Button("设置折行类型GREEDY").onClick(() => {
          this.controller.updateParagraphStyle({ start: -1, end: -1,
            style: {
              lineBreakStrategy: LineBreakStrategy.GREEDY
            }
          })
        Button("设置折行类型HIGH_QUALITY").onClick(() => {
          this.controller.updateParagraphStyle({ start: -1, end: -1,
            style: {
              lineBreakStrategy: LineBreakStrategy.HIGH_QUALITY
            }
          })
        Button("设置折行类型BALANCED").onClick(() => {
          this.controller.updateParagraphStyle({ start: -1, end: -1,
            style: {
              lineBreakStrategy: LineBreakStrategy.BALANCED
            }
          })
        Divider()
        Row(){
          Button("获取linebreak属性值").onClick(() => {
            this.spanParagraphs = this.controller.getParagraphs({ start: -1, end: -1 });
            console.info("RichEditor getParagraphs:" + JSON.stringify(this.spanParagraphs));
            this.spanParagraphs.forEach(item => {
              if(typeof(item as RichEditorParagraphResult)['style'] != 'undefined'){
                this.attributeValue = "";
                console.info('lineBreakStrategy:'+ JSON.stringify((item as RichEditorParagraphResult)['style']));
                this.attributeValue += this.lineBreakOptionStr[Number((item as RichEditorParagraphResult)['style'].lineBreakStrategy)];
              }
            })
        }
```

![image](public_sys-resources/zh-cn_image_0000002553205009.webp)

**示例21（属性字符串基本功能）**

从API version 20开始，该示例中[属性字符串](属性字符串.md)通过[RichEditorStyledStringController](#ZH-CN_TOPIC_0000002522080846__richeditorstyledstringcontroller12)中的[setStyledString](#ZH-CN_TOPIC_0000002522080846__setstyledstring12)方法与RichEditor组件绑定。通过[getStyledString](#ZH-CN_TOPIC_0000002522080846__getstyledstring12)接口获取富文本组件显示的属性字符串。

```ets
// xxx.ets
import { LengthMetrics } from '@kit.ArkUI'

@Entry
@Component
struct Index {
  stringLength: number = 0;
  @State selection: string = "";
  @State content: string = "";
  @State range: string = "";
  @State replaceString: string = "";
  @State rangeBefore: string = "";
  @State rangeAfter: string = "";
  richEditorStyledString: MutableStyledString = new MutableStyledString("");
  textStyle: TextStyle = new TextStyle({
    fontWeight: FontWeight.Lighter,
    fontFamily: 'HarmonyOS Sans',
    fontColor: Color.Green,
    fontSize: LengthMetrics.vp(30),
    fontStyle: FontStyle.Normal
  })
  fontStyle1: TextStyle = new TextStyle({ fontColor: Color.Blue });
  fontStyle2: TextStyle = new TextStyle({
    fontWeight: FontWeight.Bolder,
    fontFamily: 'Arial',
    fontColor: Color.Orange,
    fontSize: LengthMetrics.vp(30),
    fontStyle: FontStyle.Italic
  })

  controller1: RichEditorController = new RichEditorController();
  options1: RichEditorOptions = { controller: this.controller1 };
  // 创建属性字符串对象
  mutableStyledString: MutableStyledString = new MutableStyledString("初始属性字符串",
    [{ start: 0, length: 5, styledKey: StyledStringKey.FONT, styledValue: this.fontStyle1 }]);
  styledString: StyledString = new StyledString("插入属性字符串",
    [{ start: 2, length: 4, styledKey: StyledStringKey.FONT, styledValue: this.fontStyle2 }]);
  controller: RichEditorStyledStringController = new RichEditorStyledStringController();
  options: RichEditorStyledStringOptions = {controller: this.controller};
  // 文本内容变化回调
  contentChangedListener: StyledStringChangedListener = {
    onWillChange: (value: StyledStringChangeValue) => {
      this.range = '[ ' + value.range.start + ' , ' + value.range.end + ' ]';
      this.replaceString = value.replacementString.getString();
      return true;
    },
    onDidChange: (rangeBefore, rangeAfter) => {
      this.rangeBefore = '[ ' + rangeBefore.start + ' , ' + rangeBefore.end + ' ]';
      this.rangeAfter = '[ ' + rangeAfter.start + ' , ' + rangeAfter.end + ' ]';
    }

  build() {
    Column({space:6}) {
      Column() {
        Text("选中区信息")
          .fontSize(20)
          .width("100%")
        Text("selection range: " + this.selection).width("100%")
        Text("selection content: " + this.content).width("100%")
      }
      .width("100%")
      .height("10%")

      Column() {
        Text("onWillChange回调信息")
          .fontSize(20)
          .width("100%")
        Text("range: " + this.range).width("100%")
        Text("replacementString: " + this.replaceString).width("100%")
        Text("onWillChange回调信息")
          .fontSize(20)
          .width("100%")
        Text("rangeBefore: " + this.rangeBefore).width("100%")
        Text("rangeAfter: " + this.rangeAfter).width("100%")
      }
      .borderWidth(1)
      .borderColor(Color.Black)
      .width("100%")
      .height("20%")

      RichEditor(this.options)
        .onReady(() => {
          // 注册文本变化回调
          this.controller.onContentChanged(this.contentChangedListener);
          // 设定组件展示的属性字符串
          this.controller.setStyledString(this.mutableStyledString);
        })
        .height("20%")
        .width("100%")

      RichEditor(this.options1)
        .onReady(() => {
        this.controller1.addTextSpan("把这些文字转换成属性字符串");
      })
        .height("10%")
        .width("100%")
        .borderWidth(1)
        .borderColor(Color.Black)

        Row({space:2}) {
          Button("插入图片")
            .stateEffect(true)
            .onClick(() => {
              // $r('app.media.startIcon')需要替换为开发者所需的图像资源文件。
              let imageStyledString = new MutableStyledString(new ImageAttachment({
                resourceValue: $r('app.media.startIcon'),
                size: { width: 50, height: 50 },
                layoutStyle: { borderRadius: LengthMetrics.vp(10) },
                verticalAlign: ImageSpanAlignment.BASELINE,
                objectFit: ImageFit.Contain,
                syncLoad: true
              }));
              // 获取组件展示的属性字符串
              this.richEditorStyledString = this.controller.getStyledString();
              this.richEditorStyledString.appendStyledString(imageStyledString)
              // 使插入图片后的属性字符串展示在组件上
              this.controller.setStyledString(this.richEditorStyledString)
              this.controller.setCaretOffset(this.richEditorStyledString.length)
          })
          Button("插入文本").onClick(() => {
            // 获取组件展示的属性字符串
            this.richEditorStyledString = this.controller.getStyledString();
            this.richEditorStyledString.appendStyledString(this.styledString)
            // 使插入文本后的属性字符串展示在组件上
            this.controller.setStyledString(this.richEditorStyledString)
            this.controller.setCaretOffset(this.richEditorStyledString.length)
          })
          Button("删除选中内容").onClick(() => {
            // 获取选中范围
            let richEditorSelection = this.controller.getSelection();
            let start = richEditorSelection.start ? richEditorSelection.start : 0;
            let end = richEditorSelection.end ? richEditorSelection.end : 0;
            if (start < 0 || end <= start) {
              return;
            }
            // 获取组件展示的属性字符串
            this.richEditorStyledString = this.controller.getStyledString();
            this.richEditorStyledString.removeString(start, end - start)
            // 使删除内容后的属性字符串展示在组件上
            this.controller.setStyledString(this.richEditorStyledString)
          })
        }
        Row({space:2}) {
          Button("获取选中内容").onClick(() => {
            // 获取选中范围
            let richEditorSelection = this.controller.getSelection();
            let start = richEditorSelection.start ? richEditorSelection.start : 0;
            let end = richEditorSelection.end ? richEditorSelection.end : 0;
            // 获取组件展示的属性字符串
            this.richEditorStyledString = this.controller.getStyledString();
            this.selection = '[ ' + start + ' , ' + end + ' ]';
            if (start == end) {
              this.content = "";
            } else {
              this.content = this.richEditorStyledString.subStyledString(start, end - start).getString();
            }
          })
          Button("更新选中样式").onClick(() => {
            // 获取选中范围
            let richEditorSelection = this.controller.getSelection();
            let start = richEditorSelection.start ? richEditorSelection.start : 0;
            let end = richEditorSelection.end ? richEditorSelection.end : 0;
            if (start < 0 || end <= start) {
              return;
            }
            // 获取组件展示的属性字符串
            this.richEditorStyledString = this.controller.getStyledString();
            this.richEditorStyledString.setStyle({
              start: start,
              length: end - start,
              styledKey: StyledStringKey.FONT,
              styledValue: this.textStyle
            })
            // 使变更样式后的属性字符串展示在组件上
            this.controller.setStyledString(this.richEditorStyledString)
          })
        }
        Row({space:2}){
          // 将属性字符串转换成span信息
          Button("调用fromStyledString").onClick(() => {
            this.controller1.addTextSpan("调用fromStyledString：" +JSON.stringify(this.controller1.fromStyledString(this.mutableStyledString)))
          })
          // 将给定范围的组件内容转换成属性字符串
          Button("调用toStyledString").onClick(() => {
            this.controller.setStyledString(this.controller1.toStyledString({start:0,end:13}))
          })
        }
```

![image](public_sys-resources/zh-cn_image_0000002522085056.webp)

**示例22（获取布局信息）**

通过[getLayoutManager](#ZH-CN_TOPIC_0000002522080846__getlayoutmanager12)接口获取布局管理器对象，通过[getLineCount](文本组件公共接口.md#ZH-CN_TOPIC_0000002553200813__getlinecount12)接口获取组件内容或[placeholder](#ZH-CN_TOPIC_0000002522080846__placeholder12)的总行数，通过[getGlyphPositionAtCoordinate](文本组件公共接口.md#ZH-CN_TOPIC_0000002553200813__getglyphpositionatcoordinate12)接口获取较为接近给定坐标的字形的位置信息，通过[getLineMetrics](文本组件公共接口.md#ZH-CN_TOPIC_0000002553200813__getlinemetrics12)接口获取指定行的行信息、文本样式信息、以及字体属性信息。

```ets
@Entry
@Component
export struct Index {
  @State lineCount: string = ""
  @State glyphPositionAtCoordinate: string = ""
  @State lineMetrics: string = ""
  controller: RichEditorController = new RichEditorController();
  @State textStr: string =
    'Hello World! 你好，世界！'

  build() {
    Scroll() {
      Column() {
        Text('RichEditor组件getLayoutManager接口获取相对于组件的布局信息')
          .fontSize(9)
          .fontColor(0xCCCCCC)
          .width('90%')
          .padding(10)
        RichEditor({ controller: this.controller })
          .borderColor(Color.Red)
          .borderWidth(1)
          .onReady(() => {
            this.controller.addTextSpan(this.textStr)
          })
          .onAreaChange(() => {
            let layoutManager = this.controller.getLayoutManager();
            this.lineCount = "LineCount: " + layoutManager.getLineCount();
          })

        Text('LineCount').fontSize(9).fontColor(0xCCCCCC).width('90%').padding(10)
        Text(this.lineCount)

        Text('GlyphPositionAtCoordinate').fontSize(9).fontColor(0xCCCCCC).width('90%').padding(10)
        Button("相对组件坐标[150,50]字形信息")
          .onClick(() => {
            let layoutManager: LayoutManager = this.controller.getLayoutManager();
            let position = layoutManager.getGlyphPositionAtCoordinate(150, 50);
            this.glyphPositionAtCoordinate =
            "相对组件坐标[150,50] glyphPositionAtCoordinate position: " + position.position + " affinity: " +
            position.affinity;
          })
          .margin({ bottom: 20, top: 10 })
        Text(this.glyphPositionAtCoordinate)

        Text('LineMetrics').fontSize(9).fontColor(0xCCCCCC).width('90%').padding(10)
        Button("首行行信息、文本样式信息、以及字体属性信息")
          .onClick(() => {
            let layoutManager: LayoutManager = this.controller.getLayoutManager();
            let lineMetrics = layoutManager.getLineMetrics(0);
            this.lineMetrics = "lineMetrics is " + JSON.stringify(lineMetrics) + '\n\n';
            let runMetrics = lineMetrics.runMetrics;
            runMetrics.forEach((value, key) => {
              this.lineMetrics += "runMetrics key is " + key + " " + JSON.stringify(value) + "\n\n";
            });
          })
          .margin({ bottom: 20, top: 10 })
        Text(this.lineMetrics)
      }
      .margin({ top: 100, left: 8, right: 8 })
    }
```

![image](public_sys-resources/zh-cn_image_0000002553364973.webp)

**示例23（设置系统默认菜单扩展项）**

从API version 20开始，该示例通过[editMenuOptions](#ZH-CN_TOPIC_0000002522080846__editmenuoptions12)属性设置系统默认菜单的扩展项，允许配置扩展项的文本内容、图标和回调方法。

```ets
// xxx.ets
@Entry
@Component
struct RichEditorExample {
  controller: RichEditorController = new RichEditorController();
  options: RichEditorOptions = { controller: this.controller };
  @State endIndex: number | undefined = 0;
  onCreateMenu = (menuItems: Array<TextMenuItem>) => {
    const idsToFilter: TextMenuItemId[] = [
      TextMenuItemId.TRANSLATE,
      TextMenuItemId.SHARE,
      TextMenuItemId.SEARCH,
      TextMenuItemId.AI_WRITER,
      // 从API version 23开始支持TextMenuItemId.autoFill
      TextMenuItemId.autoFill
    ]
    const items = menuItems.filter(item => !idsToFilter.some(id => id.equals(item.id)))
    // $r('app.media.startIcon')需要替换为开发者所需的图像资源文件。
    let item1: TextMenuItem = {
      content: 'create1',
      icon: $r('app.media.startIcon'),
      id: TextMenuItemId.of('create1'),
    };
    let item2: TextMenuItem = {
      content: 'create2',
      id: TextMenuItemId.of('create2'),
      icon: $r('app.media.startIcon'),
    };
    items.push(item1);
    items.unshift(item2);
    return items;
  }
  onMenuItemClick = (menuItem: TextMenuItem, textRange: TextRange) => {
    if (menuItem.id.equals(TextMenuItemId.of("create2"))) {
      console.info("拦截 id: create2 start:" + textRange.start + "; end:" + textRange.end);
      return true;
    }
    if (menuItem.id.equals(TextMenuItemId.of("prepare1"))) {
      console.info("拦截 id: prepare1 start:" + textRange.start + "; end:" + textRange.end);
      return true;
    }
    if (menuItem.id.equals(TextMenuItemId.COPY)) {
      console.info("拦截 COPY start:" + textRange.start + "; end:" + textRange.end);
      return true;
    }
    if (menuItem.id.equals(TextMenuItemId.SELECT_ALL)) {
      console.info("不拦截 SELECT_ALL start:" + textRange.start + "; end:" + textRange.end);
      return false;
    }
    return false;
  }
  // $r('app.media.startIcon')需要替换为开发者所需的图像资源文件。
  onPrepareMenu = (menuItems: Array<TextMenuItem>) => {
    let item1: TextMenuItem = {
      content: 'prepare1_' + this.endIndex,
      icon: $r('app.media.startIcon'),
      id: TextMenuItemId.of('prepare1'),
    };
    menuItems.unshift(item1);
    return menuItems;
  }
  @State editMenuOptions: EditMenuOptions = {
    onCreateMenu: this.onCreateMenu,
    onMenuItemClick: this.onMenuItemClick,
    onPrepareMenu: this.onPrepareMenu
  };

  build() {
    Column() {
      RichEditor(this.options)
        .onReady(() => {
          this.controller.addTextSpan("RichEditor editMenuOptions")
        })
        .editMenuOptions(this.editMenuOptions)
        .onSelectionChange((range: RichEditorRange) => {
          console.info("onSelectionChange, (" + range.start + "," + range.end + ")");
          this.endIndex = range.end
        })
        .height(50)
        .margin({ top: 100 })
        .borderWidth(1)
        .borderColor(Color.Red)
    }
    .width("90%")
    .margin("5%")
  }
```

![image](public_sys-resources/zh-cn_image_0000002522245050.webp)

**示例24（组件部分常用属性）**

从API version 18开始，该示例通过[barState](#ZH-CN_TOPIC_0000002522080846__barstate13)属性设置组件滚动条的显示模式。通过[enableKeyboardOnFocus](#ZH-CN_TOPIC_0000002522080846__enablekeyboardonfocus12)属性设置组件通过点击以外的方式获焦时，是否主动拉起软键盘。通过[enableHapticFeedback](#ZH-CN_TOPIC_0000002522080846__enablehapticfeedback13)属性设置组件是否支持触感反馈。通过[getPreviewText](#ZH-CN_TOPIC_0000002522080846__getpreviewtext12)接口获取组件预上屏信息。通过[stopBackPress](#ZH-CN_TOPIC_0000002522080846__stopbackpress18)属性设置是否阻止返回键向其它组件或应用侧传递。

从API version 21开始，该示例通过[scrollBarColor](#ZH-CN_TOPIC_0000002522080846__scrollbarcolor21)属性设置RichEditor组件滚动条颜色。

```ets
// xxx.ets
import { JSON } from '@kit.ArkTS';
import { ColorMetrics } from '@kit.ArkUI';

@Entry
@Component
struct RichEditor_example {
  controller: RichEditorController = new RichEditorController();
  options: RichEditorOptions = { controller: this.controller };

  controller1: RichEditorController = new RichEditorController();
  options1: RichEditorOptions = { controller: this.controller1 };

  @State e: boolean = true;
  @State bs_num: number = 0;
  @State bs: (BarState | undefined)[] = [BarState.Auto, BarState.On, BarState.Off, undefined];
  @State bs_string: string[] = ["Auto", "On", "Off", "undefined"];

  build() {
    Column({space: 3}) {
      RichEditor(this.options)
        .onReady(() => {
          this.controller.addTextSpan('文本文本文本文本文本文本文本文本文本文本文本文本文本文本文本文本文本文本文本文本文本文本文本文本', {
            style: {
              fontColor: Color.Black,
              fontSize: 20
            }
          });
        })
        .onDidIMEInput((value: TextRange) => {
          this.controller1.addTextSpan("\n" + "触发了onDidIMEInput回调,输入法本次输入内容范围为：(" + value.start + "," + value.end + ")", {
            style: {
              fontColor: Color.Gray,
              fontSize: 10
            }
          });
        })
        .onSelectionChange((value: RichEditorRange) => {
          this.controller1.addTextSpan("\n" + "触发了onSelectionChange回调，起始范围信息为：(" + value.start + "," + value.end + ")", {
            style: {
              fontColor: Color.Gray,
              fontSize: 10
            }
          });
        })
        .width(300)
        .height(100)
        .margin(20)
        .barState(this.bs[this.bs_num])
        .enableKeyboardOnFocus(this.e)
        .enableHapticFeedback(true)
        .stopBackPress(false)
        .scrollBarColor(ColorMetrics.resourceColor("#2787D9"));

      RichEditor(this.options1).width(300)

      Button('设置barState为：' + this.bs_string[this.bs_num])
        .height(30)
        .fontSize(13)
        .onClick(() => {
          this.bs_num++;
          if (this.bs_num > (this.bs.length - 1)) {
            this.bs_num = 0;
          }
        })

      Button('设置enableKeyboardOnFocus为：' + this.e)
        .height(30)
        .fontSize(13)
        .onClick(() => {
          this.e = !this.e;
        })

      Button('获取预上屏信息')
        .height(30)
        .fontSize(13)
        .onClick(() => {
          this.controller1.addTextSpan("\n获取预上屏信息:" + JSON.stringify(this.controller.getPreviewText()))
        })
    }
```

![image](public_sys-resources/zh-cn_image_0000002553205011.webp)

**示例25（获取光标相对组件位置的矩形）**

从API version 18开始，该示例通过RichEditorBaseController的[getCaretRect](#ZH-CN_TOPIC_0000002522080846__getcaretrect18)方法来获取当前光标相对于组件位置的Rect。

```ets
// xxx.ets
@Entry
@Component
struct Index {
  controller: RichEditorController = new RichEditorController();
  options: RichEditorOptions = { controller: this.controller };
  @State caretRect: string = "not found";

  build() {
    Column() {
      Button('get caret rect')
        .onClick(() => {
          let rectCaret = this.controller.getCaretRect();
          if(rectCaret == undefined) {
            this.caretRect = 'undefined';
          } else {
            this.caretRect = 'X: ' + rectCaret.x + '\nY: ' + rectCaret.y
              + '\nWidth: ' + rectCaret.width + '\nHeight: ' + rectCaret.height;
          }
        })
        .fontSize(24)
        .width("60%")
        .height("10%")

      Text(this.caretRect)
        .margin(12)
        .fontSize(24)

      RichEditor(this.options)
        .onReady(() => {
          this.controller.addTextSpan('12345678901234567890', {
            style:
            {
              fontColor: Color.Orange,
              fontSize: 50
            }
          })
        .borderWidth(1)
        .borderColor(Color.Red)
        .width("100%")
        .height("60%")
    }
```

![image](public_sys-resources/zh-cn_image_0000002522085058.webp)

**示例26（设置最大行数和最大字符数）**

从API version 18开始，该示例通过[maxLength](#ZH-CN_TOPIC_0000002522080846__maxlength18)设置可输入的最大字符数，通过[maxLines](#ZH-CN_TOPIC_0000002522080846__maxlines18)设置可输入的最大行数。

```ets
@Entry
@Component
struct RichEditorExample {
  @State text: string = "As the sun begins to set, casting a warm golden hue across the sky," +
    "the world seems to slow down and breathe a sigh of relief. The sky is painted with hues of orange, " +
    " pink, and lavender, creating a breathtaking tapestry that stretches as far as the eye can see." +
    "The air is filled with the sweet scent of blooming flowers, mingling with the earthy aroma of freshly turned soil." +
    "it casts a warm," +
    "golden hue that spreads like liquid amber across the vast expanse of the sky." +
    "The once-blue heavens gradually transform, " +
    "now painted in a breathtaking palette of soft oranges, pinks, " +
    "and purples, each color blending seamlessly into the next. Wisps of clouds, tinged with fiery edges, " +
    "float lazily amidst this celestial canvas," +
    "creating a scene so serene and beautiful that it almost seems to pause time itself." +
    "As the sun begins to set, casting a warm golden hue across the sky," +
    "the world seems to slow down and breathe a sigh of relief. The sky is painted with hues of orange, " +
    " pink, and lavender, creating a breathtaking tapestry that stretches as far as the eye can see." +
    "The air is filled with the sweet scent of blooming flowers, mingling with the earthy aroma of freshly turned soil." +
    "it casts a warm," +
    "golden hue that spreads like liquid amber across the vast expanse of the sky." +
    "The once-blue heavens gradually transform, ";
  @State maxLineList: (number | undefined)[] = [2, 6, undefined];
  @State maxLineIndex: number = 0;
  @State maxLineStringList: (string)[] = ["2", "6", "undefined"];
  richEditorStyledString: MutableStyledString = new MutableStyledString("");
  controller1: RichEditorController = new RichEditorController();
  controller2: TextInputController = new TextInputController();
  controller3: RichEditorController = new RichEditorController();
  controller4: RichEditorStyledStringController = new RichEditorStyledStringController();
  controller: RichEditorController = new RichEditorController();
  option: RichEditorOptions = { controller: this.controller };

  build() {
    Column() {
      Text("当前的maxLength为7 ")
        .margin(10)
        .fontSize(25)
      Row() {
        Button("插入占1字符数的图片")
          .onClick(() => {
            // $r('app.media.startIcon')需要替换为开发者所需的图像资源文件。
            this.controller1.addImageSpan($r('app.media.startIcon'),
              {
                imageStyle:
                {
                  size: ["57px", "57px"]
                }
              })
        Button("插入占2字符数图片")
          .onClick(() => {
            this.controller1.addSymbolSpan($r("sys.symbol.ohos_trash"),
              {
                style:
                {
                  fontSize: 30
                }
              })
          .margin({ left: 20 })
      }

      RichEditor({ controller: this.controller1 })
        .width('95%')
        .margin(10)
        .height(60)
        .maxLength(7)
        .backgroundColor('rgb(240,250,255)')
      Text("当前的maxLine为 " + this.maxLineStringList[this.maxLineIndex]).margin(10)
        .fontSize(25)
      Button("更改maxLines").onClick(() => {
        this.maxLineIndex++;
        if (this.maxLineIndex > this.maxLineList.length - 1) {
          this.maxLineIndex = 0;
        }
      })
      RichEditor({ controller: this.controller3 })
        .onReady(() => {
          this.controller3.addTextSpan(this.text,
            {
              style:
              {
                fontColor: 'rgb(0,74,175)'
              }
            })
        .margin(10)
        .width('95%')
        .maxLines(this.maxLineList[this.maxLineIndex])
        .backgroundColor('rgb(240,250,255)')
    }
```

![image](public_sys-resources/zh-cn_image_0000002553364975.webp)

**示例27（文本设置Url样式）**

从API version 19开始，该示例通过在addTextSpan和UpdateSpanStyle接口中加入[UrlStyle](#ZH-CN_TOPIC_0000002522080846__richeditorurlstyle19)，来实现文本点击时跳转到指定链接的功能。

```ets
// xxx.ets

@Entry
@Component
struct RichEditorExample {
  controller: RichEditorController = new RichEditorController();
  options: RichEditorOptions = { controller: this.controller };

  build() {
    Column() {
      Row() {
        Button("Add Example Url").onClick(() => {
          this.controller.addTextSpan("示例网址", {
            urlStyle: { url: "https://www.example.com" }
          })
        Button("Clear Url").onClick(() => {
          this.controller.updateSpanStyle({
            start: 0,
            textStyle: {},
            urlStyle: { url: "" }
          })
      }

      Row() {
        RichEditor(this.options)
          .height('35%')
          .border({ width: 1, color: Color.Blue })
      }
```

![image](public_sys-resources/zh-cn_image_0000002522245052.webp)

**示例28（开启带样式的撤销还原能力）**

从API version 20开始，该示例对于不使用属性字符串的富文本组件，可以通过配置[undoStyle](#ZH-CN_TOPIC_0000002522080846__undostyle20)属性为UndoStyle.KEEP_STYLE，以支持撤销还原时保留原内容的样式。

```ets
// xxx.ets

@Entry
@Component
struct StyledUndo {
  controller: RichEditorController = new RichEditorController();
  options: RichEditorOptions = { controller: this.controller };
  private start: number = 0;
  private end: number = 0;
  @State undoStyle: UndoStyle = UndoStyle.KEEP_STYLE;
  build() {
    Column() {
        Row({space:2}) {
          Button("插入文本").onClick(() => {
            this.controller.addTextSpan("插入文本",
              {
                style:
                {
                  fontColor: Color.Orange,
                  fontSize: 32
                }
              })
          Button("插入图片").onClick(() => {
            // $r('app.media.startIcon')需要替换为开发者所需的图像资源文件。
            this.controller.addImageSpan($r('app.media.startIcon'),
              {
                imageStyle:
                {
                  size: ["100px", "100px"]
                }
              });
          })
          Button("插入Symbol").onClick(() => {
            this.controller.addSymbolSpan($r("sys.symbol.ohos_trash"),
              {
                style:
                {
                  fontSize: 32
                }
              });
          })
        }
        .borderWidth(1)
        .borderColor(Color.Red)
        .justifyContent(FlexAlign.Center)
        .width("100%")
        .height("10%")
        Row({space:2}) {
          Button("更新选中范围样式").onClick(() => {
            if (this.start < this.end) {
              this.controller.updateSpanStyle({
                start: this.start,
                end: this.end,
                textStyle:
                {
                  fontColor: Color.Red,
                  fontWeight: FontWeight.Bolder
                }
              });
            }
          })
          Button("删除选中范围内容").onClick(() => {
            if (this.start < this.end) {
              this.controller.deleteSpans({
                start: this.start,
                end: this.end
              })
            }
          })
        }
        .borderWidth(1)
        .borderColor(Color.Red)
        .justifyContent(FlexAlign.Center)
        .width("100%")
        .height("10%")
        Row({space:2}) {
          Button("撤销时不还原样式").onClick(() => {
            this.undoStyle = UndoStyle.CLEAR_STYLE;
          })
          Button("撤销时还原样式").onClick(() => {
            this.undoStyle = UndoStyle.KEEP_STYLE;
          })
        }
        .borderWidth(1)
        .borderColor(Color.Red)
        .justifyContent(FlexAlign.Center)
        .width("100%")
        .height("10%")
      }
      Column() {
        RichEditor(this.options)
          .onReady(()=>{
            // $r('app.media.startIcon')需要替换为开发者所需的图像资源文件。
            this.controller.addImageSpan($r('app.media.startIcon'),
            {
              imageStyle:
              {
                size: ["100px", "100px"]
              }
            });
            this.controller.addTextSpan("初始化图文混排内容",
              {
                style:
                {
                  fontColor: Color.Orange,
                  fontSize: 32
                }
              })
            this.controller.addSymbolSpan($r("sys.symbol.ohos_trash"),
              {
                style:
                {
                  fontSize: 32
                }
              });
          })
          .undoStyle(this.undoStyle)
          .onSelect((value: RichEditorSelection) => {
            this.start = value.selection[0];
            this.end = value.selection[1];
          })
          .borderWidth(1)
          .borderColor(Color.Green)
          .width("100%")
          .height("50%")
      }
```

![image](public_sys-resources/zh-cn_image_0000002553205013.webp)

**示例29（文本设置预设段落样式）**

从API version 20开始，该示例通过[setTypingParagraphStyle](#ZH-CN_TOPIC_0000002522080846__settypingparagraphstyle20)接口设置预设段落样式。

```ets
@Entry
@Component
struct RichEditorExample {
  controller: RichEditorController = new RichEditorController()
  options: RichEditorOptions = { controller: this.controller }
  ssController: RichEditorStyledStringController = new RichEditorStyledStringController()
  ssOptions: RichEditorStyledStringOptions = { controller: this.ssController }
  contentChangedListener: StyledStringChangedListener = {
    onWillChange: (value: StyledStringChangeValue) => {
      let range = '[ ' + value.range.start + ' , ' + value.range.end + ' ]';
      let replaceString = value.replacementString.getString();
      console.info('styledString, onWillChange, range=' + range);
      console.info('styledString, onWillChange, replaceString=' + replaceString);
      let styles: Array<SpanStyle> = []
      if (replaceString.length != 0) {
        styles = value.replacementString.getStyles(0, replaceString.length, StyledStringKey.PARAGRAPH_STYLE)
      }
      styles.forEach((style) => {
        let value = style.styledValue
        let paraStyle: ParagraphStyle = value as ParagraphStyle
        if (paraStyle != undefined) {
          console.info('styledString, onWillChange, textAlign=' + JSON.stringify(paraStyle.textAlign)
            + ', textIndent=' + JSON.stringify(paraStyle.textIndent)
            + ', maxLines=' + JSON.stringify(paraStyle.maxLines)
            + ', overflow=' + JSON.stringify(paraStyle.overflow)
            + ', wordBreak=' + JSON.stringify(paraStyle.wordBreak)
            + ', leadingMargin=' + JSON.stringify(paraStyle.leadingMargin)
            + ', paragraphSpacing=' + JSON.stringify(paraStyle.paragraphSpacing)
          );
        }
      })
      return true;
    }

  build() {
    Column() {
      Row() {
        Text('ParaStyle')
        // 设置预设段落样式为居中对齐
        Button('setStyle1').onClick(() => {
          let paragraphStyle: RichEditorParagraphStyle = {
            textAlign: TextAlign.Center
          }
          this.controller.setTypingParagraphStyle(paragraphStyle)
          this.ssController.setTypingParagraphStyle(paragraphStyle)
        })
        // 设置预设段落样式为左对齐、带有缩进
        Button('setStyle2').onClick(() => {
          let paragraphStyle: RichEditorParagraphStyle = {
            textAlign: TextAlign.Start,
            leadingMargin: 80
          }
          this.controller.setTypingParagraphStyle(paragraphStyle)
          this.ssController.setTypingParagraphStyle(paragraphStyle)
        })
        // 清除预设段落样式
        Button('clearParaStyle').onClick(() => {
          this.controller.setTypingParagraphStyle(undefined)
          this.ssController.setTypingParagraphStyle(undefined)
        })
      }

      Row() {
        Column() {
          RichEditor(this.options)
            .height('25%')
            .width('100%')
            .border({ width: 1, color: Color.Blue })
            .onWillChange((value: RichEditorChangeValue) => {
              console.info('controller, onWillChange, rangeBefore=' + JSON.stringify(value.rangeBefore))
              value.replacedSpans.forEach((item: RichEditorTextSpanResult) => {
                console.info('controller, onWillChange, replacedTextSpans=' + JSON.stringify(item))
              })
              return true
            })
          RichEditor(this.ssOptions)
            .height('25%')
            .width('100%')
            .onReady(() => {
              this.ssController.onContentChanged(this.contentChangedListener);
            })
        }
```

**示例30（设置装饰线粗细和多装饰线）**

从API version 20开始，该示例通过[thicknessScale](属性字符串.md#ZH-CN_TOPIC_0000002553360773__decorationstyle)设置装饰线粗细，通过[enableMultiType](属性字符串.md#ZH-CN_TOPIC_0000002553360773__decorationoptions20)设置多装饰线。

```ets
import { LengthMetrics } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  private controller: RichEditorController = new RichEditorController();
  private styledStringController: RichEditorStyledStringController = new RichEditorStyledStringController();

  build() {
    Column({ space: 20 }) {
      RichEditor({ controller: this.controller })
        .onReady(() => {
          // 预置一段文本
          this.controller.addTextSpan('一段预置的文本', {
            style: {
              fontSize: 25,
              decoration: {
                type: TextDecorationType.LineThrough,
                // 设置装饰线粗细比例为2
                thicknessScale: 2
              }
          })

      // 设置富文本多装饰线
      RichEditor({ controller: this.styledStringController })

      Button('追加粗细比例为8的文本')
        .fontSize(20)
        .onClick(() => {
          this.controller.addTextSpan('追加的文本', {
            style: {
              fontSize: 25,
              decoration: {
                type: TextDecorationType.LineThrough,
                // 设置装饰线粗细比例为8
                thicknessScale: 8
              }
          })

      Button('修改全段文本的粗细比例为4')
        .fontSize(20)
        .onClick(() => {
          this.controller.updateSpanStyle({
            start: 0,
            end: 1000, // 下标超过文本长度时，会更新整段文本
            textStyle: {
              decoration: {
                type: TextDecorationType.LineThrough,
                // 设置装饰线粗细比例为4
                thicknessScale: 4
              }
          })

      Button('多装饰线文本')
        .fontSize(20)
        .onClick(() => {
          let mutString: MutableStyledString = new MutableStyledString('设置富文本多装饰线', [
            {
              start: 0,
              length: 9,
              styledKey: StyledStringKey.FONT,
              styledValue: new TextStyle({ fontSize: LengthMetrics.vp(25) })
            },
            {
              start: 0,
              length: 5,
              styledKey: StyledStringKey.DECORATION,
              styledValue: new DecorationStyle(
                {
                  type: TextDecorationType.Underline,
                },
                {
                  // 开启多装饰线
                  enableMultiType: true
                }
              )
            },
            {
              start: 2,
              length: 4,
              styledKey: StyledStringKey.DECORATION,
              styledValue: new DecorationStyle(
                {
                  type: TextDecorationType.LineThrough,
                },
                {
                  // 开启多装饰线
                  enableMultiType: true
                }
              )
            },
            {
              start: 4,
              length: 5,
              styledKey: StyledStringKey.DECORATION,
              styledValue: new DecorationStyle(
                {
                  type: TextDecorationType.Overline,
                },
                {
                  // 开启多装饰线
                  enableMultiType: true
                }
              )
            },
          ])
          this.styledStringController.setStyledString(mutString);
        })
    }
    .height('100%')
    .width('100%')
    .justifyContent(FlexAlign.Center)
    .alignItems(HorizontalAlign.Center)
  }
```

![image](public_sys-resources/zh-cn_image_0000002522085060.webp)

**示例31（设置开启中西文自动间距）**

从API version 20开始，该示例通过[enableAutoSpacing](#ZH-CN_TOPIC_0000002522080846__enableautospacing20)属性设置中西文自动间距。

```ets
@Entry
@Component
struct AutoSpacing {
  controller: RichEditorController = new RichEditorController();
  options: RichEditorOptions = { controller: this.controller };
  @State enableAutoSpace: boolean = false;

  build() {
    Column() {
        Row({ space: 2 }) {
          Button("插入中西文内容").onClick(() => {
            this.controller.addTextSpan("Add文本Span",
              {
                style:
                {
                  fontColor: Color.Orange,
                  fontSize: 20
                }
              })
          Button("插入图片").onClick(() => {
            // $r('app.media.startIcon')需要替换为开发者所需的图像资源文件。
            this.controller.addImageSpan($r('app.media.startIcon'),
              {
                imageStyle:
                {
                  size: ["100px", "100px"]
                }
              });
          })
          Button("插入Symbol").onClick(() => {
            this.controller.addSymbolSpan($r("sys.symbol.ohos_trash"),
              {
                style:
                {
                  fontSize: 32
                }
              });
          })
        }
        .borderWidth(1)
        .borderColor(Color.Red)
        .justifyContent(FlexAlign.Center)
        .width("100%")
        .height("10%")

        Row({ space: 2 }) {
          Button("开启中西文自动间距").onClick(() => {
            this.enableAutoSpace = true;
          })
          Button("关闭中西文自动间距").onClick(() => {
            this.enableAutoSpace = false;
          })
        }
        .borderWidth(1)
        .borderColor(Color.Red)
        .justifyContent(FlexAlign.Center)
        .width("100%")
        .height("10%")
      }

      Column() {
        RichEditor(this.options)
          .onReady(() => {
            // $r('app.media.startIcon')需要替换为开发者所需的图像资源文件。
            this.controller.addImageSpan($r('app.media.startIcon'),
              {
                imageStyle:
                {
                  size: ["100px", "100px"]
                }
              });
            this.controller.addTextSpan("中西文Auto Spacing自动间距",
              {
                style:
                {
                  fontColor: Color.Orange,
                  fontSize: 20
                }
              })
            this.controller.addSymbolSpan($r("sys.symbol.ohos_trash"),
              {
                style:
                {
                  fontSize: 20
                }
              });
          })
          .enableAutoSpacing(this.enableAutoSpace)
          .borderWidth(1)
          .borderColor(Color.Green)
          .width("100%")
          .height("50%")
      }
```

![image](public_sys-resources/zh-cn_image_0000002553364977.webp)

**示例32（设置文本选择的AI菜单）**

从API version 22开始，该示例通过[enableSelectedDataDetector](#ZH-CN_TOPIC_0000002522080846__enableselecteddatadetector22)，配置文本选择AI菜单功能。

```ets
@Entry
@Component
struct Demo32 {
  controller: RichEditorController = new RichEditorController();
  textSpanOptions: RichEditorTextSpanOptions = { style: { fontSize: 20 } };
  exampleText: string = '示例网址：www.example.com';

  build() {
    Column() {
      Row() {
        RichEditor({ controller: this.controller })
          .onReady(() => {
            this.controller.addTextSpan(this.exampleText, this.textSpanOptions)
          })
          .copyOptions(CopyOptions.LocalDevice)
          .enableSelectedDataDetector(true)
          .border({ width: 1, color: Color.Black })
          .height(300)
          .margin(10)
      }
```

![image](public_sys-resources/zh-cn_image_0000002522245054.webp)

**示例33（设置监听输入法绑定事件）**

从API version 22开始，该示例通过[onWillAttachIME](#ZH-CN_TOPIC_0000002522080846__onwillattachime22)事件监听输入法绑定事件。

```ets
@Entry
@Component
struct SetOnWillAttachIME {
  controller: RichEditorController = new RichEditorController();
  options: RichEditorOptions = { controller: this.controller };
  @State message: string = "RichEditor未绑定输入法"

  build() {
    Column() {
     Text(this.message)
       .fontSize(24)
       .width("100%")
       .textAlign(TextAlign.Center)
      RichEditor(this.options)
        .onReady(() => {
          this.controller.addTextSpan("RichEditor组件",
            {
              style:
              {
                fontColor: Color.Orange,
                fontSize: 30
              }
            })
        .onWillAttachIME((value:IMEClient) => {
          // 给输入法传递自定义消息
          const inputConfig: InputMethodExtraConfig = {
            customSettings: {
              component: 'RichEditor',
              id: 8 as number,
              isEnable: true
            }
          };
          value.setExtraConfig(inputConfig);
          this.message = "RichEditor已绑定输入法"
        })
        .borderWidth(1)
        .borderColor(Color.Green)
        .width("100%")
        .height("20%")
    }
    .height("100%")
    .justifyContent(FlexAlign.Center)
  }
```

![image](public_sys-resources/zh-cn_image_0000002553205015.webp)

**示例34（删除输入框文本尾部字符）**

从API version 23开始，该示例通过[deleteBackward](#ZH-CN_TOPIC_0000002522080846__deletebackward23)事件在编辑态用自定义键盘删除光标前字符。

```ets
@Entry
@Component
struct RichEditorExample {
  controller: RichEditorController = new RichEditorController();

  // 自定义键盘删除键
  @Builder
  CustomKeyboardBuilder() {
    Column() {
      Button('DELETE')
        .width(200)
        .height(60)
        .backgroundColor(Color.Blue)
        .fontColor(Color.White)
        .fontSize(16)
        .onClick(() => {
          // 调用deleteBackward接口删除字符
          this.controller.deleteBackward()
        })
    }
    .padding(10)
    .backgroundColor(Color.Gray)
  }

  build() {
    Column() {
      Blank()
        .height(400)
      RichEditor({ controller: this.controller })
        .customKeyboard(this.CustomKeyboardBuilder())
        .margin(10)
        .border({ width: 1 })
        .height(150)
        .borderWidth(1)
        .borderColor(Color.Blue)
        .width("100%")
        .onReady(() => {
          // 设置初始文本用于测试
          this.controller.addTextSpan('点击DELETE键测试删除功能', {
            style: {
              fontColor: Color.Black,
              fontSize: 16
            }
          })
    }.margin(90)
  }
```

![image](public_sys-resources/zh-cn_image_0000002522085062.webp)

**示例35（优化小语种文字显示）**

该示例通过[includeFontPadding](#ZH-CN_TOPIC_0000002522080846__includefontpadding23)属性，在首行文字顶部和尾行文字底部添加文字内边距，同时通过[fallbackLineSpacing](#ZH-CN_TOPIC_0000002522080846__fallbacklinespacing23)属性实现行高自适应，基于文字实际高度动态调整。

从API version 23开始，新增includeFontPadding、fallbackLineSpacing属性。

```ets
@Entry
@Component
struct RichEditorExample {
  controller: RichEditorController = new RichEditorController();
  @State fallbackLineSpacing: boolean = true;
  @State includeFontPadding: boolean = true;

  build() {
    Column() {
      RichEditor({ controller: this.controller })
        .onReady(() => {
          this.controller.addTextSpan('བོད་ཀྱི་སྐད་ཡིག་ནི་བོད་མིའི་རྒྱུན་ལྡན་པའི་སྐད་ཡིག་དང་།\n འཇིག་རྟེན་གྱི་ཆོས་ལུགས་དང་རྒྱུན་ལྡན་པའི་ཆོས་ལུགས་ཀྱི་དོན་ཚན་གྱི་སྐད་ཡིག་རེད།\n',
            {
              style: {
                fontColor: Color.Black,
                fontSize: "30",
                lineHeight: 10
              },
              paragraphStyle: {
                textAlign: TextAlign.Start,
              }
            })
          this.controller.addTextSpan('བོད་ཀྱི་སྐད་ཡིག་ནི་བོད་མིའི་རྒྱུན་ལྡན་པའི་སྐད་ཡིག་དང་།\n འཇིག་རྟེན་གྱི་ཆོས་ལུགས་དང་རྒྱུན་ལྡན་པའི་ཆོས་ལུགས་ཀྱི་དོན་ཚན་གྱི་སྐད་ཡིག་རེད།',
            {
              style: {
                fontColor: Color.Black,
                fontSize: "30",
              },
              paragraphStyle: {
                textAlign: TextAlign.Start,
              }
            })
        .width("100%")
        .height("35%")
        .border({ width: 1, radius: 5 })
        .draggable(false)
        .includeFontPadding(this.includeFontPadding)
        .fallbackLineSpacing(this.fallbackLineSpacing)
      Row() {
        Button('开启文字行间自适应')
          .onClick(() => {
            this.fallbackLineSpacing = true
          })
          .width("45%")
          .height("10%")
          .margin({ right: 10 })
        Button('关闭文字行间自适应')
          .onClick(() => {
            this.fallbackLineSpacing = false
          })
          .width("45%")
          .height("10%")
          .margin({ left: 5 })
      }
      .margin({ top: 20 })

      Row() {
        Button('开启段落首行尾行边距增高')
          .onClick(() => {
            this.includeFontPadding = true
          })
          .width("45%")
          .height("10%")
          .margin({ right: 10 })
        Button('关闭段落首行尾行边距增高')
          .onClick(() => {
            this.includeFontPadding = false
          })
          .width("45%")
          .height("10%")
          .margin({ left: 5 })
      }
      .margin({ top: 20 })
    }
```

![image](public_sys-resources/zh-cn_image_0000002553364979.webp)

**示例36（设置开启行首标点符号压缩）**

该示例通过[compressLeadingPunctuation](#ZH-CN_TOPIC_0000002522080846__compressleadingpunctuation23)属性设置行首标点符号压缩。

从API version 23开始，新增compressLeadingPunctuation属性。

```ets
@Entry
@Component
struct CompressLeadingPunctuationDemo {
  controller: RichEditorController = new RichEditorController();
  options: RichEditorOptions = { controller: this.controller };

  @State compressLeadingPunctuation: boolean = false;
  @State text: string = '「0123456789\n『0123456789\n（0123456789\n《0123456789\n〈0123456789\n【0123456789\n〖0123456789\n〔0123456789\n［0123456789\n｛0123456789';

  build() {
    Column() {
      RichEditor(this.options)
        .onReady(() => {
          this.controller.addTextSpan(this.text)
        })
        .compressLeadingPunctuation(this.compressLeadingPunctuation)
        .borderWidth(1)
        .borderColor(Color.Green)
        .align(Alignment.Center)
        .height("30%")
        .width("50%")

      Column() {
        Button("开启行首标点符号压缩").onClick(() => {
          this.compressLeadingPunctuation = true
        }).margin({ top: 10 })
        Button("关闭行首标点符号压缩").onClick(() => {
          this.compressLeadingPunctuation = false
        }).margin({ top: 10 })
      }
    }.width("100%").padding(20)
  }
```

![image](public_sys-resources/zh-cn_image_0000002522245056.webp)

**示例37（设置拖动预览样式）**

该示例通过[selectedDragPreviewStyle](#ZH-CN_TOPIC_0000002522080846__selecteddragpreviewstyle23)接口设置拖动预览样式。

从API version 23开始，新增selectedDragPreviewStyle接口。

```ets
@Entry
@Component
struct RichEditorDemo {
  controller: RichEditorController = new RichEditorController();
  options: RichEditorOptions = { controller: this.controller };

  build() {
    Column({ space: 2 }) {
      RichEditor(this.options)
        .onReady(() => {
          this.controller.addTextSpan('RichEditor selectedDragPreviewStyle')
        })
        .borderWidth(1)
        .borderColor(Color.Green)
        .draggable(true)
        .selectedDragPreviewStyle({ color: Color.Gray })
        .width('100%')
        .height('20%')
    }
```

![image](public_sys-resources/zh-cn_image_0000002553205017.webp)

**示例38（设置单行模式）**

该示例通过[singleLine](#ZH-CN_TOPIC_0000002522080846__singleline23)接口设置单行模式。

从API version 23开始，新增singleLine接口。

```ets
@Entry
@Component
struct SingleLineDemo {
  controller: RichEditorController = new RichEditorController();
  textSpanOptions: RichEditorTextSpanOptions = { style: { fontSize: 30 } };
  exampleText: string = '这是一段示例文本\n这是一段示例文本\n这是一段示例文本';
  @State enableSingleLine: boolean = false;

  build() {
    Column() {
      Row() {
        RichEditor({ controller: this.controller })
          .onReady(() => {
            this.controller.addTextSpan(this.exampleText, this.textSpanOptions)
          })
          .singleLine(this.enableSingleLine)
          .border({ width: 1, color: Color.Black })
          .margin(10)
      }
      Row() {
        Button('切换单行模式').onClick((event: ClickEvent) => {
          this.enableSingleLine = true
        }).margin(5)
        Button('切换多行模式').onClick((event: ClickEvent) => {
          this.enableSingleLine = false
        }).margin(5)
      }
```

![image](public_sys-resources/zh-cn_image_0000002522085064.webp)