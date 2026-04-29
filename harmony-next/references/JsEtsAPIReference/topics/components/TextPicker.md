# [Text](Text.md)Picker

滑动选择文本、图片或图文混排内容的组件，用户可以按需创建单列数据选择器、多列非联动数据选择器和多列联动数据选择器。

-

该组件从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

-

该组件不建议开发者在动效过程中修改属性数据。

-

最大显示行数在横、竖屏模式下存在差异。竖屏时默认为5行，横屏时依赖系统配置，未配置时默认显示为3行。可通过如下参数查看具体配置值$r('sys.float.ohos_id_picker_show_count_landscape')。

-

多列非联动数据选择器和多列联动数据选择器在下文中统称为多列数据选择器。

#### 子组件

无

#### 接口

[Text](Text.md)Picker(options?: TextPickerOptions)

根据指定的数据列表创建文本选择器。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [Text](Text.md)PickerOptions | 否 | 配置文本选择器的参数。 |

#### [Text](Text.md)PickerOptions对象说明

文本选择器的参数说明。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| range | string[] | string[][]10+ | [Resource](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resource) | TextPickerRangeContent[]10+ | TextCascadePickerRangeContent[]10+ | 否 | 否 | 选择器的数据选择列表。不可设置为空数组，若设置为空数组，则不显示；若动态变化为空数组，则保持当前正常值显示。 说明： 1. 单列数据选择器使用string[]，Resource，TextPickerRangeContent[]类型。 2. 多列非联动数据选择器使用string[][]类型。 3. 多列联动数据选择器使用TextCascadePickerRangeContent[]类型。 4. Resource类型只支持strarray.json。 5. range的类型及列数不可以动态修改。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| selected | number | number[]10+ | 否 | 是 | 设置选中项在数据选择列表中的索引值，索引从0开始。 默认值：0 说明： 1. 单列数据选择器使用number类型。 2. 多列数据选择器使用number[]类型。 3. 从API version 10开始，该参数支持$$双向绑定变量。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| value | [ResourceStr](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcestr) | ResourceStr[] | 否 | 是 | 设置选中项的值，优先级低于selected。 默认值：数据选择列表中第一个元素的值。 说明： 1. 从API version 10开始，该参数支持$$双向绑定变量。 2. 从API version 20开始，支持Resource类型。 3. 只有显示文本列表时该值有效。显示图片或图文混排的列表时，该值无效。 4. 单列数据选择器使用ResourceStr类型。 5. 多列数据选择器使用ResourceStr[]类型。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| columnWidths18+ | [LengthMetrics](../misc/Graphics.md#ZH-CN_TOPIC_0000002529444761__lengthmetrics12)[] | 否 | 是 | 设置每一列的列宽。 默认值：每一列的列宽相等，为组件宽度除以列数。 说明： 1. 当文本长度大于列宽时，文本被截断。 2. 当设置为异常值时，使用默认值。 3. 支持设置为Undefined和Null，不支持Undefined[]和Null[]。 元服务API： 从API version 18开始，该接口支持在元服务中使用。 |

#### [Text](Text.md)PickerRangeContent10+对象说明

单列数据选择器的数据选项内容。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| icon | string | [Resource](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resource) | 否 | 否 | 图片资源。 icon是string类型时，表示图片存放的路径，例如"/common/hello.png"。 |
| text | string | [Resource](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resource) | 否 | 是 | 文本信息。 默认值：空字符串 说明：当文本长度大于列宽时，文本被截断。 |

#### [Text](Text.md)CascadePickerRangeContent10+对象说明

多列联动数据选择器的数据选项内容。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| text | string | [Resource](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resource) | 否 | 否 | 文本信息。 说明：当文本长度大于列宽时，文本被截断。 |
| children | [Text](Text.md)CascadePickerRangeContent[] | 否 | 是 | 联动数据。 |

#### DividerOptions12+对象说明

分割线的信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| strokeWidth | [Dimension](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__dimension10) | 否 | 是 | 分割线的线宽。 默认值：2.0px 单位：默认为vp，也可指定单位为px。 取值范围：strokeWidth小于0取默认值，最大不得超过列高的一半。不支持“百分比”类型。 |
| startMargin | [Dimension](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__dimension10) | 否 | 是 | 分割线与TextPicker侧边起始端的距离。 默认值：0 单位：默认为vp，也可指定单位为px。 取值范围：startMargin小于0时无效，最大值不得超过TextPicker列宽。不支持“百分比”类型。 |
| endMargin | [Dimension](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__dimension10) | 否 | 是 | 分割线与TextPicker侧边结束端的距离。 默认值：0 单位：默认为vp，也可指定单位为px。 取值范围：endMargin小于0时无效，最大值不得超过TextPicker列宽。不支持“百分比”类型。 |
| color | [ResourceColor](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor) | 否 | 是 | 分割线的颜色。 默认值：'#33000000' |

#### 属性

除支持[通用属性]([通用属性](../misc/通用属性.md).md)外，还支持以下属性：

#### defaultPickerItemHeight

defaultPickerItemHeight(value: number | string)

设置选择项的高度。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | string | 是 | 选择项的高度。 取值范围： number类型：[0, +∞)，单位为vp。 string类型：仅支持number类型取值的字符串形式，例如"56"。 默认值：选中项56vp，非选中项36vp。 说明： 设置该参数后，选中项与非选中项的高度均为所设置的值。 |

#### defaultPickerItemHeight18+

defaultPickerItemHeight(height: [Optional](自定义属性设置.md#ZH-CN_TOPIC_0000002529284845__optionalt12)<number | string>)

设置选择项的高度。与[defaultPickerItemHeight](#ZH-CN_TOPIC_0000002553200801__defaultpickeritemheight)相比，height参数新增了对undefined类型的支持。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| height | [Optional](自定义属性设置.md#ZH-CN_TOPIC_0000002529284845__optionalt12)<number | string> | 是 | 选择项的高度。 取值范围： number类型：[0, +∞)，单位为vp。 string类型：仅支持number类型取值的字符串形式，例如"56"。 默认值：选中项56vp，非选中项36vp。 说明： 1. 设置该参数后，选中项与非选中项的高度均为所设置的值。 2. 当height的值为undefined时，维持上次取值。 |

#### disappear[Text](Text.md)Style10+

disappearTextStyle(value: [PickerTextStyle](选择器（Picker）公共接口.md#ZH-CN_TOPIC_0000002529444857__pickertextstyle对象说明))

设置边缘项（以选中项为基准向上或向下的第二项）的文本颜色、字号、字体粗细。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [PickerTextStyle](选择器（Picker）公共接口.md#ZH-CN_TOPIC_0000002529444857__pickertextstyle对象说明) | 是 | 边缘项的文本颜色、字号、字体粗细。 默认值： { color: '#ff182431', font: { size: '14fp', weight: FontWeight.Regular } } |


若选中项向上或向下的可视项数低于两项则无对应边缘项。

#### disappear[Text](Text.md)Style18+

disappearTextStyle(style: [Optional](自定义属性设置.md#ZH-CN_TOPIC_0000002529284845__optionalt12)<PickerTextStyle>)

设置边缘项（以选中项为基准向上或向下的第二项）的文本颜色、字号、字体粗细。与[disappearTextStyle10+](#ZH-CN_TOPIC_0000002553200801__disappeartextstyle10)相比，style参数新增了对undefined类型的支持。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| style | [Optional](自定义属性设置.md#ZH-CN_TOPIC_0000002529284845__optionalt12)<[PickerTextStyle](选择器（Picker）公共接口.md#ZH-CN_TOPIC_0000002529444857__pickertextstyle对象说明)> | 是 | 边缘项的文本颜色、字号、字体粗细。 默认值： { color: '#ff182431', font: { size: '14fp', weight: FontWeight.Regular } } 当style的值为undefined时，使用默认值。 |


若选中项向上或向下的可视项数低于两项则无对应边缘项。

#### disappear[Text](Text.md)Style20+

disappearTextStyle(style: [Optional](自定义属性设置.md#ZH-CN_TOPIC_0000002529284845__optionalt12)<PickerTextStyle|TextPickerTextStyle>)

设置边缘项（以选中项为基准向上或向下的第二项）的文本颜色、字号、字体粗细、最大字号、最小字号、超长文本截断方式。与[disappearTextStyle](#ZH-CN_TOPIC_0000002553200801__disappeartextstyle18)18+相比，style参数新增了对[TextPickerTextStyle](#ZH-CN_TOPIC_0000002553200801__textpickertextstyle15类型说明)类型的支持。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| style | [Optional](自定义属性设置.md#ZH-CN_TOPIC_0000002529284845__optionalt12)<[PickerTextStyle](选择器（Picker）公共接口.md#ZH-CN_TOPIC_0000002529444857__pickertextstyle对象说明)|TextPickerTextStyle> | 是 | 边缘项的文本颜色、字号、字体粗细、最大字号、最小字号、超长文本截断方式。 默认值： { color: '#ff182431', font: { size: '14fp', weight: FontWeight.Regular }, minFontSize: 0, maxFontSize: 0, overflow: TextOverflow.Clip } 当style的值为undefined时，使用默认值。 |


若选中项向上或向下的可视项数低于两项则无对应边缘项。

#### textStyle10+

textStyle(value: [PickerTextStyle](选择器（Picker）公共接口.md#ZH-CN_TOPIC_0000002529444857__pickertextstyle对象说明))

设置待选项（以选中项为基准向上或向下的第一项）的文本颜色、字号、字体粗细。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [PickerTextStyle](选择器（Picker）公共接口.md#ZH-CN_TOPIC_0000002529444857__pickertextstyle对象说明) | 是 | 待选项的文本颜色、字号、字体粗细。 默认值： { color: '#ff182431', font: { size: '16fp', weight: FontWeight.Regular } } |


若选中项向上或向下可视项数低于一项则无对应待选项。

#### textStyle18+

textStyle(style: [Optional](自定义属性设置.md#ZH-CN_TOPIC_0000002529284845__optionalt12)<PickerTextStyle>)

设置待选项（以选中项为基准向上或向下的第一项）的文本颜色、字号、字体粗细。与[textStyle10+](#ZH-CN_TOPIC_0000002553200801__textstyle10)相比，style参数新增了对undefined类型的支持。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| style | [Optional](自定义属性设置.md#ZH-CN_TOPIC_0000002529284845__optionalt12)<[PickerTextStyle](选择器（Picker）公共接口.md#ZH-CN_TOPIC_0000002529444857__pickertextstyle对象说明)> | 是 | 待选项的文本颜色、字号、字体粗细。 默认值： { color: '#ff182431', font: { size: '16fp', weight: FontWeight.Regular } } 当style的值为undefined时，使用默认值。 |


若选中项向上或向下可视项数低于一项则无对应待选项。

#### textStyle20+

textStyle(style: [Optional](自定义属性设置.md#ZH-CN_TOPIC_0000002529284845__optionalt12)<PickerTextStyle|TextPickerTextStyle>)

设置待选项（以选中项为基准向上或向下的第一项）的文本颜色、字号、字体粗细、最大字号、最小字号、超长文本截断方式。与[textStyle](#ZH-CN_TOPIC_0000002553200801__textstyle18)18+相比，style参数新增了对[TextPickerTextStyle](#ZH-CN_TOPIC_0000002553200801__textpickertextstyle15类型说明)类型的支持。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| style | [Optional](自定义属性设置.md#ZH-CN_TOPIC_0000002529284845__optionalt12)<[PickerTextStyle](选择器（Picker）公共接口.md#ZH-CN_TOPIC_0000002529444857__pickertextstyle对象说明)|TextPickerTextStyle> | 是 | 待选项的文本颜色、字号、字体粗细、最大字号、最小字号、超长文本截断方式。 默认值： { color: '#ff182431', font: { size: '16fp', weight: FontWeight.Regular }, minFontSize: 0, maxFontSize: 0, overflow: TextOverflow.Clip } 当style的值为undefined时，使用默认值。 |


若选中项向上或向下可视项数低于一项则无对应待选项。

#### selected[Text](Text.md)Style10+

selectedTextStyle(value: [PickerTextStyle](选择器（Picker）公共接口.md#ZH-CN_TOPIC_0000002529444857__pickertextstyle对象说明))

设置选中项的文本颜色、字号、字体粗细。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该属性在Wearable设备上使用无效果，在其他设备中可正常生效。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [PickerTextStyle](选择器（Picker）公共接口.md#ZH-CN_TOPIC_0000002529444857__pickertextstyle对象说明) | 是 | 选中项的文本颜色、字号、字体粗细。 默认值： { color: '#ff007dff', font: { size: '20fp', weight: FontWeight.Medium } } |

#### selected[Text](Text.md)Style18+

selectedTextStyle(style: [Optional](自定义属性设置.md#ZH-CN_TOPIC_0000002529284845__optionalt12)<PickerTextStyle>)

设置选中项的文本颜色、字号、字体粗细。与[selectedTextStyle10+](#ZH-CN_TOPIC_0000002553200801__selectedtextstyle10)相比，style参数新增了对undefined类型的支持。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该属性在Wearable设备上使用无效果，在其他设备中可正常生效。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| style | [Optional](自定义属性设置.md#ZH-CN_TOPIC_0000002529284845__optionalt12)<[PickerTextStyle](选择器（Picker）公共接口.md#ZH-CN_TOPIC_0000002529444857__pickertextstyle对象说明)> | 是 | 选中项的文本颜色、字号、字体粗细。 默认值： { color: '#ff007dff', font: { size: '20fp', weight: FontWeight.Medium } } 当style的值为undefined时，使用默认值。 |

#### selected[Text](Text.md)Style20+

selectedTextStyle(style: [Optional](自定义属性设置.md#ZH-CN_TOPIC_0000002529284845__optionalt12)<PickerTextStyle|TextPickerTextStyle>)

设置选中项的文本颜色、字号、字体粗细、最大字号、最小字号、超长文本截断方式。与[selectedTextStyle](#ZH-CN_TOPIC_0000002553200801__selectedtextstyle18)18+相比，style参数新增了对[TextPickerTextStyle](#ZH-CN_TOPIC_0000002553200801__textpickertextstyle15类型说明)类型的支持。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该属性在Wearable设备上使用无效果，在其他设备中可正常生效。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| style | [Optional](自定义属性设置.md#ZH-CN_TOPIC_0000002529284845__optionalt12)<[PickerTextStyle](选择器（Picker）公共接口.md#ZH-CN_TOPIC_0000002529444857__pickertextstyle对象说明)|TextPickerTextStyle> | 是 | 选中项的文本颜色、字号、字体粗细、最大字号、最小字号、超长文本截断方式。 默认值： { color: '#ff007dff', font: { size: '20fp', weight: FontWeight.Medium }, minFontSize: 0, maxFontSize: 0, overflow: TextOverflow.Clip } 当style的值为undefined时，使用默认值。 |

#### selectedIndex10+

selectedIndex(value: number | number[])

设置选中项在数据选择列表中的索引值，优先级高于[TextPickerOptions](#ZH-CN_TOPIC_0000002553200801__textpickeroptions对象说明)中的"value"属性。单列数据选择器使用number类型。多列数据选择器使用number[]类型。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | number[] | 是 | 选中项在数据选择列表中的索引值，索引从0开始。 默认值：0 当value的值为负数或者超过数据选择列表的最大索引值时，使用默认值。 |

#### selectedIndex18+

selectedIndex(index: [Optional](自定义属性设置.md#ZH-CN_TOPIC_0000002529284845__optionalt12)<number | number[]>)

设置选中项在数据选择列表中的索引值，优先级高于[TextPickerOptions](#ZH-CN_TOPIC_0000002553200801__textpickeroptions对象说明)中的"value"属性。单列数据选择器使用number类型，多列数据选择器使用number[]类型。与[selectedIndex10+](#ZH-CN_TOPIC_0000002553200801__selectedindex10)相比，index参数新增了对undefined类型的支持。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | [Optional](自定义属性设置.md#ZH-CN_TOPIC_0000002529284845__optionalt12)<number | number[]> | 是 | 选中项在数据选择列表中的索引值，索引从0开始。 默认值：0 当index的值为undefined时，使用TextPickerOptions中的selected值。 当index的值为负数或者超过数据选择列表的最大索引值时，使用默认值。 |

#### canLoop10+

canLoop(value: boolean)

设置是否可循环滚动。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 是否可循环滚动。 - true：可循环。 - false：不可循环。 默认值：true |

#### canLoop18+

canLoop(isLoop: [Optional](自定义属性设置.md#ZH-CN_TOPIC_0000002529284845__optionalt12)<boolean>)

设置是否可循环滚动。与[canLoop10+](#ZH-CN_TOPIC_0000002553200801__canloop10)相比，isLoop参数新增了对undefined类型的支持。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isLoop | [Optional](自定义属性设置.md#ZH-CN_TOPIC_0000002529284845__optionalt12)<boolean> | 是 | 是否可循环滚动。 - true：可循环。 - false：不可循环。 默认值：true 当isLoop的值为undefined时，使用默认值。 |

#### divider12+

divider(value: DividerOptions | null)

设置分割线样式，不设置该属性则按“默认值”展示分割线。

[DividerOptions](#ZH-CN_TOPIC_0000002553200801__divideroptions12对象说明)中startMargin + endMargin 超过组件宽度后，startMargin和endMargin会被置0。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | DividerOptions | null | 是 | 默认值： { strokeWidth: '2px', startMargin: 0, endMargin: 0, color: '#33000000' } 1. 当textDivider设置为有效的DividerOptions时，按设置的样式显示分割线。 2. 当textDivider设置为null时，不显示分割线。 |

#### divider18+

divider(textDivider: [Optional](自定义属性设置.md#ZH-CN_TOPIC_0000002529284845__optionalt12)<DividerOptions | null>)

设置分割线样式，不设置该属性则按“默认值”展示分割线。与[divider12+](#ZH-CN_TOPIC_0000002553200801__divider12)相比，textDivider参数新增了对undefined类型的支持。

[DividerOptions](#ZH-CN_TOPIC_0000002553200801__divideroptions12对象说明)中startMargin + endMargin 超过组件宽度后，startMargin和endMargin会被置0。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| textDivider | [Optional](自定义属性设置.md#ZH-CN_TOPIC_0000002529284845__optionalt12)<DividerOptions | null> | 是 | 默认值： { strokeWidth: '2px', startMargin: 0, endMargin: 0, color: '#33000000' } 1. 当textDivider的值为undefined时，使用默认值。 2. 当textDivider设置为有效的DividerOptions时，按设置的样式显示分割线。 3. 当textDivider设置为null时，不显示分割线。 |

#### gradientHeight12+

gradientHeight(value: [Dimension](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__dimension10))

设置渐隐效果的高度。若未设置该属性，则显示默认渐隐效果。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Dimension](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__dimension10) | 是 | 内容区上下边缘的渐隐高度。 默认值：36vp 取值范围：[0, +∞)，支持百分比。 说明： 1. value设置为百分比时，100%为TextPicker高度的一半。 2. value设置为0时不显示渐隐效果。 3. value设置为数字且超过TextPicker高度的一半时，使用默认值。 4. 当value的值为负数时，使用默认值。 |

#### gradientHeight18+

gradientHeight(height: Optional<[Dimension](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__dimension10)>)

设置渐隐效果的高度。若未设置该属性，则显示默认渐隐效果。与[gradientHeight12+](#ZH-CN_TOPIC_0000002553200801__gradientheight12)相比，height参数新增了对undefined类型的支持。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| height | [Optional](自定义属性设置.md#ZH-CN_TOPIC_0000002529284845__optionalt12)<[Dimension](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__dimension10)> | 是 | 内容区上下边缘的渐隐高度。 默认值：36vp 取值范围：[0, +∞)，支持百分比。 说明： 1. height设置为百分比时，100%为TextPicker高度的一半。 2. height设置为0时不显示渐隐效果。 3. height设置为数字且超过TextPicker高度的一半时，使用默认值。 4. 当height的值为undefined或负数时，使用默认值。 |

#### disable[Text](Text.md)StyleAnimation15+

disable[Text](Text.md)StyleAnimation(disabled: boolean)

设置是否关闭滑动过程中文本样式变化的动效。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| disabled | boolean | 是 | 是否关闭滑动过程中文本样式变化的动效。 - true：关闭文本样式变化动效。 - false：不关闭文本样式变化动效。 默认值：false 说明： 设置为true时，滑动过程中无字号、字重、字体颜色等变化动效，且文本均显示为default[Text](Text.md)Style属性设置的样式。如未设置defaultTextStyle，则显示为Text组件默认样式。 |

#### default[Text](Text.md)Style15+

defaultTextStyle(style: Text[PickerTextStyle](选择器（Picker）公共接口.md#ZH-CN_TOPIC_0000002529444857__pickertextstyle对象说明))

设置关闭滑动过程中文本样式变化的动效时，各个选项的文本样式。仅当[disableTextStyleAnimation](#ZH-CN_TOPIC_0000002553200801__disabletextstyleanimation15)为true时生效。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| style | [Text](Text.md)PickerTextStyle | 是 | 设置关闭滑动过程中文本样式变化的动效时，各个选项的文本样式。 默认值：与Text组件默认值相同。 |

开启触控反馈时，需要在工程的src/main/module.json5文件的"module"内配置requestPermissions字段开启振动权限，配置如下：

```ets
"requestPermissions": [
   {
      "name": "ohos.permission.VIBRATE",
   }
]
```

#### enableHapticFeedback18+

enableHapticFeedback(enable: [Optional](自定义属性设置.md#ZH-CN_TOPIC_0000002529284845__optionalt12)<boolean>)

设置是否开启触控反馈。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | [Optional](自定义属性设置.md#ZH-CN_TOPIC_0000002529284845__optionalt12)<boolean> | 是 | 设置是否开启触控反馈。 - true：开启触控反馈。 - false：不开启触控反馈。 默认值：true 设置为true后，其生效情况取决于系统的硬件是否支持。 |

开启触控反馈时，需要在工程的src/main/module.json5文件的"module"内配置requestPermissions字段开启振动权限，配置如下：

```ets
"requestPermissions": [
   {
      "name": "ohos.permission.VIBRATE",
   }
]
```

#### digital[CrownSensitivity](枚举说明.md#ZH-CN_TOPIC_0000002529284967__crownsensitivity18)18+

digitalCrownSensitivity(sensitivity: [Optional](自定义属性设置.md#ZH-CN_TOPIC_0000002529284845__optionalt12)<CrownSensitivity>)

设置表冠灵敏度。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sensitivity | [Optional](自定义属性设置.md#ZH-CN_TOPIC_0000002529284845__optionalt12)<[CrownSensitivity](枚举说明.md#ZH-CN_TOPIC_0000002529284967__crownsensitivity18)> | 是 | 表冠响应灵敏度。 默认值：CrownSensitivity.MEDIUM，响应速度适中。 |


用于圆形屏幕的穿戴设备。组件响应[表冠事件](表冠事件.md)，需要先获取焦点。

#### selectedBackgroundStyle20+

selectedBackgroundStyle(style: [Optional](自定义属性设置.md#ZH-CN_TOPIC_0000002529284845__optionalt12)<PickerBackgroundStyle>)

设置选中项的背景样式。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| style | [Optional](自定义属性设置.md#ZH-CN_TOPIC_0000002529284845__optionalt12)<PickerBackgroundStyle> | 是 | 选中项背景的颜色和边框圆角半径，多列模式时会同时设置所有列的选中项背景的颜色和圆角半径。 默认值： { color: $r('sys.color.comp_background_tertiary'), borderRadius: $r('sys.float.corner_radius_level12') } |

#### 事件

除支持[通用事件]([通用事件](../misc/通用事件.md).md)外，还支持以下事件：

#### onChange

onChange(callback: (value: string | string[], index: number | number[]) => void)

滑动[Text](Text.md)Picker文本内容后，选项归位至选中项位置时，触发该回调。不能通过双向绑定的状态变量触发。当显示文本或图片加文本列表时，value值为选中项中的文本值，当显示图片列表时，value值为空。

回调会在滑动动画结束后触发，如果需要快速获取索引值变化，建议使用[onEnterSelectedArea](#ZH-CN_TOPIC_0000002553200801__onenterselectedarea18)接口。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string | string[]10+ | 是 | 当前选中项的文本。多列数据选择器的value为数组类型。 |
| index | number | number[]10+ | 是 | 当前选中项的索引值，索引从0开始。多列数据选择器的index为数组类型。 |

#### onChange18+

onChange(callback: [Optional](自定义属性设置.md#ZH-CN_TOPIC_0000002529284845__optionalt12)<OnTextPickerChangeCallback>)

滑动TextPicker文本内容后，选项归位至选中项位置时，触发该回调。不能通过双向绑定的状态变量触发。当显示文本或图片加文本列表时，value值为选中项中的文本值，当显示图片列表时，value值为空。与[onChange](#ZH-CN_TOPIC_0000002553200801__onchange)相比，callback参数新增了对undefined类型的支持。

回调会在滑动动画结束后触发，如果需要快速获取索引值变化，建议使用[onEnterSelectedArea](#ZH-CN_TOPIC_0000002553200801__onenterselectedarea18)接口。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Optional](自定义属性设置.md#ZH-CN_TOPIC_0000002529284845__optionalt12)<OnTextPickerChangeCallback> | 是 | 滑动选中TextPicker文本内容后，触发的回调。 当callback的值为undefined时，不使用回调函数。 |

#### onScrollStop14+

onScrollStop(callback: [Text](Text.md)PickerScrollStopCallback)

文本选择器的选项列滑动停止时触发该事件。

手指拖动选项列触发的滑动，手指离开屏幕且滑动停止时会触发该事件。


从API version 20开始，该接口支持在[attributeModifier](动态属性设置.md#ZH-CN_TOPIC_0000002522240800__attributemodifier)中调用。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Text](Text.md)PickerScrollStopCallback | 是 | 文本选择器的选项列滑动停止时触发该事件。 |

#### onScrollStop18+

onScrollStop(callback: [Optional](自定义属性设置.md#ZH-CN_TOPIC_0000002529284845__optionalt12)<TextPickerScrollStopCallback>)

文本选择器的选项列滑动停止时触发该事件。与[onScrollStop14+](#ZH-CN_TOPIC_0000002553200801__onscrollstop14)相比，callback参数新增了对undefined类型的支持。

手指拖动选项列触发的滑动，手指离开屏幕且滑动停止时会触发该事件。


从API version 20开始，该接口支持在[attributeModifier](动态属性设置.md#ZH-CN_TOPIC_0000002522240800__attributemodifier)中调用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Optional](自定义属性设置.md#ZH-CN_TOPIC_0000002529284845__optionalt12)<TextPickerScrollStopCallback> | 是 | 文本选择器的选项列滑动停止时触发该事件。 当callback的值为undefined时，不使用回调函数。 |

#### onEnterSelectedArea18+

onEnterSelectedArea(callback: [Text](Text.md)PickerEnterSelectedAreaCallback)

滑动[Text](Text.md)Picker过程中，选项进入分割线区域内（当前列的滑动距离超过选中项高度的一半）时，触发该回调。

-

与[onChange](#ZH-CN_TOPIC_0000002553200801__onchange)事件的差别在于，该事件的触发时机早于[onChange](#ZH-CN_TOPIC_0000002553200801__onchange)事件。

-

在多列联动场景中，不建议使用该回调，由于该回调标识的是滑动过程中选项进入分割线区域内的节点，而跟随变化的选项并不涉及滑动，因此，回调的返回值中，仅当前滑动列的值会正常变化，其余未滑动列的值保持不变。

-

该接口不支持在[attributeModifier](动态属性设置.md#ZH-CN_TOPIC_0000002522240800__attributemodifier)中调用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Text](Text.md)PickerEnterSelectedAreaCallback | 是 | 滑动TextPicker过程中，选项进入分割线区域时触发的回调。 |

#### onAccept(deprecated)

onAccept(callback: (value: string, index: number) => void)

点击弹窗中的“确定”按钮时触发该回调。该事件仅在[文本滑动选择器弹窗](文本滑动选择器弹窗 (TextPickerDialog).md)中生效。

从API version 8开始支持，从API version 10开始废弃，无替代接口。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string | 是 | 当前选中项的文本。 |
| index | number | 是 | 当前选中项的索引值，索引从0开始。 |

#### onCancel(deprecated)

onCancel(callback: () => void)

点击弹窗中的“取消”按钮时触发该回调。该事件仅在[文本滑动选择器弹窗](文本滑动选择器弹窗 (TextPickerDialog).md)中生效。

从API version 8开始支持，从API version 10开始废弃，无替代接口。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | () => void | 是 | 点击弹窗中的“取消”按钮时触发该回调。 |

#### Text[PickerTextStyle](选择器（Picker）公共接口.md#ZH-CN_TOPIC_0000002529444857__pickertextstyle对象说明)15+类型说明

文本样式选项，继承自[PickerTextStyle](选择器（Picker）公共接口.md#ZH-CN_TOPIC_0000002553200805__pickertextstyle对象说明)。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| [minFontSize](Text.md#ZH-CN_TOPIC_0000002497444914__minfontsize) | number | string | [Resource](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resource) | 否 | 是 | 文本最小显示字号，与[maxFontSize](Text.md#ZH-CN_TOPIC_0000002497444914__maxfontsize)配合使用。当设置minFontSize和maxFontSize时，font中的size将不生效。默认最大行数为1，自适应高度方式为MIN_FONT_SIZE_FIRST。详细规则请参考Text组件的minFontSize属性。 |
| maxFontSize | number | string | [Resource](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resource) | 否 | 是 | 文本最大显示字号。详细规则请参考Text组件的maxFontSize属性。 |
| overflow | [TextOverflow](枚举说明.md#ZH-CN_TOPIC_0000002529284967__textoverflow) | 否 | 是 | 文本截断方式。当设置为MARQUEE时，该属性不生效。详细规则请参考Text组件的[textOverflow](Text.md#ZH-CN_TOPIC_0000002497444914__textoverflow)属性。 |

#### On[Text](Text.md)PickerChangeCallback18+

type On[Text](Text.md)PickerChangeCallback = (selectItem: string | string[], index: number | number[]) => void

定义触发onChange事件的回调类型。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| selectItem | string | string[]10+ | 是 | 当前选中项的文本。多列数据选择器的selectItem为数组类型。 说明： 当选择器内容为文本或图文混排时，selectItem值为选中项中的文本值；当选择器内容为图片时，selectItem值为空。 |
indexnumber | number[]10+是当前选中项的索引值，索引从0开始。多列数据选择器的index为数组类型。

#### [Text](Text.md)PickerScrollStopCallback14+

type [Text](Text.md)PickerScrollStopCallback = (value: string | string[], index: number | number[]) => void

定义触发onScrollStop事件的回调类型。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string | string[] | 是 | 当前选中项的文本。多列数据选择器的value为数组类型。 说明： 当选择器内容为文本或图文混排时，value值为选中项中的文本值；当选择器内容为图片时，value值为空。 |
indexnumber | number[]是当前选中项的索引值，索引从0开始。多列数据选择器的index为数组类型。

#### [Text](Text.md)PickerEnterSelectedAreaCallback18+

type [Text](Text.md)PickerEnterSelectedAreaCallback = (value: string | string[], index: number | number[]) => void

定义触发onEnterSelectedArea事件的回调类型。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string | string[] | 是 | 当前选中项的文本。多列数据选择器的value为数组类型。 说明： 当选择器内容为文本或图文混排时，value值为选中项中的文本值；当选择器内容为图片时，value值为空。 |
indexnumber | number[]是当前选中项的索引值，索引从0开始。多列数据选择器的index为数组类型。

#### PickerBackgroundStyle20+

选择器选中项的背景样式，包括选中项的背景颜色和边框圆角半径。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| color | [ResourceColor](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor) | 否 | 是 | 选中项的背景颜色。 默认值： 'sys.color.comp_background_tertiary' |
| borderRadius | [LengthMetrics](../misc/Graphics.md#ZH-CN_TOPIC_0000002529444761__lengthmetrics12) | [BorderRadiuses](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__borderradiuses9) | [LocalizedBorderRadiuses](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__localizedborderradiuses12) | 否 | 是 | 选中项的边框圆角半径。 默认值：{ value:24, unit:LengthUnit.VP }，即四个圆角半径均为24VP。 说明： 1. LengthMetrics类型的value参数同时作用于四个圆角半径大小，unit参数用于设置单位。 2. BorderRadiuses类型可以设置四个不同值的圆角半径，所有单位固定为VP。 3. LocalizedBorderRadiuses类型可以设置四个不同值的圆角半径，并且可以单独设置每个圆角的单位。 |

#### 示例

#### 示例1（设置选择器列数）

该示例通过配置range实现单列数据选择器和多列数据选择器，并使用columnWidths调整每一列的宽度。

从API version 18开始，新增了[TextPickerOptions](#ZH-CN_TOPIC_0000002553200801__textpickeroptions对象说明)的columnWidths属性。

```ets
// xxx.ets
import { LengthMetrics } from '@kit.ArkUI';

class Bottom {
  bottom: number = 50;
}

let bott: Bottom = new Bottom();
@Entry
@Component
struct TextPickerExample {
  private select: number = 1;
  private apfruits: string[] = ['apple1', 'apple2', 'apple3', 'apple4'];
  private orfruits: string[] = ['orange1', 'orange2', 'orange3', 'orange4'];
  private pefruits: string[] = ['peach1', 'peach2', 'peach3', 'peach4'];
  private multi: string[][] = [this.apfruits, this.orfruits, this.pefruits];
  private cascade: TextCascadePickerRangeContent[] = [
    {
      text: '辽宁省',
      children: [{ text: '沈阳市', children: [{ text: '沈河区' }, { text: '和平区' }, { text: '浑南区' }] },
        { text: '大连市', children: [{ text: '中山区' }, { text: '金州区' }, { text: '长海县' }] }]
    },
    {
      text: '吉林省',
      children: [{ text: '长春市', children: [{ text: '南关区' }, { text: '宽城区' }, { text: '朝阳区' }] },
        { text: '四平市', children: [{ text: '铁西区' }, { text: '铁东区' }, { text: '梨树县' }] }]
    },
    {
      text: '黑龙江省',
      children: [{ text: '哈尔滨市', children: [{ text: '道里区' }, { text: '道外区' }, { text: '南岗区' }] },
        { text: '牡丹江市', children: [{ text: '东安区' }, { text: '西安区' }, { text: '爱民区' }] }]
    }
  ];
  private singleColumnWidths: LengthMetrics[] = [
    LengthMetrics.percent(50)
  ];

  private multipleColumnWidths: LengthMetrics[] = [
    LengthMetrics.vp(100),
    LengthMetrics.vp(200),
    LengthMetrics.vp(100)
  ];

  private cascadeColumnWidths: LengthMetrics[] = [
    LengthMetrics.percent(20),
    LengthMetrics.percent(30),
    LengthMetrics.percent(50)
  ];
  build() {
    Column() {

      TextPicker({ range: this.apfruits, selected: this.select, columnWidths: this.singleColumnWidths })
        .onChange((value: string | string[], index: number | number[]) => {
          console.info('Picker item changed, value: ' + value + ', index: ' + index);
        })
        .onScrollStop((value: string | string[], index: number | number[]) => {
          console.info('Picker scroll stopped, value: ' + value + ', index: ' + index);
        }).margin(bott)
        .onEnterSelectedArea((value: string | string[], index: number | number[]) => {
          console.info('Picker item enter selected area, value: ' + value + ', index: ' + index);
        })

      TextPicker({ range: this.multi, columnWidths: this.multipleColumnWidths })
        .onChange((value: string | string[], index: number | number[]) => {
          console.info('TextPicker 多列:onChange ' + JSON.stringify(value) + ', ' + 'index: ' + JSON.stringify(index));
        })
        .onScrollStop((value: string | string[], index: number | number[]) => {
          console.info('TextPicker 多列:onScrollStop ' + JSON.stringify(value) + ', ' + 'index: ' + JSON.stringify(index));
        }).margin(bott)
        .onEnterSelectedArea((value: string | string[], index: number | number[]) => {
          console.info('TextPicker 多列:onEnterSelectedArea ' + JSON.stringify(value) + ', ' + 'index: ' + JSON.stringify(index));
        })

      TextPicker({ range: this.cascade, columnWidths: this.cascadeColumnWidths })
        .onChange((value: string | string[], index: number | number[]) => {
          console.info('TextPicker 多列联动:onChange ' + JSON.stringify(value) + ', ' + 'index: ' + JSON.stringify(index));
        })
        .onScrollStop((value: string | string[], index: number | number[]) => {
          console.info('TextPicker 多列联动:onScrollStop ' + JSON.stringify(value) + ', ' + 'index: ' + JSON.stringify(index));
        })
        .onEnterSelectedArea((value: string | string[], index: number | number[]) => {
          console.info('TextPicker 多列联动:onEnterSelectedArea ' + JSON.stringify(value) + ', ' + 'index: ' + JSON.stringify(index));
        })
    }
```

![image](public_sys-resources/zh-cn_image_0000002522084980.webp)

#### 示例2（设置文本样式）

该示例使用[disappearTextStyle](#ZH-CN_TOPIC_0000002553200801__disappeartextstyle10)、[textStyle](#ZH-CN_TOPIC_0000002553200801__textstyle10)、[selectedTextStyle](#ZH-CN_TOPIC_0000002553200801__selectedtextstyle10)设置文本选择器中的文本样式。

```ets
// xxx.ets
@Entry
@Component
struct TextPickerExample {
  private select: number = 0;
  private fruits: string[] = ['apple1', 'orange2', 'peach3', 'grape4'];

  build() {
    Column() {
      TextPicker({
        range: this.fruits,
        selected: this.select,
        value: this.fruits[this.select]
      })
        .onChange((value: string | string[], index: number | number[]) => {
          console.info('Picker item changed, value: ' + value + ', index: ' + index);
        })
        .onScrollStop((value: string | string[], index: number | number[]) => {
          console.info('Picker scroll stopped, value: ' + value + ', index: ' + index);
        })
        .disappearTextStyle({ color: Color.Red, font: { size: 15, weight: FontWeight.Lighter } })
        .textStyle({ color: Color.Black, font: { size: 20, weight: FontWeight.Normal } })
        .selectedTextStyle({ color: Color.Blue, font: { size: 30, weight: FontWeight.Bolder } })
        .defaultPickerItemHeight(50)
        .canLoop(false)
        .selectedIndex(2)
    }.width('100%').height('100%')
  }
```

![image](public_sys-resources/zh-cn_image_0000002553364895.webp)

#### 示例3（设置无分割线样式）

该示例通过配置[divider](#ZH-CN_TOPIC_0000002553200801__divider12)为null实现无分割线样式的文本选择器。

```ets
// xxx.ets
@Entry
@Component
struct TextPickerExample {
  private select: number = 0;
  private fruits: string[] = ['apple1', 'orange2', 'peach3', 'grape4'];

  build() {
    Column() {
      TextPicker({ range: this.fruits, selected: this.select })
        .onChange((value: string | string[], index: number | number[]) => {
          console.info('Picker item changed, value: ' + value + ', index: ' + index);
        })
        .onScrollStop((value: string | string[], index: number | number[]) => {
          console.info('Picker scroll stopped, value: ' + value + ', index: ' + index);
        })
        .disappearTextStyle({color: Color.Red, font: {size: 15, weight: FontWeight.Lighter}})
        .textStyle({color: Color.Black, font: {size: 20, weight: FontWeight.Normal}})
        .selectedTextStyle({color: Color.Blue, font: {size: 30, weight: FontWeight.Bolder}})
        .divider(null)
    }.width('100%').height('100%')
}
```

#### 示例4（设置分割线样式）

该示例通过配置divider的DividerOptions设置文本选择器的分割线样式。

```ets
// xxx.ets
@Entry
@Component
struct TextPickerExample {
  private select: number = 1;
  private fruits: string[] = ['apple1', 'orange2', 'peach3', 'grape4'];

  build() {
    Column() {
      TextPicker({ range: this.fruits, selected: this.select })
        .onChange((value: string | string[], index: number | number[]) => {
          console.info('Picker item changed, value: ' + value + ', index: ' + index);
        })
        .onScrollStop((value: string | string[], index: number | number[]) => {
          console.info('Picker scroll stopped, value: ' + value + ', index: ' + index);
        })
        .disappearTextStyle({color: Color.Red, font: {size: 15, weight: FontWeight.Lighter}})
        .textStyle({color: Color.Black, font: {size: 20, weight: FontWeight.Normal}})
        .selectedTextStyle({color: Color.Blue, font: {size: 30, weight: FontWeight.Bolder}})
        .divider({
          strokeWidth: 10,
          color: Color.Red,
          startMargin: 10,
          endMargin: 20
        } as DividerOptions)
    }.width('100%').height('100%')
  }
```

![image](public_sys-resources/zh-cn_image_0000002553204935.webp)

#### 示例5（设置渐隐效果）

该示例通过配置[gradientHeight](#ZH-CN_TOPIC_0000002553200801__gradientheight12)设置文本选择器的渐隐效果高度。

```ets
// xxx.ets
@Entry
@Component
struct TextPickerExample {
  private select: number = 1;
  private fruits: string[] = ['apple1', 'orange2', 'peach3', 'grape4'];

  build() {
    Column() {
      TextPicker({ range: this.fruits, selected: this.select })
        .onChange((value: string | string[], index: number | number[]) => {
          console.info('Picker item changed, value: ' + value + ', index: ' + index);
        })
        .onScrollStop((value: string | string[], index: number | number[]) => {
          console.info('Picker scroll stopped, value: ' + value + ', index: ' + index);
        })
        .disappearTextStyle({color: Color.Red, font: {size: 15, weight: FontWeight.Lighter}})
        .textStyle({color: Color.Black, font: {size: 20, weight: FontWeight.Normal}})
        .selectedTextStyle({color: Color.Blue, font: {size: 30, weight: FontWeight.Bolder}})
        .gradientHeight(100)
    }.width('100%').height('100%')
  }
```

![image](public_sys-resources/zh-cn_image_0000002522084982.webp)

#### 示例6（设置选择项高度）

该示例通过配置[defaultPickerItemHeight](#ZH-CN_TOPIC_0000002553200801__defaultpickeritemheight)设置选择项的高度。

```ets
// xxx.ets
@Entry
@Component
struct TextPickerExample {
  private select: number = 1;
  private fruits: string[] = ['apple1', 'orange2', 'peach3', 'grape4'];

  build() {
    Column() {
      TextPicker({ range: this.fruits, selected: this.select })
        .defaultPickerItemHeight(60)
        .onChange((value: string | string[], index: number | number[]) => {
          console.info('Picker item changed, value: ' + value + ', index: ' + index);
        })
        .onScrollStop((value: string | string[], index: number | number[]) => {
          console.info('Picker scroll stopped, value: ' + value + ', index: ' + index);
        })
    }.width('100%').height('100%')
  }
```

![image](public_sys-resources/zh-cn_image_0000002553364897.webp)

#### 示例7（设置循环滚动）

该示例通过配置[canLoop](#ZH-CN_TOPIC_0000002553200801__canloop10)设置文本选择器是否循环滚动。

```ets
// xxx.ets
@Entry
@Component
struct TextPickerExample {
  @State isLoop: boolean = false;
  private select: number = 1;
  private fruits: string[] = ['apple1', 'orange2', 'peach3', 'grape4'];

  build() {
    Column() {
      TextPicker({ range: this.fruits, selected: this.select })
        .onChange((value: string | string[], index: number | number[]) => {
          console.info('Picker item changed, value: ' + value + ', index: ' + index);
        })
        .onScrollStop((value: string | string[], index: number | number[]) => {
          console.info('Picker scroll stopped, value: ' + value + ', index: ' + index);
        })
        .canLoop(this.isLoop)

      Row() {
        Text('循环滚动').fontSize(20)

        Toggle({ type: ToggleType.Switch, isOn: false })
          .onChange((isOn: boolean) => {
            this.isLoop = isOn;
          })
      }.position({ x: '60%', y: '40%' })

    }.width('100%')
  }
```

![image](public_sys-resources/zh-cn_image_0000002522244976.webp)

#### 示例8（设置选中项索引值）

该示例通过配置[selectedIndex](#ZH-CN_TOPIC_0000002553200801__selectedindex10)设置默认选中项的索引值。

```ets
// xxx.ets
@Entry
@Component
struct TextPickerExample {
  private fruits: string[] = ['apple1', 'orange2', 'peach3', 'grape4'];

  build() {
    Column() {
      TextPicker({ range: this.fruits, selected: 1 })
        .selectedIndex(2)
        .onChange((value: string | string[], index: number | number[]) => {
          console.info('Picker item changed, value: ' + value + ', index: ' + index);
        })
        .onScrollStop((value: string | string[], index: number | number[]) => {
          console.info('Picker scroll stopped, value: ' + value + ', index: ' + index);
        })
    }.width('100%').height('100%')
  }
```

![image](public_sys-resources/zh-cn_image_0000002553204937.webp)

#### 示例9（设置关闭文本样式变化动效与对应文本样式）

该示例通过配置[disableTextStyleAnimation](#ZH-CN_TOPIC_0000002553200801__disabletextstyleanimation15)、[defaultTextStyle](#ZH-CN_TOPIC_0000002553200801__defaulttextstyle15)实现关闭文本选择器文本样式变化的动效，并设置文本样式。

从API version 15开始，新增disable[Text](Text.md)StyleAnimation、defaultTextStyle接口。

```ets
// xxx.ets
@Entry
@Component
struct TextPickerExample {
  private select: number = 1;
  private fruits: string[] = ['AAAAA', 'BBBBBBBBBBBBB', 'CCCC', 'DDDDDDDD', 'EEE'];

  build() {
    Column() {
      TextPicker({
        range: this.fruits,
        selected: this.select,
        value: this.fruits[this.select]
      })
        .disableTextStyleAnimation(true)
        .margin({ bottom: 30 })
      TextPicker({
        range: this.fruits,
        selected: this.select,
        value: this.fruits[this.select]
      })
        .disableTextStyleAnimation(true)
        .defaultTextStyle({ minFontSize: 18, maxFontSize: 28, overflow: TextOverflow.Ellipsis })
    }.width('100%').height('100%')
  }
```

![image](public_sys-resources/zh-cn_image_0000002522084984.webp)

#### 示例10（设置选中项背景样式）

该示例通过配置[selectedBackgroundStyle](#ZH-CN_TOPIC_0000002553200801__selectedbackgroundstyle20)实现文本选择器选中项的背景样式。

```ets
import { LengthUnit } from '@kit.ArkUI';

// xxx.ets
@Entry
@Component
struct TextPickerExample {
  private showText1: string [] =
    ['Text1', 'Text1', 'Text1', 'Text1']
  private showText2: string[] [] =
    [
      ['Text2', 'Text2', 'Text2', 'Text2'],
      ['Text3', 'Text3', 'Text3', 'Text3']
    ]

  build() {
    Column() {
      Row() {
        TextPicker({ range: this.showText1 })
          .selectedBackgroundStyle({
            color: '#FFD5D5D5',
            borderRadius: { value: 0, unit: LengthUnit.VP }
          })
        Column()
          .width('10%')
        TextPicker({ range: this.showText1 })
          .selectedBackgroundStyle({
            color: '#FFE3F8F9',
            borderRadius: {
              topStart: { value: 5, unit: LengthUnit.VP },
              topEnd: { value: 10, unit: LengthUnit.VP },
              bottomStart: { value: 15, unit: LengthUnit.VP },
              bottomEnd: { value: 20, unit: LengthUnit.VP },
            }
          })
      }

      Row()
        .height('10%')
      Row() {
        TextPicker({ range: this.showText2 })
          .selectedBackgroundStyle({
            borderRadius: {
              topLeft: 8,
              topRight: 8,
              bottomLeft: 8,
              bottomRight: 8
            },
            color: '#FFFFEEF6'
          })
      }
    }.height('100%')
  }
```

![image](public_sys-resources/zh-cn_image_0000002553364899.webp)

#### 示例11（设置文本的最大字号、最小字号、超长文本截断方式）

该示例通过配置[disappearTextStyle](#ZH-CN_TOPIC_0000002553200801__disappeartextstyle20)、[textStyle](#ZH-CN_TOPIC_0000002553200801__textstyle20)和[selectedTextStyle](#ZH-CN_TOPIC_0000002553200801__selectedtextstyle20)，设置文本的颜色、最大字号、最小字号、超长文本截断方式。

从API version 20开始，新增disappear[Text](Text.md)Style、textStyle和selectedTextStyle接口。

```ets
// xxx.ets
@Entry
@Component
struct TextPickerExample {
  private rangeValue: string[] = ['AAAAA', 'BBBBBBBBBBBBB', 'CCCC', 'DDDDDDDD', 'EEEEEEEEEEEEEEE'];

  build() {
    RelativeContainer() {
      TextPicker({
        range: this.rangeValue
      })
        .disappearTextStyle({
          color: '#fff52769',
          // 设置minFontSize与maxFontSize时，font中的size属性将被忽略。
          font: { size: 50 },
          minFontSize: 12,
          maxFontSize: 18,
          overflow: TextOverflow.Ellipsis
        })
        .textStyle({
          color: Color.Orange,
          minFontSize: 12,
          maxFontSize: 18,
          overflow: TextOverflow.MARQUEE
        })
        .selectedTextStyle({
          color: '#ff9eea48',
          minFontSize: 12,
          maxFontSize: 18,
          overflow: TextOverflow.Clip
        })
        .width('100%')
    }
    .height('100%')
    .width('100%')
  }
```

![image](public_sys-resources/zh-cn_image_0000002522244978.webp)
