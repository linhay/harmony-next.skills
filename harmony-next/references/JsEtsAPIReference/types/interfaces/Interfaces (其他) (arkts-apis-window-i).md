[]()[]()

# Interfaces (其他)

-

本模块首批接口从API version 6开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

-

针对系统能力SystemCapability.Window.SessionManager，请先使用[canIUse()](../../topics/misc/SysCap (系统能力).md#ZH-CN_TOPIC_0000002529286149__caniuse)接口判断当前设备是否支持此syscap及对应接口。

[]()[]()

#### Configuration9+

创建子窗口或系统窗口时的参数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

名称类型只读可选说明namestring否否

窗口名字。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

windowType[WindowType](../../topics/networking/Enums (arkts-apis-window-e).md#ZH-CN_TOPIC_0000002529444769__windowtype7)否否

窗口类型。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

ctx[BaseContext](../../topics/graphics/BaseContext.md)否是

当前应用上下文信息。不设置，则默认为空。

FA模型下不需要使用该参数，即可创建子窗口，使用该参数时会报错。

Stage模型必须使用该参数，用于创建悬浮窗、模态窗或系统窗口。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

displayIdnumber否是

当前物理屏幕id。不设置，则默认为-1，该参数应为整数。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

parentIdnumber否是

父窗口id。不设置，则默认为-1，该参数应为整数。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

decorEnabled12+boolean否是

是否显示窗口装饰，仅在windowType为TYPE_DIALOG时生效。true表示显示，false表示不显示。此参数默认值为false。

**系统能力：** SystemCapability.Window.SessionManager

title12+string否是

decorEnabled属性设置为true时，窗口的标题内容。标题显示区域最右端不超过系统三键区域最左端，超过部分以省略号表示。不设置，则默认为空字符串。

**系统能力：** SystemCapability.Window.SessionManager

[]()[]()

#### SystemBarProperties

状态栏属性。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

名称类型只读可选说明statusBarColorstring否是

状态栏背景颜色，为十六进制RGB或ARGB颜色，不区分大小写，例如'#00FF00'或'#FF00FF00'。默认值：'#66000000'。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

isStatusBarLightIcon7+boolean否是

状态栏图标是否为高亮状态。true表示高亮；false表示不高亮。默认值：false。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

statusBarContentColor8+string否是

状态栏文字颜色。当设置此属性后，isStatusBarLightIcon属性设置无效。默认值：'#E5FFFFFF'。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

navigationBarColorstring否是

三键导航栏背景颜色，为十六进制RGB或ARGB颜色，不区分大小写，例如'#00FF00'或'#FF00FF00'。默认值：'#66000000'。

HarmonyOS各设备不支持此能力。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

isNavigationBarLightIcon7+boolean否是

三键导航栏图标是否为高亮状态。true表示高亮；false表示不高亮。默认值：false。

HarmonyOS各设备不支持此能力。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

navigationBarContentColor8+string否是

三键导航栏文字颜色。当设置此属性后，isNavigationBarLightIcon属性设置无效。默认值：'#E5FFFFFF'。

HarmonyOS各设备不支持此能力。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

enableStatusBarAnimation12+boolean否是

是否启用状态栏属性变化时的动画效果。true表示启用；false表示不启用。默认值：false。

**系统能力：** SystemCapability.Window.SessionManager

enableNavigationBarAnimation12+boolean否是

是否启用三键导航栏属性变化时的动画效果。true表示启用；false表示不启用。默认值：false。

HarmonyOS各设备不支持此能力。

**系统能力：** SystemCapability.Window.SessionManager

[]()[]()

#### StatusBarProperty18+

状态栏的属性。在获取状态栏属性信息时返回。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

名称类型只读可选说明contentColorstring否否

状态栏文字颜色，固定为ARGB格式，如：#E5FFFFFF。

**系统能力：** SystemCapability.Window.SessionManager

[]()[]()

#### SystemBarStyle12+

状态栏的属性。在设置页面级状态栏属性时使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

名称类型只读可选说明statusBarContentColorstring否是状态栏文字颜色。默认值：'#E5FFFFFF'。[]()[]()

#### FrameMetrics22+

帧率指标。

**系统能力：** SystemCapability.Window.SessionManager

名称类型只读可选说明firstDrawFrameboolean否否是否是首帧。true表示首帧，false表示非首帧。inputHandlingDurationnumber否否一帧中的手势处理耗时（单位：纳秒）。layoutMeasureDurationnumber否否一帧中的布局测量耗时（单位：纳秒）。vsyncTimestampnumber否否当前帧的开始时间戳（单位：纳秒）。[]()[]()

#### Rect7+

窗口矩形区域。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

名称类型只读可选说明leftnumber否否矩形区域的左边界，单位为px，该参数为整数。topnumber否否矩形区域的上边界，单位为px，该参数应为整数。widthnumber否否矩形区域的宽度，单位为px，该参数应为整数。heightnumber否否矩形区域的高度，单位为px，该参数应为整数。[]()[]()

#### AvoidArea7+

窗口内容的避让区域。

窗口内容做[沉浸式布局](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/window-terminology#沉浸式布局)适配时，需要按照[AvoidAreaType](../../topics/networking/Enums (arkts-apis-window-e).md#ZH-CN_TOPIC_0000002529444769__avoidareatype7)对应的AvoidArea做窗口内容避让。

在避让区域内，应用窗口内容被遮挡且无法响应用户点击事件。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

名称类型只读可选说明visible9+boolean否否避让区域是否可见。true表示可见；false表示不可见。leftRect[Rect](Interfaces (其他) (arkts-apis-window-i).md#ZH-CN_TOPIC_0000002529284795__rect7)否否中心位于窗口的两条对角线的左侧的矩形区。topRect[Rect](Interfaces (其他) (arkts-apis-window-i).md#ZH-CN_TOPIC_0000002529284795__rect7)否否中心位于窗口的两条对角线的顶部的矩形区。rightRect[Rect](Interfaces (其他) (arkts-apis-window-i).md#ZH-CN_TOPIC_0000002529284795__rect7)否否中心位于窗口的两条对角线的右侧的矩形区。bottomRect[Rect](Interfaces (其他) (arkts-apis-window-i).md#ZH-CN_TOPIC_0000002529284795__rect7)否否中心位于窗口的两条对角线的底部的矩形区。

示意图展示了leftRect、topRect、rightRect、bottomRect的含义。

[]()[]()

#### Size7+

窗口大小。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

名称类型只读可选说明widthnumber否否窗口宽度，单位为px，该参数应为整数。heightnumber否否窗口高度，单位为px，该参数应为整数。[]()[]()

#### Position20+

窗口或组件的位置。

**系统能力：** SystemCapability.Window.SessionManager

名称类型只读可选说明xnumber否否x坐标，单位为px，该参数应为整数。ynumber否否y坐标，单位为px，该参数应为整数。[]()[]()

#### RectChangeOptions12+

窗口矩形（窗口位置及窗口大小）变化返回的值及变化原因。

**系统能力：** SystemCapability.Window.SessionManager

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

名称类型只读可选说明rect[Rect](Interfaces (其他) (arkts-apis-window-i).md#ZH-CN_TOPIC_0000002529284795__rect7)否否窗口矩形变化后的值。reason[RectChangeReason](../../topics/networking/Enums (arkts-apis-window-e).md#ZH-CN_TOPIC_0000002529444769__rectchangereason12)否否窗口矩形变化的原因。[]()[]()

#### AvoidAreaOptions12+

系统规避区变化后返回当前规避区域以及规避区域类型。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

名称类型只读可选说明type[AvoidAreaType](../../topics/networking/Enums (arkts-apis-window-e).md#ZH-CN_TOPIC_0000002529444769__avoidareatype7)否否系统规避区变化后返回的规避区域类型。area[AvoidArea](Interfaces (其他) (arkts-apis-window-i).md#ZH-CN_TOPIC_0000002529284795__avoidarea7)否否系统规避区变化后返回的规避区域。[]()[]()

#### WindowProperties

窗口属性。

名称类型只读可选说明windowRect7+[Rect](Interfaces (其他) (arkts-apis-window-i).md#ZH-CN_TOPIC_0000002529284795__rect7)否否

窗口尺寸，可在页面生命周期[onPageShow](../../topics/misc/自定义组件的生命周期.md#ZH-CN_TOPIC_0000002529444913__onpageshow)或应用生命周期[onForeground](../../modules/ohos/@ohos.app.ability.UIAbility (带界面的应用组件).md#ZH-CN_TOPIC_0000002529444559__onforeground)阶段获取。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

drawableRect11+[Rect](Interfaces (其他) (arkts-apis-window-i).md#ZH-CN_TOPIC_0000002529284795__rect7)否否

窗口内的可绘制区域尺寸，其中左边界上边界是相对于窗口左上顶点计算。在Stage模型下，需要在调用[loadContent()](Interface (Window).md#ZH-CN_TOPIC_0000002497604802__loadcontent9)或[setUIContent()](Interface (Window).md#ZH-CN_TOPIC_0000002497604802__setuicontent9)加载页面内容后获取该属性。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

type7+[WindowType](../../topics/networking/Enums (arkts-apis-window-e).md#ZH-CN_TOPIC_0000002529444769__windowtype7)否否

窗口类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

isFullScreenboolean否否

在满足isLayoutFullScreen为true的条件下如果隐藏了状态栏，返回值为true，其他情况下均返回false。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

isLayoutFullScreen7+boolean否否

对于子窗，如果设置了[沉浸式布局](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/window-terminology#沉浸式布局)，返回值为true。

对于主窗，如果设置了[沉浸式布局](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/window-terminology#沉浸式布局)且处于全屏模式，返回值为true。

其他情况下均返回false

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

focusable7+boolean否否

窗口是否可获焦。true表示可获焦；false表示不可获焦。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

touchable7+boolean否否

窗口是否可触摸。true表示可触摸；false表示不可触摸。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

brightnessnumber否否

窗口亮度。通过[setWindowBrightness()](Interface (Window).md#ZH-CN_TOPIC_0000002497604802__setwindowbrightness9)设置窗口的亮度值。该参数为浮点数，可设置的亮度范围为[0.0, 1.0]或-1.0，其取值1.0时表示最大亮度，取值-1.0时，表示亮度跟随系统。如果窗口没有设置亮度值，表示亮度跟随系统，此时获取到的亮度值为-1.0。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

dimBehindValue(deprecated)number否否

下层窗口的暗度值。该参数为浮点数，取值范围为[0.0, 1.0]，其取1.0表示最暗。

**说明：** 从API version 7开始支持，从API version 9开始废弃，当前无可替代接口。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

isKeepScreenOnboolean否否

屏幕是否常亮。true表示常亮；false表示不常亮。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

isPrivacyMode7+boolean否否

窗口是否为隐私模式。true表示窗口为隐私模式；false表示窗口为非隐私模式。可通过[setWindowPrivacyMode()](Interface (Window).md#ZH-CN_TOPIC_0000002497604802__setwindowprivacymode9)设置窗口的隐私模式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

isRoundCorner(deprecated)boolean否否

窗口是否为圆角。true表示窗口为圆角；false表示窗口为非圆角。

**说明：** 从API version 7开始支持，从API version 9开始废弃，当前无可替代接口。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

isTransparent7+boolean否否

窗口背景是否透明。true表示透明；false表示不透明。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

id9+number否否

窗口ID，该参数为整数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

displayId12+number否是

窗口所在屏幕ID，默认返回主屏幕ID，该参数为整数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

name18+string否是

窗口名称，默认为空字符串。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

globalDisplayRect20+[Rect](Interfaces (其他) (arkts-apis-window-i).md#ZH-CN_TOPIC_0000002529284795__rect7)否是

全局坐标系下的窗口尺寸。扩展屏场景下以主屏左上角为坐标原点，虚拟屏场景下以虚拟屏左上角为坐标原点。默认值：[0, 0, 0, 0]。

**系统能力：** SystemCapability.Window.SessionManager

[]()[]()

#### DecorButtonStyle14+

系统装饰栏按钮样式。

**系统能力：** SystemCapability.Window.SessionManager

名称类型只读可选说明colorMode[ConfigurationConstant.ColorMode](../../modules/ohos/@ohos.app.ability.ConfigurationConstant (环境变量相关的常量定义).md#ZH-CN_TOPIC_0000002497604608__colormode)否是

颜色模式。深色模式下按钮颜色适配为浅色，浅色模式下按钮颜色适配为深色。未设置则默认跟随系统颜色模式。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

buttonBackgroundSizenumber否是

按钮高亮显示时的大小，取值范围20vp-40vp，默认值28vp。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

spacingBetweenButtonsnumber否是

按钮间距，取值范围8vp-24vp，默认值12vp。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

closeButtonRightMarginnumber否是

关闭按钮右侧距窗口边距，取值范围6vp-22vp，默认值20vp。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

buttonIconSize20+number否是

按键icon的大小，取值范围16vp-24vp，默认值20vp。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

buttonBackgroundCornerRadius20+number否是

按键背板圆角半径，取值范围4vp-8vp，默认值4vp。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

[]()[]()

#### WindowLimits11+

窗口尺寸限制参数。应用可以通过[getWindowLimits](Interface (Window).md#ZH-CN_TOPIC_0000002497604802__getwindowlimits11)获得当前的窗口尺寸限制。

窗口存在默认系统大小限制，应用可以通过[setWindowLimits](Interface (Window).md#ZH-CN_TOPIC_0000002497604802__setwindowlimits11)设置窗口尺寸限制，或在应用[module.json5配置文件中的abilities标签](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/module-configuration-file#abilities标签)中配置该属性。

从API version 17开始，还可以在[startAbility](../../topics/graphics/UIAbilityContext.md#ZH-CN_TOPIC_0000002497604628__startability-2)拉起窗口时通过[StartOptions](../../modules/ohos/@ohos.app.ability.StartOptions (startAbility的可选参数).md#ZH-CN_TOPIC_0000002529284585__startoptions)指定窗口尺寸限制。

最终生效结果由默认系统限制和应用设置的数据取交集得到。

**系统能力：** SystemCapability.Window.SessionManager

名称类型只读可选说明maxWidthnumber否是

窗口的最大宽度。默认单位为px，从API version 22开始，支持通过pixelUnit设置单位为px或vp。该参数为整数。默认值为0，表示该属性不发生变化。下限值为0，上限值为系统限定的最大宽度。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

maxHeightnumber否是

窗口的最大高度。默认单位为px，从API version 22开始，支持通过pixelUnit设置单位为px或vp。该参数为整数。默认值为0，表示该属性不发生变化。下限值为0，上限值为系统限定的最大高度。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

minWidthnumber否是

窗口的最小宽度。默认单位为px，从API version 22开始，支持通过pixelUnit设置单位为px或vp。该参数为整数。默认值为0，表示该属性不发生变化。下限值为0，上限值为系统限定的最小宽度。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

minHeightnumber否是

窗口的最小高度。默认单位为px，从API version 22开始，支持通过pixelUnit设置单位为px或vp。该参数为整数。默认值为0，表示该属性不发生变化。下限值为0，上限值为系统限定的最小高度。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

pixelUnit22+[PixelUnit](../../topics/networking/Enums (arkts-apis-window-e).md#ZH-CN_TOPIC_0000002529444769__pixelunit22)否是窗口尺寸限制的单位，默认为px。可显式设置为px或vp。[]()[]()

#### TitleButtonRect11+

标题栏上的最小化、最大化、关闭按钮矩形区域，该区域位置坐标相对窗口右上角。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

名称类型只读可选说明rightnumber否否矩形区域的右边界，单位为vp，该参数为整数。topnumber否否矩形区域的上边界，单位为vp，该参数为整数。widthnumber否否矩形区域的宽度，单位为vp，该参数为整数。heightnumber否否矩形区域的高度，单位为vp，该参数为整数。[]()[]()

#### MoveConfiguration15+

窗口移动选项。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

名称类型只读可选说明displayIdnumber否是目标屏幕ID，该参数应为整数，输入非整数时将向下取整。填入该参数时，将移动到相对于目标屏幕左上角的指定位置。此参数不填或传入目标屏幕ID不存在时，将移动到相对于当前屏幕左上角的指定位置。[]()[]()

#### WindowDensityInfo15+

窗口所在显示设备和窗口自定义的显示密度信息，是与像素单位无关的缩放系数，即显示大小缩放系数。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

名称类型只读可选说明systemDensitynumber否否窗口所在屏幕的系统显示大小缩放系数，跟随用户设置变化，该参数变化范围为0.5-4.0。defaultDensitynumber否否窗口所在屏幕的系统默认显示大小缩放系数，跟随窗口所在屏幕变化，该参数变化范围为0.5-4.0。customDensitynumber否否窗口自定义设置的显示大小缩放系数，该参数取值范围为0.5-4.0。未设置该参数时，将跟随系统显示大小缩放系数变化。该参数仅主窗口生效，在子窗或系统窗口上等于系统显示大小缩放系数(systemDensity)。[]()[]()

#### WindowLayoutInfo15+

窗口布局信息。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

名称类型只读可选说明windowRect[Rect](Interfaces (其他) (arkts-apis-window-i).md#ZH-CN_TOPIC_0000002529284795__rect7)否否窗口尺寸，窗口在屏幕上的实际位置和大小。[]()[]()

#### KeyboardInfo18+

软键盘窗口信息。

**系统能力：** SystemCapability.Window.SessionManager

名称类型只读可选说明beginRect[Rect](Interfaces (其他) (arkts-apis-window-i).md#ZH-CN_TOPIC_0000002529284795__rect7)否否

动画开始前软键盘的位置和大小。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

endRect[Rect](Interfaces (其他) (arkts-apis-window-i).md#ZH-CN_TOPIC_0000002529284795__rect7)否否

动画结束后软键盘的位置和大小。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

animated20+boolean否是

当前是否有显示/隐藏动画，true表示有动画，false表示没有。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

config20+[WindowAnimationConfig](Interfaces (其他) (arkts-apis-window-i).md#ZH-CN_TOPIC_0000002529284795__windowanimationconfig20)否是

动画配置信息。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

[]()[]()

#### ShowWindowOptions20+

显示子窗口或系统窗口时的参数。

**系统能力：** SystemCapability.Window.SessionManager

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

名称类型只读可选说明focusOnShowboolean否是窗口调用[showWindow()](Interface (Window).md#ZH-CN_TOPIC_0000002497604802__showwindow20)显示时是否自动获焦，默认为true。该参数对主窗、模态窗、dialog窗口不生效。[]()[]()

#### WindowAnimationConfig20+

窗口动画参数配置。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

名称类型只读可选说明curve[WindowAnimationCurve](../../topics/networking/Enums (arkts-apis-window-e).md#ZH-CN_TOPIC_0000002529444769__windowanimationcurve20)否否动画曲线类型。durationnumber否是

动画播放的时长，单位毫秒（ms）。

默认值：0，最大值：3000。

根据动画曲线类型决定是否必填。

param[WindowAnimationCurveParam](../../topics/networking/Types (arkts-apis-window-t).md#ZH-CN_TOPIC_0000002497604804__windowanimationcurveparam20)否是动画曲线参数，根据动画曲线类型决定是否必填。[]()[]()

#### WindowInfo18+

当前窗口的详细信息。

**系统能力：** SystemCapability.Window.SessionManager

名称类型只读可选说明rect[Rect](Interfaces (其他) (arkts-apis-window-i).md#ZH-CN_TOPIC_0000002529284795__rect7)否否窗口尺寸。bundleNamestring否否应用Bundle的名称。abilityNamestring否否Ability的名称。windowIdnumber否否窗口ID。windowStatusType[WindowStatusType](../../topics/networking/Enums (arkts-apis-window-e).md#ZH-CN_TOPIC_0000002529444769__windowstatustype11)否否窗口模式枚举。isFocusedboolean否是窗口是否获焦。true表示窗口获焦；false表示窗口未获焦。返回值与[isFocused()](Interface (Window).md#ZH-CN_TOPIC_0000002497604802__isfocused12)接口一致。globalDisplayRect20+[Rect](Interfaces (其他) (arkts-apis-window-i).md#ZH-CN_TOPIC_0000002529284795__rect7)否是全局坐标系下的窗口尺寸。扩展屏场景下以主屏左上角为坐标原点，虚拟屏场景下以虚拟屏左上角为坐标原点。默认值：[0, 0, 0, 0]。[]()[]()

#### TransitionAnimation20+

窗口转场动画配置。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

名称类型只读可选说明config[WindowAnimationConfig](Interfaces (其他) (arkts-apis-window-i).md#ZH-CN_TOPIC_0000002529284795__windowanimationconfig20)否否本次转场动画配置。opacitynumber否是不透明度，转场动画作用的窗口属性，值为0时窗口完全透明，默认值为1.0。当动画类型为WindowTransitionType.DESTROY时，代表动画终点的不透明度。取值范围0~1.0，在动画结束时恢复为1.0。[]()[]()

#### StartAnimationParams20+

启动动画配置。

仅对同应用的不同ability间跳转生效。

仅对全屏应用生效。

**系统能力：** SystemCapability.Window.SessionManager

名称类型只读可选说明type[AnimationType](../../topics/networking/Enums (arkts-apis-window-e).md#ZH-CN_TOPIC_0000002529444769__animationtype20)否否窗口动画类型。

**设备行为差异：** 该接口在Phone设备、Tablet设备的非[自由多窗模式](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/window-terminology#自由多窗模式)下可正常调用，在其他设备中不生效也不报错。

[]()[]()

#### WindowCreateParams20+

应用启动时的窗口参数配置。

**系统能力：** SystemCapability.Window.SessionManager

名称类型只读可选说明animationParams[StartAnimationParams](Interfaces (其他) (arkts-apis-window-i).md#ZH-CN_TOPIC_0000002529284795__startanimationparams20)否是启动动画参数配置。默认值为undefined，若不配置将保持系统默认动效。[]()[]()

#### Callback15+

[]()[]()

#### (data: T)15+

(data: T): V

通用回调函数。

开发者在使用时，可自定义data的参数类型，回调函数返回对应类型的信息。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

参数名类型必填说明dataT是回调函数调用时需要传入T类型的参数。

**返回值：**

类型说明V回调函数需要返回V类型的返回值。[]()[]()

#### RotationChangeInfo19+

窗口旋转变化时的窗口信息。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

名称类型只读可选说明type[RotationChangeType](../../topics/networking/Enums (arkts-apis-window-e).md#ZH-CN_TOPIC_0000002529444769__rotationchangetype19)否否窗口旋转事件类型。orientationnumber否否

窗口显示方向。

- 0表示竖屏。

- 1表示反向横屏。

- 2表示反向竖屏。

- 3表示横屏。

开发者在使用时，需要注意该方向与display对象的属性orientation含义不一致。

displayIdnumber否否窗口所在屏幕Id。displayRect[Rect](Interfaces (其他) (arkts-apis-window-i).md#ZH-CN_TOPIC_0000002529284795__rect7)否否窗口所在屏幕旋转后的矩形区域大小。[]()[]()

#### RotationChangeResult19+

应用在窗口旋转变化时返回的信息，系统会根据此信息改变当前窗口矩形区域大小。当返回主窗口旋转变化的信息时，系统不改变主窗口的大小。

应用窗口与系统窗口大小存在限制，具体限制与相关规则可见[resize](Interface (Window).md#ZH-CN_TOPIC_0000002497604802__resize9)。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

名称类型只读可选说明rectType[RectType](../../topics/networking/Enums (arkts-apis-window-e).md#ZH-CN_TOPIC_0000002529444769__recttype19)否否窗口矩形区域坐标系类型。windowRect[Rect](Interfaces (其他) (arkts-apis-window-i).md#ZH-CN_TOPIC_0000002529284795__rect7)否否相对于屏幕或父窗坐标系的窗口矩形区域信息。[]()[]()

#### SubWindowOptions11+

子窗口创建参数。

**系统能力：** SystemCapability.Window.SessionManager

名称类型只读可选说明title11+string否否

子窗口标题。标题显示区域最右端不超过系统三键区域最左端，超过部分以省略号表示。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

decorEnabled11+boolean否否

子窗口是否显示装饰。true表示子窗口显示装饰，false表示子窗口不显示装饰。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

isModal12+boolean否是

子窗口是否启用模态属性。true表示子窗口启用模态属性，false表示子窗口禁用模态属性。不设置，则默认为false。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

modalityType14+[ModalityType](../../topics/networking/Enums (arkts-apis-window-e).md#ZH-CN_TOPIC_0000002529444769__modalitytype14)否是

子窗口模态类型，仅当子窗口启用模态属性时生效。WINDOW_MODALITY表示子窗口模态类型为模窗口子窗，APPLICATION_MODALITY表示子窗口模态类型为模应用子窗。不设置，则默认为WINDOW_MODALITY。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

windowRect18+[Rect](Interfaces (其他) (arkts-apis-window-i).md#ZH-CN_TOPIC_0000002529284795__rect7)否是

子窗口矩形区域，其中子窗口存在大小限制，具体参考[resize()](Interface (Window).md#ZH-CN_TOPIC_0000002497604802__resize9)方法。不设置且未调用[showWindow()](Interface (Window).md#ZH-CN_TOPIC_0000002497604802__showwindow9)显示前，则默认为{left: 0, top: 0, width: 0, height: 0}。具体参考[设置应用子窗口](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/application-window-stage#设置应用子窗口)开发指南。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

zLevel18+number否是

子窗口层级级别，仅当子窗口未启用模态属性，即未设置isModal时生效。该参数是整数，取值范围为[-10000, 10000]，浮点数输入将向下取整。不设置，则默认为0。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

maximizeSupported19+boolean否是

子窗口是否支持最大化特性。true表示子窗口支持最大化，false表示子窗口不支持最大化。不设置，则默认为false。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**设备行为差异：** 该参数在2in1设备、Tablet设备的[自由多窗模式](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/window-terminology#自由多窗模式)下可正常调用，在其他设备类型中作为入参使用时，对应接口不生效不报错。

outlineEnabled20+boolean否是

子窗口是否显示描边。true表示子窗口显示描边，false表示子窗口不显示描边。不设置，则默认为false。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**设备行为差异：** 该参数在2in1设备中可正常调用，在其他设备类型中作为入参使用时，对应接口不生效不报错。

[]()[]()

#### KeyFramePolicy20+

关键帧的策略配置。

**系统能力：** SystemCapability.Window.SessionManager

名称类型只读可选说明enableboolean否否是否开启关键帧。true表示开启，false表示关闭。intervalnumber否是设置关键帧布局切换的拖拽时间间隔，单位为毫秒，默认值为1000。取值为正整数，浮点数向下取整。与distance判断为或的关系：满足其一即开始布局切换。distancenumber否是设置关键帧布局切换的拖拽距离间隔，单位为px，默认值为1000。取值为0或正整数，浮点数向下取整。设置为0时，忽略拖拽距离因素。与interval判断为或的关系：满足其一即开始布局切换。animationDurationnumber否是设置关键帧布局的动效切换时间，单位为毫秒，默认值为100。取值为0或正整数，浮点数向下取整。animationDelaynumber否是设置关键帧布局切换动效延迟时间，单位为毫秒，默认值为100。取值为0或正整数，浮点数向下取整。[]()[]()

#### MainWindowInfo21+

主窗口信息。

**系统能力：** SystemCapability.Window.SessionManager

名称类型只读可选说明displayIdnumber否否主窗口所在的屏幕ID。windowIdnumber否否主窗口ID。showingboolean否否主窗口的前后台状态。true表示主窗口在前台，false表示主窗口不在前台。labelstring否否主窗口的任务名称。[]()[]()

#### WindowSnapshotConfiguration21+

主窗口截图的配置项。

**系统能力：** SystemCapability.Window.SessionManager

名称类型只读可选说明useCacheboolean否是是否使用主窗口的已有截图。默认值为true。 true表示使用主窗口的已有截图，若主窗口无保存的截图，则使用主窗口的最新截图。false表示使用主窗口的最新截图。