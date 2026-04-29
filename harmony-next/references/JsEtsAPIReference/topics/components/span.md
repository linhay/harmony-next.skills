# Span

作为[Text](Text.md)、[ContainerSpan](ContainerSpan.md)组件的子组件，用于显示行内文本的组件。


 该组件从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

 该组件从API version 10开始支持继承父组件[Text](Text.md)的属性，即如果子组件未设置属性且父组件设置属性，则继承父组件设置的属性。支持继承的属性仅包括：fontColor、fontSize、fontStyle、fontWeight、decoration、letterSpacing、textCase、fontFamily、textShadow。

 不支持[通用属性](通用属性.md)。若需设置通用属性，应使用[Text](Text.md)进行设置，或改用[属性字符串](属性字符串.md)中的[CustomSpan](属性字符串.md#ZH-CN_TOPIC_0000002553360773__customspan)自行绘制。

 [通用事件](通用事件.md)只支持点击事件[onClick](点击事件.md#ZH-CN_TOPIC_0000002522240764__onclick)和悬浮事件[onHover](悬浮事件.md#ZH-CN_TOPIC_0000002553360691__onhover)。

#### 子组件

无

#### 接口

Span(value: string | [Resource](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resource))

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string | [Resource](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resource) | 是 | 文本内容。 |

#### 属性

属性继承自[BaseSpan](#ZH-CN_TOPIC_0000002522240844__basespan)。

#### decoration

decoration(value: DecorationStyleInterface)

设置文本装饰线样式及其颜色。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [DecorationStyleInterface12+](属性字符串.md#ZH-CN_TOPIC_0000002497444920__decorationstyleinterface) | 是 | 文本装饰线样式对象。 默认值： {  type: TextDecorationType.None,  color: Color.Black,  style: TextDecorationStyle.SOLID  } 说明：  style参数不支持卡片能力。 |


 当文字的下边缘轮廓与装饰线位置相交时，会触发下划线避让规则，下划线将在这些字符处避让文字。常见“gjyqp”等英文字符。

 当文本装饰线的颜色设置为Color.Transparent时，装饰线颜色设置为跟随每行第一个字的字体颜色。当文本装饰线的颜色设置为透明色16进制对应值“#00FFFFFF”时，装饰线颜色设置为透明色。

#### letterSpacing

letterSpacing(value: number | [Resource](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resource)Str)

设置文本字符间距。取值小于0，字符聚集重叠，取值大于0且随着数值变大，字符间距越来越大，稀疏分布。string类型支持number类型取值的字符串形式，可以附带单位，例如"10"、"10[fp](像素单位.md)"。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | [ResourceStr](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcestr) | 是 | 文本字符间距。 单位：[fp](像素单位.md)  从API version 20开始，支持Resource类型。 |

#### textCase

textCase(value: [TextCase](枚举说明.md#ZH-CN_TOPIC_0000002529284967__textcase))

设置文本大小写。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [TextCase](枚举说明.md#ZH-CN_TOPIC_0000002529284967__textcase) | 是 | 文本大小写。 默认值：TextCase.Normal |

#### fontColor

fontColor(value: [ResourceColor](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor))

设置字体颜色。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor) | 是 | 字体颜色。 默认值：'e6182431' Wearable设备上默认值为：'#c5ffffff' |

#### fontSize

fontSize(value: number | string | [Resource](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resource))

设置字体大小。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | string | [Resource](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resource) | 是 | 字体大小。fontSize为number类型时，使用fp单位。字体默认大小16fp。string类型支持number类型取值的字符串形式，可以附带单位，例如"10"、"10fp"，不支持设置百分比字符串。 Wearable设备上默认值为：15fp |

#### fontStyle

fontStyle(value: [FontStyle](枚举说明.md#ZH-CN_TOPIC_0000002529284967__fontstyle))

设置字体样式。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [FontStyle](枚举说明.md#ZH-CN_TOPIC_0000002529284967__fontstyle) | 是 | 字体样式。 默认值：FontStyle.Normal |

#### fontWeight

fontWeight(value: number | FontWeight | [Resource](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resource)Str)

设置文本的字体粗细，设置过大可能会在不同字体下有截断。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | [FontWeight](枚举说明.md#ZH-CN_TOPIC_0000002529284967__fontweight) | [ResourceStr](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcestr) | 是 | 文本的字体粗细，number类型取值[100, 900]，取值间隔为100，默认为400，取值越大，字体越粗。string类型仅支持number类型取值的字符串形式，例如"400"，以及"bold"、"bolder"、"lighter"、"regular"、"medium"，分别对应FontWeight中相应的枚举值。 默认值：FontWeight.Normal  从API version 20开始，支持Resource类型。 |

#### fontFamily

fontFamily(value: string | [Resource](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resource))

设置字体列表。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string | [Resource](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resource) | 是 | 字体列表。 默认字体'HarmonyOS Sans'。 使用多个字体时，请用逗号','分隔，字体的优先级按顺序生效。例如：'Arial,HarmonyOS Sans'。 |


可以使用[loadFontSync](@ohos.graphics.text (文本模块).md#ZH-CN_TOPIC_0000002553362061__loadfontsync)注册自定义字体。

#### lineHeight10+

lineHeight(value: [Length](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__length))

设置文本行高。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Length](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__length) | 是 | 文本行高。   number类型时单位为fp。设置string类型时，支持number类型取值的字符串形式，可以附带单位，例如"10"、"10fp"。 |

#### font10+

font(value: [Font](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__font))

设置文本样式。包括字体大小、字体粗细、字体族和字体风格。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Font](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__font) | 是 | 文本样式。 |

#### textShadow11+

textShadow(value: [ShadowOptions](图像效果.md#ZH-CN_TOPIC_0000002497444856__shadowoptions对象说明) | Array<ShadowOptions>)

设置文字阴影效果。该接口支持以数组形式入参，实现多重文字阴影。不支持fill字段, 不支持智能取色模式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ShadowOptions](图像效果.md#ZH-CN_TOPIC_0000002497444856__shadowoptions对象说明) | Array<ShadowOptions> | 是 | 文字阴影效果。 |

#### 事件

通用事件支持[点击事件onClick](点击事件.md#ZH-CN_TOPIC_0000002522240764__onclick)、[悬浮事件onHover](悬浮事件.md#ZH-CN_TOPIC_0000002553360691__onhover)。


 由于Span组件无尺寸信息，因此点击事件返回的ClickEvent对象的target属性无效。

#### BaseSpan

定义BaseSpan基础类，包含Span的通用属性。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

#### textBackgroundStyle11+

textBackgroundStyle(style: [Text](Text.md)BackgroundStyle): T

设置背景样式。作为[ContainerSpan](ContainerSpan.md)的子组件时可以继承它的此属性值，优先使用其自身的此属性。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| style | [Text](Text.md)BackgroundStyle | 是 | 背景样式。 默认值: {  color: Color.Transparent,  radius: 0 } |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前Span的属性。 |

#### baselineOffset12+

baselineOffset(value: [LengthMetrics](../misc/Graphics.md#ZH-CN_TOPIC_0000002529444761__lengthmetrics12)): T

设置Span基线的偏移量。此属性与父组件的baselineOffset是共存的。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [LengthMetrics](../misc/Graphics.md#ZH-CN_TOPIC_0000002529444761__lengthmetrics12) | 是 | 设置Span基线的偏移量，设置该值为百分比时，按默认值显示。 正数内容向上偏移，负数向下偏移。 默认值：0 在ImageSpan中，设置为非0时，[verticalAlign](../../types/interfaces/ImageSpan.md#ZH-CN_TOPIC_0000002529444861__verticalalign)将固定为ImageSpanAlignment.BASELINE对齐；设置为0时，要使基线对齐策略生效，需同时设置verticalAlign为ImageSpanAlignment.BASELINE。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前Span的属性。 |

#### [Text](Text.md)BackgroundStyle11+对象说明

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| color | [ResourceColor](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor) | 否 | 是 | 文本背景色。 |
| radius | [Dimension](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__dimension10) | [BorderRadiuses](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__borderradiuses9) | 否 | 是 | 文本背景圆角。 |

#### 示例

#### 示例1（设置文本样式）

该示例展示了设置不同样式的文本效果以及span配置点击事件。

```ets
// xxx.ets
@Entry
@Component
struct SpanExample {
  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Start }) {
      Text('Basic Usage').fontSize(9).fontColor(0xCCCCCC)
      Text() {
        Span('In Line')
        Span(' Component')
        Span(' !')
      }

      Text() {
        Span('This is the Span component').fontSize(12).textCase(TextCase.Normal)
          .decoration({ type: TextDecorationType.None, color: Color.Red })
          .fontFamily('HarmonyOS Sans')
      }.margin({ top: 12 })

      // 文本横线添加
      Text('Text Decoration').fontSize(9).fontColor(0xCCCCCC).margin({ top: 12 })
      Text() {
        Span('I am Underline-WAVY-span')
          .decoration({ type: TextDecorationType.Underline, color: Color.Red, style: TextDecorationStyle.WAVY })
          .fontSize(12)
      }

      Text() {
        Span('I am LineThrough-DOTTED-span')
          .decoration({ type: TextDecorationType.LineThrough, color: Color.Red, style: TextDecorationStyle.DOTTED })
          .fontSize(12)
      }

      Text() {
        Span('I am Overline-DASHED-span')
          .decoration({ type: TextDecorationType.Overline, color: Color.Red, style: TextDecorationStyle.DASHED })
          .fontSize(12)
      }

      // 文本字符间距
      Text('LetterSpacing').fontSize(9).fontColor(0xCCCCCC).margin({ top: 12 })
      Text() {
        Span('span letter spacing')
          .letterSpacing(0)
          .fontSize(12)
      }

      Text() {
        Span('span letter spacing')
          .letterSpacing(-2)
          .fontSize(12)
      }

      Text() {
        Span('span letter spacing')
          .letterSpacing(3)
          .fontSize(12)
      }

      // 文本大小写展示设置
      Text('Text Case').fontSize(9).fontColor(0xCCCCCC).margin({ top: 12 })
      Text() {
        Span('I am Lower-span').fontSize(12)
          .textCase(TextCase.LowerCase)
          .decoration({ type: TextDecorationType.None })
      }

      Text() {
        Span('I am Upper-span').fontSize(12)
          .textCase(TextCase.UpperCase)
          .decoration({ type: TextDecorationType.None })
      }

      // 文本字体样式设置
      Text('FontStyle').fontSize(9).fontColor(0xCCCCCC).margin({ top: 12 })
      Text() {
        Span('I am FontStyle-Normal').fontSize(12)
          .fontStyle(FontStyle.Normal)
      }

      Text() {
        Span('I am FontStyle-Italic').fontSize(12)
          .fontStyle(FontStyle.Italic)
      }

      // 文本字体粗细设置
      Text('FontWeight').fontSize(9).fontColor(0xCCCCCC).margin({ top: 12 })
      Text() {
        Span('I am FontWeight-Lighter').fontSize(12)
          .fontWeight(FontWeight.Lighter)
      }

      Text() {
        Span('I am FontWeight-Bold').fontSize(12)
          .fontWeight(FontWeight.Bold)
      }

      // 文本行高设置
      Text('LineHeight').fontSize(9).fontColor(0xCCCCCC).margin({ top: 12 })
      Text() {
        Span('I am lineHeight default\n').fontSize(12)
          .fontWeight(FontWeight.Lighter)
        Span('I am lineHeight 30').fontSize(12)
          .lineHeight(30)
      }
      .backgroundColor(Color.Gray)

      // 文本样式设置
      Text('Font').fontSize(9).fontColor(0xCCCCCC).margin({ top: 12 })
      Text() {
        Span('span font 12 Bolder Italic')
          .font({
            size: 12,
            weight: FontWeight.Bolder,
            style: FontStyle.Italic,
            family: "HarmonyOS Sans"
          })
      }

      // span点击事件设置
      Text('span click event').fontSize(9).fontColor(0xCCCCCC).margin({ top: 12 })
      Text() {
        Span('Span default ').fontSize(12)
        Span('Span click')
          .onClick((event) => {
            console.info("span onClick")
          })
      }
    }.width('100%').padding({ left: 35, right: 35, top: 35 })
  }
```

![image](public_sys-resources/zh-cn_image_0000002553205033.webp)

#### 示例2（设置文本阴影）

从API version 11开始，该示例通过[textShadow](#ZH-CN_TOPIC_0000002522240844__textshadow11)属性展示了文本设置阴影的效果。

```ets
// xxx.ets
@Entry
@Component
struct SpanExample {
  @State textShadows: ShadowOptions | Array<ShadowOptions> = [{
    radius: 10,
    color: Color.Red,
    offsetX: 10,
    offsetY: 0
  }, {
    radius: 10,
    color: Color.Orange,
    offsetX: 20,
    offsetY: 0
  },
    {
      radius: 10,
      color: Color.Yellow,
      offsetX: 30,
      offsetY: 0
    }, {
      radius: 10,
      color: Color.Green,
      offsetX: 40,
      offsetY: 0
    },
    {
      radius: 10,
      color: Color.Blue,
      offsetX: 100,
      offsetY: 0
    }]

  build() {
    Column({ space: 8 }) {
      Text() {
        Span('123456789').fontSize(50).textShadow(this.textShadows).fontColor(Color.Pink)
      }

      Text() {
        Span('123456789') // span can inherit text shadow & font size from outer text
      }.fontSize(50).textShadow(this.textShadows).fontColor(Color.Pink)
    }
```

![image](public_sys-resources/zh-cn_image_0000002522085080.webp)

#### 示例3（设置背景样式）

从API version 11开始，该示例通过[textBackgroundStyle](#ZH-CN_TOPIC_0000002522240844__textbackgroundstyle11)属性展示了文本设置背景样式的效果。

```ets
// xxx.ets
@Component
@Entry
struct SpanExample {
  build() {
    Column() {
      Text() {
        Span('   Hello World !   ')
          .fontSize('20fp')
          .textBackgroundStyle({ color: "#7F007DFF", radius: "5vp" })
          .fontColor(Color.White)
      }
    }.width('100%').margin({ bottom: '5vp' }).alignItems(HorizontalAlign.Center)
  }
```

![image](public_sys-resources/zh-cn_image_0000002553364997.webp)

#### 示例4（设置文本基线偏移量）

从API version 12开始，该示例通过[baselineOffset](#ZH-CN_TOPIC_0000002522240844__baselineoffset12)属性展示了文本设置不同基线偏移量的效果。

```ets
// xxx.ets
import { LengthUnit, LengthMetrics } from '@kit.ArkUI';

@Entry
@Component
struct SpanExample {
  build() {
    Row() {
      Column() {
        Text() {
          Span('SpanOne')
            .fontSize(10)
            .baselineOffset(new LengthMetrics(20, LengthUnit.VP))
          Span('SpanTwo')
            .fontSize(10)
            .baselineOffset(new LengthMetrics(0, LengthUnit.VP))
          // $r('app.media.sky')需要替换为开发者所需的图像资源文件。
          ImageSpan($r("app.media.sky"))
            .width('80px')
            .baselineOffset(new LengthMetrics(-20, LengthUnit.VP))
        }
        .backgroundColor('#7F007DFF')
      }
      .width('100%')
    }
    .height('100%')
  }
```

![image](public_sys-resources/zh-cn_image_0000002522245074.webp)
