# @ohos.app.ability.UIAbility (带界面的应用组件)

UIAbility是包含UI界面的应用组件，继承自[Ability](@ohos.app.ability.Ability (Ability基类).md)，提供UIAbility组件创建、销毁、前后台切换等[生命周期](#ZH-CN_TOPIC_0000002522240540__uiability生命周期状态)回调，同时也具备[后台通信能力](#ZH-CN_TOPIC_0000002522240540__后台通信能力)。


本模块首批接口从API version 9 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

各类Ability的继承关系详见[继承关系说明](@ohos.app.ability.Ability (Ability基类).md#ZH-CN_TOPIC_0000002553360447__ability的继承关系说明)。

#### UIAbility生命周期状态

**图1** UIAbility生命周期状态

![image](public_sys-resources/zh-cn_image_0000002522244666.webp)

- Create：表示UIAbility实例已创建。系统会在该状态下触发其[onCreate](#ZH-CN_TOPIC_0000002522240540__oncreate)回调函数，开发者可以在[onCreate](#ZH-CN_TOPIC_0000002522240540__oncreate)中执行初始化操作。

- Foreground：表示UIAbility被拉到前台。系统会在该状态下触发其[onForeground](#ZH-CN_TOPIC_0000002522240540__onforeground)回调函数，开发者可以在[onForeground](#ZH-CN_TOPIC_0000002522240540__onforeground)中申请应用所需的资源。

- Background：表示UIAbility被拉到后台。系统会在该状态下触发其[onBackground](#ZH-CN_TOPIC_0000002522240540__onbackground)回调函数，开发者可以在[onBackground](#ZH-CN_TOPIC_0000002522240540__onbackground)中释放一些应用资源。

- Destroy：表示UIAbility实例要销毁。系统会在该状态下触发其[onDestroy](#ZH-CN_TOPIC_0000002522240540__ondestroy)回调函数，开发者可以在[onDestroy](#ZH-CN_TOPIC_0000002522240540__ondestroy)中执行数据保存等操作。

#### 后台通信能力

通过Call调用可以与目标UIAbility进行后台通信。Call调用示意图如下所示。

**图2** Call调用示意图

![image](public_sys-resources/zh-cn_image_0000002553202727.webp)

-

Caller UIAbility调用[startAbilityByCall()](UIAbilityContext.md#ZH-CN_TOPIC_0000002553200541__startabilitybycall)接口获取[Caller](#ZH-CN_TOPIC_0000002522240540__caller)对象，并使用Caller对象的[call](#ZH-CN_TOPIC_0000002522240540__call)方法向Callee UIAbility发送数据。

-

Callee UIAbility持有一个[Callee](#ZH-CN_TOPIC_0000002522240540__callee)对象，通过Callee的[on](#ZH-CN_TOPIC_0000002522240540__on)方法注册回调函数，用于接收Caller对象发送的数据。

#### 导入模块

```ets
import { UIAbility } from '@kit.AbilityKit';
```

#### UIAbility

表示包含UI界面的应用组件，提供组件创建、销毁、前后台切换等生命周期回调，同时也具备后台通信能力。

#### 属性

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| context | [UIAbilityContext](../../topics/misc/UIAbilityContext.md) | 否 | 否 | UIAbility的上下文。 元服务API：从API version 11开始，该接口支持在元服务中使用。 |
| launchWant | Want | 否 | 否 | UIAbility冷启动时接收到的Want参数，取值为onCreate接收到的Want参数。 元服务API：从API version 11开始，该接口支持在元服务中使用。 |
| lastRequestWant | Want | 否 | 否 | 最近一次拉起UIAbility请求的Want参数。 - 首次拉起UIAbility时，取值为onCreate接收到的Want参数。 - 重复拉起UIAbility时，取值为onNewWant最近一次接收到的Want参数。 元服务API：从API version 11开始，该接口支持在元服务中使用。 |
| callee | Callee | 否 | 否 | 系统为UIAbility创建的后台通信对象，Callee UIAbility（被调用方）可以通过Callee对象接收Caller对象发送的数据。 |
| specifiedId23+ | string | 否 | 是 | 仅当UIAbility启动模式为specified时存在，取值为开发者自定义的UIAbility标识。 |

#### onCreate

onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void

当UIAbility实例创建完成时，系统会触发该回调，开发者可在该回调中执行初始化逻辑（如定义变量、加载资源等）。该回调仅会在UIAbility[冷启动](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-intra-device-interaction#目标uiability冷启动)时触发。

同步接口，不支持异步回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | Want | 是 | 调用方拉起该UIAbility时传递的数据。 |
| launchParam | AbilityConstant.LaunchParam | 是 | 应用启动参数，包含应用启动原因、应用上次退出原因等。 |

**示例：**

```ets
import { UIAbility, AbilityConstant, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

export default class MyUIAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    // 执行异步任务
    hilog.info(0x0000, 'testTag',
      `onCreate, want: ${want.abilityName}, the launchReason is ${launchParam.launchReason}, the lastExitReason is ${launchParam.lastExitReason}`);
  }
```

#### onWindowStageCreate

onWindowStageCreate(windowStage: window.WindowStage): void

当[WindowStage](Interface (WindowStage).md)实例创建完成后，系统会触发该回调。开发者可以在该回调中通过WindowStage加载页面。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| windowStage | window.WindowStage | 是 | WindowStage实例对象。 |

**示例：**

```ets
import { UIAbility } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { window } from '@kit.ArkUI';

export default class MyUIAbility extends UIAbility {
  // 主窗口已创建，为该UIAbility设置主页面
  onWindowStageCreate(windowStage: window.WindowStage): void {
    windowStage.loadContent('pages/Index', (err, data) => {
      if (err.code) {
        hilog.error(0x0000, 'testTag', `Failed to load the content. Cause: ${JSON.stringify(err)}`);
        return;
      }
      hilog.info(0x0000, 'testTag', `Succeeded in loading the content. Data: ${JSON.stringify(data)}`);
    });
  }
```

#### onWindowStageWillDestroy12+

onWindowStageWillDestroy(windowStage: window.WindowStage): void

当WindowStage即将销毁时，系统触发该回调。开发者可以在该生命周期中取消windowStage事件的监听。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| windowStage | window.WindowStage | 是 | WindowStage实例对象。 |

**示例：**

```ets
import { UIAbility } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { window } from '@kit.ArkUI';

export default class MyUIAbility extends UIAbility {
  onWindowStageWillDestroy(windowStage: window.WindowStage) {
    hilog.info(0x0000, 'testTag', `onWindowStageWillDestroy`);
}
```

#### onWindowStageDestroy

onWindowStageDestroy(): void

当WindowStage销毁后，系统触发该回调。该回调用于通知开发者WindowStage对象已被销毁，不能再继续使用。

仅当UIAbility正常退出时会触发该回调，异常退出场景（例如低内存终止进程）不会触发该回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**示例：**

```ets
import { UIAbility } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

export default class MyUIAbility extends UIAbility {
  onWindowStageDestroy() {
    // 主窗口已销毁，释放UI相关资源
    hilog.info(0x0000, 'testTag', `onWindowStageDestroy`);
  }
```

#### onWindowStageRestore

onWindowStageRestore(windowStage: window.WindowStage): void

当UIAbility跨端迁移时，目标端UIAbility恢复页面栈时回调。


在应用迁移启动时，无论是[冷启动](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-intra-device-interaction#目标uiability冷启动)还是[热启动](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-intra-device-interaction#目标uiability热启动)，都会在执行完[onCreate()](#ZH-CN_TOPIC_0000002522240540__oncreate)/[onNewWant()](#ZH-CN_TOPIC_0000002522240540__onnewwant)后，触发onWindowStageRestore()生命周期函数，不执行onWindowStageCreate()生命周期函数。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| windowStage | window.WindowStage | 是 | WindowStage实例对象。 |

**示例：**

```ets
import { UIAbility } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { window } from '@kit.ArkUI';

export default class MyUIAbility extends UIAbility {
  onWindowStageRestore(windowStage: window.WindowStage) {
    hilog.info(0x0000, 'testTag', `onWindowStageRestore`);
  }
```

#### onDestroy

onDestroy(): void | Promise<void>

当UIAbility被销毁（例如使用[terminateSelf](UIAbilityContext.md#ZH-CN_TOPIC_0000002553200541__terminateself)接口停止UIAbility）时，系统触发该回调。开发者可以在该生命周期中执行资源清理、数据保存等相关操作。

使用同步回调或Promise异步回调。

- 在执行完onDestroy生命周期回调后，应用可能会退出，从而导致其中的异步函数（比如异步写入数据库）未能正确执行。在此情况下，推荐使用Promise异步回调。
- 该回调仅在UIAbility正常退出时触发，当UIAbility异常退出（例如低内存终止进程）时，该回调将不被触发。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**返回值：**

| 类型 | 说明 |
| --- | --- |
| void | Promise<void> | 无返回结果或无返回结果的Promise对象。 |

**示例：**

-

同步回调示例如下：
```ets
import { UIAbility } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

export default class MyUIAbility extends UIAbility {
  onDestroy() {
    hilog.info(0x0000, 'testTag', `onDestroy`);
    // 调用同步函数...
  }
```

-

Promise异步回调示例如下：
```ets
import { UIAbility } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

export default class MyUIAbility extends UIAbility {
  async onDestroy() {
    hilog.info(0x0000, 'testTag', `onDestroy`);
    // 调用异步函数...
  }
```

#### onWillForeground20+

onWillForeground(): void

UIAbility生命周期回调，应用转到前台前触发，在[onForeground](#ZH-CN_TOPIC_0000002522240540__onforeground)前被调用。可在该回调中实现采集应用开始进入前台的时间。如果与[onDidForeground](#ZH-CN_TOPIC_0000002522240540__ondidforeground20)配合使用，还可以统计出从应用开始进入前台到切换至前台状态的耗时。

同步接口，不支持异步回调。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**示例：**

```ets
import { UIAbility } from '@kit.AbilityKit';
import { hiAppEvent, hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  // ...

  onWillForeground(): void {
    // 应用开始进入前台事件打点
    let eventParams: Record<string, number> = { 'xxxx': 100 };
    let eventInfo: hiAppEvent.AppEventInfo = {
      // 事件领域定义
      domain: "lifecycle",
      // 事件名称定义
      name: "onwillforeground",
      // 事件类型定义
      eventType: hiAppEvent.EventType.BEHAVIOR,
      // 事件参数定义
      params: eventParams,
    };
    hiAppEvent.write(eventInfo).then(() => {
      hilog.info(0x0000, 'testTag', `HiAppEvent success to write event`);
    }).catch((err: BusinessError) => {
      hilog.error(0x0000, 'testTag', `HiAppEvent err.code: ${err.code}, err.message: ${err.message}`);
    });
  }

  // ...

  onDidForeground(): void {
    // 应用进入前台后事件打点
    let eventParams: Record<string, number> = { 'xxxx': 100 };
    let eventInfo: hiAppEvent.AppEventInfo = {
      // 事件领域定义
      domain: "lifecycle",
      // 事件名称定义
      name: "ondidforeground",
      // 事件类型定义
      eventType: hiAppEvent.EventType.BEHAVIOR,
      // 事件参数定义
      params: eventParams,
    };
    hiAppEvent.write(eventInfo).then(() => {
      hilog.info(0x0000, 'testTag', `HiAppEvent success to write event`);
    }).catch((err: BusinessError) => {
      hilog.error(0x0000, 'testTag', `HiAppEvent err.code: ${err.code}, err.message: ${err.message}`);
    });
  }
```

#### onForeground

onForeground(): void

当应用首次启动到前台或者从后台转入到前台时，系统触发该回调。开发者可在该回调中实现系统所需资源的申请，如应用转到前台时申请定位服务等。

同步接口，不支持异步回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**示例：**

```ets
import { UIAbility } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

export default class MyUIAbility extends UIAbility {
  onForeground() {
    hilog.info(0x0000, 'testTag', `onForeground`);
  }
```

#### onDidForeground20+

onDidForeground(): void

UIAbility生命周期回调，应用转到前台后触发，在[onForeground](#ZH-CN_TOPIC_0000002522240540__onforeground)后被调用，可在该回调中实现应用切换到前台后的时间打点。如果与[onWillForeground](#ZH-CN_TOPIC_0000002522240540__onwillforeground20)配合使用，还可以统计出从应用开始进入前台到切换至前台状态的耗时。

同步接口，不支持异步回调。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**示例：**

参考[onWillForeground](#ZH-CN_TOPIC_0000002522240540__onwillforeground20)。

#### onWillBackground20+

onWillBackground(): void

UIAbility生命周期回调，当应用从前台转到后台前触发，在[onBackground](#ZH-CN_TOPIC_0000002522240540__onbackground)前被调用。可在该回调中实现数据打点，例如，打点应用运行过程中发生的故障信息、统计信息、安全信息、用户行为信息等。

同步接口，不支持异步回调。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**示例：**

```ets
import { UIAbility } from '@kit.AbilityKit';
import { hiAppEvent, hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class MyUIAbility extends UIAbility {
  onWillBackground(): void {
    let eventParams: Record<string, number | string> = {
      "int_data": 100,
      "str_data": "strValue",
    };
    // 打点应用故障信息
    hiAppEvent.write({
      domain: "test_domain",
      name: "test_event",
      eventType: hiAppEvent.EventType.FAULT,
      params: eventParams,
    }, (err: BusinessError) => {
      if (err) {
        hilog.error(0x0000, 'testTag', `hiAppEvent code: ${err.code}, message: ${err.message}`);
        return;
      }
      hilog.info(0x0000, 'testTag', `hiAppEvent success to write event`);
    });
  }
```

#### onBackground

onBackground(): void

当应用从前台转入到后台时，系统触发该回调。开发者可在该回调中实现UI不可见时的资源释放操作，如停止定位功能等。

同步接口，不支持异步回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**示例：**

```ets
import { UIAbility } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

export default class MyUIAbility extends UIAbility {
  onBackground() {
    // UIAbility回到后台
    hilog.info(0x0000, 'testTag', `onBackground`);
  }
```

#### onDidBackground20+

onDidBackground(): void

UIAbility生命周期回调，当应用从前台转到后台后触发，在[onBackground](#ZH-CN_TOPIC_0000002522240540__onbackground)之后被调用。可在该回调中实现应用进入后台之后的资源释放操作，如进入后台后停止音频播放等。

同步接口，不支持异步回调。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**示例：**

```ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { audio } from '@kit.AudioKit';

export default class MyUIAbility extends UIAbility {
  static audioRenderer: audio.AudioRenderer;

  // ...
  onForeground(): void {
    let audioStreamInfo: audio.AudioStreamInfo = {
      samplingRate: audio.AudioSamplingRate.SAMPLE_RATE_48000, // 采样率。
      channels: audio.AudioChannel.CHANNEL_2, // 通道。
      sampleFormat: audio.AudioSampleFormat.SAMPLE_FORMAT_S16LE, // 采样格式。
      encodingType: audio.AudioEncodingType.ENCODING_TYPE_RAW // 编码格式。
    };

    let audioRendererInfo: audio.AudioRendererInfo = {
      usage: audio.StreamUsage.STREAM_USAGE_MUSIC, // 音频流使用类型：音乐。根据业务场景配置，参考StreamUsage。
      rendererFlags: 0 // 音频渲染器标志。
    };

    let audioRendererOptions: audio.AudioRendererOptions = {
      streamInfo: audioStreamInfo,
      rendererInfo: audioRendererInfo
    };

    // 在前台时申请audioRenderer，用于播放PCM（Pulse Code Modulation）音频数据
    audio.createAudioRenderer(audioRendererOptions).then((data) => {
      MyUIAbility.audioRenderer = data;
      hilog.info(0x0000, 'testTag', `AudioRenderer Created : Success : Stream Type: SUCCESS.`);
    }).catch((err: BusinessError) => {
      hilog.error(0x0000, 'testTag', `AudioRenderer Created : F : ${JSON.stringify(err)}.`);
    });
  }

  onDidBackground() {
    // 转到后台后，释放audioRenderer资源
    MyUIAbility.audioRenderer.release((err: BusinessError) => {
      if (err) {
        hilog.error(0x0000, 'testTag', `AudioRenderer release failed, error: ${JSON.stringify(err)}.`);
      } else {
        hilog.info(0x0000, 'testTag', `AudioRenderer released.`);
      }
    });
  }
```

#### onContinue

onContinue(wantParam: Record<string, Object>): AbilityConstant.OnContinueResult | Promise<AbilityConstant.OnContinueResult>

当UIAbility准备跨端迁移时触发，可以保存待迁移的业务数据。

对于API version 18（不含18） 之前版本仅支持同步调用，从API version 18及后续版本可支持异步调用。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| wantParam | Record<string, Object> | 是 | 开发者通过该参数保存待迁移的数据。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| AbilityConstant.OnContinueResult | Promise<AbilityConstant.OnContinueResult> | 表示是否同意迁移的结果： - AGREE：表示同意。 - REJECT：表示拒绝，如应用在onContinue中异常可以返回REJECT。 - MISMATCH：表示版本不匹配，接续源端应用可以在onContinue中获取到迁移对端应用的版本号，进行协商后，如果版本不匹配导致无法迁移，可以返回该结果。 该回调与onWindowStageRestore成对出现。在接续场景下，源端的UIAbility触发onContinue保存自定义数据，在目标端UIAbility触发onWindowStageRestore恢复自定义数据。 |

**示例：**

-

应用迁移时使用同步接口进行数据保存，示例如下：
```ets
import { UIAbility, AbilityConstant } from '@kit.AbilityKit';

export default class MyUIAbility extends UIAbility {
  onContinue(wantParams: Record<string, Object>) {
    console.info('onContinue');
    wantParams['myData'] = 'my1234567';
    return AbilityConstant.OnContinueResult.AGREE;
}
```

-

应用迁移时使用异步接口进行数据保存，示例如下：
```ets
import { UIAbility, AbilityConstant } from '@kit.AbilityKit';

export default class MyUIAbility extends UIAbility {
  async setWant(wantParams: Record<string, Object>) {
    console.info('setWant start');
    for (let time = 0; time < 1000; ++time) {
      wantParams[time] = time;
    }
    console.info('setWant end');
  }

  async onContinue(wantParams: Record<string, Object>) {
    console.info('onContinue');
    return this.setWant(wantParams).then(() => {
      return AbilityConstant.OnContinueResult.AGREE;
    });
  }
```

#### onNewWant

onNewWant(want: Want, launchParam: AbilityConstant.LaunchParam): void

当已经启动的UIAbility实例再次被拉起时，系统会触发该回调。若在特定场景下（参见[Scenarios](@ohos.app.ability.contextConstant (Context相关常量).md#ZH-CN_TOPIC_0000002553200497__scenarios20)），不需要触发该生命周期回调，可以使用[setOnNewWantSkipScenarios](UIAbilityContext.md#ZH-CN_TOPIC_0000002553200541__setonnewwantskipscenarios20)接口设置。

同步接口，不支持异步回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | Want | 是 | 调用方再次拉起该UIAbility时传递的数据。 |
| launchParam | AbilityConstant.LaunchParam | 是 | UIAbility启动参数，包含启动原因等。 |

**示例：**

```ets
import { UIAbility, AbilityConstant, Want } from '@kit.AbilityKit';

export default class MyUIAbility extends UIAbility {
  onNewWant(want: Want, launchParam: AbilityConstant.LaunchParam) {
    console.info(`onNewWant, want: ${want.abilityName}`);
    console.info(`onNewWant, launchParam: ${JSON.stringify(launchParam)}`);
  }
```

#### onDump

onDump(params: Array<string>): Array<string>

应用调测场景下，通过命令行dump UIAbility数据时，系统会触发该回调。开发者可以在该回调中返回UIAbility要转储的非敏感信息。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| params | Array<string> | 是 | 表示dump命令参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<string> | 返回的dump信息。 |

**示例：**

```ets
import { UIAbility } from '@kit.AbilityKit';

export default class MyUIAbility extends UIAbility {
  onDump(params: Array<string>) {
    console.info(`dump, params: ${JSON.stringify(params)}`);
    return ['params'];
  }
```

#### onSaveState

onSaveState(reason: AbilityConstant.StateType, wantParam: Record<string, Object>): AbilityConstant.OnSaveResult

该接口需要与[appRecovery](@ohos.app.ability.appRecovery (应用故障恢复).md)配合使用。如果应用已使能故障恢复功能（即[enableAppRecovery](@ohos.app.ability.appRecovery (应用故障恢复).md#ZH-CN_TOPIC_0000002553360479__apprecoveryenableapprecovery)接口中的saveOccasion参数设置为SAVE_WHEN_ERROR），当应用出现故障时，系统将触发该回调来保存UIAbility的数据。


从API version 20开始，当[onSaveStateAsync](#ZH-CN_TOPIC_0000002522240540__onsavestateasync20)实现时，本回调函数将不执行。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| reason | AbilityConstant.StateType | 是 | 触发应用保存状态的原因，当前仅支持APP_RECOVERY（即应用故障恢复场景）。 |
| wantParam | Record<string, Object> | 是 | 用户自定义的应用状态数据，应用再启动时被保存在onCreate的Want.parameters中。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| AbilityConstant.OnSaveResult | 返回一个数据保存策略的对象（如全部拒绝、全部允许、只允许故障恢复场景等）。 |

**示例：**

```ets
import { UIAbility, AbilityConstant } from '@kit.AbilityKit';

export default class MyUIAbility extends UIAbility {
  onSaveState(reason: AbilityConstant.StateType, wantParam: Record<string, Object>) {
    console.info('onSaveState');
    wantParam['myData'] = 'my1234567';
    return AbilityConstant.OnSaveResult.RECOVERY_AGREE;
  }
```

#### onSaveStateAsync20+

onSaveStateAsync(stateType: AbilityConstant.StateType, wantParam: Record<string, Object>): Promise<AbilityConstant.OnSaveResult>

该接口需要与[appRecovery](@ohos.app.ability.appRecovery (应用故障恢复).md)配合使用。如果应用已使能故障恢复功能（即[enableAppRecovery](@ohos.app.ability.appRecovery (应用故障恢复).md#ZH-CN_TOPIC_0000002553360479__apprecoveryenableapprecovery)接口中的saveOccasion参数设置为SAVE_WHEN_ERROR），当应用出现故障时，将触发该回调来保存UIAbility的数据。使用Promise异步回调。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| stateType | AbilityConstant.StateType | 是 | 触发应用保存状态的原因，当前仅支持APP_RECOVERY（即应用故障恢复场景）。 |
| wantParam | Record<string, Object> | 是 | 用户自定义的应用状态数据，应用再启动时被保存在onCreate的Want.parameters中。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<AbilityConstant.OnSaveResult> | Promise对象。返回一个数据保存策略的对象（如全部拒绝、全部允许、只允许故障恢复场景等）。 |

**示例：**

```ets
import { UIAbility, AbilityConstant } from '@kit.AbilityKit';

class MyUIAbility extends UIAbility {
  async onSaveStateAsync(reason: AbilityConstant.StateType,
    wantParam: Record<string, Object>): Promise<AbilityConstant.OnSaveResult> {
    await new Promise<string>((res, rej) => {
      setTimeout(res, 1000); // 延时1秒后执行
    });
    return AbilityConstant.OnSaveResult.RECOVERY_AGREE;
  }
```

#### onShare10+

onShare(wantParam: Record<string, Object>): void

当跨端分享元服务时，系统触发该回调。开发者可以在该回调中设置待分享元服务的标题、摘要和URL等数据。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| wantParam | Record<string, Object> | 是 | 待分享的数据。 |

**示例：**

```ets
import { UIAbility } from '@kit.AbilityKit';

export default class MyUIAbility extends UIAbility {
  onShare(wantParams: Record<string, Object>) {
    console.info('onShare');
    wantParams['ohos.extra.param.key.shareUrl'] = 'example.com';
  }
```

#### onPrepareToTerminate10+

onPrepareToTerminate(): boolean

在UIAbility即将关闭前（例如用户通过点击应用窗口右上角的关闭按钮、或者通过Dock栏/托盘右键退出应用时），系统会触发该回调，用于在UIAbility正式关闭前执行其他操作。开发者可以在该回调中返回true阻拦此次关闭，然后在合适时机主动调用[terminateSelf](UIAbilityContext.md#ZH-CN_TOPIC_0000002553200541__terminateself)接口关闭。例如，询问用户是否确认关闭UIAbility，再主动销毁UIAbility。


- 从API version 15开始，当[UIAbility.onPrepareToTerminateAsync](#ZH-CN_TOPIC_0000002522240540__onpreparetoterminateasync15)实现时，本回调函数将不执行。当[AbilityStage.onPrepareTerminationAsync](@ohos.app.ability.AbilityStage (AbilityStage组件管理器).md#ZH-CN_TOPIC_0000002522080526__onprepareterminationasync15)或[AbilityStage.onPrepareTermination](@ohos.app.ability.AbilityStage (AbilityStage组件管理器).md#ZH-CN_TOPIC_0000002522080526__onpreparetermination15)实现时，在dock栏或系统托盘处右键点击关闭，本回调函数将不执行。

- 如果应用本身或者所使用的三方框架注册了[window.WindowStage.on('windowStageClose')](Interface (WindowStage).md#ZH-CN_TOPIC_0000002553360677__onwindowstageclose14)监听，本回调函数将不执行。

**需要权限**：ohos.permission.PREPARE_APP_TERMINATE

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**设备行为差异**：该接口仅在2in1和Tablet设备中可正常执行回调，在其他设备上不执行回调。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 是否执行UIAbility关闭操作，返回true表示本次UIAbility关闭流程取消，返回false表示UIAbility继续正常关闭。 |

**示例：**

```ets
import { UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onPrepareToTerminate() {
    // 开发者定义预关闭动作
    // 例如拉起另一个ability，根据ability处理结果执行异步关闭
    let want: Want = {
      bundleName: "com.example.myapplication",
      moduleName: "entry",
      abilityName: "SecondAbility"
    }
    this.context.startAbilityForResult(want)
      .then((result) => {
        // 获取ability处理结果，当返回结果的resultCode为0关闭当前UIAbility
        console.info('startAbilityForResult success, resultCode is ' + result.resultCode);
        if (result.resultCode === 0) {
          this.context.terminateSelf();
        }
      }).catch((err: BusinessError) => {
      // 异常处理
      console.error('startAbilityForResult failed, err:' + JSON.stringify(err));
      this.context.terminateSelf();
    })

    return true; // 已定义预关闭操作后，返回true表示UIAbility取消关闭
  }
```

#### onPrepareToTerminateAsync15+

onPrepareToTerminateAsync(): Promise<boolean>

在UIAbility关闭前（例如用户通过点击应用窗口右上角的关闭按钮、或者通过Dock栏/托盘右键退出应用时），系统会触发该回调，用于在UIAbility正式关闭前执行其他操作。

开发者可以在该回调中返回true阻拦此次关闭，然后在合适时机主动调用[terminateSelf](UIAbilityContext.md#ZH-CN_TOPIC_0000002553200541__terminateself)接口关闭。例如，询问用户是否确认关闭UIAbility，再主动销毁UIAbility。


-

当[AbilityStage.onPrepareTerminationAsync](@ohos.app.ability.AbilityStage (AbilityStage组件管理器).md#ZH-CN_TOPIC_0000002522080526__onprepareterminationasync15)或[AbilityStage.onPrepareTermination](@ohos.app.ability.AbilityStage (AbilityStage组件管理器).md#ZH-CN_TOPIC_0000002522080526__onpreparetermination15)实现时，在dock栏或系统托盘处右键点击关闭，本回调函数将不执行。

-

如果应用本身或者所使用的三方框架注册了[window.WindowStage.on('windowStageClose')](Interface (WindowStage).md#ZH-CN_TOPIC_0000002553360677__onwindowstageclose14)监听，本回调函数将不执行。

-

若异步回调内发生crash，按超时处理，执行等待超过10秒未响应，UIAbility将被强制关闭。

**需要权限**：ohos.permission.PREPARE_APP_TERMINATE

**元服务API**：从API version 15开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**设备行为差异**：

- 从API version 15开始，该接口仅在2in1设备中可正常执行回调，在其他设备上不执行回调。
- 从API version 19开始，该接口在2in1和Tablet设备中可正常执行回调，在其他设备上不执行回调。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。表示是否执行UIAbility关闭操作，返回true表示本次UIAbility关闭流程取消，返回false表示UIAbility继续正常关闭。 |

**示例：**

```ets
import { UIAbility } from '@kit.AbilityKit';

export default class EntryAbility extends UIAbility {
  async onPrepareToTerminateAsync(): Promise<boolean> {
    await new Promise<boolean>((res, rej) => {
      setTimeout(res, 2000); // 延时2秒
    });
    return true; // 已定义预关闭操作后，返回true表示UIAbility取消关闭
  }
```

#### onBackPressed10+

onBackPressed(): boolean

UIAbility生命周期回调，当UIAbility侧滑返回时触发，根据返回值决定是否销毁UIAbility。

- 当targetSdkVersion<12时，默认返回值为false，会销毁UIAbility。
- 当targetSdkVersion>=12时，默认返回值为true，会将UIAbility移动到后台不销毁。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回true表示UIAbility将会被移到后台不销毁，返回false表示UIAbility将正常销毁。 |

**示例：**

```ets
import { UIAbility } from '@kit.AbilityKit';

export default class EntryAbility extends UIAbility {
  onBackPressed() {
    return true;
  }
```

#### onCollaborate18+

onCollaborate(wantParam: Record<string, Object>): AbilityConstant.CollaborateResult

UIAbility生命周期回调，在多设备协同场景下，协同方应用在被拉起的过程中返回是否接受协同。

- 该生命周期回调不支持[specified启动模式](../../guides/UIAbility组件启动模式.md#specified启动模式)。

- 通过[startAbility](UIAbilityContext.md#ZH-CN_TOPIC_0000002553200541__startability)等方法拉起协同方应用时，需要在Want对象中设置协同标记[Flags](@ohos.app.ability.wantConstant (Want常量).md#ZH-CN_TOPIC_0000002553200525__flags)为FLAG_ABILITY_ON_COLLABORATE。

- [冷启动](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-intra-device-interaction#目标uiability冷启动)时，该回调在[onForeground](#ZH-CN_TOPIC_0000002522240540__onforeground)前或[onBackground](#ZH-CN_TOPIC_0000002522240540__onbackground)后调用；[热启动](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-intra-device-interaction#目标uiability热启动)时，该回调在[onNewWant](#ZH-CN_TOPIC_0000002522240540__onnewwant)前调用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| wantParam | Record<string, Object> | 是 | want相关参数，仅支持key值取"ohos.extra.param.key.supportCollaborateIndex"。通过该key值可以获取到调用方传输的数据并进行相应的处理。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| AbilityConstant.CollaborateResult | 协同方是否接受协同的结果。 |

**示例：**

```ets
import { UIAbility, AbilityConstant } from '@kit.AbilityKit';

export default class MyAbility extends UIAbility {
  onCollaborate(wantParam: Record<string, Object>) {
    return AbilityConstant.CollaborateResult.ACCEPT;
  }
```

#### Caller

调用方Caller UIAbility通过[startAbilityByCall](UIAbilityContext.md#ZH-CN_TOPIC_0000002553200541__startabilitybycall)接口拉起目标Callee UIAbility，目标UIAbility启动成功后，返回一个Caller对象给调用方进行通信。

#### call

call(method: string, data: rpc.Parcelable): Promise<void>

Caller UIAbility向Callee UIAbility发送双方约定好的序列化的数据。使用Promise异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| method | string | 是 | 由Caller和Callee双方约定好的方法名，Callee方通过该字段区分消息类型。 |
| data | rpc.Parcelable | 是 | 由Caller向Callee发送的消息内容，消息内容是序列化的数据。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码]([通用错误码](../../errors/通用错误码.md).md)和[元能力子系统错误码]([元能力子系统错误码](../../errors/元能力子系统错误码.md).md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 16200001 | The caller has been released. |
| 16200002 | The callee does not exist. |
| 16000050 | Internal error. |

**示例：**

```ets
import { UIAbility, Caller } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { rpc } from '@kit.IPCKit';
import { BusinessError } from '@kit.BasicServicesKit';

class MyMessageAble implements rpc.Parcelable { // 自定义的Parcelable数据结构
  name: string;
  str: string;
  num: number = 1;

  constructor(name: string, str: string) {
    this.name = name;
    this.str = str;
  }

  marshalling(messageSequence: rpc.MessageSequence) {
    messageSequence.writeInt(this.num);
    messageSequence.writeString(this.str);
    console.info(`MyMessageAble marshalling num[${this.num}] str[${this.str}]`);
    return true;
  }

  unmarshalling(messageSequence: rpc.MessageSequence) {
    this.num = messageSequence.readInt();
    this.str = messageSequence.readString();
    console.info(`MyMessageAble unmarshalling num[${this.num}] str[${this.str}]`);
    return true;
  }

let method = 'call_Function'; // 约定的通知消息字符串

export default class MainUIAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    this.context.startAbilityByCall({
      bundleName: 'com.example.myservice',
      abilityName: 'MainUIAbility',
      deviceId: ''
    }).then((obj) => {
      let caller: Caller = obj;
      let msg = new MyMessageAble('msg', 'world'); // 参考Parcelable数据定义
      caller.call(method, msg)
        .then(() => {
          console.info('Caller call() called');
        })
        .catch((callErr: BusinessError) => {
          console.error(`Caller.call catch error, error.code: ${callErr.code}, error.message: ${callErr.message}`);
        });
    }).catch((err: BusinessError) => {
      console.error(`Caller GetCaller error, error.code: ${err.code}, error.message: ${err.message}`);
    });
  }
```

#### callWithResult

callWithResult(method: string, data: rpc.Parcelable): Promise<rpc.MessageSequence>

Caller UIAbility向Callee UIAbility发送消息，Callee UIAbility处理完成后返回结果。使用Promise异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| method | string | 是 | 由Caller和Callee双方约定好的方法名，Callee方通过该字段区分消息类型。 |
| data | rpc.Parcelable | 是 | 由Caller向Callee发送的消息内容，消息内容是序列化的数据。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<rpc.MessageSequence> | Promise对象，返回Callee UIAbility的应答数据。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](通用错误码.md)和[元能力子系统错误码](元能力子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 16200001 | The caller has been released. |
| 16200002 | The callee does not exist. |
| 16000050 | Internal error. |

**示例：**

```ets
import { UIAbility, Caller } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { rpc } from '@kit.IPCKit';
import { BusinessError } from '@kit.BasicServicesKit';

class MyMessageAble implements rpc.Parcelable {
  name: string
  str: string
  num: number = 1

  constructor(name: string, str: string) {
    this.name = name;
    this.str = str;
  }

  marshalling(messageSequence: rpc.MessageSequence) {
    messageSequence.writeInt(this.num);
    messageSequence.writeString(this.str);
    console.info(`MyMessageAble marshalling num[${this.num}] str[${this.str}]`);
    return true;
  }

  unmarshalling(messageSequence: rpc.MessageSequence) {
    this.num = messageSequence.readInt();
    this.str = messageSequence.readString();
    console.info(`MyMessageAble unmarshalling num[${this.num}] str[${this.str}]`);
    return true;
  }

let method = 'call_Function';
let caller: Caller;

export default class MainUIAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    this.context.startAbilityByCall({
      bundleName: 'com.example.myservice',
      abilityName: 'MainUIAbility',
      deviceId: ''
    }).then((obj) => {
      caller = obj;
      let msg = new MyMessageAble('msg', 'world');
      caller.callWithResult(method, msg)
        .then((data) => {
          console.info('Caller callWithResult() called');
          let retMsg = new MyMessageAble('msg', 'world');
          data.readParcelable(retMsg);
        })
        .catch((callErr: BusinessError) => {
          console.error(`Caller.callWithResult catch error, error.code: ${callErr.code}, error.message: ${callErr.message}`);
        });
    }).catch((err: BusinessError) => {
      console.error(`Caller GetCaller error, error.code: ${err.code}, error.message: ${err.message}`);
    });
  }
```

#### release

release(): void

Caller主动释放与Callee UIAbility的连接。调用该接口后，Caller不能再使用call或callWithResult向Callee方发送消息。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**错误码：**

以下错误码详细介绍请参考[元能力子系统错误码](元能力子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 16200001 | The caller has been released. |
| 16200002 | The callee does not exist. |

**示例：**

```ets
import { UIAbility, Caller } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

let caller: Caller;

export default class MainUIAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    this.context.startAbilityByCall({
      bundleName: 'com.example.myservice',
      abilityName: 'MainUIAbility',
      deviceId: ''
    }).then((obj) => {
      caller = obj;
      try {
        caller.release();
      } catch (releaseErr) {
        console.error(`Caller.release catch error, error.code: ${releaseErr.code}, error.message: ${releaseErr.message}`);
      }
    }).catch((err: BusinessError) => {
      console.error(`Caller GetCaller error, error.code: ${err.code}, error.message: ${err.message}`);
    });
  }
```

#### onRelease

onRelease(callback: OnReleaseCallback): void

Caller UIAbility可使用该接口注册与Callee UIAbility连接断开通知的监听。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | OnReleaseCallback | 是 | 回调函数，返回onRelease回调结果。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](通用错误码.md)和[元能力子系统错误码](元能力子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 16200001 | The caller has been released. |

**示例：**

```ets
import { UIAbility, Caller } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

export default class MainUIAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    this.context.startAbilityByCall({
      bundleName: 'com.example.myservice',
      abilityName: 'MainUIAbility',
      deviceId: ''
    }).then((obj) => {
      let caller: Caller = obj;
      try {
        caller.onRelease((str) => {
          console.info(`Caller OnRelease CallBack is called ${str}`);
        });
      } catch (error) {
        console.error(`Caller.onRelease catch error, error.code: ${error.code}, error.message: ${error.message}`);
      }
    }).catch((err: BusinessError) => {
      console.error(`Caller GetCaller error, error.code: ${err.code}, error.message: ${err.message}`);
    });
  }
```

#### onRemoteStateChange10+

onRemoteStateChange(callback: OnRemoteStateChangeCallback): void

注册协同场景下跨设备组件状态变化监听通知。使用callback异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | OnRemoteStateChangeCallback | 是 | 回调函数，返回onRemoteStateChange回调结果。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](通用错误码.md)和[元能力子系统错误码](元能力子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 16200001 | The caller has been released. |

**示例：**

```ets
import { UIAbility, Caller } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

export default class MainAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    let dstDeviceId: string = 'xxxxx';
    this.context.startAbilityByCall({
      bundleName: 'com.example.myservice',
      abilityName: 'MainUIAbility',
      deviceId: dstDeviceId
    }).then((obj) => {
      let caller: Caller = obj;
      try {
        caller.onRemoteStateChange((str) => {
          console.info('Remote state changed ' + str);
        });
      } catch (error) {
        console.error(`Caller.onRemoteStateChange catch error, error.code: ${JSON.stringify(error.code)}, error.message: ${JSON.stringify(error.message)}`);
      }
    }).catch((err: BusinessError) => {
      console.error(`Caller GetCaller error, error.code: ${JSON.stringify(err.code)}, error.message: ${JSON.stringify(err.message)}`);
    });
  }
```

#### on('release')

on(type: 'release', callback: OnReleaseCallback): void

Caller UIAbility可使用该接口注册与Callee UIAbility连接断开通知的监听。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听releaseCall事件，固定为'release'。 |
| callback | OnReleaseCallback | 是 | 回调函数，返回on回调结果。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](通用错误码.md)和[元能力子系统错误码](元能力子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 16200001 | The caller has been released. |

**示例：**

```ets
import { UIAbility, Caller } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

export default class MainUIAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    let dstDeviceId: string = 'xxxx';
    this.context.startAbilityByCall({
      bundleName: 'com.example.myservice',
      abilityName: 'MainUIAbility',
      deviceId: dstDeviceId
    }).then((obj) => {
      let caller: Caller = obj;
      try {
        caller.on('release', (str) => {
          console.info(`Caller OnRelease CallBack is called ${str}`);
        });
      } catch (error) {
        console.error(`Caller.on catch error, error.code: ${error.code}, error.message: ${error.message}`);
      }
    }).catch((err: BusinessError) => {
      console.error(`Caller GetCaller error, error.code: ${err.code}, error.message: ${err.message}`);
    });
  }
```

#### off('release')

off(type: 'release', callback: OnReleaseCallback): void

取消注册Callee UIAbility断开通知的监听，与[on('release')](#ZH-CN_TOPIC_0000002522240540__onrelease-1)是反向操作，当前暂未支持。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听releaseCall事件，固定为'release'。 |
| callback | OnReleaseCallback | 是 | 回调函数，返回off回调结果。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ets
import { UIAbility, Caller, OnReleaseCallback } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

export default class MainUIAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    this.context.startAbilityByCall({
      bundleName: 'com.example.myservice',
      abilityName: 'MainUIAbility',
      deviceId: ''
    }).then((obj) => {
      let caller: Caller = obj;
      try {
        let onReleaseCallBack: OnReleaseCallback = (str) => {
          console.info(`Caller OnRelease CallBack is called ${str}`);
        };
        caller.on('release', onReleaseCallBack);
        caller.off('release', onReleaseCallBack);
      } catch (error) {
        console.error(`Caller.on or Caller.off catch error, error.code: ${error.code}, error.message: ${error.message}`);
      }
    }).catch((err: BusinessError) => {
      console.error(`Caller GetCaller error, error.code: ${err.code}, error.message: ${err.message}`);
    });
  }
```

#### off('release')

off(type: 'release'): void

取消注册Callee UIAbility断开通知的监听，与[Caller.on('release')](#ZH-CN_TOPIC_0000002522240540__onrelease-1)是反向操作，当前暂未支持。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听releaseCall事件，固定为'release'。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ets
import { UIAbility, Caller, OnReleaseCallback } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

let caller: Caller;

export default class MainUIAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    this.context.startAbilityByCall({
      bundleName: 'com.example.myservice',
      abilityName: 'MainUIAbility',
      deviceId: ''
    }).then((obj) => {
      caller = obj;
      try {
        let onReleaseCallBack: OnReleaseCallback = (str) => {
          console.info(`Caller OnRelease CallBack is called ${str}`);
        };
        caller.on('release', onReleaseCallBack);
        caller.off('release');
      } catch (error) {
        console.error(`Caller.on or Caller.off catch error, error.code: ${error.code}, error.message: ${error.message}`);
      }
    }).catch((err: BusinessError) => {
      console.error(`Caller GetCaller error, error.code: ${err.code}, error.message: ${err.message}`);
    });
  }
```

#### Callee

系统为UIAbility创建的后台通信对象，Callee UIAbility（被调用方）可以通过Callee对象接收Caller对象发送的数据。

#### on

on(method: string, callback: CalleeCallback): void

通用组件服务端注册消息通知callback。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| method | string | 是 | 由Caller和Callee双方约定好的方法名，Callee方通过该字段区分消息类型。 |
| callback | CalleeCallback | 是 | 一个rpc.MessageSequence类型入参的js通知同步回调函数, 回调函数至少要返回一个空的rpc.Parcelable数据对象, 其他视为函数执行错误。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](通用错误码.md)和[元能力子系统错误码](元能力子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 16200004 | The method has been registered. |
| 16000050 | Internal error. |

**示例：**

```ets
import { UIAbility, AbilityConstant, Want } from '@kit.AbilityKit';
import { rpc } from '@kit.IPCKit';

class MyMessageAble implements rpc.Parcelable {
  name: string
  str: string
  num: number = 1

  constructor(name: string, str: string) {
    this.name = name;
    this.str = str;
  }

  marshalling(messageSequence: rpc.MessageSequence) {
    messageSequence.writeInt(this.num);
    messageSequence.writeString(this.str);
    console.info(`MyMessageAble marshalling num[${this.num}] str[${this.str}]`);
    return true;
  }

  unmarshalling(messageSequence: rpc.MessageSequence) {
    this.num = messageSequence.readInt();
    this.str = messageSequence.readString();
    console.info(`MyMessageAble unmarshalling num[${this.num}] str[${this.str}]`);
    return true;
  }

let method = 'call_Function';

function funcCallBack(pdata: rpc.MessageSequence) {
  let msg = new MyMessageAble('test', '');
  pdata.readParcelable(msg);
  return new MyMessageAble('test1', 'Callee test');
}

export default class MainUIAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    console.info('Callee onCreate is called');
    try {
      this.callee.on(method, funcCallBack);
    } catch (error) {
      console.error(`Callee.on catch error, error.code: ${error.code}, error.message: ${error.message}`);
    }
```

#### off

off(method: string): void

解除通用组件服务端注册消息通知callback。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| method | string | 是 | 已注册的通知事件字符串。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](通用错误码.md)和[元能力子系统错误码](元能力子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 16200005 | The method has not been registered. |
| 16000050 | Internal error. |

**示例：**

```ets
import { UIAbility, AbilityConstant, Want } from '@kit.AbilityKit';

let method = 'call_Function';

export default class MainUIAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    console.info('Callee onCreate is called');
    try {
      this.callee.off(method);
    } catch (error) {
      console.error(`Callee.off catch error, error.code: ${error.code}, error.message: ${error.message}`);
    }
```

#### OnReleaseCallback

#### (msg: string)

(msg: string): void

注册通用组件服务端Stub（桩）断开监听通知的回调函数类型。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| msg | string | 是 | 用于传递释放消息。 |

**OnRemoteStateChangeCallback10+**

#### (msg: string)10+

(msg: string): void

注册协同场景下跨设备组件状态变化监听通知的回调函数类型。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| msg | string | 是 | 用于传递释放消息。 |

#### CalleeCallback

#### (indata: rpc.MessageSequence)

(indata: rpc.MessageSequence): rpc.Parcelable

通用组件服务端注册消息通知的回调函数类型。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| indata | rpc.MessageSequence | 是 | 发送需传递的数据。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| rpc.Parcelable | 返回的数据对象。 |