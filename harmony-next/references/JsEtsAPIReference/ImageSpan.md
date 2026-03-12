# ImageSpan

[Text](Text.md)、[ContainerSpan](ContainerSpan.md)组件的子组件，用于显示行内图片。

 该组件从API version 10开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

#### 子组件

无

#### 接口

ImageSpan(value: ResourceStr | PixelMap)

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明value[ResourceStr](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcestr) | [PixelMap](Interface (PixelMap).md)是

图片的数据源，支持本地图片和网络图片。

当使用相对路径引用图片资源时，例如ImageSpan("common/test.jpg")，不支持跨包/跨模块调用该ImageSpan组件，建议使用$r方式来管理需全局使用的图片资源。

- 支持的图片格式包括png、jpg、bmp、svg、gif和heif。

- 支持Base64字符串。格式data:image/[png|jpeg|bmp|webp|heif];base64,[base64 data]，其中[base64 data]为Base64字符串数据。

- 支持file://data/storage路径前缀的字符串，用于读取本应用安装目录下file文件夹下的图片资源。需要保证目录包路径下的文件有可读权限。

#### 属性

属性继承自[BaseSpan](Span.md#ZH-CN_TOPIC_0000002529284887__basespan)，通用属性方法支持[尺寸设置](尺寸设置.md)、[背景设置](背景设置.md)、[边框设置](边框设置.md)。

#### verticalAlign

verticalAlign(value: ImageSpanAlignment)

设置图片基于行高的对齐方式。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明value[ImageSpanAlignment](枚举说明.md#ZH-CN_TOPIC_0000002529284967__imagespanalignment10)是

图片基于行高的对齐方式。

默认值：ImageSpanAlignment.BOTTOM

#### objectFit

objectFit(value: ImageFit)

设置图片的缩放类型。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明value[ImageFit](枚举说明.md#ZH-CN_TOPIC_0000002529284967__imagefit)是

图片的缩放类型。

默认值：ImageFit.Cover

#### alt12+

alt(value: PixelMap)

设置图片加载过程中显示的占位图。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明value[PixelMap](Interface (PixelMap).md)是

设置图片加载过程中显示的占位图，支持[PixelMap](Interface (PixelMap).md)类型。

默认值：null

#### colorFilter14+

colorFilter(filter: ColorFilter | DrawingColorFilter)

为图像设置颜色滤镜效果。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明filter[ColorFilter](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__colorfilter9) | [DrawingColorFilter](Image.md#ZH-CN_TOPIC_0000002497444922__drawingcolorfilter12)是

1. 给图像设置颜色滤镜效果，入参为一个的4x5的RGBA转换矩阵。

矩阵第一行表示R（红色）的向量值，第二行表示G（绿色）的向量值，第三行表示B（蓝色）的向量值，第四行表示A（透明度）的向量值，4行分别代表不同的RGBA的向量值。

当矩阵对角线值为1，其余值为0时，保持图片原有色彩。

**计算规则：**

如果输入的滤镜矩阵为：

像素点为[R, G, B, A]，色值的范围[0, 255]

则过滤后的颜色为 [R’, G’, B’, A’]

2. 支持@ohos.graphics.drawing的ColorFilter类型作为入参。

**说明：**

该接口中的DrawingColorFilter类型支持在元服务中使用。其中，svg类型的图源只对stroke属性生效。

#### supportSvg222+

supportSvg2(enable: Optional<boolean>)

开启或关闭[SVG标签解析能力增强功能](SVG标签解析能力增强.md)，开启后相关SVG图片显示效果会有变化。

ImageSpan组件创建后，不支持动态修改该属性的值。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明enableOptional<boolean>是

控制是否开启[SVG标签解析能力增强功能](SVG标签解析能力增强.md)。

true：支持SVG解析新能力；false：保持原有SVG解析能力。

默认值：false

#### 事件

通用事件仅支持[点击事件](点击控制.md)。还支持以下事件：

#### onComplete12+

onComplete(callback: ImageCompleteCallback)

图片数据加载成功和解码成功时均触发该回调，返回成功加载的图片尺寸。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明callback[ImageCompleteCallback](#ZH-CN_TOPIC_0000002529444861__imagecompletecallback12)是图片数据加载成功和解码成功时触发的回调。

#### onError12+

onError(callback: ImageErrorCallback)

图片加载异常时触发该回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明callback[ImageErrorCallback](Image.md#ZH-CN_TOPIC_0000002497444922__imageerrorcallback9)是图片加载异常时触发的回调。

#### ImageCompleteCallback12+

type ImageCompleteCallback = (result: ImageLoadResult) => void

图片加载成功和解码成功时触发的回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明result[ImageLoadResult](#ZH-CN_TOPIC_0000002529444861__imageloadresult12对象说明)是图片数据加载成功和解码成功触发回调时返回的对象。

#### ImageLoadResult12+对象说明

图片数据加载成功和解码成功触发回调时返回的对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明widthnumber否否

图片的宽。

单位：[px](像素单位.md)

heightnumber否否

图片的高。

单位：[px](像素单位.md)

componentWidthnumber否否

组件的宽。

单位：[px](像素单位.md)

componentHeightnumber否否

组件的高。

单位：[px](像素单位.md)

loadingStatusnumber否否

图片加载成功的状态值。

**说明：**

返回的状态值为0时，表示图片数据加载成功。返回的状态值为1时，表示图片解码成功。

contentWidthnumber否否

图片实际绘制的宽度。

单位：[px](像素单位.md)

**说明：**

仅在loadingStatus返回1时有效。

contentHeightnumber否否

图片实际绘制的高度。

单位：[px](像素单位.md)

**说明：**

仅在loadingStatus返回1时有效。

contentOffsetXnumber否否

实际绘制内容相对于组件自身的x轴偏移。

单位：[px](像素单位.md)

**说明：**

仅在loadingStatus返回1时有效。

contentOffsetYnumber否否

实际绘制内容相对于组件自身的y轴偏移。

单位：[px](像素单位.md)

**说明：**

仅在loadingStatus返回1时有效。

#### 示例

#### 示例1（设置对齐方式）

从API version 10开始，该示例通过[verticalAlign](#ZH-CN_TOPIC_0000002529444861__verticalalign)、[objectFit](#ZH-CN_TOPIC_0000002529444861__objectfit)属性展示了ImageSpan组件的对齐方式以及缩放效果。

```ets
// xxx.ets
@Entry
@Component
struct SpanExample {
  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Text() {
        Span('This is the Span and ImageSpan component').fontSize(25).textCase(TextCase.Normal)
          .decoration({ type: TextDecorationType.None, color: Color.Pink })
      }.width('100%').textAlign(TextAlign.Center)

      Text() {
        // $r('app.media.app_icon')需要替换为开发者所需的图像资源文件。
        ImageSpan($r('app.media.app_icon'))
          .width('200px')
          .height('200px')
          .objectFit(ImageFit.Fill)
          .verticalAlign(ImageSpanAlignment.CENTER)
        Span('I am LineThrough-span')
          .decoration({ type: TextDecorationType.LineThrough, color: Color.Red }).fontSize(25)
        ImageSpan($r('app.media.app_icon'))
          .width('50px')
          .height('50px')
          .verticalAlign(ImageSpanAlignment.TOP)
        Span('I am Underline-span')
          .decoration({ type: TextDecorationType.Underline, color: Color.Red }).fontSize(25)
        ImageSpan($r('app.media.app_icon'))
          .size({ width: '100px', height: '100px' })
          .verticalAlign(ImageSpanAlignment.BASELINE)
        Span('I am Underline-span')
          .decoration({ type: TextDecorationType.Underline, color: Color.Red }).fontSize(25)
        ImageSpan($r('app.media.app_icon'))
          .width('70px')
          .height('70px')
          .verticalAlign(ImageSpanAlignment.BOTTOM)
        Span('I am Underline-span')
          .decoration({ type: TextDecorationType.Underline, color: Color.Red }).fontSize(50)
      }
      .width('100%')
      .textIndent(50)
    }.width('100%').height('100%').padding({ left: 0, right: 0, top: 0 })
  }
}
```

#### 示例2（设置背景样式）

从API version 11开始，该示例通过[textBackgroundStyle](Span.md#ZH-CN_TOPIC_0000002529284887__textbackgroundstyle11)属性展示了文本设置背景样式的效果。

```ets
// xxx.ets
@Component
@Entry
struct Index {
  build() {
    Row() {
      Column() {
        Text() {
          // $r('app.media.sky')需要替换为开发者所需的图像资源文件。
          ImageSpan($r('app.media.sky'))
            .width('60vp')
            .height('60vp')
            .verticalAlign(ImageSpanAlignment.CENTER)
            .borderRadius(20)
            .textBackgroundStyle({ color: '#7F007DFF', radius: "5vp" })
        }
      }.width('100%')
    }.height('100%')
  }
}
```

#### 示例3（为图片添加事件）

从API version 12开始，该示例通过[onComplete](#ZH-CN_TOPIC_0000002529444861__oncomplete12)、[onError](#ZH-CN_TOPIC_0000002529444861__onerror12)为图片添加加载成功和加载异常的事件。

```ets
// xxx.ets
@Entry
@Component
struct Index {
  // $r('app.media.app_icon')需要替换为开发者所需的图像资源文件。
  @State src: ResourceStr = $r('app.media.app_icon');

  build() {
    Column() {
      Text() {
        ImageSpan(this.src)
          .width(100).height(100)
          .onError((err) => {
            console.info("onError: " + err.message);
          })
          .onComplete((event) => {
            console.info("onComplete: " + event.loadingStatus);
          })
      }
    }.width('100%').height('100%')
  }
}
```

#### 示例4（设置颜色滤镜）

从API version 14开始，该示例通过[colorFilter](#ZH-CN_TOPIC_0000002529444861__colorfilter14)属性展示了给ImageSpan图像设置颜色滤镜的效果。

```ets
// xxx.ets
import { drawing } from '@kit.ArkGraphics2D';

@Entry
@Component
struct SpanExample {
  private ColorFilterMatrix: number[] = [0.239, 0, 0, 0, 0, 0, 0.616, 0, 0, 0, 0, 0, 0.706, 0, 0, 0, 0, 0, 1, 0];
  @State DrawingColorFilterFirst: ColorFilter | undefined = new ColorFilter(this.ColorFilterMatrix);

  build() {
    Row() {
      Column({ space: 10 }) {
        //创建ColorFilter对象的方式为图片设置颜色滤镜
        Text() {
          // $r('app.media.sky')需要替换为开发者所需的图像资源文件。
          ImageSpan($r('app.media.sky'))
            .width('60vp')
            .height('60vp')
            .colorFilter(this.DrawingColorFilterFirst)
        }

        //通过drawing.ColorFilter的方式为图片设置颜色滤镜
        Text() {
          // $r('app.media.sky')需要替换为开发者所需的图像资源文件。
          ImageSpan($r('app.media.sky'))
            .width('60vp')
            .height('60vp')
            .colorFilter(drawing.ColorFilter.createBlendModeColorFilter({
              alpha: 255,
              red: 112,
              green: 112,
              blue: 112
            }, drawing.BlendMode.SRC))
        }
      }.width('100%')
    }.height('100%')
  }
}
```

#### 示例5（设置加载占位图）

从API version 12开始，该示例[alt](#ZH-CN_TOPIC_0000002529444861__alt12)属性展示了ImageSpan设置加载网络图片时占位图的效果。

```ets
// xxx.ets
import { http } from '@kit.NetworkKit';
import { image } from '@kit.ImageKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct SpanExample {
  @State imageAlt: PixelMap | undefined = undefined;

  httpRequest() {
    // 直接加载网络地址，请填写一个具体的网络图片地址
    http.createHttp().request("https://www.example.com/xxx.png", (error: BusinessError, data: http.HttpResponse) => {
      if (error) {
        console.error(`http request failed with. Code: ${error.code}, message: ${error.message}`);
      } else {
        console.info(`http request success.`);
        let imageData: ArrayBuffer = data.result as ArrayBuffer;
        let imageSource: image.ImageSource = image.createImageSource(imageData);

        class tmp {
          height: number = 100;
          width: number = 100;
        }

        let option: Record<string, number | boolean | tmp> = {
          'alphaType': 0, // 透明度
          'editable': false, // 是否可编辑
          'pixelFormat': 3, // 像素格式
          'scaleMode': 1, // 缩略值
          'size': { height: 100, width: 100 }
        };
        //创建图片大小
        imageSource.createPixelMap(option).then((pixelMap: PixelMap) => {
          this.imageAlt = pixelMap;
        })
      }
    })
  }

  build() {
    Column() {
      Button("获取网络图片")
        .onClick(() => {
          this.httpRequest();
        })

      Text() {
        // 直接加载网络地址，请填写一个具体的网络图片地址
        ImageSpan('https://www.example.com/xxx.png')
          .alt(this.imageAlt)
          .width(300)
          .height(300)
      }

    }.width('100%').height(250).padding({ left: 35, right: 35, top: 35 })
  }
}
```

#### 示例6（使用supportSvg2属性时，SVG图片的显示效果）

从API version 22开始，该示例通过设置[supportSvg2](#ZH-CN_TOPIC_0000002529444861__supportsvg222)属性，使[SVG标签解析能力增强功能](zh-cn_topic_0000002529284895.html#ZH-CN_TOPIC_0000002529284895__svg易用性提升)的SVG易用性提升能力生效。

```ets
import { drawing } from '@kit.ArkGraphics2D';
@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        Text('属性字符串不支持svg2')
        // $r("app.media.ice")需要替换为开发者所需的图像资源文件。
        Text() {
          ImageSpan($r("app.media.ice"))
            .width(50)
            .height(50)
            .colorFilter(drawing.ColorFilter.createBlendModeColorFilter(
              drawing.Tool.makeColorFromResourceColor(Color.Blue), drawing.BlendMode.SRC_IN))
        }
        Text('属性字符串支持svg2')
        // $r("app.media.ice")需要替换为开发者所需的图像资源文件。
        Text() {
          ImageSpan($r("app.media.ice"))
            .width(50)
            .height(50)
            .supportSvg2(true)
            .colorFilter(drawing.ColorFilter.createBlendModeColorFilter(
              drawing.Tool.makeColorFromResourceColor(Color.Blue), drawing.BlendMode.SRC_IN))
        }
      }
      .width('100%')
    }
    .height('100%')
  }
}
```