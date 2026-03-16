# HdsListItemCard

本模块提供一个HdsListItemCard组件，提升视觉体验，统一组件风格样式，应用使用HdsListItemCard组件实现多设备上的系统列表样式。

**起始版本：**6.0.0(20)

#### 导入模块

```ets
import { HdsListItemCard } from '@kit.UIDesignKit';
```

#### 接口

HdsListItemCard(options: HdsListItemCardOptions)

HdsListItemCard列表项组件。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**设备行为异常：**该接口在TV中与ux规范不一致（获焦态和悬停态组件未放大，获焦态背板颜色未变化，Button内部的text默认颜色等），在其他设备类型中可正常使用。

**起始版本：**6.0.0(20)

**参数：**

参数名

类型

必填

说明

options

[HdsListItemCardOptions](#section6323195713321)

是

HdsListItemCard列表项内容。

#### PrefixItem

定义PrefixItem类，HdsListItemCard列表项的A区（列表左侧）元素。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

#### PrefixImage

PrefixImage继承自父类[PrefixItem](#section68021033134910)，A区（列表左侧）Image元素，穿戴设备中Image大小不可修改，为固定值46vp*46vp。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

#### 属性

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

名称

类型

只读

可选

说明

options

[ImageClickOptions](#section4353179193911)

否

是

A区（列表左侧）Image元素的配置项。

#### constructor

constructor(options?: ImageClickOptions)

PrefixImage的构造函数。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

**参数：**

参数名

类型

必填

说明

options

[ImageClickOptions](#section4353179193911)

否

A区（列表左侧）Image元素的配置项。

#### PrefixIcon

PrefixIcon继承自父类[PrefixItem](#section68021033134910)，A区（列表左侧）Icon元素。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

#### 属性

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

名称

类型

只读

可选

说明

options

[PrefixIconOptions](#section232815719440)

否

是

A区（列表左侧）Icon元素的配置项。

#### constructor

constructor(options?: PrefixIconOptions)

PrefixIcon的构造函数。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

**参数：**

参数名

类型

必填

说明

options

[PrefixIconOptions](#section232815719440)

否

A区（列表左侧）Icon元素的配置项。

#### PrefixBadge

PrefixBadge继承自父类[PrefixItem](#section68021033134910)，A区（列表左侧）Badge元素。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

#### 属性

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

名称

类型

只读

可选

说明

options

[BadgeOptions](#section1862211717471)

否

是

A区（列表左侧）Badge元素的配置项。

#### constructor

constructor(options?: BadgeOptions)

PrefixBadge的构造函数。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

**参数：**

参数名

类型

必填

说明

options

[BadgeOptions](#section1862211717471)

否

A区（列表左侧）Badge元素的配置项。

#### PrefixSwitch

PrefixSwitch继承自父类[PrefixItem](#section68021033134910)，A区（列表左侧）Switch元素。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

#### 属性

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

名称

类型

只读

可选

说明

options

[CheckOptions](#section740053134818)

否

是

A区（列表左侧）Switch元素的配置项。

#### constructor

constructor(options?: CheckOptions)

PrefixSwitch的构造函数。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

**参数：**

参数名

类型

必填

说明

options

[CheckOptions](#section740053134818)

否

A区（列表左侧）Switch元素的配置项。

#### PrefixToggleButton

PrefixToggleButton继承自父类[PrefixItem](#section68021033134910)，A区（列表左侧）ToggleButton元素。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

#### 属性

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

名称

类型

只读

可选

说明

options

[ToggleButtonOptions](#section168210477514)

否

是

A区（列表左侧）ToggleButton元素的配置项。

#### constructor

constructor(options?: ToggleButtonOptions)

PrefixToggleButton的构造函数。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

**参数：**

参数名

类型

必填

说明

options

[ToggleButtonOptions](#section168210477514)

否

A区（列表左侧）ToggleButton元素的配置项。

#### PrefixButton

PrefixButton继承自父类[PrefixItem](#section68021033134910)，A区（列表左侧）Button元素。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

#### 属性

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

名称

类型

只读

可选

说明

options

[ButtonOptions](#section35631920155512)

否

是

A区（列表左侧）Button元素的配置项。

#### constructor

constructor(options?: ButtonOptions)

PrefixButton的构造函数。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

**参数：**

参数名

类型

必填

说明

options

[ButtonOptions](#section35631920155512)

否

A区（列表左侧）Button元素的配置项。

#### PrefixCustomBuilder

PrefixCustomBuilder继承自父类[PrefixItem](#section68021033134910)，A区（列表左侧）自定义内容，建议使用Function.bind(this)的方式传入（Function为自定义函数）。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

#### 属性

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

名称

类型

只读

可选

说明

customBuilder

[CustomBuilder](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#custombuilder8)

否

是

A区（列表左侧）自定义内容。

#### constructor

constructor(customBuilder?: CustomBuilder)

PrefixCustomBuilder的构造函数。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

**参数：**

参数名

类型

必填

说明

customBuilder

[CustomBuilder](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#custombuilder8)

否

A区（列表左侧）自定义内容。

#### SuffixItem

定义SuffixItem类，HdsListItemCard列表项的C区（列表右侧）元素。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

#### SuffixText

SuffixText继承自父类[SuffixItem](#section3859111120123)，C区（列表右侧）Text元素。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

#### 属性

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

名称

类型

只读

可选

说明

options

[TextOptions](#section4754175319)

否

是

C区（列表右侧）Text元素的配置项。

#### constructor

constructor(options?: TextOptions)

SuffixText的构造函数。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

**参数：**

参数名

类型

必填

说明

options

[TextOptions](#section4754175319)

否

C区（列表右侧）Text元素的配置项。

#### SuffixImage

SuffixImage继承自父类[SuffixItem](#section3859111120123)，C区（列表右侧）Image元素。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

#### 属性

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

名称

类型

只读

可选

说明

options

[ImageClickOptions](#section4353179193911)

否

是

C区（列表右侧）Image元素的配置项。

#### constructor

constructor(options?: ImageClickOptions)

SuffixImage的构造函数。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

**参数：**

参数名

类型

必填

说明

options

[ImageClickOptions](#section4353179193911)

否

C区（列表右侧）Image元素的配置项。

#### SuffixLoadingProgress

SuffixLoadingProgress继承自父类[SuffixItem](#section3859111120123)，C区（列表右侧）LoadingProgress元素。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

#### 属性

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

名称

类型

只读

可选

说明

options

[ColorOptions](#section169543387546)

否

是

C区（列表右侧）LoadingProgress元素的配置项。

#### constructor

constructor(options?: ColorOptions)

SuffixLoadingProgress的构造函数。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

**参数：**

参数名

类型

必填

说明

options

[ColorOptions](#section169543387546)

否

C区（列表右侧）LoadingProgress元素的配置项。

#### SuffixRadio

SuffixRadio继承自父类[SuffixItem](#section3859111120123)，C区（列表右侧）Radio元素。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

#### 属性

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

名称

类型

只读

可选

说明

options

[CheckOptions](#section740053134818)

否

是

C区（列表右侧）Radio元素的配置项。

#### constructor

constructor(options?: CheckOptions)

SuffixRadio的构造函数。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

**参数：**

参数名

类型

必填

说明

options

[CheckOptions](#section740053134818)

否

C区（列表右侧）Radio元素的配置项。

#### SuffixCheckbox

SuffixCheckbox继承自父类[SuffixItem](#section3859111120123)，C区（列表右侧）Checkbox元素。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

#### 属性

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

名称

类型

只读

可选

说明

options

[CheckOptions](#section740053134818)

否

是

C区（列表右侧）Checkbox元素的配置项。

#### constructor

constructor(options?: CheckOptions)

SuffixCheckbox的构造函数。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

**参数：**

参数名

类型

必填

说明

options

[CheckOptions](#section740053134818)

否

C区（列表右侧）Checkbox元素的配置项。

#### SuffixSwitch

SuffixSwitch继承自父类[SuffixItem](#section3859111120123)，C区（列表右侧）Switch元素。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

#### 属性

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

名称

类型

只读

可选

说明

options

[CheckOptions](#section740053134818)

否

是

C区（列表右侧）Switch元素的配置项。

#### constructor

constructor(options?: CheckOptions)

SuffixSwitch的构造函数。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

**参数：**

参数名

类型

必填

说明

options

[CheckOptions](#section740053134818)

否

C区（列表右侧）Switch元素的配置项。

#### SuffixArrow

SuffixArrow继承自父类[SuffixItem](#section3859111120123)，C区（列表右侧）Arrow元素。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

#### 属性

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

名称

类型

只读

可选

说明

options

[ColorOptions](#section169543387546)

否

是

C区（列表右侧）Arrow元素的配置项。

#### constructor

constructor(options?: ColorOptions)

SuffixArrow的构造函数。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

**参数：**

参数名

类型

必填

说明

options

[ColorOptions](#section169543387546)

否

C区（列表右侧）Arrow元素的配置项。

#### SuffixBadge

SuffixBadge继承自父类[SuffixItem](#section3859111120123)，C区（列表右侧）Badge元素。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

#### 属性

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

名称

类型

只读

可选

说明

options

[BadgeOptions](#section1862211717471)

否

是

C区（列表右侧）Badge元素的配置项。

#### constructor

constructor(options?: BadgeOptions)

SuffixBadge的构造函数。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

**参数：**

参数名

类型

必填

说明

options

[BadgeOptions](#section1862211717471)

否

C区（列表右侧）Badge元素的配置项。

#### SuffixButton

SuffixButton继承自父类[SuffixItem](#section3859111120123)，C区（列表右侧）Button元素。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

#### 属性

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

名称

类型

只读

可选

说明

options

[ButtonOptions](#section35631920155512)

否

是

C区（列表右侧）Button元素的配置项。

#### constructor

constructor(options?: ButtonOptions)

SuffixButton的构造函数。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

**参数：**

参数名

类型

必填

说明

options

[ButtonOptions](#section35631920155512)

否

C区（列表右侧）Button元素的配置项。

#### SuffixIcon

SuffixIcon继承自父类[SuffixItem](#section3859111120123)，C区（列表右侧）单个Icon元素。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

#### 属性

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

名称

类型

只读

可选

说明

options

[SuffixIconOptions](#section4745511195712)

否

是

C区（列表右侧）单个Icon元素的配置项。

#### constructor

constructor(options?: SuffixIconOptions)

SuffixIcon的构造函数。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

**参数：**

参数名

类型

必填

说明

options

[SuffixIconOptions](#section4745511195712)

否

C区（列表右侧）单个Icon元素的配置项。

#### SuffixSubIcon

SuffixSubIcon继承自父类[SuffixItem](#section3859111120123)，C区（列表右侧）两个Icon元素。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

#### 属性

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

名称

类型

只读

可选

说明

options

[SuffixIconOptions](#section4745511195712)

否

是

C区（列表右侧）第一个Icon元素的配置项。

subOptions

[SuffixIconOptions](#section4745511195712)

否

是

C区（列表右侧）第二个Icon元素的配置项。

#### constructor

constructor(options?: SuffixIconOptions, subOptions?: SuffixIconOptions)

SuffixSubIcon的构造函数。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

**参数：**

参数名

类型

必填

说明

options

[SuffixIconOptions](#section4745511195712)

否

C区（列表右侧）第一个Icon元素的配置项。

subOptions

[SuffixIconOptions](#section4745511195712)

否

C区（列表右侧）第二个Icon元素的配置项。

#### SuffixSelect

SuffixSelect继承自父类[SuffixItem](#section3859111120123)，C区（列表右侧）Select元素。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

#### 属性

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

名称

类型

只读

可选

说明

options

[SelectStyle](#section1585419719586)

否

是

C区（列表右侧）Select元素的配置项。

#### constructor

constructor(options?: SelectStyle)

SuffixSelect的构造函数。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

**参数：**

参数名

类型

必填

说明

options

[SelectStyle](#section1585419719586)

否

C区（列表右侧）Select的配置项。

#### SuffixToggleButton

SuffixToggleButton继承自父类[SuffixItem](#section3859111120123)，C区（列表右侧）ToggleButton元素。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

#### 属性

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

名称

类型

只读

可选

说明

options

[ToggleButtonOptions](#section168210477514)

否

是

C区（列表右侧）ToggleButton的配置项。

#### constructor

constructor(options?: ToggleButtonOptions)

SuffixToggleButton的构造函数。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

**参数：**

参数名

类型

必填

说明

options

[ToggleButtonOptions](#section168210477514)

否

C区（列表右侧）ToggleButton的配置项。

#### SuffixBadgeAndArrow

SuffixBadgeAndArrow继承自父类[SuffixItem](#section3859111120123)，C区（列表右侧）Badge和Arrow组合元素。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

#### 属性

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

名称

类型

只读

可选

说明

badgeOptions

[BadgeOptions](#section1862211717471)

否

是

C区（列表右侧）Badge和Arrow组合元素中Badge的配置项。

arrowOptions

[ColorOptions](#section169543387546)

否

是

C区（列表右侧）Badge和Arrow组合元素中Arrow的配置项。

#### constructor

constructor(badgeOptions?: BadgeOptions, arrowOptions?: ColorOptions)

SuffixBadgeAndArrow的构造函数。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

**参数：**

参数名

类型

必填

说明

badgeOptions

[BadgeOptions](#section1862211717471)

否

C区（列表右侧）Badge和Arrow组合元素中Badge的配置项。

arrowOptions

[ColorOptions](#section169543387546)

否

C区（列表右侧）Badge和Arrow组合元素中Arrow的配置项。

#### SuffixTextAndArrow

SuffixTextAndArrow继承自父类[SuffixItem](#section3859111120123)，C区（列表右侧）Text和Arrow组合元素。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

#### 属性

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

名称

类型

只读

可选

说明

textOptions

[TextOptions](#section4754175319)

否

是

C区（列表右侧）Text和Arrow组合元素中Text的配置项。

arrowOptions

[ColorOptions](#section169543387546)

否

是

C区（列表右侧）Text和Arrow组合元素中Arrow的配置项

#### constructor

constructor(textOptions?: TextOptions, arrowOptions?: ColorOptions)

SuffixTextAndArrow的构造函数。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

**参数：**

参数名

类型

必填

说明

textOptions

[TextOptions](#section4754175319)

否

C区（列表右侧）Text和Arrow组合元素中Text的配置项。

arrowOptions

[ColorOptions](#section169543387546)

否

C区（列表右侧）Text和Arrow组合元素中Arrow的配置项。

#### SuffixArrowIconText

SuffixArrowIconText继承自父类[SuffixItem](#section3859111120123)，C区（列表右侧）Arrow、Text和Arrow组合元素。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

#### 属性

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

名称

类型

只读

可选

说明

options

[SuffixArrowIconTextOptions](#section1946963582419)

否

是

C区（列表右侧）Text、Arrow和Icon组合元素的配置项。

#### constructor

constructor(options?: SuffixArrowIconTextOptions)

SuffixArrowIconText的构造函数。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

**参数：**

参数名

类型

必填

说明

options

[SuffixArrowIconTextOptions](#section1946963582419)

否

C区（列表右侧）Text、Arrow和Icon组合元素的配置项。

#### SuffixCustomBuilder

SuffixCustomBuilder继承自父类[SuffixItem](#section3859111120123)，C区（列表右侧）自定义内容，建议使用Function.bind(this)的方式传入（Function为自定义函数）。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

#### 属性

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

名称

类型

只读

可选

说明

customBuilder

[CustomBuilder](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#custombuilder8)

否

是

C区（列表右侧）自定义内容。

#### constructor

constructor(customBuilder?: CustomBuilder)

SuffixCustomBuilder的构造函数。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

**参数：**

参数名

类型

必填

说明

customBuilder

[CustomBuilder](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#custombuilder8)

否

C区（列表右侧）自定义内容。

#### HdsListItemCardOptions

HdsListItemCard列表项内元素配置选项。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**设备行为异常：**该接口在TV中与ux规范不一致（获焦态和悬停态组件未放大，获焦态背板颜色未变化，Button内部的text默认颜色等），在其他设备类型中可正常使用。

**起始版本：**6.0.0(20)

名称

类型

只读

可选

说明

prefixItem

[PrefixItem](#section68021033134910)

否

是

HdsListItemCard列表项的A区（左侧）元素。

textItem

[TextItemOptions](#section1905201905812)

否

是

HdsListItemCard列表项的B区（中间）元素。

suffixItem

[SuffixItem](#section3859111120123)

否

是

HdsListItemCard列表项的C区（右侧）元素。

onClick

[OnClickCallback](#section975195614188)

否

是

HdsListItemCard列表项的点击回调。

cardHeight

[Dimension](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#dimension10)

否

是

HdsListItemCard列表项的高度，目前不支持使用Percentage设置。

cardWidth

[Dimension](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#dimension10)

否

是

HdsListItemCard列表项的宽度，目前不支持使用Percentage设置。

cardBackgroundColor

[ResourceColor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resourcecolor)

否

是

HdsListItemCard列表项的背景颜色。

cardBorderRadius

[Dimension](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#dimension10)

否

是

HdsListItemCard列表项的边框圆角。

cardPrefixMargin

[Dimension](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#dimension10)

否

是

HdsListItemCard列表项距离屏幕左侧的边距。

cardSuffixMargin

[Dimension](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#dimension10)

否

是

HdsListItemCard列表项距离屏幕右侧的边距。

hoverBorderRadius

[Dimension](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#dimension10)

否

是

HdsListItemCard列表项在悬浮状态下的边框圆角。

enable

boolean

否

是

HdsListItemCard列表项是否被启用。

true：列表项被启用。

false：列表项被禁用。

默认值：true。

cardId

string

否

是

HdsListItemCard列表项的Id。

accessibilityOptions

[AccessibilityOptions](#section16412175163116)

否

是

HdsListItemCard列表项的无障碍播放能力选项。

#### TextItemOptions

HdsListItemCard列表项的B区（列表中间）元素配置选项。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

名称

类型

只读

可选

说明

primaryText

[TextOptions](#section4754175319)

否

是

B区（列表中间）元素的标题内容。

primaryPrefixSymbol

[TextSymbolGlyphOptions](#section9694202504117)

否

是

标题内容左侧第一个Symbol图标。

primarySuffixSymbol

[TextSymbolGlyphOptions](#section9694202504117)

否

是

标题内容右侧第一个Symbol图标。

primaryPrefixSubSymbol

[TextSymbolGlyphOptions](#section9694202504117)

否

是

标题内容左侧Symbol第二个图标，仅在左侧第一个Symbol图标存在时才显示。

primarySuffixSubSymbol

[TextSymbolGlyphOptions](#section9694202504117)

否

是

标题内容右侧Symbol第二个图标，仅在右侧第一个Symbol图标存在时才显示。

secondaryText

[TextOptions](#section4754175319)

否

是

B区（列表中间）元素的副标题内容。

secondaryPrefixSymbol

[TextSymbolGlyphOptions](#section9694202504117)

否

是

副标题内容左侧第一个Symbol图标。

secondarySuffixSymbol

[TextSymbolGlyphOptions](#section9694202504117)

否

是

副标题内容右侧第一个Symbol图标。

secondaryPrefixSubSymbol

[TextSymbolGlyphOptions](#section9694202504117)

否

是

副标题内容左侧Symbol第二个图标，仅在左侧第一个Symbol图标存在时才显示。

secondarySuffixSubSymbol

[TextSymbolGlyphOptions](#section9694202504117)

否

是

副标题内容右侧Symbol第二个图标，仅在右侧第一个Symbol图标存在时才显示。

description

[TextOptions](#section4754175319)

否

是

B区（列表中间）元素的描述内容。

descriptionPrefixSymbol

[TextSymbolGlyphOptions](#section9694202504117)

否

是

描述内容左侧第一个Symbol图标。

descriptionSuffixSymbol

[TextSymbolGlyphOptions](#section9694202504117)

否

是

描述内容右侧第一个Symbol图标。

descriptionPrefixSubSymbol

[TextSymbolGlyphOptions](#section9694202504117)

否

是

描述内容左侧Symbol第二个图标，仅在左侧第一个Symbol图标存在时才显示。

descriptionSuffixSubSymbol

[TextSymbolGlyphOptions](#section9694202504117)

否

是

描述内容右侧Symbol第二个图标，仅在右侧第一个Symbol图标存在时才显示。

customBuilder

[CustomBuilder](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#custombuilder8)

否

是

B区（列表中间）自定义内容，建议使用Function.bind(this)的方式传入（Function为自定义函数）。

TextItemOptions中customBuilder优先级高于其它接口。

#### AccessibilityOptions

HdsListItemCard无障碍播放能力选项。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

名称

类型

只读

可选

说明

accessibilityText

[ResourceStr](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resourcestr)

否

是

列表的无障碍文本属性。当组件不包含文本属性时，屏幕朗读选中此组件时不播报，使用者无法清楚地知道当前选中了什么组件。为了解决此场景，开发人员可为不包含文字信息的组件设置无障碍文本，当屏幕朗读选中此组件时播报无障碍文本的内容，帮助屏幕朗读的使用者清楚地知道自己选中了什么组件。

默认值：""。

accessibilityDescription

[ResourceStr](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resourcestr)

否

是

列表的无障碍描述。此描述用于向用户详细解释当前组件，开发人员应为组件的这一属性提供较为详尽的文本说明，以协助用户理解即将执行的操作及其可能产生的后果。特别是当这些后果无法仅从组件的属性和无障碍文本中直接获知时。如果组件同时具备文本属性和无障碍说明属性，当组件被选中时，系统将首先播报组件的文本属性，随后播报无障碍说明属性的内容。

默认值：类型为switch时，默认值为"单指双击即可开启/关闭"，类型为checkbox时，默认值为"单指双击即可选中/取消选中"，其它类型默认值为"单指双击即可执行"。

accessibilityLevel

[ResourceStr](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resourcestr)

否

是

无障碍重要性，用于控制当前项是否可被无障碍辅助服务所识别。

支持的值为：

"auto"：当前组件会转换"yes"。

"yes"：当前组件可被无障碍辅助服务所识别。

"no"：当前组件不可被无障碍辅助服务所识别。

"no-hide-descendants"：当前组件及其所有子组件不可被无障碍辅助服务所识别。

默认值："auto"。

#### ImageOptions

HdsListItemCard中Image样式选项。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

名称

类型

只读

可选

说明

image

[ImageType](#section1650110443168)

否

是

Image资源类型。

modifier

[ImageModifier](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-attribute-modifier#自定义modifier)

否

是

Image属性样式修改器。

#### ImageClickOptions

HdsListItemCard中支持点击的Image样式选项。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

名称

类型

只读

可选

说明

image

[ImageType](#section1650110443168)

否

是

Image资源类型。

modifier

[ImageModifier](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-attribute-modifier#自定义modifier)

否

是

Image属性样式修改器。

onClick

[OnClickCallback](#section975195614188)

否

是

Image的点击回调。

enable

boolean

否

是

Image是否被启用。

true：Image被启用。

false：Image被禁用。

默认值：true。

accessibilityOptions

[AccessibilityOptions](#section16412175163116)

否

是

Image的无障碍播放能力选项。

#### SymbolGlyphOptions

HdsListItemCard中Symbol样式选项。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

名称

类型

只读

可选

说明

symbol

[SymbolType](#section19341944531)

否

是

Symbol资源类型。

#### TextSymbolGlyphOptions

HdsListItemCard中B区（列表中间）Text左右两侧的Symbol样式选项。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

名称

类型

只读

可选

说明

symbol

[SymbolType](#section19341944531)

否

是

B区（列表中间）Text左右两侧Symbol资源类型。

onClick

[OnClickCallback](#section975195614188)

否

是

B区（列表中间）Text左右两侧Symbol的点击回调。

enable

boolean

否

是

B区（列表中间）Text左右两侧Symbol是否被启用。

true：B区（列表中间）Text左右两侧Symbol被启用。

false：B区（列表中间）Text左右两侧Symbol被禁用。

默认值：true。

accessibilityOptions

[AccessibilityOptions](#section16412175163116)

否

是

B区（列表中间）Text左右两侧Symbol的无障碍播放能力选项。

#### PrefixIconOptions

HdsListItemCard中A区（列表左侧）Icon样式选项。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

名称

类型

只读

可选

说明

iconSize

[IconSize](#section6603131919318)

否

是

A区（列表左侧）Icon样式。

默认值：[IconSize](#section6603131919318).SYSTEM_ICON。

iconValue

[PrefixIconType](#section9201529151513)

否

是

A区（列表左侧）Icon资源类型。

#### BadgeOptions

HdsListItemCard中Badge样式选项。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

名称

类型

只读

可选

说明

badgeValue

number

否

是

设置提醒信息数，大于99时，显示“99+”。

默认值：-1。

设置为小于0时，不显示信息标记。

badgeColor

[ResourceColor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resourcecolor)

否

是

Badge背板颜色。

显示信息标记时默认值：$r('sys.color.warning')。

不显示信息标记时默认值：$r('sys.color.comp_background_emphasize')。

textColor

[ResourceColor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resourcecolor)

否

是

Badge中数字颜色。

默认值：$r('sys.color.font_on_primary')。

badgeId

string

否

是

Badge的Id。

#### CheckOptions

HdsListItemCard中选择类元素样式选项。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

名称

类型

只读

可选

说明

isCheck

boolean

否

是

选择类元素的初始选中状态。

true：元素被选中。

false：元素未被选中。

默认值：false。

selectColor

[ResourceColor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resourcecolor)

否

是

选择类元素被选中后的背板颜色。

onChange

[OnChangeCallback](#section1370591018245)

否

是

选择类元素的onChange回调。

onClick

[OnClickCallback](#section975195614188)

否

是

选择类元素的点击事件回调。

enable

boolean

否

是

选择类元素是否被启用。

true：选择类元素被启用。

false：选择类元素被禁用。

默认值：true。

checkId

string

否

是

选择类元素的Id。

accessibilityOptions

[AccessibilityOptions](#section16412175163116)

否

是

选择类元素的无障碍播放能力选项。

#### ToggleButtonOptions

HdsListItemCard中ToggleButton样式选项。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

名称

类型

只读

可选

说明

isCheck

boolean

否

是

ToggleButton的初始选中状态。

true：元素被选中。

false：元素未被选中。

默认值：false。

iconValue

[SymbolType](#section19341944531)

否

是

ToggleButton内部图标的Symbol资源。

selectColor

[ResourceColor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resourcecolor)

否

是

ToggleButton被选中后的背板颜色。

默认值：#00000000。

onChange

[OnChangeCallback](#section1370591018245)

否

是

ToggleButton的onChange回调。

enable

boolean

否

是

ToggleButton是否被启用。

true：ToggleButton被启用。

false：ToggleButton被禁用。

默认值：true。

toggleButtonId

string

否

是

ToggleButton的Id。

accessibilityOptions

[AccessibilityOptions](#section16412175163116)

否

是

ToggleButton的无障碍播放能力选项。

#### TextOptions

HdsListItemCard中Text样式选项。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

名称

类型

只读

可选

说明

text

[ResourceStr](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resourcestr)

否

是

Text资源类型。

modifier

[TextModifier](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-attribute-modifier#自定义modifier)

否

是

Text属性样式修改器。

#### ColorOptions

HdsListItemCard中Color样式选项。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

名称

类型

只读

可选

说明

color

[ResourceColor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resourcecolor)

否

是

对应元素的颜色修改。

componentId

string

否

是

对应元素的Id。

#### ButtonOptions

HdsListItemCard中Button样式选项。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**设备行为异常：**该接口在TV中与ux规范不一致（获焦态和悬停态组件未放大，获焦态背板颜色未变化，Button内部的text默认颜色等），在其他设备类型中可正常使用。

**起始版本：**6.0.0(20)

名称

类型

只读

可选

说明

text

[ResourceStr](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resourcestr)

否

是

Button内部的text文本内容。

textColor

[ResourceColor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resourcecolor)

否

是

Button内部的text文本颜色。

TV上默认值为$r('sys.color.font_primary')，其他设备上默认值为$r('sys.color.font_emphasize')。

onClick

[OnClickCallback](#section975195614188)

否

是

Button的点击回调。

enable

boolean

否

是

Button是否被启用。

true：Button被启用。

false：Button被禁用。

默认值：true。

buttonId

string

否

是

Button的Id。

accessibilityOptions

[AccessibilityOptions](#section16412175163116)

否

是

Button的无障碍播放能力选项。

#### SuffixIconOptions

HdsListItemCard中C区（列表右侧）Icon样式选项。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

名称

类型

只读

可选

说明

iconValue

[PrefixIconType](#section9201529151513)

否

是

C区（列表右侧）Icon的图标资源。

onClick

[OnClickCallback](#section975195614188)

否

是

C区（列表右侧）Icon的点击回调。

enable

boolean

否

是

C区（列表右侧）Icon是否被启用。

true：C区（列表右侧）Icon被启用。

false：C区（列表右侧）Icon被禁用。

默认值：true。

accessibilityOptions

[AccessibilityOptions](#section16412175163116)

否

是

C区（列表右侧）Icon的无障碍播放能力选项。

#### SuffixArrowIconTextOptions

HdsListItemCard中C区（列表右侧）箭头图标文本选项 。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

名称

类型

只读

可选

说明

startArrow

[SuffixArrowIconOptions](#section1042613291512)

否

是

C区（列表右侧）起始箭头的选项。

text

[TextOptions](#section4754175319)

否

是

C区（列表右侧）文本选项。

endArrow

[SuffixArrowIconOptions](#section1042613291512)

否

是

C区（列表右侧）结束箭头的选项。

#### SuffixArrowIconOptions

HdsListItemCard中C区（列表右侧）箭头图标选项 。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

名称

类型

只读

可选

说明

arrowColor

[ResourceColor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resourcecolor)

否

是

C区（列表右侧）箭头的颜色。

onClick

[OnClickCallback](#section975195614188)

否

是

C区（列表右侧）箭头的点击回调。

arrowId

string

否

是

C区（列表右侧）箭头的ID。

enable

boolean

否

是

C区（列表右侧）箭头是否被启用。

true：C区（列表右侧）箭头被启用。

false：C区（列表右侧）箭头被禁用。

默认值：true。

accessibilityOptions

[AccessibilityOptions](#section16412175163116)

否

是

C区（列表右侧）箭头的无障碍播放能力选项。

#### SelectStyle

HdsListItemCard中下拉按钮样式选项。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

名称

类型

只读

可选

说明

value

[ResourceStr](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resourcestr)

否

否

下拉按钮本身的文本内容。

valueColor

[ResourceColor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resourcecolor)

否

是

下拉按钮本身的文本颜色。

默认值：$r('sys.color.font_secondary')。

arrowColor

[ResourceColor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resourcecolor)

否

是

下拉按钮箭头的颜色。

默认值：$r('sys.color.icon_secondary')。

optionValues

Array<[ResourceStr](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resourcestr)>

否

否

下拉选项内容。

optionSymbol

Array<[SymbolGlyphModifier](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-attribute-modifier#自定义modifier)>

否

否

下拉选项Symbol图片。

onSelect

[OnSelectCallback](#section213423822518)

否

是

下拉菜单选中某一项的回调。

showDefaultSelectedIcon

boolean

否

是

是否显示默认选定的图标。

true：显示默认选定的图标。

false：不显示默认选定的图标。

默认值：false。

enable

boolean

否

是

下拉按钮是否被启用。

true：下拉按钮被启用。

false：下拉按钮被禁用。

默认值：true。

selectId

string

否

是

下拉按钮的Id。

accessibilityOptions

[AccessibilityOptions](#section16412175163116)

否

是

下拉按钮的无障碍播放能力选项。

#### SymbolType

type SymbolType= ResourceStr | SymbolGlyphModifier

HdsListItemCard中支持Symbol图标资源类型。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

**返回值：**

类型

说明

[ResourceStr](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resourcestr)

字符串类型。

[SymbolGlyphModifier](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-attribute-modifier#自定义modifier)

SymbolGlyph属性样式修改器。

#### PrefixIconType

type PrefixIconType= ImageOptions | SymbolGlyphOptions

HdsListItemCard中支持A区（列表左侧）Icon图标资源类型。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

**返回值：**

类型

说明

[ImageOptions](#section3582112115362)

Image类型。

[SymbolGlyphOptions](#section171912040174014)

SymbolGlyph类型。

#### ImageType

type ImageType = ResourceStr | image.PixelMap

HdsListItemCard中支持Image资源类型。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

**返回值：**

类型

说明

[ResourceStr](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resourcestr)

字符串类型。

image.[PixelMap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-pixelmap)

PixelMap类型。

#### IconSize

PrefixIcon图标大小枚举。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

名称

值

说明

SMALL_ICON

1

A区（列表左侧）Icon图标类型：小图标类型，大小为16vp * 16vp（穿戴设备上为28vp*28vp）。

SYSTEM_ICON

2

A区（列表左侧）Icon图标类型：系统图标类型，大小为24vp * 24vp（穿戴设备上为32vp*32vp）。

上述描述中所有左侧、中间、右侧均是在LTR模式下。

#### OnClickCallback

type OnClickCallback = () => void

HdsListItemCard中的点击事件回调。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

#### OnChangeCallback

type OnChangeCallback = (isOn: boolean) => void

HdsListItemCard中的onChange事件回调。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

**参数：**

参数名

类型

必填

说明

isOn

boolean

是

HdsListItemCard中的Switch/CheckBox/Radio/ToggleButton选中状态。

- isOn为true时，表示从未选中变为选中。
- isOn为false时，表示从选中变为未选中。

#### OnSelectCallback

type OnSelectCallback = (index: number, text: string) => void

HdsListItemCard中的onSelect事件回调。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

**参数：**

参数名

类型

必填

说明

index

number

是

选中项的索引，取值范围大于等于0。

text

string

是

选中项的值，无位数要求。

#### 示例

以设置简单的列表项为例

```ets
import {
  HdsListItemCard,
  IconSize,
  PrefixImage,
  PrefixIcon,
  SuffixIcon,
  SuffixSwitch,
  SuffixBadgeAndArrow
} from '@kit.UIDesignKit';
import { promptAction, ImageModifier, TextModifier } from '@kit.ArkUI';

@Entry
@Component
struct HdsListItemCardExample {
  private scroller: ListScroller = new ListScroller();

  build() {
    Column() {
      List({ space: 5, scroller: this.scroller }) {
        ListItem() {
          HdsListItemCard({
            prefixItem: new PrefixIcon({
              iconSize: IconSize.SYSTEM_ICON,
              iconValue: {
                image: $r('app.media.startIcon')
              },
            }),
            textItem: {
              primaryText: {
                text: 'Primary Text'
              },
              secondaryText: {
                text: 'Secondary Text'
              },
              description: {
                text: 'Description Text'
              },
            },
            suffixItem: new SuffixIcon({
              iconValue: {
                symbol: $r('sys.symbol.circle_dashed')
              },
              onClick: () => {
                promptAction.openToast({ message: 'onclick icon' });
              }
            }),
            onClick: () => {
              promptAction.openToast({ message: 'onclick hdslistitem' });
            },
          })
        }

        ListItem() {
          HdsListItemCard({
            prefixItem: new PrefixImage({
              image: $r('app.media.startIcon'),
              modifier: new ImageModifier().width(70).height(70).borderRadius(20)
            }),
            textItem: {
              primaryText: {
                text: 'Primary Text'
              },
              secondaryText: {
                text: 'Secondary Text'
              },
              description: {
                text: 'Description Text'
              },
            },
            suffixItem: new SuffixSwitch({
              isCheck: false,
              selectColor: Color.Orange,
              onChange: (num: boolean) => {
                if (num) {
                  promptAction.openToast({ message: 'switch is true' });
                } else {
                  promptAction.openToast({ message: 'switch is false' });
                }
              },
            })
          })
        }

        ListItem() {
          HdsListItemCard({
            prefixItem: new PrefixIcon({
              iconSize: IconSize.SYSTEM_ICON,
              iconValue: {
                symbol: $r('sys.symbol.ohos_trash')
              },
            }),
            textItem: {
              primaryText: {
                text: 'Primary Text',
                modifier: new TextModifier().fontColor(Color.Pink),
              }
            },
            suffixItem: new SuffixBadgeAndArrow({
              badgeValue: 9,
              badgeColor: Color.Orange,
              textColor: Color.Blue,
            }, {
              color: Color.Orange
            })
          })
        }
      }
      .width('100%')
      .height('100%')
      .margin(10)
    }.backgroundColor(0x1a0a59f7).height('100%')
  }
}
```