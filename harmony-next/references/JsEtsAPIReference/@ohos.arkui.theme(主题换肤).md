# @ohos.arkui.theme(主题换肤)

支持自定义主题风格，实现App组件风格跟随Theme切换。

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { Theme, ThemeControl, CustomColors, Colors, CustomTheme, CustomDarkColors } from '@kit.ArkUI';
```

#### Theme

当前生效的主题风格对象，可从[onWillApplyTheme](自定义组件的生命周期.md#ZH-CN_TOPIC_0000002529444913__onwillapplytheme12)中获取。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明colors[Colors](#ZH-CN_TOPIC_0000002529284765__colors)否否主题颜色资源。

#### Colors

主题颜色资源。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

颜色对应的组件可参考[文本色与图标色](https://developer.huawei.com/consumer/cn/doc/design-guides/color-0000001776857164#section137153164914)。

名称类型只读可选说明brand[ResourceColor](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否否

品牌色。

**影响组件：**[TextInput](TextInput.md)、[Search](Search.md)

warning[ResourceColor](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否否

一级警示色。

**影响组件：**[TipsDialog](弹出框 (Dialog).md#ZH-CN_TOPIC_0000002529284929__tipsdialog)、[AlertDialog](弹出框 (Dialog).md#ZH-CN_TOPIC_0000002529284929__alertdialog)、[CustomContentDialog](弹出框 (Dialog).md#ZH-CN_TOPIC_0000002529284929__customcontentdialog12)、

[Badge](Badge.md)、[Button](Button.md)

alert[ResourceColor](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否否

二级提示色。

**影响组件：** 暂无组件使用。

confirm[ResourceColor](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否否

确认色。

**影响组件：** 暂无组件使用。

fontPrimary[ResourceColor](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否否

一级文本字体颜色。

**影响组件：**[EditableTitleBar](EditableTitleBar.md)、[LoadingDialog](弹出框 (Dialog).md#ZH-CN_TOPIC_0000002529284929__loadingdialog)、[TipsDialog](弹出框 (Dialog).md#ZH-CN_TOPIC_0000002529284929__tipsdialog)、

[ConfirmDialog](弹出框 (Dialog).md#ZH-CN_TOPIC_0000002529284929__confirmdialog)、[AlertDialog](弹出框 (Dialog).md#ZH-CN_TOPIC_0000002529284929__alertdialog)、[SelectDialog](弹出框 (Dialog).md#ZH-CN_TOPIC_0000002529284929__selectdialog)、

[CustomContentDialog](弹出框 (Dialog).md#ZH-CN_TOPIC_0000002529284929__customcontentdialog12)、[Swiper](Swiper.md)、[Text](Text.md)、

[SubHeader](SubHeader.md)、[ProgressButton](ProgressButton.md)、[AlphabetIndexer](AlphabetIndexer.md)、

[Popup](Popup.md)、[Select](Select.md)、[Chip](Chip.md)、

[ToolBar](ToolBar.md)、[Menu](Menu.md)、[TextInput](TextInput.md)、

[Search](Search.md)、[Counter](Counter.md)、[TimePicker](TimePicker.md)、[DatePicker](DatePicker.md)、

[TextPicker](TextPicker.md)、[ComposeListItem](ComposeListItem.md)、[TreeView](TreeView.md)

fontSecondary[ResourceColor](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否否

二级文本字体颜色。

**影响组件：**[EditableTitleBar](EditableTitleBar.md)、[AlertDialog](弹出框 (Dialog).md#ZH-CN_TOPIC_0000002529284929__alertdialog)、[CustomContentDialog](弹出框 (Dialog).md#ZH-CN_TOPIC_0000002529284929__customcontentdialog12)、

[SubHeader](SubHeader.md)、[AlphabetIndexer](AlphabetIndexer.md)、[Popup](Popup.md)、

[TextInput](TextInput.md)、[Search](Search.md)、[ComposeListItem](ComposeListItem.md)、

[TreeView](TreeView.md)

fontTertiary[ResourceColor](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否否

三级文本字体颜色。

**影响组件：**[ComposeListItem](ComposeListItem.md)

fontFourth[ResourceColor](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否否

四级文本字体颜色。

**影响组件：** 暂无组件使用。

fontEmphasize[ResourceColor](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否否

高亮字体颜色。

**影响组件：**[TipsDialog](弹出框 (Dialog).md#ZH-CN_TOPIC_0000002529284929__tipsdialog)、[ConfirmDialog](弹出框 (Dialog).md#ZH-CN_TOPIC_0000002529284929__confirmdialog)、[AlertDialog](弹出框 (Dialog).md#ZH-CN_TOPIC_0000002529284929__alertdialog)、

[SelectDialog](弹出框 (Dialog).md#ZH-CN_TOPIC_0000002529284929__selectdialog)、[CustomContentDialog](弹出框 (Dialog).md#ZH-CN_TOPIC_0000002529284929__customcontentdialog12)、[SubHeader](SubHeader.md)、

[AlphabetIndexer](AlphabetIndexer.md)、[Popup](Popup.md)、[Button](Button.md)、

[Select](Select.md)、[ToolBar](ToolBar.md)、[Search](Search.md)、

[TimePicker](TimePicker.md)、[DatePicker](DatePicker.md)、[TextPicker](TextPicker.md)

fontOnPrimary[ResourceColor](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否否

一级文本反转颜色，用于彩色背景。

**影响组件：**[Badge](Badge.md)、[Button](Button.md)、[Chip](Chip.md)

fontOnSecondary[ResourceColor](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否否

二级文本反转颜色，用于彩色背景。

**影响组件：** 暂无组件使用。

fontOnTertiary[ResourceColor](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否否

三级文本反转颜色，用于彩色背景。

**影响组件：** 暂无组件使用。

fontOnFourth[ResourceColor](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否否

四级文本反转颜色，用于彩色背景。

**影响组件：** 暂无组件使用。

iconPrimary[ResourceColor](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否否

一级图标颜色。

**影响组件：**[EditableTitleBar](EditableTitleBar.md)、[Swiper](Swiper.md)、[ToolBar](ToolBar.md)、

[TreeView](TreeView.md)

iconSecondary[ResourceColor](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否否

二级图标颜色。

**影响组件：**[LoadingDialog](弹出框 (Dialog).md#ZH-CN_TOPIC_0000002529284929__loadingdialog)、[SubHeader](SubHeader.md)、[LoadingProgress](LoadingProgress.md)、

[Popup](Popup.md)、[Chip](Chip.md)、[Search](Search.md)、

[TreeView](TreeView.md)

iconTertiary[ResourceColor](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否否

三级图标颜色。

**影响组件：**[SubHeader](SubHeader.md)

iconFourth[ResourceColor](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否否

四级图标颜色。

**影响组件：**[Checkbox](Checkbox.md)、[CheckboxGroup](CheckboxGroup.md)、[Radio](Radio.md)

iconEmphasize[ResourceColor](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否否

高亮图标颜色。

**影响组件：**[ToolBar](ToolBar.md)

iconSubEmphasize[ResourceColor](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否否

高亮辅助图标颜色。

**影响组件：** 暂无组件使用。

iconOnPrimary[ResourceColor](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否否

一级图标反转颜色，用于彩色背景。

**影响组件：**[Checkbox](Checkbox.md)、[CheckboxGroup](CheckboxGroup.md)、[Radio](Radio.md)

iconOnSecondary[ResourceColor](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否否

二级图标反转颜色，用于彩色背景。

**影响组件：**[Chip](Chip.md)

iconOnTertiary[ResourceColor](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否否

三级图标反转颜色，用于彩色背景。

**影响组件：** 暂无组件使用。

iconOnFourth[ResourceColor](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否否

四级图标反转颜色，用于彩色背景。

**影响组件：**[ProgressButton](ProgressButton.md)

backgroundPrimary[ResourceColor](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否否

一级背景颜色（实色，不透明）。

**影响组件：**[TextInput](TextInput.md)、[QRCode](QRCode.md)

backgroundSecondary[ResourceColor](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否否

二级背景颜色（实色，不透明）。

**影响组件：** 暂无组件使用。

backgroundTertiary[ResourceColor](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否否

三级背景颜色（实色，不透明）。

**影响组件：** 暂无组件使用。

backgroundFourth[ResourceColor](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否否

四级背景颜色（实色，不透明）。

**影响组件：** 暂无组件使用。

backgroundEmphasize[ResourceColor](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否否

高亮背景颜色（实色，不透明）。

**影响组件：**[Progress](Progress.md)、[Button](Button.md)、[Slider](Slider.md)

compForegroundPrimary[ResourceColor](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否否

前背景。

**影响组件：**[QRCode](QRCode.md)

compBackgroundPrimary[ResourceColor](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否否

白色背景。

**影响组件：** 暂无组件使用。

compBackgroundPrimaryTran[ResourceColor](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否否

白色透明背景。

**影响组件：** 暂无组件使用。

compBackgroundPrimaryContrary[ResourceColor](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否否

常亮背景。

**影响组件：**[Toggle](Toggle.md)、[Slider](Slider.md)

compBackgroundGray[ResourceColor](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否否

灰色背景。

**影响组件：** 暂无组件使用。

compBackgroundSecondary[ResourceColor](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否否

二级背景。

**影响组件：**[Swiper](Swiper.md)、[Slider](Slider.md)

compBackgroundTertiary[ResourceColor](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否否

三级背景。

**影响组件：**[EditableTitleBar](EditableTitleBar.md)、[Progress](Progress.md)、[AlphabetIndexer](AlphabetIndexer.md)、

[Button](Button.md)、[Select](Select.md)、[Toggle](Toggle.md)、

[Chip](Chip.md)、[TextInput](TextInput.md)、[Search](Search.md)

compBackgroundEmphasize[ResourceColor](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否否

高亮背景。

**影响组件：**[Swiper](Swiper.md)、[Toggle](Toggle.md)、[Chip](Chip.md)、

[Checkbox](Checkbox.md)、[CheckboxGroup](CheckboxGroup.md)、[Radio](Radio.md)

compBackgroundNeutral[ResourceColor](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否否

黑色中性高亮背景颜色。

**影响组件：**[PatternLock](PatternLock.md)

compEmphasizeSecondary[ResourceColor](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否否

20%高亮背景颜色。

**影响组件：**[Progress](Progress.md)、[ProgressButton](ProgressButton.md)、[AlphabetIndexer](AlphabetIndexer.md)、

[Select](Select.md)、[Toggle](Toggle.md)

compEmphasizeTertiary[ResourceColor](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否否

10%高亮背景颜色。

**影响组件：** 暂无组件使用。

compDivider[ResourceColor](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否否

通用分割线颜色。

**影响组件：**[SelectDialog](弹出框 (Dialog).md#ZH-CN_TOPIC_0000002529284929__selectdialog)、[PatternLock](PatternLock.md)、[Divider](Divider.md)

compCommonContrary[ResourceColor](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否否

通用反转颜色。

**影响组件：** 暂无组件使用。

compBackgroundFocus[ResourceColor](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否否

获焦态背景颜色。

**影响组件：** 暂无组件使用。

compFocusedPrimary[ResourceColor](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否否

获焦态一级反转颜色。

**影响组件：** 暂无组件使用。

compFocusedSecondary[ResourceColor](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否否

获焦态二级反转颜色。

**影响组件：** 暂无组件使用。

compFocusedTertiary[ResourceColor](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否否

获焦态三级反转颜色。

**影响组件：**[Scroll](Scroll.md)

interactiveHover[ResourceColor](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否否

通用悬停交互式颜色。

**影响组件：**[EditableTitleBar](EditableTitleBar.md)、[Chip](Chip.md)、[TreeView](TreeView.md)

interactivePressed[ResourceColor](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否否

通用按压交互式颜色。

**影响组件：**[EditableTitleBar](EditableTitleBar.md)、[Chip](Chip.md)、[TreeView](TreeView.md)

interactiveFocus[ResourceColor](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否否

通用获焦交互式颜色。

**影响组件：**[EditableTitleBar](EditableTitleBar.md)、[Chip](Chip.md)、[TreeView](TreeView.md)

interactiveActive[ResourceColor](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否否

通用激活交互式颜色。

**影响组件：**[TreeView](TreeView.md)

interactiveSelect[ResourceColor](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否否

通用选择交互式颜色。

**影响组件：**[TreeView](TreeView.md)

interactiveClick[ResourceColor](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否否

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

将用户自定义Theme设置应用级默认主题，以实现应用风格跟随Theme切换。若在页面中使用此接口设置应用级默认主题，需确保该接口在页面build前执行。若在UIAbility中使用此接口设置应用级默认主题，需确保该接口在onWindowStageCreate阶段里windowStage.[loadContent](Interface (WindowStage).md#ZH-CN_TOPIC_0000002497444824__loadcontent9)接口调用完成的回调函数中执行。详细代码可参考[设置应用内组件自定义主题色](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/theme_skinning#设置应用内组件自定义主题色)。

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