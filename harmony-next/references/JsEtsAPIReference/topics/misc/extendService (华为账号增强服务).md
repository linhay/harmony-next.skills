# extendService (华为账号增强服务)

本模块提供Account Kit的增强能力，包括身份验证、跳转账号中心等功能。

起始版本： 4.0.0(10)

  ![image](public_sys-resources/note_3.0-zh-cn.webp)

该服务目前仅对系统应用开放。

**导入模块**

```ets
import { extendService } from '@kit.AccountKit';
```

**IdType**

该枚举为ID类型枚举对象。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.AuthenticationServices.HuaweiID.ExtendService

起始版本： 4.0.0(10)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| USER_ID | 1 | 华为账号用户的UID。 说明： 该参数仅对系统应用开放。 |
| OPEN_ID | 2 | 华为账号用户的OpenID。具体格式要求请参考OpenID和UnionID的格式说明。 |
| UNION_ID | 3 | 华为账号用户的UnionID。具体格式要求请参考OpenID和UnionID的格式说明。 |

**RiskLevel**

该枚举为风险值枚举对象。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.AuthenticationServices.HuaweiID.ExtendService

起始版本： 4.0.0(10)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| LOW | 1 | 低风险 |
| HIGH | 2 | 高风险 |

**VerifyRequest**

该类为身份验证请求对象。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.AuthenticationServices.HuaweiID.ExtendService

起始版本： 4.0.0(10)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| idType | IdType | 否 | 否 | 属性idValue的ID类型。 |
| idValue | string | 否 | 否 | 用户获取的UnionID、OpenID值，传递的类型通过idType属性定义。长度限制1-256。 UnionID、OpenID值可以通过使用LoginWithHuaweiIDResponse、AuthorizationWithHuaweiIDResponse、LoginPanel或LoginWithHuaweiIDButton接口获取，具体方法参考其示例代码。 |
| sceneId | string | 否 | 否 | 身份验证的场景值，该值与riskLevel属性一起代表了应用在华为账号服务器上的一组配置，包括验证次数、首次验证方式、二次验证方式等。长度限制1-10。 |
| riskLevel | RiskLevel | 否 | 否 | 风险等级，该值与sceneId一起代表了应用在华为账号服务器上的一组配置，一般风险等级高的场景，需要进行二次验证。 |
| nonce | string | 否 | 否 | 请求体中的nonce参数，长度限制1-64。该参数会包含在返回的verifyToken中，通过校验一致性，可用于防止重放攻击。 推荐开发者用随机数并做一致性校验。建议生成方式：util.generateRandomUUID()。 |

示例：

```ets
import { extendService } from '@kit.AccountKit';
import { util } from '@kit.ArkTS';

// 创建请求参数
const request: extendService.VerifyRequest = {
  idType: extendService.IdType.UNION_ID,
  idValue: '<可通过华为账号登录接口获取>', // 该值可以通过华为账号登录接口获取
  sceneId: '<触发身份认证的场景ID>', // 触发身份验证的场景ID
  riskLevel: extendService.RiskLevel.LOW,
  nonce: util.generateRandomUUID() // 建议使用generateRandomUUID生成nonce
  }
```

**VerifyResult**

该类为身份验证请求结果对象。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.AuthenticationServices.HuaweiID.ExtendService

起始版本： 4.0.0(10)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| verifyToken | string | 是 | 否 | 身份验证返回的Token，JWT格式的数据。 |

示例：

```ets
import { extendService } from '@kit.AccountKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { util } from '@kit.ArkTS';
import { BusinessError } from '@kit.BasicServicesKit';

// 创建请求参数
const request: extendService.VerifyRequest = {
  idType: extendService.IdType.UNION_ID,
  idValue: '<可通过华为账号登录接口获取>', // 该值可以通过华为账号登录或授权接口获取
  sceneId: '<触发身份认证的场景ID>', // 触发身份验证的场景ID
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

**ExtendErrorCode**

该枚举定义了Account Kit扩展模块错误码。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.AuthenticationServices.HuaweiID.ExtendService

起始版本： 4.0.0(10)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| INVALID_PARAMETER | 401 | 参数检查失败。 元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| NETWORK_ERROR | 1001600001 | 网络不可用。 元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| ACCOUNT_NOT_LOGGED_IN | 1001600002 | 用户未登录华为账号。 元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| PACKAGE_FINGERPRINT_CHECK_ERROR | 1001600003 | 应用指纹证书校验失败。 元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| PERMISSION_CHECK_ERROR | 1001600004 | 应用未申请对应permissions权限。 元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| USER_CANCELED | 1001600005 | 用户取消当前操作。 元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| VERIFICATION_FACTOR_UNAVAILABLE | 1001600006 | 当前设备不支持此验证要素。 元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| INTERNAL_ERROR | 1001600007 | 内部错误。 元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| DEVICE_NOT_SUPPORTED | 1001600011 | 该设备不支持此API。 起始版本：6.1.0(23) 元服务API： 从版本6.1.0(23)开始，该接口支持在元服务中使用。 |

**verifyAccount**

verifyAccount(context: common.Context, request: VerifyRequest, callback: AsyncCallback<VerifyResult>): void

执行Account Kit身份验证请求，使用Callback异步回调。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.AuthenticationServices.HuaweiID.ExtendService

起始版本： 4.0.0(10)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | common.Context | 是 | Context上下文。 应用可支持的Context有：UIAbilityContext和UIExtensionContext。不支持应用在半模态、弹出框、子窗口等非全页面组件中使用UIExtensionContext调用。 元服务可支持的Context有：UIAbilityContext。 说明： - 在4.0.0(10)版本，参数类型为UIAbilityContext。 - 从4.1.0(11)版本开始，参数类型为Context。 |
| request | VerifyRequest | 是 | 身份验证请求对象，包含请求参数。 |
| callback | AsyncCallback<VerifyResult> | 是 | 回调函数。 当身份验证请求成功，err为undefined，data为获取到的VerifyResult对象；否则为错误对象。 |

错误码：

以下错误码的详细介绍请参见[ArkTS错误码](ArkTS错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 1001600001 | The network is unavailable. |
| 1001600002 | The user has not logged in with HUAWEI ID. |
| 1001600003 | Failed to check the fingerprint of the application bundle. |
| 1001600004 | The application does not have the required permissions. |
| 1001600005 | The user canceled the current operation. |
| 1001600006 | The requested verification factors are unavailable on the device. |
| 1001600007 | Internal error. |

示例：

```ets
import { extendService } from '@kit.AccountKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { util } from '@kit.ArkTS';
import { BusinessError } from '@kit.BasicServicesKit';

// 创建请求参数
const request: extendService.VerifyRequest = {
  idType: extendService.IdType.UNION_ID,
  idValue: '<可通过华为账号登录接口获取>', // 该值可以通过华为账号登录接口获取
  sceneId: '<触发身份认证的场景ID>', // 触发身份验证的场景ID，通过配置申请获取
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

**verifyAccount**

verifyAccount(context: common.Context, request: VerifyRequest): Promise<VerifyResult>

执行Account Kit身份验证请求，使用Promise异步回调。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.AuthenticationServices.HuaweiID.ExtendService

起始版本： 4.0.0(10)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | common.Context | 是 | Context上下文。 应用可支持的Context有：UIAbilityContext和UIExtensionContext。不支持应用在半模态、弹出框、子窗口等非全页面组件中使用UIExtensionContext调用。 元服务可支持的Context有：UIAbilityContext。 说明： - 在4.0.0(10)版本，参数类型为UIAbilityContext。 - 从4.1.0(11)版本开始，参数类型为Context。 |
| request | VerifyRequest | 是 | 身份验证请求对象，包含请求参数。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<VerifyResult> | Promise对象，返回VerifyResult对象。 |

错误码：

以下错误码的详细介绍请参见[ArkTS错误码](ArkTS错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 1001600001 | The network is unavailable. |
| 1001600002 | The user has not logged in with HUAWEI ID. |
| 1001600003 | Failed to check the fingerprint of the application bundle. |
| 1001600004 | The application does not have the required permissions. |
| 1001600005 | The user canceled the current operation. |
| 1001600006 | The requested verification factors are unavailable on the device. |
| 1001600007 | Internal error. |

示例：

```ets
import { extendService } from '@kit.AccountKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { util } from '@kit.ArkTS';
import { BusinessError } from '@kit.BasicServicesKit';

// 创建请求参数
const request: extendService.VerifyRequest = {
  idType: extendService.IdType.UNION_ID,
  idValue: '<可通过华为账号登录接口获取>', // 该值可以通过华为账号登录接口获取
  sceneId: '<触发身份认证的场景ID>', // 触发身份验证的场景ID，通过配置申请获取
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

**startAccountCenter**

startAccountCenter(context: common.Context, callback: AsyncCallback<void>): void

当开发者需要实现查看当前登录的华为账号的基本信息时，执行打开账号中心请求，会拉起账号中心页面，使用Callback异步回调。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.AuthenticationServices.HuaweiID.ExtendService

设备行为差异： 该接口在Phone、PC/2in1、Tablet、TV中可正常调用，在其他设备类型中返回1001600011错误码。

起始版本： 4.0.0(10)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | common.Context | 是 | Context上下文。 可支持的Context有：UIAbilityContext和UIExtensionContext。不支持应用在半模态、弹出框、子窗口等非全页面组件中使用UIExtensionContext调用。 说明： - 在4.0.0(10)版本，参数类型为UIAbilityContext。 - 从4.1.0(11)版本开始，参数类型为Context。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 当执行打开账号中心请求成功，err为undefined；否则为错误对象。 |

错误码：

以下错误码的详细介绍请参见[ArkTS错误码](ArkTS错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 1001600001 | The network is unavailable. |
| 1001600002 | The user has not logged in with HUAWEI ID. |
| 1001600003 | Failed to check the fingerprint of the application bundle. |
| 1001600004 | The application does not have the required permissions. |
| 1001600007 | Internal error. |
| 1001600011 | This device does not support this API. |

示例：

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

**startAccountCenter**

startAccountCenter(context: common.Context): Promise<void>

当开发者需要实现查看当前登录的华为账号的基本信息时，执行打开账号中心请求，会拉起账号中心页面，使用Promise异步回调。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.AuthenticationServices.HuaweiID.ExtendService

设备行为差异： 该接口在Phone、PC/2in1、Tablet、TV中可正常调用，在其他设备类型中返回1001600011错误码。

起始版本： 4.0.0(10)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | common.Context | 是 | Context上下文。 可支持的Context有：UIAbilityContext和UIExtensionContext。不支持应用在半模态、弹出框、子窗口等非全页面组件中使用UIExtensionContext调用。 说明： - 在4.0.0(10)版本，参数类型为UIAbilityContext。 - 从4.1.0(11)版本开始，参数类型为Context。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果的Promise对象。 |

错误码：

以下错误码的详细介绍请参见[ArkTS错误码](ArkTS错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 1001600001 | The network is unavailable. |
| 1001600002 | The user has not logged in with HUAWEI ID. |
| 1001600003 | Failed to check the fingerprint of the application bundle. |
| 1001600004 | The application does not have the required permissions. |
| 1001600007 | Internal error. |
| 1001600011 | This device does not support this API. |

示例：

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