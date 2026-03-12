# @ohos.matrix4 (矩阵变换)

本模块提供矩阵变换功能，支持对图形进行平移、旋转和缩放等。

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { matrix4 } from '@kit.ArkUI';
```

#### matrix4.init

init(options: [number,number,number,number,number,number,number,number,number,number,number,number,number,number,number,number]): Matrix4Transit

Matrix的构造函数，可以通过传入的参数创建一个四阶矩阵，矩阵为列优先。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明options

[number,number,number,number,

number,number,number,number,

number,number,number,number,

number,number,number,number]

是

参数为长度为16（4*4）的number数组, 详情见四阶矩阵说明。

各number取值范围：(-∞, +∞)

默认值：

[1, 0, 0, 0,

0, 1, 0, 0,

0, 0, 1, 0,

0, 0, 0, 1]

**返回值：**

类型说明[Matrix4Transit](#ZH-CN_TOPIC_0000002529284781__matrix4transit)根据入参创建的四阶矩阵对象。

**四阶矩阵说明：**

参数名类型必填说明m00number是x轴缩放值，单位矩阵默认为1。m01number是第2个值，xyz轴旋转或倾斜会影响这个值。m02number是第3个值，xyz轴旋转会影响这个值。m03number是第4个值，透视投影会影响这个值。m10number是第5个值，xyz轴旋转或倾斜会影响这个值。m11number是y轴缩放值，单位矩阵默认为1。m12number是第7个值，xyz轴旋转会影响这个值。m13number是第8个值，透视投影会影响这个值。m20number是第9个值，xyz轴旋转会影响这个值。m21number是第10个值，xyz轴旋转会影响这个值。m22number是z轴缩放值，单位矩阵默认为1。m23number是第12个值，透视投影会影响这个值。m30number是x轴平移值，单位px，单位矩阵默认为0。m31number是y轴平移值，单位px，单位矩阵默认为0。m32number是z轴平移值，单位px，单位矩阵默认为0。m33number是齐次坐标下生效，产生透视投影效果。

**示例**

```ets
import { matrix4 } from '@kit.ArkUI';

// 创建一个四阶矩阵
let matrix = matrix4.init(
  [1.0, 0.0, 0.0, 0.0,
    0.0, 1.0, 0.0, 0.0,
    0.0, 0.0, 1.0, 0.0,
    0.0, 0.0, 0.0, 1.0]);

@Entry
@Component
struct Tests {
  build() {
    Column() {
      // $r("app.media.zh")需要替换为开发者所需的图像资源文件。
      Image($r("app.media.zh"))
        .width("40%")
        .height(100)
        .transform(matrix)
    }
  }
}
```

#### matrix4.identity

identity(): Matrix4Transit

Matrix的初始化函数，可以返回一个单位矩阵对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

类型说明[Matrix4Transit](#ZH-CN_TOPIC_0000002529284781__matrix4transit)单位矩阵对象。

**示例：**

```ets
// matrix1 和 matrix2 效果一致
import { matrix4 } from '@kit.ArkUI';

let matrix1 = matrix4.init(
  [1.0, 0.0, 0.0, 0.0,
    0.0, 1.0, 0.0, 0.0,
    0.0, 0.0, 1.0, 0.0,
    0.0, 0.0, 0.0, 1.0]);
let matrix2 = matrix4.identity();

@Entry
@Component
struct Tests {
  build() {
    Column() {
      // $r("app.media.zh")需要替换为开发者所需的图像资源文件。
      Image($r("app.media.zh"))
        .width("40%")
        .height(100)
        .transform(matrix1)
      // $r("app.media.zh")需要替换为开发者所需的图像资源文件。
      Image($r("app.media.zh"))
        .width("40%")
        .height(100)
        .margin({ top: 150 })
        .transform(matrix2)
    }
  }
}
```

#### Matrix4Transit

矩阵对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

#### copy

copy(): Matrix4Transit

Matrix的拷贝函数，可以拷贝一份当前的矩阵对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

类型说明[Matrix4Transit](#ZH-CN_TOPIC_0000002529284781__matrix4transit)当前矩阵的拷贝对象。

**示例：**

```ets
// xxx.ets
import { matrix4 } from '@kit.ArkUI';

@Entry
@Component
struct Test {
  private matrix1 = matrix4.identity().scale({ x: 1.5 });
  private matrix2 = this.matrix1.copy().translate({ x: 200 });
  imageSize: Length = '300px';

  build() {
    Column({ space: "50px" }) {
      // $r("app.media.testImage")需要替换为开发者所需的图像资源文件。
      Image($r("app.media.testImage"))
        .width(this.imageSize)
        .height(this.imageSize)
      // $r("app.media.testImage")需要替换为开发者所需的图像资源文件。
      Image($r("app.media.testImage"))
        .width(this.imageSize)
        .height(this.imageSize)
        .transform(this.matrix1)
      // $r("app.media.testImage")需要替换为开发者所需的图像资源文件。
      Image($r("app.media.testImage"))
        .width(this.imageSize)
        .height(this.imageSize)
        .transform(this.matrix2)
    }.alignItems(HorizontalAlign.Center)
    .height('100%').width("100%")
    .justifyContent(FlexAlign.Center)
  }
}
```

#### combine

combine(options: Matrix4Transit): Matrix4Transit

Matrix的叠加函数，可以将两个矩阵的效果叠加起来生成一个新的矩阵对象。会改变调用该函数的原始矩阵。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明options[Matrix4Transit](#ZH-CN_TOPIC_0000002529284781__matrix4transit)是待叠加的矩阵对象。

**返回值：**

类型说明[Matrix4Transit](#ZH-CN_TOPIC_0000002529284781__matrix4transit)矩阵叠加后的对象。

**示例：**

```ets
// xxx.ets
import { matrix4 } from '@kit.ArkUI';

@Entry
@Component
struct Test {
  private matrix1 = matrix4.identity().translate({ x: 200 });
  private matrix2 = matrix4.identity().scale({ x: 2 });

  build() {
    Column() {
      // 矩阵变换前
      // $r("app.media.icon")需要替换为开发者所需的图像资源文件。
      Image($r("app.media.icon"))
        .width("40%")
        .height(100)
        .margin({ top: 50 })
      // 先平移x轴200px，再缩放两倍x轴，得到矩阵变换后的效果图
      // $r("app.media.icon")需要替换为开发者所需的图像资源文件。
      Image($r("app.media.icon"))
        .transform(this.matrix1.copy().combine(this.matrix2))
        .width("40%")
        .height(100)
        .margin({ top: 50 })
    }
  }
}
```

#### invert

invert(): Matrix4Transit

Matrix的逆函数，可以返回一个当前矩阵对象的逆矩阵，即效果正好相反。会改变调用该函数的原始矩阵。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

类型说明[Matrix4Transit](#ZH-CN_TOPIC_0000002529284781__matrix4transit)当前矩阵的逆矩阵对象。

**示例：**

```ets
import { matrix4 } from '@kit.ArkUI';

// matrix1(宽放大2倍) 和 matrix2(宽缩小2倍) 效果相反
let matrix1 = matrix4.identity().scale({ x: 2 });
let matrix2 = matrix1.copy().invert();

@Entry
@Component
struct Tests {
  build() {
    Column() {
      // $r("app.media.zh")需要替换为开发者所需的图像资源文件。
      Image($r("app.media.zh"))
        .width(200)
        .height(100)
        .transform(matrix1)
        .margin({ top: 100 })
      // $r("app.media.zh")需要替换为开发者所需的图像资源文件。
      Image($r("app.media.zh"))
        .width(200)
        .height(100)
        .margin({ top: 150 })
        .transform(matrix2)
    }
  }
}
```

#### translate

translate(options: TranslateOption): Matrix4Transit

Matrix的平移函数，可以为当前矩阵增加x轴/y轴/z轴平移效果。会改变调用该函数的原始矩阵。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明options[TranslateOption](#ZH-CN_TOPIC_0000002529284781__translateoption)是设置平移参数。

**返回值：**

类型说明[Matrix4Transit](#ZH-CN_TOPIC_0000002529284781__matrix4transit)平移效果后的矩阵对象。

**示例：**

```ets
// xxx.ets
import { matrix4 } from '@kit.ArkUI';

@Entry
@Component
struct Test {
  private matrix1 = matrix4.identity().translate({ x: 100, y: 200, z: 30 });

  build() {
    Column() {
      // $r("app.media.bg1")需要替换为开发者所需的图像资源文件。
      Image($r("app.media.bg1")).transform(this.matrix1)
        .width("40%")
        .height(100)
    }
  }
}
```

#### scale

scale(options: ScaleOption): Matrix4Transit

Matrix的缩放函数，可以为当前矩阵增加x轴/y轴/z轴缩放效果。会改变调用该函数的原始矩阵。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明options[ScaleOption](#ZH-CN_TOPIC_0000002529284781__scaleoption)是设置缩放参数。

**返回值：**

类型说明[Matrix4Transit](#ZH-CN_TOPIC_0000002529284781__matrix4transit)缩放效果后的矩阵对象。

**示例：**

```ets
// xxx.ets
import { matrix4 } from '@kit.ArkUI';

@Entry
@Component
struct Test {
  private matrix1 = matrix4.identity()
    .scale({
      x: 2,
      y: 3,
      z: 4,
      centerX: 50,
      centerY: 50
    });

  build() {
    Column() {
      // $r("app.media.testImage")需要替换为开发者所需的图像资源文件。
      Image($r("app.media.testImage")).transform(this.matrix1)
        .width("300px")
        .height("300px")
    }.width("100%").height("100%").justifyContent(FlexAlign.Center)
  }
}
```

#### skew12+

skew(x: number, y: number): Matrix4Transit

Matrix的倾斜函数，可以为当前矩阵增加x轴/y轴倾斜效果。会改变调用该函数的原始矩阵。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明xnumber是设置x轴倾斜参数。ynumber是设置y轴倾斜参数。

**返回值：**

类型说明[Matrix4Transit](#ZH-CN_TOPIC_0000002529284781__matrix4transit)倾斜效果后的矩阵对象。

**示例：**

```ets
// xxx.ets
import { matrix4 } from '@kit.ArkUI';

@Entry
@Component
struct Test {
  private matrix1 = matrix4.identity().skew(2, 3);

  build() {
    Column() {
      // $r("app.media.bg1")需要替换为开发者所需的图像资源文件。
      Image($r("app.media.bg1")).transform(this.matrix1)
        .height(100)
        .margin({
          top: 300
        })
    }
    .width("100%")
    .height("100%")
  }
}
```

#### rotate

rotate(options: RotateOption): Matrix4Transit

Matrix的旋转函数，可以为当前矩阵增加x轴/y轴/z轴旋转效果。会改变调用该函数的原始矩阵。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明options[RotateOption](#ZH-CN_TOPIC_0000002529284781__rotateoption)是设置旋转参数。

**返回值：**

类型说明[Matrix4Transit](#ZH-CN_TOPIC_0000002529284781__matrix4transit)旋转效果后的矩阵对象。

**示例：**

```ets
// xxx.ets
import { matrix4 } from '@kit.ArkUI';

@Entry
@Component
struct Test {
  private matrix1 = matrix4.identity()
    .rotate({
      x: 1,
      y: 1,
      z: 2,
      angle: 30
    });

  build() {
    Column() {
      // $r("app.media.bg1")需要替换为开发者所需的图像资源文件。
      Image($r("app.media.bg1")).transform(this.matrix1)
        .width("40%")
        .height(100)
    }.width("100%").margin({ top: 50 })
  }
}
```

#### transformPoint

transformPoint(options: [number, number]): [number, number]

Matrix的坐标点转换函数，可以将当前的变换效果作用到一个坐标点上。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明options[number, number]是需要转换的坐标点。

**返回值：**

类型说明[number, number]返回矩阵变换后的Point对象。

**示例：**

```ets
// xxx.ets
import { matrix4 } from '@kit.ArkUI';

@Entry
@Component
struct Test {
  private originPoint: number[] = [50, 50];
  private matrix_1 = matrix4.identity().translate({ x: 150, y: -50 });
  private transformPoint = this.matrix_1.transformPoint([this.originPoint[0], this.originPoint[1]]);
  private matrix_2 = matrix4.identity().translate({ x: this.transformPoint[0], y: this.transformPoint[1] });

  build() {
    Column() {
      Text(`矩阵变换前的坐标：[${this.originPoint}]`)
        .fontSize(16)
      // $r("app.media.image")需要替换为开发者所需的图像资源文件。
      Image($r("app.media.image"))
        .width('600px')
        .height('300px')
        .margin({ top: 50 })
      Text(`矩阵变换后的坐标：[${this.transformPoint}]`)
        .fontSize(16)
        .margin({ top: 100 })
      // $r("app.media.image")需要替换为开发者所需的图像资源文件。
      Image($r("app.media.image"))
        .width('600px')
        .height('300px')
        .margin({ top: 50 })
        .transform(this.matrix_2)
    }.width("100%").padding(50)
  }
}
```

#### setPolyToPoly12+

setPolyToPoly(options: PolyToPolyOptions): Matrix4Transit

将一个多边形的顶点坐标映射到另外一个多边形的顶点坐标。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明options[PolyToPolyOptions](#ZH-CN_TOPIC_0000002529284781__polytopolyoptions12)是映射相关的参数。

**返回值：**

类型说明[Matrix4Transit](#ZH-CN_TOPIC_0000002529284781__matrix4transit)当前矩阵变换后的对象。

需要配合scale({centerX:0,centerY:0,x:1})保证变换的中心点是组件左上角。

**示例：**

```ets
import { matrix4 } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  private matrix1 = matrix4.identity().setPolyToPoly({
    src: [{ x: 0, y: 0 }, { x: 500, y: 0 }, { x: 0, y: 500 }, { x: 500, y: 500 }],
    dst: [{ x: 0, y: 0 }, { x: 500, y: 0 }, { x: 0, y: 500 }, { x: 750, y: 1000 }], pointCount: 4
  });

  build() {
    Stack() {
      Column().backgroundColor(Color.Blue)
        .width('500px')
        .height('500px')
      // $r("app.media.transition_image1")需要替换为开发者所需的图像资源文件。
      Image($r('app.media.transition_image1'))
        .scale({ centerX: 0, centerY: 0, x: 1 })
        .transform(this.matrix1)
        .width('500px')
        .height('500px')
    }.width("100%").height("100%").opacity(0.5)
  }
}
```

#### TranslateOption

平移参数。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明xnumber否是

x轴的平移距离。

单位：px

默认值：0

取值范围 (-∞, +∞)

ynumber否是

y轴的平移距离。

单位：px

默认值：0

取值范围 (-∞, +∞)

znumber否是

z轴的平移距离。

单位：px

默认值：0

取值范围 (-∞, +∞)

#### ScaleOption

缩放参数。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明xnumber否是

x轴的缩放倍数。x>1时以x轴方向放大，0<x<1时以x轴方向缩小，x<0时沿x轴反向并缩放。

默认值：1

取值范围 (-∞, +∞)

ynumber否是

y轴的缩放倍数。y>1时以y轴方向放大，0<y<1时以y轴方向缩小，y<0时沿y轴反向并缩放。

默认值：1

取值范围 (-∞, +∞)

znumber否是

z轴的缩放倍数。z>1时以z轴方向放大，0<z<1时以z轴方向缩小，z<0时沿z轴反向并缩放。

默认值：1

取值范围 (-∞, +∞)

centerXnumber否是

变换中心点x轴坐标。

单位：px

默认值：组件中心点x轴坐标。

取值范围 (-∞, +∞)

centerYnumber否是

变换中心点y轴坐标。

单位：px

默认值：组件中心点y轴坐标。

取值范围 (-∞, +∞)

#### RotateOption

旋转参数。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明xnumber否是

旋转轴向量x坐标。

默认值：0。

取值范围 (-∞, +∞)

ynumber否是

旋转轴向量y坐标。

默认值：0。

取值范围 (-∞, +∞)

znumber否是

旋转轴向量z坐标。

默认值：0。

取值范围 (-∞, +∞)。

**说明：** 旋转向量中x、y、z至少有一个不为0才有意义。

anglenumber否是

旋转角度。

默认值：0

centerXnumber否是

单次矩阵变换中心点相对于组件变换中心点（锚点）的额外x轴偏移值。

单位：px

默认值：0

**说明：**

为0时表示x方向的矩阵变换中心恰好为组件x方向锚点，取值表示相对组件x方向锚点的额外偏移量。具体实现可参考[示例3（按中心点旋转）](图形变换.md#ZH-CN_TOPIC_0000002497604834__示例3按中心点旋转)。

centerYnumber否是

单次矩阵变换中心点相对于组件变换中心点（锚点）的额外y轴偏移值。

单位：px

默认值：0

**说明：**

为0时表示y方向的矩阵变换中心恰好为组件y方向锚点，取值表示相对组件y方向锚点的额外偏移量。具体实现可参考[示例3（按中心点旋转）](图形变换.md#ZH-CN_TOPIC_0000002497604834__示例3按中心点旋转)。

#### PolyToPolyOptions12+

多边形到多边形的映射选项。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明srcArray<[Point](#ZH-CN_TOPIC_0000002529284781__point12)>否否源点坐标。srcIndexnumber否是

源点坐标起始索引。

默认值:0

 取值范围：[0, +∞)

dstArray<[Point](#ZH-CN_TOPIC_0000002529284781__point12)>否否目标点坐标。dstIndexnumber否是

目标坐标起始索引。

默认值: src.length/2

 取值范围：[0, +∞)

pointCountnumber否是

使用到的点数量。要使用的点的数量如果为0，则返回单位矩阵。如果为1，则返回一个将两个点改变之前的平移矩阵。如果为2-4，则返回一个变换矩阵。

默认值: 0

 取值范围：[0, +∞)

#### Point12+

坐标点的数据结构。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明xnumber否否

x轴坐标。

取值范围：(-∞, +∞)

ynumber否否

y轴坐标。

取值范围：(-∞, +∞)

#### matrix4.copy(deprecated)

copy(): Matrix4Transit

Matrix的拷贝函数，可以拷贝一份当前的矩阵对象。

从API version 7开始支持，从API version 10开始废弃，暂无替代接口。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

类型说明[Matrix4Transit](#ZH-CN_TOPIC_0000002529284781__matrix4transit)当前矩阵的拷贝对象。

**示例：**

```ets
// xxx.ets
import { matrix4 } from '@kit.ArkUI';

@Entry
@Component
struct Test {
  private matrix1 = matrix4.identity().translate({ x: 100 });
  // 对matrix1的拷贝矩阵做scale操作，不影响到matrix1
  private matrix2 = this.matrix1.copy().scale({ x: 2 });

  build() {
    Column() {
      // $r("app.media.bg1")需要替换为开发者所需的图像资源文件。
      Image($r("app.media.bg1"))
        .width("40%")
        .height(100)
        .transform(this.matrix1)
      // $r("app.media.bg2")需要替换为开发者所需的图像资源文件。
      Image($r("app.media.bg2"))
        .width("40%")
        .height(100)
        .margin({ top: 50 })
        .transform(this.matrix2)
    }
  }
}
```

#### matrix4.invert(deprecated)

invert(): Matrix4Transit

Matrix的逆函数，可以返回一个当前矩阵对象的逆矩阵，即效果正好相反。

从API version 7开始支持，从API version 10开始废弃，暂无替代接口。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

类型说明[Matrix4Transit](#ZH-CN_TOPIC_0000002529284781__matrix4transit)当前矩阵的逆矩阵对象。

#### matrix4.combine(deprecated)

combine(options: Matrix4Transit): Matrix4Transit

Matrix的叠加函数，可以将两个矩阵的效果叠加起来生成一个新的矩阵对象。

从API version 7开始支持，从API version 10开始废弃，暂无替代接口。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明options[Matrix4Transit](#ZH-CN_TOPIC_0000002529284781__matrix4transit)是待叠加的矩阵对象。

**返回值：**

类型说明[Matrix4Transit](#ZH-CN_TOPIC_0000002529284781__matrix4transit)叠加后的矩阵对象。

#### matrix4.translate(deprecated)

translate(options: TranslateOption): Matrix4Transit

Matrix的平移函数，可以为当前矩阵增加x轴/y轴/z轴平移效果。

从API version 7开始支持，从API version 10开始废弃，暂无替代接口。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明options[TranslateOption](#ZH-CN_TOPIC_0000002529284781__translateoption)是设置平移参数。

**返回值：**

类型说明[Matrix4Transit](#ZH-CN_TOPIC_0000002529284781__matrix4transit)平移后的矩阵对象。

#### matrix4.scale(deprecated)

scale(options: ScaleOption): Matrix4Transit

Matrix的缩放函数，可以为当前矩阵增加x轴/y轴/z轴缩放效果。

从API version 7开始支持，从API version 10开始废弃，暂无替代接口。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明options[ScaleOption](#ZH-CN_TOPIC_0000002529284781__scaleoption)是设置缩放参数。

**返回值：**

类型说明[Matrix4Transit](#ZH-CN_TOPIC_0000002529284781__matrix4transit)缩放后的矩阵对象。

#### matrix4.rotate(deprecated)

rotate(options: RotateOption): Matrix4Transit

Matrix的旋转函数，可以为当前矩阵增加x轴/y轴/z轴旋转效果。

从API version 7开始支持，从API version 10开始废弃，暂无替代接口。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明options[RotateOption](#ZH-CN_TOPIC_0000002529284781__rotateoption)是设置旋转参数。

**返回值：**

类型说明[Matrix4Transit](#ZH-CN_TOPIC_0000002529284781__matrix4transit)旋转后的矩阵对象。

#### matrix4.transformPoint(deprecated)

transformPoint(options: [number, number]): [number, number]

Matrix的坐标点转换函数，可以将当前的变换效果作用到一个坐标点上。

从API version 7开始支持，从API version 10开始废弃，暂无替代接口。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明options[number, number]是需要转换的坐标点。

**返回值：**

类型说明[number, number]返回矩阵变换后的Point对象。