# @ohos.application.formInfo (formInfo)

formInfo模块提供了卡片信息和状态等相关类型和枚举。

本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

从API version 9 开始废弃，建议使用[formInfo](@ohos.app.form.formInfo (formInfo).md)替代。

#### 导入模块

```ets
import { formInfo } from '@kit.FormKit';
```

#### FormInfo

卡片信息。

**系统能力：** SystemCapability.Ability.Form

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| bundleName | string | 否 | 否 | 表示卡片所属包的Bundle名称。 |
| moduleName | string | 否 | 否 | 表示卡片所属模块的模块名。 |
| abilityName | string | 否 | 否 | 表示卡片所属的Ability名称。 |
| name | string | 否 | 否 | 表示卡片名称。 |
| description | string | 否 | 否 | 表示卡片描述。 |
| type | FormType | 否 | 否 | 表示卡片类型，当前支持JS卡片。 |
| jsComponentName | string | 否 | 否 | 表示JS卡片的组件名。 |
| colorMode | ColorMode | 否 | 否 | 表示卡片颜色模式。 |
| isDefault | boolean | 否 | 否 | 表示是否是默认卡片。 - true：默认卡片。 - false：非默认卡片。 |
| updateEnabled | boolean | 否 | 否 | 表示卡片是否使能更新。 - true：表示支持周期性刷新。 - false：表示不支持周期性刷新。 |
| formVisibleNotify | boolean | 否 | 否 | 表示卡片是否使能可见通知。 - true：通知卡片提供方可见状态变化。 - false：不通知卡片提供方可见状态变化。 |
| relatedBundleName | string | 否 | 否 | 表示卡片所属的相关联Bundle名称。 |
| scheduledUpdateTime | string | 否 | 否 | 表示卡片更新时间。 |
| formConfigAbility | string | 否 | 否 | 表示卡片配置ability。 |
| updateDuration | number | 否 | 否 | 表示卡片更新周期。 |
| defaultDimension | number | 否 | 否 | 表示卡片规格。 |
| supportDimensions | Array<number> | 否 | 否 | 表示卡片支持的规格。 |
| customizeData | {[key: string]: [value: string]} | 否 | 否 | 表示卡片用户数据。 |

#### FormType

支持的卡片类型枚举。

**系统能力：** SystemCapability.Ability.Form

| 名称 | 值 | 说明 |
| --- | --- | --- |
| JS | 1 | 卡片类型为JS。 |

#### ColorMode

卡片支持的颜色模式枚举。

**系统能力：** SystemCapability.Ability.Form

| 名称 | 值 | 说明 |
| --- | --- | --- |
| MODE_AUTO | -1 | 表示自动模式。 |
| MODE_DARK | 0 | 表示暗色。 |
| MODE_LIGHT | 1 | 表示亮色。 |

#### FormStateInfo

卡片状态信息。

**系统能力：** SystemCapability.Ability.Form

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| formState | FormState | 否 | 否 | 表示卡片状态。 |
| want | Want | 否 | 否 | Want文本内容。 |

#### FormState

卡片状态枚举。

**系统能力：** SystemCapability.Ability.Form

| 名称 | 值 | 说明 |
| --- | --- | --- |
| UNKNOWN | -1 | 表示未知状态。 |
| DEFAULT | 0 | 表示默认状态。 |
| READY | 1 | 表示就绪状态。 |

#### FormParam

卡片参数枚举。

**系统能力：** SystemCapability.Ability.Form

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DIMENSION_KEY | 'ohos.extra.param.key.form_dimension' | 卡片规格样式。 |
| NAME_KEY | 'ohos.extra.param.key.form_name' | 卡片名称。 |
| MODULE_NAME_KEY | 'ohos.extra.param.key.module_name' | 卡片所属模块名称。 |
| WIDTH_KEY | 'ohos.extra.param.key.form_width' | 卡片宽度。 |
| HEIGHT_KEY | 'ohos.extra.param.key.form_height' | 卡片高度。 |
| TEMPORARY_KEY | 'ohos.extra.param.key.form_temporary' | 临时卡片。 |