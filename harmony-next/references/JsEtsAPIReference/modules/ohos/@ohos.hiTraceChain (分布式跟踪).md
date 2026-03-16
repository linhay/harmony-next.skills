# @ohos.hiTraceChain (分布式跟踪)

本模块提供了端侧业务流程调用链跟踪的打点能力，包括业务流程跟踪的启动、结束、信息埋点等能力。

本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { hiTraceChain } from '@kit.PerformanceAnalysisKit';
```

#### HiTraceFlag

跟踪标志组合类型枚举。

**系统能力**：SystemCapability.HiviewDFX.HiTrace

名称值说明DEFAULT0缺省标志。INCLUDE_ASYNC1

异步调用标志。

设置该标志，同时跟踪同步和异步调用；缺省只跟踪同步调用。

DONOT_CREATE_SPAN1 << 1

无分支标志。

设置该标志，不创建分支信息；缺省创建分支信息。

TP_INFO1 << 2

埋点标志。

调试场景下设置该标志，调用信息埋点接口[tracepoint()](#ZH-CN_TOPIC_0000002529285651__hitracechaintracepoint)时，会打印埋点信息hilog日志；缺省不打印埋点信息hilog日志。

NO_BE_INFO1 << 3

无开始结束信息标志。

调试场景下设置该标志，调用开始跟踪接口[begin()](#ZH-CN_TOPIC_0000002529285651__hitracechainbegin)和结束跟踪接口[end()](#ZH-CN_TOPIC_0000002529285651__hitracechainend)时，分别会打印开始、结束跟踪信息hilog日志；缺省不打印开始、结束跟踪信息hilog日志。

DISABLE_LOG1 << 4

日志关联标志。

设置该标志，不会在hilog日志中附加HiTraceId信息；缺省会在hilog日志中附加HiTraceId信息。

FAILURE_TRIGGER1 << 5故障触发标志。预置标志，暂未启用。D2D_TP_INFO1 << 6

设备间埋点标志。TP_INFO的一个子集，调试场景下使用。

当已设置TP_INFO标志时，D2D_TP_INFO标志不生效；

当未设置TP_INFO标志时，设置D2D_TP_INFO标志，此时调用信息埋点接口[tracepoint()](#ZH-CN_TOPIC_0000002529285651__hitracechaintracepoint)，仅当mode参数为设备间通信DEVICE的情况下，会打印埋点信息hilog日志。

#### HiTraceTracepointType

跟踪埋点类型枚举。

**系统能力**：SystemCapability.HiviewDFX.HiTrace

名称值说明CS0客户端发送。CR1客户端接收。SS2服务端发送。SR3服务端接收。GENERAL4通用类型，标识CS、CR、SS、SR四种场景之外的埋点。

#### HiTraceCommunicationMode

跟踪通信类型枚举。

**系统能力**：SystemCapability.HiviewDFX.HiTrace

名称值说明DEFAULT0缺省通信类型。THREAD1线程间通信。PROCESS2进程间通信。DEVICE3设备间通信。

#### HiTraceId

此接口为HiTraceId对象接口。

**系统能力**：SystemCapability.HiviewDFX.HiTrace

名称类型只读可选说明chainIdbigint否否跟踪链标识。spanIdnumber否是分支标识，默认值为0。parentSpanIdnumber否是父分支标识，默认值为0。flagsnumber否是跟踪标志位，默认值为0。

#### hiTraceChain.begin

begin(name: string, flags?: number): HiTraceId

开始跟踪，同步接口。

当前线程TLS（Thread Local Storage，线程本地存储）中不存在有效的HiTraceId时，生成有效的HiTraceId并设置到当前线程TLS中，返回该HiTraceId。

当前线程TLS中已存在有效的HiTraceId时，不会开始新的跟踪，返回各属性值均为0的无效HiTraceId。

**系统能力**：SystemCapability.HiviewDFX.HiTrace

**参数：**

参数名类型必填说明namestring是跟踪业务名。flagsnumber否跟踪标志组合，具体可参考[HiTraceFlag](#ZH-CN_TOPIC_0000002529285651__hitraceflag)，默认值为0。

**返回值：**

类型说明[HiTraceId](#ZH-CN_TOPIC_0000002529285651__hitraceid)HiTraceId实例。

**示例：**

```ets
// 开始跟踪，跟踪标志是INCLUDE_ASYNC与DONOT_CREATE_SPAN的并集。
let traceId = hiTraceChain.begin("business", hiTraceChain.HiTraceFlag.INCLUDE_ASYNC | hiTraceChain.HiTraceFlag.DONOT_CREATE_SPAN);
// 若干业务逻辑完成后，结束跟踪。
hiTraceChain.end(traceId);
```

#### hiTraceChain.end

end(id: HiTraceId): void

结束跟踪，同步接口。

若给定的HiTraceId有效，且等于当前线程TLS中的HiTraceId，结束跟踪并将当前线程TLS中的HiTraceId设置为无效。

若给定的HiTraceId无效，或不等于当前线程TLS中的HiTraceId，结束跟踪失败，打印结束跟踪失败hilog日志。

**系统能力**：SystemCapability.HiviewDFX.HiTrace

**参数：**

参数名类型必填说明id[HiTraceId](#ZH-CN_TOPIC_0000002529285651__hitraceid)是HiTraceId实例。

**示例：**

```ets
// 开始跟踪，跟踪标志是DEFAULT。
let traceId = hiTraceChain.begin("business", hiTraceChain.HiTraceFlag.DEFAULT);
// 若干业务逻辑完成后，结束跟踪。
hiTraceChain.end(traceId);
```

#### hiTraceChain.getId

getId(): HiTraceId

获取跟踪标识，同步接口。

获取当前线程TLS中的HiTraceId。

**系统能力**：SystemCapability.HiviewDFX.HiTrace

**返回值：**

类型说明[HiTraceId](#ZH-CN_TOPIC_0000002529285651__hitraceid)HiTraceId实例。

**示例：**

```ets
// 开始跟踪，跟踪标志是DEFAULT。
let traceId = hiTraceChain.begin("business", hiTraceChain.HiTraceFlag.DEFAULT);
// 若干业务逻辑完成后，获取当前跟踪标识。
let curTraceId = hiTraceChain.getId();
// 同一跟踪链获取的跟踪标识的chainId一定相同。
if (curTraceId.chainId != traceId.chainId) {
// 基于异常场景的处理逻辑。
}
// 若干业务逻辑完成后，结束跟踪。
hiTraceChain.end(traceId);
```

#### hiTraceChain.setId

setId(id: HiTraceId): void

设置跟踪标识，同步接口。

将给定的HiTraceId设置到当前线程TLS中。若给定的HiTraceId无效，则不执行任何操作。

**系统能力**：SystemCapability.HiviewDFX.HiTrace

**参数：**

参数名类型必填说明id[HiTraceId](#ZH-CN_TOPIC_0000002529285651__hitraceid)是HiTraceId实例。

**示例：**

```ets
// 获取当前跟踪链中的跟踪标识。
let traceId = hiTraceChain.getId();
// 将获取的跟踪标识设置为当前traceId。
hiTraceChain.setId(traceId);
```

#### hiTraceChain.clearId

clearId(): void

清除跟踪标识，同步接口。

将当前线程TLS中的HiTraceId设置为无效。

**系统能力**：SystemCapability.HiviewDFX.HiTrace

**示例：**

```ets
// 业务开始前，尝试清除跟踪标识。
hiTraceChain.clearId();
// 开始跟踪，跟踪标志是DEFAULT。
let traceId = hiTraceChain.begin("business", hiTraceChain.HiTraceFlag.DEFAULT);
// 若干业务逻辑完成后，结束跟踪。
hiTraceChain.end(traceId);
```

#### hiTraceChain.createSpan

createSpan(): HiTraceId

创建跟踪分支，同步接口。

创建一个HiTraceId，使用当前线程TLS中的chainId、spanId初始化HiTraceId的chainId、parentSpanId，并为HiTraceId生成一个新的spanId，返回该HiTraceId。

**系统能力**：SystemCapability.HiviewDFX.HiTrace

**返回值：**

类型说明[HiTraceId](#ZH-CN_TOPIC_0000002529285651__hitraceid)HiTraceId实例。

**示例：**

```ets
// 开始跟踪，跟踪标志是DEFAULT。
let traceId = hiTraceChain.begin("business", hiTraceChain.HiTraceFlag.DEFAULT);
// 若干业务逻辑完成后，创建跟踪分支。
let spanTraceId = hiTraceChain.createSpan();
// 同一跟踪链的跟踪标识的chainId一定相同。
if (spanTraceId.chainId != traceId.chainId) {
// 基于异常场景的处理逻辑。
}
//业务结束，结束跟踪。
hiTraceChain.end(traceId);
```

#### hiTraceChain.tracepoint

tracepoint(mode: HiTraceCommunicationMode, type: HiTraceTracepointType, id: HiTraceId, msg?: string): void

[HiTraceMeter](@ohos.hiTraceMeter (性能打点).md)跟踪信息埋点，同步接口。

当type为客户端发送CS和服务端接收SC时，进行同步HiTraceMeter开始打点；当type为客户端接收CC和服务端发送SS时，进行同步HiTraceMeter结束打点；当type为通用类型GENERAL时，不会进行HiTraceMeter打点。

type为客户端发送CS和客户端接收CC的信息埋点需配套使用；type为服务端接收SC和服务端发送SS的信息埋点需配套使用。否则，HiTraceMeter开始与结束打点无法正常匹配。

**系统能力**：SystemCapability.HiviewDFX.HiTrace

**参数：**

参数名类型必填说明mode[HiTraceCommunicationMode](#ZH-CN_TOPIC_0000002529285651__hitracecommunicationmode)是信息埋点需要指定的跟踪通信模式。type[HiTraceTracepointType](#ZH-CN_TOPIC_0000002529285651__hitracetracepointtype)是信息埋点需要指定的跟踪埋点类型。id[HiTraceId](#ZH-CN_TOPIC_0000002529285651__hitraceid)是实施信息埋点操作的HiTraceId实例。msgstring否HiTraceMeter打点操作传入的trace说明信息。

**示例：**

```ets
// 开始跟踪，跟踪标志是INCLUDE_ASYNC与DONOT_CREATE_SPAN的并集。
let traceId = hiTraceChain.begin("business", hiTraceChain.HiTraceFlag.INCLUDE_ASYNC | hiTraceChain.HiTraceFlag.DONOT_CREATE_SPAN);
// 若干业务逻辑完成后，触发信息埋点操作。
hiTraceChain.tracepoint(hiTraceChain.HiTraceCommunicationMode.THREAD, hiTraceChain.HiTraceTracepointType.SS, traceId, "Just a example");
//业务结束，结束跟踪。
hiTraceChain.end(traceId);
```

#### hiTraceChain.isValid

isValid(id: HiTraceId): boolean

判断HiTraceId是否有效，同步接口。

**系统能力**：SystemCapability.HiviewDFX.HiTrace

**参数：**

参数名类型必填说明id[HiTraceId](#ZH-CN_TOPIC_0000002529285651__hitraceid)是需要判断是否有效的HiTraceId实例。

**返回值：**

类型说明booleantrue：HiTraceId有效；false：HiTraceId无效。

**示例：**

```ets
// 开始跟踪，跟踪标志是DEFAULT。
let traceId = hiTraceChain.begin("business", hiTraceChain.HiTraceFlag.DEFAULT);
// traceIdIsvalid为true
let traceIdIsvalid = hiTraceChain.isValid(traceId);
if (traceIdIsvalid) {
// 基于跟踪标识合法性校验成功的场景的处理逻辑。
}
//业务结束，结束跟踪。
hiTraceChain.end(traceId);
```

#### hiTraceChain.isFlagEnabled

isFlagEnabled(id: HiTraceId, flag: HiTraceFlag): boolean

判断HiTraceId是否启用了跟踪标志flag，同步接口。

**系统能力**：SystemCapability.HiviewDFX.HiTrace

**参数：**

参数名类型必填说明id[HiTraceId](#ZH-CN_TOPIC_0000002529285651__hitraceid)是需要判断指定跟踪标志是否启用的HiTraceId实例。flag[HiTraceFlag](#ZH-CN_TOPIC_0000002529285651__hitraceflag)是指定的跟踪标志。

**返回值：**

类型说明booleantrue：HiTraceId已启用flag；false：HiTraceId未启用flag。

**示例：**

```ets
// 开始跟踪，跟踪标志是INCLUDE_ASYNC。
let traceId = hiTraceChain.begin("business", hiTraceChain.HiTraceFlag.INCLUDE_ASYNC);
// enabledIncludeAsyncFlag为true。
let enabledIncludeAsyncFlag = hiTraceChain.isFlagEnabled(traceId, hiTraceChain.HiTraceFlag.INCLUDE_ASYNC);
if (enabledIncludeAsyncFlag) {
// 基于INCLUDE_ASYNC跟踪标志已设置场景的处理逻辑。
}
//业务结束，结束跟踪。
hiTraceChain.end(traceId);
```

#### hiTraceChain.enableFlag

enableFlag(id: HiTraceId, flag: HiTraceFlag): void

启用HiTraceId中指定的跟踪标志，同步接口。

**系统能力**：SystemCapability.HiviewDFX.HiTrace

**参数：**

参数名类型必填说明id[HiTraceId](#ZH-CN_TOPIC_0000002529285651__hitraceid)是需要启用指定跟踪标志的HiTraceId实例。flag[HiTraceFlag](#ZH-CN_TOPIC_0000002529285651__hitraceflag)是指定的跟踪标志。

**示例：**

```ets
// 开始跟踪，跟踪标志是INCLUDE_ASYNC。
let traceId = hiTraceChain.begin("business", hiTraceChain.HiTraceFlag.INCLUDE_ASYNC);
// enabledDoNotCreateSpanFlag为false。
let enabledDoNotCreateSpanFlag = hiTraceChain.isFlagEnabled(traceId, hiTraceChain.HiTraceFlag.DONOT_CREATE_SPAN);
// 设置DONOT_CREATE_SPAN跟踪标志。
hiTraceChain.enableFlag(traceId, hiTraceChain.HiTraceFlag.DONOT_CREATE_SPAN);
// enabledDoNotCreateSpanFlag为true。
enabledDoNotCreateSpanFlag = hiTraceChain.isFlagEnabled(traceId, hiTraceChain.HiTraceFlag.DONOT_CREATE_SPAN);
if (enabledDoNotCreateSpanFlag) {
// 基于DONOT_CREATE_SPAN跟踪标志已设置场景的处理逻辑。
}
//业务结束，结束跟踪。
hiTraceChain.end(traceId);
```