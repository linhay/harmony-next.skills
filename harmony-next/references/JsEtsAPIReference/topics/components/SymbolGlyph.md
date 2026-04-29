# SymbolGlyph

显示图标小符号的组件。相关资源可参考[系统图标](https://developer.huawei.com/consumer/cn/doc/design-guides/system-icons-0000001929854962)。

  ![image](public_sys-resources/note_3.0-zh-cn.webp)

 该组件从API version 11开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

**子组件**

不支持子组件。

**接口**

SymbolGlyph(value?: Resource)

卡片能力： 从API version 12开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Resource | 否 | SymbolGlyph组件的资源名，如 $r('sys.symbol.ohos_wifi')。 |

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

 $r('sys.symbol.ohos_wifi')中引用的资源为系统预置，SymbolGlyph仅支持系统预置的symbol资源名，引用非symbol资源将显示异常。

**属性**

支持[通用属性](通用属性.md)，不支持文本通用属性，仅支持以下特有属性：

**fontColor**

fontColor(value: Array<ResourceColor>)

设置SymbolGlyph组件颜色。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

从API version 12开始，该接口支持在[attributeModifier](动态属性设置.md#ZH-CN_TOPIC_0000002522240800__attributemodifier)中调用。

卡片能力： 从API version 12开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Array<ResourceColor> | 是 | SymbolGlyph组件颜色。  默认值：不同渲染策略下默认值不同。 |

**fontSize**

fontSize(value: number | string | Resource)

设置SymbolGlyph组件大小。设置string类型时，支持number类型取值的字符串形式，可以附带单位，例如"10"、"10fp"。

组件的图标显示大小由fontSize控制，设置width或height后，其他通用属性仅对组件的占位大小生效。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

从API version 12开始，该接口支持在[attributeModifier](动态属性设置.md#ZH-CN_TOPIC_0000002522240800__attributemodifier)中调用。

卡片能力： 从API version 12开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | string | Resource | 是 | SymbolGlyph组件大小。 默认值：16fp 单位：fp 不支持设置百分比字符串。 |

**fontWeight**

fontWeight(value: number | FontWeight | string)

设置SymbolGlyph组件粗细。number类型取值[100,900]，取值间隔为100，默认为400，取值越大，字体越粗。string类型仅支持number类型取值的字符串形式，例如“400”，以及“bold”、“bolder”、“lighter”、“regular” 、“medium”分别对应FontWeight中相应的枚举值。

sys.symbol.ohos_lungs图标不支持设置fontWeight。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

从API version 12开始，该接口支持在[attributeModifier](动态属性设置.md#ZH-CN_TOPIC_0000002522240800__attributemodifier)中调用。

卡片能力： 从API version 12开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | FontWeight | string | 是 | SymbolGlyph组件粗细。 默认值：FontWeight.Normal |

**renderingStrategy**

renderingStrategy(value: SymbolRenderingStrategy)

设置SymbolGlyph组件渲染策略。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

从API version 12开始，该接口支持在[attributeModifier](动态属性设置.md#ZH-CN_TOPIC_0000002522240800__attributemodifier)中调用。

卡片能力： 从API version 12开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | SymbolRenderingStrategy | 是 | SymbolGlyph组件渲染策略。 默认值：SymbolRenderingStrategy.SINGLE |

不同渲染策略效果可参考以下示意图。

![image](public_sys-resources/zh-cn_image_0000002522085086.webp)

**effectStrategy**

effectStrategy(value: SymbolEffectStrategy)

设置SymbolGlyph组件动效策略。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

从API version 12开始，该接口支持在[attributeModifier](动态属性设置.md#ZH-CN_TOPIC_0000002522240800__attributemodifier)中调用。

卡片能力： 从API version 12开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | SymbolEffectStrategy | 是 | SymbolGlyph组件动效策略。 默认值：SymbolEffectStrategy.NONE |

**symbolEffect12+**

symbolEffect(symbolEffect: SymbolEffect, isActive?: boolean)

设置SymbolGlyph组件动效策略及播放状态。

卡片能力： 从API version 12开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| symbolEffect | SymbolEffect | 是 | SymbolGlyph组件动效策略。 默认值：SymbolEffect |
| isActive | boolean | 否 | SymbolGlyph组件动效播放状态。 true表示播放，false表示不播放。 默认值：false |

**symbolEffect12+**

symbolEffect(symbolEffect: SymbolEffect, triggerValue?: number)

设置SymbolGlyph组件动效策略及播放触发器。

卡片能力： 从API version 12开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| symbolEffect | SymbolEffect | 是 | SymbolGlyph组件动效策略。 默认值：SymbolEffect |
| triggerValue | number | 否 | SymbolGlyph组件动效播放触发器，在数值变更时触发动效。 如果首次不希望触发动效，设置-1。 |

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

 动效属性，仅支持使用effectStrategy属性或单个symbolEffect属性，不支持多种动效属性混合使用。

**minFontScale18+**

minFontScale(scale: Optional<number | Resource>)

设置SymbolGlyph组件最小的字体缩放倍数。

元服务API： 从API version 18开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scale | Optional<number | Resource> | 是 | SymbolGlyph组件最小的字体缩放倍数。 取值范围：[0, 1]  设置为0，缩放最小。 说明：  设置的值小于0时，按值为0处理。设置的值大于1，按值为1处理。异常值默认不生效。 |

**maxFontScale18+**

maxFontScale(scale: Optional<number | Resource>)

设置SymbolGlyph组件最大的字体缩放倍数。

元服务API： 从API version 18开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scale | Optional<number | Resource> | 是 | SymbolGlyph组件最大的字体缩放倍数。 取值范围：[1, +∞) 说明：  设置的值小于1时，按值为1处理，异常值默认不生效。 |

**shaderStyle20+**

shaderStyle(shader: Array<ShaderStyle | undefined> | ShaderStyle)

设置SymbolGlyph组件的渐变色效果。

可以显示为径向渐变[RadialGradientStyle](文本组件公共接口.md#ZH-CN_TOPIC_0000002553200813__radialgradientstyle20)或线性渐变[LinearGradientStyle](文本组件公共接口.md#ZH-CN_TOPIC_0000002553200813__lineargradientstyle20)或纯色[ColorShaderStyle](文本组件公共接口.md#ZH-CN_TOPIC_0000002553200813__colorshaderstyle20)的效果，shaderStyle的优先级高于[fontColor](SymbolSpan.md#ZH-CN_TOPIC_0000002553360771__fontcolor)和AI识别，纯色建议使用[fontColor](SymbolSpan.md#ZH-CN_TOPIC_0000002553360771__fontcolor)。

元服务API： 从API version 20开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| shader | Array<ShaderStyle | undefined> | ShaderStyle | 是 | 径向渐变或线性渐变或纯色。 传入ShaderStyle时，覆盖所有层；传入数组时，数据项是ShaderStyle，则应用该层；数组项是undefined，则该层使用SymbolGlyph默认颜色，未设置的层也应用默认颜色。根据传入的参数区分处理径向渐变RadialGradientStyle或线性渐变LinearGradientStyle或纯色ColorShaderStyle，最终设置到SymbolGlyph组件上显示为渐变色效果。 说明：  单位：vp 中心点请按百分比使用。如果使用的是非百分比（例如10PX），效果等同于设置1000%。 半径建议使用百分比。 百分比是基于图标大小的百分比，建议取值范围[0, 1)。 |

**symbolShadow20+**

symbolShadow(shadow: Optional<ShadowOptions>)

设置SymbolGlyph组件的阴影效果。

卡片能力： 从API version 20开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 20开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| shadow | Optional<ShadowOptions> | 是 | SymbolGlyph组件的阴影效果。 单位：vp 默认值：{ radius：0, color：Color.Black, offsetX：0, offsetY：0 }  不支持fill、type属性和color中的ColoringStrategy枚举值。 |

**ScaleSymbolEffect12+**

ScaleSymbolEffect继承自父类SymbolEffect。

卡片能力： 从API version 12开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

**属性**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| scope | EffectScope | 否 | 是 | 动效范围。 默认值：EffectScope.LAYER |
| direction | EffectDirection | 否 | 是 | 动效方向。 默认值：EffectDirection.DOWN |

**constructor12+**

constructor(scope?: EffectScope, direction?: EffectDirection)

ScaleSymbolEffect的构造函数，缩放动效。

卡片能力： 从API version 12开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scope | EffectScope | 否 | 动效范围。 默认值：EffectScope.LAYER |
| direction | EffectDirection | 否 | 动效方向。 默认值：EffectDirection.DOWN |

**HierarchicalSymbolEffect12+**

HierarchicalSymbolEffect继承自父类SymbolEffect。

卡片能力： 从API version 12开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

**属性**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| fillStyle | EffectFillStyle | 否 | 是 | 动效模式。 默认值：EffectFillStyle.CUMULATIVE |

**constructor12+**

constructor(fillStyle?: EffectFillStyle)

HierarchicalSymbolEffect的构造函数，层级动效。

卡片能力： 从API version 12开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fillStyle | EffectFillStyle | 否 | 动效模式。 默认值：EffectFillStyle.CUMULATIVE |

**AppearSymbolEffect12+**

AppearSymbolEffect继承自父类SymbolEffect。

卡片能力： 从API version 12开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

**属性**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| scope | EffectScope | 否 | 是 | 动效范围。 默认值：EffectScope.LAYER |

**constructor12+**

constructor(scope?: EffectScope)

AppearSymbolEffect的构造函数，出现动效。

卡片能力： 从API version 12开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scope | EffectScope | 否 | 动效范围。 默认值：EffectScope.LAYER |

**DisappearSymbolEffect12+**

DisappearSymbolEffect继承自父类SymbolEffect。

卡片能力： 从API version 12开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

**属性**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| scope | EffectScope | 否 | 是 | 动效范围。 默认值：EffectScope.LAYER |

**constructor12+**

constructor(scope?: EffectScope)

DisappearSymbolEffect的构造函数，消失动效。

卡片能力： 从API version 12开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scope | EffectScope | 否 | 动效范围。 默认值：EffectScope.LAYER |

**BounceSymbolEffect12+**

BounceSymbolEffect继承自父类SymbolEffect。

卡片能力： 从API version 12开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

**属性**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| scope | EffectScope | 否 | 是 | 动效范围。 默认值：EffectScope.LAYER |
| direction | EffectDirection | 否 | 是 | 动效方向。 默认值：EffectDirection.DOWN |

**constructor12+**

constructor(scope?: EffectScope, direction?: EffectDirection)

BounceSymbolEffect的构造函数，弹跳动效。

卡片能力： 从API version 12开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scope | EffectScope | 否 | 动效范围。 默认值：EffectScope.LAYER |
| direction | EffectDirection | 否 | 动效方向。 默认值：EffectDirection.DOWN |

**ReplaceSymbolEffect12+**

ReplaceSymbolEffect继承自父类SymbolEffect。

卡片能力： 从API version 12开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

**属性**

系统能力： SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| scope | EffectScope | 否 | 是 | 动效范围。 默认值：EffectScope.LAYER  卡片能力： 从API version 12开始，该接口支持在ArkTS卡片中使用。  元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| replaceType20+ | ReplaceEffectType | 否 | 是 | 替换动效类型。 默认值：ReplaceEffectType.SEQUENTIAL  卡片能力： 从API version 20开始，该接口支持在ArkTS卡片中使用。  元服务API： 从API version 20开始，该接口支持在元服务中使用。 |

**constructor12+**

constructor(scope?: EffectScope)

ReplaceSymbolEffect的构造函数，替换动效。

卡片能力： 从API version 12开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scope | EffectScope | 否 | 动效范围。 默认值：EffectScope.LAYER |

**constructor20+**

constructor(scope?: EffectScope, replaceType?: ReplaceEffectType)

ReplaceSymbolEffect的构造函数，替换动效。支持指定具体的替换动效类型。

卡片能力： 从API version 20开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 20开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scope | EffectScope | 否 | 动效范围。 默认值：EffectScope.LAYER |
| replaceType | ReplaceEffectType | 否 | 替换动效类型。 默认值：ReplaceEffectType.SEQUENTIAL |

**SymbolEffectStrategy11+枚举说明**

动效类型的枚举值。设置动效后，动效启动即生效，无需触发。

卡片能力： 从API version 12开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NONE | 0 | 无动效（默认值）。 |
| SCALE | 1 | 整体缩放动效。 |
| HIERARCHICAL | 2 | 层级动效。 |

**SymbolRenderingStrategy11+枚举说明**

渲染模式的枚举值。

卡片能力： 从API version 12开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SINGLE | 0 | 单色模式（默认值）。  可以设置一个或者多个颜色，默认为黑色。  当设置多个颜色时，仅生效第一个颜色。 |
| MULTIPLE_COLOR | 1 | 多色模式。  最多可以设置三个颜色。当只设置一个颜色时，修改symbol图标的第一层颜色，其他颜色保持默认颜色。  颜色设置顺序与图标分层顺序匹配，当颜色数量大于图标分层时，多余的颜色不生效。  仅支持设置颜色，设置透明度设置不生效。 |
| MULTIPLE_OPACITY | 2 | 分层模式。  默认为黑色，可以设置一个或者多个颜色。当设置多个颜色时，仅生效第一个颜色。 不透明度与图层相关，symbol图标的第一层透明度为100%、第二层透明度为50%、第三层透明度为20%。 |

**SymbolEffect12+对象说明**

定义SymbolEffect类。

卡片能力： 从API version 12开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

**PulseSymbolEffect12+对象说明**

PulseSymbolEffect继承自父类SymbolEffect，脉冲动效。

卡片能力： 从API version 12开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

**EffectDirection12+枚举说明**

卡片能力： 从API version 12开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DOWN | 0 | 图标缩小再复原。 |
| UP | 1 | 图标放大再复原。 |

**EffectScope12+枚举说明**

卡片能力： 从API version 12开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| LAYER | 0 | 分层模式。 |
| WHOLE | 1 | 整体模式。 |

**EffectFillStyle12+枚举说明**

卡片能力： 从API version 12开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CUMULATIVE | 0 | 累加模式。 |
| ITERATIVE | 1 | 迭代模式。 |

**ReplaceEffectType20+枚举说明**

替换动效类型的枚举值。

卡片能力： 从API version 20开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 20开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SEQUENTIAL | 0 | 默认替换动效：当前symbol完全消失后，新symbol出现。 |
| CROSS_FADE | 1 | 快速替换动效：当前symbol淡出的同时，新symbol淡入，产生更流畅、更快速的过渡效果。 |
| SLASH_OVERLAY | 2 | 禁用动效：用带有斜杠遮罩层的symbol替换当前symbol，通常用于表示禁用或非活动状态。 |

**事件**

支持[通用事件](通用事件.md)。

**示例**

**示例1（设置渲染和动效策略）**

从API version 11开始，该示例通过[renderingStrategy](#ZH-CN_TOPIC_0000002522240846__renderingstrategy)、[effectStrategy](#ZH-CN_TOPIC_0000002522240846__effectstrategy)属性展示了不同的渲染和动效策略。

```ets
// xxx.ets
@Entry
@Component
struct Index {
  build() {
    Column() {
      Row() {
        Column() {
          Text("Light")
          SymbolGlyph($r('sys.symbol.ohos_trash'))
            .fontWeight(FontWeight.Lighter)
            .fontSize(96)
        }

        Column() {
          Text("Normal")
          SymbolGlyph($r('sys.symbol.ohos_trash'))
            .fontWeight(FontWeight.Normal)
            .fontSize(96)
        }

        Column() {
          Text("Bold")
          SymbolGlyph($r('sys.symbol.ohos_trash'))
            .fontWeight(FontWeight.Bold)
            .fontSize(96)
        }

      Row() {
        Column() {
          Text("单色")
          SymbolGlyph($r('sys.symbol.ohos_folder_badge_plus'))
            .fontSize(96)
            .renderingStrategy(SymbolRenderingStrategy.SINGLE)
            .fontColor([Color.Black, Color.Green, Color.White])
        }

        Column() {
          Text("多色")
          SymbolGlyph($r('sys.symbol.ohos_folder_badge_plus'))
            .fontSize(96)
            .renderingStrategy(SymbolRenderingStrategy.MULTIPLE_COLOR)
            .fontColor([Color.Black, Color.Green, Color.White])
        }

        Column() {
          Text("分层")
          SymbolGlyph($r('sys.symbol.ohos_folder_badge_plus'))
            .fontSize(96)
            .renderingStrategy(SymbolRenderingStrategy.MULTIPLE_OPACITY)
            .fontColor([Color.Black, Color.Green, Color.White])
        }

      Row() {
        Column() {
          Text("无动效")
          SymbolGlyph($r('sys.symbol.ohos_wifi'))
            .fontSize(96)
            .effectStrategy(SymbolEffectStrategy.NONE)
        }

        Column() {
          Text("整体缩放动效")
          SymbolGlyph($r('sys.symbol.ohos_wifi'))
            .fontSize(96)
            .effectStrategy(SymbolEffectStrategy.SCALE)
        }

        Column() {
          Text("层级动效")
          SymbolGlyph($r('sys.symbol.ohos_wifi'))
            .fontSize(96)
            .effectStrategy(SymbolEffectStrategy.HIERARCHICAL)
        }
```

![image](public_sys-resources/zh-cn_image_0000002553205041.webp)

**示例2（设置动效和阴影）**

从API version 12开始，该示例通过[symbolEffect](#ZH-CN_TOPIC_0000002522240846__symboleffect12)属性展示了各种动效的效果以及结合[symbolShadow](#ZH-CN_TOPIC_0000002522240846__symbolshadow20)（从API version 20开始）的阴影效果。

```ets
// xxx.ets
@Entry
@Component
struct Index {
  @State isActive: boolean = true;
  @State triggerValueReplace: number = 0;
  @State triggerValueReplace1: number = 0;
  @State triggerValueReplace2: number = 0;
  @State renderMode: number = 1;

  replaceFlag: boolean = true;
  replaceFlag1: boolean = true;
  replaceFlag2: boolean = true;

  options: ShadowOptions = {
    radius: 10.0,
    color: Color.Blue,
    offsetX: 10,
    offsetY: 10,
  };

  build() {
    Column() {
      Row() {
        Column() {
          Text("可变颜色动效")
          SymbolGlyph($r('sys.symbol.ohos_wifi'))
            .fontSize(96)
            .symbolEffect(new HierarchicalSymbolEffect(EffectFillStyle.ITERATIVE), this.isActive)
          Button(this.isActive ? '关闭' : '播放')
            .onClick(() => {
              this.isActive = !this.isActive;
            })
        }
        .margin({ right: 20 })
        Column() {
          Text("替换动效")
          SymbolGlyph(this.replaceFlag ? $r('sys.symbol.checkmark_circle') : $r('sys.symbol.repeat_1'))
            .fontSize(96)
            .symbolEffect(new ReplaceSymbolEffect(EffectScope.WHOLE), this.triggerValueReplace)
          Button('trigger')
            .onClick(() => {
              this.replaceFlag = !this.replaceFlag;
              this.triggerValueReplace = this.triggerValueReplace + 1;
            })
        }
        .margin({ right: 20 })
      }

      Row() {
        Column() {
          Text("禁用动效")
          SymbolGlyph(this.replaceFlag1 ? $r('sys.symbol.eye_slash') : $r('sys.symbol.eye'))
            .fontSize(96)
            .renderingStrategy(this.renderMode)
            .symbolEffect(new ReplaceSymbolEffect(EffectScope.LAYER, ReplaceEffectType.SLASH_OVERLAY), this.triggerValueReplace1)
          Button('trigger')
            .onClick(() => {
              this.replaceFlag1 = !this.replaceFlag1;
              this.triggerValueReplace1 = this.triggerValueReplace1 + 1;
            })
        }
        .margin({ right: 20 })
        Column() {
          Text("快速替换动效")
          SymbolGlyph(this.replaceFlag2 ? $r('sys.symbol.checkmark_circle') : $r('sys.symbol.repeat_1'))
            .fontSize(96)
            .symbolEffect(new ReplaceSymbolEffect(EffectScope.WHOLE, ReplaceEffectType.CROSS_FADE), this.triggerValueReplace2)
          Button('trigger')
            .onClick(() => {
              this.replaceFlag2 = !this.replaceFlag2;
              this.triggerValueReplace2 = this.triggerValueReplace2 + 1;
            })
        }
        .margin({ right: 20 })
        Column() {
          Text("阴影能力")
          SymbolGlyph($r('sys.symbol.ohos_wifi'))
            .fontSize(96)
            .symbolEffect(new HierarchicalSymbolEffect(EffectFillStyle.ITERATIVE), this.isActive)
            .symbolShadow(this.options)
          Button(this.isActive ? '关闭' : '播放')
            .onClick(() => {
              this.isActive = !this.isActive;
            })
        }
        .margin({ right: 20 })
      }
    .margin({
      left: 45,
      top: 50
    })
  }
```

![image](public_sys-resources/zh-cn_image_0000002522085088.webp)

**示例3（设置颜色渐变）**

从API version 20开始，该示例通过[shaderStyle](#ZH-CN_TOPIC_0000002522240846__shaderstyle20)接口实现了symbolGlyph组件显示为渐变色的功能。

```ets
@Entry
@Component
struct Index {
  @State message: string = 'Hello World';

  linearGradientOptions1: LinearGradientOptions = {
    angle: 45,
    colors: [[Color.Red, 0.0], [Color.Blue, 0.3], [Color.Green, 0.5]]
  };

  linearGradientOptions2: LinearGradientOptions = {
    direction: GradientDirection.LeftTop,
    colors: [[Color.Red, 0.0], [Color.Blue, 0.3], [Color.Green, 0.5]],
    repeating: true,
  };

  radialGradientOptions: RadialGradientOptions = {
    center: ["50%", "50%"],
    radius: "20%",
    colors: [[Color.Red, 0.0], [Color.Blue, 0.3], [Color.Green, 0.5]],
    repeating: true,
  };

  build() {
    Column() {
      Row() {
        Column() {
          Text('angle为45°的线性渐变')
            .fontSize(18)
            .fontColor(0xCCCCCC)
            .textAlign(TextAlign.Center)
          SymbolGlyph($r('sys.symbol.ohos_folder_badge_plus'))
            .fontSize(96)
            .shaderStyle([new LinearGradientStyle(this.linearGradientOptions1)])
        }
        .margin({ right: 20 })
        Column() {
          Text('LeftTop的线性渐变')
            .fontSize(18)
            .fontColor(0xCCCCCC)
            .textAlign(TextAlign.Center)
          SymbolGlyph($r('sys.symbol.ohos_folder_badge_plus'))
            .fontSize(96)
            .shaderStyle([new LinearGradientStyle(this.linearGradientOptions2)])
        }
        .margin({ right: 20 })
      }

      Row() {
        Column() {
          Text('径向渐变')
            .fontSize(18)
            .fontColor(0xCCCCCC)
            .textAlign(TextAlign.Center)
          SymbolGlyph($r('sys.symbol.ohos_folder_badge_plus'))
            .fontSize(96)
            .shaderStyle([new RadialGradientStyle(this.radialGradientOptions)])
        }
        .margin({ right: 20 })
        Column() {
          Text('纯色')
            .fontSize(18)
            .fontColor(0xCCCCCC)
            .textAlign(TextAlign.Center)
          SymbolGlyph($r('sys.symbol.ohos_folder_badge_plus'))
            .fontSize(96)
            .shaderStyle([new ColorShaderStyle(Color.Red)])
        }
        .margin({ right: 20 })
        Column() {
          Text('线性和径向渐变')
            .fontSize(18)
            .fontColor(0xCCCCCC)
            .textAlign(TextAlign.Center)
          SymbolGlyph($r('sys.symbol.ohos_folder_badge_plus'))
            .fontSize(96)
            .shaderStyle([
              new LinearGradientStyle(this.linearGradientOptions2),
              new RadialGradientStyle(this.radialGradientOptions)
            ])
            .renderingStrategy(SymbolRenderingStrategy.MULTIPLE_OPACITY)
        }
        .margin({ right: 20 })
      }

      Row() {
        Column() {
          Text('数组单层渐变')
            .fontSize(18)
            .fontColor(0xCCCCCC)
            .textAlign(TextAlign.Center)
          SymbolGlyph($r('sys.symbol.ohos_folder_badge_plus'))
            .fontSize(96)
            .shaderStyle([
              new LinearGradientStyle(this.linearGradientOptions2),
            ])
            .renderingStrategy(SymbolRenderingStrategy.MULTIPLE_OPACITY)
        }.margin({ right: 20 })

        Column() {
          Text('非数组覆盖全部')
            .fontSize(18)
            .fontColor(0xCCCCCC)
            .textAlign(TextAlign.Center)
          SymbolGlyph($r('sys.symbol.ohos_folder_badge_plus'))
            .fontSize(96)
            .shaderStyle(new RadialGradientStyle(this.radialGradientOptions))
            .renderingStrategy(SymbolRenderingStrategy.MULTIPLE_OPACITY)
        }.margin({ right: 20 })

        Column() {
          Text('首层为默认')
            .fontSize(18)
            .fontColor(0xCCCCCC)
            .textAlign(TextAlign.Center)
          SymbolGlyph($r('sys.symbol.ohos_folder_badge_plus'))
            .fontSize(96)
            .shaderStyle([
              undefined,
              new LinearGradientStyle(this.linearGradientOptions2),
            ])
            .renderingStrategy(SymbolRenderingStrategy.MULTIPLE_OPACITY)
        }.margin({ right: 20 })
      }
    .margin({
      left: 20,
      top: 50
    })
  }
```

![image](public_sys-resources/zh-cn_image_0000002553365005.webp)