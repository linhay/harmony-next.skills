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

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**设备行为异常：**该接口在TV中与ux规范不一致（获焦态和悬停态组件未放大，获焦态背板颜色未变化，Button内部的text默认颜色等），在其他设备类型中可正常使用。

**起始版本：**6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | HdsListItemCardOptions | 是 | HdsListItemCard列表项内容。 |

**属性**

当前仅支持[通用属性](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-component-general-attributes)。


1. 该通用属性针对的是HdsListItemCard组件，无法通过其设置组件内部的左侧元素，中间元素，右侧元素的属性。

1. 对于[HdsListItemCardOptions](#ZH-CN_TOPIC_0000002553361239__hdslistitemcardoptions)中已经有的列表项属性，比如的cardWidth，cardHeight，cardBackgroundColor，onClick，enable，cardId等，建议直接使用[HdsListItemCardOptions](#ZH-CN_TOPIC_0000002553361239__hdslistitemcardoptions)进行属性设置，不要使用通用属性。否则，会出现混淆或者不生效。

#### PrefixItem

定义PrefixItem类，HdsListItemCard列表项的A区（列表左侧）元素。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

#### PrefixImage

PrefixImage继承自父类[PrefixItem](#ZH-CN_TOPIC_0000002553361239__prefixitem)，A区（列表左侧）Image元素，穿戴设备中Image大小不可修改，为固定值46vp*46vp。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

#### 属性

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| options | ImageClickOptions | 否 | 是 | A区（列表左侧）Image元素的配置项。 |

#### constructor

constructor(options?: ImageClickOptions)

PrefixImage的构造函数。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | ImageClickOptions | 否 | A区（列表左侧）Image元素的配置项。 |

#### PrefixIcon

PrefixIcon继承自父类[PrefixItem](#ZH-CN_TOPIC_0000002553361239__prefixitem)，A区（列表左侧）Icon元素。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

#### 属性

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| options | PrefixIconOptions | 否 | 是 | A区（列表左侧）Icon元素的配置项。 |

#### constructor

constructor(options?: PrefixIconOptions)

PrefixIcon的构造函数。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | PrefixIconOptions | 否 | A区（列表左侧）Icon元素的配置项。 |

#### PrefixBadge

PrefixBadge继承自父类[PrefixItem](#ZH-CN_TOPIC_0000002553361239__prefixitem)，A区（列表左侧）Badge元素。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

#### 属性

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| options | BadgeOptions | 否 | 是 | A区（列表左侧）Badge元素的配置项。 |

#### constructor

constructor(options?: BadgeOptions)

PrefixBadge的构造函数。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | BadgeOptions | 否 | A区（列表左侧）Badge元素的配置项。 |

#### PrefixSwitch

PrefixSwitch继承自父类[PrefixItem](#ZH-CN_TOPIC_0000002553361239__prefixitem)，A区（列表左侧）Switch元素。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

#### 属性

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| options | CheckOptions | 否 | 是 | A区（列表左侧）Switch元素的配置项。 |

#### constructor

constructor(options?: CheckOptions)

PrefixSwitch的构造函数。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | CheckOptions | 否 | A区（列表左侧）Switch元素的配置项。 |

#### PrefixToggleButton

PrefixToggleButton继承自父类[PrefixItem](#ZH-CN_TOPIC_0000002553361239__prefixitem)，A区（列表左侧）ToggleButton元素。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

#### 属性

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| options | ToggleButtonOptions | 否 | 是 | A区（列表左侧）ToggleButton元素的配置项。 |

#### constructor

constructor(options?: ToggleButtonOptions)

PrefixToggleButton的构造函数。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | ToggleButtonOptions | 否 | A区（列表左侧）ToggleButton元素的配置项。 |

#### PrefixButton

PrefixButton继承自父类[PrefixItem](#ZH-CN_TOPIC_0000002553361239__prefixitem)，A区（列表左侧）Button元素。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

#### 属性

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| options | ButtonOptions | 否 | 是 | A区（列表左侧）Button元素的配置项。 |

#### constructor

constructor(options?: ButtonOptions)

PrefixButton的构造函数。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | ButtonOptions | 否 | A区（列表左侧）Button元素的配置项。 |

#### PrefixCustomBuilder

PrefixCustomBuilder继承自父类[PrefixItem](#ZH-CN_TOPIC_0000002553361239__prefixitem)，A区（列表左侧）自定义内容。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

#### 属性

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| customBuilder | CustomBuilder | 否 | 是 | A区（列表左侧）自定义内容。 |

#### constructor

constructor(customBuilder?: CustomBuilder)

PrefixCustomBuilder的构造函数。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| customBuilder | CustomBuilder | 否 | A区（列表左侧）自定义内容。 |

#### SuffixItem

定义SuffixItem类，HdsListItemCard列表项的C区（列表右侧）元素。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

#### SuffixText

SuffixText继承自父类[SuffixItem](#ZH-CN_TOPIC_0000002553361239__suffixitem)，C区（列表右侧）Text元素。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

#### 属性

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| options | TextOptions | 否 | 是 | C区（列表右侧）Text元素的配置项。 |

#### constructor

constructor(options?: TextOptions)

SuffixText的构造函数。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | TextOptions | 否 | C区（列表右侧）Text元素的配置项。 |

#### SuffixImage

SuffixImage继承自父类[SuffixItem](#ZH-CN_TOPIC_0000002553361239__suffixitem)，C区（列表右侧）Image元素。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

#### 属性

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| options | ImageClickOptions | 否 | 是 | C区（列表右侧）Image元素的配置项。 |

#### constructor

constructor(options?: ImageClickOptions)

SuffixImage的构造函数。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | ImageClickOptions | 否 | C区（列表右侧）Image元素的配置项。 |

#### SuffixLoadingProgress

SuffixLoadingProgress继承自父类[SuffixItem](#ZH-CN_TOPIC_0000002553361239__suffixitem)，C区（列表右侧）LoadingProgress元素。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

#### 属性

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| options | ColorOptions | 否 | 是 | C区（列表右侧）LoadingProgress元素的配置项。 |

#### constructor

constructor(options?: ColorOptions)

SuffixLoadingProgress的构造函数。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | ColorOptions | 否 | C区（列表右侧）LoadingProgress元素的配置项。 |

#### SuffixRadio

SuffixRadio继承自父类[SuffixItem](#ZH-CN_TOPIC_0000002553361239__suffixitem)，C区（列表右侧）Radio元素。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

#### 属性

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| options | CheckOptions | 否 | 是 | C区（列表右侧）Radio元素的配置项。 |

#### constructor

constructor(options?: CheckOptions)

SuffixRadio的构造函数。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | CheckOptions | 否 | C区（列表右侧）Radio元素的配置项。 |

#### SuffixCheckbox

SuffixCheckbox继承自父类[SuffixItem](#ZH-CN_TOPIC_0000002553361239__suffixitem)，C区（列表右侧）Checkbox元素。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

#### 属性

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| options | CheckOptions | 否 | 是 | C区（列表右侧）Checkbox元素的配置项。 |

#### constructor

constructor(options?: CheckOptions)

SuffixCheckbox的构造函数。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | CheckOptions | 否 | C区（列表右侧）Checkbox元素的配置项。 |

#### SuffixSwitch

SuffixSwitch继承自父类[SuffixItem](#ZH-CN_TOPIC_0000002553361239__suffixitem)，C区（列表右侧）Switch元素。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

#### 属性

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| options | CheckOptions | 否 | 是 | C区（列表右侧）Switch元素的配置项。 |

#### constructor

constructor(options?: CheckOptions)

SuffixSwitch的构造函数。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | CheckOptions | 否 | C区（列表右侧）Switch元素的配置项。 |

#### SuffixArrow

SuffixArrow继承自父类[SuffixItem](#ZH-CN_TOPIC_0000002553361239__suffixitem)，C区（列表右侧）Arrow元素。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

#### 属性

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| options | ColorOptions | 否 | 是 | C区（列表右侧）Arrow元素的配置项。 |

#### constructor

constructor(options?: ColorOptions)

SuffixArrow的构造函数。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | ColorOptions | 否 | C区（列表右侧）Arrow元素的配置项。 |

#### SuffixBadge

SuffixBadge继承自父类[SuffixItem](#ZH-CN_TOPIC_0000002553361239__suffixitem)，C区（列表右侧）Badge元素。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

#### 属性

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| options | BadgeOptions | 否 | 是 | C区（列表右侧）Badge元素的配置项。 |

#### constructor

constructor(options?: BadgeOptions)

SuffixBadge的构造函数。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | BadgeOptions | 否 | C区（列表右侧）Badge元素的配置项。 |

#### SuffixButton

SuffixButton继承自父类[SuffixItem](#ZH-CN_TOPIC_0000002553361239__suffixitem)，C区（列表右侧）Button元素。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

#### 属性

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| options | ButtonOptions | 否 | 是 | C区（列表右侧）Button元素的配置项。 |

#### constructor

constructor(options?: ButtonOptions)

SuffixButton的构造函数。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | ButtonOptions | 否 | C区（列表右侧）Button元素的配置项。 |

#### SuffixIcon

SuffixIcon继承自父类[SuffixItem](#ZH-CN_TOPIC_0000002553361239__suffixitem)，C区（列表右侧）单个Icon元素。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

#### 属性

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| options | SuffixIconOptions | 否 | 是 | C区（列表右侧）单个Icon元素的配置项。 |

#### constructor

constructor(options?: SuffixIconOptions)

SuffixIcon的构造函数。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | SuffixIconOptions | 否 | C区（列表右侧）单个Icon元素的配置项。 |

#### SuffixSubIcon

SuffixSubIcon继承自父类[SuffixItem](#ZH-CN_TOPIC_0000002553361239__suffixitem)，C区（列表右侧）两个Icon元素。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

#### 属性

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| options | SuffixIconOptions | 否 | 是 | C区（列表右侧）第一个Icon元素的配置项。 |
| subOptions | SuffixIconOptions | 否 | 是 | C区（列表右侧）第二个Icon元素的配置项。 |

#### constructor

constructor(options?: SuffixIconOptions, subOptions?: SuffixIconOptions)

SuffixSubIcon的构造函数。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | SuffixIconOptions | 否 | C区（列表右侧）第一个Icon元素的配置项。 |
| subOptions | SuffixIconOptions | 否 | C区（列表右侧）第二个Icon元素的配置项。 |

#### SuffixSelect

SuffixSelect继承自父类[SuffixItem](#ZH-CN_TOPIC_0000002553361239__suffixitem)，C区（列表右侧）Select元素。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

#### 属性

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| options | SelectStyle | 否 | 是 | C区（列表右侧）Select元素的配置项。 |

#### constructor

constructor(options?: SelectStyle)

SuffixSelect的构造函数。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | SelectStyle | 否 | C区（列表右侧）Select的配置项。 |

#### SuffixToggleButton

SuffixToggleButton继承自父类[SuffixItem](#ZH-CN_TOPIC_0000002553361239__suffixitem)，C区（列表右侧）ToggleButton元素。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

#### 属性

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| options | ToggleButtonOptions | 否 | 是 | C区（列表右侧）ToggleButton的配置项。 |

#### constructor

constructor(options?: ToggleButtonOptions)

SuffixToggleButton的构造函数。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | ToggleButtonOptions | 否 | C区（列表右侧）ToggleButton的配置项。 |

#### SuffixBadgeAndArrow

SuffixBadgeAndArrow继承自父类[SuffixItem](#ZH-CN_TOPIC_0000002553361239__suffixitem)，C区（列表右侧）Badge和Arrow组合元素。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

#### 属性

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| badgeOptions | BadgeOptions | 否 | 是 | C区（列表右侧）Badge和Arrow组合元素中Badge的配置项。 |
| arrowOptions | ColorOptions | 否 | 是 | C区（列表右侧）Badge和Arrow组合元素中Arrow的配置项。 |

#### constructor

constructor(badgeOptions?: BadgeOptions, arrowOptions?: ColorOptions)

SuffixBadgeAndArrow的构造函数。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| badgeOptions | BadgeOptions | 否 | C区（列表右侧）Badge和Arrow组合元素中Badge的配置项。 |
| arrowOptions | ColorOptions | 否 | C区（列表右侧）Badge和Arrow组合元素中Arrow的配置项。 |

#### SuffixTextAndArrow

SuffixTextAndArrow继承自父类[SuffixItem](#ZH-CN_TOPIC_0000002553361239__suffixitem)，C区（列表右侧）Text和Arrow组合元素。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

#### 属性

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| textOptions | TextOptions | 否 | 是 | C区（列表右侧）Text和Arrow组合元素中Text的配置项。 |
| arrowOptions | ColorOptions | 否 | 是 | C区（列表右侧）Text和Arrow组合元素中Arrow的配置项 |

#### constructor

constructor(textOptions?: TextOptions, arrowOptions?: ColorOptions)

SuffixTextAndArrow的构造函数。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| textOptions | TextOptions | 否 | C区（列表右侧）Text和Arrow组合元素中Text的配置项。 |
| arrowOptions | ColorOptions | 否 | C区（列表右侧）Text和Arrow组合元素中Arrow的配置项。 |

#### SuffixArrowIconText

SuffixArrowIconText继承自父类[SuffixItem](#ZH-CN_TOPIC_0000002553361239__suffixitem)，C区（列表右侧）Arrow、Text和Arrow组合元素。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

#### 属性

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| options | SuffixArrowIconTextOptions | 否 | 是 | C区（列表右侧）Text、Arrow和Icon组合元素的配置项。 |

#### constructor

constructor(options?: SuffixArrowIconTextOptions)

SuffixArrowIconText的构造函数。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | SuffixArrowIconTextOptions | 否 | C区（列表右侧）Text、Arrow和Icon组合元素的配置项。 |

#### SuffixCustomBuilder

SuffixCustomBuilder继承自父类[SuffixItem](#ZH-CN_TOPIC_0000002553361239__suffixitem)，C区（列表右侧）自定义内容。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

#### 属性

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| customBuilder | CustomBuilder | 否 | 是 | C区（列表右侧）自定义内容。 |

#### constructor

constructor(customBuilder?: CustomBuilder)

SuffixCustomBuilder的构造函数。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| customBuilder | CustomBuilder | 否 | C区（列表右侧）自定义内容。 |

#### HdsListItemCardOptions

HdsListItemCard列表项内元素配置选项。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**设备行为异常：**该接口在TV中与ux规范不一致（获焦态和悬停态组件未放大，获焦态背板颜色未变化，Button内部的text默认颜色等），在其他设备类型中可正常使用。

**起始版本：**6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| prefixItem | PrefixItem | 否 | 是 | HdsListItemCard列表项的A区（左侧）元素。 |
| textItem | TextItemOptions | 否 | 是 | HdsListItemCard列表项的B区（中间）元素。 |
| suffixItem | SuffixItem | 否 | 是 | HdsListItemCard列表项的C区（右侧）元素。 |
| onClick | OnClickCallback | 否 | 是 | HdsListItemCard列表项的点击回调。 |
| cardHeight | Dimension | 否 | 是 | HdsListItemCard列表项的高度，目前不支持使用Percentage设置。 |
| cardWidth | Dimension | 否 | 是 | HdsListItemCard列表项的宽度，目前不支持使用Percentage设置。 |
| cardBackgroundColor | ResourceColor | 否 | 是 | HdsListItemCard列表项的背景颜色。 |
| cardBorderRadius | Dimension | 否 | 是 | HdsListItemCard列表项的边框圆角。 |
| cardPrefixMargin | Dimension | 否 | 是 | HdsListItemCard列表项距离屏幕左侧的边距。 |
| cardSuffixMargin | Dimension | 否 | 是 | HdsListItemCard列表项距离屏幕右侧的边距。 |
| hoverBorderRadius | Dimension | 否 | 是 | HdsListItemCard列表项在悬浮状态下的边框圆角。 |
| enable | boolean | 否 | 是 | HdsListItemCard列表项是否被启用。 true：列表项被启用。 false：列表项被禁用。 默认值：true。 |
| cardId | string | 否 | 是 | HdsListItemCard列表项的Id。 |
| accessibilityOptions | AccessibilityOptions | 否 | 是 | HdsListItemCard列表项的无障碍播放能力选项。 |


从6.1.0(23)开始，若同时满足如下两个条件，焦点将默认组合聚焦播报：

1. HdsListItemCard上未定义accessibilityOptions和onClick事件。

1. 列表项A区（左侧）和C区（右侧）仅有一个可点击事件。

该功能是通过修改accessibilityOptions中isGroup， stateControllerId，actionControllerId的值来实现的，其中isGroup的值会被修改为true，stateControllerId和actionControllerId的值会被修改为可点击子组件的id。

#### TextItemOptions

HdsListItemCard列表项的B区（列表中间）元素配置选项。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| primaryText | TextOptions | 否 | 是 | B区（列表中间）元素的标题内容。 |
| primaryPrefixSymbol | TextSymbolGlyphOptions | 否 | 是 | 标题内容左侧第一个Symbol图标。 |
| primarySuffixSymbol | TextSymbolGlyphOptions | 否 | 是 | 标题内容右侧第一个Symbol图标。 |
| primaryPrefixSubSymbol | TextSymbolGlyphOptions | 否 | 是 | 标题内容左侧Symbol第二个图标，仅在左侧第一个Symbol图标存在时才显示。 |
| primarySuffixSubSymbol | TextSymbolGlyphOptions | 否 | 是 | 标题内容右侧Symbol第二个图标，仅在右侧第一个Symbol图标存在时才显示。 |
| secondaryText | TextOptions | 否 | 是 | B区（列表中间）元素的副标题内容。 |
| secondaryPrefixSymbol | TextSymbolGlyphOptions | 否 | 是 | 副标题内容左侧第一个Symbol图标。 |
| secondarySuffixSymbol | TextSymbolGlyphOptions | 否 | 是 | 副标题内容右侧第一个Symbol图标。 |
| secondaryPrefixSubSymbol | TextSymbolGlyphOptions | 否 | 是 | 副标题内容左侧Symbol第二个图标，仅在左侧第一个Symbol图标存在时才显示。 |
| secondarySuffixSubSymbol | TextSymbolGlyphOptions | 否 | 是 | 副标题内容右侧Symbol第二个图标，仅在右侧第一个Symbol图标存在时才显示。 |
| description | TextOptions | 否 | 是 | B区（列表中间）元素的描述内容。 |
| descriptionPrefixSymbol | TextSymbolGlyphOptions | 否 | 是 | 描述内容左侧第一个Symbol图标。 |
| descriptionSuffixSymbol | TextSymbolGlyphOptions | 否 | 是 | 描述内容右侧第一个Symbol图标。 |
| descriptionPrefixSubSymbol | TextSymbolGlyphOptions | 否 | 是 | 描述内容左侧Symbol第二个图标，仅在左侧第一个Symbol图标存在时才显示。 |
| descriptionSuffixSubSymbol | TextSymbolGlyphOptions | 否 | 是 | 描述内容右侧Symbol第二个图标，仅在右侧第一个Symbol图标存在时才显示。 |
| accessibilityOptions | AccessibilityOptions | 否 | 是 | B区（列表中间）元素的无障碍播放能力选项。 起始版本： 6.1.0(23) |
| customBuilder | CustomBuilder | 否 | 是 | B区（列表中间）自定义内容。 |


TextItemOptions中customBuilder优先级高于其它接口。

#### AccessibilityOptions

HdsListItemCard无障碍播放能力选项。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| accessibilityText | ResourceStr | 否 | 是 | 列表的无障碍文本属性。当组件不包含文本属性时，屏幕朗读选中此组件时不播报，使用者无法清楚地知道当前选中了什么组件。为了解决此场景，开发人员可为不包含文字信息的组件设置无障碍文本，当屏幕朗读选中此组件时播报无障碍文本的内容，帮助屏幕朗读的使用者清楚地知道自己选中了什么组件。 默认值：""。 |
| accessibilityDescription | ResourceStr | 否 | 是 | 列表的无障碍描述。此描述用于向用户详细解释当前组件，开发人员应为组件的这一属性提供较为详尽的文本说明，以协助用户理解即将执行的操作及其可能产生的后果。特别是当这些后果无法仅从组件的属性和无障碍文本中直接获知时。如果组件同时具备文本属性和无障碍说明属性，当组件被选中时，系统将首先播报组件的文本属性，随后播报无障碍说明属性的内容。 默认值：类型为switch时，默认值为"单指双击即可开启/关闭"，类型为checkbox时，默认值为"单指双击即可选中/取消选中"，其它类型默认值为"单指双击即可执行"。 |
| accessibilityLevel | ResourceStr | 否 | 是 | 无障碍重要性，用于控制当前项是否可被无障碍辅助服务所识别。 支持的值为： "auto"：当前组件会转换"yes"。 "yes"：当前组件可被无障碍辅助服务所识别。 "no"：当前组件不可被无障碍辅助服务所识别。 "no-hide-descendants"：当前组件及其所有子组件不可被无障碍辅助服务所识别。 默认值："auto"。 |
| accessibilityGroup | AccessibilityGroupOptions | 否 | 是 | 是否作为群组响应无障碍操作。启用无障碍分组后，组件及其子组件作为一整个可选组件，无障碍服务不再关注子组件内容。 起始版本： 6.1.0(23) |
| accessibilityChecked | boolean | 否 | 是 | 设置无障碍节点是否选中。用于支持多选的情况使用，表示组件是否被选中。此接口只影响屏幕朗读场景下的组件状态播报信息。 true：当前组件被选中。 false：当前组件未被选中。 undefined：由组件自行确定选中状态。 默认值：undefined 起始版本： 6.1.0(23) |
| accessibilitySelected | boolean | 否 | 是 | 设置无障碍节点是否选中。用于支持单选的情况使用，表示组件是否被选中。此接口只影响屏幕朗读场景下的组件状态播报信息。 true：当前组件被选中。 false：当前组件未被选中。 undefined：由组件自行确定选中状态。 默认值：undefined 起始版本： 6.1.0(23) |
| accessibilityRole | AccessibilityRoleType | 否 | 是 | 设置无障碍节点的组件类型。特定组件类型有特定的朗读方式，可以根据应用诉求，修改组件类型，用于控制无障碍模式下对组件的朗读方式和朗读内容。不设置的时候，默认使用节点自身的组件类型。 起始版本： 6.1.0(23) |
| onAccessibilityActionIntercept | AccessibilityActionInterceptCallback | 否 | 是 | 注册onAccessibilityActionIntercept回调。该回调会在无障碍控制操作触发前调用，由注册方决定是否拦截该次无障碍动作，对不支持Click的组件注册也无法触发回调。 起始版本： 6.1.0(23) |


accessibilityChecked属性代表组件是多选模式，accessibilitySelected属性代表组件是单选模式。组件不能同时存在两种选择模式，会造成无障碍状态冲突，导致屏幕朗读等无障碍辅助应用无法正确识别选中状态。如使用accessibilityChecked设置组件为多选模式（设置为true、false），需要保证未设置accessibilitySelected属性，或已将accessibilitySelected属性值重置为undefined，反之亦然。

**AccessibilityGroupOptions**

HdsListItemCard无障碍分组能力选项。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.UIDesign.HDSComponent.Full

起始版本： 6.1.0(23)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| isGroup | boolean | 否 | 是 | 设置是否启用无障碍分组。 true：表示该组件及其所有子组件为一整个可以选中的组件，无障碍服务将不再关注其子组件内容，会合并子组件的文本与无障碍信息，并将其发送至无障碍服务。 false：表示不启用无障碍分组。 默认值：false。 |
| groupControllerOptions | AccessibilityGroupControllerOptions | 否 | 是 | 无障碍分组相关的其他属性，用于进一步控制播报内容。比如accessibilityPreferred可用于控制是否优先拼接无障碍文本进行朗读，stateController和actionController可用于指定特定的子组件进行聚合播报。 |

**AccessibilityGroupControllerOptions**

HdsListItemCard无障碍播放能力选项。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.UIDesign.HDSComponent.Full

起始本： 6.1.0(23)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| isAccessibilityPreferred | boolean | 否 | 是 | 若accessibilityPreferred设置为true，则深度遍历每个子节点时优先选择该子节点的无障碍文本accessibilityText。 若无障碍文本为空则选择本身Text文本，最终将拼接完成的文本设置给accessibilityText与Text都为空的父节点。 若accessibilityPreferred设置为false，表示不启用此功能。 默认值：false |
| stateControllerRoleType | AccessibilityRoleType | 否 | 是 | 指定特定类型的子组件。配置AccessibilityGroupOptions的容器组件进行无障碍聚合后，会将该特定类型的子组件的选中状态和状态播报文本作为聚合组件的状态和播报文本。从而聚合屏幕朗读下的状态播报，避免需要对子组件单独进行聚焦。 说明： 如果聚合组件内有多个相同类型的子组件，则以组件树上该聚合组件下的第一个查找到的子组件为控制组件。 不支持跨进程嵌入式组件内的特定类型，例如：卡片、EmbededUiextension。 默认值：无指定组件 |
| stateControllerId | string | 否 | 是 | 指定特定唯一标识ID的子组件。配置AccessibilityGroupOptions的容器组件进行无障碍聚合后，会将该特定标识的子组件的选中状态和状态播报文本作为聚合组件的状态和播报文本。从而聚合屏幕朗读下的状态播报，避免需要对子组件单独进行聚焦。 说明： 如果聚合组件内有多个相同类型的子组件，则以组件树上该聚合组件下的第一个查找到的子组件为控制组件。 如果与stateControllerRoleType同时配置，则优先匹配ID一致的组件。 不支持跨进程嵌入式组件内的特定类型，例如：卡片、EmbededUiextension。 默认值：无指定组件 |
| actionControllerRoleType | AccessibilityRoleType | 否 | 是 | 指定特定类型的子组件。配置AccessibilityGroupOptions的容器组件进行无障碍聚合后，如果触发无障碍的控制操作时，会将操作转发给该特定类型的子组件。从而聚合屏幕朗读下的点击事件，避免需要对子组件单独进行聚焦。 说明： 如果聚合组件内有多个相同类型的子组件，则以组件树上该聚合组件下的第一个查找到的子组件为控制组件。 当前只支持无障碍点击操作。 不支持跨进程嵌入式组件内的特定类型，例如：卡片、EmbededUiextension。 默认值：无指定组件 |
| actionControllerId | string | 否 | 是 | 指定特定唯一标识ID的子组件。配置AccessibilityGroupOptions的容器组件进行无障碍聚合后，如果触发无障碍的控制操作时，会将操作转发给该特定标识的子组件。从而聚合屏幕朗读下的点击事件，避免需要对子组件单独进行聚焦。 说明： 如果聚合组件内有多个相同类型的子组件，则以组件树上该聚合组件下的第一个查找到的子组件为控制组件。 当前只支持无障碍点击操作。 如果与actionControllerRoleType同时配置，则优先匹配ID一致的组件。 不支持跨进程嵌入式组件内的特定类型，例如：卡片、EmbededUiextension。 默认值：无指定组件 |

#### ImageOptions

HdsListItemCard中Image样式选项。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| image | ImageType | 否 | 是 | Image资源类型。 |
| modifier | ImageModifier | 否 | 是 | Image属性样式修改器。 |

#### ImageClickOptions

HdsListItemCard中支持点击的Image样式选项。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| image | ImageType | 否 | 是 | Image资源类型。 |
| modifier | ImageModifier | 否 | 是 | Image属性样式修改器。 |
| onClick | OnClickCallback | 否 | 是 | Image的点击回调。 |
| enable | boolean | 否 | 是 | Image是否被启用。 true：Image被启用。 false：Image被禁用。 默认值：true。 |
| accessibilityOptions | AccessibilityOptions | 否 | 是 | Image的无障碍播放能力选项。 |

#### SymbolGlyphOptions

HdsListItemCard中Symbol样式选项。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| symbol | SymbolType | 否 | 是 | Symbol资源类型。 |

#### TextSymbolGlyphOptions

HdsListItemCard中B区（列表中间）Text左右两侧的Symbol样式选项。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| symbol | SymbolType | 否 | 是 | B区（列表中间）Text左右两侧Symbol资源类型。 |
| onClick | OnClickCallback | 否 | 是 | B区（列表中间）Text左右两侧Symbol的点击回调。 |
| enable | boolean | 否 | 是 | B区（列表中间）Text左右两侧Symbol是否被启用。 true：B区（列表中间）Text左右两侧Symbol被启用。 false：B区（列表中间）Text左右两侧Symbol被禁用。 默认值：true。 |
| accessibilityOptions | AccessibilityOptions | 否 | 是 | B区（列表中间）Text左右两侧Symbol的无障碍播放能力选项。 |

#### PrefixIconOptions

HdsListItemCard中A区（列表左侧）Icon样式选项。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| iconSize | IconSize | 否 | 是 | A区（列表左侧）Icon样式。 默认值：IconSize.SYSTEM_ICON。 |
| iconValue | PrefixIconType | 否 | 是 | A区（列表左侧）Icon资源类型。 |

#### BadgeOptions

HdsListItemCard中Badge样式选项。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| badgeValue | number | 否 | 是 | 设置提醒信息数，大于99时，显示“99+”。 默认值：-1。 设置为小于0时，不显示信息标记。 |
| badgeColor | ResourceColor | 否 | 是 | Badge背板颜色。 显示信息标记时默认值：$r('sys.color.warning')。 不显示信息标记时默认值：$r('sys.color.comp_background_emphasize')。 |
| textColor | ResourceColor | 否 | 是 | Badge中数字颜色。 默认值：$r('sys.color.font_on_primary')。 |
| badgeId | string | 否 | 是 | Badge的Id。 |

#### CheckOptions

HdsListItemCard中选择类元素样式选项。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| isCheck | boolean | 否 | 是 | 选择类元素的初始选中状态。 true：元素被选中。 false：元素未被选中。 默认值：false。 |
| selectColor | ResourceColor | 否 | 是 | 选择类元素被选中后的背板颜色。 |
| onChange | OnChangeCallback | 否 | 是 | 选择类元素的onChange回调。 |
| onClick | OnClickCallback | 否 | 是 | 选择类元素的点击事件回调。 |
| enable | boolean | 否 | 是 | 选择类元素是否被启用。 true：选择类元素被启用。 false：选择类元素被禁用。 默认值：true。 |
| checkId | string | 否 | 是 | 选择类元素的Id。 |
| accessibilityOptions | AccessibilityOptions | 否 | 是 | 选择类元素的无障碍播放能力选项。 |

#### ToggleButtonOptions

HdsListItemCard中ToggleButton样式选项。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| isCheck | boolean | 否 | 是 | ToggleButton的初始选中状态。 true：元素被选中。 false：元素未被选中。 默认值：false。 |
| iconValue | SymbolType | 否 | 是 | ToggleButton内部图标的Symbol资源。 |
| selectColor | ResourceColor | 否 | 是 | ToggleButton被选中后的背板颜色。 默认值：#00000000。 |
| onChange | OnChangeCallback | 否 | 是 | ToggleButton的onChange回调。 |
| enable | boolean | 否 | 是 | ToggleButton是否被启用。 true：ToggleButton被启用。 false：ToggleButton被禁用。 默认值：true。 |
| toggleButtonId | string | 否 | 是 | ToggleButton的Id。 |
| accessibilityOptions | AccessibilityOptions | 否 | 是 | ToggleButton的无障碍播放能力选项。 |

#### TextOptions

HdsListItemCard中Text样式选项。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| text | ResourceStr | 否 | 是 | Text资源类型。 |
| modifier | TextModifier | 否 | 是 | Text属性样式修改器。 |

#### ColorOptions

HdsListItemCard中Color样式选项。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| color | ResourceColor | 否 | 是 | 对应元素的颜色修改。 |
| componentId | string | 否 | 是 | 对应元素的Id。 |

#### ButtonOptions

HdsListItemCard中Button样式选项。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**设备行为异常：**该接口在TV中与ux规范不一致（获焦态和悬停态组件未放大，获焦态背板颜色未变化，Button内部的text默认颜色等），在其他设备类型中可正常使用。

**起始版本：**6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| text | ResourceStr | 否 | 是 | Button内部的text文本内容。 |
| textColor | ResourceColor | 否 | 是 | Button内部的text文本颜色。 TV上默认值为$r('sys.color.font_primary')，其他设备上默认值为$r('sys.color.font_emphasize')。 |
| onClick | OnClickCallback | 否 | 是 | Button的点击回调。 |
| enable | boolean | 否 | 是 | Button是否被启用。 true：Button被启用。 false：Button被禁用。 默认值：true。 |
| buttonId | string | 否 | 是 | Button的Id。 |
| accessibilityOptions | AccessibilityOptions | 否 | 是 | Button的无障碍播放能力选项。 |

#### SuffixIconOptions

HdsListItemCard中C区（列表右侧）Icon样式选项。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| iconValue | PrefixIconType | 否 | 是 | C区（列表右侧）Icon的图标资源。 |
| onClick | OnClickCallback | 否 | 是 | C区（列表右侧）Icon的点击回调。 |
| enable | boolean | 否 | 是 | C区（列表右侧）Icon是否被启用。 true：C区（列表右侧）Icon被启用。 false：C区（列表右侧）Icon被禁用。 默认值：true。 |
| accessibilityOptions | AccessibilityOptions | 否 | 是 | C区（列表右侧）Icon的无障碍播放能力选项。 |

#### SuffixArrowIconTextOptions

HdsListItemCard中C区（列表右侧）箭头图标文本选项 。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| startArrow | SuffixArrowIconOptions | 否 | 是 | C区（列表右侧）起始箭头的选项。 |
| text | TextOptions | 否 | 是 | C区（列表右侧）文本选项。 |
| endArrow | SuffixArrowIconOptions | 否 | 是 | C区（列表右侧）结束箭头的选项。 |

#### SuffixArrowIconOptions

HdsListItemCard中C区（列表右侧）箭头图标选项 。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| arrowColor | ResourceColor | 否 | 是 | C区（列表右侧）箭头的颜色。 |
| onClick | OnClickCallback | 否 | 是 | C区（列表右侧）箭头的点击回调。 |
| arrowId | string | 否 | 是 | C区（列表右侧）箭头的ID。 |
| enable | boolean | 否 | 是 | C区（列表右侧）箭头是否被启用。 true：C区（列表右侧）箭头被启用。 false：C区（列表右侧）箭头被禁用。 默认值：true。 |
| accessibilityOptions | AccessibilityOptions | 否 | 是 | C区（列表右侧）箭头的无障碍播放能力选项。 |

#### SelectStyle

HdsListItemCard中下拉按钮样式选项。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| value | ResourceStr | 否 | 否 | 下拉按钮本身的文本内容。 |
| valueColor | ResourceColor | 否 | 是 | 下拉按钮本身的文本颜色。 默认值：$r('sys.color.font_secondary')。 |
| arrowColor | ResourceColor | 否 | 是 | 下拉按钮箭头的颜色。 默认值：$r('sys.color.icon_secondary')。 |
| optionValues | Array<ResourceStr> | 否 | 否 | 下拉选项内容。 |
| optionSymbol | Array<SymbolGlyphModifier> | 否 | 否 | 下拉选项Symbol图片。 |
| onSelect | OnSelectCallback | 否 | 是 | 下拉菜单选中某一项的回调。 |
| showDefaultSelectedIcon | boolean | 否 | 是 | 是否显示默认选定的图标。 true：显示默认选定的图标。 false：不显示默认选定的图标。 默认值：false。 |
| enable | boolean | 否 | 是 | 下拉按钮是否被启用。 true：下拉按钮被启用。 false：下拉按钮被禁用。 默认值：true。 |
| selectId | string | 否 | 是 | 下拉按钮的Id。 |
| accessibilityOptions | AccessibilityOptions | 否 | 是 | 下拉按钮的无障碍播放能力选项。 |
| selected | number | 否 | 是 | 设置下拉菜单初始选项的索引，第一项的索引为0。当不设置selected属性或设置为异常值时，默认选中值为-1，菜单项不选中。 默认值：-1。 起始版本： 6.1.0(23) |

#### SymbolType

type SymbolType= ResourceStr | SymbolGlyphModifier

HdsListItemCard中支持Symbol图标资源类型。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ResourceStr | 字符串类型。 |
| SymbolGlyphModifier | SymbolGlyph属性样式修改器。 |

#### PrefixIconType

type PrefixIconType= ImageOptions | SymbolGlyphOptions

HdsListItemCard中支持A区（列表左侧）Icon图标资源类型。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ImageOptions | Image类型。 |
| SymbolGlyphOptions | SymbolGlyph类型。 |

#### ImageType

type ImageType = ResourceStr | image.PixelMap

HdsListItemCard中支持Image资源类型。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ResourceStr | 字符串类型。 |
| image.PixelMap | PixelMap类型。 |

#### IconSize

PrefixIcon图标大小枚举。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SMALL_ICON | 1 | A区（列表左侧）Icon图标类型：小图标类型，大小为16vp * 16vp（穿戴设备上为28vp*28vp）。 |
| SYSTEM_ICON | 2 | A区（列表左侧）Icon图标类型：系统图标类型，大小为24vp * 24vp（穿戴设备上为32vp*32vp）。 |


上述描述中所有左侧、中间、右侧均是在LTR模式下。

#### OnClickCallback

type OnClickCallback = () => void

HdsListItemCard中的点击事件回调。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

#### OnChangeCallback

type OnChangeCallback = (isOn: boolean) => void

HdsListItemCard中的onChange事件回调。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isOn | boolean | 是 | HdsListItemCard中的Switch/CheckBox/Radio/ToggleButton选中状态。 - isOn为true时，表示从未选中变为选中。 - isOn为false时，表示从选中变为未选中。 |

#### OnSelectCallback

type OnSelectCallback = (index: number, text: string) => void

HdsListItemCard中的onSelect事件回调。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Full

**起始版本：**6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 选中项的索引，取值范围大于等于0。 |
| text | string | 是 | 选中项的值，无位数要求。 |

**HdsListItemCardModifier**

动态设置HdsListItemCard组件的属性和样式，继承自[HdsListItemCardAttribute](#ZH-CN_TOPIC_0000002553361239__属性)。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.UIDesign.HDSComponent.Core

起始版本： 6.1.0(23)

**applyNormalAttribute**

applyNormalAttribute?(instance: HdsListItemCardAttribute): void

组件普通状态时的样式。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.UIDesign.HDSComponent.Core

起始版本： 6.1.0(23)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| instance | HdsListItemCardAttribute | 是 | 动态设置HdsListItemCard组件的属性。 |

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
      }
      .width('100%')
      .height('100%')
      .margin(10)
    }.backgroundColor(0x1a0a59f7).height('100%')
  }
```

![image](public_sys-resources/zh-cn_image_0000002522245784.webp)