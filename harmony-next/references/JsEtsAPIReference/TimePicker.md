# TimePicker

滑动选择时间的组件。

-

该组件从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

-

该组件不建议开发者在动效过程中修改属性数据。

-

最大显示行数在横、竖屏模式下存在差异。竖屏时默认为5行，横屏时依赖系统配置，未配置时默认显示为3行。可通过如下参数查看具体配置值$r('sys.float.ohos_id_picker_show_count_landscape')。

#### 子组件

无

#### 接口

TimePicker(options?: TimePickerOptions)

创建滑动选择器，默认使用24小时的时间区间。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明options[TimePickerOptions](#ZH-CN_TOPIC_0000002497604888__timepickeroptions对象说明)否配置时间选择组件的参数。

#### TimePickerOptions对象说明

时间选择器组件的参数说明。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明selectedDate否是

设置选中项的时间。

默认值：当前系统时间

从API version 10开始，该参数支持[$$](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-two-way-sync)双向绑定变量。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

format11+[TimePickerFormat](#ZH-CN_TOPIC_0000002497604888__timepickerformat11枚举说明)否是

指定需要显示的TimePicker的格式。

默认值：TimePickerFormat.HOUR_MINUTE

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

start18+Date否是

指定时间选择组件的起始时间。

默认值：Date(0, 0, 0, 0, 0, 0)

**说明：**

1. 仅设置的小时和分钟生效。

2. 设置了start且为非默认值的场景下，loop不生效。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

end18+Date否是

指定时间选择组件的结束时间。

默认值：Date(0, 0, 0, 23, 59, 59)

**说明：**

1. 仅设置的小时和分钟生效。

2. 设置了end且为非默认值的场景下，loop不生效。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

-

在TimePicker组件滑动过程中修改TimePickerOptions中的属性，会导致这些属性无法生效。

-

Date对象用于处理日期和时间，使用方式如下。

**方式1：** new Date()

获取系统当前日期和时间。

**方式2：** new Date(value: number | string)

参数名类型必填说明valuenumber | string是

设置日期格式。

number：毫秒，自1970年1月1日 00:00:00以来的毫秒数。

string：时间格式的字符串，如‘2025-02-20 08:00:00’或‘2025-02-20T08:00:00’。

**方式3：** new Date(year: number, monthIndex: number, date?: number, hours?: number, minutes?: number, seconds?: number, ms?: number)

参数名类型必填说明yearnumber是设置年份，例如2025。monthIndexnumber是设置月份索引，例如2，代表3月份。datenumber否设置日期，例如10。（如果设置hours，则date不能省略）hoursnumber否设置小时，例如15。（如果设置minutes，则hours不能省略）minutesnumber否设置分钟，例如20。（如果设置seconds，则minutes不能省略）secondsnumber否设置秒，例如20。（如果设置ms，则seconds不能省略）msnumber否设置毫秒，例如10。

**起始时间和结束时间的异常情形说明：**

异常情形对应结果起始时间晚于结束时间。起始时间、结束时间都为默认值。选中时间早于起始时间。选中时间为起始时间。选中时间晚于结束时间。选中时间为结束时间。起始时间晚于当前系统时间，选中时间未设置。选中时间为起始时间。结束时间早于当前系统时间，选中时间未设置。选中时间为结束时间。时间格式不符合规范，如'01:61:61'。取默认值。

#### TimePickerFormat11+枚举说明

时间选择器的数据格式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称值说明HOUR_MINUTE-按照小时和分钟进行显示。HOUR_MINUTE_SECOND-按照小时、分钟和秒进行显示。

#### 属性

除支持[通用属性](通用属性.md)外，还支持以下属性：

#### useMilitaryTime

useMilitaryTime(value: boolean)

设置时间是否以24小时制展示，默认以12小时制展示。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明valueboolean是

时间是否以24小时制展示。

- true：时间以24小时制展示。

- false：时间以12小时制展示。

默认值：false

#### useMilitaryTime18+

useMilitaryTime(isMilitaryTime: Optional<boolean>)

设置展示时间是否为24小时制，默认展示时间为12小时制。与[useMilitaryTime](#ZH-CN_TOPIC_0000002497604888__usemilitarytime)相比，isMilitaryTime参数新增了对undefined类型的支持。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明isMilitaryTime[Optional](自定义属性设置.md#ZH-CN_TOPIC_0000002529284845__optionalt12)<boolean>是

展示时间是否为24小时制。

- true：展示时间为24小时制。

- false：展示时间为12小时制。

默认值：false

当isMilitaryTime的值为undefined时，使用默认值。

#### disappearTextStyle10+

disappearTextStyle(value: PickerTextStyle)

设置边缘项（以选中项为基准向上或向下的第二项）的文本颜色、字号、字体粗细。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明value[PickerTextStyle](选择器（Picker）公共接口.md#ZH-CN_TOPIC_0000002529444857__pickertextstyle对象说明)是

边缘项的文本颜色、字号和字体粗细。

默认值：

{

color: '#ff182431',

font: {

size: '14fp',

weight: FontWeight.Regular

}

}

若选中项向上或向下的可视项数低于两项则无对应边缘项。

#### disappearTextStyle18+

disappearTextStyle(style: Optional<PickerTextStyle>)

设置边缘项（以选中项为基准向上或向下的第二项）的文本颜色、字号、字体粗细。与[disappearTextStyle10+](#ZH-CN_TOPIC_0000002497604888__disappeartextstyle10)相比，style参数新增了对undefined类型的支持。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明style[Optional](自定义属性设置.md#ZH-CN_TOPIC_0000002529284845__optionalt12)<[PickerTextStyle](选择器（Picker）公共接口.md#ZH-CN_TOPIC_0000002529444857__pickertextstyle对象说明)>是

边缘项的文本颜色、字号、字体粗细。

默认值：

{

color: '#ff182431',

font: {

size: '14fp',

weight: FontWeight.Regular

}

}

当style的值为undefined时，使用默认值。

若选中项向上或向下的可视项数低于两项则无对应边缘项。

#### textStyle10+

textStyle(value: PickerTextStyle)

设置待选项（以选中项为基准向上或向下的第一项）的文本颜色、字号、字体粗细。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明value[PickerTextStyle](选择器（Picker）公共接口.md#ZH-CN_TOPIC_0000002529444857__pickertextstyle对象说明)是

待选项的文本颜色、字号、字体粗细。

默认值：

{

color: '#ff182431',

font: {

size: '16fp',

weight: FontWeight.Regular

}

}

若选中项向上或向下可视项数低于一项则无对应待选项。

#### textStyle18+

textStyle(style: Optional<PickerTextStyle>)

设置待选项（以选中项为基准向上或向下的第一项）的文本颜色、字号、字体粗细。与[textStyle10+](#ZH-CN_TOPIC_0000002497604888__textstyle10)相比，style参数新增了对undefined类型的支持。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明style[Optional](自定义属性设置.md#ZH-CN_TOPIC_0000002529284845__optionalt12)<[PickerTextStyle](选择器（Picker）公共接口.md#ZH-CN_TOPIC_0000002529444857__pickertextstyle对象说明)>是

待选项的文本颜色、字号、字体粗细。

默认值：

{

color: '#ff182431',

font: {

size: '16fp',

weight: FontWeight.Regular

}

}

当style的值为undefined时，使用默认值。

若选中项向上或向下可视项数低于一项则无对应待选项。

#### selectedTextStyle10+

selectedTextStyle(value: PickerTextStyle)

设置选中项的文本颜色、字号和字体粗细。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该属性在Wearable设备上使用无效果，在其他设备中可正常生效。

**参数：**

参数名类型必填说明value[PickerTextStyle](选择器（Picker）公共接口.md#ZH-CN_TOPIC_0000002529444857__pickertextstyle对象说明)是

选中项的文本颜色、字号、字体粗细。

默认值：

{

color: '#ff007dff',

font: {

size: '20fp',

weight: FontWeight.Medium

}

}

#### selectedTextStyle18+

selectedTextStyle(style: Optional<PickerTextStyle>)

设置选中项的文本颜色、字号及字体粗细。与[selectedTextStyle10+](#ZH-CN_TOPIC_0000002497604888__selectedtextstyle10)相比，style参数新增了对undefined类型的支持

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该属性在Wearable设备上使用无效果，在其他设备中可正常生效。

**参数：**

参数名类型必填说明style[Optional](自定义属性设置.md#ZH-CN_TOPIC_0000002529284845__optionalt12)<[PickerTextStyle](选择器（Picker）公共接口.md#ZH-CN_TOPIC_0000002529444857__pickertextstyle对象说明)>是

选中项的文本颜色、字号、字体粗细。

默认值：

{

color: '#ff007dff',

font: {

size: '20fp',

weight: FontWeight.Medium

}

}

当style的值为undefined时，使用默认值。

#### loop11+

loop(value: boolean)

设置是否启用循环模式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明valueboolean是

是否启用循环模式。

- true：启用循环模式。

- false：不启用循环模式。

默认值：true

#### loop18+

loop(isLoop: Optional<boolean>)

设置是否启用循环模式。与[loop11+](#ZH-CN_TOPIC_0000002497604888__loop11)相比，isLoop参数新增了对undefined类型的支持。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明isLoop[Optional](自定义属性设置.md#ZH-CN_TOPIC_0000002529284845__optionalt12)<boolean>是

是否启用循环模式。

- true：启用循环模式。

- false：不启用循环模式。

默认值：true

当isLoop的值为undefined时，使用默认值。

#### dateTimeOptions12+

dateTimeOptions(value: DateTimeOptions)

设置时分秒是否显示前导0。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明value[DateTimeOptions](#ZH-CN_TOPIC_0000002497604888__datetimeoptions12类型说明)是

设置时分秒是否显示前导0。

默认值：

hour: 24小时制默认为"2-digit"，设置hour是否按照2位数字显示，如果实际数值小于10，则会补充前导0并显示，即为"0X"；12小时制默认为"numeric"，即没有前导0。

minute: 默认为"2-digit"，设置minute是否按照2位数字显示，如果实际数值小于10，则会补充前导0并显示，即为"0X"。

second: 默认为"2-digit"，设置second是否按照2位数字显示，如果实际数值小于10，则会补充前导0并显示，即为"0X"。

当hour、minute、second的值设置为undefined时，显示效果与其默认值规则一致。

#### dateTimeOptions18+

dateTimeOptions(timeFormat: Optional<DateTimeOptions>)

设置时分秒是否显示前导0。与[dateTimeOptions12+](#ZH-CN_TOPIC_0000002497604888__datetimeoptions12)相比，timeFormat参数新增了对undefined类型的支持。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明timeFormat[Optional](自定义属性设置.md#ZH-CN_TOPIC_0000002529284845__optionalt12)<[DateTimeOptions](#ZH-CN_TOPIC_0000002497604888__datetimeoptions12类型说明)>是

设置时分秒是否显示前导0，目前只支持设置hour、minute和second参数。

默认值：

hour: 24小时制默认为"2-digit"，设置hour是否按照2位数字显示，如果实际数值小于10，则会补充前导0并显示，即为"0X"；12小时制默认为"numeric"，即没有前导0。

minute: 默认为"2-digit"，设置minute是否按照2位数字显示，如果实际数值小于10，则会补充前导0并显示，即为"0X"。

second: 默认为"2-digit"，设置second是否按照2位数字显示，如果实际数值小于10，则会补充前导0并显示，即为"0X"。

当hour、minute、second的值设置为undefined时，显示效果与其默认值规则一致。

#### enableHapticFeedback12+

enableHapticFeedback(enable: boolean)

设置是否支持触控反馈。

从API version 18开始，该接口支持在[attributeModifier](动态属性设置.md#ZH-CN_TOPIC_0000002529284843__attributemodifier)中调用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明enableboolean是

设置是否开启触控反馈。

- true：开启触控反馈。

- false：不开启触控反馈。

默认值：true

设置为true后，其生效情况取决于系统的硬件是否支持。

开启触控反馈时，需要在工程的src/main/module.json5文件的"module"内配置requestPermissions字段开启振动权限，配置如下：

```ets
"requestPermissions": [
   {
      "name": "ohos.permission.VIBRATE",
   }
]
```

#### enableHapticFeedback18+

enableHapticFeedback(enable: Optional<boolean>)

设置是否支持触控反馈。与[enableHapticFeedback12+](#ZH-CN_TOPIC_0000002497604888__enablehapticfeedback12)相比，enable参数新增了对undefined类型的支持。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明enable[Optional](自定义属性设置.md#ZH-CN_TOPIC_0000002529284845__optionalt12)<boolean>是

设置是否开启触控反馈。

- true：开启触控反馈。

- false：不开启触控反馈。

默认值：true

当enable的值为undefined时，使用默认值。

设置为true后，其生效情况取决于系统的硬件是否支持。

开启触控反馈时，需要在工程的src/main/module.json5文件的"module"内配置requestPermissions字段开启振动权限，配置如下：

```ets
"requestPermissions": [
   {
      "name": "ohos.permission.VIBRATE",
   }
]
```

#### enableCascade18+

enableCascade(enabled: boolean)

设置上午和下午的标识是否根据小时数自动切换，仅在useMilitaryTime设置为false时生效。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明enabledboolean是

上午和下午的标识是否根据小时数自动切换，仅在useMilitaryTime设置为false时生效。

- true：自动切换。

- false：不自动切换。

默认值：false

当enabled设置为true时，仅在loop参数同时为true时生效。

#### digitalCrownSensitivity18+

digitalCrownSensitivity(sensitivity: Optional<CrownSensitivity>)

设置表冠灵敏度。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明sensitivity[Optional](自定义属性设置.md#ZH-CN_TOPIC_0000002529284845__optionalt12)<[CrownSensitivity](枚举说明.md#ZH-CN_TOPIC_0000002529284967__crownsensitivity18)>是

表冠响应灵敏度。

默认值：CrownSensitivity.MEDIUM，表示响应速度适中。

用于圆形屏幕的穿戴设备。组件响应[表冠事件](表冠事件.md)，需要先获取焦点。

#### 事件

除支持[通用事件](通用事件.md)外，还支持以下事件：

#### onChange

onChange(callback: (value: TimePickerResult ) => void)

滑动TimePicker后，时间选项归位至选中项位置时，触发该回调。不能通过双向绑定的状态变量触发。

回调会在滑动动画结束后触发，如果需要快速获取索引值变化，建议使用[onEnterSelectedArea](#ZH-CN_TOPIC_0000002497604888__onenterselectedarea18)接口。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明value[TimePickerResult](#ZH-CN_TOPIC_0000002497604888__timepickerresult对象说明)是24小时制时间。

#### onChange18+

onChange(callback: Optional<OnTimePickerChangeCallback>)

滑动TimePicker后，时间选项归位至选中项位置时，触发该回调。不能通过双向绑定的状态变量触发。与[onChange](#ZH-CN_TOPIC_0000002497604888__onchange)相比，callback参数新增了对undefined类型的支持。

回调会在滑动动画结束后触发，如果需要快速获取索引值变化，建议使用[onEnterSelectedArea](#ZH-CN_TOPIC_0000002497604888__onenterselectedarea18)接口。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明callback[Optional](自定义属性设置.md#ZH-CN_TOPIC_0000002529284845__optionalt12)<[OnTimePickerChangeCallback](#ZH-CN_TOPIC_0000002497604888__ontimepickerchangecallback18)>是

选择时间时触发该回调。

当callback的值为undefined时，不使用回调函数。

#### onEnterSelectedArea18+

onEnterSelectedArea(callback: Callback<TimePickerResult>)

滑动TimePicker过程中，选项进入分割线区域内，触发该回调。

与[onChange](#ZH-CN_TOPIC_0000002497604888__onchange)事件的差别在于，该事件的触发时机早于[onChange](#ZH-CN_TOPIC_0000002497604888__onchange)事件，当当前滑动列滑动距离超过选中项高度的一半时，选项此时已经进入分割线区域内，会触发该事件。当[enableCascade](#ZH-CN_TOPIC_0000002497604888__enablecascade18)设置为true时，由于上午/下午列与小时列存在联动关系，不建议使用该回调。该回调标识的是滑动过程中选项进入分割线区域内的节点，而联动变化的选项并不涉及滑动，因此，回调的返回值中，仅当前滑动列的值会正常变化，其余未滑动列的值保持不变。

该接口不支持在[attributeModifier](动态属性设置.md#ZH-CN_TOPIC_0000002529284843__attributemodifier)中调用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明callbackCallback<[TimePickerResult](#ZH-CN_TOPIC_0000002497604888__timepickerresult对象说明)>是滑动TimePicker过程中，选项进入分割线区域时触发的回调。

#### DateTimeOptions12+类型说明

type DateTimeOptions = DateTimeOptions

时间、日期格式化时可设置的配置项。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

类型说明[DateTimeOptions](@ohos.intl (国际化-Intl).md#ZH-CN_TOPIC_0000002497605316__datetimeoptionsdeprecated)创建时间、日期格式化对象时可设置的配置项。

#### OnTimePickerChangeCallback18+

type OnTimePickerChangeCallback = (result: TimePickerResult) => void

选择时间时触发该事件。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明result[TimePickerResult](#ZH-CN_TOPIC_0000002497604888__timepickerresult对象说明)是24小时制时间。

#### TimePickerResult对象说明

返回24小时制时间。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明hournumber否否

选中时间的时。

取值范围：[0-23]

minutenumber否否

选中时间的分。

取值范围：[0-59]

second11+number否否

选中时间的秒。

取值范围：[0-59]

#### 示例

#### 示例1（设置文本样式）

该示例通过配置[disappearTextStyle](#ZH-CN_TOPIC_0000002497604888__disappeartextstyle10)、[textStyle](#ZH-CN_TOPIC_0000002497604888__textstyle10)和[selectedTextStyle](#ZH-CN_TOPIC_0000002497604888__selectedtextstyle10)实现文本选择器中的文本样式。

```ets
// xxx.ets
@Entry
@Component
struct TimePickerExample {
  private selectedTime: Date = new Date('2022-07-22T08:00:00');

  build() {
    TimePicker({
      selected: this.selectedTime
    })
      .disappearTextStyle({ color: '#004aaf', font: { size: 24, weight: FontWeight.Lighter } })
      .textStyle({ color: Color.Black, font: { size: 26, weight: FontWeight.Normal } })
      .selectedTextStyle({ color: Color.Blue, font: { size: 30, weight: FontWeight.Bolder } })
      .onChange((value: TimePickerResult) => {
        if (value.hour >= 0) {
          this.selectedTime.setHours(value.hour, value.minute);
          console.info('select current date is: ' + JSON.stringify(value));
        }
      })
  }
}
```

#### 示例2（切换小时制）

该示例通过配置useMilitaryTime实现12小时制、24小时制的切换。

```ets
// xxx.ets
@Entry
@Component
struct TimePickerExample {
  @State isMilitaryTime: boolean = false;
  private selectedTime: Date = new Date('2022-07-22T08:00:00');

  build() {
    Column() {
      Button('切换12小时制/24小时制')
        .margin(30)
        .onClick(() => {
          this.isMilitaryTime = !this.isMilitaryTime;
        })

      TimePicker({
        selected: this.selectedTime
      })
        .useMilitaryTime(this.isMilitaryTime)
        .onChange((value: TimePickerResult) => {
          if (value.hour >= 0) {
            this.selectedTime.setHours(value.hour, value.minute);
            console.info('select current time is: ' + JSON.stringify(value));
          }
        })
        .onEnterSelectedArea((value: TimePickerResult) => {
            console.info('item enter selected area, time is: ' + JSON.stringify(value));
        })
    }.width('100%')
  }
}
```

#### 示例3（设置时间格式）

该示例使用format和dateTimeOptions设置TimePicker时间格式。

```ets
// xxx.ets
@Entry
@Component
struct TimePickerExample {
  private selectedTime: Date = new Date('2022-07-22T08:00:00');

  build() {
    Column() {
      TimePicker({
        selected: this.selectedTime,
        format: TimePickerFormat.HOUR_MINUTE_SECOND
      })
        .dateTimeOptions({ hour: "numeric", minute: "2-digit", second: "2-digit" })
        .onChange((value: TimePickerResult) => {
          if (value.hour >= 0) {
            this.selectedTime.setHours(value.hour, value.minute);
            console.info('select current date is: ' + JSON.stringify(value));
          }
        })
    }.width('100%')
  }
}
```

#### 示例4（设置循环滚动）

该示例通过配置[loop](#ZH-CN_TOPIC_0000002497604888__loop11)设置TimePicker是否循环滚动。

```ets
// xxx.ets
@Entry
@Component
struct TimePickerExample {
  @State isLoop: boolean = true;
  @State selectedTime: Date = new Date('2022-07-22T12:00:00');

  build() {
    Column() {
      TimePicker({
        selected: this.selectedTime
      })
        .loop(this.isLoop)
        .onChange((value: TimePickerResult) => {
          if (value.hour >= 0) {
            this.selectedTime.setHours(value.hour, value.minute);
            console.info('select current date is: ' + JSON.stringify(value));
          }
        })

      Row() {
        Text('循环滚动').fontSize(20)

        Toggle({ type: ToggleType.Switch, isOn: true })
          .onChange((isOn: boolean) => {
            this.isLoop = isOn;
          })
      }.position({ x: '60%', y: '40%' })

    }.width('100%')
  }
}
```

#### 示例5（设置时间选择组件的起始时间）

该示例设置TimePicker的起始时间。

```ets
// xxx.ets
@Entry
@Component
struct TimePickerExample {
  private selectedTime: Date = new Date('2022-07-22T08:50:00');

  build() {
    Column() {
      TimePicker({
        selected: this.selectedTime,
        format: TimePickerFormat.HOUR_MINUTE_SECOND,
        start: new Date('2022-07-22T08:30:00')
      })
        .dateTimeOptions({ hour: "numeric", minute: "2-digit", second: "2-digit" })
        .onChange((value: TimePickerResult) => {
          if (value.hour >= 0) {
            this.selectedTime.setHours(value.hour, value.minute);
            console.info('select current date is: ' + JSON.stringify(value));
          }
        })
    }.width('100%')
  }
}
```

#### 示例6（设置时间选择组件的结束时间）

该示例设置TimePicker的结束时间。

```ets
// xxx.ets
@Entry
@Component
struct TimePickerExample {
  private selectedTime: Date = new Date('2022-07-22T08:50:00');

  build() {
    Column() {
      TimePicker({
        selected: this.selectedTime,
        format: TimePickerFormat.HOUR_MINUTE_SECOND,
        end: new Date('2022-07-22T15:20:00'),
      })
        .dateTimeOptions({ hour: "numeric", minute: "2-digit", second: "2-digit" })
        .onChange((value: TimePickerResult) => {
          if (value.hour >= 0) {
            this.selectedTime.setHours(value.hour, value.minute);
            console.info('select current date is: ' + JSON.stringify(value));
          }
        })
    }.width('100%')
  }
}
```

#### 示例7（设置上午下午跟随时间联动）

该示例通过配置[enableCascade](#ZH-CN_TOPIC_0000002497604888__enablecascade18)、[loop](#ZH-CN_TOPIC_0000002497604888__loop11)实现12小时制时上午下午跟随时间联动。

```ets
// xxx.ets
@Entry
@Component
struct TimePickerExample {
  private selectedTime: Date = new Date('2022-07-22T08:00:00');

  build() {
    Column() {
      TimePicker({
        selected: this.selectedTime,
      })
        .enableCascade(true)
        .loop(true)
        .onChange((value: TimePickerResult) => {
          if (value.hour >= 0) {
            this.selectedTime.setHours(value.hour, value.minute);
            console.info('select current date is: ' + JSON.stringify(value));
          }
        })
    }.width('100%')
  }
}
```