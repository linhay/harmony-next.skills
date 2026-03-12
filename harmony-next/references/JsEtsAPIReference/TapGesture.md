# TapGesture

支持单击、双击和多次点击事件的识别。

 从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

 当组件同时绑定双击和单击手势且双击手势先绑定时，单击手势会有300ms的延时。

#### 接口

TapGesture(value?: TapGestureParameters)

创建点击手势对象。继承自[GestureInterface<T>](手势公共接口.md#ZH-CN_TOPIC_0000002497604864__gestureinterfacet11)。

触发点击手势事件的设备类型为键盘或手柄时，事件的[SourceTool](绑定手势方法.md#ZH-CN_TOPIC_0000002529284849__sourcetool枚举说明9)值为Unknown，事件的[SourceType](绑定手势方法.md#ZH-CN_TOPIC_0000002529284849__sourcetype枚举说明8)值为KEY，JOYSTICK。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明value[TapGestureParameters](#ZH-CN_TOPIC_0000002529284851__tapgestureparameters12对象说明)否点击手势的相关参数。

#### TapGestureParameters12+对象说明

 为规范匿名对象的定义，API 12版本修改了此处的元素定义。其中，保留了历史匿名对象的起始版本信息，会出现外层元素@since版本号高于内层元素版本号的情况，但这不影响接口的使用。

点击手势参数。继承自[BaseHandlerOptions](手势处理器.md#ZH-CN_TOPIC_0000002497604858__basehandleroptions15)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明count11+number否是

识别的连续点击次数。当设置的值小于1或不设置时，会被转化为默认值。

默认值：1

取值范围：[0, +∞)

**说明：**

1. 当配置多击时，上一次的最后一根手指抬起和下一次的第一根手指按下的超时时间为300毫秒。

2. 当上次点击的位置与当前点击的位置距离超过60vp时，手势识别失败。在多指情况下，点击的位置为所有参与手势响应手指的平均位置。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

fingers11+number否是

触发点击的手指数，最小为1指， 最大为10指。当设置小于1的值或不设置时，会被转化为默认值。

默认值：1

**说明：**

1. 当配置多指时，第一根手指按下后300毫秒内未有足够的手指数按下，手势识别失败；手指抬起时，抬起后剩余的手指数小于阈值时开始计时，如300ms内未全部抬起则手势识别失败。

2. 实际点击手指数超过配置值，手势识别成功。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

distanceThresholdnumber否是

点击手势移动阈值。当设置的值小于等于0或不设置时，会被转化为默认值。

默认值：2³¹-1

单位：vp

**说明：**

当手指的移动距离超出开发者预设的移动阈值时，点击识别失败。如果初始化为默认阈值时，手指移动超过组件热区范围，点击识别失败。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

#### 事件

 组件通过手势事件绑定不同GestureType的手势对象，各手势对象在响应手势操作的事件回调中提供手势相关信息。下面通过TapGesture手势对象的[onAction](#ZH-CN_TOPIC_0000002529284851__onaction)事件响应点击事件，获取事件相关信息。其余手势对象的事件定义见各个手势对象章节。 若需绑定多种手势，请使用[组合手势](zh-cn_topic_0000002497604862.html)。

 在[GestureEvent](手势公共接口.md#ZH-CN_TOPIC_0000002497604864__gestureevent对象说明)的fingerList元素中，手指索引编号与位置相对应，即fingerList[index]的id为index。对于先按下但未参与当前手势触发的手指，fingerList中对应的位置为空。建议优先使用fingerInfos。

#### onAction

onAction(event: (event: GestureEvent) => void)

点击手势识别成功回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明event(event: [GestureEvent](手势公共接口.md#ZH-CN_TOPIC_0000002497604864__gestureevent对象说明)) => void是手势事件回调函数。

#### EventLocationInfo20+

用于点击手势获取点击位置坐标。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明xnumber否否

相对于组件左上角的x坐标。

取值范围：[0, +∞)

单位：vp

ynumber否否

相对于组件左上角的y坐标。

取值范围：[0, +∞)

单位：vp

windowXnumber否否

相对于窗口的左上角x坐标。

取值范围：[0, +∞)

单位：vp

windowYnumber否否

相对于窗口的左上角y坐标。

取值范围：[0, +∞)

单位：vp

displayXnumber否否

相对于屏幕的左上角x坐标。

取值范围：[0, +∞)

单位：vp

displayYnumber否否

相对于屏幕的左上角y坐标。

取值范围：[0, +∞)

单位：vp

#### 示例

#### 示例1（双击手势识别）

该示例通过TapGesture实现了双击手势的识别。

```ets
// xxx.ets
@Entry
@Component
struct TapGestureExample {
  @State value: string = '';

  build() {
    Column() {
      // 单指双击文本触发手势事件
      Text('Click twice').fontSize(28)
        .gesture(
        TapGesture({ count: 2 })
          .onAction((event: GestureEvent) => {
            if (event) {
              this.value = JSON.stringify(event.fingerList[0])
            }
          })
        )
      Text(this.value)
    }
    .height(300)
    .width(300)
    .padding(20)
    .border({ width: 3 })
    .margin(30)
  }
}
```

#### 示例2（获取单击手势坐标）

该示例通过TapGesture获取单击手势点击位置的坐标。

```ets
// xxx.ets
@Entry
@Component
struct TapGestureExample {
  @State value: string = ''

  build() {
    Column() {
      Text('Click Once').fontSize(28)
        .gesture(
          TapGesture({ count: 1, fingers: 1 })
            .onAction((event: GestureEvent | undefined) => {
              if (event) {
                console.info(`x = ${JSON.stringify(event.tapLocation?.x)}`)
                console.info(`y = ${JSON.stringify(event.tapLocation?.y)}`)
                console.info(`windowX = ${JSON.stringify(event.tapLocation?.windowX)}`)
                console.info(`windowY = ${JSON.stringify(event.tapLocation?.windowY)}`)
                console.info(`displayX = ${JSON.stringify(event.tapLocation?.displayX)}`)
                console.info(`displayY = ${JSON.stringify(event.tapLocation?.displayY)}`)
              }
            })
        )
      Text(this.value)
    }
    .height(200)
    .width(300)
    .padding(20)
    .border({ width: 3 })
    .margin(30)
  }
}
```