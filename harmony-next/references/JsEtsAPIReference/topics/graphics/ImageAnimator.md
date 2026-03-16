# ImageAnimator

提供帧动画组件来实现逐帧播放图片的能力，可以配置需要播放的图片列表，每张图片可以配置时长。

该组件从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

#### 子组件

无

#### 接口

ImageAnimator()

**卡片能力：** 从API version 10开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

#### 属性

除支持[通用属性](../misc/通用属性.md)外，还支持以下属性：

#### images

images(value: Array<ImageFrameInfo>)

设置图片帧信息集合。不支持动态更新。

**卡片能力：** 从API version 10开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明valueArray<[ImageFrameInfo](#ZH-CN_TOPIC_0000002529284893__imageframeinfo对象说明)>是

设置图片帧信息集合。每一帧的帧信息(ImageFrameInfo)包含图片路径、图片大小、图片位置和图片播放时长信息，详见[ImageFrameInfo](#ZH-CN_TOPIC_0000002529284893__imageframeinfo对象说明)对象说明。

默认值：[]

**说明：** 传入数组的内容过大时，内存占用会随之升高。此内存由开发者自行控制。因此，开发者在传入数据前，请充分评估内存消耗情况，以避免内存不足等问题。

#### state

state(value: AnimationStatus)

控制播放状态。

**卡片能力：** 从API version 10开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明value[AnimationStatus](../../guides/枚举说明.md#ZH-CN_TOPIC_0000002529284967__animationstatus)是

默认为初始状态，用于控制播放状态。

默认值：AnimationStatus.Initial

#### duration

duration(value: number)

设置播放时长。当Images中任意一帧图片设置了单独的duration后，该属性设置无效。

**卡片能力：** 从API version 10开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明valuenumber是

播放时长。

value为0时，不播放图片。

value平均分配给单张图片的播放时长小于一帧时间，将导致播放异常。

设置为负数时，取默认值。

value的改变只会在下一次循环开始时生效。

单位：毫秒

默认值：1000ms

#### reverse

reverse(value: boolean)

设置播放方向。

**卡片能力：** 从API version 10开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明valueboolean是

播放方向。

false表示从第1张图片播放到最后1张图片，true表示从最后1张图片播放到第1张图片。

默认值：false

#### fixedSize

fixedSize(value: boolean)

设置图片大小是否固定为组件大小。

**卡片能力：** 从API version 10开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明valueboolean是

设置图片大小是否固定为组件大小。 true表示图片大小与组件大小一致，此时设置图片的width 、height 、top 和left属性无效。false表示每一张图片的width 、height 、top和left属性都要单独设置。图片宽高与组件宽高不一致时，图片不会被拉伸。

默认值：true

#### preDecode(deprecated)

preDecode(value: number)

设置预解码的图片数量。

从API version 7开始支持，从API version 9开始废弃。当前无可替代接口。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明valuenumber是

预解码的图片数量。例如，设置为2时，播放当前页时会提前加载后面两张图片至缓存，以提升性能。

默认值：0

#### fillMode

fillMode(value: FillMode)

设置当前播放方向下，动画开始前和结束后的状态。动画结束后的状态由fillMode和reverse属性共同决定。例如，fillMode为Forwards表示停止时维持动画最后一个关键帧的状态，若reverse为false则维持正播的最后一帧，即最后一张图，若reverse为true则维持逆播的最后一帧，即第一张图。

**卡片能力：** 从API version 10开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明value[FillMode](../../guides/枚举说明.md#ZH-CN_TOPIC_0000002529284967__fillmode)是

当前播放方向下，动画开始前和结束后的状态。

默认值：FillMode.Forwards

#### iterations

iterations(value: number)

设置播放次数。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明valuenumber是

默认播放一次，设置为-1时表示无限次播放，设置为小于-1的负数时取默认值。设置为浮点数时，数值向下取整。

默认值：1

#### monitorInvisibleArea17+

monitorInvisibleArea(monitorInvisibleArea: boolean)

设置组件是否通过系统[onVisibleAreaChange](../misc/组件可见区域变化事件.md#ZH-CN_TOPIC_0000002497444844__onvisibleareachange)的可见性判定，控制组件的暂停和播放。

**元服务API：** 从API version 17开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明monitorInvisibleAreaboolean是

当设置为true时，组件将基于系统的[onVisibleAreaChange](../misc/组件可见区域变化事件.md#ZH-CN_TOPIC_0000002497444844__onvisibleareachange)可见性判定，控制组件的暂停和播放。

 当组件的运行状态为[AnimationStatus](../../guides/枚举说明.md#ZH-CN_TOPIC_0000002529284967__animationstatus)的Running时，若判定组件不可见，则自动执行暂停操作；若判定为可见，则自动恢复播放。

默认值：false

**说明：**

当该属性由true动态修改为false时，组件将依据当前的[AnimationStatus](../../guides/枚举说明.md#ZH-CN_TOPIC_0000002529284967__animationstatus)状态进行处理。

 例如，若当前状态为Running且因[onVisibleAreaChange](../misc/组件可见区域变化事件.md#ZH-CN_TOPIC_0000002497444844__onvisibleareachange)的不可见回调暂停，则在属性由true改为false后，组件会从上次暂停的位置重新开始播放。

由该属性导致的不可见暂停和可见暂停操作不会改变用户设置的[state](ImageAnimator.md#ZH-CN_TOPIC_0000002529284893__state)值。

#### ImageFrameInfo对象说明

图片帧信息集合。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明srcstring | [Resource](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resource)9+ | [PixelMap](../misc/图像类型定义.md#ZH-CN_TOPIC_0000002497604902__pixelmap)12+否否

图片路径，图片格式为jpg、jpeg、svg、png、bmp、webp、ico和heif，从API Version9开始支持[Resource](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resource)类型的路径，从API version 12开始支持[PixelMap](../misc/图像类型定义.md#ZH-CN_TOPIC_0000002497604902__pixelmap)类型。

**卡片能力：** 从API version 10开始，该接口支持在ArkTS卡片中使用。

widthnumber | string否是

图片宽度。string类型支持number类型取值的字符串形式，可以附带单位，例如"2"、"2px"。

默认值：0

单位：vp

**卡片能力：** 从API version 10开始，该接口支持在ArkTS卡片中使用

heightnumber | string否是

图片高度。string类型支持number类型取值的字符串形式，可以附带单位，例如"2"、"2px"。

默认值：0

单位：vp

**卡片能力：** 从API version 10开始，该接口支持在ArkTS卡片中使用

topnumber | string否是

图片相对于组件左上角的纵向坐标。string类型支持number类型取值的字符串形式，可以附带单位，例如"2"、"2px"。

默认值：0

单位：vp

**卡片能力：** 从API version 10开始，该接口支持在ArkTS卡片中使用

leftnumber | string否是

图片相对于组件左上角的横向坐标。string类型支持number类型取值的字符串形式，可以附带单位，例如"2"、"2px"。

默认值：0

单位：vp

**卡片能力：** 从API version 10开始，该接口支持在ArkTS卡片中使用

durationnumber否是

每帧图片的播放时长，单位毫秒。

默认值：0

不支持负数。设置为负数将导致图片在当前帧长时间停留，影响正常播放。

#### 事件

除支持[通用事件](../misc/通用事件.md)外，还支持以下事件：

#### onStart

onStart(event: () => void)

状态回调，动画开始播放时触发。

**卡片能力：** 从API version 10开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明event() => void是状态回调，动画开始播放时触发。

#### onPause

onPause(event: () => void)

状态回调，动画暂停播放时触发。

**卡片能力：** 从API version 10开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明event() => void是状态回调，动画暂停播放时触发。

#### onRepeat

onRepeat(event: () => void)

状态回调，动画重复播放时触发。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明event() => void是状态回调，动画重复播放时触发。

#### onCancel

onCancel(event: () => void)

状态回调，动画返回最初状态时触发。

**卡片能力：** 从API version 10开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明event() => void是状态回调，动画返回最初状态时触发。

#### onFinish

onFinish(event: () => void)

状态回调，动画播放完成时或者停止播放时触发。

**卡片能力：** 从API version 10开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明event() => void是状态回调，动画播放完成时或者停止播放时触发。

#### 示例

#### 示例1（播放Resource动画）

通过ImageAnimator组件播放Resource动画。

```ets
// xxx.ets
@Entry
@Component
struct ImageAnimatorExample {
  @State state: AnimationStatus = AnimationStatus.Initial;
  @State reverse: boolean = false;
  @State iterations: number = 1;

  build() {
    Column({ space: 10 }) {
      ImageAnimator()
        .images([
          {
            // $r('app.media.img1')需要替换为开发者所需的图像资源文件。
            src: $r('app.media.img1')
          },
          {
            // $r('app.media.img2')需要替换为开发者所需的图像资源文件。
            src: $r('app.media.img2')
          },
          {
            // $r('app.media.img3')需要替换为开发者所需的图像资源文件。
            src: $r('app.media.img3')
          },
          {
            // $r('app.media.img4')需要替换为开发者所需的图像资源文件。
            src: $r('app.media.img4')
          }
        ])
        .duration(4000)
        .state(this.state)
        .reverse(this.reverse)
        .fillMode(FillMode.None)
        .iterations(this.iterations)
        .width(340)
        .height(240)
        .margin({ top: 100 })
        .onStart(() => {
          console.info('Start')
        })
        .onPause(() => {
          console.info('Pause')
        })
        .onRepeat(() => {
          console.info('Repeat')
        })
        .onCancel(() => {
          console.info('Cancel')
        })
        .onFinish(() => {
          console.info('Finish')
          this.state = AnimationStatus.Stopped
        })
      Row() {
        Button('start').width(100).padding(5).onClick(() => {
          this.state = AnimationStatus.Running
        }).margin(5)
        Button('pause').width(100).padding(5).onClick(() => {
          this.state = AnimationStatus.Paused // 显示当前帧图片
        }).margin(5)
        Button('stop').width(100).padding(5).onClick(() => {
          this.state = AnimationStatus.Stopped // 显示动画的起始帧图片
        }).margin(5)
      }

      Row() {
        Button('reverse').width(100).padding(5).onClick(() => {
          this.reverse = !this.reverse
        }).margin(5)
        Button('once').width(100).padding(5).onClick(() => {
          this.iterations = 1
        }).margin(5)
        Button('infinite').width(100).padding(5).onClick(() => {
          this.iterations = -1 // 无限循环播放
        }).margin(5)
      }
    }.width('100%').height('100%')
  }
}
```

#### 示例2（播放PixelMap动画）

通过ImageAnimator组件播放PixelMap动画。

```ets
// xxx.ets
import { image } from '@kit.ImageKit';

@Entry
@Component
struct ImageAnimatorExample {
  imagePixelMap: Array<PixelMap> = [];
  @State state: AnimationStatus = AnimationStatus.Initial;
  @State reverse: boolean = false;
  @State iterations: number = 1;
  @State images: Array<ImageFrameInfo> = [];

  async aboutToAppear() {
    // $r('app.media.1')需要替换为开发者所需的图像资源文件。
    this.imagePixelMap.push(await this.getPixmapFromMedia($r('app.media.1')));
    // $r('app.media.2')需要替换为开发者所需的图像资源文件。
    this.imagePixelMap.push(await this.getPixmapFromMedia($r('app.media.2')));
    // $r('app.media.3')需要替换为开发者所需的图像资源文件。
    this.imagePixelMap.push(await this.getPixmapFromMedia($r('app.media.3')));
    // $r('app.media.4')需要替换为开发者所需的图像资源文件。
    this.imagePixelMap.push(await this.getPixmapFromMedia($r('app.media.4')));
    this.images.push({ src: this.imagePixelMap[0] });
    this.images.push({ src: this.imagePixelMap[1] });
    this.images.push({ src: this.imagePixelMap[2] });
    this.images.push({ src: this.imagePixelMap[3] });
  }

  build() {
    Column({ space: 10 }) {
      ImageAnimator()
        .images(this.images)
        .duration(2000)
        .state(this.state)
        .reverse(this.reverse)
        .fillMode(FillMode.None)
        .iterations(this.iterations)
        .width(340)
        .height(240)
        .margin({ top: 100 })
        .onStart(() => {
          console.info('Start');
        })
        .onPause(() => {
          console.info('Pause');
        })
        .onRepeat(() => {
          console.info('Repeat');
        })
        .onCancel(() => {
          console.info('Cancel');
        })
        .onFinish(() => {
          console.info('Finish');
          this.state = AnimationStatus.Stopped;
        })
      Row() {
        Button('start').width(100).padding(5).onClick(() => {
          this.state = AnimationStatus.Running;
        }).margin(5)
        Button('pause').width(100).padding(5).onClick(() => {
          this.state = AnimationStatus.Paused; // 显示当前帧图片
        }).margin(5)
        Button('stop').width(100).padding(5).onClick(() => {
          this.state = AnimationStatus.Stopped; // 显示动画的起始帧图片
        }).margin(5)
      }

      Row() {
        Button('reverse').width(100).padding(5).onClick(() => {
          this.reverse = !this.reverse;
        }).margin(5)
        Button('once').width(100).padding(5).onClick(() => {
          this.iterations = 1;
        }).margin(5)
        Button('infinite').width(100).padding(5).onClick(() => {
          this.iterations = -1; // 无限循环播放
        }).margin(5)
      }
    }.width('100%').height('100%')
  }

  private async getPixmapFromMedia(resource: Resource) {
    let unit8Array = await this.getUIContext().getHostContext()?.resourceManager?.getMediaContent(resource.id);
    let imageSource = image.createImageSource(unit8Array?.buffer.slice(0, unit8Array.buffer.byteLength));
    let createPixelMap: image.PixelMap = await imageSource.createPixelMap({
      desiredPixelFormat: image.PixelMapFormat.RGBA_8888
    });
    await imageSource.release();
    return createPixelMap;
  }
}
```

#### 示例3（设置不可见自动停播）

通过[monitorInvisibleArea](#ZH-CN_TOPIC_0000002529284893__monitorinvisiblearea17)属性实现了当ImageAnimator的[state](#ZH-CN_TOPIC_0000002529284893__state)属性为AnimationStatus.Running时，控制组件在不可见时停止播放，在可见时恢复播放。

```ets
@Entry
@Component
struct ImageAnimatorAutoPauseTest {
  scroller: Scroller = new Scroller();
  @State state: AnimationStatus = AnimationStatus.Running;
  @State reverse: boolean = false;
  @State iterations: number = 100;
  @State preCallBack: string = 'Null';
  private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];

  build() {
    Stack({ alignContent: Alignment.TopStart }) {
      Scroll(this.scroller) {
        Column() {
          ImageAnimator()
            .images([
              {
                // $r('app.media.Clouds')需要替换为开发者所需的图像资源文件。
                src: $r('app.media.Clouds')
              },
              {
                // $r('app.media.landscape')需要替换为开发者所需的图像资源文件。
                src: $r('app.media.landscape')
              },
              {
                // $r('app.media.sky')需要替换为开发者所需的图像资源文件。
                src: $r('app.media.sky')
              },
              {
                // $r('app.media.mountain')需要替换为开发者所需的图像资源文件。
                src: $r('app.media.mountain')
              }
            ])
            .borderRadius(10)
            .monitorInvisibleArea(true)
            .clip(true)
            .duration(4000)
            .state(this.state)
            .reverse(this.reverse)
            .fillMode(FillMode.Forwards)
            .iterations(this.iterations)
            .width(340)
            .height(240)
            .margin({ top: 100 })
            .onStart(() => {
              this.preCallBack = "Start";
              console.info('ImageAnimator Start');
            })
            .onPause(() => {
              this.preCallBack = "Pause";
              console.info('ImageAnimator Pause');
            })
            .onRepeat(() => {
              console.info('ImageAnimator Repeat');
            })
            .onCancel(() => {
              console.info('ImageAnimator Cancel');
            })
            .onFinish(() => {
              console.info('ImageAnimator Finish');
            })
          ForEach(this.arr, (item: number) => {
            Text(item.toString())
              .width('90%')
              .height(150)
              .backgroundColor(0xFFFFFF)
              .borderRadius(15)
              .fontSize(16)
              .textAlign(TextAlign.Center)
              .margin({ top: 10 })
          }, (item: string) => item)
        }.width('100%')
      }
      .scrollable(ScrollDirection.Vertical) // 滚动方向纵向
      .scrollBar(BarState.On) // 滚动条常驻显示
      .scrollBarColor(Color.Gray) // 滚动条颜色
      .scrollBarWidth(10) // 滚动条宽度
      .friction(0.6)
      .edgeEffect(EdgeEffect.None)
      .onWillScroll((xOffset: number, yOffset: number, scrollState: ScrollState) => {
        console.info(xOffset + ' ' + yOffset);
      })
      .onScrollEdge((side: Edge) => {
        console.info('To the edge');
      })
      .onScrollStop(() => {
        console.info('Scroll Stop');
      })

      Text("上次触发的回调（Pause/Start）：" + this.preCallBack)
        .margin({ top: 60, left: 20 })
    }.width('100%').height('100%').backgroundColor(0xDCDCDC)
  }
}
```