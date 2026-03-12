# @ohos.faultLogger (故障日志获取)

应用可以使用faultLogger接口查询系统侧缓存的当前应用的故障日志。接口以应用包名和系统分配的UID作为唯一键值。

系统侧保存的应用故障日志数量受系统日志的压力限制，推荐使用[@ohos.hiviewdfx.hiAppEvent](@ohos.hiviewdfx.hiAppEvent (应用事件打点).md)订阅APP_CRASH及APP_FREEZE等故障事件。

本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口从API version 18开始废弃使用, 该接口不再维护。后续版本推荐使用[@ohos.hiviewdfx.hiAppEvent](@ohos.hiviewdfx.hiAppEvent (应用事件打点).md)订阅APP_CRASH，APP_FREEZE事件。

查阅[从Faultlogger接口迁移崩溃事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-crash-events-arkts#从faultlogger接口迁移崩溃事件)，了解使用hiAppEvent订阅APP_CRASH的具体信息。

查阅[从Faultlogger接口迁移应用冻屏事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-freeze-events-arkts#从faultlogger接口迁移应用冻屏事件)，了解使用hiAppEvent订阅APP_FREEZE的具体信息。

#### 导入模块

```ets
import { FaultLogger } from '@kit.PerformanceAnalysisKit';
```

#### FaultType

故障类型枚举。

**系统能力**：SystemCapability.HiviewDFX.Hiview.FaultLogger

名称值说明NO_SPECIFIC0不区分故障类型。CPP_CRASH2C++程序故障类型。JS_CRASH3JS程序故障类型。APP_FREEZE4应用程序卡死故障类型。

#### FaultLogInfo

故障信息数据结构，获取到的故障信息的数据结构。

**系统能力**：SystemCapability.HiviewDFX.Hiview.FaultLogger

名称类型只读可选说明pidnumber否否故障进程的进程id。uidnumber否否故障进程的用户id。type[FaultType](#ZH-CN_TOPIC_0000002529445629__faulttype)否否故障类型。timestampnumber否否日志生成时的毫秒级时间戳。reasonstring否否发生故障的原因。modulestring否否发生故障的模块。summarystring否否故障的概要。fullLogstring否否故障日志全文。

#### FaultLogger.query9+

query(faultType: FaultType, callback: AsyncCallback<Array<FaultLogInfo>>) : void

获取当前应用故障信息，该方法通过回调方式获取故障信息数组，故障信息数组内最多上报10份故障信息。

**系统能力**：SystemCapability.HiviewDFX.Hiview.FaultLogger

**参数：**

参数名类型必填说明faultType[FaultType](#ZH-CN_TOPIC_0000002529445629__faulttype)是输入要查询的故障类型。callbackAsyncCallback<Array<[FaultLogInfo](#ZH-CN_TOPIC_0000002529445629__faultloginfo)>>是

回调函数，在回调函数中获取故障信息数组。

- value拿到故障信息数组；value为undefined表示获取过程中出现异常，error返回错误提示字符串。

**错误码：**

以下错误码的详细介绍参见[faultLogger错误码](Faultlogger 错误码.md)。

错误码ID错误信息401The parameter check failed, Parameter type error.801The specified SystemCapability name was not found.10600001The service is not started or is faulty.

**示例：**

```ets
import { FaultLogger } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

function queryFaultLogCallback(error: BusinessError, value: Array<FaultLogger.FaultLogInfo>) {
    if (error) {
        console.error(`error code:${error.code}, error msg:${error.message}`);
    } else {
        console.info("value length is " + value.length);
        let len: number = value.length;
        for (let i = 0; i < len; i++) {
            console.info(`log: ${i}`);
            console.info(`Log pid: ${value[i].pid}`);
            console.info(`Log uid: ${value[i].uid}`);
            console.info(`Log type: ${value[i].type}`);
            console.info(`Log timestamp: ${value[i].timestamp}`);
            console.info(`Log reason: ${value[i].reason}`);
            console.info(`Log module: ${value[i].module}`);
            console.info(`Log summary: ${value[i].summary}`);
            console.info(`Log text: ${value[i].fullLog}`);
        }
    }
}
try {
    FaultLogger.query(FaultLogger.FaultType.JS_CRASH, queryFaultLogCallback);
} catch (err) {
    console.error(`code: ${(err as BusinessError).code}, message: ${(err as BusinessError).message}`);
}
```

#### FaultLogger.query9+

query(faultType: FaultType) : Promise<Array<FaultLogInfo>>

获取当前应用故障信息，该方法通过Promise方式返回故障信息数组，故障信息数组内最多上报10份故障信息。

**系统能力**：SystemCapability.HiviewDFX.Hiview.FaultLogger

**参数：**

参数名类型必填说明faultType[FaultType](#ZH-CN_TOPIC_0000002529445629__faulttype)是输入要查询的故障类型。

**返回值：**

类型说明Promise<Array<[FaultLogInfo](#ZH-CN_TOPIC_0000002529445629__faultloginfo)>>

Promise实例，可以在其then()方法中获取故障信息实例，也可以使用await。

- value拿到故障信息数组；value为undefined表示获取过程中出现异常。

**错误码：**

以下错误码的详细介绍参见[faultLogger错误码](Faultlogger 错误码.md)。

错误码ID错误信息401The parameter check failed, Parameter type error.801The specified SystemCapability name was not found.10600001The service is not started or is faulty.

**示例：**

```ets
import { FaultLogger } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

async function getLog() {
  try {
    let value: Array<FaultLogger.FaultLogInfo> = await FaultLogger.query(FaultLogger.FaultType.JS_CRASH);
    if (value) {
      console.info(`value length: ${value.length}`);
      let len: number = value.length;
      for (let i = 0; i < len; i++) {
        console.info(`log: ${i}`);
        console.info(`Log pid: ${value[i].pid}`);
        console.info(`Log uid: ${value[i].uid}`);
        console.info(`Log type: ${value[i].type}`);
        console.info(`Log timestamp: ${value[i].timestamp}`);
        console.info(`Log reason: ${value[i].reason}`);
        console.info(`Log module: ${value[i].module}`);
        console.info(`Log summary: ${value[i].summary}`);
        console.info(`Log text: ${value[i].fullLog}`);
      }
    }
  } catch (err) {
    console.error(`code: ${(err as BusinessError).code}, message: ${(err as BusinessError).message}`);
  }
}
```

#### FaultLogger.querySelfFaultLog(deprecated)

querySelfFaultLog(faultType: FaultType, callback: AsyncCallback<Array<FaultLogInfo>>) : void

从 API Version 9 开始废弃，建议使用[FaultLogger.query](#ZH-CN_TOPIC_0000002529445629__faultloggerquery9)替代。

获取当前应用故障信息，该方法通过回调方式获取故障信息数组，故障信息数组内最多上报10份故障信息。

**系统能力**：SystemCapability.HiviewDFX.Hiview.FaultLogger

**参数：**

参数名类型必填说明faultType[FaultType](#ZH-CN_TOPIC_0000002529445629__faulttype)是输入要查询的故障类型。callbackAsyncCallback<Array<[FaultLogInfo](#ZH-CN_TOPIC_0000002529445629__faultloginfo)>>是

回调函数，在回调函数中获取故障信息数组。

- value拿到故障信息数组；value为undefined表示获取过程中出现异常，error返回错误提示字符串。

**示例：**

```ets
import { FaultLogger } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

function queryFaultLogCallback(error: BusinessError, value: Array<FaultLogger.FaultLogInfo>) {
  if (error) {
    console.error(`error code:${error.code}, error msg:${error.message}`);
  } else {
    console.info(`value length: ${value.length}`);
    let len: number = value.length;
    for (let i = 0; i < len; i++) {
      console.info(`log: ${i}`);
      console.info(`Log pid: ${value[i].pid}`);
      console.info(`Log uid: ${value[i].uid}`);
      console.info(`Log type: ${value[i].type}`);
      console.info(`Log timestamp: ${value[i].timestamp}`);
      console.info(`Log reason: ${value[i].reason}`);
      console.info(`Log module: ${value[i].module}`);
      console.info(`Log summary: ${value[i].summary}`);
      console.info(`Log text: ${value[i].fullLog}`);
    }
  }
}
FaultLogger.querySelfFaultLog(FaultLogger.FaultType.JS_CRASH, queryFaultLogCallback);
```

#### FaultLogger.querySelfFaultLog(deprecated)

querySelfFaultLog(faultType: FaultType) : Promise<Array<FaultLogInfo>>

从 API Version 9 开始废弃，建议使用[FaultLogger.query](#ZH-CN_TOPIC_0000002529445629__faultloggerquery9-1)替代。

获取当前应用故障信息，该方法通过Promise方式返回故障信息数组，故障信息数组内最多上报10份故障信息。

**系统能力**：SystemCapability.HiviewDFX.Hiview.FaultLogger

**参数：**

参数名类型必填说明faultType[FaultType](#ZH-CN_TOPIC_0000002529445629__faulttype)是输入要查询的故障类型。

**返回值：**

类型说明Promise<Array<[FaultLogInfo](#ZH-CN_TOPIC_0000002529445629__faultloginfo)>>

Promise实例，可以在其then()方法中获取故障信息实例，也可以使用await。

- value拿到故障信息数组；value为undefined表示获取过程中出现异常。

**示例：**

```ets
import { FaultLogger } from '@kit.PerformanceAnalysisKit';

async function getLog() {
  let value: Array<FaultLogger.FaultLogInfo> = await FaultLogger.querySelfFaultLog(FaultLogger.FaultType.JS_CRASH);
  if (value) {
    console.info(`value length: ${value.length}`);
    let len: number = value.length;
    for (let i = 0; i < len; i++) {
      console.info(`log: ${i}`);
      console.info(`Log pid: ${value[i].pid}`);
      console.info(`Log uid: ${value[i].uid}`);
      console.info(`Log type: ${value[i].type}`);
      console.info(`Log timestamp: ${value[i].timestamp}`);
      console.info(`Log reason: ${value[i].reason}`);
      console.info(`Log module: ${value[i].module}`);
      console.info(`Log summary: ${value[i].summary}`);
      console.info(`Log text: ${value[i].fullLog}`);
    }
  }
}
```