# @ohos.promptAction (弹窗)

创建并显示即时反馈、对话框和操作菜单。

-

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

-

本模块不支持在[UIAbility](@ohos.app.ability.UIAbility (带界面的应用组件).md)的文件声明处使用，即不能在UIAbility的生命周期中调用，需要在创建组件实例后使用。

-

本模块功能依赖UI的执行上下文，不可在[UI上下文不明确](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-global-interface#ui上下文不明确)的地方使用，参见[UIContext](zh-cn_topic_0000002529444749.html)说明。建议使用UIContext中的弹窗方法。

#### 导入模块

```ets
import { promptAction } from '@kit.ArkUI';
```

#### promptAction.openToast18+

openToast(options: ShowToastOptions): Promise<number>

显示即时反馈并通过Promise返回其id。

-

不支持在输入法类型窗口中使用子窗（showMode设置为TOP_MOST或者SYSTEM_TOP_MOST）的openToast，详情见输入法框架的约束与限制说明[createPanel](@ohos.inputMethodEngine (输入法服务).md#ZH-CN_TOPIC_0000002529445255__createpanel10-1)。

-

直接使用openToast可能导致[UI上下文不明确](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-global-interface#ui上下文不明确)的问题，建议使用UIContext中的getPromptAction方法获取到PromptAction对象，再通过该对象调用[openToast](zh-cn_topic_0000002529444747.html#ZH-CN_TOPIC_0000002529444747__opentoast18)实现。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数**

参数名类型必填说明options[ShowToastOptions](#ZH-CN_TOPIC_0000002529284783__showtoastoptions)是Toast选项。

**返回值**

类型说明Promise<number>返回即时反馈的id，可供closeToast使用。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[接口调用异常错误码](接口调用异常错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed.100001Internal error.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { PromptAction, UIContext } from '@kit.ArkUI';

@Entry
@Component
struct toastExample {
  @State toastId: number = 0;
  uiContext: UIContext = this.getUIContext();
  promptAction: PromptAction = this.uiContext.getPromptAction();

  build() {
    Column() {
      Button('Open Toast')
        .height(100)
        .type(ButtonType.Capsule)
        .onClick(() => {
          this.promptAction.openToast({
            message: 'Toast Message',
            duration: 10000,
          }).then((toastId: number) => {
            this.toastId = toastId;
          })
            .catch((error: BusinessError) => {
              console.error(`openToast error code is ${error.code}, message is ${error.message}`);
            })
        })
      Blank().height(50)
      Button('Close Toast')
        .height(100)
        .type(ButtonType.Capsule)
        .onClick(() => {
          try {
            this.promptAction.closeToast(this.toastId);
          } catch (error) {
            let message = (error as BusinessError).message;
            let code = (error as BusinessError).code;
            console.error(`CloseToast error code is ${code}, message is ${message}`);
          }
        })
    }.height('100%').width('100%').justifyContent(FlexAlign.Center)
  }
}
```

#### promptAction.closeToast18+

closeToast(toastId: number): void

关闭即时反馈。

直接使用closeToast可能导致[UI上下文不明确](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-global-interface#ui上下文不明确)的问题，建议使用UIContext中的getPromptAction方法获取到PromptAction对象，再通过该对象调用[openToast](zh-cn_topic_0000002529444747.html#ZH-CN_TOPIC_0000002529444747__closetoast18)实现。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数**

参数名类型必填说明toastIdnumber是openToast返回的id。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)、[弹窗错误码](弹窗错误码.md)和[接口调用异常错误码](接口调用异常错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed.100001Internal error.103401Cannot find the toast.

**示例：**

示例请看[promptAction.openToast18](#ZH-CN_TOPIC_0000002529284783__promptactionopentoast18)的示例。

#### ShowToastOptions

Toast的选项。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明messagestring | [Resource](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resource)否否

显示的文本信息。

**说明：**

默认字体为'Harmony Sans'，不支持设置其他字体。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

durationnumber否是

设置Toast弹出的持续时间。

默认值：1500ms

取值范围：[1500, 10000]

若小于1500ms则取默认值，若大于10000ms则取上限值10000ms。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

bottomstring | number否是

设置Toast底部边框距离导航条的高度，软键盘拉起时，如果bottom值过小，toast要被软键盘遮挡时，会自动避让至距离软键盘80vp处。

默认值：80vp

**说明：**

当底部没有导航条时，bottom为设置弹窗底部边框距离窗口底部的高度。

设置对齐方式alignment后，bottom不生效。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

showMode11+[ToastShowMode](#ZH-CN_TOPIC_0000002529284783__toastshowmode11)否是

设置Toast层级。

默认值：ToastShowMode.DEFAULT，默认显示在应用内。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

alignment12+[Alignment](枚举说明.md#ZH-CN_TOPIC_0000002529284967__alignment)否是

对齐方式。

**说明：**

不同alignment下，Toast位置对齐效果，如下图所示。

Toast的文本显示默认自左向右，不支持其他对齐方式。

默认值：undefined，默认底部偏上位置。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

offset12+[Offset](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__offset)否是

在对齐方式上的偏移。

默认值：{ dx: 0, dy: 0 }，默认没有偏移。

**说明：**

仅支持设置px类型的数值。如需设置其他类型的数值，应将其他类型转换为px类型后传入。例如，若需设置vp，应将其转换为px后传入。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

backgroundColor12+[ResourceColor](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否是

Toast的背板颜色。

默认值：Color.Transparent

**说明：**

backgroundColor会与模糊属性backgroundBlurStyle叠加产生效果，如果不符合预期，可将backgroundBlurStyle设置为BlurStyle.NONE，即可取消模糊。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

textColor12+[ResourceColor](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否是

Toast的文本颜色。

默认值：Color.Black

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

backgroundBlurStyle12+[BlurStyle](背景设置.md#ZH-CN_TOPIC_0000002529444791__blurstyle9)否是

Toast的背板模糊材质。

默认值：BlurStyle.COMPONENT_ULTRA_THICK

**说明：**

设置为BlurStyle.NONE即可关闭背景虚化。当设置了backgroundBlurStyle为非NONE值时，则不要设置backgroundColor，否则颜色显示将不符合预期效果。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

shadow12+[ShadowOptions](图像效果.md#ZH-CN_TOPIC_0000002497444856__shadowoptions对象说明) | [ShadowStyle](图像效果.md#ZH-CN_TOPIC_0000002497444856__shadowstyle10枚举说明)否是

Toast的背板阴影。

默认值：ShadowStyle.OUTER_DEFAULT_MD

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

enableHoverMode14+boolean否是

是否响应悬停态，值为true时，响应悬停态。

默认值：false，默认不响应。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

hoverModeArea14+[HoverModeAreaType](半模态转场.md#ZH-CN_TOPIC_0000002497604850__hovermodeareatype14)否是

响应悬停态时，弹窗的显示区域。

默认值：HoverModeAreaType.BOTTOM_SCREEN，默认显示在下半屏。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

#### ToastShowMode11+

设置Toast的显示模式，默认显示在应用内，支持显示在子窗。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称值说明DEFAULT0Toast显示在应用内。TOP_MOST1Toast显示在子窗。

#### ShowDialogOptions

对话框的选项。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明titlestring | [Resource](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resource)否是

标题文本。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

messagestring | [Resource](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resource)否是

内容文本。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

buttonsArray<[Button](#ZH-CN_TOPIC_0000002529284783__button)>否是

对话框中按钮的数组，结构为：{text:'button', color: '#666666'}，支持大于1个按钮。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

alignment10+[DialogAlignment](警告弹窗 (AlertDialog).md#ZH-CN_TOPIC_0000002529444899__dialogalignment枚举说明)否是

对话框在竖直方向上的对齐方式。

默认值：DialogAlignment.Default

**说明：**

若在UIExtension中设置showInSubWindow为true, 弹窗将基于UIExtension的宿主窗口对齐。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

offset10+[Offset](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__offset)否是

对话框相对alignment所在位置的偏移量。

默认值：{ dx: 0 , dy: 0 }

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

maskRect10+[Rectangle](警告弹窗 (AlertDialog).md#ZH-CN_TOPIC_0000002529444899__rectangle8类型说明)否是

对话框遮蔽层区域，在遮蔽层区域内的事件不透传，在遮蔽层区域外的事件透传。

默认值：{ x: 0, y: 0, width: '100%', height: '100%' }

**说明：**

showInSubWindow为true时，maskRect不生效。

maskRect在设置[Rectangle](警告弹窗 (AlertDialog).md#ZH-CN_TOPIC_0000002529444899__rectangle8类型说明)中的部分属性后，若未设置其余的属性，则其余属性的默认值为0。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

showInSubWindow11+boolean否是

某对话框需要显示在主窗口之外时，是否在子窗口显示此对话框。值为true表示在子窗口显示对话框。

默认值：false，对话框显示在应用内，而非独立子窗口。

**说明：** showInSubWindow为true的对话框无法触发显示另一个showInSubWindow为true的对话框。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

isModal11+boolean否是

对话框是否为模态窗口。值为true表示为模态窗口且有蒙层，不可与对话框周围其他控件进行交互，即蒙层区域无法事件透传。值为false表示为非模态窗口且无蒙层，可以与对话框周围其他控件进行交互。

默认值：true

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

backgroundColor12+[ResourceColor](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否是

对话框背板颜色。

默认值：Color.Transparent

**说明：**

backgroundColor会与模糊属性backgroundBlurStyle叠加产生效果，如果不符合预期，可将backgroundBlurStyle设置为BlurStyle.NONE，即可取消模糊。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

backgroundBlurStyle12+[BlurStyle](背景设置.md#ZH-CN_TOPIC_0000002529444791__blurstyle9)否是

对话框背板模糊材质。

默认值：BlurStyle.COMPONENT_ULTRA_THICK

**说明：**

设置为BlurStyle.NONE即可关闭背景虚化。当设置了backgroundBlurStyle为非NONE值时，则不要设置backgroundColor，否则颜色显示将不符合预期效果。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

backgroundBlurStyleOptions19+[BackgroundBlurStyleOptions](背景设置.md#ZH-CN_TOPIC_0000002529444791__backgroundblurstyleoptions10对象说明)否是

背景模糊效果。默认值请参考BackgroundBlurStyleOptions类型说明。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

backgroundEffect19+[BackgroundEffectOptions](背景设置.md#ZH-CN_TOPIC_0000002529444791__backgroundeffectoptions11)否是

背景效果参数。默认值请参考BackgroundEffectOptions类型说明。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

shadow12+[ShadowOptions](图像效果.md#ZH-CN_TOPIC_0000002497444856__shadowoptions对象说明) | [ShadowStyle](图像效果.md#ZH-CN_TOPIC_0000002497444856__shadowstyle10枚举说明)否是

设置对话框背板的阴影。

当设备为2in1时，默认场景下获焦阴影值为ShadowStyle.OUTER_FLOATING_MD，失焦为ShadowStyle.OUTER_FLOATING_SM。其他设备默认无阴影。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

enableHoverMode14+boolean否是

是否响应悬停态，值为true时，响应悬停态。

默认值：false，默认不响应。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

hoverModeArea14+[HoverModeAreaType](半模态转场.md#ZH-CN_TOPIC_0000002497604850__hovermodeareatype14)否是

设置悬停态下对话框的默认展示区域。

默认值：HoverModeAreaType.BOTTOM_SCREEN

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

onWillAppear19+Callback<void>否是

对话框显示动效前的事件回调。

**说明：**

1.正常时序依次为：onWillAppear>>onDidAppear>>onWillDisappear>>onDidDisappear。

2.在onWillAppear内设置改变对话框显示效果的回调事件，二次弹出生效。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

onDidAppear19+Callback<void>否是

对话框弹出后的事件回调。

**说明：**

1.正常时序依次为：onWillAppear>>onDidAppear>>onWillDisappear>>onDidDisappear。

2.在onDidAppear内设置改变弹窗显示效果的回调事件，二次弹出生效。

3.快速点击弹出，关闭对话框时，onWillDisappear在onDidAppear前生效。

4.对话框入场动效未完成时彻底关闭对话框，动效打断，onDidAppear不会触发。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

onWillDisappear19+Callback<void>否是

对话框退出动效前的事件回调。

**说明：**

1.正常时序依次为：onWillAppear>>onDidAppear>>onWillDisappear>>onDidDisappear。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

onDidDisappear19+Callback<void>否是

对话框消失后的事件回调。

**说明：**

1.正常时序依次为：onWillAppear>>onDidAppear>>onWillDisappear>>onDidDisappear。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

levelMode15+[LevelMode](#ZH-CN_TOPIC_0000002529284783__levelmode15枚举说明)否是

设置对话框显示层级。

**说明：**

- 默认值：LevelMode.OVERLAY

- 当且仅当showInSubWindow属性设置为false时生效。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

levelUniqueId15+number否是

设置页面级对话框需要显示的层级下的[节点 uniqueId](FrameNode.md#ZH-CN_TOPIC_0000002529284787__getuniqueid12)。

取值范围：大于等于0的数字。

**说明：**

- 当且仅当levelMode属性设置为LevelMode.EMBEDDED时生效。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

immersiveMode15+[ImmersiveMode](#ZH-CN_TOPIC_0000002529284783__immersivemode15枚举说明)否是

设置页面内对话框蒙层效果。

**说明：**

- 默认值：ImmersiveMode.DEFAULT

- 当且仅当levelMode属性设置为LevelMode.EMBEDDED时生效。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

levelOrder18+[LevelOrder](#ZH-CN_TOPIC_0000002529284783__levelorder18)否是

设置对话框显示的顺序。

**说明：**

- 默认值：LevelOrder.clamp(0)

- 不支持动态刷新顺序。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

#### ShowDialogSuccessResponse

对话框的响应结果。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明indexnumber否否选中按钮在buttons数组中的索引，从0开始。

#### ActionMenuOptions

操作菜单的选项。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明titlestring | [Resource](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resource)否是

标题文本。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

buttons[[Button](#ZH-CN_TOPIC_0000002529284783__button),[Button](#ZH-CN_TOPIC_0000002529284783__button)?,[Button](#ZH-CN_TOPIC_0000002529284783__button)?,[Button](#ZH-CN_TOPIC_0000002529284783__button)?,[Button](#ZH-CN_TOPIC_0000002529284783__button)?,[Button](#ZH-CN_TOPIC_0000002529284783__button)?]否否

菜单中菜单项按钮的数组，结构为：{text:'button', color: '#666666'}，支持1-6个按钮。按钮数量大于6个时，仅显示前6个按钮，之后的按钮不显示。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

showInSubWindow11+boolean否是

某操作菜单需要显示在主窗口之外时，是否在子窗口显示此菜单。值为true表示在子窗口显示菜单。

默认值：false，在子窗口不显示菜单。

**说明：**

- showInSubWindow为true的菜单无法触发显示另一个showInSubWindow为true的菜单。

- 若在UIExtension中设置showInSubWindow为true, 菜单将基于UIExtension的宿主窗口对齐。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

isModal11+boolean否是

菜单是否为模态窗口。值为true表示为模态窗口且有蒙层，不可与菜单周围其他控件进行交互，即蒙层区域无法事件透传。值为false表示为非模态窗口且无蒙层，可以与菜单周围其他控件进行交互。

默认值：true

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

levelMode15+[LevelMode](#ZH-CN_TOPIC_0000002529284783__levelmode15枚举说明)否是

设置菜单显示层级。

**说明：**

- 默认值：LevelMode.OVERLAY

- 当且仅当showInSubWindow属性设置为false时生效。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

levelUniqueId15+number否是

设置页面级菜单需要显示的层级下的[节点 uniqueId](FrameNode.md#ZH-CN_TOPIC_0000002529284787__getuniqueid12)。

取值范围：大于等于0的数字。

**说明：**

- 当且仅当levelMode属性设置为LevelMode.EMBEDDED时生效。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

immersiveMode15+[ImmersiveMode](#ZH-CN_TOPIC_0000002529284783__immersivemode15枚举说明)否是

设置页面内菜单蒙层效果。

**说明：**

- 默认值：ImmersiveMode.DEFAULT

- 当且仅当levelMode属性设置为LevelMode.EMBEDDED时生效。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

onWillAppear20+Callback<void>否是

菜单显示动效前的事件回调。

**说明：**

1.正常时序依次为：onWillAppear>>onDidAppear>>onWillDisappear>>onDidDisappear。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

onDidAppear20+Callback<void>否是

菜单弹出后的事件回调。

**说明：**

1.正常时序依次为：onWillAppear>>onDidAppear>>onWillDisappear>>onDidDisappear。

2.快速点击弹出，关闭菜单时，onWillDisappear在onDidAppear前生效。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

onWillDisappear20+Callback<void>否是

菜单退出动效前的事件回调。

**说明：**

1.正常时序依次为：onWillAppear>>onDidAppear>>onWillDisappear>>onDidDisappear。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

onDidDisappear20+Callback<void>否是

菜单消失后的事件回调。

**说明：**

1.正常时序依次为：onWillAppear>>onDidAppear>>onWillDisappear>>onDidDisappear。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

#### ActionMenuSuccessResponse

操作菜单的响应结果。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明indexnumber否否选中按钮在buttons数组中的索引，从0开始。

#### CommonState20+枚举说明

自定义弹窗的状态。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称值说明UNINITIALIZED0未初始化，控制器未与dialog绑定时。INITIALIZED1已初始化，控制器与dialog绑定后。APPEARING2显示中，dialog显示动画过程中。APPEARED3已显示，dialog显示动画结束。DISAPPEARING4消失中，dialog消失动画过程中。DISAPPEARED5已消失，dialog消失动画结束后。

#### DialogController18+

自定义弹窗控制器，继承自[CommonController](#ZH-CN_TOPIC_0000002529284783__commoncontroller18)。

DialogController可作为UIContext弹出自定义弹窗的成员变量，具体用法可看[openCustomDialogWithController](Class (PromptAction).md#ZH-CN_TOPIC_0000002529444747__opencustomdialogwithcontroller18)和[presentCustomDialog](Class (PromptAction).md#ZH-CN_TOPIC_0000002529444747__presentcustomdialog18)示例。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

#### CommonController18+

公共控制器，可以控制promptAction相关组件。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

#### constructor18+

constructor()

控制器的构造函数。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

#### close18+

close(): void

关闭显示的自定义弹窗，若已关闭，则不生效。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

#### getState20+

getState(): CommonState

获取自定义弹窗的状态。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

类型说明[CommonState](#ZH-CN_TOPIC_0000002529284783__commonstate20枚举说明)返回对应的弹窗状态。

#### LevelOrder18+

弹窗层级，可以控制弹窗显示的顺序。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

#### clamp18+

static clamp(order: number): LevelOrder

创建指定顺序的弹窗层级。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明ordernumber是弹窗显示顺序。取值范围为[-100000.0, 100000.0]，如果值小于-100000.0则设置为-100000.0，如果值大于100000.0则设置为100000.0。

**返回值：**

类型说明[LevelOrder](#ZH-CN_TOPIC_0000002529284783__levelorder18)返回当前对象实例。

#### getOrder18+

getOrder(): number

获取弹窗显示顺序。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

类型说明number返回显示顺序数值。

#### DialogOptions18+

自定义弹窗的内容，继承自[BaseDialogOptions](#ZH-CN_TOPIC_0000002529284783__basedialogoptions11)。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明backgroundColor[ResourceColor](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否是

设置弹窗背板颜色。

默认值：Color.Transparent

**说明：**

backgroundColor会与模糊属性backgroundBlurStyle叠加产生效果，如果不符合预期，可将backgroundBlurStyle设置为BlurStyle.NONE，即可取消模糊。

cornerRadius[DialogOptionsCornerRadius](#ZH-CN_TOPIC_0000002529284783__dialogoptionscornerradius18)否是

设置弹窗背板的圆角半径。

可分别设置4个圆角的半径。

默认值：{ topLeft: '32vp', topRight: '32vp', bottomLeft: '32vp', bottomRight: '32vp' }

圆角大小受组件尺寸限制，最大值为组件宽或高的一半，若值为负，则按照默认值处理。

百分比参数方式：以父元素弹窗宽和高的百分比来设置弹窗的圆角。

borderWidth[DialogOptionsBorderWidth](#ZH-CN_TOPIC_0000002529284783__dialogoptionsborderwidth18)否是

设置弹窗背板的边框宽度。

可分别设置4个边框宽度。

默认值：0

单位：vp

百分比参数方式：以父元素弹窗宽的百分比来设置弹窗的边框宽度。

当弹窗左边框和右边框大于弹窗宽度，弹窗上边框和下边框大于弹窗高度，显示可能不符合预期。

borderColor[DialogOptionsBorderColor](#ZH-CN_TOPIC_0000002529284783__dialogoptionsbordercolor18)否是

设置弹窗背板的边框颜色。

默认值：Color.Black

如果使用borderColor属性，需要和borderWidth属性一起使用。

borderStyle[DialogOptionsBorderStyle](#ZH-CN_TOPIC_0000002529284783__dialogoptionsborderstyle18)否是

设置弹窗背板的边框样式。

默认值：BorderStyle.Solid。

如果使用borderStyle属性，需要和borderWidth属性一起使用。

width[Dimension](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__dimension10)否是

设置弹窗背板的宽度。

**说明：**

- 默认最大值：400vp

- 百分比参数方式：弹窗参考宽度基于所在窗口宽度调整。

height[Dimension](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__dimension10)否是

设置弹窗背板的高度。

**说明：**

- 默认最大值：0.9 *（窗口高度 - 安全区域）。

- 百分比参数方式：弹窗参考高度为（窗口高度 - 安全区域），在此基础上调小或调大。

shadow[DialogOptionsShadow](#ZH-CN_TOPIC_0000002529284783__dialogoptionsshadow18)否是

设置弹窗背板的阴影。

当设备为2in1时，默认场景下获焦阴影值为ShadowStyle.OUTER_FLOATING_MD，失焦为ShadowStyle.OUTER_FLOATING_SM。其他设备默认无阴影。

backgroundBlurStyle[BlurStyle](背景设置.md#ZH-CN_TOPIC_0000002529444791__blurstyle9)否是

弹窗背板模糊材质。

默认值：BlurStyle.COMPONENT_ULTRA_THICK

**说明：**

设置为BlurStyle.NONE即可关闭背景虚化。当设置了backgroundBlurStyle为非NONE值时，则不要设置backgroundColor，否则颜色显示将不符合预期效果。

#### DialogOptionsCornerRadius18+

type DialogOptionsCornerRadius = Dimension | BorderRadiuses

表示弹窗背板的圆角半径允许的数据字段类型。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

类型说明[Dimension](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__dimension10)表示值类型为长度类型，用于描述尺寸单位。[BorderRadiuses](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__borderradiuses9)表示值类型为圆角类型，用于描述组件边框圆角半径。

#### DialogOptionsBorderWidth18+

type DialogOptionsBorderWidth = Dimension | EdgeWidths

表示弹窗背板的边框宽度允许的数据字段类型。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

类型说明[Dimension](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__dimension10)表示值类型为长度类型，用于描述尺寸单位。[EdgeWidths](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__edgewidths9)表示值类型为边框宽度类型，用于描述组件边框不同方向的宽度。

#### DialogOptionsBorderColor18+

type DialogOptionsBorderColor = ResourceColor | EdgeColors

表示弹窗背板的边框颜色允许的数据字段类型。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

类型说明[ResourceColor](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)表示值类型为颜色类型，用于描述资源颜色类型。[EdgeColors](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__edgecolors9)表示值类型为边框颜色，用于描述组件边框四条边的颜色。

#### DialogOptionsBorderStyle18+

type DialogOptionsBorderStyle = BorderStyle | EdgeStyles

表示弹窗背板的边框样式允许的数据字段类型。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

类型说明[BorderStyle](枚举说明.md#ZH-CN_TOPIC_0000002529284967__borderstyle)表示值类型为边框类型，用于描述组件边框的类型。[EdgeStyles](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__edgestyles9)表示值类型为边框样式，用于描述组件边框四条边的样式。

#### DialogOptionsShadow18+

type DialogOptionsShadow = ShadowOptions | ShadowStyle

表示弹窗背板的阴影允许的数据字段类型。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

类型说明[ShadowOptions](图像效果.md#ZH-CN_TOPIC_0000002497444856__shadowoptions对象说明)表示值类型为阴影属性集合，用于设置阴影的模糊半径、阴影的颜色、X轴和Y轴的偏移量。[ShadowStyle](图像效果.md#ZH-CN_TOPIC_0000002497444856__shadowstyle10枚举说明)表示值类型为阴影类型，用于描述阴影的类型。

#### CustomDialogOptions11+

自定义弹窗的内容，继承自[BaseDialogOptions](#ZH-CN_TOPIC_0000002529284783__basedialogoptions11)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明builder[CustomBuilder](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__custombuilder8)否否

设置自定义弹窗的内容。

**说明：**

builder需要赋值为箭头函数，格式如下：() => { this.XXX() }，其中XXX是内部builder名。

全局builder需要在组件内部创建，并在内部builder中调用。

builder根节点宽高百分比相对弹窗容器大小。

builder非根节点宽高百分比相对父节点大小。

backgroundColor 12+[ResourceColor](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否是

设置弹窗背板颜色。

默认值：Color.Transparent

**说明：**

当设置了backgroundColor为非透明色时，backgroundBlurStyle需要设置为BlurStyle.NONE，否则颜色显示将不符合预期效果。

cornerRadius12+[Dimension](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__dimension10) | [BorderRadiuses](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__borderradiuses9)否是

设置背板的圆角半径。

可分别设置4个圆角的半径。

默认值：{ topLeft: '32vp', topRight: '32vp', bottomLeft: '32vp', bottomRight: '32vp' }

圆角大小受组件尺寸限制，最大值为组件宽或高的一半，若值为负，则按照默认值处理。

百分比参数方式：以父元素弹窗宽和高的百分比来设置弹窗的圆角。

borderWidth12+[Dimension](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__dimension10) | [EdgeWidths](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__edgewidths9)否是

设置弹窗背板的边框宽度。

可分别设置4个边框宽度。

默认值：0

单位：vp

百分比参数方式：以父元素弹窗宽的百分比来设置弹窗的边框宽度。

当弹窗左边框和右边框大于弹窗宽度，弹窗上边框和下边框大于弹窗高度，显示可能不符合预期。

borderColor12+[ResourceColor](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor) | [EdgeColors](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__edgecolors9)否是

设置弹窗背板的边框颜色。

默认值：Color.Black

如果使用borderColor属性，需要和borderWidth属性一起使用。

borderStyle12+[BorderStyle](枚举说明.md#ZH-CN_TOPIC_0000002529284967__borderstyle) | [EdgeStyles](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__edgestyles9)否是

设置弹窗背板的边框样式。

默认值：BorderStyle.Solid

如果使用borderStyle属性，需要和borderWidth属性一起使用。

width12+[Dimension](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__dimension10)否是

设置弹窗背板的宽度。

**说明：**

- 弹窗宽度默认最大值：400vp

- 百分比参数方式：弹窗参考宽度基于所在窗口的宽度的基础上调整。

height12+[Dimension](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__dimension10)否是

设置弹窗背板的高度。

**说明：**

- 弹窗高度默认最大值：0.9 *（窗口高度 - 安全区域）。

- 百分比参数方式：弹窗参考高度为（窗口高度 - 安全区域），在此基础上调小或调大。

shadow12+[ShadowOptions](图像效果.md#ZH-CN_TOPIC_0000002497444856__shadowoptions对象说明) | [ShadowStyle](图像效果.md#ZH-CN_TOPIC_0000002497444856__shadowstyle10枚举说明)否是

设置弹窗背板的阴影。

当设备为2in1时，默认场景下获焦阴影值为ShadowStyle.OUTER_FLOATING_MD，失焦为ShadowStyle.OUTER_FLOATING_SM。其他设备默认无阴影。

backgroundBlurStyle12+[BlurStyle](背景设置.md#ZH-CN_TOPIC_0000002529444791__blurstyle9)否是

弹窗背板模糊材质。

默认值：BlurStyle.COMPONENT_ULTRA_THICK

**说明：**

设置为BlurStyle.NONE即可关闭背景虚化。当设置了backgroundBlurStyle为非NONE值时，则不要设置backgroundColor，否则颜色显示将不符合预期效果。

#### BaseDialogOptions11+

弹窗的选项。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明maskRect[Rectangle](警告弹窗 (AlertDialog).md#ZH-CN_TOPIC_0000002529444899__rectangle8类型说明)否是

弹窗遮蔽层区域。

默认值：{ x: 0, y: 0, width: '100%', height: '100%' }

**说明：**

showInSubWindow为true时，maskRect不生效。

maskRect在设置[Rectangle](警告弹窗 (AlertDialog).md#ZH-CN_TOPIC_0000002529444899__rectangle8类型说明)中的部分属性后，若未设置其余的属性，则其余属性的默认值为0。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

alignment[DialogAlignment](警告弹窗 (AlertDialog).md#ZH-CN_TOPIC_0000002529444899__dialogalignment枚举说明)否是

弹窗在竖直方向上的对齐方式。

默认值：DialogAlignment.Default

**说明：**

若在UIExtension中设置showInSubWindow为true, 弹窗将基于UIExtension的宿主窗口对齐。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

offset[Offset](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__offset)否是

弹窗相对alignment所在位置的偏移量。

默认值：{ dx: 0 , dy: 0 }

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

isModalboolean否是

弹窗是否为模态窗口。值为true表示为模态窗口且有蒙层，不可与弹窗周围其他控件进行交互，即蒙层区域无法事件透传。值为false表示为非模态窗口且无蒙层，可以与弹窗周围其他控件进行交互。

默认值：true

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

showInSubWindowboolean否是

某弹窗需要显示在主窗口之外时，是否在子窗口显示此弹窗。值为true表示在子窗口显示弹窗。

默认值：false，弹窗显示在应用内，而非独立子窗口。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

onWillDismiss12+Callback<[DismissDialogAction](#ZH-CN_TOPIC_0000002529284783__dismissdialogaction12)>否是

交互式关闭回调函数。

**说明：**

1.当用户执行点击遮障层关闭、侧滑（左滑/右滑）、三键back、键盘ESC关闭交互操作时，如果注册该回调函数，则不会立刻关闭弹窗。在回调函数中可以通过reason得到阻拦关闭弹窗的操作类型，从而根据原因选择是否能关闭弹窗。当前组件返回的reason中，暂不支持CLOSE_BUTTON的枚举值。

2.在onWillDismiss回调中，不能再做onWillDismiss拦截。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

autoCancel12+boolean否是

点击遮障层时，是否关闭弹窗，true表示关闭弹窗。false表示不关闭弹窗。

默认值：true

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

maskColor12+[ResourceColor](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否是

自定义蒙层颜色。

默认值: 0x33000000

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

transition12+[TransitionEffect](组件内转场 (transition).md#ZH-CN_TOPIC_0000002497604930__transitioneffect10对象说明)否是

设置弹窗显示和退出的过渡效果。

**说明：**

1.如果不设置，则使用默认的显示/退出动效。

2.显示动效中按back键，打断显示动效，执行退出动效，动画效果为显示动效与退出动效的曲线叠加后的效果。

3.退出动效中按back键，不会打断退出动效，退出动效继续执行，继续按back键退出应用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

dialogTransition19+[TransitionEffect](组件内转场 (transition).md#ZH-CN_TOPIC_0000002497604930__transitioneffect10对象说明)否是

设置弹窗内容显示的过渡效果。默认无动效。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

maskTransition19+[TransitionEffect](组件内转场 (transition).md#ZH-CN_TOPIC_0000002497604930__transitioneffect10对象说明)否是

设置蒙层显示的过渡效果。默认无动效。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

onDidAppear12+() => void否是

弹窗弹出后的事件回调。

**说明：**

1.正常时序依次为：onWillAppear>>onDidAppear>>(onDateAccept/onCancel/onDateChange)>>onWillDisappear>>onDidDisappear。

2.在onDidAppear内设置改变弹窗显示效果的回调事件，二次弹出生效。

3.快速点击弹出，消失弹窗时，存在onWillDisappear在onDidAppear前生效。

4. 当弹窗入场动效未完成时关闭弹窗，该回调不会触发。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

onDidDisappear12+() => void否是

弹窗消失后的事件回调。

**说明：**

正常时序依次为：onWillAppear>>onDidAppear>>(onDateAccept/onCancel/onDateChange)>>onWillDisappear>>onDidDisappear。

当弹窗退场动画未完成时（例如：同时触发弹窗关闭和页面切换），该回调不会触发。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

onWillAppear12+() => void否是

弹窗显示动效前的事件回调。

**说明：**

1.正常时序依次为：onWillAppear>>onDidAppear>>(onDateAccept/onCancel/onDateChange)>>onWillDisappear>>onDidDisappear。

2.在onWillAppear内设置改变弹窗显示效果的回调事件，二次弹出生效。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

onWillDisappear12+() => void否是

弹窗退出动效前的事件回调。

**说明：**

1.正常时序依次为：onWillAppear>>onDidAppear>>(onDateAccept/onCancel/onDateChange)>>onWillDisappear>>onDidDisappear。

2.快速点击弹出，消失弹窗时，存在onWillDisappear在onDidAppear前生效。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

keyboardAvoidMode12+[KeyboardAvoidMode](Popup控制.md#ZH-CN_TOPIC_0000002529284839__keyboardavoidmode12枚举说明)否是

用于设置弹窗是否在拉起软键盘时进行自动避让。

默认值：KeyboardAvoidMode.DEFAULT

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

enableHoverMode14+boolean否是

是否响应悬停态，值为true时，响应悬停态。

默认值：false，默认不响应。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

hoverModeArea14+[HoverModeAreaType](半模态转场.md#ZH-CN_TOPIC_0000002497604850__hovermodeareatype14)否是

悬停态下弹窗默认展示区域。

默认值：HoverModeAreaType.BOTTOM_SCREEN

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

backgroundBlurStyleOptions19+[BackgroundBlurStyleOptions](背景设置.md#ZH-CN_TOPIC_0000002529444791__backgroundblurstyleoptions10对象说明)否是

背景模糊效果。默认值请参考BackgroundBlurStyleOptions类型说明。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

backgroundEffect19+[BackgroundEffectOptions](背景设置.md#ZH-CN_TOPIC_0000002529444791__backgroundeffectoptions11)否是

背景效果参数。默认值请参考BackgroundEffectOptions类型说明。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

keyboardAvoidDistance15+[LengthMetrics](Graphics.md#ZH-CN_TOPIC_0000002529444761__lengthmetrics12)否是

弹窗避让键盘后，和键盘之间距离。

**说明：**

- 默认值：16vp

- 默认单位：vp

- 当且仅当keyboardAvoidMode属性设置为DEFAULT时生效。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

levelMode15+[LevelMode](#ZH-CN_TOPIC_0000002529284783__levelmode15枚举说明)否是

设置弹窗显示层级。

**说明：**

- 默认值：LevelMode.OVERLAY

- 当且仅当showInSubWindow属性设置为false时生效。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

levelUniqueId15+number否是

设置页面级弹窗需要显示的层级下的[节点 uniqueId](FrameNode.md#ZH-CN_TOPIC_0000002529284787__getuniqueid12)。

取值范围：大于等于0的数字。

**说明：**

- 当且仅当levelMode属性设置为LevelMode.EMBEDDED时生效。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

immersiveMode15+[ImmersiveMode](#ZH-CN_TOPIC_0000002529284783__immersivemode15枚举说明)否是

设置页面内弹窗蒙层效果。

**说明：**

- 默认值：ImmersiveMode.DEFAULT

- 当且仅当levelMode属性设置为LevelMode.EMBEDDED时生效。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

levelOrder18+[LevelOrder](#ZH-CN_TOPIC_0000002529284783__levelorder18)否是

设置弹窗显示的顺序。

**说明：**

- 默认值：LevelOrder.clamp(0)

- 不支持动态刷新顺序。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

focusable19+boolean否是

设置弹窗是否获取焦点。值为true表示获取焦点，值为false表示不获取焦点。

默认值：true

**说明：**

只有弹出覆盖在当前窗口之上的弹窗才可以获取焦点。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

#### DismissDialogAction12+

Dialog关闭的信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

#### 属性

名称类型只读可选说明dismissCallback<void>否否Dialog关闭回调函数。开发者需要退出时调用，不需要退出时无需调用。reason[DismissReason](Popup控制.md#ZH-CN_TOPIC_0000002529284839__dismissreason12枚举说明)否否Dialog无法关闭原因。根据开发者需求选择不同操作下，Dialog是否关闭。

#### LevelMode15+枚举说明

弹窗显示层级模式。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称值说明OVERLAY0弹窗层级为应用窗口根节点，应用内路由导航切换弹窗不隐藏。EMBEDDED1

弹窗节点为页面内路由/导航下的节点，随路由导航切换，弹窗随页面隐藏。

**说明：**

1. 目前只支持挂载在Page或者[NavDestination](NavDestination.md)节点上，优先挂载在Page节点下，只支持在这两种页面内顶层显示。

2. 该模式下新起的页面可以覆盖在弹窗上，页面返回后该弹窗依旧存在，弹窗内容不会丢失。

3. 该模式下需确保目标页面节点如Page节点已挂载上树，再拉起弹窗，否则弹窗将无法挂载到对应的页面节点内。

#### ImmersiveMode15+枚举说明

页面内弹窗蒙层显示区域模式。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称值说明DEFAULT0弹窗蒙层遵循父节点布局约束进行显示。EXTEND1弹窗蒙层可扩展至覆盖状态栏和导航条。

#### Button

菜单中的菜单项按钮。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明textstring | [Resource](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resource)否否

按钮文本内容。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

colorstring | [Resource](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resource)否否

按钮文本颜色。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

primary12+boolean否是

在弹窗获焦且未进行tab键走焦时，按钮是否默认响应Enter键。多个Button时，只允许一个Button的该字段配置为true，否则所有Button均不响应。多重弹窗可自动获焦连续响应。值为true表示按钮默认响应Enter键，值为false时，按钮不默认响应Enter键。

默认值：false

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

#### 示例

从API version 20开始，该示例实现了在promptAction.DialogController中调用getState获取弹窗当前状态。

```ets
// xxx.ets
import { BusinessError } from '@kit.BasicServicesKit';
import { ComponentContent, promptAction } from '@kit.ArkUI';

@Component
struct CustomDialogExample {
  build() {
    Column() {
      Text('Hello')
        .fontSize(50)
        .fontWeight(FontWeight.Bold)
        .margin({ bottom: 36 })
      Button('点我关闭弹窗')
        .onClick(() => {
          if (this.getDialogController()) {
            this.getDialogController().close();
          }
        })
      Button('点我获取状态')
        .onClick(() => {
          if (this.getDialogController()) {
            let state: promptAction.CommonState = this.getDialogController().getState();
            switch (state) {
              case promptAction.CommonState.UNINITIALIZED: {
                console.info('The dialog state is uninitialized.');
                break;
              }
              case promptAction.CommonState.INITIALIZED: {
                console.info('The dialog state is initialized.');
                break;
              }
              case promptAction.CommonState.APPEARING: {
                console.info('The dialog state is appearing.');
                break;
              }
              case promptAction.CommonState.APPEARED: {
                console.info('The dialog state is appeared.');
                break;
              }
              case promptAction.CommonState.DISAPPEARING: {
                console.info('The dialog state is disappearing.');
                break;
              }
              case promptAction.CommonState.DISAPPEARED: {
                console.info('The dialog state is disappeared.');
                break;
              }
              default: {
                console.info('The dialog state is unknown.');
                break;
              }
            }
          }
        })

    }.backgroundColor('#FFF0F0F0')
  }
}

@Builder
function buildText() {
   CustomDialogExample()
}

@Entry
@Component
struct Index {

  private dialogController: promptAction.DialogController = new promptAction.DialogController()

  build() {
    Row() {
      Column() {
        Button("click me")
          .onClick(() => {
            let uiContext = this.getUIContext();
            let promptAction = uiContext.getPromptAction();
            let contentNode = new ComponentContent(uiContext, wrapBuilder(buildText),
            );

            promptAction.openCustomDialogWithController(contentNode, this.dialogController, {

              transition: TransitionEffect.OPACITY.animation({
                duration: 3000
              })
            }).then(() => {
              console.info('succeeded')
            }).catch((error: BusinessError) => {
              console.error(`OpenCustomDialogWithController args error code is ${error.code}, message is ${error.message}`);
            })
          })
      }
      .width('100%')
      .height('100%')
    }
    .height('100%')
  }
}
```

#### promptAction.showToast(deprecated)

showToast(options: ShowToastOptions): void

创建并显示即时反馈。

-

从API version 9开始支持，从API version 18开始废弃，建议使用[showToast](Class (PromptAction).md#ZH-CN_TOPIC_0000002529444747__showtoast)替代。showToast需先通过[UIContext](Class (UIContext).md)中的[getPromptAction](Class (UIContext).md#ZH-CN_TOPIC_0000002529444749__getpromptaction)方法获取[PromptAction](Class (PromptAction).md)对象，然后通过该对象进行调用。且直接使用showToast可能导致[UI上下文不明确](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-global-interface#ui上下文不明确)的问题。

-

从API version 10开始，可以通过使用[UIContext](Class (UIContext).md)中的[getPromptAction](Class (UIContext).md#ZH-CN_TOPIC_0000002529444749__getpromptaction)方法获取当前UI上下文关联的[PromptAction](Class (PromptAction).md)对象。

-

Toast样式单一，不支持内容的自定义，具体支持能力请参考[ShowToastOptions](#ZH-CN_TOPIC_0000002529284783__showtoastoptions)提供的接口。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明options[ShowToastOptions](#ZH-CN_TOPIC_0000002529284783__showtoastoptions)是Toast选项。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[接口调用异常错误码](接口调用异常错误码.md)。

当返回100001错误码时，可能出现了UI上下文不明确的问题，对此可以使用UIContext中的接口进行替换，详细说明可参考[使用UI上下文接口操作界面](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-global-interface)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed.100001Internal error.

**示例：**

```ets
import { promptAction } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct toastExample {
  build() {
    Column() {
      Button('Show toast').fontSize(20)
        .onClick(() => {
          try {
            promptAction.showToast({
              message: 'Hello World',
              duration: 2000
            });
          } catch (error) {
            let message = (error as BusinessError).message;
            let code = (error as BusinessError).code;
            console.error(`showToast args error code is ${code}, message is ${message}`);
          };
        })
    }.height('100%').width('100%').justifyContent(FlexAlign.Center)
  }
}
```

API version 11及之前Toast样式。

API version 12及之后Toast样式。

#### promptAction.showDialog(deprecated)

showDialog(options: ShowDialogOptions): Promise<ShowDialogSuccessResponse>

创建并显示对话框，对话框通过Promise返回结果。

-

从API version 9开始支持，从API version 18开始废弃，建议使用[showDialog](Class (PromptAction).md#ZH-CN_TOPIC_0000002529444747__showdialog-1)替代。showDialog需先通过[UIContext](Class (UIContext).md)中的[getPromptAction](Class (UIContext).md#ZH-CN_TOPIC_0000002529444749__getpromptaction)方法获取[PromptAction](Class (PromptAction).md)对象，然后通过该对象进行调用。且直接使用showDialog可能导致[UI上下文不明确](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-global-interface#ui上下文不明确)的问题。

-

从API version 10开始，可以通过使用[UIContext](Class (UIContext).md)中的[getPromptAction](Class (UIContext).md#ZH-CN_TOPIC_0000002529444749__getpromptaction)方法获取当前UI上下文关联的[PromptAction](Class (PromptAction).md)对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明options[ShowDialogOptions](#ZH-CN_TOPIC_0000002529284783__showdialogoptions)是对话框选项。

**返回值：**

类型说明Promise<[ShowDialogSuccessResponse](#ZH-CN_TOPIC_0000002529284783__showdialogsuccessresponse)>Promise对象，返回对话框的响应结果。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[接口调用异常错误码](接口调用异常错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed.100001Internal error.

**示例：**

```ets
import { promptAction } from '@kit.ArkUI';

promptAction.showDialog({
  title: 'Title Info',
  message: 'Message Info',
  buttons: [
    {
      text: 'button1',
      color: '#000000'
    },
    {
      text: 'button2',
      color: '#000000'
    }
  ],
})
  .then(data => {
    console.info('showDialog success, click button: ' + data.index);
  })
  .catch((err: Error) => {
    console.info('showDialog error: ' + err);
  })
```

#### promptAction.showDialog(deprecated)

showDialog(options: ShowDialogOptions, callback: AsyncCallback<ShowDialogSuccessResponse>):void

创建并显示对话框，对话框响应结果使用callback异步回调返回。

-

从API version 9开始支持，从API version 18开始废弃，建议使用[showDialog](Class (PromptAction).md#ZH-CN_TOPIC_0000002529444747__showdialog)替代。showDialog需先通过[UIContext](Class (UIContext).md)中的[getPromptAction](Class (UIContext).md#ZH-CN_TOPIC_0000002529444749__getpromptaction)方法获取[PromptAction](Class (PromptAction).md)对象，然后通过该对象进行调用。且直接使用showDialog可能导致[UI上下文不明确](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-global-interface#ui上下文不明确)的问题。

-

从API version 10开始，可以通过使用[UIContext](Class (UIContext).md)中的[getPromptAction](Class (UIContext).md#ZH-CN_TOPIC_0000002529444749__getpromptaction)方法获取当前UI上下文关联的[PromptAction](Class (PromptAction).md)对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明options[ShowDialogOptions](#ZH-CN_TOPIC_0000002529284783__showdialogoptions)是页面显示对话框信息描述。callbackAsyncCallback<[ShowDialogSuccessResponse](#ZH-CN_TOPIC_0000002529284783__showdialogsuccessresponse)>是回调函数。弹出对话框成功，err为undefined，data为获取到的对话框响应结果，否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[接口调用异常错误码](接口调用异常错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed.100001Internal error.

**示例：**

```ets
import { promptAction } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  promptAction.showDialog({
    title: 'showDialog Title Info',
    message: 'Message Info',
    buttons: [
      {
        text: 'button1',
        color: '#000000'
      },
      {
        text: 'button2',
        color: '#000000'
      }
    ]
  }, (err, data) => {
    if (err) {
      console.info('showDialog err: ' + err);
      return;
    }
    console.info('showDialog success callback, click button: ' + data.index);
  });
} catch (error) {
  let message = (error as BusinessError).message;
  let code = (error as BusinessError).code;
  console.error(`showDialog args error code is ${code}, message is ${message}`);
};
```

当弹窗的showInSubWindow属性为true时，弹窗可显示在窗口外。

```ets
import { promptAction } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  promptAction.showDialog({
    title: 'showDialog Title Info',
    message: 'Message Info',
    isModal: true,
    showInSubWindow: true,
    buttons: [
      {
        text: 'button1',
        color: '#000000'
      },
      {
        text: 'button2',
        color: '#000000'
      }
    ]
  }, (err, data) => {
    if (err) {
      console.info('showDialog err: ' + err);
      return;
    }
    console.info('showDialog success callback, click button: ' + data.index);
  });
} catch (error) {
  let message = (error as BusinessError).message;
  let code = (error as BusinessError).code;
  console.error(`showDialog args error code is ${code}, message is ${message}`);
};
```

从API version 19开始，该示例通过调用[ShowDialogOptions](#ZH-CN_TOPIC_0000002529284783__showdialogoptions)中的onDidAppear、onDidDisappear、onWillAppear和onWillDisappear属性展示了弹窗生命周期的相关接口的使用方法。

```ets
// xxx.ets
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct DialogExample {
  @State log: string = 'Log information:';
  build() {
    Column() {
      Button('showDialog')
        .onClick(() => {
          this.showCustomDialog();
        })
      Text(this.log).fontSize(30).margin({ top: 200 })
    }.width('100%').margin({ top: 5 })
  }

  showCustomDialog() {
    try {
      this.getUIContext().getPromptAction().showDialog({
        title: '操作确认',
        message: '您确定要执行此操作吗？',
        alignment: DialogAlignment.Bottom,
        buttons: [
          {
            text: '取消',
            color: '#999999'
          },
          {
            text: '确定',
            color: '#007DFF'
          }
        ],
        onDidAppear: () => {
          this.log += '# onDidAppear';
          console.info("showDialog,is onDidAppear!");
        },
        onDidDisappear: () => {
          this.log += '# onDidDisappear';
          console.info("showDialog,is onDidDisappear!");
        },
        onWillAppear: () => {
          this.log = 'Log information:#onWillAppear';
          console.info("showDialog,is onWillAppear!");
        },
        onWillDisappear: () => {
          this.log += '# onWillDisappear';
          console.info("showDialog,is onWillDisappear!");
        },
      })
    } catch (error) {
      let err: BusinessError = error as BusinessError;
      console.error(`捕获到异常: ${err.code}, ${err.message}`);
    }
  }
}
```

#### promptAction.showActionMenu(deprecated)

showActionMenu(options: ActionMenuOptions, callback: AsyncCallback<ActionMenuSuccessResponse>):void

创建并显示操作菜单，菜单响应结果使用callback异步回调返回。

-

从API version 9开始支持，从API version 18开始废弃，建议使用[showActionMenu](Class (PromptAction).md#ZH-CN_TOPIC_0000002529444747__showactionmenu11)替代。showActionMenu需先通过[UIContext](Class (UIContext).md)中的[getPromptAction](Class (UIContext).md#ZH-CN_TOPIC_0000002529444749__getpromptaction)方法获取[PromptAction](Class (PromptAction).md)对象，然后通过该对象进行调用。且直接使用showActionMenu可能导致[UI上下文不明确](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-global-interface#ui上下文不明确)的问题。

-

从API version 11开始，可以通过使用[UIContext](Class (UIContext).md)中的[getPromptAction](Class (UIContext).md#ZH-CN_TOPIC_0000002529444749__getpromptaction)方法获取当前UI上下文关联的[PromptAction](Class (PromptAction).md)对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full。

**参数：**

参数名类型必填说明options[ActionMenuOptions](#ZH-CN_TOPIC_0000002529284783__actionmenuoptions)是操作菜单选项。callbackAsyncCallback<[ActionMenuSuccessResponse](#ZH-CN_TOPIC_0000002529284783__actionmenusuccessresponse)>是回调函数。弹出操作菜单成功，err为undefined，data为获取到的操作菜单响应结果，否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[接口调用异常错误码](接口调用异常错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed.100001Internal error.

**示例：1**

```ets
import { promptAction } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  promptAction.showActionMenu({
    title: 'Title Info',
    buttons: [
      {
        text: 'item1',
        color: '#666666'
      },
      {
        text: 'item2',
        color: '#000000'
      },
    ]
  }, (err, data) => {
    if (err) {
      console.info('showActionMenu err: ' + err);
      return;
    }
    console.info('showActionMenu success callback, click button: ' + data.index);
  })
} catch (error) {
  let message = (error as BusinessError).message
  let code = (error as BusinessError).code
  console.error(`showActionMenu args error code is ${code}, message is ${message}`);
};
```

**示例：2**

从API version 19开始，该示例通过调用[ActionMenuOptions](#ZH-CN_TOPIC_0000002529284783__actionmenuoptions)中的onDidAppear、onDidDisappear、onWillAppear和onWillDisappear属性展示了操作菜单生命周期相关接口的使用方法。

```ets
import { promptAction } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State isShown: boolean = false
  @State textColor: Color = Color.Black
  @State blueColor: Color = Color.Blue

  @State onWillAppear: boolean = false
  @State onDidAppear: boolean = false
  @State onWillDisappear: boolean = false
  @State onDidDisappear: boolean = false
  build() {
    Column({ space: 50 }) {
      Text('onWillAppear').fontColor(this.onWillAppear ? this.blueColor : this.textColor)
      Text('onDidAppear').fontColor(this.onDidAppear ? this.blueColor : this.textColor)
      Text('onWillDisappear').fontColor(this.onWillDisappear ? this.blueColor : this.textColor)
      Text('onDidDisappear').fontColor(this.onDidDisappear ? this.blueColor : this.textColor)
      Button('click')
        .width(200)
        .height(100)
        .margin(100)
        .fontColor(this.textColor)
        .onClick(() => {
          promptAction.showActionMenu({
            title: 'showActionMenu Title Info',
            buttons: [
              {
                text: 'item1',
                color: '#666666'
              },
              {
                text: 'item2',
                color: '#000000'
              },
            ],
            onWillAppear:() => {
              console.info("promptAction menu cycle life onWillAppear");
              this.onWillAppear = true;
            },
            onDidAppear:() => {
              console.info("promptAction menu cycle life onDidAppear");
              this.onDidAppear = true;
            },
            onWillDisappear:() => {
              this.isShown = false;
              console.info("promptAction menu cycle life onWillDisappear");
              this.onWillDisappear = true;
            },
            onDidDisappear:() => {
              console.info("promptAction menu cycle life onDidDisappear");
              this.onDidDisappear = true;
            }
          })
            .then(data => {
              console.info('showActionMenu success, click button: ' + data.index);
            })
            .catch((err: Error) => {
              console.info('showActionMenu error: ' + err);
            })
        })
    }
    .width('100%')
  }
}
```

#### promptAction.showActionMenu(deprecated)

showActionMenu(options: ActionMenuOptions): Promise<ActionMenuSuccessResponse>

创建并显示操作菜单，菜单响应后通过Promise返回结果。

-

从API version 9开始支持，从API version 18开始废弃，建议使用[showActionMenu](Class (PromptAction).md#ZH-CN_TOPIC_0000002529444747__showactionmenu)替代。showActionMenu需先通过[UIContext](Class (UIContext).md)中的[getPromptAction](Class (UIContext).md#ZH-CN_TOPIC_0000002529444749__getpromptaction)方法获取[PromptAction](Class (PromptAction).md)对象，然后通过该对象进行调用。且直接使用showActionMenu可能导致[UI上下文不明确](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-global-interface#ui上下文不明确)的问题。

-

从API version 10开始，可以通过使用[UIContext](Class (UIContext).md)中的[getPromptAction](Class (UIContext).md#ZH-CN_TOPIC_0000002529444749__getpromptaction)方法获取当前UI上下文关联的[PromptAction](Class (PromptAction).md)对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明options[ActionMenuOptions](#ZH-CN_TOPIC_0000002529284783__actionmenuoptions)是Promise对象，返回菜单的响应结果。

**返回值：**

类型说明Promise<[ActionMenuSuccessResponse](#ZH-CN_TOPIC_0000002529284783__actionmenusuccessresponse)>Promise对象，返回菜单的响应结果。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[接口调用异常错误码](接口调用异常错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed.100001Internal error.

**示例：**

```ets
import { promptAction } from '@kit.ArkUI';

promptAction.showActionMenu({
  title: 'showActionMenu Title Info',
  buttons: [
    {
      text: 'item1',
      color: '#666666'
    },
    {
      text: 'item2',
      color: '#000000'
    },
  ]
})
  .then(data => {
    console.info('showActionMenu success, click button: ' + data.index);
  })
  .catch((err: Error) => {
    console.info('showActionMenu error: ' + err);
  })
```

#### promptAction.openCustomDialog(deprecated)

openCustomDialog(options: CustomDialogOptions): Promise<number>

打开自定义弹窗。通过Promise返回结果。

暂不支持isModal = true与showInSubWindow = true同时使用。如果同时设置为true时，则只生效showInSubWindow = true。

弹窗宽度在设备竖屏时默认为 所在窗口宽度 - 左右margin（16vp，设备为2in1时为40vp），最大默认宽度为400vp。

-

从API version 11开始支持，从API version 18开始废弃，建议使用[openCustomDialog](Class (PromptAction).md#ZH-CN_TOPIC_0000002529444747__opencustomdialog12-1)替代。openCustomDialog需先通过[UIContext](Class (UIContext).md)中的[getPromptAction](Class (UIContext).md#ZH-CN_TOPIC_0000002529444749__getpromptaction)方法获取[PromptAction](Class (PromptAction).md)对象，然后通过该对象进行调用。且直接使用openCustomDialog可能导致[UI上下文不明确](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-global-interface#ui上下文不明确)的问题。

-

从API version 12开始，可以通过使用[UIContext](Class (UIContext).md)中的[getPromptAction](Class (UIContext).md#ZH-CN_TOPIC_0000002529444749__getpromptaction)方法获取当前UI上下文关联的[PromptAction](Class (PromptAction).md)对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明options[CustomDialogOptions](#ZH-CN_TOPIC_0000002529284783__customdialogoptions11)是自定义弹窗的内容。

**返回值：**

类型说明Promise<number>返回供closeCustomDialog使用的对话框id。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[接口调用异常错误码](接口调用异常错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed.100001Internal error.

**示例：**

```ets
import { promptAction } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  private customDialogComponentId: number = 0;

  @Builder
  customDialogComponent() {
    Column() {
      Text('弹窗').fontSize(30)
      Row({ space: 50 }) {
        Button("确认").onClick(() => {
          try {
            promptAction.closeCustomDialog(this.customDialogComponentId)
          } catch (error) {
            let message = (error as BusinessError).message;
            let code = (error as BusinessError).code;
            console.error(`closeCustomDialog error code is ${code}, message is ${message}`);
          }
        })
        Button("取消").onClick(() => {
          try {
            promptAction.closeCustomDialog(this.customDialogComponentId)
          } catch (error) {
            let message = (error as BusinessError).message;
            let code = (error as BusinessError).code;
            console.error(`closeCustomDialog error code is ${code}, message is ${message}`);
          }
        })
      }
    }.height(200).padding(5).justifyContent(FlexAlign.SpaceBetween)
  }

  build() {
    Row() {
      Column({ space: 20 }) {
        Text('组件内弹窗')
          .fontSize(30)
          .onClick(() => {
            promptAction.openCustomDialog({
              builder: () => {
                this.customDialogComponent()
              },
              onWillDismiss: (dismissDialogAction: DismissDialogAction) => {
                console.info('reason' + JSON.stringify(dismissDialogAction.reason));
                console.info('dialog onWillDismiss');
                if (dismissDialogAction.reason == DismissReason.PRESS_BACK) {
                  dismissDialogAction.dismiss();
                }
                if (dismissDialogAction.reason == DismissReason.TOUCH_OUTSIDE) {
                  dismissDialogAction.dismiss();
                }
              }
            }).then((dialogId: number) => {
              this.customDialogComponentId = dialogId;
            })
              .catch((error: BusinessError) => {
                console.error(`openCustomDialog error code is ${error.code}, message is ${error.message}`);
              })
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

该示例定义了弹窗样式，如宽度、高度、背景色、阴影等。

直接使用openCustomDialog可能导致实例不明确的问题，建议使用[UIContext](Class (UIContext).md)中的[getPromptAction](Class (UIContext).md#ZH-CN_TOPIC_0000002529444749__getpromptaction)获取[PromptAction](Class (PromptAction).md)对象，再通过此对象调用替代方法[openCustomDialog](Class (PromptAction).md#ZH-CN_TOPIC_0000002529444747__opencustomdialog12-1)。

```ets
import { LevelMode, ImmersiveMode } from '@kit.ArkUI';

let customDialogId: number = 0;

@Builder
function customDialogBuilder(uiContext: UIContext) {
  Column() {
    Text('Custom dialog Message').fontSize(10)
    Row() {
      Button("确认").onClick(() => {
        uiContext.getPromptAction().closeCustomDialog(customDialogId);
      })
      Blank().width(50)
      Button("取消").onClick(() => {
        uiContext.getPromptAction().closeCustomDialog(customDialogId);
      })
    }
  }
}

@Entry
@Component
struct Index {
  @State message: string = 'Hello World';
  private uiContext: UIContext = this.getUIContext();

  @Builder
  customDialogComponent() {
    customDialogBuilder(this.uiContext)
  }

  build() {
    Row() {
      Column() {
        Text(this.message).id("test_text")
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
          .onClick(() => {
            const node: FrameNode | null = this.uiContext.getFrameNodeById("test_text") || null;
            this.uiContext.getPromptAction().openCustomDialog({
              builder: () => {
                this.customDialogComponent()
              },
              keyboardAvoidMode: KeyboardAvoidMode.NONE,
              showInSubWindow: false,
              offset: { dx: 5, dy: 5 },
              backgroundColor: 0xd9ffffff,
              cornerRadius: 20,
              width: '80%',
              height: 200,
              borderWidth: 1,
              borderStyle: BorderStyle.Dashed, // 使用borderStyle属性，需要和borderWidth属性一起使用
              borderColor: Color.Blue, // 使用borderColor属性，需要和borderWidth属性一起使用
              shadow: ({
                radius: 20,
                color: Color.Grey,
                offsetX: 50,
                offsetY: 0
              }),
              levelMode: LevelMode.EMBEDDED,
              levelUniqueId: node?.getUniqueId(),
              immersiveMode: ImmersiveMode.DEFAULT,
            }).then((dialogId: number) => {
              customDialogId = dialogId;
            })
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

该示例实现了一个页面内的弹窗。

直接使用openCustomDialog可能导致实例不明确的问题，建议使用[UIContext](Class (UIContext).md)中的[getPromptAction](Class (UIContext).md#ZH-CN_TOPIC_0000002529444749__getpromptaction)获取[PromptAction](Class (PromptAction).md)对象，再通过此对象调用替代方法[openCustomDialog](Class (PromptAction).md#ZH-CN_TOPIC_0000002529444747__opencustomdialog12-1)。

```ets
// Index.ets
import { LevelMode, ImmersiveMode } from '@kit.ArkUI';

let customDialogId: number = 0;

@Builder
function customDialogBuilder(uiContext: UIContext) {
  Column() {
    Text('Custom dialog Message').fontSize(10).height(100)
    Row() {
      Button("Next").onClick(() => {
        uiContext.getRouter().pushUrl({ url: 'pages/Next' });
      })
      Blank().width(50)
      Button("Close").onClick(() => {
        uiContext.getPromptAction().closeCustomDialog(customDialogId);
      })
    }
  }.padding(20)
}

@Entry
@Component
struct Index {
  @State message: string = 'Hello World';
  private uiContext: UIContext = this.getUIContext();

  @Builder
  customDialogComponent() {
    customDialogBuilder(this.uiContext)
  }

  build() {
    Row() {
      Column() {
        Text(this.message).id("test_text")
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
          .onClick(() => {
            const node: FrameNode | null = this.uiContext.getFrameNodeById("test_text") || null;
            this.uiContext.getPromptAction().openCustomDialog({
              builder: () => {
                this.customDialogComponent()
              },
              levelMode: LevelMode.EMBEDDED,
              levelUniqueId: node?.getUniqueId(),
              immersiveMode: ImmersiveMode.DEFAULT,
            }).then((dialogId: number) => {
              customDialogId = dialogId;
            })
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

```ets
// Next.ets
@Entry
@Component
struct Next {
  @State message: string = 'Back';

  build() {
    Row() {
      Column() {
        Button(this.message)
          .onClick(() => {
            this.getUIContext().getRouter().back();
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

#### promptAction.closeCustomDialog(deprecated)

closeCustomDialog(dialogId: number): void

关闭自定义弹窗。

-

从API version 11开始支持，从API version 18开始废弃，建议使用[closeCustomDialog](Class (PromptAction).md#ZH-CN_TOPIC_0000002529444747__closecustomdialog12-1)替代。closeCustomDialog需先通过[UIContext](Class (UIContext).md)中的[getPromptAction](Class (UIContext).md#ZH-CN_TOPIC_0000002529444749__getpromptaction)方法获取[PromptAction](Class (PromptAction).md)对象，然后通过该对象进行调用。且直接使用closeCustomDialog可能导致[UI上下文不明确](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-global-interface#ui上下文不明确)的问题。

-

从API version 12开始，可以通过使用[UIContext](Class (UIContext).md)中的[getPromptAction](Class (UIContext).md#ZH-CN_TOPIC_0000002529444749__getpromptaction)方法获取当前UI上下文关联的[PromptAction](Class (PromptAction).md)对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明dialogIdnumber是openCustomDialog返回的对话框id。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[接口调用异常错误码](接口调用异常错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed.100001Internal error.

**示例：**

示例请看[promptAction.openCustomDialog](#ZH-CN_TOPIC_0000002529284783__promptactionopencustomdialogdeprecated)的示例。