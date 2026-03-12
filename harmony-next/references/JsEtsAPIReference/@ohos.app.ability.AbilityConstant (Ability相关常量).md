# @ohos.app.ability.AbilityConstant (Ability相关常量)

AbilityConstant提供Ability相关的枚举，包括应用启动原因[LaunchReason](#ZH-CN_TOPIC_0000002497604576__launchreason)、上次退出原因[LastExitReason](#ZH-CN_TOPIC_0000002497604576__lastexitreason)、迁移结果[OnContinueResult](#ZH-CN_TOPIC_0000002497604576__oncontinueresult)等。

-

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

-

本模块接口仅可在Stage模型下使用。

#### 导入模块

```ets
import { AbilityConstant } from '@kit.AbilityKit';
```

#### 常量

**系统能力**：SystemCapability.Ability.AbilityBase

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

名称类型值说明REASON_MESSAGE_DESKTOP_SHORTCUT20+string"ReasonMessage_DesktopShortcut"通过桌面快捷方式启动。开发者如果从[LaunchParam](#ZH-CN_TOPIC_0000002497604576__launchparam)的launchReasonMessage属性中获取到该字符串，表示UIAbility是通过点击桌面快捷方式启动的。

#### LaunchParam

启动参数，主要包括Ability启动原因以及上次退出原因。Ability启动时由系统自动传入，开发者无需修改。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

名称类型只读可选说明launchReason[LaunchReason](#ZH-CN_TOPIC_0000002497604576__launchreason)否否

枚举类型，表示Ability启动原因（如故障恢复拉起、意图调用拉起、元服务分享拉起等），详见[LaunchReason](#ZH-CN_TOPIC_0000002497604576__launchreason)。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

launchReasonMessage18+string否是

表示Ability启动的详细原因。

**元服务API**：从API version 18开始，该接口支持在元服务中使用。

lastExitReason[LastExitReason](#ZH-CN_TOPIC_0000002497604576__lastexitreason)否否

枚举类型，表示Ability上次退出原因。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

lastExitMessage12+string否否

表示Ability上次退出的详细原因。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

lastExitDetailInfo18+[LastExitDetailInfo](#ZH-CN_TOPIC_0000002497604576__lastexitdetailinfo18)否是

表示Ability上次退出时的关键运行信息（含进程ID、退出时间戳、RSS内存值等）。

**元服务API**：从API version 18开始，该接口支持在元服务中使用。

#### LaunchReason

Ability启动原因，该类型为枚举，可配合UIAbility的[onCreate(want, launchParam)](@ohos.app.ability.UIAbility (带界面的应用组件).md#ZH-CN_TOPIC_0000002529444559__oncreate)方法根据launchParam.launchReason的不同类型执行相应操作。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

名称值说明UNKNOWN0

未知原因。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

START_ABILITY1

通过[startAbility](UIAbilityContext.md#ZH-CN_TOPIC_0000002497604628__startability)接口启动Ability。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

CALL2

通过[startAbilityByCall](UIAbilityContext.md#ZH-CN_TOPIC_0000002497604628__startabilitybycall)接口启动Ability。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

CONTINUATION3

跨端迁移启动Ability。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

APP_RECOVERY4

设置应用恢复后，应用故障时自动恢复启动Ability。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

SHARE10+5

通过元服务分享启动Ability。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

AUTO_STARTUP11+8通过设置开机自启动来启动Ability。INSIGHT_INTENT11+9

通过洞察意图来启动Ability。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

PREPARE_CONTINUATION12+10

跨端迁移提前启动Ability。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

PRELOAD20+11

表明该UIAbility是通过预加载机制启动的。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**示例：**

```ets
import { UIAbility, Want, AbilityConstant } from '@kit.AbilityKit';

export default class MyAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    if (launchParam.launchReason === AbilityConstant.LaunchReason.START_ABILITY) {
      console.info('The ability has been started by the way of startAbility.');
    }
  }
}
```

#### LastExitReason

Ability上次退出原因，该类型为枚举，可配合UIAbility的[onCreate()](@ohos.app.ability.UIAbility (带界面的应用组件).md#ZH-CN_TOPIC_0000002529444559__oncreate)方法根据launchParam.lastExitReason的不同类型执行相应操作。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

名称值说明UNKNOWN0

未知原因。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

ABILITY_NOT_RESPONDING(deprecated)1

Ability未响应。

**说明:** 从API version 9开始支持，从API version 10开始废弃，请使用APP_FREEZE替代。

NORMAL2

用户主动关闭，应用程序正常退出。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**说明**：当开发者直接调用[process.exit()](@ohos.process (获取进程相关的信息).md#ZH-CN_TOPIC_0000002497604752__processexitdeprecated)、内核kill命令等非Ability Kit提供的能力强制退出应用进程时，也会返回NORMAL。

CPP_CRASH10+3

[进程崩溃](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cppcrash-guidelines)导致的应用程序退出。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

JS_ERROR10+4

当应用存在JS语法错误并未被开发者捕获时，触发JS_ERROR故障，导致应用程序退出。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

APP_FREEZE10+5

[应用冻屏](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/appfreeze-guidelines)导致的应用程序退出。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

PERFORMANCE_CONTROL10+6

因系统性能问题（如设备内存不足）导致的应用程序退出。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**说明**：该接口即将废弃，建议使用RESOURCE_CONTROL替代。

RESOURCE_CONTROL10+7

系统资源使用不当导致的应用程序退出。具体错误原因可以通过[LaunchParam.lastExitMessage](#ZH-CN_TOPIC_0000002497604576__launchparam)获取，可能原因如下:

- CPU Highload，CPU高负载。

- CPU_EXT Highload，快速CPU负载检测。

- IO Manage Control，I/O管控。

- App Memory Deterioration，应用内存超限劣化。

- Temperature Control，温度管控。

- Memory Pressure，整机低内存触发按优先级由低到高终止进程。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

UPGRADE10+8

应用升级导致的应用程序退出。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

USER_REQUEST18+9

应用程序因多任务中心请求而退出。

**元服务API**：从API version 18开始，该接口支持在元服务中使用。

SIGNAL18+10

应用程序因收到系统kill指令信号而退出。

**元服务API**：从API version 18开始，该接口支持在元服务中使用。

**示例：**

```ets
import { UIAbility, Want, AbilityConstant } from '@kit.AbilityKit';

export default class MyAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    if (launchParam.lastExitReason === AbilityConstant.LastExitReason.APP_FREEZE) {
      console.info('The ability has exit last because the ability was not responding.');
    }
    if (launchParam.lastExitReason === AbilityConstant.LastExitReason.RESOURCE_CONTROL) {
      console.info(`The ability has exit last because the rss control，the lastExitReason is ${launchParam.lastExitReason}, the lastExitMessage is ${launchParam.lastExitMessage}.`);
    }
  }
}
```

#### LastExitDetailInfo18+

记录Ability所在进程上次退出时的关键运行信息。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

名称类型只读可选说明pidnumber否否

Ability上次退出所在进程的进程号。

**元服务API**：从API version 18开始，该接口支持在元服务中使用。

processNamestring否否

Ability上次退出所在进程的名称。

**元服务API**：从API version 18开始，该接口支持在元服务中使用。

uidnumber否否

Ability上次退出所在应用的UID。

**元服务API**：从API version 18开始，该接口支持在元服务中使用。

exitSubReasonnumber否否

Ability上次退出的子原因。

**元服务API**：从API version 18开始，该接口支持在元服务中使用。

exitMsgstring否否

Ability上次退出时所在进程被kill的描述信息。

**元服务API**：从API version 18开始，该接口支持在元服务中使用。

rssnumber否否

Ability上次退出时所在进程实际占用内存大小，单位KB。

**元服务API**：从API version 18开始，该接口支持在元服务中使用。

pssnumber否否

Ability上次退出时所在进程实际使用的物理内存大小，单位KB。

**元服务API**：从API version 18开始，该接口支持在元服务中使用。

timestampnumber否否

Ability上次退出时的时间戳。

**元服务API**：从API version 18开始，该接口支持在元服务中使用。

processState20+[appManager.ProcessState](@ohos.app.ability.appManager (应用管理).md#ZH-CN_TOPIC_0000002497444628__processstate10)否是

Ability上次退出时的进程状态。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**示例**:

```ets
import { UIAbility, Want, AbilityConstant } from '@kit.AbilityKit';

export default class MyAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    if (launchParam.lastExitDetailInfo) {
      console.info(`pid: ${launchParam.lastExitDetailInfo.pid}
      \n processName: ${launchParam.lastExitDetailInfo.processName}
      \n uid: ${launchParam.lastExitDetailInfo.uid}
      \n exitSubReason: ${launchParam.lastExitDetailInfo.exitSubReason}
      \n exitMsg: ${launchParam.lastExitDetailInfo.exitMsg}
      \n rss: ${launchParam.lastExitDetailInfo.rss}
      \n pss: ${launchParam.lastExitDetailInfo.pss}
      \n timestamp: ${launchParam.lastExitDetailInfo.timestamp}
      \n processState: ${launchParam.lastExitDetailInfo.processState}.`
      );
    }
  }
}
```

#### OnContinueResult

Ability迁移结果，该类型为枚举，可配合UIAbility的[onContinue()](@ohos.app.ability.UIAbility (带界面的应用组件).md#ZH-CN_TOPIC_0000002529444559__oncontinue)方法完成相应的返回。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

名称值说明AGREE0表示同意。REJECT1表示拒绝：如应用在[onContinue](@ohos.app.ability.UIAbility (带界面的应用组件).md#ZH-CN_TOPIC_0000002529444559__oncontinue)中异常会导致迁移以后数据恢复时显示异常，则可以返回REJECT。MISMATCH2表示版本不匹配：迁移发起端应用可以在[onContinue](@ohos.app.ability.UIAbility (带界面的应用组件).md#ZH-CN_TOPIC_0000002529444559__oncontinue)中获取到迁移目标端应用的版本号，进行协商后，如果版本不匹配导致无法迁移，可以返回该结果。

**示例：**

```ets
import { UIAbility, AbilityConstant } from '@kit.AbilityKit';

export default class MyAbility extends UIAbility {
  onContinue(wantParam: Record<string, Object>) {
    return AbilityConstant.OnContinueResult.AGREE;
  }
}
```

#### MemoryLevel

整机可用内存级别，该类型为枚举，可配合UIAbility的[onMemoryLevel()](@ohos.app.ability.Ability (Ability基类).md#ZH-CN_TOPIC_0000002529444543__abilityonmemorylevel)方法根据level执行不同内存级别的相应操作。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

名称值说明MEMORY_LEVEL_MODERATE0整机可用内存适中。MEMORY_LEVEL_LOW1整机可用内存低。MEMORY_LEVEL_CRITICAL2整机可用内存极低。

不同产品的触发条件可能存在差异。以12G内存的标准设备为例：

- 当整机可用内存下降至1700M~1800M时，会触发取值为0的onMemoryLevel回调，表示当前整机可用内存适中。
- 当整机可用内存下降至1600M~1700M时，会触发取值为1的onMemoryLevel回调，表示当前整机可用内存偏低。
- 当整机可用内存下降至1600M以下时，会触发取值为2的onMemoryLevel回调，表示当前整机可用内存很低。

**示例：**

```ets
import { UIAbility, AbilityConstant } from '@kit.AbilityKit';

export default class MyAbility extends UIAbility {
  onMemoryLevel(level: AbilityConstant.MemoryLevel) {
    if (level === AbilityConstant.MemoryLevel.MEMORY_LEVEL_CRITICAL) {
      console.info('The memory of device is critical, please release some memory.');
    }
  }
}
```

#### WindowMode12+

启动UIAbility时窗口的创建模式，类型为枚举。可配合[startAbility](UIAbilityContext.md#ZH-CN_TOPIC_0000002497604628__startability-2)方法使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

名称值说明WINDOW_MODE_FULLSCREEN1全屏模式。仅在2in1和Tablet设备上生效。WINDOW_MODE_SPLIT_PRIMARY100支持应用内拉起Ability时设置为分屏，左侧分屏。仅在折叠屏和Tablet设备上生效。WINDOW_MODE_SPLIT_SECONDARY101支持应用内拉起Ability时设置为分屏，右侧分屏。仅在折叠屏和Tablet设备上生效。

**示例：**

```ets
import { UIAbility, StartOptions, Want, AbilityConstant } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let want: Want = {
  bundleName: 'com.example.myapplication',
  abilityName: 'EntryAbility'
};
let option: StartOptions = {
  windowMode: AbilityConstant.WindowMode.WINDOW_MODE_SPLIT_PRIMARY
};

// 确保从上下文获取到context
export default class MyAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    this.context.startAbility(want, option).then(() => {
      console.info('Succeed to start ability.');
    }).catch((error: BusinessError) => {
      console.error(`Failed to start ability with error: ${JSON.stringify(error)}`);
    });
  }
}
```

#### OnSaveResult

保存应用数据的结果，该类型为枚举。配合UIAbility的[onSaveState()](@ohos.app.ability.UIAbility (带界面的应用组件).md#ZH-CN_TOPIC_0000002529444559__onsavestate)方法使用，可以实现[UIAbility备份恢复](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ability-recover-guideline)。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

名称值说明ALL_AGREE0总是同意保存状态。CONTINUATION_REJECT1拒绝迁移保存状态。CONTINUATION_MISMATCH2迁移不匹配。RECOVERY_AGREE3同意恢复保存状态。RECOVERY_REJECT4拒绝恢复保存状态。ALL_REJECT5总是拒绝保存状态。

**示例：**

```ets
import { UIAbility, AbilityConstant } from '@kit.AbilityKit';

export default class MyAbility extends UIAbility {
  onSaveState(reason: AbilityConstant.StateType, wantParam: Record<string, Object>) {
    return AbilityConstant.OnSaveResult.ALL_AGREE;
  }
}
```

#### StateType

保存应用数据场景原因，该类型为枚举。配合UIAbility的[onSaveState()](@ohos.app.ability.UIAbility (带界面的应用组件).md#ZH-CN_TOPIC_0000002529444559__onsavestate)方法使用，可以实现[UIAbility备份恢复](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ability-recover-guideline)。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

名称值说明CONTINUATION0应用迁移场景。APP_RECOVERY1应用故障恢复场景。

**示例：**

```ets
import { UIAbility, AbilityConstant } from '@kit.AbilityKit';

export default class MyAbility extends UIAbility {
  onSaveState(reason: AbilityConstant.StateType, wantParam: Record<string, Object>) {
    if (reason === AbilityConstant.StateType.CONTINUATION) {
      console.info('Save the ability data when the ability continuation.');
    }
    return AbilityConstant.OnSaveResult.ALL_AGREE;
  }
}
```

#### ContinueState10+

流转状态枚举值。用于表示当前应用任务流转的状态。可配合[UIAbilityContext](UIAbilityContext.md)的[setMissionContinueState](UIAbilityContext.md#ZH-CN_TOPIC_0000002497604628__setmissioncontinuestate10)方法进行设置。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

名称值说明ACTIVE0指示当前应用任务流转处于激活状态。INACTIVE1指示当前应用任务流转处于未激活状态。

**示例：**

```ets
import { UIAbility, Want, AbilityConstant } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class MyAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    this.context.setMissionContinueState(AbilityConstant.ContinueState.INACTIVE, (result: BusinessError) => {
      console.info(`setMissionContinueState: ${JSON.stringify(result)}`);
    });
  }
}
```

#### CollaborateResult18+

应用协同状态，该类型为枚举。用于多设备场景下，调用方应用拉起协同方应用时，协同方应用是否接受协同。需要配合UIAbility的[onCollaborate()](@ohos.app.ability.UIAbility (带界面的应用组件).md#ZH-CN_TOPIC_0000002529444559__oncollaborate18)方法进行设置。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

名称值说明ACCEPT0接受协同。REJECT1拒绝协同。

**示例：**

```ets
import { UIAbility, AbilityConstant } from '@kit.AbilityKit';

export default class MyAbility extends UIAbility {
  onCollaborate(wantParam: Record<string, Object>) {
    return AbilityConstant.CollaborateResult.ACCEPT;
  }
}
```

#### PrepareTermination15+

应用准备关闭时返回的动作，该类型为枚举。需要配合[AbilityStage](@ohos.app.ability.AbilityStage (AbilityStage组件管理器).md)的[onPrepareTermination](@ohos.app.ability.AbilityStage (AbilityStage组件管理器).md#ZH-CN_TOPIC_0000002529284571__onpreparetermination15)或者[onPrepareTerminationAsync](@ohos.app.ability.AbilityStage (AbilityStage组件管理器).md#ZH-CN_TOPIC_0000002529284571__onprepareterminationasync15)方法使用。

**元服务API**：从API version 15开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

名称值说明TERMINATE_IMMEDIATELY0表示立即执行结束动作，默认值。CANCEL1表示取消结束动作。

**示例：**

```ets
import { AbilityConstant, AbilityStage } from '@kit.AbilityKit';

export default class MyAbilityStage extends AbilityStage {
  onPrepareTermination(): AbilityConstant.PrepareTermination {
    console.info('MyAbilityStage.onPrepareTermination is called');
    return AbilityConstant.PrepareTermination.CANCEL;
  }
}
```