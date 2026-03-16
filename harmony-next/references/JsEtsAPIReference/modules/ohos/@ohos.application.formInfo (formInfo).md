# @ohos.application.formInfo (formInfo)

formInfo模块提供了卡片信息和状态等相关类型和枚举。

本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

从API version 9 开始不再维护，建议使用[formInfo](@ohos.app.form.formInfo (formInfo).md)替代。

#### 导入模块

```ets
import formInfo from '@ohos.application.formInfo';
```

#### FormInfo

卡片信息。

**系统能力：** SystemCapability.Ability.Form

名称类型只读可选说明bundleNamestring否否表示卡片所属包的Bundle名称。moduleNamestring否否表示卡片所属模块的模块名。abilityNamestring否否表示卡片所属的Ability名称。namestring否否表示卡片名称。descriptionstring否否表示卡片描述。type[FormType](#ZH-CN_TOPIC_0000002497605284__formtype)否否表示卡片类型，当前支持JS卡片。jsComponentNamestring否否表示JS卡片的组件名。colorMode[ColorMode](#ZH-CN_TOPIC_0000002497605284__colormode)否否表示卡片颜色模式。isDefaultboolean否否

表示是否是默认卡片。

- true：默认卡片。

- false：非默认卡片。

updateEnabledboolean否否

表示卡片是否使能更新。

- true：表示支持周期性刷新。

- false：表示不支持周期性刷新。

formVisibleNotifyboolean否否

表示卡片是否使能可见通知。

- true：通知卡片提供方可见状态变化。

- false：不通知卡片提供方可见状态变化。

relatedBundleNamestring否否表示卡片所属的相关联Bundle名称。scheduledUpdateTimestring否否表示卡片更新时间。formConfigAbilitystring否否表示卡片配置ability。updateDurationnumber否否表示卡片更新周期。defaultDimensionnumber否否表示卡片规格。supportDimensionsArray<number>否否表示卡片支持的规格。customizeData{[key: string]: [value: string]}否否表示卡片用户数据。

#### FormType

支持的卡片类型枚举。

**系统能力：** SystemCapability.Ability.Form

名称值说明JS1卡片类型为JS。

#### ColorMode

卡片支持的颜色模式枚举。

**系统能力：** SystemCapability.Ability.Form

名称值说明MODE_AUTO-1表示自动模式。MODE_DARK0表示暗色。MODE_LIGHT1表示亮色。

#### FormStateInfo

卡片状态信息。

**系统能力：** SystemCapability.Ability.Form

名称类型只读可选说明formState[FormState](#ZH-CN_TOPIC_0000002497605284__formstate)否否表示卡片状态。want[Want](@ohos.app.ability.Want (Want).md)否否Want文本内容。

#### FormState

卡片状态枚举。

**系统能力：** SystemCapability.Ability.Form

名称值说明UNKNOWN-1表示未知状态。DEFAULT0表示默认状态。READY1表示就绪状态。

#### FormParam

卡片参数枚举。

**系统能力：** SystemCapability.Ability.Form

名称值说明DIMENSION_KEY'ohos.extra.param.key.form_dimension'卡片规格样式。NAME_KEY'ohos.extra.param.key.form_name'卡片名称。MODULE_NAME_KEY'ohos.extra.param.key.module_name'卡片所属模块名称。WIDTH_KEY'ohos.extra.param.key.form_width'卡片宽度。HEIGHT_KEY'ohos.extra.param.key.form_height'卡片高度。TEMPORARY_KEY'ohos.extra.param.key.form_temporary'临时卡片。