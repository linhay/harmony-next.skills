# 选择器（Picker）公共接口

选择器组件公共接口。

 从API version 10开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

#### PickerTextStyle对象说明

选择器组件的文本样式。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明color[ResourceColor](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否是文本颜色。font[Font](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__font)否是文本样式。

#### PickerDialogButtonStyle12+对象说明

选择器弹窗的按钮样式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明type[ButtonType](Button.md#ZH-CN_TOPIC_0000002497604884__buttontype枚举说明)否是按钮显示样式。style[ButtonStyleMode](Button.md#ZH-CN_TOPIC_0000002497604884__buttonstylemode11枚举说明)否是按钮的样式和重要程度。role[ButtonRole](Button.md#ZH-CN_TOPIC_0000002497604884__buttonrole12枚举说明)否是Button组件的角色。fontSize[Length](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__length)否是文本显示字号。fontColor[ResourceColor](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否是文本显示颜色。fontWeight[FontWeight](枚举说明.md#ZH-CN_TOPIC_0000002529284967__fontweight) | number | string否是文本的字体粗细。number类型取值[100, 900]，取值间隔为100，取值越大，字体越粗。string类型仅支持number类型取值的字符串形式，例如"200"，以及"bold"、"bolder"、"lighter"、"regular"、"medium"，分别对应FontWeight中相应的枚举值。fontStyle[FontStyle](枚举说明.md#ZH-CN_TOPIC_0000002529284967__fontstyle)否是文本的字体样式。fontFamily[Resource](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resource) | string否是字体列表。默认字体'HarmonyOS Sans'，当前支持'HarmonyOS Sans'字体和[注册自定义字体](@ohos.font (注册自定义字体).md)。backgroundColor[ResourceColor](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否是按钮背景色。borderRadius[Length](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__length) | [BorderRadiuses](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__borderradiuses9)否是圆角半径。primaryboolean否是

弹出弹窗后，未使用Tab键切换焦点时，Enter键是否默认由该按钮响应。

true：弹出弹窗后，未使用Tab键切换焦点时，按下Enter键会触发该按钮绑定的事件。

false：弹出弹窗后，未使用Tab键切换焦点时，按下Enter键不会触发该按钮绑定的事件。

默认值：false

#### DateRange19+对象说明

日期区间，用于描述起止日期区间。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明startDate否是设置日期区间的开始日期。endDate否是设置日期区间的结束日期。