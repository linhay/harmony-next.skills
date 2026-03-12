# realNameService(身份验证服务)

本模块提供身份验证服务，包括“实名信息验证”、“实名信息授权”和“人脸核身实人验证”三种功能。

**模型约束：**本模块接口仅可在Stage模型下使用。

**元服务API**： 从版本5.1.1(19)开始，该接口支持在元服务中使用。

**起始版本：**5.1.1(19)

#### 导入模块

```ets
import { realNameService } from '@kit.PaymentKit';
```

#### realNameService.startRealNameVerification

startRealNameVerification(context: common.UIAbilityContext | common.UIExtensionContext, preVerifyId: string): Promise<string>

该方法提供实名信息验证功能，调用该方法后会拉起实名信息验证授权组件，验证完成后使用Promise异步返回。调用该方法前请确保网络已连接。

**模型约束**：此接口仅可在Stage模型下使用。

**元服务API：**从版本5.1.1(19)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Payment.RealNameService

**起始版本：**5.1.1(19)

**参数**：

**参数名**

**类型**

必填

**说明**

context

common.[UIAbilityContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext) | common.[UIExtensionContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiextensioncontext)

是

UIAbility上下文。

preVerifyId

string

是

预验证ID。获取方式请参考[实名信息预验证](实名信息预验证.md)。

**返回值**:

类型

说明

Promise<string>

Promise对象。返回实名信息验证ID，用于[实名信息验证结果查询](实名信息验证结果查询.md)。

**错误码**：

 以下错误码的详细介绍请参见 [ArkTS API错误码](ArkTS API错误码.md)。

错误码ID

错误信息（此处仅提供错误抛出的关键信息）

1020100000

The application does not have the required capability.

1020100001

The user did not accept the agreement.

1020100002

The user canceled the operation.

1020100003

The pre-verify ID is invalid.

1020100004

The network is unavailable.

1020100005

System internal error.

1020100008

The app ID does not match.

1020100009

The user ID does not match.

**示例**：

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { realNameService } from '@kit.PaymentKit';
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct Index {
  context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
  requestStartRealNameVerificationPromise() {
    // use your own preVerifyId
    let preVerifyId = '';
    realNameService.startRealNameVerification(this.context, preVerifyId)
      .then((verifyResultId: string) => {
        // verify success
        console.info(`succeeded in verifying, verifyResultId: ${verifyResultId}`);
      })
      .catch((error: BusinessError) => {
        // failed to verify
        console.error(`failed to verify, error.code: ${error.code}, error.message: ${error.message}`);
      });
  }

  build() {
    Column() {
      Button('requestStartRealNameVerificationPromise')
        .type(ButtonType.Capsule)
        .width('50%')
        .margin(20)
        .onClick(() => {
          this.requestStartRealNameVerificationPromise();
        })
      }
    .width('100%')
    .height('100%')
  }
}
```

#### realNameService.startRealNameAuth

startRealNameAuth(context: common.UIAbilityContext | common.UIExtensionContext): Promise<string>

该方法提供实名信息授权功能，调用该方法后会拉起实名信息授权组件，授权完成后使用Promise异步返回。调用该方法前请确保网络已连接。

**模型约束**：此接口仅可在Stage模型下使用。

**元服务API：**从版本5.1.1(19)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Payment.RealNameService

**起始版本：**5.1.1(19)

**参数**：

**参数名**

**类型**

必填

**说明**

context

common.[UIAbilityContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext) | common.[UIExtensionContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiextensioncontext)

是

UIAbility上下文。

**返回值**:

类型

说明

Promise<string>

Promise对象。返回实名信息授权ID，用于[实名信息授权结果查询](实名信息授权结果查询.md)。

**错误码**：

 以下错误码的详细介绍请参见 [ArkTS API错误码](ArkTS API错误码.md)。

错误码ID

错误信息（此处仅提供错误抛出的关键信息）

1020100000

The application does not have the required capability.

1020100001

The user did not accept the agreement.

1020100002

The user canceled the operation.

1020100004

The network is unavailable.

1020100005

System internal error.

**示例**：

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { realNameService } from '@kit.PaymentKit';
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct Index {
  context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
  requestStartRealNameAuthPromise() {
    realNameService.startRealNameAuth(this.context)
      .then((realNameAuthId: string) => {
        // authorize success
        console.info(`succeeded in authorizing, realNameAuthId: ${realNameAuthId}`);
      })
      .catch((error: BusinessError) => {
        // failed to authorise
        console.error(`failed to authorise, error.code: ${error.code}, error.message: ${error.message}`);
      });
  }

  build() {
    Column() {
      Button('requestStartRealNameAuthPromise')
        .type(ButtonType.Capsule)
        .width('50%')
        .margin(20)
        .onClick(() => {
          this.requestStartRealNameAuthPromise();
        })
      }
    .width('100%')
    .height('100%')
  }
}
```

#### realNameService.startFaceVerification

startFaceVerification(context: common.UIAbilityContext | common.UIExtensionContext, preVerifyId: string): Promise<string>

该方法提供人脸核身实人验证功能，调用该方法后会拉起人脸核身实人验证组件，验证完成后使用Promise异步返回。调用该方法前请确保网络已连接。

**模型约束**：此接口仅可在Stage模型下使用。

**元服务API：**从版本5.1.1(19)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Payment.RealNameService

**起始版本：**5.1.1(19)

**参数**：

**参数名**

**类型**

必填

**说明**

context

common.[UIAbilityContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext) | common.[UIExtensionContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiextensioncontext)

是

UIAbility上下文。

preVerifyId

string

是

预验证ID。获取方式请参考[人脸核身实人预验证](人脸核身实人预验证.md)。

**返回值**:

类型

说明

Promise<string>

Promise对象。返回验证结果ID，用于[人脸核身实人验证结果查询](人脸核身实人验证结果查询.md)。

**错误码**：

 以下错误码的详细介绍请参见 [ArkTS API错误码](ArkTS API错误码.md)。

错误码ID

错误信息（此处仅提供错误抛出的关键信息）

1020100000

The application does not have the required capability.

1020100001

The user did not accept the agreement.

1020100002

The user canceled the operation.

1020100003

The pre-verify ID is invalid.

1020100004

The network is unavailable.

1020100005

System internal error.

1020100006

The camera permission is not granted.

1020100007

The liveness detection failed.

1020100008

The app ID does not match.

1020100009

The user ID does not match.

**示例**：

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { realNameService } from '@kit.PaymentKit';
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct Index {
  context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
  requestStartFaceVerificationPromise() {
    // use your own preVerifyId
    let preVerifyId = '';
    realNameService.startFaceVerification(this.context, preVerifyId)
      .then((verifyResultId:string ) => {
        // face verification success
        console.info(`succeeded in face verifying, verifyResultId: ${verifyResultId}`);
      })
      .catch((error: BusinessError) => {
        // failed to face verification
        console.error(`failed to face verification, error.code: ${error.code}, error.message: ${error.message}`);
      });
  }

  build() {
    Column() {
      Button('requestStartFaceVerificationPromise')
        .type(ButtonType.Capsule)
        .width('50%')
        .margin(20)
        .onClick(() => {
          this.requestStartFaceVerificationPromise();
        })
      }
    .width('100%')
    .height('100%')
  }
}
```