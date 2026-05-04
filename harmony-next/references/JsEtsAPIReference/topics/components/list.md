# [List](list.md)

列表包含一系列相同宽度的列表项。适合连续、多行呈现同类数据，例如图片和文本。

List的懒加载是指组件按需加载可见区域可见的子组件。相比全量加载，使用懒加载可以提升应用启动速度，减少内存消耗。List和[ForEach](ForEach.md)、[LazyForEach](LazyForEach.md)、[Repeat](Repeat.md)结合，懒加载能力存在差异：

-

当[List](list.md)和ForEach结合，会一次性创建所有的子节点，在需要的时候布局和渲染屏幕范围内的节点。当用户滑动时，划出屏幕范围的节点不会下树销毁，划入屏幕范围的节点会布局和渲染。

-

当[List](list.md)和LazyForEach结合，会一次性创建、布局、渲染屏幕范围的节点。当用户滑动时，划出屏幕范围的节点会下树销毁，划入屏幕范围的节点会创建、布局、渲染。

-

当List和带[virtualScroll](Repeat.md#ZH-CN_TOPIC_0000002553360847__virtualscroll)的Repeat结合，它的懒加载行为和LazyForEach一致。当List和不带[virtualScroll](Repeat.md#ZH-CN_TOPIC_0000002497604972__virtualscroll)的Repeat结合，它的懒加载行为和ForEach一致。

如果可滚动组件嵌套List组件，并且滚动方向相同，List组件又没有设置主轴尺寸时，List组件会全量加载子组件，导致懒加载失效。该场景推荐使用List嵌套[ListItemGroup](ListItemGroup.md)组件以实现优化性能。

List的预加载是指除了加载显示区域可见区域外子组件外，还支持空闲时隙提前加载部分显示区域外不可见的子组件。使用预加载可以减少滚动丢帧，提升流畅性。预加载需要结合懒加载才会生效。List支持通过[cachedCount](#ZH-CN_TOPIC_0000002522240820__cachedcount)设置预加载的数量。默认会预加载显示区域上下各一屏子节点（最大预加载16行子节点）。List和[ForEach](ForEach.md)、[LazyForEach](LazyForEach.md)、[Repeat](Repeat.md)结合，预加载能力存在差异：

-

当[List](list.md)和ForEach结合，如果设置了cachedCount，除了会布局显示区域内子组件外，还会在空闲时隙预布局显示区域外cachedCount范围内的子节点。

-

当[List](list.md)和LazyForEach结合，如果设置了cachedCount，除了会创建和布局显示区域内子组件外，还会在空闲时隙预创建和预布局显示区域外cachedCount范围内的子节点。

-

当List和带[virtualScroll](Repeat.md#ZH-CN_TOPIC_0000002553360847__virtualscroll)的Repeat结合，它的预加载行为和LazyForEach一致。当List和不带[virtualScroll](Repeat.md#ZH-CN_TOPIC_0000002497604972__virtualscroll)的Repeat结合，它的预加载行为和ForEach一致。


该组件从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

组件内部已绑定手势实现跟手滚动等功能，需要增加自定义手势操作时请参考[手势拦截增强](手势拦截增强.md)进行处理。

#### 子组件

仅支持[ListItem](ListItem.md)、[ListItemGroup](ListItemGroup.md)子组件和自定义组件。自定义组件在List下使用时，建议使用ListItem或ListItemGroup作为自定组件的顶层组件，不建议给自定义组件设置属性和事件方法。

支持通过渲染控制类型（[if/else](../../guides/if-else：条件渲染.md)、[ForEach](ForEach.md)、[LazyForEach](LazyForEach.md)和[Repeat](Repeat.md)）动态生成子组件，更推荐使用LazyForEach或Repeat以优化性能。

如果在处理大量子组件时遇到卡顿问题，请考虑采用懒加载、缓存列表项、动态预加载、组件复用和布局优化等方法来进行优化。最佳实践请参考[优化长列表加载慢丢帧问题](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-best-practices-long-list)。

从API version 21开始，[List](list.md)单个子组件的宽高最大为16777216px；API version 20及之前，List单个子组件的宽高最大为1000000px。子组件超出该大小可能导致滚动或显示异常。

[List](list.md)的子组件的索引值计算规则：

-

按子组件的顺序依次递增。

-

if/else语句中，只有条件成立的分支内的子组件会参与索引值计算，条件不成立的分支内子组件不计算索引值。

-

ForEach/LazyForEach/Repeat语句中，会计算展开所有子节点索引值。

-

[if/else](../../guides/if-else：条件渲染.md)、[ForEach](ForEach.md)、[LazyForEach](LazyForEach.md)和[Repeat](Repeat.md)发生变化以后，会更新子节点索引值。

-

[List](list.md)ItemGroup作为一个整体计算一个索引值，ListItemGroup内部的ListItem不计算索引值。

-

[List](list.md)子组件visibility属性设置为Hidden或None依然会计算索引值。

#### 接口

List(options?: [ListOptions](#ZH-CN_TOPIC_0000002522240820__listoptions18对象说明))

创建[List](list.md)列表容器。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [List](list.md)Options | 否 | 设置List组件参数。 |

#### [List](list.md)Options18+对象说明

用于设置[List](list.md)组件参数。

为规范匿名对象的定义，API 18版本修改了此处的元素定义。其中，保留了历史匿名对象的起始版本信息，会出现外层元素@since版本号高于内层元素版本号的情况，但这不影响接口的使用。

**卡片能力：** 从API version 18开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| initialIndex7+ | number | 否 | 是 | 设置当前[List](list.md)初次加载时显示区域起始位置的item索引值。 默认值：0 说明： 设置为负数或超过了当前List最后一个item的索引值时视为无效取值，无效取值按默认值显示。 从API version 14开始，如果在List组件创建完成后首次布局前（如List的[onAttach](挂载卸载事件.md#ZH-CN_TOPIC_0000002529284813__onattach12)事件中），调用[Scroller]([Scroll](Scroll.md).md#ZH-CN_TOPIC_0000002497444896__scroller)滚动控制器中不带动画的[scrollToIndex](Scroll.md#ZH-CN_TOPIC_0000002497444896__scrolltoindex)或scrollEdge方法，会覆盖initialIndex设置的值。 设置了initialIndex后，List从initialIndex对应的子组件开始布局，在这之前的子组件未参与布局，无法计算准确大小，因此通过[currentOffset](Scroll.md#ZH-CN_TOPIC_0000002497444896__currentoffset)接口获取到的List的滚动总偏移量通过估算得出，可能会有误差。可通过设置childrenMainSize确保List的滚动总偏移量的准确性。 卡片能力： 从API version 9开始，该接口支持在ArkTS卡片中使用。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| space7+ | number | string | 否 | 是 | 子组件主轴方向的间隔。 默认值：0 参数类型为number时单位为vp。 说明： 设置为负数或者大于等于[List](list.md)内容区长度时，按默认值显示。 space参数值小于List分割线宽度时，子组件主轴方向的间隔取分割线宽度。 List子组件的visibility属性设置为None时不显示，但该子组件上下的space还是会生效。 卡片能力： 从API version 9开始，该接口支持在ArkTS卡片中使用。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| scroller7+ | Scroller | 否 | 是 | 可滚动组件的控制器。与List绑定后，可以通过它控制List的滚动。 说明： 不允许和其他滚动类组件，如：[ArcList](ArcList.md)、List、[Grid](Grid.md)、Scroll和[WaterFlow](WaterFlow.md)绑定同一个滚动控制对象。 卡片能力： 从API version 9开始，该接口支持在ArkTS卡片中使用。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |

#### 属性

除支持[通用属性](通用属性.md)和[滚动组件通用属性](滚动组件通用接口.md#ZH-CN_TOPIC_0000002522240828__属性)外，还支持以下属性：


List组件通用属性[clip](形状裁剪.md#ZH-CN_TOPIC_0000002522240784__clip12)的默认值为true。

#### listDirection

listDirection(value: [Axis](枚举说明.md#ZH-CN_TOPIC_0000002529284967__axis))

设置[List](list.md)组件排列方向。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Axis](枚举说明.md#ZH-CN_TOPIC_0000002529284967__axis) | 是 | 组件的排列方向。 默认值：Axis.Vertical |

#### divider

divider(value: [ListDividerOptions](#ZH-CN_TOPIC_0000002522240820__listdivideroptions18对象说明) | null)

设置[List](list.md)Item分割线样式，默认无分割线。

[List](list.md)的分割线画在主轴方向两个子组件之间，第一个子组件上方和最后一个子组件下方不会绘制分割线。

多列模式下，[List](list.md)Item与ListItem之间的分割线起始边距从每一列的交叉轴方向起始边开始计算，单列模式从List交叉轴方向起始边开始计算。

ListItem设置[多态样式](多态样式.md)时，被按压的子组件上下的分割线不绘制。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [List](list.md)DividerOptions | null | 是 | ListItem分割线样式。 默认值：null |

#### scrollBar

scrollBar(value: [BarState](枚举说明.md#ZH-CN_TOPIC_0000002529284967__barstate))

设置滚动条状态。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [BarState](枚举说明.md#ZH-CN_TOPIC_0000002529284967__barstate) | 是 | 滚动条状态。 默认值：API version 9及以下版本默认值为BarState.Off，API version 10及以上版本的默认值为BarState.Auto。 |

#### cachedCount

cachedCount(value: number)

设置列表中[List](list.md)Item/ListItemGroup的预加载数量，懒加载场景只会预加载List显示区域外上下各cachedCount行的ListItem，非懒加载场景会全部加载。懒加载、非懒加载都只布局List显示区域+List显示区域外cachedCount的内容。

[List](list.md)设置cachedCount后，显示区域外上下各会预加载并布局cachedCount行ListItem。计算ListItem行数时，会计算ListItemGroup内部的ListItem行数。如果ListItemGroup内没有ListItem，则整个ListItemGroup算一行。

[List](list.md)下嵌套使用LazyForEach，并且LazyForEach下嵌套使用ListItemGroup时，LazyForEach会在List显示区域外上下各会创建cachedCount个ListItemGroup。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | [List](list.md)Item/ListItemGroup的预加载数量。 默认值：根据屏幕内显示的节点个数设置，最大值为16。 取值范围：[0, +∞) |

#### cachedCount14+

cachedCount(count: number, show: boolean)

设置列表中[List](list.md)Item/ListItemGroup的预加载数量，并配置是否显示预加载节点。

List设置cachedCount后，显示区域外上下各会预加载并布局cachedCount行ListItem。计算ListItem行数时，会计算ListItemGroup内部的ListItem行数。如果ListItemGroup内没有ListItem，则整个ListItemGroup算一行。配合[裁剪](形状[裁剪](形状裁剪.md#ZH-CN_TOPIC_0000002529284827__clip12).md#ZH-CN_TOPIC_0000002522240784__clip12)或[内容裁剪](滚动组件通用接口.md#ZH-CN_TOPIC_0000002522240828__clipcontent14)属性可以显示出预加载节点。


通常建议设置cachedCount=n/2（n代表一屏显示的列表项数量），同时需考虑其他因素以实现体验和内存使用的平衡。最佳实践请参考[优化长列表加载慢丢帧问题-缓存列表项](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-best-practices-long-list#section11667144010222)。

**卡片能力：** 从API version 14开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| count | number | 是 | 预加载的[List](list.md)Item的数量。 默认值：根据屏幕内显示的节点个数设置，最大值为16。 取值范围：[0, +∞) |
| show | boolean | 是 | 被预加载的[List](list.md)Item是否需要显示。设置为true时显示预加载的ListItem，设置为false时不显示预加载的ListItem。 默认值：false |

#### cachedCount22+

cachedCount(count: number | [CacheCountInfo](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__cachecountinfo22对象说明), show: boolean)

设置列表中[List](list.md)Item/ListItemGroup的预加载数量，并配置是否显示预加载节点。

若cachedCount属性的第一个参数为number类型，在帧间空闲时隙会在显示区域外上下各预加载并布局count行[List](list.md)Item。

若cachedCount属性的第一个参数为CacheCountInfo类型，当已缓存行数小于CacheCountInfo.minCount时，会在帧间空闲时隙预加载和布局。当已缓存行数大于CacheCountInfo.maxCount时，会将超出范围的节点销毁或回收复用。UI空闲时（无动画或用户操作），会在显示区域外上下各预加载CacheCountInfo.maxCount行[List](list.md)Item。

在计算ListItem行数时，会计算ListItemGroup内部的ListItem行数。如果ListItemGroup内没有ListItem，则整个ListItemGroup算一行。配合[clip](形状裁剪.md#ZH-CN_TOPIC_0000002522240784__[clip](形状裁剪.md#ZH-CN_TOPIC_0000002529284827__clip12)12)或[clipContent](滚动组件通用接口.md#ZH-CN_TOPIC_0000002522240828__clipcontent14)属性可以显示出预加载节点。

默认行为：count参数默认为number类型，数值根据屏幕内显示的节点个数设置，最大值为16。预加载的[List](list.md)Item默认不参与绘制。

通常建议设置cachedCount=n/2（n代表一屏显示的列表项数量），同时需考虑其他因素以实现体验和内存使用的平衡。从API version 22开始，支持设置最大最小缓存数，可以将最大缓存数设置稍大，如设置为最小缓存数的两倍，利用UI线程空闲时间创建节点，减少滚动过程中预加载创建节点，提升滚动流畅性。最佳实践请参考[优化长列表加载慢丢帧问题-缓存列表项](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-best-practices-long-list#section11667144010222)。

**卡片能力：** 从API version 22开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| count | number | [CacheCountInfo](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__cachecountinfo22对象说明) | 是 | 当参数类型为number时，表示预加载的ListItem的数量。 取值范围：[0, +∞) 当参数类型为CacheCountInfo时，表示预加载的最大最小范围。 |
| show | boolean | 是 | 被预加载的[List](list.md)Item是否需要显示。 true：显示预加载的ListItem。 false：不显示预加载的ListItem。 |

#### edgeEffect

edgeEffect(value: [EdgeEffect](枚举说明.md#ZH-CN_TOPIC_0000002529284967__edgeeffect), options?: EdgeEffectOptions)

设置边缘滑动效果。

当[List](list.md)组件的内容区小于一屏时，默认没有回弹效果。若要启用回弹效果，可以通过设置edgeEffect属性的options参数为{ alwaysEnabled: true }来实现。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [EdgeEffect](枚举说明.md#ZH-CN_TOPIC_0000002529284967__edgeeffect) | 是 | List组件的边缘滑动效果，支持弹簧效果和阴影效果。 默认值：EdgeEffect.Spring |
| options11+ | [EdgeEffectOptions](滚动组件通用接口.md#ZH-CN_TOPIC_0000002529284871__edgeeffectoptions11对象说明) | 否 | 组件内容大小小于组件自身时，是否开启滑动效果。设置为{ alwaysEnabled: true }会开启滑动效果，{ alwaysEnabled: false }不开启。 默认值：{ alwaysEnabled: false } |

#### chainAnimation

chainAnimation(value: boolean)

设置当前[List](list.md)是否启用链式联动动效。

- 链式联动效果是指在手指划动过程中，手指拖动的[List](list.md)Item是主动对象，相邻的ListItem为从动对象，主动对象驱动从动对象联动，驱动效果遵循弹簧物理动效。
- 链式动效的驱动效果体现在[List](list.md)Item之间的间距上。静止状态下的间距可以通过List组件space参数设置，如果不设置space参数并且启用了链式动效，该间距默认为20vp。
- 链式动效启用后，[List](list.md)的分割线不显示。
- 链式动效生效的前提是[List](list.md)处于单列模式并且边缘效果为EdgeEffect.Spring类型。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 是否启用链式联动动效。 默认值：false，不启用链式联动。true，启用链式联动。 |

#### multiSelectable8+

multiSelectable(value: boolean)

设置是否开启鼠标框选。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 是否开启鼠标框选。 默认值：false，关闭框选。true，开启框选。 |

#### lanes9+

lanes(value: number | [LengthConstrain](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__lengthconstrain), gutter?: Dimension)

设置[List](list.md)组件的布局列数或行数（List垂直滚动时表示列数，水平滚动时表示行数）。

以列数作为示例，介绍设置规则如下：

- value为number类型时，根据number类型数值指定列数。

- value为LengthConstrain类型时，LengthConstrain中的minLength表示最小列宽，[List](list.md)组件会根据自身宽度在满足最小列宽情况下计算最大列数。同时，LengthConstrain会作为最大最小布局宽度约束传递给List的子组件，子组件没有设置宽度时会生效该最大最小布局约束。

- [List](list.md)ItemGroup在多列模式下也是独占一行，ListItemGroup中的ListItem按照List组件的lanes属性设置值来布局。

- value为LengthConstrain类型时，计算[List](list.md)ItemGroup中的列数时会按照ListItemGroup的自身宽度计算。因此ListItemGroup宽度与List宽度不一致时，ListItemGroup中的列数与List中的列数可能不一样。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | [LengthConstrain](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__lengthconstrain) | 是 | List组件的布局列数或行数。 默认值：1 取值范围：[1, +∞) |
| gutter10+ | [Dimension](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__dimension10) | 否 | 列间距或行间距。 默认值：0 取值范围：[0, +∞) 说明： gutter为列间距或行间距，当列数或行数大于1时生效。 |

#### lanes22+

lanes(value: number | [LengthConstrain](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__lengthconstrain) | ItemFillPolicy, gutter?: Dimension)

设置[List](list.md)组件布局列的数量和列的间距，默认按固定一列显示。

**卡片能力：** 从API version 22开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | [LengthConstrain](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__lengthconstrain) | [ItemFillPolicy](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__itemfillpolicy22) | 是 | 当前List组件布局列的数量。 设置为number类型时，根据number类型的数值确定列数，number类型取值范围：[1, +∞)。 设置为LengthConstrain类型时，根据LengthConstrain中的最大最小值确定列数。 设置为ItemFillPolicy类型时，根据List组件宽度对应断点类型确定列数，该类型只在List滚动方向为垂直方向时才生效。 |
| gutter | [Dimension](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__dimension10) | 否 | 列间距。 默认值：0 取值范围：[0, +∞) |

#### align[List](list.md)Item9+

align[List](list.md)Item(value: ListItemAlign)

设置[List](list.md)交叉轴方向宽度大于ListItem交叉轴宽度 * lanes + (lanes - 1) * gutter时，ListItem在List交叉轴方向的布局方式。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [List](list.md)ItemAlign | 是 | 交叉轴方向的布局方式。 默认值：ListItemAlign.Start |

#### sticky9+

sticky(value: StickyStyle)

配合[ListItemGroup](ListItemGroup.md)组件使用，设置ListItemGroup中header是否要吸顶或footer是否要吸底。sticky属性可以设置为 StickyStyle.Header | StickyStyle.Footer 以同时支持header吸顶和footer吸底。从API version 20开始，sticky属性也可以设置为StickyStyle.BOTH，以同时支持header吸顶和footer吸底。


由于浮点数计算精度，设置sticky后，在List滑动过程中小概率产生缝隙，可以通过[pixelRound](组件级像素取整.md#ZH-CN_TOPIC_0000002522240780__pixelround)指定当前组件向下像素取整解决该问题。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | StickyStyle | 是 | [List](list.md)ItemGroup吸顶或吸底效果。 默认值：StickyStyle.None |

#### scrollSnapAlign10+

scrollSnapAlign(value: [Scroll](Scroll.md)SnapAlign)

设置列表项滚动结束对齐效果。

只支持item等高场景限位，不等高场景可能存在不准确的情况。对齐动画期间[onWillScroll](滚动组件通用接口.md#ZH-CN_TOPIC_0000002522240828__onwillscroll12)事件上报的滚动操作来源类型为ScrollSource.FLING。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Scroll](Scroll.md)SnapAlign | 是 | 列表项滚动结束对齐效果。 默认值：ScrollSnapAlign.NONE |

#### scrollSnapAnimationSpeed22+

scrollSnapAnimationSpeed(speed: [Scroll](Scroll.md)SnapAnimationSpeed)

设置列表项滚动限位动画速度。只在列表设置了滚动结束对齐效果后才生效。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| speed | [Scroll](Scroll.md)SnapAnimationSpeed | 是 | 列表滚动限位动画速度。 默认值：ScrollSnapAnimationSpeed.NORMAL |

#### enable[Scroll](Scroll.md)Interaction10+

enable[Scroll](Scroll.md)Interaction(value: boolean)

设置是否支持滚动手势。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 是否支持滚动手势。设置为true时可以通过手指或者鼠标滚动，设置为false时无法通过手指或者鼠标滚动，但不影响控制器[Scroller](Scroll.md#ZH-CN_TOPIC_0000002497444896__scroller)的滚动接口。 默认值：true |


组件无法通过鼠标按下拖动操作进行滚动。

#### nested[Scroll](Scroll.md)10+

nestedScroll(value: [NestedScrollOptions](滚动组件通用接口.md#ZH-CN_TOPIC_0000002529284871__nestedscrolloptions10对象说明))

设置前后两个方向的嵌套滚动模式，实现与父组件的滚动联动。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [NestedScrollOptions](滚动组件通用接口.md#ZH-CN_TOPIC_0000002529284871__nestedscrolloptions10对象说明) | 是 | 嵌套滚动选项。 默认值：{ scrollForward: NestedScrollMode.SELF_ONLY, scrollBackward: NestedScrollMode.SELF_ONLY } |

#### friction10+

friction(value: number | [Resource](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resource))

设置摩擦系数，手动划动滚动区域时生效，仅影响惯性滚动过程。设置为小于等于0的值时，按默认值处理。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | [Resource](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resource) | 是 | 摩擦系数。 默认值：非wearable设备为0.6，wearable设备为0.9。 从API version 11开始，非wearable设备默认值为0.7。 从API version 12开始，非wearable设备默认值为0.75。 |

#### contentStartOffset11+

contentStartOffset(value: number)

设置内容区域起始偏移量。列表滚动到起始位置时，列表内容与列表显示区域边界保留指定距离。

contentStartOffset + contentEndOffset超过[List](list.md)内容区长度后contentStartOffset和contentEndOffset会置0。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 内容区域起始偏移量。 默认值：0 单位：vp 说明： 设置为负数时，按默认值处理。 |

#### contentStartOffset22+

contentStartOffset(offset: number | [Resource](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resource))

设置内容区域起始偏移量。列表滚动到起始位置时，列表内容与列表显示区域边界保留指定距离。与[contentStartOffset11+](#ZH-CN_TOPIC_0000002522240820__contentstartoffset11)相比，参数名改为offset，并开始支持Resource类型。

contentStartOffset + contentEndOffset超过[List](list.md)内容区长度后contentStartOffset和contentEndOffset会置0。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| offset | number | [Resource](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resource) | 是 | 内容区域起始偏移量。 默认值：0 单位：vp 设置异常值如负数、非数字Resource时，按默认值处理。 |

#### contentEndOffset11+

contentEndOffset(value: number)

设置内容区末尾偏移量。列表滚动到末尾位置时，列表内容与列表显示区域边界保留指定距离。

contentStartOffset + contentEndOffset超过[List](list.md)内容区长度后contentStartOffset和contentEndOffset会置0。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 内容区末尾偏移量。 默认值：0 单位：vp 说明： 设置为负数时，按默认值处理。 |

#### contentEndOffset22+

contentEndOffset(offset: number | [Resource](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resource))

设置内容区末尾偏移量。列表滚动到末尾位置时，列表内容与列表显示区域边界保留指定距离。与[contentEndOffset11+](#ZH-CN_TOPIC_0000002522240820__contentendoffset11)相比，参数名改为offset，并开始支持Resource类型。

contentStartOffset + contentEndOffset超过[List](list.md)内容区长度后contentStartOffset和contentEndOffset会置0。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| offset | number | [Resource](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resource) | 是 | 内容区末尾偏移量。 默认值：0 单位：vp 设置异常值如负数、非数字Resource时，按默认值处理。 |

#### [childrenMainSize](ListItemGroup.md#ZH-CN_TOPIC_0000002497604872__childrenmainsize12)12+

[childrenMainSize](ListItemGroup.md#ZH-CN_TOPIC_0000002497604872__childrenmainsize12)(value: ChildrenMainSize)

设置[List](list.md)组件的子组件在主轴方向的大小信息。


- 该属性通过向List组件提供所有子组件在主轴方向的大小信息，确保在面对子组件主轴大小不一致、增删子组件、使用[scrollToIndex](Scroll.md#ZH-CN_TOPIC_0000002553360749__scrolltoindex)等场景时，List组件能够维护其滑动位置准确性。这样，[scrollTo](Scroll.md#ZH-CN_TOPIC_0000002553360749__scrollto)可以准确的跳转到指定位置，[currentOffset](Scroll.md#ZH-CN_TOPIC_0000002553360749__currentoffset)可以获取到当前准确的滑动位置，内置滚动条可以实现平滑移动无跳变。

- 当子组件是[List](list.md)ItemGroup时，需要根据ListItemGroup的列数、ListItemGroup中ListItem在主轴方向的间距以及ListItemGroup中header、footer和ListItem的大小，来准确计算出ListItemGroup在主轴方向的整体大小，并传递给List组件。

- 如果子组件有ListItemGroup，必须为每一个ListItemGroup设置[childrenMainSize](ListItemGroup.md#ZH-CN_TOPIC_0000002522080824__childrenmainsize12)属性。List组件和每一个ListItemGroup组件都要通过[childrenMainSize](ListItemGroup.md#ZH-CN_TOPIC_0000002497604872__childrenmainsize12)属性接口一对一绑定一个ChildrenMainSize对象。

- 多列场景使用LazyForEach生成子组件时，需确保LazyForEach全部生成[List](list.md)ItemGroup组件或者全部生成ListItem组件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ChildrenMainSize](滚动组件通用接口.md#ZH-CN_TOPIC_0000002529284871__childrenmainsize12对象说明) | 是 | 该对象用来维护子组件在主轴方向的大小信息。 |

#### maintainVisibleContentPosition12+

maintainVisibleContentPosition(enabled: boolean)

设置显示区域上方插入或删除数据时是否要保持可见内容位置不变。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean | 是 | 设置显示区域上方插入或删除数据时是否要保持可见内容位置不变。 默认值：false，显示区域上方插入或删除数据时可见内容位置会跟随变化。 true：显示区域上方插入或删除数据时可见内容位置不变。 |


- 只有使用LazyForEach在显示区域外插入或删除数据时，属性设置为true才能保持可见内容位置不变。使用ForEach插入或删除数据、使用LazyForEach重新加载数据时，即使maintainVisibleContentPosition属性设置为true，可见区内容位置也会跟随变化。
- 从API version 20开始，使用[Repeat](Repeat.md)在懒加载场景下，显示区域外插入或删除数据时，属性设置为true也能保持可见内容位置不变。

- maintainVisibleContentPosition属性设置为true后，在显示区域上方插入或删除数据，会触发[onDidScroll](滚动组件通用接口.md#ZH-CN_TOPIC_0000002522240828__ondidscroll12)、onScrollIndex事件。

- maintainVisibleContentPosition属性设置为true后，在多列场景下，一次插入或删除整行数据，可以保持可见内容位置不变，如果不是插入或删除整行数据，可见内容位置还是会发生变化。

#### stackFromEnd19+

stackFromEnd(enabled: boolean)

设置[List](list.md)组件是否从末尾开始布局。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean | 是 | 设置[List](list.md)组件是否从末尾开始布局。 默认值：false，List从顶部开始布局。 true：List组件从末尾开始布局。 |


- stackFromEnd属性设置为true后，当[List](list.md)内容小于List组件高度时，内容底部对齐。
- stackFromEnd属性设置为true后，显示区域内有[List](list.md)Item变高，或有插入ListItem，内容上方的ListItem往上移动。

- stackFromEnd属性设置为true后，[ListOptions](#ZH-CN_TOPIC_0000002522240820__listoptions18对象说明)中initialIndex参数默认值为总item个数-1。

#### focusWrapMode20+

focusWrapMode(mode: [Optional](自定义属性设置.md#ZH-CN_TOPIC_0000002529284845__optionalt12)<FocusWrapMode>)

设置方向键走焦模式。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [Optional](自定义属性设置.md#ZH-CN_TOPIC_0000002529284845__optionalt12)<[FocusWrapMode](枚举说明.md#ZH-CN_TOPIC_0000002529284967__focuswrapmode20)> | 是 | 交叉轴方向键走焦模式。 默认值：FocusWrapMode.DEFAULT 说明： 异常值按默认值处理，即交叉轴方向键不能换行。 |

#### syncLoad20+

syncLoad(enable: boolean)

设置是否同步加载[List](list.md)区域内所有子组件。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | boolean | 是 | 是否同步加载[List](list.md)区域内所有子组件。 true表示同步加载，false表示异步加载。默认值：true。 说明： 设置为false时，在首次显示、不带动画scrollToIndex跳转场景，若当帧布局耗时超过50ms，会将List区域内尚未布局的子组件延后到下一帧进行布局。 |

**editModeOptions23+**

editModeOptions(options?: EditModeOptions)

配置编辑模式选项参数。

元服务API： 从API version 23开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | EditModeOptions | 否 | 编辑模式选项。 |

#### editMode(deprecated)

editMode(value: boolean)

设置当前List组件是否处于可编辑模式。可参考[示例3](#ZH-CN_TOPIC_0000002522240820__示例3设置编辑模式)实现删除选中的list项。


从API version 7开始支持，从API version 9开始废弃，无替代接口。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 当前[List](list.md)组件是否处于可编辑模式。 默认值：false，当前List组件不处于可编辑模式。 |

**supportEmptyBranchInLazyLoading23+**

supportEmptyBranchInLazyLoading(supported: boolean | undefined)

设置当前[List](list.md)组件是否支持在LazyForEach或Repeat中使用if/else渲染控制语法生成不包含任何子组件的空分支节点。未设置时不支持空分支节点。此属性初次赋值后不支持更新，所以赋值后无法在支持空分支、不支持空分支行为之间切换。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从API version 23开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| supported | boolean | undefined | 是 | 当前[List](list.md)组件是否支持在LazyForEach或Repeat中使用if/else渲染控制语法生成一个不含任何子节点的空分支节点。 true表示支持空分支节点；false表示不支持空分支节点。 值为undefined时，按false处理。 |

#### [List](list.md)ItemAlign9+枚举说明

设置子组件在[List](list.md)交叉轴方向的对齐方式。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| Start | 0 | [List](list.md)Item在List中，交叉轴方向首部对齐。 |
| Center | 1 | [List](list.md)Item在List中，交叉轴方向居中对齐。 |
| End | 2 | [List](list.md)Item在List中，交叉轴方向尾部对齐。 |

#### StickyStyle9+枚举说明

[List](list.md)ItemGroup吸顶或吸底效果枚举。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| None | 0 | [List](list.md)ItemGroup的header不吸顶，footer不吸底。 卡片能力： 从API version 9开始，该接口支持在ArkTS卡片中使用。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| Header | 1 | [List](list.md)ItemGroup的header吸顶，footer不吸底。 卡片能力： 从API version 9开始，该接口支持在ArkTS卡片中使用。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| Footer | 2 | [List](list.md)ItemGroup的footer吸底，header不吸顶。 卡片能力： 从API version 9开始，该接口支持在ArkTS卡片中使用。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| BOTH20+ | 3 | [List](list.md)ItemGroup的header吸顶，footer吸底。 卡片能力： 从API version 20开始，该接口支持在ArkTS卡片中使用。 元服务API： 从API version 20开始，该接口支持在元服务中使用。 |

#### [Scroll](Scroll.md)SnapAlign10+枚举说明

设置列表项滚动结束对齐效果。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NONE | 0 | 默认无项目滚动对齐效果。 |
| START | 1 | 视图中的第一项将在列表的开头对齐。 说明： 当列表位移至末端，需要将末端的item完整显示，可能出现开头不对齐的情况。 |
| CENTER | 2 | 视图中的中间项将在列表中心对齐。 说明： 顶端和末尾的item都可以在列表中心对齐，列表显示可能露出空白。 |
| END | 3 | 视图中的最后一项将在列表末尾对齐。 说明： 当列表位移至顶端，需要将顶端的item完整显示，可能出现末尾不对齐的情况。 |

#### [Scroll](Scroll.md)SnapAnimationSpeed22+枚举说明

设置列表项滚动限位动画速度。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NORMAL | 0 | 默认列表限位动画速度，通常用于列表项尺寸较大，划一下滚动一个列表项场景。 |
| SLOW | 1 | 列表限位动画速度较慢，通常用于列表项尺寸较小，划一下滚动多个列表项场景。 |

#### CloseSwipeActionOptions11+对象说明

收起[EXPANDED](ListItem.md#ZH-CN_TOPIC_0000002553200785__swipeactionstate11枚举说明)状态[ListItem](ListItem.md)回调事件集合，用于设置收起动画完成后回调事件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| onFinish | ()=>void | 否 | 是 | 在收起动画完成后触发。 |

#### [List](list.md)DividerOptions18+对象说明

用于设置[List](list.md)或ListItemGroup组件的分割线样式。

为规范匿名对象的定义，API 18版本修改了此处的元素定义。其中，保留了历史匿名对象的起始版本信息，会出现外层元素@since版本号高于内层元素版本号的情况，但这不影响接口的使用。

**卡片能力：** 从API version 18开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| strokeWidth7+ | [Length](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__length) | 否 | 否 | 分割线的线宽。 单位：vp 说明： 设置为负数，百分比，或者大于等于List内容区长度时，按0处理。 卡片能力： 从API version 9开始，该接口支持在ArkTS卡片中使用。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| color7+ | [ResourceColor](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor) | 否 | 是 | 分割线颜色。 默认值：0x08000000 卡片能力： 从API version 9开始，该接口支持在ArkTS卡片中使用。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| startMargin7+ | [Length](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__length) | 否 | 是 | 分割线与列表侧边起始端的距离。 默认值：0 单位：vp 说明： 设置为负数或者百分比时，按默认值处理。 endMargin + startMargin 超过列宽度后startMargin和endMargin均会被置0。 卡片能力： 从API version 9开始，该接口支持在ArkTS卡片中使用。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| endMargin7+ | [Length](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__length) | 否 | 是 | 分割线与列表侧边结束端的距离。 默认值：0 单位：vp 说明： 设置为负数或者百分比时，按默认值处理。 endMargin + startMargin 超过列宽度后startMargin和endMargin均会被置0。 卡片能力： 从API version 9开始，该接口支持在ArkTS卡片中使用。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |

#### 事件

除支持[通用事件](通用事件.md)和[滚动组件通用事件](滚动组件通用接口.md#ZH-CN_TOPIC_0000002522240828__事件)外，还支持以下事件：

#### on[Scroll](Scroll.md)Index

on[Scroll](Scroll.md)Index(event: (start: number, end: number, center: number) => void)

有子组件划入或划出[List](list.md)显示区域时触发。计算索引值时，ListItemGroup作为一个整体占一个索引值，不计算ListItemGroup内部ListItem的索引值。

[List](list.md)的边缘效果为弹簧效果时，在List划动到边缘继续划动和松手回弹过程不会触发onScrollIndex事件。

触发该事件的条件：列表初始化时会触发一次，[List](list.md)显示区域内第一个子组件的索引值或最后一个子组件的索引值有变化时会触发。

从API version 10开始，[List](list.md)显示区域中间位置子组件变化时也会触发该事件。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| start | number | 是 | [List](list.md)显示区域内第一个子组件的索引值 |
| end | number | 是 | [List](list.md)显示区域内最后一个子组件的索引值。 |
| center10+ | number | 是 | [List](list.md)显示区域内中间位置子组件的索引值。 |

#### onReachStart

onReachStart(event: () => void)

列表到达起始位置时触发。

[List](list.md)初始化时如果initialIndex为0会触发一次，List滚动到起始位置时触发一次。List边缘效果为弹簧效果时，划动经过起始位置时触发一次，回弹回起始位置时再触发一次。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | () => void | 是 | 列表到达起始位置时触发的回调。 |

#### onReachEnd

onReachEnd(event: () => void)

列表到达末尾位置时触发事件。当最后一个子组件因滚动或内容/布局变化出现在列表视窗中时，触发此回调。

当子组件未撑满列表，无须滚动即可直接在列表内完整展示时，首次加载也会触发此事件。

[List](list.md)边缘效果为弹簧效果时，划动经过末尾位置时触发一次，回弹回末尾位置时再触发一次。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | () => void | 是 | 列表到达末尾位置时触发的回调。 |

#### on[Scroll](Scroll.md)FrameBegin9+

onScrollFrameBegin(event: [OnScrollFrameBeginCallback](Scroll.md#ZH-CN_TOPIC_0000002497444896__onscrollframebegincallback18))

该接口回调时，事件参数传入即将发生的滑动量，事件处理函数中可根据应用场景计算实际需要的滑动量并作为事件处理函数的返回值返回，列表将按照返回值的实际滑动量进行滑动。

当listDirection的值为[Axis](枚举说明.md#ZH-CN_TOPIC_0000002529284967__axis).Vertical时，返回垂直方向滑动量，当listDirection的值为Axis.Horizontal时，返回水平方向滑动量。

满足以下任一条件时触发该事件：

1. 用户交互（如手指滑动、键鼠操作等）触发滚动。
1. [List](list.md)惯性滚动。

1. 调用[fling](Scroll.md#ZH-CN_TOPIC_0000002553360749__[fling](Scroll.md#ZH-CN_TOPIC_0000002497444896__fling12)12)接口触发滚动。

不触发该事件的条件：

1. 调用除[fling](Scroll.md#ZH-CN_TOPIC_0000002553360749__[fling](Scroll.md#ZH-CN_TOPIC_0000002497444896__fling12)12)接口外的其他滚动控制接口。

1. 越界回弹。
1. 拖动滚动条。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [OnScrollFrameBeginCallback](Scroll.md#ZH-CN_TOPIC_0000002497444896__onscrollframebegincallback18) | 是 | 每帧滚动开始回调函数。 |

#### on[Scroll](Scroll.md)Start9+

on[Scroll](Scroll.md)Start(event: () => void)

列表滑动开始时触发。手指拖动列表或列表的滚动条触发的滑动开始时，会触发该事件。使用[Scroller](Scroll.md#ZH-CN_TOPIC_0000002553360749__scroller)滑动控制器触发的带动画的滑动，动画开始时会触发该事件。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | () => void | 是 | 列表滑动开始时触发的回调。 |

#### on[Scroll](Scroll.md)Stop

on[Scroll](Scroll.md)Stop(event: () => void)

列表滑动停止时触发。手拖动列表或列表的滚动条触发的滑动，手离开屏幕后滑动停止时会触发该事件。使用[Scroller](Scroll.md#ZH-CN_TOPIC_0000002553360749__scroller)滑动控制器触发的带动画的滑动，动画停止会触发该事件。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | () => void | 是 | 列表滑动停止时触发的回调。 |

#### onItemMove

onItemMove(event: (from: number, to: number) => boolean)

列表元素发生移动时触发。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| from | number | 是 | 移动前索引值。 |
| to | number | 是 | 移动后索引值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 是否已经移动。返回值为true时列表元素发生移动，返回值为false时列表元素没有移动。 |

#### onItemDragStart8+

onItemDragStart(event: OnItemDragStartCallback)

开始拖拽列表元素时触发。

不支持拖动到List边缘时触发List的自动滚动，可以使用ForEach、LazyForEach、Repeat的[onMove](拖拽排序.md#ZH-CN_TOPIC_0000002553360717__onmove)接口实现该效果，参考[示例12（使用OnMove进行拖拽）](#ZH-CN_TOPIC_0000002522240820__示例12使用onmove进行拖拽)。但需注意[onMove](拖拽排序.md#ZH-CN_TOPIC_0000002553360717__onmove)接口不支持跨ListItemGroup拖拽。


从API version 14开始，该接口支持在[attributeModifier](动态属性设置.md#ZH-CN_TOPIC_0000002522240800__attributemodifier)中调用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | OnItemDragStartCallback | 是 | 列表元素拖拽开始时触发的回调。 API version 22及之前版本，该参数类型为(event: [ItemDragInfo](滚动组件通用接口.md#ZH-CN_TOPIC_0000002529284871__itemdraginfo对象说明), itemIndex: number) => (() => any) | void，其中event和itemIndex参数含义参考OnItemDragStartCallback。 |

#### onItemDragEnter8+

onItemDragEnter(event: (event: [ItemDragInfo](滚动组件通用接口.md#ZH-CN_TOPIC_0000002529284871__itemdraginfo对象说明)) => void)

拖拽列表元素进入列表范围内时触发。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [ItemDragInfo](滚动组件通用接口.md#ZH-CN_TOPIC_0000002529284871__itemdraginfo对象说明) | 是 | 拖拽点的信息。 |

#### onItemDragMove8+

onItemDragMove(event: (event: [ItemDragInfo](滚动组件通用接口.md#ZH-CN_TOPIC_0000002529284871__itemdraginfo对象说明), itemIndex: number, insertIndex: number) => void)

拖拽列表元素在列表范围内移动时触发。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [ItemDragInfo](滚动组件通用接口.md#ZH-CN_TOPIC_0000002529284871__itemdraginfo对象说明) | 是 | 拖拽点的信息。 |
| itemIndex | number | 是 | 拖拽起始位置。 |
| insertIndex | number | 是 | 拖拽插入位置。 |

#### onItemDragLeave8+

onItemDragLeave(event: (event: [ItemDragInfo](滚动组件通用接口.md#ZH-CN_TOPIC_0000002529284871__itemdraginfo对象说明), itemIndex: number) => void)

拖拽列表元素离开列表范围时触发。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [ItemDragInfo](滚动组件通用接口.md#ZH-CN_TOPIC_0000002529284871__itemdraginfo对象说明) | 是 | 拖拽点的信息。 |
| itemIndex | number | 是 | 拖拽离开的列表元素索引值。 |

#### onItemDrop8+

onItemDrop(event: (event: [ItemDragInfo](滚动组件通用接口.md#ZH-CN_TOPIC_0000002529284871__itemdraginfo对象说明), itemIndex: number, insertIndex: number, isSuccess: boolean) => void)

绑定该事件的列表可作为拖拽释放目标，当在列表范围内停止拖拽时触发。

跨[List](list.md)拖拽时，当拖拽释放的位置绑定了onItemDrop时isSuccess为true，否则为false。List内部拖拽时，isSuccess为onItemMove事件的返回值。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [ItemDragInfo](滚动组件通用接口.md#ZH-CN_TOPIC_0000002529284871__itemdraginfo对象说明) | 是 | 拖拽点的信息。 |
| itemIndex | number | 是 | 拖拽起始位置。 |
| insertIndex | number | 是 | 拖拽插入位置。 |
| isSuccess | boolean | 是 | 是否成功释放。返回值为true时列表元素成功释放，返回值为false时列表元素没有成功释放。 |

#### on[Scroll](Scroll.md)VisibleContentChange12+

onScrollVisibleContentChange(handler: [OnScrollVisibleContentChangeCallback](list.md#ZH-CN_TOPIC_0000002529284863__onscrollvisiblecontentchangecallback12))

有子组件划入或划出[List](list.md)显示区域时触发。计算触发条件时，每一个ListItem、ListItemGroup中的header或footer都算一个子组件。

[List](list.md)的边缘效果为弹簧效果时，在List划动到边缘继续划动和松手回弹过程不会触发onScrollVisibleContentChange事件。

触发该事件的条件：列表初始化时会触发一次，[List](list.md)显示区域内第一个子组件的索引值或最后一个子组件的索引值有变化时会触发。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| handler | On[Scroll](Scroll.md)VisibleContentChangeCallback | 是 | 当前显示内容发生改变的时候触发回调。 |

#### onItemDelete(deprecated)

onItemDelete(event: (index: number) => boolean)

当[List](list.md)组件在编辑模式时，点击ListItem右边出现的删除按钮时触发。

从API version 7开始支持，从API version 9开始废弃，无替代接口。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 被删除的列表项的索引值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 是否已经删除。 |

#### on[Scroll](Scroll.md)(deprecated)

onScroll(event: (scrollOffset: number, scrollState: [ScrollState](#ZH-CN_TOPIC_0000002522240820__scrollstate枚举说明)) => void)

列表滑动时触发。


从API version 7开始支持，从API version 12开始废弃，建议使用[onDidScroll](滚动组件通用接口.md#ZH-CN_TOPIC_0000002522240828__ondidscroll12)替代。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scrollOffset | number | 是 | 相对于上一帧的偏移量，[List](list.md)的内容向上滚动时偏移量为正，向下滚动时偏移量为负。 单位vp。 |
| scrollState | [ScrollState](list.md#ZH-CN_TOPIC_0000002529284863__scrollstate枚举说明) | 是 | 当前滑动状态。 |

#### [Scroll](Scroll.md)State枚举说明

滑动状态枚举。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| Idle | 0 | 空闲状态。滚动状态回归空闲时触发，控制器提供的无动画方法控制滚动时触发。 |
| Scroll | 1 | 滚动状态。手指拖动[List](list.md)，拖动滚动条和滚动鼠标滚轮时触发。 |
| Fling | 2 | 惯性滚动状态。动画控制的滚动都会触发。包括快速划动松手后的惯性滚动， 划动到边缘回弹的滚动，快速拖动内置滚动条松手后的惯性滚动， 使用滚动控制器提供的带动画的方法控制的滚动。 |

#### List[Scroller](Scroll.md#ZH-CN_TOPIC_0000002497444896__scroller)11+

[List](list.md)组件的滚动控制器，通过它控制List组件的滚动，仅支持一对一绑定到List组件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full


ListScroller继承自[Scroller](Scroll.md#ZH-CN_TOPIC_0000002553360749__scroller)，具有[Scroller](Scroll.md#ZH-CN_TOPIC_0000002553360749__scroller)的全部方法。

#### 导入对象

```ets
listScroller: ListScroller = new ListScroller();
```

#### getItemRectInGroup11+

getItemRectInGroup(index: number, indexInGroup: number): [RectResult](自定义事件分发.md#ZH-CN_TOPIC_0000002497444840__rectresult)

获取[ListItemGroup](ListItemGroup.md)中的[ListItem](ListItem.md)的大小和相对于List的位置。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | [List](list.md)ItemGroup在List中的索引值。 |
| indexInGroup | number | 是 | [List](list.md)Item在ListItemGroup中的索引值。 |


- index必须是当前显示区域显示的子组件的索引值，否则视index为非法值。
- 索引值为index的子组件必须是[List](list.md)ItemGroup，否则视index为非法值。
- indexInGroup必须是当前显示区域内[List](list.md)ItemGroup中显示的ListItem的索引值，否则视indexInGroup为非法值。
- index或者indexInGroup为非法值时返回的大小和位置均为0。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [RectResult](自定义事件分发.md#ZH-CN_TOPIC_0000002497444840__rectresult) | ListItemGroup中的ListItem的大小和相对于List的位置。 单位：vp。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码]([通用错误码](../../errors/通用错误码.md).md)和[滚动类组件错误码]([滚动类组件错误码](../../errors/滚动类组件错误码.md).md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100004 | Controller not bound to a component. |

#### getVisible[List](list.md)ContentInfo14+

getVisible[List](list.md)ContentInfo(x: number, y: number): VisibleListContentInfo

根据坐标获取子组件的索引信息。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | x轴坐标，单位为vp。 |
| y | number | 是 | y轴坐标，单位为vp。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Visible[List](list.md)ContentInfo | 入参坐标处的子组件的索引信息。 |


- 入参坐标(x, y)的基准点是[List](list.md)组件的位置。
- 如果该坐标位置处于[List](list.md)Item范围内，且该ListItem父组件是List，则返回值对象成员index为该ListItem在List中的索引值，itemGroupArea返回undefined，itemIndexInGroup返回undefined。
- 如果该坐标位置处于[List](list.md)Item范围内，且该ListItem父组件是ListItemGroup，则返回值对象成员index为该ListItemGroup在List中的索引值，itemGroupArea返回ListItemGroupArea.IN_LIST_ITEM_AREA，itemIndexInGroup返回该ListItem在ListItemGroup中的索引值。
- 如果该坐标位置不处于[List](list.md)Item范围内，但是处于ListItemGroup的header或者footer范围内，则返回值对象成员index为该ListItemGroup在List中的索引值，itemIndexInGroup返回undefined。如果坐标位置处于header范围，itemGroupArea返回ListItemGroupArea.IN_HEADER_AREA。如果坐标位置处于footer范围，itemGroupArea返回ListItemGroupArea.IN_FOOTER_AREA。
- 如果该坐标位置既不处于[List](list.md)Item范围内，也不处于ListItemGroup的header或者footer范围内，但是处于ListItemGroup的范围内，则返回值对象成员index为该ListItemGroup在List中的索引值，itemIndexInGroup返回undefined，itemGroupArea返回ListItemGroupArea.NONE。
- 如果该坐标位置既不处于[List](list.md)Item范围内，也不处于ListItemGroup的范围内，则返回值对象成员index为-1，itemIndexInGroup返回undefined，itemGroupArea返回undefined。

**错误码**：

以下错误码详细介绍请参考[通用错误码]([通用错误码](../../errors/通用错误码.md).md)和[滚动类组件错误码]([滚动类组件错误码](../../errors/滚动类组件错误码.md).md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100004 | Controller not bound to a component. |

#### [scrollTo](Scroll.md#ZH-CN_TOPIC_0000002497444896__scrollto)ItemInGroup11+

scrollToItemInGroup(index: number, indexInGroup: number, smooth?: boolean, align?: [ScrollAlign](Scroll.md#ZH-CN_TOPIC_0000002497444896__scrollalign10枚举说明)): void

滑动到指定的[List](list.md)ItemGroup中指定的ListItem。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 要滑动到的目标元素所在的[List](list.md)ItemGroup在当前容器中的索引值。 说明： index值设置成负值或者大于当前容器子组件的最大索引值，视为异常值，本次跳转不生效。 |
| indexInGroup | number | 是 | 要滑动到的目标元素在index指定的[List](list.md)ItemGroup中的索引值。 说明： indexInGroup值设置成负值或者大于index指定的ListItemGroup容器子组件的最大索引值，视为异常值，本次跳转不生效。 |
| smooth | boolean | 否 | 设置该次滑动是否有动效，true表示有动效，false表示没有动效。 默认值：false 说明： 开启动效时，会对经过的所有item进行加载和布局计算，当大量加载item时会导致性能问题。 |
| align | [ScrollAlign](Scroll.md#ZH-CN_TOPIC_0000002497444896__scrollalign10枚举说明) | 否 | 指定滑动到的元素与当前容器的对齐方式。 默认值：ScrollAlign.START。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码]([通用错误码](../../errors/通用错误码.md).md)和[滚动类组件错误码]([滚动类组件错误码](../../errors/滚动类组件错误码.md).md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100004 | Controller not bound to a component. |

#### closeAllSwipeActions11+

closeAllSwipeActions(options?: CloseSwipeActionOptions): void

将[EXPANDED](ListItem.md#ZH-CN_TOPIC_0000002553200785__swipeactionstate11枚举说明)状态的[ListItem](ListItem.md)收起，并设置回调事件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | CloseSwipeActionOptions | 否 | 收起[EXPANDED]([ListItem](ListItem.md).md#ZH-CN_TOPIC_0000002529444837__swipeactionstate11枚举说明)状态的ListItem的回调事件集合。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码]([通用错误码](../../errors/通用错误码.md).md)和[滚动类组件错误码]([滚动类组件错误码](../../errors/滚动类组件错误码.md).md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100004 | Controller not bound to a component. |


- List[Scroller](Scroll.md#ZH-CN_TOPIC_0000002497444896__scroller)必须绑定到List组件上。

#### On[Scroll](Scroll.md)VisibleContentChangeCallback12+

type [OnScrollVisibleContentChangeCallback](list.md#ZH-CN_TOPIC_0000002529284863__onscrollvisiblecontentchangecallback12) = (start: VisibleListContentInfo, end: VisibleListContentInfo) => void

有子组件划入或划出[List](list.md)显示区域时触发。

start和end的index同时返回-1，代表[List](list.md)从有数据变成空的List。

start和end的index同时返回0，代表[List](list.md)内只有一个子组件。


从API version 14开始，该接口支持在[attributeModifier](动态属性设置.md#ZH-CN_TOPIC_0000002522240800__attributemodifier)中调用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| start | Visible[List](list.md)ContentInfo | 是 | 1. 通过该参数获取List显示区域第一个子组件在List中的索引值。 2. 如果当前List显示区域第一个子组件是ListItemGroup，可以获取当前List显示区域第一个组件属于该ListItemGroup的哪一区域。 3. 如果当前List显示区域第一个组件是ListItemGroup内的ListItem，可以获取该ListItem在ListItemGroup内的索引值。 |
| end | Visible[List](list.md)ContentInfo | 是 | 1. 通过该参数获取List显示区域最后一个子组件在List中的索引值。 2. 如果当前List显示区域最后一个子组件是ListItemGroup，可以获取当前List显示区域最后一个组件属于该ListItemGroup的哪一区域。 3. 如果当前List显示区域最后一个组件是ListItemGroup内的ListItem，可以获取该ListItem在ListItemGroup内的索引值。 |

#### Visible[List](list.md)ContentInfo12+对象说明

用于表示[List](list.md)可见内容区子组件的详细信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| index | number | 否 | 否 | 表示[List](list.md)Item或ListItemGroup在List中的索引值。 |
| itemGroupArea | [List](list.md)ItemGroupArea | 否 | 是 | 表示处于ListItemGroup的哪一个区域。 |
| itemIndexInGroup | number | 否 | 是 | 表示[List](list.md)Item在ListItemGroup中的索引值。 |

#### [List](list.md)ItemGroupArea12+枚举说明

枚举了[List](list.md)ItemGroup各个区域。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NONE | 0 | [List](list.md)ItemGroup内部ListItem区域、header区域以及footer区域以外的区域。 |
| IN_LIST_ITEM_AREA | 1 | [List](list.md)ItemGroup内部ListItem区域。 |
| IN_HEADER_AREA | 2 | [List](list.md)ItemGroup内部header区域。 |
| IN_FOOTER_AREA | 3 | [List](list.md)ItemGroup内部footer区域。 |

#### UI[List](list.md)Event19+

frameNode中[getEvent('List')](FrameNode.md#ZH-CN_TOPIC_0000002522240744__geteventlist19)方法的返回值，可用于给List节点设置滚动事件。

UIListEvent继承于[UIScrollableCommonEvent](滚动组件通用接口.md#ZH-CN_TOPIC_0000002522240828__uiscrollablecommonevent19)。

#### setOnWill[Scroll](Scroll.md)19+

setOnWill[Scroll](Scroll.md)(callback: OnWillScrollCallback | undefined): void

设置[onWillScroll](滚动组件通用接口.md#ZH-CN_TOPIC_0000002522240828__onwillscroll12)事件的回调。

方法入参为undefined时，会重置事件回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [OnWillScrollCallback](滚动组件通用接口.md#ZH-CN_TOPIC_0000002529284871__onwillscrollcallback12) | undefined | 是 | [onWillScroll](滚动组件通用接口.md#ZH-CN_TOPIC_0000002529284871__onwillscroll12)事件的回调函数。 |

#### setOnDid[Scroll](Scroll.md)19+

setOnDid[Scroll](Scroll.md)(callback: OnScrollCallback | undefined): void

设置[onDidScroll](滚动组件通用接口.md#ZH-CN_TOPIC_0000002522240828__ondidscroll12)事件的回调。

方法入参为undefined时，会重置事件回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [OnScrollCallback](滚动组件通用接口.md#ZH-CN_TOPIC_0000002529284871__onscrollcallback12) | undefined | 是 | [onDidScroll](滚动组件通用接口.md#ZH-CN_TOPIC_0000002529284871__ondidscroll12)事件的回调函数。 |

#### setOn[Scroll](Scroll.md)Index19+

setOnScrollIndex(callback: On[List](list.md)ScrollIndexCallback | undefined): void

设置[onScrollIndex](#ZH-CN_TOPIC_0000002522240820__onscrollindex)事件的回调。

方法入参为undefined时，会重置事件回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | On[List](list.md)ScrollIndexCallback | undefined | 是 | onScrollIndex事件的回调函数。 |

#### setOn[Scroll](Scroll.md)VisibleContentChange19+

setOn[Scroll](Scroll.md)VisibleContentChange(callback: OnScrollVisibleContentChangeCallback | undefined): void

设置[onScrollVisibleContentChange](#ZH-CN_TOPIC_0000002522240820__onscrollvisiblecontentchange12)事件的回调。

方法入参为undefined时，会重置事件回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [OnScrollVisibleContentChangeCallback](list.md#ZH-CN_TOPIC_0000002529284863__onscrollvisiblecontentchangecallback12) | undefined | 是 | onScrollVisibleContentChange事件的回调函数。 |

#### On[List](list.md)ScrollIndexCallback19+

type On[List](list.md)ScrollIndexCallback = (start: number, end: number, center: number) => void

[List](list.md)组件可见区域item变化事件的回调类型。

**卡片能力：** 从API version 19开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| start | number | 是 | [List](list.md)显示区域内第一个子组件的索引值。 |
| end | number | 是 | [List](list.md)显示区域内最后一个子组件的索引值。 |
| center | number | 是 | [List](list.md)显示区域内中间位置子组件的索引值。 |

#### 示例

#### 示例1（添加滚动事件）

该示例实现了设置纵向列表，并在当前显示界面发生改变时回调索引。

ListDataSource实现了LazyForEach数据源接口[IDataSource](LazyForEach.md#ZH-CN_TOPIC_0000002522080924__idatasource)，用于通过LazyForEach给List提供子组件。

```ets
// ListDataSource.ets
export class ListDataSource implements IDataSource {
  private list: number[] = [];
  private listeners: DataChangeListener[] = [];

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
    if (this.listeners.indexOf(listener) < 0) {
      this.listeners.push(listener);
    }

  unregisterDataChangeListener(listener: DataChangeListener): void {
    const pos = this.listeners.indexOf(listener);
    if (pos >= 0) {
      this.listeners.splice(pos, 1);
    }

  // 通知LazyForEach组件需要重载所有子组件
  notifyDataReload(): void {
    this.listeners.forEach(listener => {
      listener.onDataReloaded();
    });
  }

  // 通知控制器数据删除
  notifyDataDelete(index: number): void {
    this.listeners.forEach(listener => {
      listener.onDataDelete(index);
    });
  }

  // 通知控制器添加数据
  notifyDataAdd(index: number): void {
    this.listeners.forEach(listener => {
      listener.onDataAdd(index);
    });
  }

  // 在指定索引位置删除一个元素
  public deleteItem(index: number): void {
    this.list.splice(index, 1);
    this.notifyDataDelete(index);
  }

  // 在指定索引位置插入一个元素
  public insertItem(index: number, data: number): void {
    this.list.splice(index, 0, data);
    this.notifyDataAdd(index);
  }

  public reloadData(): void {
    this.notifyDataReload();
}
```

```ets
// xxx.ets
import { ListDataSource } from './ListDataSource';

@Entry
@Component
struct ListExample {
  private arr: ListDataSource = new ListDataSource([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]);

  build() {
    Column() {
      List({ space: 20, initialIndex: 0 }) {
        LazyForEach(this.arr, (item: number) => {
          ListItem() {
            Text('' + item)
              .width('100%').height(100).fontSize(16)
              .textAlign(TextAlign.Center).borderRadius(10).backgroundColor(0xFFFFFF)
          }
        }, (item: number) => item.toString())
      }
      .listDirection(Axis.Vertical) // 排列方向
      .scrollBar(BarState.Off)
      .friction(0.6)
      .divider({ strokeWidth: 2, color: 0xFFFFFF, startMargin: 20, endMargin: 20 }) // 每行之间的分界线
      .edgeEffect(EdgeEffect.Spring) // 边缘效果设置为Spring
      .onScrollIndex((firstIndex: number, lastIndex: number, centerIndex: number) => {
        console.info('first' + firstIndex);
        console.info('last' + lastIndex);
        console.info('center' + centerIndex);
      })
      .onScrollVisibleContentChange((start: VisibleListContentInfo, end: VisibleListContentInfo) => {
        console.info(' start index: ' + start.index +
                    ' start item group area: ' + start.itemGroupArea +
                    ' start index in group: ' + start.itemIndexInGroup);
        console.info(' end index: ' + end.index +
                    ' end item group area: ' + end.itemGroupArea +
                    ' end index in group: ' + end.itemIndexInGroup);
      })
      .onDidScroll((scrollOffset: number, scrollState: ScrollState) => {
        console.info(`onScroll scrollState = ScrollState` + scrollState + `, scrollOffset = ` + scrollOffset);
      })
      .width('90%')
    }
    .width('100%')
    .height('100%')
    .backgroundColor(0xDCDCDC)
    .padding({ top: 5 })
  }
```

![image](public_sys-resources/zh-cn_image_0000002553364789.webp)

#### 示例2（设置子元素对齐）

该示例展示了不同[List](list.md)ItemAlign枚举值下，List组件交叉轴方向子元素对齐效果。

ListDataSource说明及完整代码参考[示例1添加滚动事件](#ZH-CN_TOPIC_0000002522240820__示例1添加滚动事件)。

```ets
// xxx.ets
import { ListDataSource } from './ListDataSource';

@Entry
@Component
struct ListLanesExample {
  arr: ListDataSource = new ListDataSource([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]);
  @State alignListItem: ListItemAlign = ListItemAlign.Start;

  build() {
    Column() {
      List({ space: 20, initialIndex: 0 }) {
        LazyForEach(this.arr, (item: string) => {
          ListItem() {
            Text('' + item)
              .width('100%')
              .height(100)
              .fontSize(16)
              .textAlign(TextAlign.Center)
              .borderRadius(10)
              .backgroundColor(0xFFFFFF)
          }
          .border({ width: 2, color: Color.Green })
        }, (item: string) => item)
      }
      .height(300)
      .width('90%')
      .friction(0.6)
      .border({ width: 3, color: Color.Red })
      .lanes({ minLength: 40, maxLength: 40 })
      .alignListItem(this.alignListItem)
      .scrollBar(BarState.Off)

      Button('点击更改alignListItem:' + this.alignListItem).onClick(() => {
        if (this.alignListItem == ListItemAlign.Start) {
          this.alignListItem = ListItemAlign.Center;
        } else if (this.alignListItem == ListItemAlign.Center) {
          this.alignListItem = ListItemAlign.End;
        } else {
          this.alignListItem = ListItemAlign.Start;
        }
      })
    }.width('100%').height('100%').backgroundColor(0xDCDCDC).padding({ top: 5 })
  }
```

![image](public_sys-resources/zh-cn_image_0000002522244868.webp)

#### 示例3（设置编辑模式）

该示例展示了如何设置当前[List](list.md)组件是否处于可编辑模式。

ListDataSource说明及完整代码参考[示例1添加滚动事件](#ZH-CN_TOPIC_0000002522240820__示例1添加滚动事件)。

```ets
// xxx.ets
import { ListDataSource } from './ListDataSource';

@Entry
@Component
struct ListExample {
  arr: ListDataSource=new ListDataSource([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]);
  @State editFlag: boolean = false;

  build() {
    Stack({ alignContent: Alignment.TopStart }) {
      Column() {
        List({ space: 20, initialIndex: 0 }) {
          LazyForEach(this.arr, (item: number, index?: number) => {
            ListItem() {
              Flex({ direction: FlexDirection.Row, alignItems: ItemAlign.Center }) {
                Text('' + item)
                  .width('100%')
                  .height(80)
                  .fontSize(20)
                  .textAlign(TextAlign.Center)
                  .borderRadius(10)
                  .backgroundColor(0xFFFFFF)
                  .flexShrink(1)
                if (this.editFlag) {
                  Button() {
                    Text('delete').fontSize(16)
                  }.width('30%').height(40)
                  .onClick(() => {
                    if (index != undefined) {
                      console.info(this.arr.getData(index) + 'Delete');
                      this.arr.deleteItem(index);
                      this.arr.reloadData();
                      console.info(JSON.stringify(this.arr));
                      this.editFlag = false;
                    }
                  }).stateEffect(true)
                }
          }, (item: number, index: number) => item.toString() + index.toString())
        }.width('90%')
        .scrollBar(BarState.Off)
        .friction(0.6)
      }.width('100%')

      Button('edit list')
        .onClick(() => {
          this.editFlag = !this.editFlag;
        }).margin({ top: 5, left: 20 })
    }.width('100%').height('100%').backgroundColor(0xDCDCDC).padding({ top: 5 })
  }
```

![image](public_sys-resources/zh-cn_image_0000002553204829.webp)

#### 示例4（设置限位对齐）

该示例展示了[List](list.md)组件设置居中限位的实现效果。

ListDataSource说明及完整代码参考[示例1添加滚动事件](#ZH-CN_TOPIC_0000002522240820__示例1添加滚动事件)。

```ets
// xxx.ets
import { ListDataSource } from './ListDataSource';

@Entry
@Component
struct ListExample {
  private arr: ListDataSource=new ListDataSource([]);
  private scrollerForList: Scroller = new Scroller();

  aboutToAppear() {
    let list: number[] = [];
    for (let i = 0; i < 20; i++) {
      list.push(i);
    }
    this.arr = new ListDataSource(list);
  }

  build() {
    Column() {
      Row() {
        List({ space: 20, initialIndex: 3, scroller: this.scrollerForList }) {
          LazyForEach(this.arr, (item: number) => {
            ListItem() {
              Text('' + item)
                .width('100%').height(100).fontSize(16)
                .textAlign(TextAlign.Center)
            }
            .borderRadius(10).backgroundColor(0xFFFFFF)
            .width('60%')
            .height('80%')
          }, (item: number) => JSON.stringify(item))
        }
        .chainAnimation(true)
        .edgeEffect(EdgeEffect.Spring)
        .listDirection(Axis.Horizontal)
        .height('100%')
        .width('100%')
        .scrollSnapAlign(ScrollSnapAlign.CENTER)
        .borderRadius(10)
        .backgroundColor(0xDCDCDC)
      }
      .width('100%')
      .height('100%')
      .backgroundColor(0xDCDCDC)
      .padding({ top: 10 })
    }
```

![image](public_sys-resources/zh-cn_image_0000002522084876.webp)

#### 示例5（跳转准确）

该示例通过设置[childrenMainSize](#ZH-CN_TOPIC_0000002522240820__childrenmainsize12)属性，实现了List在子组件高度不一致时调用scrollTo接口也可以跳转准确。

如果配合状态管理V2使用，详情见：[List与makeObserved](../../guides/状态管理V1-V2迁移指导.md#滚动组件)。

ListDataSource说明及完整代码参考[示例1添加滚动事件](#ZH-CN_TOPIC_0000002522240820__示例1添加滚动事件)。

```ets
// xxx.ets
import { ListDataSource } from './ListDataSource';

@Entry
@Component
struct ListExample {
  private arr: ListDataSource = new ListDataSource([]);
  private scroller: ListScroller = new ListScroller();
  @State listSpace: number = 10;
  @State listChildrenSize: ChildrenMainSize = new ChildrenMainSize(100);
  aboutToAppear(){
    // 初始化数据源。
    let list: number[] = [];
    for (let i = 0; i < 10; i++) {
      list.push(i);
    }
    this.arr = new ListDataSource(list);
    // 前5个item的主轴大小不是默认大小100，因此需要通过ChildrenMainSize通知List。
    this.listChildrenSize.splice(0, 5, [300, 300, 300, 300, 300]);
  }

  build() {
    Column() {
      List({ space: this.listSpace, initialIndex: 4, scroller: this.scroller }) {
        LazyForEach(this.arr, (item: number) => {
          ListItem() {
            Text('item-' + item)
              .height( item < 5 ? 300 : this.listChildrenSize.childDefaultSize)
              .width('90%')
              .fontSize(16)
              .textAlign(TextAlign.Center)
              .borderRadius(10)
              .backgroundColor(0xFFFFFF)
          }
        }, (item: string) => item)
      }
      .backgroundColor(Color.Gray)
      .layoutWeight(1)
      .scrollBar(BarState.On)
      .childrenMainSize(this.listChildrenSize)
      .alignListItem(ListItemAlign.Center)
      Row({ space: 18 }) {
        Button() { Text('item size + 50') }.onClick(()=>{
          this.listChildrenSize.childDefaultSize += 50;
        }).height('50%').width('30%').backgroundColor(0xADD8E6)
        Button() { Text('item size - 50') }.onClick(()=>{
          if (this.listChildrenSize.childDefaultSize === 0) {
            return;
          }
          this.listChildrenSize.childDefaultSize -= 50;
        }).height('50%').width('30%').backgroundColor(0xADD8E6)
        Button() { Text('scrollTo (0, 310)') }.onClick(()=>{
          // 310: 跳转到item 1顶部与List顶部平齐的位置。
          // 如果不设置childrenMainSize，item高度不一致时scrollTo会不准确。
          this.scroller.scrollTo({ xOffset: 0, yOffset: 310 })
        }).height('50%').width('30%').backgroundColor(0xADD8E6)
      }.height('20%')
    }
```

![image](public_sys-resources/zh-cn_image_0000002553364791.webp)

#### 示例6（获得子组件索引信息）

该示例展示了含有group时，获得[List](list.md)组件的Item索引相关信息。

```ets
// xxx.ets
class TimeTableDataSource implements IDataSource {
  private list: TimeTable[] = [];

  constructor(list: TimeTable[]) {
    this.list = list;
  }

  totalCount(): number {
    return this.list.length;
  }

  getData(index: number): TimeTable {
    return this.list[index];
  }

  registerDataChangeListener(listener: DataChangeListener): void {
  }

  unregisterDataChangeListener(listener: DataChangeListener): void {
  }

class ProjectsDataSource implements IDataSource {
  private list: string[] = [];

  constructor(list: string[]) {
    this.list = list;
  }

  totalCount(): number {
    return this.list.length;
  }

  getData(index: number): string {
    return this.list[index];
  }

  registerDataChangeListener(listener: DataChangeListener): void {
  }

  unregisterDataChangeListener(listener: DataChangeListener): void {
}

@Entry
@Component
struct ListItemGroupExample {
  private timeTable: TimeTable[] = [
  {
    title: '星期一',
    projects: ['语文', '数学', '英语']
  },
  {
    title: '星期二',
    projects: ['物理', '化学', '生物']
  },
  {
    title: '星期三',
    projects: ['历史', '地理', '政治']
  },
  {
    title: '星期四',
    projects: ['美术', '音乐', '体育']
  }
];
  private scroller: ListScroller = new ListScroller();
  @State listIndexInfo: VisibleListContentInfo = { index: -1 };
  @State mess:string = 'null';
  @State itemBackgroundColorArr: boolean[] = [false];
  @Builder
  itemHead(text: string) {
    Text(text)
      .fontSize(20)
      .backgroundColor(0xAABBCC)
      .width('100%')
      .padding(10)
  }

  @Builder
  itemFoot(num: number) {
    Text('共' + num + '节课')
      .fontSize(16)
      .backgroundColor(0xAABBCC)
      .width('100%')
      .padding(5)
  }

  build() {
    Column() {
      List({ space: 20, scroller: this.scroller}) {
        LazyForEach(new TimeTableDataSource(this.timeTable), (item: TimeTable, index: number) => {
          ListItemGroup({ header: this.itemHead(item.title), footer: this.itemFoot(item.projects.length) }) {
            LazyForEach(new ProjectsDataSource(item.projects), (project: string, subIndex: number) => {
              ListItem() {
                Text(project)
                  .width('100%')
                  .height(100)
                  .fontSize(20)
                  .textAlign(TextAlign.Center)
                  .backgroundColor(this.itemBackgroundColorArr[index * 3 +subIndex] ? 0x68B4FF: 0xFFFFFF)
              }
            }, (item: string) => item)
          }
          .divider({ strokeWidth: 1, color: Color.Blue }) // 每行之间的分界线
        },(item: string) => item)
      }
      .width('90%')
      .sticky(StickyStyle.Header | StickyStyle.Footer)
      .scrollBar(BarState.Off)
      .gesture(
        PanGesture()
          .onActionUpdate((event: GestureEvent) => {
            if (event.fingerList[0] != undefined && event.fingerList[0].localX != undefined && event.fingerList[0].localY != undefined) {
              this.listIndexInfo  = this.scroller.getVisibleListContentInfo(event.fingerList[0].localX, event.fingerList[0].localY);
              let itemIndex:string = 'undefined';
              if (this.listIndexInfo.itemIndexInGroup != undefined ) {
                itemIndex = this.listIndexInfo.itemIndexInGroup.toString();
                if (this.listIndexInfo.index != undefined && this.listIndexInfo.index >= 0 &&
                  this.listIndexInfo.itemIndexInGroup >= 0 ) {
                  this.itemBackgroundColorArr[this.listIndexInfo.index * 3 + this.listIndexInfo.itemIndexInGroup] = true;
                }
              this.mess = 'index:' + this.listIndexInfo.index.toString() + ' itemIndex:' + itemIndex;
            }
          }))
      .gesture(
        TapGesture({ count: 1 })
          .onAction((event: GestureEvent) => {
            if (event) {
              this.itemBackgroundColorArr.splice(0,this.itemBackgroundColorArr.length);
            }
          })
      )
      Text('您当前位置Item索引为'+ this.mess)
        .fontColor(Color.Red)
        .height(50)
    }.width('100%').height('90%').backgroundColor(0xDCDCDC).padding({ top: 5 })
  }

interface TimeTable {
  title: string;
  projects: string[];
}
```

![image](public_sys-resources/zh-cn_image_0000002522244870.webp)

#### 示例7（设置边缘渐隐）

该示例实现了[List](list.md)组件开启边缘渐隐效果并设置边缘渐隐长度。

ListDataSource说明及完整代码参考[示例1添加滚动事件](#ZH-CN_TOPIC_0000002522240820__示例1添加滚动事件)。

```ets
import { LengthMetrics } from '@kit.ArkUI'
import { ListDataSource } from './ListDataSource';
@Entry
@Component
struct ListExample {
  private arr: ListDataSource=new ListDataSource([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]);
  scrollerForList: Scroller = new Scroller();

  build() {
    Column() {

      List({ space: 20, initialIndex: 0, scroller: this.scrollerForList }) {
        LazyForEach(this.arr, (item: number) => {
          ListItem() {
            Text('' + item)
              .width('100%').height(100).fontSize(16)
              .textAlign(TextAlign.Center).borderRadius(10).backgroundColor(0xFFFFFF)
          }
        }, (item: number) => item.toString())
      }
      .fadingEdge(true, { fadingEdgeLength: LengthMetrics.vp(80) })
    }
    .width('100%')
    .height('100%')
    .backgroundColor(0xDCDCDC)
    .padding({ top: 5 })
  }
```

![image](public_sys-resources/zh-cn_image_0000002553204831.webp)

#### 示例8（单边边缘效果）

该示例通过edgeEffect接口，实现了[List](list.md)组件设置单边边缘效果。

ListDataSource说明及完整代码参考[示例1添加滚动事件](#ZH-CN_TOPIC_0000002522240820__示例1添加滚动事件)。

```ets
// xxx.ets
import { ListDataSource } from './ListDataSource';

@Entry
@Component
struct ListExample {
  private arr: ListDataSource = new ListDataSource([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]);
  scrollerForList: Scroller = new Scroller();
  build() {
    Column() {
      List({ space: 20, initialIndex: 0, scroller: this.scrollerForList }) {
        LazyForEach(this.arr, (item: number) => {
          ListItem() {
            Text('' + item)
              .width('100%').height(100).fontSize(16)
              .textAlign(TextAlign.Center).borderRadius(10).backgroundColor(0xFFFFFF)
          }
        }, (item: string) => item)
      }
      .edgeEffect(EdgeEffect.Spring, {alwaysEnabled: true, effectEdge: EffectEdge.START})
      .width('90%').height('90%')
    }
    .width('100%')
    .height('100%')
    .backgroundColor(0xDCDCDC)
    .padding({ top: 5 })
  }
```

![image](public_sys-resources/zh-cn_image_0000002522084878.webp)

#### 示例9（设置折行走焦）

从API version 20开始，该示例通过[focusWrapMode](#ZH-CN_TOPIC_0000002522240820__focuswrapmode20)接口，实现了List组件方向键走焦换行效果。

```ets
@Entry
@Component
struct ListExample {
  @State arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
  build() {
    Stack({ alignContent: Alignment.TopStart }) {
      Column() {
        List({ space: 40, initialIndex: 0 }) {
          ForEach(this.arr, (item: number, index?: number) => {
            ListItem() {
              Flex({ direction: FlexDirection.Row, alignItems: ItemAlign.Center }) {
                Text('' + item)
                  .width(150)
                  .height(93)
                  .fontSize(30)
                  .textAlign(TextAlign.Center)
                  .borderRadius(10)
                  .backgroundColor(0xFFFFFF)
                  .flexShrink(1)
                  .focusable(true)
                  .offset({ left: 5 })
              }
          }, (item: string, index?: number) => item)
        }
        .lanes(2)
        .contentStartOffset(20)
        .contentEndOffset(20)
        .width('100%')
        .scrollBar(BarState.Off)
        .friction(0.6)
        .focusWrapMode(FocusWrapMode.WRAP_WITH_ARROW)
        .alignListItem(ListItemAlign.Center)
        .offset({ left: 20 })
      }.width('90%')
    }.width('100%').height('100%').backgroundColor(0xDCDCDC).padding({ top: 5 })
  }
```

![image](public_sys-resources/zh-cn_image_0000002553364793.webp)

#### 示例10（设置显示区域外插入数据时，保持显示内容不变）

该示例通过maintainVisibleContentPosition接口，实现了上滑无限加载历史消息场景。

ListDataSource说明及完整代码参考[示例1添加滚动事件](#ZH-CN_TOPIC_0000002522240820__示例1添加滚动事件)。

```ets
import { ListDataSource } from './ListDataSource';

@Entry
@Component
struct ListExample {
  private arr: ListDataSource = new ListDataSource([990, 991, 992, 993, 994, 995, 996, 997, 998, 999]);
  build() {
    Column() {
      List({ space: 20, initialIndex: 9 }) {
        LazyForEach(this.arr, (item: number) => {
          ListItem() {
            Text('message:' + item)
              .width('100%').height(100)
              .fontSize(16)
              .textAlign(TextAlign.Center)
              .borderRadius(10)
              .backgroundColor(0xFFFFFF)
          }
        }, (item: number) => item.toString())
      }
      .maintainVisibleContentPosition(true)
      .onScrollIndex((start:number)=>{
        if (start < 5) {
          for (let i = 0; i < 10; i++) {
            this.arr.insertItem(0, this.arr.getData(0) - 1);
          }
      })
    }
    .width('100%')
    .height('100%')
    .backgroundColor(0xDCDCDC)
    .padding(12)
  }
```

![image](public_sys-resources/zh-cn_image_0000002522244872.webp)

#### 示例11（设置滚动条的边距）

从API version 20开始，该示例展示了通过[scrollBarMargin](滚动组件通用接口.md#ZH-CN_TOPIC_0000002522240828__scrollbarmargin20)属性设置滚动条边距并避让[contentStartOffset](#ZH-CN_TOPIC_0000002522240820__contentstartoffset11)、[contentEndOffset](#ZH-CN_TOPIC_0000002522240820__contentendoffset11)区域的效果。

```ets
// xxx.ets
import { LengthMetrics } from '@kit.ArkUI';

@Entry
@Component
struct ListScrollBarMarginExample {
  @State arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];

  build() {
    Column() {
      List({ space: 40, initialIndex: 0 }) {
        ForEach(this.arr, (item: number, index?: number) => {
          ListItem() {
            Text('' + item)
              .width('100%')
              .height(100)
              .fontSize(16)
              .textAlign(TextAlign.Center)
              .borderRadius(10)
              .backgroundColor(0xFFFFFF)
          }
        }, (item: string, index?: number) => item)
      }
      .contentStartOffset(20)
      .contentEndOffset(20)
      .scrollBar(BarState.On)
      .scrollBarMargin({ start: LengthMetrics.vp(20), end: LengthMetrics.vp(20) })
      .width('90%')
    }
    .width('100%')
    .height('100%')
    .backgroundColor(0xDCDCDC)
    .padding({ top: 5 })
  }
```

![image](public_sys-resources/zh-cn_image_0000002553204833.webp)

#### 示例12（使用OnMove进行拖拽）

从API version 12开始，该示例展示了使用ForEach的[onMove](拖拽排序.md#ZH-CN_TOPIC_0000002553360717__onmove)接口进行拖拽排序的效果，支持拖动到List边缘时触发List的自动滚动。

```ets
@Entry
@Component
struct ForEachSort {
  @State arr: Array<string> = [];

  build() {
    Row() {
      List() {
        ForEach(this.arr, (item: string) => {
          ListItem() {
            Text(item.toString())
              .fontSize(16)
              .textAlign(TextAlign.Center)
              .size({ height: 100, width: '100%' })
          }.margin(10)
          .borderRadius(10)
          .backgroundColor('#FFFFFFFF')
        }, (item: string) => item)
          .onMove((from: number, to: number) => {
            let tmp = this.arr.splice(from, 1);
            this.arr.splice(to, 0, tmp[0]);
          })
      }
      .width('100%')
      .height('100%')
      .backgroundColor('#FFDCDCDC')
    }

  aboutToAppear(): void {
    for (let i = 0; i < 100; i++) {
      this.arr.push(i.toString());
    }
```

![image](public_sys-resources/zh-cn_image_0000002522084880.webp)

#### 示例13（基于断点配置lanes）

从API version 22开始，该示例展示了[List](list.md)组件支持基于断点配置lanes效果。

ListDataSource说明及完整代码参考[示例1添加滚动事件](#ZH-CN_TOPIC_0000002522240820__示例1添加滚动事件)。

```ets
// xxx.ets
import { ListDataSource } from './ListDataSource';

@Entry
@Component
struct ListExample {
  private arr: ListDataSource = new ListDataSource([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]);
  scrollerForList: Scroller = new Scroller();

  build() {
    Column() {
      List({ space: 20, initialIndex: 0, scroller: this.scrollerForList }) {
        LazyForEach(this.arr, (item: number) => {
          ListItem() {
            Text('' + item)
              .width('100%').height(100).fontSize(16)
              .textAlign(TextAlign.Center).borderRadius(10).backgroundColor(0xFFFFFF)
          }
        }, (item: string) => item)
      }
      .lanes({ fillType: PresetFillType.BREAKPOINT_SM2MD3LG5}, 10)
      .width('90%').height(600)
    }
    .width('100%')
    .height('100%')
    .backgroundColor(0xDCDCDC)
    .padding({ top: 5 })
  }
```

[List](list.md)宽度属于sm及更小的断点区间时显示2列。

[List](list.md)宽度属于md断点区间时显示3列。

[List](list.md)宽度属于lg及更大的断点区间时显示5列。

![image](public_sys-resources/zh-cn_image_0000002553204835.webp)

#### 示例14（获取内容总大小）

从API version 22 开始，该示例实现了[List](list.md)组件获取内容总大小的功能。

```ets
// xxx.ets
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct ListExample {
  private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
  scrollerForList: Scroller = new Scroller()
  @State contentWidth: number = -1;
  @State contentHeight: number = -1;
  build() {
    Column() {
      List({ space: 20, initialIndex: 0, scroller: this.scrollerForList }) {
        ForEach(this.arr, (item: number) => {
          ListItem() {
            Text('' + item)
              .width('100%')
              .height(100)
              .fontSize(16)
              .textAlign(TextAlign.Center)
              .borderRadius(10)
              .backgroundColor(0xFFFFFF)
          }
        }, (item: string) => item)
      }
      .width('90%').height('90%')
      // 点击按钮来调用contentSize函数获取内容尺寸
      Button('GetContentSize')
        .onClick(()=> {
            // Scroller未绑定组件时会抛异常，需要加上try catch保护
              try {
              // 通过调用contentSize函数获取内容尺寸的宽度值
              this.contentWidth=this.scrollerForList.contentSize().width;
              // 通过调用contentSize函数获取内容尺寸的高度值
              this.contentHeight=this.scrollerForList.contentSize().height;
            } catch (error) {
              let err: BusinessError = error as BusinessError;
                console.error(`Failed to get contentSize of the grid, code=${err.code}, message=${err.message}`);
            }
        })
      // 将获取到的内容尺寸信息通过文本进行呈现
      Text('Width：'+ this.contentWidth+'，Height：'+ this.contentHeight)
        .fontColor(Color.Red)
        .height(50)
    }
    .width('100%')
    .height('100%')
    .backgroundColor(0xDCDCDC)
    .padding({ top: 5 })
  }
```

![image](public_sys-resources/zh-cn_image_0000002522084882.webp)

#### 示例15（在两个列表之间实现拖拽功能）

该示例通过OnItemDragStart等事件实现了[List](list.md)Item在两个List组件间的拖拽效果。

```ets
// xxx.ets
@ObservedV2
class ListData {
  @Trace public title: string = '';
  @Trace public data: string[] = [];

  constructor(title: string, data: string[]) {
    this.title = title;
    this.data = data;
}

class DraggingData {
  public data?: string;
}

@ComponentV2
struct DraggableList {
  @Require @Param data: string[];
  @Require @Param draggingData: DraggingData;

  @Builder
  ItemBuilder(data: string, size: SizeOptions, event: ItemDragInfo): void {
    Stack() {
      Text(data)
    }
    .backgroundColor(Color.White)
    .borderRadius(4)
    .size(size)
  }

  viewWidth: number = 0;
  lastInsertIndex: number = 0;
  scroller: Scroller = new Scroller();

  build() {
    List({ scroller: this.scroller }) {
      ForEach(this.data, (item: string) => {
        ListItem() {
          Text(item)
        }
        .width('100%')
        .height('10%')
        .margin(10)
        .backgroundColor(Color.White)
        .borderRadius(4)
        .aspectRatio(1)
      }, (item: string) => item)
    }
    .width('50%')
    .layoutWeight(1)
    .padding(10)
    .onItemDragStart((event: ItemDragInfo, itemIndex: number) => {
      let rect = this.scroller.getItemRect(itemIndex);
      let size: SizeOptions = {
        width: rect.width,
        height: rect.height
      };
      this.lastInsertIndex = itemIndex;
      this.draggingData.data = this.data[itemIndex];
      this.data.splice(itemIndex, 1);

      return this.ItemBuilder(this.draggingData.data, size, event);
    })
    .onItemDragEnter((event: ItemDragInfo) => {
      console.info('Item drag enter at position:', event.x, event.y);
    })
    .onItemDragMove((event: ItemDragInfo, itemIndex: number, insertIndex: number) => {
      if (this.lastInsertIndex != insertIndex){
        console.info('insertIndex change from ', this.lastInsertIndex, 'to', insertIndex);
        this.lastInsertIndex = insertIndex;
      }
    })
    .onItemDragLeave((event: ItemDragInfo, itemIndex: number) => {
      console.info('Item ' + itemIndex + ' drag leave at position:', event.x, event.y);
    })
    .onItemDrop((event: ItemDragInfo, itemIndex: number, insertIndex: number, isSuccess: boolean) => {
      if (!isSuccess) {
        this.draggingData.data = undefined;
        return;
      }
      if (insertIndex >= 0) {
        this.data.splice(insertIndex, 0, this.draggingData.data!);
      }
      this.draggingData.data = undefined;
    })
    .onSizeChange((oldValue: SizeOptions, newValue: SizeOptions) => {
      this.viewWidth = newValue.width as number;
    })
  }

@Entry
@ComponentV2
struct Index {
  @Local data: ListData[] = [
    new ListData('A', ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8']),
    new ListData('B', ['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8']),
  ]
  @Local draggingData: DraggingData = new DraggingData();

  build() {
    Stack() {
      Row() {
        DraggableList({ data: this.data[0].data, draggingData: this.draggingData })
        DraggableList({ data: this.data[1].data, draggingData: this.draggingData })
      }
    .backgroundColor('#FFDCDCDC')
  }
```

![image](public_sys-resources/zh-cn_image_0000002553364797.webp)

**示例16（实现[List](list.md)ItemGroup中点击项的居中效果）**

该示例使用[scrollToItemInGroup](#ZH-CN_TOPIC_0000002522240820__scrolltoitemingroup11)接口，实现了点击[ListItemGroup](ListItemGroup.md)中的[ListItem](ListItem.md)时将其居中的效果。

```ets
import { util } from '@kit.ArkTS';

class Contact {
  key: string = util.generateRandomUUID(true);
  name: string;
  icon: Resource;

  constructor(name: string, icon: Resource) {
    this.name = name;
    this.icon = icon;
}

class ContactsGroup {
  title: string = '';
  contacts: Array<object> | null = null;
  key: string = '';
}

@Entry
@Component
struct ContactsList {
  private scroller: ListScroller = new ListScroller();
  private contactsGroups: ContactsGroup[] = [
    {
      title: 'A',
      contacts: [
        new Contact('艾佳', $r('app.media.icon')),  // $r('app.media.icon')需要替换为开发者所需的图像资源文件
        new Contact('安安', $r('app.media.icon')),
        new Contact('Angela', $r('app.media.icon'))
        // ...
      ],
      key: util.generateRandomUUID(true)
    } as ContactsGroup,
    {
      title: 'B',
      contacts: [
        new Contact('白叶', $r('app.media.icon')),
        new Contact('伯明', $r('app.media.icon'))
        // ...
      ],
      key: util.generateRandomUUID(true)
    } as ContactsGroup,
    // ...
  ]

  @Builder
  itemHead(text: string) {
    Text(text)
      .fontSize(20)
      .backgroundColor('#fff1f3f5')
      .width('100%')
      .padding(5)
  }

  build() {
    List({ scroller: this.scroller }) {
      ForEach(this.contactsGroups, (item: ContactsGroup, index: number) => {
        ListItemGroup({ header: this.itemHead(item.title) }) {
          ForEach(item.contacts, (contact: Contact, subIndex: number) => {
            ListItem() {
              Row() {
                Image(contact.icon)
                  .width(40)
                  .height(40)
                  .margin(10)
                Text(contact.name).fontSize(20)
              }
              .width('100%')
              .justifyContent(FlexAlign.Start)
              .margin(10)
            }
            .gesture(
              TapGesture({ count: 1 })
                .onAction((event: GestureEvent) => {
                  if (event) {
                    const itemRect = this.scroller.getItemRectInGroup(index, subIndex);
                    console.info('第', index + 1, '个ListItemGroup的第', subIndex + 1, '个ListItem的 x:', itemRect.x,
                      ' y:', itemRect.y, ' width:', itemRect.width, ' height:', itemRect.height)
                    this.scroller.scrollToItemInGroup(index, subIndex, true, ScrollAlign.CENTER);
                  }
                })
            )
          }, (contact: Contact) => JSON.stringify(contact))
        }
        .divider({ strokeWidth: 4 })
        .width('100%')
      }, (item: ContactsGroup) => JSON.stringify(item))
    }
    .onScrollFrameBegin((offset: number, state: ScrollState) => {
      console.info('List scrollFrameBegin offset: ' + offset + ' state: ' + state.toString());
      return { offsetRemain: offset };
    })
  }
```

![image](public_sys-resources/zh-cn_image_0000002522244876.webp)

**示例17（设置多选聚拢动画）**

该示例通过打开List多选聚拢动画开关，实现了在ListItem上[长按弹出菜单](菜单控制.md#ZH-CN_TOPIC_0000002522080798__bindcontextmenu8)时聚拢显示范围内被选中的ListItem。

从API version 23开始，List组件新增[编辑模式选项](#ZH-CN_TOPIC_0000002522240820__editmodeoptions23)接口，可以设置多选聚拢动画开关。

ListDataSource说明及完整代码参考[示例1（添加滚动事件）](#ZH-CN_TOPIC_0000002522240820__示例1添加滚动事件)。

```ets
// xxx.ets
import { ListDataSource } from './ListDataSource';

@Entry
@Component
struct ListExample {
  private arr: ListDataSource = new ListDataSource([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]);
  @State isSelected: boolean[] = [];
  selectedCount: number = 0;

  @Styles
  normalStyles(): void {
    .opacity(1.0)
  }

  @Styles
  selectStyles(): void {
    .opacity(0.4)
  }

  onPageShow(): void {
    let i: number = 0;
    for (i = 0; i < 10; i++) {
      this.isSelected.push(false);
    }

  @Builder
  MenuBuilder() {
    Flex({ direction: FlexDirection.Column, justifyContent: FlexAlign.Center, alignItems: ItemAlign.Center }) {
      Text('menu item 1')
        .fontSize(18)
        .width(120)
        .height(50)
        .textAlign(TextAlign.Center)
      Divider().height(10)
      Text('menu item 2')
        .fontSize(18)
        .width(120)
        .height(50)
        .textAlign(TextAlign.Center)
    }.width(100)
  }

  build() {
    Column({ space: 5 }) {
      List({ space: 10 }) {
        LazyForEach(this.arr, (item: number) => {
            ListItem() {
              Text(item.toString())
                .fontSize(16)
                .backgroundColor(Color.White)
                .width('100%')
                .height(50)
                .textAlign(TextAlign.Center)
            }
            .selected(this.isSelected[item])
            // 设置多选显示效果
            .stateStyles({
              normal: this.normalStyles,
              selected: this.selectStyles
            })
            .bindContextMenu(this.MenuBuilder, ResponseType.LongPress,
              { preview: MenuPreviewMode.IMAGE, hapticFeedbackMode: HapticFeedbackMode.ENABLED })
            .onClick(() => {
              this.isSelected[item] = !this.isSelected[item];
              console.info(`item:${item}, this.isSelected[item]:${this.isSelected[item]}`)
              if (this.isSelected[item]) {
                ++this.selectedCount;
              } else {
                --this.selectedCount;
              }
            })
        }, (item: number) => item.toString())
      }
      .editModeOptions({
        enableGatherSelectedItemsAnimation: true, onGetPreviewBadge: () => {
          return this.selectedCount;
        }
      })
      .width('90%')
      .height(300)
      .scrollBar(BarState.Off)
    }.width('100%').margin({ top: 5 }).backgroundColor('#FFDCDCDC')
  }
```

![image](public_sys-resources/zh-cn_image_0000002553204837.webp)
