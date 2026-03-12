# 属性动画 (animation)

组件的某些通用属性变化时，可以通过属性动画实现渐变过渡效果，提升用户体验。支持的属性包括[width](尺寸设置.md#ZH-CN_TOPIC_0000002497444850__width)、[height](尺寸设置.md#ZH-CN_TOPIC_0000002497444850__height)、[backgroundColor](背景设置.md#ZH-CN_TOPIC_0000002529444791__backgroundcolor)、[opacity](透明度设置.md#ZH-CN_TOPIC_0000002529444799__opacity)、[scale](图形变换.md#ZH-CN_TOPIC_0000002497604834__scale)、[rotate](图形变换.md#ZH-CN_TOPIC_0000002497604834__rotate)、[translate](图形变换.md#ZH-CN_TOPIC_0000002497604834__translate)等。对于改变布局类属性（如宽高）的动画，内容通常会直接跳转到最终状态，例如文字或[Canvas](Canvas.md)中的内容。如果希望内容跟随宽高变化，可以使用[renderFit](组件内容填充方式.md#ZH-CN_TOPIC_0000002497604840__renderfit)属性进行配置。

从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

#### animation

animation(value:AnimateParam): T

设置组件的属性动画。

-

在单一页面上存在大量应用动效的组件时，可以使用[renderGroup](图像效果.md#ZH-CN_TOPIC_0000002497444856__rendergroup10)方法来解决卡顿问题，从而提升动画性能。最佳实践请参考[动画使用指导-使用renderGroup](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-fair-use-animation#section1223162922415)。

-

该接口不支持在[attributeModifier](动态属性设置.md#ZH-CN_TOPIC_0000002529284843__attributemodifier)中调用。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明value[AnimateParam](显式动画 (animateTo).md#ZH-CN_TOPIC_0000002497444950__animateparam对象说明)是设置动画效果相关参数。

**返回值：**

类型说明T返回当前组件。

属性动画只对写在animation前面的属性生效，且对组件构造器的属性不生效。

```ets
@Entry
@Component
struct AnimationExample {
  @State widthSize: number = 250;
  @State heightSize: number = 100;
  @State rotateAngle: number = 0;
  @State flag: boolean = true;
  @State space: number = 10;

  build() {
    Column() {
      Column({ space: this.space }) // 改变Column构造器中的space动画不生效
        .onClick(() => {
          if (this.flag) {
            this.widthSize = 150;
            this.heightSize = 60;
            this.space = 20; // 改变this.space动画不生效
          } else {
            this.widthSize = 250;
            this.heightSize = 100;
            this.space = 10; // 改变this.space动画不生效
          }
          this.flag = !this.flag;
        })
        .backgroundColor(Color.Black)
        .margin(30)
        .width(this.widthSize) // 只有写在animation前面才生效
        .height(this.heightSize) // 只有写在animation前面才生效
        .animation({
          duration: 2000,
          curve: Curve.EaseOut,
          iterations: 3,
          playMode: PlayMode.Normal
        })
        // .width(this.widthSize) // 动画不生效
        // .height(this.heightSize) // 动画不生效
    }
  }
}
```

#### 示例

该示例通过animation实现了组件的属性动画。

```ets
// xxx.ets
@Entry
@Component
struct AttrAnimationExample {
  @State widthSize: number = 250
  @State heightSize: number = 100
  @State rotateAngle: number = 0
  @State flag: boolean = true

  build() {
    Column() {
      Button('change size')
        .onClick(() => {
          if (this.flag) {
            this.widthSize = 150
            this.heightSize = 60
          } else {
            this.widthSize = 250
            this.heightSize = 100
          }
          this.flag = !this.flag
        })
        .margin(30)
        .width(this.widthSize)
        .height(this.heightSize)
        .animation({
          duration: 2000,
          curve: Curve.EaseOut,
          iterations: 3,
          playMode: PlayMode.Normal
        })
      Button('change rotate angle')
        .onClick(() => {
          this.rotateAngle = 90
        })
        .margin(50)
        .rotate({ angle: this.rotateAngle })
        .animation({
          duration: 1200,
          curve: Curve.Friction,
          delay: 500,
          iterations: -1, // 设置-1表示动画无限循环
          playMode: PlayMode.Alternate,
          expectedFrameRateRange: {
            min: 20,
            max: 120,
            expected: 90,
          }
        })
    }.width('100%').margin({ top: 20 })
  }
}
```