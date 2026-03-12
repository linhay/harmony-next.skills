# PanGesture

滑动手势事件，当滑动的最小距离达到设定的最小值时触发滑动手势事件。

以下场景可以触发滑动手势：

触发方式输入源类型输入设备类型备注手指按下滑动。[SourceTool](绑定手势方法.md#ZH-CN_TOPIC_0000002529284849__sourcetool枚举说明9).Finger[SourceType](绑定手势方法.md#ZH-CN_TOPIC_0000002529284849__sourcetype枚举说明8).TouchScreenaxisVertical和axisHorizontal均为0。鼠标左键按下滑动。[SourceTool](绑定手势方法.md#ZH-CN_TOPIC_0000002529284849__sourcetool枚举说明9).MOUSE[SourceType](绑定手势方法.md#ZH-CN_TOPIC_0000002529284849__sourcetype枚举说明8).MouseaxisVertical和axisHorizontal均为0。鼠标滚轮滚动。[SourceTool](绑定手势方法.md#ZH-CN_TOPIC_0000002529284849__sourcetool枚举说明9).MOUSE[SourceType](绑定手势方法.md#ZH-CN_TOPIC_0000002529284849__sourcetype枚举说明8).MouseaxisVertical或axisHorizontal不为0。触摸板按下左键后滑动。[SourceTool](绑定手势方法.md#ZH-CN_TOPIC_0000002529284849__sourcetool枚举说明9).MOUSE[SourceType](绑定手势方法.md#ZH-CN_TOPIC_0000002529284849__sourcetype枚举说明8).MouseaxisVertical和axisHorizontal均为0。触摸板双指滑动。[SourceTool](绑定手势方法.md#ZH-CN_TOPIC_0000002529284849__sourcetool枚举说明9).TOUCHPAD[SourceType](绑定手势方法.md#ZH-CN_TOPIC_0000002529284849__sourcetype枚举说明8).MouseaxisVertical或axisHorizontal不为0。手写笔滑动。[SourceTool](绑定手势方法.md#ZH-CN_TOPIC_0000002529284849__sourcetool枚举说明9).Pen[SourceType](绑定手势方法.md#ZH-CN_TOPIC_0000002529284849__sourcetype枚举说明8).TouchScreenaxisVertical和axisHorizontal均为0。

 从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

#### 接口

#### PanGesture

PanGesture(value?: { fingers?: number; direction?: PanDirection; distance?: number } | PanGestureOptions)

创建滑动手势对象。继承自[GestureInterface<T>](手势公共接口.md#ZH-CN_TOPIC_0000002497604864__gestureinterfacet11)

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明value{ fingers?: number; direction?: [PanDirection](PanGesture.md#ZH-CN_TOPIC_0000002497604860__pandirection枚举说明); distance?: number } | [PanGestureOptions](#ZH-CN_TOPIC_0000002497604860__pangestureoptions)否

滑动手势参数。

 - fingers：用于指定触发滑动的最少手指数，最小为1指，最大取值为10指。

默认值：1

取值范围：[1, 10]

**说明：**

当设置的值小于1或不设置时，会被转化为默认值。

 - direction：用于指定触发滑动的手势方向，此枚举值支持逻辑与(&)和逻辑或（|）运算。

默认值：PanDirection.All

 - distance：用于指定触发滑动手势事件的最小滑动距离，单位为vp。

取值范围：[0, +∞)

手写笔默认值：8，其余输入源默认值：5

**说明：**

[Tabs](Tabs.md)组件滑动与该滑动手势事件同时存在时，可将distance值设为1，使滑动更灵敏，避免造成事件错乱。

当设定的值小于0时，按默认值处理。

#### PanGesture15+

PanGesture(options?: PanGestureHandlerOptions)

创建滑动手势对象。与[PanGesture](#ZH-CN_TOPIC_0000002497604860__pangesture-1)相比，options参数新增了对isFingerCountLimited和distanceMap参数，分别表示是否检查触摸屏幕的手指数量以及指定不同输入源触发滑动手势事件的最小滑动距离。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明options[PanGestureHandlerOptions](手势处理器.md#ZH-CN_TOPIC_0000002497604858__pangesturehandleroptions)否滑动手势处理器配置参数。

#### PanDirection枚举说明

与SwipeDirection不同，PanDirection没有角度限制。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称值说明All-所有方向。Horizontal-水平方向。Vertical-竖直方向。Left-向左滑动。Right-向右滑动。Up-向上滑动。Down-向下滑动。None-任何方向都不可触发滑动手势事件。

#### PanGestureOptions

#### constructor

constructor(value?: { fingers?: number; direction?: PanDirection; distance?: number })

创建滑动手势配置参数对象。通过PanGestureOptions对象接口可以动态修改滑动手势的属性，从而避免通过状态变量修改属性（状态变量修改会导致UI刷新）。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明value{ fingers?: number; direction?: [PanDirection](#ZH-CN_TOPIC_0000002497604860__pandirection枚举说明); distance?: number }否

滑动手势配置参数对象。

fingers用于指定触发滑动的最少手指数，最小为1指， 最大取值为10指。

默认值：1

direction用于指定触发滑动的手势方向，此枚举值支持逻辑与(&)和逻辑或（|）运算。

默认值：PanDirection.All

distance用于指定触发滑动手势事件的最小滑动距离，单位为vp。

手写笔默认值：8，其余输入源默认值：5

**说明：**

[Tabs](Tabs.md)组件滑动与该滑动手势事件同时存在时，可将distance值设为1，使滑动更灵敏，避免造成事件错乱。

当设定的值小于0时，按默认值处理。

建议设置合理的滑动距离，滑动距离设置过大时会导致滑动不跟手（响应时延慢）的问题。

#### setDirection

setDirection(value: PanDirection)

设置滑动方向。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明value[PanDirection](#ZH-CN_TOPIC_0000002497604860__pandirection枚举说明)是

用于指定触发滑动的手势方向，此枚举值支持逻辑与(&)和逻辑或（|）运算。

默认值：PanDirection.All

#### setDistance

setDistance(value: number)

设置触发滑动手势事件的最小滑动距离，单位为vp。距离值不宜设置过大，避免因滑动脱手，响应时延过大等问题导致性能劣化，最佳实践请参考：[减小拖动识别距离](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-application-latency-optimization-cases#section1116134115286)。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明valuenumber是

触发滑动手势事件的最小滑动距离，单位为vp。

手写笔默认值：8，其余输入源默认值：5

**说明：**

[Tabs组件](Tabs.md)滑动与该滑动手势事件同时存在时，可将distance值设为1，使滑动更灵敏，避免造成事件错乱。

当设定的值小于0时，按默认值处理。

建议设置合理的滑动距离，滑动距离设置过大时会导致滑动不跟手（响应时延慢）的问题。

#### setFingers

setFingers(value: number)

设置触发滑动的最少手指数。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明valuenumber是

触发滑动的最少手指数，最小为1指， 最大取值为10指。

默认值：1

#### getDirection12+

getDirection(): PanDirection

获取滑动方向。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

类型说明[PanDirection](#ZH-CN_TOPIC_0000002497604860__pandirection枚举说明)滑动方向。

#### getDistance18+

getDistance(): number

获取触发滑动手势事件的最小滑动距离。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

类型说明number滑动手势事件的最小滑动距离。

#### 事件

 在[GestureEvent](手势公共接口.md#ZH-CN_TOPIC_0000002497604864__gestureevent对象说明)的fingerList元素中，手指索引编号与位置相对应，即fingerList[index]的id为index。对于先按下但未参与当前手势触发的手指，fingerList中对应的位置为空。建议优先使用fingerInfos。

#### onActionStart

onActionStart(event: (event: GestureEvent) => void)

设置滑动手势识别成功回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明event(event: [GestureEvent](手势公共接口.md#ZH-CN_TOPIC_0000002497604864__gestureevent对象说明)) => void是滑动手势识别成功回调。

#### onActionUpdate

onActionUpdate(event: (event: GestureEvent) => void)

设置滑动手势更新回调。fingerList为多根手指时，该回调监听每次只会更新一根手指的位置信息。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明event(event: [GestureEvent](手势公共接口.md#ZH-CN_TOPIC_0000002497604864__gestureevent对象说明)) => void是滑动手势更新回调。

#### onActionEnd

onActionEnd(event: (event: GestureEvent) => void)

设置滑动手势结束回调。滑动手势识别成功后，手指抬起时触发回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明event(event: [GestureEvent](手势公共接口.md#ZH-CN_TOPIC_0000002497604864__gestureevent对象说明)) => void是滑动手势结束回调。

#### onActionCancel

onActionCancel(event: () => void)

设置滑动手势取消回调。滑动手势识别成功后，接收到触摸取消事件时触发回调。不返回手势事件信息。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明event() => void是滑动手势取消回调。

#### onActionCancel18+

onActionCancel(event: Callback<GestureEvent>)

设置滑动手势取消回调。滑动手势识别成功后，接收到触摸取消事件时触发回调。返回手势事件信息。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明eventCallback<[GestureEvent](手势公共接口.md#ZH-CN_TOPIC_0000002497604864__gestureevent对象说明)>是滑动手势取消回调。

#### 示例

该示例通过PanGesture实现了单指/双指滑动手势的识别。

```ets
// xxx.ets
@Entry
@Component
struct PanGestureExample {
  @State offsetX: number = 0;
  @State offsetY: number = 0;
  @State positionX: number = 0;
  @State positionY: number = 0;
  private panOption: PanGestureOptions = new PanGestureOptions({ direction: PanDirection.Left | PanDirection.Right });

  build() {
    Column() {
      Column() {
        Text('PanGesture offset:\nX: ' + this.offsetX + '\n' + 'Y: ' + this.offsetY)
      }
      .height(200)
      .width(300)
      .padding(20)
      .border({ width: 3 })
      .margin(50)
      .translate({ x: this.offsetX, y: this.offsetY, z: 0 }) // 以组件左上角为坐标原点进行移动
      // 左右滑动触发该手势事件
      .gesture(
      PanGesture(this.panOption)
        .onActionStart((event: GestureEvent) => {
          console.info('Pan start');
          console.info(`Pan start timeStamp is: ${event.timestamp}`);
        })
        .onActionUpdate((event: GestureEvent) => {
          if (event) {
            this.offsetX = this.positionX + event.offsetX;
            this.offsetY = this.positionY + event.offsetY;
          }
        })
        .onActionEnd((event: GestureEvent) => {
          this.positionX = this.offsetX;
          this.positionY = this.offsetY;
          console.info('Pan end');
          console.info(`Pan end timeStamp is: ${event.timestamp}`);
        })
      )

      Button('修改PanGesture触发条件')
        .onClick(() => {
          // 将PanGesture手势事件触发条件改为双指以任意方向滑动
          this.panOption.setDirection(PanDirection.All);
          this.panOption.setFingers(2);
        })
    }
  }
}
```

示意图：

向左滑动：

点击按钮时，修改PanGesture触发条件为双指向左下方滑动：