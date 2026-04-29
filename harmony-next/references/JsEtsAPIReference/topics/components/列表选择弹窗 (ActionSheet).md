# 列表选择弹窗 (ActionSheet)

列表弹窗。

  ![image](public_sys-resources/note_3.0-zh-cn.webp)

从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

本模块功能依赖UI的执行上下文，不可在[UI上下文不明确](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-global-interface#ui上下文不明确)的地方使用，参见[UIContext](Class (UIContext).md)说明。

**ActionSheetOptions对象说明**

列表选择弹窗的样式。

系统能力： SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| title | string | Resource | 否 | 否 | 弹窗标题。 当文本内容过长无法显示时，用省略号代替未显示的部分。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| subtitle10+ | ResourceStr | 否 | 是 | 弹窗副标题。 当文本内容过长无法显示时，用省略号代替未显示的部分。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| message | string | Resource | 否 | 否 | 弹窗内容。 文本超长时会触发滚动条。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| autoCancel | boolean | 否 | 是 | 点击遮障层时，是否关闭弹窗。 默认值：true 值为true时，点击遮障层关闭弹窗，值为false时，点击遮障层不关闭弹窗。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| confirm | ActionSheetButtonOptions | 否 | 是 | 确认Button的使能状态、默认焦点、按钮风格、文本内容和点击回调。在弹窗获焦且未进行tab键走焦时，该按钮默认响应Enter键。多重弹窗情况下，可自动获焦并连续响应。默认响应Enter键能力在defaultFocus为true时不生效。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| cancel | VoidCallback | 否 | 是 | 点击遮障层关闭dialog时的回调。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| alignment | DialogAlignment | 否 | 是 | 弹窗在竖直方向上的对齐方式。 默认值：DialogAlignment.Bottom 元服务API： 从API version 11开始，该接口支持在元服务中使用。 说明： 若在UIExtension中设置showInSubWindow为true，弹窗将基于UIExtension的宿主窗口对齐。 |
| offset | ActionSheetOffset | 否 | 是 | 弹窗相对alignment所在位置的偏移量。 默认值： 1.alignment设置为Top、TopStart、TopEnd时默认值为{dx: 0,dy: "40vp"} 2.alignment设置为其他时默认值为{dx: 0,dy: "-40vp"} 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| sheets | Array<SheetInfo> | 否 | 否 | 设置选项内容，每个选择项支持设置图片、文本和选中的回调。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| maskRect10+ | Rectangle | 否 | 是 | 弹窗遮蔽层区域，在遮蔽层区域内的事件不透传，在遮蔽层区域外的事件透传。 默认值：{ x: 0, y: 0, width: '100%', height: '100%' } 说明： showInSubWindow为true时，maskRect不生效。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| showInSubWindow11+ | boolean | 否 | 是 | 某弹窗需要显示在主窗口之外时，是否在子窗口显示此弹窗。值为true表示在子窗口显示弹窗。 默认值：false，弹窗显示在应用内，而非独立子窗口。 说明： showInSubWindow为true的弹窗无法触发显示另一个showInSubWindow为true的弹窗。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| isModal11+ | boolean | 否 | 是 | 弹窗是否为模态窗口，模态窗口有蒙层，非模态窗口无蒙层。值为false时，弹窗为非模态窗口，无蒙层。 默认值：true，此时弹窗有蒙层。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| backgroundColor11+ | ResourceColor | 否 | 是 | 弹窗背板颜色。 默认值：Color.Transparent 说明： backgroundColor会与模糊属性backgroundBlurStyle叠加产生效果，如果不符合预期，可将backgroundBlurStyle设置为BlurStyle.NONE，即可取消模糊。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| backgroundBlurStyle11+ | BlurStyle | 否 | 是 | 弹窗背板模糊材质。 默认值：BlurStyle.COMPONENT_ULTRA_THICK 说明： 设置为BlurStyle.NONE即可关闭背景虚化。当设置了backgroundBlurStyle为非NONE值时，则不要设置backgroundColor，否则颜色显示将不符合预期效果。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| backgroundBlurStyleOptions19+ | BackgroundBlurStyleOptions | 否 | 是 | 背景模糊效果。默认值请参考BackgroundBlurStyleOptions类型说明。 元服务API： 从API version 19开始，该接口支持在元服务中使用。 |
| backgroundEffect19+ | BackgroundEffectOptions | 否 | 是 | 背景效果参数。默认值请参考BackgroundEffectOptions类型说明。 元服务API： 从API version 19开始，该接口支持在元服务中使用。 |
| onWillDismiss12+ | Callback<DismissDialogAction> | 否 | 是 | 交互式关闭回调函数。 说明： 1.当用户执行点击遮障层关闭、侧滑（左滑/右滑）、三键back、键盘ESC关闭交互操作时，如果注册该回调函数，则不会立刻关闭弹窗。在回调函数中可以通过reason得到阻拦关闭弹窗的操作类型，从而根据原因选择是否能关闭弹窗。当前组件返回的reason中，暂不支持CLOSE_BUTTON的枚举值。 2.在onWillDismiss回调中，不能再做onWillDismiss拦截。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| cornerRadius12+ | Dimension | BorderRadiuses | LocalizedBorderRadiuses | 否 | 是 | 设置背板的圆角半径。 可分别设置4个圆角的半径。 默认值：{ topLeft: '32vp', topRight: '32vp', bottomLeft: '32vp', bottomRight: '32vp' } 圆角大小受组件尺寸限制，最大值为组件宽或高的一半，若值为负，则按照默认值处理。 百分比参数方式：以父元素弹窗宽和高的百分比来设置弹窗的圆角。 说明： 当cornerRadius属性类型为LocalizedBorderRadiuses时，支持随语言习惯改变布局顺序。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| borderWidth12+ | Dimension | EdgeWidths | LocalizedEdgeWidths | 否 | 是 | 设置弹窗背板的边框宽度。 可分别设置4个边框宽度。 默认值：0 百分比参数方式：以父元素弹窗宽的百分比来设置弹窗的边框宽度。 当弹窗左边框和右边框大于弹窗宽度，弹窗上边框和下边框大于弹窗高度，显示可能不符合预期。 说明： 当borderWidth属性类型为LocalizedEdgeWidths时，支持随语言习惯改变布局顺序。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| borderColor12+ | ResourceColor | EdgeColors | LocalizedEdgeColors | 否 | 是 | 设置弹窗背板的边框颜色。 默认值：Color.Black 如果使用borderColor属性，需要和borderWidth属性一起使用。 说明： 当borderColor属性类型为LocalizedEdgeColors时，支持随语言习惯改变布局顺序。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| borderStyle12+ | BorderStyle | EdgeStyles | 否 | 是 | 设置弹窗背板的边框样式。 默认值：BorderStyle.Solid。 如果使用borderStyle属性，需要和borderWidth属性一起使用。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| width12+ | Dimension | 否 | 是 | 设置弹窗背板的宽度。 说明： - 弹窗宽度默认最大值：400vp。 - 百分比参数方式：弹窗参考宽度为所在窗口的宽度，在此基础上调小或调大。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| height12+ | Dimension | 否 | 是 | 设置弹窗背板的高度。 说明： - 弹窗高度默认最大值：0.9 *（窗口高度 - 安全区域）。 - 百分比参数方式：弹窗参考高度为（窗口高度 - 安全区域），在此基础上调小或调大。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| shadow12+ | ShadowOptions | ShadowStyle | 否 | 是 | 设置弹窗背板的阴影。 当设备为2in1时，默认场景下获焦阴影值为ShadowStyle.OUTER_FLOATING_MD，失焦为ShadowStyle.OUTER_FLOATING_SM。其他设备默认无阴影。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| transition12+ | TransitionEffect | 否 | 是 | 设置弹窗显示和退出的过渡效果。 说明： 1.如果不设置，则使用默认的显示/退出动效。 2.显示动效中按back键，打断显示动效，执行退出动效，动画效果为显示动效与退出动效的曲线叠加后的效果。 3.退出动效中按back键，不会打断退出动效，退出动效继续执行，继续按back键退出应用。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| enableHoverMode14+ | boolean | 否 | 是 | 是否响应悬停态，值为true表示响应悬停态。 默认值：false，默认不响应。 元服务API： 从API version 14开始，该接口支持在元服务中使用。 |
| hoverModeArea14+ | HoverModeAreaType | 否 | 是 | 悬停态下弹窗默认展示区域。 默认值：HoverModeAreaType.BOTTOM_SCREEN。 元服务API： 从API version 14开始，该接口支持在元服务中使用。 |
| onWillAppear19+ | Callback<void> | 否 | 是 | 弹窗显示动效前的事件回调。 说明： 1.正常时序依次为：onWillAppear >> onDidAppear >> onWillDisappear >> onDidDisappear。 2.在onWillAppear内设置改变弹窗显示效果的回调事件，二次弹出生效。 元服务API： 从API version 19开始，该接口支持在元服务中使用。 |
| onDidAppear19+ | Callback<void> | 否 | 是 | 弹窗弹出后的事件回调。 说明： 1.正常时序依次为：onWillAppear >> onDidAppear >> onWillDisappear >> onDidDisappear。 2.在onDidAppear内设置改变弹窗显示效果的回调事件，二次弹出生效。 3.快速点击弹出，关闭弹窗时，onWillDisappear在onDidAppear前生效。 4.弹窗入场动效未完成时彻底关闭弹窗，动效打断，onDidAppear不会触发。 元服务API： 从API version 19开始，该接口支持在元服务中使用。 |
| onWillDisappear19+ | Callback<void> | 否 | 是 | 弹窗退出动效前的事件回调。 说明： 正常时序依次为：onWillAppear >> onDidAppear >> onWillDisappear >> onDidDisappear。 元服务API： 从API version 19开始，该接口支持在元服务中使用。 |
| onDidDisappear19+ | Callback<void> | 否 | 是 | 弹窗消失后的事件回调。 说明： 正常时序依次为：onWillAppear >> onDidAppear >> onWillDisappear >> onDidDisappear。 元服务API： 从API version 19开始，该接口支持在元服务中使用。 |
| levelMode15+ | LevelMode | 否 | 是 | 设置弹窗显示层级。 说明： - 默认值：LevelMode.OVERLAY - 仅当showInSubWindow属性设置为false时生效。 元服务API： 从API version 15开始，该接口支持在元服务中使用。 |
| levelUniqueId15+ | number | 否 | 是 | 设置页面级弹窗需要显示的层级下的节点 uniqueId。 取值范围：大于等于0的数字。 说明： - 当且仅当levelMode属性设置为LevelMode.EMBEDDED时生效。 元服务API： 从API version 15开始，该接口支持在元服务中使用。 |
| immersiveMode15+ | ImmersiveMode | 否 | 是 | 设置页面内弹窗蒙层效果。 说明： - 默认值：ImmersiveMode.DEFAULT - 当且仅当levelMode属性设置为LevelMode.EMBEDDED时生效。 元服务API： 从API version 15开始，该接口支持在元服务中使用。 |
| levelOrder18+ | LevelOrder | 否 | 是 | 设置弹窗显示的顺序。 说明： - 默认值：LevelOrder.clamp(0) - 不支持动态刷新顺序。 元服务API： 从API version 18开始，该接口支持在元服务中使用。 |

**SheetInfo对象说明**

弹窗中的选项内容，每一项支持设置文本、图标以及选中的回调。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| title | string | Resource | 否 | 否 | 选项的文本内容。 文本超长时会触发滚动条。 |
| icon | string | Resource | 否 | 是 | 选项的图标，默认无图标显示。 string格式可用于加载网络图片和本地图片，常用于加载网络图片。当使用相对路径引用本地图片时，例如Image("common/test.jpg")。 |
| action | VoidCallback | 否 | 否 | 选项选中的回调。 |

**LevelMode15+**

type LevelMode = LevelMode

弹窗的显示层级。

元服务API： 从API version 15开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| LevelMode | 设置弹窗的显示层级。 |

**ImmersiveMode15+**

type ImmersiveMode = ImmersiveMode

弹窗的蒙层效果。

元服务API： 从API version 15开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| ImmersiveMode | 设置页面内弹窗的蒙层效果。 |

**DismissDialogAction12+**

Dialog关闭的信息。

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

**属性**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| dismiss | Callback<void> | 否 | 否 | Dialog关闭回调函数。开发者需要退出时调用，不需要退出时无需调用。 |
| reason | DismissReason | 否 | 否 | Dialog无法关闭原因。根据开发者需求选择不同操作下，Dialog是否关闭。 |

**ActionSheetButtonOptions18+对象说明**

弹窗中按钮的样式。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

为规范匿名对象的定义，API 18版本修改了此处的元素定义。其中，保留了历史匿名对象的起始版本信息，会出现外层元素@since版本号高于内层元素版本号的情况，但这不影响接口的使用。

元服务API： 从API version 18开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| enabled10+ | boolean | 否 | 是 | 点击Button是否响应，true表示Button可以响应，false表示Button不可以响应。 默认值：true 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| defaultFocus10+ | boolean | 否 | 是 | 设置Button是否是默认焦点，true表示Button是默认焦点，false表示Button不是默认焦点。 默认值：false 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| style10+ | DialogButtonStyle | 否 | 是 | 设置Button的风格样式。 默认值：DialogButtonStyle.DEFAULT 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| value8+ | string | Resource | 否 | 否 | Button文本内容。 当文本内容过长无法显示时，用省略号代替未显示的部分。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| action8+ | VoidCallback | 否 | 否 | Button选中时的回调。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |

**ActionSheetOffset18+对象说明**

弹窗的对齐方式。

元服务API： 从API version 18开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| dx | number | string | Resource | 否 | 否 | 弹出窗口相对于对齐位置dx的偏移量。 需要显式指定像素单位，如'10px'，也可设置百分比字符串，如'100%'。 说明： 不指定像素单位时，默认单位vp，如'10'，等同于10。 |
| dy | number | string | Resource | 否 | 否 | 弹出窗口相对于对齐位置dy的偏移量。 需要显式指定像素单位，如'10px'，也可设置百分比字符串，如'100%'。 说明： 不指定像素单位时，默认单位vp，如'10'，等同于10。 |

**ActionSheet**

**show(deprecated)**

static show(value: ActionSheetOptions)

定义列表弹窗并弹出。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

从API version 8开始支持，从API version 18开始废弃，建议使用[showActionSheet](Class (UIContext).md#ZH-CN_TOPIC_0000002522240732__showactionsheet)替代。showActionSheet需先获取[UIContext](Class (UIContext).md)实例后再进行调用。

从API version 10开始，可以通过使用[UIContext](Class (UIContext).md)中的[showActionSheet](Class (UIContext).md#ZH-CN_TOPIC_0000002522240732__showactionsheet)来明确UI的执行上下文。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | ActionSheetOptions | 是 | 配置列表选择弹窗的参数。 |

**示例**

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

直接使用ActionSheet可能导致实例不明确的问题，建议使用getUIContext()获取[UIContext](Class (UIContext).md)实例，并使用[showActionSheet](Class (UIContext).md#ZH-CN_TOPIC_0000002522240732__showactionsheet)调用绑定实例的ActionSheet.show()。

**示例1（弹出列表选择弹窗）**

该示例通过点击按钮弹窗列表选择弹窗。

```ets
// xxx.ets
@Entry
@Component
struct ActionSheetExample {
  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Button('Click to Show ActionSheet')
        .onClick(() => {
          this.getUIContext().showActionSheet({
            title: 'ActionSheet title',
            subtitle: 'ActionSheet subtitle',
            message: 'message',
            autoCancel: true,
            confirm: {
              defaultFocus: true,
              value: 'Confirm button',
              action: () => {
                console.info('Get ActionSheet handled');
              }
            },
            cancel: () => {
              console.info('ActionSheet canceled');
            },
            onWillDismiss: (dismissDialogAction: DismissDialogAction) => {
              console.info(`reason= ${dismissDialogAction.reason}`);
              console.info('ActionSheet onWillDismiss');
              if (dismissDialogAction.reason === DismissReason.PRESS_BACK) {
                dismissDialogAction.dismiss();
              }
              if (dismissDialogAction.reason === DismissReason.TOUCH_OUTSIDE) {
                dismissDialogAction.dismiss();
              }
            },
            alignment: DialogAlignment.Bottom,
            offset: { dx: 0, dy: -10 },
            sheets: [
              {
                title: 'apples',
                action: () => {
                  console.info('apples');
                }
              },
              {
                title: 'bananas',
                action: () => {
                  console.info('bananas');
                }
              },
              {
                title: 'pears',
                action: () => {
                  console.info('pears');
                }
            ]
          })
    }.width('100%')
    .height('100%')
  }
```

![image](public_sys-resources/zh-cn_image_0000002553205263.webp)

**示例2（可在主窗外弹出的弹窗）**

在2in1设备上设置[showInSubWindow](#ZH-CN_TOPIC_0000002522080886__actionsheetoptions对象说明)为true时，可以弹出在主窗外显示的弹窗。

```ets
// xxx.ets
@Entry
@Component
struct ActionSheetExample {
  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Button('Click to Show ActionSheet')
        .onClick(() => {
          this.getUIContext().showActionSheet({
            title: 'ActionSheet title',
            subtitle: 'ActionSheet subtitle',
            message: 'message',
            autoCancel: true,
            showInSubWindow: true,
            isModal: true,
            confirm: {
              defaultFocus: true,
              value: 'Confirm button',
              action: () => {
                console.info('Get ActionSheet handled');
              }
            },
            cancel: () => {
              console.info('ActionSheet canceled');
            },
            onWillDismiss: (dismissDialogAction: DismissDialogAction) => {
              console.info(`reason= ${dismissDialogAction.reason}`);
              console.info('ActionSheet onWillDismiss');
              if (dismissDialogAction.reason === DismissReason.PRESS_BACK) {
                dismissDialogAction.dismiss();
              }
              if (dismissDialogAction.reason === DismissReason.TOUCH_OUTSIDE) {
                dismissDialogAction.dismiss();
              }
            },
            alignment: DialogAlignment.Center,
            offset: { dx: 0, dy: -10 },
            sheets: [
              {
                title: 'apples',
                action: () => {
                  console.info('apples');
                }
              },
              {
                title: 'bananas',
                action: () => {
                  console.info('bananas');
                }
              },
              {
                title: 'pears',
                action: () => {
                  console.info('pears');
                }
            ]
          })
    }.width('100%')
    .height('100%')
  }
```

![image](public_sys-resources/zh-cn_image_0000002522085308.webp)

**示例3（设置弹窗的动画）**

该示例通过配置[transition](#ZH-CN_TOPIC_0000002522080886__actionsheetoptions对象说明)实现弹窗的显示和消失动画。

```ets
// xxx.ets
@Entry
@Component
struct ActionSheetExample {
  build() {
    Column({ space: 5 }) {
      Button('ActionSheet Set Duration')
        .onClick(() => {
          this.getUIContext().showActionSheet({
            title: 'ActionSheet 1',
            message: 'Set Animation Duration open 3 second, close 100 ms',
            autoCancel: true,
            alignment: DialogAlignment.Top,
            transition: TransitionEffect.asymmetric(TransitionEffect.OPACITY
              .animation({ duration: 3000, curve: Curve.Sharp })
              .combine(TransitionEffect.scale({ x: 1.5, y: 1.5 }).animation({ duration: 3000, curve: Curve.Sharp })),
              TransitionEffect.OPACITY.animation({ duration: 100, curve: Curve.Smooth })
                .combine(TransitionEffect.scale({ x: 0.5, y: 0.5 }).animation({ duration: 100, curve: Curve.Smooth }))),
            offset: { dx: 0, dy: -20 },
            confirm: {
              value: 'button',
              action: () => {
                console.info('Button-clicking callback');
              }
            },
            cancel: () => {
              console.info('Closed callbacks');
            },
            sheets: [
              {
                title: 'apples',
                action: () => {
                  console.info('apples');
                }
              },
              {
                title: 'bananas',
                action: () => {
                  console.info('bananas');
                }
              },
              {
                title: 'pears',
                action: () => {
                  console.info('pears');
                }
            ]
          })
        }).backgroundColor(0x317aff).height("88px")
    }.width('100%').margin({ top: 5 })
  }
```

![image](public_sys-resources/zh-cn_image_0000002553365225.webp)

**示例4（设置弹窗的样式）**

该示例定义了ActionSheet的样式，如宽度、高度、背景色、阴影等。

```ets
// xxx.ets
@Entry
@Component
struct ActionSheetExample {
  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center }) {
      Button('Click to Show ActionSheet')
        .onClick(() => {
          this.getUIContext().showActionSheet({
            title: 'ActionSheet title',
            subtitle: 'ActionSheet subtitle',
            message: 'message',
            autoCancel: true,
            width: 300,
            height: 350,
            cornerRadius: 20,
            borderWidth: 1,
            borderStyle: BorderStyle.Solid, //使用borderStyle属性，需要和borderWidth属性一起使用
            borderColor: Color.Blue, //使用borderColor属性，需要和borderWidth属性一起使用
            backgroundColor: Color.White,
            shadow: ({
              radius: 20,
              color: Color.Grey,
              offsetX: 50,
              offsetY: 0
            }),
            confirm: {
              defaultFocus: true,
              value: 'Confirm button',
              action: () => {
                console.info('Get ActionSheet handled');
              }
            },
            cancel: () => {
              console.info('ActionSheet canceled');
            },
            onWillDismiss: (dismissDialogAction: DismissDialogAction) => {
              console.info(`reason= ${dismissDialogAction.reason}`);
              console.info('ActionSheet onWillDismiss');
              if (dismissDialogAction.reason === DismissReason.PRESS_BACK) {
                dismissDialogAction.dismiss();
              }
              if (dismissDialogAction.reason === DismissReason.TOUCH_OUTSIDE) {
                dismissDialogAction.dismiss();
              }
            },
            alignment: DialogAlignment.Bottom,
            offset: { dx: 0, dy: -10 },
            sheets: [
              {
                title: 'apples',
                action: () => {
                  console.info('apples');
                }
              },
              {
                title: 'bananas',
                action: () => {
                  console.info('bananas');
                }
              },
              {
                title: 'pears',
                action: () => {
                  console.info('pears');
                }
            ]
          })
    }.width('100%')
  }
```

![image](public_sys-resources/zh-cn_image_0000002522245302.webp)

**示例5（悬停态弹窗）**

该示例展示了在折叠屏悬停态下设置dialog布局区域的效果。

```ets
// xxx.ets
@Entry
@Component
struct ActionSheetExample {
  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Button('Click to Show ActionSheet')
        .onClick(() => {
          this.getUIContext().showActionSheet({
            title: 'ActionSheet title',
            subtitle: 'ActionSheet subtitle',
            message: 'message',
            autoCancel: true,
            confirm: {
              defaultFocus: true,
              value: 'Confirm button',
              action: () => {
                console.info('Get ActionSheet handled');
              }
            },
            cancel: () => {
              console.info('ActionSheet canceled');
            },
            onWillDismiss: (dismissDialogAction: DismissDialogAction) => {
              console.info(`reason= ${dismissDialogAction.reason}`);
              console.info('ActionSheet onWillDismiss');
              if (dismissDialogAction.reason === DismissReason.PRESS_BACK) {
                dismissDialogAction.dismiss();
              }
              if (dismissDialogAction.reason === DismissReason.TOUCH_OUTSIDE) {
                dismissDialogAction.dismiss();
              }
            },
            alignment: DialogAlignment.Bottom,
            offset: { dx: 0, dy: -10 },
            enableHoverMode: true,
            hoverModeArea: HoverModeAreaType.TOP_SCREEN,
            sheets: [
              {
                title: 'apples',
                action: () => {
                  console.info('apples');
                }
              },
              {
                title: 'bananas',
                action: () => {
                  console.info('bananas');
                }
              },
              {
                title: 'pears',
                action: () => {
                  console.info('pears');
                }
            ]
          })
    }.width('100%')
    .height('100%')
  }
```

![image](public_sys-resources/zh-cn_image_0000002553205265.webp)

**示例6（弹窗生命周期）**

该示例为弹窗配置生命周期回调。

从API version 19开始，在[ActionSheetOptions](#ZH-CN_TOPIC_0000002522080886__actionsheetoptions对象说明)中新增了onDidAppear、onDidDisappear、onWillAppear和onWillDisappear属性。

```ets
// xxx.ets
@Entry
@Component
struct Example1 {
  @State log: string = 'Log information:';
  flag: boolean = false;

  build() {
    Column({ space: 5 }) {
      Button('ActionSheet')
        .onClick(() => {
          this.getUIContext().showActionSheet({
            title: 'ActionSheet',
            message: 'message',
            autoCancel: true,
            alignment: DialogAlignment.Bottom,
            offset: { dx: 0, dy: -20 },
            confirm: {
              value: 'button',
              action: () => {
                console.info('ActionSheet Button-clicking callback');
              }
            },
            cancel: () => {
              console.info('ActionSheet Closed callbacks');
            },
            sheets: [
              {
                title: 'apples',
                action: () => {
                  console.info('ActionSheet apples')
                }
              },
              {
                title: 'bananas',
                action: () => {
                  console.info('ActionSheet bananas')
                }
              },
              {
                title: 'pears',
                action: () => {
                  console.info('ActionSheet pears')
                }
            ],
            onDidAppear: () => {
              this.log += '# onDidAppear';
              console.info('ActionSheet,is onDidAppear!');
            },
            onDidDisappear: () => {
              this.log += '# onDidDisappear';
              console.info('ActionSheet,is onDidDisappear!');
            },
            onWillAppear: () => {
              this.log = 'Log information:onWillAppear';
              console.info('ActionSheet,is onWillAppear!');
            },
            onWillDisappear: () => {
              this.log += '# onWillDisappear';
              console.info('ActionSheet,is onWillDisappear!');
            }
          })
      Text(this.log).fontSize(30).margin({ top: 200 })
    }.width('100%').margin({ top: 5 })
  }
```

![image](public_sys-resources/zh-cn_image_0000002522085310.webp)

**示例7（自定义背景模糊效果参数）**

该示例通过配置[backgroundBlurStyleOptions](#ZH-CN_TOPIC_0000002522080886__actionsheetoptions对象说明)，实现自定义背景模糊效果。

从API version 19开始，在[ActionSheetOptions](#ZH-CN_TOPIC_0000002522080886__actionsheetoptions对象说明)中新增了backgroundBlurStyleOptions属性。

```ets
@Entry
@Component
struct ActionSheetExample {
  build() {
    Stack({ alignContent: Alignment.Top }) {
      Image($r('app.media.bg'))
      Column() {
        Button("ActionSheet")
          .margin(20)
          .onClick(() => {
            this.getUIContext().showActionSheet({
              title: 'ActionSheet Title',
              subtitle: 'ActionSheet Subtitle',
              message: 'ActionSheet Text',
              sheets: [
                {
                  title: 'Apples',
                  action: () => {
                    console.info('apples');
                  }
                },
                {
                  title: 'Bananas',
                  action: () => {
                    console.info('bananas');
                  }
                },
                {
                  title: 'Pears',
                  action: () => {
                    console.info('pears');
                  }
              ],
              alignment: DialogAlignment.Center,
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
```

![image](public_sys-resources/zh-cn_image_0000002553365227.webp)

**示例8（自定义背景效果参数）**

该示例通过配置[backgroundEffect](#ZH-CN_TOPIC_0000002522080886__actionsheetoptions对象说明)，实现自定义背景效果。

从API version 19开始，在[ActionSheetOptions](#ZH-CN_TOPIC_0000002522080886__actionsheetoptions对象说明)中新增了backgroundEffect属性。

```ets
@Entry
@Component
struct ActionSheetExample {
  build() {
    Stack({ alignContent: Alignment.Top }) {
      Image($r('app.media.bg'))
      Column() {
        Button("ActionSheet")
          .margin(20)
          .onClick(() => {
            this.getUIContext().showActionSheet({
              title: 'ActionSheet Title',
              subtitle: 'ActionSheet Subtitle',
              message: 'ActionSheet Text',
              sheets: [
                {
                  title: 'Apples',
                  action: () => {
                    console.info('apples');
                  }
                },
                {
                  title: 'Bananas',
                  action: () => {
                    console.info('bananas');
                  }
                },
                {
                  title: 'Pears',
                  action: () => {
                    console.info('pears');
                  }
              ],
              alignment: DialogAlignment.Center,
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
```

![image](public_sys-resources/zh-cn_image_0000002522245304.webp)