# Class (ImageFilter)

图像滤波器。

-

本模块首批接口从API version 11开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

-

本Class首批接口从API version 12开始支持。

-

本模块使用屏幕物理像素单位px。

-

本模块为单线程模型策略，需要调用方自行管理线程安全和上下文状态的切换。

#### 导入模块

```ets
import { drawing } from '@kit.ArkGraphics2D';
```

#### createBlurImageFilter12+

static createBlurImageFilter(sigmaX: number, sigmaY: number, tileMode: TileMode, imageFilter?: ImageFilter | null ): ImageFilter

创建具有模糊效果的图像滤波器。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

参数名类型必填说明sigmaXnumber是表示沿x轴方向上高斯模糊的标准差，必须大于0，该参数为浮点数。sigmaYnumber是表示沿y轴方向上高斯模糊的标准差，必须大于0，该参数为浮点数。tileMode[TileMode](Enums.md#ZH-CN_TOPIC_0000002529285977__tilemode12)是表示在边缘处应用的平铺模式。imageFilter[ImageFilter](Class (ImageFilter).md) | null否要与当前图像滤波器叠加的输入滤波器，默认为null，表示直接将当前图像滤波器作用于原始图像。

**返回值：**

类型说明[ImageFilter](Class (ImageFilter).md)返回创建的图像滤波器。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types;3.Parameter verification failed.

**示例：**

```ets
import { drawing } from '@kit.ArkGraphics2D';

let imgFilter = drawing.ImageFilter.createBlurImageFilter(5, 10, drawing.TileMode.CLAMP);
```

#### createFromImage20+

static createFromImage(pixelmap: image.PixelMap, srcRect?: common2D.Rect | null, dstRect?: common2D.Rect | null): ImageFilter

基于给定的图像创建一个图像滤波器。此接口不建议用于录制类型的画布，会影响性能。

**系统能力**：SystemCapability.Graphics.Drawing

**参数：**

参数名类型必填说明pixelmap[image.PixelMap](Interface (PixelMap).md)是图片对象。srcRect[common2D.Rect](@ohos.graphics.common2D (2D图形通用数据类型).md#ZH-CN_TOPIC_0000002529445937__rect) | null否可选参数，默认为空。图片要被此滤波器使用的像素区域，如果为空，则使用pixelmap全部区域。dstRect[common2D.Rect](@ohos.graphics.common2D (2D图形通用数据类型).md#ZH-CN_TOPIC_0000002529445937__rect) | null否可选参数，默认为空。要进行渲染的区域，如果为空，则和srcRect保持一致。

**返回值：**

类型说明[ImageFilter](Class (ImageFilter).md)返回创建的图像滤波器。

**示例：**

```ets
import { RenderNode } from '@kit.ArkUI';
import { image } from '@kit.ImageKit';
import { common2D, drawing } from '@kit.ArkGraphics2D';
class DrawingRenderNode extends RenderNode {
  draw(context : DrawContext) {
    const width = 1000;
    const height = 1000;
    const bufferSize = width * height * 4;
    const color: ArrayBuffer = new ArrayBuffer(bufferSize);

    const colorData = new Uint8Array(color);
    for (let i = 0; i < colorData.length; i += 4) {
      colorData[i] = 255;
      colorData[i+1] = 156;
      colorData[i+2] = 0;
      colorData[i+3] = 255;
    }

    let opts : image.InitializationOptions = {
      editable: true,
      pixelFormat: 3,
      size: { height, width }
    }

    let pixelMap: image.PixelMap = image.createPixelMapSync(color, opts);
    let srcRect: common2D.Rect = { left: 10, top: 10, right: 80, bottom: 80 };
    let dstRect: common2D.Rect = { left: 200, top: 200, right: 400, bottom: 400 };
    if (pixelMap != null) {
      let filter = drawing.ImageFilter.createFromImage(pixelMap, srcRect, dstRect);
    }
  }
}
```

#### createBlendImageFilter20+

static createBlendImageFilter(mode: BlendMode, background: ImageFilter, foreground: ImageFilter): ImageFilter

按照指定的混合模式对两个滤波器进行叠加，生成一个新的滤波器。

**系统能力**：SystemCapability.Graphics.Drawing

**参数：**

参数名类型必填说明mode[BlendMode](Enums.md#ZH-CN_TOPIC_0000002529285977__blendmode)是颜色混合模式。background[ImageFilter](Class (ImageFilter).md)是在混合模式中作为目标色的滤波器。foreground[ImageFilter](Class (ImageFilter).md)是在混合模式中作为源色的滤波器。

**返回值：**

类型说明[ImageFilter](Class (ImageFilter).md)返回创建的图像滤波器。

**错误码：**

以下错误码的详细介绍请参见[图形绘制与显示错误码](图形绘制与显示错误码.md)。

错误码ID错误信息25900001Parameter error.Possible causes: Incorrect parameter range.

**示例：**

```ets
import { drawing } from '@kit.ArkGraphics2D';

let dx = 15.0;
let dy = 10.0;
let offsetFilter1 = drawing.ImageFilter.createOffsetImageFilter(dx, dy, null);
let x = 15.0;
let y = 30.0;
let offsetFilter2 = drawing.ImageFilter.createOffsetImageFilter(x, y, null);
let blendImageFilter = drawing.ImageFilter.createBlendImageFilter(drawing.BlendMode.SRC_IN, offsetFilter1, offsetFilter2);
```

#### createComposeImageFilter20+

static createComposeImageFilter(cOuter: ImageFilter, cInner: ImageFilter): ImageFilter

将两个图像滤波器进行级联生成新的图像滤波器，级联时会将第一级滤波器的输出作为第二级滤波器的输入，经过第二级滤波器处理后，输出最终的滤波结果。

**系统能力**：SystemCapability.Graphics.Drawing

**参数：**

参数名类型必填说明cOuter[ImageFilter](Class (ImageFilter).md)是在级联中，作为第二级的滤波器，处理第一级滤波器的输出。如果第二级滤波器为空，第一级滤波器不为空，最后输出第一级滤波器的结果。两级滤波器不能同时为空。cInner[ImageFilter](Class (ImageFilter).md)是在级联中，作为第一级的滤波器，直接处理图像的原始内容。如果第一级滤波器为空，第二级滤波器不为空，最后输出第二级滤波器的结果。两级滤波器不能同时为空。

**返回值：**

类型说明[ImageFilter](Class (ImageFilter).md)返回创建的图像滤波器。

**示例：**

```ets
import { drawing } from '@kit.ArkGraphics2D';

let blurSigmaX = 10.0;
let blurSigmaY = 10.0;
let blurFilter = drawing.ImageFilter.createBlurImageFilter(blurSigmaX, blurSigmaY, drawing.TileMode.CLAMP, null);
let colorMatrix:Array<number> = [
  0, 0, 0, 0, 0,
  0, 1, 0, 0, 0,
  0, 0, 1, 0, 0,
  0, 0, 0, 1, 0
];
let redRemovalFilter = drawing.ColorFilter.createMatrixColorFilter(colorMatrix);
let colorFilter = drawing.ImageFilter.createFromColorFilter(redRemovalFilter, null);
let composedImageFilter = drawing.ImageFilter.createComposeImageFilter(colorFilter, blurFilter);
```

#### createFromColorFilter12+

static createFromColorFilter(colorFilter: ColorFilter, imageFilter?: ImageFilter | null): ImageFilter

创建一个将颜色滤波器应用于传入的图像滤波器的图像滤波器。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

参数名类型必填说明colorFilter[ColorFilter](Class (ColorFilter).md)是表示颜色滤波器。imageFilter[ImageFilter](Class (ImageFilter).md) | null否要与当前图像滤波器叠加的输入滤波器，默认为null，表示直接将当前图像滤波器作用于原始图像。

**返回值：**

类型说明[ImageFilter](Class (ImageFilter).md)返回创建的图像滤波器。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error.Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.

**示例：**

```ets
import { drawing } from '@kit.ArkGraphics2D';
let imgFilter = drawing.ImageFilter.createBlurImageFilter(5, 10, drawing.TileMode.CLAMP);
let colorFilter = drawing.ColorFilter.createSRGBGammaToLinear();
let imgFilter1 = drawing.ImageFilter.createFromColorFilter(colorFilter, imgFilter);
```

#### createOffsetImageFilter20+

static createOffsetImageFilter(dx: number, dy: number, input?: ImageFilter | null): ImageFilter

创建一个偏移滤波器，将输入的滤波器按照指定向量进行平移。

**系统能力**：SystemCapability.Graphics.Drawing

**参数：**

参数名类型必填说明dxnumber是水平方向的平移距离， 该参数为浮点数。dynumber是竖直方向的平移距离， 该参数为浮点数。input[ImageFilter](Class (ImageFilter).md) | null否需进行平移的滤波器。默认为空，如果为空，则将无滤波效果的绘制结果进行平移。

**返回值：**

类型说明[ImageFilter](Class (ImageFilter).md)返回创建的图像滤波器。

**示例：**

```ets
import { drawing } from '@kit.ArkGraphics2D';

let dx = 15.0;
let dy = 10.0;
let offsetFilter = drawing.ImageFilter.createOffsetImageFilter(dx, dy, null);
```

#### createFromShaderEffect20+

static createFromShaderEffect(shader: ShaderEffect): ImageFilter

基于着色器创建一个图像滤波器。

**系统能力**：SystemCapability.Graphics.Drawing

**参数：**

参数名类型必填说明shader[ShaderEffect](Class (ShaderEffect).md)是表示应用于图像的着色器效果。

**返回值：**

类型说明[ImageFilter](Class (ImageFilter).md)返回创建的图像滤波器。

**示例：**

```ets
import { drawing } from '@kit.ArkGraphics2D';

let shaderEffect = drawing.ShaderEffect.createColorShader(0xFF00FF00);
let renderEffect = drawing.ImageFilter.createFromShaderEffect(shaderEffect);
```