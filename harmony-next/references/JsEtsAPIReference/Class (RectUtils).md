# Class (RectUtils)

提供了处理矩形的工具。

主要的使用场景：

1.

矩形快速构建与获取基本属性，如构造新矩形、拷贝矩形、获取矩形的宽高以及中心点等。

1.

边界计算与调整，如获取包含关系、计算与更新矩形之间交集和并集，更新边界值等。

-

本模块首批接口从API version 11开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

-

本Class首批接口从API version 20开始支持。

-

本模块使用屏幕物理像素单位px。

-

本模块为单线程模型策略，需要调用方自行管理线程安全和上下文状态的切换。

#### 导入模块

```ets
import { drawing } from '@kit.ArkGraphics2D';
```

#### makeEmpty20+

static makeEmpty(): common2D.Rect

创建一个上下左右边界坐标都是0的矩形。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

类型说明[common2D.Rect](@ohos.graphics.common2D (2D图形通用数据类型).md#ZH-CN_TOPIC_0000002529445937__rect)创建的矩形对象。

**示例：**

```ets
import { drawing, common2D } from '@kit.ArkGraphics2D';

let rect = drawing.RectUtils.makeEmpty();
```

#### makeLtrb20+

static makeLtrb(left: number, top: number, right: number, bottom: number): common2D.Rect

创建指定上下左右边界的矩形。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

参数名类型必填说明leftnumber是矩形的左上角x轴坐标，该参数为浮点数。0表示坐标原点，负数表示位于坐标原点左侧，正数表示位于坐标原点右侧。topnumber是矩形的左上角y轴坐标，该参数为浮点数。0表示坐标原点，负数表示位于坐标原点上侧，正数表示位于坐标原点下侧。rightnumber是矩形的右下角x轴坐标，该参数为浮点数。0表示坐标原点，负数表示位于坐标原点左侧，正数表示位于坐标原点右侧。bottomnumber是矩形的右下角y轴坐标，该参数为浮点数。0表示坐标原点，负数表示位于坐标原点上侧，正数表示位于坐标原点下侧。

**返回值：**

类型说明[common2D.Rect](@ohos.graphics.common2D (2D图形通用数据类型).md#ZH-CN_TOPIC_0000002529445937__rect)创建的矩形。

**示例：**

```ets
import { drawing, common2D } from '@kit.ArkGraphics2D';

let rect = drawing.RectUtils.makeLtrb(10, 10, 20, 20);
```

#### makeCopy20+

static makeCopy(src: common2D.Rect): common2D.Rect

拷贝一个矩形。

**系统能力**：SystemCapability.Graphics.Drawing

**参数：**

参数名类型必填说明src[common2D.Rect](@ohos.graphics.common2D (2D图形通用数据类型).md#ZH-CN_TOPIC_0000002529445937__rect)是用于拷贝的矩形。

**返回值：**

类型说明[common2D.Rect](@ohos.graphics.common2D (2D图形通用数据类型).md#ZH-CN_TOPIC_0000002529445937__rect)创建的新矩形。

**示例：**

```ets
import { drawing, common2D } from '@kit.ArkGraphics2D';
let rect = drawing.RectUtils.makeLtrb(10, 10, 20, 20);
let rect2 = drawing.RectUtils.makeCopy(rect);
console.info('rect2.left:', rect2.left);
console.info('rect2.top: ', rect2.top);
console.info('rect2.right: ', rect2.right);
console.info('rect2.bottom: ', rect2.bottom);
```

#### getWidth20+

static getWidth(rect: common2D.Rect): number

获取矩形的宽度。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

参数名类型必填说明rect[common2D.Rect](@ohos.graphics.common2D (2D图形通用数据类型).md#ZH-CN_TOPIC_0000002529445937__rect)是矩形对象。

**返回值：**

类型说明number返回矩形的宽。如果矩形的左边界大于右边界，获取的宽度为负值，左边界小于右边界则为正值。

**示例：**

```ets
import { drawing, common2D } from '@kit.ArkGraphics2D';
let rect = drawing.RectUtils.makeLtrb(10, 10, 20, 20);
let width = drawing.RectUtils.getWidth(rect);
console.info('width:', width);
```

#### getHeight20+

static getHeight(rect: common2D.Rect): number

获取矩形的高度。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

参数名类型必填说明rect[common2D.Rect](@ohos.graphics.common2D (2D图形通用数据类型).md#ZH-CN_TOPIC_0000002529445937__rect)是矩形对象。

**返回值：**

类型说明number返回矩形的高。如果矩形的上边界大于下边界，获取的高度为负值，上边界小于下边界则为正值。

**示例：**

```ets
import { drawing, common2D } from '@kit.ArkGraphics2D';
let rect = drawing.RectUtils.makeLtrb(10, 10, 20, 20);
let height = drawing.RectUtils.getHeight(rect);
```

#### centerX20+

static centerX(rect: common2D.Rect): number

获取矩形中心的横坐标。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

参数名类型必填说明rect[common2D.Rect](@ohos.graphics.common2D (2D图形通用数据类型).md#ZH-CN_TOPIC_0000002529445937__rect)是矩形对象。

**返回值：**

类型说明number返回矩形中心的横坐标。

**示例：**

```ets
import { drawing, common2D } from '@kit.ArkGraphics2D';
let rect = drawing.RectUtils.makeLtrb(20, 30, 30, 40);
let x = drawing.RectUtils.centerX(rect);
```

#### centerY20+

static centerY(rect: common2D.Rect): number

获取矩形中心的纵坐标。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

参数名类型必填说明rect[common2D.Rect](@ohos.graphics.common2D (2D图形通用数据类型).md#ZH-CN_TOPIC_0000002529445937__rect)是矩形对象。

**返回值：**

类型说明number返回矩形中心的纵坐标。

**示例：**

```ets
import { drawing, common2D } from '@kit.ArkGraphics2D';
let rect = drawing.RectUtils.makeLtrb(20, 30, 30, 40);
let x = drawing.RectUtils.centerY(rect);
```

#### contains20+

static contains(rect: common2D.Rect, other: common2D.Rect): boolean

判断一个矩形是否完全包含另外一个矩形。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

参数名类型必填说明rect[common2D.Rect](@ohos.graphics.common2D (2D图形通用数据类型).md#ZH-CN_TOPIC_0000002529445937__rect)是矩形对象。other[common2D.Rect](@ohos.graphics.common2D (2D图形通用数据类型).md#ZH-CN_TOPIC_0000002529445937__rect)是判断是否被包含的矩形对象。

**返回值：**

类型说明boolean返回矩形是否完全包含另一个矩形的结果。true表示指定矩形在另一个矩形内部或者相等，false表示指定矩形在另一个矩形外部。空的矩形不包含任何矩形。

**示例：**

```ets
import { drawing, common2D } from '@kit.ArkGraphics2D';
let rect = drawing.RectUtils.makeLtrb(10, 10, 20, 20);
let rect2 = drawing.RectUtils.makeLtrb(0, 0, 40, 40);
let isContains = drawing.RectUtils.contains(rect2, rect);
console.info('isContains: ', isContains);
```

#### contains20+

static contains(rect: common2D.Rect, left: number, top: number, right: number, bottom: number): boolean

判断一个矩形是否完全包含另外一个矩形（另一个矩形分别用左上右下坐标表示）。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

参数名类型必填说明rect[common2D.Rect](@ohos.graphics.common2D (2D图形通用数据类型).md#ZH-CN_TOPIC_0000002529445937__rect)是矩形对象。leftnumber是矩形的左上角x轴坐标，该参数为浮点数。0表示坐标原点，负数表示位于坐标原点左侧，正数表示位于坐标原点右侧。topnumber是矩形的左上角y轴坐标，该参数为浮点数。0表示坐标原点，负数表示位于坐标原点上侧，正数表示位于坐标原点下侧。rightnumber是矩形的右下角x轴坐标，该参数为浮点数。0表示坐标原点，负数表示位于坐标原点左侧，正数表示位于坐标原点右侧。bottomnumber是矩形的右下角y轴坐标，该参数为浮点数。0表示坐标原点，负数表示位于坐标原点上侧，正数表示位于坐标原点下侧。

**返回值：**

类型说明boolean返回矩形是否完全包含由左上右下坐标组成的矩形的结果。true表示指定左上右下坐标组成的矩形在矩形的内部或者相等，false表示指定左上右下坐标组成的矩形在矩形的外部。空的矩形不包含任何矩形。

**示例：**

```ets
import { drawing, common2D } from '@kit.ArkGraphics2D';
let rect = drawing.RectUtils.makeLtrb(0, 0, 100, 100);
let isContains = drawing.RectUtils.contains(rect, 10, 20, 30, 40);
console.info('isContains :', isContains);
```

#### contains20+

static contains(rect: common2D.Rect, x: number, y: number): boolean

判断一个矩形是否完全包含一个点。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

参数名类型必填说明rect[common2D.Rect](@ohos.graphics.common2D (2D图形通用数据类型).md#ZH-CN_TOPIC_0000002529445937__rect)是矩形对象。xnumber是要判断点的x轴坐标，该参数为浮点数。0表示坐标原点，负数表示位于坐标原点左侧，正数表示位于坐标原点右侧。ynumber是要判断点的y轴坐标，该参数为浮点数。0表示坐标原点，负数表示位于坐标原点上侧，正数表示位于坐标原点下侧。

**返回值：**

类型说明boolean返回矩形是否完全包含x、y组成的点的结果。true表示矩形完全包含x、y组成的点，false表示矩形不完全包含x、y组成的点。左边界和上边界属于矩形内部，右边界和下边界不属于矩形内部。空的矩形不包含任何点。

**示例：**

```ets
import { drawing, common2D } from '@kit.ArkGraphics2D';
let rect = drawing.RectUtils.makeLtrb(0, 0, 100, 100);
let isContains = drawing.RectUtils.contains(rect, 10, 20);
console.info('isContains: ', isContains);
```

#### inset20+

static inset(rect: common2D.Rect, left: number, top: number, right: number, bottom: number): void

将指定矩形的左边界、上边界、右边界和下边界分别和传入的"左上右下"的值相加。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

参数名类型必填说明rect[common2D.Rect](@ohos.graphics.common2D (2D图形通用数据类型).md#ZH-CN_TOPIC_0000002529445937__rect)是矩形对象。leftnumber是添加到矩形左边界的值（矩形左上角横坐标），该参数为浮点数。0表示不进行任何运算，正数表示进行相加运算，负数表示相减运算。topnumber是添加到矩形上边界的值（矩形左上角纵坐标），该参数为浮点数。0表示不进行任何运算，正数表示进行相加运算，负数表示相减运算。rightnumber是添加到矩形右边界的值（矩形右下角横坐标），该参数为浮点数。0表示不进行任何运算，正数表示进行相加运算，负数表示相减运算。bottomnumber是添加到矩形下边界的值（矩形右下角纵坐标），该参数为浮点数。0表示不进行任何运算，正数表示进行相加运算，负数表示相减运算。

**示例：**

```ets
import { drawing, common2D } from '@kit.ArkGraphics2D';
let rect = drawing.RectUtils.makeLtrb(10, 10, 20, 20);
drawing.RectUtils.inset(rect, 10, -20, 30, 60);
console.info('rect.left:', rect.left);
console.info('rect.top: ', rect.top);
console.info('rect.right: ', rect.right);
console.info('rect.bottom: ', rect.bottom);
```

#### intersect20+

static intersect(rect: common2D.Rect, other: common2D.Rect): boolean

计算两个矩形的交集区域，并将交集结果更新到第一个入参代表的矩形区域。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

参数名类型必填说明rect[common2D.Rect](@ohos.graphics.common2D (2D图形通用数据类型).md#ZH-CN_TOPIC_0000002529445937__rect)是用于计算交集的原矩形。other[common2D.Rect](@ohos.graphics.common2D (2D图形通用数据类型).md#ZH-CN_TOPIC_0000002529445937__rect)是用于计算交集的另一个矩形。

**返回值：**

类型说明boolean返回两个矩形是否有交集的结果。true表示两个矩形有交集，false表示两个矩形没有交集。

**示例：**

```ets
import { drawing, common2D } from '@kit.ArkGraphics2D';
let rect = drawing.RectUtils.makeLtrb(0, 0, 20, 20);
let rect2 = drawing.RectUtils.makeLtrb(10, 10, 40, 40);
let isIntersect = drawing.RectUtils.intersect(rect, rect2);
console.info('isIntersect :', isIntersect);
console.info('rect.left:', rect.left);
console.info('rect.top: ', rect.top);
console.info('rect.right: ', rect.right);
console.info('rect.bottom: ', rect.bottom);
```

#### isIntersect20+

static isIntersect(rect: common2D.Rect, other: common2D.Rect): boolean

判断两个矩形是否相交。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

参数名类型必填说明rect[common2D.Rect](@ohos.graphics.common2D (2D图形通用数据类型).md#ZH-CN_TOPIC_0000002529445937__rect)是用于计算交集的原矩形。other[common2D.Rect](@ohos.graphics.common2D (2D图形通用数据类型).md#ZH-CN_TOPIC_0000002529445937__rect)是用于计算交集的另一个矩形。

**返回值：**

类型说明boolean返回两个矩形是否有交集的结果。true表示指定矩形与原矩形相交，false表示指定矩形和原矩形没有交集。两矩形仅边重叠或点相交返回false。

**示例：**

```ets
import { drawing, common2D } from '@kit.ArkGraphics2D';
let rect = drawing.RectUtils.makeLtrb(0, 0, 20, 20);
let rect2 = drawing.RectUtils.makeLtrb(10, 10, 40, 40);
let isIntersect = drawing.RectUtils.isIntersect(rect, rect2);
console.info('isIntersect :', isIntersect);
```

#### union20+

static union(rect: common2D.Rect, other: common2D.Rect): void

计算矩形的并集区域，并将并集结果更新到第一个入参表示的矩形区域。如果第一个入参矩形为空，则将并集结果更新到第二个入参代表的矩形区域；如果第二个入参的矩形为空，则不进行任何操作。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

参数名类型必填说明rect[common2D.Rect](@ohos.graphics.common2D (2D图形通用数据类型).md#ZH-CN_TOPIC_0000002529445937__rect)是用于计算并集的原矩形。other[common2D.Rect](@ohos.graphics.common2D (2D图形通用数据类型).md#ZH-CN_TOPIC_0000002529445937__rect)是用于计算并集的另一个矩形。

**示例：**

```ets
import { drawing, common2D } from '@kit.ArkGraphics2D';
let rect = drawing.RectUtils.makeLtrb(0, 0, 20, 20);
let rect2 = drawing.RectUtils.makeLtrb(10, 10, 40, 40);
drawing.RectUtils.union(rect, rect2);
console.info('rect.left:', rect.left);
console.info('rect.top: ', rect.top);
console.info('rect.right: ', rect.right);
console.info('rect.bottom: ', rect.bottom);
```

#### isEmpty20+

static isEmpty(rect: common2D.Rect): boolean

判断矩形是否为空（左边界大于等于右边界或者上边界大于等于下边界）。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

参数名类型必填说明rect[common2D.Rect](@ohos.graphics.common2D (2D图形通用数据类型).md#ZH-CN_TOPIC_0000002529445937__rect)是用于判断的矩形对象。

**返回值：**

类型说明boolean返回矩形是否为空的结果。true表示矩形是空，false表示矩形不为空。

**示例：**

```ets
import { drawing, common2D } from '@kit.ArkGraphics2D';
let rect = drawing.RectUtils.makeEmpty();
let isEmpty = drawing.RectUtils.isEmpty(rect);
console.info('isEmpty :', isEmpty);
let rect2 = drawing.RectUtils.makeLtrb(0, 0, 20, 20);
isEmpty = drawing.RectUtils.isEmpty(rect2);
console.info('isEmpty :', isEmpty);
```

#### offset20+

static offset(rect: common2D.Rect, dx: number, dy: number): void

对矩形进行平移。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

参数名类型必填说明rect[common2D.Rect](@ohos.graphics.common2D (2D图形通用数据类型).md#ZH-CN_TOPIC_0000002529445937__rect)是发生偏移的矩形区域。dxnumber是水平方向平移的距离，该参数为浮点数。0表示不平移，负数表示向左平移，正数表示向右平移。dynumber是竖直方向平移的距离，该参数为浮点数。0表示不平移，负数表示向上平移，正数表示向下平移。

**示例：**

```ets
import { drawing, common2D } from '@kit.ArkGraphics2D';
let rect = drawing.RectUtils.makeLtrb(0, 0, 20, 20);
drawing.RectUtils.offset(rect, 10, 20);
console.info('rect.left:', rect.left);
console.info('rect.top: ', rect.top);
console.info('rect.right: ', rect.right);
console.info('rect.bottom: ', rect.bottom);
```

#### offsetTo20+

static offsetTo(rect: common2D.Rect, newLeft: number, newTop: number): void

将矩形平移到指定位置。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

参数名类型必填说明rect[common2D.Rect](@ohos.graphics.common2D (2D图形通用数据类型).md#ZH-CN_TOPIC_0000002529445937__rect)是发生偏移的矩形区域。newLeftnumber是要平移到的对应位置的x轴坐标，浮点数。0表示坐标原点，负数位于坐标原点左侧，正数位于坐标原点右侧。newTopnumber是要平移到的对应位置的y轴坐标，浮点数。0表示坐标原点，负数位于坐标原点上侧，正数位于坐标原点下侧。

**示例：**

```ets
import { drawing, common2D } from '@kit.ArkGraphics2D';
let rect = drawing.RectUtils.makeLtrb(20, 20, 40, 40);
drawing.RectUtils.offsetTo(rect, 10, 20);
console.info('rect.left:', rect.left);
console.info('rect.top: ', rect.top);
console.info('rect.right: ', rect.right);
console.info('rect.bottom: ', rect.bottom);
```

#### setRect20+

static setRect(rect: common2D.Rect, other: common2D.Rect): void

使用另一个矩形对当前矩形进行赋值。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

参数名类型必填说明rect[common2D.Rect](@ohos.graphics.common2D (2D图形通用数据类型).md#ZH-CN_TOPIC_0000002529445937__rect)是原矩形。other[common2D.Rect](@ohos.graphics.common2D (2D图形通用数据类型).md#ZH-CN_TOPIC_0000002529445937__rect)是用于赋值的矩形。

**示例：**

```ets
import { drawing, common2D } from '@kit.ArkGraphics2D';
let rect = drawing.RectUtils.makeLtrb(10, 20, 30, 40);
let rect2 = drawing.RectUtils.makeEmpty();
drawing.RectUtils.setRect(rect2, rect);
console.info('rect2.left:', rect2.left);
console.info('rect2.top: ', rect2.top);
console.info('rect2.right: ', rect2.right);
console.info('rect2.bottom: ', rect2.bottom);
```

#### setLtrb20+

static setLtrb(rect: common2D.Rect, left: number, top: number, right: number, bottom: number): void

使用传入的"上下左右"的值更新当前矩形的上下左右边界值。

**系统能力**：SystemCapability.Graphics.Drawing

**参数：**

参数名类型必填说明rect[common2D.Rect](@ohos.graphics.common2D (2D图形通用数据类型).md#ZH-CN_TOPIC_0000002529445937__rect)是矩形对象。leftnumber是矩形的左上角x轴坐标，该参数为浮点数。0表示坐标原点，负数表示位于坐标原点左侧，正数表示位于坐标原点右侧。topnumber是矩形的左上角y轴坐标，该参数为浮点数。0表示坐标原点，负数表示位于坐标原点上侧，正数表示位于坐标原点下侧。rightnumber是矩形的右下角x轴坐标，该参数为浮点数。0表示坐标原点，负数表示位于坐标原点左侧，正数表示位于坐标原点右侧。bottomnumber是矩形的右下角y轴坐标，该参数为浮点数。0表示坐标原点，负数表示位于坐标原点上侧，正数表示位于坐标原点下侧。

**示例：**

```ets
import { drawing, common2D } from '@kit.ArkGraphics2D';
let rect = drawing.RectUtils.makeEmpty();
drawing.RectUtils.setLtrb(rect, 10, 20, 30, 60);
console.info('rect.left:', rect.left);
console.info('rect.top: ', rect.top);
console.info('rect.right: ', rect.right);
console.info('rect.bottom: ', rect.bottom);
```

#### setEmpty20+

static setEmpty(rect: common2D.Rect): void

将矩形的上下左右边界都设为0。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

参数名类型必填说明rect[common2D.Rect](@ohos.graphics.common2D (2D图形通用数据类型).md#ZH-CN_TOPIC_0000002529445937__rect)是用于设置为空的矩形对象。

**示例：**

```ets
import { drawing, common2D } from '@kit.ArkGraphics2D';
let rect = drawing.RectUtils.makeLtrb(10, 20, 20, 30);
drawing.RectUtils.setEmpty(rect)
console.info('rect.left:', rect.left);
console.info('rect.top: ', rect.top);
console.info('rect.right: ', rect.right);
console.info('rect.bottom: ', rect.bottom);
```

#### sort20+

static sort(rect: common2D.Rect): void

如果矩形存在反转的情况（即左边界大于右边界或上边界大于下边界），则对矩形的上下（左右）边界值进行交换，使得上边界小于下边界（左边界小于右边界）。

如果矩形不存在反转的情况（即左边界小于等于右边界或上边界小于等于下边界)，不做任何操作。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

参数名类型必填说明rect[common2D.Rect](@ohos.graphics.common2D (2D图形通用数据类型).md#ZH-CN_TOPIC_0000002529445937__rect)是用于设置的矩形对象。

**示例：**

```ets
import { drawing, common2D } from '@kit.ArkGraphics2D';
let rect = drawing.RectUtils.makeLtrb(20, 40, 30, 30);
drawing.RectUtils.sort(rect);
console.info('rect.left:', rect.left);
console.info('rect.top: ', rect.top);
console.info('rect.right: ', rect.right);
console.info('rect.bottom: ', rect.bottom);
```

#### isEqual20+

static isEqual(rect: common2D.Rect, other: common2D.Rect): boolean

判断两个矩形是否相等。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

参数名类型必填说明rect[common2D.Rect](@ohos.graphics.common2D (2D图形通用数据类型).md#ZH-CN_TOPIC_0000002529445937__rect)是需要判断的原矩形。other[common2D.Rect](@ohos.graphics.common2D (2D图形通用数据类型).md#ZH-CN_TOPIC_0000002529445937__rect)是需要判断的另一矩形。

**返回值：**

类型说明boolean返回两个矩形是否相等的结果。true表示两个矩形相等，false表示两个矩形不相等。

**示例：**

```ets
import { drawing, common2D } from '@kit.ArkGraphics2D';
let rect = drawing.RectUtils.makeLtrb(10, 20, 20, 30);
let rect2 = drawing.RectUtils.makeEmpty();
let isEqual = drawing.RectUtils.isEqual(rect, rect2);
console.info('isEqual :', isEqual);
```