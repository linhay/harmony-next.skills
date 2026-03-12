# GridContainer

纵向排布栅格布局容器，仅在栅格布局场景中使用。

 从API version 9开始，该组件不再维护，推荐使用新组件[GridCol](GridCol.md)、[GridRow](GridRow.md)。

 该组件从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

#### 子组件

可以包含子组件。

#### 接口

GridContainer(value?: GridContainerOptions)

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明valueGridContainerOptions否GridContainer参数。

#### GridContainerOptions对象说明

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明columnsnumber | 'auto'否是

当前布局总列数。

默认值：'auto'

sizeTypeSizeType否是

选用设备宽度类型。

默认值：SizeType.Auto

gutternumber | string否是栅格布局列间距，不支持百分比。marginnumber | string否是栅格布局两侧间距，不支持百分比。

#### SizeType枚举说明

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称说明XS最小宽度类型设备。SM小宽度类型设备。MD中等宽度类型设备。LG大宽度类型设备。Auto根据设备类型进行选择。

#### 属性

支持[通用属性](通用属性.md)和Column组件的[属性方法](Column.md#ZH-CN_TOPIC_0000002529444831__属性)。

#### 事件

支持[通用事件](通用事件.md)。

#### 示例

```ets
// xxx.ets
@Entry
@Component
struct GridContainerExample {
  @State sizeType: SizeType = SizeType.XS

  build() {
    Column({ space: 5 }) {
      GridContainer({ columns: 12, sizeType: this.sizeType, gutter: 10, margin: 20 }) {
        Row() {
          Text('1')
            .useSizeType({
              xs: { span: 6, offset: 0 },
              sm: { span: 2, offset: 0 },
              md: { span: 2, offset: 0 },
              lg: { span: 2, offset: 0 }
            })
            .height(50).backgroundColor(0x4682B4).textAlign(TextAlign.Center)
          Text('2')
            .useSizeType({
              xs: { span: 2, offset: 6 },
              sm: { span: 6, offset: 2 },
              md: { span: 2, offset: 2 },
              lg: { span: 2, offset: 2 }
            })
            .height(50).backgroundColor(0x00BFFF).textAlign(TextAlign.Center)
          Text('3')
            .useSizeType({
              xs: { span: 2, offset: 8 },
              sm: { span: 2, offset: 8 },
              md: { span: 6, offset: 4 },
              lg: { span: 2, offset: 4 }
            })
            .height(50).backgroundColor(0x4682B4).textAlign(TextAlign.Center)
          Text('4')
            .useSizeType({
              xs: { span: 2, offset: 10 },
              sm: { span: 2, offset: 10 },
              md: { span: 2, offset: 10 },
              lg: { span: 6, offset: 6 }
            })
            .height(50).backgroundColor(0x00BFFF).textAlign(TextAlign.Center)
        }
      }.width('90%')

      Text('Click Simulate to change the device width').fontSize(9).width('90%').fontColor(0xCCCCCC)
      Row() {
        Button('XS')
          .onClick(() => {
            this.sizeType = SizeType.XS
          }).backgroundColor(0x317aff)
        Button('SM')
          .onClick(() => {
            this.sizeType = SizeType.SM
          }).backgroundColor(0x317aff)
        Button('MD')
          .onClick(() => {
            this.sizeType = SizeType.MD
          }).backgroundColor(0x317aff)
        Button('LG')
          .onClick(() => {
            this.sizeType = SizeType.LG
          }).backgroundColor(0x317aff)
      }
    }.width('100%').margin({ top: 5 })
  }
}
```