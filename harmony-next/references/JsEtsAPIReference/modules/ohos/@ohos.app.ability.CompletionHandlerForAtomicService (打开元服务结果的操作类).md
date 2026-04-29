# @ohos.app.ability.CompletionHandlerForAtomicService (打开元服务结果的操作类)

CompletionHandlerForAtomicService作为[AtomicServiceOptions](@ohos.app.ability.AtomicServiceOptions (openAtomicService可选参数).md)的可选参数，用于接收打开元服务请求的结果。

-

本模块首批接口从API version 20 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

-

本模块接口仅可在Stage模型下使用。

#### 导入模块

```ets
import { CompletionHandlerForAtomicService } from '@kit.AbilityKit';
```

#### FailureCode

打开元服务失败的特定错误码。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| FAILURE_CODE_SYSTEM_MALFUNCTION | 0 | 表示由于系统错误（如跳转弹框崩溃）而无法打开元服务。 |
| FAILURE_CODE_USER_CANCEL | 1 | 用户取消。 |
| FAILURE_CODE_USER_REFUSE | 2 | 用户拒绝。 |

#### CompletionHandlerForAtomicService

CompletionHandlerForAtomicService提供了[onAtomicServiceRequestSuccess](#ZH-CN_TOPIC_0000002553360455__onatomicservicerequestsuccess)和[onAtomicServiceRequestFailure](#ZH-CN_TOPIC_0000002553360455__onatomicservicerequestfailure)两个回调函数，分别在打开元服务成功和失败时回调。

#### onAtomicServiceRequestSuccess

onAtomicServiceRequestSuccess(appId: string): void

打开元服务成功时的回调函数。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| appId | string | 是 | 被拉起元服务的appId。 |

**示例：**

参见[CompletionHandlerForAtomicService示例](#ZH-CN_TOPIC_0000002553360455__completionhandlerforatomicservice示例)。

#### onAtomicServiceRequestFailure

onAtomicServiceRequestFailure(appId: string, failureCode: FailureCode, failureMessage: string): void

打开元服务失败时的回调函数。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| appId | string | 是 | 被拉起元服务的appId。 |
| failureCode | FailureCode | 是 | 失败原因的错误码。 |
| failureMessage | string | 是 | 失败原因的描述。 |

**示例：**

参见[CompletionHandlerForAtomicService示例](#ZH-CN_TOPIC_0000002553360455__completionhandlerforatomicservice示例)。

#### CompletionHandlerForAtomicService示例

```ets
import { AbilityConstant, AtomicServiceOptions, common, UIAbility, Want, CompletionHandlerForAtomicService, FailureCode } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    let completionHandler: CompletionHandlerForAtomicService = {
      onAtomicServiceRequestSuccess(appId: string) {
        hilog.info(0x0000, 'testTag', `appId:${appId}`);
      },
      onAtomicServiceRequestFailure(appId: string, failureCode: FailureCode, failureMessage: string) {
        hilog.info(0x0000, 'testTag', `appId:${appId}, failureCode:${failureCode}, failureMessage:${failureMessage}`);
      }
    };
    let options: AtomicServiceOptions = {
      completionHandlerForAtomicService: completionHandler
    };
    let appId: string = '5765880207853275489'; // 根据实际appId修改此值
    this.context.openAtomicService(appId, options).then((result: common.AbilityResult) => {
      hilog.info(0x0000, 'testTag', `openAtomicService succeed:${JSON.stringify(result)}`);
    }).catch((err: BusinessError) => {
      hilog.error(0x0000, 'testTag', `openAtomicService failed:${JSON.stringify(err)}`);
    });
  }
```