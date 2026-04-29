# @ohos.arkui.drawableDescriptor (DrawableDescriptor)

本模块提供分层图标合成（包括前景，背景，蒙版），动图播放与控制，基础图像处理的能力。

-

本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

-

示例效果请以真机运行为准，当前DevEco Studio预览器不支持。

#### 导入模块

```ets
import {
  DrawableDescriptor,
  LayeredDrawableDescriptor,
  AnimatedDrawableDescriptor,
  AnimationOptions,
  AnimationController
} from '@kit.ArkUI';
```

#### DrawableDescriptorLoadedResult21+

传入的图片资源或地址的加载结果。

**元服务API：** 从API version 21开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| imageWidth | number | 否 | 否 | 图片的宽度。 单位：px |
| imageHeight | number | 否 | 否 | 图片的高度。 单位：px |

**示例：**

```ets
import { AnimatedDrawableDescriptor, AnimationOptions, DrawableDescriptor, DrawableDescriptorLoadedResult } from '@kit.ArkUI';

let options: AnimationOptions = { duration: 2000, iterations: 1 };
let drawable: DrawableDescriptor = new AnimatedDrawableDescriptor($r('app.media.gif'), options)
try {
    // 可以提前手动加载动图资源到内存中。
    let result: DrawableDescriptorLoadedResult = drawable.loadSync()
    console.info(`load result = ${JSON.stringify(result)}`)
} catch(e) {
    console.error("load failed")
}
```

#### DrawableDescriptor

父类对象提供可重写的方法，包含：获取[PixelMap](Interface (PixelMap).md)实例，图片资源加载能力。

#### getPixelMap

getPixelMap(): image.PixelMap

获取PixelMap实例。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| image.PixelMap | PixelMap |

**示例：**

```ets
import { DrawableDescriptor, LayeredDrawableDescriptor } from '@kit.ArkUI'
import { image } from '@kit.ImageKit'

let resManager = this.getUIContext().getHostContext()?.resourceManager;
// $r('app.media.app_icon')需要替换为开发者所需的图像资源文件。
let pixmap: DrawableDescriptor = (resManager?.getDrawableDescriptor($r('app.media.icon')
  .id)) as DrawableDescriptor; // 当传入资源id或name为普通图片时，生成DrawableDescriptor对象。
let pixmapNew: image.PixelMap | undefined = pixmap?.getPixelMap();
```

#### loadSync21+

loadSync(): DrawableDescriptorLoadedResult

发起图片资源的同步加载，并返回加载结果。

**元服务API：** 从API version 21开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| DrawableDescriptorLoadedResult | 图片资源的加载结果。 |

**错误码：**

以下错误码的详细介绍请参见[DrawableDescriptor错误码]([DrawableDescriptor错误码](../../errors/DrawableDescriptor错误码.md).md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 111001 | resource loading failed. |

```ets
import { AnimatedDrawableDescriptor, DrawableDescriptor, DrawableDescriptorLoadedResult, AnimationOptions } from '@kit.ArkUI';

let options: AnimationOptions = { duration: 2000, iterations: 1 };
let drawable: DrawableDescriptor = new AnimatedDrawableDescriptor($r('app.media.gif'), options)
try {
    // 可以提前手动加载动图资源到内存中
    let result: DrawableDescriptorLoadedResult = drawable.loadSync()
    console.info(`load result = ${JSON.stringify(result)}`)
} catch(e) {
    console.error("load failed")
}
```

#### load21+

load(): Promise<DrawableDescriptorLoadedResult>

发起图片资源的异步加载，并返回加载结果。使用Promise异步回调。

**元服务API：** 从API version 21开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<DrawableDescriptorLoadedResult> | 图片资源的加载结果。 |

**错误码：**

以下错误码的详细介绍请参见[DrawableDescriptor错误码](DrawableDescriptor错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 111001 | resource loading failed. |

```ets
import {
  AnimatedDrawableDescriptor,
  DrawableDescriptor,
  DrawableDescriptorLoadedResult,
  AnimationOptions
} from '@kit.ArkUI';

let options: AnimationOptions = { duration: 2000, iterations: 1 };
let drawable: DrawableDescriptor = new AnimatedDrawableDescriptor($r('app.media.gif'), options)
drawable.load().then((result: DrawableDescriptorLoadedResult) => {
  console.info(`load result = ${JSON.stringify(result)}`)
}).catch(() => {
  console.info(`load failed`)
})
```

#### PixelMapDrawableDescriptor12+

支持通过传入PixelMap创建PixelMapDrawableDescriptor对象。继承自[DrawableDescriptor](#ZH-CN_TOPIC_0000002553200683__drawabledescriptor)。

#### constructor12+

constructor(src?: image.PixelMap)

PixelMapDrawableDescriptor的构造函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src | image.PixelMap | 否 | PixelMap类型参数，存储 PixelMap 图片数据。 |

#### LayeredDrawableDescriptor

当传入资源id或name为包含前景和背景资源的json文件时，生成LayeredDrawableDescriptor对象。继承自[DrawableDescriptor](#ZH-CN_TOPIC_0000002553200683__drawabledescriptor)。

drawable.json位于项目工程entry/src/main/resources/base/media目录下。定义请参考：

```ets
{
  "layered-image":
  {
    "background" : "$media:background",
    "foreground" : "$media:foreground"
}
```

**示例：**

使用json文件创建LayeredDrawableDescriptor，示例代码如下。

```ets
// xxx.ets
import { DrawableDescriptor, LayeredDrawableDescriptor } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  private resManager = this.getUIContext().getHostContext()?.resourceManager;
  // $r('app.media.drawable')需要替换为开发者所需的图像资源文件。
  private layeredDrawableDescriptor: DrawableDescriptor | undefined =
    this.resManager?.getDrawableDescriptor($r('app.media.drawable').id);

  build() {
    Row() {
      Column() {
        Image((this.layeredDrawableDescriptor instanceof LayeredDrawableDescriptor) ?
          this.layeredDrawableDescriptor : undefined)
        Image((this.layeredDrawableDescriptor instanceof LayeredDrawableDescriptor) ?
          this.layeredDrawableDescriptor?.getForeground()?.getPixelMap() : undefined)
      }.height('50%')
    }.width('50%')
}
```

使用PixelMapDrawableDescriptor创建LayeredDrawableDescriptor，示例代码如下。

```ets
import { DrawableDescriptor, LayeredDrawableDescriptor, PixelMapDrawableDescriptor } from '@kit.ArkUI';
import { image } from '@kit.ImageKit';

@Entry
@Component
struct Index {
  @State fore1: image.PixelMap | undefined = undefined;
  @State back1: image.PixelMap | undefined = undefined;

  @State foregroundDraw: DrawableDescriptor | undefined = undefined;
  @State backgroundDraw: DrawableDescriptor | undefined = undefined;
  @State maskDraw: DrawableDescriptor | undefined = undefined;
  @State maskPixel: image.PixelMap | undefined = undefined;
  @State draw: LayeredDrawableDescriptor | undefined = undefined;

  async aboutToAppear() {
    // $r('app.media.foreground')需要替换为开发者所需的图像资源文件。
    this.fore1 = await this.getPixmapFromMedia($r('app.media.foreground'));
    // $r('app.media.background')需要替换为开发者所需的图像资源文件。
    this.back1 = await this.getPixmapFromMedia($r('app.media.background'));
    // $r('app.media.ohos_icon_mask')需要替换为开发者所需的图像资源文件。
    this.maskPixel = await this.getPixmapFromMedia($r('app.media.ohos_icon_mask'));
    // 使用PixelMapDrawableDescriptor创建LayeredDrawableDescriptor。
    this.foregroundDraw = new PixelMapDrawableDescriptor(this.fore1);
    this.backgroundDraw = new PixelMapDrawableDescriptor(this.back1);
    this.maskDraw = new PixelMapDrawableDescriptor(this.maskPixel);
    this.draw = new LayeredDrawableDescriptor(this.foregroundDraw,this.backgroundDraw,this.maskDraw);
  }

  build() {
    Row() {
      Column() {
          Image(this.draw)
            .width(300)
            .height(300)
      }.height('100%').justifyContent(FlexAlign.Center)
    }.width('100%').height("100%").backgroundColor(Color.Pink)
  }
  // 根据资源，通过图片框架获取pixelMap。
  private async getPixmapFromMedia(resource: Resource) {
    let unit8Array = await this.getUIContext().getHostContext()?.resourceManager?.getMediaContent(resource.id);
    let imageSource = image.createImageSource(unit8Array?.buffer.slice(0, unit8Array.buffer.byteLength));
    let createPixelMap: image.PixelMap = await imageSource.createPixelMap({
      desiredPixelFormat: image.PixelMapFormat.BGRA_8888
    });
    await imageSource.release();
    return createPixelMap;
  }
```

#### constructor12+

constructor(foreground?: DrawableDescriptor, background?: DrawableDescriptor, mask?: DrawableDescriptor)

LayeredDrawableDescriptor的构造函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| foreground | DrawableDescriptor | 否 | 分层图标的前景图片选项。 |
| background | DrawableDescriptor | 否 | 分层图标的背景图片选项。 |
| mask | DrawableDescriptor | 否 | 分层图标的遮罩选项。 |

#### getForeground

getForeground(): DrawableDescriptor

获取前景的DrawableDescriptor对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| DrawableDescriptor | DrawableDescriptor对象。 |

**示例：**

```ets
import { DrawableDescriptor, LayeredDrawableDescriptor } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State drawableDescriptor: DrawableDescriptor | undefined = undefined;

  private getForeground(): DrawableDescriptor | undefined {
    let resManager = this.getUIContext().getHostContext()?.resourceManager;
    // $r('app.media.drawable')需要替换为开发者所需的图像资源文件。
    let drawable: DrawableDescriptor | undefined = resManager?.getDrawableDescriptor($r('app.media.drawable').id);
    if (!drawable) {
      return undefined;
    }
    if (drawable instanceof LayeredDrawableDescriptor) {
      let layeredDrawableDescriptor = (drawable as LayeredDrawableDescriptor).getForeground();
      return layeredDrawableDescriptor;
    }
    return undefined;
  }

  aboutToAppear(): void {
    this.drawableDescriptor = this.getForeground();
  }

  build() {
    RelativeContainer() {
      if (this.drawableDescriptor) {
        Image(this.drawableDescriptor)
          .width(100)
          .height(100)
          .borderWidth(1)
          .backgroundColor(Color.Green);
      }
    .height('100%')
    .width('100%')
}
```

#### getBackground

getBackground(): DrawableDescriptor

获取背景的DrawableDescriptor对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| DrawableDescriptor | DrawableDescriptor对象。 |

**示例：**

```ets
import { DrawableDescriptor, LayeredDrawableDescriptor } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State drawableDescriptor: DrawableDescriptor | undefined = undefined;

  private getBackground(): DrawableDescriptor | undefined {
    let resManager = this.getUIContext().getHostContext()?.resourceManager;
    // $r('app.media.drawable')需要替换为开发者所需的图像资源文件。
    let drawable: DrawableDescriptor | undefined = resManager?.getDrawableDescriptor($r('app.media.drawable').id);
    if (!drawable) {
      return undefined;
    }
    let layeredDrawableDescriptor = (drawable as LayeredDrawableDescriptor).getBackground();
    return layeredDrawableDescriptor;
  }

  aboutToAppear(): void {
    this.drawableDescriptor = this.getBackground();
  }

  build() {
    RelativeContainer() {
      if (this.drawableDescriptor) {
        Image(this.drawableDescriptor)
          .width(100)
          .height(100)
      }
    .height('100%')
    .width('100%')
}
```

#### getMask

getMask(): DrawableDescriptor

获取蒙版的DrawableDescriptor对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| DrawableDescriptor | DrawableDescriptor对象。 |

**示例：**

```ets
import { DrawableDescriptor, LayeredDrawableDescriptor } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State drawableDescriptor: DrawableDescriptor | undefined = undefined;

  private getMask(): DrawableDescriptor | undefined {
    let resManager = this.getUIContext().getHostContext()?.resourceManager;
    // $r('app.media.drawable')需要替换为开发者所需的图像资源文件。
    let drawable: DrawableDescriptor | undefined = resManager?.getDrawableDescriptor($r('app.media.drawable').id);
    if (!drawable) {
      return undefined;
    }
    let layeredDrawableDescriptor = (drawable as LayeredDrawableDescriptor).getMask();
    return layeredDrawableDescriptor;
  }

  aboutToAppear(): void {
    this.drawableDescriptor = this.getMask();
  }

  build() {
    RelativeContainer() {
      if (this.drawableDescriptor) {
        Image(this.drawableDescriptor)
          .width(100)
          .height(100)
      }
    .height('100%')
    .width('100%')
}
```

#### getMaskClipPath

static getMaskClipPath(): string

LayeredDrawableDescriptor的静态方法，获取系统内置的裁切路径参数。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回裁切路径的命令字符串。 |

**示例：**

```ets
// xxx.ets
import { DrawableDescriptor, LayeredDrawableDescriptor } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        // $r('app.media.icon')需要替换为开发者所需的图像资源文件。
        Image($r('app.media.icon'))
          .width('200px').height('200px')
          .clipShape(new Path({commands:LayeredDrawableDescriptor.getMaskClipPath()}))
        Text(`获取系统内置的裁剪路径参数：`)
          .fontWeight(800)
        Text(JSON.stringify(LayeredDrawableDescriptor.getMaskClipPath()))
          .padding({ left: 20, right: 20 })
      }.height('100%').justifyContent(FlexAlign.Center)
    }.width('100%')
  }
```

**setBlendMode23+**

setBlendMode(mode: drawing.BlendMode): void

设置LayeredDrawableDescriptor的混合模式。对同一LayeredDrawableDescriptor对象多次调用setBlendMode接口时，仅在绘制完成前的最后一次调用生效。该接口不支持动态切换。LayeredDrawableDescriptor的默认绘制顺序为背景、蒙版、前景。设置了混合模式后，绘制顺序变为背景、前景、蒙版。若设置的值无效，则按照未设置混合模式进行绘制。

元服务API： 从API version 23开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | drawing.BlendMode | 是 | 混合模式。 |

示例：

```ets
import { DrawableDescriptor, LayeredDrawableDescriptor } from '@kit.ArkUI';
import { image } from '@kit.ImageKit';
import { drawing } from '@kit.ArkGraphics2D';

@Entry
@Component
struct Index {
  @State drawableDescriptor: DrawableDescriptor | undefined = undefined;

  private setBlendMode(blendMode: drawing.BlendMode): DrawableDescriptor | undefined {
    let resManager = this.getUIContext().getHostContext()?.resourceManager;
    // $r('app.media.drawable')需要替换为开发者提供的分层图标文件。
    let drawable: DrawableDescriptor | undefined = resManager?.getDrawableDescriptor($r('app.media.drawable').id);
    if (!drawable) {
      return undefined;
    }
    let layeredDrawableDescriptor = drawable as LayeredDrawableDescriptor;
    layeredDrawableDescriptor.setBlendMode(blendMode);
    return layeredDrawableDescriptor;
  }

  aboutToAppear(): void {
    this.drawableDescriptor = this.setBlendMode(drawing.BlendMode.SRC_OVER);
  }

  build() {
    RelativeContainer() {
      if (this.drawableDescriptor) {
        Image(this.drawableDescriptor)
          .width(100)
          .height(100)
      }
    .height('100%')
    .width('100%')
}
```

#### AnimationOptions12+

动画播放参数。包括播放时延，迭代次数，单帧播放时间，是否自动播放。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| duration | number | 否 | 是 | 设置图片数组播放总时间。 PixelMap数组的默认值是每张图片播放1秒。本地图片或者应用资源的默认值是图片资源中携带的播放时延。 单位：毫秒  取值范围：[0, +∞) 设置负数取默认值。  元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| iterations | number | 否 | 是 | 设置图片数组播放次数。 值为-1时表示无限播放，值为0时表示不播放，值大于0时表示有限的播放次数。 默认值为1。  元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| frameDurations21+ | Array<number> | 否 | 是 | 设置动图中的单帧播放时间。不设置则按照总时间播放。 设置的优先级高于duration，即同时设置了duration和frameDurations时，duration不生效。 当设置的frameDurations长度与图片的数量不一致时，按照总时间播放。 单位：毫秒  元服务API： 从API version 21开始，该接口支持在元服务中使用。 |
| autoPlay21+ | boolean | 否 | 是 | 设置动图是否自动播放。  true表示自动播放，false表示不自动播放。 默认值为true。  元服务API： 从API version 21开始，该接口支持在元服务中使用。 |

**示例：**

```ets
import { AnimationOptions, AnimatedDrawableDescriptor } from '@kit.ArkUI';
import { image } from '@kit.ImageKit';

@Entry
@Component
struct Example {
  pixelMaps: Array<image.PixelMap> = [];
  // 设置了4张图，同时设置4张图的duration。
  options: AnimationOptions = {
    duration: 2000,
    iterations: 1,
    frameDurations: [20, 30, 40, 50],
    autoPlay: true
  };
  @State animated?: DrawableDescriptor = undefined;

  aboutToAppear() {
    // $r('app.media.png1')需要替换为开发者所需的图像资源文件。
    this.pixelMaps.push(this.getPixmapFromMedia($r('app.media.png1')));
     // $r('app.media.png2')需要替换为开发者所需的图像资源文件。
    this.pixelMaps.push(this.getPixmapFromMedia($r('app.media.png2')));
     // $r('app.media.png3')需要替换为开发者所需的图像资源文件。
    this.pixelMaps.push(this.getPixmapFromMedia($r('app.media.png3')));
     // $r('app.media.png4')需要替换为开发者所需的图像资源文件。
    this.pixelMaps.push(this.getPixmapFromMedia($r('app.media.png4')));
    this.animated = new AnimatedDrawableDescriptor(this.pixelMaps, this.options);
  }

  build() {
    Column() {
      Row() {
        Image(this.animated)
          .width(100)
          .height(100)
      }

  private getPixmapFromMedia(resource: Resource) {
    let unit8Array = this.getUIContext().getHostContext()?.resourceManager?.getMediaContentSync(resource.id);
    let imageSource = image.createImageSource(unit8Array?.buffer.slice(0, unit8Array.buffer.byteLength));
    let pixelMap: image.PixelMap = imageSource.createPixelMapSync({
      desiredPixelFormat: image.PixelMapFormat.RGBA_8888
    });
    imageSource.release();
    return pixelMap;
  }
```

#### AnimatedDrawableDescriptor12+

使用[Image](Image.md)组件播放PixelMap数组或动图资源时传入AnimatedDrawableDescriptor对象，该对象继承自[DrawableDescriptor](#ZH-CN_TOPIC_0000002553200683__drawabledescriptor)。

#### constructor12+

constructor(pixelMaps: Array<image.PixelMap>, options?: AnimationOptions)

AnimatedDrawableDescriptor的构造函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pixelMaps | Array<image.PixelMap> | 是 | PixelMap 数组类型参数，存储 PixelMap 图片数据。 |
| options | AnimationOptions | 否 | 动画控制选项。 |

#### constructor21+

constructor(src: [ResourceStr](../../topics/components/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcestr) | Array<image.PixelMap>, options?: AnimationOptions)

AnimatedDrawableDescriptor的构造函数。

**元服务API：** 从API version 21开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src | [ResourceStr](../../topics/components/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcestr) | Array<image.PixelMap> | 是 | 动图资源地址或者PixelMap对象构成的数组。  ResourceStr当前支持的范围：应用资源Resource，沙箱路径（file://<bundleName>/<sandboxPath>），BASE64字符串。 |
| options | AnimationOptions | 否 | 动画控制参数。 |

**示例：**

```ets
import { AnimationOptions, AnimatedDrawableDescriptor } from '@kit.ArkUI';
import { fileUri } from '@kit.CoreFileKit';

@Entry
@Component
struct Example {
  options: AnimationOptions = { duration: 1000, iterations: -1, autoPlay: false };
  // 支持传入file://xx沙箱路径和应用资源Resource。
  @State animated1: AnimatedDrawableDescriptor = new AnimatedDrawableDescriptor($r('app.media.gif'), this.options);
  @State animated2: AnimatedDrawableDescriptor | undefined = undefined;

  aboutToAppear() {
    let files = this.getUIContext().getHostContext()?.filesDir
    let originPath = files + "/flower.gif"
    let resultPath = fileUri.getUriFromPath(originPath)
    this.animated2 = new AnimatedDrawableDescriptor(resultPath, { iterations: -1 })
  }

  build() {
    Column() {
      Row() {
        Image(this.animated1).width(100).height(100)
        Image(this.animated2).width(100).height(100)
      }
```

#### getAnimationController21+

getAnimationController(id?: string): AnimationController | undefined

获取动画控制器。

**元服务API：** 从API version 21开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | string | 否 | 组件的id。 当[Image](../../types/interfaces/Image.md)组件与AnimatedDrawableDescriptor确保1比1持有（仅传入一个Image组件）时，id非必填； 若同一AnimatedDrawableDescriptor需绑定多个Image组件，则必须设置唯一id以准确获取对应组件的动画控制器（唯一性由开发者保证）。 此规则基于动画系统设计原则：动画数据可多组件共享，但各组件动画独立运行，AnimationController与组件严格1比1持有关系（一个组件一个AnimationController对象）。 另外，AnimatedDrawableDescriptor支持不可见时自动暂停播放功能，详见[onVisibleAreaChange](../../topics/components/组件可见区域变化事件.md#ZH-CN_TOPIC_0000002497444844__onvisibleareachange)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| AnimationController | undefined | 动画控制器对象。 |

**示例：**

[Image](Image.md)组件与AnimatedDrawableDescriptor保持1比1持有关系，示例代码如下。

```ets
import { AnimationOptions, AnimatedDrawableDescriptor, AnimationController } from '@kit.ArkUI';

@Entry
@Component
struct Example {
  options: AnimationOptions = { duration: 1000, iterations: -1, autoPlay: false };
  // $r('app.media.gif')需要替换为开发者所需的图像资源文件。
  @State animated: AnimatedDrawableDescriptor = new AnimatedDrawableDescriptor($r('app.media.gif'), this.options);

  build() {
    Column() {
      Image(this.animated)
        .width(100)
        .height(100)
        .borderColor(Color.Red)
        .borderWidth(1)
      Button("start")
        .onClick(() => {
          let controller = this.animated.getAnimationController()
          controller?.start()
        })
      Button("stop")
        .onClick(() => {
          let controller = this.animated.getAnimationController()
          controller?.stop()
        })
    }
```

[Image](Image.md)组件与AnimatedDrawableDescriptor保持1比N持有关系，示例代码如下。

```ets
import { AnimationOptions, AnimatedDrawableDescriptor, AnimationController } from '@kit.ArkUI';

@Entry
@Component
struct Example {
  options: AnimationOptions = { duration: 1000, iterations: -1, autoPlay: false };
  // $r('app.media.gif')需要替换为开发者所需的图像资源文件。
  @State animated: AnimatedDrawableDescriptor = new AnimatedDrawableDescriptor($r('app.media.gif'), this.options);

  build() {
    Column() {
      Image(this.animated)
        .width(100)
        .height(100)
        .borderColor(Color.Red)
        .borderWidth(1)
        .id("Component1")
      Image(this.animated)
        .width(100)
        .height(100)
        .borderColor(Color.Red)
        .borderWidth(1)
      Button("start")
        .onClick(() => {
          let controller = this.animated.getAnimationController("Component1")
          controller?.start()
        })
      Button("stop")
        .onClick(() => {
          let controller = this.animated.getAnimationController("Component1")
          controller?.stop()
        })
    }
```

#### AnimationController21+

动画控制器对象。包含控制动画播放、停止、恢复、暂停和状态查询等方法。

#### start21+

start(): void

从首帧开始播放。

**元服务API：** 从API version 21开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```ets
import { AnimationOptions, AnimatedDrawableDescriptor } from '@kit.ArkUI';

@Entry
@Component
struct Example {
  options: AnimationOptions = { duration: 1000, iterations: -1, autoPlay: false };
  // $r('app.media.gif')需要替换为开发者所需的图像资源文件。
  @State animated: AnimatedDrawableDescriptor = new AnimatedDrawableDescriptor($r('app.media.gif'), this.options);

  build() {
    Column() {
      Image(this.animated)
        .width(100)
        .height(100)
        .onClick(() => {
          let controller = this.animated.getAnimationController()
          // 可以通过start启动动图播放。
          controller?.start()
        })
    }
```

#### stop21+

stop(): void

停止动图的播放并回到首帧。

**元服务API：** 从API version 21开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```ets
import { AnimationOptions, AnimatedDrawableDescriptor } from '@kit.ArkUI';

@Entry
@Component
struct Example {
  options: AnimationOptions = { duration: 1000, iterations: -1 };
  // $r('app.media.gif')需要替换为开发者所需的图像资源文件。
  @State animated: AnimatedDrawableDescriptor = new AnimatedDrawableDescriptor($r('app.media.gif'), this.options);

  build() {
    Column() {
      Image(this.animated)
        .width(100)
        .height(100)
        .onClick(() => {
          let controller = this.animated.getAnimationController()
          // 可以在动图播放时，通过stop停下播放并回到动图的首帧。
          controller?.stop()
        })
}
```

#### resume21+

resume(): void

在当前帧恢复播放动图。

**元服务API：** 从API version 21开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```ets
import { AnimationOptions, AnimatedDrawableDescriptor } from '@kit.ArkUI';

@Entry
@Component
struct Example {
  options: AnimationOptions = { duration: 1000, iterations: -1 };
  // $r('app.media.gif')需要替换为开发者所需的图像资源文件。
  @State animated: AnimatedDrawableDescriptor = new AnimatedDrawableDescriptor($r('app.media.gif'), this.options);

  build() {
    Column() {
      Image(this.animated)
        .width(100)
        .height(100)
        .onClick(() => {
          let controller = this.animated.getAnimationController()
          // 可以在动图暂停或停止时从当前帧开始播放。
          controller?.resume()
        })
    }
```

#### pause21+

pause(): void

暂停动图的播放，保持在当前帧。

**元服务API：** 从API version 21开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```ets
import { AnimationOptions, AnimatedDrawableDescriptor } from '@kit.ArkUI';

@Entry
@Component
struct Example {
  options: AnimationOptions = { duration: 1000, iterations: -1 };
  // $r('app.media.gif')需要替换为开发者所需的图像资源文件。
  @State animated: AnimatedDrawableDescriptor = new AnimatedDrawableDescriptor($r('app.media.gif'), this.options);

  build() {
    Column() {
      Image(this.animated)
        .width(100)
        .height(100)
        .onClick(() => {
          let controller = this.animated.getAnimationController()
          // 可以在动图播放时，暂停播放并保持在当前帧。
          controller?.pause()
        })
    }
```

#### getStatus21+

getStatus(): [AnimationStatus](../../topics/components/枚举说明.md#ZH-CN_TOPIC_0000002529284967__animationstatus)

获取当前动图播放的状态。

**元服务API：** 从API version 21开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AnimationStatus](../../topics/components/枚举说明.md#ZH-CN_TOPIC_0000002529284967__animationstatus) | 动图的播放状态。包含4种状态：初始态、播放态、暂停态、停止态。 |

**示例：**

```ets
import { AnimationOptions, AnimatedDrawableDescriptor } from '@kit.ArkUI';

@Entry
@Component
struct Example {
  options: AnimationOptions = { duration: 1000, iterations: -1 };
  // $r('app.media.gif')需要替换为开发者所需的图像资源文件。
  @State animated: AnimatedDrawableDescriptor = new AnimatedDrawableDescriptor($r('app.media.gif'), this.options);

  statusToString(status: AnimationStatus): string {
    switch (status) {
      case AnimationStatus.Initial:
        return "Initial"
      case AnimationStatus.Running:
        return "Running"
      case AnimationStatus.Paused:
        return "Paused"
      case AnimationStatus.Stopped:
        return "Stopped"
      default:
        return "Error"
    }

  build() {
    Column() {
      Image(this.animated)
        .width(100)
        .height(100)
        .onClick(() => {
          let controller = this.animated.getAnimationController()
          // 获取当前动画的状态。
          let status = controller?.getStatus()
          console.info(`animation status = ${this.statusToString(status)}`)
        })
    }
```