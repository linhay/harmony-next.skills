# @ohos.app.appstartup.StartupTask (启动框架任务)

本模块提供[应用启动框架](../../guides/应用启动框架AppStartup.md)任务的相关能力。

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

#### 导入模块

```ets
import { StartupTask } from '@kit.AbilityKit';
```

#### StartupTask

该类提供启动任务的相关能力，使用[@Sendable装饰器](../../guides/Sendable对象简介.md#sendable装饰器)装饰。

**装饰器类型**：@Sendable

#### onDependencyCompleted

onDependencyCompleted?(dependency: string, result: Object): void

当依赖的启动任务执行完成时该方法将会被调用。

**系统能力**：SystemCapability.Ability.AppStartup

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| dependency | string | 是 | 依赖的启动任务名称。 |
| result | Object | 是 | 依赖的启动任务init返回的执行结果。 |

**示例：**

```ets
import { StartupTask, common } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

@Sendable
export default class StartupTask_001 extends StartupTask {
  constructor() {
    super();
  }

  async init(context: common.AbilityStageContext) {
    // ...
  }

  onDependencyCompleted(dependency: string, result: Object): void {
    hilog.info(0x0000, 'testTag', 'StartupTask_001 onDependencyCompleted, dependency: %{public}s, result: %{public}s',
      dependency, JSON.stringify(result));
    // ...
  }
```

#### init

init(context: [AbilityStageContext](../../topics/misc/AbilityStageContext.md)): Promise<Object | void>

当所有依赖的启动任务都执行完成后，该方法将会被调用。开发者可以在该回调中执行该启动任务的初始化操作。使用Promise异步回调。

**系统能力**：SystemCapability.Ability.AppStartup

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [AbilityStageContext](../../topics/misc/AbilityStageContext.md) | 是 | AbilityStage的上下文环境 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Object | void> | Promise对象，返回启动任务执行结果对象。 |

**示例：**

```ets
import { StartupTask, common } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

@Sendable
export default class StartupTask_001 extends StartupTask {
  constructor() {
    super();
  }
  async init(context: common.AbilityStageContext) {
    hilog.info(0x0000, 'testTag', 'StartupTask_001 init.');
    // ...

    return "StartupTask_001";
  }

  onDependencyCompleted(dependency: string, result: Object): void {
    // ...
  }
```