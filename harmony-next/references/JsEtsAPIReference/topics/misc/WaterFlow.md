# WaterFlow

瀑布流容器，由“行”和“列”分割的单元格所组成，通过容器自身的排列规则，将不同大小的“项目”自上而下，如瀑布般紧密布局。

该组件从API version 9 开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

WaterFlow组件支持展示瀑布流布局，不支持编辑模式和子元素拖动功能。

组件内部已绑定手势实现跟手滚动等功能，需要增加自定义手势操作时请参考[手势拦截增强](手势拦截增强.md)进行处理。

#### 子组件

仅支持[FlowItem](../components/FlowItem.md)子组件和自定义组件。自定义组件在WaterFlow下使用时，建议使用FlowItem作为自定组件的顶层组件，不建议给自定义组件设置属性和事件方法。

支持通过渲染控制类型（[if/else](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-rendering-control-ifelse)、[ForEach](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-rendering-control-foreach)、[LazyForEach](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-rendering-control-lazyforeach)和[Repeat](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-rendering-control-repeat)）动态生成子组件，更推荐使用LazyForEach或Repeat以优化性能。

WaterFlow子组件的visibility属性设置为None时不显示，但该子组件周围的columnsGap、rowsGap、margin仍会生效。

在涉及大量子组件的情况下，建议采用懒加载、缓存数据、组件复用、固定宽高以及布局优化等方法，以提升性能和减少内存占用。最佳实践请参考[优化瀑布流加载慢丢帧问题](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-waterflow-performance-optimization)。

纵向布局时，WaterFlow会计算每一列中已放置子组件的累计高度，并将新子组件放入累计高度最小的那一列，以保持整体布局紧凑。

若多个列的高度相同，优先放入最左边的列。在RTL模式下，优先放入最右边的列。

从API version 21开始，WaterFlow单个子组件的宽高最大为16777216px；API version 20及之前，WaterFlow单个子组件的宽高最大为1000000px。子组件超出该大小可能导致滚动或显示异常。

#### 接口

WaterFlow(options?: WaterFlowOptions)

创建瀑布流容器。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明options[WaterFlowOptions](#ZH-CN_TOPIC_0000002497604876__waterflowoptions对象说明)否瀑布流组件参数。

#### WaterFlowOptions对象说明

瀑布流组件参数对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明footer[CustomBuilder](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__custombuilder8)否是

设置WaterFlow尾部组件。

**说明：**

使用方法参见[示例1](#ZH-CN_TOPIC_0000002497604876__示例1使用基本瀑布流)。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

footerContent18+[ComponentContent](../components/ComponentContent.md)否是

设置WaterFlow尾部组件。

该参数的优先级高于参数footer，即同时设置footer和footerContent时，以footerContent设置的组件为准。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

scroller[Scroller](../components/Scroll.md#ZH-CN_TOPIC_0000002497444896__scroller)否是

可滚动组件的控制器，与可滚动组件绑定。

**说明：**

不允许和其他滚动类组件，如：[ArcList](../components/ArcList.md)、[List](../components/list.md)、[Grid](../components/Grid.md)、[Scroll](../components/Scroll.md)和[WaterFlow](WaterFlow.md)绑定同一个滚动控制对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

sections12+[WaterFlowSections](#sections12)否是

设置FlowItem分组，实现同一个瀑布流组件内部各分组使用不同列数混合布局。

**说明：**

1. 使用分组混合布局时会忽略[columnsTemplate](#ZH-CN_TOPIC_0000002497604876__columnstemplate)和[rowsTemplate](#ZH-CN_TOPIC_0000002497604876__rowstemplate)属性。

2. 使用分组混合布局时不支持单独设置footer，可以使用最后一个分组作为尾部组件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

layoutMode12+[WaterFlowLayoutMode](#ZH-CN_TOPIC_0000002497604876__waterflowlayoutmode12枚举说明)否是

设置WaterFlow的布局模式，根据使用场景选择更切合的模式。

**说明：**

默认值：[ALWAYS_TOP_DOWN](#ZH-CN_TOPIC_0000002497604876__waterflowlayoutmode12枚举说明)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

#### WaterFlowSections12+

瀑布流分组信息。

使用splice、push、update修改分组信息后需要保证所有分组子节点总数与瀑布流实际子节点总数一致，否则会出现瀑布流因为不能正常布局而无法滑动的问题。

#### constructor

constructor()

创建一个瀑布流分组。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

#### splice12+

splice(start: number, deleteCount?: number, sections?: Array<SectionOptions>): boolean

移除或者替换已存在的分组和/或添加新分组。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明startnumber是

从0开始计算的索引，会转换为整数，表示要开始改变分组的位置。

**说明：**

1. 如果索引是负数，则从末尾开始计算，使用start + WaterFlowSections.length()。

2. 如果 start < -WaterFlowSections.length()，则使用0。

3. 如果 start >= WaterFlowSections.length()，则在最后添加新分组。

deleteCountnumber否

表示要从start开始删除的分组数量。

**说明：**

1. 如果省略了deleteCount，或者其值大于或等于由start指定的位置到WaterFlowSections末尾的分组数量，那么从start到WaterFlowSections末尾的所有分组将被删除。

2. 如果deleteCount是0或者负数，则不会删除任何分组。

sectionsArray<[SectionOptions](#sectionoptions12对象说明)>否表示要从start开始加入的分组。如果不指定，splice()将只从瀑布流中删除分组。

**返回值：**

类型说明boolean分组修改成功返回true；修改失败（要加入的分组中有任意分组的itemsCount不是非负数）返回false。

#### push12+

push(section: SectionOptions): boolean

将指定分组添加到瀑布流末尾。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明section[SectionOptions](#sectionoptions12对象说明)是添加到瀑布流末尾的分组。

**返回值：**

类型说明boolean分组添加成功返回true，添加失败（新分组的itemsCount不是非负数）返回false。

#### update12+

update(sectionIndex: number, section: SectionOptions): boolean

修改指定索引分组的配置信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明sectionIndexnumber是

从0开始计算的索引，会转换为整数，表示要修改的分组的位置。

**说明：**

1. 如果索引是负数，则从末尾开始计算，使用sectionIndex + WaterFlowSections.length()。

2. 如果sectionIndex < -WaterFlowSections.length()，则使用0。

3. 如果sectionIndex >= WaterFlowSections.length()，则在最后添加新分组。

section[SectionOptions](#sectionoptions12对象说明)是新的分组信息。

**返回值：**

类型说明boolean分组是否更新成功，新分组的itemsCount不是非负数时返回false。

#### values12+

values(): Array<SectionOptions>

获取瀑布流中所有分组配置信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

类型说明Array<[SectionOptions](#sectionoptions12对象说明)>瀑布流中所有分组配置信息。

#### length12+

length(): number

获取瀑布流中分组数量。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

类型说明number瀑布流中分组数量。

#### SectionOptions12+对象说明

FlowItem分组配置信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明itemsCountnumber否否分组中FlowItem数量，必须是非负数。若splice、push、update方法收到的分组中有分组的itemsCount小于0，则不会执行该方法。 避免使用itemsCount为0的分组，这可能导致布局计算异常。crossCountnumber否是纵向布局时为列数，横向布局时为行数，默认值：1。小于1的按默认值处理。columnsGap[Dimension](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__dimension10)否是该分组的列间距，不设置时使用瀑布流的columnsGap，设置非法值时使用0vp。rowsGap[Dimension](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__dimension10)否是该分组的行间距，不设置时使用瀑布流的rowsGap，设置非法值时使用0vp。margin[Margin](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__margin) | [Dimension](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__dimension10)否是

该分组的外边距参数为Length类型时，四个方向外边距同时生效。

默认值：0

单位：vp

margin设置百分比时，上下左右外边距均以瀑布流的width作为基础值。

onGetItemMainSizeByIndex[GetItemMainSizeByIndex](#ZH-CN_TOPIC_0000002497604876__getitemmainsizebyindex12)否是

瀑布流组件布局过程中获取指定index的FlowItem的主轴大小，纵向瀑布流时为高度，横向瀑布流时为宽度，单位vp。

**说明：**

1. 同时使用onGetItemMainSizeByIndex和FlowItem的宽高属性时，主轴大小以onGetItemMainSizeByIndex返回结果为准，onGetItemMainSizeByIndex会覆盖FlowItem的主轴长度。

2. 使用onGetItemMainSizeByIndex可以提高瀑布流跳转到指定位置或index时的效率，避免混用设置onGetItemMainSizeByIndex和未设置的分组，会导致布局异常。

3. onGetItemMainSizeByIndex返回负数时FlowItem高度为0。

#### GetItemMainSizeByIndex12+

type GetItemMainSizeByIndex = (index: number) => number

根据index获取指定Item的主轴大小。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明indexnumber是

FlowItem在WaterFlow中的索引。

取值范围：[0, 子节点总数-1]

**返回值：**

类型说明number指定index的FlowItem的主轴大小，纵向瀑布流时为高度，横向瀑布流时为宽度，单位vp。

#### WaterFlowLayoutMode12+枚举说明

瀑布流组件布局模式枚举。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称值说明ALWAYS_TOP_DOWN0默认的从上到下的布局模式。视窗内的FlowItem依赖视窗上方所有FlowItem的布局信息。因此跳转或切换列数时，需要计算出上方所有的FlowItem的布局信息。SLIDING_WINDOW1

移动窗口式的布局模式。只考虑视窗内的布局信息，对视窗上方的FlowItem没有依赖关系，因此向后跳转或切换列数时只需要布局视窗内的FlowItem。建议优先采用该模式，尤其在应用需要支持屏幕旋转或动态切换列数的场景下。

**说明：**

1. 无动画跳转到较远的位置时，会以目标位置为基准，向前或向后布局FlowItem。这之后如果滑回跳转前的位置，内容的布局效果可能和之前不一致。 这个效果会导致跳转后回滑到顶部时，顶部节点可能不对齐。所以该布局模式下会在滑动到顶部后自动调整布局，保证顶部对齐。在有多个分组的情况下，会在滑动结束时调整在视窗内的分组。

2. [scroller](#ZH-CN_TOPIC_0000002497604876__waterflowoptions对象说明)的[currentOffset](../components/Scroll.md#ZH-CN_TOPIC_0000002497444896__currentoffset)接口返回的总偏移量在触发跳转或数据更新后不准确，在回滑到顶部时会重新校准。

3. 如果在同一帧内调用跳转（如无动画的[scrollToIndex](../components/Scroll.md#ZH-CN_TOPIC_0000002497444896__scrolltoindex)、[scrollEdge](../components/Scroll.md#ZH-CN_TOPIC_0000002497444896__scrolledge)）和输入偏移量（如滑动手势或滚动动画），两者都会生效。

4. 调用无动画的[scrollToIndex](../components/Scroll.md#ZH-CN_TOPIC_0000002497444896__scrolltoindex)进行跳转，如果跳转到较远位置（超过视窗内的FlowItem数量的位置）时，移动窗口模式对总偏移量进行估算。

5. 仅在API version 18及以上版本中支持滚动条[scrollBar](滚动组件通用接口.md#ZH-CN_TOPIC_0000002529284871__scrollbar11)显示。低于此版本时，设置滚动条将不显示。

对比维度ALWAYS_TOP_DOWN (默认)SLIDING_WINDOW适用场景固定列数、简单瀑布流动态列数、大数据量、屏幕旋转布局策略从顶部开始完整布局滑动窗口式布局性能特点依赖上方所有 FlowItem只考虑视窗内布局跳转效率需要计算上方所有布局快速跳转，无需完整计算列数切换需要重新计算全部布局只重新布局视窗内容屏幕旋转支持，但性能较差支持，性能好滚动条显示始终支持API 18+ 支持布局一致性始终保持一致跳转后可能不一致

#### 属性

除支持[通用属性](通用属性.md)和[滚动组件通用属性](滚动组件通用接口.md#ZH-CN_TOPIC_0000002529284871__属性)外，还支持以下属性：

WaterFlow组件使用通用属性[clip12+](形状裁剪.md#ZH-CN_TOPIC_0000002529284827__clip12)和通用属性[clip18+](形状裁剪.md#ZH-CN_TOPIC_0000002529284827__clip18)时默认值都为true。

WaterFlow组件内容裁剪模式[ContentClipMode14+枚举说明](滚动组件通用接口.md#ZH-CN_TOPIC_0000002529284871__contentclipmode14枚举说明)为ContentClipMode.CONTENT_ONLY，padding区域会被裁剪不显示。

#### columnsTemplate

columnsTemplate(value: string)

设置当前瀑布流组件布局列的数量，不设置时默认1列。

例如，'1fr 1fr 2fr' 是将父组件分3列，将父组件允许的宽分为4等份，第1列占1份，第2列占1份，第3列占2份。

可使用columnsTemplate('repeat(auto-fill,track-size)')根据给定的列宽track-size自动计算列数，其中repeat、auto-fill为关键字，track-size为可设置的宽度，支持的单位包括px、vp、%或有效数字，默认单位为vp，使用方法参见[示例2](#ZH-CN_TOPIC_0000002497604876__示例2自动计算列数)。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明valuestring是

当前瀑布流组件布局列的数量。

默认值：'1fr'

#### columnsTemplate22+

columnsTemplate(value: string | ItemFillPolicy)

设置当前瀑布流组件布局列的数量，不设置时默认1列。

当value设置为string类型时，使用方法参考[columnsTemplate(value: string)](#ZH-CN_TOPIC_0000002497604876__columnstemplate)。

当value设置为ItemFillPolicy类型时，将根据WaterFlow组件宽度对应[断点类型](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-grid-layout#栅格容器断点)确定列数。

例如，ItemFillPolicy.BREAKPOINT_DEFAULT在组件宽度属于sm及更小的断点区间时显示2列，属于md断点区间时显示3列，属于lg及更大的断点区间时显示5列，且每列均为1fr。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明valuestring | [ItemFillPolicy](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__itemfillpolicy22)是当前瀑布流组件布局列的数量。

#### rowsTemplate

rowsTemplate(value: string)

设置当前瀑布流组件布局行的数量，不设置时默认1行。

例如，'1fr 1fr 2fr'是将父组件分3行，将父组件允许的高分为4等份，第1行占1份，第2行占1份，第3行占2份。

可使用rowsTemplate('repeat(auto-fill,track-size)')根据给定的行高track-size自动计算行数，其中repeat、auto-fill为关键字，track-size为可设置的高度，支持的单位包括px、vp、%或有效数字，默认单位为vp。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明valuestring是

当前瀑布流组件布局行的数量。

默认值：'1fr'

#### itemConstraintSize

itemConstraintSize(value: ConstraintSizeOptions)

设置约束尺寸，子组件布局时，进行尺寸范围限制。使用方法参考[示例1](#ZH-CN_TOPIC_0000002497604876__示例1使用基本瀑布流)。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明value[ConstraintSizeOptions](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__constraintsizeoptions)是

约束尺寸。设置小于0的值，参数不生效。

**说明：**

1.同时设置itemConstraintSize和FlowItem的[constraintSize](尺寸设置.md#ZH-CN_TOPIC_0000002497444850__constraintsize)属性时，minWidth/minHeight会取其中的最大值，maxWidth/maxHeight会取其中的最小值，调整后的值作为FlowItem的constraintSize处理。

2.只设置itemConstraintSize时，相当于对WaterFlow所有子组件设置了相同的constraintSize。

3.itemConstraintSize通过以上两种方式转换成FlowItem的constraintSize后的生效规则与通用属性[constraintSize](尺寸设置.md#ZH-CN_TOPIC_0000002497444850__constraintsize)相同。

#### columnsGap

columnsGap(value: Length)

设置列与列的间距。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明value[Length](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__length)是

列与列的间距。

默认值：0

取值范围：[0, +∞)

#### rowsGap

rowsGap(value: Length)

设置行与行的间距。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明value[Length](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__length)是

行与行的间距。

默认值：0

取值范围：[0, +∞)

#### layoutDirection

layoutDirection(value: FlexDirection)

设置布局的主轴方向。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明value[FlexDirection](../../guides/枚举说明.md#ZH-CN_TOPIC_0000002529284967__flexdirection)是

布局的主轴方向。

默认值：FlexDirection.Column

layoutDirection优先级高于rowsTemplate和columnsTemplate。根据layoutDirection设置情况，分为以下三种设置模式：

-

layoutDirection设置纵向布局（FlexDirection.Column 或 FlexDirection.ColumnReverse）

此时columnsTemplate有效（如果未设置，取默认值）。例如columnsTemplate设置为'1fr 1fr'、rowsTemplate设置为'1fr 1fr 1fr'时，瀑布流组件纵向布局，辅轴均分成横向2列。

-

layoutDirection设置横向布局（FlexDirection.Row 或 FlexDirection.RowReverse）

此时rowsTemplate有效（如果未设置，取默认值）。例如columnsTemplate设置为'1fr 1fr'、rowsTemplate设置为'1fr 1fr 1fr'时，瀑布流组件横向布局，辅轴均分成纵向3列。

-

layoutDirection未设置布局方向

布局方向为layoutDirection的默认值：FlexDirection.Column，此时columnsTemplate有效。例如columnsTemplate设置为'1fr 1fr'、rowsTemplate设置为'1fr 1fr 1fr'时，瀑布流组件纵向布局，辅轴均分成横向2列。

#### enableScrollInteraction10+

enableScrollInteraction(value: boolean)

设置是否支持滚动手势。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明valueboolean是

是否支持滚动手势。设置为true时可以通过手指或者鼠标滚动，设置为false时无法通过手指或者鼠标滚动，但不影响控制器[Scroller](../components/Scroll.md#ZH-CN_TOPIC_0000002497444896__scroller)的滚动接口。

默认值：true

组件无法通过鼠标按下拖动操作进行滚动。

#### nestedScroll10+

nestedScroll(value: NestedScrollOptions)

设置前后两个方向的嵌套滚动模式，实现与父组件的滚动联动。使用方法参考[嵌套滚动实现方式二](../components/Scroll.md#ZH-CN_TOPIC_0000002497444896__示例3嵌套滚动实现方式二)。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明value[NestedScrollOptions](滚动组件通用接口.md#ZH-CN_TOPIC_0000002529284871__nestedscrolloptions10对象说明)是嵌套滚动选项。

#### friction10+

friction(value: number | Resource)

设置摩擦系数，手动划动滚动区域时生效，仅影响惯性滚动过程，对惯性滚动过程中的链式效果有间接影响。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明valuenumber | [Resource](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resource)是

摩擦系数。

默认值：非可穿戴设备为0.6，可穿戴设备为0.9。

从API version 11开始，非可穿戴设备默认值为0.7。

从API version 12开始，非可穿戴设备默认值为0.75。

取值范围：(0, +∞)，设置为小于等于0的值时，按默认值处理。

#### cachedCount11+

cachedCount(value: number)

设置预加载的FlowItem数量。

只在[LazyForEach](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-rendering-control-lazyforeach)和开启了[virtualScroll](Repeat.md#ZH-CN_TOPIC_0000002497604972__virtualscroll)开关的[Repeat](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-rendering-control-repeat)中生效，超出显示及缓存范围的FlowItem会被释放。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明valuenumber是

预加载的FlowItem的数量。

默认值：根据屏幕内显示的节点个数设置，最大值为16。

取值范围：[0, +∞)，设置为小于0的值时，按1处理。

#### cachedCount14+

cachedCount(count: number, show: boolean)

设置预加载的FlowItem数量，并配置是否显示预加载节点。

配合[clip](形状裁剪.md#ZH-CN_TOPIC_0000002529284827__clip12)或[clipContent](滚动组件通用接口.md#ZH-CN_TOPIC_0000002529284871__clipcontent14)属性可以显示出预加载节点。

只在[LazyForEach](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-rendering-control-lazyforeach)和开启了virtualScroll开关的[Repeat](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-rendering-control-repeat)中生效，超出显示及缓存范围的FlowItem会被释放。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明countnumber是

预加载的FlowItem的数量。

默认值：根据屏幕内显示的节点个数设置，最大值为16。

取值范围：[0, +∞)，设置为小于0的值时，按1处理。

showboolean是

被预加载的FlowItem是否需要显示。设置为true时显示预加载的FlowItem，设置为false时不显示预加载的FlowItem。

默认值：false

#### syncLoad20+

syncLoad(enable: boolean)

设置是否同步加载WaterFlow区域内所有子组件。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明enableboolean是

是否同步加载WaterFlow区域内所有子组件。

true表示同步加载，false表示异步加载。

默认值：true。

**说明：**

设置为false时，在首次显示、不带动画[scrollToIndex](../components/Scroll.md#ZH-CN_TOPIC_0000002497444896__scrolltoindex)跳转场景，若当帧布局耗时超过50ms，会将WaterFlow区域内尚未布局的子组件延后到下一帧进行布局。

#### 事件

除支持[通用事件](通用事件.md)和[滚动组件通用事件](滚动组件通用接口.md#ZH-CN_TOPIC_0000002529284871__事件)外，还支持以下事件：

#### onReachStart

onReachStart(event: () => void)

瀑布流内容到达起始位置时触发。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明event() => void是瀑布流内容到达起始位置时触发的回调。

#### onReachEnd

onReachEnd(event: () => void)

瀑布流内容到达末尾位置时触发。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明event() => void是瀑布流内容到达末尾位置时触发的回调。

#### onScrollFrameBegin10+

onScrollFrameBegin(event: OnScrollFrameBeginCallback)

该接口回调时，事件参数传入即将发生的滑动量，事件处理函数中可根据应用场景计算实际需要的滑动量并作为事件处理函数的返回值返回，瀑布流将按照返回值的实际滑动量进行滑动。

满足以下任一条件时触发该事件：

1. 用户交互（如手指滑动、键鼠操作等）触发滚动。
1. WaterFlow惯性滚动。
1. 调用[fling](../components/Scroll.md#ZH-CN_TOPIC_0000002497444896__fling12)接口触发滚动。

不触发该事件的条件：

1. 调用除[fling](../components/Scroll.md#ZH-CN_TOPIC_0000002497444896__fling12)接口外的其他滚动控制接口。
1. 越界回弹。
1. 拖动滚动条。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明event[OnScrollFrameBeginCallback](../components/Scroll.md#ZH-CN_TOPIC_0000002497444896__onscrollframebegincallback18)是每帧滚动开始回调函数。

#### onScrollIndex11+

onScrollIndex(event: (first: number, last: number) => void)

当前瀑布流显示的起始位置/终止位置的子组件发生变化时触发。瀑布流初始化时会触发一次。

瀑布流显示区域上第一个子组件/最后一个组件的索引值有变化就会触发。

从API version 20开始，该接口支持在[attributeModifier](动态属性设置.md#ZH-CN_TOPIC_0000002529284843__attributemodifier)中调用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明firstnumber是

当前显示的瀑布流起始位置的索引值。

取值范围：[0, 子节点总数-1]

lastnumber是

当前显示的瀑布流终止位置的索引值。

取值范围：[0, 子节点总数-1]

通过last参数可以判断是否“继续加载数据”，参考[示例3使用分组](#ZH-CN_TOPIC_0000002497604876__示例3使用分组)中“即将触底时提前增加数据”的处理逻辑。

当WaterFlow列表为空时，使用不同的WaterFlowOptions参数会导致onScrollIndex事件的返回值有所不同。具体差异请参见下表：

layoutModesectionsfirstlastALWAYS_TOP_DOWN无00ALWAYS_TOP_DOWN有0-1SLIDING_WINDOW可选1000000-1

#### UIWaterFlowEvent19+

frameNode中[getEvent('WaterFlow')](../components/FrameNode.md#ZH-CN_TOPIC_0000002529284787__geteventwaterflow19)方法的返回值，可用于给WaterFlow节点设置滚动事件。

UIWaterFlowEvent继承于[UIScrollableCommonEvent](滚动组件通用接口.md#ZH-CN_TOPIC_0000002529284871__uiscrollablecommonevent19)。

#### setOnWillScroll19+

setOnWillScroll(callback: OnWillScrollCallback | undefined): void

设置[onWillScroll](滚动组件通用接口.md#ZH-CN_TOPIC_0000002529284871__onwillscroll12)事件的回调。

方法入参为undefined时，会重置事件回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明callback[OnWillScrollCallback](滚动组件通用接口.md#ZH-CN_TOPIC_0000002529284871__onwillscrollcallback12) | undefined是onWillScroll事件的回调函数。

#### setOnDidScroll19+

setOnDidScroll(callback: OnScrollCallback | undefined): void

设置[onDidScroll](滚动组件通用接口.md#ZH-CN_TOPIC_0000002529284871__ondidscroll12)事件的回调。

方法入参为undefined时，会重置事件回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明callback[OnScrollCallback](滚动组件通用接口.md#ZH-CN_TOPIC_0000002529284871__onscrollcallback12) | undefined是onDidScroll事件的回调函数。

#### setOnScrollIndex19+

setOnScrollIndex(callback: OnWaterFlowScrollIndexCallback | undefined): void

设置[onScrollIndex](#ZH-CN_TOPIC_0000002497604876__onscrollindex11)事件的回调。

方法入参为undefined时，会重置事件回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明callback[OnWaterFlowScrollIndexCallback](#ZH-CN_TOPIC_0000002497604876__onwaterflowscrollindexcallback19) | undefined是onScrollIndex事件的回调函数。

#### OnWaterFlowScrollIndexCallback19+

type OnWaterFlowScrollIndexCallback = (first: number, last: number) => void

WaterFlow组件可见区域item变化事件的回调类型。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明firstnumber是当前显示的瀑布流起始位置的索引值。lastnumber是当前显示的瀑布流终止位置的索引值。

#### 示例

#### 示例1（使用基本瀑布流）

该示例展示了WaterFlow组件数据加载处理、属性设置和事件回调等基本使用场景。

WaterFlowDataSource实现了LazyForEach数据源接口[IDataSource](LazyForEach.md#ZH-CN_TOPIC_0000002529444937__idatasource)，用于通过LazyForEach给WaterFlow提供子组件。

```ets
// WaterFlowDataSource.ets

// 实现IDataSource接口的对象，用于瀑布流组件加载数据
export class WaterFlowDataSource implements IDataSource {
  private dataArray: number[] = [];
  private listeners: DataChangeListener[] = [];

  constructor() {
    for (let i = 0; i < 100; i++) {
      this.dataArray.push(i);
    }
  }

  // 获取索引对应的数据
  public getData(index: number): number {
    return this.dataArray[index];
  }

  // 通知控制器数据重新加载
  notifyDataReload(): void {
    this.listeners.forEach(listener => {
      listener.onDataReloaded();
    })
  }

  // 通知控制器数据增加
  notifyDataAdd(index: number): void {
    this.listeners.forEach(listener => {
      listener.onDataAdd(index);
    })
  }

  // 通知控制器数据变化
  notifyDataChange(index: number): void {
    this.listeners.forEach(listener => {
      listener.onDataChange(index);
    })
  }

  // 通知控制器数据删除
  notifyDataDelete(index: number): void {
    this.listeners.forEach(listener => {
      listener.onDataDelete(index);
    })
  }

  // 通知控制器数据位置变化
  notifyDataMove(from: number, to: number): void {
    this.listeners.forEach(listener => {
      listener.onDataMove(from, to);
    })
  }

  //通知控制器数据批量修改
  notifyDatasetChange(operations: DataOperation[]): void {
    this.listeners.forEach(listener => {
      listener.onDatasetChange(operations);
    })
  }

  // 获取数据总数
  public totalCount(): number {
    return this.dataArray.length;
  }

  // 注册改变数据的控制器
  registerDataChangeListener(listener: DataChangeListener): void {
    if (this.listeners.indexOf(listener) < 0) {
      this.listeners.push(listener);
    }
  }

  // 注销改变数据的控制器
  unregisterDataChangeListener(listener: DataChangeListener): void {
    const pos = this.listeners.indexOf(listener);
    if (pos >= 0) {
      this.listeners.splice(pos, 1);
    }
  }

  // 增加数据
  public add1stItem(): void {
    this.dataArray.splice(0, 0, this.dataArray.length);
    this.notifyDataAdd(0);
  }

  // 在数据尾部增加一个元素
  public addLastItem(): void {
    this.dataArray.splice(this.dataArray.length, 0, this.dataArray.length);
    this.notifyDataAdd(this.dataArray.length - 1);
  }

  // 在指定索引位置增加一个元素
  public addItem(index: number): void {
    this.dataArray.splice(index, 0, this.dataArray.length);
    this.notifyDataAdd(index);
  }

  // 删除第一个元素
  public delete1stItem(): void {
    this.dataArray.splice(0, 1);
    this.notifyDataDelete(0);
  }

  // 删除第二个元素
  public delete2ndItem(): void {
    this.dataArray.splice(1, 1);
    this.notifyDataDelete(1);
  }

  // 删除最后一个元素
  public deleteLastItem(): void {
    this.dataArray.splice(-1, 1);
    this.notifyDataDelete(this.dataArray.length);
  }

  // 在指定索引位置删除一个元素
  public deleteItem(index: number): void {
    this.dataArray.splice(index, 1);
    this.notifyDataDelete(index);
  }

  // 重新加载数据
  public reload(): void {
    this.dataArray.splice(1, 1);
    this.dataArray.splice(3, 2);
    this.notifyDataReload();
  }

  // 在数据尾部增加count个元素
  public addNewItems(count: number): void {
    let len = this.dataArray.length;
    for (let i = 0; i < count; i++) {
      this.dataArray.push(this.dataArray[len - 1] + i + 1);
      this.notifyDataAdd(this.dataArray.length - 1);
    }
  }

  // 刷新所有元素
  public refreshItems(): void {
    let newDataArray: number[] = [];
    for (let i = 0; i < 100; i++) {
      newDataArray.push(this.dataArray[0] + i + 1000);
    }
    this.dataArray = newDataArray;
    this.notifyDataReload();
  }
}
```

```ets
// Index.ets
import { WaterFlowDataSource } from './WaterFlowDataSource';

enum FooterState {
  Loading = 0,
  End = 1
}

@Entry
@Component
struct WaterFlowDemo {
  @State minSize: number = 80;
  @State maxSize: number = 180;
  @State colors: number[] = [0xFFC0CB, 0xDA70D6, 0x6B8E23, 0x6A5ACD, 0x00FFFF, 0x00FF7F];
  @State footerState: FooterState = FooterState.Loading;
  scroller: Scroller = new Scroller();
  dataSource: WaterFlowDataSource = new WaterFlowDataSource();
  private itemWidthArray: number[] = [];
  private itemHeightArray: number[] = [];

  // 计算FlowItem宽/高
  getSize() {
    let ret = Math.floor(Math.random() * this.maxSize);
    return (ret > this.minSize ? ret : this.minSize);
  }

  // 设置FlowItem的宽/高数组
  setItemSizeArray() {
    for (let i = 0; i < 100; i++) {
      this.itemWidthArray.push(this.getSize());
      this.itemHeightArray.push(this.getSize());
    }
  }

  // 组件生命周期：在组件即将出现时初始化尺寸数组
  aboutToAppear() {
    this.setItemSizeArray();
  }

  @Builder
  itemFoot() {
    // 注意：不要直接用IfElse节点作为footer的根节点
    // 必须在外面使用(Column/Row/Stack等)容器包裹，确保布局正确
    Column() {
      if (this.footerState == FooterState.Loading) {
        Text(`加载中...`)
          .fontSize(10)
          .backgroundColor(Color.Red)
          .width(50)
          .height(50)
          .align(Alignment.Center)
          .margin({ top: 2 })
      } else if (this.footerState == FooterState.End) {
        Text(`到底啦...`)
          .fontSize(10)
          .backgroundColor(Color.Red)
          .width(50)
          .height(50)
          .align(Alignment.Center)
          .margin({ top: 2 })
      } else {
        Text(`Footer`)
          .fontSize(10)
          .backgroundColor(Color.Red)
          .width(50)
          .height(50)
          .align(Alignment.Center)
          .margin({ top: 2 })
      }
    }
  }

  build() {
    Column({ space: 2 }) {
      WaterFlow({ footer: this.itemFoot() }) {
        LazyForEach(this.dataSource, (item: number) => {
          FlowItem() {
            Column() {
              Text('N' + item).fontSize(12).height('16')
              // 注意：需要确保对应的jpg文件存在才会正常显示
              Image('res/waterFlowTest(' + item % 5 + ').jpg')
                .objectFit(ImageFit.Fill)
                .width('100%')
                .layoutWeight(1)
            }
          }
          .width('100%')
          .height(this.itemHeightArray[item % 100])
          .backgroundColor(this.colors[item % this.colors.length])
        }, (item: string) => item)
      }
      .columnsTemplate('1fr 1fr')    // 设置2列等宽布局
      .columnsGap(10)
      .rowsGap(5)
      .backgroundColor(0xFAEEE0)
      .width('100%')
      .height('100%')
      .itemConstraintSize({minWidth:80,maxWidth:180,minHeight:80,maxHeight:180})
      // 触底加载数据：滚动到底部时触发分页加载
      .onReachEnd(() => {
        console.info('onReachEnd')

        // 模拟分页加载：当数据超过200条时停止加载
        if (this.dataSource.totalCount() > 200) {
          this.footerState = FooterState.End;
          return;
        }
        setTimeout(() => {
          for (let i = 0; i < 100; i++) {
            this.dataSource.addLastItem();
          }
        }, 1000)
      })
      .onReachStart(() => {
        // 滚动到顶部时触发
        console.info('waterFlow reach start');
      })
      .onScrollStart(() => {
        // 开始滚动时触发
        console.info('waterFlow scroll start');
      })
      .onScrollStop(() => {
        // 停止滚动时触发
        console.info('waterFlow scroll stop');
      })
      .onScrollFrameBegin((offset: number, state: ScrollState) => {
        // 滚动帧开始时触发：可以控制滚动行为
        // offset：滚动偏移量，state：滚动状态
        console.info('waterFlow scrollFrameBegin offset: ' + offset + ' state: ' + state.toString());
        return { offsetRemain: offset };  // 返回开发者期望的实际滚动偏移量
      })
    }
  }
}
```

#### 示例2（自动计算列数）

该示例通过auto-fill实现了自动计算列数的效果。

WaterFlowDataSource说明及完整代码参考[示例1使用基本瀑布流](#ZH-CN_TOPIC_0000002497604876__示例1使用基本瀑布流)。

```ets
// Index.ets
import { WaterFlowDataSource } from './WaterFlowDataSource';

@Entry
@Component
struct WaterFlowDemo {
  @State minSize: number = 80;
  @State maxSize: number = 180;
  @State colors: number[] = [0xFFC0CB, 0xDA70D6, 0x6B8E23, 0x6A5ACD, 0x00FFFF, 0x00FF7F];
  dataSource: WaterFlowDataSource = new WaterFlowDataSource();
  private itemWidthArray: number[] = [];
  private itemHeightArray: number[] = [];

  // 计算FlowItem宽/高
  getSize() {
    let ret = Math.floor(Math.random() * this.maxSize);
    return (ret > this.minSize ? ret : this.minSize);
  }

  // 设置FlowItem宽/高数组
  setItemSizeArray() {
    for (let i = 0; i < 100; i++) {
      this.itemWidthArray.push(this.getSize());
      this.itemHeightArray.push(this.getSize());
    }
  }

  // 组件生命周期：在组件即将出现时初始化尺寸数组
  aboutToAppear() {
    this.setItemSizeArray();
  }

  build() {
    Column({ space: 2 }) {
      WaterFlow() {
        LazyForEach(this.dataSource, (item: number) => {
          FlowItem() {
            Column() {
              Text('N' + item).fontSize(12).height('16')
              // 存在对应的jpg文件才会显示图片
              Image('res/waterFlowTest(' + item % 5 + ').jpg')
            }
          }
          .width('100%')
          .height(this.itemHeightArray[item % 100])
          .backgroundColor(this.colors[item % this.colors.length])
        }, (item: string) => item)
      }
      // auto-fill自动计算列数
      // 'repeat(auto-fill,80)' 表示：根据容器宽度自动计算能放下多少个80px宽的列
      // 例如：容器宽度400px，则自动计算为5列（400÷80=5）
      .columnsTemplate('repeat(auto-fill,80)')
      .columnsGap(10)
      .rowsGap(5)
      .padding({left:5})
      .backgroundColor(0xFAEEE0)
      .width('100%')
      .height('100%')
    }
  }
}
```

#### 示例3（使用分组）

该示例展示了分组的初始化以及splice、push、update、values、length等接口的不同效果。

如果配合状态管理V2使用，详情见：[WaterFlow与makeObserved](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-v1-v2-migration-application-and-others#滚动组件)。

WaterFlowDataSource说明及完整代码参考[示例1使用基本瀑布流](#ZH-CN_TOPIC_0000002497604876__示例1使用基本瀑布流)。

```ets
// Index.ets
import { WaterFlowDataSource } from './WaterFlowDataSource';

// 可复用组件：优化性能，减少组件创建销毁开销
@Reusable
@Component
struct ReusableFlowItem {
  @State item: number = 0;

  // 组件复用生命周期：从复用缓存中取出时调用
  // 用于更新组件状态，显示新的内容
  aboutToReuse(params: Record<string, number>) {
    this.item = params.item;
    console.info('Reuse item:' + this.item);
  }

  // 组件生命周期：初始化尺寸数组和分组配置
  aboutToAppear() {
    console.info('new item:' + this.item);
  }

  build() {
    Column() {
      // 注意：需要确保对应的jpg文件存在才会正常显示
      Image('res/waterFlowTest(' + this.item % 5 + ').jpg')
        .overlay('N' + this.item, { align: Alignment.Top })
        .objectFit(ImageFit.Fill)
        .width('100%')
        .layoutWeight(1)
    }
  }
}

@Entry
@Component
struct WaterFlowDemo {
  minSize: number = 80;
  maxSize: number = 180;
  colors: number[] = [0xFFC0CB, 0xDA70D6, 0x6B8E23, 0x6A5ACD, 0x00FFFF, 0x00FF7F];
  scroller: Scroller = new Scroller();
  dataSource: WaterFlowDataSource = new WaterFlowDataSource();
  dataCount: number = this.dataSource.totalCount();
  private itemWidthArray: number[] = [];
  private itemHeightArray: number[] = [];
  // 分组管理：WaterFlow的核心特性，支持不同区域使用不同列数
  @State sections: WaterFlowSections = new WaterFlowSections();
  // 分组边距配置：统一的外边距设置
  sectionMargin: Margin = { top: 10, left: 5, bottom: 10, right: 5 };

  oneColumnSection: SectionOptions = {
    itemsCount: 4,                     // 该分组包含4个FlowItem
    crossCount: 1,                     // 使用1列布局
    columnsGap: '5vp',
    rowsGap: 10,
    margin: this.sectionMargin,
    // 回调函数：动态设置每个item的高度
    onGetItemMainSizeByIndex: (index: number) => {
      return this.itemHeightArray[index % 100];
    }
  };

  // 第二种分组：双列布局，适合展示列表内容
  twoColumnSection: SectionOptions = {
    itemsCount: 2,                     // 该分组包含2个FlowItem
    crossCount: 2,                     // 使用2列布局
    // 回调函数：固定高度100px
    onGetItemMainSizeByIndex: (index: number) => {
      return 100;
    }
  };

  // 最后一个分组：用于处理剩余数据
  lastSection: SectionOptions = {
    itemsCount: 20,                    // 该分组包含20个FlowItem
    crossCount: 2,                     // 使用2列布局
    // 回调函数：使用随机高度
    onGetItemMainSizeByIndex: (index: number) => {
      return this.itemHeightArray[index % 100];
    }
  };

  // 计算FlowItem高度
  getSize() {
    let ret = Math.floor(Math.random() * this.maxSize);
    return (ret > this.minSize ? ret : this.minSize);
  }

  // 设置FlowItem的高度数组
  setItemSizeArray() {
    for (let i = 0; i < 100; i++) {
      this.itemHeightArray.push(this.getSize());
    }
  }

  // 组件生命周期：初始化数据和恢复上次的列数设置
  aboutToAppear() {
    this.setItemSizeArray();

    // 初始化瀑布流分组信息：交替使用单列和双列布局
    let sectionOptions: SectionOptions[] = [];
    let count = 0;                     // 已分配的FlowItem数量计数
    let oneOrTwo = 0;                  // 用于交替选择分组类型

    while (count < this.dataCount) {
      // 剩余数据不足20个时，使用最后一个分组处理
      if (this.dataCount - count < 20) {
        this.lastSection.itemsCount = this.dataCount - count;
        sectionOptions.push(this.lastSection);
        break;
      }

      // 交替使用单列和双列布局
      if (oneOrTwo++ % 2 == 0) {
        sectionOptions.push(this.oneColumnSection);
        count += this.oneColumnSection.itemsCount;
      } else {
        sectionOptions.push(this.twoColumnSection);
        count += this.twoColumnSection.itemsCount;
      }
    }

    // 将配置好的分组添加到WaterFlow中
    this.sections.splice(0, 0, sectionOptions);
  }

  build() {
    Column({ space: 2 }) {
      Row() {
        Button('splice')
          .height('5%')
          .onClick(() => {
            // 重要：必须保证LazyForEach中数据数量和新分组itemsCount累计总数保持一致
            let totalCount: number = this.dataSource.totalCount();
            let newSection: SectionOptions = {
              itemsCount: totalCount,
              crossCount: 2,
              onGetItemMainSizeByIndex: (index: number) => {
                return this.itemHeightArray[index % 100];
              }
            };
            let oldLength: number = this.sections.length();
            this.sections.splice(0, oldLength, [newSection]);  // 替换所有分组
          })
          .margin({ top: 10, left: 20 })

        Button('update')
          .height('5%')
          .onClick(() => {
            // 在第一个分组中增加4个FlowItem
            // 重要：必须保证数据源和分组itemsCount同步更新
            const sections: Array<SectionOptions> = this.sections.values();
            let newSection: SectionOptions = sections[0];

            // 先在数据源中添加4个新数据
            this.dataSource.addItem(this.oneColumnSection.itemsCount);
            this.dataSource.addItem(this.oneColumnSection.itemsCount + 1);
            this.dataSource.addItem(this.oneColumnSection.itemsCount + 2);
            this.dataSource.addItem(this.oneColumnSection.itemsCount + 3);

            // 然后更新分组的itemsCount
            newSection.itemsCount += 4;
            const result: boolean = this.sections.update(0, newSection);
            console.info('update:' + result);
          })
          .margin({ top: 10, left: 20 })

        Button('delete')
          .height('5%')
          .onClick(() => {
            // 在第一个分组中减少4个FlowItem
            // 重要：必须保证数据源和分组itemsCount同步更新
            const sections: Array<SectionOptions> = this.sections.values();
            let newSection: SectionOptions = sections[0];

            // 检查是否有足够的item可以删除
            if (newSection.itemsCount < 4) {
              return;
            }

            // 先从数据源中删除4条数据
            this.dataSource.deleteItem(this.oneColumnSection.itemsCount - 1);
            this.dataSource.deleteItem(this.oneColumnSection.itemsCount - 2);
            this.dataSource.deleteItem(this.oneColumnSection.itemsCount - 3);
            this.dataSource.deleteItem(this.oneColumnSection.itemsCount - 4);

            // 更新分组的itemsCount
            newSection.itemsCount -= 4;
            this.sections.update(0, newSection);
          })
          .margin({ top: 10, left: 20 })

        Button('values')
          .height('5%')
          .onClick(() => {
            const sections: Array<SectionOptions> = this.sections.values();
            for (const value of sections) {
              console.info(JSON.stringify(value));
            }
            console.info('count:' + this.sections.length());
          })
          .margin({ top: 10, left: 20 })
      }.margin({ bottom: 20 })

      WaterFlow({ scroller: this.scroller, sections: this.sections }) {
        LazyForEach(this.dataSource, (item: number) => {
          FlowItem() {
            // 使用可复用组件，提升性能
            ReusableFlowItem({ item: item })
          }
          .width('100%')
          // 注意：同时设置onGetItemMainSizeByIndex和height属性时，
          // 主轴大小以onGetItemMainSizeByIndex返回结果为准
          .height(this.itemHeightArray[item % 100])
          .backgroundColor(this.colors[item % this.colors.length])
        }, (item: string) => item)
      }
      .columnsTemplate('1fr 1fr')
      .columnsGap(10)
      .rowsGap(5)
      .backgroundColor(0xFAEEE0)
      .width('100%')
      .height('100%')
      .layoutWeight(1)
      .onScrollIndex((first: number, last: number) => {
        // 滚动监听：即将触底时提前加载更多数据
        if (last + 20 >= this.dataSource.totalCount()) {
          // 添加100个新数据到数据源
          for (let i = 0; i < 100; i++) {
            this.dataSource.addLastItem();
          }

          // 重要：更新数据源后必须同步更新sections
          // 修改最后一个section的FlowItem数量
          const sections: Array<SectionOptions> = this.sections.values();
          let newSection: SectionOptions = sections[this.sections.length() - 1];
          newSection.itemsCount += 100;
          this.sections.update(-1, newSection);  // -1表示最后一个分组
        }
      })
    }
  }
}
```

#### 示例4（双指缩放改变列数）

该示例通过[priorityGesture](绑定手势方法.md#ZH-CN_TOPIC_0000002529284849__prioritygesture)和[PinchGesture](../input/PinchGesture.md)实现了双指缩放改变列数效果。

WaterFlowDataSource说明及完整代码参考[示例1使用基本瀑布流](#ZH-CN_TOPIC_0000002497604876__示例1使用基本瀑布流)。

```ets
// Index.ets
import { WaterFlowDataSource } from './WaterFlowDataSource';
import { image } from '@kit.ImageKit';

// 可复用组件：优化性能，减少组件创建销毁开销
@Reusable
@Component
struct ReusableFlowItem {
  @State item: number = 0;

  // 从复用缓存中加入到组件树之前调用，可在此处更新组件的状态变量以展示正确的内容
  aboutToReuse(params: Record<string, number>) {
    this.item = params.item;
  }

  build() {
    Column() {
      Text('N' + this.item).fontSize(12).height('16')
      // 注意：需要确保对应的jpg文件存在才会正常显示
      Image('res/waterFlow(' + this.item % 5 + ').jpg')
        .objectFit(ImageFit.Fill)
        .width('100%')
        .layoutWeight(1)
    }
  }
}

@Entry
@Component
struct WaterFlowDemo {
  minSize: number = 80;
  maxSize: number = 180;
  colors: number[] = [0xFFC0CB, 0xDA70D6, 0x6B8E23, 0x6A5ACD, 0x00FFFF, 0x00FF7F];
  dataSource: WaterFlowDataSource = new WaterFlowDataSource();
  private itemWidthArray: number[] = [];
  private itemHeightArray: number[] = [];
  @State columns: number = 2;
  @State waterFlowScale: number = 1;
  @State imageScale: number = 1;
  @State waterFlowOpacity: number = 1;
  @State waterFlowSnapshot: image.PixelMap | undefined = undefined;
  private columnChanged: boolean = false;
  private oldColumn: number = this.columns;
  private pinchTime: number = 0;

  // 计算FlowItem宽/高
  getSize() {
    let ret = Math.floor(Math.random() * this.maxSize);
    return (ret > this.minSize ? ret : this.minSize);
  }

  // 设置FlowItem的宽/高数组
  setItemSizeArray() {
    for (let i = 0; i < 100; i++) {
      this.itemWidthArray.push(this.getSize());
      this.itemHeightArray.push(this.getSize());
    }
  }

  // 组件生命周期：初始化数据和恢复上次的列数设置
  aboutToAppear() {
    // 读取上次最后切换到的列数
    let lastCount = AppStorage.get<number>('columnsCount');
    if (typeof lastCount != 'undefined') {
      this.columns = lastCount;
    }
    this.setItemSizeArray();
  }

  // 根据缩放阈值改变列数，触发WaterFlow重新布局
  changeColumns(scale: number) {
    if (scale > (this.columns / (this.columns - 0.5)) && this.columns > 1) {
      this.columns--;
      this.columnChanged = true;
    } else if (scale < 1 && this.columns < 4) {
      this.columns++;
      this.columnChanged = true;
    }
  }

  build() {
    Column({ space: 2 }) {
      Row() {
        Text('双指缩放改变列数')
          .height('5%')
          .margin({ top: 10, left: 20 })
      }

      Stack() {
        // 用于展示缩放前的WaterFlow截图
        Image(this.waterFlowSnapshot)
          .width('100%')
          .height('100%')
          .scale({
            x: this.imageScale,
            y: this.imageScale,
            centerX: 0,
            centerY: 0
          })

        WaterFlow() {
          LazyForEach(this.dataSource, (item: number) => {
            FlowItem() {
              // 使用可复用组件，提升性能
              ReusableFlowItem({ item: item })
            }
            .width('100%')
            .aspectRatio(this.itemHeightArray[item % 100] / this.itemWidthArray[item%100])
            .backgroundColor(this.colors[item % this.colors.length])
          }, (item: string) => item)
        }
        .id('waterflow') // 设置id用于截图
        .columnsTemplate('1fr '.repeat(this.columns))  // 动态生成列模板，如：'1fr 1fr 1fr'表示3列等宽
        .backgroundColor(0xFAEEE0)
        .width('100%')
        .height('100%')
        .layoutWeight(1)
        .opacity(this.waterFlowOpacity)
        .scale({
          x: this.waterFlowScale,
          y: this.waterFlowScale,
          centerX: 0,
          centerY: 0
        })
        .priorityGesture(
          PinchGesture()
            .onActionStart((event: GestureEvent) => {
              // 双指捏合手势识别成功时截图
              this.pinchTime = event.timestamp;
              this.columnChanged = false;
              this.oldColumn = this.columns;
              this.getUIContext().getComponentSnapshot().get('waterflow', (error: Error, pixmap: image.PixelMap) => {
                if (error) {
                  console.info('error:' + JSON.stringify(error));
                  return;
                }
                this.waterFlowSnapshot = pixmap;
              })
            })
            .onActionUpdate((event: GestureEvent) => {
              // 手势更新：处理缩放逻辑和视觉效果
              // 边界限制：防止超出列数范围时继续缩放
              if ((this.oldColumn === 1 && event.scale > 1) || (this.oldColumn === 4 && event.scale < 1)) {
                return;
              }

              // 节流处理：避免过于频繁的更新，提升性能
              if (event.timestamp - this.pinchTime < 10000000) {
                return;
              }
              this.pinchTime = event.timestamp;

              this.waterFlowScale = event.scale;
              this.imageScale = event.scale;
              // 根据缩放比例设置WaterFlow透明度
              this.waterFlowOpacity = (this.waterFlowScale > 1) ? (this.waterFlowScale - 1) : (1 - this.waterFlowScale);
              this.waterFlowOpacity *= 3;
              if (!this.columnChanged) {
                this.changeColumns(event.scale);
              }

              // 列数改变后的缩放比例调整：避免出现空白区域
              if (this.columnChanged) {
                this.waterFlowScale = this.imageScale * this.columns / this.oldColumn;

                // 限制缩放范围，确保视觉效果自然
                if (event.scale < 1) {
                  this.waterFlowScale = this.waterFlowScale > 1 ? this.waterFlowScale : 1;
                } else {
                  this.waterFlowScale = this.waterFlowScale < 1 ? this.waterFlowScale : 1;
                }
              }
            })
            .onActionEnd((event: GestureEvent) => {
              // 手势结束：执行归位动画并保存状态
              // 执行归位动画：平滑过渡到正常状态
              this.getUIContext()?.animateTo({ duration: 300 }, () => {
                this.waterFlowScale = 1;
                this.waterFlowOpacity = 1;
              })

              // 持久化保存当前列数：下次启动时恢复
              AppStorage.setOrCreate<number>('columnsCount', this.columns);
            })
        )
      }
    }
  }
}
```

#### 示例5（设置边缘渐隐效果）

该示例通过[fadingEdge](滚动组件通用接口.md#ZH-CN_TOPIC_0000002529284871__fadingedge14)实现了WaterFlow组件开启边缘渐隐效果，并通过fadingEdgeLength参数设置边缘渐隐长度。

WaterFlowDataSource说明及完整代码参考[示例1使用基本瀑布流](#ZH-CN_TOPIC_0000002497604876__示例1使用基本瀑布流)。

```ets
// Index.ets
import { LengthMetrics } from '@kit.ArkUI';
import { WaterFlowDataSource } from './WaterFlowDataSource';

@Entry
@Component
struct WaterFlowDemo {
  @State minSize: number = 80;
  @State maxSize: number = 180;
  @State colors: number[] = [0xFFC0CB, 0xDA70D6, 0x6B8E23, 0x6A5ACD, 0x00FFFF, 0x00FF7F];
  dataSource: WaterFlowDataSource = new WaterFlowDataSource();
  scroller: Scroller = new Scroller();
  private itemWidthArray: number[] = [];
  private itemHeightArray: number[] = [];

  // 计算FlowItem宽/高
  getSize() {
    let ret = Math.floor(Math.random() * this.maxSize);
    return (ret > this.minSize ? ret : this.minSize);
  }

  // 设置FlowItem宽/高数组
  setItemSizeArray() {
    for (let i = 0; i < 100; i++) {
      this.itemWidthArray.push(this.getSize());
      this.itemHeightArray.push(this.getSize());
    }
  }

  // 组件生命周期：在组件即将出现时初始化尺寸数组
  aboutToAppear() {
    this.setItemSizeArray();
  }

  build() {
    Column({ space: 2 }) {
      WaterFlow({ scroller: this.scroller }) {
        LazyForEach(this.dataSource, (item: number) => {
          FlowItem() {
            Column() {
              Text('N' + item).fontSize(12).height('16')
            }
          }
          .width('100%')
          .height(this.itemHeightArray[item % 100])
          .backgroundColor(this.colors[item % 5])
        }, (item: string) => item)
      }
      // auto-fill自动计算列数：根据容器宽度自动计算能放下多少个80px宽的列
      .columnsTemplate('repeat(auto-fill,80)')
      .columnsGap(10)
      .rowsGap(5)
      .height('90%')
      .scrollBar(BarState.On)
      // 边缘渐隐效果：在滚动边缘创建渐隐过渡效果
      // true：启用渐隐效果
      // fadingEdgeLength: LengthMetrics.vp(80)：渐隐区域长度为80vp
      // 效果：在瀑布流顶部和底部边缘会有80vp的渐隐过渡区域
      .fadingEdge(true, { fadingEdgeLength: LengthMetrics.vp(80) })
    }
  }
}
```

#### 示例6（单边边缘效果）

该示例通过[edgeEffect](滚动组件通用接口.md#ZH-CN_TOPIC_0000002529284871__edgeeffect11)接口，实现了WaterFlow组件设置单边边缘效果。

WaterFlowDataSource说明及完整代码参考[示例1使用基本瀑布流](#ZH-CN_TOPIC_0000002497604876__示例1使用基本瀑布流)。

```ets
// Index.ets
import { WaterFlowDataSource } from './WaterFlowDataSource';

@Entry
@Component
struct WaterFlowDemo {
  @State minSize: number = 80;
  @State maxSize: number = 180;
  @State colors: number[] = [0xFFC0CB, 0xDA70D6, 0x6B8E23, 0x6A5ACD, 0x00FFFF, 0x00FF7F];
  dataSource: WaterFlowDataSource = new WaterFlowDataSource();
  scroller: Scroller = new Scroller();
  private itemWidthArray: number[] = [];
  private itemHeightArray: number[] = [];

  // 计算FlowItem宽/高
  getSize() {
    let ret = Math.floor(Math.random() * this.maxSize);
    return (ret > this.minSize ? ret : this.minSize);
  }

  // 设置FlowItem宽/高数组
  setItemSizeArray() {
    for (let i = 0; i < 100; i++) {
      this.itemWidthArray.push(this.getSize());
      this.itemHeightArray.push(this.getSize());
    }
  }

  // 组件生命周期：在组件即将出现时初始化尺寸数组
  aboutToAppear() {
    this.setItemSizeArray();
  }

  build() {
    Column({ space: 2 }) {
      WaterFlow({ scroller: this.scroller }) {
        LazyForEach(this.dataSource, (item: number) => {
          FlowItem() {
            Column() {
              Text('N' + item).fontSize(12).height('16')
            }
          }
          .width('100%')
          .height(this.itemHeightArray[item % 100])
          .backgroundColor(this.colors[item % 5])
        }, (item: number) => item.toString())
      }
      // auto-fill自动计算列数：根据容器宽度自动计算能放下多少个80px宽的列
      .columnsTemplate('repeat(auto-fill,80)')
      .columnsGap(10)
      .rowsGap(5)
      .height('90%')
      // 单边边缘效果：设置弹簧效果，仅在顶部生效
      // EdgeEffect.Spring：弹簧回弹效果，滑动到边界时会有弹性回弹
      // alwaysEnabled: true：始终启用边缘效果，即使内容不足以滚动
      // effectEdge: EffectEdge.START：仅在起始边缘（顶部）生效
      // 效果：只有向上滑动到顶部时才会有弹簧回弹效果，向下滑动到底部不会有效果
      .edgeEffect(EdgeEffect.Spring, { alwaysEnabled: true, effectEdge: EffectEdge.START })

    }
  }
}
```

#### 示例7（WaterFlow组件设置和改变尾部组件）

从API version 18开始，该示例通过[WaterFlowOptions对象说明](#ZH-CN_TOPIC_0000002497604876__waterflowoptions对象说明)的footerContent接口，实现了WaterFlow组件设置尾部组件。通过[ComponentContent](../components/ComponentContent.md)的update函数更新尾部组件。

WaterFlowDataSource说明及完整代码参考[示例1使用基本瀑布流](#ZH-CN_TOPIC_0000002497604876__示例1使用基本瀑布流)。

```ets
// Index.ets
import { ComponentContent, UIContext } from '@kit.ArkUI';
import { WaterFlowDataSource } from './WaterFlowDataSource';

class Params {
  text: string = '';

  constructor(text: string) {
    this.text = text;
  }
}

// Builder函数：构建尾部组件的UI结构
@Builder
function buildText(params: Params) {
  Column() {
    Text(params.text)
      .fontSize(20)
      .fontWeight(FontWeight.Bold)
      .margin(20)
  }
}

@Entry
@Component
struct Index {
  @State message1: string = '已经到底了';
  @State message2: string = '加载更多';
  @State colors: number[] = [0xD5D5D5, 0x7F7F7F, 0xF7F7F7];
  @State minSize: number = 80;
  @State maxSize: number = 180;

  // UI上下文：用于创建ComponentContent
  context: UIContext = this.getUIContext();

  // 动态尾部组件：使用ComponentContent创建可更新的尾部组件
  // ComponentContent<Params>：泛型指定参数类型
  // wrapBuilder<[Params]>(buildText)：包装Builder函数
  // new Params(this.message1)：初始参数，显示'已经到底了'
  footerContent: ComponentContent<Params> = new ComponentContent<Params>(
    this.context,
    wrapBuilder<[Params]>(buildText),
    new Params(this.message1)
  );

  dataSource: WaterFlowDataSource = new WaterFlowDataSource();
  private itemWidthArray: number[] = [];
  private itemHeightArray: number[] = [];

  // 计算FlowItem宽/高
  getSize() {
    let ret = Math.floor(Math.random() * this.maxSize);
    return (ret > this.minSize ? ret : this.minSize);
  }

  // 设置FlowItem宽/高数组
  setItemSizeArray() {
    for (let i = 0; i < 100; i++) {
      this.itemWidthArray.push(this.getSize());
      this.itemHeightArray.push(this.getSize());
    }
  }

  // 组件生命周期：在组件即将出现时初始化尺寸数组
  aboutToAppear() {
    this.setItemSizeArray();
  }

  build() {
    Row() {
      Column() {
        Button('更新footer').width('90%').margin(20)
          .onClick((event?: ClickEvent) => {
            // 调用ComponentContent的update方法更新尾部组件
            // 传入新的Params对象，文本内容从'已经到底了'变为'加载更多'
            this.footerContent.update(new Params(this.message2));
          })
        WaterFlow({ footerContent: this.footerContent }) {
          LazyForEach(this.dataSource, (item: number) => {
            FlowItem() {
              Column() {
                Text('N' + item).fontSize(12).height('16')
              }
              .width('100%')
              .height(this.itemHeightArray[item % 100])
              .backgroundColor(this.colors[item % 3])
              .justifyContent(FlexAlign.Center)
              .alignItems(HorizontalAlign.Center)
            }
          }, (item: number) => item.toString())
        }
        .columnsTemplate('1fr')
        .height('90%')
      }
      .width('100%')
      .height('100%')
    }
    .height('100%')
  }
}
```

#### 示例8（WaterFlow组件实现下拉刷新）

该示例通过[Refresh](refresh.md)组件和WaterFlow组件，实现了下拉刷新瀑布流组件数据源。

WaterFlowDataSource说明及完整代码参考[示例1使用基本瀑布流](#ZH-CN_TOPIC_0000002497604876__示例1使用基本瀑布流)。

```ets
// Index.ets
import { WaterFlowDataSource } from './WaterFlowDataSource';

@Entry
@Component
struct WaterFlowDemo {
  @State minSize: number = 80;
  @State maxSize: number = 180;
  @State colors: number[] = [0xFFC0CB, 0xDA70D6, 0x6B8E23, 0x6A5ACD, 0x00FFFF, 0x00FF7F];
  @State isRefreshing: boolean = false;
  dataSource: WaterFlowDataSource = new WaterFlowDataSource();
  scroller: Scroller = new Scroller();
  private itemWidthArray: number[] = [];
  private itemHeightArray: number[] = [];

  // 计算FlowItem宽/高
  getSize() {
    let ret = Math.floor(Math.random() * this.maxSize);
    return (ret > this.minSize ? ret : this.minSize);
  }

  // 设置FlowItem宽/高数组
  setItemSizeArray() {
    for (let i = 0; i < 100; i++) {
      this.itemWidthArray.push(this.getSize());
      this.itemHeightArray.push(this.getSize());
    }
  }

  // 组件生命周期：在组件即将出现时初始化尺寸数组
  aboutToAppear() {
    this.setItemSizeArray();
  }

  build() {
    Column({ space: 2 }) {
      // refreshing: $$this.isRefreshing：双向绑定刷新状态
      Refresh({ refreshing: $$this.isRefreshing }) {
        WaterFlow({ scroller: this.scroller }) {
          LazyForEach(this.dataSource, (item: number) => {
            FlowItem() {
              Column() {
                Text('N' + item).fontSize(12).height('16')
              }
            }
            .width('100%')
            .height(this.itemHeightArray[item % 100])
            .backgroundColor(this.colors[item % this.colors.length])
          }, (item: number) => item.toString())
        }
        // auto-fill自动计算列数：根据容器宽度自动计算能放下多少个80px宽的列
        .columnsTemplate('repeat(auto-fill,80)')
        .columnsGap(10)
        .rowsGap(5)
        .height('90%')
        // 边缘效果：弹簧回弹效果
        .edgeEffect(EdgeEffect.Spring, { alwaysEnabled: true })
        .onReachEnd(() => {
          // 触底加载更多数据：滚动到底部时触发
          setTimeout(() => {
            this.dataSource.addNewItems(100);
          }, 1000)
        })
      }
      .onStateChange((refreshStatus: RefreshStatus) => {
        // 刷新状态变化监听：处理不同的刷新状态
        if (refreshStatus === RefreshStatus.Done) {
          // 刷新完成时：调用数据源的刷新方法，更新所有数据
          this.dataSource.refreshItems();
        }
      })
      .onRefreshing(() => {
        // 正在刷新时的回调：模拟刷新过程
        setTimeout(() => {
          this.isRefreshing = false;
        }, 1000)
      })
    }
  }
}
```

#### 示例9（WaterFlow组件基于断点配置列数）

从API version 22开始，该示例展示了WaterFlow组件支持基于断点配置列数效果。

```ets
// Index.ets
import { WaterFlowDataSource } from './WaterFlowDataSource';

@Entry
@Component
struct WaterFlowDemo {
  minSize: number = 80;
  maxSize: number = 180;
  colors: number[] = [0xFFC0CB, 0xDA70D6, 0x6B8E23, 0x6A5ACD, 0x00FFFF, 0x00FF7F];
  dataSource: WaterFlowDataSource = new WaterFlowDataSource();
  private itemHeightArray: number[] = [];

  // 计算FlowItem宽/高
  getSize() {
    let ret = Math.floor(Math.random() * this.maxSize);
    return (ret > this.minSize ? ret : this.minSize);
  }

  // 设置FlowItem的宽/高数组
  setItemSizeArray() {
    for (let i = 0; i < 100; i++) {
      this.itemHeightArray.push(this.getSize());
    }
  }

  // 组件生命周期：在组件即将出现时初始化尺寸数组
  aboutToAppear() {
    this.setItemSizeArray();
  }

  build() {
    Column({ space: 2 }) {
      WaterFlow() {
        LazyForEach(this.dataSource, (item: number) => {
          FlowItem() {
            Column() {
              Text('N' + item).fontSize(12).height('16')
              // 注意：需要确保对应的jpg文件存在才会正常显示
              Image('res/waterFlowTest(' + item % 5 + ').jpg')
                .objectFit(ImageFit.Fill)
                .width('100%')
                .layoutWeight(1)
            }
          }
          .width('100%')
          .height(this.itemHeightArray[item % 100])
          .backgroundColor(this.colors[item % this.colors.length])
        }, (item: string) => item)
      }
      .key('waterFlow')
      // 设置WaterFlow按断点决定列数
      .columnsTemplate({fillType:PresetFillType.BREAKPOINT_SM2MD3LG5})
      .columnsGap(10)
      .rowsGap(5)
      .backgroundColor(0xFAEEE0)
      .margin('20vp')
      .width('100%')
      .height('30%')
    }
  }
}
```

WaterFlow宽度属于sm及更小的断点区间时显示2列。

WaterFlow宽度属于md断点区间时显示3列。

WaterFlow宽度属于lg及更大的断点区间时显示5列。

#### 示例10（WaterFlow组件实现获取内容高度）

从API version 22 开始，该示例通过WaterFlow组件，实现了获取内容高度。

WaterFlowDataSource说明及完整代码参考[示例1使用基本瀑布流](#ZH-CN_TOPIC_0000002497604876__示例1使用基本瀑布流)。

```ets
// Index.ets
import { WaterFlowDataSource } from './WaterFlowDataSource';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WaterFlowContentSizeDemo {
  @State minSize: number = 80;
  @State maxSize: number = 180;
  @State colors: number[] = [0xFFC0CB, 0xDA70D6, 0x6B8E23, 0x6A5ACD, 0x00FFFF, 0x00FF7F];
  @State contentWidth: number = -1;
  @State contentHeight: number = -1;
  scroller: Scroller = new Scroller();
  dataSource: WaterFlowDataSource = new WaterFlowDataSource();
  private itemWidthArray: number[] = [];
  private itemHeightArray: number[] = [];

  // 计算FlowItem宽/高
  getSize() {
    let ret = Math.floor(Math.random() * this.maxSize);
    return (ret > this.minSize ? ret : this.minSize);
  }

  // 设置FlowItem的宽/高数组
  setItemSizeArray() {
    for (let i = 0; i < 100; i++) {
      this.itemWidthArray.push(this.getSize());
      this.itemHeightArray.push(this.getSize());
    }
  }

  // 组件生命周期：在组件即将出现时初始化尺寸数组
  aboutToAppear() {
    this.setItemSizeArray();
  }

  @Builder
  itemFoot() {
    Column() {
      Text(`到底啦...`)
        .fontSize(10)
        .backgroundColor(Color.Red)
        .width(50)
        .height(50)
        .align(Alignment.Center)
        .margin({ top: 2 })
    }
  }

  build() {
    Column({ space: 2 }) {
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
        }).margin(5)
      // 将获取到的内容尺寸信息通过文本进行呈现
      Text('Width:' + this.contentWidth)
        .fontColor(Color.Red)
        .height(30)
      Text('Height:' + this.contentHeight)
        .fontColor(Color.Red)
        .height(30)

      WaterFlow({ scroller: this.scroller, footer: this.itemFoot() }) {
        LazyForEach(this.dataSource, (item: number) => {
          FlowItem() {
            Column() {
              Text('N' + item).fontSize(12).height('16')
            }
          }
          .width('100%')
          .height(this.itemHeightArray[item % 100])
          .backgroundColor(this.colors[item % this.colors.length])
        }, (item: string) => item)
      }
      .columnsTemplate('1fr 1fr') // 设置2列等宽布局
      .columnsGap(10)
      .rowsGap(5)
      .backgroundColor(0xFAEEE0)
      .width('100%')
      .height('80%')
    }
  }
}
```

#### 示例11（设置滚动事件）

该示例通过FrameNode中的[getEvent('WaterFlow')](../components/FrameNode.md#ZH-CN_TOPIC_0000002529284787__geteventwaterflow19)获取[UIWaterFlowEvent](#ZH-CN_TOPIC_0000002497604876__uiwaterflowevent19)，并为WaterFlow设置滚动事件回调，用于事件监听方因无法直接修改页面代码而无法使用声明式接口设置回调的场景。

从API version 19开始，新增UIWaterFlowEvent接口。

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
    // 获取WaterFlow事件
    let waterFlowEvent: UIWaterFlowEvent | undefined = typeNode.getEvent(frameNode, 'WaterFlow');

    // 设置OnWillScroll事件
    waterFlowEvent?.setOnWillScroll((scrollOffset: number, scrollState: ScrollState, scrollSource: ScrollSource) => {
      console.info('onWillScroll scrollOffset = ${scrollOffset}, scrollState = ${scrollState}, scrollSource = ${scrollSource}');
    });

    // 设置OnDidScroll事件
    waterFlowEvent?.setOnDidScroll((scrollOffset: number, scrollState: ScrollState) => {
      console.info('onDidScroll scrollOffset = ${scrollOffset}, scrollState = ${scrollState}');
    });

    // 设置OnReachStart事件
    waterFlowEvent?.setOnReachStart(() => {
      console.info('onReachStart');
    });

    // 设置OnReachEnd事件
    waterFlowEvent?.setOnReachEnd(() => {
      console.info('onReachEnd');
    });

    // 设置OnScrollStart事件
    waterFlowEvent?.setOnScrollStart(() => {
      console.info('onScrollStart');
    });

    // 设置OnScrollStop事件
    waterFlowEvent?.setOnScrollStop(() => {
      console.info('onScrollStop');
    });

    // 设置OnScrollFrameBegin事件
    waterFlowEvent?.setOnScrollFrameBegin((offset: number, state: ScrollState) => {
      console.info('onScrollFrameBegin offset = ${offset}, state = ${state}');
      return undefined;
    });

    // 设置OnScrollIndex事件
    waterFlowEvent?.setOnScrollIndex((first: number, last: number) => {
      console.info('onScrollIndex start = ${first}, end = ${last}');
    });
  }
}

@Entry
@Component
struct Index {
  @State index: number = 0;
  private myNodeController: MyNodeController = new MyNodeController();
  @State numbers: string[] = [];
  @State heights: number[] = [];

  aboutToAppear() {
    for (let i = 0; i < 30; i++) {
      this.numbers.push('${i+1}');
      this.heights.push(70 + Math.floor(Math.random() * 60));
    }
  }

  build() {
    Column() {
      Button('add CommonEvent to WaterFlow')
        .onClick(() => {
          this.myNodeController!.addCommonEvent(this.myNodeController!.rootNode!.getParent()!.getPreviousSibling()!)
        })
      WaterFlow() {
        ForEach(this.numbers, (day: string, index: number) => {
          FlowItem() {
            Text(day)
              .fontSize(16)
              .backgroundColor(0xF9CF93)
              .width('100%')
              .height(this.heights[index])
              .textAlign(TextAlign.Center)
          }
          .width('100%')
        }, (day: string, index: number) => index.toString() + day)
      }
      .columnsTemplate('1fr 1fr')
      .columnsGap(10)
      .rowsGap(10)
      .enableScrollInteraction(true)
      .width('90%')
      .backgroundColor(0xFAEEE0)
      .height(300)
      NodeContainer(this.myNodeController)
    }.width('100%')
  }
}
```
