# @ohos.animator (动画)

本模块提供组件动画效果，包括定义动画、启动动画和以相反的顺序播放动画等。

-

本模块首批接口从API version 6开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

-

本模块从API version 9开始支持在ArkTS中使用。

-

该模块不支持在[UIAbility](@ohos.app.ability.UIAbility (带界面的应用组件).md)的文件声明处使用，即不能在UIAbility的生命周期中调用，需要在创建组件实例后使用。

-

本模块功能依赖UI的执行上下文，不可在[UI上下文不明确](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-global-interface#ui上下文不明确)的地方使用，参见[UIContext](../../types/classes/Class (UIContext).md)说明。

-

自定义组件中一般会持有一个[create](#ZH-CN_TOPIC_0000002497604768__create18)接口返回的[AnimatorResult](#ZH-CN_TOPIC_0000002497604768__animatorresult)对象，以保证动画对象不在动画过程中析构，而这个对象也通过回调捕获了自定义组件对象。则需要在自定义组件销毁时的[aboutToDisappear](../../topics/misc/自定义组件的生命周期.md#ZH-CN_TOPIC_0000002529444913__abouttodisappear)中释放动画对象，来避免因为循环依赖导致内存泄漏，详细示例可参考：[基于ArkTS扩展的声明式开发范式](#ZH-CN_TOPIC_0000002497604768__基于arkts扩展的声明式开发范式)。

-

Animator对象析构或主动调用[cancel](#ZH-CN_TOPIC_0000002497604768__cancel)、[finish](#ZH-CN_TOPIC_0000002497604768__finish)都会有一次额外的[onFrame](#ZH-CN_TOPIC_0000002497604768__属性)，返回值是动画终点的值。所以如果在动画过程中调用[cancel](#ZH-CN_TOPIC_0000002497604768__cancel)、[finish](#ZH-CN_TOPIC_0000002497604768__finish)会一帧跳变到终点，如果希望在中途停止，可以先将onFrame设置为空函数，再调用[finish](#ZH-CN_TOPIC_0000002497604768__finish)。

-

无限循环的Animator动画，当开发者选项设置全局动画速率为0（关闭动画）时，仍执行循环动画。

#### 导入模块

```ets
import { Animator as animator, AnimatorOptions, AnimatorResult, SimpleAnimatorOptions } from '@kit.ArkUI';
```

#### Animator

定义Animator类。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

#### create(deprecated)

create(options: AnimatorOptions): AnimatorResult

创建animator动画结果对象（AnimatorResult）。

-

从API version 9开始支持，从API version 18开始废弃，建议使用[createAnimator](../../types/classes/Class (UIContext).md#ZH-CN_TOPIC_0000002529444749__createanimator)替代。

-

从API version 10开始，可以通过使用[UIContext](../../types/classes/Class (UIContext).md)中的[createAnimator](../../types/classes/Class (UIContext).md#ZH-CN_TOPIC_0000002529444749__createanimator)来明确UI的执行上下文。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明options[AnimatorOptions](#ZH-CN_TOPIC_0000002497604768__animatoroptions)是定义动画选项。

**返回值：**

类型说明[AnimatorResult](#ZH-CN_TOPIC_0000002497604768__animatorresult)Animator结果接口。

**错误码**：

以下错误码详细介绍请参考[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed.

**示例：**

完整示例请参考[基于ArkTS扩展的声明式开发范式](#ZH-CN_TOPIC_0000002497604768__基于arkts扩展的声明式开发范式)。

推荐通过使用[UIContext](../../types/classes/Class (UIContext).md)中的[createAnimator](../../types/classes/Class (UIContext).md#ZH-CN_TOPIC_0000002529444749__createanimator)接口明确UI上下文。

```ets
import { Animator as animator, AnimatorOptions } from '@kit.ArkUI';

let options: AnimatorOptions = {
  duration: 1500,
  easing: "friction",
  delay: 0,
  fill: "forwards",
  direction: "normal",
  iterations: 3,
  begin: 200.0,
  end: 400.0
};
animator.create(options); // 建议使用 UIContext.createAnimator()接口
```

#### create18+

create(options: AnimatorOptions | SimpleAnimatorOptions): AnimatorResult

创建animator动画结果对象（AnimatorResult）。与[create](#ZH-CN_TOPIC_0000002497604768__createdeprecated)相比，新增对[SimpleAnimatorOptions](#ZH-CN_TOPIC_0000002497604768__simpleanimatoroptions18)类型入参的支持。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明options[AnimatorOptions](#ZH-CN_TOPIC_0000002497604768__animatoroptions) | [SimpleAnimatorOptions](#ZH-CN_TOPIC_0000002497604768__simpleanimatoroptions18)是定义动画参数选项。

**返回值：**

类型说明[AnimatorResult](#ZH-CN_TOPIC_0000002497604768__animatorresult)Animator结果接口。

**错误码**：

以下错误码详细介绍请参考[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed.

**示例：**

完整示例请参考[基于ArkTS扩展的声明式开发范式](#ZH-CN_TOPIC_0000002497604768__基于arkts扩展的声明式开发范式)。

推荐通过使用[UIContext](../../types/classes/Class (UIContext).md)中的[createAnimator](../../types/classes/Class (UIContext).md#ZH-CN_TOPIC_0000002529444749__createanimator)接口明确UI上下文。

```ets
import { Animator as animator, SimpleAnimatorOptions } from '@kit.ArkUI';
let options: SimpleAnimatorOptions = new SimpleAnimatorOptions(100, 200).duration(2000);
animator.create(options);// 建议使用 UIContext.createAnimator()接口
```

#### createAnimator(deprecated)

createAnimator(options: AnimatorOptions): AnimatorResult

创建动画

从API version 6开始支持，从API version 9开始废弃，建议使用[create](#ZH-CN_TOPIC_0000002497604768__createdeprecated)替代。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明options[AnimatorOptions](#ZH-CN_TOPIC_0000002497604768__animatoroptions)是定义动画选项。

**返回值：**

类型说明[AnimatorResult](#ZH-CN_TOPIC_0000002497604768__animatorresult)Animator结果接口。

**示例：**

完整示例请参考[基于ArkTS扩展的声明式开发范式](#ZH-CN_TOPIC_0000002497604768__基于arkts扩展的声明式开发范式)。

```ets
import { Animator as animator } from '@kit.ArkUI';

let options: AnimatorOptions = {
  // xxx.js文件中不需要强调显式类型AnimatorOptions
  duration: 1500,
  easing: "friction",
  delay: 0,
  fill: "forwards",
  direction: "normal",
  iterations: 3,
  begin: 200.0,
  end: 400.0,
};
this.animator = animator.createAnimator(options);
```

#### AnimatorResult

定义Animator结果接口。

#### 属性

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明onFrame12+(progress: number) => void否否

接收到帧时回调。

progress表示动画的当前值。取值范围为[AnimatorOptions](#ZH-CN_TOPIC_0000002497604768__animatoroptions)定义的[begin, end]，默认取值范围为[0, 1]。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

onFinish12+() => void否否

动画完成时回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

onCancel12+() => void否否

动画被取消时回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

onRepeat12+() => void否否

动画重复时回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

onframe(deprecated)(progress: number) => void否否

接收到帧时回调。

**说明:** 从API version 6开始支持，从API version 12开始废弃，推荐使用onFrame。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

onfinish(deprecated)() => void否否

动画完成时回调。

**说明:** 从API version 6开始支持，从API version 12开始废弃，推荐使用onFinish。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

oncancel(deprecated)() => void否否

动画被取消时回调。

**说明:** 从API version 6开始支持，从API version 12开始废弃，推荐使用onCancel。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

onrepeat(deprecated)() => void否否

动画重复时回调。

**说明:** 从API version 6开始支持，从API version 12开始废弃，推荐使用onRepeat。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

#### reset9+

reset(options: AnimatorOptions): void

重置当前animator动画参数。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明options[AnimatorOptions](#ZH-CN_TOPIC_0000002497604768__animatoroptions)是定义动画选项。

**错误码：**

以下错误码的详细介绍请参考[通用错误码](../../errors/通用错误码.md)和[接口调用异常错误码](../../errors/接口调用异常错误码.md)

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed.100001The specified page is not found or the object property list is not obtained.

**示例：**

```ets
import { AnimatorResult } from '@kit.ArkUI';

@Entry
@Component
struct AnimatorTest {
  private animatorResult: AnimatorResult | undefined = undefined;

  create() {
    this.animatorResult = this.getUIContext().createAnimator({
      duration: 1500,
      easing: "friction",
      delay: 0,
      fill: "forwards",
      direction: "normal",
      iterations: 3,
      begin: 200.0,
      end: 400.0
    })
    this.animatorResult.reset({
      duration: 1500,
      easing: "friction",
      delay: 0,
      fill: "forwards",
      direction: "normal",
      iterations: 5,
      begin: 200.0,
      end: 400.0
    });
  }

  build() {
    // ......
  }
}
```

#### reset18+

reset(options: AnimatorOptions | SimpleAnimatorOptions): void

重置当前animator动画参数。与[reset](#ZH-CN_TOPIC_0000002497604768__reset9)相比，新增对[SimpleAnimatorOptions](#ZH-CN_TOPIC_0000002497604768__simpleanimatoroptions18)类型入参的支持。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明options[AnimatorOptions](#ZH-CN_TOPIC_0000002497604768__animatoroptions) | [SimpleAnimatorOptions](#ZH-CN_TOPIC_0000002497604768__simpleanimatoroptions18)是定义动画选项。

**错误码：**

以下错误码的详细介绍请参考[通用错误码](../../errors/通用错误码.md)和[接口调用异常错误码](../../errors/接口调用异常错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed.100001The specified page is not found or the object property list is not obtained.

**示例：**

完整示例请参考[基于ArkTS扩展的声明式开发范式](#ZH-CN_TOPIC_0000002497604768__基于arkts扩展的声明式开发范式)。

```ets
import { Animator as animator, AnimatorResult, AnimatorOptions, SimpleAnimatorOptions } from '@kit.ArkUI';

let options: AnimatorOptions = {
  duration: 1500,
  easing: "ease",
  delay: 0,
  fill: "forwards",
  direction: "normal",
  iterations: 1,
  begin: 100,
  end: 200
};
let optionsNew: SimpleAnimatorOptions = new SimpleAnimatorOptions(100, 200)
  .duration(2000)
  .iterations(3)
  .delay(1000)
let animatorResult: AnimatorResult = animator.create(options);
animatorResult.reset(optionsNew);
```

#### play

play(): void

启动动画。动画会保留上一次的播放状态，比如播放状态设置reverse后，再次播放会保留reverse的播放状态。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

完整示例请参考[基于ArkTS扩展的声明式开发范式](#ZH-CN_TOPIC_0000002497604768__基于arkts扩展的声明式开发范式)。

```ets
animator.play();
```

#### finish

finish(): void

结束动画，会触发[onFinish](#ZH-CN_TOPIC_0000002497604768__属性)回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

完整示例请参考[基于ArkTS扩展的声明式开发范式](#ZH-CN_TOPIC_0000002497604768__基于arkts扩展的声明式开发范式)。

```ets
animator.finish();
```

#### pause

pause(): void

暂停动画。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

完整示例请参考[基于ArkTS扩展的声明式开发范式](#ZH-CN_TOPIC_0000002497604768__基于arkts扩展的声明式开发范式)。

```ets
animator.pause();
```

#### cancel

cancel(): void

取消动画，会触发[onCancel](#ZH-CN_TOPIC_0000002497604768__属性)回调。此接口和[finish](#ZH-CN_TOPIC_0000002497604768__finish)接口功能上没有区别，仅触发的回调不同，建议使用finish接口结束动画。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

完整示例请参考[基于ArkTS扩展的声明式开发范式](#ZH-CN_TOPIC_0000002497604768__基于arkts扩展的声明式开发范式)。

```ets
animator.cancel();
```

#### reverse

reverse(): void

以相反的顺序播放动画。使用interpolating-spring曲线时此接口无效。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

完整示例请参考[基于ArkTS扩展的声明式开发范式](#ZH-CN_TOPIC_0000002497604768__基于arkts扩展的声明式开发范式)。

```ets
animator.reverse();
```

#### setExpectedFrameRateRange12+

setExpectedFrameRateRange(rateRange: ExpectedFrameRateRange): void

设置期望的帧率范围。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明rateRange[ExpectedFrameRateRange](../../topics/misc/显式动画 (animateTo).md#ZH-CN_TOPIC_0000002497444950__expectedframeraterange11)是设置期望的帧率范围。

开发者通过设置有效的期望帧率后，系统会收集设置的请求帧率，进行决策和分发，在渲染管线上进行分频，尽量能够满足开发者的期望帧率。开发者设置的期望帧率值不能代表最终实际效果，会受限于系统能力和屏幕刷新率。

**示例：**

```ets
import { AnimatorResult } from '@kit.ArkUI';

let expectedFrameRate: ExpectedFrameRateRange = {
  min: 0,
  max: 120,
  expected: 30
}

@Entry
@Component
struct AnimatorTest {
  private backAnimator: AnimatorResult | undefined = undefined

  create() {
    this.backAnimator = this.getUIContext().createAnimator({
      duration: 2000,
      easing: "ease",
      delay: 0,
      fill: "forwards",
      direction: "normal",
      iterations: 1,
      begin: 100, //动画插值起点
      end: 200 //动画插值终点
    })
    this.backAnimator.setExpectedFrameRateRange(expectedFrameRate);
  }

  build() {
    // ......
  }
}
```

#### update(deprecated)

update(options: AnimatorOptions): void

更新当前动画器。

从API version 6开始支持，从API version 9开始废弃。建议使用[reset](#ZH-CN_TOPIC_0000002497604768__reset9)替代。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明options[AnimatorOptions](#ZH-CN_TOPIC_0000002497604768__animatoroptions)是定义动画选项。

**示例：**

完整示例请参考[基于ArkTS扩展的声明式开发范式](#ZH-CN_TOPIC_0000002497604768__基于arkts扩展的声明式开发范式)。

```ets
animator.update(options);
```

#### AnimatorOptions

定义动画选项。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

#### 属性

名称类型只读可选说明durationnumber否否

动画播放的时长，单位毫秒。

取值范围：[0, +∞)

默认值：0

easingstring否否

动画插值曲线，支持的曲线类型可参考表1。

非法字符串时取:"ease"。

delaynumber否否

动画延时播放时长，单位毫秒，设置为0时，表示不延时。设置为负数时动画提前播放，如果提前播放的时长大于动画总时长，动画直接过渡到终点。

默认值：0

fill'none' | 'forwards' | 'backwards' | 'both'否否

动画执行后是否恢复到初始状态，动画执行后，动画结束时的状态（在最后一个关键帧中定义）将保留。

'none'：在动画执行之前和之后都不会应用任何样式到目标上。

'forwards'：在动画结束后，目标将保留动画结束时的状态（在最后一个关键帧中定义）。

'backwards'：动画将在[AnimatorOptions](#ZH-CN_TOPIC_0000002497604768__animatoroptions)中的delay期间应用第一个关键帧中定义的值。当[AnimatorOptions](#ZH-CN_TOPIC_0000002497604768__animatoroptions)中的direction为'normal'或'alternate'时应用from关键帧中的值，当[AnimatorOptions](#ZH-CN_TOPIC_0000002497604768__animatoroptions)中的direction为'reverse'或'alternate-reverse'时应用to关键帧中的值。

'both'：动画将遵循forwards和backwards的规则，从而在两个方向上扩展动画属性。

direction'normal' | 'reverse' | 'alternate' | 'alternate-reverse'否否

动画播放模式。

'normal'： 动画正向循环播放。

'reverse'： 动画反向循环播放。

'alternate'：动画交替循环播放，奇数次正向播放，偶数次反向播放。

'alternate-reverse'：动画反向交替循环播放，奇数次反向播放，偶数次正向播放。

默认值：'normal'

iterationsnumber否否

动画播放次数。设置为0时不播放，设置为-1时无限次播放，设置大于0时为播放次数。

**说明:** 设置为除-1外其他负数视为无效取值，无效取值动画默认播放1次。

beginnumber否否

动画插值起点。

**说明:** 会影响[onFrame](#ZH-CN_TOPIC_0000002497604768__属性)回调的入参值。

默认值：0

endnumber否否

动画插值终点。

**说明:** 会影响[onFrame](#ZH-CN_TOPIC_0000002497604768__属性)回调的入参值。

默认值：1

**表1 支持的曲线类型：**

类型说明"linear"动画线性变化。"ease"动画开始和结束时的速度较慢，cubic-bezier(0.25, 0.1, 0.25, 1.0)。"ease-in"动画播放速度先慢后快，cubic-bezier(0.42, 0.0, 1.0, 1.0)。"ease-out"动画播放速度先快后慢，cubic-bezier(0.0, 0.0, 0.58, 1.0)。"ease-in-out"动画播放速度先加速后减速，cubic-bezier(0.42, 0.0, 0.58, 1.0)。"fast-out-slow-in"标准曲线，cubic-bezier(0.4, 0.0, 0.2, 1.0)。"linear-out-slow-in"减速曲线，cubic-bezier(0.0, 0.0, 0.2, 1.0)。"fast-out-linear-in"加速曲线，cubic-bezier(0.4, 0.0, 1.0, 1.0)。"friction"阻尼曲线，cubic-bezier(0.2, 0.0, 0.2, 1.0)。"extreme-deceleration"急缓曲线，cubic-bezier(0.0, 0.0, 0.0, 1.0)。"rhythm"节奏曲线，cubic-bezier(0.7, 0.0, 0.2, 1.0)。"sharp"锐利曲线，cubic-bezier(0.33, 0.0, 0.67, 1.0)。"smooth"平滑曲线，cubic-bezier(0.4, 0.0, 0.4, 1.0)。"cubic-bezier(x1, y1, x2, y2)"三次贝塞尔曲线，x1、x2的值必须处于0-1之间。例如"cubic-bezier(0.42, 0.0, 0.58, 1.0)"。"steps(number, step-position)"阶梯曲线，number必须设置，为正整数，step-position参数可选，支持设置start或end，默认值为end。例如"steps(3, start)"。interpolating-spring(velocity, mass, stiffness, damping)

插值弹簧曲线。

velocity、mass、stiffness、damping都是数值类型，且mass、stiffness、damping参数均应该大于0，具体参数含义参考[插值弹簧曲线](@ohos.curves (插值计算).md#ZH-CN_TOPIC_0000002497604788__curvesinterpolatingspring10)。

使用interpolating-spring时，duration不生效，由弹簧参数决定；fill、direction、iterations设置无效，fill固定设置为"forwards"，direction固定设置为"normal"，iterations固定设置为1，且对animator的[reverse](#ZH-CN_TOPIC_0000002497604768__reverse)函数调用无效。即animator使用interpolating-spring时只能正向播放1次。

从API version 11开始支持且仅在ArkTS中支持使用。

#### SimpleAnimatorOptions18+

animator简易动画参数对象。与AnimatorOptions相比，部分动画参数有默认值，可不设置。

#### constructor18+

constructor(begin: number, end: number)

SimpleAnimatorOptions的构造函数。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明beginnumber是动画插值起点。endnumber是动画插值终点。

**示例：**

完整示例请参考[基于ArkTS扩展的声明式开发范式](#ZH-CN_TOPIC_0000002497604768__基于arkts扩展的声明式开发范式)。

```ets
import { AnimatorResult, SimpleAnimatorOptions } from '@kit.ArkUI';

@Entry
@Component
struct AnimatorTest {
  private animatorResult: AnimatorResult | undefined = undefined;
  options: SimpleAnimatorOptions = new SimpleAnimatorOptions(100, 200); // 动画插值过程从100到200，其余动画参数使用默认值。

  create() {
    this.animatorResult = this.getUIContext().createAnimator(this.options);
  }

  build() {
    // ......
  }
}
```

#### duration18+

duration(duration: number): SimpleAnimatorOptions

设置animator动画时长。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明durationnumber是

设置动画时长，单位毫秒。

默认值：1000

**返回值：**

类型说明[SimpleAnimatorOptions](#ZH-CN_TOPIC_0000002497604768__simpleanimatoroptions18)Animator简易动画参数对象。

**示例：**

完整示例请参考[基于ArkTS扩展的声明式开发范式](#ZH-CN_TOPIC_0000002497604768__基于arkts扩展的声明式开发范式)。

```ets
import { AnimatorResult, SimpleAnimatorOptions } from '@kit.ArkUI';

@Entry
@Component
struct AnimatorTest {
  private animatorResult: AnimatorResult | undefined = undefined;
  options: SimpleAnimatorOptions = new SimpleAnimatorOptions(100, 200).duration(500);

  create() {
    this.animatorResult = this.getUIContext().createAnimator(this.options);
  }

  build() {
    // ......
  }
}
```

#### easing18+

easing(curve: string): SimpleAnimatorOptions

设置animator动画插值曲线。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明curvestring是

设置animator动画插值曲线，具体说明参考[AnimatorOptions](#ZH-CN_TOPIC_0000002497604768__animatoroptions)。

默认值：“ease”

**返回值：**

类型说明[SimpleAnimatorOptions](#ZH-CN_TOPIC_0000002497604768__simpleanimatoroptions18)Animator简易动画参数对象。

**示例：**

完整示例请参考[基于ArkTS扩展的声明式开发范式](#ZH-CN_TOPIC_0000002497604768__基于arkts扩展的声明式开发范式)。

```ets
import { AnimatorResult, SimpleAnimatorOptions } from '@kit.ArkUI';

@Entry
@Component
struct AnimatorTest {
  private animatorResult: AnimatorResult | undefined = undefined;
  options: SimpleAnimatorOptions = new SimpleAnimatorOptions(100, 200).easing("ease-in");

  create() {
    this.animatorResult = this.getUIContext().createAnimator(this.options);
  }

  build() {
    // ......
  }
}
```

#### delay18+

delay(delay: number): SimpleAnimatorOptions

设置animator动画播放时延。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明delaynumber是

设置animator动画播放时延，单位毫秒，设置为0时，表示不延时。设置为负数时动画提前播放，如果提前播放的时长大于动画总时长，动画直接过渡到终点。

默认值：0

**返回值：**

类型说明[SimpleAnimatorOptions](#ZH-CN_TOPIC_0000002497604768__simpleanimatoroptions18)Animator简易动画参数对象。

**示例：**

完整示例请参考[基于ArkTS扩展的声明式开发范式](#ZH-CN_TOPIC_0000002497604768__基于arkts扩展的声明式开发范式)。

```ets
import { AnimatorResult, SimpleAnimatorOptions } from '@kit.ArkUI';

@Entry
@Component
struct AnimatorTest {
  private animatorResult: AnimatorResult | undefined = undefined;
  options: SimpleAnimatorOptions = new SimpleAnimatorOptions(100, 200).delay(500);

  create() {
    this.animatorResult = this.getUIContext().createAnimator(this.options);
  }

  build() {
    // ......
  }
}
```

#### fill18+

fill(fillMode: [FillMode](../../guides/枚举说明.md#ZH-CN_TOPIC_0000002529284967__fillmode)): SimpleAnimatorOptions

设置animator动画填充方式。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明fillMode[FillMode](../../guides/枚举说明.md#ZH-CN_TOPIC_0000002529284967__fillmode)是

设置animator动画填充方式，影响动画delay期间和结束时的表现。

默认值：FillMode.Forwards

**返回值：**

类型说明[SimpleAnimatorOptions](#ZH-CN_TOPIC_0000002497604768__simpleanimatoroptions18)Animator简易动画参数对象。

**示例：**

完整示例请参考[基于ArkTS扩展的声明式开发范式](#ZH-CN_TOPIC_0000002497604768__基于arkts扩展的声明式开发范式)。

```ets
import { AnimatorResult, SimpleAnimatorOptions } from '@kit.ArkUI';

@Entry
@Component
struct AnimatorTest {
  private animatorResult: AnimatorResult | undefined = undefined;
  options: SimpleAnimatorOptions = new SimpleAnimatorOptions(100, 200).fill(FillMode.Forwards);

  create() {
    this.animatorResult = this.getUIContext().createAnimator(this.options);
  }

  build() {
    // ......
  }
}
```

#### direction18+

direction(direction: [PlayMode](../../guides/枚举说明.md#ZH-CN_TOPIC_0000002529284967__playmode)): SimpleAnimatorOptions

设置animator动画播放方向。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明direction[PlayMode](../../guides/枚举说明.md#ZH-CN_TOPIC_0000002529284967__playmode)是

设置animator动画播放方向。

默认值：PlayMode.Normal

**返回值：**

类型说明[SimpleAnimatorOptions](#ZH-CN_TOPIC_0000002497604768__simpleanimatoroptions18)Animator简易动画参数对象。

**示例：**

完整示例请参考[基于ArkTS扩展的声明式开发范式](#ZH-CN_TOPIC_0000002497604768__基于arkts扩展的声明式开发范式)。

```ets
import { AnimatorResult, SimpleAnimatorOptions } from '@kit.ArkUI';

@Entry
@Component
struct AnimatorTest {
  private animatorResult: AnimatorResult | undefined = undefined;
  options: SimpleAnimatorOptions = new SimpleAnimatorOptions(100, 200).direction(PlayMode.Alternate);

  create() {
    this.animatorResult = this.getUIContext().createAnimator(this.options);
  }

  build() {
    // ......
  }
}
```

#### iterations18+

iterations(iterations: number): SimpleAnimatorOptions

设置animator动画播放次数。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明iterationsnumber是

设置animator动画播放次数，设置为0时不播放，设置为-1时无限次播放。

默认值：1

**返回值：**

类型说明[SimpleAnimatorOptions](#ZH-CN_TOPIC_0000002497604768__simpleanimatoroptions18)Animator简易动画参数对象。

**示例：**

完整示例请参考[基于ArkTS扩展的声明式开发范式](#ZH-CN_TOPIC_0000002497604768__基于arkts扩展的声明式开发范式)。

```ets
import { AnimatorResult, SimpleAnimatorOptions } from '@kit.ArkUI';

@Entry
@Component
struct AnimatorTest {
  private animatorResult: AnimatorResult | undefined = undefined;
  options: SimpleAnimatorOptions = new SimpleAnimatorOptions(100, 200).iterations(3);

  create() {
    this.animatorResult = this.getUIContext().createAnimator(this.options);
  }

  build() {
    // ......
  }
}
```

#### 完整示例

#### 基于JS扩展的类Web开发范式

```ets
<!-- hml -->
<div class="container">
  <div class="Animation" style="height: {{divHeight}}px; width: {{divWidth}}px; background-color: red;" onclick="Show">
  </div>
</div>
```

```ets
import { Animator as animator, AnimatorResult } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

let DataTmp: Record<string, Animator> = {
  'divWidth': 200,
  'divHeight': 200,
  'animator': animator
}

class Tmp {
  data: animator = DataTmp
  onInit: Function = () => {
  }
  Show: Function = () => {
  }
}

class DateT {
  divWidth: number = 0
  divHeight: number = 0
  animator: AnimatorResult | null = null
}

(Fn: (v: Tmp) => void) => {
  Fn({
    data: DataTmp,
    onInit() {
      let options: AnimatorOptions = {
        duration: 1500,
        easing: "friction",
        delay: 0,
        fill: "forwards",
        direction: "normal",
        iterations: 2,
        begin: 200.0,
        end: 400.0
      };
      let DataTmp: DateT = {
        divWidth: 200,
        divHeight: 200,
        animator: null
      }
      DataTmp.animator = animator.create(options);
    },
    Show() {
      let options1: AnimatorOptions = {
        duration: 1500,
        easing: "friction",
        delay: 0,
        fill: "forwards",
        direction: "normal",
        iterations: 2,
        begin: 0,
        end: 400.0,
      };
      let DataTmp: DateT = {
        divWidth: 200,
        divHeight: 200,
        animator: null
      }
      try {
        DataTmp.animator = animator.create(options1);
        DataTmp.animator.reset(options1);
      } catch (error) {
        let message = (error as BusinessError).message
        let code = (error as BusinessError).code
        console.error(`Animator reset failed, error code: ${code}, message: ${message}.`);
      }
      let _this = DataTmp;
      if (DataTmp.animator) {
        DataTmp.animator.onFrame = (value: number) => {
          _this.divWidth = value;
          _this.divHeight = value;
        };
        DataTmp.animator.play();
      }
    }
  })
}
```

#### 基于ArkTS扩展的声明式开发范式

推荐通过使用[UIContext](../../types/classes/Class (UIContext).md)中的[createAnimator](../../types/classes/Class (UIContext).md#ZH-CN_TOPIC_0000002529444749__createanimator)接口明确UI上下文。

```ets
import { AnimatorResult } from '@kit.ArkUI';

@Entry
@Component
struct AnimatorTest {
  private TAG: string = '[AnimatorTest]'
  private backAnimator: AnimatorResult | undefined = undefined
  private flag: boolean = false
  @State columnWidth: number = 100
  @State columnHeight: number = 100

  create() {
    this.backAnimator = this.getUIContext().createAnimator({
      // 建议使用 this.getUIContext().createAnimator()接口
      duration: 2000,
      easing: "ease",
      delay: 0,
      fill: "forwards",
      direction: "normal",
      iterations: 1,
      begin: 100, //动画插值起点
      end: 200 //动画插值终点
    })
    this.backAnimator.onFinish = () => {
      this.flag = true
      console.info(this.TAG, 'backAnimator onFinish')
    }
    this.backAnimator.onRepeat = () => {
      console.info(this.TAG, 'backAnimator repeat')
    }
    this.backAnimator.onCancel = () => {
      console.info(this.TAG, 'backAnimator cancel')
    }
    this.backAnimator.onFrame = (value: number) => {
      this.columnWidth = value
      this.columnHeight = value
    }
  }

  aboutToDisappear() {
    // 自定义组件消失时调用finish使未完成的动画结束，避免动画继续运行。
    // 由于backAnimator在onframe中引用了this, this中保存了backAnimator，
    // 在自定义组件消失时应该将保存在组件中的backAnimator置空，避免内存泄漏
    this.backAnimator?.finish();
    this.backAnimator = undefined;
  }

  build() {
    Column() {
      Column() {
        Column()
          .width(this.columnWidth)
          .height(this.columnHeight)
          .backgroundColor(Color.Red)
      }
      .width('100%')
      .height(300)

      Column() {
        Row() {
          Button('create')
            .fontSize(30)
            .fontColor(Color.Black)
            .onClick(() => {
              this.create()
            })
        }
        .padding(10)

        Row() {
          Button('play')
            .fontSize(30)
            .fontColor(Color.Black)
            .onClick(() => {
              this.flag = false
              if (this.backAnimator) {
                this.backAnimator.play()
              }
            })
        }
        .padding(10)

        Row() {
          Button('pause')
            .fontSize(30)
            .fontColor(Color.Black)
            .onClick(() => {
              if (this.backAnimator) {
                this.backAnimator.pause()
              }
            })
        }
        .padding(10)

        Row() {
          Button('finish')
            .fontSize(30)
            .fontColor(Color.Black)
            .onClick(() => {
              this.flag = true
              if (this.backAnimator) {
                this.backAnimator.finish()
              }
            })
        }
        .padding(10)

        Row() {
          Button('reverse')
            .fontSize(30)
            .fontColor(Color.Black)
            .onClick(() => {
              this.flag = false
              if (this.backAnimator) {
                this.backAnimator.reverse()
              }
            })
        }
        .padding(10)

        Row() {
          Button('cancel')
            .fontSize(30)
            .fontColor(Color.Black)
            .onClick(() => {
              if (this.backAnimator) {
                this.backAnimator.cancel()
              }
            })
        }
        .padding(10)

        Row() {
          Button('reset')
            .fontSize(30)
            .fontColor(Color.Black)
            .onClick(() => {
              if (this.flag) {
                this.flag = false
                if (this.backAnimator) {
                  this.backAnimator.reset({
                    duration: 3000,
                    easing: "ease-in",
                    delay: 0,
                    fill: "forwards",
                    direction: "alternate",
                    iterations: 3,
                    begin: 100,
                    end: 300
                  })
                }
              } else {
                console.info(this.TAG, 'Animation not ended')
              }
            })
        }
        .padding(10)
      }
    }
  }
}
```

#### 位移动画示例（简易入参）

```ets
import { AnimatorResult, SimpleAnimatorOptions } from '@kit.ArkUI';

@Entry
@Component
struct AnimatorTest {
  private TAG: string = '[AnimatorTest]'
  private backAnimator: AnimatorResult | undefined = undefined
  private flag: boolean = false
  @State translate_: number = 0

  create() {
    this.backAnimator = this.getUIContext()?.createAnimator(
      new SimpleAnimatorOptions(0, 100)
    )
    this.backAnimator.onFinish = ()=> {
      this.flag = true
      console.info(this.TAG, 'backAnimator onFinish')
    }
    this.backAnimator.onFrame = (value:number)=> {
      this.translate_ = value
    }
  }

  aboutToDisappear() {
    // 自定义组件消失时调用finish使未完成的动画结束，避免动画继续运行。
    // 由于backAnimator在onframe中引用了this, this中保存了backAnimator，
    // 在自定义组件消失时应该将保存在组件中的backAnimator置空，避免内存泄漏
    this.backAnimator?.finish();
    this.backAnimator = undefined;
  }

  build() {
    Column() {
      Column() {
        Column()
          .width(100)
          .height(100)
          .translate({x: this.translate_})
          .backgroundColor(Color.Green)
      }
      .width('100%')
      .height(300)

      Column() {
        Column() {
          Button('create')
            .fontSize(30)
            .fontColor(Color.White)
            .onClick(() => {
              this.create()
            })
        }
        .padding(10)

        Column() {
          Button('play')
            .fontSize(30)
            .fontColor(Color.White)
            .onClick(() => {
              this.flag = false
              if(this.backAnimator){
                this.backAnimator.play()
              }
            })
        }
        .padding(10)

        Column() {
          Button('reset')
            .fontSize(30)
            .fontColor(Color.White)
            .onClick(() => {
              if (this.flag) {
                this.flag = false
                if(this.backAnimator){
                  this.backAnimator.reset(
                    new SimpleAnimatorOptions(0, -100)
                      .duration(2000)
                      .easing("ease-in")
                      .fill(FillMode.Forwards)
                      .direction(PlayMode.Alternate)
                      .iterations(2)
                  )
                }
              } else {
                console.info(this.TAG, 'Animation not ended')
              }
            })
        }
        .padding(10)
      }
    }
  }
}
```