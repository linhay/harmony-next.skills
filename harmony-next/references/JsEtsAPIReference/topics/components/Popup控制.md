# Popup控制

为组件绑定Popup气泡，并设置气泡内容、交互逻辑和显示状态。

  ![image](public_sys-resources/note_3.0-zh-cn.webp)

-

从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

-

Popup气泡的显示状态在[PopupOptions](#ZH-CN_TOPIC_0000002522240796__popupoptions类型说明)或[CustomPopupOptions](#ZH-CN_TOPIC_0000002522240796__custompopupoptions8类型说明)中onStateChange属性的回调中反馈。当绑定Popup气泡的组件被销毁时气泡会消失，但不会通过onStateChange反馈显示状态。

-

Popup气泡的最大高度为当前窗口高度 - 上下安全区域高度（状态栏、导航条）- 80vp。

-

多个气泡同时弹出时，子窗内显示的气泡比主窗内显示的气泡层级高，所处窗口相同时，后面弹出的气泡层级比先弹出的气泡层级高。

-

PC/2in1设备默认有双描边，其他设备默认无双描边。

-

子窗弹窗里不能再弹出子窗弹窗，例如bindPopup设置了showInSubWindow为true时，则不能再弹出另一个设置了showInSubWindow为true的弹窗。

-

当绑定气泡的组件销毁、横竖屏旋转或应用进入后台状态时，气泡会自动消失，且不会触发[onWillDismiss](#ZH-CN_TOPIC_0000002522240796__popupoptions类型说明)事件。

**bindPopup**

bindPopup(show: boolean, popup: PopupOptions | CustomPopupOptions): T

为组件绑定Popup气泡。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

-

不支持在输入法类型窗口中使用子窗（showInSubwindow为true）的bindPopup，详情见输入法框架的约束与限制说明[createPanel](@ohos.inputMethodEngine (输入法服务).md#ZH-CN_TOPIC_0000002553201227__createpanel10-1)。

-

该接口不支持在[attributeModifier](动态属性设置.md#ZH-CN_TOPIC_0000002522240800__attributemodifier)中调用。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| show | boolean | 是 | 气泡显示状态。Popup气泡必须等待页面全部构建完成才能展示，因此show不能在页面构建中设置为true，否则会导致Popup气泡显示位置及形状错误。该参数从API version 18开始支持!!语法双向绑定变量。 true：弹出气泡；false：关闭气泡。 默认值：false |
| popup | PopupOptions | CustomPopupOptions8+ | 是 | 配置弹出气泡的参数。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

**PopupOptions类型说明**

基础气泡的信息。

系统能力： SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| message | string | 否 | 否 | 气泡信息内容。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| primaryButton | { value: string, action: () => void } | 否 | 是 | 第一个按钮。 value：气泡里主按钮的文本。 action：点击主按钮的回调函数。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| secondaryButton | { value: string, action: () => void } | 否 | 是 | 第二个按钮。 value：气泡里辅助按钮的文本。 action：点击辅助按钮的回调函数。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| onStateChange | (event: { isVisible: boolean }) => void | 否 | 是 | 气泡状态变化事件回调，参数isVisible为气泡的显示状态。返回true时，表示气泡从关闭到打开，返回false时，表示气泡从打开到关闭。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| showInSubWindow9+ | boolean | 否 | 是 | 气泡是否显示在创建的子窗里。 true：气泡会显示在创建的子窗里；false：气泡会显示在对应的主窗中。 默认值：false 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| mask10+ | boolean | { color : ResourceColor } | 否 | 是 | 设置气泡是否有遮罩层及遮罩颜色。 true：显示透明色遮罩层；false：不显示遮罩层。 Color：显示指定颜色的遮罩层。 默认值：true 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| messageOptions10+ | PopupMessageOptions | 否 | 是 | 设置气泡信息文本参数。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| targetSpace10+ | Length | 否 | 是 | 设置Popup与宿主节点的间距。不支持设置百分比。 默认值：8 单位：vp 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| placement10+ | Placement | 否 | 是 | 设置Popup组件相对于宿主节点的显示位置，默认值为Placement.Bottom。 如果同时设置了placementOnTop和placement，则以placement的设置为准。如果开发者设置的位置上无法完整显示气泡，气泡会自动避让至可以完整显示的位置。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| offset10+ | Position | 否 | 是 | 设置Popup组件相对于placement设置的显示位置的偏移。 默认值：{ x: 0, y: 0 } 单位：vp 说明： 不支持设置百分比。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| enableArrow10+ | boolean | 否 | 是 | 设置是否显示箭头。 true：显示箭头；false：不显示箭头。 默认值：true 说明： 当页面可用空间无法让气泡完全避让时，气泡会覆盖到组件上并且不显示箭头。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| arrowPointPosition11+ | ArrowPointPosition | 否 | 是 | 气泡箭头相对于父组件显示位置，气泡箭头在垂直和水平方向上有Start、Center、End三个位置点可选。以上所有位置点均位于父组件区域的范围内，不会超出父组件的边界范围。 默认值：ArrowPointPosition.CENTER 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| arrowWidth11+ | Dimension | 否 | 是 | 设置箭头宽度。若所设置的箭头宽度超过所在边的长度减去两倍的气泡圆角大小，则不绘制气泡箭头。 默认值：16 单位：vp 说明： 不支持设置百分比。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| arrowOffset9+ | Length | 否 | 是 | Popup箭头在气泡处的偏移。 箭头在气泡上下方时，数值为0表示箭头居最左侧，偏移量为箭头至最左侧的距离，默认居中。 箭头在气泡左右侧时，偏移量为箭头至最上侧的距离，默认居中。 显示在屏幕边缘时，气泡会自动左右偏移，数值为0时箭头始终指向绑定组件。 单位：vp 说明： 1. 没设置arrowOffset的情况下，气泡箭头与四个角的距离不能小于圆角半径。 2. 如果设置了arrowPointPosition属性，arrowOffset属性将不生效。 3. 不支持设置百分比。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| arrowHeight11+ | Dimension | 否 | 是 | 设置箭头高度。 默认值：8 单位：vp 说明： 不支持设置百分比。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| popupColor11+ | Color | string | Resource | number | 否 | 是 | 气泡的颜色。如需去除模糊背景填充效果，需将backgroundBlurStyle设置为BlurStyle.NONE。 默认值：透明色TRANSPARENT加模糊背景填充效果COMPONENT_ULTRA_THICK。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| autoCancel11+ | boolean | 否 | 是 | 页面有操作时，气泡是否自动关闭。 true：自动关闭气泡；false：气泡不会自动关闭。 默认值：true 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| width11+ | Dimension | 否 | 是 | 气泡宽度，未设置或者异常值场景下，气泡自适应内容宽度。 单位：vp 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| radius11+ | Dimension | 否 | 是 | 设置气泡圆角半径。 默认值：20 单位：vp 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| shadow11+ | ShadowOptions | ShadowStyle | 否 | 是 | 设置气泡阴影。 默认值：ShadowStyle.OUTER_DEFAULT_MD 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| backgroundBlurStyle11+ | BlurStyle | 否 | 是 | 设置气泡模糊背景参数。 默认值：BlurStyle.COMPONENT_ULTRA_THICK 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| transition12+ | TransitionEffect | 否 | 是 | 自定义设置Popup气泡显示和退出的动画效果。 说明： 1. 不设置时使用默认的显示/退出动效。 2. 显示动效中按back键，打断显示动效，执行退出动效，动画效果为显示动效与退出动效的曲线叠加后的效果。 3. 退出动效中按back键，不会打断退出动效，back键不被响应。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| onWillDismiss12+ | boolean | Callback<DismissPopupAction> | 否 | 是 | 设置Popup交互式关闭拦截开关及拦截回调函数，默认值为true，Popup响应点击、侧滑（左滑/右滑）、三键back。 1. 当为boolean类型时，如果设置为false，则不响应点击、侧滑（左滑/右滑）、三键back、路由跳转或键盘ESC退出事件，仅当设置“气泡显示状态”参数show值为false时才退出；如果设置为true，则正常响应退出事件； 2. 如果设置为函数类型，则拦截退出事件且执行回调函数。侧滑（左滑/右滑）、三键back、路由跳转或键盘ESC在回调函数中返回的reason为PRESS_BACK，点击为TOUCH_OUTSIDE。 说明： 在onWillDismiss回调中，不能再做onWillDismiss拦截。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| followTransformOfTarget13+ | boolean | 否 | 是 | 气泡绑定的宿主组件或其宿主组件的父容器添加了旋转、缩放等变换时，气泡是否跟随宿主组件变换。 true：气泡可以拿到变换后宿主的位置，显示到相应位置；false：气泡拿不到宿主变换后的位置，可能显示异常。 默认值：false 元服务API： 从API version 13开始，该接口支持在元服务中使用。 |
| keyboardAvoidMode15+ | KeyboardAvoidMode | 否 | 是 | 气泡是否避让软键盘，默认不避让。设置为避让后，气泡显示空间不足时，由原先居中覆盖父组件的方式改为平移覆盖父组件，且气泡箭头不指向宿主时，不再显示箭头。 默认值：KeyboardAvoidMode.NONE 元服务API： 从API version 15开始，该接口支持在元服务中使用。 |
| enableHoverMode18+ | boolean | 否 | 是 | Popup组件是否响应悬停态（半折叠状态）变化，即在悬停态下是否触发避让折痕区域。 默认值：false，2in1设备默认为true。未设置或者值为非法值时，生效默认值。 说明： 1. 如果Popup的弹出位置在悬停态折痕区域，Popup组件不会响应悬停态。 2. 2in1设备从API version 20开始生效。 3. 2in1设备仅在窗口瀑布模式下生效。 元服务API： 从API version 18开始，该接口支持在元服务中使用。 |
| outlineWidth20+ | Dimension | 否 | 是 | 设置Popup组件外描边的宽度。 默认值：1 单位：vp 说明： 1. 不支持设置百分比，设置百分比时按0处理。 2. 在没有设置Popup组件外描边的情况下，该接口需要和outlineLinearGradient配合使用。 3. 当设置双描边时，建议外描边宽度不超过10vp。 元服务API： 从API version 20开始，该接口支持在元服务中使用。 |
| borderWidth20+ | Dimension | 否 | 是 | 设置Popup组件内描边的宽度。 默认值：1 单位：vp 说明： 1. 不支持设置百分比，设置百分比时按0处理。 2. 在没有设置Popup组件内描边的情况下，该接口需要和borderLinearGradient配合使用。 3. 当设置双描边时，建议内描边宽度不超过10vp。 元服务API： 从API version 20开始，该接口支持在元服务中使用。 |
| outlineLinearGradient20+ | PopupBorderLinearGradient | 否 | 是 | 设置Popup组件外描边线性渐变的颜色。 说明： 1. outlineLinearGradient不设置或者设置为null、undefined时，外描边没有线性渐变效果。 2. outlineLinearGradient设置时，direction默认值是：GradientDirection.Bottom。 元服务API： 从API version 20开始，该接口支持在元服务中使用。 |
| borderLinearGradient20+ | PopupBorderLinearGradient | 否 | 是 | 设置Popup组件内描边线性渐变的颜色。 说明： 1. borderLinearGradient不设置或者设置为null、undefined时，内描边没有线性渐变效果。 2. borderLinearGradient设置时，direction默认值是：GradientDirection.Bottom。 元服务API： 从API version 20开始，该接口支持在元服务中使用。 |
| avoidTarget20+ | AvoidanceMode | 否 | 是 | 设置Popup避让时是否覆盖指向组件。 默认值：AvoidanceMode.COVER_TARGET 元服务API： 从API version 20开始，该接口支持在元服务中使用。 |
| placementOnTop(deprecated) | boolean | 否 | 是 | 是否在组件上方显示，默认值为false。取值为true：气泡显示到绑定组件的上方，取值false：气泡显示到绑定组件的下方。 说明： 从API version 7开始支持，从API version 10开始废弃，建议使用placement替代。 |

**PopupMessageOptions10+类型说明**

气泡文本的样式。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| textColor | ResourceColor | 否 | 是 | 设置气泡信息文本颜色。 |
| font | Font | 否 | 是 | 设置气泡信息字体属性。 说明： 1. 不支持设置family。 2. Font中的weight属性不支持传入number类型。 |

**DismissPopupAction12+类型说明**

气泡关闭的信息。

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| dismiss | Callback<void> | 否 | 否 | Popup关闭回调函数。开发者需要退出时调用，不需要退出时无需调用。 |
| reason | DismissReason | 否 | 否 | 关闭原因，返回本次拦截Popup消失的事件原因。 |

**DismissReason12+枚举说明**

关闭原因类型。

系统能力： SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PRESS_BACK | 0 | 点击三键back、侧滑（左滑/右滑）、键盘ESC。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| TOUCH_OUTSIDE | 1 | 点击遮障层时。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| CLOSE_BUTTON | 2 | 点击关闭按钮。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| SLIDE_DOWN | 3 | 下拉关闭。 说明： 该接口仅支持在半模态转场中使用。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| SLIDE20+ | 4 | 侧滑（左滑/右滑）关闭。默认表示向右滑动关闭，镜像场景表示向左滑动关闭，不支持选择向左或向右滑动。 说明： 该接口仅支持在半模态转场中使用。 元服务API： 从API version 20开始，该接口支持在元服务中使用。 |

**CustomPopupOptions8+类型说明**

弹出自定义气泡的信息。

系统能力： SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| builder | CustomBuilder | 否 | 否 | 提示气泡内容的构造器。 说明： 1. Popup为通用属性，自定义Popup中不支持再次弹出Popup。对builder下的第一层容器组件不支持使用position属性，如果使用将导致气泡不显示。 2. builder中若使用自定义组件，自定义组件的aboutToAppear和aboutToDisappear生命周期与Popup气泡的显隐无关，不能使用其生命周期判断Popup气泡的显隐。 3. 该构造器的builder仅支持定义在UI组件中，例如可以定义在Builder函数、方法或者build方法里。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| placement | Placement | 否 | 是 | 气泡组件优先显示的位置，当前位置显示不下时，会自动调整位置。 默认值：Placement.Bottom 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| popupColor | Color | string | Resource | number | 否 | 是 | 气泡的颜色。如需去除模糊背景填充效果，需将backgroundBlurStyle设置为BlurStyle.NONE。 API version 10，默认值：'#4d4d4d' API version 11及以后，默认值：透明色TRANSPARENT加模糊背景填充效果COMPONENT_ULTRA_THICK 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| autoCancel | boolean | 否 | 是 | 页面有操作时，气泡是否自动关闭。 true：自动关闭气泡；false：气泡不会自动关闭。 默认值：true 说明： 如果要实现点击气泡内消失需要在builder中先放一个布局组件，然后再将Popup高级组件放在布局组件里面，再在布局组件的onClick事件中修改控制显隐的状态变量show为false。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| onStateChange | (event: { isVisible: boolean }) => void | 否 | 是 | 气泡状态变化事件回调，参数为气泡的显示状态。返回true时，表示气泡从关闭到打开，返回false时，表示气泡从打开到关闭。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| enableArrow | boolean | 否 | 是 | 是否显示箭头。 true：显示箭头；false：不显示箭头。 从API version 9开始，如果箭头所在方位侧的气泡长度不足以显示下箭头，则会默认不显示箭头。比如：placement设置为Left，此时如果气泡高度小于箭头的宽度（32vp）与气泡圆角两倍（48vp）之和（80vp），则实际不会显示箭头。 默认值：true 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| arrowOffset9+ | Length | 否 | 是 | Popup箭头在气泡处的偏移。 箭头在气泡上下方时，数值为0表示箭头居最左侧，偏移量为箭头至最左侧的距离，默认居中。 箭头在气泡左右侧时，偏移量为箭头至最上侧的距离，默认居中。 显示在屏幕边缘时，气泡会自动左右偏移，数值为0时箭头始终指向绑定组件。 单位：vp 说明： 1. 没设置arrowOffset的情况下，气泡箭头与四个角的距离不能小于圆角半径。 2. 如果设置了arrowPointPosition属性，arrowOffset属性将不生效。 3. 不支持设置百分比。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| arrowPointPosition11+ | ArrowPointPosition | 否 | 是 | 气泡箭头相对于父组件显示位置，气泡箭头在垂直和水平方向上有Start、Center、End三个位置点可选。以上所有位置点均位于父组件区域的范围内，不会超出父组件的边界范围。 默认值：ArrowPointPosition.CENTER 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| arrowWidth11+ | Dimension | 否 | 是 | 设置箭头宽度。若所设置的箭头宽度超过所在边的长度减去两倍的气泡圆角大小，则不绘制气泡箭头。 默认值：16 单位：vp 说明： 不支持设置百分比。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| arrowHeight11+ | Dimension | 否 | 是 | 设置箭头高度。 默认值：8 单位：vp 说明： 不支持设置百分比。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| showInSubWindow9+ | boolean | 否 | 是 | 气泡是否显示在创建的子窗里。 true：气泡会显示在创建的子窗里；false：气泡会显示在对应的主窗中。 默认值：false 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| maskColor(deprecated) | Color | string | Resource | number | 否 | 是 | 设置气泡遮罩层颜色。 说明： 从 API version 10 开始废弃，建议使用mask替代。 |
| mask10+ | boolean | { color : ResourceColor } | 否 | 是 | 设置气泡是否有遮罩层及遮罩颜色。如果设置为false，则没有遮罩层；如果设置为true，则设置有遮罩层并且颜色为透明色；如果设置为Color，则为遮罩层的颜色。默认值：true 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| targetSpace10+ | Length | 否 | 是 | 设置Popup与宿主节点的间距。不支持设置百分比。 默认值：8 单位：vp 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| offset10+ | Position | 否 | 是 | 设置Popup组件相对于placement设置的显示位置的偏移。 说明： 不支持设置百分比。 默认值：{ x: 0, y: 0 } 单位：vp 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| width11+ | Dimension | 否 | 是 | 气泡宽度，未设置或者异常值场景下，气泡自适应内容宽度。 单位：vp 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| radius11+ | Dimension | 否 | 是 | 设置气泡圆角半径。 默认值：20 单位：vp 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| shadow11+ | ShadowOptions | ShadowStyle | 否 | 是 | 设置气泡阴影。 默认值：ShadowStyle.OUTER_DEFAULT_MD 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| backgroundBlurStyle11+ | BlurStyle | 否 | 是 | 设置气泡模糊背景参数。 默认值：BlurStyle.COMPONENT_ULTRA_THICK 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| focusable11+ | boolean | 否 | 是 | 设置气泡弹出后是否获焦。 true：气泡可以获焦；false：气泡不会获焦。 默认值：false 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| transition12+ | TransitionEffect | 否 | 是 | 自定义设置Popup气泡显示和退出的动画效果。 说明： 如果不设置，则使用默认的显示/退出动效。 2. 显示动效中按back键，打断显示动效，执行退出动效，动画效果为显示动效与退出动效的曲线叠加后的效果。 3. 退出动效中按back键，不会打断退出动效，退出动效继续执行，back键不被响应。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| onWillDismiss12+ | boolean | Callback<DismissPopupAction> | 否 | 是 | 设置Popup交互式关闭拦截开关及拦截回调函数，默认值为true，Popup响应点击、侧滑（左滑/右滑）、三键back。 1. 当为boolean类型时，如果设置为false，则不响应点击、侧滑（左滑/右滑）、三键back、路由跳转或键盘ESC退出事件，仅当设置“气泡显示状态”参数show值为false时才退出；如果设置为true，则正常响应退出事件； 2. 如果设置为函数类型，则拦截退出事件且执行回调函数。侧滑（左滑/右滑）、三键back、路由跳转或键盘ESC在回调函数中返回的reason为PRESS_BACK，点击为TOUCH_OUTSIDE。 说明： 在onWillDismiss回调中，不能再做onWillDismiss拦截。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| followTransformOfTarget13+ | boolean | 否 | 是 | 气泡绑定的宿主组件或其宿主组件的父容器添加了旋转、缩放等变换时，气泡是否跟随宿主组件变换。 true：气泡可以拿到变换后宿主的位置，显示到相应位置；false：气泡拿不到宿主变换后的位置，可能显示异常。 默认值：false 元服务API： 从API version 13开始，该接口支持在元服务中使用。 |
| keyboardAvoidMode15+ | KeyboardAvoidMode | 否 | 是 | 气泡是否避让软键盘，默认不避让。设置为避让后，气泡显示空间不足时，由原先居中覆盖父组件的方式改为平移覆盖父组件，且气泡箭头不指向宿主时，不再显示箭头。 默认值：KeyboardAvoidMode.NONE 元服务API： 从API version 15开始，该接口支持在元服务中使用。 |
| enableHoverMode18+ | boolean | 否 | 是 | Popup组件是否响应悬停态（半折叠状态）变化，即在悬停态下是否触发避让折痕区域。 默认值：false，2in1设备默认为true。未设置或者值为非法值时，生效默认值。 说明： 1. 如果Popup的弹出位置在悬停态折痕区域，Popup组件不会响应悬停态。 2. 2in1设备从API version 20开始生效。 3. 2in1设备仅在窗口瀑布模式下生效。 元服务API： 从API version 18开始，该接口支持在元服务中使用。 |
| outlineWidth20+ | Dimension | 否 | 是 | 设置Popup组件外描边的宽度。 默认值：1 单位：vp 说明： 1. 不支持设置百分比，设置百分比时按0处理。 2. 在没有设置Popup组件外描边的情况下，该接口需要和outlineLinearGradient配合使用。 3. 当设置双描边时，建议外描边宽度不超过10vp。 元服务API： 从API version 20开始，该接口支持在元服务中使用。 |
| borderWidth20+ | Dimension | 否 | 是 | 设置Popup组件内描边的宽度。 默认值：1 单位：vp 说明： 1. 不支持设置百分比，设置百分比时按0处理。 2. 在没有设置Popup组件内描边的情况下，该接口需要和borderLinearGradient配合使用。 3. 当设置双描边时，建议内描边宽度不超过10vp。 元服务API： 从API version 20开始，该接口支持在元服务中使用。 |
| outlineLinearGradient20+ | PopupBorderLinearGradient | 否 | 是 | 设置Popup组件外描边线性渐变的颜色。 说明： 1. outlineLinearGradient不设置或者设置为null、undefined时，外描边没有线性渐变效果。 2. outlineLinearGradient设置时，direction默认值是：GradientDirection.Bottom。 元服务API： 从API version 20开始，该接口支持在元服务中使用。 |
| borderLinearGradient20+ | PopupBorderLinearGradient | 否 | 是 | 设置Popup组件内描边线性渐变的颜色。 说明： 1. borderLinearGradient不设置或者设置为null、undefined时，内描边没有线性渐变效果。 2. borderLinearGradient设置时，direction默认值是：GradientDirection.Bottom。 元服务API： 从API version 20开始，该接口支持在元服务中使用。 |
| avoidTarget20+ | AvoidanceMode | 否 | 是 | 设置Popup避让时是否覆盖指向组件。 说明： 设置avoidTarget为AvoidanceMode.AVOID_AROUND_TARGET时，气泡在剩余显示空间不足的情况下会进行压缩，此时气泡内容需结合Scroll使用，否则气泡内容会出现遮挡。 默认值：AvoidanceMode.COVER_TARGET 元服务API： 从API version 20开始，该接口支持在元服务中使用。 |

**PopupCommonOptions18+类型说明**

配置弹出气泡的参数。使用[UIContext](Class (UIContext).md)中的[getPromptAction()](Class (UIContext).md#ZH-CN_TOPIC_0000002522240732__getpromptaction)方法获取到[PromptAction](Class (PromptAction).md)对象，再通过该对象调用[openPopup](Class (PromptAction).md#ZH-CN_TOPIC_0000002522240730__openpopup18)和[updatePopup](Class (PromptAction).md#ZH-CN_TOPIC_0000002522240730__updatepopup18)时options的属性。

系统能力： SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| placement | Placement | 否 | 是 | 气泡组件优先显示的位置，当前位置显示不下时，会自动调整位置。 默认值：Placement.Bottom 元服务API： 从API version 18开始，该接口支持在元服务中使用。 |
| popupColor | ResourceColor | 否 | 是 | 气泡的颜色。如需去除模糊背景填充效果，需将backgroundBlurStyle设置为BlurStyle.NONE。默认值：透明色TRANSPARENT加模糊背景填充效果COMPONENT_ULTRA_THICK。 元服务API： 从API version 18开始，该接口支持在元服务中使用。 |
| autoCancel | boolean | 否 | 是 | 页面有操作时，值为true表示自动关闭气泡，值为false表示气泡不会自动关闭。 默认值：true 元服务API： 从API version 18开始，该接口支持在元服务中使用。 |
| onStateChange | PopupStateChangeCallback | 否 | 是 | 气泡状态变化事件回调。 说明： 不支持通过updatePopup进行更新。 元服务API： 从API version 18开始，该接口支持在元服务中使用。 |
| arrowOffset | Length | 否 | 是 | Popup箭头在气泡处的偏移。 箭头在气泡上下方时，数值为0表示箭头居最左侧，偏移量为箭头至最左侧的距离，默认居中。 箭头在气泡左右侧时，偏移量为箭头至最上侧的距离，默认居中。 显示在屏幕边缘时，气泡会自动左右偏移，数值为0时箭头始终指向绑定组件。 单位：vp 说明： 1. 没设置arrowOffset的情况下，气泡箭头与四个角的距离不能小于圆角半径。 2. 如果设置了arrowPointPosition属性，arrowOffset属性将不生效。 3. 不支持设置百分比。 元服务API： 从API version 18开始，该接口支持在元服务中使用。 |
| enableArrow | boolean | 否 | 是 | 是否显示箭头。值为true时显示箭头，值为false时不显示箭头。 如果箭头所在方位侧的气泡长度不足以显示下箭头，则会默认不显示箭头。比如：placement设置为Left，此时如果气泡高度小于箭头的宽度（32vp）与气泡圆角两倍（48vp）之和（80vp），则实际不会显示箭头。 默认值：true 元服务API： 从API version 18开始，该接口支持在元服务中使用。 |
| arrowPointPosition | ArrowPointPosition | 否 | 是 | 气泡箭头相对于父组件显示位置，气泡箭头在垂直和水平方向上有Start、Center、End三个位置点可选。以上所有位置点均位于父组件区域的范围内，不会超出父组件的边界范围。 默认值：ArrowPointPosition.CENTER 元服务API： 从API version 18开始，该接口支持在元服务中使用。 |
| arrowWidth | Dimension | 否 | 是 | 设置箭头宽度。若所设置的箭头宽度超过所在边的长度减去两倍的气泡圆角大小，则不绘制气泡箭头。 默认值：16 单位：vp 说明： 不支持设置百分比。 元服务API： 从API version 18开始，该接口支持在元服务中使用。 |
| arrowHeight | Dimension | 否 | 是 | 设置箭头高度。 默认值：8 单位：vp 说明： 不支持设置百分比。 元服务API： 从API version 18开始，该接口支持在元服务中使用。 |
| showInSubWindow | boolean | 否 | 是 | 取值为true时，气泡会显示在创建的子窗里，取值为false时，气泡会显示在对应的主窗中。 默认值：false 说明： 不支持通过updatePopup进行更新。 元服务API： 从API version 18开始，该接口支持在元服务中使用。 |
| mask | boolean | PopupMaskType | 否 | 是 | 设置气泡是否有遮罩层及遮罩颜色。设置为false时不显示遮罩层，设置为true时显示透明色遮罩层，设置为PopupMaskType时显示指定颜色的遮罩层。默认值：true 元服务API： 从API version 18开始，该接口支持在元服务中使用。 |
| targetSpace | Length | 否 | 是 | 设置Popup与宿主节点的间隙。不支持设置百分比。 默认值：8 单位：vp 元服务API： 从API version 18开始，该接口支持在元服务中使用。 |
| offset | Position | 否 | 是 | 设置Popup组件相对于placement设置的显示位置的偏移。 说明： 不支持设置百分比。 默认值：{ x: 0, y: 0 } 单位：vp 元服务API： 从API version 18开始，该接口支持在元服务中使用。 |
| width | Dimension | 否 | 是 | 气泡宽度。 元服务API： 从API version 18开始，该接口支持在元服务中使用。 |
| radius | Dimension | 否 | 是 | 设置气泡圆角半径。 默认值：20 单位：vp 元服务API： 从API version 18开始，该接口支持在元服务中使用。 |
| shadow | ShadowOptions | ShadowStyle | 否 | 是 | 设置气泡阴影。 默认值：ShadowStyle.OUTER_DEFAULT_MD 元服务API： 从API version 18开始，该接口支持在元服务中使用。 |
| backgroundBlurStyle | BlurStyle | 否 | 是 | 设置气泡模糊背景参数。 默认值：BlurStyle.COMPONENT_ULTRA_THICK 元服务API： 从API version 18开始，该接口支持在元服务中使用。 |
| focusable | boolean | 否 | 是 | 设置气泡弹出后是否获焦。 true：气泡可以获焦；false：气泡不会获焦。 默认值：false 说明： 不支持通过updatePopup进行更新。 元服务API： 从API version 18开始，该接口支持在元服务中使用。 |
| transition | TransitionEffect | 否 | 是 | 自定义设置Popup气泡显示和退出的动画效果。 说明： 1. 如果不设置，则使用默认的显示/退出动效。 2. 显示动效中按back键，打断显示动效，执行退出动效，动画效果为显示动效与退出动效的曲线叠加后的效果。 3. 退出动效中按back键，不会打断退出动效，退出动效继续执行，back键不被响应。 4.不支持通过updatePopup进行更新。 元服务API： 从API version 18开始，该接口支持在元服务中使用。 |
| onWillDismiss | boolean|Callback<DismissPopupAction> | 否 | 是 | 设置Popup交互式关闭拦截开关及拦截回调函数，默认值为true，Popup响应点击、侧滑（左滑/右滑）、三键back。 1. 当为boolean类型时，如果设置为false，则不响应点击、侧滑（左滑/右滑）、三键back、路由跳转或键盘ESC退出事件，仅当设置“气泡显示状态”参数show值为false时才退出；如果设置为true，则正常响应退出事件； 2. 如果设置为函数类型，则拦截退出事件且执行回调函数。侧滑（左滑/右滑）、三键back、路由跳转或键盘ESC在回调函数中返回的reason为PRESS_BACK，点击为TOUCH_OUTSIDE。 说明： 1. 在onWillDismiss回调中，不能再做onWillDismiss拦截。 2. 不支持通过updatePopup进行更新。 元服务API： 从API version 18开始，该接口支持在元服务中使用。 |
| followTransformOfTarget | boolean | 否 | 是 | 气泡绑定的宿主组件或其宿主组件的父容器添加了旋转、缩放等变换时，气泡是否跟随宿主组件变换。 true：气泡可以拿到变换后宿主的位置，显示到相应位置；false：气泡拿不到宿主变换后的位置，可能显示异常。 默认值：false 元服务API： 从API version 18开始，该接口支持在元服务中使用。 |
| enableHoverMode | boolean | 否 | 是 | Popup组件是否响应悬停态（半折叠状态）变化，即在悬停态下是否触发避让折痕区域。 默认值：false，2in1设备默认为true。未设置或者值为非法值时，生效默认值。 说明： 1. 如果Popup的弹出位置在悬停态折痕区域，Popup组件不会响应悬停态。 2. 2in1设备从API version 20开始生效。 3. 2in1设备仅在窗口瀑布模式下生效。 元服务API： 从API version 18开始，该接口支持在元服务中使用。 |
| outlineWidth20+ | Dimension | 否 | 是 | 设置Popup组件外描边的宽度。 默认值：1 单位：vp 说明： 1. 不支持设置百分比，设置百分比时按0处理。 2. 在没有设置Popup组件外描边的情况下，该接口需要和outlineLinearGradient配合使用。 3. 当设置双描边时，建议外描边宽度不超过10vp。 元服务API： 从API version 20开始，该接口支持在元服务中使用。 |
| borderWidth20+ | Dimension | 否 | 是 | 设置Popup组件内描边的宽度。 默认值：1 单位：vp 说明： 1. 不支持设置百分比，设置百分比时按0处理。 2. 在没有设置Popup组件内描边的情况下，该接口需要和borderLinearGradient配合使用。 3. 当设置双描边时，建议内描边宽度不超过10vp。 元服务API： 从API version 20开始，该接口支持在元服务中使用。 |
| outlineLinearGradient20+ | PopupBorderLinearGradient | 否 | 是 | 设置Popup组件外描边线性渐变的颜色。 说明： 1. outlineLinearGradient不设置或者设置为null、undefined时，外描边没有线性渐变效果。 2. outlineLinearGradient设置时，direction默认值是：GradientDirection.Bottom。 元服务API： 从API version 20开始，该接口支持在元服务中使用。 |
| borderLinearGradient20+ | PopupBorderLinearGradient | 否 | 是 | 设置Popup组件内描边线性渐变的颜色。 说明： 1. borderLinearGradient不设置或者设置为null、undefined时，内描边没有线性渐变效果。 2. borderLinearGradient设置时，direction默认值是：GradientDirection.Bottom。 元服务API： 从API version 20开始，该接口支持在元服务中使用。 |
| avoidTarget20+ | AvoidanceMode | 否 | 是 | 设置Popup避让时是否覆盖指向组件。 说明： 设置avoidTarget为AvoidanceMode.AVOID_AROUND_TARGET时，气泡在剩余显示空间不足的情况下会进行压缩，此时气泡内容需结合Scroll使用，否则气泡内容会出现遮挡。 默认值：AvoidanceMode.COVER_TARGET 元服务API： 从API version 20开始，该接口支持在元服务中使用。 |

**PopupStateChangeParam18+类型说明**

气泡的显示状态。

元服务API： 从API version 18开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| isVisible | boolean | 否 | 否 | 气泡的显示状态。返回true时，表示气泡从关闭到打开，返回false时，表示气泡从打开到关闭。 |

**PopupStateChangeCallback18+**

type PopupStateChangeCallback = (event: PopupStateChangeParam) => void;

气泡状态变化事件回调。

元服务API： 从API version 18开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | PopupStateChangeParam | 是 | 气泡当前的显示状态。 |

**PopupMaskType18+类型说明**

设置遮罩层颜色。

元服务API： 从API version 18开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| color | ResourceColor | 否 | 否 | 设置遮罩层颜色。 |

**PopupBorderLinearGradient20+类型说明**

设置描边线性渐变的颜色和方向。

元服务API： 从API version 20开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| direction | GradientDirection | 否 | 是 | 线性渐变的方向。 默认值：GradientDirection.Bottom 说明： 当线性渐变的方向设置为GradientDirection.None时，显示默认值。 |
| colors | Array<[ResourceColor, number]> | 否 | 否 | 指定渐变色颜色和其对应的百分比位置的数组，设置非法颜色直接跳过。 说明： 颜色设置方式可参考：ResourceColor，非ResourceColor范围内的颜色值即为非法颜色。 数组内颜色设置为undefined或者null时，默认为黑色。 colors参数的约束： ResourceColor表示填充的颜色，number表示指定颜色所处的位置，取值范围为[0,1.0]，0表示需要设置渐变色的容器的起始位置，1.0表示容器的结束位置。为实现多个颜色渐变效果，建议多个数组中number参数递增设置，如后一个数组number参数比前一个数组number小时，按照等于前一个数组number的值处理。 |

**KeyboardAvoidMode12+枚举说明**

弹窗避让键盘时，避让模式的枚举类型。

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DEFAULT | 0 | 默认避让软键盘并在到达极限高度之后进行高度压缩。 |
| NONE | 1 | 不避让软键盘。 |

**示例**

**示例1（弹出不同类型的气泡）**

该示例通过配置[PopupOptions](#ZH-CN_TOPIC_0000002522240796__popupoptions类型说明)或[CustomPopupOptions](#ZH-CN_TOPIC_0000002522240796__custompopupoptions8类型说明)中的keyboardAvoidMode属性，设置气泡是否避让软键盘。

从API version 15开始，分别在PopupOptions和CustomPopupOptions中新增了keyboardAvoidMode属性。

```ets
// xxx.ets
@Entry
@Component
struct PopupExample {
  @State handlePopup: boolean = false;
  @State customPopup: boolean = false;

  // Popup构造器定义弹框内容
  @Builder popupBuilder() {
    Row({ space: 2 }) {
      // $r('app.media.icon')需要替换为开发者所需的图像资源文件。
      Image($r("app.media.icon")).width(24).height(24).margin({ left: -5 })
      Text('Custom Popup').fontSize(10)
    }.width(100).height(50).padding(5)
  }

  build() {
    Flex({ direction: FlexDirection.Column }) {
      // PopupOptions 类型设置弹框内容
      Button('PopupOptions')
        .onClick(() => {
          this.handlePopup = !this.handlePopup;
        })
        .bindPopup(this.handlePopup, {
          message: 'This is a popup with PopupOptions',
          placement: Placement.Top,
          showInSubWindow:false,
          keyboardAvoidMode: KeyboardAvoidMode.DEFAULT, // 设置气泡避让软键盘
          primaryButton: {
            value: 'confirm',
            action: () => {
              this.handlePopup = !this.handlePopup;
              console.info('confirm Button click');
            }
          },
          // 第二个按钮
          secondaryButton: {
            value: 'cancel',
            action: () => {
              this.handlePopup = !this.handlePopup;
              console.info('cancel Button click');
            }
          },
          onStateChange: (e) => {
            console.info(JSON.stringify(e.isVisible))
            if (!e.isVisible) {
              this.handlePopup = false;
            }
        })
        .position({ x: 100, y: 150 })

      // CustomPopupOptions 类型设置弹框内容
      Button('CustomPopupOptions')
        .onClick(() => {
          this.customPopup = !this.customPopup;
        })
        .bindPopup(this.customPopup, {
          builder: this.popupBuilder,
          placement: Placement.Top,
          mask: {color:'#33000000'},
          popupColor: Color.Yellow,
          enableArrow: true,
          keyboardAvoidMode: KeyboardAvoidMode.DEFAULT, // 设置气泡避让软键盘
          showInSubWindow: false,
          onStateChange: (e) => {
            if (!e.isVisible) {
              this.customPopup = false;
            }
        })
        .position({ x: 80, y: 300 })
    }.width('100%').padding({ top: 5 })
  }
```

![image](public_sys-resources/zh-cn_image_0000002522244810.webp)

**示例2（设置气泡的文本样式）**

该示例通过配置[PopupOptions](#ZH-CN_TOPIC_0000002522240796__popupoptions类型说明)中的messageOptions属性，实现了弹出自定义文本样式的气泡。

```ets
// xxx.ets

@Entry
@Component
struct PopupExample {
  @State handlePopup: boolean = false;

  build() {
    Column({ space: 100 }) {
      Button('PopupOptions').margin(100)
        .onClick(() => {
          this.handlePopup = !this.handlePopup;
        })
        .bindPopup(this.handlePopup, {
          // PopupOptions类型气泡的内容
          message: 'This is a popup with PopupOptions',
          messageOptions: {
            // 气泡的文本样式
            textColor: Color.Red,
            font: {
              size: '14vp',
              style: FontStyle.Italic,
              weight: FontWeight.Bolder
            }
          },
          placement: Placement.Bottom,
          enableArrow: false, // 气泡弹出时不显示箭头
          targetSpace: '15vp',
          onStateChange: (e) => {
            console.info(JSON.stringify(e.isVisible));
            if (!e.isVisible) {
              this.handlePopup = false;
            }
        })
    }.margin(20)
  }
```

![image](public_sys-resources/zh-cn_image_0000002553204771.webp)

**示例3（设置气泡的样式）**

该示例通过配置[PopupOptions](#ZH-CN_TOPIC_0000002522240796__popupoptions类型说明)中的arrowHeight、arrowWidth、radius、shadow和popupColor属性，实现了气泡箭头以及气泡本身的样式。

```ets
// xxx.ets

@Entry
@Component
struct PopupExample {
  @State customPopup: boolean = false;
  @State handlePopup: boolean = false;

  build() {
    Column({ space: 100 }) {
      Button("popup")
        .margin({ top: 50 })
        .onClick(() => {
          this.customPopup = !this.customPopup;
        })
        .bindPopup(this.customPopup!!, {
          message: "this is a popup",
          arrowHeight: 20, // 设置气泡箭头高度
          arrowWidth: 20, // 设置气泡箭头宽度
          radius: 20, // 设置气泡的圆角
          shadow: ShadowStyle.OUTER_DEFAULT_XS, // 设置气泡的阴影
        })

      Button('PopupOptions')
        .onClick(() => {
          this.handlePopup = !this.handlePopup;
        })
        .bindPopup(this.handlePopup!!, {
          width: 300,
          message: 'This is a popup with PopupOptions',
          arrowPointPosition: ArrowPointPosition.START, // 设置箭头的位置
          backgroundBlurStyle: BlurStyle.NONE, // 关闭气泡的模糊背景
          popupColor: Color.Red, // 设置气泡的背景色
          autoCancel: true,
        })
    }
    .width('100%')
  }
```

![image](public_sys-resources/zh-cn_image_0000002522084818.webp)

**示例4（设置气泡的动效）**

该示例通过配置[PopupOptions](#ZH-CN_TOPIC_0000002522240796__popupoptions类型说明)或[CustomPopupOptions](#ZH-CN_TOPIC_0000002522240796__custompopupoptions8类型说明)中的transition属性，实现了气泡显示以及退出的动效。

```ets
// xxx.ets
@Entry
@Component
struct PopupExample {
  @State handlePopup: boolean = false;
  @State customPopup: boolean = false;

  // Popup构造器定义弹框内容
  @Builder
  popupBuilder() {
    Row() {
      Text('Custom Popup with transitionEffect').fontSize(10)
    }.height(50).padding(5)
  }

  build() {
    Flex({ direction: FlexDirection.Column }) {
      // PopupOptions 类型设置弹框内容
      Button('PopupOptions')
        .onClick(() => {
          this.handlePopup = !this.handlePopup;
        })
        .bindPopup(this.handlePopup, {
          message: 'This is a popup with transitionEffect',
          placement: Placement.Top,
          showInSubWindow: false,
          onStateChange: (e) => {
            console.info(JSON.stringify(e.isVisible))
            if (!e.isVisible) {
              this.handlePopup = false;
            }
          },
          // 设置气泡显示动效为透明度动效与平移动效的组合效果，无退出动效
          transition: TransitionEffect.asymmetric(
            TransitionEffect.OPACITY.animation({ duration: 1000, curve: Curve.Ease }).combine(
              TransitionEffect.translate({ x: 50, y: 50 })),
            TransitionEffect.IDENTITY)
        })
        .position({ x: 100, y: 150 })

      // CustomPopupOptions 类型设置弹框内容
      Button('CustomPopupOptions')
        .onClick(() => {
          this.customPopup = !this.customPopup;
        })
        .bindPopup(this.customPopup, {
          builder: this.popupBuilder,
          placement: Placement.Top,
          showInSubWindow: false,
          onStateChange: (e) => {
            if (!e.isVisible) {
              this.customPopup = false;
            }
          },
          // 设置气泡显示动效与退出动效为缩放动效
          transition: TransitionEffect.scale({ x: 1, y: 0 }).animation({ duration: 500, curve: Curve.Ease })
        })
        .position({ x: 80, y: 300 })
    }.width('100%').padding({ top: 5 })
  }
```

![image](public_sys-resources/zh-cn_image_0000002553364731.webp)

**示例5（为气泡添加事件）**

该示例通过配置[PopupOptions](#ZH-CN_TOPIC_0000002522240796__popupoptions类型说明)中的onWillDismiss属性，实现了当气泡退出时，拦截退出事件并执行回调函数。

```ets
// xxx.ets

@Entry
@Component
struct PopupExample {
  @State handlePopup: boolean = false;
  build() {
    Column() {
      Button('PopupOptions')
        .onClick(() => {
          this.handlePopup = true;
        })
        .bindPopup(this.handlePopup, {
          message: 'This is a popup with PopupOptions',
          messageOptions: {
            textColor: Color.Red,
            font: {
              size: '14vp',
              style: FontStyle.Italic,
              weight: FontWeight.Bolder
            }
          },
          placement: Placement.Bottom,
          enableArrow: false,
          targetSpace: '15vp',
          onStateChange: (e) => {
            if (!e.isVisible) {
              this.handlePopup = false;
            }
          },
          onWillDismiss: (
            (dismissPopupAction: DismissPopupAction) => {
              console.info("dismissReason:" + JSON.stringify(dismissPopupAction.reason));
              if (dismissPopupAction.reason === DismissReason.PRESS_BACK) {
                dismissPopupAction.dismiss();
              }
          )
        })
    }.margin(20)
  }
```

![image](public_sys-resources/zh-cn_image_0000002522244812.webp)

**示例6（为气泡拦截退出事件）**

该示例通过将[PopupOptions](#ZH-CN_TOPIC_0000002522240796__popupoptions类型说明)中onWillDismiss属性设置为false，实现拦截气泡的退出事件。同时，配置[PopupOptions](#ZH-CN_TOPIC_0000002522240796__popupoptions类型说明)中的followTransformOfTarget属性，可以设置宿主变换位置时，气泡是否跟随显示到相应位置。

```ets
// xxx.ets

@Entry
@Component
struct PopupExample {
  @State handlePopup: boolean = false;

  build() {
    Column() {
      Button('PopupOptions')
        .onClick(() => {
          this.handlePopup = true;
        })
        .bindPopup(this.handlePopup, {
          message: 'This is a popup with PopupOptions',
          messageOptions: {
            textColor: Color.Red,
            font: {
              size: '14vp',
              style: FontStyle.Italic,
              weight: FontWeight.Bolder
            }
          },
          placement: Placement.Bottom,
          enableArrow: false,
          targetSpace: '15vp',
          followTransformOfTarget: true,
          onStateChange: (e) => {
            let timer = setTimeout(() => {
              this.handlePopup = false;
            }, 6000);
            if (!e.isVisible) {
              this.handlePopup = false;
              clearTimeout(timer);
            }
          },
          onWillDismiss: false
        })
    }.margin(20)
  }
```

![image](public_sys-resources/zh-cn_image_0000002553204773.webp)

**示例7（为气泡内外描边设置线性渐变）**

该示例通过配置[PopupOptions](#ZH-CN_TOPIC_0000002522240796__popupoptions类型说明)中的outlineWidth、borderWidth、outlineLinearGradient、borderLinearGradient属性，为气泡设置内外描边线性渐变的颜色和方向。

从API version 20开始，在PopupOptions中新增了outlineWidth、borderWidth、outlineLinearGradient、borderLinearGradient属性。

```ets
// xxx.ets
@Entry
@Component
struct PopupExample {
  @State handlePopup: boolean = false

  build() {
    Flex({ direction: FlexDirection.Column }) {
      Button('PopupOptions')
        .onClick(() => {
          this.handlePopup = !this.handlePopup
        })
        .bindPopup(this.handlePopup!!, {
          message: 'This is a popup with PopupOptions',
          placement: Placement.Top,
          outlineWidth: 1,
          outlineLinearGradient: {
            direction: GradientDirection.Top,
            colors: [[Color.Yellow, 0.0], [Color.Green, 1.0]]
          },
          borderWidth: 1,
          borderLinearGradient: {
            direction: GradientDirection.Bottom,
            colors: [[Color.Red, 0.0], [Color.Blue, 1.0]]
          }
        })
        .position({ x: 100, y: 150 })
    }.width('100%').padding({ top: 5 })
  }
```

![image](public_sys-resources/zh-cn_image_0000002522084820.webp)

**示例8（为气泡设置避让宿主模式）**

该示例通过配置[PopupOptions](#ZH-CN_TOPIC_0000002522240796__popupoptions类型说明)的avoidTarget属性，实现气泡对其绑定组件的避让。

从API version 20开始，在PopupOptions中新增了avoidTarget属性。

```ets
// xxx.ets
@Entry
@Component
struct PopupExample {
  @State handlePopup: boolean = false;

  build() {
    Flex({ direction: FlexDirection.Column }) {
      Button('PopupOptions')
        .onClick(() => {
          this.handlePopup = !this.handlePopup
        })
        .bindPopup(this.handlePopup!!, {
          message: 'popup message '.repeat(200),
          placement: Placement.Top,
          avoidTarget: AvoidanceMode.AVOID_AROUND_TARGET,
        })
        .position({ x: 100, y: 150 })
    }.width('100%').padding({ top: 5 })
  }
```

![image](public_sys-resources/zh-cn_image_0000002553364733.webp)