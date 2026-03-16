# CanvasGradient

渐变对象。

 从 API version 8 开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

#### addColorStop

addColorStop(offset: number, color: string): void

设置渐变断点值，包括偏移和颜色。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明offsetnumber是

设置渐变点距离起点的位置占总体长度的比例，范围为[0, 1]。

设置offset<0或offset>1无渐变效果。

异常值undefined和null按无效值处理，NaN和Infinity会导致CanvasGradient异常。

colorstring是

设置渐变的颜色。颜色格式参考[ResourceColor](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)中string类型说明。

未按格式设置颜色无渐变效果。

**示例：**

通过addColorStop设置渐变断点值，包括偏移和颜色。支持设置rgb或者argb格式颜色。

```ets
// xxx.ets
@Entry
@Component
struct AddColorStop {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('rgb(213,213,213)')
        .onReady(() => {
          let grad = this.context.createLinearGradient(50, 0, 300, 100)
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

#### addColorStop20+

addColorStop(offset: number, color: string | ColorMetrics): void

设置渐变断点值，包括偏移和颜色。支持设置rgb或者argb格式颜色。支持通过传入[ColorMetrics](Graphics.md#ZH-CN_TOPIC_0000002529444761__colormetrics12)类型设置P3色域颜色值，可在支持高色域的设备上获得更丰富的色彩表现。

**卡片能力：** 从API version 20开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明offsetnumber是

设置渐变点距离起点的位置占总体长度的比例，范围为[0, 1]。

设置offset<0或offset>1无渐变效果。

异常值undefined和null按无效值处理，NaN和Infinity会导致CanvasGradient异常。

colorstring | [ColorMetrics](Graphics.md#ZH-CN_TOPIC_0000002529444761__colormetrics12)是

设置渐变填充的颜色。

可以使用[colorWithSpace](Graphics.md#ZH-CN_TOPIC_0000002529444761__colorwithspace20)方法构造指定色域属性[ColorSpace](../../guides/枚举说明.md#ZH-CN_TOPIC_0000002529284967__colorspace20)为SRGB或DISPLAY_P3的颜色。每个渐变ColorMetrics的色域属性应当统一，设置不同色域的属性时将抛出异常，错误码：103701。

设置null和undefined无效。

**错误码：**

以下错误码的详细介绍请参见[Canvas组件错误码](../../errors/Canvas组件错误码.md)。

错误码ID错误信息103701The color's ColorSpace is not the same as the last color's.

仅[CanvasRenderingContext2D](../components/CanvasRenderingContext2D.md)对象的[fillStyle](../components/CanvasRenderingContext2D.md#ZH-CN_TOPIC_0000002497444936__fillstyle)和[strokeStyle](../components/CanvasRenderingContext2D.md#ZH-CN_TOPIC_0000002497444936__strokestyle)属性支持设置P3广色域的CanvasGradient对象，且需要将Canvas组件所在窗口的色域模式通过[setWindowColorSpace](../../types/interfaces/Interface (Window).md#ZH-CN_TOPIC_0000002497604802__setwindowcolorspace9)方法设置为广色域模式WIDE_GAMUT。

**示例：**

通过addColorStop设置指定色域的渐变断点值，包括偏移和颜色。设置窗口色域模式为广色域参照方法[setWindowColorSpace](../../types/interfaces/Interface (Window).md#ZH-CN_TOPIC_0000002497604802__setwindowcolorspace9)。

```ets
// xxx.ets
import { BusinessError } from '@kit.BasicServicesKit';
import { ColorMetrics } from '@kit.ArkUI'

@Entry
@Component
struct AddColorStop {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .onReady(() => {
          // 设置fillStyle为SRGB色域效果的gradient
          let gradSRGB = this.context.createLinearGradient(85, 10, 160, 110)
          // 使用try catch对可能出现的异常进行捕获
          try {
            gradSRGB.addColorStop(0.0, ColorMetrics.colorWithSpace(ColorSpace.SRGB, 1.0, 0.0, 0.0, 1.0))
            gradSRGB.addColorStop(0.5, ColorMetrics.colorWithSpace(ColorSpace.SRGB, 1.0, 1.0, 1.0, 1.0))
            gradSRGB.addColorStop(1.0, ColorMetrics.colorWithSpace(ColorSpace.SRGB, 0.0, 1.0, 0.0, 1.0))
          } catch (error) {
            let e: BusinessError = error as BusinessError;
            console.error(`Failed to addColorStop. Code: ${e.code}, message: ${e.message}`);
          }
          this.context.fillStyle = gradSRGB
          this.context.fillRect(10, 10, 150, 150)

          // 设置fillStyle为DISPLAY_P3色域效果的gradient
          let gradP3 = this.context.createLinearGradient(245, 10, 320, 110)
          // 使用try catch对可能出现的异常进行捕获
          try {
            gradP3.addColorStop(0.0, ColorMetrics.colorWithSpace(ColorSpace.DISPLAY_P3, 1.0, 0.0, 0.0, 1.0))
            gradP3.addColorStop(0.5, ColorMetrics.colorWithSpace(ColorSpace.DISPLAY_P3, 1.0, 1.0, 1.0, 1.0))
            gradP3.addColorStop(1.0, ColorMetrics.colorWithSpace(ColorSpace.DISPLAY_P3, 0.0, 1.0, 0.0, 1.0))
          } catch (error) {
            let e: BusinessError = error as BusinessError;
            console.error(`Failed to addColorStop. Code: ${e.code}, message: ${e.message}`);
          }
          this.context.fillStyle = gradP3
          this.context.fillRect(170, 10, 150, 150)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```