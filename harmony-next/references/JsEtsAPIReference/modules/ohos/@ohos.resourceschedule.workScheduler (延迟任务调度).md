# @ohos.resourceschedule.workScheduler (延迟任务调度)

本模块提供延迟任务注册、取消、查询的能力。在开发过程中，对于实时性要求不高的任务，可以调用本模块接口注册延迟任务，在系统空闲时根据性能、功耗、热等情况进行调度执行。开发指导请参考[延迟任务开发指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/work-scheduler)。

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

#### 导入模块

```ets
import { workScheduler } from '@kit.BackgroundTasksKit';
```

#### workScheduler.startWork

startWork(work: WorkInfo): void

申请延迟任务，成功后会把任务添加到执行队列，满足触发条件后由系统调度执行。

**系统能力**：SystemCapability.ResourceSchedule.WorkScheduler

**参数**：

参数名类型必填说明work[WorkInfo](#ZH-CN_TOPIC_0000002529445205__workinfo)是指定延迟任务具体信息，比如延迟任务ID、触发条件等。

**错误码**：

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[workScheduler错误码](../../errors/workScheduler错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed.9700001Memory operation failed.9700002Failed to write data into parcel. Possible reasons: 1. Invalid parameters; 2. Failed to apply for memory.9700003System service operation failed.9700004Check on workInfo failed.9700005Calling startWork failed.

**示例**：

```ets
  import { BusinessError } from '@kit.BasicServicesKit';
  import { workScheduler } from '@kit.BackgroundTasksKit';

  let workInfo: workScheduler.WorkInfo = {
      workId: 1,
      batteryStatus:workScheduler.BatteryStatus.BATTERY_STATUS_LOW,
      isRepeat: false,
      isPersisted: true,
      bundleName: "com.example.myapplication",
      abilityName: "MyExtension",
      parameters: {
          mykey0: 1,
          mykey1: "string value",
          mykey2: true,
          mykey3: 1.5
      }
  }
  try{
    workScheduler.startWork(workInfo);
    console.info('workschedulerLog startWork success');
  } catch (error) {
    console.error(`workschedulerLog startwork failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}`);
  }
```

#### workScheduler.stopWork

stopWork(work: WorkInfo, needCancel?: boolean): void

取消延迟任务。

**系统能力**：SystemCapability.ResourceSchedule.WorkScheduler

**参数**：

参数名类型必填说明work[WorkInfo](#ZH-CN_TOPIC_0000002529445205__workinfo)是要停止或移除的延迟任务。needCancelboolean否

是否需要移除任务。

true表示停止并移除，false表示只停止不移除。默认为false。

**错误码**：

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[workScheduler错误码](../../errors/workScheduler错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed.9700001Memory operation failed.9700002Failed to write data into parcel. Possible reasons: 1. Invalid parameters; 2. Failed to apply for memory.9700003System service operation failed.9700004Check on workInfo failed.

**示例**：

```ets
  import { BusinessError } from '@kit.BasicServicesKit';
  import { workScheduler } from '@kit.BackgroundTasksKit';

  let workInfo: workScheduler.WorkInfo = {
      workId: 1,
      batteryStatus:workScheduler.BatteryStatus.BATTERY_STATUS_LOW,
      isRepeat: false,
      isPersisted: true,
      bundleName: "com.example.myapplication",
      abilityName: "MyExtension",
      parameters: {
          mykey0: 1,
          mykey1: "string value",
          mykey2: true,
          mykey3: 1.5
      }
     }
  try{
    workScheduler.stopWork(workInfo, false);
    console.info('workschedulerLog stopWork success');
  } catch (error) {
    console.error(`workschedulerLog stopWork failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}`);
  }
```

#### workScheduler.getWorkStatus

getWorkStatus(workId: number, callback : AsyncCallback<WorkInfo>): void

通过workId获取延迟任务，使用Callback异步回调。

**系统能力**：SystemCapability.ResourceSchedule.WorkScheduler

**参数**：

参数名类型必填说明workIdnumber是延迟任务Id。callbackAsyncCallback<[WorkInfo](#ZH-CN_TOPIC_0000002529445205__workinfo)>是回调函数。如果workId有效，则返回从WorkSchedulerService获取的任务，否则抛出异常。

**错误码**：

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[workScheduler错误码](../../errors/workScheduler错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: Parameter verification failed.9700001Memory operation failed.9700002Failed to write data into parcel. Possible reasons: 1. Invalid parameters; 2. Failed to apply for memory.9700003System service operation failed.9700004Check on workInfo failed.

**示例**：

```ets
  import { BusinessError } from '@kit.BasicServicesKit';
  import { workScheduler } from '@kit.BackgroundTasksKit';

  workScheduler.getWorkStatus(50, (error: BusinessError, res: workScheduler.WorkInfo) => {
    if (error) {
      console.error(`workschedulerLog getWorkStatus failed. code is ${error.code} message is ${error.message}`);
    } else {
      console.info(`workschedulerLog getWorkStatus success, ${JSON.stringify(res)}`);
    }
  });
```

#### workScheduler.getWorkStatus

getWorkStatus(workId: number): Promise<WorkInfo>

通过workId获取延迟任务，使用Promise异步回调。

**系统能力**：SystemCapability.ResourceSchedule.WorkScheduler

**参数**：

参数名类型必填说明workIdnumber是延迟任务Id。

**返回值**：

类型说明Promise<[WorkInfo](#ZH-CN_TOPIC_0000002529445205__workinfo)>Promise对象，如果workId有效，则返回从WorkSchedulerService获取的任务，否则抛出异常。

**错误码**：

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[workScheduler错误码](../../errors/workScheduler错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: Parameter verification failed.9700001Memory operation failed.9700002Failed to write data into parcel. Possible reasons: 1. Invalid parameters; 2. Failed to apply for memory.9700003System service operation failed.9700004Check on workInfo failed.

**示例**：

```ets
  import { BusinessError } from '@kit.BasicServicesKit';
  import { workScheduler } from '@kit.BackgroundTasksKit';

  workScheduler.getWorkStatus(50).then((res: workScheduler.WorkInfo) => {
    console.info(`workschedulerLog getWorkStatus success, ${JSON.stringify(res)}`);
  }).catch((error: BusinessError) => {
    console.error(`workschedulerLog getWorkStatus failed. code is ${error.code} message is ${error.message}`);
  })
```

#### workScheduler.obtainAllWorks(deprecated)

obtainAllWorks(callback : AsyncCallback<void>) : Array<WorkInfo>

获取当前应用所有的延迟任务，使用Callback异步回调。

从API version 9开始支持，从API version 10开始废弃，建议使用[workScheduler.obtainAllWorks10+](#ZH-CN_TOPIC_0000002529445205__workschedulerobtainallworks10)替代。

**系统能力**：SystemCapability.ResourceSchedule.WorkScheduler

**参数**：

参数名类型必填说明callbackAsyncCallback<void>是回调函数，获取成功时，err为undefined，否则为错误对象。

**返回值**：

类型说明Array<[WorkInfo](#ZH-CN_TOPIC_0000002529445205__workinfo)>延迟任务列表，如果已添加延迟任务到执行队列，则返回当前应用所有的延迟任务列表；否则返回空列表。

**错误码**：

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[workScheduler错误码](../../errors/workScheduler错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types.9700001Memory operation failed.9700002Failed to write data into parcel. Possible reasons: 1. Invalid parameters; 2. Failed to apply for memory.9700003System service operation failed.

#### workScheduler.obtainAllWorks10+

obtainAllWorks(callback : AsyncCallback<Array<WorkInfo>>): void

获取当前应用所有的延迟任务，使用Callback异步回调。

**系统能力**：SystemCapability.ResourceSchedule.WorkScheduler

**参数**：

参数名类型必填说明callbackAsyncCallback<Array<WorkInfo>>是回调函数，获取成功时，err为undefined，否则为错误对象。

**错误码**：

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[workScheduler错误码](../../errors/workScheduler错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types.9700001Memory operation failed.9700002Failed to write data into parcel. Possible reasons: 1. Invalid parameters; 2. Failed to apply for memory.9700003System service operation failed.

**示例**：

```ets
  import { BusinessError } from '@kit.BasicServicesKit';
  import { workScheduler } from '@kit.BackgroundTasksKit';

  workScheduler.obtainAllWorks((error: BusinessError, res: Array<workScheduler.WorkInfo>) =>{
    if (error) {
      console.error(`workschedulerLog obtainAllWorks failed. code is ${error.code} message is ${error.message}`);
    } else {
      console.info(`workschedulerLog obtainAllWorks success, data is: ${JSON.stringify(res)}`);
    }
  });
```

#### workScheduler.obtainAllWorks

obtainAllWorks(): Promise<Array<WorkInfo>>

获取当前应用所有的延迟任务，使用Promise异步回调。

**系统能力**：SystemCapability.ResourceSchedule.WorkScheduler

**返回值**：

类型说明Promise<Array<[WorkInfo](#ZH-CN_TOPIC_0000002529445205__workinfo)>>Promise对象，返回当前应用所有的延迟任务。

**错误码**：

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[workScheduler错误码](../../errors/workScheduler错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types.9700001Memory operation failed.9700002Failed to write data into parcel. Possible reasons: 1. Invalid parameters; 2. Failed to apply for memory.9700003System service operation failed.

**示例**：

```ets
  import { BusinessError } from '@kit.BasicServicesKit';
  import { workScheduler } from '@kit.BackgroundTasksKit';

  workScheduler.obtainAllWorks().then((res: Array<workScheduler.WorkInfo>) => {
    console.info(`workschedulerLog obtainAllWorks success, data is: ${JSON.stringify(res)}`);
  }).catch((error: BusinessError) => {
    console.error(`workschedulerLog obtainAllWorks failed. code is ${error.code} message is ${error.message}`);
  })
```

#### workScheduler.stopAndClearWorks

stopAndClearWorks(): void

停止和取消当前应用所有的延迟任务。

**系统能力**：SystemCapability.ResourceSchedule.WorkScheduler

**错误码**：

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[workScheduler错误码](../../errors/workScheduler错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types.9700001Memory operation failed.9700002Failed to write data into parcel. Possible reasons: 1. Invalid parameters; 2. Failed to apply for memory.9700003System service operation failed.

**示例**：

```ets
  import { BusinessError } from '@kit.BasicServicesKit';
  import { workScheduler } from '@kit.BackgroundTasksKit';

  try{
    workScheduler.stopAndClearWorks();
    console.info(`workschedulerLog stopAndClearWorks success`);
  } catch (error) {
    console.error(`workschedulerLog stopAndClearWorks failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}`);
  }
```

#### workScheduler.isLastWorkTimeOut(deprecated)

isLastWorkTimeOut(workId: number, callback : AsyncCallback<void>): boolean

从API version 9开始支持，从API version 10开始废弃，建议使用[workScheduler.isLastWorkTimeOut10+](#ZH-CN_TOPIC_0000002529445205__workschedulerislastworktimeout10)替代。

检查延迟任务的最后一次执行是否超时，使用Callback异步回调。

**系统能力**：SystemCapability.ResourceSchedule.WorkScheduler

**参数**：

参数名类型必填说明workIdnumber是指定延迟任务的Id。callbackAsyncCallback<void>是回调函数。

**返回值**：

类型说明boolean检查延迟任务最后一次执行是否超时，如果workId有效，则返回从WorkSchedulerService获取的任务最后一次执行是否超时；否则，抛出异常。true，对应workId延迟任务最后一次执行超时，false，对应workId延迟任务最后一次执行未超时。

**错误码**：

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[workScheduler错误码](../../errors/workScheduler错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: Parameter verification failed.9700001Memory operation failed.9700002Failed to write data into parcel. Possible reasons: 1. Invalid parameters; 2. Failed to apply for memory.9700003System service operation failed.9700004Check on workInfo failed.

#### workScheduler.isLastWorkTimeOut10+

isLastWorkTimeOut(workId: number, callback : AsyncCallback<boolean>): void

检查延迟任务的最后一次执行是否超时，使用Callback异步回调。

**系统能力**：SystemCapability.ResourceSchedule.WorkScheduler

**参数**：

参数名类型必填说明workIdnumber是指定延迟任务的Id。callbackAsyncCallback<boolean>是回调函数。

**错误码**：

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[workScheduler错误码](../../errors/workScheduler错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: Parameter verification failed.9700001Memory operation failed.9700002Failed to write data into parcel. Possible reasons: 1. Invalid parameters; 2. Failed to apply for memory.9700003System service operation failed.9700004Check on workInfo failed.

**示例**：

```ets
  import { BusinessError } from '@kit.BasicServicesKit';
  import { workScheduler } from '@kit.BackgroundTasksKit';

  workScheduler.isLastWorkTimeOut(500, (error: BusinessError, res: boolean) =>{
    if (error) {
      console.error(`workschedulerLog isLastWorkTimeOut failed. code is ${error.code} message is ${error.message}`);
    } else {
      console.info(`workschedulerLog isLastWorkTimeOut success, data is: ${res}`);
    }
  });
```

#### workScheduler.isLastWorkTimeOut

isLastWorkTimeOut(workId: number): Promise<boolean>

检查延迟任务的最后一次执行是否超时，使用Promise形式返回。

**系统能力**：SystemCapability.ResourceSchedule.WorkScheduler

**参数**：

参数名类型必填说明workIdnumber是指定延迟任务的Id。

**返回值**：

类型说明Promise<boolean>Promise对象。返回true表示指定任务的最后一次执行超时，false表示未超时。

**错误码**：

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[workScheduler错误码](../../errors/workScheduler错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: Parameter verification failed.9700001Memory operation failed.9700002Failed to write data into parcel. Possible reasons: 1. Invalid parameters; 2. Failed to apply for memory.9700003System service operation failed.9700004Check on workInfo failed.

**示例**：

```ets
  import { BusinessError } from '@kit.BasicServicesKit';
  import { workScheduler } from '@kit.BackgroundTasksKit';

  workScheduler.isLastWorkTimeOut(500)
    .then((res: boolean) => {
      console.info(`workschedulerLog isLastWorkTimeOut success, data is: ${res}`);
    })
    .catch((error: BusinessError) =>  {
      console.error(`workschedulerLog isLastWorkTimeOut failed. code is ${error.code} message is ${error.message}`);
    });
```

#### WorkInfo

延迟任务的具体信息, 用于设置延迟任务的触发条件等。

WorkInfo参数设置时需遵循以下规则：

1. workId、bundleName、abilityName为必填项，bundleName需为本应用包名。
1. 携带参数信息仅支持number、string、boolean三种类型。
1. 至少设置一个满足的条件，包括网络类型、充电类型、存储状态、电池状态等。
1. 对于循环任务，任务执行间隔至少2小时。设置了循环任务时间间隔时，须同时设置是否循环或循环次数中的一个。
1. 对于可选参数，如果缺省表示延迟任务的触发不依赖该条件。

**系统能力**：SystemCapability.ResourceSchedule.WorkScheduler

名称类型只读可选说明workIdnumber否否延迟任务ID。bundleNamestring否否延迟任务所在应用的包名。abilityNamestring否否包内ability名称。networkType[NetworkType](#ZH-CN_TOPIC_0000002529445205__networktype)否是网络类型。isChargingboolean否是

是否充电，默认为false。

- true表示充电触发延迟任务回调。

- false表示不充电触发延迟任务回调。

chargerType[ChargingType](#ZH-CN_TOPIC_0000002529445205__chargingtype)否是充电类型。batteryLevelnumber否是电量。batteryStatus[BatteryStatus](#ZH-CN_TOPIC_0000002529445205__batterystatus)否是电池状态。storageRequest[StorageRequest](#ZH-CN_TOPIC_0000002529445205__storagerequest)否是存储状态。isRepeatboolean否是

是否循环任务，默认为false。

- true表示循环任务。

- false表示非循环任务。

repeatCycleTimenumber否是循环间隔，单位为毫秒。repeatCountnumber否是循环次数。isPersistedboolean否是

注册的延迟任务是否可保存在系统中，默认为false。

- true表示可保存，即系统重启后，任务可恢复。

- false表示不可保存。

isDeepIdleboolean否是

是否要求设备进入空闲状态，默认为false。

- true表示需要。

- false表示不需要。

idleWaitTimenumber否是空闲等待时间，单位为毫秒。parametersRecord<string, number | string | boolean>否是携带参数信息。earliestStartTime22+number否是任务首次执行时间距离任务申请时间的间隔，单位为毫秒，默认为0，范围大于等于0。

#### NetworkType

触发延迟任务回调的网络类型。

**系统能力**：SystemCapability.ResourceSchedule.WorkScheduler

名称值说明NETWORK_TYPE_ANY0表示这个触发条件是任何类型的网络连接。NETWORK_TYPE_MOBILE1表示这个触发条件是Mobile网络连接。NETWORK_TYPE_WIFI2表示这个触发条件是Wifi类型的网络连接。NETWORK_TYPE_BLUETOOTH3表示这个触发条件是Bluetooth网络连接。NETWORK_TYPE_WIFI_P2P4表示这个触发条件是Wifi P2P网络连接。NETWORK_TYPE_ETHERNET5表示这个触发条件是有线网络连接。

#### ChargingType

触发延迟任务回调的充电类型。

**系统能力**：SystemCapability.ResourceSchedule.WorkScheduler

名称值说明CHARGING_PLUGGED_ANY0表示这个触发条件是任何类型的充电器连接。CHARGING_PLUGGED_AC1表示这个触发条件是直流充电器连接。CHARGING_PLUGGED_USB2表示这个触发条件是USB充连接。CHARGING_PLUGGED_WIRELESS3表示这个触发条件是无线充电器连接。

#### BatteryStatus

触发延迟任务回调的电池状态。

**系统能力**：SystemCapability.ResourceSchedule.WorkScheduler

名称值说明BATTERY_STATUS_LOW0表示这个触发条件是低电告警。BATTERY_STATUS_OKAY1表示这个触发条件是从低电恢复到正常电量。BATTERY_STATUS_LOW_OR_OKAY2表示这个触发条件是从低电恢复到正常电量或者低电告警。

#### StorageRequest

触发延迟任务回调的存储状态。

**系统能力**：SystemCapability.ResourceSchedule.WorkScheduler

名称值说明STORAGE_LEVEL_LOW0表示这个触发条件是存储空间不足。STORAGE_LEVEL_OKAY1表示这个触发条件是从存储空间不足恢复到正常。STORAGE_LEVEL_LOW_OR_OKAY2表示这个触发条件是存储空间不足或者从存储空间不足恢复到正常。