# [Grid](Grid.md)

网格容器，由“行”和“列”分割的单元格所组成，通过指定“项目”所在的单元格做出各种各样的布局。

该组件从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

组件内部已绑定手势实现跟手滚动等功能，需要增加自定义手势操作时请参考[手势拦截增强](手势拦截增强.md)进行处理。

#### 子组件

仅支持[GridItem](GridItem.md)子组件和自定义组件。自定义组件在Grid下使用时，建议使用GridItem作为自定义组件的顶层组件，不建议给自定义组件设置属性和事件方法。

支持通过渲染控制类型（[if/else](../../guides/if-else：条件渲染.md)、[ForEach](ForEach.md)、[LazyForEach](LazyForEach.md)和[Repeat](Repeat.md)）动态生成子组件，更推荐使用LazyForEach或Repeat以优化性能。

[Grid](Grid.md)子组件的索引值计算规则：

按子组件的顺序依次递增。

if/else语句中，只有条件成立分支内的子组件会参与索引值计算，条件不成立分支内的子组件不计算索引值。

ForEach/LazyForEach和Repeat语句中，会计算展开所有子组件索引值。

[if/else](../../guides/if-else：条件渲染.md)、[ForEach](ForEach.md)、[LazyForEach](LazyForEach.md)和[Repeat](Repeat.md)发生变化以后，会更新子组件索引值。

[Grid](Grid.md)子组件的visibility属性设置为Hidden或None时依然会计算索引值。

[Grid](Grid.md)子组件的visibility属性设置为None时不显示，但依然会占用子组件对应的网格。

[Grid](Grid.md)子组件设置position属性，会占用子组件对应的网格，子组件将显示在相对Grid左上角偏移position的位置。该子组件不会随其对应网格滚动，在对应网格滑出Grid显示范围外后不显示。

当Grid子组件之间留有空隙时，会根据当前的展示区域尽可能填补空隙，因此[GridItem](GridItem.md)可能会随着网格滚动而改变相对位置。

从API version 21开始，[Grid](Grid.md)单个子组件的宽高最大为16777216px；API version 20及之前，Grid单个子组件的宽高最大为1000000px。子组件超出该大小可能导致滚动或显示异常。

#### 接口

Grid(scroller?: [Scroller](Scroll.md#ZH-CN_TOPIC_0000002497444896__scroller), layoutOptions?: GridLayoutOptions)

创建网格容器。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scroller | [Scroller]([Scroll](Scroll.md).md#ZH-CN_TOPIC_0000002497444896__scroller) | 否 | 可滚动组件的控制器。用于与可滚动组件进行绑定。 说明： 不允许和其他滚动类组件，如：[ArcList](Arc[List](list.md).md)、List、[Grid](Grid.md)、Scroll和[WaterFlow](WaterFlow.md)绑定同一个滚动控制对象。 |
| layoutOptions10+ | [Grid](Grid.md)LayoutOptions | 否 | Grid布局选项。 |

#### [Grid](Grid.md)LayoutOptions10+对象说明

Grid布局选项。其中，irregularIndexes和onGetIrregularSizeByIndex可对仅设置rowsTemplate或columnsTemplate的Grid使用，可以指定一个index数组，并为其中的index对应的GridItem设置其占据的行数与列数，使用方法参见[示例3](#ZH-CN_TOPIC_0000002553200787__示例3可滚动grid设置跨行跨列节点)；onGetRectByIndex可对同时设置rowsTemplate和columnsTemplate的Grid使用，为指定的index对应的GridItem设置位置和大小，使用方法参见[示例1](#ZH-CN_TOPIC_0000002553200787__示例1固定行列grid)。

为提高Grid在跳转、列数变化等场景的性能，应该尽量使用GridLayoutOptions。即使Grid中没有任何特殊的跨行跨列节点，也可以通过使用'Grid(this.scroller, {regularSize: [1, 1]})'的方式提高跳转性能。参考[优化Grid组件加载慢丢帧问题](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-improve_grid_performance)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| regularSize | [number, number] | 否 | 否 | 大小规则的[GridItem](GridItem.md)在Grid中占的行数和列数，只支持占1行1列即[1, 1]。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| irregularIndexes | number[] | 否 | 是 | 指定索引的[GridItem](GridItem.md)在Grid中的大小是不规则的。当不设置onGetIrregularSizeByIndex时，irregularIndexes中GridItem的默认大小为垂直滚动Grid的一整行或水平滚动Grid的一整列。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| onGetIrregularSizeByIndex | (index: number) => [number, number] | 否 | 是 | 配合irregularIndexes使用，设置不规则[GridItem](GridItem.md)占用的行数和列数。开发者可为irregularIndexes中指明的index对应的GridItem设置占用的行数和列数。在API version 12之前，垂直滚动Grid不支持GridItem占多行，水平滚动Grid不支持GridItem占多列。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| onGetRectByIndex11+ | (index: number) => [number, number,number,number] | 否 | 是 | 设置指定索引index对应的[GridItem](GridItem.md)的位置及大小[rowStart,columnStart,rowSpan,columnSpan]。 其中rowStart为行起始位置，columnStart为列起始位置，无单位。 rowSpan为GridItem占用的行数，columnSpan为GridItem占用的列数，无单位。 rowStart和columnStart取大于等于0的自然数，若取负数时，rowStart和columnStart默认为0。 rowSpan和columnSpan取大于等于1的自然数，若取小数则向下取整，若小于1则按1计算。 说明： 第一种情况：某个GridItem发现给它指定的起始位置被占据了，则从起始位置[0,0]开始按顺序从左到右，从上到下寻找起始的放置位置。 第二种情况：如果起始位置没有被占据，但其他位置被占据了，无法显示全部的GridItem大小，则只会布局一部分。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |

#### 属性

除支持[通用属性]([通用属性](../misc/通用属性.md).md)和[滚动组件通用属性](滚动组件通用接口.md#ZH-CN_TOPIC_0000002522240828__属性)外，还支持以下属性：


Grid组件使用通用属性[clip12+](形状裁剪.md#ZH-CN_TOPIC_0000002522240784__clip12)和通用属性[clip18+](形状裁剪.md#ZH-CN_TOPIC_0000002522240784__clip18)时默认值都为true。

设置Grid的padding后，如果子组件部分位于Grid内容区且部分位于padding区域内，则会显示；如果子组件完全位于padding区域内，则不会显示。如下图所示，[GridItem](GridItem.md)1显示，而GridItem2不显示。

#### columnsTemplate

columnsTemplate(value: string)

设置当前网格布局列的数量、固定列宽或最小列宽值，不设置时默认1列。

例如， '1fr 1fr 2fr' 是将父组件分3列，将父组件允许的宽分为4等份，第1列占1份，第2列占1份，第3列占2份。

columnsTemplate('repeat(auto-fit, track-size)')是设置最小列宽值为track-size，自动计算列数和实际列宽。

columnsTemplate('repeat(auto-fill, track-size)')是设置固定列宽值为track-size，自动计算列数。

columnsTemplate('repeat(auto-stretch, track-size)')是设置固定列宽值为track-size，使用columnsGap作为最小列间距，自动计算列数和实际列间距。

其中repeat、auto-fit、auto-fill、auto-stretch为关键字。track-size为列宽，支持的单位包括px、vp、%或有效数字，默认单位为vp，track-size至少包括一个有效列宽。

auto-fit模式和auto-stretch模式只支持track-size为一个有效列宽值，并且auto-stretch模式中的track-size只支持px、vp和有效数字，不支持%。auto-fill模式支持一个或多个有效列宽，如columnsTemplate('repeat(auto-fill, 20)')、columnsTemplate('repeat(auto-fill, 20 80px)')。

使用效果可以参考[示例8](#ZH-CN_TOPIC_0000002553200787__示例8设置自适应列数)。

设置为'0fr'时，该列的列宽为0，不显示[GridItem](GridItem.md)。设置为其他非法值时，GridItem显示为固定1列。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string | 是 | 当前网格布局列的数量或最小列宽值。 |

#### columnsTemplate22+

columnsTemplate(value: string | [ItemFillPolicy](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__itemfillpolicy22))

设置当前网格组件布局列的数量，不设置时默认1列。

当value设置为string类型时，使用方法参考[columnsTemplate(value: string)](#ZH-CN_TOPIC_0000002553200787__columnstemplate)。

当value设置为ItemFillPolicy类型时，将根据Grid组件宽度对应[断点类型](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-grid-layout#栅格容器断点)确定列数。

例如，[ItemFillPolicy](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__itemfillpolicy22).BREAKPOINT_DEFAULT在组件宽度属于sm及更小的断点区间时显示2列，属于md断点区间时显示3列，属于lg及更大的断点区间时显示5列，且每列均为1fr。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string | [ItemFillPolicy](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__itemfillpolicy22) | 是 | 当前网格组件布局列的数量。 |

#### rowsTemplate

rowsTemplate(value: string)

设置当前网格布局行的数量、固定行高或最小行高值，不设置时默认1行。

例如， '1fr 1fr 2fr'是将父组件分3行，将父组件允许的高分为4等份，第1行占1份，第2行占1份，第3行占2份。

rowsTemplate('repeat(auto-fit, track-size)')是设置最小行高值为track-size，自动计算行数和实际行高。

rowsTemplate('repeat(auto-fill, track-size)')是设置固定行高值为track-size，自动计算行数。

rowsTemplate('repeat(auto-stretch, track-size)')是设置固定行高值为track-size，使用rowsGap为最小行间距，自动计算行数和实际行间距。

其中repeat、auto-fit、auto-fill、auto-stretch为关键字。track-size为行高，支持的单位包括px、vp、%或有效数字，默认单位为vp，track-size至少包括一个有效行高。

auto-fit模式和auto-stretch模式只支持track-size为一个有效行高值，并且auto-stretch模式中的track-size只支持px、vp和有效数字，不支持%。auto-fill模式支持一个或多个有效行高，如rowsTemplate('repeat(auto-fill, 20)')、rowsTemplate('repeat(auto-fill, 20 80px)')。

设置为'0fr'，则这一行的行高为0，这一行[GridItem](GridItem.md)不显示。设置为其他非法值，按固定1行处理。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string | 是 | 当前网格布局行的数量或最小行高值。 |


[Grid](Grid.md)组件根据rowsTemplate、columnsTemplate属性的设置情况，可分为以下三种布局模式：

1、rowsTemplate、columnsTemplate同时设置：

- [Grid](Grid.md)只展示固定行列数的元素，其余元素不展示，且Grid不可滚动。
- 此模式下以下属性不生效：layoutDirection、maxCount、minCount、cell[Length](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__length)。
- [Grid](Grid.md)的宽高没有设置时，默认适应父组件尺寸。
- [Grid](Grid.md)网格列大小按照Grid自身内容区域大小减去所有行列Gap后按各个行列所占比重分配。
- [GridItem](GridItem.md)默认填满网格大小。

2、rowsTemplate、columnsTemplate仅设置其中的一个：

- 元素按照设置的方向进行排布，超出[Grid](Grid.md)显示区域后，Grid可通过滚动的方式展示。
- 如果设置了columnsTemplate，[Grid](Grid.md)滚动方向为垂直方向，主轴方向为垂直方向，交叉轴方向为水平方向。
- 如果设置了rowsTemplate，[Grid](Grid.md)滚动方向为水平方向，主轴方向为水平方向，交叉轴方向为垂直方向。
- 此模式下以下属性不生效：layoutDirection、maxCount、minCount、cell[Length](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__length)。
- 网格交叉轴方向尺寸根据[Grid](Grid.md)自身内容区域交叉轴尺寸减去交叉轴方向所有Gap后按所占比重分配。
- 网格主轴方向尺寸取当前网格交叉轴方向所有[GridItem](GridItem.md)主轴方向尺寸最大值。

- 此模式下GridItem交叉轴方向尺寸与网格一致，可以通过设置[constraintSize](尺寸设置.md#ZH-CN_TOPIC_0000002553360703__constraintsize)中的maxWidth或maxHeight限制GridItem交叉轴方向尺寸小于网格。

3、rowsTemplate、columnsTemplate都不设置：

- 元素在layoutDirection方向上排布，列数由[Grid](Grid.md)的宽度、首个元素的宽度、minCount、maxCount、columnsGap共同决定。
- 行数由[Grid](Grid.md)高度、首个元素高度、cellLength、rowsGap共同决定。超出行列容纳范围的元素不显示，也不能通过滚动进行展示。
- 此模式下仅生效以下属性：layoutDirection、maxCount、minCount、cell[Length](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__length)、editMode、columnsGap、rowsGap。
- 当前layoutDirection设置为Row时，先从左到右排列，排满一行再排下一行。剩余高度不足时不再布局，整体内容顶部居中。
- 当前layoutDirection设置为Column时，先从上到下排列，排满一列再排下一列，剩余宽度不足时不再布局。整体内容顶部居中。
- 当前Grid下面没有[GridItem](GridItem.md)时，Grid的宽高为0。

#### columnsGap

columnsGap(value: [Length](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__length))

设置列与列的间距。设置为小于0的值时，按默认值显示。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Length](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__length) | 是 | 列与列的间距。 默认值：0 取值范围：[0, +∞) |

#### rowsGap

rowsGap(value: [Length](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__length))

设置行与行的间距。设置为小于0的值时，按默认值显示。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Length](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__length) | 是 | 行与行的间距。 默认值：0 取值范围：[0, +∞) |

#### scrollBar

scrollBar(value: [BarState](枚举说明.md#ZH-CN_TOPIC_0000002529284967__barstate))

设置滚动条状态。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [BarState](枚举说明.md#ZH-CN_TOPIC_0000002529284967__barstate) | 是 | 滚动条状态。 默认值：BarState.Auto 说明： API version 9及以下版本默认值为BarState.Off，API version 10及以上版本的默认值为BarState.Auto。 |

#### scrollBar[Color](枚举说明.md#ZH-CN_TOPIC_0000002529284967__color)

scrollBar[Color](枚举说明.md#ZH-CN_TOPIC_0000002529284967__color)(value: Color | number | string)

设置滚动条的颜色。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Color](枚举说明.md#ZH-CN_TOPIC_0000002529284967__color) | number | string | 是 | 滚动条的颜色。 默认值：'#182431'（40%不透明度） number为HEX格式颜色，支持rgb或者argb，示例：0xffffff。 string为rgb或者argb格式颜色，示例：'#ffffff'。 |

#### scrollBar[Color](枚举说明.md#ZH-CN_TOPIC_0000002529284967__color)22+

scrollBar[Color](枚举说明.md#ZH-CN_TOPIC_0000002529284967__color)(color: Color | number | string | Resource)

设置滚动条的颜色。与[scrollBarColor](#ZH-CN_TOPIC_0000002553200787__scrollbarcolor)相比， 参数名改为color，并开始支持Resource类型。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| color | [Color](枚举说明.md#ZH-CN_TOPIC_0000002529284967__color) | number | string | [Resource](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resource) | 是 | 滚动条的颜色。 默认值：'#182431'（40%不透明度） number为HEX格式颜色，支持rgb或者argb，示例：0xffffff。string为rgb或者argb格式颜色，示例：'#ffffff'。 |

#### scrollBarWidth

scrollBarWidth(value: number | string)

设置滚动条的宽度，不支持百分比设置。宽度设置后，滚动条正常状态和按压状态宽度均为滚动条的宽度值。如果滚动条的宽度超过[Grid](Grid.md)组件主轴方向的高度，则滚动条的宽度会变为默认值。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | string | 是 | 滚动条的宽度。 默认值：4 单位：vp 取值范围：设置为小于0的值时，按默认值处理。设置为0时，不显示滚动条。 |

#### cachedCount

cachedCount(value: number)

设置预加载的GridItem的数量，只在[LazyForEach](LazyForEach.md)和开启了[virtualScroll](Repeat.md#ZH-CN_TOPIC_0000002553360847__virtualscroll)开关的[Repeat](Repeat.md)中生效。

设置缓存后会在Grid显示区域上下各缓存cachedCount*列数个[GridItem](GridItem.md)。

[LazyForEach](LazyForEach.md)和开启了[virtualScroll](Repeat.md#ZH-CN_TOPIC_0000002553360847__virtualscroll)开关的[Repeat](Repeat.md)超出显示和缓存范围的GridItem会被释放。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 预加载的[GridItem](GridItem.md)的数量。 默认值：垂直滚动时为一个屏幕内可显示的行数，水平滚动时为一个屏幕内可显示的列数，最大值为16。 取值范围：[0, +∞)，设置为小于0的值时，按1处理。 通过状态变量单独更新value值时，Grid组件不会触发布局更新，缓存节点数量仅会在下次布局时更新。 |

#### cachedCount14+

cachedCount(count: number, show: boolean)

设置预加载的[GridItem](GridItem.md)数量，并配置是否显示预加载节点。

设置缓存后会在Grid显示区域上下各缓存cachedCount*列数个GridItem。配合[裁剪](形状[裁剪](形状裁剪.md#ZH-CN_TOPIC_0000002529284827__clip12).md#ZH-CN_TOPIC_0000002522240784__clip12)或[内容裁剪](滚动组件通用接口.md#ZH-CN_TOPIC_0000002522240828__clipcontent14)属性可以显示出预加载节点。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| count | number | 是 | 预加载的[GridItem](GridItem.md)的数量。 默认值：垂直滚动时为一个屏幕内可显示的行数，水平滚动时为一个屏幕内可显示的列数，最大值为16。 取值范围：[0, +∞)，设置为小于0的值时，按1处理。 通过状态变量单独更新count值时，Grid组件不会触发布局更新，缓存节点数量仅会在下次布局时更新。 |
| show | boolean | 是 | 被预加载的[GridItem](GridItem.md)是否需要显示。设置为true时显示预加载的GridItem，设置为false时不显示预加载的GridItem。 默认值：false |

#### editMode8+

editMode(value: boolean)

设置Grid是否进入编辑模式，进入编辑模式可以拖拽Grid组件内部[GridItem](GridItem.md)。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | [Grid](Grid.md)是否进入编辑模式。设置为true时当前Grid组件处于可编辑模式，设置为false时当前Grid组件处于不可编辑模式。 默认值：false |

#### layoutDirection8+

layoutDirection(value: [Grid](Grid.md)Direction)

设置布局的主轴方向。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Grid](Grid.md)Direction | 是 | 布局的主轴方向。 默认值：GridDirection.Row |

#### maxCount8+

maxCount(value: number)

设置可显示的最大行数或列数。设置为小于1的值时，按默认值显示。

当layoutDirection是Row/RowReverse时，表示可显示的最大列数。

当layoutDirection是Column/ColumnReverse时，表示可显示的最大行数。

当maxCount小于minCount时，maxCount和minCount都按默认值处理。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 可显示的最大行数或列数。 默认值：Infinity |

#### minCount8+

minCount(value: number)

设置可显示的最小行数或列数。设置为小于1的值时，按默认值显示。

当layoutDirection是Row/RowReverse时，表示可显示的最小列数。

当layoutDirection是Column/ColumnReverse时，表示可显示的最小行数。

当minCount大于maxCount时，minCount和maxCount都按默认值处理。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 可显示的最小行数或列数。 默认值：1 |

#### cell[Length](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__length)8+

cell[Length](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__length)(value: number)

设置一行的高度或者一列的宽度。

当layoutDirection是Row/RowReverse时，表示一行的高度。

当layoutDirection是Column/ColumnReverse时，表示一列的宽度。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 一行的高度或者一列的宽度。 默认值：第一个元素的大小 单位：vp 取值范围：(0, +∞)，设置为小于等于0的值时，按默认值显示。 |

#### multiSelectable8+

multiSelectable(value: boolean)

设置是否开启鼠标框选。开启框选后，可以配合GridItem的selected属性和onSelect事件获取GridItem的选中状态，还可以通过[多态样式](多态样式.md)设置GridItem的[选中态样式](多态样式.md)（GridItem默认无选中态样式）。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 是否开启鼠标框选。 默认值：false false：关闭框选。true：开启框选。 |

#### supportAnimation8+

supportAnimation(value: boolean)

设置是否支持动画。当前支持[GridItem](GridItem.md)拖拽动画。仅在滚动模式下（只设置rowsTemplate、columnsTemplate其中一个）支持动画。

仅在大小规则的[Grid](Grid.md)中支持拖拽动画，跨行或跨列场景不支持。

supportAnimation动画效果参考[示例5（Grid拖拽场景）](#ZH-CN_TOPIC_0000002553200787__示例5grid拖拽场景)，其他动画效果需要应用自定义拖拽实现。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 是否支持动画。设置为true时支持[GridItem](GridItem.md)拖拽动画，设置为false时不支持GridItem拖拽动画。 默认值：false |

#### edgeEffect10+

edgeEffect(value: [EdgeEffect](枚举说明.md#ZH-CN_TOPIC_0000002529284967__edgeeffect), options?: EdgeEffectOptions)

设置边缘滑动效果。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [EdgeEffect](枚举说明.md#ZH-CN_TOPIC_0000002529284967__edgeeffect) | 是 | Grid组件的边缘滑动效果，支持弹簧效果和阴影效果。 默认值：EdgeEffect.None |
| options11+ | [EdgeEffectOptions](滚动组件通用接口.md#ZH-CN_TOPIC_0000002529284871__edgeeffectoptions11对象说明) | 否 | 组件内容大小小于组件自身时，是否开启滑动效果。设置为{ alwaysEnabled: true }会开启滑动效果，{ alwaysEnabled: false }不开启。 默认值：{ alwaysEnabled: false } |

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

设置嵌套滚动选项。设置前后两个方向的嵌套滚动模式，实现与父组件的滚动联动。当组件内容大小小于组件自身，且[edgeEffect](#ZH-CN_TOPIC_0000002553200787__edgeeffect10)的options为{ alwaysEnabled: false }时，组件自身滑动手势不会触发，嵌套滚动属性不会生效，如果其父滚动组件有滑动手势，则会触发父组件的滑动手势。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [NestedScrollOptions](滚动组件通用接口.md#ZH-CN_TOPIC_0000002529284871__nestedscrolloptions10对象说明) | 是 | 嵌套滚动选项。 |

#### friction10+

friction(value: number | [Resource](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resource))

设置摩擦系数，手动划动滚动区域时生效，仅影响惯性滚动过程，对惯性滚动过程中的链式效果有间接影响。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | [Resource](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resource) | 是 | 摩擦系数。 默认值：非可穿戴设备为0.6，可穿戴设备为0.9。 从API version 11开始，非可穿戴设备默认值为0.7。 从API version 12开始，非可穿戴设备默认值为0.75。 取值范围：(0, +∞)，设置为小于等于0的值时，按默认值处理。 |

#### alignItems12+

alignItems(alignment: [Optional](自定义属性设置.md#ZH-CN_TOPIC_0000002529284845__optionalt12)<GridItemAlignment>)

设置Grid中GridItem的对齐方式， 使用方法可以参考[示例9](#ZH-CN_TOPIC_0000002553200787__示例9以当前行最高的griditem的高度为其他griditem的高度)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| alignment | [Optional](自定义属性设置.md#ZH-CN_TOPIC_0000002529284845__optionalt12)<GridItemAlignment> | 是 | 设置Grid中GridItem的对齐方式。 默认值：GridItemAlignment.DEFAULT |

#### focusWrapMode20+

focusWrapMode(mode: [Optional](自定义属性设置.md#ZH-CN_TOPIC_0000002529284845__optionalt12)<FocusWrapMode>)

设置交叉轴方向键走焦模式。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [Optional](自定义属性设置.md#ZH-CN_TOPIC_0000002529284845__optionalt12)<[FocusWrapMode](枚举说明.md#ZH-CN_TOPIC_0000002529284967__focuswrapmode20)> | 是 | 交叉轴方向键走焦模式。 默认值：FocusWrapMode.DEFAULT 说明： 异常值按默认值处理，即交叉轴方向键不能换行。 |

#### syncLoad20+

syncLoad(enable: boolean)

设置是否同步加载[Grid](Grid.md)区域内所有子组件。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | boolean | 是 | 是否同步加载[Grid](Grid.md)区域内所有子组件。 true表示同步加载，false表示异步加载。默认值：true。 说明： 设置为false时，在首次显示、不带动画[scrollToIndex](Scroll.md#ZH-CN_TOPIC_0000002497444896__scrolltoindex)跳转场景，若当帧布局耗时超过50ms，会将Grid区域内尚未布局的子组件延后到下一帧进行布局。 |

**supportEmptyBranchInLazyLoading23+**

supportEmptyBranchInLazyLoading(supported: boolean | undefined)

设置当前[Grid](Grid.md)组件是否支持在LazyForEach或Repeat中使用if/else渲染控制语法生成不包含任何子组件的空分支节点。未设置时不支持空分支节点。此属性初次赋值后不支持更新，所以赋值后无法在支持空分支、不支持空分支行为之间切换。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从API version 23开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| supported | boolean | undefined | 是 | 当前[Grid](Grid.md)组件是否支持在LazyForEach或Repeat中使用if/else渲染控制语法生成一个不含任何子节点的空分支节点。 true表示支持空分支节点；false表示不支持空分支节点。 值为undefined时，按false处理。 |

**editModeOptions23+**

editModeOptions(options?: EditModeOptions)

配置编辑模式选项参数。

元服务API： 从API version 23开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | EditModeOptions | 否 | 编辑模式选项。 |

#### [GridItem](GridItem.md)Alignment12+枚举说明

[GridItem](GridItem.md)的对齐方式枚举。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DEFAULT | 0 | 使用[Grid](Grid.md)的默认对齐方式。 |
| STRETCH | 1 | 以一行中的最高的[GridItem](GridItem.md)作为其他GridItem的高度。 |


1、只有可滚动的[Grid](Grid.md)中，设置STRETCH参数会生效，其他场景不生效。

2、在Grid的一行中，如果每个[GridItem](GridItem.md)都是大小规律的（只占一行一列），设置STRETCH参数会生效，存在跨行或跨列的GridItem的场景不生效。

3、设置STRETCH后，只有不设置高度的[GridItem](GridItem.md)才会以当前行中最高的GridItem作为自己的高度，设置过高度的GridItem高度不会变化。

4、设置STRETCH后，[Grid](Grid.md)布局时会有额外的布局流程，可能会带来额外的性能开销。

#### [Grid](Grid.md)Direction8+枚举说明

主轴布局方向枚举。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| Row | 0 | 主轴布局方向沿水平方向布局，即自左往右先填满一行，再去填下一行。 |
| Column | 1 | 主轴布局方向沿垂直方向布局，即自上往下先填满一列，再去填下一列。 |
| RowReverse | 2 | 主轴布局方向沿水平方向反向布局，即自右往左先填满一行，再去填下一行。 |
| ColumnReverse | 3 | 主轴布局方向沿垂直方向反向布局，即自下往上先填满一列，再去填下一列。 |

#### 事件

除支持[通用事件]([通用事件](../misc/通用事件.md).md)和[滚动组件通用事件](滚动组件通用接口.md#ZH-CN_TOPIC_0000002522240828__事件)外，还支持以下事件：

#### on[Scroll](Scroll.md)Index

on[Scroll](Scroll.md)Index(event: (first: number, last: number) => void)

当前网格显示的起始位置/终止位置的item发生变化时触发。网格初始化时会触发一次。[Grid](Grid.md)显示区域上第一个子组件/最后一个组件的索引值有变化就会触发。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| first | number | 是 | 当前显示的网格起始位置的索引值。 |
| last10+ | number | 是 | 当前显示的网格终止位置的索引值。 |

#### onItemDragStart8+

onItemDragStart(event: OnItemDragStartCallback)

开始拖拽网格元素时触发。

手指长按[GridItem](GridItem.md)时触发该事件。

由于拖拽检测也需要长按，且事件处理机制优先触发子组件事件，GridItem上绑定[LongPressGesture]([LongPressGesture](LongPressGesture.md#ZH-CN_TOPIC_0000002529444825__longpressgesture-1).md#ZH-CN_TOPIC_0000002553200773__longpressgesture-1)时无法触发拖拽。如有长按和拖拽同时使用的需求可以使用通用拖拽事件。

拖拽浮起的网格元素可在应用窗口内移动，若需限制移动范围，可通过自定义手势实现，具体参考[示例16（实现GridItem自定义拖拽）](#ZH-CN_TOPIC_0000002553200787__示例16实现griditem自定义拖拽)。

不支持拖动到Grid边缘时自动滚动，可使用通用拖拽实现，具体参考[示例17（通过拖拽事件实现griditem拖拽）](#ZH-CN_TOPIC_0000002553200787__示例17通过拖拽事件实现griditem拖拽)。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | OnItemDragStartCallback | 是 | 网格元素拖拽开始时触发的回调。 API version 22及之前版本，该参数类型为(event: [ItemDragInfo](滚动组件通用接口.md#ZH-CN_TOPIC_0000002529284871__itemdraginfo对象说明), itemIndex: number) => (() => any) | void，其中event和itemIndex参数含义参考OnItemDragStartCallback。 |

#### onItemDragEnter8+

onItemDragEnter(event: (event: [ItemDragInfo](滚动组件通用接口.md#ZH-CN_TOPIC_0000002529284871__itemdraginfo对象说明)) => void)

拖拽进入网格元素范围内时触发。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [ItemDragInfo](滚动组件通用接口.md#ZH-CN_TOPIC_0000002529284871__itemdraginfo对象说明) | 是 | 拖拽点的信息。 |

#### onItemDragMove8+

onItemDragMove(event: (event: [ItemDragInfo](滚动组件通用接口.md#ZH-CN_TOPIC_0000002529284871__itemdraginfo对象说明), itemIndex: number, insertIndex: number) => void)

拖拽在网格元素范围内移动时触发。

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

拖拽离开网格元素时触发。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [ItemDragInfo](滚动组件通用接口.md#ZH-CN_TOPIC_0000002529284871__itemdraginfo对象说明) | 是 | 拖拽点的信息。 |
| itemIndex | number | 是 | 拖拽离开的网格元素索引值。 |

#### onItemDrop8+

onItemDrop(event: (event: [ItemDragInfo](滚动组件通用接口.md#ZH-CN_TOPIC_0000002529284871__itemdraginfo对象说明), itemIndex: number, insertIndex: number, isSuccess: boolean) => void)

绑定该事件的网格元素可作为拖拽释放目标，当[GridItem](GridItem.md)停止拖拽时触发。

当拖拽释放位置在网格元素之内时，isSuccess会返回true；在网格元素之外时，isSuccess会返回false。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [ItemDragInfo](滚动组件通用接口.md#ZH-CN_TOPIC_0000002529284871__itemdraginfo对象说明) | 是 | 拖拽点的信息。 |
| itemIndex | number | 是 | 拖拽起始位置。 |
| insertIndex | number | 是 | 拖拽插入位置。 |
| isSuccess | boolean | 是 | 拖拽释放位置是否在设置了onItemDrop的网格元素之内。 true：表示拖拽释放位置在设置了onItemDrop的网格元素之内；false：表示拖拽释放位置在设置了onItemDrop的网格元素之外。 |

#### on[Scroll](Scroll.md)BarUpdate10+

on[Scroll](Scroll.md)BarUpdate(event: (index: number, offset: number) => ComputedBarAttribute)

在[Grid](Grid.md)每帧布局结束时触发，可通过该回调设置滚动条的位置及长度。

该接口只用作设置[Grid](Grid.md)的滚动条位置，不建议开发者在此接口中做业务逻辑处理。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 当前显示的网格起始位置的索引值。 |
| offset | number | 是 | 当前显示的网格起始位置元素相对网格显示起始位置的偏移，单位vp。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ComputedBarAttribute | 滚动条的位置及长度。 |

#### onReachStart10+

onReachStart(event: () => void)

网格到达起始位置时触发。

[Grid](Grid.md)初始化时会触发一次，Grid滚动到起始位置时触发一次。Grid边缘效果为弹簧效果时，划动经过起始位置时触发一次，回弹回起始位置时再触发一次。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | () => void | 是 | 网格到达起始位置时触发的回调。 |

#### onReachEnd10+

onReachEnd(event: () => void)

网格到达末尾位置时触发。不满一屏并且最后一个子组件末端在[Grid](Grid.md)内时触发。

[Grid](Grid.md)边缘效果为弹簧效果时，划动经过末尾位置时触发一次，回弹回末尾位置时再触发一次。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | () => void | 是 | 网格到达末尾位置时触发的回调。 |

#### on[Scroll](Scroll.md)FrameBegin10+

onScrollFrameBegin(event: [OnScrollFrameBeginCallback](Scroll.md#ZH-CN_TOPIC_0000002497444896__onscrollframebegincallback18))

该接口回调时，事件参数传入即将发生的滑动量，事件处理函数中可根据应用场景计算实际需要的滑动量并作为事件处理函数的返回值返回，网格将按照返回值的实际滑动量进行滑动。

满足以下任一条件时触发该事件：

1. 用户交互（如手指滑动、键鼠操作等）触发滚动。
1. [Grid](Grid.md)惯性滚动。

1. 调用[fling](Scroll.md#ZH-CN_TOPIC_0000002553360749__[fling](Scroll.md#ZH-CN_TOPIC_0000002497444896__fling12)12)接口触发滚动。

不触发该事件的条件：

1. 调用除[fling](Scroll.md#ZH-CN_TOPIC_0000002553360749__[fling](Scroll.md#ZH-CN_TOPIC_0000002497444896__fling12)12)接口外的其他滚动控制接口。

1. 越界回弹。
1. 拖动滚动条。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [OnScrollFrameBeginCallback](Scroll.md#ZH-CN_TOPIC_0000002497444896__onscrollframebegincallback18) | 是 | 每帧滚动开始回调函数。 |

#### on[Scroll](Scroll.md)Start10+

on[Scroll](Scroll.md)Start(event: () => void)

网格滑动开始时触发。手指拖动网格或网格的滚动条触发的滑动开始时，会触发该事件。使用[Scroller](Scroll.md#ZH-CN_TOPIC_0000002553360749__scroller)滑动控制器触发的带动画的滑动，动画开始时会触发该事件。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | () => void | 是 | 网格滑动开始时触发的回调。 |

#### on[Scroll](Scroll.md)Stop10+

on[Scroll](Scroll.md)Stop(event: () => void)

网格滑动停止时触发。手指拖动网格或网格的滚动条触发的滑动，手指离开屏幕后滑动停止时会触发该事件。使用[Scroller](Scroll.md#ZH-CN_TOPIC_0000002553360749__scroller)滑动控制器触发的带动画的滑动，动画停止会触发该事件。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | () => void | 是 | 网格滑动停止时触发的回调。 |

#### on[Scroll](Scroll.md)(deprecated)

onScroll(event: (scrollOffset: number, scrollState: [ScrollState](List.md#ZH-CN_TOPIC_0000002522240820__scrollstate枚举说明)) => void)

网格滑动时触发。


从API version 10开始支持，从API version 12开始废弃，建议使用[onDidScroll](滚动组件通用接口.md#ZH-CN_TOPIC_0000002522240828__ondidscroll12)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scrollOffset | number | 是 | 相对于上一帧的偏移量，[Grid](Grid.md)的内容向上滚动时偏移量为正，向下滚动时偏移量为负。 单位vp。 |
| scrollState | [ScrollState](list.md#ZH-CN_TOPIC_0000002529284863__scrollstate枚举说明) | 是 | 当前滑动状态。 |

#### ComputedBarAttribute10+对象说明

滚动条位置和长度对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| totalOffset | number | 否 | 否 | [Grid](Grid.md)内容相对显示区域的总偏移，单位px。 |
| totalLength | number | 否 | 否 | [Grid](Grid.md)内容总长度，单位px。 |

#### UI[Grid](Grid.md)Event19+

frameNode中[getEvent('Grid')](FrameNode.md#ZH-CN_TOPIC_0000002522240744__geteventgrid19)方法的返回值，可用于给Grid节点设置滚动事件。

UIGridEvent继承于[UIScrollableCommonEvent](滚动组件通用接口.md#ZH-CN_TOPIC_0000002522240828__uiscrollablecommonevent19)。

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

setOnScrollIndex(callback: On[Grid](Grid.md)ScrollIndexCallback | undefined): void

设置[onScrollIndex](#ZH-CN_TOPIC_0000002553200787__onscrollindex)事件的回调。

方法入参为undefined时，会重置事件回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | On[Grid](Grid.md)ScrollIndexCallback | undefined | 是 | onScrollIndex事件的回调函数。 |

#### On[Grid](Grid.md)ScrollIndexCallback19+

type On[Grid](Grid.md)ScrollIndexCallback = (first: number, last: number) => void

[Grid](Grid.md)组件可见区域item变化事件的回调类型。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| first | number | 是 | 当前显示的[Grid](Grid.md)起始位置的索引值。 |
| last | number | 是 | 当前显示的[Grid](Grid.md)终止位置的索引值。 |

#### 示例

#### 示例1（固定行列[Grid](Grid.md)）

可以使用[GridLayoutOptions](#ZH-CN_TOPIC_0000002553200787__gridlayoutoptions10对象说明)中的onGetRectByIndex指定GridItem的位置和大小。

```ets
// xxx.ets
@Entry
@Component
struct GridExample {
  @State numbers1: string[] = ['0', '1', '2', '3', '4'];
  @State numbers2: string[] = ['0', '1', '2', '3', '4', '5'];
  layoutOptions3: GridLayoutOptions = {
    regularSize: [1, 1],
    onGetRectByIndex: (index: number) => {
      if (index == 0) {
        return [0, 0, 1, 1];
      } else if (index == 1) {
        return [0, 1, 2, 2];
      } else if (index == 2) {
        return [0, 3, 3, 3];
      } else if (index == 3) {
        return [3, 0, 3, 3];
      } else if (index == 4) {
        return [4, 3, 2, 2];
      } else {
        return [5, 5, 1, 1];
      }
  };

  build() {
    Column({ space: 5 }) {
      Grid() {
          ForEach(this.numbers1, (day: string) => {
            GridItem() {
              Text(day)
                .fontSize(16)
                .backgroundColor(0xF9CF93)
                .width('100%')
                .height('100%')
                .textAlign(TextAlign.Center)
            }
          }, (day: string) => day)
      }
      .columnsTemplate('1fr 1fr 1fr 1fr 1fr')
      .rowsTemplate('1fr 1fr 1fr 1fr 1fr')
      .columnsGap(10)
      .rowsGap(10)
      .width('90%')
      .backgroundColor(0xFAEEE0)
      .height(300)

      Text('GridLayoutOptions的使用：onGetRectByIndex。').fontColor(0x000000).fontSize(14).width('90%')

      Grid(undefined, this.layoutOptions3) {
        ForEach(this.numbers2, (day: string) => {
          GridItem() {
            Text(day)
              .fontSize(16)
              .backgroundColor(0xF9CF93)
              .width('100%')
              .height('100%')
              .textAlign(TextAlign.Center)
          }
          .height('100%')
          .width('100%')
        }, (day: string) => day)
      }
      .columnsTemplate('1fr 1fr 1fr 1fr 1fr 1fr')
      .rowsTemplate('1fr 1fr 1fr 1fr 1fr 1fr')
      .columnsGap(10)
      .rowsGap(10)
      .width('90%')
      .backgroundColor(0xFAEEE0)
      .height(300)
    }.width('100%').margin({ top: 5 })
  }
```

#### 示例2（可滚动[Grid](Grid.md)和滚动事件）

可滚动[Grid](Grid.md)，包括所有滚动属性和事件。

GridDataSource实现了LazyForEach数据源接口[IDataSource](LazyForEach.md#ZH-CN_TOPIC_0000002522080924__idatasource)，用于通过LazyForEach给Grid提供子组件。

```ets
// GridDataSource.ets
export class GridDataSource implements IDataSource {
  private list: string[] = [];
  private listeners: DataChangeListener[] = [];

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
    if (this.listeners.indexOf(listener) < 0) {
      this.listeners.push(listener);
    }

  unregisterDataChangeListener(listener: DataChangeListener): void {
    const pos = this.listeners.indexOf(listener);
    if (pos >= 0) {
      this.listeners.splice(pos, 1);
  }

  // 通知控制器数据位置变化
  notifyDataMove(from: number, to: number): void {
    this.listeners.forEach(listener => {
      listener.onDataMove(from, to);
    })
  }

  // 交换元素位置
  public swapItem(from: number, to: number): void {
    let temp: string = this.list[from];
    this.list[from] = this.list[to];
    this.list[to] = temp;
    this.notifyDataMove(from, to);
}
```

```ets
// xxx.ets
import { GridDataSource } from './GridDataSource';

@Entry
@Component
struct GridExample {
  numbers: GridDataSource = new GridDataSource([]);
  scroller: Scroller = new Scroller();
  @State gridPosition: number = 0; //0代表滚动到grid顶部，1代表中间值，2代表滚动到grid底部。

  aboutToAppear() {
    let list: string[] = [];
    for (let i = 0; i < 5; i++) {
      for (let j = 0; j < 5; j++) {
        list.push(j.toString());
      }
    this.numbers = new GridDataSource(list);
  }

  build() {
    Column({ space: 5 }) {
      Text('Grid').fontColor(0x000000).fontSize(16).width('90%')
      Grid(this.scroller) {
        LazyForEach(this.numbers, (day: string) => {
          GridItem() {
            Text(day)
              .fontSize(16)
              .backgroundColor(0xF9CF93)
              .width('100%')
              .height(80)
              .textAlign(TextAlign.Center)
          }
        }, (index: number) => index.toString())
      }
      .columnsTemplate('1fr 1fr 1fr 1fr 1fr')
      .columnsGap(10)
      .rowsGap(10)
      .friction(0.6)
      .enableScrollInteraction(true)
      .supportAnimation(false)
      .multiSelectable(false)
      .edgeEffect(EdgeEffect.Spring)
      .scrollBar(BarState.On)
      .scrollBarColor(Color.Grey)
      .scrollBarWidth(4)
      .width('90%')
      .backgroundColor(0xFAEEE0)
      .height(300)
      .onScrollIndex((first: number, last: number) => {
        console.info(first.toString());
        console.info(last.toString());
      })
      .onScrollBarUpdate((index: number, offset: number) => {
        console.info('XXX' + 'Grid onScrollBarUpdate,index : ' + index.toString() + ',offset' + offset.toString());
        return { totalOffset: (index / 5) * (80 + 10) - offset, totalLength: 80 * 5 + 10 * 4 };
      })  //只适用于当前示例代码数据源，如果数据源有变化，则需要修改该部分代码，或者删掉此属性
      .onDidScroll((scrollOffset: number, scrollState: ScrollState) => {
        console.info(scrollOffset.toString());
        console.info(scrollState.toString());
      })
      .onScrollStart(() => {
        console.info('XXX' + 'Grid onScrollStart');
      })
      .onScrollStop(() => {
        console.info('XXX' + 'Grid onScrollStop');
      })
      .onReachStart(() => {
        this.gridPosition = 0;
        console.info('XXX' + 'Grid onReachStart');
      })
      .onReachEnd(() => {
        this.gridPosition = 2;
        console.info('XXX' + 'Grid onReachEnd');
      })

      Button('next page')
        .onClick(() => { // 点击后滑到下一页
          this.scroller.scrollPage({ next: true });
        })
    }.width('100%').margin({ top: 5 })
  }
```

![image](public_sys-resources/zh-cn_image_0000002553364805.webp)

#### 示例3（可滚动[Grid](Grid.md)设置跨行跨列节点）

[GridLayoutOptions](#ZH-CN_TOPIC_0000002553200787__gridlayoutoptions10对象说明)的使用：irregularIndexes与onGetIrregularSizeByIndex。

GridDataSource说明及完整代码参考[示例2可滚动grid和滚动事件](#ZH-CN_TOPIC_0000002553200787__示例2可滚动grid和滚动事件)。

```ets
// xxx.ets
import { GridDataSource } from './GridDataSource';

@Entry
@Component
struct GridExample {
  numbers: GridDataSource = new GridDataSource([]);
  scroller: Scroller = new Scroller();
  layoutOptions1: GridLayoutOptions = {
    regularSize: [1, 1],        // 只支持[1, 1]
    irregularIndexes: [0, 6],   // 索引为0和6的GridItem占用一行
  };

  layoutOptions2: GridLayoutOptions = {
    regularSize: [1, 1],
    irregularIndexes: [0, 7],   // 索引为0和7的GridItem占用的列数由onGetIrregularSizeByIndex指定
    onGetIrregularSizeByIndex: (index: number) => {
      if (index === 0) {
        return [1, 5];
      }
      return [1, index % 6 + 1];
    }
  };

  aboutToAppear() {
    let list: string[] = [];
    for (let i = 0; i < 5; i++) {
      for (let j = 0; j < 5; j++) {
        list.push(j.toString());
      }
    this.numbers = new GridDataSource(list);
  }

  build() {
    Column({ space: 5 }) {
      Text('Grid1').fontColor(0x000000).fontSize(16).width('90%')
      Grid(this.scroller, this.layoutOptions1) {
        LazyForEach(this.numbers, (day: string) => {
          GridItem() {
            Text(day)
              .fontSize(16)
              .backgroundColor(0xF9CF93)
              .width('100%')
              .height(80)
              .textAlign(TextAlign.Center)
          }.selectable(false)
        }, (index: number) => index.toString())
      }
      .columnsTemplate('1fr 1fr 1fr 1fr 1fr')
      .columnsGap(10)
      .rowsGap(10)
      .multiSelectable(true)
      .scrollBar(BarState.Off)
      .width('90%')
      .backgroundColor(0xFAEEE0)
      .height(300)

      Text('Grid2').fontColor(0x000000).fontSize(16).width('90%')
      // 不使用scroll，需要undefined占位
      Grid(undefined, this.layoutOptions2) {
        LazyForEach(this.numbers, (day: string) => {
          GridItem() {
            Text(day)
              .fontSize(16)
              .backgroundColor(0xF9CF93)
              .width('100%')
              .height(80)
              .textAlign(TextAlign.Center)
          }
        }, (index: number) => index.toString())
      }
      .columnsTemplate('1fr 1fr 1fr 1fr 1fr')
      .columnsGap(10)
      .rowsGap(10)
      .scrollBar(BarState.Off)
      .width('90%')
      .backgroundColor(0xFAEEE0)
      .height(300)
    }.width('100%').margin({ top: 5 })
  }
```

![image](public_sys-resources/zh-cn_image_0000002522244884.webp)

#### 示例4（[Grid](Grid.md)嵌套滚动）

[nestedScroll](#ZH-CN_TOPIC_0000002553200787__nestedscroll10)和[onScrollFrameBegin](#ZH-CN_TOPIC_0000002553200787__onscrollframebegin10)的使用。

GridDataSource说明及完整代码参考[示例2可滚动grid和滚动事件](#ZH-CN_TOPIC_0000002553200787__示例2可滚动grid和滚动事件)。

```ets
import { GridDataSource } from './GridDataSource';

@Entry
@Component
struct GridExample {
  @State colors: number[] = [0xFFC0CB, 0xDA70D6, 0x6B8E23, 0x6A5ACD, 0x00FFFF, 0x00FF7F];
  numbers: GridDataSource = new GridDataSource([]);
  @State translateY: number = 0;
  private scroller: Scroller = new Scroller();
  private gridScroller: Scroller = new Scroller();
  private touchDown: boolean = false;
  private listTouchDown: boolean = false;
  private scrolling: boolean = false;

  aboutToAppear() {
    let list: string[] = [];
    for (let i = 0; i < 100; i++) {
      list.push(i.toString());
    }
    this.numbers = new GridDataSource(list);
  }

  build() {
    Stack() {
      Column() {
        Row() {
          Text('Head')
        }

        Column() {
          List({ scroller: this.scroller }) {
            ListItem() {
              Grid() {
                GridItem() {
                  Text('GoodsTypeList1')
                }
                .backgroundColor(this.colors[0])
                .columnStart(0)
                .columnEnd(1)

                GridItem() {
                  Text('GoodsTypeList2')
                }
                .backgroundColor(this.colors[1])
                .columnStart(0)
                .columnEnd(1)

                GridItem() {
                  Text('GoodsTypeList3')
                }
                .backgroundColor(this.colors[2])
                .columnStart(0)
                .columnEnd(1)

                GridItem() {
                  Text('GoodsTypeList4')
                }
                .backgroundColor(this.colors[3])
                .columnStart(0)
                .columnEnd(1)

                GridItem() {
                  Text('GoodsTypeList5')
                }
                .backgroundColor(this.colors[4])
                .columnStart(0)
                .columnEnd(1)
              }
              .scrollBar(BarState.Off)
              .columnsGap(15)
              .rowsGap(10)
              .rowsTemplate('1fr 1fr 1fr 1fr 1fr')
              .columnsTemplate('1fr')
              .width('100%')
              .height(200)
            }

            ListItem() {
              Grid(this.gridScroller) {
                LazyForEach(this.numbers, (item: string) => {
                  GridItem() {
                    Text(item)
                      .fontSize(16)
                      .backgroundColor(0xF9CF93)
                      .width('100%')
                      .height('100%')
                      .textAlign(TextAlign.Center)
                  }
                  .width('100%')
                  .height(40)
                  .shadow({ radius: 10, color: '#909399', offsetX: 1, offsetY: 1 })
                  .borderRadius(10)
                  .translate({ x: 0, y: this.translateY })
                }, (item: string) => item)
              }
              .columnsTemplate('1fr 1fr')
              .friction(0.3)
              .columnsGap(15)
              .rowsGap(10)
              .scrollBar(BarState.Off)
              .width('100%')
              .height('100%')
              .layoutDirection(GridDirection.Column)
              .nestedScroll({
                scrollForward: NestedScrollMode.PARENT_FIRST,
                scrollBackward: NestedScrollMode.SELF_FIRST
              })
              .onTouch((event: TouchEvent) => {
                if (event.type == TouchType.Down) {
                  this.listTouchDown = true;
                } else if (event.type == TouchType.Up) {
                  this.listTouchDown = false;
                }
              })
            }
          .scrollBar(BarState.Off)
          .edgeEffect(EdgeEffect.None)
          .onTouch((event: TouchEvent) => {
            if (event.type == TouchType.Down) {
              this.touchDown = true;
            } else if (event.type == TouchType.Up) {
              this.touchDown = false;
            }
          })
          .onScrollFrameBegin((offset: number, state: ScrollState) => {
            if (this.scrolling && offset > 0) {
              let newOffset = this.scroller.currentOffset().yOffset;
              if (newOffset >= 590) {
                this.gridScroller.scrollBy(0, offset);
                return { offsetRemain: 0 };
              } else if (newOffset + offset > 590) {
                this.gridScroller.scrollBy(0, newOffset + offset - 590);
                return { offsetRemain: 590 - newOffset };
            }
            return { offsetRemain: offset };
          })
          .onScrollStart(() => {
            if (this.touchDown && !this.listTouchDown) {
              this.scrolling = true;
            }
          })
          .onScrollStop(() => {
            this.scrolling = false;
          })
        }
        .width('100%')
        .height('100%')
        .padding({ left: 10, right: 10 })
      }

      Row() {
        Text('Top')
          .width(30)
          .height(30)
          .borderRadius(50)
      }
      .padding(5)
      .borderRadius(50)
      .backgroundColor('#ffffff')
      .shadow({ radius: 10, color: '#909399', offsetX: 1, offsetY: 1 })
      .margin({ right: 22, bottom: 15 })
      .onClick(() => {
        this.scroller.scrollTo({ xOffset: 0, yOffset: 0 });
        this.gridScroller.scrollTo({ xOffset: 0, yOffset: 0 });
      })
    }
    .align(Alignment.BottomEnd)
  }
```

![image](public_sys-resources/zh-cn_image_0000002553204845.webp)

#### 示例5（[Grid](Grid.md)拖拽场景）

1. 通过属性[editMode](#ZH-CN_TOPIC_0000002553200787__editmode8)设置Grid是否进入编辑模式，进入编辑模式可以拖拽Grid组件内部GridItem。

1. 在[onItemDragStart](#ZH-CN_TOPIC_0000002553200787__onitemdragstart8)回调中设置拖拽过程中显示的图片。

1. 在[onItemDrop](#ZH-CN_TOPIC_0000002553200787__onitemdrop8)中获取拖拽起始位置，和拖拽插入位置，并在[onItemDrop](#ZH-CN_TOPIC_0000002553200787__onitemdrop8)中完成交换数组位置逻辑。

1. 设置属性supportAnimation(true)支持动画。

预览器窗口不支持显示拖拽跟手。

GridDataSource说明及完整代码参考[示例2可滚动grid和滚动事件](#ZH-CN_TOPIC_0000002553200787__示例2可滚动grid和滚动事件)。

```ets
import { GridDataSource } from './GridDataSource';

@Entry
@Component
struct GridExample {
  numbers: GridDataSource = new GridDataSource([]);
  scroller: Scroller = new Scroller();
  @State text: string = 'drag';

  @Builder pixelMapBuilder() { //拖拽过程样式
    Column() {
      Text(this.text)
        .fontSize(16)
        .backgroundColor(0xF9CF93)
        .width(80)
        .height(80)
        .textAlign(TextAlign.Center)
  }

  aboutToAppear() {
    let list: string[] = [];
    for (let i = 1; i <= 15; i++) {
      list.push(i + '');
    }
    this.numbers = new GridDataSource(list);
  }

  changeIndex(index1: number, index2: number) { //交换数组位置
    this.numbers.swapItem(index1, index2);
  }

  build() {
    Column({ space: 5 }) {
      Grid(this.scroller) {
        LazyForEach(this.numbers, (day: string) => {
          GridItem() {
            Text(day)
              .fontSize(16)
              .backgroundColor(0xF9CF93)
              .width(80)
              .height(80)
              .textAlign(TextAlign.Center)
          }
        }, (day: string) => day)
      }
      .columnsTemplate('1fr 1fr 1fr')
      .columnsGap(10)
      .rowsGap(10)
      .width('90%')
      .backgroundColor(0xFAEEE0)
      .height(300)
      .editMode(true) //设置Grid是否进入编辑模式，进入编辑模式可以拖拽Grid组件内部GridItem
      .supportAnimation(true) // 设置支持动画
      .onItemDragStart((event: ItemDragInfo, itemIndex: number) => { //第一次拖拽此事件绑定的组件时，触发回调。
        this.text = this.numbers.getData(itemIndex);
        return this.pixelMapBuilder(); //设置拖拽过程中显示的图片。
      })
      .onItemDrop((event: ItemDragInfo, itemIndex: number, insertIndex: number, isSuccess: boolean) => { //绑定此事件的组件可作为拖拽释放目标，当在本组件范围内停止拖拽行为时，触发回调。
        // isSuccess=false时，说明drop的位置在grid外部；insertIndex > length时，说明有新增元素的事件发生
        if (!isSuccess || insertIndex >= this.numbers.totalCount()) {
          return;
        }
        console.info('itemIndex:' + itemIndex + ', insertIndex:' + insertIndex); //itemIndex拖拽起始位置，insertIndex拖拽插入位置
        this.changeIndex(itemIndex, insertIndex);
      })
    }.width('100%').margin({ top: 5 })
  }
```

示例图：

网格子组件开始拖拽：

网格子组件拖拽过程中：

网格子组件1与子组件6拖拽交换位置后：

拖拽动画：

![image](public_sys-resources/zh-cn_image_0000002553204847.webp)

#### 示例6（自适应[Grid](Grid.md)）

[layoutDirection](#ZH-CN_TOPIC_0000002553200787__layoutdirection8)、[maxCount](#ZH-CN_TOPIC_0000002553200787__maxcount8)、[minCount](#ZH-CN_TOPIC_0000002553200787__mincount8)、[cellLength](#ZH-CN_TOPIC_0000002553200787__celllength8)的使用。

GridDataSource说明及完整代码参考[示例2可滚动grid和滚动事件](#ZH-CN_TOPIC_0000002553200787__示例2可滚动grid和滚动事件)。

```ets
import { GridDataSource } from './GridDataSource';

@Entry
@Component
struct GridExample {
  numbers: GridDataSource = new GridDataSource([]);

  aboutToAppear() {
    let list: string[] = [];
    for (let i = 1; i <= 30; i++) {
      list.push(i + '');
    }
    this.numbers = new GridDataSource(list);
  }

  build() {
    Scroll() {
      Column({ space: 5 }) {
        Blank()
        Text('rowsTemplate、columnsTemplate都不设置时，layoutDirection、maxCount、minCount、cellLength才生效')
          .fontSize(16).fontColor(0x000000).width('90%')
        Grid() {
          LazyForEach(this.numbers, (day: string) => {
            GridItem() {
              Text(day).fontSize(16).backgroundColor(0xF9CF93)
            }.width(40).height(80).borderWidth(2).borderColor(Color.Red)
          }, (day: string) => day)
        }
        .height(300)
        .columnsGap(10)
        .rowsGap(10)
        .backgroundColor(0xFAEEE0)
        .maxCount(6)
        .minCount(2)
        .cellLength(0)
        .layoutDirection(GridDirection.Row)
      }
      .width('90%').margin({ top: 5, left: 5, right: 5 })
      .align(Alignment.Center)
    }
```

#### 示例7（双指缩放修改[Grid](Grid.md)列数）

双指缩放修改[Grid](Grid.md)列数。

GridDataSource说明及完整代码参考[示例2可滚动grid和滚动事件](#ZH-CN_TOPIC_0000002553200787__示例2可滚动grid和滚动事件)。

```ets
// xxx.ets
import { GridDataSource } from './GridDataSource';

@Entry
@Component
struct GridExample {
  numbers: GridDataSource = new GridDataSource([]);
  @State columns: number = 2;

  aboutToAppear() {
    let lastCount = AppStorage.get<number>('columnsCount');
    if (typeof lastCount != 'undefined') {
      this.columns = lastCount;
    }

    let list: string[] = [];
    for (let i = 0; i < 20; i++) {
      for (let j = 0; j < 20; j++) {
        list.push(j.toString());
    }
    this.numbers = new GridDataSource(list);
  }

  build() {
    Column({ space: 5 }) {
      Row() {
        Text('双指缩放改变列数')
          .height('5%')
          .margin({ top: 10, left: 20 })
      }

      Grid() {
        LazyForEach(this.numbers, (day: string) => {
          GridItem() {
            Text(day)
              .fontSize(16)
              .backgroundColor(0xF9CF93)
              .width('100%')
              .height(80)
              .textAlign(TextAlign.Center)
          }
        }, (index: number) => index.toString())
      }
      .columnsTemplate('1fr '.repeat(this.columns))
      .columnsGap(10)
      .rowsGap(10)
      .width('90%')
      .scrollBar(BarState.Off)
      .backgroundColor(0xFAEEE0)
      .height('100%')
      .cachedCount(3)
      // 切换列数item位置重排动画
      .animation({
        duration: 300,
        curve: Curve.Smooth
      })
      .priorityGesture(
        PinchGesture()
          .onActionEnd((event: GestureEvent) => {
            console.info('end scale:' + event.scale);
            // 手指分开，减少列数以放大Item，触发阈值可以自定义，示例为2
            if (event.scale > 2) {
              this.columns--;
            } else if (event.scale < 0.6) {
              this.columns++;
            }
            // 可以根据设备屏幕宽度设定最大和最小列数，此处以最小1列最大4列为例
            this.columns = Math.min(4, Math.max(1, this.columns));
            AppStorage.setOrCreate<number>('columnsCount', this.columns);
          })
      )
    }.width('100%').margin({ top: 5 })
  }
```

![image](public_sys-resources/zh-cn_image_0000002553364809.webp)

#### 示例8（设置自适应列数）

属性[columnsTemplate](#ZH-CN_TOPIC_0000002553200787__columnstemplate)中auto-fill、auto-fit和auto-stretch的使用示例。

```ets
@Entry
@Component
struct GridColumnsTemplate {
  data: number[] = [0, 1, 2, 3, 4, 5];
  data1: number[] = [0, 1, 2, 3, 4, 5];
  data2: number[] = [0, 1, 2, 3, 4, 5];

  build() {
    Column({ space: 10 }) {
      Text('auto-fill 根据设定的列宽自动计算列数').width('90%')
      Grid() {
        ForEach(this.data, (item: number) => {
          GridItem() {
            Text('N' + item).height(80)
          }
          .backgroundColor(Color.Orange)
        })
      }
      .width('90%')
      .border({ width: 1, color: Color.Black })
      .columnsTemplate('repeat(auto-fill, 70)')
      .columnsGap(10)
      .rowsGap(10)
      .height(150)

      Text('auto-fit 先根据设定的列宽计算列数，余下的空间会均分到每一列中').width('90%')
      Grid() {
        ForEach(this.data1, (item: number) => {
          GridItem() {
            Text('N' + item).height(80)
          }
          .backgroundColor(Color.Orange)
        })
      }
      .width('90%')
      .border({ width: 1, color: Color.Black })
      .columnsTemplate('repeat(auto-fit, 70)')
      .columnsGap(10)
      .rowsGap(10)
      .height(150)

      Text('auto-stretch 先根据设定的列宽计算列数，余下的空间会均分到每个列间距中').width('90%')
      Grid() {
        ForEach(this.data2, (item: number) => {
          GridItem() {
            Text('N' + item).height(80)
          }
          .backgroundColor(Color.Orange)
        })
      }
      .width('90%')
      .border({ width: 1, color: Color.Black })
      .columnsTemplate('repeat(auto-stretch, 70)')
      .columnsGap(10)
      .rowsGap(10)
      .height(150)
    }
    .width('100%')
    .height('100%')
  }
```

#### 示例9（以当前行最高的[GridItem](GridItem.md)的高度为其他GridItem的高度）

下面的Grid中包含两列，每列中的[GridItem](GridItem.md)包括高度确定的两个Column和一个高度不确定的Text共三个子组件。

在默认情况下，左右两个GridItem的高度可能是不同的；在设置了Grid的[alignItems](#ZH-CN_TOPIC_0000002553200787__alignitems12)属性为GridItemAlignment.STRETCH后，一行左右两个GridItem中原本高度较小的GridItem会以另一个高度较大的GridItem的高度作为自己的高度。

GridDataSource说明及完整代码参考[示例2可滚动grid和滚动事件](#ZH-CN_TOPIC_0000002553200787__示例2可滚动grid和滚动事件)。

```ets
import { GridDataSource } from './GridDataSource';

@Entry
@Component
struct Index {
  data: GridDataSource = new GridDataSource([]);
  @State items: number[] = [];

  aboutToAppear(): void {
    let list: string[] = [];
    for (let i = 0; i < 100; i++) {
      list.push(i.toString());
      this.items.push(this.getSize());
    }
    this.data= new GridDataSource(list);
  }

  getSize() {
    let ret = Math.floor(Math.random() * 5);
    return Math.max(1, ret);
  }

  build() {
    Column({ space: 10 }) {
      Text('Grid alignItems示例代码')

      Grid() {
        LazyForEach(this.data, (item: number) => {
          // GridItem和Column不设置高度，默认会自适应子组件大小，设置STRETCH的场景下，会变成与当前行最高节点同高。
          // 若设置高度，则会保持已设置的高度，不会与当前行最高节点同高。
          GridItem() {
            Column() {
              Column().height(100).backgroundColor('#D5D5D5').width('100%')
              // 中间的Text设置flexGrow(1)来自适应填满父组件的空缺
              Text('这是一段文字。'.repeat(this.items[item]))
                .flexGrow(1).width('100%').align(Alignment.TopStart)
                .backgroundColor('#F7F7F7')
              Column().height(50).backgroundColor('#707070').width('100%')
            }
          .border({ color: Color.Black, width: 1 })
        })
      }
      .columnsGap(10)
      .rowsGap(5)
      .columnsTemplate('1fr 1fr')
      .width('80%')
      .height('100%')
      // Grid设置alignItems为STRETCH，以当前行最高的GridItem的高度为其他GridItem的高度。
      .alignItems(GridItemAlignment.STRETCH)
      .scrollBar(BarState.Off)
    }
    .height('100%')
    .width('100%')
  }
```

![image](public_sys-resources/zh-cn_image_0000002553204849.webp)

#### 示例10（设置边缘渐隐）

通过[fadingEdge](滚动组件通用接口.md#ZH-CN_TOPIC_0000002522240828__fadingedge14)属性来设置边缘渐隐效果。

GridDataSource说明及完整代码参考[示例2可滚动grid和滚动事件](#ZH-CN_TOPIC_0000002553200787__示例2可滚动grid和滚动事件)。

```ets
// xxx.ets
//该示例实现了Grid组件开启边缘渐隐效果并设置边缘渐隐长度
import { LengthMetrics } from '@kit.ArkUI';
import { GridDataSource } from './GridDataSource';

@Entry
@Component
struct GridExample {
  numbers: GridDataSource = new GridDataSource([]);
  scroller: Scroller = new Scroller();

  aboutToAppear() {
    let list: string[] = [];
    for (let i = 0; i <= 10; i++) {
      for (let j = 0; j < 5; j++) {
        list.push(j.toString());
      }
    this.numbers = new GridDataSource(list);
  }

  build() {
    Column({ space: 5 }) {
      Text('Grid').fontColor(0x000000).fontSize(16).width('90%')
      Grid(this.scroller) {
        LazyForEach(this.numbers, (day: string) => {
          GridItem() {
            Text(day)
              .fontSize(16)
              .backgroundColor(0xF9CF93)
              .width('100%')
              .height(80)
              .textAlign(TextAlign.Center)
          }
        }, (index: number) => index.toString())
      }
      .columnsTemplate('1fr 1fr 1fr 1fr 1fr')
      .columnsGap(10)
      .rowsGap(20)
      .height('90%')
      .fadingEdge(true, { fadingEdgeLength: LengthMetrics.vp(80) })

    }.width('100%').margin({ top: 5 })
  }
```

![image](public_sys-resources/zh-cn_image_0000002522084896.webp)

#### 示例11（单边边缘效果）

该示例通过[edgeEffect](#ZH-CN_TOPIC_0000002553200787__edgeeffect10)接口，实现了Grid组件设置单边边缘效果。

GridDataSource说明及完整代码参考[示例2可滚动grid和滚动事件](#ZH-CN_TOPIC_0000002553200787__示例2可滚动grid和滚动事件)。

```ets
// xxx.ets
import { GridDataSource } from './GridDataSource';

@Entry
@Component
struct GridExample {
  numbers: GridDataSource = new GridDataSource([]);
  scroller: Scroller = new Scroller();

  aboutToAppear() {
    let list: string[] = [];
    for (let i = 0; i <= 10; i++) {
      for (let j = 0; j < 5; j++) {
        list.push(j.toString());
    }
    this.numbers = new GridDataSource(list);
  }

  build() {
    Column({ space: 5 }) {
      Grid(this.scroller) {
        LazyForEach(this.numbers, (day: string) => {
          GridItem() {
            Text(day)
              .fontSize(16)
              .backgroundColor(0xF9CF93)
              .width('100%')
              .height(80)
              .textAlign(TextAlign.Center)
          }
        }, (index: number) => index.toString())
      }
      .columnsTemplate('1fr 1fr 1fr 1fr 1fr')
      .columnsGap(10)
      .rowsGap(20)
      .edgeEffect(EdgeEffect.Spring, { alwaysEnabled: true, effectEdge: EffectEdge.START })
      .width('90%')
      .backgroundColor(0xDCDCDC)
      .height('80%')

    }.width('100%').margin({ top: 5 })
  }
```

![image](public_sys-resources/zh-cn_image_0000002553364811.webp)

#### 示例12（方向键走焦换行模式）

从API version 20开始，该示例通过[focusWrapMode](#ZH-CN_TOPIC_0000002553200787__focuswrapmode20)接口，实现了Grid组件方向键走焦换行效果。

```ets
// xxx.ets
@Entry
@Component
struct GridExample {
  scroller: Scroller = new Scroller();
  build() {
    Column() {
      Grid(this.scroller) {
        GridItem() {
          Text('A')
            .focusable(true)
            .fontSize(18)
            .fontWeight(5)
            .backgroundColor(0xF9CF93)
            .width('100%')
            .height(80)
            .textAlign(TextAlign.Center)
        }
        GridItem() {
          Text('B')
            .focusable(true)
            .fontSize(18)
            .fontWeight(5)
            .backgroundColor(0xF9CF93)
            .width('100%')
            .height(80)
            .textAlign(TextAlign.Center)
        }
        GridItem() {
          Text('C')
            .focusable(true)
            .fontSize(18)
            .fontWeight(5)
            .backgroundColor(0xF9CF93)
            .width('100%')
            .height(80)
            .textAlign(TextAlign.Center)
        }
        GridItem() {
          Text('D')
            .focusable(true)
            .fontSize(18)
            .fontWeight(5)
            .backgroundColor(0xF9CF93)
            .width('100%')
            .height(80)
            .textAlign(TextAlign.Center)
        }
        GridItem() {
          Text('E')
            .focusable(true)
            .fontSize(18)
            .fontWeight(5)
            .backgroundColor(0xF9CF93)
            .width('100%')
            .height(80)
            .textAlign(TextAlign.Center)
        }
        GridItem() {
          Text('F')
            .focusable(true)
            .fontSize(18)
            .fontWeight(5)
            .backgroundColor(0xF9CF93)
            .width('100%')
            .height(80)
            .textAlign(TextAlign.Center)
        }
      .focusWrapMode(FocusWrapMode.WRAP_WITH_ARROW)
      .columnsTemplate('1fr 1fr 1fr 1fr 1fr')
      .columnsGap(10)
      .rowsGap(20)
      .backgroundColor(0xDCDCDC)
    }.width('100%').margin({ top: 5 })
  }
```

![image](public_sys-resources/zh-cn_image_0000002522244890.webp)

#### 示例13（设置滚动事件）

该示例通过FrameNode中的[getEvent('Grid')](FrameNode.md#ZH-CN_TOPIC_0000002522240744__geteventgrid19)获取[UIGridEvent](#ZH-CN_TOPIC_0000002553200787__uigridevent19)，并为Grid设置滚动事件回调，用于事件监听方因无法直接修改页面代码而无法使用声明式接口设置回调的场景。

从API version 19开始，新增UI[Grid](Grid.md)Event接口。

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
    let gridEvent: UIGridEvent | undefined = typeNode.getEvent(frameNode, 'Grid');
    gridEvent?.setOnWillScroll((scrollOffset: number, scrollState: ScrollState, scrollSource: ScrollSource) => {
      console.info(`onWillScroll scrollOffset = ${scrollOffset}, scrollState = ${scrollState}, scrollSource = ${scrollSource}`);
    });
    gridEvent?.setOnDidScroll((scrollOffset: number, scrollState: ScrollState) => {
      console.info(`onDidScroll scrollOffset = ${scrollOffset}, scrollState = ${scrollState}`);
    });
    gridEvent?.setOnReachStart(() => {
      console.info(`onReachStart`);
    });
    gridEvent?.setOnReachEnd(() => {
      console.info(`onReachEnd`);
    });
    gridEvent?.setOnScrollStart(() => {
      console.info(`onScrollStart`);
    });
    gridEvent?.setOnScrollStop(() => {
      console.info(`onScrollStop`);
    });
    gridEvent?.setOnScrollFrameBegin((offset: number, state: ScrollState) => {
      console.info(`onScrollFrameBegin offset = ${offset}, state = ${state}`);
      return undefined;
    });
    gridEvent?.setOnScrollIndex((first: number, last: number) => {
      console.info(`onScrollIndex start = ${first}, end = ${last}`);
    });
  }

@Entry
@Component
struct Index {
  @State index: number = 0;
  private myNodeController: MyNodeController = new MyNodeController();
  @State numbers: string[] = [];

  aboutToAppear() {
    for (let i = 0; i < 5; i++) {
      for (let j = 0; j < 5; j++) {
        this.numbers.push(j.toString());
  }

  build() {
    Column() {
      Button('add CommonEvent to Grid')
        .onClick(() => {
          this.myNodeController!.addCommonEvent(this.myNodeController!.rootNode!.getParent()!.getPreviousSibling()!);
        })
      Grid() {
        ForEach(this.numbers, (day: string, index: number) => {
          GridItem() {
            Text(day)
              .fontSize(16)
              .backgroundColor(0xF9CF93)
              .width('100%')
              .height(80)
              .textAlign(TextAlign.Center)
          }
        }, (day: string, index: number) => index.toString() + day)
      }
      .columnsTemplate('1fr 1fr 1fr 1fr 1fr')
      .columnsGap(10)
      .rowsGap(10)
      .enableScrollInteraction(true)
      .width('90%')
      .backgroundColor(0xFAEEE0)
      .height(300)
      NodeContainer(this.myNodeController)
    }.width('100%')
  }
```

#### 示例14（滚动到指定位置）

该示例通过[scrollToIndex](Scroll.md#ZH-CN_TOPIC_0000002553360749__scrolltoindex)接口，实现了Grid组件滚动到指定位置。

GridDataSource说明及完整代码参考[示例2可滚动grid和滚动事件](#ZH-CN_TOPIC_0000002553200787__示例2可滚动grid和滚动事件)。

```ets
import { GridDataSource } from './GridDataSource';
@Entry
@Component
struct GridScrollToIndexSample {
  numbers: GridDataSource = new GridDataSource([]);
  scroller: Scroller = new Scroller();
  aboutToAppear(): void {
    let list: string[] = [];
    for (let i = 0; i < 10; i++) {
      for (let j = 0; j < 10; j++) {
        list.push((i * 5 + j  + 1).toString());
    }
    this.numbers =  new GridDataSource(list);
  }

  build() {
    Column({ space: 5 }) {
      Button('scrollToIndex')
        .onClick(() => { // 滚动到对应的位置
          this.scroller.scrollToIndex(25, true, ScrollAlign.START);
        })
      Grid(this.scroller) {
        LazyForEach(this.numbers, (day: string) => {
          GridItem() {
            Text(day)
              .fontSize(16)
              .backgroundColor(0xF9CF93)
              .width('100%')
              .height(80)
              .textAlign(TextAlign.Center)
          }
        }, (index: number) => index.toString())
      }
      .columnsTemplate('1fr 1fr 1fr 1fr 1fr')
      .columnsGap(10)
      .rowsGap(10)
      .friction(0.6)
      .enableScrollInteraction(true)
      .supportAnimation(false)
      .multiSelectable(false)
      .edgeEffect(EdgeEffect.Spring)
      .scrollBar(BarState.On)
      .scrollBarColor(Color.Grey)
      .scrollBarWidth(4)
      .width('90%')
      .backgroundColor(0xFAEEE0)
      .height(300)
    }.width('100%').margin({ top: 5 })
  }
```

![image](public_sys-resources/zh-cn_image_0000002553204851.webp)

#### 示例15（实现[Grid](Grid.md)滑动选择）

该示例通过[PanGesture]([PanGesture](PanGesture.md#ZH-CN_TOPIC_0000002497604860__pangesture-1).md#ZH-CN_TOPIC_0000002522080810__pangesture-1)接口，实现了Grid组件一边滑动一边选择的效果。

GridDataSource说明及完整代码参考[示例2可滚动grid和滚动事件](#ZH-CN_TOPIC_0000002553200787__示例2可滚动grid和滚动事件)。

```ets
// xxx.ets
import { GridDataSource } from './GridDataSource';
import { display, curves } from '@kit.ArkUI';

enum SlideActionType {
  START,
  UPDATE,
  END
}
// 热区
const HOT_AREA_LENGTH =
  Math.round(display.getDefaultDisplaySync().densityDPI * 10 / 25.4 / display.getDefaultDisplaySync().densityPixels);
// 滚动曲线: 贝塞尔曲线
const SLIDE_SELECT_SPEED_CURVE = curves.cubicBezierCurve(0.33, 0, 0.67, 1);
// 滚动速度: 最大速度
const AUTO_SPEED_MAX: number = Math.round(2400 / display.getDefaultDisplaySync().densityPixels);
@Entry
@Component
struct GridExample {
  numbers: GridDataSource = new GridDataSource([]);
  scroller: Scroller = new Scroller();
  @State selectedIndexes: string[] = [];
  // 滑动多选时，当前变更选中状态的item
  @State updateIndex: number = -1;
  @State lastUpdateIndex: number = -1;
  @State updateTimer: number = new Date().valueOf();
  // 是否可进行滑动多选
  @State canSlideSelect: boolean = false;
  @State isAutoScroll: boolean = false;
  // 停止手势
  @State stopGesture: boolean = false;
  private scrollStartIndex: number = 0;
  private scrollEndIndex: number = 0;
  // 滑动的初始点位
  @State startIndex: number = -1;
  @State endIndex: number = -1;
  // 滚动部位显示区域的高度
  @State contentHeight: number = 0;
  @State areaY: number = 0;
  // 列表宽度
  @State listWidth: number = 0;
  @State oldCheckList: boolean[] = [];
  // 滑动过程中是否将经过的点设为选中状态
  @State setChecked: boolean = false;
  aboutToAppear() {
    let list: string[] = [];
    for (let i = 0; i < 20; i++) {
      for (let j = 0; j < 20; j++) {
        list.push((20 * i + j + 1).toString());
      }
    this.numbers = new GridDataSource(list);
  }
  /**
   * 获取当前点位
   * @param finger
   * @returns
   */
  getIndex(finger: FingerInfo): number {
    // 初始化数据
    let index = -1;
    try {
      index = this.scroller.getItemIndex(finger.localX, finger.localY);
      if (index === -1) {
        for (let i = this.scrollStartIndex; i <= this.scrollEndIndex; i++) {
          const item = this.scroller.getItemRect(i);
          if (finger.localY < item.y ||
            finger.localY >= item.y && finger.localY <= item.y + item.height && finger.localX < item.x) {
            break;
          }
          index = i;
      }
    } catch {
      this.stopGesture = true;
      return index;
    }
    return index;
  }
  slideActionStart(index: number): void {
    if (index < 0) {
      return;
    }
    console.debug('start index: ' + index.toString());
    const targetIndex = index + 1;
    this.setChecked = !this.selectedIndexes.includes(targetIndex.toString());
    this.startIndex = index;
    this.selectedIndexes.push(targetIndex.toString());
    this.updateIndex = index;

  }
  slideActionUpdate(index: number): void {
    if (!this.canSlideSelect) {
      return;
    }
    if (this.startIndex === -1) {
      //（初始接触点在空隙）时，重新配置滑动的初始数据
      this.slideActionStart(index);
      return;
    }
    if (index === -1) {
      return;
    }

    this.lastUpdateIndex = this.updateIndex;
    this.setItemChecked(index);
    this.updateIndex = index;
  }
  setItemChecked(index: number):void {
    const start = Math.min(this.startIndex, index);
    const end = Math.max(this.startIndex, index);
    for (let i = start; i < end+1;i++) {
      const item = (i+1).toString();
      if (this.setChecked) {
        this.selectedIndexes.push(item);
      } else {
        if (this.selectedIndexes.includes(item)) {
          this.selectedIndexes = this.selectedIndexes.filter(selectIndex => selectIndex != item);
        }

      }
  /**
   * 滑动结束
   */
  slideActionEnd(): void {
    this.startIndex = -1;
    this.updateIndex = -1;
    this.scroller.scrollBy(0, 0);
    this.isAutoScroll = false;
  }
  /**
   * 自动滚动--
   * @param finger
   */
  autoScroll(finger: FingerInfo): void {
    // 不可多选
    if (!this.canSlideSelect) {
      return;
    }
    let pointY = finger.globalY - this.areaY;
    if (pointY <= HOT_AREA_LENGTH) {
      if (this.isAutoScroll && pointY <= 0) {
        return;
      }
      const speedFlag = pointY > 0 ? SLIDE_SELECT_SPEED_CURVE
        .interpolate(1 - pointY / HOT_AREA_LENGTH) : 1;
      this.scroller.scrollEdge(Edge.Top, {
        velocity: speedFlag * AUTO_SPEED_MAX
      });
      this.isAutoScroll = true;
    } else if (pointY > this.contentHeight - HOT_AREA_LENGTH) {
      if (this.isAutoScroll && pointY >= this.contentHeight) {
        return;
      }
      const speedFlag = pointY < this.contentHeight ? SLIDE_SELECT_SPEED_CURVE
        .interpolate(1 - (this.contentHeight - pointY) / HOT_AREA_LENGTH) : 1;
      this.scroller.scrollEdge(Edge.Bottom, {
        velocity: speedFlag * AUTO_SPEED_MAX
      });
      this.isAutoScroll = true;
    } else {
      if (this.isAutoScroll) {
        this.scroller.scrollBy(0, 0);
        this.isAutoScroll = false;
      }

  panGestureAction(type: SlideActionType, event: GestureEvent | undefined): void {
    if (this.stopGesture || !event) {
      return;
    }
    const finger = event!.fingerList[0];
    const index = this.getIndex(finger);
    switch (type) {
      case SlideActionType.START: {
        this.slideActionStart(index);
        break;
      }
      case SlideActionType.UPDATE: {
        this.slideActionUpdate(index);
        this.autoScroll(finger);
        break;
      }
      case SlideActionType.END: {
        this.slideActionEnd();
        break;
      }
      default: {
      }
  build() {
    Column({ space: 5 }) {
      Grid(this.scroller) {
        LazyForEach(this.numbers, (day: string) => {
          GridItem() {
            Stack() {
              Text(day)
                .fontSize(16)
                .backgroundColor(0xF9CF93)
                .width('100%')
                .height(80)
                .textAlign(TextAlign.Center)
              if (this.canSlideSelect) {
                // $r('app.media.gouxuan')和$r('app.media.weigouxuan')需要替换为开发者所需的图像资源文件。
                Image(this.selectedIndexes.includes(day) ? $r('app.media.gouxuan') :$r('app.media.weigouxuan'))
                  .width(30)
                  .height(30)
                  .position({right:5,top:5})
                  .draggable(false)
            }

          }
        }, (index: number) => index.toString())
      }
      .columnsTemplate('1fr 1fr 1fr')
      .columnsGap(10)
      .rowsGap(10)
      .friction(0.6)
      .enableScrollInteraction(true)
      .supportAnimation(false)
      .multiSelectable(false)
      .edgeEffect(EdgeEffect.Spring)
      .scrollBar(BarState.On)
      .scrollBarColor(Color.Grey)
      .scrollBarWidth(4)
      .width('90%')
      .height('85%')
      .draggable(!this.canSlideSelect)
      .backgroundColor(0xFAEEE0)
      .onAreaChange((oldVal, newVal) => {
        this.listWidth = newVal.width as number;
        this.areaY = newVal.globalPosition.y as number;
        this.contentHeight = newVal.height as number;
      })
      .onScrollIndex((start, end) => {
        this.scrollStartIndex = start;
        this.scrollEndIndex = end;
      })
      .gesture(
        // 手势滑动
        PanGesture({ direction: PanDirection.Vertical })
          .onActionStart((event: GestureEvent | undefined) => {
            this.panGestureAction(SlideActionType.START, event);
          })
          .onActionUpdate((event: GestureEvent | undefined) => {
            this.panGestureAction(SlideActionType.UPDATE, event);
          })
          .onActionEnd((event?: GestureEvent) => {
            this.panGestureAction(SlideActionType.END, event);
          }),
        GestureMask.Normal
      )
      .onGestureRecognizerJudgeBegin((event: BaseGestureEvent, current: GestureRecognizer,
        recognizers: Array<GestureRecognizer>) => {
        if (this.canSlideSelect && current.isBuiltIn() &&
          current.getType() == GestureControl.GestureType.PAN_GESTURE) {
          return GestureJudgeResult.REJECT;
        }
        return GestureJudgeResult.CONTINUE;
      })
      Row() {
        Button('开始编辑').onClick(()=>{
          this.selectedIndexes = [];
          this.canSlideSelect = true;
        })
        Button('结束编辑').onClick(()=>{
          this.canSlideSelect = false;
          this.selectedIndexes = [];
        })
      }
      .margin({
        bottom: 30
      })
      Text(`${this.selectedIndexes.join(',')}`)
    }.width('100%').margin({ top: 5 })
  }
```

![image](public_sys-resources/zh-cn_image_0000002522084898.webp)

#### 示例16（实现[GridItem](GridItem.md)自定义拖拽）

该示例通过[gesture](绑定手势方法.md#ZH-CN_TOPIC_0000002522240806__[gesture](绑定手势方法.md#ZH-CN_TOPIC_0000002529284849__gesture))接口，实现了GridItem组件自定义拖拽效果。

```ets
import { curves } from '@kit.ArkUI';

@Entry
@Component
struct GridItemExample {
  @State numbers: number[] = [];
  @State dragItem: number = -1;
  @State scaleItem: number = -1;
  @State item: number = -1;
  private dragRefOffsetX: number = 0;
  private dragRefOffsetY: number = 0;
  @State offsetX: number = 0;
  @State offsetY: number = 0;
  private FIX_VP_X: number = 108;
  private FIX_VP_Y: number = 120;

  aboutToAppear() {
    for (let i = 1; i <= 11; i++) {
      this.numbers.push(i);
  }

  itemMove(index: number, newIndex: number): void {
    console.info('index:' + index + ' newIndex:' + newIndex);
    if (!this.isDraggable(newIndex)) {
      return;
    }
    let tmp = this.numbers.splice(index, 1);
    this.numbers.splice(newIndex, 0, tmp[0]);
  }

  //向下滑
  down(index: number): void {
    // 指定固定GridItem不响应事件
    if (!this.isDraggable(index + 3)) {
      return;
    }
    this.offsetY -= this.FIX_VP_Y;
    this.dragRefOffsetY += this.FIX_VP_Y;
    this.itemMove(index, index + 3);
  }

  //向下滑(右下角为空)
  down2(index: number): void {
    if (!this.isDraggable(index + 3)) {
      return;
    }
    this.offsetY -= this.FIX_VP_Y;
    this.dragRefOffsetY += this.FIX_VP_Y;
    this.itemMove(index, index + 3);
  }

  //向上滑
  up(index: number): void {
    if (!this.isDraggable(index - 3)) {
      return;
    }
    this.offsetY += this.FIX_VP_Y;
    this.dragRefOffsetY -= this.FIX_VP_Y;
    this.itemMove(index, index - 3);
  }

  //向左滑
  left(index: number): void {
    if (!this.isDraggable(index - 1)) {
      return;
    }
    this.offsetX += this.FIX_VP_X;
    this.dragRefOffsetX -= this.FIX_VP_X;
    this.itemMove(index, index - 1);
  }

  //向右滑
  right(index: number): void {
    if (!this.isDraggable(index + 1)) {
      return;
    }
    this.offsetX -= this.FIX_VP_X;
    this.dragRefOffsetX += this.FIX_VP_X;
    this.itemMove(index, index + 1);
  }

  //向右下滑
  lowerRight(index: number): void {
    if (!this.isDraggable(index + 4)) {
      return;
    }
    this.offsetX -= this.FIX_VP_X;
    this.dragRefOffsetX += this.FIX_VP_X;
    this.offsetY -= this.FIX_VP_Y;
    this.dragRefOffsetY += this.FIX_VP_Y;
    this.itemMove(index, index + 4);
  }

  //向右上滑
  upperRight(index: number): void {
    if (!this.isDraggable(index - 2)) {
      return;
    }
    this.offsetX -= this.FIX_VP_X;
    this.dragRefOffsetX += this.FIX_VP_X;
    this.offsetY += this.FIX_VP_Y;
    this.dragRefOffsetY -= this.FIX_VP_Y;
    this.itemMove(index, index - 2);
  }

  //向左下滑
  lowerLeft(index: number): void {
    if (!this.isDraggable(index + 2)) {
      return;
    }
    this.offsetX += this.FIX_VP_X;
    this.dragRefOffsetX -= this.FIX_VP_X;
    this.offsetY -= this.FIX_VP_Y;
    this.dragRefOffsetY += this.FIX_VP_Y;
    this.itemMove(index, index + 2);
  }

  //向左上滑
  upperLeft(index: number): void {
    if (!this.isDraggable(index - 4)) {
      return;
    }
    this.offsetX += this.FIX_VP_X;
    this.dragRefOffsetX -= this.FIX_VP_X;
    this.offsetY += this.FIX_VP_Y;
    this.dragRefOffsetY -= this.FIX_VP_Y;
    this.itemMove(index, index - 4);
  }

  isDraggable(index: number): boolean {
    console.info('index:' + index)
    return index > 1;
  }

  build() {
    Column() {
      Grid() {
        ForEach(this.numbers, (item: number) => {
          GridItem() {
            Text(item + '')
              .fontSize(16)
              .width('100%')
              .textAlign(TextAlign.Center)
              .height(100)
              .borderRadius(10)
              .backgroundColor(0xF9CF93)
              .shadow(this.scaleItem == item ? {
                radius: 70,
                color: '#15000000',
                offsetX: 0,
                offsetY: 0
              } :
                {
                  radius: 0,
                  color: '#15000000',
                  offsetX: 0,
                  offsetY: 0
                })
              .animation({ curve: Curve.Sharp, duration: 300 })
          }
          // 指定固定GridItem不响应事件
          .hitTestBehavior(this.isDraggable(this.numbers.indexOf(item)) ? HitTestMode.Default : HitTestMode.None)
          .scale({ x: this.scaleItem == item ? 1.05 : 1, y: this.scaleItem == item ? 1.05 : 1 })
          .zIndex(this.dragItem == item ? 1 : 0)
          .translate(this.dragItem == item ? { x: this.offsetX, y: this.offsetY } : { x: 0, y: 0 })
          .padding(10)
          .gesture(
            // 以下组合手势为顺序识别，当长按手势事件未正常触发时则不会触发拖动手势事件
            GestureGroup(GestureMode.Sequence,
              LongPressGesture({ repeat: true })
                .onAction((event?: GestureEvent) => {
                  this.getUIContext()?.animateTo({ curve: Curve.Friction, duration: 300 }, () => {
                    this.scaleItem = item;
                  })
                .onActionEnd(() => {
                  this.getUIContext()?.animateTo({ curve: Curve.Friction, duration: 300 }, () => {
                    this.scaleItem = -1;
                  })
                }),
              PanGesture({ fingers: 1, direction: null, distance: 0 })
                .onActionStart(() => {
                  this.dragItem = item;
                  this.dragRefOffsetX = 0;
                  this.dragRefOffsetY = 0;
                })
                .onActionUpdate((event: GestureEvent) => {
                  this.offsetY = event.offsetY - this.dragRefOffsetY;
                  this.offsetX = event.offsetX - this.dragRefOffsetX;
                  this.getUIContext()?.animateTo({ curve: curves.interpolatingSpring(0, 1, 400, 38) }, () => {
                    let index = this.numbers.indexOf(this.dragItem);
                    if (this.offsetY >= this.FIX_VP_Y / 2 && (this.offsetX <= 44 && this.offsetX >= -44) &&
                      ![8, 9, 10].includes(index)) {
                      //向下滑
                      this.down(index);
                    } else if (this.offsetY <= -this.FIX_VP_Y / 2 && (this.offsetX <= 44 && this.offsetX >= -44) &&
                      ![0, 1, 2].includes(index)) {
                      //向上滑
                      this.up(index);
                    } else if (this.offsetX >= this.FIX_VP_X / 2 && (this.offsetY <= 50 && this.offsetY >= -50) &&
                      ![2, 5, 8, 10].includes(index)) {
                      //向右滑
                      this.right(index);
                    } else if (this.offsetX <= -this.FIX_VP_X / 2 && (this.offsetY <= 50 && this.offsetY >= -50) &&
                      ![0, 3, 6, 9].includes(index)) {
                      //向左滑
                      this.left(index);
                    } else if (this.offsetX >= this.FIX_VP_X / 2 && this.offsetY >= this.FIX_VP_Y / 2 &&
                      ![2, 5, 7, 8, 9, 10].includes(index)) {
                      //向右下滑
                      this.lowerRight(index);
                    } else if (this.offsetX >= this.FIX_VP_X / 2 && this.offsetY <= -this.FIX_VP_Y / 2 &&
                      ![0, 1, 2, 5, 8].includes(index)) {
                      //向右上滑
                      this.upperRight(index);
                    } else if (this.offsetX <= -this.FIX_VP_X / 2 && this.offsetY >= this.FIX_VP_Y / 2 &&
                      ![0, 3, 6, 9, 10].includes(index)) {
                      //向左下滑
                      this.lowerLeft(index);
                    } else if (this.offsetX <= -this.FIX_VP_X / 2 && this.offsetY <= -this.FIX_VP_Y / 2 &&
                      ![0, 1, 2, 3, 6, 9].includes(index)) {
                      //向左上滑
                      this.upperLeft(index);
                    } else if (this.offsetX >= this.FIX_VP_X / 2 && this.offsetY >= this.FIX_VP_Y / 2 &&
                    [7].includes(index)) {
                      //向右下滑(右下角为空)
                      this.down2(index);
                    }
                  })
                .onActionEnd(() => {
                  this.getUIContext()?.animateTo({ curve: curves.interpolatingSpring(0, 1, 400, 38) }, () => {
                    this.dragItem = -1;
                  })
                  this.getUIContext()?.animateTo({
                    curve: curves.interpolatingSpring(14, 1, 170, 17), delay: 150
                  }, () => {
                    this.scaleItem = -1;
                })
            )
              .onCancel(() => {
                this.getUIContext()?.animateTo({ curve: curves.interpolatingSpring(0, 1, 400, 38) }, () => {
                  this.dragItem = -1;
                })
                this.getUIContext()?.animateTo({
                  curve: curves.interpolatingSpring(14, 1, 170, 17)
                }, () => {
                  this.scaleItem = -1;
                })
          )
        }, (item: number) => item.toString())
      }
      .width('90%')
      .editMode(true)
      .scrollBar(BarState.Off)
      .columnsTemplate('1fr 1fr 1fr')
    }.width('100%').height('100%').backgroundColor('#0D182431').padding({ top: 5 })
  }
```

![image](public_sys-resources/zh-cn_image_0000002553364813.webp)

#### 示例17（通过拖拽事件实现[GridItem](GridItem.md)拖拽）

该示例通过[拖拽事件](拖拽事件.md)实现拖拽GridItem到Grid边缘时Grid自动滚动的功能。

GridDataSource说明及完整代码参考[示例2可滚动grid和滚动事件](#ZH-CN_TOPIC_0000002553200787__示例2可滚动grid和滚动事件)。

```ets
// xxx.ets
import { GridDataSource } from './GridDataSource';

@Entry
@Component
struct Example {
  numbers: GridDataSource = new GridDataSource([]);

  aboutToAppear(): void {
    let list: string[] = [];
    for (let index = 0; index < 100; index++) {
      list.push(index.toString());
    }
    this.numbers = new GridDataSource(list);
  }

  changeIndex(index1: number, index2: number) { // 交换数组位置
    console.info(index1 + 'index2:' + index2);
    this.numbers.swapItem(index1, index2);
  }

  build() {
    Column({ space: 5 }) {
      Grid() {
        LazyForEach(this.numbers, (item: number, index: number) => {
          GridItem() {
            Text(item + '')
              .fontSize(16)
              .backgroundColor(0xF9CF93)
              .width(80)
              .height(80)
              .textAlign(TextAlign.Center)
          }
          .width(90)
          .height(90)
          .selectable(true)
          .selected(true)
          .allowDrop([])
          .onDragStart((event: DragEvent) => {
            return { extraInfo: index + '' };
          })
          .onDragEnter((event: DragEvent, extraParams?: string) => {
            console.info(index + '' + extraParams);
          })
          .onDragEnd((event: DragEvent, extraParams?: string) => {
            console.info('onDragEnd' + index + '' + extraParams);
          })
          .onDrop((event?: DragEvent, extraParams?: string) => {
            console.info('drop:' + item + '' + extraParams + JSON.stringify(event!));
            this.changeIndex(parseInt(JSON.parse(extraParams!).extraInfo), index);
          })
        }, (item: string) => item)
      }
      .columnsGap(5)
      .rowsGap(5)
      .columnsTemplate('1fr 1fr 1fr')
      .height(300)
    }
    .width('100%')
  }
```

#### 示例18（[Grid](Grid.md)组件基于断点配置列数）

从API version 22开始，该示例展示了[Grid](Grid.md)组件支持基于断点配置列数效果。

```ets
// Index.ets
// xxx.ets
import { GridDataSource } from './GridDataSource';

@Entry
@Component
struct GridExample {
  numbers: GridDataSource = new GridDataSource([]);

  aboutToAppear() {
    let list: string[] = [];
    for (let i = 0; i < 5; i++) {
      for (let j = 0; j < 5; j++) {
        list.push(j.toString());
    }
    this.numbers = new GridDataSource(list);
  }

  build() {
    Column({ space: 5 }) {
      Grid(undefined) {
        LazyForEach(this.numbers, (day: string) => {
          GridItem() {
            Text(day)
              .fontSize(16)
              .backgroundColor(0xF9CF93)
              .width('100%')
              .height(80)
              .textAlign(TextAlign.Center)
          }
        }, (index: number) => index.toString())
      }
      .columnsTemplate({fillType:PresetFillType.BREAKPOINT_SM2MD3LG5})
      .columnsGap(10)
      .rowsGap(10)
      .scrollBar(BarState.Off)
      .width('100%')
      .backgroundColor(0xFAEEE0)
      .height(300)
    }.width('100%').height('10%').justifyContent(FlexAlign.SpaceBetween)
  }
```

[Grid](Grid.md)宽度属于sm及更小的断点区间时显示2列。

[Grid](Grid.md)宽度属于md断点区间时显示3列。

[Grid](Grid.md)宽度属于lg及更大的断点区间时显示5列。

#### 示例19（获取内容总大小）

从API version 22 开始，该示例实现了获取内容总大小的功能。

GridDataSource说明及完整代码参考[示例2（可滚动Grid和滚动事件）](#ZH-CN_TOPIC_0000002553200787__示例2可滚动grid和滚动事件)。

```ets
import { GridDataSource } from './GridDataSource';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct GridExample {
  numbers: GridDataSource = new GridDataSource([]);
  scroller: Scroller = new Scroller();
  @State contentWidth: number = -1;
  @State contentHeight: number = -1;

  aboutToAppear() {
    let list: string[] = [];
    for (let i = 0; i < 10; i++) {
      for (let j = 0; j < 5; j++) {
        list.push(j.toString());
    }
    this.numbers = new GridDataSource(list);
  }

  build() {
    Column({ space: 5 }) {
      Text('可滚动Grid和LazyForEach')
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

      Grid(this.scroller) {
        LazyForEach(this.numbers, (day: string) => {
          GridItem() {
            Text(day)
              .fontSize(16)
              .backgroundColor(0xF9CF93)
              .width('100%')
              .height(80)
              .textAlign(TextAlign.Center)
          }
          .margin(20)
        }, (index: number) => index.toString())
      }
      .columnsTemplate('1fr 1fr 1fr 1fr 1fr')
      .columnsGap(10)
      .rowsGap(10)
      .friction(0.6)
      .enableScrollInteraction(true)
      .supportAnimation(false)
      .multiSelectable(false)
      .edgeEffect(EdgeEffect.Spring)
      .scrollBar(BarState.On)
      .scrollBarColor(Color.Grey)
      .scrollBarWidth(4)
      .width('90%')
      .backgroundColor(0xFAEEE0)
      .height(300)
    }.width('100%').margin({ top: 5 })
  }
```

![image](public_sys-resources/zh-cn_image_0000002522244894.webp)

**示例20（设置多选聚拢动画）**

该示例通过打开Grid多选聚拢动画开关，实现了在GridItem上[长按弹出菜单](菜单控制.md#ZH-CN_TOPIC_0000002522080798__bindcontextmenu8)时聚拢显示范围内被选中的GridItem。

从API version 23开始，Grid组件新增[编辑模式选项](#ZH-CN_TOPIC_0000002553200787__editmodeoptions23)接口，可以设置多选聚拢动画开关。

GridDataSource说明及完整代码参考[示例2（可滚动Grid和滚动事件）](#ZH-CN_TOPIC_0000002553200787__示例2可滚动grid和滚动事件)。

```ets
// xxx.ets
import { GridDataSource } from './GridDataSource';

@Entry
@Component
struct GridExample {
  numbers: GridDataSource = new GridDataSource(['1', '2', '3', '4', '5', '6', '7', '8', '9']);
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
    for (i = 0; i < 9; i++) {
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
      Text('Grid')
      Grid() {
        LazyForEach(this.numbers, (day: string, index: number) => {
          GridItem() {
            Text(day)
              .fontSize(16)
              .backgroundColor(0xF9CF93)
              .width('100%')
              .height('100%')
              .textAlign(TextAlign.Center)
          }
          .selected(this.isSelected[index])
          // 设置多选显示效果
          .stateStyles({
            normal: this.normalStyles,
            selected: this.selectStyles
          })
          .bindContextMenu(this.MenuBuilder, ResponseType.LongPress,
            { preview: MenuPreviewMode.IMAGE, hapticFeedbackMode: HapticFeedbackMode.ENABLED })
          .onClick(() => {
            this.isSelected[index] = !this.isSelected[index];
            console.info(`item:${index}, this.isSelected[item]:${this.isSelected[index]}`)
            if (this.isSelected[index]) {
              ++this.selectedCount;
            } else {
              --this.selectedCount;
            }
          })
        }, (day: string) => day)
      }
      .editModeOptions({
        enableGatherSelectedItemsAnimation: true, onGetPreviewBadge: () => {
          return this.selectedCount;
        }
      })
      .columnsTemplate('1fr 1fr 1fr')
      .rowsTemplate('1fr 1fr 1fr')
      .columnsGap(10)
      .rowsGap(10)
      .width('90%')
      .backgroundColor(0xFAEEE0)
      .height(300)
    }.width('100%').margin({ top: 5 })
  }
```

![image](public_sys-resources/zh-cn_image_0000002553204855.webp)
