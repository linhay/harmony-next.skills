# loginComponentManager (华为账号登录组件管理)

本模块提供华为账号登录组件的逻辑管理，辅助应用通过集成华为账号登录组件完成登录功能。

**起始版本：**4.1.0(11)

#### 导入模块

```ets
import { loginComponentManager } from '@kit.AccountKit';
```

#### LoginType

该枚举定义了华为账号登录类型。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力****：**SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：**4.1.0(11)

名称

值

说明

ID

0

表示用OpenID、UnionID来关联华为账号。

用户在登录成功后会返回对应数据。

该登录类型响应数据包含openID、unionID、authorizationCode、idToken字段。

PHONE_NUMBER

1

表示用PhoneNumber来关联华为账号。

用户在登录成功后，如之前未对快速验证手机号进行授权，则会拉起手机号授权页面；如已授权，则返回对应数据。

该登录类型不需要实时验证华为账号的手机号码，响应数据包含openID、unionID、authorizationCode、idToken字段。

应用使用Authorization Code调用[获取用户级凭证接口](获取用户级凭证.md#section1085901313579)向华为账号服务器请求获取Access Token，再使用Access Token调用[获取华为账号用户信息接口](获取华为账号用户信息-获取手机号.md#section2520125725115)获取用户信息，从用户信息中获取用户手机号。

REAL_TIME_PHONE_NUMBER

2

表示用PhoneNumber来关联华为账号。

用户每次在登录成功后，都会拉起实时验证手机号授权页面。

该登录类型会实时验证华为账号的手机号码，响应数据包含openID、unionID、authorizationCode、idToken字段。

应用使用Authorization Code调用[获取用户级凭证接口](获取用户级凭证.md#section1085901313579)向华为账号服务器请求获取Access Token，再使用Access Token调用[获取华为账号用户信息接口](获取华为账号用户信息-获取手机号.md#section2520125725115)获取用户信息，从用户信息中获取用户手机号。

 说明：

REAL_TIME_PHONE_NUMBER暂不支持使用。

QUICK_LOGIN

3

表示用PhoneNumber来关联华为账号。

该类型不支持Icon类型和图文类型的LoginWithHuaweiIDButton组件。

该登录类型需要通过[AuthorizationWithHuaweiIDRequest](authentication (华为账号应用统一认证服务).md#section12940173017165)接口获取华为账号绑定的匿名手机号，如果未获取到华为账号绑定的匿名手机号，请使用其他登录类型。

该登录类型响应数据包含openID、unionID、authorizationCode、idToken字段。

应用使用Authorization Code调用[/oauth2/v6/quickLogin/getPhoneNumber接口](一键登录获取华为账号绑定号码和UnionID_OpenID.md#section2520125725115)获取用户信息，从用户信息中获取用户手机号。

**起始版本：**5.0.0(12)

**设备行为差异：**该接口在Phone、PC/2in1、Tablet、TV(仅在5.1.1版本)中可正常调用，在其他设备类型中返回1001500003错误码。

#### AppInfo

该接口定义了用于显示登录面板的应用信息。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力****：**SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：**4.1.0(11)

名称

类型

只读

可选

说明

appIcon

[PixelMap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-pixelmap) | [ResourceStr](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resourcestr) | [DrawableDescriptor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-drawabledescriptor#drawabledescriptor)

否

否

应用的图标。

appName

[ResourceStr](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resourcestr)

否

否

应用的名称，长度限制1-19个字符，字符超长和大字体下展示不全会截断，使用省略号填充。

appDescription

[ResourceStr](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resourcestr)

否

是

应用的详细描述，长度限制1-44个字符。

 说明：

- 在4.1.0(11)版本，为必填参数。
- 从5.0.0(12)版本开始，为非必填参数。仅当登录类型为[LoginType.QUICK_LOGIN](#section79023235528)时不需要设置该值。

#### TextType

该枚举定义了显示在登录面板上的隐私文本类型。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力****：**SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：**4.1.0(11)

名称

值

说明

PLAIN_TEXT

0

纯文本类型不支持点击。

RICH_TEXT

1

富文本类型展示为蓝色，支持点击。用于展示《华为账号用户认证协议》和应用相关隐私协议。

#### PrivacyText

该接口定义了使用登录面板或登录按钮时需要展示的隐私文本。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力****：**SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：**4.1.0(11)

名称

类型

只读

可选

说明

type

[TextType](#section7401948625)

否

否

隐私文本的类型，包含纯文本和富文本。

text

[ResourceStr](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resourcestr)

否

否

在登录面板上显示的隐私文本内容，一般用于展示应用隐私协议和《华为账号用户认证协议》跳转链接。

tag

string

否

是

当type类型为[TextType.RICH_TEXT](#section7401948625)必须设置tag。当用户点击文本时将跳转应用给tag设置的链接，应用可以根据用户的点击行为展示不同的隐私内容。

#### LoginIcon

该接口定义了可选登录区域展示的登录Icon属性。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力****：**SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：**5.0.0(12)

名称

类型

只读

可选

说明

icon

[PixelMap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-pixelmap) | [ResourceStr](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resourcestr) | [DrawableDescriptor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-drawabledescriptor#drawabledescriptor)

否

否

可选登录区域展示其他登录方式的Icon。根据[视觉规范](https://developer.huawei.com/consumer/cn/doc/design-guides/id-0000001880001344#section61791745172816)，Icon建议为半径18vp的圆形图片。

tag

string

否

是

当用户点击Icon时可以将tag对应值回调给应用，应用可以根据用户的点击行为展示其他登录方式页面。

#### OptionalLoginButtonAttr

该接口定义了可选登录按钮的属性。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力****：**SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：**4.1.0(11)

名称

类型

只读

可选

说明

text

[ResourceStr](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resourcestr)

否

否

可选登录按钮的文字描述。

#### OptionalLoginAreaAttr

该接口定义了可选登录区域的属性。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力****：**SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：**5.0.0(12)

名称

类型

只读

可选

说明

iconArray

[LoginIcon](#section1248254952118)[]

否

否

可选登录区域会展示应用传入的其他登录方式的Icon，最多支持展示5个Icon。

#### LoginPanelParams

该接口定义了显示在登录面板上的信息。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力****：**SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：**4.1.0(11)

名称

类型

只读

可选

说明

appInfo

[AppInfo](#section52091116105916)

否

否

组件展示应用信息。

privacyText

[PrivacyText](#section7272252193)[]

否

是

组件展示隐私文本内容。

optionalLoginButtonAttr

[OptionalLoginButtonAttr](#section16996104113138)

否

是

组件展示可选登录按钮。

loginType

[LoginType](#section79023235528)

否

是

华为账号登录类型。默认值：[LoginType.ID](#section79023235528)。

一键登录请使用[LoginType.QUICK_LOGIN](#section79023235528)。

anonymousPhoneNumber

string

否

是

华为账号绑定的匿名手机号。当登录类型为[LoginType.QUICK_LOGIN](#section79023235528)时需要设置该参数。可参考[华为账号一键登录客户端开发](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-phone-unionid-login#section834212543125)获取。

**起始版本：**5.0.0(12)

verifyPhoneNumber

boolean

否

是

华为账号用户在过去90天内未进行过短信验证，是否拉起Account Kit提供的短信验证码页面。

true：拉起Account Kit提供的短信验证码页面。

false：不拉起Account Kit提供的短信验证码页面。需要应用验证手机号时效性。

默认值：true。

**起始版本：**5.0.0(12)

optionalLoginAreaAttr

[OptionalLoginAreaAttr](#section438720171816)

否

是

组件可选登录区域属性。

如果optionalLoginButtonAttr和optionalLoginAreaAttr同时存在，优先展示optionalLoginAreaAttr。

**起始版本：**5.0.0(12)

riskLevel

boolean

否

是

是否需要获取华为账号用户风险等级。

仅登录类型为[LoginType.QUICK_LOGIN](#section79023235528)时需要设置该参数。

true：需要[获取用户风险等级](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-get-risklevel-byquicklogin)。

false：不获取用户风险等级。

默认值：false。

**起始版本：**5.1.0(18)

securityVerification

boolean

否

是

用户开启华为账号一键登录增强身份验证后，应用会在登录过程中通过华为账号使用生物识别或短信进行身份验证。如果需要获取用户一键登录增强身份验证的开关状态，需设置该字段为false。

仅登录类型为[LoginType.QUICK_LOGIN](#section79023235528)时需要设置该参数。

true：响应结果HuaweiIDCredential将不会返回 [enableSecurityVerification](#section1862534912215)。

false：响应结果HuaweiIDCredential将返回 [enableSecurityVerification](#section1862534912215)。

默认值：true。

**起始版本：**6.0.0(20)

#### ClickEvent

该枚举定义了用户点击华为账号登录按钮事件。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力****：**SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：**5.0.0(12)

名称

值

说明

HUAWEI_ID_LOGIN_BUTTON

0

点击华为账号登录按钮。

#### AgreementStatus

该枚举定义了用户是否同意通过[TextType.RICH_TEXT](#section7401948625)设置的协议的状态。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力****：**SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：**5.0.0(12)

名称

值

说明

NOT_ACCEPTED

0

用户未同意协议。

ACCEPTED

1

用户已同意协议。

#### HuaweiIDCredential

定义使用华为账号登录成功响应结果。用于获取用户相关信息和关联华为账号。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力****：**SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：**4.1.0(11)

名称

类型

只读

可选

说明

unionID

string

是

否

UnionID。UnionID是华为账号用户在同一个开发者账号下产品的身份ID，同一个用户，同一个开发者账号下管理的不同应用，UnionID值相同。具体格式要求请参考[OpenID和UnionID的格式说明](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-faq-9)。

openID

string

是

否

OpenID。OpenID是华为账号用户在不同类型的产品的身份ID，同一个用户，不同应用，OpenID值不同。具体格式要求请参考[OpenID和UnionID的格式说明](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-faq-9)。

authorizationCode

string

是

否

Authorization Code。临时凭据，用于获取Access Token，有效时间5分钟，并且只能使用1次。长度限制1-1024。

idToken

string

是

是

ID Token。JWT格式的字符串，包含用户信息，用于应用获取部分用户相关信息及验证签名。长度限制1-2048。

enableSecurityVerification

boolean

是

是

enableSecurityVerification。华为账号用户是否开启一键登录增强身份验证。如果开发者需要获取该字段，请将参数[securityVerification](#section4717249182518)设置为false。

仅登录类型为[LoginType.QUICK_LOGIN](#section79023235528)时会返回该字段。

true：表示用户已启用增强身份验证。

false：表示用户未启用增强身份验证。

**起始版本：**6.0.0(20)

#### 事件

不支持通用事件，仅支持以下事件：

#### LoginPanelController

[LoginPanel](LoginPanel (华为账号Panel登录组件).md)组件控制器，用来注册组件内部的点击事件。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力****：**SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：**4.1.0(11)

#### onClickLoginWithHuaweiIDButton

onClickLoginWithHuaweiIDButton(callback: AsyncCallback<HuaweiIDCredential>): LoginPanelController

注册华为账号一键登录结果事件。使用callback异步回调。可在回调方法中处理登录响应结果。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力****：**SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：**4.1.0(11)

**参数：**

参数名

类型

必填

说明

callback

AsyncCallback<[HuaweiIDCredential](#section1862534912215)>

是

回调函数。当注册华为账号登录返回结果成功，err为undefined，data为获取到的[HuaweiIDCredential](#section1862534912215)对象；否则为错误对象。

**返回值：**

类型

说明

[LoginPanelController](#section1419019854714)

[LoginPanel](LoginPanel (华为账号Panel登录组件).md)组件控制器可以用来注册组件内部的点击事件或者调用组件提供的方法。

**错误码：**

以下错误码的详细介绍请参见[ArkTS错误码](ArkTS错误码.md)和[账号管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-account)。

错误码ID

错误信息

[401](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal#section401-参数检查失败)

Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.

[1001500001](ArkTS错误码.md#section1581681312511)

Failed to check the fingerprint of the app bundle.

[1001500002](ArkTS错误码.md#section134761318124311)

This error code is reported when a request is already being processed.

[1001500003](ArkTS错误码.md#section116574197436)

The scopes or permissions are not supported.

[1001502001](ArkTS错误码.md#section539558125020)

The user has not logged in with HUAWEI ID.

[1001502002](ArkTS错误码.md#section1393125918588)

The application is not authorized.

[1001502003](ArkTS错误码.md#section289120911112)

Invalid input parameter value.

[1001502005](ArkTS错误码.md#section1281526328)

Network error.

[1001502009](ArkTS错误码.md#section17561151616317)

Internal error.

[1001502012](ArkTS错误码.md#section223413481361)

The user canceled the authorization.

[1001502014](ArkTS错误码.md#section78953611814)

The app does not have the required scopes or permissions.

[12300001](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-account#section12300001-系统服务异常)

System service works abnormally.

[1005300001](ArkTS错误码.md#section54021153246)

The user did not accept the agreement.

#### onClickOptionalLoginButton

onClickOptionalLoginButton(callback: AsyncCallback<void>): LoginPanelController

注册可选登录按钮的点击事件。使用callback异步回调。用于应用跳转其他登录方式。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力****：**SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：**4.1.0(11)

**参数：**

参数名

类型

必填

说明

callback

AsyncCallback<void>

是

回调函数。当用户点击可选登录按钮操作成功，err为undefined，否则为错误对象。

**返回值：**

类型

说明

[LoginPanelController](#section1419019854714)

[LoginPanel](LoginPanel (华为账号Panel登录组件).md)组件控制器可以用来注册组件内部的点击事件或者调用组件提供的方法。

#### onClickOptionalLoginIcon

onClickOptionalLoginIcon(callback: AsyncCallback<string>): LoginPanelController

注册可选登录Icon的点击事件。使用callback异步回调。用于应用跳转其他登录方式。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力****：**SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：**5.0.0(12)

**参数：**

参数名

类型

必填

说明

callback

AsyncCallback<string>

是

回调函数。当用户点击[LoginIcon](#section1248254952118)操作成功，err为undefined，data为获取到的[LoginIcon](#section1248254952118)的tag；否则为错误对象。

**返回值：**

类型

说明

[LoginPanelController](#section1419019854714)

[LoginPanel](LoginPanel (华为账号Panel登录组件).md)组件控制器可以用来注册组件内部的点击事件或者调用组件提供的方法。

#### onClickPrivacyText

onClickPrivacyText(callback: AsyncCallback<string>): LoginPanelController

注册隐私内容为富文本的点击事件。使用callback异步回调。应用可以让用户点击跳转到应用的隐私协议。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力****：**SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：**4.1.0(11)

**参数：**

参数名

类型

必填

说明

callback

AsyncCallback<string>

是

回调函数。当注册隐私内容为富文本的点击操作成功时，err为undefined，data为获取到的[PrivacyText](#section7272252193)的tag；否则为错误对象。

**返回值：**

类型

说明

[LoginPanelController](#section1419019854714)

[LoginPanel](LoginPanel (华为账号Panel登录组件).md)组件控制器可以用来注册组件内部的点击事件或者调用组件提供的方法。

#### onChangeAgreementStatus

onChangeAgreementStatus(callback: AsyncCallback<AgreementStatus>): LoginPanelController

注册用户协议状态变化的事件。使用callback异步回调。当用户同意或者取消同意协议成功时，通过[setAgreementStatus](#section20291953195314)设置用户同意或取消同意的协议状态。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力****：**SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：**5.0.0(12)

**参数：**

参数名

类型

必填

说明

callback

AsyncCallback<[AgreementStatus](#section183397331373)>

是

回调函数。当用户同意或者取消同意协议成功，err为undefined，data为获取到的[AgreementStatus](#section183397331373)；否则为错误对象。

**返回值：**

类型

说明

[LoginPanelController](#section1419019854714)

[LoginPanel](LoginPanel (华为账号Panel登录组件).md)组件控制器可以用来注册组件内部的点击事件或者调用组件提供的方法。

#### setAgreementStatus

setAgreementStatus(agreementStatus: AgreementStatus): LoginPanelController

设置用户协议的状态。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力****：**SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：**5.0.0(12)

**参数：**

参数名

类型

必填

说明

agreementStatus

[AgreementStatus](#section183397331373)

是

开发者如果使用自定义协议页面，需要先设置agreementStatus为NOT_ACCEPTED，当用户同意协议后设置为ACCEPTED。

**返回值：**

类型

说明

[LoginPanelController](#section1419019854714)

[LoginPanel](LoginPanel (华为账号Panel登录组件).md)组件控制器可以用来注册组件内部的点击事件或者调用组件提供的方法。

#### setShowAgreementForOptionalLogin

setShowAgreementForOptionalLogin(): LoginPanelController

设置用户点击其他方式登录选项时展示隐私协议弹框。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力****：**SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：**5.0.0(12)

**返回值：**

类型

说明

[LoginPanelController](#section1419019854714)

[LoginPanel](LoginPanel (华为账号Panel登录组件).md)组件控制器可以用来注册组件内部的点击事件或者调用组件提供的方法。

#### onClickEvent

onClickEvent(callback: AsyncCallback<ClickEvent>): LoginPanelController

注册华为账号登录按钮的点击事件。使用callback异步回调。应用可以在用户点击华为账号登录按钮后收到回调，可用于记录运营事件等场景。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力****：**SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：**5.0.0(12)

**参数：**

参数名

类型

必填

说明

callback

AsyncCallback<[ClickEvent](#section967316103272)>

是

回调函数。当用户点击华为账号登录按钮时，err为undefined，data为获取到的[ClickEvent](#section967316103272)；否则为错误对象。

**返回值：**

类型

说明

[LoginPanelController](#section1419019854714)

[LoginPanel](LoginPanel (华为账号Panel登录组件).md)组件控制器可以用来注册组件内部的点击事件或者调用组件提供的方法。

#### onClickCloseButton

onClickCloseButton(callback: AsyncCallback<void>): LoginPanelController

注册关闭按钮的点击事件或用户侧滑返回事件。使用callback异步回调。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力****：**SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：**4.1.0(11)

**参数：**

参数名

类型

必填

说明

callback

AsyncCallback<void>

是

回调函数。当注册关闭按钮的点击操作或侧滑返回成功，err为undefined，否则为错误对象。

**返回值：**

类型

说明

[LoginPanelController](#section1419019854714)

[LoginPanel](LoginPanel (华为账号Panel登录组件).md)组件控制器可以用来注册组件内部的点击事件或者调用组件提供的方法。

**示例：**

```ets
import { LoginPanel, loginComponentManager } from '@kit.AccountKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct PreviewLoginPanelPage {
  // 是否展示LoginPanel组件
  @State show: boolean = true;
  // 定义LoginPanel展示的隐私文本
  privacyText: loginComponentManager.PrivacyText[] = [{
    text: '已阅读并同意',
    type: loginComponentManager.TextType.PLAIN_TEXT
  }, {
    text: '《用户服务协议》',
    tag: '用户服务协议',
    type: loginComponentManager.TextType.RICH_TEXT
  }, {
    text: '《隐私协议》',
    tag: '隐私协议',
    type: loginComponentManager.TextType.RICH_TEXT
  }, {
    text: '和',
    type: loginComponentManager.TextType.PLAIN_TEXT
  }, {
    text: '《华为账号用户认证协议》',
    tag: '华为账号用户认证协议',
    type: loginComponentManager.TextType.RICH_TEXT
  }];
  // 定义LoginPanel展示的其他方式登录Icon
  iconArray: loginComponentManager.LoginIcon[] = [{
    // 此处为示例资源，开发者可使用应用图标进行替换，以保证正常编译运行
    icon: $r('app.media.app_icon'),
    tag: '其他方式登录'
  }];
  // 构造LoginPanel组件的控制器
  controller: loginComponentManager.LoginPanelController = new loginComponentManager.LoginPanelController()
    // 当登录类型不是QUICK_LOGIN且未设置协议时，如果需要展示自定义协议弹框，需要设置协议状态为NOT_ACCEPTED
    .setAgreementStatus(loginComponentManager.AgreementStatus.NOT_ACCEPTED)
    // 用户点击其他方式登录展示隐私协议弹框
    .setShowAgreementForOptionalLogin()
    .onClickLoginWithHuaweiIDButton((error: BusinessError, response: loginComponentManager.HuaweiIDCredential) => {
      hilog.info(0x0000, 'testTag', 'onClickLoginWithHuaweiIDButton');
      if (error) {
        this.dealAllError(error);
        return;
      }
      if (response) {
        // 获取到Authorization Code后，传给应用服务端
        const authorizationCode = response.authorizationCode;
        hilog.info(0x0000, 'testTag', 'Succeeded in getting response.');
        this.show = false;
        return;
      }
    })
    .onClickOptionalLoginButton(() => {
      hilog.info(0x0000, 'testTag', 'onClickOptionalLoginButton');
      this.show = false;
    })
    .onClickOptionalLoginIcon((error: BusinessError, tag: string) => {
      if (error) {
        this.dealAllError(error);
        return;
      }
      hilog.info(0x0000, 'testTag', `onClickOptionalLoginIcon tag: ${tag}`);
      this.show = false;
    })
    .onClickPrivacyText((error: BusinessError, tag: string) => {
      if (error) {
        this.dealAllError(error);
        return;
      }
      // 应用需要实现协议页面的跳转逻辑
      hilog.info(0x0000, 'testTag', `onClickPrivacyText tag: ${tag}`);
    })
    .onClickCloseButton(() => {
      hilog.info(0x0000, 'testTag', 'onClickCloseButton.');
      this.show = false;
    })
    .onChangeAgreementStatus((error: BusinessError, agreementStatus: loginComponentManager.AgreementStatus) => {
      if (error) {
        this.dealAllError(error);
        return;
      }
      hilog.info(0x0000, 'testTag', `onChangeAgreementStatus agreementStatus: ${agreementStatus}`);
    })
    .onClickEvent((error: BusinessError, clickEvent: loginComponentManager.ClickEvent) => {
      if (error) {
        this.dealAllError(error);
        return;
      }
      hilog.info(0x0000, 'testTag', `onClickEvent clickEvent: ${clickEvent}`);
    });

  // 错误处理
  dealAllError(error: BusinessError): void {
    hilog.error(0x0000, 'testTag', `Failed to login, errorCode=${error.code}, errorMsg=${error.message}`);
    // 在应用登录涉及UI交互场景下，建议按照如下错误码指导提示用户
    if (error.code === ErrorCode.ERROR_CODE_LOGIN_OUT) {
      // 用户未登录华为账号，请登录华为账号并重试或者尝试使用其他方式登录
    } else if (error.code === ErrorCode.ERROR_CODE_NETWORK_ERROR) {
      // 网络异常，请检查当前网络状态并重试或者尝试使用其他方式登录
    } else if (error.code === ErrorCode.ERROR_CODE_INTERNAL_ERROR) {
      // 登录失败，请尝试使用其他方式登录
    } else if (error.code === ErrorCode.ERROR_CODE_USER_CANCEL) {
      // 用户取消授权
    } else if (error.code === ErrorCode.ERROR_CODE_SYSTEM_SERVICE) {
      // 系统服务异常，请稍后重试或者尝试使用其他方式登录
    } else if (error.code === ErrorCode.ERROR_CODE_REQUEST_REFUSE) {
      // 重复请求，应用无需处理
    } else if (error.code === ErrorCode.ERROR_CODE_AGREEMENT_STATUS_NOT_ACCEPTED) {
      // 用户未同意协议
    } else {
      // 应用登录失败，请尝试使用其他方式登录
    }
  }

  build() {
    if (this.show) {
      Stack() {
        LoginPanel({
          show: this.show,
          params: {
            appInfo: {
              // 此处为示例资源，开发者可使用应用图标进行替换，以保证正常编译运行
              appIcon: $r('app.media.app_icon'),
              appName: '应用名称',
            },
            privacyText: this.privacyText,
            // 参考华为账号开发指南获取匿名手机号
            anonymousPhoneNumber: '139******99',
            loginType: loginComponentManager.LoginType.QUICK_LOGIN,
            // optionalLoginAreaAttr和optionalLoginButtonAttr同时存在时优先展示optionalLoginAreaAttr
            optionalLoginAreaAttr: { iconArray: this.iconArray },
            optionalLoginButtonAttr: { text: '其他方式登录' }
          },
          controller: this.controller
        })
      }
      .height('100%')
      .width('100%')
    }
  }
}

export enum ErrorCode {
  // 账号未登录
  ERROR_CODE_LOGIN_OUT = 1001502001,
  // 网络错误
  ERROR_CODE_NETWORK_ERROR = 1001502005,
  // 内部错误
  ERROR_CODE_INTERNAL_ERROR = 1001502009,
  // 用户取消授权
  ERROR_CODE_USER_CANCEL = 1001502012,
  // 系统服务异常
  ERROR_CODE_SYSTEM_SERVICE = 12300001,
  // 用户未同意用户协议
  ERROR_CODE_AGREEMENT_STATUS_NOT_ACCEPTED = 1005300001,
  // 重复请求
  ERROR_CODE_REQUEST_REFUSE = 1001500002
}
```

#### LoginWithHuaweiIDButtonParams

该接口定义了华为账号登录按钮的属性。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力****：**SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：**4.1.0(11)

名称

类型

只读

可选

说明

style

[Style](#section19823216112610)

否

否

[LoginWithHuaweiIDButton](LoginWithHuaweiIDButton (华为账号Button登录组件).md)组件的样式。

borderRadius

number

否

是

按钮边框圆角半径。

取值范围：[0,+∞)，值小于0时，按0处理。

默认值：height属性取值的一半。

单位：vp。

iconRadius

number

否

是

Icon类型按钮的半径。

取值范围：[0,+∞)，值小于0时，按0处理。

默认值：24。

单位：vp。

supportDarkMode

boolean

否

是

表示按钮的样式是否随系统深浅色模式变化。

true：按钮的样式会随着系统深浅色模式变化。

false：按钮的样式不会随着系统深浅色模式变化。

默认值：true。

loginType

[LoginType](#section79023235528)

否

是

华为账号登录类型。默认值：[LoginType.ID](#section79023235528)。

一键登录请使用[LoginType.QUICK_LOGIN](#section79023235528)。

textAndIconStyle

boolean

否

是

是否展示图文混合样式的华为账号登录按钮。

true：按钮支持Icon和文字混合样式。

false：按钮仅支持文本样式。

默认值：false。

当loginType不等于[LoginType.QUICK_LOGIN](#section79023235528)且style等于[BUTTON_RED](#section19823216112610)、[BUTTON_WHITE](#section19823216112610)、[BUTTON_WHITE_OUTLINE](#section19823216112610)、[BUTTON_BLACK](#section19823216112610)、[BUTTON_GRAY](#section19823216112610)时该参数生效。

**起始版本：**5.0.0(12)

customButtonParams

[CustomButtonParams](#section2938142118617)

否

是

[BUTTON_CUSTOM](#section19823216112610)按钮样式参数。

**起始版本：**5.0.0(12)

verifyPhoneNumber

boolean

否

是

华为账号用户在过去90天内未进行短信验证，是否拉起Account Kit提供的短信验证码页面。

true：拉起Account Kit提供的短信验证码页面。

false：不拉起Account Kit提供的短信验证码页面。需要应用验证手机号时效性。

默认值：true。

**起始版本：**5.0.0(12)

extraStyle

[ExtraStyle](#section87572031102713)

否

是

如果应用想使用华为账号提供的固定样式之外的效果，可使用此接口自定义按钮样式。

**起始版本：**5.0.0(12)

loginButtonTextType

[LoginButtonTextType](#section1645283915811)

否

是

当loginType为[LoginType.QUICK_LOGIN](#section79023235528)时，可传入此参数，控制按钮文本内容显示。

默认值：[LoginButtonTextType.QUICK_LOGIN](#section1645283915811)

- 当该参数为[LoginButtonTextType.QUICK_LOGIN](#section1645283915811)时，按钮文本内容显示“华为账号一键登录”。
- 当该参数为[LoginButtonTextType.QUICK_REGISTRATION](#section1645283915811)时，按钮文本内容显示“华为账号一键注册”。

**起始版本：**5.0.0(12)

riskLevel

boolean

否

是

是否需要获取华为账号用户风险等级。

仅登录类型为[LoginType.QUICK_LOGIN](#section79023235528)时需要设置该参数。

true：需要[获取用户风险等级](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-get-risklevel-byquicklogin)。

false：不获取用户风险等级。

默认值：false。

**起始版本：**5.1.0(18)

securityVerification

boolean

否

是

用户开启华为账号一键登录增强身份验证后，应用会在登录过程中通过华为账号使用生物识别或短信进行身份验证。如果需要获取用户一键登录增强身份验证的开关状态，需设置该字段为false。

仅登录类型为[LoginType.QUICK_LOGIN](#section79023235528)时需要设置该参数。

true：响应结果HuaweiIDCredential将不会返回 [enableSecurityVerification](#section1862534912215)。

false：响应结果HuaweiIDCredential将返回 [enableSecurityVerification](#section1862534912215)。

默认值：true。

**起始版本：**6.0.0(20)

#### Style

该枚举表示华为账号登录按钮的类型。

如果以下华为账号登录按钮的样式仍不能满足开发需求，请参见[华为账号开放登录设计指南](https://developer.huawei.com/consumer/cn/doc/design-guides/id-0000001880001344)。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力****：**SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：**4.1.0(11)

名称

值

说明

BUTTON_RED

0

红色背景白色文字按钮，字体大小会随着按钮的宽高自适应，最小为9号，最大为16号。

根据开发场景从以下链接中选择其中一个规范查看。

请参见[【华为账号一键登录】按钮](https://developer.huawei.com/consumer/cn/doc/design-guides/id-0000001880001344#section41792374210)视觉规范。

请参见[【华为账号登录】按钮](https://developer.huawei.com/consumer/cn/doc/design-guides/id-0000001880001344#section2624430102713)视觉规范。

BUTTON_WHITE

1

白色背景黑色文字按钮，字体大小会随着按钮的宽高自适应，最小为9号，最大为16号。

根据开发场景从以下链接中选择其中一个规范查看。

请参见[【华为账号一键登录】按钮](https://developer.huawei.com/consumer/cn/doc/design-guides/id-0000001880001344#section41792374210)视觉规范。

请参见[【华为账号登录】按钮](https://developer.huawei.com/consumer/cn/doc/design-guides/id-0000001880001344#section2624430102713)视觉规范。

BUTTON_WHITE_OUTLINE

2

白色背景黑色文字带边框按钮，字体大小会随着按钮的宽高自适应，最小为9号，最大为16号。

根据开发场景从以下链接中选择其中一个规范查看。

请参见[【华为账号一键登录】按钮](https://developer.huawei.com/consumer/cn/doc/design-guides/id-0000001880001344#section41792374210)视觉规范。

请参见[【华为账号登录】按钮](https://developer.huawei.com/consumer/cn/doc/design-guides/id-0000001880001344#section2624430102713)视觉规范。

BUTTON_BLACK

3

黑色背景白色文字按钮，字体大小会随着按钮的宽高自适应，最小为9号，最大为16号。

根据开发场景从以下链接中选择其中一个规范查看。

请参见[【华为账号一键登录】按钮](https://developer.huawei.com/consumer/cn/doc/design-guides/id-0000001880001344#section41792374210)视觉规范。

请参见[【华为账号登录】按钮](https://developer.huawei.com/consumer/cn/doc/design-guides/id-0000001880001344#section2624430102713)视觉规范。

ICON_RED

4

红色背景白色Icon按钮。

请参见[【华为账号登录】按钮](https://developer.huawei.com/consumer/cn/doc/design-guides/id-0000001880001344#section2624430102713)视觉规范。

ICON_WHITE

5

白色背景红色Icon按钮。

请参见[【华为账号登录】按钮](https://developer.huawei.com/consumer/cn/doc/design-guides/id-0000001880001344#section2624430102713)视觉规范。

ICON_WHITE_OUTLINE

6

白色背景红色Icon带边框按钮。

请参见[【华为账号登录】按钮](https://developer.huawei.com/consumer/cn/doc/design-guides/id-0000001880001344#section2624430102713)视觉规范。

ICON_BLACK

7

黑色背景白色Icon按钮。

请参见[【华为账号登录】按钮](https://developer.huawei.com/consumer/cn/doc/design-guides/id-0000001880001344#section2624430102713)视觉规范。

ICON_GRAY

8

灰色背景红色Icon按钮。

请参见[【华为账号登录】按钮](https://developer.huawei.com/consumer/cn/doc/design-guides/id-0000001880001344#section2624430102713)视觉规范。

**起始版本：**5.0.0(12)

BUTTON_GRAY

9

灰色背景黑色文字按钮，字体大小会随着按钮的宽高自适应，最小为9号，最大为16号。

根据开发场景从以下链接中选择其中一个规范查看。

请参见[【华为账号一键登录】按钮](https://developer.huawei.com/consumer/cn/doc/design-guides/id-0000001880001344#section41792374210)视觉规范。

请参见[【华为账号登录】按钮](https://developer.huawei.com/consumer/cn/doc/design-guides/id-0000001880001344#section2624430102713)视觉规范。

**起始版本：**5.0.0(12)

BUTTON_CUSTOM

10

支持自定义背景颜色、文字颜色及圆角等效果的按钮，字体大小会随着按钮的宽高自适应，最小为9号，最大为16号。开发者可以通过[CustomButtonParams](#section2938142118617)设置按钮自定义的参数，且需要自行适配深浅色模式。

根据开发场景从以下链接中选择其中一个规范查看。

请参见[【华为账号一键登录】按钮](https://developer.huawei.com/consumer/cn/doc/design-guides/id-0000001880001344#section41792374210)视觉规范。

请参见[【华为账号登录】按钮](https://developer.huawei.com/consumer/cn/doc/design-guides/id-0000001880001344#section2624430102713)视觉规范。

 须知：

此类型仅支持纯文本按钮。

**起始版本：**5.0.0(12)

#### LoginButtonTextType

该枚举表示华为账号一键登录按钮显示的文本内容。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力****：**SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：**5.0.0(12)

名称

值

说明

QUICK_LOGIN

0

华为账号一键登录按钮文本内容显示为“华为账号一键登录”。用于应用账号登录场景。

QUICK_REGISTRATION

1

华为账号一键登录按钮文本内容显示为“华为账号一键注册”。用于应用账号注册场景。

#### CustomButtonParams

该接口定义了[BUTTON_CUSTOM](#section19823216112610)按钮的参数。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力****：**SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：**5.0.0(12)

名称

类型

只读

可选

说明

fontColor

[FontColor](#section1660816591873)

否

是

[LoginWithHuaweiIDButton](LoginWithHuaweiIDButton (华为账号Button登录组件).md)按钮文字颜色。

默认值：[FontColor](#section1660816591873).WHITE

backgroundColor

[ResourceColor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resourcecolor)

否

是

[LoginWithHuaweiIDButton](LoginWithHuaweiIDButton (华为账号Button登录组件).md)按钮背景颜色。

默认值：Red

#### FontColor

该枚举定义了[BUTTON_CUSTOM](#section19823216112610)按钮可以使用的文字颜色。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力****：**SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：**5.0.0(12)

名称

值

说明

WHITE

0

华为账号登录按钮文字颜色为白色。

BLACK

1

华为账号登录按钮文字颜色为黑色。

#### ExtraStyle

该接口定义了华为账号登录按钮拓展参数。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力****：**SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：**5.0.0(12)

名称

类型

只读

可选

说明

buttonStyle

[ButtonStyle](#section4742141694510)

否

是

华为账号登录按钮提供给开发者自定义按钮样式，可动态设置一些属性。

customButtonStateStyles

[StateStyles](#section885411463712)

否

是

华为账号登录按钮提供给开发者自定义按钮多态样式。仅对[BUTTON_CUSTOM](#section19823216112610)类型按钮生效。

textAndIconButtonParams

[TextAndIconButtonParams](#section68654575117)

否

是

图文混合样式按钮下设置该参数可以控制图文间距。

iconButtonParams

[IconButtonParams](#section474074855419)

否

是

纯图标按钮下设置该参数可控制图标按钮内图标的显示半径。

#### RadialGradient

该接口定义了华为账号登录按钮径向渐变的样式。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力****：**SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：**5.0.0(12)

名称

类型

只读

可选

说明

center

[[Length](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#length), [Length](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#length)]

否

否

径向渐变的中心点，即相对于当前组件左上角的坐标。

radius

number | string

否

否

径向渐变的半径。

取值范围：[0,+∞)。

值小于0时，按0处理。

colors

Array<[[ResourceColor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resourcecolor), number]>

否

否

指定某百分比位置处的渐变色颜色，设置非法颜色直接跳过。

不设置则无效果。

repeating

boolean

否

是

为渐变的颜色重复着色。

true：重复着色。

false：不重复着色。

默认值：false。

#### SweepGradient

该接口定义了华为账号登录按钮角度渐变的样式。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力****：**SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：**5.0.0(12)

名称

类型

只读

可选

说明

center

[[Length](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#length), [Length](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#length)]

否

否

角度渐变的中心点，即相对于当前组件左上角的坐标。

start

number | string

否

是

角度渐变的起点。

当start的数据类型为number时，默认值是0，设置为小于0的值时，按值为0处理，设置为大于360的值时，按值为360处理。

当start的数据类型为string时，合法的取值为纯数字或纯数字后带"deg"(度)、"rad"(弧度)、"grad"(梯度)、"turn"(圈)单位，例如："90"、 "90deg"、"1.57rad"。

end

number | string

否

是

角度渐变的终点。

当end的数据类型为number时，默认值是0，设置为小于0的值时，按值为0处理，设置为大于360的值时，按值为360处理。

当end的数据类型为string时，合法的取值为纯数字或纯数字后带"deg"(度)、"rad"(弧度)、"grad"(梯度)、"turn"(圈)单位，例如："90"、 "90deg"、"1.57rad"。

rotation

number | string

否

是

角度渐变的旋转角度。

当rotation的数据类型为number时，默认值是0，设置为小于0的值时，按值为0处理，设置为大于360的值时，按值为360处理。

当rotation的数据类型为string时，合法的取值为纯数字或纯数字后带"deg"(度)、"rad"(弧度)、"grad"(梯度)、"turn"(圈)单位，例如："90"、 "90deg"、"1.57rad"。

colors

Array<[[ResourceColor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resourcecolor), number]>

否

否

指定某百分比位置处的渐变色颜色，设置非法颜色直接跳过。

不设置则无效果。

repeating

boolean

否

是

为渐变的颜色重复着色。

true：重复着色。

false：不重复着色。

默认值：false。

#### ButtonStyle

该类定义了华为账号登录按钮的通用属性。通过new loginComponentManager.ButtonStyle()构造实例。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力****：**SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：**5.0.0(12)

#### buttonSize

buttonSize(value: ButtonSize): ButtonStyle

调用该方法设置华为账号登录按钮的宽高尺寸。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力****：**SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：**5.0.0(12)

**参数：**

参数名

类型

必填

说明

value

[ButtonSize](#section169691441164919)

是

当按钮类型为纯图标按钮时，按钮的宽度和高度相等，取value.width和value.height的非undefined的最小值，如果value.width和value.height都为undefined取[LoginWithHuaweiIDButtonParams](#section4717249182518)的iconRadius的2倍值，如果iconRadius也是undefined则取默认值48vp；

当按钮类型为非纯图标按钮时，按钮的宽度和高度分别取value.width和value.height，当value.width或者value.height为undefined，按钮宽度或高度取父布局宽高。

 须知：

当设置该属性的宽高，父组件的宽高值应该大于等于该属性的宽高值。

**返回值：**

类型

说明

[ButtonStyle](#section4742141694510)

定义了华为账号登录按钮的通用属性。

#### fontSize

fontSize(value: Length): ButtonStyle

调用该方法设置华为账号登录按钮的字号。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力****：**SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：**5.0.0(12)

**参数：**

参数名

类型

必填

说明

value

[Length](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#length)

是

当按钮为图文按钮或文本按钮时，设置按钮文字的字号。根据[华为账号开放登录视觉规范](https://developer.huawei.com/consumer/cn/doc/design-guides/id-0000001880001344#section61791745172816)，设置范围建议在按钮高度的30%~50%之间。

如果没传此值，字号大小在9~16vp之间随按钮宽度自适应。

**返回值：**

类型

说明

[ButtonStyle](#section4742141694510)

定义了华为账号登录按钮的通用属性。

#### fontColor

fontColor(value: ResourceColor | FontColor): ButtonStyle

调用该方法设置华为账号登录按钮的文字颜色。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力****：**SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：**5.0.0(12)

**参数：**

参数名

类型

必填

说明

value

[ResourceColor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resourcecolor) | [FontColor](#section1660816591873)

是

当按钮类型为[BUTTON_CUSTOM](#section19823216112610)时，此参数可设置按钮文字颜色。当已经设置[CustomButtonParams](#section2938142118617)的fontColor属性时，优先取此参数值。

不设置则为黑色。

**返回值：**

类型

说明

[ButtonStyle](#section4742141694510)

定义了华为账号登录按钮的通用属性。

#### fontWeight

fontWeight(value: string | number | FontWeight): ButtonStyle

调用该方法设置华为账号登录按钮的文字字重。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力****：**SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：**5.0.0(12)

**参数：**

参数名

类型

必填

说明

value

string | number | [FontWeight](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-appendix-enums#fontweight)

是

当按钮类型为[BUTTON_CUSTOM](#section19823216112610)时，此参数可设置按钮文字字重。number类型取值[100, 900]，取值间隔为100，取值越大字体越粗，当超出边界值时取值为400。string类型仅支持number类型取值的字符串形式，例如"400"，以及"bold"、"bolder"、"lighter"、"regular"、"medium"，分别对应FontWeight中相应的枚举值。

默认字重为FontWeight.Medium，对应的number值为500。

**返回值：**

类型

说明

[ButtonStyle](#section4742141694510)

定义了华为账号登录按钮的通用属性。

#### fontFamily

fontFamily(value: ResourceStr): ButtonStyle

调用该方法设置华为账号登录按钮的文字字体。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力****：**SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：**5.0.0(12)

**参数：**

参数名

类型

必填

说明

value

[ResourceStr](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resourcestr)

是

当按钮类型为[BUTTON_CUSTOM](#section19823216112610)时，此参数可设置按钮文字字体。

默认字体'HarmonyOS Sans'。

应用当前支持'HarmonyOS Sans'字体和[注册自定义字体](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-font)。

**返回值：**

类型

说明

[ButtonStyle](#section4742141694510)

定义了华为账号登录按钮的通用属性。

#### backgroundColor

backgroundColor(value: ResourceColor): ButtonStyle

调用该方法设置华为账号登录按钮的背景颜色。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力****：**SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：**5.0.0(12)

**参数：**

参数名

类型

必填

说明

value

[ResourceColor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resourcecolor)

是

当按钮类型为[BUTTON_CUSTOM](#section19823216112610)时，此参数可设置按钮背景颜色。

当已经设置[CustomButtonParams](#section2938142118617)的backgroundColor属性时，优先取此参数值。

不设置则为 Red 红色背景。

**返回值：**

类型

说明

[ButtonStyle](#section4742141694510)

定义了华为账号登录按钮的通用属性。

#### backgroundEffect

backgroundEffect(value: BackgroundEffectOptions): ButtonStyle

调用该方法设置华为账号登录按钮的背景属性。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力****：**SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：**5.0.0(12)

**参数：**

参数名

类型

必填

说明

value

[BackgroundEffectOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-background#backgroundeffectoptions11)

是

当按钮类型为[BUTTON_CUSTOM](#section19823216112610)时，此参数可设置按钮背景属性，包括饱和度，亮度，颜色。

不设置则无效果。

**返回值：**

类型

说明

[ButtonStyle](#section4742141694510)

定义了华为账号登录按钮的通用属性。

#### backgroundBrightness

backgroundBrightness(value: BackgroundBrightnessOptions): ButtonStyle

调用该方法设置华为账号登录按钮的背景提亮效果。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力****：**SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：**5.0.0(12)

**参数：**

参数名

类型

必填

说明

value

[BackgroundBrightnessOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-background#backgroundbrightnessoptions12对象说明)

是

当按钮类型为[BUTTON_CUSTOM](#section19823216112610)时，此参数可设置按钮背景提亮效果，包括：亮度变化速率，提亮程度。

不设置则无效果。

**返回值：**

类型

说明

[ButtonStyle](#section4742141694510)

定义了华为账号登录按钮的通用属性。

#### linearGradient

linearGradient(value: LinearGradient): ButtonStyle

调用该方法设置华为账号登录按钮的背景颜色线性渐变效果。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力****：**SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：**5.0.0(12)

**参数：**

参数名

类型

必填

说明

value

[LinearGradient](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-border-image#lineargradient)

是

当按钮类型为[BUTTON_CUSTOM](#section19823216112610)时，此参数可设置按钮背景颜色线性渐变效果，不设置则无效果。

 须知：

使用此属性时，按钮不能有背景色，否则按钮边缘会出现锯齿毛边，需把按钮背景色设置为透明色，如backgroundColor(Color.Transparent)。

**返回值：**

类型

说明

[ButtonStyle](#section4742141694510)

定义了华为账号登录按钮的通用属性。

#### sweepGradient

sweepGradient(value: SweepGradient): ButtonStyle

调用该方法设置华为账号登录按钮的背景颜色角度渐变效果。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力****：**SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：**5.0.0(12)

**参数：**

参数名

类型

必填

说明

value

[SweepGradient](#section4541924134916)

是

当按钮类型为[BUTTON_CUSTOM](#section19823216112610)时，此参数可设置按钮背景颜色角度渐变效果。

不设置则无效果。

 须知：

使用此属性时，按钮不能有背景色，否则按钮边缘会出现锯齿毛边，需把按钮背景色设置为透明色，如backgroundColor(Color.Transparent)。

**返回值：**

类型

说明

[ButtonStyle](#section4742141694510)

定义了华为账号登录按钮的通用属性。

#### radialGradient

radialGradient(value: RadialGradient): ButtonStyle

调用该方法设置华为账号登录按钮的背景颜色径向渐变效果。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力****：**SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：**5.0.0(12)

**参数：**

参数名

类型

必填

说明

value

[RadialGradient](#section17457938194018)

是

当按钮类型为[BUTTON_CUSTOM](#section19823216112610)时，此参数可设置按钮背景颜色径向渐变效果。

不设置则无效果。

 须知：

使用此属性时，按钮不能有背景色，否则按钮边缘会出现锯齿毛边，需把按钮背景色设置为透明色，如backgroundColor(Color.Transparent)。

**返回值：**

类型

说明

[ButtonStyle](#section4742141694510)

定义了华为账号登录按钮的通用属性。

#### shadow

shadow(value: ShadowOptions | ShadowStyle): ButtonStyle

调用该方法设置华为账号登录按钮的阴影效果。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力****：**SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：**5.0.0(12)

**参数：**

参数名

类型

必填

说明

value

[ShadowOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-image-effect#shadowoptions对象说明) | [ShadowStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-image-effect#shadowstyle10枚举说明)

是

当按钮类型为[BUTTON_CUSTOM](#section19823216112610)时，此参数可设置按钮阴影效果，不设置则无效果。

**返回值：**

类型

说明

[ButtonStyle](#section4742141694510)

定义了华为账号登录按钮的通用属性。

#### opacity

opacity(value: number | Resource): ButtonStyle

调用该方法设置华为账号登录按钮的不透明度。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力****：**SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：**5.0.0(12)

**参数：**

参数名

类型

必填

说明

value

number | [Resource](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resource)

是

元素的不透明度，取值范围为0到1，1表示不透明，0表示完全透明, 达到隐藏组件效果，但是在布局中占位。

默认值：1

当按钮类型为[BUTTON_CUSTOM](#section19823216112610)时，此参数可设置按钮的不透明度。

**返回值：**

类型

说明

[ButtonStyle](#section4742141694510)

定义了华为账号登录按钮的通用属性。

#### border

border(value: BorderOptions): ButtonStyle

调用该方法设置华为账号登录按钮的边框样式。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力****：**SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：**5.0.0(12)

**参数：**

参数名

类型

必填

说明

value

[BorderOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#borderoptions)

是

当按钮类型为[BUTTON_CUSTOM](#section19823216112610)时，此参数可设置按钮的边框样式，不设置则无效果。

 须知：

设置内边框需要预留充足的空间展示按钮，请确保按钮父组件宽高大于按钮本身。

**返回值：**

类型

说明

[ButtonStyle](#section4742141694510)

定义了华为账号登录按钮的通用属性。

#### borderImage

borderImage(value: BorderImageOption): ButtonStyle

调用该方法设置华为账号登录按钮的图片边框样式。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力****：**SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：**5.0.0(12)

**参数：**

参数名

类型

必填

说明

value

[BorderImageOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-border-image#borderimageoption对象说明)

是

当按钮类型为[BUTTON_CUSTOM](#section19823216112610)时，此参数可设置按钮的图片边框样式，不设置则无效果。

**返回值：**

类型

说明

[ButtonStyle](#section4742141694510)

定义了华为账号登录按钮的通用属性。

#### outline

outline(value: OutlineOptions): ButtonStyle

调用该方法设置华为账号登录按钮的外描边样式。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力****：**SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：**5.0.0(12)

**参数：**

参数名

类型

必填

说明

value

[OutlineOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#outlineoptions11对象说明)

是

当按钮类型为[BUTTON_CUSTOM](#section19823216112610)时，此参数可设置按钮的外描边样式，不设置则无效果。

**返回值：**

类型

说明

[ButtonStyle](#section4742141694510)

定义了华为账号登录按钮的通用属性。

#### hoverEffect

hoverEffect(value: HoverEffect): ButtonStyle

调用该方法设置华为账号登录按钮的悬浮态效果。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力****：**SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：**5.0.0(12)

**参数：**

参数名

类型

必填

说明

value

[HoverEffect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-appendix-enums#hovereffect8)

是

当按钮类型为[BUTTON_CUSTOM](#section19823216112610)时，此参数可设置按钮的悬浮态效果，不设置则为默认效果。

**返回值：**

类型

说明

[ButtonStyle](#section4742141694510)

定义了华为账号登录按钮的通用属性。

#### clickEffect

clickEffect(value: ClickEffect): ButtonStyle

调用该方法设置华为账号登录按钮的点击回弹效果。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力****：**SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：**5.0.0(12)

**参数：**

参数名

类型

必填

说明

value

[ClickEffect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-click-effect#clickeffect对象说明)

是

当按钮类型为[BUTTON_CUSTOM](#section19823216112610)时，此参数可设置按钮的点击回弹效果，不设置则无效果。

**返回值：**

类型

说明

[ButtonStyle](#section4742141694510)

定义了华为账号登录按钮的通用属性。

#### loadingStyle

loadingStyle(value: LoadingStyle): ButtonStyle

调用该方法设置华为账号登录按钮在登录过程中是否显示加载态。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力****：**SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：**5.0.0(12)

**参数：**

参数名

类型

必填

说明

value

[LoadingStyle](#section1075651914820)

是

此参数可设置按钮在登录过程中是否显示加载态，

默认不显示加载态。

 须知：

纯图标按钮不支持设置加载态，此参数不生效。

**返回值：**

类型

说明

[ButtonStyle](#section4742141694510)

定义了华为账号登录按钮的通用属性。

#### ButtonSize

该接口定义了华为账号登录按钮的尺寸参数。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力****：**SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：**5.0.0(12)

名称

类型

只读

可选

说明

width

[Length](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#length)

否

是

设置华为账号登录按钮宽度。

height

[Length](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#length)

否

是

设置华为账号登录按钮高度。

#### LoadingStyle

该接口定义了华为账号登录按钮在登录过程中是否展示加载态。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力****：**SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：**5.0.0(12)

名称

类型

只读

可选

说明

show

boolean

否

是

设置华为账号登录按钮在登录过程中是否展示加载态。

true：展示登录按钮加载态

false：不展示登录按钮加载态

默认值：false

#### TextAndIconButtonParams

该接口定义了华为账号登录按钮为图文按钮时的图文间距。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力****：**SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：**5.0.0(12)

名称

类型

只读

可选

说明

textAndIconMargin

number

否

是

设置华为账号登录按钮为图文按钮时的图文间距。默认值：8vp，取值范围：4~16vp。当小于4vp时取值为4vp，当大于16vp时取值为16vp。

#### IconButtonParams

该接口定义了华为账号登录按钮为纯图标按钮时的华为图标的半径。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力****：**SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：**5.0.0(12)

名称

类型

只读

可选

说明

logoRadius

number

否

是

设置华为账号登录按钮为纯图标按钮时的华为图标的半径。

默认值：14vp，最小值：8vp。取值范围：按钮高度的20%~32%。当小于20%时取值为20%，当大于32%时取值为32%。

#### StateStyles

该接口定义了华为账号登录按钮的多态样式。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力****：**SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：**5.0.0(12)

名称

类型

只读

可选

说明

normal

[ButtonStyle](#section4742141694510)

否

是

登录按钮正常态的通用样式。

pressed

[ButtonStyle](#section4742141694510)

否

是

登录按钮按压态的通用样式。

disabled

[ButtonStyle](#section4742141694510)

否

是

登录按钮不可点击态的通用样式。

focused

[ButtonStyle](#section4742141694510)

否

是

登录按钮聚焦态的通用样式。

#### LoginWithHuaweiIDButtonController

[LoginWithHuaweiIDButton](LoginWithHuaweiIDButton (华为账号Button登录组件).md#section1624716107193)组件控制器，用来回调组件内部的点击事件。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力****：**SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：**4.1.0(11)

#### setAgreementStatus

setAgreementStatus(agreementStatus: AgreementStatus): LoginWithHuaweiIDButtonController

设置用户协议的状态。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力****：**SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：**5.0.0(12)

**参数：**

参数名

类型

必填

说明

agreementStatus

[AgreementStatus](#section183397331373)

是

当登录类型为[LoginType.QUICK_LOGIN](#section79023235528)时必须设置协议状态为ACCEPTED才可以完成华为账号登录。

当登录类型不是[LoginType.QUICK_LOGIN](#section79023235528)时，如果需要用户同意协议才能完成华为账号登录，请先设置协议状态为NOT_ACCEPTED，当用户同意协议后设置协议状态为ACCEPTED，才可以完成华为账号登录。

**返回值：**

类型

说明

[LoginWithHuaweiIDButtonController](#section6921622144614)

[LoginWithHuaweiIDButton](LoginWithHuaweiIDButton (华为账号Button登录组件).md)组件控制器可以用来注册组件内部的点击事件或者调用组件提供的方法。

#### onClickEvent

onClickEvent(callback: AsyncCallback<ClickEvent>): LoginWithHuaweiIDButtonController

华为账号登录按钮的点击事件。使用callback异步回调。应用可以在用户点击华为账号登录按钮后收到回调，可用于记录运营事件等场景。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力****：**SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：**5.0.0(12)

**参数：**

参数名

类型

必填

说明

callback

AsyncCallback<[ClickEvent](#section967316103272)>

是

回调函数。当用户点击华为账号登录时，err为undefined，data为获取到的[ClickEvent](#section967316103272)；否则为错误对象。

**返回值：**

类型

说明

[LoginWithHuaweiIDButtonController](#section6921622144614)

[LoginWithHuaweiIDButton](LoginWithHuaweiIDButton (华为账号Button登录组件).md)组件控制器可以用来注册组件内部的点击事件或者调用组件提供的方法。

#### onClickLoginWithHuaweiIDButton

onClickLoginWithHuaweiIDButton(callback: AsyncCallback<HuaweiIDCredential>): LoginWithHuaweiIDButtonController

华为账号一键登录结果事件。使用callback异步回调。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力****：**SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：**4.1.0(11)

**参数：**

参数名

类型

必填

说明

callback

AsyncCallback<[HuaweiIDCredential](#section1862534912215)>

是

回调函数。当华为账号登录成功返回结果，err为undefined，data为获取到的[HuaweiIDCredential](#section1862534912215)对象；否则为错误对象。

**返回值：**

类型

说明

[LoginWithHuaweiIDButtonController](#section6921622144614)

[LoginWithHuaweiIDButton](LoginWithHuaweiIDButton (华为账号Button登录组件).md)组件控制器可以用来注册组件内部的点击事件或者调用组件提供的方法。

**错误码：**

以下错误码的详细介绍请参见[ArkTS错误码](ArkTS错误码.md)和[账号管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-account)。

错误码ID

错误信息

[401](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal#section401-参数检查失败)

Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.

[1001500001](ArkTS错误码.md#section1581681312511)

Failed to check the fingerprint of the app bundle.

[1001500002](ArkTS错误码.md#section134761318124311)

This error code is reported when a request is already being processed.

[1001500003](ArkTS错误码.md#section116574197436)

The scopes or permissions are not supported.

[1001502001](ArkTS错误码.md#section539558125020)

The user has not logged in with HUAWEI ID.

[1001502002](ArkTS错误码.md#section1393125918588)

The application is not authorized.

[1001502003](ArkTS错误码.md#section289120911112)

Invalid input parameter value.

[1001502005](ArkTS错误码.md#section1281526328)

Network error.

[1001502009](ArkTS错误码.md#section17561151616317)

Internal error.

[1001502012](ArkTS错误码.md#section223413481361)

The user canceled the authorization.

[1001502014](ArkTS错误码.md#section78953611814)

The app does not have the required scopes or permissions.

[12300001](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-account#section12300001-系统服务异常)

System service works abnormally.

[1005300001](ArkTS错误码.md#section54021153246)

The user did not accept the agreement.

#### setEnabled

setEnabled(enabled: boolean): LoginWithHuaweiIDButtonController

设置华为账号登录按钮是否可点击。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力****：**SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：**5.0.0(12)

**参数：**

参数名

类型

必填

说明

enabled

boolean

是

按钮是否可点击。

当enabled为true时，华为账号登录按钮高亮可点击，当enabled为false时，华为账号登录按钮置灰不可点击，默认值：true。

**返回值：**

类型

说明

[LoginWithHuaweiIDButtonController](#section6921622144614)

[LoginWithHuaweiIDButton](LoginWithHuaweiIDButton (华为账号Button登录组件).md)组件控制器可以用来注册组件内部的点击事件或者调用组件提供的方法。

#### continueLogin

continueLogin(callback: AsyncCallback<void>): LoginWithHuaweiIDButtonController

未同意协议时点击登录按钮弹出协议确认弹框，点击同意并登录按钮时调用该接口。使用callback异步回调。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力****：**SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：**5.0.0(12)

**参数：**

参数名

类型

必填

说明

callback

AsyncCallback<void>

是

回调函数。当用户点击协议弹框的同意并登录按钮操作成功，err为undefined，否则为错误对象。

**返回值：**

类型

说明

[LoginWithHuaweiIDButtonController](#section6921622144614)

[LoginWithHuaweiIDButton](LoginWithHuaweiIDButton (华为账号Button登录组件).md)组件控制器可以用来注册组件内部的点击事件或者调用组件提供的方法。

**错误码：**

以下错误码的详细介绍请参见[ArkTS错误码](ArkTS错误码.md)。

错误码ID

错误信息

[1005300002](ArkTS错误码.md#section1396765353817)

The user did not click the HUAWEI ID login button.

**示例：**

```ets
import { util } from '@kit.ArkTS';
import { authentication, loginComponentManager, LoginWithHuaweiIDButton } from '@kit.AccountKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct QuickLoginButtonComponent {
  logTag: string = 'QuickLoginButtonComponent';
  domainId: number = 0x0000;
  // 匿名化手机号
  @State quickLoginAnonymousPhone: string = '';
  // 是否勾选协议
  @State isSelected: boolean = false;
  // 华为账号用户认证协议链接，此处仅为示例，实际开发过程中，出于可维护性、安全性等方面考虑，域名不建议硬编码在本地
  private static USER_AUTHENTICATION_PROTOCOL: string =
    'https://privacy.consumer.huawei.com/legal/id/authentication-terms.htm?code=CN&language=zh-CN';
  private static USER_SERVICE_TAG = '用户服务协议';
  private static PRIVACY_TAG = '隐私协议';
  private static USER_AUTHENTICATION_TAG = '华为账号用户认证协议';
  // 定义LoginWithHuaweiIDButton展示的隐私文本，展示应用的用户服务协议、隐私协议和华为账号用户认证协议
  privacyText: loginComponentManager.PrivacyText[] = [{
    text: '已阅读并同意',
    type: loginComponentManager.TextType.PLAIN_TEXT
  }, {
    text: '《用户服务协议》',
    tag: QuickLoginButtonComponent.USER_SERVICE_TAG,
    type: loginComponentManager.TextType.RICH_TEXT
  }, {
    text: '《隐私协议》',
    tag: QuickLoginButtonComponent.PRIVACY_TAG,
    type: loginComponentManager.TextType.RICH_TEXT
  }, {
    text: '和',
    type: loginComponentManager.TextType.PLAIN_TEXT
  }, {
    text: '《华为账号用户认证协议》',
    tag: QuickLoginButtonComponent.USER_AUTHENTICATION_TAG,
    type: loginComponentManager.TextType.RICH_TEXT
  }, {
    text: '。',
    type: loginComponentManager.TextType.PLAIN_TEXT
  }];
  // 构造LoginWithHuaweiIDButton组件的控制器
  controller: loginComponentManager.LoginWithHuaweiIDButtonController =
    new loginComponentManager.LoginWithHuaweiIDButtonController()
      /**
       * 当应用使用自定义的登录页时，如果用户未同意协议，需要设置协议状态为NOT_ACCEPTED，当用户同意协议后再设置
       * 协议状态为ACCEPTED，才可以使用华为账号一键登录功能
       */
      .setAgreementStatus(loginComponentManager.AgreementStatus.NOT_ACCEPTED)
      .onClickLoginWithHuaweiIDButton((error: BusinessError | undefined,
        response: loginComponentManager.HuaweiIDCredential) => {
        this.handleLoginWithHuaweiIDButton(error, response);
      })
      .onClickEvent((error: BusinessError, clickEvent: loginComponentManager.ClickEvent) => {
        if (error) {
          hilog.error(this.domainId, this.logTag,
            `Failed to click. errCode is ${error.code}, errMessage is ${error.message}`);
          return;
        }
        hilog.info(this.domainId, this.logTag, `onClickEvent clickEvent: ${clickEvent}`);
      });
  agreementDialog: CustomDialogController = new CustomDialogController({
    builder: AgreementDialog({
      privacyText: this.privacyText,
      cancel: () => {
        this.agreementDialog.close();
        this.controller.setAgreementStatus(loginComponentManager.AgreementStatus.NOT_ACCEPTED);
      },
      confirm: () => {
        this.agreementDialog.close();
        this.isSelected = true;
        this.controller.setAgreementStatus(loginComponentManager.AgreementStatus.ACCEPTED);
        // 调用此方法，同意协议与登录一并完成，无需再次点击登录按钮
        this.controller.continueLogin((error: BusinessError) => {
          if (error) {
            hilog.error(this.domainId, this.logTag,
              `Failed to login with agreementDialog. errCode is ${error.code}, errMessage is ${error.message}`);
          } else {
            hilog.info(this.domainId, this.logTag,
              'Succeeded in clicking agreementDialog continueLogin.');
          }
        });
      },
      clickHyperlinkText: () => {
        this.agreementDialog.close();
        this.jumpToPrivacyWebView();
      }
    }),
    autoCancel: false,
    alignment: DialogAlignment.Center,
  });

  // 传递页面渲染所需的数据，如匿名手机号等
  aboutToAppear(): void {
    this.getQuickLoginAnonymousPhone();
  }

  // Toast提示
  showToast(resource: string) {
    try {
      this.getUIContext().getPromptAction().showToast({
        message: resource,
        duration: 2000
      });
    } catch (error) {
      const message = (error as BusinessError).message
      const code = (error as BusinessError).code
      hilog.error(this.domainId, this.logTag, `showToast args  errCode is ${code}, errMessage is ${message}`);
    }
  }

  // 跳转华为账号用户认证协议页,该页面需在工程main_pages.json文件配置
  jumpToPrivacyWebView() {
    this.getUIContext().getRouter().pushUrl({
      // 需在module.json5中增加“ohos.permission.INTERNET”权限
      url: 'pages/WebPage',
      params: {
        isFromDialog: true,
        url: QuickLoginButtonComponent.USER_AUTHENTICATION_PROTOCOL,
      }
    }, (err) => {
      if (err) {
        hilog.error(this.domainId, this.logTag,
          `Failed to jumpToPrivacyWebView, errCode is ${err.code}, errMessage is ${err.message}`);
      }
    });
  }

  handleLoginWithHuaweiIDButton(error: BusinessError | undefined,
    response: loginComponentManager.HuaweiIDCredential) {
    if (error) {
      hilog.error(this.domainId, this.logTag,
        `Failed to login with LoginWithHuaweiIDButton. errCode is ${error.code}, errMessage is ${error.message}`);
      if (error.code === ErrorCode.ERROR_CODE_NETWORK_ERROR) {
        this.getUIContext().showAlertDialog(
          {
            message: "网络未连接，请检查网络设置。",
            offset: { dx: 0, dy: -12 },
            alignment: DialogAlignment.Bottom,
            autoCancel: false,
            confirm: {
              value: "知道了",
              action: () => {
              }
            }
          }
        );
      } else if (error.code === ErrorCode.ERROR_CODE_AGREEMENT_STATUS_NOT_ACCEPTED) {
        // 未同意协议，弹出协议弹框，推荐使用该回调方式
        this.agreementDialog.open();
      } else if (error.code === ErrorCode.ERROR_CODE_LOGIN_OUT) {
        // 华为账号未登录提示
        this.showToast("华为账号未登录，请重试");
      } else if (error.code === ErrorCode.ERROR_CODE_NOT_SUPPORTED) {
        // 不支持该scopes或permissions提示
        this.showToast("该scopes或permissions不支持");
      } else if (error.code === ErrorCode.ERROR_CODE_PARAMETER_ERROR) {
        // 参数错误提示
        this.showToast("参数错误");
      } else if (error.code === ErrorCode.ERROR_CODE_USER_CANCEL) {
        // 用户取消，无需特别处理
      } else {
        // 其他提示系统或服务异常
        this.showToast('服务或网络异常，请稍后重试');
      }
      return;
    }
    try {
      if (this.isSelected) {
        if (response) {
          hilog.info(this.domainId, this.logTag, 'Succeeded in clicking LoginWithHuaweiIDButton.');
          // 开发者根据实际业务情况使用以下信息
          const authCode = response.authorizationCode;
          const openID = response.openID;
        }
      } else {
        this.agreementDialog.open();
      }
    } catch (err) {
      hilog.error(this.domainId, this.logTag,
        `Failed to login with LoginWithHuaweiIDButton, errCode: ${err.code}, errMessage: ${err.message}`);
      this.getUIContext().showAlertDialog(
        {
          message: '服务或网络异常，请稍后重试',
          offset: { dx: 0, dy: -12 },
          alignment: DialogAlignment.Bottom,
          autoCancel: false,
          confirm: {
            value: '知道了',
            action: () => {
            }
          }
        }
      );
    }
  }

  // 错误处理
  dealAllError(error: BusinessError): void {
    hilog.error(0x0000, 'testTag', `Failed to login, errorCode=${error.code}, errorMsg=${error.message}`);
    // 在应用登录涉及UI交互场景下，建议按照如下错误码指导提示用户
    if (error.code === ErrorCode.ERROR_CODE_LOGIN_OUT) {
      // 用户未登录华为账号，请登录华为账号并重试或者尝试使用其他方式登录
    } else if (error.code === ErrorCode.ERROR_CODE_NETWORK_ERROR) {
      // 网络异常，请检查当前网络状态并重试或者尝试使用其他方式登录
    } else if (error.code === ErrorCode.ERROR_CODE_INTERNAL_ERROR) {
      // 登录失败，请尝试使用其他方式登录
    } else if (error.code === ErrorCode.ERROR_CODE_USER_CANCEL) {
      // 用户取消授权
    } else if (error.code === ErrorCode.ERROR_CODE_SYSTEM_SERVICE) {
      // 系统服务异常，请稍后重试或者尝试使用其他方式登录
    } else if (error.code === ErrorCode.ERROR_CODE_REQUEST_REFUSE) {
      // 重复请求，应用无需处理
    } else if (error.code === ErrorCode.ERROR_CODE_AGREEMENT_STATUS_NOT_ACCEPTED) {
      // 用户未同意协议
    } else {
      // 应用登录失败，请尝试使用其他方式登录
    }
  }

  getQuickLoginAnonymousPhone() {
    // 创建授权请求，并设置参数
    const authRequest = new authentication.HuaweiIDProvider().createAuthorizationWithHuaweiIDRequest();
    /**
     * 获取匿名手机号需传quickLoginAnonymousPhone这个scope，传参之前需要先申请“华为账号一键登录”权限
     * (权限名称为：quickLoginMobilePhone),后续才能获取匿名手机号数据
     */
    authRequest.scopes = ['quickLoginAnonymousPhone'];
    // 用于防跨站点请求伪造
    authRequest.state = util.generateRandomUUID();
    // 一键登录场景该参数必须设置为false
    authRequest.forceAuthorization = false;
    const controller = new authentication.AuthenticationController();
    try {
      controller.executeRequest(authRequest).then((response: authentication.AuthorizationWithHuaweiIDResponse) => {
        // 获取到匿名手机号
        const anonymousPhone = response.data?.extraInfo?.quickLoginAnonymousPhone as string;
        if (anonymousPhone) {
          hilog.info(this.domainId, this.logTag, 'Succeeded in authentication.');
          this.quickLoginAnonymousPhone = anonymousPhone;
          return;
        }
        hilog.info(this.domainId, this.logTag, 'Succeeded in authentication. AnonymousPhone is empty.');
        // 未获取到匿名手机号需要跳转到应用自定义的登录页面
      }).catch((error: BusinessError) => {
        this.dealAllError(error);
      })
    } catch (error) {
      this.dealAllError(error);
    }
  }

  build() {
    Scroll() {
      Column() {
        Column() {
          Column() {
            // 此处为示例资源，开发者可使用应用图标进行替换，以保证正常编译运行
            Image($r('app.media.app_icon'))
              .width(48)
              .height(48)
              .draggable(false)
              .copyOption(CopyOptions.None)
              .onComplete(() => {
                hilog.info(this.domainId, this.logTag, 'appIcon loading success.');
              })
              .onError(() => {
                hilog.error(this.domainId, this.logTag, 'appIcon loading fail.');
              })

            Text($r('app.string.app_name'))
              .fontFamily($r('sys.string.ohos_id_text_font_family_medium'))
              .fontWeight(FontWeight.Medium)
              .fontWeight(FontWeight.Bold)
              .maxFontSize($r('sys.float.ohos_id_text_size_headline8'))
              .minFontSize($r('sys.float.ohos_id_text_size_body1'))
              .maxLines(1)
              .fontColor($r('sys.color.ohos_id_color_text_primary'))
              .constraintSize({ maxWidth: '100%' })
              .margin({
                top: 12,
              })

            Text('应用描述')
              .fontSize($r('sys.float.ohos_id_text_size_body2'))
              .fontColor($r('sys.color.ohos_id_color_text_secondary'))
              .fontFamily($r('sys.string.ohos_id_text_font_family_regular'))
              .fontWeight(FontWeight.Regular)
              .constraintSize({ maxWidth: '100%' })
              .margin({
                top: 8,
              })
          }.margin({
            top: 100
          })

          Column() {
            Text(this.quickLoginAnonymousPhone)
              .fontSize(36)
              .fontColor($r('sys.color.ohos_id_color_text_primary'))
              .fontFamily($r('sys.string.ohos_id_text_font_family_medium'))
              .fontWeight(FontWeight.Bold)
              .lineHeight(48)
              .textAlign(TextAlign.Center)
              .maxLines(1)
              .constraintSize({ maxWidth: '100%', minHeight: 48 })

            Text('华为账号绑定号码')
              .fontSize($r('sys.float.ohos_id_text_size_body2'))
              .fontColor($r('sys.color.ohos_id_color_text_secondary'))
              .fontFamily($r('sys.string.ohos_id_text_font_family_regular'))
              .fontWeight(FontWeight.Regular)
              .lineHeight(19)
              .textAlign(TextAlign.Center)
              .maxLines(1)
              .constraintSize({ maxWidth: '100%' })
              .margin({
                top: 8
              })
          }.margin({
            top: 64
          })

          Column() {
            LoginWithHuaweiIDButton({
              params: {
                // LoginWithHuaweiIDButton支持的样式
                style: loginComponentManager.Style.BUTTON_RED,
                // 账号登录按钮在登录过程中展示加载态
                extraStyle: {
                  buttonStyle: new loginComponentManager.ButtonStyle().loadingStyle({
                    show: true
                  })
                },
                // LoginWithHuaweiIDButton的边框圆角半径
                borderRadius: 24,
                // LoginWithHuaweiIDButton支持的登录类型
                loginType: loginComponentManager.LoginType.QUICK_LOGIN,
                // LoginWithHuaweiIDButton支持按钮的样式跟随系统深浅色模式切换
                supportDarkMode: true
              },
              controller: this.controller
            })
          }
          .height(40)
          .margin({
            top: 56
          })

          Column() {
            Button({
              type: ButtonType.Capsule,
              stateEffect: true
            }) {
              Text('其他方式登录')
                .fontColor($r('sys.color.ohos_id_color_text_primary_activated'))
                .fontFamily($r('sys.string.ohos_id_text_font_family_medium'))
                .fontWeight(FontWeight.Medium)
                .fontSize($r('sys.float.ohos_id_text_size_button1'))
                .focusable(true)
                .focusOnTouch(true)
                .textOverflow({ overflow: TextOverflow.Ellipsis })
                .maxLines(1)
                .padding({ left: 8, right: 8 })
            }
            .fontColor($r('sys.color.ohos_id_color_text_primary_activated'))
            .fontFamily($r('sys.string.ohos_id_text_font_family_medium'))
            .fontWeight(FontWeight.Medium)
            .backgroundColor($r('sys.color.ohos_id_color_button_normal'))
            .focusable(true)
            .focusOnTouch(true)
            .constraintSize({ minHeight: 40 })
            .width('100%')
            .onClick(() => {
              hilog.info(this.domainId, this.logTag, 'click optionalLoginButton.');
            })
          }.margin({ top: 16 })
        }.width('100%')

        Row() {
          Row() {
            Checkbox({ name: 'privacyCheckbox', group: 'privacyCheckboxGroup' })
              .width(24)
              .height(24)
              .focusable(true)
              .focusOnTouch(true)
              .margin({ top: 0 })
              .select(this.isSelected)
              .onChange((value: boolean) => {
                if (value) {
                  this.isSelected = true;
                  this.controller.setAgreementStatus(loginComponentManager.AgreementStatus.ACCEPTED);
                } else {
                  this.isSelected = false;
                  this.controller.setAgreementStatus(loginComponentManager.AgreementStatus.NOT_ACCEPTED);
                }
                hilog.info(this.domainId, this.logTag, `agreementChecked: ${value}`);
              })
          }

          Row() {
            Text() {
              ForEach(this.privacyText, (item: loginComponentManager.PrivacyText) => {
                if (item?.type === loginComponentManager.TextType.PLAIN_TEXT && item?.text) {
                  Span(item?.text)
                    .fontColor($r('sys.color.ohos_id_color_text_secondary'))
                    .fontFamily($r('sys.string.ohos_id_text_font_family_regular'))
                    .fontWeight(FontWeight.Regular)
                    .fontSize($r('sys.float.ohos_id_text_size_body3'))
                } else if (item?.type === loginComponentManager.TextType.RICH_TEXT && item?.text) {
                  Span(item?.text)
                    .fontColor($r('sys.color.ohos_id_color_text_primary_activated'))
                    .fontFamily($r('sys.string.ohos_id_text_font_family_medium'))
                    .fontWeight(FontWeight.Medium)
                    .fontSize($r('sys.float.ohos_id_text_size_body3'))
                    .onClick(() => {
                      // 应用需要根据item.tag实现协议页面的跳转逻辑
                      hilog.info(this.domainId, this.logTag, `click privacy text tag: ${item.tag}`);
                      // 华为账号用户认证协议
                      if (item.tag === QuickLoginButtonComponent.USER_AUTHENTICATION_TAG) {
                        this.jumpToPrivacyWebView();
                      }
                    })
                }
              }, (item: loginComponentManager.PrivacyText) => item.text.toString())
            }
            .width('100%')
          }
          .margin({ left: 12 })
          .layoutWeight(1)
          .constraintSize({ minHeight: 24 })
        }
        .alignItems(VerticalAlign.Top)
        .margin({
          bottom: 44
        })
      }
      .justifyContent(FlexAlign.SpaceBetween)
      .constraintSize({ minHeight: '100%' })
      .margin({
        left: 16,
        right: 16
      })
    }
    .width('100%')
    .height('100%')
  }
}

@CustomDialog
export struct AgreementDialog {
  logTag: string = 'AgreementDialog';
  domainId: number = 0x0000;
  dialogController?: CustomDialogController;
  cancel: () => void = () => {
  };
  confirm: () => void = () => {
  };
  clickHyperlinkText: () => void = () => {
  };
  privacyText: loginComponentManager.PrivacyText[] = [];
  private static USER_AUTHENTICATION_TAG = '华为账号用户认证协议';

  build() {
    Column() {
      Row() {
        Text('用户协议与隐私条款')
          .id('loginPanel_agreement_dialog_privacy_title')
          .maxFontSize($r('sys.float.ohos_id_text_size_headline8'))
          .minFontSize($r('sys.float.ohos_id_text_size_body1'))
          .fontColor($r('sys.color.ohos_id_color_text_primary'))
          .fontFamily($r('sys.string.ohos_id_text_font_family_medium'))
          .fontWeight(FontWeight.Bold)
          .textAlign(TextAlign.Center)
          .textOverflow({ overflow: TextOverflow.Ellipsis })
          .maxLines(2)
      }
      .alignItems(VerticalAlign.Center)
      .constraintSize({ minHeight: 56, maxWidth: 400 })
      .margin({
        left: $r('sys.float.ohos_id_max_padding_start'),
        right: $r('sys.float.ohos_id_max_padding_start')
      })

      Row() {
        Text() {
          ForEach(this.privacyText, (item: loginComponentManager.PrivacyText) => {
            if (item?.type === loginComponentManager.TextType.PLAIN_TEXT && item?.text) {
              Span(item?.text)
                .fontSize($r('sys.float.ohos_id_text_size_body1'))
                .fontColor($r('sys.color.ohos_id_color_text_primary'))
                .fontFamily($r('sys.string.ohos_id_text_font_family_regular'))
                .fontWeight(FontWeight.Regular)
            } else if (item?.type === loginComponentManager.TextType.RICH_TEXT && item?.text) {
              Span(item?.text)
                .fontSize($r('sys.float.ohos_id_text_size_body1'))
                .fontColor('#CE0E2D')
                .fontFamily($r('sys.string.ohos_id_text_font_family_medium'))
                .fontWeight(FontWeight.Medium)
                .onClick(() => {
                  // 应用需要根据item.tag实现协议页面的跳转逻辑
                  hilog.info(this.domainId, this.logTag, `click privacy text tag: ${item.tag}`);
                  // 华为账号用户认证协议
                  if (item.tag === AgreementDialog.USER_AUTHENTICATION_TAG) {
                    hilog.info(this.domainId, this.logTag, 'AgreementDialog click.');
                    this.clickHyperlinkText();
                  }
                })
            }
          }, (item: loginComponentManager.PrivacyText) => item.text.toString())
        }
        .width('100%')
        .textOverflow({ overflow: TextOverflow.Ellipsis })
        .maxLines(10)
        .textAlign(TextAlign.Start)
        .focusable(true)
        .focusOnTouch(true)
        .padding({ left: 24, right: 24 })
      }.width('100%')

      Flex({
        direction: FlexDirection.Row
      }) {
        Button('取消',
          { type: ButtonType.Capsule, stateEffect: true })
          .id('loginPanel_agreement_cancel_btn')
          .fontColor($r('sys.color.ohos_id_color_text_primary'))
          .fontSize($r('sys.float.ohos_id_text_size_button1'))
          .fontFamily($r('sys.string.ohos_id_text_font_family_medium'))
          .backgroundColor(Color.Transparent)
          .fontWeight(FontWeight.Medium)
          .focusable(true)
          .focusOnTouch(true)
          .constraintSize({ minHeight: 40, maxWidth: 400 })
          .width('50%')
          .onClick(() => {
            hilog.info(this.domainId, this.logTag, 'AgreementDialog cancel.');
            this.cancel();
          })

        Button('同意并登录',
          { type: ButtonType.Capsule, stateEffect: true })
          .id('loginPanel_agreement_dialog_huawei_id_login_btn')
          .fontColor(Color.White)
          .backgroundColor('#CE0E2D')
          .fontSize($r('sys.float.ohos_id_text_size_button1'))
          .fontFamily($r('sys.string.ohos_id_text_font_family_medium'))
          .fontWeight(FontWeight.Medium)
          .focusable(true)
          .focusOnTouch(true)
          .constraintSize({ minHeight: 40, maxWidth: 400 })
          .width('50%')
          .onClick(() => {
            hilog.info(this.domainId, this.logTag, 'AgreementDialog confirm.');
            this.confirm();
          })
      }
      .margin({
        top: 8,
        left: $r('sys.float.ohos_id_elements_margin_horizontal_l'),
        right: $r('sys.float.ohos_id_elements_margin_horizontal_l'),
        bottom: 16
      })
    }.backgroundColor($r('sys.color.ohos_id_color_dialog_default_bg'))
    .padding({
      left: 16,
      right: 16
    })
  }
}

export enum ErrorCode {
  // 账号未登录
  ERROR_CODE_LOGIN_OUT = 1001502001,
  // 该账号不支持一键登录，如海外账号
  ERROR_CODE_NOT_SUPPORTED = 1001500003,
  // 网络错误
  ERROR_CODE_NETWORK_ERROR = 1001502005,
  // 内部错误
  ERROR_CODE_INTERNAL_ERROR = 1001502009,
  // 用户取消授权
  ERROR_CODE_USER_CANCEL = 1001502012,
  // 系统服务异常
  ERROR_CODE_SYSTEM_SERVICE = 12300001,
  // 用户未同意用户协议
  ERROR_CODE_AGREEMENT_STATUS_NOT_ACCEPTED = 1005300001,
  // 参数错误
  ERROR_CODE_PARAMETER_ERROR = 401,
  // 重复请求
  ERROR_CODE_REQUEST_REFUSE = 1001500002
}
```

```ets
import { webview } from '@kit.ArkWeb';
import { hilog } from '@kit.PerformanceAnalysisKit';

// 华为账号用户认证协议展示页
@Entry
@Component
struct WebPage {
  @State webUrl?: string = '';
  @State progress: number = 0;
  logTag: string = 'WebPage';
  domainId: number = 0x0000;
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Column() {
        Button({ type: ButtonType.Normal }) {
          Image($r('sys.media.ohos_ic_compnent_titlebar_back'))
            .backgroundColor(Color.Transparent)
            .borderRadius(20)
            .width(24)
            .height(24)
            .draggable(false)
            .autoResize(false)
            .focusable(true)
            .fillColor($r('sys.color.ohos_id_color_titlebar_icon'))
            .matchTextDirection(true)
        }
        .alignSelf(ItemAlign.Start)
        .backgroundColor($r('sys.color.ohos_id_color_button_normal'))
        .borderRadius(20)
        .width(40)
        .height(40)
        .onClick(() => {
          this.getUIContext().getRouter().back();
        })
      }
      .height(56)
      .width('100%')
      .justifyContent(FlexAlign.Center)

      Progress({ value: this.progress, type: ProgressType.Linear })
        .width('100%')
        .visibility(this.progress <= 99 ? Visibility.Visible : Visibility.None)

      Web({ src: this.webUrl ?? '', controller: this.controller })
        .backgroundColor(Color.Transparent)
        .onProgressChange((event) => {
          hilog.info(this.domainId, this.logTag,
            'onProgressChange: ', (event ? event.newProgress : -1));
          this.progress = event ? event.newProgress : 0;
        })
        .darkMode(WebDarkMode.Auto)
        .forceDarkAccess(true)
        .onLoadIntercept((event) => {
          hilog.info(this.domainId, this.logTag, 'onLoadIntercept');
          return false;
        })
        .onErrorReceive((event) => {
          if (event) {
            hilog.error(this.domainId, this.logTag, `onErrorReceive,errorInfo: ${event?.error?.getErrorInfo()}`);
          }
        })
    }
    .alignItems(HorizontalAlign.Start)
    .padding({ left: 12, right: 12 })
    .width('100%')
    .height('100%')
  }

  aboutToAppear(): void {
    hilog.info(0x0000, 'testTag', 'aboutToAppear');
    const params = this.getUIContext().getRouter().getParams() as Record<string, string>;
    this.webUrl = params.url ?? '';
    hilog.info(0x0000, 'testTag', `webUrl: ${this.webUrl}`);
  }

  aboutToDisappear(): void {
    hilog.info(0x0000, 'testTag', 'aboutToDisappear');
    if (this.webUrl) {
      try {
        this.controller.stop();
      } catch (error) {
        hilog.error(0x0000, 'testTag', `stop web error, errorCode=${error.code}, errorMsg=${error.message}`);
      }
    }
  }
}
```