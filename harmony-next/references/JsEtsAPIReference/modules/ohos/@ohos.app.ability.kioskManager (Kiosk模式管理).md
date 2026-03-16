# @ohos.app.ability.kioskManager (Kiosk模式管理)

KioskManager模块提供Kiosk模式管理能力，包括系统进入/退出Kiosk模式操作。

Kiosk模式是一种特殊的设备锁定模式，可以确保设备界面只服务于特定的交互场景。在这种模式下，用户只能使用特定的应用。例如，在银行ATM机上，用户只能通过ATM软件进行操作，而不能退出该软件或切换到其他应用。

- 本模块首批接口从API version 20开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
- 本模块接口仅可在Stage模型下使用。
- 本模块接口仅适用于通过[setAllowedKioskApps接口](@ohos.enterprise.applicationManager（应用管理）.md#ZH-CN_TOPIC_0000002497605586__applicationmanagersetallowedkioskapps20)配置的支持Kiosk模式的应用。

#### 导入模块

```ets
import { kioskManager } from '@kit.AbilityKit';
```

#### kioskManager.enterKioskMode

enterKioskMode(context: UIAbilityContext): Promise<void>

进入Kiosk模式。使用Promise异步回调。

**系统能力**： SystemCapability.Ability.AbilityRuntime.Core

**设备行为差异**：该接口仅在2in1和Tablet设备中可正常调用，在其他设备中返回801错误码。

**参数**：

参数名类型必填说明context[UIAbilityContext](../../topics/graphics/UIAbilityContext.md)是需要进入kiosk模式的UIAbility的上下文。

**返回值：**

类型说明Promise<void>无返回结果的Promise对象。

**错误码**：

以下错误码详细介绍请参考[通用错误码](../../errors/通用错误码.md)和[元能力子系统错误码](../../errors/元能力子系统错误码.md)。

错误码ID错误信息801Capability not supported.16000050Failed to connect to the system service.16000110The current application is not in Kiosk app list and cannot enter Kiosk mode.16000111The system is already in Kiosk mode and cannot enter Kiosk mode again.16000113Current ability is not in foreground.

**示例**：

```ets
import { common, kioskManager } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  private uiAbilityContext: common.UIAbilityContext | undefined =
    this.getUIContext().getHostContext() as common.UIAbilityContext;

  build() {
    Column() {
      Button('enterKioskMode').margin({ top: 30 })
        .onClick(() => {
          kioskManager.enterKioskMode(this.uiAbilityContext)
            .then(() => {
              hilog.info(0x0000, 'testTag', '%{public}s', 'enterKioskMode success');
            })
            .catch((error: BusinessError) => {
              hilog.error(0x0000, 'testTag', '%{public}s', `enterKioskMode failed:${JSON.stringify(error)}`);
            });
        })
    }
    .height('100%')
    .width('100%')
  }
}
```

#### kioskManager.exitKioskMode

exitKioskMode(context: UIAbilityContext): Promise<void>

退出Kiosk模式。使用Promise异步回调。

该接口仅对已进入Kiosk模式的应用生效。

**系统能力**： SystemCapability.Ability.AbilityRuntime.Core

**设备行为差异**：该接口仅在2in1和Tablet设备中可正常调用，在其他设备中返回801错误码。

**参数**：

参数名类型必填说明context[UIAbilityContext](../../topics/graphics/UIAbilityContext.md)是需要退出kiosk模式的UIAbility的上下文。

**返回值：**

类型说明Promise<void>无返回结果的Promise对象。

**错误码**：

以下错误码详细介绍请参考[通用错误码](../../errors/通用错误码.md)和[元能力子系统错误码](../../errors/元能力子系统错误码.md)。

错误码ID错误信息801Capability not supported.16000050Failed to connect to the system service.16000110The current application is not in Kiosk app list and cannot enter Kiosk mode.16000112The current application is not in Kiosk mode and cannot exit Kiosk mode.

**示例**：

```ets
import { common, kioskManager } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  private uiAbilityContext: common.UIAbilityContext | undefined =
    this.getUIContext().getHostContext() as common.UIAbilityContext;

  build() {
    Column() {
      Button('exitKioskMode').margin({ top: 10 })
        .onClick(() => {
          kioskManager.exitKioskMode(this.uiAbilityContext)
            .then(() => {
              hilog.info(0x0000, 'testTag', '%{public}s', 'exitKioskMode success');
            })
            .catch((error: BusinessError) => {
              hilog.error(0x0000, 'testTag', '%{public}s', `exitKioskMode failed:${JSON.stringify(error)}`);
            });
        })
    }
    .height('100%')
    .width('100%')
  }
}
```

#### KioskStatus

type KioskStatus = _KioskStatus

Kiosk状态信息，包括系统是否处于Kiosk模式以及该模式下的应用信息。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

类型说明[_KioskStatus](../../topics/misc/KioskStatus (Kiosk状态信息).md#ZH-CN_TOPIC_0000002497604626__kioskstatus)表示Kiosk状态信息，包括系统是否处于Kiosk模式以及该模式下的应用信息。