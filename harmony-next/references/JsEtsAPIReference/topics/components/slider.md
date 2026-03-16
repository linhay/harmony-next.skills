[]()[]()

# Slider

滑动条组件，通常用于快速调节设置值，如音量调节、亮度调节等应用场景。

该组件从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

[]()[]()

#### 子组件

无

[]()[]()

#### 接口

Slider(options?: SliderOptions)

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明options[SliderOptions](#ZH-CN_TOPIC_0000002497604890__slideroptions对象说明)否配置滑动条的参数。[]()[]()

#### SliderOptions对象说明

滑动条的信息。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明valuenumber否是

当前进度值。

默认值：与属性min的取值一致。

从API version 10开始，该属性支持[$$](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-two-way-sync)双向绑定变量。

该属性支持[!!](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-binding#系统组件参数双向绑定)双向绑定变量。

取值范围： [min, max]

小于min时取min，大于max时取max。

$$运算符为系统组件提供TS变量的引用，使得TS变量和slider组件的value值保持同步。详细使用示例请参考[示例7设置滑动条的双向绑定](#ZH-CN_TOPIC_0000002497604890__示例7设置滑动条的双向绑定)。

minnumber否是

设置最小值。

默认值：0

maxnumber否是

设置最大值。

默认值：100

**说明：**

min >= max异常情况，min取默认值0，max取默认值100。

value不在[min, max]范围之内，取min或者max，靠近min取min，靠近max取max。

stepnumber否是

设置Slider滑动步长。

默认值：1

取值范围：[0.01, max - min]

**说明：**

若设置的step值小于0或大于max值，则按默认值显示。

style[SliderStyle](#ZH-CN_TOPIC_0000002497604890__sliderstyle枚举说明)否是

设置Slider的滑块与滑轨显示样式。

默认值：SliderStyle.OutSet

direction8+[Axis](../../guides/枚举说明.md#ZH-CN_TOPIC_0000002529284967__axis)否是

设置滑动条滑动方向为水平或竖直方向。

默认值：Axis.Horizontal

reverse8+boolean否是

设置滑动条取值范围是否反向。

true：横向Slider从右往左滑动，竖向Slider从下往上滑动；false：横向Slider从左往右滑动，竖向Slider从上往下滑动。

默认值：false

[]()[]()

#### SliderStyle枚举说明

滑动条滑块在滑轨上显示的样式，具体样式请参考[Slider组件滑块与滑轨是如何对齐的](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-select-component-faq#slider组件滑块与滑轨是如何对齐的)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称说明OutSet

滑块在滑轨上。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

InSet

滑块在滑轨内。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

NONE12+

无滑块

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

- Slider无默认padding。
- 当Slider为水平滑动条时，默认高度为40vp，宽度为父容器的宽度，滑动条居中显示，当滑动条的style为SliderStyle.OutSet时，左右间距分别为9vp，即为[blockSize](#ZH-CN_TOPIC_0000002497604890__blocksize10)宽度的一半，当滑动条的style为SliderStyle.InSet时，左右间距分别为6vp，若设置padding，padding不会覆盖左右间距。
- 当Slider为竖直滑动条时，默认宽度为40vp，高度为父容器的高度，滑动条居中显示，当滑动条的style为SliderStyle.OutSet时，上下间距分别为10vp，当滑动条的style为SliderStyle.InSet时，上下间距分别为6vp，若设置padding，padding不会覆盖上下间距。

[]()[]()

#### 属性

支持除触摸热区以外的[通用属性](通用属性 (ts-component-general-attributes).md)。

[]()[]()

#### blockColor

blockColor(value: ResourceColor)

设置滑块的颜色。

当滑块形状设置为SliderBlockType.DEFAULT时，blockColor可设置默认圆形滑块颜色。

当滑块形状设置为SliderBlockType.IMAGE时，滑块无填充，设置blockColor不生效。

当滑块形状设置为SliderBlockType.SHAPE时，blockColor可设置自定义形状的填充颜色。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明value[ResourceColor](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)是

滑块的颜色。

默认值：$r('sys.color.ohos_id_color_foreground_contrary')

[]()[]()

#### blockColor21+

blockColor(value: ResourceColor | LinearGradient)

设置Slider滑块的颜色，支持渐变色。

当滑块形状设置为SliderBlockType.DEFAULT时，blockColor可设置默认圆形滑块颜色。

当滑块形状设置为SliderBlockType.IMAGE时，滑块无填充，设置blockColor不生效。

当滑块形状设置为SliderBlockType.SHAPE时，blockColor可设置自定义形状的填充颜色。

**卡片能力：** 从API version 21开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 21开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明value[ResourceColor](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor) | [LinearGradient](DataPanel.md#ZH-CN_TOPIC_0000002497604906__lineargradient10)是

滑块的颜色。

默认值：$r('sys.color.ohos_id_color_foreground_contrary')

[]()[]()

#### trackColor

trackColor(value: ResourceColor | LinearGradient)

设置滑轨的背景颜色。

从API version 12开始支持利用LinearGradient设置滑轨的渐变色。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明value[ResourceColor](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor) | [LinearGradient12+](DataPanel.md#ZH-CN_TOPIC_0000002497604906__lineargradient10)是

滑轨的背景颜色。

默认值：$r('sys.color.ohos_id_color_component_normal')

**说明：**

1. 设置渐变色时，如果颜色断点颜色值为非法值或渐变色断点为空，渐变色将不起效果。

2. 该接口中的LinearGradient类型不支持在元服务中使用。

[]()[]()

#### selectedColor

selectedColor(value: ResourceColor)

设置滑轨的已滑动部分颜色。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明value[ResourceColor](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)是

滑轨的已滑动部分颜色。

默认值：$r('sys.color.ohos_id_color_emphasize')

[]()[]()

#### selectedColor18+

selectedColor(selectedColor: ResourceColor | LinearGradient)

设置滑轨的已滑动部分颜色。与[selectedColor](#ZH-CN_TOPIC_0000002497604890__selectedcolor)相比，新增了LinearGradient类型的支持。

**卡片能力：** 从API version 18开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明selectedColor[ResourceColor](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor) | [LinearGradient](DataPanel.md#ZH-CN_TOPIC_0000002497604906__lineargradient10)是

滑轨的已滑动部分颜色。

默认值：$r('sys.color.ohos_id_color_emphasize')

**说明：**

设置渐变色时，若颜色断点颜色值为非法值或者渐变色断点为空时，渐变色不起效果。

[]()[]()

#### showSteps

showSteps(value: boolean)

设置当前是否显示步长刻度值。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明valueboolean是

当前是否显示步长刻度值。

true：显示刻度值；false：不显示刻度值。

默认值：false

[]()[]()

#### showTips

showTips(value: boolean, content?: ResourceStr)

设置滑动时是否显示气泡提示。

当direction的值为Axis.Horizontal时，tip显示在滑块上方，如果上方空间不够，则在下方显示。当值为Axis.Vertical时，tip显示在滑块左边，如果左边空间不够，则在右边显示。当不设置周边边距或者周边边距比较小时，tip会被截断。

tip的绘制区域为Slider自身节点的overlay。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明valueboolean是

滑动时是否显示气泡提示。

true：显示气泡；false：不显示气泡。

默认值：false

content10+[ResourceStr](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcestr)否气泡提示的文本内容，默认显示当前百分比。[]()[]()

#### trackThickness8+

trackThickness(value: Length)

设置滑轨的粗细。设置小于等于0的值时，取默认值。

为保证滑块和滑轨的[SliderStyle](#ZH-CN_TOPIC_0000002497604890__sliderstyle枚举说明)样式，[blockSize](#ZH-CN_TOPIC_0000002497604890__blocksize10)跟随trackThickness同比例增减。

当style为[SliderStyle](#ZH-CN_TOPIC_0000002497604890__sliderstyle枚举说明).OutSet时，trackThickness ：[blockSize](#ZH-CN_TOPIC_0000002497604890__blocksize10) = 1 ：4，当style为[SliderStyle](#ZH-CN_TOPIC_0000002497604890__sliderstyle枚举说明).InSet时，trackThickness ：[blockSize](#ZH-CN_TOPIC_0000002497604890__blocksize10) = 5 ：3。

trackThickness或[blockSize](#ZH-CN_TOPIC_0000002497604890__blocksize10)的大小超过Slider组件的宽度或高度时，取默认值。

当[SliderStyle](#ZH-CN_TOPIC_0000002497604890__sliderstyle枚举说明)设置为OutSet时，尽管trackThickness的大小没超过Slider组件的宽度或高度，但是[blockSize](#ZH-CN_TOPIC_0000002497604890__blocksize10)超过了，取默认值。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明value[Length](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__length)是

滑轨的粗细。

默认值：当参数style的值设置[SliderStyle](#ZH-CN_TOPIC_0000002497604890__sliderstyle枚举说明).OutSet 时为 4.0vp，[SliderStyle](#ZH-CN_TOPIC_0000002497604890__sliderstyle枚举说明).InSet时为20.0vp。

[]()[]()

#### blockBorderColor10+

blockBorderColor(value: ResourceColor)

设置滑块描边颜色。

当滑块形状设置为SliderBlockType.DEFAULT时，blockBorderColor可设置默认圆形滑块描边颜色。

当滑块形状设置为SliderBlockType.IMAGE时，滑块无描边，设置blockBorderColor不生效。

当滑块形状设置为SliderBlockType.SHAPE时，blockBorderColor可设置自定义形状中线的颜色。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明value[ResourceColor](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)是

滑块描边颜色。

默认值：'#00000000'

[]()[]()

#### blockBorderWidth10+

blockBorderWidth(value: Length)

设置滑块描边粗细。

当滑块形状设置为SliderBlockType.DEFAULT时，blockBorderWidth可设置默认圆形滑块描边粗细。

当滑块形状设置为SliderBlockType.IMAGE时，滑块无描边，设置blockBorderWidth不生效。

当滑块形状设置为SliderBlockType.SHAPE时，blockBorderWidth可设置自定义形状中线的粗细。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明value[Length](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__length)是

滑块描边粗细。

**说明：**

设置string类型时，不支持百分比。

[]()[]()

#### stepColor10+

stepColor(value: ResourceColor)

设置刻度颜色。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明value[ResourceColor](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)是

刻度颜色。

默认值：

$r('sys.color.ohos_id_color_foreground')混合

$r('sys.color.ohos_id_alpha_normal_bg')透明度的颜色

[]()[]()

#### trackBorderRadius10+

trackBorderRadius(value: Length)

设置底板圆角半径。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明value[Length](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__length)是

底板圆角半径。

默认值：

style值为SliderStyle.OutSet时默认值为'2vp'。

style值为SliderStyle.InSet时默认值为'10vp'。

**说明：**

设定值小于0时取默认值。

[]()[]()

#### selectedBorderRadius12+

selectedBorderRadius(value: Dimension)

设置已滑动部分（高亮）圆角半径。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明value[Dimension](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__dimension10)是

已选择部分的圆角半径。

默认值：当style值为SliderStyle.InSet或SliderStyle.OutSet时，跟随底板圆角；当style值为SliderStyle.NONE时，为0。

**说明：**

不支持Percentage类型。设定值小于0时取默认值。

[]()[]()

#### blockSize10+

blockSize(value: SizeOptions)

设置滑块大小。

当滑块形状设置为SliderBlockType.DEFAULT时，取宽高的最小值作为圆形半径。

当滑块形状设置为SliderBlockType.IMAGE时，用于设置图片的尺寸大小，图片采用ObjectFit.Cover策略进行缩放。

当滑块形状设置为SliderBlockType.SHAPE时，用于设置自定义形状的大小，自定义形状也会采用ObjectFit.Cover策略进行缩放。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明value[SizeOptions](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__sizeoptions)是

滑块大小。

默认值：当参数style的值设置为[SliderStyle](#ZH-CN_TOPIC_0000002497604890__sliderstyle枚举说明).OutSet时为{width: 18, height: 18}，当参数style的值设置为[SliderStyle](#ZH-CN_TOPIC_0000002497604890__sliderstyle枚举说明).InSet时为{width: 12, height: 12}，当参数style的值设置为[SliderStyle](#ZH-CN_TOPIC_0000002497604890__sliderstyle枚举说明).NONE时为，此字段不生效。

当设置的blockSize的宽高值不相等时，取较小值的尺寸，当设置的宽高值中有一个或两个都小于等于0的时候，取默认值。

[]()[]()

#### blockStyle10+

blockStyle(value: SliderBlockStyle)

设置滑块形状参数。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明value[SliderBlockStyle](#ZH-CN_TOPIC_0000002497604890__sliderblockstyle10对象说明)是

滑块形状参数。

默认值：SliderBlockType.DEFAULT，滑块形状为圆形。

[]()[]()

#### stepSize10+

stepSize(value: Length)

设置刻度大小（直径）。当值为0时，刻度点不显示，当值小于0时，取默认值。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明value[Length](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__length)是

刻度大小（直径）。

默认值：'4vp'

取值范围：[0, [trackThickness](#ZH-CN_TOPIC_0000002497604890__trackthickness8))

[]()[]()

#### sliderInteractionMode12+

sliderInteractionMode(value: SliderInteraction)

设置用户与滑动条组件交互方式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明value[SliderInteraction](#ZH-CN_TOPIC_0000002497604890__sliderinteraction12枚举说明)是

用户与滑动条组件交互方式。

默认值：SliderInteraction.SLIDE_AND_CLICK。

[]()[]()

#### minResponsiveDistance12+

minResponsiveDistance(value: number)

设置滑动响应的最小距离。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明valuenumber是

设置滑动响应的最小距离，滑动超过此距离后滑块才开始滑动。

默认值：0

**说明：**

单位与[SliderOptions](#ZH-CN_TOPIC_0000002497604890__slideroptions对象说明)中的属性min以及属性max一致。

当value小于0、大于max-min或非法值时，取默认值。

[]()[]()

#### contentModifier12+

contentModifier(modifier: ContentModifier<SliderConfiguration>)

定制Slider内容区的方法。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明modifier[ContentModifier](../misc/自定义内容.md)[<SliderConfiguration>](#ZH-CN_TOPIC_0000002497604890__sliderconfiguration12对象说明)是

在Slider组件上，定制内容区的方法。

ContentModifier：内容修改器，开发者需要自定义class实现ContentModifier接口。

- 设置了contentModifier后，自定义区域内点击和手势滑动均不会触发原Slider组件的onChange事件。
- 仅当调用triggerChange函数且传递正确的参数值时，才可以触发原Slider组件的onChange事件。

[]()[]()

#### slideRange12+

slideRange(value: SlideRange)

设置有效滑动区间。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明value[SlideRange](#ZH-CN_TOPIC_0000002497604890__sliderange12对象说明)是设置有效滑动区间[]()[]()

#### enableHapticFeedback18+

enableHapticFeedback(enabled: boolean)

设置是否开启触控反馈。

开启触控反馈时，需要在工程的[module.json5](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/module-configuration-file)中配置requestPermissions字段开启振动权限，配置如下：

```ets
"requestPermissions": [
  {
    "name": "ohos.permission.VIBRATE"
  }
 ]
```

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明enabledboolean是

设置是否开启触控反馈。

true：开启触控反馈；false：不开启触控反馈。

默认值：true

[]()[]()

#### digitalCrownSensitivity18+

digitalCrownSensitivity(sensitivity: Optional<CrownSensitivity>)

设置旋转表冠的灵敏度。

该接口不支持在[attributeModifier](../misc/动态属性设置.md#ZH-CN_TOPIC_0000002529284843__attributemodifier)中调用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明sensitivity[Optional](../misc/自定义属性设置.md#ZH-CN_TOPIC_0000002529284845__optionalt12)[<CrownSensitivity>](../../guides/枚举说明.md#ZH-CN_TOPIC_0000002529284967__crownsensitivity18)是

旋转表冠的灵敏度。

默认值：CrownSensitivity.MEDIUM

[]()[]()

#### prefix20+

prefix(content: ComponentContent, options?: SliderPrefixOptions)

设置滑动条的前缀。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明content[ComponentContent](ComponentContent.md)是自定义组件内容，用于定义滑块前缀的可视化内容，该内容会显示在滑块的起始位置。options[SliderPrefixOptions](#ZH-CN_TOPIC_0000002497604890__sliderprefixoptions20)否滑块前缀的配置选项，用于设置与无障碍功能相关的属性。[]()[]()

#### suffix20+

suffix(content: ComponentContent, options?: SliderSuffixOptions)

设置滑动条的后缀。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明content[ComponentContent](ComponentContent.md)是自定义组件内容，用于定义滑块后缀的可视化内容，该内容会显示在滑块的结束位置。options[SliderSuffixOptions](#ZH-CN_TOPIC_0000002497604890__slidersuffixoptions20)否滑块后缀的配置选项，用于设置与无障碍功能相关的属性。[]()[]()

#### showSteps20+

showSteps(value: boolean, options?: SliderShowStepOptions)

设置当前是否显示步长刻度值。

支持设置每个刻度点的无障碍文本信息，不设置时默认使用当前刻度点的值作为无障碍文本信息。

当显示步长时，设置的刻度点无障碍文本信息生效。

**卡片能力：** 从API version 20开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明valueboolean是

当前是否显示步长刻度值。

true：显示刻度值；false：不显示刻度值。

默认值：false

options[SliderShowStepOptions](#ZH-CN_TOPIC_0000002497604890__slidershowstepoptions20)否

刻度点无障碍文本的配置选项，用于设置与无障碍功能相关的属性。

默认值：null

[]()[]()

#### minLabel(deprecated)

minLabel(value: string)

设置最小值。

从API version 7开始支持，从API version 9开始废弃，建议使用min替代。min是[SliderOptions](#ZH-CN_TOPIC_0000002497604890__slideroptions对象说明)中的属性。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明valuestring是最小值。[]()[]()

#### maxLabel(deprecated)

maxLabel(value: string)

设置最大值。

从API version 7开始支持，从API version 9开始废弃，建议使用max替代。max是[SliderOptions](#ZH-CN_TOPIC_0000002497604890__slideroptions对象说明)中的属性。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明valuestring是最大值。[]()[]()

#### SliderCustomContentOptions20+

Slider前后缀组件无障碍信息参数。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明accessibilityText[ResourceStr](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcestr)否是

用于提供辅助功能的文本，供屏幕阅读器等工具读取，增强无障碍功能。

默认值：""

accessibilityDescription[ResourceStr](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcestr)否是

用于提供辅助功能的详细描述，描述滑块前缀或后缀的功能或用途，供屏幕阅读器等工具使用。

默认值为“单指双击即可执行”。

accessibilityLevelstring否是

用于控制某个组件是否可被无障碍辅助服务所识别。

支持的值为:

"auto"：当前组件会转换为“yes”。

"yes"：当前组件可被无障碍辅助服务所识别。

"no"：当前组件不可被无障碍辅助服务所识别。

"no-hide-descendants"：当前组件及其所有子组件不可被无障碍辅助服务所识别。

默认值："auto"。

accessibilityGroupboolean否是

用于标识该元素是否属于一个无障碍的组，帮助屏幕阅读器等工具将相关元素进行分组处理。

true：该组件及其所有子组件为一整个可以选中的组件，无障碍服务将不再关注其子组件内容；false：不启用无障碍分组。

默认值：false

[]()[]()

#### SliderPrefixOptions20+

Slider前缀组件无障碍信息参数。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

提供前缀组件的无障碍信息，继承自[SliderCustomContentOptions](#ZH-CN_TOPIC_0000002497604890__slidercustomcontentoptions20)。

[]()[]()

#### SliderSuffixOptions20+

Slider后缀组件无障碍信息参数。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

提供后缀组件的无障碍信息，继承自[SliderCustomContentOptions](#ZH-CN_TOPIC_0000002497604890__slidercustomcontentoptions20)。

[]()[]()

#### SliderStepItemAccessibility20+

Slider刻度点的无障碍文本信息。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明text[ResourceStr](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcestr)否是

用于提供辅助功能的文本，供屏幕阅读器等工具读取，增强无障碍功能。

默认值：""

[]()[]()

#### SliderShowStepOptions20+

Slider刻度点的无障碍文本信息映射集。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明stepsAccessibilityMap<number, [SliderStepItemAccessibility](#ZH-CN_TOPIC_0000002497604890__sliderstepitemaccessibility20)>否是

用于设置刻度点提供辅助功能文本，供屏幕阅读器等工具读取，增强无障碍功能。

Key取值范围：[0, INT32_MAX]，当Key设定为负数和小数时，设定项不生效。

默认值：{}

[]()[]()

#### SliderBlockStyle10+对象说明

Slider组件滑块形状参数。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明type[SliderBlockType](#ZH-CN_TOPIC_0000002497604890__sliderblocktype10枚举说明)否否

设置滑块形状。

默认值：SliderBlockType.DEFAULT，使用圆形滑块。

image[ResourceStr](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcestr)否是

设置滑块图片资源。

图片显示区域大小由blockSize属性控制，请勿输入尺寸过大的图片。

shape[Circle](../misc/circle.md) | [Ellipse](../misc/Ellipse.md) | [Path](../graphics/path.md) | [Rect](Rect (ts-drawing-components-rect).md)否是设置滑块使用的自定义形状。[]()[]()

#### SliderBlockType10+枚举说明

Slider组件滑块形状枚举。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称值说明DEFAULT0使用默认滑块（圆形）。IMAGE1使用图片资源作为滑块。SHAPE2使用自定义形状作为滑块。[]()[]()

#### SliderInteraction12+枚举说明

用户与滑动条组件交互方式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称值说明SLIDE_AND_CLICK0用户可拖拽滑块或者点击滑轨使滑块移动，鼠标或手指按下即发生移动。SLIDE_ONLY1禁止用户通过点击滑轨使滑块移动。SLIDE_AND_CLICK_UP2用户可拖拽滑块或者点击滑轨使滑块移动，当鼠标或手指抬起时，若与屏幕按压位置一致，则触发移动。[]()[]()

#### SlideRange12+对象说明

定义SlideRange中使用的回调类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明fromnumber否是设置有效滑动区间的开始。tonumber否是设置有效滑动区间的结束。

- 当前仅当min<=from<=to<=max时该接口生效(min和max不依赖于其设置的值，而取决于其实际生效的值)。
- 可只设置from或者to，也可以同时设置from和to。
- 当接口生效且设置的from处于紧邻的step整数倍的值之间，则from实际取左区间step整数倍的那个值或者min作为修正后的值。
- 当接口生效且设置的to处于紧邻的step整数倍的值之间，则to实际取右区间step整数倍的那个值或者MAX作为修正后的值。
- 在from和to取修正值后， 当value是undefined或null时，其取值与from一致; 当value是数值型且value <= from，则取from; 当value > to，则取to。

[]()[]()

#### 事件

除支持[通用事件](通用事件 (ts-component-general-events).md)外，还支持以下事件：

[]()[]()

#### onChange

onChange(callback: (value: number, mode: SliderChangeMode) => void)

Slider拖动或点击时触发事件回调。

Begin和End状态当手势点击时都会触发，Moving和Click状态当value值发生变化时触发。

当连贯动作为拖动动作时，不触发Click状态。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明valuenumber是当前滑动进度值，变化范围为对应步长steps数组。若返回值有小数，可使用number.toFixed()方法将数据处理为预期的精度。mode[SliderChangeMode](#ZH-CN_TOPIC_0000002497604890__sliderchangemode枚举说明)是事件触发的相关状态值。[]()[]()

#### SliderChangeMode枚举说明

滑块的状态值。包括按下、拖动、离开以及点击滑动条使滑块位置时。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称值说明Begin0手势/鼠标接触或者按下滑块。Moving1正在拖动滑块过程中。End2

手势/鼠标离开滑块。

**说明：**

异常值恢复成默认值时触发，即value设置小于min或大于max。

Click8+3点击滑动条使滑块位置移动。[]()[]()

#### SliderConfiguration12+对象说明

开发者需要自定义class实现ContentModifier接口。继承自[CommonConfiguration](../misc/自定义内容.md#ZH-CN_TOPIC_0000002497444874__commonconfigurationt)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明valuenumber否否当前进度值。minnumber否否最小值。maxnumber否否最大值。stepnumber否否Slider滑动步长。triggerChange[SliderTriggerChangeCallback](#ZH-CN_TOPIC_0000002497604890__slidertriggerchangecallback12)否否触发Slider变化。[]()[]()

#### SliderTriggerChangeCallback12+

type SliderTriggerChangeCallback = (value: number, mode: SliderChangeMode) => void

定义SliderConfiguration中使用的回调类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明valuenumber是

设置当前的进度值。

取值范围：[[min](#ZH-CN_TOPIC_0000002497604890__slideroptions对象说明)-[max](#ZH-CN_TOPIC_0000002497604890__slideroptions对象说明)]

mode[SliderChangeMode](#ZH-CN_TOPIC_0000002497604890__sliderchangemode枚举说明)是设置事件触发的相关状态值。[]()[]()

#### 示例

[]()[]()

#### 示例1（滑动条基础样式）

该示例通过配置style、showTips、showSteps控制气泡、刻度值、滑块和滑轨的显示。

```ets
// xxx.ets
@Entry
@Component
struct SliderExample {
  @State outSetValueOne: number = 40;
  @State inSetValueOne: number = 40;
  @State noneValueOne: number = 40;
  @State outSetValueTwo: number = 40;
  @State inSetValueTwo: number = 40;
  @State vOutSetValueOne: number = 40;
  @State vInSetValueOne: number = 40;
  @State vOutSetValueTwo: number = 40;
  @State vInSetValueTwo: number = 40;

  build() {
    Column({ space: 8 }) {
      Text('outset slider').fontSize(9).fontColor(0xCCCCCC).width('90%').margin(15)
      Row() {
        Slider({
          value: this.outSetValueOne,
          min: 0,
          max: 100,
          style: SliderStyle.OutSet
        })
          .showTips(true)
          .onChange((value: number, mode: SliderChangeMode) => {
            this.outSetValueOne = value;
            console.info('value:' + value + 'mode:' + mode.toString());
          })
        // toFixed(0)将滑动条返回值处理为整数精度
        Text(this.outSetValueOne.toFixed(0)).fontSize(12)
      }
      .width('80%')
      Row() {
        Slider({
          value: this.outSetValueTwo,
          step: 10,
          style: SliderStyle.OutSet
        })
          .showSteps(true)
          .onChange((value: number, mode: SliderChangeMode) => {
            this.outSetValueTwo = value;
            console.info('value:' + value + 'mode:' + mode.toString());
          })
        Text(this.outSetValueTwo.toFixed(0)).fontSize(12)
      }
      .width('80%')

      Text('inset slider').fontSize(9).fontColor(0xCCCCCC).width('90%').margin(15)
      Row() {
        Slider({
          value: this.inSetValueOne,
          min: 0,
          max: 100,
          style: SliderStyle.InSet
        })
          .blockColor('#191970')
          .trackColor('#ADD8E6')
          .selectedColor('#4169E1')
          .showTips(true)
          .onChange((value: number, mode: SliderChangeMode) => {
            this.inSetValueOne = value;
            console.info('value:' + value + 'mode:' + mode.toString());
          })
        Text(this.inSetValueOne.toFixed(0)).fontSize(12)
      }
      .width('80%')
      Row() {
        Slider({
          value: this.inSetValueTwo,
          step: 10,
          style: SliderStyle.InSet
        })
          .blockColor('#191970')
          .trackColor('#ADD8E6')
          .selectedColor('#4169E1')
          .showSteps(true)
          .onChange((value: number, mode: SliderChangeMode) => {
            this.inSetValueTwo = value;
            console.info('value:' + value + 'mode:' + mode.toString());
          })
        Text(this.inSetValueTwo.toFixed(0)).fontSize(12)
      }
      .width('80%')

      Text('none slider').fontSize(9).fontColor(0xCCCCCC).width('90%').margin(15)
      Row() {
        Slider({
          value: this.noneValueOne,
          min: 0,
          max: 100,
          style: SliderStyle.NONE
        })
          .blockColor('#191970')
          .trackColor('#ADD8E6')
          .selectedColor('#4169E1')
          .showTips(true)
          .onChange((value: number, mode: SliderChangeMode) => {
            this.noneValueOne = value;
            console.info('value:' + value + 'mode:' + mode.toString());
          })
        Text(this.noneValueOne.toFixed(0)).fontSize(12)
      }
      .width('80%')

      Row() {
        Column() {
          Text('vertical outset slider').fontSize(9).fontColor(0xCCCCCC).width('50%').margin(15)
          Row() {
            Text().width('10%')
            Slider({
              value: this.vOutSetValueOne,
              style: SliderStyle.OutSet,
              direction: Axis.Vertical
            })
              .blockColor('#191970')
              .trackColor('#ADD8E6')
              .selectedColor('#4169E1')
              .showTips(true)
              .onChange((value: number, mode: SliderChangeMode) => {
                this.vOutSetValueOne = value;
                console.info('value:' + value + 'mode:' + mode.toString());
              })
            Slider({
              value: this.vOutSetValueTwo,
              step: 10,
              style: SliderStyle.OutSet,
              direction: Axis.Vertical
            })
              .blockColor('#191970')
              .trackColor('#ADD8E6')
              .selectedColor('#4169E1')
              .showSteps(true)
              .onChange((value: number, mode: SliderChangeMode) => {
                this.vOutSetValueTwo = value;
                console.info('value:' + value + 'mode:' + mode.toString());
              })
          }
        }.width('50%').height(300)

        Column() {
          Text('vertical inset slider').fontSize(9).fontColor(0xCCCCCC).width('50%').margin(15)
          Row() {
            Slider({
              value: this.vInSetValueOne,
              style: SliderStyle.InSet,
              direction: Axis.Vertical,
              reverse: true // 竖向的Slider默认是上端是min值，下端是max值，因此想要从下往上滑动，需要设置reverse为true
            })
              .showTips(true)
              .onChange((value: number, mode: SliderChangeMode) => {
                this.vInSetValueOne = value;
                console.info('value:' + value + 'mode:' + mode.toString());
              })
            Slider({
              value: this.vInSetValueTwo,
              step: 10,
              style: SliderStyle.InSet,
              direction: Axis.Vertical,
              reverse: true
            })
              .showSteps(true)
              .onChange((value: number, mode: SliderChangeMode) => {
                this.vInSetValueTwo = value;
                console.info('value:' + value + 'mode:' + mode.toString());
              })
          }
        }.width('50%').height(300)
      }
    }.width('100%')
  }
}
```

[]()[]()

#### 示例2（设置滑动条样式）

该示例通过blockBorderColor、blockSize、blockBorderWidth、blockStyle设置滑块的样式，通过stepSize、stepColor设置刻度值的样式，通过trackBorderRadius设置底板的圆角，通过selectedBorderRadius设置已滑动部分的圆角。

```ets
@Entry
@Component
struct SliderExample {
  @State tipsValue: number = 40;

  build() {
    Column({ space: 8 }) {
      Text('block').fontSize(9).fontColor(0xCCCCCC).margin(15).width('90%')
      Slider({ style: SliderStyle.OutSet, value: 40 })
        .blockSize({ width: 40, height: 40 })
        .blockBorderColor(Color.Red)
        .blockBorderWidth(5)
      Divider()
      Text('step').fontSize(9).fontColor(0xCCCCCC).margin(15).width('90%')
      Slider({ style: SliderStyle.InSet, value: 40, step: 10 })
        .showSteps(true)
        .stepSize(8)
        .stepColor(Color.Yellow)
      Divider()
      Text('track').fontSize(9).fontColor(0xCCCCCC).margin(15).width('90%')
      Slider({ style: SliderStyle.InSet, value: 40 })
        .trackBorderRadius(2)
      Divider()
      Text('selected').fontSize(9).fontColor(0xCCCCCC).margin(15).width('90%')
      Slider({ style: SliderStyle.InSet, value: 40 })
        .selectedBorderRadius(2)
      Divider()
      Text('blockStyle').fontSize(9).fontColor(0xCCCCCC).margin(15).width('90%')
      Slider({ style: SliderStyle.OutSet, value: 40 })
        .blockStyle({ type: SliderBlockType.DEFAULT })
      Slider({ style: SliderStyle.OutSet, value: 40 })
        .blockStyle({ type: SliderBlockType.IMAGE, image: $r('sys.media.ohos_app_icon') })
      Slider({ style: SliderStyle.OutSet, value: 40 })
        .blockSize({ width: '60px', height: '60px' })
        .blockColor(Color.Red)
        .blockStyle({ type: SliderBlockType.SHAPE, shape: new Path({ commands: 'M60 60 M30 30 L15 56 L45 56 Z' }) })
      Divider()
      Text('tips').fontSize(9).fontColor(0xCCCCCC).margin(15).width('90%')
      Slider({ style: SliderStyle.InSet, value: this.tipsValue })
        .showTips(true, this.tipsValue.toFixed())
        .onChange(value => {
          this.tipsValue = value;
        })
    }
  }
}
```

[]()[]()

#### 示例3（自定义滑动条）

该示例实现了Slider组件通过样式Builder定制内容区。点击增加按钮，进度条会按照原Slider设置的步长增加，反之点减少按钮进度条会减少，并触发原组件的onChange事件。

```ets
// xxx.ets

@Builder
function buildSlider(config: SliderConfiguration) {
  Row() {
    Column({ space: 30 }) {
      Progress({ value: config.value, total: config.max, type: ProgressType.Ring })
        .margin({ top: 20 })

      Button('增加')
        .onClick(() => {
          config.value = config.value + config.step;
          config.triggerChange(config.value, SliderChangeMode.Click);
        })
        .width(100)
        .height(25)
        .fontSize(10)
        .enabled(config.value < config.max)

      Button('减少')
        .onClick(() => {
          config.value = config.value - config.step;
          config.triggerChange(config.value, SliderChangeMode.Click);
        })
        .width(100)
        .height(25)
        .fontSize(10)
        .enabled(config.value > config.min)

      Slider({
        value: config.value,
        min: config.min,
        max: config.max,
        step: config.step,
      })
        .width(100)
        .visibility((config.contentModifier as MySliderStyle).showSlider ? Visibility.Visible : Visibility.Hidden)
        .showSteps(true)
        .onChange((value: number, mode: SliderChangeMode) => {
          config.triggerChange(value, mode);
        })
      Text('当前状态：' + ((config.contentModifier as MySliderStyle).sliderChangeMode == 0 ? "Begin"
        : ((config.contentModifier as MySliderStyle).sliderChangeMode == 1 ? "Moving"
          : ((config.contentModifier as MySliderStyle).sliderChangeMode == 2 ? "End"
            : ((config.contentModifier as MySliderStyle).sliderChangeMode == 3 ? "Click" : "无")))))
        .fontSize(10)
      Text('进度值：' + config.value)
        .fontSize(10)
      Text('最小值：' + config.min)
        .fontSize(10)
      Text('最大值：' + config.max)
        .fontSize(10)
      Text('步长：' + config.step)
        .fontSize(10)
    }
    .width('80%')

  }
  .width('100%')
}

class MySliderStyle implements ContentModifier<SliderConfiguration> {
  showSlider: boolean = true;
  sliderChangeMode: number = 0;

  constructor(showSlider: boolean, sliderChangeMode: number) {
    this.showSlider = showSlider;
    this.sliderChangeMode = sliderChangeMode;
  }

  applyContent(): WrappedBuilder<[SliderConfiguration]> {
    return wrapBuilder(buildSlider);
  }
}

@Entry
@Component
struct SliderExample {
  @State showSlider: boolean = true;
  @State sliderValue: number = 0;
  @State sliderMin: number = 10;
  @State sliderMax: number = 100;
  @State sliderStep: number = 20;
  @State sliderChangeMode: number = 0;

  build() {
    Column({ space: 8 }) {

      Row() {
        Slider({
          value: this.sliderValue,
          min: this.sliderMin,
          max: this.sliderMax,
          step: this.sliderStep,
        })
          .showSteps(true)
          .onChange((value: number, mode: SliderChangeMode) => {
            this.sliderValue = value;
            this.sliderChangeMode = mode;
            console.info('SliderLog value:' + value + 'mode:' + mode.toString());
          })
          .contentModifier(new MySliderStyle(this.showSlider, this.sliderChangeMode))

      }
      .width('100%')

    }.width('100%')
  }
}
```

[]()[]()

#### 示例4（设置滑动条渐变色）

该示例通过colorGradient设置滑动条渐变色，通过focusable、defaultFocus和focusOnTouch设置滑动条支持表冠操作。

```ets
// xxx.ets
@Entry
@Component
struct SliderExample {
  @State inSetValueOne: number = 60
  @State colorGradient: LinearGradient = new LinearGradient([{ color: "#FF0000FF", offset: 0 }, { color: "#FFFF0000", offset: 1 }])
  @State sensitivity: CrownSensitivity | undefined | null = CrownSensitivity.MEDIUM
  scroller: Scroller = new Scroller()

  getIntegerDigits(num: number): string {
    let numRound = Math.round(num);
    return numRound.toString();
  }

  build() {
    Column() {
      Scroll(this.scroller){
        Column() {
          Row() {
            Stack({ alignContent: Alignment.Top }) {
              Slider({
                value: this.inSetValueOne,
                min: 0,
                max: 100,
                style: SliderStyle.NONE,
                direction: Axis.Vertical,
                reverse: true
              })
                .focusable(true)
                .defaultFocus(true)
                .focusOnTouch(true)
                .digitalCrownSensitivity(this.sensitivity)
                .trackColor("#26FFFFFF")
                .trackThickness(52)
                .selectedColor(this.colorGradient)
                .onChange((value: number, mode: SliderChangeMode) => {
                  this.inSetValueOne = value
                })
            }
            .height(233 - 66)
            .width(52)
            .margin({ top: 33, bottom: 33, left: 56 })
            Column() {
              Text('音量')
                .fontSize(19)
                .fontColor("#A9FFFFFF")
                .fontWeight(500)
                .textAlign(TextAlign.Start)
                .margin({ left: 20 })
              Row() {
                Text(this.getIntegerDigits(this.inSetValueOne))
                  .fontSize(52)
                  .fontColor("#FFFFFFFF")
                  .fontWeight(700)
                  .textAlign(TextAlign.Start)
                  .margin({ left: 20 })
                Text('%')
                  .fontSize(19)
                  .fontColor("#FFFFFFFF")
                  .fontWeight(500)
                  .textAlign(TextAlign.Start)
                  .margin({ left: 2 })
              }
            }.alignItems(HorizontalAlign.Start)
          }
          .width(233)
          .height(233)
          .borderRadius(116.5)
          .backgroundColor(Color.Black)
        }
      }
    }.width('100%')
  }
}
```

[]()[]()

#### 示例5（滑动条设置前后缀内容）

该示例实现了Slider组件通过prefix、suffix属性设置滑动条的前后缀内容，定制其内容区以及无障碍属性。设置无障碍属性后，屏幕阅读器将以设置的无障碍内容进行朗读。

```ets
// xxx.ets
import { ComponentContent } from '@kit.ArkUI';

class NodeParams {
  param: ResourceStr = ""

  constructor(param: ResourceStr) {
    this.param = param;
  }
}

@Builder
function textBuilder(params: NodeParams) {
  Text(params.param)
    .fontSize($r('sys.float.Caption_L'))
    .clip(true)
    .textAlign(TextAlign.Center)
    .fontColor(Color.Black)
}

@Entry
@Component
struct SliderExample {
  private pre: string = '低';
  private suf: string = '高';
  private uiContext: UIContext = this.getUIContext();

  private preNode1: ComponentContent<NodeParams> = new ComponentContent(this.uiContext, wrapBuilder(textBuilder), new NodeParams(this.pre));
  private sufNode1: ComponentContent<NodeParams> = new ComponentContent(this.uiContext, wrapBuilder(textBuilder), new NodeParams(this.suf));
  private preNode2: ComponentContent<NodeParams> = new ComponentContent(this.uiContext, wrapBuilder(textBuilder), new NodeParams(this.pre));
  private sufNode2: ComponentContent<NodeParams> = new ComponentContent(this.uiContext, wrapBuilder(textBuilder), new NodeParams(this.suf));
  private preNode3: ComponentContent<NodeParams> = new ComponentContent(this.uiContext, wrapBuilder(textBuilder), new NodeParams(this.pre));
  private sufNode3: ComponentContent<NodeParams> = new ComponentContent(this.uiContext, wrapBuilder(textBuilder), new NodeParams(this.suf));
  private preNode4: ComponentContent<NodeParams> = new ComponentContent(this.uiContext, wrapBuilder(textBuilder), new NodeParams(this.pre));
  private sufNode4: ComponentContent<NodeParams> = new ComponentContent(this.uiContext, wrapBuilder(textBuilder), new NodeParams(this.suf));
  private preNode5: ComponentContent<NodeParams> = new ComponentContent(this.uiContext, wrapBuilder(textBuilder), new NodeParams(this.pre));
  private sufNode5: ComponentContent<NodeParams> = new ComponentContent(this.uiContext, wrapBuilder(textBuilder), new NodeParams(this.suf));
  private preNode6: ComponentContent<NodeParams> = new ComponentContent(this.uiContext, wrapBuilder(textBuilder), new NodeParams(this.pre));
  private sufNode6: ComponentContent<NodeParams> = new ComponentContent(this.uiContext, wrapBuilder(textBuilder), new NodeParams(this.suf));

  build() {
    Column({ space: 8 }) {
      Text('outset slider').fontSize(9).fontColor(0xCCCCCC).width('90%').margin(15)
      Row() {
        Slider({
          value: 50,
          min: 0,
          max: 100,
          style: SliderStyle.OutSet
        })
          .showTips(true)
          .prefix(this.preNode1)
          .suffix(this.sufNode1)
      }
      .width('80%')

      Row() {
        Slider({
          value: 50,
          min: 0,
          max: 100,
          style: SliderStyle.OutSet
        })
          .showTips(true)
          .prefix(this.preNode3)
      }
      .width('80%')

      Row() {
        Slider({
          value: 50,
          min: 0,
          max: 100,
          style: SliderStyle.OutSet
        })
          .showTips(true)
          .suffix(this.sufNode3)
      }
      .width('80%')

      Text('inset slider').fontSize(9).fontColor(0xCCCCCC).width('90%').margin(15)
      Row() {
        Slider({
          value: 50,
          min: 0,
          max: 100,
          style: SliderStyle.InSet
        })
          .blockColor('#191970')
          .trackColor('#ADD8E6')
          .selectedColor('#4169E1')
          .showTips(true)
          .trackThickness(36)
          .prefix(this.preNode2)
          .suffix(this.sufNode2)
      }
      .width('80%')

      Row() {
        Slider({
          value: 50,
          min: 0,
          max: 100,
          style: SliderStyle.InSet
        })
          .blockColor('#191970')
          .trackColor('#ADD8E6')
          .selectedColor('#4169E1')
          .showTips(true)
          .trackThickness(36)
          .prefix(this.preNode4)
      }
      .width('80%')

      Row() {
        Slider({
          value: 50,
          min: 0,
          max: 100,
          style: SliderStyle.InSet
        })
          .blockColor('#191970')
          .trackColor('#ADD8E6')
          .selectedColor('#4169E1')
          .showTips(true)
          .trackThickness(36)
          .suffix(this.sufNode4)
      }
      .width('80%')

      Text('slider Show Step').fontSize(9).fontColor(0xCCCCCC).width('90%').margin(15)
      Row() {
        Slider({
          value: 50,
          min: 0,
          max: 100,
          step:10,
          style: SliderStyle.InSet
        })
          .blockColor('#191970')
          .trackColor('#ADD8E6')
          .selectedColor('#4169E1')
          .showTips(true)
          .trackThickness(36)
          .showSteps(true)
          .prefix(this.preNode5, {
            accessibilityText: 'prefixText',
            accessibilityDescription: 'prefixDescription',
            accessibilityLevel: 'auto',
            accessibilityGroup: true
          })
          .suffix(this.sufNode5, {
            accessibilityText: 'suffixText',
            accessibilityDescription: 'suffixDescription',
            accessibilityLevel: 'auto',
            accessibilityGroup: true
          })
      }
      .width('80%')

      Row() {
        Slider({
          value: 50,
          min: 0,
          max: 100,
          step:10,
          style: SliderStyle.InSet
        })
          .blockColor('#191970')
          .trackColor('#ADD8E6')
          .selectedColor('#4169E1')
          .showTips(true)
          .trackThickness(36)
          .showSteps(true)
          .prefix(this.preNode6, {
            accessibilityText: 'prefixText',
            accessibilityDescription: 'prefixDescription',
            accessibilityLevel: 'auto',
            accessibilityGroup: true
          })
      }
      .width('80%')

      Row() {
        Slider({
          value: 50,
          min: 0,
          max: 100,
          step:10,
          style: SliderStyle.InSet
        })
          .blockColor('#191970')
          .trackColor('#ADD8E6')
          .selectedColor('#4169E1')
          .showTips(true)
          .trackThickness(36)
          .showSteps(true)
          .suffix(this.sufNode6, {
            accessibilityText: 'suffixText',
            accessibilityDescription: 'suffixDescription',
            accessibilityLevel: 'auto',
            accessibilityGroup: true
          })
      }
      .width('80%')
    }.width('100%')
  }
}
```

[]()[]()

#### 示例6（滑动条设置刻度点无障碍文本）

该示例实现了Slider组件通过showSteps属性设置刻度点的无障碍文本信息。设置后，屏幕阅读器将以设置的无障碍内容进行朗读。

```ets
class SliderBlockBorderColorModifier1 implements AttributeModifier<SliderAttribute>{
  optionMaps:Map<number, SliderStepItemAccessibility> = new Map()
    .set(1, {text : "123123"})
    .set(2, {text : "Slider无障碍文本"})
    .set(3, {text : $r('app.string.stepItemText')})
    .set(4, {text : "!@#$%^&*()"});
  applyNormalAttribute(instance: SliderAttribute): void {
    instance.showSteps(true, {stepsAccessibility: this.optionMaps})
  }
}
@Entry
@Component
struct SliderExample {
  @State show: boolean = true;
  @State optionMaps:Map<number, SliderStepItemAccessibility> = new Map();
  private  sliderModifier: SliderBlockBorderColorModifier1 =new SliderBlockBorderColorModifier1()
  aboutToAppear(){
    this.optionMaps.set(1, {text : "123123"})
    this.optionMaps.set(2, {text : "Slider无障碍文本"})
    this.optionMaps.set(3, {text : $r('app.string.app_name')})
    this.optionMaps.set(4, {text : "!@#$%^&*()"})
    this.show = true;
  }
  build() {
    Column({ space: 8 }) {
      Text("show steps").fontSize(12).fontColor(0xCCCCCC).margin(15).width('90%')
      Row() {
        Slider({
          style: SliderStyle.InSet,
          value: 20,
          step: 10,
          max: 50,
          min: 0,
          direction: Axis.Horizontal
        })
          .stepSize(8)
          .stepColor(Color.Yellow)
          .showSteps(true, {stepsAccessibility: this.optionMaps})
      } .width('80%').height(300)
      Divider()
      Text("modifier").fontSize(12).fontColor(0xCCCCCC).margin(15).width('90%')
      Row() {
        Slider({
          style: SliderStyle.InSet,
          value: 20,
          step: 10,
          max: 50,
          min: 0,
          direction: Axis.Horizontal
        })
          .stepSize(8)
          .stepColor(Color.Yellow)
          .attributeModifier(this.sliderModifier)
      } .width('80%').height(300)
      Divider()
    }
  }
}
```

[]()[]()

#### 示例7（设置滑动条的双向绑定）

从API version 11开始，通过将[SliderOptions](#ZH-CN_TOPIC_0000002497604890__slideroptions对象说明)的value属性设置为[$$](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-two-way-sync)绑定的变量，实现数据同步。

```ets
// xxx.ets
@Entry
@Component
struct SliderExample {
  @State valueWith$: number = 40
  @State valueWithout$: number = 40
  build() {
    Column({ space: 20 }) {
      Text("使用$$双向绑定: " + this.valueWith$)
      Slider({
        value: $$this.valueWith$,
        min: 0,
        max: 100,
      })

      Text("不使用$$双向绑定: " + this.valueWithout$)
      Slider({
        value: this.valueWithout$,
        min: 0,
        max: 100,
      })
    }
  }
}
```

[]()[]()

#### 示例8（滑块设置渐变色）

该示例实现了Slider组件通过blockColor属性设置滑块渐变色。

```ets
@Entry
@Component
struct SliderExample {
  @State colorGradient: LinearGradient = new LinearGradient([{ color: "#FFFFFF", offset: 0 }, { color: "#007DFF", offset: 1 }])

  build() {
    Column({ space: 10 }) {
      Slider({
        style:SliderStyle.OutSet,
        min: 0,
        max: 100,
      })
        .blockColor(this.colorGradient)
        .blockSize({width:"50vp",height:"50vp"})
      Slider({
        style:SliderStyle.OutSet,
        min: 0,
        max: 100,
        reverse: true
      })
        .blockColor(this.colorGradient)
        .blockSize({width:"50vp",height:"50vp"})
      Slider({
        style:SliderStyle.InSet,
        min: 0,
        max: 100,
      })
        .blockColor(this.colorGradient)
        .blockSize({width:"50vp",height:"50vp"})
      Slider({
        style:SliderStyle.InSet,
        min: 0,
        max: 100,
        reverse: true
      })
        .blockColor(this.colorGradient)
        .blockSize({width:"50vp",height:"50vp"})
      Slider({
        style:SliderStyle.NONE,
        min: 0,
        max: 100,
      })
        .blockColor(this.colorGradient)
        .blockSize({width:"50vp",height:"50vp"})
      Slider({
        style:SliderStyle.NONE,
        min: 0,
        max: 100,
        reverse: true
      })
        .blockColor(this.colorGradient)
        .blockSize({width:"50vp",height:"50vp"})

      Row({ space: 20 }){
        Slider({
          style:SliderStyle.OutSet,
          min: 0,
          max: 100,
          direction:Axis.Vertical
        })
          .blockColor(this.colorGradient)
          .blockSize({width:"50vp",height:"50vp"})
        Slider({
          style:SliderStyle.OutSet,
          min: 0,
          max: 100,
          reverse: true,
          direction:Axis.Vertical
        })
          .blockColor(this.colorGradient)
          .blockSize({width:"50vp",height:"50vp"})
        Slider({
          style:SliderStyle.InSet,
          min: 0,
          max: 100,
          direction:Axis.Vertical
        })
          .blockColor(this.colorGradient)
          .blockSize({width:"50vp",height:"50vp"})
        Slider({
          style:SliderStyle.InSet,
          min: 0,
          max: 100,
          reverse: true,
          direction:Axis.Vertical
        })
          .blockColor(this.colorGradient)
          .blockSize({width:"50vp",height:"50vp"})
        Slider({
          style:SliderStyle.NONE,
          min: 0,
          max: 100,
          direction:Axis.Vertical
        })
          .blockColor(this.colorGradient)
          .blockSize({width:"50vp",height:"50vp"})
        Slider({
          style:SliderStyle.NONE,
          min: 0,
          max: 100,
          reverse: true,
          direction:Axis.Vertical
        })
          .blockColor(this.colorGradient)
          .blockSize({width:"50vp",height:"50vp"})
      }.height("50%")
    }.width("100%")

  }
}
```