# @ohos.measure (文本计算)

本模块提供文本宽度、高度等相关计算。

-

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

-

该模块不支持在[UIAbility](@ohos.app.ability.UIAbility (带界面的应用组件).md)的文件声明处使用，即不能在UIAbility的生命周期中调用，需要在创建组件实例后使用。

-

如需更多测算文本参数，建议使用图形对应测算接口[Paragraph](@ohos.graphics.text (文本模块).md#ZH-CN_TOPIC_0000002553362061__paragraph)接口。

-

调用文本计算接口时，不建议同时使用[ApplicationContext.setFontSizeScale](ApplicationContext (应用上下文).md#ZH-CN_TOPIC_0000002553360493__applicationcontextsetfontsizescale13)设置应用字体大小缩放比例。为了确保时序的一致性，建议开发者自行监听字体缩放变化，以保证测算结果的准确性。

-

在测算裁剪后的文本时，由于某些Unicode字符（如emoji）的码位长度大于1，直接按字符串长度裁剪会导致不准确的结果。建议基于Unicode码点进行迭代处理，避免错误截断字符，确保测算结果准确。

#### 导入模块

```ets
import { MeasureText } from '@kit.ArkUI';
```

#### MeasureText.measureText(deprecated)

static measureText(options: MeasureOptions): number

计算指定文本作为单行文本显示时的宽度。如果文本包含多行（由换行符\n分隔），则返回其中最长的行的宽度。


-

从API version 9开始支持，从API version 18开始废弃，建议使用[measureText](Class (MeasureUtils).md#ZH-CN_TOPIC_0000002553200693__measuretext12)替代。measureText需要先通过[UIContext](Class (UIContext).md)中的[getMeasureUtils](Class (UIContext).md#ZH-CN_TOPIC_0000002522240732__getmeasureutils12)方法获取[MeasureUtils](Class (MeasureUtils).md)对象，然后通过该对象进行调用。且直接使用measureText可能导致[UI上下文不明确](../../types/classes/Class (UIContext).md)的问题。

-

从API version 12开始，可以通过使用[UIContext](Class (UIContext).md)中的[getMeasureUtils](Class (UIContext).md#ZH-CN_TOPIC_0000002522240732__getmeasureutils12)方法获取当前UI上下文关联的[MeasureUtils](Class (MeasureUtils).md)对象。

-

measureText接口的计算结果始终是单行文本的宽度，入参options中配置的布局约束（如constraintWidth、maxLines）对measureText的结果没有影响。如果需要计算布局约束下的宽度，请使用[measureTextSize](Class (MeasureUtils).md#ZH-CN_TOPIC_0000002553200693__measuretextsize12)方法。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | MeasureOptions | 是 | 被计算文本描述信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 文本宽度。 单位：px |


直接使用MeasureText可能导致[UI上下文不明确](../../types/classes/Class (UIContext).md)的问题，推荐通过[UIContext](Class (UIContext).md)中的[getMeasureUtils](Class (UIContext).md#ZH-CN_TOPIC_0000002522240732__getmeasureutils12)方法获取当前UI上下文关联的[MeasureUtils](Class (MeasureUtils).md)实例。

**示例：**

```ets
import { MeasureText } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State textWidth: number = MeasureText.measureText({
    // 建议使用 this.getUIContext().getMeasureUtils().measureText()接口
    textContent: "Hello World",
    fontSize: '50px'
  });

  build() {
    Row() {
      Column() {
        Text(`The width of 'Hello World': ${this.textWidth}`)
      }
      .width('100%')
    }
    .height('100%')
  }
```

#### MeasureText.measureTextSize(deprecated)

static measureTextSize(options: MeasureOptions): [SizeOptions](../../topics/components/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__sizeoptions)

计算指定文本的宽度和高度。


-

从API version 10开始支持，从API version 18开始废弃，建议使用[measureTextSize](Class (MeasureUtils).md#ZH-CN_TOPIC_0000002553200693__measuretextsize12)替代。measureTextSize需要先通过[UIContext](Class (UIContext).md)中的[getMeasureUtils](Class (UIContext).md#ZH-CN_TOPIC_0000002522240732__getmeasureutils12)方法获取[MeasureUtils](Class (MeasureUtils).md)对象，然后通过该对象进行调用。且直接使用measureTextSize可能导致[UI上下文不明确](../../types/classes/Class (UIContext).md)的问题。

-

从API version 12开始，可以通过使用[UIContext](Class (UIContext).md)中的[getMeasureUtils](Class (UIContext).md#ZH-CN_TOPIC_0000002522240732__getmeasureutils12)方法获取当前UI上下文关联的[MeasureUtils](Class (MeasureUtils).md)对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | MeasureOptions | 是 | 被计算文本描述信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [SizeOptions](../../topics/components/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__sizeoptions) | 返回文本所占布局宽度和高度。 说明: 文本宽度以及高度返回值单位均为px。 |


直接使用MeasureText可能导致[UI上下文不明确](../../types/classes/Class (UIContext).md)的问题，推荐通过[UIContext](Class (UIContext).md)中的[getMeasureUtils](Class (UIContext).md#ZH-CN_TOPIC_0000002522240732__getmeasureutils12)方法获取当前UI上下文关联的[MeasureUtils](Class (MeasureUtils).md)实例。

**示例：**

```ets
import { MeasureText } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  textSize: SizeOptions = MeasureText.measureTextSize({
    // 建议使用 this.getUIContext().getMeasureUtils().measureTextSize()接口
    textContent: "Hello World",
    fontSize: '50px'
  });

  build() {
    Row() {
      Column() {
        Text(`The width of 'Hello World': ${this.textSize.width}`)
        Text(`The height of 'Hello World': ${this.textSize.height}`)
      }
      .width('100%')
    }
    .height('100%')
  }
```

#### MeasureOptions

被计算文本属性。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| textContent | string | [Resource](../../topics/components/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resource) | 否 | 否 | 设置被计算文本内容。 |
| constraintWidth10+ | number | string | Resource | 否 | 是 | 设置被计算文本布局宽度。 说明： 默认单位为vp，不支持设置百分比字符串。若不设置，则文本[SizeOptions](../../topics/components/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__sizeoptions)宽度为单行布局所占最大宽度值，若设置则为设置值。 |
| fontSize | number | string | [Resource](../../topics/components/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resource) | 否 | 是 | 设置被计算文本字体大小，fontSize为number类型时，使用vp单位。 默认值：16 说明： 不支持设置百分比字符串。 从API version 12开始，fontSize为number类型时，使用fp单位。 |
| fontStyle | number | [FontStyle](../../topics/components/枚举说明.md#ZH-CN_TOPIC_0000002529284967__fontstyle) | 否 | 是 | 设置被计算文本字体样式。 默认值：FontStyle.Normal number类型取值范围为[0,1]，取值间隔为1，依次对应FontStyle中的枚举值。 |
| fontWeight | number | string | [FontWeight](../../topics/components/枚举说明.md#ZH-CN_TOPIC_0000002529284967__fontweight) | 否 | 是 | 设置被计算文本的字体粗细，number类型取值[100, 900]，取值间隔为100，默认为400，取值越大，字体越粗。string类型仅支持number类型取值的字符串形式，例如"400"，以及"bold"、"bolder"、"lighter"、"regular"、"medium"，分别对应FontWeight中相应的枚举值。 默认值：FontWeight.Normal |
| fontFamily | string | [Resource](../../topics/components/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resource) | 否 | 是 | 设置被计算文本字体列表。默认字体'HarmonyOS Sans'，且当前只支持这种字体。 |
| letterSpacing | number | string | 否 | 是 | 设置被计算文本字符间距。 默认值：0 |
| textAlign10+ | number | [TextAlign](../../topics/components/枚举说明.md#ZH-CN_TOPIC_0000002529284967__textalign) | 否 | 是 | 设置被计算文本水平方向的对齐方式。 默认值：TextAlign.Start number类型取值范围为[0,3]，取值间隔为1，依次对应TextAlign中的枚举值。 |
| overflow10+ | number | [TextOverflow](../../topics/components/枚举说明.md#ZH-CN_TOPIC_0000002529284967__textoverflow) | 否 | 是 | 设置被计算文本超长时的截断方式。 默认值：1 number类型取值范围为[0,3]，取值间隔为1，依次对应TextOverflow中的枚举值。 |
| maxLines10+ | number | 否 | 是 | 设置被计算文本最大行数。 取值范围：[0, INT32_MAX] |
| lineHeight10+ | number | string | [Resource](../../topics/components/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resource) | 否 | 是 | 设置被计算文本行高。 |
| baselineOffset10+ | number | string | 否 | 是 | 设置被计算文本基线的偏移量。 默认值：0 |
| textCase10+ | number | [TextCase](../../topics/components/枚举说明.md#ZH-CN_TOPIC_0000002529284967__textcase) | 否 | 是 | 设置被计算文本大小写。 默认值：TextCase.Normal number类型取值范围为[0,2]，取值间隔为1，依次对应TextCase中的枚举值。 |
| textIndent11+ | number | string | 否 | 是 | 设置首行文本缩进，默认值为0。 |
| wordBreak11+ | [WordBreak](../../topics/components/枚举说明.md#ZH-CN_TOPIC_0000002529284967__wordbreak11) | 否 | 是 | 设置断行规则。 默认值：WordBreak.BREAK_WORD 说明： WordBreak.BREAK_ALL与{overflow: [TextOverflow](../../topics/components/枚举说明.md#ZH-CN_TOPIC_0000002529284967__textoverflow).Ellipsis}，maxLines组合使用可实现英文单词按字母截断，超出部分以省略号显示。 |