# Canvas

提供画布组件，用于自定义绘制图形。

 该组件从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

#### 子组件

不支持。

#### 接口

#### Canvas

Canvas(context?: CanvasRenderingContext2D | DrawingRenderingContext)

创建Canvas组件时，最大面积不超过10000px*10000px，超过最大面积则无法正常创建。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明context[CanvasRenderingContext2D](CanvasRenderingContext2D.md) | [DrawingRenderingContext12+](DrawingRenderingContext.md)否

CanvasRenderingContext2D: 不支持多个Canvas共用一个CanvasRenderingContext2D对象，具体描述见[CanvasRenderingContext2D](CanvasRenderingContext2D.md)对象。DrawingRenderingContext: 不支持多个Canvas共用一个DrawingRenderingContext对象，具体描述见[DrawingRenderingContext](DrawingRenderingContext.md)对象。

异常值null按无效值处理。

#### Canvas12+

Canvas(context: CanvasRenderingContext2D | DrawingRenderingContext, imageAIOptions: ImageAIOptions)

创建Canvas组件，支持设置CanvasRenderingContext2D对象或DrawingRenderingContext对象，支持设置AI分析选项。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明context[CanvasRenderingContext2D](CanvasRenderingContext2D.md) | [DrawingRenderingContext12+](DrawingRenderingContext.md)是

CanvasRenderingContext2D: 不支持多个Canvas共用一个CanvasRenderingContext2D对象，具体描述见[CanvasRenderingContext2D](CanvasRenderingContext2D.md)对象。DrawingRenderingContext: 不支持多个Canvas共用一个DrawingRenderingContext对象，具体描述见[DrawingRenderingContext](DrawingRenderingContext.md)对象。

异常值null按无效值处理。

imageAIOptions[ImageAIOptions](图像类型定义.md#ZH-CN_TOPIC_0000002497604902__imageaioptions12)是

给组件设置一个AI分析选项，通过此项可配置分析类型或绑定一个分析控制器。

异常值null和undefined按[ImageAIOptions](图像类型定义.md#ZH-CN_TOPIC_0000002497604902__imageaioptions12)的默认值处理。

#### 属性

除支持[通用属性](通用属性.md)外，还支持以下属性：

#### enableAnalyzer12+

设置组件支持AI分析，当前支持主体识别、文字识别和对象查找等功能，支持[attributeModifier](动态属性设置.md#ZH-CN_TOPIC_0000002529284843__attributemodifier)动态设置属性方法。

需要搭配[CanvasRenderingContext2D](CanvasRenderingContext2D.md)中的[StartImageAnalyzer](CanvasRenderingContext2D.md#ZH-CN_TOPIC_0000002497444936__startimageanalyzer12)和[StopImageAnalyzer](CanvasRenderingContext2D.md#ZH-CN_TOPIC_0000002497444936__stopimageanalyzer12)一起使用。

不能和[overlay](浮层.md#ZH-CN_TOPIC_0000002497604826__overlay)属性同时使用，两者同时设置时overlay中CustomBuilder属性将失效。该特性依赖设备能力。

从API version 20开始，该接口支持在[attributeModifier](动态属性设置.md#ZH-CN_TOPIC_0000002529284843__attributemodifier)中调用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明enableboolean是

组件支持AI分析，需要组件内容支持主体识别、文字识别或对象查找。

设置为true时，组件可进行AI分析，设置为false时，组件不可进行AI分析。

异常值null和undefined按默认值处理。

默认值：false

#### 事件

除支持[通用事件](通用事件.md)外，还支持如下事件：

#### onReady

onReady(event: VoidCallback)

Canvas组件初始化完成或者发生大小变化时的事件回调，支持[attributeModifier](动态属性设置.md#ZH-CN_TOPIC_0000002529284843__attributemodifier)动态设置属性方法。

当该事件被触发时画布被清空，该事件之后Canvas组件宽高确定且可获取，可使用Canvas相关API进行绘制。当Canvas组件仅发生位置变化时，只触发[onAreaChange](组件区域变化事件.md#ZH-CN_TOPIC_0000002529444787__onareachange)事件，不触发onReady事件。[onAreaChange](组件区域变化事件.md#ZH-CN_TOPIC_0000002529444787__onareachange)事件在onReady事件后触发。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明event[VoidCallback](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__voidcallback12)是Canvas组件初始化完成或者发生大小变化时的事件回调事件。

#### 示例

#### 示例1（使用CanvasRenderingContext2D中的方法）

该示例实现了如何在Canvas组件使用[CanvasRenderingContext2D](CanvasRenderingContext2D.md)中的方法进行绘制。

```ets
// xxx.ets
@Entry
@Component
struct CanvasExample {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() => {
          this.context.fillRect(0, 30, 100, 100)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

#### 示例2（使用DrawingRenderingContext中的方法）

该示例实现了如何在Canvas组件使用[DrawingRenderingContext](DrawingRenderingContext.md)中的方法进行绘制。

```ets
// xxx.ets
@Entry
@Component
struct CanvasExample {
  private context: DrawingRenderingContext = new DrawingRenderingContext();

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('rgb(213,213,213)')
        .onReady(() => {
          this.context.canvas.drawCircle(200, 200, 100)
          this.context.invalidate()
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

#### 示例3（使用attributeModifier动态设置Canvas组件的属性及方法）

该示例展示了如何使用[attributeModifier](动态属性设置.md#ZH-CN_TOPIC_0000002529284843__attributemodifier)动态设置Canvas组件的[enableAnalyzer](#ZH-CN_TOPIC_0000002529284905__enableanalyzer12)属性和[onReady](#ZH-CN_TOPIC_0000002529284905__onready)方法。

```ets
// xxx.ets
import { BusinessError } from '@kit.BasicServicesKit';

class MyCanvasModifier implements AttributeModifier<CanvasAttribute> {
  context: CanvasRenderingContext2D = new CanvasRenderingContext2D()

  applyNormalAttribute(instance: CanvasAttribute): void {
    // 从（0，0）绘制一张宽高为200vp的图片
    instance.onReady(() => {
      let image = new ImageBitmap("image.png")
      this.context.drawImage(image, 0, 0, 200, 200)
    })
    // 设置开启组件AI分析功能，点击start后，长按触发AI识别功能
    instance.enableAnalyzer(true)
  }
}

@Entry
@Component
struct attributeDemo {
  @State modifier: MyCanvasModifier = new MyCanvasModifier()
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)
  private config: ImageAnalyzerConfig = {
    types: [ImageAnalyzerType.SUBJECT, ImageAnalyzerType.TEXT]
  }
  private aiController: ImageAnalyzerController = new ImageAnalyzerController()
  private options: ImageAIOptions = {
    types: [ImageAnalyzerType.SUBJECT, ImageAnalyzerType.TEXT],
    aiController: this.aiController
  }

  build() {
    Row() {
      Column() {
        Button('start')
          .width(100)
          .height(50)
          .margin(5)
          .onClick(() => {
            this.context.startImageAnalyzer(this.config)
              .then(() => {
                console.info("analysis complete")
              })
              .catch((error: BusinessError) => {
                console.info("error code: " + error.code)
              })
          })
        Button('stop')
          .width(100)
          .height(50)
          .margin(5)
          .onClick(() => {
            this.context.stopImageAnalyzer()
          })
        Button('getTypes')
          .width(100)
          .height(50)
          .margin(5)
          .onClick(() => {
            this.aiController.getImageAnalyzerSupportTypes()
          })
        Canvas(this.context, this.options)
          .borderWidth(1)
          .height(200)
          .width(200)
          .attributeModifier(this.modifier)
          .onAppear(() => {
            this.modifier.context = this.context
          })
      }
    }
  }
}
```