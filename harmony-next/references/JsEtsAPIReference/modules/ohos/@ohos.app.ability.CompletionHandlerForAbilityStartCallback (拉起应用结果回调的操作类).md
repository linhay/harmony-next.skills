# @ohos.app.ability.CompletionHandlerForAbilityStartCallback (拉起应用结果回调的操作类)

CompletionHandlerForAbilityStartCallback作为[AbilityStartCallback](../../topics/system-services/AbilityStartCallback.md)的可选参数，用于返回垂域面板拉起指定类型的Ability组件的回调结果。

-

本模块首批接口从API version 21 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

-

本模块接口仅可在Stage模型下使用。

#### 导入模块

```ets
import { CompletionHandlerForAbilityStartCallback } from '@kit.AbilityKit';
```

#### CompletionHandlerForAbilityStartCallback

CompletionHandlerForAbilityStartCallback提供了onRequestSuccess和onRequestFailure两个回调函数属性，分别在拉起指定类型的Ability组件成功和失败时回调。

#### 属性

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

名称类型只读可选说明onRequestSuccess[OnRequestSuccessFn](#ZH-CN_TOPIC_0000002497604584__onrequestsuccessfn)否是

拉起指定类型的Ability组件成功时的回调函数。

**元服务API**：从API version 21开始，该接口支持在元服务中使用。

onRequestFailure[OnRequestFailureFn](#ZH-CN_TOPIC_0000002497604584__onrequestfailurefn)否是

拉起指定类型的Ability组件失败时的回调函数。

**元服务API**：从API version 21开始，该接口支持在元服务中使用。

#### OnRequestSuccessFn

type OnRequestSuccessFn = (name: string) => void

拉起指定类型的Ability组件成功时的回调函数类型。

**元服务API**：从API version 21开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

参数名类型必填说明namestring是

被拉起Ability组件或系统操作的名称。

Ability组件名称采用'[bundleName]#[moduleName]#[abilityName]'格式拼接。

**示例：**

参见[OnRequestFailureFn](#ZH-CN_TOPIC_0000002497604584__onrequestfailurefn)。

#### OnRequestFailureFn

type OnRequestFailureFn = (name: string, failureCode: AbilityStartFailureCode, failureMessage: string) => void

拉起指定类型的Ability组件失败时的回调函数类型。

**元服务API**：从API version 21开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

参数名类型必填说明namestring是

被拉起Ability组件或系统操作的名称。

Ability组件名称采用'[bundleName]#[moduleName]#[abilityName]'格式拼接。如果用户自动取消拉起，name为空。

failureCode[AbilityStartFailureCode](#ZH-CN_TOPIC_0000002497604584__abilitystartfailurecode)是失败原因的错误码。failureMessagestring是失败原因的描述。

**示例：**

```ets
import { AbilityStartFailureCode, common, CompletionHandlerForAbilityStartCallback } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  @State message: string = 'Hello World';
  context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;

  completionHandler: CompletionHandlerForAbilityStartCallback = {
    onRequestSuccess: (name: string) => {
      console.info(`testTag onRequestSuccess name` + name);
    },
    onRequestFailure: (name: string, failureCode: AbilityStartFailureCode, failureMessage: string) => {
      console.info(`testTag onRequestFailure name: ` + name + `, failureCode:` + failureCode + `, failureMessage:` +
        failureMessage);
    }
  };
  abilityStartCallback: common.AbilityStartCallback = {
    onError: (code: number, name: string, message: string) => {
      console.info(`testTag code:` + code + `name:` + name + `message:` + message);
    },
    onResult: (abilityResult: common.AbilityResult) => {
      console.info(`testTag resultCode:` + abilityResult.resultCode + `bundleName:` + abilityResult.want?.bundleName);
    },
    completionHandler: this.completionHandler,
  };

  build() {
    Column({ space: 10 }) {
      Button('test')
        .type(ButtonType.Capsule)
        .offset({ x: 0, y: 60 })
        .width('80%')
        .type(ButtonType.Capsule)
        .margin({ top: 10 })
        .onClick(() => {
          let wantParam: Record<string, Object> = {
            'time': '2023-10-23 20:45'
          };
          this.context.startAbilityByType("share", wantParam, this.abilityStartCallback).then(() => {
            console.info(`startAbilityByType success`);
          }).catch((err: BusinessError) => {
            console.error(`startAbilityByType fail, err: ${JSON.stringify(err)}`);
          });
        })
    }
  }
}
```

#### AbilityStartFailureCode

拉起指定类型的Ability组件失败的特定错误码。

**元服务API**：从API version 21开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

名称值说明FAILURE_CODE_SYSTEM_MALFUNCTION0表示由于系统错误（如跳转弹框崩溃）而无法拉起Ability组件。FAILURE_CODE_USER_CANCEL1用户取消。