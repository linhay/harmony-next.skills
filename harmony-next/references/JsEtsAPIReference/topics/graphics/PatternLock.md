# PatternLock

图案密码锁组件，以九宫格图案的方式输入密码，用于密码验证场景。手指在PatternLock组件区域按下时开始进入输入状态，手指离开屏幕时结束输入状态完成密码输入。

该组件从API version 9开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

#### 子组件

无

#### 接口

PatternLock(controller?: PatternLockController)

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明controller[PatternLockController](#ZH-CN_TOPIC_0000002497604908__patternlockcontroller)否设置PatternLock组件控制器，可用于控制组件状态重置。

#### 属性

除支持[通用属性](../misc/通用属性.md)外，还支持以下属性：

#### sideLength

sideLength(value: Length)

设置组件的宽度和高度（宽高相同）。当设置为0或负数时，组件不显示。

PatternLock组件设置了通用属性宽高比[aspectRatio](../misc/布局约束.md#ZH-CN_TOPIC_0000002529444795__aspectratio)，且不等于1时（组件尺寸被设定为长方形），九宫格依然绘制为正方形（超出组件范围）。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明value[Length](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__length)是组件的宽度和高度。默认值：288vp

#### circleRadius

circleRadius(value: Length)

设置宫格中圆点的半径。设置为0或负数时，取默认值。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明value[Length](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__length)是

宫格中圆点的半径。

默认值：6vp

取值范围：(0, sideLength/11]。设置小于等于0的值时，按默认值处理；超过最大值时，按最大值处理。

#### backgroundColor

backgroundColor(value: ResourceColor)

设置背景颜色。

从API version 20开始，该接口支持在[attributeModifier](../misc/动态属性设置.md#ZH-CN_TOPIC_0000002529284843__attributemodifier)中调用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明value[ResourceColor](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)是背景颜色。

#### regularColor

regularColor(value: ResourceColor)

设置宫格圆点在“未选中”状态的填充颜色。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明value[ResourceColor](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)是

宫格圆点在“未选中”状态的填充颜色。

默认值：'#ff182431'

#### selectedColor

selectedColor(value: ResourceColor)

设置宫格圆点在“选中”状态的填充颜色。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明value[ResourceColor](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)是

宫格圆点在“选中”状态的填充颜色。

默认值：'#ff182431'

#### activeColor

activeColor(value: ResourceColor)

设置宫格圆点在“激活”状态的填充颜色，“激活”状态为手指经过圆点但还未选中的状态。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明value[ResourceColor](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)是

宫格圆点在“激活”状态的填充颜色。

默认值：'#ff182431'

#### pathColor

pathColor(value: ResourceColor)

设置连线的颜色。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明value[ResourceColor](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)是

连线的颜色。

默认值：'#33182431'

#### pathStrokeWidth

pathStrokeWidth(value: number | string)

设置连线的宽度。设置为0或负数时连线不显示。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明valuenumber | string是

连线的宽度。

默认值：12vp

取值范围：(0, sideLength/3]，超过最大值按最大值处理。

#### autoReset

autoReset(value: boolean)

设置在完成密码输入后再次在组件区域按下时是否重置组件状态。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明valueboolean是

在完成密码输入后再次在组件区域按下时是否重置组件状态。

true：完成密码输入后再次在组件区域按下时重置组件状态（即清除之前输入的密码）；false：完成密码输入后再次在组件区域按下时不重置组件状态。

默认值：true

#### activateCircleStyle12+

activateCircleStyle(options: Optional<CircleStyleOptions>)

设置宫格圆点在“激活”状态下的背景圆环样式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明optionsOptional<[CircleStyleOptions](#ZH-CN_TOPIC_0000002497604908__circlestyleoptions12对象说明)>是宫格圆点在“激活”状态的背景圆环样式。

#### skipUnselectedPoint15+

skipUnselectedPoint(skipped: boolean)

设置未选中的宫格圆点在密码路径经过时是否自动选中。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明skippedboolean是

未选中的宫格圆点在密码路径经过时是否自动选中。

默认值：false，自动选中密码路径经过的宫格圆点。

#### 事件

除支持[通用事件](../misc/通用事件.md)外，还支持以下事件：

#### onPatternComplete

onPatternComplete(callback: (input: Array<number>) => void)

密码输入结束时触发该回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明inputArray<number>是与选中宫格圆点顺序一致的数字数组，每个数字表示选中宫格圆点的索引值（第一行圆点从左往右依次为0、1、2，第二行圆点从左往右依次为3、4、5，第三行圆点从左往右依次为6、7、8）。

#### onDotConnect11+

onDotConnect(callback: [Callback](../../modules/ohos/@ohos.base (公共回调信息).md#ZH-CN_TOPIC_0000002497445536__callback)<number>)

密码输入选中宫格圆点时触发该回调。

回调参数为选中宫格圆点顺序的数字，数字为选中宫格圆点的索引值（第一行圆点从左往右依次为0、1、2，第二行圆点从左往右依次为3、4、5，第三行圆点从左往右依次为6、7、8）。

从API version 20开始，该接口支持在[attributeModifier](../misc/动态属性设置.md#ZH-CN_TOPIC_0000002529284843__attributemodifier)中调用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明callback[Callback](../../modules/ohos/@ohos.base (公共回调信息).md#ZH-CN_TOPIC_0000002497445536__callback)<number>是密码输入选中宫格圆点时触发该回调。

#### CircleStyleOptions12+对象说明

圆环样式的参数说明。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明color[ResourceColor](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否是

背景圆环颜色。

默认值：与[pathColor](#ZH-CN_TOPIC_0000002497604908__pathcolor)值相同。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

radius[LengthMetrics](Graphics.md#ZH-CN_TOPIC_0000002529444761__lengthmetrics12)否是

背景圆环的半径。

默认值：[circleRadius](#ZH-CN_TOPIC_0000002497604908__circleradius)的1.833倍（即11/6）。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

enableWaveEffectboolean否是

选中宫格圆点后的波浪效果开关。

默认值：true，表示波浪效果打开。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

enableForeground15+boolean否是

背景圆环是否显示在宫格圆点上层。

默认值：false，背景圆环显示在宫格圆点下层，不遮盖宫格圆点。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

#### PatternLockController

PatternLock组件的控制器，用于重置组件状态。

#### 导入对象

```ets
let patternLockController: PatternLockController = new PatternLockController()
```

#### constructor

constructor()

PatternLockController的构造函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

#### reset

reset()

重置组件状态。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

#### setChallengeResult11+

setChallengeResult(result: PatternLockChallengeResult): void

设置图案密码的正确或错误状态。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明result[PatternLockChallengeResult](#ZH-CN_TOPIC_0000002497604908__patternlockchallengeresult11枚举说明)是图案密码状态。

#### PatternLockChallengeResult11+枚举说明

图案密码状态。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称值说明CORRECT1图案密码正确。WRONG2图案密码错误。

#### 示例

#### 示例1（创建图案密码锁）

该示例展示了PatternLock组件的基本使用方法。

```ets
// xxx.ets
@Entry
@Component
struct PatternLockExample {
  @State passwords: number[] = [];
  @State message: string = 'please input password!';
  private patternLockController: PatternLockController = new PatternLockController();

  build() {
    Column() {
      Text(this.message).textAlign(TextAlign.Center).margin(20).fontSize(20)
      PatternLock(this.patternLockController)
        .sideLength(200)
        .circleRadius(9)
        .pathStrokeWidth(5)
        .activeColor('#707070')
        .selectedColor('#707070')
        .pathColor('#707070')
        .backgroundColor('#F5F5F5')
        .autoReset(true)
        .onDotConnect((index: number) => {
          console.info("onDotConnect index: " + index);
        })
    }.width('100%').height('100%')
  }
}
```

#### 示例2（判断密码是否正确）

该示例通过[sideLength](#ZH-CN_TOPIC_0000002497604908__sidelength)属性设置九宫格的大小、[circleRadius](#ZH-CN_TOPIC_0000002497604908__circleradius)等属性设置宫格圆点样式、[onPatternComplete](#ZH-CN_TOPIC_0000002497604908__onpatterncomplete)属性设置密码输入时的回调。

当用户密码输入完成后，按输入的密码不同，给予不同的回应：输入的密码长度小于5时，提示重新输入；第一次输入完成后，提示第二次输入密码；第二次输入完成后，判断两次输入的密码是否相同，相同则提示密码设置成功，否则提示重新输入。

通过'Reset PatternLock'按钮，用户可以重置密码锁。

```ets
// xxx.ets
import { LengthUnit } from '@kit.ArkUI';

@Entry
@Component
struct PatternLockExample {
  @State passwords: number[] = [];
  @State message: string = 'please input password!';
  private patternLockController: PatternLockController = new PatternLockController();

  build() {
    Column() {
      Text(this.message).textAlign(TextAlign.Center).margin(20).fontSize(20)
      PatternLock(this.patternLockController)
        .sideLength(200)
        .circleRadius(9)
        .pathStrokeWidth(5)
        .activeColor('#707070')
        .selectedColor('#707070')
        .pathColor('#707070')
        .backgroundColor('#F5F5F5')
        .autoReset(true)
        .activateCircleStyle({
          color: '#707070',
          radius: { value: 16, unit: LengthUnit.VP },
          enableWaveEffect: true
        })
        .onDotConnect((index: number) => {
          console.info("onDotConnect index: " + index);
        })
        .onPatternComplete((input: Array<number>) => {
          // 输入的密码长度小于5时，提示重新输入
          if (input.length < 5) {
            this.message = 'The password length needs to be greater than 5, please enter again.';
            return;
          }
          // 判断密码长度是否大于0
          if (this.passwords.length > 0) {
            // 判断两次输入的密码是否相同，相同则提示密码设置成功，否则提示重新输入
            if (this.passwords.toString() === input.toString()) {
              this.passwords = input;
              this.message = 'Set password successfully: ' + this.passwords.toString();
              this.patternLockController.setChallengeResult(PatternLockChallengeResult.CORRECT);
            } else {
              this.message = 'Inconsistent passwords, please enter again.';
              this.patternLockController.setChallengeResult(PatternLockChallengeResult.WRONG);
            }
          } else {
            // 提示第二次输入密码
            this.passwords = input;
            this.message = "Please enter again.";
          }
        })
      Button('Reset PatternLock').margin(30).onClick(() => {
        // 重置密码锁
        this.patternLockController.reset();
        this.passwords = [];
        this.message = 'Please input password';
      })
    }.width('100%').height('100%')
  }
}
```