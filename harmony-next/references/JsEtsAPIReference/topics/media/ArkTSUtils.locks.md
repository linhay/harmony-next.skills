# ArkTSUtils.locks

为了解决多并发实例间的数据竞争问题，ArkTS语言基础库引入了异步锁能力。为了开发者的开发效率，AsyncLock对象支持跨并发实例引用传递。

由于ArkTS语言支持异步操作，阻塞锁容易产生死锁问题，因此我们在ArkTS中仅支持异步锁（非阻塞式锁）。

使用异步锁的方法需要标记为async，调用方需要await修饰调用，才能保证时序正确。因此会导致外层调用函数全部标记成async。

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

此模块仅支持在ArkTS文件（文件后缀为.ets）中导入使用。

#### 导入模块

```ets
import { ArkTSUtils } from '@kit.ArkTS'
```

#### AsyncLockCallback

type AsyncLockCallback<T> = () => T | Promise<T>

这是一个补充类型别名，表示[lockAsync](#ZH-CN_TOPIC_0000002529284741__lockasync)函数所有重载中的回调。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

#### AsyncLock

实现异步锁功能的类，允许在锁下执行异步操作。该类使用[@Sendable装饰器](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-sendable)装饰。

#### 属性

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

名称类型只读可选说明namestring是否锁的名称。

**示例：**

```ets
// 示例一：
@Sendable
class A {
  count_: number = 0;
  async getCount(): Promise<number> {
    let lock: ArkTSUtils.locks.AsyncLock = ArkTSUtils.locks.AsyncLock.request("lock_1");
    return lock.lockAsync(() => {
      return this.count_;
    })
  }
  async setCount(count: number) {
    let lock: ArkTSUtils.locks.AsyncLock = ArkTSUtils.locks.AsyncLock.request("lock_1");
    await lock.lockAsync(() => {
      this.count_ = count;
    })
  }
}

// 示例二：
@Sendable
class A {
  count_: number = 0;
  lock_: ArkTSUtils.locks.AsyncLock = new ArkTSUtils.locks.AsyncLock();
  async getCount(): Promise<number> {
    return this.lock_.lockAsync(() => {
      return this.count_;
    })
  }
  async setCount(count: number) {
    await this.lock_.lockAsync(() => {
      this.count_ = count;
    })
  }
}

@Concurrent
async function foo(a: A) {
  await a.setCount(10)
}
```

#### constructor

constructor()

默认构造函数。创建一个异步锁。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**示例：**

```ets
let lock = new ArkTSUtils.locks.AsyncLock();
```

#### request

static request(name: string): AsyncLock

使用指定的名称查找或创建（如果未找到）异步锁实例。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

名称类型必填说明namestring是按指定名称查找或创建异步锁实例。

**返回值：**

类型说明[AsyncLock](#ZH-CN_TOPIC_0000002529284741__asynclock)返回查找到或创建后的异步锁实例。

**示例：**

```ets
let lockName = 'isAvailableLock';
let lock = ArkTSUtils.locks.AsyncLock.request(lockName);
```

#### query

static query(name: string): AsyncLockState

查询指定异步锁的信息。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

名称类型必填说明namestring是要查询的锁的名称，仅可查询通过[request接口](#ZH-CN_TOPIC_0000002529284741__request)获取的锁（即与[request接口](#ZH-CN_TOPIC_0000002529284741__request)入参锁名称保持一致）。

**返回值：**

类型说明[AsyncLockState](#ZH-CN_TOPIC_0000002529284741__asynclockstate)包含状态描述的异步锁状态实例。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息401The input parameters are invalid.10200030The lock does not exist.

**示例：**

```ets
// 你已经在别的地方创建了一个锁。
// let lock = ArkTSUtils.locks.AsyncLock.request("queryTestLock");
let state = ArkTSUtils.locks.AsyncLock.query('queryTestLock');
if (!state) {
    throw new Error('测试失败：期望有效的状态，但得到的是 ' + state);
}
let pending: ArkTSUtils.locks.AsyncLockInfo[] = state.pending;
let held: ArkTSUtils.locks.AsyncLockInfo[] = state.held;
```

#### queryAll

static queryAll(): AsyncLockState[]

查询所有现有锁的信息。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明[AsyncLockState](#ZH-CN_TOPIC_0000002529284741__asynclockstate)[]包含锁状态信息的异步锁状态数组。

**示例：**

```ets
let states: ArkTSUtils.locks.AsyncLockState[] = ArkTSUtils.locks.AsyncLock.queryAll();
if (states.length === 0) {
    throw new Error('测试失败：期望至少有1个状态，但得到的是 ' + states.length);
}
```

#### lockAsync

lockAsync<T>(callback: AsyncLockCallback<T>): Promise<T>

在获取的锁下执行操作。该方法首先获取锁，然后调用回调，最后释放锁。回调在调用[lockAsync](#ZH-CN_TOPIC_0000002529284741__lockasync)的同一线程中以异步方式执行。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

名称类型必填说明callback[AsyncLockCallback<T>](#ZH-CN_TOPIC_0000002529284741__asynclockcallback)是获取锁后要调用的函数。

**返回值：**

类型说明Promise<T>回调执行后将解决的Promise。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息401The input parameters are invalid.10200030The lock does not exist.

**示例：**

```ets
let lock = new ArkTSUtils.locks.AsyncLock();
let p1 = lock.lockAsync<void>(() => {
    // 执行某些操作
});
```

#### lockAsync

lockAsync<T>(callback: AsyncLockCallback<T>, mode: AsyncLockMode): Promise<T>

在获取的锁下执行操作。该方法首先获取锁，然后调用回调，最后释放锁。回调在调用[lockAsync](#ZH-CN_TOPIC_0000002529284741__lockasync)的同一线程中以异步方式执行。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

名称类型必填说明callback[AsyncLockCallback<T>](#ZH-CN_TOPIC_0000002529284741__asynclockcallback)是获取锁后要调用的函数。mode[AsyncLockMode](#ZH-CN_TOPIC_0000002529284741__asynclockmode)是锁的操作模式。

**返回值：**

类型说明Promise<T>回调执行后将解决的Promise。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息401The input parameters are invalid.10200030The lock does not exist.

**示例：**

```ets
let lock = new ArkTSUtils.locks.AsyncLock();
let p1 = lock.lockAsync<void>(() => {
    // 执行某些操作
}, ArkTSUtils.locks.AsyncLockMode.EXCLUSIVE);
```

#### lockAsync

lockAsync<T, U>(callback: AsyncLockCallback<T>, mode: AsyncLockMode, options: AsyncLockOptions<U>): Promise<T | U>

在获取的锁下执行操作。该方法首先获取锁，然后调用回调，最后释放锁。回调在调用[lockAsync](#ZH-CN_TOPIC_0000002529284741__lockasync)的同一线程中以异步方式执行。在[AsyncLockOptions](#ZH-CN_TOPIC_0000002529284741__asynclockoptions)中可以提供一个可选的超时值。在这种情况下，如果超时前未能获取锁，lockAsync将返回被拒绝的Promise并带上一个BusinessError实例。这种情况下，错误信息将包含持有的锁和等待的锁的信息以及可能的死锁警告。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

名称类型必填说明callback[AsyncLockCallback<T>](#ZH-CN_TOPIC_0000002529284741__asynclockcallback)是获取锁后要调用的函数。mode[AsyncLockMode](#ZH-CN_TOPIC_0000002529284741__asynclockmode)是锁的操作模式。options[AsyncLockOptions<U>](#ZH-CN_TOPIC_0000002529284741__asynclockoptions)是锁的操作选项。

**返回值：**

类型说明Promise<T | U>回调执行后解决的Promise，或者在超时情况下被拒绝。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[语言基础类库错误码](../../errors/语言基础类库错误码.md)。

错误码ID错误信息401The input parameters are invalid.10200030The lock does not exist.10200031Timeout exceeded.

**示例：**

```ets
let lock = new ArkTSUtils.locks.AsyncLock();
let options = new ArkTSUtils.locks.AsyncLockOptions<void>();
options.timeout = 1000;
let p: Promise<void> = lock.lockAsync<void, void>(
    () => {
        // 执行某些操作
    },
    ArkTSUtils.locks.AsyncLockMode.EXCLUSIVE,
    options
);
```

#### AsyncLockMode

锁操作对应的模式枚举。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

名称值说明SHARED1共享锁模式。如果指定了此模式，允许​​多个线程或并发任务同时获取锁并执行操作。多用于读操作、无数据竞争的并行任务。EXCLUSIVE2独占锁模式。如果指定了此模式，仅允许持有锁的任务执行。 它与任何其他锁均不兼容​​，包括其他独占锁和共享锁。多用于写操作、数据更新、状态修改等可能产生竞争的场景。

**示例：**

```ets
let lock = new ArkTSUtils.locks.AsyncLock();
// shared0可获取锁并开始执行
lock.lockAsync(async () => {
    console.info('shared0');
    await new Promise<void>((resolve) => setTimeout(resolve, 1000));
}, ArkTSUtils.locks.AsyncLockMode.SHARED);
// shared1可获取锁并开始执行，无需等待shared0
lock.lockAsync(async () => {
    console.info('shared1');
    await new Promise<void>((resolve) => setTimeout(resolve, 1000));
}, ArkTSUtils.locks.AsyncLockMode.SHARED);
// exclusive0需等待shared0、1执行完后才可获取锁并执行
lock.lockAsync(async () => {
    console.info('exclusive0');
    await new Promise<void>((resolve) => setTimeout(resolve, 1000));
}, ArkTSUtils.locks.AsyncLockMode.EXCLUSIVE);
// shared2需等待exclusive0执行完后才可获取锁并执行
lock.lockAsync(async () => {
    console.info('shared2');
    await new Promise<void>((resolve) => setTimeout(resolve, 1000));
}, ArkTSUtils.locks.AsyncLockMode.SHARED);
// shared3需等待exclusive0执行完后才可获取锁并执行，无需等待shared2
lock.lockAsync(async () => {
    console.info('shared3');
    await new Promise<void>((resolve) => setTimeout(resolve, 1000));
}, ArkTSUtils.locks.AsyncLockMode.SHARED);
```

#### AsyncLockOptions

class AsyncLockOptions<T>

表示锁操作选项的类。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

#### constructor

constructor()

默认构造函数。创建一个所有属性均具有默认值的异步锁配置项实例。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**示例：**

```ets
let s: ArkTSUtils.locks.AbortSignal<string> = { aborted: false, reason: 'Aborted' };
let options = new ArkTSUtils.locks.AsyncLockOptions<string>();
options.isAvailable = false;
options.signal = s;
let lock = new ArkTSUtils.locks.AsyncLock();
let p = lock.lockAsync<void, string>(
  () => {
    // 执行某些操作
  },
  ArkTSUtils.locks.AsyncLockMode.EXCLUSIVE,
  options,
);
```

#### 属性

名称类型只读可选说明isAvailableboolean否否当前锁是否可用。取值为true，则只有在尚未持有锁定请求时才会授予该锁定请求；为false则表示将等待当前锁被释放。默认为 false。signal[AbortSignal<T>](#ZH-CN_TOPIC_0000002529284741__abortsignal)|null否否用于终止异步操作的对象。当signal.aborted为true时，锁请求将被丢弃；当signal.aborted为false时，请求会继续等待获取锁；当signal为null时，请求正常排队运行。默认为 null。timeoutnumber否否锁的超时时间，单位为毫秒。若该值大于零，且操作运行时间超过该时间，[lockAsync](#ZH-CN_TOPIC_0000002529284741__lockasync)将返回被拒绝的Promise。默认为 0。

#### AsyncLockState

用于存储异步锁实例上当前执行的所有锁操作的信息的类。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

#### 属性

名称类型只读可选说明held[AsyncLockInfo[]](#ZH-CN_TOPIC_0000002529284741__asynclockinfo)否否持有的锁信息。pending[AsyncLockInfo[]](#ZH-CN_TOPIC_0000002529284741__asynclockinfo)否否等待中的锁信息。

#### AsyncLockInfo

关于锁的信息。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

#### 属性

名称类型只读可选说明namestring否否锁的名称。mode[AsyncLockMode](#ZH-CN_TOPIC_0000002529284741__asynclockmode)否否锁的模式。contextIdnumber否否[AsyncLockMode](#ZH-CN_TOPIC_0000002529284741__asynclockmode)调用者的执行上下文标识符。

#### AbortSignal

用于终止异步操作的对象。该类的实例必须在其创建的同一线程中访问。从其他线程访问此类的字段会导致未定义的行为。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

#### 属性

名称类型只读可选说明abortedboolean否否是否终止异步操作。为true时表示终止异步操作，为false时表示异步操作未被终止。reasonT否否终止的原因。此值将用于拒绝[lockAsync](#ZH-CN_TOPIC_0000002529284741__lockasync)返回的Promise。

#### ConditionVariable18+

实现异步等待功能的类，支持异步等待通知操作。该类使用[@Sendable装饰器](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-sendable)装饰。

**元服务API**：从API version 18 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

#### constructor18+

constructor()

默认构造函数。创建一个异步等待通知操作的对象。

**元服务API**：从API version 18 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**示例：**

```ets
let conditionVariable = new ArkTSUtils.locks.ConditionVariable();
```

#### request18+

static request(name: string): ConditionVariable

使用指定的名称查找或创建（如果未找到）异步等待通知操作的对象。

**元服务API**：从API version 18 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

名称类型必填说明namestring是按指定名称查找或创建等待通知操作的对象名称，字符串无特别限制。

**返回值：**

类型说明[ConditionVariable](#ZH-CN_TOPIC_0000002529284741__conditionvariable18)返回查找到或创建后的异步等待通知操作的实例。

**示例：**

```ets
let conditionVariable = ArkTSUtils.locks.ConditionVariable.request("conditionName");
```

#### wait18+

wait(): Promise<void>

异步调用进入等待中，将在被唤醒后继续执行。使用Promise异步回调。

**元服务API**：从API version 18 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明Promise<void>无返回结果的Promise对象。

**示例：**

```ets
const conditionVariable: ArkTSUtils.locks.ConditionVariable = new ArkTSUtils.locks.ConditionVariable();
conditionVariable.wait().then(() => {
  console.info(`Thread being awakened, then continue...`); //被唤醒后输出日志
});
```

#### waitFor18+

waitFor(timeout : number) : Promise<void>

异步调用进入等待中, 将在被唤醒或者等待时间结束后继续执行。使用Promise异步回调。

**元服务API**：从API version 18 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

名称类型必填说明timeoutnumber是等待时间，单位为ms，正整数。

**返回值：**

类型说明Promise<void>无返回结果的Promise对象。

**示例：**

```ets
const conditionVariable: ArkTSUtils.locks.ConditionVariable = new ArkTSUtils.locks.ConditionVariable();
conditionVariable.waitFor(3000).then(() => {
  console.info(`Thread being awakened, then continue...`); //被唤醒后输出日志
});
```

#### notifyAll18+

notifyAll() : void

通知所有等待的线程。

**元服务API**：从API version 18 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**示例：**

```ets
const conditionVariable: ArkTSUtils.locks.ConditionVariable = new ArkTSUtils.locks.ConditionVariable();
conditionVariable.waitFor(3000).then(() => {
  console.info(`Thread being awakened, then continue...`); //被唤醒后输出日志
});
// 通知所有等待的线程。
conditionVariable.notifyAll();
```

#### notifyOne18+

notifyOne() : void

通知第一个等待的线程。

**元服务API**：从API version 18 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**示例：**

```ets
const conditionVariable: ArkTSUtils.locks.ConditionVariable = new ArkTSUtils.locks.ConditionVariable();
conditionVariable.waitFor(3000).then(() => {
  console.info(`Thread a being awakened, then continue...`); //被唤醒后输出日志
});
// 通知第一个等待的线程。
conditionVariable.notifyOne();
```