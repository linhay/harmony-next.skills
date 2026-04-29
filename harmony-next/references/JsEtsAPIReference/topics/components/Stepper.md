# Stepper

步骤导航器组件，适用于引导用户按照步骤完成任务的导航场景。

  ![image](public_sys-resources/note_3.0-zh-cn.webp)

-

从API version 8开始支持，从API version 22开始废弃，建议使用[Swiper](Swiper.md)替代。详细示例请参考[示例2](#ZH-CN_TOPIC_0000002522080932__示例2使用swiper替代stepper)。

-

该组件从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

**子组件**

仅能包含子组件[StepperItem](StepperItem.md)。

**接口**

Stepper(value?: { index?: number })

创建步骤导航器组件。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

从API version 8开始支持，从API version 22开始废弃，建议使用[index](Swiper.md#ZH-CN_TOPIC_0000002522240824__index)替代。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | { index?: number } | 否 | 设置步骤导航器当前显示StepperItem的索引值。 默认值：0 从API version 10开始，该参数支持$$双向绑定变量。 |

**属性**

无

**事件**

**onFinish(deprecated)**

onFinish(callback: () => void)

步骤导航器最后一个[StepperItem](StepperItem.md)的[nextLabel](StepperItem.md#ZH-CN_TOPIC_0000002553360855__nextlabeldeprecated)被点击时，并且[ItemState](StepperItem.md#ZH-CN_TOPIC_0000002553360855__itemstate枚举说明)属性为Normal时，触发该回调。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

从API version 8开始支持，从API version 22开始废弃，建议使用[onChange](Swiper.md#ZH-CN_TOPIC_0000002522240824__onchange)替代。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | () => void | 是 | 步骤导航器最后一个StepperItem的nextLabel被点击时，并且ItemState属性为Normal时，触发该回调。 |

**onSkip(deprecated)**

onSkip(callback: () => void)

当前显示的[StepperItem](StepperItem.md)状态为ItemState.Skip时，[nextLabel](StepperItem.md#ZH-CN_TOPIC_0000002553360855__nextlabeldeprecated)被点击时触发该回调。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

从API version 8开始支持，从API version 22开始废弃，建议使用[onChange](Swiper.md#ZH-CN_TOPIC_0000002522240824__onchange)替代。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | () => void | 是 | 当前显示的StepperItem状态为ItemState.Skip时，nextLabel被点击时触发该回调。 |

**onChange(deprecated)**

onChange(callback: (prevIndex: number, index: number) => void)

点击当前StepperItem的[prevLabel](StepperItem.md#ZH-CN_TOPIC_0000002553360855__prevlabeldeprecated)进行步骤切换时触发该回调；或点击当前StepperItem的[nextLabel](StepperItem.md#ZH-CN_TOPIC_0000002553360855__nextlabeldeprecated)，当前页面不为步骤导航器最后一个StepperItem且[ItemState](StepperItem.md#ZH-CN_TOPIC_0000002553360855__itemstate枚举说明)属性为Normal时，触发该回调。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

从API version 8开始支持，从API version 22开始废弃，建议使用[onChange](Swiper.md#ZH-CN_TOPIC_0000002522240824__onchange)替代。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| prevIndex | number | 是 | 切换前的步骤页索引值。 取值范围：[0, +∞) |
| index | number | 是 | 切换后的步骤页（前一页或者下一页）索引值。 取值范围：[0, +∞) |

**onNext(deprecated)**

onNext(callback: (index: number, pendingIndex: number) => void)

点击StepperItem的[nextLabel](StepperItem.md#ZH-CN_TOPIC_0000002553360855__nextlabeldeprecated)切换下一步骤时，当前页面不为步骤导航器最后一个StepperItem且[ItemState](StepperItem.md#ZH-CN_TOPIC_0000002553360855__itemstate枚举说明)属性为Normal时，触发该回调。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

从API version 8开始支持，从API version 22开始废弃，建议使用[onChange](Swiper.md#ZH-CN_TOPIC_0000002522240824__onchange)替代。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 当前步骤页索引值。 |
| pendingIndex | number | 是 | 下一步骤页索引值。 |

**onPrevious(deprecated)**

onPrevious(callback: (index: number, pendingIndex: number) => void)

点击StepperItem的[prevLabel](StepperItem.md#ZH-CN_TOPIC_0000002553360855__prevlabeldeprecated)切换上一步骤时触发该回调。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

从API version 8开始支持，从API version 22开始废弃，建议使用[onChange](Swiper.md#ZH-CN_TOPIC_0000002522240824__onchange)替代。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 当前步骤页索引值。 |
| pendingIndex | number | 是 | 上一步骤页索引值。 |

**示例**

**示例1（使用Stepper）**

该示例主要演示如何使用步骤导航器组件。

```ets
// xxx.ets
@Styles function itemStyle () {
  .width(336)
  .height(621)
  .margin({ top: 48, left: 12 })
  .borderRadius(24)
  .backgroundColor('#FFFFFF')
}

@Extend(Text) function itemTextStyle () {
  .fontColor('#182431')
  .fontSize(36)
  .fontWeight(500)
  .opacity(0.4)
  .margin({ top: 82, bottom: 40 })
}

@Entry
@Component
struct StepperExample {
  @State currentIndex: number = 0;
  @State firstState: ItemState = ItemState.Normal;
  @State secondState: ItemState = ItemState.Normal;
  @State thirdState: ItemState = ItemState.Normal;

  build() {
    Stepper({
      index: this.currentIndex
    }) {
      // 第一个步骤页
      StepperItem() {
        Column() {
          Text('Page One')
            .itemTextStyle()
          Button('change status:' + this.firstState)
            .backgroundColor('#007dFF')
            .onClick(() => {
              this.firstState = this.firstState === ItemState.Skip ? ItemState.Normal : ItemState.Skip;
            })
        }.itemStyle()
      }
      .nextLabel('Next')
      .status(this.firstState)
      // 第二个步骤页
      StepperItem() {
        Column() {
          Text('Page Two')
            .itemTextStyle()
          Button('change status:' + this.secondState)
            .backgroundColor('#007dFF')
            .onClick(() => {
              this.secondState = this.secondState === ItemState.Disabled ? ItemState.Normal : ItemState.Disabled;
            })
        }.itemStyle()
      }
      .nextLabel('Next')
      .prevLabel('Previous')
      .status(this.secondState)
      // 第三个步骤页
      StepperItem() {
        Column() {
          Text('Page Three')
            .itemTextStyle()
          Button('change status:' + this.thirdState)
            .backgroundColor('#007dFF')
            .onClick(() => {
              this.thirdState = this.thirdState === ItemState.Waiting ? ItemState.Normal : ItemState.Waiting;
            })
        }.itemStyle()
      }
      .status(this.thirdState)
      // 第四个步骤页
      StepperItem() {
        Column() {
          Text('Page Four')
            .itemTextStyle()
        }.itemStyle()
      }
    .backgroundColor('#F1F3F5')
    .onFinish(() => {
      // 此处可处理点击最后一页的Finish时的逻辑，例如路由跳转等
      console.info('onFinish');
    })
    .onSkip(() => {
      // 此处可处理点击跳过时的逻辑，例如动态修改Stepper的index值使其跳转到某一步骤页等
      console.info('onSkip');
    })
    .onChange((prevIndex?: number, index?: number) => {
      if(index){
        this.currentIndex = index;
      }
    })
  }
```

![image](public_sys-resources/zh-cn_image_0000002522085440.webp)

**示例2（使用Swiper替代Stepper）**

该示例主要演示如何使用Swiper组件实现Stepper组件的功能，示例效果图同示例1。

```ets
@Styles
function itemStyle() {
  .width(336)
  .height(621)
  .margin({ top: 48, left: 12 })
  .borderRadius(24)
  .backgroundColor('#FFFFFF')
}

@Extend(Text)
function itemTextStyle() {
  .fontColor('#182431')
  .fontSize(36)
  .fontWeight(500)
  .opacity(0.4)
  .margin({ top: 82, bottom: 40 })
}

@Entry
@Component
struct StepperExample {
  @State currentIndex: number = 0;
  @State status: number = 0;
  @State nextLabel: string = "Next";
  @State prevLabel: string = "Previous";
  private swiperController: SwiperController = new SwiperController();

  build() {
    Column() {
      Swiper(this.swiperController) {
        // 第一个步骤页
        Column() {
          Text('Page One')
            .itemTextStyle()
          Button('change status:' + this.status)
            .backgroundColor('#007dFF')
            .onClick(() => {
              if (this.status < 3) {
                this.status += 1
              } else {
                this.status = 0
              }
            })
        }.itemStyle()
        // 第二个步骤页
        Column() {
          Text('Page Two')
            .itemTextStyle()
          Button('change status:' + this.status)
            .backgroundColor('#007dFF')
            .onClick(() => {
              if (this.status < 3) {
                this.status += 1
              } else {
                this.status = 0
              }
            })
        }.itemStyle()
        // 第三个步骤页
        Column() {
          Text('Page Three')
            .itemTextStyle()
          Button('change status:' + this.status)
            .backgroundColor('#007dFF')
            .onClick(() => {
              if (this.status < 3) {
                this.status += 1
              } else {
                this.status = 0
              }
            })
        }.itemStyle()
        // 第四个步骤页
        Column() {
          Text('Page Four')
            .itemTextStyle()
        }.itemStyle()
      }
      .index(this.currentIndex)
      .disableSwipe(true)
      .loop(false)
      .indicator(false)
      .backgroundColor('#fff5f2f2')
      .onChange((index) => {
        console.info("Changed")
        this.currentIndex = index
        this.nextLabel = this.currentIndex == 2 ? "下一步" : "Next"
        this.prevLabel = this.currentIndex == 2 ? "返回" : "Previous"
      })
      // 底部按钮
      Row() {
        if (this.currentIndex > 0) {
          Row() {
            SymbolGlyph($r("sys.symbol.chevron_left"))
              .fontSize(20)
              .margin({ right: 5 })
            Text(this.prevLabel)
            // 使用这里的onClick替代原Stepper的onPrevious
              .onClick(() => {
                this.swiperController.showPrevious()
              })
          }
          .justifyContent(FlexAlign.Start)
          .width(100)
          .height(20)
          .position({ left: 20 })
        }
        Row() {
          if (this.currentIndex == 3) {
            Text("开始")
            // 使用这里的onClick替代原Stepper的onFinish
              .onClick(() => {
                console.info("Finish")
              })
          } else if (this.status == 0) {
            Text(this.nextLabel)
            // 使用这里的onClick替代原Stepper的onNext
              .onClick(() => {
                this.swiperController.showNext()
              })
            SymbolGlyph($r("sys.symbol.chevron_right"))
              .fontSize(20)
              .margin({ left: 5 })
          } else if (this.status == 1) {
            Text(this.nextLabel)
              .fontColor('#ff818181')
            SymbolGlyph($r("sys.symbol.chevron_right"))
              .fontSize(20)
              .fontColor(['#ff818181'])
              .margin({ left: 5 })
          } else if (this.status == 2) {
            LoadingProgress()
              .width(25)
          } else if (this.status == 3) {
            Text("跳过")
            // 使用这里的onClick替代原Stepper的onSkip
              .onClick(() => {
                console.info("Skip")
              })
            SymbolGlyph($r("sys.symbol.chevron_right"))
              .fontSize(20)
              .margin({ left: 5 })
          }
        .justifyContent(FlexAlign.End)
        .width(100)
        .height(20)
        .position({ right: 20 })
      }
      .backgroundColor('#fff5f2f2')
      .position({ bottom: 30 })
      .width("100%")
    }
    .backgroundColor('#fff5f2f2')
    .width("100%")
    .height("100%")
  }
```