# Class (Font)

描述字型绘制时所使用的属性，如大小、字体等。

-

本模块首批接口从API version 11开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

-

本模块使用屏幕物理像素单位px。

-

本模块为单线程模型策略，需要调用方自行管理线程安全和上下文状态的切换。

#### 导入模块

```ets
import { drawing } from '@kit.ArkGraphics2D';
```

#### isSubpixel12+

isSubpixel(): boolean

获取字型是否使用次像素渲染。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

类型说明boolean返回字型是否使用次像素渲染的结果，true表示使用，false表示不使用。

**示例：**

```ets
import {drawing} from '@kit.ArkGraphics2D';

let font: drawing.Font = new drawing.Font();
font.enableSubpixel(true)
console.info("values=" + font.isSubpixel());
```

#### isLinearMetrics12+

isLinearMetrics(): boolean

获取字型是否可以线性缩放。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

类型说明boolean返回字型是否可线性缩放的结果，true表示可线性缩放，false表示不可线性缩放。

**示例：**

```ets
import {drawing} from '@kit.ArkGraphics2D';

let font: drawing.Font = new drawing.Font();
font.enableLinearMetrics(true)
console.info("values=" + font.isLinearMetrics());
```

#### getSkewX12+

getSkewX(): number

获取字型在x轴方向上的倾斜度。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

类型说明number返回字型在x轴方向上的倾斜度。

**示例：**

```ets
import {drawing} from '@kit.ArkGraphics2D';

let font: drawing.Font = new drawing.Font();
font.setSkewX(-1)
console.info("values=" + font.getSkewX());
```

#### isEmbolden12+

isEmbolden(): boolean

获取字型是否设置了粗体效果。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

类型说明boolean返回字型是否设置粗体效果的结果，true表示设置了粗体效果，false表示未设置粗体效果。

**示例：**

```ets
import {drawing} from '@kit.ArkGraphics2D';

let font: drawing.Font = new drawing.Font();
font.enableEmbolden(true);
console.info("values=" + font.isEmbolden());
```

#### getScaleX12+

getScaleX(): number

获取字型在x轴方向上的缩放比例。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

类型说明number返回字型在x轴方向上的缩放比例。

**示例：**

```ets
import {drawing} from '@kit.ArkGraphics2D';

let font: drawing.Font = new drawing.Font();
font.setScaleX(2);
console.info("values=" + font.getScaleX());
```

#### getHinting12+

getHinting(): FontHinting

获取字型轮廓效果。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

类型说明[FontHinting](Enums.md#ZH-CN_TOPIC_0000002529285977__fonthinting12)返回字型轮廓效果。

**示例：**

```ets
import {drawing} from '@kit.ArkGraphics2D';

let font: drawing.Font = new drawing.Font();
console.info("values=" + font.getHinting());
```

#### getEdging12+

getEdging(): FontEdging

获取字型边缘效果。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

类型说明[FontEdging](Enums.md#ZH-CN_TOPIC_0000002529285977__fontedging12)返回字型边缘效果。

**示例：**

```ets
import {drawing} from '@kit.ArkGraphics2D';

let font: drawing.Font = new drawing.Font();
console.info("values=" + font.getEdging());
```

#### enableSubpixel

enableSubpixel(isSubpixel: boolean): void

使能字型亚像素级别的文字绘制，显示效果平滑。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

参数名类型必填说明isSubpixelboolean是表示是否使能字型亚像素级别的文字绘制。true表示使能，false表示不使能。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types.

**示例：**

```ets
import { drawing } from '@kit.ArkGraphics2D';

let font = new drawing.Font();
font.enableSubpixel(true);
```

#### enableEmbolden

enableEmbolden(isEmbolden: boolean): void

使能字型粗体。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

参数名类型必填说明isEmboldenboolean是表示是否使能字型粗体。true表示使能，false表示不使能。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types.

**示例：**

```ets
import { drawing } from '@kit.ArkGraphics2D';

let font = new drawing.Font();
font.enableEmbolden(true);
```

#### enableLinearMetrics

enableLinearMetrics(isLinearMetrics: boolean): void

使能字型的线性缩放。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

参数名类型必填说明isLinearMetricsboolean是表示是否使能字型的线性缩放。true表示使能，false表示不使能。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types.

**示例：**

```ets
import { drawing } from '@kit.ArkGraphics2D';

let font = new drawing.Font();
font.enableLinearMetrics(true);
```

#### setSize

setSize(textSize: number): void

设置字型大小。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

参数名类型必填说明textSizenumber是字型大小，该参数为浮点数，为负数时字型大小会被置为0。字型大小为0时，绘制的文字不会显示。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types;3.Parameter verification failed.

**示例：**

```ets
import { drawing } from '@kit.ArkGraphics2D';

let font = new drawing.Font();
font.setSize(5);
```

#### getSize

getSize(): number

获取字型大小。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

类型说明number字型大小，浮点数。

**示例：**

```ets
import { drawing } from '@kit.ArkGraphics2D';

let font = new drawing.Font();
font.setSize(5);
let fontSize = font.getSize();
```

#### setTypeface

setTypeface(typeface: Typeface): void

为字型设置字体样式（包括字体名称、粗细、斜体等属性）。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

参数名类型必填说明typeface[Typeface](Class (Typeface).md)是字体样式，包括字体名称、粗细、斜体等属性。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types.

**示例：**

```ets
import { drawing } from '@kit.ArkGraphics2D';

let font = new drawing.Font();
font.setTypeface(new drawing.Typeface());
```

#### getTypeface

getTypeface(): Typeface

获取字体。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

类型说明[Typeface](Class (Typeface).md)字体。

**示例：**

```ets
import { drawing } from '@kit.ArkGraphics2D';

let font = new drawing.Font();
let typeface = font.getTypeface();
```

#### getMetrics

getMetrics(): FontMetrics

获取与字体关联的FontMetrics属性。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

类型说明[FontMetrics](Interfaces (其他).md#ZH-CN_TOPIC_0000002497446006__fontmetrics)FontMetrics属性。

**示例：**

```ets
import { drawing } from '@kit.ArkGraphics2D';

let font = new drawing.Font();
let metrics = font.getMetrics();
```

#### measureText

measureText(text: string, encoding: TextEncoding): number

测量文本的宽度。

此接口用于测量原始字符串的文本宽度，若想测量排版后的文本宽度，建议使用[measure.measureText](Class (MeasureUtils).md#ZH-CN_TOPIC_0000002497604780__measuretext12)替代。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

参数名类型必填说明textstring是文本内容。encoding[TextEncoding](Enums.md#ZH-CN_TOPIC_0000002529285977__textencoding)是编码格式。

**返回值：**

类型说明number文本的宽度，浮点数。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types.

**示例：**

```ets
import { drawing } from '@kit.ArkGraphics2D';

let font = new drawing.Font();
font.measureText("drawing", drawing.TextEncoding.TEXT_ENCODING_UTF8);
```

#### measureSingleCharacter12+

measureSingleCharacter(text: string): number

测量单个字符的宽度。当前字型中的字体不支持待测量字符时，退化到使用系统字体测量字符宽度。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数**

参数名类型必填说明textstring是待测量的单个字符，字符串的长度必须为1。

**返回值：**

类型说明number字符的宽度，浮点数。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types;3.Parameter verification failed.

**示例：**

```ets
import { RenderNode } from '@kit.ArkUI';
import { drawing } from '@kit.ArkGraphics2D';

class DrawingRenderNode extends RenderNode {
  draw(context : DrawContext) {
    const canvas = context.canvas;
    const font = new drawing.Font();
    font.setSize(20);
    let width = font.measureSingleCharacter("你");
  }
}
```

#### measureSingleCharacterWithFeatures20+

measureSingleCharacterWithFeatures(text: string, features: Array<FontFeature>): number

测量单个字符的宽度，字符带有字体特征。当前字型中的字体不支持待测量字符时，退化到使用系统字体测量字符宽度。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数**

参数名类型必填说明textstring是待测量的单个字符。字符串长度必须为1。featuresArray<[FontFeature](Interfaces (其他).md#ZH-CN_TOPIC_0000002497446006__fontfeature20)>是字体特征对象数组。参数为空数组时使用TTF(TrueType Font)文件中预设的字体特征。

**返回值：**

类型说明number字符的宽度，浮点数，单位为px。

**错误码：**

以下错误码的详细介绍请参见[图形绘制与显示错误码](图形绘制与显示错误码.md)。

错误码ID错误信息25900001Parameter error. Possible causes: Incorrect parameter range.

**示例：**

```ets
import { RenderNode } from '@kit.ArkUI';
import { drawing } from '@kit.ArkGraphics2D';

class DrawingRenderNode extends RenderNode {
  draw(context : DrawContext) {
    const font = new drawing.Font();
    font.setSize(20);
    let fontFeatures : Array<drawing.FontFeature> = [];
    fontFeatures.push({name: 'calt', value: 0});
    let width = font.measureSingleCharacterWithFeatures("你", fontFeatures);
  }
}
```

#### setScaleX12+

setScaleX(scaleX: number): void

设置字型对象在x轴上的缩放比例。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

参数名类型必填说明scaleXnumber是文本在x轴上的缩放比例，该参数为浮点数。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types.

**示例：**

```ets
import { RenderNode } from '@kit.ArkUI';
import { common2D, drawing } from '@kit.ArkGraphics2D';

class DrawingRenderNode extends RenderNode {
  draw(context : DrawContext) {
    const canvas = context.canvas;
    const pen = new drawing.Pen();
    pen.setStrokeWidth(5);
    pen.setColor({alpha: 255, red: 255, green: 0, blue: 0});
    canvas.attachPen(pen);
    let font = new drawing.Font();
    font.setSize(100);
    font.setScaleX(2);
    const textBlob = drawing.TextBlob.makeFromString("hello", font, drawing.TextEncoding.TEXT_ENCODING_UTF8);
    canvas.drawTextBlob(textBlob, 200, 200);
  }
}
```

#### setSkewX12+

setSkewX(skewX: number): void

设置字型对象在x轴上的倾斜比例。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

参数名类型必填说明skewXnumber是文本在x轴上的倾斜比例，正数表示往左边倾斜，负数表示往右边倾斜，该参数为浮点数。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types.

**示例：**

```ets
import { RenderNode } from '@kit.ArkUI';
import { common2D, drawing } from '@kit.ArkGraphics2D';

class DrawingRenderNode extends RenderNode {
  draw(context : DrawContext) {
    const canvas = context.canvas;
    const pen = new drawing.Pen();
    pen.setStrokeWidth(5);
    pen.setColor({alpha: 255, red: 255, green: 0, blue: 0});
    canvas.attachPen(pen);
    let font = new drawing.Font();
    font.setSize(100);
    font.setSkewX(1);
    const textBlob = drawing.TextBlob.makeFromString("hello", font, drawing.TextEncoding.TEXT_ENCODING_UTF8);
    canvas.drawTextBlob(textBlob, 200, 200);
  }
}
```

#### setEdging12+

setEdging(edging: FontEdging): void

设置字型边缘效果。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

参数名类型必填说明edging[FontEdging](Enums.md#ZH-CN_TOPIC_0000002529285977__fontedging12)是字型边缘效果。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3. Parameter verification failed.

**示例：**

```ets
import { drawing } from '@kit.ArkGraphics2D';

let font = new drawing.Font();
font.setEdging(drawing.FontEdging.SUBPIXEL_ANTI_ALIAS);
```

#### setHinting12+

setHinting(hinting: FontHinting): void

设置字型轮廓效果。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

参数名类型必填说明hinting[FontHinting](Enums.md#ZH-CN_TOPIC_0000002529285977__fonthinting12)是字型轮廓效果。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3. Parameter verification failed.

**示例：**

```ets
import { drawing } from '@kit.ArkGraphics2D';

let font = new drawing.Font();
font.setHinting(drawing.FontHinting.FULL);
```

#### countText12+

countText(text: string): number

获取文本所表示的字符数量。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

参数名类型必填说明textstring是文本内容。

**返回值：**

类型说明number返回文本所表示的字符数量，整数。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types.

**示例：**

```ets
import { drawing } from '@kit.ArkGraphics2D';

let font = new drawing.Font();
let resultNumber: number = font.countText('ABCDE');
console.info("count text number: " + resultNumber);
```

#### setBaselineSnap12+

setBaselineSnap(isBaselineSnap: boolean): void

当前画布矩阵轴对齐时，设置字型基线是否与像素对齐。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

参数名类型必填说明isBaselineSnapboolean是指示字型基线是否和像素对齐，true表示对齐，false表示不对齐。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types.

**示例：**

```ets
import { drawing } from '@kit.ArkGraphics2D';

let font : drawing.Font = new drawing.Font();
font.setBaselineSnap(true);
console.info("drawing font isBaselineSnap: " + font.isBaselineSnap());
```

#### isBaselineSnap()12+

isBaselineSnap(): boolean

当前画布矩阵轴对齐时，获取字型基线是否与像素对齐的结果。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

类型说明boolean返回字型基线是否与像素对齐，true为对齐，false为没有对齐。

**示例：**

```ets
import { drawing } from '@kit.ArkGraphics2D';

let font : drawing.Font = new drawing.Font();
font.setTypeface(new drawing.Typeface());
font.setBaselineSnap(true);
console.info("drawing font isBaselineSnap: " + font.isBaselineSnap());
```

#### setEmbeddedBitmaps12+

setEmbeddedBitmaps(isEmbeddedBitmaps: boolean): void

设置字型是否转换成位图处理。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

参数名类型必填说明isEmbeddedBitmapsboolean是设置字型是否转换成位图处理，true表示转换成位图处理，false表示不转换成位图处理。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types.

**示例：**

```ets
import { drawing } from '@kit.ArkGraphics2D';

let font : drawing.Font = new drawing.Font();
font.setTypeface(new drawing.Typeface());
font.setEmbeddedBitmaps(false);
console.info("draw isEmbeddedBitmaps: " + font.isEmbeddedBitmaps());
```

#### isEmbeddedBitmaps()12+

isEmbeddedBitmaps(): boolean

获取字型是否转换成位图处理的结果。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

类型说明boolean返回字型是否转换成位图处理结果，true表示转换成位图处理，false表示不转换成位图处理。

**示例：**

```ets
import { drawing } from '@kit.ArkGraphics2D';

let font : drawing.Font = new drawing.Font();
font.setTypeface(new drawing.Typeface());
font.setEmbeddedBitmaps(true);
console.info("draw isEmbeddedBitmaps: " + font.isEmbeddedBitmaps());
```

#### setForceAutoHinting12+

setForceAutoHinting(isForceAutoHinting: boolean): void

设置是否自动调整字型轮廓。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

参数名类型必填说明isForceAutoHintingboolean是是否自动调整字型轮廓，true为自动调整，false为不自动调整。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types.

**示例：**

```ets
import { drawing } from '@kit.ArkGraphics2D';

let font : drawing.Font = new drawing.Font();
font.setTypeface(new drawing.Typeface());
font.setForceAutoHinting(false);
console.info("drawing isForceAutoHinting:  " + font.isForceAutoHinting());
```

#### isForceAutoHinting12+

isForceAutoHinting(): boolean

获取字型轮廓是否自动调整的结果。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

类型说明boolean返回字型轮廓是否自动调整，true为自动调整，false为不自动调整。

**示例：**

```ets
import { drawing } from '@kit.ArkGraphics2D';

let font : drawing.Font = new drawing.Font();
font.setTypeface(new drawing.Typeface());
font.setForceAutoHinting(false);
console.info("drawing isForceAutoHinting:  " + font.isForceAutoHinting());
```

#### getWidths12+

getWidths(glyphs: Array<number>): Array<number>

获取字形数组中每个字形对应的宽度。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

参数名类型必填说明glyphsArray<number>是字形索引数组，可由[textToGlyphs](#ZH-CN_TOPIC_0000002529285967__texttoglyphs12)生成。

**返回值：**

类型说明Array<number>返回字形宽度数组。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types.

**示例：**

```ets
import { drawing } from '@kit.ArkGraphics2D';

let font: drawing.Font = new drawing.Font();
let text: string = 'hello world';
let glyphs: number[] = font.textToGlyphs(text);
let fontWidths: Array<number> = font.getWidths(glyphs);
for (let index = 0; index < fontWidths.length; index++) {
  console.info("get fontWidths[", index, "]:", fontWidths[index]);
}
```

#### textToGlyphs12+

textToGlyphs(text: string, glyphCount?: number): Array<number>

将文本转换为字形索引。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

参数名类型必填说明textstring是文本字符串。glyphCountnumber否文本表示的字符数量，必须与[countText](#ZH-CN_TOPIC_0000002529285967__counttext12)获取的值相等，默认为text的字符数量，该参数为整数。

**返回值：**

类型说明Array<number>返回转换得到的字形索引数组。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types.

**示例：**

```ets
import { drawing } from '@kit.ArkGraphics2D';

let font : drawing.Font = new drawing.Font();
let text : string = 'hello world';
let glyphs : number[] = font.textToGlyphs(text);
console.info("drawing text toglyphs OnTestFunction num =  " + glyphs.length );
```

#### getBounds18+

getBounds(glyphs: Array<number>): Array<common2D.Rect>

获取字形数组中每个字形的边界矩形。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

参数名类型必填说明glyphsArray<number>是字形索引数组，可由[textToGlyphs](#ZH-CN_TOPIC_0000002529285967__texttoglyphs12)生成。

**返回值：**

类型说明Array<[common2D.Rect](@ohos.graphics.common2D (2D图形通用数据类型).md#ZH-CN_TOPIC_0000002529445937__rect)>返回字形边界矩形数组。

**示例：**

```ets
import { common2D, drawing } from '@kit.ArkGraphics2D';

let font: drawing.Font = new drawing.Font();
let text: string = 'hello world';
let glyphs: number[] = font.textToGlyphs(text);
let fontBounds: Array<common2D.Rect> = font.getBounds(glyphs);
for (let index = 0; index < fontBounds.length; index++) {
  console.info("get fontWidths[", index, "] left:", fontBounds[index].left, " top:", fontBounds[index].top,
    " right:", fontBounds[index].right, " bottom:", fontBounds[index].bottom);
}
```

#### getTextPath18+

getTextPath(text: string, byteLength: number, x: number, y: number): Path

获取文字的轮廓路径。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

参数名类型必填说明textstring是表示存储UTF-8 文本编码的字符。byteLengthnumber是表示要获取对应文本路径的字节长度，按传入的字节长度和实际的文本字节大小之间的最小值来获取对应的文本路径。xnumber是表示文本在绘图区域内以原点为起始位置的X坐标。ynumber是表示文本在绘图区域内以原点为起始位置的Y坐标。

**返回值：**

类型说明[Path](Class (Path).md)返回获取到的文本的路径轮廓。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types;3.Parameter verification failed.

**示例：**

```ets
import { drawing } from '@kit.ArkGraphics2D';
import { buffer } from '@kit.ArkTS';
import { RenderNode } from '@kit.ArkUI';

class DrawingRenderNode extends RenderNode {
  draw(context : DrawContext) {
    const canvas = context.canvas;
    let font = new drawing.Font();
    font.setSize(50);
    let myString: string = "Hello";
    let length: number = buffer.from(myString).length;
    let path = font.getTextPath(myString, length, 0, 100);
    canvas.drawPath(path);
  }
}
```

#### createPathForGlyph18+

createPathForGlyph(index: number): Path

获取指定字形的路径轮廓。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

参数名类型必填说明indexnumber是字形索引。

**返回值：**

类型说明[Path](Class (Path).md)返回指定字形的路径轮廓。

**示例：**

```ets
import { FrameNode, NodeController, RenderNode } from '@kit.ArkUI';
import { drawing } from '@kit.ArkGraphics2D';

class DrawingRenderNode extends RenderNode {
  draw(context : DrawContext) {
    const canvas = context.canvas;
    let font = new drawing.Font();
    font.setSize(50)
    let text: string = '你好';
    let glyphs: number[] = font.textToGlyphs(text);
    for (let index = 0; index < glyphs.length; index++) {
      let path: drawing.Path = font.createPathForGlyph(glyphs[index])
      canvas.drawPath(path)
    }
  }
}
```

#### setThemeFontFollowed15+

setThemeFontFollowed(followed: boolean): void

设置字型中的字体是否跟随主题字体。设置跟随主题字体后，若系统启用主题字体并且字型未被设置字体，字型会使用该主题字体。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

参数名类型必填说明followedboolean是字型中的字体是否跟随主题字体，true表示跟随主题字体，false表示不跟随主题字体。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types.

**示例：**

```ets
import { drawing } from '@kit.ArkGraphics2D';

let font : drawing.Font = new drawing.Font();
font.setThemeFontFollowed(true);
console.info("font is theme font followed: " + font.isThemeFontFollowed());
```

#### isThemeFontFollowed()15+

isThemeFontFollowed(): boolean

获取字型中的字体是否跟随主题字体。默认不跟随。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

类型说明boolean返回字型中的字体是否跟随主题字体的结果，true表示跟随主题字体，false表示不跟随主题字体。

**示例：**

```ets
import { drawing } from '@kit.ArkGraphics2D';

let font : drawing.Font = new drawing.Font();
font.setThemeFontFollowed(true);
console.info("font is theme font followed: " + font.isThemeFontFollowed());
```