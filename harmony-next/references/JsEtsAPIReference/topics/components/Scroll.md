# Scroll

可滚动的容器组件，当子组件的布局尺寸超过父组件的尺寸时，内容可以滚动。

- 该组件从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
- 该组件嵌套List子组件滚动时，若List不设置宽高，则默认全部加载，在对性能有要求的场景下建议指定List的宽高，最佳实践请参考[懒加载优化性能-Scroll嵌套List导致按需加载失效](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-lazyforeach-optimization#section6296154115367)。
- 该组件滚动的前提是主轴方向大小小于内容大小。
- Scroll组件[通用属性clip](../misc/形状裁剪.md#ZH-CN_TOPIC_0000002529284827__clip12)的默认值为true。
- Scroll组件的高度超出屏幕显示范围时，可以通过设置通用属性[layoutWeight](../misc/尺寸设置.md#ZH-CN_TOPIC_0000002497444850__layoutweight)让Scroll高度适应主轴的剩余空间。
- 手指触摸屏幕时，会停止当前触摸范围内所有滚动组件的滚动动画（[scrollTo](#ZH-CN_TOPIC_0000002497444896__scrollto)和[scrollToIndex](#ZH-CN_TOPIC_0000002497444896__scrolltoindex)接口触发的滚动动画除外），包括边缘回弹动画。
- 组件内部已绑定手势实现跟手滚动等功能，需要增加自定义手势操作时请参考[手势拦截增强](../misc/手势拦截增强.md)进行处理。

#### 子组件

支持单个子组件。

从API version 21开始，Scroll单个子组件的宽高最大为16777216px；API version 20及之前，Scroll单个子组件的宽高最大为1000000px。子组件超出该大小可能导致滚动或显示异常。

#### 接口

Scroll(scroller?: Scroller)

创建Scroll滚动容器。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明scroller[Scroller](#ZH-CN_TOPIC_0000002497444896__scroller)否

可滚动组件的控制器。用于与可滚动组件进行绑定。

**说明：**

不允许和其他滚动类组件，如：[ArcList](ArcList.md)、[List](list.md)、[Grid](Grid.md)、[Scroll](Scroll.md)和[WaterFlow](../misc/WaterFlow.md)绑定同一个滚动控制对象。

#### 属性

除支持[通用属性](../misc/通用属性.md)和[滚动组件通用属性](../misc/滚动组件通用接口.md#ZH-CN_TOPIC_0000002529284871__属性)外，还支持以下属性：

#### scrollable

scrollable(value: ScrollDirection)

设置滚动方向。该值被修改后会重置滚动偏移量。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明value[ScrollDirection](#ZH-CN_TOPIC_0000002497444896__scrolldirection枚举说明)是

滚动方向。

默认值：ScrollDirection.Vertical

当滚动方向设置为[ScrollDirection.FREE](#ZH-CN_TOPIC_0000002497444896__scrolldirection枚举说明)时，Scroll组件仅支持部分能力，见[自由滚动模式下支持的能力](#ZH-CN_TOPIC_0000002497444896__scrolldirection枚举说明)。

#### scrollBar

scrollBar(barState: BarState)

设置滚动条状态。如果容器组件无法滚动，则滚动条不显示。如果容器组件的子组件大小为无穷大，则滚动条不支持拖动和伴随滚动。

从API version 10开始，当滚动组件存在圆角时，为避免滚动条被圆角截断，滚动条会自动计算距顶部和底部的避让距离。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明barState[BarState](../../guides/枚举说明.md#ZH-CN_TOPIC_0000002529284967__barstate)是

滚动条状态。

默认值：BarState.Auto

#### scrollBarColor

scrollBarColor(color: Color | number | string)

设置滚动条的颜色。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明color[Color](../../guides/枚举说明.md#ZH-CN_TOPIC_0000002529284967__color) | number | string是

滚动条的颜色。

默认值：'#66182431'

number为HEX格式颜色，支持rgb或者argb，示例：0xffffff。

string为rgb或者argb格式颜色，示例：'#ffffff'。

#### scrollBarColor22+

scrollBarColor(color: Color | number | string | Resource)

设置滚动条的颜色。与[scrollBarColor](#ZH-CN_TOPIC_0000002497444896__scrollbarcolor)相比，color参数开始支持Resource类型。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明color[Color](../../guides/枚举说明.md#ZH-CN_TOPIC_0000002529284967__color) | number | string | [Resource](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resource)是

滚动条的颜色。

默认值：'#66182431'

number为HEX格式颜色，支持rgb或者argb，示例：0xffffff。string为rgb或者argb格式颜色，示例：'#ffffff'。

#### scrollBarWidth

scrollBarWidth(value: number | string)

设置滚动条的宽度，不支持百分比设置。宽度设置后，滚动条正常状态和按压状态宽度均为滚动条的宽度值。如果滚动条的宽度超过Scroll组件主轴方向的高度，则滚动条的宽度会变为默认值。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明valuenumber | string是

滚动条的宽度。

默认值：4

单位：vp

取值范围：设置为小于0的值时，按默认值处理。设置为0时，不显示滚动条。

#### scrollSnap10+

scrollSnap(value: ScrollSnapOptions)

设置Scroll组件的限位滚动模式。

限位动画期间[onWillScroll](#ZH-CN_TOPIC_0000002497444896__onwillscroll12)事件上报的滚动操作来源类型为ScrollSource.FLING。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明value[ScrollSnapOptions](#ZH-CN_TOPIC_0000002497444896__scrollsnapoptions10对象说明)是Scroll组件的限位滚动模式。

#### edgeEffect

edgeEffect(edgeEffect: EdgeEffect, options?: EdgeEffectOptions)

设置边缘滑动效果。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明edgeEffect[EdgeEffect](../../guides/枚举说明.md#ZH-CN_TOPIC_0000002529284967__edgeeffect)是

Scroll组件的边缘滑动效果，支持弹簧效果和阴影效果。

默认值：EdgeEffect.None

options11+[EdgeEffectOptions](../misc/滚动组件通用接口.md#ZH-CN_TOPIC_0000002529284871__edgeeffectoptions11对象说明)否

组件内容大小小于组件自身时，是否开启滑动效果。设置为{ alwaysEnabled: true }会开启滑动效果，{ alwaysEnabled: false }不开启。

默认值：{ alwaysEnabled: true }

#### enableScrollInteraction10+

enableScrollInteraction(value: boolean)

设置是否支持滚动手势。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明valueboolean是

是否支持滚动手势。设置为true时可以通过手指或者鼠标滚动，设置为false时无法通过手指或者鼠标滚动，但不影响控制器[Scroller](Scroll.md#ZH-CN_TOPIC_0000002497444896__scroller)的滚动接口。

默认值：true

组件无法通过鼠标按下拖动操作进行滚动。

#### nestedScroll10+

nestedScroll(value: NestedScrollOptions)

设置前后两个方向的嵌套滚动模式，实现与父组件的滚动联动。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明value[NestedScrollOptions](../misc/滚动组件通用接口.md#ZH-CN_TOPIC_0000002529284871__nestedscrolloptions10对象说明)是

嵌套滚动选项。

默认值：{ scrollForward: NestedScrollMode.SELF_ONLY, scrollBackward: NestedScrollMode.SELF_ONLY }

Scroll设置[enablePaging](#ZH-CN_TOPIC_0000002497444896__enablepaging11)或者[scrollSnap](#ZH-CN_TOPIC_0000002497444896__scrollsnap10)，并同时设置父组件优先的嵌套滚动时，嵌套滚动不生效。

#### friction10+

friction(value: number | Resource)

设置摩擦系数，手动划动滚动区域时生效，仅影响惯性滚动过程，对惯性滚动过程中的链式效果有间接影响。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明valuenumber | [Resource](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resource)是

摩擦系数。

默认值：非可穿戴设备为0.6，可穿戴设备为0.9。

从API version 11开始，非可穿戴设备默认值为0.7。

从API version 12开始，非可穿戴设备默认值为0.75。

取值范围：(0, +∞)，设置为小于等于0的值时，按默认值处理。

#### enablePaging11+

enablePaging(value: boolean)

设置是否支持划动翻页。如果同时设置了划动翻页enablePaging和限位滚动scrollSnap，则scrollSnap优先生效，enablePaging不生效。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明valueboolean是

是否支持划动翻页。设置为true支持滑动翻页，false不支持。

默认值：false

#### initialOffset12+

initialOffset(value: OffsetOptions)

设置初始滚动偏移量。只在首次布局时生效，后续动态修改该属性值不生效。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明value[OffsetOptions](#ZH-CN_TOPIC_0000002497444896__offsetoptions12对象说明)是当输入的大小为百分比时，初始滚动偏移量为Scroll组件主轴方向大小与百分比数值之积。

#### maxZoomScale20+

maxZoomScale(scale: number)

设置Scroll组件内容的最大手势缩放比例。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明scalenumber是

Scroll组件内容的最大手势缩放比例。

默认值：1

取值范围：(0, +∞)，小于或等于0时按默认值1处理。

#### minZoomScale20+

minZoomScale(scale: number)

设置Scroll组件内容的最小手势缩放比例。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明scalenumber是

Scroll组件内容的最小手势缩放比例。

默认值：1

取值范围：(0, maxZoomScale]，小于或等于0时按默认值1处理，大于maxZoomScale时按maxZoomScale处理。

当maxZoomScale和minZoomScale不同时为1时，Scroll组件会启用缩放手势。

#### zoomScale20+

zoomScale(scale: number)

设置Scroll组件内容的缩放比例。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明scalenumber是

设置Scroll组件内容的缩放比例，该参数支持[!!](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-binding)双向绑定变量。

默认值：1

取值范围：(0, +∞)，小于或等于0时按默认值1处理。

#### enableBouncesZoom20+

enableBouncesZoom(enable: boolean)

启用过缩放回弹效果。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明enableboolean是

启用过缩放回弹效果。设置为true表示启用该效果，设置为false表示禁用该效果。

默认值：true

#### ScrollDirection枚举说明

滚动方向枚举。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称值说明Vertical0

仅支持竖直方向滚动。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

Horizontal1

仅支持水平方向滚动。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

Free(deprecated) 2

支持竖直或水平方向滚动。

**说明：** 从API version 7开始支持，从API version 9开始废弃，建议使用FREE替代。FREE枚举值从API version 20开始支持。

None3

不可滚动。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

FREE20+4

自由滚动。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

FREE（自由滚动）模式下支持的能力：

**支持的属性****支持的事件****支持的[Scroller](#ZH-CN_TOPIC_0000002497444896__scroller)接口**[scrollBar](#ZH-CN_TOPIC_0000002497444896__scrollbar)[onWillScroll](#ZH-CN_TOPIC_0000002497444896__onwillscroll12)[scrollTo](#ZH-CN_TOPIC_0000002497444896__scrollto)[scrollBarColor](#ZH-CN_TOPIC_0000002497444896__scrollbarcolor)[onDidScroll](#ZH-CN_TOPIC_0000002497444896__ondidscroll12)[scrollEdge](#ZH-CN_TOPIC_0000002497444896__scrolledge)[scrollBarWidth](#ZH-CN_TOPIC_0000002497444896__scrollbarwidth)[onScrollEdge](#ZH-CN_TOPIC_0000002497444896__onscrolledge)[scrollPage](#ZH-CN_TOPIC_0000002497444896__scrollpage9)[scrollBarMargin](../misc/滚动组件通用接口.md#ZH-CN_TOPIC_0000002529284871__scrollbarmargin20)[onScrollStart](#ZH-CN_TOPIC_0000002497444896__onscrollstart9)[currentOffset](#ZH-CN_TOPIC_0000002497444896__currentoffset)[edgeEffect](#ZH-CN_TOPIC_0000002497444896__edgeeffect)[onScrollStop](#ZH-CN_TOPIC_0000002497444896__onscrollstop9)[scrollBy](#ZH-CN_TOPIC_0000002497444896__scrollby9)[enableScrollInteraction](#ZH-CN_TOPIC_0000002497444896__enablescrollinteraction10)-[getItemRect](#ZH-CN_TOPIC_0000002497444896__getitemrect11)[friction](#ZH-CN_TOPIC_0000002497444896__friction10)--[clipContent](../misc/滚动组件通用接口.md#ZH-CN_TOPIC_0000002529284871__clipcontent14)--[initialOffset](#ZH-CN_TOPIC_0000002497444896__initialoffset12)--[scrollable](#ZH-CN_TOPIC_0000002497444896__scrollable)--

- edgeEffect属性仅支持Spring和None边缘滑动效果。
- onWillScroll回调仅支持在跟手滑动阶段重载偏移量。
- onScrollEdge回调只在到达边缘时触发一次，回弹后不会重复触发。
- 在抛滑动画过程中切换边缘模式不会打断动画。

#### ScrollSnapOptions10+对象说明

限位滚动模式对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明snapAlign[ScrollSnapAlign](list.md#ZH-CN_TOPIC_0000002529284863__scrollsnapalign10枚举说明)否否

设置Scroll组件限位滚动时的对齐方式。

**说明：**

1.该属性默认值为ScrollSnapAlign.NONE。

snapPagination[Dimension](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__dimension10) | Array<Dimension>否是

设置Scroll组件限位滚动时的分页点。

**说明：**

1.当属性为Dimension时，Dimension表示每页的大小，系统按照该大小进行分页。

2.当属性为Array<Dimension>时，每个Dimension表示分页点，系统按照分页点进行分页。每个Dimension的范围为[0,可滑动距离]。

3.当该属性不填或者Dimension为小于等于0的输入时，按异常值，无限位滚动处理。当该属性值为Array<Dimension>数组时，数组中的数值必须为单调递增。

4.当输入为百分比时，实际的大小为Scroll组件的视口与百分比数值之积。

enableSnapToStartboolean否是

在Scroll组件限位滚动模式下，该属性设置为true后，不允许Scroll在开头和第一页间自由滑动，该属性设置为false后，允许Scroll在开头和第一页间自由滑动。

**说明：**

1.该属性值默认为true。

2.该属性仅当snapPagination属性为Array<Dimension>时生效，不支持Dimension。

enableSnapToEndboolean否是

在Scroll组件限位滚动模式下，该属性设置为true后，不允许Scroll在最后一页和末尾间自由滑动，该属性设置为false后，允许Scroll在最后一页和末尾间自由滑动。

**说明：**

1.该属性值默认为true。

2.该属性仅当snapPagination属性为Array<Dimension>时生效，不支持Dimension。

#### 事件

除支持[通用事件](../misc/通用事件.md)和[滚动组件通用事件](../misc/滚动组件通用接口.md#ZH-CN_TOPIC_0000002529284871__事件)外，还支持以下事件：

不支持滚动组件通用事件中的[onWillScroll](../misc/滚动组件通用接口.md#ZH-CN_TOPIC_0000002529284871__onwillscroll12)、[onDidScroll](../misc/滚动组件通用接口.md#ZH-CN_TOPIC_0000002529284871__ondidscroll12)事件。

#### onScrollFrameBegin9+

onScrollFrameBegin(event: OnScrollFrameBeginCallback)

该接口回调时，事件参数传入即将发生的滚动量，事件处理函数中可根据应用场景计算实际需要的滚动量并作为事件处理函数的返回值返回，Scroll将按照返回值的实际滚动量进行滚动。

支持[offsetRemain](#ZH-CN_TOPIC_0000002497444896__onscrollframebeginhandlerresult18对象说明)为负值。

若通过onScrollFrameBegin事件和[scrollBy](#ZH-CN_TOPIC_0000002497444896__scrollby9)方法实现容器嵌套滚动，需设置子滚动节点的[EdgeEffect](#ZH-CN_TOPIC_0000002497444896__edgeeffect)为None。如Scroll嵌套List滚动时，List组件的[edgeEffect](list.md#ZH-CN_TOPIC_0000002529284863__edgeeffect)属性需设置为EdgeEffect.None，否则抛滑List，会触发List的边缘回弹动画，导致嵌套滚动失效。

满足以下任一条件时触发该事件：

1. 用户交互（如手指滑动、键鼠操作等）触发滚动。
1. Scroll惯性滚动。
1. 调用[fling](#ZH-CN_TOPIC_0000002497444896__fling12)接口触发滚动。

不触发该事件的条件：

1. 调用除[fling](#ZH-CN_TOPIC_0000002497444896__fling12)接口外的其他滚动控制接口。
1. 越界回弹。
1. 拖动滚动条。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明event[OnScrollFrameBeginCallback](#ZH-CN_TOPIC_0000002497444896__onscrollframebegincallback18)是每帧滚动开始回调函数。

#### onScroll(deprecated)

onScroll(event: (xOffset: number, yOffset: number) => void)

滚动事件回调，返回滚动时水平、竖直方向偏移量，单位vp。

触发该事件的条件：

1、滚动组件触发滚动时触发，支持键鼠操作等其他触发滚动的输入设置。

2、通过滚动控制器API接口调用。

3、越界回弹。

从API version 7开始支持，从API version 12开始废弃，建议使用[onWillScroll](#ZH-CN_TOPIC_0000002497444896__onwillscroll12)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明xOffsetnumber是

相对于上一帧水平方向的偏移量，Scroll中的内容向左滚动时偏移量为正，向右滚动时偏移量为负。

单位vp。

yOffsetnumber是

相对于上一帧竖直方向的偏移量，Scroll中的内容向上滚动时偏移量为正，向下滚动时偏移量为负。

单位vp。

#### onWillScroll12+

onWillScroll(handler: ScrollOnWillScrollCallback)

滚动事件回调，Scroll滚动前触发。

回调当前帧将要滚动的偏移量和当前滚动状态和滚动操作来源，其中回调的偏移量为计算得到的将要滚动的偏移量值，并非最终实际滚动偏移。可以通过该回调返回值指定Scroll将要滚动的偏移。

触发该事件的条件：

1、滚动组件触发滚动时触发，支持键鼠操作等其他触发滚动的输入设置。

2、通过滚动控制器API接口调用。

3、越界回弹。

滚动事件的回调函数在滚动过程中会被频繁触发，因此应避免在该回调函数中执行耗时操作，以防止应用出现卡顿和丢帧的问题。最佳实践请参考[主线程耗时操作优化指导-高频回调场景](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-time-optimization-of-the-main-thread#section10112623611)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明handler[ScrollOnWillScrollCallback](#ZH-CN_TOPIC_0000002497444896__scrollonwillscrollcallback12)是Scroll滚动前触发的回调。

#### onDidScroll12+

onDidScroll(handler: ScrollOnScrollCallback)

滚动事件回调，Scroll滚动时触发。

返回当前帧滚动的偏移量和当前滚动状态。

触发该事件的条件：

1、滚动组件触发滚动时触发，支持键鼠操作等其他触发滚动的输入设置。

2、通过滚动控制器API接口调用。

3、越界回弹。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明handler[ScrollOnScrollCallback](#ZH-CN_TOPIC_0000002497444896__scrollonscrollcallback12)是Scroll滚动时触发的回调。

#### onScrollEdge

onScrollEdge(event: OnScrollEdgeCallback)

滚动到边缘事件回调。

触发该事件的条件：

1、滚动组件滚动到边缘时触发，支持键鼠操作等其他触发滚动的输入设置。

2、通过滚动控制器API接口调用。

3、越界回弹。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明event[OnScrollEdgeCallback](#ZH-CN_TOPIC_0000002497444896__onscrolledgecallback18)是

滚动到的边缘位置。

当Scroll设置为水平方向滚动时，上报[Edge.Center](../../guides/枚举说明.md#ZH-CN_TOPIC_0000002529284967__edge)表示水平方向起始位置，上报[Edge.Baseline](../../guides/枚举说明.md#ZH-CN_TOPIC_0000002529284967__edge)表示水平方向末尾位置。由于[Edge.Center](../../guides/枚举说明.md#ZH-CN_TOPIC_0000002529284967__edge)和[Edge.Baseline](../../guides/枚举说明.md#ZH-CN_TOPIC_0000002529284967__edge)枚举值已经废弃，推荐使用[onReachStart](../misc/滚动组件通用接口.md#ZH-CN_TOPIC_0000002529284871__onreachstart11)、[onReachEnd](../misc/滚动组件通用接口.md#ZH-CN_TOPIC_0000002529284871__onreachend11)事件监听是否滚动到边界。

#### onScrollEnd(deprecated)

onScrollEnd(event: () => void)

滚动停止事件回调。

触发该事件的条件：

1、滚动组件触发滚动后停止，支持键鼠操作等其他触发滚动的输入设置。

2、通过滚动控制器API接口调用后停止，带过渡动效。

从API version 7开始支持，从API version 9开始废弃，建议使用[onScrollStop](#ZH-CN_TOPIC_0000002497444896__onscrollstop9)替代。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明event() => void是滚动停止事件回调。

#### onScrollStart9+

onScrollStart(event: VoidCallback)

滚动开始时触发。手指拖动Scroll或拖动Scroll的滚动条触发的滚动开始时，会触发该事件。使用[Scroller](#ZH-CN_TOPIC_0000002497444896__scroller)滚动控制器触发的带动画的滚动，动画开始时会触发该事件。

触发该事件的条件：

1、滚动组件开始滚动时触发，支持键鼠操作等其他触发滚动的输入设置。

2、通过滚动控制器API接口调用后开始，带过渡动效。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明event[VoidCallback](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__voidcallback12)是滚动开始回调。

#### onScrollStop9+

onScrollStop(event: VoidCallback)

滚动停止时触发。手拖动Scroll或拖动Scroll的滚动条触发的滚动，手离开屏幕后滚动停止时会触发该事件。使用[Scroller](#ZH-CN_TOPIC_0000002497444896__scroller)滚动控制器触发的带动画的滚动，动画停止时会触发该事件。

触发该事件的条件：

1、滚动组件触发滚动后停止，支持键鼠操作等其他触发滚动的输入设置。

2、通过滚动控制器API接口调用后开始，带过渡动效。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明event[VoidCallback](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__voidcallback12)是滚动停止回调。

#### onDidZoom20+

onDidZoom(event: ScrollOnDidZoomCallback)

每帧缩放完成时触发。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明event[ScrollOnDidZoomCallback](#ZH-CN_TOPIC_0000002497444896__scrollondidzoomcallback20)是每帧缩放完成时回调。

#### onZoomStart20+

onZoomStart(event: VoidCallback)

手势缩放开始触发。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明event[VoidCallback](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__voidcallback12)是缩放开始回调。

#### onZoomStop20+

onZoomStop(event: VoidCallback)

手势缩放停止时触发。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明event[VoidCallback](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__voidcallback12)是缩放停止回调。

#### ScrollOnScrollCallback12+

type ScrollOnScrollCallback = (xOffset: number, yOffset: number, scrollState: ScrollState) => void

Scroll滚动时触发的回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明xOffsetnumber是

相对于上一帧水平方向的偏移量，Scroll中的内容向左滚动时偏移量为正，向右滚动时偏移量为负。

单位vp。

yOffsetnumber是

相对于上一帧竖直方向的偏移量，Scroll中的内容向上滚动时偏移量为正，向下滚动时偏移量为负。

单位vp。

scrollState[ScrollState](list.md#ZH-CN_TOPIC_0000002529284863__scrollstate枚举说明)是当前滚动状态。

若通过[onScrollFrameBegin](#ZH-CN_TOPIC_0000002497444896__onscrollframebegin9)事件和[scrollBy](#ZH-CN_TOPIC_0000002497444896__scrollby9)方法实现容器嵌套滚动，需设置子滚动节点的EdgeEffect为None。如Scroll嵌套List滚动时，List组件的[edgeEffect](list.md#ZH-CN_TOPIC_0000002529284863__edgeeffect)属性需设置为EdgeEffect.None。

#### ScrollOnWillScrollCallback12+

type ScrollOnWillScrollCallback = (xOffset: number, yOffset: number, scrollState: ScrollState, scrollSource: ScrollSource) => void | OffsetResult

Scroll滚动前触发的回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明xOffsetnumber是

相对于上一帧水平方向的偏移量，Scroll中的内容向左滚动时偏移量为正，向右滚动时偏移量为负。

单位vp。

yOffsetnumber是

相对于上一帧竖直方向的偏移量，Scroll中的内容向上滚动时偏移量为正，向下滚动时偏移量为负。

单位vp。

scrollState[ScrollState](list.md#ZH-CN_TOPIC_0000002529284863__scrollstate枚举说明)是当前滚动状态。scrollSource[ScrollSource](../../guides/枚举说明.md#ZH-CN_TOPIC_0000002529284967__scrollsource12)是当前滚动操作的来源。

**返回值：**

类型说明void | [OffsetResult](#ZH-CN_TOPIC_0000002497444896__offsetresult11对象说明)返回OffsetResult时按照开发者指定的偏移量滚动；不返回时按回调参数(xOffset, yOffset)滚动。

#### OnScrollEdgeCallback18+

type OnScrollEdgeCallback = (side: Edge) => void

滚动到边缘时触发的回调。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明side[Edge](../../guides/枚举说明.md#ZH-CN_TOPIC_0000002529284967__edge)是滚动到的边缘位置。

#### OnScrollFrameBeginCallback18+

type OnScrollFrameBeginCallback = (offset: number, state: ScrollState) => OnScrollFrameBeginHandlerResult;

Scroll每帧滚动前触发的回调。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明offsetnumber是即将发生的滑动量，单位vp。state[ScrollState](list.md#ZH-CN_TOPIC_0000002529284863__scrollstate枚举说明)是当前滑动状态。

**返回值：**

类型说明[OnScrollFrameBeginHandlerResult](#ZH-CN_TOPIC_0000002497444896__onscrollframebeginhandlerresult18对象说明)返回实际滑动量。

#### OnScrollFrameBeginHandlerResult18+对象说明

[OnScrollFrameBeginCallback](#ZH-CN_TOPIC_0000002497444896__onscrollframebegincallback18)返回的实际相对上一帧滚动偏移量。

为规范匿名对象的定义，API version 18版本修改了此处的元素定义。其中，保留了历史匿名对象的起始版本信息，会出现外层元素@since版本号高于内层元素版本号的情况，但这不影响接口的使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明offsetRemain9+number否否

实际相对上一帧的滚动偏移量。

单位vp。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

#### ScrollOnDidZoomCallback20+

type ScrollOnDidZoomCallback = (scale: number) => void

Scroll每帧缩放完成时触发的回调。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明scalenumber是当前缩放倍数。

#### Scroller

可滚动容器组件的控制器，可以将此组件绑定至容器组件，然后通过它控制容器组件的滚动。同一个控制器不可以控制多个容器组件，目前支持绑定到ArcList、ArcScrollBar、List、Scroll、ScrollBar、Grid、WaterFlow上。

1、Scroller控制器与滚动容器组件的绑定发生在组件创建阶段。

2、Scroller控制器与滚动容器组件绑定后才可以正常调用Scroller方法，否则根据调用接口不同会不生效或者抛异常。

3、以[aboutToAppear](../misc/自定义组件的生命周期.md#ZH-CN_TOPIC_0000002529444913__abouttoappear)为例，aboutToAppear在创建自定义组件的新实例后，在执行其build()方法之前执行。因此如果滚动组件在自定义组件build内，在该自定义组件aboutToAppear执行时，内部滚动组件还没有创建，是不能正常调用上述Scroller方法的。

4、以[onAppear](../misc/挂载卸载事件.md#ZH-CN_TOPIC_0000002529284813__onappear)为例，组件挂载显示后触发此回调。因此在滚动组件的onAppear回调执行时，滚动组件已经创建并已经和Scroller绑定成功，是可以正常调用Scroller方法的。

#### 导入对象

```ets
scroller: Scroller = new Scroller();
```

#### constructor

constructor()

Scroller的构造函数。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

#### scrollTo

scrollTo(options: ScrollOptions)

滑动到指定位置。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明options[ScrollOptions](#ZH-CN_TOPIC_0000002497444896__scrolloptions18对象说明)是滑动到指定位置的参数。

ScrollTo动画速度大于200vp/s时，滚动组件区域内的组件不响应点击事件。

#### scrollEdge

scrollEdge(value: Edge, options?: ScrollEdgeOptions)

滚动到容器边缘，不区分滚动轴方向，Edge.Top和Edge.Start表现相同，Edge.Bottom和Edge.End表现相同。

Scroll组件默认有动画，Grid、List、WaterFlow组件默认无动画。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明value[Edge](../../guides/枚举说明.md#ZH-CN_TOPIC_0000002529284967__edge)是滚动到的边缘位置。options12+[ScrollEdgeOptions](#ZH-CN_TOPIC_0000002497444896__scrolledgeoptions12对象说明)否设置滚动到边缘位置的模式。

#### fling12+

fling(velocity: number): void

滚动类组件根据传入的初始速度进行惯性滚动。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明velocitynumber是

惯性滚动的初始速度值。单位：vp/s

**说明：**

velocity值设置为0，视为异常值，本次滚动不生效。如果值为正数，则向顶部滚动；如果值为负数，则向底部滚动。

取值范围：(-∞, +∞)

**错误码**：

以下错误码详细介绍请参考[通用错误码](../../errors/通用错误码.md)和[滚动类组件错误码](../../errors/滚动类组件错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed.100004Controller not bound to component.

#### scrollPage9+

scrollPage(value: ScrollPageOptions)

滚动到下一页或者上一页。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明value[ScrollPageOptions](#ZH-CN_TOPIC_0000002497444896__scrollpageoptions14对象说明)是设置翻页模式。

#### scrollPage(deprecated)

scrollPage(value: { next: boolean, direction?: Axis })

滚动到下一页或者上一页。

从API version 7开始支持，从API version 9开始废弃，建议使用[scrollPage9+](#ZH-CN_TOPIC_0000002497444896__scrollpage9)替代。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明nextboolean是是否向下翻页。true表示向下翻页，false表示向上翻页。direction[Axis](../../guides/枚举说明.md#ZH-CN_TOPIC_0000002529284967__axis)否设置滚动方向为水平或竖直方向。

#### currentOffset

currentOffset(): OffsetResult

获取当前的滚动总偏移量。

Grid、List、WaterFlow组件有懒加载机制，组件内容没有加载并布局完成时，内容总偏移量通过估算得到，估算结果可能会有误差。其中List组件可以通过[childrenMainSize](list.md#ZH-CN_TOPIC_0000002529284863__childrenmainsize12)属性解决估算不准确的问题。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

类型说明[OffsetResult11+](#ZH-CN_TOPIC_0000002497444896__offsetresult11对象说明)

返回当前的滚动总偏移量。

**说明：**

当scroller控制器未绑定容器组件或者容器组件被异常释放时，currentOffset的返回值为空。

#### scrollToIndex

scrollToIndex(value: number, smooth?: boolean, align?: ScrollAlign, options?: ScrollToIndexOptions)

滑动到指定Index，支持设置滑动额外偏移量。

开启smooth动效时，会对经过的所有item进行加载和布局计算，当大量加载item时会导致性能问题，建议先调用scrollToIndex不带动画跳转到目标附近位置，再调用scrollToIndex带动画滚动到目标位置。

1.仅支持ArcList、Grid、List、WaterFlow组件。

2.在[LazyForEach](../misc/LazyForEach.md)、[ForEach](../misc/ForEach.md)、[Repeat](../misc/Repeat.md)刷新数据源时，需确保在数据刷新完成之后再调用此接口。

3.从API version 11开始，在List中支持[contentStartOffset](list.md#ZH-CN_TOPIC_0000002529284863__contentstartoffset11)和[contentEndOffset](list.md#ZH-CN_TOPIC_0000002529284863__contentendoffset11)。从API version 22开始，在Grid和Waterflow组件中支持设置[contentStartOffset](../misc/滚动组件通用接口.md#ZH-CN_TOPIC_0000002529284871__contentstartoffset22)和[contentEndOffset](../misc/滚动组件通用接口.md#ZH-CN_TOPIC_0000002529284871__contentendoffset22)。

-

当滚动容器组件设置contentStartOffset时，如果ScrollAlign设置为START，滚动结束时，指定item首部会与滚动容器组件contentStartOffset处对齐。

-

当滚动容器组件设置contentEndOffset时，如果ScrollAlign设置为END，滚动结束时，指定item尾部会与滚动容器组件contentEndOffset处对齐。

-

当滚动容器组件设置contentStartOffset或contentEndOffset时，如果ScrollAlign设置为AUTO，且指定item完全处于显示区内，不做调整；否则依照滚动距离最短的原则，将指定item首部与滚动组件contentStartOffset处对齐，或指定item尾部与滚动组件contentEndOffset处对齐，使指定item完全显示。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明valuenumber是

要滑动到的目标元素在当前容器中的索引值。

**说明：**

value值设置成负值或者大于当前容器子组件的最大索引值，视为异常值，本次跳转不生效。

smoothboolean否

设置滑动到列表项在列表中的索引值时是否有动效，true表示有动效，false表示没有动效。

默认值：false。

align[ScrollAlign](#ZH-CN_TOPIC_0000002497444896__scrollalign10枚举说明)否

指定滑动到的元素与当前容器的对齐方式。

List中的默认值为：ScrollAlign.START。Grid中默认值为：ScrollAlign.AUTO。WaterFlow中的默认值为：ScrollAlign.START。

**说明：**

仅List、Grid、WaterFlow组件支持该参数。

options12+[ScrollToIndexOptions](#ZH-CN_TOPIC_0000002497444896__scrolltoindexoptions12对象说明)否

设置滑动到指定Index的选项，如额外偏移量。

默认值：0，单位：vp。

#### scrollBy9+

scrollBy(dx: Length, dy: Length)

滑动指定距离。

支持ArcList、Scroll、List、Grid、WaterFlow组件。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明dx[Length](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__length)是

水平方向滚动距离，不支持百分比形式。

取值范围：(-∞, +∞)

dy[Length](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__length)是

竖直方向滚动距离，不支持百分比形式。

取值范围：(-∞, +∞)

#### isAtEnd10+

isAtEnd(): boolean

查询组件是否滚动到底部。

支持ArcList、Scroll、List、Grid、WaterFlow组件。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

类型说明booleantrue表示组件已经滚动到底部，false表示组件还没滚动到底部。

#### getItemRect11+

getItemRect(index: number): RectResult

获取子组件的大小及相对容器组件的位置。

支持ArcList、Scroll、List、Grid、WaterFlow组件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明indexnumber是子组件的索引值。

- index必须是当前显示区域显示的子组件的索引值，否则视为非法值。
- 非法值返回的大小和位置均为0。

**返回值：**

类型说明[RectResult](../misc/自定义事件分发.md#ZH-CN_TOPIC_0000002497444840__rectresult)

子组件的大小和相对于组件的位置。

单位：vp。

**错误码**：

以下错误码详细介绍请参考[通用错误码](../../errors/通用错误码.md)和[滚动类组件错误码](../../errors/滚动类组件错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed.100004Controller not bound to component.

#### getItemIndex14+

getItemIndex(x: number, y: number): number

通过坐标获取子组件的索引。

支持List、Grid、WaterFlow组件。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明xnumber是x轴坐标，单位为vp。ynumber是y轴坐标，单位为vp。

非法值返回的索引为-1。

**返回值：**

类型说明number返回子组件的索引。

**错误码**：

以下错误码详细介绍请参考[通用错误码](../../errors/通用错误码.md)和[滚动类组件错误码](../../errors/滚动类组件错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed.100004The controller not bound to component.

#### contentSize22+

contentSize(): SizeResult

获取滚动组件内容总大小。

-

Grid、List、WaterFlow和Scroll组件主轴方向内容大小为所有子组件布局后的总大小，交叉轴方向内容大小为组件自身交叉轴方向大小减去padding和border后的大小。

-

Grid、List、WaterFlow组件有懒加载机制，该接口依赖已布局的子节点进行估算。如果组件内容没有布局完成且子组件高度不一致，估算结果可能会有误差，需要开发者去适配，比如List组件可以通过childrenMainSize属性解决估算不准问题。

-

如果应用动态增删子节点，则需要应用动态获取内容总大小，来保证接口获取结果的即时性。

-

当Scroll组件设置scrollable为ScrollDirection.FREE自由滚动模式时，获取到的内容总大小为子组件缩放后的总大小。

-

当Scroll组件设置scrollable为ScrollDirection.None不可滚动时，获取到的内容总大小为0。

-

当Grid组件同时设置columnsTemplate和rowsTemplate，或columnsTemplate和rowsTemplate都不设置时即为不可滚动场景，此时获取到的内容总大小高度为0，宽度为Grid组件内容区宽度。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

类型说明[SizeResult](../misc/自定义组件的自定义布局.md#ZH-CN_TOPIC_0000002497604948__sizeresult10)

滚动组件内容总大小，包括内容宽度和高度。

单位：vp

**错误码**：

以下错误码详细介绍请参考[滚动类组件错误码](../../errors/滚动类组件错误码.md)。

错误码ID错误信息100004Controller not bound to a component.

#### OffsetResult11+对象说明

滑动偏移量对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明xOffsetnumber否否

水平滑动偏移。

返回值单位为vp。

yOffsetnumber否否

竖直滑动偏移。

返回值单位为vp。

#### ScrollAnimationOptions12+对象说明

自定义滚动动效的参数选项。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明durationnumber否是

设置滚动时长。

默认值：1000

**说明：**

设置为小于0的值时，按默认值显示。

curve[Curve](../../guides/枚举说明.md#ZH-CN_TOPIC_0000002529284967__curve) | [ICurve](../../modules/ohos/@ohos.curves (插值计算).md#ZH-CN_TOPIC_0000002497604788__icurve9)否是

设置滚动曲线。

默认值：Curve.Ease

canOverScrollboolean否是

设置滚动动画滚动到边界后，是否转换成越界回弹动画。

默认值：false

**说明：**

仅在设置为true，且组件的edgeEffect设置为[EdgeEffect.Spring](../../guides/枚举说明.md#ZH-CN_TOPIC_0000002529284967__edgeeffect)时，使用动画滚动到边界会转换为越界回弹动画，设置为false时，滚动到边界会直接停止动画，不会转换为越界回弹动画。

从API version 20开始，如果[ScrollOptions](#ZH-CN_TOPIC_0000002497444896__scrolloptions18对象说明)中的canOverScroll设置为true，表示滚动可以停留在过界位置，滚动动画过界后不会转换为回弹动画。

#### ScrollAlign10+枚举说明

对齐方式枚举。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称值说明START0首部对齐。指定item首部与滚动容器组件首部对齐。CENTER1居中对齐。指定item主轴方向居中对齐于滚动容器组件。END2尾部对齐。指定item尾部与滚动容器组件尾部对齐。AUTO3

自动对齐。

若指定item完全处于显示区，不做调整。否则依照滑动距离最短的原则，将指定item首部对齐或尾部对齐于滚动容器组件，使指定item完全处于显示区。

#### ScrollToIndexOptions12+对象说明

滑动到指定Index的参数选项。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明extraOffset[LengthMetrics](../graphics/Graphics.md#ZH-CN_TOPIC_0000002529444761__lengthmetrics12)否是滑动到指定Index的额外偏移量。如果值为正数，则向底部额外偏移；如果值为负数，则向顶部额外偏移。

#### ScrollPageOptions14+对象说明

翻页模式的参数选项。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明nextboolean否否是否向下翻页。true表示向下翻页，false表示向上翻页。animationboolean否是

是否开启翻页动画效果。true有动画，false无动画。

默认值：false。

#### OffsetOptions12+对象说明

初始滚动偏移量的参数选项。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明xOffset[Dimension](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__dimension10)否是

水平滚动偏移。

默认值：0

yOffset[Dimension](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__dimension10)否是

垂直滚动偏移。

默认值：0

#### ScrollEdgeOptions12+对象说明

滚动到边缘位置的参数选项。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明velocitynumber否是

设置滚动到容器边缘的固定速度。如果设置小于等于0的值，参数不生效。

默认值：0

单位： vp/s

#### ScrollOptions18+对象说明

滚动到指定位置的参数选项。

为规范匿名对象的定义，API 18版本修改了此处的元素定义。其中，保留了历史匿名对象的起始版本信息，会出现外层元素@since版本号高于内层元素版本号的情况，但这不影响接口的使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明xOffset10+number | string否否

水平滚动总偏移量。

**说明：**

该参数值不支持设置百分比。

仅滚动轴为x轴时生效。

取值范围：当值小于0时，不带动画的滚动，按0处理。带动画的滚动，默认滚动到起始位置后停止，可通过设置animation参数，使滚动在越界时启动回弹动画。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

yOffset10+number | string否否

垂直滚动总偏移量。

**说明：**

该参数值不支持设置百分比。

仅滚动轴为y轴时生效。

取值范围：当值小于0时，不带动画的滚动，按0处理。带动画的滚动，默认滚动到起始位置后停止，可通过设置animation参数，使滚动在越界时启动回弹动画。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

animation10+[ScrollAnimationOptions](#ZH-CN_TOPIC_0000002497444896__scrollanimationoptions12对象说明) | boolean否是

动画配置。

- ScrollAnimationOptions: 自定义滚动动效。

- boolean: 使能默认弹簧动效。

默认值：

ScrollAnimationOptions: { duration: 1000, curve: Curve.Ease, canOverScroll: false }

boolean: false

**说明：**

当前List、Scroll、Grid、WaterFlow均支持boolean类型和ICurve曲线。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

canOverScroll20+boolean否是

滚动目标位置是否可以超出边界停留。仅当组件的edgeEffect设置为EdgeEffect.Spring时，滚动能够越界停留。

设置为true时滚动可以在过界后停留，设置为false时滚动无法在过界后停留。

默认值：false

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

#### UIScrollEvent19+

frameNode中[getEvent('Scroll')](FrameNode.md#ZH-CN_TOPIC_0000002529284787__geteventscroll19)方法的返回值，可用于给Scroll节点设置滚动事件。

UIScrollEvent继承于[UIScrollableCommonEvent](../misc/滚动组件通用接口.md#ZH-CN_TOPIC_0000002529284871__uiscrollablecommonevent19)。

#### setOnWillScroll19+

setOnWillScroll(callback: ScrollOnWillScrollCallback | undefined): void

设置[onWillScroll](#ZH-CN_TOPIC_0000002497444896__onwillscroll12)事件的回调。

方法入参为undefined时，会重置事件回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明callback[ScrollOnWillScrollCallback](Scroll.md#ZH-CN_TOPIC_0000002497444896__scrollonwillscrollcallback12) | undefined是onWillScroll事件的回调函数。

#### setOnDidScroll19+

setOnDidScroll(callback: ScrollOnScrollCallback | undefined): void

设置[onDidScroll](#ZH-CN_TOPIC_0000002497444896__ondidscroll12)事件的回调。

方法入参为undefined时，会重置事件回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明callback[ScrollOnScrollCallback](Scroll.md#ZH-CN_TOPIC_0000002497444896__scrollonscrollcallback12) | undefined是onDidScroll事件的回调函数。

#### 示例

#### 示例1（设置scroller控制器）

该示例展示了Scroll组件部分属性和scroller控制器的使用。

```ets
// xxx.ets
import { curves } from '@kit.ArkUI';

@Entry
@Component
struct ScrollExample {
  scroller: Scroller = new Scroller();
  private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];

  build() {
    Stack({ alignContent: Alignment.TopStart }) {
      Scroll(this.scroller) {
        Column() {
          ForEach(this.arr, (item: number) => {
            Text(item.toString())
              .width('90%')
              .height(150)
              .backgroundColor(0xFFFFFF)
              .borderRadius(15)
              .fontSize(16)
              .textAlign(TextAlign.Center)
              .margin({ top: 10 })
          }, (item: number) => item.toString())
        }.width('100%')
      }
      .scrollable(ScrollDirection.Vertical) // 滚动方向纵向
      .scrollBar(BarState.On) // 滚动条常驻显示
      .scrollBarColor(Color.Gray) // 滚动条颜色
      .scrollBarWidth(10) // 滚动条宽度
      .friction(0.6)
      .edgeEffect(EdgeEffect.None)
      .onWillScroll((xOffset: number, yOffset: number, scrollState: ScrollState) => {
        console.info(xOffset + ' ' + yOffset);
      })
      .onScrollEdge((side: Edge) => {
        console.info('To the edge');
      })
      .onScrollStop(() => {
        console.info('Scroll Stop');
      })

      Button('scroll 150')
        .height('5%')
        .onClick(() => { // 点击后下滑指定距离150.0vp
          this.scroller.scrollBy(0, 150);
        })
        .margin({ top: 10, left: 20 })
      Button('scroll 100')
        .height('5%')
        .onClick(() => { // 点击后滑动到指定位置，即下滑100.0vp的距离
          const yOffset: number = this.scroller.currentOffset().yOffset;
          this.scroller.scrollTo({ xOffset: 0, yOffset: yOffset + 100 });
        })
        .margin({ top: 60, left: 20 })
      Button('scroll 100')
        .height('5%')
        .onClick(() => { // 点击后滑动到指定位置，即下滑100.0vp的距离，滑动过程配置有动画
          let curve = curves.interpolatingSpring(10, 1, 228, 30); //创建一个弹簧曲线
          const yOffset: number = this.scroller.currentOffset().yOffset;
          this.scroller.scrollTo({ xOffset: 0, yOffset: yOffset + 100, animation: { duration: 1000, curve: curve } });
        })
        .margin({ top: 110, left: 20 })
      Button('back top')
        .height('5%')
        .onClick(() => { // 点击后回到顶部
          this.scroller.scrollEdge(Edge.Top);
        })
        .margin({ top: 160, left: 20 })
      Button('next page')
        .height('5%')
        .onClick(() => { // 点击后滑到下一页
          this.scroller.scrollPage({ next: true ,animation: true });
        })
        .margin({ top: 210, left: 20 })
      Button('fling -3000')
        .height('5%')
        .onClick(() => { // 点击后触发初始速度为-3000vp/s的惯性滚动
          this.scroller.fling(-3000);
        })
        .margin({ top: 260, left: 20 })
      Button('scroll to bottom 700')
        .height('5%')
        .onClick(() => { // 点击后滑到下边缘，速度值是700vp/s
          this.scroller.scrollEdge(Edge.Bottom, { velocity: 700 });
        })
        .margin({ top: 310, left: 20 })
    }.width('100%').height('100%').backgroundColor(0xDCDCDC)
  }
}
```

#### 示例2（嵌套滚动实现方式一）

该示例使用onScrollFrameBegin事件实现了内层List组件和外层Scroll组件的嵌套滚动。

```ets
import { LengthMetrics } from '@kit.ArkUI';

@Entry
@Component
struct NestedScroll {
  @State listPosition: number = 0; // 0代表滚动到List顶部，1代表中间值，2代表滚动到List底部。
  private arr: number[] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
  private scrollerForScroll: Scroller = new Scroller();
  private scrollerForList: Scroller = new Scroller();

  build() {
    Flex() {
      Scroll(this.scrollerForScroll) {
        Column() {
          Text('Scroll Area')
            .width('100%')
            .height('40%')
            .backgroundColor(0X330000FF)
            .fontSize(16)
            .textAlign(TextAlign.Center)
            .onClick(() => {
              this.scrollerForList.scrollToIndex(5, false, ScrollAlign.START, { extraOffset: LengthMetrics.vp(5) });
            })

          List({ space: 20, scroller: this.scrollerForList }) {
            ForEach(this.arr, (item: number) => {
              ListItem() {
                Text('ListItem' + item)
                  .width('100%')
                  .height('100%')
                  .borderRadius(15)
                  .fontSize(16)
                  .textAlign(TextAlign.Center)
                  .backgroundColor(Color.White)
              }.width('100%').height(100)
            }, (item: string) => item)
          }
          .width('100%')
          .height('50%')
          .edgeEffect(EdgeEffect.None)
          .friction(0.6)
          .onReachStart(() => {
            this.listPosition = 0;
          })
          .onReachEnd(() => {
            this.listPosition = 2;
          })
          .onScrollFrameBegin((offset: number) => {
            if ((this.listPosition == 0 && offset <= 0) || (this.listPosition == 2 && offset >= 0)) {
              this.scrollerForScroll.scrollBy(0, offset);
              return { offsetRemain: 0 };
            }
            this.listPosition = 1;
            return { offsetRemain: offset };
          })

          Text('Scroll Area')
            .width('100%')
            .height('40%')
            .backgroundColor(0X330000FF)
            .fontSize(16)
            .textAlign(TextAlign.Center)
        }
      }
      .width('100%').height('100%')
    }.width('100%').height('100%').backgroundColor(0xDCDCDC).padding(20)
  }
}
```

#### 示例3（嵌套滚动实现方式二）

该示例使用[nestedScroll](#ZH-CN_TOPIC_0000002497444896__nestedscroll10)属性实现了内层List组件和外层Scroll组件的嵌套滚动。

```ets
@Entry
@Component
struct StickyNestedScroll {
  @State arr: number[] = [];

  @Styles
  listCard() {
    .backgroundColor(Color.White)
    .height(72)
    .width('100%')
    .borderRadius(12)
  }

  build() {
    Scroll() {
      Column() {
        Text('Scroll Area')
          .width('100%')
          .height('40%')
          .backgroundColor('#0080DC')
          .textAlign(TextAlign.Center)
        Tabs({ barPosition: BarPosition.Start }) {
          TabContent() {
            List({ space: 10 }) {
              ForEach(this.arr, (item: number) => {
                ListItem() {
                  Text('item' + item)
                    .fontSize(16)
                }.listCard()
              }, (item: number) => item.toString())
            }.width('100%')
            .edgeEffect(EdgeEffect.Spring)
            .nestedScroll({
              scrollForward: NestedScrollMode.PARENT_FIRST,
              scrollBackward: NestedScrollMode.SELF_FIRST
            })
          }.tabBar('Tab1')

          TabContent() {
          }.tabBar('Tab2')
        }
        .vertical(false)
        .height('100%')
      }.width('100%')
    }
    .edgeEffect(EdgeEffect.Spring)
    .friction(0.6)
    .backgroundColor('#DCDCDC')
    .scrollBar(BarState.Off)
    .width('100%')
    .height('100%')
  }

  aboutToAppear() {
    for (let i = 0; i < 30; i++) {
      this.arr.push(i);
    }
  }
}
```

#### 示例4（嵌套滚动父组件向子组件传递滚动）

该示例使用[enableScrollInteraction](#ZH-CN_TOPIC_0000002497444896__enablescrollinteraction10)属性和[onScrollFrameBegin](#ZH-CN_TOPIC_0000002497444896__onscrollframebegin9)事件实现了父组件向子组件传递滚动。

```ets
@Entry
@Component
struct NestedScroll {
  private headerHeight: number = 0;
  private arr: number[] = [];
  private scrollerForParent: Scroller = new Scroller();
  private scrollerForChild: Scroller = new Scroller();

  aboutToAppear(): void {
    for (let i = 0; i < 10; i++) {
      this.arr.push(i);
    }
  }

  build() {
    Scroll(this.scrollerForParent) {
      Column() {
        Text('Scroll Area')
          .width('100%')
          .height('40%')
          .backgroundColor(0X330000FF)
          .fontSize(16)
          .textAlign(TextAlign.Center)
          .onClick(() => {
            this.scrollerForChild.scrollToIndex(5);
          })
          .onSizeChange((oldValue: SizeOptions, newValue: SizeOptions) => {
            this.headerHeight = newValue.height! as number;
          })
        List({ space: 20, scroller: this.scrollerForChild }) {
          ForEach(this.arr, (item: number) => {
            ListItem() {
              Text('ListItem' + item)
                .width('100%')
                .height('100%')
                .borderRadius(15)
                .fontSize(16)
                .textAlign(TextAlign.Center)
                .backgroundColor(Color.White)
            }.width('100%').height(100)
          }, (item: number) => item.toString())
        }
        .width('100%')
        .height('100%')
        .edgeEffect(EdgeEffect.None)
        .scrollBar(BarState.Off)
        .enableScrollInteraction(false)

        Text('Scroll Area')
          .width('100%')
          .height('40%')
          .backgroundColor(0X330000FF)
          .fontSize(16)
          .textAlign(TextAlign.Center)
      }
    }
    .scrollBar(BarState.Off)
    .edgeEffect(EdgeEffect.Spring)
    .onScrollFrameBegin((offset: number, state: ScrollState) => {
      let retOffset = offset;
      let currOffset = this.scrollerForParent.currentOffset().yOffset;
      let newOffset = currOffset + offset;
      if (offset > 0) {
        if (this.scrollerForChild.isAtEnd()) {
          return { offsetRemain: offset };
        }
        if (newOffset > this.headerHeight) {
          retOffset = this.headerHeight - currOffset;
        }
        this.scrollerForChild.scrollBy(0, offset - retOffset);
      } else {
        if (this.scrollerForChild.currentOffset().yOffset <= 0) {
          return { offsetRemain: offset };
        }
        if (newOffset < this.headerHeight) {
          retOffset = this.headerHeight - currOffset;
        }
        this.scrollerForChild.scrollBy(0, offset - retOffset);
      }
      return { offsetRemain: retOffset };
    })
    .width('100%')
    .height('100%')
    .backgroundColor(0xDCDCDC)
  }
}
```

#### 示例5（设置限位滚动）

该示例实现了Scroll组件的限位滚动。

```ets
@Entry
@Component
struct Index {
  scroller: Scroller = new Scroller();
  private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15];
  build() {
    Scroll(this.scroller) {
      Column() {
        ForEach(this.arr, (item: number) => {
          Text(item.toString())
            .width('90%')
            .height(200)
            .backgroundColor(0xFFFFFF)
            .borderWidth(1)
            .borderColor(Color.Black)
            .borderRadius(15)
            .fontSize(16)
            .textAlign(TextAlign.Center)
        }, (item: number) => item.toString())
      }.width('100%').backgroundColor(0xDCDCDC)
    }
    .backgroundColor(Color.Yellow)
    .height('100%')
    .edgeEffect(EdgeEffect.Spring)
    .scrollSnap({snapAlign:ScrollSnapAlign.START, snapPagination:400, enableSnapToStart:true, enableSnapToEnd:true})
  }
}
```

#### 示例6（获取子组件索引）

该示例展示了如何获得List组件的子组件索引。

```ets
// xxx.ets
@Entry
@Component
struct ListExample {
  private arr: number[] = [];
  private scroller: ListScroller = new ListScroller();
  @State listSpace: number = 10;
  @State listChildrenSize: ChildrenMainSize = new ChildrenMainSize(100);
  @State listIndex: number = -1;
  @State itemBackgroundColorArr: boolean[] = [false];
  aboutToAppear(){
    // 初始化数据源。
    for (let i = 0; i < 10; i++) {
      this.arr.push(i);
    }
    this.listChildrenSize.splice(0, 5, [100, 100, 100, 100, 100]);
  }
  build() {
    Column() {
      List({ space: this.listSpace, initialIndex: 4, scroller: this.scroller }) {
        ForEach(this.arr, (item: number) => {
          ListItem() {
            Text('item-' + item)
              .height( item < 5 ? 100 : this.listChildrenSize.childDefaultSize)
              .width('90%')
              .fontSize(16)
              .textAlign(TextAlign.Center)
              .borderRadius(10)
              .backgroundColor( this.itemBackgroundColorArr[item] ? 0x68B4FF: 0xFFFFFF)
          }
        }, (item: number) => item.toString())
      }
      .backgroundColor(Color.Gray)
      .layoutWeight(1)
      .scrollBar(BarState.On)
      .childrenMainSize(this.listChildrenSize)
      .alignListItem(ListItemAlign.Center)
      .gesture(
        PanGesture()
          .onActionUpdate((event: GestureEvent) => {
            if (event.fingerList[0] != undefined && event.fingerList[0].localX != undefined && event.fingerList[0].localY != undefined) {
              this.listIndex = this.scroller.getItemIndex(event.fingerList[0].localX, event.fingerList[0].localY);
              this.itemBackgroundColorArr[this.listIndex] = true;
            }
          })
      )
      .gesture(
        TapGesture({ count: 1 })
          .onAction((event: GestureEvent) => {
            if (event) {
              this.itemBackgroundColorArr.splice(0,this.itemBackgroundColorArr.length);
            }
          })
      )

      Text('您当前位置Item索引为：'+ this.listIndex)
        .fontColor(Color.Red)
        .height(50)
    }
  }
}
```

#### 示例7（设置边缘渐隐）

该示例实现了Scroll组件开启边缘渐隐效果并设置边缘渐隐长度。

```ets
// xxx.ets
import { LengthMetrics } from '@kit.ArkUI';
@Entry
@Component
struct ScrollExample {
  scroller: Scroller = new Scroller();
  private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12];

  build() {
    Stack({ alignContent: Alignment.TopStart }) {
      Scroll(this.scroller) {
        Column() {
          ForEach(this.arr, (item: number) => {
            Text(item.toString())
              .width('90%')
              .height(150)
              .backgroundColor(0xFFFFFF)
              .borderRadius(15)
              .fontSize(16)
              .textAlign(TextAlign.Center)
              .margin({ top: 10 })
          }, (item: string) => item)
        }.width('100%')
      }
      .fadingEdge(true,{fadingEdgeLength:LengthMetrics.vp(80)})

    }.width('100%').height('100%').backgroundColor(0xDCDCDC)
  }
}
```

#### 示例8（单边边缘效果）

该示例通过[edgeEffect](#ZH-CN_TOPIC_0000002497444896__edgeeffect)接口，实现了Scroll组件设置单边边缘效果。

```ets
// xxx.ets
@Entry
@Component
struct ScrollExample {
  scroller: Scroller = new Scroller();
  private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12];

  build() {
    Stack({ alignContent: Alignment.TopStart }) {
      Scroll(this.scroller) {
        Column() {
          ForEach(this.arr, (item: number) => {
            Text(item.toString())
              .width('90%')
              .height(150)
              .backgroundColor(0xFFFFFF)
              .borderRadius(15)
              .fontSize(16)
              .textAlign(TextAlign.Center)
              .margin({ top: 10 })
          }, (item: string) => item)
        }.width('100%')
      }
      .edgeEffect(EdgeEffect.Spring,{alwaysEnabled:true,effectEdge:EffectEdge.START})
    }.width('100%').height('100%').backgroundColor(0xDCDCDC)
  }
}
```

#### 示例9（划动翻页效果）

该示例通过[enablePaging](#ZH-CN_TOPIC_0000002497444896__enablepaging11)接口，实现了Scroll组件滑动翻页效果。

```ets
// xxx.ets
@Entry
@Component
struct EnablePagingExample {
  private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

  build() {
    Stack({ alignContent: Alignment.Center }) {
      Scroll() {
        Column() {
          ForEach(this.arr, (item: number) => {
            Text(item.toString())
              .width('100%')
              .height('100%')
              .borderRadius(15)
              .fontSize(16)
              .textAlign(TextAlign.Center)
              .backgroundColor(0xFFFFFF)
          }, (item: number) => item.toString())
        }
      }.width('90%').height('90%')
      .enablePaging(true)
    }.width('100%').height('100%').backgroundColor(0xDCDCDC)
  }
}
```

#### 示例10（设置过界停留）

该示例通过[scrollTo](#ZH-CN_TOPIC_0000002497444896__scrollto)接口，实现了Scroll组件设置过界停留效果。

```ets
// xxx.ets
import { curves } from '@kit.ArkUI';

@Entry
@Component
struct StickyNestedScroll {
  scroller: Scroller = new Scroller;

  build() {
    Column() {
      Row() {
        Button('有动画scrollTo').onClick(() => {
          let curve = curves.interpolatingSpring(0.5, 5, 10, 15) //创建一个弹簧曲线
          const yOffset: number = this.scroller.currentOffset().yOffset;
          this.scroller.scrollTo({
            xOffset: 0,
            yOffset: yOffset - 100,
            animation: { duration: 1000, curve: curve, canOverScroll: true },
            canOverScroll: true
          })
        }).margin({ top: 10 })
        Button('无动画scrollTo').onClick(() => {
          const yOffset: number = this.scroller.currentOffset().yOffset;
          this.scroller.scrollTo({
            xOffset: 0,
            yOffset: yOffset - 100,
            animation: false,
            canOverScroll: true
          })
        }).margin({ top: 10, left: 20 })
      }.margin({ bottom: 20 })

      Scroll(this.scroller) {
        Column() {
          Text('Scroll Area')
            .width('100%')
            .height('100%')
            .backgroundColor('#0080DC')
            .textAlign(TextAlign.Center)
        }
        .width('100%')
        .height('100%')
      }
      .scrollable(ScrollDirection.Vertical)
      .edgeEffect(EdgeEffect.Spring) //设置边缘效果
      .fadingEdge(false) //关闭边缘渐隐效果
      .scrollBar(BarState.Auto)
      .friction(undefined)
      .backgroundColor('#DCDCDC')
      .width('100%')
      .height('50%')
    }
  }
}
```

#### 示例11（自由滚动和缩放）

从API version 20开始，该示例实现了Scroll组件自由滚动和缩放效果。

```ets
@Entry
@Component
struct ScrollZoomExample {
  @State currScale:number = 1;
  build() {
    Column() {
      Scroll() {
        Image($r('app.media.image1')) // 'app.media.image1'仅作示例，请替换实际图片。
      }
      .height(400)
      .scrollable(ScrollDirection.FREE)
      .minZoomScale(1)
      .maxZoomScale(2)
      .zoomScale(this.currScale!!)
      .enableBouncesZoom(true)
      .onDidZoom((scale: number) => {
        console.info(`onDidZoom:${scale}`);
      })
      .onZoomStart(() => {
        console.info('onZoomStart');
      })
      .onZoomStop(() => {
        console.info('onZoomStop');
      })
    }.width('100%').height('100%')
  }
}
```

#### 示例12（获取内容总大小）

从API version 22 开始，该示例实现了获取内容总大小的功能。

```ets
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct ScrollExample1 {
  scroller: Scroller = new Scroller();
  private arr: number[] = []

  aboutToAppear() {
    for (let j = 0; j < 10; j++) {
      this.arr.push(j);
    }
  }

  @State contentWidth: number = -1;
  @State contentHeight: number = -1;

  build() {
    Column() {
      Text('设置scroller控制器和ForEach')
      Row() {
        // 点击按钮来调用contentSize函数获取内容尺寸
        Button('GetContentSize')
          .onClick(() => {
            // Scroller未绑定组件时会抛异常，需要加上try catch保护
            try {
              // 通过调用contentSize函数获取内容尺寸的宽度值
              this.contentWidth = this.scroller.contentSize().width;
              // 通过调用contentSize函数获取内容尺寸的高度值
              this.contentHeight = this.scroller.contentSize().height;
            } catch (error) {
              let err: BusinessError = error as BusinessError;
                console.error(`Failed to get contentSize of the grid, code=${err.code}, message=${err.message}`);
            }
          })
        // 将获取到的内容尺寸信息通过文本进行呈现
        Text('Width：' + this.contentWidth + '，Height：' + this.contentHeight)
          .fontColor(Color.Red)
          .height(50)
      }

      Stack({ alignContent: Alignment.TopStart }) {
        Scroll(this.scroller) {
          Column() {
            ForEach(this.arr, (item: number) => {
              Text(item.toString())
                .width('90%')
                .height(150)
                .backgroundColor(0xFFFFFF)
                .borderRadius(15)
                .fontSize(16)
                .textAlign(TextAlign.Center)
                .margin({ top: 10 })
            }, (item: number) => item.toString())
          }.width('100%')
        }
        .scrollable(ScrollDirection.Vertical) // 滚动方向纵向
        .scrollBar(BarState.On) // 滚动条常驻显示
        .scrollBarColor(Color.Gray) // 滚动条颜色
        .scrollBarWidth(10) // 滚动条宽度
        .friction(0.6)
        .edgeEffect(EdgeEffect.None)
      }.width('100%').height('100%').backgroundColor(0xDCDCDC)
    }
  }
}
```

#### 示例13（设置滚动事件）

该示例通过FrameNode中的[getEvent('Scroll')](FrameNode.md#ZH-CN_TOPIC_0000002529284787__geteventscroll19)获取[UIScrollEvent](#ZH-CN_TOPIC_0000002497444896__uiscrollevent19)，并为Scroll设置滚动事件回调，用于事件监听方因无法直接修改页面代码而无法使用声明式接口设置回调的场景。

从API version 19开始，新增UIScrollEvent接口。

```ets
import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';

class MyNodeController extends NodeController {
  public rootNode: FrameNode | null = null;

  makeNode(uiContext: UIContext): FrameNode | null {
    this.rootNode = new FrameNode(uiContext);
    this.rootNode.commonAttribute.width(100);
    return this.rootNode;
  }

  addCommonEvent(frameNode: FrameNode) {
    // 获取Scroll事件
    let scrollEvent: UIScrollEvent | undefined = typeNode.getEvent(frameNode, 'Scroll');

    // 设置OnWillScroll事件
    scrollEvent?.setOnWillScroll((xOffset: number, yOffset: number, scrollState: ScrollState,
      scrollSource: ScrollSource) => {
      console.info('onWillScroll xOffset = ${xOffset}, yOffset = ${yOffset}, scrollState = ${scrollState}, scrollSource = ${scrollSource}');
    });

    // 设置OnDidScroll事件
    scrollEvent?.setOnDidScroll((scrollOffset: number, scrollState: ScrollState) => {
      console.info('onDidScroll scrollOffset = ${scrollOffset}, scrollState = ${scrollState}');
    });

    // 设置OnReachStart事件
    scrollEvent?.setOnReachStart(() => {
      console.info('onReachStart');
    });

    // 设置OnReachEnd事件
    scrollEvent?.setOnReachEnd(() => {
      console.info('onReachEnd');
    });

    // 设置OnScrollStart事件
    scrollEvent?.setOnScrollStart(() => {
      console.info('onScrollStart');
    });

    // 设置OnScrollStop事件
    scrollEvent?.setOnScrollStop(() => {
      console.info('onScrollStop');
    });

    // 设置OnScrollFrameBegin事件
    scrollEvent?.setOnScrollFrameBegin((offset: number, state: ScrollState) => {
      console.info('onScrollFrameBegin offset = ${offset}, state = ${state}');
      return undefined;
    });
  }
}

@Entry
@Component
struct Index {
  @State index: number = 0;
  private myNodeController: MyNodeController = new MyNodeController();
  @State numbers: string[] = [];

  aboutToAppear() {
    for (let i = 0; i < 30; i++) {
      this.numbers.push('${i+1}');
    }
  }

  build() {
    Column() {
      Button('add CommonEvent to Scroll')
        .onClick(() => {
          this.myNodeController!.addCommonEvent(this.myNodeController!.rootNode!.getParent()!.getPreviousSibling()!)
        })
      Scroll() {
        Column() {
          ForEach(this.numbers, (day: string, index: number) => {
            Column() {
              Text(day)
                .fontSize(16)
                .backgroundColor(0xF9CF93)
                .width('90%')
                .height(80)
                .textAlign(TextAlign.Center)
                .margin({ top: 10 })
            }
            .width('100%')
            .justifyContent(FlexAlign.Center)
            .alignItems(HorizontalAlign.Center)
          }, (day: string, index: number) => index.toString() + day)
        }
      }
      .scrollable(ScrollDirection.Vertical)
      .edgeEffect(EdgeEffect.Spring)
      .width('90%')
      .backgroundColor(0xFAEEE0)
      .height(300)
      NodeContainer(this.myNodeController)
    }
  }
}
```