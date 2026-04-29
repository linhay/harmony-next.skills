# Arc[Scroll](Scroll.md)Bar

弧形滚动条组件ArcScrollBar，用于配合可滚动组件使用，如[ArcList](Arc[List](list.md).md)、[List](List.md)、[Grid](Grid.md)、[Scroll](Scroll.md)、[WaterFlow](WaterFlow.md)。


- 该组件从API version 18开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

- ArcScrollBar不设置宽高时，采用父组件[布局约束](FrameNode.md#ZH-CN_TOPIC_0000002522240744__layoutconstraint12)中的maxSize作为宽高。如果ArcScrollBar的父组件存在可滚动组件，如[ArcList](Arc[List](list.md).md)、[List](List.md)、[Grid](Grid.md)、[Scroll](Scroll.md)、[WaterFlow](WaterFlow.md)，建议设置ArcScrollBar宽高，否则ArcScrollBar的宽高可能为无穷大。

- 该组件支持在Phone、PC/2in1、Tablet、TV、Wearable设备上使用。API version 22及以前版本，在Phone、PC/2in1、Tablet、TV上使用会编译告警，但可以正常运行。

#### 子组件

不包含子组件。

#### 接口

Arc[Scroll](Scroll.md)Bar(options: ArcScrollBarOptions)

Arc[Scroll](Scroll.md)Bar的构造函数。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | Arc[Scroll](Scroll.md)BarOptions | 是 | 滚动条组件参数。 |

#### Arc[Scroll](Scroll.md)BarOptions

Arc[Scroll](Scroll.md)Bar的构造函数参数。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| scroller | [Scroller](Scroll.md#ZH-CN_TOPIC_0000002497444896__scroller) | 否 | 否 | 可滚动组件的控制器，用于与可滚动组件进行绑定。 |
| state | [BarState](枚举说明.md#ZH-CN_TOPIC_0000002529284967__barstate) | 否 | 是 | 滚动条状态。 默认值：BarState.Auto |


Arc[Scroll](Scroll.md)Bar与可滚动组件需通过scroller进行绑定后方能实现联动，且ArcScrollBar与可滚动组件仅限于一对一的绑定方式。

#### 示例

该示例通过ArcScrollBar与[Scroll](Scroll.md)组件联动，设置了弧形外置滚动条。

```ets
import { ArcScrollBar } from '@kit.ArkUI';

@Entry
@Component
struct ArcScrollBarExample {
  private scroller: Scroller = new Scroller();
  private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];

  build() {
    Stack({ alignContent: Alignment.Center }) {
      Scroll(this.scroller) {
        Flex({ direction: FlexDirection.Column }) {
          ForEach(this.arr, (item: number) => {
            Row() {
              Text(item.toString())
                .width('80%')
                .height(60)
                .backgroundColor('#3366CC')
                .borderRadius(15)
                .fontSize(16)
                .textAlign(TextAlign.Center)
                .margin({ top: 5 })
            }
          }, (item: number) => item.toString())
        }.margin({ right: 15 })
      }
      .width('90%')
      .scrollBar(BarState.Off)

      ArcScrollBar({ scroller: this.scroller, state: BarState.Auto })
    }
    .width('100%')
    .height('100%')
  }
```

![image](public_sys-resources/zh-cn_image_0000002553364843.webp)
