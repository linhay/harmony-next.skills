# @ohos.runningLock (RunningLock锁)

该模块为RunningLock锁相关操作的接口，RunningLock锁提供使能接近光亮灭屏或者设备熄屏后阻止进入睡眠的能力，包括创建、查询、持锁、释放锁等操作，RunningLock锁的类型详情见[RunningLockType](#ZH-CN_TOPIC_0000002553361513__runninglocktype)。


本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import {runningLock} from '@kit.BasicServicesKit';
```

#### runningLock.isSupported9+

isSupported(type: RunningLockType): boolean

**方法介绍：** 查询系统是否支持该类型的锁。

**系统能力：** SystemCapability.PowerManager.PowerManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | RunningLockType | 是 | 需要查询的锁的类型；该参数必须是一个枚举类。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回true表示支持，返回false表示不支持。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码]([通用错误码](../../errors/通用错误码.md).md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Incorrect parameter types; 2.Parameter verification failed. |

**示例：**

```ets
try {
    let isSupported = runningLock.isSupported(runningLock.RunningLockType.PROXIMITY_SCREEN_CONTROL);
    console.info('BACKGROUND type supported: ' + isSupported);
} catch(err) {
    console.error('check supported failed, err: ' + err);
}
```

#### runningLock.create9+

create(name: string, type: RunningLockType, callback: AsyncCallback<RunningLock>): void

**方法介绍：** 创建RunningLock锁。使用callback异步回调。

**系统能力：** SystemCapability.PowerManager.PowerManager.Core

**需要权限：** ohos.permission.RUNNING_LOCK

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 锁的名字；该参数必须为字符串类型。 |
| type | RunningLockType | 是 | 要创建的锁的类型；该参数必须是一个枚举类。 |
| callback | AsyncCallback<RunningLock> | 是 | 回调函数。当创建锁成功，err为undefined，data为创建的RunningLock；否则为错误对象；AsyncCallback封装了一个RunningLock类型的类。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Parameter verification failed. |
| 201 | If the permission is denied. |

**示例：**

```ets
runningLock.create('running_lock_test', runningLock.RunningLockType.PROXIMITY_SCREEN_CONTROL, (err: Error, lock: runningLock.RunningLock) => {
    if (typeof err === 'undefined') {
        console.info('created running lock: ' + lock);
    } else {
        console.error('create running lock failed, err: ' + err);
    }
});
```

#### runningLock.create9+

create(name: string, type: RunningLockType): Promise<RunningLock>

**方法介绍：** 创建RunningLock锁。使用Promise异步回调。

**系统能力：** SystemCapability.PowerManager.PowerManager.Core

**需要权限：** ohos.permission.RUNNING_LOCK

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 锁的名字；该参数必须为字符串类型。 |
| type | RunningLockType | 是 | 要创建的锁的类型；该参数必须是一个枚举类。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<RunningLock> | Promise对象，返回RunningLock锁对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Parameter verification failed. |
| 201 | If the permission is denied. |

**示例：**

```ets
runningLock.create('running_lock_test', runningLock.RunningLockType.PROXIMITY_SCREEN_CONTROL)
.then((lock: runningLock.RunningLock) => {
    console.info('created running lock: ' + lock);
})
.catch((err: Error) => {
    console.error('create running lock failed, err: ' + err);
});
```

#### runningLock.isRunningLockTypeSupported(deprecated)

isRunningLockTypeSupported(type: RunningLockType, callback: AsyncCallback<boolean>): void


从API version 7开始支持，从API version 9开始不再维护，建议使用[runningLock.isSupported](#ZH-CN_TOPIC_0000002553361513__runninglockissupported9)替代。

**方法介绍：** 查询系统是否支持该类型的锁。使用callback异步回调。

**系统能力：** SystemCapability.PowerManager.PowerManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | RunningLockType | 是 | 需要查询的锁的类型。 |
| callback | AsyncCallback<boolean> | 是 | 回调函数。当查询成功，err为undefined，data为获取到的支持情况，返回true表示支持，返回false表示不支持；否则为错误对象。 |

**示例：**

```ets
runningLock.isRunningLockTypeSupported(runningLock.RunningLockType.BACKGROUND, (err: Error, data: boolean) => {
    if (typeof err === 'undefined') {
        console.info('BACKGROUND lock support status: ' + data);
    } else {
        console.error('check BACKGROUND lock support status failed, err: ' + err);
    }
});
```

#### runningLock.isRunningLockTypeSupported(deprecated)

isRunningLockTypeSupported(type: RunningLockType): Promise<boolean>


从API version 7开始支持，从API version 9开始不再维护，建议使用[runningLock.isSupported](#ZH-CN_TOPIC_0000002553361513__runninglockissupported9)替代。

**方法介绍：** 查询系统是否支持该类型的锁。使用Promise异步回调。

**系统能力：** SystemCapability.PowerManager.PowerManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | RunningLockType | 是 | 需要查询的锁的类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示支持；返回false表示不支持。 |

**示例：**

```ets
runningLock.isRunningLockTypeSupported(runningLock.RunningLockType.BACKGROUND)
.then((data: boolean) => {
    console.info('BACKGROUND lock support status: ' + data);
})
.catch((err: Error) => {
    console.error('check BACKGROUND lock support status failed, err: ' + err);
});
```

#### runningLock.createRunningLock(deprecated)

createRunningLock(name: string, type: RunningLockType, callback: AsyncCallback<RunningLock>): void


从API version 7开始支持，从API version 9开始不再维护，建议使用[runningLock.create](#ZH-CN_TOPIC_0000002553361513__runninglockcreate9)替代。

**方法介绍：** 创建RunningLock锁。使用callback异步回调。

**系统能力：** SystemCapability.PowerManager.PowerManager.Core

**需要权限：** ohos.permission.RUNNING_LOCK

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 锁的名字。 |
| type | RunningLockType | 是 | 要创建的锁的类型。 |
| callback | AsyncCallback<RunningLock> | 是 | 回调函数。当创建锁成功，err为undefined，data为创建的RunningLock；否则为错误对象。 |

**示例：**

```ets
runningLock.createRunningLock('running_lock_test', runningLock.RunningLockType.BACKGROUND, (err: Error, lock: runningLock.RunningLock) => {
    if (typeof err === 'undefined') {
        console.info('created running lock: ' + lock);
    } else {
        console.error('create running lock failed, err: ' + err);
    }
});
```

#### runningLock.createRunningLock(deprecated)

createRunningLock(name: string, type: RunningLockType): Promise<RunningLock>


从API version 7开始支持，从API version 9开始不再维护，建议使用[runningLock.create](#ZH-CN_TOPIC_0000002553361513__runninglockcreate9)替代。

**方法介绍：** 创建RunningLock锁。使用Promise异步回调。

**系统能力：** SystemCapability.PowerManager.PowerManager.Core

**需要权限：** ohos.permission.RUNNING_LOCK

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 锁的名字。 |
| type | RunningLockType | 是 | 要创建的锁的类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<RunningLock> | Promise对象，返回RunningLock锁对象。 |

**示例：**

```ets
runningLock.createRunningLock('running_lock_test', runningLock.RunningLockType.BACKGROUND)
.then((lock: runningLock.RunningLock) => {
    console.info('created running lock: ' + lock);
})
.catch((err: Error) => {
    console.error('create running lock failed, err: ' + err);
});
```

#### RunningLock

阻止系统睡眠的锁。

#### hold9+

hold(timeout: number): void

**方法介绍：** 锁定和持有RunningLock。

**系统能力：** SystemCapability.PowerManager.PowerManager.Core

**需要权限：** ohos.permission.RUNNING_LOCK

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| timeout | number | 是 | 锁定和持有RunningLock的时长，单位：毫秒。 该参数必须为数字类型： -1：永久持锁，需要主动释放。 0：默认3s后超时释放。 >0：按传入值超时释放。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types. |
| 201 | If the permission is denied. |

**示例：**

```ets
// RunningLockTest.ets
class RunningLockTest {
    public static recordLock: runningLock.RunningLock;

    public static holdRunningLock(): void {
        if (RunningLockTest.recordLock) {
            RunningLockTest.recordLock.hold(500);
            console.info('hold running lock success');
        } else {
            runningLock.create('running_lock_test', runningLock.RunningLockType.PROXIMITY_SCREEN_CONTROL, (err: Error, lock: runningLock.RunningLock) => {
                if (typeof err === 'undefined') {
                    console.info('create running lock: ' + lock);
                    RunningLockTest.recordLock = lock;
                    try {
                        lock.hold(500);
                        console.info('hold running lock success');
                    } catch(err) {
                        console.error('hold running lock failed, err: ' + err);
                    }
                } else {
                    console.error('create running lock failed, err: ' + err);
                }
            });
        }
```

#### unhold9+

unhold(): void

**方法介绍：** 释放RunningLock锁。

**系统能力：** SystemCapability.PowerManager.PowerManager.Core

**需要权限：** ohos.permission.RUNNING_LOCK

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | If the permission is denied. |

**示例：**

```ets
// RunningLockTest.ets
class RunningLockTest {
    public static recordLock: runningLock.RunningLock;

    public static unholdRunningLock(): void {
        if (RunningLockTest.recordLock) {
            RunningLockTest.recordLock.unhold();
            console.info('unhold running lock success');
        } else {
            runningLock.create('running_lock_test', runningLock.RunningLockType.PROXIMITY_SCREEN_CONTROL, (err: Error, lock: runningLock.RunningLock) => {
                if (typeof err === 'undefined') {
                    console.info('create running lock: ' + lock);
                    RunningLockTest.recordLock = lock;
                    try {
                        lock.unhold();
                        console.info('unhold running lock success');
                    } catch(err) {
                        console.error('unhold running lock failed, err: ' + err);
                    }
                } else {
                    console.error('create running lock failed, err: ' + err);
                }
            });
        }
```

#### isHolding9+

isHolding(): boolean

**方法介绍：** 查询当前RunningLock是持有状态还是释放状态。

**系统能力：** SystemCapability.PowerManager.PowerManager.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回true表示当前RunningLock是持有状态，返回false表示当前RunningLock是释放状态。 |

**示例：**

```ets
// RunningLockTest.ets
class RunningLockTest {
    public static recordLock: runningLock.RunningLock;

    public static isHoldingRunningLock(): void {
        if (RunningLockTest.recordLock) {
            let isHolding = RunningLockTest.recordLock.isHolding();
            console.info('check running lock holding status: ' + isHolding);
        } else {
            runningLock.create('running_lock_test', runningLock.RunningLockType.PROXIMITY_SCREEN_CONTROL, (err: Error, lock: runningLock.RunningLock) => {
                if (typeof err === 'undefined') {
                    console.info('create running lock: ' + lock);
                    RunningLockTest.recordLock = lock;
                    let isHolding = lock.isHolding();
                    console.info('check running lock holding status: ' + isHolding);
                } else {
                    console.error('create running lock failed, err: ' + err);
                }
            });
        }
```

#### lock(deprecated)

lock(timeout: number): void


从API version 7开始支持，从API version 9开始不再维护，建议使用[RunningLock.hold](#ZH-CN_TOPIC_0000002553361513__hold9)替代。

**方法介绍：** 锁定和持有RunningLock。

**系统能力：** SystemCapability.PowerManager.PowerManager.Core

**需要权限：** ohos.permission.RUNNING_LOCK

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| timeout | number | 是 | 锁定和持有RunningLock的时长，单位：毫秒。 |

**示例：**

```ets
runningLock.createRunningLock('running_lock_test', runningLock.RunningLockType.BACKGROUND)
.then((lock: runningLock.RunningLock) => {
    lock.lock(500);
    console.info('create running lock and lock success');
})
.catch((err: Error) => {
    console.error('create running lock failed, err: ' + err);
});
```

#### unlock(deprecated)

unlock(): void


从API version 7开始支持，从API version 9开始不再维护，建议使用[RunningLock.unhold](#ZH-CN_TOPIC_0000002553361513__unhold9)替代。

**方法介绍：** 释放RunningLock锁。

**系统能力：** SystemCapability.PowerManager.PowerManager.Core

**需要权限：** ohos.permission.RUNNING_LOCK

**示例：**

```ets
runningLock.createRunningLock('running_lock_test', runningLock.RunningLockType.BACKGROUND)
.then((lock: runningLock.RunningLock) => {
    lock.unlock();
    console.info('create running lock and unlock success');
})
.catch((err: Error) => {
    console.error('create running lock failed, err: ' + err);
});
```

#### isUsed(deprecated)

isUsed(): boolean


从API version 7开始支持，从API version 9开始不再维护，建议使用[RunningLock.isHolding](#ZH-CN_TOPIC_0000002553361513__isholding9)替代。

**方法介绍：** 查询当前RunningLock是持有状态还是释放状态。

**系统能力：** SystemCapability.PowerManager.PowerManager.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回true表示当前RunningLock是持有状态，返回false表示当前RunningLock是释放状态。 |

**示例：**

```ets
runningLock.createRunningLock('running_lock_test', runningLock.RunningLockType.BACKGROUND)
.then((lock: runningLock.RunningLock) => {
    let isUsed = lock.isUsed();
    console.info('check running lock used status: ' + isUsed);
})
.catch((err: Error) => {
    console.error('check running lock used status failed, err: ' + err);
});
```

#### RunningLockType

RunningLock锁的类型。

**系统能力：** SystemCapability.PowerManager.PowerManager.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| BACKGROUND(deprecated) | 1 | 阻止系统睡眠的锁。 说明： 从API version 7开始支持，从API version 10开始废弃。 |
PROXIMITY_SCREEN_CONTROL2接近光锁，使能接近光传感器，并根据传感器与障碍物的距离远近发起亮灭屏流程。| BACKGROUND_USER_IDLE23+ | 129 | 阻止系统自动睡眠的后台闲时任务锁，持锁能保证一段时间用户不活动后系统不进入自动睡眠。注意：不能阻止如PC合盖等场景系统进入强制睡眠，使用方必须监听进入强制睡眠公共事件，监听到事件后释放该锁。该类型锁行为存在设备差异，使用该类型锁请参考阻止系统闲时进入睡眠开发指南。 |