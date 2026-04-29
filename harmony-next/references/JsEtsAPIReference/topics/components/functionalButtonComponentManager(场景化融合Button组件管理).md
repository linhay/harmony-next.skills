# functionalButtonComponentManager(场景化融合Button组件管理)

本模块提供Button组件的逻辑管理，辅助HarmonyOS应用和元服务通过Button组件完成相应功能。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力****：**SystemCapability.AtomicserviceComponent.UIComponent

**起始版本：**4.1.0(11)

#### 导入模块

```ets
import { functionalButtonComponentManager } from '@kit.ScenarioFusionKit';
```

#### OpenType

该枚举定义了[FunctionalButton](FunctionalButton（Button组件）.md#section1753203873911)组件的功能类型，通过设置该参数来指定FunctionalButton的功能。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力****：**SystemCapability.AtomicserviceComponent.UIComponent

**起始版本：**4.1.0(11)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| GET_PHONE_NUMBER | 0 | 快速验证手机号。 元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| GET_REALTIME_PHONENUMBER | 1 | 实时验证手机号。 元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。 说明：  从版本5.0.0(12)开始，GET_REALTIME_PHONENUMBER暂不对外开放使用。 |
| LAUNCH_APP | 2 | 打开APP。 元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| OPEN_SETTING | 3 | 打开授权设置页。 元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。 说明：  从版本5.0.2(14)开始，OPEN_SETTING不再演进，建议使用PERMISSION_SETTING。 |
| CHOOSE_AVATAR | 4 | 选择头像。 元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| CHOOSE_ADDRESS | 5 | 选择地址。 起始版本： 5.0.0(12) 元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。 |
| CHOOSE_INVOICE_TITLE | 6 | 选择发票抬头。 起始版本： 5.0.0(12) 元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。 |
| REAL_NAME_AUTHENTICATION | 7 | 实名信息校验。 起始版本： 5.0.0(12) 元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。 说明：  REAL_NAME_AUTHENTICATION暂不对外开放使用。 |
| FACE_AUTHENTICATION | 8 | 人脸核身。 起始版本： 5.0.0(12) 元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。 说明：  FACE_AUTHENTICATION暂不对外开放使用。 |
| CHOOSE_LOCATION | 9 | 地图选点。 起始版本： 5.0.0(12) 元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。 |
| SUBSCRIBE_LIVE_VIEW | 10 | 实况窗订阅。 起始版本： 5.0.0(12) 说明：  SUBSCRIBE_LIVE_VIEW暂不对外开放使用。 |
| PERMISSION_SETTING | 11 | 权限设置。 起始版本： 5.0.2(14) 元服务API： 从版本5.0.2(14)开始，该接口支持在元服务中使用。 |
| REQUEST_SUBSCRIBE_MESSAGE | 12 | 服务动态授权码按钮的类型。 起始版本： 6.0.0(20) 元服务API： 从版本6.0.0(20)开始，该接口支持在元服务中使用。 |
| SHARE | 13 | 分享按钮的类型。 起始版本： 6.0.0(20) 元服务API： 从版本6.0.0(20)开始，该接口支持在元服务中使用。 |
| FEEDBACK | 14 | 反馈按钮的类型。 起始版本： 6.0.0(20) 元服务API： 从版本6.0.0(20)开始，该接口支持在元服务中使用。 |
| GET_PHONE_NUMBER_AND_RISK_LEVEL | 15 | 获取手机号和风险等级。 起始版本： 6.0.2(22) 元服务API： 从版本6.0.2(22)开始，该接口支持在元服务中使用。 |

#### SizeType

该枚举定义了[FunctionalButton](FunctionalButton（Button组件）.md#section1753203873911)的尺寸类型。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.AtomicserviceComponent.UIComponent

**起始版本：**4.1.0(11)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DEFAULT | 0 | 默认大小。 |
| MINI | 1 | 小尺寸。 |

#### HoverClassType

该枚举定义了[FunctionalButton](FunctionalButton（Button组件）.md#section1753203873911)点击态的类型。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.AtomicserviceComponent.UIComponent

**起始版本：**4.1.0(11)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NONE | 0 | 无效果。 |
| HOVER_CLASS | 1 | 默认样式。 |

#### ColorType

该枚举定义了[FunctionalButton](FunctionalButton（Button组件）.md#section1753203873911)的颜色类型。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.AtomicserviceComponent.UIComponent

**起始版本：**4.1.0(11)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DEFAULT | 0 | 蓝色。 |
| PRIMARY | 1 | 绿色。 |
| WARN | 2 | 红色。 |

#### CredentialType(deprecated)


从5.0.0(12)开始支持，从6.0.2(22)开始废弃，无替代接口。

该枚举定义了[FunctionalButton](FunctionalButton（Button组件）.md#section1753203873911)的认证类型。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.AtomicserviceComponent.UIComponent

**起始版本：**5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| IDCard | 0 | 身份证件类型。 |

#### RealNameAuthenticationInfo(deprecated)


从5.0.0(12)开始支持，从6.0.2(22)开始废弃，无替代接口。

该接口定义了[FunctionalButton](FunctionalButton（Button组件）.md#section1753203873911)组件的实名信息校验对象（预留能力，暂未支持）。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.AtomicserviceComponent.UIComponent

**起始版本：**5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| openID | string | 否 | 否 | OpenID是华为账号用户在不同类型的产品的身份ID，同一个用户，不同应用，OpenID值不同。 |
| realName | string | 否 | 否 | 证件姓名。 |
| credentialID | Uint8Array | 否 | 否 | 证件号码。 |
| credentialType | CredentialType | 否 | 是 | 证件类型。 |

#### StyleOption

该接口定义了[FunctionalButton](FunctionalButton（Button组件）.md#section1753203873911)组件的样式信息。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.AtomicserviceComponent.UIComponent

**起始版本：**4.1.0(11)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| size | SizeType | 否 | 是 | 按钮尺寸类型。默认值：functionalButtonComponentManager.SizeType.DEFAULT，字体大小为：16fp。 |
| bgColor | ColorType | 否 | 是 | 按钮颜色类型。默认值：functionalButtonComponentManager.ColorType.DEFAULT，默认蓝底白字按钮样式。 |
| plain | boolean | 否 | 是 | 按钮是否镂空。“true”表示镂空。默认值：false，不镂空。 |
| disabled | boolean | 否 | 是 | 按钮是否禁用。“true”表示按钮禁用。默认值：false，不禁用Button。 |
| loading | boolean | 否 | 是 | 名称前是否带loading图标。“true”表示名称前带loading图标。 默认值：false，关闭loading动画。 |
| hoverClass | HoverClassType | 否 | 是 | 按钮按下去的样式。默认值：functionalButtonComponentManager.HoverClassType.HOVER_CLASS，开启点击效果。 |
| hoverStartTime | number | 否 | 是 | 按住后多久出现点击态，单位毫秒。 默认值：0 取值范围： [0, +∞) 说明：  设置为小于0的值时，按值为0处理。 |
| hoverStayTime | number | 否 | 是 | 手指松开后点击态保留时间，单位毫秒。 默认值：0 取值范围： [0, +∞) 说明：  设置为小于0的值时，按值为0处理。 |
| styleConfig | ButtonConfig | 否 | 是 | 按钮样式配置。 说明：  当styleConfig和StyleOption中定义的样式冲突时，最终以styleConfig的为准。 |

#### [FunctionalButton](FunctionalButton（Button组件）.md#section1753203873911)Params

该接口定义了[FunctionalButton](FunctionalButton（Button组件）.md#section1753203873911)组件的参数，定义Button功能以及样式等。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力****：**SystemCapability.AtomicserviceComponent.UIComponent

**起始版本：**4.1.0(11)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| openType | OpenType | 否 | 否 | 按钮功能场景类型。默认值：functionalButtonComponentManager.OpenType.GET_PHONE_NUMBER。 元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| label | ResourceStr | 否 | 否 | 按钮展示文字。默认值：空字符串。 元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| styleOption | StyleOption | 否 | 是 | 按钮样式。 元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。 说明：  - 在Button外设置的样式属性不生效，仅生效styleOption中设置的样式。  - 使用buttonModifier、textModifier、loadingProgressModifier设置按钮样式时，对应属性会被覆盖。 |
| appParam | AppParam | 否 | 是 | 需打开APP的信息。例如：{bundleName: "xxx", abilityName: "xxx"}。 bundleName：包名。 abilityName：Ability名称。 元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。 说明：  openType为“functionalButtonComponentManager.OpenType.LAUNCH_APP”时必填。 |
| realNameAuthenticationInfo(deprecated) | RealNameAuthenticationInfo | 否 | 是 | 实名信息校验按钮信息。 起始版本： 5.0.0(12) 元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。 说明：  从5.0.0(12)开始支持，从6.0.2(22)开始废弃，无替代接口。 |
| subscribeLiveViewParam | SubscribeLiveViewParam | 否 | 是 | 实况窗订阅按钮信息。 起始版本： 5.0.0(12) |
| permissionListParam | Array<Permissions> | 否 | 是 | 权限设置Button参数。 起始版本： 5.0.2(14) 元服务API： 从版本5.0.2(14)开始，该接口支持在元服务中使用。 说明：  需设置权限的权限名称列表，权限名称可参考应用权限列表。 |
| subSceneId | string | 否 | 是 | 子场景ID，在服务动态授权码场景时，该参数必填。参考服务动态场景模板，由开发者传入。 起始版本： 6.0.0(20) 元服务API： 从版本6.0.0(20)开始，该接口支持在元服务中使用。 |
| shareParam | ShareParam | 否 | 是 | 需要分享的Button参数。 起始版本： 6.0.0(20) 元服务API： 从版本6.0.0(20)开始，该接口支持在元服务中使用。 |
| buttonModifier | ButtonModifier | 否 | 是 | 设置Button的属性，如设置按钮的样式，颜色等。 起始版本： 5.1.0(18) 元服务API： 从版本5.1.0(18)开始，该接口支持在元服务中使用。 |
| textModifier | TextModifier | 否 | 是 | 设置文本的属性，如设置文本颜色，字体大小，字重等。 起始版本： 5.1.0(18) 元服务API： 从版本5.1.0(18)开始，该接口支持在元服务中使用。 |
| loadingProgressModifier | LoadingProgressModifier | 否 | 是 | 设置加载动效的属性，如设置加载动效的样式，颜色，定制内容区等。 起始版本： 5.1.0(18) 元服务API： 从版本5.1.0(18)开始，该接口支持在元服务中使用。 说明：  使用loadingProgressModifier时，使用styleOption设置loading为true时才能生效。 |

#### GetPhoneNumberResult

该接口定义了使用快速验证功能成功验证的响应。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.AtomicserviceComponent.UIComponent

**设备行为差异：**对于4.1.0(11)版本，该接口在Phone、Tablet、2in1中可正常调用，在其他设备类型中返回801错误码。对于5.1.0(18)及之后版本，该接口在Phone、Tablet、2in1、TV中可正常调用，在其他设备类型中返回801错误码。

**起始版本：**4.1.0(11)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| code | string | 否 | 是 | 账号用户的临时登录凭证（Authorization Code）。 说明：  可通过临时登录凭证获取真实手机号，临时登录凭证时效5分钟，具体操作可参考“服务端开发”章节。 |

#### GetRealtimePhoneNumberResult

该接口定义了使用实时验证功能成功验证的响应。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.AtomicserviceComponent.UIComponent

**设备行为差异：**对于4.1.0(11)版本，该接口在Phone、Tablet、2in1中可正常调用，在其他设备类型中返回801错误码。对于5.1.0(18)及之后版本，该接口在Phone、Tablet、2in1、TV中可正常调用，在其他设备类型中返回801错误码。

**起始版本：**4.1.0(11)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| code | string | 否 | 是 | 账号用户的临时登录凭证（Authorization Code）。 说明：  可通过临时登录凭证获取真实手机号，临时登录凭证时效5分钟，具体操作可参考“服务端开发”章节。 |

#### OpenSettingResult

该接口定义了使用打开授权设置页功能，成功跳转授权设置页后返回应用或结束设置应用，应用权限设置情况的响应。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.AtomicserviceComponent.UIComponent

**设备行为差异：**对于4.1.0(11)版本，该接口在Phone、Tablet、2in1中可正常调用，在其他设备类型中返回801错误码。对于5.1.0(18)及之后版本，该接口在Phone、Tablet、2in1、TV中可正常调用，在其他设备类型中返回801错误码。

**起始版本：**4.1.0(11)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| permissions | Map<string, boolean> | 否 | 是 | 权限字典表。 key为权限名称，value为权限是否开启，true表示开启权限，false表示关闭权限。 |

#### ChooseAvatarResult

该接口定义了使用选择头像功能成功选择的响应。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.AtomicserviceComponent.UIComponent

**设备行为差异：**该接口在Phone、Tablet、2in1中可正常调用，在其他设备类型中返回801错误码。

**起始版本：**4.1.0(11)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| avatarUri | string | 否 | 是 | 所选头像图片的地址。 说明：  返回的地址为裁剪之后的图片对应的地址。 |

#### AppParam

该接口定义了[FunctionalButton](FunctionalButton（Button组件）.md#section1753203873911)为打开APP功能时，通过该参数指定打开的应用对应的包名和Ability名称。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.AtomicserviceComponent.UIComponent

**设备行为差异：**对于4.1.0(11)版本，该接口在Phone、Tablet、2in1中可正常调用，在其他设备类型中返回801错误码。对于5.1.0(18)及之后版本，该接口在Phone、Tablet、2in1、TV中可正常调用，在其他设备类型中返回801错误码。

**起始版本：**4.1.0(11)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| bundleName | ResourceStr | 否 | 否 | 包名。 |
| abilityName | ResourceStr | 否 | 是 | Ability名称。默认值：EntryAbility。 |

#### ChooseAddressResult

该接口定义了[FunctionalButton](FunctionalButton（Button组件）.md#section1753203873911)为选择收货地址功能时，通过该参数指定选择收货地址对应的返回体。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.AtomicserviceComponent.UIComponent

**设备行为差异：**该接口在Phone、Tablet、2in1中可正常调用，在其他设备类型中返回801错误码。

**起始版本：**5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| userName | string | 否 | 否 | 用户名称。 |
| mobileNumber | string | 否 | 是 | 手机号码。 |
| telNumber | string | 否 | 是 | 固定电话号码。 |
| zipCode | string | 否 | 是 | 邮政编码。 |
| countryCode | string | 否 | 是 | 国家/地区代码。 |
| provinceName | string | 否 | 是 | 省份名称。 |
| cityName | string | 否 | 是 | 城市名称。 |
| districtName | string | 否 | 是 | 地区名称。 |
| streetName | string | 否 | 是 | 街道名称。 |
| detailedAddress | string | 否 | 否 | 详细地址。 |

#### ChooseInvoiceTitleResult

该接口定义了[FunctionalButton](FunctionalButton（Button组件）.md#section1753203873911)为选择发票抬头功能时，通过该参数指定选择发票抬头对应的返回体。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.AtomicserviceComponent.UIComponent

**设备行为差异：**该接口在Phone、Tablet、2in1中可正常调用，在其他设备类型中返回801错误码。

**起始版本：**5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | string | 否 | 否 | 发票类型，0-个人 1-企业。 |
| title | string | 否 | 否 | 发票抬头。 |
| taxNumber | string | 否 | 否 | 税号。 |
| companyAddress | string | 否 | 是 | 公司地址。 |
| telephone | string | 否 | 是 | 电话号码。 |
| bankName | string | 否 | 是 | 银行名称。 |
| bankAccount | string | 否 | 是 | 银行账户。 |

#### RealNameAuthenticationResult

该接口定义了[FunctionalButton](FunctionalButton（Button组件）.md#section1753203873911)为实名信息校验功能时，通过该参数指定实名信息校验对应的返回体。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.AtomicserviceComponent.UIComponent

设备行为差异： 该接口在Phone、Tablet中可正常调用，在2in1中返回1001500003错误码，在TV中返回801错误码。

**起始版本：**5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| authCode | string | 否 | 是 | 临时凭据，有效时间5分钟，并且只能使用一次。 |
| openID | string | 否 | 是 | OpenID是华为账号用户在不同类型的产品的身份ID，同一个用户，不同应用，OpenID值不同。 |

#### FaceAuthenticationResult

该接口定义了[FunctionalButton](FunctionalButton（Button组件）.md#section1753203873911)为人脸核身功能时，通过该参数指定人脸认证对应的返回体。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.AtomicserviceComponent.UIComponent

设备行为差异： 该接口在Phone、Tablet中可正常调用，在2in1中返回1001500003错误码，在TV中返回801错误码。

**起始版本：**5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| authCode | string | 否 | 是 | 临时凭据，有效时间5分钟，并且只能使用一次。 |
| openID | string | 否 | 是 | OpenID是华为账号用户在不同类型的产品的身份ID，同一个用户，不同应用，OpenID值不同。 |

#### FaceVerificationResult

该接口定义了[FunctionalButton](FunctionalButton（Button组件）.md#section1753203873911)为人脸核身功能时，通过该参数指定人脸核身对应的返回体。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.AtomicserviceComponent.UIComponent

设备行为差异： 该接口在Phone、Tablet中可正常调用，在2in1中返回1001500003错误码，在TV中返回801错误码。

**起始版本：**5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| facialRecognitionVerificationToken | string | 否 | 是 | 验证成功后返回的token。 |
| state | string | 否 | 是 | 响应体中返回的state，字符包含0-9、a-z、A-Z、英文点号、英文冒号、斜杆、下划线等，长度限制255，校验规则^[0-9a-zA-Z:/.-_]{1,255}$。与请求体中传入的state比较，校验是否是当前请求，防止跨站攻击。 |

#### ChooseLocationResult

该接口定义了[FunctionalButton](FunctionalButton（Button组件）.md#section1753203873911)为地图选点功能时，通过该参数指定地图选点对应的返回体。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.AtomicserviceComponent.UIComponent

**设备行为差异：**对于5.0.0(12)版本，该接口在Phone、Tablet中可正常调用，在其他设备类型中返回801错误码。对于5.0.1(13)及之后版本，该接口在Phone、Tablet、2in1中可正常调用，在其他设备类型中返回801错误码。

**起始版本：**5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| name | string | 否 | 否 | 位置名称。 |
| longitude | number | 否 | 否 | 经度。 |
| latitude | number | 否 | 否 | 纬度。 |
| address | string | 否 | 否 | 地址。 |

#### SubscribeLiveViewParam

该接口定义了[FunctionalButton](FunctionalButton（Button组件）.md#section1753203873911)组件为实况窗订阅功能时，通过该参数指定实况窗订阅对应的订阅事件和计时器。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力****：**SystemCapability.AtomicserviceComponent.UIComponent

**设备行为差异：**该接口在Phone、Tablet中可正常调用，在其他设备类型中返回801错误码。

**起始版本：**5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| event | string | 否 | 否 | 订阅事件。 固定值：SUBSCRIBE_TIMER。 |
| alertTime | number | 否 | 否 | 计时器提醒时间，毫秒级时间戳。 说明：  1. 参数不能为空。  2. 0<=startTime-alertTime。  3. startTime和alertTime晚于当前时间。  4. startTime-alertTime <= 3600000(可在push侧配置)。 |
| startTime | number | 否 | 否 | 计时器开始时间，毫秒级时间戳。 说明：  1. 参数不能为空。  2. 0<=startTime-alertTime。  3. startTime和alertTime晚于当前时间。  4. startTime-alertTime <= 3600000(可在push侧配置)。 |

#### SubscribeLiveViewResult

该接口定义了[FunctionalButton](FunctionalButton（Button组件）.md#section1753203873911)组件为实况窗订阅功能时，通过该参数指定实况窗订阅对应的返回体。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力****：**SystemCapability.AtomicserviceComponent.UIComponent

**设备行为差异：**该接口在Phone、Tablet中可正常调用，在其他设备类型中返回801错误码。

**起始版本：**5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| subscribeId | string | 否 | 否 | 订阅事件ID。 |

#### PermissionSettingResult

该接口定义了[FunctionalButton](FunctionalButton（Button组件）.md#section1753203873911)组件为权限设置功能时，通过该参数指定权限设置的返回体，用于UIAbility/UIExtensionAbility二次拉起权限设置弹框。

在调用此接口前，应用需要先调用[requestPermissionsFromUser](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-abilityaccessctrl#requestpermissionsfromuser9)，如果用户在首次弹窗授权时已授权，调用当前接口将无法拉起弹窗。

仅支持UIAbility/UIExtensionAbility。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.2(14)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.AtomicserviceComponent.UIComponent

**设备行为差异：**对于5.0.2(14)版本，该接口在Phone、Tablet、2in1中可正常调用，在其他设备类型中返回801错误码。对于5.1.0(18)及之后版本，该接口在Phone、Tablet、2in1、TV中可正常调用，在其他设备类型中返回801错误码。

**起始版本：**5.0.2(14)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| permissionResult | Array<abilityAccessCtrl.GrantStatus> | 否 | 否 | 权限设置结果。 |

#### RequestSubscribeMessageResult

该接口定义请求订阅消息的返回体。

仅提供给元服务使用。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.AtomicserviceComponent.UIComponent

**设备行为差异：**该接口在Phone、Tablet中可正常调用，在其他设备类型中返回801错误码。

**起始版本：**6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| code | string | 否 | 否 | 服务动态授权码 。用于校验服务是否合法，服务动态等 |

#### ShareParam

该接口定义分享的参数。

仅提供给已发布的元服务使用。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.AtomicserviceComponent.UIComponent

**设备行为差异：**该接口在Phone、Tablet中可正常调用，在其他设备类型中返回801错误码。

**起始版本：**6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| description | string | 否 | 是 | 元服务描述，支持开发者传入，默认是元服务描述。 |
| previewUri | string | 否 | 是 | 元服务预览图，由开发者传入图片，否则返回默认元服务icon图标；本地文件路径、代码包文件路径或者网络图片路径。 |

#### GetPhoneNumberAndRiskLevelResult

该接口定义获取手机号和风险等级的返回体。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本6.0.2(22)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.AtomicserviceComponent.UIComponent

**起始版本：**6.0.2(22)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| code | string | 否 | 是 | 手机号和风险等级授权码。成功获取授权码时返回。 |
| errCode | number | 否 | 是 | 错误码。获取授权码失败时返回。 |
| errMsg | string | 否 | 是 | 错误信息。获取授权码失败时返回。 |

#### 事件

不支持通用事件，仅支持以下事件：

#### [FunctionalButton](FunctionalButton（Button组件）.md#section1753203873911)Controller

[FunctionalButton](FunctionalButton（Button组件）.md#section1753203873911)组件控制器，用来回调组件内部的点击事件。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.AtomicserviceComponent.UIComponent

**起始版本：**4.1.0(11)

#### onGetPhoneNumber

onGetPhoneNumber(callback: AsyncCallback<GetPhoneNumberResult>): [FunctionalButton](FunctionalButton（Button组件）.md#section1753203873911)Controller

注册[FunctionalButton](FunctionalButton（Button组件）.md#section1753203873911)组件为快速验证手机号的点击事件，使用callback异步回调。

该接口功能依赖Account Kit，参见[createAuthorizationWithHuaweiIDRequest](authentication (华为账号应用统一认证服务).md#ZH-CN_TOPIC_0000002553202245__createauthorizationwithhuaweiidrequest)。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.AtomicserviceComponent.UIComponent

**设备行为差异：**对于4.1.0(11)版本，该接口在Phone、Tablet、2in1中可正常调用，在其他设备类型中返回801错误码。对于5.1.0(18)及之后版本，该接口在Phone、Tablet、2in1、TV中可正常调用，在其他设备类型中返回801错误码。

**起始版本：**4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<GetPhoneNumberResult> | 是 | 回调函数。当获取电话号码成功，err为undefined，data为获取到的账号用户的临时登录凭证（Authorization Code）；否则为错误对象。 说明：  可通过临时登录凭证获取真实手机号，临时登录凭证时效5分钟，具体操作可参考“服务端开发”章节。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [FunctionalButton](FunctionalButton（Button组件）.md#section1753203873911)Controller | FunctionalButton组件控制器。 |

**示例：**

```ets
import { FunctionalButton, functionalButtonComponentManager } from '@kit.ScenarioFusionKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        // 声明FunctionalButton。
        FunctionalButton({
          params: {
            // OpenType.GET_PHONE_NUMBER表示该按钮用于快速验证手机号码。
            openType: functionalButtonComponentManager.OpenType.GET_PHONE_NUMBER,
            label: '快速验证手机号',
            // 调整按钮样式。
            styleOption: {
              styleConfig: new functionalButtonComponentManager.ButtonConfig()
                .fontSize(20)
            },
          // 当OpenType为GET_PHONE_NUMBER时，回调必须为onGetPhoneNumber。
          controller: new functionalButtonComponentManager.FunctionalButtonController()
            .onGetPhoneNumber((err, data) => {
              if (err) {
                // 错误日志处理。
                hilog.error(0x0000, "testTag", "error: %{public}d %{public}s", err.code, err.message);
                return;
              }
              // 成功日志处理。
              hilog.info(0x0000, "testTag", "succeeded in authenticating");
              // 获取授权码。
              let authorizationCode = data.code;
            })
      }.width('100%')
    }.height('100%')
}
```

#### onGetRealtimePhoneNumber

onGetRealtimePhoneNumber(callback: AsyncCallback<GetRealtimePhoneNumberResult>): [FunctionalButton](FunctionalButton（Button组件）.md#section1753203873911)Controller

注册[FunctionalButton](FunctionalButton（Button组件）.md#section1753203873911)组件为实时验证手机号的点击事件，使用callback异步回调。

该接口功能依赖Account Kit，参见[createAuthorizationWithHuaweiIDRequest](authentication (华为账号应用统一认证服务).md#ZH-CN_TOPIC_0000002553202245__createauthorizationwithhuaweiidrequest)。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.AtomicserviceComponent.UIComponent

**设备行为差异：**对于4.1.0(11)版本，该接口在Phone、Tablet、2in1中可正常调用，在其他设备类型中返回801错误码。对于5.1.0(18)及之后版本，该接口在Phone、Tablet、2in1、TV中可正常调用，在其他设备类型中返回801错误码。

**起始版本：**4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<GetRealtimePhoneNumberResult> | 是 | 回调函数。当获取实时电话号码成功，err为undefined，data为获取到的账号用户的临时登录凭证（Authorization Code）；否则为错误对象。 说明：  可通过临时登录凭证获取真实手机号，临时登录凭证时效5分钟，具体操作可参考“服务端开发”章节。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [FunctionalButton](FunctionalButton（Button组件）.md#section1753203873911)Controller | FunctionalButton组件控制器。 |

**示例：**

```ets
import {FunctionalButton, functionalButtonComponentManager} from '@kit.ScenarioFusionKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        // 声明FunctionalButton。
        FunctionalButton({
          params: {
            // OpenType.GET_REALTIME_PHONENUMBER表示该按钮用于实时验证手机号码。
            openType: functionalButtonComponentManager.OpenType.GET_REALTIME_PHONENUMBER,
            label: '实时验证手机号',
            // 调整按钮样式。
            styleOption: {
              styleConfig: new functionalButtonComponentManager.ButtonConfig()
                .fontSize(20)
            },
          // 当OpenType为GET_REALTIME_PHONENUMBER时，回调必须为onGetRealtimePhoneNumber。
          controller: new functionalButtonComponentManager.FunctionalButtonController()
            .onGetRealtimePhoneNumber((err, data) => {
              if (err) {
                // 错误日志处理。
                hilog.error(0x0000, "testTag", "error: %{public}d %{public}s", err.code, err.message);
                return;
              }
              // 成功日志处理。
              hilog.info(0x0000, "testTag", "succeeded in authenticating");
              // 获取授权码。
              let authorizationCode = data.code;
            })
      }
      .width('100%')
    }
    .height('100%')
}
```

#### onLaunchApp

onLaunchApp(callback: AsyncCallback<void>): [FunctionalButton](FunctionalButton（Button组件）.md#section1753203873911)Controller

注册[FunctionalButton](FunctionalButton（Button组件）.md#section1753203873911)组件为打开APP的点击事件，使用callback异步回调。

该接口功能依赖Ability Kit，参见[startAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext#startability)。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.AtomicserviceComponent.UIComponent

**设备行为差异：**对于4.1.0(11)版本，该接口在Phone、Tablet、2in1中可正常调用，在其他设备类型中返回801错误码。对于5.1.0(18)及之后版本，该接口在Phone、Tablet、2in1、TV中可正常调用，在其他设备类型中返回801错误码。

**起始版本：**4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当打开APP完成，err为undefined，否则返回错误对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [FunctionalButton](FunctionalButton（Button组件）.md#section1753203873911)Controller | FunctionalButton组件控制器。 |

**示例：**

```ets
import { FunctionalButton, functionalButtonComponentManager } from '@kit.ScenarioFusionKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        // 声明FunctionalButton。
        FunctionalButton({
          params: {
            // OpenType.LAUNCH_APP表示该按钮用于启动应用。
            openType: functionalButtonComponentManager.OpenType.LAUNCH_APP,
            label: '打开APP',
            // 当OpenType为functionButtonComponentManager.OpenType.LAUNCH_APP时，appParam为必填项。
            appParam: {
              bundleName: "xxx",
              abilityName: "xxx"
            },
            // 调整按钮样式。
            styleOption: {
              styleConfig: new functionalButtonComponentManager.ButtonConfig()
                .fontSize(20)
            },
          // 当OpenType设置为LAUNCH_APP时，回调函数必须是onLaunchApp。
          controller: new functionalButtonComponentManager.FunctionalButtonController().onLaunchApp((err) => {
            if (err) {
              // 错误日志处理。
              hilog.error(0x0000, "testTag", "error: %{public}d %{public}s", err.code, err.message);
              return;
            }
            // 处理成功。成功时不会返回任何值。
            hilog.info(0x0000, "testTag", "succeeded in launching app");
          })
      }.width('100%')
    }.height('100%')
}
```

“bundleName”为包名，“abilityName”为Ability名称。

#### onOpenSetting

onOpenSetting(callback: AsyncCallback<OpenSettingResult>): [FunctionalButton](FunctionalButton（Button组件）.md#section1753203873911)Controller

注册[FunctionalButton](FunctionalButton（Button组件）.md#section1753203873911)组件为打开授权设置页的点击事件，使用callback异步回调。

该接口功能依赖Ability Kit，参见[startAbilityForResult](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext#startabilityforresult)。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.AtomicserviceComponent.UIComponent

**设备行为差异：**对于4.1.0(11)版本，该接口在Phone、Tablet、2in1中可正常调用，在其他设备类型中返回801错误码。对于5.1.0(18)及之后版本，该接口在Phone、Tablet、2in1、TV中可正常调用，在其他设备类型中返回801错误码。

**起始版本：**4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<OpenSettingResult> | 是 | 回调函数。当打开授权设置页成功，err为undefined，data为打开设置成功时返回的响应；否则为错误对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [FunctionalButton](FunctionalButton（Button组件）.md#section1753203873911)Controller | FunctionalButton组件控制器。 |

**示例：**

```ets
import { FunctionalButton, functionalButtonComponentManager } from '@kit.ScenarioFusionKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        // 声明FunctionalButton。
        FunctionalButton({
          params: {
            // OpenType.OPEN_SETTING表示该按钮用于打开授权设置页面。
            openType: functionalButtonComponentManager.OpenType.OPEN_SETTING,
            label: '打开授权设置页',
            // 调整按钮样式。
            styleOption: {
              styleConfig: new functionalButtonComponentManager.ButtonConfig()
                .fontSize(20)
            },
          // 当OpenType为OPEN_SETTING时，回调必须为onOpenSetting。
          controller: new functionalButtonComponentManager.FunctionalButtonController().onOpenSetting((err, data) => {
            if (err) {
              // 错误日志处理。
              hilog.error(0x0000, "testTag", "error: %{public}d %{public}s", err.code, err.message);
              return;
            }
            // 成功处理，当应用程序进程停止时触发。
            hilog.info(0x0000, "testTag", "succeeded in opening setting");
            data.permissions!.forEach((value, key) => {
              hilog.info(0x0000, "testTag", "key: %{public}s value: %{public}s", String(key), value);
            })
      }.width('100%')
    }.height('100%')
}
```

#### onChooseAvatar

onChooseAvatar(callback: AsyncCallback<ChooseAvatarResult>): [FunctionalButton](FunctionalButton（Button组件）.md#section1753203873911)Controller

注册[FunctionalButton](FunctionalButton（Button组件）.md#section1753203873911)组件为选择头像的点击事件，使用callback异步回调。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.AtomicserviceComponent.UIComponent

**设备行为差异：**该接口在Phone、Tablet、2in1中可正常调用，在其他设备类型中返回801错误码。

**起始版本：**4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<ChooseAvatarResult> | 是 | 回调函数。当选择头像调用成功，err为undefined，data为选择头像成功时返回的所选头像图片的地址；否则为错误对象。 说明：  返回的地址为裁剪之后的图片对应的地址。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [FunctionalButton](FunctionalButton（Button组件）.md#section1753203873911)Controller | FunctionalButton组件控制器。 |

**示例：**

```ets
import { FunctionalButton, functionalButtonComponentManager } from '@kit.ScenarioFusionKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

@Entry
@Component
struct Index {
  // 将account.png文件添加到/resources/base/media/目录中。否则，将显示错误信息，提示找不到该文件。
  @State url: ResourceStr = $r('app.media.account');

  build() {
    Column() {
      // 声明FunctionalButton。
      FunctionalButton({
        params: {
          // OpenType.CHOOSE_AVATAR表示该按钮用于选择头像。
          openType: functionalButtonComponentManager.OpenType.CHOOSE_AVATAR,
          label: '',
          // 调整按钮样式。
          styleOption: {
            styleConfig: new functionalButtonComponentManager.ButtonConfig()
              .type(ButtonType.Normal)
              .backgroundImage(this.url)
              .backgroundImageSize(ImageSize.Cover)
              .width(80)
              .height(80)
              .backgroundColor('#E5E5E5')
          },
        // 当OpenType设置为CHOOSE_AVATAR时，回调函数必须是onChooseAvatar。
        controller: new functionalButtonComponentManager.FunctionalButtonController().onChooseAvatar((err, data) => {
          if (err) {
            // 错误日志处理。
            hilog.error(0x0000, "testTag", "error: %{public}d %{public}s", err.code, err.message);
            return;
          }
          // 成功日志处理。
          hilog.info(0x0000, "testTag", "succeeded in choosing avatar");
          this.url = data.avatarUri!;
        })
    }
    .padding({ top: 200 })
    .height('100%')
    .width('100%')
  }
```

#### onChooseAddress

onChooseAddress(callback: AsyncCallback<ChooseAddressResult>): [FunctionalButton](FunctionalButton（Button组件）.md#section1753203873911)Controller

注册[FunctionalButton](FunctionalButton（Button组件）.md#section1753203873911)组件为选择收货地址的点击事件，使用callback异步回调。

该接口功能依赖Account Kit，参见[chooseAddress](shippingAddress (华为账号收货地址管理服务).md#ZH-CN_TOPIC_0000002553362207__chooseaddress)。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.AtomicserviceComponent.UIComponent

**设备行为差异：**该接口在Phone、Tablet、2in1中可正常调用，在其他设备类型中返回801错误码。

**起始版本：**5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<ChooseAddressResult> | 是 | 回调函数。当选择收货地址点击成功，err为undefined，data为选择收货地址的返回结果；否则为错误对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [FunctionalButton](FunctionalButton（Button组件）.md#section1753203873911)Controller | FunctionalButton组件控制器。 |

**示例：**

```ets
import { FunctionalButton, functionalButtonComponentManager } from '@kit.ScenarioFusionKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        // 声明FunctionalButton。
        FunctionalButton({
          params: {
            // OpenType.CHOOSE_ADDRESS表示该按钮用于选择收货地址。
            openType: functionalButtonComponentManager.OpenType.CHOOSE_ADDRESS,
            label: '选择收货地址',
            // 调整按钮样式。
            styleOption: {
              bgColor:functionalButtonComponentManager.ColorType.DEFAULT,
              size: functionalButtonComponentManager.SizeType.DEFAULT,
              plain: false,
              disabled:false,
              loading: false,
              hoverClass: functionalButtonComponentManager.HoverClassType.HOVER_CLASS,
              hoverStartTime: 0,
              hoverStayTime: 0,
              styleConfig: new functionalButtonComponentManager.ButtonConfig()
                .fontSize(20)
            },
          // 当OpenType设置为CHOOSE_ADDRESS时，回调必须为onChooseAddress。
          controller: new functionalButtonComponentManager.FunctionalButtonController()
            .onChooseAddress((err, data) => {
              if (err) {
                // 错误日志处理。
                hilog.error(0x0000, "testTag", "error: %{public}d %{public}s", err.code, err.message);
                return;
              }
              // 成功日志处理。
              hilog.info(0x0000, "testTag", "succeeded in choosing address");
              // 获取地址信息。
              let userName: string = data.userName;
              let mobileNumber: string = data.mobileNumber as string;
              let countryCode: string = data.countryCode as string;
              let provinceName: string = data.provinceName as string;
              let cityName: string = data.cityName as string;
              let districtName: string = data.districtName as string;
              let streetName: string = data.streetName as string;
              let detailedAddress: string = data.detailedAddress;
            })
      }.width('100%')
    }.height('100%')
}
```

#### onChooseInvoiceTitle

onChooseInvoiceTitle(callback: AsyncCallback<ChooseInvoiceTitleResult>): [FunctionalButton](FunctionalButton（Button组件）.md#section1753203873911)Controller

注册[FunctionalButton](FunctionalButton（Button组件）.md#section1753203873911)组件为选择发票抬头的点击事件，使用callback异步回调。

该接口功能依赖Account Kit，参见[selectInvoiceTitle](invoiceAssistant (华为账号发票助手服务).md#ZH-CN_TOPIC_0000002553202247__selectinvoicetitle)。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.AtomicserviceComponent.UIComponent

**设备行为差异：**该接口在Phone、Tablet、2in1中可正常调用，在其他设备类型中返回801错误码。

**起始版本：**5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<ChooseInvoiceTitleResult> | 是 | 回调函数。当选择发票抬头点击成功，err为undefined，data为选择发票抬头的返回结果；否则为错误对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [FunctionalButton](FunctionalButton（Button组件）.md#section1753203873911)Controller | FunctionalButton组件控制器。 |

**示例：**

```ets
import { FunctionalButton, functionalButtonComponentManager } from '@kit.ScenarioFusionKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        // 声明FunctionalButton。
        FunctionalButton({
          params: {
            // OpenType.CHOOSE_INVOICE_TITLE表示该按钮用于选择发票标题。
            openType: functionalButtonComponentManager.OpenType.CHOOSE_INVOICE_TITLE,
            label: '选择发票抬头',
            // 调整按钮样式。
            styleOption: {
              bgColor:functionalButtonComponentManager.ColorType.DEFAULT,
              size: functionalButtonComponentManager.SizeType.DEFAULT,
              plain: false,
              disabled:false,
              loading: false,
              hoverClass: functionalButtonComponentManager.HoverClassType.HOVER_CLASS,
              hoverStartTime: 0,
              hoverStayTime: 0,
              styleConfig: new functionalButtonComponentManager.ButtonConfig()
                .fontSize(20)
            },
          // 当OpenType为CHOOSE_INVOICE_TITLE时，回调必须为onChooseInvoiceTitle。
          controller: new functionalButtonComponentManager.FunctionalButtonController()
            .onChooseInvoiceTitle((err, data) => {
              if (err) {
                // 错误日志处理。
                hilog.error(0x0000, "testTag", "error: %{public}d %{public}s", err.code, err.message);
                return;
              }
              // 成功日志处理。
              hilog.info(0x0000, "testTag", "succeeded in obtaining invoice title");
              // 获取发票信息。
              let type: string = data.type;
              let title: string = data.title;
              let taxNumber: string = data.taxNumber;
              let companyAddress: string | undefined = data.companyAddress;
              let telephone: string | undefined = data.telephone;
              let bankName: string | undefined = data.bankName;
              let bankAccount: string | undefined = data.bankAccount;
            })
      }.width('100%')
    }.height('100%')
}
```

#### onRealNameAuthentication

onRealNameAuthentication(callback: AsyncCallback<RealNameAuthenticationResult>): [FunctionalButton](FunctionalButton（Button组件）.md#section1753203873911)Controller

注册[FunctionalButton](FunctionalButton（Button组件）.md#section1753203873911)组件为实名信息校验的点击事件，使用callback异步回调。

该接口功能依赖Account Kit，参见[createAuthorizationWithHuaweiIDRequest](authentication (华为账号应用统一认证服务).md#ZH-CN_TOPIC_0000002553202245__createauthorizationwithhuaweiidrequest)，[AuthenticationController](authentication (华为账号应用统一认证服务).md#ZH-CN_TOPIC_0000002553202245__authenticationcontroller)，[executeRequest](authentication (华为账号应用统一认证服务).md#ZH-CN_TOPIC_0000002553202245__executerequest)。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.AtomicserviceComponent.UIComponent

设备行为差异： 该接口在Phone、Tablet中可正常调用，在2in1中返回1001500003错误码，在TV中返回801错误码。

**起始版本：**5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<RealNameAuthenticationResult> | 是 | 回调函数。当实名信息校验成功，err为undefined，data为获取到的实名信息校验鉴权对应的返回体：authCode、openID；否则为错误对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [FunctionalButton](FunctionalButton（Button组件）.md#section1753203873911)Controller | FunctionalButton组件控制器。 |

**示例：**

```ets
import { FunctionalButton, functionalButtonComponentManager } from '@kit.ScenarioFusionKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { http } from '@kit.NetworkKit';
import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';

interface Result {
  state?: number;
  realNameLevel?: number;
  verifyResult?: number;
  verifyToken?: string;
}

@Entry
@Component
struct SecondPage {

  obtainRealNameDataInfo(authCode: string, sceneID:number, openID: string, realName: string, idNo: string,
    callback: AsyncCallback<Result>) {
    // 每个httpRequest对应一个HTTP请求任务，且不可重复使用。
    let httpRequest = http.createHttp();
    // 监听HTTP响应头事件，该事件比HTTP请求的响应返回得更早。是否监听HTTP响应头事件由您决定。
    httpRequest.on('headersReceive', (header) => {
      hilog.info(0x0000, "testTag", "header: %{public}s", header as string);
    });
    httpRequest.request(
      // 请自行在extraData中自定义EXAMPLE_URL。是否向URL添加参数由您决定。
      "EXAMPLE_URL",
      {
        method: http.RequestMethod.POST,
        // 您可以根据服务需求添加头部字段。
        header: {
          'Content-Type': 'application/json'
        },
        // 使用此字段在POST请求中传递信息。
        extraData: {
          "authCode": authCode,
          "sceneID": sceneID,
          "openID": openID,
          "realname": realName,
          "idNo": idNo,
        },
        expectDataType: http.HttpDataType.STRING,
        usingCache: true,
        priority: 1,
        connectTimeout: 60000,
        readTimeout: 60000,
        usingProtocol: http.HttpProtocol.HTTP1_1,
      }, (err, data) => {
      if (!err) {
        let res: Result = JSON.parse(data.result as string);
        callback(undefined, res);
      } else {
        let error: BusinessError = {code: err.code, message: err.message, name: ''};
        callback(error, undefined);
        // 取消订阅HTTP响应头事件。
        httpRequest.off('headersReceive');
        // 在httpRequest完成后调用destroy()方法以释放资源。
        httpRequest.destroy();
      }
    })
  }

  build() {
    Row() {
      Column() {
        FunctionalButton({
          params: {
            // OpenType.REAL_NAME_AUTHENTICATION表示该按钮用于实名信息校验。
            openType: functionalButtonComponentManager.OpenType.REAL_NAME_AUTHENTICATION,
            label: '实名信息校验',
            // 调整按钮样式。
            styleOption: {
              styleConfig: new functionalButtonComponentManager.ButtonConfig()
                .fontSize(20)
            },
          // 当OpenType设置为REAL_NAME_AUTHENTICATION时，回调必须为onRealNameAuthentication。
          controller: new functionalButtonComponentManager.FunctionalButtonController()
            .onRealNameAuthentication((err, data) => {
              if (err) {
                // 错误日志处理。
                hilog.error(0x0000, "testTag", "error: %{public}d %{public}s", err.code, err.message);
                return;
              }
              // 成功日志处理。
              hilog.info(0x0000, "testTag", "succeeded in authenticating");
              // 获取授权码。
              let authCode: string = data.authCode as string;
              let openID: string = data.openID as string;
              // sceneid 表示场景ID。选项包括：0（实名验证）、1（人脸验证，验证姓名、证件类型、证件号码和人脸）和2（人脸验证，仅验证人脸）。
              this.obtainRealNameDataInfo(authCode, 0, openID, 'name', 'idNo', (err, data) => {
                if (err) {
                  hilog.error(0x0000, "testTag", "error: %{public}d %{public}s", err.code, err.message);
                  return;
                }
                let state = data.state;
                let realNameLevel = data.realNameLevel;
                let verifyResult = data.verifyResult;
                let verifyToken = data.verifyToken;
                hilog.info(0x0000, "testTag", "succeeded in verifying");
              })
      }
      .width('100%')
    }
    .height('100%')
  }
```

#### onFaceAuthentication

onFaceAuthentication(callback: AsyncCallback<FaceAuthenticationResult>): [FunctionalButton](FunctionalButton（Button组件）.md#section1753203873911)Controller

注册[FunctionalButton](FunctionalButton（Button组件）.md#section1753203873911)组件为人脸核身的点击事件，使用callback异步回调。

该接口功能依赖Account Kit，参见[createAuthorizationWithHuaweiIDRequest](authentication (华为账号应用统一认证服务).md#ZH-CN_TOPIC_0000002553202245__createauthorizationwithhuaweiidrequest)，[AuthenticationController](authentication (华为账号应用统一认证服务).md#ZH-CN_TOPIC_0000002553202245__authenticationcontroller)，[executeRequest](authentication (华为账号应用统一认证服务).md#ZH-CN_TOPIC_0000002553202245__executerequest)。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.AtomicserviceComponent.UIComponent

设备行为差异： 该接口在Phone、Tablet中可正常调用，在2in1中返回1001500003错误码，在TV中返回801错误码。

**起始版本：**5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<FaceAuthenticationResult> | 是 | 回调函数。当人脸认证成功，err为undefined，data为获取到的人脸认证对应的返回体：authCode、openID；否则为错误对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [FunctionalButton](FunctionalButton（Button组件）.md#section1753203873911)Controller | FunctionalButton组件控制器。 |

**示例：**

```ets
import { FunctionalButton, functionalButtonComponentManager } from '@kit.ScenarioFusionKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { http } from '@kit.NetworkKit';
import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';

interface Result {
  state?: number;
  realNameLevel?: number;
  verifyResult?: number;
  verifyToken?: string;
}

@Entry
@Component
struct SecondPage {
  obtainFaceVerifyDataInfo(authCode: string, sceneID: number, openID: string, realName: string, idNo: string,
    callback: AsyncCallback<Result>) {
    // 每个httpRequest对应一个HTTP请求任务，且不可重复使用。
    let httpRequest = http.createHttp();
    // 监听HTTP响应头事件，该事件比HTTP请求的响应返回得更早。是否监听HTTP响应头事件由您决定。
    httpRequest.on('headersReceive', (header) => {
      hilog.info(0x0000, "testTag", "header: %{public}s", header as string);
    });
    httpRequest.request(
      // 请自行在extraData中自定义EXAMPLE_URL。是否向URL添加参数由您决定。
      "EXAMPLE_URL",
      {
        method: http.RequestMethod.POST,
        // 您可以根据服务需求添加头部字段。
        header: {
          'Content-Type': 'application/json'
        },
        // 使用此字段在POST请求中传递信息。
        extraData: {
          "authCode": authCode,
          "sceneID": sceneID,
          "openID": openID,
          "realname": realName,
          "idNo": idNo,
        },
        expectDataType: http.HttpDataType.STRING,
        usingCache: true,
        priority: 1,
        connectTimeout: 60000,
        readTimeout: 60000,
        usingProtocol: http.HttpProtocol.HTTP1_1,
      }, (err, data) => {
      if (!err) {
        let res: Result = JSON.parse(data.result as string);
        callback(undefined, res);
      } else {
        let error: BusinessError = { code: err.code, message: err.message, name: '' };
        callback(error, undefined);
        // 取消订阅HTTP响应头事件。
        httpRequest.off('headersReceive');
        // 在httpRequest完成后调用destroy()方法以释放资源。
        httpRequest.destroy();
      }
    })
  }

  build() {
    Row() {
      Column() {
        FunctionalButton({
          params: {
            // OpenType.FACE_AUTHENTICATION表示该按钮用于人脸身份验证。
            openType: functionalButtonComponentManager.OpenType.FACE_AUTHENTICATION,
            label: '人脸核身',
            // 调整按钮样式。
            styleOption: {
              styleConfig: new functionalButtonComponentManager.ButtonConfig()
                .fontSize(20)
            },
          // 当OpenType为FACE_AUTHENTICATION时，回调必须为onFaceAuthentication。
          controller: new functionalButtonComponentManager.FunctionalButtonController()
            .onFaceAuthentication((err, data) => {
              if (err) {
                // 错误日志处理。
                hilog.error(0x0000, "testTag", "error: %{public}d %{public}s", err.code, err.message);
                return;
              }
              // 成功日志处理。
              hilog.info(0x0000, "testTag", "succeeded in authenticating");
              // 获取授权码。
              let authCode: string = data.authCode as string;
              let openID: string = data.openID as string;
              hilog.info(0x0000, "testTag", "succeeded in authCode");
              // sceneid 表示场景ID。选项包括：0（实名验证）、1（人脸验证，验证姓名、证件类型、证件号码和人脸）和2（人脸验证，仅验证人脸）。
              this.obtainFaceVerifyDataInfo(authCode, 2, openID, "", "", (err, data) => {
                if (err) {
                  hilog.error(0x0000, "testTag", "error: %{public}d %{public}s", err.code, err.message);
                  return;
                }
                let verifyToken: string = data.verifyToken as string;
                new functionalButtonComponentManager.FunctionalButtonController().onFaceVerification(verifyToken,
                  (error, data) => {
                    if (error) {
                      // 错误日志处理。
                      hilog.error(0x0000, "testTag", "error: %{public}d %{public}s", error.code, error.message);
                      return;
                    }
                    let facialRecognitionVerificationToken = data.facialRecognitionVerificationToken;
                    let state = data.state;
                    hilog.info(0x0000, 'testTag', 'auth result success');
                  });
              })
      }
      .width('100%')
    }
    .height('100%')
  }
```

#### onFaceVerification

onFaceVerification(verifyToken: string, callback: AsyncCallback<FaceVerificationResult>): void

注册[FunctionalButton](FunctionalButton（Button组件）.md#section1753203873911)组件为人脸验证的点击事件，使用callback异步回调。

该接口功能依赖Account Kit，参见[createAuthorizationWithHuaweiIDRequest](authentication (华为账号应用统一认证服务).md#ZH-CN_TOPIC_0000002553202245__createauthorizationwithhuaweiidrequest)，[AuthenticationController](authentication (华为账号应用统一认证服务).md#ZH-CN_TOPIC_0000002553202245__authenticationcontroller)，[executeRequest](authentication (华为账号应用统一认证服务).md#ZH-CN_TOPIC_0000002553202245__executerequest)。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.AtomicserviceComponent.UIComponent

设备行为差异： 该接口在Phone、Tablet中可正常调用，在2in1中返回1001500003错误码，在TV中返回801错误码。

**起始版本：**5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| verifyToken | string | 是 | 验证成功的idToken，三方应用拉起华为账号客户端人脸验证页面时传入此Token，供华为账号客户端校验验证结果，参见FacialRecognitionVerificationRequest。 |
| callback | AsyncCallback<FaceVerificationResult> | 是 | 回调函数。当人脸验证点击成功，err为undefined，data为人脸验证的返回结果；否则为错误对象。 |

**示例：**

```ets
import { FunctionalButton, functionalButtonComponentManager } from '@kit.ScenarioFusionKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { http } from '@kit.NetworkKit';
import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';

interface Result {
  state?: number;
  realNameLevel?: number;
  verifyResult?: number;
  verifyToken?: string;
}

@Entry
@Component
struct SecondPage {
  obtainFaceVerifyDataInfo(authCode: string, sceneID: number, openID: string, realName: string, idNo: string,
    callback: AsyncCallback<Result>) {
    // 每个httpRequest对应一个HTTP请求任务，且不可重复使用。
    let httpRequest = http.createHttp();
    // 监听HTTP响应头事件，该事件比HTTP请求的响应返回得更早。是否监听HTTP响应头事件由您决定。
    httpRequest.on('headersReceive', (header) => {
      hilog.info(0x0000, "testTag", "header: %{public}s", header as string);
    });
    httpRequest.request(
      // 请自行在extraData中自定义EXAMPLE_URL。是否向URL添加参数由您决定。
      "EXAMPLE_URL",
      {
        method: http.RequestMethod.POST,
        // 您可以根据服务需求添加头部字段。
        header: {
          'Content-Type': 'application/json'
        },
        // 使用此字段在POST请求中传递信息。
        extraData: {
          "authCode": authCode,
          "sceneID": sceneID,
          "openID": openID,
          "realname": realName,
          "idNo": idNo,
        },
        expectDataType: http.HttpDataType.STRING,
        usingCache: true,
        priority: 1,
        connectTimeout: 60000,
        readTimeout: 60000,
        usingProtocol: http.HttpProtocol.HTTP1_1,
      }, (err, data) => {
      if (!err) {
        let res: Result = JSON.parse(data.result as string);
        callback(undefined, res);
      } else {
        let error: BusinessError = { code: err.code, message: err.message, name: '' };
        callback(error, undefined);
        // 取消订阅HTTP响应头事件。
        httpRequest.off('headersReceive');
        // 在httpRequest完成后调用destroy()方法以释放资源。
        httpRequest.destroy();
      }
    })
  }

  build() {
    Row() {
      Column() {
        FunctionalButton({
          params: {
            // OpenType.FACE_AUTHENTICATION表示该按钮用于人脸身份验证。
            openType: functionalButtonComponentManager.OpenType.FACE_AUTHENTICATION,
            label: '人脸核身',
            // 调整按钮样式。
            styleOption: {
              styleConfig: new functionalButtonComponentManager.ButtonConfig()
                .fontSize(20)
            },
          // 当OpenType为FACE_AUTHENTICATION时，回调必须为onFaceAuthentication。
          controller: new functionalButtonComponentManager.FunctionalButtonController()
            .onFaceAuthentication((err, data) => {
              if (err) {
                // 错误日志处理。
                hilog.error(0x0000, "testTag", "error: %{public}d %{public}s", err.code, err.message);
                return;
              }
              // 成功日志处理。
              hilog.info(0x0000, "testTag", "succeeded in authenticating");
              // 获取授权码。
              let authCode: string = data.authCode as string;
              let openID: string = data.openID as string;
              hilog.info(0x0000, "testTag", "succeeded in authCode");
              // sceneid 表示场景ID。选项包括：0（实名验证）、1（人脸验证，验证姓名、证件类型、证件号码和人脸）和2（人脸验证，仅验证人脸）。
              this.obtainFaceVerifyDataInfo(authCode, 2, openID, "", "", (err, data) => {
                if (err) {
                  hilog.error(0x0000, "testTag", "error: %{public}d %{public}s", err.code, err.message);
                  return;
                }
                let verifyToken: string = data.verifyToken as string;
                new functionalButtonComponentManager.FunctionalButtonController().onFaceVerification(verifyToken,
                  (error, data) => {
                    if (error) {
                      // 错误日志处理。
                      hilog.error(0x0000, "testTag", "error: %{public}d %{public}s", error.code, error.message);
                      return;
                    }
                    let facialRecognitionVerificationToken = data.facialRecognitionVerificationToken;
                    let state = data.state;
                    hilog.info(0x0000, 'testTag', 'auth result success');
                  });
              })
      }
      .width('100%')
    }
    .height('100%')
  }
```

#### onChooseLocation

onChooseLocation(callback: AsyncCallback<ChooseLocationResult>): [FunctionalButton](FunctionalButton（Button组件）.md#section1753203873911)Controller

注册[FunctionalButton](FunctionalButton（Button组件）.md#section1753203873911)组件为打开地图选点的点击事件，使用callback异步回调。

该接口功能依赖Map Kit，参见[chooseLocation](sceneMap（场景化控件）.md#ZH-CN_TOPIC_0000002553202377__chooselocation)。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.AtomicserviceComponent.UIComponent

**设备行为差异：**对于5.0.0(12)版本，该接口在Phone、Tablet中可正常调用，在其他设备类型中返回801错误码。对于5.0.1(13)及之后版本，该接口在Phone、Tablet、2in1中可正常调用，在其他设备类型中返回801错误码。

**起始版本：**5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<ChooseLocationResult> | 是 | 回调函数。当打开地图选点成功，err为undefined，data为地图选点的返回结果；否则为错误对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [FunctionalButton](FunctionalButton（Button组件）.md#section1753203873911)Controller | FunctionalButton组件控制器。 |

**示例：**

```ets
import { FunctionalButton, functionalButtonComponentManager } from '@kit.ScenarioFusionKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        // 声明FunctionalButton。
        FunctionalButton({
          params: {
            // OpenType.CHOOSE_LOCATION表示该按钮用于在地图上选择位置。
            openType: functionalButtonComponentManager.OpenType.CHOOSE_LOCATION,
            label: '地图选点',
            // 调整按钮样式。
            styleOption: {
              bgColor:functionalButtonComponentManager.ColorType.DEFAULT,
              size: functionalButtonComponentManager.SizeType.DEFAULT,
              plain: false,
              disabled:false,
              loading: false,
              hoverClass: functionalButtonComponentManager.HoverClassType.HOVER_CLASS,
              hoverStartTime: 0,
              hoverStayTime: 0,
              styleConfig: new functionalButtonComponentManager.ButtonConfig()
                .fontSize(20)
            },
          // 当OpenType设置为CHOOSE_LOCATION时，回调必须为onChooseLocation。
          controller: new functionalButtonComponentManager.FunctionalButtonController()
            .onChooseLocation((err, data) => {
              if (err) {
                // 错误日志处理。
                hilog.error(0x0000, "testTag", "error: %{public}d %{public}s", err.code, err.message);
                return;
              }
              // 成功日志处理。
              hilog.info(0x0000, "testTag", "succeeded in choosing location");
              let name: string = data.name;
              let address: string = data.address;
              let longitude: number = data.longitude;
              let latitude: number = data.latitude;
            })
      }.width('100%')
    }.height('100%')
}
```

#### onSubscribeLiveView

onSubscribeLiveView(callback: AsyncCallback<SubscribeLiveViewResult>): [FunctionalButton](FunctionalButton（Button组件）.md#section1753203873911)Controller

注册[FunctionalButton](FunctionalButton（Button组件）.md#section1753203873911)组件为实况窗订阅的点击事件，使用callback异步回调。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力****：**SystemCapability.AtomicserviceComponent.UIComponent

**设备行为差异：**该接口在Phone、Tablet中可正常调用，在其他设备类型中返回801错误码。

**起始版本：**5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<SubscribeLiveViewResult> | 是 | 回调函数。当实况窗订阅点击成功，err为undefined，data为实况订阅的返回结果；否则为错误对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [FunctionalButton](FunctionalButton（Button组件）.md#section1753203873911)Controller | FunctionalButton组件控制器。 |

**示例：**

```ets
import { hilog } from '@kit.PerformanceAnalysisKit';
import { FunctionalButton, functionalButtonComponentManager } from '@kit.ScenarioFusionKit';

@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        // 声明FunctionalButton。
        FunctionalButton({
          params: {
            // OpenType.SUBSCRIBE_LIVE_VIEW表示该按钮用于实时视图订阅。
            openType: functionalButtonComponentManager.OpenType.SUBSCRIBE_LIVE_VIEW,
            label: '预约抢购',
            // 调整按钮样式。
            styleOption: {
              styleConfig: new functionalButtonComponentManager.ButtonConfig()
                .fontSize(20)
            },
            subscribeLiveViewParam: {
              event: "SUBSCRIBE_TIMER",
              alertTime: 172178838111,
              startTime: 172170198111
            },
          // 当OpenType为SUBSCRIBE_LIVE_VIEW时，回调必须为onSubscribeLiveView。
          controller: new functionalButtonComponentManager.FunctionalButtonController().onSubscribeLiveView((err,
            data) => {
            if (err) {
              // 错误日志处理。
              hilog.error(0x0000, "testTag", `error code is: ${err?.code} message is ${err?.message}`);
              return;
            }
            let subscribeId = data.subscribeId;
            // 成功日志处理。
            hilog.info(0x0000, "testTag", "succeeded in subscribing LiveView");
          })
      }
      .width('100%')
    }
    .height('100%')
}
```

#### onPermissionSetting

onPermissionSetting(callback: AsyncCallback<PermissionSettingResult>): [FunctionalButton](FunctionalButton（Button组件）.md#section1753203873911)Controller

注册[FunctionalButton](FunctionalButton（Button组件）.md#section1753203873911)组件为权限设置的点击事件，使用callback异步回调。

该接口功能依赖Ability Kit，参见[requestPermissionOnSetting](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-abilityaccessctrl#requestpermissiononsetting12)。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.2(14)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.AtomicserviceComponent.UIComponent

**设备行为差异：**对于5.0.2(14)版本，该接口在Phone、Tablet、2in1中可正常调用，在其他设备类型中返回801错误码。对于5.1.0(18)及之后版本，该接口在Phone、Tablet、2in1、TV中可正常调用，在其他设备类型中返回801错误码。

**起始版本：**5.0.2(14)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<PermissionSettingResult> | 是 | 回调函数。当权限设置点击成功，err为undefined，data为获取到的权限设置返回结果；否则为错误对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [FunctionalButton](FunctionalButton（Button组件）.md#section1753203873911)Controller | FunctionalButton组件控制器。 |

**示例：**

```ets
import { FunctionalButton, functionalButtonComponentManager } from '@kit.ScenarioFusionKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { abilityAccessCtrl, common, PermissionRequestResult } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    Row() {
      Column({ space: 3 }) {
        // 调用requestPermissionsFromUser接口Button。
        Button('请求用户授权')
          .fontSize(20)
          .onClick(() => {
            let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
            let context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
            try {
              // 在module.json5文件中添加ohos.permission.READ_CALENDAR、ohos.permission.WRITE_CALENDAR权限。
              atManager.requestPermissionsFromUser(context,
                ['ohos.permission.READ_CALENDAR', 'ohos.permission.WRITE_CALENDAR'],
                (err: BusinessError, data: PermissionRequestResult) => {
                  if (err) {
                    hilog.error(0x0000, "testTag", "failed in requesting Permissions from user : %{public}d %{public}s",
                      err.code, err.message);
                  } else {
                   hilog.info(0x0000, "testTag", 'data permissions: %{public}s', data.permissions?.join(','));
                   hilog.info(0x0000, "testTag", 'data authResults: %{public}s', data.authResults?.join(','));
                   hilog.info(0x0000, "testTag", 'data dialogShownResults: %{public}s',data.dialogShownResults?.join(','));
                  }
                })
            } catch (err) {
              hilog.error(0x0000, "testTag", "error: %{public}d %{public}s", err.code, err.message);
            }
          })

        // 声明FunctionalButton。
        FunctionalButton({
          params: {
            // OpenType.PERMISSION_SETTING表示该按钮用于设置权限。
            openType: functionalButtonComponentManager.OpenType.PERMISSION_SETTING,
            label: '权限设置',
            permissionListParam: ['ohos.permission.READ_CALENDAR', 'ohos.permission.WRITE_CALENDAR'],
            // 调整按钮样式。
            styleOption: {
              styleConfig: new functionalButtonComponentManager.ButtonConfig()
                .fontSize(20)
            },
          // 当OpenType设置为PERMISSION_SETTING时，回调必须为onPermissionSetting。
          controller: new functionalButtonComponentManager.FunctionalButtonController().onPermissionSetting((err,
            data) => {
            if (err) {
              // 错误日志处理。
              hilog.error(0x0000, "testTag", "error: %{public}d %{public}s", err.code, err.message);
              return;
            }
            // 成功日志处理。
            hilog.info(0x0000, "testTag", "succeeded in setting permission ");
            let result = data.permissionResult;
            result.forEach(res => {
              hilog.info(0x0000, "testTag", "data: %{public}s", String(res));
            })
      }
      .width('100%')
    }
    .height('100%')
  }
```

#### onRequestSubscribeMessage

onRequestSubscribeMessage(callback: AsyncCallback<RequestSubscribeMessageResult>): [FunctionalButton](FunctionalButton（Button组件）.md#section1753203873911)Controller

注册[FunctionalButton](FunctionalButton（Button组件）.md#section1753203873911)组件为服务动态授权码按钮的点击事件，使用callback异步回调。


该接口在元服务中可正常使用。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.AtomicserviceComponent.UIComponent

**设备行为差异：**该接口在Phone、Tablet中可正常调用，在其他设备类型中返回801错误码。

**起始版本：**6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<RequestSubscribeMessageResult> | 是 | 回调函数。当服务动态授权码按钮点击成功，err为undefined，data为获取到的code返回结果；否则为错误对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [FunctionalButton](FunctionalButton（Button组件）.md#section1753203873911)Controller | FunctionalButton组件控制器。 |

错误码：

| 错误码ID | 错误信息 |
| --- | --- |
| 10004 | Internal error. |
| 10008 | Not atomic service. |

**示例：**

```ets
import { FunctionalButton, functionalButtonComponentManager } from '@kit.ScenarioFusionKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        // 声明FunctionalButton。
        FunctionalButton({
          params: {
            // OpenType.REQUEST_SUBSCRIBE_MESSAGE表示该按钮用于获取服务动态授权码。
            openType: functionalButtonComponentManager.OpenType.REQUEST_SUBSCRIBE_MESSAGE,
            label: '服务动态授权码',
            // 在获取服务动态授权码时，名为subSceneId的参数是必填项。
            subSceneId: '',
            // 调整按钮样式。
            styleOption: {
              styleConfig: new functionalButtonComponentManager.ButtonConfig()
                .fontSize(20)
            },
          // 当OpenType为REQUEST_SUBSCRIBE_MESSAGE时，回调必须为onRequestSubscribeMessage。
          controller: new functionalButtonComponentManager.FunctionalButtonController()
            .onRequestSubscribeMessage((err, data) => {
              if (err) {
                // 错误日志处理。
                hilog.error(0x0000, "testTag", "error: %{public}d %{public}s", err.code, err.message);
                return;
              }
              // 成功日志处理。
              hilog.info(0x0000, "testTag", "succeeded in requesting subscribe message");
              // 处理服务代码。
              let code = data.code;
            })
      }.width('100%')
    }.height('100%')
}
```

#### onShare

onShare(callback: AsyncCallback<void>): [FunctionalButton](FunctionalButton（Button组件）.md#section1753203873911)Controller

注册[FunctionalButton](FunctionalButton（Button组件）.md#section1753203873911)组件为分享按钮的点击事件，使用callback异步回调。

仅提供给已发布的元服务使用。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.AtomicserviceComponent.UIComponent

**设备行为差异：**该接口在Phone、Tablet中可正常调用，在其他设备类型中返回801错误码。

**起始版本：**6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当分享按钮点击成功，err为undefined，否则为错误对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [FunctionalButton](FunctionalButton（Button组件）.md#section1753203873911)Controller | FunctionalButton组件控制器。 |

错误码：

| 错误码ID | 错误信息 |
| --- | --- |
| 10004 | Internal error. |
| 10006 | Failed to get data. |
| 10008 | Not atomic service. |

**示例：**

```ets
import { FunctionalButton, functionalButtonComponentManager } from '@kit.ScenarioFusionKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        // 声明FunctionalButton。
        FunctionalButton({
          params: {
            // OpenType.SHARE 表示该按钮用于调出分享页面。
            openType: functionalButtonComponentManager.OpenType.SHARE,
            label: '元服务分享',
            shareParam: {
              previewUri: '',
              description: ''
            },
            // 调整按钮样式。
            styleOption: {
              styleConfig: new functionalButtonComponentManager.ButtonConfig()
                .fontSize(20)
            },
          // 当OpenType设置为SHARE时，回调函数必须是onShare。
          controller: new functionalButtonComponentManager.FunctionalButtonController()
            .onShare((err) => {
              if (err) {
                // 错误日志处理。
                hilog.error(0x0000, "testTag", "error: %{public}d %{public}s", err.code, err.message);
                return;
              }
              // 成功日志处理。
              hilog.info(0x0000, "testTag", "succeeded in pulling up the sharing page");
            })
      }.width('100%')
    }.height('100%')
}
```

#### onFeedback

onFeedback(callback: AsyncCallback<void>): [FunctionalButton](FunctionalButton（Button组件）.md#section1753203873911)Controller

注册[FunctionalButton](FunctionalButton（Button组件）.md#section1753203873911)组件为反馈按钮的点击事件，使用callback异步回调。

仅提供给元服务使用。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.AtomicserviceComponent.UIComponent

**设备行为差异：**该接口在Phone、Tablet中可正常调用，在其他设备类型中返回801错误码。

**起始版本：**6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当反馈按钮点击成功，err为undefined，否则为错误对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [FunctionalButton](FunctionalButton（Button组件）.md#section1753203873911)Controller | FunctionalButton组件控制器。 |

错误码：

| 错误码ID | 错误信息 |
| --- | --- |
| 10008 | Not atomic service. |

**示例：**

```ets
import { FunctionalButton, functionalButtonComponentManager } from '@kit.ScenarioFusionKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        // 声明FunctionalButton。
        FunctionalButton({
          params: {
            // OpenType.FEEDBACK表示该按钮用于拉起反馈页面。
            openType: functionalButtonComponentManager.OpenType.FEEDBACK,
            label: '反馈与投诉',
            // 调整按钮样式。
            styleOption: {
              styleConfig: new functionalButtonComponentManager.ButtonConfig()
                .fontSize(20)
            },
          // 当OpenType设置为FEEDBACK时，回调函数必须是onFeedback。
          controller: new functionalButtonComponentManager.FunctionalButtonController()
            .onFeedback((err) => {
              if (err) {
                // 错误日志处理。
                hilog.error(0x0000, "testTag", "error: %{public}d %{public}s", err.code, err.message);
                return;
              }
              // 成功日志处理。
              hilog.info(0x0000, "testTag", "succeeded in pulling up the feedback page");
            })
      }.width('100%')
    }.height('100%')
}
```

#### onGetPhoneNumberAndRiskLevel

onGetPhoneNumberAndRiskLevel(callback: Callback<GetPhoneNumberAndRiskLevelResult>): [FunctionalButton](FunctionalButton（Button组件）.md#section1753203873911)Controller

注册[FunctionalButton](FunctionalButton（Button组件）.md#section1753203873911)组件为获取手机号和风险等级的点击事件，使用callback异步回调。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本6.0.2(22)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.AtomicserviceComponent.UIComponent

**起始版本：**6.0.2(22)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<GetPhoneNumberAndRiskLevelResult> | 是 | 回调函数。返回获取手机号和风险等级的授权码。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [FunctionalButton](FunctionalButton（Button组件）.md#section1753203873911)Controller | FunctionalButton组件控制器。 |

**示例：**

```ets
import { FunctionalButton, functionalButtonComponentManager } from '@kit.ScenarioFusionKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        // 声明FunctionalButton。
        FunctionalButton({
          params: {
            // OpenType.GET_PHONE_NUMBER_AND_RISK_LEVEL表示该按钮用于获取手机号和风险等级。
            openType: functionalButtonComponentManager.OpenType.GET_PHONE_NUMBER_AND_RISK_LEVEL,
            label: '获取手机号和风险等级',
            // 调整按钮样式。
            styleOption: {
              styleConfig: new functionalButtonComponentManager.ButtonConfig()
                .fontSize(20)
            },
          // 当OpenType为GET_PHONE_NUMBER_AND_RISK_LEVEL时，回调必须为onGetPhoneNumberAndRiskLevel。
          controller: new functionalButtonComponentManager.FunctionalButtonController()
            .onGetPhoneNumberAndRiskLevel((data) => {
              if (data?.errCode) {
                // 错误日志处理。
                hilog.error(0x0000, "testTag", "error: %{public}d %{public}s", data?.errCode, data?.errMsg);
                return;
              }
              // 成功日志处理。
              hilog.info(0x0000, "testTag", "succeeded in authentication");
              // 授权码处理。
              let authorizationCode = data?.code;
            })
      }
      .width('100%')
    }
    .height('100%')
}
```

#### ButtonConfig

该类提供了实现[FunctionalButton](FunctionalButton（Button组件）.md#section1753203873911)自定义属性的方法。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.AtomicserviceComponent.UIComponent

**起始版本：**4.1.0(11)

#### type

type(value: ButtonType): ButtonConfig

设置[FunctionalButton](FunctionalButton（Button组件）.md#section1753203873911)的显示样式属性。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.AtomicserviceComponent.UIComponent

**起始版本：**4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | ButtonType | 是 | 描述按钮显示样式。 默认值：ButtonType.Capsule |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ButtonConfig | ButtonConfig对象。 |

#### stateEffect

stateEffect(value: boolean): ButtonConfig

设置[FunctionalButton](FunctionalButton（Button组件）.md#section1753203873911)是否开启按压态显示效果属性。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.AtomicserviceComponent.UIComponent

**起始版本：**4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 按钮按下时是否开启按压态显示效果，当设置为false时，按压效果关闭；设置为true时，按压效果开启。 默认值：true |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ButtonConfig | ButtonConfig对象。 |

#### fontColor

fontColor(value: ResourceColor): ButtonConfig

设置[FunctionalButton](FunctionalButton（Button组件）.md#section1753203873911)的字体颜色属性。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.AtomicserviceComponent.UIComponent

**起始版本：**4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | ResourceColor | 是 | 设置字体颜色。 默认值：#ffffff |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ButtonConfig | ButtonConfig对象。 |

#### fontSize

fontSize(value: Length): ButtonConfig

设置[FunctionalButton](FunctionalButton（Button组件）.md#section1753203873911)的字体大小属性。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.AtomicserviceComponent.UIComponent

**起始版本：**4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Length | 是 | 设置字体大小，Length为number类型时，使用fp单位。 字体默认大小16fp。不支持设置百分比字符串。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ButtonConfig | ButtonConfig对象。 |

#### fontWeight

fontWeight(value: string | number | FontWeight): ButtonConfig

设置[FunctionalButton](FunctionalButton（Button组件）.md#section1753203873911)的字体粗细属性。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.AtomicserviceComponent.UIComponent

**起始版本：**4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string | number | FontWeight | 是 | 设置文本的字体粗细，number类型取值[100, 900]，取值间隔为100，默认为400，取值越大，字体越粗。string类型仅支持number类型取值的字符串形式，例如"400"，以及"bold"，"bolder"，"lighter"，"regular"，"medium"，"normal"，分别对应FontWeight中相应的枚举值。 默认值：FontWeight.Normal |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ButtonConfig | ButtonConfig对象。 |

#### fontStyle

fontStyle(value: FontStyle): ButtonConfig

设置[FunctionalButton](FunctionalButton（Button组件）.md#section1753203873911)的字体样式属性。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.AtomicserviceComponent.UIComponent

**起始版本：**4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | FontStyle | 是 | 设置字体样式。 默认值：FontStyle.Normal |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ButtonConfig | ButtonConfig对象。 |

#### fontFamily

fontFamily(value: string | Resource): ButtonConfig

设置[FunctionalButton](FunctionalButton（Button组件）.md#section1753203873911)的字体属性。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.AtomicserviceComponent.UIComponent

**起始版本：**4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string | Resource | 是 | 设置字体列表。默认字体'HarmonyOS Sans'，当前支持'HarmonyOS Sans'字体和注册自定义字体。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ButtonConfig | ButtonConfig对象。 |

#### width

width(value: Length): ButtonConfig

设置[FunctionalButton](FunctionalButton（Button组件）.md#section1753203873911)的宽度属性。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.AtomicserviceComponent.UIComponent

**起始版本：**4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Length | 是 | 设置组件自身的宽度，缺省时使用元素自身内容需要的宽度。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ButtonConfig | ButtonConfig对象。 |

#### height

height(value: Length): ButtonConfig

设置[FunctionalButton](FunctionalButton（Button组件）.md#section1753203873911)的高度属性。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.AtomicserviceComponent.UIComponent

**起始版本：**4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Length | 是 | 设置组件自身的高度，缺省时使用元素自身内容需要的高度。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ButtonConfig | ButtonConfig对象。 |

#### size

size(value: SizeOptions): ButtonConfig

设置[FunctionalButton](FunctionalButton（Button组件）.md#section1753203873911)的高宽尺寸属性。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.AtomicserviceComponent.UIComponent

**起始版本：**4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | SizeOptions | 是 | 设置高宽尺寸。举例： { width: 20, height: 50 } 单位：vp。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ButtonConfig | ButtonConfig对象。 |

#### constraintSize

constraintSize(value: ConstraintSizeOptions): ButtonConfig

设置[FunctionalButton](FunctionalButton（Button组件）.md#section1753203873911)的约束尺寸属性。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.AtomicserviceComponent.UIComponent

**起始版本：**4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | ConstraintSizeOptions | 是 | 设置约束尺寸，组件布局时，进行尺寸范围限制。constraintSize的优先级高于width和height。取值结果参考constraintSize取值对width/height影响。 默认值： { minWidth: 0, maxWidth: Infinity, minHeight: 0, maxHeight: Infinity } 单位：vp。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ButtonConfig | ButtonConfig对象。 |

#### padding

padding(value: Length | Padding): ButtonConfig

设置[FunctionalButton](FunctionalButton（Button组件）.md#section1753203873911)的内边距属性。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.AtomicserviceComponent.UIComponent

**起始版本：**4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Length | Padding | 是 | 设置内边距属性。 参数为Length类型时，四个方向内边距同时生效。 默认值：{left: 16, right: 16} 单位：vp。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ButtonConfig | ButtonConfig对象。 |

#### margin

margin(value: Length | Padding): ButtonConfig

设置[FunctionalButton](FunctionalButton（Button组件）.md#section1753203873911)的外边距属性。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.AtomicserviceComponent.UIComponent

**起始版本：**4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Length | Padding | 是 | 设置外边距属性。 参数为Length类型时，四个方向外边距同时生效。 默认值：0 单位：vp。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ButtonConfig | ButtonConfig对象。 |

#### backgroundColor

backgroundColor(value: ResourceColor): ButtonConfig

设置[FunctionalButton](FunctionalButton（Button组件）.md#section1753203873911)的背景色属性。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.AtomicserviceComponent.UIComponent

**起始版本：**4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | ResourceColor | 是 | 设置组件的背景色。 默认值：#ff007dff |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ButtonConfig | ButtonConfig对象。 |

#### backgroundImage

backgroundImage(src: ResourceStr, repeat?: ImageRepeat): ButtonConfig

设置[FunctionalButton](FunctionalButton（Button组件）.md#section1753203873911)的背景图像属性。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.AtomicserviceComponent.UIComponent

**起始版本：**4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src | ResourceStr | 是 | 图片地址，支持网络图片资源和本地图片资源地址，不支持svg类型的图片。 |
| repeat | ImageRepeat | 否 | 设置背景图的重复样式，默认不重复。当设置的背景图片为透明底色图片，且同时设置了backgroundColor时，二者叠加显示，背景颜色在最底部。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ButtonConfig | ButtonConfig对象。 |

#### backgroundImageSize

backgroundImageSize(value: SizeOptions | ImageSize): ButtonConfig

设置[FunctionalButton](FunctionalButton（Button组件）.md#section1753203873911)的背景图像的高度和宽度属性。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.AtomicserviceComponent.UIComponent

**起始版本：**4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | SizeOptions | ImageSize | 是 | 设置背景图像的高度和宽度。当输入为{width: Length, height: Length}对象时，如果只设置一个属性，则第二个属性保持图片原始宽高比进行调整。默认保持原图的比例不变。 width和height取值范围： [0, +∞) 默认值：ImageSize.Auto 说明：  设置为小于0的值时，按值为0显示。当设置了height未设置width时，width根据图片原始宽高比进行调整。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ButtonConfig | ButtonConfig对象。 |

#### backgroundImagePosition

backgroundImagePosition(value: Position | Alignment): ButtonConfig

设置[FunctionalButton](FunctionalButton（Button组件）.md#section1753203873911)的背景图像的显示位置属性。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.AtomicserviceComponent.UIComponent

**起始版本：**4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Position | Alignment | 是 | 设置背景图像在组件中显示位置，即相对于组件左上角的坐标，单位vp。 默认值： { x: 0, y: 0 } x和y值设置百分比时，偏移量是相对组件自身宽高计算的。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ButtonConfig | ButtonConfig对象。 |

#### opacity

opacity(value: number | Resource): ButtonConfig

设置[FunctionalButton](FunctionalButton（Button组件）.md#section1753203873911)的透明度属性。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.AtomicserviceComponent.UIComponent

**起始版本：**4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | Resource | 是 | 元素的不透明度，取值范围为0到1，默认值：1，1表示不透明，0表示完全透明, 达到隐藏组件效果，但是在布局中占位。 说明：  子组件可以继承父组件的此属性。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ButtonConfig | ButtonConfig对象。 |

#### border

border(value: BorderOptions): ButtonConfig

统一设置[FunctionalButton](FunctionalButton（Button组件）.md#section1753203873911)的边框宽度、边框颜色、边框圆角半径、边框样式属性。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.AtomicserviceComponent.UIComponent

**起始版本：**4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | BorderOptions | 是 | 统一边框样式设置接口。 - width：设置边框宽度。 - color：设置边框颜色。 - radius：设置边框圆角半径。 - style：设置边框样式。 说明：  边框宽度默认值为0，即不显示边框。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ButtonConfig | ButtonConfig对象。 |

#### borderStyle

borderStyle(value: BorderStyle | EdgeStyles): ButtonConfig

设置[FunctionalButton](FunctionalButton（Button组件）.md#section1753203873911)的边框样式属性。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.AtomicserviceComponent.UIComponent

**起始版本：**4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | BorderStyle | EdgeStyles | 是 | 设置元素的边框样式。 默认值：BorderStyle.Solid |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ButtonConfig | ButtonConfig对象。 |

#### borderWidth

borderWidth(value: Length | EdgeWidths): ButtonConfig

设置[FunctionalButton](FunctionalButton（Button组件）.md#section1753203873911)的边框宽度属性。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.AtomicserviceComponent.UIComponent

**起始版本：**4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Length | EdgeWidths | 是 | 设置元素的边框宽度，不支持百分比。 默认值：1，单位：vp。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ButtonConfig | ButtonConfig对象。 |

#### borderColor

borderColor(value: ResourceColor | EdgeColors): ButtonConfig

设置[FunctionalButton](FunctionalButton（Button组件）.md#section1753203873911)的边框颜色属性。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.AtomicserviceComponent.UIComponent

**起始版本：**4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | ResourceColor | EdgeColors | 是 | 设置元素的边框颜色。 默认值：#000000 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ButtonConfig | ButtonConfig对象。 |

#### borderRadius

borderRadius(value: Length | BorderRadiuses): ButtonConfig

设置[FunctionalButton](FunctionalButton（Button组件）.md#section1753203873911)的边框圆角半径属性。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.AtomicserviceComponent.UIComponent

**起始版本：**4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Length | BorderRadiuses | 是 | 设置元素的边框圆角半径，不支持百分比。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ButtonConfig | ButtonConfig对象。 |

#### borderImage

borderImage(value: BorderImageOption): ButtonConfig

设置[FunctionalButton](FunctionalButton（Button组件）.md#section1753203873911)的图片边框属性。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.AtomicserviceComponent.UIComponent

**起始版本：**4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | BorderImageOption | 是 | 图片边框或者渐变色边框设置接口。 该接口支持在ArkTS卡片中使用。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ButtonConfig | ButtonConfig对象。 |

#### scale

scale(value: ScaleOptions): ButtonConfig

设置[FunctionalButton](FunctionalButton（Button组件）.md#section1753203873911)的缩放属性。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.AtomicserviceComponent.UIComponent

**起始版本：**4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | ScaleOptions | 是 | 可以分别设置X轴、Y轴、Z轴的缩放比例，默认值为1.0，同时可以通过centerX和centerY设置缩放的中心点。 默认值： { x: 1.0, y: 1.0, z: 1.0, centerX:'0.5', centerY:'0.5' } |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ButtonConfig | ButtonConfig对象。 |

#### align

align(value: Alignment): ButtonConfig

设置[FunctionalButton](FunctionalButton（Button组件）.md#section1753203873911)的对齐方式属性。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.AtomicserviceComponent.UIComponent

**起始版本：**4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Alignment | 是 | 设置元素内容的对齐方式，只有当设置的width和height大小超过元素本身内容大小时生效。 默认值：Alignment.Center |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ButtonConfig | ButtonConfig对象。 |

#### markAnchor

markAnchor(value: Position): ButtonConfig

设置[FunctionalButton](FunctionalButton（Button组件）.md#section1753203873911)在位置定位时的锚点。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.AtomicserviceComponent.UIComponent

**起始版本：**4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Position | 是 | 设置元素在位置定位时的锚点，以元素顶部起点作为基准点进行偏移，单位vp。 默认值： { x: 0, y: 1 } |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ButtonConfig | ButtonConfig对象。 |

#### offset

offset(value: Position): ButtonConfig

设置[FunctionalButton](FunctionalButton（Button组件）.md#section1753203873911)在位置坐标偏移量。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.AtomicserviceComponent.UIComponent

**起始版本：**4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Position | 是 | 设置元素在位置定位时的锚点，以元素顶部起点作为基准点进行偏移，单位vp。 默认值： { x: 0, y: 1 } |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ButtonConfig | ButtonConfig对象。 |

#### enabled

enabled(value: boolean): ButtonConfig

设置[FunctionalButton](FunctionalButton（Button组件）.md#section1753203873911)的是否禁用属性。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.AtomicserviceComponent.UIComponent

**起始版本：**4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 值为true表示组件可交互，响应点击等操作。 值为false表示组件不可交互，不响应点击等操作。 默认值：true |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ButtonConfig | ButtonConfig对象。 |

#### loadingColor

loadingColor(value: ResourceColor): ButtonConfig

设置[FunctionalButton](FunctionalButton（Button组件）.md#section1753203873911)中的LoadingProgress图标的颜色属性。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.AtomicserviceComponent.UIComponent

**起始版本：**4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | ResourceColor | 是 | 设置图标颜色。默认值：#FFFFFF 说明：  设置为异常值时，按值为'#ff666666'显示。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ButtonConfig | ButtonConfig对象。 |

#### loadingWidth

loadingWidth(value: Length): ButtonConfig

设置[FunctionalButton](FunctionalButton（Button组件）.md#section1753203873911)中的LoadingProgress图标的宽度属性。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.AtomicserviceComponent.UIComponent

**起始版本：**4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Length | 是 | 设置图标自身的宽度。默认值：20，单位：vp。 取值范围：(-∞, +∞) 填写为负数时，宽度不超过按钮大小；填写正数时，宽度不受限于按钮大小，请合理填写数值。 说明：  LoadingProgress图标始终保持正方形，在显示时边长会取loadingWidth和loadingHeight中的最小值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ButtonConfig | ButtonConfig对象。 |

#### loadingHeight

loadingHeight(value: Length): ButtonConfig

设置[FunctionalButton](FunctionalButton（Button组件）.md#section1753203873911)中的LoadingProgress图标的高度属性。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.AtomicserviceComponent.UIComponent

**起始版本：**4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Length | 是 | 设置图标自身的高度。默认值：20，单位：vp。 取值范围：(-∞, +∞) 填写为负数时，高度不超过按钮大小。填写正数时，高度不受限于按钮大小，请合理填写数值。 说明：  LoadingProgress图标始终保持正方形，在显示时边长会取loadingWidth和loadingHeight中的最小值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ButtonConfig | ButtonConfig对象。 |

#### loadingPadding

loadingPadding(value: Length | Padding): ButtonConfig

设置[FunctionalButton](FunctionalButton（Button组件）.md#section1753203873911)中的LoadingProgress图标的内边距属性。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.AtomicserviceComponent.UIComponent

**起始版本：**4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Length | Padding | 是 | 设置图标内边距属性。单位：vp。 默认值：0 取值范围：(-∞, +∞) |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ButtonConfig | ButtonConfig对象。 |

#### loadingMargin

loadingMargin(value: Length | Padding): ButtonConfig

设置[FunctionalButton](FunctionalButton（Button组件）.md#section1753203873911)中的LoadingProgress图标的外边距属性。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.AtomicserviceComponent.UIComponent

**起始版本：**4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Length | Padding | 是 | 设置图标外边距属性。单位：vp。 默认值：{left: -2, right: 2} 取值范围：(-∞, +∞) |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ButtonConfig | ButtonConfig对象。 |

#### 示例

#### 示例一（场景化Button使用自定义Modifier设置按钮样式）

```ets
import { FunctionalButton, functionalButtonComponentManager } from '@kit.ScenarioFusionKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { ButtonModifier, LoadingProgressModifier, TextModifier } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        // 声明FunctionalButton。
        FunctionalButton({
          params: {
            // OpenType.GET_PHONE_NUMBER表示该按钮用于快速验证手机号码。
            openType: functionalButtonComponentManager.OpenType.GET_PHONE_NUMBER,
            label: '快速验证手机号',
            // 调整按钮样式。
            styleOption: {
              loading: true,
            },
            textModifier: new TextModifier().fontColor(Color.Pink),
            buttonModifier: new ButtonModifier().backgroundColor(Color.Green),
            loadingProgressModifier: new LoadingProgressModifier().width(20).height(20),
          },
          // 当OpenType为GET_PHONE_NUMBER时，回调必须为onGetPhoneNumber。
          controller: new functionalButtonComponentManager.FunctionalButtonController()
            .onGetPhoneNumber((err, data) => {
              if (err) {
                // 错误日志处理。
                hilog.error(0x0000, "testTag", "error: %{public}d %{public}s", err.code, err.message);
                return;
              }
              // 成功日志处理。
              hilog.info(0x0000, "testTag", "succeeded in authenticating");
              // 处理授权码。
              let authorizationCode = data.code;
            })
      }
      .width('100%')
    }
    .height('100%')
  }
```

![image](public_sys-resources/zh-cn_image_0000002553206129.webp)