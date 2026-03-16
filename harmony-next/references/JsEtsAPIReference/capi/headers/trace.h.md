# trace.h

#### 概述

HiTraceMeter和HitraceChain模块接口定义，通过这些接口实现性能打点和分布式跟踪功能。

用户态trace格式使用竖线字符作为分隔符，所以通过HiTraceMeter接口传递的字符串类型参数应避免包含该字符，防止trace解析异常。

用户态trace总长度限制512字符，超过的部分将会被截断。

**引用文件：** <hitrace/trace.h>

**库：** libhitrace_ndk.z.so

**系统能力：** SystemCapability.HiviewDFX.HiTrace

**起始版本：** 10

**相关模块：**[Hitrace](../../topics/input/HiTrace.md)

#### 汇总

#### 结构体

名称typedef关键字描述[HiTraceId](../../topics/input/HiTraceId.md)HiTraceIdHiTraceId定义。

#### 枚举

名称typedef关键字描述[HiTraceId_Valid](#ZH-CN_TOPIC_0000002497605672__hitraceid_valid)HiTraceId_ValidHiTraceId是否有效标志。[HiTrace_Version](#ZH-CN_TOPIC_0000002497605672__hitrace_version)HiTrace_VersionHiTrace版本号。[HiTrace_Flag](#ZH-CN_TOPIC_0000002497605672__hitrace_flag)HiTrace_FlagHiTrace跟踪标志。[HiTrace_Tracepoint_Type](#ZH-CN_TOPIC_0000002497605672__hitrace_tracepoint_type)HiTrace_Tracepoint_Type跟踪埋点类型枚举。[HiTrace_Communication_Mode](#ZH-CN_TOPIC_0000002497605672__hitrace_communication_mode)HiTrace_Communication_Mode跟踪通信类型枚举。[HiTrace_Output_Level](#ZH-CN_TOPIC_0000002497605672__hitrace_output_level)HiTrace_Output_LevelHiTrace输出级别。低于系统跟踪输出级别阈值的打点将不会生效。log版本阈值为HITRACE_LEVEL_INFO；nolog版本阈值为HITRACE_LEVEL_COMMERCIAL。

#### 函数

名称描述[HiTraceId OH_HiTrace_BeginChain(const char *name, int flags)](#ZH-CN_TOPIC_0000002497605672__oh_hitrace_beginchain)

开始跟踪。

 当前线程TLS（Thread Local Storage，线程本地存储）中不存在有效的HiTraceId时，生成有效的HiTraceId并设置到当前线程TLS中，返回该HiTraceId。

 当前线程TLS中已存在有效的HiTraceId时，不会开始新的跟踪，返回各属性值均为0的无效HiTraceId。

[void OH_HiTrace_EndChain()](#ZH-CN_TOPIC_0000002497605672__oh_hitrace_endchain)

结束跟踪。

 结束跟踪并将当前线程TLS中的HiTraceId设置为无效。

[HiTraceId OH_HiTrace_GetId()](#ZH-CN_TOPIC_0000002497605672__oh_hitrace_getid)

获取跟踪标识。

 获取当前线程TLS中的HiTraceId。

[void OH_HiTrace_SetId(const HiTraceId *id)](#ZH-CN_TOPIC_0000002497605672__oh_hitrace_setid)

设置跟踪标识。

 将给定的HiTraceId设置到当前线程TLS中。若给定的HiTraceId无效，则不执行任何操作。

[void OH_HiTrace_ClearId(void)](#ZH-CN_TOPIC_0000002497605672__oh_hitrace_clearid)

清除跟踪标识。

 将当前线程TLS中的HiTraceId设置为无效。

[HiTraceId OH_HiTrace_CreateSpan(void)](#ZH-CN_TOPIC_0000002497605672__oh_hitrace_createspan)

创建跟踪分支。

 创建一个HiTraceId，使用当前线程TLS中的chainId、spanId初始化HiTraceId的chainId、parentSpanId，并为HiTraceId生成一个新的spanId，返回该HiTraceId。

[void OH_HiTrace_Tracepoint(HiTrace_Communication_Mode mode, HiTrace_Tracepoint_Type type, const HiTraceId *id, const char *fmt, ...)](#ZH-CN_TOPIC_0000002497605672__oh_hitrace_tracepoint)

HiTraceMeter跟踪信息埋点。

type为客户端发送CS和服务端接收SC时，进行同步HiTraceMeter开始打点；

type为客户端接收CC和服务端发送SS时，进行同步HiTraceMeter结束打点；

type为通用类型GENERAL时，不会进行HiTraceMeter打点。

type为客户端发送CS和客户端接收CC的信息埋点需配套使用；

type为服务端接收SC和服务端发送SS的信息埋点需配套使用。

否则，HiTraceMeter开始与结束打点无法正常匹配。

[void OH_HiTrace_InitId(HiTraceId *id)](#ZH-CN_TOPIC_0000002497605672__oh_hitrace_initid)初始化HiTraceId。[void OH_HiTrace_IdFromBytes(HiTraceId *id, const uint8_t *pIdArray, int len)](#ZH-CN_TOPIC_0000002497605672__oh_hitrace_idfrombytes)根据字节数组创建HiTraceId。[bool OH_HiTrace_IsIdValid(const HiTraceId *id)](#ZH-CN_TOPIC_0000002497605672__oh_hitrace_isidvalid)判断HiTraceId是否有效。[bool OH_HiTrace_IsFlagEnabled(const HiTraceId *id, HiTrace_Flag flag)](#ZH-CN_TOPIC_0000002497605672__oh_hitrace_isflagenabled)判断HiTraceId是否启用了跟踪标志flag。[void OH_HiTrace_EnableFlag(const HiTraceId *id, HiTrace_Flag flag)](#ZH-CN_TOPIC_0000002497605672__oh_hitrace_enableflag)启用HiTraceId中指定的跟踪标志。[int OH_HiTrace_GetFlags(const HiTraceId *id)](#ZH-CN_TOPIC_0000002497605672__oh_hitrace_getflags)获取HiTraceId中设置的跟踪标志位。[void OH_HiTrace_SetFlags(HiTraceId *id, int flags)](#ZH-CN_TOPIC_0000002497605672__oh_hitrace_setflags)设置跟踪标志位到[HiTraceId](../../topics/input/HiTraceId.md)中。[uint64_t OH_HiTrace_GetChainId(const HiTraceId *id)](#ZH-CN_TOPIC_0000002497605672__oh_hitrace_getchainid)获取HiTraceId中的跟踪链ID。[void OH_HiTrace_SetChainId(HiTraceId *id, uint64_t chainId)](#ZH-CN_TOPIC_0000002497605672__oh_hitrace_setchainid)设置跟踪链ID到HiTraceId中。[uint64_t OH_HiTrace_GetSpanId(const HiTraceId *id)](#ZH-CN_TOPIC_0000002497605672__oh_hitrace_getspanid)获取当前HiTraceId中的分支ID。[void OH_HiTrace_SetSpanId(HiTraceId *id, uint64_t spanId)](#ZH-CN_TOPIC_0000002497605672__oh_hitrace_setspanid)设置分支ID到HiTraceId中。[uint64_t OH_HiTrace_GetParentSpanId(const HiTraceId *id)](#ZH-CN_TOPIC_0000002497605672__oh_hitrace_getparentspanid)获取当前HiTraceId中的父分支ID。[void OH_HiTrace_SetParentSpanId(HiTraceId *id, uint64_t parentSpanId)](#ZH-CN_TOPIC_0000002497605672__oh_hitrace_setparentspanid)设置HiTraceId结构的parentSpanId字符。[int OH_HiTrace_IdToBytes(const HiTraceId* id, uint8_t* pIdArray, int len)](#ZH-CN_TOPIC_0000002497605672__oh_hitrace_idtobytes)将HiTraceId转换为字节数组，用于缓存或者通信传递。[void OH_HiTrace_StartTrace(const char *name)](#ZH-CN_TOPIC_0000002497605672__oh_hitrace_starttrace)

标记一个同步跟踪耗时任务的开始。

 同步跟踪打点接口OH_HiTrace_StartTrace()和OH_HiTrace_FinishTrace()必须配对使用。

 OH_HiTrace_StartTrace()和OH_HiTrace_FinishTrace()函数对可以嵌套使用，跟踪解析时使用栈式数据结构进行匹配。

 从API version 19开始，建议使用OH_HiTrace_StartTraceEx()接口，以便分级控制跟踪输出。

[void OH_HiTrace_FinishTrace(void)](#ZH-CN_TOPIC_0000002497605672__oh_hitrace_finishtrace)

标记一个同步跟踪耗时任务的结束。

 必须和OH_HiTrace_StartTrace()配对使用。跟踪解析时，和其前执行流程中最近的OH_HiTrace_StartTrace()进行匹配。

 从API version 19开始，建议使用OH_HiTrace_FinishTraceEx()接口，以便分级控制跟踪输出。

[void OH_HiTrace_StartAsyncTrace(const char *name, int32_t taskId)](#ZH-CN_TOPIC_0000002497605672__oh_hitrace_startasynctrace)

标记一个异步跟踪耗时任务的开始。

 用于在异步操作前调用进行开始打点，异步跟踪开始和结束数据由于不是顺序发生的，所以解析时需要通过一个唯一的taskId进行识别。

 必须和OH_HiTrace_FinishAsyncTrace()配对使用，参数name和taskId相同的开始与结束打点相匹配，构成一个异步跟踪耗时任务。

 如果有多个相同name的任务需要跟踪或者对同一个任务跟踪多次，并且任务同时被执行，则每次调用的taskId需不相同。

 如果具有相同name的任务是串行执行的，则taskId可以相同。

 从API version 19开始，建议使用OH_HiTrace_StartAsyncTraceEx()接口，以便分级控制跟踪输出与跟踪聚类。

[void OH_HiTrace_FinishAsyncTrace(const char *name, int32_t taskId)](#ZH-CN_TOPIC_0000002497605672__oh_hitrace_finishasynctrace)

标记一个异步跟踪耗时任务的结束。

 在异步操作完成后如回调函数中调用，进行结束打点。

 和OH_HiTrace_StartAsyncTrace()配对使用，参数name和taskId必须与异步跟踪的开始打点接口的对应参数值保持一致。

 从API version 19开始，建议使用OH_HiTrace_FinishAsyncTraceEx()接口，以便分级控制跟踪输出。

[void OH_HiTrace_CountTrace(const char *name, int64_t count)](#ZH-CN_TOPIC_0000002497605672__oh_hitrace_counttrace)

用于跟踪给定整数变量名和整数值。

 多次执行该接口可以跟踪给定整数变量在不同时刻的数值变化。

 从API version 19开始，建议使用OH_HiTrace_CountTraceEx()接口，以便分级控制跟踪输出。

[void OH_HiTrace_StartTraceEx(HiTrace_Output_Level level, const char *name, const char *customArgs)](#ZH-CN_TOPIC_0000002497605672__oh_hitrace_starttraceex)

标记一个同步跟踪耗时任务的开始，分级控制跟踪输出。

 同步跟踪打点接口OH_HiTrace_StartTraceEx()和OH_HiTrace_FinishTraceEx()必须配对使用。

 OH_HiTrace_StartTraceEx()和OH_HiTrace_FinishTraceEx()函数对可以嵌套使用，跟踪解析时使用栈式数据结构进行匹配。

[void OH_HiTrace_FinishTraceEx(HiTrace_Output_Level level)](#ZH-CN_TOPIC_0000002497605672__oh_hitrace_finishtraceex)

标记一个同步跟踪耗时任务的结束，分级控制跟踪输出。

 必须和OH_HiTrace_StartTraceEx()配对使用，参数level必须与同步跟踪的开始打点接口OH_HiTrace_StartTraceEx()的对应参数值一致。

 跟踪数据解析时，和其前执行流程中最近的OH_HiTrace_StartTraceEx()进行匹配。

[void OH_HiTrace_StartAsyncTraceEx(HiTrace_Output_Level level, const char *name, int32_t taskId, const char *customCategory, const char *customArgs)](#ZH-CN_TOPIC_0000002497605672__oh_hitrace_startasynctraceex)

标记一个异步跟踪耗时任务的开始，分级控制跟踪输出。

 用于在异步操作执行前进行开始打点，异步跟踪开始和结束数据由于不是顺序发生的，所以解析时需要通过一个唯一的taskId进行识别。

 和OH_HiTrace_FinishAsyncTraceEx()配对使用，参数name和taskId相同的开始与结束打点相匹配，构成一个异步跟踪耗时任务。

 如果有多个相同name的任务需要跟踪或者对同一个任务跟踪多次，并且任务同时被执行，则每次调用的taskId需不相同。

 如果具有相同name的任务是串行执行的，则taskId可以相同。

 不同进程的taskId不会相互干扰。

[void OH_HiTrace_FinishAsyncTraceEx(HiTrace_Output_Level level, const char *name, int32_t taskId)](#ZH-CN_TOPIC_0000002497605672__oh_hitrace_finishasynctraceex)

标记一个异步跟踪耗时任务的结束，分级控制跟踪输出。

 用于在异步操作完成后进行结束打点，例如在回调函数中调用。

 和OH_HiTrace_StartAsyncTraceEx()配对使用，参数level、name和taskId必须与异步跟踪开始打点接口的对应参数值保持一致。

[void OH_HiTrace_CountTraceEx(HiTrace_Output_Level level, const char *name, int64_t count)](#ZH-CN_TOPIC_0000002497605672__oh_hitrace_counttraceex)标记一个跟踪的整数变量，分级控制跟踪输出。[bool OH_HiTrace_IsTraceEnabled(void)](#ZH-CN_TOPIC_0000002497605672__oh_hitrace_istraceenabled)判断当前是否开启应用trace捕获。

#### 枚举类型说明

#### HiTraceId_Valid

```ets
enum HiTraceId_Valid
```

**描述**

HiTraceId是否有效标志。

**系统能力：** SystemCapability.HiviewDFX.HiTrace

**起始版本：** 12

枚举项描述HITRACE_ID_INVALID = 0

无效HiTraceId。

**起始版本：** 12

**系统能力：** SystemCapability.HiviewDFX.HiTrace

HITRACE_ID_VALID = 1

有效HiTraceId。

**起始版本：** 12

**系统能力：** SystemCapability.HiviewDFX.HiTrace

#### HiTrace_Version

```ets
enum HiTrace_Version
```

**描述**

HiTrace版本号。

**系统能力：** SystemCapability.HiviewDFX.HiTrace

**起始版本：** 12

枚举项描述HITRACE_VER_1 = 0

版本1。

**起始版本：** 12

**系统能力：** SystemCapability.HiviewDFX.HiTrace

#### HiTrace_Flag

```ets
enum HiTrace_Flag
```

**描述**

HiTrace跟踪标志。

**系统能力：** SystemCapability.HiviewDFX.HiTrace

**起始版本：** 12

枚举项描述HITRACE_FLAG_DEFAULT = 0

缺省标志。

**起始版本：** 12

**系统能力：** SystemCapability.HiviewDFX.HiTrace

HITRACE_FLAG_INCLUDE_ASYNC = 1 << 0

异步调用标志。

 设置该标志，同时跟踪同步和异步调用；缺省只跟踪同步调用。

**起始版本：** 12

**系统能力：** SystemCapability.HiviewDFX.HiTrace

HITRACE_FLAG_DONOT_CREATE_SPAN = 1 << 1

无分支标志。

 设置该标志，不创建分支信息；缺省创建分支信息。

**起始版本：** 12

**系统能力：** SystemCapability.HiviewDFX.HiTrace

HITRACE_FLAG_TP_INFO = 1 << 2

埋点标志。

 调试场景下设置该标志，调用信息埋点接口OH_HiTrace_Tracepoint()时，会打印埋点信息hilog日志；缺省不打印埋点信息hilog日志。

**起始版本：** 12

**系统能力：** SystemCapability.HiviewDFX.HiTrace

HITRACE_FLAG_NO_BE_INFO = 1 << 3

无开始结束信息标志。

 调试场景下设置该标志，调用开始跟踪接口OH_HiTrace_BeginChain()和结束跟踪接口OH_HiTrace_EndChain()时，分别会打印开始、结束跟踪信息hilog日志；缺省不打印开始、结束跟踪信息hilog日志。

**起始版本：** 12

**系统能力：** SystemCapability.HiviewDFX.HiTrace

HITRACE_FLAG_DONOT_ENABLE_LOG = 1 << 4

日志关联标志。

 设置该标志，不会在hilog日志中附加HiTraceId信息；缺省会在hilog日志中附加HiTraceId信息。

**起始版本：** 12

**系统能力：** SystemCapability.HiviewDFX.HiTrace

HITRACE_FLAG_FAULT_TRIGGER = 1 << 5

故障触发标志。预置标志，暂未启用。

**起始版本：** 12

**系统能力：** SystemCapability.HiviewDFX.HiTrace

HITRACE_FLAG_D2D_TP_INFO = 1 << 6

设备间埋点标志。HITRACE_FLAG_TP_INFO的一个子集，调试场景下使用。

 当已设置HITRACE_FLAG_TP_INFO标志时，HITRACE_FLAG_D2D_TP_INFO标志不生效；

 当未设置HITRACE_FLAG_TP_INFO标志时，设置HITRACE_FLAG_D2D_TP_INFO标志，此时调用信息埋点接口OH_HiTrace_Tracepoint()，仅当mode参数为设备间通信HITRACE_CM_DEVICE的情况下，会打印埋点信息hilog日志。

**起始版本：** 12

**系统能力：** SystemCapability.HiviewDFX.HiTrace

#### HiTrace_Tracepoint_Type

```ets
enum HiTrace_Tracepoint_Type
```

**描述**

跟踪埋点类型枚举。

**系统能力：** SystemCapability.HiviewDFX.HiTrace

**起始版本：** 12

枚举项描述HITRACE_TP_CS = 0

客户端发送。

**起始版本：** 12

**系统能力：** SystemCapability.HiviewDFX.HiTrace

HITRACE_TP_CR = 1

客户端接收。

**起始版本：** 12

**系统能力：** SystemCapability.HiviewDFX.HiTrace

HITRACE_TP_SS = 2

服务端发送。

**起始版本：** 12

**系统能力：** SystemCapability.HiviewDFX.HiTrace

HITRACE_TP_SR = 3

服务端接收。

**起始版本：** 12

**系统能力：** SystemCapability.HiviewDFX.HiTrace

HITRACE_TP_GENERAL = 4

通用类型，标识HITRACE_TP_CS、HITRACE_TP_CR、HITRACE_TP_SS、HITRACE_TP_SR四种场景之外的埋点。

**起始版本：** 12

**系统能力：** SystemCapability.HiviewDFX.HiTrace

#### HiTrace_Communication_Mode

```ets
enum HiTrace_Communication_Mode
```

**描述**

跟踪通信类型枚举。

**系统能力：** SystemCapability.HiviewDFX.HiTrace

**起始版本：** 12

枚举项描述HITRACE_CM_DEFAULT = 0

缺省通信类型。

**起始版本：** 12

**系统能力：** SystemCapability.HiviewDFX.HiTrace

HITRACE_CM_THREAD = 1

线程间通信。

**起始版本：** 12

**系统能力：** SystemCapability.HiviewDFX.HiTrace

HITRACE_CM_PROCESS = 2

进程间通信。

**起始版本：** 12

**系统能力：** SystemCapability.HiviewDFX.HiTrace

HITRACE_CM_DEVICE = 3

设备间通信。

**起始版本：** 12

**系统能力：** SystemCapability.HiviewDFX.HiTrace

#### HiTrace_Output_Level

```ets
enum HiTrace_Output_Level
```

**描述**

HiTrace输出级别。低于系统跟踪输出级别阈值的打点将不会生效。log版本阈值为HITRACE_LEVEL_INFO；nolog版本阈值为HITRACE_LEVEL_COMMERCIAL。

**系统能力：** SystemCapability.HiviewDFX.HiTrace

**起始版本：** 19

枚举项描述HITRACE_LEVEL_DEBUG = 0

仅用于调试的输出级别，优先级最低。

**起始版本：** 19

HITRACE_LEVEL_INFO = 1

用于log版本的输出级别。

**起始版本：** 19

HITRACE_LEVEL_CRITICAL = 2

用于log版本的输出级别，优先级高于HITRACE_LEVEL_INFO。

**起始版本：** 19

HITRACE_LEVEL_COMMERCIAL = 3

用于nolog版本的输出级别，优先级最高。

**起始版本：** 19

HITRACE_LEVEL_MAX = HITRACE_LEVEL_COMMERCIAL

输出级别范围限制。

**起始版本：** 19

#### 函数说明

#### OH_HiTrace_BeginChain()

```ets
HiTraceId OH_HiTrace_BeginChain(const char *name, int flags)
```

**描述**

开始跟踪。

 当前线程TLS（Thread Local Storage，线程本地存储）中不存在有效的HiTraceId时，生成有效的HiTraceId并设置到当前线程TLS中，返回该HiTraceId。

 当前线程TLS中已存在有效的HiTraceId时，不会开始新的跟踪，返回各属性值均为0的无效HiTraceId。

**系统能力：** SystemCapability.HiviewDFX.HiTrace

**起始版本：** 12

**参数：**

参数项描述const char *name跟踪业务名。int flags跟踪标志组合，见[HiTrace_Flag](trace.h.md#ZH-CN_TOPIC_0000002497605672__hitrace_flag)。

**返回：**

类型说明[HiTraceId](../../topics/input/HiTraceId.md)[HiTraceId](../../topics/input/HiTraceId.md)结构体。

#### OH_HiTrace_EndChain()

```ets
void OH_HiTrace_EndChain()
```

**描述**

结束跟踪。

 结束跟踪并将当前线程TLS中的HiTraceId设置为无效。

**系统能力：** SystemCapability.HiviewDFX.HiTrace

**起始版本：** 12

#### OH_HiTrace_GetId()

```ets
HiTraceId OH_HiTrace_GetId()
```

**描述**

获取跟踪标识。

 获取当前线程TLS中的HiTraceId。

**系统能力：** SystemCapability.HiviewDFX.HiTrace

**起始版本：** 12

**返回：**

类型说明[HiTraceId](../../topics/input/HiTraceId.md)[HiTraceId](../../topics/input/HiTraceId.md)结构体。

#### OH_HiTrace_SetId()

```ets
void OH_HiTrace_SetId(const HiTraceId *id)
```

**描述**

设置跟踪标识。

 将给定的HiTraceId设置到当前线程TLS中。若给定的HiTraceId无效，则不执行任何操作。

**系统能力：** SystemCapability.HiviewDFX.HiTrace

**起始版本：** 12

**参数：**

参数项描述[const HiTraceId](../../topics/input/HiTraceId.md) *id要设置的[HiTraceId](../../topics/input/HiTraceId.md)。

#### OH_HiTrace_ClearId()

```ets
void OH_HiTrace_ClearId(void)
```

**描述**

清除跟踪标识。

 将当前线程TLS中的HiTraceId设置为无效。

**系统能力：** SystemCapability.HiviewDFX.HiTrace

**起始版本：** 12

#### OH_HiTrace_CreateSpan()

```ets
HiTraceId OH_HiTrace_CreateSpan(void)
```

**描述**

创建跟踪分支。

 创建一个HiTraceId，使用当前线程TLS中的chainId、spanId初始化HiTraceId的chainId、parentSpanId，并为HiTraceId生成一个新的spanId，返回该HiTraceId。

**系统能力：** SystemCapability.HiviewDFX.HiTrace

**起始版本：** 12

**返回：**

类型说明[HiTraceId](../../topics/input/HiTraceId.md)[HiTraceId](../../topics/input/HiTraceId.md)结构体。

#### OH_HiTrace_Tracepoint()

```ets
void OH_HiTrace_Tracepoint(HiTrace_Communication_Mode mode, HiTrace_Tracepoint_Type type, const HiTraceId *id, const char *fmt, ...)
```

**描述**

HiTraceMeter跟踪信息埋点。

type为客户端发送CS和服务端接收SC时，进行同步HiTraceMeter开始打点；

type为客户端接收CC和服务端发送SS时，进行同步HiTraceMeter结束打点；

type为通用类型GENERAL时，不会进行HiTraceMeter打点。

type为客户端发送CS和客户端接收CC的信息埋点需配套使用；

type为服务端接收SC和服务端发送SS的信息埋点需配套使用。

否则，HiTraceMeter开始与结束打点无法正常匹配。

**系统能力：** SystemCapability.HiviewDFX.HiTrace

**起始版本：** 12

**参数：**

参数项描述[HiTrace_Communication_Mode](trace.h.md#ZH-CN_TOPIC_0000002497605672__hitrace_communication_mode) mode跟踪通信模式，见[HiTrace_Communication_Mode](trace.h.md#ZH-CN_TOPIC_0000002497605672__hitrace_communication_mode)。[HiTrace_Tracepoint_Type](trace.h.md#ZH-CN_TOPIC_0000002497605672__hitrace_tracepoint_type) type跟踪信息类型，见[HiTrace_Tracepoint_Type](trace.h.md#ZH-CN_TOPIC_0000002497605672__hitrace_tracepoint_type)。[const HiTraceId](../../topics/input/HiTraceId.md) *id实施信息埋点操作的[HiTraceId](../../topics/input/HiTraceId.md)。const char *fmtHiTraceMeter打点操作传入的trace说明信息的格式化字符串。

#### OH_HiTrace_InitId()

```ets
void OH_HiTrace_InitId(HiTraceId *id)
```

**描述**

初始化HiTraceId。

**系统能力：** SystemCapability.HiviewDFX.HiTrace

**起始版本：** 12

**参数：**

参数项描述[HiTraceId](../../topics/input/HiTraceId.md) *id需要初始化的[HiTraceId](../../topics/input/HiTraceId.md)。

#### OH_HiTrace_IdFromBytes()

```ets
void OH_HiTrace_IdFromBytes(HiTraceId *id, const uint8_t *pIdArray, int len)
```

**描述**

根据字节数组创建HiTraceId。

**系统能力：** SystemCapability.HiviewDFX.HiTrace

**起始版本：** 12

**参数：**

参数项描述[HiTraceId](../../topics/input/HiTraceId.md) *id需要创建的[HiTraceId](../../topics/input/HiTraceId.md)。const uint8_t *pIdArray字节数组。int len字节数组长度。

#### OH_HiTrace_IsIdValid()

```ets
bool OH_HiTrace_IsIdValid(const HiTraceId *id)
```

**描述**

判断HiTraceId是否有效。

**系统能力：** SystemCapability.HiviewDFX.HiTrace

**起始版本：** 12

**参数：**

参数项描述[const HiTraceId](../../topics/input/HiTraceId.md) *id需要判断是否有效的[HiTraceId](../../topics/input/HiTraceId.md)。

**返回：**

类型说明booltrue：[HiTraceId](../../topics/input/HiTraceId.md)有效；false：[HiTraceId](../../topics/input/HiTraceId.md)无效。

#### OH_HiTrace_IsFlagEnabled()

```ets
bool OH_HiTrace_IsFlagEnabled(const HiTraceId *id, HiTrace_Flag flag)
```

**描述**

判断HiTraceId是否启用了跟踪标志flag。

**系统能力：** SystemCapability.HiviewDFX.HiTrace

**起始版本：** 12

**参数：**

参数项描述[const HiTraceId](../../topics/input/HiTraceId.md) *id需要判断指定跟踪标志是否启用的[HiTraceId](../../topics/input/HiTraceId.md)。[HiTrace_Flag](trace.h.md#ZH-CN_TOPIC_0000002497605672__hitrace_flag) flag指定的跟踪标志，见[HiTrace_Flag](trace.h.md#ZH-CN_TOPIC_0000002497605672__hitrace_flag)。

**返回：**

类型说明booltrue：[HiTraceId](../../topics/input/HiTraceId.md)已启用flag；false：[HiTraceId](../../topics/input/HiTraceId.md)未启用flag。

#### OH_HiTrace_EnableFlag()

```ets
void OH_HiTrace_EnableFlag(const HiTraceId *id, HiTrace_Flag flag)
```

**描述**

启用HiTraceId中指定的跟踪标志。

**系统能力：** SystemCapability.HiviewDFX.HiTrace

**起始版本：** 12

**参数：**

参数项描述[const HiTraceId](../../topics/input/HiTraceId.md) *id需要启用指定跟踪标志的[HiTraceId](../../topics/input/HiTraceId.md)。[HiTrace_Flag](trace.h.md#ZH-CN_TOPIC_0000002497605672__hitrace_flag) flag指定的跟踪标志，见[HiTrace_Flag](trace.h.md#ZH-CN_TOPIC_0000002497605672__hitrace_flag)。

#### OH_HiTrace_GetFlags()

```ets
int OH_HiTrace_GetFlags(const HiTraceId *id)
```

**描述**

获取HiTraceId中设置的跟踪标志位。

**系统能力：** SystemCapability.HiviewDFX.HiTrace

**起始版本：** 12

**参数：**

参数项描述[const HiTraceId](../../topics/input/HiTraceId.md) *id需要获取跟踪标志位的[HiTraceId](../../topics/input/HiTraceId.md)。

**返回：**

类型说明int[HiTraceId](../../topics/input/HiTraceId.md)中设置的跟踪标志位。

#### OH_HiTrace_SetFlags()

```ets
void OH_HiTrace_SetFlags(HiTraceId *id, int flags)
```

**描述**

设置跟踪标志位到[HiTraceId](../../topics/input/HiTraceId.md)中。

**系统能力：** SystemCapability.HiviewDFX.HiTrace

**起始版本：** 12

**参数：**

参数项描述[HiTraceId](../../topics/input/HiTraceId.md) *id需要设置跟踪标志位的[HiTraceId](../../topics/input/HiTraceId.md)。int flags指定的跟踪标志位，见[HiTrace_Flag](trace.h.md#ZH-CN_TOPIC_0000002497605672__hitrace_flag)。

#### OH_HiTrace_GetChainId()

```ets
uint64_t OH_HiTrace_GetChainId(const HiTraceId *id)
```

**描述**

获取HiTraceId中的跟踪链ID。

**系统能力：** SystemCapability.HiviewDFX.HiTrace

**起始版本：** 12

**参数：**

参数项描述[const HiTraceId](../../topics/input/HiTraceId.md) *id需要获取跟踪链ID的[HiTraceId](../../topics/input/HiTraceId.md)。

**返回：**

类型说明uint64_t跟踪链ID。

#### OH_HiTrace_SetChainId()

```ets
void OH_HiTrace_SetChainId(HiTraceId *id, uint64_t chainId)
```

**描述**

设置跟踪链ID到HiTraceId中。

**系统能力：** SystemCapability.HiviewDFX.HiTrace

**起始版本：** 12

**参数：**

参数项描述[HiTraceId](../../topics/input/HiTraceId.md) *id需要设置跟踪链ID的[HiTraceId](../../topics/input/HiTraceId.md)。uint64_t chainId需要设置的跟踪链ID。

#### OH_HiTrace_GetSpanId()

```ets
uint64_t OH_HiTrace_GetSpanId(const HiTraceId *id)
```

**描述**

获取当前HiTraceId中的分支ID。

**系统能力：** SystemCapability.HiviewDFX.HiTrace

**起始版本：** 12

**参数：**

参数项描述[const HiTraceId](../../topics/input/HiTraceId.md) *id需要获取分支ID的[HiTraceId](../../topics/input/HiTraceId.md)。

**返回：**

类型说明uint64_t[HiTraceId](../../topics/input/HiTraceId.md)中设置的分支ID。

#### OH_HiTrace_SetSpanId()

```ets
void OH_HiTrace_SetSpanId(HiTraceId *id, uint64_t spanId)
```

**描述**

设置分支ID到HiTraceId中。

**系统能力：** SystemCapability.HiviewDFX.HiTrace

**起始版本：** 12

**参数：**

参数项描述[HiTraceId](../../topics/input/HiTraceId.md) *id需要设置分支ID的[HiTraceId](../../topics/input/HiTraceId.md)。uint64_t spanId需要设置的分支ID。

#### OH_HiTrace_GetParentSpanId()

```ets
uint64_t OH_HiTrace_GetParentSpanId(const HiTraceId *id)
```

**描述**

获取当前HiTraceId中的父分支ID。

**系统能力：** SystemCapability.HiviewDFX.HiTrace

**起始版本：** 12

**参数：**

参数项描述[const HiTraceId](../../topics/input/HiTraceId.md) *id需要获取父分支ID的[HiTraceId](../../topics/input/HiTraceId.md)。

**返回：**

类型说明uint64_t[HiTraceId](../../topics/input/HiTraceId.md)中设置的父分支ID。

#### OH_HiTrace_SetParentSpanId()

```ets
void OH_HiTrace_SetParentSpanId(HiTraceId *id, uint64_t parentSpanId)
```

**描述**

设置HiTraceId结构的parentSpanId字符。

**系统能力：** SystemCapability.HiviewDFX.HiTrace

**起始版本：** 12

**参数：**

参数项描述[HiTraceId](../../topics/input/HiTraceId.md) *id需要设置父分支ID的[HiTraceId](../../topics/input/HiTraceId.md)。uint64_t parentSpanId需要设置的父分支ID。

#### OH_HiTrace_IdToBytes()

```ets
int OH_HiTrace_IdToBytes(const HiTraceId* id, uint8_t* pIdArray, int len)
```

**描述**

将HiTraceId转换为字节数组，用于缓存或者通信传递。

**系统能力：** SystemCapability.HiviewDFX.HiTrace

**起始版本：** 12

**参数：**

参数项描述[const HiTraceId](../../topics/input/HiTraceId.md)* id需要转换的[HiTraceId](../../topics/input/HiTraceId.md)。uint8_t* pIdArray字节数组。int len字节数组长度。

**返回：**

类型说明int转换后的字节数组长度。

#### OH_HiTrace_StartTrace()

```ets
void OH_HiTrace_StartTrace(const char *name)
```

**描述**

标记一个同步跟踪耗时任务的开始。

 同步跟踪打点接口OH_HiTrace_StartTrace()和OH_HiTrace_FinishTrace()必须配对使用。

 OH_HiTrace_StartTrace()和OH_HiTrace_FinishTrace()函数对可以嵌套使用，跟踪解析时使用栈式数据结构进行匹配。

 从API version 19开始，建议使用OH_HiTrace_StartTraceEx()接口，以便分级控制跟踪输出。

**系统能力：** SystemCapability.HiviewDFX.HiTrace

**起始版本：** 10

**参数：**

参数项描述const char *name跟踪的名字。

#### OH_HiTrace_FinishTrace()

```ets
void OH_HiTrace_FinishTrace(void)
```

**描述**

标记一个同步跟踪耗时任务的结束。

 必须和OH_HiTrace_StartTrace()配对使用。跟踪解析时，和其前执行流程中最近的OH_HiTrace_StartTrace()进行匹配。

 从API version 19开始，建议使用OH_HiTrace_FinishTraceEx()接口，以便分级控制跟踪输出。

**系统能力：** SystemCapability.HiviewDFX.HiTrace

**起始版本：** 10

#### OH_HiTrace_StartAsyncTrace()

```ets
void OH_HiTrace_StartAsyncTrace(const char *name, int32_t taskId)
```

**描述**

标记一个异步跟踪耗时任务的开始。

 用于在异步操作前调用进行开始打点，异步跟踪开始和结束数据由于不是顺序发生的，所以解析时需要通过一个唯一的taskId进行识别。

 必须和OH_HiTrace_FinishAsyncTrace()配对使用，参数name和taskId相同的开始与结束打点相匹配，构成一个异步跟踪耗时任务。

 如果有多个相同name的任务需要跟踪或者对同一个任务跟踪多次，并且任务同时被执行，则每次调用的taskId需不相同。

 如果具有相同name的任务是串行执行的，则taskId可以相同。

 从API version 19开始，建议使用OH_HiTrace_StartAsyncTraceEx()接口，以便分级控制跟踪输出与跟踪聚类。

**系统能力：** SystemCapability.HiviewDFX.HiTrace

**起始版本：** 10

**参数：**

参数项描述const char *name异步跟踪的名字。int32_t taskId异步跟踪的ID。 异步跟踪开始和结束由于不是顺序发生的，所以需要通过name和每次执行唯一的taskId进行开始和结束的匹配。

#### OH_HiTrace_FinishAsyncTrace()

```ets
void OH_HiTrace_FinishAsyncTrace(const char *name, int32_t taskId)
```

**描述**

标记一个异步跟踪耗时任务的结束。

 在异步操作完成后如回调函数中调用，进行结束打点。

 和OH_HiTrace_StartAsyncTrace()配对使用，参数name和taskId必须与异步跟踪的开始打点接口的对应参数值保持一致。

 从API version 19开始，建议使用OH_HiTrace_FinishAsyncTraceEx()接口，以便分级控制跟踪输出。

**系统能力：** SystemCapability.HiviewDFX.HiTrace

**起始版本：** 10

**参数：**

参数项描述const char *name异步跟踪的名字。int32_t taskId异步跟踪的ID。异步跟踪开始和结束由于不是顺序发生的，所以需要通过name和每次执行唯一的taskId进行开始和结束的匹配。

#### OH_HiTrace_CountTrace()

```ets
void OH_HiTrace_CountTrace(const char *name, int64_t count)
```

**描述**

用于跟踪给定整数变量名和整数值。

 多次执行该接口可以跟踪给定整数变量在不同时刻的数值变化。

 从API version 19开始，建议使用OH_HiTrace_CountTraceEx()接口，以便分级控制跟踪输出。

**系统能力：** SystemCapability.HiviewDFX.HiTrace

**起始版本：** 10

**参数：**

参数项描述const char *name整数变量跟踪的名字，不必与真实变量名相同。int64_t count整数值。

#### OH_HiTrace_StartTraceEx()

```ets
void OH_HiTrace_StartTraceEx(HiTrace_Output_Level level, const char *name, const char *customArgs)
```

**描述**

标记一个同步跟踪耗时任务的开始，分级控制跟踪输出。

 同步跟踪打点接口OH_HiTrace_StartTraceEx()和OH_HiTrace_FinishTraceEx()必须配对使用。

 OH_HiTrace_StartTraceEx()和OH_HiTrace_FinishTraceEx()函数对可以嵌套使用，跟踪解析时使用栈式数据结构进行匹配。

**起始版本：** 19

**参数：**

参数项描述[HiTrace_Output_Level](trace.h.md#ZH-CN_TOPIC_0000002497605672__hitrace_output_level) level跟踪输出优先级。const char *name同步跟踪的名字。const char *customArgs键值对，多个键值对使用逗号分隔，例"key1=value1,key2=value2"。

#### OH_HiTrace_FinishTraceEx()

```ets
void OH_HiTrace_FinishTraceEx(HiTrace_Output_Level level)
```

**描述**

标记一个同步跟踪耗时任务的结束，分级控制跟踪输出。

 必须和OH_HiTrace_StartTraceEx()配对使用，参数level必须与同步跟踪的开始打点接口OH_HiTrace_StartTraceEx()的对应参数值一致。

 跟踪数据解析时，和其前执行流程中最近的OH_HiTrace_StartTraceEx()进行匹配。

**起始版本：** 19

**参数：**

参数项描述[HiTrace_Output_Level](trace.h.md#ZH-CN_TOPIC_0000002497605672__hitrace_output_level) level跟踪输出优先级。

#### OH_HiTrace_StartAsyncTraceEx()

```ets
void OH_HiTrace_StartAsyncTraceEx(HiTrace_Output_Level level, const char *name, int32_t taskId, const char *customCategory, const char *customArgs)
```

**描述**

标记一个异步跟踪耗时任务的开始，分级控制跟踪输出。

 用于在异步操作执行前进行开始打点，异步跟踪开始和结束数据由于不是顺序发生的，所以解析时需要通过一个唯一的taskId进行识别。

 和OH_HiTrace_FinishAsyncTraceEx()配对使用，参数name和taskId相同的开始与结束打点相匹配，构成一个异步跟踪耗时任务。

 如果有多个相同name的任务需要跟踪或者对同一个任务跟踪多次，并且任务同时被执行，则每次调用的taskId需不相同。

 如果具有相同name的任务是串行执行的，则taskId可以相同。

 不同进程的taskId不会相互干扰。

**起始版本：** 19

**参数：**

参数项描述[HiTrace_Output_Level](trace.h.md#ZH-CN_TOPIC_0000002497605672__hitrace_output_level) level跟踪输出优先级。const char *name异步跟踪的名字。int32_t taskId异步跟踪的ID。const char *customCategory自定义聚类名称，用于聚合同一类异步跟踪打点。const char *customArgs键值对，多个键值对使用逗号分隔，例"key1=value1,key2=value2"。

#### OH_HiTrace_FinishAsyncTraceEx()

```ets
void OH_HiTrace_FinishAsyncTraceEx(HiTrace_Output_Level level, const char *name, int32_t taskId)
```

**描述**

标记一个异步跟踪耗时任务的结束，分级控制跟踪输出。

 用于在异步操作完成后进行结束打点，例如在回调函数中调用。

 和OH_HiTrace_StartAsyncTraceEx()配对使用，参数level、name和taskId必须与异步跟踪开始打点接口的对应参数值保持一致。

**起始版本：** 19

**参数：**

参数项描述[HiTrace_Output_Level](trace.h.md#ZH-CN_TOPIC_0000002497605672__hitrace_output_level) level跟踪输出优先级。const char *name异步跟踪的名字。int32_t taskId异步跟踪的ID。

#### OH_HiTrace_CountTraceEx()

```ets
void OH_HiTrace_CountTraceEx(HiTrace_Output_Level level, const char *name, int64_t count)
```

**描述**

标记一个跟踪的整数变量，分级控制跟踪输出。

**起始版本：** 19

**参数：**

参数项描述[HiTrace_Output_Level](trace.h.md#ZH-CN_TOPIC_0000002497605672__hitrace_output_level) level跟踪输出优先级。const char *name整数变量的名称，不必与实际变量名相同。int64_t count整数值。

#### OH_HiTrace_IsTraceEnabled()

```ets
bool OH_HiTrace_IsTraceEnabled(void)
```

**描述**

判断当前是否开启应用trace捕获。

**起始版本：** 19

**返回：**

类型说明bool

使用hitrace命令行工具等方式开启采集时返回true。

 未开启采集或停止采集后返回false，此时调用HiTraceMeter性能跟踪打点接口无效。