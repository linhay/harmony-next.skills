# @ohos.resourceschedule.backgroundProcessManager (后台子进程管控)

本模块提供了后台子进程管控接口。开发者可以通过本模块接口对子进程进行压制、解压制，避免子进程过多占用系统资源，导致系统使用卡顿。本模块接口仅对通过[OH_Ability_StartNativeChildProcess](../../capi/headers/native_child_process.h.md#ZH-CN_TOPIC_0000002529444625__oh_ability_startnativechildprocess)接口创建的子进程生效。

本模块首批接口从API version 17开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { backgroundProcessManager } from '@kit.BackgroundTasksKit';
```

#### backgroundProcessManager.setProcessPriority

setProcessPriority(pid: number, priority: ProcessPriority): Promise<void>

设置子进程的压制档位，子进程被压制后可获得的CPU资源将会受到限制。如果主进程调度策略发生变化，如从后台切至前台等，子进程会跟随主进程一同变化，子进程如需继续压制，需要重新调用本接口。

**系统能力**： SystemCapability.Resourceschedule.BackgroundProcessManager

**参数**：

参数名类型必填说明pidnumber是需要被压制子进程的进程号，[OH_Ability_StartNativeChildProcess](../../capi/headers/native_child_process.h.md#ZH-CN_TOPIC_0000002529444625__oh_ability_startnativechildprocess)接口创建子进程后的pid参数，即为子进程进程号。priority[ProcessPriority](#ZH-CN_TOPIC_0000002497445262__processpriority)是压制档位。

**返回值**：

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**错误码**：

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: priority is out of range.

**示例**：

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { backgroundProcessManager } from '@kit.BackgroundTasksKit';

let childProcessPid = 33333;
try {
    backgroundProcessManager.setProcessPriority(childProcessPid,
        backgroundProcessManager.ProcessPriority.PROCESS_INACTIVE);
} catch (error) {
    console.error(`setProcessPriority failed, errCode: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}`);
}
```

#### backgroundProcessManager.resetProcessPriority

resetProcessPriority(pid: number): Promise<void>

为子进程解压制，即子进程策略恢复为主进程调度策略。若主进程调度策略发生变化，如从后台切至前台等， 子进程会跟随主进程一同变化，等效于执行一次resetProcessPriority动作。

**系统能力**： SystemCapability.Resourceschedule.BackgroundProcessManager

**参数**：

参数名类型必填说明pidnumber是子进程的进程号，[OH_Ability_StartNativeChildProcess](../../capi/headers/native_child_process.h.md#ZH-CN_TOPIC_0000002529444625__oh_ability_startnativechildprocess)接口创建子进程后的pid参数，即为子进程进程号。

**返回值**：

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**示例**：

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { backgroundProcessManager } from '@kit.BackgroundTasksKit';

let childProcessPid = 33333;
try {
    backgroundProcessManager.resetProcessPriority(childProcessPid);
} catch (error) {
    console.error(`setProcessPriority failed, errCode: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}`);
}
```

#### backgroundProcessManager.setPowerSaveMode20+

setPowerSaveMode(pid: number, powerSaveMode: PowerSaveMode): Promise<void>

设置进程的能效模式，使用Promise异步回调。

当应用满足以下条件时，可以设置自身是否进入能效模式：

- 应用未获取系统焦点，未执行音频或界面刷新操作。
- 无法通过框架层获取电源锁。
- 应用需要执行压缩、解压缩、编译等耗时较长的计算任务，不希望这些任务受到显著的CPU资源限制（即被迫进入能效模式）。

**设备行为差异**：该接口在PC/2in1中可正常调用，在其他设备类型中返回801错误码。

**需要权限**： ohos.permission.BACKGROUND_MANAGER_POWER_SAVE_MODE

**系统能力**： SystemCapability.Resourceschedule.BackgroundProcessManager

**参数**：

参数名类型必填说明pidnumber是进程号。powerSaveMode[PowerSaveMode](#ZH-CN_TOPIC_0000002497445262__powersavemode20)是能效模式。

**返回值**：

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**错误码**：

以下错误码的详细介绍请参见[backgroundProcessManager错误码](../../errors/backgroundProcessManager错误码.md)和[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息201Permission denied.801Capability not supported.31800002

Parameter error. Possible causes:

 1. Mandatory parameters are left unspecified;

 2. Incorrect parameter types; 3. PowerSaveMode status is out of range.

31800003Setup error, This setting is overridden by setting in Task Manager.31800004The setting failed due to system scheduling reasons.

**示例**：

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { backgroundProcessManager } from '@kit.BackgroundTasksKit';

let pid = 33333;
try {
    backgroundProcessManager.setPowerSaveMode(pid, backgroundProcessManager.PowerSaveMode.EFFICIENCY_MODE);
} catch (error) {
    console.error(`setPowerSaveMode failed, errCode: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}`);
}
```

#### backgroundProcessManager.isPowerSaveMode20+

isPowerSaveMode(pid: number): Promise<boolean>

查询进程是否处于能效模式，使用Promise异步回调。

**设备行为差异**：该接口在PC/2in1中可正常调用，在其他设备类型中返回801错误码。

**需要权限**： ohos.permission.BACKGROUND_MANAGER_POWER_SAVE_MODE

**系统能力**： SystemCapability.Resourceschedule.BackgroundProcessManager

**参数**：

参数名类型必填说明pidnumber是进程号。

**返回值**：

类型说明Promise<boolean>Promise对象。返回进程PID是否处于能效模式，返回true表示进程处于能效模式，返回false表示进程未处于能效模式。

**错误码**：

以下错误码的详细介绍请参见[backgroundProcessManager错误码](../../errors/backgroundProcessManager错误码.md)和[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息201Permission denied.801Capability not supported.31800002

Parameter error. Possible causes:

 1. Mandatory parameters are left unspecified;

 2. Incorrect parameter types.

**示例**：

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { backgroundProcessManager } from '@kit.BackgroundTasksKit';

let pid = 33333;
try {
    backgroundProcessManager.isPowerSaveMode(pid).then((result: boolean) => {
        console.info("isPowerSaveMode: " + result.toString());
    });
} catch (error) {
    console.error(`isPowerSaveMode failed, errCode: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}`);
}
```

#### backgroundProcessManager.getPowerSaveMode22+

getPowerSaveMode(pid: number): Promise<PowerSaveMode>

获取进程能效模式。使用Promise异步回调。

**设备行为差异：** 该接口在PC/2in1中可正常调用，在其他设备类型中返回801错误码。

**需要权限：** ohos.permission.BACKGROUND_MANAGER_POWER_SAVE_MODE

**系统能力：** SystemCapability.Resourceschedule.BackgroundProcessManager

**参数：**

参数名类型必填说明pidnumber是

进程号。

取值范围：大于0的整数。

**返回值：**

类型说明Promise<[PowerSaveMode](#ZH-CN_TOPIC_0000002497445262__powersavemode20)>Promise对象。返回进程能效模式状态。

**错误码：**

以下错误码的详细介绍请参见[backgroundProcessManager错误码](../../errors/backgroundProcessManager错误码.md)和[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息201Permission denied.801Capability not supported.31800002

Parameter error. Possible causes:

 1. Mandatory parameters are left unspecified;

 2. Incorrect parameter types.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { backgroundProcessManager } from '@kit.BackgroundTasksKit';
// 请开发者替换为实际的进程号
let pid = 33333;
try {
    backgroundProcessManager.getPowerSaveMode(pid).then((result: PowerSaveMode) => {
        console.info("getPowerSaveMode: " + result.toString());
    });
} catch (error) {
    console.error(`getPowerSaveMode failed, errCode: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}`);
}
```

#### ProcessPriority

子进程压制档位。

**系统能力**： SystemCapability.Resourceschedule.BackgroundProcessManager

名称值说明PROCESS_BACKGROUND1该档位相较PROCESS_INACTIVE压制效果更显著，获取到的CPU资源更少。推荐执行处于后台的图文页面等用户无感知业务的后台子进程时设置该档位。PROCESS_INACTIVE2推荐正在执行播放音频、导航等用户可感知业务的后台子进程时设置该档位。

#### PowerSaveMode20+

能效模式。

**系统能力**： SystemCapability.Resourceschedule.BackgroundProcessManager

名称值说明EFFICIENCY_MODE1效率模式，不会跟随系统进入能效模式，进入能效模式后获取到的CPU资源更少。DEFAULT_MODE2跟随系统，可能会进入能效模式。