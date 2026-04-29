# Ellipse

椭圆绘制组件。

  ![image](public_sys-resources/note_3.0-zh-cn.webp)

 该组件从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

**子组件**

无

**接口**

Ellipse(options?: EllipseOptions)

卡片能力： 从API version 9开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | EllipseOptions | 否 | 椭圆绘制尺寸。  异常值undefined和null按照无效值处理。 |

**EllipseOptions18+对象说明**

用于描述Ellipse组件绘制属性。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

为规范匿名对象的定义，API 18版本修改了此处的元素定义。其中，保留了历史匿名对象的起始版本信息，会出现外层元素@since版本号高于内层元素版本号的情况，但这不影响接口的使用。

卡片能力： 从API version 18开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 18开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| width7+ | Length | 否 | 是 | 宽度，取值范围≥0。 默认值：0 默认单位：vp 异常值undefined、null、NaN和Infinity按照默认值处理。 从API version 20开始，支持Resource类型。 卡片能力： 从API version 9开始，该接口支持在ArkTS卡片中使用。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| height7+ | Length | 否 | 是 | 高度，取值范围≥0。 默认值：0 默认单位：vp 异常值undefined、null、NaN和Infinity按照默认值处理。 从API version 20开始，支持Resource类型。 卡片能力： 从API version 9开始，该接口支持在ArkTS卡片中使用。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |

**属性**

除支持[通用属性](通用属性.md)外，还支持以下属性：

**fill**

fill(value: ResourceColor)

设置填充区域的颜色，支持[attributeModifier](动态属性设置.md#ZH-CN_TOPIC_0000002522240800__attributemodifier)动态设置属性方法，异常值按照默认值处理。与通用属性foregroundColor同时设置时，后设置的属性生效。

卡片能力： 从API version 9开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | ResourceColor | 是 | 填充区域颜色。 默认值：Color.Black  异常值undefined、null、NaN和Infinity按照默认值处理。 |

**fillOpacity**

fillOpacity(value: number | string | Resource)

设置填充区域透明度，支持[attributeModifier](动态属性设置.md#ZH-CN_TOPIC_0000002522240800__attributemodifier)动态设置属性方法。

卡片能力： 从API version 9开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | string | Resource | 是 | 填充区域透明度。 说明： number格式取值范围是[0.0, 1.0]，若给定值小于0.0，则取值为0.0；若给定值大于1.0，则取值为1.0，其余异常值按1.0处理。 string格式支持number格式取值的字符串形式，取值范围与number格式相同。 Resource格式支持系统资源或者应用资源中的字符串，取值范围和number格式相同。 异常值NaN按0.0处理，undefined、null和Infinity按1.0处理。 默认值：1.0 |

**stroke**

stroke(value: ResourceColor)

设置边框颜色，支持[attributeModifier](动态属性设置.md#ZH-CN_TOPIC_0000002522240800__attributemodifier)动态设置属性方法，不设置时，默认边框透明度为0，即没有边框。

卡片能力： 从API version 9开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | ResourceColor | 是 | 边框颜色。 异常值undefined和null按照默认值处理，NaN和Infinity按照Color.Black处理。 |

**strokeDashArray**

strokeDashArray(value: Array<any>)

设置边框间隙，支持[attributeModifier](动态属性设置.md#ZH-CN_TOPIC_0000002522240800__attributemodifier)动态设置属性方法。取值范围应为≥0，异常值按照默认值处理。

卡片能力： 从API version 9开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Array<any> | 是 | 定义Ellipse轮廓的虚线模式的数组，数组元素交替表示线段长度和间隙长度。 默认值：[]（空数组） 默认单位：vp  异常值undefined和null按照默认值处理。 说明： 空数组：实线 偶数多元素数组：数组元素按顺序循环，如[a, b, c, d]表示线段长度a->间隙长度b->线段长度c->间隙长度d->线段长度a->... 奇数多元素数组：重复一次该数组元素，按偶数多元素数组的规则顺序循环，如[a, b, c]等效于[a, b, c, a, b, c]，表示线段长度a->间隙长度b->线段长度c->间隙长度a->线段长度b->间隙长度c->线段长度a->... |

**strokeDashOffset**

strokeDashOffset(value: number | string)

设置边框绘制起点的偏移量，支持[attributeModifier](动态属性设置.md#ZH-CN_TOPIC_0000002522240800__attributemodifier)动态设置属性方法。

卡片能力： 从API version 9开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | string | 是 | 边框绘制起点的偏移量。 默认值：0 默认单位：vp  异常值undefined和null按照默认值处理，NaN和Infinity会导致strokeDashArray失效。 |

**strokeLineCap**

strokeLineCap(value: LineCapStyle)

设置边框端点绘制样式，支持[attributeModifier](动态属性设置.md#ZH-CN_TOPIC_0000002522240800__attributemodifier)动态设置属性方法。

卡片能力： 从API version 9开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | LineCapStyle | 是 | 边框端点绘制样式。 默认值：LineCapStyle.Butt  异常值undefined、null、NaN和Infinity按照默认值处理。 |

**strokeLineJoin**

strokeLineJoin(value: LineJoinStyle)

设置边框拐角绘制样式，支持[attributeModifier](动态属性设置.md#ZH-CN_TOPIC_0000002522240800__attributemodifier)动态设置属性方法。Ellipse组件无法形成拐角，该属性设置无效。

卡片能力： 从API version 9开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | LineJoinStyle | 是 | 边框拐角绘制样式。 默认值：LineJoinStyle.Miter  异常值undefined、null、NaN和Infinity按照默认值处理。 |

**strokeMiterLimit**

strokeMiterLimit(value: number | string)

设置斜接长度与边框宽度比值的极限值，支持[attributeModifier](动态属性设置.md#ZH-CN_TOPIC_0000002522240800__attributemodifier)动态设置属性方法。Ellipse组件不支持设置尖角图形，该属性设置无效。

卡片能力： 从API version 9开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | string | 是 | 斜接长度与边框宽度比值的极限值。 默认值：4  异常值undefined、null和NaN按照默认值处理，Infinity会导致stroke失效。 |

**strokeOpacity**

strokeOpacity(value: number | string | Resource)

设置边框透明度，支持[attributeModifier](动态属性设置.md#ZH-CN_TOPIC_0000002522240800__attributemodifier)动态设置属性方法。该属性的取值范围是[0.0, 1.0]，若给定值小于0.0，则取值为0.0；若给定值大于1.0，则取值为1.0。

卡片能力： 从API version 9开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | string | Resource | 是 | 边框透明度。 默认值：stroke接口设置的透明度。 异常值NaN按0.0处理，undefined、null和Infinity按1.0处理。 |

**strokeWidth**

strokeWidth(value: Length)

设置边框宽度，支持[attributeModifier](动态属性设置.md#ZH-CN_TOPIC_0000002522240800__attributemodifier)动态设置属性方法。该属性若为string类型，暂不支持百分比，百分比按照1px处理。

卡片能力： 从API version 9开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Length | 是 | 边框宽度，取值范围≥0。 默认值：1 默认单位：vp 异常值undefined、null和NaN按照默认值处理，Infinity按0处理。 |

**antiAlias**

antiAlias(value: boolean)

设置是否开启抗锯齿效果，支持[attributeModifier](动态属性设置.md#ZH-CN_TOPIC_0000002522240800__attributemodifier)动态设置属性方法。

卡片能力： 从API version 9开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 是否开启抗锯齿效果。 true：开启抗锯齿；false：关闭抗锯齿。 默认值：true  异常值undefined和null按照默认值处理。 |

**示例**

**示例1（组件属性绘制）**

通过fillOpacity、stroke属性分别绘制椭圆的透明度、边框颜色。

```ets
// xxx.ets
@Entry
@Component
struct EllipseExample {
  build() {
    Column({ space: 10 }) {
      // 绘制一个 150 * 80 的椭圆
      Ellipse({ width: 150, height: 80 })
      // 绘制一个 150 * 100 、线条为蓝色的椭圆环
      Ellipse()
        .width(150)
        .height(100)
        .fillOpacity(0)
        .stroke(Color.Blue)
        .strokeWidth(3)
    }.width('100%')
  }
```

![image](public_sys-resources/zh-cn_image_0000002553365191.webp)

**示例2（宽和高使用不同参数类型绘制椭圆）**

width、height属性分别使用不同的长度类型绘制椭圆。

```ets
// xxx.ets
@Entry
@Component
struct EllipseTypeExample {
  build() {
    Column({ space: 10 }) {
      // 绘制一个 150 * 80 的椭圆
      Ellipse({ width: '150', height: '80' }) // 使用string类型
      // 绘制一个 80 * 150 的椭圆
      Ellipse({ width: 80, height: 150 }) // 使用number类型
      // 绘制一个 150 * 150 的椭圆
      Ellipse({ width: $r('app.string.EllipseWidth'), height: $r('app.string.EllipseHeight') }) // 使用Resource类型，需用户自定义
    }.width('100%')
  }
```

![image](public_sys-resources/zh-cn_image_0000002522245268.webp)

**示例3（使用attributeModifier动态设置Ellipse组件的属性）**

以下示例展示了如何使用attributeModifier动态设置Ellipse组件的fill、fillOpacity、stroke、strokeDashArray、strokeDashOffset、strokeLineCap、strokeOpacity、strokeWidth和antiAlias属性。

```ets
// xxx.ets
class MyEllipseModifier implements AttributeModifier<EllipseAttribute> {
  applyNormalAttribute(instance: EllipseAttribute): void {
    // 填充颜色#707070，填充透明度0.5，边框颜色#2787D9，边框间隙[20]，向左偏移15，线条两端样式为半圆，边框透明度0.5，边框宽度10，抗锯齿开启
    instance.fill("#707070")
    instance.fillOpacity(0.5)
    instance.stroke("#2787D9")
    instance.strokeDashArray([20])
    instance.strokeDashOffset("15")
    instance.strokeLineCap(LineCapStyle.Round)
    instance.strokeOpacity(0.5)
    instance.strokeWidth(10)
    instance.antiAlias(true)
  }

@Entry
@Component
struct EllipseModifierDemo {
  @State modifier: MyEllipseModifier = new MyEllipseModifier()

  build() {
    Column() {
      Ellipse({ width: 150, height: 80 })
        .attributeModifier(this.modifier)
        .offset({ x: 20, y: 20 })
    }
```

![image](public_sys-resources/zh-cn_image_0000002553205231.webp)