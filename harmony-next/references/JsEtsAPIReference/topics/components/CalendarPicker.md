# CalendarPicker

日历选择器组件，提供下拉日历弹窗，可以让用户选择日期。

该组件从API version 10开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

#### 子组件

无

#### 接口

CalendarPicker(options?: CalendarOptions)

日历选择器。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

**参数：**

参数名类型必填说明options[CalendarOptions](#ZH-CN_TOPIC_0000002497444908__calendaroptions对象说明)否配置日历选择器组件的参数。

#### 属性

除支持[通用属性](../misc/通用属性.md)外，还支持以下属性：

#### edgeAlign

edgeAlign(alignType: CalendarAlign, offset?: Offset)

设置选择器与入口组件的对齐方式。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

**参数：**

参数名类型必填说明alignType[CalendarAlign](#ZH-CN_TOPIC_0000002497444908__calendaralign枚举说明)是

对齐方式的类型。

默认值：CalendarAlign.END

offset[Offset](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__offset)否

按照对齐方式对齐后，选择器相对入口组件的偏移量。

默认值：{dx: 0, dy: 0}

#### edgeAlign18+

edgeAlign(alignType: Optional<CalendarAlign>, offset?: Offset)

设置选择器与入口组件的对齐方式。与[edgeAlign](#ZH-CN_TOPIC_0000002497444908__edgealign)相比，alignType参数新增了对undefined类型的支持。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

**参数：**

参数名类型必填说明alignType[Optional](../misc/自定义属性设置.md#ZH-CN_TOPIC_0000002529284845__optionalt12)<[CalendarAlign](#ZH-CN_TOPIC_0000002497444908__calendaralign枚举说明)>是

对齐方式的类型。

默认值：CalendarAlign.END

当alignType的值为undefined时，使用默认值。

offset[Offset](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__offset)否

按照对齐方式对齐后，选择器相对入口组件的偏移量。

默认值：{dx: 0, dy: 0}

#### textStyle

textStyle(value: PickerTextStyle)

入口区的文本颜色、字号、字体粗细。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

**参数：**

参数名类型必填说明value[PickerTextStyle](选择器（Picker）公共接口.md#ZH-CN_TOPIC_0000002529444857__pickertextstyle对象说明)是

设置入口区的文本颜色、字号、字体粗细。

默认值：

{

color: '#ff182431',

font: {

size: '16fp',

weight: FontWeight.Regular

}

}

#### textStyle18+

textStyle(style: Optional<PickerTextStyle>)

入口区的文本颜色、字号、字体粗细。与[textStyle](#ZH-CN_TOPIC_0000002497444908__textstyle)相比，style参数新增了对undefined类型的支持。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

**参数：**

参数名类型必填说明style[Optional](../misc/自定义属性设置.md#ZH-CN_TOPIC_0000002529284845__optionalt12)<[PickerTextStyle](选择器（Picker）公共接口.md#ZH-CN_TOPIC_0000002529444857__pickertextstyle对象说明)>是

设置入口区的文本颜色、字号、字体粗细。

默认值：

{

color: '#ff182431',

font: {

size: '16fp',

weight: FontWeight.Regular

}

}

当style的值为undefined时，使用默认值。

#### markToday19+

markToday(enabled: boolean)

设置日历选择器中系统当前日期是否保持高亮显示。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

**参数：**

参数名类型必填说明enabledboolean是

设置日历选择器中系统当前日期是否保持高亮显示。

- true：系统当前日期在日历选择器内保持高亮显示。

- false：系统当前日期在日历选择器内不保持高亮显示。

默认值：false

#### 事件

除支持[通用事件](../misc/通用事件.md)，还支持以下事件：

#### onChange

onChange(callback: Callback<Date>)

选择日期时触发该事件。不能通过双向绑定的状态变量触发。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

**参数：**

参数名类型必填说明callback[Callback](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__callback12)<Date>是选中的日期值。

#### onChange18+

onChange(callback: Optional<Callback<Date>>)

选择日期时触发该事件。不能通过双向绑定的状态变量触发。与[onChange](#ZH-CN_TOPIC_0000002497444908__onchange)相比，callback参数新增了对undefined类型的支持。

从API version 20开始，该接口支持在[attributeModifier](../misc/动态属性设置.md#ZH-CN_TOPIC_0000002529284843__attributemodifier)中调用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

**参数：**

参数名类型必填说明callback[Optional](../misc/自定义属性设置.md#ZH-CN_TOPIC_0000002529284845__optionalt12)<[Callback](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__callback12)<Date>>是

选中的日期值。

当callback的值为undefined时，不使用回调函数。

#### CalendarOptions对象说明

日历选择器组件的参数说明。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

名称类型只读可选说明hintRadiusnumber | [Resource](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resource)否是

描述日期选中态底板样式。

取值范围：[0.0, 16.0]

单位：vp

默认值：16.0，即底板样式为圆形。

**说明：**

当hintRadius为0.0时表示底板样式为直角矩形；当hintRadius为(0.0, 16.0)时，底板样式为圆角矩形；当hintRadius为负数或大于16.0时，恢复成默认值16.0。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

selectedDate否是

设置选中项的日期。选中的日期未设置或日期格式不符合规范则为默认值。

默认值：当前系统日期。

取值范围：[Date('0001-01-01'), Date('5000-12-31')]

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

start18+Date否是

设置开始日期。

默认值：Date('0001-01-01')

取值范围：[Date('0001-01-01'), Date('5000-12-31')]

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

end18+Date否是

设置结束日期。

默认值：Date('5000-12-31')

取值范围：[Date('0001-01-01'), Date('5000-12-31')]

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

disabledDateRange19+[DateRange](选择器（Picker）公共接口.md#ZH-CN_TOPIC_0000002529444857__daterange19对象说明)[]否是

设置禁用日期区间。

**说明：**

1. 若日期区间内的开始日期或结束日期未设置或设置为异常值，则该日期区间无效。

2. 若在日期区间内，结束日期早于开始日期，则该日期区间无效。

3. 当在入口区选定某日期，通过上下箭头调整日期进行增加或减少操作时，若遇到禁用日期，系统将自动跳过整个禁用区间。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**start和end设置规则：**

场景说明start日期晚于end日期start日期、end日期都设置无效，选中日期为默认值选中日期早于start日期选中日期为start日期选中日期晚于end日期选中日期为end日期start日期晚于当前系统日期，选中日期未设置选中日期为start日期end日期早于当前系统日期，选中日期未设置选中日期为end日期日期格式不符合规范，如‘1999-13-32’start日期或end日期设置无效，选中日期取默认值

#### CalendarAlign枚举说明

对齐方式类型。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

名称值说明START0设置选择器与入口组件的对齐方式为左对齐。CENTER1设置选择器与入口组件的对齐方式为居中对齐。END2设置选择器与入口组件的对齐方式为右对齐。

#### 示例

#### 示例1（设置下拉日历弹窗）

该示例实现了日历选择器组件，提供下拉日历弹窗。

```ets
// xxx.ets
@Entry
@Component
struct CalendarPickerExample {
  private selectedDate: Date = new Date('2024-03-05');

  build() {
    Column() {
      Column() {
        CalendarPicker({ hintRadius: 10, selected: this.selectedDate })
          .edgeAlign(CalendarAlign.END)
          .textStyle({ color: "#ff182431", font: { size: 20, weight: FontWeight.Normal } })
          .margin(10)
          .onChange((value) => {
            console.info(`CalendarPicker onChange: ${value.toString()}`);
          })
      }.alignItems(HorizontalAlign.End).width("100%")

      Text('日历日期选择器').fontSize(30)
    }.width('100%').margin({ top: 350 })
  }
}
```

#### 示例2（设置开始日期和结束日期）

该示例通过start和end设置日历选择器的开始日期和结束日期。

从API version 18开始，[CalendarOptions](#ZH-CN_TOPIC_0000002497444908__calendaroptions对象说明)中新增了start、end属性。

```ets
// xxx.ets
@Entry
@Component
struct CalendarPickerExample {
  private selectedDate: Date = new Date('2025-01-15');
  private startDate: Date = new Date('2025-01-05');
  private endDate: Date = new Date('2025-01-25');

  build() {
    Column() {
      Column() {
        CalendarPicker({ hintRadius: 10, selected: this.selectedDate, start: this.startDate, end: this.endDate })
          .edgeAlign(CalendarAlign.END)
          .textStyle({ color: "#ff182431", font: { size: 20, weight: FontWeight.Normal } })
          .margin(10)
          .onChange((value) => {
            console.info(`CalendarPicker onChange: ${value.toString()}`);
          })
      }.alignItems(HorizontalAlign.End).width("100%")
    }.width('100%').margin({ top: 350 })
  }
}
```

#### 示例3（设置日历选择器在系统当前日期时，保持高亮显示和禁用日期区间）

该示例通过[markToday](#ZH-CN_TOPIC_0000002497444908__marktoday19)设置日历选择器在系统当前日期时，开启保持高亮显示，同时，通过[disabledDateRange](#ZH-CN_TOPIC_0000002497444908__calendaroptions对象说明)设置日历选择器的禁用日期区间。

从API version 19开始，新增了markToday接口。

```ets
// xxx.ets
@Entry
@Component
struct CalendarPickerExample {
  private disabledDateRange: DateRange[] = [
    { start: new Date('2025-01-01'), end: new Date('2025-01-02') },
    { start: new Date('2025-01-09'), end: new Date('2025-01-10') },
    { start: new Date('2025-01-15'), end: new Date('2025-01-16') },
    { start: new Date('2025-01-19'), end: new Date('2025-01-19') },
    { start: new Date('2025-01-22'), end: new Date('2025-01-25') }
  ];

  build() {
    Column() {
      CalendarPicker({ disabledDateRange: this.disabledDateRange })
        .margin(10)
        .markToday(true)
        .onChange((value) => {
          console.info(`CalendarPicker onChange: ${value.toString()}`);
        })
    }.alignItems(HorizontalAlign.End).width('100%')
  }
}
```