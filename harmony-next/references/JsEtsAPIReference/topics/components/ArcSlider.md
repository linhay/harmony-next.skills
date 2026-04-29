# ArcSlider

弧形滑动条组件，通常用于在圆形屏幕的穿戴设备中快速调节设置值，如音量调节、亮度调节等应用场景。


 该组件从API version 18开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

- 该组件支持在Phone、PC/2in1、Tablet、TV、Wearable设备上使用。API version 22及以前版本，在Phone、PC/2in1、Tablet、TV上使用会编译告警，但可以正常运行。

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

不支持[通用属性]([通用属性](../misc/通用属性.md).md)。

#### 事件

不支持[通用事件]([通用事件](../misc/通用事件.md).md)。

#### ArcSlider

ArcSlider({ options: ArcSliderOptions })

创建ArcSlider实例，入参是弧形进度条配置选项。

**装饰器类型：**@Component

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | ArcSliderOptions | 是 | 配置弧形滑动条的参数。 默认值：ArcSliderOptions的各项子属性均取其默认值。 |

#### ArcSliderOptions

配置弧形Slider的信息。

**装饰器类型：**@ObservedV2

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

#### 属性

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| valueOptions | ArcSliderValueOptions | 否 | 是 | 配置弧形Slider的数值信息。 默认值：ArcSliderValueOptions的各项子属性均取其默认值。 装饰器类型： @Trace |
| layoutOptions | ArcSliderLayoutOptions | 否 | 是 | 配置弧形Slider的布局信息。 默认值：ArcSliderLayoutOptions的各项子属性均取其默认值。 装饰器类型： @Trace |
| styleOptions | ArcSliderStyleOptions | 否 | 是 | 配置弧形Slider的样式信息。 默认值：ArcSliderStyleOptions的各项子属性均取其默认值。 装饰器类型： @Trace |
| digital[CrownSensitivity](枚举说明.md#ZH-CN_TOPIC_0000002529284967__crownsensitivity18) | CrownSensitivity | 否 | 是 | 设置旋转表冠的灵敏度。 默认值：CrownSensitivity.MEDIUM 装饰器类型： @Trace |
| onTouch | ArcSliderTouchHandler | 否 | 是 | 弧形Slider被触摸时，告知应用。 默认值：不传入的情况，无回调。 装饰器类型： @Trace |
| onChange | ArcSliderChangeHandler | 否 | 是 | 弧形Slider的进度值发生变化时，告知应用。 默认值：不传入的情况，无回调。 装饰器类型： @Trace |
| onEnlarge | ArcSliderEnlargeHandler | 否 | 是 | 弧形Slider放大或缩小时，告知应用。 默认值：不传入的情况，无回调。 装饰器类型： @Trace |

#### constructor

constructor(options?: ArcSliderOptionsConstructorOptions)

ArcSliderOptions的构造函数。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | ArcSliderOptionsConstructorOptions | 否 | ArcSliderOptions的构造信息。 |

#### ArcSliderValueOptions

配置弧形Slider的数值信息。

**装饰器类型：**@ObservedV2

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

#### 属性

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| progress | number | 否 | 是 | 设置当前进度值。 默认值：与参数min的取值一致 装饰器类型： @Trace |
| min | number | 否 | 是 | 设置最小值。 默认值：0 装饰器类型： @Trace |
| max | number | 否 | 是 | 设置最大值。 默认值：100 说明： 当出现异常情况min >= max时，min取默认值0，max取默认值100。 progress不在[min, max]范围之内，取min或者max，靠近min取min，靠近max取max。 装饰器类型： @Trace |

#### constructor

constructor(options?: ArcSliderValueOptionsConstructorOptions)

ArcSliderValueOptions的构造函数。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | ArcSliderValueOptionsConstructorOptions | 否 | ArcSliderValueOptions的构造信息。 |

#### ArcSliderLayoutOptions

配置弧形Slider的布局信息。

**装饰器类型：**@ObservedV2

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

#### 属性

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| reverse | boolean | 否 | 是 | 设置弧形Slider取值范围是否反向。值为false时表示从上往下滑。 默认值：true，表示从下往上滑动。 装饰器类型： @Trace |
| position | ArcSliderPosition | 否 | 是 | 弧形Slider的屏幕显示位置。 默认值：ArcSliderPosition.RIGHT 装饰器类型： @Trace |

#### constructor

constructor(options?: ArcSliderLayoutOptionsConstructorOptions)

ArcSliderLayoutOptions的构造函数。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | ArcSliderLayoutOptionsConstructorOptions | 否 | ArcSliderLayoutOptions的构造信息。 |

#### ArcSliderStyleOptions

配置弧形Slider的样式信息。

**装饰器类型：**@ObservedV2

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

#### 属性

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| trackThickness | number | 否 | 是 | 正常状态下弧形Slider的描边粗细，单位：vp。 默认值：5 取值范围：[5, 16]，异常值按默认值处理。 装饰器类型： @Trace |
| activeTrackThickness | number | 否 | 是 | 放大状态下弧形Slider的描边粗细，单位：vp。 默认值：24 取值范围：[24, 36]，异常值按默认值处理。 装饰器类型： @Trace |
| trackColor | string | 否 | 是 | 设置描边背景色。 默认值：#33FFFFFF 装饰器类型： @Trace |
| selectedColor | string | 否 | 是 | 设置描边高亮色。 默认值：#FF5EA1FF 装饰器类型： @Trace |
| trackBlur | number | 否 | 是 | 设置描边背景模糊值，单位：vp。 默认值：20 设置小于0的值时，按照默认值处理。 装饰器类型： @Trace |

#### constructor

constructor(options?: ArcSliderStyleOptionsConstructorOptions)

ArcSliderStyleOptions的构造函数。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | ArcSliderStyleOptionsConstructorOptions | 否 | ArcSliderStyleOptions的构造信息。 |

#### ArcSliderPosition

配置弧形Slider的屏幕显示位置。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

| 名称 | 值 | 说明 |
| --- | --- | --- |
| LEFT | 0 | 弧形Slider的屏幕显示位置在左侧。 |
| RIGHT | 1 | 弧形Slider的屏幕显示位置在右侧。 |

#### ArcSliderTouchHandler

type ArcSliderTouchHandler = (event: [TouchEvent](触摸事件.md#ZH-CN_TOPIC_0000002529444777__touchevent对象说明)) => void

弧形Slider被触摸时，告知应用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [TouchEvent](触摸事件.md#ZH-CN_TOPIC_0000002529444777__touchevent对象说明) | 是 | 获得TouchEvent对象。 |

#### ArcSliderChangeHandler

type ArcSliderChangeHandler = (progress: number) => void

弧形Slider的进度值发生变化时，告知应用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| progress | number | 是 | Slider当前的进度值。 |

#### ArcSliderEnlargeHandler

type ArcSliderEnlargeHandler = (isEnlarged: boolean) => void

弧形Slider放大或缩小时，告知应用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isEnlarged | boolean | 是 | ArcSlider当前是否放大。 isEnlarged为false时，ArcSlider组件处于缩小状态。 isEnlarged为true时，ArcSlider组件处于放大状态。 |

#### ArcSliderOptionsConstructorOptions

ArcSliderOptions的构造信息。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| valueOptions | ArcSliderValueOptions | 否 | 是 | 配置弧形Slider的数值信息。 默认值：ArcSliderValueOptions的各项子属性均取其默认值。 |
| layoutOptions | ArcSliderLayoutOptions | 否 | 是 | 配置弧形Slider的布局信息。 默认值：ArcSliderLayoutOptions的各项子属性均取其默认值。 |
| styleOptions | ArcSliderStyleOptions | 否 | 是 | 配置弧形Slider的样式信息。 默认值：ArcSliderStyleOptions的各项子属性均取其默认值。 |
| digital[CrownSensitivity](枚举说明.md#ZH-CN_TOPIC_0000002529284967__crownsensitivity18) | CrownSensitivity | 否 | 是 | 设置旋转表冠的灵敏度。 默认值：CrownSensitivity.MEDIUM |
| onTouch | ArcSliderTouchHandler | 否 | 是 | 弧形Slider被触摸时，告知应用。 默认值：不传入的情况，无回调。 |
| onChange | ArcSliderChangeHandler | 否 | 是 | 弧形Slider的进度值发生变化时，告知应用。 默认值：不传入的情况，无回调。 |
| onEnlarge | ArcSliderEnlargeHandler | 否 | 是 | 弧形Slider放大或缩小时，告知应用。 默认值：不传入的情况，无回调。 |

#### ArcSliderValueOptionsConstructorOptions

ArcSliderValueOptions的构造信息。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| progress | number | 否 | 是 | 设置当前进度值。 默认值：与参数min的取值一致。 |
| min | number | 否 | 是 | 设置最小值。 默认值：0 |
| max | number | 否 | 是 | 设置最大值。 默认值：100 说明： 当出现异常情况min >= max时，min取默认值0，max取默认值100。 progress不在[min, max]范围之内，取min或者max，靠近min取min，靠近max取max。 |

#### ArcSliderLayoutOptionsConstructorOptions

ArcSliderLayoutValueOptions的构造信息。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| reverse | boolean | 否 | 是 | 设置弧形Slider取值范围是否反向。 默认值：true。表示从下往上滑动。 |
| position | ArcSliderPosition | 否 | 是 | 弧形Slider的屏幕显示位置。 默认值：ArcSliderPosition.RIGHT |

#### ArcSliderStyleOptionsConstructorOptions

ArcSliderStyleOptions的构造信息。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| trackThickness | number | 否 | 是 | 正常状态下弧形Slider的描边粗细，单位：vp。 默认值：5 取值范围：[5, 16]，异常值按默认值处理。 |
| activeTrackThickness | number | 否 | 是 | 放大状态下弧形Slider的描边粗细，单位：vp。 默认值：24 取值范围：[24, 36]，异常值按默认值处理。 |
| trackColor | string | 否 | 是 | 设置描边背景色。 默认值：#33FFFFFF |
| selectedColor | string | 否 | 是 | 设置描边高亮色。 默认值：#FF5EA1FF |
| trackBlur | number | 否 | 是 | 设置描边背景模糊值，单位：vp。 默认值：20 设置小于0的值时，按照默认值处理。 |

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
```

![image](public_sys-resources/zh-cn_image_0000002553364917.webp)
