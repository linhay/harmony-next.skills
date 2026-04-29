# @ohos.app.ability.sendableContextManager (sendable上下文管理)

sendableContextManager模块提供Context与[SendableContext](SendableContext.md)相互转换的能力。


- 本模块首批接口从API version 12 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
- 本模块接口仅可在Stage模型下使用。

#### 使用场景

本模块主要用于ArkTS并发实例间（包括主线程、TaskPool&Worker工作线程）的数据传递。

例如，从主线程向子线程（如TaskPool或Worker工作线程）传递Sendable数据（符合[Sendable协议](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-sendable#sendable协议)的数据）时，需要通过Context与SendableContext之间的相互转换来实现。过程如下：

- 主线程向子线程传递Sendable数据时，需要将Context转换为[SendableContext](../../topics/misc/SendableContext.md)。
- 子线程使用Sendable数据时，需要将[SendableContext](../../topics/misc/SendableContext.md)转换为Context。

这里的Context与[createModuleContext](@ohos.app.ability.application (应用工具类).md#ZH-CN_TOPIC_0000002522240526__applicationcreatemodulecontext12)方法创建的Context不同，具体差异如下：

-

与SendableContext相互转换的Context：ArkTS并发实例持有的应用侧Context是不同的实例，底层对应同一个Context对象。当一个实例中Context属性和方法被修改时，相关实例中的Context属性和方法将会同步修改。其中，Context实例中的eventHub属性比较特殊，不同实例中的eventHub是独立的对象，不支持跨ArkTS实例使用。如果需要使用[EventHub](EventHub.md)跨实例传递数据，可以通过[setEventHubMultithreadingEnabled](#ZH-CN_TOPIC_0000002553360465__sendablecontextmanagerseteventhubmultithreadingenabled20)启用跨线程数据传递功能。

-

通过[createModuleContext](@ohos.app.ability.application (应用工具类).md#ZH-CN_TOPIC_0000002522240526__applicationcreatemodulecontext12)创建的Context：ArkTS并发实例持有的应用侧Context是不同的实例，底层对应不同的Context对象。

#### 约束限制

“Context转换为SendableContext”和“SendableContext转换为Context”两个环节中的Context类型必须保持一致。例如，主线程使用[convertFromContext](#ZH-CN_TOPIC_0000002553360465__sendablecontextmanagerconvertfromcontext)将[UIAbilityContext](UIAbilityContext.md)转换为SendableContext，子线程收到该SendableContext之后，需要通过[convertToUIAbilityContext](#ZH-CN_TOPIC_0000002553360465__sendablecontextmanagerconverttouiabilitycontext)将SendableContext转换为[UIAbilityContext](UIAbilityContext.md)。

目前支持转换的Context包括[Context](Context (Stage模型的上下文基类).md)、[ApplicationContext](ApplicationContext (应用上下文).md)、[AbilityStageContext](AbilityStageContext.md)、[UIAbilityContext](UIAbilityContext.md)。

#### 导入模块

```ets
import { sendableContextManager } from '@kit.AbilityKit';
```

#### [SendableContext](../../topics/misc/SendableContext.md)

type [SendableContext](../../topics/misc/SendableContext.md) = [_SendableContext](../../topics/misc/SendableContext.md)

Sendable上下文，符合[Sendable协议](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-sendable#sendable协议)，继承自[lang.ISendable](@arkts.lang (ArkTS语言基础能力).md#ZH-CN_TOPIC_0000002553200659__langisendable)。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

| 类型 | 说明 |
| --- | --- |
| _[SendableContext](../../topics/misc/SendableContext.md) | 表示Sendable上下文，可以与Context对象相互转换，用于ArkTS并发实例间（包括主线程、TaskPool&Worker工作线程）的数据传递。 |

#### sendableContextManager.convertFromContext

convertFromContext(context: common.Context): [SendableContext](../../topics/misc/SendableContext.md)

将Context转换为[SendableContext](../../topics/misc/SendableContext.md)对象。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | common.Context | 是 | Context对象。支持Context基类，ApplicationContext、AbilityStageContext和[UIAbilityContext](../../topics/misc/UIAbilityContext.md)子类。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [SendableContext](../../topics/misc/SendableContext.md) | SendableContext对象。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码]([通用错误码](../../errors/通用错误码.md).md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter invalid. Possible causes: 1.Incorrect parameter types; 2.Parameter verification failed. |

**示例：**

```ets
import { AbilityConstant, UIAbility, Want, sendableContextManager } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { worker } from '@kit.ArkTS';

@Sendable
export class SendableObject {
  constructor(sendableContext: sendableContextManager.SendableContext) {
    this.sendableContext = sendableContext;
  }

  sendableContext: sendableContextManager.SendableContext;
  // other sendable object
}

export default class EntryAbility extends UIAbility {
  worker: worker.ThreadWorker = new worker.ThreadWorker('entry/ets/workers/Worker.ets');

  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');

    // convert and post
    try {
      let sendableContext: sendableContextManager.SendableContext =
        sendableContextManager.convertFromContext(this.context);
      let object: SendableObject = new SendableObject(sendableContext);
      hilog.info(0x0000, 'testTag', '%{public}s', 'Ability post message');
      this.worker.postMessageWithSharedSendable(object);
    } catch (error) {
      hilog.error(0x0000, 'testTag', 'convertFromContext failed %{public}s', JSON.stringify(error));
    }
```

#### sendableContextManager.convertToContext

convertToContext(sendableContext: [SendableContext](../../topics/misc/SendableContext.md)): common.Context

将[SendableContext](../../topics/misc/SendableContext.md)对象转换为Context。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sendableContext | [SendableContext](../../topics/misc/SendableContext.md) | 是 | SendableContext对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| common.Context | Context对象。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter invalid. Possible causes: 1.Incorrect parameter types; 2.Parameter verification failed. |

**示例：**

主线程传递Context：

```ets
import { AbilityConstant, UIAbility, Want, common, sendableContextManager } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { worker } from '@kit.ArkTS';

@Sendable
export class SendableObject {
  constructor(sendableContext: sendableContextManager.SendableContext, contextName: string) {
    this.sendableContext = sendableContext;
    this.contextName = contextName;
  }

  sendableContext: sendableContextManager.SendableContext;
  contextName: string;
}

export default class EntryAbility extends UIAbility {
  worker: worker.ThreadWorker = new worker.ThreadWorker('entry/ets/workers/Worker.ets');

  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');

    // convert and post
    try {
      let context: common.Context = this.context as common.Context;
      let sendableContext: sendableContextManager.SendableContext = sendableContextManager.convertFromContext(context);
      let object: SendableObject = new SendableObject(sendableContext, 'BaseContext');
      hilog.info(0x0000, 'testTag', '%{public}s', 'Ability post message');
      this.worker.postMessageWithSharedSendable(object);
    } catch (error) {
      hilog.error(0x0000, 'testTag', 'convertFromContext failed %{public}s', JSON.stringify(error));
    }
```

Worker线程接收Context：

```ets
import { ErrorEvent, MessageEvents, ThreadWorkerGlobalScope, worker } from '@kit.ArkTS';
import { common, sendableContextManager } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

@Sendable
export class SendableObject {
  constructor(sendableContext: sendableContextManager.SendableContext, contextName: string) {
    this.sendableContext = sendableContext;
    this.contextName = contextName;
  }

  sendableContext: sendableContextManager.SendableContext;
  contextName: string;
}

const workerPort: ThreadWorkerGlobalScope = worker.workerPort;

workerPort.onmessage = (e: MessageEvents) => {
  let object: SendableObject = e.data;
  let sendableContext: sendableContextManager.SendableContext = object.sendableContext;
  if (object.contextName == 'BaseContext') {
    hilog.info(0x0000, 'testTag', '%{public}s', 'convert to context.');
    try {
      let context: common.Context = sendableContextManager.convertToContext(sendableContext);
      // 获取context后获取沙箱路径
      hilog.info(0x0000, 'testTag', 'worker context.databaseDir: %{public}s', context.databaseDir);
    } catch (error) {
      hilog.error(0x0000, 'testTag', 'convertToContext failed %{public}s', JSON.stringify(error));
    }

workerPort.onmessageerror = (e: MessageEvents) => {
  hilog.info(0x0000, 'testTag', '%{public}s', 'onmessageerror');
}

workerPort.onerror = (e: ErrorEvent) => {
  hilog.info(0x0000, 'testTag', '%{public}s', 'onerror');
}
```

#### sendableContextManager.convertToApplicationContext

convertToApplicationContext(sendableContext: [SendableContext](../../topics/misc/SendableContext.md)): common.ApplicationContext

将[SendableContext](../../topics/misc/SendableContext.md)对象转换为ApplicationContext。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sendableContext | [SendableContext](../../topics/misc/SendableContext.md) | 是 | SendableContext对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| common.ApplicationContext | ApplicationContext对象。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter invalid. Possible causes: 1.Incorrect parameter types; 2.Parameter verification failed. |

**示例：**

主线程传递Context：

```ets
import { AbilityConstant, UIAbility, Want, common, sendableContextManager } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { worker } from '@kit.ArkTS';

@Sendable
export class SendableObject {
  constructor(sendableContext: sendableContextManager.SendableContext, contextName: string) {
    this.sendableContext = sendableContext;
    this.contextName = contextName;
  }

  sendableContext: sendableContextManager.SendableContext;
  contextName: string;
}

export default class EntryAbility extends UIAbility {
  worker: worker.ThreadWorker = new worker.ThreadWorker('entry/ets/workers/Worker.ets');

  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');

    // convert and post
    try {
      let context: common.Context = this.context as common.Context;
      let applicationContext = context.getApplicationContext();
      let sendableContext: sendableContextManager.SendableContext =
        sendableContextManager.convertFromContext(applicationContext);
      let object: SendableObject = new SendableObject(sendableContext, 'ApplicationContext');
      hilog.info(0x0000, 'testTag', '%{public}s', 'Ability post message');
      this.worker.postMessageWithSharedSendable(object);
    } catch (error) {
      hilog.error(0x0000, 'testTag', 'convertFromContext failed %{public}s', JSON.stringify(error));
    }
```

Worker线程接收Context：

```ets
import { ErrorEvent, MessageEvents, ThreadWorkerGlobalScope, worker } from '@kit.ArkTS';
import { common, sendableContextManager } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

@Sendable
export class SendableObject {
  constructor(sendableContext: sendableContextManager.SendableContext, contextName: string) {
    this.sendableContext = sendableContext;
    this.contextName = contextName;
  }

  sendableContext: sendableContextManager.SendableContext;
  contextName: string;
}

const workerPort: ThreadWorkerGlobalScope = worker.workerPort;

workerPort.onmessage = (e: MessageEvents) => {
  let object: SendableObject = e.data;
  let sendableContext: sendableContextManager.SendableContext = object.sendableContext;
  if (object.contextName == 'ApplicationContext') {
    hilog.info(0x0000, 'testTag', '%{public}s', 'convert to application context.');
    try {
      let context: common.ApplicationContext = sendableContextManager.convertToApplicationContext(sendableContext);
      // 获取context后获取沙箱路径
      hilog.info(0x0000, 'testTag', 'worker context.databaseDir: %{public}s', context.databaseDir);
    } catch (error) {
      hilog.error(0x0000, 'testTag', 'convertToApplicationContext failed %{public}s', JSON.stringify(error));
    }

workerPort.onmessageerror = (e: MessageEvents) => {
  hilog.info(0x0000, 'testTag', '%{public}s', 'onmessageerror');
}

workerPort.onerror = (e: ErrorEvent) => {
  hilog.info(0x0000, 'testTag', '%{public}s', 'onerror');
}
```

#### sendableContextManager.convertTo[AbilityStageContext](../../topics/misc/AbilityStageContext.md)

convertToAbilityStageContext(sendableContext: [SendableContext](../../topics/misc/SendableContext.md)): common.AbilityStageContext

将[SendableContext](../../topics/misc/SendableContext.md)对象转换为AbilityStageContext。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sendableContext | [SendableContext](../../topics/misc/SendableContext.md) | 是 | SendableContext对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| common.[AbilityStageContext](../../topics/misc/AbilityStageContext.md) | AbilityStageContext对象。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter invalid. Possible causes: 1.Incorrect parameter types; 2.Parameter verification failed. |

**示例：**

主线程传递Context：

```ets
import { UIAbility, sendableContextManager } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { worker } from '@kit.ArkTS';

@Sendable
export class SendableObject {
  constructor(sendableContext: sendableContextManager.SendableContext, contextName: string) {
    this.sendableContext = sendableContext;
    this.contextName = contextName;
  }

  sendableContext: sendableContextManager.SendableContext;
  contextName: string;
}

export default class EntryAbility extends UIAbility {
  worker: worker.ThreadWorker = new worker.ThreadWorker('entry/ets/workers/Worker.ets');

  onCreate(): void {
    hilog.info(0x0000, 'testTag', '%{public}s', 'AbilityStage onCreate');

    // convert and post
    try {
      let sendableContext: sendableContextManager.SendableContext =
        sendableContextManager.convertFromContext(this.context);
      let object: SendableObject = new SendableObject(sendableContext, 'AbilityStageContext');
      hilog.info(0x0000, 'testTag', '%{public}s', 'AbilityStage post message');
      this.worker.postMessageWithSharedSendable(object);
    } catch (error) {
      hilog.error(0x0000, 'testTag', 'convertFromContext failed %{public}s', JSON.stringify(error));
    }
```

Worker线程接收Context：

```ets
import { ErrorEvent, MessageEvents, ThreadWorkerGlobalScope, worker } from '@kit.ArkTS';
import { common, sendableContextManager } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

@Sendable
export class SendableObject {
  constructor(sendableContext: sendableContextManager.SendableContext, contextName: string) {
    this.sendableContext = sendableContext;
    this.contextName = contextName;
  }

  sendableContext: sendableContextManager.SendableContext;
  contextName: string;
}

const workerPort: ThreadWorkerGlobalScope = worker.workerPort;

workerPort.onmessage = (e: MessageEvents) => {
  let object: SendableObject = e.data;
  let sendableContext: sendableContextManager.SendableContext = object.sendableContext;
  if (object.contextName == 'AbilityStageContext') {
    hilog.info(0x0000, 'testTag', '%{public}s', 'convert to abilitystage context.');
    try {
      let context: common.AbilityStageContext = sendableContextManager.convertToAbilityStageContext(sendableContext);
      // 获取context后获取沙箱路径
      hilog.info(0x0000, 'testTag', 'worker context.databaseDir: %{public}s', context.databaseDir);
    } catch (error) {
      hilog.error(0x0000, 'testTag', 'convertToAbilityStageContext failed %{public}s', JSON.stringify(error));
    }

workerPort.onmessageerror = (e: MessageEvents) => {
  hilog.info(0x0000, 'testTag', '%{public}s', 'onmessageerror');
}

workerPort.onerror = (e: ErrorEvent) => {
  hilog.info(0x0000, 'testTag', '%{public}s', 'onerror');
}
```

#### sendableContextManager.convertTo[UIAbilityContext](../../topics/misc/UIAbilityContext.md)

convertToUIAbilityContext(sendableContext: [SendableContext](../../topics/misc/SendableContext.md)): common.UIAbilityContext

将[SendableContext](../../topics/misc/SendableContext.md)对象转换为UIAbilityContext。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sendableContext | [SendableContext](../../topics/misc/SendableContext.md) | 是 | SendableContext对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| common.[UIAbilityContext](../../topics/misc/UIAbilityContext.md) | UIAbilityContext对象。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter invalid. Possible causes: 1.Incorrect parameter types; 2.Parameter verification failed. |

**示例：**

主线程传递Context：

```ets
import { AbilityConstant, UIAbility, Want, common, sendableContextManager } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { worker } from '@kit.ArkTS';

@Sendable
export class SendableObject {
  constructor(sendableContext: sendableContextManager.SendableContext, contextName: string) {
    this.sendableContext = sendableContext;
    this.contextName = contextName;
  }

  sendableContext: sendableContextManager.SendableContext;
  contextName: string;
}

export default class EntryAbility extends UIAbility {
  worker: worker.ThreadWorker = new worker.ThreadWorker('entry/ets/workers/Worker.ets');

  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');

    // convert and post
    try {
      let sendableContext: sendableContextManager.SendableContext =
        sendableContextManager.convertFromContext(this.context);
      let object: SendableObject = new SendableObject(sendableContext, 'EntryAbilityContext');
      hilog.info(0x0000, 'testTag', '%{public}s', 'Ability post message');
      this.worker.postMessageWithSharedSendable(object);
    } catch (error) {
      hilog.error(0x0000, 'testTag', 'convertFromContext failed %{public}s', JSON.stringify(error));
    }
```

Worker线程接收Context：

```ets
import { ErrorEvent, MessageEvents, ThreadWorkerGlobalScope, worker } from '@kit.ArkTS';
import { common, sendableContextManager } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

@Sendable
export class SendableObject {
  constructor(sendableContext: sendableContextManager.SendableContext, contextName: string) {
    this.sendableContext = sendableContext;
    this.contextName = contextName;
  }

  sendableContext: sendableContextManager.SendableContext;
  contextName: string;
}

const workerPort: ThreadWorkerGlobalScope = worker.workerPort;

workerPort.onmessage = (e: MessageEvents) => {
  let object: SendableObject = e.data;
  let sendableContext: sendableContextManager.SendableContext = object.sendableContext;
  if (object.contextName == 'EntryAbilityContext') {
    hilog.info(0x0000, 'testTag', '%{public}s', 'convert to UIAbility context.');
    try {
      let context: common.UIAbilityContext = sendableContextManager.convertToUIAbilityContext(sendableContext);
      // 获取context后获取沙箱路径
      hilog.info(0x0000, 'testTag', 'worker context.databaseDir: %{public}s', context.databaseDir);
    } catch (error) {
      hilog.error(0x0000, 'testTag', 'convertToUIAbilityContext failed %{public}s', JSON.stringify(error));
}

workerPort.onmessageerror = (e: MessageEvents) => {
  hilog.info(0x0000, 'testTag', '%{public}s', 'onmessageerror');
}

workerPort.onerror = (e: ErrorEvent) => {
  hilog.info(0x0000, 'testTag', '%{public}s', 'onerror');
}
```

#### sendableContextManager.set[EventHub](../../topics/misc/EventHub.md)MultithreadingEnabled20+

set[EventHub](../../topics/misc/EventHub.md)MultithreadingEnabled(context: common.Context, enabled: boolean): void

设置[Context](Context (Stage模型的上下文基类).md)中的[EventHub](EventHub.md)是否启用跨线程通信能力。


- 当多个Context进行通信时，需要调用该接口设置每个Context都支持[EventHub](../../topics/misc/EventHub.md)跨线程数据传递功能。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | common.Context | 是 | Context对象。其中，Eventhub支持传递的序列化数据类型参见[序列化支持的类型](@ohos.taskpool（启动任务池）.md#ZH-CN_TOPIC_0000002497444774__序列化支持类型)，数据大小不超过16MB。 |
| enabled | boolean | 是 | 表示是否启用Context的[EventHub](../../topics/misc/EventHub.md)跨线程通信能力。 - true：表示启用跨线程通信能力，数据将通过引用的方式传递。 - false：表示禁用跨线程通信能力，数据将通过序列化的方式传递，即发送端线程与接收端线程的数据相互独立。 |

**示例：**

主线程启用[Context](Context (Stage模型的上下文基类).md)中[EventHub](EventHub.md)的跨线程通信能力，并将Context转换为[SendableContext](SendableContext.md)后发送到[Worker](@ohos.worker (启动一个Worker).md)线程。

```ets
import { common, sendableContextManager } from '@kit.AbilityKit';
import { worker } from '@kit.ArkTS';
import { hilog } from '@kit.PerformanceAnalysisKit';

const DOMAIN = 0x0000;

@Sendable
export class SendableObject {
  constructor(sendableContext: sendableContextManager.SendableContext, contextName: string) {
    this.sendableContext = sendableContext;
    this.contextName = contextName;
  }

  sendableContext: sendableContextManager.SendableContext;
  contextName: string;
}

@Entry
@Component
struct Index {
  @State context: common.Context | undefined = this.getUIContext().getHostContext();
  worker1: worker.ThreadWorker = new worker.ThreadWorker('entry/ets/workers/Worker.ets');

  aboutToAppear(): void {
    let context: common.Context = this.context as common.Context;
    context.eventHub.on('event1', this.eventFunc);
    context.eventHub.emit('event1', 'xingming', 22);
  }

  eventFunc(name: string, age: number) {
    hilog.info(DOMAIN, 'testTag', 'name %{public}s age %{public}d', name, age);
  }

  build() {
    Column() {
      Row() {
        Button('thread 1')
          .size({ width: 100, height: 100 })
          .onClick(() => {
            if (this.context == undefined) {
              return;
            }
            sendableContextManager.setEventHubMultithreadingEnabled(this.context, true);
            let sendableContext: sendableContextManager.SendableContext =
              sendableContextManager.convertFromContext(this.context);
            let object: SendableObject = new SendableObject(sendableContext, 'BaseContext');
            this.worker1.postMessageWithSharedSendable(object);
          })
      }
```

[Worker](@ohos.worker (启动一个Worker).md)线程接收到[SendableContext](SendableContext.md)后，将其转换为[Context](Context (Stage模型的上下文基类).md)。然后，在Worker线程内，启用Context中[EventHub](EventHub.md)的跨线程通信能力，并通过该功能向主线程发送消息。

```ets
import { ErrorEvent, MessageEvents, ThreadWorkerGlobalScope, worker } from '@kit.ArkTS';
import { common, sendableContextManager } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const DOMAIN = 0x0000;

@Sendable
export class SendableObject {
  constructor(sendableContext: sendableContextManager.SendableContext, contextName: string) {
    this.sendableContext = sendableContext;
    this.contextName = contextName;
  }

  sendableContext: sendableContextManager.SendableContext;
  contextName: string;
}

const workerPort: ThreadWorkerGlobalScope = worker.workerPort;

workerPort.onmessage = (e: MessageEvents) => {
  let object: SendableObject = e.data;
  let sendableContext: sendableContextManager.SendableContext = object.sendableContext;
  if (object.contextName == 'BaseContext') {
    let context: common.Context = sendableContextManager.convertToContext(sendableContext);
    sendableContextManager.setEventHubMultithreadingEnabled(context, true);
    context.eventHub.emit('event1', 'xingming', 40);
  }
};

workerPort.onmessageerror = (e: MessageEvents) => {
  hilog.error(DOMAIN, 'testTag', '%{public}s', 'onmessageerror');
};

workerPort.onerror = (e: ErrorEvent) => {
  hilog.error(DOMAIN, 'testTag', '%{public}s', 'onerror');
};
```