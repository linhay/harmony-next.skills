# @ohos.app.ability.contextConstant (Context相关常量)

ContextConstant提供Context相关的枚举，包含文件加密分区等级、UIAbility启动后的进程模式等。

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

#### 导入模块

```ets
import { contextConstant } from '@kit.AbilityKit';
```

#### AreaMode

文件加密分区等级，保证应用在不同场景下的数据安全。开发者可以根据应用的具体需求选择合适的加密等级，以保护用户的数据安全。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

名称值说明EL10

设备级加密区，设备开机后可访问的数据区。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

EL21

用户级加密区，设备开机，首次输入密码后才能够访问的数据区。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

EL311+2

用户级加密区，不同场景的文件权限如下：

已打开文件：锁屏时，可读写；解锁后，可读写。

未打开文件：锁屏时，不可打开、不可读写；解锁后，可打开、可读写。

创建新文件：锁屏时，可创建、可打开、可写不可读；解锁后，可创建、可打开、可读写。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

EL411+3

用户级加密区，不同场景的文件权限如下：

已打开文件：锁屏时，不可读写；解锁后，可读写。

未打开文件：锁屏时，不可打开、不可读写；解锁后，可打开、可读写。

创建新文件：锁屏时，不可创建；解锁后，可创建、可打开、可读写。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

EL512+4

应用级加密区，不同场景的文件权限如下：

已打开文件：锁屏时，可读写；解锁后，可读写。

未打开文件：锁屏时，调用[Access](@ohos.ability.screenLockFileManager (锁屏敏感数据管理).md#ZH-CN_TOPIC_0000002529444571__screenlockfilemanageracquireaccess)接口获取保留密钥后，可打开、可读写，否则不可打开、不可读写；解锁后，可打开、可读写。

创建新文件：锁屏时，可创建、可打开、可读写；解锁后，可创建、可打开、可读写。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

#### ProcessMode12+

UIAbility启动后的进程模式。

ProcessMode作为[StartOptions](@ohos.app.ability.StartOptions (startAbility的可选参数).md)的一个属性，仅在[UIAbilityContext.startAbility](../../topics/graphics/UIAbilityContext.md#ZH-CN_TOPIC_0000002497604628__startability-1)中生效，用来指定目标UIAbility的进程模式。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**设备行为差异**：该功能仅在2in1和Tablet设备上生效，在其他设备中返回801错误码。

名称值说明NEW_PROCESS_ATTACH_TO_PARENT1

创建一个新进程，并在该进程上启动UIAbility。该进程会跟随父进程退出。

**约束：**

使用此模式时，要求目标UIAbility跟调用方是在同一个应用。

NEW_PROCESS_ATTACH_TO_STATUS_BAR_ITEM2

创建一个新进程，在该进程上启动UIAbility，并绑定该进程到状态栏图标上。

**约束：**

使用此模式时，要求目标UIAbility跟调用方是在同一个应用，并且应用要在状态栏中有图标。

ATTACH_TO_STATUS_BAR_ITEM3

启动UIAbility，并绑定该UIAbility所在进程到状态栏图标上。

**约束：**

使用此模式时，要求目标UIAbility跟调用方是在同一个应用，并且应用要在状态栏中有图标。

**示例：**

```ets
import { UIAbility, Want, StartOptions, contextConstant } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onForeground() {
    let want: Want = {
      deviceId: '',
      bundleName: 'com.example.myapplication',
      abilityName: 'MainAbility2'
    };
    let options: StartOptions = {
      processMode: contextConstant.ProcessMode.NEW_PROCESS_ATTACH_TO_STATUS_BAR_ITEM,
      startupVisibility: contextConstant.StartupVisibility.STARTUP_HIDE
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

#### StartupVisibility12+

UIAbility启动后是否可见。

当用户设置目标UIAbility为不可见时，目标UIAbility的窗口不会显示在前台，dock栏也不会有图标，同时目标UIAbility的onForeground生命周期不会被调用。

StartupVisibility作为[StartOptions](@ohos.app.ability.StartOptions (startAbility的可选参数).md)的一个属性，仅在[UIAbilityContext.startAbility](../../topics/graphics/UIAbilityContext.md#ZH-CN_TOPIC_0000002497604628__startability-1)中生效，用来指定目标UIAbility启动后的可见性。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**设备行为差异**：该功能仅在2in1和Tablet设备上生效，在其他设备中返回801错误码。

名称值说明STARTUP_HIDE0目标UIAbility启动后，进入隐藏状态。不会调用UIAbility的onForeground生命周期。STARTUP_SHOW1目标UIAbility启动后，正常显示。

**示例：**

 参见[ContextConstant.ProcessMode](#ZH-CN_TOPIC_0000002497444608__processmode12)。

#### Scenarios20+

表示不触发[onNewWant](@ohos.app.ability.UIAbility (带界面的应用组件).md#ZH-CN_TOPIC_0000002529444559__onnewwant)生命周期回调场景的枚举，用于[setOnNewWantSkipScenarios](../../topics/graphics/UIAbilityContext.md#ZH-CN_TOPIC_0000002497604628__setonnewwantskipscenarios20)接口。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

名称值说明SCENARIO_MOVE_MISSION_TO_FRONT0x00000001共享屏幕时系统将用户选择的UIAbility拉起到前台场景。SCENARIO_SHOW_ABILITY0x00000002[showAbility](../../topics/graphics/UIAbilityContext.md#ZH-CN_TOPIC_0000002497604628__showability12)接口触发的UIAbility到前台场景。SCENARIO_BACK_TO_CALLER_ABILITY_WITH_RESULT0x00000004[backToCallerAbilityWithResult](../../topics/graphics/UIAbilityContext.md#ZH-CN_TOPIC_0000002497604628__backtocallerabilitywithresult12)接口触发的UIAbility到前台场景。

**示例：**

```ets
import { AbilityConstant, contextConstant, UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    let scenarios: number = contextConstant.Scenarios.SCENARIO_MOVE_MISSION_TO_FRONT |
      contextConstant.Scenarios.SCENARIO_SHOW_ABILITY |
      contextConstant.Scenarios.SCENARIO_BACK_TO_CALLER_ABILITY_WITH_RESULT;

    try {
      this.context.setOnNewWantSkipScenarios(scenarios).then(() => {
        // 执行正常业务
        console.info('setOnNewWantSkipScenarios succeed');
      }).catch((err: BusinessError) => {
        // 处理业务逻辑错误
        console.error(`setOnNewWantSkipScenarios failed, code is ${err.code}, message is ${err.message}`);
      });
    } catch (err) {
      // 处理入参错误异常
      let code = (err as BusinessError).code;
      let message = (err as BusinessError).message;
      console.error(`setOnNewWantSkipScenarios failed, code is ${code}, message is ${message}`);
    }
  }
}
```