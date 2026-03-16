[]()[]()

# Enums

-

本模块首批接口从API version 6开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

-

针对系统能力SystemCapability.Window.SessionManager，请先使用[canIUse()](../misc/SysCap (系统能力).md#ZH-CN_TOPIC_0000002529286149__caniuse)接口判断当前设备是否支持此syscap及对应接口。

[]()[]()

#### WindowType7+

窗口类型枚举。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

名称值说明TYPE_APP0

表示应用子窗口。

**模型约束：** 此接口仅可在FA模型下使用。

TYPE_SYSTEM_ALERT(deprecated)1

表示系统告警窗口。

**说明：** 从API version 11开始废弃。

从API version 7开始支持。

TYPE_FLOAT9+8

表示全局悬浮窗。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

TYPE_DIALOG10+16

表示模态窗口。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

TYPE_MAIN18+32

表示应用主窗口。

此窗口类型不支持在创建窗口时使用。

[]()[]()

#### AvoidAreaType7+

窗口内容的避让区域的类型枚举。

窗口内容做[沉浸式布局](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/window-terminology#沉浸式布局)适配时，需要按照AvoidAreaType对应的[AvoidArea](../../types/interfaces/Interfaces (其他) (arkts-apis-window-i).md#ZH-CN_TOPIC_0000002529284795__avoidarea7)做窗口内容避让。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

名称值说明TYPE_SYSTEM0表示系统默认区域。通常表示状态栏区域，悬浮窗状态下的应用主窗中表示三点控制栏区域。TYPE_CUTOUT1表示挖孔区域。TYPE_SYSTEM_GESTURE9+2表示侧边返回手势区域。当前所有设备均无此类型避让区域。TYPE_KEYBOARD9+3表示固定态软键盘区域。TYPE_NAVIGATION_INDICATOR11+4表示底部导航区域。根据用户设置，可表现为导航条或三键导航栏。[]()[]()

#### Orientation9+

窗口显示方向类型枚举。

名称值说明UNSPECIFIED0

表示未定义方向模式，由系统判定。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

PORTRAIT1

表示竖屏显示模式。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

LANDSCAPE2

表示横屏显示模式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

PORTRAIT_INVERTED3

表示反向竖屏显示模式。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

LANDSCAPE_INVERTED4

表示反向横屏显示模式。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

AUTO_ROTATION5

跟随传感器自动旋转，可以旋转到竖屏、横屏、反向竖屏、反向横屏四个方向，且不受控制中心的旋转开关控制。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

AUTO_ROTATION_PORTRAIT6

跟随传感器自动竖向旋转，可以旋转到竖屏、反向竖屏，无法旋转到横屏、反向横屏，且不受控制中心的旋转开关控制。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

AUTO_ROTATION_LANDSCAPE7

跟随传感器自动横向旋转，可以旋转到横屏、反向横屏，无法旋转到竖屏、反向竖屏，且不受控制中心的旋转开关控制。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

AUTO_ROTATION_RESTRICTED8

跟随传感器自动旋转，可以旋转到竖屏、横屏、反向竖屏、反向横屏四个方向，且受控制中心的旋转开关控制。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

AUTO_ROTATION_PORTRAIT_RESTRICTED9

跟随传感器自动竖向旋转，可以旋转到竖屏、反向竖屏，无法旋转到横屏、反向横屏，且受控制中心的旋转开关控制。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

AUTO_ROTATION_LANDSCAPE_RESTRICTED10

跟随传感器自动横向旋转，可以旋转到横屏、反向横屏，无法旋转到竖屏、反向竖屏，且受控制中心的旋转开关控制。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

LOCKED11

表示锁定模式，窗口显示方向与屏幕当前方向一致。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

AUTO_ROTATION_UNSPECIFIED12+12

跟随传感器自动旋转，受控制中心的旋转开关控制，且可旋转方向受系统判定（如在某种设备，可以旋转到竖屏、横屏、反向横屏三个方向，无法旋转到反向竖屏）。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

USER_ROTATION_PORTRAIT12+13

调用时临时旋转到竖屏，之后跟随传感器自动旋转，受控制中心的旋转开关控制，且可旋转方向受系统判定。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

USER_ROTATION_LANDSCAPE12+14

调用时临时旋转到横屏，之后跟随传感器自动旋转，受控制中心的旋转开关控制，且可旋转方向受系统判定。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

USER_ROTATION_PORTRAIT_INVERTED12+15

调用时临时旋转到反向竖屏，之后跟随传感器自动旋转，受控制中心的旋转开关控制，且可旋转方向受系统判定。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

USER_ROTATION_LANDSCAPE_INVERTED12+16

调用时临时旋转到反向横屏，之后跟随传感器自动旋转，受控制中心的旋转开关控制，且可旋转方向受系统判定。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

FOLLOW_DESKTOP12+17

表示跟随桌面的旋转模式，如果桌面可以旋转则可旋转，桌面不可旋转则不可旋转。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

[]()[]()

#### RectChangeReason12+

窗口矩形（窗口位置及窗口大小）变化的原因。

**系统能力：** SystemCapability.Window.SessionManager

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

名称值说明UNDEFINED0默认值。MAXIMIZE1窗口最大化。RECOVER2窗口恢复到上一次的状态。MOVE3窗口拖拽移动。DRAG4窗口拖拽缩放。DRAG_START5窗口开始拖拽缩放。DRAG_END6窗口结束拖拽缩放。[]()[]()

#### ColorSpace8+

色域模式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

名称值说明DEFAULT0默认SRGB色域模式。WIDE_GAMUT1广色域模式。[]()[]()

#### WindowEventType10+

窗口生命周期。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

名称值说明WINDOW_SHOWN1

切到前台。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

WINDOW_ACTIVE2

获焦状态。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

WINDOW_INACTIVE3

失焦状态。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

WINDOW_HIDDEN4

切到后台。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

WINDOW_DESTROYED11+7

窗口销毁。

**系统能力：** SystemCapability.Window.SessionManager

[]()[]()

#### WindowStatusType11+

窗口模式枚举。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

名称值说明UNDEFINED0表示APP未定义窗口模式。FULL_SCREEN1表示APP全屏模式，在2in1设备中，窗口铺满整个屏幕，且无dock栏和状态栏。MAXIMIZE2表示APP窗口最大化模式，在2in1设备中，窗口铺满整个屏幕，有dock栏和状态栏。MINIMIZE3表示APP窗口最小化模式。FLOATING4表示APP自由悬浮形式窗口模式。SPLIT_SCREEN5表示APP分屏模式。[]()[]()

#### PixelUnit22+

像素单位枚举。

物理像素单位和虚拟像素单位换算可使用[px2vp](../../types/classes/Class (UIContext).md#ZH-CN_TOPIC_0000002529444749__px2vp12)和[vp2px](../../types/classes/Class (UIContext).md#ZH-CN_TOPIC_0000002529444749__vp2px12)。

**系统能力：** SystemCapability.Window.SessionManager

名称值说明PX0物理像素单位（px）。VP1虚拟像素单位（vp）。[]()[]()

#### MaximizePresentation12+

窗口最大化时的布局枚举。

**系统能力：** SystemCapability.Window.SessionManager

名称值说明FOLLOW_APP_IMMERSIVE_SETTING0

最大化时，跟随应用app当前设置的全屏模式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

EXIT_IMMERSIVE1

最大化时，如果当前窗口设置了全屏模式会退出全屏模式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

ENTER_IMMERSIVE2

最大化时，进入全屏模式，鼠标Hover在热区上显示窗口标题栏和dock栏。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

ENTER_IMMERSIVE_DISABLE_TITLE_AND_DOCK_HOVER14+3

最大化时，进入全屏模式，鼠标Hover在热区上不显示窗口标题栏和dock栏。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

[]()[]()

#### WindowAnimationCurve20+

窗口动画曲线类型。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

名称值说明LINEAR0

表示动画从头到尾的速度都是相同的。

使用该曲线类型时[WindowAnimationConfig](../../types/interfaces/Interfaces (其他) (arkts-apis-window-i).md#ZH-CN_TOPIC_0000002529284795__windowanimationconfig20)中duration必填。

使用该曲线类型时[WindowAnimationConfig](../../types/interfaces/Interfaces (其他) (arkts-apis-window-i).md#ZH-CN_TOPIC_0000002529284795__windowanimationconfig20)中param选填，且不生效。

INTERPOLATION_SPRING1

表示插值器弹簧曲线，一条从0到1的动画曲线，实际动画值根据曲线进行插值计算。动画时间由曲线参数决定，不受[WindowAnimationConfig](../../types/interfaces/Interfaces (其他) (arkts-apis-window-i).md#ZH-CN_TOPIC_0000002529284795__windowanimationconfig20)中的duration参数控制。

使用该曲线类型时[WindowAnimationConfig](../../types/interfaces/Interfaces (其他) (arkts-apis-window-i).md#ZH-CN_TOPIC_0000002529284795__windowanimationconfig20)中duration选填，且不生效。

使用该曲线类型时[WindowAnimationConfig](../../types/interfaces/Interfaces (其他) (arkts-apis-window-i).md#ZH-CN_TOPIC_0000002529284795__windowanimationconfig20)中param必填。

CUBIC_BEZIER2

表示贝塞尔曲线。

使用该曲线类型时[WindowAnimationConfig](../../types/interfaces/Interfaces (其他) (arkts-apis-window-i).md#ZH-CN_TOPIC_0000002529284795__windowanimationconfig20)中的param和duration为必填项。

[]()[]()

#### WindowTransitionType20+

窗口转场动画类型枚举。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

名称值说明DESTROY0表示窗口销毁时的转场动画。[]()[]()

#### AnimationType20+

窗口动画类型枚举。

**系统能力：** SystemCapability.Window.SessionManager

名称值说明FADE_IN_OUT0表示窗口动画类型为淡入淡出。淡入动画在窗口显示过程中生效，淡出动画在窗口隐藏过程中生效。[]()[]()

#### WindowAnchor20+

窗口锚点枚举。

**系统能力：** SystemCapability.Window.SessionManager

名称值说明TOP_START0窗口左上角。TOP1窗口上边界横向居中点。TOP_END2窗口右上角。START3窗口左边界纵向居中点。CENTER4窗口横向和纵向居中点。END5窗口右边界纵向居中点。BOTTOM_START6窗口左下角。BOTTOM7窗口下边界横向居中点。BOTTOM_END8窗口右下角。[]()[]()

#### RotationChangeType19+

窗口旋转事件类型。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

名称值说明WINDOW_WILL_ROTATE0窗口即将旋转。WINDOW_DID_ROTATE1窗口旋转结束。[]()[]()

#### RectType19+

窗口矩形区域坐标系类型。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

名称值说明RELATIVE_TO_SCREEN0窗口矩形区域相对于屏幕坐标系。RELATIVE_TO_PARENT_WINDOW1窗口矩形区域相对于父窗口坐标系。[]()[]()

#### GlobalWindowMode20+

窗口模式。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

名称值说明FULLSCREEN1全屏窗口，二进制从右往左，第一个二进制位为1。SPLIT1 << 1分屏窗口，二进制从右往左，第二个二进制位为1。FLOAT1 << 2悬浮窗，二进制从右往左，第三个二进制位为1。PIP1 << 3画中画，二进制从右往左，第四个二进制位为1。[]()[]()

#### OcclusionState22+

窗口可见性状态枚举。

**系统能力：** SystemCapability.Window.SessionManager

名称值说明NO_OCCLUSION0窗口完全可见（没有任何部分被其他非透明窗口遮挡）。PARTIAL_OCCLUSION1窗口部分可见（部分被其他非透明窗口遮挡）。FULL_OCCLUSION2窗口完全不可见（完全被其他非透明窗口遮挡，或窗口最小化，或窗口隐藏）。[]()[]()

#### WindowStageEventType9+

WindowStage生命周期状态枚举。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

名称值说明SHOWN1前台状态，例如点击应用图标启动，无论是首次启动还是从后台启动均会触发。ACTIVE2获焦状态，例如应用窗口处理点击事件后的状态、应用启动后的状态。INACTIVE3失焦状态，例如打开新应用或点击其他窗口后，原获焦窗口的状态。HIDDEN4后台状态，例如应用上滑退出、应用窗口关闭。RESUMED11+5前台可交互状态，例如打开应用后，应用处于前台，且可以与用户交互的状态。PAUSED11+6前台不可交互状态，例如应用在前台时，进入多任务界面，应用依然处于前台但不可以与用户交互的状态。[]()[]()

#### WindowStageLifecycleEventType20+

WindowStage生命周期的状态类型枚举。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Window.SessionManager

名称值说明SHOWN1切到前台，例如点击应用图标启动，无论是首次启动还是从后台启动均会触发。RESUMED2前台可交互状态，例如打开应用后，应用处于前台，且可以与用户交互的状态。PAUSED3前台不可交互状态，例如应用在前台时，进入多任务界面，应用依然处于前台但不可以与用户交互的状态。HIDDEN4切到后台，例如应用上滑退出、应用窗口关闭。[]()[]()

#### ModalityType14+

子窗口模态类型枚举。

**系统能力：** SystemCapability.Window.SessionManager

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

名称值说明WINDOW_MODALITY0模态子窗类型为模窗口子窗，当仅需要其父级窗口不响应用户操作时，可选此参数。APPLICATION_MODALITY1

模态子窗类型为模应用子窗，该窗口仅在[自由窗口](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/window-terminology#自由窗口)状态下生效。

除其父级窗口外还需要该应用其他实例的窗口不响应用户操作时，可选此参数。

**设备行为差异：** 该枚举在2in1设备、Tablet设备中可正常调用，在其他设备类型中作为入参使用时，对应接口返回801错误码。

[]()[]()

#### ScreenshotEventType20+

截屏事件类型枚举。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

名称值说明SYSTEM_SCREENSHOT0系统截屏成功。SYSTEM_SCREENSHOT_ABORT1系统截屏中止。SCROLL_SHOT_START2滚动截屏开始。SCROLL_SHOT_END3滚动截屏结束。SCROLL_SHOT_ABORT4滚动截屏中止。