# @ohos.arkui.theme(主题换肤)

支持自定义主题风格，实现App组件风格跟随Theme切换。

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { Theme, ThemeControl, CustomColors, Colors, CustomTheme, CustomDarkColors } from '@kit.ArkUI';
```

#### Theme

当前生效的主题风格对象，可从[onWillApplyTheme](../../topics/misc/自定义组件的生命周期.md#ZH-CN_TOPIC_0000002529444913__onwillapplytheme12)中获取。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明colors[Colors](#ZH-CN_TOPIC_0000002529284765__colors)否否主题颜色资源。

#### Colors

主题颜色资源。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

颜色对应的组件可参考[文本色与图标色](https://developer.huawei.com/consumer/cn/doc/design-guides/color-0000001776857164#section137153164914)。

名称类型只读可选说明brand[ResourceColor](../../topics/misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否否

品牌色。

**影响组件：**[TextInput](../../topics/graphics/TextInput.md)、[Search](../../topics/components/search.md)

warning[ResourceColor](../../topics/misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否否

一级警示色。

**影响组件：**[TipsDialog](../../topics/components/弹出框 (Dialog).md#ZH-CN_TOPIC_0000002529284929__tipsdialog)、[AlertDialog](../../topics/components/弹出框 (Dialog).md#ZH-CN_TOPIC_0000002529284929__alertdialog)、[CustomContentDialog](../../topics/components/弹出框 (Dialog).md#ZH-CN_TOPIC_0000002529284929__customcontentdialog12)、

[Badge](../../topics/components/badge.md)、[Button](../../topics/components/Button.md)

alert[ResourceColor](../../topics/misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否否

二级提示色。

**影响组件：** 暂无组件使用。

confirm[ResourceColor](../../topics/misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否否

确认色。

**影响组件：** 暂无组件使用。

fontPrimary[ResourceColor](../../topics/misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否否

一级文本字体颜色。

**影响组件：**[EditableTitleBar](../../topics/components/EditableTitleBar.md)、[LoadingDialog](../../topics/components/弹出框 (Dialog).md#ZH-CN_TOPIC_0000002529284929__loadingdialog)、[TipsDialog](../../topics/components/弹出框 (Dialog).md#ZH-CN_TOPIC_0000002529284929__tipsdialog)、

[ConfirmDialog](../../topics/components/弹出框 (Dialog).md#ZH-CN_TOPIC_0000002529284929__confirmdialog)、[AlertDialog](../../topics/components/弹出框 (Dialog).md#ZH-CN_TOPIC_0000002529284929__alertdialog)、[SelectDialog](../../topics/components/弹出框 (Dialog).md#ZH-CN_TOPIC_0000002529284929__selectdialog)、

[CustomContentDialog](../../topics/components/弹出框 (Dialog).md#ZH-CN_TOPIC_0000002529284929__customcontentdialog12)、[Swiper](../../topics/misc/swiper.md)、[Text](../../topics/graphics/Text.md)、

[SubHeader](../../topics/misc/SubHeader.md)、[ProgressButton](../../topics/components/ProgressButton.md)、[AlphabetIndexer](../../topics/misc/AlphabetIndexer.md)、

[Popup](../../topics/misc/popup.md)、[Select](../../topics/misc/Select.md)、[Chip](../../topics/misc/Chip.md)、

[ToolBar](../../topics/components/toolbar.md)、[Menu](../../topics/components/menu.md)、[TextInput](../../topics/graphics/TextInput.md)、

[Search](../../topics/components/search.md)、[Counter](../../topics/misc/Counter.md)、[TimePicker](../../topics/components/TimePicker.md)、[DatePicker](../../topics/components/DatePicker.md)、

[TextPicker](../../topics/components/TextPicker.md)、[ComposeListItem](../../topics/components/ComposeListItem.md)、[TreeView](../../topics/misc/TreeView.md)

fontSecondary[ResourceColor](../../topics/misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否否

二级文本字体颜色。

**影响组件：**[EditableTitleBar](../../topics/components/EditableTitleBar.md)、[AlertDialog](../../topics/components/弹出框 (Dialog).md#ZH-CN_TOPIC_0000002529284929__alertdialog)、[CustomContentDialog](../../topics/components/弹出框 (Dialog).md#ZH-CN_TOPIC_0000002529284929__customcontentdialog12)、

[SubHeader](../../topics/misc/SubHeader.md)、[AlphabetIndexer](../../topics/misc/AlphabetIndexer.md)、[Popup](../../topics/misc/popup.md)、

[TextInput](../../topics/graphics/TextInput.md)、[Search](../../topics/components/search.md)、[ComposeListItem](../../topics/components/ComposeListItem.md)、

[TreeView](../../topics/misc/TreeView.md)

fontTertiary[ResourceColor](../../topics/misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否否

三级文本字体颜色。

**影响组件：**[ComposeListItem](../../topics/components/ComposeListItem.md)

fontFourth[ResourceColor](../../topics/misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否否

四级文本字体颜色。

**影响组件：** 暂无组件使用。

fontEmphasize[ResourceColor](../../topics/misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否否

高亮字体颜色。

**影响组件：**[TipsDialog](../../topics/components/弹出框 (Dialog).md#ZH-CN_TOPIC_0000002529284929__tipsdialog)、[ConfirmDialog](../../topics/components/弹出框 (Dialog).md#ZH-CN_TOPIC_0000002529284929__confirmdialog)、[AlertDialog](../../topics/components/弹出框 (Dialog).md#ZH-CN_TOPIC_0000002529284929__alertdialog)、

[SelectDialog](../../topics/components/弹出框 (Dialog).md#ZH-CN_TOPIC_0000002529284929__selectdialog)、[CustomContentDialog](../../topics/components/弹出框 (Dialog).md#ZH-CN_TOPIC_0000002529284929__customcontentdialog12)、[SubHeader](../../topics/misc/SubHeader.md)、

[AlphabetIndexer](../../topics/misc/AlphabetIndexer.md)、[Popup](../../topics/misc/popup.md)、[Button](../../topics/components/Button.md)、

[Select](../../topics/misc/Select.md)、[ToolBar](../../topics/components/toolbar.md)、[Search](../../topics/components/search.md)、

[TimePicker](../../topics/components/TimePicker.md)、[DatePicker](../../topics/components/DatePicker.md)、[TextPicker](../../topics/components/TextPicker.md)

fontOnPrimary[ResourceColor](../../topics/misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否否

一级文本反转颜色，用于彩色背景。

**影响组件：**[Badge](../../topics/components/badge.md)、[Button](../../topics/components/Button.md)、[Chip](../../topics/misc/Chip.md)

fontOnSecondary[ResourceColor](../../topics/misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否否

二级文本反转颜色，用于彩色背景。

**影响组件：** 暂无组件使用。

fontOnTertiary[ResourceColor](../../topics/misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否否

三级文本反转颜色，用于彩色背景。

**影响组件：** 暂无组件使用。

fontOnFourth[ResourceColor](../../topics/misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否否

四级文本反转颜色，用于彩色背景。

**影响组件：** 暂无组件使用。

iconPrimary[ResourceColor](../../topics/misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否否

一级图标颜色。

**影响组件：**[EditableTitleBar](../../topics/components/EditableTitleBar.md)、[Swiper](../../topics/misc/swiper.md)、[ToolBar](../../topics/components/toolbar.md)、

[TreeView](../../topics/misc/TreeView.md)

iconSecondary[ResourceColor](../../topics/misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否否

二级图标颜色。

**影响组件：**[LoadingDialog](../../topics/components/弹出框 (Dialog).md#ZH-CN_TOPIC_0000002529284929__loadingdialog)、[SubHeader](../../topics/misc/SubHeader.md)、[LoadingProgress](../../topics/components/LoadingProgress.md)、

[Popup](../../topics/misc/popup.md)、[Chip](../../topics/misc/Chip.md)、[Search](../../topics/components/search.md)、

[TreeView](../../topics/misc/TreeView.md)

iconTertiary[ResourceColor](../../topics/misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否否

三级图标颜色。

**影响组件：**[SubHeader](../../topics/misc/SubHeader.md)

iconFourth[ResourceColor](../../topics/misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否否

四级图标颜色。

**影响组件：**[Checkbox](../../topics/components/Checkbox.md)、[CheckboxGroup](../../topics/components/CheckboxGroup.md)、[Radio](../../topics/components/Radio.md)

iconEmphasize[ResourceColor](../../topics/misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否否

高亮图标颜色。

**影响组件：**[ToolBar](../../topics/components/toolbar.md)

iconSubEmphasize[ResourceColor](../../topics/misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否否

高亮辅助图标颜色。

**影响组件：** 暂无组件使用。

iconOnPrimary[ResourceColor](../../topics/misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否否

一级图标反转颜色，用于彩色背景。

**影响组件：**[Checkbox](../../topics/components/Checkbox.md)、[CheckboxGroup](../../topics/components/CheckboxGroup.md)、[Radio](../../topics/components/Radio.md)

iconOnSecondary[ResourceColor](../../topics/misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否否

二级图标反转颜色，用于彩色背景。

**影响组件：**[Chip](../../topics/misc/Chip.md)

iconOnTertiary[ResourceColor](../../topics/misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否否

三级图标反转颜色，用于彩色背景。

**影响组件：** 暂无组件使用。

iconOnFourth[ResourceColor](../../topics/misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否否

四级图标反转颜色，用于彩色背景。

**影响组件：**[ProgressButton](../../topics/components/ProgressButton.md)

backgroundPrimary[ResourceColor](../../topics/misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否否

一级背景颜色（实色，不透明）。

**影响组件：**[TextInput](../../topics/graphics/TextInput.md)、[QRCode](../../topics/misc/qrcode.md)

backgroundSecondary[ResourceColor](../../topics/misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否否

二级背景颜色（实色，不透明）。

**影响组件：** 暂无组件使用。

backgroundTertiary[ResourceColor](../../topics/misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否否

三级背景颜色（实色，不透明）。

**影响组件：** 暂无组件使用。

backgroundFourth[ResourceColor](../../topics/misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否否

四级背景颜色（实色，不透明）。

**影响组件：** 暂无组件使用。

backgroundEmphasize[ResourceColor](../../topics/misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否否

高亮背景颜色（实色，不透明）。

**影响组件：**[Progress](../../topics/components/progress.md)、[Button](../../topics/components/Button.md)、[Slider](../../topics/components/slider.md)

compForegroundPrimary[ResourceColor](../../topics/misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否否

前背景。

**影响组件：**[QRCode](../../topics/misc/qrcode.md)

compBackgroundPrimary[ResourceColor](../../topics/misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否否

白色背景。

**影响组件：** 暂无组件使用。

compBackgroundPrimaryTran[ResourceColor](../../topics/misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否否

白色透明背景。

**影响组件：** 暂无组件使用。

compBackgroundPrimaryContrary[ResourceColor](../../topics/misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否否

常亮背景。

**影响组件：**[Toggle](../../topics/misc/toggle.md)、[Slider](../../topics/components/slider.md)

compBackgroundGray[ResourceColor](../../topics/misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否否

灰色背景。

**影响组件：** 暂无组件使用。

compBackgroundSecondary[ResourceColor](../../topics/misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否否

二级背景。

**影响组件：**[Swiper](../../topics/misc/swiper.md)、[Slider](../../topics/components/slider.md)

compBackgroundTertiary[ResourceColor](../../topics/misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否否

三级背景。

**影响组件：**[EditableTitleBar](../../topics/components/EditableTitleBar.md)、[Progress](../../topics/components/progress.md)、[AlphabetIndexer](../../topics/misc/AlphabetIndexer.md)、

[Button](../../topics/components/Button.md)、[Select](../../topics/misc/Select.md)、[Toggle](../../topics/misc/toggle.md)、

[Chip](../../topics/misc/Chip.md)、[TextInput](../../topics/graphics/TextInput.md)、[Search](../../topics/components/search.md)

compBackgroundEmphasize[ResourceColor](../../topics/misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否否

高亮背景。

**影响组件：**[Swiper](../../topics/misc/swiper.md)、[Toggle](../../topics/misc/toggle.md)、[Chip](../../topics/misc/Chip.md)、

[Checkbox](../../topics/components/Checkbox.md)、[CheckboxGroup](../../topics/components/CheckboxGroup.md)、[Radio](../../topics/components/Radio.md)

compBackgroundNeutral[ResourceColor](../../topics/misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否否

黑色中性高亮背景颜色。

**影响组件：**[PatternLock](../../topics/graphics/PatternLock.md)

compEmphasizeSecondary[ResourceColor](../../topics/misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否否

20%高亮背景颜色。

**影响组件：**[Progress](../../topics/components/progress.md)、[ProgressButton](../../topics/components/ProgressButton.md)、[AlphabetIndexer](../../topics/misc/AlphabetIndexer.md)、

[Select](../../topics/misc/Select.md)、[Toggle](../../topics/misc/toggle.md)

compEmphasizeTertiary[ResourceColor](../../topics/misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否否

10%高亮背景颜色。

**影响组件：** 暂无组件使用。

compDivider[ResourceColor](../../topics/misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否否

通用分割线颜色。

**影响组件：**[SelectDialog](../../topics/components/弹出框 (Dialog).md#ZH-CN_TOPIC_0000002529284929__selectdialog)、[PatternLock](../../topics/graphics/PatternLock.md)、[Divider](../../topics/misc/divider.md)

compCommonContrary[ResourceColor](../../topics/misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否否

通用反转颜色。

**影响组件：** 暂无组件使用。

compBackgroundFocus[ResourceColor](../../topics/misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否否

获焦态背景颜色。

**影响组件：** 暂无组件使用。

compFocusedPrimary[ResourceColor](../../topics/misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否否

获焦态一级反转颜色。

**影响组件：** 暂无组件使用。

compFocusedSecondary[ResourceColor](../../topics/misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否否

获焦态二级反转颜色。

**影响组件：** 暂无组件使用。

compFocusedTertiary[ResourceColor](../../topics/misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否否

获焦态三级反转颜色。

**影响组件：**[Scroll](../../topics/components/Scroll.md)

interactiveHover[ResourceColor](../../topics/misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否否

通用悬停交互式颜色。

**影响组件：**[EditableTitleBar](../../topics/components/EditableTitleBar.md)、[Chip](../../topics/misc/Chip.md)、[TreeView](../../topics/misc/TreeView.md)

interactivePressed[ResourceColor](../../topics/misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否否

通用按压交互式颜色。

**影响组件：**[EditableTitleBar](../../topics/components/EditableTitleBar.md)、[Chip](../../topics/misc/Chip.md)、[TreeView](../../topics/misc/TreeView.md)

interactiveFocus[ResourceColor](../../topics/misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否否

通用获焦交互式颜色。

**影响组件：**[EditableTitleBar](../../topics/components/EditableTitleBar.md)、[Chip](../../topics/misc/Chip.md)、[TreeView](../../topics/misc/TreeView.md)

interactiveActive[ResourceColor](../../topics/misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否否

通用激活交互式颜色。

**影响组件：**[TreeView](../../topics/misc/TreeView.md)

interactiveSelect[ResourceColor](../../topics/misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否否

通用选择交互式颜色。

**影响组件：**[TreeView](../../topics/misc/TreeView.md)

interactiveClick[ResourceColor](../../topics/misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否否

通用点击交互式颜色。

**影响组件：** 暂无组件使用。

#### CustomTheme

自定义主题风格对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明colors[CustomColors](#ZH-CN_TOPIC_0000002529284765__customcolors)否是

自定义主题颜色资源。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

darkColors20+[CustomDarkColors](#ZH-CN_TOPIC_0000002529284765__customdarkcolors20)否是

自定义深色主题颜色资源。

**说明**：如果未设置darkColors，颜色值将与浅色模式下的colors配置相同，并且不会随着颜色模式的变化而变化，除非该颜色是通过dark目录下的资源进行设置的。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

#### CustomColors

type CustomColors = Partial<Colors>

自定义主题颜色资源类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

类型说明Partial<[Colors](#ZH-CN_TOPIC_0000002529284765__colors)>自定义主题颜色资源类型。

#### CustomDarkColors20+

type CustomDarkColors = Partial<Colors>

自定义深色主题颜色资源类型。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

类型说明Partial<[Colors](#ZH-CN_TOPIC_0000002529284765__colors)>自定义深色主题颜色资源类型。

#### ThemeControl

ThemeControl将自定义Theme应用于App组件内，实现App组件风格跟随Theme切换。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

#### setDefaultTheme

setDefaultTheme(theme: [CustomTheme](#ZH-CN_TOPIC_0000002529284765__customtheme)): void

将用户自定义Theme设置应用级默认主题，以实现应用风格跟随Theme切换。若在页面中使用此接口设置应用级默认主题，需确保该接口在页面build前执行。若在UIAbility中使用此接口设置应用级默认主题，需确保该接口在onWindowStageCreate阶段里windowStage.[loadContent](../../types/interfaces/Interface (WindowStage).md#ZH-CN_TOPIC_0000002497444824__loadcontent9)接口调用完成的回调函数中执行。详细代码可参考[设置应用内组件自定义主题色](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/theme_skinning#设置应用内组件自定义主题色)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明theme[CustomTheme](#ZH-CN_TOPIC_0000002529284765__customtheme)是表示设置的自定义主题风格。

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
}
```