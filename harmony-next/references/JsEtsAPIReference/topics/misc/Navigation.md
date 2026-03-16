# Navigation

Navigation组件是路由导航的根视图容器，一般作为Page页面的根容器使用，其内部默认包含了标题栏、内容区和工具栏，其中内容区默认首页显示导航内容（Navigation的子组件）或非首页显示（[NavDestination](NavDestination.md)的子组件），首页和非首页通过路由进行切换。

-

该组件从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

-

该组件从API version 11开始默认支持安全区避让特性(默认值为：expandSafeArea([SafeAreaType.SYSTEM, SafeAreaType.KEYBOARD, SafeAreaType.CUTOUT], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM]))，开发者可以重写该属性覆盖默认行为，API version 11之前的版本需配合[expandSafeArea](安全区域.md)属性实现安全区避让。

-

[NavBar](#ZH-CN_TOPIC_0000002497444902__navbar12)嵌套使用Navigation时，内层Navigation的生命周期不和外层Navigation以及[全模态](全屏模态转场.md)的生命周期进行联动。

-

Navigation未设置主副标题（[title](#ZH-CN_TOPIC_0000002497444902__title)或[subTitle](#ZH-CN_TOPIC_0000002497444902__subtitledeprecated)）且[hideBackButton](#ZH-CN_TOPIC_0000002497444902__hidebackbutton)属性设置为true时，不显示标题栏。

-

Navigation的子页面切换时，新页面会主动请求焦点。

-

在[aboutToAppear](自定义组件的生命周期.md#ZH-CN_TOPIC_0000002529444913__abouttoappear)里面不建议使用栈操作。

#### 子组件

可以包含子组件。

从API version 9开始，推荐与[NavRouter](../networking/NavRouter.md)组件搭配使用。

从API version 10开始，推荐使用[NavPathStack](#ZH-CN_TOPIC_0000002497444902__navpathstack10)配合[navDestination](#ZH-CN_TOPIC_0000002497444902__navdestination10)属性进行页面路由。

#### 接口

#### Navigation

Navigation()

创建路由导航的根视图容器，适用于使用[NavRouter](../networking/NavRouter.md)组件进行页面路由。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

#### Navigation10+

Navigation(pathInfos: NavPathStack)

绑定导航控制器到Navigation组件，适用于使用[NavPathStack](#ZH-CN_TOPIC_0000002497444902__navpathstack10)配合[navDestination](#ZH-CN_TOPIC_0000002497444902__navdestination10)属性进行页面路由。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明pathInfos[NavPathStack](#ZH-CN_TOPIC_0000002497444902__navpathstack10)是导航控制器对象。

#### Navigation20+

Navigation(pathInfos: NavPathStack, homeDestination: HomePathInfo)

绑定路由栈到Navigation组件，并且指定一个NavDestination作为Navigation的导航页（主页），适用于使用[NavPathStack](#ZH-CN_TOPIC_0000002497444902__navpathstack10)配合[navDestination](#ZH-CN_TOPIC_0000002497444902__navdestination10)属性或者系统路由表进行页面路由。使用示例参考[示例16（Navigation使用NavDestination作为导航页）](#ZH-CN_TOPIC_0000002497444902__示例16navigation使用navdestination作为导航页)。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明pathInfos[NavPathStack](#ZH-CN_TOPIC_0000002497444902__navpathstack10)是路由栈信息。homeDestination[HomePathInfo](#ZH-CN_TOPIC_0000002497444902__homepathinfo20)是主页NavDestination信息。

如果使用了主页NavDestination，则Navigation有如下变化：

-

开发者写在Navigation组件内的内容不会被创建。

-

对于Navigation的各种属性，如果主页NavDestination有对应功能的属性，则Navigation的属性不生效。

#### 属性

除支持[通用属性](通用属性.md)外，还支持以下属性：

#### title

title(value: ResourceStr | CustomBuilder | NavigationCommonTitle | NavigationCustomTitle, options?: NavigationTitleOptions)

设置页面标题。

从API version 12开始，该接口支持在[attributeModifier](动态属性设置.md#ZH-CN_TOPIC_0000002529284843__attributemodifier)中调用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明value[ResourceStr](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcestr)10+ | [CustomBuilder](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__custombuilder8) | [NavigationCommonTitle](#ZH-CN_TOPIC_0000002497444902__navigationcommontitle9)9+ | [NavigationCustomTitle](#ZH-CN_TOPIC_0000002497444902__navigationcustomtitle9)9+是

页面标题，使用NavigationCustomTitle类型设置height高度时，[titleMode](#ZH-CN_TOPIC_0000002497444902__titlemode)属性不会生效。

字符串超长时，如果不设置副标题，先缩小再换行（2行）最后截断。如果设置副标题，先缩小最后截断。

options11+[NavigationTitleOptions](#ZH-CN_TOPIC_0000002497444902__navigationtitleoptions11)否标题栏选项。 包含标题栏背景颜色、标题栏背景模糊样式及模糊选项、标题栏背景属性、标题栏布局方式、标题栏起始端内间距、标题栏结束端内间距、主标题属性修改器、子标题属性修改器、是否响应悬停态。

#### menus

menus(value: Array<NavigationMenuItem> | CustomBuilder)

设置页面右上角菜单。不设置时不显示菜单项。使用Array<[NavigationMenuItem](#ZH-CN_TOPIC_0000002497444902__navigationmenuitem)> 写法时，竖屏最多支持显示3个图标，横屏最多支持显示5个图标，多余的图标会被放入自动生成的更多图标。

不支持通过SymbolGlyphModifier对象的fontSize属性修改图标大小、effectStrategy属性修改动效、symbolEffect属性修改动效类型。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明valueArray<[NavigationMenuItem](#ZH-CN_TOPIC_0000002497444902__navigationmenuitem)> | [CustomBuilder](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__custombuilder8)是页面右上角菜单。

#### menus19+

menus(items: Array<NavigationMenuItem> | CustomBuilder, options?: NavigationMenuOptions)

设置页面右上角菜单。不设置时不显示菜单项。与[menus](#ZH-CN_TOPIC_0000002497444902__menus)相比，新增菜单选项。使用Array<[NavigationMenuItem](#ZH-CN_TOPIC_0000002497444902__navigationmenuitem)> 写法时，竖屏最多支持显示3个图标，横屏最多支持显示5个图标，多余的图标会被放入自动生成的更多图标。

该接口不支持在[attributeModifier](动态属性设置.md#ZH-CN_TOPIC_0000002529284843__attributemodifier)中调用。

不支持通过SymbolGlyphModifier对象的fontSize属性修改图标大小、effectStrategy属性修改动效、symbolEffect属性修改动效类型。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明itemsArray<[NavigationMenuItem](#ZH-CN_TOPIC_0000002497444902__navigationmenuitem)> | [CustomBuilder](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__custombuilder8)是页面右上角菜单。options[NavigationMenuOptions](#ZH-CN_TOPIC_0000002497444902__navigationmenuoptions19)否页面右上角菜单选项。

#### titleMode

titleMode(value: NavigationTitleMode)

设置页面标题栏显示模式。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明value[NavigationTitleMode](#ZH-CN_TOPIC_0000002497444902__navigationtitlemode枚举说明)是

页面标题栏显示模式。

默认值：NavigationTitleMode.Free

#### toolbarConfiguration10+

toolbarConfiguration(value: Array<ToolbarItem> | CustomBuilder, options?: NavigationToolbarOptions)

设置工具栏内容。不设置时不显示工具栏。

从API version 20开始，该接口支持在[attributeModifier](动态属性设置.md#ZH-CN_TOPIC_0000002529284843__attributemodifier)中调用。

不支持通过SymbolGlyphModifier对象的fontSize属性修改图标大小、effectStrategy属性修改动效、symbolEffect属性修改动效类型。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明valueArray<[ToolbarItem](#ZH-CN_TOPIC_0000002497444902__toolbaritem10)> | [CustomBuilder](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__custombuilder8)是

工具栏内容，使用Array<[ToolbarItem](#ZH-CN_TOPIC_0000002497444902__toolbaritem10)>设置的工具栏有如下特性：

工具栏所有选项均分底部工具栏，在每个均分内容区布局文本和图标。

竖屏最多支持显示5个图标，多余的图标会被放入自动生成的更多图标。横屏时，如果为[Split](#ZH-CN_TOPIC_0000002497444902__navigationmode9枚举说明)模式，仍按照竖屏规则显示，如果为[Stack](#ZH-CN_TOPIC_0000002497444902__navigationmode9枚举说明)模式需配合menus属性的Array<[NavigationMenuItem](#ZH-CN_TOPIC_0000002497444902__navigationmenuitem)>使用，底部工具栏会自动隐藏，同时底部工具栏所有选项移动至页面右上角菜单。

使用[CustomBuilder](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__custombuilder8)写法为用户自定义工具栏选项，除均分底部工具栏外不具备以上功能。

options11+[NavigationToolbarOptions](#ZH-CN_TOPIC_0000002497444902__navigationtoolbaroptions11)否工具栏选项。 包含工具栏背景颜色、工具栏背景模糊样式及模糊选项、工具栏背景属性、工具栏布局方式、是否隐藏工具栏的文本、工具栏更多图标的菜单选项。

#### hideToolBar

hideToolBar(value: boolean)

设置是否隐藏工具栏。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明valueboolean是

是否隐藏工具栏。

true：隐藏工具栏；false：显示工具栏。

传入参数非法时，按false处理。

#### hideToolBar13+

hideToolBar(hide: boolean, animated: boolean)

设置是否隐藏工具栏。与[hideToolBar](#ZH-CN_TOPIC_0000002497444902__hidetoolbar)相比，新增工具栏显隐时是否使用动画。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明hideboolean是

是否隐藏工具栏。

true：隐藏工具栏；false：显示工具栏。

传入参数非法时，按false处理。

animatedboolean是

设置是否使用动画显隐工具栏。

true：使用动画显示隐藏工具栏；false：不使用动画显示隐藏工具栏。

传入参数非法时，按false处理。

#### hideTitleBar

hideTitleBar(value: boolean)

设置是否隐藏标题栏。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明valueboolean是

是否隐藏标题栏。

true：隐藏标题栏；false：显示标题栏。

传入参数非法时，按false处理。

#### hideTitleBar13+

hideTitleBar(hide: boolean, animated: boolean)

设置是否隐藏标题栏。与[hideTitleBar](#ZH-CN_TOPIC_0000002497444902__hidetitlebar)相比，新增标题栏显隐时是否使用动画。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明hideboolean是

是否隐藏标题栏。

true：隐藏标题栏；false：显示标题栏。

传入参数非法时，按false处理。

animatedboolean是

设置是否使用动画显隐标题栏。

true：使用动画显示隐藏标题栏；false：不使用动画显示隐藏标题栏。

传入参数非法时，按false处理。

#### hideBackButton

hideBackButton(value: boolean)

设置是否隐藏标题栏中的返回键。返回键仅在[titleMode](#ZH-CN_TOPIC_0000002497444902__titlemode)设置为NavigationTitleMode.Mini时才生效。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明valueboolean是

是否隐藏标题栏中的返回键。

true：隐藏返回键。

false：显示返回键。

传入参数非法时，按false处理。

#### navBarWidth9+

navBarWidth(value: Length)

设置导航页宽度。仅在[mode](#ZH-CN_TOPIC_0000002497444902__mode9)设置为NavigationMode.Auto或NavigationMode.Split时生效。

从API version 18开始，该参数支持[!!](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-binding)双向绑定变量。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明value[Length](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__length)是

导航页宽度。

默认值：240

单位：vp

undefined：行为不做处理，导航页宽度与默认值保持一致。

#### navBarPosition9+

navBarPosition(value: NavBarPosition)

设置导航页位置。仅在[mode](#ZH-CN_TOPIC_0000002497444902__mode9)设置为NavigationMode.Auto或NavigationMode.Split时生效。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明value[NavBarPosition](#ZH-CN_TOPIC_0000002497444902__navbarposition9枚举说明)是

导航页位置。

默认值：NavBarPosition.Start

#### mode9+

mode(value: NavigationMode)

设置导航页的显示模式，支持单栏（Stack）、分栏（Split）和自适应（Auto）。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明value[NavigationMode](#ZH-CN_TOPIC_0000002497444902__navigationmode9枚举说明)是

导航页的显示模式。

默认值：NavigationMode.Auto

自适应：基于组件宽度自适应单栏和双栏。

#### backButtonIcon9+

backButtonIcon(value: string | PixelMap | Resource | SymbolGlyphModifier)

设置标题栏中返回键图标。

不支持通过SymbolGlyphModifier对象的fontSize属性修改图标大小、effectStrategy属性修改动效、symbolEffect属性修改动效类型。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明valuestring | [PixelMap](../../types/interfaces/Interface (PixelMap).md) | [Resource](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resource) | [SymbolGlyphModifier12+](动态SymbolGlyphModifier属性设置.md#ZH-CN_TOPIC_0000002529444819__symbolglyphmodifier)是标题栏中返回键图标。

#### backButtonIcon19+

backButtonIcon(icon: string | PixelMap | Resource | SymbolGlyphModifier, accessibilityText?: ResourceStr)

设置标题栏中返回键图标和无障碍播报内容。

该接口不支持在[attributeModifier](动态属性设置.md#ZH-CN_TOPIC_0000002529284843__attributemodifier)中调用。

不支持通过SymbolGlyphModifier对象的fontSize属性修改图标大小、effectStrategy属性修改动效、symbolEffect属性修改动效类型。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明iconstring | [PixelMap](../../types/interfaces/Interface (PixelMap).md) | [Resource](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resource) | [SymbolGlyphModifier](动态SymbolGlyphModifier属性设置.md#ZH-CN_TOPIC_0000002529444819__symbolglyphmodifier)是标题栏中返回键图标。accessibilityText[ResourceStr](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcestr)否

返回键无障碍播报内容。

默认值：系统语言是中文时为“返回”，系统语言是英文时为“back”。

#### hideNavBar9+

hideNavBar(value: boolean)

设置是否隐藏导航页。设置为true时，隐藏Navigation的导航页，包括标题栏、内容区和工具栏。如果此时路由栈中存在NavDestination页面，则直接显示栈顶NavDestination页面，反之显示空白。

从API version 9开始到API version 10仅在双栏模式下生效。从API version 11开始在单栏、双栏与自适应模式均生效。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明valueboolean是

是否隐藏导航页。

true：隐藏导航页；false：显示导航页。

传入参数非法时，按false处理。

#### navDestination10+

navDestination(builder: (name: string, param: unknown) => void)

创建NavDestination组件。使用builder函数，基于name和param构造NavDestination组件。builder下只能有一个根节点。builder中允许在NavDestination组件外包含一层自定义组件， 但自定义组件不允许设置属性和事件，否则仅显示空白。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明builder(name: string, param: unknown) => void是创建NavDestination组件。name：NavDestination页面名称。param：开发者设置的NavDestination页面详细参数，unknown可以是用户自定义的类型。

#### navBarWidthRange10+

navBarWidthRange(value: [Dimension, Dimension])

设置导航页最小和最大宽度（双栏模式下生效）。

**规则：** 优先级规则详见[minContentWidth](#ZH-CN_TOPIC_0000002497444902__mincontentwidth10)说明。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明value[[Dimension](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__dimension10), [Dimension](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__dimension10)]是

导航页最小和最大宽度。

默认值：最小默认值 240，最大默认值为组件宽度的40% ，且不大于 432，未正确设置的值按照默认值计算。

单位：vp

#### minContentWidth10+

minContentWidth(value: Dimension)

设置导航页内容区最小宽度（双栏模式下生效）。

优先级规则：

1.

仅设置navBarWidth，不支持Navigation分割线拖拽。

1.

navBarWidthRange指定分割线可以拖拽范围。如果不设置值，则按照默认值处理。拖拽范围需要满足navBarWidthRange设置的范围和minContentWidth限制。

1.

Navigation显示范围缩小：a. 缩小内容区大小。如果不设置minContentWidth属性，则可以缩小内容区至0， 否则最小缩小至minContentWidth。b. 缩小导航页大小，缩小时需要满足导航页宽度大于navBarRange的下限。c. 对显示内容进行裁切。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明value[Dimension](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__dimension10)是

导航页内容区最小宽度。

默认值：360

单位：vp

undefined：行为不做处理，导航页内容区最小宽度与默认值保持一致。

Auto模式断点计算：默认600vp，minNavBarWidth(240vp) + minContentWidth (360vp)

#### ignoreLayoutSafeArea12+

ignoreLayoutSafeArea(types?: Array<LayoutSafeAreaType>, edges?: Array<LayoutSafeAreaEdge>)

控制组件的布局，使其扩展到非安全区域。

组件设置ignoreLayoutSafeArea之后生效的条件为：

设置LayoutSafeAreaType.SYSTEM时，组件的边界与非安全区域重合时组件能够延伸到非安全区域下。例如：设备顶部状态栏高度100，组件在屏幕中纵向方位的绝对偏移需要在0到100之间。

若组件延伸到非安全区域内，此时在非安全区域里触发的事件（例如：点击事件）等可能会被系统拦截，优先响应状态栏等系统组件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明typesArray <[LayoutSafeAreaType](安全区域.md#ZH-CN_TOPIC_0000002497444852__layoutsafeareatype12)>否

配置扩展安全区域的类型。

默认值：

[LayoutSafeAreaType.SYSTEM]

edgesArray <[LayoutSafeAreaEdge](安全区域.md#ZH-CN_TOPIC_0000002497444852__layoutsafeareaedge12)>否

配置扩展安全区域的方向。

默认值：

[LayoutSafeAreaEdge.TOP, LayoutSafeAreaEdge.BOTTOM]。

#### systemBarStyle12+

systemBarStyle(style: Optional<SystemBarStyle>)

当Navigation中显示Navigation首页时，设置对应系统状态栏的样式。

1. 不建议混合使用systemBarStyle属性和window设置状态栏样式的相关接口，例如：[setWindowSystemBarProperties](../../types/interfaces/Interface (Window).md#ZH-CN_TOPIC_0000002497604802__setwindowsystembarproperties9)。
1. 初次设置Navigation/NavDestination的systemBarStyle属性时，会备份当前状态栏样式用于后续的恢复场景。
1. Navigation总是以首页（路由栈内没有NavDestination时）或者栈顶NavDestination设置的状态栏样式为准。
1. Navigation首页或者任何栈顶NavDestination页面，如果设置了有效的systemBarStyle，则会使用设置的样式，反之如果之前已经备份了样式，则使用备份的样式，否则不做任何处理。
1. [Split](#ZH-CN_TOPIC_0000002497444902__navigationmode9枚举说明)模式下的Navigation，如果内容区没有NavDestination，则遵从Navigation首页的设置，反之则遵从栈顶NavDestination的设置。
1. 仅支持在主窗口的主页面中使用systemBarStyle设置状态栏样式。
1. 仅当Navigation占满整个页面时，设置的样式才会生效，当Navigation没有占满整个页面时，如果有备份的样式，则恢复备份的样式。
1. 当页面设置不同样式时，在页面转场开始时生效。
1. 非全屏窗口下，Navigation/NavDestination设置的状态栏不生效。

从API version 20开始，该接口支持在[attributeModifier](动态属性设置.md#ZH-CN_TOPIC_0000002529284843__attributemodifier)中调用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明style[Optional](自定义属性设置.md#ZH-CN_TOPIC_0000002529284845__optionalt12)<[SystemBarStyle](../../types/interfaces/Interfaces (其他).md#ZH-CN_TOPIC_0000002529284795__systembarstyle12)>是系统状态栏样式。

#### recoverable14+

recoverable(recoverable: Optional<boolean>)

配置Navigation是否可恢复。如配置为可恢复，当应用进程异常退出并重新冷启动时，可自动创建该Navigation，并恢复至异常退出时的路由栈。

1. 使用该接口需要先设置Navigation的[id属性](组件标识.md#ZH-CN_TOPIC_0000002497604824__id)，否则该接口无效。
1. 该接口需要配合NavDestination的[recoverable](NavDestination.md#ZH-CN_TOPIC_0000002529284873__recoverable14)接口使用。
1. 恢复的过程中不可序列化的信息，例如不可序列化的参数与用户设置的onPop等，会被丢弃，无法恢复。
1. 当应用退到后台，因系统资源不足等原因被系统终止后，如果某页面已配置为可恢复，当应用再次被唤醒至前台时，系统将自动恢复该页面。详细说明请参考[UIAbility备份恢复](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ability-recover-guideline)，详细使用请参考[示例18](#ZH-CN_TOPIC_0000002497444902__示例18设置navigation可恢复)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明recoverable[Optional](自定义属性设置.md#ZH-CN_TOPIC_0000002529284845__optionalt12)<boolean>是

Navigation是否可恢复，默认为不可恢复。

true：路由栈可恢复；false：路由栈不可恢复。

传入参数非法时，按false处理。

#### enableDragBar14+

enableDragBar(isEnabled: Optional<boolean>)

控制分栏场景下是否显示拖拽条。该属性在PC/2in1设备上不生效。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明isEnabled[Optional](自定义属性设置.md#ZH-CN_TOPIC_0000002529284845__optionalt12)<boolean>是

是否开启拖拽条，默认为无拖拽条样式。

true：有拖拽条样式；false：无拖拽条样式。

传入参数非法时，按false处理。

#### enableModeChangeAnimation15+

enableModeChangeAnimation(isEnabled: Optional<boolean>)

控制是否开启单双栏切换时的动效。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明isEnabled[Optional](自定义属性设置.md#ZH-CN_TOPIC_0000002529284845__optionalt12)<boolean>是

是否开启单双栏切换动效。

true：开启单双栏切换动效；false：关闭单双栏切换动效。

传入参数非法时，按true处理。

#### enableToolBarAdaptation19+

enableToolBarAdaptation(enable: Optional<boolean>)

设置是否启用Navigation和NavDestination的工具栏[toolbarConfiguration](#ZH-CN_TOPIC_0000002497444902__toolbarconfiguration10)自适应能力。关闭此能力后，底部工具栏[toolbarConfiguration](#ZH-CN_TOPIC_0000002497444902__toolbarconfiguration10)将不会再移动至页面右上角的菜单中。该接口不适配于自定义菜单，使用该接口需采用[NavigationMenuItem](#ZH-CN_TOPIC_0000002497444902__navigationmenuitem)接口来定义[菜单](#ZH-CN_TOPIC_0000002497444902__menus)。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明enableOptional<boolean>是

是否启用Navigation和NavDestination的工具栏自适应能力。

默认值：true

true：启用Navigation和NavDestination的工具栏自适应能力。

false：不启用Navigation和NavDestination的工具栏自适应能力。

#### splitPlaceholder20+

splitPlaceholder(placeholder: ComponentContent)

Navigation双栏模式下，支持设置右侧页面显示默认占位页，占位页仅作为UI展示页，不可获焦和响应事件。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明placeholder[ComponentContent](../components/ComponentContent.md#ZH-CN_TOPIC_0000002497444816__componentcontent-1)是设置Navigation双栏模式下右侧的默认占位页。

#### enableVisibilityLifecycleWithContentCover21+

enableVisibilityLifecycleWithContentCover(isEnabled: Optional<boolean>)

设置是否启用[NavDestination](NavDestination.md)页面[onHidden](NavDestination.md#ZH-CN_TOPIC_0000002529284873__onhidden10)、[onShown](NavDestination.md#ZH-CN_TOPIC_0000002529284873__onshown10)生命周期与全模态的联动触发。

**元服务API：** 从API version 21开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明isEnabledOptional<boolean>是

是否启用NavDestination页面onShown、onHidden生命周期与全模态的联动触发。

默认值：true

true：全模态拉起时，会触发当前NavDestination页面的onHidden生命周期；全模态关闭时会触发当前NavDestination页面的onShown生命周期

false：NavDestination页面onHidden、onShown生命周期不会因为全模态的拉起、关闭而触发。

#### subTitle(deprecated)

subTitle(value: string)

设置页面副标题。

从API version 8开始支持，从API version 9开始废弃，建议使用[title](#ZH-CN_TOPIC_0000002497444902__title)替代。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明valuestring是页面副标题。

#### toolBar(deprecated)

toolBar(value: object | CustomBuilder)

设置工具栏内容。不设置时不显示工具栏。items均分底部工具栏，在每个均分内容区布局文本和图标，文本超长时，逐级缩小，缩小之后换行，最后截断。

从API version 8开始支持，从API version 10开始废弃，建议使用[toolbarConfiguration](#ZH-CN_TOPIC_0000002497444902__toolbarconfiguration10)替代。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明valueobject | [CustomBuilder](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__custombuilder8)是工具栏内容。

**object类型说明：**

名称类型必填说明valuestring是工具栏单个选项的显示文本。iconstring否工具栏单个选项的图标资源路径。action() => void否当前选项被选中的事件回调。

#### 事件

#### onTitleModeChange

onTitleModeChange(callback: (titleMode: NavigationTitleMode) => void)

当[titleMode](#ZH-CN_TOPIC_0000002497444902__titlemode)为NavigationTitleMode.Free时，随着可滚动组件的滑动标题栏模式发生变化时触发此回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明titleMode[NavigationTitleMode](#ZH-CN_TOPIC_0000002497444902__navigationtitlemode枚举说明)是标题模式。

#### onNavBarStateChange9+

onNavBarStateChange(callback: (isVisible: boolean) => void)

导航页显示状态切换时触发该回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明isVisibleboolean是isVisible为true时表示显示，为false时表示隐藏。

#### onNavigationModeChange11+

onNavigationModeChange(callback: (mode: NavigationMode) => void)

当Navigation首次显示或者单双栏状态发生变化时触发该回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明mode[NavigationMode](#ZH-CN_TOPIC_0000002497444902__navigationmode9枚举说明)是

NavigationMode.Split：当前Navigation显示为双栏;

NavigationMode.Stack：当前Navigation显示为单栏。

#### customNavContentTransition11+

customNavContentTransition(delegate:(from: NavContentInfo, to: NavContentInfo, operation: NavigationOperation) => NavigationAnimatedTransition | undefined)

自定义转场动画回调。

从API version 20开始，该接口支持在[attributeModifier](动态属性设置.md#ZH-CN_TOPIC_0000002529284843__attributemodifier)中调用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明from[NavContentInfo](#ZH-CN_TOPIC_0000002497444902__navcontentinfo11)是退场Destination的页面。to[NavContentInfo](#ZH-CN_TOPIC_0000002497444902__navcontentinfo11)是进场Destination的页面。operation[NavigationOperation](#ZH-CN_TOPIC_0000002497444902__navigationoperation11枚举说明)是转场类型。

**返回值：**

类型说明[NavigationAnimatedTransition](#ZH-CN_TOPIC_0000002497444902__navigationanimatedtransition11) | undefined

NavigationAnimatedTransition：自定义转场动画协议。

undefined: 返回未定义，执行默认转场动效。

#### NavPathStack10+

Navigation导航控制器，以栈的数据结构管理Navigation中所有的子页面，并提供栈操作的方法用于控制Navigation中子页面的切换。

从API version 12开始，NavPathStack允许被继承，派生类对象可以替代基类NavPathStack对象使用。使用示例参见[示例10](#ZH-CN_TOPIC_0000002497444902__示例10定义导航控制器派生类)。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

1.连续调用多个导航控制器操作方法时，中间过程会被忽略，显示最终的栈操作结果。

例如：在Page1页面先pop再push一个Page1，系统会认为操作前和操作后的结果一致而不进行任何操作，如果需要强行push一个Page1实例，可以使用NEW_INSTANCE模式。

2.不建议开发者通过监听生命周期的方式管理自己的导航控制器。

3.在应用处于后台状态下，调用NavPathStack的栈操作方法，会在应用再次回到前台状态时触发刷新。

#### constructor

constructor()

创建NavPathStack对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

#### pushPath10+

pushPath(info: NavPathInfo, animated?: boolean): void

将info指定的NavDestination页面信息入栈。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明info[NavPathInfo](#ZH-CN_TOPIC_0000002497444902__navpathinfo10)是NavDestination页面的信息。animated11+boolean否

是否支持转场动画。

true：支持转场动画；false：不支持转场动画。

传入参数非法时，按true处理。

#### pushPath12+

pushPath(info: NavPathInfo, options?: NavigationOptions): void

将info指定的NavDestination页面信息入栈，具体根据options中指定不同的[LaunchMode](#ZH-CN_TOPIC_0000002497444902__launchmode12枚举说明)，有不同的行为。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明info[NavPathInfo](#ZH-CN_TOPIC_0000002497444902__navpathinfo10)是NavDestination页面的信息。options[NavigationOptions](#ZH-CN_TOPIC_0000002497444902__navigationoptions12)否路由栈操作选项。

#### pushPathByName10+

pushPathByName(name: string, param: unknown, animated?: boolean): void

将name指定的NavDestination页面信息入栈，传递的数据为param。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明namestring是NavDestination页面名称。paramunknown是开发者设置的NavDestination页面详细参数，unknown可以是用户自定义的类型。animated11+boolean否

是否支持转场动画。

true：支持转场动画；false：不支持转场动画。

默认值：true

#### pushPathByName11+

pushPathByName(name: string, param: Object, onPop: Callback<PopInfo>, animated?: boolean): void

将name指定的NavDestination页面信息入栈，传递的数据为param，添加onPop回调接收入栈页面出栈时的返回结果，并进行处理。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明namestring是NavDestination页面名称。paramObject是开发者设置的NavDestination页面详细参数。onPopCallback<[PopInfo](#ZH-CN_TOPIC_0000002497444902__popinfo11)>是Callback回调，用于页面出栈时触发该回调处理返回结果。仅[pop](#ZH-CN_TOPIC_0000002497444902__pop11)、[popToName](#ZH-CN_TOPIC_0000002497444902__poptoname11)、[popToIndex](#ZH-CN_TOPIC_0000002497444902__poptoindex11)中设置result参数后触发。animatedboolean否

是否支持转场动画。

true：支持转场动画；false：不支持转场动画。

默认值：true

#### pushDestination11+

pushDestination(info: NavPathInfo, animated?: boolean): Promise<void>

将info指定的NavDestination页面信息入栈，使用Promise异步回调返回接口调用结果。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明info[NavPathInfo](#ZH-CN_TOPIC_0000002497444902__navpathinfo10)是NavDestination页面的信息。animatedboolean否

是否支持转场动画。

true：支持转场动画；false：不支持转场动画。

默认值：true

**返回值：**

类型说明Promise<void>异步返回结果。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)、[页面路由错误码](../../errors/页面路由错误码.md)和[接口调用异常错误码](../../errors/接口调用异常错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed.100001Internal error.100005Builder function not registered.100006NavDestination not found.

- 在[aboutToAppear](自定义组件的生命周期.md#ZH-CN_TOPIC_0000002529444913__abouttoappear)里面不建议使用栈操作。

#### pushDestination12+

pushDestination(info: NavPathInfo, options?: NavigationOptions): Promise<void>

将info指定的NavDestination页面信息入栈，使用Promise异步回调返回接口调用结果，具体根据options中指定不同的[LaunchMode](#ZH-CN_TOPIC_0000002497444902__launchmode12枚举说明)，有不同的行为。

在[aboutToAppear](自定义组件的生命周期.md#ZH-CN_TOPIC_0000002529444913__abouttoappear)里面不建议使用栈操作。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明info[NavPathInfo](#ZH-CN_TOPIC_0000002497444902__navpathinfo10)是NavDestination页面的信息。options[NavigationOptions](#ZH-CN_TOPIC_0000002497444902__navigationoptions12)否路由栈操作选项。

**返回值：**

类型说明Promise<void>异常返回结果。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)、[页面路由错误码](../../errors/页面路由错误码.md)和[接口调用异常错误码](../../errors/接口调用异常错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed.100001Internal error.100005Builder function not registered.100006NavDestination not found.

#### pushDestinationByName11+

pushDestinationByName(name: string, param: Object, animated?: boolean): Promise<void>

将name指定的NavDestination页面信息入栈，传递的数据为param，使用Promise异步回调返回接口调用结果。

在[aboutToAppear](自定义组件的生命周期.md#ZH-CN_TOPIC_0000002529444913__abouttoappear)里面不建议使用栈操作。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明namestring是NavDestination页面名称。paramObject是开发者设置的NavDestination页面详细参数。animatedboolean否

是否支持转场动画。

true：支持转场动画；false：不支持转场动画。

默认值：true

**返回值：**

类型说明Promise<void>异常返回结果。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)、[页面路由错误码](../../errors/页面路由错误码.md)和[接口调用异常错误码](../../errors/接口调用异常错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed.100001Internal error.100005Builder function not registered.100006NavDestination not found.

#### pushDestinationByName11+

pushDestinationByName(name: string, param: Object, onPop: Callback<PopInfo>, animated?: boolean): Promise<void>

将name指定的NavDestination页面信息入栈，传递的数据为param，并且添加用于页面出栈时处理返回结果的onPop回调，使用Promise异步回调返回接口调用结果。

在[aboutToAppear](自定义组件的生命周期.md#ZH-CN_TOPIC_0000002529444913__abouttoappear)里面不建议使用栈操作。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明namestring是NavDestination页面名称。paramObject是开发者设置的NavDestination页面详细参数。onPopCallback<[PopInfo](#ZH-CN_TOPIC_0000002497444902__popinfo11)>是Callback回调，用于页面出栈时处理返回结果。仅[pop](#ZH-CN_TOPIC_0000002497444902__pop11)、[popToName](#ZH-CN_TOPIC_0000002497444902__poptoname11)、[popToIndex](#ZH-CN_TOPIC_0000002497444902__poptoindex11)中设置result参数后触发。animatedboolean否

是否支持转场动画。

true：支持转场动画；false：不支持转场动画。

默认值：true

**返回值：**

类型说明Promise<void>异常返回结果。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)、[页面路由错误码](../../errors/页面路由错误码.md)和[接口调用异常错误码](../../errors/接口调用异常错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed.100001Internal error.100005Builder function not registered.100006NavDestination not found.

#### replacePath11+

replacePath(info: NavPathInfo, animated?: boolean): void

将当前路由栈栈顶退出，将info指定的NavDestination页面信息入栈。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明info[NavPathInfo](#ZH-CN_TOPIC_0000002497444902__navpathinfo10)是新栈顶页面参数信息。animatedboolean否

是否支持转场动画。

true：支持转场动画；false：不支持转场动画。

默认值：true

#### replacePath12+

replacePath(info: NavPathInfo, options?: NavigationOptions): void

替换路由栈操作，具体根据options中指定不同的[LaunchMode](#ZH-CN_TOPIC_0000002497444902__launchmode12枚举说明)，有不同的行为。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明info[NavPathInfo](#ZH-CN_TOPIC_0000002497444902__navpathinfo10)是新栈顶页面参数信息。options[NavigationOptions](#ZH-CN_TOPIC_0000002497444902__navigationoptions12)否路由栈操作选项。

#### replacePathByName11+

replacePathByName(name: string, param: Object, animated?: boolean): void

将当前路由栈栈顶退出，将name指定的页面入栈。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明namestring是NavDestination页面名称。paramObject是开发者设置的NavDestination页面详细参数。animated11+boolean否

是否支持转场动画。

true：支持转场动画；false：不支持转场动画。

默认值：true

#### replaceDestination18+

replaceDestination(info: NavPathInfo, options?: NavigationOptions): Promise<void>

替换路由栈操作。使用Promise异步回调返回接口调用结果，具体根据options中指定不同的[LaunchMode](#ZH-CN_TOPIC_0000002497444902__launchmode12枚举说明)，有不同的行为。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明info[NavPathInfo](#ZH-CN_TOPIC_0000002497444902__navpathinfo10)是NavDestination页面的信息。options[NavigationOptions](#ZH-CN_TOPIC_0000002497444902__navigationoptions12)否路由栈操作选项。

**返回值：**

类型说明Promise<void>异常返回结果。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)、[页面路由错误码](../../errors/页面路由错误码.md)和[接口调用异常错误码](../../errors/接口调用异常错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed.100001Internal error.100005Builder function not registered.100006NavDestination not found.

#### removeByIndexes11+

removeByIndexes(indexes: Array<number>): number

将路由栈内索引值在indexes中的NavDestination页面删除。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明indexesArray<number>是待删除NavDestination页面的索引值数组。索引值从0开始。

**返回值：**

类型说明number返回删除的NavDestination页面数量。

#### removeByName11+

removeByName(name: string): number

将路由栈内指定name的NavDestination页面删除。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明namestring是删除的NavDestination页面的名字。

**返回值：**

类型说明number返回删除的NavDestination页面数量。

#### removeByNavDestinationId12+

removeByNavDestinationId(navDestinationId: string): boolean

将路由栈内指定navDestinationId的NavDestination页面删除。navDestinationId可以在NavDestination的[onReady](NavDestination.md#ZH-CN_TOPIC_0000002529284873__onready11)回调中获取，也可以在[NavDestinationInfo](../../modules/ohos/@ohos.arkui.observer (无感监听).md#ZH-CN_TOPIC_0000002529444737__navdestinationinfo)中获取。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明navDestinationIdstring是删除的NavDestination页面的唯一标识符navDestinationId。

**返回值：**

类型说明boolean

返回是否成功删除该页面，

true：删除成功。

false：删除失败。

#### pop10+

pop(animated?: boolean): NavPathInfo | undefined

弹出路由栈栈顶元素。

连续调用多个导航控制器方法时，中间被pop的页面会被缓存，后续push同名页面时会优先复用该页面，不会走新的页面创建流程。

例如：

pathStack: NavPathStack = new NavPathStack()

// 初始页面栈为：[A]

pathStack.pop()

pathStack.pushPath(A)

pathStack.pushPath(B)

// 操作后页面栈为：[A B]

此时A页面会被复用，不会走新的创建流程。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明animated11+boolean否

是否支持转场动画。

true：支持转场动画；false：不支持转场动画。

默认值：true

**返回值：**

类型说明[NavPathInfo](#ZH-CN_TOPIC_0000002497444902__navpathinfo10) | undefined

NavPathInfo：返回栈顶NavDestination页面的信息。

undefined: 当路由栈为空时返回undefined。

#### pop11+

pop(result: Object, animated?: boolean): NavPathInfo | undefined

弹出路由栈栈顶元素，并触发onPop回调传入页面处理结果。

连续调用多个导航控制器方法时，中间被pop的页面会被缓存，后续push同名页面时会优先复用该页面，不会走新的页面创建流程。

例如：

pathStack: NavPathStack = new NavPathStack()

// 初始页面栈为：[A]

pathStack.pop()

pathStack.pushPath(A)

pathStack.pushPath(B)

// 操作后页面栈为：[A B]

此时A页面会被复用，不会走新的创建流程。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明resultObject是页面自定义处理结果。不支持boolean类型。animatedboolean否

是否支持转场动画。

true：支持转场动画；false：不支持转场动画。

默认值：true

**返回值：**

类型说明[NavPathInfo](#ZH-CN_TOPIC_0000002497444902__navpathinfo10) | undefined

NavPathInfo：返回栈顶NavDestination页面的信息。

undefined: 当路由栈为空时返回undefined。

#### popToName10+

popToName(name: string, animated?: boolean): number

回退路由栈到由栈底开始第一个名为name的NavDestination页面。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明namestring是NavDestination页面名称。animated11+boolean否

是否支持转场动画。

true：支持转场动画；false：不支持转场动画。

默认值：true

**返回值：**

类型说明number如果栈中存在名为name的NavDestination页面，则返回由栈底开始第一个名为name的NavDestination页面的索引，否则返回-1。

#### popToName11+

popToName(name: string, result: Object, animated?: boolean): number

回退路由栈到由栈底开始第一个名为name的NavDestination页面，并触发onPop回调传入页面处理结果。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明namestring是NavDestination页面名称。resultObject是页面自定义处理结果。不支持boolean类型。animatedboolean否

是否支持转场动画。

true：支持转场动画；false：不支持转场动画。

默认值：true

**返回值：**

类型说明number如果栈中存在名为name的NavDestination页面，则返回由栈底开始第一个名为name的NavDestination页面的索引，否则返回-1。

#### popToIndex10+

popToIndex(index: number, animated?: boolean): void

回退路由栈到index指定的NavDestination页面。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明indexnumber是NavDestination页面的位置索引。索引值从0开始。animated11+boolean否

是否支持转场动画。

true：支持转场动画；false：不支持转场动画。

默认值：true

#### popToIndex11+

popToIndex(index: number, result: Object, animated?: boolean): void

回退路由栈到index指定的NavDestination页面，并触发onPop回调传入页面处理结果。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明indexnumber是NavDestination页面的位置索引。索引值从0开始。resultObject是页面自定义处理结果。不支持boolean类型。animatedboolean否

是否支持转场动画。

true：支持转场动画；false：不支持转场动画。

默认值：true

#### moveToTop10+

moveToTop(name: string, animated?: boolean): number

将由栈底开始第一个名为name的NavDestination页面移到栈顶。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明namestring是NavDestination页面名称。animated11+boolean否

是否支持转场动画。

true：支持转场动画；false：不支持转场动画。

默认值：true

**返回值：**

类型说明number如果栈中存在名为name的NavDestination页面，则返回由栈底开始第一个名为name的NavDestination页面的当前索引，否则返回-1。

#### moveIndexToTop10+

moveIndexToTop(index: number, animated?: boolean): void

将index指定的NavDestination页面移到栈顶。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明indexnumber是NavDestination页面的位置索引。索引值从0开始。animated11+boolean否

是否支持转场动画。

true：支持转场动画；false：不支持转场动画。

默认值：true

#### clear10+

clear(animated?: boolean): void

清除栈中所有页面。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明animated11+boolean否

是否支持转场动画。

true：支持转场动画；false：不支持转场动画。

默认值：true

#### getAllPathName10+

getAllPathName(): Array<string>

获取栈中所有NavDestination页面的名称。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

类型说明Array<string>返回栈中所有NavDestination页面的名称。

#### getParamByIndex10+

getParamByIndex(index: number): unknown | undefined

获取index指定的NavDestination页面的参数信息。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明indexnumber是NavDestination页面的位置索引。 索引值从0开始。

**返回值：**

类型说明unknown | undefined

unknown：返回对应NavDestination页面的参数信息，unknown可以是用户自定义的类型。

undefined: 传入index无效时返回undefined。

#### getParamByName10+

getParamByName(name: string): Array<unknown>

获取所有名为name的NavDestination页面的参数信息，按页面索引从小到大排序。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明namestring是NavDestination页面名称。

**返回值：**

类型说明Array<unknown>返回全部名为name的NavDestination页面的参数信息，unknown可以是用户自定义的类型。

#### getIndexByName10+

getIndexByName(name: string): Array<number>

获取全部名为name的NavDestination页面的位置索引。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明namestring是NavDestination页面名称。

**返回值：**

类型说明Array<number>返回全部名为name的NavDestination页面的位置索引。 当路由栈中不存在此name，返回空数组。索引取值范围为[0, 路由栈大小-1]

#### size10+

size(): number

获取栈大小。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

类型说明number

返回栈大小。

取值范围：[0, +∞)

#### disableAnimation11+

disableAnimation(value: boolean): void

关闭（true）或打开（false）当前Navigation中所有转场动画。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明valueboolean是

是否关闭转场动画，

默认值：false

true：关闭转场动画。

false：不关闭转场动画。

#### getParent11+

getParent(): NavPathStack | null

获取父NavPathStack。

当出现Navigation嵌套Navigation的情况时（可以是直接嵌套，也可以是间接嵌套），内部Navigation的NavPathStack能够获取到外层Navigation的NavPathStack。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

类型说明[NavPathStack](#ZH-CN_TOPIC_0000002497444902__navpathstack10) | null如果当前NavPathStack所属Navigation的外层有另外的一层Navigation，则能够获取到外层Navigation的NavPathStack。否则获取不到NavPathStack，返回null。

#### setInterception12+

setInterception(interception: NavigationInterception): void

设置Navigation页面跳转拦截回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明interception[NavigationInterception](#ZH-CN_TOPIC_0000002497444902__navigationinterception12)是设置Navigation跳转拦截对象。

#### getPathStack19+

getPathStack(): Array<NavPathInfo>

获取当前路由栈中的路由页面信息数组。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

类型说明Array<[NavPathInfo](#ZH-CN_TOPIC_0000002497444902__navpathinfo10)>当前路由栈中的路由页面信息数组。

#### setPathStack19+

setPathStack(pathStack: Array<NavPathInfo>, animated?: boolean): void

将当前路由栈中的路由页面信息数组更新为指定内容，并实现路由转场。

1. 开发者可以在原有栈的基础上批量添加或删除页面。批量入栈的页面中，只有可见的页面会触发创建，其他页面虽已入栈但不会立即创建，当这些页面变为可见时，才会触发创建。
1. 通过批量入栈功能更新的路由栈，各页面的生命周期事件触发顺序为从栈顶到底部依次触发，这与其它入栈接口从栈底到顶部的触发顺序不同。
1. 开发者可以通过[NavPathInfo](#ZH-CN_TOPIC_0000002497444902__navpathinfo10)中的页面唯一标识符navDestinationId来操作已有页面，该id由系统默认生成且全局唯一（可以通过[getPathStack](#ZH-CN_TOPIC_0000002497444902__getpathstack19)接口获取，不可主动赋新值）。若该id在当前路由栈中不存在，则表示新增页面，若在当前路由栈中存在，同时对应的name相同，则表示复用已有页面。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明pathStackArray<[NavPathInfo](#ZH-CN_TOPIC_0000002497444902__navpathinfo10)>是

设置当前路由栈中的路由页面信息数组。

**说明：**

数组长度无限制。

animatedboolean否

是否开启转场动画。

true：开启转场动画；false：不开启转场动画。

默认值：true

#### NavPathInfo10+

路由页面信息。

#### constructor

constructor(name: string, param: unknown, onPop?: Callback<PopInfo>, isEntry?: boolean)

创建NavPathInfo对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明namestring是

NavDestination页面名称。该名称匹配开发者设置的路由表中的name，包括以下两种：

1. 自定义路由表，开发者通过[navDestination](#ZH-CN_TOPIC_0000002497444902__navdestination10)方法传递。

2. 系统路由表，通过routerMap中的name设置，可参考[示例2](#ZH-CN_TOPIC_0000002497444902__示例2使用导航控制器方法)。

paramunknown是开发者设置的NavDestination页面详细参数，unknown可以是用户自定义的类型。onPop11+Callback<[PopInfo](#ZH-CN_TOPIC_0000002497444902__popinfo11)>否NavDestination页面触发[pop](#ZH-CN_TOPIC_0000002497444902__pop11)、[popToName](#ZH-CN_TOPIC_0000002497444902__poptoname11)、[popToIndex](#ZH-CN_TOPIC_0000002497444902__poptoindex11)时返回的回调。仅[pop](#ZH-CN_TOPIC_0000002497444902__pop11)、[popToName](#ZH-CN_TOPIC_0000002497444902__poptoname11)、[popToIndex](#ZH-CN_TOPIC_0000002497444902__poptoindex11)中设置result参数后触发。isEntry12+boolean否

标记NavDestination是否为入口页面。

true：NavDestination是入口页面；false：NavDestination不是入口页面。

默认值：false

标记清理时机：1. 在当前navDestination页面触发一次全局返回事件。2. 应用退至后台。

**说明：**

入口NavDestination不响应应用内的全局back事件，直接触发应用间的全局back事件。

#### 属性

NavPathInfo参数信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明namestring否否

NavDestination页面名称。该名称匹配开发者设置的路由表中的name，包括以下两种：

1. 自定义路由表，开发者通过[navDestination](#ZH-CN_TOPIC_0000002497444902__navdestination10)方法传递。

2. 系统路由表，通过routerMap中的name设置，可参考[示例2](#ZH-CN_TOPIC_0000002497444902__示例2使用导航控制器方法)。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

paramunknown否是

开发者设置的NavDestination页面详细参数，unknown可以是用户自定义的类型。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

onPop11+Callback<[PopInfo](#ZH-CN_TOPIC_0000002497444902__popinfo11)>否是

NavDestination页面触发[pop](#ZH-CN_TOPIC_0000002497444902__pop11)、[popToName](#ZH-CN_TOPIC_0000002497444902__poptoname11)、[popToIndex](#ZH-CN_TOPIC_0000002497444902__poptoindex11)时返回的回调。仅[pop](#ZH-CN_TOPIC_0000002497444902__pop11)、[popToName](#ZH-CN_TOPIC_0000002497444902__poptoname11)、[popToIndex](#ZH-CN_TOPIC_0000002497444902__poptoindex11)中设置result参数后触发。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

isEntry12+boolean否是

标记NavDestination是否为入口页面。

true：NavDestination是入口页面；false：NavDestination不是入口页面。

默认值：false

标记清理时机：1. 在当前navDestination页面触发一次全局back事件。2. 应用退至后台。

**说明：**

入口NavDestination不响应应用内的全局back事件，直接触发应用间的全局back事件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

navDestinationId19+string否是

NavDestination页面唯一标识符，该id由系统默认生成且全局唯一，通过[getPathStack](#ZH-CN_TOPIC_0000002497444902__getpathstack19)接口可读取，但不可以主动赋新值。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

#### PopInfo11+

下一个页面返回的回调信息载体。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明info[NavPathInfo](#ZH-CN_TOPIC_0000002497444902__navpathinfo10)否否页面触发返回时的当前页面信息，系统自动获取填入，无需开发者传入。resultObject否否页面触发返回时的结果，开发者自定义对象。

#### NavContentInfo11+

跳转Destination信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明namestring否是NavDestination名称，如果为根视图(NavBar)，则返回值为undefined。indexnumber否否

NavDestination在NavPathStack中的序号， 如果为根视图(NavBar)，则返回值为 -1。

取值范围：[-1, +∞)。

mode[NavDestinationMode](NavDestination.md#ZH-CN_TOPIC_0000002529284873__navdestinationmode枚举说明11)否是NavDestination的模式，如果是根视图(NavBar)，则返回值为undefined。param12+Object否是NavDestination页面加载的参数。navDestinationId12+string否是NavDestination的唯一标识符。

#### NavigationAnimatedTransition11+

自定义转场动画协议，开发者需实现该协议来定义Navigation路由跳转的跳转动画。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明timeoutnumber否是

动画超时结束时间。

单位：ms。

取值范围：[0, +∞)。

默认值：可交互动画无默认值，不可交互动画默认超时时间为1000ms。

transition(transitionProxy:[NavigationTransitionProxy](#ZH-CN_TOPIC_0000002497444902__navigationtransitionproxy-11)) => void否否

自定义转场动画执行回调。

transitionProxy：自定义转场动画代理对象。

onTransitionEnd(success:boolean) => void否是

转场完成回调。

success：转场是否成功。

isInteractive12+boolean否是

本次转场动画是否为可交互转场。

true：本次转场动画是可交互转场；false：本次转场动画不是可交互转场。

默认值：false

#### NavigationTransitionProxy 11+

自定义转场动画代理对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

#### 属性

NavigationTransitionProxy参数信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明from[NavContentInfo](#ZH-CN_TOPIC_0000002497444902__navcontentinfo11)否否退场页面信息。to[NavContentInfo](#ZH-CN_TOPIC_0000002497444902__navcontentinfo11)否否进场页面信息。isInteractive12+boolean否是

是否为可交互转场动画。

默认值：false

true：本次转场动画是可交互转场。

false：本次转场动画不是可交互转场。

#### finishTransition

finishTransition(): void;

结束本次自定义转场动画，开发者需要主动触发该方法来结束本次转场，否则系统会在timeout的时间后结束本次转场。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

#### cancelTransition12+

cancelTransition?(): void;

取消本次交互转场，恢复到页面跳转前的路由栈(不支持取消不可交互转场动画)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

#### updateTransition12+

updateTransition?(progress: number): void;

更新交互转场动画进度(不可交互动画不支持动画进度设置)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明progressnumber是设置交互转场动画进度百分比。取值范围：[0, 1]

#### NavigationInterception12+

Navigation跳转拦截对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明willShow[InterceptionShowCallback](#ZH-CN_TOPIC_0000002497444902__interceptionshowcallback12)否是

页面跳转前的回调，允许操作栈，在当前跳转中生效。拦截的页面会被创建。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

didShow[InterceptionShowCallback](#ZH-CN_TOPIC_0000002497444902__interceptionshowcallback12)否是

页面跳转后回调。在该回调中操作栈在下一次跳转中刷新。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

modeChange[InterceptionModeCallback](#ZH-CN_TOPIC_0000002497444902__interceptionmodecallback12)否是

Navigation单双栏显示状态发生变更时触发该回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

interception22+[InterceptionCallback](#ZH-CN_TOPIC_0000002497444902__interceptioncallback22)否是

页面跳转前的回调，允许操作栈，在当前跳转中生效。拦截的页面不会被创建。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

#### InterceptionShowCallback12+

type InterceptionShowCallback = (from: NavDestinationContext | NavBar, to: NavDestinationContext | NavBar, operation: NavigationOperation, isAnimated: boolean) => void

Navigation页面跳转前和页面跳转后的拦截回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明from[NavDestinationContext](NavDestination.md#ZH-CN_TOPIC_0000002529284873__navdestinationcontext11) | [NavBar](#ZH-CN_TOPIC_0000002497444902__navbar12)是页面跳转之前的栈顶页面信息。参数值为navBar，则表示跳转前的页面为Navigation首页。to[NavDestinationContext](NavDestination.md#ZH-CN_TOPIC_0000002529284873__navdestinationcontext11) | [NavBar](#ZH-CN_TOPIC_0000002497444902__navbar12)是页面跳转之后的栈顶页面信息。参数值为navBar，则表示跳转的目标页面为Navigation首页。operation[NavigationOperation](#ZH-CN_TOPIC_0000002497444902__navigationoperation11枚举说明)是当前页面跳转类型。isAnimatedboolean是

页面跳转是否有动画。

true：页面跳转有动画。

false：页面跳转没有动画。

#### InterceptionModeCallback12+

type InterceptionModeCallback = (mode: NavigationMode) => void

Navigation单双栏显示状态发生变更时的拦截回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明mode[NavigationMode](#ZH-CN_TOPIC_0000002497444902__navigationmode9枚举说明)是导航页的显示模式。

#### InterceptionCallback22+

type InterceptionCallback = (from: NavPathInfo | NavBar, to: NavPathInfo | NavBar, pathStack: NavPathStack, operation: NavigationOperation, isAnimated: boolean) => void

Navigation页面跳转前的拦截回调。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明from[NavPathInfo](Navigation.md#ZH-CN_TOPIC_0000002497444902__navpathinfo10) |[NavBar](#ZH-CN_TOPIC_0000002497444902__navbar12)是退场页面信息。参数值为navBar，则表示跳转前的页面为Navigation首页。to[NavPathInfo](Navigation.md#ZH-CN_TOPIC_0000002497444902__navpathinfo10) |[NavBar](#ZH-CN_TOPIC_0000002497444902__navbar12)是进场页面信息。参数值为navBar，则表示跳转的目标页面为Navigation首页。pathStack[NavPathStack](Navigation.md#ZH-CN_TOPIC_0000002497444902__navpathstack10)是页面栈。operation[NavigationOperation](#ZH-CN_TOPIC_0000002497444902__navigationoperation11枚举说明)是当前页面跳转类型。isAnimatedboolean是

页面跳转是否有动画。

true：页面跳转有动画。

false：页面跳转没有动画。

#### NavBar12+

type NavBar = 'navBar'

Navigation首页名字。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

类型说明'navBar'Navigation首页。

#### NavigationMenuItem

导航菜单项，包括菜单图标和菜单信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明valuestring | [Resource14+](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resource)否否

API version 9：显示菜单栏单个选项的文本。

从API version 10开始，不显示菜单栏单个选项的文本。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

iconstring | [Resource14+](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resource)否是

菜单栏单个选项的图标资源路径。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

isEnabled12+boolean否是

使能状态，默认使能（false未使能，true使能）。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

action() => void否是

当前选项被选中的事件回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

symbolIcon12+[SymbolGlyphModifier](动态SymbolGlyphModifier属性设置.md#ZH-CN_TOPIC_0000002529444819__symbolglyphmodifier)否是

菜单栏单个选项的symbol资源（优先级高于icon）。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

#### ToolbarItem10+

工具栏可配置参数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明valueResourceStr否否

工具栏单个选项的显示文本。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

iconResourceStr否是

工具栏单个选项的图标资源路径。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

action() => void否是

当前选项被选中的事件回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

status[ToolbarItemStatus](#ZH-CN_TOPIC_0000002497444902__toolbaritemstatus10枚举说明)否是

工具栏单个选项的状态。

默认值：ToolbarItemStatus.NORMAL

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

activeIconResourceStr否是

工具栏单个选项处于ACTIVE态时的图标资源路径。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

symbolIcon12+[SymbolGlyphModifier](动态SymbolGlyphModifier属性设置.md#ZH-CN_TOPIC_0000002529444819__symbolglyphmodifier)否是

工具栏单个选项的symbol资源（优先级高于icon）。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

activeSymbolIcon12+[SymbolGlyphModifier](动态SymbolGlyphModifier属性设置.md#ZH-CN_TOPIC_0000002529444819__symbolglyphmodifier)否是

工具栏单个选项处于ACTIVE态时的symbol资源（优先级高于activeIcon）。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

#### ToolbarItemStatus10+枚举说明

工具栏单个选项的状态。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称值说明NORMAL0设置工具栏单个选项为NORMAL态，该选项显示默认样式，可以触发Hover，Press，Focus事件并显示对应的多态样式。DISABLED1设置工具栏单个选项为DISABLED态， 该选项显示DISABLED态样式，并且不可交互。ACTIVE2设置工具栏单个选项为ACTIVE态， 该选项通过点击事件可以将icon图标更新为activeIcon对应的图片资源。

#### NavigationTitleMode枚举说明

标题栏显示模式。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称值说明Free0

当内容为满一屏的可滚动组件时，标题随着内容向上滚动而缩小（子标题的大小不变、淡出）。向下滚动内容到顶时则恢复原样。

**说明：**

标题随着内容滚动大小联动的动效在title设置为ResourceStr和NavigationCommonTitle时生效，设置成其余自定义节点类型时字体样式无法变化，下拉时只影响标题栏偏移。

可滚动组件不满一屏时，如果想使用联动效果，就要使用滚动组件提供的[edgeEffect](../components/list.md#ZH-CN_TOPIC_0000002529284863__edgeeffect)接口将options参数设置为true。未滚动状态，标题栏高度与Full模式一致；滚动时，标题栏的最小高度与Mini模式一致。

Full1

固定为大标题模式。

默认值：只有主标题时，标题栏高度为112vp；同时有主标题和副标题时，标题栏高度为138vp。

Mini2

固定为小标题模式。

默认值：API version 12之前，只有主标题时，标题栏高度为56vp；同时有主标题和副标题时，标题栏高度为82vp。从API version 12开始，该模式下标题栏高度为56vp。

#### NavigationCommonTitle9+

Navigation通用标题。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明mainstring | [Resource14+](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resource)否否设置主标题。substring | [Resource14+](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resource)否否设置副标题。

#### NavigationCustomTitle9+

Navigation自定义标题。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明builder[CustomBuilder](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__custombuilder8)否否设置标题栏内容。height[TitleHeight](../../guides/枚举说明.md#ZH-CN_TOPIC_0000002529284967__titleheight9) | [Length](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__length)否否设置标题栏高度。

#### NavBarPosition9+枚举说明

导航页位置。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称说明Start双栏显示时，主列在主轴方向首部。End双栏显示时，主列在主轴方向尾部。

#### NavigationMode9+枚举说明

导航页显示模式。Navigation处于分栏显示状态时，导航页和内容区之间会显示分割线。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称值说明Stack0导航页与内容区独立显示，相当于两个页面。Split1

导航页与内容区分两栏显示。

**1.** navBarWidth最终取值与开发者设置值的关系参见表1。

**2.** 缩小组件尺寸时，先缩小内容区的尺寸至minContentWidth，然后再缩小导航页的尺寸至minNavBarWidth。若继续缩小，先缩小内容区，内容区消失后再缩小导航页。

**3.** 设置导航页为固定尺寸时，若持续缩小组件尺寸，导航页最后压缩显示。

**4.** 若只设置了navBarWidth属性，则导航页宽度为navBarWidth，且分割线不可拖动。

**5.** 分割线的热区左右各2vp，建议避让4vp以上。

**6.** Split模式下，内容区若只存在一个页面，则页面左上角不会显示返回按钮。

Auto2

API version 9之前：窗口宽度>=520vp时，采用Split模式显示；窗口宽度<520vp时，采用Stack模式显示。

API version 10及以上：窗口宽度>=600vp时，采用Split模式显示；窗口宽度<600vp时，采用Stack模式显示，600vp等于minNavBarWidth(240vp) + minContentWidth (360vp)。

**表1** navBarWidth最终取值与开发者设置值的关系表

开发者设置的navBarWidth值calcNavBarWidth计算值navBarWidth最终取值navBarWidth < minNavBarWidthNAminNavBarWidthnavBarWidth > maxNavBarWidthcalcNavBarWidth > maxNavBarWidthmaxNavBarWidthnavBarWidth > maxNavBarWidthcalcNavBarWidth < minNavBarWidthminNavBarWidthnavBarWidth > maxNavBarWidthminNavBarWidth ≤ calcNavBarWidth ≤ maxNavBarWidthcalcNavBarWidthminNavBarWidth ≤ navBarWidth ≤ maxNavBarWidthcalcNavBarWidth ≤ minNavBarWidthminNavBarWidthminNavBarWidth ≤ navBarWidth ≤ maxNavBarWidthminNavBarWidth < calcNavBarWidth <= navBarWidthcalcNavBarWidthminNavBarWidth ≤ navBarWidth ≤ maxNavBarWidthcalcNavBarWidth > navBarWidthnavBarWidth

为了简化表示，可以将组件宽度 - minContentWidth - 分割线宽度 (1vp)称为calcNavBarWidth。

#### NavigationOperation11+枚举说明

页面跳转类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称值说明PUSH1本次转场为页面进场。POP2本次转场为页面退场。REPLACE3本次转场为页面替换。

#### BarStyle12+枚举说明

标题栏或工具栏的布局样式。NavDestination的工具栏不支持设置该属性。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称值说明STANDARD0

指定该模式的标题栏或工具栏与内容区采用上下布局。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

STACK1

指定该模式的标题栏或工具栏与内容区采用层叠布局，标题栏或工具栏布局在内容区上层。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

SAFE_AREA_PADDING14+2

将指定该模式的标题栏或工具栏设置为[组件级安全区](尺寸设置.md#ZH-CN_TOPIC_0000002497444850__safeareapadding14)。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

#### NavigationTitleOptions11+

标题栏选项。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明backgroundColor[ResourceColor](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否是

标题栏背景颜色，不设置时为系统默认颜色。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

backgroundBlurStyle[BlurStyle](背景设置.md#ZH-CN_TOPIC_0000002529444791__blurstyle9)否是

标题栏背景模糊样式，不设置时关闭背景模糊效果。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

backgroundBlurStyleOptions19+[BackgroundBlurStyleOptions](背景设置.md#ZH-CN_TOPIC_0000002529444791__backgroundblurstyleoptions10对象说明)否是

标题栏背景模糊选项。

**说明：**

只在设置了backgroundBlurStyle时生效。

不建议与backgroundEffect同时使用。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

backgroundEffect19+[BackgroundEffectOptions](背景设置.md#ZH-CN_TOPIC_0000002529444791__backgroundeffectoptions11)否是

设置标题栏背景属性包括：模糊半径，亮度，饱和度，颜色等。

**说明：**

不建议与backgroundBlurStyleOptions同时使用。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

barStyle12+[BarStyle](#ZH-CN_TOPIC_0000002497444902__barstyle12枚举说明)否是

设置标题栏布局方式。

默认值：BarStyle.STANDARD

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

paddingStart12+[LengthMetrics](../graphics/Graphics.md#ZH-CN_TOPIC_0000002529444761__lengthmetrics12)否是

标题栏起始端内间距。

仅支持以下任一场景：

1. 显示返回图标，即[hideBackButton](#ZH-CN_TOPIC_0000002497444902__hidebackbutton)为false；

2. 使用非自定义标题，即[标题value](#ZH-CN_TOPIC_0000002497444902__title)类型为ResourceStr或NavigationCommonTitle。

默认值：

LengthMetrics.resource($r('sys.float.margin_left'))。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

paddingEnd12+[LengthMetrics](../graphics/Graphics.md#ZH-CN_TOPIC_0000002529444761__lengthmetrics12)否是

标题栏结束端内间距。

仅支持以下任一场景：

1. 使用非自定义菜单，即[菜单value](#ZH-CN_TOPIC_0000002497444902__menus)为Array<NavigationMenuItem>；

2. 没有右上角菜单，且使用非自定义标题，即[标题value](#ZH-CN_TOPIC_0000002497444902__title)类型为ResourceStr或NavigationCommonTitle。

默认值：

LengthMetrics.resource($r('sys.float.margin_right'))

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

mainTitleModifier13+[TextModifier](动态属性设置.md)否是

主标题属性修改器。

1. 通过Modifier设置的属性会覆盖系统默认的属性（如果Modifier设置了fontSize，maxFontSize，minFontSize任一属性，则系统设置的大小相关属性不生效，以开发者的设置为准）；

2. 不设该属性或者设置了异常值，则恢复系统默认设置；

3. [Free](#ZH-CN_TOPIC_0000002497444902__navigationtitlemode枚举说明)模式下设置字体大小时，原有滑动改变标题大小的效果失效。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

subTitleModifier13+[TextModifier](动态属性设置.md)否是

子标题属性修改器。

1. 通过Modifier设置的属性会覆盖系统默认的属性（如果Modifier设置了fontSize，maxFontSize，minFontSize任一属性，则系统设置的大小相关属性不生效，以开发者的设置为准）；

2. 不设该属性或者设置了异常值，则恢复系统默认设置。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

enableHoverMode13+boolean否是

是否响应悬停态。

使用规则：

1. 需满足Navigation为全屏大小；

2. 标题栏显示模式为[Free](#ZH-CN_TOPIC_0000002497444902__navigationtitlemode枚举说明)时或者标题栏布局方式为[STANDARD](#ZH-CN_TOPIC_0000002497444902__barstyle12枚举说明)时，此接口设置无效。

true：响应悬停态；false：不响应悬停态。

默认值：false

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

#### NavigationToolbarOptions11+

工具栏选项。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明backgroundColor[ResourceColor](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否是

工具栏背景颜色，不设置时为系统默认颜色。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

backgroundBlurStyle[BlurStyle](背景设置.md#ZH-CN_TOPIC_0000002529444791__blurstyle9)否是

工具栏背景模糊样式，不设置时关闭背景模糊效果。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

backgroundBlurStyleOptions19+[BackgroundBlurStyleOptions](背景设置.md#ZH-CN_TOPIC_0000002529444791__backgroundblurstyleoptions10对象说明)否是

工具栏背景模糊选项。

**说明：**

只在设置了backgroundBlurStyle时生效。

不建议与backgroundEffect同时使用。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

backgroundEffect19+[BackgroundEffectOptions](背景设置.md#ZH-CN_TOPIC_0000002529444791__backgroundeffectoptions11)否是

设置工具栏背景属性包括：模糊半径，亮度，饱和度，颜色等。

**说明：**

不建议与backgroundBlurStyleOptions同时使用。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

barStyle14+[BarStyle](#ZH-CN_TOPIC_0000002497444902__barstyle12枚举说明)否是

设置工具栏布局方式。

默认值：BarStyle.STANDARD

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

hideItemValue19+boolean否是

设置是否隐藏工具栏的文本，默认显示文本。

true：隐藏工具栏的文本；false：不隐藏工具栏的文本。

默认值：false

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

moreButtonOptions19+[MoreButtonOptions](#ZH-CN_TOPIC_0000002497444902__morebuttonoptions19)否是

工具栏更多图标的菜单选项。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

#### NavigationMenuOptions19+

页面右上角菜单选项。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明moreButtonOptions[MoreButtonOptions](#ZH-CN_TOPIC_0000002497444902__morebuttonoptions19)否是更多图标的菜单选项。

#### LaunchMode12+枚举说明

路由栈操作模式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称值说明STANDARD0

系统默认的栈操作模式。

push操作会将指定的NavDestination入栈；replace操作会将当前栈顶NavDestination替换。

MOVE_TO_TOP_SINGLETON1从栈底向栈顶查找，如果指定的名称已经存在，则将对应的NavDestination页面移到栈顶（replace操作会将最后的栈顶替换成指定的NavDestination），否则行为和STANDARD一致。POP_TO_SINGLETON2从栈底向栈顶查找，如果指定的名称已经存在，则将其上方的NavDestination页面全部移除（replace操作会将最后的栈顶替换成指定的NavDestination），否则行为和STANDARD一致。NEW_INSTANCE3创建新的NavDestination实例。与STANDARD模式相比，该方法不会复用栈中同名实例。并且指定该模式时，新创建的页面默认会执行push动效。

#### NavigationOptions12+

路由栈操作选项。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明launchMode[LaunchMode](#ZH-CN_TOPIC_0000002497444902__launchmode12枚举说明)否是

路由栈的操作模式。

默认值：LaunchMode.STANDARD

animatedboolean否是

是否支持转场动画。

true：支持转场动画；false：不支持转场动画。

默认值：true

#### MoreButtonOptions19+

更多图标的菜单选项。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明backgroundBlurStyle[BlurStyle](背景设置.md#ZH-CN_TOPIC_0000002529444791__blurstyle9)否是更多图标的菜单背景模糊样式，不设置时关闭背景模糊效果。backgroundBlurStyleOptions[BackgroundBlurStyleOptions](背景设置.md#ZH-CN_TOPIC_0000002529444791__backgroundblurstyleoptions10对象说明)否是

更多图标的菜单背景模糊选项。

**说明：**

只在设置了backgroundBlurStyle时生效。

不建议与backgroundEffect同时使用。

backgroundEffect[BackgroundEffectOptions](背景设置.md#ZH-CN_TOPIC_0000002529444791__backgroundeffectoptions11)否是

设置更多图标的菜单背景属性包括：模糊半径，亮度，饱和度，颜色等。

**说明：**

不建议与backgroundBlurStyleOptions同时使用。

#### SystemBarStyle12+

type SystemBarStyle = SystemBarStyle

状态栏的属性。在设置页面级状态栏属性时使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

类型说明[SystemBarStyle](../../types/interfaces/Interfaces (其他).md#ZH-CN_TOPIC_0000002529284795__systembarstyle12)

状态栏文字颜色。

默认值：'#0xE5FFFFFF'

#### HomePathInfo20+

主页NavDestination的信息。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明namestring否否主页NavDestination的页面名称。paramObject否是主页NavDestination的页面详细参数。

#### 示例

示例效果请以真机为准，系统路由表不支持预览器以及模拟器。

#### 示例1（Navigation页面布局）

该示例主要演示Navigation页面的布局包括标题栏[title](#ZH-CN_TOPIC_0000002497444902__title)，菜单栏[menus](#ZH-CN_TOPIC_0000002497444902__menus)，内容区和工具栏[toolbarConfiguration](#ZH-CN_TOPIC_0000002497444902__toolbarconfiguration10)。

```ets
// xxx.ets

@Entry
@Component
struct NavigationExample {
  private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];

  @Builder
  NavigationTitle() {
    Column() {
      Text('Title')
        .fontColor('#182431')
        .fontSize(30)
        .lineHeight(41)
        .fontWeight(700)
      Text('subtitle')
        .fontColor('#182431')
        .fontSize(14)
        .lineHeight(19)
        .opacity(0.4)
        .margin({ top: 2, bottom: 20 })
    }.alignItems(HorizontalAlign.Start)
  }

  @Builder
  NavigationMenus() {
    Row() {
      // 'resources/base/media/ic_public_add.svg'需要替换为开发者所需的资源文件
      Image('resources/base/media/ic_public_add.svg')
        .width(24)
        .height(24)
      // 'resources/base/media/ic_public_add.svg'需要替换为开发者所需的资源文件
      Image('resources/base/media/ic_public_add.svg')
        .width(24)
        .height(24)
        .margin({ left: 24 })
      // 'common/ic_public_more.svg'需要替换为开发者所需的资源文件
      Image('common/ic_public_more.svg')
        .width(24)
        .height(24)
        .margin({ left: 24 })
    }
  }

  build() {
    Column() {
      Navigation() {
        TextInput({ placeholder: 'search...' })
          .width('90%')
          .height(40)
          .backgroundColor('#FFFFFF')
          .margin({ top: 8 })

        List({ space: 12, initialIndex: 0 }) {
          ForEach(this.arr, (item: number) => {
            ListItem() {
              Text('' + item)
                .width('90%')
                .height(72)
                .backgroundColor('#FFFFFF')
                .borderRadius(24)
                .fontSize(16)
                .fontWeight(500)
                .textAlign(TextAlign.Center)
            }
          }, (item: number) => item.toString())
        }
        .height(324)
        .width('100%')
        .margin({ top: 12, left: '10%' })
      }
      .title(this.NavigationTitle)
      .menus(this.NavigationMenus)
      .titleMode(NavigationTitleMode.Full)
      .toolbarConfiguration([
        {
          // $r("app.string.navigation_toolbar_add")和$r("app.media.ic_public_highlights_ed")需要替换为开发者所需的资源文件
          value: $r("app.string.navigation_toolbar_add"),
          icon: $r("app.media.ic_public_highlights_ed")
        },
        {
          // $r("app.string.navigation_toolbar_app")和$r("app.media.ic_public_highlights")需要替换为开发者所需的资源文件
          value: $r("app.string.navigation_toolbar_app"),
          icon: $r("app.media.ic_public_highlights")
        },
        {
          // $r("app.string.navigation_toolbar_collect")和$r("app.media.ic_public_highlights")需要替换为开发者所需的资源文件
          value: $r("app.string.navigation_toolbar_collect"),
          icon: $r("app.media.ic_public_highlights")
        }
      ])
      .hideTitleBar(false)
      .hideToolBar(false)
      .onTitleModeChange((titleModel: NavigationTitleMode) => {
        console.info('titleMode' + titleModel)
      })
    }.width('100%').height('100%').backgroundColor('#F1F3F5')
  }
}
```

#### 示例2（使用导航控制器方法）

该示例主要演示[NavPathStack](#ZH-CN_TOPIC_0000002497444902__navpathstack10)中方法的使用及路由拦截。

```ets
// Index.ets
@Entry
@Component
struct NavigationExample {
  pageInfos: NavPathStack = new NavPathStack();
  isUseInterception: boolean = false;

  registerInterception() {
    this.pageInfos.setInterception({
      // 页面跳转前拦截，允许操作栈，在当前跳转中生效。
      willShow: (from: NavDestinationContext | "navBar", to: NavDestinationContext | "navBar",
        operation: NavigationOperation, animated: boolean) => {
        if (!this.isUseInterception) {
          return;
        }
        if (typeof to === "string") {
          console.info("target page is navigation home");
          return;
        }
        // 重定向目标页面，更改为pageTwo页面到pageOne页面。
        let target: NavDestinationContext = to as NavDestinationContext;
        if (target.pathInfo.name === 'pageTwo') {
          target.pathStack.pop();
          target.pathStack.pushPathByName('pageOne', null);
        }
      },
      // 页面跳转后回调，在该回调中操作栈在下一次跳转中刷新。
      didShow: (from: NavDestinationContext | "navBar", to: NavDestinationContext | "navBar",
        operation: NavigationOperation, isAnimated: boolean) => {
        if (!this.isUseInterception) {
          return;
        }
        if (typeof from === "string") {
          console.info("current transition is from navigation home");
        } else {
          console.info(`current transition is from  ${(from as NavDestinationContext).pathInfo.name}`);
        }
        if (typeof to === "string") {
          console.info("current transition to is navBar");
        } else {
          console.info(`current transition is to ${(to as NavDestinationContext).pathInfo.name}`);
        }
      },
      // Navigation单双栏显示状态发生变更时触发该回调。
      modeChange: (mode: NavigationMode) => {
        if (!this.isUseInterception) {
          return;
        }
        console.info(`current navigation mode is ${mode}`);
      }
    })
  }

  build() {
    Navigation(this.pageInfos) {
      Column() {
        Button('pushPath', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(20)
          .onClick(() => {
            this.pageInfos.pushPath({ name: 'pageOne' }); //将name指定的NavDestination页面信息入栈
          })
        Button('use interception', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(20)
          .onClick(() => {
            this.isUseInterception = !this.isUseInterception;
            if (this.isUseInterception) {
              this.registerInterception();
            } else {
              this.pageInfos.setInterception(undefined);
            }
          })
      }
    }.title('NavIndex')
  }
}
```

```ets
// PageOne.ets
class TmpClass {
  count: number = 10;
}

@Builder
export function PageOneBuilder(name: string, param: Object) {
  PageOne()
}

@Component
export struct PageOne {
  pageInfos: NavPathStack = new NavPathStack();

  build() {
    NavDestination() {
      Column() {
        Button('pushPathByName', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(20)
          .onClick(() => {
            let tmp = new TmpClass();
            this.pageInfos.pushPathByName('pageTwo', tmp); //将name指定的NavDestination页面信息入栈，传递的数据为param
          })
        Button('singletonLaunchMode', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(20)
          .onClick(() => {
            this.pageInfos.pushPath({ name: 'pageOne' },
              { launchMode: LaunchMode.MOVE_TO_TOP_SINGLETON }); //从栈底向栈顶查找，如果指定的名称已经存在，则将对应的NavDestination页面移到栈顶
          })
        Button('popToname', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(20)
          .onClick(() => {
            this.pageInfos.popToName('pageTwo'); //回退路由栈到第一个名为name的NavDestination页面
            console.info(`popToName ${JSON.stringify(this.pageInfos)}，` +
              `返回值 ${JSON.stringify(this.pageInfos.popToName('pageTwo'))}`);
          })
        Button('popToIndex', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(20)
          .onClick(() => {
            this.pageInfos.popToIndex(1); // 回退路由栈到index指定的NavDestination页面
            console.info(`popToIndex ${JSON.stringify(this.pageInfos)}`);
          })
        Button('moveToTop', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(20)
          .onClick(() => {
            this.pageInfos.moveToTop('pageTwo'); // 将第一个名为name的NavDestination页面移到栈顶
            console.info(`moveToTop ${JSON.stringify(this.pageInfos)}，` +
              `返回值 ${JSON.stringify(this.pageInfos.popToName('pageTwo'))}`);
          })
        Button('moveIndexToTop', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(20)
          .onClick(() => {
            this.pageInfos.moveIndexToTop(1); // 将index指定的NavDestination页面移到栈顶
            console.info(`moveIndexToTop ${JSON.stringify(this.pageInfos)}`);
          })
        Button('clear', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(20)
          .onClick(() => {
            this.pageInfos.clear(); //清除栈中所有页面
          })
        Button('get', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(20)
          .onClick(() => {
            console.info('-------------------');
            console.info(`获取栈中所有NavDestination页面的名称 ${JSON.stringify(this.pageInfos.getAllPathName())}`);
            console.info(`获取index指定的NavDestination页面的参数信息 ${JSON.stringify(this.pageInfos.getParamByIndex(1))}`);
            console.info(`获取全部名为name的NavDestination页面的参数信息 ${JSON.stringify(this.pageInfos.getParamByName('pageTwo'))}`);
            console.info(`获取全部名为name的NavDestination页面的位置索引 ${JSON.stringify(this.pageInfos.getIndexByName('pageOne'))}`);
            console.info(`获取栈大小 ${JSON.stringify(this.pageInfos.size())}`);
          })
      }.width('100%').height('100%')
    }.title('pageOne')
    .onBackPressed(() => {
      const popDestinationInfo = this.pageInfos.pop(); // 弹出路由栈栈顶元素
      console.info(`pop 返回值 ${JSON.stringify(popDestinationInfo)}`);
      return true;
    }).onReady((context: NavDestinationContext) => {
      this.pageInfos = context.pathStack;
    })
  }
}
```

```ets
// PageTwo.ets
@Builder
export function PageTwoBuilder(name: string, param: Object) {
  PageTwo()
}

@Component
export struct PageTwo {
  pathStack: NavPathStack = new NavPathStack();
  private menuItems: Array<NavigationMenuItem> = [
    {
      // 'resources/base/media/undo.svg'需要替换为开发者所需的资源文件
      value: "1",
      icon: 'resources/base/media/undo.svg',
    },
    {
      // 'resources/base/media/redo.svg'需要替换为开发者所需的资源文件
      value: "2",
      icon: 'resources/base/media/redo.svg',
      isEnabled: false,
    },
    {
      // 'resources/base/media/ic_public_ok.svg'需要替换为开发者所需的资源文件
      value: "3",
      icon: 'resources/base/media/ic_public_ok.svg',
      isEnabled: true,
    }
  ];

  build() {
    NavDestination() {
      Column() {
        Button('pushPathByName', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(20)
          .onClick(() => {
            this.pathStack.pushPathByName('pageOne', null);
          })
      }.width('100%').height('100%')
    }.title('pageTwo')
    .menus(this.menuItems)
    .onBackPressed(() => {
      this.pathStack.pop();
      return true;
    })
    .onReady((context: NavDestinationContext) => {
      this.pathStack = context.pathStack;
      console.info(`current page config info is ${JSON.stringify(context.getConfigInRouteMap())}`);
    })
  }
}
```

在src/main目录下的[module.json5配置文件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/module-configuration-file)中的module字段里配置"routerMap": "$profile:router_map"，并在src/main/resources/base/profile目录下新增router_map.json。router_map.json示例如下。

```ets
{
  "routerMap": [
    {
      "name": "pageOne",
      "pageSourceFile": "src/main/ets/pages/PageOne.ets",
      "buildFunction": "PageOneBuilder",
      "data": {
        "description": "this is pageOne"
      }
    },
    {
      "name": "pageTwo",
      "pageSourceFile": "src/main/ets/pages/PageTwo.ets",
      "buildFunction": "PageTwoBuilder"
    }
  ]
}
```

#### 示例3（设置可交互转场动画）

该示例主要演示设置每个[NavDestination](NavDestination.md)子页面的自定义转场动画及可交互转场动画。

```ets
// Index.ets
import { CustomTransition, AnimateCallback } from './CustomNavigationUtils'

@Entry
@Component
struct NavigationExample {
  pageInfos: NavPathStack = new NavPathStack();

  aboutToAppear() {
    if (this.pageInfos === undefined) {
      this.pageInfos = new NavPathStack();
    }
    this.pageInfos.pushPath({ name: 'pageOne', param: CustomTransition.getInstance().getAnimationId() });
  }

  build() {
    Navigation(this.pageInfos) {
    }
    .title('NavIndex')
    .hideNavBar(true)
    .customNavContentTransition((from: NavContentInfo, to: NavContentInfo, operation: NavigationOperation) => {
      if (from.mode == NavDestinationMode.DIALOG || to.mode == NavDestinationMode.DIALOG) {
        return undefined;
      }

      // 首页不进行自定义动画
      if (from.index === -1 || to.index === -1) {
        return undefined;
      }

      CustomTransition.getInstance().operation = operation;
      if (CustomTransition.getInstance().interactive) {
        let customAnimation: NavigationAnimatedTransition = {
          onTransitionEnd: (isSuccess: boolean) => {
            console.info("===== current transition is " + isSuccess);
            CustomTransition.getInstance().recoverState();
            CustomTransition.getInstance().proxy = undefined;
          },
          transition: (transitionProxy: NavigationTransitionProxy) => {
            CustomTransition.getInstance().proxy = transitionProxy;
            let targetIndex: string | undefined = operation == NavigationOperation.PUSH ?
              (to.navDestinationId) : (from.navDestinationId);
            if (targetIndex) {
              CustomTransition.getInstance().fireInteractiveAnimation(targetIndex, operation);
            }
          },
          isInteractive: CustomTransition.getInstance().interactive
        }
        return customAnimation;
      }
      let customAnimation: NavigationAnimatedTransition = {
        onTransitionEnd: (isSuccess: boolean) => {
          console.info(`current transition result is ${isSuccess}`);
        },
        timeout: 7000,
        // 转场开始时系统调用该方法，并传入转场上下文代理对象
        transition: (transitionProxy: NavigationTransitionProxy) => {
          if (!from.navDestinationId || !to.navDestinationId) {
            return;
          }
          // 从封装类CustomTransition中根据子页面的序列获取对应的转场动画回调
          let fromParam: AnimateCallback = CustomTransition.getInstance().getAnimateParam(from.navDestinationId);
          let toParam: AnimateCallback = CustomTransition.getInstance().getAnimateParam(to.navDestinationId);
          if (operation == NavigationOperation.PUSH) {
            if (toParam.start) {
              toParam.start(true, false);
            }
            this.getUIContext()?.animateTo({
              duration: 500, onFinish: () => {
                transitionProxy.finishTransition();
              }
            }, () => {
              if (toParam.finish) {
                toParam.finish(true, false);
              }
            })
          } else {
            if (fromParam.start) {
              fromParam.start(true, true);
            }
            this.getUIContext()?.animateTo({
              duration: 500, onFinish: () => {
                transitionProxy.finishTransition();
              }
            }, () => {
              if (fromParam.finish) {
                fromParam.finish(true, true);
              }
            })
          }
        }
      };
      return customAnimation;
    })
  }
}
```

```ets
// PageOne.ets
import { CustomTransition } from './CustomNavigationUtils';

@Builder
export function PageOneBuilder(name: string, param: Object) {
  PageOne()
}

@Component
export struct PageOne {
  pageInfos: NavPathStack = new NavPathStack();
  @State translateX: string = '0';
  pageId: string = '';
  rectWidth: number = 0;
  interactive: boolean = false;

  registerCallback() {
    CustomTransition.getInstance().registerNavParam(this.pageId, (isPush: boolean, isExit: boolean) => {
      if (isPush) {
        this.translateX = '100%';
      } else {
        this.translateX = '0';
      }
    }, (isPush: boolean, isExit: boolean) => {
      if (isPush) {
        this.translateX = '0';
      } else {
        this.translateX = '100%';
      }
    }, (isPush: boolean, isExit: boolean) => {
      this.translateX = '0';
    }, (operation: NavigationOperation) => {
      if (operation == NavigationOperation.PUSH) {
        this.translateX = '100%';
        this.getUIContext()?.animateTo({
          duration: 1000,
          onFinish: () => {
            this.translateX = '0';
          }
        }, () => {
          this.translateX = '0';
        })
      } else {
        this.translateX = '0';
        this.getUIContext()?.animateTo({
          duration: 1000,
          onFinish: () => {
            this.translateX = '0';
          }
        }, () => {
          this.translateX = '100%';
        })
      }
    }, 200);
  }

  build() {
    NavDestination() {
      Column() {
        Button(`setInteractive`)
          .onClick(() => {
            CustomTransition.getInstance().interactive = !CustomTransition.getInstance().interactive;
            this.interactive = CustomTransition.getInstance().interactive;
          })

        Button('pushPathByName', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(20)
          .onClick(() => {
            //将name指定的NavDestination页面信息入栈，传递的数据为param
            this.pageInfos.pushDestinationByName('pageTwo', CustomTransition.getInstance().getAnimationId());
          })
      }
      .size({ width: '100%', height: '100%' })
    }
    .title('pageOne')
    .onDisAppear(() => {
      CustomTransition.getInstance().unRegisterNavParam(this.pageId);
    })
    .onReady((context: NavDestinationContext) => {
      this.pageInfos = context.pathStack;
      if (context.navDestinationId) {
        this.pageId = context.navDestinationId;
        this.registerCallback();
      }
    })
    .translate({ x: this.translateX })
    .backgroundColor('#F1F3F5')
    .gesture(PanGesture()
      .onActionStart((event: GestureEvent) => {
        this.rectWidth = event.target.area.width as number;
        if (event.offsetX < 0) {
          this.pageInfos.pushPath({ name: 'pageTwo', param: CustomTransition.getInstance().getAnimationId() });
        } else {
          this.pageInfos.pop();
        }
      })
      .onActionUpdate((event: GestureEvent) => {
        let rate = event.fingerList[0].localX / this.rectWidth;
        CustomTransition.getInstance().updateProgress(rate);
      })
      .onActionEnd((event: GestureEvent) => {
        let rate: number = event.fingerList[0].localX / this.rectWidth;
        CustomTransition.getInstance().finishInteractiveAnimation(rate);
      }))
  }
}
```

```ets
// PageTwo.ets
import { CustomTransition } from './CustomNavigationUtils'

@Builder
export function PageTwoBuilder(name: string, param: Object) {
  PageTwo({ param: param as number })
}

@Component
export struct PageTwo {
  pageInfos: NavPathStack = new NavPathStack();
  @State translateX: string = '0';
  pageId: string = '';
  rectWidth: number = 0;
  param: number = 0;

  registerCallback() {
    CustomTransition.getInstance().registerNavParam(this.pageId, (isPush: boolean, isExit: boolean) => {
      if (isPush) {
        this.translateX = '100%'
      } else {
        this.translateX = '0';
      }
    }, (isPush: boolean, isExit: boolean) => {
      if (isPush) {
        this.translateX = '0';
      } else {
        this.translateX = '100%';
      }
    }, (isPush: boolean, isExit: boolean) => {
      this.translateX = '0';
    }, (operation: NavigationOperation) => {
      if (operation == NavigationOperation.PUSH) {
        this.translateX = '100%';
        this.getUIContext()?.animateTo({
          duration: 500, onFinish: () => {
            this.translateX = '0';
          }
        }, () => {
          this.translateX = '0';
        })
      } else {
        this.translateX = '0';
        this.getUIContext()?.animateTo({
          duration: 500, onFinish: () => {
            this.translateX = "0";
          }
        }, () => {
          this.translateX = '100%';
        })
      }
    }, 2000)
  }

  build() {
    NavDestination() {
      Column() {
        Button('pushPathByName', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(20)
          .onClick(() => {
            //将name指定的NavDestination页面信息入栈，传递的数据为param
            this.pageInfos.pushPath({ name: 'pageOne', param: CustomTransition.getInstance().getAnimationId() });
          })
      }
      .size({ width: '100%', height: '100%' })
    }
    .title('pageTwo')
    .gesture(PanGesture()
      .onActionStart((event: GestureEvent) => {
        this.rectWidth = event.target.area.width as number;
        if (event.offsetX < 0) {
          this.pageInfos.pushPath({ name: 'pageOne', param: CustomTransition.getInstance().getAnimationId() });
        } else {
          this.pageInfos.pop();
        }
      })
      .onActionUpdate((event: GestureEvent) => {
        let rate = event.fingerList[0].localX / this.rectWidth;
        CustomTransition.getInstance().updateProgress(rate);
      })
      .onActionEnd((event: GestureEvent) => {
        let rate = event.fingerList[0].localX / this.rectWidth;
        CustomTransition.getInstance().finishInteractiveAnimation(rate);
      }))
    .onAppear(() => {
      this.registerCallback();
    })
    .onDisAppear(() => {
      CustomTransition.getInstance().unRegisterNavParam(this.pageId);
    })
    .onReady((context: NavDestinationContext) => {
      this.pageInfos = context.pathStack;
      if (context.navDestinationId) {
        this.pageId = context.navDestinationId;
        this.registerCallback();
      }
    })
    .translate({ x: this.translateX })
    .backgroundColor(Color.Yellow)
  }
}
```

```ets
// src/main/pages/CustomNavigationUtils.ets
// 自定义接口，用来保存某个页面相关的转场动画回调和参数

export interface AnimateCallback {
  finish: ((isPush: boolean, isExit: boolean) => void | undefined) | undefined;
  start: ((isPush: boolean, isExit: boolean) => void | undefined) | undefined;
  onFinish: ((isPush: boolean, isExit: boolean) => void | undefined) | undefined;
  interactive: ((operation: NavigationOperation) => void | undefined) | undefined;
  timeout: (number | undefined) | undefined;
}

const customTransitionMap: Map<string, AnimateCallback> = new Map();

export class CustomTransition {
  static delegate = new CustomTransition();
  interactive: boolean = false;
  proxy: NavigationTransitionProxy | undefined = undefined;
  private animationId: number = 0;
  operation: NavigationOperation = NavigationOperation.PUSH;

  static getInstance() {
    return CustomTransition.delegate;
  }

  /* 注册某个页面的动画回调
   * name: 注册页面的唯一id
   * startCallback：用来设置动画开始时页面的状态
   * endCallback：用来设置动画结束时页面的状态
   * onFinish：用来执行动画结束后页面的其他操作
   * interactiveCallback: 注册的可交互转场的动效
   * timeout：转场结束的超时时间
   */
  registerNavParam(name: string, startCallback: (operation: boolean, isExit: boolean) => void,
    endCallback: (operation: boolean, isExit: boolean) => void,
    onFinish: (operation: boolean, isExit: boolean) => void,
    interactiveCallback: (operation: NavigationOperation) => void,
    timeout: number): void {
    if (customTransitionMap.has(name)) {
      let param = customTransitionMap.get(name);
      if (param != undefined) {
        param.start = startCallback;
        param.finish = endCallback;
        param.timeout = timeout;
        param.onFinish = onFinish;
        param.interactive = interactiveCallback;
        return;
      }
    }
    let params: AnimateCallback = {
      timeout: timeout,
      start: startCallback,
      finish: endCallback,
      onFinish: onFinish,
      interactive: interactiveCallback
    };
    customTransitionMap.set(name, params);
  }

  getAnimationId() {
    return Date.now();
  }

  unRegisterNavParam(name: string): void {
    customTransitionMap.delete(name);
  }

  fireInteractiveAnimation(id: string, operation: NavigationOperation) {
    let animation = customTransitionMap.get(id)?.interactive;
    if (!animation) {
      return;
    }
    animation(operation);
  }

  updateProgress(progress: number) {
    if (!this.proxy?.updateTransition) {
      return;
    }
    progress = this.operation == NavigationOperation.PUSH ? 1 - progress : progress;
    this.proxy?.updateTransition(progress);
  }

  cancelTransition() {
    if (this.proxy?.cancelTransition) {
      this.proxy.cancelTransition();
    }
  }

  recoverState() {
    if (!this.proxy?.from.navDestinationId || !this.proxy?.to.navDestinationId) {
      return;
    }
    let fromParam = customTransitionMap.get(this.proxy.from.navDestinationId);
    if (fromParam?.onFinish) {
      fromParam.onFinish(false, false);
    }
    let toParam = customTransitionMap.get(this.proxy?.to.navDestinationId);
    if (toParam?.onFinish) {
      toParam.onFinish(true, true);
    }
  }

  finishTransition() {
    this.proxy?.finishTransition();
  }

  finishInteractiveAnimation(rate: number) {
    if (this.operation == NavigationOperation.PUSH) {
      if (rate > 0.5) {
        if (this.proxy?.cancelTransition) {
          this.proxy.cancelTransition();
        }
      } else {
        this.proxy?.finishTransition();
      }
    } else {
      if (rate > 0.5) {
        this.proxy?.finishTransition();
      } else {
        if (this.proxy?.cancelTransition) {
          this.proxy.cancelTransition();
        }
      }
    }
  }

  getAnimateParam(name: string): AnimateCallback {
    let result: AnimateCallback = {
      start: customTransitionMap.get(name)?.start,
      finish: customTransitionMap.get(name)?.finish,
      timeout: customTransitionMap.get(name)?.timeout,
      onFinish: customTransitionMap.get(name)?.onFinish,
      interactive: customTransitionMap.get(name)?.interactive,
    };
    return result;
  }
}
```

在src/main目录下的[module.json5配置文件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/module-configuration-file)中的module字段里配置"routerMap": "$profile:router_map"，并在src/main/resources/base/profile目录下新增router_map.json。router_map.json示例如下。

```ets
{
  "routerMap": [
    {
      "name": "pageOne",
      "pageSourceFile": "src/main/ets/pages/PageOne.ets",
      "buildFunction": "PageOneBuilder",
      "data": {
        "description": "this is pageOne"
      }
    },
    {
      "name": "pageTwo",
      "pageSourceFile": "src/main/ets/pages/PageTwo.ets",
      "buildFunction": "PageTwoBuilder"
    }
  ]
}
```

#### 示例4（Navigation带参返回）

该示例主要演示Navigation通过[NavPathStack](#ZH-CN_TOPIC_0000002497444902__navpathstack10)提供的接口来实现将设置的参数传给上一级页面。

```ets
// Index.ets
@Entry
@Component
struct NavigationExample {
  pageInfo: NavPathStack = new NavPathStack();

  build() {
    Navigation(this.pageInfo) {
      Column() {
        Button('StartTest', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(20)
          .onClick(() => {
            this.pageInfo.pushPath({ name: 'pageOne' }); // 将name指定的NavDestination页面信息入栈。
          })
      }
    }.title('NavIndex')
  }
}
```

```ets
// PageOne.ets
import { BusinessError } from '@kit.BasicServicesKit';

class TmpClass {
  count: number = 10;
}

class ParamWithOp {
  operation: number = 1;
  count: number = 10;
}

@Builder
export function PageOneBuilder(name: string, param: Object) {
  PageOne()
}

@Component
export struct PageOne {
  pageInfo: NavPathStack = new NavPathStack();
  @State message: string = 'Hello World';

  build() {
    NavDestination() {
      Column() {
        Text(this.message)
          .width('80%')
          .height(50)
          .margin(10)

        Button('pushPath', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(10)
          .onClick(() => {
            this.pageInfo.pushPath({
              name: 'pageTwo', param: new ParamWithOp(), onPop: (popInfo: PopInfo) => {
                this.message =
                  `[pushPath]last page is: ${popInfo.info.name},result: ${JSON.stringify(popInfo.result)}`;
              }
            }); // 将name指定的NavDestination页面信息入栈，传递的数据为param，添加接收处理结果的onPop回调。
          })

        Button('pushPathByName', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(10)
          .onClick(() => {
            let tmp = new TmpClass();
            this.pageInfo.pushPathByName('pageTwo', tmp, (popInfo) => {
              this.message =
                `[pushPathByName]last page is: ${popInfo.info.name}, result: ${JSON.stringify(popInfo.result)}`;
            }); // 将name指定的NavDestination页面信息入栈，传递的数据为param，添加接收处理结果的onPop回调。
          })

        Button('pushDestination', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(10)
          .onClick(() => {
            let tmp = new TmpClass();
            // 将name指定的NavDestination页面信息入栈，传递的数据为param，添加接收处理结果的onPop回调。
            this.pageInfo.pushDestination({
              name: 'pageTwo', param: new ParamWithOp(), onPop: (popInfo: PopInfo) => {
                this.message =
                  `[pushDestination]last page is: ${popInfo.info.name}, result: ${JSON.stringify(popInfo.result)}`;
              }
            }).catch((error: BusinessError) => {
              console.error(`[pushDestination]failed, error code = ${error.code}, error.message = ${error.message}.`);
            }).then(() => {
              console.error('[pushDestination]success.');
            });
          })

        Button('pushDestinationByName', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(10)
          .onClick(() => {
            let tmp = new TmpClass();
            // 将name指定的NavDestination页面信息入栈，传递的数据为param，添加接收处理结果的onPop回调。
            this.pageInfo.pushDestinationByName('pageTwo', tmp, (popInfo) => {
              this.message =
                `[pushDestinationByName]last page is: ${popInfo.info.name}, result: ${JSON.stringify(popInfo.result)}`;
            }).catch((error: BusinessError) => {
              console.error(`[pushDestinationByName]failed, error code = ${error.code}, error.message = ${error.message}.`);
            }).then(() => {
              console.error('[pushDestinationByName]success.');
            });
          })

        Button('pushPathWithoutOnPop', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(10)
          .onClick(() => {
            this.pageInfo.pushPath({ name: 'pageTwo', param: new ParamWithOp() }); // 将name指定的NavDestination页面信息入栈。
          })

        Button('pushPathByNameWithoutOnPop', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(10)
          .onClick(() => {
            let tmp = new TmpClass();
            this.pageInfo.pushPathByName('pageTwo', tmp); // 将name指定的NavDestination页面信息入栈，传递的数据为param。
          })

        Button('pushDestinationWithoutOnPop', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(10)
          .onClick(() => {
            let tmp = new TmpClass();
            // 将name指定的NavDestination页面信息入栈，传递的数据为param，添加接收处理结果的onPop回调。
            this.pageInfo.pushDestination({ name: 'pageTwo', param: new ParamWithOp() })
              .catch((error: BusinessError) => {
                console.error(`[pushDestinationWithoutOnPop]failed, error code = ${error.code}, error.message = ${error.message}.`);
              }).then(() => {
              console.error('[pushDestinationWithoutOnPop]success.');
            });
          })

        Button('pushDestinationByNameWithoutOnPop', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(10)
          .onClick(() => {
            let tmp = new TmpClass();
            // 将name指定的NavDestination页面信息入栈，传递的数据为param。
            this.pageInfo.pushDestinationByName('pageTwo', tmp)
              .catch((error: BusinessError) => {
                console.error(`[pushDestinationByNameWithoutOnPop]failed, error code = ${error.code}, error.message = ${error.message}.`);
              }).then(() => {
              console.error('[pushDestinationByNameWithoutOnPop]success.');
            });
          })

        Button('clear', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(10)
          .onClick(() => {
            this.pageInfo.clear(); // 清除栈中所有页面。
          })
      }.width('100%').height('100%')
    }.title('pageOne')
    .onBackPressed(() => {
      this.pageInfo.pop({ number: 1 }); // 弹出路由栈栈顶元素。
      return true;
    }).onReady((context: NavDestinationContext) => {
      this.pageInfo = context.pathStack;
    })
  }
}
```

```ets
// PageTwo.ets
class resultClass {
  constructor(count: number) {
    this.count = count;
  }

  count: number = 10;
}

@Builder
export function PageTwoBuilder() {
  PageTwo();
}

@Component
export struct PageTwo {
  pathStack: NavPathStack = new NavPathStack();

  build() {
    NavDestination() {
      Column() {
        Button('pop', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(20)
          .onClick(() => {
            this.pathStack.pop(new resultClass(1)); // 回退到上一个页面，将处理结果传入push的onPop回调中。
          })

        Button('popToName', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(20)
          .onClick(() => {
            this.pathStack.popToName('pageOne',
              new resultClass(11)); // 将第一个名为name的NavDestination页面移到栈顶，将处理结果传入push的onPop回调中。
          })

        Button('popToIndex', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(20)
          .onClick(() => {
            this.pathStack.popToIndex(0, new resultClass(111)); // 将index指定的NavDestination页面移到栈顶，将处理结果传入push的onPop回调中。
          })

        Button('popWithoutResult', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(20)
          .onClick(() => {
            this.pathStack.pop();
          })

        Button('popToNameWithoutResult', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(20)
          .onClick(() => {
            this.pathStack.popToName('pageOne');
          })

        Button('popToIndexWithoutResult', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(20)
          .onClick(() => {
            this.pathStack.popToIndex(0);
          })
      }.width('100%').height('100%')
    }.title('pageTwo')
    .onBackPressed(() => {
      this.pathStack.pop(new resultClass(0)); // 回退到上一个页面，将处理结果传入push的onPop回调。
      return true;
    }).onReady((context: NavDestinationContext) => {
      this.pathStack = context.pathStack;
    })
  }
}
```

在src/main目录下的[module.json5配置文件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/module-configuration-file)中的module字段里配置"routerMap": "$profile:router_map"，并在src/main/resources/base/profile目录下新增router_map.json。router_map.json示例如下。

```ets
{
  "routerMap": [
    {
      "name": "pageOne",
      "pageSourceFile": "src/main/ets/pages/PageOne.ets",
      "buildFunction": "PageOneBuilder",
      "data": {
        "description": "this is pageOne"
      }
    },
    {
      "name": "pageTwo",
      "pageSourceFile": "src/main/ets/pages/PageTwo.ets",
      "buildFunction": "PageTwoBuilder"
    }
  ]
}
```

#### 示例5（设置背景颜色和模糊效果）

该示例主要演示设置Navigation主页的标题栏、工具栏和[NavDestination](NavDestination.md)页面的标题栏的背景颜色和背景模糊效果。

```ets
// Index
import {
  COLOR1,
  COLOR2,
  BLUR_STYLE_1,
  BLUR_STYLE_2,
  BLUR_STYLE_OPTION_1,
  BLUR_STYLE_OPTION_2,
} from './Utils';

@Entry
@Component
struct Index {
  @Provide('navPathStack') navPathStack: NavPathStack = new NavPathStack();
  @State useColor1: boolean = true;
  @State useBlur1: boolean = true;
  @State useBlurOption1: boolean = true;

  build() {
    Navigation(this.navPathStack) {
      Stack({ alignContent: Alignment.Center }) {
        BackComponent()
          .width('100%')
          .height('100%')
        Column() {
          Stack({ alignContent: Alignment.Center }) {
            Button("switch color")
              .onClick(() => {
                this.useColor1 = !this.useColor1;
              })
          }
          .width('100%')
          .layoutWeight(1)

          Stack({ alignContent: Alignment.Center }) {
            Button("switch blur")
              .onClick(() => {
                this.useBlur1 = !this.useBlur1;
              })
          }
          .width('100%')
          .layoutWeight(1)

          Stack({ alignContent: Alignment.Center }) {
            Button("switch blurOption")
              .onClick(() => {
                this.useBlurOption1 = !this.useBlurOption1;
              })
          }
          .width('100%')
          .layoutWeight(1)

          Stack({ alignContent: Alignment.Center }) {
            Button("push page")
              .onClick(() => {
                this.navPathStack.pushPathByName('NavigationMenu', null);
              })
          }
          .width('100%')
          .layoutWeight(1)
        }
        .width('100%')
        .height('80%')
      }.width('100%')
      .height('100%')
    }
    .width('100%')
    .height('100%')
    // 开发者可以设置标题栏的背景颜色和背景模糊效果
    .title("NavTitle", {
      backgroundColor: this.useColor1 ? COLOR1 : COLOR2,
      backgroundBlurStyle: this.useBlur1 ? BLUR_STYLE_1 : BLUR_STYLE_2,
      barStyle: BarStyle.STACK,
      backgroundBlurStyleOptions: this.useBlurOption1 ? BLUR_STYLE_OPTION_1 : BLUR_STYLE_OPTION_2,
    })
    // 开发者可以设置菜单的背景颜色和背景模糊效果
    .menus([
      { value: "A" },
      { value: "B" },
      { value: "C" },
      { value: "D" },
    ], {
      moreButtonOptions: {
        backgroundBlurStyle: this.useBlur1 ? BLUR_STYLE_1 : BLUR_STYLE_2,
        backgroundBlurStyleOptions: this.useBlurOption1 ? BLUR_STYLE_OPTION_1 : BLUR_STYLE_OPTION_2,
      }
    })
    // 开发者可以设置工具栏的背景颜色和背景模糊效果
    .toolbarConfiguration([
      { value: "A" },
      { value: "B" },
      { value: "C" },
      { value: "D" },
      { value: "E" },
      { value: "F" }
    ], {
      backgroundColor: this.useColor1 ? COLOR1 : COLOR2,
      backgroundBlurStyle: this.useBlur1 ? BLUR_STYLE_1 : BLUR_STYLE_2,
      // 开发者可以设置工具栏的菜单的背景颜色和背景模糊效果
      moreButtonOptions: {
        backgroundBlurStyle: this.useBlur1 ? BLUR_STYLE_1 : BLUR_STYLE_2,
        backgroundBlurStyleOptions: this.useBlurOption1 ? BLUR_STYLE_OPTION_1 : BLUR_STYLE_OPTION_2,
      }
    })
  }
}

@Component
export struct BackComponent {
  build() {
    Row() {
      Column() {
      }
      .height('100%')
      .backgroundColor("#3D9DB4")
      .layoutWeight(9)

      Column() {
      }
      .height('100%')
      .backgroundColor("#17A98D")
      .layoutWeight(9)

      Column() {
      }
      .height('100%')
      .backgroundColor("#FFC000")
      .layoutWeight(9)
    }
    .height('100%')
    .width('100%')
  }
}
```

```ets
// PageOne.ets
import {
  COLOR1,
  COLOR2,
  BLUR_STYLE_1,
  BLUR_STYLE_2,
  EFFECT_OPTION_1,
  EFFECT_OPTION_2
} from './Utils';
import { BackComponent } from './Index';

@Builder
export function PageBuilder(name: string, param?: Object) {
  ColorAndBlur();
}

@Component
struct ColorAndBlur {
  @State useColor1: boolean = true;
  @State useBlur1: boolean = true;
  @State useEffect1: boolean = true;

  build() {
    NavDestination() {
      Stack({ alignContent: Alignment.Center }) {
        BackComponent()
          .width('100%')
          .height('100%')
        Column() {
          Stack({ alignContent: Alignment.Center }) {
            Button("switch color")
              .onClick(() => {
                this.useColor1 = !this.useColor1;
              })
          }
          .width('100%')
          .layoutWeight(1)

          Stack({ alignContent: Alignment.Center }) {
            Button("switch blur")
              .onClick(() => {
                this.useBlur1 = !this.useBlur1;
              })
          }
          .width('100%')
          .layoutWeight(1)

          Stack({ alignContent: Alignment.Center }) {
            Button("switch effect")
              .onClick(() => {
                this.useEffect1 = !this.useEffect1;
              })
          }
          .width('100%')
          .layoutWeight(1)
        }
        .width('100%')
        .height('100%')
      }.width('100%')
      .height('100%')
    }
    .width('100%')
    .height('100%')
    // 开发者可以设置标题栏的背景颜色和背景模糊效果
    .title("Destination Title", {
      backgroundColor: this.useColor1 ? COLOR1 : COLOR2,
      backgroundBlurStyle: this.useBlur1 ? BLUR_STYLE_1 : BLUR_STYLE_2,
      barStyle: BarStyle.STACK,
      backgroundEffect: this.useEffect1 ? EFFECT_OPTION_1 : EFFECT_OPTION_2,
    })
    // 开发者可以设置菜单的背景颜色和背景模糊效果
    .menus([
      { value: "A" },
      { value: "B" },
      { value: "C" },
      { value: "D" },
    ], {
      moreButtonOptions: {
        backgroundEffect: this.useEffect1 ? EFFECT_OPTION_1 : EFFECT_OPTION_2,
      }
    })
    // 开发者可以设置工具栏的背景颜色和背景模糊效果
    .toolbarConfiguration([
      { value: "A" },
      { value: "B" },
      { value: "C" },
      { value: "D" },
      { value: "E" },
      { value: "F" }
    ], {
      backgroundEffect: this.useEffect1 ? EFFECT_OPTION_1 : EFFECT_OPTION_2,
      // 开发者可以设置工具栏的菜单的背景颜色和背景模糊效果
      moreButtonOptions: {
        backgroundEffect: this.useEffect1 ? EFFECT_OPTION_1 : EFFECT_OPTION_2,
      }
    })
  }
}
```

```ets
// Utils.ets
export const COLOR1: string = "#80004AAF";
export const COLOR2: string = "#802787D9";
export const BLUR_STYLE_1: BlurStyle = BlurStyle.BACKGROUND_THIN;
export const BLUR_STYLE_2: BlurStyle = BlurStyle.BACKGROUND_THICK;
export const BLUR_STYLE_OPTION_1: BackgroundBlurStyleOptions = {
  colorMode: ThemeColorMode.DARK,
  adaptiveColor: AdaptiveColor.DEFAULT,
  blurOptions: { grayscale: [20, 20] },
  scale: 1
};
export const BLUR_STYLE_OPTION_2: BackgroundBlurStyleOptions = {
  colorMode: ThemeColorMode.LIGHT,
  adaptiveColor: AdaptiveColor.AVERAGE,
  blurOptions: { grayscale: [20, 20] },
  scale: 1
};
export const EFFECT_OPTION_1: BackgroundEffectOptions = {
  radius: 20,
  saturation: 10,
  brightness: 0,
  color: '#66FFFFFF',
  adaptiveColor: AdaptiveColor.DEFAULT,
  blurOptions: { grayscale: [0, 0] },
};
export const EFFECT_OPTION_2: BackgroundEffectOptions = {
  radius: 60,
  saturation: 40,
  brightness: 1,
  color: '#661A1A1A',
  adaptiveColor: AdaptiveColor.AVERAGE,
  blurOptions: { grayscale: [20, 20] },
};
```

在src/main目录下的[module.json5配置文件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/module-configuration-file)中的module字段里配置"routerMap": "$profile:router_map"，并在src/main/resources/base/profile目录下新增router_map.json。router_map.json示例如下。

```ets
{
  "routerMap": [
    {
      "name": "NavigationMenu",
      "pageSourceFile": "src/main/ets/pages/PageOne.ets",
      "buildFunction": "PageBuilder",
      "data": {
        "description": "this is pageOne"
      }
    }
  ]
}
```

#### 示例6（嵌套场景下获取外层栈）

该示例主要演示在嵌套Navigation场景下，如何获取父[NavPathStack](#ZH-CN_TOPIC_0000002497444902__navpathstack10)。

```ets
@Entry
@Component
struct NavigationExample1 {
  @State childNavStack: NavPathStack = new NavPathStack();

  build() {
    Navigation() {
      Stack({ alignContent: Alignment.Center }) {
        Navigation(this.childNavStack) {
          Button('push Path to parent Navigation', { stateEffect: true, type: ButtonType.Capsule })
            .width('80%')
            .height(40)
            .margin(20)
            .onClick(() => {
              // 可以获取父NavPathStack
              let parentStack = this.childNavStack.getParent();
              parentStack?.pushPath({ name: "pageOne" });
            })
        }
        .clip(true)
        .backgroundColor(Color.Orange)
        .width('80%')
        .height('80%')
        .title('ChildNavigation')
      }
      .width('100%')
      .height('100%')
    }
    .backgroundColor(Color.Green)
    .width('100%')
    .height('100%')
    .title('ParentNavigation')
  }
}
```

```ets
// PageOne.ets
@Builder
export function PageOneBuilder(name: string) {
  NavDestination() {
    Text("this is " + name)
  }
  .title(name)
}
```

在src/main目录下的[module.json5配置文件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/module-configuration-file)中的module字段里配置"routerMap": "$profile:router_map"，并在src/main/resources/base/profile目录下新增router_map.json。router_map.json示例如下。

```ets
{
  "routerMap": [
    {
      "name": "pageOne",
      "pageSourceFile": "src/main/ets/pages/PageOne.ets",
      "buildFunction": "PageOneBuilder",
      "data": {
        "description": "this is pageOne"
      }
    }
  ]
}
```

#### 示例7（通过onReady获取栈）

该示例主要演示如下两点功能：

1.

[NavPathStack](#ZH-CN_TOPIC_0000002497444902__navpathstack10)无需声明为状态变量，也可以实现路由栈操作功能。

1.

[NavDestination](NavDestination.md)通过[onReady](NavDestination.md#ZH-CN_TOPIC_0000002529284873__onready11)事件能够拿到对应的[NavPathInfo](#ZH-CN_TOPIC_0000002497444902__navpathinfo10)和所属的[NavPathStack](#ZH-CN_TOPIC_0000002497444902__navpathstack10)。

```ets
class PageParam {
  constructor(num_: number) {
    this.num = num_;
  }

  num: number = 0;
}

@Builder
export function PageOneBuilder(name: string, param: Object) {
  PageOne();
}

@Component
struct PageOne {
  private stack: NavPathStack | null = null;
  private name: string = "";
  private paramNum: number = 0;

  build() {
    NavDestination() {
      Column() {
        Text("NavPathInfo: name: " + this.name + ", paramNum: " + this.paramNum)
        Button('pushPath', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(20)
          .onClick(() => {
            if (this.stack) {
              let p = new PageParam(this.paramNum + 1);
              this.stack.pushPath({ name: "pageOne", param: p });
            }
          })
        Button('pop', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(20)
          .onClick(() => {
            this.stack?.pop();
          })
      }
      .width('100%')
      .height('100%')
    }
    .title('pageOne')
    .onReady((ctx: NavDestinationContext) => {
      // 在NavDestination中能够拿到传来的NavPathInfo和当前所处的NavPathStack
      try {
        this.name = ctx?.pathInfo?.name;
        this.paramNum = (ctx?.pathInfo?.param as PageParam)?.num;
        this.stack = ctx.pathStack;
      } catch (e) {
        console.error(`testTag onReady catch exception: ${JSON.stringify(e)}`);
      }
    })
  }
}

@Entry
@Component
struct NavigationExample2 {
  private stack: NavPathStack = new NavPathStack();

  build() {
    Navigation(this.stack) {
      Stack({ alignContent: Alignment.Center }) {
        Button('pushPath', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(20)
          .onClick(() => {
            let p = new PageParam(1);
            this.stack.pushPath({ name: "pageOne", param: p });
          })
      }
      .width('100%')
      .height('100%')
    }
    .width('100%')
    .height('100%')
    .title('Navigation')
  }
}
```

在src/main目录下的[module.json5配置文件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/module-configuration-file)中的module字段里配置"routerMap": "$profile:router_map"，并在src/main/resources/base/profile目录下新增router_map.json。router_map.json示例如下。

```ets
{
  "routerMap": [
    {
      "name": "pageOne",
      "pageSourceFile": "src/main/ets/pages/Index.ets",
      "buildFunction": "PageOneBuilder",
      "data": {
        "description": "this is pageOne"
      }
    }
  ]
}
```

#### 示例8（NavDestination生命周期时序）

该示例演示[NavDestination](NavDestination.md)的[onAppear](挂载卸载事件.md#ZH-CN_TOPIC_0000002529284813__onappear)，[onDisAppear](挂载卸载事件.md#ZH-CN_TOPIC_0000002529284813__ondisappear)，[onShown](NavDestination.md#ZH-CN_TOPIC_0000002529284873__onshown10)，[onHidden](NavDestination.md#ZH-CN_TOPIC_0000002529284873__onhidden10)，[onWillAppear](NavDestination.md#ZH-CN_TOPIC_0000002529284873__onwillappear12)，[onWillDisappear](NavDestination.md#ZH-CN_TOPIC_0000002529284873__onwilldisappear12)，[onWillShow](NavDestination.md#ZH-CN_TOPIC_0000002529284873__onwillshow12)，[onWillHide](NavDestination.md#ZH-CN_TOPIC_0000002529284873__onwillhide12)接口的生命周期时序。

```ets
@Builder
export function PageOneBuilder(name: string, param: Object) {
  PageOneComponent();
}

@Component
struct PageOneComponent {
  private stack: NavPathStack | null = null;
  @State eventStr: string = "";

  build() {
    NavDestination() {
      Column() {
        Text("event: " + this.eventStr)
        Button('pushPath', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(20)
          .onClick(() => {
            if (this.stack) {
              this.stack.pushPath({ name: "pageOne" });
            }
          })
        Button('pop', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(20)
          .onClick(() => {
            this.stack?.pop();
          })
      }
      .width('100%')
      .height('100%')
    }
    .title('pageOne')
    .onAppear(() => {
      this.eventStr += "<onAppear>";
    })
    .onDisAppear(() => {
      this.eventStr += "<onDisAppear>";
    })
    .onShown(() => {
      this.eventStr += "<onShown>";
    })
    .onHidden(() => {
      this.eventStr += "<onHidden>";
    })
    .onWillAppear(() => {
      this.eventStr += "<onWillAppear>";
    })
    .onWillDisappear(() => {
      this.eventStr += "<onWillDisappear>";
    })
    .onWillShow(() => {
      this.eventStr += "<onWillShow>";
    })
    .onWillHide(() => {
      this.eventStr += "<onWillHide>";
    })
    // onReady会在onAppear之前调用
    .onReady((ctx: NavDestinationContext) => {
      try {
        this.eventStr += "<onReady>";
        this.stack = ctx.pathStack;
      } catch (e) {
        console.error(`testTag onReady catch exception: ${JSON.stringify(e)}`);
      }
    })
  }
}

@Entry
@Component
struct NavigationExample3 {
  private stack: NavPathStack = new NavPathStack();

  build() {
    Navigation(this.stack) {
      Stack({ alignContent: Alignment.Center }) {
        Button('pushPath', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(20)
          .onClick(() => {
            this.stack.pushPath({ name: "pageOne" });
          })
      }
      .width('100%')
      .height('100%')
    }
    .width('100%')
    .height('100%')
    .title('Navigation')
  }
}
```

在src/main目录下的[module.json5配置文件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/module-configuration-file)中的module字段里配置"routerMap": "$profile:router_map"，并在src/main/resources/base/profile目录下新增router_map.json。router_map.json示例如下。

```ets
{
  "routerMap": [
    {
      "name": "pageOne",
      "pageSourceFile": "src/main/ets/pages/Index.ets",
      "buildFunction": "PageOneBuilder",
      "data": {
        "description": "this is pageOne"
      }
    }
  ]
}
```

#### 示例9（标题栏布局效果）

该示例演示Navigation标题栏STACK布局效果。

```ets
@Entry
@Component
struct NavigationExample {
  private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11];
  private scrollerForScroll: Scroller = new Scroller();
  @State barStyle: BarStyle = BarStyle.STANDARD;

  build() {
    Column() {
      Navigation() {
        Column() {
          Scroll(this.scrollerForScroll) {
            Column() {
              // $r('app.media.image_1')需要替换为开发者所需的资源文件
              Image($r('app.media.image_1'))// 设置与标题栏高度一致，以便观察STACK效果
                .height(138)
                .width('100%')
              Button('BarStyle.STANDARD')
                .height('50vp')
                .onClick(() => {
                  this.barStyle = BarStyle.STANDARD;
                })
              Button('BarStyle.STACK')
                .height('50vp')
                .margin({ top: 12 })
                .onClick(() => {
                  this.barStyle = BarStyle.STACK;
                })

              ForEach(this.arr, (item: number) => {
                ListItem() {
                  Text('' + item)
                    .width('100%')
                    .height(100)
                    .fontSize(16)
                    .textAlign(TextAlign.Center)
                    .borderRadius(10)
                    .backgroundColor(Color.Orange)
                    .margin({ top: 12 })
                }
              }, (item: number) => item.toString())
            }
          }
        }
        .width('100%')
        .height('100%')
        .backgroundColor(0xDCDCDC)
      }
      .title(
        {
          main: 'NavTitle',
          sub: 'subtitle'
        },
        {
          backgroundBlurStyle: BlurStyle.COMPONENT_THICK,
          barStyle: this.barStyle,
        }
      )
      .titleMode(NavigationTitleMode.Free)
      .hideTitleBar(false)
    }.width('100%').height('100%').backgroundColor('#F1F3F5')
  }
}
```

#### 示例10（定义导航控制器派生类）

该示例主要演示如何定义[NavPathStack](#ZH-CN_TOPIC_0000002497444902__navpathstack10)的派生类和派生类在Navigation中的基本用法。

```ets
// Index.ets
import { DerivedNavPathStack, NewParam } from './Utils';

@Entry
@Component
struct Index {
  derivedStack: DerivedNavPathStack = new DerivedNavPathStack();

  aboutToAppear(): void {
    this.derivedStack.setId('origin stack');
  }

  build() {
    Navigation(this.derivedStack) {
      Button('to Page One').margin(20).onClick(() => {
        this.derivedStack.pushPath({
          name: 'pageOne',
          param: new NewParam('push pageOne in homePage when stack size: ' + this.derivedStack.size())
        });
      })
    }
    .title('Home Page')
  }
}
```

```ets
// PageOne.ets
import { DerivedNavPathStack, NewParam } from './Utils';

@Builder
export function pageMap(name: string) {
  PageOne();
}

@Component
struct PageOne {
  derivedStack: DerivedNavPathStack = new DerivedNavPathStack();
  curStringifyParam: string = "NA";

  build() {
    NavDestination() {
      Column() {
        Text(this.derivedStack.getInfo())
          .margin(10)
          .fontSize(25)
          .fontWeight(FontWeight.Bold)
          .textAlign(TextAlign.Start)
        Text('current page param info:')
          .margin(10)
          .fontSize(25)
          .fontWeight(FontWeight.Bold)
          .textAlign(TextAlign.Start)
        Text(this.curStringifyParam)
          .margin(20)
          .fontSize(20)
          .textAlign(TextAlign.Start)
      }.backgroundColor(Color.Pink)

      Button('to Page One').margin(20).onClick(() => {
        this.derivedStack.pushPath({
          name: 'pageOne',
          param: new NewParam('push pageOne in pageOne when stack size: ' + this.derivedStack.size())
        });
      })
    }.title('Page One')
    .onReady((context: NavDestinationContext) => {
      console.info('[derive-test] reached PageOne\'s onReady');
      // 从navdestinationContext获取派生堆栈
      this.derivedStack = context.pathStack as DerivedNavPathStack;
      console.info('[derive-test] -- got derivedStack: ' + this.derivedStack.id);
      this.curStringifyParam = JSON.stringify(context.pathInfo.param);
      console.info('[derive-test] -- got param: ' + this.curStringifyParam);
    })
  }
}
```

```ets
// Utils.ets
export class DerivedNavPathStack extends NavPathStack {
  // 用户定义的属性'id'
  id: string = "__default__";

  // 派生类中的新功能
  setId(id: string) {
    this.id = id;
  }

  // 派生类中的新功能
  getInfo(): string {
    return "this page used Derived NavPathStack, id: " + this.id;
  }

  // 重载NavPathStack的功能
  pushPath(info: NavPathInfo, animated?: boolean): void
  pushPath(info: NavPathInfo, options?: NavigationOptions): void
  pushPath(info: NavPathInfo, secArg?: boolean | NavigationOptions): void {
    console.info('[derive-test] reached DerivedNavPathStack\'s pushPath');
    if (typeof secArg === 'boolean') {
      super.pushPath(info, secArg);
    } else {
      super.pushPath(info, secArg);
    }
  }

  // 重写和重载NavPathStack的函数
  pop(animated?: boolean | undefined): NavPathInfo | undefined
  pop(result: Object, animated?: boolean | undefined): NavPathInfo | undefined
  pop(result?: Object, animated?: boolean | undefined): NavPathInfo | undefined {
    console.info('[derive-test] reached DerivedNavPathStack\'s pop');
    return super.pop(result, animated);
  }

  // 基类的其他功能...
}

export class NewParam {
  info: string = "__default_param__";

  constructor(info: string) {
    this.info = info;
  }
}
```

在src/main目录下的[module.json5配置文件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/module-configuration-file)中的module字段里配置"routerMap": "$profile:router_map"，并在src/main/resources/base/profile目录下新增router_map.json。router_map.json示例如下。

```ets
{
  "routerMap": [
    {
      "name": "pageOne",
      "pageSourceFile": "src/main/ets/pages/PageOne.ets",
      "buildFunction": "pageMap",
      "data": {
        "description": "this is pageOne"
      }
    }
  ]
}
```

#### 示例11（使用Symbol组件）

该示例主要演示Navigation和[NavDestination](NavDestination.md)如何使用Symbol组件。

```ets
// Index.ets
import { SymbolGlyphModifier } from '@kit.ArkUI';

@Entry
@Component
struct NavigationExample {
  @Provide('navPathStack') navPathStack: NavPathStack = new NavPathStack();
  @State menuItems: Array<NavigationMenuItem> = [
    {
      // 'resources/base/media/ic_public_ok.svg'需要替换为开发者所需的资源文件
      value: 'menuItem1',
      icon: 'resources/base/media/ic_public_ok.svg' // 图标资源路径
    },
    {
      // resources/base/media/ic_public_ok.svg'需要替换为开发者所需的资源文件
      value: 'menuItem2',
      icon: 'resources/base/media/ic_public_ok.svg', // 图标资源路径
      symbolIcon: new SymbolGlyphModifier($r('sys.symbol.ohos_folder_badge_plus')).fontColor([Color.Red, Color.Green])
        .renderingStrategy(SymbolRenderingStrategy.MULTIPLE_COLOR),
    },
    {
      value: 'menuItem3',
      symbolIcon: new SymbolGlyphModifier($r('sys.symbol.ohos_lungs')),
    },
  ];
  @State toolItems: Array<ToolbarItem> = [
    {
      // 'resources/base/media/ic_public_ok.svg'需要替换为开发者所需的资源文件
      value: 'toolItem1',
      icon: 'resources/base/media/ic_public_ok.svg', // 图标资源路径
      symbolIcon: new SymbolGlyphModifier($r('sys.symbol.ohos_lungs')),
      status: ToolbarItemStatus.ACTIVE,
      activeSymbolIcon: new SymbolGlyphModifier($r('sys.symbol.ohos_folder_badge_plus')).fontColor([Color.Red,
        Color.Green]).renderingStrategy(SymbolRenderingStrategy.MULTIPLE_COLOR),
      action: () => {
      }
    },
    {
      // 'resources/base/media/ic_public_more.svg'需要替换为开发者所需的资源文件
      value: 'toolItem2',
      symbolIcon: new SymbolGlyphModifier($r('sys.symbol.ohos_star')),
      status: ToolbarItemStatus.ACTIVE,
      activeIcon: 'resources/base/media/ic_public_more.svg', // 图标资源路径
      action: () => {
      }
    },
    {
      value: 'toolItem3',
      symbolIcon: new SymbolGlyphModifier($r('sys.symbol.ohos_star')),
      status: ToolbarItemStatus.ACTIVE,
      activeSymbolIcon: new SymbolGlyphModifier($r('sys.symbol.ohos_lungs')),
      action: () => {
      }
    }
  ];

  build() {
    Navigation(this.navPathStack) {
      Column() {
        Button('跳转').onClick(() => {
          this.navPathStack.pushPathByName('NavigationMenu', null);
        })
      }
    }
    .backButtonIcon(new SymbolGlyphModifier($r('sys.symbol.ohos_wifi')))
    .titleMode(NavigationTitleMode.Mini)
    .menus(this.menuItems)
    .toolbarConfiguration(this.toolItems)
    .title('一级页面')
  }
}
```

```ets
// PageOne.ets
import { SymbolGlyphModifier } from '@kit.ArkUI';

@Builder
export function myRouter(name: string, param?: Object) {
  NavigationMenu();
}

@Component
export struct NavigationMenu {
  @Consume('navPathStack') navPathStack: NavPathStack;
  @State menuItems: Array<NavigationMenuItem> = [
    {
      // 'resources/base/media/ic_public_ok.svg'需要替换为开发者所需的资源文件
      value: 'menuItem1',
      icon: 'resources/base/media/ic_public_ok.svg', // 图标资源路径
      action: () => {
      }
    },
    {
      value: 'menuItem2',
      symbolIcon: new SymbolGlyphModifier($r('sys.symbol.ohos_folder_badge_plus')).fontColor([Color.Red, Color.Green])
        .renderingStrategy(SymbolRenderingStrategy.MULTIPLE_COLOR),
      action: () => {
      }
    },
    {
      value: 'menuItem3',
      symbolIcon: new SymbolGlyphModifier($r('sys.symbol.repeat_1')),
      action: () => {
      }
    },
  ];

  build() {
    NavDestination() {
      Row() {
        Column() {
        }
        .width('100%')
      }
      .height('100%')
    }
    .hideTitleBar(false)
    .title('NavDestination title')
    .backgroundColor($r('sys.color.ohos_id_color_titlebar_sub_bg'))
    .backButtonIcon(new SymbolGlyphModifier($r('sys.symbol.ohos_star'))
      .fontColor([Color.Blue]))
    .menus(this.menuItems)
  }
}
```

在src/main目录下的[module.json5配置文件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/module-configuration-file)中的module字段里配置"routerMap": "$profile:router_map"，并在src/main/resources/base/profile目录下新增router_map.json。router_map.json示例如下。

```ets
{
  "routerMap": [
    {
      "name": "NavigationMenu",
      "pageSourceFile": "src/main/ets/pages/PageOne.ets",
      "buildFunction": "myRouter",
      "data": {
        "description": "this is pageOne"
      }
    }
  ]
}
```

#### 示例12（设置自定义标题栏边距）

该示例主要演示Navigation和[NavDestination](NavDestination.md)如何设置自定义标题栏边距，如何通过TextModifier修改主副标题文本样式。

```ets
// Index.ets
import { LengthMetrics } from '@kit.ArkUI';
import { MainTitleTextModifier, SubTitleTextModifier } from './Utils';

@Entry
@Component
struct NavigationExample {
  private navPathStack: NavPathStack = new NavPathStack();
  // 初始化标题栏起始端内间距
  @State paddingStart: LengthMetrics = LengthMetrics.vp(0);
  // 初始化标题栏结束端内间距
  @State paddingEnd: LengthMetrics = LengthMetrics.vp(0);
  // 主标题样式修改器
  @State mainTitleModifier: MainTitleTextModifier = new MainTitleTextModifier();
  // 副标题样式修改器
  @State subTitleModifier: SubTitleTextModifier = new SubTitleTextModifier();
  @State applyModifier: boolean = false;
  @State useStyle1: boolean = true;

  build() {
    Navigation(this.navPathStack) {
      Column() {
        // 标题栏内间距切换
        Button('apply padding 32vp')
          .onClick(() => {
            this.paddingStart = LengthMetrics.vp(32);
            this.paddingEnd = LengthMetrics.vp(32);
          })
          .margin({ top: 70 })
          .width(180)
        Button('apply padding 20vp')
          .onClick(() => {
            this.paddingStart = LengthMetrics.vp(20);
            this.paddingEnd = LengthMetrics.vp(20);
          })
          .margin({ top: 40 })
          .width(180)
        Button('pushPage')
          .onClick(() => {
            this.navPathStack.pushPath({ name: 'NavDestinationExample' });
          })
          .margin({ top: 40 })
          .width(180)
        Row() {
          Text(`apply Modifier`)
          Toggle({ isOn: this.applyModifier, type: ToggleType.Switch }).onChange((isOn: boolean) => {
            this.applyModifier = isOn;
          })
        }
        .padding({ top: 95, left: 5, right: 5 })
        .width(180)
        .justifyContent(FlexAlign.SpaceBetween)

        Row() {
          Text(`use Style1`)
          Toggle({ isOn: this.useStyle1, type: ToggleType.Switch }).onChange((isOn: boolean) => {
            this.mainTitleModifier.useStyle1 = isOn;
            this.subTitleModifier.useStyle1 = isOn;
            this.useStyle1 = isOn;
          })
        }
        .padding({ top: 40, left: 5, right: 5 })
        .width(180)
        .justifyContent(FlexAlign.SpaceBetween)
      }
      .width('100%')
      .height('100%')
    }
    .titleMode(NavigationTitleMode.Full)
    .title(
      { main: "Title", sub: "subTitle" },
      this.applyModifier ?
        {
          paddingStart: this.paddingStart,
          paddingEnd: this.paddingEnd,
          mainTitleModifier: this.mainTitleModifier,
          subTitleModifier: this.subTitleModifier,
        } : {
        paddingStart: this.paddingStart,
        paddingEnd: this.paddingEnd
      })
  }
}
```

```ets
// PageOne.ets
import { LengthMetrics } from '@kit.ArkUI';
import { MainTitleTextModifier, SubTitleTextModifier } from './Utils';

@Builder
export function myRouter(name: string, param?: Object) {
  NavDestinationExample();
}
@Component
export struct NavDestinationExample {
  @State menuItems: Array<NavigationMenuItem> = [
    {
      // 'resources/base/media/ic_public_ok.svg'需要替换为开发者所需的资源文件
      value: 'menuItem1',
      icon: 'resources/base/media/ic_public_ok.svg', // 图标资源路径
      action: () => {
      }
    }
  ];
  @State paddingStart: LengthMetrics = LengthMetrics.vp(0);
  @State paddingEnd: LengthMetrics = LengthMetrics.vp(0);
  // 主标题样式修改器
  @State mainTitleModifier: MainTitleTextModifier = new MainTitleTextModifier();
  // 副标题样式修改器
  @State subTitleModifier: SubTitleTextModifier = new SubTitleTextModifier();
  @State applyModifier: boolean = false;
  @State useStyle1: boolean = true;

  build() {
    NavDestination() {
      Column() {
        // 标题栏内间距切换
        Button('apply padding 32vp')
          .onClick(() => {
            this.paddingStart = LengthMetrics.vp(32);
            this.paddingEnd = LengthMetrics.vp(32);
          })
          .margin({ top: 150 })
          .width(180)
        Button('apply padding 20vp')
          .onClick(() => {
            this.paddingStart = LengthMetrics.vp(20);
            this.paddingEnd = LengthMetrics.vp(20);
          })
          .margin({ top: 40 })
          .width(180)
        Row() {
          Text(`apply Modifier`)
          Toggle({ isOn: this.applyModifier, type: ToggleType.Switch }).onChange((isOn: boolean) => {
            this.applyModifier = isOn;
          })
        }
        .padding({ top: 95, left: 5, right: 5 })
        .width(180)
        .justifyContent(FlexAlign.SpaceBetween)

        Row() {
          Text(`use Style1`)
          Toggle({ isOn: this.useStyle1, type: ToggleType.Switch }).onChange((isOn: boolean) => {
            this.mainTitleModifier.useStyle1 = isOn;
            this.subTitleModifier.useStyle1 = isOn;
            this.useStyle1 = isOn;
          })
        }
        .padding({ top: 40, left: 5, right: 5 })
        .width(180)
        .justifyContent(FlexAlign.SpaceBetween)
      }
      .width('100%')
      .height('90%')
    }
    .hideTitleBar(false)
    .title(
      { main: "Title", sub: "subTitle" },
      this.applyModifier ?
        {
          paddingStart: this.paddingStart,
          paddingEnd: this.paddingEnd,
          mainTitleModifier: this.mainTitleModifier,
          subTitleModifier: this.subTitleModifier,
        } : {
        paddingStart: this.paddingStart,
        paddingEnd: this.paddingEnd
      })
    .menus(this.menuItems)
  }
}
```

```ets
// Utils.ets
import { TextModifier } from '@kit.ArkUI';

export class MainTitleTextModifier extends TextModifier {
  useStyle1: boolean = true;

  applyNormalAttribute(instance: TextModifier): void {
    if (this.useStyle1) {
      console.info(`testTag mainTitle use style1`);
      instance.fontColor('#FFFFC000');
      instance.fontSize(35);
      instance.fontWeight(FontWeight.Bolder);
      instance.fontStyle(FontStyle.Normal);
      instance.textShadow({ radius: 5, offsetX: 9 });
    } else {
      console.info(`testTag mainTitle use style2`);
      instance.fontColor('#FF23A98D');
      instance.fontSize(20);
      instance.heightAdaptivePolicy(TextHeightAdaptivePolicy.MIN_FONT_SIZE_FIRST);
      instance.fontWeight(FontWeight.Lighter);
      instance.fontStyle(FontStyle.Italic);
      instance.textShadow({ radius: 3, offsetX: 3 });
    }
  }
}

export class SubTitleTextModifier extends TextModifier {
  useStyle1: boolean = true;

  applyNormalAttribute(instance: TextModifier): void {
    if (this.useStyle1) {
      console.info(`testTag subTitle use style1`);
      instance.fontColor('#FFFFC000');
      instance.fontSize(15);
      instance.fontWeight(FontWeight.Bolder);
      instance.fontStyle(FontStyle.Normal);
      instance.textShadow({ radius: 5, offsetX: 9 });
    } else {
      console.info(`testTag subTitle use style2`);
      instance.fontColor('#FF23A98D');
      instance.fontSize(10);
      instance.fontWeight(FontWeight.Lighter);
      instance.fontStyle(FontStyle.Italic);
      instance.textShadow({ radius: 3, offsetX: 3 });
    }
  }
}
```

在src/main目录下的[module.json5配置文件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/module-configuration-file)中的module字段里配置"routerMap": "$profile:router_map"，并在src/main/resources/base/profile目录下新增router_map.json。router_map.json示例如下。

```ets
{
  "routerMap": [
    {
      "name": "NavDestinationExample",
      "pageSourceFile": "src/main/ets/pages/PageOne.ets",
      "buildFunction": "myRouter",
      "data": {
        "description": "this is pageOne"
      }
    }
  ]
}
```

#### 示例13（自定义转场动画）

该示例主要实现Navigation简单的自定义转场动画。

```ets
// Index.ets
import { AnimateCallback, CustomTransition } from './CustomTransitionUtils'

@Entry
@Component
struct NavigationCustomTransitionExample {
  pageInfos: NavPathStack = new NavPathStack();

  aboutToAppear() {
    this.pageInfos.pushPath({ name: 'PageOne' }, false);
  }

  build() {
    Navigation(this.pageInfos) {
    }
    .hideNavBar(true)
    .customNavContentTransition((from: NavContentInfo, to: NavContentInfo, operation: NavigationOperation) => {
      // 首页不进行自定义动画
      if (from.index === -1 || to.index === -1) {
        return undefined;
      }

      let customAnimation: NavigationAnimatedTransition = {
        timeout: 2000,
        // 转场开始时系统调用该方法，并传入转场上下文代理对象
        transition: (transitionProxy: NavigationTransitionProxy) => {
          if (!from.navDestinationId || !to.navDestinationId) {
            return;
          }
          // 从封装类CustomTransition中根据子页面的序列获取对应的转场动画回调
          let fromParam: AnimateCallback = CustomTransition.getInstance().getAnimateParam(from.navDestinationId);
          let toParam: AnimateCallback = CustomTransition.getInstance().getAnimateParam(to.navDestinationId);
          // Push动画
          if (operation == NavigationOperation.PUSH) {
            if (fromParam.start && toParam.start) {
              // 设置Push转场的两个页面的动画起点
              fromParam.start(true, true);
              toParam.start(true, false);
            }
            this.getUIContext()?.animateTo({
              duration: 500, curve: Curve.Friction, onFinish: () => {
                // 动画结束后需要手动调用finishTransition，否则在timeout时间后由系统调用
                transitionProxy.finishTransition();
              }
            }, () => {
              if (fromParam.finish && toParam.finish) {
                // 设置Push转场的两个页面的动画终点
                fromParam.finish(true, true);
                toParam.finish(true, false);
              }

            })
          } else if (operation == NavigationOperation.POP) {
            // Pop动画
            if (fromParam.start && toParam.start) {
              // 设置Pop转场的两个页面的动画起点
              fromParam.start(false, true);
              toParam.start(false, false);
            }
            this.getUIContext()?.animateTo({
              duration: 500, curve: Curve.Friction, onFinish: () => {
                // 动画结束后需要手动调用finishTransition，否则在timeout时间后由系统调用
                transitionProxy.finishTransition();
              }
            }, () => {
              if (fromParam.finish && toParam.finish) {
                // 设置Pop转场的两个页面的动画终点
                fromParam.finish(false, true);
                toParam.finish(false, false);
              }
            })
          } else {
            // Replace不做动画
          }
        }
      };
      return customAnimation;
    })
  }
}

// PageOne
@Builder
export function PageOneBuilder() {
  PageContainer({ title: "PageOne" });
}

// PageTwo
@Builder
export function PageTwoBuilder() {
  PageContainer({ title: "PageTwo" });
}

@Component
export struct PageContainer {
  pageInfos: NavPathStack = new NavPathStack();
  @State translateY: string = '0';
  pageId: string = '';
  title: string = ''

  registerCallback() {
    CustomTransition.getInstance().registerNavParam(this.pageId,
      // 设置转场动画起点，根据不同的转场类型分别设置
      (isPush: boolean, isExit: boolean) => {
        if (isPush) {
          if (isExit) {
            this.translateY = '0';
          } else {
            this.translateY = '100%';
          }
        } else {
          if (isExit) {
            this.translateY = '0';
          } else {
            this.translateY = '0';
          }
        }
      },
      // 设置转场动画终点，根据不同的转场类型分别设置
      (isPush: boolean, isExit: boolean) => {
        if (isPush) {
          if (isExit) {
            this.translateY = '0';
          } else {
            this.translateY = '0';
          }
        } else {
          if (isExit) {
            this.translateY = '100%';
          } else {
            this.translateY = '0';
          }
        }
      });
  }

  build() {
    NavDestination() {
      Column() {
        Button('push next page', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(20)
          .onClick(() => {
            this.pageInfos.pushPath({ name: this.title == 'PageOne' ? "PageTwo" : "PageOne" });
          })
      }
      .size({ width: '100%', height: '100%' })
    }
    .title(this.title)
    .onDisAppear(() => {
      // 页面销毁时解注册自定义转场动画参数
      CustomTransition.getInstance().unRegisterNavParam(this.pageId);
    })
    .onReady((context: NavDestinationContext) => {
      this.pageInfos = context.pathStack;
      if (context.navDestinationId) {
        this.pageId = context.navDestinationId;
        // 页面创建时注册自定义转场动画参数
        this.registerCallback();
      }
    })
    .translate({ y: this.translateY })
    .backgroundColor(this.title == 'PageOne' ? '#F1F3F5' : '#ff11dee5')
  }
}
```

```ets
// src/main/pages/CustomTransitionUtils.ts 工具类，用来管理所有页面的自定义动画参数注册和获取等
// 自定义接口，用来保存某个页面相关的转场动画回调和参数
export interface AnimateCallback {
  start: ((isPush: boolean, isExit: boolean) => void | undefined) | undefined;
  finish: ((isPush: boolean, isExit: boolean) => void | undefined) | undefined;
}

const customTransitionMap: Map<string, AnimateCallback> = new Map();

export class CustomTransition {
  static delegate = new CustomTransition();

  static getInstance() {
    return CustomTransition.delegate;
  }

  /* 注册某个页面的动画回调
   * name: 注册页面的唯一id
   * startCallback：用来设置动画开始时页面的状态
   * endCallback：用来设置动画结束时页面的状态
   */
  registerNavParam(name: string, startCallback: (isPush: boolean, isExit: boolean) => void,
    endCallback: (isPush: boolean, isExit: boolean) => void): void {
    if (customTransitionMap.has(name)) {
      let param = customTransitionMap.get(name);
      if (param != undefined) {
        param.start = startCallback;
        param.finish = endCallback;
        return;
      }
    }
    let params: AnimateCallback = { start: startCallback, finish: endCallback };
    customTransitionMap.set(name, params);
  }

  unRegisterNavParam(name: string): void {
    customTransitionMap.delete(name);
  }

  getAnimateParam(name: string): AnimateCallback {
    let result: AnimateCallback = {
      start: customTransitionMap.get(name)?.start,
      finish: customTransitionMap.get(name)?.finish
    };
    return result;
  }
}
```

在src/main目录下的[module.json5配置文件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/module-configuration-file)中的module字段里配置"routerMap": "$profile:router_map"，并在src/main/resources/base/profile目录下新增router_map.json。router_map.json示例如下。

```ets
{
  "routerMap": [
    {
      "name": "PageOne",
      "pageSourceFile": "src/main/ets/pages/Index.ets",
      "buildFunction": "PageOneBuilder",
      "data": {
        "description": "this is pageOne"
      }
    },
    {
      "name": "PageTwo",
      "pageSourceFile": "src/main/ets/pages/Index.ets",
      "buildFunction": "PageTwoBuilder"
    }
  ]
}
```

#### 示例14（设置Navigation双栏模式）

该示例主要展示Navigation在双栏模式下，右侧显示默认占位页，并通过[navBarWidthRange](#ZH-CN_TOPIC_0000002497444902__navbarwidthrange10)设置Navigation导航页最小和最大宽度。

此示例在运行前需要在工程配置文件[module.json5](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/module-configuration-file)中的abilities字段里配置"orientation": "auto_rotation"。

```ets
import { ComponentContent } from '@kit.ArkUI';

@Builder function PlaceholderPage() {
  Column() {
    Text("分栏模式占位页")
      .fontSize(28)
      .fontWeight(700)
      .margin({ top: 200 })
  }.width("100%")
  .height("100%")
}

@Entry
@Component
struct NavigationExample {
  @State minNavBarWidth: Dimension | undefined = undefined;
  @State maxNavBarWidth: Dimension | undefined = undefined;
  @State minContentWidth: Dimension|undefined = undefined;
  private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
  @State currentIndex: number = 0;
  placeholder = new ComponentContent(this.getUIContext(), wrapBuilder(PlaceholderPage))

  @Builder
  NavigationTitle() {
    Column() {
      Text('Title')
        .fontColor('#182431')
        .fontSize(30)
        .lineHeight(41)
        .fontWeight(700)
      Text('subtitle')
        .fontColor('#182431')
        .fontSize(14)
        .lineHeight(19)
        .opacity(0.4)
        .margin({ top: 2, bottom: 20 })
    }.alignItems(HorizontalAlign.Start)
  }

  @Builder
  NavigationMenus() {
    Row() {
      // $r('sys.media.ohos_ic_public_add')需要替换为开发者所需的资源文件
      Image($r('sys.media.ohos_ic_public_add'))
        .width(24)
        .height(24)
      // $r('sys.media.ohos_ic_public_add')需要替换为开发者所需的资源文件
      Image($r('sys.media.ohos_ic_public_add'))
        .width(24)
        .height(24)
        .margin({ left: 24 })
      // $r('sys.media.ohos_ic_public_more')需要替换为开发者所需的资源文件
      Image($r('sys.media.ohos_ic_public_more'))
        .width(24)
        .height(24)
        .margin({ left: 24 })
    }.margin({ top: 30 })
  }

  build() {
    Column() {
      Navigation() {
        TextInput({ placeholder: 'search...' })
          .width('90%')
          .height(40)
          .backgroundColor('#FFFFFF')
          .margin({ top: 8 })

        List({ space: 12, initialIndex: 0 }) {
          ForEach(this.arr, (item: number) => {
            ListItem() {
              Text('' + item)
                .width('90%')
                .height(72)
                .backgroundColor('#FFFFFF')
                .borderRadius(24)
                .fontSize(16)
                .fontWeight(500)
                .textAlign(TextAlign.Center)
            }
          }, (item: number) => item.toString())
        }
        .height(324)
        .width('100%')
        .margin({ top: 12, left: '10%' })
      }
      .title(this.NavigationTitle)
      .padding({ left: 12 })
      .menus(this.NavigationMenus)
      .titleMode(NavigationTitleMode.Full)
      .toolbarConfiguration([
        {
          // $r("app.string.navigation_toolbar_add")和$r("app.media.startIcon")需要替换为开发者所需的图像资源文件
          value: $r("app.string.navigation_toolbar_add"),
          icon: $r("app.media.startIcon")
        },
        {
          // $r("app.string.navigation_toolbar_app")和$r("app.media.startIcon")需要替换为开发者所需的图像资源文件
          value: $r("app.string.navigation_toolbar_app"),
          icon: $r("app.media.startIcon")
        },
        {
          // $r("app.string.navigation_toolbar_collect")和$r("app.media.startIcon")需要替换为开发者所需的图像资源文件
          value: $r("app.string.navigation_toolbar_collect"),
          icon: $r("app.media.startIcon")
        }
      ])
      .mode(NavigationMode.Split) // 设置Navigation模式为Split
      .navBarWidthRange([this.minNavBarWidth, this.maxNavBarWidth]) // 设置导航栏宽度范围：[最小宽度, 最大宽度]
      .minContentWidth(this.minContentWidth)
      .hideTitleBar(false)
      .hideToolBar(false)
      .onTitleModeChange((titleModel: NavigationTitleMode) => {
        console.info('titleMode' + titleModel)
      })
      .splitPlaceholder(this.placeholder)
    }.width('100%').height('100%').backgroundColor('#F1F3F5')
  }
}
```

#### 示例15（Navigation工具栏自适应）

该示例主要展示Navigation工具栏的自适应能力的启用及关闭。

在工程配置文件[module.json5](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/module-configuration-file)中的abilities字段里配置"orientation": "landscape"（该工程配置仅方便演示在横屏模式下的Navigation工具栏自适应能力，实际配置可自行设置为"auto_rotation"）。

```ets
import { SymbolGlyphModifier } from '@kit.ArkUI';

@Entry
@Component
struct NavigationExample {
  @Provide('navPathStack') navPathStack:NavPathStack = new NavPathStack();
  @State enable: boolean = false
  @State menuItems:Array<NavigationMenuItem> = [
    {
      value:'menuItem1',
      symbolIcon: new SymbolGlyphModifier($r('sys.symbol.card_writer')),
    },
    {
      value:'menuItem2',
      symbolIcon: new SymbolGlyphModifier($r('sys.symbol.ohos_folder_badge_plus'))
    },
    {
      value:'menuItem3',
      symbolIcon: new SymbolGlyphModifier($r('sys.symbol.ohos_lungs')),
    },
  ]

  @State toolItems:Array<ToolbarItem> = [
    {
      value:'toolItem1',
      symbolIcon:new SymbolGlyphModifier($r('sys.symbol.ohos_lungs')),
      action:()=>{}
    },
    {
      value:'toolItem2',
      symbolIcon:new SymbolGlyphModifier($r('sys.symbol.card_migration')),
      action:()=>{}
    },
    {
      value:'toolItem3',
      symbolIcon:new SymbolGlyphModifier($r('sys.symbol.ohos_star')),
      action:()=>{}
    }
  ]

  build() {
    Navigation(this.navPathStack) {
      Column() {
        Button('启用/关闭自适应').onClick(()=> {
          this.enable = !this.enable;
        })
        Text("启用自适应能力：" + this.enable)
      }
    }
    .mode(NavigationMode.Stack)
    .enableToolBarAdaptation(this.enable) //是否启用工具栏自适应能力
    .backButtonIcon(new SymbolGlyphModifier($r('sys.symbol.ohos_wifi')))
    .titleMode(NavigationTitleMode.Mini)
    .menus(this.menuItems)
    .toolbarConfiguration(this.toolItems)
    .title('一级页面')
  }
}
```

#### 示例16（Navigation使用NavDestination作为导航页）

该示例代码主要展示Navigation可以使用[NavDestination](NavDestination.md)作为导航页（主页）。

```ets
@Component
struct PageHome {
  private stack: NavPathStack | undefined = undefined;

  build() {
    NavDestination() {
      Stack({alignContent: Alignment.Center}) {
        Button('push PageOne').onClick(() => {
          this.stack?.pushPath({name: 'PageOne'});
        })
      }.width('100%').height('100%')
    }.title('PageHome')
    .onReady((ctx: NavDestinationContext) => {
      this.stack = ctx.pathStack;
    })
  }
}

@Builder
function PageHomeBuilder() {
  PageHome()
}

@Component
struct PageOne {
  build() {
    NavDestination() {
      Stack({alignContent: Alignment.Center}) {
        Text('PageOne')
      }.width('100%').height('100%')
    }.title('PageOne')
  }
}

@Builder
function PageOneBuilder() {
  PageOne()
}

@Entry
@Component
struct Index {
  private stack: NavPathStack = new NavPathStack();

  build() {
    // 在这里配置主页NavDestination信息
    Navigation(this.stack, { name: 'PageHome' }) {
    }
    .width('100%').height('100%')
  }
}
```

在src/main目录下的[module.json5配置文件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/module-configuration-file)中的module字段里配置"routerMap": "$profile:router_map"，并在src/main/resources/base/profile目录下新增router_map.json。router_map.json示例如下。

```ets
{
  "routerMap": [
    {
      "name": "PageHome",
      "pageSourceFile": "src/main/ets/pages/Index.ets",
      "buildFunction": "PageHomeBuilder",
      "data": {
        "description": "this is PageHome"
      }
    },
    {
      "name": "PageOne",
      "pageSourceFile": "src/main/ets/pages/Index.ets",
      "buildFunction": "PageOneBuilder",
      "data": {
        "description": "this is PageOne"
      }
    }
  ]
}
```

#### 示例17（使用新增导航控制器方法）

该示例演示如何使用路由拦截功能，并在[NavDestinationContext](NavDestination.md#ZH-CN_TOPIC_0000002529284873__navdestinationcontext11)中获取mode。

```ets
// Index.ets
@Entry
@Component
struct NavigationExample {
  pageInfos: NavPathStack = new NavPathStack();
  isUseInterception: boolean = false;

  registerInterception() {
    this.pageInfos.setInterception({
      // 页面创建前拦截，允许操作栈，在当前跳转中生效。
      interception: (from: NavPathInfo | "navBar", to: NavPathInfo | NavBar, navStack: NavPathStack,
        operation: NavigationOperation, animated: boolean) => {
        if (!this.isUseInterception) {
          return;
        }
        if (typeof to === "string") {
          return;
        }
        // 重定向目标页面，更改为pageTwo页面到pageOne页面。
        let target: NavPathInfo = to as NavPathInfo;
        let navStacktarget: NavPathStack = navStack as NavPathStack;
        if (target.name === 'pageTwo') {
          navStacktarget.pop();
          navStacktarget.pushPathByName('pageOne', null);
        }
      },
      // 页面跳转后回调，在该回调中操作栈在下一次跳转中刷新。
      didShow: (from: NavDestinationContext | "navBar", to: NavDestinationContext | "navBar",
        operation: NavigationOperation, isAnimated: boolean) => {
        if (!this.isUseInterception) {
          return;
        }
        if (typeof from === "string") {
          console.info("current transition is from navigation home");
        } else {
          console.info(`current transition is from  ${(from as NavDestinationContext).pathInfo.name}`);
          console.info(`current transition mode is to ${(to as NavDestinationContext).mode?.toString()}`);
        }
        if (typeof to === "string") {
          console.info("current transition to is navBar");
        } else {
          console.info(`current transition is to ${(to as NavDestinationContext).pathInfo.name}`);
          console.info(`current transition mode is to ${(to as NavDestinationContext).mode?.toString()}`);
        }
      },
      // Navigation单双栏显示状态发生变更时触发该回调。
      modeChange: (mode: NavigationMode) => {
        if (!this.isUseInterception) {
          return;
        }
        console.info(`current navigation mode is ${mode}`);
      }
    })
  }

  build() {
    Navigation(this.pageInfos) {
      Column() {
        Button('pushPath', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(20)
          .onClick(() => {
            this.pageInfos.pushPath({ name: 'pageOne' }); // 将name指定的NavDestination页面信息入栈。
          })
        Button('use interception', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(20)
          .onClick(() => {
            this.isUseInterception = !this.isUseInterception;
            if (this.isUseInterception) {
              this.registerInterception();
            } else {
              this.pageInfos.setInterception(undefined);
            }
          })
      }
    }.title('NavIndex')
  }
}
```

```ets
// PageOne.ets
class TmpClass {
  count: number = 10;
}

@Builder
export function PageOneBuilder(name: string, param: Object) {
  PageOne()
}

@Component
export struct PageOne {
  pageInfos: NavPathStack = new NavPathStack();

  build() {
    NavDestination() {
      Column() {
        Button('pushPathByName', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(20)
          .onClick(() => {
            let tmp = new TmpClass();
            this.pageInfos.pushPathByName('pageTwo', tmp); // 将name指定的NavDestination页面信息入栈，传递的数据为param。
          })
        Button('singletonLaunchMode', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(20)
          .onClick(() => {
            this.pageInfos.pushPath({ name: 'pageOne' },
              { launchMode: LaunchMode.MOVE_TO_TOP_SINGLETON }); // 从栈底向栈顶查找，如果指定的名称已经存在，则将对应的NavDestination页面移到栈顶。
          })
        Button('popToname', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(20)
          .onClick(() => {
            this.pageInfos.popToName('pageTwo'); // 回退路由栈到第一个名为name的NavDestination页面。
            console.info('popToName' + JSON.stringify(this.pageInfos),
              '返回值' + JSON.stringify(this.pageInfos.popToName('pageTwo')));
          })
        Button('popToIndex', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(20)
          .onClick(() => {
            this.pageInfos.popToIndex(1); // 回退路由栈到index指定的NavDestination页面。
            console.info('popToIndex' + JSON.stringify(this.pageInfos));
          })
        Button('moveToTop', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(20)
          .onClick(() => {
            this.pageInfos.moveToTop('pageTwo'); // 将第一个名为name的NavDestination页面移到栈顶。
            console.info('moveToTop' + JSON.stringify(this.pageInfos),
              '返回值' + JSON.stringify(this.pageInfos.moveToTop('pageTwo')));
          })
        Button('moveIndexToTop', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(20)
          .onClick(() => {
            this.pageInfos.moveIndexToTop(1); // 将index指定的NavDestination页面移到栈顶。
            console.info('moveIndexToTop' + JSON.stringify(this.pageInfos));
          })
        Button('clear', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(20)
          .onClick(() => {
            this.pageInfos.clear(); // 清除栈中所有页面。
          })
        Button('get', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(20)
          .onClick(() => {
            console.info('-------------------');
            console.info('获取栈中所有NavDestination页面的名称', JSON.stringify(this.pageInfos.getAllPathName()));
            console.info('获取index指定的NavDestination页面的参数信息',
              JSON.stringify(this.pageInfos.getParamByIndex(1)));
            console.info('获取全部名为name的NavDestination页面的参数信息',
              JSON.stringify(this.pageInfos.getParamByName('pageTwo')));
            console.info('获取全部名为name的NavDestination页面的位置索引',
              JSON.stringify(this.pageInfos.getIndexByName('pageOne')));
            console.info('获取栈大小', JSON.stringify(this.pageInfos.size()));
          })
      }.width('100%').height('100%')
    }.title('pageOne')
    .onBackPressed(() => {
      const popDestinationInfo = this.pageInfos.pop(); // 弹出路由栈栈顶元素。
      console.info('pop' + '返回值' + JSON.stringify(popDestinationInfo));
      return true;
    }).onReady((context: NavDestinationContext) => {
      this.pageInfos = context.pathStack;
    })
  }
}
```

```ets
// PageTwo.ets
@Builder
export function PageTwoBuilder(name: string, param: Object) {
  PageTwo()
}

@Component
export struct PageTwo {
  pathStack: NavPathStack = new NavPathStack();
  private menuItems: Array<NavigationMenuItem> = [
    {
      value: "1",
      icon: 'resources/base/media/undo.svg',
    },
    {
      value: "2",
      icon: 'resources/base/media/redo.svg',
      isEnabled: false,
    },
    {
      value: "3",
      icon: 'resources/base/media/ic_public_ok.svg',
      isEnabled: true,
    }
  ];

  build() {
    NavDestination() {
      Column() {
        Button('pushPathByName', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(20)
          .onClick(() => {
            this.pathStack.pushPathByName('pageOne', null);
          })
      }.width('100%').height('100%')
    }.title('pageTwo')
    .menus(this.menuItems)
    .onBackPressed(() => {
      this.pathStack.pop();
      return true;
    })
    .onReady((context: NavDestinationContext) => {
      this.pathStack = context.pathStack;
      console.info("current page config info is " + JSON.stringify(context.getConfigInRouteMap()));
    })
  }
}
```

在src/main目录下的工程配置文件[module.json5](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/module-configuration-file)中的module字段里配置"routerMap": "$profile:router_map"。

```ets
// src/main/resources/base/profile/router_map.json
{
  "routerMap": [
    {
      "name": "pageOne",
      "pageSourceFile": "src/main/ets/pages/PageOne.ets",
      "buildFunction": "PageOneBuilder",
      "data": {
        "description": "this is pageOne"
      }
    },
    {
      "name": "pageTwo",
      "pageSourceFile": "src/main/ets/pages/PageTwo.ets",
      "buildFunction": "PageTwoBuilder"
    }
  ]
}
```

#### 示例18（设置Navigation可恢复）

该示例演示如何使用[recoverable](#ZH-CN_TOPIC_0000002497444902__recoverable14)配置Navigation可恢复，需要开发者在应用模块初始化时启用[UIAbility](../../modules/ohos/@ohos.app.ability.UIAbility (带界面的应用组件).md)的备份恢复功能，可参考[UIAbility备份恢复](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ability-recover-guideline)。

从API version 14开始，新增recoverable接口。

```ets
// Index.ets
import { SymbolGlyphModifier } from '@kit.ArkUI';

@Entry
@Component
struct NavigationExample {
  navPathStack: NavPathStack = new NavPathStack();
  @State menuItems: Array<NavigationMenuItem> = [
    {
      // 'resources/base/media/startIcon.png'需要替换为开发者所需的资源文件
      value: 'menuItem1',
      icon: 'resources/base/media/startIcon.png' // 图标资源路径
    },
    {
      // resources/base/media/ic_public_ok.svg'需要替换为开发者所需的资源文件
      value: 'menuItem2',
      icon: 'resources/base/media/ic_public_ok.svg', // 图标资源路径
      symbolIcon: new SymbolGlyphModifier($r('sys.symbol.ohos_folder_badge_plus')).fontColor([Color.Red, Color.Green])
        .renderingStrategy(SymbolRenderingStrategy.MULTIPLE_COLOR),
    },
    {
      value: 'menuItem3',
      symbolIcon: new SymbolGlyphModifier($r('sys.symbol.ohos_lungs')),
    },
  ];
  @State toolItems: Array<ToolbarItem> = [
    {
      // 'resources/base/media/ic_public_ok.svg'需要替换为开发者所需的资源文件
      value: 'toolItem1',
      icon: 'resources/base/media/ic_public_ok.svg', // 图标资源路径
      symbolIcon: new SymbolGlyphModifier($r('sys.symbol.ohos_lungs')),
      status: ToolbarItemStatus.ACTIVE,
      activeSymbolIcon: new SymbolGlyphModifier($r('sys.symbol.ohos_folder_badge_plus')).fontColor([Color.Red,
        Color.Green]).renderingStrategy(SymbolRenderingStrategy.MULTIPLE_COLOR),
      action: () => {
      }
    },
    {
      // 'resources/base/media/startIcon.png'需要替换为开发者所需的资源文件
      value: 'toolItem2',
      symbolIcon: new SymbolGlyphModifier($r('sys.symbol.ohos_star')),
      status: ToolbarItemStatus.ACTIVE,
      activeIcon: 'resources/base/media/startIcon.png', // 图标资源路径
      action: () => {
      }
    },
    {
      value: 'toolItem3',
      symbolIcon: new SymbolGlyphModifier($r('sys.symbol.ohos_star')),
      status: ToolbarItemStatus.ACTIVE,
      activeSymbolIcon: new SymbolGlyphModifier($r('sys.symbol.ohos_lungs')),
      action: () => {
      }
    }
  ];

  build() {
    Navigation(this.navPathStack) {
      Column() {
        Button('跳转').onClick(() => {
          this.navPathStack.pushPathByName('NavigationMenu', null);
        })
      }
    }
    .backButtonIcon(new SymbolGlyphModifier($r('sys.symbol.ohos_wifi')))
    .titleMode(NavigationTitleMode.Mini)
    .menus(this.menuItems)
    .toolbarConfiguration(this.toolItems)
    .title('一级页面')
    .id('test')
    .recoverable(true)
  }
}
```

```ets
// PageOne.ets
import { SymbolGlyphModifier } from '@kit.ArkUI';

@Builder
export function myRouter(name: string, param?: Object) {
  NavigationMenu();
}

@Component
export struct NavigationMenu {
  navPathStack: NavPathStack = new NavPathStack();
  @State menuItems: Array<NavigationMenuItem> = [
    {
      // 'resources/base/media/startIcon.png'需要替换为开发者所需的资源文件
      value: 'menuItem1',
      icon: 'resources/base/media/startIcon.png', // 图标资源路径
      action: () => {
      }
    },
    {
      value: 'menuItem2',
      symbolIcon: new SymbolGlyphModifier($r('sys.symbol.ohos_folder_badge_plus')).fontColor([Color.Red, Color.Green])
        .renderingStrategy(SymbolRenderingStrategy.MULTIPLE_COLOR),
      action: () => {
      }
    },
    {
      value: 'menuItem3',
      symbolIcon: new SymbolGlyphModifier($r('sys.symbol.repeat_1')),
      action: () => {
      }
    },
  ];

  build() {
    NavDestination() {
      Row() {
        Column() {
        }
        .width('100%')
      }
      .height('100%')
    }
    .onReady((context: NavDestinationContext) => {
      this.navPathStack = context.pathStack;
    })
    .hideTitleBar(false)
    .title('NavDestination title')
    .backgroundColor($r('sys.color.ohos_id_color_titlebar_sub_bg'))
    .backButtonIcon(new SymbolGlyphModifier($r('sys.symbol.ohos_star'))
    .fontColor([Color.Blue]))
    .menus(this.menuItems)
    .recoverable(true)
  }
}
```

在src/main目录下[module.json5配置文件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/module-configuration-file)中的module字段里配置"routerMap": "$profile:router_map"，并在src/main/resources/base/profile目录下新增router_map.json文件。示例如下：

```ets
{
  "routerMap": [
    {
      "name": "NavigationMenu",
      "pageSourceFile": "src/main/ets/pages/PageOne.ets",
      "buildFunction": "myRouter",
      "data": {
        "description": "this is pageOne"
      }
    }
  ]
}
```

为模拟进程异常退出并重新冷启动，可执行以下步骤：

1.

工程运行成功后点击跳转按钮。

1.

应用上划回退到后台，开启命令行窗口。

1.

输入"hdc shell"，回车后输入"pidof 工程包名"，查询pid值。

1.

输入"aa force-stop 工程包名 -p pid值 -r RESOURCE_CONTROL"进行回车，模拟资源使用不当导致的应用退出。

1.

点击应用重新进入，可发现页面依然是点击跳转按钮后的页面。