# 警告弹窗 (AlertDialog)

显示警告弹窗组件，可设置文本内容与响应回调。

从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

本模块功能依赖UI的执行上下文，不可在[UI上下文不明确](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-global-interface)的地方使用，参见[UIContext](../../types/classes/Class (UIContext).md)说明。

#### AlertDialogParam对象说明

警告弹窗的样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明title[ResourceStr](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcestr)否是

弹窗标题。

API version 20之前，弹窗标题的对齐方式为左对齐。

API version 20及之后，弹窗标题的对齐方式为居中对齐。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

subtitle10+[ResourceStr](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcestr)否是

弹窗副标题。

API version 20之前，弹窗副标题的对齐方式为左对齐。

API version 20及之后，弹窗副标题的对齐方式为居中对齐。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

message[ResourceStr](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcestr)否否

弹窗内容。

API version 20之前，弹窗内容的对齐方式为左对齐。

API version 20及之后，弹窗内容的对齐方式为居中对齐。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

autoCancelboolean否是

点击遮障层时，是否关闭弹窗，true表示关闭弹窗。false表示不关闭弹窗。

默认值：true

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

cancel[VoidCallback](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__voidcallback12)否是

点击遮障层关闭dialog时的回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

alignment[DialogAlignment](#ZH-CN_TOPIC_0000002529444899__dialogalignment枚举说明)否是

弹窗在竖直方向上的对齐方式。

默认值：DialogAlignment.Default

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**说明**：

若在UIExtension中设置showInSubWindow为true，弹窗将基于UIExtension的宿主窗口对齐。

offset[Offset](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__offset)否是

弹窗相对alignment所在位置的偏移量。

默认值：{ dx: 0 , dy: 0 }

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

gridCountnumber否是

弹窗容器宽度所占用栅格数。

默认值：4

取值范围：大于等于0的整数。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

maskRect10+[Rectangle](#ZH-CN_TOPIC_0000002529444899__rectangle8类型说明)否是

弹窗遮蔽层区域，在遮蔽层区域内的事件不透传，在遮蔽层区域外的事件透传。

默认值：{ x: 0, y: 0, width: '100%', height: '100%' }

**说明：**

showInSubWindow为true时，maskRect不生效。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

showInSubWindow11+boolean否是

某弹窗需要显示在主窗口之外时，是否在子窗口显示此弹窗。值为true表示在子窗口显示弹窗。

默认值：false，弹窗显示在应用内，而非独立子窗口。

**说明**：showInSubWindow为true的弹窗无法触发显示另一个showInSubWindow为true的弹窗。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

isModal11+boolean否是

弹窗是否为模态窗口，模态窗口有蒙层，非模态窗口无蒙层。值为false时，弹窗为非模态窗口，无蒙层。

默认值：true，此时弹窗有蒙层。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

backgroundColor11+[ResourceColor](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否是

弹窗背板颜色。

默认值：Color.Transparent

**说明：**

backgroundColor会与模糊属性backgroundBlurStyle叠加产生效果，如果不符合预期，可将backgroundBlurStyle设置为BlurStyle.NONE，即可取消模糊。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

backgroundBlurStyle11+[BlurStyle](../misc/背景设置.md#ZH-CN_TOPIC_0000002529444791__blurstyle9)否是

弹窗背板模糊材质。

默认值：BlurStyle.COMPONENT_ULTRA_THICK

**说明：**

设置为BlurStyle.NONE即可关闭背景虚化。当设置了backgroundBlurStyle为非NONE值时，则不要设置backgroundColor，否则颜色显示将不符合预期效果。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

backgroundBlurStyleOptions19+[BackgroundBlurStyleOptions](../misc/背景设置.md#ZH-CN_TOPIC_0000002529444791__backgroundblurstyleoptions10对象说明)否是

背景模糊效果。默认值请参考BackgroundBlurStyleOptions类型说明。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

backgroundEffect19+[BackgroundEffectOptions](../misc/背景设置.md#ZH-CN_TOPIC_0000002529444791__backgroundeffectoptions11)否是

背景效果参数。默认值请参考BackgroundEffectOptions类型说明。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

onWillDismiss12+Callback<[DismissDialogAction](#ZH-CN_TOPIC_0000002529444899__dismissdialogaction12)>否是

交互式关闭回调函数。

**说明：**

1.当用户执行点击遮障层关闭、侧滑（左滑/右滑）、三键back、键盘ESC关闭交互操作时，如果注册该回调函数，则不会立刻关闭弹窗。在回调函数中可以通过reason得到阻拦关闭弹窗的操作类型，从而根据原因选择是否能关闭弹窗。当前组件返回的reason中，暂不支持CLOSE_BUTTON的枚举值。

2.在onWillDismiss回调中，不能再做onWillDismiss拦截。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

cornerRadius12+[Dimension](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__dimension10) | [BorderRadiuses](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__borderradiuses9) | [LocalizedBorderRadiuses](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__localizedborderradiuses12)否是

设置背板的圆角半径。

可分别设置4个圆角的半径。

默认值：{ topLeft: '32vp', topRight: '32vp', bottomLeft: '32vp', bottomRight: '32vp' }

圆角大小受组件尺寸限制，最大值为组件宽或高的一半，若值为负，则按照默认值处理。

百分比参数方式：以父元素弹窗宽和高的百分比来设置弹窗的圆角。

**说明：**

当cornerRadius属性类型为LocalizedBorderRadiuses时，支持随语言习惯改变布局顺序。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

transition12+[TransitionEffect](../misc/组件内转场 (transition).md#ZH-CN_TOPIC_0000002497604930__transitioneffect10对象说明)否是

设置弹窗显示和退出的过渡效果。

**说明：**

1.如果不设置，则使用默认的显示/退出动效。

2.显示动效中按back键，打断显示动效，执行退出动效，动画效果为显示动效与退出动效的曲线叠加后的效果。

3.退出动效中按back键，不会打断退出动效，退出动效继续执行，继续按back键退出应用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

width12+[Dimension](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__dimension10)否是

设置弹窗背板的宽度。

**说明：**

- 弹窗宽度默认最大值：400vp。

- 百分比参数方式：弹窗参考宽度为所在窗口的宽度，在此基础上调小或调大。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

height12+[Dimension](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__dimension10)否是

设置弹窗背板的高度。

**说明：**

- 弹窗高度默认最大值：0.9 *（窗口高度 - 安全区域）。

- 百分比参数方式：弹窗参考高度为（窗口高度 - 安全区域），在此基础上调小或调大。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

borderWidth12+[Dimension](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__dimension10) | [EdgeWidths](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__edgewidths9) | [LocalizedEdgeWidths](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__localizededgewidths12)否是

可分别设置4个边框宽度。

默认值：0

百分比参数方式：以父元素弹窗宽的百分比来设置弹窗的边框宽度。

当弹窗左边框和右边框大于弹窗宽度，弹窗上边框和下边框大于弹窗高度，显示可能不符合预期。

**说明：**

当borderWidth属性类型为LocalizedEdgeWidths时，支持随语言习惯改变布局顺序。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

borderColor12+[ResourceColor](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor) | [EdgeColors](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__edgecolors9) | [LocalizedEdgeColors](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__localizededgecolors12)否是

设置弹窗背板的边框颜色。

默认值：Color.Black

如果使用borderColor属性，需要和borderWidth属性一起使用。

**说明：**

当borderColor属性类型为LocalizedEdgeColors时，支持随语言习惯改变布局顺序。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

borderStyle12+[BorderStyle](../../guides/枚举说明.md#ZH-CN_TOPIC_0000002529284967__borderstyle) | [EdgeStyles](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__edgestyles9)否是

设置弹窗背板的边框样式。

默认值：BorderStyle.Solid

如果使用borderStyle属性，需要和borderWidth属性一起使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

shadow12+[ShadowOptions](../misc/图像效果.md#ZH-CN_TOPIC_0000002497444856__shadowoptions对象说明) | [ShadowStyle](../misc/图像效果.md#ZH-CN_TOPIC_0000002497444856__shadowstyle10枚举说明)否是

设置弹窗背板的阴影。

当设备为2in1时，默认场景下获焦阴影值为ShadowStyle.OUTER_FLOATING_MD，失焦为ShadowStyle.OUTER_FLOATING_SM。其他设备默认无阴影。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

textStyle12+[TextStyle](#ZH-CN_TOPIC_0000002529444899__textstyle12对象说明)否是

设置弹窗message内容的文本样式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

enableHoverMode14+boolean否是

是否响应悬停态，值为true时，响应悬停态。

默认值：false，默认不响应。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

hoverModeArea14+[HoverModeAreaType](../misc/半模态转场.md#ZH-CN_TOPIC_0000002497604850__hovermodeareatype14)否是

悬停态下弹窗默认展示区域。

默认值：HoverModeAreaType.BOTTOM_SCREEN。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

onWillAppear19+Callback<void>否是

弹窗显示动效前的事件回调。

**说明：**

1.正常时序依次为：onWillAppear >> onDidAppear >> onWillDisappear >> onDidDisappear。

2.在onWillAppear内设置改变弹窗显示效果的回调事件，二次弹出生效。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

onDidAppear19+Callback<void>否是

弹窗弹出后的事件回调。

**说明：**

1.正常时序依次为：onWillAppear >> onDidAppear >> onWillDisappear >> onDidDisappear。

2.在onDidAppear内设置改变弹窗显示效果的回调事件，二次弹出生效。

3.快速点击弹出，关闭弹窗时，onWillDisappear在onDidAppear前生效。

4.弹窗入场动效未完成时彻底关闭弹窗，动效打断，onDidAppear不会触发。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

onWillDisappear19+Callback<void>否是

弹窗退出动效前的事件回调。

**说明：**

正常时序依次为：onWillAppear >> onDidAppear >> onWillDisappear >> onDidDisappear。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

onDidDisappear19+Callback<void>否是

弹窗消失后的事件回调。

**说明：**

正常时序依次为：onWillAppear >> onDidAppear >> onWillDisappear >> onDidDisappear。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

levelMode15+[LevelMode](../../modules/ohos/@ohos.promptAction (弹窗).md#ZH-CN_TOPIC_0000002529284783__levelmode15枚举说明)否是

设置弹窗显示层级。

**说明：**

- 默认值：LevelMode.OVERLAY。

- 当且仅当showInSubWindow属性设置为false时生效。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

levelUniqueId15+number否是

设置页面级弹窗需要显示的层级下的[节点uniqueId](FrameNode.md#ZH-CN_TOPIC_0000002529284787__getuniqueid12)。仅在levelMode属性设置为LevelMode.EMBEDDED时生效。

取值范围：大于等于0的数字。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

immersiveMode15+[ImmersiveMode](../../modules/ohos/@ohos.promptAction (弹窗).md#ZH-CN_TOPIC_0000002529284783__immersivemode15枚举说明)否是

设置页面内弹窗蒙层效果。

**说明：**

- 默认值：ImmersiveMode.DEFAULT

- 当且仅当levelMode属性设置为LevelMode.EMBEDDED时生效。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

levelOrder18+[LevelOrder](#ZH-CN_TOPIC_0000002529444899__levelorder18)否是

设置弹窗显示的顺序。

**说明：**

- 默认值：LevelOrder.clamp(0)

- 不支持动态刷新顺序。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

#### LevelOrder18+

type LevelOrder = LevelOrder

弹窗的显示顺序。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

类型说明[LevelOrder](../../modules/ohos/@ohos.promptAction (弹窗).md#ZH-CN_TOPIC_0000002529284783__levelorder18)设置弹窗的显示顺序。

#### AlertDialogParamWithConfirm对象说明

继承自[AlertDialogParam](#ZH-CN_TOPIC_0000002529444899__alertdialogparam对象说明)。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明confirm[AlertDialogButtonBaseOptions](#ZH-CN_TOPIC_0000002529444899__alertdialogbuttonbaseoptions18对象说明)否是确认Button的使能状态、默认焦点、按钮风格、文本内容、文本色、按钮背景色和点击回调。在弹窗获焦且未进行tab键走焦时，该按钮默认响应Enter键。多重弹窗情况下，可自动获焦并连续响应。默认响应Enter键能力在defaultFocus为true时不生效。

confirm参数优先级：fontColor、backgroundColor > style > defaultFocus

backgroundColorfontColorstyledefaultFocus效果绿底红字--绿底红字绿底-DialogButtonStyle.HIGHLIGHT-绿底白字绿底-DialogButtonStyle.DEFAULT-绿底蓝字绿底--TRUE绿底白字绿底--FALSE/-绿底蓝字-红字DialogButtonStyle.HIGHLIGHT-蓝底红字-红字DialogButtonStyle.DEFAULT-白底红字-红字-TRUE蓝底红字-红字-FALSE/-白底红字--DialogButtonStyle.HIGHLIGHT-蓝底白字--DialogButtonStyle.DEFAULT-白底蓝字---TRUE蓝底白字---FALSE/-白底蓝字

#### AlertDialogParamWithButtons对象说明

继承自[AlertDialogParam](#ZH-CN_TOPIC_0000002529444899__alertdialogparam对象说明)。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明primaryButton[AlertDialogButtonBaseOptions](#ZH-CN_TOPIC_0000002529444899__alertdialogbuttonbaseoptions18对象说明)否否确认Button的使能状态、默认焦点、按钮风格、文本内容、文本色、按钮背景色和点击回调。在弹窗获焦且未进行tab键走焦时，该按钮默认响应Enter键，且多重弹窗可自动获焦连续响应。默认响应Enter键能力在defaultFocus为true时不生效。secondaryButton[AlertDialogButtonBaseOptions](#ZH-CN_TOPIC_0000002529444899__alertdialogbuttonbaseoptions18对象说明)否否确认Button的使能状态、默认焦点、按钮风格、文本内容、文本色、按钮背景色和点击回调。

#### AlertDialogParamWithOptions10+对象说明

继承自[AlertDialogParam](#ZH-CN_TOPIC_0000002529444899__alertdialogparam对象说明)。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明buttonsArray<[AlertDialogButtonOptions](#ZH-CN_TOPIC_0000002529444899__alertdialogbuttonoptions10对象说明)>否否弹窗容器中的多个按钮。buttonDirection[DialogButtonDirection](#ZH-CN_TOPIC_0000002529444899__dialogbuttondirection10枚举说明)否是按钮排布方向默认为DialogButtonDirection.AUTO。建议3个以上按钮使用Auto模式（两个以上按钮会切换为纵向模式，通常能显示更多按钮）。非Auto模式下，3个以上按钮可能会显示不全，超出显示范围的按钮会被截断。

#### AlertDialogButtonOptions10+对象说明

继承自[AlertDialogButtonBaseOptions](#ZH-CN_TOPIC_0000002529444899__alertdialogbuttonbaseoptions18对象说明)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明primary12+boolean否是

在弹窗获焦且未进行tab键走焦时，按钮是否默认响应Enter键。多个Button时，只允许一个Button的该字段配置为true，否则所有Button均不响应。多重弹窗可自动获焦连续响应。在defaultFocus为true时不生效。值为true表示按钮默认响应Enter键，值为false时，按钮不默认响应Enter键。

默认值：false

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

#### AlertDialogButtonBaseOptions18+对象说明

警告弹窗中按钮的样式。

为规范匿名对象的定义，API 18版本修改了此处的元素定义。其中，保留了历史匿名对象的起始版本信息，会出现外层元素@since版本号高于内层元素版本号的情况，但这不影响接口的使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明enabled10+boolean否是

点击Button是否响应，默认值true。

值为true时，Button可以响应。值为false时，Button不可以响应。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

defaultFocus10+boolean否是

设置Button是否是默认焦点，默认值false。值为true表示Button为默认焦点，值为false表示Button不为默认焦点。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

style10+[DialogButtonStyle](../../guides/枚举说明.md#ZH-CN_TOPIC_0000002529284967__dialogbuttonstyle10)否是

设置Button的风格样式，默认值DialogButtonStyle.DEFAULT。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

value10+[ResourceStr](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcestr)否否

Button的文本内容，若值为null，则该按钮不显示。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

fontColor10+[ResourceColor](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否是

Button的文本颜色。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

backgroundColor10+[ResourceColor](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否是

Button背景颜色。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

action10+[VoidCallback](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__voidcallback12)否否

Button选中时的回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

#### DialogButtonDirection10+枚举说明

警告弹窗中按钮的对齐方式。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称值说明AUTO0两个及以下按钮水平排布，两个以上为竖直排布。HORIZONTAL1按钮水平布局。VERTICAL2按钮竖直布局。

#### DialogAlignment枚举说明

警告弹窗的对齐方式。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称值说明Top0垂直顶部对齐。Center1垂直居中对齐。Bottom2垂直底部对齐。Default3默认对齐。TopStart8+4左上对齐。TopEnd8+5右上对齐。CenterStart8+6左中对齐。CenterEnd8+7右中对齐。BottomStart8+8左下对齐。BottomEnd8+9右下对齐。

#### Rectangle8+类型说明

Rectangle是各种Dialog中maskRect参数的类型。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明x[Length](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__length)否是

弹窗遮蔽层区域相对于窗口左上角的x轴坐标。

默认值：0vp

y[Length](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__length)否是

弹窗遮蔽层区域相对于窗口左上角的y轴坐标。

默认值：0vp

width[Length](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__length)否是

弹窗遮蔽层区域的宽度。

默认值：'100%'

height[Length](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__length)否是

弹窗遮蔽层区域的高度。

默认值：'100%'

x和y可以设置正负值百分比。当x设置为'100%'时表示遮蔽层区域往右偏移窗口本身宽度大小，当x设置为'-100%'时表示遮蔽层区域往左偏移窗口本身宽度大小。当y设置为'100%'时表示遮蔽层区域往下偏移窗口本身高度大小，当y设置为'-100%'时表示遮蔽层区域往上偏移窗口本身高度大小。

width和height只能设置正值，支持百分比，如果设置为负值，那么该值将被重置为默认值。

百分比相对于窗口自身宽高进行计算。

#### DismissDialogAction12+

Dialog关闭的信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

#### 属性

名称类型只读可选说明dismissCallback<void>否否Dialog关闭回调函数。开发者需要退出时调用，不需要退出时无需调用。reason[DismissReason](../misc/Popup控制.md#ZH-CN_TOPIC_0000002529284839__dismissreason12枚举说明)否否Dialog无法关闭原因。根据开发者需要选择不同操作下，Dialog是否需要关闭。

#### TextStyle12+对象说明

弹窗中message的截断方式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明wordBreak[WordBreak](../../guides/枚举说明.md#ZH-CN_TOPIC_0000002529284967__wordbreak11)否是

弹窗message内容的文本截断方式。

默认值：WordBreak.BREAK_ALL

#### AlertDialog

#### show(deprecated)

static show(value: AlertDialogParamWithConfirm | AlertDialogParamWithButtons | AlertDialogParamWithOptions)

定义警告弹窗并弹出。

从API version 7开始支持，从API version 18开始废弃，建议使用[showAlertDialog](../../types/classes/Class (UIContext).md#ZH-CN_TOPIC_0000002529444749__showalertdialog)替代。showAlertDialog需先获取[UIContext](../../types/classes/Class (UIContext).md)实例后再进行调用。

从API version 10开始，可以通过使用[UIContext](../../types/classes/Class (UIContext).md)中的[showAlertDialog](../../types/classes/Class (UIContext).md#ZH-CN_TOPIC_0000002529444749__showalertdialog)来明确UI的执行上下文。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明value[AlertDialogParamWithConfirm](#ZH-CN_TOPIC_0000002529444899__alertdialogparamwithconfirm对象说明) | [AlertDialogParamWithButtons](#ZH-CN_TOPIC_0000002529444899__alertdialogparamwithbuttons对象说明) | [AlertDialogParamWithOptions](#ZH-CN_TOPIC_0000002529444899__alertdialogparamwithoptions10对象说明)10+是定义并显示AlertDialog组件。

#### 示例

直接使用AlertDialog可能导致[UI上下文不明确](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-global-interface)的问题，建议使用getUIContext()获取[UIContext](../../types/classes/Class (UIContext).md)实例，并使用[showAlertDialog](../../types/classes/Class (UIContext).md#ZH-CN_TOPIC_0000002529444749__showalertdialog)调用绑定实例的AlertDialog.show()。

#### 示例1（弹出多个按钮的弹窗）

该示例实现了分别弹出一、二、三个按钮的弹窗。

```ets
// xxx.ets
@Entry
@Component
struct AlertDialogExample {
  build() {
    Column({ space: 5 }) {
      Button('one button dialog')
        .onClick(() => {
          this.getUIContext().showAlertDialog(
            {
              title: 'title',
              message: 'text',
              autoCancel: true,
              alignment: DialogAlignment.Bottom,
              offset: { dx: 0, dy: -20 },
              gridCount: 3,
              confirm: {
                value: 'button',
                action: () => {
                  console.info('Button-clicking callback');
                }
              },
              cancel: () => {
                console.info('Closed callbacks');
              },
              onWillDismiss: (dismissDialogAction: DismissDialogAction) => {
                console.info(`reason= ${dismissDialogAction.reason}`);
                console.info('AlertDialog onWillDismiss');
                if (dismissDialogAction.reason === DismissReason.PRESS_BACK) {
                  dismissDialogAction.dismiss();
                }
                if (dismissDialogAction.reason === DismissReason.TOUCH_OUTSIDE) {
                  dismissDialogAction.dismiss();
                }
              }
            }
          )
        })
        .backgroundColor(0x317aff)
      Button('two button dialog')
        .onClick(() => {
          this.getUIContext().showAlertDialog(
            {
              title: 'title',
              subtitle: 'subtitle',
              message: 'text',
              autoCancel: true,
              alignment: DialogAlignment.Bottom,
              gridCount: 4,
              offset: { dx: 0, dy: -20 },
              primaryButton: {
                value: 'cancel',
                action: () => {
                  console.info('Callback when the first button is clicked');
                }
              },
              secondaryButton: {
                enabled: true,
                defaultFocus: true,
                style: DialogButtonStyle.HIGHLIGHT,
                value: 'ok',
                action: () => {
                  console.info('Callback when the second button is clicked');
                }
              },
              cancel: () => {
                console.info('Closed callbacks');
              },
              onWillDismiss: (dismissDialogAction: DismissDialogAction) => {
                console.info(`reason= ${dismissDialogAction.reason}`);
                console.info('AlertDialog onWillDismiss');
                if (dismissDialogAction.reason === DismissReason.PRESS_BACK) {
                  dismissDialogAction.dismiss();
                }
                if (dismissDialogAction.reason === DismissReason.TOUCH_OUTSIDE) {
                  dismissDialogAction.dismiss();
                }
              }
            }
          )
        }).backgroundColor(0x317aff)
      Button('three button dialog')
        .onClick(() => {
          this.getUIContext().showAlertDialog(
            {
              title: 'title',
              subtitle: 'subtitle',
              message: 'text',
              autoCancel: true,
              alignment: DialogAlignment.Bottom,
              gridCount: 4,
              offset: { dx: 0, dy: -20 },
              buttonDirection: DialogButtonDirection.HORIZONTAL,
              buttons: [
                {
                  value: '按钮',
                  action: () => {
                    console.info('Callback when button1 is clicked');
                  }
                },
                {
                  value: '按钮',
                  action: () => {
                    console.info('Callback when button2 is clicked');
                  }
                },
                {
                  value: '按钮',
                  enabled: true,
                  defaultFocus: true,
                  style: DialogButtonStyle.HIGHLIGHT,
                  action: () => {
                    console.info('Callback when button3 is clicked');
                  }
                },
              ],
              cancel: () => {
                console.info('Closed callbacks');
              },
              onWillDismiss: (dismissDialogAction: DismissDialogAction) => {
                console.info(`reason= ${dismissDialogAction.reason}`);
                console.info('AlertDialog onWillDismiss');
                if (dismissDialogAction.reason === DismissReason.PRESS_BACK) {
                  dismissDialogAction.dismiss();
                }
                if (dismissDialogAction.reason === DismissReason.TOUCH_OUTSIDE) {
                  dismissDialogAction.dismiss();
                }
              }
            }
          )
        }).backgroundColor(0x317aff)
    }.width('100%').margin({ top: 5 })
  }
}
```

#### 示例2（可在主窗外弹出的弹窗）

在2in1设备上设置showInSubWindow为true时，可以弹出在主窗外显示的弹窗。

```ets
// xxx.ets
@Entry
@Component
struct AlertDialogExample {
  build() {
    Column({ space: 5 }) {
      Button('one button dialog')
        .onClick(() => {
          this.getUIContext().showAlertDialog(
            {
              title: 'title',
              subtitle: 'subtitle',
              message: 'text',
              autoCancel: true,
              alignment: DialogAlignment.Center,
              gridCount: 4,
              showInSubWindow: true,
              isModal: true,
              offset: { dx: 0, dy: -20 },
              buttonDirection: DialogButtonDirection.HORIZONTAL,
              buttons: [
                {
                  value: '按钮',
                  action: () => {
                    console.info('Callback when button1 is clicked');
                  }
                },
                {
                  value: '按钮',
                  action: () => {
                    console.info('Callback when button2 is clicked');
                  }
                },
                {
                  value: '按钮',
                  enabled: true,
                  defaultFocus: true,
                  style: DialogButtonStyle.HIGHLIGHT,
                  action: () => {
                    console.info('Callback when button3 is clicked');
                  }
                },
              ],
              cancel: () => {
                console.info('Closed callbacks');
              },
              onWillDismiss: (dismissDialogAction: DismissDialogAction) => {
                console.info(`reason= ${dismissDialogAction.reason}`);
                console.info('AlertDialog onWillDismiss');
                if (dismissDialogAction.reason === DismissReason.PRESS_BACK) {
                  dismissDialogAction.dismiss();
                }
                if (dismissDialogAction.reason === DismissReason.TOUCH_OUTSIDE) {
                  dismissDialogAction.dismiss();
                }
              }
            })
        })
    }.width('100%').margin({ top: 5 })
  }
}
```

#### 示例3（设置弹窗的动画）

该示例通过配置transition实现弹窗的显示和消失动画。

```ets
// xxx.ets
@Entry
@Component
struct AlertDialogExample {
  build() {
    Column({ space: 5 }) {
      Button('AlertDialog Set Duration')
        .onClick(() => {
          this.getUIContext().showAlertDialog(
            {
              title: 'AlertDialog 1',
              message: 'Set Animation Duration open 3 second, close 100ms',
              autoCancel: true,
              alignment: DialogAlignment.Top,
              offset: { dx: 0, dy: -20 },
              gridCount: 3,
              transition: TransitionEffect.asymmetric(TransitionEffect.OPACITY
                .animation({ duration: 3000, curve: Curve.Sharp })
                .combine(TransitionEffect.scale({ x: 1.5, y: 1.5 }).animation({ duration: 3000, curve: Curve.Sharp })),
                TransitionEffect.OPACITY.animation({ duration: 100, curve: Curve.Smooth })
                  .combine(TransitionEffect.scale({ x: 0.5, y: 0.5 })
                    .animation({ duration: 100, curve: Curve.Smooth }))),
              confirm: {
                value: 'button',
                action: () => {
                  console.info('Button-clicking callback');
                }
              },
              cancel: () => {
                console.info('Closed callbacks');
              }
            }
          )
        })
        .backgroundColor(0x317aff).height('88px')
    }.width('100%').margin({ top: 5 })
  }
}
```

#### 示例4（设置弹窗的样式）

示例定义了AlertDialog的样式，包括宽度、高度、背景色、阴影等。

```ets
// xxx.ets
@Entry
@Component
struct AlertDialogExample {
  build() {
    Column({ space: 5 }) {
      Button('one button dialog')
        .onClick(() => {
          this.getUIContext().showAlertDialog(
            {
              title: 'title',
              message: 'text',
              autoCancel: true,
              alignment: DialogAlignment.Center,
              offset: { dx: 0, dy: -20 },
              gridCount: 3,
              width: 300,
              height: 200,
              cornerRadius: 20,
              borderWidth: 1,
              borderStyle: BorderStyle.Dashed, //使用borderStyle属性，需要和borderWidth属性一起使用
              borderColor: Color.Blue, //使用borderColor属性，需要和borderWidth属性一起使用
              backgroundColor: Color.White,
              shadow: ({
                radius: 20,
                color: Color.Grey,
                offsetX: 50,
                offsetY: 0
              }),
              textStyle: { wordBreak: WordBreak.BREAK_ALL },
              confirm: {
                value: 'button',
                action: () => {
                  console.info('Button-clicking callback');
                }
              },
              cancel: () => {
                console.info('Closed callbacks');
              },
              onWillDismiss: (dismissDialogAction: DismissDialogAction) => {
                console.info(`reason= ${dismissDialogAction.reason}`);
                console.info('AlertDialog onWillDismiss');
                if (dismissDialogAction.reason === DismissReason.PRESS_BACK) {
                  dismissDialogAction.dismiss();
                }
                if (dismissDialogAction.reason === DismissReason.TOUCH_OUTSIDE) {
                  dismissDialogAction.dismiss();
                }
              }
            }
          )
        })
        .backgroundColor(0x317aff)
    }.width('100%').margin({ top: 5 })
  }
}
```

#### 示例5（悬停态弹窗）

该示例展示了在折叠屏悬停态下设置dialog布局区域的效果。

```ets
// xxx.ets
@Entry
@Component
struct AlertDialogExample {
  build() {
    Column({ space: 5 }) {
      Button('one button dialog')
        .onClick(() => {
          this.getUIContext().showAlertDialog(
            {
              title: 'title',
              message: 'text',
              autoCancel: true,
              alignment: DialogAlignment.Bottom,
              gridCount: 3,
              confirm: {
                value: 'button',
                action: () => {
                  console.info('Button-clicking callback');
                }
              },
              cancel: () => {
                console.info('Closed callbacks');
              },
              onWillDismiss: (dismissDialogAction: DismissDialogAction) => {
                console.info(`reason= ${dismissDialogAction.reason}`);
                console.info('AlertDialog onWillDismiss');
                if (dismissDialogAction.reason === DismissReason.PRESS_BACK) {
                  dismissDialogAction.dismiss();
                }
                if (dismissDialogAction.reason === DismissReason.TOUCH_OUTSIDE) {
                  dismissDialogAction.dismiss();
                }
              },
              enableHoverMode: true,
              hoverModeArea: HoverModeAreaType.TOP_SCREEN
            }
          )
        })
        .backgroundColor(0x317aff)
    }.width('100%').margin({ top: 5 })
  }
}
```

#### 示例6（弹窗生命周期）

该示例展示了弹窗生命周期的相关接口的使用方法。

```ets
// xxx.ets
@Entry
@Component
struct Example2 {
  @State log: string = 'Log information:';

  build() {
    Column({ space: 5 }) {
      Button('AlertDialog')
        .onClick(() => {
          this.getUIContext().showAlertDialog({
            title: 'AlertDialog',
            message: 'message',
            autoCancel: true,
            alignment: DialogAlignment.Bottom,
            offset: { dx: 0, dy: -20 },
            confirm: {
              value: 'button',
              action: () => {
                console.info('AlertDialog Button-clicking callback');
              }
            },
            cancel: () => {
              console.info('Closed callbacks');
            },
            onDidAppear: () => {
              this.log += '# onDidAppear';
              console.info('AlertDialog,is onDidAppear!');
            },
            onDidDisappear: () => {
              this.log += '# onDidDisappear';
              console.info('AlertDialog,is onDidDisappear!');
            },
            onWillAppear: () => {
              this.log = 'Log information:onWillAppear';
              console.info('AlertDialog,is onWillAppear!');
            },
            onWillDisappear: () => {
              this.log += '# onWillDisappear';
              console.info('AlertDialog,is onWillDisappear!');
            }
          })
        })
      Text(this.log).fontSize(30).margin({ top: 200 })
    }.width('100%').margin({ top: 5 })
  }
}
```

#### 示例7（自定义背景模糊效果参数）

从API version 19开始，该示例通过配置[backgroundBlurStyleOptions](#ZH-CN_TOPIC_0000002529444899__alertdialogparam对象说明)，实现自定义背景模糊效果。

```ets
@Entry
@Component
struct AlertDialogExample {
  build() {
    Stack({ alignContent: Alignment.Top }) {
      // $r('app.media.bg')需要替换为开发者所需的图像资源文件。
      Image($r('app.media.bg'))
      Column() {
        Button("AlertDialog")
          .margin(20)
          .onClick(() => {
            this.getUIContext().showAlertDialog({
              title: 'AlertDialog Title',
              message: 'AlertDialog Text',
              primaryButton: {
                value: '确定',
                action: () => {
                  console.info('primaryButton');
                }
              },
              secondaryButton: {
                value: '取消',
                action: () => {
                  console.info('secondaryButton');
                }
              },
              backgroundColor: undefined,
              backgroundBlurStyle: BlurStyle.Thin,
              backgroundBlurStyleOptions: {
                colorMode: ThemeColorMode.LIGHT,
                adaptiveColor: AdaptiveColor.AVERAGE,
                scale: 1,
                blurOptions: { grayscale: [20, 20] },
              },
            });
          })
      }.width('100%')
    }
  }
}
```

#### 示例8（自定义背景效果参数）

从API version 19开始，该示例通过配置[backgroundEffect](#ZH-CN_TOPIC_0000002529444899__alertdialogparam对象说明)，实现自定义背景效果。

```ets
@Entry
@Component
struct AlertDialogExample {
  build() {
    Stack({ alignContent: Alignment.Top }) {
      // $r('app.media.bg')需要替换为开发者所需的图像资源文件。
      Image($r('app.media.bg'))
      Column() {
        Button("AlertDialog")
          .margin(20)
          .onClick(() => {
            this.getUIContext().showAlertDialog({
              title: 'AlertDialog Title',
              message: 'AlertDialog Text',
              primaryButton: {
                value: '确定',
                action: () => {
                  console.info('primaryButton');
                }
              },
              secondaryButton: {
                value: '取消',
                action: () => {
                  console.info('secondaryButton');
                }
              },
              backgroundColor: undefined,
              backgroundBlurStyle: BlurStyle.Thin,
              backgroundEffect: {
                radius: 60,
                saturation: 0,
                brightness: 1,
                color: Color.White,
                blurOptions: { grayscale: [20, 20] }
              },
            });
          })
      }.width('100%')
    }
  }
}
```
