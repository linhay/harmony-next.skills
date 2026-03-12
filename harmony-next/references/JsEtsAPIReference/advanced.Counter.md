# advanced.Counter

Counter组件用于精确调节数值。

 该组件从API Version 11开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

 如果Counter设置[通用属性](通用属性.md)和[通用事件](通用事件.md)，编译工具链会额外生成节点__Common__，并将通用属性或通用事件挂载在__Common__上，而不是直接应用到Counter本身。这可能导致开发者设置的通用属性或通用事件的效果不生效或不符合预期，因此，不建议Counter设置通用属性和通用事件。

#### 导入模块

```ets
import { CounterType, CounterComponent, CounterOptions, DateData } from '@kit.ArkUI';
```

#### 子组件

无

#### CounterComponent

CounterComponent({ options: CounterOptions })

定义Counter。

**装饰器类型：**@Component

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数**：

名称类型必填装饰器类型说明options[CounterOptions](#ZH-CN_TOPIC_0000002497604968__counteroptions)是@Prop定义Counter组件的类型。

#### CounterOptions

CounterOptions定义Counter类型及样式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明type[CounterType](#ZH-CN_TOPIC_0000002497604968__countertype)否否指定当前Counter的类型。direction12+[Direction](zh-cn_topic_0000002529284967.html#ZH-CN_TOPIC_0000002529284967__direction)否是

布局方向。

默认值：Direction.Auto

值为undefined时，按默认值处理。

numberOptions[NumberStyleOptions](#ZH-CN_TOPIC_0000002497604968__numberstyleoptions)否是

列表型和紧凑型Counter的样式。

默认值：显示计数器为0的列表型或紧凑型Counter。

值为undefined时，按默认值处理。

inlineOptions[InlineStyleOptions](#ZH-CN_TOPIC_0000002497604968__inlinestyleoptions)否是

普通数字内联调节型Counter的样式。

默认值：显示计数器为0的普通数字内联调节型Counter。

值为undefined时，按默认值处理。

dateOptions[DateStyleOptions](#ZH-CN_TOPIC_0000002497604968__datestyleoptions)否是

日期型内联型Counter的样式。

默认值：显示0001/01/01的日期型内联型Counter。

值为undefined时，按默认值处理。

选择不同的Counter类型，需要选择对应的Counter样式。

counter类型counter样式CounterType.LISTNumberStyleOptionsCounterType.COMPACTNumberStyleOptionsCounterType.INLINEInlineStyleOptionsCounterType.INLINE_DATEDateStyleOptions

#### CounterType

CounterType指定Counter类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称值说明LIST0列表型Counter。COMPACT1紧凑型Counter。INLINE2普通数字内联调节型Counter。INLINE_DATE3日期型内联型Counter。

#### CommonOptions

CommonOptions定义了Counter的共通属性和事件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明focusableboolean否是

设置Counter是否可获焦。

**说明：**

该属性对列表型和紧凑型Counter生效。

默认值：true

true：Counter可获焦；false：Counter不可获焦。

值为undefined时，按默认值处理。

stepnumber否是

设置Counter的步长。

取值范围：大于等于1的整数。

默认值：1

值为undefined时，按默认值处理。

onHoverIncrease(isHover: boolean) => void否是

鼠标进入或退出Counter组件的增加按钮时触发该回调。

isHover：表示鼠标是否悬浮在组件上，鼠标进入时为true，退出时为false。

默认值：不触发鼠标进入或退出Counter组件的增加按钮时的回调。

值为undefined时，按默认值处理。

onHoverDecrease(isHover: boolean) => void否是

鼠标进入或退出Counter组件的减小按钮时触发该回调。

isHover：表示鼠标是否悬浮在组件上，进入时为true，离开时为false。

默认值：不触发鼠标进入或退出Counter组件的减小按钮时的回调。

值为undefined时，按默认值处理。

#### InlineStyleOptions

InlineStyleOptions定义了数值内联型Counter的属性和事件。

继承于[CommonOptions](#ZH-CN_TOPIC_0000002497604968__commonoptions)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明valuenumber否是

设置Counter的初始值。

默认值：0

取值范围：[min, max]，其中min和max分别对应下述Counter的最小值和最大值。

值为undefined时，按默认值处理。

minnumber否是

设置Counter的最小值。

默认值：0

取值范围：(-∞, +∞)

值为undefined时，按默认值处理。

maxnumber否是

设置Counter的最大值。

默认值：999

取值范围：(-∞, +∞)

值为undefined时，按默认值处理。

textWidthnumber否是

设置数值文本的宽度。

默认值：自适应文本宽度。

取值范围：[0, +∞)

单位：vp

值为undefined时，按默认值处理。

onChange(value: number) => void否是

数值改变时，返回当前值。

value：当前显示的数值。

默认值：数值改变时，不返回值。

值为undefined时，按默认值处理。

#### NumberStyleOptions

NumberStyleOptions定义了列表型和紧凑型Counter的属性和事件。

继承于[InlineStyleOptions](#ZH-CN_TOPIC_0000002497604968__inlinestyleoptions)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明label[ResourceStr](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcestr)否是

设置Counter的说明文本。

默认值：' '

值为undefined时，按默认值处理。

onFocusIncrease() => void否是

当前Counter组件的增加按钮获取焦点时触发的回调。

默认值：不触发增加按钮获取焦点时的回调。

值为undefined时，按默认值处理。

onFocusDecrease() => void否是

当前Counter组件的减小按钮获取焦点时触发的回调。

默认值：不触发减少按钮获取焦点时的回调。

值为undefined时，按默认值处理。

onBlurIncrease() => void否是

当前Counter组件的增加按钮失去焦点时触发的回调。

默认值：不触发增加按钮失去焦点时的回调。

值为undefined时，按默认值处理。

onBlurDecrease() => void否是

当前Counter组件的减小按钮失去焦点时触发的回调。

默认值：不触发减少按钮失去焦点时的回调。

值为undefined时，按默认值处理。

#### DateStyleOptions

DateStyleOptions定义日期内联型Counter的属性和事件。

继承于[CommonOptions](#ZH-CN_TOPIC_0000002497604968__commonoptions)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明yearnumber否是

设置日期内联型初始年份。

默认值：1

取值范围：[1, 5000]

值为undefined时，按默认值处理。

monthnumber否是

设置日期内联型初始月份。

默认值：1

取值范围：[1, 12]

值为undefined时，按默认值处理。

daynumber否是

设置日期内联型初始日。

默认值：1

取值范围：[1, 31]

值为undefined时，按默认值处理。

onDateChange(date: [DateData](#ZH-CN_TOPIC_0000002497604968__datedata)) => void否是

当日期改变时，返回当前日期。

date：当前显示的日期值。

值为undefined时，不显示当前的日期值。

#### DateData

DateData定义了日期通用属性和方法，包括年、月、日。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明yearnumber否否

设置日期内联型初始年份。

默认值：1

取值范围：[1, 5000]

值为undefined时，按默认值处理。

monthnumber否否

设置日期内联型初始月份。

默认值：1

取值范围：[1, 12]

值为undefined时，按默认值处理。

daynumber否否

设置日期内联型初始日。

默认值：1

取值范围：[1, 31]

值为undefined时，按默认值处理。

#### constructor

constructor(year: number, month: number, day: number)

DateData的构造函数用于初始化日期对象。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明yearnumber是设置日期内联型初始年份。monthnumber是设置日期内联型初始月份。daynumber是设置日期内联型初始日。

#### toString

toString(): string

以字符串格式返回当前日期值。格式为’YYYY-MM-DD'。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

类型说明string当前日期值。

#### 示例

#### 示例1（列表型Counter）

该示例通过设置type为CounterType.LIST和配置numberOptions，实现了列表型Counter。

```ets
import { CounterType, CounterComponent } from '@kit.ArkUI';

@Entry
@Component
struct ListCounterExample {
  build() {
    Column() {
      //列表型Counter
      CounterComponent({
        options: {
          type: CounterType.LIST,
          numberOptions: {
            label: "价格",
            min: 0,
            value: 5,
            max: 10
          }
        }
      })
    }
  }
}
```

#### 示例2（紧凑型Counter）

该示例通过设置type为CounterType.COMPACT和numberOptions，实现紧凑型Counter。

```ets
import { CounterType, CounterComponent } from '@kit.ArkUI';

@Entry
@Component
struct CompactCounterExample {
  build() {
    Column() {
      //紧凑型Counter
      CounterComponent({
        options: {
          type: CounterType.COMPACT,
          numberOptions: {
            label: "数量",
            value: 10,
            min: 0,
            max: 100,
            step: 10
          }
        }
      })
    }
  }
}
```

#### 示例3（数值内联型Counter）

设置type为CounterType.INLINE和inlineOptions，实现数值内联型Counter。

```ets
import { CounterType, CounterComponent } from '@kit.ArkUI';

@Entry
@Component
struct NumberStyleExample {
  build() {
    Column() {
      //数值内联型Counter
      CounterComponent({
        options: {
          type: CounterType.INLINE,
          inlineOptions: {
            value: 100,
            min: 10,
            step: 2,
            max: 1000,
            textWidth: 100,
            onChange: (value: number) => {
              console.info('onCounterChange Counter: ' + value.toString());
            }
          }
        }
      })
    }
  }
}
```

#### 示例4（日期内联型Counter）

设置type为CounterType.INLINE_DATE和dateOptions，实现日期内联型Counter。

```ets
import { CounterType, CounterComponent, DateData } from '@kit.ArkUI';

@Entry
@Component
struct DataStyleExample {
  build() {
    Column() {
      //日期内联型counter
      CounterComponent({
        options: {
          type: CounterType.INLINE_DATE,
          dateOptions: {
            year: 2016,
            onDateChange: (date: DateData) => {
              console.info('onDateChange Date: ' + date.toString());
            }
          }
        }
      })
    }
  }
}
```

#### 示例5（镜像布局展示）

设置direction属性，实现列表型、紧凑型、数字内联型、日期内联型Counter的镜像布局。

```ets
import { CounterType, CounterComponent, DateData } from '@kit.ArkUI';

@Entry
@Component
struct CounterPage {
  @State currentDirection: Direction = Direction.Rtl

  build() {
    Column({}) {

      //列表型Counter
      CounterComponent({
        options: {
          direction: this.currentDirection,
          type: CounterType.LIST,
          numberOptions: {
            label: "价格",
            min: 0,
            value: 5,
            max: 10,
          }
        }
      })
        .width('80%')

      //数值型Counter
      CounterComponent({
        options: {
          direction: this.currentDirection,
          type: CounterType.COMPACT,
          numberOptions: {
            label: "数量",
            value: 10,
            min: 0,
            max: 100,
            step: 10
          }
        }
      }).margin({ top: 20 })

      //数值内联型Counter
      CounterComponent({
        options: {
          type: CounterType.INLINE,
          direction: this.currentDirection,
          inlineOptions: {
            value: 100,
            min: 10,
            step: 2,
            max: 1000,
            textWidth: 100,
            onChange: (value: number) => {
              console.info('onCounterChange Counter: ' + value.toString());
            }
          }
        }
      }).margin({ top: 20 })
      //日期内联型counter
      CounterComponent({
        options: {
          direction: this.currentDirection,
          type: CounterType.INLINE_DATE,
          dateOptions: {
            year: 2024,
            onDateChange: (date: DateData) => {
              console.info('onDateChange Date: ' + date.toString());
            }
          }
        }
      }).margin({ top: 20 })
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
    .alignItems(HorizontalAlign.Center)
  }
}
```