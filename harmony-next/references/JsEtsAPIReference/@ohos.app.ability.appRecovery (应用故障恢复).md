# @ohos.app.ability.appRecovery (应用故障恢复)

appRecovery模块提供了应用在故障状态下的恢复能力。

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。API9仅支持单进程中单Ability的应用恢复。API10支持进程中包含多个Ability的场景。

#### 导入模块

```ets
import { appRecovery } from '@kit.AbilityKit';
```

#### RestartFlag

应用重启标志，[enableAppRecovery](#ZH-CN_TOPIC_0000002529284599__apprecoveryenableapprecovery)接口重启选项参数，该类型为枚举。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

名称值说明ALWAYS_RESTART0总是重启应用。RESTART_WHEN_JS_CRASH0x0001发生JS_CRASH时重启应用。RESTART_WHEN_APP_FREEZE0x0002发生APP_FREEZE时重启应用。NO_RESTART0xFFFF总是不重启应用。

#### SaveOccasionFlag

保存条件标志，[enableAppRecovery](#ZH-CN_TOPIC_0000002529284599__apprecoveryenableapprecovery)接口状态保存时的选项参数，该类型为枚举。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

名称值说明SAVE_WHEN_ERROR0x0001当发生应用故障时保存。SAVE_WHEN_BACKGROUND0x0002当应用切入后台时保存。

#### SaveModeFlag

状态保存标志，[enableAppRecovery](#ZH-CN_TOPIC_0000002529284599__apprecoveryenableapprecovery)接口状态保存方式的参数，该类型为枚举。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

名称值说明SAVE_WITH_FILE0x0001每次状态保存都会写入到本地文件缓存。SAVE_WITH_SHARED_MEMORY0x0002状态先保存在内存中，应用故障退出时写入到本地文件缓存。

#### appRecovery.enableAppRecovery

enableAppRecovery(restart?: [RestartFlag](#ZH-CN_TOPIC_0000002529284599__restartflag), saveOccasion?: [SaveOccasionFlag](#ZH-CN_TOPIC_0000002529284599__saveoccasionflag), saveMode?: [SaveModeFlag](#ZH-CN_TOPIC_0000002529284599__savemodeflag)) : void

使能应用恢复功能，参数按顺序填入。该接口调用后，应用从启动器启动时第一个Ability支持恢复。

**模型约束**：此接口仅可在Stage模型下使用。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

参数名类型必填说明restart[RestartFlag](#ZH-CN_TOPIC_0000002529284599__restartflag)否枚举类型，发生对应故障时是否重启，默认为重启。saveOccasion[SaveOccasionFlag](#ZH-CN_TOPIC_0000002529284599__saveoccasionflag)否枚举类型，状态保存时机，默认为故障时保存。saveMode[SaveModeFlag](#ZH-CN_TOPIC_0000002529284599__savemodeflag)否枚举类型，状态保存方式， 默认为文件缓存。

**示例：**

```ets
import { appRecovery, AbilityStage } from '@kit.AbilityKit';

export default class MyAbilityStage extends AbilityStage {
  onCreate() {
    appRecovery.enableAppRecovery(
      appRecovery.RestartFlag.ALWAYS_RESTART,
      appRecovery.SaveOccasionFlag.SAVE_WHEN_ERROR,
      appRecovery.SaveModeFlag.SAVE_WITH_FILE
    );
  }
}
```

#### appRecovery.restartApp

restartApp(): void

重启当前进程，并拉起应用启动时第一个Ability，如果该Ability存在已经保存的状态，这些状态数据会在Ability的onCreate生命周期回调的want参数中作为wantParam属性传入。

API10时将启动由[setRestartWant](#ZH-CN_TOPIC_0000002529284599__apprecoverysetrestartwant10)指定的Ability。如果没有指定则按以下规则启动：

如果当前应用前台的Ability支持恢复，则重新拉起该Ability。

如果存在多个支持恢复的Ability处于前台，则只拉起最后一个。

如果没有Ability处于前台，则不拉起。

可以配合[errorManager](@ohos.app.ability.errorManager (错误管理模块).md)相关接口使用。两次重启的间隔应大于一分钟，一分钟之内重复调用此接口只会退出应用不会重启应用。自动重启的行为与主动重启一致。

**模型约束**：此接口仅可在Stage模型下使用。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**示例：**

```ets
import { appRecovery, errorManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let observer: errorManager.ErrorObserver = {
  onUnhandledException(errorMsg) {
    console.error('onUnhandledException, errorMsg: ', errorMsg);
    appRecovery.restartApp();
  }
};

try {
  errorManager.on('error', observer);
} catch (paramError) {
  console.error(`error: ${(paramError as BusinessError).code}, ${(paramError as BusinessError).message}`);
}
```

#### appRecovery.saveAppState

saveAppState(): boolean

保存当前App状态，可以配合[errorManager](@ohos.app.ability.errorManager (错误管理模块).md)相关接口使用。

**模型约束**：此接口仅可在Stage模型下使用。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**返回值：**

类型说明boolean保存成功与否。true：保存成功，false：保存失败。

**示例：**

```ets
import { appRecovery, errorManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let observer: errorManager.ErrorObserver = {
  onUnhandledException(errorMsg) {
    console.error('onUnhandledException, errorMsg: ', errorMsg);
    appRecovery.saveAppState();
  }
};

try {
  errorManager.on('error', observer);
} catch (paramError) {
  console.error(`error: ${(paramError as BusinessError).code}, ${(paramError as BusinessError).message}`);
}
```

#### appRecovery.saveAppState10+

saveAppState(context?: UIAbilityContext): boolean

主动保存Ability的状态，这个状态将在下次恢复启动时使用。可以配合[errorManager](@ohos.app.ability.errorManager (错误管理模块).md)相关接口使用。

**模型约束**：此接口仅可在Stage模型下使用。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

参数名类型必填说明context[UIAbilityContext](UIAbilityContext.md)否需要保存状态的UIAbility所对应的context。

**返回值：**

类型说明boolean保存成功与否。true：保存成功，false：保存失败。

**示例：**

```ets
import { appRecovery, errorManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let observer: errorManager.ErrorObserver = {
  onUnhandledException(errorMsg) {
    console.error('onUnhandledException, errorMsg: ', errorMsg);
    appRecovery.saveAppState(this.context);
  }
};

try {
  errorManager.on('error', observer);
} catch (paramError) {
  console.error(`error: ${(paramError as BusinessError).code}, ${(paramError as BusinessError).message}`);
}
```

#### appRecovery.setRestartWant10+

setRestartWant(want: Want): void

设置下次恢复主动拉起场景下的Ability。该Ability必须为当前包下的UIAbility。

**模型约束**：此接口仅可在Stage模型下使用。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

参数名类型必填说明want[Want](@ohos.app.ability.Want (Want).md)是通过设置Want中"bundleName"和"abilityName"字段来指定恢复重启的Ability。

**示例：**

```ets
import { appRecovery, Want } from '@kit.AbilityKit';

@Entry
@Component
struct Index {
  build() {
    Button("启动到恢复Ability")
      .fontSize(40)
      .fontWeight(FontWeight.Bold)
      .onClick(()=> {
        // set restart want
        let want: Want = {
          bundleName: "ohos.samples.recovery",
          abilityName: "RecoveryAbility"
        };

        appRecovery.setRestartWant(want);
      })
  }
}
```