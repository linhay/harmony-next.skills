# GridCol

栅格子组件，必须作为栅格容器组件([GridRow](GridRow.md))的子组件使用。

该组件从API version 9开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

#### 子组件

可以包含单个子组件。

#### 接口

GridCol(option?: GridColOptions)

栅格列布局组件。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明option[GridColOptions](#ZH-CN_TOPIC_0000002497444890__gridcoloptions对象说明)否栅格布局子组件参数。

#### GridColOptions对象说明

设置栅格列布局组件布局选项。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明spannumber | [GridColColumnOption](#ZH-CN_TOPIC_0000002497444890__gridcolcolumnoption)否是

栅格子组件占用栅格容器组件的列数。span为0表示该元素不参与布局计算，即不会被渲染。

取值为非负整数，默认值为1

非法值：按默认值处理。

offsetnumber | [GridColColumnOption](#ZH-CN_TOPIC_0000002497444890__gridcolcolumnoption)否是

栅格子组件相对于原本位置偏移的列数。

取值为非负整数，默认值为0

非法值：按默认值处理。

ordernumber | [GridColColumnOption](#ZH-CN_TOPIC_0000002497444890__gridcolcolumnoption)否是

元素的序号，根据栅格子组件的序号，从小到大对栅格子组件做排序。

取值为非负整数，默认值为0。

非法值：按默认值处理。

**说明：**

当子组件不设置order或者设置相同的order，子组件按照代码顺序展示。

当子组件部分设置order，部分不设置order时，未设置order的子组件依次排序靠前，设置了order的子组件按照数值从小到大排列。

span、offset、order属性按照xs、sm、md、lg、xl、xxl的顺序具有“继承性”，未设置值的断点将会从前一个断点取值。

API version 20之后，span的继承规则见[GridColColumnOption](#ZH-CN_TOPIC_0000002497444890__gridcolcolumnoption)。

#### 属性

除支持[通用属性](../misc/通用属性.md)外，还支持以下属性：

#### span

span(value: number | GridColColumnOption)

设置占用列数。span为0，意味着该元素不参与布局计算，即不会被渲染。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明valuenumber | [GridColColumnOption](#ZH-CN_TOPIC_0000002497444890__gridcolcolumnoption)是

占用列数。

取值为非负整数，默认值为1。

非法值：按默认值处理。

#### gridColOffset

gridColOffset(value: number | GridColColumnOption)

设置相对于前一个栅格子组件偏移的列数。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明valuenumber | [GridColColumnOption](#ZH-CN_TOPIC_0000002497444890__gridcolcolumnoption)是

相对于前一个栅格子组件偏移的列数。

取值为非负整数，默认值：0

非法值：按默认值处理。

#### order

order(value: number | GridColColumnOption)

设置栅格子组件的序号，根据序号从小到大对栅格子组件进行排序。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明valuenumber | [GridColColumnOption](#ZH-CN_TOPIC_0000002497444890__gridcolcolumnoption)是

元素的序号，根据栅格子组件的序号，从小到大对栅格子组件做排序。

取值为非负整数，默认值：0

非法值：按默认值处理。

#### GridColColumnOption

用于自定义指定在不同宽度设备类型上，栅格子组件占据的栅格数量单位。

- API version 20之前，仅配置部分断点下GridCol组件所占列数，取已配置的更小断点的列数补全未配置的列数。若未配置更小断点的列数，取默认值1。

```ets
  span: {xs:2, md:4, lg:8} // 等于配置 span: {xs:2, sm:2, md:4, lg:8, xl:8, xxl:8}
  span: {md:4, lg:8} // 等于配置 span: {xs:1, sm:1, md:4, lg:8, xl:8, xxl:8}
```

- API version 20及以后，仅配置部分断点下GridCol组件所占列数，取已配置的更小断点的列数补全未配置的列数。若未配置更小断点的列数，取已配置的更大断点的列数补全未配置的列数。

```ets
  span: {xs:2, md:4, lg:8} // 等于配置 span: {xs:2, sm:2, md:4, lg:8, xl:8, xxl:8}
  span: {md:4, lg:8} // 等于配置 span: {xs:4, sm:4, md:4, lg:8, xl:8, xxl:8}
```

- 建议手动配置不同断点下GridCol组件所占列数，避免默认补全列数的布局效果不符合预期。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明xsnumber否是在栅格大小为xs的设备上，栅格容器组件的栅格列数。smnumber否是在栅格大小为sm的设备上，栅格容器组件的栅格列数。mdnumber否是在栅格大小为md的设备上，栅格容器组件的栅格列数。lgnumber否是在栅格大小为lg的设备上，栅格容器组件的栅格列数。xlnumber否是在栅格大小为xl的设备上，栅格容器组件的栅格列数。xxlnumber否是在栅格大小为xxl的设备上，栅格容器组件的栅格列数。

#### 事件

支持[通用事件](../misc/通用事件.md)。

#### 示例

GridCol的基本用法示例。

```ets
// xxx.ets
@Entry
@Component
struct GridColExample {
  @State bgColors: Color[] =
    [Color.Red, Color.Orange, Color.Yellow, Color.Green, Color.Pink, Color.Grey, Color.Blue, Color.Brown]
  @State currentBp: string = 'unknown'

  build() {
    Column() {
      GridRow({
        columns: 5,
        gutter: { x: 5, y: 10 },
        breakpoints: {
          value: ['400vp', '600vp', '800vp'],
          reference: BreakpointsReference.WindowSize
        },
        direction: GridRowDirection.Row
      }) {
        ForEach(this.bgColors, (color: Color) => {
          GridCol({
            span: { xs: 1, sm: 2, md: 3, lg: 4 },
            offset: 0,
            order: 0
          }) {
            Row().width('100%').height('20vp')
          }.borderColor(color).borderWidth(2)
        })
      }.width('100%').height('100%')
      .onBreakpointChange((breakpoint) => {
        this.currentBp = breakpoint
      })
    }.width('80%').margin({ left: 10, top: 5, bottom: 5 }).height(200)
    .border({ color: '#880606', width: 2 })
  }
}
```