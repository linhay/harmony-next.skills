# Swiper

滑块视图容器，提供子组件滑动轮播显示的能力。

  ![image](public_sys-resources/note_3.0-zh-cn.webp)

-

该组件从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

-

Swiper组件通过内置的[PanGesture](PanGesture.md)拖动手势实现滑动轮播效果，将[disableSwipe](#ZH-CN_TOPIC_0000002522240824__disableswipe8)属性设为true时，会禁用该手势监听，从而阻止滑动操作。

-

Swiper中复用[NodeContainer](NodeContainer.md)时，禁止递归流程中子节点更新父节点状态变量。

**子组件**

可以包含子组件。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

-

子组件类型：系统组件和自定义组件，支持渲染控制类型（[if/else](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-rendering-control-ifelse)、[ForEach](ForEach.md)、[LazyForEach](LazyForEach.md)和[Repeat](Repeat.md)）。不建议子组件中混用懒加载组件（包括LazyForEach、Repeat）和非懒加载组件，或者子组件中使用多个懒加载组件，否则可能导致懒加载组件预加载能力失效等问题。不建议在组件动画过程中对数据源进行操作，否则会导致布局出现异常。

-

Swiper子组件的[visibility](显隐控制.md#ZH-CN_TOPIC_0000002522240774__visibility)属性设置为Visibility.None，且Swiper的displayCount属性设置为'auto'时，对应子组件在视窗内不占位，但不影响导航点个数；visibility属性设置为Visibility.None或者Visibility.Hidden时，对应子组件不显示，但依然会在视窗内占位。

-

当Swiper子组件设置了[offset](位置设置.md#ZH-CN_TOPIC_0000002522240778__offset)属性时，会按照子组件的层级进行绘制，层级高的子组件会覆盖层级低的子组件。例如，Swiper包含3个子组件，其中第3个子组件设置了offset({ x : 100 })，那么在横向循环滑动中，第3个子组件会覆盖第1个子组件，此时可设置第1个子组件的[zIndex](Z序控制.md#ZH-CN_TOPIC_0000002553360701__zindex)属性值大于第3个子组件，使第1个子组件层级高于第3个子组件。

-

在走焦到用户定义的子节点时，导航点、箭头会由于[焦点样式](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-common-events-focus-event#焦点样式)修改zIndex的行为被遮挡。

-

在包含大量子组件的场景中，建议采用懒加载、缓存数据、预加载数据和组件复用等方法，以优化Swiper的性能并减少内存占用。最佳实践请参考[优化Swiper组件加载慢丢帧问题](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-swiper_high_performance_development_guide)。

**接口**

Swiper(controller?: SwiperController)

创建滑块视图容器。

卡片能力： 从API version 10开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| controller | SwiperController | 否 | 给组件绑定一个控制器，用来控制组件翻页或者预加载指定子节点。 |

**属性**

除支持[通用属性](通用属性.md)外，还支持以下属性：

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

Swiper组件通用属性[clip](形状裁剪.md#ZH-CN_TOPIC_0000002522240784__clip12)的默认值为true。

**index**

index(value: number)

设置当前在容器中显示的子组件的索引值。

从API version 10开始，该属性支持[$$](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-two-way-sync)双向绑定变量。

卡片能力： 从API version 10开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 当前在容器中显示的子组件的索引值。 默认值：0 说明： 设置的值小于0或大于最大页面索引时，取0。 |

**autoPlay**

autoPlay(value: boolean)

设置子组件是否自动播放。轮播方向为索引从小到大。

[loop](#ZH-CN_TOPIC_0000002522240824__loop)为false时，自动轮播到最后一页时停止轮播。手势切换后不是最后一页时继续播放。当Swiper不可见时会停止轮播。

卡片能力： 从API version 10开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 子组件是否自动播放。 true：自动播放；false：不自动播放。 传入非法值时，按false处理。 |

**autoPlay18+**

autoPlay(autoPlay: boolean, options: AutoPlayOptions)

设置子组件是否自动播放。options入参控制手指或者鼠标等按下屏幕时子组件是否停止自动播放。

当[loop](#ZH-CN_TOPIC_0000002522240824__loop)设置为false时，自动轮播将在到达最后一页时停止。在通过手势切换且未处于最后一页的情况下，轮播将继续进行。Swiper在不可见时，轮播也将停止。

卡片能力： 从API version 18开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 18开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| autoPlay | boolean | 是 | 子组件是否自动播放。 true：自动播放；false：不自动播放。 传入非法值时，按false处理。 |
| options | AutoPlayOptions | 是 | 配置手指或者鼠标等按下屏幕时子组件是否停止自动播放。当stopWhenTouched设置为true时，多指按下场景中任意一个手指抬起后，将自动继续播放。 默认值：{ stopWhenTouched: true }，停止自动播放。 |

**indicator**

indicator(value: DotIndicator | DigitIndicator | boolean)

设置可选导航点指示器样式。

卡片能力： 从API version 10开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | DotIndicator10+ | DigitIndicator10+ | boolean | 是 | 可选导航点指示器样式。 - DotIndicator：圆点指示器样式。 - DigitIndicator：数字指示器样式。 - boolean：是否启用导航点指示器。设置为true启用，false不启用。 默认值：true 默认类型：DotIndicator |

**indicator15+**

indicator(indicator: IndicatorComponentController | DotIndicator | DigitIndicator | boolean)

设置外部绑定的导航点组件控制器。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

设置外部绑定的导航点组件控制器后，可以和外部导航点结合使用。外部导航点支持自定义设置显示位置和大小。详细介绍可参看[Indicator](Indicator.md)。

卡片能力： 从API version 15开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 15开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| indicator | IndicatorComponentController15+ | DotIndicator | DigitIndicator | boolean | 是 | 可选导航点指示器样式。 - IndicatorComponentController：单独导航点指示器控制器。当使用单独导航点指示器控制器时，可以与外部单独导航点进行绑定，但是绑定的单独导航点和内置导航点不能同时存在。 - DotIndicator：圆点指示器样式。 - DigitIndicator：数字指示器样式。 - boolean：是否启用导航点指示器。设置为true启用，false不启用。 默认值：true 默认类型：DotIndicator。 |

**nestedScroll11+**

nestedScroll(value: SwiperNestedScrollMode)

设置Swiper组件和父组件的嵌套滚动模式。[loop](#ZH-CN_TOPIC_0000002522240824__loop)为true时Swiper组件没有边缘，不会触发父组件嵌套滚动。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

由于Swiper的抛滑动画逻辑和其它滚动类组件不同（Swiper一次只能滑动一页，抛滑时做翻页动画），当Swiper内嵌套其它滚动组件时，如果Swiper的翻页动画已经启动，将无法接受子节点上传的滚动偏移量。这时Swiper的翻页动画和子节点的边缘效果动画会同时执行。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | SwiperNestedScrollMode | 是 | Swiper组件和父组件的嵌套滚动模式。 传入非法值时，按SwiperNestedScrollMode.SELF_ONLY处理。 |

**loop**

loop(value: boolean)

设置是否开启循环。在LazyForEach懒循环加载模式下，加载的组件数量建议大于5个。

卡片能力： 从API version 10开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 是否开启循环。 true：开启循环；false：不开启循环。 传入参数非法时，按true处理。 |

**effectMode8+**

effectMode(value: EdgeEffect)

设置边缘滑动效果，[loop](#ZH-CN_TOPIC_0000002522240824__loop)为false或Swiper视窗内一屏显示所有子节点时生效。调用[SwiperController.changeIndex()](#ZH-CN_TOPIC_0000002522240824__changeindex12)、[SwiperController.showNext()](#ZH-CN_TOPIC_0000002522240824__shownext)和[SwiperController.showPrevious()](#ZH-CN_TOPIC_0000002522240824__showprevious)接口跳转至首尾页时不生效回弹。

卡片能力： 从API version 10开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | EdgeEffect | 是 | 边缘滑动效果。 默认值：EdgeEffect.Spring |

**interval**

interval(value: number)

设置使用自动播放时播放的时间间隔。

卡片能力： 从API version 10开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 自动播放时播放的时间间隔。当该值小于duration属性值时，翻页完成后会立即开始下一次轮播。 默认值：3000 单位：毫秒 取值范围：[0, +∞)，设置小于0的值时，按照默认值处理。 |

**duration**

duration(value: number)

设置子组件切换的动画时长。

duration需要和[curve](#ZH-CN_TOPIC_0000002522240824__curve8)一起使用。

curve默认曲线为[interpolatingSpring](@ohos.curves (插值计算).md#ZH-CN_TOPIC_0000002522080738__curvesinterpolatingspring10)，此时动画时长只受曲线自身参数影响，不再受duration的控制。不受duration控制的曲线可以查阅[插值计算](@ohos.curves (插值计算).md)模块，比如，[springMotion](@ohos.curves (插值计算).md#ZH-CN_TOPIC_0000002522080738__curvesspringmotion9)、[responsiveSpringMotion](@ohos.curves (插值计算).md#ZH-CN_TOPIC_0000002522080738__curvesresponsivespringmotion9)和interpolatingSpring类型的曲线不受duration控制。如果希望动画时长受到duration控制，需要给curve设置其他曲线。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 子组件切换的动画时长。 默认值：400 单位：毫秒 取值范围：[0, +∞)，设置小于0的值时，按照默认值处理。 |

**curve8+**

curve(value: Curve | string | ICurve)

设置Swiper的动画曲线，默认为弹簧插值曲线，常用曲线参考[Curve枚举说明](枚举说明.md#ZH-CN_TOPIC_0000002553200889__curve)，也可以通过[插值计算](@ohos.curves (插值计算).md)模块提供的接口创建自定义的插值曲线对象。

卡片能力： 从API version 10开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Curve | string | ICurve | 是 | Swiper的动画曲线。 string类型来源curves.init，curves.steps，curves.cubicBezier，curves.spring函数从API version 9开始废弃，推荐使用Curve和ICurve类型。 默认值：interpolatingSpring(-1, 1, 328, 34) |

**vertical**

vertical(value: boolean)

设置是否为纵向滑动。

卡片能力： 从API version 10开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 是否为纵向滑动。true为纵向滑动，false为横向滑动。 默认值：false |

**itemSpace**

itemSpace(value: number | string)

设置子组件与子组件之间间隙。不支持设置百分比。

类型为number时，默认单位vp。类型为string时，需要显式指定像素单位，如'10px'；未指定像素单位时，如'10'，单位为vp。

卡片能力： 从API version 10开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | string | 是 | 子组件与子组件之间间隙。 默认值：0 取值范围：[0, +∞)，当设置数值小于0或超出Swiper组件宽度范围时，按照默认值处理。 |

**cachedCount8+**

cachedCount(value: number)

设置预加载子组件个数，以当前页面为基准，加载当前显示页面的前后个数。前面item删除，后面会向前补位。例如cachedCount=1时，会将当前显示的页面的前面一页和后面一页的子组件都预加载。如果设置为按组翻页，即displayCount的swipeByGroup参数设为true，预加载时会以组为基本单位。例如cachedCount=1，swipeByGroup=true时，会将当前组的前面一组和后面一组的子组件都预加载。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

-

在连续滑动场景中，一屏显示一个Swiper子组件时，通常将cachedCount值设置为1或2即可。最佳实践请参考[优化Swiper组件加载慢丢帧问题-缓存数据项](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-swiper_high_performance_development_guide#section143504547145)。

-

只在[LazyForEach](LazyForEach.md)和开启了virtualScroll开关的[Repeat](Repeat.md)中生效，生效后超出显示及缓存范围的子节点会被释放。

卡片能力： 从API version 10开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 预加载子组件个数。 默认值：1 取值范围：[0, +∞)，设置小于0的值时，按照默认值处理。 |

**cachedCount15+**

cachedCount(count: number, isShown: boolean)

设置预加载子组件个数。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

- isShown值为true，且设置的count过大时，如果前后预加载范围内可加载的节点不足，循环场景下同一个可加载节点只会布局在一侧。

卡片能力： 从API version 15开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 15开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| count | number | 是 | 预加载子组件个数。 默认值：1 取值范围：[0, +∞)，设置小于0的值时，按照默认值处理。 |
| isShown | boolean | 是 | 预加载范围内的节点是否进行绘制，不下渲染树。 true：预加载范围内的节点进行绘制；false：预加载范围内的节点不进行绘制。 传入非法值时，按false处理。 |

**disableSwipe8+**

disableSwipe(value: boolean)

设置禁用组件滑动切换功能。

卡片能力： 从API version 10开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 禁用组件滑动切换功能。设置为true禁用，false不禁用。 默认值：false |

**displayCount8+**

displayCount(value: number | string | SwiperAutoFill, swipeByGroup?: boolean)

设置Swiper视窗内元素显示个数。

使用number类型时，子元素主轴宽度会基于Swiper主轴宽度适应。子组件按照主轴均分Swiper宽度（减去displayCount-1个itemSpace）的方式进行主轴拉伸（收缩）布局，设置为小于等于0的值时，按默认值1显示。

使用string类型时，根据子元素的主轴宽度线性布局，不再适应Swiper主轴宽度。此时value值仅支持设置为'auto'，设置[customContentTransition](#ZH-CN_TOPIC_0000002522240824__customcontenttransition12)和[onContentDidScroll](#ZH-CN_TOPIC_0000002522240824__oncontentdidscroll12)事件不生效。

使用SwiperAutoFill类型时，子元素主轴宽度会基于Swiper主轴宽度适应。通过设置一个子组件最小宽度值minSize，会根据Swiper当前宽度和minSize值自动计算并更改一页内元素显示个数。当minSize为空或者小于等于0时，Swiper显示1列。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

-

按组进行翻页时，判定翻页的拖拽距离阈值将调整为Swiper宽度的50%（若按子元素翻页，该阈值为子元素宽度的50%）。若最后一组的子元素数量少于displayCount，将利用占位子元素进行填充，占位子元素仅用于布局定位，不显示任何内容，其位置将直接显示Swiper的背景样式。

-

displayCount设置为'auto'，并且设置loop属性的值为false时，选中导航点的位置与视窗内首个页面的位置保持一致。如果翻页完成后，视窗内首个页面仅部分显示在视窗内，选中导航点亦与页面的位置保持一致，位于两个未选中的导航点之间。在此情况下，建议开发者隐藏导航点。

-

导航点样式设定为圆形导航点，视窗内显示子元素数量等于1时（单页场景）或者 displayCount设置为'auto'时，显示导航点数量等于子元素数量。

-

displayCount设置为'auto'时，若设置swipeByGroup为true，则单个子元素按组翻页，一次只能翻一页。在此情况下，建议开发者不设置swipeByGroup或者设置swipeByGroup为false。

-

从API version 18开始，该接口支持在[attributeModifier](动态属性设置.md#ZH-CN_TOPIC_0000002522240800__attributemodifier)中调用。

当导航点样式设定为圆形导航点，视窗内显示子元素数量大于1（多页场景），显示导航点数量情况如下表：

| 子元素总数量是否大于视窗内显示的子元素数量 | 是否按组翻页 | 是否循环 | 圆形导航点显示数量 | 说明 |
| --- | --- | --- | --- | --- |
| 是 | 是 | loop设置为true | 圆形导航点的数量将与组数相等（组数计算方式为子元素总数量除以视窗内显示的子元素数量，若除不尽，则向上取整） | 该效果在displayCount设置为'auto'时不生效 |
| 是 | 是 | loop设置为false | 圆形导航点的数量将与组数相等（组数计算方式为子元素总数量除以视窗内显示的子元素数量，若除不尽，则向上取整） | 该效果在displayCount设置为'auto'时不生效 |
| 是 | 否 | loop设置为true | 圆形导航点的数量将与实际可翻页次数一致（显示导航点的数量等于子元素总数量） | —— |
| 是 | 否 | loop设置为false | 圆形导航点的数量将与实际可翻页次数一致（计算方式是子元素的总数量减去视窗内显示的子元素数量+1个） | 该效果在displayCount设置为'auto'时不生效 |
| 否（同时子元素的总数量大于0） | —— | —— | 显示1个圆形导航点 | 该效果在displayCount设置为'auto'时不生效 |
| 否（同时子元素的总数量等于0） | —— | —— | 显示0个圆形导航点 | —— |

卡片能力： 从API version 10开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | string | SwiperAutoFill10+ | 是 | 视窗内显示的子元素个数。 默认值：1 取值范围：(0, +∞)，设置小于等于0的值时，按照默认值处理。 |
| swipeByGroup11+ | boolean | 否 | 是否按组进行翻页。如果设为true，在翻页时会按组进行翻页，每组内子元素的数量为displayCount value的值；如果为false，则为默认翻页行为，即按照子元素进行翻页。 默认值：false |

**displayCount22+**

displayCount(value: number | string | SwiperAutoFill | ItemFillPolicy, swipeByGroup?: boolean)

设置Swiper视窗内元素显示个数。

使用number类型时，子元素主轴宽度会基于Swiper主轴宽度适应。子组件按照主轴均分Swiper宽度（减去displayCount-1个itemSpace）的方式进行主轴拉伸（收缩）布局，设置为小于等于0的值时，按默认值1显示。

使用string类型时，根据子元素的主轴宽度线性布局，不再适应Swiper主轴宽度。此时value值仅支持设置为'auto'，设置[customContentTransition](#ZH-CN_TOPIC_0000002522240824__customcontenttransition12)和[onContentDidScroll](#ZH-CN_TOPIC_0000002522240824__oncontentdidscroll12)事件不生效。

使用SwiperAutoFill类型时，子元素主轴宽度会基于Swiper主轴宽度适应。通过设置一个子组件最小宽度值minSize，会根据Swiper当前宽度和minSize值自动计算并更改一页内元素显示个数。当minSize为空或者小于等于0时，Swiper显示1列。

使用ItemFillPolicy类型时，子元素主轴宽度会基于Swiper主轴宽度适应。将根据Swiper组件宽度对应断点类型确定显示个数。例如，设置断点类型为ItemFillPolicy.BREAKPOINT_DEFAULT时，在组件宽度相当于sm及更小断点区间时显示1列，相当于md断点区间时显示2列，相当于lg及更大断点区间时显示3列。

参数说明参考[displayCount](#ZH-CN_TOPIC_0000002522240824__displaycount8)。

卡片能力： 从API version 22开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 22开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | string | SwiperAutoFill | ItemFillPolicy | 是 | 视窗内显示的子元素个数。 取值范围：(0, +∞)，设置小于等于0的值时，按照1处理。 |
| swipeByGroup | boolean | 否 | 是否按组进行翻页。如果设为true，在翻页时会按组进行翻页，每组内子元素的数量为displayCount的值；如果为false，则为默认翻页行为，即按照子元素进行翻页。 默认值：false |

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

当Swiper子组件个数小于等于Swiper组件内容区内显示的节点总个数(totalDisplayCount = DisplayCount + prevMargin? (1 : 0) + nextMargin? (1 : 0))时，一般按照非循环模式布局处理，此时，前后边距对应子组件不显示，但依然会在视窗内占位。Swiper组件按照totalDisplayCount个数判断测算规格。例外情况如下：

-

当Swiper子组件个数等于Swiper组件内容区内显示的节点总个数且prevMargin和nextMargin都生效时，设置loop为true支持循环。

-

当Swiper子组件个数等于Swiper组件DisplayCount数 + 1，且prevMargin和nextMargin至少一个生效时，在非按组翻页模式下设置loop为true，会生成截图占位组件(如果使用图片异步加载等显示耗时较长的组件可能不能正确生成截图，不建议在该场景开启循环)，支持循环。

**displayArrow10+**

displayArrow(value: ArrowStyle | boolean, isHoverShow?: boolean)

设置导航点箭头样式。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

Swiper视窗内显示所有子节点时，只显示一屏，无法翻页，左右翻页箭头均不显示。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | ArrowStyle | boolean | 是 | 支持设置箭头和底板样式，异常场景使用ArrowStyle对象中的默认值。设置为false不显示箭头和底板，true显示默认的箭头和底板样式。 默认值：false |
| isHoverShow | boolean | 否 | 设置鼠标悬停时是否显示箭头。 默认值：false 说明： 1. isHoverShow为false时，常驻显示箭头。 2. isHoverShow为true时，有导航点时鼠标悬停在导航点和箭头范围内显示箭头，无导航点时鼠标悬停在Swiper显示范围内显示箭头。 3. 箭头显示时，支持点击翻页。 |

**displayMode**

displayMode(value: SwiperDisplayMode)

设置主轴方向上元素排列的模式，优先以[displayCount](#ZH-CN_TOPIC_0000002522240824__displaycount8)设置的个数显示，displayCount未设置时本属性生效。

卡片能力： 从API version 10开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | SwiperDisplayMode | 是 | 主轴方向上元素排列的模式。 默认值：SwiperDisplayMode.STRETCH |

**nextMargin10+**

nextMargin(value: Length, ignoreBlank?:boolean)

设置后边距，用于露出后一项的一小部分，使用效果可以参考[示例1设置导航点交互及翻页动效](#ZH-CN_TOPIC_0000002522240824__示例1设置导航点交互及翻页动效)。仅当Swiper子组件的布局方式为拉伸时生效，主要包括两种场景：1、displayMode属性设置为SwiperDisplayMode.STRETCH；2、displayCount属性设置为number类型。

当主轴方向为横向布局时，nextMargin或prevMargin中任意一个大于子组件测算的宽度，nextMargin和prevMargin均不显示。

当主轴方向为纵向布局时，nextMargin或prevMargin中任意一个大于子组件测算的高度，nextMargin和prevMargin均不显示。

使用nextMargin/prevMargin接口时，不要对子组件进行[尺寸范围限制](尺寸设置.md#ZH-CN_TOPIC_0000002553360703__constraintsize)，否则子节点主轴将不会被拉伸到预期长度，边距失去效果。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

该接口不支持在[attributeModifier](动态属性设置.md#ZH-CN_TOPIC_0000002522240800__attributemodifier)中调用。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Length | 是 | 后边距。不支持设置百分比。 默认值：0 |
| ignoreBlank12+ | boolean | 否 | 非loop场景下尾页不显示nextMargin。在非loop场景下，设置为true时，尾页不显示空白的nextMargin，尾页的右边缘与Swiper视窗右边缘对齐；设置false时，尾页显示空白nextMargin，尾页的右边缘与Swiper视窗右边缘的距离为nextMargin。 默认值：false 说明： 尾页场景下，prevMargin和nextMargin的值相加作为左边边距显示前一个页面。 |

**prevMargin10+**

prevMargin(value: Length, ignoreBlank?:boolean)

设置前边距，用于露出前一项的一小部分，使用效果可以参考[示例1设置导航点交互及翻页动效](#ZH-CN_TOPIC_0000002522240824__示例1设置导航点交互及翻页动效)。仅当Swiper子组件的布局方式为拉伸时生效，主要包括两种场景：1、displayMode属性设置为SwiperDisplayMode.STRETCH；2、displayCount属性设置为number类型。

当主轴方向为横向布局时，nextMargin/prevMargin中任意一个大于子组件测算的宽度，nextMargin和prevMargin均不显示。

当主轴方向为纵向布局时，nextMargin/prevMargin中任意一个大于子组件测算的高度，nextMargin和prevMargin均不显示。

使用nextMargin/prevMargin接口时，不要对子组件进行[尺寸范围限制](尺寸设置.md#ZH-CN_TOPIC_0000002553360703__constraintsize)，否则子节点主轴将不会被拉伸到预期长度，边距失去效果。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

该接口不支持在[attributeModifier](动态属性设置.md#ZH-CN_TOPIC_0000002522240800__attributemodifier)中调用。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Length | 是 | 前边距。不支持设置百分比。 默认值：0 |
| ignoreBlank12+ | boolean | 否 | 非loop场景下首页不显示prevMargin。在非loop场景下，设置为true时，首页不显示空白的prevMargin，首页的左边缘与Swiper视窗左边缘对齐；设置false时，首页显示空白prevMargin，首页的左边缘与Swiper视窗左边缘的距离为prevMargin。 默认值：false 说明： 首页场景下，prevMargin和nextMargin的值相加作为右边边距显示后一个页面。 |

**indicatorInteractive12+**

indicatorInteractive(value: boolean)

设置禁用组件导航点交互功能。

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 导航点是否可交互。 true：导航点可交互；false：导航点不可交互。 传入参数非法时，按true处理。 |

**pageFlipMode15+**

pageFlipMode(mode: Optional<PageFlipMode>)

设置鼠标滚轮翻页模式。未通过该接口设置时，默认为连续翻页模式，取值为PageFlipMode.CONTINUOUS。

卡片能力： 从API version 15开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 15开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | Optional<PageFlipMode> | 是 | 鼠标滚轮翻页模式。 取undefined时，按取值为PageFlipMode.CONTINUOUS处理。 |

**maintainVisibleContentPosition20+**

maintainVisibleContentPosition(enabled: boolean)

设置显示区域上方或前方插入或删除数据时是否保持可见内容位置不变。适用于使用单一[LazyForEach](LazyForEach.md)作为Swiper子节点的情况，通过LazyForEach的[onDataAdd](LazyForEach.md#ZH-CN_TOPIC_0000002522080924__ondataadd8)、[onDataDelete](LazyForEach.md#ZH-CN_TOPIC_0000002522080924__ondatadelete8)等接口修改数据源。其他场景下，显示区域上方或前方插入或删除数据，可见内容位置会变化。

在[displayCount](#ZH-CN_TOPIC_0000002522240824__displaycount8)属性的swipeByGroup参数设置为true，即按组翻页生效时，一次在显示区域上方或前方插入或删除数据，且插入或删除的是一组节点数量倍数的数据量时，才能保持可见内容位置不变，否则可见内容位置可能会随每组数据重新分组改变。

卡片能力： 从API version 20开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 20开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean | 是 | 设置显示区域上方或前方插入或删除数据时是否要保持可见内容位置不变。 默认值：false，显示区域上方或前方插入或删除数据时可见内容位置会跟随变化。 true：显示区域上方或前方插入或删除数据时可见内容位置不变。如果改变数据源是在动画过程中，由于目标索引变化会导致动画停止。 |

**indicatorStyle(deprecated)**

indicatorStyle(value?: IndicatorStyle)

设置导航点样式。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

从API version 8开始支持，从API version 10开始废弃，建议使用[indicator](#ZH-CN_TOPIC_0000002522240824__indicator)替代。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | IndicatorStyle | 否 | 导航点样式。 |

**SwiperDisplayMode枚举说明**

Swiper在主轴上的尺寸大小模式枚举。

系统能力： SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| Stretch(deprecated) | 0 | Swiper滑动一页的宽度为Swiper组件自身的宽度。 说明：从API version 7开始支持，从API version 10开始废弃，建议使用STRETCH替代。 卡片能力： 从API version 7开始，该接口支持在ArkTS卡片中使用。 |
| AutoLinear(deprecated) | 1 | Swiper滑动一页的宽度为子组件宽度中的最大值。此枚举表现形式与displayCount中使用string类型，将值设置为auto表现一致，具体可参考displayCount说明。 说明：从API version 7开始支持，从API version 10开始废弃，建议使用AUTO_LINEAR替代。 卡片能力： 从API version 7开始，该接口支持在ArkTS卡片中使用。 |
| STRETCH10+ | 0 | Swiper滑动一页的宽度为Swiper组件自身的宽度。 卡片能力： 从API version 10开始，该接口支持在ArkTS卡片中使用。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| AUTO_LINEAR(deprecated) | 1 | Swiper滑动一页的宽度为视窗内最左侧子组件的宽度。此枚举表现形式与displayCount中使用string类型，将值设置为auto表现一致，具体可参考displayCount说明。 说明：从API version 10开始支持，从API version 12开始废弃，建议使用Scroller.scrollTo替代。 卡片能力： 从API version 10开始，该接口支持在ArkTS卡片中使用。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |

**SwiperNestedScrollMode11+枚举说明**

Swiper组件和父组件的嵌套滚动模式枚举。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SELF_ONLY | 0 | Swiper只自身滚动，不与父组件联动。 |
| SELF_FIRST | 1 | Swiper自身先滚动，自身滚动到边缘以后父组件滚动。父组件滚动到边缘以后，如果父组件有边缘效果，则父组件触发边缘效果，否则Swiper触发边缘效果。 |

**SwiperController**

Swiper容器组件的控制器，可以将此对象绑定至Swiper组件，实现控制Swiper翻页等功能。

卡片能力： 从API version 10开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

**constructor**

constructor()

SwiperController的构造函数。

卡片能力： 从API version 10开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

**showNext**

showNext()

翻至下一页。翻页带动效切换过程，时长通过Swiper的[duration](#ZH-CN_TOPIC_0000002522240824__duration)属性设置。

卡片能力： 从API version 10开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

**showPrevious**

showPrevious()

翻至上一页。翻页带动效切换过程，时长通过Swiper的[duration](#ZH-CN_TOPIC_0000002522240824__duration)属性设置。

卡片能力： 从API version 10开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

**changeIndex12+**

changeIndex(index: number, useAnimation?: boolean)

翻至指定页面。

卡片能力： 从API version 12开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 指定页面在Swiper中的索引值。 说明： 设置的值小于0或大于最大页面索引时，取0。 |
| useAnimation | boolean | 否 | 设置翻至指定页面时是否有动效，true表示有动效，false表示没有动效。 默认值：false。 |

**changeIndex15+**

changeIndex(index: number, animationMode?: SwiperAnimationMode | boolean)

翻页至指定页面。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

该接口本身提供了不带动画跳转页面的能力（animationMode设置为false或者SwiperAnimationMode.NO_ANIMATION），不建议使用changeIndex接口启动动画后，直接使用finishAnimation接口打断来实现页面不带动画跳转。

卡片能力： 从API version 15开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 15开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 指定页面在Swiper中的索引值。 说明： 设置的值小于0或大于最大页面索引时，取0。 |
| animationMode | SwiperAnimationMode | boolean | 否 | 设置翻页至指定页面时的动效模式。 默认值：SwiperAnimationMode.NO_ANIMATION 说明： 当传入true时有动效，等同于SwiperAnimationMode.DEFAULT_ANIMATION；当传入false时无动效，等同于SwiperAnimationMode.NO_ANIMATION。 |

**finishAnimation**

finishAnimation(callback?: VoidCallback)

停止播放动画。

卡片能力： 从API version 10开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | VoidCallback | 否 | 动画结束的回调。 |

**preloadItems18+**

preloadItems(indices: Optional<Array<number>>): Promise<void>

控制Swiper预加载指定子节点。调用该接口后会一次性加载所有指定的子节点，因此为了性能考虑，建议分批加载子节点。使用Promise异步回调。

如果SwiperController对象未绑定任何Swiper组件，直接调用该接口，会抛出JS异常，并返回错误码100004。因此使用该接口时，建议通过try-catch捕获异常。

与[LazyForEach](LazyForEach.md)和自定义组件结合使用时，由于[LazyForEach](LazyForEach.md)只会保留缓存范围内的自定义组件，在缓存范围外的会被删除，因此需要开发者保证通过该接口预加载的节点index在缓存范围内。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

Swiper的preloadItems需要在Swiper创建之后去调用，首次预加载推荐在Swiper的[onAppear](挂载卸载事件.md#ZH-CN_TOPIC_0000002522240770__onappear)生命周期中去控制。

卡片能力： 从API version 18开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 18开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| indices | Optional<Array<number>> | 是 | 需预加载的子节点的下标数组。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

错误码：

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[滚动类组件错误码](滚动类组件错误码.md)错误码。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter invalid. Possible causes: 1. The parameter type is not Array<number>; 2. The parameter is an empty array; 3. The parameter contains an invalid index. |
| 100004 | Controller not bound to component. |

**startFakeDrag23+**

startFakeDrag(): boolean

开启模拟拖拽功能。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

-

Swiper已经处在真实手势拖拽中，或者已经开启了模拟拖拽，调用接口会返回false表示操作失败。

-

模拟拖拽无法触发嵌套滚动。

卡片能力： 从API version 23开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 23开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

模型约束： 此接口仅可在Stage模型下使用。

返回值：

| 类型 | 说明 |
| --- | --- |
| boolean | 是否开启模拟拖拽功能。 true表示开启模拟拖拽功能成功；false表示开启模拟拖拽功能失败。 |

**fakeDragBy23+**

fakeDragBy(offset: number): boolean

设置模拟拖拽的拖拽距离。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

-

模拟拖拽的距离需要依赖布局体现，建议接口在布局之前调用，拖拽效果可以在当前帧布局后体现。如果在未布局前调用了多次该接口，当前帧布局时只生效最后一次调用传入的拖拽距离。

-

在循环场景下，传入模拟拖拽的距离过大，导致布局过程中套圈，会多次布局当前视窗显示的子节点时，当次传入的拖拽距离会被调整为拖拽到刚好显示第一个子节点（向布局起点拖拽）或者最后一个子节点（向布局终点方向拖拽）。

-

[onGestureSwipe](#ZH-CN_TOPIC_0000002522240824__ongestureswipe10)事件、[onContentWillScroll](#ZH-CN_TOPIC_0000002522240824__oncontentwillscroll15)事件在拖拽过程中不触发。[customContentTransition](#ZH-CN_TOPIC_0000002522240824__customcontenttransition12)会在布局前触发，由于真实的拖拽距离可能在布局时被调整，在传入拖拽距离过大时，触发事件时的返回的节点显示信息可能与布局结果不一致。

卡片能力： 从API version 23开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 23开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

模型约束： 此接口仅可在Stage模型下使用。

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| offset | number | 是 | 需要模拟拖拽的拖拽距离。 正数表示向布局起点拖拽；负数表示向布局终点方向拖拽。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| boolean | 是否消费传入的拖拽距离。 true表示消费任意传入的拖拽距离；false表示当前没有在模拟拖拽中，或者已经拖拽到边界，没有消费传入的拖拽距离。 设置0为不可消费的拖拽距离。 |

**stopFakeDrag23+**

stopFakeDrag(): boolean

关闭模拟拖拽功能。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

在开启模拟拖拽后，如果接收到真实拖拽手势，模拟拖拽会结束。

卡片能力： 从API version 23开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 23开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

模型约束： 此接口仅可在Stage模型下使用。

返回值：

| 类型 | 说明 |
| --- | --- |
| boolean | 是否关闭模拟拖拽功能。 true表示关闭模拟拖拽功能成功；false表示关闭模拟拖拽功能失败。 |

**isFakeDragging23+**

isFakeDragging(): boolean

获取是否在模拟拖拽中的状态。

卡片能力： 从API version 23开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 23开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

模型约束： 此接口仅可在Stage模型下使用。

返回值：

| 类型 | 说明 |
| --- | --- |
| boolean | 是否处在模拟拖拽状态。 true表示当前处在模拟拖拽状态；false表示当前不处在模拟拖拽状态。 |

**SwiperAnimationMode15+枚举说明**

Swiper组件翻页至指定页面的动效模式。

卡片能力： 从API version 15开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 15开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NO_ANIMATION | 0 | 无动效翻页至指定页面。 |
| DEFAULT_ANIMATION | 1 | 有动效翻页至指定页面。 |
| FAST_ANIMATION | 2 | 先无动效翻页至指定页面附近，再有动效翻页至指定页面。 |

**Indicator10+**

设置导航点距离Swiper组件距离。由于导航点有默认交互区域，交互区域高度为32vp，所以无法让显示部分完全贴底。若想实现完全贴底，可以使用[IndicatorComponent](Indicator.md#ZH-CN_TOPIC_0000002522080832__indicatorcomponent)组件，更灵活地调整位置。

卡片能力： 从API version 10开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

**left**

left(value: Length): T

导航点左侧相对于Swiper的位置。

卡片能力： 从API version 10开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Length | 是 | 设置导航点左侧相对于Swiper的位置。 未设置left和right时，进行自适应大小布局，按照指示器本身大小和Swiper的大小在主轴方向上进行居中对齐。 设置为0时：按照0位置布局计算。 优先级：高于right属性。 取值范围：[0,Swiper宽度-导航点区域宽度]，超出该范围时，取最近的边界值。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| T | 返回当前导航点指示器。 |

**top**

top(value: Length): T

导航点顶部相对于Swiper的位置。

卡片能力： 从API version 10开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Length | 是 | 设置导航点顶部相对于Swiper的位置。 未设置top和bottom时，进行自适应大小布局，按照指示器本身大小和Swiper的大小，在交叉轴方向上，位于底部，效果与设置bottom=0一致。 设置为0时：按照0位置布局计算。 优先级：高于bottom属性。 取值范围：[0,Swiper高度-导航点区域高度]，超出该范围时，取最近的边界值。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| T | 返回当前导航点指示器。 |

**right**

right(value: Length): T

导航点右侧相对于Swiper的位置。

卡片能力： 从API version 10开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Length | 是 | 设置导航点右侧相对于Swiper的位置。 未设置left和right时，进行自适应大小布局，按照指示器本身大小和Swiper的大小在主轴方向上进行居中对齐。 设置为0时：按照0位置布局计算。 优先级：低于left属性。 取值范围：[0,Swiper宽度-导航点区域宽度]，超出该范围 时，取最近的边界值。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| T | 返回当前导航点指示器。 |

**bottom**

bottom(value: Length): T

导航点底部相对于Swiper的位置。

卡片能力： 从API version 10开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Length | 是 | 设置导航点底部相对于Swiper的位置。 未设置top和bottom时，进行自适应大小布局，按照指示器本身大小和Swiper的大小，在交叉轴方向上，位于底部，效果与设置bottom=0一致。 设置为0时：按照0位置布局计算。 优先级：低于top属性。 取值范围：[0,Swiper高度-导航点区域高度]，超出该范围时，取最近的边界值。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| T | 返回当前导航点指示器。 |

**bottom19+**

bottom(bottom: LengthMetrics | Length, ignoreSize: boolean): T

导航点底部相对于Swiper的位置，并可通过ignoreSize属性忽略导航点大小。

卡片能力： 从API version 19开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 19开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bottom | LengthMetrics | Length | 是 | 设置导航点底部相对于Swiper的位置。 未设置top和bottom时，进行自适应大小布局，按照指示器本身大小和Swiper的大小，在交叉轴方向上，位于底部，效果与设置bottom=0一致。 设置为0时：按照0位置布局计算。 优先级：低于top属性。 取值范围：[0,Swiper高度-导航点区域高度]，超出该范围时，取最近的边界值。 |
| ignoreSize | boolean | 是 | 设置是否忽略导航点本身大小，默认false。 设为true时可以将导航点更靠近Swiper底部，使用方法可以参考示例9演示导航点space与bottom。 说明：数字导航点ignoreSize属性，不生效的场景如下： • 当vertical 设置为false，且bottom > 0。 • 当vertical 设置为true时： 1、bottom > 0 时。 2、bottom设为undefined。 3、isSidebarMiddle设置为false时。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| T | 返回当前导航点指示器。 |

**start12+**

start(value: LengthMetrics): T

在[RTL](内置环境变量说明.md#ZH-CN_TOPIC_0000002522240920__layoutdirection)模式下为导航点距离Swiper组件右边的距离，在[LTR](内置环境变量说明.md#ZH-CN_TOPIC_0000002522240920__layoutdirection)模式下为导航点距离Swiper组件左边的距离。

卡片能力： 从API version 12开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | LengthMetrics | 是 | 设置在RTL模式下为导航点距离Swiper组件右边的距离，在LTR模式下为导航点距离Swiper组件左边的距离。 默认值：0 单位：vp 取值范围：[0, Swiper宽度-导航点区域宽度]，超出该范围时，取最近的边界值。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| T | 返回当前导航点指示器。 |

**end12+**

end(value: LengthMetrics): T

在RTL模式下为导航点距离Swiper组件左边的距离，在LTR模式下为导航点距离Swiper组件右边的距离。

卡片能力： 从API version 12开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | LengthMetrics | 是 | 设置在RTL模式下为导航点距离Swiper组件左边的距离，在LTR模式下为导航点距离Swiper组件右边的距离。 默认值：0 单位：vp 取值范围：[0, Swiper宽度-导航点区域宽度]，超出该范围时，取最近的边界值。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| T | 返回当前导航点指示器。 |

**dot**

static dot(): DotIndicator

返回一个DotIndicator对象。

卡片能力： 从API version 10开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

返回值：

| 类型 | 说明 |
| --- | --- |
| DotIndicator | 圆点指示器。 |

**digit**

static digit(): DigitIndicator

返回一个DigitIndicator对象。

卡片能力： 从API version 10开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

返回值：

| 类型 | 说明 |
| --- | --- |
| DigitIndicator | 数字指示器。 |

**DotIndicator10+**

构造圆点指示器的样式，继承自[Indicator](#ZH-CN_TOPIC_0000002522240824__indicator10)。

卡片能力： 从API version 10开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

**constructor**

constructor()

DotIndicator的构造函数。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

-

按压导航点时，导航点会放大至1.33倍显示，因此非按压态时导航点的可见范围边界至实际范围边界存在一定距离，该距离会随着itemWidth、itemHeight、selectedItemWidth、selectedItemHeight等参数变大而变大。

-

若页面数量较多、圆点导航点超出页面时，建议使用maxDisplayCount设置导航点显示个数。

卡片能力： 从API version 10开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

**itemWidth**

itemWidth(value: Length): DotIndicator

Swiper组件圆点导航指示器的宽。

卡片能力： 从API version 10开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Length | 是 | 设置Swiper组件圆点导航指示器的宽，不支持设置百分比。 默认值：6 单位：vp 取值范围：(0, +∞) |

返回值：

| 类型 | 说明 |
| --- | --- |
| DotIndicator | 返回当前圆点指示器。 |

**itemHeight**

itemHeight(value: Length): DotIndicator

Swiper组件圆点导航指示器的高。

卡片能力： 从API version 10开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Length | 是 | 设置Swiper组件圆点导航指示器的高，不支持设置百分比。 默认值：6 单位：vp 取值范围：(0, +∞) |

返回值：

| 类型 | 说明 |
| --- | --- |
| DotIndicator | 返回当前圆点指示器。 |

**selectedItemWidth**

selectedItemWidth(value: Length): DotIndicator

选中Swiper组件圆点导航指示器的宽。

卡片能力： 从API version 10开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Length | 是 | 设置选中Swiper组件圆点导航指示器的宽，不支持设置百分比。 默认值：6 单位：vp 取值范围：(0, +∞) |

返回值：

| 类型 | 说明 |
| --- | --- |
| DotIndicator | 返回当前圆点指示器。 |

**selectedItemHeight**

selectedItemHeight(value: Length): DotIndicator

选中Swiper组件圆点导航指示器的高。

卡片能力： 从API version 10开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Length | 是 | 设置选中Swiper组件圆点导航指示器的高，不支持设置百分比。 默认值：6 单位：vp 取值范围：(0, +∞) |

返回值：

| 类型 | 说明 |
| --- | --- |
| DotIndicator | 返回当前圆点指示器。 |

**mask**

mask(value: boolean): DotIndicator

是否显示Swiper组件圆点导航指示器的蒙版样式。

卡片能力： 从API version 10开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 设置是否显示Swiper组件圆点导航指示器的蒙版样式。true为显示Swiper组件圆点导航指示器的蒙版样式，false为不显示。 默认值：false |

返回值：

| 类型 | 说明 |
| --- | --- |
| DotIndicator | 返回当前圆点指示器。 |

**color**

color(value: ResourceColor): DotIndicator

Swiper组件圆点导航指示器的颜色。

卡片能力： 从API version 10开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | ResourceColor | 是 | 设置Swiper组件圆点导航指示器的颜色。 默认值：'#1A182431'，浅灰色。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| DotIndicator | 返回当前圆点指示器。 |

**selectedColor**

selectedColor(value: ResourceColor): DotIndicator

选中Swiper组件圆点导航指示器的颜色。

卡片能力： 从API version 10开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | ResourceColor | 是 | 设置选中Swiper组件圆点导航指示器的颜色。 默认值：'#007DFF'，蓝色。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| DotIndicator | 返回当前圆点指示器。 |

**maxDisplayCount12+**

maxDisplayCount(maxDisplayCount: number): DotIndicator

圆点导航点指示器样式下，导航点显示个数最大值。

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| maxDisplayCount | number | 是 | 设置圆点导航点指示器样式下，导航点显示个数最大值，当实际导航点个数大于最大导航点个数时，会生效超长效果样式，样式如示例5所示。 默认值：这个属性没有默认值，如果设置异常值那等同于没有超长显示效果。 取值范围：[6, 9] 说明： 1、超长显示场景，目前暂时不支持交互功能（包括：手指点击拖拽、鼠标操作等）。 2、在超长显示场景下，中间页面对应的选中导航点的位置，并不是完全固定的，取决于之前的翻页操作序列。 3、当前仅支持displayCount为1的场景。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| DotIndicator | 返回当前圆点指示器。 |

**space19+**

space(space: LengthMetrics): DotIndicator

设置Swiper圆点导航点间距。

卡片能力： 从API version 19开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 19开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| space | LengthMetrics | 是 | 设置圆点导航点间距，不支持设置百分比。 默认值：PC/2in1设备上为10，其他设备为8。 单位：vp 取值范围：[0, +∞) |

返回值：

| 类型 | 说明 |
| --- | --- |
| DotIndicator | 返回当前圆点指示器。 |

**DigitIndicator10+**

构造数字指示器的样式，继承自[Indicator](#ZH-CN_TOPIC_0000002522240824__indicator10)。

卡片能力： 从API version 10开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

按组翻页时，数字导航点显示的子节点数量不包括占位节点。

数字导航点文本最大的字体缩放倍数[maxFontScale](Text.md#ZH-CN_TOPIC_0000002553360767__maxfontscale12)为2。

页码的镜像显示依据为系统的RTL状态。

**fontColor**

fontColor(value: ResourceColor): DigitIndicator

Swiper组件数字导航点的字体颜色。

卡片能力： 从API version 10开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | ResourceColor | 是 | 设置Swiper组件数字导航点的字体颜色。 默认值：'#ff182431' |

返回值：

| 类型 | 说明 |
| --- | --- |
| DigitIndicator | 返回当前数字指示器。 |

**selectedFontColor**

selectedFontColor(value: ResourceColor): DigitIndicator

选中Swiper组件数字导航点的字体颜色。

卡片能力： 从API version 10开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | ResourceColor | 是 | 设置选中Swiper组件数字导航点的字体颜色。 默认值：'#ff182431' |

返回值：

| 类型 | 说明 |
| --- | --- |
| DigitIndicator | 返回当前数字指示器。 |

**digitFont**

digitFont(value: Font): DigitIndicator

Swiper组件数字导航点的字体样式。

卡片能力： 从API version 10开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Font | 是 | 设置Swiper组件数字导航点的字体样式。 只支持Font中size和weight参数，family和style设置不生效。 默认值： { size: 14, weight: FontWeight.Normal } |

返回值：

| 类型 | 说明 |
| --- | --- |
| DigitIndicator | 返回当前数字指示器。 |

**selectedDigitFont**

selectedDigitFont(value: Font): DigitIndicator

选中Swiper组件数字导航点的字体样式。

卡片能力： 从API version 10开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Font | 是 | 设置选中Swiper组件数字导航点的字体样式。 默认值： { size: 14, weight: FontWeight.Normal } |

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

按组翻页时，数字导航点显示的子节点数量不包括占位节点。

返回值：

| 类型 | 说明 |
| --- | --- |
| DigitIndicator | 返回当前数字指示器。 |

**constructor**

constructor()

DigitIndicator的构造函数。

卡片能力： 从API version 10开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

**ArrowStyle10+对象说明**

左右箭头属性。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| showBackground | boolean | 否 | 是 | 设置箭头底板是否显示。为true时箭头底板显示，为false时箭头底板不显示。 默认值：false |
| isSidebarMiddle | boolean | 否 | 是 | 设置箭头显示位置。为true时箭头居中显示在Swiper组件两侧，为false时显示在导航点指示器两侧。 默认值：false 默认显示在导航点指示器两侧。 |
| backgroundSize | Length | 否 | 是 | 设置底板大小。 在导航点两侧显示： 默认值：24vp 在组件两侧显示： 默认值：32vp 不支持设置百分比。 |
| backgroundColor | ResourceColor | 否 | 是 | 设置底板颜色。 在导航点两侧显示： 默认值：'#00000000' 在组件两侧显示： 默认值：'#19182431' |
| arrowSize | Length | 否 | 是 | 设置箭头大小。 在导航点两侧显示时： 默认值：18vp 在组件两侧显示时： 默认值：24vp 说明： showBackground为true时，arrowSize为backgroundSize的3/4。 不支持设置百分比。 |
| arrowColor | ResourceColor | 否 | 是 | 设置箭头颜色。 默认值：'#182431' |

**SwiperAutoFill10+**

自适应属性。

卡片能力： 从API version 10开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| minSize | VP | 否 | 否 | 设置元素显示最小宽度。 默认值：0 |

**AutoPlayOptions18+对象说明**

自动播放属性。

卡片能力： 从API version 18开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 18开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| stopWhenTouched | boolean | 否 | 否 | 在按下事件中配置子组件是否立即停止播放。 设置为true时，停止播放。设置为false时，自动播放不中断。 默认值：true |

**事件**

除支持[通用事件](通用事件.md)外，还支持以下事件：

**onChange**

onChange(event: Callback<number>)

当前显示元素索引变化时触发该事件，返回值为当前显示元素的索引值。

Swiper组件结合LazyForEach使用时，不能在onChange事件里触发子页面UI的刷新。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

如果是动画引起的索引变化，回调在动画结束时触发。

卡片能力： 从API version 10开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | Callback<number> | 是 | 当前显示元素的索引。 |

**onAnimationStart9+**

onAnimationStart(event: OnSwiperAnimationStartCallback)

切换动画开始时触发该回调。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

-

调用此回调后，切换动画的逻辑将在渲染线程中执行，从而使处于空闲状态的主线程能够充分利用这段时间来加载子组件所需资源，减少后续在cachedCount范围内节点的预加载时间。最佳实践请参考[优化Swiper组件加载慢丢帧问题-提前加载数据](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-swiper_high_performance_development_guide#section8783121513246)。

-

当翻页动画时长为0时，只有以下场景会触发该回调：滑动翻页、自动轮播、调用SwiperController.showNext()和SwiperController.showPrevious()接口以及手指点击导航点翻页。

卡片能力： 从API version 10开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | OnSwiperAnimationStartCallback | 是 | 切换动画开始时触发的回调。 |

**onAnimationEnd9+**

onAnimationEnd(event: OnSwiperAnimationEndCallback)

切换动画结束时触发该回调。

当Swiper切换动效结束时触发，包括动画过程中手势中断，通过SwiperController调用finishAnimation。

卡片能力： 从API version 10开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | OnSwiperAnimationEndCallback | 是 | 切换动画结束时触发的回调。 |

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

- 当翻页动画时长为0时，只有以下场景会触发该回调：滑动翻页、自动轮播、调用SwiperController.showNext()和SwiperController.showPrevious()接口以及手指点击导航点翻页。

**onGestureSwipe10+**

onGestureSwipe(event: OnSwiperGestureSwipeCallback)

在页面跟手滑动过程中，逐帧触发该回调。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | OnSwiperGestureSwipeCallback | 是 | 在页面跟手滑动过程中，逐帧触发的回调。onGestureSwipe回调触发时机在onTouch之后，如果需要在离手后执行操作建议使用onAnimationStart。 |

**customContentTransition12+**

customContentTransition(transition: SwiperContentAnimatedTransition)

自定义Swiper页面切换动画。在页面跟手滑动和离手后执行切换动画的过程中，会对视窗内所有页面逐帧触发回调，开发者可以在回调中设置透明度、缩放比例、位移等属性来自定义切换动画。

使用说明：

1、循环场景下，设置prevMargin和nextMargin属性，使得Swiper前后端显示同一页面时，该接口不生效。

2、在页面跟手滑动和离手后执行切换动画的过程中，会对视窗内所有页面逐帧触发[SwiperContentTransitionProxy](#ZH-CN_TOPIC_0000002522240824__swipercontenttransitionproxy12)回调。例如，当视窗内有下标为0、1的两个页面时，会每帧触发两次index值分别为0和1的回调。

3、设置displayCount属性的swipeByGroup参数为true时，若同组中至少有一个页面在视窗内时，则会对同组中所有页面触发回调，若同组所有页面均不在视窗内时，则会一起下渲染树。

4、在页面跟手滑动和离手后执行切换动画的过程中，默认动画（页面滑动）依然会发生，若希望页面不滑动，可以设置主轴方向上负的位移（translate属性）来抵消页面滑动。例如：当displayCount属性值为2，视窗内有下标为0、1的两个页面时，页面水平滑动过程中，可以逐帧设置第0页的translate属性在x轴上的值为-position * mainAxisLength来抵消第0页的位移，设置第1页的translate属性在x轴上的值为-(position - 1) * mainAxisLength来抵消第1页的位移。

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| transition | SwiperContentAnimatedTransition | 是 | Swiper自定义切换动画相关信息。 |

**onContentDidScroll12+**

onContentDidScroll(handler: ContentDidScrollCallback)

监听Swiper页面滑动事件。

使用说明：

1、循环场景下，设置prevMargin和nextMargin属性，使得Swiper前后端显示同一页面时，该接口不生效。

2、在页面滑动过程中，会对视窗内所有页面逐帧触发[ContentDidScrollCallback](#ZH-CN_TOPIC_0000002522240824__contentdidscrollcallback12)回调。例如，当视窗内有下标为0、1的两个页面时，会每帧触发两次index值分别为0和1的回调。

3、设置displayCount属性的swipeByGroup参数为true时，若同组中至少有一个页面在视窗内时，则会对同组中所有页面触发回调。

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| handler | ContentDidScrollCallback | 是 | Swiper滑动时触发的回调。 |

**onSelected18+**

onSelected(event: Callback<number>)

当选中元素改变时触发该回调，返回值为当前选中的元素的索引值。

卡片能力： 从API version 18开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 18开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | Callback<number> | 是 | 当前选中元素的索引。 |

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

onSelected回调中不可修改swiper的index属性，不可调用SwiperController.changeIndex()、SwiperController.showNext()和SwiperController.showPrevious()方法。

**onUnselected18+**

onUnselected(event: Callback<number>)

当选中元素改变时触发该回调，返回值为将要隐藏的元素的索引值。

卡片能力： 从API version 18开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 18开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | Callback<number> | 是 | 将要隐藏元素的索引。 |

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

onUnselected回调中不可修改swiper的index属性，不可调用SwiperController.changeIndex()、SwiperController.showNext()和SwiperController.showPrevious()方法。

**onContentWillScroll15+**

onContentWillScroll(handler: ContentWillScrollCallback)

Swiper滑动行为拦截事件，在滑动前触发。Swiper会依据该事件的返回值来决定是否允许此次滑动行为。若返回true，表示允许此次滑动行为，Swiper页面将跟随滑动。若返回false，表示不允许此次滑动，页面将保持静止。

1.

触发该事件的场景仅限于手势操作，具体包括手指滑动、滚动鼠标滚轮以及使用键盘方向键进行焦点移动。

1.

在手指滑动的过程中，每帧都将触发该事件，系统会依据事件的返回值判断是否对每帧的滑动做出响应。

1.

对于滚动鼠标滚轮和使用键盘方向键进行焦点移动的场景，每次翻页操作都会触发一次该事件，翻页是否被允许将根据事件的返回值来决定。

卡片能力： 从API version 15开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 15开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| handler | ContentWillScrollCallback | 是 | Swiper滑动时触发的回调。 |

**onScrollStateChanged20+**

onScrollStateChanged(event: Callback<ScrollState>)

Swiper滑动状态变化事件回调，在跟手滑动、离手动画、停止三种滑动状态变化时触发，返回值为当前滑动状态。

卡片能力： 从API version 20开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 20开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | Callback<ScrollState> | 是 | 滑动状态变化的回调。 |

**OnSwiperAnimationStartCallback18+**

type OnSwiperAnimationStartCallback = (index: number, targetIndex: number, extraInfo: SwiperAnimationEvent) => void

切换动画开始时触发的回调。

卡片能力： 从API version 18开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 18开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 当前显示元素的索引。多列Swiper时，index为最左侧组件的索引。 |
| targetIndex10+ | number | 是 | 切换动画目标元素的索引。 |
| extraInfo10+ | SwiperAnimationEvent | 是 | 动画相关信息，包括主轴方向上当前显示元素和目标元素相对Swiper起始位置的位移，以及离手速度。 |

**OnSwiperAnimationEndCallback18+**

type OnSwiperAnimationEndCallback = (index: number, extraInfo: SwiperAnimationEvent) => void

切换动画结束时触发的回调。

卡片能力： 从API version 18开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 18开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 当前显示元素的索引。多列Swiper时，index为最左侧组件的索引。 |
| extraInfo10+ | SwiperAnimationEvent | 是 | 动画相关信息，只返回主轴方向上当前显示元素相对于Swiper起始位置的位移。 |

**OnSwiperGestureSwipeCallback18+**

type OnSwiperGestureSwipeCallback = (index: number, extraInfo: SwiperAnimationEvent) => void

在页面跟手滑动过程中，逐帧触发的回调。

元服务API： 从API version 18开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 当前显示元素的索引。多列Swiper时，index为最左侧组件的索引。 |
| extraInfo | SwiperAnimationEvent | 是 | 动画相关信息，只返回主轴方向上当前显示元素相对于Swiper起始位置的位移。 |

**ContentDidScrollCallback12+**

type ContentDidScrollCallback = (selectedIndex: number, index: number, position: number, mainAxisLength: number) => void

Swiper滑动时触发的回调，参数可参考[SwiperContentTransitionProxy](#ZH-CN_TOPIC_0000002522240824__swipercontenttransitionproxy12)中的说明。

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| selectedIndex | number | 是 | 当前选中页面的索引。 |
| index | number | 是 | 视窗内页面的索引。 |
| position | number | 是 | index页面相对于Swiper主轴起始位置（selectedIndex对应页面的起始位置）的移动比例。 |
| mainAxisLength | number | 是 | index对应页面在主轴方向上的长度，单位vp。 |

**ContentWillScrollCallback15+**

type ContentWillScrollCallback = (result: SwiperContentWillScrollResult) => boolean

Swiper即将滑动前触发的回调，返回值表示是否允许此次滑动。

卡片能力： 从API version 15开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 15开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| result | SwiperContentWillScrollResult | 是 | 即将滑动的相关信息，主要包括：当前页面对应的index、滑动方向上即将显示的页面index和此次滑动的位移。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| boolean | Swiper是否响应本次滑动，true表示响应，false表示不响应。 |

**SwiperContentWillScrollResult15+对象说明**

滑动的相关信息，主要包括：当前页面对应的index、滑动方向上即将显示的页面index和此次滑动的位移。

卡片能力： 从API version 15开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 15开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| currentIndex | number | 否 | 否 | 当前页面对应的index。在一次跟手滑动过程中，只要手指未离开屏幕，该值将保持不变，即使该页面已完全移出视窗，如在涉及多个页面的场景中。 |
| comingIndex | number | 否 | 否 | 滑动方向上即将显示的页面index。 |
| offset | number | 否 | 否 | 此次滑动的位移，带有符号，正负分别指示不同的翻页方向。正数表示从index=1向index=0翻页，负数表示从index=0向index=1翻页。 在手指滑动的场景中，该值为滑动事件中每帧传递下来的偏移量。在滚动鼠标滚轮和使用键盘方向键导航的场景中，该值代表即将翻页的距离。 |

**SwiperAnimationEvent10+对象说明**

Swiper组件动画相关信息集合。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| currentOffset | number | 否 | 否 | Swiper当前显示元素在主轴方向上，相对于Swiper起始位置的位移。单位VP，默认值为0。 |
| targetOffset | number | 否 | 否 | Swiper动画目标元素在主轴方向上，相对于Swiper起始位置的位移。单位VP，默认值为0。 |
| velocity | number | 否 | 否 | Swiper离手动画开始时的离手速度。单位VP/S，默认值为0。 |

**SwiperContentAnimatedTransition12+**

Swiper自定义切换动画相关信息。

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| timeout | number | 否 | 是 | Swiper自定义切换动画超时时间。从页面执行默认动画（页面滑动）至移出视窗外的第一帧开始计时，如果到达该时间后，开发者仍未调用SwiperContentTransitionProxy的finishTransition接口通知Swiper组件此页面的自定义动画已结束，那么组件就会认为此页面的自定义动画已结束，立即将该页面节点下渲染树。单位ms，默认值为0。 |
| transition | Callback<SwiperContentTransitionProxy> | 否 | 否 | 自定义切换动画具体内容。 |

**SwiperContentTransitionProxy12+**

Swiper自定义切换动画执行过程中，返回给开发者的proxy对象。开发者可通过该对象获取自定义动画视窗内的页面信息，同时，也可以通过调用该对象的finishTransition接口通知Swiper组件页面自定义动画已结束。

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

**属性**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| selectedIndex | number | 否 | 否 | 当前选中页面的索引。 |
| index | number | 否 | 否 | 视窗内页面的索引。 |
| position | number | 否 | 否 | index页面相对于Swiper主轴起始位置（selectedIndex对应页面的起始位置）的移动比例。 |
| mainAxisLength | number | 否 | 否 | index对应页面在主轴方向上的长度，单位vp。 |

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

-

例如，当前选中的子组件的索引为0，从第0页切换到第1页的动画过程中，每帧都会对视窗内所有页面触发回调，当视窗内有第0页和第1页两页时，每帧会触发两次回调。其中，第一次回调的selectedIndex为0、index为0、position为当前帧第0页相对于动画开始前第0页的移动比例，mainAxisLength为主轴方向上第0页的长度。第二次回调的selectedIndex仍为0、index为1、position为当前帧第1页相对于动画开始前第0页的移动比例，mainAxisLength为主轴方向上第1页的长度。

-

若动画曲线为弹簧插值曲线，从第0页切换到第1页的动画过程中，可能会因为离手时的位置和速度，先过滑到第2页，再回弹到第1页，该过程中每帧会对视窗内第1页和第2页触发回调。

**finishTransition12+**

finishTransition(): void

通知Swiper组件，此页面的自定义动画已结束。

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

**IndicatorStyle(deprecated)对象说明**

导航点样式。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

从API version 8开始支持，从API version 10开始废弃，建议使用[indicator](#ZH-CN_TOPIC_0000002522240824__indicator10)替代。

系统能力： SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| left | Length | 否 | 是 | 设置导航点左侧相对于Swiper的位置。 未设置left和right时，进行自适应大小布局，按照指示器本身大小和Swiper的大小在主轴方向上进行居中对齐 设置为0时：按照0位置布局计算 优先级：高于right属性 取值范围：[0,Swiper宽度-导航点区域宽度]，超出该范围时，取最近的边界值。 |
| top | Length | 否 | 是 | 设置导航点顶部相对于Swiper的位置。 未设置top和bottom时，进行自适应大小布局，按照指示器本身大小和Swiper的大小，在交叉轴方向上，位于底部，效果与设置bottom=0一致 设置为0时：按照0位置布局计算 优先级：高于bottom属性 取值范围：[0,Swiper高度-导航点区域高度]，超出该范围时，取最近的边界值。 |
| right | Length | 否 | 是 | 设置导航点右侧相对于Swiper的位置。 未设置left和right时，进行自适应大小布局，按照指示器本身大小和Swiper的大小在主轴方向上进行居中对齐 设置为0时：按照0位置布局计算 优先级：低于left属性 取值范围：[0,Swiper宽度-导航点区域宽度]，超出该范围时，取最近的边界值。 |
| bottom | Length | 否 | 是 | 设置导航点底部相对于Swiper的位置。 未设置top和bottom时，进行自适应大小布局，按照指示器本身大小和Swiper的大小，在交叉轴方向上，位于底部，效果与设置bottom=0一致 设置为0时：按照0位置布局计算 优先级：低于top属性 取值范围：[0,Swiper高度-导航点区域高度]，超出该范围时，取最近的边界值。 |
| size | Length | 否 | 是 | 设置导航点的直径，不支持设置百分比。 默认值：6vp |
| mask | boolean | 否 | 是 | 设置是否显示导航点蒙层样式。 true：显示导航点蒙层样式，false：不显示导航点蒙层样式。 默认值：false |
| color | ResourceColor | 否 | 是 | 设置导航点的颜色。 默认值：'#1A182431'，浅灰色。 |
| selectedColor | ResourceColor | 否 | 是 | 设置选中的导航点的颜色。 默认值：'#007DFF'，蓝色。 |

**示例**

**示例1（设置导航点交互及翻页动效）**

该示例通过[changeIndex](#ZH-CN_TOPIC_0000002522240824__changeindex15)接口设置[SwiperAnimationMode](#ZH-CN_TOPIC_0000002522240824__swiperanimationmode15枚举说明)动效模式，实现了Swiper组件翻页至指定页面。

```ets
// xxx.ets
class MyDataSource implements IDataSource {
  private list: number[] = [];

  constructor(list: number[]) {
    this.list = list;
  }

  totalCount(): number {
    return this.list.length;
  }

  getData(index: number): number {
    return this.list[index];
  }

  registerDataChangeListener(listener: DataChangeListener): void {
  }

  unregisterDataChangeListener() {
  }

@Entry
@Component
struct SwiperExample {
  private swiperController: SwiperController = new SwiperController();
  private data: MyDataSource = new MyDataSource([]);

  aboutToAppear(): void {
    let list: number[] = [];
    for (let i = 1; i <= 10; i++) {
      list.push(i);
    }
    this.data = new MyDataSource(list);
  }

  build() {
    Column({ space: 5 }) {
      Swiper(this.swiperController) {
        LazyForEach(this.data, (item: string) => {
          Text(item.toString())
            .width('90%')
            .height(160)
            .backgroundColor(0xAFEEEE)
            .textAlign(TextAlign.Center)
            .fontSize(30)
        }, (item: string) => item)
      }
      .cachedCount(2)
      .index(1)
      .autoPlay(true)
      .interval(4000)
      .loop(true)
      .indicatorInteractive(true)
      .duration(1000)
      .itemSpace(5)
      .prevMargin(35)
      .nextMargin(35)
      .indicator( // 设置圆点导航点样式
        new DotIndicator()
          .itemWidth(15)
          .itemHeight(15)
          .selectedItemWidth(15)
          .selectedItemHeight(15)
          .color(Color.Gray)
          .selectedColor(Color.Blue))
      .displayArrow({ // 设置导航点箭头样式
        showBackground: true,
        isSidebarMiddle: true,
        backgroundSize: 24,
        backgroundColor: Color.White,
        arrowSize: 18,
        arrowColor: Color.Blue
      }, false)
      .curve(Curve.Linear)
      .onChange((index: number) => {
        console.info(index.toString());
      })
      .onScrollStateChanged((event: ScrollState) => {
        console.info("event: " + event);
      })
      .onGestureSwipe((index: number, extraInfo: SwiperAnimationEvent) => {
        console.info("index: " + index);
        console.info("current offset: " + extraInfo.currentOffset);
      })
      .onAnimationStart((index: number, targetIndex: number, extraInfo: SwiperAnimationEvent) => {
        console.info("index: " + index);
        console.info("targetIndex: " + targetIndex);
        console.info("current offset: " + extraInfo.currentOffset);
        console.info("target offset: " + extraInfo.targetOffset);
        console.info("velocity: " + extraInfo.velocity);
      })
      .onAnimationEnd((index: number, extraInfo: SwiperAnimationEvent) => {
        console.info("index: " + index);
        console.info("current offset: " + extraInfo.currentOffset);
      })

      Row({ space: 12 }) {
        Button('showPrevious')
          .onClick(() => {
            this.swiperController.showPrevious();
          })
        Button('showNext')
          .onClick(() => {
            this.swiperController.showNext();
          })
      }.margin(5)
      Row({ space: 5 }) {
        Button('FAST 0')
          .onClick(() => {
            // 控制器：跳转到索引0，使用快速动画模式
            this.swiperController.changeIndex(0, SwiperAnimationMode.FAST_ANIMATION);
          })
        Button('FAST 3')
          .onClick(() => {
            // 控制器：跳转到索引3，使用快速动画模式
            this.swiperController.changeIndex(3, SwiperAnimationMode.FAST_ANIMATION);
          })
        Button('FAST ' + 9)
          .onClick(() => {
            // 控制器：跳转到索引9，使用快速动画模式
            this.swiperController.changeIndex(9, SwiperAnimationMode.FAST_ANIMATION);
          })
      }.margin(5)
    }.width('100%')
    .margin({ top: 5 })
  }
```

![image](public_sys-resources/zh-cn_image_0000002522244902.webp)

**示例2（设置数字指示器）**

该示例通过[DigitIndicator](#ZH-CN_TOPIC_0000002522240824__digitindicator10)接口，实现了数字指示器的效果和功能。

```ets
// xxx.ets
class MyDataSource implements IDataSource {
  private list: number[] = [];

  constructor(list: number[]) {
    this.list = list;
  }

  totalCount(): number {
    return this.list.length;
  }

  getData(index: number): number {
    return this.list[index];
  }

  registerDataChangeListener(listener: DataChangeListener): void {
  }

  unregisterDataChangeListener() {
  }

@Entry
@Component
struct SwiperExample {
  private swiperController: SwiperController = new SwiperController();
  private data: MyDataSource = new MyDataSource([]);

  aboutToAppear(): void {
    let list: number[] = [];
    for (let i = 1; i <= 10; i++) {
      list.push(i);
    }
    this.data = new MyDataSource(list);
  }

  build() {
    Column({ space: 5 }) {
      Swiper(this.swiperController) {
        LazyForEach(this.data, (item: string) => {
          Text(item.toString())
            .width('90%')
            .height(160)
            .backgroundColor(0xAFEEEE)
            .textAlign(TextAlign.Center)
            .fontSize(30)
        }, (item: string) => item)
      }
      .cachedCount(2)
      .index(1)
      .autoPlay(true)
      .interval(4000)
      .indicator(Indicator.digit() // 设置数字导航点样式
        .top(200)
        .fontColor(Color.Gray)
        .selectedFontColor(Color.Gray)
        .digitFont({ size: 20, weight: FontWeight.Bold })
        .selectedDigitFont({ size: 20, weight: FontWeight.Normal }))
      .loop(true)
      .duration(1000)
      .itemSpace(0)
      .displayArrow(true, false)

      Row({ space: 12 }) {
        Button('showNext')
          .onClick(() => {
            this.swiperController.showNext();
          })
        Button('showPrevious')
          .onClick(() => {
            this.swiperController.showPrevious();
          })
      }.margin(5)
    }.width('100%')
    .margin({ top: 5 })
  }
```

![image](public_sys-resources/zh-cn_image_0000002553204863.webp)

**示例3（设置按组翻页）**

该示例通过[displayCount](#ZH-CN_TOPIC_0000002522240824__displaycount8)属性实现了按组翻页效果。

```ets
// xxx.ets
class MyDataSource implements IDataSource {
  private list: number[] = [];

  constructor(list: number[]) {
    this.list = list;
  }

  totalCount(): number {
    return this.list.length;
  }

  getData(index: number): number {
    return this.list[index];
  }

  registerDataChangeListener(listener: DataChangeListener): void {
  }

  unregisterDataChangeListener() {
  }

@Entry
@Component
struct SwiperExample {
  private swiperController: SwiperController = new SwiperController();
  private data: MyDataSource = new MyDataSource([]);

  aboutToAppear(): void {
    let list: number[] = [];
    for (let i = 1; i <= 10; i++) {
      list.push(i);
    }
    this.data = new MyDataSource(list);
  }

  build() {
    Column({ space: 5 }) {
      Swiper(this.swiperController) {
        LazyForEach(this.data, (item: string) => {
          Text(item.toString())
            .width('90%')
            .height(160)
            .backgroundColor(0xAFEEEE)
            .textAlign(TextAlign.Center)
            .fontSize(30)
        }, (item: string) => item)
      }
      .displayCount(3, true) // 开启按组翻页：每页显示3个轮播项，且翻页时整组切换
      .autoPlay(true)
      .interval(4000)
      .loop(true)
      .duration(1000)
      .itemSpace(10)
      .indicator( // 设置圆点导航点样式
        new DotIndicator()
          .itemWidth(15)
          .itemHeight(15)
          .selectedItemWidth(15)
          .selectedItemHeight(15)
          .color(Color.Gray)
          .selectedColor(Color.Blue))

      Row({ space: 12 }) {
        Button('showNext')
          .onClick(() => {
            this.swiperController.showNext();
          })
        Button('showPrevious')
          .onClick(() => {
            this.swiperController.showPrevious();
          })
      }.margin(5)
    }.width('100%')
    .margin({ top: 5 })
  }
```

![image](public_sys-resources/zh-cn_image_0000002522084910.webp)

**示例4（设置自定义页面切换动画）**

该示例通过[customContentTransition](#ZH-CN_TOPIC_0000002522240824__customcontenttransition12)接口，实现了自定义Swiper页面按组翻页动画效果。

```ets
// EntryAbility.ets
import { Configuration, UIAbility } from '@kit.AbilityKit';
import { i18n } from '@kit.LocalizationKit';
import { CommonUtil } from '../common/CommonUtil';

export default class EntryAbility extends UIAbility {
  onConfigurationUpdate(newConfig: Configuration): void {
    // 监听系统配置变化
    if (newConfig.language) {
      CommonUtil.setIsRTL(i18n.isRTL(newConfig.language));
    }
```

```ets
// CommonUtil.ets
export class CommonUtil {
  private static isRTL: boolean = false;

  public static setIsRTL(isRTL: boolean): void {
    CommonUtil.isRTL = isRTL;
  }

  public static getIsRTL(): boolean {
    return CommonUtil.isRTL;
  }
```

```ets
// xxx.ets
import { CommonUtil } from '../common/CommonUtil';

@Entry
@Component
struct SwiperCustomAnimationExample {
  private DISPLAY_COUNT: number = 2;
  private MIN_SCALE: number = 0.75;

  @State backgroundColors: Color[] = [Color.Green, Color.Blue, Color.Yellow, Color.Pink, Color.Gray, Color.Orange];
  @State opacityList: number[] = [];
  @State scaleList: number[] = [];
  @State translateList: number[] = [];
  @State zIndexList: number[] = [];

  aboutToAppear(): void {
    for (let i = 0; i < this.backgroundColors.length; i++) {
      this.opacityList.push(1.0);
      this.scaleList.push(1.0);
      this.translateList.push(0.0);
      this.zIndexList.push(0);
    }

  build() {
    Column() {
      Swiper() {
        ForEach(this.backgroundColors, (backgroundColor: Color, index: number) => {
          Text(index.toString()).width('100%').height('100%').fontSize(50).textAlign(TextAlign.Center)
            .backgroundColor(backgroundColor)
            // 自定义动画变化透明度、缩放页面、抵消系统默认位移、渲染层级等
            .opacity(this.opacityList[index])
            .scale({ x: this.scaleList[index], y: this.scaleList[index] })
            .translate({ x: this.translateList[index] })
            .zIndex(this.zIndexList[index])
        })
      }
      .height(300)
      .indicator(false)
      .displayCount(this.DISPLAY_COUNT, true)
      .customContentTransition({
        // 页面移除视窗时超时1000ms下渲染树
        timeout: 1000,
        // 对视窗内所有页面逐帧回调transition，在回调中修改opacity、scale、translate、zIndex等属性值，实现自定义动画
        transition: (proxy: SwiperContentTransitionProxy) => {
          if (!CommonUtil.getIsRTL()) {
            if (proxy.position <= proxy.index % this.DISPLAY_COUNT || proxy.position >= this.DISPLAY_COUNT + proxy.index % this.DISPLAY_COUNT) {
              // 同组页面往左滑或往右完全滑出视窗外时，重置属性值
              this.opacityList[proxy.index] = 1.0;
              this.scaleList[proxy.index] = 1.0;
              this.translateList[proxy.index] = 0.0;
              this.zIndexList[proxy.index] = 0;
            } else {
              // 同组页面往右滑且未滑出视窗外时，对同组中左右两个页面，逐帧根据position修改属性值，实现两个页面往Swiper中间靠拢并透明缩放的自定义切换动画
              if (proxy.index % this.DISPLAY_COUNT === 0) {
                this.opacityList[proxy.index] = 1 - proxy.position / this.DISPLAY_COUNT;
                this.scaleList[proxy.index] = this.MIN_SCALE + (1 - this.MIN_SCALE) * (1 - proxy.position / this.DISPLAY_COUNT);
                this.translateList[proxy.index] = -proxy.position * proxy.mainAxisLength + (1 - this.scaleList[proxy.index]) * proxy.mainAxisLength / 2.0;
              } else {
                this.opacityList[proxy.index] = 1 - (proxy.position - 1) / this.DISPLAY_COUNT;
                this.scaleList[proxy.index] = this.MIN_SCALE + (1 - this.MIN_SCALE) * (1 - (proxy.position - 1) / this.DISPLAY_COUNT);
                this.translateList[proxy.index] = -(proxy.position - 1) * proxy.mainAxisLength - (1 - this.scaleList[proxy.index]) * proxy.mainAxisLength / 2.0;
              }
              this.zIndexList[proxy.index] = -1;
            }
          } else {
            // 适配镜像
            if (proxy.position >= -proxy.index % this.DISPLAY_COUNT || proxy.position <= -this.DISPLAY_COUNT - proxy.index % this.DISPLAY_COUNT) {
              // 同组页面往右滑或往左完全滑出视窗外时，重置属性值
              this.opacityList[proxy.index] = 1.0;
              this.scaleList[proxy.index] = 1.0;
              this.translateList[proxy.index] = 0.0;
              this.zIndexList[proxy.index] = 0;
            } else {
              // 同组页面往左滑且未滑出视窗外时，对同组中左右两个页面，逐帧根据position修改属性值，实现两个页面往Swiper中间靠拢并透明缩放的自定义切换动画
              if (proxy.index % this.DISPLAY_COUNT === 0) {
                this.opacityList[proxy.index] = 1 + proxy.position / this.DISPLAY_COUNT;
                this.scaleList[proxy.index] = this.MIN_SCALE + (1 - this.MIN_SCALE) * (1 + proxy.position / this.DISPLAY_COUNT);
                this.translateList[proxy.index] = -proxy.position * proxy.mainAxisLength - (1 - this.scaleList[proxy.index]) * proxy.mainAxisLength / 2.0;
              } else {
                this.opacityList[proxy.index] = 1 + (proxy.position + 1) / this.DISPLAY_COUNT;
                this.scaleList[proxy.index] = this.MIN_SCALE + (1 - this.MIN_SCALE) * (1 + (proxy.position + 1) / this.DISPLAY_COUNT);
                this.translateList[proxy.index] = -(proxy.position + 1) * proxy.mainAxisLength + (1 - this.scaleList[proxy.index]) * proxy.mainAxisLength / 2.0;
              }
              this.zIndexList[proxy.index] = -1;
            }
      })
      .onContentDidScroll((selectedIndex: number, index: number, position: number, mainAxisLength: number) => {
        // 监听Swiper页面滑动事件，在该回调中可以实现自定义导航点切换动画等
        console.info("onContentDidScroll selectedIndex: " + selectedIndex + ", index: " + index + ", position: " + position + ", mainAxisLength: " + mainAxisLength);
      })
    }.width('100%')
  }
```

![image](public_sys-resources/zh-cn_image_0000002553364825.webp)

**示例5（设置圆点导航点超长显示）**

该示例通过DotIndicator接口的[maxDisplayCount](#ZH-CN_TOPIC_0000002522240824__maxdisplaycount12)属性，实现了圆点导航点超长显示动画效果。

```ets
class MyDataSource implements IDataSource {
  private list: number[] = [];

  constructor(list: number[]) {
    this.list = list;
  }

  totalCount(): number {
    return this.list.length;
  }

  getData(index: number): number {
    return this.list[index];
  }

  registerDataChangeListener(listener: DataChangeListener): void {
  }

  unregisterDataChangeListener() {
  }

@Entry
@Component
struct Index {
  private swiperController: SwiperController = new SwiperController();
  private data: MyDataSource = new MyDataSource([]);

  aboutToAppear(): void {
    let list: number[] = [];
    for (let i = 1; i <= 15; i++) {
      list.push(i);
    }
    this.data = new MyDataSource(list);
  }

  build() {
    Column({ space: 5 }) {
      Swiper(this.swiperController) {
        LazyForEach(this.data, (item: string) => {
          Text(item.toString())
            .width('90%')
            .height(160)
            .backgroundColor(0xAFEEEE)
            .textAlign(TextAlign.Center)
            .fontSize(30)
        }, (item: string) => item)
      }
      .cachedCount(2)
      .index(5)
      .autoPlay(true)
      .interval(4000)
      .loop(true)
      .duration(1000)
      .itemSpace(0)
      .indicator( // 设置圆点导航点样式
        new DotIndicator()
          .itemWidth(8)
          .itemHeight(8)
          .selectedItemWidth(16)
          .selectedItemHeight(8)
          .color(Color.Gray)
          .selectedColor(Color.Blue)
          .maxDisplayCount(9)) // 设置导航点最大显示数量为9个
      .displayArrow({ // 设置导航点箭头样式
        showBackground: true,
        isSidebarMiddle: true,
        backgroundSize: 24,
        backgroundColor: Color.White,
        arrowSize: 18,
        arrowColor: Color.Blue
      }, false)
      .curve(Curve.Linear)
      Row({ space: 12 }) {
        Button('showNext')
          .onClick(() => {
            this.swiperController.showNext();
          })
        Button('showPrevious')
          .onClick(() => {
            this.swiperController.showPrevious();
          })
      }.margin(5)
    }.width('100%')
    .margin({ top: 5 })
  }
```

![image](public_sys-resources/zh-cn_image_0000002522244904.webp)

**示例6（预加载子节点）**

该示例通过[preloadItems](#ZH-CN_TOPIC_0000002522240824__preloaditems18)接口实现了预加载指定子节点。

```ets
// xxx.ets
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct SwiperPreloadItems {
  @State currentIndex: number = 1;
  private swiperController: SwiperController = new SwiperController();
  @State arr: string[] = ["0", "1", "2", "3", "4", "5"];

  build() {
    Column() {
      Swiper(this.swiperController) {
        ForEach(this.arr, (item: string) => {
          MyComponent({ txt: item })
        })
      }
      .cachedCount(1, true)
      .width("70%")
      .height("50%")

      Button('preload items: [2, 3]')
        .margin(5)
        .onClick(() => {
          // 预加载index=2和index=3的子节点
          try {
            this.swiperController.preloadItems([2, 3])
              .then(() => {
                console.info('preloadItems [2, 3] success.');
              })
              .catch((error: BusinessError) => {
                console.error('preloadItems [2, 3] failed, error code: ' + error.code + ', error message: ' + error.message);
              })
          } catch (error) {
            console.error('preloadItems [2, 3] failed, error code: ' + error.code + ', error message: ' + error.message);
          }

        })
    }
    .width("100%")
    .margin(5)
  }

@Component
struct MyComponent {
  private txt: string = "";

  aboutToAppear(): void {
    console.info('aboutToAppear txt:' + this.txt);
  }

  aboutToDisappear(): void {
    console.info('aboutToDisappear txt:' + this.txt);
  }

  build() {
    Text(this.txt)
      .textAlign(TextAlign.Center)
      .width('100%')
      .height('100%')
      .backgroundColor(0xAFEEEE)
  }
```

**示例7（实现Tabs与Swiper联动）**

该示例通过[onSelected](#ZH-CN_TOPIC_0000002522240824__onselected18)接口，实现了[Tabs](Tabs.md)与Swiper联动切换。

```ets
// xxx.ets
class MyDataSource implements IDataSource {
  private list: number[] = [];

  constructor(list: number[]) {
    this.list = list;
  }

  totalCount(): number {
    return this.list.length;
  }

  getData(index: number): number {
    return this.list[index];
  }

  registerDataChangeListener(listener: DataChangeListener): void {
  }

  unregisterDataChangeListener() {
  }

@Entry
@Component
struct TabsSwiperExample {
  @State fontColor: string = '#182431';
  @State selectedFontColor: string = '#007DFF';
  @State currentIndex: number = 0;
  private list: number[] = [];
  private tabsController: TabsController = new TabsController();
  private swiperController: SwiperController = new SwiperController();
  private swiperData: MyDataSource = new MyDataSource([]);

  aboutToAppear(): void {
    for (let i = 0; i <= 9; i++) {
      this.list.push(i);
    }
    this.swiperData = new MyDataSource(this.list);
  }

  @Builder tabBuilder(index: number, name: string) {
    Column() {
      Text(name)
        .fontColor(this.currentIndex === index ? this.selectedFontColor : this.fontColor)
        .fontSize(16)
        .fontWeight(this.currentIndex === index ? 500 : 400)
        .lineHeight(22)
        .margin({ top: 17, bottom: 7 })
      Divider()
        .strokeWidth(2)
        .color('#007DFF')
        .opacity(this.currentIndex === index ? 1 : 0)
    }.width('20%')
  }

  build() {
    Column() {
      Tabs({ barPosition: BarPosition.Start, controller: this.tabsController }) {
        ForEach(this.list, (index: number) =>{
          TabContent().tabBar(this.tabBuilder(index, '页签 ' + this.list[index]))
        })
      }
      .onTabBarClick((index: number) => {
        this.currentIndex = index;
        this.swiperController.changeIndex(index, true);
      })
      .barMode(BarMode.Scrollable)
      .backgroundColor('#F1F3F5')
      .height(56)
      .width('100%')

      Swiper(this.swiperController) {
        LazyForEach(this.swiperData, (item: string) => {
          Text(item.toString())
            .onAppear(()=>{
              console.info('onAppear ' + item.toString());
            })
            .onDisAppear(()=>{
              console.info('onDisAppear ' + item.toString());
            })
            .width('100%')
            .height('40%')
            .backgroundColor(0xAFEEEE)
            .textAlign(TextAlign.Center)
            .fontSize(30)
        }, (item: string) => item)
      }
      .loop(false)
      // 选中/切换轮播项时触发
      .onSelected((index: number) => {
        console.info("onSelected:" + index);
        // 同步选中索引到currentIndex（更新页签选中态）
        this.currentIndex = index;
        // 控制Tabs切换到对应索引页签
        this.tabsController.changeIndex(index);
      })
    }
```

![image](public_sys-resources/zh-cn_image_0000002553204865.webp)

**示例8（滑动行为拦截事件）**

该示例通过[onContentWillScroll](#ZH-CN_TOPIC_0000002522240824__oncontentwillscroll15)事件实现了单方向的滑动翻页，即只能滑动向前翻页，滑动向后翻页的行为会被拦截。

```ets
// xxx.ets
class MyDataSource implements IDataSource {
  private list: number[] = [];

  constructor(list: number[]) {
    this.list = list;
  }

  totalCount(): number {
    return this.list.length;
  }

  getData(index: number): number {
    return this.list[index];
  }

  registerDataChangeListener(listener: DataChangeListener): void {
  }

  unregisterDataChangeListener() {
  }

@Entry
@Component
struct SwiperExample {
  private swiperController: SwiperController = new SwiperController();
  private data: MyDataSource = new MyDataSource([]);
  private currentIndex: number = 4;

  aboutToAppear(): void {
    let list: number[] = [];
    for (let i = 1; i <= 10; i++) {
      list.push(i);
    }
    this.data = new MyDataSource(list);
  }

  build() {
    Column({ space: 5 }) {
      Swiper(this.swiperController) {
        LazyForEach(this.data, (item: string) => {
          Text(item.toString())
            .width('90%')
            .height(160)
            .backgroundColor(0xAFEEEE)
            .textAlign(TextAlign.Center)
            .fontSize(30)
        }, (item: string) => item)
      }
      .index(this.currentIndex)
      .loop(false)
      .onChange((index: number) => {
        this.currentIndex = index;
      })
      .onContentWillScroll((result: SwiperContentWillScrollResult) => {
        // result.comingIndex：即将要滑动到的目标索引
        // 拦截逻辑：
        // 1. 若目标索引 > 当前索引：返回false，拦截该滑动行为
        // 2. 若目标索引 < 当前索引：返回true，允许该滑动行为
        if (result.comingIndex > this.currentIndex) {
          return false;
        }
        return true;
      })

      Row({ space: 12 }) {
        Button('showNext')
          .onClick(() => {
            this.swiperController.showNext();
          })
        Button('showPrevious')
          .onClick(() => {
            this.swiperController.showPrevious();
          })
      }.margin(5)
    }.width('100%')
    .margin({ top: 5 })
  }
```

![image](public_sys-resources/zh-cn_image_0000002522084912.webp)

**示例9（演示导航点space与bottom）**

该示例通过[bottom](#ZH-CN_TOPIC_0000002522240824__bottom19)和[space](#ZH-CN_TOPIC_0000002522240824__space19)接口，实现了圆点导航点与底部间距为0的间距控制以及导航点之间的间距控制。

```ets
import { LengthMetrics } from '@kit.ArkUI';

// MyDataSource.ets
class MyDataSource implements IDataSource {
  private list: number[] = [];

  constructor(list: number[]) {
    this.list = list;
  }

  totalCount(): number {
    return this.list.length;
  }

  getData(index: number): number {
    return this.list[index];
  }

  registerDataChangeListener(listener: DataChangeListener): void {
  }

  unregisterDataChangeListener() {
  }

// SwiperExample.ets
@Entry
@Component
struct SwiperExample {

  @State space: LengthMetrics = LengthMetrics.vp(0);
  @State spacePool: LengthMetrics[] = [LengthMetrics.vp(0), LengthMetrics.px(3), LengthMetrics.vp(10)];
  @State spaceIndex: number = 0;

  @State ignoreSize: boolean = false;
  @State ignoreSizePool: boolean[] = [false, true];
  @State ignoreSizeIndex: number = 0;

  private swiperController1: SwiperController = new SwiperController();
  private data1: MyDataSource = new MyDataSource([]);

  aboutToAppear(): void {
    let list1: number[] = [];
    for (let i = 1; i <= 10; i++) {
      list1.push(i);
    }
    this.data1 = new MyDataSource(list1);
  }

  build() {
    Scroll() {
      Column({ space: 20 }) {
        Swiper(this.swiperController1) {
          LazyForEach(this.data1, (item: string) => {
            Text(item.toString())
              .width('90%')
              .height(120)
              .backgroundColor(0xAFEEEE)
              .textAlign(TextAlign.Center)
              .fontSize(30)
          }, (item: string) => item)
        }
        .indicator(new DotIndicator()
          .space(this.space) // 控制导航点之间的间距
          .bottom(LengthMetrics.vp(0), this.ignoreSize) // 控制导航点与Swiper底部的间距
          .itemWidth(15)
          .itemHeight(15)
          .selectedItemWidth(15)
          .selectedItemHeight(15)
          .color(Color.Gray)
          .selectedColor(Color.Blue))
        .displayArrow({
          showBackground: true,
          isSidebarMiddle: true,
          backgroundSize: 24,
          backgroundColor: Color.White,
          arrowSize: 18,
          arrowColor: Color.Blue
        }, false)

        Column({ space: 4 }) {
          Button('spaceIndex:' + this.spaceIndex).onClick(() => {
            this.spaceIndex = (this.spaceIndex + 1) % this.spacePool.length;
            this.space = this.spacePool[this.spaceIndex];
          }).margin(10)

          Button('ignoreSizeIndex:' + this.ignoreSizeIndex).onClick(() => {
            this.ignoreSizeIndex = (this.ignoreSizeIndex + 1) % this.ignoreSizePool.length;
            this.ignoreSize = this.ignoreSizePool[this.ignoreSizeIndex];
          }).margin(10)
        }.margin(2)
      }.width('100%')
    }
```

![image](public_sys-resources/zh-cn_image_0000002553364827.webp)

**示例10（Swiper组件基于断点配置显示个数）**

该示例展示了Swiper组件基于断点配置显示个数的效果。

从API version 22开始，新增[displaycount](#ZH-CN_TOPIC_0000002522240824__displaycount22)接口，用于设置Swiper视窗内元素显示个数。

```ets
class MyDataSource implements IDataSource {
  private list: number[] = [];

  constructor(list: number[]) {
    this.list = list;
  }

  totalCount(): number {
    return this.list.length;
  }

  getData(index: number): number {
    return this.list[index];
  }

  registerDataChangeListener(listener: DataChangeListener): void {
  }

  unregisterDataChangeListener() {
  }

@Entry
@Component
struct SwiperExample {
  private data: MyDataSource = new MyDataSource([]);

  aboutToAppear(): void {
    let list: number[] = [];
    for (let i = 1; i <= 10; i++) {
      list.push(i);
    }
    this.data = new MyDataSource(list);
  }

  build() {
    Column() {
      Swiper() {
        LazyForEach(this.data, (item: string) => {
          Text(item.toString())
            .height(160)
            .backgroundColor(0xAFEEEE)
            .textAlign(TextAlign.Center)
            .fontSize(30)
        }, (item: string) => item)
      }
      .width('100%')
      .displayCount({fillType:PresetFillType.BREAKPOINT_SM1MD2LG3}) // 按断点设置视窗内元素显示个数
    }
```

Swiper宽度属于[sm](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-grid-layout#栅格容器断点)及更小的断点区间时显示1列。

![image](public_sys-resources/zh-cn_image_0000002522244906.webp)

Swiper宽度属于[md](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-grid-layout#栅格容器断点)断点区间时显示2列。

![image](public_sys-resources/zh-cn_image_0000002553204867.webp)

**示例11（Swiper组件模拟拖拽）**

该示例展示了Swiper组件如何实现模拟拖拽。在自身不响应拖拽事件的情况下，子组件Column通过触摸事件的信息调用Swiper接口，实现类似跟手拖拽的效果。

从API version 23开始，新增[startFakeDrag](#ZH-CN_TOPIC_0000002522240824__startfakedrag23)接口、[fakeDragBy](#ZH-CN_TOPIC_0000002522240824__fakedragby23)接口、[stopFakeDrag](#ZH-CN_TOPIC_0000002522240824__stopfakedrag23)接口、[isFakeDragging](#ZH-CN_TOPIC_0000002522240824__isfakedragging23)接口，用于实现模拟拖拽。

```ets
// SwiperFakeDragExample.ets
@Entry
@Component
struct SwiperFakeDragExample {
  private swiperController: SwiperController = new SwiperController();
  private baseDisplayX: number = 0;
  private panOption: PanGestureOptions = new PanGestureOptions({ direction: PanDirection.Left | PanDirection.Right });

  build() {
    Scroll() {
      Column({ space: 20 }) {
        Swiper(this.swiperController) {
          Column() {
            Text('可消费拖动事件的内层组件')
              .fontSize(20)
          }
          .justifyContent(FlexAlign.Center)
          .backgroundColor('#D5D5D5')
          .gesture(
            // 内层组件消费了拖拽事件，根据事件信息触发外层Swiper滚动。
            PanGesture(this.panOption)
              .onActionStart((event: GestureEvent) => {
                let ret = this.swiperController.isFakeDragging();
                if (ret) {
                  return;
                }
                ret = this.swiperController.startFakeDrag();
                console.info('startFakeDrag ret = ', ret);
                this.baseDisplayX = event.offsetX;
              })
              .onActionUpdate((event: GestureEvent) => {
                if (event) {
                  let ret = this.swiperController.fakeDragBy(event.offsetX - this.baseDisplayX);
                  console.info('fakeDragBy ret = ', ret);
                  this.baseDisplayX = event.offsetX;
                }
              })
              .onActionEnd((event: GestureEvent) => {
                let ret = this.swiperController.stopFakeDrag();
                console.info('stopFakeDrag ret = ', ret);
              })
          )

          Column()
            .backgroundColor('#E3F8F9')
        }
        .width('90%')
        .height('50%')
      }
      .width('100%')
    }
```

![image](public_sys-resources/zh-cn_image_0000002522084914.webp)