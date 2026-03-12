# @ohos.app.ability.CompletionHandler (拉起应用结果的操作类)

CompletionHandler作为[StartOptions](@ohos.app.ability.StartOptions (startAbility的可选参数).md#ZH-CN_TOPIC_0000002529284585__startoptions)和[OpenLinkOptions](@ohos.app.ability.OpenLinkOptions (openLink的可选参数).md#ZH-CN_TOPIC_0000002497604592__openlinkoptions)的可选参数，用于处理拉起应用请求的结果。

-

本模块首批接口从API version 20 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

-

本模块接口仅可在Stage模型下使用。

#### 约束限制

当前支持使用该模块的接口包括：

-

[startAbility](UIAbilityContext.md#ZH-CN_TOPIC_0000002497604628__startability-2)

-

[startAbilityForResult](UIAbilityContext.md#ZH-CN_TOPIC_0000002497604628__startabilityforresult-2)

-

[openLink](UIAbilityContext.md#ZH-CN_TOPIC_0000002497604628__openlink12)

#### 导入模块

```ets
import { CompletionHandler } from '@kit.AbilityKit';
```

#### CompletionHandler

CompletionHandler提供了[onRequestSuccess](#ZH-CN_TOPIC_0000002529284577__onrequestsuccess)和[onRequestFailure](#ZH-CN_TOPIC_0000002529284577__onrequestfailure)两个回调函数，分别用来处理拉起应用成功和失败时的结果。

#### onRequestSuccess

onRequestSuccess(elementName: ElementName, message: string): void

拉起应用成功时的回调函数。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

参数名类型必填说明elementName[ElementName](ElementName.md)是ElementName信息用于标识被拉起应用。通常，ElementName仅包含abilityName和bundleName。moduleName和deviceId信息是否存在取决于调用方是否传入。shortName和uri为空。messagestring是

成功拉起应用时的信息。该信息采用JSON格式，样式如下：

{

 "errMsg": "Succeeded."

}

**示例：**

参见[CompletionHandler使用](#ZH-CN_TOPIC_0000002529284577__completionhandler使用)。

#### onRequestFailure

onRequestFailure(elementName: ElementName, message: string): void

拉起应用失败时的回调函数。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

参数名类型必填说明elementName[ElementName](ElementName.md)是

ElementName信息用于标识被拉起应用。

- 通常，ElementName仅包含abilityName和bundleName。moduleName和deviceId信息是否存在取决于调用方是否传入。shortName和uri为空。

- 隐式启动失败时，无法获取ElementName信息。

messagestring是

拉起应用失败时的信息。该信息采用JSON格式，样式如下：

{

 "errMsg": "xxx"

}

其中，"xxx"的取值说明如下：

Failed to call <api-name>：表示调用接口出错。其中，<api-name>为具体的接口名，比如startAbility。

User refused redirection：表示用户关闭了应用跳转弹框。

User closed the implicit startup picker：表示用户关闭了隐式启动时的应用选择弹框。

User closed the app clone picker：表示用户关闭了分身应用选择弹框。

Free installation failed：表示免安装失败。

**示例：**

参见[CompletionHandler使用](#ZH-CN_TOPIC_0000002529284577__completionhandler使用)。

#### CompletionHandler使用

```ets
import { UIAbility, Want, StartOptions, CompletionHandler, bundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onForeground() {
    let want: Want = {
      deviceId: '',
      bundleName: 'com.example.myapplication',
      abilityName: 'EntryAbility'
    };

    let completionHandler: CompletionHandler = {
      onRequestSuccess: (elementName: bundleManager.ElementName, message: string): void => {
        console.info(`${elementName.bundleName}-${elementName.moduleName}-${elementName.abilityName} start succeeded: ${message}`);
      },
      onRequestFailure: (elementName: bundleManager.ElementName, message: string): void => {
        console.error(`${elementName.bundleName}-${elementName.moduleName}-${elementName.abilityName} start failed: ${message}`);
      }
    };

    let options: StartOptions = {
      completionHandler: completionHandler
    };

    try {
      this.context.startAbility(want, options, (err: BusinessError) => {
        if (err.code) {
          // 处理业务逻辑错误
          console.error(`startAbility failed, code is ${err.code}, message is ${err.message}`);
          return;
        }
        // 执行正常业务
        console.info('startAbility succeed');
      });
    } catch (err) {
      // 处理入参错误异常
      let code = (err as BusinessError).code;
      let message = (err as BusinessError).message;
      console.error(`startAbility failed, code is ${code}, message is ${message}`);
    }
  }
}
```