# ImageBitmap

ImageBitmap对象可以存储canvas渲染的像素数据。从API version 11开始，当应用创建[Worker线程](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/worker-introduction)，支持使用postMessage将ImageBitmap实例传到Worker中进行绘制，并使用onmessage接收Worker线程发送的绘制结果进行显示。

从 API version 8 开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

#### constructor

constructor(src: string)

通过ImageSrc创建ImageBitmap对象。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明srcstring是

图片的数据源支持本地图片。

1、string格式用于加载本地图片，例如ImageBitmap("common/images/example.jpg")，type为"entry"和"feature"类型的Module，其图片加载路径的起点为当前Module的ets文件夹，type为"har"和"shared"类型的Module，其图片加载路径的起点为当前构建的"entry"或"feature"类型Module的ets文件夹。

type为"har"和"shared"类型的Module中推荐使用[ImageSource](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-decoding)图片解码方式将资源图片解码为统一的PixelMap加载使用。

2、支持本地图片类型：bmp、jpg、png、svg和webp类型。

**说明：**

- ArkTS卡片上不支持http://等网络相关路径前缀、datashare://路径前缀以及file://data/storage路径前缀的字符串。

#### constructor

constructor(data: PixelMap)

通过PixelMap创建ImageBitmap对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明data[PixelMap](Interface (PixelMap).md)是图片的数据源支持PixelMap对象。

#### constructor12+

constructor(src: string, unit: LengthMetricsUnit)

通过ImageSrc创建ImageBitmap对象，支持使用unit配置Path2D对象的单位模式。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明srcstring是

图片的数据源支持本地图片。

1、string格式用于加载本地图片，例如ImageBitmap("common/images/example.jpg")，type为"entry"和"feature"类型的Module，其图片加载路径的起点为当前Module的ets文件夹，type为"har"和"shared"类型的Module，其图片加载路径的起点为当前构建的"entry"或"feature"类型Module的ets文件夹。

type为"har"和"shared"类型的Module中推荐使用[ImageSource](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-decoding)图片解码方式将资源图片解码为统一的PixelMap加载使用。

2、支持本地图片类型：bmp、jpg、png、svg和webp类型。

**说明：**

- ArkTS卡片上不支持http://等网络相关路径前缀、datashare://路径前缀以及file://data/storage路径前缀的字符串。

unit[LengthMetricsUnit](Graphics.md#ZH-CN_TOPIC_0000002529444761__lengthmetricsunit12)是

用来配置ImageBitmap对象的单位模式，配置后无法动态更改，配置方法同[CanvasRenderingContext2D](CanvasRenderingContext2D.md)。

异常值undefined、NaN和Infinity按默认值处理。

#### constructor12+

constructor(data: PixelMap, unit: LengthMetricsUnit)

通过PixelMap创建ImageBitmap对象，支持使用unit配置Path2D对象的单位模式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明data[PixelMap](Interface (PixelMap).md)是图片的数据源支持PixelMap对象。unit[LengthMetricsUnit](Graphics.md#ZH-CN_TOPIC_0000002529444761__lengthmetricsunit12)是用来配置ImageBitmap对象的单位模式，配置后无法动态更改，配置方法同[CanvasRenderingContext2D](CanvasRenderingContext2D.md)。

#### close

close(): void

释放ImageBitmap对象相关联的所有图形资源，并将ImageBitmap对象的宽高置为0。close示例代码同创建ImageBitmap代码。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

#### 属性

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明widthnumber是否

ImageBitmap的像素宽度。

默认单位为vp。

heightnumber是否

ImageBitmap的像素高度。

默认单位为vp。

#### 示例

#### 示例1（加载图片）

通过ImageBitmap加载本地图片。

```ets
// xxx.ets
@Entry
@Component
struct ImageExample {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  // "common/images/example.jpg"需要替换为开发者所需的图像资源文件
  private img: ImageBitmap = new ImageBitmap("common/images/example.jpg");

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() => {
          this.context.drawImage(this.img, 0, 0, 500, 500, 0, 0, 400, 200)
          this.img.close()
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

#### 示例2（创建ImageBitmap）

通过PixelMap创建ImageBitmap对象。

DevEco Studio的预览器不支持getPixelMap接口，不支持显示PixelMap绘制的内容。

```ets
// xxx.ets
@Entry
@Component
struct Demo {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('50%')
        .backgroundColor('#ffff00')
        .onReady(() => {
          this.context.fillStyle = "#00ff00"
          this.context.fillRect(0, 0, 100, 100)
          let pixel = this.context.getPixelMap(0, 0, 100, 100)
          let image = new ImageBitmap(pixel)
          this.context.drawImage(image, 100, 100)
        })

    }
    .width('100%')
    .height('100%')
  }
}
```

#### 示例3（支持并发线程绘制）

通过创建Worker线程，实现并发线程绘制。

DevEco Studio的预览器不支持显示在worker线程中绘制的内容。

```ets
import { worker } from '@kit.ArkTS';

@Entry
@Component
struct imageBitmapExamplePage {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private myWorker = new worker.ThreadWorker('entry/ets/workers/Worker.ts');
  // "common/images/example.jpg"需要替换为开发者所需的图像资源文件
  private img: ImageBitmap = new ImageBitmap("common/images/example.jpg");

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() => {
          this.myWorker.postMessage({ myImage: this.img });
          this.myWorker.onmessage = (e): void => {
            if (e.data.myImage) {
              let image: ImageBitmap = e.data.myImage
              this.context.transferFromImageBitmap(image)
            }
          }
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

Worker线程在onmessage中接收到主线程postMessage发送的ImageBitmap，并进行绘制。

```ets
import { MessageEvents, ThreadWorkerGlobalScope, worker } from '@kit.ArkTS';
import { image } from '@kit.ImageKit';

const workerPort: ThreadWorkerGlobalScope = worker.workerPort;
workerPort.onmessage = (e: MessageEvents) => {
  if (e.data.myImage) {
    let img: ImageBitmap = e.data.myImage
    let offCanvas = new OffscreenCanvas(600, 600)
    let offContext = offCanvas.getContext("2d")
    offContext.drawImage(img, 0, 0, 500, 500, 0, 0, 400, 200)
    let image = offCanvas.transferToImageBitmap()
    workerPort.postMessage({ myImage: image });
  }
}
```