# @ohos.curves (插值计算)

本模块提供设置动画插值曲线功能，用于构造阶梯曲线对象、三阶贝塞尔曲线对象和弹簧曲线对象。

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { curves } from '@kit.ArkUI';
```

#### curves.initCurve9+

initCurve(curve?: Curve): ICurve

插值曲线的初始化函数，可以根据入参创建一个插值曲线对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| curve | Curve | 否 | 曲线类型。 默认值：Curve.Linear |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ICurve | 曲线的插值对象。 |

#### Curve

插值曲线和动效请参考[贝塞尔曲线](https://developer.huawei.com/consumer/cn/doc/design-guides/animation-attributes-0000001797117229)。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| Linear | 0 | 表示动画从头到尾的速度都是相同的。 |
| Ease | 1 | 表示动画以低速开始，然后加快，在结束前变慢，cubic-bezier(0.25, 0.1, 0.25, 1.0)。 |
| EaseIn | 2 | 表示动画以低速开始，cubic-bezier(0.42, 0.0, 1.0, 1.0)。 |
| EaseOut | 3 | 表示动画以低速结束，cubic-bezier(0.0, 0.0, 0.58, 1.0)。 |
| EaseInOut | 4 | 表示动画以低速开始和结束，cubic-bezier(0.42, 0.0, 0.58, 1.0)。 |
| FastOutSlowIn | 5 | 标准曲线，cubic-bezier(0.4, 0.0, 0.2, 1.0)。 |
| LinearOutSlowIn | 6 | 减速曲线，cubic-bezier(0.0, 0.0, 0.2, 1.0)。 |
| FastOutLinearIn | 7 | 加速曲线，cubic-bezier(0.4, 0.0, 1.0, 1.0)。 |
| ExtremeDeceleration | 8 | 急缓曲线，cubic-bezier(0.0, 0.0, 0.0, 1.0)。 |
| Sharp | 9 | 锐利曲线，cubic-bezier(0.33, 0.0, 0.67, 1.0)。 |
| Rhythm | 10 | 节奏曲线，cubic-bezier(0.7, 0.0, 0.2, 1.0)。 |
| Smooth | 11 | 平滑曲线，cubic-bezier(0.4, 0.0, 0.4, 1.0)。 |
| Friction | 12 | 阻尼曲线，cubic-bezier(0.2, 0.0, 0.2, 1.0)。 |

**示例：**

```ets
import { curves } from '@kit.ArkUI';
curves.initCurve(Curve.EaseIn) // 创建一个默认先慢后快插值曲线
```

#### curves.stepsCurve9+

stepsCurve(count: number, end: boolean): ICurve

构造阶梯曲线对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| count | number | 是 | 阶梯的数量，需要为正整数。 取值范围：[1, +∞) 说明：  设置小于1的值时，按值为1处理。 |
| end | boolean | 是 | 在每个间隔的起点或终点发生阶跃变化。 -true：在终点发生阶跃变化。 -false：在起点发生阶跃变化。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ICurve | 曲线的插值对象。 |

**示例：**

```ets
import { curves } from '@kit.ArkUI';
curves.stepsCurve(9, true)  //创建一个阶梯曲线
```

#### curves.cubicBezierCurve9+

cubicBezierCurve(x1: number, y1: number, x2: number, y2: number): ICurve

构造三阶贝塞尔曲线对象，确保曲线的值在0到1之间。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x1 | number | 是 | 确定贝塞尔曲线第一点横坐标。 取值范围：[0, 1] 说明：  设置的值小于0时，按0处理；设置的值大于1时，按1处理。 |
| y1 | number | 是 | 确定贝塞尔曲线第一点纵坐标。 取值范围：(-∞, +∞) |
| x2 | number | 是 | 确定贝塞尔曲线第二点横坐标。 取值范围：[0, 1] 说明：  设置的值小于0时，按0处理；设置的值大于1时，按1处理。 |
| y2 | number | 是 | 确定贝塞尔曲线第二点纵坐标。 取值范围：(-∞, +∞) |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ICurve | 曲线的插值对象。 |

**示例：**

```ets
import { curves } from '@kit.ArkUI';
curves.cubicBezierCurve(0.1, 0.0, 0.1, 1.0) // 创建一个三阶贝塞尔曲线
```

#### curves.springCurve9+

springCurve(velocity: number, mass: number, stiffness: number, damping: number): ICurve

构造弹簧曲线对象，曲线形状由弹簧参数决定，动画时长受animation、animateTo中的duration参数控制。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| velocity | number | 是 | 初始速度。是由外部因素对弹性动效产生的影响参数，其目的是保证对象从之前的运动状态平滑地过渡到弹性动效。该速度是归一化速度，其值等于动画开始时的实际速度除以动画属性改变值。 取值范围：(-∞, +∞) |
| mass | number | 是 | 质量。弹性系统的受力对象，会对弹性系统产生惯性影响。质量越大，震荡的幅度越大，恢复到平衡位置的速度越慢。 取值范围：(0, +∞) 说明：  设置的值小于等于0时，按1处理。 |
| stiffness | number | 是 | 刚度。是物体抵抗施加的力而形变的程度。在弹性系统中，刚度越大，抵抗变形的能力越强，恢复到平衡位置的速度就越快。 取值范围：(0, +∞) 说明：  设置的值小于等于0时，按1处理。 |
| damping | number | 是 | 阻尼。用于描述系统在受到扰动后震荡及衰减的情形。阻尼越大，弹性运动的震荡次数越少、震荡幅度越小。 取值范围：(0, +∞) 说明：  设置的值小于等于0时，按1处理。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ICurve | 曲线的插值对象。 |

**示例：**

```ets
import { curves } from '@kit.ArkUI';
curves.springCurve(10, 1, 228, 30) // 创建一个弹簧插值曲线
```

#### curves.springMotion9+

springMotion(response?: number, dampingFraction?: number, overlapDuration?: number): ICurve

构造弹性动画曲线对象。如果对同一对象的同一属性进行多个弹性动画，每个动画会替换掉前一个动画，并继承之前的速度。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| response | number | 否 | 弹簧自然振动周期，决定弹簧复位的速度。 默认值：0.55 单位：秒 取值范围：(0, +∞) 说明：  设置小于等于0的值时，按默认值0.55处理。 |
| dampingFraction | number | 否 | 阻尼系数。 0表示无阻尼，一直处于震荡状态； 大于0小于1的值为欠阻尼，运动过程中会超出目标值； 等于1为临界阻尼； 大于1为过阻尼，运动过程中逐渐趋于目标值。 默认值：0.825 单位：秒 取值范围：[0, +∞) 说明：  设置小于0的值时，按默认值0.825处理。 |
| overlapDuration | number | 否 | 弹性动画衔接时长。发生动画继承时，如果前后两个弹性动画response不一致，response参数会在overlapDuration时间内平滑过渡。 默认值：0 单位：秒 取值范围：[0, +∞)  说明：  设置小于0的值时，按默认值0处理。 弹性动画曲线为物理曲线，animation、animateTo、pageTransition中的duration参数不生效，动画持续时间取决于springMotion动画曲线参数和之前的速度。时间不能归一，故不能通过该曲线的interpolate函数获得插值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ICurve | 曲线对象。 说明:  弹性动画曲线为物理曲线，animation、animateTo、pageTransition中的duration参数不生效，动画持续时间取决于springMotion动画曲线参数和之前的速度。时间不能归一，故不能通过该曲线的interpolate函数获得插值。 |

**示例：**

```ets
import { curves } from '@kit.ArkUI'
curves.springMotion() // 创建一个默认弹性动画曲线
curves.springMotion(0.5) // 创建指定response、其余参数默认的弹性动画曲线
curves.springMotion(0.5, 0.6) // 创建指定response和dampingFraction、其余参数默认的弹性动画曲线
curves.springMotion(0.5, 0.6, 0) // 创建三个参数均自定义的弹性动画曲线
```

#### curves.responsiveSpringMotion9+

responsiveSpringMotion(response?: number, dampingFraction?: number, overlapDuration?: number): ICurve

构造弹性跟手动画曲线对象，是[springMotion](#ZH-CN_TOPIC_0000002522080738__curvesspringmotion9)的一种特例，仅默认参数不同，可与springMotion混合使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| response | number | 否 | 解释同springMotion中的response。 默认值：0.15 单位：秒 取值范围：(0, +∞) 说明：  设置小于等于0的值时，按默认值0.15处理。 |
| dampingFraction | number | 否 | 解释同springMotion中的dampingFraction。 默认值：0.86 单位：秒 取值范围：[0, +∞) 说明：  设置小于0的值时，按默认值0.86处理。 |
| overlapDuration | number | 否 | 解释同springMotion中的overlapDuration。 默认值：0.25 单位：秒 取值范围：[0, +∞) 说明：  设置小于0的值时，按默认值0.25处理。 弹性跟手动画曲线为springMotion的一种特例，仅默认值不同。如果使用自定义参数的弹性曲线，推荐使用springMotion构造曲线。如果使用跟手动画，推荐使用默认参数的弹性跟手动画曲线。 animation、animateTo、pageTransition中的duration参数不生效，动画持续时间取决于responsiveSpringMotion动画曲线参数和之前的速度，也不能通过该曲线的interpolate函数获得插值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ICurve | 曲线对象。 说明:  1、弹性跟手动画曲线为springMotion的一种特例，仅默认值不同。如果使用自定义参数的弹性曲线，推荐使用springMotion构造曲线；如果使用跟手动画，推荐使用默认参数的弹性跟手动画曲线。 2、animation、animateTo、pageTransition中的duration参数不生效，动画持续时间取决于responsiveSpringMotion动画曲线参数和之前的速度，也不能通过该曲线的interpolate函数获得插值。 |

**示例：**

```ets
import { curves } from '@kit.ArkUI'
curves.responsiveSpringMotion() // 创建一个默认弹性跟手动画曲线
```

#### curves.interpolatingSpring10+

interpolatingSpring(velocity: number, mass: number, stiffness: number, damping: number): ICurve

构造插值器弹簧曲线对象，生成一条从0到1的动画曲线，实际动画值根据曲线进行插值计算。动画时间由曲线参数决定，不受animation、animateTo中的duration参数控制。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| velocity | number | 是 | 初始速度。外部因素对弹性动效产生的影响参数，目的是保证对象从之前的运动状态平滑地过渡到弹性动效。该速度是归一化速度，其值等于动画开始时的实际速度除以动画属性改变值。 取值范围：(-∞, +∞) |
| mass | number | 是 | 质量。弹性系统的受力对象，会对弹性系统产生惯性影响。质量越大，震荡的幅度越大，恢复到平衡位置的速度越慢。 取值范围：(0, +∞) 说明：  设置的值小于等于0时，按1处理。 |
| stiffness | number | 是 | 刚度。表示物体抵抗施加的力而形变的程度。刚度越大，抵抗变形的能力越强，恢复到平衡位置的速度越快。 取值范围：(0, +∞) 说明：  设置的值小于等于0时，按1处理。 |
| damping | number | 是 | 阻尼。用于描述系统在受到扰动后震荡及衰减的情形。阻尼越大，弹性运动的震荡次数越少、震荡幅度越小。 取值范围：(0, +∞) 说明：  设置的值小于等于0时，按1处理。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ICurve | 曲线对象。 说明: 弹性动画曲线为物理曲线，animation、animateTo、pageTransition中的duration参数不生效，动画持续时间取决于interpolatingSpring动画曲线参数。时间不能归一，故不能通过该曲线的interpolate函数获得插值。 |

**示例：**

```ets
import { curves } from '@kit.ArkUI'
curves.interpolatingSpring(10, 1, 228, 30) // 创建一个时长由弹簧参数决定的弹簧插值曲线
```

#### curves.customCurve10+

customCurve(interpolate: (fraction: number) => number): ICurve

构造自定义曲线对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| interpolate | (fraction: number) => number | 是 | 用户自定义的插值回调函数。 fraction为动画开始时的插值输入x值。取值范围：[0,1] 返回值为曲线的y值。取值范围：[0,1] 说明： fraction等于0时，返回值为0对应动画起点，返回不为0，动画在起点处有跳变效果。 fraction等于1时，返回值为1对应动画终点，返回值不为1将导致动画的终值不是状态变量的值，出现大于或者小于状态变量值，再跳变到状态变量值的效果。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ICurve | 曲线的插值对象。 |

**示例：**

```ets
import { curves } from '@kit.ArkUI'
let interpolate = (fraction:number):number => {
  return Math.sqrt(fraction)
}
let curve = curves.customCurve(interpolate) // 创建一个用户自定义插值曲线
```

#### ICurve9+

曲线对象，支持通过本模块中的[curves.cubicBezierCurve](#ZH-CN_TOPIC_0000002522080738__curvescubicbeziercurve9)、[curves.interpolatingSpring](#ZH-CN_TOPIC_0000002522080738__curvesinterpolatingspring10)等方法创建不同类型的曲线对象，并可通过曲线对象调用其[interpolate](#ZH-CN_TOPIC_0000002522080738__interpolate9)的成员方法。

#### interpolate9+

interpolate(fraction: number): number

插值曲线的插值计算函数，可以通过传入的归一化时间参数返回当前的插值

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fraction | number | 是 | 当前的归一化时间参数。 取值范围：[0,1] 说明：  设置的值小于0时，按0处理；设置的值大于1时，按1处理。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回归一化time时间点对应的曲线插值。 |

**示例：**

```ets
import { curves } from '@kit.ArkUI'
let curveValue = curves.initCurve(Curve.EaseIn) // 创建一个默认先慢后快插值曲线
let value: number = curveValue.interpolate(0.5) // 计算得到时间到一半时的插值
```

#### curves.init(deprecated)

init(curve?: Curve): string

插值曲线的初始化函数，可以根据入参创建一个插值曲线对象。


从API version 7开始支持，从API version 9开始废弃。建议使用[Curves.initCurve](#ZH-CN_TOPIC_0000002522080738__curvesinitcurve9)替代。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| curve | Curve | 否 | 曲线类型。 默认值：Curve.Linear |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回插值曲线对象。 |

#### curves.steps(deprecated)

steps(count: number, end: boolean): string

构造阶梯曲线对象。


从API version 7开始支持，从API version 9开始废弃。建议使用[Curves. stepsCurve](#ZH-CN_TOPIC_0000002522080738__curvesstepscurve9)替代。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| count | number | 是 | 阶梯的数量，需要为正整数。 |
| end | boolean | 是 | 在每个间隔的起点或是终点发生阶跃变化。 -true：在终点发生阶跃变化。 -false：在起点发生阶跃变化。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回阶梯曲线对象。 |

#### curves.cubicBezier(deprecated)

cubicBezier(x1: number, y1: number, x2: number, y2: number): string

构造三阶贝塞尔曲线对象，曲线的值必须处于0-1之间。


从API version 7开始支持，从API version 9开始废弃。建议使用[Curves.cubicBezierCurve](#ZH-CN_TOPIC_0000002522080738__curvescubicbeziercurve9)替代。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x1 | number | 是 | 确定贝塞尔曲线第一点横坐标。 |
| y1 | number | 是 | 确定贝塞尔曲线第一点纵坐标。 |
| x2 | number | 是 | 确定贝塞尔曲线第二点横坐标。 |
| y2 | number | 是 | 确定贝塞尔曲线第二点纵坐标。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回三阶贝塞尔曲线对象。 |

#### curves.spring(deprecated)

spring(velocity: number, mass: number, stiffness: number, damping: number): string

构造弹簧曲线对象。


从API version 7开始支持，从API version 9开始废弃。建议使用[Curves.springCurve](#ZH-CN_TOPIC_0000002522080738__curvesspringcurve9)替代。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| velocity | number | 是 | 初始速度。是由外部因素对弹性动效产生的影响参数，其目的是保证对象从之前的运动状态平滑地过渡到弹性动效。 |
| mass | number | 是 | 质量。弹性系统的受力对象，会对弹性系统产生惯性影响。质量越大，震荡的幅度越大，恢复到平衡位置的速度越慢。 |
| stiffness | number | 是 | 刚度。是物体抵抗施加的力而形变的程度。在弹性系统中，刚度越大，抵抗变形的能力越强，恢复到平衡位置的速度就越快。 |
| damping | number | 是 | 阻尼。是一个纯数，无真实的物理意义，用于描述系统在受到扰动后震荡及衰减的情形。阻尼越大，弹性运动的震荡次数越少、震荡幅度越小。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回弹簧曲线对象。 |

#### 整体示例

```ets
// xxx.ets
import { curves } from '@kit.ArkUI';

@Entry
@Component
struct ImageComponent {
  @State widthSize: number = 200;
  @State heightSize: number = 200;

  build() {
    Column() {
      Text()
        .margin({ top: 100 })
        .width(this.widthSize)
        .height(this.heightSize)
        .backgroundColor(Color.Red)
        .onClick(() => {
          let curve = curves.cubicBezierCurve(0.25, 0.1, 0.25, 1.0);
          this.widthSize = curve.interpolate(0.5) * this.widthSize;
          this.heightSize = curve.interpolate(0.5) * this.heightSize;
        })
        .animation({ duration: 2000, curve: curves.stepsCurve(9, true) })
    }.width("100%").height("100%")
  }
```

![image](public_sys-resources/zh-cn_image_0000002522244688.webp)