# CanvasRenderingContext2D

使用RenderingContext在Canvas组件上进行绘制，绘制对象可以是矩形、文本、图片等。

从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

本文绘制接口在调用时会存入被关联的Canvas组件的指令队列中。仅当当前帧进入渲染阶段且关联的Canvas组件处于可见状态时，这些指令才会从队列中被提取并执行。因此，在Canvas组件不可见的情况下，应尽量避免频繁调用绘制接口，以防止指令在队列中堆积，从而避免内存占用过大的问题，具体示例请参考[控制在画布组件不可见时不进行绘制](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-drawing-customization-on-canvas#控制在画布组件不可见时不进行绘制)。

[beginPath](#ZH-CN_TOPIC_0000002497444936__beginpath)、[moveTo](#ZH-CN_TOPIC_0000002497444936__moveto)、[lineTo](#ZH-CN_TOPIC_0000002497444936__lineto)、[closePath](#ZH-CN_TOPIC_0000002497444936__closepath)、[bezierCurveTo](#ZH-CN_TOPIC_0000002497444936__beziercurveto)、[quadraticCurveTo](#ZH-CN_TOPIC_0000002497444936__quadraticcurveto)、[arc](#ZH-CN_TOPIC_0000002497444936__arc)、[arcTo](#ZH-CN_TOPIC_0000002497444936__arcto)、[ellipse](#ZH-CN_TOPIC_0000002497444936__ellipse)、[rect](#ZH-CN_TOPIC_0000002497444936__rect)和[roundRect](#ZH-CN_TOPIC_0000002497444936__roundrect20)接口只能对CanvasRenderingContext2D中的路径生效，无法对[OffscreenCanvasRenderingContext2D](zh-cn_topic_0000002529444883.html)和[Path2D](Path2D.md)对象中设置的路径生效。

Canvas组件的宽或高超过8000px时使用CPU渲染，会导致性能明显下降。

#### 构造函数

#### constructor

constructor(settings?: RenderingContextSettings)

构造Canvas画布对象，支持配置CanvasRenderingContext2D对象的参数。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 在API version 11中，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明settings[RenderingContextSettings](#ZH-CN_TOPIC_0000002497444936__renderingcontextsettings)否

用来配置CanvasRenderingContext2D对象的参数，见[RenderingContextSettings](#ZH-CN_TOPIC_0000002497444936__renderingcontextsettings)。

异常值undefined和null按[RenderingContextSettings](#ZH-CN_TOPIC_0000002497444936__renderingcontextsettings)的默认值处理。

#### constructor12+

constructor(settings?: RenderingContextSettings, unit?: LengthMetricsUnit)

构造Canvas画布对象，支持配置CanvasRenderingContext2D对象的参数和单位模式。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 在API version 12中，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明settings[RenderingContextSettings](#ZH-CN_TOPIC_0000002497444936__renderingcontextsettings)否

用来配置CanvasRenderingContext2D对象的参数，见[RenderingContextSettings](#ZH-CN_TOPIC_0000002497444936__renderingcontextsettings)。

异常值undefined和null按[RenderingContextSettings](#ZH-CN_TOPIC_0000002497444936__renderingcontextsettings)的默认值处理。

unit[LengthMetricsUnit](Graphics.md#ZH-CN_TOPIC_0000002529444761__lengthmetricsunit12)否

用来配置CanvasRenderingContext2D对象的单位模式，配置后无法更改。

异常值undefined、NaN和Infinity按默认值处理。

默认值：DEFAULT

**示例：**

以下示例展示了配置CanvasRenderingContext2D对象的单位模式，默认单位模式为LengthMetricsUnit.DEFAULT，对应默认单位vp，配置后无法动态更改。详细说明见[LengthMetricsUnit](Graphics.md#ZH-CN_TOPIC_0000002529444761__lengthmetricsunit12)。

```ets
// xxx.ets
import { LengthMetricsUnit } from '@kit.ArkUI'

@Entry
@Component
struct LengthMetricsUnitDemo {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private contextPX: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings, LengthMetricsUnit.PX);
  private contextVP: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.contextPX)
        .width('100%')
        .height(150)
        .backgroundColor('#ffff00')
        .onReady(() => {
          this.contextPX.fillRect(10,10,100,100)
          this.contextPX.clearRect(10,10,50,50)
        })

      Canvas(this.contextVP)
        .width('100%')
        .height(150)
        .backgroundColor('#ffff00')
        .onReady(() => {
          this.contextVP.fillRect(10,10,100,100)
          this.contextVP.clearRect(10,10,50,50)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

#### 属性

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明[fillStyle](#ZH-CN_TOPIC_0000002497444936__fillstyle)string |number10+ |[CanvasGradient](zh-cn_topic_0000002529444879.html) | [CanvasPattern](CanvasPattern.md)否否

指定绘制的填充色，此属性为只写属性，可通过赋值语句设置其值，但无法通过读取操作获取其当前值，若尝试读取将返回undefined。

- 类型为string时，表示设置填充区域的颜色，颜色格式参考[ResourceColor](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)中string类型说明。

- 类型为number时，表示设置填充区域的颜色，不支持设置全透明色，颜色格式参考[ResourceColor](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)中number类型说明。

- 类型为CanvasGradient时，表示渐变对象，使用[createLinearGradient](#ZH-CN_TOPIC_0000002497444936__createlineargradient)方法创建。

- 类型为CanvasPattern时，使用[createPattern](#ZH-CN_TOPIC_0000002497444936__createpattern)方法创建。

默认值：'#000000'（黑色）

异常值NaN和Infinity按默认值处理。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

[lineWidth](#ZH-CN_TOPIC_0000002497444936__linewidth)number否否

设置绘制线条的宽度，此属性为只写属性，可通过赋值语句设置其值，但无法通过读取操作获取其当前值，若尝试读取将返回undefined。

默认值：1(px)

默认单位：vp

lineWidth取值不支持0和负数，0、负数和NaN按默认值处理，Infinity会导致lineWidth属性异常。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

[strokeStyle](#ZH-CN_TOPIC_0000002497444936__strokestyle)string |number10+ |[CanvasGradient](zh-cn_topic_0000002529444879.html) | [CanvasPattern](CanvasPattern.md)否否

设置线条的颜色，此属性为只写属性，可通过赋值语句设置其值，但无法通过读取操作获取其当前值，若尝试读取将返回undefined。

- 类型为string时，表示设置线条使用的颜色，颜色格式参考[ResourceColor](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)中string类型说明。

- 类型为number时，表示设置线条使用的颜色，不支持设置全透明色，颜色格式参考[ResourceColor](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)中number类型说明。

- 类型为CanvasGradient时，表示渐变对象，使用[createLinearGradient](#ZH-CN_TOPIC_0000002497444936__createlineargradient)方法创建。

- 类型为CanvasPattern时，使用[createPattern](#ZH-CN_TOPIC_0000002497444936__createpattern)方法创建。

默认值：'#000000'（黑色）

异常值NaN和Infinity按默认值处理。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

[lineCap](#ZH-CN_TOPIC_0000002497444936__linecap)[CanvasLineCap](#ZH-CN_TOPIC_0000002497444936__canvaslinecap类型说明)否否

指定线端点的样式，此属性为只写属性，可通过赋值语句设置其值，但无法通过读取操作获取其当前值，若尝试读取将返回undefined。

可选值为：

- 'butt'：线端点以方形结束。

- 'round'：线端点以圆形结束。

- 'square'：线端点以方形结束，该样式下会增加一个长度和线段厚度相同，宽度是线段厚度一半的矩形。

默认值：'butt'

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

[lineJoin](#ZH-CN_TOPIC_0000002497444936__linejoin)[CanvasLineJoin](#ZH-CN_TOPIC_0000002497444936__canvaslinejoin类型说明)否否

指定线段间相交的交点样式，此属性为只写属性，可通过赋值语句设置其值，但无法通过读取操作获取其当前值，若尝试读取将返回undefined。

可选值为：

- 'round'：在线段相连处绘制一个扇形，扇形的圆角半径是线段的宽度。

- 'bevel'：在线段相连处使用三角形为底填充， 每个部分矩形拐角独立。

- 'miter'：在相连部分的外边缘处进行延伸，使其相交于一点，形成一个菱形区域，该属性可以通过设置miterLimit属性展现效果。

默认值：'miter'

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

[miterLimit](#ZH-CN_TOPIC_0000002497444936__miterlimit)number否否

设置斜接面限制值，该值指定了线条相交处内角和外角的距离，仅当设置了lineJoin为miter才生效，此属性为只写属性，可通过赋值语句设置其值，但无法通过读取操作获取其当前值，若尝试读取将返回undefined。

默认值：10px

单位：px

miterLimit取值不支持0和负数，0、负数和NaN按默认值处理，Infinity会导致miterLimit属性异常。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

[font](#ZH-CN_TOPIC_0000002497444936__font)string否否

设置文本绘制中的字体样式，此属性为只写属性，可通过赋值语句设置其值，但无法通过读取操作获取其当前值，若尝试读取将返回undefined。

语法：ctx.font = 'font-style font-weight font-size font-family'

- font-style(可选)，用于指定字体样式，支持如下几种样式：'normal','italic'。

- font-weight(可选)，用于指定字体的粗细，支持如下几种类型：'normal', 'bold', 'bolder', 'lighter', 100, 200, 300, 400, 500, 600, 700, 800, 900。

- font-size(可选)，指定字号和行高，单位支持px、vp。使用时需要添加单位。

- font-family(可选)，指定字体系列，支持如下几种类型：'sans-serif', 'serif', 'monospace'。API version 20及以后支持注册过的自定义字体（DevEco Studio的预览器不支持显示自定义字体），具体使用方法参考自定义字体[font](#ZH-CN_TOPIC_0000002497444936__font)示例。

默认值：'normal normal 14px sans-serif'

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

[textAlign](#ZH-CN_TOPIC_0000002497444936__textalign)[CanvasTextAlign](#ZH-CN_TOPIC_0000002497444936__canvastextalign类型说明)否否

设置文本绘制中的文本对齐方式，此属性为只写属性，可通过赋值语句设置其值，但无法通过读取操作获取其当前值，若尝试读取将返回undefined。

可选值为：

- 'left'：文本左对齐。

- 'right'：文本右对齐。

- 'center'：文本居中对齐。

- 'start'：文本对齐界线开始的地方。

- 'end'：文本对齐界线结束的地方。

ltr布局模式下'start'和'left'一致，rtl布局模式下'start'和'right'一致。

默认值：'left'

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

[textBaseline](#ZH-CN_TOPIC_0000002497444936__textbaseline)[CanvasTextBaseline](#ZH-CN_TOPIC_0000002497444936__canvastextbaseline类型说明)否否

设置文本绘制中的水平对齐方式，此属性为只写属性，可通过赋值语句设置其值，但无法通过读取操作获取其当前值，若尝试读取将返回undefined。

可选值为：

- 'alphabetic'：文本基线是标准的字母基线。

- 'top'：文本基线在文本块的顶部。

- 'hanging'：文本基线是悬挂基线。

- 'middle'：文本基线在文本块的中间。

- 'ideographic'：文字基线是表意字基线；如果字符本身超出了alphabetic基线，那么ideographic基线位置在字符本身的底部。

- 'bottom'：文本基线在文本块的底部。 与ideographic基线的区别在于ideographic基线不需要考虑下行字母。

默认值：'alphabetic'

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

[globalAlpha](#ZH-CN_TOPIC_0000002497444936__globalalpha)number否否

设置透明度，此属性为只写属性，可通过赋值语句设置其值，但无法通过读取操作获取其当前值，若尝试读取将返回undefined。

范围为[0.0, 1.0]，0.0为完全透明，1.0为完全不透明。若给定值小于0.0，则取值0.0；若给定值大于1.0，则取值1.0.

API version 18之前，设置NaN或Infinity时，在该方法后执行的绘制方法无法绘制。API version 18及以后，设置NaN或Infinity时当前接口不生效，其他传入有效参数的绘制方法正常绘制。

默认值：1.0

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

[lineDashOffset](#ZH-CN_TOPIC_0000002497444936__linedashoffset)number否否

设置画布的虚线偏移量，精度为float，仅当设置setLineDash时属性才生效，此属性为只写属性，可通过赋值语句设置其值，但无法通过读取操作获取其当前值，若尝试读取将返回undefined。

API version 18之前，设置NaN或Infinity时，设置了虚线样式的线条绘制出来是实线。API version 18及以后，设置NaN或Infinity时当前接口不生效，设置了虚线样式的线条绘制出来是虚线。

默认值：0.0

默认单位：vp

异常值NaN和Infinity按默认值处理。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

[globalCompositeOperation](#ZH-CN_TOPIC_0000002497444936__globalcompositeoperation)string否否

设置合成操作的方式，此属性为只写属性，可通过赋值语句设置其值，但无法通过读取操作获取其当前值，若尝试读取将返回undefined。

类型字段可选值有'source-over'，'source-atop'，'source-in'，'source-out'，'destination-over'，'destination-atop'，'destination-in'，'destination-out'，'lighter'，'copy'，'xor'。

默认值：'source-over'

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

[shadowBlur](#ZH-CN_TOPIC_0000002497444936__shadowblur)number否否

设置绘制阴影时的模糊级别，此属性为只写属性，可通过赋值语句设置其值，但无法通过读取操作获取其当前值，若尝试读取将返回undefined。

值越大越模糊，精度为float，取值范围≥0。

默认值：0.0

单位：px

shadowBlur取值不支持负数，负数、NaN和Infinity按默认值处理。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

[shadowColor](#ZH-CN_TOPIC_0000002497444936__shadowcolor)string否否

设置绘制阴影时的阴影颜色，此属性为只写属性，可通过赋值语句设置其值，但无法通过读取操作获取其当前值，若尝试读取将返回undefined。

颜色格式参考[ResourceColor](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)中string类型说明。

默认值：透明黑色

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

[shadowOffsetX](#ZH-CN_TOPIC_0000002497444936__shadowoffsetx)number否否

设置绘制阴影时和原有对象的水平偏移值，此属性为只写属性，可通过赋值语句设置其值，但无法通过读取操作获取其当前值，若尝试读取将返回undefined。

默认值：0.0

默认单位：vp

异常值NaN和Infinity按默认值处理。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

[shadowOffsetY](#ZH-CN_TOPIC_0000002497444936__shadowoffsety)number否否

设置绘制阴影时和原有对象的垂直偏移值，此属性为只写属性，可通过赋值语句设置其值，但无法通过读取操作获取其当前值，若尝试读取将返回undefined。

默认值：0.0

默认单位：vp

异常值NaN和Infinity按默认值处理。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

[imageSmoothingEnabled](#ZH-CN_TOPIC_0000002497444936__imagesmoothingenabled)boolean否否

用于设置绘制图片时是否进行图像平滑度调整，true为启用，false为不启用，此属性为只写属性，可通过赋值语句设置其值，但无法通过读取操作获取其当前值，若尝试读取将返回undefined。

默认值：true

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

[height](#ZH-CN_TOPIC_0000002497444936__height)number是否

组件高度。

默认单位：vp

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

[width](#ZH-CN_TOPIC_0000002497444936__width)number是否

组件宽度。

默认单位：vp

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

[imageSmoothingQuality](#ZH-CN_TOPIC_0000002497444936__imagesmoothingquality)[ImageSmoothingQuality](#ZH-CN_TOPIC_0000002497444936__imagesmoothingquality类型说明)否否

imageSmoothingEnabled为true时，用于设置图像平滑度，此属性为只写属性，可通过赋值语句设置其值，但无法通过读取操作获取其当前值，若尝试读取将返回undefined。

默认值："low"

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

[direction](#ZH-CN_TOPIC_0000002497444936__direction)[CanvasDirection](#ZH-CN_TOPIC_0000002497444936__canvasdirection类型说明)否否

用于设置绘制文字时使用的文字方向，此属性为只写属性，可通过赋值语句设置其值，但无法通过读取操作获取其当前值，若尝试读取将返回undefined。

默认值："inherit"

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

[filter](#ZH-CN_TOPIC_0000002497444936__filter)string否否

用于设置图像的滤镜，可以组合任意数量的滤镜，此属性为只写属性，可通过赋值语句设置其值，但无法通过读取操作获取其当前值，若尝试读取将返回undefined。

支持的滤镜效果如下：

- 'none': 无滤镜效果。

- 'blur(<length>)'：给图像设置高斯模糊，取值范围≥0，支持单位px、vp、rem，默认值：blur(0px)。

- 'brightness([<number>|<percentage>])'：给图片应用一种线性乘法，使其看起来更亮或更暗，支持数字和百分比参数，取值范围≥0，默认值：brightness(1)。

- 'contrast([<number>|<percentage>])'：调整图像的对比度，支持数字和百分比参数，取值范围≥0，默认值：contrast(1)。

- 'grayscale([<number>|<percentage>])'：将图像转换为灰度图像，支持数字和百分比参数，取值范围[0, 1]，默认值：grayscale(0)。

- 'hue-rotate(<angle>)'：给图像应用色相旋转，取值范围0deg-360deg，默认值：hue-rotate(0deg)。

- 'invert([<number>|<percentage>])'：反转输入图像，支持数字和百分比参数，取值范围[0, 1]，默认值：invert(0)。

- 'opacity([<number>|<percentage>])'：转化图像的透明程度，支持数字和百分比参数，取值范围[0, 1]，默认值：opacity(1)。

- 'saturate([<number>|<percentage>])'：转换图像饱和度，支持数字和百分比参数，取值范围≥0，默认值：saturate(1)。

- 'sepia([<number>|<percentage>])'：将图像转换为深褐色，支持数字和百分比参数，取值范围[0, 1]，默认值：sepia(0)。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

[canvas13+](#ZH-CN_TOPIC_0000002497444936__canvas13)[FrameNode](zh-cn_topic_0000002529284787.html)是否

获取和CanvasRenderingContext2D关联的Canvas组件的FrameNode实例。

可用于监听关联的Canvas组件的可见状态。

默认值：null

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

[letterSpacing18+](#ZH-CN_TOPIC_0000002497444936__letterspacing18)string | [LengthMetrics](zh-cn_topic_0000002529444761.html#ZH-CN_TOPIC_0000002529444761__lengthmetrics12)否否

用于指定绘制文本时字母之间的间距，此属性为只写属性，可通过赋值语句设置其值，但无法通过读取操作获取其当前值，若尝试读取将返回undefined。

当使用LengthMetrics时：

字间距按照指定的单位设置；

不支持FP、PERCENT和LPX（按无效值处理）；

支持负数和小数，设为小数时字间距不四舍五入。

当使用string时：

不支持设置百分比（按无效值处理）；

支持负数和小数，设为小数时字间距不四舍五入；

若letterSpacing的赋值未指定单位（例如：letterSpacing='10'），且未指定LengthMetricsUnit时，默认单位设置为vp；

指定LengthMetricsUnit为px时，默认单位设置为px；

当letterSpacing的赋值指定单位时（例如：letterSpacing='10vp'），字间距按照指定的单位设置。

默认值：0（输入无效值时，字间距设为默认值）

注：推荐使用LengthMetrics，性能更好。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

fillStyle、shadowColor与 strokeStyle 中string类型格式为rgb(255, 255, 255)、rgba(255, 255, 255, 1.0)或者#FFFFFF。

#### fillStyle

```ets
// xxx.ets
@Entry
@Component
struct FillStyleExample {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          this.context.fillStyle = '#0000ff'
          this.context.fillRect(20, 20, 150, 100)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

#### lineWidth

```ets
// xxx.ets
@Entry
@Component
struct LineWidthExample {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
        this.context.lineWidth = 5
        this.context.strokeRect(25, 25, 85, 105)
      })
    }
    .width('100%')
    .height('100%')
  }
}
```

#### strokeStyle

```ets
// xxx.ets
@Entry
@Component
struct StrokeStyleExample {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          this.context.lineWidth = 10
          this.context.strokeStyle = '#0000ff'
          this.context.strokeRect(25, 25, 155, 105)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

#### lineCap

```ets
// xxx.ets
@Entry
@Component
struct LineCapExample {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          this.context.lineWidth = 8
          this.context.beginPath()
          this.context.lineCap = 'round'
          this.context.moveTo(30, 50)
          this.context.lineTo(220, 50)
          this.context.stroke()
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

#### lineJoin

```ets
// xxx.ets
@Entry
@Component
struct LineJoinExample {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
        this.context.beginPath()
        this.context.lineWidth = 8
        this.context.lineJoin = 'miter'
        this.context.moveTo(30, 30)
        this.context.lineTo(120, 60)
        this.context.lineTo(30, 110)
        this.context.stroke()
      })
    }
    .width('100%')
    .height('100%')
  }
}
```

#### miterLimit

```ets
// xxx.ets
@Entry
@Component
struct MiterLimit {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          this.context.lineWidth = 8
          this.context.lineJoin = 'miter'
          this.context.miterLimit = 3
          this.context.moveTo(30, 30)
          this.context.lineTo(60, 35)
          this.context.lineTo(30, 37)
          this.context.stroke()
      })
    }
    .width('100%')
    .height('100%')
  }
}
```

#### font

自定义字体注册有以下两种方式。一种是通过ArkUI的异步接口this.uiContext.getFont().[registerFont](Class (Font).md#ZH-CN_TOPIC_0000002497604778__registerfont)注册，调用后立即绘制可能会导致自定义字体不生效。另一种是直接调用字体引擎的fontCollection.[loadFontSync](@ohos.graphics.text (文本模块).md#ZH-CN_TOPIC_0000002497605988__loadfontsync)接口来注册自定义字体到字体引擎。在直接调用字体引擎接口注册自定义字体时，fontCollection的实例需要是text.FontCollection.getGlobalInstance()，因为组件默认会从该实例加载字体。如果使用其他实例，可能会导致自定义字体不生效。

```ets
// xxx.ets
import { text } from '@kit.ArkGraphics2D';

@Entry
@Component
struct FontDemo {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('rgb(213,213,213)')
        .onReady(() => {
          // 常规字体样式，常规粗细，字体大小为30px，字体系列为sans-serif
          this.context.font = 'normal normal 30px sans-serif'
          this.context.fillText("Hello px", 20, 60)
          // 斜体样式，加粗，字体大小为30vp，字体系列为monospace
          this.context.font = 'italic bold 30vp monospace'
          this.context.fillText("Hello vp", 20, 100)
          // 加载rawfile目录下的自定义字体文件HarmonyOS_Sans_Thin_Italic.ttf
          let fontCollection = text.FontCollection.getGlobalInstance();
          fontCollection.loadFontSync('HarmonyOS_Sans_Thin_Italic', $rawfile("HarmonyOS_Sans_Thin_Italic.ttf"))
          // 加粗，字体大小为30vp，字体系列为HarmonyOS_Sans_Thin_Italic
          this.context.font = "bold 30vp HarmonyOS_Sans_Thin_Italic"
          this.context.fillText("Hello customFont", 20, 140)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

#### textAlign

```ets
// xxx.ets
@Entry
@Component
struct CanvasExample {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() => {
          this.context.strokeStyle = '#0000ff'
          this.context.moveTo(140, 10)
          this.context.lineTo(140, 160)
          this.context.stroke()
          this.context.font = '18px sans-serif'
          this.context.textAlign = 'start'
          this.context.fillText('textAlign=start', 140, 60)
          this.context.textAlign = 'end'
          this.context.fillText('textAlign=end', 140, 80)
          this.context.textAlign = 'left'
          this.context.fillText('textAlign=left', 140, 100)
          this.context.textAlign = 'center'
          this.context.fillText('textAlign=center', 140, 120)
          this.context.textAlign = 'right'
          this.context.fillText('textAlign=right', 140, 140)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

#### textBaseline

```ets
// xxx.ets
@Entry
@Component
struct TextBaseline {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('rgb(213,213,213)')
        .onReady(() => {
          this.context.strokeStyle = 'rgb(0,0,255)'
          this.context.moveTo(0, 120)
          this.context.lineTo(400, 120)
          this.context.stroke()
          this.context.font = '20px sans-serif'
          this.context.textBaseline = 'top'
          this.context.fillText('Top', 10, 120)
          this.context.textBaseline = 'bottom'
          this.context.fillText('Bottom', 55, 120)
          this.context.textBaseline = 'middle'
          this.context.fillText('Middle', 125, 120)
          this.context.textBaseline = 'alphabetic'
          this.context.fillText('Alphabetic', 195, 120)
          this.context.textBaseline = 'hanging'
          this.context.fillText('Hanging', 295, 120)
      })
    }
    .width('100%')
    .height('100%')
  }
}
```

#### globalAlpha

```ets
// xxx.ets
@Entry
@Component
struct GlobalAlpha {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          this.context.fillStyle = 'rgb(0,0,255)'
          this.context.fillRect(0, 0, 50, 50)
          this.context.globalAlpha = 0.4
          this.context.fillStyle = 'rgb(0,0,255)'
          this.context.fillRect(50, 50, 50, 50)
      })
    }
    .width('100%')
    .height('100%')
  }
}
```

#### lineDashOffset

```ets
// xxx.ets
@Entry
@Component
struct LineDashOffset {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          this.context.arc(100, 75, 50, 0, 6.28)
          this.context.setLineDash([10,20])
          this.context.lineDashOffset = 10.0
          this.context.stroke()
      })
    }
    .width('100%')
    .height('100%')
  }
}
```

#### globalCompositeOperation

名称描述source-over在现有绘制内容上显示新绘制内容，属于默认值。source-atop在现有绘制内容顶部显示新绘制内容。source-in在现有绘制内容中显示新绘制内容。source-out在现有绘制内容之外显示新绘制内容。destination-over在新绘制内容上方显示现有绘制内容。destination-atop在新绘制内容顶部显示现有绘制内容。destination-in在新绘制内容中显示现有绘制内容。destination-out在新绘制内容外显示现有绘制内容。lighter显示新绘制内容和现有绘制内容。copy显示新绘制内容而忽略现有绘制内容。xor使用异或操作对新绘制内容与现有绘制内容进行融合。

```ets
// xxx.ets
@Entry
@Component
struct GlobalCompositeOperation {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          this.context.fillStyle = 'rgb(255,0,0)'
          this.context.fillRect(20, 20, 50, 50)
          this.context.globalCompositeOperation = 'source-over'
          this.context.fillStyle = 'rgb(0,0,255)'
          this.context.fillRect(50, 50, 50, 50)
          this.context.fillStyle = 'rgb(255,0,0)'
          this.context.fillRect(120, 20, 50, 50)
          this.context.globalCompositeOperation = 'destination-over'
          this.context.fillStyle = 'rgb(0,0,255)'
          this.context.fillRect(150, 50, 50, 50)
      })
    }
    .width('100%')
    .height('100%')
  }
}
```

#### shadowBlur

```ets
// xxx.ets
@Entry
@Component
struct ShadowBlur {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          this.context.shadowBlur = 30
          this.context.shadowColor = 'rgb(0,0,0)'
          this.context.fillStyle = 'rgb(255,0,0)'
          this.context.fillRect(20, 20, 100, 80)
      })
    }
    .width('100%')
    .height('100%')
  }
}
```

#### shadowColor

```ets
// xxx.ets
@Entry
@Component
struct ShadowColor {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          this.context.shadowBlur = 30
          this.context.shadowColor = 'rgb(0,0,255)'
          this.context.fillStyle = 'rgb(255,0,0)'
          this.context.fillRect(30, 30, 100, 100)
      })
    }
    .width('100%')
    .height('100%')
  }
}
```

#### shadowOffsetX

```ets
// xxx.ets
@Entry
@Component
struct ShadowOffsetX {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          this.context.shadowBlur = 10
          this.context.shadowOffsetX = 20
          this.context.shadowColor = 'rgb(0,0,0)'
          this.context.fillStyle = 'rgb(255,0,0)'
          this.context.fillRect(20, 20, 100, 80)
      })
    }
    .width('100%')
    .height('100%')
  }
}
```

#### shadowOffsetY

```ets
// xxx.ets
@Entry
@Component
struct ShadowOffsetY {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)
  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          this.context.shadowBlur = 10
          this.context.shadowOffsetY = 20
          this.context.shadowColor = 'rgb(0,0,0)'
          this.context.fillStyle = 'rgb(255,0,0)'
          this.context.fillRect(30, 30, 100, 100)
      })
    }
    .width('100%')
    .height('100%')
  }
}
```

#### imageSmoothingEnabled

```ets
// xxx.ets
@Entry
@Component
struct ImageSmoothingEnabled {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)
  // "common/images/icon.jpg"需要替换为开发者所需的图像资源文件
  private img:ImageBitmap = new ImageBitmap("common/images/icon.jpg")

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          this.context.imageSmoothingEnabled = false
          this.context.drawImage( this.img,0,0,400,200)
      })
    }
    .width('100%')
    .height('100%')
  }
}
```

#### height

```ets
// xxx.ets
@Entry
@Component
struct HeightExample {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width(300)
        .height(300)
        .backgroundColor('#ffff00')
        .onReady(() => {
          let h = this.context.height
          this.context.fillRect(0, 0, 300, h/2)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

#### width

```ets
// xxx.ets
@Entry
@Component
struct WidthExample {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width(300)
        .height(300)
        .backgroundColor('#ffff00')
        .onReady(() => {
          let w = this.context.width
          this.context.fillRect(0, 0, w/2, 300)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

#### canvas13+

```ets
import { FrameNode } from '@kit.ArkUI'
// xxx.ets
@Entry
@Component
struct CanvasExample {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)
  private text: string = ''

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() => {
          let node: FrameNode = this.context.canvas
          node?.commonEvent.setOnVisibleAreaApproximateChange(
            { ratios: [0, 1], expectedUpdateInterval: 10},
            (isVisible: boolean, currentRatio: number) => {
              if (!isVisible && currentRatio <= 0.0) {
                this.text = 'Canvas is completely invisible.'
              }
              if (isVisible && currentRatio >= 1.0) {
                this.text = 'Canvas is fully visible.'
              }
              this.context.reset()
              this.context.font = '30vp sans-serif'
              this.context.fillText(this.text, 50, 50)
            }
          )
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

#### imageSmoothingQuality

```ets
  // xxx.ets
  @Entry
  @Component
  struct ImageSmoothingQualityDemo {
    private settings: RenderingContextSettings = new RenderingContextSettings(true);
    private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
    // "common/images/example.jpg"需要替换为开发者所需的图像资源文件
    private img:ImageBitmap = new ImageBitmap("common/images/example.jpg");

    build() {
      Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
        Canvas(this.context)
          .width('100%')
          .height('100%')
          .backgroundColor('#ffff00')
          .onReady(() =>{
            let ctx = this.context
            ctx.imageSmoothingEnabled = true
            ctx.imageSmoothingQuality = 'high'
            ctx.drawImage(this.img, 0, 0, 400, 200)
          })
      }
      .width('100%')
      .height('100%')
    }
  }
```

#### direction

```ets
  // xxx.ets
  @Entry
  @Component
  struct DirectionDemo {
    private settings: RenderingContextSettings = new RenderingContextSettings(true);
    private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);

    build() {
      Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
        Canvas(this.context)
          .width('100%')
          .height('100%')
          .backgroundColor('#ffff00')
          .onReady(() =>{
            let ctx = this.context
            ctx.font = '48px serif';
            ctx.textAlign = 'start'
            ctx.fillText("Hi ltr!", 200, 50);

            ctx.direction = "rtl";
            ctx.fillText("Hi rtl!", 200, 100);
          })
      }
      .width('100%')
      .height('100%')
    }
  }
```

#### filter

```ets
  // xxx.ets
  @Entry
  @Component
  struct FilterDemo {
    private settings: RenderingContextSettings = new RenderingContextSettings(true);
    private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
    // "common/images/example.jpg"需要替换为开发者所需的图像资源文件
    private img: ImageBitmap = new ImageBitmap("common/images/example.jpg");

    build() {
      Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
        Canvas(this.context)
          .width('100%')
          .height('100%')
          .onReady(() => {
            let ctx = this.context
            let img = this.img

            ctx.drawImage(img, 0, 0, 100, 100);

            ctx.filter = 'grayscale(50%)';
            ctx.drawImage(img, 100, 0, 100, 100);

            ctx.filter = 'sepia(60%)';
            ctx.drawImage(img, 200, 0, 100, 100);

            ctx.filter = 'saturate(30%)';
            ctx.drawImage(img, 0, 100, 100, 100);

            ctx.filter = 'hue-rotate(90deg)';
            ctx.drawImage(img, 100, 100, 100, 100);

            ctx.filter = 'invert(100%)';
            ctx.drawImage(img, 200, 100, 100, 100);

            ctx.filter = 'opacity(25%)';
            ctx.drawImage(img, 0, 200, 100, 100);

            ctx.filter = 'brightness(0.4)';
            ctx.drawImage(img, 100, 200, 100, 100);

            ctx.filter = 'contrast(200%)';
            ctx.drawImage(img, 200, 200, 100, 100);

            ctx.filter = 'blur(5px)';
            ctx.drawImage(img, 0, 300, 100, 100);

            // Applying multiple filters
            ctx.filter = 'opacity(50%) contrast(200%) grayscale(50%)';
            ctx.drawImage(img, 100, 300, 100, 100);
          })
      }
      .width('100%')
      .height('100%')
    }
  }
```

#### letterSpacing18+

```ets
  // xxx.ets
  import { LengthMetrics, LengthUnit } from '@kit.ArkUI'

  @Entry
  @Component
  struct letterSpacingDemo {
    private settings: RenderingContextSettings = new RenderingContextSettings(true)
    private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

    build() {
      Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
        Canvas(this.context)
          .width('100%')
          .height('100%')
          .backgroundColor('rgb(213,213,213)')
          .onReady(() => {
            this.context.font = '30vp'
            this.context.letterSpacing = '10vp'
            this.context.fillText('hello world', 30, 50)
            this.context.letterSpacing = new LengthMetrics(10, LengthUnit.VP)
            this.context.fillText('hello world', 30, 100)
          })
      }
      .width('100%')
      .height('100%')
    }
  }
```

#### 方法

以下方法在隐藏页面中调用会产生缓存，应避免在隐藏页面中频繁刷新Canvas。

#### fillRect

fillRect(x: number, y: number, w: number, h: number): void

填充一个矩形。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明xnumber是

指定矩形左上角点的x坐标。

异常值undefined、null、NaN或Infinity按无效值处理，不进行绘制。

默认单位：vp

ynumber是

指定矩形左上角点的y坐标。

异常值undefined、null、NaN或Infinity按无效值处理，不进行绘制。

默认单位：vp

wnumber是

指定矩形的宽度。

异常值undefined、null、NaN或Infinity按无效值处理，不进行绘制。

默认单位：vp

hnumber是

指定矩形的高度。

异常值undefined、null、NaN或Infinity按无效值处理，不进行绘制。

默认单位：vp

**示例：**

```ets
// xxx.ets
@Entry
@Component
struct FillRect {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('rgb(213,213,213)')
        .onReady(() => {
          this.context.fillRect(30, 30, 100, 100)
       })
      }
    .width('100%')
    .height('100%')
  }
}
```

#### strokeRect

strokeRect(x: number, y: number, w: number, h: number): void

绘制具有边框的矩形，矩形内部不填充。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明xnumber是

指定矩形的左上角x坐标。

异常值undefined、null、NaN或Infinity按无效值处理，不进行绘制。

默认单位：vp

ynumber是

指定矩形的左上角y坐标。

异常值undefined、null、NaN或Infinity按无效值处理，不进行绘制。

默认单位：vp

wnumber是

指定矩形的宽度。

异常值undefined、null、NaN或Infinity按无效值处理，不进行绘制。

默认单位：vp

hnumber是

指定矩形的高度。

异常值undefined、null、NaN或Infinity按无效值处理，不进行绘制。

默认单位：vp

**示例：**

```ets
// xxx.ets
@Entry
@Component
struct StrokeRect {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          this.context.strokeRect(30, 30, 200, 150)
      })
    }
    .width('100%')
    .height('100%')
  }
}
```

#### clearRect

clearRect(x: number, y: number, w: number, h: number): void

删除指定区域内的绘制内容。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明xnumber是

指定矩形上的左上角x坐标。

异常值undefined、null、NaN或Infinity按无效值处理，不进行绘制。

默认单位：vp

ynumber是

指定矩形上的左上角y坐标。

异常值undefined、null、NaN或Infinity按无效值处理，不进行绘制。

默认单位：vp

wnumber是

指定矩形的宽度。

异常值undefined、null、NaN或Infinity按无效值处理，不进行绘制。

默认单位：vp

hnumber是

指定矩形的高度。

异常值undefined、null、NaN或Infinity按无效值处理，不进行绘制。

默认单位：vp

**示例：**

```ets
// xxx.ets
@Entry
@Component
struct ClearRect {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          this.context.fillStyle = 'rgb(0,0,255)'
          this.context.fillRect(20,20,200,200)
          this.context.clearRect(30,30,150,100)
      })
    }
    .width('100%')
    .height('100%')
  }
}
```

#### fillText

fillText(text: string, x: number, y: number, maxWidth?: number): void

绘制填充类文本。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明textstring是

需要绘制的文本内容。

异常值undefined或null按无效值处理，不进行绘制。

xnumber是

文本绘制起点的x轴坐标。

异常值undefined、null、NaN或Infinity按无效值处理，不进行绘制。

默认单位：vp

ynumber是

文本绘制起点的y轴坐标。

异常值undefined、null、NaN或Infinity按无效值处理，不进行绘制。

默认单位：vp

maxWidthnumber否

指定文本允许的最大宽度。

异常值null按无效值处理，不进行绘制，undefined、NaN或Infinity按默认值处理。

默认值：不限制宽度。

默认单位：vp

**示例：**

```ets
// xxx.ets
@Entry
@Component
struct FillText {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          this.context.font = '30px sans-serif'
          this.context.fillText("Hello World!", 20, 100)
      })
    }
    .width('100%')
    .height('100%')
  }
}
```

#### strokeText

strokeText(text: string, x: number, y: number, maxWidth?: number): void

绘制描边类文本。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明textstring是

需要绘制的文本内容。

异常值undefined或null按无效值处理，不进行绘制。

xnumber是

文本绘制起点的x轴坐标。

异常值undefined、null、NaN或Infinity按无效值处理，不进行绘制。

默认单位：vp

ynumber是

文本绘制起点的y轴坐标。

异常值undefined、null、NaN或Infinity按无效值处理，不进行绘制。

默认单位：vp

maxWidthnumber否

需要绘制的文本的最大宽度。

异常值null按无效值处理，不进行绘制，undefined、NaN或Infinity按默认值处理。

默认单位：vp

默认值：不限制宽度。

**示例：**

```ets
// xxx.ets
@Entry
@Component
struct StrokeText {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('rgb(213,213,213)')
        .onReady(() => {
          this.context.font = '50vp sans-serif'
          this.context.strokeText("Hello World!", 20, 60)
      })
    }
    .width('100%')
    .height('100%')
  }
}
```

#### measureText

measureText(text: string): TextMetrics

该方法返回一个文本测算的对象，通过该对象可以获取指定文本的宽度值。不同设备上获取的宽度值可能不同。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明textstring是

需要进行测量的文本。

传入异常值undefined或null时按"undefined"或"null"计算。

**返回值：**

类型说明[TextMetrics](#ZH-CN_TOPIC_0000002497444936__textmetrics)文本的尺寸信息。

**示例：**

```ets
// xxx.ets
@Entry
@Component
struct MeasureText {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('rgb(213,213,213)')
        .onReady(() => {
          this.context.font = '50px sans-serif'
          this.context.fillText("Hello World!", 20, 100)
          this.context.fillText("width:" + this.context.measureText("Hello World!").width, 20, 200)
      })
    }
    .width('100%')
    .height('100%')
  }
}
```

#### stroke

stroke(): void

根据当前的路径，进行边框绘制操作。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```ets
// xxx.ets
@Entry
@Component
struct Stroke {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() => {
          this.context.moveTo(125, 25)
          this.context.lineTo(125, 105)
          this.context.lineTo(175, 105)
          this.context.lineTo(175, 25)
          this.context.strokeStyle = 'rgb(255,0,0)'
          this.context.stroke()
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

#### stroke

stroke(path: Path2D): void

根据指定的路径，进行边框绘制操作。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明path[Path2D](Path2D.md)是

需要绘制的Path2D。

异常值undefined或null按无效值处理，不进行绘制。

**示例：**

```ets
// xxx.ets
@Entry
@Component
struct Stroke {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)
  private path2Da: Path2D = new Path2D()

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() => {
          this.path2Da.moveTo(25, 25)
          this.path2Da.lineTo(25, 105)
          this.path2Da.lineTo(75, 105)
          this.path2Da.lineTo(75, 25)
          this.context.strokeStyle = 'rgb(0,0,255)'
          this.context.stroke(this.path2Da)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

#### beginPath

beginPath(): void

创建一个新的绘制路径。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```ets
// xxx.ets
@Entry
@Component
struct BeginPath {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('rgb(213,213,213)')
        .onReady(() => {
          this.context.lineWidth = 6
          this.context.strokeStyle = 'rgb(39,135,217)'
          this.context.moveTo(15, 80)
          this.context.lineTo(280, 160)
          this.context.stroke()
          this.context.beginPath()
          this.context.lineTo(300, 240)
          this.context.lineTo(15, 240)
          this.context.stroke()
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

#### moveTo

moveTo(x: number, y: number): void

路径从当前点移动到指定点。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明xnumber是

指定位置的x坐标。

API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。

默认单位：vp

ynumber是

指定位置的y坐标。

API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。

默认单位：vp

API version 18之前，若未执行moveTo接口或moveTo接口传入无效参数，路径以(0,0)为起点。

API version 18及以后，若未执行moveTo接口或moveTo接口传入无效参数，路径以初次调用的lineTo、arcTo、bezierCurveTo或quadraticCurveTo接口中的起始点为起点。

**示例：**

```ets
// xxx.ets
@Entry
@Component
struct MoveTo {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          this.context.beginPath()
          this.context.moveTo(10, 10)
          this.context.lineTo(280, 160)
          this.context.stroke()
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

#### lineTo

lineTo(x: number, y: number): void

从当前点到指定点进行路径连接。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明xnumber是

指定位置的x坐标。

API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。

默认单位：vp

ynumber是

指定位置的y坐标。

API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。

默认单位：vp

**示例：**

```ets
// xxx.ets
@Entry
@Component
struct LineTo {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          this.context.beginPath()
          this.context.moveTo(10, 10)
          this.context.lineTo(280, 160)
          this.context.stroke()
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

#### closePath

closePath(): void

结束当前路径，形成一个封闭路径。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```ets
// xxx.ets
@Entry
@Component
struct ClosePath {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
            this.context.beginPath()
            this.context.moveTo(30, 30)
            this.context.lineTo(110, 30)
            this.context.lineTo(70, 90)
            this.context.closePath()
            this.context.stroke()
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

#### createPattern

createPattern(image: ImageBitmap, repetition: string | null): CanvasPattern | null

通过指定图像和重复方式创建图片填充的模板。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明image[ImageBitmap](ImageBitmap.md)是

图源对象，具体参考ImageBitmap对象。

异常值undefined或null按无效值处理。

repetitionstring | null是

设置图像重复的方式：

'repeat'：沿x轴和y轴重复绘制图像；

'repeat-x'：沿x轴重复绘制图像；

'repeat-y'：沿y轴重复绘制图像；

'no-repeat'：不重复绘制图像；

'clamp'：在原始边界外绘制时，超出部分使用边缘的颜色绘制；

'mirror'：沿x轴和y轴重复翻转绘制图像。

异常值undefined或null按无效值处理。

**返回值：**

类型说明[CanvasPattern](CanvasPattern.md) | null通过指定图像和重复方式创建图片填充的模板对象。

**示例：**

```ets
// xxx.ets
@Entry
@Component
struct CreatePattern {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)
  // "common/images/icon.jpg"需要替换为开发者所需的图像资源文件
  private img:ImageBitmap = new ImageBitmap("common/images/icon.jpg")

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          let pattern = this.context.createPattern(this.img, 'repeat')
          if (pattern) {
            this.context.fillStyle = pattern
          }
          this.context.fillRect(0, 0, 200, 200)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

#### bezierCurveTo

bezierCurveTo(cp1x: number, cp1y: number, cp2x: number, cp2y: number, x: number, y: number): void

创建三次贝塞尔曲线的路径。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明cp1xnumber是

第一个贝塞尔参数的x坐标值。

API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。

默认单位：vp

cp1ynumber是

第一个贝塞尔参数的y坐标值。

API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。

默认单位：vp

cp2xnumber是

第二个贝塞尔参数的x坐标值。

API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。

默认单位：vp

cp2ynumber是

第二个贝塞尔参数的y坐标值。

API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。

默认单位：vp

xnumber是

路径结束时的x坐标值。

API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。

默认单位：vp

ynumber是

路径结束时的y坐标值。

API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。

默认单位：vp

**示例：**

```ets
// xxx.ets
@Entry
@Component
struct BezierCurveTo {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          this.context.beginPath()
          this.context.moveTo(10, 10)
          this.context.bezierCurveTo(20, 100, 200, 100, 200, 20)
          this.context.stroke()
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

#### quadraticCurveTo

quadraticCurveTo(cpx: number, cpy: number, x: number, y: number): void

创建二次贝塞尔曲线的路径。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明cpxnumber是

贝塞尔参数的x坐标值。

API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。

默认单位：vp

cpynumber是

贝塞尔参数的y坐标值。

API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。

默认单位：vp

xnumber是

路径结束时的x坐标值。

API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。

默认单位：vp

ynumber是

路径结束时的y坐标值。

API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。

默认单位：vp

**示例：**

```ets
// xxx.ets
@Entry
@Component
struct QuadraticCurveTo {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          this.context.beginPath()
          this.context.moveTo(20, 20)
          this.context.quadraticCurveTo(100, 100, 200, 20)
          this.context.stroke()
      })
    }
    .width('100%')
    .height('100%')
  }
}
```

#### arc

arc(x: number, y: number, radius: number, startAngle: number, endAngle: number, counterclockwise?: boolean): void

绘制弧线路径。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明xnumber是

弧线圆心的x坐标值。

API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。

默认单位：vp

ynumber是

弧线圆心的y坐标值。

API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。

默认单位：vp

radiusnumber是

弧线的圆半径。

API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。

默认单位：vp

startAnglenumber是

弧线的起始弧度。

API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。

单位：弧度

endAnglenumber是

弧线的终止弧度。

API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。

单位：弧度

counterclockwiseboolean否

是否逆时针绘制圆弧。

true：逆时针方向绘制圆弧。

false：顺时针方向绘制圆弧。

默认值：false，设置null或undefined按默认值处理。

**示例：**

```ets
// xxx.ets
@Entry
@Component
struct Arc {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          this.context.beginPath()
          this.context.arc(100, 75, 50, 0, 6.28)
          this.context.stroke()
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

#### arcTo

arcTo(x1: number, y1: number, x2: number, y2: number, radius: number): void

依据给定的控制点和圆弧半径创建圆弧路径。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明x1number是

第一个控制点的x坐标值。

API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。

默认单位：vp

y1number是

第一个控制点的y坐标值。

API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。

默认单位：vp

x2number是

第二个控制点的x坐标值。

API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。

默认单位：vp

y2number是

第二个控制点的y坐标值。

API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。

默认单位：vp

radiusnumber是

圆弧的圆半径值。

API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。

默认单位：vp

**示例：**

```ets
// xxx.ets
@Entry
@Component
struct ArcTo {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          // 切线
          this.context.beginPath()
          this.context.strokeStyle = '#808080'
          this.context.lineWidth = 1.5;
          this.context.moveTo(360, 20);
          this.context.lineTo(360, 170);
          this.context.lineTo(110, 170);
          this.context.stroke();

          // 圆弧
          this.context.beginPath()
          this.context.strokeStyle = '#000000'
          this.context.lineWidth = 3;
          this.context.moveTo(360, 20)
          this.context.arcTo(360, 170, 110, 170, 150)
          this.context.stroke()

          // 起始点
          this.context.beginPath();
          this.context.fillStyle = '#00ff00';
          this.context.arc(360, 20, 4, 0, 2 * Math.PI);
          this.context.fill();

          // 控制点
          this.context.beginPath();
          this.context.fillStyle = '#ff0000';
          this.context.arc(360, 170, 4, 0, 2 * Math.PI);
          this.context.arc(110, 170, 4, 0, 2 * Math.PI);
          this.context.fill();
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

此示例中，arcTo()创建的圆弧为黑色，圆弧的两条切线为灰色。控制点为红色，起始点为绿色。

可以想象两条切线：一条切线从起始点到第一个控制点，另一条切线从第一个控制点到第二个控制点。arcTo()在这两条切线间创建一个圆弧，并使圆弧与这两条切线都相切。

#### ellipse

ellipse(x: number, y: number, radiusX: number, radiusY: number, rotation: number, startAngle: number, endAngle: number, counterclockwise?: boolean): void

在规定的矩形区域绘制一个椭圆。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明xnumber是

椭圆圆心的x轴坐标。

API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。

默认单位：vp

ynumber是

椭圆圆心的y轴坐标。

API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。

默认单位：vp

radiusXnumber是

椭圆x轴的半径长度。

API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。

默认单位：vp

radiusYnumber是

椭圆y轴的半径长度。

API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。

默认单位：vp

rotationnumber是

椭圆的旋转角度。

API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。

单位：弧度

startAnglenumber是

椭圆绘制的起始点角度。

API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。

单位：弧度

endAnglenumber是

椭圆绘制的结束点角度。

API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。

单位：弧度

counterclockwiseboolean否

是否以逆时针方向绘制椭圆。

true：逆时针方向绘制椭圆。

false：顺时针方向绘制椭圆。

默认值：false，设置null或undefined按默认值处理。

**示例：**

```ets
// xxx.ets
@Entry
@Component
struct CanvasExample {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          this.context.beginPath()
          this.context.ellipse(200, 200, 50, 100, Math.PI * 0.25, Math.PI * 0.5, Math.PI * 2, false)
          this.context.stroke()
          this.context.beginPath()
          this.context.ellipse(200, 300, 50, 100, Math.PI * 0.25, Math.PI * 0.5, Math.PI * 2, true)
          this.context.stroke()
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

#### rect

rect(x: number, y: number, w: number, h: number): void

创建矩形路径。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明xnumber是

指定矩形的左上角x坐标值。

API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。

默认单位：vp

ynumber是

指定矩形的左上角y坐标值。

API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。

默认单位：vp

wnumber是

指定矩形的宽度。

API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。

默认单位：vp

hnumber是

指定矩形的高度。

API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。

默认单位：vp

**示例：**

```ets
// xxx.ets
@Entry
@Component
struct CanvasExample {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          this.context.rect(20, 20, 100, 100) // Create a 100*100 rectangle at (20, 20)
          this.context.stroke()
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

#### roundRect20+

roundRect(x: number, y: number, w: number, h: number, radii?: number | Array<number>): void

创建圆角矩形路径，此方法不会直接渲染内容，如需将圆角矩形绘制到画布上，可以使用fill或stroke方法。

**卡片能力：** 从API version 20开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明xnumber是

指定矩形的左上角x坐标值。

null按0处理，undefined按无效值处理，不进行绘制。

如需绘制完整矩形，取值范围：[0, Canvas宽度)。

默认单位：vp

ynumber是

指定矩形的左上角y坐标值。

null按0处理，undefined按无效值处理，不进行绘制。

如需绘制完整矩形，取值范围：[0, Canvas高度)。

默认单位：vp

wnumber是

指定矩形的宽度，设置负值为向左绘制。

null按0处理，undefined按无效值处理，不进行绘制。

如需绘制完整矩形，取值范围：[-x, Canvas宽度 - x]。

默认单位：vp

hnumber是

指定矩形的高度，设置负值为向上绘制。

null按0处理，undefined按无效值处理，不进行绘制。

如需绘制完整矩形，取值范围：[-y, Canvas高度 - y]。

默认单位：vp

radiinumber | Array<number>否

指定用于矩形角的圆弧半径的数字或列表。

参数类型为number时，所有矩形角的圆弧半径按该数字执行。

参数类型为Array<number>时，数目为1-4个按下面执行：

[所有矩形角的圆弧半径]

[左上及右下矩形角的圆弧半径, 右上及左下矩形角的圆弧半径]

[左上矩形角的圆弧半径, 右上及左下矩形角的圆弧半径, 右下矩形角的圆弧半径]

[左上矩形角的圆弧半径, 右上矩形角的圆弧半径, 右下矩形角的圆弧半径, 左下矩形角的圆弧半径]

radii存在负数或列表的数目不在[1,4]内时抛出异常，错误码：103701。

默认值：0，null和undefined按默认值处理。

圆弧半径超过矩形宽高时会等比例缩放到宽高的长度。

默认单位：vp

**错误码：**

以下错误码的详细介绍请参见[Canvas组件错误码](Canvas组件错误码.md)。

错误码ID错误信息可能原因103701Parameter error.1. The param radii is a list that has zero or more than four elements; 2. The param radii contains negative value.

**示例：**

该示例展示了绘制六个圆角矩形：

1.

创建一个(10vp, 10vp)为起点，宽高为100vp，四个矩形角圆弧半径为10vp的圆角矩形并填充；

1.

创建一个(120vp, 10vp)为起点，宽高为100vp，四个矩形角圆弧半径为10vp的圆角矩形并填充；

1.

创建一个(10vp, 120vp)为起点，宽高为100vp，左上矩形角圆弧半径及右下矩形角圆弧半径为10vp，右上矩形角圆弧半径及左下矩形角圆弧半径为20vp的圆角矩形并描边；

1.

创建一个(120vp, 120vp)为起点，宽高为100vp，左上矩形角圆弧半径为10vp，右上矩形角圆弧半径及左下矩形角圆弧半径为20vp，右下矩形角圆弧半径为30vp的圆角矩形并描边；

1.

创建一个(10vp, 230vp)为起点，宽高为100vp，左上矩形角圆弧半径为10vp，右上矩形角圆弧半径为20vp，右下矩形角圆弧半径为30vp，左下矩形角圆弧半径为40vp的圆角矩形并描边；

1.

创建一个(220vp, 330vp)为起点，宽高为-100vp，左上矩形角圆弧半径为10vp，右上矩形角圆弧半径为20vp，右下矩形角圆弧半径为30vp，左下矩形角圆弧半径为40vp的圆角矩形并描边。

```ets
// xxx.ets
import { BusinessError } from '@kit.BasicServicesKit';

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
        .backgroundColor('#D5D5D5')
        .onReady(() => {
          try {
            this.context.fillStyle = '#707070'
            this.context.beginPath()
            // 创建一个(10vp, 10vp)为起点，宽高为100vp，四个矩形角圆弧半径为10vp的圆角矩形
            this.context.roundRect(10, 10, 100, 100, 10)
            // 创建一个(120vp, 10vp)为起点，宽高为100vp，四个矩形角圆弧半径为10vp的圆角矩形
            this.context.roundRect(120, 10, 100, 100, [10])
            this.context.fill()
            this.context.beginPath()
            // 创建一个(10vp, 120vp)为起点，宽高为100vp，左上矩形角圆弧半径及右下矩形角圆弧半径为10vp，右上矩形角圆弧半径及左下矩形角圆弧半径为20vp的圆角矩形
            this.context.roundRect(10, 120, 100, 100, [10, 20])
            // 创建一个(120vp, 120vp)为起点，宽高为100vp，左上矩形角圆弧半径为10vp，右上矩形角圆弧半径及左下矩形角圆弧半径为20vp，右下矩形角圆弧半径为30vp的圆角矩形
            this.context.roundRect(120, 120, 100, 100, [10, 20, 30])
            // 创建一个(10vp, 230vp)为起点，宽高为100vp，左上矩形角圆弧半径为10vp，右上矩形角圆弧半径为20vp，右下矩形角圆弧半径为30vp，左下矩形角圆弧半径为40vp的圆角矩形
            this.context.roundRect(10, 230, 100, 100, [10, 20, 30, 40])
            // 创建一个(220vp, 330vp)为起点，宽高为-100vp，左上矩形角圆弧半径为10vp，右上矩形角圆弧半径为20vp，右下矩形角圆弧半径为30vp，左下矩形角圆弧半径为40vp的圆角矩形
            this.context.roundRect(220, 330, -100, -100, [10, 20, 30, 40])
            this.context.stroke()
          } catch (error) {
            let e: BusinessError = error as BusinessError;
            console.error(`Failed to create roundRect. Code: ${e.code}, message: ${e.message}`);
          }
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

#### fill

fill(fillRule?: CanvasFillRule): void

对当前路径进行填充。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数:**

参数名类型必填说明fillRule[CanvasFillRule](#ZH-CN_TOPIC_0000002497444936__canvasfillrule类型说明)否

指定要填充对象的规则。

可选参数为："nonzero"，"evenodd"。

异常值undefined或null按默认值处理。

默认值："nonzero"

**示例:**

```ets
// xxx.ets
@Entry
@Component
struct Fill {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          this.context.rect(20, 20, 100, 100) // Create a 100*100 rectangle at (20, 20)
          this.context.fill()
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

#### fill

fill(path: Path2D, fillRule?: CanvasFillRule): void

对指定路径进行填充。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数:**

参数名类型必填说明path[Path2D](Path2D.md)是

Path2D填充路径。

异常值undefined或null按无效值处理。

fillRule[CanvasFillRule](#ZH-CN_TOPIC_0000002497444936__canvasfillrule类型说明)否

指定要填充对象的规则。

可选参数为："nonzero"，"evenodd"。

异常值undefined或null按默认值处理。

默认值："nonzero"

**示例:**

```ets
// xxx.ets
@Entry
@Component
struct Fill {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          let region = new Path2D()
          region.moveTo(30, 90)
          region.lineTo(110, 20)
          region.lineTo(240, 130)
          region.lineTo(60, 130)
          region.lineTo(190, 20)
          region.lineTo(270, 90)
          region.closePath()
          // Fill path
          this.context.fillStyle = '#00ff00'
          this.context.fill(region, "evenodd")
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

#### clip

clip(fillRule?: CanvasFillRule): void

设置当前路径为剪切路径。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数:**

参数名类型必填说明fillRule[CanvasFillRule](#ZH-CN_TOPIC_0000002497444936__canvasfillrule类型说明)否

指定要剪切对象的规则。

可选参数为："nonzero"，"evenodd"。

异常值undefined或null按默认值处理。

默认值："nonzero"

**示例:**

```ets
// xxx.ets
@Entry
@Component
struct Clip {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          this.context.rect(0, 0, 100, 200)
          this.context.stroke()
          this.context.clip()
          this.context.fillStyle = "rgb(255,0,0)"
          this.context.fillRect(0, 0, 200, 200)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

#### clip

clip(path: Path2D, fillRule?: CanvasFillRule): void

设置指定路径为剪切路径。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数:**

参数名类型必填说明path[Path2D](Path2D.md)是

Path2D剪切路径。

异常值undefined或null按无效值处理。

fillRule[CanvasFillRule](#ZH-CN_TOPIC_0000002497444936__canvasfillrule类型说明)否

指定要剪切对象的规则。

可选参数为："nonzero"，"evenodd"。

异常值undefined或null按默认值处理。

默认值："nonzero"

**示例:**

```ets
// xxx.ets
@Entry
@Component
struct Clip {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)
  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          let region = new Path2D()
          region.moveTo(30, 90)
          region.lineTo(110, 20)
          region.lineTo(240, 130)
          region.lineTo(60, 130)
          region.lineTo(190, 20)
          region.lineTo(270, 90)
          region.closePath()
          this.context.clip(region,"evenodd")
          this.context.fillStyle = "rgb(0,255,0)"
          this.context.fillRect(0, 0, this.context.width, this.context.height)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

#### reset12+

reset(): void

将CanvasRenderingContext2D重置为其默认状态，清除后台缓冲区、绘制状态栈、绘制路径和样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```ets
// xxx.ets
@Entry
@Component
struct Reset {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          this.context.fillStyle = '#0000ff'
          this.context.fillRect(20, 20, 150, 100)
          this.context.reset()
          this.context.fillRect(20, 150, 150, 100)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

#### saveLayer12+

saveLayer(): void

创建一个图层。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```ets
// xxx.ets
@Entry
@Component
struct saveLayer {
private settings: RenderingContextSettings = new RenderingContextSettings(true)
private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

build() {
  Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
    Canvas(this.context)
      .width('100%')
      .height('100%')
      .backgroundColor('#ffff00')
      .onReady(() =>{
        this.context.fillStyle = "#0000ff"
        this.context.fillRect(50,100,300,100)
        this.context.fillStyle = "#00ffff"
        this.context.fillRect(50,150,300,100)
        this.context.globalCompositeOperation = 'destination-over'
        this.context.saveLayer()
        this.context.globalCompositeOperation = 'source-over'
        this.context.fillStyle = "#ff0000"
        this.context.fillRect(100,50,100,300)
        this.context.fillStyle = "#00ff00"
        this.context.fillRect(150,50,100,300)
        this.context.restoreLayer()
      })
  }
  .width('100%')
  .height('100%')
}
}
```

#### restoreLayer12+

restoreLayer(): void

恢复图像变换和裁剪状态至saveLayer前的状态，并将图层绘制在canvas上。restoreLayer示例代码同saveLayer。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

#### resetTransform

resetTransform(): void

使用单位矩阵重新设置当前矩阵。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```ets
// xxx.ets
@Entry
@Component
struct ResetTransform {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          this.context.setTransform(1,0.5, -0.5, 1, 10, 10)
          this.context.fillStyle = 'rgb(0,0,255)'
          this.context.fillRect(0, 0, 100, 100)
          this.context.resetTransform()
          this.context.fillStyle = 'rgb(255,0,0)'
          this.context.fillRect(0, 0, 100, 100)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

#### rotate

rotate(angle: number): void

针对当前坐标轴进行顺时针旋转。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明anglenumber是

设置顺时针旋转的弧度值，可以通过 degree * Math.PI / 180 将角度转换为弧度值。

API version 18之前，设置NaN或Infinity时，在该方法后执行的绘制方法无法绘制；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的绘制方法正常绘制。

单位：弧度

**示例：**

```ets
// xxx.ets
@Entry
@Component
struct Rotate {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          this.context.rotate(45 * Math.PI / 180)
          this.context.fillRect(70, 20, 50, 50)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

#### scale

scale(x: number, y: number): void

设置canvas画布的缩放变换属性，后续的绘制操作将按照缩放比例进行缩放。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明xnumber是

设置水平方向的缩放值。

API version 18之前，设置NaN或Infinity时，在该方法后执行的绘制方法无法绘制；不支持设置0和负数，设置0、负数、null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、0、负数、null或undefined时当前接口不生效，其他传入有效参数的绘制方法正常绘制。

ynumber是

设置垂直方向的缩放值，不支持设置负数。

API version 18之前，设置NaN或Infinity时，在该方法后执行的绘制方法无法绘制；不支持设置0和负数，设置0、负数、null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、0、负数、null或undefined时当前接口不生效，其他传入有效参数的绘制方法正常绘制。

**示例：**

```ets
// xxx.ets
@Entry
@Component
struct Scale {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          this.context.lineWidth = 3
          this.context.strokeRect(30, 30, 50, 50)
          this.context.scale(2, 2) // Scale to 200%
          this.context.strokeRect(30, 30, 50, 50)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

#### transform

transform(a: number, b: number, c: number, d: number, e: number, f: number): void

transform方法对应一个变换矩阵，想对一个图形进行变化的时候，只要设置此变换矩阵相应的参数，对图形的各个定点的坐标分别乘以这个矩阵，就能得到新的定点的坐标。矩阵变换效果可叠加。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

图形中各个点变换后的坐标可通过下方坐标计算公式计算。

变换后的坐标计算方式（x和y为变换前坐标，x'和y'为变换后坐标）：

-

x' = a * x + c * y + e

-

y' = b * x + d * y + f

**参数：**

参数名类型必填说明anumber是

变换矩阵中第一行第一列的单元格。scaleX：指定水平缩放值，支持设置负数。

API version 18之前，设置NaN或Infinity时，在该方法后执行的绘制方法无法绘制；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的绘制方法正常绘制。

bnumber是

变换矩阵第二行第一列的单元格。skewY：指定垂直倾斜值，支持设置负数。

API version 18之前，设置NaN或Infinity时，在该方法后执行的绘制方法无法绘制；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的绘制方法正常绘制。

cnumber是

变换矩阵第一行第二列的单元格。skewX：指定水平倾斜值，支持设置负数。

API version 18之前，设置NaN或Infinity时，在该方法后执行的绘制方法无法绘制；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的绘制方法正常绘制。

dnumber是

变换矩阵第二行第二列的单元格。scaleY：指定垂直缩放值，支持设置负数。

API version 18之前，设置NaN或Infinity时，在该方法后执行的绘制方法无法绘制；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的绘制方法正常绘制。

enumber是

变换矩阵第一行第三列的单元格。translateX：指定水平移动值，支持设置负数。

API version 18之前，设置NaN或Infinity时，在该方法后执行的绘制方法无法绘制；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的绘制方法正常绘制。

默认单位：vp

fnumber是

变换矩阵第二行第三列的单元格。translateY：指定垂直移动值，支持设置负数。

API version 18之前，设置NaN或Infinity时，在该方法后执行的绘制方法无法绘制；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的绘制方法正常绘制。

默认单位：vp

**示例：**

```ets
// xxx.ets
@Entry
@Component
struct Transform {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('rgb(213,213,213)')
        .onReady(() => {
          this.context.fillStyle = 'rgb(112,112,112)'
          this.context.fillRect(0, 0, 100, 100)
          this.context.transform(1, 0.5, -0.5, 1, 10, 10)
          this.context.fillStyle = 'rgb(0,74,175)'
          this.context.fillRect(0, 0, 100, 100)
          this.context.transform(1, 0.5, -0.5, 1, 10, 10)
          this.context.fillStyle = 'rgb(39,135,217)'
          this.context.fillRect(0, 0, 100, 100)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

#### setTransform

setTransform(a: number, b: number, c: number, d: number, e: number, f: number): void

setTransform方法使用的参数和transform()方法相同，但setTransform()方法会重置现有的变换矩阵并创建新的变换矩阵。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

图形中各个点变换后的坐标可通过下方坐标计算公式计算。

变换后的坐标计算方式（x和y为变换前坐标，x'和y'为变换后坐标）：

-

x' = a * x + c * y + e

-

y' = b * x + d * y + f

**参数：**

参数名类型必填说明anumber是

scaleX：指定水平缩放值，支持设置负数。

API version 18之前，设置NaN或Infinity时，在该方法后执行的绘制方法无法绘制；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的绘制方法正常绘制。

bnumber是

skewY：指定垂直倾斜值，支持设置负数。

API version 18之前，设置NaN或Infinity时，在该方法后执行的绘制方法无法绘制；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的绘制方法正常绘制。

cnumber是

skewX：指定水平倾斜值，支持设置负数。

API version 18之前，设置NaN或Infinity时，在该方法后执行的绘制方法无法绘制；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的绘制方法正常绘制。

dnumber是

scaleY：指定垂直缩放值，支持设置负数。

API version 18之前，设置NaN或Infinity时，在该方法后执行的绘制方法无法绘制；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的绘制方法正常绘制。

enumber是

translateX：指定水平移动值，支持设置负数。

API version 18之前，设置NaN或Infinity时，在该方法后执行的绘制方法无法绘制；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的绘制方法正常绘制。

默认单位：vp

fnumber是

translateY：指定垂直移动值，支持设置负数。

API version 18之前，设置NaN或Infinity时，在该方法后执行的绘制方法无法绘制；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的绘制方法正常绘制。

默认单位：vp

**示例：**

```ets
// xxx.ets
@Entry
@Component
struct SetTransform {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('rgb(213,213,213)')
        .onReady(() => {
          this.context.fillStyle = 'rgb(112,112,112)'
          this.context.fillRect(0, 0, 100, 100)
          this.context.transform(1, 0.5, -0.5, 1, 10, 10)
          this.context.fillStyle = 'rgb(23,169,141)'
          this.context.fillRect(0, 0, 100, 100)
          this.context.setTransform(1, 0.5, -0.5, 1, 10, 10)
          this.context.fillStyle = 'rgb(39,135,217)'
          this.context.fillRect(0, 0, 100, 100)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

#### setTransform

setTransform(transform?: Matrix2D): void

以Matrix2D对象为模板重置现有的变换矩阵并创建新的变换矩阵。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明transform[Matrix2D](Matrix2D.md)否

变换矩阵。

异常值undefined或null按无效值处理。

默认值：null

**示例：**

```ets
// xxx.ets
@Entry
@Component
struct TransFormDemo {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context1: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private context2: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Text('context1');
      Canvas(this.context1)
        .width('230vp')
        .height('160vp')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          this.context1.fillRect(100, 20, 50, 50);
          this.context1.setTransform(1, 0.5, -0.5, 1, 10, 10);
          this.context1.fillRect(100, 20, 50, 50);
        })
      Text('context2');
      Canvas(this.context2)
        .width('230vp')
        .height('160vp')
        .backgroundColor('#0ffff0')
        .onReady(() =>{
          this.context2.fillRect(100, 20, 50, 50);
          let storedTransform = this.context1.getTransform();
          this.context2.setTransform(storedTransform);
          this.context2.fillRect(100, 20, 50, 50);
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

#### getTransform

getTransform(): Matrix2D

获取当前被应用到上下文的转换矩阵。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

类型说明[Matrix2D](Matrix2D.md)当前被应用到上下文的转换矩阵。

**示例：**

```ets
// xxx.ets
@Entry
@Component
struct TransFormDemo {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context1: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private context2: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Text('context1');
      Canvas(this.context1)
        .width('230vp')
        .height('120vp')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          this.context1.fillRect(50, 50, 50, 50);
          this.context1.setTransform(1.2, Math.PI/8, Math.PI/6, 0.5, 30, -25);
          this.context1.fillRect(50, 50, 50, 50);
        })
      Text('context2');
      Canvas(this.context2)
        .width('230vp')
        .height('120vp')
        .backgroundColor('#0ffff0')
        .onReady(() =>{
          this.context2.fillRect(50, 50, 50, 50);
          let storedTransform = this.context1.getTransform();
          console.info("Matrix [scaleX = " + storedTransform.scaleX + ", scaleY = " + storedTransform.scaleY +
          ", rotateX = " + storedTransform.rotateX + ", rotateY = " + storedTransform.rotateY +
          ", translateX = " + storedTransform.translateX + ", translateY = " + storedTransform.translateY + "]")
          this.context2.setTransform(storedTransform);
          this.context2.fillRect(50,50,50,50);
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

#### translate

translate(x: number, y: number): void

移动当前坐标系的原点。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明xnumber是

设置水平平移量。

API version 18之前，设置NaN或Infinity时，在该方法后执行的绘制方法无法绘制；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的绘制方法正常绘制。

默认单位：vp

ynumber是

设置竖直平移量。

API version 18之前，设置NaN或Infinity时，在该方法后执行的绘制方法无法绘制；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的绘制方法正常绘制。

默认单位：vp

**示例：**

```ets
// xxx.ets
@Entry
@Component
struct Translate {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          this.context.fillRect(10, 10, 50, 50)
          this.context.translate(70, 70)
          this.context.fillRect(10, 10, 50, 50)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

#### drawImage

drawImage(image: ImageBitmap | PixelMap, dx: number, dy: number): void

进行图像绘制。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用，卡片中不支持PixelMap对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明image[ImageBitmap](ImageBitmap.md) | [PixelMap](Interface (PixelMap).md)是

图片资源，请参考ImageBitmap或PixelMap。

异常值undefined或null按无效值处理，不进行绘制。

dxnumber是

绘制区域左上角在x轴的位置。

异常值undefined或null按0处理，NaN和Infinity按无效值处理，不进行绘制。

默认单位：vp

dynumber是

绘制区域左上角在y轴的位置。

异常值undefined或null按0处理，NaN和Infinity按无效值处理，不进行绘制。

默认单位：vp

**示例：**

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
        .backgroundColor('#D5D5D5')
        .onReady(() => {
          this.context.drawImage(this.img, 0, 0)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

#### drawImage

drawImage(image: ImageBitmap | PixelMap, dx: number, dy: number, dw: number, dh: number): void

将图像裁剪后拉伸或压缩绘制。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用，卡片中不支持PixelMap对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明image[ImageBitmap](ImageBitmap.md) | [PixelMap](Interface (PixelMap).md)是

图片资源，请参考ImageBitmap或PixelMap。

异常值undefined或null按无效值处理，不进行绘制。

dxnumber是

绘制区域左上角在x轴的位置。

异常值undefined或null按0处理，NaN和Infinity按无效值处理，不进行绘制。

默认单位：vp

dynumber是

绘制区域左上角在y轴的位置。

异常值undefined或null按0处理，NaN和Infinity按无效值处理，不进行绘制。

默认单位：vp

dwnumber是

绘制区域的宽度。当绘制区域的宽度和裁剪图像的宽度不一致时，将图像宽度拉伸或压缩为绘制区域的宽度。

负数、异常值undefined或null按0处理，NaN和Infinity按无效值处理，不进行绘制。

默认单位：vp

dhnumber是

绘制区域的高度。当绘制区域的高度和裁剪图像的高度不一致时，将图像高度拉伸或压缩为绘制区域的高度。

负数、异常值undefined或null按0处理，NaN和Infinity按无效值处理，不进行绘制。

默认单位：vp

**示例：**

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
        .backgroundColor('#D5D5D5')
        .onReady(() => {
          this.context.drawImage(this.img, 0, 0, 300, 300)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

#### drawImage

drawImage(image: ImageBitmap | PixelMap, sx: number, sy: number, sw: number, sh: number, dx: number, dy: number, dw: number, dh: number): void

将图像裁剪后拉伸或压缩绘制。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用，卡片中不支持PixelMap对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明image[ImageBitmap](ImageBitmap.md) | [PixelMap](Interface (PixelMap).md)是

图片资源，请参考ImageBitmap或PixelMap。

异常值undefined或null按无效值处理，不进行绘制。

sxnumber是

裁切源图像时距离源图像左上角的x坐标值。

异常值undefined或null按0处理，NaN和Infinity按无效值处理，不进行绘制。

image类型为ImageBitmap时，默认单位：vp

image类型为PixelMap时，API version 18前，默认单位：px；API version 18及以后，默认单位：vp

synumber是

裁切源图像时距离源图像左上角的y坐标值。

异常值undefined或null按0处理，NaN和Infinity按无效值处理，不进行绘制。

image类型为ImageBitmap时，默认单位：vp

image类型为PixelMap时，API version 18前，默认单位：px；API version 18及以后，默认单位：vp

swnumber是

裁切源图像时需要裁切的宽度。

负数、异常值undefined或null按0处理，NaN和Infinity按无效值处理，不进行绘制。

image类型为ImageBitmap时，默认单位：vp

image类型为PixelMap时，API version 18前，默认单位：px；API version 18及以后，默认单位：vp

shnumber是

裁切源图像时需要裁切的高度。

负数、异常值undefined或null按0处理，NaN和Infinity按无效值处理，不进行绘制。

image类型为ImageBitmap时，默认单位：vp

image类型为PixelMap时，API version 18前，默认单位：px；API version 18及以后，默认单位：vp

dxnumber是

绘制区域左上角在x轴的位置。

异常值undefined或null按0处理，NaN和Infinity按无效值处理，不进行绘制。

默认单位：vp

dynumber是

绘制区域左上角在y轴的位置。

异常值undefined或null按0处理，NaN和Infinity按无效值处理，不进行绘制。

默认单位：vp

dwnumber是

绘制区域的宽度。

负数、异常值undefined或null按0处理，NaN和Infinity按无效值处理，不进行绘制。当绘制区域的宽度和裁剪图像的宽度不一致时，将图像宽度拉伸或压缩为绘制区域的宽度。

默认单位：vp

dhnumber是

绘制区域的高度。

负数、异常值undefined或null按0处理，NaN和Infinity按无效值处理，不进行绘制。当绘制区域的高度和裁剪图像的高度不一致时，将图像高度拉伸或压缩为绘制区域的高度。

默认单位：vp

**示例：**

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
        .backgroundColor('#D5D5D5')
        .onReady(() => {
          this.context.drawImage(this.img, 0, 0, 500, 500, 0, 0, 400, 300)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

#### createImageData

createImageData(sw: number, sh: number): ImageData

创建新的、空白的、指定大小的ImageData 对象，请参考[ImageData](ImageData.md)，该接口存在内存拷贝行为，高耗时，应避免频繁使用。createImageData示例同putImageData。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明swnumber是

ImageData的宽度。

异常值undefined、null、NaN和Infinity按0处理。

默认单位：vp

shnumber是

ImageData的高度。

异常值undefined、null、NaN和Infinity按0处理。

默认单位：vp

**返回值：**

类型说明[ImageData](ImageData.md)新的ImageData对象。

#### createImageData

createImageData(imageData: ImageData): ImageData

根据一个现有的ImageData对象重新创建一个宽、高相同的ImageData对象（不会复制图像数据），请参考[ImageData](ImageData.md)，该接口存在内存拷贝行为，高耗时，应避免频繁使用。createImageData示例同putImageData。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明imageData[ImageData](ImageData.md)是

现有的ImageData对象。

异常值undefined和null按width和height为0的ImageData处理。

**返回值：**

类型说明[ImageData](ImageData.md)新的ImageData对象。

#### getPixelMap

getPixelMap(sx: number, sy: number, sw: number, sh: number): PixelMap

以当前canvas指定区域内的像素创建[PixelMap](Interface (PixelMap).md)对象，该接口存在内存拷贝行为，高耗时，应避免频繁使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明sxnumber是

需要输出的区域的左上角x坐标。

异常值undefined、null、NaN和Infinity按0处理。

默认单位：vp

synumber是

需要输出的区域的左上角y坐标。

异常值undefined、null、NaN和Infinity按0处理。

默认单位：vp

swnumber是

需要输出的区域的宽度。

异常值undefined、null、NaN和Infinity按0处理。

默认单位：vp

shnumber是

需要输出的区域的高度。

异常值undefined、null、NaN和Infinity按0处理。

默认单位：vp

**返回值：**

类型说明[PixelMap](Interface (PixelMap).md)新的PixelMap对象。

**示例：**

DevEco Studio的预览器不支持显示使用setPixelMap绘制的内容。

```ets
// xxx.ets
@Entry
@Component
struct GetPixelMap {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)
  // "common/images/example.jpg"需要替换为开发者所需的图像资源文件
  private img: ImageBitmap = new ImageBitmap("common/images/example.jpg")

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() => {
          this.context.drawImage(this.img, 100, 100, 130, 130)
          let pixelmap = this.context.getPixelMap(150, 150, 130, 130)
          this.context.setPixelMap(pixelmap)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

#### setPixelMap

setPixelMap(value?: PixelMap): void

将当前传入[PixelMap](Interface (PixelMap).md)对象绘制在画布上。setPixelMap示例同getPixelMap。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明value[PixelMap](Interface (PixelMap).md)否

包含像素值的PixelMap对象。

异常值undefined和null按无效值处理，不进行绘制。

默认值：null

#### getImageData

getImageData(sx: number, sy: number, sw: number, sh: number): ImageData

以当前canvas指定区域内的像素创建[ImageData](ImageData.md)对象，该接口存在内存拷贝行为，高耗时，应避免频繁使用。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明sxnumber是

需要输出的区域的左上角x坐标。

异常值undefined、null、NaN和Infinity按0处理。

默认单位：vp

synumber是

需要输出的区域的左上角y坐标。

异常值undefined、null、NaN和Infinity按0处理。

默认单位：vp

swnumber是

需要输出的区域的宽度。

异常值undefined、null、NaN和Infinity按0处理。

默认单位：vp

shnumber是

需要输出的区域的高度。

异常值undefined、null、NaN和Infinity按0处理。

默认单位：vp

**返回值：**

类型说明[ImageData](ImageData.md)新的ImageData对象。

**示例：**

```ets
// xxx.ets
@Entry
@Component
struct GetImageData {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)
  // "/common/images/1234.png"需要替换为开发者所需的图像资源文件
  private img:ImageBitmap = new ImageBitmap("/common/images/1234.png")

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          this.context.drawImage(this.img,0,0,130,130)
          let imageData = this.context.getImageData(50,50,130,130)
          this.context.putImageData(imageData,150,150)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

#### putImageData

putImageData(imageData: ImageData, dx: number | string, dy: number | string): void

使用[ImageData](ImageData.md)数据填充新的矩形区域。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明imageData[ImageData](ImageData.md)是

包含像素值的ImageData对象。

异常值undefined或null按无效值处理，不进行绘制。

dxnumber | string10+是

填充区域在x轴方向的偏移量。

异常值undefined、null、NaN和Infinity按0处理。

默认单位：vp

dynumber | string10+是

填充区域在y轴方向的偏移量。

异常值undefined、null、NaN和Infinity按0处理。

默认单位：vp

**示例：**

```ets
// xxx.ets
@Entry
@Component
struct PutImageData {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('rgb(213,213,213)')
        .onReady(() => {
          let imageDataNum = this.context.createImageData(100, 100)
          let imageData = this.context.createImageData(imageDataNum)
          for (let i = 0; i < imageData.data.length; i += 4) {
            imageData.data[i + 0] = 112
            imageData.data[i + 1] = 112
            imageData.data[i + 2] = 112
            imageData.data[i + 3] = 255
          }
          this.context.putImageData(imageData, 10, 10)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

#### putImageData

putImageData(imageData: ImageData, dx: number | string, dy: number | string, dirtyX: number | string, dirtyY: number | string, dirtyWidth: number | string, dirtyHeight: number | string): void

使用[ImageData](ImageData.md)数据裁剪后填充至新的矩形区域。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明imageData[ImageData](ImageData.md)是

包含像素值的ImageData对象。

异常值undefined或null按无效值处理，不进行绘制。

dxnumber | string10+是

填充区域在x轴方向的偏移量。

异常值undefined、null、NaN和Infinity按0处理。

默认单位：vp

dynumber | string10+是

填充区域在y轴方向的偏移量。

异常值undefined、null、NaN和Infinity按0处理。

默认单位：vp

dirtyXnumber | string10+是

源图像数据矩形裁切范围左上角距离源图像左上角的x轴偏移量。

异常值undefined、null、NaN和Infinity按0处理。

默认单位：vp

dirtyYnumber | string10+是

源图像数据矩形裁切范围左上角距离源图像左上角的y轴偏移量。

异常值undefined、null、NaN和Infinity按0处理。

默认单位：vp

dirtyWidthnumber | string10+是

源图像数据矩形裁切范围的宽度。

异常值undefined、null、NaN和Infinity按0处理。

默认单位：vp

dirtyHeightnumber | string10+是

源图像数据矩形裁切范围的高度。

异常值undefined、null、NaN和Infinity按0处理。

默认单位：vp

**示例：**

```ets
// xxx.ets
@Entry
@Component
struct PutImageData {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('rgb(213,213,213)')
        .onReady(() => {
          let imageDataNum = this.context.createImageData(100, 100)
          let imageData = this.context.createImageData(imageDataNum)
          for (let i = 0; i < imageData.data.length; i += 4) {
            imageData.data[i + 0] = 112
            imageData.data[i + 1] = 112
            imageData.data[i + 2] = 112
            imageData.data[i + 3] = 255
          }
          this.context.putImageData(imageData, 10, 10, 0, 0, 100, 50)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

#### setLineDash

setLineDash(segments: number[]): void

设置画布的虚线样式。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明segmentsnumber[]是

描述线段如何交替和线段间距长度的数组。

异常值undefined或null按无效值处理。

默认单位：vp

**示例：**

```ets
// xxx.ets
@Entry
@Component
struct SetLineDash {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#D5D5D5')
        .onReady(() =>{
          this.context.arc(100, 75, 50, 0, 6.28)
          this.context.setLineDash([10,20])
          this.context.stroke()
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

#### getLineDash

getLineDash(): number[]

获得当前画布的虚线样式。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

类型说明number[]

返回数组，该数组用来描述线段如何交替和间距长度。

默认单位：vp

**示例：**

```ets
// xxx.ets
@Entry
@Component
struct CanvasGetLineDash {
  @State message: string = 'Hello World'
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Row() {
      Column() {
        Text(this.message)
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
        Canvas(this.context)
          .width('100%')
          .height('100%')
          .backgroundColor('#D5D5D5')
          .onReady(() => {
            this.context.arc(100, 75, 50, 0, 6.28)
            this.context.setLineDash([10, 20])
            this.context.stroke()
            let res = this.context.getLineDash()
            this.message = JSON.stringify(res)
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

#### transferFromImageBitmap

transferFromImageBitmap(bitmap: ImageBitmap): void

显示给定的ImageBitmap对象。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明bitmap[ImageBitmap](ImageBitmap.md)是待显示的ImageBitmap对象。

**示例：**

```ets
// xxx.ets
@Entry
@Component
struct TransferFromImageBitmap {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)
  private offContext: OffscreenCanvasRenderingContext2D = new OffscreenCanvasRenderingContext2D(600, 600, this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('rgb(213,213,213)')
        .onReady(() =>{
          let imageData = this.offContext.createImageData(100, 100)
          for (let i = 0; i < imageData.data.length; i += 4) {
            imageData.data[i + 0] = 255
            imageData.data[i + 1] = 0
            imageData.data[i + 2] = 60
            imageData.data[i + 3] = 80
          }
          this.offContext.putImageData(imageData, 10, 10)
          let image = this.offContext.transferToImageBitmap()
          this.context.transferFromImageBitmap(image)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

#### toDataURL

toDataURL(type?: string, quality?: any): string

生成一个包含图片展示的URL，该接口存在内存拷贝行为，高耗时，应避免频繁使用。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明typestring否

用于指定图像格式。

可选参数为："image/png"，"image/jpeg"，"image/webp"。

异常值undefined或null按默认值处理。

默认值：image/png

qualityany否

在指定图片格式为image/jpeg或image/webp的情况下，可以从0到1的区间内选择图片的质量。如果超出取值范围，将会使用默认值0.92。

异常值undefined、null、NaN和Infinity按默认值处理。

默认值：0.92

**返回值：**

类型说明string图像的URL地址。

**示例：**

```ets
// xxx.ets
@Entry
@Component
struct CanvasExample {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)
  @State toDataURL: string = ""

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width(100)
        .height(100)
        .onReady(() =>{
          this.context.fillStyle = "#00ff00"
          this.context.fillRect(0,0,100,100)
          this.toDataURL = this.context.toDataURL("image/png", 0.92)
        })
      Text(this.toDataURL)
    }
    .width('100%')
    .height('100%')
    .backgroundColor('#ffff00')
  }
}
```

#### restore

restore(): void

恢复保存的绘图上下文。

当restore()次数未超出save()次数时，从栈中弹出存储的绘制状态并恢复CanvasRenderingContext2D对象的属性、剪切路径和变换矩阵的值。

当restore()次数超出save()次数时，此方法不做任何改变。

当没有保存状态时，此方法不做任何改变。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```ets
// xxx.ets
@Entry
@Component
struct CanvasExample {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          this.context.save() // save the default state
          this.context.fillStyle = "#00ff00"
          this.context.fillRect(20, 20, 100, 100)
          this.context.restore() // restore to the default state
          this.context.fillRect(150, 75, 100, 100)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

#### save

save(): void

将当前状态放入栈中，保存canvas的全部状态，通常在需要保存绘制状态时调用。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```ets
// xxx.ets
@Entry
@Component
struct CanvasExample {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          this.context.save() // save the default state
          this.context.fillStyle = "#00ff00"
          this.context.fillRect(20, 20, 100, 100)
          this.context.restore() // restore to the default state
          this.context.fillRect(150, 75, 100, 100)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

#### createLinearGradient

createLinearGradient(x0: number, y0: number, x1: number, y1: number): CanvasGradient

创建一个线性渐变色。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明x0number是

起点的x轴坐标。

异常值undefined和null会导致此接口返回undefined，NaN和Infinity按无效值处理。

默认单位：vp

y0number是

起点的y轴坐标。

异常值undefined和null会导致此接口返回undefined，NaN和Infinity按无效值处理。

默认单位：vp

x1number是

终点的x轴坐标。

异常值undefined和null会导致此接口返回undefined，NaN和Infinity按无效值处理。

默认单位：vp

y1number是

终点的y轴坐标。

异常值undefined和null会导致此接口返回undefined，NaN和Infinity按无效值处理。

默认单位：vp

**返回值：**

类型说明[CanvasGradient](CanvasGradient.md)新的CanvasGradient对象，用于在canvas上创建渐变效果。

**示例：**

```ets
// xxx.ets
@Entry
@Component
struct CreateLinearGradient {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('rgb(213,213,213)')
        .onReady(() =>{
          let grad = this.context.createLinearGradient(50,0, 300,100)
          grad.addColorStop(0.0, 'rgb(39,135,217)')
          grad.addColorStop(0.5, 'rgb(255,238,240)')
          grad.addColorStop(1.0, 'rgb(23,169,141)')
          this.context.fillStyle = grad
          this.context.fillRect(0, 0, 400, 400)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

#### createRadialGradient

createRadialGradient(x0: number, y0: number, r0: number, x1: number, y1: number, r1: number): CanvasGradient

创建一个径向渐变色。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明x0number是

起始圆的x轴坐标。

异常值undefined和null会导致此接口返回undefined，NaN和Infinity按无效值处理。

默认单位：vp

y0number是

起始圆的y轴坐标。

异常值undefined和null会导致此接口返回undefined，NaN和Infinity按无效值处理。

默认单位：vp

r0number是

起始圆的半径。必须是非负且有限的。

异常值undefined和null会导致此接口返回undefined，NaN和Infinity按无效值处理。

默认单位：vp

x1number是

终点圆的x轴坐标。

异常值undefined和null会导致此接口返回undefined，NaN和Infinity按无效值处理。

默认单位：vp

y1number是

终点圆的y轴坐标。

异常值undefined和null会导致此接口返回undefined，NaN和Infinity按无效值处理。

默认单位：vp

r1number是

终点圆的半径。必须为非负且有限的。

异常值undefined和null会导致此接口返回undefined，NaN和Infinity按无效值处理。

默认单位：vp

**返回值：**

类型说明[CanvasGradient](CanvasGradient.md)新的CanvasGradient对象，用于在canvas上创建渐变效果。

**示例：**

```ets
// xxx.ets
@Entry
@Component
struct CreateRadialGradient {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('rgb(213,213,213)')
        .onReady(() => {
          let grad = this.context.createRadialGradient(200, 200, 50, 200, 200, 200)
          grad.addColorStop(0.0, 'rgb(39,135,217)')
          grad.addColorStop(0.5, 'rgb(255,238,240)')
          grad.addColorStop(1.0, 'rgb(112,112,112)')
          this.context.fillStyle = grad
          this.context.fillRect(0, 0, 440, 440)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

#### createConicGradient10+

createConicGradient(startAngle: number, x: number, y: number): CanvasGradient

创建一个圆锥渐变色。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明startAnglenumber是

开始渐变的角度。角度测量从中心右侧水平开始，顺时针移动。

异常值undefined和null按0处理，NaN和Infinity按无效值处理。

单位：弧度

xnumber是

圆锥渐变的中心x轴坐标。

异常值undefined和null按0处理，NaN和Infinity按无效值处理。

默认单位：vp

ynumber是

圆锥渐变的中心y轴坐标。

异常值undefined和null按0处理，NaN和Infinity按无效值处理。

默认单位：vp

**返回值：**

类型说明[CanvasGradient](CanvasGradient.md)新的CanvasGradient对象，用于在canvas上创建渐变效果。

**示例：**

```ets
// xxx.ets
@Entry
@Component
struct CanvasExample {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffffff')
        .onReady(() => {
          let grad = this.context.createConicGradient(0, 50, 80)
          grad.addColorStop(0.0, '#ff0000')
          grad.addColorStop(0.5, '#ffffff')
          grad.addColorStop(1.0, '#00ff00')
          this.context.fillStyle = grad
          this.context.fillRect(0, 30, 100, 100)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

#### on('onAttach')13+

on(type: 'onAttach', callback: () => void): void

订阅CanvasRenderingContext2D与Canvas组件发生绑定的场景。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明typestring是

订阅CanvasRenderingContext2D与Canvas组件发生绑定的回调。

异常值undefined或null按无效值处理。

callback() => void是

订阅CanvasRenderingContext2D与Canvas组件发生绑定后触发的回调。

异常值undefined或null按无效值处理。

CanvasRenderingContext2D对象在同一时间只能与一个Canvas组件绑定。

当CanvasRenderingContext2D对象和Canvas组件发生绑定时，会触发'onAttach'回调，表示可以获取到[canvas](#ZH-CN_TOPIC_0000002497444936__canvas13)。

避免在'onAttach'中执行绘制方法，应保证Canvas组件已经'[onReady](Canvas.md#ZH-CN_TOPIC_0000002529284905__事件)'再进行绘制。

触发'onAttach'回调的一般场景：

1、Canvas组件创建时绑定CanvasRenderingContext2D对象;

2、CanvasRenderingContext2D对象新绑定一个Canvas组件时。

#### on('onDetach')13+

on(type: 'onDetach', callback: () => void): void

订阅CanvasRenderingContext2D与Canvas组件解除绑定的场景。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明typestring是

订阅CanvasRenderingContext2D与Canvas组件解除绑定的回调。

异常值undefined或null按无效值处理。

callback() => void是

订阅CanvasRenderingContext2D与Canvas组件解除绑定后触发的回调。

异常值undefined或null按无效值处理。

当CanvasRenderingContext2D对象和Canvas组件解除绑定时，会触发'onDetach'回调，表示应停止绘制行为。

触发'onDetach'回调的一般场景：

1、Canvas组件销毁时解除绑定CanvasRenderingContext2D对象;

2、CanvasRenderingContext2D对象新绑定一个Canvas组件，会先解除已有的绑定。

#### off('onAttach')13+

off(type: 'onAttach', callback?: () => void): void

取消订阅CanvasRenderingContext2D与Canvas组件发生绑定的场景。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明typestring是

取消订阅CanvasRenderingContext2D与Canvas组件发生绑定的回调。

异常值undefined或null按无效值处理。

callback() => void否

为空表示取消所有订阅CanvasRenderingContext2D与Canvas组件发生绑定后触发的回调。

非空则取消订阅发生绑定对应的回调。

异常值undefined或null按无效值处理。

#### off('onDetach')13+

off(type: 'onDetach', callback?: () => void): void

取消订阅CanvasRenderingContext2D与Canvas组件解除绑定的场景。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明typestring是

取消订阅CanvasRenderingContext2D与Canvas组件解除绑定的回调。

异常值undefined或null按无效值处理。

callback() => void否

为空代表取消所有订阅CanvasRenderingContext2D与Canvas组件解除绑定后触发的回调。

非空代表取消订阅解除绑定对应的回调。

异常值undefined或null按无效值处理。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { FrameNode } from '@kit.ArkUI'

// xxx.ets
@Entry
@Component
struct AttachDetachExample {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)
  private scroller: Scroller = new Scroller()
  private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
  private node: FrameNode | null = null
  attachCallback = () => {
    console.info('CanvasRenderingContext2D attached to the canvas frame node.')
    this.node = this.context.canvas
  }
  detachCallback = () => {
    console.info('CanvasRenderingContext2D detach from the canvas frame node.')
    this.node = null
  }

  aboutToAppear(): void {
    try {
      this.context.on('onAttach', this.attachCallback)
      this.context.on('onDetach', this.detachCallback)
    } catch (error) {
      let e: BusinessError = error as BusinessError;
      console.error(`Error code: ${e.code}, message: ${e.message}`);
    }
  }

  aboutToDisappear(): void {
    try {
      this.context.off('onAttach')
      this.context.off('onDetach')
    } catch (error) {
      let e: BusinessError = error as BusinessError;
      console.error(`Error code: ${e.code}, message: ${e.message}`);
    }
  }

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Scroll(this.scroller) {
        Flex({ direction: FlexDirection.Column }) {
          ForEach(this.arr, (item: number) => {
            Row() {
              if (item == 3) {
                Canvas(this.context)
                  .width('100%')
                  .height(150)
                  .backgroundColor('rgb(213,213,213)')
                  .onReady(() => {
                    this.context.font = '30vp sans-serif'
                    this.node?.commonEvent.setOnVisibleAreaApproximateChange(
                      { ratios: [0, 1], expectedUpdateInterval: 10 },
                      (isVisible: boolean, currentRatio: number) => {
                        if (!isVisible && currentRatio <= 0.0) {
                          console.info('Canvas is completely invisible.')
                        }
                        if (isVisible && currentRatio >= 1.0) {
                          console.info('Canvas is fully visible.')
                        }
                      }
                    )
                  })
              } else {
                Text(item.toString())
                  .width('100%')
                  .height(150)
                  .backgroundColor('rgb(39,135,217)')
                  .borderRadius(15)
                  .fontSize(16)
                  .textAlign(TextAlign.Center)
                  .margin({ top: 5 })
              }
            }
          }, (item: number) => item.toString())
        }
      }
      .width('90%')
      .scrollBar(BarState.Off)
      .scrollable(ScrollDirection.Vertical)
    }
    .width('100%')
    .height('100%')
  }
}
```

#### startImageAnalyzer12+

startImageAnalyzer(config: ImageAnalyzerConfig): Promise<void>

配置并启动AI分析功能，使用Promise异步回调。使用前需先[启用图像AI分析能力](Canvas.md#ZH-CN_TOPIC_0000002529284905__enableanalyzer12)。

该方法调用时，将截取调用时刻的画面帧进行分析，使用时需注意启动分析的时机，避免出现画面和分析内容不一致的情况。

未执行完重复调用该方法会触发错误回调。示例代码同stopImageAnalyzer。

分析类型不支持动态修改。

当检测到画面有变化时，分析结果将自动销毁，可重新调用本接口启动分析。

该特性依赖设备能力，不支持该能力的情况下，将返回错误码。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明config[ImageAnalyzerConfig](图像类型定义.md#ZH-CN_TOPIC_0000002497604902__imageanalyzerconfig12)是

执行AI分析所需要的入参，用于配置AI分析功能。

异常值undefined或null按无效值处理。

**返回值：**

类型说明Promise<void>Promise对象，无返回结果。

**错误码：**

以下错误码的详细介绍请参见[AI分析类库错误码](图像AI分析错误码.md)。

错误码ID错误信息110001Image analysis feature is unsupported.110002Image analysis is currently being executed.110003Image analysis is stopped.

#### stopImageAnalyzer12+

stopImageAnalyzer(): void

停止AI分析功能，AI分析展示的内容将被销毁。

在startImageAnalyzer方法未返回结果时调用本方法，会触发其错误回调。

该特性依赖设备能力。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```ets
// xxx.ets
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct ImageAnalyzerExample {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)
  private config: ImageAnalyzerConfig = {
    types: [ImageAnalyzerType.SUBJECT, ImageAnalyzerType.TEXT]
  }
  // 'common/images/example.png'需要替换为开发者所需的图像资源文件
  private img = new ImageBitmap('common/images/example.png')
  private aiController: ImageAnalyzerController = new ImageAnalyzerController()
  private options: ImageAIOptions = {
    types: [ImageAnalyzerType.SUBJECT, ImageAnalyzerType.TEXT],
    aiController: this.aiController
  }

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
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
        .width(200)
        .height(200)
        .enableAnalyzer(true)
        .onReady(() => {
          this.context.drawImage(this.img, 0, 0, 200, 200)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

#### CanvasDirection类型说明

type CanvasDirection = "inherit" | "ltr" | "rtl"

定义当前文本方向的类型。取值类型为下表类型中的并集。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

类型说明inherit继承canvas组件通用属性已设定的文本方向。ltr从左往右。rtl从右往左。

#### CanvasFillRule类型说明

type CanvasFillRule = "evenodd" | "nonzero"

定义用于确定点是在路径内还是路径外的填充样式算法的类型。取值类型为下表类型中的并集。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

类型说明evenodd

奇偶规则。

此规则通过从画布上的某点向任意方向发射一条射线，并统计图形路径与射线的交点数量来判断该点是否在图形内部。如果交点数量是奇数，则该点在图形内部，否则在图形外部。

nonzero

非零规则。

此规则通过从画布上的某点向任意方向发射一条射线，并检查图形路径与射线的交点来判断该点是否在图形内部。初始计数为0，为路径的每一段线段指定一个方向值，每当路径从左向右穿过射线时加1，从右向左穿过时减1。如果最终的结果是0，则该点在图形外部，否则在图形内部。

**示例**

```ets
// xxx.ets
@Entry
@Component
struct Index {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('rgb(213, 213, 213)')
        .onReady(() => {
          let offContext = this.offCanvas.getContext("2d", this.settings)
          offContext.font = '60px sans-serif'
          offContext.fillStyle = 'rgb(39, 135, 217)';
          // 非零环绕规则 (nonzero)
          offContext.beginPath();
          offContext.arc(100, 100, 60, 0, Math.PI * 2);
          offContext.arc(100, 100, 20, 0, Math.PI * 2);
          offContext.fill('nonzero'); // 使用非零环绕规则
          offContext.fillText('nonzero', 65, 200)
          // 奇偶环绕规则 (evenodd)
          offContext.beginPath();
          offContext.arc(250, 100, 60, 0, Math.PI * 2);
          offContext.arc(250, 100, 20, 0, Math.PI * 2);
          offContext.fill('evenodd'); // 使用奇偶环绕规则
          offContext.fillText('evenodd', 215, 200)
          let image = this.offCanvas.transferToImageBitmap()
          this.context.transferFromImageBitmap(image)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

#### CanvasLineCap类型说明

type CanvasLineCap = "butt" | "round" | "square"

定义绘制每条线段端点的类型。取值类型为下表类型中的并集。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

类型说明butt线条两端为平行线，不额外扩展。round在线条两端延伸半个圆，直径等于线宽。square在线条两端延伸一个矩形，宽度等于线宽的一半，高度等于线宽。

#### CanvasLineJoin类型说明

type CanvasLineJoin = "bevel" | "miter" | "round"

定义长度不为0的两个连接部分（线段、圆弧和曲线）的类型。取值类型为下表类型中的并集。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

类型说明bevel在线段相连处使用三角形为底填充， 每个部分矩形拐角独立。miter在相连部分的外边缘处进行延伸，使其相交于一点，形成一个菱形区域，该属性可以通过设置miterLimit属性展现效果。round在线段相连处绘制一个扇形，扇形的圆角半径是线段的宽度。

#### CanvasTextAlign类型说明

type CanvasTextAlign = "center" | "end" | "left" | "right" | "start"

定义文本对齐方式的类型。取值类型为下表类型中的并集。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

类型说明center文本居中对齐。start文本对齐界线开始的地方。end文本对齐界线结束的地方。left文本左对齐。right文本右对齐。

#### CanvasTextBaseline类型说明

type CanvasTextBaseline = "alphabetic" | "bottom" | "hanging" | "ideographic" | "middle" | "top"

定义文本基线类型。取值类型为下表类型中的并集。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

类型说明alphabetic文本基线是标准的字母基线。bottom文本基线在文本块的底部。 与ideographic基线的区别在于ideographic基线不需要考虑下行字母。hanging文本基线是悬挂基线。ideographic文字基线是表意字基线；如果字符本身超出了alphabetic基线，那么ideographic基线位置在字符本身的底部。middle文本基线在文本块的中间。top文本基线在文本块的顶部。

#### ImageSmoothingQuality类型说明

type ImageSmoothingQuality = "high" | "low" | "medium"

定义图片平滑度类型。取值类型为下表类型中的并集。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

类型说明low低画质medium中画质high高画质

#### TextMetrics

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明widthnumber是否只读属性，文本方块的宽度。heightnumber是否只读属性，文本方块的高度。actualBoundingBoxAscentnumber是否只读属性，从[CanvasRenderingContext2D.textBaseline](#ZH-CN_TOPIC_0000002497444936__canvastextbaseline类型说明)属性标明的水平线到渲染文本的矩形边界顶部的距离。actualBoundingBoxDescentnumber是否只读属性，从[CanvasRenderingContext2D.textBaseline](#ZH-CN_TOPIC_0000002497444936__canvastextbaseline类型说明)属性标明的水平线到渲染文本的矩形边界底部的距离。actualBoundingBoxLeftnumber是否只读属性，平行于基线，从[CanvasRenderingContext2D.textAlign](#ZH-CN_TOPIC_0000002497444936__canvastextalign类型说明)属性确定的对齐点到文本矩形边界左侧的距离。actualBoundingBoxRightnumber是否只读属性，平行于基线，从[CanvasRenderingContext2D.textAlign](#ZH-CN_TOPIC_0000002497444936__canvastextalign类型说明)属性确定的对齐点到文本矩形边界右侧的距离。alphabeticBaselinenumber是否只读属性，从[CanvasRenderingContext2D.textBaseline](#ZH-CN_TOPIC_0000002497444936__canvastextbaseline类型说明)属性标明的水平线到线框的 alphabetic 基线的距离。emHeightAscentnumber是否只读属性，从[CanvasRenderingContext2D.textBaseline](#ZH-CN_TOPIC_0000002497444936__canvastextbaseline类型说明)属性标明的水平线到线框中 em 方块顶部的距离。emHeightDescentnumber是否只读属性，从[CanvasRenderingContext2D.textBaseline](#ZH-CN_TOPIC_0000002497444936__canvastextbaseline类型说明)属性标明的水平线到线框中 em 方块底部的距离。fontBoundingBoxAscentnumber是否只读属性，从[CanvasRenderingContext2D.textBaseline](#ZH-CN_TOPIC_0000002497444936__canvastextbaseline类型说明)属性标明的水平线到渲染文本的所有字体的矩形最高边界顶部的距离。fontBoundingBoxDescentnumber是否只读属性，从[CanvasRenderingContext2D.textBaseline](#ZH-CN_TOPIC_0000002497444936__canvastextbaseline类型说明)属性标明的水平线到渲染文本的所有字体的矩形边界最底部的距离。hangingBaselinenumber是否只读属性，从[CanvasRenderingContext2D.textBaseline](#ZH-CN_TOPIC_0000002497444936__canvastextbaseline类型说明)属性标明的水平线到线框的 hanging 基线的距离。ideographicBaselinenumber是否只读属性，从[CanvasRenderingContext2D.textBaseline](#ZH-CN_TOPIC_0000002497444936__canvastextbaseline类型说明)属性标明的水平线到线框的 ideographic 基线的距离。

#### RenderingContextSettings

用来配置CanvasRenderingContext2D对象的参数，包括是否开启抗锯齿。

RenderingContextSettings的抗锯齿效果对文本绘制无影响。

#### constructor

constructor(antialias?: boolean)

构造CanvasRenderingContext2D对象，支持配置开启抗锯齿。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明antialiasboolean否

表明canvas是否开启抗锯齿。

异常值undefined按默认值处理。

false：表示不开启抗锯齿功能，true：表示开启抗锯齿。

默认值：false

#### 属性

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明antialiasboolean否是

表明canvas是否开启抗锯齿。

异常值undefined按默认值处理。

false：表示不开启抗锯齿功能，true：表示开启抗锯齿。

默认值：false