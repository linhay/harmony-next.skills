# @ohos.app.ability.OpenLinkOptions (openLink的可选参数)

OpenLinkOptions可以作为[openLink()](../../topics/graphics/UIAbilityContext.md#ZH-CN_TOPIC_0000002497604628__openlink12)的入参，用于标识是否仅打开AppLinking和传递键值对可选参数。

-

本模块首批接口从API version 12 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

-

本模块接口仅可在Stage模型下使用。

#### 导入模块

```ets
import { OpenLinkOptions } from '@kit.AbilityKit';
```

#### OpenLinkOptions

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

名称类型只读可选说明appLinkingOnlyboolean否是

表示是否必须以[AppLinking](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-linking-startup)的方式启动UIAbility。

- 取值为true时，如果不存在与AppLinking相匹配的UIAbility，直接返回。

- 取值为false时，如果不存在与AppLinking相匹配的UIAbility，AppLinking会退化为[DeepLinking](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/deep-linking-startup)。默认值为false。

aa命令隐式拉起Ability时可以通过设置"--pb appLinkingOnly true/false"以AppLinking的方式进行启动。

parametersRecord<string, Object>否是

表示WantParams参数。

**说明**：具体使用规则请参考[want](@ohos.app.ability.Want (Want).md)中的parameters属性。

hideFailureTipDialog21+boolean否是

表示[Deep Linking](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/deep-linking-startup)找不到应用时是否显示“暂无可用打开方式”的弹窗。

- 取值为true时，不显示“暂无可用打开方式”的弹窗。

- 取值为false时，显示“暂无可用打开方式”的弹窗。默认值为false。

**说明**：appLinkingOnly字段为true时不会触发Deep Linking流程，该字段不会生效。

**元服务API**：从API version 21开始，该接口支持在元服务中使用。

completionHandler21+[CompletionHandler](@ohos.app.ability.CompletionHandler (拉起应用结果的操作类).md#ZH-CN_TOPIC_0000002529284577__completionhandler)否是

拉起应用结果的操作类，用于处理拉起应用的结果。

**元服务API**：从API version 21开始，该接口支持在元服务中使用。

**示例：**

```ets
import { common, OpenLinkOptions, wantConstant, CompletionHandler, bundleManager } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

const DOMAIN = 0xeeee;
const TAG: string = '[openLinkDemo]';

@Entry
@Component
struct Index {
  @State message: string = 'I am caller';

  build() {
    Row() {
      Column() {
        Text(this.message)
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
        Button('start browser', { type: ButtonType.Capsule, stateEffect: true })
          .width('87%')
          .height('5%')
          .margin({ bottom: '12vp' })
          .onClick(() => {
            let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
            let link: string = 'https://www.example.com';
            let completionHandler: CompletionHandler = {
              onRequestSuccess: (elementName: bundleManager.ElementName, message: string): void => {
                console.info(`${elementName.bundleName}-${elementName.moduleName}-${elementName.abilityName} start succeeded: ${message}`);
              },
              onRequestFailure: (elementName: bundleManager.ElementName, message: string): void => {
                console.error(`${elementName.bundleName}-${elementName.moduleName}-${elementName.abilityName} start failed: ${message}`);
              }
            };
            let openLinkOptions: OpenLinkOptions = {
              appLinkingOnly: true,
              // hideFailureTipDialog字段需要在appLinkingOnly字段是false时才生效
              // hideFailureTipDialog: true,
              parameters: {
                [wantConstant.Params.CONTENT_TITLE_KEY]: 'contentTitle',
                keyString: 'str',
                keyNumber: 200,
                keyBool: false,
                keyObj: {
                  keyObjKey: 'objValue',
                }
              },
              completionHandler: completionHandler
            };
            try {
              context.openLink(
                link,
                openLinkOptions,
                (err, result) => {
                  hilog.error(DOMAIN, TAG, `openLink callback error.code: ${JSON.stringify(err)}`);
                  hilog.info(DOMAIN, TAG, `openLink callback result: ${JSON.stringify(result.resultCode)}`);
                  hilog.info(DOMAIN, TAG, `openLink callback result data: ${JSON.stringify(result.want)}`);
                }
              ).then(() => {
                hilog.info(DOMAIN, TAG, `open link success.`);
              }).catch((err: BusinessError) => {
                hilog.error(DOMAIN, TAG, `open link failed, errCode: ${JSON.stringify(err.code)}`);
              });
            } catch (e) {
              hilog.error(DOMAIN, TAG, `open link failed, errCode: ${JSON.stringify(e.code)}`);
            }
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```