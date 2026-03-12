# PinchGesture

用于触发捏合手势，最少需要2指，最多5指，最小识别距离为5vp。

 从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

 捏合手势触发成功后，抬起手指直至不再满足触发条件。再次满足条件时，可重新触发捏合手势。

#### 接口

#### PinchGesture

PinchGesture(value?: { fingers?: number; distance?: number })

继承自[GestureInterface<T>](手势公共接口.md#ZH-CN_TOPIC_0000002497604864__gestureinterfacet11)，设置捏合手势事件。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明value{ fingers?: number; distance?: number }否

设置捏合手势事件参数。

 - fingers：触发捏合的最少手指数，最小为2指，最大为5指。

默认值：2

取值范围：[2, 5]。当设置的值不在该范围内时，会被转化为默认值。

触发手势的手指数量可以多于fingers数目，但只有最先落下的与fingers相同数目的手指参与手势计算。

 - distance：最小识别距离，单位为vp。该距离是指当前多根手指位置与手指中心位置的平均距离，与手指落下时的平均距离之间的差值。当这一差值大于或等于最小识别距离时，捏合手势被视为成功。

默认值：5

**说明：**

取值范围：[0, +∞)。当识别距离的值小于等于0时，会被转化为默认值。

#### PinchGesture15+

PinchGesture(options?: PinchGestureHandlerOptions)

设置捏合手势事件。与[PinchGesture](#ZH-CN_TOPIC_0000002497444882__pinchgesture-1)相比，options参数新增isFingerCountLimited，表示是否检查触摸屏幕的手指数量。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明options[PinchGestureHandlerOptions](手势处理器.md#ZH-CN_TOPIC_0000002497604858__pinchgesturehandleroptions)否捏合手势处理器配置参数。

#### 事件

 在[GestureEvent](手势公共接口.md#ZH-CN_TOPIC_0000002497604864__gestureevent对象说明)的fingerList元素中，手指索引编号与位置相对应，即fingerList[index]的id为index。对于先按下但未参与当前手势触发的手指，fingerList中对应的位置为空。建议开发者优先使用fingerInfos。

#### onActionStart

onActionStart(event: (event: GestureEvent) => void)

Pinch手势识别成功后触发回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明event(event: [GestureEvent](手势公共接口.md#ZH-CN_TOPIC_0000002497604864__gestureevent对象说明)) => void是手势事件回调函数。

#### onActionUpdate

onActionUpdate(event: (event: GestureEvent) => void)

Pinch手势移动过程中回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明event(event: [GestureEvent](手势公共接口.md#ZH-CN_TOPIC_0000002497604864__gestureevent对象说明)) => void是手势事件回调函数。

#### onActionEnd

onActionEnd(event: (event: GestureEvent) => void)

Pinch手势识别成功，当抬起最后一根满足手势触发条件的手指后，触发回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明event(event: [GestureEvent](手势公共接口.md#ZH-CN_TOPIC_0000002497604864__gestureevent对象说明)) => void是手势事件回调函数。

#### onActionCancel

onActionCancel(event: () => void)

Pinch手势识别成功，接收到触摸取消事件触发的回调，不返回手势事件信息。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明event() => void是手势事件回调函数。

#### onActionCancel18+

onActionCancel(event: Callback<GestureEvent>)

Pinch手势识别成功并接收到触摸取消事件的回调。与[onActionCancel](#ZH-CN_TOPIC_0000002497444882__onactioncancel)相比，该回调返回手势事件信息。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明eventCallback<[GestureEvent](手势公共接口.md#ZH-CN_TOPIC_0000002497604864__gestureevent对象说明)>是手势事件回调函数。

#### 示例

#### 示例1（实现简单缩放）

该示例通过配置PinchGesture实现了三指捏合手势的识别功能。

```ets
// xxx.ets
@Entry
@Component
struct PinchGestureExample {
  @State scaleValue: number = 1;
  @State pinchValue: number = 1;
  @State pinchX: number = 0;
  @State pinchY: number = 0;

  build() {
    Column() {
      Column() {
        Text('PinchGesture scale:\n' + this.scaleValue)
        Text('PinchGesture center:\n(' + this.pinchX + ',' + this.pinchY + ')')
      }
      .height(200)
      .width(300)
      .padding(20)
      .border({ width: 3 })
      .margin({ top: 100 })
      .scale({ x: this.scaleValue, y: this.scaleValue, z: 1 })
      // 三指捏合触发该手势事件
      .gesture(
      PinchGesture({ fingers: 3 }) // 三指捏合手势，用于缩放操作
        .onActionStart((event: GestureEvent) => {
          console.info('Pinch start')
        })
        .onActionUpdate((event: GestureEvent) => {
          if (event) {
            this.scaleValue = this.pinchValue * event.scale
            this.pinchX = event.pinchCenterX
            this.pinchY = event.pinchCenterY
          }
        })
        .onActionEnd((event: GestureEvent) => {
          this.pinchValue = this.scaleValue
          console.info('Pinch end')
        })
      )
    }.width('100%')
  }
}
```

#### 示例2（实现图片跟手缩放）

通过配置PinchGesture，该示例实现了图片的跟手缩放效果。

```ets
// xxx.ets
import { UIContext, display, matrix4 } from '@kit.ArkUI';

@Entry
@Component
struct PinchGestureExample {
  private uiContext: UIContext = new UIContext();
  private contentWidth: number = 0;
  private contentHeight: number = 0;
  private scaleMin: number = 0.3;
  private scaleMax: number = 30.0;
  private screenWidth: number = 0;
  private screenHeight: number = 0;
  @State pntX: number = 0;
  @State pntY: number = 0;
  @State curScale: number = 1;
  @State preScale: number = 1;
  @State offsetX: number = 0;
  @State offsetY: number = 0;
  @State matrix: matrix4.Matrix4Transit = matrix4.identity()
    .translate({ x: this.offsetX, y: this.offsetY })
    .scale({ x: this.curScale, y: this.curScale });

  public updateMatrix(): void {
    this.matrix = matrix4.identity()
      .scale({ x: this.curScale, y: this.curScale })
      .translate({ x: this.uiContext.vp2px(this.offsetX), y: this.uiContext.vp2px(this.offsetY) });
  }

  aboutToAppear(): void {
    this.uiContext = this.getUIContext();
    let screenSize = display.getDefaultDisplaySync();
    this.screenWidth = this.uiContext.px2vp(screenSize.width);
    this.screenHeight = this.uiContext.px2vp(screenSize.height);
  }

  build() {
    Column() {
      // $r('app.media.img')需要替换为开发者所需的图像资源文件。
      Image($r('app.media.img'))
        .objectFit(ImageFit.Contain)
        .draggable(false)
        .onComplete((event) => {
          this.contentWidth = this.uiContext.px2vp(event!.contentWidth);
          this.contentHeight = this.uiContext.px2vp(event!.contentHeight);
        })
        .transform(this.matrix)
    }
    // 双指捏合触发该手势事件
    .gesture(
      PinchGesture({ fingers: 2 }) // 双指捏合手势，用于缩放图片
        .onActionStart((event: GestureEvent) => {
          // 图片本次缩放前展示大小
          const displayWidth = this.contentWidth * this.curScale;
          const displayHeight = this.contentHeight * this.curScale;
          // 图片本次缩放前左上角顶点
          const left = (this.screenWidth - displayWidth) / 2 + this.offsetX;
          const top = (this.screenHeight - displayHeight) / 2 + this.offsetY;
          // 本次缩放前手指终点相对图片左上角顶点尺寸占图片展示尺寸的百分比
          this.pntX = (event.pinchCenterX - left) / displayWidth;
          this.pntY = (event.pinchCenterY - top) / displayHeight;
          // 图片本次缩放前的缩放比例
          this.preScale = this.curScale;
        })
        .onActionUpdate((event: GestureEvent) => {
          // 目标缩放比
          this.curScale = this.preScale * event.scale;
          let targetDisplayWidth = this.contentWidth * this.curScale;
          let targetDisplayHeight = this.contentHeight * this.curScale;
          // 本次缩放前手指中点在本次缩放后的坐标
          const pointX = (this.screenWidth - targetDisplayWidth) / 2 + targetDisplayWidth * this.pntX;
          const pointY = (this.screenHeight - targetDisplayHeight) / 2 + targetDisplayHeight * this.pntY;
          // 将pointX、pointY移动到缩放后的手指中点，需要移动的距离
          this.offsetX = event.pinchCenterX - pointX;
          this.offsetY = event.pinchCenterY - pointY;
          this.updateMatrix();
        })
        .onActionEnd((event: GestureEvent) => {
          if (this.curScale < this.scaleMin || this.curScale > this.scaleMax) {
            this.curScale = 1;
            this.offsetX = 0;
            this.offsetY = 0;
            this.updateMatrix();
          }
        })
    )
  }
}
```