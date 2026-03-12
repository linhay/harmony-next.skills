# ArcSlider

弧形滑动条组件，通常用于在圆形屏幕的穿戴设备中快速调节设置值，如音量调节、亮度调节等应用场景。

 该组件从API version 18开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

#### 导入模块

```ets
import {
  ArcSlider,
  ArcSliderPosition,
  ArcSliderOptions,
  ArcSliderValueOptions,
  ArcSliderLayoutOptions,
  ArcSliderStyleOptions,
  ArcSliderValueOptionsConstructorOptions,
  ArcSliderLayoutOptionsConstructorOptions,
  ArcSliderStyleOptionsConstructorOptions,
  ArcSliderOptionsConstructorOptions
} from '@kit.ArkUI';
```

#### 子组件

无

#### 属性

不支持[通用属性](通用属性.md)。

#### 事件

不支持[通用事件](通用事件.md)。

#### ArcSlider

ArcSlider({ options: ArcSliderOptions })

创建ArcSlider实例，入参是弧形进度条配置选项。

**装饰器类型：**@Component

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

名称类型必填说明options[ArcSliderOptions](#ZH-CN_TOPIC_0000002529284883__arcslideroptions)是

配置弧形滑动条的参数。

默认值：[ArcSliderOptions](#ZH-CN_TOPIC_0000002529284883__arcslideroptions)的各项子属性均取其默认值。

#### ArcSliderOptions

配置弧形Slider的信息。

**装饰器类型：**@ObservedV2

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

#### 属性

名称类型只读可选说明valueOptions[ArcSliderValueOptions](#ZH-CN_TOPIC_0000002529284883__arcslidervalueoptions)否是

配置弧形Slider的数值信息。

默认值：[ArcSliderValueOptions](#ZH-CN_TOPIC_0000002529284883__arcslidervalueoptions)的各项子属性均取其默认值。

**装饰器类型：** @Trace

layoutOptions[ArcSliderLayoutOptions](#ZH-CN_TOPIC_0000002529284883__arcsliderlayoutoptions)否是

配置弧形Slider的布局信息。

默认值：[ArcSliderLayoutOptions](#ZH-CN_TOPIC_0000002529284883__arcsliderlayoutoptions)的各项子属性均取其默认值。

**装饰器类型：** @Trace

styleOptions[ArcSliderStyleOptions](#ZH-CN_TOPIC_0000002529284883__arcsliderstyleoptions)否是

配置弧形Slider的样式信息。

默认值：[ArcSliderStyleOptions](#ZH-CN_TOPIC_0000002529284883__arcsliderstyleoptions)的各项子属性均取其默认值。

**装饰器类型：** @Trace

digitalCrownSensitivity[CrownSensitivity](枚举说明.md#ZH-CN_TOPIC_0000002529284967__crownsensitivity18)否是

设置旋转表冠的灵敏度。

默认值：CrownSensitivity.MEDIUM

**装饰器类型：** @Trace

onTouch[ArcSliderTouchHandler](#ZH-CN_TOPIC_0000002529284883__arcslidertouchhandler)否是

弧形Slider被触摸时，告知应用。

默认值：不传入的情况，无回调。

**装饰器类型：** @Trace

onChange[ArcSliderChangeHandler](#ZH-CN_TOPIC_0000002529284883__arcsliderchangehandler)否是

弧形Slider的进度值发生变化时，告知应用。

默认值：不传入的情况，无回调。

**装饰器类型：** @Trace

onEnlarge[ArcSliderEnlargeHandler](#ZH-CN_TOPIC_0000002529284883__arcsliderenlargehandler)否是

弧形Slider放大或缩小时，告知应用。

默认值：不传入的情况，无回调。

**装饰器类型：** @Trace

#### constructor

constructor(options?: ArcSliderOptionsConstructorOptions)

ArcSliderOptions的构造函数。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

参数名类型必填说明options[ArcSliderOptionsConstructorOptions](#ZH-CN_TOPIC_0000002529284883__arcslideroptionsconstructoroptions)否ArcSliderOptions的构造信息。

#### ArcSliderValueOptions

配置弧形Slider的数值信息。

**装饰器类型：**@ObservedV2

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

#### 属性

名称类型只读可选说明progressnumber否是

设置当前进度值。

默认值：与参数min的取值一致

**装饰器类型：** @Trace

minnumber否是

设置最小值。

默认值：0

**装饰器类型：** @Trace

maxnumber否是

设置最大值。

默认值：100

**说明：**

当出现异常情况min >= max时，min取默认值0，max取默认值100。

progress不在[min, max]范围之内，取min或者max，靠近min取min，靠近max取max。

**装饰器类型：** @Trace

#### constructor

constructor(options?: ArcSliderValueOptionsConstructorOptions)

ArcSliderValueOptions的构造函数。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

参数名类型必填说明options[ArcSliderValueOptionsConstructorOptions](#ZH-CN_TOPIC_0000002529284883__arcslidervalueoptionsconstructoroptions)否ArcSliderValueOptions的构造信息。

#### ArcSliderLayoutOptions

配置弧形Slider的布局信息。

**装饰器类型：**@ObservedV2

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

#### 属性

名称类型只读可选说明reverseboolean否是

设置弧形Slider取值范围是否反向。值为false时表示从上往下滑。

默认值：true，表示从下往上滑动。

**装饰器类型：** @Trace

position[ArcSliderPosition](#ZH-CN_TOPIC_0000002529284883__arcsliderposition)否是

弧形Slider的屏幕显示位置。

默认值：ArcSliderPosition.RIGHT

**装饰器类型：** @Trace

#### constructor

constructor(options?: ArcSliderLayoutOptionsConstructorOptions)

ArcSliderLayoutOptions的构造函数。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

参数名类型必填说明options[ArcSliderLayoutOptionsConstructorOptions](#ZH-CN_TOPIC_0000002529284883__arcsliderlayoutoptionsconstructoroptions)否ArcSliderLayoutOptions的构造信息。

#### ArcSliderStyleOptions

配置弧形Slider的样式信息。

**装饰器类型：**@ObservedV2

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

#### 属性

名称类型只读可选说明trackThicknessnumber否是

正常状态下弧形Slider的描边粗细，单位：vp。

默认值：5

取值范围：[5, 16]，异常值按默认值处理。

**装饰器类型：** @Trace

activeTrackThicknessnumber否是

放大状态下弧形Slider的描边粗细，单位：vp。

默认值：24

取值范围：[24, 36]，异常值按默认值处理。

**装饰器类型：** @Trace

trackColorstring否是

设置描边背景色。

默认值：#33FFFFFF

**装饰器类型：** @Trace

selectedColorstring否是

设置描边高亮色。

默认值：#FF5EA1FF

**装饰器类型：** @Trace

trackBlurnumber否是

设置描边背景模糊值，单位：vp。

默认值：20

设置小于0的值时，按照默认值处理。

**装饰器类型：** @Trace

#### constructor

constructor(options?: ArcSliderStyleOptionsConstructorOptions)

ArcSliderStyleOptions的构造函数。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

参数名类型必填说明options[ArcSliderStyleOptionsConstructorOptions](#ZH-CN_TOPIC_0000002529284883__arcsliderstyleoptionsconstructoroptions)否ArcSliderStyleOptions的构造信息。

#### ArcSliderPosition

配置弧形Slider的屏幕显示位置。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

名称值说明LEFT0弧形Slider的屏幕显示位置在左侧。RIGHT1弧形Slider的屏幕显示位置在右侧。

#### ArcSliderTouchHandler

type ArcSliderTouchHandler = (event: TouchEvent) => void

弧形Slider被触摸时，告知应用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

参数名类型必填说明event[TouchEvent](触摸事件.md#ZH-CN_TOPIC_0000002529444777__touchevent对象说明)是获得TouchEvent对象。

#### ArcSliderChangeHandler

type ArcSliderChangeHandler = (progress: number) => void

弧形Slider的进度值发生变化时，告知应用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

参数名类型必填说明progressnumber是Slider当前的进度值。

#### ArcSliderEnlargeHandler

type ArcSliderEnlargeHandler = (isEnlarged: boolean) => void

弧形Slider放大或缩小时，告知应用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

参数名类型必填说明isEnlargedboolean是

ArcSlider当前是否放大。

isEnlarged为false时，ArcSlider组件处于缩小状态。

isEnlarged为true时，ArcSlider组件处于放大状态。

#### ArcSliderOptionsConstructorOptions

ArcSliderOptions的构造信息。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

名称类型只读可选说明valueOptions[ArcSliderValueOptions](#ZH-CN_TOPIC_0000002529284883__arcslidervalueoptions)否是

配置弧形Slider的数值信息。

默认值：[ArcSliderValueOptions](#ZH-CN_TOPIC_0000002529284883__arcslidervalueoptions)的各项子属性均取其默认值。

layoutOptions[ArcSliderLayoutOptions](#ZH-CN_TOPIC_0000002529284883__arcsliderlayoutoptions)否是

配置弧形Slider的布局信息。

默认值：[ArcSliderLayoutOptions](#ZH-CN_TOPIC_0000002529284883__arcsliderlayoutoptions)的各项子属性均取其默认值。

styleOptions[ArcSliderStyleOptions](#ZH-CN_TOPIC_0000002529284883__arcsliderstyleoptions)否是

配置弧形Slider的样式信息。

默认值：[ArcSliderStyleOptions](#ZH-CN_TOPIC_0000002529284883__arcsliderstyleoptions)的各项子属性均取其默认值。

digitalCrownSensitivity[CrownSensitivity](枚举说明.md#ZH-CN_TOPIC_0000002529284967__crownsensitivity18)否是

设置旋转表冠的灵敏度。

默认值：CrownSensitivity.MEDIUM

onTouch[ArcSliderTouchHandler](#ZH-CN_TOPIC_0000002529284883__arcslidertouchhandler)否是

弧形Slider被触摸时，告知应用。

默认值：不传入的情况，无回调。

onChange[ArcSliderChangeHandler](#ZH-CN_TOPIC_0000002529284883__arcsliderchangehandler)否是

弧形Slider的进度值发生变化时，告知应用。

默认值：不传入的情况，无回调。

onEnlarge[ArcSliderEnlargeHandler](#ZH-CN_TOPIC_0000002529284883__arcsliderenlargehandler)否是

弧形Slider放大或缩小时，告知应用。

默认值：不传入的情况，无回调。

#### ArcSliderValueOptionsConstructorOptions

ArcSliderValueOptions的构造信息。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

名称类型只读可选说明progressnumber否是

设置当前进度值。

默认值：与参数min的取值一致。

minnumber否是

设置最小值。

默认值：0

maxnumber否是

设置最大值。

默认值：100

**说明：**

当出现异常情况min >= max时，min取默认值0，max取默认值100。

progress不在[min, max]范围之内，取min或者max，靠近min取min，靠近max取max。

#### ArcSliderLayoutOptionsConstructorOptions

ArcSliderLayoutValueOptions的构造信息。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

名称类型只读可选说明reverseboolean否是

设置弧形Slider取值范围是否反向。

默认值：true。表示从下往上滑动。

position[ArcSliderPosition](#ZH-CN_TOPIC_0000002529284883__arcsliderposition)否是

弧形Slider的屏幕显示位置。

默认值：ArcSliderPosition.RIGHT

#### ArcSliderStyleOptionsConstructorOptions

ArcSliderStyleOptions的构造信息。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

名称类型只读可选说明trackThicknessnumber否是

正常状态下弧形Slider的描边粗细，单位：vp。

默认值：5

取值范围：[5, 16]，异常值按默认值处理。

activeTrackThicknessnumber否是

放大状态下弧形Slider的描边粗细，单位：vp。

默认值：24

取值范围：[24, 36]，异常值按默认值处理。

trackColorstring否是

设置描边背景色。

默认值：#33FFFFFF

selectedColorstring否是

设置描边高亮色。

默认值：#FF5EA1FF

trackBlurnumber否是

设置描边背景模糊值，单位：vp。

默认值：20

设置小于0的值时，按照默认值处理。

#### 示例

从API version 18开始，该示例展示了ArcSlider组件的基本用法。

```ets
// xxx.ets
import {
  ArcSlider,
  ArcSliderPosition,
  ArcSliderOptions,
  ArcSliderValueOptions,
  ArcSliderLayoutOptions,
  ArcSliderStyleOptions,
  ArcSliderValueOptionsConstructorOptions,
  ArcSliderLayoutOptionsConstructorOptions,
  ArcSliderStyleOptionsConstructorOptions,
  ArcSliderOptionsConstructorOptions
} from '@kit.ArkUI';

@Entry
@ComponentV2
struct ArcSliderExample {
  valueOptionsConstructorOptions: ArcSliderValueOptionsConstructorOptions = {
    progress: 60,
    min: 10,
    max: 110
  };

  layoutOptionsConstructorOptions: ArcSliderLayoutOptionsConstructorOptions = {
    reverse: true,
    position: ArcSliderPosition.RIGHT
  };
  styleOptionsConstructorOptions: ArcSliderStyleOptionsConstructorOptions = {
    trackThickness: 8,
    activeTrackThickness: 30,
    trackColor: '#ffd5d5d5',
    selectedColor: '#ff2787d9',
    trackBlur: 20
  };
  valueOptions: ArcSliderValueOptions = new ArcSliderValueOptions(this.valueOptionsConstructorOptions);
  layoutOptions: ArcSliderLayoutOptions = new ArcSliderLayoutOptions(this.layoutOptionsConstructorOptions);
  styleOptions: ArcSliderStyleOptions = new ArcSliderStyleOptions(this.styleOptionsConstructorOptions);
  arcSliderOptionsConstructorOptions: ArcSliderOptionsConstructorOptions = {
    valueOptions: this.valueOptions,
    layoutOptions: this.layoutOptions,
    styleOptions: this.styleOptions,
    digitalCrownSensitivity:CrownSensitivity.LOW,
    onTouch: (event: TouchEvent) => {
    },
    onChange: (progress: number) => {
    },
    onEnlarge: (isEnlarged: boolean) => {
    }
  };
  arcSliderOptions: ArcSliderOptions = new ArcSliderOptions(this.arcSliderOptionsConstructorOptions);

  build() {
    Column() {
      ArcSlider({ options: this.arcSliderOptions })}
      .width('100%')
  }
}
```