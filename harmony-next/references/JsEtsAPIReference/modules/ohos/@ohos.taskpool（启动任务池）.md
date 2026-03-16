# @ohos.taskpool（启动任务池）

任务池（taskpool）的作用是为应用程序提供多线程运行环境，降低资源消耗并提升系统性能，且您无需关心线程的生命周期。您可以使用任务池API创建后台任务（Task），并进行如执行任务或取消任务等操作。理论上，任务池API允许创建的任务数量不受限制，但由于内存限制，不建议这样做。此外，不建议在任务中执行阻塞操作，尤其是无限期阻塞操作，因为长时间的阻塞操作会占用工作线程，可能阻塞其他任务的调度，影响应用性能。

创建同一优先级的任务时，可以自行决定其执行顺序。任务的实际执行顺序与调用任务池API提供的任务执行接口的顺序一致。任务的默认优先级为MEDIUM。

当同一时间待执行的任务数量大于任务池工作线程数量，任务池会根据负载均衡机制进行扩容，增加工作线程数量，减少整体等待时长。同样，当执行的任务数量减少，工作线程数量大于执行任务数量，部分工作线程处于空闲状态，任务池会根据负载均衡机制进行缩容，减少工作线程数量。

任务池API返回错误码。如需了解各错误码的详细信息，请参阅文档[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

请查阅[TaskPool注意事项](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/taskpool-introduction#taskpool注意事项)，了解使用TaskPool时的相关注意点。

文档中涉及以下任务概念：

- 任务组任务：对应为[TaskGroup](#ZH-CN_TOPIC_0000002497444774__taskgroup10)任务。
- 串行队列任务：对应为[SequenceRunner](#ZH-CN_TOPIC_0000002497444774__sequencerunner-11)任务。
- 异步队列任务：对应为[AsyncRunner](#ZH-CN_TOPIC_0000002497444774__asyncrunner18)任务。
- 周期任务：由[executePeriodically](#ZH-CN_TOPIC_0000002497444774__taskpoolexecuteperiodically12)执行的任务。

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { taskpool } from '@kit.ArkTS';
```

#### taskpool.execute

execute(func: Function, ...args: Object[]): Promise<Object>

将待执行的函数放入taskpool的内部任务队列，函数不会立即执行，而是等待分发到工作线程执行。在当前执行模式下，不支持取消任务。使用Promise异步回调。

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数：**

参数名类型必填说明funcFunction是执行的逻辑需要传入一个函数，该函数必须使用[@Concurrent装饰器](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/taskpool-introduction#concurrent装饰器)装饰。支持的函数返回值类型请查[序列化支持类型](#ZH-CN_TOPIC_0000002497444774__序列化支持类型)。argsObject[]否执行逻辑的函数所需要的入参，支持的参数类型请查[序列化支持类型](#ZH-CN_TOPIC_0000002497444774__序列化支持类型)。默认值为undefined。

**返回值：**

类型说明Promise<Object>Promise对象，返回任务函数的执行结果。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.10200006An exception occurred during serialization.10200014The function is not marked as concurrent.

**示例：**

```ets
@Concurrent
function printArgs(args: number): number {
    console.info("printArgs: " + args);
    return args;
}

taskpool.execute(printArgs, 100).then((value: Object) => { // 100: test number
  console.info("taskpool result: " + value);
});
```

#### taskpool.execute13+

execute<A extends Array<Object>, R>(func: (...args: A) => R | Promise<R>, ...args: A): Promise<R>

校验并发函数的参数类型和返回类型后，将函数添加到taskpool的任务队列。使用Promise异步回调。

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**参数：**

参数名类型必填说明func(...args: A) => R | Promise<R>是执行的逻辑需要传入函数，必须使用[@Concurrent装饰器](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/taskpool-introduction#concurrent装饰器)装饰，支持的函数返回值类型请查[序列化支持类型](#ZH-CN_TOPIC_0000002497444774__序列化支持类型)。argsA否执行逻辑的函数所需要的入参，支持的参数类型请查[序列化支持类型](#ZH-CN_TOPIC_0000002497444774__序列化支持类型)。默认值为undefined。

**返回值：**

类型说明Promise<R>Promise对象，返回任务函数的执行结果。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Incorrect parameter types; 2.Parameter verification failed.10200006An exception occurred during serialization.10200014The function is not marked as concurrent.

**示例：**

```ets
@Concurrent
function printArgs(args: number): number {
  console.info("printArgs: " + args);
  return args;
}

@Concurrent
function testWithThreeParams(a: number, b: string, c: number): string {
  return b;
}

@Concurrent
function testWithArray(args: [number, string]): string {
  return "success";
}

taskpool.execute<[number], number>(printArgs, 100).then((value: number) => { // 100: test number
  console.info("taskpool result: " + value); // "taskpool result: 100"
});

taskpool.execute<[number, string, number], string>(testWithThreeParams, 100, "test", 100).then((value: string) => {
  console.info("taskpool result: " + value); // "taskpool result: test"
});

taskpool.execute<[[number, string]], string>(testWithArray, [100, "test"]).then((value: string) => {
  console.info("taskpool result: " + value); // "taskpool result: success"
});
```

#### taskpool.execute

execute(task: Task, priority?: Priority): Promise<Object>

将创建好的任务添加到taskpool的内部任务队列中，任务不会立即执行，而是等待分发到工作线程执行。当前模式支持设置任务优先级和通过cancel取消任务。任务不能是任务组任务、串行队列任务或异步队列任务。非长时任务可以多次调用执行。使用Promise异步回调。

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数：**

参数名类型必填说明task[Task](#ZH-CN_TOPIC_0000002497444774__task)是需要在任务池中执行的任务。priority[Priority](#ZH-CN_TOPIC_0000002497444774__priority)否该参数表示等待执行的任务的优先级，默认值为taskpool.Priority.MEDIUM。

**返回值：**

类型说明Promise<Object>Promise对象，返回任务函数的执行结果。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.10200006An exception occurred during serialization.10200014The function is not marked as concurrent.10200051The periodic task cannot be executed again.10200057The task cannot be executed by two APIs.

**示例：**

```ets
@Concurrent
function printArgs(args: number): number {
    console.info("printArgs: " + args);
    return args;
}

let task1: taskpool.Task = new taskpool.Task(printArgs, 100); // 100: test number
let task2: taskpool.Task = new taskpool.Task(printArgs, 200); // 200: test number
let task3: taskpool.Task = new taskpool.Task(printArgs, 300); // 300: test number
taskpool.execute(task1, taskpool.Priority.LOW).then((value: Object) => {
  console.info("taskpool result1: " + value);
});
taskpool.execute(task2, taskpool.Priority.MEDIUM).then((value: Object) => {
  console.info("taskpool result2: " + value);
});
taskpool.execute(task3, taskpool.Priority.HIGH).then((value: Object) => {
  console.info("taskpool result3: " + value);
});
```

#### taskpool.execute13+

execute<A extends Array<Object>, R>(task: GenericsTask<A, R>, priority?: Priority): Promise<R>

将创建好的泛型任务放入taskpool的内部任务队列，不校验任务的参数类型和返回值类型。使用Promise异步回调。

execute任务的校验是结合new GenericsTask一起用的，参数、返回值类型需与new GenericsTask中的类型保持一致。

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**参数：**

参数名类型必填说明task[GenericsTask<A, R>](#ZH-CN_TOPIC_0000002497444774__genericstask13)是需要在任务池中执行的泛型任务。priority[Priority](#ZH-CN_TOPIC_0000002497444774__priority)否等待执行的任务的优先级，默认值为taskpool.Priority.MEDIUM。

**返回值：**

类型说明Promise<R>Promise对象，返回任务函数的执行结果。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Incorrect parameter types; 2.Parameter verification failed.10200006An exception occurred during serialization.10200014The function is not marked as concurrent.10200051The periodic task cannot be executed again.10200057The task cannot be executed by two APIs.

**示例：**

```ets
@Concurrent
function printArgs(args: number): number {
    console.info("printArgs: " + args);
    return args;
}

let task1: taskpool.Task = new taskpool.GenericsTask<[number], number>(printArgs, 100); // 100: test number
let task2: taskpool.Task = new taskpool.GenericsTask<[number], number>(printArgs, 200); // 200: test number
let task3: taskpool.Task = new taskpool.GenericsTask<[number], number>(printArgs, 300); // 300: test number
taskpool.execute<[number], number>(task1, taskpool.Priority.LOW).then((value: number) => {
  console.info("taskpool result1: " + value);
});
taskpool.execute<[number], number>(task2, taskpool.Priority.MEDIUM).then((value: number) => {
  console.info("taskpool result2: " + value);
});
taskpool.execute<[number], number>(task3, taskpool.Priority.HIGH).then((value: number) => {
  console.info("taskpool result3: " + value);
});
```

#### taskpool.execute10+

execute(group: TaskGroup, priority?: Priority): Promise<Object[]>

将创建好的任务组放入taskpool内部任务队列，任务组中的任务不会立即执行，而是等待分发到工作线程执行。任务组中任务全部执行完成后，结果数组统一返回。此模式适用于执行关联任务。使用Promise异步回调。

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数：**

参数名类型必填说明group[TaskGroup](#ZH-CN_TOPIC_0000002497444774__taskgroup10)是需要在任务池中执行的任务组。priority[Priority](#ZH-CN_TOPIC_0000002497444774__priority)否等待执行的任务组的优先级，该参数默认值为taskpool.Priority.MEDIUM。

**返回值：**

类型说明Promise<Object[]>Promise对象数组，返回任务函数的执行结果。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.10200006An exception occurred during serialization.

**示例：**

```ets
@Concurrent
function printArgs(args: number): number {
    console.info("printArgs: " + args);
    return args;
}

let taskGroup1: taskpool.TaskGroup = new taskpool.TaskGroup();
taskGroup1.addTask(printArgs, 10); // 10: test number
taskGroup1.addTask(printArgs, 20); // 20: test number
taskGroup1.addTask(printArgs, 30); // 30: test number

let taskGroup2: taskpool.TaskGroup = new taskpool.TaskGroup();
let task1: taskpool.Task = new taskpool.Task(printArgs, 100); // 100: test number
let task2: taskpool.Task = new taskpool.Task(printArgs, 200); // 200: test number
let task3: taskpool.Task = new taskpool.Task(printArgs, 300); // 300: test number
taskGroup2.addTask(task1);
taskGroup2.addTask(task2);
taskGroup2.addTask(task3);
taskpool.execute(taskGroup1).then((res: Array<Object>) => {
  console.info("taskpool execute res is:" + res);
});
taskpool.execute(taskGroup2).then((res: Array<Object>) => {
  console.info("taskpool execute res is:" + res);
});
```

#### taskpool.executeDelayed11+

executeDelayed(delayTime: number, task: Task, priority?: Priority): Promise<Object>

延时执行任务。当前执行模式可以设置任务优先级，并且可以尝试调用cancel取消任务。该任务不能是任务组任务、串行队列任务、异步队列任务或周期任务。如果任务不是长时任务，可以多次调用executeDelayed执行；如果是长时任务，则仅支持执行一次。使用Promise异步回调。

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数：**

参数名类型必填说明delayTimenumber是延时时间。单位为ms。delayTime值必须要大于等于0。task[Task](#ZH-CN_TOPIC_0000002497444774__task)是需要延时执行的任务。priority[Priority](#ZH-CN_TOPIC_0000002497444774__priority)否延时执行的任务的优先级，该参数默认值为taskpool.Priority.MEDIUM。

**返回值：**

类型说明Promise<Object>Promise对象，返回任务函数的执行结果。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.10200006An exception occurred during serialization.10200014The function is not marked as concurrent.10200028The delayTime is less than zero.10200051The periodic task cannot be executed again.10200057The task cannot be executed by two APIs.

**示例：**

```ets
// import BusinessError
import { BusinessError } from '@kit.BasicServicesKit';

@Concurrent
function printArgs(args: number): void {
    console.info("printArgs: " + args);
}

let t: number = Date.now();
console.info("taskpool start time is: " + t);
let task: taskpool.Task = new taskpool.Task(printArgs, 100); // 100: test number
taskpool.executeDelayed(1000, task).then(() => { // 1000: delayTime is 1000ms
  console.info("taskpool execute success");
}).catch((e: BusinessError) => {
  console.error(`taskpool execute: Code: ${e.code}, message: ${e.message}`);
})
```

#### taskpool.executeDelayed13+

executeDelayed<A extends Array<Object>, R>(delayTime: number, task: GenericsTask<A, R>, priority?: Priority): Promise<R>

延时执行泛型任务，不校验任务的参数类型和返回值类型。使用Promise异步回调。

executeDelayed任务的校验是结合new GenericsTask一起用的，参数、返回值类型需与new GenericsTask中的类型保持一致。

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**参数：**

参数名类型必填说明delayTimenumber是延时时间。单位为ms。delayTime值必须要大于等于0。task[GenericsTask<A, R>](#ZH-CN_TOPIC_0000002497444774__genericstask13)是需要延时执行的泛型任务。priority[Priority](#ZH-CN_TOPIC_0000002497444774__priority)否延时执行的任务的优先级，默认值为taskpool.Priority.MEDIUM。

**返回值：**

类型说明Promise<R>Promise对象，返回任务函数的执行结果。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Incorrect parameter types; 2.Parameter verification failed.10200028The delayTime is less than zero.10200051The periodic task cannot be executed again.10200057The task cannot be executed by two APIs.

**示例：**

```ets
// import BusinessError
import { BusinessError } from '@kit.BasicServicesKit'

@Concurrent
function printArgs(args: number): string {
    console.info("printArgs: " + args);
    return "success";
}

let task: taskpool.Task = new taskpool.GenericsTask<[number], string>(printArgs, 100); // 100: test number
taskpool.executeDelayed<[number], string>(1000, task).then((res: string) => { // 1000: delayTime is 1000ms
  console.info("taskpool execute success");
}).catch((e: BusinessError) => {
  console.error(`taskpool execute: Code: ${e.code}, message: ${e.message}`);
})
```

#### taskpool.executePeriodically12+

executePeriodically(period: number, task: Task, priority?: Priority): void

周期任务每隔period时长执行一次。当前执行模式支持设置任务优先级，并可以通过调用cancel取消周期任务的执行。周期任务不能是任务组任务、串行队列任务或异步队列任务，不能再次调用执行接口，且执行的任务不能拥有依赖关系。

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

参数名类型必填说明periodnumber是周期时长。单位为ms。period值必须要大于等于0。task[Task](#ZH-CN_TOPIC_0000002497444774__task)是需要周期执行的任务。priority[Priority](#ZH-CN_TOPIC_0000002497444774__priority)否周期执行的任务的优先级，该参数默认值为taskpool.Priority.MEDIUM。

**错误码：**

以下错误码的详细介绍，请参见[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.10200006An exception occurred during serialization.10200014The function is not marked as concurrent.10200028The period is less than zero.10200050The concurrent task has been executed and cannot be executed periodically.10200057The task cannot be executed by two APIs.

**示例：**

```ets
@Concurrent
function printArgs(args: number): void {
  console.info("printArgs: " + args);
}

@Concurrent
function testExecutePeriodically(args: number): void {
  let t = Date.now();
  while ((Date.now() - t) < args) {
    continue;
  }
  taskpool.Task.sendData(args); // 向宿主线程发送消息
}

function printResult(data: number): void {
  console.info("taskpool: data is: " + data);
}

function taskpoolTest() {
  try {
    let task: taskpool.Task = new taskpool.Task(printArgs, 100); // 100: test number
    taskpool.executePeriodically(1000, task); // 1000: period is 1000ms
  } catch (e) {
    console.error(`taskpool execute-1: Code: ${e.code}, message: ${e.message}`);
  }

  try {
    let periodicTask: taskpool.Task = new taskpool.Task(testExecutePeriodically, 200); // 200: test number
    periodicTask.onReceiveData(printResult);
    taskpool.executePeriodically(1000, periodicTask); // 1000: period is 1000ms
  } catch (e) {
    console.error(`taskpool execute-2: Code: ${e.code}, message: ${e.message}`);
  }
}

taskpoolTest();
```

#### taskpool.executePeriodically13+

executePeriodically<A extends Array<Object>, R>(period: number, task: GenericsTask<A, R>, priority?: Priority): void

周期执行泛型任务，每隔period时长执行一次。不校验任务的参数类型和返回值类型。

executePeriodically任务的校验是结合new GenericsTask一起用的，参数、返回值类型需与new GenericsTask中的类型保持一致。

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**参数：**

参数名类型必填说明periodnumber是周期时长。单位为ms。period值必须要大于等于0。task[GenericsTask<A, R>](#ZH-CN_TOPIC_0000002497444774__genericstask13)是需要周期执行的泛型任务。priority[Priority](#ZH-CN_TOPIC_0000002497444774__priority)否周期执行的任务的优先级，该参数默认值为taskpool.Priority.MEDIUM。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Incorrect parameter types; 2.Parameter verification failed.10200006An exception occurred during serialization.10200014The function is not marked as concurrent.10200028The period is less than zero.10200050The concurrent task has been executed and cannot be executed periodically.10200057The task cannot be executed by two APIs.

**示例：**

```ets
@Concurrent
function printArgs(args: number): void {
  console.info("printArgs: " + args);
}

@Concurrent
function testExecutePeriodically(args: number): void {
  let t = Date.now();
  while ((Date.now() - t) < args) {
    continue;
  }
  taskpool.Task.sendData(args); // 向宿主线程发送消息
}

function printResult(data: number): void {
  console.info("taskpool: data is: " + data);
}

function taskpoolTest() {
  try {
    let task: taskpool.Task = new taskpool.GenericsTask<[number], void>(printArgs, 100); // 100: test number
    taskpool.executePeriodically<[number], void>(1000, task); // 1000: period is 1000ms
  } catch (e) {
    console.error(`taskpool execute-1: Code: ${e.code}, message: ${e.message}`);
  }

  try {
    let periodicTask: taskpool.Task = new taskpool.GenericsTask<[number], void>(testExecutePeriodically, 200); // 200: test number
    periodicTask.onReceiveData(printResult);
    taskpool.executePeriodically<[number], void>(1000, periodicTask); // 1000: period is 1000ms
  } catch (e) {
    console.error(`taskpool execute-2: Code: ${e.code}, message: ${e.message}`);
  }
}

taskpoolTest();
```

#### taskpool.cancel

cancel(task: Task): void

取消任务池中的任务。当任务在taskpool等待队列中，取消该任务后该任务将不再执行，并返回任务被取消的异常；当任务已经在taskpool工作线程执行，取消该任务并不影响任务继续执行，执行结果在catch分支返回，搭配isCanceled使用可以对任务取消行为作出响应。taskpool.cancel对其之前的taskpool.execute、taskpool.executeDelayed或taskpool.executePeriodically生效。

从API version 20开始，支持在执行cancel操作后，在catch分支里使用BusinessError<[taskpool.TaskResult](#ZH-CN_TOPIC_0000002497444774__taskresult20)>的泛型标记，来获取任务中抛出的异常信息或最终的执行结果。

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数：**

参数名类型必填说明task[Task](#ZH-CN_TOPIC_0000002497444774__task)是需要取消执行的任务。

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息10200015The task to cancel does not exist.10200055The asyncRunner task has been canceled.

从API version 10开始，此接口调用时不再涉及上报错误码10200016。

**正在执行的任务取消示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

@Concurrent
function inspectStatus(arg: number): number {
  // 第一次检查任务是否已经取消并作出响应
  if (taskpool.Task.isCanceled()) {
    console.info("task has been canceled before 2s sleep.");
    return arg + 2;
  }
  // 2s sleep
  let t: number = Date.now();
  while (Date.now() - t < 2000) {
    continue;
  }
  // 第二次检查任务是否已经取消并作出响应
  if (taskpool.Task.isCanceled()) {
    console.info("task has been canceled after 2s sleep.");
    return arg + 3;
  }
  return arg + 1;
}

function concurrentFunc() {
  let task1: taskpool.Task = new taskpool.Task(inspectStatus, 100); // 100: test number
  let task2: taskpool.Task = new taskpool.Task(inspectStatus, 200); // 200: test number
  let task3: taskpool.Task = new taskpool.Task(inspectStatus, 300); // 300: test number
  let task4: taskpool.Task = new taskpool.Task(inspectStatus, 400); // 400: test number
  let task5: taskpool.Task = new taskpool.Task(inspectStatus, 500); // 500: test number
  let task6: taskpool.Task = new taskpool.Task(inspectStatus, 600); // 600: test number
  taskpool.execute(task1).then((res: Object) => {
    console.info("taskpool test result: " + res);
  }).catch((err: BusinessError) => {
    console.error("taskpool catch err: " + err.message);
  });
  taskpool.execute(task2);
  taskpool.execute(task3);
  taskpool.execute(task4);
  taskpool.execute(task5);
  taskpool.execute(task6);
  // 1s后取消task
  setTimeout(() => {
    try {
      taskpool.cancel(task1);
    } catch (e) {
      console.error(`taskpool: cancel error code: ${e.code}, info: ${e.message}`);
    }
  }, 1000);
}

concurrentFunc();
```

#### taskpool.cancel10+

cancel(group: TaskGroup): void

取消任务池中的任务组。如果任务组中的任务未全部执行结束，返回undefined作为任务组结果。

从API version 20开始，支持在执行cancel操作后，在catch分支里使用BusinessError<[taskpool.TaskResult](#ZH-CN_TOPIC_0000002497444774__taskresult20)>的泛型标记，来获取任务中抛出的异常信息或最终的执行结果。

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数：**

参数名类型必填说明group[TaskGroup](#ZH-CN_TOPIC_0000002497444774__taskgroup10)是需要取消执行的任务组。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.10200018The task group to cancel does not exist.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

@Concurrent
function printArgs(args: number): number {
  let t: number = Date.now();
  while (Date.now() - t < 2000) {
    continue;
  }
  console.info("printArgs: " + args);
  return args;
}

function concurrentFunc() {
  let taskGroup1: taskpool.TaskGroup = new taskpool.TaskGroup();
  taskGroup1.addTask(printArgs, 10); // 10: test number
  let taskGroup2: taskpool.TaskGroup = new taskpool.TaskGroup();
  taskGroup2.addTask(printArgs, 100); // 100: test number
  taskpool.execute(taskGroup1).then((res: Array<Object>) => {
    console.info("taskGroup1 res is:" + res);
  });
  taskpool.execute(taskGroup2).then((res: Array<Object>) => {
    console.info("taskGroup2 res is:" + res);
  }).catch((err: BusinessError) => {
    console.error("taskGroup2 catch err: " + err.message);
  });
  setTimeout(() => {
    try {
      taskpool.cancel(taskGroup2);
    } catch (e) {
      console.error(`taskpool: cancel error code: ${e.code}, info: ${e.message}`);
    }
  }, 1000);
}

concurrentFunc();
```

#### taskpool.cancel18+

cancel(taskId: number): void

通过任务ID取消任务池中的任务。如果任务在taskpool等待队列中，取消后任务将不再执行，并返回任务取消的异常。如果任务已在taskpool工作线程中执行，取消不影响任务继续执行，执行结果在catch分支返回。使用isCanceled可以对任务取消行为作出响应。taskpool.cancel对其之前的taskpool.execute或taskpool.executeDelayed生效。在其他线程调用taskpool.cancel时，需注意其行为是异步的，可能影响之后的taskpool.execute或taskpool.executeDelayed。

从API version 20开始，支持在执行cancel操作后，在catch分支里使用BusinessError<[taskpool.TaskResult](#ZH-CN_TOPIC_0000002497444774__taskresult20)>的泛型标记。这可以用来获取任务中抛出的异常信息或最终的执行结果。

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**参数：**

参数名类型必填说明taskIdnumber是需要取消执行的任务的ID。

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息10200015The task to cancel does not exist.10200055The asyncRunner task has been canceled.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

@Concurrent
function printArgs(args: number): number {
  let t: number = Date.now();
  while (Date.now() - t < 2000) {
    continue;
  }
  if (taskpool.Task.isCanceled()) {
    console.info("task has been canceled after 2s sleep.");
    return args + 1;
  }
  console.info("printArgs: " + args);
  return args;
}

@Concurrent
function cancelFunction(taskId: number) {
  try {
    taskpool.cancel(taskId);
  } catch (e) {
    console.error(`taskpool: cancel error code: ${e.code}, info: ${e.message}`);
  }
}

function concurrentFunc() {
  let task = new taskpool.Task(printArgs, 100); // 100: test number
  taskpool.execute(task).catch((err: BusinessError) => {
    console.error("taskpool catch err: " + err.message);
  });
  setTimeout(() => {
    let cancelTask = new taskpool.Task(cancelFunction, task.taskId);
    taskpool.execute(cancelTask);
  }, 1000);
}

concurrentFunc();
```

#### taskpool.terminateTask12+

terminateTask(longTask: LongTask): void

中止任务池中的长时任务，在长时任务执行完成后调用。中止后，执行长时任务的线程可能会被回收。

**系统能力：** SystemCapability.Utils.Lang

**元服务API**： 从API version 12开始，该接口支持在元服务中使用。

**参数：**

参数名类型必填说明longTask[LongTask](#ZH-CN_TOPIC_0000002497444774__longtask12)是需要中止的长时任务。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

**示例：**

```ets
@Concurrent
function longTask(arg: number): number {
  let t: number = Date.now();
  while (Date.now() - t < arg) {
    continue;
  }
  console.info("longTask has been executed.");
  return arg;
}

function concurrentFunc() {
  let task1: taskpool.LongTask = new taskpool.LongTask(longTask, 1000); // 1000: sleep time
  taskpool.execute(task1).then((res: Object) => {
    taskpool.terminateTask(task1);
    console.info("taskpool longTask result: " + res);
  });
}

concurrentFunc();
```

#### taskpool.isConcurrent12+

isConcurrent(func: Function): boolean

检查函数是否为并发函数。

**系统能力：** SystemCapability.Utils.Lang

**元服务API**： 从API version 12开始，该接口支持在元服务中使用。

**参数：**

参数名类型必填说明funcFunction是需要检查的函数。

**返回值：**

类型说明boolean如果被检查函数标注了[@Concurrent装饰器](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/taskpool-introduction#concurrent装饰器)，则返回true，否则返回false。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

**示例：**

```ets
@Concurrent
function test() {}

let result: Boolean = taskpool.isConcurrent(test);
console.info("result is: " + result);
```

#### taskpool.getTaskPoolInfo10+

getTaskPoolInfo(): TaskPoolInfo

获取任务池的线程信息和任务信息。

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**返回值：**

类型说明[TaskPoolInfo](#ZH-CN_TOPIC_0000002497444774__taskpoolinfo10)任务池的内部信息。

**示例：**

```ets
let taskpoolInfo: taskpool.TaskPoolInfo = taskpool.getTaskPoolInfo();
```

#### taskpool.getTask22+

getTask(taskId: number, taskName?: string): Task | undefined

通过taskId或taskId与taskName获取对应的Task实例。

- 如果传入的taskId查询不到对应的Task实例，则会返回undefined；
- 如果传入的taskId能够查询到对应的Task实例，但是调用getTask方法的线程和创建Task实例的线程不一致，则会返回undefined；
- 如果传入了taskId和taskName，通过taskId查询到的Task实例的name和传入的taskName不一致，则会返回undefined。

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**参数：**

参数名类型必填说明taskIdnumber是任务ID。taskNamestring否任务名称。默认值为undefined。

**返回值：**

类型说明[Task](#ZH-CN_TOPIC_0000002497444774__task) | undefined返回Task实例；当情况异常时，返回undefined，具体可见上文说明。

**示例：**

```ets
import { taskpool } from '@kit.ArkTS';

@Concurrent
function addNum(num1: number, num2: number) {
  return num1 + num2;
}

function checkTask() {
  try {
    taskpool.getTask(null);
  } catch (e) {
    console.error("error:" + e);
    // error:BusinessError: Parameter error. The input parameters are invalid, the type of the first param must be number.
  }

  let task1:taskpool.Task = new taskpool.Task("addNum", addNum, 1, 2);
  let task2:taskpool.Task | undefined = taskpool.getTask(task1.taskId, "addNum"); // task2 is not undefined
  let task3:taskpool.Task | undefined = taskpool.getTask(task1.taskId, "add"); // task3 is undefined
  let task4:taskpool.Task | undefined = taskpool.getTask(0); // task4 is undefined
}

function dealTask() {
  let task1:taskpool.Task = new taskpool.Task(addNum, 1, 2);
  let task2:taskpool.Task | undefined = taskpool.getTask(task1.taskId);
  if (task2 === undefined) {
    return;
  }

  taskpool.execute(task2).then((result) => {
    console.info("task2 result: " + result); // task2 result: 3
  })
}
```

#### Priority

表示所创建任务（Task）执行时的优先级。工作线程优先级跟随任务优先级更新，对应关系参考[QoS等级定义](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/qos-guidelines#qos等级定义)。

**系统能力：** SystemCapability.Utils.Lang

名称值说明HIGH0

任务为高优先级。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

MEDIUM1

任务为中优先级。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

LOW2

任务为低优先级。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

IDLE12+3

任务为后台任务。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**示例：**

```ets
@Concurrent
function printArgs(args: number): number {
  let t: number = Date.now();
  while (Date.now() - t < 1000) { // 1000: delay 1s
    continue;
  }
  console.info("printArgs: " + args);
  return args;
}

let allCount = 100; // 100: test number
let taskArray: Array<taskpool.Task> = [];
// 创建400个任务并添加至taskArray
for (let i: number = 0; i < allCount; i++) {
  let task1: taskpool.Task = new taskpool.Task(printArgs, i);
  taskArray.push(task1);
  let task2: taskpool.Task = new taskpool.Task(printArgs, i * 10); // 10: test number
  taskArray.push(task2);
  let task3: taskpool.Task = new taskpool.Task(printArgs, i * 100); // 100: test number
  taskArray.push(task3);
  let task4: taskpool.Task = new taskpool.Task(printArgs, i * 1000); // 1000: test number
  taskArray.push(task4);
}

// 从taskArray中获取不同的任务并给定不同优先级执行
for (let i: number = 0; i < taskArray.length; i+=4) { // 4: 每次执行4个任务，循环取任务时需后移4项，确保执行的是不同的任务
  taskpool.execute(taskArray[i], taskpool.Priority.HIGH);
  taskpool.execute(taskArray[i + 1], taskpool.Priority.LOW);
  taskpool.execute(taskArray[i + 2], taskpool.Priority.MEDIUM);
  taskpool.execute(taskArray[i + 3], taskpool.Priority.IDLE);
}
```

#### Task

任务可以多次执行，也可以放入任务组、串行队列或异步队列执行，还支持添加依赖关系。

#### 属性

**系统能力：** SystemCapability.Utils.Lang

名称类型只读可选说明functionFunction否否

创建任务时需要传入的函数，支持的函数返回值类型请查[序列化支持类型](#ZH-CN_TOPIC_0000002497444774__序列化支持类型)。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

argumentsObject[]否是

创建任务传入函数所需的参数，支持的参数类型请查[序列化支持类型](#ZH-CN_TOPIC_0000002497444774__序列化支持类型)。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

name11+string否否

创建任务时指定的任务名称。不建议修改此值。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

taskId18+number否否

任务的ID。任务的标识符，系统默认提供全局唯一值，不建议修改此值。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

totalDuration11+number否否

执行任务总耗时。单位为ms。不建议修改此值。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

ioDuration11+number否否

执行任务异步IO耗时。单位为ms。不建议修改此值。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

cpuDuration11+number否否

执行任务CPU耗时。单位为ms。不建议修改此值。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

#### constructor

constructor(func: Function, ...args: Object[])

Task的构造函数。

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数：**

参数名类型必填说明funcFunction是执行的逻辑需要传入函数，必须使用[@Concurrent装饰器](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/taskpool-introduction#concurrent装饰器)装饰，支持的函数返回值类型请查[序列化支持类型](#ZH-CN_TOPIC_0000002497444774__序列化支持类型)。argsObject[]否任务执行传入函数的入参，支持的参数类型请查[序列化支持类型](#ZH-CN_TOPIC_0000002497444774__序列化支持类型)。默认值为undefined。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息401The input parameters are invalid.10200014The function is not marked as concurrent.

**示例：**

```ets
@Concurrent
function printArgs(args: number): number {
  console.info("printArgs: " + args);
  return args;
}

let task: taskpool.Task = new taskpool.Task(printArgs, "this is my first Task");
```

#### constructor11+

constructor(name: string, func: Function, ...args: Object[])

Task的构造函数用于创建任务，并可指定任务名称。

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数：**

参数名类型必填说明namestring是任务名称。funcFunction是执行的逻辑需要传入函数，必须使用[@Concurrent装饰器](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/taskpool-introduction#concurrent装饰器)装饰，支持的函数返回值类型请查[序列化支持类型](#ZH-CN_TOPIC_0000002497444774__序列化支持类型)。argsObject[]否任务执行时传入函数的参数。支持的类型请参考[序列化支持类型](#ZH-CN_TOPIC_0000002497444774__序列化支持类型)。默认值为undefined。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息401The input parameters are invalid.10200014The function is not marked as concurrent.

**示例：**

```ets
@Concurrent
function printArgs(args: string): string {
  console.info("printArgs: " + args);
  return args;
}

let taskName: string = "taskName";
let task: taskpool.Task = new taskpool.Task(taskName, printArgs, "this is my first Task");
let name: string = task.name;
```

#### isCanceled10+

static isCanceled(): boolean

检查当前正在运行的任务是否已取消。使用此方法前，需要先创建一个Task对象。

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**返回值：**

类型说明boolean如果当前正在运行的任务被取消返回true，否则返回false。

**示例：**

```ets
@Concurrent
function inspectStatus(arg: number): number {
    // do something
    if (taskpool.Task.isCanceled()) {
      console.info("task has been canceled.");
      // do something
      return arg + 1;
    }
    // do something
    return arg;
}
```

isCanceled方法需要和taskpool.cancel方法搭配使用，如果不调用cancel方法，isCanceled方法默认返回false。

**示例：**

```ets
@Concurrent
function inspectStatus(arg: number): number {
  // 第一次检查任务是否已经取消并作出响应
  if (taskpool.Task.isCanceled()) {
    console.info("task has been canceled before 2s sleep.");
    return arg + 2;
  }
  // 延时2s
  let t: number = Date.now();
  while (Date.now() - t < 2000) {
    continue;
  }
  // 第二次检查任务是否已经取消并作出响应
  if (taskpool.Task.isCanceled()) {
    console.info("task has been canceled after 2s sleep.");
    return arg + 3;
  }
  return arg + 1;
}

let task: taskpool.Task = new taskpool.Task(inspectStatus, 100); // 100: test number
taskpool.execute(task).then((res: Object) => {
  console.info("taskpool test result: " + res);
}).catch((err: string) => {
  console.error("taskpool test occur error: " + err);
});
// 不调用cancel，isCanceled()默认返回false，task执行的结果为101
```

#### setTransferList10+

setTransferList(transfer?: ArrayBuffer[]): void

设置任务的传输列表。使用该方法前需要先构造Task。不调用该接口，则传给任务的数据中的ArrayBuffer默认transfer转移。

此接口可以设置任务池中ArrayBuffer的transfer列表，transfer列表中的ArrayBuffer对象在传输时不会复制buffer内容到工作线程而是转移buffer控制权至工作线程，传输后当前的ArrayBuffer失效。若ArrayBuffer为空，则不会transfer转移。

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数：**

参数名类型必填说明transferArrayBuffer[]否可传输对象是ArrayBuffer的实例对象，默认为空数组。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Incorrect parameter types; 2. Parameter verification failed.10200029An ArrayBuffer cannot be set as both a transfer list and a clone list.

**示例：**

```ets
@Concurrent
function testTransfer(arg1: ArrayBuffer, arg2: ArrayBuffer): number {
  console.info("testTransfer arg1 byteLength: " + arg1.byteLength);
  console.info("testTransfer arg2 byteLength: " + arg2.byteLength);
  return 100;
}

let buffer: ArrayBuffer = new ArrayBuffer(8);
let view: Uint8Array = new Uint8Array(buffer);
let buffer1: ArrayBuffer = new ArrayBuffer(16);
let view1: Uint8Array = new Uint8Array(buffer1);

console.info("testTransfer view byteLength: " + view.byteLength);
console.info("testTransfer view1 byteLength: " + view1.byteLength);
// 执行结果为：
// testTransfer view byteLength: 8
// testTransfer view1 byteLength: 16

let task: taskpool.Task = new taskpool.Task(testTransfer, view, view1);
task.setTransferList([view.buffer, view1.buffer]);
taskpool.execute(task).then((res: Object) => {
  console.info("test result: " + res);
}).catch((e: string) => {
  console.error("test catch: " + e);
})
console.info("testTransfer view2 byteLength: " + view.byteLength);
console.info("testTransfer view3 byteLength: " + view1.byteLength);
// 经过transfer转移之后值为0，执行结果为：
// testTransfer view2 byteLength: 0
// testTransfer view3 byteLength: 0
```

#### setCloneList11+

setCloneList(cloneList: Object[] | ArrayBuffer[]): void

设置任务的拷贝列表。在使用该方法前，需先构造Task对象。

需搭配[@Sendable装饰器](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-sendable#sendable装饰器)使用，否则会抛异常。建议开发者使用该装饰器以避免异常。

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数：**

参数名类型必填说明cloneListObject[] | ArrayBuffer[]是

- 传入数组的类型必须为[Sendable支持的数据类型](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-sendable#sendable支持的数据类型)或ArrayBuffer。

- 所有传入cloneList的对象持有的[Sendable class](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-sendable#sendable-class)实例或ArrayBuffer类型对象，在线程间传输的行为都会变成拷贝传递，即修改传输后的对象不会对原有对象产生任何影响。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.10200029An ArrayBuffer cannot be set as both a transfer list and a clone list.

**示例：**

```ets
// sendable.ets
// 定义两个Sendable class：BaseClass及其子类DeriveClass
@Sendable
export class BaseClass {
  private str: string = "sendable: BaseClass";
  static num :number = 10;
  str1: string = "sendable: this is BaseClass's string";
  num1: number = 5;
  isDone1: boolean = false;

  private fibonacciRecursive(n: number): number {
    if (n <= 1) {
      return n;
    } else {
      return this.fibonacciRecursive(n - 1) + this.fibonacciRecursive(n - 2);
    }
  }

  private privateFunc(num: number): number{
    let res: number = this.fibonacciRecursive(num);
    console.info("sendable: BaseClass privateFunc res is: " + res);
    return res;
  }

  publicFunc(num: number): number {
    return this.privateFunc(num);
  }

  get GetNum(): number {
    return this.num1;
  }
  set SetNum(num: number) {
    this.num1 = num;
  }

  constructor() {
    console.info(this.str);
    this.isDone1 = true;
  }
}

@Sendable
export class DeriveClass extends BaseClass {
  name: string = "sendable: this is DeriveClass";
  printName() {
    console.info(this.name);
  }
  constructor() {
    super();
  }
}
```

```ets
// index.ets
// 宿主线程（这里的宿主线程为UI主线程）调用taskpool，在taskpool线程中调用BaseClass和DeriveClass的方法、访问对应属性
import { taskpool } from '@kit.ArkTS';
import { BusinessError } from '@kit.BasicServicesKit';
import { BaseClass, DeriveClass } from './sendable';

@Concurrent
function testFunc(arr: Array<BaseClass>, num: number): number {
  let baseInstance1 = arr[0];
  console.info("sendable: str1 is: " + baseInstance1.str1);
  baseInstance1.SetNum = 100;
  console.info("sendable: num1 is: " + baseInstance1.GetNum);
  console.info("sendable: isDone1 is: " + baseInstance1.isDone1);
  // 获取斐波那契数列第num项的结果
  let res: number = baseInstance1.publicFunc(num);
  return res;
}

@Concurrent
function printLog(arr: Array<DeriveClass>): void {
  let deriveInstance = arr[0];
  deriveInstance.printName();
}

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
        Button() {
          Text("TaskPool Test");
        }.onClick(() => {
          // task1访问调用BaseClass.str1/BaseClass.SetNum/BaseClass.GetNum/BaseClass.isDone1/BaseClass.publicFunc
          let baseInstance1: BaseClass = new BaseClass();
          let array1 = new Array<BaseClass>();
          array1.push(baseInstance1);
          let task1 = new taskpool.Task(testFunc, array1, 10);
          task1.setCloneList(array1);
          taskpool.execute(task1).then((res: Object) => {
            console.info("sendable: task1 res is: " + res);
          }).catch((e:BusinessError) => {
            console.error(`sendable: task1 execute Code is ${e.code}, message is ${e.message}`);
          })

          // task2调用DeriveClass.printName
          let deriveInstance: DeriveClass = new DeriveClass();
          let array2 = new Array<DeriveClass>();
          array2.push(deriveInstance);
          let task2 = new taskpool.Task(printLog, array2);
          task2.setCloneList(array2);
          taskpool.execute(task2).then(() => {
            console.info("sendable: task2 execute success");
          }).catch((e:BusinessError) => {
            console.error(`sendable: task2 execute Code is ${e.code}, message is ${e.message}`);
          })
        })
        .height('15%')
        .width('30%')
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

#### sendData11+

static sendData(...args: Object[]): void

任务执行过程中向宿主线程发送消息并触发回调。使用此方法前需构造Task。

- 该接口应在taskpool的线程中调用。
- 避免在回调函数中调用该方法，否则可能导致消息无法传递到宿主线程。
- 避免在异步函数中调用该方法，否则可能导致消息无法传递到宿主线程。如果在异步函数中使用，则需要使用await来确保该异步函数在任务中同步执行完成。
- 调用该接口时，请确保处理数据的回调函数已在宿主线程注册。

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数：**

参数名类型必填说明argsObject[]否可传输对象默认转移，作为回调函数的参数。支持的参数类型请参见[序列化支持类型](#ZH-CN_TOPIC_0000002497444774__序列化支持类型)，默认值为undefined。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息401The input parameters are invalid.10200006An exception occurred during serialization.10200022The function is not called in the TaskPool thread.10200023The function is not called in the concurrent function.10200024The callback is not registered on the host side.

**示例：**

```ets
@Concurrent
function sendDataTest(num: number): number {
  let res: number = num * 10;
  taskpool.Task.sendData(res);
  return num;
}

function printLog(data: number): void {
  console.info("taskpool: data is: " + data);
}

async function taskpoolTest(): Promise<void> {
  try {
    let task: taskpool.Task = new taskpool.Task(sendDataTest, 1);
    task.onReceiveData(printLog);
    await taskpool.execute(task);
  } catch (e) {
    console.error(`taskpool: error code: ${e.code}, info: ${e.message}`);
  }
}

taskpoolTest();
```

```ets
// 异步函数中调用该方法
@Concurrent
async function sendDataTest(num: number) {
  let func = async () => {
    let asyncSleep = async (time: number): Promise<Object> => {
      return new Promise(resolve => setTimeout(resolve, time));
    }
    await asyncSleep(10000);
    let res: number = num * 10;
    taskpool.Task.sendData(res);
  }
  await func(); // 需要使用await来确保该异步函数在任务中同步执行完成。
}

function taskpoolTest() {
  try {
    let task: taskpool.Task = new taskpool.Task(sendDataTest, 10);
    task.onReceiveData((data: string) => {
      console.info("taskpool: data is: " + data);
    });
    taskpool.execute(task);
  } catch (e) {
    console.error(`taskpool: error code: ${e.code}, info: ${e.message}`);
  }
}

taskpoolTest();
```

#### onReceiveData11+

onReceiveData(callback?: Function): void

为任务注册回调函数，接收并处理任务池工作线程的数据。使用此方法前，需构造Task。

不支持为同一任务定义多种回调函数。如果多次赋值，只有最后一次赋值的回调函数会生效。

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数：**

参数名类型必填说明callbackFunction否处理数据的回调函数，发送到宿主线程的数据将会作为入参传入该回调函数。不传参可以取消注册的回调函数。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Incorrect parameter types; 2. Parameter verification failed.

**示例：**

```ets
@Concurrent
function ConcurrentFunc(num: number): number {
  let res: number = num * 10;
  taskpool.Task.sendData(res);
  return num;
}

function printLog(data: number): void {
  console.info("taskpool: data is: " + data);
}

async function testFunc(): Promise<void> {
  try {
    let task: taskpool.Task = new taskpool.Task(ConcurrentFunc, 1);
    task.onReceiveData(printLog);
    await taskpool.execute(task);
  } catch (e) {
    console.error(`taskpool: error code: ${e.code}, info: ${e.message}`);
  }
}

testFunc();
```

#### addDependency11+

addDependency(...tasks: Task[]): void

为当前任务添加对其他任务的依赖。使用该方法前需先构造Task。该任务和被依赖的任务不能是任务组任务、串行队列任务、异步队列任务、已执行任务或周期任务。存在依赖关系的任务（依赖其他任务的任务或被依赖的任务）执行后不可再次执行。

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数：**

参数名类型必填说明tasks[Task](#ZH-CN_TOPIC_0000002497444774__task)[]否被依赖的任务数组。默认值为undefined。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.10200026There is a circular dependency.10200052The periodic task cannot have a dependency.10200056The task has been executed by the AsyncRunner.

**示例：**

```ets
@Concurrent
function delay(args: number): number {
  let t: number = Date.now();
  while ((Date.now() - t) < 1000) {
    continue;
  }
  return args;
}

let task1:taskpool.Task = new taskpool.Task(delay, 100);
let task2:taskpool.Task = new taskpool.Task(delay, 200);
let task3:taskpool.Task = new taskpool.Task(delay, 200);

console.info("dependency: add dependency start");
task1.addDependency(task2);
task2.addDependency(task3);
console.info("dependency: add dependency end");

console.info("dependency: start execute second");
taskpool.execute(task1).then(() => {
  console.info("dependency: second task1 success");
})
taskpool.execute(task2).then(() => {
  console.info("dependency: second task2 success");
})
taskpool.execute(task3).then(() => {
  console.info("dependency: second task3 success");
})
```

#### removeDependency11+

removeDependency(...tasks: Task[]): void

删除当前任务对其他任务的依赖。在使用该方法之前，需要先构造Task对象。

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数：**

参数名类型必填说明tasks[Task](#ZH-CN_TOPIC_0000002497444774__task)[]否被依赖的任务数组。默认值为undefined。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.10200027The dependency does not exist.10200052The periodic task cannot have a dependency.10200056The task has been executed by the AsyncRunner.

**示例：**

```ets
@Concurrent
function delay(args: number): number {
  let t: number = Date.now();
  while ((Date.now() - t) < 1000) {
    continue;
  }
  return args;
}

let task1:taskpool.Task = new taskpool.Task(delay, 100);
let task2:taskpool.Task = new taskpool.Task(delay, 200);
let task3:taskpool.Task = new taskpool.Task(delay, 200);

console.info("dependency: add dependency start");
task1.addDependency(task2);
task2.addDependency(task3);
console.info("dependency: add dependency end");
console.info("dependency: remove dependency start");
task1.removeDependency(task2);
task2.removeDependency(task3);
console.info("dependency: remove dependency end");

console.info("dependency: start execute");
taskpool.execute(task1).then(() => {
  console.info("dependency: task1 success");
})
taskpool.execute(task2).then(() => {
  console.info("dependency: task2 success");
})
taskpool.execute(task3).then(() => {
  console.info("dependency: task3 success");
})
```

#### onEnqueued12+

onEnqueued(callback: CallbackFunction): void

注册回调函数，任务入队时将调用该函数。若任务执行前未注册回调函数，将抛出异常。

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

参数名类型必填说明callback[CallbackFunction](#ZH-CN_TOPIC_0000002497444774__callbackfunction12)是需注册的回调函数。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息401The input parameters are invalid.10200034The executed task does not support the registration of listeners.

**示例：**

```ets
import { taskpool } from '@kit.ArkTS';

@Concurrent
function delay(args: number): number {
  let t: number = Date.now();
  while ((Date.now() - t) < 1000) {
      continue;
  }
  return args;
}

let task: taskpool.Task = new taskpool.Task(delay, 1);
task.onEnqueued(() => {
  console.info("taskpool: onEnqueued");
});
taskpool.execute(task).then(() => {
  console.info("taskpool: execute task success");
});
```

#### onStartExecution12+

onStartExecution(callback: CallbackFunction): void

注册回调函数，任务执行前将调用该函数。若任务执行前未注册回调函数，将抛出异常。

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

参数名类型必填说明callback[CallbackFunction](#ZH-CN_TOPIC_0000002497444774__callbackfunction12)是需注册的回调函数。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息401The input parameters are invalid.10200034The executed task does not support the registration of listeners.

**示例：**

```ets
import { taskpool } from '@kit.ArkTS';

@Concurrent
function delay(args: number): number {
  let t: number = Date.now();
  while ((Date.now() - t) < 1000) {
      continue;
  }
  return args;
}

let task: taskpool.Task = new taskpool.Task(delay, 1);
task.onStartExecution(() => {
  console.info("taskpool: onStartExecution");
});
taskpool.execute(task).then(() => {
  console.info("taskpool: execute task success");
});
```

#### onExecutionFailed12+

onExecutionFailed(callback: CallbackFunctionWithError): void

注册一个回调函数，并在任务执行失败时调用它（周期任务不支持）。需在任务执行前注册，否则会抛异常。

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

参数名类型必填说明callback[CallbackFunctionWithError](#ZH-CN_TOPIC_0000002497444774__callbackfunctionwitherror12)是需注册的回调函数。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息401The input parameters are invalid.10200034The executed task does not support the registration of listeners.

**示例：**

```ets
import { taskpool } from '@kit.ArkTS';
import { BusinessError } from '@kit.BasicServicesKit';
import { HashMap } from '@kit.ArkTS';

@Concurrent
function test(args: number) {
  let t = Date.now();
  while ((Date.now() - t) < 100) {
    continue;
  }
  let hashMap1: HashMap<string, number> = new HashMap();
  hashMap1.set('a', args);
  return hashMap1;
}

let task2 = new taskpool.Task(test, 1);
task2.onExecutionFailed((e: Error) => {
  console.info("taskpool: onExecutionFailed error is " + e);
})
taskpool.execute(task2).then(() => {
  console.info("taskpool: execute task success");
}).catch((e:BusinessError) => {
  console.error(`taskpool: error code: ${e.code}, error info: ${e.message}`);
})
```

#### onExecutionSucceeded12+

onExecutionSucceeded(callback: CallbackFunction): void

注册一个回调函数，并在任务执行成功时调用它（周期任务不支持）。需在任务执行前注册，否则会抛异常。

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

参数名类型必填说明callback[CallbackFunction](#ZH-CN_TOPIC_0000002497444774__callbackfunction12)是需注册的回调函数。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息401The input parameters are invalid.10200034The executed task does not support the registration of listeners.

**示例：**

```ets
import { taskpool } from '@kit.ArkTS';

@Concurrent
function delay(args: number): number {
  let t: number = Date.now();
  while ((Date.now() - t) < 1000) {
      continue;
  }
  return args;
}

let task: taskpool.Task = new taskpool.Task(delay, 1);
task.onExecutionSucceeded(() => {
  console.info("taskpool: onExecutionSucceeded");
});
taskpool.execute(task).then(() => {
  console.info("taskpool: execute task success");
});
```

#### isDone12+

isDone(): boolean

检查任务是否已完成。

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**返回值：**

类型说明boolean任务执行完成时返回true，任务未执行完成时返回false。

**示例：**

```ets
@Concurrent
function inspectStatus(arg: number): number {
  // 1s sleep
  let t: number = Date.now();
  while (Date.now() - t < 1000) {
    continue;
  }
  return arg + 1;
}

async function taskpoolCancel(): Promise<void> {
  let task: taskpool.Task = new taskpool.Task(inspectStatus, 100); // 100: test number
  taskpool.execute(task).then((res: Object) => {
    console.info("taskpool test result: " + res);
  }).catch((err: string) => {
    console.error("taskpool test occur error: " + err);
  });

  setTimeout(() => {
    if (!task.isDone()) {
      taskpool.cancel(task);
    }
  }, 3000); // 延时3s，确保任务已执行
}

taskpoolCancel();
```

#### CallbackFunction12+

type CallbackFunction = () => void

注册的回调函数类型。

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

#### CallbackFunctionWithError12+

type CallbackFunctionWithError = (e: Error) => void

注册带有错误码的回调函数类型。

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

参数名类型必填说明eError是错误信息。

#### LongTask12+

表示长时任务。LongTask继承自[Task](#ZH-CN_TOPIC_0000002497444774__task)。

长时任务不设置执行时间上限，长时间运行不会触发超时异常，但不支持将同一任务多次执行或者将该任务加入任务组（TaskGroup）。

执行长时任务的线程会持续存在，直到任务完成并调用[terminateTask](#ZH-CN_TOPIC_0000002497444774__taskpoolterminatetask12)后，该线程在空闲时被回收。

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**示例：**

```ets
@Concurrent
function printArgs(args: string): string {
  console.info("printArgs: " + args);
  return args;
}

let task: taskpool.LongTask = new taskpool.LongTask(printArgs, "this is my first LongTask");
```

#### GenericsTask13+

表示泛型任务。GenericsTask继承自[Task](#ZH-CN_TOPIC_0000002497444774__task)。

相比创建Task，创建GenericsTask可以在编译阶段校验并发函数的传参和返回值类型。其余行为与Task相同。

**系统能力：** SystemCapability.Utils.Lang

#### constructor13+

constructor(func: (...args: A) => R | Promise<R>, ...args: A)

GenericsTask的构造函数。

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**参数：**

参数名类型必填说明func(...args: A) => R | Promise<R>是执行的逻辑需要传入函数，必须使用[@Concurrent装饰器](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/taskpool-introduction#concurrent装饰器)装饰，支持的函数返回值类型请查[序列化支持类型](#ZH-CN_TOPIC_0000002497444774__序列化支持类型)。argsA否任务执行传入函数的入参，支持的参数类型请查[序列化支持类型](#ZH-CN_TOPIC_0000002497444774__序列化支持类型)。默认值为undefined。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Incorrect parameter types; 2.Parameter verification failed.10200014The function is not marked as concurrent.

**示例：**

```ets
@Concurrent
function printArgs(args: string): string {
  console.info("printArgs: " + args);
  return args;
}

@Concurrent
function testWithThreeParams(a: number, b: string, c: number): string {
  return b;
}

@Concurrent
function testWithArray(args: [number, string]): string {
  return "success";
}

let task1: taskpool.Task = new taskpool.GenericsTask<[string], string>(printArgs, "this is my first LongTask");

let task2: taskpool.Task = new taskpool.GenericsTask<[number, string, number], string>(testWithThreeParams, 100, "test", 100);

let task3: taskpool.Task = new taskpool.GenericsTask<[[number, string]], string>(testWithArray, [100, "test"]);
```

#### constructor13+

constructor(name: string, func: (...args: A) => R | Promise<R>, ...args: A)

GenericsTask的构造函数，可以指定任务名称。

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**参数：**

参数名类型必填说明namestring是泛型任务名称。func(...args: A) => R | Promise<R>是执行的逻辑需要传入函数，必须使用[@Concurrent装饰器](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/taskpool-introduction#concurrent装饰器)装饰，支持的函数返回值类型请查[序列化支持类型](#ZH-CN_TOPIC_0000002497444774__序列化支持类型)。argsA否任务执行传入函数的入参，支持的参数类型请查[序列化支持类型](#ZH-CN_TOPIC_0000002497444774__序列化支持类型)。默认值为undefined。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Incorrect parameter types; 2.Parameter verification failed.10200014The function is not marked as concurrent.

**示例：**

```ets
@Concurrent
function printArgs(args: string): string {
  console.info("printArgs: " + args);
  return args;
}

let taskName: string = "taskName";
let task: taskpool.Task = new taskpool.GenericsTask<[string], string>(taskName, printArgs, "this is my first Task");
let name: string = task.name;
```

#### TaskGroup10+

表示任务组，一次执行一组任务，适用于执行一组有关联的任务。如果所有任务正常执行，异步执行完毕后返回所有任务结果的数组，数组中元素的顺序与[addTask](#ZH-CN_TOPIC_0000002497444774__addtask10-1)的顺序相同；如果任意任务失败，则会抛出对应异常。如果任务组中存在多个任务失败的情况，则会抛出第一个失败任务的异常。任务组可以多次执行，但执行后不能新增任务。

#### constructor10+

constructor()

TaskGroup的构造函数。

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**示例：**

```ets
let taskGroup = new taskpool.TaskGroup();
```

#### constructor11+

constructor(name: string)

TaskGroup的构造函数，支持指定任务组名称。

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数：**

参数名类型必填说明namestring是任务组名称。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

**示例：**

```ets
let taskGroupName: string = "groupName";
let taskGroup: taskpool.TaskGroup = new taskpool.TaskGroup(taskGroupName);
let name: string = taskGroup.name;
```

#### addTask10+

addTask(func: Function, ...args: Object[]): void

将待执行的函数添加到任务组中。使用该方法前需要先构造TaskGroup。

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数：**

参数名类型必填说明funcFunction是需要传入使用[@Concurrent装饰器](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/taskpool-introduction#concurrent装饰器)装饰的函数。支持的返回值类型请查[序列化支持类型](#ZH-CN_TOPIC_0000002497444774__序列化支持类型)。argsObject[]否任务执行函数的入参，支持的类型请查[序列化支持类型](#ZH-CN_TOPIC_0000002497444774__序列化支持类型)，默认值为undefined。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.10200014The function is not marked as concurrent.

**示例：**

```ets
@Concurrent
function printArgs(args: number): number {
  console.info("printArgs: " + args);
  return args;
}

let taskGroup: taskpool.TaskGroup = new taskpool.TaskGroup();
taskGroup.addTask(printArgs, 100); // 100: test number
```

#### addTask10+

addTask(task: Task): void

将创建好的任务添加到任务组中。使用此方法前需要先构造TaskGroup。任务组不能添加其他任务组中的任务、串行队列任务、异步队列任务、有依赖关系的任务、长时任务、周期任务和已执行的任务。

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数：**

参数名类型必填说明task[Task](#ZH-CN_TOPIC_0000002497444774__task)是需要添加到任务组中的任务。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.10200014The function is not marked as concurrent.10200051The periodic task cannot be executed again.10200057The task cannot be executed by two APIs.

**示例：**

```ets
@Concurrent
function printArgs(args: number): number {
  console.info("printArgs: " + args);
  return args;
}

let taskGroup: taskpool.TaskGroup = new taskpool.TaskGroup();
let task: taskpool.Task = new taskpool.Task(printArgs, 200); // 200: test number
taskGroup.addTask(task);
```

#### 属性

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

名称类型只读可选说明name11+string否否创建任务组时指定的任务组名称。

#### SequenceRunner 11+

表示串行队列的任务，用于执行一组需要串行执行的任务。

#### constructor11+

constructor(priority?: Priority)

SequenceRunner的构造函数。

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数：**

参数名类型必填说明priority[Priority](#ZH-CN_TOPIC_0000002497444774__priority)否指定任务的优先级，该参数默认值为taskpool.Priority.MEDIUM。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Incorrect parameter types; 2. Parameter verification failed.

**示例：**

```ets
let runner: taskpool.SequenceRunner = new taskpool.SequenceRunner();
```

#### constructor12+

constructor(name: string, priority?: Priority)

SequenceRunner的构造函数。构造一个全局串行队列，如果名字相同，将返回同一个串行队列。

- 底层通过单例模式保证了：创建同名串行队列时，获取到同一个实例。
- 无法修改串行队列的优先级。

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

参数名类型必填说明namestring是串行队列的名字。priority[Priority](#ZH-CN_TOPIC_0000002497444774__priority)否指定任务的优先级，该参数默认值为taskpool.Priority.MEDIUM。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed.

**示例：**

```ets
let runner:taskpool.SequenceRunner = new taskpool.SequenceRunner("runner1", taskpool.Priority.LOW);
```

#### execute11+

execute(task: Task): Promise<Object>

执行串行任务。使用该方法前需先构造SequenceRunner。串行队列不能执行任务组任务、其他串行队列任务、异步队列任务、有依赖关系的任务和已执行的任务。使用Promise异步回调。

- 不支持加入存在依赖的任务。
- 前面的任务执行失败或取消不会影响后续任务的执行。

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数：**

参数名类型必填说明task[Task](#ZH-CN_TOPIC_0000002497444774__task)是需要添加到串行任务队列中的任务。

**返回值：**

类型说明Promise<Object>Promise对象，返回任务执行的结果。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.10200006An exception occurred during serialization.10200025dependent task not allowed.10200051The periodic task cannot be executed again.10200057The task cannot be executed by two APIs.

**示例：**

```ets
@Concurrent
function additionDelay(delay: number): void {
  let start: number = new Date().getTime();
  while (new Date().getTime() - start < delay) {
    continue;
  }
}
@Concurrent
function waitForRunner(finalString: string): string {
  return finalString;
}
async function seqRunner() {
  let finalString:string = "";
  let task1:taskpool.Task = new taskpool.Task(additionDelay, 3000);
  let task2:taskpool.Task = new taskpool.Task(additionDelay, 2000);
  let task3:taskpool.Task = new taskpool.Task(additionDelay, 1000);
  let task4:taskpool.Task = new taskpool.Task(waitForRunner, finalString);

  let runner:taskpool.SequenceRunner = new taskpool.SequenceRunner();
  runner.execute(task1).then(() => {
    finalString += 'a';
    console.info("seqrunner: task1 done.");
  });
  runner.execute(task2).then(() => {
    finalString += 'b';
    console.info("seqrunner: task2 done");
  });
  runner.execute(task3).then(() => {
    finalString += 'c';
    console.info("seqrunner: task3 done");
  });
  await runner.execute(task4);
  console.info("seqrunner: task4 done, finalString is " + finalString);
}
```

#### AsyncRunner18+

表示异步队列。可以指定任务执行的并发度和排队策略。

#### constructor18+

constructor(runningCapacity: number, waitingCapacity?: number)

AsyncRunner的构造函数。构造一个非全局的异步队列，如果参数相同，返回的是不同的异步队列。

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**参数：**

参数名类型必填说明runningCapacitynumber是指定任务执行的最大并发度，该参数应为正整数，负数时报错，非整数时会向下取整。waitingCapacitynumber否指定等待任务的列表容量，取值需大于等于0，负数时报错，输入非整数时会向下取整。默认值为0，表示等待任务列表的容量没有限制。如果设置大于0的值，则表示排队策略为丢弃策略，当加入的任务数量超过该值时，等待列表中处于队头的任务会被丢弃。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed.

**示例：**

```ets
let runner: taskpool.AsyncRunner = new taskpool.AsyncRunner(5);
```

#### constructor18+

constructor(name: string, runningCapacity: number, waitingCapacity?: number)

AsyncRunner的构造函数用于构造一个全局异步队列。如果队列名称相同，将返回同一个异步队列实例。

- 底层通过单例模式确保创建同名的异步队列时，获取同一个实例。
- 无法修改并发度和等待任务列表容量。

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**参数：**

参数名类型必填说明namestring是异步队列的名字。runningCapacitynumber是指定任务执行的最大并发度，该参数应为正整数。负数时报错，非整数会向下取整。waitingCapacitynumber否指定等待任务的列表容量，取值需大于等于0，负数时报错，非整数时会向下取整。默认值为0，表示等待任务列表的容量没有限制。如果设置大于0的值，则表示排队策略为丢弃策略，当加入的任务数量超过该值时，等待列表中处于队头的任务会被丢弃。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed.

**示例：**

```ets
let runner:taskpool.AsyncRunner = new taskpool.AsyncRunner("runner1", 5, 5);
```

#### execute18+

execute(task: Task, priority?: Priority): Promise<Object>

执行异步任务。使用该方法前需要先构造AsyncRunner。使用Promise异步回调。

- 不支持执行任务组中的任务。
- 不支持执行串行队列中的任务。
- 不支持执行其他异步队列任务。
- 不支持执行周期性任务。
- 不支持执行延迟任务。
- 不支持执行存在依赖的任务。
- 不支持执行已执行过的任务。

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**参数：**

参数名类型必填说明task[Task](#ZH-CN_TOPIC_0000002497444774__task)是需要添加到异步队列中的任务。priority[Priority](#ZH-CN_TOPIC_0000002497444774__priority)否指定任务的优先级，该参数默认值为taskpool.Priority.MEDIUM。

**返回值：**

类型说明Promise<Object>Promise对象，返回任务执行的结果。

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息10200006An exception occurred during serialization.10200025dependent task not allowed.10200051The periodic task cannot be executed again.10200054The asyncRunner task is discarded.10200057The task cannot be executed by two APIs.

**示例：**

```ets
import { taskpool } from '@kit.ArkTS';
import { BusinessError } from '@kit.BasicServicesKit';

@Concurrent
function additionDelay(delay: number): void {
  let start: number = new Date().getTime();
  while (new Date().getTime() - start < delay) {
    continue;
  }
}
async function asyRunner() {
  let runner:taskpool.AsyncRunner = new taskpool.AsyncRunner("runner1", 5, 5);
  for (let i = 0; i < 30; i++) {
    let task:taskpool.Task = new taskpool.Task(additionDelay, 1000);
    runner.execute(task).then(() => {
      console.info("asyncRunner: task" + i + " done.");
    }).catch((e: BusinessError) => {
      console.error("asyncRunner: task" + i + " error." + e.code + "-" + e.message);
    });
  }
}

async function asyRunner2() {
  let runner:taskpool.AsyncRunner = new taskpool.AsyncRunner(5);
  for (let i = 0; i < 20; i++) {
    let task:taskpool.Task = new taskpool.Task(additionDelay, 1000);
    runner.execute(task).then(() => {
      console.info("asyncRunner: task" + i + " done.");
    });
  }
}
```

#### State10+

表示任务（Task）状态的枚举。当任务创建成功后，调用execute，任务进入taskpool等待队列，状态设置为WAITING；任务从等待队列出来进入taskpool工作线程中，任务状态更新为RUNNING；当任务执行完成，返回结果后任务状态重置为WAITING；当主动cancel任务时，将任务状态更新为CANCELED。

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

名称值说明WAITING1任务正在等待。RUNNING2任务正在执行。CANCELED3任务已被取消。

#### TaskInfo10+

任务的内部信息。

**系统能力：** SystemCapability.Utils.Lang

#### 属性

**系统能力：** SystemCapability.Utils.Lang

名称类型只读可选说明name12+string否否

任务的名字，不建议修改此值。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

taskIdnumber否否

任务的ID。任务的标识符，系统默认提供全局唯一值，不建议修改此值。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

state[State](#ZH-CN_TOPIC_0000002497444774__state10)否否

任务的状态。state标识任务的当前状态，不建议修改此值。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

durationnumber否是

任务执行至当前所用的时间，默认为0，单位为ms。当返回为0时，表示任务未执行；返回为空时，表示没有任务执行。不建议修改此值。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

#### ThreadInfo10+

工作线程的内部信息。

**系统能力：** SystemCapability.Utils.Lang

#### 属性

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

名称类型只读可选说明tidnumber否否工作线程的标识符。如果返回为空，表示当前没有任务执行。不建议修改此值。taskIdsnumber[]否是在当前线程上运行的任务ID列表。返回为空时，代表没有任务执行。不建议修改此值。priority[Priority](#ZH-CN_TOPIC_0000002497444774__priority)否是当前线程的优先级。返回为空时，代表没有任务执行。 不建议修改此值。

#### TaskPoolInfo10+

任务池的内部信息。

**系统能力：** SystemCapability.Utils.Lang

#### 属性

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

名称类型只读可选说明threadInfos[ThreadInfo[]](#ZH-CN_TOPIC_0000002497444774__threadinfo10)否否工作线程的内部信息。不建议修改此值。taskInfos[TaskInfo[]](#ZH-CN_TOPIC_0000002497444774__taskinfo10)否否任务的内部信息。不建议修改此值。

#### TaskResult20+

处于等待或执行过程中的任务进行取消操作后，在catch分支里捕获到BusinessError里的补充信息。其他场景下该信息为undefined。

**系统能力：** SystemCapability.Utils.Lang

#### 属性

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

名称类型只读可选说明resultObject否是任务执行结果。默认为undefined。 不建议修改此值。errorError | Object否是错误信息。默认和BusinessError的message字段一致。不建议修改此值。

任务被取消后，有如下两种情况：

- 如果当前任务是处于等待阶段，则result的值为undefined，error的值和BusinessError的message字段一致；
- 如果当前任务正在运行，有异常抛出的情况下result的值为undefined，error的值为抛出的异常信息；没有异常的情况下，result为任务执行完成后的结果，error的值和BusinessError的message字段一致。

**示例**

```ets
import { taskpool } from '@kit.ArkTS';
import { BusinessError } from '@kit.BasicServicesKit'

@Concurrent
function loop(): Error | number {
  let start: number = Date.now();
  while (Date.now() - start < 1500) {
  }
  if (taskpool.Task.isCanceled()) {
    return 0;
  }
  while (Date.now() - start < 3000) {
  }
  if (taskpool.Task.isCanceled()) {
    throw new Error("this is loop error");
  }
  return 1;
}

// 执行前取消
function waitingCancel() {
  let task = new taskpool.Task(loop);
  taskpool.executeDelayed(2000, task).catch((e:BusinessError<taskpool.TaskResult>) => {
    console.error(`waitingCancel task catch code: ${e.code}, message: ${e.message}`);
    // waitingCancel task catch code: 0, message: taskpool:: task has been canceled
    if (e.data !== undefined) {
      console.error(`waitingCancel task catch data: result: ${e.data.result}, error: ${e.data.error}`);
      // waitingCancel task catch data: result: undefined, error: taskpool:: task has been canceled
    }
  })
  setTimeout(() => {
    taskpool.cancel(task);
  }, 1000);
}

// 执行过程中取消
function runningCancel() {
  let task = new taskpool.Task(loop);
  taskpool.execute(task).catch((e:BusinessError<taskpool.TaskResult>) => {
    console.error(`runningCancel task catch code: ${e.code}, message: ${e.message}`);
    // runningCancel task catch code: 0, message: taskpool:: task has been canceled
    if (e.data !== undefined) {
      console.error(`runningCancel task catch data: result: ${e.data.result}, error: ${e.data.error}`);
      // runningCancel task catch data: result: 0, error: taskpool:: task has been canceled
    }
  })
  setTimeout(() => {
    taskpool.cancel(task);
  }, 1000);
}

// 执行过程中抛异常
function runningCancelError() {
  let task = new taskpool.Task(loop);
  taskpool.execute(task).catch((e:BusinessError<taskpool.TaskResult>) => {
    console.error(`runningCancelError task catch code: ${e.code}, message: ${e.message}`);
    // runningCancelError task catch code: 0, message: taskpool:: task has been canceled
    if (e.data !== undefined) {
      console.error(`runningCancelError task catch data: result: ${e.data.result}, error: ${e.data.error}`);
      // runningCancelError task catch data: result: undefined, error: Error: this is loop error
    }
  })
  setTimeout(() => {
    taskpool.cancel(task);
  }, 2000);
}
```

#### 其他说明

#### 序列化支持类型

序列化支持类型参考[线程间通信对象概述](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/serializable-overview)里的介绍。

#### 简单使用

**示例一**

```ets
// 支持普通函数、引用入参传递
@Concurrent
function printArgs(args: string): string {
  console.info("func: " + args);
  return args;
}

async function taskpoolExecute(): Promise<void> {
  // taskpool.execute(task)
  let task: taskpool.Task = new taskpool.Task(printArgs, "create task, then execute");
  console.info("taskpool.execute(task) result: " + await taskpool.execute(task));
  // taskpool.execute(function)
  console.info("taskpool.execute(function) result: " + await taskpool.execute(printArgs, "execute task by func"));
}

taskpoolExecute();
```

**示例二**

```ets
// b.ets
export let c: string = "hello";
```

```ets
// 引用import变量
// a.ets(与b.ets位于同一目录中)
import { c } from "./b";

@Concurrent
function printArgs(a: string): string {
  console.info(a);
  console.info(c);
  return a;
}

async function taskpoolExecute(): Promise<void> {
  // taskpool.execute(task)
  let task: taskpool.Task = new taskpool.Task(printArgs, "create task, then execute");
  console.info("taskpool.execute(task) result: " + await taskpool.execute(task));

  // taskpool.execute(function)
  console.info("taskpool.execute(function) result: " + await taskpool.execute(printArgs, "execute task by func"));
}

taskpoolExecute();
```

**示例三**

```ets
// 支持async函数
@Concurrent
async function delayExecute(): Promise<Array<Object>> {
  let ret = await Promise.all<Object>([
    new Promise<Object>(resolve => setTimeout(resolve, 1000, "resolved"))
  ]);
  return ret;
}

async function taskpoolExecute(): Promise<void> {
  taskpool.execute(delayExecute).then((result: Object) => {
    console.info("taskPoolTest task result: " + result);
  }).catch((err: string) => {
    console.error("taskpool test occur error: " + err);
  });
}

taskpoolExecute();
```

**示例四**

```ets
// c.ets
@Concurrent
function strSort(inPutArr: Array<string>): Array<string> {
  let newArr = inPutArr.sort();
  return newArr;
}

export async function func1(): Promise<void> {
  console.info("taskpoolTest start");
  let strArray: Array<string> = ['c test string', 'b test string', 'a test string'];
  let task: taskpool.Task = new taskpool.Task(strSort, strArray);
  console.info("func1 result:" + await taskpool.execute(task));
}

export async function func2(): Promise<void> {
  console.info("taskpoolTest2 start");
  let strArray: Array<string> = ['c test string', 'b test string', 'a test string'];
  taskpool.execute(strSort, strArray).then((result: Object) => {
    console.info("func2 result: " + result);
  }).catch((err: string) => {
    console.error("taskpool test occur error: " + err);
  });
}
```

```ets
// index.ets
import { func1, func2 } from "./c";

func1();
func2();
```

**示例五**

```ets
// 任务取消成功
@Concurrent
function inspectStatus(arg: number): number {
  // 第一次检查任务是否已经取消并作出响应
  if (taskpool.Task.isCanceled()) {
    console.info("task has been canceled before 2s sleep.");
    return arg + 2;
  }
  // 2s sleep
  let t: number = Date.now();
  while (Date.now() - t < 2000) {
    continue;
  }
  // 第二次检查任务是否已经取消并作出响应
  if (taskpool.Task.isCanceled()) {
    console.info("task has been canceled after 2s sleep.");
    return arg + 3;
  }
  return arg + 1;
}

async function taskpoolCancel(): Promise<void> {
  let task: taskpool.Task = new taskpool.Task(inspectStatus, 100); // 100: test number
  taskpool.execute(task).then((res: Object) => {
    console.info("taskpool test result: " + res);
  }).catch((err: string) => {
    console.error("taskpool test occur error: " + err);
  });
  // 1s后取消task
  setTimeout(() => {
    try {
      taskpool.cancel(task);
    } catch (e) {
      console.error(`taskpool: cancel error code: ${e.code}, info: ${e.message}`);
    }
  }, 1000);
}

taskpoolCancel();
```

**示例六**

```ets
// 已执行的任务取消失败
@Concurrent
function inspectStatus(arg: number): number {
  // 第一次检查任务是否已经取消并作出响应
  if (taskpool.Task.isCanceled()) {
    return arg + 2;
  }
  // 延时0.5s
  let t: number = Date.now();
  while (Date.now() - t < 500) {
    continue;
  }
  // 第二次检查任务是否已经取消并作出响应
  if (taskpool.Task.isCanceled()) {
    return arg + 3;
  }
  return arg + 1;
}

async function taskpoolCancel(): Promise<void> {
  let task: taskpool.Task = new taskpool.Task(inspectStatus, 100); // 100: test number
  taskpool.execute(task).then((res: Object) => {
    console.info("taskpool test result: " + res);
  }).catch((err: string) => {
    console.error("taskpool test occur error: " + err);
  });

  setTimeout(() => {
    try {
      taskpool.cancel(task); // 任务已执行,取消失败
    } catch (e) {
      console.error(`taskpool: cancel error code: ${e.code}, info: ${e.message}`);
    }
  }, 3000); // 延时3s，确保任务已执行
}

taskpoolCancel();
```

**示例七**

```ets
// 待执行的任务组取消成功
@Concurrent
function printArgs(args: number): number {
  let t: number = Date.now();
  while (Date.now() - t < 1000) {
    continue;
  }
  console.info("printArgs: " + args);
  return args;
}

async function taskpoolGroupCancelTest(): Promise<void> {
  let taskGroup1: taskpool.TaskGroup = new taskpool.TaskGroup();
  taskGroup1.addTask(printArgs, 10); // 10: test number
  taskGroup1.addTask(printArgs, 20); // 20: test number
  taskGroup1.addTask(printArgs, 30); // 30: test number
  let taskGroup2: taskpool.TaskGroup = new taskpool.TaskGroup();
  let task1: taskpool.Task = new taskpool.Task(printArgs, 100); // 100: test number
  let task2: taskpool.Task = new taskpool.Task(printArgs, 200); // 200: test number
  let task3: taskpool.Task = new taskpool.Task(printArgs, 300); // 300: test number
  taskGroup2.addTask(task1);
  taskGroup2.addTask(task2);
  taskGroup2.addTask(task3);
  taskpool.execute(taskGroup1).then((res: Array<Object>) => {
    console.info("taskpool execute res is:" + res);
  }).catch((e: string) => {
    console.error("taskpool execute error is:" + e);
  });
  taskpool.execute(taskGroup2).then((res: Array<Object>) => {
    console.info("taskpool execute res is:" + res);
  }).catch((e: string) => {
    console.error("taskpool execute error is:" + e);
  });

  try {
    taskpool.cancel(taskGroup2);
  } catch (e) {
    console.error(`taskpool: cancel error code: ${e.code}, info: ${e.message}`);
  }
}

taskpoolGroupCancelTest()
```

**示例八**

```ets
// 分别创建执行100个高、中、低优先级的任务，查看其各项信息
@Concurrent
function delay(): void {
  let start: number = new Date().getTime();
  while (new Date().getTime() - start < 500) {
    continue;
  }
}

let highCount: number = 0;
let mediumCount: number = 0;
let lowCount: number = 0;
let allCount: number = 100;
for (let i = 0; i < allCount; i++) {
  let task1: taskpool.Task = new taskpool.Task(delay);
  let task2: taskpool.Task = new taskpool.Task(delay);
  let task3: taskpool.Task = new taskpool.Task(delay);
  taskpool.execute(task1, taskpool.Priority.LOW).then(() => {
    lowCount++;
  }).catch((e: string) => {
    console.error("low task error: " + e);
  })
  taskpool.execute(task2, taskpool.Priority.MEDIUM).then(() => {
    mediumCount++;
  }).catch((e: string) => {
    console.error("medium task error: " + e);
  })
  taskpool.execute(task3, taskpool.Priority.HIGH).then(() => {
    highCount++;
  }).catch((e: string) => {
    console.error("high task error: " + e);
  })
}
let start: number = new Date().getTime();
while (new Date().getTime() - start < 1000) {
  continue;
}
let taskpoolInfo: taskpool.TaskPoolInfo = taskpool.getTaskPoolInfo();
let tid: number = 0;
let taskIds: Array<number> = [];
let priority: number = 0;
let taskId: number = 0;
let state: number = 0;
let duration: number = 0;
let name: string = "";
let threadIS = Array.from(taskpoolInfo.threadInfos);
for (let threadInfo of threadIS) {
  tid = threadInfo.tid;
  if (threadInfo.taskIds != undefined && threadInfo.priority != undefined) {
    taskIds.length = threadInfo.taskIds.length;
    priority = threadInfo.priority;
  }
  console.info("taskpool---tid is:" + tid + ", taskIds is:" + taskIds + ", priority is:" + priority);
}
let taskIS = Array.from(taskpoolInfo.taskInfos);
for (let taskInfo of taskIS) {
  taskId = taskInfo.taskId;
  state = taskInfo.state;
  if (taskInfo.duration != undefined) {
    duration = taskInfo.duration;
    name = taskInfo.name;
  }
  console.info("taskpool---taskId is:" + taskId + ", state is:" + state + ", duration is:" + duration + ", name is:" + name);
}
```