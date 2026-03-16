# realName (华为账号实名认证服务)

本模块提供Account Kit实名认证能力，包括人脸核身功能。当需要验证用户实名信息的场景，为保证用户填写的实名信息的正确性，应用需要对用户的实名信息进行校验。

**起始版本：**5.0.0(12)

该接口目前暂停开放。

#### 导入模块

```ets
import { realName } from '@kit.AccountKit';
```

#### FacialRecognitionVerificationRequest

该类为人脸核身请求对象，定义了人脸核身请求参数。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.AuthenticationServices.HuaweiID.RealNameVerify

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

verificationToken

string

否

否

身份验证令牌，调用华为账号OpenRealName服务[实名信息校验](实名信息校验.md)接口获取。长度限制1-2048。

state

string

否

是

请求体中的state参数，开发者可自定义，字符包含0-9、a-z、A-Z、英文点号、英文冒号、斜杠、下划线等，长度限制1-255，校验规则^[0-9a-zA-Z:/\.\-_]{1,255}$。该参数与响应体中返回的state比较，校验是否是当前请求，可防止跨站攻击。

默认值：undefined。

推荐开发者用随机数并做一致性校验。建议生成方式：[util.generateRandomUUID()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-util#utilgeneraterandomuuid9)。

**示例：**

```ets
import { realName } from '@kit.AccountKit';
import { util } from '@kit.ArkTS';

const request: realName.FacialRecognitionVerificationRequest = {
  verificationToken: "*<可调用华为账号服务实名信息校验接口获取>*", // 调用华为账号OpenRealName服务实名信息校验接口获取
  state: util.generateRandomUUID() // 建议使用generateRandomUUID生成state
}
```

#### FacialRecognitionVerificationResult

该类为人脸核身请求结果对象，定义了人脸核身请求返回结果数据字段。如果成功返回该对象，说明人脸核身验证成功。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.AuthenticationServices.HuaweiID.RealNameVerify

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

facialRecognitionVerificationToken

string

是

否

验证成功后返回的人脸核身验证令牌。长度限制1-2048。

state

string

是

是

响应体中返回的state，字符包含0-9、a-z、A-Z、英文点号、英文冒号、斜杠、下划线等，长度限制1-255，校验规则^[0-9a-zA-Z:/\.\-_]{1,255}$。与请求体中传入的state比较，校验是否是当前请求，防止跨站攻击。

推荐开发者用随机数并做一致性校验。建议生成方式：[util.generateRandomUUID()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-util#utilgeneraterandomuuid9)。

#### RealNameErrorCode

该枚举为Account Kit实名认证服务的错误码。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.AuthenticationServices.HuaweiID.RealNameVerify

**起始版本：**5.0.0(12)

**名称**

**值**

**说明**

NETWORK_ERROR

[1002500001](../../errors/ArkTS错误码.md#section126501952132317)

网络不可用。

ACCOUNT_NOT_LOGGED_IN

[1002500002](../../errors/ArkTS错误码.md#section1651105232319)

用户未登录华为账号。

PACKAGE_FINGERPRINT_CHECK_ERROR

[1002500003](../../errors/ArkTS错误码.md#section665175210236)

应用指纹证书校验失败。

PERMISSION_CHECK_ERROR

[1002500004](../../errors/ArkTS错误码.md#section17651105272310)

应用程序未申请对应permissions权限。

USER_CANCELED

[1002500005](../../errors/ArkTS错误码.md#section1995615923313)

用户取消验证。

INTERNAL_ERROR

[1002500006](../../errors/ArkTS错误码.md#section10196176171810)

内部错误。

REAL_NAME_UNSUPPORTED

[1002500008](../../errors/ArkTS错误码.md#section177525511359)

该华为账号不支持实名验证。

REAL_NAME_VERIFICATION_ERROR

[1002500009](../../errors/ArkTS错误码.md#section1055112416269)

实名渠道验证错误。

FACE_NOT_MATCH

[1002500011](../../errors/ArkTS错误码.md#section12860126792)

您的面部与作为身份证明的面部图像不匹配。

REAL_NAME_NOT_EXIST

[1002500012](../../errors/ArkTS错误码.md#section1235141017912)

未查询到该华为账号的实名信息。

NAME_AND_ID_NUMBER_NOT_MATCH

[1002500013](../../errors/ArkTS错误码.md#section1792982614911)

姓名和身份证号码不匹配。

TOO_MANY_ATTEMPTS

[1002500014](../../errors/ArkTS错误码.md#section13455833098)

实名验证尝试次数过多。24小时后重试。

VERIFICATION_TOKEN_INCORRECT

[1002500015](../../errors/ArkTS错误码.md#section1377413361998)

参数verificationToken不合法。

DEVICE_NOT_SUPPORTED

[1002500016](../../errors/ArkTS错误码.md#section1239413431916)

此设备不支持此API。

#### startFacialRecognitionVerification

startFacialRecognitionVerification(context: common.Context, request: FacialRecognitionVerificationRequest): Promise<FacialRecognitionVerificationResult>

执行华为账号人脸核身请求，拉起验证人脸页面。使用Promise异步回调。

该接口暂不支持儿童账号使用。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.AuthenticationServices.HuaweiID.RealNameVerify

**设备行为差异：**该接口在Phone、PC/2in1、Tablet中可正常调用，在其他设备类型中返回801错误码。

**起始版本：**5.0.0(12)

**参数：**

参数名

类型

必填

说明

context

[common.Context](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-common#context)

是

Context上下文。

应用可支持的Context有：[UIAbilityContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext)和[UIExtensionContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiextensioncontext)。不支持应用在半模态、弹出框、子窗口等非全页面组件中使用[UIExtensionContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiextensioncontext)调用。

元服务可支持的Context有：[UIAbilityContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext)。

request

[FacialRecognitionVerificationRequest](#section10967755141115)

是

人脸核身请求对象，传入令牌等信息。

**返回值：**

类型

说明

Promise<[FacialRecognitionVerificationResult](#section19699554110)>

Promise对象，返回[FacialRecognitionVerificationResult](#section19699554110)对象。返回该对象，说明人脸核身验证成功。可使用该对象的state和入参对象的state比较，校验是否是当前请求，可防止跨站攻击。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[ArkTS错误码](../../errors/ArkTS错误码 (account-api-error-code).md)。

错误码ID

错误信息

[401](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal#section401-参数检查失败)

Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

[801](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal#section801-该设备不支持此api)

Capability not supported. Function startFacialRecognitionVerification can not work correctly due to limited device capabilities.

[1002500001](../../errors/ArkTS错误码.md#section126501952132317)

The network is unavailable.

[1002500002](../../errors/ArkTS错误码.md#section1651105232319)

The user has not logged in with HUAWEI ID.

[1002500003](../../errors/ArkTS错误码.md#section665175210236)

Failed to check the fingerprint of the application bundle.

[1002500004](../../errors/ArkTS错误码.md#section17651105272310)

The application does not have the required permissions.

[1002500005](../../errors/ArkTS错误码.md#section1995615923313)

The user canceled the verification of the HUAWEI ID.

[1002500006](../../errors/ArkTS错误码.md#section10196176171810)

Internal error.

[1002500008](../../errors/ArkTS错误码.md#section177525511359)

Real-name verification is not supported for the HUAWEI ID.

[1002500011](../../errors/ArkTS错误码.md#section12860126792)

Your face does not match your facial image as proof of identity.

[1002500012](../../errors/ArkTS错误码.md#section1235141017912)

No real-name information is found for the HUAWEI ID.

[1002500013](../../errors/ArkTS错误码.md#section1792982614911)

Your name and ID number do not match.

[1002500014](../../errors/ArkTS错误码.md#section13455833098)

Too many real-name verification attempts.

[1002500015](../../errors/ArkTS错误码.md#section1377413361998)

The verificationToken parameter is incorrectly set.

[1002500016](../../errors/ArkTS错误码.md#section1239413431916)

This device does not support this API.

**示例：**

```ets
import { realName } from '@kit.AccountKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { util } from '@kit.ArkTS';

const request: realName.FacialRecognitionVerificationRequest = {
  verificationToken: "*<可调用华为账号服务实名信息校验接口获取>*", // 调用华为账号OpenRealName服务实名信息校验接口获取
  state: util.generateRandomUUID() // 建议使用generateRandomUUID生成state
}
hilog.info(0x0000, 'testTag', `verifyFacialRecognitionWithPromise params ${request}`);
// 此示例为代码片段，实际需在自定义组件实例中使用，以获取UIContext对象作为函数入参
realName.startFacialRecognitionVerification(this.getUIContext().getHostContext(), request).then(data => {
  const verifyResult = data as realName.FacialRecognitionVerificationResult;
  // 开发者处理verifyResult
  hilog.info(0x0000, 'testTag', 'Succeeded in verifying facial recognition.');
}).catch((error: BusinessError<Object>) => {
  dealAllError(error);
})

// 错误处理
function dealAllError(error: BusinessError<Object>): void {
  hilog.error(0x0000, 'testTag', `Failed to authorize. Code: ${error.code}, message: ${error.message}`);
}
```
