# 关键帧动画 (keyframeAnimateTo)

在[UIContext](Class (UIContext).md)中提供keyframeAnimateTo接口来指定若干个关键帧状态，实现分段的动画。同属性动画，布局类改变宽高的动画，内容都是直接到终点状态，例如文字、[Canvas](Canvas.md)的内容等，如果要内容跟随宽高变化，可以使用[renderFit](组件内容填充方式.md)属性配置。

 从API version 11开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

 该接口为[UIContext](Class (UIContext).md)类的成员函数，需要通过UIContext实例对象调用。

keyframeAnimateTo(param: KeyframeAnimateParam, keyframes: Array<KeyframeState>): void

设置关键帧动画。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明param[KeyframeAnimateParam](#ZH-CN_TOPIC_0000002529284921__keyframeanimateparam对象说明)是关键帧动画的整体动画参数。keyframesArray<[KeyframeState](#ZH-CN_TOPIC_0000002529284921__keyframestate对象说明)>是所有的关键帧状态。

#### KeyframeAnimateParam对象说明

动画选项设置。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明delaynumber否是

动画的整体延时时间，单位为ms（毫秒），默认不延时播放。

默认值：0

**说明：**

 delay>=0为延迟播放，delay<0表示提前播放。对于delay<0的情况：当delay的绝对值小于实际动画时长，动画将在开始后第一帧直接运动到delay绝对值的时刻的状态；当delay的绝对值大于等于实际动画时长，动画将在开始后第一帧直接运动到终点状态。其中实际动画时长等于单次动画时长乘以动画播放次数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

iterationsnumber否是

动画播放次数。默认播放一次，设置为-1时表示无限次播放。设置为0时表示无动画效果。

默认值：1

**取值范围：**[-1, +∞)

**说明：**

- 设置浮点型类型的值时，向下取整。例如，设置值为1.2，按照1处理。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

onFinish() => void否是

动画播放完成回调。当keyframe动画所有次数播放完成后调用。在设置的开发者选项中关闭过渡动画，或UIAbility从前台切换至后台时会立即结束仍在步进中的有限循环keyframe动画，触发播放完成回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

expectedFrameRateRange19+[ExpectedFrameRateRange](显式动画 (animateTo).md#ZH-CN_TOPIC_0000002497444950__expectedframeraterange11)否是

设置动画的期望帧率。

**默认值：**{min:0, max:0, expected:0}，即跟随应用帧率。

**说明：**

开发者通过设置有效的期望帧率后，系统会收集设置的请求帧率，进行决策和分发，在渲染管线上进行分频，尽量能够满足开发者的期望帧率。开发者设置的期望帧率值不能代表最终实际效果，会受限于系统能力和屏幕刷新率。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

#### KeyframeState对象说明

设置关键帧选项。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

名称类型只读可选说明durationnumber否否

该段关键帧动画的持续时间，单位为毫秒。

取值范围：[0, +∞)

**说明：**

- 设置小于0的值时按0处理。

- 设置浮点型类型的值时，向下取整。例如，设置值为1.2，按照1处理。

curve[Curve](枚举说明.md#ZH-CN_TOPIC_0000002529284967__curve)| string | [ICurve](显式动画 (animateTo).md#ZH-CN_TOPIC_0000002497444950__icurve9)否是

该关键帧使用的动画曲线。

推荐以Curve或ICurve形式指定。

当类型为string时，为动画插值曲线，取值参考[AnimateParam](显式动画 (animateTo).md#ZH-CN_TOPIC_0000002497444950__animateparam对象说明)的curve参数。

默认值：Curve.EaseInOut

**说明：**

由于[springMotion](@ohos.curves (插值计算).md#ZH-CN_TOPIC_0000002497604788__curvesspringmotion9)、[responsiveSpringMotion](@ohos.curves (插值计算).md#ZH-CN_TOPIC_0000002497604788__curvesresponsivespringmotion9)、[interpolatingSpring](@ohos.curves (插值计算).md#ZH-CN_TOPIC_0000002497604788__curvesinterpolatingspring10)曲线时长不生效，故不支持这三种曲线。

event() => void否否指定在该关键帧时刻状态的闭包函数，即在该关键帧时刻要达到的状态。

#### 示例

该示例主要演示如何通过keyframeAnimateTo来设置关键帧动画。

```ets
// xxx.ets
import { UIContext } from '@kit.ArkUI';

@Entry
@Component
struct KeyframeDemo {
  @State myScale: number = 1.0;
  uiContext: UIContext | undefined = undefined;

  aboutToAppear() {
    this.uiContext = this.getUIContext?.();
  }

  build() {
    Column() {
      Circle()
        .width(100)
        .height(100)
        .fill("#46B1E3")
        .margin(100)
        .scale({ x: this.myScale, y: this.myScale })
        .onClick(() => {
          if (!this.uiContext) {
            console.info("no uiContext, keyframe failed");
            return;
          }
          this.myScale = 1;
          // 设置关键帧动画整体播放3次
          this.uiContext.keyframeAnimateTo({
              iterations: 3,
              expectedFrameRateRange: {
                min: 10,
                max: 120,
                expected: 60,
              }
            }, [
            {
              // 第一段关键帧动画时长为800ms，scale属性做从1到1.5的动画
              duration: 800,
              event: () => {
                this.myScale = 1.5;
              }
            },
            {
              // 第二段关键帧动画时长为500ms，scale属性做从1.5到1的动画
              duration: 500,
              event: () => {
                this.myScale = 1;
              }
            }
          ]);
        })
    }.width('100%').margin({ top: 5 })
  }
}
```