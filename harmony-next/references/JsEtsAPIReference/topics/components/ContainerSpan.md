# Container[Span](span.md)

[Text](Text.md)组件的子组件，用于统一管理多个[Span]([Span](span.md).md)、[ImageSpan]([ImageSpan](../../types/interfaces/ImageSpan.md).md)的背景色及圆角弧度。


该组件从API version 11开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

#### 子组件

可以包含[Span]([Span](span.md).md)、[ImageSpan]([ImageSpan](../../types/interfaces/ImageSpan.md).md) 子组件。

#### 接口

Container[Span](span.md)()

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

#### 属性

仅支持以下属性：

#### textBackgroundStyle

textBackgroundStyle(style: [TextBackgroundStyle](span.md#ZH-CN_TOPIC_0000002529284887__textbackgroundstyle11对象说明))

设置文本背景样式。子组件在不设置该属性时，将继承此属性值。


从API version 12开始，该接口支持在[attributeModifier](动态属性设置.md#ZH-CN_TOPIC_0000002522240800__attributemodifier)中调用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| style | [TextBackgroundStyle](span.md#ZH-CN_TOPIC_0000002529284887__textbackgroundstyle11对象说明) | 是 | 文本背景样式。 默认值： {  color: Color.Transparent,  radius: 0 } |

#### [attributeModifier](动态属性设置.md#ZH-CN_TOPIC_0000002529284843__attributemodifier)12+

[attributeModifier](动态属性设置.md#ZH-CN_TOPIC_0000002529284843__attributemodifier)(modifier: AttributeModifier<ContainerSpanAttribute>)

设置组件的动态属性。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](动态属性设置.md#ZH-CN_TOPIC_0000002529284843__attributemodifiert)<ContainerSpanAttribute> | 是 | 动态设置组件的属性。 |

#### 事件

不支持[通用事件]([通用事件](../misc/通用事件.md).md)。

#### 示例

#### 示例1（设置背景样式）

从API version 11开始，该示例通过[textBackgroundStyle](#ZH-CN_TOPIC_0000002522080848__textbackgroundstyle)属性展示了文本设置背景样式的效果。

```ets
// xxx.ets
@Component
@Entry
struct Index {
  build() {
    Column() {
      Text() {
        ContainerSpan() {
          // $r('app.media.app_icon')需要替换为开发者所需的图像资源文件。
          ImageSpan($r('app.media.app_icon'))
            .width('40vp')
            .height('40vp')
            .verticalAlign(ImageSpanAlignment.CENTER)
          Span('   Hello World !   ').fontSize('16fp').fontColor(Color.White)
        }
        .textBackgroundStyle({
          color: "#7F007DFF",
          radius: {
            topLeft: 12,
            topRight: 12,
            bottomLeft: 12,
            bottomRight: 12
          }
        })
      }
    }.width('100%').alignItems(HorizontalAlign.Center)
  }
```

![image](public_sys-resources/zh-cn_image_0000002522245078.webp)

#### 示例2（通过[attributeModifier](动态属性设置.md#ZH-CN_TOPIC_0000002529284843__attributemodifier)设置背景样式）

从API version 12开始，该示例通过[attributeModifier](#ZH-CN_TOPIC_0000002522080848__attributemodifier12)属性展示了文本设置背景样式的效果。

```ets
import { ContainerSpanModifier } from '@kit.ArkUI';

class MyContainerSpanModifier extends ContainerSpanModifier {
  applyNormalAttribute(instance: ContainerSpanAttribute): void {
    super.applyNormalAttribute?.(instance);
    this.textBackgroundStyle({ color: "#7F007DFF", radius: "12vp" });
}

@Entry
@Component
struct ContainerSpanModifierExample {
  @State containerSpanModifier: ContainerSpanModifier = new MyContainerSpanModifier();

  build() {
    Column() {
      Text() {
        ContainerSpan() {
          // $r('app.media.startIcon')需要替换为开发者所需的图像资源文件。
          ImageSpan($r('app.media.startIcon'))
            .width('40vp')
            .height('40vp')
            .verticalAlign(ImageSpanAlignment.CENTER)
          Span(' I\'m ContainerSpan attributeModifier ').fontSize('16fp').fontColor(Color.White)
        }.attributeModifier(this.containerSpanModifier as MyContainerSpanModifier)
      }
    }.width('100%').alignItems(HorizontalAlign.Center)
  }
```

![image](public_sys-resources/zh-cn_image_0000002553205039.webp)
