# @ohos.arkui.theme(主题换肤)

支持自定义主题风格，实现App组件风格跟随Theme切换。

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { Theme, ThemeControl, CustomColors, Colors, CustomTheme, CustomDarkColors } from '@kit.ArkUI';
```

#### Theme

当前生效的主题风格对象，可从[onWillApplyTheme](自定义组件的生命周期.md#ZH-CN_TOPIC_0000002553200861__onwillapplytheme12)中获取。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| colors | Colors | 否 | 否 | 主题颜色资源。 |

#### Colors

主题颜色资源。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full


颜色对应的组件可参考[文本色与图标色](https://developer.huawei.com/consumer/cn/doc/design-guides/color-0000001776857164#section137153164914)。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| brand | [ResourceColor](../../topics/components/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor) | 否 | 否 | 品牌色。 影响组件： [TextInput](../../topics/components/[Text](../../topics/components/Text.md)Input.md)、[Search](../../topics/components/search.md) |
| warning | [ResourceColor](../../topics/components/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor) | 否 | 否 | 一级警示色。 影响组件： TipsDialog、AlertDialog、CustomContentDialog、 [Badge](../../topics/components/badge.md)、[Button](../../topics/components/Button.md) |
| alert | [ResourceColor](../../topics/components/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor) | 否 | 否 | 二级提示色。 影响组件： 暂无组件使用。 |
| confirm | [ResourceColor](../../topics/components/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor) | 否 | 否 | 确认色。 影响组件： 暂无组件使用。 |
| fontPrimary | [ResourceColor](../../topics/components/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor) | 否 | 否 | 一级文本字体颜色。 影响组件： [EditableTitleBar](../../topics/components/EditableTitleBar.md)、LoadingDialog、TipsDialog、 ConfirmDialog、AlertDialog、[Select](../../topics/misc/Select.md)Dialog、 CustomContentDialog、[Swiper](../../topics/misc/swiper.md)、Text、 [SubHeader](../../topics/components/SubHeader.md)、[ProgressButton](../../topics/components/[Progress](../../topics/components/progress.md)Button.md)、[AlphabetIndexer](../../topics/components/AlphabetIndexer.md)、 [Popup](../../topics/misc/popup.md)、Select、[Chip](../../topics/components/Chip.md)、 [ToolBar](../../topics/components/toolbar.md)、[Menu](../../topics/components/menu.md)、TextInput、 Search、[Counter](../../topics/components/Counter.md)、[TimePicker](../../topics/components/TimePicker.md)、[DatePicker](../../topics/components/DatePicker.md)、 [TextPicker](../../topics/components/TextPicker.md)、[ComposeListItem](../../topics/components/ComposeListItem.md)、[TreeView](../../topics/components/TreeView.md) |
| fontSecondary | [ResourceColor](../../topics/components/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor) | 否 | 否 | 二级文本字体颜色。 影响组件： EditableTitleBar、AlertDialog、CustomContentDialog、 SubHeader、AlphabetIndexer、Popup、 TextInput、Search、ComposeListItem、 TreeView |
| fontTertiary | [ResourceColor](../../topics/components/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor) | 否 | 否 | 三级文本字体颜色。 影响组件： ComposeListItem |
| fontFourth | [ResourceColor](../../topics/components/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor) | 否 | 否 | 四级文本字体颜色。 影响组件： 暂无组件使用。 |
| fontEmphasize | [ResourceColor](../../topics/components/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor) | 否 | 否 | 高亮字体颜色。 影响组件： TipsDialog、ConfirmDialog、AlertDialog、 SelectDialog、CustomContentDialog、SubHeader、 AlphabetIndexer、Popup、Button、 Select、ToolBar、Search、 TimePicker、DatePicker、TextPicker |
| fontOnPrimary | [ResourceColor](../../topics/components/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor) | 否 | 否 | 一级文本反转颜色，用于彩色背景。 影响组件： Badge、Button、Chip |
| fontOnSecondary | [ResourceColor](../../topics/components/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor) | 否 | 否 | 二级文本反转颜色，用于彩色背景。 影响组件： 暂无组件使用。 |
| fontOnTertiary | [ResourceColor](../../topics/components/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor) | 否 | 否 | 三级文本反转颜色，用于彩色背景。 影响组件： 暂无组件使用。 |
| fontOnFourth | [ResourceColor](../../topics/components/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor) | 否 | 否 | 四级文本反转颜色，用于彩色背景。 影响组件： 暂无组件使用。 |
| iconPrimary | [ResourceColor](../../topics/components/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor) | 否 | 否 | 一级图标颜色。 影响组件： EditableTitleBar、Swiper、ToolBar、 TreeView |
| iconSecondary | [ResourceColor](../../topics/components/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor) | 否 | 否 | 二级图标颜色。 影响组件： LoadingDialog、SubHeader、[LoadingProgress](../../topics/components/LoadingProgress.md)、 Popup、Chip、Search、 TreeView |
| iconTertiary | [ResourceColor](../../topics/components/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor) | 否 | 否 | 三级图标颜色。 影响组件： SubHeader |
| iconFourth | [ResourceColor](../../topics/components/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor) | 否 | 否 | 四级图标颜色。 影响组件： [Checkbox](../../topics/components/Checkbox.md)、[CheckboxGroup](../../topics/components/CheckboxGroup.md)、[Radio](../../topics/components/Radio.md) |
| iconEmphasize | [ResourceColor](../../topics/components/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor) | 否 | 否 | 高亮图标颜色。 影响组件： ToolBar |
| iconSubEmphasize | [ResourceColor](../../topics/components/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor) | 否 | 否 | 高亮辅助图标颜色。 影响组件： 暂无组件使用。 |
| iconOnPrimary | [ResourceColor](../../topics/components/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor) | 否 | 否 | 一级图标反转颜色，用于彩色背景。 影响组件： Checkbox、CheckboxGroup、Radio |
| iconOnSecondary | [ResourceColor](../../topics/components/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor) | 否 | 否 | 二级图标反转颜色，用于彩色背景。 影响组件： Chip |
| iconOnTertiary | [ResourceColor](../../topics/components/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor) | 否 | 否 | 三级图标反转颜色，用于彩色背景。 影响组件： 暂无组件使用。 |
| iconOnFourth | [ResourceColor](../../topics/components/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor) | 否 | 否 | 四级图标反转颜色，用于彩色背景。 影响组件： ProgressButton |
| backgroundPrimary | [ResourceColor](../../topics/components/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor) | 否 | 否 | 一级背景颜色（实色，不透明）。 影响组件： TextInput、[QRCode](../../topics/misc/qrcode.md) |
| backgroundSecondary | [ResourceColor](../../topics/components/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor) | 否 | 否 | 二级背景颜色（实色，不透明）。 影响组件： 暂无组件使用。 |
| backgroundTertiary | [ResourceColor](../../topics/components/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor) | 否 | 否 | 三级背景颜色（实色，不透明）。 影响组件： 暂无组件使用。 |
| backgroundFourth | [ResourceColor](../../topics/components/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor) | 否 | 否 | 四级背景颜色（实色，不透明）。 影响组件： 暂无组件使用。 |
| backgroundEmphasize | [ResourceColor](../../topics/components/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor) | 否 | 否 | 高亮背景颜色（实色，不透明）。 影响组件： Progress、Button、[Slider](../../topics/components/slider.md) |
| compForegroundPrimary | [ResourceColor](../../topics/components/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor) | 否 | 否 | 前背景。 影响组件： QRCode |
| compBackgroundPrimary | [ResourceColor](../../topics/components/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor) | 否 | 否 | 白色背景。 影响组件： 暂无组件使用。 |
| compBackgroundPrimaryTran | [ResourceColor](../../topics/components/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor) | 否 | 否 | 白色透明背景。 影响组件： 暂无组件使用。 |
| compBackgroundPrimaryContrary | [ResourceColor](../../topics/components/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor) | 否 | 否 | 常亮背景。 影响组件： [Toggle](../../topics/misc/toggle.md)、Slider |
| compBackgroundGray | [ResourceColor](../../topics/components/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor) | 否 | 否 | 灰色背景。 影响组件： 暂无组件使用。 |
| compBackgroundSecondary | [ResourceColor](../../topics/components/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor) | 否 | 否 | 二级背景。 影响组件： Swiper、Slider |
| compBackgroundTertiary | [ResourceColor](../../topics/components/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor) | 否 | 否 | 三级背景。 影响组件： EditableTitleBar、Progress、AlphabetIndexer、 Button、Select、Toggle、 Chip、TextInput、Search |
| compBackgroundEmphasize | [ResourceColor](../../topics/components/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor) | 否 | 否 | 高亮背景。 影响组件： Swiper、Toggle、Chip、 Checkbox、CheckboxGroup、Radio |
| compBackgroundNeutral | [ResourceColor](../../topics/components/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor) | 否 | 否 | 黑色中性高亮背景颜色。 影响组件： [PatternLock](../../topics/components/PatternLock.md) |
| compEmphasizeSecondary | [ResourceColor](../../topics/components/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor) | 否 | 否 | 20%高亮背景颜色。 影响组件： Progress、ProgressButton、AlphabetIndexer、 Select、Toggle |
| compEmphasizeTertiary | [ResourceColor](../../topics/components/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor) | 否 | 否 | 10%高亮背景颜色。 影响组件： 暂无组件使用。 |
| comp[Divider](../../topics/misc/divider.md) | [ResourceColor](../../topics/components/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor) | 否 | 否 | 通用分割线颜色。 影响组件： SelectDialog、PatternLock、Divider |
| compCommonContrary | [ResourceColor](../../topics/components/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor) | 否 | 否 | 通用反转颜色。 影响组件： 暂无组件使用。 |
| compBackgroundFocus | [ResourceColor](../../topics/components/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor) | 否 | 否 | 获焦态背景颜色。 影响组件： 暂无组件使用。 |
| compFocusedPrimary | [ResourceColor](../../topics/components/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor) | 否 | 否 | 获焦态一级反转颜色。 影响组件： 暂无组件使用。 |
| compFocusedSecondary | [ResourceColor](../../topics/components/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor) | 否 | 否 | 获焦态二级反转颜色。 影响组件： 暂无组件使用。 |
| compFocusedTertiary | [ResourceColor](../../topics/components/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor) | 否 | 否 | 获焦态三级反转颜色。 影响组件： [Scroll](../../topics/components/Scroll.md) |
| interactiveHover | [ResourceColor](../../topics/components/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor) | 否 | 否 | 通用悬停交互式颜色。 影响组件： EditableTitleBar、Chip、TreeView |
| interactivePressed | [ResourceColor](../../topics/components/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor) | 否 | 否 | 通用按压交互式颜色。 影响组件： EditableTitleBar、Chip、TreeView |
| interactiveFocus | [ResourceColor](../../topics/components/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor) | 否 | 否 | 通用获焦交互式颜色。 影响组件： EditableTitleBar、Chip、TreeView |
| interactiveActive | [ResourceColor](../../topics/components/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor) | 否 | 否 | 通用激活交互式颜色。 影响组件： TreeView |
| interactiveSelect | [ResourceColor](../../topics/components/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor) | 否 | 否 | 通用选择交互式颜色。 影响组件： TreeView |
| interactiveClick | [ResourceColor](../../topics/components/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor) | 否 | 否 | 通用点击交互式颜色。 影响组件： 暂无组件使用。 |

#### CustomTheme

自定义主题风格对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| colors | CustomColors | 否 | 是 | 自定义浅色主题颜色资源。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| darkColors20+ | CustomDarkColors | 否 | 是 | 自定义深色主题颜色资源。 说明：如果未设置darkColors，颜色值将与浅色模式下的colors配置相同，并且不会随着颜色模式的变化而变化，除非该颜色是通过dark目录下的资源进行设置的。 元服务API： 从API version 20开始，该接口支持在元服务中使用。 |

#### CustomColors

type CustomColors = Partial<Colors>

自定义主题颜色资源类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| Partial<Colors> | 自定义主题颜色资源类型。 |

#### CustomDarkColors20+

type CustomDarkColors = Partial<Colors>

自定义深色主题颜色资源类型。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| Partial<Colors> | 自定义深色主题颜色资源类型。 |

#### ThemeControl

ThemeControl将自定义Theme应用于App组件内，实现App组件风格跟随Theme切换。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

#### setDefaultTheme

setDefaultTheme(theme: [CustomTheme](#ZH-CN_TOPIC_0000002553360647__customtheme)): void

将用户自定义Theme设置应用级默认主题，以实现应用风格跟随Theme切换。若在页面中使用此接口设置应用级默认主题，需确保该接口在页面build前执行。若在UIAbility中使用此接口设置应用级默认主题，需确保该接口在onWindowStageCreate阶段里windowStage.[loadContent](Interface (WindowStage).md#ZH-CN_TOPIC_0000002553360677__loadcontent9)接口调用完成的回调函数中执行。详细代码可参考[设置应用内组件自定义主题色](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/theme_skinning#设置应用内组件自定义主题色)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| theme | CustomTheme | 是 | 表示设置的自定义主题风格。 |

**示例**

```ets
import { CustomTheme, CustomColors, ThemeControl } from '@kit.ArkUI';
// 自定义主题颜色
class BlueColors implements CustomColors {
  fontPrimary = "#FF707070";
  backgroundPrimary = "#FF2787D9";
  brand = "#FFEEAAFF"; // 品牌色
}

class PageCustomTheme implements CustomTheme {
  colors?: CustomColors;

  constructor(colors: CustomColors) {
    this.colors = colors;
}
// 创建实例
const BlueColorsTheme = new PageCustomTheme(new BlueColors());
// 在页面build之前执行ThemeControl.setDefaultTheme，设置App默认样式风格为BlueColorsTheme。
ThemeControl.setDefaultTheme(BlueColorsTheme);

@Entry
@Component
struct Index {

  build() {
    Row() {
      Column() {
        // 文本颜色应用fontPrimary
        Text('这是一段文本')
          .fontSize(30)
          .fontWeight(FontWeight.Bold)
          .margin('5%')
        // 二维码背景色应用backgroundPrimary
        QRCode('Hello')
          .width(100)
          .height(100)
        // 输入框光标颜色应用brand
        TextInput({placeholder: 'input your word...'})
          .width('80%')
          .height(40)
          .margin(20)
      }
      .width('100%')
    }
    .height('100%')
  }
```

![image](public_sys-resources/zh-cn_image_0000002522084682.webp)

![image](public_sys-resources/zh-cn_image_0000002553364595.webp)