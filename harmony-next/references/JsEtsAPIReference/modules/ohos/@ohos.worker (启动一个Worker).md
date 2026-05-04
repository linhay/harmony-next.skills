# @ohos.worker (启动一个Worker)

Worker是与主线程并行的独立线程。创建Worker的线程称为宿主线程，Worker自身的线程称为Worker线程。创建Worker时传入的URL文件在Worker线程中执行，可以处理耗时操作，但不能直接操作UI。

Worker的主要作用是为应用程序提供多线程运行环境，使应用程序在执行过程中与宿主线程分离，在后台线程中运行脚本处理耗时操作，避免计算密集型或高延迟任务阻塞宿主线程。由于Worker一旦创建不会主动销毁，若不处于任务状态会一直运行，造成资源浪费，应及时销毁空闲的Worker。

Worker的上下文环境和UI线程的上下文环境是独立的，Worker线程不支持UI操作。

请查看[Worker注意事项](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/worker-introduction)，了解Worker使用过程中的相关注意点。


本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { worker } from '@kit.ArkTS';
```

#### 属性

**系统能力：** SystemCapability.Utils.Lang

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| workerPort9+ | ThreadWorkerGlobalScope | 否 | 否 | Worker线程用于与宿主线程通信的对象。 元服务API：从API version 11开始，该接口支持在元服务中使用。 |
| parentPort(deprecated) | DedicatedWorkerGlobalScope | 否 | 否 | Worker线程用于与宿主线程通信的对象。 此属性从API version 7开始支持，从API version 9开始被废弃。 建议使用workerPort9+替代。 |

#### WorkerOptions

Worker构造函数的选项，用于为Worker添加其他信息。

**系统能力：** SystemCapability.Utils.Lang

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | 'classic' | 'module' | 否 | 是 | Worker执行脚本的模式类型，暂不支持module类型，默认值为"classic"。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| name | string | 否 | 是 | Worker的名称，默认值为undefined。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| shared | boolean | 否 | 是 | 表示Worker共享功能，此接口暂不支持。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| priority18+ | ThreadWorkerPriority | 否 | 是 | 表示Worker线程优先级。默认值为MEDIUM。 元服务API： 从API version 18开始，该接口支持在元服务中使用。 |

#### ThreadWorkerPriority18+

Worker线程的优先级枚举，各优先级对应关系请参考[QoS等级定义](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/qos-guidelines#qos等级定义)。

**系统能力：** SystemCapability.Utils.Lang

| 名称 | 值 | 说明 |
| --- | --- | --- |
| HIGH | 0 | 适用于打开文档等用户触发并且可以看到进展的任务，任务在几秒钟之内完成。对应QOS_USER_INITIATED。 元服务API：从API version 18开始，该接口支持在元服务中使用。 |
| MEDIUM | 1 | 任务完成需要几秒钟。是ThreadWorkerPriority的默认值。对应QOS_DEFAULT。 元服务API：从API version 18开始，该接口支持在元服务中使用。 |
| LOW | 2 | 适用于下载等不需要立即看到响应效果的任务，任务完成需要几秒到几分钟。对应QOS_UTILITY。 元服务API：从API version 18开始，该接口支持在元服务中使用。 |
| IDLE | 3 | 适用于数据同步等用户不可见的后台任务，任务完成需要几分钟甚至几小时。对应QOS_BACKGROUND。 元服务API：从API version 18开始，该接口支持在元服务中使用。 |
| DEADLINE20+ | 4 | 适用于页面加载等越快越好的关键任务，任务几乎是瞬间完成的。对应QOS_DEADLINE_REQUEST。 元服务API：从API version 20开始，该接口支持在元服务中使用。 |
| VIP20+ | 5 | 适用于UI线程、动画渲染等用户交互任务，任务是即时的。对应QOS_USER_INTERACTIVE。 元服务API：从API version 20开始，该接口支持在元服务中使用。 |

#### ThreadWorker9+

使用以下方法前，需先构造ThreadWorker实例。ThreadWorker类继承自[WorkerEventTarget](#ZH-CN_TOPIC_0000002522240710__workereventtarget9)。

#### 属性

**系统能力：** SystemCapability.Utils.Lang

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| onexit9+ | (code: number) => void | 否 | 是 | 回调函数。表示Worker线程销毁时被调用的事件处理程序，该处理程序在宿主线程中执行。回调函数的code参数类型为number，异常退出时code为1，正常退出时code为0。默认值为undefined。 元服务API：从API version 11开始，该属性支持在元服务中使用。 |
| onerror9+ | (err: ErrorEvent) => void | 否 | 是 | 回调函数，用于处理onmessage回调函数中同步代码产生的异常，处理程序在宿主线程中执行。回调函数的err类型为ErrorEvent，表示收到的异常数据。默认值为undefined。 元服务API：从API version 11开始，该属性支持在元服务中使用。 |
| onAllErrors18+ | ErrorCallback | 否 | 是 | 回调函数。表示Worker线程生命周期内发生异常被调用的事件处理程序，处理程序在宿主线程中执行。 元服务API：从API version 18开始，该属性支持在元服务中使用。 |
| onmessage9+ | (event: MessageEvents) => void | 否 | 是 | 回调函数。表示宿主线程接收到来自其创建的Worker通过workerPort.postMessage或workerPort.postMessageWithSharedSendable接口发送的消息时被调用的事件处理程序，处理程序在宿主线程中执行。其中回调函数中event类型为MessageEvents，表示收到的Worker线程发送的消息数据。默认值为undefined。 元服务API：从API version 11开始，该属性支持在元服务中使用。 |
| onmessageerror9+ | (event: MessageEvents) => void | 否 | 是 | 回调函数。用于处理Worker对象接收到的无法被序列化的消息。该处理程序在宿主线程中执行，event类型为MessageEvents，表示收到的Worker消息数据。默认值为undefined。 元服务API：从API version 11开始，该属性支持在元服务中使用。 |

使用Worker模块时，API version 18及之后的版本建议在宿主线程中注册onAllErrors回调，以捕获Worker线程生命周期内的各种异常。API version 18之前的版本应注册onerror回调。如果未注册onAllErrors或onerror回调，当Worker线程出现异常时会发生jscrash问题。注意，onerror接口仅能捕获onmessage回调中的同步异常，捕获异常后，Worker线程将进入销毁流程，无法继续使用。

onAllErrors接口与onerror接口之间的行为差异如下：

1.

异常捕获范围

onAllErrors接口可以捕获Worker线程的onmessage回调、timer回调以及文件执行等流程中产生的全局异常。

onerror接口仅能捕获Worker线程的onmessage回调中同步方法产生的异常，无法捕获多线程回调和模块化相关异常。

1.

异常捕获后的线程状态

onAllErrors接口捕获异常后，Worker线程仍然存活并可以继续使用。这使开发者可以在捕获异常后执行其他操作，无需担心线程终止。

onerror接口捕获异常后，Worker线程会进入销毁流程，无法继续使用。这意味着在onerror触发后，Worker线程将被终止，后续操作将无法进行。

1.

适用场景

onAllErrors接口适用于捕获Worker线程中所有类型异常的场景，特别是确保异常发生后Worker线程仍能继续运行的复杂场景。

onerror接口适用于只需要捕获onmessage回调中同步异常的简单场景。由于捕获异常后线程会被销毁，适用于不需要继续使用Worker线程的情况。

推荐使用onAllErrors接口，因为它提供了更全面的异常捕获能力，并且不会导致线程终止。

#### constructor9+

constructor(scriptURL: string, options?: WorkerOptions)

ThreadWorker构造函数。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scriptURL | string | 是 | Worker线程文件的路径。 路径规则详细参考文件路径注意事项。 |
| options | WorkerOptions | 否 | Worker构造的选项。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码]([通用错误码](../../errors/通用错误码.md).md)和[语言基础类库错误码]([语言基础类库错误码](../../errors/语言基础类库错误码.md).md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 10200003 | Worker initialization failed. |
| 10200007 | The worker file path is invalid. |

**示例：**

以下示例展示了在Stage模型的entry模块Index.ets文件中加载Worker文件的方法，使用Library加载Worker线程文件的场景参考[文件路径注意事项](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/worker-introduction#文件路径注意事项)。

```ets
// Index.ets
import { worker } from '@kit.ArkTS';

// worker文件所在路径："entry/src/main/ets/workers/worker.ets"
const workerInstance = new worker.ThreadWorker('entry/ets/workers/worker.ets', {name: "WorkerThread"});
```

#### postMessage9+

postMessage(message: Object, transfer: ArrayBuffer[]): void

宿主线程通过转移对象所有权的方式向Worker线程发送消息。

**系统能力：** SystemCapability.Utils.Lang

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| message | Object | 是 | 发送至Worker的数据，该数据对象必须是可序列化对象，序列化支持类型见其他说明。 |
| transfer | ArrayBuffer[] | 是 | 表示可转移的ArrayBuffer实例对象数组，该数组中对象的所有权会被转移到Worker线程，在宿主线程中将会变为不可用，仅在Worker线程中可用，数组不可传入null。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[语言基础类库错误码](语言基础类库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 10200004 | The Worker instance is not running. |
| 10200006 | An exception occurred during serialization. |

**示例：**

```ets
// Worker.ets
import { worker, MessageEvents, ErrorEvent } from '@kit.ArkTS';

// 创建worker线程中与宿主线程通信的对象
const workerPort = worker.workerPort;

// worker线程接收宿主线程信息
workerPort.onmessage = (e: MessageEvents): void => {
  // data：宿主线程发送的信息
  let data: ArrayBuffer = e.data;
  // 往收到的buffer里写入数据
  const view = new Int8Array(data).fill(3);
  // worker线程向宿主线程发送信息
  workerPort.postMessage(view);
}

// worker线程发生error的回调
workerPort.onerror = (err: ErrorEvent) => {
  console.error("worker.ets onerror" + err.message);
}
```

```ets
// Index.ets
import { worker, MessageEvents, ErrorEvent } from '@kit.ArkTS';

@Entry
@Component
struct Index {
  @State message: string = 'Hello World';

  build() {
    Row() {
      Column() {
        Text(this.message)
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
          .onClick(() => {
            // 宿主线程中创建Worker对象
            const workerInstance = new worker.ThreadWorker("entry/ets/workers/Worker.ets");
            // 宿主线程向worker线程传递信息
            const buffer = new ArrayBuffer(8);
            workerInstance.postMessage(buffer, [buffer]);

            // 此时buffer的所有权转移到了worker线程，在宿主线程中不可用
            // const view = new Int8Array(buffer).fill(3);

            // 宿主线程接收worker线程信息
            workerInstance.onmessage = (e: MessageEvents): void => {
              // data：worker线程发送的信息
              let data: Int8Array = e.data;
              console.info("main thread data is  " + data);
              // 销毁Worker对象
              workerInstance.terminate();
            }
            // 在调用terminate后，执行onexit
            workerInstance.onexit = (code) => {
              console.info("main thread terminate");
            }
            // 监听Worker错误
            workerInstance.onAllErrors = (err: ErrorEvent) => {
              console.error("main error message " + err.message);
            }
          })
      }
      .width('100%')
      .height('100%')
    }
```

#### postMessage9+

postMessage(message: Object, options?: PostMessageOptions): void

宿主线程可以通过转移对象所有权或拷贝数据的方式向Worker线程发送消息。在传递[Sendable对象](../../guides/Sendable对象简介.md)时，使用拷贝数据的方式。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| message | Object | 是 | 发送至Worker的数据，该数据对象必须是可序列化对象，序列化支持类型见其他说明。 |
| options | PostMessageOptions | 否 | 当填入该参数时，传输的数据将通过所有权转移的方式发送到Worker线程。这些数据在宿主线程中将变为不可用，仅在Worker线程中可用。 若不填入该参数，默认设置为 undefined，数据将通过拷贝的方式传输到Worker线程。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[语言基础类库错误码](语言基础类库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 10200004 | The Worker instance is not running. |
| 10200006 | An exception occurred during serialization. |

**示例：**

```ets
import { worker } from '@kit.ArkTS';

const workerInstance = new worker.ThreadWorker("entry/ets/workers/worker.ets");

workerInstance.postMessage("hello world");

let buffer = new ArrayBuffer(8);

// 填入options参数，buffer的所有权会转移到Worker线程，在宿主线程中将不可用
workerInstance.postMessage(buffer, [buffer]);

// 未填入options参数，默认值为undefined，通过拷贝数据的方式将buffer发送到Worker线程
workerInstance.postMessage(buffer);
```

#### postMessageWithSharedSendable12+

postMessageWithSharedSendable(message: Object, transfer?: ArrayBuffer[]): void

宿主线程向Worker线程发送消息，消息中的[Sendable对象](../../guides/Sendable对象简介.md)通过引用传递，非Sendable对象通过拷贝数据的方式传递。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| message | Object | 是 | 发送至Worker的数据，该数据对象必须是可序列化对象，序列化支持类型见序列化类型说明。如果需要共享数据，支持类型见Sendable支持的数据类型。 |
| transfer | ArrayBuffer[] | 否 | 可转移的ArrayBuffer实例对象数组。该数组中对象的所有权将转移到Worker线程，在宿主线程中变为不可用，仅在Worker线程中可用，数组不可传入null。默认值为空数组。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[语言基础类库错误码](语言基础类库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 10200004 | The Worker instance is not running. |
| 10200006 | An exception occurred during serialization. |

**示例：**

```ets
// Index.ets
// 新建SendableObject实例并通过宿主线程传递至Worker线程

import { worker } from '@kit.ArkTS';
import { SendableObject } from './sendable';

const workerInstance = new worker.ThreadWorker("entry/ets/workers/Worker.ets");
let object: SendableObject = new SendableObject();
workerInstance.postMessageWithSharedSendable(object);

// 使用postMessage接口传递Sendable对象，使用拷贝数据的方式传递
workerInstance.postMessage(object);
```

```ets
// sendable.ets
// 定义SendableObject

@Sendable
export class SendableObject {
  a:number = 45;
}
```

```ets
// worker文件路径为：entry/src/main/ets/workers/Worker.ets
// Worker.ets
// 接收宿主线程传递至Worker线程的数据并访问

import { SendableObject } from '../pages/sendable';
import { worker, ThreadWorkerGlobalScope, MessageEvents, ErrorEvent } from '@kit.ArkTS';

const workerPort: ThreadWorkerGlobalScope = worker.workerPort;

workerPort.onmessage = (e: MessageEvents) => {
  let obj: SendableObject = e.data;
  console.info("sendable obj is: " + obj.a);
}
```

#### on9+

on(type: string, listener: WorkerEventListener): void

向宿主线程的Worker实例对象添加一个事件监听，该接口与[addEventListener9+](#ZH-CN_TOPIC_0000002522240710__addeventlistener9)接口功能一致。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听的事件类型。 |
| listener | WorkerEventListener | 是 | 回调的事件。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[语言基础类库错误码](语言基础类库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 10200004 | Worker instance is not running. |
| 10200005 | The invoked API is not supported in workers. |

**示例：**

```ets
// Index.ets
import { worker } from '@kit.ArkTS';

const workerInstance = new worker.ThreadWorker("entry/ets/workers/worker.ets");

workerInstance.on("alert", () => {
    console.info("alert listener callback");
})

// 使用on添加的事件监听可以多次执行
workerInstance.dispatchEvent({type: "alert", timeStamp: 0}); // timeStamp暂未支持
```

#### once9+

once(type: string, listener: WorkerEventListener): void

向宿主线程的Worker实例对象添加一个事件监听，该事件监听只执行一次，执行完后会自动删除。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听的事件类型。 |
| listener | WorkerEventListener | 是 | 回调的事件。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[语言基础类库错误码](语言基础类库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 10200004 | Worker instance is not running. |
| 10200005 | The invoked API is not supported in workers. |

**示例：**

```ets
// Index.ets
import { worker } from '@kit.ArkTS';

const workerInstance = new worker.ThreadWorker("entry/ets/workers/worker.ets");

workerInstance.once("alert", () => {
  console.info("alert listener callback");
})

workerInstance.dispatchEvent({type: "alert", timeStamp: 0}); // timeStamp暂未支持

// 使用once添加的事件监听在执行一次后自动删除，无法多次执行
// workerInstance.dispatchEvent({type: "alert", timeStamp: 0}); // timeStamp暂未支持
```

#### off9+

off(type: string, listener?: WorkerEventListener): void

移除宿主线程的Worker实例对象中类型为type的事件监听，该接口与[removeEventListener9+](#ZH-CN_TOPIC_0000002522240710__removeeventlistener9)接口功能一致。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 需要删除的事件类型。 |
| listener | WorkerEventListener | 否 | 需要删除的特定监听器回调函数。如果未传入此参数，则会删除该类型的所有监听器。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[语言基础类库错误码](语言基础类库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 10200004 | Worker instance is not running. |
| 10200005 | The invoked API is not supported in workers. |

**示例：**

```ets
// Index.ets
import { worker } from '@kit.ArkTS';

const workerInstance = new worker.ThreadWorker("entry/ets/workers/worker.ets");

const handler1 = () => console.info("Handler 1");
const handler2 = () => console.info("Handler 2");

// 注册两个监听器
workerInstance.on("alert", handler1);
workerInstance.on("alert", handler2);

// 首次触发：两个监听器都会执行
workerInstance.dispatchEvent({type: "alert", timeStamp: 0}); // timeStamp暂未支持

// 删除 handler1 监听器
workerInstance.off("alert", handler1);

// 再次触发：只剩 handler2 会执行
workerInstance.dispatchEvent({type: "alert", timeStamp: 0}); // timeStamp暂未支持

// 删除"alert"类型所有监听器
workerInstance.off("alert");
```

#### registerGlobalCallObject11+

registerGlobalCallObject(instanceName: string, globalCallObject: Object): void

在宿主线程的ThreadWorker实例上注册一个对象，该对象的方法可在Worker线程中调用。详情请参见[callGlobalCallObjectMethod](#ZH-CN_TOPIC_0000002522240710__callglobalcallobjectmethod11)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| instanceName | string | 是 | 注册对象时使用的键，调用时通过该键值找到被注册的对象。 |
| globalCallObject | Object | 是 | 被注册的对象，ThreadWorker实例会持有被注册对象的强引用。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[语言基础类库错误码](语言基础类库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 10200004 | Worker instance is not running. |

**示例：**

```ets
//Index.ets
import { worker } from '@kit.ArkTS';

const workerInstance = new worker.ThreadWorker("entry/ets/workers/worker.ets");
class TestObj {
  private message : string = "this is a message from TestObj";
  public getMessage() : string {
    return this.message;
  }
  public getMessageWithInput(str : string) : string {
    return this.message + " with input: " + str;
}
let registerObj = new TestObj();
// 在ThreadWorker实例上注册registerObj
workerInstance.registerGlobalCallObject("myObj", registerObj);
workerInstance.postMessage("start worker");
```

```ets
// worker.ets
import { worker, MessageEvents } from '@kit.ArkTS';

const workerPort = worker.workerPort;
workerPort.onmessage = (e: MessageEvents): void => {
  try {
    // 调用方法无入参
    let res : string = workerPort.callGlobalCallObjectMethod("myObj", "getMessage", 0) as string;
    console.info("worker:", res) // worker: this is a message from TestObj
  } catch (error) {
    // 异常处理
    console.error("worker: error code is " + error.code + " error message is " + error.message);
  }
  try {
    // 调用方法有入参
    let res : string = workerPort.callGlobalCallObjectMethod("myObj", "getMessageWithInput", 0, "hello there!") as string;
    console.info("worker:", res); //worker: this is a message from TestObj with input: hello there!
  } catch (error) {
    // 异常处理
    console.error("worker: error code is " + error.code + " error message is " + error.message);
  }
```

#### unregisterGlobalCallObject11+

unregisterGlobalCallObject(instanceName?: string): void

取消在宿主线程ThreadWorker实例上注册的对象，该方法会释放ThreadWorker实例中与该键相匹配的对象的强引用。如果无匹配对象，该方法不会报错。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| instanceName | string | 否 | 注册对象时使用的键。此参数不填时，会释放ThreadWorker实例中所有已注册的对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[语言基础类库错误码](语言基础类库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 10200004 | Worker instance is not running. |

**示例：**

```ets
// Index.ets
import { worker } from '@kit.ArkTS';

const workerInstance = new worker.ThreadWorker("entry/ets/workers/worker.ets");
class TestObj {
  private message : string = "this is a message from TestObj";
  public getMessage() : string {
    return this.message;
  }
  public getMessageWithInput(str : string) : string {
    return this.message + " with input: " + str;
}
let registerObj = new TestObj();
workerInstance.registerGlobalCallObject("myObj", registerObj);
// 取消对象注册
workerInstance.unregisterGlobalCallObject("myObj");
// 取消ThreadWorker实例上的所有对象注册
//workerInstance.unregisterGlobalCallObject();
workerInstance.postMessage("start worker");
```

#### terminate9+

terminate(): void

销毁Worker线程并停止Worker线程接收消息。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](语言基础类库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200004 | The Worker instance is not running. |

**示例：**

```ets
// Index.ets
import { worker } from '@kit.ArkTS';

const workerInstance = new worker.ThreadWorker("entry/ets/workers/worker.ets");
workerInstance.terminate();
```

#### addEventListener9+

addEventListener(type: string, listener: WorkerEventListener): void

向宿主线程的Worker实例对象添加一个事件监听，该接口与[on9+](#ZH-CN_TOPIC_0000002522240710__on9)接口功能一致。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听的事件类型。 |
| listener | WorkerEventListener | 是 | 回调的事件。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[语言基础类库错误码](语言基础类库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 10200004 | Worker instance is not running. |
| 10200005 | The invoked API is not supported in workers. |

**示例：**

```ets
// Index.ets
import { worker } from '@kit.ArkTS';

const workerInstance = new worker.ThreadWorker("entry/ets/workers/worker.ets");

workerInstance.addEventListener("alert", () => {
  console.info("alert listener callback");
})

// 执行 alert 事件类型的回调
workerInstance.dispatchEvent({type: "alert", timeStamp: 0}); // timeStamp暂未支持
```

#### removeEventListener9+

removeEventListener(type: string, callback?: WorkerEventListener): void

移除宿主线程的Worker实例对象中类型为type的事件监听，该接口与[off9+](#ZH-CN_TOPIC_0000002522240710__off9)接口功能一致。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 需要删除的监听事件类型。 |
| callback | WorkerEventListener | 否 | 回调函数，删除监听事件后执行。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[语言基础类库错误码](语言基础类库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 10200004 | Worker instance is not running. |

**示例：**

```ets
// Index.ets
import { worker } from '@kit.ArkTS';

const workerInstance = new worker.ThreadWorker("entry/ets/workers/worker.ets");

workerInstance.addEventListener("alert", () => {
  console.info("alert listener callback");
})

workerInstance.dispatchEvent({type: "alert", timeStamp: 0}); // timeStamp暂未支持

workerInstance.removeEventListener("alert");
```

#### dispatchEvent9+

dispatchEvent(event: Event): boolean

在宿主线程将事件对象分发到Worker线程的事件系统，该系统会自动触发该类型事件对应的所有监听器回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | Event | 是 | 需要分发的事件。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 分发的结果。true表示分发成功，false表示分发失败。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[语言基础类库错误码](语言基础类库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 10200004 | Worker instance is not running. |

**示例：**

```ets
// Index.ets
import { worker } from '@kit.ArkTS';

const workerInstance = new worker.ThreadWorker("entry/ets/workers/worker.ets");

workerInstance.addEventListener("alert", () => {
  console.info("alert listener callback");
})

let result: Boolean = workerInstance.dispatchEvent({type: "alert", timeStamp: 0}); // timeStamp暂未支持

console.info("dispatchEvent result is: ", result);
```

分发事件（dispatchEvent）可与监听接口（on、once、addEventListener）搭配使用，完整示例请参考[分发事件与监听接口搭配使用示例](#ZH-CN_TOPIC_0000002522240710__分发事件与监听接口搭配使用示例)。

#### removeAllListener9+

removeAllListener(): void

移除宿主线程中Worker实例对象的所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](语言基础类库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200004 | Worker instance is not running. |

**示例：**

```ets
// Index.ets
import { worker } from '@kit.ArkTS';

const workerInstance = new worker.ThreadWorker("entry/ets/workers/worker.ets");
workerInstance.addEventListener("alert", () => {
    console.info("alert listener callback");
})
workerInstance.removeAllListener();
```

#### WorkerEventTarget9+

用于管理Worker的监听事件。

#### addEventListener9+

addEventListener(type: string, listener: WorkerEventListener): void

向Worker线程的实例对象添加事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听的事件类型。 |
| listener | WorkerEventListener | 是 | 回调的事件。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[语言基础类库错误码](语言基础类库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 10200004 | The Worker instance is not running. |
| 10200005 | The called API is not supported in the worker thread. |

**示例：**

```ets
// worker.ets
import { ErrorEvent, MessageEvents, ThreadWorkerGlobalScope, worker } from '@kit.ArkTS';

const workerPort: ThreadWorkerGlobalScope = worker.workerPort;

workerPort.onmessage = (event: MessageEvents) => {
  workerPort.addEventListener("alert", () => {
    console.info("alert listener callback");
  })
};
```

#### removeEventListener9+

removeEventListener(type: string, callback?: WorkerEventListener): void

移除Worker线程实例对象中类型为type的事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 需要删除的监听事件类型。 |
| callback | WorkerEventListener | 否 | 回调函数，删除监听事件后执行。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](语言基础类库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 10200004 | The Worker instance is not running. |

**示例：**

```ets
// worker.ets
import { ErrorEvent, MessageEvents, ThreadWorkerGlobalScope, worker } from '@kit.ArkTS';

const workerPort: ThreadWorkerGlobalScope = worker.workerPort;

workerPort.onmessage = (event: MessageEvents) => {
  workerPort.addEventListener("alert", () => {
    console.info("alert listener callback");
  });

  workerPort.removeEventListener("alert");
};
```

#### dispatchEvent9+

dispatchEvent(event: Event): boolean

在Worker线程将事件对象分发到Worker线程的事件系统，并触发该类型事件的所有监听器回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | Event | 是 | 需要分发的事件。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 分发的结果。true表示分发成功，false表示分发失败。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[语言基础类库错误码](语言基础类库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 10200004 | The Worker instance is not running. |

**示例：**

```ets
// worker.ets
import { ErrorEvent, MessageEvents, ThreadWorkerGlobalScope, worker } from '@kit.ArkTS';

const workerPort: ThreadWorkerGlobalScope = worker.workerPort;

workerPort.onmessage = (event: MessageEvents) => {
  workerPort.addEventListener("alert", () => {
    console.info("alert listener callback");
  });

  workerPort.dispatchEvent({type: "alert", timeStamp: 0}); // timeStamp暂未支持
};
```

分发事件（dispatchEvent）可与监听接口（addEventListener）搭配使用，完整示例请参考[分发事件与监听接口搭配使用示例](#ZH-CN_TOPIC_0000002522240710__分发事件与监听接口搭配使用示例)。

#### removeAllListener9+

removeAllListener(): void

移除Worker线程的实例对象所有的事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](语言基础类库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200004 | The Worker instance is not running. |

**示例：**

```ets
// worker.ets
import { ErrorEvent, MessageEvents, ThreadWorkerGlobalScope, worker } from '@kit.ArkTS';

const workerPort: ThreadWorkerGlobalScope = worker.workerPort;

workerPort.onmessage = (event: MessageEvents) => {
  workerPort.addEventListener("alert", () => {
    console.info("alert listener callback");
  });

  workerPort.removeAllListener();
};
```

#### ThreadWorkerGlobalScope9+

Worker线程用于与宿主线程通信的类。ThreadWorkerGlobalScope类继承[GlobalScope](#ZH-CN_TOPIC_0000002522240710__globalscope9)。

#### 属性

**系统能力：** SystemCapability.Utils.Lang

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| onmessage9+ | (this: ThreadWorkerGlobalScope, ev: MessageEvents) => void | 否 | 是 | 回调函数。表示Worker线程收到来自其宿主线程通过postMessage或postMessageWithSharedSendable接口发送的消息时被调用的事件处理程序，处理程序在Worker线程中执行。其中this指调用者对象本身ThreadWorkerGlobalScope，ev类型为MessageEvents，表示收到的宿主线程发送的消息数据。默认值为undefined。 元服务API：从API version 11开始，该属性支持在元服务中使用。 |
| onmessageerror9+ | (this: ThreadWorkerGlobalScope, ev: MessageEvents) => void | 否 | 是 | 回调函数。表示当Worker线程的Worker对象接收到一条无法被反序列化的消息时被调用的事件处理程序，处理程序在Worker线程中执行。其中this指调用者对象本身ThreadWorkerGlobalScope，ev类型为MessageEvents，表示收到的消息数据。默认值为undefined。 元服务API：从API version 11开始，该属性支持在元服务中使用。 |

#### postMessage9+

postMessage(messageObject: Object, transfer: ArrayBuffer[]): void;

Worker线程通过转移对象所有权的方式向宿主线程发送消息。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| messageObject | Object | 是 | 发送至宿主线程的数据，该数据对象必须是可序列化对象，序列化支持类型见其他说明。 |
| transfer | ArrayBuffer[] | 是 | 表示可转移的ArrayBuffer实例对象数组，该数组中对象的所有权会被转移到宿主线程，在Worker线程中将会变为不可用，仅在宿主线程中可用，数组不可传入null。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[语言基础类库错误码](语言基础类库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 10200004 | The Worker instance is not running. |
| 10200006 | An exception occurred during serialization. |

**示例：**

```ets
// Index.ets
import { worker, MessageEvents } from '@kit.ArkTS';

const workerInstance = new worker.ThreadWorker("entry/ets/workers/worker.ets");
workerInstance.postMessage("hello world");
workerInstance.onmessage = (e: MessageEvents): void => {
    console.info("receive data from worker.ets");
}
```

```ets
// worker.ets
import { worker, MessageEvents } from '@kit.ArkTS';

const workerPort = worker.workerPort;
workerPort.onmessage = (e: MessageEvents): void => {
    let buffer = new ArrayBuffer(8);
    workerPort.postMessage(buffer, [buffer]);
}
```

#### postMessage9+

postMessage(messageObject: Object, options?: PostMessageOptions): void

Worker线程通过转移对象所有权或拷贝数据的方式向宿主线程发送消息。在传递[Sendable对象](../../guides/Sendable对象简介.md)时，使用拷贝数据的方式进行传递。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| messageObject | Object | 是 | 发送至宿主线程的数据，该数据对象必须是可序列化对象，序列化支持类型见其他说明。 |
| options | PostMessageOptions | 否 | 当填入该参数时，其作用与传入ArrayBuffer[]相同，该数组中对象的所有权会被转移到宿主线程，在Worker线程中将变为不可用，仅在宿主线程中可用。 若不填入该参数，默认设置为 undefined，通过拷贝数据的方式传输信息到宿主线程。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[语言基础类库错误码](语言基础类库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 10200004 | The Worker instance is not running. |
| 10200006 | An exception occurred during serialization. |

**示例：**

```ets
// Index.ets
import { worker, MessageEvents } from '@kit.ArkTS';

const workerInstance = new worker.ThreadWorker("entry/ets/workers/worker.ets");
workerInstance.postMessage("hello world");
workerInstance.onmessage = (e: MessageEvents): void => {
    console.info("receive data from worker.ets");
}
```

```ets
// worker.ets
import { worker, MessageEvents } from '@kit.ArkTS';

const workerPort = worker.workerPort;
workerPort.onmessage = (e: MessageEvents): void => {
    workerPort.postMessage("receive data from main thread");
}
```

#### postMessageWithSharedSendable12+

postMessageWithSharedSendable(message: Object, transfer?: ArrayBuffer[]): void

Worker线程向宿主线程发送消息，消息中的[Sendable对象](../../guides/Sendable对象简介.md)通过引用传递，非Sendable对象通过拷贝数据的方式传递。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| message | Object | 是 | 发送至宿主线程的数据，该数据对象必须是可序列化或可共享，序列化支持类型见序列化类型说明，共享支持类型见Sendable支持的数据类型。 |
| transfer | ArrayBuffer[] | 否 | 表示可转移的ArrayBuffer实例对象数组，该数组中对象的所有权会被转移到宿主线程，在Worker线程中将会变为不可用，仅在宿主线程中可用，数组不可传入null。默认值为空数组。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[语言基础类库错误码](语言基础类库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 10200004 | The Worker instance is not running. |
| 10200006 | An exception occurred during serialization. |

**示例：**

```ets
// worker文件路径为：entry/src/main/ets/workers/Worker.ets
// Worker.ets
// 新建SendableObject实例并通过Worker线程传递至宿主线程

import { SendableObject } from '../pages/sendable';
import { worker, ThreadWorkerGlobalScope, MessageEvents, ErrorEvent } from '@kit.ArkTS';

const workerPort: ThreadWorkerGlobalScope = worker.workerPort;
workerPort.onmessage = (e: MessageEvents) => {
  let object: SendableObject = new SendableObject();
  workerPort.postMessageWithSharedSendable(object);
}
```

```ets
// sendable.ets
// 定义SendableObject

@Sendable
export class SendableObject {
  a:number = 45;
}
```

```ets
// Index.ets
// 接收Worker线程传递至宿主线程的数据并访问其属性

import { worker, MessageEvents } from '@kit.ArkTS';
import { SendableObject } from './sendable';

const workerInstance = new worker.ThreadWorker("entry/ets/workers/Worker.ets");
workerInstance.postMessage(1);
workerInstance.onmessage = (e: MessageEvents) => {
  let obj: SendableObject = e.data;
  console.info("sendable index obj is: " + obj.a);
}
```

#### callGlobalCallObjectMethod11+

callGlobalCallObjectMethod(instanceName: string, methodName: string, timeout: number, ...args: Object[]): Object

Worker线程调用宿主线程上注册的对象的指定方法，此调用对Worker线程同步，对宿主线程异步，返回值通过数据拷贝传递。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| instanceName | string | 是 | 注册对象时使用的键，用于在宿主线程中查找对象。 |
| methodName | string | 是 | 在已注册对象上调用的方法名。该方法不能使用async修饰，也不能基于底层异步机制返回结果，否则会抛出异常。 |
| timeout | number | 是 | 表示从Worker线程发起调用开始到在主线程中执行目标方法的最大等待时间，单位为ms，取整数，取值范围为[1-5000]ms。也可取特殊值0，此时表示本次调用等待时间为5000ms。 API version 21 之前，在debug模式下受此参数设置的最大等待时间限制。 从API version 21 开始，在debug模式下不受此参数设置的最大等待时间限制，可一直等待。 |
argsObject[]否注册对象上所调用方法的参数数组。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Object | 返回值为调用方法在宿主线程的返回值，该返回值必须是可序列化的，具体可见序列化支持类型。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[语言基础类库错误码](语言基础类库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 10200004 | Worker instance is not running. |
| 10200006 | An exception occurred during serialization. |
| 10200019 | The globalCallObject is not registered. |
| 10200020 | The method to be called is not callable or is an async method or a generator. |
| 10200021 | The global call exceeds the timeout. |

**示例：**

```ets
//Index.ets
import { worker } from '@kit.ArkTS';

const workerInstance = new worker.ThreadWorker("entry/ets/workers/worker.ets");
class TestObj {
  private message : string = "this is a message from TestObj";
  public getMessage() : string {
    return this.message;
  }
  public getMessageWithInput(str : string) : string {
    return this.message + " with input: " + str;
}
let registerObj = new TestObj();
// 在ThreadWorker实例上注册registerObj
workerInstance.registerGlobalCallObject("myObj", registerObj);
workerInstance.postMessage("start worker");
// 需要在组件生命周期结束时调用：
// workerInstance.unregisterGlobalCallObject("myObj");
```

```ets
// worker.ets
import { worker, MessageEvents } from '@kit.ArkTS';

const workerPort = worker.workerPort;
workerPort.onmessage = (e: MessageEvents): void => {
  try {
    // 调用方法无入参
    let res : string = workerPort.callGlobalCallObjectMethod("myObj", "getMessage", 0) as string;
    console.info("worker:", res); // worker: this is a message from TestObj
  } catch (error) {
    // 异常处理
    console.error("worker: error code is " + error.code + " error message is " + error.message);
  }
  try {
    // 调用方法有入参
    let res : string = workerPort.callGlobalCallObjectMethod("myObj", "getMessageWithInput", 0, "hello there!") as string;
    console.info("worker:", res); //worker: this is a message from TestObj with input: hello there!
  } catch (error) {
    // 异常处理
    console.error("worker: error code is " + error.code + " error message is " + error.message);
  }
```

#### close9+

close(): void

销毁Worker线程，终止Worker接收消息。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](语言基础类库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200004 | The Worker instance is not running. |

**示例：**

```ets
// Index.ets
import { worker } from '@kit.ArkTS';

const workerInstance = new worker.ThreadWorker("entry/ets/workers/worker.ets");
workerInstance.postMessage("hello world");
```

```ets
// worker.ets
import { worker, MessageEvents } from '@kit.ArkTS';

const workerPort = worker.workerPort;
workerPort.onmessage = (e: MessageEvents): void => {
    workerPort.close();
}
```

#### WorkerEventListener9+

事件监听类。

#### (event: Event)9+

(event: Event): void | Promise<void>

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | Event | 是 | 回调的事件类。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| void | Promise<void> | 无返回值或者以Promise形式返回。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[语言基础类库错误码](语言基础类库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 10200004 | Worker instance is not running. |
| 10200005 | The invoked API is not supported in workers. |

**示例：**

```ets
// Index.ets
import { worker, Event } from "@kit.ArkTS"

const workerInstance = new worker.ThreadWorker("entry/ets/workers/worker.ets");

workerInstance.addEventListener("alert", (event: Event) => {
  console.info("event type is: ", JSON.stringify(event.type));
});

const eventToDispatch : Event = { type: "alert", timeStamp: 0 }; // timeStamp暂未支持
workerInstance.dispatchEvent(eventToDispatch);
```

#### GlobalScope9+

Worker线程自身的运行环境，GlobalScope类继承[WorkerEventTarget](#ZH-CN_TOPIC_0000002522240710__workereventtarget9)。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| name | string | 是 | 否 | Worker的名字，new Worker时指定。 |
| self | GlobalScope & typeof globalThis | 是 | 否 | GlobalScope本身。 |
| onerror | (ev: ErrorEvent) => void | 否 | 是 | Worker在执行过程中发生异常被调用的回调函数，在Worker线程中执行，ev表示收到的异常数据。默认值为undefined。 |

#### MessageEvents9+

消息类，持有Worker线程间传递的数据，MessageEvents类继承[Event](#ZH-CN_TOPIC_0000002522240710__event)。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| data | any | 是 | 否 | 线程间传递的数据。 |

**MessageType**

type MessageType = 'message' | 'messageerror'

表示消息类型。预留数据类型，暂未实现。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

| 类型 | 说明 |
| --- | --- |
| 'message' | 表示消息类型为message，值固定为'message'字符串。 |
| 'messageerror' | 表示消息类型为messageerror，值固定为'messageerror'字符串。 |

#### ErrorCallback18+

type ErrorCallback = (err: ErrorEvent) => void

表示异常回调类型。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| err | ErrorEvent | 是 | 错误事件类，表示Worker执行过程中出现的异常信息。 |

#### Worker(deprecated)

使用以下方法前，均需先构造Worker实例，Worker类继承[EventTarget](#ZH-CN_TOPIC_0000002522240710__eventtargetdeprecated)。


从API version 7开始支持，从API version 9开始废弃，建议使用[ThreadWorker9+](#ZH-CN_TOPIC_0000002522240710__threadworker9)替代。

#### 属性

**系统能力：** SystemCapability.Utils.Lang

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| onexit(deprecated) | (code: number) => void | 否 | 是 | 回调函数。表示Worker销毁时被调用的事件处理程序，处理程序在宿主线程中执行。其中回调函数中code类型为number，异常退出为1，正常退出为0。默认值为undefined。 说明：从API version 7开始支持，从API version 9开始废弃，建议使用ThreadWorker.onexit替代。 |
| onerror(deprecated) | (err: ErrorEvent) => void | 否 | 是 | 回调函数。表示Worker在执行过程中发生异常被调用的事件处理程序，处理程序在宿主线程中执行。其中回调函数中err类型为ErrorEvent，表示收到的异常数据。默认值为undefined。 说明：从API version 7开始支持，从API version 9开始废弃，建议使用ThreadWorker.onerror替代。 |
| onmessage(deprecated) | (event: MessageEvent) => void | 否 | 是 | 回调函数。表示宿主线程接收到来自其创建的Worker通过workerPort.postMessage接口发送的消息时被调用的事件处理程序，处理程序在宿主线程中执行。其中回调函数中event类型为MessageEvent，表示收到的Worker消息数据。默认值为undefined。 说明：从API version 7开始支持，从API version 9开始废弃，建议使用ThreadWorker.onmessage替代。 |
| onmessageerror(deprecated) | (event: MessageEvent) => void | 否 | 是 | 回调函数。表示当Worker对象接收到一条无法被序列化的消息时被调用的事件处理程序，处理程序在宿主线程中执行。其中回调函数中event类型为MessageEvent，表示收到的Worker消息数据。默认值为undefined。 说明：从API version 7开始支持，从API version 9开始废弃，建议使用ThreadWorker.onmessageerror替代。 |

#### constructor(deprecated)

constructor(scriptURL: string, options?: WorkerOptions)

Worker构造函数。


从API version 7开始支持，从API version 9开始废弃，建议使用[ThreadWorker.constructor9+](#ZH-CN_TOPIC_0000002522240710__constructor9)替代。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scriptURL | string | 是 | Worker线程文件的路径，详细参考文件路径注意事项。 |
| options | WorkerOptions | 否 | Worker构造的选项。 |

**示例：**

此处以在Stage模型的entry模块Index.ets文件中加载Worker文件为例，使用Library加载Worker线程文件的场景参考[文件路径注意事项](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/worker-introduction#文件路径注意事项)。

```ets
// Index.ets
import { worker } from '@kit.ArkTS';

// worker文件所在路径："entry/src/main/ets/workers/worker.ets"
const workerInstance = new worker.Worker('entry/ets/workers/worker.ets', {name: "WorkerThread"});
```

#### postMessage(deprecated)

postMessage(message: Object, transfer: ArrayBuffer[]): void

宿主线程通过转移对象所有权的方式向Worker线程发送消息。


从API version 7开始支持，从API version 9开始废弃，建议使用[ThreadWorker.postMessage9+](#ZH-CN_TOPIC_0000002522240710__postmessage9)替代。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| message | Object | 是 | 发送至Worker的数据对象必须是可序列化对象，序列化支持类型见其他说明。 |
| transfer | ArrayBuffer[] | 是 | 表示可转移的ArrayBuffer实例对象数组，所有权会转移到Worker线程，仅在该线程中可用。数组不可传入null。 |

**示例：**

```ets
// Index.ets
import { worker } from '@kit.ArkTS';

const workerInstance = new worker.Worker("entry/ets/workers/worker.ets");

let buffer = new ArrayBuffer(8);
workerInstance.postMessage(buffer, [buffer]);
```

#### postMessage(deprecated)

postMessage(message: Object, options?: PostMessageOptions): void

宿主线程通过转移对象所有权或者拷贝数据的方式向Worker线程发送消息。


从API version 7开始支持，从API version 9开始废弃，建议使用[ThreadWorker.postMessage9+](#ZH-CN_TOPIC_0000002522240710__postmessage9-1)替代。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| message | Object | 是 | 发送至Worker的数据，该数据对象必须是可序列化对象，序列化支持类型见其他说明。 |
| options | PostMessageOptions | 否 | 当填入该参数时，与传入ArrayBuffer[]的作用一致，该数组中对象的所有权会被转移到Worker线程，在宿主线程中将变为不可用，仅在Worker线程中可用。 若不填入该参数，默认设置为undefined，通过拷贝数据的方式传输信息到Worker线程。 |

**示例：**

```ets
// Index.ets
import { worker } from '@kit.ArkTS';

const workerInstance = new worker.Worker("entry/ets/workers/worker.ets");

workerInstance.postMessage("hello world");

let buffer = new ArrayBuffer(8);
workerInstance.postMessage(buffer, [buffer]);
```

#### on(deprecated)

on(type: string, listener: EventListener): void

向Worker添加一个事件监听，该接口与[addEventListener(deprecated)](#ZH-CN_TOPIC_0000002522240710__addeventlistenerdeprecated)接口功能一致。


从API version 7开始支持，从API version 9开始废弃，建议使用[ThreadWorker.on9+](#ZH-CN_TOPIC_0000002522240710__on9)替代。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听的事件类型。 |
| listener | EventListener | 是 | 回调事件。 |

**示例：**

```ets
// Index.ets
import { worker } from '@kit.ArkTS';

const workerInstance = new worker.Worker("entry/ets/workers/worker.ets");
workerInstance.on("alert", () => {
    console.info("alert listener callback");
})
```

#### once(deprecated)

once(type: string, listener: EventListener): void

向Worker添加一个事件监听，该事件监听只执行一次，执行完后会自动删除。


从API version 7开始支持，从API version 9开始废弃，建议使用[ThreadWorker.once9+](#ZH-CN_TOPIC_0000002522240710__once9)替代。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听的事件类型。 |
| listener | EventListener | 是 | 回调事件。 |

**示例：**

```ets
// Index.ets
import { worker } from '@kit.ArkTS';

const workerInstance = new worker.Worker("entry/ets/workers/worker.ets");
workerInstance.once("alert", () => {
    console.info("alert listener callback");
})
```

#### off(deprecated)

off(type: string, listener?: EventListener): void

移除类型为type的事件监听，该接口与[removeEventListener(deprecated)](#ZH-CN_TOPIC_0000002522240710__removeeventlistenerdeprecated)接口功能一致。


从API version 7开始支持，从API version 9开始废弃，建议使用[ThreadWorker.off9+](#ZH-CN_TOPIC_0000002522240710__off9)替代。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 需要删除的事件类型。 |
| listener | EventListener | 否 | 移除监听事件后所执行的回调事件。 |

**示例：**

```ets
// Index.ets
import { worker } from '@kit.ArkTS';

const workerInstance = new worker.Worker("entry/ets/workers/worker.ets");
//使用on接口、once接口或addEventListener接口创建“alert”事件，使用off接口删除事件。
workerInstance.off("alert");
```

#### terminate(deprecated)

terminate(): void

销毁Worker线程，终止Worker接收消息。


从API version 7开始支持，从API version 9开始废弃，建议使用[ThreadWorker.terminate9+](#ZH-CN_TOPIC_0000002522240710__terminate9)替代。

**系统能力：** SystemCapability.Utils.Lang

**示例：**

```ets
// Index.ets
import { worker } from '@kit.ArkTS';

const workerInstance = new worker.Worker("entry/ets/workers/worker.ets");
workerInstance.terminate();
```

#### EventTarget(deprecated)


从API version 7开始支持，从API version 9开始废弃，建议使用[WorkerEventTarget9+](#ZH-CN_TOPIC_0000002522240710__workereventtarget9)替代。

#### addEventListener(deprecated)

addEventListener(type: string, listener: EventListener): void

向Worker添加一个事件监听，该接口与[on(deprecated)](#ZH-CN_TOPIC_0000002522240710__ondeprecated)接口功能一致。


从API version 7开始支持，从API version 9开始废弃，建议使用[addEventListener9+](#ZH-CN_TOPIC_0000002522240710__addeventlistener9)替代。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听的事件类型。 |
| listener | EventListener | 是 | 事件触发时的回调函数。 |

**示例：**

```ets
// worker.ets
import { DedicatedWorkerGlobalScope, ErrorEvent, MessageEvents, worker } from '@kit.ArkTS';

const workerPort: DedicatedWorkerGlobalScope = worker.parentPort;

workerPort.addEventListener("alert", () => {
  console.info("alert listener callback");
})
```

#### removeEventListener(deprecated)

removeEventListener(type: string, callback?: EventListener): void

移除Worker的事件监听，该接口与[off(deprecated)](#ZH-CN_TOPIC_0000002522240710__offdeprecated)接口功能一致。


从API version 7开始支持，从API version 9开始废弃，建议使用[removeEventListener9+](#ZH-CN_TOPIC_0000002522240710__removeeventlistener9)替代。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 需要移除的事件类型。 |
| callback | EventListener | 否 | 回调函数，删除监听事件后执行。 |

**示例：**

```ets
// worker.ets
import { DedicatedWorkerGlobalScope, ErrorEvent, MessageEvents, worker } from '@kit.ArkTS';

const workerPort: DedicatedWorkerGlobalScope = worker.parentPort;

workerPort.addEventListener("alert", () => {
  console.info("alert listener callback");
})

workerPort.removeEventListener('alert');
```

#### dispatchEvent(deprecated)

dispatchEvent(event: Event): boolean

分发定义在Worker的事件。


从API version 7开始支持，从API version 9开始废弃，建议使用[dispatchEvent9+](#ZH-CN_TOPIC_0000002522240710__dispatchevent9)替代。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | Event | 是 | 需要分发的事件。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 分发的结果。true表示分发成功，false表示分发失败。 |

**示例：**

```ets
// worker.ets
import { DedicatedWorkerGlobalScope, ErrorEvent, MessageEvents, worker } from '@kit.ArkTS';

const workerPort: DedicatedWorkerGlobalScope = worker.parentPort;

workerPort.addEventListener("alert_add", ()=>{
  console.info("alert listener callback");
})

workerPort.dispatchEvent({type: 'alert_add', timeStamp: 0}); // timeStamp暂未支持
```

分发事件（dispatchEvent）可与监听接口（addEventListener）搭配使用，示例如下：

```ets
// Index.ets
import { worker } from '@kit.ArkTS';

const workerInstance = new worker.Worker("entry/ets/workers/worker.ets");
workerInstance.postMessage("hello world");
workerInstance.onmessage = (): void => {
    console.info("receive data from worker.ets");
}
```

```ets
// worker.ets
import { DedicatedWorkerGlobalScope, ErrorEvent, MessageEvents, worker } from '@kit.ArkTS';

const workerPort: DedicatedWorkerGlobalScope = worker.parentPort;

workerPort.addEventListener("alert", ()=>{
  console.info("alert listener callback");
})

workerPort.onmessage = (event: MessageEvents) => {
  workerPort.dispatchEvent({type:"alert", timeStamp:0}); // timeStamp暂未支持
}
```

#### removeAllListener(deprecated)

removeAllListener(): void

移除Worker所有的事件监听。


从API version 7开始支持，从API version 9开始废弃，建议使用[removeAllListener9+](#ZH-CN_TOPIC_0000002522240710__removealllistener9)替代。

**系统能力：** SystemCapability.Utils.Lang

**示例：**

```ets
// worker.ets
import { DedicatedWorkerGlobalScope, ErrorEvent, MessageEvents, worker } from '@kit.ArkTS';

const workerPort: DedicatedWorkerGlobalScope = worker.parentPort;

workerPort.addEventListener("alert_add", ()=>{
  console.info("alert listener callback");
})

workerPort.removeAllListener();
```

#### DedicatedWorkerGlobalScope(deprecated)

Worker线程用于与宿主线程通信的类。DedicatedWorkerGlobalScope类继承[WorkerGlobalScope](#ZH-CN_TOPIC_0000002522240710__workerglobalscopedeprecated)。


从API version 7开始支持，从API version 9开始废弃，建议使用[ThreadWorkerGlobalScope9+](#ZH-CN_TOPIC_0000002522240710__threadworkerglobalscope9)替代。

#### 属性

**系统能力：** SystemCapability.Utils.Lang

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| onmessage(deprecated) | (this: DedicatedWorkerGlobalScope, ev: MessageEvent) => void | 否 | 是 | 回调函数，表示Worker线程收到来自其宿主线程通过postMessage接口发送的消息时被调用的事件处理程序，处理程序在Worker线程中执行。其中this指调用者对象本身DedicatedWorkerGlobalScope，ev类型为MessageEvent，表示收到的Worker消息数据。默认值为undefined。 说明：从API version 7开始支持，从API version 9开始废弃，建议使用ThreadWorkerGlobalScope.onmessage替代。 |
| onmessageerror(deprecated) | (this: DedicatedWorkerGlobalScope, ev: MessageEvent) => void | 否 | 是 | 回调函数，表示当Worker对象接收到一条无法被反序列化的消息时被调用的事件处理程序，处理程序在Worker线程中执行。其中this指调用者对象本身DedicatedWorkerGlobalScope，ev类型为MessageEvent，表示收到的Worker消息数据。从API version 7开始支持，默认值为undefined。 说明：从API version 9开始废弃，建议使用ThreadWorkerGlobalScope.onmessageerror替代。 |

#### postMessage(deprecated)

postMessage(messageObject: Object, transfer: Transferable[]): void

Worker线程通过转移对象所有权的方式向宿主线程发送消息。


此接口暂不支持使用，从API version 9开始废弃，建议使用[ThreadWorkerGlobalScope9+.postMessage9+](#ZH-CN_TOPIC_0000002522240710__postmessage9-2)替代。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| messageObject | Object | 是 | 发送至宿主线程的数据，该数据对象必须是可序列化对象，序列化支持类型见其他说明。 |
| transfer | Transferable[] | 是 | 暂不支持该参数类型。 |

#### postMessage(deprecated)

postMessage(messageObject: Object, transfer: ArrayBuffer[]): void

Worker线程通过转移对象所有权的方式向宿主线程发送消息。


postMessage接口从API version 9开始支持，从API version 9开始废弃，建议使用[ThreadWorkerGlobalScope9+.postMessage9+](#ZH-CN_TOPIC_0000002522240710__postmessage9-2)替代。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| messageObject | Object | 是 | 发送至宿主线程的数据，该数据对象必须是可序列化对象，序列化支持类型见其他说明。 |
| transfer | ArrayBuffer[] | 是 | 表示可转移的ArrayBuffer实例对象数组，该数组中对象的所有权会被转移到宿主线程，在Worker线程中将会变为不可用，仅在宿主线程中可用，数组不可传入null。 |

**示例：**

```ets
// Index.ets
import { worker } from '@kit.ArkTS';

const workerInstance = new worker.Worker("entry/ets/workers/worker.ets");
workerInstance.postMessage("hello world");
workerInstance.onmessage = (e: MessageEvents): void => {
    // let data = e.data;
    console.info("receive data from worker.ets");
}
```

```ets
// worker.ets
import { DedicatedWorkerGlobalScope, worker } from '@kit.ArkTS';

const workerPort: DedicatedWorkerGlobalScope = worker.parentPort;

workerPort.onmessage = (): void => {
    // let data = e.data;
    let buffer = new ArrayBuffer(5)
    workerPort.postMessage(buffer, [buffer]);
}
```

#### postMessage(deprecated)

postMessage(messageObject: Object, options?: PostMessageOptions): void

Worker线程通过转移对象所有权或者拷贝数据的方式向宿主线程发送消息。


从API version 7开始支持，从API version 9开始废弃，建议使用[ThreadWorkerGlobalScope9+.postMessage9+](#ZH-CN_TOPIC_0000002522240710__postmessage9-3)替代。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| messageObject | Object | 是 | 发送至宿主线程的数据，该数据对象必须是可序列化对象，序列化支持类型见其他说明。 |
| options | PostMessageOptions | 否 | 当填入该参数时，与传入ArrayBuffer[]的作用一致，该数组中对象的所有权会被转移到宿主线程，在Worker线程中将会变为不可用，仅在宿主线程中可用。 若不填入该参数，默认设置为 undefined，通过拷贝数据的方式传输信息到宿主线程。 |

**示例：**

```ets
// Index.ets
import { worker } from '@kit.ArkTS';

const workerInstance = new worker.Worker("entry/ets/workers/worker.ets");
workerInstance.postMessage("hello world");
workerInstance.onmessage = (): void => {
    console.info("receive data from worker.ets");
}
```

```ets
// worker.ets
import { ErrorEvent, MessageEvents, worker } from '@kit.ArkTS';

const parentPort = worker.parentPort;
parentPort.onmessage = (e: MessageEvents) => {
  parentPort.postMessage("receive data from main thread");
}
```

#### close(deprecated)

close(): void

销毁Worker线程，终止Worker接收消息。


从API version 7开始支持，从API version 9开始废弃，建议使用[ThreadWorkerGlobalScope9+.close9+](#ZH-CN_TOPIC_0000002522240710__close9)替代。

**系统能力：** SystemCapability.Utils.Lang

**示例：**

```ets
// Index.ets
import { worker } from '@kit.ArkTS';

const workerInstance = new worker.Worker("entry/ets/workers/worker.ets");
workerInstance.postMessage("hello world");
```

```ets
// worker.ets
import { worker } from '@kit.ArkTS';

const parentPort = worker.parentPort;
parentPort.onmessage = (): void => {
    parentPort.close()
}
```

#### PostMessageOptions

明确数据传递过程中需要转移所有权的对象，这些对象必须是ArrayBuffer，在发送方的上下文中将变为不可用，仅在接收方可用。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| transfer | Object[] | 否 | 是 | ArrayBuffer数组，用于传递所有权。该数组中不可传入null。默认值为undefined。 |

#### Event

事件类。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | string | 是 | 否 | 指定事件的类型。 |
| timeStamp | number | 是 | 否 | 事件创建时的时间戳（精度为毫秒），目前不支持。 |

#### EventListener(deprecated)

事件监听类用于处理事件。


从API version 7开始支持，从API version 9开始废弃，建议使用[WorkerEventListener9+](#ZH-CN_TOPIC_0000002522240710__workereventlistener9)替代。

#### (evt: Event)(deprecated)

(evt: Event): void | Promise<void>


从API version 7开始支持，从API version 9开始废弃，建议使用[(event:Event)9+](#ZH-CN_TOPIC_0000002522240710__event-event9)替代。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| evt | Event | 是 | 回调的事件类。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| void | Promise<void> | 无返回值或者以Promise形式返回。 |

**示例：**

```ets
// Index.ets
import { worker } from '@kit.ArkTS';

const workerInstance = new worker.Worker("entry/ets/workers/worker.ets");
workerInstance.addEventListener("alert", ()=>{
    console.info("alert listener callback");
})
```

#### ErrorEvent

错误事件类用于表示Worker执行过程中出现异常的详细信息，该类继承[Event](#ZH-CN_TOPIC_0000002522240710__event)。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| message | string | 是 | 否 | 异常发生的错误信息。 |
| filename | string | 是 | 否 | 出现异常所在的文件。 |
| lineno | number | 是 | 否 | 异常所在的行数。 |
| colno | number | 是 | 否 | 异常所在的列数。 |
| error | Object | 是 | 否 | 异常类型。 |

#### MessageEvent<T>

消息类，持有Worker线程间传递的数据，MessageEvent类继承[Event](#ZH-CN_TOPIC_0000002522240710__event)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| data | T | 是 | 否 | 线程间传递的数据。 |

#### WorkerGlobalScope(deprecated)

Worker线程自身的运行环境，WorkerGlobalScope类继承[EventTarget](#ZH-CN_TOPIC_0000002522240710__eventtargetdeprecated)。


从API version 7开始支持，从API version 9开始废弃，建议使用[GlobalScope9+](#ZH-CN_TOPIC_0000002522240710__globalscope9)替代。

**系统能力：** SystemCapability.Utils.Lang

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| name | string | 是 | 否 | Worker的名字，new Worker时指定。 |
| self | WorkerGlobalScope & typeof globalThis | 是 | 否 | WorkerGlobalScope本身。 |
| onerror | (ev: ErrorEvent) => void | 否 | 是 | Worker在执行过程中发生异常被调用的回调函数，在Worker线程中执行，ev表示收到的异常数据，默认值为undefined。 |

#### 其他说明

#### 序列化支持类型

序列化支持类型包括：除Symbol之外的基础类型、Date、String、RegExp、Array、Map、Set、Object（仅限简单对象，比如通过"{}"或者"new Object"创建，普通对象仅支持传递属性，不支持传递其原型及方法）、ArrayBuffer、TypedArray。

特例：传递通过自定义class创建出来的object时，不会发生序列化错误，但是自定义class的属性（如Function）无法通过序列化传递。

以API version 9的FA工程为例。

```ets
// Index.ets
import { worker, MessageEvents } from '@kit.ArkTS';

const workerInstance = new worker.ThreadWorker("workers/worker.ets");
workerInstance.postMessage("message from main thread to worker");
workerInstance.onmessage = (d: MessageEvents): void => {
  // 当Worker线程传递obj2时，data即为obj2。data没有Init、SetName的方法
  let data: string  = d.data;
}
```

```ets
// worker.ets
import { worker, MessageEvents, ErrorEvent } from '@kit.ArkTS';

const workerPort = worker.workerPort;
class MyModel {
    name = "undefined";
    Init() {
        this.name = "MyModel";
}
workerPort.onmessage = (d: MessageEvents): void => {
  console.info("worker.ets onmessage");
  let data: string = d.data;
  let func1 = () => {
    console.info("post message is function");
  }
  // workerPort.postMessage(func1); 传递func1发生序列化错误
  let obj2 = new MyModel();
  workerPort.postMessage(obj2);     // 传递obj2不会发生序列化错误，obj2中的函数会丢失
}
workerPort.onmessageerror = () => {
    console.error("worker.ets onmessageerror");
}
workerPort.onerror = (err: ErrorEvent) => {
    console.error("worker.ets onerror" + err.message);
}
```

#### 内存模型

Worker基于Actor并发模型实现。在Worker的交互流程中，宿主线程可以创建多个Worker子线程，各个Worker线程间运行环境相互隔离，并通过序列化、引用传递或转移所有权的方式传递对象，等到Worker线程完成计算任务，再把结果返回给宿主线程。

Actor并发模型的交互原理：各个Actor并发地处理宿主线程任务，每个Actor内部都有一个消息队列和单线程执行模块。消息队列负责接收宿主线程及其他Actor的请求，而单线程执行模块则负责串行地处理这些请求、向其他Actor发送请求以及创建新的Actor。由于Actor采用的是异步方式，各个Actor之间相互隔离且没有数据竞争，因此Actor可以高并发运行。

#### 完整示例

API version 8及之前的版本仅支持FA模型，如需使用，注意更换构造Worker的接口和创建Worker线程中与宿主线程通信的对象的两个方法。

#### FA模型

此处以API version 9的工程为例。

```ets
// main thread(同级目录为例)
import { worker, MessageEvents, ErrorEvent } from '@kit.ArkTS';

// 宿主线程中创建Worker对象
const workerInstance = new worker.ThreadWorker("workers/worker.ets");

// 宿主线程向worker线程传递信息
const buffer = new ArrayBuffer(8);
workerInstance.postMessage(buffer, [buffer]);

// 宿主线程接收worker线程信息
workerInstance.onmessage = (e: MessageEvents): void => {
    // data：worker线程发送的信息
    let data: Int8Array = e.data;
    console.info("main thread onmessage");

    // 销毁Worker对象
    workerInstance.terminate();
}

// 在调用terminate后，执行回调onexit
workerInstance.onexit = (code) => {
    console.info("main thread terminate");
}

workerInstance.onerror = (err: ErrorEvent) => {
    console.error("main error message " + err.message);
}
```

```ets
// worker.ets
import { worker, MessageEvents, ErrorEvent } from '@kit.ArkTS';

// 创建worker线程中与宿主线程通信的对象
const workerPort = worker.workerPort;

// worker线程接收宿主线程信息
workerPort.onmessage = (e: MessageEvents): void => {
    // data：宿主线程发送的信息
    let data: ArrayBuffer = e.data;
    const view = new Int8Array(data).fill(3);
    console.info("worker.ets onmessage");

    // worker线程向宿主线程发送信息
    workerPort.postMessage(view);
}

// worker线程发生error的回调
workerPort.onerror = (err: ErrorEvent) => {
    console.error("worker.ets onerror");
}
```

在模块级entry/build-profile.json5配置文件中添加如下配置:

```ets
  "buildOption": {
    "sourceOption": {
      "workers": [
        "./src/main/ets/entryability/workers/worker.ets"
      ]
    }
```

#### Stage模型

此处以API version 18的工程为例。

```ets
// Index.ets
import { worker, MessageEvents, ErrorEvent } from '@kit.ArkTS';

@Entry
@Component
struct Index {
  @State message: string = 'Hello World';
  build() {
    Row() {
      Column() {
        Text(this.message)
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
          .onClick(() => {
            // 宿主线程中创建Worker对象
            const workerInstance = new worker.ThreadWorker("entry/ets/workers/Worker.ets");
            // 宿主线程向worker线程传递信息
            const buffer = new ArrayBuffer(8);
            workerInstance.postMessage(buffer);
            // 宿主线程接收worker线程信息
            workerInstance.onmessage = (e: MessageEvents): void => {
              // data：worker线程发送的信息
              let data: Int8Array = e.data;
              console.info("main thread data is  " + data);
              // 销毁Worker对象
              workerInstance.terminate();
            }
            // 在调用terminate后，执行onexit
            workerInstance.onexit = (code) => {
              console.info("main thread terminate");
            }

            workerInstance.onAllErrors = (err: ErrorEvent) => {
              console.error("main error message " + err.message);
            }
          })
      }
      .width('100%')
      .height('100%')
    }
```

```ets
// Worker.ets
import { worker, MessageEvents, ErrorEvent } from '@kit.ArkTS';

// 创建worker线程中与宿主线程通信的对象
const workerPort = worker.workerPort;

// worker线程接收宿主线程信息
workerPort.onmessage = (e: MessageEvents): void => {
  // data：宿主线程发送的信息
  let data: ArrayBuffer = e.data;
  // 往收到的buffer里写入数据
  const view = new Int8Array(data).fill(3);
  // worker线程向宿主线程发送信息
  workerPort.postMessage(view);
}

// worker线程发生error的回调
workerPort.onerror = (err: ErrorEvent) => {
  console.error("worker.ets onerror" + err.message);
}
```

在模块级entry/build-profile.json5配置文件中添加如下配置:

```ets
  "buildOption": {
    "sourceOption": {
      "workers": [
        "./src/main/ets/workers/Worker.ets"
      ]
  }
```

#### 分发事件与监听接口搭配使用示例

```ets
// Index.ets
import { worker, MessageEvents } from '@kit.ArkTS';

@Entry
@Component
struct Index {
  @State message: string = 'Hello World';

  build() {
    RelativeContainer() {
      Text(this.message)
        .id('HelloWorld')
        .fontSize($r('app.float.page_text_font_size'))
        .fontWeight(FontWeight.Bold)
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        })
        .onClick(() => {
          const workerInstance = new worker.ThreadWorker("entry/ets/workers/worker.ets");

          // 用法一:
          workerInstance.on("alert_on", () => {
            console.info("alert listener callback: alert_on");
          })
          workerInstance.once("alert_once", () => {
            console.info("alert listener callback: alert_once");
          })
          workerInstance.addEventListener("alert_add", () => {
            console.info("alert listener callback: alert_add");
          })

          // once接口创建的事件执行一次便会删除。
          workerInstance.dispatchEvent({type: "alert_once", timeStamp: 0}); // timeStamp暂未支持
          // on接口创建的事件可以一直被分发，不能主动删除。
          workerInstance.dispatchEvent({type: "alert_on", timeStamp: 0}); // timeStamp暂未支持
          // addEventListener接口创建的事件可以一直被分发，不能主动删除。
          workerInstance.dispatchEvent({type: "alert_add", timeStamp: 0}); // timeStamp暂未支持

          // 用法二:
          // event类型的type支持自定义，同时存在"message"/"messageerror"/"error"特殊类型，如下所示
          // 当type = "message"，onmessage接口定义的方法同时会执行。
          // 当type = "messageerror"，onmessageerror接口定义的方法同时会执行。
          // 当type = "error"，onerror接口定义的方法同时会执行。
          // 若调用removeEventListener接口或者off接口取消事件时，能且只能取消使用addEventListener/on/once创建的事件。

          workerInstance.addEventListener("message", () => {
            console.info("message listener callback");
          })
          workerInstance.onmessage = (e: MessageEvents): void => {
            console.info("onmessage : message listener callback");
          }
          // 调用dispatchEvent分发“message”事件，addEventListener和onmessage中定义的方法都会被执行。
          workerInstance.dispatchEvent({type: "message", timeStamp: 0}); // timeStamp暂未支持

          // 向worker线程发送消息
          workerInstance.postMessage("test");
        })
    }
    .height('100%')
    .width('100%')
  }
```

```ets
// worker.ets
import { ErrorEvent, MessageEvents, ThreadWorkerGlobalScope, worker } from '@kit.ArkTS';

const workerPort: ThreadWorkerGlobalScope = worker.workerPort;

workerPort.onmessage = (event: MessageEvents) => {
  console.info("worker thread recv data is: ", event.data);
  let data: string = event.data;
  const workerHandler1 = () => console.info("Handler 1 is: ", data);
  const workerHandler2 = () => console.info("Handler 2 is: ", data);

  // 注册两个监听器
  workerPort.addEventListener("workerListener", workerHandler1);
  workerPort.addEventListener("workerListener", workerHandler2);

  // 事件workerListener注册了两个监听器，两个监听器都会执行
  workerPort.dispatchEvent({type: "workerListener", timeStamp: 0}); // timeStamp暂未支持

  // 删除workerHandler1监听器
  workerPort.removeEventListener("workerListener", workerHandler1); // timeStamp暂未支持

  // workerHandler1监听器已删除，只有workerHandler2执行
  workerPort.dispatchEvent({type: "workerListener", timeStamp: 0}); // timeStamp暂未支持

  // 删除所有事件监听
  workerPort.removeAllListener();
};
```