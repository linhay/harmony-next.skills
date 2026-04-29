# getContext

如果需要在页面中获得当前Ability的Context，可调用getContext接口获取当前页面关联的[UIAbilityContext](UIAbilityContext.md)或[ExtensionContext](ExtensionContext.md)。

  ![image](public_sys-resources/note_3.0-zh-cn.webp)

- 本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

- 该接口仅限Stage模型使用。

**getContext(deprecated)**

getContext(component?: Object):Context

获取与页面上下文组件关联的Context对象。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

从API version 9开始支持，从API version 18开始废弃，建议使用getHostContext替代。[getHostContext](Class (UIContext).md#ZH-CN_TOPIC_0000002522240732__gethostcontext12)需先获取[UIContext](Class (UIContext).md)实例对象后再进行获取。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

模型约束： 此接口仅可在Stage模型下使用。

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| component | Object | 否 | 当前自定义组件的实例。未传入component或传入的参数类型非法，则返回默认上下文。默认上下文是指通过追溯当前方法的调用链所跟踪到的Context。在异步调用的回调方法中使用该接口，或者该接口的起始调用不在当前页面，将可能导致无法跟踪到该实例的Context，则会返回undefined。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Context | 返回当前组件所在Ability的Context，Context的具体类型为当前Ability关联的Context对象。例如：在UIAbility窗口中的页面调用该接口，返回类型为UIAbilityContext。在ExtensionAbility窗口中的页面调用该接口，返回类型为ExtensionContext。 |

**Context**

type Context = Context

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

模型约束： 此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| Context | 返回当前组件所在Ability的Context，Context的具体类型为当前Ability关联的Context对象。例如：在UIAbility窗口中的页面调用该接口，返回类型为UIAbilityContext。在ExtensionAbility窗口中的页面调用该接口，返回类型为ExtensionContext。 |

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

直接使用getContext可能导致[UI上下文不明确](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-global-interface#ui上下文不明确)的问题，建议使用getUIContext()获取[UIContext](Class (UIContext).md)实例，并使用[getHostContext](Class (UIContext).md#ZH-CN_TOPIC_0000002522240732__gethostcontext12)调用绑定实例的getContext。

示例：

在UIAbility中通过windowStage.loadContent加载具体页面。

```ets
// EntryAbility.ets
import { UIAbility, AbilityConstant, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');
  }

  onDestroy() {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onDestroy');
  }

  onWindowStageCreate(windowStage: window.WindowStage) {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

    windowStage.loadContent('pages/Index', (err, data) => {
      if (err.code) {
        hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
        return;
      }
      hilog.info(0x0000, 'testTag', 'Succeeded in loading the content. Data: %{public}s', JSON.stringify(data) ?? '');
    });
  }

  onWindowStageDestroy() {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageDestroy');
  }

  onForeground() {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onForeground');
  }

  onBackground() {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onBackground');
  }
```

在具体的Index.ets中可以通过getContext接口获取Context上下文，本示例返回的Context类型为UIAbilityContext。

```ets
//pages/Index.ets
@Entry
@Component
struct Index {
  @State message: string = 'Hello World'

  build() {
    Row() {
      Column() {
        Text(this.message)
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
          .onClick(() => {
            // 建议使用this.getUIContext().getHostContext()
            let context: Context = getContext(this) as Context;
            console.info("CacheDir:" + context.cacheDir);
          })
      }
      .width('100%')
    }
    .height('100%')
  }
```