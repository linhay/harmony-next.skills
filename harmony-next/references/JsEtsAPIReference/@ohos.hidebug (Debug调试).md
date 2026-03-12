# @ohos.hidebug (Debug调试)

为应用提供多种调试、调优的方法。包括但不限于内存、CPU、GPU、GC等相关数据的获取，进程trace、profiler采集，VM堆快照转储等。由于该模块的接口大多比较耗费性能，接口调用较为耗时，且基于HiDebug模块定义，该模块内的接口仅建议在应用调试、调优阶段使用。若需要在其他场景使用时，请认真评估所需调用的接口对应用性能的影响。

本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { hidebug } from '@kit.PerformanceAnalysisKit';
```

#### hidebug.getNativeHeapSize

getNativeHeapSize(): bigint

获取内存分配器统计的进程持有的普通块所占用的总字节数。

**系统能力**：SystemCapability.HiviewDFX.HiProfiler.HiDebug

**返回值**：

类型说明bigint内存分配器统计的进程持有的普通块所占用内存的大小（含分配器元数据），单位为Byte。

**示例**：

```ets
import { hidebug } from '@kit.PerformanceAnalysisKit';

let nativeHeapSize: bigint = hidebug.getNativeHeapSize();
```

#### hidebug.getNativeHeapAllocatedSize

getNativeHeapAllocatedSize(): bigint

获取内存分配器统计的进程持有的已使用的普通块所占用的总字节数。

**系统能力**：SystemCapability.HiviewDFX.HiProfiler.HiDebug

**返回值**：

类型说明bigint返回内存分配器统计的进程持有的已使用的普通块所占用内存大小，单位为Byte。

**示例**：

```ets
import { hidebug } from '@kit.PerformanceAnalysisKit';

let nativeHeapAllocatedSize: bigint = hidebug.getNativeHeapAllocatedSize();
```

#### hidebug.getNativeHeapFreeSize

getNativeHeapFreeSize(): bigint

获取内存分配器统计的进程持有的空闲的普通块所占用的总字节数。

**系统能力**：SystemCapability.HiviewDFX.HiProfiler.HiDebug

**返回值**：

类型说明bigint返回内存分配器统计的进程持有的空闲的普通块所占用内存大小，单位为Byte。

**示例**：

```ets
import { hidebug } from '@kit.PerformanceAnalysisKit';

let nativeHeapFreeSize: bigint = hidebug.getNativeHeapFreeSize();
```

#### hidebug.getPss

getPss(): bigint

获取应用进程实际使用的物理内存大小。接口实现方式：读取/proc/{pid}/smaps_rollup节点中的Pss与SwapPss值并求和。

由于/proc/{pid}/smaps_rollup的读取耗时较长，建议不要在主线程中使用该接口，可通过[@ohos.taskpool](@ohos.taskpool（启动任务池）.md)或[@ohos.worker](@ohos.worker (启动一个Worker).md)开启异步线程以避免应用出现卡顿。

**系统能力**：SystemCapability.HiviewDFX.HiProfiler.HiDebug

**返回值**：

类型说明bigint返回应用进程实际使用的物理内存大小，单位为KB。

**示例**：

```ets
import { hidebug } from '@kit.PerformanceAnalysisKit';

let pss: bigint = hidebug.getPss();
```

#### hidebug.getVss11+

getVss(): bigint

获取应用进程占用的虚拟内存大小。接口实现方式：读取/proc/{pid}/statm节点中的size值（内存页数），vss = size * 页大小（4KB/页）。

**系统能力**：SystemCapability.HiviewDFX.HiProfiler.HiDebug

**返回值**：

类型说明bigint返回应用进程占用的虚拟内存大小，单位为KB。

**示例**：

```ets
import { hidebug } from '@kit.PerformanceAnalysisKit';

let vss: bigint = hidebug.getVss();
```

#### hidebug.getSharedDirty

getSharedDirty(): bigint

获取进程的共享脏内存大小。接口实现方式：读取/proc/{pid}/smaps_rollup节点中的Shared_Dirty值。

由于/proc/{pid}/smaps_rollup的读取耗时较长，建议不要在主线程中使用该接口，可通过[@ohos.taskpool](@ohos.taskpool（启动任务池）.md)或[@ohos.worker](@ohos.worker (启动一个Worker).md)开启异步线程以避免应用出现卡顿。

**系统能力**：SystemCapability.HiviewDFX.HiProfiler.HiDebug

**返回值**：

类型说明bigint返回进程的共享脏内存大小，单位为KB。

**示例**：

```ets
import { hidebug } from '@kit.PerformanceAnalysisKit';

let sharedDirty: bigint = hidebug.getSharedDirty();
```

#### hidebug.getPrivateDirty9+

getPrivateDirty(): bigint

获取进程的私有脏内存大小。读取/proc/{pid}/smaps_rollup中的Private_Dirty值。

由于/proc/{pid}/smaps_rollup的读取耗时较长，建议不要在主线程中使用该接口，可通过[@ohos.taskpool](@ohos.taskpool（启动任务池）.md)或[@ohos.worker](@ohos.worker (启动一个Worker).md)开启异步线程以避免应用出现卡顿。

**系统能力**：SystemCapability.HiviewDFX.HiProfiler.HiDebug

**返回值**：

类型说明bigint返回进程的私有脏内存大小，单位为KB。

**示例**：

```ets
import { hidebug } from '@kit.PerformanceAnalysisKit';

let privateDirty: bigint = hidebug.getPrivateDirty();
```

#### hidebug.getCpuUsage9+

getCpuUsage(): number

获取进程的CPU使用率。

由于该接口涉及跨进程通信，耗时较长，为了避免引入性能问题，建议不要在主线程中直接调用该接口。

**系统能力**：SystemCapability.HiviewDFX.HiProfiler.HiDebug

**返回值**：

类型说明number获取进程的CPU使用率。如占用率为50%，则返回0.5。

**示例**：

```ets
import { hidebug } from '@kit.PerformanceAnalysisKit';

let cpuUsage: number = hidebug.getCpuUsage();
```

#### hidebug.getServiceDump9+

getServiceDump(serviceid: number, fd: number, args: Array<string>): void

获取系统服务信息。

**需要权限**：ohos.permission.DUMP，仅系统应用可申请。

**系统能力**：SystemCapability.HiviewDFX.HiProfiler.HiDebug

**参数**：

参数名类型必填说明serviceidnumber是基于用户输入的service id获取系统服务信息。fdnumber是文件描述符，接口会向该fd写入数据。argsArray<string>是系统服务的dump接口参数列表。string长度的最大值为254。

**错误码**：

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)与[HiDebug错误码](HiDebug错误码.md)。

错误码ID错误信息401the parameter check failed,Possible causes:1.the parameter type error 2.the args parameter is not string array.11400101ServiceId invalid. The system ability does not exist.

**示例**：

```ets
import { fileIo } from '@kit.CoreFileKit';
import { hidebug } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

let fileFd = -1;
try {
  // 请在组件内获取context，确保this.getUiContext().getHostContext()返回结果为UIAbilityContext。
  let path: string = this.getUIContext().getHostContext()!.filesDir + "/serviceInfo.txt";
  console.info("output path: " + path);
  fileFd = fileIo.openSync(path, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE).fd;
  let serviceId: number = 10;
  let args: Array<string> = new Array("allInfo");
  hidebug.getServiceDump(serviceId, fileFd, args);
} catch (error) {
  console.error(`error code: ${(error as BusinessError).code}, error msg: ${(error as BusinessError).message}`);
}

if (fileFd >= 0) {
  fileIo.closeSync(fileFd);
}
```

#### hidebug.startJsCpuProfiling9+

startJsCpuProfiling(filename: string): void

启动虚拟机Profiling方法跟踪，startJsCpuProfiling(filename: string)方法的调用需要与stopJsCpuProfiling()方法的调用一一对应，先开启后关闭，请避免重复开启或重复关闭的调用方式，否则会接口调用异常。

**系统能力**：SystemCapability.HiviewDFX.HiProfiler.HiDebug

**参数**：

参数名类型必填说明filenamestring是用户自定义的采样结果输出的文件名，将在应用的files目录下生成以该参数命名的json文件。string长度的最大值为128。

**错误码**：

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401the parameter check failed,Parameter type error.

**示例**：

```ets
import { hidebug } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  hidebug.startJsCpuProfiling("cpu_profiling");
  // ...
  hidebug.stopJsCpuProfiling();
} catch (error) {
  console.error(`error code: ${(error as BusinessError).code}, error msg: ${(error as BusinessError).message}`);
}
```

#### hidebug.stopJsCpuProfiling9+

stopJsCpuProfiling(): void

停止虚拟机Profiling方法跟踪，stopJsCpuProfiling()方法的调用需要与startJsCpuProfiling(filename: string)方法的调用一一对应，先开启后关闭，请避免重复开启或重复关闭的调用方式，否则会接口调用异常。

**系统能力**：SystemCapability.HiviewDFX.HiProfiler.HiDebug

**示例**：

```ets
import { hidebug } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  hidebug.startJsCpuProfiling("cpu_profiling");
  // ...
  hidebug.stopJsCpuProfiling();
} catch (error) {
  console.error(`error code: ${(error as BusinessError).code}, error msg: ${(error as BusinessError).message}`);
}
```

#### hidebug.dumpJsHeapData9+

dumpJsHeapData(filename: string): void

虚拟机堆数据转储。

由于虚拟机堆导出极其耗时，且该接口为同步接口，建议不要在上架版本中调用该接口，以避免应用冻屏，影响用户体验。

**系统能力**：SystemCapability.HiviewDFX.HiProfiler.HiDebug

**参数**：

参数名类型必填说明filenamestring是用户自定义的虚拟机堆数据转储输出的文件名，将在应用的files目录下生成以该参数命名的heapsnapshot文件。string长度的最大值为128。

**错误码**：

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401the parameter check failed, Parameter type error.

**示例**：

```ets
import { hidebug } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  hidebug.dumpJsHeapData("heapData");
} catch (error) {
  console.error(`error code: ${(error as BusinessError).code}, error msg: ${(error as BusinessError).message}`);
}
```

#### hidebug.startProfiling(deprecated)

startProfiling(filename: string): void

从 API Version 9 开始废弃，建议使用[hidebug.startJsCpuProfiling](#ZH-CN_TOPIC_0000002497605658__hidebugstartjscpuprofiling9)替代。

启动虚拟机Profiling方法跟踪，startProfiling(filename: string)方法的调用需要与stopProfiling()方法的调用一一对应，先开启后关闭，请避免重复开启或重复关闭的调用方式，否则会接口调用异常。

**系统能力**：SystemCapability.HiviewDFX.HiProfiler.HiDebug

**参数**：

参数名类型必填说明filenamestring是用户自定义的采样结果输出的文件名，将在应用的files目录下生成以该参数命名的json文件。string长度的最大值为128。

**示例**：

```ets
import { hidebug } from '@kit.PerformanceAnalysisKit';

hidebug.startProfiling("cpuprofiler-20220216");
// code block
// ...
// code block
hidebug.stopProfiling();
```

#### hidebug.stopProfiling(deprecated)

stopProfiling(): void

从 API Version 9 开始废弃，建议使用[hidebug.stopJsCpuProfiling](#ZH-CN_TOPIC_0000002497605658__hidebugstopjscpuprofiling9)替代。

停止虚拟机Profiling方法跟踪，stopProfiling()方法的调用需要与startProfiling(filename: string)方法的调用一一对应，先开启后关闭，请避免重复开启或重复关闭的调用方式，否则会接口调用异常。

**系统能力**：SystemCapability.HiviewDFX.HiProfiler.HiDebug

**示例**：

```ets
import { hidebug } from '@kit.PerformanceAnalysisKit';

hidebug.startProfiling("cpuprofiler-20220216");
// code block
// ...
// code block
hidebug.stopProfiling();
```

#### hidebug.dumpHeapData(deprecated)

dumpHeapData(filename: string): void

从 API Version 9 开始废弃，建议使用[hidebug.dumpJsHeapData](#ZH-CN_TOPIC_0000002497605658__hidebugdumpjsheapdata9)替代。

虚拟机堆数据转储，生成filename.heapsnapshot文件。

**系统能力**：SystemCapability.HiviewDFX.HiProfiler.HiDebug

**参数**：

参数名类型必填说明filenamestring是用户自定义的虚拟机堆转储文件名，将在应用的files目录下生成以该参数命名的heapsnapshot文件。string长度的最大值为128。

**示例**：

```ets
import { hidebug } from '@kit.PerformanceAnalysisKit';

hidebug.dumpHeapData("heap-20220216");
```

#### hidebug.getAppVMMemoryInfo12+

getAppVMMemoryInfo(): VMMemoryInfo

获取VM内存相关信息。

**系统能力**：SystemCapability.HiviewDFX.HiProfiler.HiDebug

**返回值**：

类型说明[VMMemoryInfo](#ZH-CN_TOPIC_0000002497605658__vmmemoryinfo12)返回VM内存信息。

**示例**：

```ets
import { hidebug } from '@kit.PerformanceAnalysisKit';

let vmMemory: hidebug.VMMemoryInfo = hidebug.getAppVMMemoryInfo();
console.info(`totalHeap = ${vmMemory.totalHeap}, heapUsed = ${vmMemory.heapUsed},` +
  `allArraySize = ${vmMemory.allArraySize}` );
```

#### hidebug.getAppVMObjectUsedSize21+

getAppVMObjectUsedSize(): bigint

获取当前虚拟机中ArkTS对象所占用的内存大小。

**系统能力**：SystemCapability.HiviewDFX.HiProfiler.HiDebug

**返回值**：

类型说明bigint当前虚拟机中ArkTS对象所占用的内存大小，单位为KB。

**示例**：

```ets
import { hidebug } from '@kit.PerformanceAnalysisKit';

console.info(`getAppVMObjectUsedSize = ${hidebug.getAppVMObjectUsedSize()}`);
```

#### hidebug.getAppThreadCpuUsage12+

getAppThreadCpuUsage(): ThreadCpuUsage[]

获取应用线程CPU使用情况。

由于该接口涉及跨进程通信，耗时较长，为了避免引入性能问题，建议不要在主线程中直接调用该接口。

**系统能力**：SystemCapability.HiviewDFX.HiProfiler.HiDebug

**返回值**：

类型说明[ThreadCpuUsage](#ZH-CN_TOPIC_0000002497605658__threadcpuusage12)[]返回当前应用进程下所有ThreadCpuUsage数组。

**示例**：

```ets
import { hidebug } from '@kit.PerformanceAnalysisKit';

let appThreadCpuUsage: hidebug.ThreadCpuUsage[] = hidebug.getAppThreadCpuUsage();
for (let i = 0; i < appThreadCpuUsage.length; i++) {
  console.info(`threadId=${appThreadCpuUsage[i].threadId}, cpuUsage=${appThreadCpuUsage[i].cpuUsage}`);
}
```

#### hidebug.startAppTraceCapture12+

startAppTraceCapture(tags: number[], flag: TraceFlag, limitSize: number): string

该接口补充了[hitrace](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hitrace)功能，开发者可通过该接口完成指定范围的trace自动化采集。由于该接口中trace采集过程中消耗的性能与需要采集的范围成正相关，建议开发者在使用该接口前，通过hitrace命令抓取应用的trace日志，从中筛选出所需trace采集的关键范围，以提高该接口性能。

startAppTraceCapture()方法的调用需要与'[stopAppTraceCapture()](#ZH-CN_TOPIC_0000002497605658__hidebugstopapptracecapture12)'方法的调用一一对应，重复开启trace采集将导致接口调用异常，由于trace采集过程中会消耗较多性能，开发者应在完成采集后及时关闭。

应用调用startAppTraceCapture接口启动采集trace，当采集的trace大小超过了limitSize，系统将自动调用stopAppTraceCapture接口停止采集。因此limitSize大小设置不当，将导致生成trace数据不足，无法满足故障分析。所以要求开发者根据实际情况，评估limitSize大小。

评估方法：limitSize = 预期trace采集时长 * trace单位流量。

预期trace采集时长：开发者根据分析的故障场景自行决定，单位秒。

trace单位流量：应用每秒产生的trace大小，系统推荐值为300KB/s，建议开发者采用自身应用的实测值，单位KB/s。

trace单位流量实测方法：limitSize设置为最大值500M，调用startAppTraceCapture接口，在应用上操作N秒后，调用stopAppTraceCapture停止采集，然后查看trace大小S（Kb）。那么trace单位流量 = S/N（Kb/s）。

**系统能力**：SystemCapability.HiviewDFX.HiProfiler.HiDebug

**参数**：

参数名类型必填说明tagsnumber[]是trace范围，详情请见[tags](#ZH-CN_TOPIC_0000002497605658__hidebugtags12)。flagTraceFlag是详情请见[TraceFlag](#ZH-CN_TOPIC_0000002497605658__traceflag12)。limitSizenumber是开启trace文件大小限制，单位为Byte，单个文件大小上限为500MB。

**返回值**：

类型说明string返回trace文件名路径（接口返回真实物理路径，若应用内需要访问，请参考[应用沙箱路径和真实物理路径的对应关系](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-sandbox-directory#应用沙箱路径和真实物理路径的对应关系)进行路径转换）。

**错误码**：

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)与[HiDebug-Trace错误码](HiDebug Trace错误码.md)。

错误码ID错误信息401Invalid argument, Possible causes:1.The limit parameter is too small 2.The parameter is not within the enumeration type 3.The parameter type error or parameter order error.11400102Capture trace already enabled.11400103No write permission on the file.11400104Abnormal trace status.

**示例**：

```ets
import { hidebug } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tags: number[] = [hidebug.tags.ABILITY_MANAGER, hidebug.tags.ARKUI];
let flag: hidebug.TraceFlag = hidebug.TraceFlag.MAIN_THREAD;
let limitSize: number = 1024 * 1024;

try {
  let fileName: string = hidebug.startAppTraceCapture(tags, flag, limitSize);
  // code block
  // ...
  // code block
  hidebug.stopAppTraceCapture();
} catch (error) {
  console.error(`error code: ${(error as BusinessError).code}, error msg: ${(error as BusinessError).message}`);
}
```

#### hidebug.stopAppTraceCapture12+

stopAppTraceCapture(): void

停止应用trace采集。调用前，需先调用'[startAppTraceCapture()](#ZH-CN_TOPIC_0000002497605658__hidebugstartapptracecapture12)'方法开始采集。关闭前未开启或重复关闭会导致接口异常。

调用startAppTraceCapture接口，如果没有合理传入limitSize参数，生成trace的大小大于传入的limitSize大小，系统内部会自动调用stopAppTraceCapture，再次手动调用stopAppTraceCapture就会抛出错误码11400105。

**系统能力**：SystemCapability.HiviewDFX.HiProfiler.HiDebug

**错误码**：

以下错误码的详细介绍请参见[HiDebug-Trace错误码](HiDebug Trace错误码.md)。

错误码ID错误信息11400104The status of the trace is abnormal.11400105No capture trace running.

**示例**：

```ets
import { hidebug } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tags: number[] = [hidebug.tags.ABILITY_MANAGER, hidebug.tags.ARKUI];
let flag: hidebug.TraceFlag = hidebug.TraceFlag.MAIN_THREAD;
let limitSize: number = 1024 * 1024;
try {
  let fileName: string = hidebug.startAppTraceCapture(tags, flag, limitSize);
  // code block
  // ...
  // code block
  hidebug.stopAppTraceCapture();
} catch (error) {
  console.error(`error code: ${(error as BusinessError).code}, error msg: ${(error as BusinessError).message}`);
}
```

#### hidebug.getAppMemoryLimit12+

getAppMemoryLimit(): MemoryLimit

获取应用程序进程的内存限制。

**系统能力**：SystemCapability.HiviewDFX.HiProfiler.HiDebug

**返回值**：

类型说明[MemoryLimit](#ZH-CN_TOPIC_0000002497605658__memorylimit12)应用程序进程内存限制。

**示例**：

```ets
import { hidebug } from '@kit.PerformanceAnalysisKit';

let appMemoryLimit:hidebug.MemoryLimit = hidebug.getAppMemoryLimit();
```

#### hidebug.getSystemCpuUsage12+

getSystemCpuUsage(): number

获取系统的CPU资源占用情况。

由于该接口涉及跨进程通信，耗时较长，为了避免引入性能问题，建议不要在主线程中直接调用该接口。

**系统能力**：SystemCapability.HiviewDFX.HiProfiler.HiDebug

**返回值**：

类型说明number系统CPU资源占用情况。如占用率为50%，则返回0.5。

**错误码**：

以下错误码的详细介绍请参见[HiDebug-CpuUsage错误码](HiDebug CpuUsage错误码.md)。

错误码ID错误信息11400104The status of the system CPU usage is abnormal.

**示例**：

```ets
import { hidebug } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  console.info(`getSystemCpuUsage: ${hidebug.getSystemCpuUsage()}`)
} catch (error) {
  console.error(`error code: ${(error as BusinessError).code}, error msg: ${(error as BusinessError).message}`);
}
```

#### hidebug.setAppResourceLimit12+

setAppResourceLimit(type: string, value: number, enableDebugLog: boolean): void

设置应用的文件描述符数量、线程数量、JS内存或Native内存资源限制。

主要应用场景在于构造内存泄漏故障，参见[订阅资源泄漏事件（ArkTS）](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-resourceleak-events-arkts)、[订阅资源泄漏事件（C/C++）](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-resourceleak-events-ndk)。

当设置的开发者选项开关打开并重启设备后，此功能有效。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.HiviewDFX.HiProfiler.HiDebug

**参数**：

参数名类型必填说明typestring是

泄漏资源类型，共四种：

- pss_memory（native内存）

- js_heap（js堆内存）

- fd（文件描述符）

- thread（线程）

valuenumber是

对应泄漏资源类型的最大值，范围：

- pss_memory类型：[1024, 4 * 1024 * 1024]（单位：KB）

- js_heap类型：[85, 95]（分配给JS堆内存上限的85%~95%）

- fd类型：[10, 10000]

- thread类型：[1, 1000]

enableDebugLogboolean是

是否启用外部调试日志。外部调试日志请仅在灰度版本（正式版本发布之前，先向一小部分用户推出的测试版本）中启用，因为收集调试日志会占用大量的cpu资源和内存资源，可能会引起应用流畅性问题。

true：启用外部调试日志。

false：禁用外部调试日志。

**错误码**：

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)与[HiDebug错误码](HiDebug错误码.md)。

错误码ID错误信息401Invalid argument, Possible causes:1.The limit parameter is too small 2.The parameter is not in the specified type 3.The parameter type error or parameter order error.11400104Set limit failed due to remote exception.

**示例**：

```ets
import { hidebug } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

let type: string = 'js_heap';
let value: number = 85;
let enableDebugLog: boolean = false;
try {
  hidebug.setAppResourceLimit(type, value, enableDebugLog);
} catch (error) {
  console.error(`error code: ${(error as BusinessError).code}, error msg: ${(error as BusinessError).message}`);
}
```

#### hidebug.getAppNativeMemInfo12+

getAppNativeMemInfo(): NativeMemInfo

获取应用进程内存信息。读取/proc/{pid}/smaps_rollup和/proc/{pid}/statm节点的数据。

**系统能力**：SystemCapability.HiviewDFX.HiProfiler.HiDebug

由于读取/proc/{pid}/smaps_rollup耗时较长，推荐使用异步接口[hidebug.getAppNativeMemInfoAsync](#ZH-CN_TOPIC_0000002497605658__hidebuggetappnativememinfoasync20)，以避免应用丢帧或卡顿。

**返回值**：

类型说明[NativeMemInfo](#ZH-CN_TOPIC_0000002497605658__nativememinfo12)应用进程内存信息。

**示例**：

```ets
import { hidebug } from '@kit.PerformanceAnalysisKit';

let nativeMemInfo: hidebug.NativeMemInfo = hidebug.getAppNativeMemInfo();
console.info(`pss: ${nativeMemInfo.pss}, vss: ${nativeMemInfo.vss}, rss: ${nativeMemInfo.rss}, ` +
  `sharedDirty: ${nativeMemInfo.sharedDirty}, privateDirty: ${nativeMemInfo.privateDirty}, ` +
  `sharedClean: ${nativeMemInfo.sharedClean}, privateClean: ${nativeMemInfo.privateClean}`);
```

#### hidebug.getAppNativeMemInfoAsync20+

getAppNativeMemInfoAsync(): Promise<NativeMemInfo>

读取/proc/{pid}/smaps_rollup和/proc/{pid}/statm节点的数据以获取应用进程内存信息，使用Promise异步回调。

**系统能力**：SystemCapability.HiviewDFX.HiProfiler.HiDebug

**返回值**：

类型说明Promise<[NativeMemInfo](#ZH-CN_TOPIC_0000002497605658__nativememinfo12)>promise对象，返回应用进程内存信息。

**示例**：

```ets
hidebug.getAppNativeMemInfoAsync().then((nativeMemInfo: hidebug.NativeMemInfo)=>{
  console.info(`pss: ${nativeMemInfo.pss}, vss: ${nativeMemInfo.vss}, rss: ${nativeMemInfo.rss}, ` +
    `sharedDirty: ${nativeMemInfo.sharedDirty}, privateDirty: ${nativeMemInfo.privateDirty}, ` +
    `sharedClean: ${nativeMemInfo.sharedClean}, privateClean: ${nativeMemInfo.privateClean}`);
});
```

#### hidebug.getAppNativeMemInfoWithCache20+

getAppNativeMemInfoWithCache(forceRefresh?: boolean): NativeMemInfo

获取应用进程内存信息。与getAppNativeMemInfo接口相比，该接口使用了缓存机制，以提高性能。缓存的有效期为5分钟。

由于读取 /proc/{pid}/smaps_rollup 比较耗时，建议不在主线程中使用该接口。可以通过 @ohos.taskpool 或 @ohos.worker 开启异步线程，以避免应用卡顿。

**系统能力**：SystemCapability.HiviewDFX.HiProfiler.HiDebug

**参数**：

参数名类型必填说明forceRefreshboolean否

是否需要无视缓存有效性，强制更新缓存值。默认值：false。

true：直接获取当前内存数据并更新缓存值。

false：缓存有效时，直接返回缓存值，缓存失效时获取当前内存数据并更新缓存值。

**返回值**：

类型说明[NativeMemInfo](#ZH-CN_TOPIC_0000002497605658__nativememinfo12)应用进程内存信息。

**示例**：

```ets
let nativeMemInfo: hidebug.NativeMemInfo = hidebug.getAppNativeMemInfoWithCache();
console.info(`pss: ${nativeMemInfo.pss}, vss: ${nativeMemInfo.vss}, rss: ${nativeMemInfo.rss}, ` +
  `sharedDirty: ${nativeMemInfo.sharedDirty}, privateDirty: ${nativeMemInfo.privateDirty}, ` +
  `sharedClean: ${nativeMemInfo.sharedClean}, privateClean: ${nativeMemInfo.privateClean}`);
```

#### hidebug.getSystemMemInfo12+

getSystemMemInfo(): SystemMemInfo

获取系统内存信息。读取/proc/meminfo节点的数据。

**系统能力**：SystemCapability.HiviewDFX.HiProfiler.HiDebug

**返回值**：

类型说明[SystemMemInfo](#ZH-CN_TOPIC_0000002497605658__systemmeminfo12)系统内存信息。

**示例**：

```ets
import { hidebug } from '@kit.PerformanceAnalysisKit';

let systemMemInfo: hidebug.SystemMemInfo = hidebug.getSystemMemInfo();

console.info(`totalMem: ${systemMemInfo.totalMem}, freeMem: ${systemMemInfo.freeMem}, ` +
  `availableMem: ${systemMemInfo.availableMem}`);
```

#### hidebug.getVMRuntimeStats12+

getVMRuntimeStats(): GcStats

获取系统[GC](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/gc-introduction)统计信息。

**系统能力**：SystemCapability.HiviewDFX.HiProfiler.HiDebug

**返回值**：

类型说明[GcStats](#ZH-CN_TOPIC_0000002497605658__gcstats12)系统GC统计信息。

**示例**：

```ets
import { hidebug } from '@kit.PerformanceAnalysisKit';

let vMRuntimeStats: hidebug.GcStats = hidebug.getVMRuntimeStats();
console.info(`gc-count: ${vMRuntimeStats['ark.gc.gc-count']}`);
console.info(`gc-time: ${vMRuntimeStats['ark.gc.gc-time']}`);
console.info(`gc-bytes-allocated: ${vMRuntimeStats['ark.gc.gc-bytes-allocated']}`);
console.info(`gc-bytes-freed: ${vMRuntimeStats['ark.gc.gc-bytes-freed']}`);
console.info(`fullgc-longtime-count: ${vMRuntimeStats['ark.gc.fullgc-longtime-count']}`);
```

#### hidebug.getVMRuntimeStat12+

getVMRuntimeStat(item: string): number

根据参数获取指定的系统[GC](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/gc-introduction)统计信息。

**系统能力**：SystemCapability.HiviewDFX.HiProfiler.HiDebug

**参数**：

参数名类型必填说明itemstring是

所需统计信息的类型。可获取的统计信息类型如下：

"ark.gc.gc-count"：当前线程的GC次数。

"ark.gc.gc-time"：当前线程触发的GC总耗时，以ms为单位。

"ark.gc.gc-bytes-allocated"：当前线程Ark虚拟机已分配的内存大小，以B为单位。

"ark.gc.gc-bytes-freed"：当前线程GC成功回收的内存，以B为单位。

"ark.gc.fullgc-longtime-count "：当前线程超长fullGC次数。

**返回值**：

类型说明number系统GC统计信息，根据传入的参数，返回相应的信息。

**错误码**：

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Possible causes:1. Invalid parameter, a string parameter required. 2. Invalid parameter, unknown property.

**示例**：

```ets
import { hidebug } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  console.info(`gc-count: ${hidebug.getVMRuntimeStat('ark.gc.gc-count')}`);
  console.info(`gc-time: ${hidebug.getVMRuntimeStat('ark.gc.gc-time')}`);
  console.info(`gc-bytes-allocated: ${hidebug.getVMRuntimeStat('ark.gc.gc-bytes-allocated')}`);
  console.info(`gc-bytes-freed: ${hidebug.getVMRuntimeStat('ark.gc.gc-bytes-freed')}`);
  console.info(`fullgc-longtime-count: ${hidebug.getVMRuntimeStat('ark.gc.fullgc-longtime-count')}`);
} catch (error) {
  console.error(`error code: ${(error as BusinessError).code}, error msg: ${(error as BusinessError).message}`);
}
```

#### MemoryLimit12+

应用进程内存限制。

**系统能力**：SystemCapability.HiviewDFX.HiProfiler.HiDebug

名称类型只读可选说明rssLimitbigint否否应用进程的驻留集的限制，以KB为单位。vssLimitbigint否否进程的虚拟内存限制，以KB为单位。vmHeapLimitbigint否否当前线程的 JS VM 堆大小限制，以KB为单位。vmTotalHeapSizebigint否否当前进程的 JS 堆内存大小限制，以KB为单位。

#### VMMemoryInfo12+

VM内存信息。

**系统能力**：SystemCapability.HiviewDFX.HiProfiler.HiDebug

名称类型只读可选说明totalHeapbigint否否表示当前虚拟机的堆总大小，以KB为单位。heapUsedbigint否否表示当前虚拟机使用的堆大小，以KB为单位。allArraySizebigint否否表示当前虚拟机的所有数组对象大小，以KB为单位。

#### ThreadCpuUsage12+

线程的CPU使用情况。

**系统能力**：SystemCapability.HiviewDFX.HiProfiler.HiDebug

名称类型只读可选说明threadIdnumber否否线程号。cpuUsagenumber否否线程CPU使用率。

#### hidebug.tags12+

支持trace使用场景的标签，用户可通过[hitrace](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hitrace)抓取指定标签的trace内容。

以下标签实际值由系统定义，可能随版本升级而发生改变，为避免升级后出现兼容性问题，在生产中应直接使用标签名称而非标签数值。

**系统能力**：SystemCapability.HiviewDFX.HiProfiler.HiDebug

名称类型只读说明ABILITY_MANAGERnumber是能力管理标签，hitrace命令行工具对应tagName:ability。ARKUInumber是ArkUI开发框架标签，hitrace命令行工具对应tagName:ace。ARKnumber是JSVM虚拟机标签，hitrace命令行工具对应tagName:ark。BLUETOOTHnumber是蓝牙标签，hitrace命令行工具对应tagName:bluetooth。COMMON_LIBRARYnumber是公共库子系统标签，hitrace命令行工具对应tagName:commonlibrary。DISTRIBUTED_HARDWARE_DEVICE_MANAGERnumber是分布式硬件设备管理标签，hitrace命令行工具对应tagName:devicemanager。DISTRIBUTED_AUDIOnumber是分布式音频标签，hitrace命令行工具对应tagName:daudio。DISTRIBUTED_CAMERAnumber是分布式相机标签，hitrace命令行工具对应tagName:dcamera。DISTRIBUTED_DATAnumber是分布式数据管理模块标签，hitrace命令行工具对应tagName:distributeddatamgr。DISTRIBUTED_HARDWARE_FRAMEWORKnumber是分布式硬件框架标签，hitrace命令行工具对应tagName:dhfwk。DISTRIBUTED_INPUTnumber是分布式输入标签，hitrace命令行工具对应tagName:dinput。DISTRIBUTED_SCREENnumber是分布式屏幕标签，hitrace命令行工具对应tagName:dscreen。DISTRIBUTED_SCHEDULERnumber是分布式调度器标签，hitrace命令行工具对应tagName:dsched。FFRTnumber是FFRT任务标签，hitrace命令行工具对应tagName:ffrt。FILE_MANAGEMENTnumber是文件管理系统标签，hitrace命令行工具对应tagName:filemanagement。GLOBAL_RESOURCE_MANAGERnumber是全局资源管理标签，hitrace命令行工具对应tagName:gresource。GRAPHICSnumber是图形模块标签，hitrace命令行工具对应tagName:graphic。HDFnumber是HDF子系统标签，hitrace命令行工具对应tagName:hdf。MISCnumber是MISC模块标签，hitrace命令行工具对应tagName:misc。MULTIMODAL_INPUTnumber是多模态输入模块标签，hitrace命令行工具对应tagName:multimodalinput。NETnumber是网络标签，hitrace命令行工具对应tagName:net。NOTIFICATIONnumber是通知模块标签，hitrace命令行工具对应tagName:notification。NWEBnumber是Nweb标签，hitrace命令行工具对应tagName:nweb。OHOSnumber是OHOS通用标签，hitrace命令行工具对应tagName:ohos。POWER_MANAGERnumber是电源管理标签，hitrace命令行工具对应tagName:power。RPCnumber是RPC标签，hitrace命令行工具对应tagName:rpc。SAMGRnumber是系统能力管理标签，hitrace命令行工具对应tagName:samgr。WINDOW_MANAGERnumber是窗口管理标签，hitrace命令行工具对应tagName:window。AUDIOnumber是音频模块标签，hitrace命令行工具对应tagName:zaudio。CAMERAnumber是相机模块标签，hitrace命令行工具对应tagName:zcamera。IMAGEnumber是图片模块标签，hitrace命令行工具对应tagName:zimage。MEDIAnumber是媒体模块标签，hitrace命令行工具对应tagName:zmedia。

#### NativeMemInfo12+

描述应用进程的内存信息。

**系统能力**：SystemCapability.HiviewDFX.HiProfiler.HiDebug

名称类型只读可选说明pssbigint否否实际占用的物理内存大小(比例分配共享库占用的内存)，以KB为单位，计算方式：/proc/{pid}/smaps_rollup: Pss + SwapPss。vssbigint否否占用的虚拟内存大小(包括共享库所占用的内存)，以KB为单位，计算方式：/proc/{pid}/statm: size * 4。rssbigint否否实际占用的物理内存大小(包括共享库占用)，以KB为单位，计算方式：/proc/{pid}/smaps_rollup: Rss。sharedDirtybigint否否共享脏内存大小，以KB为单位，计算方式：/proc/{pid}/smaps_rollup: Shared_Dirty。privateDirtybigint否否私有脏内存大小，以KB为单位，计算方式：/proc/{pid}/smaps_rollup: Private_Dirty。sharedCleanbigint否否共享净内存大小，以KB为单位，计算方式：/proc/{pid}/smaps_rollup: Shared_Clean。privateCleanbigint否否私有干净内存大小，以KB为单位，计算方式：/proc/{pid}/smaps_rollup: Private_Clean。

#### SystemMemInfo12+

描述系统内存信息，包括总内存、空闲内存和可用内存。

**系统能力**：SystemCapability.HiviewDFX.HiProfiler.HiDebug

名称类型只读可选说明totalMembigint否否系统总的内存，以KB为单位，计算方式：/proc/meminfo: MemTotalfreeMembigint否否系统空闲的内存，以KB为单位，计算方式：/proc/meminfo: MemFreeavailableMembigint否否系统可用的内存，以KB为单位，计算方式：/proc/meminfo: MemAvailable

#### TraceFlag12+

描述采集trace线程的类型，包括主线程和所有线程。

**系统能力**：SystemCapability.HiviewDFX.HiProfiler.HiDebug

名称值说明MAIN_THREAD1只采集当前应用主线程。ALL_THREADS2采集当前应用下所有线程。

#### GcStats12+

type GcStats = Record<string, number>

描述用于存储GC统计信息的键值对。该类型不支持多线程操作，如果应用中存在多线程同时访问，需加锁保护。

**系统能力**：SystemCapability.HiviewDFX.HiProfiler.HiDebug

类型说明Record<string, number>

用于存储GC统计信息的键值对。包含以下键值信息：

"ark.gc.gc-count"：当前线程的GC次数。

"ark.gc.gc-time"：当前线程触发的GC总耗时，以ms为单位。

"ark.gc.gc-bytes-allocated"：当前线程Ark虚拟机已分配的内存大小，以B为单位。

"ark.gc.gc-bytes-freed"：当前线程GC成功回收的内存，以B为单位。

"ark.gc.fullgc-longtime-count "：当前线程超长fullGC次数。

#### JsRawHeapTrimLevel20+

转储堆快照的裁剪级别的枚举。

TRIM_LEVEL_2相比TRIM_LEVEL_1，裁剪时间更长。冻屏的阈值为6秒。使用TRIM_LEVEL_1时，不会达到该阈值；切换至TRIM_LEVEL_2时，裁剪时间可能会超过6秒，触发APP_FREEZE（冻屏事件），导致应用被系统终止，此时回退至TRIM_LEVEL_1级别进行裁剪。

推荐优先使用TRIM_LEVEL_1确保应用稳定，仅在需要更彻底裁剪时尝试TRIM_LEVEL_2。

**系统能力**：SystemCapability.HiviewDFX.HiProfiler.HiDebug

名称值说明TRIM_LEVEL_10LEVEL 1级别裁剪，主要裁剪字符串。TRIM_LEVEL_21LEVEL 2级别裁剪，在TRIM_LEVEL_1的基础上，精简了对象地址标识的大小，从8个字节减少到4个字节。

#### hidebug.isDebugState12+

isDebugState(): boolean

获取应用进程的调试状态。

**系统能力**：SystemCapability.HiviewDFX.HiProfiler.HiDebug

**返回值**：

类型说明boolean应用进程的Ark层或Native层是否处于调试状态。true：处于调试状态。false：未处于调试状态。

**示例**：

```ets
import { hidebug } from '@kit.PerformanceAnalysisKit';

console.info(`isDebugState = ${hidebug.isDebugState()}`)
```

#### hidebug.getGraphicsMemory14+

getGraphicsMemory(): Promise<number>

获取应用显存总大小（gl + graph），使用Promise异步回调。

**元服务API**：从API version 14开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.HiviewDFX.HiProfiler.HiDebug

**返回值**：

类型说明Promise<number>promise对象，返回应用显存总大小，单位为KB。

**错误码**：

以下错误码的详细介绍请参见[HiDebug错误码](HiDebug错误码.md)。

错误码ID错误信息11400104Failed to get the application memory due to a remote exception.

**示例**：

```ets
import { hidebug, hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

hidebug.getGraphicsMemory().then((ret: number) => {
  console.info(`graphicsMemory: ${ret}`)
}).catch((error: BusinessError) => {
  console.error(`error code: ${error.code}, error msg: ${error.message}`);
})
```

#### hidebug.getGraphicsMemorySync14+

getGraphicsMemorySync(): number

使用同步方式获取应用显存总大小（gl + graph）。

由于该接口涉及多次跨进程通信，其耗时可能达到秒级。为了避免引入性能问题，建议不要在主线程调用该接口，推荐使用异步接口getGraphicsMemory。

**元服务API**：从API version 14开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.HiviewDFX.HiProfiler.HiDebug

**返回值**：

类型说明number应用显存总大小，单位为KB。

**错误码**：

以下错误码的详细介绍请参见[HiDebug错误码](HiDebug错误码.md)。

错误码ID错误信息11400104Failed to get the application memory due to a remote exception.

**示例**：

```ets
import { hidebug } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  console.info(`graphicsMemory: ${hidebug.getGraphicsMemorySync()}`)
} catch (error) {
  console.error(`error code: ${(error as BusinessError).code}, error msg: ${(error as BusinessError).message}`);
}
```

#### hidebug.getGraphicsMemorySummary21+

getGraphicsMemorySummary(interval?: number): Promise<GraphicsMemorySummary>

获取应用显存数据，使用Promise进行异步回调。

**元服务API**：从API version 21开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.HiviewDFX.HiProfiler.HiDebug

**参数**：

参数名类型必填说明intervalnumber否

显存数据缓存值有效时间，单位为秒。默认值：300。取值范围为[2-3600]。若传入值超出取值范围时，将使用默认值。

当显存数据缓存值存在时间超过该值时，获取最新显存数据并更新缓存值；否则，直接获取缓存值。

**返回值**：

类型说明Promise<[GraphicsMemorySummary](#ZH-CN_TOPIC_0000002497605658__graphicsmemorysummary21)>promise对象，返回应用显存数据。

**错误码**：

以下错误码的详细介绍请参见[HiDebug错误码](HiDebug错误码.md)。

错误码ID错误信息11400104Failed to get the application memory due to a remote exception.

**示例**：

```ets
import { hidebug } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

hidebug.getGraphicsMemorySummary().then((ret: hidebug.GraphicsMemorySummary) => {
  console.info(`get graphicsMemory gl: ${ret.gl} graph: ${ret.graph}.`)
}).catch((error: BusinessError) => {
  console.error(`error code: ${error.code}, error msg: ${error.message}.`);
})
```

#### hidebug.dumpJsRawHeapData18+

dumpJsRawHeapData(needGC?: boolean): Promise<string>

为当前线程转储虚拟机的原始堆快照，并生成的rawheap文件，该文件可通过[rawheap-translator工具](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/rawheap-translator)将所生成文件转化为heapsnapshot文件进行解析。生成的文件路径使用Promise进行异步回调。

系统通过该接口转存快照会消耗大量资源，因此严格限制了调用频率和次数。处理完生成的文件后，请立即删除。

建议仅在应用的灰度版本中使用。在正式版本中不推荐使用，避免影响应用流畅性。

**元服务API**：从API version 18开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.HiviewDFX.HiProfiler.HiDebug

**参数**：

参数名类型必填说明needGCboolean否转储堆快照前是否需要GC。true：需要GC。false：不需GC。默认值：true。

**返回值**：

类型说明Promise<string>Promise对象，返回生成的快照文件路径（[应用沙箱内路径](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-sandbox-directory#应用沙箱路径和真实物理路径的对应关系)）。

**错误码**：

以下错误码的详细介绍请参见[HiDebug错误码](HiDebug错误码.md)。

错误码ID错误信息11400106Quota exceeded.11400107Fork operation failed.11400108Failed to wait for the child process to finish.11400109Timeout while waiting for the child process to finish.11400110Disk remaining space too low.11400111Napi interface call exception.11400112Repeated data dump.11400113Failed to create dump file.

**示例**：

```ets
import { hidebug } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';
hidebug.dumpJsRawHeapData().then((filePath: string) => {
  console.info(`dumpJsRawHeapData success and generated file path is ${filePath}`)
}).catch((error: BusinessError) => {
  console.error(`error code: ${error.code}, error msg: ${error.message}`);
})
```

#### hidebug.enableGwpAsanGrayscale20+

enableGwpAsanGrayscale(options?: GwpAsanOptions, duration?: number): void

使能GWP-ASan，用于检测堆内存使用中的非法行为。

该接口主要用于动态配置并启用GWP-ASan，以适配应用自定义的GWP-ASan检测策略。配置在应用重新启动后生效。

更多关于GWP-ASan的说明，请参见[使用GWP-ASan检测内存错误](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-stability-gwpasan-detection)。

1. 若设备运行期间通过本接口设置的GWP-ASan应用数量超过配额限制，调用该接口将会失败并抛出错误码。请使用try-catch捕获异常，以避免应用异常退出。
1. 设备重启后，本接口设置的GWP-ASan参数将会失效。

**系统能力**：SystemCapability.HiviewDFX.HiProfiler.HiDebug

**参数**：

参数名类型必填说明options[GwpAsanOptions](#ZH-CN_TOPIC_0000002497605658__gwpasanoptions20)否GWP-ASan配置项。未设置时，使用默认参数。durationnumber否GWP-ASan持续时间，单位为天，默认值为7。需传入大于0的正整数。

**错误码**：

以下错误码的详细介绍请参见[HiDebug错误码](HiDebug错误码.md)。

错误码ID错误信息11400114The number of GWP-ASAN applications of this device overflowed after last boot.

**示例**：

```ets
import { hidebug } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

let options: hidebug.GwpAsanOptions = {
  alwaysEnabled: true,
  sampleRate: 2500,
  maxSimutaneousAllocations: 5000,
};
let duration: number = 4;

try {
  hidebug.enableGwpAsanGrayscale(options, duration);
  console.info(`Succeeded in enabling GWP-ASan.`);
} catch (error) {
  const err: BusinessError = error as BusinessError;
  console.error(`Failed to enable GWP-ASan. Code: ${err.code}, message: ${err.message}`);
}
```

#### GwpAsanOptions20+

GWP-ASan配置项。可用于配置是否使能、采样频率，以及最大分配的插槽数。

**系统能力**：SystemCapability.HiviewDFX.HiProfiler.HiDebug

名称类型只读可选说明alwaysEnabledboolean否是

true：100%使能GWP-ASan。

false：1/128概率使能GWP-ASan。

默认值：false。

sampleRatenumber否是

GWP-ASan采样频率，默认值为2500，需要传入大于0的正整数，若传入小数则向上取整。

1/sampleRate的概率对分配的内存进行采样。

建议值：>=1000，过小会显著影响性能。

maxSimutaneousAllocationsnumber否是

最大分配的插槽数，默认值为1000，需要传入大于0的正整数，若传入小数则向上取整。

当插槽用尽时，新分配的内存将不再受监控。

释放已使用的内存后，其占用的插槽将自动复用，以便于后续内存的监控。

建议值：<=20000，过大会可能导致VMA超限崩溃。

#### hidebug.disableGwpAsanGrayscale20+

disableGwpAsanGrayscale(): void

停止使能GWP-ASan。调用该接口将取消自定义配置，恢复默认参数[GwpAsanOptions](#ZH-CN_TOPIC_0000002497605658__gwpasanoptions20)。

**系统能力**：SystemCapability.HiviewDFX.HiProfiler.HiDebug

**示例**：

```ets
import { hidebug } from '@kit.PerformanceAnalysisKit';

hidebug.disableGwpAsanGrayscale();
```

#### hidebug.getGwpAsanGrayscaleState20+

getGwpAsanGrayscaleState(): number

获取当前GWP-ASan剩余使能天数。

**系统能力**：SystemCapability.HiviewDFX.HiProfiler.HiDebug

**返回值**：

类型说明number获取当前GWP-ASan剩余使能天数。若当前未使能，返回值0。

**示例**：

```ets
import { hidebug } from '@kit.PerformanceAnalysisKit';

let remainDays: number = hidebug.getGwpAsanGrayscaleState();
console.info(`remainDays: ${remainDays}`);
```

#### hidebug.setJsRawHeapTrimLevel20+

setJsRawHeapTrimLevel(level: JsRawHeapTrimLevel): void

设置当前进程转储虚拟机原始堆快照的裁剪级别。使用该接口并传入参数TRIM_LEVEL_2，可以有效减少堆快照的文件大小。

默认裁剪级别是TRIM_LEVEL_1。如果设置了TRIM_LEVEL_2裁剪，需使用API version 20之后的[rawheap-translator](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/rawheap-translator)工具才能将.rawheap文件转换为.heapsnapshot文件，否则可能导致转换失败。

该接口影响[dumpJsRawHeapData](#ZH-CN_TOPIC_0000002497605658__hidebugdumpjsrawheapdata18)的结果。

**系统能力**：SystemCapability.HiviewDFX.HiProfiler.HiDebug

**参数**：

参数名类型必填说明level[JsRawHeapTrimLevel](#ZH-CN_TOPIC_0000002497605658__jsrawheaptrimlevel20)是转储堆快照的裁剪级别，默认为TRIM_LEVEL_1。

**示例**：

```ets
import { hidebug } from '@kit.PerformanceAnalysisKit';

hidebug.setJsRawHeapTrimLevel(hidebug.JsRawHeapTrimLevel.TRIM_LEVEL_2);
```

#### GraphicsMemorySummary21+

描述应用显存数据，包括gl和graph部分。

**元服务API**：从API version 21开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.HiviewDFX.HiProfiler.HiDebug

名称类型只读可选说明glnumber否否gl显存大小，RenderService渲染进程加载所需资源占用的内存，例如图片、纹理等，以KB为单位。graphnumber否否graph显存大小，进程统计的DMA内存占用，包括直接通过接口申请的DMA buffer和通过allocator_host申请的DMA buffer，以KB为单位。