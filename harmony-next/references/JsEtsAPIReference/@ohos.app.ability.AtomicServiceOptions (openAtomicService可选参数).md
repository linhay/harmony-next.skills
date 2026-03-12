# @ohos.app.ability.AtomicServiceOptions (openAtomicService可选参数)

AtomicServiceOptions可以作为[openAtomicService()](UIAbilityContext.md#ZH-CN_TOPIC_0000002497604628__openatomicservice12)的入参，用于携带参数。继承于[StartOptions](@ohos.app.ability.StartOptions (startAbility的可选参数).md)。

本模块首批接口从API version 12 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

#### 导入模块

```ets
import { AtomicServiceOptions } from '@kit.AbilityKit';
```

#### AtomicServiceOptions

#### 属性

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

名称类型只读可选说明[flags](@ohos.app.ability.wantConstant (Want常量).md#ZH-CN_TOPIC_0000002497604612__flags)number否是

系统处理该次启动的方式。

例如通过wantConstant.Flags.FLAG_INSTALL_ON_DEMAND表示使用免安装能力。

parametersRecord<string, Object>否是表示额外参数描述。具体描述参考[Want](@ohos.app.ability.Want (Want).md)中parameters字段描述。completionHandlerForAtomicService20+[CompletionHandlerForAtomicService](@ohos.app.ability.CompletionHandlerForAtomicService (打开元服务结果的操作类).md)否是

打开元服务结果的操作类，用于接收打开元服务的结果。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**示例：**

```ets
import { UIAbility, AtomicServiceOptions, common, wantConstant, CompletionHandlerForAtomicService, FailureCode } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

export default class EntryAbility extends UIAbility {
  onForeground() {
    let completionHandler: CompletionHandlerForAtomicService = {
      onAtomicServiceRequestSuccess(appId: string) {
        hilog.info(0x0000, 'testTag', `appId:${appId}`);
      },
      onAtomicServiceRequestFailure(appId: string, failureCode: FailureCode, failureMessage: string) {
        hilog.info(0x0000, 'testTag', `appId:${appId}, failureCode:${failureCode}, failureMessage:${failureMessage}`);
      }
    };

    let options: AtomicServiceOptions = {
      flags: wantConstant.Flags.FLAG_INSTALL_ON_DEMAND,
      parameters: {
        'demo.result': 123456
      },
      completionHandlerForAtomicService: completionHandler
    };

    try {
      let appId: string = '6918661953712445909'; // 根据实际appId修改此值
      this.context.openAtomicService(appId, options)
        .then((result: common.AbilityResult) => {
          // 执行正常业务
          console.info('openAtomicService succeed');
        })
        .catch((err: BusinessError) => {
          // 处理业务逻辑错误
          console.error(`openAtomicService failed, code is ${err.code}, message is ${err.message}`);
        });
    } catch (err) {
      // 处理入参错误异常
      let code = (err as BusinessError).code;
      let message = (err as BusinessError).message;
      console.error(`openAtomicService failed, code is ${code}, message is ${message}`);
    }
  }
}
```