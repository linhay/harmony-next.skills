# @ohos.arkui.shape (形状)

在 clipShape 和 maskShape 接口中可以传入对应的形状。

-

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

-

示例效果请以真机运行为准，当前DevEco Studio预览器不支持。

#### 导入模块

```ets
import { CircleShape, EllipseShape, PathShape, RectShape } from "@kit.ArkUI";
```

#### CircleShape

用于 clipShape 和 maskShape 接口的圆形形状。

继承自[BaseShape](#ZH-CN_TOPIC_0000002497444794__baseshape)。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

#### constructor

constructor(options?: ShapeSize)

创建CircleShape对象。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明options[ShapeSize](#ZH-CN_TOPIC_0000002497444794__shapesize)否形状的大小。

#### EllipseShape

用于 clipShape 和 maskShape 接口的椭圆形状。

继承自[BaseShape](#ZH-CN_TOPIC_0000002497444794__baseshape)。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

#### constructor

constructor(options?: ShapeSize)

创建EllipseShape对象。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明options[ShapeSize](#ZH-CN_TOPIC_0000002497444794__shapesize)否形状的大小。

#### PathShape

用于 clipShape 和 maskShape 接口的路径。

继承自[CommonShapeMethod](#ZH-CN_TOPIC_0000002497444794__commonshapemethod)。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

#### constructor

constructor(options?: PathShapeOptions)

创建PathShape对象。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明options[PathShapeOptions](#ZH-CN_TOPIC_0000002497444794__pathshapeoptions)否路径参数。

#### commands

commands(commands: string): PathShape

设置路径的绘制指令。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明commandsstring是路径的绘制指令。

**返回值：**

类型说明PathShape返回PathShape对象。

#### RectShape

用于 clipShape 和 maskShape 接口的矩形形状。

继承自[BaseShape](#ZH-CN_TOPIC_0000002497444794__baseshape)。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

#### constructor

constructor(options?: RectShapeOptions | RoundRectShapeOptions)

创建RectShape对象。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明options[RectShapeOptions](#ZH-CN_TOPIC_0000002497444794__rectshapeoptions) | [RoundRectShapeOptions](#ZH-CN_TOPIC_0000002497444794__roundrectshapeoptions)否矩形形状参数。

#### radiusWidth

radiusWidth(rWidth: number | string): RectShape

设置矩形形状圆角半径的宽度。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明rWidthnumber | string是

矩形形状圆角半径的宽度。

 类型为number时取值范围是[0, +∞)，string时是[Length](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__length)。

**返回值：**

类型说明RectShape返回RectShape对象。

#### radiusHeight

radiusHeight(rHeight: number | string): RectShape

设置矩形形状圆角半径的高度。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明rHeightnumber | string是

矩形形状圆角半径的高度。

 类型为number时取值范围是[0, +∞)，string时是[Length](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__length)。

**返回值：**

类型说明RectShape返回RectShape对象。

#### radius

radius(radius: number | string | Array<number | string>): RectShape

设置矩形形状的圆角半径。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明radiusnumber | string | Array<number | string>是

矩形形状的圆角半径。仅接受数组的前四个元素，分别为矩形左上，右上，左下，右下的圆角半径。

 类型为number时取值范围是[0, +∞)，string时是[Length](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__length)。

**返回值：**

类型说明RectShape返回RectShape对象。

#### ShapeSize

形状的尺寸参数。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明widthnumber | string否是

形状的宽度。

 类型为number时取值范围是[0, +∞)，string时是[Length](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__length)。

单位：vp

heightnumber | string否是

形状的高度。

 类型为number时取值范围是[0, +∞)，string时是[Length](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__length)。

单位：vp

#### PathShapeOptions

PathShape 的构造函数参数。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明commandsstring否是绘制路径的指令。更多说明请参考commands支持的[绘制命令](Path.md#ZH-CN_TOPIC_0000002529444887__commands)。

#### RectShapeOptions

RectShape 的构造函数参数。

继承自[ShapeSize](#ZH-CN_TOPIC_0000002497444794__shapesize)。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明radiusnumber | string | Array<number | string>否是

矩形形状的圆角半径。

 类型为number时取值范围是[0, +∞)，string时是[Length](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__length)。

#### RoundRectShapeOptions

RectShape 带有半径的构造函数参数。

继承自[ShapeSize](#ZH-CN_TOPIC_0000002497444794__shapesize)。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明radiusWidthnumber | string否是

矩形形状圆角半径的宽度。

 类型为number时取值范围是[0, +∞)，string时是[Length](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__length)。

radiusHeightnumber | string否是

矩形形状圆角半径的高度。

 类型为number时取值范围是[0, +∞)，string时是[Length](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__length)。

#### BaseShape

继承自[CommonShapeMethod](#ZH-CN_TOPIC_0000002497444794__commonshapemethod)。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

#### width

width(width: Length): T

设置形状的宽度。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明width[Length](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__length)是形状的宽度。

**返回值：**

类型说明T返回当前对象。

#### height

height(height: Length): T

设置形状的高度。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明height[Length](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__length)是形状的高度。

**返回值：**

类型说明T返回当前对象。

#### size

size(size: SizeOptions): T

设置形状的大小。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明size[SizeOptions](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__sizeoptions)是形状的大小。

**返回值：**

类型说明T返回当前对象。

#### CommonShapeMethod

常见的形状方法。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

#### offset

offset(offset: Position): T

设置相对于组件布局位置的坐标偏移。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明offset[Position](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__position)是相对于组件布局位置的坐标偏移。

**返回值：**

类型说明T返回当前对象。

#### fill

fill(color: ResourceColor): T

设置形状的填充区域的透明度，黑色表示完全透明，白色表示完全不透明。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明color[ResourceColor](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)是形状的填充区域的透明度，黑色表示完全透明，白色表示完全不透明。

**返回值：**

类型说明T返回当前对象。

#### position

position(position: Position): T

设置形状的位置。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明position[Position](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__position)是设置形状的位置。

**返回值：**

类型说明T返回当前对象。

#### **示例**

```ets
import { CircleShape, EllipseShape, PathShape, RectShape } from "@kit.ArkUI";

@Entry
@Component
struct ShapeExample {
  build() {
    Column({ space: 15 }) {
      Text('CircleShape, position').fontSize(20).width('75%').fontColor('#DCDCDC')
      Image($r('app.media.startIcon'))
        .clipShape(new CircleShape({ width: '280px', height: '280px' }).position({ x: '20px', y: '20px' }))
        .width('500px').height('280px')

      Text('EllipseShape, offset').fontSize(20).width('75%').fontColor('#DCDCDC')
      Image($r('app.media.startIcon'))
        .clipShape(new EllipseShape({ width: '350px', height: '280px' }).offset({ x: '10px', y: '10px' }))
        .width('500px').height('280px')

      Text('PathShape, fill').fontSize(20).width('75%').fontColor('#DCDCDC')
      Image($r('app.media.startIcon'))
        .maskShape(new PathShape().commands('M100 0 L200 240 L0 240 Z').fill(Color.Red))
        .width('500px').height('280px')

      Text('RectShape, width, height, fill').fontSize(20).width('75%').fontColor('#DCDCDC')
      Image($r('app.media.startIcon'))
        .maskShape(new RectShape().width('350px').height('280px').fill(Color.Red))
        .width('500px').height('280px')
    }
    .width('100%')
    .margin({ top: 15 })
  }
}
```