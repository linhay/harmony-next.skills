# @ohos.app.form.formInfo (formInfo)

formInfo模块提供了卡片信息和状态等相关类型和枚举。

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { formInfo } from '@kit.FormKit';
```

#### FormInfo

卡片配置信息。

**系统能力：** SystemCapability.Ability.Form

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| bundleName | string | 否 | 否 | 卡片所属包的Bundle名称。  元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| moduleName | string | 否 | 否 | 卡片所属模块的模块名称。  元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| abilityName | string | 否 | 否 | 卡片所属的Ability名称。  元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| name | string | 否 | 否 | 卡片名称。  元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| displayName11+ | string | 否 | 否 | 卡片展示名称。  元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| displayNameId11+ | number | 否 | 否 | 卡片预览时标识卡片名称的ID。  元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| description | string | 否 | 否 | 卡片描述。  元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| descriptionId10+ | number | 否 | 否 | 卡片描述id。  元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| type | FormType | 否 | 否 | 卡片类型。当前支持JS卡片、ArkTS卡片。  元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| jsComponentName | string | 否 | 否 | js卡片的组件名。  元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| colorMode(deprecated) | ColorMode | 否 | 否 | 卡片颜色模式。  元服务API： 从API version 11开始，该接口支持在元服务中使用。  说明：   从API version 9开始支持，从API version 20开始废弃。应用卡片需要支持深浅色两种显示模式，无替代接口。 |
| isDefault | boolean | 否 | 否 | 卡片是否是默认卡片。 - true：默认卡片。 - false：非默认卡片。  元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| updateEnabled | boolean | 否 | 否 | 卡片是否使能更新。 - true：表示支持周期性刷新。 - false：表示不支持周期性刷新。  元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| formVisibleNotify | boolean | 否 | 否 | 卡片是否使能可见通知。 - true：通知卡片提供方可见状态变化。 - false：不通知卡片提供方可见状态变化。  元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| scheduledUpdateTime | string | 否 | 否 | 卡片更新时间。  元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| formConfigAbility | string | 否 | 否 | 卡片配置ability。指定长按卡片弹出的选择框内，编辑选项所对应的ability。  元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| updateDuration | number | 否 | 否 | 卡片更新周期。  元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| defaultDimension | number | 否 | 否 | 卡片规格  元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| supportDimensions | Array<number> | 否 | 否 | 卡片支持的规格。具体可选规格参考FormDimension  元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| customizeData | Record<string, string> | 否 | 否 | 卡片用户数据。  元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| isDynamic10+ | boolean | 否 | 否 | 卡片是否为动态卡片。 仅ArkTS卡片区分动静态卡片，JS卡片均为动态卡片。 - true：为动态卡片。 - false：为静态卡片。  元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| transparencyEnabled11+ | boolean | 否 | 否 | 卡片是否支持设置背景透明度。 ArkTS卡片由用户配置决定是否支持，JS卡片均不支持。 - true：表示是透明卡片。 - false：表示不是透明卡片。  元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| supportedShapes12+ | Array<number> | 否 | 否 | 卡片支持的形状。具体可选形状参考FormShape12+  元服务API： 从API version 12开始，该接口支持在元服务中使用。 |

#### FormType

支持的卡片类型枚举。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Ability.Form

| 名称 | 值 | 说明 |
| --- | --- | --- |
| JS | 1 | 卡片类型为JS。 |
| eTS | 2 | 卡片类型为ArkTS。 |

#### ColorMode(deprecated)

卡片主题样式统一跟随系统的颜色模式，卡片支持的颜色模式枚举。

从API version 9开始支持，从API version 20开始废弃。应用卡片需要支持深浅色两种显示模式，无替代接口。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Ability.Form

| 名称 | 值 | 说明 |
| --- | --- | --- |
| MODE_AUTO | -1 | 表示自动模式。 |
| MODE_DARK | 0 | 表示暗色。 |
| MODE_LIGHT | 1 | 表示亮色。 |

#### FormStateInfo

卡片状态信息。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Ability.Form

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| formState | FormState | 否 | 否 | 卡片状态。 |
| want | Want | 否 | 否 | Want文本内容。 |

#### FormState

卡片状态枚举。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

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
| IDENTITY_KEY | 'ohos.extra.param.key.form_identity' | 卡片标识。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| DIMENSION_KEY | 'ohos.extra.param.key.form_dimension' | 卡片规格，规格尺寸参考FormDimension。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| NAME_KEY | 'ohos.extra.param.key.form_name' | 卡片名称。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| MODULE_NAME_KEY | 'ohos.extra.param.key.module_name' | 卡片所属模块名称。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| WIDTH_KEY | 'ohos.extra.param.key.form_width' | 卡片宽度。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| HEIGHT_KEY | 'ohos.extra.param.key.form_height' | 卡片高度。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| TEMPORARY_KEY | 'ohos.extra.param.key.form_temporary' | 临时卡片。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| ABILITY_NAME_KEY | 'ohos.extra.param.key.ability_name' | ability名称。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| BUNDLE_NAME_KEY | 'ohos.extra.param.key.bundle_name' | Bundle名称。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| LAUNCH_REASON_KEY10+ | 'ohos.extra.param.key.form_launch_reason' | 卡片创建原因。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| PARAM_FORM_CUSTOMIZE_KEY10+ | 'ohos.extra.param.key.form_customize' | 自定义数据。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| FORM_RENDERING_MODE_KEY11+ | 'ohos.extra.param.key.form_rendering_mode' | 卡片渲染模式。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| HOST_BG_INVERSE_COLOR_KEY12+ | 'ohos.extra.param.key.host_bg_inverse_color' | 卡片使用方的背景反色颜色值。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| FORM_LOCATION_KEY12+ | 'ohos.extra.param.key.form_location' | 卡片位置。  OTHER -1 （其他位置）  DESKTOP 0 （桌面）  FORM_CENTER 1 （桌面的卡片中心）  FORM_MANAGER 2 （桌面的卡片管理器）  NEGATIVE_SCREEN 3 （负一屏）  FORM_CENTER_NEGATIVE_SCREEN 4 （负一屏的服务中心）  FORM_MANAGER_NEGATIVE_SCREEN 5 （负一屏的卡片管理器）  SCREEN_LOCK 6 （锁屏）  AI_SUGGESTION 7 （AI智慧助手推荐区） STANDBY 8 （灵动显示界面） |
| FORM_PERMISSION_NAME_KEY12+ | 'ohos.extra.param.key.permission_name' | 用户授权权限名称。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| FORM_PERMISSION_GRANTED_KEY12+ | 'ohos.extra.param.key.permission_granted' | 用户是否授权。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| ORIGINAL_FORM_KEY20+ | 'ohos.extra.param.key.original_form_id' | 用groupId关联的一组卡片，在调整大小时，会先创建新尺寸的卡片，再删除旧尺寸的卡片。新尺寸卡片创建时want参数会通过该key传递旧尺寸卡片的卡片id。 元服务API： 从API version 20开始，该接口支持在元服务中使用。 |
| EDIT_FORM_KEY22+ | 'ohos.extra.param.key.edit_form_id' | 在半模态页面的卡片编辑中，通过onAddForm回调函数传递该key表示被编辑的卡片id，用来确保预览卡片与被编辑卡片信息同步。如果卡片onAddForm回调函数中携带了该key，则说明当前卡片为半模态页面中的预览卡片，需要基于被编辑卡片来筛选预览卡片内容。  元服务API： 从API version 22开始，该接口支持在元服务中使用。 |

#### FormDimension

定义卡片尺寸枚举。

**系统能力：** SystemCapability.Ability.Form

| 名称 | 值 | 说明 |
| --- | --- | --- |
| Dimension_1_2 | 1 | 1 x 2 form。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| Dimension_2_2 | 2 | 2 x 2 form。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| Dimension_2_4 | 3 | 2 x 4 form。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| Dimension_4_4 | 4 | 4 x 4 form。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| Dimension_2_1(deprecated) | 5 | 2 x 1 form。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 说明： 该字段从API version 9开始支持，从API version 20开始废弃。 |
| DIMENSION_1_111+ | 6 | 1 x 1 form。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 说明： 该尺寸仅在锁屏卡片上生效。 |
| DIMENSION_6_412+ | 7 | 6 x 4 form。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| DIMENSION_2_318+ | 8 | 2 x 3 form。 元服务API： 从API version 18开始，该接口支持在元服务中使用。 设备行为差异： 该字段仅在Wearable上生效，在其他设备类型中无效果。 |
| DIMENSION_3_318+ | 9 | 3 x 3 form。 元服务API： 从API version 18开始，该接口支持在元服务中使用。 设备行为差异： 该字段仅在Wearable上生效，在其他设备类型中无效果。 |

#### FormShape12+

定义卡片形状枚举。

**系统能力：** SystemCapability.Ability.Form

| 名称 | 值 | 说明 |
| --- | --- | --- |
| RECT | 1 | 方形 form。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| CIRCLE | 2 | 圆形 form。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |

#### FormInfoFilter

卡片信息过滤器，仅将符合过滤器内要求的卡片信息返回。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Ability.Form

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| moduleName | string | 否 | 是 | 选填，仅保留含moduleName与提供值相符的卡片信息， 未填写时则不通过moduleName进行过滤。 |

#### VisibilityType

卡片当前可见类型枚举。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Ability.Form

| 名称 | 值 | 说明 |
| --- | --- | --- |
| UNKNOWN10+ | 0 | 表示卡片为未知。 |
| FORM_VISIBLE | 1 | 表示卡片为可见。 |
| FORM_INVISIBLE | 2 | 表示卡片为不可见。 |

#### LaunchReason10+

卡片创建原因枚举。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Ability.Form

| 名称 | 值 | 说明 |
| --- | --- | --- |
| FORM_DEFAULT | 1 | 表示卡片创建原因为默认创建。 |
| FORM_SHARE | 2 | 表示卡片创建原因为共享创建。 |
| FORM_SIZE_CHANGE20+ | 3 | 表示卡片创建原因为尺寸变化。 元服务API： 从API version 20开始，该接口支持在元服务中使用。 |

#### OverflowInfo20+

互动卡片动效信息。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Ability.Form

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| area | Rect | 否 | 否 | 描述互动卡片动效区域范围，以卡片左上角为原点，单位为vp。 |
| duration | number | 否 | 否 | 互动卡片动效持续时长，单位ms。取值为大于0的整数，取值要求不大于3500。 |
| useDefaultAnimation | boolean | 否 | 是 | 互动卡片状态切换时是否启动系统提供的默认动效，默认为true。 - true：表示系统提供默认切换动效。 - false：表示系统不提供切换动效，画面直接切换，适合切换时非激活态和激活态UI完全一致的场景。 |

#### Rect20+

通用矩形区域信息。可用于描述卡片位置、互动卡片动效区域等信息。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Ability.Form

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| left | number | 否 | 否 | 描述矩形的左上角顶点的 x 坐标，单位：vp。 |
| top | number | 否 | 否 | 描述矩形的左上角顶点的 y 坐标，单位：vp。 |
| width | number | 否 | 否 | 描述矩形的宽度，单位：vp。 |
| height | number | 否 | 否 | 描述矩形的高度，单位：vp。 |

#### FormLocation20+

卡片当前位置枚举。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.Form

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DESKTOP | 0 | 表示卡片位于桌面。 |
| FORM_CENTER | 1 | 表示卡片位于桌面的卡片中心。 |
| FORM_MANAGER | 2 | 表示卡片位于桌面的卡片管理器。 |
| NEGATIVE_SCREEN | 3 | 表示卡片位于负一屏。 |
| SCREEN_LOCK | 6 | 表示卡片位于锁屏页面。 |
| AI_SUGGESTION | 7 | 表示卡片位于小艺建议的推荐区。 |
| STANDBY | 8 | 表示卡片位于灵动显示界面。 |

#### RunningFormInfo20+

已经添加到桌面的卡片信息。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Ability.Form

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| formId | string | 是 | 否 | 卡片标识。 |
| bundleName | string | 是 | 否 | 卡片提供方所属包的Bundle名称。 |
| moduleName | string | 是 | 否 | 卡片所属模块的名称。 |
| abilityName | string | 是 | 否 | 卡片所属的Ability名称。 |
| formName | string | 是 | 否 | 卡片名称。 |
| dimension | number | 是 | 否 | 卡片尺寸，取值及其对应含义请参考FormDimension。 |
| formLocation | FormLocation | 是 | 否 | 卡片位置信息。 |