# authentication (华为账号应用统一认证服务)

本模块提供Account Kit（华为账号服务）认证能力，包括账号登录、授权、取消授权等功能。应用可以使用该能力实现应用账号的登录注册、获取华为账号登录状态、手机号一致性校验状态、用户授权信息等。

**起始版本：**4.0.0(10)

#### 导入模块

```ets
import { authentication } from '@kit.AccountKit';
```

#### HuaweiIDProvider

该类提供实现认证服务的方法，用于创建登录、授权、取消授权请求对象。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.AuthenticationServices.HuaweiID.Auth

**起始版本：**4.0.0(10)

**继承：**HuaweiIDProvider继承自[AuthenticationProvider](#section1860064133610)。

#### createLoginWithHuaweiIDRequest

createLoginWithHuaweiIDRequest(): LoginWithHuaweiIDRequest

创建默认scope和permission登录请求对象，可通过属性值设置请求参数。作为应用使用华为账号登录场景的请求参数。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.AuthenticationServices.HuaweiID.Auth

**起始版本：**4.0.0(10)

**返回值：**

类型

说明

[LoginWithHuaweiIDRequest](#section42261825935)

应用登录场景定义应用使用Account Kit登录请求获取UnionID、OpenID等数据的请求对象。华为账号登录场景请求对象参数请应用根据自身实际场景进行选择。

**示例：**

```ets
import { authentication } from '@kit.AccountKit';

const huaweiIdProvider = new authentication.HuaweiIDProvider();
const loginWithHuaweiIDRequest = huaweiIdProvider.createLoginWithHuaweiIDRequest();
```

#### createAuthorizationWithHuaweiIDRequest

createAuthorizationWithHuaweiIDRequest(): AuthorizationWithHuaweiIDRequest

创建一个Account Kit授权请求对象，可通过属性值设置请求参数。作为应用使用华为账号登录场景的请求参数。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.AuthenticationServices.HuaweiID.Auth

**起始版本：**4.0.0(10)

**返回值：**

类型

说明

[AuthorizationWithHuaweiIDRequest](#section12940173017165)

定义应用授权获取用户信息请求对象。

**示例：**

```ets
import { authentication } from '@kit.AccountKit';

const huaweiIdProvider = new authentication.HuaweiIDProvider();
const request = huaweiIdProvider.createAuthorizationWithHuaweiIDRequest();
```

#### createCancelAuthorizationRequest

createCancelAuthorizationRequest(): CancelAuthorizationRequest

创建一个Account Kit取消授权请求对象，可通过属性值设置参数。作为应用取消华为账号授权场景的请求参数。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.AuthenticationServices.HuaweiID.Auth

**起始版本：**4.0.0(10)

**返回值：**

类型

说明

[CancelAuthorizationRequest](#section17720275174)

定义应用取消Account Kit授权请求对象。

**示例：**

```ets
import { authentication } from '@kit.AccountKit';

const huaweiIdProvider = new authentication.HuaweiIDProvider();
const cancelAuthorizationRequest = huaweiIdProvider.createCancelAuthorizationRequest();
```

#### getHuaweiIDState

getHuaweiIDState(request: StateRequest): Promise<StateResult>

获取华为账号登录状态，使用Promise异步回调。在应用需要判断账号是否已登录场景下使用，不依赖网络连接。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.AuthenticationServices.HuaweiID.Auth

**起始版本：**5.0.0(12)

**参数：**

参数名

类型

必填

说明

request

[StateRequest](#section9615740103819)

是

获取华为账号登录状态请求对象，包含请求参数。

**返回值：**

类型

说明

Promise<[StateResult](#section18875010506)>

Promise对象，返回[StateResult](#section18875010506)对象。

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-account)和[ArkTS错误码](zh-cn_topic_0000002528943201.md)。

错误码ID

错误信息

[12300001](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-account#section12300001-系统服务异常)

System service works abnormally.

[1001502003](ArkTS错误码.md#section289120911112)

Invalid input parameter value.

**示例：**

```ets
import { authentication } from '@kit.AccountKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 创建请求参数
const stateRequest: authentication.StateRequest = {
  idType: authentication.IdType.UNION_ID,
  idValue: '*<可通过华为账号登录接口获取>*' // 该值可以通过华为账号登录接口获取
}
try {
  // 执行获取华为账号登录状态请求，并处理结果
  new authentication.HuaweiIDProvider().getHuaweiIDState(stateRequest).then((data: authentication.StateResult) => {
    hilog.info(0x0000, 'testTag', 'Succeeded in getting huaweiIdState result.');
    const state = data.state;
    // 处理state
  }).catch((error: BusinessError) => {
    dealAllError(error);
  })
} catch (error) {
  dealAllError(error);
}

// 错误处理
function dealAllError(error: BusinessError): void {
  hilog.error(0x0000, 'testTag', `Failed to get huaweiIdState, errorCode=${error.code}, errorMsg=${error.message}`);
}
```

#### getMobileNumberConsistency

getMobileNumberConsistency(request: ConsistencyRequest): Promise<ConsistencyResult>

获取手机号一致性状态，使用Promise异步回调。在应用需要校验华为账号绑定的手机号是否与本机SIM卡一致场景下使用。

开发者在使用获取手机号一致性状态接口前，需要完成quickLoginMobilePhone（华为账号一键登录）的scope权限申请，详情参见[开发前提](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-phone-unionid-login#section95093591227)。scope权限申请审批未完成或未通过，将报错[1001502014 应用未申请scopes或permissions权限](zh-cn_topic_0000002528943201.html#section78953611814)。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.AuthenticationServices.HuaweiID.Auth

**设备行为差异：**该接口在Phone、PC/2in1、Tablet中可正常调用，在其他设备类型中返回801错误码。

**起始版本：**5.0.0(12)

**参数：**

参数名

类型

必填

说明

request

[ConsistencyRequest](#section168131411512)

是

获取手机号一致性请求对象，包含请求参数。

**返回值：**

类型

说明

Promise<[ConsistencyResult](#section155352089012)>

Promise对象，返回[ConsistencyResult](#section155352089012)对象。

**错误码：**

以下错误码的详细介绍请参见[ArkTS错误码](ArkTS错误码.md)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

错误码ID

错误信息

[401](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal#section401-参数检查失败)

Parameter error. Possible causes:

1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

[801](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal#section801-该设备不支持此api)

Capability not supported. Function getMobileNumberConsistency can not work correctly due to limited device capabilities.

[1001500001](ArkTS错误码.md#section1581681312511)

Failed to check the fingerprint of the app bundle.

[1001500004](ArkTS错误码.md#section13107132603718)

The account does not support this function.

[1001500005](ArkTS错误码.md#section612754419379)

This function is restricted from being called.

[1001502001](ArkTS错误码.md#section539558125020)

The user has not logged in with HUAWEI ID.

[1001502002](ArkTS错误码.md#section1393125918588)

The application is not authorized.

[1001502005](ArkTS错误码.md#section1281526328)

Network error.

[1001502009](ArkTS错误码.md#section17561151616317)

Internal error.

[1001502014](ArkTS错误码.md#section78953611814)

The app does not have the required scopes or permissions.

**示例：**

```ets
import { authentication } from '@kit.AccountKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 创建请求参数
const consistencyRequest: authentication.ConsistencyRequest = {
  idType: authentication.IdType.UNION_ID,
  idValue: '*<可通过华为账号登录接口获取>*', // 该值可以通过华为账号登录接口获取
  mobileNumber: '+86xxxxxxxxxxx' // 通过华为账号一键登录功能获取到的明文手机号
}
try {
  // 执行获取手机号一致性状态请求，并处理结果
  new authentication.HuaweiIDProvider().getMobileNumberConsistency(consistencyRequest)
    .then((data: authentication.ConsistencyResult) => {
      hilog.info(0x0000, 'testTag', `Succeeded in getting getMobileNumberConsistency result = ${data.state}`);
      const state = data.state;
      // 处理state
    })
    .catch((err: BusinessError) => {
      dealAllError(err);
    })
} catch (error) {
  dealAllError(error);
}

// 错误处理
function dealAllError(error: BusinessError): void {
  hilog.error(0x0000, 'testTag',
    `Failed to get mobileNumberConsistency, errorCode=${error.code}, errorMsg=${error.message}`);
}
```

#### LoginWithHuaweiIDRequest

应用登录场景定义应用使用Account Kit登录请求获取UnionID、OpenID等数据的请求对象。华为账号登录场景请求对象参数请应用根据自身实际场景进行选择。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.AuthenticationServices.HuaweiID.Auth

**起始版本：**4.0.0(10)

**继承：**LoginWithHuaweiIDRequest继承自[AuthenticationRequest](#section3118182610348)。

**名称**

**类型**

只读

可选

**说明**

forceLogin

boolean

否

是

表示是否需要强制拉起华为账号登录页。

如果该值为true，华为账号未登录时，则将拉起华为账号登录页。

如果该值为false，且华为账号未登录，调用[executeRequest](#section3975181884311)将返回[1001502001 用户未登录华为账号](zh-cn_topic_0000002528943201.html#section539558125020)。

默认值：true。

state

string

否

是

请求体中的state参数，该参数与响应体中返回的state比较，校验是否是当前请求，可防止跨站攻击。

开发者可自定义，字符包含0-9、a-z、A-Z、英文点号、英文冒号、斜杠、下划线等，长度限制1-255，校验规则^[0-9a-zA-Z:/\.\-_]{1,255}$。

推荐开发者用随机数并做一致性校验。建议生成方式：[util.generateRandomUUID()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-util#utilgeneraterandomuuid9)。

nonce

string

否

是

请求体中的nonce参数，该参数会包含在返回的ID Token中，通过校验一致性，可用于防止重放攻击。

字符包含0-9、a-z、A-Z、点号、冒号、斜杠、下划线等，长度限制1-255，校验规则^[0-9a-zA-Z:/\.\-_]{1,255}$。

如该参数未传、传空，ID Token中nonce默认值：“default”。

推荐开发者用随机数并做一致性校验。建议生成方式：[util.generateRandomUUID()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-util#utilgeneraterandomuuid9)。

idTokenSignAlgorithm

[IdTokenSignAlgorithm](#section3339031310)

否

是

用于指定ID Token的签名算法。应用根据实际安全要求、性能、系统环境兼容性进行选择。

默认值：PS256。

**示例：**

```ets
import { authentication } from '@kit.AccountKit';
import { util } from '@kit.ArkTS';

const loginRequest = new authentication.HuaweiIDProvider().createLoginWithHuaweiIDRequest();
// 默认值为true，若账号未登录则强制拉起账号登录页
loginRequest.forceLogin = true;
loginRequest.idTokenSignAlgorithm = authentication.IdTokenSignAlgorithm.PS256; // 默认为PS256
loginRequest.state = util.generateRandomUUID(); // 建议使用generateRandomUUID生成state
```

#### IdTokenSignAlgorithm

ID Token签名算法，该类型为枚举，根据IdTokenSignAlgorithm的不同类型，对ID Token进行不同方式的加密。请应用根据实际安全要求、性能、系统环境兼容性进行选择。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.AuthenticationServices.HuaweiID.Auth

**起始版本：**4.0.0(10)

名称

值

说明

PS256

1

RSASSA-PSS使用SHA-256和基于SHA-256的MGF1。为保证安全性建议使用PS256。

RS256

2

RSASSA-PKCS1-v1_5使用SHA-256。

**示例：**

```ets
import { authentication } from '@kit.AccountKit';

const loginRequest = new authentication.HuaweiIDProvider().createLoginWithHuaweiIDRequest();
// 默认值为true，若账号未登录则强制拉起账号登录页
loginRequest.forceLogin = true;
loginRequest.idTokenSignAlgorithm = authentication.IdTokenSignAlgorithm.PS256;
```

#### LoginWithHuaweiIDResponse

Account Kit登录请求响应对象，解析响应结果可得到OpenID、UnionID、Authorization Code、ID Token数据。作为华为账号登录成功的返回结果，用于获取或关联华为账号相关信息。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.AuthenticationServices.HuaweiID.Auth

**起始版本：**4.0.0(10)

**继承：**LoginWithHuaweiIDResponse继承自[AuthenticationResponse](#section2697164193515)。

**名称**

**类型**

**只读**

可选

**说明**

data

[LoginWithHuaweiIDCredential](#section17820155561513)

是

是

登录结果数据，用于获取或关联华为账号相关信息。包含openID、unionID、authorizationCode、idToken字段。

state

string

是

是

响应体中返回的state，账号服务将该字段与请求体中传入的state比较，防止跨站攻击。字符包含“0-9”、“a-z”、“A-Z”、英文点号、英文冒号、斜杠、下划线等，长度限制1-255。校验规则^[0-9a-zA-Z:/\.\-_]{1,255}$。

**示例：**

```ets
import { authentication } from '@kit.AccountKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { util } from '@kit.ArkTS';
import { BusinessError } from '@kit.BasicServicesKit';

// 创建登录请求，并设置参数
const loginRequest = new authentication.HuaweiIDProvider().createLoginWithHuaweiIDRequest();
// 默认值为true，若账号未登录则强制拉起账号登录页
loginRequest.forceLogin = true;
loginRequest.idTokenSignAlgorithm = authentication.IdTokenSignAlgorithm.PS256;
loginRequest.state = util.generateRandomUUID(); // 建议使用generateRandomUUID生成state

// 执行登录请求，并处理结果
try {
  // 此示例为代码片段，实际需在自定义组件实例中使用，以获取UIContext对象作为函数入参
  const controller = new authentication.AuthenticationController(this.getUIContext().getHostContext());
  controller.executeRequest(loginRequest, (error: BusinessError<Object>, data) => {
    if (error) {
      dealAllError(error);
      return;
    }
    const loginWithHuaweiIDResponse = data as authentication.LoginWithHuaweiIDResponse;
    const state = loginWithHuaweiIDResponse.state;
    if (state && loginRequest.state !== state) {
      hilog.error(0x0000, 'testTag', `Failed to login. The state is different, response state: ${state}`);
      return;
    }
    hilog.info(0x0000, 'testTag', 'Succeeded in login.');
    const loginWithHuaweiIDCredential = loginWithHuaweiIDResponse?.data;
    const code = loginWithHuaweiIDCredential?.authorizationCode;
    const idToken = loginWithHuaweiIDCredential?.idToken;
    // 开发者处理code, idToken
  });
} catch (error) {
  dealAllError(error);
}

// 错误处理
function dealAllError(error: BusinessError<Object>): void {
  hilog.error(0x0000, 'testTag', `Failed to login. Code: ${error.code}, message: ${error.message}`);
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
  } else {
    // 应用登录失败，请尝试使用其他方式登录
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
  // 重复请求
  ERROR_CODE_REQUEST_REFUSE = 1001500002
}
```

#### LoginWithHuaweiIDCredential

Account Kit登录成功返回的凭据，用于获取用户相关信息和关联华为账号（OpenID/UnionID）。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.AuthenticationServices.HuaweiID.Auth

**起始版本：**4.0.0(10)

**名称**

**类型**

**只读**

可选

**说明**

authorizationCode

string

是

是

Authorization Code。临时凭据，用于获取Access Token，有效时间5分钟，并且只能使用1次。长度限制1-1024。

idToken

string

是

是

ID Token。JWT格式的字符串，包含用户信息，用于应用获取部分用户相关信息及验证签名。长度限制1-2048。

openID

string

是

否

OpenID。OpenID是华为账号用户在不同类型的产品的身份ID，同一个用户，不同应用，OpenID值不同。具体格式要求请参考[OpenID和UnionID的格式说明](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-faq-9)。

unionID

string

是

否

UnionID。UnionID是华为账号用户在同一个开发者账号下产品的身份ID，同一个用户，同一个开发者账号下管理的不同应用，UnionID值相同。具体格式要求请参考[OpenID和UnionID的格式说明](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-faq-9)。

**示例：**

```ets
import { authentication } from '@kit.AccountKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { util } from '@kit.ArkTS';
import { BusinessError } from '@kit.BasicServicesKit';

// 创建登录请求，并设置参数
const loginRequest = new authentication.HuaweiIDProvider().createLoginWithHuaweiIDRequest();
// 默认值为true，若账号未登录则强制拉起账号登录页
loginRequest.forceLogin = true;
loginRequest.idTokenSignAlgorithm = authentication.IdTokenSignAlgorithm.PS256;
loginRequest.state = util.generateRandomUUID(); // 建议使用generateRandomUUID生成state

// 执行登录请求，并处理结果
try {
  // 此示例为代码片段，实际需在自定义组件实例中使用，以获取UIContext对象作为函数入参
  const controller = new authentication.AuthenticationController(this.getUIContext().getHostContext());
  controller.executeRequest(loginRequest, (error: BusinessError<Object>, data) => {
    if (error) {
      dealAllError(error);
      return;
    }
    const loginWithHuaweiIDResponse = data as authentication.LoginWithHuaweiIDResponse;
    const state = loginWithHuaweiIDResponse.state;
    if (state && loginRequest.state !== state) {
      hilog.error(0x0000,
        'testTag', `Failed to login. The state is different, response state: ${state}`);
      return;
    }
    hilog.info(0x0000, 'testTag', 'Succeeded in login.');

    const loginWithHuaweiIDCredential = loginWithHuaweiIDResponse?.data;
    const code = loginWithHuaweiIDCredential?.authorizationCode;
    const idToken = loginWithHuaweiIDCredential?.idToken;
    // 开发者处理code, idToken
  });
} catch (error) {
  dealAllError(error);
}

// 错误处理
function dealAllError(error: BusinessError<Object>): void {
  hilog.error(0x0000, 'testTag', `Failed to login. Code: ${error.code}, message: ${error.message}`);
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
  } else {
    // 应用登录失败，请尝试使用其他方式登录
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
  // 重复请求
  ERROR_CODE_REQUEST_REFUSE = 1001500002
}
```

#### AuthorizationWithHuaweiIDRequest

该类为应用创建的授权请求对象，使用Account Kit请求授权以申请更多的用户信息，包括scopes、permissions等属性。作为向华为账号申请授权的请求对象，应用根据实际场景按需获取。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.AuthenticationServices.HuaweiID.Auth

**起始版本：**4.0.0(10)

**继承：**AuthorizationWithHuaweiIDRequest继承自[AuthenticationRequest](#section3118182610348)。

**名称**

**类型**

只读

可选

**说明**

scopes

string[]

否

是

scope列表，用于获取用户数据。与permissions属性不能同时为空，否则会返回[1001502003 输入参数值无效](ArkTS错误码.md#section289120911112)错误码。如果传入不合法的scope（例如空值等）则直接返回OpenID和UnionID。

默认值：['openid']。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

scope取值范围：

- profile：华为账号用户的基本信息，如昵称头像等（元服务从5.1.1(19)开始，支持该scope，并需配合supportAtomicService参数使用）。
- openid：华为账号用户的OpenID、UnionID。具体格式要求请参考[OpenID和UnionID的格式说明](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-faq-9)。
- phone：华为账号快速验证手机号（元服务不能直接调用该接口获取手机号，可参考场景化控件[快速验证手机号Button](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scenario-fusion-button-getphonenumber)获取。儿童账号的手机号无法通过该scope获取），使用该scope前需要申请账号权限，具体请参考[开发前提](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-get-phonenumber#section2011736191112)。
- quickLoginAnonymousPhone：获取华为账号绑定的匿名手机号（该scope只能与openid同时使用，Wearable设备以及海外账号无法获取到手机号，会报[1001500003 不支持该scopes或permissions](ArkTS错误码.md#section116574197436)），使用该scope前需要申请账号权限，具体请参考[开发前提](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-phone-unionid-login#section95093591227)。  说明：

**中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）匿名手机号的返回格式不包含国际电话区号，其他国家和地区默认包含国际电话区号。**

- riskLevel：获取用户风险等级（该scope 仅支持与openid、phone、profile组合使用，元服务不支持与phone组合使用，元服务如果需要与phone组合使用可参考场景化控件[获取手机号和风险等级Button](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scenario-fusion-button-get-risklevel)。海外账号不支持获取风险等级），使用该scope前需要申请账号权限，具体请参考[开发前提](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-get-risklevel-on-demand-acquisition#section13750142919492)。

permissions

string[]

否

是

permission列表，用于获取用户授权临时凭据和用户身份认证信息。与scopes属性不能同时为空，否则会返回[1001502003 输入参数值无效](ArkTS错误码.md#section289120911112)错误码。如果传入不合法的permission（例如空值等）则直接返回OpenID和UnionID。

默认值为空，不返回用户授权临时凭据和用户身份认证信息。

permission取值范围：

- serviceauthcode：用户授权临时凭据。
- idtoken：用户身份认证信息。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

forceAuthorization

boolean

否

是

表示华为账号未登录时，是否需要强制拉起华为账号登录页。

默认值：true。

如果该值为true且用户未登录或未授权，则会拉起用户登录或授权页面。

如果该值为false并且用户未登录，执行授权请求将返回[1001502001 用户未登录华为账号](ArkTS错误码.md#section539558125020)。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

state

string

否

是

请求体中的state参数，开发者可自定义，字符包含0-9、a-z、A-Z、点号、冒号、斜杠、下划线等，长度限制1-255，校验规则^[0-9a-zA-Z:/\.\-_]{1,255}$。该参数与响应体中返回的state比较，校验是否是当前请求，可防止跨站攻击。

推荐开发者用随机数并做一致性校验。建议生成方式：[util.generateRandomUUID()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-util#utilgeneraterandomuuid9)。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

nonce

string

否

是

请求体中的nonce参数，字符包含0-9、a-z、A-Z、点号、冒号、斜杠、下划线等，长度限制1-255，校验规则^[0-9a-zA-Z:/\.\-_]{1,255}$。该参数会包含在返回的ID Token中，通过校验一致性，可用于防止重放攻击。如该参数未传、传空，ID Token中nonce默认值：“default”。

推荐开发者用随机数并做一致性校验。建议生成方式：[util.generateRandomUUID()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-util#utilgeneraterandomuuid9)。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

idTokenSignAlgorithm

[IdTokenSignAlgorithm](#section3339031310)

否

是

默认值：PS256，用于指定ID Token的签名算法。应用根据实际安全要求、性能、系统环境兼容性进行选择。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

supportAtomicService

boolean

否

是

在元服务场景下，当传入scopes包含profile时，是否支持获取用户头像昵称。

默认值：false。

如果该值为true，可以正常获取用户头像昵称。

如果该值为false，执行授权请求将返回[1001500003 不支持该scopes或permissions](ArkTS错误码.md#section116574197436)。

**起始版本**：5.1.1(19)

**元服务API：**从版本5.1.1(19)开始，该接口支持在元服务中使用。

 说明：

用于元服务场景调用。

**示例：**

```ets
import { authentication } from '@kit.AccountKit';
import { util } from '@kit.ArkTS';

const authRequest = new authentication.HuaweiIDProvider().createAuthorizationWithHuaweiIDRequest();
authRequest.scopes = ['profile']; // 元服务可传supportAtomicService值为true，以使用profile授权能力
authRequest.permissions = ['idtoken'];
authRequest.forceAuthorization = true;
authRequest.state = util.generateRandomUUID(); // 建议使用generateRandomUUID生成state
authRequest.idTokenSignAlgorithm = authentication.IdTokenSignAlgorithm.PS256;
```

#### AuthorizationWithHuaweiIDResponse

该类封装[AuthorizationWithHuaweiIDRequest](#section12940173017165)授权请求对象获取的用户信息结果。作为华为账号授权成功的返回结果，用于获取或关联华为账号用户信息。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.AuthenticationServices.HuaweiID.Auth

**起始版本：**4.0.0(10)

**继承：**AuthorizationWithHuaweiIDResponse继承自[AuthenticationResponse](#section2697164193515)。

**名称**

**类型**

**只读**

可选

**说明**

data

[AuthorizationWithHuaweiIDCredential](#section1846111631718)

是

是

用户授权结果数据，用于获取或关联华为账号用户信息。

state

string

是

是

响应体中返回的state，字符包含0-9、a-z、A-Z、英文点号、英文冒号、斜杠、下划线等，长度限制1-255，校验规则^[0-9a-zA-Z:/\.\-_]{1,255}$。与请求体中传入的state比较，校验是否是当前请求，防止跨站攻击。

**示例：**

```ets
import { authentication } from '@kit.AccountKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { util } from '@kit.ArkTS';
import { BusinessError } from '@kit.BasicServicesKit';

// 创建授权请求，并设置参数
const authRequest = new authentication.HuaweiIDProvider().createAuthorizationWithHuaweiIDRequest();
// 'openid'为默认值可不传，开发者若需要获取其他用户信息，可传入其他scope参数，具体请参考AuthorizationWithHuaweiIDRequest类说明
authRequest.scopes = ['openid'];
authRequest.permissions = ['idtoken', 'serviceauthcode'];
authRequest.forceAuthorization = true;
authRequest.state = util.generateRandomUUID(); // 建议使用generateRandomUUID生成state
authRequest.idTokenSignAlgorithm = authentication.IdTokenSignAlgorithm.PS256;

// 执行授权请求，并处理结果
try {
  // 此示例为代码片段，实际需在自定义组件实例中使用，以获取UIContext对象作为函数入参
  const controller = new authentication.AuthenticationController(this.getUIContext().getHostContext());
  controller.executeRequest(authRequest, (error: BusinessError<Object>, data) => {
    if (error) {
      dealAllError(error);
      return;
    }
    const authorizationWithHuaweiIDResponse = data as authentication.AuthorizationWithHuaweiIDResponse;
    const state = authorizationWithHuaweiIDResponse.state;
    if (state && authRequest.state !== state) {
      hilog.error(0x0000, 'testTag', `Failed to authorize. The state is different, response state: ${state}`);
      return;
    }
    hilog.info(0x0000, 'testTag', 'Succeeded in authentication.');
    const authorizationWithHuaweiIDCredential = authorizationWithHuaweiIDResponse?.data;
    const idToken = authorizationWithHuaweiIDCredential?.idToken;
    const code = authorizationWithHuaweiIDCredential?.authorizationCode;
    // 开发者处理idToken, code等信息
  });
} catch (error) {
  dealAllError(error);
}

// 错误处理
function dealAllError(error: BusinessError<Object>): void {
  hilog.error(0x0000, 'testTag', `Failed to obtain userInfo. Code: ${error.code}, message: ${error.message}`);
  // 在涉及UI交互场景下，建议按照如下错误码指导提示用户
  if (error.code === ErrorCode.ERROR_CODE_LOGIN_OUT) {
    // 用户未登录华为账号，请登录华为账号并重试
  } else if (error.code === ErrorCode.ERROR_CODE_NETWORK_ERROR) {
    // 网络异常，请检查当前网络状态并重试
  } else if (error.code === ErrorCode.ERROR_CODE_USER_CANCEL) {
    // 用户取消授权
  } else if (error.code === ErrorCode.ERROR_CODE_SYSTEM_SERVICE) {
    // 系统服务异常，请稍后重试
  } else if (error.code === ErrorCode.ERROR_CODE_REQUEST_REFUSE) {
    // 重复请求，应用无需处理
  } else {
    // 获取用户信息失败，请稍后重试
  }
}

export enum ErrorCode {
  // 账号未登录
  ERROR_CODE_LOGIN_OUT = 1001502001,
  // 网络错误
  ERROR_CODE_NETWORK_ERROR = 1001502005,
  // 用户取消授权
  ERROR_CODE_USER_CANCEL = 1001502012,
  // 系统服务异常
  ERROR_CODE_SYSTEM_SERVICE = 12300001,
  // 重复请求
  ERROR_CODE_REQUEST_REFUSE = 1001500002
}
```

#### AuthorizationWithHuaweiIDCredential

Account Kit授权成功返回的凭据，用于获取用户相关信息（头像昵称、匿名手机号等）和关联华为账号（OpenID/UnionID）。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.AuthenticationServices.HuaweiID.Auth

**起始版本：**4.0.0(10)

**名称**

**类型**

**只读**

可选

**说明**

authorizationCode

string

是

是

Authorization Code。临时凭据，用于获取Access Token。有效时间5分钟，并且只能使用1次。长度限制1-1024。

**返回场景**：[AuthorizationWithHuaweiIDRequest](#section12940173017165)接口的permissions中传入'serviceauthcode'参数时返回。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

idToken

string

是

是

ID Token。JWT格式的字符串，包含用户信息，用于应用获取部分用户相关信息及验证签名。长度限制1-2048。

**返回场景**：[AuthorizationWithHuaweiIDRequest](#section12940173017165)接口的permissions中传入'idtoken'参数时返回。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

openID

string

是

是

OpenID。OpenID是华为账号用户在不同类型的产品的身份ID，同一个用户不同应用，OpenID值不同。具体格式要求请参考[OpenID和UnionID的格式说明](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-faq-9)。

**返回场景**：默认返回。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

unionID

string

是

是

UnionID。UnionID是华为账号用户在同一个开发者账号下产品的身份ID，同一个用户，同一个开发者账号下管理的不同应用，UnionID值相同。具体格式要求请参考[OpenID和UnionID的格式说明](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-faq-9)。

**返回场景**：默认返回。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

avatarUri

string

是

是

用户头像链接，有效期较短，建议先将头像下载保存后再使用。

没有长度限制，格式例如：https://xxx/xxx。

**返回场景**：[AuthorizationWithHuaweiIDRequest](#section12940173017165)接口的scopes中传入'profile'参数时返回。

**元服务API：**从版本6.0.0(20)开始，该接口支持在元服务中使用。

nickName

string

是

是

用户昵称。长度限制2-20个字符。

**返回场景**：[AuthorizationWithHuaweiIDRequest](#section12940173017165)接口的scopes中传入'profile'参数时返回。

**元服务API：**从版本6.0.0(20)开始，该接口支持在元服务中使用。

email

string

是

是

用户邮箱。长度限制4-254。

**返回场景**：[AuthorizationWithHuaweiIDRequest](#section12940173017165)接口的scopes中传入'email'参数时返回。

 须知：

元服务不支持该字段。

authorizedScopes

string[]

是

是

本次授权成功的scope清单，通过设置对应scope授权成功后返回Authorization Code来获取对应用户信息。

**返回场景**：默认返回'openid'。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

extraInfo

Record<string, Object>

是

是

扩展信息。可能的key值有quickLoginAnonymousPhone和localNumberConsistency。

如果开发者开启了[代码混淆](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/source-obfuscation-guide)需要配置混淆白名单防止其中包含的属性被混淆。

**返回场景**：[AuthorizationWithHuaweiIDRequest](#section12940173017165)接口的scopes中传入扩展请求参数（'quickLoginAnonymousPhone'等）时返回。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**说明：**华为账号一键登录场景下，可通过"localNumberConsistency"字段获取华为账号绑定手机号和用户本机SIM卡手机号对比结果：

true：华为账号绑定的手机号和本机SIM卡手机号一致。

false：华为账号绑定的手机号和本机SIM卡手机号不一致。

 说明：

若用户本机无SIM卡，返回false。

若用户本机有SIM卡，只要其中有1张SIM卡手机号比对成功即返回true，否则返回false。

**示例：**

```ets
import { authentication } from '@kit.AccountKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { util } from '@kit.ArkTS';
import { BusinessError } from '@kit.BasicServicesKit';

// 创建授权请求，并设置参数
const authRequest = new authentication.HuaweiIDProvider().createAuthorizationWithHuaweiIDRequest();
// 'openid'为默认值可不传，开发者若需要获取其他用户信息，可传入其他scope参数，具体请参考AuthorizationWithHuaweiIDRequest类说明
authRequest.scopes = ['openid'];
authRequest.permissions = ['idtoken', 'serviceauthcode'];
authRequest.forceAuthorization = true;
authRequest.state = util.generateRandomUUID(); // 建议使用generateRandomUUID生成state
authRequest.idTokenSignAlgorithm = authentication.IdTokenSignAlgorithm.PS256;

// 执行授权请求，并处理结果
try {
  // 此示例为代码片段，实际需在自定义组件实例中使用，以获取UIContext对象作为函数入参
  const controller = new authentication.AuthenticationController(this.getUIContext().getHostContext());
  controller.executeRequest(authRequest, (error: BusinessError<Object>, data) => {
    if (error) {
      dealAllError(error);
      return;
    }
    const authorizationWithHuaweiIDResponse = data as authentication.AuthorizationWithHuaweiIDResponse;
    const state = authorizationWithHuaweiIDResponse.state;
    if (state && authRequest.state !== state) {
      hilog.error(0x0000, 'testTag', `Failed to authorize. The state is different, response state: ${state}`);
      return;
    }
    hilog.info(0x0000, 'testTag', 'Succeeded in authentication.');
    const authorizationWithHuaweiIDCredential = authorizationWithHuaweiIDResponse?.data;
    const idToken = authorizationWithHuaweiIDCredential?.idToken;
    const code = authorizationWithHuaweiIDCredential?.authorizationCode;
    // 开发者处理idToken, code等信息
  });
} catch (error) {
  dealAllError(error);
}

// 错误处理
function dealAllError(error: BusinessError<Object>): void {
  hilog.error(0x0000, 'testTag', `Failed to obtain userInfo. Code: ${error.code}, message: ${error.message}`);
  // 在涉及UI交互场景下，建议按照如下错误码指导提示用户
  if (error.code === ErrorCode.ERROR_CODE_LOGIN_OUT) {
    // 用户未登录华为账号，请登录华为账号并重试
  } else if (error.code === ErrorCode.ERROR_CODE_NETWORK_ERROR) {
    // 网络异常，请检查当前网络状态并重试
  } else if (error.code === ErrorCode.ERROR_CODE_USER_CANCEL) {
    // 用户取消授权
  } else if (error.code === ErrorCode.ERROR_CODE_SYSTEM_SERVICE) {
    // 系统服务异常，请稍后重试
  } else if (error.code === ErrorCode.ERROR_CODE_REQUEST_REFUSE) {
    // 重复请求，应用无需处理
  } else {
    // 获取用户信息失败，请稍后重试
  }
}

export enum ErrorCode {
  // 账号未登录
  ERROR_CODE_LOGIN_OUT = 1001502001,
  // 网络错误
  ERROR_CODE_NETWORK_ERROR = 1001502005,
  // 用户取消授权
  ERROR_CODE_USER_CANCEL = 1001502012,
  // 系统服务异常
  ERROR_CODE_SYSTEM_SERVICE = 12300001,
  // 重复请求
  ERROR_CODE_REQUEST_REFUSE = 1001500002
}
```

#### CancelAuthorizationRequest

该类为应用取消Account Kit授权的请求对象，作为华为账号取消授权的请求参数。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.AuthenticationServices.HuaweiID.Auth

**起始版本：**4.0.0(10)

**继承：**CancelAuthorizationRequest继承自[AuthenticationRequest](#section3118182610348)。

**名称**

**类型**

只读

可选

**说明**

state

string

否

是

请求体中的state参数，开发者可自定义，字符包含0-9、a-z、A-Z、英文点号、英文冒号、斜杠、下划线等，长度限制1-255，校验规则^[0-9a-zA-Z:/\.\-_]{1,255}$。

该参数与响应体中返回的state比较，校验是否是当前请求，可防止跨站攻击。

推荐开发者用随机数并做一致性校验。建议生成方式：[util.generateRandomUUID()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-util#utilgeneraterandomuuid9)。

**示例：**

```ets
import { authentication } from '@kit.AccountKit';
import { util } from '@kit.ArkTS';

const cancelRequest = new authentication.HuaweiIDProvider().createCancelAuthorizationRequest();
cancelRequest.state = util.generateRandomUUID(); // 建议使用generateRandomUUID生成state
```

#### CancelAuthorizationResponse

该类为应用取消华为账号授权的响应结果。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.AuthenticationServices.HuaweiID.Auth

**起始版本：**4.0.0(10)

**继承：**CancelAuthorizationResponse继承自[AuthenticationResponse](#section2697164193515)。

**属性：**

**名称**

**类型**

**只读**

可选

**说明**

state

string

是

是

响应体中返回的state，字符包含0-9、a-z、A-Z、英文点号、英文冒号、斜杠、下划线等，长度限制1-255，校验规则^[0-9a-zA-Z:/\.\-_]{1,255}$。

与请求体中传入的state比较，校验是否是当前请求，防止跨站攻击。

**示例：**

```ets
import { authentication } from '@kit.AccountKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { util } from '@kit.ArkTS';
import { BusinessError } from '@kit.BasicServicesKit';

// 创建取消授权请求，并设置参数
const cancelRequest = new authentication.HuaweiIDProvider().createCancelAuthorizationRequest();
cancelRequest.state = util.generateRandomUUID(); // 建议使用generateRandomUUID生成state

// 执行取消授权请求，并处理结果
try {
  // 此示例为代码片段，实际需在自定义组件实例中使用，以获取UIContext对象作为函数入参
  const controller = new authentication.AuthenticationController(this.getUIContext().getHostContext());
  controller.executeRequest(cancelRequest, (error: BusinessError<Object>, data) => {
    if (error) {
      dealAllError(error);
      return;
    }
    const cancelAuthorizationResponse = data as authentication.CancelAuthorizationResponse;
    const state = cancelAuthorizationResponse.state;
    if (state && cancelRequest.state !== state) {
      hilog.error(0x0000, 'testTag', `Failed to cancel. The state is different, response state: ${state}`);
      return;
    }
    hilog.info(0x0000, 'testTag', 'Succeeded in canceling.');
  });
} catch (error) {
  dealAllError(error);
}

// 错误处理
function dealAllError(error: BusinessError<Object>): void {
  hilog.error(0x0000, 'testTag', `Failed to cancel. Code: ${error.code}, message: ${error.message}`);
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
  } else {
    // 应用登录失败，请尝试使用其他方式登录
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
  // 重复请求
  ERROR_CODE_REQUEST_REFUSE = 1001500002
}
```

#### AuthenticationErrorCode

该枚举为登录、授权、取消授权等接口的错误码。应用可根据如下错误码进行不同的处理。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.AuthenticationServices.HuaweiID.Auth

**起始版本：**4.0.0(10)

**名称**

**值**

**说明**

PACKAGE_FINGERPRINT_CHECK_ERROR

[1001500001](ArkTS错误码.md#section1581681312511)

应用指纹证书校验失败。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

DUPLICATE_REQUEST_REJECTED

[1001500002](ArkTS错误码.md#section134761318124311)

重复请求，当已有相同的请求在处理时，返回此错误码，此错误码不需要处理。你的应用需实现点击控制，防止连续点击发起相同请求。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

SCOPE_OR_PERRMISSION_UNSUPPORTED

[1001500003](ArkTS错误码.md#section116574197436)

不支持该scopes或permissions。

**起始版本**：5.0.0(12)

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

UNSUPPORTED

[1001500004](ArkTS错误码.md#section13107132603718)

已登录的华为账号不支持该功能。

**起始版本**：5.0.0(12)

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

REQUEST_RESTRICTED

[1001500005](ArkTS错误码.md#section612754419379)

该功能被限制调用。

**起始版本**：5.0.0(12)

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

ACCOUNT_NOT_LOGGED_IN

[1001502001](ArkTS错误码.md#section539558125020)

用户未登录华为账号。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

APP_NOT_AUTHORIZED

[1001502002](ArkTS错误码.md#section1393125918588)

应用未授权。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

PARAMETER_INVALID

[1001502003](ArkTS错误码.md#section289120911112)

输入参数值无效，接口传参异常等。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

NETWORK_ERROR

[1001502005](ArkTS错误码.md#section1281526328)

网络异常。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

INTERNAL_ERROR

[1001502009](ArkTS错误码.md#section17561151616317)

内部错误，如华为账号服务器错误或其他内部错误等。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

USER_CANCELED

[1001502012](ArkTS错误码.md#section223413481361)

用户取消授权。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

SCOPE_OR_PERMISSION_NOT_REQUESTED

[1001502014](ArkTS错误码.md#section78953611814)

应用未申请scopes或permissions权限。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

#### AuthenticationController

该类为Account Kit登录授权、取消授权请求Controller。用于执行登录授权请求方法。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.AuthenticationServices.HuaweiID.Auth

**起始版本：**4.0.0(10)

#### constructor

constructor(context?: common.Context)

构造器，构造Account Kit登录授权等请求Controller实例。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.AuthenticationServices.HuaweiID.Auth

**起始版本：**4.0.0(10)

**参数：**

参数名

类型

必填

说明

context

[common.Context](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-common#context)

否

Context上下文，当需要拉起华为账号登录、授权页面时必须传该参数，否则会报[401](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal#section401-参数检查失败)参数检查失败错误码。

应用可支持的Context有：[UIAbilityContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext)和[UIExtensionContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiextensioncontext)。不支持应用在半模态、弹出框、子窗口等非全页面组件中使用[UIExtensionContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiextensioncontext)调用。

元服务可支持的Context有：[UIAbilityContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext)。

 说明：

- 在4.0.0(10)版本，参数类型为[UIAbilityContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext)。
- 从4.1.0(11)版本开始，参数类型为[Context](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-context)。

**示例：**

```ets
import { authentication } from '@kit.AccountKit';

// 此示例为代码片段，实际需在自定义组件实例中使用，以获取UIContext对象作为函数入参
const controller = new authentication.AuthenticationController(this.getUIContext().getHostContext());
```

#### executeRequest

executeRequest(request: AuthenticationRequest, callback: AsyncCallback<AuthenticationResponse, Record<string, Object>>): void

执行Account Kit登录、授权等请求。使用callback异步回调。用于应用向华为账号请求登录、授权、取消授权等场景。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.AuthenticationServices.HuaweiID.Auth

**起始版本：**4.0.0(10)

**参数：**

参数名

类型

必填

说明

request

[AuthenticationRequest](#section3118182610348)

是

登录授权认证请求体。

如该参数未正确传入，会抛出[401](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal#section401-参数检查失败)参数检查失败错误码。

callback

AsyncCallback<[AuthenticationResponse](#section2697164193515), Record<string, Object>>

是

登录授权回调函数。

当获取响应数据成功，err为undefined，data为获取到的[AuthenticationResponse](#section2697164193515)对象；否则为错误对象。

如该参数未正确传入，会抛出[401](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal#section401-参数检查失败)参数检查失败错误码。

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-account)和[ArkTS错误码](zh-cn_topic_0000002528943201.md)。

错误码ID

错误信息

[401](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal#section401-参数检查失败)

Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.

[12300001](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-account#section12300001-系统服务异常)

System service works abnormally.

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

[1001500001](ArkTS错误码.md#section1581681312511)

Failed to check the fingerprint of the app bundle.

[1001502012](ArkTS错误码.md#section223413481361)

The user canceled the authorization.

[1001502014](ArkTS错误码.md#section78953611814)

The app does not have the required scopes or permissions.

[1001500002](ArkTS错误码.md#section134761318124311)

This error code is reported when a request is already being processed.

[1001500003](ArkTS错误码.md#section116574197436)

The scopes or permissions are not supported.

**示例：**

```ets
import { authentication } from '@kit.AccountKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { util } from '@kit.ArkTS';
import { BusinessError } from '@kit.BasicServicesKit';

// 创建授权请求，并设置参数
const authRequest = new authentication.HuaweiIDProvider().createAuthorizationWithHuaweiIDRequest();
// 'openid'为默认值可不传，开发者若需要获取其他用户信息，可传入其他scope参数，具体请参考AuthorizationWithHuaweiIDRequest类说明
authRequest.scopes = ['openid'];
authRequest.permissions = ['idtoken', 'serviceauthcode'];
authRequest.forceAuthorization = true;
authRequest.state = util.generateRandomUUID(); // 建议使用generateRandomUUID生成state
authRequest.idTokenSignAlgorithm = authentication.IdTokenSignAlgorithm.PS256;

// 执行授权请求，并处理结果
try {
  // 此示例为代码片段，实际需在自定义组件实例中使用，以获取UIContext对象作为函数入参
  const controller = new authentication.AuthenticationController(this.getUIContext().getHostContext());
  controller.executeRequest(authRequest, (error: BusinessError<Object>, data) => {
    if (error) {
      dealAllError(error);
      return;
    }
    const authorizationWithHuaweiIDResponse = data as authentication.AuthorizationWithHuaweiIDResponse;
    const state = authorizationWithHuaweiIDResponse.state;
    if (state && authRequest.state !== state) {
      hilog.error(0x0000, 'testTag', `Failed to authorize. The state is different, response state: ${state}`);
      return;
    }
    hilog.info(0x0000, 'testTag', 'Succeeded in authentication.');
    const authorizationWithHuaweiIDCredential = authorizationWithHuaweiIDResponse?.data;
    const idToken = authorizationWithHuaweiIDCredential?.idToken;
    const code = authorizationWithHuaweiIDCredential?.authorizationCode;
    // 开发者处理idToken, code等信息
  });
} catch (error) {
  dealAllError(error);
}

// 错误处理
function dealAllError(error: BusinessError<Object>): void {
  hilog.error(0x0000, 'testTag', `Failed to obtain userInfo. Code: ${error.code}, message: ${error.message}`);
  // 在涉及UI交互场景下，建议按照如下错误码指导提示用户
  if (error.code === ErrorCode.ERROR_CODE_LOGIN_OUT) {
    // 用户未登录华为账号，请登录华为账号并重试
  } else if (error.code === ErrorCode.ERROR_CODE_NETWORK_ERROR) {
    // 网络异常，请检查当前网络状态并重试
  } else if (error.code === ErrorCode.ERROR_CODE_USER_CANCEL) {
    // 用户取消授权
  } else if (error.code === ErrorCode.ERROR_CODE_SYSTEM_SERVICE) {
    // 系统服务异常，请稍后重试
  } else if (error.code === ErrorCode.ERROR_CODE_REQUEST_REFUSE) {
    // 重复请求，应用无需处理
  } else {
    // 获取用户信息失败，请稍后重试
  }
}

export enum ErrorCode {
  // 账号未登录
  ERROR_CODE_LOGIN_OUT = 1001502001,
  // 网络错误
  ERROR_CODE_NETWORK_ERROR = 1001502005,
  // 用户取消授权
  ERROR_CODE_USER_CANCEL = 1001502012,
  // 系统服务异常
  ERROR_CODE_SYSTEM_SERVICE = 12300001,
  // 重复请求
  ERROR_CODE_REQUEST_REFUSE = 1001500002
}
```

#### executeRequest

executeRequest(request: AuthenticationRequest): Promise<AuthenticationResponse>

执行Account Kit登录授权等请求，使用Promise异步回调。用于应用向华为账号请求登录、授权、取消授权等场景。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.AuthenticationServices.HuaweiID.Auth

**起始版本：**4.0.0(10)

**参数****：**

参数名

类型

必填

说明

request

[AuthenticationRequest](#section3118182610348)

是

登录授权认证请求体。如该参数未正确传入，会抛出[401](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal#section401-参数检查失败)参数检查失败错误码。

**返回值：**

类型

说明

Promise<[AuthenticationResponse](#section2697164193515)>

登录授权Promise对象，返回[AuthenticationResponse](#section2697164193515)对象。

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-account)和[ArkTS错误码](zh-cn_topic_0000002528943201.md)。

错误码ID

错误信息

[401](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal#section401-参数检查失败)

Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.

[12300001](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-account#section12300001-系统服务异常)

System service works abnormally.

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

[1001500001](ArkTS错误码.md#section1581681312511)

Failed to check the fingerprint of the app bundle.

[1001502012](ArkTS错误码.md#section223413481361)

The user canceled the authorization.

[1001502014](ArkTS错误码.md#section78953611814)

The app does not have the required scopes or permissions.

[1001500002](ArkTS错误码.md#section134761318124311)

This error code is reported when a request is already being processed.

[1001500003](ArkTS错误码.md#section116574197436)

The scopes or permissions are not supported.

**示例：**

```ets
import { authentication } from '@kit.AccountKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { util } from '@kit.ArkTS';
import { BusinessError } from '@kit.BasicServicesKit';

// 创建授权请求，并设置参数
const authRequest = new authentication.HuaweiIDProvider().createAuthorizationWithHuaweiIDRequest();
// 'openid'为默认值可不传，开发者若需要获取其他用户信息，可传入其他scope参数，具体请参考AuthorizationWithHuaweiIDRequest类说明
authRequest.scopes = ['openid'];
authRequest.permissions = ['idtoken', 'serviceauthcode'];
authRequest.forceAuthorization = true;
authRequest.state = util.generateRandomUUID(); // 建议使用generateRandomUUID生成state
authRequest.idTokenSignAlgorithm = authentication.IdTokenSignAlgorithm.PS256;

// 执行授权请求，并处理结果
try {
  // 此示例为代码片段，实际需在自定义组件实例中使用，以获取UIContext对象作为函数入参
  const controller = new authentication.AuthenticationController(this.getUIContext().getHostContext());
  controller.executeRequest(authRequest).then((data) => {
    const authorizationWithHuaweiIDResponse = data as authentication.AuthorizationWithHuaweiIDResponse;
    const state = authorizationWithHuaweiIDResponse.state;
    if (state && authRequest.state !== state) {
      hilog.error(0x0000, 'testTag', `Failed to authorize. The state is different, response state: ${state}`);
      return;
    }
    hilog.info(0x0000, 'testTag', 'Succeeded in authentication.');
    const authorizationWithHuaweiIDCredential = authorizationWithHuaweiIDResponse?.data;
    const idToken = authorizationWithHuaweiIDCredential?.idToken;
    const code = authorizationWithHuaweiIDCredential?.authorizationCode;
    // 开发者处理idToken, code等信息
  }).catch((err: BusinessError) => {
    dealAllError(err);
  });
} catch (error) {
  dealAllError(error);
}

// 错误处理
function dealAllError(error: BusinessError): void {
  hilog.error(0x0000, 'testTag', `Failed to obtain userInfo. Code: ${error.code}, message: ${error.message}`);
  // 在涉及UI交互场景下，建议按照如下错误码指导提示用户
  if (error.code === ErrorCode.ERROR_CODE_LOGIN_OUT) {
    // 用户未登录华为账号，请登录华为账号并重试
  } else if (error.code === ErrorCode.ERROR_CODE_NETWORK_ERROR) {
    // 网络异常，请检查当前网络状态并重试
  } else if (error.code === ErrorCode.ERROR_CODE_USER_CANCEL) {
    // 用户取消授权
  } else if (error.code === ErrorCode.ERROR_CODE_SYSTEM_SERVICE) {
    // 系统服务异常，请稍后重试
  } else if (error.code === ErrorCode.ERROR_CODE_REQUEST_REFUSE) {
    // 重复请求，应用无需处理
  } else {
    // 获取用户信息失败，请稍后重试
  }
}

export enum ErrorCode {
  // 账号未登录
  ERROR_CODE_LOGIN_OUT = 1001502001,
  // 网络错误
  ERROR_CODE_NETWORK_ERROR = 1001502005,
  // 用户取消授权
  ERROR_CODE_USER_CANCEL = 1001502012,
  // 系统服务异常
  ERROR_CODE_SYSTEM_SERVICE = 12300001,
  // 重复请求
  ERROR_CODE_REQUEST_REFUSE = 1001500002
}
```

#### AuthenticationRequest

华为账号登录授权认证请求父类对象。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.AuthenticationServices.HuaweiID.Auth

**起始版本：**4.0.0(10)

#### AuthenticationResponse

华为账号登录授权认证请求响应父类对象。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.AuthenticationServices.HuaweiID.Auth

**起始版本：**4.0.0(10)

#### AuthenticationProvider

华为账号登录授权认证请求provider父类对象。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.AuthenticationServices.HuaweiID.Auth

**起始版本：**4.0.0(10)

#### IdType

该枚举为ID类型枚举对象，作为华为账号登录状态请求参数传入。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.AuthenticationServices.HuaweiID.Auth

**起始版本：**5.0.0(12)

**名称**

**值**

**说明**

USER_ID

1

华为账号用户的UID。

 说明：

该参数仅对系统应用开放。

OPEN_ID

2

华为账号用户的OpenID。具体格式要求请参考[OpenID和UnionID的格式说明](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-faq-9)。

UNION_ID

3

华为账号用户的UnionID。具体格式要求请参考[OpenID和UnionID的格式说明](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-faq-9)。

#### State

该枚举为华为账号登录状态枚举对象。用于保存华为账号登录状态结果。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.AuthenticationServices.HuaweiID.Auth

**起始版本：**5.0.0(12)

**名称**

**值**

**说明**

UNLOGGED_IN

0

华为账号未登录。

AUTHORIZED

1

华为账号已登录且传入账号的UnionID/OpenID与当前账号一致。

UNAUTHORIZED

2

华为账号已登录且传入账号的UnionID/OpenID与当前账号不一致。

#### StateRequest

该类为获取华为账号登录状态请求对象，作为[getHuaweiIDState](#section102884586336)传参。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.AuthenticationServices.HuaweiID.Auth

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

idType

[IdType](#section13891254145017)

否

否

属性idValue的ID类型，当前非系统应用只能传IdType.UNION_ID或IdType.OPEN_ID。

idValue

string

否

否

用户获取的UnionID、OpenID值，传递的类型通过idType属性定义。不可为空，否则会报[1001502003 输入参数值无效](ArkTS错误码.md#section289120911112)错误码。长度限制1-256。

UnionID、OpenID值可以通过[LoginWithHuaweiIDResponse](#section15454203811311)、[AuthorizationWithHuaweiIDResponse](#section10418450161620)、[LoginPanel](zh-cn_topic_0000002528823215.html#section72281234181611)或[LoginWithHuaweiIDButton](LoginWithHuaweiIDButton (华为账号Button登录组件).md#section1624716107193)接口获取，具体方法参考其示例代码。

**示例：**

```ets
import { authentication } from '@kit.AccountKit';

// 创建请求参数
const request: authentication.StateRequest = {
  idType: authentication.IdType.UNION_ID,
  idValue: '*<可通过华为账号登录接口获取>*' // 该值可以通过华为账号登录接口获取
}
```

#### StateResult

该类为获取华为账号登录状态结果对象。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.AuthenticationServices.HuaweiID.Auth

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

state

[State](#section1687013712515)

否

否

华为账号登录状态枚举对象。用于保存华为账号登录状态结果。

**示例：**

```ets
import { authentication } from '@kit.AccountKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 创建请求参数
const stateRequest: authentication.StateRequest = {
  idType: authentication.IdType.UNION_ID,
  idValue: '*<可通过华为账号登录接口获取>*' // 该值可以通过华为账号登录接口获取
}
try {
  // 执行获取华为账号登录状态请求，并处理结果
  new authentication.HuaweiIDProvider().getHuaweiIDState(stateRequest).then((data: authentication.StateResult) => {
    hilog.info(0x0000, 'testTag', 'Succeeded in getting huaweiIdState result.');
    const state = data.state;
    // 处理state
  }).catch((err: BusinessError) => {
    dealAllError(err);
  })
} catch (error) {
  dealAllError(error);
}

// 错误处理
function dealAllError(error: BusinessError): void {
  hilog.error(0x0000, 'testTag', `Failed to getHuaweiIdState, errorCode=${error.code}, errorMsg=${error.message}`);
}
```

#### ConsistencyState

该枚举为手机号一致性状态枚举对象。应用可根据结果进行相应风控处理。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.AuthenticationServices.HuaweiID.Auth

**起始版本：**5.0.0(12)

**名称**

**值**

**说明**

CONSISTENT

0

华为账号已登录，传入的手机号与当前账号绑定的手机号一致，与当前设备任意一个SIM卡手机号一致。

INCONSISTENT_WITH_DEVICES

1

华为账号已登录，传入的手机号与当前账号绑定的手机号一致，与当前设备SIM卡手机号不一致或当前设备无SIM卡。

INCONSISTENT

2

华为账号已登录，传入的手机号与当前账号绑定的手机号不一致。

#### ConsistencyRequest

该类为获取手机号一致性状态请求对象。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.AuthenticationServices.HuaweiID.Auth

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

idType

[IdType](#section13891254145017)

否

否

属性idValue的ID类型，当前非系统应用只能传IdType.UNION_ID或IdType.OPEN_ID。

idValue

string

否

否

用户的UnionID、OpenID值，不可为空，长度限制1-256，传递的类型通过idType属性定义。

UnionID、OpenID值可以通过[LoginWithHuaweiIDResponse](#section15454203811311)、[AuthorizationWithHuaweiIDResponse](#section10418450161620)、[LoginPanel](zh-cn_topic_0000002528823215.html#section72281234181611)或[LoginWithHuaweiIDButton](LoginWithHuaweiIDButton (华为账号Button登录组件).md#section1624716107193)接口获取，具体方法参考其示例代码。

mobileNumber

string

否

否

通过[LoginWithHuaweiIDButton](LoginWithHuaweiIDButton (华为账号Button登录组件).md#section1624716107193)组件的一键登录功能获取到的手机号，传入完整的手机号需要添加国家码，例如中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）为+86，值不可为空，长度限制1-256。

手机号示例：+86xxxxxxxxxxx（明文手机号）。

**示例：**

```ets
import { authentication } from '@kit.AccountKit';

// 创建请求参数
const request: authentication.ConsistencyRequest = {
  idType: authentication.IdType.UNION_ID,
  idValue: '*<可通过华为账号登录接口获取>*', // 该值可以通过华为账号登录接口获取
  mobileNumber: '+86xxxxxxxxxxx' // 通过华为账号一键登录功能获取到的明文手机号
}
```

#### ConsistencyResult

该类为获取手机号一致性状态结果对象。应用可根据结果进行相应风控处理。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.AuthenticationServices.HuaweiID.Auth

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

state

[ConsistencyState](#section1271024585118)

否

否

手机号一致性状态枚举对象。

**示例：**

```ets
import { authentication } from '@kit.AccountKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 创建请求参数
const consistencyRequest: authentication.ConsistencyRequest = {
  idType: authentication.IdType.UNION_ID,
  idValue: '*<可通过华为账号登录接口获取>*', // 该值可以通过华为账号登录接口获取
  mobileNumber: '+86xxxxxxxxxxx' // 通过华为账号一键登录功能获取到的明文手机号
}
try {
  // 执行获取手机号一致性状态请求，并处理结果
  new authentication.HuaweiIDProvider().getMobileNumberConsistency(consistencyRequest)
    .then((data: authentication.ConsistencyResult) => {
      hilog.info(0x0000, 'testTag', `Succeeded in getting getMobileNumberConsistency result = ${data.state}`);
      const state = data.state;
      // 处理state
    })
    .catch((err: BusinessError) => {
      dealAllError(err);
    })
} catch (error) {
  dealAllError(error);
}

// 错误处理
function dealAllError(error: BusinessError): void {
  hilog.error(0x0000, 'testTag',
    `Failed to get mobileNumberConsistency, errorCode=${error.code}, errorMsg=${error.message}`);
}
```