# HdsActionBar

提供多个按钮操作，如果有主按钮则支持展开和收缩的动效，其内部包含了0或1个主按钮、0或多个非主按钮和背板，其中主按钮可以用户自定义CustomBuilder。

**起始版本：**6.0.0(20)

#### 导入模块

```ets
import { HdsActionBar } from '@kit.UIDesignKit';
```

#### 接口

HdsActionBar({ primaryButton?: ActionBarButton, primaryButtonBuilder?: CustomBuilder, primaryButtonBuilderWidth?: LengthMetrics, startButtons?: Array<ActionBarButton>, endButtons?: Array<ActionBarButton>, actionBarStyle?: ActionBarStyle, isExpand?: boolean, $isExpand?: Callback<boolean>, blurStrategy?: BlurStrategy})

HdsActionBar核心操作组件。

**装饰器类型：**@ComponentV2

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSPattern.Standard

**起始版本：**6.0.0(20)

**参数：**

参数名

类型

必填

装饰器类型

说明

primaryButton

[ActionBarButton](#section1092811431828)

否

@Param

主按钮。

primaryButtonBuilder

[CustomBuilder](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#custombuilder8)

否

@BuilderParam

自定义主按钮。

 说明：

primaryButtonBuilder优先级高于primaryButton。

primaryButtonBuilderWidth

[LengthMetrics](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-graphics#lengthmetrics12)

否

@Param

主按钮是自定义组件时，需要设置主按钮宽度。

startButtons

Array<[ActionBarButton](#section1092811431828)>

否

@Param

HdsActionBar布局起始位置按钮组。

endButtons

Array<[ActionBarButton](#section1092811431828)>

否

@Param

HdsActionBar布局末尾位置按钮组。

actionBarStyle

[ActionBarStyle](#section1511110111610)

否

@Param

HdsActionBar的样式。

isExpand

boolean

否

@Param

HdsActionBar是展开状态还是收起状态，isExpand=true表示展开状态，isExpand=false表示收起状态。

默认值：false。

$isExpand

[Callback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#callback12)<boolean>

否

@Event

HdsActionBar是否展开的回调。

 说明：

回调函数的入参值为true时HdsActionBar是展开状态，为false时HdsActionBar是收起状态。

blurStrategy

[BlurStrategy](HdsNavigation.md#section1086755971212)

否

@Param

HdsActionBar的模糊生效策略。

默认值：BlurStrategy.ADAPTIVE。

#### ActionBarButton

定义HdsActionBar的按钮。

**装饰器类型：**@ObservedV2

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSPattern.Standard

**起始版本：**6.0.0(20)

#### 属性

ActionBarButton的属性。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSPattern.Standard

**起始版本：**6.0.0(20)

**参数：**

名称

类型

只读

可选

装饰器类型

说明

width

[LengthMetrics](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-graphics#lengthmetrics12)

否

是

@Trace

圆形按钮的宽度。

 说明：

支持px,vp,fp,lpx单位，不支持percent。

backgroundColor

[ColorMetrics](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-graphics#colormetrics12)

否

是

@Trace

圆形按钮的背景颜色。

shadowStyle

[ShadowOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-image-effect#shadowoptions对象说明) | [ShadowStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-image-effect#shadowstyle10枚举说明)

否

是

@Trace

圆形按钮的阴影。

默认值：ShadowStyle.OUTER_DEFAULT_LG。

enabled

boolean

否

是

@Trace

圆形按钮是否启用。

默认值：true。

 说明：

enabled为true表示圆形按钮启用，enabled为false表示圆形按钮禁用。

baseIcon

[ResourceStr](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resourcestr)

否

是

@Trace

主按钮的初始状态的图标。

 说明：

如果是非主按钮，baseIcon是非主按钮的图标。

altIcon

[ResourceStr](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resourcestr)

否

是

@Trace

主按钮切换后的图标。

 说明：

如果是非主按钮，altIcon不生效。

iconFillColor

[ColorMetrics](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-graphics#colormetrics12)

否

是

@Trace

圆形按钮的图标颜色。

iconSize

[LengthMetrics](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-graphics#lengthmetrics12)

否

是

@Trace

圆形按钮的图标大小。

baseIconSymbolGlyphModifier

[SymbolGlyphModifier](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-attribute-modifier#自定义modifier)

否

是

@Trace

圆形按钮切换前的图标的Modifier样式。

altIconSymbolGlyphModifier

[SymbolGlyphModifier](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-attribute-modifier#自定义modifier)

否

是

@Trace

圆形按钮切换后的图标的Modifier样式。

accessibilityText

[ResourceStr](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resourcestr)

否

是

@Trace

圆形按钮的无障碍文本属性。当组件不包含文本属性时，屏幕朗读选中此组件时不播报，使用者无法清楚地知道当前选中了什么组件。为了解决此场景，开发人员可为不包含文字信息的组件设置无障碍文本，当屏幕朗读选中此组件时播报无障碍文本的内容，帮助屏幕朗读的使用者清楚地知道自己选中了什么组件。

默认值：""。

accessibilityDescription

[ResourceStr](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resourcestr)

否

是

@Trace

圆形按钮的无障碍描述。此描述用于向用户详细解释当前组件，开发人员应为组件的这一属性提供较为详尽的文本说明，以协助用户理解即将执行的操作及其可能产生的后果。特别是当这些后果无法仅从组件的属性和无障碍文本中直接获知时。如果组件同时具备文本属性和无障碍说明属性，当组件被选中时，系统将首先播报组件的文本属性，随后播报无障碍说明属性的内容。

默认值："单指双击即可执行"。

accessibilityLevel

string

否

是

@Trace

圆形按钮的无障碍重要性，用于控制当前项是否可被无障碍辅助服务所识别。

支持的值为：

"auto"：当前组件会转换"yes"。

"yes"：当前组件可被无障碍辅助服务所识别。

"no"：当前组件不可被无障碍辅助服务所识别。

"no-hide-descendants"：当前组件及其所有子组件不可被无障碍辅助服务所识别。

默认值："auto"。

id

string

否

是

@Trace

圆形按钮的id，用于[openPopup](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-promptaction#openpopup18)绑定的id。

hoverTips

[ResourceStr](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resourcestr)

否

是

@Trace

圆形按钮的悬浮提示信息。

buttonModifier

[ButtonModifier](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-attribute-modifier#自定义modifier)

否

是

@Trace

圆形按钮的modifier。

#### constructor

constructor(options: ActionBarButtonOptions)

ActionBarButton的构造函数。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSPattern.Standard

**起始版本：**6.0.0(20)

**参数：**

参数名

类型

必填

说明

options

[ActionBarButtonOptions](#section82531145191119)

是

HdsActionBar的按钮参数。

#### ActionBarButtonOptions

定义ActionBarButton的constructor参数。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSPattern.Standard

**起始版本：**6.0.0(20)

**参数：**

名称

类型

只读

可选

说明

width

[LengthMetrics](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-graphics#lengthmetrics12)

否

是

圆形按钮的宽度。

 说明：

支持px,vp,fp,lpx单位，不支持percent。

backgroundColor

[ColorMetrics](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-graphics#colormetrics12)

否

是

圆形按钮的背景颜色。

shadowStyle

[ShadowOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-image-effect#shadowoptions对象说明) | [ShadowStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-image-effect#shadowstyle10枚举说明)

否

是

圆形按钮的阴影。

默认值：ShadowStyle.OUTER_DEFAULT_LG。

enabled

boolean

否

是

圆形按钮是否启用。

默认值：true。

 说明：

enabled为true表示圆形按钮启用，enabled为false表示圆形按钮禁用。

onClick

[Callback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#callback12)<void>

否

是

圆形按钮的点击事件。

baseIcon

[ResourceStr](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resourcestr)

否

是

主按钮的初始状态的图标。

 说明：

如果是非主按钮，baseIcon是非主按钮的图标。

altIcon

[ResourceStr](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resourcestr)

否

是

主按钮切换后的图标。

 说明：

如果是非主按钮，altIcon不生效。

iconFillColor

[ColorMetrics](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-graphics#colormetrics12)

否

是

圆形按钮的图标颜色。

iconSize

[LengthMetrics](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-graphics#lengthmetrics12)

否

是

圆形按钮的图标大小。

baseIconSymbolGlyphModifier

[SymbolGlyphModifier](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-attribute-modifier#自定义modifier)

否

是

圆形按钮切换前的图标的Modifier样式。

altIconSymbolGlyphModifier

[SymbolGlyphModifier](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-attribute-modifier#自定义modifier)

否

是

圆形按钮切换后的图标的Modifier样式。

accessibilityText

[ResourceStr](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resourcestr)

否

是

圆形按钮的无障碍文本属性。当组件不包含文本属性时，屏幕朗读选中此组件时不播报，使用者无法清楚地知道当前选中了什么组件。为了解决此场景，开发人员可为不包含文字信息的组件设置无障碍文本，当屏幕朗读选中此组件时播报无障碍文本的内容，帮助屏幕朗读的使用者清楚地知道自己选中了什么组件。

默认值：""。

accessibilityDescription

[ResourceStr](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resourcestr)

否

是

圆形按钮的无障碍描述。此描述用于向用户详细解释当前组件，开发人员应为组件的这一属性提供较为详尽的文本说明，以协助用户理解即将执行的操作及其可能产生的后果。特别是当这些后果无法仅从组件的属性和无障碍文本中直接获知时。如果组件同时具备文本属性和无障碍说明属性，当组件被选中时，系统将首先播报组件的文本属性，随后播报无障碍说明属性的内容。

默认值："单指双击即可执行"。

accessibilityLevel

string

否

是

圆形按钮的无障碍重要性，用于控制当前项是否可被无障碍辅助服务所识别。

支持的值为：

"auto"：当前组件会转换"yes"。

"yes"：当前组件可被无障碍辅助服务所识别。

"no"：当前组件不可被无障碍辅助服务所识别。

"no-hide-descendants"：当前组件及其所有子组件不可被无障碍辅助服务所识别。

默认值："auto"。

id

string

否

是

圆形按钮的id，用于[openPopup](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-promptaction#openpopup18)绑定的id。

hoverTips

[ResourceStr](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resourcestr)

否

是

圆形按钮的悬浮提示信息。

buttonModifier

[ButtonModifier](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-attribute-modifier#自定义modifier)

否

是

圆形按钮的modifier。

#### ActionBarStyle

定义HdsActionBar的样式。

**装饰器类型：**@ObservedV2

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSPattern.Standard

**起始版本：**6.0.0(20)

#### 属性

ActionBarStyle的属性。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSPattern.Standard

**起始版本：**6.0.0(20)

**参数：**

名称

类型

只读

可选

装饰器类型

说明

height

[LengthMetrics](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-graphics#lengthmetrics12)

否

是

@Trace

HdsActionBar的背板高度。

backgroundBlurStyle

[BlurStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-background#blurstyle9)

否

是

@Trace

HdsActionBar的背板背景模糊效果。

默认值：BlurStyle.COMPONENT_REGULAR。

backgroundColor

[ColorMetrics](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-graphics#colormetrics12)

否

是

@Trace

HdsActionBar的背板背景颜色。

innerSpace

[LengthMetrics](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-graphics#lengthmetrics12)

否

是

@Trace

主轴方向HdsActionBar的主按钮和起始位置按钮的距离，或者主轴方向HdsActionBar的主按钮和终止位置按钮的距离。

startSpace

[LengthMetrics](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-graphics#lengthmetrics12)

否

是

@Trace

主轴方向HdsActionBar的起始位置按钮和背板的左边框的距离。

endSpace

[LengthMetrics](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-graphics#lengthmetrics12)

否

是

@Trace

主轴方向HdsActionBar的终止位置按钮和背板的右边框的距离。

enabled

boolean

否

是

@Trace

HdsActionBar是否启用。

默认值：true。

 说明：

如果enabled=false表示不启用，则背板不启用并且所有按钮都不启用；如果enabled=true表示启用，则每个按钮可以单独设置是否启用。

isHorizontal

boolean

否

是

@Trace

HdsActionBar是水平排列还是竖直排列，isHorizontal=true表示水平排列，isHorizontal=false表示竖直排列。

默认值：true。

isPrimaryIconChanged

boolean

否

是

@Trace

HdsActionBar是否切换主按钮图标，isPrimaryIconChanged=true表示切换主按钮图标，主按钮图标是altIcon，isPrimaryIconChanged=false表示不切换主按钮图标，主按钮图标是baseIcon。

默认值：false。

#### constructor

constructor(options: ActionBarStyleOptions)

ActionBarStyle的构造函数。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSPattern.Standard

**起始版本：**6.0.0(20)

**参数：**

参数名

类型

必填

说明

options

[ActionBarStyleOptions](#section13821143712333)

是

HdsActionBar的样式参数。

#### ActionBarStyleOptions

定义ActionBarStyle的constructor参数。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSPattern.Standard

**起始版本：**6.0.0(20)

**参数：**

名称

类型

只读

可选

说明

height

[LengthMetrics](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-graphics#lengthmetrics12)

否

是

HdsActionBar的背板高度。

backgroundBlurStyle

[BlurStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-background#blurstyle9)

否

是

HdsActionBar的背板背景模糊效果。

默认值：BlurStyle.COMPONENT_REGULAR。

backgroundColor

[ColorMetrics](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-graphics#colormetrics12)

否

是

HdsActionBar的背板背景颜色。

innerSpace

[LengthMetrics](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-graphics#lengthmetrics12)

否

是

主轴方向HdsActionBar的主按钮和起始位置按钮的距离，或者主轴方向HdsActionBar的主按钮和终止位置按钮的距离。

startSpace

[LengthMetrics](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-graphics#lengthmetrics12)

否

是

主轴方向HdsActionBar的起始位置按钮和背板的左边框的距离。

endSpace

[LengthMetrics](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-graphics#lengthmetrics12)

否

是

主轴方向HdsActionBar的终止位置按钮和背板的右边框的距离。

enabled

boolean

否

是

HdsActionBar是否启用。

默认值：true。

 说明：

如果enabled=false表示不启用，则背板不启用并且所有按钮都不启用；如果enabled=true表示启用，则每个按钮可以单独设置是否启用。

isHorizontal

boolean

否

是

HdsActionBar是水平排列还是竖直排列，isHorizontal=true表示水平排列，isHorizontal=false表示竖直排列。

默认值：true。

isPrimaryIconChanged

boolean

否

是

HdsActionBar是否切换主按钮图标，isPrimaryIconChanged=true表示切换主按钮图标，主按钮图标是altIcon，isPrimaryIconChanged=false表示不切换主按钮图标，主按钮图标是baseIcon。

默认值：false。

#### 示例

HdsActionBar提供一种多按钮组件。

```ets
import { HdsActionBar, ActionBarButton, ActionBarStyle } from '@kit.UIDesignKit'

@Entry
@ComponentV2
struct TestActionBar {
  @Local isExpand: boolean = true;

  @Local isPrimaryIconChanged: boolean = false;

  @Local primaryHoverTips: ResourceStr = '开始';

  build() {
    Column() {
      HdsActionBar({
        startButtons: [new ActionBarButton({
          baseIcon: $r('sys.symbol.stopwatch_fill')
        })],
        endButtons: [new ActionBarButton({
          baseIcon: $r('sys.symbol.mic_fill')
        })],
        primaryButton: new ActionBarButton({
          baseIcon: $r('sys.symbol.plus'),
          altIcon: $r('sys.symbol.play_fill'),
          onClick: () => {
            this.isExpand = !this.isExpand;
            this.isPrimaryIconChanged = !this.isPrimaryIconChanged;
            if (this.isPrimaryIconChanged) {
              this.primaryHoverTips = '暂停';
            } else {
              this.primaryHoverTips = '开始';
            }
          },
          hoverTips: this.primaryHoverTips
        }),
        actionBarStyle: new ActionBarStyle({
          isPrimaryIconChanged: this.isPrimaryIconChanged
        }),
        isExpand: this.isExpand!!
      })
    }
    .width('100%')
    .height('100%')
    .backgroundColor(0xF1F3F5)
    .justifyContent(FlexAlign.Center)
    .alignItems(HorizontalAlign.Center)
  }
}
```

效果图：