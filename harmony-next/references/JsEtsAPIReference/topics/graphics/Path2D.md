# Path2D

路径对象，支持通过对象的接口进行路径的描述，并通过Canvas的stroke接口或者fill接口进行绘制。

 从 API version 8 开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

 Path2D对象不支持重置已设置的路径，如需新路径可重新创建一个空的Path2D对象。

 Path2D对象的方法无法对[CanvasRenderingContext2D](../components/CanvasRenderingContext2D.md)和[OffscreenCanvasRenderingContext2D](../components/OffscreenCanvasRenderingContext2D.md)对象中设置的路径生效。

#### 构造函数

#### constructor

constructor()

构造一个空的Path2D对象。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

#### constructor12+

constructor(unit: LengthMetricsUnit)

构造一个空的Path2D对象，支持配置Path2D对象的单位模式。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明unit[LengthMetricsUnit](Graphics.md#ZH-CN_TOPIC_0000002529444761__lengthmetricsunit12)是

用来配置Path2D对象的单位模式，配置后无法动态更改，配置方法同[CanvasRenderingContext2D](../components/CanvasRenderingContext2D.md)。

异常值NaN和Infinity按默认值处理。

默认值：DEFAULT

#### constructor

constructor(path: Path2D)

使用路径对象构造Path2D对象。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明pathPath2D是路径对象。

#### constructor12+

constructor(path: Path2D, unit: LengthMetricsUnit)

使用路径对象构造Path2D对象，支持配置Path2D对象的单位模式。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明pathPath2D是路径对象。unit[LengthMetricsUnit](Graphics.md#ZH-CN_TOPIC_0000002529444761__lengthmetricsunit12)是

用来配置Path2D对象的单位模式，配置后无法动态更改，配置方法同[CanvasRenderingContext2D](../components/CanvasRenderingContext2D.md)。

异常值NaN和Infinity按默认值处理。

默认值：DEFAULT

#### constructor

constructor(d: string)

使用符合SVG路径描述规范的路径字符串构造Path2D对象。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明dstring是符合SVG路径描述规范的路径字符串，格式参考[SVG路径描述规范](path.md#ZH-CN_TOPIC_0000002529444887__svg路径描述规范)，异常值按无效值处理。

#### constructor12+

constructor(description: string, unit: LengthMetricsUnit)

使用符合SVG路径描述规范的路径字符串构造Path2D对象，支持配置Path2D对象的单位模式。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明descriptionstring是符合SVG路径描述规范的路径字符串，格式参考[SVG路径描述规范](path.md#ZH-CN_TOPIC_0000002529444887__svg路径描述规范)，异常值按无效值处理。unit[LengthMetricsUnit](Graphics.md#ZH-CN_TOPIC_0000002529444761__lengthmetricsunit12)是

用来配置Path2D对象的单位模式，配置后无法动态更改，配置方法同[CanvasRenderingContext2D](../components/CanvasRenderingContext2D.md)。

异常值NaN和Infinity按默认值处理。

默认值：DEFAULT

#### 方法

#### addPath

addPath(path: Path2D, transform?: Matrix2D): void

将另一个路径添加到当前的路径对象中。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明pathPath2D是

需要添加到当前路径的路径对象，路径单位：px。

异常值undefined和null按无效值处理。

transform[Matrix2D](Matrix2D.md)否

新增路径的变换矩阵对象。

异常值undefined和null按无效值处理。

默认值：null

**示例：**

```ets
// xxx.ets
@Entry
@Component
struct AddPath {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private path2Da: Path2D = new Path2D("M250 150 L150 350 L350 350 Z");
  private path2Db: Path2D = new Path2D();

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() => {
          this.path2Db.addPath(this.path2Da)
          this.context.stroke(this.path2Db)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

#### closePath

closePath(): void

将路径的当前点移回到路径的起点，当前点到起点间画一条直线。如果形状已经闭合或只有一个点，则此功能不执行任何操作。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```ets
// xxx.ets
@Entry
@Component
struct ClosePath {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private path2Db: Path2D = new Path2D();

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() => {
          this.path2Db.moveTo(200, 100)
          this.path2Db.lineTo(300, 100)
          this.path2Db.lineTo(200, 200)
          this.path2Db.closePath()
          this.context.stroke(this.path2Db)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

#### moveTo

moveTo(x: number, y: number): void

将路径的当前坐标点移动到目标点，移动过程中不绘制线条。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数类型必填描述xnumber是

目标点X轴坐标。

API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。

默认单位：vp

ynumber是

目标点Y轴坐标。

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
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private path2Db: Path2D = new Path2D();

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() => {
          this.path2Db.moveTo(50, 100)
          this.path2Db.lineTo(250, 100)
          this.path2Db.lineTo(150, 200)
          this.path2Db.closePath()
          this.context.stroke(this.path2Db)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

#### lineTo

lineTo(x: number, y: number): void

从当前点绘制一条直线到目标点。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明xnumber是

目标点X轴坐标。

API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。

默认单位：vp

ynumber是

目标点Y轴坐标。

API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。

默认单位：vp

**示例：**

```ets
// xxx.ets
@Entry
@Component
struct LineTo {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private path2Db: Path2D = new Path2D();

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() => {
          this.path2Db.moveTo(100, 100)
          this.path2Db.lineTo(100, 200)
          this.path2Db.lineTo(200, 200)
          this.path2Db.lineTo(200, 100)
          this.path2Db.closePath()
          this.context.stroke(this.path2Db)
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
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private path2Db: Path2D = new Path2D();

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() => {
          this.path2Db.moveTo(10, 10)
          this.path2Db.bezierCurveTo(20, 100, 200, 100, 200, 20)
          this.context.stroke(this.path2Db)
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
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private path2Db: Path2D = new Path2D();

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() => {
          this.path2Db.moveTo(10, 10)
          this.path2Db.quadraticCurveTo(100, 100, 200, 20)
          this.context.stroke(this.path2Db)
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

单位：弧度。

endAnglenumber是

弧线的终止弧度。

API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。

单位：弧度。

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
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private path2Db: Path2D = new Path2D();

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() => {
          this.path2Db.arc(100, 75, 50, 0, 6.28)
          this.context.stroke(this.path2Db)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

#### arcTo

arcTo(x1: number, y1: number, x2: number, y2: number, radius: number): void

依据圆弧经过的点和圆弧半径创建圆弧路径。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明x1number是

圆弧经过的第一个点的x坐标值。

API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。

默认单位：vp

y1number是

圆弧经过的第一个点的y坐标值。

API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。

默认单位：vp

x2number是

圆弧经过的第二个点的x坐标值。

API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。

默认单位：vp

y2number是

圆弧经过的第二个点的y坐标值。

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
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private path2Db: Path2D = new Path2D();

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() => {
          this.path2Db.moveTo(0, 0)
          this.path2Db.arcTo(150, 20, 150, 70, 50)
          this.context.stroke(this.path2Db)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

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
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private path2Db: Path2D = new Path2D();

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() => {
          this.path2Db.ellipse(200, 200, 50, 100, 0, Math.PI * 1, Math.PI * 2)
          this.context.stroke(this.path2Db)
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
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private path2Db: Path2D = new Path2D();

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() => {
          this.path2Db.rect(20, 20, 100, 100);
          this.context.stroke(this.path2Db)
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

以下错误码的详细介绍请参见[Canvas组件错误码](../../errors/Canvas组件错误码.md)。

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
  private pathA: Path2D = new Path2D();
  private pathB: Path2D = new Path2D();

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#D5D5D5')
        .onReady(() => {
          try {
            this.context.fillStyle = '#707070'
            // 创建一个(10vp, 10vp)为起点，宽高为100vp，四个矩形角圆弧半径为10vp的圆角矩形
            this.pathA.roundRect(10, 10, 100, 100, 10)
            // 创建一个(120vp, 10vp)为起点，宽高为100vp，四个矩形角圆弧半径为10vp的圆角矩形
            this.pathA.roundRect(120, 10, 100, 100, [10])
            this.context.fill(this.pathA)
            // 创建一个(10vp, 120vp)为起点，宽高为100vp，左上矩形角圆弧半径及右下矩形角圆弧半径为10vp，右上矩形角圆弧半径及左下矩形角圆弧半径为20vp的圆角矩形
            this.pathB.roundRect(10, 120, 100, 100, [10, 20])
            // 创建一个(120vp, 120vp)为起点，宽高为100vp，左上矩形角圆弧半径为10vp，右上矩形角圆弧半径及左下矩形角圆弧半径为20vp，右下矩形角圆弧半径为30vp的圆角矩形
            this.pathB.roundRect(120, 120, 100, 100, [10, 20, 30])
            // 创建一个(10vp, 230vp)为起点，宽高为100vp，左上矩形角圆弧半径为10vp，右上矩形角圆弧半径为20vp，右下矩形角圆弧半径为30vp，左下矩形角圆弧半径为40vp的圆角矩形
            this.pathB.roundRect(10, 230, 100, 100, [10, 20, 30, 40])
            // 创建一个(220vp, 330vp)为起点，宽高为-100vp，左上矩形角圆弧半径为10vp，右上矩形角圆弧半径为20vp，右下矩形角圆弧半径为30vp，左下矩形角圆弧半径为40vp的圆角矩形
            this.pathB.roundRect(220, 330, -100, -100, [10, 20, 30, 40])
            this.context.stroke(this.pathB)
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