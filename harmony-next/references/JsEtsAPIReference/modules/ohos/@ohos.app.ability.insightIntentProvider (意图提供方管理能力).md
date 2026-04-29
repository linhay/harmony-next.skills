# @ohos.app.ability.insightIntentProvider (意图提供方管理能力)

本模块为意图提供方提供管理能力，如主动发送指定意图的执行结果。

  ![image](public_sys-resources/note_3.0-zh-cn.webp)

本模块首批接口从API version 23开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

**导入模块**

```ets
import { insightIntentProvider } from '@kit.AbilityKit';
```

**insightIntentProvider.sendExecuteResult**

sendExecuteResult(instanceId: number, result: insightIntent.ExecuteResult): Promise<void>

如果意图提供方需要在业务处理的特定流程中主动发送意图执行结果，可以先通过[setReturnModeForUIAbilityForeground接口](@ohos.app.ability.InsightIntentContext (意图执行上下文).md#ZH-CN_TOPIC_0000002553360459__insightintentcontextsetreturnmodeforuiabilityforeground23)或[setReturnModeForUIExtensionAbility接口](@ohos.app.ability.InsightIntentContext (意图执行上下文).md#ZH-CN_TOPIC_0000002553360459__insightintentcontextsetreturnmodeforuiextensionability23)将[意图执行结果返回形式](@ohos.app.ability.insightIntent (意图框架基础定义).md#ZH-CN_TOPIC_0000002522080536__returnmode23)设置为FUNCTION，然后调用该接口发送意图执行结果，适用于[配置类意图](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/insight-intent-config-development)。使用Promise异步回调。

[意图执行结果返回形式](@ohos.app.ability.insightIntent (意图框架基础定义).md#ZH-CN_TOPIC_0000002522080536__returnmode23)设置为FUNCTION后，应用将无需再通过[onExecuteInUIAbilityForegroundMode接口](@ohos.app.ability.InsightIntentExecutor (意图执行基类).md#ZH-CN_TOPIC_0000002522080538__onexecuteinuiabilityforegroundmode)或[onExecuteInUIExtensionAbility接口](@ohos.app.ability.InsightIntentExecutor (意图执行基类).md#ZH-CN_TOPIC_0000002522080538__onexecuteinuiextensionability)的返回值返回意图执行结果。

模型约束：此接口仅可在Stage模型下使用。

系统能力：SystemCapability.Ability.AbilityRuntime.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| instanceId | number | 是 | 意图实例唯一ID。 |
| result | insightIntent.ExecuteResult | 是 | 返回意图执行结果，表示本次意图执行返回给系统入口的数据。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

错误码：

以下错误码详细介绍请参考[元能力子系统错误码](元能力子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 16000003 | The specified ID does not exist. |
| 16000050 | Internal error. Possible causes: 1. Connect to system service failed; 2.Send restart message to system service failed; 3.System service failed to communicate with dependency module. |

示例：

设置意图执行结果延迟返回示例：

```ets
import { InsightIntentExecutor, insightIntent } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { hilog } from '@kit.PerformanceAnalysisKit';

export default class InsightIntentExecutorUI extends InsightIntentExecutor {
  onExecuteInUIAbilityForegroundMode(name: string, param: Record<string, Object>,
    pageLoader: window.WindowStage): insightIntent.ExecuteResult {
    hilog.info(0x0000, 'testTag', 'onExecuteInUIAbilityForegroundMode %{public}s', name);
    let result: insightIntent.ExecuteResult;
    result = {
      code: 0,
      result: {
        message: 'Unsupported insight intent.',
      },
    };
    try {
      // 设置意图执行结果的返回形式为延迟返回
      this.context.setReturnModeForUIAbilityForeground(insightIntent.ReturnMode.FUNCTION);
    } catch (error) {
      let code = (error as BusinessError).code;
      let msg = (error as BusinessError).message;
      console.error(`testTag setReturnModeForUIExtensionAbility fail, error code: ${code}, error msg: ${msg}.`);
    }
    // 将意图实例的id通过localStorage传入目标页面中
    let localStorageData: Record<string, number> = {
      'insightId': this.context.instanceId,
    };
    let storage: LocalStorage = new LocalStorage(localStorageData);
    // 通过pageLoader加载页面
    pageLoader.loadContent('pages/UIAbilityIndex', storage, (err, data) => {
      if (err.code) {
        hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err));
      } else {
        hilog.info(0x0000, 'testTag', '%{public}s', 'Succeeded in loading the content');
      }
    });
    return result;
  }
```

主动发送意图执行结果示例：

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { insightIntent, insightIntentProvider } from '@kit.AbilityKit';

@Entry
@Component
struct Index {
  storage: LocalStorage | undefined = this.getUIContext().getSharedLocalStorage();
  insightId: number | undefined = this.storage?.get<number>('insightId');

  build() {
    Column() {
      // 通过sendExecuteResult接口主动返回意图执行结果
      Button('insightIntentProvider sendExecuteResult')
        .onClick(() => {
          try {
            let result: insightIntent.ExecuteResult;
            result = {
              code: 0,
              result: {
                message: 'Unsupported insight intent.',
              },
            };
            insightIntentProvider.sendExecuteResult(this.insightId, result)
              .then(() => {
                console.info('testTag setExecuteResult success');
              })
              .catch((error: BusinessError) => {
                console.error(`testTag setExecuteResult fail1, error code: ${error.code}, error msg: ${error.message}.`);
              });
          } catch (e) {
            let code = (e as BusinessError).code;
            let msg = (e as BusinessError).message;
            console.error(`testTag setExecuteResult fail2, error code: ${code}, error msg: ${msg}`);
          }
        })
    }
    .height('100%')
    .width('100%')
  }
```

**insightIntentProvider.sendIntentResult**

sendIntentResult(instanceId: number, result: insightIntent.IntentResult<T>): Promise<void>

如果意图提供方需要在业务处理的特定流程中主动发送意图执行结果，可以先通过[setReturnModeForUIAbilityForeground接口](@ohos.app.ability.InsightIntentContext (意图执行上下文).md#ZH-CN_TOPIC_0000002553360459__insightintentcontextsetreturnmodeforuiabilityforeground23)或[setReturnModeForUIExtensionAbility接口](@ohos.app.ability.InsightIntentContext (意图执行上下文).md#ZH-CN_TOPIC_0000002553360459__insightintentcontextsetreturnmodeforuiextensionability23)将[意图执行结果返回形式](@ohos.app.ability.insightIntent (意图框架基础定义).md#ZH-CN_TOPIC_0000002522080536__returnmode23)设置为FUNCTION，然后调用该接口发送意图执行结果。适用于[@InsightIntentEntry](@ohos.app.ability.InsightIntentDecorator (意图装饰器定义).md#ZH-CN_TOPIC_0000002522240536__insightintententry)修饰的[装饰器类意图](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/insight-intent-decorator-development)。使用Promise异步回调。

[意图执行结果返回形式](@ohos.app.ability.insightIntent (意图框架基础定义).md#ZH-CN_TOPIC_0000002522080536__returnmode23)设置为FUNCTION后，应用将无需再通过[onExecute接口](@ohos.app.ability.InsightIntentEntryExecutor (@InsightIntentEntry的意图执行基类).md#ZH-CN_TOPIC_0000002553200501__onexecute)的返回值返回意图执行结果。

模型约束：此接口仅可在Stage模型下使用。

系统能力：SystemCapability.Ability.AbilityRuntime.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| instanceId | number | 是 | 意图实例唯一ID。 |
| result | insightIntent.IntentResult | 是 | 返回意图执行结果，表示本次意图执行返回给系统入口的数据。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

错误码：

以下错误码详细介绍请参考[元能力子系统错误码](元能力子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 16000003 | The specified ID does not exist. |
| 16000050 | Internal error. Possible causes: 1. Connect to system service failed; 2.Send restart message to system service failed; 3.System service failed to communicate with dependency module. |

示例：

设置意图执行结果延迟返回示例：

```ets
import { insightIntent, InsightIntentEntry, InsightIntentEntryExecutor } from '@kit.AbilityKit';

class PlayVideoResultDef {
  resultCode: number = 0;
  resultMsg: string = '';
  someInvalid1: string | undefined = undefined;
  someInvalid2: string | null = null;
}

// 播放视频
@InsightIntentEntry({
  intentName: 'PlayVideo',
  domain: 'VideosDomain',
  intentVersion: '1.0.2',
  displayName: '播放视频',
  displayDescription: '播放视频意图',
  schema: 'PlayVideo',
  icon: $r('app.media.background'),
  llmDescription: '播放视频意图',
  keywords: ['视频播放', '播放视频', 'PlayVideo'],
  abilityName: 'EntryAbility1',
  executeMode: [insightIntent.ExecuteMode.UI_ABILITY_FOREGROUND],
})
export default class PlayVideo extends InsightIntentEntryExecutor<PlayVideoResultDef> {
  entityId: string = 'zhz';
  episodeId: string = '50';
  episodeNumber: number = 12;

  onExecute(): Promise<insightIntent.IntentResult<PlayVideoResultDef>> {
    console.info('testTag', 'PlayVideo onExecute success')
    let result: insightIntent.IntentResult<PlayVideoResultDef> = {
      code: 0,
      result: {
        resultCode: 0x0000,
        resultMsg: 'Callback PlayVideo Success',
        someInvalid1: undefined,
        someInvalid2: null
      }
    let instanceId: number = this.context.instanceId;
    try {
      // 设置意图执行结果的返回形式为延迟返回
      this.context.setReturnModeForUIAbilityForeground(insightIntent.ReturnMode.FUNCTION);
      console.info('testTag: setReturnModeForUIAbilityForeground success');
    } catch (error) {
      let code = (error as BusinessError).code;
      let msg = (error as BusinessError).message;
      console.error(`testTag: setReturnModeForUIAbilityForeground failed，error code: ${code}, error msg: ${msg}.`);
    }

    try {
      // 将意图实例的id通过localStorage传入目标页面中
      let localStorageData: Record<string, number> = {
        'insightId': instanceId,
      };
      let storage: LocalStorage = new LocalStorage(localStorageData);
      // 通过pageLoader加载页面
      this.windowStage?.loadContent('pages/Index', storage);
      console.info('testTag', 'Succeeded in loading the content1')
    } catch (err) {
      let code = (err as BusinessError).code;
      let msg = (err as BusinessError).message;
      console.error(`testTag loadContent error code: ${code}, error msg: ${msg}.`);
    }
    return Promise.resolve(result);
  }
```

主动发送意图执行结果示例：

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { insightIntent, insightIntentProvider } from '@kit.AbilityKit';

class PlayVideoResultDef {
  resultCode: number = 0;
  resultMsg: string = '';
  someInvalid1: string | undefined = undefined;
  someInvalid2: string | null = null;
}

@Entry
@Component
struct Index {
  storage: LocalStorage | undefined = this.getUIContext().getSharedLocalStorage();
  insightId: number | undefined = this.storage?.get<number>('insightId');

  build() {
    Column() {
      // 通过sendExecuteResult接口主动返回意图执行结果
      Button('insightIntentProvider sendIntentResult')
        .onClick(() => {
          try {
            let result: insightIntent.IntentResult<PlayVideoResultDef> = {
              code: 0,
              result: {
                resultCode: 123,
                resultMsg: 'Function PlayVideo Success',
                someInvalid1: undefined,
                someInvalid2: null
              }
            insightIntentProvider.sendIntentResult(this.insightId, result)
              .then(() => {
                console.info('testTag sendIntentResult success');
              })
              .catch((error: BusinessError) => {
                console.error(`testTag sendIntentResult error, error code: ${error.code}, error msg: ${error.message}.`);
              });
          } catch (error) {
            let code = (error as BusinessError).code;
            let msg = (error as BusinessError).message;
            console.error(`testTag sendIntentResult fail, error code: ${code}, error msg: ${msg}.`);
          }
        })
    }
    .height('100%')
    .width('100%')
  }
```