# RotationGesture

用于触发旋转手势，最少需要2指，最多5指，最小改变度数为1度。该手势不支持通过触控板双指旋转操作触发。

 从API Version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

#### 接口

#### RotationGesture

RotationGesture(value?: { fingers?: number; angle?: number })

继承自[GestureInterface<T>](手势公共接口.md#ZH-CN_TOPIC_0000002497604864__gestureinterfacet11)，设置旋转手势事件。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明value{ fingers?: number; angle?: number }否

设置旋转手势事件参数。

 - fingers：触发旋转手势所需的最少手指数， 最小为2指，最大为5指。

默认值：2

取值范围：[2, 5]。当设置的值小于2或大于5时，会被转化为默认值。

触发手势时手指数量可以多于fingers参数值，但仅最先落下的两指参与手势计算。

 - angle：触发旋转手势所需的最小角度变化，单位为deg。

默认值：1

**说明：**

当改变度数的值小于等于0或大于360时，会被转化为默认值。

#### RotationGesture15+

RotationGesture(options?: RotationGestureHandlerOptions)

设置旋转手势事件。与[RotationGesture](#ZH-CN_TOPIC_0000002529284853__rotationgesture-1)相比，options参数新增了isFingerCountLimited参数，表示是否检查触摸屏幕的手指数量。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明options[RotationGestureHandlerOptions](手势处理器.md#ZH-CN_TOPIC_0000002497604858__rotationgesturehandleroptions)否旋转手势处理器配置参数。

#### 事件

 在[GestureEvent](手势公共接口.md#ZH-CN_TOPIC_0000002497604864__gestureevent对象说明)的fingerList元素中，手指索引编号与位置相对应，即fingerList[index]的id为index。对于先按下但未参与当前手势触发的手指，fingerList中对应的位置为空。建议优先使用fingerInfos。

#### onActionStart

onActionStart(event: (event: GestureEvent) => void)

Rotation手势识别成功后触发的回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明event(event: [GestureEvent](手势公共接口.md#ZH-CN_TOPIC_0000002497604864__gestureevent对象说明)) => void是手势事件回调函数。

#### onActionUpdate

onActionUpdate(event: (event: GestureEvent) => void)

Rotation手势移动过程中触发的回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明event(event: [GestureEvent](手势公共接口.md#ZH-CN_TOPIC_0000002497604864__gestureevent对象说明)) => void是手势事件回调函数。

#### onActionEnd

onActionEnd(event: (event: GestureEvent) => void)

Rotation手势识别成功，当抬起最后一根满足手势触发条件的手指后触发的回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明event(event: [GestureEvent](手势公共接口.md#ZH-CN_TOPIC_0000002497604864__gestureevent对象说明)) => void是手势事件回调函数。

#### onActionCancel

onActionCancel(event: () => void)

Rotation手势识别成功，接收到触摸取消事件触发的回调。该回调不返回手势事件信息。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明event() => void是手势事件回调函数。

#### onActionCancel18+

onActionCancel(event: Callback<GestureEvent>)

Rotation手势识别成功，接收到触摸取消事件触发的回调。与[onActionCancel](#ZH-CN_TOPIC_0000002529284853__onactioncancel)相比，该回调返回手势事件信息。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明eventCallback<[GestureEvent](手势公共接口.md#ZH-CN_TOPIC_0000002497604864__gestureevent对象说明)>是手势事件回调函数。

#### 示例

该示例通过配置RotationGesture实现了双指旋转手势的识别。

```ets
// xxx.ets
@Entry
@Component
struct RotationGestureExample {
  @State angle: number = 0;
  @State rotateValue: number = 0;

  build() {
    Column() {
      Column() {
        Text('RotationGesture angle:' + this.angle)
      }
      .height(200)
      .width(300)
      .padding(20)
      .border({ width: 3 })
      .margin(80)
      .rotate({ angle: this.angle })
      // 双指旋转触发该手势事件
      .gesture(
      RotationGesture()
        .onActionStart((event: GestureEvent) => {
          console.info('Rotation start')
        })
        .onActionUpdate((event: GestureEvent) => {
          if (event) {
            this.angle = this.rotateValue + event.angle
          }
        })
        .onActionEnd((event: GestureEvent) => {
          this.rotateValue = this.angle
          console.info('Rotation end')
        })
      )
    }.width('100%')
  }
}
```