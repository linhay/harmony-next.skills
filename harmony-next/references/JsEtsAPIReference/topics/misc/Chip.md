# Chip

Chip用于搜索框历史记录、邮件发送列表等场景。

该组件从API Version 11开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

#### 导入模块

```ets
import { Chip, ChipOptions, ChipSize } from '@kit.ArkUI';
```

#### 子组件

无

#### Chip

Chip(options:ChipOptions): void

**装饰器类型：**@Builder

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常， 异常信息中提示接口未定义，在其他设备中可正常调用。

**参数**：

参数名类型必填说明options[ChipOptions](#ZH-CN_TOPIC_0000002529444919__chipoptions)是定义Chip组件的参数。

#### ChipOptions

ChipOptions定义Chip的样式及具体式样参数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

名称类型只读可选说明size[ChipSize](#ZH-CN_TOPIC_0000002529444919__chipsize) | [SizeOptions](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__sizeoptions)否是

Chip尺寸。

默认值：ChipSize.NORMAL

SizeOptions类型参数不支持百分比设置，异常值按默认值处理。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**说明**：[适老化](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkui-support-for-aging-adaptation)在size指定具体宽高时不生效，size设置为{ height: 0, width: 0 }除外。

enabledboolean否是

Chip是否可选中。

默认值：true。

true：操作块可选中；false：操作块不可选中。

值为undefined时，按默认值处理。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

activated12+boolean否是

Chip是否为激活态。

默认值：false。

true：操作块为激活态；false：操作块为非激活态。

值为undefined时，按默认值处理。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

prefixIcon[PrefixIconOptions](#ZH-CN_TOPIC_0000002529444919__prefixiconoptions)否是

前缀图标属性。

默认值：不显示前缀图标。

值为undefined时，按默认值处理。

prefixIcon和prefixSymbol同时设置时，显示prefixSymbol的效果，prefixIcon无效。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

prefixSymbol12+[ChipSymbolGlyphOptions](#ZH-CN_TOPIC_0000002529444919__chipsymbolglyphoptions12)否是

前缀图标属性，symbol类型。

默认值：不显示前缀图标。

值为undefined时，按默认值处理。

prefixIcon和prefixSymbol同时设置时，显示prefixSymbol的效果，prefixIcon无效。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

label[LabelOptions](#ZH-CN_TOPIC_0000002529444919__labeloptions)否否

文本属性。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

suffixIcon[SuffixIconOptions](#ZH-CN_TOPIC_0000002529444919__suffixiconoptions)否是

后缀图标属性。

默认值：不显示后缀图标。

值为undefined时，按默认值处理。

suffixIcon和suffixSymbol同时设置时，显示suffixSymbol的效果，suffixIcon无效。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

suffixSymbol12+[ChipSymbolGlyphOptions](#ZH-CN_TOPIC_0000002529444919__chipsymbolglyphoptions12)否是

后缀图标属性，symbol类型。

默认值：不显示后缀图标。

值为undefined时，按默认值处理。

suffixIcon和suffixSymbol同时设置时，显示suffixSymbol的效果，suffixIcon无效。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

suffixSymbolOptions14+[ChipSuffixSymbolGlyphOptions](#ZH-CN_TOPIC_0000002529444919__chipsuffixsymbolglyphoptions14)否是

symbol类型后缀图标属性的无障碍朗读功能属性。

默认值：不显示后缀图标。

值为undefined时，按默认值处理。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

backgroundColor[ResourceColor](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否是

Chip背景颜色。

默认值：$r('sys.color.ohos_id_color_button_normal')。

值为undefined时，按默认值处理。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

activatedBackgroundColor12+[ResourceColor](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否是

Chip激活时的背景颜色。

默认值：$r('sys.color.ohos_id_color_emphasize')。

值为undefined时，按默认值处理。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

borderRadius[Dimension](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__dimension10)否是

Chip背景圆角半径大小，不支持百分比。

默认值：$r('sys.float.ohos_id_corner_radius_button')。

值为undefined时，按默认值处理。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

allowCloseboolean否是

关闭图标是否显示。

默认值：true

true：删除图标显示；false：删除图标不显示。

值为undefined时，按默认值处理。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

onClose()=>void否是

默认关闭图标点击事件。

值为undefined时，关闭图标点击事件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

onClicked12+Callback<void>否是

Chip点击事件。

值为undefined时，Chip不能被点击。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

direction12+[Direction](../../guides/枚举说明.md#ZH-CN_TOPIC_0000002529284967__direction)否是

布局方向。

默认值：Direction.Auto。

值为undefined时，按默认值处理。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

closeOptions14+[CloseOptions](#ZH-CN_TOPIC_0000002529444919__closeoptions14)否是

默认关闭图标的无障碍朗读功能属性。

值为undefined时，按默认值处理。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

accessibilityDescription14+[ResourceStr](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcestr)否是

Chip组件的无障碍描述。此描述用于向用户详细解释当前组件，开发人员应为组件的这一属性提供较为详尽的文本说明，以协助用户理解即将执行的操作及其可能产生的后果。特别是当这些后果无法仅从组件的属性和无障碍文本中直接获知时。如果组件同时具备文本属性和无障碍说明属性，当组件被选中时，系统将首先播报组件的文本属性，随后播报无障碍说明属性的内容。

默认值：空字符串。

值为undefined时，按默认值处理。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

accessibilityLevel14+string否是

Chip组件无障碍重要性。用于控制后缀图标是否可被无障碍辅助服务所识别。

支持的值为:

"auto"：当前组件会转化为“yes”。

"yes"：当前组件可被无障碍辅助服务所识别。

"no"：当前组件不可被无障碍辅助服务所识别。

"no-hide-descendants"：当前组件及其所有子组件不可被无障碍辅助服务所识别。

默认值："auto"。

值为undefined时，按默认值处理。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

accessibilitySelectedType14+[AccessibilitySelectedType](#ZH-CN_TOPIC_0000002529444919__accessibilityselectedtype14)否是

Chip组件选中态类型。

默认值：当设置了activated属性但未指定accessibilitySelectedType时，默认使用CHECKED类型。当未设置activated属性时，默认使用CLICKED类型。

值为undefined时，按默认值处理。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

1.

当suffixSymbol有传入参数时，suffixIcon和allowClose不生效；当suffixSymbol没有传入参数而suffixIcon有传入参数时，allowClose不生效；当suffixSymbol和suffixIcon都没有传入参数时，allowClose决定是否显示删除图标。

1.

backgroundColor和activatedBackgroundColor赋值为undefined时，显示默认背景颜色；赋值为非法值时，背景颜色透明。

1.

prefixSymbol/suffixSymbol的fontColor默认值为：normalFontColor: [$r('sys.color.ohos_id_color_primary')]、activatedFontColor: [$r('sys.color.ohos_id_color_text_primary_contrary')]。fontColor默认值为16。

1.

prefixIcon的fillColor默认值为：$r('sys.color.ohos_id_color_secondary')，suffixIcon的fillColor默认值为：$r('sys.color.ohos_id_color_primary')。fillColor对颜色的解析与Image组件保持一致。

1.

prefixIcon和suffixIcon的activatedFillColor默认值均为：$r('sys.color.ohos_id_color_text_primary_contrary')。activatedFillColor对颜色的解析与Image组件保持一致。

#### ChipSize

ChipSize是Chip可指定的尺寸类型，如普通型Chip。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

名称值说明NORMAL"NORMAL"normal尺寸操作块。SMALL"SMALL"small尺寸操作块。

#### AccessibilitySelectedType14+

AccessibilitySelectedType是Chip可指定的选中态类型，用于控制无障碍服务如何向用户传达组件的选中状态。不同的选中态类型提供了不同的语义和用户体验。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

名称值说明CLICKED0单击型。组件不向无障碍服务报告任何选中状态，仅作为可单击组件使用。适用于执行某个操作但不保持状态的场景，如普通按钮。CHECKED1复选型。组件通过 [accessibilityChecked](无障碍属性.md#ZH-CN_TOPIC_0000002497444870__accessibilitychecked13) 属性向无障碍服务报告选中状态。适用于多选场景，如标签筛选、属性选择等。SELECTED2单选型。组件通过 [accessibilitySelected](无障碍属性.md#ZH-CN_TOPIC_0000002497444870__accessibilityselected13) 属性向无障碍服务报告选中状态。适用于表示当前选中项的场景，如导航栏标签、单选列表项等。

#### IconCommonOptions

IconCommonOptions定义图标的共通属性。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

名称类型只读可选说明src[ResourceStr](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcestr)否否图标图片或图片地址引用。size[SizeOptions](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__sizeoptions)否是

图标大小，不支持百分比。

默认值：

- 当ChipOptions.size为ChipSize.SMALL时，默认值为：{width: $r('sys.float.chip_small_icon_size'), height: $r('sys.float.chip_small_icon_size')}

- 当ChipOptions.size为ChipSize.NORMAL时，默认值为：{width: $r('sys.float.chip_normal_icon_size'), height: $r('sys.float.chip_normal_icon_size')}

单位：vp

值为undefined时，按默认值处理。

fillColor[ResourceColor](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否是

图标填充颜色。

默认值：$r('sys.color.chip_usually_icon_color')

值为undefined时，按默认值处理。

activatedFillColor12+[ResourceColor](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否是

操作块激活时图标填充颜色。

默认值：$r('sys.color.chip_active_icon_color')

值为undefined时，按默认值处理。

仅在图片格式为SVG时，fillColor和activatedFillColor属性才生效。

#### PrefixIconOptions

PrefixIconOptions定义前缀图标的属性。

继承于[IconCommonOptions](#ZH-CN_TOPIC_0000002529444919__iconcommonoptions)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

#### SuffixIconOptions

SuffixIconOptions定义后缀图标的属性。

继承于[IconCommonOptions](#ZH-CN_TOPIC_0000002529444919__iconcommonoptions)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

名称类型只读可选说明action() => void否是

后缀图标设定事件。

值为undefined时，不设定后缀图标事件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

accessibilityText14+[ResourceStr](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcestr)否是

后缀图标无障碍文本属性。当后缀图标不包含文本属性时，屏幕朗读选中后缀图标时不播报，使用者无法清楚地知道当前是否选中了后缀图标。为了解决此场景，开发人员可为不包含文字信息的后缀图标设置无障碍文本，当屏幕朗读选中后缀图标时播报无障碍文本的内容，帮助屏幕朗读的使用者清楚地知道自己是否选中了后缀图标。

默认值：‘ ’

值为undefined时，按默认值处理。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

accessibilityDescription14+[ResourceStr](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcestr)否是

后缀图标的无障碍描述。此描述用于向用户详细解释后缀图标，开发人员应为后缀图标的这一属性提供较为详尽的文本说明，以协助用户理解即将执行的操作及其可能产生的后果。特别是当这些后果无法仅从后缀图标的属性和无障碍文本中直接获知时。如果后缀图标同时具备文本属性和无障碍说明属性，当后缀图标被选中时，系统将首先播报后缀图标的文本属性，随后播报无障碍说明属性的内容。

默认值：‘ ’

值为undefined时，按默认值处理。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

accessibilityLevel14+string否是

后缀图标的无障碍重要性。用于控制后缀图标是否可被无障碍辅助服务识别。

支持的值为:

"auto"：当前组件存在action时转化为“yes”，不存在action时，转化为“no”。

"yes"：当前组件可被无障碍辅助服务所识别。

"no"：当前组件不可被无障碍辅助服务所识别。

"no-hide-descendants"：当前组件及其所有子组件不可被无障碍辅助服务所识别。

默认值："auto"。

值为undefined时，按默认值处理。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

#### AccessibilityOptions14+

后缀图标的无障碍朗读功能属性。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

名称类型只读可选说明accessibilityText[ResourceStr](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcestr)否是

无障碍文本属性。当组件无文本属性时，屏幕朗读选中此组件不会播报，导致使用者无法清楚了解当前选中的组件。开发人员可为此类组件设置无障碍文本，屏幕朗读时将播报该文本，帮助使用者明确选中了什么组件。

默认值：‘ ’

值为undefined时，按默认值处理。

accessibilityDescription[ResourceStr](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcestr)否是

无障碍描述。此描述用于向用户详细解释当前组件，开发人员应提供详尽的文本说明，以协助用户理解即将执行的操作及其后果。特别是当这些后果无法仅从组件的属性和无障碍文本中直接获知时。如果组件同时具备文本属性和无障碍说明属性，当组件被选中时，系统将首先播报组件的文本属性，随后播报无障碍说明属性的内容。

默认值：‘ ’

值为undefined时，按默认值处理。

accessibilityLevelstring否是

无障碍重要性。用于控制组件是否可被无障碍辅助服务识别。

支持的值为:

"auto"：当前组件会转换为“yes”。

"yes"：当前组件可被无障碍辅助服务所识别。

"no"：当前组件不可被无障碍辅助服务所识别。

"no-hide-descendants"：当前组件及其所有子组件不可被无障碍辅助服务所识别。

默认值："auto"。

值为undefined时，按默认值处理。

#### ChipSuffixSymbolGlyphOptions14+

symbol类型后缀图标属性的无障碍朗读功能属性类型。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

名称类型只读可选说明action[VoidCallback](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__voidcallback12)否是

后缀图标设定事件。

默认值：undefined

normalAccessibility[AccessibilityOptions](#ZH-CN_TOPIC_0000002529444919__accessibilityoptions14)否是

非激活态无障碍朗读功能属性。

默认值：undefined

activatedAccessibility[AccessibilityOptions](#ZH-CN_TOPIC_0000002529444919__accessibilityoptions14)否是

激活态无障碍朗读功能属性。

默认值：undefined

#### ChipSymbolGlyphOptions12+

ChipSymbolGlyphOptions定义前缀图标和后缀图标的属性。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

名称类型只读可选说明normal[SymbolGlyphModifier](动态属性设置.md)否是

非激活时图标设定。

默认值：不显示前缀图标或后缀图标

值为undefined时，按默认值处理。

activated[SymbolGlyphModifier](动态属性设置.md)否是

激活时图标设定。

默认值：不显示前缀图标或后缀图标

值为undefined时，按默认值处理。

不支持使用symbolEffect修改动效类型及effectStrategy设置动效。

#### LabelOptions

LabelOptions定义文本属性。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

名称类型只读可选说明textstring否否文本文字内容。fontSize[Dimension](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__dimension10)否是

文字字号，不支持百分比。

默认值：$r('sys.float.ohos_id_text_size_button2')

值为undefined时，按默认值处理。

fontColor[ResourceColor](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否是

文字颜色。

默认值：$r('sys.color.ohos_id_color_text_primary')

值为undefined时，按默认值处理。

activatedFontColor12+[ResourceColor](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否是

操作块激活时的文字颜色。

默认值：$r('sys.color.ohos_id_color_text_primary_contrary')

值为undefined时，按默认值处理。

fontFamilystring否是

文字字体。

默认值："HarmonyOS Sans"

值为undefined时，按默认值处理。

labelMargin[LabelMarginOptions](#ZH-CN_TOPIC_0000002529444919__labelmarginoptions)否是

文本与左右侧图标之间间距。

默认值：

size为ChipSize.SMALL时，默认值：{ left: 4, right: 4 }

size为ChipSize.NORMAL时，默认值：{ left: 6, right: 6 }

单位：vp

值为undefined时，按默认值处理。

localizedLabelMargin12+[LocalizedLabelMarginOptions](#ZH-CN_TOPIC_0000002529444919__localizedlabelmarginoptions12)否是

本地化文本与左右侧图标之间间距。

默认值：

size为ChipSize.SMALL时，默认值：

{ start: LengthMetrics.resource($r('sys.float.chip_small_text_margin')), end: LengthMetrics.resource($r('sys.float.chip_small_text_margin')) }

size为ChipSize.NORMAL时，默认值：

{ start: LengthMetrics.resource($r('sys.float.chip_normal_text_margin')), end: LengthMetrics.resource($r('sys.float.chip_normal_text_margin')) }

值为undefined时，按默认值处理。

#### CloseOptions14+

默认关闭图标的无障碍朗读功能属性，accessibilityText默认为"删除"。

继承于[AccessibilityOptions](#ZH-CN_TOPIC_0000002529444919__accessibilityoptions14)。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

#### LabelMarginOptions

LabelMarginOptions用于定义文本与左右侧图标之间间距。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

名称类型只读可选说明left[Dimension](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__dimension10)否是

文本与左侧图标之间间距，不支持百分比。

默认值：

size为ChipSize.SMALL时，left默认值：4

size为ChipSize.NORMAL时，left默认值：6

单位：vp

值为undefined时，按默认值处理。

取值范围：[0, +∞)

right[Dimension](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__dimension10)否是

文本与右侧图标之间间距，不支持百分比。

默认值：

size为ChipSize.SMALL时，right默认值：4

size为ChipSize.NORMAL时，right默认值：6

单位：vp

值为undefined时，按默认值处理。

取值范围：[0, +∞)

#### LocalizedLabelMarginOptions12+

LocalizedLabelMarginOptions用于定义本地化文本与左右侧图标之间间距。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

名称类型只读可选说明start[LengthMetrics](../graphics/Graphics.md#ZH-CN_TOPIC_0000002529444761__lengthmetrics12)否是

文本与左侧图标之间间距，不支持百分比。

默认值：

size为ChipSize.SMALL时，start默认值:

LengthMetrics.resource($r('sys.float.chip_small_text_margin'))

size为ChipSize.NORMAL时，start默认值：

LengthMetrics.resource($r('sys.float.chip_normal_text_margin'))

值为undefined时，按默认值处理。

end[LengthMetrics](../graphics/Graphics.md#ZH-CN_TOPIC_0000002529444761__lengthmetrics12)否是

文本与右侧图标之间间距，不支持百分比。

默认值：

size为ChipSize.SMALL时，end默认值：

LengthMetrics.resource($r('sys.float.chip_small_text_margin'))

size为ChipSize.NORMAL时，end默认值:

LengthMetrics.resource($r('sys.float.chip_normal_text_margin'))

值为undefined时，按默认值处理。

#### 示例

#### 示例1（自定义后缀图标）

通过配置suffixIcon实现自定义操作块的后缀图标。

```ets
import { Chip, ChipSize } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  build() {
    Column({ space: 10 }) {
      Chip({
        prefixIcon: {
          // 'app.media.chips'仅作示例，请替换为实际使用图片。
          src: $r('app.media.chips'),
          size: { width: 16, height: 16 },
          fillColor: Color.Red
        },
        label: {
          text: '操作块',
          fontSize: 12,
          fontColor: Color.Blue,
          fontFamily: 'HarmonyOS Sans',
          labelMargin: { left: 20, right: 30 }
        },
        suffixIcon: {
          // 'app.media.close'仅作示例，请替换为实际使用图片。
          src: $r('app.media.close'),
          size: { width: 16, height: 16 },
          fillColor: Color.Red
        },
        size: ChipSize.NORMAL,
        allowClose: false,
        enabled: true,
        backgroundColor: $r('sys.color.ohos_id_color_button_normal'),
        borderRadius: $r('sys.float.ohos_id_corner_radius_button')
      })
    }
  }
}
```

#### 示例2（设置默认后缀图标）

配置allowClose为true，显示后缀移除图标。

```ets
import { Chip, ChipSize } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  build() {
    Column({ space: 10 }) {
      Chip({
        prefixIcon: {
          // 'app.media.chips'仅作示例，请替换为实际使用图片。
          src: $r('app.media.chips'),
          size: { width: 16, height: 16 },
          fillColor: Color.Blue
        },
        label: {
          text: '操作块',
          fontSize: 12,
          fontColor: Color.Blue,
          fontFamily: 'HarmonyOS Sans',
          labelMargin: { left: 20, right: 30 }
        },
        size: ChipSize.NORMAL,
        allowClose: true,
        enabled: true,
        backgroundColor: $r('sys.color.ohos_id_color_button_normal'),
        borderRadius: $r('sys.float.ohos_id_corner_radius_button')
      })
    }
  }
}
```

#### 示例3（不显示后缀图标）

配置allowClose为false，隐藏后缀移除图标。

```ets
import { Chip, ChipSize } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  build() {
    Column({ space: 10 }) {
      Chip({
        prefixIcon: {
          // 'app.media.chips'仅作示例，请替换为实际使用图片。
          src: $r('app.media.chips'),
          size: { width: 16, height: 16 },
          fillColor: Color.Blue
        },
        label: {
          text: '操作块',
          fontSize: 12,
          fontColor: Color.Blue,
          fontFamily: 'HarmonyOS Sans',
          labelMargin: { left: 20, right: 30 }
        },
        size: ChipSize.SMALL,
        allowClose: false,
        enabled: true,
        backgroundColor: $r('sys.color.ohos_id_color_button_normal'),
        borderRadius: $r('sys.float.ohos_id_corner_radius_button'),
        onClose: () => {
          console.info('chip on close');
        }
      })
    }
  }
}
```

#### 示例4（激活态操作块）

该示例通过配置activated实现激活态操作块。

```ets
import { Chip, ChipSize } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State isActivated: boolean = false;

  build() {
    Column({ space: 10 }) {
      Chip({
        prefixIcon: {
          // 'app.media.chips'仅作示例，请替换为实际使用图片。
          src: $r('app.media.chips'),
          size: { width: 16, height: 16 },
          fillColor: Color.Blue,
          activatedFillColor: $r('sys.color.ohos_id_color_text_primary_contrary')
        },
        label: {
          text: '操作块',
          fontSize: 12,
          fontColor: Color.Blue,
          activatedFontColor: $r('sys.color.ohos_id_color_text_primary_contrary'),
          fontFamily: 'HarmonyOS Sans',
          labelMargin: { left: 20, right: 30 }
        },
        size: ChipSize.NORMAL,
        allowClose: true,
        enabled: true,
        activated: this.isActivated,
        backgroundColor: $r('sys.color.ohos_id_color_button_normal'),
        activatedBackgroundColor: $r('sys.color.ohos_id_color_emphasize'),
        borderRadius: $r('sys.float.ohos_id_corner_radius_button'),
        onClose: () => {
          console.info('chip on close');
        },
        onClicked: () => {
          console.info('chip on clicked');
        }
      })

      Button('改变激活状态').onClick(() => {
        this.isActivated = !this.isActivated;
      })
    }
  }
}
```

#### 示例5（设置symbol类型图标）

Chip组件的前缀、后缀图标使用symbol类型资源展示。

```ets
import { Chip, ChipSize, SymbolGlyphModifier } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State isActivated: boolean = false;

  build() {
    Column({ space: 10 }) {
      Chip({
        prefixSymbol: {
          normal: new SymbolGlyphModifier($r('sys.symbol.ohos_star')).fontSize(16).fontColor([Color.Green]),
          activated: new SymbolGlyphModifier($r('sys.symbol.ohos_star')).fontSize(16).fontColor([Color.Red]),
        },
        label: {
          text: '操作块',
          fontSize: 12,
          fontColor: Color.Blue,
          activatedFontColor: $r('sys.color.ohos_id_color_text_primary_contrary'),
          fontFamily: 'HarmonyOS Sans',
          labelMargin: { left: 20, right: 30 },
        },
        size: ChipSize.NORMAL,
        allowClose: true,
        enabled: true,
        activated: this.isActivated,
        backgroundColor: $r('sys.color.ohos_id_color_button_normal'),
        activatedBackgroundColor: $r('sys.color.ohos_id_color_emphasize'),
        borderRadius: $r('sys.float.ohos_id_corner_radius_button'),
        onClose: () => {
          console.info('chip on close');
        },
        onClicked: () => {
          console.info('chip on clicked');
        }
      })

      Button('改变激活状态').onClick(() => {
        this.isActivated = !this.isActivated;
      })
    }
  }
}
```

#### 示例6（设置镜像效果）

配置direction实现Chip布局镜像化展示。

```ets
import { Chip, ChipSize, LengthMetrics } from '@kit.ArkUI';

@Entry
@Component
struct ChipPage {
  build() {
    Column() {
      Chip({
        direction: Direction.Rtl,
        prefixIcon: {
          // 'app.media.chips'仅作示例，请替换为实际使用图片。
          src: $r('app.media.chips'),
          size: { width: 16, height: 16 },
          fillColor: Color.Red,
        },
        label: {
          text: '操作块',
          fontSize: 12,
          fontColor: Color.Blue,
          fontFamily: 'HarmonyOS Sans',
          localizedLabelMargin: { start: LengthMetrics.vp(20), end: LengthMetrics.vp(20) },
        },
        suffixIcon: {
          // 'app.media.close'仅作示例，请替换为实际使用图片。
          src: $r('app.media.close'),
          size: { width: 16, height: 16 },
          fillColor: Color.Red,
        },
        size: ChipSize.NORMAL,
        allowClose: false,
        enabled: true,
        backgroundColor: $r('sys.color.ohos_id_color_button_normal'),
        borderRadius: $r('sys.float.ohos_id_corner_radius_button')
      })
    }.justifyContent(FlexAlign.Center)
    .width('100%')
    .height('100%')
  }
}
```

#### 示例7（Image类型无障碍朗读）

该示例代码实现Chip组件Image类型后缀图标的无障碍朗读功能。

```ets
import { Chip } from '@kit.ArkUI';

@Builder
function DefaultFunction(): void {
}

@Component
struct SectionGroup {
  @Prop
  @Require
  title: ResourceStr;
  @BuilderParam
  @Require
  content: () => void = DefaultFunction;

  build() {
    Column({ space: 4 }) {
      Text(this.title)
        .fontColor('#FF666666')
        .fontSize(12)
      Column({ space: 8 }) {
        this.content()
      }
    }
    .alignItems(HorizontalAlign.Start)
    .width('100%')
  }
}

@Component
struct SectionItem {
  @Prop
  @Require
  title: ResourceStr;
  @BuilderParam
  @Require
  content: () => void = DefaultFunction;

  build() {
    Column({ space: 12 }) {
      Text(this.title)
      this.content()
    }
    .backgroundColor('#FFFFFFFF')
    .borderRadius(12)
    .padding(12)
    .width('100%')
  }
}

@Entry
@Component
struct ChipExample2 {
  @State activated: boolean = false;

  build() {
    NavDestination() {
      Scroll() {
        SectionGroup({ title: '后缀图标播报' }) {
          SectionItem({ title: '自定义播报' }) {
            Chip({
              label: { text: '操作块' },
              suffixIcon: {
                src: $r('sys.media.ohos_ic_public_cut'),
                accessibilityText: '图标',
                accessibilityDescription: '新手提醒',
                action: () => {
                  this.getUIContext().getPromptAction().showToast({
                    message: '后缀图标被点击！'
                  });
                }
              },
              onClicked: () => {
                this.getUIContext().getPromptAction().showToast({
                  message: '操作块被点击！'
                });
              }
            })
          }
        }
      }
    }
  }
}
```

#### 示例8（symbol类型无障碍朗读）

该示例代码实现Chip组件symbol类型后缀图标的无障碍朗读功能。

```ets
import { Chip, SymbolGlyphModifier } from '@kit.ArkUI';

@Builder
function DefaultFunction(): void {
}

@Component
struct SectionGroup {
  @Prop
  @Require
  title: ResourceStr;
  @BuilderParam
  @Require
  content: () => void = DefaultFunction;

  build() {
    Column({ space: 4 }) {
      Text(this.title)
        .fontColor('#FF666666')
        .fontSize(12)
      Column({ space: 8 }) {
        this.content()
      }
    }
    .alignItems(HorizontalAlign.Start)
    .width('100%')
  }
}

@Component
struct SectionItem {
  @Prop
  @Require
  title: ResourceStr;
  @BuilderParam
  @Require
  content: () => void = DefaultFunction;

  build() {
    Column({ space: 12 }) {
      Text(this.title)
      this.content()
    }
    .backgroundColor('#FFFFFFFF')
    .borderRadius(12)
    .padding(12)
    .width('100%')
  }
}

@Entry
@Component
struct ChipExample2 {
  @State activated: boolean = false;

  build() {
    NavDestination() {
      Scroll() {
        SectionGroup({ title: '后缀Symbol播报' }) {
          SectionItem({ title: 'activatedAccessibility' }) {
            Chip({
              label: { text: '操作块' },
              activated: true,
              suffixSymbol: {
                activated: new SymbolGlyphModifier($r('sys.symbol.media_sound'))
                  .fontSize(72),
              },
              suffixSymbolOptions: {
                activatedAccessibility: {
                  accessibilityText: '音乐',
                  accessibilityDescription: '新手提醒'
                },
                action: () => {
                  this.getUIContext().getPromptAction().showToast({
                    message: '后缀Symbol被点击！'
                  });
                }
              },
              onClicked: () => {
                this.getUIContext().getPromptAction().showToast({
                  message: '操作块被点击！'
                });
              }
            })
          }

          SectionItem({ title: 'normalAccessibility' }) {
            Chip({
              label: { text: '操作块' },
              suffixSymbol: {
                normal: new SymbolGlyphModifier($r('sys.symbol.media_sound'))
                  .fontSize(72),
              },
              suffixSymbolOptions: {
                normalAccessibility: {
                  accessibilityText: '音乐',
                  accessibilityDescription: '新手提醒'
                },
                action: () => {
                  this.getUIContext().getPromptAction().showToast({
                    message: '后缀Symbol被点击！'
                  });
                }
              },
              onClicked: () => {
                this.getUIContext().getPromptAction().showToast({
                  message: '操作块被点击！'
                });
              }
            })
          }
        }
      }
    }
    .padding({
      top: 8,
      bottom: 8,
      left: 16,
      right: 16,
    })
  }
}
```

#### 示例9（Chip组件无障碍朗读）

示例展示Chip组件的无障碍属性设置，包括不同的accessibilitySelectedType类型和各种无障碍属性。

```ets
import { AccessibilitySelectedType, Chip, ChipSize } from '@kit.ArkUI';

@Entry
@Component
struct ChipAccessibilityExample {
  @State clickedChipActivated: boolean = false;
  @State checkedChipActivated: boolean = false;
  @State selectedChipActivated: boolean = false;

  build() {
    Column({ space: 20 }) {
      Text('Chip组件无障碍属性示例').fontSize(20).fontWeight(FontWeight.Bold)

      // 点击型Chip - CLICKED类型
      Chip({
        label: { text: '点击型Chip' },
        prefixIcon: {
          src: $r('sys.media.ohos_app_icon'),
          fillColor: Color.Blue
        },
        size: ChipSize.NORMAL,
        accessibilitySelectedType: AccessibilitySelectedType.CLICKED, // 点击型
        accessibilityDescription: '这是一个点击型Chip', // 整体无障碍描述
        accessibilityLevel: 'yes', // 确保可被无障碍服务识别
        closeOptions: {
          accessibilityDescription: '删除此Chip，此操作无法撤销' // 为删除按钮提供详细说明
        },
        activated: this.clickedChipActivated,
        onClicked: () => {
          this.clickedChipActivated = !this.clickedChipActivated;
          this.getUIContext().getPromptAction().showToast({ message: '点击型Chip被点击' });
        },
        onClose: () => {
          this.getUIContext().getPromptAction().showToast({ message: '点击型Chip的关闭按钮被点击' });
        }
      })

      // 复选型Chip - CHECKED类型
      Chip({
        label: { text: '复选型Chip' },
        prefixIcon: {
          src: $r('sys.media.ohos_app_icon'),
          fillColor: Color.Green
        },
        size: ChipSize.NORMAL,
        accessibilitySelectedType: AccessibilitySelectedType.CHECKED, // 复选型
        accessibilityDescription: '这是一个复选型Chip', // 整体无障碍描述
        activated: this.checkedChipActivated,
        onClicked: () => {
          this.checkedChipActivated = !this.checkedChipActivated;
          this.getUIContext().getPromptAction().showToast({
            message: this.checkedChipActivated ? '复选型Chip被选中' : '复选型Chip被取消选中'
          });
        }
      })

      // 单选型Chip - SELECTED类型
      Chip({
        label: { text: '单选型Chip' },
        prefixIcon: {
          src: $r('sys.media.ohos_app_icon'),
          fillColor: Color.Red
        },
        size: ChipSize.NORMAL,
        accessibilitySelectedType: AccessibilitySelectedType.SELECTED, // 单选型
        accessibilityDescription: '这是一个单选型Chip', // 整体无障碍描述
        activated: this.selectedChipActivated,
        onClicked: () => {
          this.selectedChipActivated = !this.selectedChipActivated;
          this.getUIContext().getPromptAction().showToast({
            message: this.selectedChipActivated ? '单选型Chip被选中' : '单选型Chip被取消选中'
          });
        }
      })

      // 无障碍级别设置示例
      Chip({
        label: { text: '无障碍级别为no' },
        size: ChipSize.NORMAL,
        accessibilityLevel: 'no', // 此Chip不能被无障碍服务识别
        closeOptions: {
          accessibilityLevel: 'no'
        },
        backgroundColor: '#CCCCCC',
        onClicked: () => {
          this.getUIContext().getPromptAction().showToast({ message: '此Chip无法被无障碍服务识别' });
        }
      })
    }
    .width('100%')
    .padding(16)
  }
}
```