# Class (Path)

由直线、圆弧、二阶贝塞尔、三阶贝塞尔组成的复合几何路径。

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

#### constructor12+

constructor()

构造一个路径。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**示例：**

```ets
import { drawing } from '@kit.ArkGraphics2D';

let path: drawing.Path = new drawing.Path();
```

#### constructor12+

constructor(path: Path)

构造一个已有路径的副本。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

参数名类型必填说明path[Path](Class (Path).md)是待复制的路径对象。

**示例：**

```ets
import { drawing } from '@kit.ArkGraphics2D';

let path: drawing.Path = new drawing.Path();
path.moveTo(0, 0);
path.lineTo(0, 700);
path.lineTo(700, 0);
path.close();
let path1: drawing.Path =  new drawing.Path(path);
```

#### set20+

set(src: Path): void

使用另一个路径对当前路径进行更新。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

参数名类型必填说明src[Path](Class (Path).md)是用于更新的路径。

**示例：**

```ets
import { drawing } from '@kit.ArkGraphics2D';
let path: drawing.Path = new drawing.Path();
path.moveTo(0, 0);
path.lineTo(0, 700);
path.lineTo(700, 0);
path.close();
let path1: drawing.Path = new drawing.Path();
path1.set(path);
```

#### moveTo

moveTo(x: number, y: number) : void

设置自定义路径的起始点位置。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

参数名类型必填说明xnumber是起始点的x轴坐标，该参数为浮点数。ynumber是起始点的y轴坐标，该参数为浮点数。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types.

**示例：**

```ets
import { drawing } from '@kit.ArkGraphics2D';

let path = new drawing.Path();
path.moveTo(10,10);
```

#### lineTo

lineTo(x: number, y: number) : void

添加一条从路径的最后点位置（若路径没有内容则默认为 (0, 0)）到目标点位置的线段。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

参数名类型必填说明xnumber是目标点的x轴坐标，该参数为浮点数。ynumber是目标点的y轴坐标，该参数为浮点数。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types.

**示例：**

```ets
import { drawing } from '@kit.ArkGraphics2D';

let path = new drawing.Path();
path.moveTo(10,10);
path.lineTo(10, 15);
```

#### arcTo

arcTo(x1: number, y1: number, x2: number, y2: number, startDeg: number, sweepDeg: number): void

给路径添加一段弧线，绘制弧线的方式为角度弧，该方式首先会指定一个矩形边框，取其内切椭圆，然后会指定一个起始角度和扫描度数，从起始角度扫描截取的椭圆周长一部分即为绘制的弧线。另外会默认添加一条从路径的最后点位置到弧线起始点位置的线段。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

参数名类型必填说明x1number是矩形左上角的x坐标，该参数为浮点数。y1number是矩形左上角的y坐标，该参数为浮点数。x2number是矩形右下角的x坐标，该参数为浮点数。y2number是矩形右下角的y坐标，该参数为浮点数。startDegnumber是起始的角度。角度的起始方向（0°）为x轴正方向。sweepDegnumber是扫描的度数，为正数时顺时针扫描，为负数时逆时针扫描。实际扫描的度数为该入参对360取模的结果。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types.

**示例：**

```ets
import { drawing } from '@kit.ArkGraphics2D';

let path = new drawing.Path();
path.moveTo(10,10);
path.arcTo(10, 15, 10, 10, 10, 10);
```

#### quadTo

quadTo(ctrlX: number, ctrlY: number, endX: number, endY: number): void

添加从路径最后点位置（若路径没有内容则为 (0, 0)）到目标点位置的二阶贝塞尔曲线。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

参数名类型必填说明ctrlXnumber是控制点的x坐标，该参数为浮点数。ctrlYnumber是控制点的y坐标，该参数为浮点数。endXnumber是目标点的x坐标，该参数为浮点数。endYnumber是目标点的y坐标，该参数为浮点数。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types.

**示例：**

```ets
import { drawing } from '@kit.ArkGraphics2D';

let path = new drawing.Path();
path.moveTo(10,10);
path.quadTo(10, 15, 10, 10);
```

#### conicTo12+

conicTo(ctrlX: number, ctrlY: number, endX: number, endY: number, weight: number): void

在当前路径上添加一条路径最后点位置（若路径没有内容则默认为 (0, 0)）到目标点位置的圆锥曲线，其控制点为 (ctrlX, ctrlY)，结束点为 (endX, endY)。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

参数名类型必填说明ctrlXnumber是控制点的x坐标，该参数为浮点数。ctrlYnumber是控制点的y坐标，该参数为浮点数。endXnumber是目标点的x坐标，该参数为浮点数。endYnumber是目标点的y坐标，该参数为浮点数。weightnumber是表示曲线权重，决定了曲线的形状。值越大，曲线越接近控制点。小于等于0时，效果与[lineTo](#ZH-CN_TOPIC_0000002529445943__lineto)相同；值为1时，效果与[quadTo](#ZH-CN_TOPIC_0000002529445943__quadto)相同。该参数为浮点数。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types.

**示例：**

```ets
import { drawing } from '@kit.ArkGraphics2D';

const path = new drawing.Path();
path.conicTo(200, 400, 100, 200, 0);
```

#### cubicTo

cubicTo(ctrlX1: number, ctrlY1: number, ctrlX2: number, ctrlY2: number, endX: number, endY: number): void

添加一条从路径最后点位置（若路径没有内容则默认为 (0, 0)）到目标点位置的三阶贝塞尔圆滑曲线。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

参数名类型必填说明ctrlX1number是第一个控制点的x坐标，该参数为浮点数。ctrlY1number是第一个控制点的y坐标，该参数为浮点数。ctrlX2number是第二个控制点的x坐标，该参数为浮点数。ctrlY2number是第二个控制点的y坐标，该参数为浮点数。endXnumber是目标点的x坐标，该参数为浮点数。endYnumber是目标点的y坐标，该参数为浮点数。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types.

**示例：**

```ets
import { drawing } from '@kit.ArkGraphics2D';

let path = new drawing.Path();
path.moveTo(10,10);
path.cubicTo(100, 100, 80, 150, 300, 150);
```

#### rMoveTo12+

rMoveTo(dx: number, dy: number): void

设置一个相对于当前路径终点（若路径没有内容则默认为 (0, 0)）的路径起始点位置。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

参数名类型必填说明dxnumber是路径新起始点相对于当前路径终点的x轴偏移量，正数往x轴正方向偏移，负数往x轴负方向偏移，该参数为浮点数。dynumber是路径新起始点相对于当前路径终点的y轴偏移量，正数往y轴正方向偏移，负数往y轴负方向偏移，该参数为浮点数。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types.

**示例：**

```ets
import { drawing } from '@kit.ArkGraphics2D';

const path = new drawing.Path();
path.rMoveTo(10, 10);
```

#### rLineTo12+

rLineTo(dx: number, dy: number): void

使用相对位置在当前路径上添加一条当前路径终点（若路径没有内容则默认为 (0, 0)）到目标点位置的线段。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

参数名类型必填说明dxnumber是目标点相对于当前路径终点的x轴偏移量，正数往x轴正方向偏移，负数往x轴负方向偏移，该参数为浮点数。dynumber是目标点相对于当前路径终点的y轴偏移量，正数往y轴正方向偏移，负数往y轴负方向偏移，该参数为浮点数。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types.

**示例：**

```ets
import { drawing } from '@kit.ArkGraphics2D';

const path = new drawing.Path();
path.rLineTo(400, 200);
```

#### rQuadTo12+

rQuadTo(dx1: number, dy1: number, dx2: number, dy2: number): void

使用相对位置在当前路径上添加一条当前路径终点（若路径没有内容则默认为 (0, 0)）到目标点位置的二阶贝塞尔曲线。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

参数名类型必填说明dx1number是控制点相对于路径终点的x轴偏移量，正数往x轴正方向偏移，负数往x轴负方向偏移，该参数为浮点数。dy1number是控制点相对于路径终点的y轴偏移量，正数往y轴正方向偏移，负数往y轴负方向偏移，该参数为浮点数。dx2number是目标点相对于路径终点的x轴偏移量，正数往x轴正方向偏移，负数往x轴负方向偏移，该参数为浮点数。dy2number是目标点相对于路径终点的y轴偏移量，正数往y轴正方向偏移，负数往y轴负方向偏移，该参数为浮点数。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types.

**示例：**

```ets
import { drawing } from '@kit.ArkGraphics2D';

const path = new drawing.Path();
path.rQuadTo(100, 0, 0, 200);
```

#### rConicTo12+

rConicTo(ctrlX: number, ctrlY: number, endX: number, endY: number, weight: number): void

使用相对位置在当前路径上添加一条路径终点（若路径没有内容则默认为 (0, 0)）到目标点位置的圆锥曲线。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

参数名类型必填说明ctrlXnumber是控制点相对于路径终点的x轴偏移量，正数往x轴正方向偏移，负数往x轴负方向偏移，该参数为浮点数。ctrlYnumber是控制点相对于路径终点的y轴偏移量，正数往y轴正方向偏移，负数往y轴负方向偏移，该参数为浮点数。endXnumber是目标点相对于路径终点的x轴偏移量，正数往x轴正方向偏移，负数往x轴负方向偏移，该参数为浮点数。endYnumber是目标点相对于路径终点的y轴偏移量，正数往y轴正方向偏移，负数往y轴负方向偏移，该参数为浮点数。weightnumber是表示曲线的权重，决定了曲线的形状，越大越接近控制点。若小于等于0则等同于使用[rLineTo](#ZH-CN_TOPIC_0000002529445943__rlineto12)添加一条到结束点的线段，若为1则等同于[rQuadTo](#ZH-CN_TOPIC_0000002529445943__rquadto12)，该参数为浮点数。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types.

**示例：**

```ets
import { drawing } from '@kit.ArkGraphics2D';

const path = new drawing.Path();
path.rConicTo(200, 400, 100, 200, 0);
```

#### rCubicTo12+

rCubicTo(ctrlX1: number, ctrlY1: number, ctrlX2: number, ctrlY2: number, endX: number, endY: number): void

使用相对位置在当前路径上添加一条当前路径终点（若路径没有内容则默认为 (0, 0)）到目标点位置的三阶贝塞尔曲线。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

参数名类型必填说明ctrlX1number是第一个控制点相对于路径终点的x轴偏移量，正数往x轴正方向偏移，负数往x轴负方向偏移，该参数为浮点数。ctrlY1number是第一个控制点相对于路径终点的y轴偏移量，正数往y轴正方向偏移，负数往y轴负方向偏移，该参数为浮点数。ctrlX2number是第二个控制点相对于路径终点的x轴偏移量，正数往x轴正方向偏移，负数往x轴负方向偏移，该参数为浮点数。ctrlY2number是第二个控制点相对于路径终点的y轴偏移量，正数往y轴正方向偏移，负数往y轴负方向偏移，该参数为浮点数。endXnumber是目标点相对于路径终点的x轴偏移量，正数往x轴正方向偏移，负数往x轴负方向偏移，该参数为浮点数。endYnumber是目标点相对于路径终点的y轴偏移量，正数往y轴正方向偏移，负数往y轴负方向偏移，该参数为浮点数。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types.

**示例：**

```ets
import { drawing } from '@kit.ArkGraphics2D';

const path = new drawing.Path();
path.rCubicTo(200, 0, 0, 200, -20, 0);
```

#### addArc12+

addArc(rect: common2D.Rect, startAngle: number, sweepAngle: number): void

向路径添加一段圆弧。

当startAngle和sweepAngle同时满足以下两种情况时，添加整个椭圆而不是圆弧:

1.startAngle对90取余接近于0；

2.sweepAngle不在(-360, 360)区间内。

其余情况sweepAngle会对360取余后添加圆弧。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

参数名类型必填说明rect[common2D.Rect](../../modules/ohos/@ohos.graphics.common2D (2D图形通用数据类型).md#ZH-CN_TOPIC_0000002529445937__rect)是包含弧的椭圆的矩形边界。startAnglenumber是弧的起始角度，单位为度，0度为x轴正方向，该参数为浮点数。sweepAnglenumber是扫描角度，单位为度。正数表示顺时针方向，负数表示逆时针方向，该参数为浮点数。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types.

**示例：**

```ets
import { common2D, drawing } from '@kit.ArkGraphics2D';

let path = new drawing.Path();
const rect: common2D.Rect = {left:100, top:100, right:500, bottom:500};
path.addArc(rect, 90, 180);
```

#### addCircle12+

addCircle(x: number, y: number, radius: number, pathDirection?: PathDirection): void

按指定方向，向路径添加圆形，圆的起点位于(x + radius, y)。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

参数名类型必填说明xnumber是表示圆心的x轴坐标，该参数为浮点数。ynumber是表示圆心的y轴坐标，该参数为浮点数。radiusnumber是表示圆形的半径，该参数为浮点数，小于等于0时不会有任何效果。pathDirection[PathDirection](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529285977__pathdirection12)否表示路径方向，默认为顺时针方向。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3. Parameter verification failed.

**示例：**

```ets

import { drawing } from '@kit.ArkGraphics2D';

let path = new drawing.Path();
path.addCircle(100, 200, 50, drawing.PathDirection.CLOCKWISE);
```

#### addOval12+

addOval(rect: common2D.Rect, start: number, pathDirection?: PathDirection): void

按指定方向，将矩形的内切椭圆添加到路径中。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

参数名类型必填说明rect[common2D.Rect](../../modules/ohos/@ohos.graphics.common2D (2D图形通用数据类型).md#ZH-CN_TOPIC_0000002529445937__rect)是椭圆的矩形边界。startnumber是表示椭圆初始点的索引，0，1，2，3分别对应椭圆的上端点，右端点，下端点，左端点，该参数为不小于0的整数，大于等于4时会对4取余。pathDirection[PathDirection](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529285977__pathdirection12)否表示路径方向，默认为顺时针方向。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3. Parameter verification failed.

**示例：**

```ets
import { common2D, drawing } from '@kit.ArkGraphics2D';

let path = new drawing.Path();
const rect: common2D.Rect = {left:100, top:100, right:500, bottom:500};
path.addOval(rect, 5, drawing.PathDirection.CLOCKWISE);
```

#### addRect12+

addRect(rect: common2D.Rect, pathDirection?: PathDirection): void

按指定方向，将矩形添加到路径中，添加的路径的起始点为矩形左上角。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

参数名类型必填说明rect[common2D.Rect](../../modules/ohos/@ohos.graphics.common2D (2D图形通用数据类型).md#ZH-CN_TOPIC_0000002529445937__rect)是向路径中添加的矩形轮廓。pathDirection[PathDirection](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529285977__pathdirection12)否表示路径方向，默认为顺时针方向。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3. Parameter verification failed.

**示例：**

```ets
import { common2D, drawing } from '@kit.ArkGraphics2D';

let path = new drawing.Path();
const rect: common2D.Rect = {left:100, top:100, right:500, bottom:500};
path.addRect(rect, drawing.PathDirection.CLOCKWISE);
```

#### addRoundRect12+

addRoundRect(roundRect: RoundRect, pathDirection?: PathDirection): void

按指定方向，向路径添加圆角矩形轮廓。路径添加方向为顺时针时，起始点位于圆角矩形左下方圆角与左边界的交点；路径添加方向为逆时针时，起始点位于圆角矩形左上方圆角与左边界的交点。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

参数名类型必填说明roundRect[RoundRect](Class (RoundRect).md)是圆角矩形对象。pathDirection[PathDirection](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529285977__pathdirection12)否表示路径方向，默认为顺时针方向。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3. Parameter verification failed.

**示例：**

```ets
import { common2D, drawing } from '@kit.ArkGraphics2D';

let path = new drawing.Path();
const rect: common2D.Rect = {left:100, top:100, right:500, bottom:500};
let roundRect = new drawing.RoundRect(rect, 50, 50);
path.addRoundRect(roundRect, drawing.PathDirection.CLOCKWISE);
```

#### addPath12+

addPath(path: Path, matrix?: Matrix | null): void

对源路径进行矩阵变换后，将其添加到当前路径中。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

参数名类型必填说明path[Path](Class (Path).md)是表示源路径对象。matrix[Matrix](Class (Matrix).md)|null否表示矩阵对象，默认为单位矩阵。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types.

**示例：**

```ets
import { common2D, drawing } from '@kit.ArkGraphics2D';

let path = new drawing.Path();
let matrix = new drawing.Matrix();
const rect: common2D.Rect = {left:100, top:100, right:500, bottom:500};
let roundRect = new drawing.RoundRect(rect, 50, 50);
path.addRoundRect(roundRect, drawing.PathDirection.CLOCKWISE);
let dstPath = new drawing.Path();
dstPath.addPath(path, matrix);
```

#### transform12+

transform(matrix: Matrix): void

对路径进行矩阵变换。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

参数名类型必填说明matrix[Matrix](Class (Matrix).md)是表示矩阵对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types.

**示例：**

```ets
import { common2D, drawing } from '@kit.ArkGraphics2D';

let path = new drawing.Path();
let matrix = new drawing.Matrix();
matrix.setScale(1.5, 1.5, 10, 10);
const rect: common2D.Rect = {left:100, top:100, right:500, bottom:500};
let roundRect = new drawing.RoundRect(rect, 50, 50);
path.addRoundRect(roundRect, drawing.PathDirection.CLOCKWISE);
path.transform(matrix);
```

#### contains12+

contains(x: number, y: number): boolean

判断指定坐标点是否被路径包含，判定是否被路径包含的规则参考[PathFillType](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529285977__pathfilltype12)。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

参数名类型必填说明xnumber是x轴上坐标点，该参数必须为浮点数。ynumber是y轴上坐标点，该参数必须为浮点数。

**返回值：**

类型说明boolean返回指定坐标点是否在路径内。true表示点在路径内，false表示点不在路径内。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types.

**示例：**

```ets
import { common2D, drawing } from '@kit.ArkGraphics2D';

const path = new drawing.Path();
let rect : common2D.Rect = {left: 50, top: 50, right: 250, bottom: 250};
path.addRect(rect, drawing.PathDirection.CLOCKWISE);
console.info("test contains: " + path.contains(0, 0));
console.info("test contains: " + path.contains(60, 60));
```

#### setLastPoint20+

setLastPoint(x: number, y: number): void

修改路径的最后一个点。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

参数名类型必填说明xnumber是指定点的x轴坐标，该参数为浮点数。0表示坐标原点，负数表示位于坐标原点左侧，正数表示位于坐标原点右侧。ynumber是指定点的y轴坐标，该参数为浮点数。0表示坐标原点，负数表示位于坐标原点上侧，正数表示位于坐标原点下侧。

**示例：**

```ets
import { drawing } from '@kit.ArkGraphics2D';
const path = new drawing.Path();
path.moveTo(0, 0);
path.lineTo(0, 700);
let isEmpty = path.isEmpty();
console.info('isEmpty:', isEmpty);
path.reset();
isEmpty = path.isEmpty();
console.info('isEmpty:', isEmpty);
path.setLastPoint(50, 50);
isEmpty = path.isEmpty();
console.info('isEmpty:', isEmpty);
```

#### setFillType12+

setFillType(pathFillType: PathFillType): void

设置路径的填充类型，决定路径内部区域的定义方式。例如，使用Winding填充类型时，路径内部区域由路径环绕的次数决定，而使用EvenOdd填充类型时，路径内部区域由路径环绕的次数是否为奇数决定。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

参数名类型必填说明pathFillType[PathFillType](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529285977__pathfilltype12)是表示路径填充规则。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3. Parameter verification failed.

**示例：**

```ets
import { drawing } from '@kit.ArkGraphics2D';

const path = new drawing.Path();
path.setFillType(drawing.PathFillType.WINDING);
```

#### getFillType20+

getFillType(): PathFillType

获取路径的填充类型。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

类型说明[PathFillType](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529285977__pathfilltype12)路径填充类型。

**示例：**

```ets
import { drawing } from '@kit.ArkGraphics2D';
const path = new drawing.Path();
path.setFillType(drawing.PathFillType.WINDING);
let type = path.getFillType();
console.info("type :" + type);
```

#### getBounds12+

getBounds(): common2D.Rect

获取包含路径的最小矩形边界。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

类型说明[common2D.Rect](../../modules/ohos/@ohos.graphics.common2D (2D图形通用数据类型).md#ZH-CN_TOPIC_0000002529445937__rect)包含路径的最小矩形区域。

**示例：**

```ets
import { common2D, drawing } from '@kit.ArkGraphics2D';

const path = new drawing.Path();
path.lineTo(50, 40)
let rect : common2D.Rect = {left: 0, top: 0, right: 0, bottom: 0};
rect = path.getBounds();
console.info("test rect.left: " + rect.left);
console.info("test rect.top: " + rect.top);
console.info("test rect.right: " + rect.right);
console.info("test rect.bottom: " + rect.bottom);
```

#### addPolygon12+

addPolygon(points: Array<common2D.Point>, close: boolean): void

通过坐标点列表添加多条连续的线段。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

参数名类型必填说明pointsArray<[common2D.Point](../../modules/ohos/@ohos.graphics.common2D (2D图形通用数据类型).md#ZH-CN_TOPIC_0000002529445937__point12)>是坐标点数组。closeboolean是表示是否将路径闭合，即是否添加路径起始点到终点的连线。true表示将路径闭合，false表示不将路径闭合。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types.

**示例：**

```ets
import { common2D, drawing } from '@kit.ArkGraphics2D';

let pointsArray = new Array<common2D.Point>();
const point1: common2D.Point = { x: 200, y: 200 };
const point2: common2D.Point = { x: 400, y: 200 };
const point3: common2D.Point = { x: 100, y: 400 };
const point4: common2D.Point = { x: 300, y: 400 };
pointsArray.push(point1);
pointsArray.push(point2);
pointsArray.push(point3);
pointsArray.push(point4);
const path = new drawing.Path();
path.addPolygon(pointsArray, false);
```

#### offset12+

offset(dx: number, dy: number): Path

将路径沿着x轴和y轴方向偏移一定距离并保存在返回的路径对象中。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

参数名类型必填说明dxnumber是x轴方向偏移量，正数往x轴正方向偏移，负数往x轴负方向偏移，该参数为浮点数。dynumber是y轴方向偏移量，正数往y轴正方向偏移，负数往y轴负方向偏移，该参数为浮点数。

**返回值：**

类型说明[Path](Class (Path).md)返回当前路径偏移(dx,dy)后生成的新路径对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types.

**示例：**

```ets
import { drawing } from '@kit.ArkGraphics2D';

const path = new drawing.Path();
path.moveTo(200, 200);
path.lineTo(300, 300);
const dst = path.offset(200, 200);
```

#### op12+

op(path: Path, pathOp: PathOp): boolean

将当前路径置为和path按照指定的路径操作类型合并后的结果。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

参数名类型必填说明path[Path](Class (Path).md)是路径对象，用于与当前路径合并。pathOp[PathOp](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529285977__pathop12)是路径操作类型枚举。

**返回值：**

类型说明boolean返回路径合并是否成功的结果。true表示合并成功，false表示合并失败。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types;3.Parameter verification failed.

**示例：**

```ets
import { drawing } from '@kit.ArkGraphics2D';

const path = new drawing.Path();
const path2 = new drawing.Path();
path.addCircle(100, 200, 100, drawing.PathDirection.CLOCKWISE);
console.info("get pathOp: ", path2.op(path, drawing.PathOp.DIFFERENCE));
```

#### close

close(): void

闭合路径，会添加一条从路径起点位置到最后点位置的线段。

**系统能力：** SystemCapability.Graphics.Drawing

**示例：**

```ets
import { drawing } from '@kit.ArkGraphics2D';

let path = new drawing.Path();
path.moveTo(10,10);
path.cubicTo(10, 10, 10, 10, 15, 15);
path.close();
```

#### reset

reset(): void

重置自定义路径数据。

**系统能力：** SystemCapability.Graphics.Drawing

**示例：**

```ets
import { drawing } from '@kit.ArkGraphics2D';

let path = new drawing.Path();
path.moveTo(10,10);
path.cubicTo(10, 10, 10, 10, 15, 15);
path.reset();
```

#### rewind20+

rewind(): void

将路径内添加的各类点/线清空，但是保留内存空间。

**系统能力：** SystemCapability.Graphics.Drawing

**示例：**

```ets
import { drawing } from '@kit.ArkGraphics2D';
let path = new drawing.Path();
path.moveTo(10,10);
path.lineTo(20,20);
path.rewind();
let empty = path.isEmpty();
console.info('empty : ', empty);
```

#### isEmpty20+

isEmpty(): boolean

判断路径是否为空。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

类型说明boolean路径是否为空。true表示当前路径为空，false表示路径不为空。

**示例：**

```ets
import { drawing } from '@kit.ArkGraphics2D';
let path = new drawing.Path();
path.moveTo(10,10);
path.lineTo(20,20);
let isEmpty = path.isEmpty();
console.info('isEmpty:', isEmpty);
```

#### isRect20+

isRect(rect: common2D.Rect | null): boolean

判断路径是否构成矩形。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

参数名类型必填说明rect[common2D.Rect](../../modules/ohos/@ohos.graphics.common2D (2D图形通用数据类型).md#ZH-CN_TOPIC_0000002529445937__rect)| null是矩形对象，作为出参使用，路径构成矩形时，会被改写为路径表示的矩形，否则不会改变。可以为null，表示无需获取路径表示的矩形。

**返回值：**

类型说明boolean返回路径是否构成矩形。true表示路径构成矩形，false表示路径不构成矩形。

**示例：**

```ets
import { common2D, drawing } from '@kit.ArkGraphics2D';

let path = new drawing.Path();
path.moveTo(10,10);
path.lineTo(20,10);
let isRect = path.isRect(null);
console.info("isRect: ", isRect);
let rect: common2D.Rect = { left : 100, top : 100, right : 400, bottom : 500 };
path.lineTo(20, 20);
path.lineTo(10, 20);
path.lineTo(10, 10);
isRect = path.isRect(rect);
console.info('isRect: ', isRect);
```

#### getLength12+

getLength(forceClosed: boolean): number

获取路径长度。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

参数名类型必填说明forceClosedboolean是表示是否按照闭合路径测量，true表示测量时路径会被强制视为已闭合，false表示会根据路径的实际闭合状态测量。

**返回值：**

类型说明number路径长度。

**示例：**

```ets
import { drawing } from '@kit.ArkGraphics2D';

let path = new drawing.Path();
path.arcTo(20, 20, 180, 180, 180, 90);
let len = path.getLength(false);
console.info("path length = " + len);
```

#### getPositionAndTangent12+

getPositionAndTangent(forceClosed: boolean, distance: number, position: common2D.Point, tangent: common2D.Point): boolean

获取路径起始点指定距离处的坐标点和切线值。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

参数名类型必填说明forceClosedboolean是表示是否按照闭合路径测量，true表示测量时路径会被强制视为已闭合，false表示会根据路径的实际闭合状态测量。distancenumber是表示与路径起始点的距离，小于0时会被视作0，大于路径长度时会被视作路径长度。该参数为浮点数。position[common2D.Point](../../modules/ohos/@ohos.graphics.common2D (2D图形通用数据类型).md#ZH-CN_TOPIC_0000002529445937__point12)是存储获取到的距离路径起始点distance处的点的坐标。tangent[common2D.Point](../../modules/ohos/@ohos.graphics.common2D (2D图形通用数据类型).md#ZH-CN_TOPIC_0000002529445937__point12)是存储获取到的距离路径起始点distance处的点的切线值，tangent.x表示该点切线的余弦值，tangent.y表示该点切线的正弦值。

**返回值：**

类型说明boolean表示是否成功获取距离路径起始点distance处的点的坐标和正切值的结果。true表示获取成功，false表示获取失败，position和tangent不会被改变。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types.

**示例：**

```ets
import { common2D, drawing } from '@kit.ArkGraphics2D';

let path: drawing.Path = new drawing.Path();
path.moveTo(0, 0);
path.lineTo(0, 700);
path.lineTo(700, 0);
let position: common2D.Point = { x: 0.0, y: 0.0 };
let tangent: common2D.Point = { x: 0.0, y: 0.0 };
if (path.getPositionAndTangent(false, 0.1, position, tangent)) {
  console.info("getPositionAndTangent-----position:  "+ position.x);
  console.info("getPositionAndTangent-----position:  "+ position.y);
  console.info("getPositionAndTangent-----tangent:  "+ tangent.x);
  console.info("getPositionAndTangent-----tangent:  "+ tangent.y);
}
```

#### getSegment18+

getSegment(forceClosed: boolean, start: number, stop: number, startWithMoveTo: boolean, dst: Path): boolean

截取路径的片段并追加到目标路径上。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

参数名类型必填说明forceClosedboolean是表示是否按照闭合路径测量，true表示测量时路径会被强制视为已闭合，false表示会根据路径的实际闭合状态测量。startnumber是表示与路径起始点的距离，距离路径起始点start距离的位置即为截取路径片段的起始点，小于0时会被视作0，大于等于stop时会截取失败。该参数为浮点数。stopnumber是表示与路径起始点的距离，距离路径起始点stop距离的位置即为截取路径片段的终点，小于等于start时会截取失败，大于路径长度时会被视作路径长度。该参数为浮点数。startWithMoveToboolean是表示是否在目标路径执行[moveTo](#ZH-CN_TOPIC_0000002529445943__moveto)移动到截取路径片段的起始点位置。true表示执行，false表示不执行。dst[Path](Class (Path).md)是目标路径，截取成功时会将得到的路径片段追加到目标路径上，截取失败时不做改变。

**返回值：**

类型说明boolean表示是否成功截取路径片段。true表示截取成功，false表示截取失败。

**示例：**

```ets
import { drawing } from '@kit.ArkGraphics2D';

let path: drawing.Path = new drawing.Path();
path.moveTo(0, 0);
path.lineTo(0, 700);
path.lineTo(700, 0);
let dstPath: drawing.Path = new drawing.Path();
console.info("getSegment-----result:  "+ path.getSegment(true, 10.0, 20.0, true, dstPath));
```

#### isClosed12+

isClosed(): boolean

获取路径是否闭合。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

类型说明boolean表示当前路径是否闭合，true表示闭合，false表示不闭合。

**示例：**

```ets
import { drawing } from '@kit.ArkGraphics2D';

let path: drawing.Path = new drawing.Path();
path.moveTo(0, 0);
path.lineTo(0, 700);
if (path.isClosed()) {
  console.info("path is closed.");
} else {
  console.info("path is not closed.");
}
```

#### getMatrix12+

getMatrix(forceClosed: boolean, distance: number, matrix: Matrix, flags: PathMeasureMatrixFlags): boolean

在路径上的某个位置，获取一个变换矩阵，用于表示该点的坐标和朝向。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

参数名类型必填说明forceClosedboolean是表示是否按照闭合路径测量，true表示测量时路径会被强制视为已闭合，false表示会根据路径的实际闭合状态测量。distancenumber是表示与路径起始点的距离，小于0时会被视作0，大于路径长度时会被视作路径长度。该参数为浮点数。matrix[Matrix](Class (Matrix).md)是矩阵对象，用于存储得到的矩阵。flags[PathMeasureMatrixFlags](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529285977__pathmeasurematrixflags12)是矩阵信息维度枚举。

**返回值：**

类型说明boolean返回是否成功获取变换矩阵的结果。true表示成功，false表示失败。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: Mandatory parameters are left unspecified.

**示例：**

```ets
import { drawing } from '@kit.ArkGraphics2D';

let path: drawing.Path = new drawing.Path();
let matrix = new drawing.Matrix();
if(path.getMatrix(false, 10, matrix, drawing.PathMeasureMatrixFlags.GET_TANGENT_MATRIX)) {
  console.info("path.getMatrix return true");
} else {
  console.info("path.getMatrix return false");
}
```

#### buildFromSvgString12+

buildFromSvgString(str: string): boolean

解析SVG字符串表示的路径。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

参数名类型必填说明strstring是SVG格式的字符串，用于描述绘制路径。

**返回值：**

类型说明boolean返回是否成功解析SVG字符串的结果。true表示解析成功，false表示解析失败。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: Mandatory parameters are left unspecified.

**示例：**

```ets
import { drawing } from '@kit.ArkGraphics2D';

let path: drawing.Path = new drawing.Path();
let svgStr: string =  "M150 100 L75 300 L225 300 Z";
if(path.buildFromSvgString(svgStr)) {
  console.info("buildFromSvgString return true");
} else {
  console.info("buildFromSvgString return false");
}
```

#### getPathIterator18+

getPathIterator(): PathIterator

返回该路径的操作迭代器。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

类型说明[PathIterator](Class (PathIterator).md)该路径的迭代器对象。

**示例：**

```ets
import { drawing } from '@kit.ArkGraphics2D';

let path: drawing.Path = new drawing.Path();
let iter = path.getPathIterator();
```

#### approximate20+

approximate(acceptableError: number): Array<number>

将当前路径转化为由连续直线段构成的近似路径。

- 当acceptableError为0时，曲线路径被极度细分，会严重影响性能和内存消耗，不建议设置误差值为0。
- 当acceptableError特别大时，路径会极度简化，保留少量关键点，可能会丢失原有形状。
- 对于椭圆等曲线，当acceptableError过大时，拟合结果通常只包含椭圆的分段贝塞尔曲线的起止点，椭圆形会被极度简化为多边形。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

参数名类型必填说明acceptableErrornumber是表示路径上每条线段的可接受误差。该参数为浮点数，不应小于0，当参数小于0时报错。

**返回值：**

类型说明Array<number>

返回包含近似路径的点的数组，至少包含两个点。每个点由三个值组成：

1. 该点所在的位置距离路径起点的长度比例值，范围为[0.0, 1.0]。

2. 点的x坐标。

3. 点的y坐标。

**错误码：**

以下错误码的详细介绍请参见[图形绘制与显示错误码](../../errors/图形绘制与显示错误码.md)。

错误码ID错误信息25900001Parameter error.Possible causes: Incorrect parameter range.

**示例：**

```ets
import { drawing } from '@kit.ArkGraphics2D';

let path: drawing.Path = new drawing.Path();
path.moveTo(100, 100);
path.lineTo(500, 500);
let points: number[] = path.approximate(0.5);
for (let i = 0; i < points.length; i += 3) {
  console.info("PathApproximate Fraction =" + points[i] + ", X =" + points[i + 1] + ", Y =" + points[i + 2] + "\n");
}
```

#### interpolate20+

interpolate(other: Path, weight: number, interpolatedPath: Path): boolean

根据给定的权重，在当前路径和另一条路径之间进行插值，并将结果存储在目标路径对象中。两条路径点数相同即可插值成功，目标路径按照当前路径的结构进行创建。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

参数名类型必填说明other[Path](Class (Path).md)是表示另一条路径对象。weightnumber是表示插值权重，必须在[0.0, 1.0]范围内。该参数为浮点数。interpolatedPath[Path](Class (Path).md)是表示用于存储插值结果的目标路径对象。

**返回值：**

类型说明boolean返回插值操作是否成功的结果。true表示插值成功，false表示插值失败。

**错误码：**

以下错误码的详细介绍请参见[图形绘制与显示错误码](../../errors/图形绘制与显示错误码.md)。

错误码ID错误信息25900001Parameter error.Possible causes: Incorrect parameter range.

**示例：**

```ets
import { drawing } from '@kit.ArkGraphics2D';

let path: drawing.Path = new drawing.Path();
path.moveTo(50, 50);
path.lineTo(100, 100);
path.lineTo(200, 200);
let other: drawing.Path = new drawing.Path();
other.moveTo(80, 80);
other.lineTo(300, 300);
let interpolatedPath: drawing.Path = new drawing.Path();
if (path.interpolate(other, 0.0, interpolatedPath)) {
  console.info('interpolate return true');
} else {
  console.info('interpolate return false');
}
```

#### isInterpolate20+

isInterpolate(other: Path): boolean

判断当前路径与另一条路径在结构和操作顺序上是否完全一致，以确定两条路径是否兼容插值。若路径中包含圆锥曲线（Conic）操作，则对应操作的权重值也必须一致，才能视为兼容插值。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

参数名类型必填说明other[Path](Class (Path).md)是表示另一条路径对象。

**返回值：**

类型说明boolean返回当前路径与另一条路径是否兼容插值的结果。true表示兼容插值，false表示不兼容插值。

**示例：**

```ets
import { drawing } from '@kit.ArkGraphics2D';

let path: drawing.Path = new drawing.Path();
path.moveTo(0, 0);
path.lineTo(100, 100);
let other: drawing.Path = new drawing.Path();
other.moveTo(0, 1);
other.lineTo(200, 200);
if (path.isInterpolate(other)) {
  console.info('isInterpolate return true');
} else {
  console.info('isInterpolate return false');
}
```