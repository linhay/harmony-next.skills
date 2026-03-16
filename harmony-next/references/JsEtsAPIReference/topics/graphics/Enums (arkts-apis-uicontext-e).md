[]()[]()

# Enums

本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

[]()[]()

#### KeyboardAvoidMode11+

配置键盘弹出时页面的避让模式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称值说明OFFSET0

上抬模式。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

RESIZE1

压缩模式。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

OFFSET_WITH_CARET14+2

上抬模式，输入框光标位置发生变化时候也会触发避让。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

RESIZE_WITH_CARET14+3

压缩模式，输入框光标位置发生变化时候也会触发避让。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

NONE14+4

不避让键盘。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

[]()[]()

#### SwiperDynamicSyncSceneType12+

枚举值，表示动态帧率场景的类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称值说明GESTURE0手势操作场景。ANIMATION1动画过渡场景。[]()[]()

#### MarqueeDynamicSyncSceneType14+

枚举值，表示Marquee的动态帧率场景的类型。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称值说明ANIMATION1动画过渡场景。[]()[]()

#### NodeRenderState20+

组件的渲染状态。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称值说明ABOUT_TO_RENDER_IN0该节点已挂载到渲染树上，一般将会在下一帧被渲染。一般情况下可被看见，但会被渲染并不等同于一定可见。ABOUT_TO_RENDER_OUT1该节点已从渲染树中删除，一般下一帧不会被渲染，用户将不会看到此节点。[]()[]()

#### GestureActionPhase20+

此枚举类型表示手势回调触发阶段，对应gesture.d.ts中定义的动作回调，但不同手势类型支持的阶段不同（如SwipeGesture仅包含WILL_START枚举值）。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称值说明WILL_START0手势已被系统成功识别，将立即触发onActionStart或onAction回调。若手势绑定了onActionStart，则在onActionStart处触发；若手势绑定了onAction，则在onAction处触发；若两者同时绑定，则优先在onActionStart处触发；若两者均未绑定，则不会触发任何回调。某些容器有内置手势绑定了回调（如滚动类容器），默认支持上述回调触发机制，无需显式绑定即可触发回调。WILL_END1表示手势已被判定为结束状态（通常发生在用户抬起手指终止交互时）。onActionEnd回调将立即触发，但手势必须显式绑定onActionEnd。某些容器有内置手势绑定了回调（如滚动类容器），默认支持该结束状态判定，无需显式绑定即可触发onActionEnd回调。[]()[]()

#### GestureListenerType20+

此枚举类型用于指定需要监控的手势类型。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称值说明TAP0点击手势。LONG_PRESS1长按手势。PAN2平移手势。PINCH3捏合手势。SWIPE4滑动手势。ROTATION5旋转手势。