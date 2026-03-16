# extendService (华为账号增强服务)

本模块提供Account Kit的增强能力，包括身份验证、跳转账号中心等功能。

**起始版本：**4.0.0(10)

该服务目前仅对系统应用开放。

#### 导入模块

```ets
import { extendService } from '@kit.AccountKit';
```

#### IdType

该枚举为ID类型枚举对象。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.AuthenticationServices.HuaweiID.ExtendService

**起始版本：**4.0.0(10)

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

#### RiskLevel

该枚举为风险值枚举对象。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.AuthenticationServices.HuaweiID.ExtendService

**起始版本：**4.0.0(10)

**名称**

**值**

**说明**

LOW

1

低风险

HIGH

2

高风险

#### VerifyRequest

该类为身份验证请求对象。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.AuthenticationServices.HuaweiID.ExtendService

**起始版本：**4.0.0(10)

**名称**

**类型**

只读

可选

**说明**

idType

[IdType](#section816451553012)

否

否

属性idValue的ID类型。

idValue

string

否

否

用户获取的UnionID、OpenID值，传递的类型通过idType属性定义。长度限制1-256。

UnionID、OpenID值可以通过使用[LoginWithHuaweiIDResponse](../security/authentication (华为账号应用统一认证服务).md#section15454203811311)、[AuthorizationWithHuaweiIDResponse](../security/authentication (华为账号应用统一认证服务).md#section10418450161620)、[LoginPanel](../components/LoginPanel (华为账号Panel登录组件).md#section72281234181611)或[LoginWithHuaweiIDButton](../components/LoginWithHuaweiIDButton (华为账号Button登录组件).md#section1624716107193)接口获取，具体方法参考其示例代码。

sceneId

string

否

否

身份验证的场景值，该值与riskLevel属性一起代表了应用在华为账号服务器上的一组配置，包括验证次数、首次验证方式、二次验证方式等。长度限制1-10。

riskLevel

[RiskLevel](#section7913052143518)

否

否

风险等级，该值与sceneId一起代表了应用在华为账号服务器上的一组配置，一般风险等级高的场景，需要进行二次验证。

nonce

string

否

否

请求体中的nonce参数，长度限制1-64。该参数会包含在返回的verifyToken中，通过校验一致性，可用于防止重放攻击。

推荐开发者用随机数并做一致性校验。建议生成方式：[util.generateRandomUUID()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-util#utilgeneraterandomuuid9)。

**示例：**

```ets
import { extendService } from '@kit.AccountKit';
import { util } from '@kit.ArkTS';

// 创建请求参数
const request: extendService.VerifyRequest = {
  idType: extendService.IdType.UNION_ID,
  idValue: '*<可通过华为账号登录接口获取>*', // 该值可以通过华为账号登录接口获取
  sceneId: '*<触发身份认证的场景ID>*', // 触发身份验证的场景ID
  riskLevel: extendService.RiskLevel.LOW,
  nonce: util.generateRandomUUID() // 建议使用generateRandomUUID生成nonce
  }
```

#### VerifyResult

该类为身份验证请求结果对象。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.AuthenticationServices.HuaweiID.ExtendService

**起始版本：**4.0.0(10)

**名称**

**类型**

只读

可选

**说明**

verifyToken

string

是

否

身份验证返回的Token，JWT格式的数据。

**示例：**

```ets
import { extendService } from '@kit.AccountKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { util } from '@kit.ArkTS';
import { BusinessError } from '@kit.BasicServicesKit';

// 创建请求参数
const request: extendService.VerifyRequest = {
  idType: extendService.IdType.UNION_ID,
  idValue: '*<可通过华为账号登录接口获取>*', // 该值可以通过华为账号登录或授权接口获取
  sceneId: '*<触发身份认证的场景ID>*', // 触发身份验证的场景ID
  riskLevel: extendService.RiskLevel.LOW,
  nonce: util.generateRandomUUID() // 建议使用generateRandomUUID生成nonce
}

// 执行身份验证请求，并处理结果
try {
  // 此示例为代码片段，实际需在自定义组件实例中使用，以获取UIContext对象作为函数入参
  extendService.verifyAccount(this.getUIContext().getHostContext(), request, (error: BusinessError, data) => {
    if (error) {
      dealAllError(error);
      return;
    }
    const verifyResult = data as extendService.VerifyResult;
    hilog.info(0x0000, 'testTag', 'Succeeded in verifying.');
    const verifyToken = verifyResult.verifyToken;
    // 开发者处理verifyToken
  });
} catch (error) {
  dealAllError(error);
}

// 错误处理
function dealAllError(error: BusinessError): void {
  hilog.error(0x0000, 'testTag', `Failed to verify. Code: ${error.code}, message: ${error.message}`);
}
```

#### ExtendErrorCode

该枚举定义了Account Kit扩展模块错误码。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.AuthenticationServices.HuaweiID.ExtendService

**起始版本：**4.0.0(10)

**名称**

**值**

**说明**

INVALID_PARAMETER

[401](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal#section401-参数检查失败)

参数检查失败

NETWORK_ERROR

[1001600001](../../errors/ArkTS错误码.md#section1211715201154)

网络不可用

ACCOUNT_NOT_LOGGED_IN

[1001600002](../../errors/ArkTS错误码.md#section174914372610)

用户未登录华为账号

PACKAGE_FINGERPRINT_CHECK_ERROR

[1001600003](../../errors/ArkTS错误码.md#section176803402816)

应用指纹证书校验失败

PERMISSION_CHECK_ERROR

[1001600004](../../errors/ArkTS错误码.md#section1924781781013)

应用未申请对应permissions权限

USER_CANCELED

[1001600005](../../errors/ArkTS错误码.md#section051982312124)

用户取消当前操作

VERIFICATION_FACTOR_UNAVAILABLE

[1001600006](../../errors/ArkTS错误码.md#section1140794171313)

当前设备不支持此验证要素

INTERNAL_ERROR

[1001600007](../../errors/ArkTS错误码.md#section7982145091511)

内部错误

#### verifyAccount

verifyAccount(context: common.Context, request: VerifyRequest, callback: AsyncCallback<VerifyResult>): void

执行Account Kit身份验证请求，使用Callback异步回调。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.AuthenticationServices.HuaweiID.ExtendService

**起始版本：**4.0.0(10)

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

 说明：

- 在4.0.0(10)版本，参数类型为[UIAbilityContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext)。
- 从4.1.0(11)版本开始，参数类型为[Context](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-context)。

request

[VerifyRequest](#section9615740103819)

是

身份验证请求对象，包含请求参数。

callback

AsyncCallback<[VerifyResult](#section155352089012)>

是

回调函数。

当身份验证请求成功，err为undefined，data为获取到的[VerifyResult](#section155352089012)对象；否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[ArkTS错误码](../../errors/ArkTS错误码.md)。

错误码ID

错误信息

[401](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal#section401-参数检查失败)

Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

[1001600001](../../errors/ArkTS错误码.md#section1211715201154)

The network is unavailable.

[1001600002](../../errors/ArkTS错误码.md#section174914372610)

The user has not logged in with HUAWEI ID.

[1001600003](../../errors/ArkTS错误码.md#section176803402816)

Failed to check the fingerprint of the application bundle.

[1001600004](../../errors/ArkTS错误码.md#section1924781781013)

The application does not have the required permissions.

[1001600005](../../errors/ArkTS错误码.md#section051982312124)

The user canceled the current operation.

[1001600006](../../errors/ArkTS错误码.md#section1140794171313)

The requested verification factors are unavailable on the device.

[1001600007](../../errors/ArkTS错误码.md#section7982145091511)

Internal error.

**示例：**

```ets
import { extendService } from '@kit.AccountKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { util } from '@kit.ArkTS';
import { BusinessError } from '@kit.BasicServicesKit';

// 创建请求参数
const request: extendService.VerifyRequest = {
  idType: extendService.IdType.UNION_ID,
  idValue: '*<可通过华为账号登录接口获取>*', // 该值可以通过华为账号登录接口获取
  sceneId: '*<触发身份认证的场景ID>*', // 触发身份验证的场景ID，通过配置申请获取
  riskLevel: extendService.RiskLevel.LOW,
  nonce: util.generateRandomUUID() // 建议使用generateRandomUUID生成nonce
}

// 执行身份验证请求，并处理结果
try {
  // 此示例为代码片段，实际需在自定义组件实例中使用，以获取UIContext对象作为函数入参
  extendService.verifyAccount(this.getUIContext().getHostContext(), request, (error, data) => {
    if (error) {
      dealAllError(error);
      return;
    }
    const verifyResult = data as extendService.VerifyResult;
    hilog.info(0x0000, 'testTag', 'Succeeded in verifying.');
    const verifyToken = verifyResult.verifyToken;
    // 开发者处理verifyToken
  });
} catch (error) {
  dealAllError(error);
}

// 错误处理
function dealAllError(error: BusinessError): void {
  hilog.error(0x0000, 'testTag', `Failed to verify. Code: ${error.code}, message: ${error.message}`);
}
```

#### verifyAccount

verifyAccount(context: common.Context, request: VerifyRequest): Promise<VerifyResult>

执行Account Kit身份验证请求，使用Promise异步回调。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.AuthenticationServices.HuaweiID.ExtendService

**起始版本：**4.0.0(10)

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

 说明：

- 在4.0.0(10)版本，参数类型为[UIAbilityContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext)。
- 从4.1.0(11)版本开始，参数类型为[Context](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-context)。

request

[VerifyRequest](#section9615740103819)

是

身份验证请求对象，包含请求参数。

**返回值：**

类型

说明

Promise<[VerifyResult](#section155352089012)>

Promise对象，返回[VerifyResult](#section155352089012)对象。

**错误码：**

以下错误码的详细介绍请参见[ArkTS错误码](../../errors/ArkTS错误码.md)。

错误码ID

错误信息

[401](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal#section401-参数检查失败)

Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

[1001600001](../../errors/ArkTS错误码.md#section1211715201154)

The network is unavailable.

[1001600002](../../errors/ArkTS错误码.md#section174914372610)

The user has not logged in with HUAWEI ID.

[1001600003](../../errors/ArkTS错误码.md#section176803402816)

Failed to check the fingerprint of the application bundle.

[1001600004](../../errors/ArkTS错误码.md#section1924781781013)

The application does not have the required permissions.

[1001600005](../../errors/ArkTS错误码.md#section051982312124)

The user canceled the current operation.

[1001600006](../../errors/ArkTS错误码.md#section1140794171313)

The requested verification factors are unavailable on the device.

[1001600007](../../errors/ArkTS错误码.md#section7982145091511)

Internal error.

**示例：**

```ets
import { extendService } from '@kit.AccountKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { util } from '@kit.ArkTS';
import { BusinessError } from '@kit.BasicServicesKit';

// 创建请求参数
const request: extendService.VerifyRequest = {
  idType: extendService.IdType.UNION_ID,
  idValue: '*<可通过华为账号登录接口获取>*', // 该值可以通过华为账号登录接口获取
  sceneId: '*<触发身份认证的场景ID>*', // 触发身份验证的场景ID，通过配置申请获取
  riskLevel: extendService.RiskLevel.LOW,
  nonce: util.generateRandomUUID() // 建议使用generateRandomUUID生成nonce
}

// 此示例为代码片段，实际需在自定义组件实例中使用，以获取UIContext对象作为函数入参
// 执行身份验证请求，并处理结果
extendService.verifyAccount(this.getUIContext().getHostContext(), request).then(data => {
  const verifyResult = data as extendService.VerifyResult;
  hilog.info(0x0000, 'testTag', 'Succeeded in verifying.');
  const verifyToken = verifyResult.verifyToken;
  // 开发者处理verifyToken
}).catch((error: BusinessError) => {
  dealAllError(error);
})

// 错误处理
function dealAllError(error: BusinessError): void {
  hilog.error(0x0000, 'testTag', `Failed to verify. Code: ${error.code}, message: ${error.message}`);
}
```

#### startAccountCenter

startAccountCenter(context: common.Context, callback: AsyncCallback<void>): void

当开发者需要实现查看当前登录的华为账号的基本信息时，执行打开账号中心请求，会拉起账号中心页面，使用Callback异步回调。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.AuthenticationServices.HuaweiID.ExtendService

**起始版本：**4.0.0(10)

**参数：**

参数名

类型

必填

说明

context

[common.Context](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-common#context)

是

Context上下文。

可支持的Context有：[UIAbilityContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext)和[UIExtensionContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiextensioncontext)。不支持应用在半模态、弹出框、子窗口等非全页面组件中使用[UIExtensionContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiextensioncontext)调用。

 说明：

- 在4.0.0(10)版本，参数类型为[UIAbilityContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext)。
- 从4.1.0(11)版本开始，参数类型为[Context](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-context)。

callback

AsyncCallback<void>

是

回调函数。

当执行打开账号中心请求成功，err为undefined；否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[ArkTS错误码](../../errors/ArkTS错误码.md)。

错误码ID

错误信息

[401](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal#section401-参数检查失败)

Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.

[1001600001](../../errors/ArkTS错误码.md#section1211715201154)

The network is unavailable.

[1001600002](../../errors/ArkTS错误码.md#section174914372610)

The user has not logged in with HUAWEI ID.

[1001600003](../../errors/ArkTS错误码.md#section176803402816)

Failed to check the fingerprint of the application bundle.

[1001600004](../../errors/ArkTS错误码.md#section1924781781013)

The application does not have the required permissions.

[1001600007](../../errors/ArkTS错误码.md#section7982145091511)

Internal error.

**示例：**

```ets
import { extendService } from '@kit.AccountKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 执行打开账号中心请求，并处理结果
try {
  // 此示例为代码片段，实际需在自定义组件实例中使用，以获取UIContext对象作为函数入参
  extendService.startAccountCenter(this.getUIContext().getHostContext(), (error: BusinessError) => {
    if (error) {
      dealAllError(error);
      return;
    }
    hilog.info(0x0000, 'testTag', 'Succeeded in starting account center');
  });
} catch (error) {
  dealAllError(error);
}

// 错误处理
function dealAllError(error: BusinessError): void {
  hilog.error(0x0000, 'testTag', `Failed to startAccountCenter. Code: ${error.code}, message: ${error.message}`);
}
```

#### startAccountCenter

startAccountCenter(context: common.Context): Promise<void>

当开发者需要实现查看当前登录的华为账号的基本信息时，执行打开账号中心请求，会拉起账号中心页面，使用Promise异步回调。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.AuthenticationServices.HuaweiID.ExtendService

**起始版本：**4.0.0(10)

**参数：**

参数名

类型

必填

说明

context

[common.Context](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-common#context)

是

Context上下文。

可支持的Context有：[UIAbilityContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext)和[UIExtensionContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiextensioncontext)。不支持应用在半模态、弹出框、子窗口等非全页面组件中使用[UIExtensionContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiextensioncontext)调用。

 说明：

- 在4.0.0(10)版本，参数类型为[UIAbilityContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext)。
- 从4.1.0(11)版本开始，参数类型为[Context](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-context)。

**返回值：**

类型

说明

Promise<void>

Promise对象，无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[ArkTS错误码](../../errors/ArkTS错误码.md)。

错误码ID

错误信息

[401](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal#section401-参数检查失败)

Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.

[1001600001](../../errors/ArkTS错误码.md#section1211715201154)

The network is unavailable.

[1001600002](../../errors/ArkTS错误码.md#section174914372610)

The user has not logged in with HUAWEI ID.

[1001600003](../../errors/ArkTS错误码.md#section176803402816)

Failed to check the fingerprint of the application bundle.

[1001600004](../../errors/ArkTS错误码.md#section1924781781013)

The application does not have the required permissions.

[1001600007](../../errors/ArkTS错误码.md#section7982145091511)

Internal error.

**示例：**

```ets
import { extendService } from '@kit.AccountKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 此示例为代码片段，实际需在自定义组件实例中使用，以获取UIContext对象作为函数入参
// 执行打开账号中心请求，并处理结果
extendService.startAccountCenter(this.getUIContext().getHostContext()).then(() => {
  hilog.info(0x0000, 'testTag', 'Succeeded in starting account center');
}).catch((error: BusinessError<Object>) => {
  dealAllError(error);
})

// 错误处理
function dealAllError(error: BusinessError<Object>): void {
  hilog.error(0x0000, 'testTag', `Failed to startAccountCenter. Code: ${error.code}, message: ${error.message}`);
}
```