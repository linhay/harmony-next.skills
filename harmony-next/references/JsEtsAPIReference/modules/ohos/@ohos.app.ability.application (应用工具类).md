# @ohos.app.ability.application (应用工具类)

开发者可以通过该模块管理和获取应用的上下文[Context](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/application-context-stage)，以及控制应用进程的状态。

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

#### 导入模块

```ets
import { application } from '@kit.AbilityKit';
```

#### AppPreloadType22+

表示应用当前进程的预加载类型枚举。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

名称值说明UNSPECIFIED0未发生预加载或预加载数据已被清除。TYPE_CREATE_PROCESS1进程最终预加载到进程创建完成阶段。TYPE_CREATE_ABILITY_STAGE2进程最终预加载到[AbilityStage](@ohos.app.ability.AbilityStage (AbilityStage组件管理器).md)创建完成阶段。TYPE_CREATE_WINDOW_STAGE3进程最终预加载到[WindowStage](../../types/interfaces/Interface (WindowStage).md)创建完成阶段。

#### application.createModuleContext12+

createModuleContext(context: Context, moduleName: string): Promise<Context>

创建指定模块的上下文。创建出的模块上下文中[resourceManager.Configuration](@ohos.resourceManager (资源管理).md#ZH-CN_TOPIC_0000002497445338__configuration)资源继承自入参上下文，便于开发者获取[跨HAP/HSP包应用资源](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/resource-categories-and-access#跨haphsp包应用资源)。使用Promise异步回调。

由于创建模块上下文的过程涉及资源查询与初始化，耗时相对较长，在对应用流畅性要求较高的场景下，不建议频繁或多次调用createModuleContext接口创建多个Context实例，以免影响用户体验。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数**：

参数名类型必填说明context[Context](../../topics/graphics/Context (Stage模型的上下文基类).md)是表示应用上下文。moduleNamestring是表示应用模块名。

**返回值：**

类型说明Promise<[Context](../../topics/graphics/Context (Stage模型的上下文基类).md)>Promise对象。返回创建的Context。

**错误码：**

以下错误码详细介绍请参考[通用错误码说明文档](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.

**示例：**

```ets
import { AbilityConstant, UIAbility, application, common, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    let moduleContext: common.Context;
    try {
      application.createModuleContext(this.context, 'entry').then((data: Context) => {
        moduleContext = data;
        console.info('createModuleContext success!');
      }).catch((error: BusinessError) => {
        let code: number = (error as BusinessError).code;
        let message: string = (error as BusinessError).message;
        console.error(`createModuleContext failed, error.code: ${code}, error.message: ${message}`);
      });
    } catch (error) {
      let code: number = (error as BusinessError).code;
      let message: string = (error as BusinessError).message;
      console.error(`createModuleContext failed, error.code: ${code}, error.message: ${message}`);
    }
  }
}
```

#### application.getApplicationContext14+

getApplicationContext(): ApplicationContext

获取应用上下文。开发者使用该接口时，无需依赖Context基类。

重复调用该接口，将生成新的ApplicationContext对象。

**元服务API**：从API version 14开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**返回值：**

类型说明[ApplicationContext](../../topics/graphics/ApplicationContext (应用上下文).md)应用上下文。

**错误码：**

以下错误码详细介绍请参考[元能力子系统错误码](../../errors/元能力子系统错误码.md)。

错误码ID错误信息16000050Internal error.

**示例：**

```ets
import { AbilityConstant, UIAbility, application, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    try {
      let applicationContext = application.getApplicationContext();
    } catch (error) {
      let code: number = (error as BusinessError).code;
      let message: string = (error as BusinessError).message;
      console.error(`getApplicationContext failed, error.code: ${code}, error.message: ${message}`);
    }
  }
}
```

#### application.createPluginModuleContext19+

createPluginModuleContext(context: Context, pluginBundleName: string, pluginModuleName: string): Promise<Context>

根据入参Context、指定的插件包名和插件模块名，创建本应用下插件的Context，用于获取插件的基本信息。使用Promise异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数**：

参数名类型必填说明context[Context](../../topics/graphics/Context (Stage模型的上下文基类).md)是表示应用上下文。pluginBundleNamestring是表示应用的插件包名。pluginModuleNamestring是表示应用的插件模块名。

**返回值：**

类型说明Promise<[Context](../../topics/graphics/Context (Stage模型的上下文基类).md)>Promise对象。返回创建的Context。

**示例：**

```ets
import { AbilityConstant, UIAbility, application, common, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    let moduleContext: common.Context;
    try {
      application.createPluginModuleContext(this.context, 'com.example.pluginBundleName', 'pluginModuleName')
        .then((data: Context) => {
          moduleContext = data;
          console.info('createPluginModuleContext success!');
        })
        .catch((error: BusinessError) => {
          let code: number = (error as BusinessError).code;
          let message: string = (error as BusinessError).message;
          console.error(`createPluginModuleContext failed, error.code: ${code}, error.message: ${message}`);
        });
    } catch (error) {
      let code: number = (error as BusinessError).code;
      let message: string = (error as BusinessError).message;
      console.error(`createPluginModuleContext failed, error.code: ${code}, error.message: ${message}`);
    }
  }
}
```

#### application.promoteCurrentToCandidateMasterProcess20+

promoteCurrentToCandidateMasterProcess(insertToHead: boolean): Promise<void>

开发者可以调用该接口将当前进程放入[备选主控进程](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ability-terminology#candidatemasterprocess备选主控进程)链表。使用Promise异步回调。

当[主控进程](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ability-terminology#masterprocess主控进程)销毁后，再次启动配置了isolationProcess为true的UIAbility/UIExtensionAbility组件时，系统会根据是否存在备选主控进程执行相应操作。

- 如果存在备选主控进程，系统会将备选主控进程链表首节点的进程设置为主控进程，触发[onNewProcessRequest](@ohos.app.ability.AbilityStage (AbilityStage组件管理器).md#ZH-CN_TOPIC_0000002529284571__onnewprocessrequest11)回调。
- 如果不存在备选主控进程，系统会根据组件类型执行相应的操作。

  - 对于UIAbility组件，系统将创建新的空进程作为主控进程。
  - 对于UIExtensionAbility组件，系统会优先复用已有的UIExtensionAbility进程作为新的主控进程，无可用进程时则创建新的空进程作为主控进程。

如果当前进程已经是[主控进程](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ability-terminology#masterprocess主控进程)，调用该接口无效并且不会抛出错误码。

当前进程只有运行了isolationProcess字段设为true的组件，或曾经成为过主控进程，开发者才可将其设置为备选主控进程。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**设备行为差异**：该接口在PC/2in1、Tablet中可正常调用，在其他设备类型中返回801错误码。

**参数**：

参数名类型必填说明insertToHeadboolean是表示是否将当前进程放入备选主控进程链表的表头。true表示放入表头，false表示放入表尾。

**返回值：**

类型说明Promise<void>Promise对象。无返回结果。

**错误码：**

以下错误码详细介绍请参考[通用错误码说明文档](../../errors/通用错误码.md)和[元能力子系统错误码](../../errors/元能力子系统错误码.md)。

错误码ID错误信息801Capability not supported.16000115The current process cannot be set as a candidate master process.

**示例：**

```ets
import { AbilityConstant, UIAbility, application, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    try {
      application.promoteCurrentToCandidateMasterProcess(true)
        .then(() => {
          console.info('promote succeed');
        })
        .catch((err: BusinessError) => {
          console.error(`promote failed, code is ${err.code}, message is ${err.message}`);
        });
    } catch (error) {
      let code: number = (error as BusinessError).code;
      let message: string = (error as BusinessError).message;
      console.error(`promoteCurrentToCandidateMasterProcess failed, error.code: ${code}, error.message: ${message}`);
    }
  }
}
```

#### application.demoteCurrentFromCandidateMasterProcess20+

demoteCurrentFromCandidateMasterProcess(): Promise<void>

撤销当前进程的备选主控进程资格。使用Promise异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**设备行为差异**：该接口在PC/2in1、Tablet中可正常调用，在其他设备类型中返回801错误码。

**返回值：**

类型说明Promise<void>Promise对象。无返回结果。

**错误码：**

以下错误码详细介绍请参考[通用错误码说明文档](../../errors/通用错误码.md)和[元能力子系统错误码](../../errors/元能力子系统错误码.md)。

错误码ID错误信息801Capability not supported.16000116The current process is already a master process and does not support cancellation.16000117The current process is not a candidate master process and does not support cancellation.

**示例：**

```ets
import { AbilityConstant, UIAbility, application, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    try {
      application.demoteCurrentFromCandidateMasterProcess()
        .then(() => {
          console.info('demote succeed');
        })
        .catch((err: BusinessError) => {
          console.error(`demote failed, code is ${err.code}, message is ${err.message}`);
        });
    } catch (error) {
      let code: number = (error as BusinessError).code;
      let message: string = (error as BusinessError).message;
      console.error(`demoteCurrentFromCandidateMasterProcess failed, error.code: ${code}, error.message: ${message}`);
    }
  }
}
```

#### application.exitMasterProcessRole21+

exitMasterProcessRole(): Promise<void>

放弃当前进程的[主控进程](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ability-terminology#masterprocess主控进程)身份。使用Promise异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**设备行为差异：** 该接口仅在2in1、Tablet设备中可正常调用，在其他设备中返回801错误码。

**返回值：**

类型说明Promise<void>Promise对象，无返回结果。

**错误码：**

以下错误码详细介绍请参考[通用错误码说明文档](../../errors/通用错误码.md)和[元能力子系统错误码](../../errors/元能力子系统错误码.md)。

错误码ID错误信息801Capability not supported.16000118Not a master process.16000119Cannot exit because there is an unfinished request.

**示例：**

```ets
import { AbilityConstant, UIAbility, application, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    try {
      application.exitMasterProcessRole()
        .then(() => {
          console.info('exitMasterProcessRole succeed');
        })
        .catch((err: BusinessError) => {
          console.error(`exitMasterProcessRole failed, code is ${err.code}, message is ${err.message}`);
        });
    } catch (error) {
      let code: number = (error as BusinessError).code;
      let message: string = (error as BusinessError).message;
      console.error(`exitMasterProcessRole failed, error.code: ${code}, error.message: ${message}`);
    }
  }
}
```

#### application.getAppPreloadType22+

getAppPreloadType(): AppPreloadType

获取应用当前进程的预加载类型。

- 只有在进程首次执行[AbilityStage.onCreate](@ohos.app.ability.AbilityStage (AbilityStage组件管理器).md#ZH-CN_TOPIC_0000002529284571__oncreate)完成之前调用该接口，才可以返回真实的预加载类型。
- AbilityStage创建完成后，应用的预加载数据将被清除，调用该接口将返回UNSPECIFIED，无法获取到真实的预加载类型。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**返回值：**

类型说明[AppPreloadType](#ZH-CN_TOPIC_0000002497604578__apppreloadtype22)应用当前进程的预加载类型。

**示例：**

```ets
import { AbilityStage, application } from '@kit.AbilityKit';

export default class MyAbilityStage extends AbilityStage{
  onCreate() {
    let appPreloadType = application.getAppPreloadType();
  }
}
```