# LongPressGesture

用于触发长按手势事件，触发长按手势的最少手指数为1，默认最短长按时间为500毫秒。可配置duration参数控制最短长按时长。

-

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

-

从API version 18开始，部分设备会优先响应系统的双指长按手势，导致应用的双指长按手势不生效。

#### 接口

#### LongPressGesture

LongPressGesture(value?: { fingers?: number; repeat?: boolean; duration?: number })

创建长按手势对象。继承自[GestureInterface<T>](手势公共接口.md#ZH-CN_TOPIC_0000002497604864__gestureinterfacet11)。

当组件默认支持可拖拽时，如Text、TextInput、TextArea、HyperLink、Image和RichEditor等组件。长按手势与拖拽会出现冲突，事件优先级如下：

当长按触发时间小于500毫秒时，系统优先响应长按事件而非拖拽事件。

当长按触发时间达到或超过500毫秒时，系统优先响应拖拽事件而非长按事件。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明value{ fingers?: number; repeat?: boolean; duration?: number }否

设置长按手势参数。

 - fingers：触发长按的最少手指数，最小值为1， 最大值为10。

默认值：1

 - repeat：是否连续触发事件回调。true表示连续触发事件回调，false表示不连续触发事件回调。

默认值：false

 - duration：触发长按的最短时间，单位为毫秒（ms）。

默认值：500

#### LongPressGesture15+

LongPressGesture(options?: LongPressGestureHandlerOptions)

创建长按手势对象。与[LongPressGesture](#ZH-CN_TOPIC_0000002529444825__longpressgesture-1)相比，options参数新增了对isFingerCountLimited参数，表示是否检查触摸屏幕的手指数量。

当组件默认支持可拖拽时，如Text、TextInput、TextArea、HyperLink、Image和RichEditor等组件。长按手势与拖拽会出现冲突，事件优先级如下：

当长按触发时间小于500毫秒时，系统优先响应长按事件而非拖拽事件。

当长按触发时间达到或超过500毫秒时，系统优先响应拖拽事件而非长按事件。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明options[LongPressGestureHandlerOptions](手势处理器.md#ZH-CN_TOPIC_0000002497604858__longpressgesturehandleroptions)否长按手势处理器配置参数。

#### 事件

-

在[GestureEvent](手势公共接口.md#ZH-CN_TOPIC_0000002497604864__gestureevent对象说明)的fingerList元素中，手指索引编号与位置相对应，即fingerList[index]的id为index。对于先按下但未参与当前手势触发的手指，fingerList中对应的位置为空。建议优先使用fingerInfos。

-

长按手势触发后，[GestureEvent](手势公共接口.md#ZH-CN_TOPIC_0000002497604864__gestureevent对象说明)中fingerList和fingerInfo的信息仅在有手指按下时才会更新，手指抬起时不会更新。

#### onAction

onAction(event: (event: GestureEvent) => void)

设置长按手势识别成功回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明event(event: [GestureEvent](手势公共接口.md#ZH-CN_TOPIC_0000002497604864__gestureevent对象说明)) => void是长按手势识别成功回调函数。

#### onActionEnd

onActionEnd(event: (event: GestureEvent) => void)

设置长按手势结束回调。长按手势识别成功后，最后一根手指抬起时触发回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明event(event: [GestureEvent](手势公共接口.md#ZH-CN_TOPIC_0000002497604864__gestureevent对象说明)) => void是长按手势结束回调函数。

#### onActionCancel

onActionCancel(event: () => void)

设置长按手势取消回调。长按手势识别成功后，接收到触摸取消事件时触发回调。不返回手势事件信息。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明event() => void是长按手势取消回调函数。

#### onActionCancel18+

onActionCancel(event: Callback<GestureEvent>)

设置长按手势取消回调。长按手势识别成功后，接收到触摸取消事件时触发回调。返回手势事件信息。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明eventCallback<[GestureEvent](手势公共接口.md#ZH-CN_TOPIC_0000002497604864__gestureevent对象说明)>是长按手势取消回调函数。

#### 示例

该示例通过LongPressGesture实现了长按手势的识别。从API version 22开始，支持通过[LongPressGestureHandlerOptions](手势处理器.md#ZH-CN_TOPIC_0000002497604858__longpressgesturehandleroptions)的allowableMovement属性设置识别手势的最大移动距离。

```ets
// xxx.ets
@Entry
@Component
struct LongPressGestureExample {
  @State count: number = 0;

  build() {
    Column() {
      Text('LongPress onAction:' + this.count).fontSize(28)
        // 单指长按文本触发该手势事件
        .gesture(
        // 设置长按手势识别器识别的手势的最大移动距离为200px
        LongPressGesture({ repeat: true, allowableMovement: 200 })
          // 由于repeat设置为true，长按动作存在时会连续触发，触发间隔为duration（默认值500ms）
          .onAction((event: GestureEvent) => {
            if (event && event.repeat) {
              this.count++
            }
          })
            // 长按动作一结束触发
          .onActionEnd((event: GestureEvent) => {
            this.count = 0
          })
        )
    }
    .height(200)
    .width(300)
    .padding(20)
    .border({ width: 3 })
    .margin(30)
  }
}
```